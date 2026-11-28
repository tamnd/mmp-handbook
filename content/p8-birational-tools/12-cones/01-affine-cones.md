---
title: The affine cone over a polarized variety
nodes: []
sources: [Kol13, Har77, Laz04, KM98]
reads_with: [Kol13:3.1, Har77:II.5]
requires: [P3.6, P3.8, P3.12, P4.2, P8.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The affine cone over a polarized variety

### Statement

In this chapter $V$ is a smooth projective variety of dimension $n - 1 \geq 1$ over the algebraically closed field $k$, and $L$ is an ample line bundle on $V$. The pair $(V, L)$ is a *polarized variety*.

**Definition P8.12.1 (the cone and its blow-up).** The *section ring* of $(V, L)$ is the graded $k$-algebra
$$R(V, L) = \bigoplus_{m \geq 0} H^0(V, L^m),$$
and the *affine cone* over $(V, L)$ is $X = C(V, L) = \operatorname{Spec} R(V, L)$. The *vertex* $0 \in X$ is the point defined by the maximal ideal $R_+ = \bigoplus_{m > 0} H^0(V, L^m)$. Put
$$Y = \operatorname{Spec}_V \bigoplus_{m \geq 0} L^m, \qquad p \colon Y \to V,$$
the total space of the line bundle $L^{-1}$, with *zero section* $E \subseteq Y$ defined by the ideal $\bigoplus_{m > 0} L^m$, so that $p|_E \colon E \to V$ is an isomorphism. Since $H^0(Y, \mathcal{O}_Y) = H^0(V, p_* \mathcal{O}_Y) = R(V, L)$, there is a natural morphism $f \colon Y \to X$.

**Proposition P8.12.2 (the cone is a normal variety).** In the situation of Definition P8.12.1:

1. $R(V, L)$ is a finitely generated normal domain, and $X$ is a normal affine variety of dimension $n$.
2. $f$ restricts to an isomorphism $Y \setminus E \to X \setminus \{ 0 \}$, and $f^{-1}(0) = E$ as sets.
3. $f$ is proper and birational, and $f_* \mathcal{O}_Y = \mathcal{O}_X$.
4. $X \setminus \{ 0 \}$ is smooth, so $0$ is the only point at which $X$ can be singular.

Lean: not in Lean as stated.

**Proposition P8.12.3 (the exceptional divisor and the canonical class of $Y$).** In the situation of Definition P8.12.1, $Y$ is a smooth variety of dimension $n$, so $f$ is a resolution of $X$ with exceptional divisor $E \cong V$, and

1. $\mathcal{O}_Y(-E) \cong p^* L$, so $\mathcal{O}_Y(E)|_E \cong L^{-1}$ under $E \cong V$;
2. $K_Y \sim p^* K_V - E$.

For $n = 2$, $V$ is a smooth curve and $E^2 = -\deg L$.

Lean: not in Lean as stated.

### Proof in words

The total space of $L^{-1}$ is a smooth variety that maps to the affine cone by its ring of global functions. Away from the zero section it is a $\mathbb{G}_m$-bundle, and over the open set where a section $s$ of a power of $L$ does not vanish, its functions are the localization of the section ring at $s$; this identifies the complement of the zero section with the punctured cone. Normality descends from $Y$ to its ring of global functions. The ideal of the zero section is $L$ times the structure sheaf, which gives $\mathcal{O}_Y(-E) = p^* L$, and the relative cotangent sheaf of $p$ is the same line bundle, which gives the canonical class.

### Examples

**Example P8.12.4 (the cones over rational normal curves).** Let $V = \mathbb{P}^1$ and $L = \mathcal{O}(n)$, $n \geq 1$. Then $R(V, L) = \bigoplus_m k[s, t]_{mn}$ is the ring of polynomials whose monomials have degree divisible by $n$, which is $k[s, t]^{\mu_n}$ for $\mu_n$ acting by $\zeta \cdot (s, t) = (\zeta s, \zeta t)$. So $C(\mathbb{P}^1, \mathcal{O}(n))$ is the cyclic quotient singularity $\frac{1}{n}(1, 1)$ of Example P8.9.25, it is the affine cone over the rational normal curve of degree $n$ in $\mathbb{P}^n$, and by Proposition P8.12.3 its resolution $Y$ has a single exceptional curve $E \cong \mathbb{P}^1$ with $E^2 = -n$. For $n = 1$ the cone is $\mathbb{A}^2$ and $f$ is the blow-up of the origin; for $n = 2$ it is the quadric cone $xz = y^2$, with generators $s^2, st, t^2$.

**Example P8.12.5 (the singularities $\frac{1}{d}(1, \dots, 1)$).** Let $V = \mathbb{P}^{n-1}$ and $L = \mathcal{O}(d)$. As in Example P8.12.4, $R(V, L) = k[x_1, \dots, x_n]^{\mu_d}$ for $\mu_d$ acting by scalars, so $C(\mathbb{P}^{n-1}, \mathcal{O}(d)) = \mathbb{A}^n / \mu_d = \frac{1}{d}(1, \dots, 1)$. For $d = 2$, $n = 3$ this is the singularity $\frac{1}{2}(1, 1, 1)$ of Example P8.9.11, the cone over the Veronese surface.

**Example P8.12.6 (cones over hypersurfaces).** Let $V = V_+(F) \subseteq \mathbb{P}^n$, $n \geq 2$, be a smooth hypersurface of degree $e$ and $L = \mathcal{O}_V(1)$. From $0 \to \mathcal{O}_{\mathbb{P}^n}(m - e) \to \mathcal{O}_{\mathbb{P}^n}(m) \to \mathcal{O}_V(m) \to 0$ and $H^1(\mathbb{P}^n, \mathcal{O}(m - e)) = 0$ (Theorem P4.2.1, since $n \geq 2$), every section of $\mathcal{O}_V(m)$ is the restriction of a form of degree $m$, so $R(V, L) = k[x_0, \dots, x_n]/(F)$ and $X = V(F) \subseteq \mathbb{A}^{n+1}$ is the affine cone in the naive sense. For a smooth plane cubic this is the elliptic cone of Example P4.9.24, and for the quadric $xy - zw$ it is the cone over $\mathbb{P}^1 \times \mathbb{P}^1$ with $L = \mathcal{O}(1, 1)$.

**Example P8.12.7 (the same variety, two polarizations).** For $V = \mathbb{P}^1$ the cones over $\mathcal{O}(1)$ and $\mathcal{O}(2)$ are $\mathbb{A}^2$ and the quadric cone. For a fixed $V$ the singularity depends on $L$, and replacing $L$ by $L^d$ replaces $R(V, L)$ by its Veronese subring $\bigoplus_m R_{dm}$, so that $C(V, L^d) = C(V, L)/\mu_d$, with $\mu_d$ acting on $R_m$ by $\zeta^m$.

### Proof

*Proposition P8.12.2.* By Theorem P3.6.25 there is $m_0$ such that $L^m$ is very ample for every $m \geq m_0$. For $s \in R_m = H^0(V, L^m)$ with $m \geq m_0$, the open set $V_s = \{ s \neq 0 \}$ is the complement of a hyperplane section in a projective embedding, hence affine. Over $V_s$ the bundle $L$ is a line bundle on an affine scheme, and $p^{-1}(V_s) \setminus E = \operatorname{Spec}_{V_s} \bigoplus_{j \in \mathbb{Z}} L^j$, because on $V_s$ the section $s$ trivializes $L^m$, and inverting the generator $s$ of degree $m$ inverts every local generator of $L$. So
$$\mathcal{O}(p^{-1}(V_s) \setminus E) = \bigoplus_{j \in \mathbb{Z}} H^0(V_s, L^j).$$
By Lemma II.5.14 of Hartshorne (Har77), applied to the sheaves $L^j$ and the section $s$, every element of $H^0(V_s, L^j)$ is of the form $u / s^i$ with $u \in H^0(V, L^{j + im})$, and $u / s^i = 0$ if and only if $s^{i'} u = 0$ in $R$ for some $i'$. So the ring above is the localization $R[1/s]$, and $f$ restricts to an isomorphism $p^{-1}(V_s) \setminus E \to D_X(s) = \operatorname{Spec} R[1/s]$.

The function $s$ on $Y$ vanishes on $E$, since $s$ has positive degree, and on $p^{-1}(V \setminus V_s)$; so $p^{-1}(V_s) \setminus E = f^{-1}(D_X(s))$. The sets $V_s$ cover $V$ because $L^m$ is very ample. On $X$, a homogeneous element $u \in R_j$ with $j > 0$ satisfies $D_X(u) = D_X(u^{m_0})$ with $u^{m_0}$ of degree $j m_0 \geq m_0$, so the sets $D_X(s)$ with $\deg s \geq m_0$ cover $X \setminus V(R_+) = X \setminus \{ 0 \}$. This proves that $f^{-1}(X \setminus \{ 0 \}) = Y \setminus E$ and that $f$ is an isomorphism there, which is part 2.

For part 1, $R$ is finitely generated over $k$ because $L$ is ample (Laz04, Section 2.1). It is a domain, being the ring of functions of the integral scheme $Y$. By part 2, $X \setminus \{ 0 \}$ is a nonempty open subset isomorphic to $Y \setminus E$, so $\operatorname{Frac}(R) = k(Y)$ and $\dim X = \dim Y = n$. An element of $k(Y)$ integral over $R$ is integral over every local ring $\mathcal{O}_{Y, y}$, which is normal since $Y$ is smooth, so it lies in every $\mathcal{O}_{Y, y}$ and hence in $H^0(Y, \mathcal{O}_Y) = R$. So $R$ is normal.

For part 3, $f$ is birational by part 2 and $f_* \mathcal{O}_Y = \mathcal{O}_X$ because $X$ is affine with ring $H^0(Y, \mathcal{O}_Y)$. For properness, fix $d \geq m_0$. The image $B \subseteq \bigoplus_m L^m$ of $R \otimes_k \mathcal{O}_V$ contains $\bigoplus_m L^{dm}$, since $L^{dm}$ is generated by its global sections, and $\bigoplus_m L^m$ is a finite module over $\bigoplus_m L^{dm}$, generated by local generators of $L^0, \dots, L^{d-1}$. So $Y \to \operatorname{Spec}_V B$ is finite, $\operatorname{Spec}_V B \to V \times X$ is a closed immersion, and $V \times X \to X$ is proper because $V$ is projective. The composite $f$ is proper. Part 4 follows from part 2 and the smoothness of $Y$ in Proposition P8.12.3.

*Proposition P8.12.3.* Over an open set $U \subseteq V$ on which $L$ has a generator $t$, $p^{-1}(U) = \operatorname{Spec}_U \mathcal{O}_U[t] = U \times \mathbb{A}^1$, which is smooth of dimension $n$; so $Y$ is smooth and $f$ is a resolution with exceptional set $E$, by Proposition P8.12.2. (1) On $p^{-1}(U)$ the ideal $\bigoplus_{m > 0} L^m$ of $E$ is generated by $t$, so it is the invertible sheaf $L \otimes_{\mathcal{O}_V} \bigoplus_{m \geq 0} L^m = p^* L$, and $\mathcal{O}_Y(-E) \cong p^* L$. Restricting to $E \cong V$ gives $\mathcal{O}_Y(-E)|_E \cong L$. (2) Since $p$ is smooth of relative dimension $1$, the sequence $0 \to p^* \Omega_V \to \Omega_Y \to \Omega_{Y/V} \to 0$ is exact, and $\Omega_{Y/V}$ is generated on $p^{-1}(U)$ by $dt$. A change of generator $t' = u t$ with $u \in \mathcal{O}_U^*$ gives $dt' = u \, dt$ modulo $p^* \Omega_U$, so $\Omega_{Y/V} \cong p^* L$, with the same transition functions as $t$. Taking determinants, $\omega_Y \cong p^* \omega_V \otimes p^* L$, so $K_Y \sim p^* K_V + p^* L \sim p^* K_V - E$ by part 1. For $n = 2$, $E^2 = \deg(\mathcal{O}_Y(E)|_E) = -\deg L$.

As a check, Theorem P3.12.30 gives $K_E = (K_Y + E)|_E = (p^* K_V)|_E = K_V$, as it should be.

### Exercises

1. (A) Show that $C(\mathbb{P}^1 \times \mathbb{P}^1, \mathcal{O}(1, 1))$ is $\{ xy = zw \} \subseteq \mathbb{A}^4$, and compare its resolution $Y$ of Proposition P8.12.3 with the two small resolutions of Example P8.8.16.
2. (A) Let $V$ be a smooth plane cubic and $L = \mathcal{O}_V(1)$. Show that $f$ of Definition P8.12.1 is the blow-up of the vertex of $V(F) \subseteq \mathbb{A}^3$, and that $E^2 = -3$.
3. (B) Show that when $R(V, L)$ is generated by $R_1$, the morphism $f$ is the blow-up of $X$ at the vertex, that is, $Y = \operatorname{Proj} \bigoplus_j R_+^j$.
4. (B) Let $V = \mathbb{P}^1$ and $L = \mathcal{O}(3)$. Show that $R(V, L)$ is generated by four elements of degree $1$, that the ideal of relations is generated by three quadrics, and that $X$ is not a complete intersection.
5. (B) Show that $X$ is smooth at the vertex when $(V, L) = (\mathbb{P}^{n-1}, \mathcal{O}(1))$. Conversely, show that if $X$ is smooth at $0$ and $R$ is generated by $R_1$, then $\dim R_1 = n$ and $(V, L) \cong (\mathbb{P}^{n-1}, \mathcal{O}(1))$.
6. (C) The multiplicative group $\mathbb{G}_m$ acts on $X$ through the grading, $\lambda \cdot u = \lambda^m u$ for $u \in R_m$. Show that $V$ is the quotient $(X \setminus \{ 0 \}) / \mathbb{G}_m$, that is, $V = \operatorname{Proj} R(V, L)$, and that $Y \setminus E \to V$ is a principal $\mathbb{G}_m$-bundle.

### Lean

Section rings, affine cones and the total space of a line bundle are not in the repository.

### Notes and history

Cones are the first source of examples in the theory of singularities: every question about the vertex becomes a question about the cohomology of the line bundles $L^m$ on $V$, as in Proposition P4.9.23. The construction here follows Kollár (Kol13), Section 3.1, who works with normal $V$ and with $\mathbb{Q}$-divisors in place of $L$. When $R(V, L)$ is generated in degree $1$, $X$ is the cone over the image of $V$ in $\mathbb{P}(H^0(V, L))$, and $X$ is normal exactly when that embedding is projectively normal. Proposition P8.12.2 avoids this hypothesis by taking the full section ring.
