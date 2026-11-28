---
title: The ascending chain condition and semicontinuity
nodes: []
sources: [HMX14, Sho04, Amb99, Ale93, Bor97, Amb06, Kol92]
reads_with: [HMX14:thm1.1, Sho04:intro]
requires: [1.1, 4.1, 4.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The ascending chain condition and semicontinuity

### Statement

The two numbers of this chapter vary with the pair. This section asks how the sets of their values look. Volume 1, Section 1.5, explains why the answer matters: Shokurov reduced the termination of flips to two properties of minimal log discrepancies, an ascending chain condition and a lower semicontinuity. The analogue for thresholds is a theorem.

**Definition 4.6.26 (chain conditions).** A subset $S \subset \mathbb{R}$ satisfies the *ascending chain condition* (ACC) if it contains no infinite strictly increasing sequence, and the *descending chain condition* (DCC) if it contains no infinite strictly decreasing sequence. The same words apply to a subset of any linearly ordered set.

A set satisfies the ACC if and only if each of its nonempty subsets has a largest element (Exercise 1). A finite set satisfies both conditions. The set $\{1 - \frac1k : k \ge 1\}$ satisfies the DCC and not the ACC, and the set of standard coefficients $\{1 - \frac1m : m \ge 1\} \cup \{1\}$ is the main example of a DCC set of coefficients.

**Theorem 4.6.27 (ACC for log canonical thresholds; Hacon, McKernan and Xu).** Fix $n$ and sets $I \subset [0, 1]$ and $J \subset [0, \infty)$ that satisfy the DCC. The set of the numbers $\operatorname{lct}(X, \Delta; M)$, where $(X, \Delta)$ is an lc pair of dimension $n$ with the coefficients of $\Delta$ in $I$, and $M$ is an effective $\mathbb{R}$-Cartier divisor with coefficients in $J$, satisfies the ACC.

Lean: not yet in Lean. The statement is `MinimalModel.ACCLct`.

This is HMX14, Theorem 1.1. It is also Theorem 17.3.2 of Volume 17. The handbook does not prove it: the proof uses the boundedness of log Fano varieties and the minimal model program in dimension $n$.

**Conjecture 4.6.28 (ACC for minimal log discrepancies; Shokurov).** Fix $n$ and a set $I \subset [0, 1]$ that satisfies the DCC. The set of the numbers $\operatorname{mld}(x; X, \Delta)$, for lc pairs $(X, \Delta)$ of dimension $n$ with the coefficients of $\Delta$ in $I$ and closed points $x \in X$, satisfies the ACC.

This is Conjecture 1.1.21, restated with the definitions of this chapter, and the statement `MinimalModel.ACCMld` of the library.

**Conjecture 4.6.29 (lower semicontinuity of minimal log discrepancies; Ambro).** Let $(X, \Delta)$ be an lc pair. For every $t \in \mathbb{R}$ the set of closed points $x \in X$ with $\operatorname{mld}(x; X, \Delta) > t$ is the set of closed points of an open subset of $X$.

This is Conjecture 1.1.22, and the statement `MinimalModel.LSCMld`. The function $x \mapsto \operatorname{mld}(x; X, \Delta)$ on closed points is lower semicontinuous exactly when this holds.

**Conjecture 4.6.30 (the mld bound; Shokurov).** Let $(X, \Delta)$ be a pair of dimension $n$ and $x \in X$ a closed point. Then $\operatorname{mld}(x; X, \Delta) \le n$, with equality only if $X$ is smooth at $x$ and $x \notin \operatorname{Supp} \Delta$.

This is Conjecture 17.3.5 and the statement `MinimalModel.MldBound`. By Theorem 4.6.18, equality does hold at a smooth point outside $\operatorname{Supp} \Delta$.

**Theorem 4.6.31 (the known cases).** Let $I \subset [0, 1]$ satisfy the DCC.

1. (Alexeev; Shokurov.) Conjecture 4.6.28 holds for $n = 2$: the minimal log discrepancies of lc surface pairs with coefficients in $I$ satisfy the ACC.
2. (Ambro.) Conjecture 4.6.29 holds for pairs of dimension at most 3, and for toric pairs $(U_\sigma, \Delta)$ with $\Delta$ invariant under the torus in every dimension.
3. (Borisov.) The minimal log discrepancies of the $\mathbb{Q}$-Gorenstein affine toric varieties of dimension $n$, with $\Delta = 0$, satisfy the ACC.
4. (Ambro.) The minimal log discrepancies of the toric pairs of dimension $n$, with $\Delta$ invariant under the torus and coefficients in $I$, satisfy the ACC.

Lean: not yet in Lean.

The references are Ale93 for part 1, with an independent proof in Shokurov's work on surfaces, Amb99 for part 2, Bor97 for part 3 and Amb06 for part 4. In dimension 3 and higher, Conjecture 4.6.28 is open, and in dimension 4 and higher so is Conjecture 4.6.29.

The bridge from these conjectures to termination is a lemma with no geometry, which is proved here in full. Let $\mathcal{S}$ be a set of *states* with a relation $x \to y$, the *steps*. Each state $x$ has a topological space $P_x$, a nonempty compact subset $L_x \subset P_x$, the *locus*, and a function $a_x \colon P_x \to \mathbb{R}$, the *local invariant*. The function $a_x$ is *lower semicontinuous on $L_x$* if for every $p \in L_x$ and every $s < a_x(p)$ there is a neighbourhood $U$ of $p$ with $a_x > s$ on $U \cap L_x$.

**Lemma 4.6.32 (the abstract Shokurov lemma).** Suppose that every $a_x$ is lower semicontinuous on $L_x$, that all the values $a_x(p)$ with $p \in L_x$ lie in a set $S \subset \mathbb{R}$ that satisfies the ACC, and that each step $x \to y$ improves the invariant: for every $q \in L_y$ there is $p \in L_x$ with $a_x(p) < a_y(q)$. Then there is no infinite sequence of steps $x_0 \to x_1 \to x_2 \to \cdots$.

Lean: `MinimalModel.shokurovLemma`, a proof of the pinned statement `MinimalModel.ShokurovLemma`, with values in any linear order.

**Theorem 4.6.33 (Shokurov's reduction).** If Conjectures 4.6.28 and 4.6.29 hold in dimension $n$, then every sequence of flips of lc pairs of dimension $n$ is finite.

Lean: not yet in Lean. The statement is `MinimalModel.ShokurovReduction`, with the termination conjecture `MinimalModel.Termination`.

This is Sho04, the main theorem, and Theorem 1.1.23 of Volume 1. The handbook states it for lc pairs, as Volume 1 and the library do. The source states it for the pairs that the flips of the minimal model program produce, and its class of pairs is to be checked against the source before the statement is used.

### Proof in words

For the abstract lemma: lower semicontinuity and compactness make the invariant attain its minimum on each locus. Then the improvement at each step says that the minimum strictly increases. A strictly increasing sequence of values in an ACC set is finite. Without the lower semicontinuity the infimum on a locus need not be a value, so it need not lie in $S$, and the argument breaks (Problem 12).

For Shokurov's reduction, the steps are the flips $X_i \dashrightarrow X_{i+1}$, and the input from geometry is the monotonicity of discrepancies (Volume 1, Section 1.5): $a(E, X_i, \Delta_i) \le a(E, X_{i+1}, \Delta_{i+1})$ for every $E$, with strict inequality when the centre of $E$ on $X_i$ lies in the flipping locus. So minimal log discrepancies over the flipped loci go up. The ACC conjecture puts all the values in one ACC set, since the coefficients of $\Delta_i$ do not change, and the lower semicontinuity makes the minima over the closed loci values of the function. Shokurov's argument organizes the flipping loci by dimension and applies the abstract lemma to invariants built from minimal log discrepancies, in a finite induction (Sho04). The lemma is the only part of the argument with no geometry, and it is the part proved here.

### Examples

**Example 4.6.34 (the thresholds of the curves $x^a + y^b$).** By Example 4.6.13, the thresholds of the curves $x^a + y^b = 0$ in $\mathbb{A}^2$ form the set
$$T = \Big\{ \min\Big\{1, \frac1a + \frac1b\Big\} : a, b \ge 1 \Big\}.$$
It satisfies the ACC, as Theorem 4.6.27 predicts with $I = \{0\}$ and $J = \{1\}$. Directly: let $t_i = \frac1{a_i} + \frac1{b_i}$ be strictly increasing, with $a_i \le b_i$. Then $t_i \ge t_0 > 0$ and $\frac1{a_i} \ge \frac{t_i}{2} \ge \frac{t_0}{2}$, so $a_i$ is bounded, and after passing to a subsequence $a_i = a$ is constant. Then $\frac1{b_i}$ is strictly increasing, so $b_i$ is a strictly decreasing sequence of positive integers, which is finite. The set has the accumulation points $\frac1a$, as $b \to \infty$, and $0$, and each of them is approached from above: the thresholds can decrease to a limit, and they never increase to one.

**Example 4.6.35 (the DCC hypothesis is needed).** Let $L \subset \mathbb{A}^2$ be a line and $x \in L$. By Theorem 4.6.18, $\operatorname{mld}(x; \mathbb{A}^2, \frac1k L) = 2 - \frac1k$. These numbers increase strictly with $k$. So for the coefficient set $I = \{\frac1k : k \ge 1\}$, which satisfies the ACC and not the DCC, the minimal log discrepancies of surface pairs with coefficients in $I$ do not satisfy the ACC. The same pairs with $I = \{1 - \frac1k\}$ give $1 + \frac1k$, a decreasing sequence, in agreement with part 1 of Theorem 4.6.31.

**Example 4.6.36 (semicontinuity on a simple pair).** Let $\Delta = \frac12 L_1 + \frac13 L_2$ on $\mathbb{A}^2$, with $L_1 = \{x = 0\}$ and $L_2 = \{y = 0\}$. By Theorem 4.6.18 the minimal log discrepancy at a closed point is
$$2 \text{ off } L_1 \cup L_2, \qquad \frac32 \text{ on } L_1 \setminus \{0\}, \qquad \frac53 \text{ on } L_2 \setminus \{0\}, \qquad \frac76 \text{ at the origin}.$$
The sets $\{\operatorname{mld} \le t\}$ are $\{0\}$ for $\frac76 \le t < \frac32$, then $L_1$ for $\frac32 \le t < \frac53$, then $L_1 \cup L_2$ for $\frac53 \le t < 2$, and the plane for $t \ge 2$, all closed, as Corollary 4.6.19 says. The minimum $\frac76$ over the closed locus $L_1$ is attained at the origin. The generic point $\eta$ of $L_1$ has $\operatorname{mld}(L_1; \mathbb{A}^2, \Delta) = \frac12$, smaller than the value at any closed point of $L_1$. So the plain function $W \mapsto \operatorname{mld}(W)$ on all scheme points is not lower semicontinuous: the set where it is at most $\frac12$ contains $\eta$ and none of its specializations. This is why Conjecture 4.6.29 is stated on closed points. On all points the natural function is $W \mapsto \operatorname{mld}(W) + \dim W$, which agrees with $\operatorname{mld}$ on closed points and, by Theorem 4.6.18, equals $2 - \sum_{W \subset L_i} b_i$ here, a lower semicontinuous function.

### Proof

*The abstract lemma.* First, for each state $x$ the function $a_x$ attains its minimum on $L_x$. Suppose not. Then for each $p \in L_x$ there is $p' \in L_x$ with $a_x(p') < a_x(p)$, and by lower semicontinuity with $s = a_x(p')$ there is an open neighbourhood $U_p$ of $p$ with $a_x > a_x(p')$ on $U_p \cap L_x$. The sets $U_p$ cover the compact set $L_x$, so finitely many of them, $U_{p_1}, \dots, U_{p_r}$, cover it. Among $p_1', \dots, p_r'$ choose $p_j'$ with the least value of $a_x$. The point $p_j'$ lies in $L_x$, so in some $U_{p_i}$, and then $a_x(p_j') > a_x(p_i') \ge a_x(p_j')$, a contradiction. Let $\mu(x) = \min_{L_x} a_x$. It is a value of $a_x$ on $L_x$, so $\mu(x) \in S$.

Next, $\mu(x) < \mu(y)$ for every step $x \to y$. Choose $q \in L_y$ with $a_y(q) = \mu(y)$. By hypothesis there is $p \in L_x$ with $a_x(p) < a_y(q)$, so $\mu(x) \le a_x(p) < \mu(y)$.

So an infinite sequence of steps $x_0 \to x_1 \to \cdots$ gives an infinite strictly increasing sequence $\mu(x_0) < \mu(x_1) < \cdots$ in $S$, which contradicts the ACC. $\square$

*The known cases.* Theorem 4.6.27 is HMX14, Theorem 1.1. The four parts of Theorem 4.6.31 are proved in Ale93, Amb99, Bor97 and Amb06, as listed after the statement. In the toric case, Theorem 4.6.20 turns the minimal log discrepancy into a minimum of a linear function over the lattice points of a cone, and the chain conditions become statements about lattice points of cones.

*Shokurov's reduction.* This is the main theorem of Sho04, and Theorem 1.1.23 of Volume 1. The geometric input, the monotonicity of discrepancies under flips, is proved in Volume 1, Section 1.5, from the negativity lemma. The combinatorial input is Lemma 4.6.32. The organization of the flipping loci by dimension, which connects them, is in Sho04 and is not reproduced here. $\square$

### Exercises

1. (A) Show that $S \subset \mathbb{R}$ satisfies the ACC if and only if every nonempty subset of $S$ has a largest element, and the DCC if and only if every nonempty subset has a smallest element.
2. (A) Show that the strict inequality in Lemma 4.6.32 cannot be weakened to $a_x(p) \le a_y(q)$: give one state with a step to itself and a constant invariant.
3. (B) Show that the compactness in Lemma 4.6.32 cannot be dropped. Take $S = \{-1, -2, -3, \dots\}$, which satisfies the ACC, and a single state with $L = P = \mathbb{Z}_{\ge 1}$ with the discrete topology, $a(p) = -p$, and a step from the state to itself.
4. (B) Show that the set $\{ \min\{1, \frac1a + \frac1b + \frac1c\} : a, b, c \ge 1 \}$ of the thresholds of Exercise 6 of Section 2 satisfies the ACC, and find its accumulation points.
5. (B) Show that the set $\{\operatorname{mld}(x; \mathbb{A}^2, cL) : c \in I\}$, for a line $L$ and $x \in L$, satisfies the ACC if and only if $I \subset [0, 1]$ satisfies the DCC. Show that the minimal log discrepancies $1 + \frac1r$ of Example 4.6.23 form a set that satisfies the ACC and not the DCC.
6. (C) Let $I \subset [0, 1]$ satisfy the DCC. Show that the set of sums of at most $n$ elements of $I$ satisfies the DCC. Deduce that the minimal log discrepancies at closed points of snc pairs $(Y, \Delta)$ of dimension $n$ with coefficients in $I$ form a set that satisfies the ACC. This is the case of Conjecture 4.6.28 for smooth $Y$ with snc boundary.

### Lean

The library states the conjectures and the theorem of this section with the definitions `MinimalModel.mld` and `MinimalModel.lct` of Sections 1 and 3. `MinimalModel.ACCLct` is Theorem 4.6.27, `MinimalModel.ACCMld` is Conjecture 4.6.28, `MinimalModel.LSCMld` is Conjecture 4.6.29, and `MinimalModel.MldBound` is Conjecture 4.6.30. The reduction is the implication `MinimalModel.ShokurovReduction`, from `MinimalModel.ACCMld` and `MinimalModel.LSCMld` to `MinimalModel.Termination`, and it is not proved. The abstract lemma is proved: `MinimalModel.not_exists_chain_of_acc` is the last step of the proof, that an invariant that strictly increases in an ACC set gives no infinite sequence, `MinimalModel.not_exists_chain_of_lsc` is Lemma 4.6.32, and `MinimalModel.shokurovLemma` proves the pinned statement `MinimalModel.ShokurovLemma` from it.

### Notes and history

Shokurov conjectured the ACC for log canonical thresholds in his work of 1992 on 3-fold log flips, and Kol92 records it. Alexeev proved it for surfaces (Ale93). Hacon, McKernan and Xu proved it in every dimension (HMX14), by an induction that uses the boundedness of log Fano varieties and gives the global ACC for the volume and for numerically trivial pairs at the same time. Shokurov proposed the ACC for minimal log discrepancies and reduced termination to it and to the lower semicontinuity (Sho04). Ambro formulated the lower semicontinuity and proved it in dimension at most 3 and in the toric case (Amb99). The toric ACC goes back to Borisov (Bor97), and Ambro described the set of toric minimal log discrepancies and its accumulation points (Amb06). Volume 17, Chapter 3, treats the present state of the two conjectures and the later reductions of termination to other forms of the ACC.
