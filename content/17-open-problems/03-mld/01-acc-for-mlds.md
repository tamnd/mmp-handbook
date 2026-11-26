---
title: The ACC for minimal log discrepancies
nodes: [MMWK2DDDPC, MMGSDKRGR6, MMFPRYMSNJ, MMAWP4SA44]
sources: [Sho04, Amb99, KM98, HL25, Rei83]
reads_with: []
requires: ["3", "4", "10"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The ACC for minimal log discrepancies

### Statement

**Conjecture 17.3.1 (ACC for minimal log discrepancies).** Fix $n$ and a set $I \subseteq [0, 1]$ that satisfies the DCC. The set of the numbers $\operatorname{mld}(x; X, \Delta)$, for lc pairs $(X, \Delta)$ of dimension $n$ with the coefficients of $\Delta$ in $I$ and closed points $x \in X$, satisfies the ACC.

Node: MMWK2DDDPC · Lean: `MinimalModel.ACCMld`

This is statement S49, due to Shokurov. It is open for $n \ge 3$.

**Theorem 17.3.2 (ACC for log canonical thresholds).** Fix $n$ and DCC sets $I \subseteq [0, 1]$ and $J \subseteq [0, \infty)$. The log canonical thresholds $\operatorname{lct}(X, \Delta; M)$ of lc pairs of dimension $n$ with coefficients in $I$, with respect to effective divisors $M$ with coefficients in $J$, satisfy the ACC.

Node: MMGSDKRGR6 · Lean: `MinimalModel.ACCLct`

This is statement S48, a theorem of Hacon, McKernan and Xu (Ann. of Math. 180 (2014), arXiv:1208.4150).

**Theorem 17.3.3 (Shokurov's reduction).** The ACC and the LSC for mlds in dimension $n$ give T(n).

Node: MMFPRYMSNJ · Lean: `MinimalModel.ShokurovReduction`

### Proof in words

What is known, by dimension, from the records:

- **Dimension 2.** The ACC holds for surfaces (Alexeev; spec 07, row T10-06, rated [U]).
- **Dimension 3.** The ACC is open. Kawakita proves it for smooth 3-folds and for any fixed 3-fold (arXiv:2312.13599, 2412.03006). Han, Liu and Luo (arXiv:2202.05287) and Liu and Luo (arXiv:2207.04610) prove it for 3-fold mlds near 1 and find the accumulation point $5/6$.
- **Each dimension.** The ACC holds for germs with local volume bounded below (Han-Liu-Qi, arXiv:2408.15090), for bounded generalized sub-pairs (Chen-Lin, arXiv:2609.20515), and for toric germs (Ambro; Borisov's toric ACC, rows T5-07 and T10-06 of spec 07). Han, Qi and Zhuang (arXiv:2506.20183) show that in a program of general type the mlds take finitely many values.

The ACC for log canonical thresholds is a theorem in all dimensions, but the ACC for mlds is open from dimension 3 on. The records do not say why the proof for thresholds does not extend. Spec 04.5 says only that the ACC for 3-fold mlds "is open after thirty years". Volume 1, Section 1.5, says that the ACC and the LSC are open in dimension 4 and higher. For the ACC this is weaker than the records: the ACC is open in dimension 3 too.

Spec 03.7 gives the idea of Shokurov's reduction: along a sequence of flips $X_i \dashrightarrow X_{i+1}$, the mlds of the flipping loci form a sequence in a set with the ACC, and the sequence cannot go on for ever. Volume 1 adds that the LSC lets the invariant be read off at the points of the flipping locus. Spec 03.11 rates the source [U]: the project has not checked a full written proof.

### Examples

The first test case of the ACC in the records is dimension 3 (target O-R4-3, difficulty 3). A smaller case is dimension 4 on a fixed variety, with a DCC boundary, after a check of what Chen-Lin cover (target O-R4-7, difficulty 2). Dimension 4 in general is target O-R4-4, difficulty 4.

Toric germs give exact data. For a $\mathbb{Q}$-Gorenstein cone $\sigma$ and $\Delta = \sum d_\rho D_\rho$, the log discrepancy of the divisor of a primitive vector $v$ in the interior of $\sigma$ is $\langle m_\sigma, v \rangle$, where $\langle m_\sigma, u_\rho \rangle = 1 - d_\rho$ (spec 03.13, item 7). So the mld at the fixed point is the minimum of a linear function on the lattice points of a cone: a finite computation.

The lab ran a first version of experiment E2 on 2026-11-26 (run `2026-11-26-e2-cyclic-quotient-mld-3-6d070b98`). It lists each isolated cyclic quotient 3-fold germ $\frac{1}{r}(a, b, c)$ with $2 \le r \le 40$. For such a germ the mld at the origin is the smallest age $\sum_i \{k a_i / r\}$ over $1 \le k < r$. The run found 1747 germs, of which 245 are terminal and 302 canonical. In each case the germ is terminal exactly when two weights add to 0 mod $r$ (the terminal lemma), and each terminal germ has mld $1 + \frac{1}{r}$. The run found 344 distinct mlds below 1. The record says that the run is a search, not a proof, and that only a certificate that Lean checks makes a theorem (spec 13.4).

### Lean

`MinimalModel.ACCMld n`, in `MinimalModel/Statements/Termination.lean`, says: for each $I \subseteq [0, 1]$ that is well-founded, there is no strictly increasing sequence of mlds at closed points of lc pairs of dimension $n$ with coefficients in $I$. The DCC of the node is the well-foundedness `I.IsWF` of the Lean statement. `MinimalModel.ACCLct` is in `MinimalModel/Statements/Boundedness.lean`. The library defines `MinimalModel.mld` and `MinimalModel.lct`. None of these statements has a proof.

Spec 04.5 names the obstruction for Lean: an mld needs all divisorial valuations, and Mathlib has `Valuation` but not the divisorial valuations of a variety. The project defines log discrepancies over divisorial valuations, and the test on one log resolution is a theorem only under the hypothesis `HasLogResolution` (spec 03.14).

### Notes and history

**Claims of 2025 and 2026.** The records hold no claim of the ACC for mlds in any open case. Landi's claim (C16) is on the LSC and the mld bound, and it is withdrawn (Section 3.2).

**Routes.** Route R4 (weight 0.10) has O-R4-1, the abstract Shokurov lemma: over an axiomatic sequence of flips with an invariant in an ACC set that is LSC and improves strictly, the sequence is finite (difficulty 1). Its first nodes are `shokurov-abstract`, `red-shokurov`, `red-han-liu`, `acc-mld-statement` and `lsc-mld-statement`. Spec 04.5 notes that O-R4-1 is cheap and that R1 (O-R1-5) and R3 reuse it. Route R3 has O-R3-2, the toric ACC and LSC in Lean. The lab has E2.

**References.** Sho04; Amb99; KM98; HL25; Rei83 for toric geometry; arXiv:1208.4150 (Hacon, McKernan and Xu); arXiv:2312.13599 and 2412.03006 (Kawakita); arXiv:2408.15090 (Han-Liu-Qi); arXiv:2609.20515 (Chen-Lin); arXiv:2202.05287 and 2207.04610; arXiv:2506.20183 (HQZ). Volume 4 treats mlds, and Volume 3 treats toric mlds.

**Questions for a reader.**

- Which bounded families do Chen-Lin cover, and does a fixed 4-fold with a DCC boundary fall in them?
- Is the set of 3-fold mlds with coefficients in a finite set known to have only finitely many accumulation points above $5/6$?
- The run of E2 found 344 values below 1 up to index 40. How does the count grow with the bound on $r$?
