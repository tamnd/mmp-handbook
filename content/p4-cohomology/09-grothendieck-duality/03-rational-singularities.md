---
title: Rational singularities and Kempf's criterion
nodes: []
sources: [KKMS73, KM98, Kov00, Har77]
reads_with: [KM98:ch5]
requires: [P1.11, P2.8, P3.7, P3.12, P4.4, P4.6, P4.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Rational singularities and Kempf's criterion

### Statement

Let $k$ be an algebraically closed field of characteristic $0$, and $X$ a variety over $k$ of dimension $n$, quasi-projective so that Section 9.2 applies. A *resolution* of $X$ is a proper birational morphism $f \colon Y \to X$ from a smooth variety $Y$. Resolutions exist by Hironaka's theorem, a black box stated in P8 Chapter 5, and they can be chosen projective. The second black box of this section is the Grauert-Riemenschneider vanishing theorem, stated as Theorem P2.8.26 and proved in P7: for a resolution $f \colon Y \to X$, $R^i f_* \omega_Y = 0$ for $i > 0$. Write $\omega_X = \mathcal{H}^{-n}(\omega^\bullet_X)$, which is the sheaf $\omega^\circ_X$ of Section 7.3 and, for $X$ normal, the sheaf $j_* \omega_U$ of Corollary P4.7.22.

**Definition P4.9.18 (rational singularities).** The variety $X$ has *rational singularities* if it has a resolution $f \colon Y \to X$ with $Rf_* \mathcal{O}_Y = \mathcal{O}_X$, that is, $f_* \mathcal{O}_Y = \mathcal{O}_X$ and $R^i f_* \mathcal{O}_Y = 0$ for $i > 0$.

For any resolution, $f_* \mathcal{O}_Y$ is the integral closure of $\mathcal{O}_X$ in the function field, by the Zariski main theorem in the form of Corollary P4.6.10, so $f_* \mathcal{O}_Y = \mathcal{O}_X$ holds exactly when $X$ is normal. A variety with rational singularities is normal.

**Lemma P4.9.19 (smooth varieties).** Let $g \colon Y' \to Y$ be a proper birational morphism of smooth varieties. Then $g_* \omega_{Y'} = \omega_Y$ and $Rg_* \mathcal{O}_{Y'} = \mathcal{O}_Y$.

Lean: not in Lean as stated.

**Proposition P4.9.20 (independence of the resolution).** If $Rf_* \mathcal{O}_Y = \mathcal{O}_X$ for one resolution $f \colon Y \to X$, then $Rf'_* \mathcal{O}_{Y'} = \mathcal{O}_X$ for every resolution $f' \colon Y' \to X$. In particular smooth varieties have rational singularities.

Lean: not in Lean as stated.

**Theorem P4.9.21 (Kempf's criterion).** Let $f \colon Y \to X$ be a resolution.

1. There is a natural injection $f_* \omega_Y \hookrightarrow \omega_X$ when $X$ is normal.
2. $Rf_* \omega_Y[n] \cong \mathbb{D}_X(Rf_* \mathcal{O}_Y)$.
3. $X$ has rational singularities if and only if $X$ is normal, Cohen-Macaulay and $f_* \omega_Y = \omega_X$.

Lean: not in Lean as stated.

**Corollary P4.9.22.** Let $X$ be a variety.

1. If $X$ has rational singularities, then $X$ is Cohen-Macaulay.
2. Suppose $X$ is normal, Gorenstein, so that $\omega_X$ is invertible and $K_X$ is Cartier. Let $f \colon Y \to X$ be a resolution and write $K_Y = f^* K_X + \sum_i a_i E_i$ with $E_i$ the exceptional prime divisors, as in Section P3.12. Then $X$ has rational singularities if and only if $a_i \geq 0$ for all $i$.

Lean: not in Lean as stated.

**Proposition P4.9.23 (cones).** Let $V$ be a smooth projective variety of dimension $n - 1 \geq 1$ and $L$ an ample line bundle on $V$ such that the ring $S = \bigoplus_{m \geq 0} H^0(V, L^m)$ is normal and generated in degree $1$. Let $C = \operatorname{Spec} S$ be the affine cone, with vertex $0$. Then $C$ has rational singularities if and only if $H^i(V, L^m) = 0$ for all $i > 0$ and $m \geq 0$.

Lean: not in Lean as stated.

### Proof in words

Duality turns $Rf_* \mathcal{O}_Y$ into $Rf_* \omega_Y[n]$, and Grauert-Riemenschneider says that the second is a sheaf in one degree. So $Rf_* \mathcal{O}_Y$ is a sheaf exactly when $\mathbb{D}_X$ of a sheaf in degree $-n$ is a sheaf in degree $0$. If $Rf_* \mathcal{O}_Y = \mathcal{O}_X$, then $\mathbb{D}_X \mathcal{O}_X = \omega^\bullet_X$ is the sheaf $f_* \omega_Y$ in degree $-n$, which is the Cohen-Macaulay condition, and $\omega_X = f_* \omega_Y$. Conversely, if $X$ is Cohen-Macaulay and $f_* \omega_Y = \omega_X$, then $Rf_* \omega_Y[n] = \omega^\bullet_X$, and dualizing again gives $Rf_* \mathcal{O}_Y = \mathcal{O}_X$. For Gorenstein $X$, the condition $f_* \omega_Y = \omega_X$ asks that forms on the smooth locus extend holomorphically across the exceptional divisors, which is a condition on the discrepancies $a_i$.

### Examples

**Example P4.9.24 (surface cones).** Let $V = \mathbb{P}^1$ and $L = \mathcal{O}(d)$, $d \geq 1$. The cone $C$ is the cone over the rational normal curve of degree $d$, and $H^1(\mathbb{P}^1, \mathcal{O}(md)) = 0$ for $m \geq 0$, so $C$ has rational singularities by Proposition P4.9.23. Let instead $V = E$ be an elliptic curve and $L$ of degree $d \geq 3$. Then $H^1(E, \mathcal{O}_E) = k \neq 0$, so the cone is not rational. It is Cohen-Macaulay, as every normal surface is (Corollary P1.11.13), so by Kempf's criterion $f_* \omega_Y \neq \omega_C$. Concretely, the generator of $\omega_C$ near the vertex has a pole of order $1$ along the exceptional curve $E$ of the resolution: here $\omega_C$ is invertible and $K_Y = f^* K_C - E$, by adjunction on the exceptional curve with $K_E = 0$.

**Example P4.9.25 (an abelian surface).** Let $V = A$ be an abelian surface and $L$ a very ample line bundle with projectively normal embedding. Then $H^1(A, \mathcal{O}_A) = k^2 \neq 0$, and the cone is not rational. It is not even Cohen-Macaulay, by Example P4.8.16.

**Example P4.9.26 (the $A_n$ singularities).** Let $X = \{xy = z^{n+1}\} \subseteq \mathbb{A}^3$. It is a hypersurface, hence Gorenstein, and the minimal resolution, obtained by blowing up the vertex repeatedly, has a chain of $n$ smooth rational curves $E_1, \dots, E_n$ with $E_i^2 = -2$ as exceptional locus. By adjunction $K_Y \cdot E_i = 0$ for each $i$, and since the intersection matrix of the $E_i$ is negative definite, $K_Y = f^* K_X$, so all $a_i = 0$. By Corollary P4.9.22, $X$ has rational singularities. The same holds for the other du Val singularities $D_n$, $E_6$, $E_7$, $E_8$.

**Example P4.9.27 (cones over Fano varieties).** Let $V$ be a smooth Fano variety, that is, $-K_V$ is ample, and $L$ ample with $S$ normal and generated in degree $1$. For $m \geq 0$, $L^m - K_V$ is ample, so the Kodaira vanishing theorem (P7) gives $H^i(V, L^m) = H^i(V, K_V + (L^m - K_V)) = 0$ for $i > 0$. By Proposition P4.9.23 the cone has rational singularities. The cone over a smooth quadric surface, the singularity $xy = zw$, is an example. Quotient singularities $\mathbb{A}^n / G$ for finite groups $G$ are rational as well, by a result of Viehweg and Boutot.

### Proof

*Lemma P4.9.19.* Both $Y$ and $Y'$ are smooth, so $\omega_Y = \Omega^n_Y$ and $\omega_{Y'} = \Omega^n_{Y'}$ by part 4 of Theorem P4.9.13. Pullback of $n$-forms gives an injection $g^* \Omega^n_Y \to \Omega^n_{Y'}$, and by adjunction a map $\Omega^n_Y \to g_* \Omega^n_{Y'}$. It is injective, since $g$ is an isomorphism over a dense open set. It is surjective. The rational map $g^{-1} \colon Y \dashrightarrow Y'$ is defined on an open set $Y^\circ \subseteq Y$ whose complement has codimension at least $2$, because $Y$ is normal and $g$ is proper: at a codimension $1$ point the local ring of $Y$ is a discrete valuation ring, and the valuative criterion extends $g^{-1}$ across it. Over $Y^\circ$, the morphism $g^{-1}$ is a section of $g$, so a section $\eta$ of $g_* \Omega^n_{Y'}$ over an open $W \subseteq Y$ restricts to the $n$-form $(g^{-1})^* \eta$ on $W \cap Y^\circ$, which agrees with $\eta$ where $g$ is an isomorphism. Since $\Omega^n_Y$ is locally free and $Y$ is normal, this form extends to $W$ by the Hartogs property (Theorem P3.7.33), and its pullback is $\eta$ because the two agree on a dense open set. Hence $g_* \omega_{Y'} = \omega_Y$.

The morphism $g$ is a resolution of the smooth variety $Y$, so Grauert-Riemenschneider gives $R^i g_* \omega_{Y'} = 0$ for $i > 0$, and $Rg_* \omega_{Y'} = \omega_Y$. Since $\omega^\bullet_{Y'} = \omega_{Y'}[n]$ and $\omega^\bullet_Y = \omega_Y[n]$, Theorem P4.9.13, part 1, applied to $K = \mathcal{O}_{Y'}$ gives
$$\omega_Y[n] = Rg_* \omega_{Y'}[n] = Rg_* \mathbb{D}_{Y'} \mathcal{O}_{Y'} \cong \mathbb{D}_Y Rg_* \mathcal{O}_{Y'}.$$
Applying $\mathbb{D}_Y$ and Theorem P4.9.4, part 1, $Rg_* \mathcal{O}_{Y'} \cong \mathbb{D}_Y(\omega_Y[n]) = \mathcal{O}_Y$. The isomorphism is the natural map $\mathcal{O}_Y \to Rg_* \mathcal{O}_{Y'}$, since both are the identity on $W^\circ$ and $\operatorname{Hom}(\mathcal{O}_Y, \mathcal{O}_Y) = \Gamma(Y, \mathcal{O}_Y)$ has no sections supported on a proper closed set.

*Proposition P4.9.20.* Let $f \colon Y \to X$ and $f' \colon Y' \to X$ be resolutions with $Rf_* \mathcal{O}_Y = \mathcal{O}_X$. Let $Z$ be the closure of the graph of the birational map $Y \dashrightarrow Y'$ in $Y \times_X Y'$, and let $Y''$ be a resolution of $Z$ by Hironaka's theorem. The maps $g \colon Y'' \to Y$ and $g' \colon Y'' \to Y'$ are proper birational morphisms of smooth varieties, and $f g = f' g'$. By Lemma P4.9.19 and the composition of derived functors (Proposition P2.8.18),
$$Rf'_* \mathcal{O}_{Y'} = Rf'_* Rg'_* \mathcal{O}_{Y''} = Rf_* Rg_* \mathcal{O}_{Y''} = Rf_* \mathcal{O}_Y = \mathcal{O}_X.$$
For $X$ smooth, take $f = \mathrm{id}_X$.

*Theorem P4.9.21, part 2.* This is part 1 of Theorem P4.9.13 for $K = \mathcal{O}_Y$, with $\mathbb{D}_Y \mathcal{O}_Y = \omega^\bullet_Y = \omega_Y[n]$.

*Part 1.* Let $U \subseteq X$ be the smooth locus, an open set with complement of codimension at least $2$ since $X$ is normal. Over $U$, $f$ is a resolution of a smooth variety, so $f_* \omega_Y|_U = \omega_U$ by Lemma P4.9.19. The sheaf $f_* \omega_Y$ is torsion free, so the restriction map $f_* \omega_Y \to j_* (f_* \omega_Y|_U) = j_* \omega_U = \omega_X$ is injective, the last equality by Corollary P4.7.22.

*Part 3.* Suppose $X$ has rational singularities. Then $X$ is normal. By part 2 and Grauert-Riemenschneider,
$$\omega^\bullet_X = \mathbb{D}_X \mathcal{O}_X = \mathbb{D}_X Rf_* \mathcal{O}_Y \cong Rf_* \omega_Y[n] = (f_* \omega_Y)[n].$$
So $\omega^\bullet_X$ has cohomology only in degree $-n$, and $X$ is Cohen-Macaulay by part 3 of Proposition P4.9.7. Taking $\mathcal{H}^{-n}$ gives $\omega_X \cong f_* \omega_Y$. The isomorphism is the inclusion of part 1, because both are the identity over $U$.

Conversely, suppose $X$ is normal, Cohen-Macaulay and $f_* \omega_Y = \omega_X$. By Grauert-Riemenschneider and part 3 of Proposition P4.9.7, $Rf_* \omega_Y[n] = (f_* \omega_Y)[n] = \omega_X[n] \cong \omega^\bullet_X$. By part 2 and Theorem P4.9.4, part 1,
$$Rf_* \mathcal{O}_Y \cong \mathbb{D}_X \mathbb{D}_X Rf_* \mathcal{O}_Y \cong \mathbb{D}_X(Rf_* \omega_Y[n]) \cong \mathbb{D}_X \omega^\bullet_X = \mathcal{O}_X.$$
So $R^i f_* \mathcal{O}_Y = 0$ for $i > 0$, and $X$ has rational singularities.

*Corollary P4.9.22, part 1* is part 3 of Theorem P4.9.21.

*Part 2.* Let $A = \sum_{a_i > 0} a_i E_i$ and $B = \sum_{a_i < 0} (-a_i) E_i$, effective divisors without common components, so that $\omega_Y = f^* \omega_X \otimes \mathcal{O}_Y(A - B)$. By the projection formula (Proposition P4.4.10), $f_* \omega_Y = \omega_X \otimes f_* \mathcal{O}_Y(A - B)$. A Gorenstein variety is Cohen-Macaulay, so by Theorem P4.9.21, $X$ has rational singularities if and only if $f_* \mathcal{O}_Y(A - B) = \mathcal{O}_X$.

The sheaf $f_* \mathcal{O}_Y(A - B)$ is contained in $f_* \mathcal{O}_Y(A)$, which equals $\mathcal{O}_X$: a rational function $h$ with $\operatorname{div}(f^* h) + A \geq 0$ is regular on $X$ minus the image of the exceptional set, which has codimension at least $2$, so $h$ is regular on $X$ by normality. So $f_* \mathcal{O}_Y(A - B)$ is the ideal of functions $h \in \mathcal{O}_X$ with $\operatorname{div}(f^* h) \geq B$. If $B = 0$, this ideal is $\mathcal{O}_X$. If $B \neq 0$, the function $1$ is not in it, so it is a proper ideal. Hence $f_* \mathcal{O}_Y(A - B) = \mathcal{O}_X$ if and only if $B = 0$, that is, all $a_i \geq 0$.

*Proposition P4.9.23.* Let $Y = \operatorname{Spec}_V \bigoplus_{m \geq 0} L^m$ be the total space of the dual line bundle $L^{-1}$, with projection $\pi \colon Y \to V$ and zero section $V_0 \subseteq Y$. The morphism $\pi$ is affine. The global sections $H^0(Y, \mathcal{O}_Y) = \bigoplus_m H^0(V, L^m) = S$ give a morphism $f \colon Y \to C$, which contracts $V_0$ to the vertex and is an isomorphism elsewhere, because $L$ is very ample, as $S$ is generated in degree $1$. So $f$ is a resolution of $C$. Since $\pi$ is affine, Corollary P4.4.3 gives $H^i(Y, \mathcal{O}_Y) = H^i(V, \pi_* \mathcal{O}_Y) = \bigoplus_{m \geq 0} H^i(V, L^m)$. Since $C$ is affine, Proposition P4.4.2 gives $R^i f_* \mathcal{O}_Y = H^i(Y, \mathcal{O}_Y)^\sim$. So $R^i f_* \mathcal{O}_Y = 0$ for $i > 0$ if and only if $H^i(V, L^m) = 0$ for all $i > 0$, $m \geq 0$. Finally $f_* \mathcal{O}_Y = \widetilde{S} = \mathcal{O}_C$, and by Proposition P4.9.20 the condition does not depend on the resolution.

### Exercises

1. (A) Show that a normal surface singularity whose minimal resolution has a single exceptional curve $E \cong \mathbb{P}^1$ with $E^2 = -d$ is rational. Identify it with the cone of Example P4.9.24.
2. (A) Let $X = \{x^3 + y^3 + z^3 = 0\} \subseteq \mathbb{A}^3$. Show that $X$ is the cone over an elliptic curve, and compute the discrepancy of the exceptional curve of the blow-up of the vertex.
3. (B) Let $n \geq 3$, $V \subseteq \mathbb{P}^{n-1}$ a smooth hypersurface of degree $d$ and $C \subseteq \mathbb{A}^n$ its affine cone. Show that $C$ has rational singularities if and only if $d \leq n - 1$, that is, if and only if $V$ is Fano.
4. (B) Let $X$ have rational singularities and $f \colon Y \to X$ be a resolution. Show that $H^i(Y, \mathcal{O}_Y) = H^i(X, \mathcal{O}_X)$ for all $i$, and deduce that the arithmetic genus is a birational invariant of smooth projective varieties in characteristic $0$.
5. (B) Let $X$ be a normal variety of dimension $n \geq 2$ with a single singular point $x$, and $f \colon Y \to X$ a resolution that is an isomorphism over $X \setminus \{x\}$. Use the triangle $\mathcal{O}_X \to Rf_* \mathcal{O}_Y \to Q \to$, part 2 of Theorem P4.9.21 and Matlis duality to show that $\mathcal{H}^{-i-1}(\omega^\bullet_X)_x$ is Matlis dual to $R^i f_* \mathcal{O}_Y$ for $1 \leq i \leq n - 2$, and that $\omega_X / f_* \omega_Y$ is Matlis dual to $R^{n-1} f_* \mathcal{O}_Y$. Deduce that $X$ is Cohen-Macaulay if and only if $R^i f_* \mathcal{O}_Y = 0$ for $0 < i < n - 1$.
6. (C) Let $X$ have rational singularities and $H \subseteq X$ a general member of a base point free linear system. Show that $H$ has rational singularities. Use Bertini's theorem for $f^* H$ on a resolution $f \colon Y \to X$, the sequence $0 \to \mathcal{O}_Y(-f^* H) \to \mathcal{O}_Y \to \mathcal{O}_{f^* H} \to 0$ and the projection formula. Explain why the case of a general hyperplane through a fixed singular point, Elkik's theorem, needs more.

### Lean

Mathlib has neither resolutions of singularities nor the coherent duality used here. The handbook adds no `MinimalModel` node here. Hironaka's theorem and the Grauert-Riemenschneider theorem enter as the black boxes of P8 Chapter 5 and P7, with Lean hypotheses not yet named.

### Notes and history

Rational singularities of surfaces were introduced by Artin in 1966, who showed that they are the surface singularities whose deformations and resolutions behave like those of smooth points. Kempf defined them in all dimensions and proved the criterion of Theorem P4.9.21 in the toroidal embeddings volume of 1973 (KKMS73). Elkik proved in 1978 that rational singularities deform to rational singularities, and Boutot proved in 1987 that quotients of rational singularities by reductive groups are rational. Kovács (Kov00) gave a characterization by a splitting of $\mathcal{O}_X \to Rf_* \mathcal{O}_Y$ that applies to any morphism from a variety with rational singularities. The literature state is theorem. In the minimal model program, rational singularities enter through the theorem that klt singularities are rational (Kollár and Mori, Theorem 5.22), proved in Volume 4, which makes the duality of this chapter available on the varieties that the program produces.
