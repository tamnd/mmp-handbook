---
title: Termination by dimension
nodes: [MMTJ3YNHTG, MMH0CM56AA, MME79K17YJ, MM07D8FAVG, MMFCAWE0XH, MMFPRYMSNJ, MM0NXABJ9S]
sources: [KM98, KMM87, Kaw92, Fuj04, Mor25, AHK07, BCHM10, Sho04, HL25]
reads_with: []
requires: ["10", "16"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Termination by dimension

### Statement

**Conjecture 17.1.1 (Termination of flips, T(n)).** Let $(X, \Delta)$ be a projective lc pair of dimension $n$ over an algebraically closed field of characteristic 0. Then there is no infinite sequence of $(K_X + \Delta)$-flips that starts at $(X, \Delta)$.

Node: MMTJ3YNHTG · Lean: `MinimalModel.Termination`

This is statement S20 of spec 06.2. On 2026-11-26 the conjecture is open for each $n \ge 4$ in refereed work. It is a theorem for $n \le 3$.

**Theorem 17.1.2 (Termination in dimension 3).** Each sequence of flips of a projective lc pair of dimension 3 is finite.

Node: MMH0CM56AA · Lean: `MinimalModel.ThreefoldTermination`

**Theorem 17.1.3 (Termination for pseudo-effective lc 4-folds).** Let $(X, \Delta)$ be a projective lc pair of dimension 4 with $K_X + \Delta$ pseudo-effective. Then each sequence of $(K_X + \Delta)$-flips is finite.

Node: MME79K17YJ · Lean: `MinimalModel.TerminationPseffLc4`

**Theorem 17.1.4 (Termination with scaling for a big boundary).** Let $(X, \Delta)$ be a $\mathbb{Q}$-factorial klt pair, projective over $U$, with $\Delta$ big over $U$. Then the $(K_X + \Delta)$-program with scaling of an ample divisor is finite (BCHM10, Corollary 1.4.2).

Node: MM07D8FAVG · Lean: `MinimalModel.TerminationScalingBig`

**Theorem 17.1.5 (Special termination).** Assume T(m) for each $m < n$. Let $(X, \Delta)$ be a projective $\mathbb{Q}$-factorial dlt pair of dimension $n$. Then each program for $(X, \Delta)$ is an isomorphism near $\lfloor \Delta \rfloor$ after finitely many steps.

Node: MMFCAWE0XH · Lean: `MinimalModel.SpecialTermination`

**Theorem 17.1.6 (Shokurov's reduction).** If the ACC for minimal log discrepancies (S49) and the lower semicontinuity of minimal log discrepancies (S50) hold in dimension $n$, then T(n) holds.

Node: MMFPRYMSNJ · Lean: `MinimalModel.ShokurovReduction`

**Theorem 17.1.7 (The Han-Liu reduction).** Fix $n$. Assume the ACC for the minimal log discrepancies of enc germs of dimension $n$ and the termination of terminal flips in dimension $n$. Then T(n) holds.

Node: MM0NXABJ9S · Lean: `MinimalModel.HanLiuReduction`

### Proof in words

What is known depends on the dimension. The list gives the state in refereed work. Section 1.2 gives the claims.

- **Dimension 1 and 2.** A curve has no contractions of the needed kind, and a contraction of a surface is never small, because a curve on a surface is a divisor. So no flip exists, and a program stops after at most $\rho(X) - 1$ steps.
- **Dimension 3.** T(3) is a theorem for lc pairs. Shokurov proved termination for terminal 3-folds with the difficulty, a count of the exceptional divisors of small discrepancy (KMM87). Kawamata extended it to klt 3-fold pairs (Kaw92). Han and Liu give a proof with no difficulty function, through the ACC for the minimal log discrepancies of enc 3-folds (HL25, Geom. Topol. 29 (2025)).
- **Dimension 4.** Termination is a theorem for terminal 4-folds (KMM87), for canonical 4-folds (Fuj04), for 4-folds with $\kappa \ge 2$ (Birkar), and for lc 4-folds with $K + \Delta$ pseudo-effective (Moraga, Mor25, Math. Z. 310 (2025)). Chen and Tsakanikas (arXiv:2011.02236) give the pseudo-effective case for NQC generalized pairs. Alexeev, Hacon and Kawamata prove termination for many 4-dimensional log flips (AHK07). The general lc case is open in refereed work. The case of a rational boundary is claimed (Section 1.2).
- **Each dimension.** BCHM prove that a program with scaling of an ample divisor is finite for a klt pair with a big boundary (BCHM10, Corollary 1.4.2). This is enough for most uses, but it is a statement about one program, not about every sequence of flips. Special termination holds in dimension $n$ if T(m) holds for each $m < n$ (Fujino, as spec 03.11 gives it).

The proofs in dimension 3 and in the terminal and canonical cases of dimension 4 count divisors. A flip does not lower any discrepancy, by the negativity lemma, and it raises the discrepancy of each divisor with centre in the flipping locus. When the set of divisors of small discrepancy is finite, each flip removes one of them, and the sequence stops. In dimension 4 and higher the set is no longer finite in a usable way. The discrepancies can climb towards a limit without reaching it.

The two reductions replace the count. Shokurov's reduction (Sho04) uses an invariant built from minimal log discrepancies. The ACC stops an infinite increasing sequence of values of the invariant, and the lower semicontinuity lets the invariant be read at the points of the flipping locus. Spec 03.11 rates the source of this arrow [U]: the records mark the reduction as one that the project has not yet checked against a full written proof. The Han-Liu reduction (HL25) is sharper. It needs the ACC only for enc germs (exceptionally non-canonical germs) and the termination of terminal flips, which is a theorem in dimension 4. So the Han-Liu Conjecture 1.9(2') in dimension 4 gives T(4) for lc flips (spec 03.11). Its toric case is Target T of the project (Section 3.3).

A third reduction is Birkar's: the ACC for log canonical thresholds and T(n-1) give T(n) for pairs with $\kappa(K + \Delta) \ge 0$. Spec 03.11 gives the source as Birkar 2007, rated [S]. The ACC for log canonical thresholds is a theorem in all dimensions (Hacon, McKernan and Xu), so the reduction turns T(4) into termination for effective lc 5-folds, if its hypotheses fit. The exact hypothesis is a recheck item of the records (spec 01.16, item 5). Section 1.3 says more.

### Examples

The first test case of T(4) is the lc 4-fold with $K + \Delta$ not pseudo-effective and a boundary with irrational coefficients. Every case with $K + \Delta$ pseudo-effective is a theorem (Mor25), and the claim of Section 1.2 covers a rational boundary. So a pair with $\kappa(K + \Delta) = -\infty$ and a real boundary is the smallest case that no refereed result and no claim covers. Route R2 asks the same question as target O-R2-4: does the Lean proof for a rational boundary extend to real coefficients? Spec 04.3 rates its difficulty 2 to 3 [U].

A test case that the project can compute is the toric one. Each sequence of toric flips of a simplicial fan terminates (spec 03.13, item 6). The records mark the exact scope of this argument as a recheck item (Q-12). The toric MMP is statement S39 (`MinimalModel.ToricMMP`), and route R3 builds it in Lean on Mathlib alone. It gives positive instances for the statement S20, but it does not touch the open cases, because a toric flip is a finite operation on cones.

A sequence that is infinite and is not a counterexample is the sequence of Atiyah flops $X \dashrightarrow X^+ \dashrightarrow X \dashrightarrow \cdots$ (Volume 1, Section 1.4). Its steps are not $(K + \Delta)$-negative, so the conjecture does not apply.

### Lean

The statement S20 is `MinimalModel.Termination n`, in the file `MinimalModel/Statements/Termination.lean` of mmp-lean at commit 6e779d01. For each pair `A : PairModel k` of dimension `n` that is lc, it says `¬ HasInfiniteFlips A`. The field carries `[IsAlgClosed k] [CharZero k]`. The library also has `HasInfiniteProgram`, a sequence of steps of any kind, and the claimed statements of Section 1.2 use it.

`MinimalModel.ShokurovReduction n` says that `ACCMld n` and `LSCMld n` give `Termination n`. Its docstring says that the reader role must still check the class of pairs of the source. `MinimalModel.SpecialTermination n` takes T(m) for each $m < n$ as a hypothesis and is about $\mathbb{Q}$-factorial dlt pairs. `MinimalModel.TerminationScalingBig` is about programs with scaling only. `MinimalModel.HanLiuReduction` has no Lean statement yet.

None of these statements has a proof in the library. On 2026-11-26 none of them has an entry in `records/fidelity.json`, so none has passed the fidelity checks of spec 06.3.

### Notes and history

**Claims of 2025 and 2026.** The claims on termination are in Section 1.2: OpenAI 056 with AxiomMath/MMP (C1), Han-Liu-Zhuang (S24), Hashizume (C2) and Hu-Liu (C5). Each claim record has the status `fresh` on 2026-11-26.

**Routes.** Route R4 (weight 0.10) attacks T(n) through the ACC and the lower semicontinuity. Its first targets are O-R4-1, the abstract Shokurov lemma in Lean, and O-R4-2, the Han-Liu reduction in Lean, both over named hypotheses. Route R2 (weight 0.15) attacks T(4) for a rational boundary through the audit of AxiomMath/MMP (O-R2-1). Route R1 (weight 0.20) checks parts of the claims for a big boundary (O-R1-5, O-R1-10). Route R3 (weight 0.15) builds the toric MMP and Target T.

**References.** KMM87 and Kaw92 for dimension 3; Fuj04 and Mor25 for dimension 4; AHK07 for many 4-fold log flips; BCHM10 for termination with scaling; Sho04 for the reduction; HL25 for the Han-Liu reduction. Volume 10 treats termination in full, and Volume 16 reports the state of dimension 4.

**Questions for a reader.**

- Which class of pairs does the Shokurov reduction of Sho04 need: lc pairs, or $\mathbb{Q}$-factorial dlt pairs? The Lean docstring leaves the question to the reader role.
- Does the proof of Mor25 use the pseudo-effectivity of $K + \Delta$ only through the existence of a minimal model, or in a second place?
- Spec 03.11 credits special termination to Fujino and rates part of the source [U]. Which written proof covers the dlt case in each dimension?
