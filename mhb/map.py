"""The map of tamnd/mmp: the nodes of the blueprint, the paper records and the Lean records.

    blueprint/nodes/MM*.yaml   tag, kind, title, lean.statement, lean.proof, hypotheses, literature
    papers/<Key>.yaml          key, title, authors, year, arxiv
    records/status.json        the status and the literature state of each node (optional, written by mmp status)
    records/lean.json          the Lean declarations that exist (optional)

The folder books/ of the handbook holds the records of the books and papers that the map does not have yet. A
record of the map wins over a record of books/ with the same key.

The status of a node comes from records/status.json when it has the node. Otherwise it is computed here, in a
simple form. With no records/lean.json, or with a node whose Lean statement is not in it, the status is
"unstated". records/lean.json is read in one of these forms:

    {"declarations": {"MinimalModel.foo": {...}, ...}}
    {"decls": {"MinimalModel.foo": {...}, ...}}           (the form that tamnd/mmp-lean writes)
    {"MinimalModel.foo": {...}, ...}
    [{"name": "MinimalModel.foo", ...}, ...]

A record is a status string, or an object that can have "status" (used as it is) and "sorry" (true when the
proof is not finished). records/status.json is {"nodes": {TAG: {...}}} or {TAG: {...}}, where a value is a
status string or an object with "status" and "literature".

The literature state of a node (theorem, claimed, conjecture or refuted) is independent of its Lean status. It
comes from records/status.json, then from the key `literature` of the node, then from its kind.
"""

from __future__ import annotations

import glob
import json
import os
import subprocess
from dataclasses import dataclass, field

import yaml

from .content import read

SITE = "https://mmp.tamnd.com"

LITERATURE = ("theorem", "claimed", "conjecture", "refuted")
_KIND_LITERATURE = {"conjecture": "conjecture", "claim": "claimed", "theorem": "theorem", "lemma": "theorem",
                     "reduction": "theorem", "example": "theorem", "counterexample": "theorem"}


def node_url(tag: str) -> str:
    return f"{SITE}/node/{tag}/"


def commit(path: str) -> str:
    try:
        return subprocess.run(["git", "-C", path, "rev-parse", "HEAD"], capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:
        return ""


@dataclass
class Node:
    tag: str
    kind: str
    title: str
    statement: str    # the Lean name of the statement, "" if none
    proof: str        # the Lean name of the proof, "" if none
    hypotheses: list = field(default_factory=list)   # the tags of the named hypotheses that the proof takes
    literature: str = ""   # the key `literature` of the node, if any


@dataclass
class Paper:
    key: str
    title: str
    authors: list
    year: str
    arxiv: list

    def cite(self) -> str:
        """One line of a list of references, in Markdown."""
        bits = []
        if self.authors:
            bits.append(", ".join(str(a) for a in self.authors))
        bits.append(self.title)
        if self.year and str(self.year) not in self.title:
            bits.append(str(self.year))
        s = ". ".join(b.rstrip(".") for b in bits if b) + "."
        for a in self.arxiv:
            s += f" <https://arxiv.org/abs/{a}>"
        return s


@dataclass
class Map:
    root: str
    nodes: dict[str, Node] = field(default_factory=dict)
    papers: dict[str, Paper] = field(default_factory=dict)
    records: dict[str, object] | None = None   # None: no records/lean.json
    status_records: dict[str, object] = field(default_factory=dict)   # records/status.json

    @property
    def exists(self) -> bool:
        return os.path.isdir(os.path.join(self.root, "blueprint", "nodes"))

    @classmethod
    def load(cls, root: str, books: str = "") -> "Map":
        """Read the map at `root`. The records of `books` (a folder of paper records) fill the keys that the map lacks."""
        m = cls(root)
        for p in sorted(glob.glob(os.path.join(root, "blueprint", "nodes", "MM*.yaml"))):
            y = yaml.safe_load(read(p)) or {}
            lean = y.get("lean") or {}
            tag = str(y.get("tag") or os.path.basename(p)[:-5])
            m.nodes[tag] = Node(tag, str(y.get("kind") or ""), str(y.get("title") or ""),
                                str(lean.get("statement") or ""), str(lean.get("proof") or ""),
                                [str(h) for h in y.get("hypotheses") or []], str(y.get("literature") or ""))
        paths = sorted(glob.glob(os.path.join(root, "papers", "*.yaml")))
        if books:
            paths += sorted(glob.glob(os.path.join(books, "*.yaml")))
        for p in paths:
            y = yaml.safe_load(read(p)) or {}
            key = str(y.get("key") or os.path.basename(p)[:-5])
            if key in m.papers:
                continue
            arxiv = y.get("arxiv") or []
            m.papers[key] = Paper(key, str(y.get("title") or key), list(y.get("authors") or []),
                                  str(y.get("year") or ""), [str(a) for a in (arxiv if isinstance(arxiv, list) else [arxiv])])
        rp = os.path.join(root, "records", "lean.json")
        if os.path.exists(rp):
            m.records = _records(json.loads(read(rp)))
        sp = os.path.join(root, "records", "status.json")
        if os.path.exists(sp):
            data = json.loads(read(sp))
            if isinstance(data, dict) and isinstance(data.get("nodes"), dict):
                data = data["nodes"]
            m.status_records = data if isinstance(data, dict) else {}
        return m

    def commit(self) -> str:
        return commit(self.root)

    def literature(self, tag: str) -> str:
        """The literature state: theorem, claimed, conjecture or refuted; "" for a definition."""
        rec = self.status_records.get(tag)
        if isinstance(rec, dict) and rec.get("literature"):
            return str(rec["literature"])
        n = self.nodes.get(tag)
        if n is None:
            return ""
        if n.literature:
            return n.literature
        return _KIND_LITERATURE.get(n.kind, "")

    def status(self, tag: str) -> str:
        rec = self.status_records.get(tag)
        if isinstance(rec, str) and rec:
            return rec
        if isinstance(rec, dict) and rec.get("status"):
            return str(rec["status"])
        n = self.nodes.get(tag)
        if n is not None and n.kind == "claim" and (self.records is None or n.statement not in self.records):
            return "claimed"
        if n is None or self.records is None or not n.statement or n.statement not in self.records:
            return "unstated"
        rec = self.records[n.statement]
        if isinstance(rec, str) and rec:
            return rec
        if isinstance(rec, dict) and rec.get("status"):
            return str(rec["status"])
        if n.proof and n.proof in self.records:
            prec = self.records[n.proof]
            if not (isinstance(prec, dict) and prec.get("sorry")):
                return "proved-mod" if n.hypotheses else "proved"
        if n.kind == "conjecture":
            return "open"
        return "claimed" if n.kind == "claim" else "stated"


def _records(data) -> dict:
    for key in ("declarations", "decls"):
        if isinstance(data, dict) and isinstance(data.get(key), (dict, list)):
            data = data[key]
            break
    if isinstance(data, list):
        out = {}
        for r in data:
            if isinstance(r, str):
                out[r] = {}
            elif isinstance(r, dict) and r.get("name"):
                out[str(r["name"])] = r
        return out
    if isinstance(data, dict):
        return data
    return {}
