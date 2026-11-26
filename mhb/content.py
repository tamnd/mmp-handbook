"""The content of the handbook: content/<id>-<slug>/<NN-chapter>/ with an intro.md, one file NN-<slug>.md per
section and an optional problems.md.

The id of a volume is p0 to p8 for the prerequisites and 00 to 17 for the program. The label of a volume is P0 to
P8 or 0 to 17. A volume folder has a volume.yaml with number, title, subtitle, level, requires and spine. A section
file has YAML front matter (title, nodes, sources, reads_with, requires, level, kind, status, drafted_by,
reviewed_by), and its text starts with a ## heading.
"""

from __future__ import annotations

import glob
import os
import re
from dataclasses import dataclass, field

import yaml

STATUSES = ("drafted", "checked", "reviewed")
LEVELS = ("guide", "prereq", "background", "core", "advanced", "research")
KINDS = ("theorem", "background", "survey")

# The chapters of each volume in the plan of spec 11.1 and 11.2. `requires` keys are checked against it.
P_CHAPTERS = {"P0": 8, "P1": 13, "P2": 8, "P3": 13, "P4": 9, "P5": 12, "P6": 8, "P7": 11, "P8": 13}
M_VOLUMES = range(0, 18)


def read(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def front(text: str) -> tuple[dict, str]:
    """Split a Markdown file into its YAML front matter and its body."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end > 0:
            return yaml.safe_load(text[4:end]) or {}, text[end + 5:]
    return {}, text


_SLUG = re.compile(r"[^a-z0-9 -]")


def anchor(heading: str) -> str:
    """The anchor of a heading: lower case, spaces become hyphens, other punctuation goes."""
    s = _SLUG.sub("", heading.strip().lower())
    return re.sub(r" +", "-", s).strip("-")


def as_list(x) -> list[str]:
    if x is None or x == "":
        return []
    if isinstance(x, (list, tuple)):
        return [str(i) for i in x]
    return [str(x)]


def label_of(vid: str) -> str:
    """The label of a volume id: p3 is P3, 08 is 8."""
    if vid[:1] in "pP":
        return "P" + vid[1:]
    return str(int(vid))


@dataclass
class Section:
    path: str
    fm: dict
    body: str
    volume_level: str = ""

    @property
    def status(self) -> str:
        return str(self.fm.get("status") or "drafted")

    @property
    def title(self) -> str:
        return str(self.fm.get("title") or "")

    @property
    def level(self) -> str:
        """The level of the section, or the level of its volume."""
        return str(self.fm.get("level") or self.volume_level or "")

    @property
    def kind(self) -> str:
        return str(self.fm.get("kind") or "")

    @property
    def reads_with(self) -> list[str]:
        return as_list(self.fm.get("reads_with"))

    @property
    def requires(self) -> list[str]:
        return as_list(self.fm.get("requires"))


@dataclass
class Chapter:
    num: int          # the NN of the folder
    slug: str
    dir: str
    title: str
    intro: str        # intro.md without its # title line
    sections: list[Section] = field(default_factory=list)
    problems: str = ""   # problems.md, if any

    @property
    def status(self) -> str:
        """The lowest status of its sections. A chapter with no sections is a draft."""
        if not self.sections:
            return "drafted"
        rank = min(STATUSES.index(s.status) if s.status in STATUSES else 0 for s in self.sections)
        return STATUSES[rank]

    @property
    def draft(self) -> bool:
        return self.status != "reviewed"

    @property
    def text(self) -> str:
        return "\n\n".join(s.body.strip("\n") for s in self.sections)


@dataclass
class Volume:
    id: str           # p0 or 00
    dirname: str      # p0-classical
    dir: str
    title: str
    subtitle: str
    intro: str
    meta: dict = field(default_factory=dict)   # volume.yaml
    chapters: list[Chapter] = field(default_factory=list)

    @property
    def label(self) -> str:
        """P0 to P8, or 0 to 17."""
        return label_of(self.id)

    @property
    def number(self) -> str:
        return self.label

    @property
    def index(self) -> int:
        """P0 to P8 are 0 to 8 and Volumes 0 to 17 are 9 to 26: the place of the volume in the series."""
        k, n = self.sort_key
        return n + 9 * k

    @property
    def prereq(self) -> bool:
        return self.id[:1] in "pP"

    @property
    def item_prefix(self) -> str:
        """The start of the number of an item: Theorem P5.7.2 in P5, Theorem 8.3.4 in Volume 8."""
        return self.label + "."

    @property
    def sort_key(self) -> tuple[int, int]:
        return (0 if self.prereq else 1, int(self.id[1:] if self.prereq else self.id))

    @property
    def slug(self) -> str:
        return self.dirname.split("-", 1)[1] if "-" in self.dirname else self.dirname

    @property
    def level(self) -> str:
        return str(self.meta.get("level") or "")

    @property
    def requires(self) -> list[str]:
        return as_list(self.meta.get("requires"))

    @property
    def spine(self) -> list[str]:
        return as_list(self.meta.get("spine"))

    @property
    def squares(self) -> list[float]:
        """The cover: one square per chapter, filled by its status."""
        fill = {"drafted": 0.25, "checked": 0.6, "reviewed": 1.0}
        return [fill.get(c.status, 0.0) for c in self.chapters]


def _intro(path: str) -> tuple[str, str]:
    """The title (its # line) and the rest of an intro.md."""
    if not os.path.exists(path):
        return "", ""
    _, body = front(read(path))
    lines = body.lstrip("\n").split("\n")
    if lines and lines[0].startswith("# "):
        return lines[0][2:].strip(), "\n".join(lines[1:]).strip("\n")
    return "", body.strip("\n")


_VDIR = re.compile(r"^(p[0-9]|[0-9][0-9])-")


def load_volume(d: str) -> Volume:
    vy = os.path.join(d, "volume.yaml")
    v = (yaml.safe_load(read(vy)) or {}) if os.path.exists(vy) else {}
    base = os.path.basename(d)
    vid = base.split("-", 1)[0]
    _, vintro = _intro(os.path.join(d, "intro.md"))
    slug = base.split("-", 1)[1] if "-" in base else base
    vol = Volume(vid, base, d, str(v.get("title") or slug.title()), str(v.get("subtitle") or ""), vintro, v)
    for cdir in sorted(glob.glob(os.path.join(d, "[0-9][0-9]-*"))):
        if not os.path.isdir(cdir):
            continue
        cbase = os.path.basename(cdir)
        title, intro = _intro(os.path.join(cdir, "intro.md"))
        secs = []
        for sp in sorted(glob.glob(os.path.join(cdir, "[0-9][0-9]-*.md"))):
            fm, body = front(read(sp))
            secs.append(Section(sp, fm, body, vol.level))
        pp = os.path.join(cdir, "problems.md")
        problems = front(read(pp))[1].strip("\n") if os.path.exists(pp) else ""
        if not secs and not intro and not title:   # a chapter of the plan with nothing written yet
            continue
        if not title:
            title = cbase[3:].replace("-", " ").capitalize()
        vol.chapters.append(Chapter(int(cbase[:2]), cbase[3:], cdir, title, intro, secs, problems))
    return vol


def load(content: str) -> list[Volume]:
    out = []
    for d in sorted(glob.glob(os.path.join(content, "*"))):
        if os.path.isdir(d) and _VDIR.match(os.path.basename(d)):
            out.append(load_volume(d))
    return sorted(out, key=lambda v: v.sort_key)
