---
title: Rational singularities and quotients
nodes: []
sources: [Kov00, KM98, Art66, Kol13]
reads_with: [KM98:5.1, Kov00:all, Kol13:ch2]
requires: [P4.6, P4.9, P8.6, P8.7, P8.9, P8.10]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Rational singularities and quotients

### Statement

In this section $k$ has characteristic $0$, so that resolutions of singularities exist. Recall from Definition P4.9.18 that a variety $X$ has *rational singularities* if it is normal and $R f_* \mathcal{O}_Y = \mathcal{O}_X$ for a resolution $f \colon Y \to X$, that is, $f_* \mathcal{O}_Y = \mathcal{O}_X$ and $R^i f_* \mathcal{O}_Y = 0$ for $i > 0$. By Proposition P4.9.20 the condition does not depend on the resolution, by part 1 of Corollary P4.9.22 rational singularities are Cohen-Macaulay, by Theorem P4.9.21 they are characterized by Kempf's criterion $f_* \omega_Y = \omega_X$, and by part 2 of Corollary P4.9.22 a Gorenstein variety has rational singularities if and only if all discrepancies $a_i$ of $K_Y = f^* K_X + \sum a_i E_i$ are nonnegative. The condition is local on $X$, so a point $x \in X$ is a *rational singularity* if some neighbourhood of $x$ has rational singularities. This section adds one more tool, a splitting criterion, and applies it to quotients.

**Definition P8.11.1 (split morphisms).** A morphism $g \colon Z \to X$ of varieties is *split* if the natural map $\mathcal{O}_X \to R g_* \mathcal{O}_Z$ has a left inverse in the derived category of $\mathcal{O}_X$-modules, that is, a morphism $\tau \colon R g_* \mathcal{O}_Z \to \mathcal{O}_X$ with $\tau \circ g^\# = \operatorname{id}$. For a finite morphism $R g_* \mathcal{O}_Z = g_* \mathcal{O}_Z$, and the condition is that $\mathcal{O}_X \to g_* \mathcal{O}_Z$ has an $\mathcal{O}_X$-linear left inverse.

**Theorem P8.11.2 (Kovács's splitting criterion).** Let $g \colon Z \to X$ be a split morphism of varieties over $k$ of characteristic $0$. If $Z$ has rational singularities, then so does $X$.

Lean: not in Lean as stated.

**Theorem P8.11.3 (quotients of rational singularities).** Let $G$ be a finite group acting on an affine variety $V$ with rational singularities, for instance a smooth one. Then $X = V/G$ has rational singularities. In particular $\mathbb{A}^n / G$ has rational singularities for every finite $G \subseteq GL_n(k)$, and so does $V/G$ for $V$ quasi-projective and smooth.

Lean: not in Lean as stated.

**Corollary P8.11.4 (quotients are Cohen-Macaulay).** For every finite $G \subseteq GL_n(k)$ the ring of invariants $k[x_1, \dots, x_n]^G$ is Cohen-Macaulay.

Lean: not in Lean as stated.

**Corollary P8.11.5 (small subgroups of $SL_n$).** Let $G \subseteq SL_n(k)$ be finite and small, $X = \mathbb{A}^n / G$ and $f \colon Y \to X$ a resolution. Then $K_X$ is Cartier, and $K_Y = f^* K_X + \sum_i a_i E_i$ with every $a_i \geq 0$.

Lean: not in Lean as stated.

**Corollary P8.11.6 (quotients by finite subgroups of $SL_2$ are Du Val).** Let $G \subseteq SL_2(k)$ be a nontrivial finite subgroup. Then the image of the origin in $\mathbb{A}^2 / G$ is a Du Val singularity.

Lean: not in Lean as stated.

### Proof in words

A morphism whose structure map splits behaves, for the purposes of cohomology, as if the target were a direct summand of the source, and Kovács shows by Grothendieck duality and the Grauert-Riemenschneider vanishing theorem that rationality descends along such morphisms. For a quotient by a finite group, the Reynolds operator is the splitting. A quotient of affine space is therefore rational, hence Cohen-Macaulay, and when the group lies in $SL_n$ and is small it is also Gorenstein, so all discrepancies of a resolution are nonnegative. In dimension two this lands on the characterization of Du Val singularities as the rational Gorenstein points.

### Examples

**Example P8.11.7 (the singularity $\frac{1}{2}(1, 1, 1)$).** By Theorem P8.11.3 the quotient $X = \mathbb{A}^3 / \{ \pm 1 \}$ of Example P8.9.11 has rational singularities. This agrees with Proposition P4.9.23: $X$ is the affine cone over $V = \mathbb{P}^2$ with $L = \mathcal{O}(2)$, its coordinate ring $\bigoplus_m H^0(\mathbb{P}^2, \mathcal{O}(2m))$ is the ring of even degree polynomials, normal and generated in degree $1$, and $H^i(\mathbb{P}^2, \mathcal{O}(2m)) = 0$ for $i > 0$ and $m \geq 0$. The group $\{ \pm 1 \}$ is small but not in $SL_3$, since $\det(-1) = -1$, and indeed $K_X$ is not Cartier but $2 K_X$ is, by part 2 of Proposition P8.9.16 with $e = 2$ and by Chapter 12.

**Example P8.11.8 (cones that are not quotient singularities).** The cone over an elliptic curve and the cone over an abelian surface are not rational, by Examples P4.9.24 and P4.9.25. By Theorem P8.11.3 they are not isomorphic to an open subset of any quotient $V/G$ with $V$ smooth.

**Example P8.11.9 (a rational point that is not a quotient).** Let $X = \{ xy = zw \} \subseteq \mathbb{A}^4$, the affine cone over a smooth quadric surface, which is the toric variety of the cone over a square of Example P8.6.10. It has rational singularities by Example P4.9.27, and it is Gorenstein, being a hypersurface. By Example P8.7.14 the divisor $D_1$ is not $\mathbb{Q}$-Cartier at the vertex. By Proposition P8.9.4 every Weil divisor on $\mathbb{A}^3 / G$ is $\mathbb{Q}$-Cartier, so no neighbourhood of the vertex is isomorphic to an open subset of a quotient $\mathbb{A}^3 / G$. Rational singularities form a strictly larger class than quotient singularities.

### Proof

*Theorem P8.11.2.* This is Kovács (Kov00), Theorem 1, stated there over $\mathbb{C}$; the Lefschetz principle extends it to every algebraically closed field of characteristic $0$. The proof uses the Grauert-Riemenschneider vanishing theorem $R^i f_* \omega_Y = 0$ for $i > 0$ and a resolution $f \colon Y \to X$, together with Grothendieck duality as in Theorem P4.9.21, to show that $\mathcal{O}_X \to R f_* \mathcal{O}_Y$ is an isomorphism.

*Theorem P8.11.3.* Let $\pi \colon V \to X$ be the quotient map, which is finite by Theorem P8.9.3, and write $V = \operatorname{Spec} A$, $X = \operatorname{Spec} A^G$. The Reynolds operator $R \colon A \to A^G$ of Lemma P8.9.2 is $A^G$-linear and satisfies $R(a) = a$ for $a \in A^G$. Since $X$ is affine, $R$ is a morphism of quasi-coherent sheaves $\pi_* \mathcal{O}_V \to \mathcal{O}_X$ that is a left inverse of $\mathcal{O}_X \to \pi_* \mathcal{O}_V$. By Definition P8.11.1, $\pi$ is split, and Theorem P8.11.2 shows that $X$ has rational singularities. For $V = \mathbb{A}^n$ smooth, $V$ has rational singularities by Proposition P4.9.20. For $V$ quasi-projective, $V/G$ is covered by the quotients of $G$-stable affine open subsets (Exercise 6 of Section 9.1), and rationality is local.

*Corollary P8.11.4.* By Theorem P8.11.3 and part 1 of Corollary P4.9.22, $\mathbb{A}^n / G$ is Cohen-Macaulay, so its coordinate ring is Cohen-Macaulay at every maximal ideal, hence Cohen-Macaulay.

*Corollary P8.11.5.* By part 2 of Proposition P8.9.16, $K_X \sim 0$ is Cartier. Since $X$ is Cohen-Macaulay by Corollary P8.11.4 and $\omega_X \cong \mathcal{O}_X$ is invertible, $X$ is Gorenstein. By Theorem P8.11.3 it has rational singularities, and part 2 of Corollary P4.9.22 gives $a_i \geq 0$ for every $i$.

*Corollary P8.11.6.* A nontrivial element $g \in SL_2(k)$ of finite order is diagonalizable with eigenvalues $\lambda, \lambda^{-1}$; if one of them is $1$ both are, and $g = 1$. So $G$ contains no pseudo-reflection, it is small, and $X = \mathbb{A}^2 / G$ has $K_X \sim 0$ by Proposition P8.9.16. The image $x$ of the origin is singular. Otherwise $X$ is smooth near $x$, and $\pi$ is a finite morphism from the normal surface $\mathbb{A}^2$ that is étale outside the single point $0$ over $x$, by part 1 of Proposition P8.9.16. By the purity of the branch locus (SGA 1, Exposé X, Théorème 3.1) $\pi$ is then étale at $0$ as well, so the fibre over $x$ has $|G| > 1$ points, while it is the single orbit $\{ 0 \}$ by Theorem P8.9.3. By Theorem P8.11.3 the point is rational, and it is Gorenstein because $K_X$ is Cartier and normal surfaces are Cohen-Macaulay. Condition 4 of Theorem P8.10.12 holds, so the point is Du Val.

### Exercises

1. (A) Show that the quadric cone $\mathbb{A}^2 / \{ \pm 1 \}$ is Du Val by Corollary P8.11.6, and compare with Example P8.10.6.
2. (A) Show that the ring $k[s^4, s^3 t, s t^3, t^4]$ is neither normal nor Cohen-Macaulay, and deduce from Corollary P8.11.4 and Theorem P8.9.3 that it is not a ring of invariants of a finite group acting on a polynomial ring.
3. (B) Let $G$ act on a normal affine variety $V$. Show directly, without Theorem P8.11.2, that $H^i(U, \mathcal{O}_U)^G = H^i(U/G, \mathcal{O}_{U/G})$ for every $G$-stable open $U \subseteq V$ with an affine quotient map, using Lemma P8.9.2.
4. (B) Show that the binary dihedral group of order $8$, generated by $\operatorname{diag}(i, -i)$ and $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, has invariants $x^2 y^2$, $x^4 + y^4$ and $xy(x^4 - y^4)$, and find the relation among them. Identify the singularity using Theorem P8.10.5.
5. (B) Let $G \subseteq GL_n(k)$ be finite and small with $G \not\subseteq SL_n(k)$. Using Watanabe's theorem quoted in the Notes of Section 9.2, show that $\mathbb{A}^n / G$ is rational but not Gorenstein.
6. (C) Show that Theorem P8.11.2 fails if the splitting is only required on $\mathcal{O}_X \to g_* \mathcal{O}_Z$, not on $R g_* \mathcal{O}_Z$, by considering the blow-up of the vertex of the cone over an elliptic curve.

### Lean

Rational singularities are not in the repository. The klt condition `MinimalModel.IsKlt` is stated in `MinimalModel/Statements/Basic.lean`; that klt singularities are rational is a theorem of Elkik and of Kollár and Mori, Section 5.2, which is not formalized there.

### Notes and history

That quotient singularities are rational is due to Viehweg in 1977 in characteristic $0$; Boutot (1987) proved more generally that the quotient of a variety with rational singularities by a reductive group is rational, and Kovács's criterion (Kov00) gives the short proof above. Hochster and Eagon proved Corollary P8.11.4 directly in 1971, in every characteristic not dividing $|G|$, by the Reynolds operator and local cohomology. The formal version, that every quotient singularity in the sense of Definition P8.9.7 is rational, follows because rationality is local in the étale topology and two singularities with isomorphic completions have a common étale neighbourhood, by Artin's approximation theorem (Publications Mathématiques de l'IHÉS 36, 1969). Kollár (Kol13, Chapter 2) treats rational singularities in the setting of the minimal model program.
