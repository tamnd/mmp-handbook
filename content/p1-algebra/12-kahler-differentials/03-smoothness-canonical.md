---
title: Smoothness and the canonical module
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [Mat86:ch9, Eis95:ch16]
requires: [P1.1, P1.4, P1.5, P1.8, P1.9, P1.10, P1.11]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Smoothness and the canonical module

### Statement

Throughout, $k$ is a perfect field, $A = k[x_1, \dots, x_n]/I$ is a finitely generated $k$-algebra that is a domain of dimension $d$, and $K$ is its fraction field. For a maximal ideal $\mathfrak{m}$ write $\kappa(\mathfrak{m}) = A/\mathfrak{m}$, a finite extension of $k$, and $\Omega_A = \Omega_{A/k}$.

**Lemma P1.12.22 (equal fibre dimensions give freeness).** Let $(R, \mathfrak{m}, \kappa)$ be a Noetherian local domain with fraction field $F$, and $M$ a finitely generated $R$-module. If $\dim_\kappa M \otimes_R \kappa = \dim_F M \otimes_R F = r$, then $M$ is free of rank $r$.

Lean: not in Mathlib in this form.

*Proof.* By Nakayama's lemma (Theorem P1.1.26) there are $r$ elements that generate $M$, so there is an exact sequence $0 \to N \to R^r \to M \to 0$. Tensoring with $F$ is exact, since $F$ is a localization, and gives a surjection $F^r \to M \otimes_R F$ of vector spaces of the same dimension $r$. So it is bijective and $N \otimes_R F = 0$. Then every element of $N$ is killed by a nonzero element of $R$. But $N \subseteq R^r$, and $R$ is a domain, so $N = 0$. $\square$

**Theorem P1.12.23 (smoothness and differentials).** Let $\mathfrak{m}$ be a maximal ideal of $A$. Then
$$
\dim_{\kappa(\mathfrak{m})} \Omega_A \otimes_A \kappa(\mathfrak{m}) = \dim_{\kappa(\mathfrak{m})} \mathfrak{m}/\mathfrak{m}^2 \geq d ,
$$
and the local ring $A_\mathfrak{m}$ is regular if and only if $(\Omega_A)_\mathfrak{m}$ is a free $A_\mathfrak{m}$-module of rank $d$.

Lean: not in Mathlib in this form. Mathlib defines smooth algebras, `Algebra.Smooth`, through `Algebra.FormallySmooth`, whose field `projective_kaehlerDifferential` says that `Ω[A⁄R]` is projective (definitions).

*Proof.* Let $P \subseteq k[x_1, \dots, x_n]$ be the preimage of $\mathfrak{m}$, and $I = (f_1, \dots, f_r)$. By Corollary P1.12.7, $\Omega_A \otimes_A \kappa(\mathfrak{m})$ is the quotient of $\kappa(\mathfrak{m})^n$ by the rows of the matrix $J(P)$ of the values of the partial derivatives $\partial f_j/\partial x_i$ modulo $P$, so its dimension is $n - \operatorname{rank} J(P)$. The field $\kappa(\mathfrak{m})$ is finite over the perfect field $k$, hence separable. By Theorem P1.9.12, $n - \operatorname{rank} J(P)$ is the dimension of $\mathfrak{m}A_\mathfrak{m}/\mathfrak{m}^2A_\mathfrak{m} = \mathfrak{m}/\mathfrak{m}^2$, which is at least $\dim A_\mathfrak{m} = d$ (Corollary P1.5.19 and Corollary P1.5.42).

By Corollary P1.12.15, $\dim_K \Omega_A \otimes_A K = d$. If $A_\mathfrak{m}$ is regular, then $\dim \Omega_A \otimes \kappa(\mathfrak{m}) = d$, and the lemma, applied to $R = A_\mathfrak{m}$ and $M = (\Omega_A)_\mathfrak{m}$, shows that $(\Omega_A)_\mathfrak{m}$ is free of rank $d$. Conversely, if $(\Omega_A)_\mathfrak{m}$ is free of rank $d$, then $\dim \mathfrak{m}/\mathfrak{m}^2 = \dim \Omega_A \otimes \kappa(\mathfrak{m}) = d = \dim A_\mathfrak{m}$, so $A_\mathfrak{m}$ is regular. $\square$

This is the algebraic form of the statement that a variety is smooth where its cotangent bundle is a vector bundle of the right rank. It explains Example P1.9.17: over an imperfect field a regular ring can have $\Omega$ of the wrong rank.

**Corollary P1.12.24 (the smooth locus).** Let $U \subseteq \operatorname{Spec} A$ be the set of primes $\mathfrak{p}$ with $(\Omega_A)_\mathfrak{p}$ free of rank $d$. Then $U$ is open, a maximal ideal $\mathfrak{m}$ lies in $U$ if and only if $A_\mathfrak{m}$ is regular, and $U \supseteq D(\delta)$ for every $\delta \in J_A$. On $U$ the module $\Omega^d_A = \textstyle\bigwedge^d \Omega_A$ is locally free of rank one.

Lean: Mathlib has the exterior powers `ExteriorAlgebra.exteriorPower`, with notation `⋀[R]^n M` (definition). The corollary is not in Mathlib.

*Proof.* Let $\mathfrak{p} \in U$ and choose $\omega_1, \dots, \omega_d \in \Omega_A$ whose images form a basis of $(\Omega_A)_\mathfrak{p}$. The map $A^d \to \Omega_A$ that they define has a kernel and a cokernel that are finitely generated, since $A$ is Noetherian, and both vanish at $\mathfrak{p}$. So both are killed by some $s \notin \mathfrak{p}$ (Chapter 2), and $(\Omega_A)_s$ is free of rank $d$, which gives $D(s) \subseteq U$. The statement on maximal ideals is the theorem. For $\delta \in J_A$ and $\mathfrak{p} \in D(\delta)$, take a maximal ideal $\mathfrak{m} \supseteq \mathfrak{p}$. If $\delta \notin \mathfrak{m}$, then $A_\mathfrak{m}$ is regular by Corollary P1.9.13, so $(\Omega_A)_\mathfrak{m}$ is free of rank $d$, and its localization $(\Omega_A)_\mathfrak{p}$ is free of rank $d$. The ring $A/\mathfrak{p}$ is a finitely generated $k$-algebra, so it is a Jacobson ring (Theorem P1.4.30), and $\mathfrak{p}$ is the intersection of the maximal ideals that contain it. Since $\delta \notin \mathfrak{p}$, such an $\mathfrak{m}$ with $\delta \notin \mathfrak{m}$ exists. The last statement holds because the exterior power of a free module of rank $d$ is free of rank $\binom{d}{d} = 1$, and exterior powers commute with localization. $\square$

**Definition P1.12.25 (canonical module).** Let $A$ be normal. The *canonical module* of $A$ is the reflexive hull
$$
\omega_A = \left( \Omega^d_A / \text{torsion} \right)^{**} ,
$$
regarded as a submodule of the one dimensional $K$-vector space $\Omega^d_{K/k} = \Omega^d_A \otimes_A K$. By Theorem P1.11.24 it has the form $\omega_A \cong A(K_A)$ for a Weil divisor $K_A$, the *canonical divisor*, whose class in $\operatorname{Cl}(A)$ is determined by $A$.

**Proposition P1.12.26 (the canonical module on the smooth locus).** Let $A$ be normal.

1. The module $\omega_A$ is reflexive of rank one, and $\omega_A = \bigcap_{\operatorname{ht} \mathfrak{p} = 1} (\omega_A)_\mathfrak{p}$ inside $\Omega^d_{K/k}$.
2. For every prime $\mathfrak{p}$ in the smooth locus $U$, $(\omega_A)_\mathfrak{p} = (\Omega^d_A)_\mathfrak{p}$, a free module of rank one.
3. If no height one prime lies outside $U$, then $\omega_A = \bigcap_{\operatorname{ht} \mathfrak{p} = 1} (\Omega^d_A)_\mathfrak{p}$, so a $d$-form on $K$ lies in $\omega_A$ if and only if it is regular at every prime divisor.

Lean: not in Mathlib.

*Proof.* (1) The module $\Omega^d_A$ is finitely generated, and its rank is $\dim_K \Omega^d_{K/k} = \binom{d}{d} = 1$ by Section 12.2. The quotient by torsion is a torsion-free module of rank one, and its dual is a dual of a finitely generated module, hence reflexive by Theorem P1.11.22, and so is the double dual. The double dual of a torsion-free module $M$ of rank one is again of rank one, and the map $M \to M^{**}$ is injective, since $M$ embeds in a free module by Lemma P1.11.21. The formula is Theorem P1.11.22. (2) For $\mathfrak{p} \in U$ the module $(\Omega^d_A)_\mathfrak{p}$ is free of rank one by the corollary, so it is torsion-free and reflexive, and duals of finitely generated modules commute with localization. (3) Combine (1) and (2). $\square$

For a normal variety $X$ with smooth locus $j : U \to X$, the same construction gives the sheaf $\omega_X = j_*\Omega^d_U$, reflexive of rank one, and the canonical divisor $K_X$ with $\omega_X \cong \mathcal{O}_X(K_X)$. The set $U$ is exactly the set of primes $\mathfrak{p}$ with $A_\mathfrak{p}$ regular, also for primes that are not maximal (Eisenbud, Chapter 16). So the complement of $U$ has codimension at least two, since a normal ring satisfies $R_1$ (Section 11.2). This is the definition of $K_X$ used in Volume 4. When $X$ is Cohen-Macaulay this $\omega_X$ agrees with the canonical module of Section 10.3, and $K_X$ is Cartier exactly at the Gorenstein points (Example P1.10.31).

### Proof in words

Over a perfect field the cotangent space at a closed point is the fibre of the module of differentials, and the generic fibre has dimension $d$ by Section 12.2. A finitely generated module over a local domain with the same fibre dimension at the closed point and at the generic point is free. So a point is regular exactly when the differentials are free of rank $d$ near it, and this is an open condition. On the smooth part, the top exterior power of the differentials is a line bundle, and on a normal variety the reflexive hull of this line bundle across the small singular set is the canonical module, which defines the canonical divisor.

### Examples

**Example P1.12.27 (affine space).** For $A = k[x_1, \dots, x_n]$, $\Omega_A$ is free with basis $dx_i$, and $\omega_A = A\,dx_1 \wedge \dots \wedge dx_n$. So $K_A = 0$, which is no information, since $\operatorname{Cl}(A) = 0$. The form $dx_1 \wedge \dots \wedge dx_n$ has neither zeros nor poles on $\mathbb{A}^n$.

**Example P1.12.28 (projective space).** On $\mathbb{P}^n$ with coordinates $x_0, \dots, x_n$, let $u_i = x_i/x_0$ on the chart $x_0 \neq 0$ and $\sigma = du_1 \wedge \dots \wedge du_n$, a generator of $\Omega^n$ on this chart. On the chart $x_1 \neq 0$ put $v_0 = x_0/x_1$ and $v_j = x_j/x_1$ for $j \geq 2$. Then $u_1 = 1/v_0$ and $u_j = v_j/v_0$, so
$$
du_1 = -v_0^{-2}\,dv_0, \qquad du_j = v_0^{-1}\,dv_j - v_j v_0^{-2}\,dv_0 \quad (j \geq 2).
$$
In the wedge product the terms with $dv_0$ in the factors $du_j$ vanish, since $dv_0 \wedge dv_0 = 0$, and
$$
\sigma = -v_0^{-(n+1)}\,dv_0 \wedge dv_2 \wedge \dots \wedge dv_n .
$$
So $\sigma$ has a pole of order $n + 1$ along the hyperplane $H = \{x_0 = 0\}$, whose generic point lies in the second chart, and no zeros or poles elsewhere. So $K_{\mathbb{P}^n} = -(n+1)H$. This is the first example of a variety with $-K_X$ ample (Volume 4).

**Example P1.12.29 (hypersurfaces and the residue form).** Let $f \in k[x, y, z]$ be irreducible, and let $A = k[x, y, z]/(f)$ be normal with finitely many singular points. In $\Omega_A$ the relation $df = f_x\,dx + f_y\,dy + f_z\,dz = 0$ holds. Its wedge product with $dy$ and with $dx$ gives $f_x\,dx \wedge dy = f_z\,dy \wedge dz$ and $f_z\,dz \wedge dx = f_y\,dx \wedge dy$ in $\Omega^2_A$. So the form
$$
\omega_0 = \frac{dx \wedge dy}{f_z} = \frac{dy \wedge dz}{f_x} = \frac{dz \wedge dx}{f_y}
$$
in $\Omega^2_{K/k}$ is well defined wherever one of the partial derivatives is nonzero. At a smooth maximal ideal $\mathfrak{m}$, some partial derivative, say $f_z$, is a unit in $A_\mathfrak{m}$, and then $(\Omega_A)_\mathfrak{m}$ is free on $dx, dy$, since $dz$ is a combination of them, so $(\Omega^2_A)_\mathfrak{m} = A_\mathfrak{m}\,dx \wedge dy = A_\mathfrak{m}\,\omega_0$. No height one prime contains $J_A = (f_x, f_y, f_z)A$: such a prime $\mathfrak{p}$ has $\dim A/\mathfrak{p} = 1$ and lies in infinitely many maximal ideals, all singular. So by part 3 of Proposition P1.12.26 and the algebraic Hartogs theorem (Corollary P1.8.3),
$$
\omega_A = \bigcap_{\operatorname{ht} \mathfrak{p} = 1} A_\mathfrak{p}\,\omega_0 = A\,\omega_0 .
$$
So $\omega_A \cong A$ and $K_A = 0$ in $\operatorname{Cl}(A)$. This applies to the du Val singularities and to the quadric cone $xy - z^2$, whose class group is $\mathbb{Z}/2$ by Example P1.8.14: the canonical divisor is Cartier and trivial, although not every Weil divisor is Cartier. This agrees with Example P1.10.31.

**Example P1.12.30 (an affine elliptic curve).** Let $A = k[x, y]/(y^2 - x^3 - ax - b)$ be smooth, with $\operatorname{char} k \neq 2, 3$. The same computation in one dimension lower gives the residue form $\omega_0 = dx/(2y) = dy/(3x^2 + a)$ in $\Omega_{K/k}$. At each maximal ideal $\mathfrak{m}$ one of $2y$ and $3x^2 + a$ is a unit of $A_\mathfrak{m}$, since the curve is smooth, so $\omega_0$ lies in $(\Omega_A)_\mathfrak{m}$ and generates it. The module $\Omega_A$ is locally free, hence torsion-free, and it is the intersection of its localizations at the maximal ideals inside $\Omega_{K/k}$. So $\omega_0 \in \Omega_A$, and $\Omega_A = A\,\omega_0 \cong A$. Here $\omega_A = \Omega_A$, and $K_A = 0$.

### Exercises

1. (A) Let $A = k[x, y]/(xy)$. Show that $\Omega_A \otimes_A \kappa$ has dimension $2$ at the origin and $1$ at every other point, and that $(\Omega_A)_\mathfrak{m}$ is not free at the origin. Which hypothesis of the theorem fails?
2. (A) Let $k = \mathbb{F}_p(t)$ and $A = k[x]/(x^p - t)$. Show that $A$ is regular and $\Omega_A$ is free of rank $1$, while $\dim A = 0$. Which hypothesis of the theorem fails?
3. (A) Compute $K_{\mathbb{P}^1}$ with the form $du$ on the chart $x_0 \neq 0$, and check that it has degree $-2$.
4. (B) Let $f \in k[x_1, \dots, x_{n+1}]$ define a normal hypersurface $A$ with finitely many singular points, and $n \geq 2$. Show that the forms $(-1)^{i-1} dx_1 \wedge \dots \wedge \widehat{dx_i} \wedge \dots \wedge dx_{n+1} / f_{x_i}$ agree, and that their common value generates $\omega_A$.
5. (B) Let $A = k[x, y, z]/(xy - z^2)$ with $\operatorname{char} k \neq 2$. Compute the residue form $\omega_0$ in terms of $dx \wedge dz$ and show directly that $\omega_A = A\,\omega_0$ by checking that $\omega_0$ generates $(\Omega^2_A)_\mathfrak{p}$ at every height one prime.
6. (B) Let $A$ be as in the theorem, $\mathfrak{m}$ a maximal ideal with $A_\mathfrak{m}$ regular, and $t_1, \dots, t_d \in \mathfrak{m}$ whose images form a basis of $\mathfrak{m}/\mathfrak{m}^2$. Show that $dt_1, \dots, dt_d$ is a basis of $(\Omega_A)_\mathfrak{m}$. (Hint: use the cotangent space and Nakayama's lemma.)
7. (C) Let $A = k[x, y]/(y^2 - x^3)$ with $\operatorname{char} k \neq 2, 3$. Show that $\Omega_A$ is not free near the origin in two ways: with the theorem, and with the torsion form of Section 12.1.
8. (C) Let $X = \mathbb{P}^1 \times \mathbb{P}^1$ with the lines $F_1 = \{\infty\} \times \mathbb{P}^1$ and $F_2 = \mathbb{P}^1 \times \{\infty\}$. With the form $du \wedge dv$ on the chart $\mathbb{A}^2$, show that $K_X = -2F_1 - 2F_2$.

### Lean

Mathlib defines formally smooth algebras, `Algebra.FormallySmooth`, one of whose conditions is that the module of differentials is projective, smooth algebras, `Algebra.Smooth`, and exterior powers `⋀[R]^n M`. It does not prove the equivalence between regularity and freeness of the differentials over a perfect field, and it does not define the canonical module or the canonical divisor of a normal variety. The handbook adds no `MinimalModel` node here.

### Notes and history

The link between smoothness and the Jacobian matrix is classical, and Zariski's paper of 1947 on simple points made it precise over imperfect fields. The description of smoothness through differentials is due to Grothendieck in EGA IV. The residue form of a hypersurface goes back to Poincaré's residues of rational differential forms. The definition of $K_X$ for a normal variety through the smooth locus is the one used in the minimal model program since the work of Reid around 1980. The literature state of every result here is theorem. The section follows Matsumura, Chapter 9, and Eisenbud, Chapter 16.
