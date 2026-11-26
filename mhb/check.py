"""The checks of `mhb check`.

A fault fails the check:
- the map (tamnd/mmp) is not found;
- a volume has no volume.yaml, or the file has no title; its `level` is not a level of spec 11.3; a key of its
  `requires` does not resolve;
- a section has a `level` that is not guide, prereq, background, core, advanced or research, or a `kind` that is
  not theorem, background or survey; a section of a level other than guide has no `kind`;
- a key of `requires` does not resolve: it must be P0 to P8 or 0 to 17, alone or with a chapter of the plan
  (P5.6, 3.4);
- a key of `reads_with` is not `<paper>:<place>` with a paper of the map;
- a section with a `kind` does not have its parts as ### headings, in the order Statement, Proof in words,
  Examples, Exercises, Lean, Notes and history. A theorem section has all six. A background section may leave
  out Proof in words. A survey section may leave out Exercises;
- an exercise (a numbered item under an Exercises or Problems heading, or in problems.md) does not start with
  its grade (A), (B) or (C), with (M) after it when it needs a computer;
- a section names a node whose literature state is conjecture, claimed or refuted, or whose status is open or
  claimed, and its text does not say so in words ("open" or "conjecture", "claimed", "refuted");
- a section has no title, no status, a status that is not drafted, checked or reviewed, no drafted_by, or the
  status reviewed with an empty reviewed_by;
- a section does not open with a ## heading;
- a tag in `nodes` or on a Node line is not a node of the map;
- a key in `sources` is not a paper of the map;
- a line starts with "Node:" and does not have the form of a Node line;
- a Node line marks a Lean name as "the statement only", and records/lean.json exists and does not have
  the name;
- an en dash, an em dash or a word of the banned list in the prose.

A warning does not fail the check:
- a volume.yaml has no level, requires or spine;
- a theorem section has fewer than 3 or more than 8 exercises;
- a tag on a Node line is not in the `nodes` of its section;
- the Lean name on a Node line is not the lean.statement or lean.proof of the node;
- a theorem, proposition, lemma or corollary has no Node line and no Lean line under it.
"""

from __future__ import annotations

import os
import re

from .content import KINDS, LEVELS, M_VOLUMES, P_CHAPTERS, STATUSES, Volume, front, read
from .map import Map
from .md import _FENCE, _STMT, NODE

BANNED = (r"\b(leverag(?:e|es|ed|ing)|showcas(?:e|es|ed|ing)|powerful|elegant(?:ly)?|seamless(?:ly)?|crucial(?:ly)?|"
          r"delv(?:e|es|ed|ing)|journey|landscape|tapestry|realm|intricate|pivotal|robust|underscores?|"
          r"notably|furthermore|moreover)\b")
_ANY_NODE = re.compile(r"^(?:>\s*)?Node:\s*([^\s·,;]+)")


def _prose(t: str) -> str:
    p = re.sub(r"```.*?```|\$\$.*?\$\$|\$[^$\n]*\$|`[^`\n]*`", " ", t, flags=re.S)
    return re.sub(r"\]\([^)]*\)", "]", p)


def _style(rel: str, text: str, faults: list[str]):
    prose = _prose(text)
    for w in sorted(set(re.findall(BANNED, prose, flags=re.I))):
        faults.append(f"{rel}: style: the word '{w}'")
    if re.search("[\u2013\u2014]", prose):
        faults.append(f"{rel}: style: an en dash or an em dash")


def _body(rel: str, body: str, offset: int, fm_nodes: set, smap: Map, faults: list[str], warns: list[str]):
    fence = None
    open_stmt = None     # (line, kind) of a theorem-like statement with no Node line yet
    for i, ln in enumerate(body.split("\n"), offset):
        f = _FENCE.match(ln)
        if f:
            fence = None if fence == f.group(1)[0] else (fence or f.group(1)[0])
            continue
        if fence:
            continue
        sm = _STMT.match(ln)
        if sm or ln.startswith("#"):
            if open_stmt:
                warns.append(f"{rel}:{open_stmt[0]}: {open_stmt[1]} with no Node line")
            open_stmt = (i, sm.group(1)) if sm and sm.group(1) in ("Theorem", "Proposition", "Lemma",
                                                                    "Corollary") else None
            continue
        if re.match(r"^\*?Lean:", ln):
            open_stmt = None
            continue
        a = _ANY_NODE.match(ln)
        if not a and re.match(r"^(?:>\s*)?Node:", ln):
            faults.append(f"{rel}:{i}: a Node line without a tag")
            continue
        if not a:
            continue
        tag = a.group(1)
        quoted = ln.startswith(">")
        if not quoted:
            open_stmt = None
            if not NODE.match(ln):
                faults.append(f"{rel}:{i}: a Node line not of the form 'Node: TAG · Lean: `Name`'")
        node = smap.nodes.get(tag)
        if node is None:
            faults.append(f"{rel}:{i}: the node {tag} is not in the map")
            continue
        if quoted:
            continue
        if tag not in fm_nodes:
            warns.append(f"{rel}:{i}: the node {tag} is not in the nodes of the front matter")
        names = re.findall(r"`([^`]+)`", ln)
        known = {n for n in (node.statement, node.proof) if n}
        for nm in names:
            if known and nm not in known:
                warns.append(f"{rel}:{i}: the Lean name {nm} is not the Lean name of {tag} in the map "
                             f"({', '.join(sorted(known))})")
        if smap.records is not None and "statement only" in ln:
            for nm in names:
                if nm not in smap.records:
                    faults.append(f"{rel}:{i}: the Lean name {nm} is marked as a statement, but it is not in "
                                  f"records/lean.json")
    if open_stmt:
        warns.append(f"{rel}:{open_stmt[0]}: {open_stmt[1]} with no Node line")


PARTS = ("Statement", "Proof in words", "Examples", "Exercises", "Lean", "Notes and history")
OPTIONAL = {"theorem": set(), "background": {"Proof in words"}, "survey": {"Exercises"}}
_GRADE = re.compile(r"^\d+\.\s+\((A|B|C)\)(?:\s+\(M\))?\s")
_REQ = re.compile(r"^(P[0-8]|[0-9]{1,2})(?:\.([0-9]{1,2}))?$")
_READS = re.compile(r"^([A-Za-z][A-Za-z0-9+_-]*):(\S.*)$")
# The words that a section must have when it names a node in each state.
_SAYS = {"conjecture": ("open", "conjecture"), "open": ("open", "conjecture"), "claimed": ("claimed",),
         "claim": ("claimed",), "refuted": ("refuted",)}


def requires_ok(key: str) -> bool:
    """A key of `requires`: P0 to P8 or 0 to 17, alone or with a chapter that the plan has."""
    m = _REQ.match(key)
    if not m:
        return False
    vol, ch = m.group(1), m.group(2)
    if vol.startswith("P"):
        return ch is None or 1 <= int(ch) <= P_CHAPTERS[vol]
    return int(vol) in M_VOLUMES and (ch is None or int(ch) >= 1)


def _headings(body: str) -> list[tuple[int, int, str]]:
    """The headings of a body outside code: (line index, level, text)."""
    out, fence = [], None
    for i, ln in enumerate(body.split("\n")):
        f = _FENCE.match(ln)
        if f:
            fence = None if fence == f.group(1)[0] else (fence or f.group(1)[0])
            continue
        if fence:
            continue
        m = re.match(r"^(#{1,6}) +(.*?)\s*$", ln)
        if m:
            out.append((i, len(m.group(1)), m.group(2)))
    return out


def _parts(rel: str, kind: str, body: str, faults: list[str]):
    """The six parts of spec 11.3, as ### headings in this order."""
    found = [t for _, lv, t in _headings(body) if lv == 3 and t in PARTS]
    need = [p for p in PARTS if p not in OPTIONAL.get(kind, set())]
    for p in need:
        if p not in found:
            faults.append(f"{rel}: a {kind} section has no part '### {p}'")
    order = [PARTS.index(t) for t in found]
    if order != sorted(order) or len(set(found)) != len(found):
        faults.append(f"{rel}: the parts are not in the order {', '.join(PARTS)}")


def exercises(body: str, whole: bool = False) -> list[tuple[int, str]]:
    """The numbered items under an Exercises or Problems heading (or in all of `body` when `whole`)."""
    out, fence, inside = [], None, whole
    for i, ln in enumerate(body.split("\n")):
        f = _FENCE.match(ln)
        if f:
            fence = None if fence == f.group(1)[0] else (fence or f.group(1)[0])
            continue
        if fence:
            continue
        m = re.match(r"^(#{1,6}) +(.*?)\s*$", ln)
        if m:
            inside = whole or m.group(2).strip() in ("Exercises", "Problems")
            continue
        if inside and re.match(r"^\d+\.\s", ln):
            out.append((i, ln))
    return out


def _grades(rel: str, body: str, offset: int, faults: list[str], whole: bool = False) -> int:
    items = exercises(body, whole)
    for i, ln in items:
        if not _GRADE.match(ln):
            faults.append(f"{rel}:{i + offset}: an exercise with no grade (A), (B) or (C)")
    return len(items)


def _says(rel: str, body: str, tags: set, smap: Map, faults: list[str]):
    """The text never claims more than the status (spec 11.3)."""
    prose = _prose(body).lower()
    for t in sorted(tags):
        if t not in smap.nodes:
            continue
        for state in {smap.literature(t), smap.status(t), smap.nodes[t].kind}:
            words = _SAYS.get(state)
            if words and not any(re.search(r"\b" + w, prose) for w in words):
                faults.append(f"{rel}: the node {t} is {state}, and the text does not say "
                              f"{' or '.join(repr(w) for w in words)}")


def _volume_meta(vrel: str, v: Volume, faults: list[str], warns: list[str]):
    for k in ("level", "requires", "spine"):
        if k not in v.meta:
            warns.append(f"{vrel}/volume.yaml: no {k}")
    if v.level and v.level not in LEVELS:
        faults.append(f"{vrel}/volume.yaml: the level '{v.level}' is not one of {', '.join(LEVELS)}")
    for r in v.requires:
        if not requires_ok(r):
            faults.append(f"{vrel}/volume.yaml: the requires key '{r}' does not resolve")


def _keys(rel: str, s, smap: Map, faults: list[str]):
    lv = s.fm.get("level")
    if lv and str(lv) not in LEVELS:
        faults.append(f"{rel}: the level '{lv}' is not one of {', '.join(LEVELS)}")
    kind = s.kind
    if kind and kind not in KINDS:
        faults.append(f"{rel}: the kind '{kind}' is not one of {', '.join(KINDS)}")
    if not kind and s.level != "guide":
        faults.append(f"{rel}: the front matter has no kind (a section of level {s.level or 'none'})")
    for r in s.requires:
        if not requires_ok(r):
            faults.append(f"{rel}: the requires key '{r}' does not resolve")
    for r in s.reads_with:
        m = _READS.match(r)
        if not m:
            faults.append(f"{rel}: the reads_with key '{r}' is not of the form paper:place")
        elif smap.exists and m.group(1) not in smap.papers:
            faults.append(f"{rel}: the reads_with paper {m.group(1)} is not a paper of the map")


def check(volumes: list[Volume], smap: Map, root: str) -> tuple[list[str], list[str]]:
    faults: list[str] = []
    warns: list[str] = []
    if not smap.exists:
        faults.append(f"the map is not found at {smap.root} (give it with --map PATH)")
    for v in volumes:
        vrel = os.path.relpath(v.dir, root)
        vy = os.path.join(v.dir, "volume.yaml")
        if not os.path.exists(vy):
            faults.append(f"{vrel}: no volume.yaml")
        else:
            if not v.meta.get("title"):
                faults.append(f"{vrel}/volume.yaml: no title")
            _volume_meta(vrel, v, faults, warns)
        p = os.path.join(v.dir, "intro.md")
        if os.path.exists(p):
            _style(os.path.relpath(p, root), read(p), faults)
        for ch in v.chapters:
            ip = os.path.join(ch.dir, "intro.md")
            if os.path.exists(ip):
                _style(os.path.relpath(ip, root), read(ip), faults)
            pp = os.path.join(ch.dir, "problems.md")
            if os.path.exists(pp):
                prel = os.path.relpath(pp, root)
                ptext = read(pp)
                _style(prel, ptext, faults)
                pfm, pbody = front(ptext)
                _grades(prel, pbody, ptext[:len(ptext) - len(pbody)].count("\n") + 1, faults, whole=True)
            for s in ch.sections:
                rel = os.path.relpath(s.path, root)
                text = read(s.path)
                fm, body = front(text)
                offset = text[:len(text) - len(body)].count("\n") + 1
                _style(rel, text, faults)
                for k in ("title", "status", "drafted_by"):
                    if not fm.get(k):
                        faults.append(f"{rel}: the front matter has no {k}")
                st = fm.get("status")
                if st and st not in STATUSES:
                    faults.append(f"{rel}: the status '{st}' is not one of {', '.join(STATUSES)}")
                if st == "reviewed" and not fm.get("reviewed_by"):
                    faults.append(f"{rel}: the status is reviewed and reviewed_by is empty")
                if not re.match(r"\s*## ", body):
                    faults.append(f"{rel}: a section must open with a ## heading")
                fm_nodes = {str(t) for t in fm.get("nodes") or []}
                for t in sorted(fm_nodes):
                    if smap.exists and t not in smap.nodes:
                        faults.append(f"{rel}: the node {t} of the front matter is not in the map")
                for k in fm.get("sources") or []:
                    if smap.exists and str(k) not in smap.papers:
                        faults.append(f"{rel}: the source {k} is not a paper of the map")
                _keys(rel, s, smap, faults)
                if s.kind in KINDS:
                    _parts(rel, s.kind, body, faults)
                n_ex = _grades(rel, body, offset, faults)
                if s.kind == "theorem" and not 3 <= n_ex <= 8:
                    warns.append(f"{rel}: a theorem section with {n_ex} exercises (spec 11.3 asks for 3 to 8)")
                if smap.exists:
                    _body(rel, body, offset, fm_nodes, smap, faults, warns)
                    line_tags = {a.group(1) for a in map(_ANY_NODE.match, body.split("\n")) if a}
                    _says(rel, body, fm_nodes | line_tags, smap, faults)
    return faults, warns
