---
title: Negativity and the termination of toric flips
nodes: []
sources: [CLS11, FS04, KM98, Rei83]
reads_with: [FS04:4, KM98:3.38, CLS11:ch15]
requires: [3.1, 3.3, 3.4, 3.5]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Negativity and the termination of toric flips

### Statement

A flip replaces a $D$-negative curve by a $D$-positive one, and the minimal model program needs a reason why this cannot go on forever. In general the reason is a delicate count of discrepancies. For toric varieties it is a finiteness: a flip does not change the rays of the fan, there are only finitely many simplicial fans on a given set of rays, and a flip can never return to a fan it has left, because it raises the support function of $D$ strictly. This section proves the last point, the toric form of the negativity lemma, and deduces the termination of every sequence of toric $D$-flips.

Throughout, $\Sigma$ is a complete simplicial fan with $X = X_\Sigma$ projective, $D = \sum_\rho a_\rho D_\rho$ is a torus-invariant $\mathbb{Q}$-divisor, and $R$ is a small extremal ray of $NE(X)$ with $D \cdot R < 0$, with relation $b^R$, contraction $\pi \colon X \to Z_R$ and flip $\pi^+ \colon X^+ = X_{\Sigma^+} \to Z_R$ as in Theorem 3.5.20. The divisor $D^+ = \sum_\rho a_\rho D^+_\rho$ is the strict transform. Both $\Sigma$ and $\Sigma^+$ have the rays $\Sigma(1)$, and the support functions $\varphi_D$ of $\Sigma$ and $\varphi_{D^+}$ of $\Sigma^+$ (Definition 3.4.11) take the same value $-a_\rho$ at each $u_\rho$. They differ in between.

**Proposition 3.6.1 (toric negativity).** In this situation:

1. $\varphi_{D^+}(x) \ge \varphi_D(x)$ for every $x \in N_{\mathbb{R}}$.
2. Equality holds at $x$ if and only if $x$ lies in a cone that belongs to both $\Sigma$ and $\Sigma^+$. In particular $\varphi_{D^+} \neq \varphi_D$.
3. Let $C$ be a maximal cone of $\Sigma_R$ of the second kind, with circuit data $(W_C, b^R)$ (Theorem 3.5.15), and let $x \in C$. Write the nonnegative expressions of $x$ in $W_C$ as $\lambda + t b^R$ with $t \in [t_{\mathrm{lo}}, t_{\mathrm{hi}}]$, as in the proof of Lemma 3.5.11. Then
$$\varphi_{D^+}(x) - \varphi_D(x) = (t_{\mathrm{hi}} - t_{\mathrm{lo}}) \cdot \Big( - \sum_\rho a_\rho b^R_\rho \Big).$$

Lean: not yet in Lean.

The name comes from the negativity lemma of the general theory (Kollár-Mori, Lemma 3.38), in the form that Fujino and Sato use for toric varieties (Fujino-Sato, Lemma 4.10). To compare, let $v \in N$ be primitive and let $E_v$ be the divisor over $X$ given by the ray $\mathbb{R}_{\ge 0} v$: the divisor $D_v$ on any toric variety whose fan refines $\Sigma$ and has the ray of $v$, for instance a star subdivision (Definition 3.1.28). If $\mu \colon X_{\tilde\Sigma} \to X$ is such a refinement, the pullback $\mu^* D$ is the torus-invariant divisor with support function $\varphi_D$, so its coefficient at $D_v$ is $-\varphi_D(v)$. This is how a support function records the coefficients of $D$ on all toric divisors over $X$ at once.

**Corollary 3.6.2 (the coefficients go down).** Let $\tilde\Sigma$ be a fan that refines both $\Sigma$ and $\Sigma^+$, with $\mu \colon \tilde X = X_{\tilde\Sigma} \to X$ and $\nu \colon \tilde X \to X^+$ the toric morphisms of Corollary 3.2.39. Then

$$\mu^* D - \nu^* D^+ = \sum_{v} \big( \varphi_{D^+}(v) - \varphi_D(v) \big) \, D_v,$$

the sum over the minimal generators $v$ of the rays of $\tilde\Sigma$. This divisor is effective, it is exceptional over $Z_R$, and it is not zero. If $D = K_X$, then $K_{X^+} = D^+$ and the discrepancies satisfy $a(E_v, X^+) \ge a(E_v, X)$ for every primitive $v \in N$, with strict inequality exactly when $v$ lies in no cone common to $\Sigma$ and $\Sigma^+$.

Lean: not yet in Lean.

A common refinement $\tilde\Sigma$ always exists: the intersections $\delta \cap \delta'$ of a cone of $\Sigma$ and a cone of $\Sigma^+$ form a fan (Exercise 5), and a smooth refinement of it (Theorem 3.1.29) is a common toric resolution, as in Fujino-Sato, Lemma 4.10.

**Theorem 3.6.3 (termination of toric flips).** Let $X_0 = X_{\Sigma_0}$ be projective with $\Sigma_0$ complete simplicial, and $D_0$ a torus-invariant $\mathbb{Q}$-divisor on $X_0$. There is no infinite sequence

$$X_0 \dashrightarrow X_1 \dashrightarrow X_2 \dashrightarrow \cdots$$

in which each $X_k \dashrightarrow X_{k+1}$ is the toric flip of Theorem 3.5.20 of a small extremal ray $R_k$ of $NE(X_k)$ with $D_k \cdot R_k < 0$, and $D_{k+1}$ is the strict transform of $D_k$.

Lean: not yet in Lean. It is the part of `MinimalModel.ToricMMP` that concerns flips; see Section 2.

The theorem is Fujino-Sato, Theorem 4.9, where the flips are called elementary transformations. The divisor $D_0$ is arbitrary: it need not be $K_{X_0}$, need not be effective, and the singularities of $X_0$ play no role. In the general theory, termination of flips is known only in low dimension and for special classes (Volume 1, Section 5 of Chapter 1); the toric case is easy because the set of rays is fixed and finite.

### Proof in words

Inside a circuit cone the two triangulations $T_+$ and $T_-$ choose, for each point $x$, one of the nonnegative expressions $\lambda + t b^R$ of $x$: the side $T_+$ takes the one with the smallest $t$, and $T_-$ the one with the largest (Lemma 3.5.11). The value of a support function at $x$ is the same linear form $\mu \mapsto -\sum a_\rho \mu_\rho$ applied to the chosen expression. Along the segment of expressions this form changes at the rate $-\sum a_\rho b^R_\rho$, which is positive because $D \cdot R < 0$. So $\varphi_{D^+}$, which uses the largest $t$, is at least $\varphi_D$, and it is larger wherever the expression is not unique. That is all of Proposition 3.6.1.

For termination, put the support functions of the $D_k$ in a row. They all take the values $-a_\rho$ at the same rays, and each is at least the one before and different from it. So no two are equal. But each is determined by its fan, all fans are simplicial with the same finite set of rays, and there are only finitely many such fans. An infinite sequence would repeat a fan, and so a support function.

### Examples

**Example 3.6.4 (negativity for the Atiyah flop).** Take the cone over a square of Example 3.5.23: $u_1 = (0,0,1)$, $u_2 = (1,0,1)$, $u_3 = (1,1,1)$, $u_4 = (0,1,1)$, $q = (1, -1, 1, -1)$, and $D = D_2$, so $a = (0, 1, 0, 0)$ and $\sum_i a_i q_i = -1 < 0$. The point $x = (1, 1, 2) = u_1 + u_3 = u_2 + u_4$ has the nonnegative expressions

$$\lambda + t q = (1 + t, \, -t, \, 1 + t, \, -t), \qquad t \in [-1, 0].$$

At $t_{\mathrm{lo}} = -1$ the expression is $u_2 + u_4$, which lies in the cones of $T_+$, and $\varphi_D(x) = -a_2 - a_4 = -1$. At $t_{\mathrm{hi}} = 0$ it is $u_1 + u_3$, in the cones of $T_-$, and $\varphi_{D^+}(x) = -a_1 - a_3 = 0$. The difference $1$ is $(t_{\mathrm{hi}} - t_{\mathrm{lo}}) \cdot 1$, as in part 3. The vector $x$ is primitive, and the star subdivision of $T_+$ at $x$ has the new divisor $E_x$, which lies over the vertex of the cone; it is the exceptional divisor of the blow-up of the curve $C_+ = V_+(\operatorname{Cone}(u_2, u_4))$, since $x = u_2 + u_4$ and $\operatorname{Cone}(u_2, u_4)$ is smooth (Corollary 3.2.39). The coefficient of $E_x$ in the pullback of $D_2$ from $X_+$ is $1$, and in the pullback of $D_2^+$ from $X_-$ it is $0$. On the side $X_+$ the divisor $D_2$ contains $C_+$, and on the side $X_-$ the divisor $D_2^+$ does not contain $C_- = V_-(\operatorname{Cone}(u_1, u_3))$, which is why the coefficient drops. Since $K$ is trivial on both curves, $K_{X_+}$ and $K_{X_-}$ have the same support function: both are $\langle (0,0,1), \cdot \rangle$ on all of the cone, by Example 3.3.39, and a flop changes no discrepancy.

**Example 3.6.5 (discrepancies go up in the Francia flip).** Let $q = (1, 1, -1, -2)$ and $X_\pm$ be as in Example 3.5.24, with $X_+$ smooth and $X_-$ having one point $\frac12(1,1,1)$. There $K \cdot C_+ = 1$ and $K \cdot C_- = -\frac12$, so the $K$-flip goes from $X_-$ to $X_+$. In the notation of this section, the starting fan is $T_-$, the relation of the flipped ray is $-q$, and $D = K$, with $a = (-1, -1, -1, -1)$ and $\sum_i a_i (-q_i) = \sum_i q_i = -1 < 0$. By Theorem 3.3.34 the discrepancy of $E_v$ over a toric variety with $K$ $\mathbb{Q}$-Cartier is $a(E_v) = \varphi_K(v) - 1$, and $\varphi_K(u_i) = 1$.

- The vector $w = u_3 + u_4$ lies in $N$ and has the expressions $(t, t, 1 - t, 1 - 2t)$ with $t \in [0, \frac12]$. At $t = \frac12$ it is $\frac12(u_1 + u_2 + u_3)$, the point of the cone $\operatorname{Cone}(u_1, u_2, u_3)$ of $\frac12(1,1,1)$, and $a(E_w, X_-) = \frac32 - 1 = \frac12$, as in Example 3.3.40. At $t = 0$ it is $u_3 + u_4$ in the smooth cone $\operatorname{Cone}(u_1, u_3, u_4)$ of $X_+$, and $a(E_w, X_+) = 2 - 1 = 1$: $E_w$ is the exceptional divisor of the blow-up of $C_+$.
- The vector $x = u_1 + u_2 = u_3 + 2 u_4$, primitive since in the basis $u_2, u_3, u_4$ it is $(0, 1, 2)$, has the expressions $(1 + t, 1 + t, -t, -2t)$ with $t \in [-1, 0]$. So $a(E_x, X_-) = 2 - 1 = 1$ and $a(E_x, X_+) = 3 - 1 = 2$.

In both cases the discrepancy goes up by $(t_{\mathrm{hi}} - t_{\mathrm{lo}}) \cdot 1$. This is the toric face of the general fact that a $K$-flip raises discrepancies (Kollár-Mori, Lemma 3.38), the fact behind every termination argument of the general theory.

**Example 3.6.6 (a sequence of flips on one set of rays).** Theorem 3.6.3 bounds the length of a sequence of $D$-flips by the number of simplicial fans on the rays of $\Sigma_0$, and in fact by the number of those fans whose support functions for the fixed values $-a_\rho$ form a strictly increasing chain. For the circuit of Example 3.6.4 there are two fans with the support $\operatorname{Cone}(u_1, \dots, u_4)$ and the four rays, $T_+$ and $T_-$, and for each $D$ at most one $D$-flip is possible: from $T_+$ if $\sum a_i q_i < 0$ and from $T_-$ if $\sum a_i q_i > 0$. If $\sum a_i q_i = 0$, $D$ is trivial on both flipping curves and neither side has a $D$-negative small ray.

### Proof

*Proof of Proposition 3.6.1.* Let $x \in N_{\mathbb{R}}$. The fan $\Sigma_R$ is complete, so $x$ lies in a maximal cone $C$ of $\Sigma_R$. If $C$ is of the first kind, it is a cone of $\Sigma$ and of $\Sigma^+$ (Theorem 3.5.15, part 1, and the definition of $\Sigma^+$ in Theorem 3.5.20). Both $\varphi_D$ and $\varphi_{D^+}$ are linear on $C$ with the values $-a_\rho$ at its rays, and $C$ is simplicial, so they agree on $C$. In that case $x$ lies in a common cone and the difference is $0$, which is also what part 3 gives, since then $x$ has one expression.

Let $C$ be of the second kind, with $W_C = \{w_0, \dots, w_n\}$ and $q = b^R$ restricted to $W_C$, which is the circuit relation of $W_C$ because $b^R$ vanishes off the rays in $C$ (Theorem 3.5.15, part 1). Write $a_i$ for the coefficient of $D$ at $w_i$ and $L(\mu) = -\sum_i a_i \mu_i$ for $\mu \in \mathbb{R}^{W_C}$. Let $x \in C$, choose $\lambda \ge 0$ with $x = \sum_i \lambda_i w_i$, and let $t_{\mathrm{lo}} \le 0 \le t_{\mathrm{hi}}$ be as in the proof of Lemma 3.5.11, so that the nonnegative expressions of $x$ are the $\lambda + t q$ with $t \in [t_{\mathrm{lo}}, t_{\mathrm{hi}}]$.

The cones of $\Sigma$ in $C$ are the cones of $T_+(W_C)$ (Theorem 3.5.15, part 1). By the claim in the proof of Lemma 3.5.11, the point $x$ lies in $\operatorname{Cone}(W_C \setminus \{w_j\})$ for some $j \in J_+$ at which $\mu = \lambda + t_{\mathrm{lo}} q$ vanishes, and $\mu$ is then the expression of $x$ in that simplicial cone. The function $\varphi_D$ is linear on this cone with $\varphi_D(w_i) = -a_i$, so $\varphi_D(x) = L(\lambda + t_{\mathrm{lo}} q)$. The cones of $\Sigma^+$ in $C$ are the cones of $T_-(W_C)$, by the definition of $\Sigma^+$. The same claim with the roles of $J_+$ and $J_-$ exchanged, which is the claim for the circuit data $(W_C, -q)$, shows that $x$ lies in $\operatorname{Cone}(W_C \setminus \{w_k\})$ for some $k \in J_-$ at which $\lambda + t_{\mathrm{hi}} q$ vanishes. So $\varphi_{D^+}(x) = L(\lambda + t_{\mathrm{hi}} q)$. Since $L$ is linear,

$$\varphi_{D^+}(x) - \varphi_D(x) = L(\lambda + t_{\mathrm{hi}} q) - L(\lambda + t_{\mathrm{lo}} q) = (t_{\mathrm{hi}} - t_{\mathrm{lo}}) \, L(q),$$

and $L(q) = -\sum_\rho a_\rho b^R_\rho$. This is part 3. By definition of $D \cdot R < 0$ (Theorem 3.5.20, part 4), $\sum_\rho a_\rho b^R_\rho < 0$, so $L(q) > 0$, and since $t_{\mathrm{hi}} \ge t_{\mathrm{lo}}$, the difference is $\ge 0$. This is part 1 on $C$, and $C$ was arbitrary.

Part 2. By part 3 equality holds at $x \in C$ if and only if $t_{\mathrm{hi}} = t_{\mathrm{lo}}$, that is, if and only if $x$ has a unique nonnegative expression in $W_C$. If it does, then $\mu = \lambda + t_{\mathrm{lo}} q$ vanishes at some $j \in J_+$ and at some $k \in J_-$, so $x$ lies in $\operatorname{Cone}(W_C \setminus \{w_j, w_k\})$, which is a cone of both $T_+$ and $T_-$ because it misses an element of $J_+$ and one of $J_-$ (Definition 3.5.10). Conversely, let $x$ lie in a cone $\delta$ that belongs to both $\Sigma$ and $\Sigma^+$. Both $\varphi_D$ and $\varphi_{D^+}$ are linear on $\delta$, and they take the same values $-a_\rho$ at the minimal generators of the rays of the simplicial cone $\delta$, so they agree on $\delta$, and in particular at $x$.

Finally $\varphi_{D^+} \neq \varphi_D$. The cone $C$ of the second kind exists because $R$ has $R$-walls. Its interior contains $x = \sum_i w_i$, whose expressions $\mathbf{1} + t q$ are nonnegative for $t$ in an interval around $0$, so $t_{\mathrm{lo}} < 0 < t_{\mathrm{hi}}$ and the difference at $x$ is positive. $\square$

*Proof of Corollary 3.6.2.* By Corollary 3.2.39 the identity of $N$ gives proper birational toric morphisms $\mu$ and $\nu$. Since $\tilde\Sigma$ refines $\Sigma$, each cone of $\tilde\Sigma$ lies in a cone of $\Sigma$, so $\varphi_D$ is linear on the cones of $\tilde\Sigma$ and is a support function of $\tilde\Sigma$; with Cartier data $m_\sigma$ for $rD$ on $U_\sigma$, the pullback $\mu^*(rD)$ is $\operatorname{div}(\chi^{-m_\sigma})$ on $\mu^{-1}(U_\sigma)$, whose coefficient at $D_v$ is $-\langle m_\sigma, v \rangle$ by Proposition 3.3.3, exactly as in the proof of Theorem 3.3.34. So $\mu^* D = -\sum_v \varphi_D(v) D_v$, and likewise $\nu^* D^+ = -\sum_v \varphi_{D^+}(v) D_v$. Subtracting gives the formula. Its coefficients are $\ge 0$ by part 1 of Proposition 3.6.1. At a ray $v = u_\rho$ of $\Sigma$ the coefficient is $-a_\rho + a_\rho = 0$, so the divisor is supported on the divisors $D_v$ with $v \notin \Sigma(1)$, which are exceptional over $X$, over $X^+$ and so over $Z_R$. It is not zero: $\varphi_{D^+} - \varphi_D$ is linear on each cone of $\tilde\Sigma$, and each cone of $\tilde\Sigma$ is spanned by the minimal generators of its rays, so if the difference vanished at every ray of $\tilde\Sigma$ it would vanish everywhere, against part 2.

For $D = K_X = -\sum_\rho D_\rho$ the strict transform is $-\sum_\rho D^+_\rho = K_{X^+}$ (Theorem 3.3.26). By Theorem 3.3.34, applied to the refinement of $\Sigma$ and of $\Sigma^+$ by a star subdivision at $v$, $a(E_v, X) = \varphi_{K_X}(v) - 1$ and $a(E_v, X^+) = \varphi_{K_{X^+}}(v) - 1$, since $\varphi_K = \langle m_\sigma, \cdot \rangle$ on $\sigma$. Part 1 and part 2 of Proposition 3.6.1 give the inequality and the case of equality. $\square$

*Proof of Theorem 3.6.3.* Suppose the infinite sequence exists. By Theorem 3.5.20, part 1, each $\Sigma_{k+1}$ is a complete simplicial fan with $\Sigma_{k+1}(1) = \Sigma_k(1)$, and by part 4 each $X_{k+1}$ is projective, so the next flip is defined. So all $\Sigma_k$ have the same rays $\Sigma_0(1)$, and $D_k = \sum_\rho a_\rho D_{\rho, k}$ has the coefficients of $D_0$. Let $\varphi_k$ be the support function of $D_k$ on $\Sigma_k$; it is the unique function that is linear on each cone of $\Sigma_k$ and takes the value $-a_\rho$ at $u_\rho$ (Definition 3.4.11).

By Proposition 3.6.1, applied to the flip $X_k \dashrightarrow X_{k+1}$, $\varphi_{k+1} \ge \varphi_k$ everywhere and $\varphi_{k+1} \neq \varphi_k$. Let $k < l$. Then $\varphi_l \ge \varphi_{k+1} \ge \varphi_k$. If $\varphi_l = \varphi_k$, then $\varphi_k \ge \varphi_{k+1} \ge \varphi_k$, so $\varphi_{k+1} = \varphi_k$, which is false. So the $\varphi_k$ are pairwise different, and so are the fans $\Sigma_k$, since $\varphi_k$ is determined by $\Sigma_k$ and the fixed values $-a_\rho$.

A complete simplicial fan with ray set $\Sigma_0(1)$ is determined by its set of maximal cones, and each maximal cone is $\operatorname{Cone}(S)$ for a set $S$ of $n$ of the minimal generators $u_\rho$, $\rho \in \Sigma_0(1)$. So there are at most $2^{\binom{r}{n}}$ such fans, with $r = |\Sigma_0(1)|$. This contradicts the infinitely many different fans $\Sigma_k$. $\square$

This is the proof of Fujino-Sato, Theorem 4.9: there the composite $X_k \dashrightarrow X_l$ for a repeated fan is the identity, and Lemma 4.10 of that paper, the negativity lemma with a common resolution, gives $E \neq 0$ in $\mu^* D_k = \nu^* D_l + E$, a contradiction. The proof above replaces that lemma by Proposition 3.6.1, which is the same statement read on support functions.

### Exercises

1. (A) In Example 3.6.4, show that $\varphi_{D^+} - \varphi_D = \min(x, \, y, \, z - x, \, z - y)$ on the cone $\operatorname{Cone}(u_1, \dots, u_4)$, and that it vanishes exactly on the four facets of the cone, which are the cones common to $T_+$ and $T_-$. (Hint: for $\lambda \ge 0$ the interval of $t$ is $[-\min(\lambda_1, \lambda_3), \min(\lambda_2, \lambda_4)]$.)
2. (A) In Example 3.6.5, find the support functions of $K_{X_-}$ and $K_{X_+}$ on each maximal cone, as linear forms in the basis dual to $u_2, u_3, u_4$.
3. (B) Show that in a sequence of $D$-flips no fan occurs twice, so that the number of flips is less than the number of complete simplicial fans with ray set $\Sigma_0(1)$. For the four rays of the cone over a square, show that there are exactly two simplicial fans with these rays and with support $\operatorname{Cone}(u_1, \dots, u_4)$.
4. (B) Let $(W, q)$ be circuit data and $D = \sum_i a_i D_{w_i}$ with $\sum a_i q_i < 0$. Show that $\varphi_{D^+} - \varphi_D$, restricted to $\operatorname{Cone}(W)$, is the function $x \mapsto (t_{\mathrm{hi}}(x) - t_{\mathrm{lo}}(x)) \cdot (-\sum a_i q_i)$, and that $t_{\mathrm{hi}} - t_{\mathrm{lo}}$ is a concave piecewise linear function on $\operatorname{Cone}(W)$ that vanishes exactly on the cones common to $T_+$ and $T_-$.
5. (C) Let $\Sigma$ and $\Sigma'$ be fans with the same support. Show that the set of the cones $\delta \cap \delta'$, $\delta \in \Sigma$, $\delta' \in \Sigma'$, is a fan that refines both. (Hint: if $F$ is a face of $\delta$ and $F'$ a face of $\delta'$, cut out by $m \in \delta^\vee$ and $m' \in \delta'^\vee$, then $F \cap F'$ is the face of $\delta \cap \delta'$ cut out by $m + m'$. For the converse, show that every face of $\delta \cap \delta'$ has this form.)

### Lean

- Status: not yet in Lean. The library has the support functions of `MinimalModel/Toric/Fan.lean` and the steps `MinimalModel.Toric.IsToricStep` of `MinimalModel/Toric/Program.lean`, but no circuits and no comparison of support functions across a flip.
- Fidelity: in `IsToricStep` the next model has the same coefficients as the old one and the same rays as the base, and $-D$ and $D^+$ are ample over the base in the sense of strict convexity of the support functions on the cones of the base. Part 1 of Proposition 3.6.1 follows from these conditions without circuits. On a cone $C$ of the base, $\varphi_{-D}$ and $\varphi_{D^+}$ are convex in the sense of this handbook, so for every nonnegative expression $x = \sum_i \mu_i w_i$ in the rays of $C$ one has $\varphi_D(x) \le -\sum_i \mu_i a_i \le \varphi_{D^+}(x)$. A Lean proof could take that route. Theorem 3.6.3 is part 1 of the statement `MinimalModel.ToricMMP` restricted to flips, and it is not proved in Lean.
- No node of the map covers this section by itself. The node MMAWP4SA44 (toric-mmp) is the program as a whole, in Section 2.

### Notes and history

The argument is that of Fujino and Sato (2004), Theorem 4.9 and Lemma 4.10. They prove the negativity lemma in general by the standard argument of Kollár-Mori, Lemma 3.38, and use it to show that a repeated fan is impossible. Here the lemma is replaced by its toric content, the comparison of support functions on a circuit cone, which is proved directly from the circuit lemma of Chapter 5. Reid's paper of 1983 contains the toric minimal model program for $D = K_X$; it was not read for this section. Cox-Little-Schenck treat the termination of toric flips in Chapter 15. The counting bound is crude. Its point is that, unlike the general case (Volume 1, Chapter 1, Section 5), no invariant of singularities is needed, and the divisor $D$ can be any $\mathbb{Q}$-divisor.
