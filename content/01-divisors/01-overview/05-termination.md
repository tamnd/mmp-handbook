---
title: Termination of flips
nodes: [MMTJ3YNHTG, MMH0CM56AA, MMWK2DDDPC, MMFKZ7VB29, MMFPRYMSNJ, MMBTDMD2XP]
sources: [KM98, KMM87, Kol92, Fuj04, Mor25, Sho04, BCHM10, OAI26, AxiomMMP]
reads_with: [KM98:ch3]
requires: [P8]
level: background
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Termination of flips

### Statement

Each divisorial contraction lowers the Picard number by one, so a program has at most $\rho(X) - 1$ divisorial contractions. A flip keeps the Picard number. So the program stops if and only if every sequence of flips is finite.

**Definition 1.1.17.** A *sequence of flips* of a pair $(X, \Delta) = (X_0, \Delta_0)$ is a sequence $X_0 \dashrightarrow X_1 \dashrightarrow X_2 \dashrightarrow \cdots$ in which each $X_i \dashrightarrow X_{i+1}$ is the flip of a $(K_{X_i} + \Delta_i)$-negative flipping contraction, and $\Delta_{i+1}$ is the strict transform of $\Delta_i$.

Lean: `MinimalModel.HasInfiniteFlips` (an infinite sequence of flips) and `MinimalModel.HasInfiniteProgram` (an infinite sequence of steps), in the project library.

**Conjecture 1.1.18 (Termination of flips).** Let $(X, \Delta)$ be a projective lc pair of dimension $n$. Then every sequence of $(K_X + \Delta)$-flips that starts at $(X, \Delta)$ is finite.

Node: MMTJ3YNHTG · Lean: `MinimalModel.Termination`

The conjecture is a theorem for $n \le 3$ and open for every $n \ge 4$. It is the main open problem of the program.

**Theorem 1.1.19 (Termination in dimension 3).** Every sequence of flips of a projective lc pair of dimension 3 is finite.

Node: MMH0CM56AA

**Definition 1.1.20.** Let $(X, \Delta)$ be a pair and $x \in X$ a closed point. The *minimal log discrepancy* $\operatorname{mld}(x; X, \Delta)$ is the infimum of the log discrepancies $a(E, X, \Delta) + 1$ over the prime divisors $E$ over $X$ with centre $x$. It is $-\infty$ if the pair is not lc near $x$.

Lean: `MinimalModel.mld`, in the project library.

**Conjecture 1.1.21 (ACC for minimal log discrepancies).** Fix $n$ and a set $I \subset [0, 1]$ that satisfies the descending chain condition. Then the set of the numbers $\operatorname{mld}(x; X, \Delta)$, for lc pairs of dimension $n$ with the coefficients of $\Delta$ in $I$ and closed points $x$, satisfies the ascending chain condition.

Node: MMWK2DDDPC · Lean: `MinimalModel.ACCMld`

**Conjecture 1.1.22 (Lower semicontinuity of minimal log discrepancies).** Let $(X, \Delta)$ be an lc pair. Then the function $x \mapsto \operatorname{mld}(x; X, \Delta)$ on the closed points of $X$ is lower semicontinuous.

Node: MMFKZ7VB29 · Lean: `MinimalModel.LSCMld`

The ACC conjecture is known for surfaces (Alexeev) and is open in dimension 3 and higher. The lower semicontinuity is known in dimension at most 3 (Ambro) and is open in dimension 4 and higher.

**Theorem 1.1.23 (Shokurov's reduction).** If the ACC conjecture and the lower semicontinuity conjecture hold in dimension $n$, then the termination conjecture holds in dimension $n$.

Node: MMFPRYMSNJ · Lean: `MinimalModel.ShokurovReduction`

**Remark 1.1.24 (A claimed case in dimension 4).** In 2026 a proof was announced that every program for a projective lc pair of dimension 4 with a rational boundary is finite. The proof comes from OpenAI problem family 056 (OAI26), and it is formalized in Lean in the repository AxiomMath/MMP at commit 1f9ade3670 (AxiomMMP), about 2.05 million lines. No human has reviewed the proof. The handbook records the result as claimed, not as a theorem, and no proof in the handbook uses it as a hypothesis.

Node: MMBTDMD2XP · Lean: `MinimalModel.TerminationLc4Rational`

### Proof in words

Discrepancies go up under flips. Let $X \dashrightarrow X^+$ be a flip over $Z$, and take a common resolution $p \colon W \to X$, $q \colon W \to X^+$. Let $G = p^*(K_X + \Delta) - q^*(K_{X^+} + \Delta^+)$. Then $p_* G = 0$, because $X$ and $X^+$ agree outside codimension 2, and $-G$ is nef over $X$, because $K_{X^+} + \Delta^+$ is ample over $Z$. The negativity lemma gives $G \ge 0$, and the coefficient of $G$ along $E$ is $a(E, X^+, \Delta^+) - a(E, X, \Delta)$. This gives $a(E, X, \Delta) \le a(E, X^+, \Delta^+)$ for every $E$, with strict inequality when the centre of $E$ on $X$ is in the flipping locus (KM98, Chapter 3).

For terminal 3-folds Shokurov turned this into a count. The *difficulty* of $X$ is the number of exceptional divisors $E$ over $X$ with $a(E, X, 0) < 1$. It is finite for a terminal 3-fold, because $X$ has isolated singularities and only finitely many divisors over them have small discrepancy. The monotonicity shows that a flip does not raise the difficulty, and the flipped curve $C^+$ makes it drop. At a general point of $C^+$ the 3-fold $X^+$ is smooth, so the blow-up of $C^+$ there gives a divisor $E$ with $a(E, X^+, 0) = 1$. Its centre on $X$ is in the flipping locus, so $a(E, X, 0) < 1$: the divisor $E$ counts for $X$ and not for $X^+$. So a sequence of flips has at most as many steps as the difficulty of $X_0$ (KMM87). Kawamata extended the argument to klt 3-fold pairs in 1992, and the lc case of dimension 3 also holds (Volume 10). In dimension 4 the same kind of count works for terminal pairs (KMM87) and canonical pairs (Fuj04), and Moraga proved termination for 4-fold flips of pairs with $K + \Delta$ pseudo-effective (Mor25).

In dimension 4 and higher the count fails. The set of divisors with small discrepancy is no longer finite in a usable way, and the discrepancies can approach a limit without reaching it. Shokurov's reduction replaces the count by a well-ordered invariant built from minimal log discrepancies. The ACC conjecture stops an infinite increasing sequence of these invariants, and the lower semicontinuity lets the invariant be read off at points of the flipping locus. The ACC conjecture is open from dimension 3 and the lower semicontinuity from dimension 4, so the reduction does not settle termination in dimension 4 and higher.

### Examples

Surfaces, computed in full. Let $X$ be a projective surface and $\varphi \colon X \to Z$ a birational contraction. Its exceptional set is a union of curves, and a curve on a surface is a divisor. So no contraction of a surface is small, and the surface program has no flips. It stops after at most $\rho(X) - 1$ steps. This proves termination for $n = 2$; for $n = 1$ there is nothing to prove.

A minimal log discrepancy, computed in full. Let $X = \frac{1}{2}(1, 1, 1)$, the quotient of $\mathbb{A}^3$ by $-1$, which is the cone over the Veronese surface. The blow-up $f \colon Y \to X$ of the vertex has exceptional divisor $E \cong \mathbb{P}^2$ with $\mathcal{O}_E(E) = \mathcal{O}_{\mathbb{P}^2}(-2)$. Adjunction gives $K_Y|_E = K_E - E|_E = \mathcal{O}_{\mathbb{P}^2}(-3 + 2) = \mathcal{O}_{\mathbb{P}^2}(-1)$. Write $K_Y = f^* K_X + aE$ and restrict to a line $\ell \subset E$: $-1 = a \cdot (-2)$, so $a = \frac{1}{2}$. The space $Y$ is smooth, so every other divisor over the vertex has a larger log discrepancy, and $\operatorname{mld}(0; X, 0) = \frac{3}{2}$. The singularity is terminal, and its difficulty is 1.

A hypothesis that fails. Let $X \to Z \leftarrow X^+$ be the Atiyah flop of Section 1.4. The flop $X \dashrightarrow X^+$ and its inverse $X^+ \dashrightarrow X$ can be repeated without end: $X \dashrightarrow X^+ \dashrightarrow X \dashrightarrow X^+ \dashrightarrow \cdots$. This sequence is infinite, so the conclusion fails. It is not a counterexample to the conjecture, because the steps are not $(K + \Delta)$-negative: $K_X \cdot C = 0$. Termination is a statement about flips, and the negativity is what makes the discrepancies increase.

### Exercises

1. (A) Show that a program for a $\mathbb{Q}$-factorial pair has at most $\rho(X) - 1$ divisorial contractions, so the program stops if every sequence of flips is finite.
2. (A) Show that the set $\{1 - \frac{1}{m} : m \ge 1\}$ satisfies the descending chain condition, and that $\{\frac{1}{m} : m \ge 1\}$ does not.
3. (A) Let $X$ be a smooth variety of dimension $n$ and $x \in X$ a closed point. Show that $\operatorname{mld}(x; X, 0) = n$, by the blow-up of $x$ and the fact that every divisor with centre $x$ has log discrepancy at least $n$.
4. (B) Let $X = \frac{1}{r}(1, 1, 1)$. Blow up the vertex and show that the exceptional divisor has $a = \frac{3}{r} - 1$. Conclude that $X$ is terminal for $r = 2$ (and smooth for $r = 1$), canonical and not terminal for $r = 3$, and klt for every $r$.
5. (B) Prove that discrepancies do not decrease under a flip: use a common resolution and the negativity lemma, as in the Proof in words.
6. (B) Explain why the infinite sequence of Atiyah flops does not contradict the termination conjecture, and find the step of the proof of monotonicity that fails for flops.

### Lean

`MinimalModel.Termination n` says that no projective lc pair of dimension $n$ has an infinite sequence of flips. `MinimalModel.TerminationLc4Rational` is stronger in its conclusion, because it rules out an infinite sequence of all steps (divisorial contractions and flips), and weaker in its class: dimension 4, lc, with rational boundary. `MinimalModel.ShokurovReduction n` is the implication from `MinimalModel.ACCMld` and `MinimalModel.LSCMld` to `MinimalModel.Termination`, with lc pairs; the class of pairs of the source is still to be checked against the statement. 3-fold termination is a node of the map with no Lean statement yet.

### Notes and history

Shokurov proved termination for terminal 3-folds in 1985 with the difficulty, and KMM87 gives the proof. Together with Mori's flips (Mor88) this gave the minimal model program for terminal 3-folds. Kawamata proved termination of log flips for klt 3-folds in 1992. Shokurov proposed the reduction to the ACC and the lower semicontinuity in 2004 (Sho04). Birkar, Cascini, Hacon and McKernan proved termination of the program with scaling for klt pairs with a big boundary (BCHM10, Volume 9), which suffices for many uses, but the general conjecture stays open in dimension 4 and higher. Volume 10 treats termination in detail, Volume 16 reports the state of dimension 4, including the claimed result of 2026, and Volume 17 lists the open cases.
