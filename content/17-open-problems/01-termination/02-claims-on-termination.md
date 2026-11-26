---
title: The claims of 2025 and 2026 on termination
nodes: [MMBTDMD2XP, MMY38TT73M, MM2NY6352R, MMQMD68H79, MMDQRR7TZB]
sources: [OAI26, AxiomMMP, HLZ25, BCHM10, Bir12, HX13]
reads_with: []
requires: ["10", "16"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The claims of 2025 and 2026 on termination

### Statement

Four claims of 2025 and 2026 bear on termination. None of them is refereed. The records give each one the class claimed, and no proof in the handbook uses one as a hypothesis.

**Remark 17.1.8 (Claim C1: termination for lc 4-folds with rational boundary).** Let $(X, \Delta)$ be a projective lc pair of dimension 4 over an algebraically closed field of characteristic 0, with $\Delta$ a $\mathbb{Q}$-divisor. Then each $(K_X + \Delta)$-program terminates.

Node: MMBTDMD2XP · Lean: `MinimalModel.TerminationLc4Rational`

This is statement S22. It is claimed by the OpenAI problem family 056 (OAI26) and by its Lean formalization in AxiomMath/MMP (AxiomMMP).

**Remark 17.1.9 (Termination for a big boundary in dimension at most 5).** Let $(X, \Delta)$ be a projective klt pair of dimension $n \le 5$ with $\Delta$ big or $K_X + \Delta$ big. Then each $(K_X + \Delta)$-program terminates.

Node: MMY38TT73M · Lean: `MinimalModel.TerminationBigLe5`

This is statement S24, claimed by Han, Liu and Zhuang (HLZ25, arXiv:2509.01501).

**Remark 17.1.10 (Claim C2: termination for a big boundary in all dimensions).** Let $(X, \Delta)$ be a projective klt pair of any dimension with $\Delta$ big or $K_X + \Delta$ big. Then each $(K_X + \Delta)$-program terminates.

Node: MM2NY6352R · Lean: `MinimalModel.TerminationBig`

This is statement S25, claimed by Hashizume (arXiv:2609.33679).

**Remark 17.1.11 (Claim C5: flips for lc generalized pairs).** Flips exist for all lc generalized pairs, with no NQC hypothesis and no $\mathbb{Q}$-factorial hypothesis.

Node: MMQMD68H79 · Lean: `MinimalModel.GeneralizedLcFlips`

This is statement S27, claimed by Hu and Liu (arXiv:2603.03817). For usual lc pairs, flips exist by a refereed theorem.

**Theorem 17.1.12 (Existence of lc flips).** Let $(X, \Delta)$ be a projective lc pair and $f \colon X \to Z$ a flipping contraction. Then the flip of $f$ exists.

Node: MMDQRR7TZB · Lean: `MinimalModel.LcFlips`

### Proof in words

**C1, OpenAI 056 and AxiomMath/MMP.** OpenAI released problem family 056 on 2026-09-24, as part of a release of AI-written manuscripts. AxiomMath posted a Lean formalization on 2026-11-16. The pinned commit is `1f9ade3670`, under Apache-2.0, on Lean v4.35.0, Mathlib `56a005855e` and AxiomMath/Stacks `c496df0d9b`. The code has 2,269 files and about 2.05 million lines. Its main theorems are `MMP.Fourfold.Program.IsMaximal.isNefOnCurves_or_isMoriFibreSpace`, `MMP.Fourfold.Program.isContinuableRay`, `MMP.Fourfold.Program.n_ne_top_of_isAlgClosed` and `MMP.Fourfold.projectiveLowerLogMMP_three`. The hypotheses are: $k$ algebraically closed of characteristic 0; $X$ projective, integral and normal; a rational boundary. There is no $\mathbb{Q}$-factorial hypothesis and no pseudo-effective hypothesis. The README of the repository says that no human has reviewed the code, and that abundance is out of scope.

The Lean kernel checked the inferences of the code. The open question is a different one: do the Lean definitions mean the textbook notions? Spec 01.13 puts it so: for C1 the question is no longer "is the paper right" but "do the Lean definitions mean the textbook notions". The audit of Section 7.3 answers that question. If it passes, the records change S22 from claimed to `proved-ext`. If it finds a fault of severity 1, a wrong meaning, S22 stays claimed.

**S24, Han-Liu-Zhuang.** The preprint arXiv:2509.01501 claims termination of each program for a klt pair with a big boundary or a big $K + \Delta$ in dimension at most 5, with explicit bounds on the number of steps in dimension at most 4. It uses the uniform index bound of Han, Qi and Zhuang (arXiv:2506.20183). Han, Qi and Zhuang also show that the minimal log discrepancies in a program of general type take finitely many values. The paper record HLZ25 has the expert status claimed. The records have no claim record in `claims/` for this preprint.

**C2, Hashizume.** The preprint arXiv:2609.33679 (v2 of 2026-10-13) claims full termination for klt pairs with $\Delta$ or $K + \Delta$ big in all dimensions, the finiteness of marked Mori fibre spaces, and the strong Sarkisov program (Section 1.3). The records say that ChatGPT and Codex wrote drafts and that the author revised them. Spec 03.11 gives the arrows: the HQZ index bound gives termination for general type in dimension at most 5 (HLZ), and HLZ gives termination for a big boundary in all dimensions (Hashizume).

**C5, Hu-Liu.** The preprint arXiv:2603.03817 claims flips for all lc generalized pairs. It also claims that the existence of minimal models for lc generalized pairs is equivalent to termination with scaling. For klt generalized pairs with the NQC condition, flips exist by Hacon and Liu (arXiv:2105.13590). For usual lc pairs, flips exist by Birkar (Bir12) and Hacon-Xu (HX13).

The records give the shape of the claims for a big boundary only through target O-R1-5 of route R1. There the core is the finiteness of the set of models that a program meets, with two inputs as hypotheses: the HQZ index bound, and the finiteness of models of BCHM (statement S34, the statement $E_n$ of the induction of BCHM10: for a rational polytope of klt boundaries with a fixed big part, there are finitely many log terminal models). The records do not say more about the inner steps of the proofs.

### Examples

The first test case of C1 is a positive instance: a program in AxiomMath/MMP that runs to its end on a known 4-fold. Audit step A6 asks for one, for $\mathrm{Bl}_p\mathbb{P}^2 \times \mathbb{P}^2$ or a toric 4-fold, if the API allows. The same step asks for the triviality attack: an attempt to prove each main statement from assumptions that are like `False`, or from empty types. A main theorem that holds for a vacuous reason is a fault of severity 1.

The first test case of S24 is a bound that can be computed. Target O-R1-10 asks for the HLZ bound as a computable function and a certificate on examples. Experiment E8 of the lab evaluates the bounds in dimension at most 4 and compares them with the lengths of toric runs (E9) and with the 3-fold examples of the handbook. On 2026-11-26 the lab has no record of E8.

The first test case of C2 is its combinatorial core: the set of models that a program meets is finite, given the HQZ index bound and the BCHM finiteness of models as hypotheses (target O-R1-5).

### Lean

On 2026-11-26 the library mmp-lean (commit 6e779d01) states S22, S24 and S25 in `MinimalModel/Statements/Termination.lean`. `MinimalModel.TerminationLc4Rational` says: for each pair of dimension 4 that is lc and has a rational boundary, `¬ HasInfiniteProgram A`. So it is about each sequence of steps, not only about flips. `MinimalModel.TerminationBigLe5` and `MinimalModel.TerminationBig n` have the same conclusion for klt pairs with $\Delta$ big or $K + \Delta$ big. Each docstring says that the class is claimed and that the statement is never a hypothesis of another proof (spec 06.6).

`MinimalModel.GeneralizedLcFlips` (S27) is not in `records/lean.json`. Generalized pairs are not in the vocabulary of the library yet.

The bridge `MinimalModelBridge` of spec 09.4 is the place where S20 to S24 are to be proved from the theorems of AxiomMath/MMP (audit step A8). On 2026-11-26 it does not exist.

### Notes and history

**Status of the records on 2026-11-26.**

| Claim | Statement | Record | Status | Parts checked |
|---|---|---|---|---|
| C1, OpenAI 056 and AxiomMath/MMP | S22 | `claims/AxiomMath-MMP.yaml` | fresh | none |
| Han-Liu-Zhuang | S24 | paper record HLZ25 only | expert status claimed | none |
| C2, Hashizume | S25 | `claims/arXiv-2609-33679.yaml` | fresh | none |
| C5, Hu-Liu | S27 | `claims/arXiv-2603-03817.yaml` | fresh | none |

Each claim record says: "Nobody has read the claim for the project yet." Item 4 of spec 01.16 asks for the referee status of Hashizume, HLZ and HQZ.

**Routes.** Route R2 (weight 0.15) audits C1 in eight steps (Section 7.3). Its targets are O-R2-1 (T(4) for a rational boundary), O-R2-2 (the surface and 3-fold programs of AxiomMath/MMP bridged to S10 to S19), O-R2-3 (the port of Kawamata-Viehweg vanishing), O-R2-4 (real boundary) and O-R2-5 (klt Kähler 4-folds, the Kähler part of OpenAI 056). Route R1 (weight 0.20) has O-R1-5 for Hashizume, O-R1-8 for Hu-Liu as a reduction node, and O-R1-10 for the HLZ bounds.

**References.** OAI26 and AxiomMMP for C1; HLZ25; arXiv:2609.33679 (Hashizume); arXiv:2603.03817 (Hu-Liu); arXiv:2506.20183 (Han-Qi-Zhuang); BCHM10; Bir12 and HX13 for lc flips. Volume 16 reports dimension 4 in more detail.

**Questions for a reader.**

- `TerminationLc4Rational` concludes `¬ HasInfiniteProgram`, while AxiomMath/MMP states `n_ne_top_of_isAlgClosed` for a `Program`. Do the two notions of a program agree? Audit step A6 asks whether `n_ne_top` says that every program terminates, not that one does.
- Does the proof of C1 use the rationality of the boundary in an essential way? Target O-R2-4 asks this.
- Which statements of Hashizume rest on HLZ and HQZ, and which are new?
