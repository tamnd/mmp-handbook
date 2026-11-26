---
title: Levels, bands and the status of a section
nodes: []
sources: []
reads_with: []
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Levels, bands and the status of a section

Each section has a *level*. The level says how the section is written and what it assumes.

| Level | Volumes | Style |
|---|---|---|
| guide | P0 Ch. 1 and 2, Volume 0 | short chapters, no proofs, the status table |
| prereq | P0 to P8 | complete proofs; each definition is followed by two examples; the text follows a standard book closely and names it; 15 to 30 exercises per chapter |
| background | 1 | complete proofs; each definition is followed by two examples |
| core | 2 to 8 | examples first, then the theorem, then the proof in words, then the full proof; each chapter ends with a computation by hand; each flip is first seen in a toric or weighted example |
| advanced | 9 to 12 | proof maps before proofs; induction diagrams; full proofs of the key lemmas, and page references for the others |
| research | 13 to 17 | full statements, proof sketches and a dated status; claims from preprints are marked claimed |

Each section also has a *status*. The status says how far the text has been checked.

- **drafted.** A writer wrote the section from the papers, the map and the Lean code. Nobody has checked it. Every section of this edition is drafted.
- **checked.** A second pass and the scripts found no problem: each cited result exists at the cited place, each link resolves, the six parts are present and in order, and each exercise has a grade and a solution.
- **reviewed.** A person with the right background read the section and signed it. Only reviewed chapters go into a numbered release.

A chapter that is not reviewed carries the mark **Draft** at its start. Treat a drafted chapter as notes that can contain errors. Please report errors at <https://github.com/tamnd/mmp-handbook/issues>.

Exercises have a grade: (A) routine, (B) standard, (C) research level. An exercise that needs a computer also has the mark (M).

### Exercises

1. (A) Find the level and the status of this section in its source file.
