"""The HTML of a volume for the site (/learn/ of spec 12): the Markdown of the volume, then pandoc with MathJax,
one standalone page per volume, and an index page of the volumes that the build wrote."""

from __future__ import annotations

import html as _html
import os
import subprocess
import time

from .book import Book
from .content import Volume
from .paths import ROOT

CSS = """body{max-width:46rem;margin:2rem auto;padding:0 1rem;font-family:Georgia,serif;line-height:1.5;color:#222}
h1,h2,h3{font-family:Helvetica,Arial,sans-serif;line-height:1.25}
.node{display:block;font-family:Helvetica,Arial,sans-serif;font-size:0.85em;color:#555;margin:0.3em 0 0.8em}
.draft{border:1px solid #c33;padding:0.4em 0.8em;margin:1em 0;background:#fdf3f3}
table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:0.2em 0.5em;vertical-align:top}
blockquote{border-left:3px solid #ccc;margin-left:0;padding-left:1em;color:#333}
code{font-size:0.9em}nav#TOC li{list-style:none}
"""


def build(book: Book, vol: Volume, md: str, outdir: str, edition: str, date: str) -> dict:
    os.makedirs(outdir, exist_ok=True)
    t = time.time()
    css = os.path.join(outdir, "handbook.css")
    with open(css, "w", encoding="utf-8") as f:
        f.write(CSS)
    out = os.path.join(outdir, "index.html")
    title = f"Volume {vol.label}: {vol.title}"
    cmd = ["pandoc", "-f", "markdown-auto_identifiers-raw_tex", "-t", "html5", "-s", "-o", out,
           "--lua-filter", os.path.join(ROOT, "filters", "mhb.lua"), "--math-method=mathjax", "--toc", "--toc-depth=2",
           "--css", "handbook.css", "--metadata", f"title={title}",
           "--metadata", f"subtitle=The Minimal Model Program Handbook. Edition {edition}, {date}.",
           "--metadata", "lang=en"]
    r = subprocess.run(cmd, input=md, capture_output=True, text=True)
    info = {"html_s": round(time.time() - t, 1), "html_ok": r.returncode == 0}
    if r.returncode:
        info["error"] = r.stderr[-4000:]
    else:
        info["html"] = out
        if r.stderr.strip():
            info["html_warnings"] = r.stderr.count("[WARNING]")
    return info


def index(book: Book, outdir: str, edition: str, date: str) -> str:
    """build/html/index.html: one line per volume that has a page."""
    os.makedirs(outdir, exist_ok=True)
    rows = []
    for v in book.volumes:
        if os.path.exists(os.path.join(outdir, v.dirname, "index.html")):
            rows.append(f'<li><a href="{v.dirname}/index.html">Volume {_html.escape(v.label)}: '
                        f'{_html.escape(v.title)}</a>. {_html.escape(v.subtitle)}</li>')
    page = (f'<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><title>The Minimal Model Program '
            f'Handbook</title></head>\n<body><h1>The Minimal Model Program Handbook</h1>\n<p>Edition '
            f'{_html.escape(edition)}, {_html.escape(date)}. Every chapter is a draft.</p>\n<ul>\n'
            + "\n".join(rows) + "\n</ul></body></html>\n")
    p = os.path.join(outdir, "index.html")
    with open(p, "w", encoding="utf-8") as f:
        f.write(page)
    return p
