"""Write the numbers of the build into the Markdown of the section files.

A statement head **Theorem (Name).** becomes **Theorem P5.7.2 (Name).** in a P volume and **Theorem 8.3.4
(Name).** in an MMP volume: the label of the volume, the chapter (the NN of the chapter folder) and the place of
the item in the chapter, counted over the section files in order (spec 11.3). So the source on GitHub reads as
the book does.

    python -m mhb number           # list the files that would change
    python -m mhb number --write   # change them
"""

from __future__ import annotations

import re

from .content import read
from .md import _FENCE, _STMT, KINDS

_HEAD = re.compile(r"^(\*\*(?:" + KINDS + r")(?: [a-z]+)?)(?: P?[0-9]+(?:\.[0-9]+)*)?")


def stamp(text: str, prefix: str, item: int) -> tuple[str, int]:
    """Number the statement heads of one section file. `prefix` is "P5.7." or "8.3."; `item` is the number of
    items before this file in the chapter. The new count is returned."""
    out, fence = [], None
    for ln in text.split("\n"):
        f = _FENCE.match(ln)
        if f:
            fence = None if fence == f.group(1)[0] else (fence or f.group(1)[0])
        elif not fence and _STMT.match(ln):
            item += 1
            ln = _HEAD.sub(lambda m: f"{m.group(1)} {prefix}{item}", ln, count=1)
        out.append(ln)
    return "\n".join(out), item


def run(volumes, write: bool) -> list[str]:
    changed = []
    for v in volumes:
        for ch in v.chapters:
            item = 0
            for s in ch.sections:
                src = read(s.path)
                fm_end = 0
                if src.startswith("---\n"):
                    fm_end = src.index("\n---\n", 4) + 5
                body, item = stamp(src[fm_end:], f"{v.item_prefix}{ch.num}.", item)
                new = src[:fm_end] + body
                if new != src:
                    changed.append(s.path)
                    if write:
                        with open(s.path, "w", encoding="utf-8") as f:
                            f.write(new)
    for p in changed:
        print(("numbered " if write else "would number ") + p)
    print(f"{len(changed)} files")
    return changed
