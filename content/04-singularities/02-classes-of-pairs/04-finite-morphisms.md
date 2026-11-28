---
title: Finite morphisms and quotient singularities
nodes: []
sources: [KM98, Kol13, Che55, Rei87]
reads_with: [KM98:ch5, Kol13:ch2]
requires: [P8.9, 4.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Finite morphisms and quotient singularities

### Statement

A finite morphism changes discrepancies in a simple way: the log discrepancy multiplies by the ramification index. This section proves it and deduces that the quotient of a smooth variety by a finite group is klt. The cones of Section 2.3 that are quotients, $\frac1n(1,1)$ and $\frac12(1,1,1)$, give the same numbers by this method.

Let $g \colon X' \to X$ be a finite surjective morphism of normal varieties. Since $k$ has characteristic 0, the extension $k(X) \subset k(X')$ is finite and separable. For a prime divisor $D'$ of $X'$ with image $D = g(D')$, the *ramification index* $e_{D'}$ is the integer with $v_{D'}(t) = e_{D'}$, where $t$ is a uniformizer of the discrete valuation ring $\mathcal{O}_{X,D}$. Only finitely many $D'$ have $e_{D'} > 1$. For an $\mathbb{R}$-divisor $B = \sum_D b_D D$ on $X$, put $g^* B = \sum_{D'} e_{D'} b_{g(D')} D'$. This is the pullback on the smooth locus, extended over a closed set of codimension at least 2, and it agrees with the pullback of Lemma 4.1.2 when $B$ is $\mathbb{R}$-Cartier. The *ramification divisor* is $R = \sum_{D'} (e_{D'} - 1) D'$.

**Lemma 4.2.28 (the Hurwitz formula).** Let $K_X = \operatorname{div}_X(\omega)$ and $K_{X'} = \operatorname{div}_{X'}(g^* \omega)$. Then $K_{X'} = g^* K_X + R$. So for an $\mathbb{R}$-divisor $\Delta$ on $X$ and
$$\Delta' = g^* \Delta - R,$$
the equality $K_{X'} + \Delta' = g^*(K_X + \Delta)$ holds. If $K_X + \Delta$ is $\mathbb{R}$-Cartier, then $(X', \Delta')$ is a sub-pair. It is a pair if and only if $g^*\Delta \ge R$.

Lean: not yet in Lean.

**Theorem 4.2.29 (log discrepancies under a finite morphism).** Let $(X, \Delta)$ be a sub-pair and $\Delta' = g^*\Delta - R$.

1. For each divisor $E'$ over $X'$, the restriction of $v_{E'}$ to $k(X)$ is $e \cdot v_E$ for a divisor $E$ over $X$ and an integer $e \ge 1$, and every divisor $E$ over $X$ arises in this way. The divisor $E'$ is exceptional over $X'$ if and only if $E$ is exceptional over $X$.
2. In this situation
$$A(E', X', \Delta') = e \cdot A(E, X, \Delta).$$
3. $(X, \Delta)$ is sub-klt if and only if $(X', \Delta')$ is sub-klt, and sub-lc if and only if $(X', \Delta')$ is sub-lc.
4. If $(X, \Delta)$ is sub-canonical, so is $(X', \Delta')$, and if it is sub-terminal, so is $(X', \Delta')$. The converse of part 4 is false.

Lean: not yet in Lean.

This is the form of KM98, Chapter 5, with the log discrepancy $A = a + 1$ of Volume 0, Chapter 3. With $a$ it reads $a' + 1 = e(a + 1)$.

**Theorem 4.2.30 (quotient singularities are klt).** Let $G$ be a finite group acting on a smooth variety $M$, with $X = M/G$ a variety, for instance $M$ quasi-projective, and let $g \colon M \to X$ be the quotient. Then $X$ is $\mathbb{Q}$-factorial and klt. In particular $\mathbb{A}^n / G$ is $\mathbb{Q}$-factorial and klt for every finite $G \subset GL_n(k)$.

Lean: not yet in Lean.

A *pseudo-reflection* is an element of $GL_n(k)$ of finite order that fixes a hyperplane pointwise. The ramification divisor of $\mathbb{A}^n \to \mathbb{A}^n/G$ is supported on the hyperplanes of the pseudo-reflections of $G$. By the theorem of Chevalley, Shephard and Todd (Che55), the quotient by the subgroup $H$ that the pseudo-reflections generate is again $\mathbb{A}^n$, and $\mathbb{A}^n / G = \mathbb{A}^n / (G/H)$, where $G/H$ acts linearly on $\mathbb{A}^n/H \cong \mathbb{A}^n$ with no pseudo-reflections. So for the study of quotient singularities one may assume that $G$ has no pseudo-reflections, that is $g$ is étale in codimension 1 and $R = 0$. This section does not use that theorem.

### Proof in words

At a general point of $E'$, choose a local equation $s$ of $E'$ and $t$ of $E$. Then $t = s^e u$ with $u$ a unit, and the other coordinates of $E$ pull back to coordinates of $E'$, because $E' \to E$ is generically étale. So $dt$ pulls back to $s^{e-1}$ times a unit times $ds$, and a rational top form picks up $e - 1$ in its order along $E'$, on top of $e$ times its order along $E$. Add 1 on both sides: log discrepancies multiply by $e$. The classes klt and lc are conditions $A > 0$ and $A \ge 0$, and a positive factor $e$ does not change them, in either direction. For a quotient, a Weil divisor on $M/G$ pulls back to a divisor that is Cartier on $M$, and the norm of a local equation is a local equation of $|G|$ times the divisor downstairs. And the pair $(M, -R)$ upstairs has $A \ge 1$ everywhere, since $M$ is smooth and $-R \le 0$.

### Examples

**Example 4.2.31 (the quotient $\frac13(1,1)$ by its cover).** Let $\mu_3$ act on $\mathbb{A}^2$ by $\zeta \cdot (x, y) = (\zeta x, \zeta y)$, and $X = \mathbb{A}^2 / \mu_3 = \frac13(1,1)$. The action is free outside the origin, so $R = 0$ and $\Delta' = 0$. Let $E'$ be the exceptional curve of the blow-up of the origin, with $A(E', \mathbb{A}^2, 0) = 2$. The action lifts to the blow-up. In the chart $x = u$, $y = uv$ it is $(u, v) \mapsto (\zeta u, v)$, so it fixes $E' = \{u = 0\}$ pointwise, and the invariants $u^3$ and $v$ show that $e = 3$. The quotient of the blow-up is the minimal resolution of $X$, with exceptional curve $E$. So
$$A(E, X, 0) = \frac{2}{3}, \qquad a(E, X, 0) = -\frac13,$$
as for the cone over the twisted cubic in Example 4.2.24. The same argument for $\mu_n$ gives $A = \frac2n$ and $a = -\frac{n-2}{n}$.

**Example 4.2.32 (the quotient $\frac12(1,1,1)$ by its cover).** Let $-1$ act on $\mathbb{A}^3$. The blow-up of the origin has $A(E') = 3$, and the action fixes $E' \cong \mathbb{P}^2$ with $e = 2$. So $A(E, X, 0) = \frac32$ and $a = \frac12$, as in Example 4.2.25. For $\mu_n$ acting on $\mathbb{A}^N$ by scalars, $A = \frac{N}{n}$.

**Counterexample 4.2.33 (terminal does not go down).** In the example of $\frac13(1,1)$, the cover $(\mathbb{A}^2, 0)$ is terminal and the quotient is not even canonical. Part 4 holds, since it goes up only: the quotient has $A = \frac23 < 1$, and the cover has $A = 3 \cdot \frac23 = 2$.

**Example 4.2.34 (a reflection and the boundary).** Let $\mu_2$ act on $\mathbb{A}^2$ by $(x, y) \mapsto (-x, y)$, a reflection. The quotient is $\mathbb{A}^2$ with coordinates $(x^2, y)$, and the map $g$ is ramified along $D' = \{x = 0\}$ with $e = 2$, so $R = D'$. Let $D = \{x^2 = 0\}$ be the branch line downstairs. For $\Delta = cD$, $g^* \Delta = 2c D'$ and $\Delta' = (2c - 1) D'$. So $(\mathbb{A}^2, \frac12 D)$ on the base corresponds to $(\mathbb{A}^2, 0)$ on the cover, and $(\mathbb{A}^2, 0)$ on the base corresponds to the sub-pair $(\mathbb{A}^2, -D')$. This is why the theorem is stated for sub-pairs, and why the boundary $\frac12 D$ appears in the study of double covers. Check part 2 on the divisor $D'$ itself: $A(D', \mathbb{A}^2, (2c-1)D') = 2 - 2c = 2(1 - c) = 2 A(D, \mathbb{A}^2, cD)$.

### Proof

*The Hurwitz formula and part 2.* Both are one local computation. Let $E$ be a prime divisor on a normal model $Y$ of $X$, let $Y'$ be the normalization of $Y$ in $k(X')$, and let $E'$ be a prime divisor of $Y'$ over $E$, with ramification index $e$. At a general point of $E$, the variety $Y$ is smooth and there are local coordinates $t, y_2, \dots, y_n$ with $E = \{t = 0\}$. The morphism $E' \to E$ is finite and generically étale, since $k$ has characteristic 0. So at a general point of $E'$, the pullbacks of $y_2, \dots, y_n$ restrict to local coordinates of $E'$, and with a local equation $s$ of $E'$ they form local coordinates $s, y_2, \dots, y_n$ of $Y'$. Write $t = s^e u$ with $u$ a unit. Then
$$dt \wedge dy_2 \wedge \dots \wedge dy_n = s^{e-1} \Big( e u + s \frac{\partial u}{\partial s} \Big) \, ds \wedge dy_2 \wedge \dots \wedge dy_n,$$
and $eu + s \frac{\partial u}{\partial s}$ is a unit, because $e \ne 0$ in $k$. For a rational top form $\eta = h \, dt \wedge dy_2 \wedge \dots \wedge dy_n$ on $Y$, $\operatorname{ord}_{E'}(g^* h) = e \operatorname{ord}_E(h)$. So
$$\operatorname{ord}_{E'}(g^* \eta) = e \operatorname{ord}_E(\eta) + e - 1.$$
With $Y = X$ and $E = D$, this is the Hurwitz formula: the coefficient of $D'$ in $\operatorname{div}(g^* \omega)$ is $e_{D'} \operatorname{ord}_D(\omega) + e_{D'} - 1$. Then $K_{X'} + \Delta' = g^* K_X + R + g^* \Delta - R = g^*(K_X + \Delta)$.

For part 2, choose $U$ and $h_i$ with $(K_X + \Delta)|_U = \sum_i r_i \operatorname{div}_U(h_i)$, as in Theorem 4.1.12. Then $(K_{X'} + \Delta')|_{g^{-1}U} = \sum_i r_i \operatorname{div}(g^* h_i)$, and $v_{E'}(g^* h_i) = e \, v_E(h_i)$. The same theorem, applied on $X'$ with the form $g^*\omega$, gives
$$A(E', X', \Delta') = 1 + e \operatorname{ord}_E(\omega) + e - 1 - e \sum_i r_i v_E(h_i) = e \, A(E, X, \Delta).$$

*Part 1.* Let $E$ be a divisor over $X$ on a model $Y$, and $Y'$ the normalization of $Y$ in $k(X')$. Then $Y' \to Y$ is finite and surjective, and $Y' \to X'$ is proper and birational, since $Y' \to X$ is proper and both have the function field $k(X')$. Since $Y' \to Y$ is finite and surjective, some prime divisor $E'$ of $Y'$ maps onto $E$, and it is a divisor over $X'$ over $E$. Conversely, let $E'$ be a divisor over $X'$. The restriction of $v_{E'}$ to $k(X)$ is a discrete valuation, nontrivial because $k(X')$ is algebraic over $k(X)$, with value group $e \mathbb{Z}$ for some $e \ge 1$. Its residue field is a subfield of the residue field of $v_{E'}$ over which that field is algebraic, so it also has transcendence degree $n - 1$. The centre of $v_{E'}$ on $X'$ maps to a centre on $X$. By Zariski's theorem of Section 1.2, $\frac1e v_{E'}|_{k(X)} = v_E$ for a divisor $E$ over $X$, and $E'$ appears on the normalization $Y'$ above. Finally, $g$ is finite, so $g(c_{X'}(E')) = c_X(E)$ and both centres have the same dimension. So $E'$ is exceptional if and only if $E$ is.

*Parts 3 and 4.* Sub-klt is the condition $A > 0$ for every divisor over the variety, and sub-lc is $A \ge 0$. By parts 1 and 2 the values of $A$ over $X'$ are the values over $X$, each multiplied by a positive integer, and every divisor over $X$ gives at least one over $X'$. So each condition holds on $X$ if and only if it holds on $X'$. For part 4, sub-canonical is $A \ge 1$ for every exceptional divisor. If $A(E) \ge 1$, then $A(E') = eA(E) \ge A(E) \ge 1$, and the same with strict inequalities for sub-terminal. The counterexample above shows that the converse fails.

*Quotients.* Let $D$ be a prime divisor on $X = M/G$. Its pullback $g^*D$ is a $G$-invariant Weil divisor on the smooth $M$, so $\mathcal{O}_M(g^*D)$ is a line bundle. Let $x \in X$. The fibre $g^{-1}(x)$ is finite, and a line bundle on the semi-local ring of a finite set of points is trivial, since the Picard group of a semi-local ring is trivial. So $\mathcal{O}_M(g^*D)$ is trivial on an open set $W$ that contains the fibre. Since $g$ is finite, it is closed, and $U = X \setminus g(M \setminus W)$ is an open neighbourhood of $x$ with $g^{-1}U \subset W$. So $g^*D|_{g^{-1}U} = \operatorname{div}(h)$ for some $h \in k(M)^*$. The norm $N(h) = \prod_{\sigma \in G} \sigma^* h$ is $G$-invariant, so it lies in $k(M)^G = k(X)$, and
$$g^* \operatorname{div}_U(N(h)) = \operatorname{div}(N(h)) = \sum_{\sigma \in G} \sigma^* g^* D = |G| \, g^* D.$$
Since $g^*$ is injective on divisors, $\operatorname{div}_U(N(h)) = |G| D$. So $|G| D$ is Cartier, and $X$ is $\mathbb{Q}$-factorial. In particular $K_X$ is $\mathbb{Q}$-Cartier, and $(X, 0)$ is a pair. Its cover is the sub-pair $(M, -R)$ by the Hurwitz formula. For a divisor $E'$ over $M$, Exercise 3 of Section 1.2 gives $A(E', M, -R) = A(E', M, 0) + v_{E'}(R) \ge A(E', M, 0)$. The smooth $M$ has $A(E', M, 0) = 1$ for prime divisors of $M$, and $A(E', M, 0) \ge 2$ for exceptional ones, by Theorem 4.2.12 when $\dim M \ge 2$. So $(M, -R)$ is sub-klt, and by part 3 $X$ is klt. $\square$

### Exercises

1. (A) Let $X = \frac14(1,1)$. Compute $a(E, X, 0)$ by the cover $\mathbb{A}^2 \to X$ and by the cone $C(\mathbb{P}^1, \mathcal{O}(4))$, and check that they agree.
2. (A) Let $X' = \{z^2 = xy\}$ and $g \colon X' \to \mathbb{A}^2$ the projection to $(x, y)$, a double cover branched along $B = \{xy = 0\}$. Show that $R = \{z = 0\}$ and that $\Delta' = 0$ for $\Delta = \frac12 B$. Deduce that the $A_1$ singularity is klt and canonical from the snc pair $(\mathbb{A}^2, \frac12 B)$.
3. (B) Let $X' = \{z^2 = y^2 - x^3\}$, a double cover of $\mathbb{A}^2$ branched along the cusp $C = \{y^2 = x^3\}$. Show that $X'$ is the $A_2$ singularity $\{uv = x^3\}$ after a change of coordinates. Use Exercise 2 of Section 2.2 to show that $X'$ is canonical.
4. (B) Let $X' = \{z^3 = x^3 + y^3\}$ and $g$ the projection to $(x, y)$, a triple cover branched along three concurrent lines $B$. Show that $\Delta' = 0$ for $\Delta = \frac23 B$, and deduce from Exercise 1 of Section 2.2 that the cone over a plane cubic is lc and not klt.
5. (B) In the same way, use the cover $\{z^4 = x^4 + y^4\} \to \mathbb{A}^2$ and the pair $(\mathbb{A}^2, \frac34 B)$, with $B$ four concurrent lines, to show that the cone over a plane quartic is not lc.
6. (C) Let $G$ act on a normal variety $X'$ with quotient $g \colon X' \to X$, and let $\Delta$ be an $\mathbb{R}$-divisor on $X$ with $\Delta' = g^*\Delta - R$. Show by the norm argument that if $K_{X'} + \Delta'$ is $\mathbb{Q}$-Cartier and $\Delta$ is a $\mathbb{Q}$-divisor, then $K_X + \Delta$ is $\mathbb{Q}$-Cartier. Deduce that in parts 3 and 4 of the theorem, for a Galois cover, the hypothesis that $K_X + \Delta$ is $\mathbb{R}$-Cartier can be checked upstairs.

### Lean

The theorems of this section are not yet in Lean. The library has no finite morphisms between the varieties of `MinimalModel.Pair` and no group actions. `MinimalModel.IsQFactorial` can state the first half of the theorem on quotients.

### Notes and history

The formula $A' = eA$ is the basic tool for covering tricks, and KM98, Chapter 5, uses it to compare a pair with its index one cover and with cyclic covers. KM98, Chapter 5, proves that quotient singularities are klt by the argument of this section. Quotients by groups generated by pseudo-reflections are again smooth by Chevalley's theorem (Che55) and the work of Shephard and Todd, and the sub-pair $(M, -R)$ is the way to include them without that theorem. Section 3.3 proves a converse in dimension 2: every klt surface germ is a quotient singularity. In dimension 3 and higher the converse fails, and terminal 3-fold singularities that are not quotients are the subject of Chapter 4.
