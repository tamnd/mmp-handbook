---
title: Termination in dimension 4, proved and claimed
nodes: [MMTJ3YNHTG, MME79K17YJ, MM07D8FAVG, MMBTDMD2XP, MMY38TT73M, MM2NY6352R, MMFPRYMSNJ, MM0NXABJ9S, MMH0CM56AA]
sources: [KMM87, Fuj04, Mor25, BCHM10, AHK07, HLZ25, Sho04, HL25, Kaw92, OAI26, AxiomMMP]
reads_with: []
requires: ["3.5", "3.6", "10", "12"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Termination in dimension 4, proved and claimed

### Statement

**Conjecture 16.3.1 (termination of flips, $T(n)$).** For each projective lc pair $(X, \Delta)$ of dimension $n$ over an algebraically closed field of characteristic 0, each sequence of $(K_X + \Delta)$-flips is finite.

Node: MMTJ3YNHTG · Lean: `MinimalModel.Termination`

This is statement S20. It is a theorem for $n \le 3$ (Node MMH0CM56AA below; Kaw92 for log flips of 3-folds) and open for $n \ge 4$. The following results are refereed.

**Theorem 16.3.2 (terminal 4-folds, Kawamata, Matsuda and Matsuki).** Each sequence of flips of a $\mathbb{Q}$-factorial projective 4-fold with terminal singularities is finite.

Lean: not yet in Lean. The library states the termination of $\mathbb{Q}$-factorial terminal flips in dimension $d$ as `MinimalModel.QFactorialTerminalTermination d`, a `def` with no proof and no node, used as a hypothesis of S29 below.

**Theorem 16.3.3 (canonical 4-folds, Fujino).** Each sequence of flips of a $\mathbb{Q}$-factorial projective 4-fold with canonical singularities is finite.

Lean: not yet in Lean.

**Theorem 16.3.4 (pseudo-effective lc 4-folds, Moraga; Chen and Tsakanikas).** For each projective lc pair $(X, \Delta)$ of dimension 4 with $K_X + \Delta$ pseudo-effective, each sequence of $(K_X + \Delta)$-flips is finite.

Node: MME79K17YJ · Lean: `MinimalModel.TerminationPseffLc4`

**Theorem 16.3.5 (the program with scaling for a big boundary, BCHM).** Let $(X, \Delta)$ be a projective $\mathbb{Q}$-factorial klt pair with $\Delta$ big, and $C \ge 0$ a divisor with $(X, \Delta + C)$ klt and $K_X + \Delta + C$ nef. Then each $(K_X + \Delta)$-program with scaling of $C$ terminates.

Node: MM07D8FAVG · Lean: `MinimalModel.TerminationScalingBig`

This is BCHM10, Corollary 1.4.2, in every dimension. It is about programs with scaling only. Spec 01.2 also lists Birkar's termination for 4-folds with $\kappa \ge 2$, and the records have the paper of Alexeev, Hacon and Kawamata, "Termination of (many) 4-dimensional log flips" (AHK07). The records do not say which class of 4-fold log flips AHK07 covers: no statement of spec 06.2 has it as a source. This report does not fill the gap.

Two reductions are refereed and stated in the library.

**Theorem 16.3.6 (Shokurov's reduction).** The ACC and the lower semicontinuity of minimal log discrepancies in dimension $n$ imply $T(n)$.

Node: MMFPRYMSNJ · Lean: `MinimalModel.ShokurovReduction`

**Theorem 16.3.7 (the reduction of Han and Liu).** Let $d \ge 1$. Assume the ACC for the global minimal log discrepancies of enc pairs of dimension $d$ with coefficients in a finite set, and the termination of $\mathbb{Q}$-factorial terminal flips in dimension $d$. Then $T(m)$ holds for each $m \le d$.

Node: MM0NXABJ9S · Lean: `MinimalModel.HanLiuReduction`

For $d = 4$ the second hypothesis is the theorem of Kawamata, Matsuda and Matsuki. So $T(4)$ follows from the ACC for the global mlds of enc 4-fold pairs with coefficients in a finite set (HL25, Theorem 1.2). That ACC is open.

Three claims bear on dimension 4. Each is claimed, and none is a hypothesis of any argument of the handbook.

**Remark 16.3.8 (claim C1: lc 4-folds with rational boundary).** Let $(X, \Delta)$ be a projective lc pair of dimension 4 with $\Delta$ a $\mathbb{Q}$-divisor. Then each $(K_X + \Delta)$-program terminates.

Node: MMBTDMD2XP · Lean: `MinimalModel.TerminationLc4Rational`

**Remark 16.3.9 (big boundary in dimension at most 5, Han, Liu and Zhuang).** Let $(X, \Delta)$ be a projective klt pair of dimension at most 5 with $\Delta$ big or $K_X + \Delta$ big. Then each $(K_X + \Delta)$-program terminates.

Node: MMY38TT73M · Lean: `MinimalModel.TerminationBigLe5`

**Remark 16.3.10 (claim C2: big boundary in all dimensions, Hashizume).** The statement of the last remark holds in every dimension.

Node: MM2NY6352R · Lean: `MinimalModel.TerminationBig`

These are S22 (OAI26 and AxiomMMP), S24 (HLZ25, arXiv:2509.01501) and S25 (arXiv:2609.33679). The termination of 3-folds is this theorem.

Node: MMH0CM56AA · Lean: `MinimalModel.ThreefoldTermination`

### Proof in words

**Difficulty.** The proof for terminal 4-folds follows Shokurov's proof for 3-folds. A flip of a terminal variety keeps it terminal, and the discrepancies of divisors over $X$ do not go down; those over the flipping locus go up (KM98, Lemma 3.38). The *difficulty*, the number of exceptional divisors with discrepancy less than a fixed bound, is finite for a terminal variety and does not go up. The work is to find a bound for which it goes down strictly, and in dimension 4 this needs a study of the possible flipping loci, which are curves or surfaces. The records do not describe the proof of KMM87 further. Fujino's proof for canonical 4-folds refines the count. Section 16.3.2 carries out a toric form of the count on an example.

**Pseudo-effective lc 4-folds.** In outline, a pseudo-effective program from an lc 4-fold can be compared with programs on dlt models, and special termination reduces the question near the boundary to $T(3)$. The records give the theorem through its paper record Mor25 (accepted, Math. Z. 310, 2025) and do not describe the proof further.

**The claims.** The claim C1 is a Lean proof (AxiomMath/MMP, commit `1f9ade3670`) of an AI-written manuscript (OpenAI family 056). The Lean kernel checked the inferences; whether the definitions mean the textbook notions is the subject of the audit of Section 16.4.2. The claims S24 and S25 rest on the uniform index bound of Han, Qi and Zhuang (arXiv:2506.20183); target O-R1-5 isolates the combinatorial core of S25, the finiteness of the set of models that a program meets.

### Examples

**Example 16.3.11 (a flip that the count does not see).** In $N = \mathbb{Z}^4$ take the circuit $v_1 + v_2 = v_3 + v_4 + v_5$ with $v_1, \dots, v_4$ a basis. Its toric flip (Theorem 3.5.20) replaces a plane $V(\operatorname{Cone}(v_1, v_2)) \cong \mathbb{P}^2$ with normal bundle $\mathcal{O}(-1)^2$ by a line $V(\operatorname{Cone}(v_3, v_4, v_5)) \cong \mathbb{P}^1$ with normal bundle $\mathcal{O}(-1)^3$. The line $\ell$ has $D_{v_i} \cdot \ell$ proportional to $(1, 1, -1, -1, -1)$, so $-K \cdot \ell$ is proportional to $1 + 1 - 3 = -1$: the line is $K$-positive, and the plane is the $K$-negative side. Both sides are smooth, so no toric valuation has log discrepancy less than 2 on either side, and the count of Section 16.3.2 is 0 before and after. A count that is to prove termination must drop at every flip, so this count alone does not. For toric varieties termination comes instead from Theorem 3.6.3: a flip raises the support function strictly, and there are finitely many simplicial fans on a fixed set of rays.

**Example 16.3.12 (why "each program").** The statements S22, S24 and S25 say that each program terminates, not only that one program does. In Section 16.3.2 the 4-fold $X_0$ has two $K$-negative rays: one is a Mori fibre space, and the program that chooses it stops at once. The other starts a sequence of two flips. A statement of the form "some program terminates" holds for $X_0$ by the first choice alone and says nothing about the flips.

### Lean

On 2026-11-28 the library mmp-lean (commit `8028303`) states S20, S21, S22, S23, S24, S25, S28 and S29 in `MinimalModel/Statements/Termination.lean` and S16 in `LowDim.lean`, each as a `def` of type `Prop`. None of them has a proof. S22, S24 and S25 conclude `¬ HasInfiniteProgram A`, a statement about each sequence of steps; S20 and S21 conclude `¬ HasInfiniteFlips A`. Each docstring of a claimed statement says that it is never a hypothesis of another proof (spec 06.6). In `records/fidelity.json`, `MinimalModel.TerminationLc4Rational` has F1 and F3 and `MinimalModel.Termination` has F1, F2 and F3; neither passes, since F4 to F7 are not done.

### Notes and history

The terminal case is KMM87, the canonical case Fuj04, the pseudo-effective case Mor25 with Chen-Tsakanikas (arXiv:2011.02236) for NQC generalized pairs. The reductions are Sho04 and HL25. The claims are recorded in `claims/AxiomMath-MMP.yaml` (C1), `claims/arXiv-2609-33679.yaml` (C2) and the paper record HLZ25 (no claim record), all fresh and unread.

**Questions for a reader.**

- What is the class of 4-fold log flips that AHK07 covers, and is it contained in the pseudo-effective case of Mor25?
- The reduction of Han and Liu turns $T(4)$ into an ACC for enc 4-fold pairs. Does the claim C1 prove that ACC on the way, or does it avoid it?
