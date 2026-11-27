---
title: Ramification and the Hurwitz formula
nodes: []
sources: [Har77, Vak25, Sil09]
reads_with: [Har77:IV.2, Vak25:ch21]
requires: [P1.7, P1.12, P3.12, P5.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Ramification and the Hurwitz formula

### Statement

In this section $k$ is algebraically closed of characteristic $p \geq 0$, and $f \colon C \to D$ is a nonconstant morphism of smooth projective curves of degree $n$. By Proposition P5.1.4, $f$ is finite. For a point $P \in C$ with $Q = f(P)$, a local parameter $t$ at $Q$ and a local parameter $s$ at $P$, the *ramification index* is $e_P = v_P(f^* t)$. The morphism $f$ is *ramified* at $P$ if $e_P > 1$, *tamely ramified* if in addition $p \nmid e_P$, and *wildly ramified* if $p \mid e_P$. The point $Q$ is a *branch point* if $f$ is ramified at some point over it. The morphism $f$ is *separable* if the extension $K(C) / K(D)$ is separable.

**Proposition P5.2.1 (the relative differentials).** Let $f$ be separable.

1. The sequence $0 \to f^* \omega_D \to \omega_C \to \Omega_{C/D} \to 0$ is exact, and $\Omega_{C/D}$ is a torsion sheaf supported on the ramification points.
2. At a point $P$, $\Omega_{C/D, P}$ has length $v_P(d(f^* t) / ds)$. This length is $e_P - 1$ if $f$ is tamely ramified or unramified at $P$, and at least $e_P$ if $f$ is wildly ramified at $P$.
3. The *ramification divisor* $R = \sum_P \operatorname{length}(\Omega_{C/D, P}) \, P$ satisfies $K_C \sim f^* K_D + R$.

So $f$ has finitely many ramification points.

Lean: not in Lean as stated.

**Theorem P5.2.2 (Hurwitz).** Let $f$ be separable of degree $n$. Then
$$2 g(C) - 2 = n (2 g(D) - 2) + \deg R.$$
If $f$ has only tame ramification, then $\deg R = \sum_P (e_P - 1)$.

Lean: not in Lean as stated.

**Corollary P5.2.3.** Let $f$ be separable of degree $n$.

1. $g(C) \geq g(D)$.
2. If $D = \mathbb{P}^1$ and $n \geq 2$, then $f$ is ramified somewhere. A connected unramified cover of $\mathbb{P}^1$ is an isomorphism.
3. If $g(C) = g(D) \geq 2$, then $f$ is an isomorphism.
4. If $g(D) = 1$ and $f$ is unramified, then $g(C) = 1$. If $g(D) = 1$ and $f$ is ramified, then $g(C) \geq 2$.
5. If $p = 0$ or $p > n$, every ramification is tame and $\sum_{f(P) = Q} (e_P - 1) \leq n - 1$ for every $Q$, so $f$ has at most $2 g(C) - 2 + 2n$ ramification points when $D = \mathbb{P}^1$.

Lean: not in Lean as stated.

### Proof in words

Pulling back a differential from $D$ to $C$ is injective when the function fields are separable, since then $\Omega_{K(C)/K(D)} = 0$. Locally, $f^* t = u s^e$ with $u$ a unit, and $d(f^* t) = (e u + s u') s^{e - 1} ds$. When $p \nmid e$, the factor in parentheses is a unit, and the pulled back differential vanishes to order exactly $e - 1$. So the canonical divisor of $C$ is the pullback of a canonical divisor of $D$ plus the ramification divisor. Taking degrees and using $\deg f^* K_D = n \deg K_D$ gives the formula. The corollaries come from the signs: a cover of degree $n$ multiplies $2g - 2$ by $n$ before adding the nonnegative $\deg R$.

### Examples

**Example P5.2.4 (hyperelliptic curves).** Let $p \neq 2$ and $C$ be the curve of $y^2 = h(x)$ with $h$ of degree $2g + 1$ or $2g + 2$ without repeated roots, with $f = x \colon C \to \mathbb{P}^1$ of degree $2$. The ramification is tame, and $f$ ramifies exactly over the roots of $h$ and, when $\deg h$ is odd, over $\infty$: these are the points with one preimage. That is $2g + 2$ branch points in both cases. Hurwitz gives $2g(C) - 2 = 2 \cdot (-2) + (2g + 2)$, so $g(C) = g$, as Example P5.1.18 found by computing differentials. Conversely, a double cover of $\mathbb{P}^1$ branched at $b$ points has $b$ even and genus $b/2 - 1$.

**Example P5.2.5 (projection of a plane curve).** Let $p = 0$, $C \subseteq \mathbb{P}^2$ a smooth curve of degree $d$, and $O \notin C$. The projection $\pi_O \colon C \to \mathbb{P}^1$ has degree $d$ (Example P5.1.9), and it is ramified at $P$ exactly when the line $OP$ is tangent to $C$ at $P$. Hurwitz gives
$$\deg R = d(d - 3) + 2d = d(d - 1).$$
For a general $O$, every tangent line through $O$ is simply tangent, $e_P = 2$, so there are $d(d - 1)$ tangent lines to $C$ through $O$. This number is the *class* of $C$, the degree of the dual curve. For a conic it is $2$, and for a smooth cubic it is $6$.

**Example P5.2.6 (Fermat curves).** Let $p \nmid d$ and $C = V_+(x^d + y^d + z^d)$, with $f = [x : y] \colon C \to \mathbb{P}^1$ of degree $d$. The fibre over $[a : b]$ is given by $z^d = -(a^d + b^d)$, which has $d$ distinct solutions unless $a^d + b^d = 0$, where it has one solution with $e = d$. There are $d$ such points, so $\deg R = d(d - 1)$ and $2g - 2 = -2d + d(d - 1)$, giving $g = (d - 1)(d - 2)/2$, the genus of a plane curve of degree $d$.

**Example P5.2.7 (Artin-Schreier curves).** Let $p > 0$, $m \geq 1$ prime to $p$, and $C$ the smooth projective curve of $y^p - y = x^m$, with $f = x \colon C \to \mathbb{P}^1$ of degree $p$. The extension $k(x, y)/k(x)$ is separable, since $y^p - y - x^m$ has derivative $-1$ in $y$. For the same reason the affine curve is smooth and $x$ is a local parameter at each of its points, so $f$ is unramified over $\mathbb{A}^1$ and $dx$ has no zeros or poles on the affine part. Over $\infty$, a point $P_\infty$ has $v(x) = -e$ with $e = e_{P_\infty} \leq p$, since $1/x$ is a parameter at $\infty$. Then $v(y) < 0$, so $v(y^p - y) = p \, v(y)$, and $p \, v(y) = m \, v(x) = -me$. Since $p \nmid m$, $p \mid e$, so $e = p$: there is one point over $\infty$, wildly ramified, with $v(x) = -p$ and $v(y) = -m$.

To compute $v(dx)$ at $P_\infty$, choose integers $a, b$ with $-pa - mb = 1$, so that $s = x^a y^b$ is a local parameter, and $p \nmid b$. From $-dy = m x^{m-1} dx$,
$$\frac{ds}{s} = a \frac{dx}{x} + b \frac{dy}{y} = \Big( \frac{a}{x} - \frac{b m x^{m-1}}{y} \Big) dx.$$
The two terms in parentheses have valuations $\geq p$ and exactly $-pm + p + m < p$, so $v(ds) - v(s) = -1 = v(dx) - pm + p + m$. Hence $K_C = \operatorname{div}(dx) = ((p - 1)(m - 1) - 2) P_\infty$ and
$$g(C) = \frac{(p - 1)(m - 1)}{2}.$$
On $\mathbb{P}^1$, $\operatorname{div}(dx) = -2 \infty$, so $R = K_C - f^*(-2\infty)$ has degree $(p - 1)(m + 1)$, concentrated at $P_\infty$, while $e - 1 = p - 1$. A cover of $\mathbb{P}^1$ of degree $p$ with a single branch point can have arbitrarily large genus, which Corollary P5.2.3, part 5, forbids in characteristic $0$.

### Proof

*Proposition P5.2.1, part 1.* By Theorem P3.12.4, part 1, for $C \to D \to \operatorname{Spec} k$ the sequence $f^* \Omega_D \to \Omega_C \to \Omega_{C/D} \to 0$ is exact. Both $f^* \omega_D$ and $\omega_C$ are invertible. At the generic point, $\Omega_{C/D}$ has stalk $\Omega_{K(C)/K(D)}$, which is $0$ by Theorem P1.12.13 since the extension is finite and separable. So $f^* \omega_D \to \omega_C$ is a map of invertible sheaves that is nonzero at the generic point, hence injective, and $\Omega_{C/D}$ is a coherent sheaf with zero generic stalk, hence a torsion sheaf with finite support.

*Part 2.* At $P$, $\omega_{C, P}$ is free on $ds$ and $(f^* \omega_D)_P$ is free on $f^* dt = d(f^* t)$. So $\Omega_{C/D, P} = \mathcal{O}_{C, P} / (g)$ with $g = d(f^* t)/ds$, of length $v_P(g)$. Write $f^* t = u s^e$ with $e = e_P$ and $u$ a unit. Then
$$d(f^* t) = e u s^{e - 1} ds + s^e du = (e u + s \, du/ds) s^{e - 1} ds.$$
If $p \nmid e$, then $e u$ is a unit and $v_P(g) = e - 1$. If $p \mid e$, then $e u = 0$ in $\mathcal{O}_{C, P}$, the first term vanishes, and $v_P(g) = e + v_P(du/ds) \geq e$. In particular the support of $\Omega_{C/D}$ is the set of ramification points.

*Part 3.* Let $\eta$ be a nonzero rational differential on $D$, with $\operatorname{div}(\eta) = K_D$. Then $f^* \eta$ is a nonzero rational differential on $C$ by part 1. At $P$, write $\eta = h \, dt$ near $Q$. Then $f^* \eta = f^*(h) \, g \, ds$, so
$$v_P(f^* \eta) = v_P(f^* h) + v_P(g) = e_P v_Q(h) + v_P(g).$$
Summing over $P$, $\operatorname{div}(f^* \eta) = f^* K_D + R$ by part 2 of Proposition P5.1.4.

*Theorem P5.2.2.* Take degrees in part 3 of Proposition P5.2.1: $\deg K_C = 2g(C) - 2$ and $\deg K_D = 2g(D) - 2$ by Corollary P5.1.11, and $\deg f^* K_D = n \deg K_D$ by Proposition P5.1.4. The tame case is part 2 of Proposition P5.2.1.

*Corollary P5.2.3, part 1.* If $g(D) \geq 1$, then $2g(C) - 2 \geq n(2g(D) - 2) \geq 2g(D) - 2$. If $g(D) = 0$, there is nothing to prove.

*Part 2.* If $f$ is unramified, then $2g(C) - 2 = -2n < 0$, so $g(C) = 0$ and $n = 1$.

*Part 3.* If $g = g(C) = g(D) \geq 2$, then $2g - 2 \geq n(2g - 2)$ forces $n = 1$, so $f$ is birational and an isomorphism by Corollary P5.1.5.

*Part 4.* With $g(D) = 1$, Hurwitz reads $2g(C) - 2 = \deg R$.

*Part 5.* If $p = 0$ or $p > n$, every $e_P \leq n$ is prime to $p$. Over a point $Q$, $\sum_{f(P) = Q} e_P = n$, so $\sum (e_P - 1) = n - \#f^{-1}(Q) \leq n - 1$. When $D = \mathbb{P}^1$, the number of ramification points is at most $\deg R = 2g(C) - 2 + 2n$.

### Exercises

1. (A) Show that a morphism $\mathbb{P}^1 \to \mathbb{P}^1$ of degree $n$ in characteristic $0$ has $2n - 2$ ramification points counted with multiplicity, and find them for $x \mapsto x^n$.
2. (A) Show that a smooth plane cubic in characteristic $0$ has exactly $6$ tangent lines through a general point of $\mathbb{P}^2$, and $4$ through a general point of the cubic itself.
3. (B) Let $f \colon C \to D$ be separable and unramified of degree $n$. Show that $g(C) - 1 = n (g(D) - 1)$, and construct, for every $n$, an unramified cover of degree $n$ of an elliptic curve.
4. (B) Let $G$ be a finite group of automorphisms of a curve $C$ of genus $g \geq 2$ in characteristic $0$, and $D = C/G$. Using Hurwitz, show that $|G| \leq 84 (g - 1)$.
5. (B) Show that in characteristic $0$ a separable cover $C \to \mathbb{P}^1$ of degree $n \geq 2$ has at least two branch points, and that if it has exactly two, then $C \cong \mathbb{P}^1$ and the cover is $x \mapsto x^n$ in suitable coordinates. Compare with Example P5.2.7.
6. (C) Let $f \colon C \to D$ be a Galois cover with group $G$ in characteristic $0$. Show that the ramification indices over a point $Q$ are all equal, to $e_Q$ say, and prove the Riemann-Hurwitz formula in the form $2g(C) - 2 = |G| \big(2 g(D) - 2 + \sum_Q (1 - 1/e_Q)\big)$.

### Lean

Mathlib has Kähler differentials and their exact sequences, but not ramification of curves. The handbook adds no `MinimalModel` node here.

### Notes and history

Riemann used the formula in 1857 to compute the genus of a Riemann surface presented as a branched cover of the sphere, and Hurwitz proved the bound $84(g - 1)$ on automorphism groups in 1893. Wild ramification, which has no analogue over $\mathbb{C}$, was studied by Hasse and Artin in the 1930s; its contribution to $R$ is measured by the higher ramification groups of Hilbert. The literature state is theorem. In the minimal model program the Hurwitz formula reappears as the ramification formula $K_X = f^* K_Y + R$ for finite morphisms in Volume 4, used to show that quotient singularities are klt, and as the canonical bundle formula for fibrations, where the base has a correction term like $\sum_Q (1 - 1/e_Q) Q$ in Exercise 6.
