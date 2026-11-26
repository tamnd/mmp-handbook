# The Minimal Model Program Handbook

The MMP Handbook is a set of textbooks on the minimal model program of birational geometry. It has two parts. The prerequisite volumes P0 to P8 go from classical varieties to schemes, cohomology, curves and surfaces, Hodge theory, positivity and the tools of birational geometry. The program volumes 0 to 17 go from divisors and cones through the program for surfaces, singularities of pairs, the cone theorem, flips and BCHM to abundance, boundedness, moduli and the open problems. It is for graduate students and for mathematicians, and it comes as a set of books in HTML, PDF and EPUB.

Each section is written as a mathematician writes a textbook. It states its results with numbers (Theorem P5.7.2, Theorem 8.3.4), proves them, gives examples and exercises, and ends with notes and history. Where a result has a Lean form in [tamnd/mmp-lean](https://github.com/tamnd/mmp-lean), a line under the statement gives the node of the map [tamnd/mmp](https://github.com/tamnd/mmp), the Lean name, the Lean status and the state of the result in the literature.

## What is open

The program for surfaces and for 3-folds in characteristic 0, the cone and contraction theorems for klt pairs, the existence of klt flips and the finite generation of the canonical ring are theorems. Termination of flips and abundance in dimension 4 and higher are open in general, and termination for lc 4-folds with rational boundary is claimed. The handbook does not claim a proof of an open conjecture. The Lean status (stated, proved, ...) and the literature state (theorem, claimed, conjecture, refuted) are separate, and the builder writes both from the records of the map at build time. No status in the books is written by hand.

## The volumes

| | Prerequisite volume |
|---|---|
| P0 | Guide and classical varieties |
| P1 | Commutative algebra for geometry |
| P2 | Categories, homological algebra and sheaves |
| P3 | Schemes, divisors and line bundles |
| P4 | Cohomology and duality |
| P5 | Curves and surfaces |
| P6 | Complex geometry and Hodge theory |
| P7 | Intersection numbers, positivity and vanishing |
| P8 | Tools of birational geometry: rational curves, resolution, toric varieties, singularities |

| | Program volume |
|---|---|
| 0 | How to read this handbook |
| 1 | Divisors, curves and cones |
| 2 | The MMP for surfaces |
| 3 | The toric MMP |
| 4 | Singularities of pairs |
| 5 | Vanishing theorems and multiplier ideals |
| 6 | Rational curves and bend-and-break |
| 7 | Cone and contraction theorems |
| 8 | Flips, flops and the 3-fold MMP |
| 9 | BCHM: existence of minimal models |
| 10 | Abundance, termination and the Sarkisov program |
| 11 | The MMP in positive and mixed characteristic |
| 12 | Boundedness, complements and BAB |
| 13 | Moduli of stable varieties |
| 14 | K-stability and K-moduli of Fano varieties |
| 15 | The MMP for foliations |
| 16 | The 2026 frontier: generalized pairs, Kähler spaces, 4-folds |
| 17 | Open problems |

The repository has today Volume 0 (the guide), P0 and the first chapter of Volume 1. Every section has the status `drafted`. A volume has a release when all its chapters have the status `reviewed`.

## The content format

A volume is a folder `content/<id>-<slug>/`, with `id` one of `p0` to `p8` or `00` to `17`. It has a file `volume.yaml` with `number`, `title`, `subtitle`, `level`, `requires` and `spine`. A chapter is a folder `NN-<slug>/` with an optional `intro.md`, whose `#` heading is the title of the chapter, one file `NN-<slug>.md` for each section and an optional `problems.md`.

A section file starts with YAML front matter:

```markdown
---
title: Castelnuovo's contraction theorem
nodes: [MM8MGCYF75]
sources: [Har77, KM98]
reads_with: [Har77:V.5, KM98:1.28]
requires: [P6.4]
level: core
kind: theorem
status: drafted
drafted_by: writer
reviewed_by: []
---
## Castelnuovo's contraction theorem

### Statement

**Theorem (Castelnuovo).** Let $X$ be a smooth projective surface ...

Node: MM8MGCYF75 · Lean: `MinimalModel.Castelnuovo`

### Proof in words
### Examples
### Exercises
### Lean
### Notes and history
```

- `nodes` lists the tags of the map that the section uses. Each tag must be a file `blueprint/nodes/<TAG>.yaml` of the map.
- `sources` lists the keys of the papers that the section cites, and `reads_with` lists places in them as `Key:place`. Each key must be a paper of the map, or a record in the folder `books/` of this repository. The build lists these papers at the end of the chapter.
- `requires` lists the chapters that the section uses, as `P5.6` or `3.4`.
- `level` is `guide`, `prereq`, `background`, `core`, `advanced` or `research`. It falls back to the level of the volume.
- `kind` is `theorem`, `background` or `survey`. A theorem section has the six parts above, in that order. A background section may omit "Proof in words", and a survey section may omit "Exercises". A section of level `guide` needs no kind.
- `status` is `drafted`, `checked` or `reviewed`. A chapter that is not `reviewed` is a draft and has a Draft mark. A section at status `reviewed` must have a name in `reviewed_by`.

A statement starts with a bold head: `**Definition.**`, `**Theorem (Name).**`. The build numbers the statements by volume, chapter and place in the chapter (Theorem P0.3.5, Lemma 1.1.2). `mhb number --write` writes the same numbers into the sources. Each exercise starts with its grade, (A), (B) or (C), and (M) when it asks for a machine check.

A statement that has a node has a line ``Node: <TAG> · Lean: `<Name>` `` under it. At build time `mhb` adds the Lean status and the literature state. A status that is written in the source is replaced.

## Build

You need Python 3.11 or later and [pandoc](https://pandoc.org) 3.12 or later. The PDF also needs [Tectonic](https://tectonic-typesetting.github.io). Put a checkout of [tamnd/mmp](https://github.com/tamnd/mmp) next to this repository, at `../mmp`, or give its path with `--map PATH` or the environment variable `MHB_MAP`.

```sh
pip install .
python scripts/style.py
python -m mhb check
python -m mhb number --write
python -m mhb build --volume 0,P0 --formats html,pdf,epub
python -m unittest discover -s tests
```

`mhb check` reports a bad front matter, a missing part, an exercise with no grade, a tag or a key that is not in the map, a `requires` key that is not a chapter of the plan, and a text that claims more than the state of its node. It also gives warnings that do not fail the check.

The books go to `build/mmp-handbook-<id>-<slug>-<version>.pdf` and `.epub`, and the HTML to `build/html/`. `EDITION` gives the version and the commits of tamnd/mmp, tamnd/mmp-lean and AxiomMath/MMP that the edition describes.

## Licence

The text is licensed under [CC BY 4.0](LICENSE-CONTENT). The builder `mhb`, the filter and the style files are licensed under the [MIT licence](LICENSE).

Please report errors at [issues](https://github.com/tamnd/mmp-handbook/issues). [CONTRIBUTING.md](CONTRIBUTING.md) tells how to send a change.
