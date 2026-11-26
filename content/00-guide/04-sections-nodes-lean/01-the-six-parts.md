---
title: The six parts of a section
nodes: []
sources: []
reads_with: []
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The six parts of a section

A section of a program volume has six parts, in this order.

1. **Statement.** The definitions and the main result, with numbers. In a P volume this part also holds the full proofs, as a textbook gives them.
2. **Proof in words.** The idea of the proof in a few paragraphs, then the proof. For a long proof the part gives a map of the steps first.
3. **Examples.** At least one example that shows the hypotheses are needed, and one that computes something.
4. **Exercises.** Three to eight exercises with grades: (A) routine, (B) needs an idea, (C) hard. (M) marks an exercise that asks for a machine check in Lean.
5. **Lean.** The Lean names of the statements, what the Lean statement says and where it differs from the text.
6. **Notes and history.** Who proved what, and where to read more.

The *kind* of a section tells which parts it must have. A theorem section has all six. A background section collects definitions and standard facts, and it may omit "Proof in words". A survey section reports results without proofs, and it may omit "Exercises". The sections of this guide have level `guide` and no kind.

The front matter of the source file also gives the level of the section, the chapters it requires, the places in standard books that read with it, and its status: `drafted`, `checked` or `reviewed`. Only a person who has read the section sets `reviewed`.
