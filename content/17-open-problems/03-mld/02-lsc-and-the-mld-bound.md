---
title: The LSC for minimal log discrepancies and the mld bound
nodes: [MMFKZ7VB29, MM0FZHT2BB, MMFPRYMSNJ]
sources: [Amb99, Sho04, KM98]
reads_with: []
requires: ["4", "10"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The LSC for minimal log discrepancies and the mld bound

### Statement

**Conjecture 17.3.4 (LSC for minimal log discrepancies).** Let $(X, \Delta)$ be an lc pair of dimension $n$. Then the function $x \mapsto \operatorname{mld}(x; X, \Delta)$ is lower semicontinuous on the scheme points of $X$.

Node: MMFKZ7VB29 · Lean: `MinimalModel.LSCMld`

This is statement S50, due to Ambro. It is open.

**Conjecture 17.3.5 (The mld bound).** Let $(X, \Delta)$ be a pair and $x \in X$ a closed point. Then $\operatorname{mld}(x; X, \Delta) \le \dim X$. Equality holds only if $X$ is smooth at $x$ and $\Delta = 0$ near $x$.

Node: MM0FZHT2BB · Lean: `MinimalModel.MldBound`

This is statement S51, due to Shokurov. It is open in general.

### Proof in words

**The LSC, by dimension.** The records do not agree on the low dimensions.

- Spec 03, Conjecture 3.17, says that the LSC is open in dimension at least 4 in general. Volume 1, Section 1.5, says that the LSC is known in dimension at most 3 (Ambro).
- The table of spec 01.1 lists "ACC and LSC for 3-folds" in its column of open problems.

So the records do not settle whether the LSC holds for all lc 3-folds. This report takes the safe reading: the LSC is open in dimension 3 and higher, and the case of dimension 2 is not stated in the records.

The known cases in the records hold in every dimension, for special classes:

- **Toric varieties.** Ambro (1999; spec 07, row T5-08, rated [U]).
- **Smooth and lci varieties.** Ein, Mustaţă and Yasuda prove the LSC and inversion of adjunction with jet schemes (Invent. Math. 153 (2003), math/0209392; row T4-08).
- **Hyperquotients.** Nakamura and Shibata prove the LSC for hyperquotient singularities (spec 01.1).

The records also hold two negative results of Nakamura and Shibata (Duke 175 (2026), arXiv:2404.06164, and arXiv:2608.28038; row T4-11). The PIA conjecture is false, and the LSC fails in families. The index conjecture fails outside the klt case. So a proof of the LSC cannot pass through a statement for families.

**The mld bound.** The records give no dimension in which the mld bound is open or known beyond the statement. They say that it is open in general (target O-R4-6, difficulty 4). At a smooth point with $\Delta = 0$ near $x$, the mld is $n$: the blow-up of the point has discrepancy $n - 1$, so log discrepancy $n$. The conjecture says that a singular point, or a point of the boundary, has a smaller mld.

**How the LSC enters termination.** By Volume 1, Shokurov's reduction (S28, Section 3.1) uses the LSC to read the invariant off at the points of the flipping locus. The records do not say how the mld bound enters the argument, and they do not give the details; spec 03.11 rates the source [U].

### Examples

The first test case of the LSC in the records is dimension 4 (target O-R4-5, difficulty 4). A smaller case is the LSC for hyperquotients in characteristic $p$ (target O-R7-5, difficulty 2). The toric case is known, and route R3 proves it in Lean (O-R3-2, step 8 of R3).

The toric formula of Section 3.1 gives an instance of the mld bound. For the cyclic quotient germ $\frac{1}{r}(a, b, c)$, the mld at the origin is the smallest age $\sum_i \{k a_i / r\}$, and each age is less than 3. The smooth point $\mathbb{A}^3$ has mld 3. In the run of E2, each terminal germ has mld $1 + \frac{1}{r}$, and each germ that is not terminal has mld at most 1. So each of the 1747 germs up to index 40 has mld at most $\frac{3}{2}$, far below the bound 3, and the bound holds for them with strict inequality.

### Lean

On 2026-11-26 the library states S50 as `MinimalModel.LSCMld n` in `MinimalModel/Statements/Termination.lean`: for each lc pair of dimension `n` and each real `t`, there is an open set $U$ such that a closed point $x$ is in $U$ exactly when $t < \operatorname{mld}(x)$. The Lean form uses closed points, while the node text and spec 03 use all scheme points. The two forms can differ, and the fidelity check of the statement must compare them.

The library states S51 as `MinimalModel.MldBound` in `MinimalModel/Statements/Boundedness.lean`. It asks for no lc hypothesis, as the node does; the mld is a value in `WithBot ℝ`, so it is $-\infty$ when the pair is not lc at $x$. Neither statement has a proof.

### Notes and history

**Claims of 2025 and 2026.** Landi (arXiv:2611.30971, claim C16, `claims/arXiv-2611-30971.yaml`) claimed the full LSC for mlds and the mld bound. The record has the status withdrawn. The authors withdrew the preprint on 2026-11-24, with the reason that Lemma 3.2 is false. Spec 07 gives the date of the claim as 2026-11-23 and says that version 2 of the preprint says "Lemma 3.2 is false". The record says: "Nobody has read the claim for the project yet." S50 and S51 stay open.

Spec 01.13 lists the withdrawal as one of three claims of the autumn of 2026 that have already failed or changed, with the gap in Chan's proof of Fujita freeness and the OpenAI retractions of 2026-10-07.

**Routes.** Route R4 has O-R4-5 and O-R4-6. Route R1 has O-R1-12: the false Lemma 3.2 as a Lean refutation, if the counterexample is finite (difficulty 1, formal check 2). Route R7 has O-R7-5. Route R3 has O-R3-2. The lab experiment E2 tests Ambro's LSC on toric families (spec 13.4).

**References.** Amb99; Sho04; KM98; Ein, Mustaţă and Yasuda, Invent. Math. 153 (2003), math/0209392; Nakamura and Shibata, Duke 175 (2026), arXiv:2404.06164, and arXiv:2608.28038; arXiv:2611.30971 (Landi, withdrawn). Volume 4 treats mlds.

**Questions for a reader.**

- Is the LSC known for all lc 3-folds? Spec 03 and Volume 1 say yes, and the table of spec 01.1 says no. One record must change.
- Do the closed point form and the scheme point form of the LSC agree for an lc pair?
- Is the counterexample to Lemma 3.2 of Landi finite, so that O-R1-12 can check it in Lean?
