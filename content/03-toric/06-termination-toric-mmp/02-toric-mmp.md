---
title: The toric MMP and its end
nodes: [MMAWP4SA44]
sources: [CLS11, FS04, Rei83, KM98, Laz04]
reads_with: [FS04:3, FS04:4, CLS11:ch15, KM98:2]
requires: [1.1, 3.2, 3.3, 3.4, 3.5]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The toric MMP and its end

### Statement

The pieces are now in place. Chapter 4 gives the cone of curves, Chapter 5 the contraction of each extremal ray and the flip of each small one, and Section 1 the termination of flips. This section assembles them into the toric minimal model program for an arbitrary torus-invariant $\mathbb{Q}$-divisor $D$, and proves that it ends. It then computes the invariant that the general program uses to control singularities, the minimal log discrepancy, at a torus-fixed point.

**Definition 3.6.7 (the toric $D$-MMP).** Let $\Sigma$ be a complete simplicial fan with $X = X_\Sigma$ projective, and $D$ a torus-invariant $\mathbb{Q}$-divisor on $X$. A *toric $D$-MMP* from $(X, D)$ is a finite or infinite sequence of pairs $(X_k, D_k)$, $X_k = X_{\Sigma_k}$, with $(X_0, D_0) = (X, D)$, built by the following rule. Given $(X_k, D_k)$ with $\Sigma_k$ complete simplicial and $X_k$ projective:

1. If $D_k$ is nef, the sequence stops, and $(X_k, D_k)$ is a *minimal model* of $D$.
2. Otherwise choose an extremal ray $R_k$ of $NE(X_k)$ with $D_k \cdot R_k < 0$, and let $\pi_k \colon X_k \to Z_k$ be its contraction (Theorem 3.5.6).
   - If $\pi_k$ is of fibre type, the sequence stops, and $\pi_k$ is a *Mori fibre space* for $D_k$.
   - If $\pi_k$ is divisorial, put $X_{k+1} = Z_k$ and $D_{k+1} = (\pi_k)_* D_k$.
   - If $\pi_k$ is small, let $X_{k+1}$ be its flip (Theorem 3.5.20) and $D_{k+1}$ the strict transform of $D_k$.

For $D = K_X$ this is the toric $K$-MMP, and for $D = K_X + \Delta$ with $\Delta$ torus-invariant it is the toric MMP of the pair $(X, \Delta)$.

The choices are the extremal rays. Different choices give different programs, and Section 3 gives an example where two programs from the same $X$ end in different places.

**Theorem 3.6.8 (the toric MMP).** Let $\Sigma$, $X$ and $D$ be as in Definition 3.6.7.

1. At each step the rule can be applied: if $D_k$ is not nef, an extremal ray $R_k$ with $D_k \cdot R_k < 0$ exists. Each $\Sigma_{k+1}$ is complete and simplicial, each $X_{k+1}$ is projective and $\mathbb{Q}$-factorial, and $D_{k+1}$ is a torus-invariant $\mathbb{Q}$-divisor, $\mathbb{Q}$-Cartier on $X_{k+1}$. In the divisorial case $\rho(X_{k+1}) = \rho(X_k) - 1$, and in the small case $\rho(X_{k+1}) = \rho(X_k)$.
2. In a Mori fibre space $\pi_k$, the divisor $-D_k$ is $\pi_k$-ample, $\dim Z_k < \dim X_k$, and the curves contracted by $\pi_k$ are the curves with class in $R_k$.
3. Every toric $D$-MMP is finite. It has at most $\rho(X) - 1 = |\Sigma(1)| - n - 1$ divisorial steps, and it ends with a minimal model or a Mori fibre space.
4. If $D = K_X$, then $D_k = K_{X_k}$ for every $k$. If $D = K_X + \Delta$ with $\Delta = \sum_\rho d_\rho D_\rho$, then $D_k = K_{X_k} + \Delta_k$ with $\Delta_k$ the strict transform of $\Delta$, whose coefficients are the $d_\rho$ for the rays that remain.

Node: MMAWP4SA44 · Lean: `MinimalModel.ToricMMP`

**Corollary 3.6.9 (the $K$-MMP ends with a Mori fibre space).** Every toric $(K_X + \Delta)$-MMP with $\Delta = \sum_\rho d_\rho D_\rho$ and all $d_\rho < 1$ ends with a Mori fibre space. In particular every toric $K$-MMP ends with a Mori fibre space, and never with a minimal model.

Lean: not yet in Lean.

The second half of the node concerns singularities. For a pair $(X, \Delta)$ and a closed point $x$, the minimal log discrepancy $\operatorname{mld}(x; X, \Delta)$ is the infimum of the log discrepancies $a(E, X, \Delta) + 1$ over the prime divisors $E$ over $X$ with centre $x$ (Definition 1.1.20). The torus-fixed points of $X_\Sigma$ are the points $\gamma_\sigma = O(\sigma)$ for the cones $\sigma$ of dimension $n$ (Theorem 3.2.29).

**Theorem 3.6.10 (the toric mld).** Let $\sigma$ be a strongly convex rational polyhedral cone of dimension $n$, $U = U_\sigma$ with fixed point $\gamma_\sigma$, and $\Delta = \sum_{\rho \in \sigma(1)} d_\rho D_\rho$ with $0 \le d_\rho \le 1$ rational, such that $K_U + \Delta$ is $\mathbb{Q}$-Cartier. Let $m_\Delta \in M_{\mathbb{Q}}$ be the vector with

$$\langle m_\Delta, u_\rho \rangle = 1 - d_\rho \qquad \text{for all } \rho \in \sigma(1).$$

1. For every prime divisor $E$ over $U$ with centre $\gamma_\sigma$, there is a lattice point $w_E \in \operatorname{int}(\sigma) \cap N$ with $a(E, U, \Delta) + 1 \ge \langle m_\Delta, w_E \rangle$.
2. For every primitive $v \in \operatorname{int}(\sigma) \cap N$, the divisor $E_v$ of the star subdivision at $v$ has centre $\gamma_\sigma$ and $a(E_v, U, \Delta) + 1 = \langle m_\Delta, v \rangle$.
3. Hence
$$\operatorname{mld}(\gamma_\sigma; U, \Delta) = \min \{ \langle m_\Delta, v \rangle : v \in \operatorname{int}(\sigma) \cap N \},$$
and the minimum exists and is attained at a primitive vector.

If $\sigma$ is simplicial, $K_U + \Delta$ is $\mathbb{Q}$-Cartier for every $\Delta$ (Theorem 3.3.20), and $m_\Delta$ is the linear form with the values $1 - d_\rho$ at the $n$ minimal generators. The mld at a fixed point of a complete toric variety $X_\Sigma$ is the mld on the chart $U_\sigma$, since it only involves divisors with centre $\gamma_\sigma \in U_\sigma$.

Lean: not yet in Lean. The node MMAWP4SA44 includes this formula; the Lean statement `MinimalModel.ToricMMP` does not, see below.

### Proof in words

For Theorem 3.6.8 the only new input is bookkeeping. The cone of curves is polyhedral and contains no line, so a divisor that is not nef is negative on one of its edges. The contraction of that edge is one of three kinds, decided by the signs of its relation. A divisorial contraction lowers the number of rays by one, and a flip keeps the rays. There are fewer than $|\Sigma(1)|$ divisorial steps, and between two of them only finitely many flips, by Section 1.

The mld formula comes from one rational $n$-form. The form $\omega = \bigwedge_i d\chi^{m_i}/\chi^{m_i}$ has divisor $-\sum D_\rho$ on every toric variety, and $\chi^{m_\Delta} \omega$ is a generator of $K_U + \Delta$. For a divisor $E$ over $U$ the valuation $v_E$, restricted to the characters, is a lattice point $w_E$ of $N$, and the order of $\chi^{m_\Delta}$ along $E$ is $\langle m_\Delta, w_E \rangle$. The order of $\omega$ along $E$ is at least $-1$, with equality for the toric divisors. So the log discrepancy is at least $\langle m_\Delta, w_E \rangle$, and toric divisors attain the bound.

### Examples

**Example 3.6.11 (the quotients $\frac12(1,1)$ and $\frac13(1,1)$).** Let $\sigma_n = \operatorname{Cone}(e_2, n e_1 - e_2)$, the cone of $\frac1n(1,1)$ (Example 3.5.17), and $\Delta = 0$. By Example 3.3.38, $m_{\sigma_n} = (2/n, 1)$, and $\langle m, (x, y) \rangle = 2x/n + y$. A point of $\operatorname{int}(\sigma_n)$ is $\alpha e_2 + \beta (n e_1 - e_2)$ with $\alpha, \beta > 0$, that is $(x, y) = (n\beta, \alpha - \beta)$, and $\langle m, (x, y) \rangle = \alpha + \beta$. For a lattice point, $\beta = x/n \ge 1/n$ and $\alpha = (ny + x)/n$ with $ny + x$ a positive integer, so $\alpha + \beta \ge 2/n$, with equality at $e_1 = (1, 0)$. So

$$\operatorname{mld}(\gamma; U_{\sigma_2}) = 1, \qquad \operatorname{mld}(\gamma; U_{\sigma_3}) = \tfrac23,$$

attained by the exceptional curve of the minimal resolution, the divisor $E_{e_1}$ of Example 3.5.17. For $n = 2$ this is the quadric cone, the $A_1$ singularity, which is canonical; for $n = 3$ it is klt and not canonical. In both cases $\operatorname{mld} = a(E_{e_1}) + 1 = 2/n$, as Example 3.3.38 computed.

**Example 3.6.12 (smooth points, $\frac12(1,1,1)$ and the cone over a square).**

- For $\sigma = \operatorname{Cone}(e_1, \dots, e_n)$ and $N = \mathbb{Z}^n$, $m_\Delta = (1 - d_1, \dots, 1 - d_n)$, and the minimum over $v \in \mathbb{Z}^n_{\ge 1}$ is at $v = (1, \dots, 1)$: $\operatorname{mld}(0; \mathbb{A}^n, \sum d_i D_i) = n - \sum_i d_i$. For $\Delta = 0$ it is $n$, attained by the blow-up of the origin.
- For $\frac12(1,1,1)$, with $N = \mathbb{Z}^3 + \mathbb{Z} \cdot \frac12(1,1,1)$ and $\sigma = \operatorname{Cone}(e_1, e_2, e_3)$, the value of $m = (1,1,1)$ at $v$ is $v_1 + v_2 + v_3$. The interior lattice points are $\frac12(1,1,1) + w$ with $w \in \mathbb{Z}^3_{\ge 0}$ and the points of $\mathbb{Z}^3_{\ge 1}$, so the minimum is $\frac32$, at $\frac12(1,1,1)$. So $\operatorname{mld} = \frac32$, and the pair is terminal at the point, as in Example 3.3.40.
- For the cone over a square, $m = (0, 0, 1)$ (Example 3.3.39). The lattice points with $z = 1$ are the four vertices, which are on the boundary, and $(1, 1, 2)$ lies in the interior. So $\operatorname{mld} = 2$, attained by the blow-up of the vertex, which here is $E_{(1,1,2)}$. This cone is not simplicial, and the theorem applies because $K$ is Cartier.

**Example 3.6.13 (the toric $K$-MMPs of $\mathbb{F}_1$).** Let $X = \mathbb{F}_1$ with the rays $u_1 = (1, 0)$, $u_2 = (0, 1)$, $u_3 = (-1, 1)$, $u_4 = (0, -1)$ of Example 3.5.7 with $n = 1$. The wall relations are $u_1 + u_3 - u_2 = 0$ at $u_2$ and $u_2 + u_4 = 0$ at $u_1$ and $u_3$, so $NE(X)$ has the two extremal rays spanned by the curve $D_2$, with $D_2^2 = -1$ and $K \cdot D_2 = -(1 + 1 - 1) = -1$, and by the fibre $f = D_1$, with $K \cdot f = -(1 + 1) = -2$. Both are $K$-negative.

- The ray of $D_2$ has $J_- = \{u_2\}$, so it is divisorial. Its contraction removes $u_2$, and the remaining rays satisfy $u_1 + u_3 + u_4 = 0$: the result is $\mathbb{P}^2$. There $\rho = 1$, the only extremal ray has $K \cdot \ell = -3$ and empty $J_-$, and the program ends with the Mori fibre space $\mathbb{P}^2 \to \mathrm{pt}$.
- The ray of $f$ has $J_- = \emptyset$, so its contraction $\mathbb{F}_1 \to \mathbb{P}^1$ is of fibre type, and the program ends at once with this Mori fibre space.

These are the two toric $K$-MMPs of $\mathbb{F}_1$, and both end with a Mori fibre space, as Corollary 3.6.9 says.

### Proof

*Proof of Theorem 3.6.8.* Part 1, existence of a ray. Since $X_k$ is projective and $\Sigma_k$ complete simplicial, $NE(X_k)$ is a closed rational polyhedral cone that contains no line, spanned by the classes of the wall curves (Theorem 3.4.21). If $D_k$ is not nef, then $D_k \cdot V(\tau) < 0$ for some wall $\tau$ (Theorem 3.4.21, the description of $\operatorname{Nef}(X_k)$). A polyhedral cone that contains no line is the sum of its one-dimensional faces; this is the standard fact of convex geometry behind Exercise 4 of Section 1 of Chapter 1. So $[V(\tau)]$ is a sum of vectors in the extremal rays of $NE(X_k)$, and $D_k$ is negative on one of them. That ray is $R_k$.

Part 1, the new model. If $\pi_k$ is divisorial, $X_{k+1} = Z_k = X_{\Sigma_{R_k}}$ is projective (Theorem 3.5.6, part 2), $\Sigma_{R_k}$ is simplicial with the rays $\Sigma_k(1) \setminus \{\rho\}$ for the one ray $\rho$ in $J_-$, and $\rho(Z_k) = \rho(X_k) - 1$ (Theorem 3.5.15, part 4). The pushforward of a torus-invariant divisor deletes the coefficient of the contracted divisor $D_\rho$, so $D_{k+1}$ is torus-invariant, and it is $\mathbb{Q}$-Cartier since $\Sigma_{R_k}$ is simplicial (Theorem 3.3.20). If $\pi_k$ is small, $\Sigma_{k+1}$ is complete simplicial with the same rays, $X_{k+1}$ is projective, and $\rho(X_{k+1}) = \rho(X_k)$ (Theorem 3.5.20, parts 1, 2 and 4). In both cases $X_{k+1}$ is $\mathbb{Q}$-factorial by Theorem 3.3.20.

Part 2. A contraction of fibre type has $\dim Z_k < n$ by definition, and it contracts exactly the curves with class in $R_k$ (Theorem 3.5.6, part 3). For relative ampleness, argue as in the proof of part 4 of Theorem 3.5.20. Let $P$ be a supporting divisor of $R_k$ (Lemma 3.5.4) and $A$ the ample divisor on $Z_k$ with $\pi_k^* A \sim_{\mathbb{Q}} P$ (Theorem 3.5.6, part 2). The divisor $-D_k$ is positive on the $R_k$-walls, where $P$ vanishes, and $P$ is positive on the other walls. For $t_0$ large, $t_0 P - D_k$ is positive on every wall, so its support function is strictly convex (Theorem 3.4.13) and it is ample (Cox-Little-Schenck, Theorem 6.1.14). So $-D_k$ is an ample divisor minus the pullback of $t_0 A$, and it is $\pi_k$-ample (Lazarsfeld, Section 1.7).

Part 3. The number of rays drops by one at each divisorial step and is unchanged at each small step. Every model is complete, and a complete fan in $N_{\mathbb{R}}$ has at least $n + 1$ rays, so there are at most $|\Sigma(1)| - n - 1$ divisorial steps. By Theorem 3.4.20 this number is $\rho(X) - 1$. Between two divisorial steps, and after the last one, the steps are flips of $D_k$-negative small rays, and there are finitely many of them by Theorem 3.6.3. So the sequence is finite. A finite sequence stops only in cases 1 and 2 of the rule, by part 1.

Part 4. By Theorem 3.3.26, $K_{X_k} = -\sum_{\rho \in \Sigma_k(1)} D_\rho$ on every $X_k$. If $D_k = K_{X_k} + \Delta_k$ with $\Delta_k = \sum d_\rho D_\rho$, then $D_k = \sum_\rho (d_\rho - 1) D_\rho$. A divisorial step deletes the term of the contracted ray, and a flip keeps all terms with the same coefficients, so $D_{k+1} = \sum_{\rho \in \Sigma_{k+1}(1)} (d_\rho - 1) D_\rho = K_{X_{k+1}} + \Delta_{k+1}$. $\square$

*Proof of Corollary 3.6.9.* By part 3 of Theorem 3.6.8 the program ends, and by part 4 its last divisor is $D_m = \sum_\rho (d_\rho - 1) D_\rho$ on $X_m$, a torus-invariant divisor whose coefficients are all negative. Suppose $D_m$ were nef. Let $H$ be an ample divisor on $X_m$; then $D_m \cdot H^{n-1} \ge 0$, since the intersection of a nef divisor with $n - 1$ ample ones is a limit of degrees of curves. But $-D_m$ is a nonzero effective divisor, and $(-D_m) \cdot H^{n-1}$ is a positive combination of the degrees $D_\rho \cdot H^{n-1} > 0$ of the components, so $D_m \cdot H^{n-1} < 0$. So $D_m$ is not nef, and the program ends with a Mori fibre space. For $\Delta = 0$ this is the $K$-MMP. $\square$

*Proof of Theorem 3.6.10.* Choose a basis $m_1, \dots, m_n$ of $M$ and let $\omega = \bigwedge_i d\chi^{m_i} / \chi^{m_i}$. By Theorem 3.3.26 its divisor on any toric variety with lattice $N$ is $-\sum_\rho D_\rho$, the sum over all rays. Fix $r \ge 1$ with $r m_\Delta \in M$; it exists because $K_U + \Delta$ is $\mathbb{Q}$-Cartier (Theorem 3.3.20 and Theorem 3.3.12). By Proposition 3.3.3, on $U$

$$K_U + \Delta = \operatorname{div}(\omega) + \Delta = \sum_\rho (d_\rho - 1) D_\rho = -\tfrac1r \operatorname{div}(\chi^{r m_\Delta}),$$

with $K_U$ represented by $\operatorname{div}(\omega)$.

Let $E$ be a prime divisor over $U$, realized on a normal variety $Y$ with a proper birational morphism $f \colon Y \to U$, and $v_E$ its valuation of the function field $k(U) = k(Y)$. Represent $K_Y$ by $\operatorname{div}_Y(f^* \omega)$. This is the same choice as in the proof of Theorem 3.3.34: $f$ is birational, so $\omega$ is a rational $n$-form on $Y$, and $f_* \operatorname{div}_Y(\omega) = \operatorname{div}_U(\omega)$. Then $f^*(K_U + \Delta) = -\frac1r \operatorname{div}_Y(\chi^{r m_\Delta})$, and the coefficient of $E$ in $K_Y - f^*(K_U + \Delta)$ is

$$a(E, U, \Delta) = \operatorname{ord}_E(\omega) + \langle m_\Delta, w_E \rangle, \qquad (\ast)$$

where $w_E \in N$ is defined by $\langle m, w_E \rangle = v_E(\chi^m)$ for $m \in M$. This $w_E$ is a lattice point: since $\chi^{m + m'} = \chi^m \chi^{m'}$ and $v_E$ is a valuation, $m \mapsto v_E(\chi^m)$ is a homomorphism $M \to \mathbb{Z}$, an element of $\operatorname{Hom}(M, \mathbb{Z}) = N$.

Step 1: $\operatorname{ord}_E(\omega) \ge -1$. At a general point $p$ of $E$, $Y$ is smooth and $E$ is smooth, so there are local coordinates $s, y_2, \dots, y_n$ at $p$ with $E = \{s = 0\}$. Each $\chi^{m_i}$ is a unit of $k(Y)$, and near $p$ one has $f^* \chi^{m_i} = s^{c_i} g_i$ with $c_i = v_E(\chi^{m_i}) \in \mathbb{Z}$ and $g_i$ a unit at $p$, after shrinking. Then

$$\frac{d \chi^{m_i}}{\chi^{m_i}} = c_i \frac{ds}{s} + \frac{dg_i}{g_i},$$

and $dg_i / g_i$ is regular at $p$. In the wedge product of these $n$ forms every term has at most one factor $ds/s$, since $ds/s \wedge ds/s = 0$. So $s \cdot f^* \omega$ is regular at $p$, and $\operatorname{ord}_E(\omega) \ge -1$. This is the computation in the proof of the logarithmic bound of Volume 4 (Lemma 4.2.11), with the characters in place of the coordinates.

Step 2: $w_E \in \operatorname{int}(\sigma)$ if the centre of $E$ is $\gamma_\sigma$. The centre of $E$ on $U$ is the closure of $f(\eta_E)$, where $\eta_E$ is the generic point of $E$. It lies in $U$, so $v_E \ge 0$ on $k[U] = k[\sigma^\vee \cap M]$, and it is the closed point $\gamma_\sigma$, so $v_E > 0$ on the ideal of $\gamma_\sigma$. Since $\dim \sigma = n$, $\sigma^\perp = 0$, and $\gamma_\sigma$ is the point at which $\chi^0 = 1$ and every $\chi^m$ with $0 \neq m \in \sigma^\vee \cap M$ vanishes (Chapter 2, Section 4); so the ideal of $\gamma_\sigma$ is spanned by these $\chi^m$. So $\langle m, w_E \rangle \ge 1$ for every nonzero $m \in \sigma^\vee \cap M$, and in particular $w_E \in (\sigma^\vee)^\vee = \sigma$ (Theorem 3.1.3). If $w_E$ were on the boundary of $\sigma$, it would lie in a proper face $\tau$. By Proposition 3.1.4, part 5, the dual face $\tau^* = \sigma^\vee \cap \tau^\perp$ has dimension $n - \dim \tau > 0$, and it is rational by part 1 applied to the rational cone $\sigma^\vee$, so it contains some $m \in M$, $m \neq 0$. Then $\langle m, w_E \rangle = 0$, a contradiction. So $w_E \in \operatorname{int}(\sigma) \cap N$.

Part 1 now follows from $(\ast)$ and Steps 1 and 2: $a(E, U, \Delta) + 1 \ge \langle m_\Delta, w_E \rangle$.

Part 2. Let $v \in \operatorname{int}(\sigma) \cap N$ be primitive and $\Sigma^*(v)$ the star subdivision at $v$ of the fan of the faces of $\sigma$ (Definition 3.1.28), with $f \colon Y = X_{\Sigma^*(v)} \to U$ (Corollary 3.2.39). The divisor $E_v = D_v$ is a prime divisor on $Y$. By Proposition 3.3.3, $v_{E_v}(\chi^m) = \langle m, v \rangle$, so $w_{E_v} = v$, and $\operatorname{ord}_{E_v}(\omega) = -1$ by Theorem 3.3.26. So $(\ast)$ gives $a(E_v, U, \Delta) + 1 = \langle m_\Delta, v \rangle$. The smallest cone of $\sigma$ that contains the ray of $v$ is $\sigma$, since $v$ is interior, so $f$ maps the orbit $O(\operatorname{Cone}(v))$, which is dense in $E_v$, into $O(\sigma) = \{\gamma_\sigma\}$ (Theorem 3.2.37, part 3). So the centre of $E_v$ is $\gamma_\sigma$.

Part 3. For $v \in \sigma$ write $v = \sum_\rho \lambda_\rho u_\rho$ with $\lambda_\rho \ge 0$; then $\langle m_\Delta, v \rangle = \sum_\rho \lambda_\rho (1 - d_\rho) \ge 0$. The values $\langle m_\Delta, v \rangle$ for $v \in N$ lie in $\frac1r \mathbb{Z}$, so the set of values on $\operatorname{int}(\sigma) \cap N$, which is nonempty since $\dim \sigma = n$, is a nonempty set of nonnegative elements of $\frac1r \mathbb{Z}$, and it has a minimum $\mu$. If $v = t v_0$ with $v_0$ primitive and $t \ge 1$ an integer, then $v_0 \in \operatorname{int}(\sigma)$ and $\langle m_\Delta, v \rangle = t \langle m_\Delta, v_0 \rangle \ge \langle m_\Delta, v_0 \rangle$, so $\mu$ is attained at a primitive vector. By part 1, every $E$ with centre $\gamma_\sigma$ has log discrepancy at least $\mu$, and by part 2 the divisor $E_{v_0}$ for a primitive $v_0$ attaining $\mu$ has log discrepancy $\mu$. So the infimum of Definition 1.1.20 is the minimum $\mu$. $\square$

### Exercises

1. (A) Use Theorem 3.6.10 to compute the mld at the fixed point of $\frac15(1,2)$, the cone $\operatorname{Cone}(e_2, 5 e_1 - 2 e_2)$, and find the divisor that attains it.
2. (A) Let $\Delta = d_1 D_1 + d_2 D_2$ on $U_{\sigma_2}$, the quadric cone. Compute $m_\Delta$ and $\operatorname{mld}(\gamma; U, \Delta)$ as a function of $d_1, d_2 \in [0, 1]$.
3. (B) Show that a divisorial step of a toric $D$-MMP contracts the divisor $D_\rho$ of the ray $\rho \in J_-$, and that $D_\rho \cdot R < 0$. Deduce that if $D$ is effective and $D \cdot R < 0$ for a divisorial ray $R$, then the coefficient of $D$ at the contracted divisor is positive.
4. (B) Run all toric $K$-MMPs of the blow-up of $\mathbb{P}^2$ at its three fixed points, and list their outcomes.
5. (B) Let $X = X_\Sigma$ be complete simplicial with $K$ $\mathbb{Q}$-Cartier. Use part 1 of Theorem 3.6.10 to prove part 2 of Theorem 3.3.36 for those divisors $E$ over $X$ whose centre is a torus-fixed point.
6. (C) Show that if $D$ is big, every toric $D$-MMP ends with a minimal model. (Hint: bigness is kept by the steps, and the restriction of a big divisor to a general fibre of a fibre type contraction is big.)

### Lean

- Status: the theorem is stated and not proved. `MinimalModel.ToricMMP` in `MinimalModel/Statements/ToricMMP.lean` is a `Prop` with no proof in the library. The vocabulary is in `MinimalModel/Toric/Program.lean`: `MinimalModel.Toric.ToricModel` (a fan with a divisor), `MinimalModel.Toric.IsToricStep` and `MinimalModel.Toric.IsToricMoriFibreSpace`. The cone theorem it rests on, Theorem 3.4.13, is proved as `MinimalModel.Toric.Fan.coneTheorem`; the contractions, flips and termination of Chapter 5 and Section 1 are not.
- Fidelity: the Lean statement takes a complete simplicial projective fan `F` (`F.IsSimplicialFan`, `F.IsProjectiveFan`) and a torus-invariant divisor `D` with rational coefficients. It has two parts: no infinite sequence of toric steps starts at `(F, D)`; and at the last model of each finite sequence of steps, `D` is nef (`F.IsNef D`), or the model is a toric Mori fibre space for `D`, or one more step exists. Together these say that each program ends with a minimal model or a Mori fibre space, which is part 3 of Theorem 3.6.8. It is a statement on fans only. Nef means a convex support function, ample over a base means strict convexity on the cones of the base, and a Mori fibre space is a refinement of a quasi-fan with a cone that is not strongly convex, of relative Picard number one, over which $-D$ is ample. The scheme $X_\Sigma$ is not built in the library, so the statement does not mention varieties, curves or $\mathbb{Q}$-factoriality, and the equivalence of these fan conditions with the geometric ones is the content of Chapters 4 and 5, not of the Lean statement. The step relation `IsToricStep` records the conclusions of Theorems 3.5.15 and 3.5.20 rather than constructing the steps.
- The mld formula, Theorem 3.6.10, is in the statement of node MMAWP4SA44 but not in the Lean statement: its docstring says that comparing with `mld` of `Basic.lean` needs the toric variety as a scheme, so this part is not stated.
- Node MMAWP4SA44 (toric-mmp) is Theorem 3.6.8 with Theorem 3.6.10. Its map entry uses the toric cone theorem MM6EHAYFKV of Chapter 4.

### Notes and history

Reid (1983) set up the toric minimal model program for $K_X$ on a projective toric variety with terminal singularities and proved that it ends; Fujino and Sato (2004, Section 3 and Remark 3.3) state it for an arbitrary $\mathbb{Q}$-divisor $D$, relative to a projective toric morphism, and prove it with the cone theorem, the contraction theorem, the flip and the termination of Section 1 (their Theorems 4.1, 4.5, 4.8 and 4.9). Their Remark 3.2 stresses that the toric program works for every $\mathbb{Q}$-divisor. Cox-Little-Schenck give the program in Chapter 15. The proof of Theorem 3.6.8 here is assembled from the earlier chapters of this volume. The formula for the mld at a fixed point is a direct computation from the canonical form of Theorem 3.3.26, and the proof here was written for the handbook. The docstring of the Lean statement attributes the formula to Ambro; the handbook has not read Ambro's paper. Fujino and Sato, Proposition 2.10, prove that $(X, \sum_i a_i D_i)$ is log canonical, respectively klt, when $K_X + \sum a_i D_i$ is $\mathbb{Q}$-Cartier with all $0 \le a_i \le 1$, respectively $< 1$; Theorem 3.6.10 recovers this at the fixed points, since $\langle m_\Delta, v \rangle \ge 0$ on $\sigma$, with $\langle m_\Delta, v \rangle > 0$ on $\operatorname{int}(\sigma)$ when all $d_\rho < 1$.
