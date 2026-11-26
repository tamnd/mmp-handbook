---
title: The Kähler and analytic program
nodes: [MMK4VRWSWA, MMPTP8SV13, MMZ5XGBW5M]
sources: [BCHM10]
reads_with: []
requires: ["16"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Kähler and analytic program

### Statement

**Theorem 17.6.4 (The program for Kähler 3-folds).** The minimal model program holds for compact Kähler 3-folds.

Node: MMK4VRWSWA · Lean: `MinimalModel.KahlerThreefoldMMP`

This is statement S59.

**Conjecture 17.6.5 (The Kähler program in dimension 4).** The minimal model program holds for compact Kähler 4-folds.

The map has no node for this problem. It is target O-R9-2 (difficulty 4), and it is open in the records. Claim C11 below covers the big case in all dimensions.

**Conjecture 17.6.6 (Non-vanishing for compact Kähler manifolds).** Let $X$ be a compact Kähler manifold with $K_X$ pseudo-effective. Then $\kappa(X) \ge 0$.

The map has no node for this problem. It is target O-R9-4 (difficulty 5). The records do not state it in a sentence; the statement above is the Kähler form of non-vanishing (S41, Section 2.1), which is open.

**Remark 17.6.7 (Claim C11: the program for big gklt Kähler pairs).** The minimal model program holds for big gklt Kähler pairs in all dimensions, and the transcendental base point free conjecture of Tosatti holds.

This is claimed by Hacon and Xie (arXiv:2607.24986, v2 of 2026-11-22).

**Remark 17.6.8 (Claim C10: termination with scaling for Kähler klt pairs).** Flips with scaling terminate for compact Kähler klt pairs, and good minimal models exist.

This is claimed by Hacon and Wang (arXiv:2611.29683, posted 2026-11-22), with two OpenAI manuscripts as input. Its Corollary 1.2 rests on claim C3, the claimed log abundance of OpenAI 034 (Section 2.2). The records do not say which hypotheses the claim puts on the pair.

### Proof in words

**What is known, by dimension** (spec 01.5):

- **Dimension 3.** The Kähler 3-fold program is complete. The program is due to Höring and Peternell (Invent. Math. 2016) and to Das and Hacon. Abundance is due to Campana, Höring and Peternell (Ann. ENS 2016), log abundance to Das and Ou, and slc abundance to S. Das (arXiv:2604.28085) [P][S].
- **Dimension 4.** Z. Jiang (arXiv:2604.03879) gives Kähler abundance through the algebraic reduction in some 4-fold cases [P]. The records do not say which cases.
- **All dimensions.** Only the claims C10 and C11.

**The analytic program.** The program for projective morphisms of complex analytic spaces is mature (spec 01.5): Fujino (arXiv:2201.11315, a preprint), Das, Hacon and Păun (analytic flips, Adv. Math. 2024), Lyu and Murayama (arXiv:2209.08732, for excellent schemes, formal schemes, analytic germs, and rigid and Berkovich spaces in equal characteristic 0), Enokizono and Hashizume (arXiv:2404.05126) for lc pairs, and Landi (arXiv:2611.15899) for slc pairs [P]. This preprint of Landi is not the withdrawn claim C16 of Section 3.2. Spec 01.5 lists no open problem for it. The open problems of this section are on compact Kähler manifolds.

Spec 04.10 names the obstruction for the mathematics in three words: "currents replace curves". The records do not say more.

**How C10 depends on the other claims.** Claim C10 uses two OpenAI manuscripts, and its Corollary 1.2 rests on C3. So C10 is a claim on a claim: if C3 fails, Corollary 1.2 of C10 loses its proof. Target O-R9-1 (the same as O-R1-11) is a citation audit of C10: which statements of which AI manuscripts it uses, and whether each one is a claim or a theorem (difficulty 1, formal check 1).

### Examples

The first test cases in the records:

- The citation audit of Hacon and Wang: O-R9-1 (difficulty 1).
- b-semiampleness for Kähler morphisms of relative dimension 1: O-R9-3 (difficulty 2; Section 2.3).
- The Kähler program in dimension 4: O-R9-2 (difficulty 4).
- Kähler non-vanishing: O-R9-4 (difficulty 5).

Volume 16 treats the Kähler program for 3-folds (spec 11).

### Lean

On 2026-11-26, `MinimalModel.KahlerThreefoldMMP` (S59) is not in `records/lean.json`. The node plans it in `MinimalModel/Statements/OtherSettings.lean` for milestone S6. Its vocabulary is missing: spec 04.10 says that Kähler manifolds are absent from Mathlib. The first nodes of route R9 are `kahler-pair-def` and `kahler-mmp-statement`; the map has the second as S59. The library states S40 and S41 only for projective varieties over a field (`MinimalModel.Abundance`, `MinimalModel.NonVanishing`), so a Kähler form of either needs a new family of statements.

### Notes and history

**Claims of 2025 and 2026.**

| Claim | What it claims | Record | Status |
|---|---|---|---|
| C10, Hacon-Wang | termination of klt flips with scaling for compact Kähler klt pairs; good minimal models | `claims/arXiv-2611-29683.yaml` | fresh; unrefereed; Cor. 1.2 rests on C3 |
| C11, Hacon-Xie | the program for big gklt Kähler pairs in all dimensions; Tosatti's transcendental base point free conjecture | `claims/arXiv-2607-24986.yaml` | fresh; unrefereed |

Each record says: "Nobody has read the claim for the project yet." Spec 01.3 adds that six of the 14 papers of the OpenAI release that were revised on 2026-10-07 are on Kähler programs and abundance.

**Routes.** Route R9 (weight 0.05) has O-R9-1 to O-R9-4. Spec 04.10 says that the route checks the dependencies of the new claims and states the Kähler program as a separate family. Route R1 has O-R1-11.

**References.** BCHM10 for the projective program; arXiv:2607.24986 (Hacon and Xie); arXiv:2611.29683 (Hacon and Wang); arXiv:2604.28085 (S. Das); arXiv:2604.03879 (Z. Jiang); arXiv:2201.11315 (Fujino); arXiv:2209.08732 (Lyu and Murayama); arXiv:2404.05126 (Enokizono and Hashizume); arXiv:2611.15899 (Landi). Volume 16 treats the Kähler program.

**Questions for a reader.**

- Which statements of the two OpenAI manuscripts does C10 use, and is either of them in a family that was revised or retracted on 2026-10-07?
- Does C11 imply the Kähler program in dimension 4 for big pairs, and so a case of O-R9-2?
- In which 4-fold cases does Z. Jiang prove Kähler abundance?
