---
title: Minimal models and non-vanishing
nodes: [MMY4HT1Q8M, MMZ5XGBW5M, MM9399B0QP, MME79K17YJ, MMQMD68H79]
sources: [BCHM10, Mor25, BDPP13]
reads_with: []
requires: ["9", "10"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Minimal models and non-vanishing

### Statement

**Conjecture 17.2.1 (The minimal model conjecture).** Let $(X, \Delta)$ be a projective lc pair of dimension $n$ with $K_X + \Delta$ pseudo-effective. Then $(X, \Delta)$ has a minimal model.

Node: MMY4HT1Q8M · Lean: `MinimalModel.MinimalModelConj`

This is statement S33. It is open in general.

**Conjecture 17.2.2 (Non-vanishing).** Let $(X, \Delta)$ be a projective lc pair of dimension $n$ with $K_X + \Delta$ pseudo-effective. Then $\kappa(X, K_X + \Delta) \ge 0$: some multiple of $K_X + \Delta$ is linearly equivalent to an effective divisor.

Node: MMZ5XGBW5M · Lean: `MinimalModel.NonVanishing`

This is statement S41. It is open for $n \ge 4$. Spec 01.2 calls it the central open problem of the program: every conditional abundance result of the records uses it.

**Theorem 17.2.3 (BCHM).** Let $(X, \Delta)$ be a projective klt pair of log general type. Then $(X, \Delta)$ has a minimal model.

Node: MM9399B0QP · Lean: `MinimalModel.BCHM`

### Proof in words

**Minimal models, by dimension.**

- Dimension at most 3: minimal models exist, by the 3-fold program (Volume 8).
- Dimension 4: termination holds for lc 4-folds with $K + \Delta$ pseudo-effective (Mor25, statement S21), and lc flips exist (statement S26). A program for such a pair cannot end with a Mori fibre space, so it ends with a minimal model. The records do not state this consequence as a node. The docstring of `MinimalModel.MinimalModelConj` says that S33 is open for $n \ge 4$, and the table of spec 01.1 gives the open case as "lc pairs with $K + \Delta$ pseudo-effective, $\dim \ge 5$". The two records differ on $n = 4$.
- Dimension 5: Birkar (arXiv:0706.1792) gives minimal models for $\kappa \ge 0$ in dimension 5 (spec 07, row T7-05).
- Each dimension: BCHM give minimal models for klt pairs of log general type (BCHM10). Birkar (arXiv:0907.4170) shows that weak non-vanishing implies the existence of minimal models.

So the minimal model conjecture reduces to a form of non-vanishing. A second reduction for lc generalized pairs is claimed by Hu and Liu: the existence of minimal models is equivalent to termination with scaling (arXiv:2603.03817, claim C5, Section 1.2). Spec 03.11 rates the source of that arrow [S].

**Non-vanishing, by dimension.**

- Dimension at most 3: non-vanishing holds, as a part of abundance for 3-folds (statement S17).
- Dimension 4 and higher: open.

The records give three reductions. Hashizume (arXiv:1609.00121) and Lazić-Tsakanikas (Publ. RIMS 58 (2022)) reduce non-vanishing and minimal models to smooth varieties (spec 07, row T9-07). Lazić and Meng show that non-vanishing in dimension $n - 1$ gives non-vanishing for uniruled lc pairs of dimension $n$ (spec 03.11). Since non-vanishing holds in dimension 3, the uniruled case of dimension 4 follows. For a smooth projective variety with $\Delta = 0$, $K_X$ is pseudo-effective exactly when $X$ is not uniruled (BDPP13).

So the hardest case is a smooth projective 4-fold $X$ that is not uniruled, with $\Delta = 0$ and $K_X$ pseudo-effective. Spec 01.2 names this case and rates the claim [U]. The conjecture asks for one $m > 0$ with $H^0(X, mK_X) \ne 0$. Spec 04.6 says that no one has a strategy for it.

### Examples

The first test case of non-vanishing is the core case of the records: a smooth projective 4-fold that is not uniruled, with $K_X$ pseudo-effective (target O-R5-1). Spec 04.6 rates it 4 on the scale of 1 to 5.

The first test case of the minimal model conjecture is the case of dimension 5 with $\kappa = -\infty$ and $K + \Delta$ pseudo-effective. Birkar covers $\kappa \ge 0$ in dimension 5, and non-vanishing would rule out $\kappa = -\infty$. So the smallest case that is open in the records is the one that non-vanishing in dimension 5 would remove.

A known instance that the library can state is the big case. If $\Delta$ is big, or $K + \Delta$ is big, then $\kappa(K + \Delta) = n \ge 0$, and BCHM give a minimal model for a klt pair. These are the positive instances of S33 and S41 that the fidelity checks of spec 06.3 can use.

### Lean

On 2026-11-26 the library states S33 as `MinimalModel.MinimalModelConj n` in `MinimalModel/Statements/Models.lean`: each projective lc pair of dimension `n` with `K + Δ` pseudo-effective has a minimal model in the sense of KM98, Definition 3.50. It states S41 as `MinimalModel.NonVanishing n` in `MinimalModel/Statements/Abundance.lean`: if `K + Δ` is pseudo-effective, it is $\mathbb{R}$-linearly equivalent to an effective divisor. The Lean form uses $\mathbb{R}$-linear equivalence, while the node text uses $\kappa \ge 0$. For a boundary with real coefficients the two forms can differ, and the fidelity check of the statement must compare them.

`MinimalModel.BCHM` (S31) is not in `records/lean.json` yet. The library has `iitakaDim` and `numericalDim` as definitions.

### Notes and history

**Claims of 2025 and 2026.** OpenAI family 034 (claim C3, in `claims/openai-math.yaml`, status fresh) claims canonical non-vanishing and 4-fold non-vanishing, with log abundance. One tracker marks the family "Contested", at the step of log Iitaka subadditivity [S]. No Lean proof exists for the family. Hu-Liu (C5, `claims/arXiv-2603-03817.yaml`, status fresh) claim the equivalence of minimal models and termination with scaling for lc generalized pairs. The records say for each: "Nobody has read the claim for the project yet."

**Routes.** Route R5 (weight 0.10) has O-R5-1, non-vanishing in dimension 4. Its first nodes include `nonvanishing-statement`, `red-birkar-nv-mm` and `red-lazic-meng`: the reductions of Birkar and of Lazić-Meng as implications between named statements. Route R1 has O-R1-6, the dependency map of OpenAI 034 with the disputed step as a named `Prop`, and O-R1-8 for Hu-Liu.

**References.** BCHM10; Mor25; BDPP13; arXiv:0706.1792 and arXiv:0907.4170 (Birkar); arXiv:1609.00121 (Hashizume); Lazić-Tsakanikas, Publ. RIMS 58 (2022); arXiv:2603.03817 (Hu-Liu). Volume 9 proves BCHM, and Volume 10 treats minimal models and non-vanishing.

**Questions for a reader.**

- Does the case $n = 4$ of the minimal model conjecture follow from S21 and S26 for every lc pair, or only for $\mathbb{Q}$-factorial dlt pairs? The answer decides which record must change.
- Do the Lean form and the node form of non-vanishing agree for a boundary with real coefficients?
- Which steps of OpenAI 034 does the non-vanishing claim for 4-folds use, and does it use the contested step?
