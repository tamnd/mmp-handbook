---
title: The Lefschetz theorem on (1,1)-classes
nodes: []
sources: [Huy05, GH78, Voi02, Lef21a, Mum70a]
reads_with: [Huy05:3.3, GH78:1.2, Voi02:7, Mum70a:1]
requires: [P2.7, P6.4, P7.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Lefschetz theorem on (1,1)-classes

### Statement

Let $X$ be a compact Kähler manifold of dimension $n$. The Hodge decomposition $H^2(X, \mathbb{C}) = H^{2,0}(X) \oplus H^{1,1}(X) \oplus H^{0,2}(X)$ of Theorem P6.4.16 is compatible with complex conjugation, which exchanges $H^{2,0}$ and $H^{0,2}$ and preserves $H^{1,1}$. Write $H^{1,1}(X, \mathbb{R}) = H^{1,1}(X) \cap H^2(X, \mathbb{R})$, a real vector space of dimension $h^{1,1}(X)$.

**Definition P6.5.11 (Néron-Severi group, Picard number and integral $(1,1)$-classes).** The *Néron-Severi group* of $X$ is the image $\operatorname{NS}(X) \subseteq H^2(X, \mathbb{Z})$ of $c_1 \colon \operatorname{Pic}(X) \to H^2(X, \mathbb{Z})$, and its rank $\rho(X)$ is the *Picard number*. The group of *integral $(1,1)$-classes* is
$$H^{1,1}(X, \mathbb{Z}) = \{ c \in H^2(X, \mathbb{Z}) : \text{the image of } c \text{ in } H^2(X, \mathbb{C}) \text{ lies in } H^{1,1}(X) \}.$$
It contains the torsion subgroup of $H^2(X, \mathbb{Z})$, whose image in $H^2(X, \mathbb{C})$ is zero.

**Lemma P6.5.12 (real classes of type $(1,1)$).** A class $a \in H^2(X, \mathbb{R})$ lies in $H^{1,1}(X, \mathbb{R})$ if and only if its image under the map $\iota \colon H^2(X, \mathbb{C}) \to H^2(X, \mathcal{O}_X)$ of Lemma P6.5.7 is zero.

Lean: not in Lean as stated.

**Theorem P6.5.13 (Lefschetz (1,1)).** Let $X$ be a compact Kähler manifold. A class $c \in H^2(X, \mathbb{Z})$ is the first Chern class of a holomorphic line bundle if and only if its image in $H^2(X, \mathbb{C})$ is of type $(1,1)$:
$$\operatorname{NS}(X) = H^{1,1}(X, \mathbb{Z}).$$

Lean: not in Lean as stated.

**Corollary P6.5.14 (the Picard number).** $\operatorname{NS}(X) \otimes \mathbb{R}$ maps isomorphically onto a subspace of $H^{1,1}(X, \mathbb{R})$, and $\rho(X) \leq h^{1,1}(X)$.

Lean: not in Lean as stated.

**Corollary P6.5.15 (vanishing of $h^{0,2}$).** If $h^{0,2}(X) = 0$, then $c_1 \colon \operatorname{Pic}(X) \to H^2(X, \mathbb{Z})$ is surjective and $\rho(X) = b_2(X)$. If also $h^{0,1}(X) = 0$, then $c_1 \colon \operatorname{Pic}(X) \to H^2(X, \mathbb{Z})$ is an isomorphism.

Lean: not in Lean as stated.

### Proof in words

The exponential sequence gives the exact segment $\operatorname{Pic}(X) \to H^2(X, \mathbb{Z}) \to H^2(X, \mathcal{O}_X)$, so a class is a Chern class exactly when its image in $H^2(X, \mathcal{O}_X)$ vanishes. That image is computed in two steps, through $H^2(X, \mathbb{C})$, and the second step is the projection to the $(0,2)$-part of the Hodge decomposition. A real class has a $(2,0)$-part conjugate to its $(0,2)$-part, so the $(0,2)$-part vanishes exactly when the class is of type $(1,1)$. Integral classes are real, and the theorem follows.

Over the rationals the theorem says that $\operatorname{NS}(X) \otimes \mathbb{Q}$ is the space of rational classes of type $(1,1)$. On a projective manifold every line bundle is the line bundle of a divisor, by Chapter 7, so the rational $(1,1)$-classes are the classes of divisors: this is the Hodge conjecture in degree $2$, the one case of the conjecture that is a theorem. The Hodge conjecture in higher degree is open.

The examples compute $\operatorname{NS}(X)$ on tori, where both the integral structure and the Hodge decomposition are explicit. A product of two copies of an elliptic curve has Picard number $3$ or $4$, according as the curve has complex multiplication or not, and a suitable two-dimensional torus has no nontrivial line bundle classes at all.

### Examples

On a complex torus $X = V / \Lambda$, with $V = \mathbb{C}^n$ and $\Lambda \cong \mathbb{Z}^{2n}$ a lattice, the de Rham cohomology is represented by translation invariant forms, and $H^k(X, \mathbb{Z}) = \bigwedge^k \operatorname{Hom}(\Lambda, \mathbb{Z})$, the alternating integral $k$-forms on $\Lambda$ (Mum70a, Section 1; Huy05, Section 3.3). A translation invariant form $\sum \alpha_{IJ} dz_I \wedge d\bar z_J$ with constant coefficients is harmonic for the flat metric, and its $(p,q)$-parts give the Hodge decomposition. So a class in $H^2(X, \mathbb{Z})$ is an alternating form $E \colon \Lambda \times \Lambda \to \mathbb{Z}$, extended $\mathbb{R}$-bilinearly to $V$, and it has type $(1,1)$ if and only if its $(0,2)$-part vanishes. For $n = 2$ the space $H^{2,0}$ is spanned by $\sigma = dz_1 \wedge dz_2$, and a real $2$-form $E$ has vanishing $(0,2)$-part if and only if $E \wedge \sigma = 0$, because $E^{1,1} \wedge \sigma$ and $E^{2,0} \wedge \sigma$ have type $(3,1)$ and $(4,0)$ and vanish, while $E^{0,2} \wedge \sigma = 0$ forces $E^{0,2} = 0$.

**Example P6.5.16 (the square of an elliptic curve).** Let $\tau$ lie in the upper half plane, $E_\tau = \mathbb{C}/(\mathbb{Z} + \tau \mathbb{Z})$ and $X = E_\tau \times E_\tau$. On the $k$-th factor write $z_k = x_k + \tau y_k$, with $dx_k, dy_k$ the integral basis of $H^1(E_\tau, \mathbb{Z})$ dual to $1, \tau$. Then $dz_k = dx_k + \tau dy_k$, $d\bar z_k = dx_k + \bar\tau dy_k$, and
$$dy_k = \frac{dz_k - d\bar z_k}{\tau - \bar \tau}, \qquad dx_k = \frac{-\bar\tau \, dz_k + \tau \, d\bar z_k}{\tau - \bar\tau}.$$
The classes $dx_1 \wedge dy_1$ and $dx_2 \wedge dy_2$ are multiples of $dz_k \wedge d\bar z_k$, of type $(1,1)$, and they are the pullbacks of the point classes of the two factors. A class in the Künneth summand $H^1 \otimes H^1$ is
$$\omega = a\, dx_1 \wedge dx_2 + b\, dx_1 \wedge dy_2 + c\, dy_1 \wedge dx_2 + d\, dy_1 \wedge dy_2, \qquad a, b, c, d \in \mathbb{Z},$$
and its coefficient on $dz_1 \wedge dz_2$ is $(\tau - \bar\tau)^{-2} (a \bar\tau^2 - (b + c) \bar\tau + d)$. Since $\omega$ is real, it is of type $(1,1)$ if and only if this vanishes, that is, after conjugation, if and only if
$$a \tau^2 - (b + c) \tau + d = 0.$$
If $\tau$ is not a root of a quadratic polynomial with rational coefficients, this forces $a = d = 0$ and $b = -c$, a group of rank $1$ spanned by $\delta = dx_1 \wedge dy_2 - dy_1 \wedge dx_2$, which is, up to sign, the Künneth component of the class of the diagonal. Then $\rho(X) = 3$. If $\tau$ satisfies a primitive equation $A \tau^2 + B \tau + C = 0$ with $A, B, C \in \mathbb{Z}$ and $A > 0$, the solutions are $(a, -(b+c), d) \in \mathbb{Z}(A, B, C)$, which together with the kernel direction $(0, 1, -1, 0)$ gives a group of rank $2$, and $\rho(X) = 4 = h^{1,1}(X)$. For $\tau = i$ the condition reads $d = a$ and $c = -b$, spanned by $dx_1 \wedge dx_2 + dy_1 \wedge dy_2$ and $dx_1 \wedge dy_2 - dy_1 \wedge dx_2$; the first comes from the graph of multiplication by $i$, as Exercise 5 asks to verify.

**Example P6.5.17 (a torus with Picard number 0).** Let $X = \mathbb{C}^2 / \Lambda$ where $\Lambda$ is spanned by the columns $\lambda_1, \dots, \lambda_4$ of $(I \mid Z)$ with
$$Z = \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} i & \sqrt{2} \\ \sqrt{3} & i\sqrt{5} \end{pmatrix}.$$
Since $\operatorname{Im} Z = \operatorname{diag}(1, \sqrt 5)$ is invertible, the four columns are linearly independent over $\mathbb{R}$, so $\Lambda$ is a lattice. In the real coordinates $x_1, \dots, x_4$ dual to $\lambda_1, \dots, \lambda_4$, the holomorphic coordinates are $z_1 = x_1 + a x_3 + b x_4$ and $z_2 = x_2 + c x_3 + d x_4$, so
$$\sigma = dz_1 \wedge dz_2 = dx_{12} + c\, dx_{13} + d\, dx_{14} - a\, dx_{23} - b\, dx_{24} + (ad - bc)\, dx_{34},$$
with $dx_{jk} = dx_j \wedge dx_k$. An integral class is $E = \sum_{j<k} e_{jk} dx_{jk}$ with $e_{jk} \in \mathbb{Z}$, and with $dx_{1234}$ the volume form,
$$E \wedge \sigma = \big( e_{12}(ad - bc) + e_{13} b - e_{14} a + e_{23} d - e_{24} c + e_{34} \big) dx_{1234}.$$
Here $ad - bc = -\sqrt 5 - \sqrt 6$. The imaginary part of the coefficient is $-e_{14} + \sqrt{5} e_{23}$, which vanishes only if $e_{14} = e_{23} = 0$ because $\sqrt 5$ is irrational. The real part is then $e_{34} + \sqrt{2} e_{13} - \sqrt{3} e_{24} - e_{12} (\sqrt 5 + \sqrt 6)$. If $e_{12} \neq 0$ this would put $\sqrt{5}$ in the field $\mathbb{Q}(\sqrt 2, \sqrt 3)$, whose quadratic subfields are $\mathbb{Q}(\sqrt 2)$, $\mathbb{Q}(\sqrt 3)$ and $\mathbb{Q}(\sqrt 6)$; so $e_{12} = 0$, and then $e_{34} = e_{13} = e_{24} = 0$ since $1, \sqrt 2, \sqrt 3$ are linearly independent over $\mathbb{Q}$. Hence $H^{1,1}(X, \mathbb{Z}) = 0$ and, by Theorem P6.5.13, every holomorphic line bundle on $X$ has $c_1 = 0$: $\operatorname{Pic}(X) = \operatorname{Pic}^0(X)$ and $\rho(X) = 0$. Section 5.3 shows that $X$ carries no positive line bundle, and Chapter 6 deduces that $X$ is not projective.

**Example P6.5.18 (the quadric surface).** Let $X = \mathbb{P}^1 \times \mathbb{P}^1$. By the Künneth formula $b_1 = 0$, $b_2 = 2$ and $H^2(X, \mathbb{Z}) \cong \mathbb{Z}^2$, with basis the pullbacks $f_1 = \mathrm{pr}_1^* [\mathrm{pt}]$ and $f_2 = \mathrm{pr}_2^*[\mathrm{pt}]$. So $h^{0,1} = 0$ by Theorem P6.5.8, part 1. Let $\omega_k = \mathrm{pr}_k^* \omega_{\mathrm{FS}}$; then $\omega_1 + \omega_2$ is a Kähler form, and $\omega_1$, $\omega_2$ are closed $(1,1)$-forms with $\int_{\mathbb{P}^1 \times \{q\}} \omega_1 = 1$, $\int_{\mathbb{P}^1 \times \{q\}} \omega_2 = 0$, and symmetrically, so their classes are linearly independent and $h^{1,1} \geq 2$. Since $h^{2,0} + h^{1,1} + h^{0,2} = b_2 = 2$, $h^{2,0} = h^{0,2} = 0$. Corollary P6.5.15 gives $\operatorname{Pic}(X) \cong H^2(X, \mathbb{Z}) \cong \mathbb{Z}^2$, generated by $\mathcal{O}(1, 0) = \mathrm{pr}_1^* \mathcal{O}(1)$ and $\mathcal{O}(0, 1)$, whose Chern classes are $f_1$ and $f_2$ by Proposition P6.5.6, part 3, and Example P6.5.9. This agrees with the algebraic computation of P7, Chapter 2.

### Proof

*Lemma P6.5.12.* Let $\alpha$ be the real harmonic representative of $a$ for a Kähler metric (Corollary P6.4.15) and $\alpha = \alpha^{2,0} + \alpha^{1,1} + \alpha^{0,2}$ its decomposition by type. The components are harmonic, and since $\alpha$ is real, $\alpha^{2,0} = \overline{\alpha^{0,2}}$. By Lemma P6.5.7, $\iota(a)$ is the Dolbeault class of $\alpha^{0,2}$. A harmonic form whose Dolbeault class is zero vanishes, since harmonic forms map isomorphically onto Dolbeault cohomology (Corollary P6.4.15). So $\iota(a) = 0$ if and only if $\alpha^{0,2} = 0$, if and only if $\alpha^{0,2} = \alpha^{2,0} = 0$, if and only if $\alpha$ has type $(1,1)$. Finally $a \in H^{1,1}(X)$ if and only if its harmonic representative has type $(1,1)$, by uniqueness of the harmonic representative and the fact that the Hodge decomposition is the decomposition of harmonic forms by type.

*Theorem P6.5.13.* By Theorem P6.5.8, part 3, a class $c \in H^2(X, \mathbb{Z})$ is in $\operatorname{NS}(X)$ if and only if it maps to zero in $H^2(X, \mathcal{O}_X)$. The inclusion $\mathbb{Z} \to \mathcal{O}_X$ factors through $\mathbb{Z} \to \mathbb{R} \to \mathbb{C} \to \mathcal{O}_X$, so this image is $\iota(c_\mathbb{R})$ with $c_\mathbb{R} \in H^2(X, \mathbb{R})$ the image of $c$. By Lemma P6.5.12 it vanishes if and only if $c_\mathbb{R}$, equivalently the image of $c$ in $H^2(X, \mathbb{C})$, has type $(1,1)$.

*Corollary P6.5.14.* The image $\overline{H}$ of $H^2(X, \mathbb{Z})$ in $H^2(X, \mathbb{R})$ is a lattice, and $H^2(X, \mathbb{Z}) \to \overline{H}$ has finite kernel, the torsion. The image $\overline{N}$ of $\operatorname{NS}(X)$ is a subgroup of $\overline{H}$, free of rank $\rho(X)$, and a subgroup of a lattice is free on elements that are linearly independent over $\mathbb{R}$. So $\operatorname{NS}(X) \otimes \mathbb{R} = \overline{N} \otimes \mathbb{R}$ maps isomorphically onto the span of $\overline{N}$, which lies in $H^{1,1}(X, \mathbb{R})$ by Theorem P6.5.13. Since $\dim_\mathbb{R} H^{1,1}(X, \mathbb{R}) = h^{1,1}(X)$, as $H^{1,1}(X)$ is stable under conjugation, $\rho(X) \leq h^{1,1}(X)$.

*Corollary P6.5.15.* If $h^{0,2} = 0$ then $H^2(X, \mathcal{O}_X) = 0$ by the Dolbeault isomorphism, so $c_1$ is surjective by the exact sequence of Theorem P6.5.8, part 3, and $\rho = \operatorname{rank} H^2(X, \mathbb{Z}) = b_2$. If also $h^{0,1} = 0$, then $\operatorname{Pic}^0(X) = 0$ and $c_1$ is injective.

### Exercises

1. (A) Let $C$ be a compact Riemann surface. Show directly that $H^{1,1}(C, \mathbb{Z}) = H^2(C, \mathbb{Z})$ and deduce from Theorem P6.5.13 that every integer is the degree of a line bundle. Find such line bundles without the theorem.
2. (A) Show that $\rho(E_\tau \times E_{\tau'}) \geq 2$ for any two elliptic curves, and compute it when $\tau = i$ and $\tau' = i\sqrt 2$, using the method of Example P6.5.16 with two different period lattices.
3. (B) Let $X = \mathbb{P}^n \times \mathbb{P}^m$. Compute $h^{p,q}(X)$ for $p + q \leq 2$ from the Betti numbers as in Example P6.5.18, and show $\operatorname{Pic}(X) \cong \mathbb{Z}^2$.
4. (B) Let $X$ be a compact Kähler manifold and $Y \subseteq X$ a compact complex submanifold of codimension $1$. Show that $c_1(\mathcal{O}_X(Y))$ is nonzero in $H^2(X, \mathbb{R})$ by computing $\int_X c_1(\mathcal{O}_X(Y)) \wedge \omega^{n-1} = \int_Y \omega^{n-1}$, which you may take from the Poincaré-Lelong formula of Chapter 8. Deduce that the torus of Example P6.5.17 contains no compact complex curve.
5. (B) In Example P6.5.16, show that the class of the graph $\Gamma_\phi \subseteq E_\tau \times E_\tau$ of an endomorphism $\phi(z) = \mu z$, $\mu \in \mathbb{Z} + \tau \mathbb{Z}$, is a $(1,1)$-class, and identify its Künneth component in terms of the action of $\mu$ on $H^1(E_\tau, \mathbb{Z})$.
6. (C) Let $X = V/\Lambda$ be a complex torus of dimension $n$. Show that $h^{1,1}(X) = n^2$, that $\rho(X)$ can take the value $n^2$, and that for a very general lattice $\rho(X) = 0$, meaning that $\rho(X) = 0$ outside a countable union of proper real analytic subsets of the space of period matrices. Hint: each nonzero integral alternating form imposes a nontrivial analytic condition.

### Lean

Mathlib has no Hodge decomposition and no sheaf cohomology of complex manifolds, so neither Theorem P6.5.13 nor its corollaries are formalized, and the project library has no node for them.

### Notes and history

Lefschetz proved the theorem for algebraic surfaces in his memoir on numerical invariants (Lef21a), in the form that an integral class on which the periods of all holomorphic $2$-forms vanish is the class of a divisor; Kodaira and Spencer gave the sheaf theoretic proof through the exponential sequence, which is the one given here, following Griffiths and Harris, Chapter 1, Section 2 (GH78), Huybrechts, Section 3.3 (Huy05), and Voisin, Chapter 7 (Voi02). The Hodge conjecture predicts the same statement for rational classes of type $(p,p)$ and algebraic cycles of codimension $p$; it is open. Theorem P6.5.13 is the reason the Picard number $\rho(X)$, defined algebraically as the rank of $N^1(X)$ in P7, Chapter 2, equals the rank of $\operatorname{NS}(X)$ for a smooth projective variety over $\mathbb{C}$, given the comparison of algebraic and analytic line bundles in Chapter 7. The computations on tori follow Mumford, Section 1 (Mum70a), and the Appell-Humbert theorem described there lists all line bundles on a torus.
