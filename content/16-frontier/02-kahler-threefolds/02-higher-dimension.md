---
title: "Kähler spaces in higher dimension: the claims of 2026"
nodes: [MMK4VRWSWA, MMBTDMD2XP]
sources: [HP16, OAI26, AxiomMMP, BCHM10]
reads_with: []
requires: ["9", "16.2"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Kähler spaces in higher dimension: the claims of 2026

### Statement

In dimension 4 and higher the Kähler program has no refereed general result on 2026-11-28. The records list two preprints of 2026 that claim large parts of it, one preprint on abundance, and the Kähler part of an OpenAI manuscript. None of them is refereed, and each is claimed.

**Remark 16.2.6 (claim C11: big gklt Kähler pairs, Hacon and Xie).** The minimal model program runs for big gklt Kähler pairs in all dimensions, and Tosatti's transcendental basepoint-free conjecture holds.

This is claimed in arXiv:2607.24986 (v2 of 2026-11-22). The records state the claim in these words only and do not give its exact hypotheses. Tosatti's conjecture is the transcendental analogue of the basepoint free theorem: a nef and big class $\alpha$ such that $\alpha - K_X$ is nef and big is the pullback of a Kähler class by a morphism.

**Remark 16.2.7 (claim C10: termination with scaling, Hacon and Wang).** For compact Kähler klt pairs, the program with scaling terminates (for klt flips), and good minimal models exist, with two OpenAI manuscripts as input.

This is claimed in arXiv:2611.29683, posted on 2026-11-22. Spec 01.3 records that its Corollary 1.2 rests on the claim C3 (OpenAI family 034, log abundance in all dimensions), which one tracker lists as contested at the step of log Iitaka subadditivity. So Corollary 1.2 is a claim that rests on a contested claim.

**Conjecture 16.2.8 (the Kähler program in dimension 4).** Let $X$ be a $\mathbb{Q}$-factorial compact Kähler 4-fold with terminal singularities. Then a program of divisorial contractions and flips from $X$ exists and ends with a model with nef canonical class or with a Mori fibre space.

This is target O-R9-2 of route R9, of mathematical difficulty 4. It is open. The claims C10 and C11 cover parts of it: C11 the case of a big boundary, C10 the program with scaling.

**Conjecture 16.2.9 (non-vanishing for compact Kähler manifolds).** Let $X$ be a compact Kähler manifold with $K_X$ pseudo-effective. Then $\kappa(X) \ge 0$.

This is target O-R9-4, of mathematical difficulty 5. It is open in dimension at least 4 as in the projective case, and the Kähler form contains the projective conjecture.

### Proof in words

The records do not describe the proofs of C10 and C11, and nobody has read them for the project. What the records give is their dependencies. The claim C10 uses two OpenAI manuscripts, and its Corollary 1.2 rests on C3. Target O-R1-11 of route R1 (the same as O-R9-1) is a citation audit of C10: which statements of which AI manuscripts it uses, and whether each is a claim or a theorem. Its mathematical and formal difficulties are both 1. On 2026-11-28 the audit has not started.

Two other lines of 2026 bear on the Kähler program, as spec 01.5 records them. Z. Jiang (arXiv:2604.03879) gives Kähler abundance through the algebraic reduction in some 4-fold cases. The program for projective morphisms of complex analytic spaces is mature: Fujino (arXiv:2201.11315), Das-Hacon-Păun for analytic flips, Lyu-Murayama (arXiv:2209.08732) for excellent schemes, formal schemes and analytic germs, Enokizono-Hashizume (arXiv:2404.05126) for lc pairs, and Landi (arXiv:2611.15899) for slc pairs. The relative analytic program is the tool by which the 3-fold flips of Section 16.2.1 are local over the base. A compact Kähler space that is not projective over a point is outside its scope.

The OpenAI manuscript of family 056 (OAI26), the source of the claim C1, also has a Kähler part: termination for klt Kähler 4-folds. This is target O-R2-5 of route R2, of mathematical difficulty 4 and formal difficulty 5. The Lean code of AxiomMath/MMP does not cover it: it works with projective schemes over a field. Spec 01.3 adds that on 2026-10-07 three papers of the OpenAI release were retracted and fourteen revised, and that six of the revised papers are on Kähler programs and abundance.

### Examples

**Example 16.2.10 (a 4-fold that only a Kähler program sees).** Let $T$ be a general complex torus of dimension 4 and $X = \mathrm{Bl}_p T$, with exceptional divisor $E \cong \mathbb{P}^3$. Then $K_X = 3E$, a line $l \subset E$ has $K_X \cdot l = -3$, and every curve of $X$ lies in $E$. The only step of the program is the contraction $X \to T$, and $K_T = 0$. So this case of the 4-fold Kähler program is easy: a divisorial contraction whose existence is the blow-down. The open part of O-R9-2 is the flips, which need a contraction theorem for small rays in $\overline{NA}(X)$ and a flip theorem over a non-projective base.

**Example 16.2.11 (where the claim C10 meets the claim C3).** Good minimal models in C10 mean minimal models on which $K + B$ is semiample. For a klt pair with $K + B$ nef, semiampleness is abundance, and in the projective case with rational boundary it is the claim C3. A compact Kähler klt pair that is projective is a projective klt pair. So the projective case of the good minimal models of C10 contains a case of abundance, and a proof of it would need an input of the strength of C3. This is consistent with the record that Corollary 1.2 of C10 rests on C3.

### Lean

Kähler spaces are absent from Mathlib (spec 04.10, the key obstruction of route R9). The library mmp-lean states no Kähler statement on 2026-11-28; S59 is in the plan with vocabulary missing. The statement S22 of the claim C1, `MinimalModel.TerminationLc4Rational`, is about projective pairs and does not include the Kähler part of OpenAI 056.

Node: MMBTDMD2XP · Lean: `MinimalModel.TerminationLc4Rational`

S22 is claimed. Section 16.4.2 gives the audit that would change its class.

### Notes and history

**Status of the records on 2026-11-28.**

| Claim | Source | Record | Status | Parts checked |
|---|---|---|---|---|
| C10, Hacon-Wang | arXiv:2611.29683 | `claims/arXiv-2611-29683.yaml` | fresh | none |
| C11, Hacon-Xie | arXiv:2607.24986 v2 | `claims/arXiv-2607-24986.yaml` | fresh | none |
| Kähler part of C1 | OpenAI 056 | `claims/AxiomMath-MMP.yaml` (for C1 as a whole) | fresh | none |

Neither C10 nor C11 has a node in the map. Each record says: "Nobody has read the claim for the project yet." Route R9 has the first weight 0.05 and the targets O-R9-1 to O-R9-4; on 2026-11-28 none of them has a record of progress.

**References.** HP16 for the 3-fold program; arXiv:2607.24986 (Hacon-Xie); arXiv:2611.29683 (Hacon-Wang); arXiv:2604.03879 (Z. Jiang); OAI26 and AxiomMMP for C1; BCHM10 for the projective program with scaling that C10 extends.

**Questions for a reader.**

- Which two OpenAI manuscripts does C10 use, and is either of them among the papers that the release retracted or revised on 2026-10-07?
- Does the claim C11 for a big boundary reduce, as in BCHM, to a finiteness of models, and does that finiteness need projectivity anywhere?
