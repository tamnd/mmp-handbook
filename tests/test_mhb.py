"""Tests of mhb on the small volume in tests/fixture. They do not need Tectonic. One test needs pandoc and is
skipped without it.

    python -m unittest discover -s tests
    python -m pytest tests
"""

from __future__ import annotations

import io
import os
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from mhb import number  # noqa: E402
from mhb.__main__ import main  # noqa: E402
from mhb.book import Book, out_name  # noqa: E402
from mhb.check import check  # noqa: E402
from mhb.content import load, read  # noqa: E402
from mhb.map import Map  # noqa: E402

FIXTURE = os.path.join(HERE, "fixture")
CONTENT = os.path.join(FIXTURE, "content")
MAP = os.path.join(FIXTURE, "map")


class Tmp(unittest.TestCase):
    """A copy of the fixture that a test can change."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        shutil.copytree(FIXTURE, os.path.join(self.tmp, "fixture"))
        self.content = os.path.join(self.tmp, "fixture", "content")
        self.map = os.path.join(self.tmp, "fixture", "map")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def write(self, rel: str, text: str):
        p = os.path.join(self.content, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(text)


class TestParse(unittest.TestCase):
    def test_books(self):
        m = Map.load(MAP)
        self.assertNotIn("Rei88", m.papers)
        b = Book(CONTENT, MAP)    # the folder books/ next to content/ fills the keys that the map lacks
        self.assertEqual(b.map.papers["Rei88"].title, "Undergraduate algebraic geometry")
        self.assertNotEqual(b.map.papers["Kol87"].title, "A record that the map record replaces")

    def test_volumes(self):
        p0, v0 = load(CONTENT)    # the P volumes come first
        self.assertEqual((p0.id, p0.label, p0.dirname, p0.prereq, p0.item_prefix), ("p0", "P0", "p0-pre", True, "P0."))
        self.assertEqual((v0.id, v0.label, v0.dirname, v0.title, v0.subtitle),
                         ("00", "0", "00-test", "Test", "A small volume for the tests"))
        self.assertEqual((v0.level, v0.requires, v0.spine), ("guide", ["P0.2", "P5.12"], ["Kol87"]))
        self.assertEqual([c.num for c in v0.chapters], [1, 2])
        first, second = v0.chapters
        self.assertEqual(first.title, "The first chapter")
        self.assertEqual(second.title, "Second")
        self.assertEqual(len(first.sections), 2)
        s = first.sections[0]
        self.assertEqual(s.fm["nodes"], ["MM0000000A"])
        self.assertEqual((s.level, s.kind, s.reads_with, s.requires), ("core", "theorem", ["Har77:V.5"], ["P0.5", "2"]))
        self.assertEqual(second.sections[0].level, "guide")
        self.assertEqual((first.status, first.draft), ("reviewed", False))
        self.assertEqual((second.status, second.draft), ("drafted", True))
        self.assertIn("(B) Show that a plane conic", p0.chapters[0].problems)
        self.assertEqual(p0.chapters[0].sections[0].level, "prereq")   # from volume.yaml

    def test_out_name(self):
        p0, v0 = load(CONTENT)
        self.assertEqual(out_name(v0, "0.1.0"), "mmp-handbook-00-test-0.1.0")
        self.assertEqual(out_name(p0, "0.1.0"), "mmp-handbook-p0-pre-0.1.0")


class TestStatus(unittest.TestCase):
    def test_with_records(self):
        m = Map.load(MAP)
        self.assertEqual(m.status("MM0000000A"), "proved")
        self.assertEqual(m.status("MM0000000B"), "open")
        self.assertEqual(m.status("MM0000000C"), "unstated")
        self.assertEqual([m.literature(t) for t in ("MM0000000A", "MM0000000B", "MM0000000C")],
                         ["theorem", "conjecture", "theorem"])

    def test_decls_and_hypotheses(self):
        # The form that tamnd/mmp-lean writes has the key "decls". A node with hypotheses is proved-mod.
        with tempfile.TemporaryDirectory() as d:
            root = os.path.join(d, "map")
            shutil.copytree(MAP, root)
            with open(os.path.join(root, "records", "lean.json"), "w") as f:
                f.write('{"commit": "x", "decls": {"MinimalModel.Castelnuovo": {"axioms": []}, '
                        '"MinimalModel.castelnuovo": {}}}')
            with open(os.path.join(root, "blueprint", "nodes", "MM0000000A.yaml"), "a") as f:
                f.write("hypotheses:\n- MM0000000B\n")
            m = Map.load(root)
            self.assertEqual(set(m.records), {"MinimalModel.Castelnuovo", "MinimalModel.castelnuovo"})
            self.assertEqual(m.status("MM0000000A"), "proved-mod")

    def test_status_json(self):
        # records/status.json wins over the computed status and over the kind of the node
        with tempfile.TemporaryDirectory() as d:
            root = os.path.join(d, "map")
            shutil.copytree(MAP, root)
            with open(os.path.join(root, "records", "status.json"), "w") as f:
                f.write('{"nodes": {"MM0000000C": {"status": "stated", "literature": "claimed"}, '
                        '"MM0000000A": "proved-ext"}}')
            m = Map.load(root)
            self.assertEqual((m.status("MM0000000C"), m.literature("MM0000000C")), ("stated", "claimed"))
            self.assertEqual(m.status("MM0000000A"), "proved-ext")

    def test_without_records(self):
        with tempfile.TemporaryDirectory() as d:
            shutil.copytree(MAP, os.path.join(d, "map"), ignore=shutil.ignore_patterns("records"))
            m = Map.load(os.path.join(d, "map"))
            self.assertIsNone(m.records)
            self.assertEqual({m.status(t) for t in m.nodes}, {"unstated"})


class TestMarkdown(unittest.TestCase):
    def setUp(self):
        self.book = Book(CONTENT, MAP)
        self.md, self.stats = self.book.markdown(self.book.volume(0))
        self.pmd, _ = self.book.markdown(self.book.volume("P0"))

    def test_numbers(self):
        # items are numbered by volume, chapter and place in the chapter (spec 11.3)
        self.assertIn('# The first chapter {#v00-c1 num="1"}', self.md)
        self.assertIn('## The start {#v00-c1-the-start num="1.1"}', self.md)
        self.assertIn('## More {#v00-c1-more num="1.2"}', self.md)
        self.assertIn("[Theorem 0.1.1 (Castelnuovo).]", self.md)
        self.assertIn("[Definition 0.1.2.]", self.md)
        self.assertIn("[Conjecture 0.1.3 (abundance).]", self.md)
        self.assertIn("[Lemma 0.2.1.]", self.md)
        self.assertIn("[Definition P0.1.1.]", self.pmd)
        self.assertIn("[Proposition P0.1.2.]", self.pmd)
        self.assertIn("## Problems", self.pmd)

    def test_node_lines(self):
        self.assertIn("[Node: [MM0000000A](https://mmp.tamnd.com/node/MM0000000A/) · Lean: "
                      "`MinimalModel.Castelnuovo` · status: proved · literature: theorem]{.node latex-cmd=\"hblean\"}",
                      self.md)
        # a status written in the source is replaced by the computed one
        self.assertIn("`MinimalModel.Abundance` · status: open · literature: conjecture]", self.md)
        self.assertNotIn("status: proved · literature: theorem · status", self.md)
        self.assertIn("[Node: [MM0000000C](https://mmp.tamnd.com/node/MM0000000C/) · status: unstated · "
                      "literature: theorem]", self.md)
        self.assertEqual(self.stats["nodes"], 3)
        self.assertEqual([x["lean"] for x in self.stats["lean"]], ["MinimalModel.Castelnuovo",
                                                                  "MinimalModel.Abundance", ""])

    def test_draft_mark(self):
        self.assertEqual(self.md.count('::: {.draft latex-env="hbdraft"}'), 1)
        self.assertLess(self.md.index("# Second"), self.md.index(".draft"))

    def test_references(self):
        self.assertIn("- **Har77**. Robin Hartshorne. Algebraic geometry", self.md)
        self.assertIn("<https://arxiv.org/abs/math/0610203>", self.md)

    def test_pick(self):
        self.assertEqual(self.book.volume("p0").label, "P0")
        self.assertEqual(self.book.volume("00").label, "0")
        with self.assertRaises(KeyError):
            self.book.volume("7")


class TestNumber(Tmp):
    def test_write(self):
        with redirect_stdout(io.StringIO()):
            changed = number.run(load(self.content), write=True)
        self.assertEqual(len(changed), 4)
        t = read(os.path.join(self.content, "00-test", "01-first", "01-start.md"))
        self.assertIn("**Theorem 0.1.1 (Castelnuovo).**", t)
        self.assertIn("**Definition 0.1.2.**", t)
        self.assertTrue(t.startswith("---\ntitle: The start\n"))
        t = read(os.path.join(self.content, "00-test", "01-first", "02-more.md"))
        self.assertIn("**Conjecture 0.1.3 (abundance).**", t)
        t = read(os.path.join(self.content, "p0-pre", "01-only", "01-one.md"))
        self.assertIn("**Definition P0.1.1.**", t)
        self.assertIn("**Proposition P0.1.2.**", t)
        with redirect_stdout(io.StringIO()):
            self.assertEqual(number.run(load(self.content), write=True), [])   # a second run changes nothing

    def test_dry_run(self):
        with redirect_stdout(io.StringIO()):
            changed = number.run(load(self.content), write=False)
        self.assertEqual(len(changed), 4)
        self.assertIn("**Definition.**", read(changed[0]))


class TestCheck(Tmp):
    def faults(self):
        return check(load(self.content), Map.load(self.map), self.tmp)

    def test_clean(self):
        faults, warns = self.faults()
        self.assertEqual(faults, [])
        self.assertEqual(warns, [])

    def test_faults(self):
        self.write("00-test/02-second/02-bad.md", "---\ntitle: Bad\nnodes: [MM0000000Y]\nsources: [Nope99]\n"
                   "status: done\ndrafted_by: writer\nlevel: guide\n---\n## Bad\n\n**Theorem.** A claim.\n\n"
                   "Node: MM0000000Z · Lean: `MinimalModel.nothing`\n\nNode:\n")
        faults, _ = self.faults()
        text = "\n".join(faults)
        self.assertIn("02-bad.md:13: the node MM0000000Z is not in the map", text)
        self.assertIn("the node MM0000000Y of the front matter is not in the map", text)
        self.assertIn("the source Nope99 is not a paper of the map", text)
        self.assertIn("the status 'done' is not one of drafted, checked, reviewed", text)
        self.assertIn("02-bad.md:15: a Node line without a tag", text)

    def test_new_keys(self):
        self.write("00-test/02-second/02-keys.md", "---\ntitle: Keys\nnodes: []\nstatus: drafted\ndrafted_by: w\n"
                   "level: expert\nkind: lemma\nrequires: [P9.1, P0.9, P3.13, 17, 18, 3.4, x]\n"
                   "reads_with: [Har77:II.6, Nope99:1.2, Har77]\n---\n## Keys\n")
        self.write("00-test/02-second/03-nokind.md", "---\ntitle: No kind\nnodes: []\nstatus: drafted\n"
                   "drafted_by: w\nlevel: core\n---\n## No kind\n")
        faults, _ = self.faults()
        text = "\n".join(faults)
        self.assertIn("the level 'expert' is not one of guide, prereq, background, core, advanced, research", text)
        self.assertIn("the kind 'lemma' is not one of theorem, background, survey", text)
        for bad in ("P9.1", "P0.9", "18", "x"):
            self.assertIn(f"the requires key '{bad}' does not resolve", text)
        for good in ("P3.13", "'17'", "3.4"):
            self.assertNotIn(f"requires key {good}", text)
        self.assertIn("the reads_with paper Nope99 is not a paper of the map", text)
        self.assertIn("the reads_with key 'Har77' is not of the form paper:place", text)
        self.assertNotIn("Har77:II.6", text)
        self.assertIn("03-nokind.md: the front matter has no kind", text)

    def test_volume_yaml(self):
        with open(os.path.join(self.content, "00-test", "volume.yaml"), "w") as f:
            f.write("number: 0\ntitle: Test\nlevel: middle\nrequires: [P1.20]\n")
        faults, warns = self.faults()
        self.assertIn("00-test/volume.yaml: the level 'middle' is not one of", "\n".join(faults))
        self.assertIn("00-test/volume.yaml: the requires key 'P1.20' does not resolve", "\n".join(faults))
        self.assertIn("00-test/volume.yaml: no spine", "\n".join(warns))

    def test_six_parts(self):
        t = read(os.path.join(self.content, "00-test", "01-first", "01-start.md"))
        self.write("00-test/01-first/01-start.md", t.replace("### Proof in words", "### Proofs"))
        faults, _ = self.faults()
        self.assertIn("01-start.md: a theorem section has no part '### Proof in words'", "\n".join(faults))
        a, b = t.index("### Lean"), t.index("### Notes and history")
        swapped = t[:a] + t[b:] + "\n" + t[a:b]
        self.write("00-test/01-first/01-start.md", swapped)
        faults, _ = self.faults()
        self.assertIn("01-start.md: the parts are not in the order", "\n".join(faults))
        # a survey may leave out Exercises (02-more.md has none) and a background section Proof in words
        self.assertNotIn("02-more.md: a survey", "\n".join(faults))
        self.assertNotIn("01-one.md", "\n".join(faults))

    def test_grades(self):
        t = read(os.path.join(self.content, "00-test", "01-first", "01-start.md"))
        self.write("00-test/01-first/01-start.md", t.replace("2. (B) Show", "2. Show").replace("3. (B) (M)", "3. (D)"))
        with open(os.path.join(self.content, "p0-pre", "01-only", "problems.md"), "a") as f:
            f.write("2. A problem with no grade.\n")
        faults, _ = self.faults()
        text = "\n".join(faults)
        self.assertIn("01-start.md:40: an exercise with no grade", text)
        self.assertIn("01-start.md:41: an exercise with no grade", text)
        self.assertNotIn("01-start.md:39:", text)
        self.assertIn("problems.md:4: an exercise with no grade", text)

    def test_claims_no_more_than_status(self):
        t = read(os.path.join(self.content, "00-test", "01-first", "02-more.md"))
        self.write("00-test/01-first/02-more.md", t.replace("The conjecture is open in dimension 4.",
                                                            "It holds.").replace("It is a conjecture.", "Known.")
                   .replace("Conjecture (abundance)", "Theorem (abundance)"))
        faults, _ = self.faults()
        self.assertIn("02-more.md: the node MM0000000B is conjecture, and the text does not say 'open' or "
                      "'conjecture'", "\n".join(faults))

    def test_statement_not_in_records(self):
        self.write("00-test/02-second/02-planned.md", "---\ntitle: Planned\nnodes: [MM0000000C]\nstatus: drafted\n"
                   "drafted_by: writer\nlevel: guide\n---\n## Planned\n\n**Theorem.** A claim.\n\n"
                   "Node: MM0000000C · Lean: `MinimalModel.missing` (the statement only)\n")
        faults, _ = self.faults()
        self.assertIn("02-planned.md:12: the Lean name MinimalModel.missing is marked as a statement, but it is "
                      "not in records/lean.json", "\n".join(faults))

    def test_section_rules(self):
        self.write("00-test/02-second/02-bad.md", "---\ntitle: Bad\nstatus: reviewed\ndrafted_by: writer\n"
                   "level: guide\nreviewed_by: []\n---\nNo heading here, and a dash — here.\n")
        faults, _ = self.faults()
        text = "\n".join(faults)
        self.assertIn("a section must open with a ## heading", text)
        self.assertIn("the status is reviewed and reviewed_by is empty", text)
        self.assertIn("an en dash or an em dash", text)

    def test_warnings(self):
        self.write("00-test/02-second/02-warn.md", "---\ntitle: Warn\nnodes: []\nstatus: drafted\ndrafted_by: writer\n"
                   "level: guide\n---\n## Warn\n\n**Theorem.** A claim.\n\n**Lemma.** Another claim.\n\n"
                   "Node: MM0000000A · Lean: `MinimalModel.other`\n")
        faults, warns = self.faults()
        self.assertEqual(faults, [])
        text = "\n".join(warns)
        self.assertIn("02-warn.md:10: Theorem with no Node line", text)
        self.assertIn("the node MM0000000A is not in the nodes of the front matter", text)
        self.assertIn("the Lean name MinimalModel.other is not the Lean name of MM0000000A", text)

    def test_no_map(self):
        faults, _ = check(load(self.content), Map.load(os.path.join(self.tmp, "nowhere")), self.tmp)
        self.assertTrue(faults[0].startswith("the map is not found"))


class TestCli(unittest.TestCase):
    def run_cli(self, argv):
        with redirect_stdout(io.StringIO()) as out, redirect_stderr(io.StringIO()):
            code = main(argv)
        return code, out.getvalue()

    def test_check(self):
        self.assertEqual(self.run_cli(["--map", MAP, "--content", CONTENT, "check"])[0], 0)
        self.assertEqual(self.run_cli(["check", "--map", MAP, "--content", CONTENT, "--volume", "0"])[0], 0)
        self.assertEqual(self.run_cli(["check", "--map", MAP, "--content", CONTENT, "--volume", "p0,00"])[0], 0)

    def test_check_bad_map(self):
        code, out = self.run_cli(["check", "--map", os.path.join(HERE, "nowhere"), "--content", CONTENT])
        self.assertEqual(code, 1)
        self.assertIn("the map is not found", out)

    def test_check_bad_volume(self):
        with self.assertRaises(SystemExit):
            self.run_cli(["check", "--map", MAP, "--content", CONTENT, "--volume", "P9"])


@unittest.skipUnless(shutil.which("pandoc"), "pandoc is not installed")
class TestHtml(unittest.TestCase):
    def test_html(self):
        from mhb import html
        book = Book(CONTENT, MAP)
        v = book.volume(0)
        md, _ = book.markdown(v)
        with tempfile.TemporaryDirectory() as d:
            info = html.build(book, v, md, os.path.join(d, v.dirname), "0.1.0", "2026-11-26")
            self.assertTrue(info["html_ok"], info.get("error"))
            page = read(info["html"])
            self.assertIn("https://mmp.tamnd.com/node/MM0000000A/", page)
            self.assertIn("Theorem 0.1.1", page)
            self.assertIn("1.1 The start", page)
            idx = read(html.index(book, d, "0.1.0", "2026-11-26"))
            self.assertIn("00-test/index.html", idx)


@unittest.skipUnless(shutil.which("pandoc"), "pandoc is not installed")
class TestLatex(unittest.TestCase):
    def test_pandoc(self):
        from mhb.latex import pandoc_latex
        book = Book(CONTENT, MAP)
        md, _ = book.markdown(book.volume(0))
        tex = pandoc_latex(md)
        self.assertIn(r"\hbchapter{1}{The first chapter}{v00-c1}", tex)
        self.assertIn(r"\hbsection{1.1}{The start}{v00-c1-the-start}", tex)
        self.assertIn(r"\href{https://mmp.tamnd.com/node/MM0000000A/}{MM0000000A}", tex)
        self.assertIn(r"\hblean{", tex)
        self.assertEqual(tex.count(r"\begin{hbdraft}"), 1)


if __name__ == "__main__":
    unittest.main()
