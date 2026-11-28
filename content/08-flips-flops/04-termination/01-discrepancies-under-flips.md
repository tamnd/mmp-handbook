---
title: Discrepancies under flips and flops
nodes: []
sources: [KM98, KMM87, Sho85]
reads_with: [KM98:3.7, KMM87:ch5]
requires: [1.5, 3.5, 3.6, 4.1, 4.2, P8.13]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Discrepancies under flips and flops

### Statement

The ground field $k$ is algebraically closed of characteristic $0$. Discrepancies are those of Definition 4.1.4, for divisors over $X$ in the sense of Definition 4.1.11. The conventions on flips are those of Chapter 1 and of Volume 3, Definition 3.5.19, in the following form.

**Definition 8.4.1 (flips of pairs).** Let $(X, \Delta)$ be a pair with $X$ normal and $\Delta$ an effective $\mathbb{Q}$-divisor such that $K_X + \Delta$ is $\mathbb{Q}$-Cartier. A *flipping contraction* of $(X, \Delta)$ is a small projective birational morphism $\varphi \colon X \to Z$ onto a normal variety, not an isomorphism, with $-(K_X + \Delta)$ $\varphi$-ample. Its *flip* is a small projective birational morphism $\varphi^+ \colon X^+ \to Z$ from a normal variety such that, for the strict transform $\Delta^+$ of $\Delta$, the divisor $K_{X^+} + \Delta^+$ is $\mathbb{Q}$-Cartier and $\varphi^+$-ample. The *flipping locus* $\operatorname{Ex}(\varphi)$ is the set of points of $X$ at which $\varphi$ is not a local isomorphism, equivalently the union of the positive dimensional fibres of $\varphi$, and the *flipped locus* is $\operatorname{Ex}(\varphi^+)$. A *flop* is defined in the same way with $K_X + \Delta$ numerically trivial over $Z$, a divisor $D$ with $-D$ $\varphi$-ample in place of $K_X + \Delta$, and $D^+$ $\varphi^+$-ample.

The rational map $X \dashrightarrow X^+$ is an isomorphism in codimension $1$, since both $\varphi$ and $\varphi^+$ are small, so the prime divisors of $X$, $X^+$ and $Z$ correspond, and a divisor over $X$ is the same as a divisor over $X^+$. It is exceptional over $X$ if and only if it is exceptional over $X^+$.

**Lemma 8.4.2 (discrepancies under a flip).** Let $\varphi \colon X \to Z$ be a flipping contraction of $(X, \Delta)$ with flip $\varphi^+ \colon X^+ \to Z$.

1. $\varphi(\operatorname{Ex}(\varphi)) = \varphi^+(\operatorname{Ex}(\varphi^+))$; call this closed set $S \subset Z$.
2. For every divisor $E$ over $X$, $a(E, X, \Delta) \le a(E, X^+, \Delta^+)$.
3. If the centre $c_Z(E)$ of $E$ on $Z$ lies in $S$, the inequality is strict.

Lean: not yet in Lean.

**Proposition 8.4.3 (discrepancies under a flop).** Let $\varphi \colon X \to Z$ and $\varphi^+ \colon X^+ \to Z$ be small projective birational morphisms of normal varieties, $\Delta$ an $\mathbb{R}$-divisor on $X$ and $\Delta^+$ its strict transform, with $K_X + \Delta$ and $K_{X^+} + \Delta^+$ both $\mathbb{R}$-Cartier and numerically trivial over $Z$. Then $a(E, X, \Delta) = a(E, X^+, \Delta^+)$ for every divisor $E$ over $X$.

Lean: not yet in Lean.

**Corollary 8.4.4 (the classes are preserved).** In the situation of Lemma 8.4.2, if $(X, \Delta)$ is terminal, canonical, klt or lc, then so is $(X^+, \Delta^+)$. In the situation of Proposition 8.4.3 the same holds in both directions.

Lean: not yet in Lean.

### Proof in words

Work over an affine neighbourhood of a point of $Z$. Sections of $m(K_X + \Delta)$ and of $m(K_{X^+} + \Delta^+)$ are rational functions with conditions along prime divisors only, and the prime divisors of $X$ and $X^+$ are the same, so the two linear systems are one. On $X^+$ the system is free, because $K_{X^+} + \Delta^+$ is ample over an affine base. On $X$ every member contains the flipping locus, because $K_X + \Delta$ is negative on the flipping curves. Pull both back to a common resolution $W$: the difference of the two pullbacks is $B = \sum_E (a(E, X^+, \Delta^+) - a(E, X, \Delta)) E$, and the members of the first system are the members of the second plus $mB$. A general member of the free system misses any given divisor, so $B$ is effective, and it contains every divisor over the flipping locus, since the members of the first system all do. For a flop, $B$ is numerically trivial over $Z$ and pushes forward to $0$, so the negativity lemma, applied to $B$ and $-B$, gives $B = 0$.

### Examples

**Example 8.4.5 (the Francia flip).** Take the Francia flip of Volume 3, Example 3.5.24, with $u_1 + u_2 = u_3 + 2 u_4$. Write $X^-$ for the side with the two cones $\operatorname{Cone}(u_1, u_2, u_4)$, smooth, and $\operatorname{Cone}(u_1, u_2, u_3)$, of multiplicity $2$, which is the point $\frac12(1,1,1)$; the flipping curve is $C^- = V(\operatorname{Cone}(u_1, u_2))$. Write $X^+$ for the smooth side, with the cones $\operatorname{Cone}(u_2, u_3, u_4)$ and $\operatorname{Cone}(u_1, u_3, u_4)$ and the flipped curve $C^+ = V(\operatorname{Cone}(u_3, u_4))$. On $X^+$ the wall relation of $C^+$ is $u_1 + u_2 - u_3 - 2u_4 = 0$, normalized with coefficient $1$ at the two vectors off the wall, so $D_1 \cdot C^+ = D_2 \cdot C^+ = 1$, $D_3 \cdot C^+ = -1$, $D_4 \cdot C^+ = -2$, and $K_{X^+} \cdot C^+ = -(1 + 1 - 1 - 2) = 1$. On $X^-$ the relation enters with the opposite sign, and the computation of Volume 3, Example 3.5.24, divides it by $2$: $D_1 \cdot C^- = D_2 \cdot C^- = -\frac12$, $D_3 \cdot C^- = \frac12$, $D_4 \cdot C^- = 1$, so $K_{X^-} \cdot C^- = -\frac12$. These are the numbers $K \cdot C^- = -\frac12$ and $K \cdot C^+ = 1$ of the Francia flip.

Let $v = u_3 + u_4$. Then $v = \frac12(u_1 + u_2 + u_3)$, since $u_1 + u_2 - u_3 = 2u_4$. By the toric discrepancy formula, Theorem 3.3.34, the divisor $E_v$ of the ray of $v$ has discrepancy one less than the sum of the coefficients of $v$ in the cone that contains it. On $X^-$, $v$ is interior to $\operatorname{Cone}(u_1, u_2, u_3)$ with coefficients $\frac12, \frac12, \frac12$, so $a(E_v, X^-) = \frac12$; $E_v$ is the exceptional divisor of the weighted blow-up of the point $\frac12(1,1,1)$, as in Example 4.4.8. On $X^+$, $v$ lies in the two-dimensional cone $\operatorname{Cone}(u_3, u_4)$ with coefficients $1, 1$, so $a(E_v, X^+) = 1$; the star subdivision at $v$ is the blow-up of the smooth curve $C^+$. So $\frac12 < 1$, as Lemma 8.4.2 says for a divisor whose centre on $Z$ is the image point of the flipping curve.

**Example 8.4.6 (the Atiyah flop).** In Volume 3, Example 3.5.23, $u_2 + u_4 = u_1 + u_3 = (1, 1, 2)$. The vector $v = (1,1,2)$ lies in the wall $\operatorname{Cone}(u_2, u_4)$ of one side and in the wall $\operatorname{Cone}(u_1, u_3)$ of the other, with coefficients $1, 1$ in both. So the blow-up of the flopping curve on either side has exceptional divisor $E_v$ with $a(E_v, X) = a(E_v, X^+) = 1$, as Proposition 8.4.3 predicts. The divisor $E_v$ is $\mathbb{P}^1 \times \mathbb{P}^1$, the common blow-up of the two sides, and both sides contract it along one of its two rulings.

**Example 8.4.7 (a flip with a boundary).** Let $X^-$, $X^+$ and $Z$ be as in Example 8.4.5, and let $\Delta = b D_3$ with $0 \le b < 1$, where $D_3$ is the toric divisor of $u_3$. On $X^-$, $D_3 \cdot C^- = \frac12$, so $(K_{X^-} + b D_3) \cdot C^- = -\frac12(1 - b) < 0$, and on $X^+$, $(K_{X^+} + b D_3^+) \cdot C^+ = 1 - b > 0$. So the Francia flip is also the flip of the pair $(X^-, bD_3)$. The vector $v = u_3 + u_4$ has $a(E_v, X^-, bD_3) = \frac12 - \frac{b}{2}$, since the coefficient of $u_3$ in $v$ on $X^-$ is $\frac12$, and $a(E_v, X^+, bD_3^+) = 1 - b$, since the coefficient of $u_3$ in $v$ on $X^+$ is $1$. The difference is $\frac{1 - b}{2} > 0$. For $b = 1$ both intersection numbers are $0$, the map is no longer a flip of the pair, and the two discrepancies agree, as Proposition 8.4.3 says.

### Proof

*Lemma 8.4.2.* For part 1, let $S = \varphi(\operatorname{Ex}(\varphi))$ and $S^+ = \varphi^+(\operatorname{Ex}(\varphi^+))$. Over $Z \setminus S$, $\varphi$ is an isomorphism, so $K_Z + \Delta_Z$ is $\mathbb{Q}$-Cartier there, where $\Delta_Z = \varphi_* \Delta$. Over $Z \setminus S$ the divisors $K_{X^+} + \Delta^+$ and $(\varphi^+)^*(K_Z + \Delta_Z)$ are $\mathbb{Q}$-Cartier and agree outside the exceptional locus of $\varphi^+$, which has codimension at least $2$, so they are $\mathbb{Q}$-linearly equivalent. So $K_{X^+} + \Delta^+$ is numerically trivial on every curve that $\varphi^+$ contracts over $Z \setminus S$; it is also $\varphi^+$-ample, so $\varphi^+$ contracts no curve over $Z \setminus S$. A projective birational morphism onto a normal variety with finite fibres is an isomorphism, by Zariski's main theorem, so $S^+ \subseteq S$. The same argument with the roles reversed, using that $-(K_X + \Delta)$ is $\varphi$-ample, gives $S \subseteq S^+$.

For parts 2 and 3, fix $E$. The discrepancy is local on $X$ by Corollary 4.1.15, so $Z$ may be replaced by an affine neighbourhood of the generic point of $c_Z(E)$, and $X$, $X^+$ by the preimages. Choose a normal variety $W$ with projective birational morphisms $p \colon W \to X$ and $q \colon W \to X^+$ with $\varphi p = \varphi^+ q$, on which $E$ is a prime divisor: take the normalization of the closure of the graph of $X \dashrightarrow X^+$ and blow it up further, by Theorem 4.2.10 and Lemma 4.1.5. Write
$$K_W = p^*(K_X + \Delta) + \sum_F a(F, X, \Delta) F = q^*(K_{X^+} + \Delta^+) + \sum_F a(F, X^+, \Delta^+) F,$$
the sums over the prime divisors $F$ of $W$, where for a non-exceptional $F$ the coefficient is minus the coefficient of its image in $\Delta$, the same on both sides. Then
$$B := p^*(K_X + \Delta) - q^*(K_{X^+} + \Delta^+) = \sum_F \big(a(F, X^+, \Delta^+) - a(F, X, \Delta)\big) F.$$

Let $m \ge 1$ be such that $L = m(K_X + \Delta)$ and $L^+ = m(K_{X^+} + \Delta^+)$ are Cartier. Since $Z$ is affine and $L^+$ is $\varphi^+$-ample, $L^+$ is ample on $X^+$, and after replacing $m$ by a multiple, $|L^+|$ is free. For a rational function $f \in k(X) = k(X^+)$, the condition $\operatorname{div}(f) + L \ge 0$ concerns the coefficients along the prime divisors of $X$, and the condition $\operatorname{div}(f) + L^+ \ge 0$ the same coefficients along the same prime divisors of $X^+$, because $L^+$ is the strict transform of $L$. So $H^0(X, L) = H^0(X^+, L^+)$ as subspaces of $k(X)$. For such an $f$, let $G = \operatorname{div}(f) + L$ and $G^+ = \operatorname{div}(f) + L^+$. Then, on $W$,
$$p^* G = q^* G^+ + mB,$$
since $p^*\operatorname{div}(f) = q^* \operatorname{div}(f) = \operatorname{div}_W(f)$.

Since $|L^+|$ is free, there is $f$ such that $G^+$ does not contain the closed set $q(E)$. Then $\operatorname{mult}_E q^* G^+ = 0$ and $m \operatorname{mult}_E B = \operatorname{mult}_E p^* G \ge 0$. This is part 2. For part 3, suppose $c_Z(E) \subseteq S$. Then $c_X(E) \subseteq \varphi^{-1}(S) = \operatorname{Ex}(\varphi)$, which is the union of the curves contracted by $\varphi$. Each such curve $C$ has $G \cdot C = L \cdot C < 0$, so $C \subseteq \operatorname{Supp} G$. So $c_X(E) \subseteq \operatorname{Supp} G$, $E \subseteq \operatorname{Supp} p^*G$, and $m \operatorname{mult}_E B = \operatorname{mult}_E p^*G > 0$.

*Proposition 8.4.3.* Let $W$, $p$, $q$ be as above, with $E$ a divisor on $W$, and let $\psi = \varphi p = \varphi^+ q \colon W \to Z$, a projective birational morphism of normal varieties. With the same notation, $B = p^*(K_X + \Delta) - q^*(K_{X^+} + \Delta^+)$ is $\mathbb{R}$-Cartier. For a curve $\gamma \subseteq W$ contracted by $\psi$, the curves $p_*\gamma$ and $q_* \gamma$ are zero or contracted by $\varphi$ and $\varphi^+$, so $B \cdot \gamma = (K_X + \Delta) \cdot p_* \gamma - (K_{X^+} + \Delta^+) \cdot q_* \gamma = 0$ by the projection formula. So $B$ and $-B$ are $\psi$-nef. The divisor $\psi_* B$ is the difference of $\varphi_*(K_X + \Delta)$ and $\varphi^+_*(K_{X^+} + \Delta^+)$, which are the same Weil divisor $K_Z + \Delta_Z$, so $\psi_* B = 0$. By the negativity lemma, Theorem 1.5.22, applied to $B$ and to $-B$, both are effective, so $B = 0$.

*Corollary 8.4.4.* The prime divisors of $X$ and $X^+$ correspond with the same coefficients in $\Delta$ and $\Delta^+$, and the exceptional divisors over them are the same. By Lemma 8.4.2 every discrepancy over $X^+$ is at least the corresponding discrepancy over $X$. Each of the four classes is defined by a lower bound on the discrepancies of the exceptional divisors and on the coefficients of the boundary, so it passes from $(X, \Delta)$ to $(X^+, \Delta^+)$. For Proposition 8.4.3 the discrepancies are equal.

### Exercises

1. (A) In Example 8.4.5, check that $(K + \frac12 D_1) \cdot C^- = -\frac34$ and $(K + \frac12 D_1^+) \cdot C^+ = \frac32$, so that the Francia flip is also the flip of $(X^-, \frac12 D_1)$, and compute $a(E_v)$ for this pair on both sides. Then check that $K + \frac12 D_4$ is numerically trivial on $C^-$ and on $C^+$, so that for the pair $(X^-, \frac12 D_4)$ the map is a flop.
2. (A) Let $\varphi \colon X \to Z$ be a flipping contraction and $X^+$ its flip. Show that the flipped locus has dimension at most $\dim X - 2$, and that, for $\dim X = 3$, it is a nonempty union of curves.
3. (B) In the proof of Lemma 8.4.2, show directly that $\operatorname{mult}_E B > 0$ for the exceptional divisor $E_v$ of Example 8.4.5, by computing the multiplicity of $p^* G$ along $E_v$ for a member $G$ of $|2K_{X^-}|$.
4. (B) Show that the flip of a flipping contraction is unique when it exists: two flips $X^+_1$, $X^+_2$ of $\varphi$ are isomorphic over $Z$. Use the equality of sections in the proof of Lemma 8.4.2 to identify both with $\operatorname{Proj}_Z \bigoplus_{m \ge 0} \varphi_* \mathcal{O}_X(m(K_X + \Delta))$.
5. (B) State and prove a version of Lemma 8.4.2 for a $D$-flip, where $D$ is a $\mathbb{Q}$-Cartier divisor with $-D$ $\varphi$-ample and $D^+$ $\varphi^+$-ample: the quantity that increases is $\operatorname{mult}_E$ of the pullback of $D$, compared with that of $D^+$.
6. (C) Prove part 2 of Lemma 8.4.2 for an $\mathbb{R}$-divisor $\Delta$ with the negativity lemma, Theorem 1.5.22, applied to $q \colon W \to X^+$ and the divisor $B$: show that $-B$ is $q$-nef and that $q_* B = 0$.

### Lean

The library has `MinimalModel.IsFlip` for a flip between two pair models and `MinimalModel.DiscrepancyCompare` for the comparison of log discrepancies along a birational map. Lemma 8.4.2, Proposition 8.4.3 and Corollary 8.4.4 are not yet in Lean.

### Notes and history

Lemma 8.4.2 is KM98, Lemma 3.38, where it is proved with the negativity lemma; the proof here with linear systems over an affine base is the argument behind the uniqueness of flips and works for $\mathbb{Q}$-divisors. For $\mathbb{R}$-divisors the negativity lemma gives part 2 in the same way as in the proof of Proposition 8.4.3, and part 3 follows from the strong form of the negativity lemma, KM98, Lemma 3.39. The comparison of discrepancies is the reason why flips are the right surgery: the singularities do not get worse, and they get strictly better over the flipped locus. Volume 3, Example 3.6.5, computes the same increase on the toric side for every divisor at once.
