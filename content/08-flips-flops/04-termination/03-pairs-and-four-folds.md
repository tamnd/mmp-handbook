---
title: Pairs in dimension 3 and terminal 4-folds
nodes: [MMH0CM56AA]
sources: [Kaw92, Sho92, KM98, KMM87, Fuj04, AHK07, Kol92]
reads_with: [Kaw92:main, KM98:6, KMM87:ch5]
requires: [4.2, 4.5, 4.6]
level: core
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Pairs in dimension 3 and terminal 4-folds

### Statement

This section is a survey. The theorems in it are cited, and their proofs are outlined, not given in full. The ground field is algebraically closed of characteristic $0$.

Section 2 used two facts about a terminal or canonical 3-fold: the difficulty is finite, and a flipped curve lies in the smooth locus at its generic point, so that its blow-up has discrepancy exactly $1$. For a pair $(X, \Delta)$ both fail. Example 8.4.18 shows that the count is infinite at a klt point that is not canonical, and a flipped curve contained in $\operatorname{Supp} \Delta^+$ gives a blow-up with $a(E, X^+, \Delta^+) = 1 - \operatorname{mult}_{C^+} \Delta^+ < 1$, which the count already contains. The proofs for pairs therefore split the flips into those whose flipped curves lie in the reduced boundary, handled by special termination, and the others, handled by a count with weights.

**Definition 8.4.19 (special termination).** Let $(X, \Delta)$ be a $\mathbb{Q}$-factorial dlt pair. A sequence of $(K + \Delta)$-flips starting at $(X, \Delta)$ satisfies *special termination* if, after finitely many steps, the flipping loci are disjoint from $\lfloor \Delta_i \rfloor$.

**Theorem 8.4.20 (special termination in dimension 3, cited).** Every sequence of flips of a $\mathbb{Q}$-factorial dlt 3-fold pair satisfies special termination.

Lean: not yet in Lean.

**Theorem 8.4.21 (termination of 3-fold log flips, Kawamata; Shokurov; cited).** Let $(X, \Delta)$ be an lc pair of dimension $3$. There is no infinite sequence of $(K_X + \Delta)$-flips starting at $(X, \Delta)$.

Node: MMH0CM56AA · Lean: `MinimalModel.ThreefoldTermination`

**Theorem 8.4.22 (terminal 4-folds, Kawamata, Matsuda and Matsuki; cited).** Let $X$ be a terminal 4-fold. There is no infinite sequence of $K_X$-flips starting at $X$.

Lean: not yet in Lean.

**Theorem 8.4.23 (canonical 4-folds, Fujino; cited).** Let $X$ be a canonical 4-fold. There is no infinite sequence of $K_X$-flips starting at $X$.

Lean: not yet in Lean.

**Theorem 8.4.24 (Alexeev, Hacon and Kawamata; cited).** Let $(X, \Delta)$ be a klt pair of dimension $4$ such that $-(K_X + \Delta)$ is numerically equivalent to an effective divisor. Then every sequence of $(K_X + \Delta)$-flips starting at $(X, \Delta)$ is finite.

Lean: not yet in Lean.

### Proof in words

*Outline for Theorem 8.4.20.* A flip of a dlt pair restricts, on each component $S$ of $\lfloor \Delta \rfloor$, to a birational map of surfaces $S \dashrightarrow S^+$, and by adjunction (Volume 4, Chapter 5) the pairs $(S, \operatorname{Diff}_S(\Delta - S))$ are klt surface pairs whose discrepancies go up, by the argument of Lemma 8.4.2 applied on $S$. A klt surface pair has finitely many exceptional divisors with discrepancy at most $0$ over it, the coefficients of the different lie in a finite set determined by the coefficients of $\Delta$ (Theorem 4.5.12), and a map $S \dashrightarrow S^+$ that contracts a curve lowers the Picard number. A count of these divisors together with the Picard number shows that after finitely many steps every $S \dashrightarrow S^+$ is an isomorphism in codimension $1$, hence an isomorphism of normal surfaces. A further argument with the intersection numbers of the flipping curves with the components of $\lfloor \Delta \rfloor$ then shows that the flipping loci are eventually disjoint from $\lfloor \Delta \rfloor$.

*Outline for Theorem 8.4.21.* By a dlt modification and the comparison of discrepancies, the klt case is the main one. Replace $(X, \Delta)$ by a $\mathbb{Q}$-factorial dlt pair whose reduced boundary contains all divisors over $X$ with log discrepancy $0$ that matter, so that by Theorem 8.4.20 the flipping curves eventually miss $\lfloor \Delta \rfloor$. For the remaining flips, the flipped curves are not in the reduced boundary, and a count of exceptional divisors in the style of Definition 8.4.8, with thresholds determined by the coefficients of $\Delta$ in place of the single threshold $1$, is finite and drops at each such flip, by the argument of Theorem 8.4.11 with the blow-up of a flipped curve. Kawamata's proof (Kaw92) treats the lc case by this route; Shokurov's (Sho92) is close to it.

*Outline for Theorems 8.4.22 to 8.4.24.* In dimension 4 the flipped locus of a terminal flip is a curve or a surface. For a surface the count of Section 2 still drops. For a curve $C^+$ the blow-up has discrepancy $2$ over $X^+$, the count of divisors with discrepancy less than $1$ need not drop, and Kawamata, Matsuda and Matsuki combine it with a second count adapted to the flips whose flipped locus is a curve (KMM87, Chapter 5). Fujino's canonical case needs a finer analysis of the flips through curves of canonical singularities. Alexeev, Hacon and Kawamata combine special termination with results on the minimal log discrepancies of 3-folds, in the spirit of Shokurov's reduction, Theorem 4.6.33.

### Examples

**Example 8.4.25 (a flipped curve in the boundary).** In Example 8.4.7 take $\Delta = b D_3$ with $0 < b < 1$. The flipped curve $C^+ = V(\operatorname{Cone}(u_3, u_4))$ lies in $D_3^+$, the blow-up $E_v$ of $C^+$ has $a(E_v, X^+, bD_3^+) = 1 - b < 1$, and it is counted by $\#\{E : a(E, X^+, \Delta^+) < 1\}$. So the count of Definition 8.4.8, applied to the pair, contains $E_v$ on both sides. It is in fact infinite on both sides: the blow-up of any smooth curve in $D_3$, at a general point of the curve, has discrepancy $1 - b < 1$. With the threshold $1 - b$ in place of $1$ the picture changes: $a(E_v, X^-, bD_3) = \frac{1-b}{2} < 1 - b$, while $a(E_v, X^+, b D_3^+) = 1 - b$ is not less than $1 - b$, and the blow-ups of curves in $D_3$ are no longer counted. This is the role of the thresholds in the outline.

**Example 8.4.26 (special termination for a surface).** Let $X$ be a smooth 3-fold and $S \subset X$ a smooth surface containing a $(-1)$-curve $\ell$ with $N_{\ell / X} = \mathcal{O}(-1) \oplus \mathcal{O}(-1)$, so that $S \cdot \ell = -1$ and $(K_X + S) \cdot \ell = K_S \cdot \ell = -1$. A $(K_X + S)$-flop or flip in $\ell$ restricts on $S$ to the contraction of $\ell$: the strict transform $S^+$ is $S$ with $\ell$ contracted, and its Picard number is one less. This is the step of Theorem 8.4.20 that lowers the Picard number of the boundary, and it can happen only finitely many times.

### Exercises

1. (A) In Example 8.4.25, let $\Gamma \subset D_3^+$ be a smooth curve through no torus fixed point. Compute the discrepancy of the blow-up of $\Gamma$ for the pair $(X^+, bD_3^+)$, and conclude that infinitely many exceptional divisors have discrepancy less than $1$.
2. (A) In Example 8.4.26, check $(K_X + S) \cdot \ell = -1$ with adjunction, and show that $S^+$ is smooth.
3. (B) Let $(S, B)$ be a klt surface pair with the coefficients of $B$ in a finite set. Show that a sequence of birational contractions $(S, B) \to (S_1, B_1) \to \cdots$, each contracting one curve, has length at most $\rho(S) - 1$.
4. (B) Show that in dimension 4 the blow-up $E$ of a smooth flipped curve $C^+$ in the smooth locus of $X^+$ has $a(E, X^+) = 2$, and give an inequality for $a(E, X)$ from Lemma 8.4.2.
5. (B) Let $X$ be a smooth 3-fold, $D \subset X$ a smooth surface and $0 < b < 1$. Using Theorem 4.2.12, show that no exceptional divisor over $X$ has $a(E, X, bD) < 1 - b$, and that infinitely many have $a(E, X, bD) = 1 - b$.
6. (C) Read Theorem 4.6.33 and explain in a paragraph why ACC and lower semicontinuity for minimal log discrepancies would give termination in every dimension, and which part of that argument the difficulty of Section 2 replaces in dimension 3.

### Lean

`MinimalModel.ThreefoldTermination` states Theorem 8.4.21 as a statement without proof, and `MinimalModel.SpecialTermination` states special termination. The 4-fold theorems are not yet in Lean.

### Notes and history

Theorem 8.4.21 is Kawamata's (Kaw92) for lc 3-folds; Shokurov (Sho92) gave termination for 3-fold log flips with a related argument, and Kollár et al. (Kol92) collect the 3-fold theory. Theorem 8.4.22 is in KMM87, Chapter 5, Theorem 8.4.23 is Fuj04, and Theorem 8.4.24 is AHK07, whose hypotheses are stated there in full and are only paraphrased here. Termination of flips in general is the conjecture of Volume 1; its status in dimension 4 and higher, and the reductions of Shokurov, Birkar and others, are the subject of Volume 10.
