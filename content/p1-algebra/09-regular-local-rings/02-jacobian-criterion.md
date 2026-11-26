---
title: The Jacobian criterion
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [Mat86:ch5, Eis95:ch16]
requires: [P1.1, P1.3, P1.4, P1.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Jacobian criterion

### Statement

Throughout, $k$ is a field, $R = k[x_1, \dots, x_n]$, $I = (f_1, \dots, f_r)$ is an ideal of $R$ and $A = R/I$. For a maximal ideal $P$ of $R$ write $L = \kappa(P) = R/P$, a finite extension of $k$ by Zariski's lemma P1.4.28, and $\bar{g}$ for the image of $g \in R$ in $L$. The *Jacobian matrix* of $f_1, \dots, f_r$ at $P$ is the $r \times n$ matrix
$$
J(P) = \left( \overline{\partial f_j/\partial x_i} \right)_{j, i}
$$
with entries in $L$. The partial derivatives are the formal ones, so they make sense over every field. When $P = (x_1 - a_1, \dots, x_n - a_n)$ is the ideal of a rational point $a \in k^n$, the entries are the values $\partial f_j/\partial x_i (a)$.

**Lemma P1.9.11 (differentials at a point).** Let $P$ be a maximal ideal of $R$ such that $L = R/P$ is separable over $k$. Then the map
$$
D : P/P^2 \longrightarrow L^n, \qquad f \longmapsto \left( \overline{\partial f/\partial x_1}, \dots, \overline{\partial f/\partial x_n} \right),
$$
is an isomorphism of $L$-vector spaces. This holds for every maximal ideal when $k$ is perfect, and for the ideal of every rational point over every field.

Lean: not in Mathlib in this form.

*Proof.* For $f \in P$ and $g \in R$, the product rule gives $\partial (gf)/\partial x_i = g\,\partial f/\partial x_i + f\,\partial g/\partial x_i$, and $\bar{f} = 0$. So $D(gf) = \bar{g} D(f)$, and for $g \in P$ this is $0$. Hence $D$ vanishes on $P^2$, and it is a well defined $L$-linear map on the $L$-vector space $P/P^2$. Since $P$ is maximal, elements of $R \setminus P$ act invertibly on $P/P^2$, so $P/P^2 = PR_P/P^2R_P$, which has dimension $n$ over $L$ by the example on affine space in Section 9.1. So it suffices to prove that $D$ is surjective.

Use induction on $n$. For $n = 0$, $P = 0$ and there is nothing to prove. Let $n \geq 1$, $R' = k[x_1, \dots, x_{n-1}]$ and $P' = P \cap R'$. As in the example on affine space, $P'$ is maximal, $L' = R'/P'$ is a subfield of $L$, $L = L'(\bar{x}_n)$, and $P = P'R + gR$, where $g \in R'[x_n]$ is monic in $x_n$ and its image $\bar{g} \in L'[x_n]$ is the minimal polynomial of $\bar{x}_n$ over $L'$. Since $L$ is separable over $k$, the element $\bar{x}_n$ is separable over $k$, so it is separable over $L'$, and $\bar{g}$ has no repeated root. Hence the derivative of $\bar{g}$ does not vanish at $\bar{x}_n$, that is, $\overline{\partial g/\partial x_n} \neq 0$. The field $L'$ is separable over $k$, as a subfield of $L$, so by induction the vectors $D(h)$ for $h \in P'$ span $L'^{n-1}$ over $L'$, and they have last coordinate $0$ since $h$ does not involve $x_n$. Over $L$ they span $L^{n-1} \times 0$, and $D(g)$ has a nonzero last coordinate. So $D$ is surjective. $\square$

**Theorem P1.9.12 (Jacobian criterion).** Let $M$ be a maximal ideal of $A$, let $P \supseteq I$ be its preimage in $R$, and suppose that $\kappa(P)$ is separable over $k$.

1. The cotangent space of $A_M$ has dimension
$$
\dim_{\kappa(P)} MA_M/M^2A_M = n - \operatorname{rank} J(P) .
$$
2. If $A$ is a domain of dimension $d$, then $\operatorname{rank} J(P) \leq n - d$, and $A_M$ is regular if and only if $\operatorname{rank} J(P) = n - d$.

Lean: not in Mathlib. Mathlib has `Algebra.PreSubmersivePresentation.jacobian`, the determinant of the Jacobian matrix of a presentation with as many equations as variables to eliminate (definition), which is used to define standard smooth algebras.

*Proof.* (1) Since $M$ is maximal, $MA_M/M^2A_M = M/M^2 = P/(P^2 + I)$, the quotient of $P/P^2$ by the image of $I$. An element of $I$ has the form $\sum g_j f_j$, and by the lemma $D(\sum g_j f_j) = \sum \bar{g}_j D(f_j)$. So $D$ maps the image of $I$ onto the $L$-span of the vectors $D(f_1), \dots, D(f_r)$, which are the rows of $J(P)$. Since $D$ is an isomorphism, $P/(P^2 + I) \cong L^n/\operatorname{row}(J(P))$, of dimension $n - \operatorname{rank} J(P)$.

(2) By Corollary P1.5.42, $\operatorname{ht} M = d - \dim A/M = d$, so $\dim A_M = d$. Corollary P1.5.19 gives $d \leq n - \operatorname{rank} J(P)$, with equality exactly when $A_M$ is regular. $\square$

Over an algebraically closed field the theorem says: a point $a$ of an irreducible affine variety $X = V(f_1, \dots, f_r) \subseteq \mathbb{A}^n$ of dimension $d$ with $I(X) = (f_1, \dots, f_r)$ is a regular point if and only if the Jacobian matrix at $a$ has rank $n - d$, the classical definition of a smooth point. The hypothesis that the $f_j$ generate the ideal of $X$ matters: $x^2 = 0$ defines the same set as $x = 0$ in $\mathbb{A}^1$, but its Jacobian vanishes at the origin.

For an $r \times n$ matrix over a field, the rank is at least $s$ if and only if some $s \times s$ minor is nonzero. Let $J_A \subseteq A$ be the ideal generated by the images in $A$ of the $(n - d) \times (n - d)$ minors of the matrix $(\partial f_j/\partial x_i)$ with entries in $R$. Its formation commutes with reduction modulo $P$.

**Corollary P1.9.13 (the singular locus).** Let $k$ be perfect and let $A$ be a domain of dimension $d$. A maximal ideal $M$ of $A$ satisfies "$A_M$ is not regular" if and only if $M \supseteq J_A$. So the singular closed points form the closed set $V(J_A) \cap \operatorname{Max} A$. Also $J_A \neq 0$, so the regular closed points form a nonempty open subset of $\operatorname{Max} A$.

Lean: not in Mathlib.

*Proof.* By the theorem, $A_M$ is regular if and only if $\operatorname{rank} J(P) \geq n - d$, that is, if and only if some $(n-d)$-minor is nonzero modulo $P$, that is, if and only if $J_A \not\subseteq M$.

*Sketch for $J_A \neq 0$.* Let $K$ be the fraction field of $A$. The same computation with the module of Kähler differentials shows that $\Omega_{K/k} \cong K^n/\operatorname{row}(J)$, where $J$ is the Jacobian matrix with entries in $K$. Since $k$ is perfect, $K$ is separably generated over $k$, and then $\dim_K \Omega_{K/k} = \operatorname{trdeg}_k K = d$. Chapter 12 proves both statements. So $\operatorname{rank} J = n - d$ over $K$, and some $(n-d)$-minor is nonzero in $K$, hence in $A$. A finitely generated $k$-algebra is a Jacobson ring (Theorem P1.4.30), so the Jacobson radical of the domain $A$ is $0$, and a nonzero element $\delta \in J_A$ lies outside some maximal ideal. $\square$

For a hypersurface the minors are the partial derivatives themselves: if $f$ is irreducible and $A = k[x_1, \dots, x_n]/(f)$, then $d = n - 1$, and the singular closed points are the closed points of
$$
V\left(f, \frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_n}\right) .
$$
Exercise 6 proves $J_A \neq 0$ for hypersurfaces without Chapter 12. The full Jacobian criterion of Eisenbud, Chapter 16, treats every prime of $A$, not only maximal ideals. With the result of Section 9.3 that a localization of a regular local ring is regular, it gives that the singular locus of $\operatorname{Spec} A$ is the closed set $V(J_A)$.

### Proof in words

At a rational point, $f \mapsto (\partial f/\partial x_i(a))$ is the linear part of the Taylor expansion, and it identifies $\mathfrak{m}_a/\mathfrak{m}_a^2$ with $k^n$. The equations of $X$ cut this space down by the span of their gradients, so the cotangent space of $X$ at $a$ has dimension $n$ minus the rank of the Jacobian matrix. Comparing with the dimension of $X$ gives the criterion. At a closed point whose residue field is a separable extension, the same holds after a short induction, because a separable minimal polynomial has a nonzero derivative at its root. For inseparable residue fields the derivatives lose information, and the criterion fails. The rank condition is a condition on minors, so the singular points form a closed set, and the generic point of $X$ is regular, so the set is not everything.

### Examples

**Example P1.9.14 (cones and curves).** Let $k$ have characteristic not $2$.

- For the quadric cone $f = xy - z^2$, $\nabla f = (y, x, -2z)$ vanishes only at the origin, the only singular point.
- For the cone $f = xw - yz$ over a quadric surface, $\nabla f = (w, -z, -y, x)$, and the origin is again the only singular point.
- For the cusp $f = y^2 - x^3$ with characteristic not $3$, $\nabla f = (-3x^2, 2y)$, and the only singular point is the origin. For the node $f = y^2 - x^2 - x^3$, $\nabla f = (-2x - 3x^2, 2y)$ vanishes on the curve only at the origin, since $x = -2/3$ gives $f(-2/3, 0) = -4/9 + 8/27 \neq 0$.

**Example P1.9.15 (the Whitney umbrella).** Let $k$ have characteristic not $2$ and $f = x^2 - y^2 z$, which is irreducible. Then $\nabla f = (2x, -2yz, -y^2)$ vanishes exactly on the line $x = y = 0$, which lies on the surface. So the singular locus of the surface $A = k[x, y, z]/(f)$ is the whole $z$-axis, a closed subset of codimension one. By Section 8.1, a Noetherian normal domain is regular at every prime of height one, so $A$ is not normal. Indeed $x/y$ is integral over $A$, since $(x/y)^2 = z$, and $x/y \notin A$.

**Example P1.9.16 (affine elliptic curves).** Let $k$ be algebraically closed of characteristic not $2$ or $3$, and $f = y^2 - (x^3 + ax + b)$. The singular points satisfy $2y = 0$, $3x^2 + a = 0$ and $x^3 + ax + b = 0$, so they exist if and only if the cubic $x^3 + ax + b$ has a repeated root, that is, if and only if $4a^3 + 27b^2 = 0$. For $a = b = 0$ this is the cusp, and for $a = -3$, $b = 2$ it is the node at $(1, 0)$, since $x^3 - 3x + 2 = (x - 1)^2(x + 2)$.

**Example P1.9.17 (the criterion fails over an imperfect field).** Let $k = \mathbb{F}_p(t)$ and $A = k[x]/(x^p - t)$. The polynomial $x^p - t$ is irreducible, so $A$ is a field, purely inseparable of degree $p$ over $k$, and $A$ is regular of dimension $0$. Here $n = 1$, $d = 0$, and $\partial (x^p - t)/\partial x = p x^{p-1} = 0$, so $\operatorname{rank} J = 0 \neq n - d$. The residue field $\kappa(P) = A$ is not separable over $k$, which is the hypothesis that fails. Over the algebraic closure, $A \otimes_k \bar{k} \cong \bar{k}[x]/((x - t^{1/p})^p)$ is not reduced. The Jacobian criterion detects *geometric* regularity, that is, smoothness, and Chapter 12 explains this with Kähler differentials.

### Exercises

1. (A) Find the singular points of the plane curves $y^2 = x^4 + x^5$ and $x^3 + y^3 = 3xy$ over an algebraically closed field of characteristic $0$.
2. (A) Let $m \geq 1$ and let $k$ have characteristic not dividing $m$. Show that the affine Fermat surface $x^m + y^m + z^m = 1$ is smooth at every closed point.
3. (A) Show that the cone $xy = z^m$ with $m \geq 2$ is singular exactly at the origin, in every characteristic. Show that the twisted cubic $A = k[x, y, z]/(y - x^2, z - x^3)$ is regular at every maximal ideal.
4. (B) Let $k = \mathbb{F}_p(t)$ and $P = (x^p - t) \subseteq k[x]$. Show that the map $D$ of the lemma is zero on $P/P^2$, a vector space of dimension one. Show directly that $D$ is an isomorphism for the ideal of a rational point over every field.
5. (A) Let $X = V(f_1, \dots, f_r) \subseteq \mathbb{A}^n$ with $I = (f_1, \dots, f_r)$, and let $a \in X$ be a rational point with $\operatorname{rank} J(a) = n - d$, where $d = \dim A_M$. Show that $A_M$ is regular, without assuming that $A$ is a domain.
6. (B) Let $k$ be perfect and $f \in k[x_1, \dots, x_n]$ irreducible. Show that some $\partial f/\partial x_i$ is not divisible by $f$, and deduce that $V(f)$ has a regular closed point. (Hint: if every $\partial f/\partial x_i$ is divisible by $f$, it is $0$ for degree reasons. In characteristic $p$, $f$ is then a polynomial in $x_1^p, \dots, x_n^p$, and over a perfect field it is a $p$-th power.)
7. (C) Let $p$ be an odd prime, $k = \mathbb{F}_p(t)$ and $B = k[x, y]/(y^2 - x^p + t)$. Let $M = (y, x^p - t)$. Show that $M$ is a maximal ideal of $B$, that $M = yB$, so that $B_M$ is a discrete valuation ring, and that both entries of the Jacobian matrix lie in $M$. Explain which hypothesis of the theorem fails.

### Lean

Mathlib defines smoothness of algebras through `Algebra.FormallySmooth` and `Algebra.Smooth`, and standard smooth algebras through presentations, with the Jacobian determinant `Algebra.PreSubmersivePresentation.jacobian` and the matrix `Algebra.PreSubmersivePresentation.jacobiMatrix`. The comparison of the rank of the Jacobian matrix with the cotangent space of a local ring, the Jacobian criterion for regularity and the closedness of the singular locus are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

The rank condition on the Jacobian matrix is the classical definition of a nonsingular point in algebraic geometry over the complex numbers. Zariski proved in 1947 that over a perfect field it is equivalent to the regularity of the local ring, and he gave examples over imperfect fields where the two notions differ. Grothendieck separated the two notions in EGA as regularity and smoothness. The literature state of every result here is theorem. The section follows Eisenbud, Chapter 16, and Matsumura, Chapter 5.
