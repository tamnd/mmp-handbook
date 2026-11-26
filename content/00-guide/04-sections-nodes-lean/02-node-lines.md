---
title: The node line
nodes: [MMRP5RX4JJ, MMBTDMD2XP]
sources: []
reads_with: []
requires: []
level: guide
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The node line

A statement that has a node in the map has a line under it, for example:

Node: MMRP5RX4JJ · Lean: `MinimalModel.Castelnuovo`

The build adds two states to the line from the records of the map. A writer never types them.

- The **Lean status** tells how far the Lean code has come. `unstated`: the map has no Lean statement yet. `stated`: a Lean statement exists. `faithful`: the statement passed the fidelity review. `proved`: the proof is complete and has no `sorry`. `proved-mod`: the proof is complete from named hypotheses, for example a black box. `proved-ext`: the proof is in an external project, AxiomMath/MMP, at the commit of `EDITION`. `open`: the statement is a conjecture. `claimed`: the map has a claim of a proof, not yet checked.
- The **literature state** tells what mathematicians know. `theorem`: the result has a published, accepted proof. `claimed`: a proof is announced and not yet accepted. `conjecture`: the result is open. `refuted`: the result is false.

The two states are separate. A theorem of the literature is often only `stated` in Lean. A result can be `claimed` in the literature, and the text then says "claimed", never "proved". The check of the builder reports a text whose node is a conjecture or a claim, and whose words do not say so.

Example: the termination of flips for lc 4-folds with rational boundary.

Node: MMBTDMD2XP

The node has the kind `claim`. Its literature state is `claimed`, so the handbook writes "termination for these 4-folds is claimed".

### Exercises

1. (A) A node has the Lean status `proved-mod` and the literature state `theorem`. Say in two sentences what a reader may conclude, and what not.
