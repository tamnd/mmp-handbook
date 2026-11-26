---
title: The routes, the milestones and the gaps of Lean
nodes: [MMXCD16PTN, MMWK2DDDPC, MMFKZ7VB29]
sources: [Rei83, Amb99, HL25, Sho04]
reads_with: []
requires: ["0"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The routes, the milestones and the gaps of Lean

### Statement

**Remark 17.7.7 (The routes and their weights).** Spec 04.1 divides the work of the project into nine routes and the lab. Each route has a weight, the share of the effort that the project puts on it in the first year.

| Route | Subject | Weight | Chapters |
|---|---|---|---|
| R1 | formal checks of fresh claims | 0.20 | all; Section 7.2 |
| R2 | the audit and bridge of AxiomMath/MMP | 0.15 | 1, 7 |
| R3 | the toric program and toric invariants | 0.15 | 3 |
| R4 | termination through the ACC and the LSC | 0.10 | 1, 3 |
| R5 | abundance and non-vanishing | 0.10 | 2 |
| R6 | boundedness, Calabi-Yau varieties, the cone conjecture and effective results | 0.10 | 4 |
| R7 | characteristic $p$ and mixed characteristic | 0.05 | 5 |
| R8 | foliations | 0.05 | 6 |
| R9 | Kähler and analytic | 0.05 | 6 |
| Lab | the computation lab | 0.05 | 3, 4 |

Spec 16, Q-06, keeps these weights for the first year. They change only at the milestone reports, from the proved, refuted and stalled nodes.

**Conjecture 17.7.8 (Target T).** The project names one open target for level G5: target O-R3-3, the conjecture 1.9(2') of Han and Liu (HL25) for enc 4-fold germs that are toric. Section 3.3 gives it.

Node: MMXCD16PTN · Lean: `MinimalModel.HanLiuEncACC`

S52 is a conjecture, and it has no Lean statement on 2026-11-26.

### Proof in words

**Why Target T** (spec 04.12). It is open, and report D of the records rates it at the small end of its scale. It is convex geometry over $\mathbb{Z}^4$, on the infrastructure of route R3. It is on the reduction graph: the full conjecture in dimension 4 gives T(4) for lc flips, so a toric case is a human proof of a piece of T(4) that does not rest on AI code. The lab can search the cones first, with experiment E2. The backups are O-R6-2 (the questions of Ajit, with the lab) and O-R8-1 (a question on foliations on surfaces). The project reviews the choice at milestone S3.

**The milestones** (spec 15). Each milestone gives a new dated report of this volume.

| Milestone | Date | Release | Main items |
|---|---|---|---|
| S0 | 2026-12-20 | the records do not say | the records do not say |
| S1 | 2027-02-28 | v0.2.0 | the check of Ajit (S57, E3) with the letter sent; E1 run; audit steps A3 and A4 done; Volume 17, the first dated report |
| S2 | 2027-04-30 | v0.3.0 | the toric `coneTheorem`; E2 in dimension 3 |
| S3 | 2027-06-30 | v0.4.0 | the audit closes and the decision on S22; `shokurovLemma` proved; E2 in dimension 4 to index 6; the review of Target T |
| S4 | 2027-09-30 | the records do not say | the toric program |
| S5 | 2027-12-31 | v1.0.0 | surfaces; `HanLiuReduction` proved-mod |
| S6 | 2028-04-30 | the records do not say | the scheme dictionary; S59 and S60 stated |
| S7 | 2028-08-31 | the records do not say | Target T proved or refuted in Lean, with a preprint |
| S8 | 2028-12-31 | the records do not say | the records do not say |
| S9 | open | v2.0.0 | an open case (level G5) |

The record `records/trust.json` lists the planned theorems of the milestones. On 2026-11-26, `Toric.coneTheorem`, `shokurovLemma`, `Toric.flipExists`, `Toric.terminationOfFlips`, `Surface.minimalModel` and `Toric.hanLiuEncACC` are not in the map. `Toric.mmp`, `Surface.castelnuovo` and `Reductions.hanLiu` are in the map and unstated.

**The lab** (spec 13.4). The lab has ten experiments, E1 to E10.

- E1: the baskets and plurigenera of 3-folds of general type (Section 4.1).
- E2: toric mlds and enc germs (Sections 3.1 and 3.3).
- E3: the arithmetic of the counterexamples of Ajit (Section 4.2).
- E4: the questions of Ajit on weighted hypersurfaces (Section 4.2).
- E5: Fano and general type volumes (Section 4.1).
- E6: the cone conjecture for one deformation class of Calabi-Yau 3-folds (Section 4.1).
- E7: characteristic $p$: $F$-purity and the LSC for hyperquotients (Section 5.1).
- E8: the explicit bounds of Han, Liu and Zhuang (Section 1.2).
- E9: runs of the toric program in dimension 3 and 4.
- E10: the explicit identities and numbers of each new claim of route R1 (Section 7.2).

On 2026-11-26 the lab has one run, `2026-11-26-e2-cyclic-quotient-mld-3-6d070b98`, from the spec `lab/specs/e2-cyclic-quotient-mld-3.yaml`. The other nine experiments have no run. Spec 04.1 gives the limit of the lab in three words: "data is not proof".

**The gaps of Lean.** The pinned toolchain is Lean v4.35.0 with Mathlib v4.35.0. Spec 01.11 lists what Mathlib lacks for the program:

- Cartier divisors, the Picard group of a scheme and line bundles on schemes;
- ample and nef divisors, and intersection numbers;
- normal schemes as a class, and blow-ups;
- the finiteness of coherent cohomology, and the cohomology of $\mathcal{O}(d)$ on $\mathbb{P}^n$;
- Serre duality, the vanishing theorems and Riemann-Roch;
- Kähler manifolds and toric varieties.

Spec 05.7 lists what the base of the project does not give:

1. the finiteness of coherent cohomology, Serre duality, Riemann-Roch and the vanishing theorems, which stay named hypotheses until milestone S6;
2. resolution of singularities, which is the hypothesis `HasLogResolution`, shared with spec 2161;
3. the finite dimension of $N^1$, which is a hypothesis;
4. a reviewed program;
5. anything toric;
6. Kähler geometry and foliations, which have statements only.

**The risks of a wrong statement.** Spec 06.5 ranks ten risks. The first is the most important for this volume: "some program terminates" in place of "every program terminates". The first is a theorem with scaling (BCHM). The second is the conjecture. A statement with the quantifier in the wrong place proves a known theorem and claims an open one. The other nine risks are: a flip that is not a flip; a hidden or dropped hypothesis; the definition of the numerical dimension; the conventions of discrepancy; the cone of curves; $\mathbb{Q}$ and $\mathbb{R}$; universe and size; hypotheses with no model; and relative against absolute. The fidelity battery F1 to F7 of spec 06.3 tests each risk.

### Examples

The first test of the gaps is the toric world. Route R3 builds fans, cones and the toric program in Lean, so the toric case of each statement can be a positive instance (check F2) without the scheme layer. The first planned theorem is the toric cone theorem, at milestone S2. Rei83 is the source of the toric program and Amb99 of the toric mlds.

Node: MMWK2DDDPC · Lean: `MinimalModel.ACCMld`

The ACC for mlds (S49) is open. Its Lean statement needs the mld, and the mld needs valuations or log resolutions. This is the gap of item 2 of spec 05.7.

Node: MMFKZ7VB29 · Lean: `MinimalModel.LSCMld`

The LSC for mlds (S50) is open. With S49 it gives termination by the reduction of Sho04 (S28).

### Lean

Spec 06.2.2 gives each statement a row, and a statement with missing vocabulary has the status unstated with `needs` edges to the missing definitions (row G1b). On 2026-11-26, 24 statements are unstated. Some of them wait for the vocabulary of the lists above: S58 waits for Frobenius singularities, S59 for Kähler manifolds, S60 for foliations, and S39 for toric varieties.

### Notes and history

**What the next report must give.** The next report is due at milestone S1. It must give the new state of each cell of Section 7.1, of each claim of Section 7.2 and of each audit step of Section 7.3, and the weights of the routes after the review.

**References.** Rei83 for the toric program; Amb99 for toric mlds; HL25 for Target T; Sho04 for the reduction. Volume 0 gives the plan of the handbook.

**Questions for a reader.**

- Which item of spec 05.7 blocks the most statements of the map?
- Must the planned theorems that are not in the map, such as `Toric.coneTheorem`, get nodes before milestone S2?
- Does the choice of Target T need to change after the first run of E2?
