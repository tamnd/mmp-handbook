---
title: The toric cone theorem
nodes: []
sources: [CLS11, Ful93, FS04]
reads_with: [CLS11:ch6, Ful93:5.1]
requires: [P5.5, P5.12, 3.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The toric cone theorem

### Statement

Let $\Sigma$ be a complete simplicial fan in $N_\mathbb{R}$ of dimension $n$, so $X_\Sigma$ is complete and $\mathbb{Q}$-factorial (Theorem P8.6.28 and Corollary P8.7.12). Every Weil divisor is $\mathbb{Q}$-Cartier, so Definition P8.8.11 pairs every $\mathbb{R}$-divisor with every complete curve.

**Definition P8.8.17 (numerical classes and the cone of curves).** Let $Z_1(X_\Sigma)_\mathbb{R}$ be the real vector space of $1$-cycles $\sum c_i C_i$, with $C_i$ integral complete curves. A $1$-cycle $Z$ is *numerically trivial* if $D \cdot Z = 0$ for every Cartier divisor $D$, and $N_1(X_\Sigma)$ is the quotient of $Z_1(X_\Sigma)_\mathbb{R}$ by the numerically trivial cycles. Dually $N^1(X_\Sigma)$ is the space of $\mathbb{R}$-Cartier divisors modulo numerical equivalence. The *cone of curves* $NE(X_\Sigma) \subseteq N_1(X_\Sigma)$ is the convex cone spanned by the classes of integral curves, and $\overline{NE}(X_\Sigma)$ is its closure. An $\mathbb{R}$-Cartier divisor $D$ is *nef* if $D \cdot C \geq 0$ for every integral curve $C$. For surfaces these are the cones of Definition P5.12.1.

**Theorem P8.8.18 (the toric cone theorem).** Let $\Sigma$ be a complete simplicial fan.

1. $NE(X_\Sigma) = \overline{NE}(X_\Sigma) = \sum_{\tau \text{ a wall}} \mathbb{R}_{\geq 0} [V(\tau)]$, a closed rational polyhedral cone.
2. For an $\mathbb{R}$-divisor $D = \sum a_\rho D_\rho$, the following are equivalent: $D$ is nef; $D \cdot V(\tau) \geq 0$ for every wall $\tau$; the support function $\varphi_D$ is convex.
3. A nef Cartier divisor on $X_\Sigma$ is globally generated.
4. If $X_\Sigma$ is projective, a divisor $D$ is ample if and only if $D \cdot V(\tau) > 0$ for every wall $\tau$.

Lean: the equivalence of convexity with nonnegativity on all walls in part 2 is `MinimalModel.Toric.Fan.coneTheorem`, for real divisors on a complete simplicial fan, and `MinimalModel.Toric.toricConeTheorem` proves the pinned statement `ToricConeTheorem`; the geometric statements about curves on $X_\Sigma$ are not in Lean as stated.

The theorem is Theorem 3.4.21 of Volume 3, and Cox, Little and Schenck, Theorem 6.3.20 (with Theorem 6.3.12 for part 2 and Theorem 6.3.12 with Theorem 6.1.7 for part 3); it holds for complete fans that are not simplicial and in a relative form over a proper toric morphism (Fujino and Sato). Here it is proved in full for smooth projective toric surfaces, and part 2 in the combinatorial direction is proved for all complete simplicial fans.

**Proposition P8.8.19 (convexity is local at the walls).** Let $\Sigma$ be complete and simplicial and $\varphi$ a support function of $\Sigma$. Then $\varphi$ is convex if and only if for every wall pair $(\sigma, \sigma')$ the linear function $\langle m_{\sigma'}, \cdot \rangle$ of $\varphi$ on $\sigma'$ satisfies $\langle m_{\sigma'}, u \rangle \geq \varphi(u)$ on $\sigma$.

Lean: `MinimalModel.Toric.Fan.concaveOn_iff_forall_isConvexAcross_of_isSimplicialFan`, with the wall inequality `MinimalModel.Toric.IsConvexAcross` and convexity written as `ConcaveOn`.

### Proof in words

On a surface every curve that is not invariant under the torus is the closure of a curve $f = 0$ in the torus, for an irreducible Laurent polynomial $f$. Dividing $f$ by the character of a vertex of its Newton polygon makes $f$ regular along every invariant divisor, so the divisor of the new function is the curve minus a nonnegative combination of invariant curves. So every curve is linearly equivalent to an effective sum of wall curves, and the wall curves span the cone. Nefness is then positivity on finitely many curves, which by the degree formula of Section 8.2 is the wall inequality for the support function, and the wall inequalities together give convexity because a function that is locally the minimum of linear functions along a line is concave there.

### Examples

**Example P8.8.20 (the Hirzebruch surfaces).** By Example P8.8.14 the wall curves of $F_n$ are $D_1 \equiv D_3 \equiv F$, $D_2 = C_-$ and $D_4 \equiv C_- + nF$. So
$$NE(F_n) = \mathbb{R}_{\geq 0} [F] + \mathbb{R}_{\geq 0} [C_-],$$
since $C_- + nF$ is in the cone spanned by the other two. For $D = aC_- + bF$, $D \cdot F = a$ and $D \cdot C_- = b - na$, so
$$\operatorname{Nef}(F_n) = \{ a \geq 0, \ b \geq na \} = \mathbb{R}_{\geq 0} [F] + \mathbb{R}_{\geq 0} [C_- + nF],$$
in agreement with Example P5.12.8 and with Example P8.7.23. With $K \cdot F = -2$ and $K \cdot C_- = n - 2$ (Example P8.8.14), the ray of $F$ is $K$-negative for every $n$, and its contraction is the ruling $F_n \to \mathbb{P}^1$. The ray of $C_-$ is $K$-negative only for $n \leq 1$: for $n = 1$ it is the contraction $F_1 \to \mathbb{P}^2$ of the $(-1)$-curve, for $n = 0$ it is the second ruling of $\mathbb{P}^1 \times \mathbb{P}^1$, for $n = 2$ it is $K$-trivial, with contraction $F_2 \to \mathbb{P}(1, 1, 2)$ to a quadric cone, and for $n \geq 3$ it is $K$-positive, with contraction $F_n \to \mathbb{P}(1, 1, n)$ of Example P8.8.7.

**Example P8.8.21 (the projective plane).** The fan of $\mathbb{P}^2$ has three walls, the rays, and the relations $e_0 + e_2 = -e_1$ and its rotations give $D_i^2 = 1$ and $D_i \cdot D_j = 1$. So $NE(\mathbb{P}^2) = \mathbb{R}_{\geq 0} [\ell]$ for a line $\ell$, and a divisor $dD_0$ is nef exactly when $d \geq 0$, and globally generated exactly then, by part 3 and Example P8.7.22.

**Example P8.8.22 (the relative cone of the Atiyah flop).** The varieties $X_{\Sigma_\pm}$ of Example P8.8.16 are not complete, but the relative version of the theorem over $U_\sigma$ applies, and is elementary here: the only complete curve of $X_{\Sigma_+}$ is the fibre $C_+$ over the vertex, because a complete curve maps to a point of the affine $U_\sigma$ and $\pi$ is an isomorphism outside the vertex. So the relative cone of curves is $\mathbb{R}_{\geq 0} [C_+]$, it is $K$-trivial, and the divisor $-D_1$, with $-D_1 \cdot C_+ = 1$, is relatively ample, while on $X_{\Sigma_-}$ the divisor $D_1$ is relatively ample. This is the toric picture of a flop, and Volume 3 uses the same computation, with $K$-negative relations, to construct toric flips.

### Proof

*Proposition P8.8.19.* If $\varphi$ is convex, the argument for (4) $\Rightarrow$ (3) in the proof of Theorem P8.7.20 shows $\varphi \leq \langle m_{\sigma'}, \cdot \rangle$ everywhere, in particular on $\sigma$. Conversely assume the wall inequalities. Let $x \in N_\mathbb{R}$ lie in the relative interior of a wall $\tau = \sigma \cap \sigma'$. The cones of $\Sigma$ containing $x$ are $\tau$, $\sigma$ and $\sigma'$, as in Proposition P8.8.10, and they cover a neighbourhood $U$ of $x$, as in the proof of Theorem P8.6.28. By the wall inequality for $(\sigma, \sigma')$ and for $(\sigma', \sigma)$, which are equivalent by Proposition P8.8.12, $\varphi = \min(\langle m_\sigma, \cdot \rangle, \langle m_{\sigma'}, \cdot \rangle)$ on $U$, which is concave on $U$. At interior points of cones of dimension $n$, $\varphi$ is linear nearby. So $\varphi$ is concave near every point of the set $W$ of points lying in no cone of dimension $\leq n - 2$. Let $u, v \in N_\mathbb{R}$. The union of the cones of dimension $\leq n - 2$ has codimension $2$, so the segments $[u', v']$ that meet it form a nowhere dense set of pairs, and for $(u', v')$ arbitrarily close to $(u, v)$ the segment lies in $W$. On such a segment $\varphi$ is continuous and locally concave, hence concave, and by continuity of $\varphi$ the inequality $\varphi(tu + (1 - t)v) \geq t \varphi(u) + (1 - t) \varphi(v)$ passes to the limit.

*Theorem P8.8.18, part 2, for complete simplicial fans.* By Proposition P8.8.12, $D \cdot V(\tau) \geq 0$ is the wall inequality across $\tau$, so the second and third conditions are equivalent by Proposition P8.8.19. If $D$ is nef, then $D \cdot V(\tau) \geq 0$ since $V(\tau)$ is a complete curve. The converse, that positivity on wall curves gives positivity on all curves, is part 1.

*Theorem P8.8.18, part 3.* If $D$ is a nef Cartier divisor, then $\varphi_D$ is convex by part 2, and $\mathcal{O}(D)$ is globally generated by Theorem P8.7.20.

*Theorem P8.8.18, parts 1 and 4, for smooth projective toric surfaces.* Let $X = X_\Sigma$ be a smooth projective toric surface, with rays $\rho_1, \dots, \rho_r$; the walls are the rays and the wall curves are the $D_i = D_{\rho_i}$. Let $C \subseteq X$ be an integral curve. If $C$ does not meet $T_N$, then $C \subseteq \bigcup_i D_i$, and $C$ is one of the $D_i$. Otherwise $C \cap T_N$ is an irreducible closed subset of codimension one in $T_N = \operatorname{Spec} k[M]$, and since $k[M]$ is factorial it is $V(f)$ for an irreducible Laurent polynomial $f = \sum_m c_m \chi^m$ (Proposition P3.8.12). The prime divisors of $X$ meeting $T_N$ are the closures of those of $T_N$, so by Lemma P8.7.2
$$\operatorname{div}(f) = C + \sum_{i=1}^r \Big( \min_{c_m \neq 0} \langle m, u_i \rangle \Big) D_i .$$
Choose $m_0$ with $c_{m_0} \neq 0$, for instance a vertex of the Newton polygon $\operatorname{conv} \{ m : c_m \neq 0 \}$, and put $g = \chi^{-m_0} f$. Then $\min_{c_m \neq 0} \langle m - m_0, u_i \rangle \leq 0$ for every $i$, so
$$C = \operatorname{div}(g) + \sum_i c_i D_i, \qquad c_i = - \min_{c_m \neq 0} \langle m - m_0, u_i \rangle \geq 0 .$$
The surface is smooth and projective, so linearly equivalent divisors have the same intersection numbers (Theorem P5.5.6), and $[C] = \sum_i c_i [D_i]$ in $N_1(X)$. Hence $NE(X)$ is the cone spanned by the $[D_i]$. It is finitely generated, so it is closed by Theorem P8.6.3, and $NE(X) = \overline{NE}(X)$. This is part 1, and part 2 follows as above. Part 4 is Kleiman's criterion, Theorem P5.12.6: $D$ is ample if and only if $D$ is positive on $\overline{NE}(X) \setminus \{0\}$, which for a cone spanned by the $[D_i]$ means $D \cdot D_i > 0$ for every $i$ for which $[D_i] \neq 0$, and every $[D_i]$ is nonzero, since $D_i \cdot H > 0$ for an ample $H$.

*The general case.* For a complete simplicial fan of dimension $n \geq 3$, the same strategy needs to move an arbitrary curve to a sum of invariant curves. Cox, Little and Schenck, Theorem 6.3.20, do this by degenerating the curve under a one-parameter subgroup to a limit $1$-cycle supported on the complement of the torus, which is a union of smaller toric varieties, and using induction on the dimension of the orbit closures; this is not reproduced here.

### Exercises

1. (A) Compute $NE$ and $\operatorname{Nef}$ of $\mathbb{P}^1 \times \mathbb{P}^1$ from its fan.
2. (A) For the curve $C = \{ 1 + x + y = 0 \} \subseteq \mathbb{G}_m^2$ in $\mathbb{P}^2$, with $x = \chi^{e_1^*}$ and $y = \chi^{e_2^*}$, find the coefficients $c_i$ of the proof and check that $C$ is a line.
3. (B) Compute $NE$ and $\operatorname{Nef}$ for the blow-up of $\mathbb{P}^2$ at the three fixed points of Exercise 2 of Section 8.2, and find the $K$-negative extremal rays.
4. (B) Show that for the conic $C = \{ x y = 1 + x + y \}$ in the torus of $\mathbb{P}^1 \times \mathbb{P}^1$ the proof gives $[C] = [D_1] + [D_2]$ for two rays $D_1$, $D_2$ from different rulings, whichever vertex of the Newton polygon is chosen.
5. (B) Let $X$ be a smooth projective toric surface. Show that the extremal rays of $NE(X)$ are spanned by curves $D_i$ with $D_i^2 \leq 0$ when $X \neq \mathbb{P}^2$, and that a $K$-negative extremal ray is either a curve with $D_i^2 = -1$ or a fibre of a ruling.
6. (C) Let $\Sigma$ be complete and $\varphi$ a convex support function with linear pieces $m_\sigma$ on $\sigma \in \Sigma(n)$. Show that $\varphi$ is strictly convex in the sense of Definition P8.7.18 if and only if $\langle m_\sigma, u_\rho \rangle > \varphi(u_\rho)$ for every $\sigma \in \Sigma(n)$ and every ray $\rho \notin \sigma(1)$, and, for $\Sigma$ simplicial, if and only if every wall inequality is strict.

### Lean

The combinatorial core of the theorem is proved in the repository. `MinimalModel.Toric.Fan.coneTheorem` states that for a complete simplicial fan an $\mathbb{R}$-Cartier divisor is nef, meaning that it has a convex support function (`MinimalModel.Toric.Fan.IsNef`), exactly when its degree `MinimalModel.Toric.Fan.WallData.degree` is nonnegative on every wall pair. `MinimalModel.Toric.toricConeTheorem` proves the pinned statement `ToricConeTheorem` from it. Proposition P8.8.19 is `MinimalModel.Toric.Fan.concaveOn_iff_forall_isConvexAcross_of_isSimplicialFan`, with the version without the simplicial hypothesis `MinimalModel.Toric.Fan.concaveOn_iff_forall_isConvexAcross`. The geometric statement, that the cone of curves of $X_\Sigma$ is spanned by the wall curves, needs the scheme $X_\Sigma$ and is not in Lean.

### Notes and history

The toric cone theorem goes back to Reid's 1983 paper on the minimal model program for toric varieties, where the cone of curves of a projective simplicial toric variety is shown to be spanned by the wall curves and the contractions of its extremal rays are constructed combinatorially. Cox, Little and Schenck, Theorem 6.3.20, prove it for every complete fan, and Fujino and Sato give a relative version and a proof that works without projectivity. Volume 3 uses it as the first step of the toric minimal model program, and the proof for surfaces given here is the toric case of the general principle that a curve can be moved to the boundary along a family.
