---
title: Abundance
nodes: [MMPTP8SV13, MM5ECX1RGZ, MMRKRVGY9M, MM5QPM66FR, MMM6KF309B, MMZ5XGBW5M]
sources: [KM98, Kol92, BCHM10]
reads_with: []
requires: ["10"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Abundance

### Statement

**Conjecture 17.2.4 (Abundance).** Let $(X, \Delta)$ be a projective lc pair of dimension $n$ with $K_X + \Delta$ nef. Then $K_X + \Delta$ is semiample.

Node: MMPTP8SV13 · Lean: `MinimalModel.Abundance`

This is statement S40. It is open for $n \ge 4$. Four cases are theorems.

**Theorem 17.2.5 (Abundance for 3-folds).** Let $(X, \Delta)$ be a projective lc pair of dimension 3 with $K_X + \Delta$ nef. Then $K_X + \Delta$ is semiample.

Node: MM5ECX1RGZ · Lean: `MinimalModel.ThreefoldAbundance`

**Theorem 17.2.6 (Abundance in the big case).** Let $(X, \Delta)$ be a projective klt pair with $K_X + \Delta$ nef and big. Then $K_X + \Delta$ is semiample.

Node: MMRKRVGY9M · Lean: `MinimalModel.AbundanceBig`

**Theorem 17.2.7 (Abundance for numerical dimension 0).** Let $(X, \Delta)$ be a projective lc pair with $K_X + \Delta$ nef and $\nu(K_X + \Delta) = 0$. Then $K_X + \Delta$ is semiample.

Node: MM5QPM66FR · Lean: `MinimalModel.AbundanceNuZero`

**Theorem 17.2.8 (The Liu-Xu reduction).** Fix $d$. Assume non-vanishing in dimension $d$. Then abundance holds for the projective lc pairs of dimension $d$ with $\nu(K_X + \Delta) \le 1$.

Node: MMM6KF309B · Lean: `MinimalModel.LiuXuReduction`

### Proof in words

What is known, by dimension:

- **Dimension at most 3.** Abundance is a theorem (Miyaoka; Kawamata; Keel, Matsuki and McKernan; Kol92).
- **Dimension 4.** Abundance is known for $\kappa > 0$ (Kawamata; Fukuda) [S]. It is open for $\kappa = 0$ and for $\kappa = -\infty$. For $\kappa = -\infty$, a nef $K + \Delta$ is a counterexample to non-vanishing, so this case is the non-vanishing problem of Section 2.1.
- **Dimension at most 5, smooth.** Liu and Xu (arXiv:2505.05250) prove abundance for smooth varieties of dimension at most 5 with $\kappa \ge 0$ and $\nu \le 1$.
- **Each dimension.** Abundance holds in the big case, by the base point free theorem (KM98, Theorem 3.3, with BCHM10 for a boundary with real coefficients), and for $\nu = 0$ (Nakayama; Gongyo for lc pairs, arXiv:1005.2796).

The tool of the big case is the base point free theorem: if $K + \Delta$ is nef and $a(K + \Delta) - (K + \Delta)$ is nef and big for some $a > 1$, then $K + \Delta$ is semiample. A nef and big $K + \Delta$ meets this test. When $K + \Delta$ is not big, the test fails, and a proof needs a second input. The records name the inputs.

- Non-vanishing and dlt extension give abundance (Demailly, Hacon and Păun, Acta Math. 210 (2013), as spec 07 gives it, rated [S]).
- Non-vanishing in dimension $d$ gives abundance for $\nu \le 1$ in dimension $d$ (Liu-Xu, statement S44).
- If $\kappa(K + \Delta) = \nu(K + \Delta)$, then $K + \Delta$ is semiample (Kawamata, as the records give it).

So every conditional result in the records goes through non-vanishing (spec 03.11). This is why the records call non-vanishing the main entrance to abundance.

### Examples

The first test case of abundance is a 4-fold with $\kappa = 0$ (target O-R5-2, difficulty 4). Abundance for $\kappa > 0$ in dimension 4 is known, and the case $\kappa = -\infty$ is non-vanishing. So $\kappa = 0$ is the smallest case of abundance that does not reduce to non-vanishing in the records.

A second test case is the relative form of Liu-Xu: their results for $\nu \le 1$ in the relative lc case (target O-R5-8, difficulty 1).

A known instance is the case $\nu = 0$. If $K + \Delta$ is nef with $\nu = 0$, then $K + \Delta$ is numerically trivial, and the theorem says that some multiple is linearly trivial. The positive instances of the fidelity checks can come from this case and from the big case.

### Lean

The library states S40 as `MinimalModel.Abundance n`: for each projective lc pair of dimension `n` with `K + Δ` nef, `K + Δ` is semiample. It states S42 as `MinimalModel.AbundanceBig` and S44 as `MinimalModel.LiuXuReduction d`. The docstring of S44 says that the numerical dimension is Nakayama's $\kappa_\sigma$ (spec 06.5, risk 4), and that for a nef divisor it agrees with the usual numerical dimension. `MinimalModel.ThreefoldAbundance` (S17) and `MinimalModel.AbundanceNuZero` (S43) are not in `records/lean.json` on 2026-11-26. None of these statements has a proof in the library.

### Notes and history

**Claims of 2025 and 2026.**

| Claim | What it claims | Record | Status |
|---|---|---|---|
| C3, OpenAI 034 | log abundance in characteristic 0 for a rational boundary, in all dimensions; canonical non-vanishing; 4-fold non-vanishing; the effective Iitaka fibration; the index conjecture for slc log CY pairs | `claims/openai-math.yaml` | fresh; "Contested" on one tracker (log Iitaka subadditivity) [S]; no Lean |
| C4, J. Liu | non-vanishing for smooth varieties in dimension $d$ implies abundance for lc pairs in dimension at most $d$ | `claims/arXiv-2610-35913.yaml`, posted 2026-10-07 | fresh; no node yet |

OpenAI released 722 manuscripts in 372 families on 2026-10-06. On 2026-10-07, 3 papers were retracted and 14 revised; six of the revised papers are on Kähler programs and abundance. The README of the release says that some of the results with no Lean proof could have issues. None of the MMP families of the release has a Lean proof.

If C4 holds, the whole abundance conjecture in dimension $d$ reduces to non-vanishing for smooth varieties of dimension $d$. With the reductions of Section 2.1, the core case of dimension 4 is then the smooth, non-uniruled 4-fold.

**Routes.** Route R5 (weight 0.10) has O-R5-2 (4-folds with $\kappa = 0$), O-R5-3 (log abundance in all dimensions, difficulty 5, claimed by OpenAI 034) and O-R5-8 (Liu-Xu in the relative lc case). Its first nodes are `abundance-statement` and `red-liu-xu`. Route R1 has O-R1-4: the J. Liu reduction as an implication between named `Prop`s, with each cited input a hypothesis, then the steps that use only the program with scaling. Its first node is `red-jliu`. Route R1 also has O-R1-6 for the dependency map of OpenAI 034.

**References.** KM98 and Kol92 for the base point free theorem and dimension 3; BCHM10; arXiv:2505.05250 (Liu-Xu); arXiv:1005.2796 (Gongyo); arXiv:2610.35913 (J. Liu); Demailly, Hacon and Păun, Acta Math. 210 (2013). Volume 10 treats abundance.

**Questions for a reader.**

- Which statement of the literature gives abundance for 4-folds with $\kappa > 0$, and for which class of pairs? The records cite Kawamata and Fukuda with the tag [S] and give no paper record.
- Which steps of C4 use the program with scaling only, and which use a cited input that is itself a claim?
- Is the contested step of OpenAI 034, log Iitaka subadditivity, also used by C4?
