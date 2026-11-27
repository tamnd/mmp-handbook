---
title: The Riemann-Roch theorem
nodes: []
sources: [Har77, Vak25, Ful69]
reads_with: [Har77:IV.1, Vak25:ch19]
requires: [P3.9, P3.10, P3.12, P4.3, P4.7, P5.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Riemann-Roch theorem

### Statement

In this section $k$ is algebraically closed and $C$ is a smooth projective curve over $k$. For a divisor $D$ on $C$ write $\ell(D) = h^0(C, \mathcal{O}_C(D))$, so that $|D|$ is a projective space of dimension $\ell(D) - 1$ (Theorem P3.10.3). The *genus* of $C$ is
$$g = g(C) = h^1(C, \mathcal{O}_C),$$
which is the arithmetic genus $p_a(C)$ of Definition P4.3.9, since $h^0(C, \mathcal{O}_C) = 1$ (Example P3.4.27). The canonical sheaf is $\omega_C = \Omega_{C/k}$, an invertible sheaf since $C$ is smooth of dimension $1$ (Corollary P3.12.11), and a *canonical divisor* is any divisor $K$ with $\mathcal{O}_C(K) \cong \omega_C$. For a nonzero rational differential $\eta$, the divisor $\operatorname{div}(\eta) = \sum_P v_P(\eta / dt_P) P$, with $t_P$ a local parameter at $P$, is a canonical divisor, and all canonical divisors arise in this way.

**Theorem P5.1.10 (Riemann-Roch).** For every divisor $D$ on $C$,
$$\ell(D) - \ell(K - D) = \deg D + 1 - g.$$

Lean: not in Lean as stated.

**Corollary P5.1.11.** Let $C$ have genus $g$.

1. $\ell(K) = g$ and $\deg K = 2g - 2$.
2. If $\deg D > 2g - 2$, then $h^1(C, \mathcal{O}_C(D)) = 0$ and $\ell(D) = \deg D + 1 - g$.
3. If $\deg D = 2g - 2$ and $\ell(D) = g$, then $D \sim K$.
4. For every point $P$, $\ell(D) - 1 \leq \ell(D - P) \leq \ell(D)$.

Lean: not in Lean as stated.

**Proposition P5.1.12 (curves of genus $0$).** The following are equivalent:

1. $g(C) = 0$;
2. there are two distinct points $P \neq Q$ of $C$ with $P \sim Q$;
3. $C \cong \mathbb{P}^1$.

Lean: not in Lean as stated.

**Proposition P5.1.13 (curves of genus $1$).** Let $g(C) = 1$ and fix a point $O \in C$.

1. $K \sim 0$, so $\omega_C \cong \mathcal{O}_C$.
2. Every divisor of degree $1$ is linearly equivalent to exactly one point. The map $P \mapsto [P - O]$ is a bijection from the points of $C$ to $\operatorname{Pic}^0(C)$, the group of classes of degree $0$.
3. The linear system $|3O|$ embeds $C$ as a smooth plane cubic, and $|2O|$ is a morphism $C \to \mathbb{P}^1$ of degree $2$.

Lean: not in Lean as stated.

**Proposition P5.1.14 (gonality).** Every curve of genus $g$ has a nonconstant morphism to $\mathbb{P}^1$ of degree at most $g + 1$.

Lean: not in Lean as stated.

### Proof in words

The first form of Riemann-Roch in P4 Ch. 3 computes $h^0 - h^1$. Serre duality on a smooth projective curve says that $H^1(\mathcal{O}_C(D))$ is dual to $H^0(\omega_C(-D))$. Putting the two together gives the classical formula, in which the correction term is the dimension of the space of differentials vanishing on $D$. With $D = K$ the formula computes $\deg K$. With $\deg D$ large, $K - D$ has negative degree and no sections, so Riemann-Roch becomes an equality. A curve with two linearly equivalent points has a rational function with one simple pole, which is an isomorphism to $\mathbb{P}^1$. On a curve of genus $1$, divisors of degree $1$ have exactly one section, which identifies points with divisor classes.

### Examples

**Example P5.1.15 (the projective line).** On $\mathbb{P}^1$ with coordinate $x$, the differential $dx$ has no zeros or poles on $\mathbb{A}^1$, and at $\infty$ with parameter $u = 1/x$, $dx = -u^{-2} du$. So $K = -2 \infty$ and $\deg K = -2 = 2g - 2$ with $g = 0$, and $\omega_{\mathbb{P}^1} \cong \mathcal{O}(-2)$, as Corollary P3.12.22 says.

**Example P5.1.16 (plane curves).** Let $C \subseteq \mathbb{P}^2$ be a smooth curve of degree $d$ and $H$ a line section. By Example P4.7.23, $\omega_C \cong \mathcal{O}_C(d - 3)$, so $K \sim (d - 3) H$ and $g = (d - 1)(d - 2)/2$. As a check, $\deg K = d(d - 3) = 2g - 2$. Concretely, for $C = V(F)$ with affine equation $f(x, y) = 0$ and $f_y = \partial f / \partial y$, the differential $\eta = dx / f_y$ has no zeros or poles in the affine part, and the differentials $h \, dx / f_y$, with $h$ a polynomial of degree at most $d - 3$, are a basis of $H^0(C, \omega_C)$ when the line at infinity is transverse to $C$. These are the *adjoint* differentials of the classical theory, and there are $\binom{d - 1}{2}$ of them.

**Example P5.1.17 (a cubic and its group law).** Let $C$ be a smooth plane cubic and $O \in C$. By Proposition P5.1.13, $C(k) \cong \operatorname{Pic}^0(C)$ via $P \mapsto [P - O]$, which makes $C$ a group with identity $O$. Three points $P, Q, R$ are collinear if and only if $P + Q + R \sim H$, so for $O$ a flex point, with $3 O \sim H$, the relation $P + Q + R = 0$ in the group holds exactly when $P, Q, R$ are collinear. This is the chord and tangent law. Chapter 4 proves that it is a morphism $C \times C \to C$.

**Example P5.1.18 (a hyperelliptic curve).** Let $k$ have characteristic not $2$ and $C$ be the smooth projective curve of $y^2 = f(x)$, with $f$ of degree $2g + 2$ without repeated roots, $g \geq 1$ (Exercise 5 of Section 1.1). The function $x \colon C \to \mathbb{P}^1$ has degree $2$, with two points $\infty_1, \infty_2$ over $\infty$. The differential $\eta = dx / y$ is regular and nonzero on the affine part: where $y \neq 0$, $x$ is a local parameter, and where $y = 0$, $y$ is a local parameter and $dx = 2y \, dy / f'(x)$, with $f'(x) \neq 0$. At $\infty_i$, with $u = 1/x$, $dx = -u^{-2} du$ and $v(y) = -(g + 1)$, so $v(\eta) = -2 + g + 1 = g - 1$. Hence $K = \operatorname{div}(\eta) = (g - 1)(\infty_1 + \infty_2)$, and $\deg K = 2g - 2$. The differentials $x^i \, dx / y$ for $0 \leq i \leq g - 1$ are regular, since $x^i$ has a pole of order $i \leq g - 1$ at each $\infty_j$, and they are linearly independent. By Corollary P5.1.11 they are a basis of $H^0(C, \omega_C)$.

### Proof

*Theorem P5.1.10.* By Theorem P4.3.16, $h^0(\mathcal{O}_C(D)) - h^1(\mathcal{O}_C(D)) = \deg D + 1 - g$. The curve $C$ is smooth and projective over the perfect field $k$, so Corollary P4.7.21 with $n = 1$ and $\mathcal{E} = \mathcal{O}_C(D)$ gives
$$H^1(C, \mathcal{O}_C(D)) \cong H^0(C, \mathcal{O}_C(-D) \otimes \omega_C)' = H^0(C, \mathcal{O}_C(K - D))'.$$
So $h^1(\mathcal{O}_C(D)) = \ell(K - D)$, which is the theorem.

The description of canonical divisors by differentials: $\Omega_{K(C)/k}$ is a one-dimensional $K(C)$-vector space, the stalk of $\omega_C$ at the generic point, and at a point $P$ with parameter $t_P$, the stalk $\omega_{C, P}$ is free with basis $dt_P$ (Theorem P3.12.9). A nonzero rational section $\eta$ of $\omega_C$ is a nonzero element of $\Omega_{K(C)/k}$, and $\eta / dt_P \in K(C)$ has a valuation at $P$. As for any invertible sheaf, the divisor of a rational section satisfies $\mathcal{O}_C(\operatorname{div}(\eta)) \cong \omega_C$ (Theorem P3.9.4), and two rational sections differ by a rational function, so their divisors differ by a principal divisor.

*Corollary P5.1.11, part 1.* With $D = 0$, $\ell(0) = 1$ and Riemann-Roch gives $1 - \ell(K) = 1 - g$, so $\ell(K) = g$. With $D = K$, $\ell(K) - \ell(0) = \deg K + 1 - g$, so $g - 1 = \deg K + 1 - g$.

*Part 2.* If $\deg D > 2g - 2$, then $\deg(K - D) < 0$ and $\ell(K - D) = 0$ by part 2 of Corollary P4.3.17. So $h^1(\mathcal{O}_C(D)) = \ell(K - D) = 0$, and Riemann-Roch gives the formula.

*Part 3.* By Riemann-Roch, $\ell(K - D) = \ell(D) - (2g - 2) - 1 + g = 1$. So $K - D$ is linearly equivalent to an effective divisor of degree $0$, which is $0$.

*Part 4.* The sequence $0 \to \mathcal{O}_C(D - P) \to \mathcal{O}_C(D) \to k(P) \to 0$ gives $0 \to H^0(\mathcal{O}_C(D - P)) \to H^0(\mathcal{O}_C(D)) \to k$, so $\ell(D)$ exceeds $\ell(D - P)$ by $0$ or $1$.

*Proposition P5.1.12.* (1) implies (2): for a point $P$, part 2 of Corollary P5.1.11 gives $\ell(P) = 2$ since $1 > -2$. A nonconstant $h \in H^0(\mathcal{O}_C(P))$ has $\operatorname{div}(h) = Q - P$ for some effective $Q$ of degree $1$, a point, and $Q \neq P$ since $h$ is not constant. (2) implies (3): if $P \sim Q$ with $P \neq Q$, there is $h$ with $\operatorname{div}(h) = Q - P$, so $h \colon C \to \mathbb{P}^1$ has $\operatorname{div}_\infty(h) = P$ of degree $1$. By Corollary P5.1.5, $[K(C) : k(h)] = 1$, so $h$ is birational, hence an isomorphism by Corollary P5.1.5, part 2. (3) implies (1): $h^1(\mathbb{P}^1, \mathcal{O}) = 0$ by Theorem P4.2.1.

*Proposition P5.1.13, part 1.* By Corollary P5.1.11, $\deg K = 0$ and $\ell(K) = 1$, so $K$ is linearly equivalent to an effective divisor of degree $0$, which is $0$.

*Part 2.* Let $D$ have degree $1$. By part 2 of Corollary P5.1.11, $\ell(D) = 1 + 1 - 1 = 1$, so $D \sim P$ for an effective divisor $P$ of degree $1$, a point. If $P \sim P'$ for points $P \neq P'$, Proposition P5.1.12 would give $g = 0$. So $P$ is unique. For a class $\xi$ of degree $0$, $\xi + [O]$ has degree $1$ and is the class of exactly one point $P$, with $[P - O] = \xi$.

*Part 3.* For $\deg D = n \geq 1$, $\ell(D) = n$. Base point freeness and very ampleness are proved in Section 1.3 (Corollary P5.1.20): $3O$ has degree $3 = 2g + 1$, so it is very ample and embeds $C$ in $\mathbb{P}^{\ell(3O) - 1} = \mathbb{P}^2$ as a curve of degree $3$, which is smooth since $C$ is. The divisor $2O$ has degree $2 = 2g$, so it is base point free, and gives a morphism to $\mathbb{P}^1$ of degree $2$.

*Proposition P5.1.14.* Let $D = P_1 + \dots + P_{g+1}$ be a sum of $g + 1$ points. By Riemann-Roch, $\ell(D) \geq g + 1 + 1 - g = 2$, so there is a nonconstant $h$ with $\operatorname{div}_\infty(h) \leq D$. By Corollary P5.1.5, $h \colon C \to \mathbb{P}^1$ has degree $\deg \operatorname{div}_\infty(h) \leq g + 1$.

### Exercises

1. (A) Use Riemann-Roch to show that a smooth plane curve of degree $4$ has genus $3$ and that its canonical divisors are its line sections.
2. (A) Compute $\ell(nP)$ for every $n \geq 0$ on a curve of genus $1$, and show that $1$ is the only gap: $\ell(nP) = \ell((n - 1)P)$ only for $n = 1$.
3. (B) Let $P$ be a point on a curve of genus $g \geq 1$. An integer $n \geq 1$ is a *gap* at $P$ if $\ell(nP) = \ell((n - 1)P)$. Show that there are exactly $g$ gaps, all in $[1, 2g - 1]$.
4. (B) Let $C$ be the hyperelliptic curve of Example P5.1.18 and $D = \infty_1 + \infty_2$. Compute $\ell(nD)$ for all $n \geq 0$ and find a basis of $H^0(C, \mathcal{O}_C(nD))$ in terms of $x$ and $y$.
5. (B) Show that a curve $C$ of genus $g$ has $\ell(D) \leq \deg D$ for every divisor $D$ of degree $\geq 1$ unless $C \cong \mathbb{P}^1$.
6. (C) Let $k$ have characteristic $p > 0$ and $C$ a smooth projective curve. Show that $d \colon K(C) \to \Omega_{K(C)/k}$ kills $K(C)^p$, and compute $\operatorname{div}(dx)$ for $x \colon C \to \mathbb{P}^1$ of degree $p$ purely inseparable. Explain why $\operatorname{div}(dx)$ is not then described by ramification as in Chapter 2.

### Lean

Mathlib does not have the Riemann-Roch theorem for curves. The handbook adds no `MinimalModel` node here.

### Notes and history

Riemann proved in 1857 that a compact Riemann surface of genus $g$ carries a space of meromorphic functions with poles bounded by $D$ of dimension at least $\deg D + 1 - g$, and his student Roch identified the correction term in 1865 as the space of differentials vanishing on $D$. Dedekind and Weber gave the first algebraic proof in 1882, and F. K. Schmidt extended it to arbitrary perfect fields in 1931. The cohomological form is due to Serre, in *Groupes algébriques et corps de classes* and *Faisceaux algébriques cohérents*. The literature state is theorem. In the minimal model program, Riemann-Roch on curves is used through its consequence $\deg K_C = 2g - 2$, which together with adjunction computes $K_X \cdot C$ for curves on a surface and gives the bound on the length of extremal rays in Volume 7.
