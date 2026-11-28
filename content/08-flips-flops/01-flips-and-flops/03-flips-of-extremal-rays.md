---
title: Flips of extremal rays and discrepancies
nodes: []
sources: [KM98, Cor07, Kol92]
reads_with: [KM98:3.7, Cor07:2]
requires: [1.1, 1.5, 4.1, 4.2, P7.1, P7.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Flips of extremal rays and discrepancies

### Statement

In this section $(X, \Delta)$ is a pair with $K_X + \Delta$ $\mathbb{Q}$-Cartier, $f \colon X \to Z$ is a flipping contraction of $(X, \Delta)$ (Definition 8.1.1) and $f^+ \colon X^+ \to Z$ is its flip, with $\Delta^+ = f^{+\,-1}_* f_* \Delta$. Discrepancies $a(E, X, \Delta)$ of divisors $E$ over $X$ are as in Volume 4 (Definition 4.1.11), and the classes terminal, canonical, klt, plt and lc are those of Definition 4.2.1. Since $X \dashrightarrow X^+$ is an isomorphism in codimension $1$, a divisor over $X$ is a divisor over $X^+$, it is exceptional over $X$ if and only if it is exceptional over $X^+$, and the non-exceptional ones have the same coefficients in $\Delta$ and in $\Delta^+$.

**Proposition 8.1.17 (the flip of an extremal ray).** Let $(X, \Delta)$ be a projective $\mathbb{Q}$-factorial klt pair, $R$ a $(K_X + \Delta)$-negative extremal ray and $f = \varphi_R \colon X \to Z$ its contraction (Theorem 1.1.12), and suppose that $f$ is small and that the flip $f^+ \colon X^+ \to Z$ exists. Let $D = K_X + \Delta$.

1. Every $\mathbb{Q}$-Cartier divisor $B$ on $X$ satisfies $B \sim_{\mathbb{Q}} cD + f^* L$ for a rational number $c$ and a $\mathbb{Q}$-Cartier divisor $L$ on $Z$, and then $B^+ \sim_{\mathbb{Q}} cD^+ + f^{+*} L$ on $X^+$.
2. $X^+$ is projective and $\mathbb{Q}$-factorial, $\rho(X^+/Z) = 1$ and $\rho(X^+) = \rho(X)$.
3. For every $\mathbb{Q}$-Cartier $\mathbb{Q}$-divisor $D'$ on $X$ with $-D'$ ample over $Z$, the $D'$-flip exists and is $X^+$.

Lean: not yet in Lean.

**Lemma 8.1.18 (the exceptional loci).** In the situation of the section, let $S = f(\operatorname{Exc}(f))$. Then $f^+(\operatorname{Exc}(f^+)) = S$, both $f$ and $f^+$ are isomorphisms over $Z \setminus S$, and $\operatorname{Exc}(f) = f^{-1}(S)$, $\operatorname{Exc}(f^+) = f^{+\,-1}(S)$.

Lean: not yet in Lean.

**Lemma 8.1.19 (discrepancies go up under a flip).** In the situation of the section, let $E$ be a divisor over $X$. Then
$$a(E, X, \Delta) \le a(E, X^+, \Delta^+),$$
and the inequality is strict if the centre of $E$ on $X$ lies in $\operatorname{Exc}(f)$, or equivalently if the centre of $E$ on $X^+$ lies in $\operatorname{Exc}(f^+)$. If the centre of $E$ on $X$ is not contained in $\operatorname{Exc}(f)$, the two discrepancies are equal.

Lean: not yet in Lean.

**Corollary 8.1.20 (flips preserve the singularities).** If $(X, \Delta)$ is terminal, canonical, klt, plt or lc, then so is $(X^+, \Delta^+)$. If $(X, \Delta)$ is terminal, every divisor $E$ with centre on $X^+$ in $\operatorname{Exc}(f^+)$ has $a(E, X^+, \Delta^+) > a(E, X, \Delta) > 0$.

Lean: not yet in Lean.

So a sequence of flips of projective $\mathbb{Q}$-factorial klt pairs stays in this class, with the Picard number unchanged, and the discrepancy of every fixed divisor can only increase. Chapter 4 builds the termination of 3-fold flips on this monotonicity.

### Proof in words

For the extremal ray, the contraction theorem says that a divisor which is zero on the ray is a pullback from $Z$. So every divisor on $X$ is a multiple of the flipping divisor up to pullbacks, and the same relation passes to $X^+$ by strict transform. This gives $\mathbb{Q}$-factoriality, the Picard numbers and the independence of the divisor at once.

For the discrepancies, compare the pullbacks of $K_X + \Delta$ and $K_{X^+} + \Delta^+$ to a common resolution $W$. Their difference $F$ pushes forward to $0$ on $X$, and $-F$ is nef over $X$, because $K_{X^+} + \Delta^+$ is ample over $Z$. The negativity lemma gives $F \ge 0$, which is the inequality. A flipping curve on $X$ lifts to a curve on $W$ on which $F$ is negative, so $F$ cannot vanish near the fibre of $W \to Z$ through it, and the dichotomy in the negativity lemma then puts the whole fibre in the support of $F$.

### Examples

**Example 8.1.21 (discrepancies across a flop).** Let $(X, \Delta)$ be a projective $\mathbb{Q}$-factorial klt pair, $f \colon X \to Z$ the small contraction of an extremal ray $R$ with $(K_X + \Delta) \cdot R = 0$, and $X^+$ a $D$-flop. By Theorem 1.1.12, $r(K_X + \Delta) \sim f^* L$ for some $r \ge 1$ and a Cartier divisor $L$ on $Z$, so $r(K_{X^+} + \Delta^+) \sim f^{+*} L$ by the strict transform argument of part 1 of Proposition 8.1.17. On a common resolution as in the proof of Lemma 8.1.19, $F = p^*(K_X + \Delta) - q^*(K_{X^+} + \Delta^+)$ is then numerically trivial over $Z$ and $p_* F = 0$, so $F \ge 0$ and $-F \ge 0$ by Theorem 1.5.22 applied to $F$ and to $-F$. Hence $F = 0$ and $a(E, X, \Delta) = a(E, X^+, \Delta^+)$ for every $E$. For the Atiyah flop of Proposition 8.1.11, the divisor $E$ over $C_1$ has discrepancy $1$ over both $X_1$ and $X_2$, being the exceptional divisor of the blow-up of a smooth curve on each side.

**Example 8.1.22 (the Francia flip).** In the Francia flip of Proposition 8.1.13 the divisor $F = D_v$ has centre the $\frac12(1,1,1)$ point on $X^-$, which lies on $C^-$, and centre $C^+$ on $X^+$. By Example 8.1.16, $a(F, X^-) = \frac12 < 1 = a(F, X^+)$, as Lemma 8.1.19 requires. A divisor whose centre on $X^-$ is not contained in $C^-$, such as the exceptional divisor of the blow-up of a general point of $X^-$, has discrepancy $2$ on both sides, as the last statement of Lemma 8.1.19 says.

**Example 8.1.23 (antiflips make the singularities worse).** The inverse $X^+ \dashrightarrow X^-$ of the Francia flip is the $(-K_{X^+})$-flip of $f^+$, the flip of a $K$-positive small contraction, called an *antiflip*. For it the inequality reverses: $a(F, X^+) = 1 > \frac12 = a(F, X^-)$, and the smooth $X^+$ becomes the singular $X^-$. So the sign of $K \cdot C$ is what makes the singularities improve.

### Proof

*Proposition 8.1.17.* Fix a curve $C$ with $[C] \in R$, so that $D \cdot C < 0$.

Part 1. Let $B$ be a $\mathbb{Q}$-Cartier divisor on $X$ and $c = (B \cdot C)/(D \cdot C) \in \mathbb{Q}$. Then $(B - cD) \cdot R = 0$, and for $r \ge 1$ with $r(B - cD)$ Cartier, Theorem 1.1.12 gives a Cartier divisor $L'$ on $Z$ with $r(B - cD) \sim f^* L'$; put $L = \frac1r L'$. For the second statement, write $r(B - cD) - f^* L' = \operatorname{div} \psi$. Push forward by $f$ and take the strict transform by $f^+$. Both operations commute with $\operatorname{div} \psi$, since $f$ and $f^+$ are small, and they take $f^* L'$ to $f^{+*} L'$, since $f^{+*} L' - f^{+\,-1}_* f_* f^* L'$ is an $f^+$-exceptional divisor and so $0$. So $rB^+ - rcD^+ - f^{+*} L' = \operatorname{div} \psi$ on $X^+$.

Part 2. Every Weil divisor on $X^+$ is $B^+$ for its strict transform $B$ on $X$, which is $\mathbb{Q}$-Cartier since $X$ is $\mathbb{Q}$-factorial. By part 1, $B^+ \sim_{\mathbb{Q}} cD^+ + f^{+*} L$ with $D^+ = K_{X^+} + \Delta^+$ $\mathbb{Q}$-Cartier, so $B^+$ is $\mathbb{Q}$-Cartier and $X^+$ is $\mathbb{Q}$-factorial. The variety $Z$ is projective, as the image of a projective variety, and $f^+$ is projective, so $X^+$ is projective.

For the Picard numbers, first $f^* \colon N^1(Z) \to N^1(X)$ is injective: if $f^* M \equiv 0$ for a Cartier divisor $M$ on $Z$ and $\gamma \subset Z$ is a curve, Lemma P7.2.6 gives a curve $\tilde\gamma \subset X$ with $f_* \tilde\gamma = d \gamma$ for some $d \ge 1$, and the projection formula (Theorem P7.1.15) gives $d \, M \cdot \gamma = f^* M \cdot \tilde\gamma = 0$. By part 1, $N^1(X) = f^* N^1(Z) + \mathbb{R}[D]$, and $[D] \notin f^* N^1(Z)$ since $D \cdot C < 0$ while pullbacks are zero on $C$. So $\rho(X) = \rho(Z) + 1$. The curves contracted by $f^+$ exist: otherwise $f^+$ would be finite and birational onto the normal $Z$, hence an isomorphism, so $f_* D = f^+_* D^+$ would be $\mathbb{Q}$-Cartier on $Z$ and $D = f^* f_* D$ by Lemma 8.1.4, contradicting $D \cdot C < 0$. The same argument on $X^+$, with $D^+$ positive on the curves contracted by $f^+$ and with part 1 for $X^+$, gives $\rho(X^+) = \rho(Z) + 1$ and $\rho(X^+/Z) = 1$.

Part 3. Let $D'$ be $\mathbb{Q}$-Cartier with $-D'$ ample over $Z$. By part 1, $D' \sim_{\mathbb{Q}} cD + f^* L$ with $c = (D' \cdot C)/(D \cdot C) > 0$. By part 2 of Corollary 8.1.7, the $D'$-flip exists and is $X^+$.

*Lemma 8.1.18.* Since $f$ is a projective birational morphism onto a normal variety, $f$ is an isomorphism over $Z \setminus S$ and $\operatorname{Exc}(f) = f^{-1}(S)$ (Proposition 1.5.6). Over $Z \setminus S$ the divisor $D_Z = f_* D$ is $\mathbb{Q}$-Cartier, so its strict transform $D^+$ on $f^{+\,-1}(Z \setminus S)$ is $f^{+*} D_Z$, as $f^+$ is small. It is numerically trivial on curves contracted by $f^+$ and ample over $Z$, so there are no such curves over $Z \setminus S$, and $f^+$ is finite and birational over $Z \setminus S$, hence an isomorphism there by Zariski's main theorem. So $S^+ = f^+(\operatorname{Exc}(f^+)) \subseteq S$. The same argument with the roles of $f$ and $f^+$ exchanged, using that $X$ is the $(-D^+)$-flip of $f^+$ (Example 8.1.8), gives $S \subseteq S^+$.

*Lemma 8.1.19.* Let $W$ be a smooth variety with projective birational morphisms $p \colon W \to X$ and $q \colon W \to X^+$ with $f \circ p = f^+ \circ q = g$, on which $E$ is a divisor: take a resolution of the closure of the graph of $X \dashrightarrow X^+$ and blow up further until the centre of $E$ is a divisor (Theorem 4.2.10). Choose $K_W$ and set $K_X = p_* K_W$ and $K_{X^+} = q_* K_W$, which are strict transforms of each other. Write
$$K_W = p^*(K_X + \Delta) + \sum_E a(E, X, \Delta) E = q^*(K_{X^+} + \Delta^+) + \sum_E a(E, X^+, \Delta^+) E,$$
the sums over the prime divisors of $W$, with $a$ equal to minus the coefficient of the boundary for non-exceptional divisors. Let
$$F = p^*(K_X + \Delta) - q^*(K_{X^+} + \Delta^+) = \sum_E \big(a(E, X^+, \Delta^+) - a(E, X, \Delta)\big) E.$$
The divisors that are not $p$-exceptional are the strict transforms of divisors on $X$, which are not $q$-exceptional either, and have the same coefficient in $\Delta$ and $\Delta^+$; so $p_* F = 0$. For a curve $\gamma \subset W$ contracted by $p$, the curve $q(\gamma)$ is a point or a curve contracted by $f^+$, since $f^+(q(\gamma)) = f(p(\gamma))$ is a point. As $K_{X^+} + \Delta^+$ is ample over $Z$, $q^*(K_{X^+} + \Delta^+) \cdot \gamma \ge 0$, while $p^*(K_X + \Delta) \cdot \gamma = 0$. So $F \cdot \gamma \le 0$ and $-F$ is $p$-nef. By the negativity lemma (Theorem 1.5.22), $F \ge 0$. This is the inequality.

The same computation for curves $\gamma$ contracted by $g$ gives $F \cdot \gamma = (K_X + \Delta) \cdot p_* \gamma - (K_{X^+} + \Delta^+) \cdot q_* \gamma \le 0$, since $-(K_X + \Delta)$ and $K_{X^+} + \Delta^+$ are both ample over $Z$. So $-F$ is $g$-nef and $g_* F = 0$. By the dichotomy in the negativity lemma (KM98, Lemma 3.39), for every $z \in Z$ either $g^{-1}(z) \subseteq \operatorname{Supp} F$ or $g^{-1}(z) \cap \operatorname{Supp} F = \emptyset$.

Let $z \in S$. There is a curve $C \subseteq f^{-1}(z) \subseteq \operatorname{Exc}(f)$, as the fibre is positive dimensional. By Lemma P7.2.6 there is a curve $\gamma \subset g^{-1}(z)$ with $p_* \gamma = dC$ for some $d \ge 1$. Then $F \cdot \gamma = d (K_X + \Delta) \cdot C - (K_{X^+} + \Delta^+) \cdot q_* \gamma < 0$, since the first term is negative and the second is at least $0$. If $\operatorname{Supp} F$ were disjoint from $g^{-1}(z)$, $F \cdot \gamma$ would be $0$. So $g^{-1}(z) \subseteq \operatorname{Supp} F$ for every $z \in S$, that is $g^{-1}(S) \subseteq \operatorname{Supp} F$.

Now let the centre $p(E)$ of $E$ lie in $\operatorname{Exc}(f) = f^{-1}(S)$. Then $E \subseteq g^{-1}(S) \subseteq \operatorname{Supp} F$, so $E$ is a component of $F$ and $a(E, X^+, \Delta^+) - a(E, X, \Delta) = \operatorname{mult}_E F > 0$. By Lemma 8.1.18, $p(E) \subseteq f^{-1}(S)$ if and only if $g(E) \subseteq S$ if and only if $q(E) \subseteq f^{+\,-1}(S) = \operatorname{Exc}(f^+)$, which is the equivalence of the two conditions. If $p(E) \not\subseteq \operatorname{Exc}(f)$, the generic point of $E$ maps to $Z \setminus S$, over which $X$ and $X^+$ are both identified with $Z$ by Lemma 8.1.18, so $p^*(K_X + \Delta)$ and $q^*(K_{X^+} + \Delta^+)$ agree near the generic point of $E$ and $\operatorname{mult}_E F = 0$. This argument is KM98, Lemma 3.38, in the form of Cor07, Chapter 2.

*Corollary 8.1.20.* The classes of Definition 4.2.1 are defined by lower bounds on $a(E, X, \Delta)$ for exceptional $E$, together with conditions on the coefficients of $\Delta$, which are minus the discrepancies of the non-exceptional divisors. A divisor is exceptional over $X^+$ if and only if it is exceptional over $X$, Lemma 8.1.19 shows that each discrepancy over $X^+$ is at least the corresponding one over $X$, and the coefficients of $\Delta^+$ are those of $\Delta$. So every lower bound satisfied over $X$ is satisfied over $X^+$. The last statement is the strict inequality of Lemma 8.1.19.

### Exercises

1. (A) In Example 8.1.22, compute the discrepancy over $X^-$ and over $X^+$ of the exceptional divisor of the blow-up of the smooth torus fixed point $V(\operatorname{Cone}(u_1, u_2, u_4))$ of $X^-$, and check Lemma 8.1.19.
2. (A) For the family of Example 8.1.14, compute $a(D_v, X^-)$ and $a(D_v, X^+)$ for $v = u_3 + u_4$, and show that the gap is $\frac{n-1}{n}$.
3. (A) In the Atiyah flop of Proposition 8.1.11, compute $F = p^* K_{X_1} - q^* K_{X_2}$ on the common blow-up $Y$ of part 4 directly, and check that $F = 0$.
4. (B) Show by an example on the Francia flip that the discrepancy of a divisor whose centre on $X^+$ meets $\operatorname{Exc}(f^+)$ without being contained in it can stay the same: take the blow-up of a torus invariant curve $V(\operatorname{Cone}(u_1, u_3))$ of $X^+$, which meets $C^+$ in one point.
5. (B) Let $X$ be a $\mathbb{Q}$-factorial 3-fold with terminal singularities and $f$ an extremal flipping contraction with flip $X^+$. Using Corollary 8.1.20 and Theorem 4.4.15, show that $X^+$ has isolated singularities and that the singular points of $X^+$ lie on the flipped curves or away from $\operatorname{Exc}(f^+)$ with the same analytic type as on $X$.
6. (C) Prove that for the flip of an extremal ray of a projective $\mathbb{Q}$-factorial klt pair the contraction $f^+$ is the contraction of a $(K_{X^+} + \Delta^+)$-positive extremal ray of $\overline{NE}(X^+)$, using part 2 of Proposition 8.1.17.

### Lean

The library has `MinimalModel.IsFlip` and `MinimalModel.KltFlips`; the preservation of singularities and Lemma 8.1.19 are not yet in Lean.

### Notes and history

The monotonicity of discrepancies under flips is KM98, Lemma 3.38; it is the input to Shokurov's difficulty function and to the termination arguments of Shokurov (Sho85) and Kawamata. Proposition 8.1.17 is KM98, Proposition 3.37, in the form used to run the program: the class of projective $\mathbb{Q}$-factorial klt pairs is stable under flips of extremal rays. The antiflip of Example 8.1.23 shows that the direction of a flip matters.
