---
title: Support functions and the combinatorial cone theorem
nodes: [MM6EHAYFKV]
sources: [CLS11, Rei83, FS04, Dem70, KKMS73]
reads_with: [CLS11:ch4, CLS11:ch6, FS04:4]
requires: [P8.6, 3.1, 3.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Support functions and the combinatorial cone theorem

### Statement

In this section $\Sigma$ is a complete fan in $N_{\mathbb{R}} \cong \mathbb{R}^n$, and divisors may have real coefficients. A *torus-invariant $\mathbb{R}$-divisor* is a formal sum $D = \sum_\rho a_\rho D_\rho$ with $a_\rho \in \mathbb{R}$. It is *$\mathbb{R}$-Cartier on the fan* if for each $\sigma \in \Sigma$ there is $m_\sigma \in M_{\mathbb{R}}$ with $\langle m_\sigma, u_\rho \rangle = -a_\rho$ for all $\rho \in \sigma(1)$. On a simplicial fan every $D$ has this property, since the $u_\rho$ of a cone are independent. For a $\mathbb{Q}$-divisor it is the $\mathbb{Q}$-Cartier condition of Theorem 3.3.20, part 1.

**Definition 3.4.11 (support functions).** A *support function* of $\Sigma$ is a function $\varphi \colon N_{\mathbb{R}} \to \mathbb{R}$ that is linear on each cone of $\Sigma$. The support function of an $\mathbb{R}$-Cartier divisor $D$ is

$$\varphi_D(u) = \langle m_\sigma, u \rangle \quad \text{for } u \in \sigma.$$

It is well defined, since on $\sigma \cap \sigma'$, which is spanned by its rays, $m_\sigma$ and $m_{\sigma'}$ agree. It satisfies $\varphi_D(u_\rho) = -a_\rho$, and it is the only support function with these values. The function $\varphi_D$ is *convex* if

$$\varphi_D(t u + (1 - t) v) \ge t \varphi_D(u) + (1 - t) \varphi_D(v) \quad \text{for all } u, v \in N_{\mathbb{R}}, \ t \in [0, 1].$$

It is *strictly convex* if it is convex and $m_\sigma \neq m_{\sigma'}$ for any two different cones $\sigma, \sigma'$ of dimension $n$.

The word convex follows Cox-Little-Schenck, Chapter 6. In the usual language of analysis, $\varphi_D$ is concave. The sign comes from $\varphi_D(u_\rho) = -a_\rho$: an effective divisor has a support function that is negative on the rays.

**Proposition 3.4.12 (convex support functions).** Let $\varphi$ be a support function of the complete fan $\Sigma$, and for each cone $\sigma$ of dimension $n$ let $m_\sigma$ be the linear form that agrees with $\varphi$ on $\sigma$. The following are equivalent.

1. $\varphi$ is convex.
2. $\langle m_\sigma, u \rangle \ge \varphi(u)$ for all $u \in N_{\mathbb{R}}$ and all $\sigma$ of dimension $n$.
3. $\varphi(u) = \min_\sigma \langle m_\sigma, u \rangle$ for all $u$.

Lean: the step from 1 to 2 for the two cones of a wall is `MinimalModel.Toric.Fan.isConvexAcross_of_concaveOn`.

**Theorem 3.4.13 (the toric cone theorem, combinatorial form).** Let $\Sigma$ be a complete simplicial fan and $D = \sum_\rho a_\rho D_\rho$ a torus-invariant $\mathbb{R}$-divisor. The following are equivalent.

1. $\varphi_D$ is convex.
2. For each wall pair $(\sigma, \sigma')$ of $\Sigma$, with the standard labels of Definition 3.4.1, $\langle m_\sigma, u_{n+1} \rangle \ge -a_{n+1}$. This is the *wall inequality*.
3. $D \cdot V(\tau) \ge 0$ for each wall $\tau$ of $\Sigma$, where $D \cdot V(\tau)$ is the number of Theorem 3.4.4, extended linearly to $\mathbb{R}$-divisors.

Also, $\varphi_D$ is strictly convex if and only if $D \cdot V(\tau) > 0$ for each wall $\tau$.

Node: MM6EHAYFKV · Lean: `MinimalModel.Toric.toricConeTheorem`

Part 1 is called *$D$ is nef* in the Lean library, and in Section 3 it becomes the nefness of $D$ on $X_\Sigma$. The equivalence of parts 1 and 3 is the Lean theorem. The statement about strict convexity is not in Lean.

**Theorem 3.4.14 (local to global).** Let $\Sigma$ be a complete fan, not necessarily simplicial, and $\varphi$ a support function. If $\varphi$ satisfies the wall inequality at every wall, in the form $\langle m_\sigma, x \rangle \ge \varphi(x)$ for all $x \in \sigma'$ and every wall pair $(\sigma, \sigma')$, then $\varphi$ is convex.

Lean: `MinimalModel.Toric.Fan.concaveOn_iff_forall_isConvexAcross`, with the hypothesis that every cone of the fan is a closed subset of $N_{\mathbb{R}}$. For simplicial fans the hypothesis is proved, and the result is `MinimalModel.Toric.Fan.concaveOn_iff_forall_isConvexAcross_of_isSimplicialFan`.

### Proof in words

A support function is a tent made of flat pieces, one for each maximal cone. It is convex in the sense of the definition when the tent bends down at every crease. Proposition 3.4.12 says that this is the same as asking that each flat piece, extended to a whole hyperplane, lies above the tent everywhere.

The creases of the tent are the walls. At a wall between $\sigma$ and $\sigma'$, the tent bends down when the plane of $\sigma$ lies above the plane of $\sigma'$ on the side of $\sigma'$. Since the two planes agree on the wall, it suffices to compare them at one point off the wall, the generator $u_{n+1}$. This is the wall inequality, and by Theorem 3.4.4 it says $D \cdot V(\tau) \ge 0$.

The main step is that bending down at each wall gives bending down everywhere. Restrict $\varphi$ to a segment. A generic segment crosses only walls, never a cone of dimension $n - 2$ or less, because the segments that meet such a cone form a set of smaller dimension. At each crossing point the slope of $\varphi$ along the segment drops, by the wall inequality. So $\varphi$ restricted to the segment is a concave piecewise linear function of one variable, and the chord lies below it. A limit removes the genericity.

### Examples

**Example 3.4.15 (projective space).** On $\mathbb{P}^n$ take $D = a D_0$. Its data are $m_{\sigma_0} = 0$ on the cone without $u_0$, and $m_{\sigma_i} = a e_i^*$ on the cone without $u_i$, for $i \ge 1$ (Example 3.3.15). So $\varphi_D(u) = \min(0, a u_1, \dots, a u_n)$ for $a \ge 0$, which is convex, and strictly convex for $a > 0$. For $a < 0$ the function is $\max(0, a u_1, \dots, a u_n)$, which is not convex. By Theorem 3.4.13 this matches $D \cdot V(\tau) = a$ for every line $V(\tau)$.

**Example 3.4.16 (the Hirzebruch surface).** On $\mathbb{F}_n$ let $D = a D_2 + b D_4$, so $\varphi_D(u_2) = -a$, $\varphi_D(u_4) = -b$ and $\varphi_D(u_1) = \varphi_D(u_3) = 0$. By Example 3.4.7,

$$D \cdot D_1 = D \cdot D_3 = a + b, \qquad D \cdot D_2 = -na, \qquad D \cdot D_4 = nb.$$

So for $n \ge 1$, $\varphi_D$ is convex if and only if $a \le 0 \le b$ and $a + b \ge 0$. For instance $D = D_4$ is convex, and $D = D_2$ is not: $\varphi_{D_2}$ is $-1$ at $u_2 = (0, 1)$ and $0$ at $u_1$ and $u_3$, so on the segment from $u_1 = (1, 0)$ to $u_3 = (-1, n)$ its value at the midpoint $(0, \frac n2) = \frac n2 u_2$ is $-\frac n2$. This is below the chord value $0$. The failure sits at the wall $u_2$, the negative section.

**Example 3.4.17 (the wall inequality at a singular point).** On $\mathbb{P}(1,1,n)$ let $D = D_1$. On $\sigma' = \operatorname{Cone}(u_1, u_3)$ the data solves $\langle m, (1, 0) \rangle = -1$ and $\langle m, (-1, n) \rangle = 0$, so $m_{\sigma'} = (-1, -\frac1n)$. It is rational, which reflects that $D_1$ is only $\mathbb{Q}$-Cartier (Example 3.3.17). On $\sigma = \operatorname{Cone}(u_1, u_4)$ the data is $m_\sigma = (-1, 0)$. The wall inequality at the wall $u_1$, with $u_{n+1} = u_3$, reads $\langle m_\sigma, u_3 \rangle = 1 \ge -a_3 = 0$, which holds. By Example 3.4.8 the intersection number is $D_1^2 = \frac1n$, and Theorem 3.4.4 gives $\frac1n (1 - 0) = \frac1n$, the same.

**Example 3.4.18 (the small resolution).** On $\Sigma_+$ of Example 3.4.9 the fan is not complete, so Theorem 3.4.13 does not apply as stated. The wall inequality still makes sense on the one wall. For $D = D_1$ it fails, since $D_1 \cdot C = -1 < 0$, and for $D = D_2$ it holds strictly. Chapter 5 uses the relative form of the cone theorem, over the affine variety $U_\sigma$ of the cone over a square, where these two signs decide the flip.

### Proof

*Proof of Proposition 3.4.12.* First, $\varphi$ is positively homogeneous, $\varphi(s u) = s \varphi(u)$ for $s \ge 0$, since it is linear on each cone. Assume 1. Then $\varphi(u + v) = 2 \varphi(\frac12 u + \frac12 v) \ge \varphi(u) + \varphi(v)$. Let $\sigma$ have dimension $n$ and $x \in N_{\mathbb{R}}$. Since $\sigma$ spans $N_{\mathbb{R}}$, write $x = p - q$ with $p, q \in \sigma$. Then

$$\langle m_\sigma, p \rangle = \varphi(p) = \varphi(x + q) \ge \varphi(x) + \varphi(q) = \varphi(x) + \langle m_\sigma, q \rangle,$$

so $\varphi(x) \le \langle m_\sigma, x \rangle$. This is 2. Given 2, every $u$ lies in some cone of dimension $n$ (the cones of dimension $n$ cover $N_{\mathbb{R}}$, as in the proof of Lemma 3.4.2), and there $\varphi(u) = \langle m_\sigma, u \rangle$, which gives 3. A minimum of linear functions satisfies the inequality of 1, which gives 1. $\square$

*Proof of Theorem 3.4.14.* Since the fan is finite and each cone is closed, $\varphi$ is continuous: it is continuous on each closed cone, and finitely many closed sets cover $N_{\mathbb{R}}$. The inequality of convexity is preserved under limits of $u$ and $v$, so it is enough to prove it for $(u, v)$ in a dense subset of $N_{\mathbb{R}} \times N_{\mathbb{R}}$.

*The generic segments.* Let $\delta \in \Sigma$ with $\dim \delta \le n - 2$, and let $W \supset \operatorname{span}(\delta)$ be a subspace of dimension $n - 2$. If the segment $[u, v]$ meets $\delta$, say at $w$, then $u, v \in W + \mathbb{R}(v - u)$, since $u = w + s(u - v)$ for some $s$. So $\dim (W + \mathbb{R} u + \mathbb{R} v) \le n - 1$. The set of pairs $(u, v)$ with this property is the zero set of the $n \times n$ minors of the matrix of a basis of $W$ together with $u$ and $v$. These polynomials are not all zero, since $W$ can be completed to $N_{\mathbb{R}}$ by two vectors. So the bad pairs for $\delta$ form a proper algebraic subset, and so do the bad pairs for all the finitely many $\delta$. Its complement $G$ is open and dense.

*The crossing points.* Fix $(u, v) \in G$ and put $g(t) = \varphi(u + t(v - u))$ for $t \in [0, 1]$. For each cone $\sigma$ of dimension $n$, the set $I_\sigma = \{t : u + t(v - u) \in \sigma\}$ is a closed interval, since $\sigma$ is convex and closed, and $g$ is affine on it with slope $\langle m_\sigma, v - u \rangle$. The intervals $I_\sigma$ cover $[0, 1]$, and the ones with nonempty interior already cover it, since the others are points and the union of the first kind is closed. Let $0 = t_0 < t_1 < \dots < t_r = 1$ be the endpoints of these intervals, so that each $[t_{j-1}, t_j]$ lies in some $I_{\sigma_j}$. Consider a point $t_j$ with $0 < j < r$, and $p = u + t_j (v - u)$. Then $p \in \sigma_j \cap \sigma_{j+1}$, which is a cone of the fan. If $\sigma_j = \sigma_{j+1}$, the slope does not change at $t_j$. Otherwise $\sigma_j \cap \sigma_{j+1}$ is a proper face of $\sigma_j$, so its dimension is at most $n - 1$, and it contains $p$, so its dimension is at least $n - 1$ by the choice of $G$. So $(\sigma_j, \sigma_{j+1})$ is a wall pair. For small $h > 0$, $p + h(v - u) \in \sigma_{j+1}$, and the hypothesis gives

$$\langle m_{\sigma_j}, p + h(v - u) \rangle \ge \varphi(p + h(v - u)) = \langle m_{\sigma_{j+1}}, p + h(v - u) \rangle.$$

Both forms equal $\varphi(p)$ at $p$, so $\langle m_{\sigma_j}, v - u \rangle \ge \langle m_{\sigma_{j+1}}, v - u \rangle$. So the slopes of $g$ do not increase from left to right.

*The chord.* A continuous function on $[0, 1]$ that is affine on each $[t_{j-1}, t_j]$ with nonincreasing slopes is concave, so $g(t) \ge (1 - t) g(0) + t g(1)$. This is the inequality $\varphi((1 - t) u + t v) \ge (1 - t) \varphi(u) + t \varphi(v)$. $\square$

*Proof of Theorem 3.4.13.* Let $(\sigma, \sigma')$ be a wall pair with the standard labels. Since $m_\sigma - m_{\sigma'}$ vanishes on $\tau$ and $\sigma' = \tau + \mathbb{R}_{\ge 0} u_{n+1}$, for $x = y + s u_{n+1}$ in $\sigma'$ with $y \in \tau$ and $s \ge 0$,

$$\langle m_\sigma, x \rangle - \varphi_D(x) = \langle m_\sigma - m_{\sigma'}, x \rangle = s \big( \langle m_\sigma, u_{n+1} \rangle + a_{n+1} \big).$$

So the wall inequality of part 2 is the same as $\langle m_\sigma, x \rangle \ge \varphi_D(x)$ on $\sigma'$. With $u_{n+1} = \sum c_i u_i$, the number $\langle m_\sigma, u_{n+1} \rangle + a_{n+1}$ is $a_{n+1} - \sum c_i a_i$, which is a positive multiple of $D \cdot V(\tau)$ by Theorem 3.4.4. So parts 2 and 3 are equivalent. Part 1 implies part 2 by Proposition 3.4.12. Part 2 implies part 1 by Theorem 3.4.14, since simplicial cones are closed.

For strict convexity, assume $\varphi_D$ convex. If $D \cdot V(\tau) = 0$ for some wall, then $m_\sigma - m_{\sigma'}$ vanishes on $\tau$ and at $u_{n+1}$, so on $N_{\mathbb{R}}$, and $\varphi_D$ is not strictly convex. Conversely, suppose that $D \cdot V(\tau) > 0$ for every wall but $m_\sigma = m_{\sigma''}$ for two different cones $\sigma$, $\sigma''$ of dimension $n$. Put $m = m_\sigma$. By Proposition 3.4.12, $\varphi_D \le m$, with equality on $\sigma \cup \sigma''$. For $p \in \sigma$ and $q \in \sigma''$, convexity gives $\varphi_D \ge m$ on $[p, q]$, so $\varphi_D = m$ on the convex hull of $\sigma \cup \sigma''$. Pick $p$ in the interior of $\sigma$ and $q$ in the interior of $\sigma''$ with $(p, q) \in G$, the set of generic pairs in the proof of Theorem 3.4.14. Balls $B_p \subset \sigma$ and $B_q \subset \sigma''$ around $p$ and $q$ have a convex hull that contains a neighbourhood of each point of the open segment $(p, q)$, and $\varphi_D = m$ there. Only $\sigma$ contains $p$ among the cones of dimension $n$, so with the notation of that proof $\sigma_1 = \sigma$. The segment ends in the interior of $\sigma'' \neq \sigma$, so there is a first crossing point $t_1$, where it passes from $\sigma_1$ to a cone $\sigma_2 \neq \sigma_1$ across a wall. For $t_1 < t < t_2$ the point $p + t(q - p)$ lies in $\sigma_2$ and has a neighbourhood on which $\varphi_D = m$. That neighbourhood meets the interior of $\sigma_2$ in an open set, where $\varphi_D = m_{\sigma_2}$, so $m_{\sigma_2} = m = m_{\sigma_1}$. Then $D \cdot V(\sigma_1 \cap \sigma_2) = 0$, a contradiction. $\square$

### Exercises

1. (A) Show that the support function of a principal divisor $\operatorname{div}(\chi^m)$ is the linear function $-\langle m, \cdot \rangle$, and that $\varphi_{D + \operatorname{div}(\chi^m)} = \varphi_D - m$. Deduce that convexity depends only on the class of $D$ in $\operatorname{Cl}(X_\Sigma) \otimes \mathbb{R}$.
2. (A) On $\mathbb{P}^1 \times \mathbb{P}^1$, with rays $\pm e_1, \pm e_2$, find all $(a_1, a_2, a_3, a_4)$ for which $D = \sum a_i D_i$ has a convex support function, and those for which it is strictly convex.
3. (A) On $\mathbb{F}_n$, show that $-K = \sum D_i$ has a convex support function if and only if $n \le 2$, and a strictly convex one if and only if $n \le 1$.
4. (B) Show that a support function that is convex and also satisfies the reverse inequality is linear. Deduce that if $D \cdot V(\tau) = 0$ for every wall of a complete simplicial fan, then $D$ is the divisor of a real character: $a_\rho = \langle m, u_\rho \rangle$ for one $m \in M_{\mathbb{R}}$.
5. (B) Let $\Sigma$ be the complete fan in $\mathbb{R}^2$ with the rays $(1, 0)$, $(0, 1)$, $(-1, -1)$ and the star subdivision at $(1, 1)$, the fan of the blow-up of $\mathbb{P}^2$ at a fixed point. List its four walls and the wall inequalities, and find the cone of $(a_\rho) \in \mathbb{R}^4$ with $\varphi_D$ convex.
6. (C) Let $\Sigma$ be a fan, not necessarily complete, whose support $|\Sigma|$ is convex and of dimension $n$. Adapt the proof of Theorem 3.4.14 to show: if a support function satisfies the wall inequality at every wall pair of $\Sigma$, then it is convex on $|\Sigma|$. Apply it to the fan $\Sigma_+$ of Example 3.4.18 and the divisor $D_2$.

### Lean

- Status: proved. The combinatorial cone theorem is `MinimalModel.Toric.Fan.coneTheorem`: for a complete fan `F.IsComplete`, simplicial `F.IsSimplicialFan`, and an $\mathbb{R}$-Cartier divisor `F.IsRCartier D`, it states that `F.IsNef D` holds if and only if `0 ≤ W.degree D` for every wall pair `F.IsWallPair σ σ'` and every wall datum `W : F.WallData σ σ'`. The pinned form is `MinimalModel.Toric.toricConeTheorem`, which proves the statement `MinimalModel.Toric.ToricConeTheorem` of the file of pinned statements. A comparator job checks that the two agree.
- Fidelity: `MinimalModel.Toric.Fan.IsNef` is defined as the existence of a support function of $D$ that is convex in the sense of this section (`ConcaveOn` in Mathlib). It is not the nefness of a line bundle, because the library does not construct the scheme $X_\Sigma$, its curves or its intersection numbers. So the Lean theorem is the equivalence of parts 1 and 3 of Theorem 3.4.13 on the fan, and not the geometric statement of Section 3. The degree `MinimalModel.Toric.Fan.WallData.degree` is $a_{n+1} - \sum c_i a_i$, a positive multiple of $D \cdot V(\tau)$ (Theorem 3.4.4), so the signs agree. The proof follows the proof above: `MinimalModel.Toric.Fan.isConvexAcross_of_concaveOn` is Proposition 3.4.12 for a wall, `MinimalModel.Toric.exists_forall_notMem` chooses the generic segment, `MinimalModel.Toric.chord_le_of_local` is the chord step, and `MinimalModel.Toric.Fan.IsWallPair.nonempty_wallData` shows that every wall pair of a simplicial fan has wall data, so the condition on degrees is not empty.
- Fidelity of the general case: Theorem 3.4.14 for a complete fan that is not simplicial is `MinimalModel.Toric.Fan.concaveOn_iff_forall_isConvexAcross`, and it takes as a hypothesis that every cone is a closed set. Every finitely generated cone is closed, but Mathlib has no such lemma yet, so the library proves it only for simplicial cones (`MinimalModel.Toric.IsSimplicial.isClosed`).
- Node MM6EHAYFKV is Theorem 3.4.13, parts 1 and 3. Its statement on the map is this combinatorial form.

### Notes and history

Piecewise linear functions on a fan describe the torus-invariant Cartier divisors in the work of Demazure (1970) and of Kempf, Knudsen, Mumford and Saint-Donat (1973), together with the criterion of ampleness by strict convexity. Cox-Little-Schenck give these criteria in Chapter 6, together with the nef criterion of Section 3 below. The generic segment argument is the usual proof that a function which is locally convex near each wall is convex. Fujino and Sato (2004, Theorem 4.1) state the cone theorem for toric varieties over a base. The map cites Reid (1983, Section 1) for the simplicial case, the first step of his toric MMP.
