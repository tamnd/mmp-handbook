---
title: Smoothness over a field and the Jacobian criterion
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch12, Har77:I.5, GW20:ch6]
requires: [P1.4, P1.9, P1.12, P3.2, P3.3, P3.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Smoothness over a field and the Jacobian criterion

### Statement

Throughout, $k$ is a field and $X$ is a scheme locally of finite type over $k$. For an affine open $V = \operatorname{Spec} A$ of $X$ with a presentation $A = k[x_1, \dots, x_n]/(f_1, \dots, f_r)$ and a point $x \in V$, the *Jacobian matrix at $x$* is the $r \times n$ matrix $J(x) = (\partial f_j/\partial x_i (x))$, where $\partial f_j/\partial x_i (x)$ is the image of the formal partial derivative in $\kappa(x)$. For the $A$-module $\Omega_{A/k}$ of Kähler differentials (Definition P1.12.2) write $\Omega_{A/k}(x) = \Omega_{A/k} \otimes_A \kappa(x)$.

**Definition P3.7.21 (smooth over a field).** Let $d \geq 0$. The scheme $X$ is *smooth of dimension $d$ over $k$ at $x$* if there are an open neighbourhood $U$ of $x$ of pure dimension $d$ and an affine open $V \subseteq U$ containing $x$ with a presentation as above such that $\operatorname{rank} J(x) = n - d$. It is *smooth over $k$ at $x$* if it is smooth of some dimension at $x$, and *smooth over $k$* if it is smooth at every point. The *smooth locus* is the set of points at which $X$ is smooth.

Lean: Mathlib `AlgebraicGeometry.Smooth` and `AlgebraicGeometry.SmoothOfRelativeDimension`, defined for morphisms through smooth and standard smooth ring maps (definitions). The equivalence with the definition here is not in Lean as stated.

**Lemma P3.7.22 (the Jacobian rank is intrinsic).** In the situation above:

1. $\operatorname{rank} J(x) = n - \dim_{\kappa(x)} \Omega_{A/k}(x)$. So the condition $\operatorname{rank} J(x) = n - d$ does not depend on the affine open $V \ni x$ or on its presentation.
2. If $U$ is open and of pure dimension $d$, then $\dim_{\kappa(x)} \Omega_{A/k}(x) \geq d$ for every affine open $V = \operatorname{Spec} A \subseteq U$ and every $x \in V$.

Lean: not in Lean as stated. Mathlib `KaehlerDifferential.isLocalizedModule_of_isLocalizedModule` is the localization of differentials used in the proof (proved in Mathlib).

**Lemma P3.7.23 (dimension under extension of the base field).** Let $A$ be a finitely generated $k$-algebra that is a domain of dimension $d$, and let $K/k$ be a field extension. Then every irreducible component of $\operatorname{Spec} A \otimes_k K$ has dimension $d$. Consequently, if $X$ has pure dimension $d$, then so has $X_K = X \times_k \operatorname{Spec} K$.

Lean: not in Lean as stated.

**Theorem P3.7.24 (the Jacobian criterion).** Let $X$ be locally of finite type over $k$.

1. The smooth locus of $X$ is open.
2. Let $x \in X$ be a closed point with $\kappa(x)$ separable over $k$, and let $X$ have pure dimension $d$ near $x$. Then $X$ is smooth of dimension $d$ at $x$ if and only if $\mathcal{O}_{X, x}$ is a regular local ring.
3. If $k$ is perfect, then $X$ is smooth over $k$ if and only if $X$ is regular.
4. If $X$ is smooth of dimension $d$ over $k$ and $K/k$ is a field extension, then $X_K$ is smooth of dimension $d$ over $K$.

Lean: Mathlib `AlgebraicGeometry.Scheme.Hom.isOpen_smoothLocus` is part 1 for Mathlib's smoothness, and `AlgebraicGeometry.Scheme.Hom.dense_smoothLocus_of_perfectField` proves that a reduced scheme locally of finite presentation over a perfect field has a dense smooth locus (proved in Mathlib). Parts 2 to 4 are not in Lean as stated.

**Proposition P3.7.25 (smooth projective hypersurfaces).** Let $F \in k[x_0, \dots, x_n]$ be a nonzero homogeneous polynomial of degree $e \geq 1$, with $e$ not divisible by the characteristic of $k$, and let $X = V_+(F) \subseteq \mathbb{P}^n_k$. Then the points at which $X$ is not smooth form the closed set $V_+(\partial F/\partial x_0, \dots, \partial F/\partial x_n)$. In particular $X$ is smooth over $k$ if and only if the $n + 1$ partial derivatives of $F$ have no common zero in $\mathbb{P}^n_k$.

Lean: not in Lean as stated.

### Proof in words

The module of differentials of $k[x_1, \dots, x_n]/(f_1, \dots, f_r)$ is the cokernel of the transposed Jacobian matrix, so the rank of the Jacobian at a point is $n$ minus the fibre dimension of $\Omega$ there, and the fibre dimension does not depend on the presentation. It is at least the dimension, by comparison with the generic point, where it is at least the transcendence degree. At a closed point with separable residue field the cotangent space has dimension $n - \operatorname{rank} J$, so smoothness is regularity. Over a perfect field all residue fields of closed points are separable, and regularity at closed points propagates to all points. Since the Jacobian matrix is made of polynomials, it does not change when the field is extended. For a projective hypersurface Euler's formula $eF = \sum x_i \, \partial F/\partial x_i$ makes the vanishing of the $n + 1$ partial derivatives equivalent to the vanishing of the $n$ derivatives of each affine chart.

### Examples

**Example P3.7.26 (linear groups).** The group $\mathrm{GL}_n = D(\det) \subseteq \mathbb{A}^{n^2}_k$ is open in affine space, so it is smooth of dimension $n^2$. Let $\mathrm{SL}_n = V(\det - 1) \subseteq \mathbb{A}^{n^2}_k$. It has pure dimension $n^2 - 1$ by Proposition P3.7.5, as $\det - 1$ is neither $0$ nor a unit; it is irreducible, since $\det - 1$ is an irreducible polynomial, a fact not needed here. The partial derivative $\partial \det/\partial x_{ij}$ is the cofactor $C_{ij}$, and $\sum_j x_{ij} C_{ij} = \det = 1$ on $\mathrm{SL}_n$. So at every point some cofactor is nonzero, the $1 \times n^2$ Jacobian matrix has rank $1$, and $\mathrm{SL}_n$ is smooth of dimension $n^2 - 1$ over every field.

**Example P3.7.27 (plane cubics).** Let $\operatorname{char} k \neq 2, 3$ and $F = y^2 z - x^3 - a x z^2 - b z^3$, with $a, b \in k$, and $X = V_+(F) \subseteq \mathbb{P}^2_k$. On the chart $z = 1$, with $f = y^2 - x^3 - a x - b$, the partial derivatives are $-3x^2 - a$ and $2y$. A point is singular when $y = 0$ and $x$ is a common root of $g = x^3 + a x + b$ and $g' = 3x^2 + a$, that is, a double root of $g$. This happens if and only if the discriminant $-(4a^3 + 27b^2)$ vanishes. The only point of $X$ off this chart is $[0 : 1 : 0]$, and on the chart $y = 1$, with $h = z - x^3 - a x z^2 - b z^3$, $\partial h/\partial z = 1$ at the origin. So $X$ is smooth if and only if $4a^3 + 27b^2 \neq 0$. For $a = b = 0$ it is the cuspidal cubic, and for $a = -3$, $b = 2$, where $g = (x - 1)^2(x + 2)$, it has a node at $(1, 0)$.

**Example P3.7.28 (Fermat hypersurfaces).** Let $F = x_0^e + \dots + x_n^e$. If $\operatorname{char} k \nmid e$, then $\partial F/\partial x_i = e x_i^{e - 1}$, and these have no common zero, so $V_+(F)$ is smooth of dimension $n - 1$ by Proposition P3.7.25. If $\operatorname{char} k = p$ and $e = p$, then $F = (x_0 + \dots + x_n)^p$, and $V_+(F)$ is the hyperplane $x_0 + \dots + x_n = 0$ with multiplicity $p$. It is not reduced, and not smooth at any point, since all partial derivatives vanish.

**Example P3.7.29 (regular but not smooth).** Let $p > 2$ be a prime, $k = \mathbb{F}_p(t)$, and $X = V(y^2 - x^p + t) \subseteq \mathbb{A}^2_k$, of pure dimension $1$. The Jacobian matrix is $(0, \ 2y)$, of rank $1$ except on $y = 0$. On $X$, $y = 0$ forces $x^p = t$, so the only point of $X$ that is not smooth is the closed point $P = (y, x^p - t)$, with residue field $k(t^{1/p})$, which is not separable over $k$. It is regular: in $k[x, y]$ the ideal $\mathfrak{M} = (y, x^p - t)$ is maximal and $y^2 - x^p + t \equiv -(x^p - t) \not\equiv 0$ modulo $\mathfrak{M}^2$. So $\mathfrak{m}_P/\mathfrak{m}_P^2$ has dimension $1$, spanned by $y$. Over $\bar k$, with $s = t^{1/p}$, the equation becomes $y^2 = (x - s)^p$, which is singular at $(s, 0)$. So $X$ is regular, not smooth, and $X_{\bar k}$ is not regular. This shows that part 2 of Theorem P3.7.24 needs the separability of $\kappa(x)$ and that part 3 needs $k$ to be perfect. Example P1.9.17 is the zero-dimensional version.

**Example P3.7.30 (the cone and the double line).** The quadric cone $X = V(xy - z^2) \subseteq \mathbb{A}^3_k$ has pure dimension $2$ and Jacobian matrix $(y, x, -2z)$. Its smooth locus is the complement of the vertex in every characteristic: in characteristic $2$ the matrix is $(y, x, 0)$, and $x = y = 0$ on $X$ still forces $z = 0$. The scheme $V(y^2) \subseteq \mathbb{A}^2_k$ has Jacobian matrix $(0, 2y)$, which vanishes on $V(y^2)$ in every characteristic, as $y$ is nilpotent there, so it is nowhere smooth. A smooth scheme is reduced by part 3 of Theorem P3.7.24 over a perfect field, and by part 4 and the perfect case in general (Exercise 4).

### Proof

*Proof of Lemma P3.7.22.* (1) By Corollary P1.12.7, $\Omega_{A/k}$ is the cokernel of the map $A^r \to A^n$ given by the transposed Jacobian matrix. Tensor products are right exact, so $\Omega_{A/k}(x)$ is the cokernel of $J(x)^T \colon \kappa(x)^r \to \kappa(x)^n$, of dimension $n - \operatorname{rank} J(x)$. For independence, let $V = \operatorname{Spec} A$ and $V' = \operatorname{Spec} A'$ be two affine opens containing $x$, each with a presentation. By the proof of Lemma P3.2.22 there is an open $W \ni x$ that is a basic open set $D(g)$ of $V$ and $D(g')$ of $V'$, so $A_g \cong A'_{g'}$ as $k$-algebras. By Proposition P1.12.8, $\Omega_{A/k} \otimes_A A_g = \Omega_{A_g/k} \cong \Omega_{A'_{g'}/k} = \Omega_{A'/k} \otimes_{A'} A'_{g'}$, and tensoring with $\kappa(x)$ gives $\Omega_{A/k}(x) \cong \Omega_{A'/k}(x)$. So $n - \operatorname{rank} J(x)$ is the same for both presentations.

(2) Let $x = \mathfrak{q} \in V$ and let $\mathfrak{p} \subseteq \mathfrak{q}$ be a minimal prime of $A$. Then $\overline{\{\mathfrak{p}\}}$ is an irreducible component of $V$, so $\dim A/\mathfrak{p} = d$, and the field $\kappa(\mathfrak{p}) = \operatorname{Frac}(A/\mathfrak{p})$ has transcendence degree $d$ over $k$ (Theorem P1.4.31). The quotient map $A_\mathfrak{p} \to \kappa(\mathfrak{p})$ gives, by the conormal sequence (Theorem P1.12.6) and Proposition P1.12.8, a surjection $\Omega_{A/k} \otimes_A \kappa(\mathfrak{p}) \to \Omega_{\kappa(\mathfrak{p})/k}$. By Theorem P1.12.16, $\dim \Omega_{\kappa(\mathfrak{p})/k} \geq d$, so $\dim \Omega_{A/k}(\mathfrak{p}) \geq d$. The sheaf $\widetilde{\Omega_{A/k}}$ on $V$ is of finite type, and its fibre at a point $y$ is $\Omega_{A/k}(y)$. By part 3 of Proposition P3.5.25, the set where the fibre dimension is at least $d$ is closed. It contains $\mathfrak{p}$, so it contains $\mathfrak{q} \in \overline{\{\mathfrak{p}\}}$. $\square$

*Proof of Lemma P3.7.23.* By Noether normalization (Theorem P1.4.27) there is a finite injective map $R = k[y_1, \dots, y_d] \to A$, with $d = \dim A$ by Theorem P1.4.31. The $R$-module $A$ is finitely generated and torsion-free, as $A$ is a domain. So it embeds in a free module: if $a_1, \dots, a_s$ generate $A$, write them in a basis of $A \otimes_R \operatorname{Frac}(R)$, of dimension $m$, and clear denominators; this gives an injective $R$-linear map $A \to R^m$. Tensoring over $k$ with $K$ is exact, so $A_K = A \otimes_k K \to R_K^m$ is injective, where $R_K = K[y_1, \dots, y_d]$. So no nonzero element of $R_K$ is a zero divisor on $A_K$, and $A_K$ is finite over $R_K$.

Let $P$ be a minimal prime of $A_K$. Every element $a \in P$ is a zero divisor: in $(A_K)_P$ the ideal $P(A_K)_P$ is the only prime, so $a$ is nilpotent there, and $a^m s = 0$ for some $s \notin P$ and some $m \geq 1$ chosen minimal; then $a \cdot a^{m-1} s = 0$ with $a^{m-1} s \neq 0$. Hence $P \cap R_K = 0$, and $R_K \to A_K/P$ is finite and injective. By Corollary P1.4.14, $\dim A_K/P = \dim R_K = d$. For the second statement, cover $X$ by affine opens $\operatorname{Spec} A$ with irreducible components $V(\mathfrak{p}_i)$, $\dim A/\mathfrak{p}_i = d$. The preimage of $V(\mathfrak{p}_i)$ in $\operatorname{Spec} A_K$ is $\operatorname{Spec} (A/\mathfrak{p}_i)_K$, so every irreducible component of $\operatorname{Spec} A_K$ is an irreducible component of one of these, of dimension $d$ by the first part. By part 2 of Proposition P3.7.2 and Theorem P3.7.4 applied to the components, $X_K$ has pure dimension $d$. $\square$

*Proof of Theorem P3.7.24.* (1) Let $X$ be smooth of dimension $d$ at $x$, with $U$ and $V = \operatorname{Spec} A$ as in Definition P3.7.21. By Lemma P3.7.22, $\dim \Omega_{A/k}(y) \geq d$ for all $y \in V$, with equality at $x$. By part 3 of Proposition P3.5.25 the set of $y \in V$ with $\dim \Omega_{A/k}(y) \leq d$ is open. On it, $\operatorname{rank} J(y) = n - d$, and $X$ is smooth of dimension $d$ at each such $y$, with the same $U$ and $V$.

(2) Let $U \ni x$ be open of pure dimension $d$, and $V = \operatorname{Spec} A \subseteq U$ an affine open containing $x$ with a presentation. As $x$ is closed, it is a maximal ideal of $A$. By part 1 of Theorem P1.9.12, $\dim \mathfrak{m}_x/\mathfrak{m}_x^2 = n - \operatorname{rank} J(x)$. Every irreducible component $Z$ of $U$ through $x$ has dimension $d$, and with its reduced structure it has $\operatorname{codim}(\{x\}, Z) = d$ by part 4 of Theorem P3.7.4, as $\dim \{x\} = 0$. By part 4 of Proposition P3.7.2, $\dim \mathcal{O}_{X, x} = \operatorname{codim}(\{x\}, U) = d$, since every chain of irreducible closed sets that starts at $\{x\}$ lies in one component. So $\mathcal{O}_{X, x}$ is regular if and only if $n - \operatorname{rank} J(x) = d$, that is, if and only if $X$ is smooth of dimension $d$ at $x$.

(3) Let $k$ be perfect. Every closed point $x$ has $\kappa(x)$ finite over $k$ (Proposition P3.7.3), hence separable. Let $X$ be smooth. Then $X$ has pure dimension near every closed point, and part 2 shows that every closed point is regular. By part 4 of Proposition P3.7.15, $X$ is regular. Conversely, let $X$ be regular. By part 2 of Proposition P3.7.15 every point lies on exactly one irreducible component, so the irreducible components are pairwise disjoint. They are locally finite, as $X$ is locally Noetherian, so each component is open, as the complement of the union of the others. Hence $X$ has pure dimension near every point. By part 2 every closed point lies in the smooth locus, which is open by part 1. Its complement is closed and contains no closed point, so it is empty by part 3 of Proposition P3.7.3.

(4) Let $x' \in X_K$ lie over $x \in X$, and let $U$ and $V = \operatorname{Spec} k[x_1, \dots, x_n]/(f_1, \dots, f_r)$ be as in Definition P3.7.21 for $x$. Then $U_K$ is an open neighbourhood of $x'$ of pure dimension $d$ by Lemma P3.7.23, and $V_K = \operatorname{Spec} K[x_1, \dots, x_n]/(f_1, \dots, f_r)$ is an affine open containing $x'$, with the same polynomials. The matrix $J(x')$ is the image of $J(x)$ under the field extension $\kappa(x) \to \kappa(x')$, and rank does not change under field extension. So $\operatorname{rank} J(x') = n - d$. $\square$

*Proof of Proposition P3.7.25.* By part 3 of Proposition P3.7.5 every irreducible component of $X$ has dimension $n - 1$. Let $x \in X \cap D_+(x_0)$; the other charts are the same. On $D_+(x_0) = \operatorname{Spec} k[t_1, \dots, t_n]$, $t_i = x_i/x_0$, the scheme $X$ is $V(f)$ with $f(t) = F(1, t_1, \dots, t_n)$, and $\partial f/\partial t_i = (\partial F/\partial x_i)(1, t)$ for $i \geq 1$. So $X$ is smooth at $x$ if and only if some $\partial F/\partial x_i$ with $i \geq 1$ does not vanish at $x$. By Euler's formula
$$e F = \sum_{i = 0}^n x_i \frac{\partial F}{\partial x_i},$$
evaluated at $(1, t)$, $(\partial F/\partial x_0)(1, t) = e f(t) - \sum_{i \geq 1} t_i \, (\partial f/\partial t_i)(t)$. At a point of $X$, $f = 0$, so if all $\partial F/\partial x_i$ with $i \geq 1$ vanish at $x$, then so does $\partial F/\partial x_0$. So $X$ is not smooth at $x$ if and only if $x \in V_+(\partial F/\partial x_0, \dots, \partial F/\partial x_n)$. Conversely, Euler's formula and $e \neq 0$ in $k$ show that $V_+(\partial F/\partial x_0, \dots, \partial F/\partial x_n) \subseteq V_+(F) = X$. $\square$

### Exercises

1. (A) Show that the twisted cubic of Exercise 3 of Section 7.1 is smooth, using its parametrization and the chart $x_0 = 1$, where it is $V(x_2 - x_1^2, x_3 - x_1^3)$.
2. (A) Let $\operatorname{char} k \neq 2$. Show that the quadric $V_+(x_0^2 + \dots + x_n^2) \subseteq \mathbb{P}^n_k$ is smooth, and that $V_+(x_0^2 + x_1^2) \subseteq \mathbb{P}^2_k$ is singular at $[0 : 0 : 1]$. Describe it over $k = \mathbb{C}$ and over $k = \mathbb{R}$.
3. (A) Find the points at which the Whitney umbrella $V(x^2 - y^2 z) \subseteq \mathbb{A}^3_k$ is not smooth, for $\operatorname{char} k \neq 2$.
4. (B) Show that a scheme that is smooth over a field $k$ is reduced. Use part 4 of Theorem P3.7.24 with $K = \bar k$, part 3 for $\bar k$, and the injectivity of $A \to A \otimes_k \bar k$.
5. (B) Show that the affine curve $V(y^2 - x^p + t)$ of Example P3.7.29 is a regular integral scheme whose base change to $\bar k$ is integral and not normal. Compute its normalization over $\bar k$.
6. (B) Let $X$ be smooth of dimension $d$ over $k$ and $Y$ smooth of dimension $e$. Show that $X \times_k Y$ is smooth of dimension $d + e$. For the pure dimension, use Lemma P3.7.23 and Theorem P3.7.6.
7. (C) Let $\operatorname{char} k = 0$. Show that a general hypersurface of degree $e$ in $\mathbb{P}^n_k$ is smooth: the coefficient vectors of the singular hypersurfaces lie in a proper closed subset of $\mathbb{P}^N_k$, $N = \binom{n + e}{e} - 1$. Use the incidence correspondence $\{(F, x) : x \in V_+(\partial F/\partial x_i \text{ for all } i)\} \subseteq \mathbb{P}^N \times \mathbb{P}^n$, compute the dimension of its fibres over $\mathbb{P}^n$, and apply Theorem P3.7.6 and the properness of $\mathbb{P}^n$.

### Lean

Mathlib defines smooth morphisms of schemes, `AlgebraicGeometry.Smooth`, by asking that the ring maps on affine opens be smooth in the sense of `Algebra.Smooth`, and `AlgebraicGeometry.SmoothOfRelativeDimension` by standard smooth presentations, `Algebra.IsStandardSmoothOfRelativeDimension`. It proves that the smooth locus `AlgebraicGeometry.Scheme.Hom.smoothLocus` is open and that it is dense for reduced schemes over a perfect field. The definition through the rank of the Jacobian, its equivalence with Mathlib's, and the comparison with regularity are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

The definition through the Jacobian matrix follows Vakil, Section 12.2, and agrees with Hartshorne's definition of a nonsingular variety over an algebraically closed field, Section I.5. Grothendieck's definition of a smooth morphism is through flatness and the fibres, or through the infinitesimal lifting property, and Chapter 12 shows that a scheme over $k$ is smooth of dimension $d$ if and only if its sheaf of differentials is locally free of rank $d$. Over every field, smooth implies regular and is equivalent to the regularity of $X_{\bar k}$; this needs the descent of regularity along the faithfully flat map $X_{\bar k} \to X$ and is not proved here; the Stacks Project treats it in its chapter on varieties. Example P3.7.29 is the reason why the minimal model program in positive and mixed characteristic works with regular schemes rather than smooth ones. The literature state is theorem.
