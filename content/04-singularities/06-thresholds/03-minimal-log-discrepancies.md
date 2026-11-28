---
title: Minimal log discrepancies
nodes: []
sources: [KM98, Amb99, Bor97, Rei87, CLS11, Sho04]
reads_with: [Amb99:sec2, KM98:ch2]
requires: [3.1, 3.2, 3.3, 4.1, 4.2, 4.3, 4.4]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Minimal log discrepancies

### Statement

The classes of Chapter 2 ask whether all discrepancies over $X$ are above a bound. The minimal log discrepancy asks for the smallest one over a given centre. It is the second number of this chapter, and the one that enters the termination of flips.

**Definition 4.6.16 (minimal log discrepancy).** Let $(X, \Delta)$ be a sub-pair and $W \subset X$ a closed irreducible subset. The *minimal log discrepancy* of $(X, \Delta)$ at $W$ is
$$\operatorname{mld}(W; X, \Delta) = \inf\{ A(E, X, \Delta) : E \text{ a divisor over } X \text{ with } c_X(E) = W \}$$
if every such $E$ has $A(E, X, \Delta) \ge 0$, and $\operatorname{mld}(W; X, \Delta) = -\infty$ otherwise. For a closed point $x$ write $\operatorname{mld}(x; X, \Delta)$.

Here $A = a + 1$ is the log discrepancy of Definition 4.1.4. If $W$ is a prime divisor, the only divisor over $X$ with centre $W$ is $W$ itself, and $\operatorname{mld}(W; X, \Delta) = 1 - \operatorname{mult}_W \Delta$ when this is at least 0. For an lc pair every log discrepancy is at least 0, so the minimal log discrepancy is a number in $[0, \infty)$, and the definition agrees with Definition 1.1.20.

**Proposition 4.6.17 (the classes and the minimal log discrepancy).** Let $(X, \Delta)$ be a pair and $x \in X$ a closed point, with $n = \dim X \ge 2$. If $(X, \Delta)$ is lc, then $\operatorname{mld}(x; X, \Delta) \ge 1 + \operatorname{discrep}(X, \Delta)$. In particular $\operatorname{mld}(x; X, \Delta)$ is greater than 1 if the pair is terminal, at least 1 if it is canonical, greater than 0 if it is klt, and at least 0 if it is lc.

Lean: not yet in Lean.

**Theorem 4.6.18 (the minimal log discrepancy of an snc pair).** Let $Y$ be a smooth variety and $\Delta = \sum_i b_i F_i$ an $\mathbb{R}$-divisor with snc support and every $b_i \le 1$. Let $W \subset Y$ be a closed irreducible subset of codimension $c \ge 1$. Then
$$\operatorname{mld}(W; Y, \Delta) = c - \sum_{i : W \subset F_i} b_i,$$
and the minimum is attained by the blow-up of $W$, or by $W$ itself if $c = 1$. In particular $\operatorname{mld}(x; Y, \Delta) = n - \sum_{x \in F_i} b_i$ for a closed point $x$, and a smooth point $x$ of a variety $X$ of dimension $n$ has $\operatorname{mld}(x; X, 0) = n$.

Lean: not yet in Lean.

**Corollary 4.6.19 (semicontinuity for snc pairs).** In the theorem, let every $b_i$ lie in $[0, 1]$. Then the function $x \mapsto \operatorname{mld}(x; Y, \Delta)$ on the closed points of $Y$ takes finitely many values and is lower semicontinuous: for every $t$,
$$\{ x : \operatorname{mld}(x; Y, \Delta) \le t \} = \bigcup \Big\{ F_I : F_I \ne \emptyset, \ \sum_{i \in I} b_i \ge n - t \Big\}, \qquad F_I = \bigcap_{i \in I} F_i,$$
a finite union of closed sets, with $F_\emptyset = Y$.

Lean: not yet in Lean.

For toric varieties the minimal log discrepancy at the fixed point is a minimum over lattice points. Let $\sigma \subset N_\mathbb{R}$ be a strongly convex rational polyhedral cone of dimension $n = \operatorname{rank} N$, with fixed point $\gamma_\sigma \in U_\sigma$ (Theorem 3.2.29). Let $\Delta = \sum_{\rho \in \sigma(1)} d_\rho D_\rho$ with every $d_\rho \in [0, 1]$, and suppose that there is $m_{\sigma, \Delta} \in M_\mathbb{R}$ with $\langle m_{\sigma, \Delta}, u_\rho \rangle = 1 - d_\rho$ for every ray $\rho$ of $\sigma$. For $\Delta = 0$ this is the vector $m_\sigma$ of Corollary 3.3.27.

**Theorem 4.6.20 (the toric minimal log discrepancy).** In this situation $K_{U_\sigma} + \Delta$ is $\mathbb{R}$-Cartier, the pair $(U_\sigma, \Delta)$ is lc, and
$$\operatorname{mld}(\gamma_\sigma; U_\sigma, \Delta) = \inf\{ \langle m_{\sigma, \Delta}, v \rangle : v \in N \cap \operatorname{int} \sigma \}.$$
The infimum is a minimum if every $d_\rho < 1$. For every primitive $v \in N \cap \operatorname{int} \sigma$, the toric divisor of $v$ has centre $\gamma_\sigma$ and log discrepancy $\langle m_{\sigma, \Delta}, v \rangle$.

Lean: not yet in Lean.

### Proof in words

A divisor with centre a point is exceptional, so the minimal log discrepancy is at least one more than the discrepancy. For an snc pair, the blow-up of $W$ gives the value $c - \sum b_i$ by the formula for blow-ups, and the logarithmic bound shows that no divisor with centre $W$ does better: each coordinate that vanishes on $W$ contributes at least its weight $1 - b_i$ or $1$. The semicontinuity follows, because the formula only depends on which components pass through the point, and passing through more components can only lower it.

For a toric pair, every toric divisor is a ray of a refinement, and its log discrepancy is the value of the linear function $m_{\sigma, \Delta}$ on its generator. The rays in the interior of $\sigma$ are those whose divisor lies over the fixed point. Conversely, any divisor with centre the fixed point has its centre on a smooth toric model inside an orbit closure $V(\tau)$ with $\tau$ meeting the interior of $\sigma$, and the logarithmic bound in toric coordinates gives a log discrepancy at least $\langle m_{\sigma, \Delta}, w \rangle$ for the lattice point $w = \sum_\rho v_E(x_\rho) u_\rho$ of the interior.

### Examples

**Example 4.6.21 (the surface quotients $\frac1r(1, a)$).** Let $X = \frac1r(1, a)$ with $r \ge 2$ and $\gcd(a, r) = 1$, and for $1 \le k \le r - 1$ write $\overline{ka}$ for the residue of $ka$ in $\{1, \dots, r - 1\}$. By Lemma 4.4.3, $X = U_\sigma$ with $\sigma$ the positive quadrant and $N = \mathbb{Z}^2 + \mathbb{Z} \frac1r(1, a)$, so $m_\sigma = (1, 1)$, and the lattice points of $\sigma$ are $v_k + w$ with $w \in \mathbb{Z}^2_{\ge 0}$. For $k \ge 1$ both coordinates of $v_k = (\frac{k}{r}, \frac{\overline{ka}}{r})$ are positive, so $v_k$ lies in the interior. For $k = 0$ an interior point $w$ has both coordinates at least 1. So
$$\operatorname{mld}(0; X) = \min\Big\{ 2, \min_{1 \le k \le r-1} \frac{k + \overline{ka}}{r} \Big\} = \min_{1 \le k \le r-1} \frac{k + \overline{ka}}{r},$$
since $k + \overline{ka} \le 2r - 2$. For $\frac1r(1, 1)$ the values are $\frac{2k}{r}$, and $\operatorname{mld} = \frac2r$, which matches $a(E) = -\frac{r-2}{r}$ in Example 4.2.24. For $\frac15(1, 2)$ the four values are
$$\frac{1 + 2}{5} = \frac35, \qquad \frac{2 + 4}{5} = \frac65, \qquad \frac{3 + 1}{5} = \frac45, \qquad \frac{4 + 3}{5} = \frac75,$$
so $\operatorname{mld} = \frac35$. The values $\frac35$ and $\frac45$ are the log discrepancies of the two curves of the minimal resolution, $1 - \frac25$ and $1 - \frac15$ (Example 4.3.10).

**Example 4.6.22 (the $A_n$ singularity).** The $A_n$ singularity is $\frac{1}{n+1}(1, n)$ (Example 4.3.14). Here $\overline{kn} = n + 1 - k$, so every value $\frac{k + \overline{kn}}{n+1}$ is 1, and $\operatorname{mld}(0; X) = 1$. The minimal resolution gives the same answer without toric geometry. It is crepant, so $(Y, 0)$ is the crepant pullback, and every divisor $E$ with centre the singular point has centre on $Y$ inside the exceptional curves. If the centre on $Y$ is one of the curves $E_i$, then $A(E) = 1$. If it is a point, Theorem 4.6.18 on $Y$ gives $A(E) \ge 2$. So the minimum is 1, attained by each of the $n$ curves.

**Example 4.6.23 (the terminal quotients $\frac1r(1, -1, a)$).** Let $X = \frac1r(1, -1, a)$ with $\gcd(a, r) = 1$. Example 4.4.10 gives $v_k = (\frac kr, \frac{r-k}{r}, \frac{\overline{ka}}{r})$, with all three coordinates positive for $1 \le k \le r - 1$, and $\langle m_\sigma, v_k \rangle = S(k) = 1 + \frac{\overline{ka}}{r}$. A lattice point $v_k + w$ has value at least $S(k)$, and the interior points with $k = 0$ have value at least 3. So
$$\operatorname{mld}(0; X) = \min_{1 \le k \le r - 1} \Big( 1 + \frac{\overline{ka}}{r} \Big) = 1 + \frac1r,$$
attained at $k \equiv a^{-1} \pmod r$. The terminal quotients of index $r$ have minimal log discrepancy $1 + \frac1r$, and these numbers decrease to 1 as $r$ grows.

**Example 4.6.24 (the quotients $\frac1r(1, 1, 1)$).** For $X = \frac1r(1, 1, 1)$ the vectors are $v_k = \frac kr (1, 1, 1)$, all in the interior, with values $\frac{3k}{r}$. So $\operatorname{mld}(0; X) = \min\{3, \frac3r\} = \frac3r$. For $r = 2$ this is $\frac32$, which matches the discrepancy $\frac12$ of the blow-up of the vertex in Example 4.2.25. For $r = 3$ it is 1, and $X$ is canonical and not terminal. For $r \ge 4$ it is less than 1.

**Example 4.6.25 (the cone over a curve).** Let $V$ be a smooth projective curve of genus $g$, $L$ a line bundle of degree $d > 0$ and $X = C(V, L)$ the cone, with vertex $0$, and suppose that $K_X$ is $\mathbb{Q}$-Cartier. The blow-up $f \colon Y \to X$ of the vertex is the total space of $L^{-1}$, a smooth surface, with exceptional curve $E \cong V$, and Corollary 4.2.20 gives
$$a(E, X, 0) = -1 - \frac{2g - 2}{d}, \qquad A(E, X, 0) = \frac{2 - 2g}{d}.$$
If $g \ge 2$ this is negative, and $\operatorname{mld}(0; X) = -\infty$. If $g \le 1$, the crepant pullback is $(Y, bE)$ with $b = 1 + \frac{2g-2}{d} \le 1$, and $E$ is a smooth divisor. A divisor $E'$ over $X$ with centre the vertex has centre $W \subset E$ on $Y$. By Theorem 4.6.18, $A(E') \ge \operatorname{mld}(W; Y, bE)$, which is $1 - b$ if $W = E$ and $2 - b > 1 - b$ if $W$ is a point. So
$$\operatorname{mld}(0; X) = \frac{2 - 2g}{d} \quad \text{for } g \le 1.$$
For $g = 0$ and $L = \mathcal{O}(r)$, the cone is $\frac1r(1, 1)$ and the value $\frac2r$ agrees with Example 4.6.21. For the cone over a plane cubic, $g = 1$ and the minimal log discrepancy is 0: the pair is lc and not klt (Example 4.2.22).

### Proof

*Proposition 4.6.17.* A divisor $E$ with $c_X(E) = \{x\}$ is exceptional, because $\{x\}$ has codimension $n \ge 2$. So $A(E, X, \Delta) = a(E, X, \Delta) + 1 \ge 1 + \operatorname{discrep}(X, \Delta)$. If the pair is lc, then $\operatorname{discrep}(X, \Delta) \ge -1$, so no log discrepancy over $x$ is negative, the minimal log discrepancy is the infimum of the definition, and it is at least $1 + \operatorname{discrep}(X, \Delta)$. The four classes have $\operatorname{discrep} > 0$, $\ge 0$, $> -1$ and $\ge -1$ (Definition 4.2.1), so $1 + \operatorname{discrep}$ is greater than 1, at least 1, greater than 0 and at least 0.

*Theorem 4.6.18.* Let $F_1, \dots, F_k$ be the components that contain $W$, and $s = \sum_{i \le k} b_i$. If $c = 1$, then $W$ is a prime divisor, the only divisor over $Y$ with centre $W$ is $W$, and $A(W) = 1 - \operatorname{mult}_W \Delta = c - s$. Let $c \ge 2$. The upper bound: $Y$ and $W$ are smooth at the generic point of $W$, so Lemma 4.1.20 applies to the blow-up of $W$. Each $F_i$ with $i \le k$ is smooth and contains $W$, so $\operatorname{mult}_W F_i = 1$, and the other components do not contain $W$. So $A(E_W) = c - \operatorname{mult}_W \Delta = c - s$. The lower bound: let $E$ have centre $W$. Lemma 4.2.11 gives coordinates $x_1, \dots, x_c$ at the generic point of $W$ with $F_i = \{x_i = 0\}$ for $i \le k$, and
$$A(E, Y, \Delta) \ge \sum_{i=1}^{k} (1 - b_i) \, v_E(x_i) + \sum_{j = k+1}^{c} v_E(x_j) \ge \sum_{i=1}^{k} (1 - b_i) + (c - k) = c - s,$$
because every $v_E(x_j) \ge 1$ and every $1 - b_i \ge 0$. In particular no log discrepancy over $W$ is negative, and the infimum is the minimum $c - s$. For a closed point $c = n$. A smooth point $x$ of $X$ has a smooth neighbourhood $U$, and $\operatorname{mld}(x; X, 0) = \operatorname{mld}(x; U, 0) = n$ by Corollary 4.1.15.

*Corollary 4.6.19.* By the theorem, $\operatorname{mld}(x) = n - \sum_{i \in I(x)} b_i$ with $I(x) = \{ i : x \in F_i \}$, so it takes at most $2^N$ values, where $N$ is the number of components. If $x \in F_I$ with $\sum_{i \in I} b_i \ge n - t$, then $I \subset I(x)$, and since every $b_i \ge 0$, $\sum_{i \in I(x)} b_i \ge n - t$, so $\operatorname{mld}(x) \le t$. Conversely, if $\operatorname{mld}(x) \le t$, then $x \in F_{I(x)}$ and $I = I(x)$ has $\sum_{i \in I} b_i \ge n - t$.

*Theorem 4.6.20.* Write $m = m_{\sigma, \Delta}$, and $m = \sum_j r_j m_j$ with $m_j \in M$ and $r_j \in \mathbb{R}$. Each $\langle m, u_\rho \rangle = 1 - d_\rho \ge 0$, so $m$ is nonnegative on $\sigma$.

Step 1, the log discrepancies of toric divisors. Let $\Sigma'$ be a refinement of the fan of faces of $\sigma$ and $f \colon Y = X_{\Sigma'} \to U_\sigma$ the proper birational toric morphism of Corollary 3.2.39. Take $K_{U_\sigma} = \operatorname{div}(\omega) = -\sum_\rho D_\rho$ and $K_Y = \operatorname{div}(\omega) = -\sum_{\rho'} D_{\rho'}$ with the form $\omega$ of Theorem 3.3.26. By Proposition 3.3.3,
$$K_{U_\sigma} + \Delta = -\sum_\rho \langle m, u_\rho \rangle D_\rho = -\sum_j r_j \operatorname{div}(\chi^{m_j}),$$
so $K_{U_\sigma} + \Delta$ is $\mathbb{R}$-Cartier, and $f^*(K_{U_\sigma} + \Delta) = -\sum_j r_j \operatorname{div}_Y(\chi^{m_j}) = -\sum_{\rho' \in \Sigma'(1)} \langle m, u_{\rho'} \rangle D_{\rho'}$, by Proposition 3.3.3 on $Y$. Hence
$$\Delta_Y = \sum_{\rho' \in \Sigma'(1)} (1 - \langle m, u_{\rho'} \rangle) D_{\rho'}, \qquad A(D_{\rho'}, U_\sigma, \Delta) = \langle m, u_{\rho'} \rangle.$$
If $\Sigma'$ is smooth, $\Delta_Y$ has snc support and coefficients at most 1, so Proposition 4.1.14 and Corollary 4.2.13 show that $(U_\sigma, \Delta)$ is lc.

Step 2, the upper bound. Let $v \in N \cap \operatorname{int} \sigma$ be primitive, and let $\Sigma'$ be the star subdivision of $\sigma$ at $v$, a refinement with the ray $\rho_v$ through $v$. By Theorem 3.2.37, part 3, $f$ maps $O(\rho_v)$ into the orbit of the smallest face of $\sigma$ that contains $v$, which is $\sigma$ itself. So $f(D_{\rho_v}) = \gamma_\sigma$, and Step 1 gives $A(D_{\rho_v}) = \langle m, v \rangle$. A lattice point $v$ of the interior that is not primitive is $v = \ell v'$ with $\ell \ge 2$ and $v' \in N \cap \operatorname{int} \sigma$ primitive, and $\langle m, v' \rangle \le \langle m, v \rangle$ since $m \ge 0$ on $\sigma$. So $\operatorname{mld}(\gamma_\sigma) \le \inf \langle m, v \rangle$.

Step 3, the lower bound. Let $E$ be a divisor over $U_\sigma$ with centre $\gamma_\sigma$, and let $f \colon Y \to U_\sigma$ come from a smooth refinement $\Sigma'$ (Theorem 3.1.29). The centre $W$ of $E$ on $Y$ is irreducible. Let $\tau \in \Sigma'$ be the cone whose orbit contains the generic point of $W$ (Theorem 3.2.29). Then $f(O(\tau)) \subset O(\sigma')$ for the smallest face $\sigma'$ of $\sigma$ containing $\tau$, and $f$ maps the generic point of $W$ to $\gamma_\sigma = O(\sigma)$, so $\sigma' = \sigma$. A point of the relative interior of $\tau$ that lies in a proper face of $\sigma$ forces all of $\tau$ into that face, so the relative interior of $\tau$ lies in $\operatorname{int} \sigma$. On the chart $U_\tau \cong \mathbb{A}^{\ell} \times (k^*)^{n - \ell}$, with $\ell = \dim \tau$, the divisors $D_\rho$ for $\rho \in \tau(1)$ are the coordinate hyperplanes $\{x_\rho = 0\}$, they contain $W$, and they are the only components of $\operatorname{Supp} \Delta_Y$ through the generic point of $W$, because $W$ meets $O(\tau)$, which lies in $D_{\rho'}$ only for $\rho' \in \tau(1)$. Extend the $x_\rho$ to a regular system of parameters at the generic point of $W$, and apply Lemma 4.2.11 to $(Y, \Delta_Y)$. The coefficient of $D_\rho$ is $1 - \langle m, u_\rho \rangle$, so
$$A(E, U_\sigma, \Delta) = A(E, Y, \Delta_Y) \ge \sum_{\rho \in \tau(1)} \langle m, u_\rho \rangle \, v_E(x_\rho) = \langle m, w \rangle, \qquad w = \sum_{\rho \in \tau(1)} v_E(x_\rho) \, u_\rho,$$
where the terms of the other parameters, which are nonnegative, have been dropped, and a $D_\rho$ with coefficient 0 counts as a parameter with weight $1 = \langle m, u_\rho \rangle$. Each $v_E(x_\rho) \ge 1$, so $w$ is a lattice point in the relative interior of $\tau$, hence in $\operatorname{int} \sigma$. So $A(E) \ge \inf \langle m, v \rangle$, which is at least 0. With Step 2 this proves the formula.

If every $d_\rho < 1$, then $m$ is positive on $\sigma \setminus \{0\}$, so $\{ v \in \sigma : \langle m, v \rangle \le C \}$ is bounded for every $C$, and it contains finitely many lattice points. So the infimum is a minimum. $\square$

### Exercises

1. (A) Let $\Delta = \frac12(H_1 + H_2 + H_3)$ for the coordinate planes of $\mathbb{A}^3$. Compute $\operatorname{mld}(x; \mathbb{A}^3, \Delta)$ at every closed point, and $\operatorname{mld}(W; \mathbb{A}^3, \Delta)$ for each coordinate axis $W$.
2. (A) Compute $\operatorname{mld}(0; \frac1r(1, 1))$ from Theorem 4.6.20, and check that the minimum is attained by the vector $v_1$, the exceptional curve of the minimal resolution.
3. (B) Show that every Du Val singularity has minimal log discrepancy 1 at its singular point, using that its minimal resolution is crepant (Chapter 3) and Theorem 4.6.18.
4. (B) Let $X$ be a terminal 3-fold and $x \in X$ a closed point. Show that $\operatorname{mld}(x; X, 0) > 1$, and that the set of numbers $\operatorname{mld}(0; \frac1r(1, -1, a))$ has 1 as its only accumulation point.
5. (B) Let $X = \frac1r(1, \dots, 1)$ in dimension $n$ with $r \ge 2$. Show that $\operatorname{mld}(0; X) = \frac{n}{r}$, and compare with Volume 3, Example 3.3.40.
6. (C) Let $X = \frac1r(a_1, \dots, a_n)$ with a faithful action and no pseudo-reflections. Show that
$$\operatorname{mld}(0; X) = \min\Big\{ n, \ \min_{1 \le k \le r - 1} \big( S(k) + \#\{ i : k a_i \equiv 0 \pmod r \} \big) \Big\},$$
with $S(k)$ as in Definition 4.4.2. Compute it for $\frac14(1, 1, 2)$ and for $\frac15(1, 1, 2)$.

### Lean

The definition `MinimalModel.mld` takes a pair and a scheme point $x$ and returns a value in $\mathbb{R} \cup \{-\infty\}$, written `WithBot ℝ`. It is $-\infty$ if some divisorial valuation with centre $x$ has negative log discrepancy, and otherwise the infimum of the log discrepancies of the divisorial valuations with centre $x$. This is Definition 4.6.16 for $W$ the closure of $x$. The statements of Section 4 are phrased with it. None of the theorems of this section is in Lean.

### Notes and history

The minimal log discrepancy was introduced by Shokurov in his approach to the termination of flips (Sho04). Its first systematic study is Ambro's paper (Amb99), which proves the lower semicontinuity in dimension at most 3 and for toric pairs, and computes toric minimal log discrepancies by lattice points as in Theorem 4.6.20. Borisov (Bor97) studied the minimal log discrepancies of toric singularities without boundary. For terminal quotients the value $1 + \frac1r$ is part of the terminal lemma of Reid and of Morrison and Stevens (Rei87). KM98, Chapter 2, works with discrepancies of the whole variety. The minimal log discrepancy refines them: the discrepancy is controlled by the minimal log discrepancies at the generic points of all subvarieties of codimension at least 2, while the minimal log discrepancy at a closed point only sees the divisors over that point.
