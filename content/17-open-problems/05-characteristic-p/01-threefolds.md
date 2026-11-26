---
title: Three-folds in positive characteristic
nodes: [MMD90YG1TD, MM5ECX1RGZ]
sources: [KM98, Kol92]
reads_with: []
requires: ["5", "8", "11"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Three-folds in positive characteristic

### Statement

**Theorem 17.5.1 (The lc 3-fold program in characteristic $p \ge 5$).** Let $k$ be a perfect field of characteristic $p \ge 5$. The minimal model program holds for projective lc 3-fold pairs over $k$.

Node: MMD90YG1TD · Lean: `MinimalModel.CharP3foldLcMMP`

This is statement S58.

**Conjecture 17.5.2 (The 3-fold program in characteristic 2 and 3).** The minimal model program holds for projective 3-folds over a perfect field of characteristic 2 or 3.

The map has no node for this problem. The records list it as open (target O-R7-2, difficulty 4). They do not fix the class of pairs.

**Remark 17.5.3 (Claim C9: abundance for lc 3-folds in characteristic $p$).** Abundance holds for lc 3-folds in characteristic $p > 42$, and for 3-folds with $\nu = 1$ in characteristic $p > 3$.

The first part is claimed by Bernasconi, Witaszek and Xu (BWX, arXiv:2610.10439; spec 07.13 gives the names), and the authors call it "very preliminary". The second part is claimed by OpenAI family 035. The map has no node for either part. In characteristic 0, abundance for 3-folds is a theorem (S17, Section 2.2).

### Proof in words

**The program, by characteristic.**

- **$p > 5$.** The lc 3-fold program is complete over perfect fields: Hacon-Xu, Cascini-Tanaka-Xu, Birkar, Birkar-Waldron and Hashizume-Nakamura-Tanaka [P].
- **$p = 5$.** Hacon and Witaszek (arXiv:1911.12895) [P].
- **$p = 2, 3$.** Only the relative dlt program over $\mathbb{Q}$-factorial 3-folds is known (Hacon and Witaszek, arXiv:1909.12872). Version 2 of that preprint removed its Theorem 1.6 [P]. Totaro (arXiv:2407.02608) gives terminal 3-folds that are not Cohen-Macaulay [P]. In characteristic 0, klt singularities are rational, so Cohen-Macaulay (KM98, Theorem 5.22). Spec 01.4 lists the example of Totaro with the small primes.

The records do not give the years or the arXiv numbers of the papers for $p > 5$. Spec 07 does not have them as paper records yet.

**Abundance, by characteristic and numerical dimension.**

- **$p > 3$, $\nu \ne 1$.** Zheng Xu (arXiv:2307.03938, to appear in Compositio) [P].
- **$p > 3$, $\nu = 1$.** Claimed by OpenAI family 035 (claim C9).
- **$p > 42$, lc.** Claimed by BWX (claim C9). Spec 01.4 writes that BWX "prove" lc abundance for $p > 42$ [P], while the claim record and spec 01.3 keep the result as a claim that the authors call very preliminary. This report follows the claim record.
- **$5 \le p \le 42$, $\nu = 1$.** Only the AI manuscript of OpenAI 035 covers this case (spec 01.3).
- **$p = 2, 3$.** The records do not say.

So the gap between the theorems and the claims is the case $\nu = 1$. If the claim of BWX holds, abundance for lc 3-folds holds for $p > 42$. For $5 \le p \le 42$ the case $\nu = 1$ then rests on the AI manuscript alone.

### Examples

The first test cases in the records:

- Abundance with $\nu = 1$ for $5 \le p \le 42$: a human audit of OpenAI 035 against Zheng Xu (arXiv:2307.03938). This is O-R7-1, the same target as O-R1-9 (difficulty 1 to 2; no formal check in year 1).
- The 3-fold program in characteristic 2 and 3: O-R7-2 (difficulty 4).
- The LSC of mlds for hyperquotients in characteristic $p$: O-R7-5 (difficulty 2; Section 3.2).

Lab experiment E7 computes the $F$-purity of hypersurface germs by Fedder's criterion, the $F$-purity of the quotient germs $\frac{1}{n}(1, q)$ for small $p$, the LSC of mlds for hyperquotients in families, and the discrepancies of wild $\mathbb{Z}/p$ quotients by the $v$-function of Yasuda [U]. On 2026-11-26 the lab has no run of E7.

A known instance of the failure of the tools is in Volume 11 (spec 11): a quasi-elliptic surface in characteristic 2 or 3, and the counterexample of Raynaud to Kodaira vanishing, in outline.

### Lean

On 2026-11-26, `MinimalModel.CharP3foldLcMMP` (S58) is not in `records/lean.json`. The node plans it in `MinimalModel/Statements/OtherSettings.lean` for milestone S4. Spec 06.2.3 fixes the field of S58 as `CharP k p` and `PerfectField k`, where the other families use `IsAlgClosed k` and `CharZero k`. The vocabulary is partial: it lacks Frobenius singularities. Spec 04.8 says that Frobenius singularities and Witt vectors are partial in Mathlib.

### Notes and history

**Claims of 2025 and 2026.**

| Claim | What it claims | Record | Status |
|---|---|---|---|
| C9, BWX | abundance for lc 3-folds, $p > 42$ | `claims/arXiv-2610-10439.yaml` | fresh; "very preliminary" by the authors |
| C9, OpenAI 035 | 3-fold abundance with $\nu = 1$, $p > 3$ | `claims/openai-math.yaml` | fresh; no Lean |

Each record says: "Nobody has read the claim for the project yet."

**Routes.** Route R7 (weight 0.05) has O-R7-1, O-R7-2 and O-R7-5, with the first node `charp-3fold-mmp-statement`. Route R1 has O-R1-9. The lab has E7.

**References.** KM98 and Kol92 for the program of characteristic 0; arXiv:1911.12895 and 1909.12872 (Hacon and Witaszek); arXiv:2407.02608 (Totaro); arXiv:2307.03938 (Zheng Xu); arXiv:2610.10439 (BWX). Volume 11 treats the program in characteristic $p$.

**Questions for a reader.**

- What did Theorem 1.6 of arXiv:1909.12872 state before version 2 removed it?
- Is the bound $p > 42$ of BWX a limit of the method, or of one estimate?
- Is abundance for 3-folds known in characteristic 2 or 3 in any case?
