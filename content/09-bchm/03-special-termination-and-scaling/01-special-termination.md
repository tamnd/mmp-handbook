---
title: Special termination
nodes: [MMFCAWE0XH]
sources: [BCHM10, Fuj11, Cor07, Sho04, KM98]
reads_with: [BCHM10:4, Cor07:4]
requires: [4.2, 4.5, 7.6, 8.1, 8.3, 8.4]
level: advanced
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Special termination

### Statement

Recall from Definition 8.4.19 that a sequence of flips of a $\mathbb{Q}$-factorial dlt pair $(X, \Delta)$ satisfies special termination if after finitely many steps the flipping loci are disjoint from $\lfloor \Delta_i \rfloor$, and that every sequence of 3-fold flips does, Theorem 8.4.20. Throughout, $X = X_0 \dashrightarrow X_1 \dashrightarrow \cdots$ is a sequence of flips $X_i \to Z_i \leftarrow X_{i+1}$ of $(K_{X_i} + \Delta_i)$-negative extremal rays, projective over $U$, with $\Delta_{i+1}$ the strict transform of $\Delta_i$ and every $(X_i, \Delta_i)$ a $\mathbb{Q}$-factorial dlt pair. The lc centres are those of Definition 7.6.7.

**Lemma 9.3.1 (lc centres leave the flipping loci).** In such a sequence, the number $N_i$ of lc centres of $(X_i, \Delta_i)$ is finite and $N_{i+1} \le N_i$, with strict inequality if the flipping locus $\operatorname{Exc}(X_i \to Z_i)$ contains an lc centre of $(X_i, \Delta_i)$. No flipped locus $\operatorname{Exc}(X_{i+1} \to Z_i)$ contains an lc centre of $(X_{i+1}, \Delta_{i+1})$. So after finitely many steps no flipping or flipped locus contains an lc centre.

Lean: not yet in Lean.

**Theorem 9.3.2 (special termination from termination in lower dimension).** Let $n \ge 2$ and suppose that every sequence of flips of $\mathbb{Q}$-factorial dlt pairs of dimension at most $n - 1$ terminates. Then every sequence of flips of $n$-dimensional $\mathbb{Q}$-factorial dlt pairs as above satisfies special termination.

Lean: not yet in Lean.

**Theorem 9.3.3 ($E_{n-1} \Rightarrow B_n$).** Let $n \ge 2$. If Theorem 9.1.8 holds in dimension $n - 1$, then Theorem 9.1.5 holds in dimension $n$.

Lean: not yet in Lean.

**Theorem 9.3.4 (special termination for the program with scaling).** Suppose Theorem 9.1.5 holds in dimension $n$. Let $(X, \Delta)$ be an $n$-dimensional $\mathbb{Q}$-factorial dlt pair, projective over $U$, with $\Delta \in \mathcal{L}_{S + A}(V)$ for $S = \lfloor \Delta \rfloor$, a general ample $\mathbb{Q}$-divisor $A$ over $U$ and $V$ as in Definition 9.1.2, and let $C \ge 0$ with $\Delta + C \in \mathcal{L}_{S + A}(V)$, $(X, \Delta + C)$ dlt and $K_X + \Delta + C$ nef over $U$. Then every $(K_X + \Delta)$-program with scaling of $C$ over $U$, in the sense of Definition 9.3.6, satisfies special termination.

Lean: not yet in Lean.

### Proof in words

A flip only raises discrepancies, and raises them strictly over the flipping locus. An lc centre is a place of discrepancy $-1$, the smallest value allowed, so an lc centre inside a flipped locus would come from a divisor of discrepancy less than $-1$ before the flip, which is impossible; and an lc centre inside a flipping locus is destroyed. As there are finitely many lc centres, this can happen only finitely often.

After that, every flip is an isomorphism near the generic point of every lc centre, and in particular near the generic point of each component $S$ of $\lfloor \Delta \rfloor$. Adjunction restricts $K_X + \Delta$ to $K_S + \Delta_S$, and the flips restrict to birational maps of $S$ that are isomorphisms in codimension one, with the same flavour as the steps of a minimal model program on $S$. Termination in lower dimension, or, for the program with scaling, finiteness of models near $S$, then forces the flips to be isomorphisms near $S$ after finitely many steps.

### Examples

**Example 9.3.5 (the restriction of a flip to a boundary component).** In the toric 4-fold flip of Example 9.2.4, $(X^-, D_4)$ is a plt pair and its only lc centre is $S = D_4$. The flipping locus $V(\operatorname{Cone}(u_4, u_5)) \cong \mathbb{P}^2$ lies inside $S$, but it is not an lc centre, so Lemma 9.3.1 says nothing, and $N_0 = N_1 = 1$. The flip restricts on $S$ to the blow-down $S^- = \operatorname{Bl}_0 \mathbb{A}^3 \to S^+ = \mathbb{A}^3$, a birational morphism that contracts the divisor $E \cong \mathbb{P}^2$ of $S^-$. So the restriction of a flip to a boundary component need not be a flip: here it is a $K_S$-negative divisorial contraction, as $K_S = 2E$ and $E \cdot \ell = -1$ for a line $\ell$ in $E$. This is why the proof of Theorem 9.3.2 counts the divisors of $S$ and their discrepancies, and does not treat the restricted maps as flips. The flipping locus meets $S$, so this one-step sequence is not yet special: special termination is about long sequences, and it asserts that only finitely many such steps occur.

### Proof

*Lemma 9.3.1.* An lc centre of $(X_i, \Delta_i)$ is the centre of a divisor $G$ over $X_i$ with $a(G, X_i, \Delta_i) = -1$. As the pair is dlt, the lc centres are the strata of $\lfloor \Delta_i \rfloor$, the irreducible components of intersections of its components, by the definition of dlt, Definition 4.2.2; so $N_i$ is finite.

Let $W$ be an lc centre of $(X_{i+1}, \Delta_{i+1})$ and $G$ a divisor over $X_{i+1}$ with centre $W$ and $a(G, X_{i+1}, \Delta_{i+1}) = -1$. If $W$ were contained in the flipped locus, Lemma 8.1.19 would give $a(G, X_i, \Delta_i) < a(G, X_{i+1}, \Delta_{i+1}) = -1$, contradicting that $(X_i, \Delta_i)$ is log canonical. So $W$ is not contained in the flipped locus, the flip is an isomorphism near the generic point of $W$, and the strict transform $W'$ of $W$ in $X_i$ is the centre of $G$ on $X_i$, where by Lemma 8.1.19 $a(G, X_i, \Delta_i) = a(G, X_{i+1}, \Delta_{i+1}) = -1$, as the centre of $G$ on $X_i$ is not contained in the flipping locus. So $W'$ is an lc centre of $(X_i, \Delta_i)$ not contained in the flipping locus, and $W \mapsto W'$ is injective, since the flip is an isomorphism near the generic points. This gives $N_{i+1} \le N_i$ and the statement about flipped loci. If the flipping locus contains an lc centre $W'$ of $(X_i, \Delta_i)$, then $W'$ is not in the image of $W \mapsto W'$, so $N_{i+1} < N_i$. A non-increasing sequence of non-negative integers is eventually constant, and from then on no flipping locus contains an lc centre.

*Theorem 9.3.2.* This is Fujino's theorem, in Cor07, Chapter 4, and Fuj11; the following is an outline. By Lemma 9.3.1, after finitely many steps no flipping or flipped locus contains an lc centre. One proves by induction on $d$ that after finitely many further steps the flipping loci are disjoint from the lc centres of dimension at most $d$. For $d = 0$ this is the case: an lc centre that is a point and lies in a flipping locus would be contained in it. Let $W$ be an lc centre of dimension $d$ and assume the flipping loci are eventually disjoint from the lc centres of smaller dimension. Then near $W$ the pair is plt along the generic point of each such stratum, and by adjunction, Theorem 4.5.17, $(K_{X_i} + \Delta_i)|_{W_i} = K_{W_i} + \Delta_{W_i}$ for the strict transforms $W_i$ of $W$, with $(W_i, \Delta_{W_i})$ dlt, and $W_i$ normal by Theorem 4.5.18 in the plt case. The induced maps $W_i \dashrightarrow W_{i+1}$ are isomorphisms in codimension one after finitely many steps, since the discrepancies $a(G, W_i, \Delta_{W_i})$ of the finitely many divisors $G$ over $W$ with negative discrepancy can only increase, and they take values in a finite set. A Q-factorialization of the $W_i$, which exists by a dlt modification and the induction, turns them into a sequence of flips of $\mathbb{Q}$-factorial dlt pairs of dimension $d \le n - 1$, which terminates by hypothesis. Hence the maps $W_i \dashrightarrow W_{i+1}$ are eventually isomorphisms, and, using that $-(K_{X_i} + \Delta_i)$ is ample on the flipping curves, the flipping loci are eventually disjoint from $W_i$. The last implication and the existence of the Q-factorializations are the delicate points of the argument, and they are not proved here.

*Theorem 9.3.3.* An outline, following BCHM10, Section 4. Let $\varphi \colon X \dashrightarrow Z$ be a weak log canonical model of $K_X + \Delta$ with $\Delta \in \mathcal{C}$ that contracts no component $S_i$ of $S$. By adjunction, Theorem 4.5.17, the induced map $S_i \dashrightarrow T_i$ to the strict transform of $S_i$ on $Z$ is a weak log canonical model of $K_{S_i} + \Delta_{S_i}$, where $(K_X + \Delta)|_{S_i} = K_{S_i} + \Delta_{S_i}$, up to the normalization of $T_i$. The boundaries $\Delta_{S_i}$, as $\Delta$ runs through the rational polytope $\mathcal{C}$, run through a rational polytope of boundaries on $S_i$ of the form $A|_{S_i} + B'$, because the different depends affinely on $\Delta$ (Lemma 7.6.1 and the formula of Definition 4.5.5). So $E_{n-1}$ on $S_i$ gives finitely many models of $S_i$. A model $Z$ is determined near $S$ by its restriction to the $S_i$ and the classes of $K_Z + \varphi_* \Delta$ near $S$, and BCHM10 show, with a further induction on the number of components and the dimension of $\mathcal{C}$, that finitely many maps $\varphi_j$ suffice. The details are not reproduced here.

*Theorem 9.3.4.* An outline, following BCHM10, Section 4. By Lemma 9.3.1 one may assume that no flipping locus contains an lc centre, so no step contracts a component of $S$ and every $X_i$ is isomorphic to $X$ near the generic point of each stratum of $S$. By Proposition 9.3.10 each $X_i$ is a weak log canonical model of $K_X + \Delta + t C$ for $t \in [\lambda_i, \lambda_{i-1}]$, and these boundaries lie in the rational polytope $\mathcal{C} = \{\Delta + tC : 0 \le t \le 1\} \subseteq \mathcal{L}_{S + A}(V)$, on which the pairs are dlt. By Theorem 9.1.5 there are finitely many maps $\varphi_j$ such that each $X_i$ is isomorphic near the strict transform of $S$ to one of the $Z_j$, compatibly with the maps from $X$. So for infinitely many $i$ the pairs $(X_i, \Delta_i)$ are isomorphic near $S$ to a fixed $(Z_j, \Delta_{Z_j})$. If infinitely many flipping loci met $S$, then infinitely many flips would strictly raise the discrepancy of some divisor whose centre meets $S$, by Lemma 8.1.19, and discrepancies never decrease along the program; but for divisors with centre on $S$ and negative discrepancy, which are finitely many up to the strict transform, the discrepancies on $X_i$ near $S$ take finitely many values, one for each $Z_j$. This is the contradiction that gives special termination; making the finiteness of the relevant divisors precise near $S$ is the technical part of the argument in BCHM10, which is not reproduced.

### Exercises

1. (A) Show that the lc centres of a $\mathbb{Q}$-factorial dlt pair $(X, S_1 + S_2)$, with $S_1, S_2$ smooth meeting transversally in an irreducible curve, are $S_1$, $S_2$ and $S_1 \cap S_2$, and compute $N$ in Lemma 9.3.1.
2. (A) Show that the restriction of the 4-fold flip of Example 9.3.5 to $D_5$ is also the blow-down of $\operatorname{Bl}_0 \mathbb{A}^3$, and that its restriction to $D_1$ is the Atiyah flop of a 3-fold, by computing the stars of $u_5$ and $u_1$ in $\Sigma^-$ and $\Sigma^+$.
3. (B) Give an example of a 3-fold flip of a dlt pair $(X, S)$ whose flipping curve meets $S$ in finitely many points, and describe the induced birational map of $S$.
4. (B) Deduce Theorem 8.4.20 from Theorem 9.3.2 and the termination of flips for surfaces, and explain why the latter is a statement about the absence of surface flips.
5. (B) Show that in a sequence of flips of a dlt pair the components of $\lfloor \Delta_i \rfloor$ are never contracted, so the number of components is constant.
6. (C) Prove Theorem 9.3.2 for $n = 3$ under the extra assumption that every component of $\lfloor \Delta \rfloor$ is smooth and the components meet transversally along smooth curves, using that the restricted maps on surfaces are compositions of blow-ups and blow-downs.

### Lean

The library states the conclusion of Theorem 9.3.2 as `MinimalModel.SpecialTermination`, with termination in every dimension below $n$ as its hypothesis. It is a statement with no proof. Lemma 9.3.1 and Theorems 9.3.3 and 9.3.4 are not in Lean.

### Notes and history

Special termination is due to Shokurov, who used it in his reduction of klt flips to pl flips, Sho04 and the 3-fold case in Volume 8. The deduction from termination in lower dimension, Theorem 9.3.2, is Fujino's, in his chapter of Cor07 and in Fuj11. BCHM10 avoid termination in lower dimension, which is not known, and replace it by special finiteness, Theorem 9.1.5, which follows from the finiteness of models in lower dimension and is enough for the program with scaling; that is Theorems 9.3.3 and 9.3.4, from BCHM10, Section 4. Example 9.3.5 is the standard warning that a flip restricts on a boundary component to a map that need not be a flip.
