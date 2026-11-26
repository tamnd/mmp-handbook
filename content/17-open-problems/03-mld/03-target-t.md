---
title: The Han-Liu reduction and Target T
nodes: [MMXCD16PTN, MM0NXABJ9S, MMTJ3YNHTG, MMAWP4SA44]
sources: [HL25, Amb99, Rei83, FS04]
reads_with: []
requires: ["3", "4", "10"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Han-Liu reduction and Target T

### Statement

The word enc stands for "exceptionally non-canonical", from the title of HL25. The records do not define an enc germ. The notes of the node say that the definition must be checked against Han and Liu before a proof uses it [U].

**Conjecture 17.3.6 (ACC for the mlds of enc 4-fold germs).** The mlds of the enc germs of dimension 4 satisfy the ACC. This is Conjecture 1.9(2') of Han and Liu in dimension 4.

Node: MMXCD16PTN · Lean: `MinimalModel.HanLiuEncACC`

This is statement S52. It is open. Its toric case is Target T of the project.

**Theorem 17.3.7 (The Han-Liu reduction).** Fix $n$. Assume the ACC for the mlds of enc germs in dimension $n$ and the termination of terminal flips in dimension $n$. Then T(n) holds.

Node: MM0NXABJ9S · Lean: `MinimalModel.HanLiuReduction`

This is statement S29, Theorem 1.2 of HL25 (Geom. Topol. 29 (2025), arXiv:2209.13122).

### Proof in words

**What is known.** The records give the Han-Liu reduction as a theorem with the tag [P] (spec 03.11). Spec 03.11 also says that the full Conjecture 1.9(2') in dimension 4 gives T(4) for lc flips [P], and that Han and Liu give a proof of termination in dimension at most 3 by the ACC for 3-fold mlds. The records give no known case of S52 in dimension 4, and no claim of it. So S52 is open in dimension 4 in each case that the records name.

The reduction is sharper than Shokurov's reduction (Section 3.1) in two ways. It needs the ACC only for one class of germs, the enc germs, and it needs no LSC. In exchange, it needs the termination of terminal flips.

**Target T.** Spec 04.12 names one open target for the level G5 of the project: O-R3-3, Conjecture 1.9(2') of Han and Liu for the enc 4-fold germs that are toric. The target must be open, small enough for one paper, checkable in Lean, and on a route that the project builds anyway. Spec 04.12 gives four reasons for the choice.

1. It is open, and report D rates it at the small end of its scale (D §20 #15).
2. It is convex geometry over $\mathbb{Z}^4$, on the infrastructure of route R3.
3. It is on the reduction graph: the full conjecture in dimension 4 gives T(4) for lc flips. A toric case gives a human proof of a piece of T(4) that does not depend on AI code.
4. The lab can search the cones first (E2) and produce candidate counterexamples or a classification before a proof.

The backups are O-R6-2 (the questions of Ajit, with the lab; Chapter 4) and O-R8-1 (a surface question on foliations; Chapter 6). The choice is reviewed at milestone S3.

Spec 04.4 names the key obstruction for the mathematics of O-R3-3: the enc condition and the 4-dimensional cones need a classification that may be large. O-R3-3 has the difficulty 2, with the tag [U].

### Examples

The data of the lab on 2026-11-26 is the run `2026-11-26-e2-cyclic-quotient-mld-3-6d070b98` of Section 3.1, in dimension 3 only. The record of the run names node MMXCD16PTN. The table of the run has a column "enc" for each index; the run counts 25 enc germs among the 1747 germs, all of index at most 20. The summary of the run does not define the column. The run uses mmp commit 814e61a4, has no Lean certificate and covers only the isolated cyclic quotients. Milestone S2 asks for the full dimension 3.

Spec 13.3 gives the spec of the first 4-dimensional search as its example, `toric-enc-mld-4fold-index-le-12`. On 2026-11-26 the folder `lab/specs` holds only the spec of the 3-dimensional run. The example spec asks for the simplicial cones of dimension 4 with index 1 to 12, one cone for each $GL(4, \mathbb{Z})$ orbit in Hermite normal form. Its outputs are the mld, the minimizers, the violating germs if any, and one certificate for each cone. Spec 13 rates the cost of E2 in dimension 3, and in dimension 4 to index 12, at 500 to 5,000 core hours [U]. The first measurement at index 6 sets the plan for index 12 (Q-22).

The certificate of a toric mld (spec 13.5) is finite. Let $\psi$ be the linear function with $\psi(v_i) = 1$ on the primitive generators of the cone. A certificate gives a minimizer $v$ and the finite list of lattice points of the bounded region $\{u \in \sigma : \psi(u) < \psi(v)\}$, which has no interior point. Lean checks the list by `decide`. So a violating germ for Target T would be a proved counterexample, under the reduction from all valuations to toric valuations (row T5-08 of spec 07, proved or a named hypothesis).

The first test case of S52 beyond Target T is the case of the hyperquotient germs (target O-R3-4, difficulty 3 [U], after Nakamura and Shibata, arXiv:2606.24592).

### Lean

On 2026-11-26, `MinimalModel.HanLiuEncACC` (S52) and `MinimalModel.HanLiuReduction` (S29) are not in `records/lean.json`. The module note of `MinimalModel/Statements/Boundedness.lean` says that S52 needs the definition of an enc germ, which is not in `Basic.lean` yet. The node plans S52 for milestone S1 and S29 for milestone S2. Spec 13.3 names a node `MM4T0RCENC` for the toric case of S52. The map has no node with this tag on 2026-11-26.

Target O-R4-2 is the Han-Liu reduction in Lean, over named hypotheses (difficulty 2). The map gives S29 the kind theorem, because the agent of the project has no kind for a reduction.

### Notes and history

**Claims of 2025 and 2026.** The records hold no claim of S52, in the toric case or in general.

**Routes.** Route R3 (weight 0.15) has O-R3-3 and O-R3-4, with the first nodes `toric-fan`, `toric-wall-relation`, `toric-cone-theorem`, `toric-flip`, `toric-termination` and `toric-mld`. Step 7 of R3 is toric log discrepancies and mlds, and step 8 is the toric ACC and LSC. Route R4 has O-R4-2 and O-R4-8 (Conjecture 7.5 of Han and Liu for $N = 1$ in dimension 4, difficulty 2). The lab has E2.

**References.** HL25; Amb99; Rei83 and FS04 for the toric program; arXiv:2606.24592 (Nakamura and Shibata). Volume 3 treats the toric program.

**Questions for a reader.**

- What is the exact definition of an enc germ in HL25, and does the column "enc" of the run of E2 follow it?
- Which statement of Han and Liu is the source of the arrow "Conjecture 1.9(2') in dimension 4 gives T(4) for lc flips", and does it need the termination of terminal 4-fold flips as a second input?
- How many $GL(4, \mathbb{Z})$ orbits of simplicial cones of index at most 12 are there?
