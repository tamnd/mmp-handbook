---
title: The canonical sheaf and adjunction
nodes: []
sources: [Vak25, Har77, Stacks]
reads_with: [Vak25:ch21, Har77:II.8]
requires: [P1.12, P3.7, P3.8, P3.9, P3.11]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The canonical sheaf and adjunction

### Statement

In this section $k$ is a perfect field and a variety is an integral separated scheme of finite type over $k$. A smooth variety $X$ is regular by part 3 of Theorem P3.7.24, so it is normal (Proposition P3.7.32) and locally factorial (Corollary P3.9.11), and every Weil divisor on it is Cartier. Write $K = k(X)$ for the function field and $d = \dim X$. The $K$-vector space $\Omega^d_{K/k}$ has dimension one: by Theorem P3.12.12 and part 4 of Theorem P3.12.2, $\Omega_{K/k}$ is the stalk of $\Omega_X$ at the generic point, of dimension $d$. Its nonzero elements are the *rational $d$-forms* on $X$.

**Definition P3.12.28 (the canonical sheaf of a smooth variety).** Let $X$ be a smooth variety of dimension $d$. The *canonical sheaf* of $X$ is the invertible sheaf $\omega_X = \Omega^d_X = \bigwedge^d \Omega_X$ of Corollary P3.12.11. For a rational $d$-form $\omega \neq 0$ and a prime divisor $P$ with generic point $\eta_P$, the stalk $\omega_{X, \eta_P}$ is a free module of rank one over the discrete valuation ring $\mathcal{O}_{X, \eta_P}$, with a generator $\omega_P$, and $\omega = g\,\omega_P$ with $g \in K^*$. The *order* of $\omega$ along $P$ is $\operatorname{ord}_P(\omega) = \operatorname{ord}_P(g)$, and the *divisor* of $\omega$ is
$$
\operatorname{div}(\omega) = \sum_P \operatorname{ord}_P(\omega)\, P .
$$
A *canonical divisor* of $X$ is a divisor $K_X = \operatorname{div}(\omega)$ of a nonzero rational $d$-form.

Lean: `MinimalModel.CanonicalDivisor` and `MinimalModel.IsDivOfForm` (definition), for normal varieties; see Proposition P3.12.29.

**Proposition P3.12.29 (the canonical divisor of a normal variety).** Let $X$ be a normal variety of dimension $d$, $j \colon U \to X$ the inclusion of its smooth locus, and $\omega \neq 0$ a rational $d$-form. By Proposition P3.12.13, $X \setminus U$ has codimension at least $2$, so the prime divisors of $X$ and of $U$ correspond by $P \mapsto P \cap U$, and $\operatorname{div}(\omega)$ is defined on $X$ by the orders of $\omega$ along the $P \cap U$. Put $\omega_X = j_* \omega_U$ and $K_X = \operatorname{div}(\omega)$.

1. $\operatorname{ord}_P(\omega)$ is well defined, and $\operatorname{div}(\omega)$ is a Weil divisor.
2. For $g \in K^*$, $\operatorname{div}(g \omega) = \operatorname{div}(g) + \operatorname{div}(\omega)$. So the class of $K_X$ in $\operatorname{Cl}(X)$ does not depend on $\omega$, and two canonical divisors are linearly equivalent.
3. Multiplication by $\omega$ is an isomorphism $\mathcal{O}_X(K_X) \to \omega_X$. So $\omega_X$ is a coherent sheaf, and it is invertible near $x$ if and only if $K_X$ is Cartier at $x$.
4. A rational $d$-form $g\omega$ is a section of $\omega_X$ over an open $V$ if and only if $\operatorname{ord}_P(g \omega) \geq 0$ for every prime divisor $P$ meeting $V$. On an affine open $\operatorname{Spec} A$, $\omega_X$ is the sheaf of the canonical module $\omega_A$ of Definition P1.12.25.
5. If $X$ is smooth, then $\omega_X = \Omega^d_X$, so Definition P3.12.28 is the special case $U = X$.

Lean: `MinimalModel.CanonicalDivisor` (definition): a divisor $K$ with a rational top form $\omega$ such that `MinimalModel.IsDivOfForm K ω`, the condition of part 4 at every prime divisor. The sheaf $\omega_X$ is not in Lean.

**Theorem P3.12.30 (adjunction).** Let $X$ be a smooth variety of dimension $n$ and $Y \subseteq X$ a closed subscheme that is smooth over $k$ of pure dimension $n - 1$, with inclusion $i$. Then $Y$ is an effective Cartier divisor, and there is an isomorphism
$$
\omega_Y \cong i^* \big( \omega_X \otimes \mathcal{O}_X(Y) \big) = (\omega_X \otimes \mathcal{O}_X(Y))|_Y .
$$
If $\mathcal{I}_Y$ is generated near $y$ by $f$, and $\sigma$ is a local section of $\omega_X$ with $\sigma = \tau \wedge df$ for a local section $\tau$ of $\Omega^{n-1}_X$, then the isomorphism sends $\sigma \otimes f^{-1}$ to the restriction $\tau|_Y$, the *residue* of $\sigma / f$ along $Y$. When $Y$ is a prime divisor, the formula is $K_Y = (K_X + Y)|_Y$ in $\operatorname{Pic}(Y)$.

Lean: not in Lean as stated.

**Corollary P3.12.31 (hypersurfaces in projective space).** Let $n \geq 2$ and $Y = V_+(F) \subseteq \mathbb{P}^n_k$ a hypersurface of degree $e \geq 1$ that is smooth over $k$. Then
$$
\omega_Y \cong \mathcal{O}_Y(e - n - 1) .
$$
More generally, if $Y \subseteq X$ is as in Theorem P3.12.30 and $X$ is a smooth closed subvariety of $\mathbb{P}^N_k$ with $\omega_X \cong \mathcal{O}_X(a)$ and $\mathcal{O}_X(Y) \cong \mathcal{O}_X(e)$, then $\omega_Y \cong \mathcal{O}_Y(a + e)$.

Lean: not in Lean as stated.

**Theorem P3.12.32 (the canonical divisor of a blow-up of a point).** Let $X$ be a smooth variety of dimension $2$, $p \in X$ a point with $\kappa(p) = k$, and $\pi \colon \tilde X = \operatorname{Bl}_p X \to X$ the blow-up with exceptional divisor $E$. Then $\tilde X$ is a smooth variety, $E \cong \mathbb{P}^1_k$, and
$$
K_{\tilde X} = \pi^* K_X + E, \qquad \omega_{\tilde X} \cong \pi^* \omega_X \otimes \mathcal{O}_{\tilde X}(E) .
$$
More precisely, if $\omega$ is a rational $2$-form on $X$, then $\operatorname{div}_{\tilde X}(\omega) = \pi^* \operatorname{div}_X(\omega) + E$, where $\omega$ is a rational $2$-form on $\tilde X$ through the isomorphism $k(\tilde X) = k(X)$.

Lean: not in Lean as stated.

### Proof in words

On the smooth part of a variety the top exterior power of the differentials is a line bundle, and a rational top form has a divisor of zeros and poles. A normal variety is smooth away from codimension two, so this divisor is a Weil divisor on all of it, and the sheaf of forms regular in codimension one is the sheaf of this divisor. Adjunction is the determinant of the conormal sequence: the ambient top form is the wedge of the normal direction $df$ and a top form of the divisor, so dividing by $f$ and restricting gives the top form of the divisor. For the blow-up of a point of a surface, in the chart $y = xt$ the form $dx \wedge dy$ becomes $x\, dx \wedge dt$, which vanishes to order one along $E = V(x)$.

### Examples

**Example P3.12.33 (plane curves).** Let $C = V_+(F) \subseteq \mathbb{P}^2_k$ be a smooth curve of degree $e$. By Corollary P3.12.31, $\omega_C \cong \mathcal{O}_C(e - 3)$. For a line, $\omega_C \cong \mathcal{O}_C(-2)$, as in Example P3.12.6. For a conic, $\omega_C \cong \mathcal{O}_C(-1)$, and $\mathcal{O}_{\mathbb{P}^2}(1)|_C$ is $\mathcal{O}_{\mathbb{P}^1}(2)$ under the isomorphism $C \cong \mathbb{P}^1$ given by a parametrization of degree $2$, so again $\omega_C \cong \mathcal{O}_{\mathbb{P}^1}(-2)$. For a cubic, $\omega_C \cong \mathcal{O}_C$, and a nowhere vanishing $1$-form exists: on an affine chart it is the residue form $dx/(2y)$ of Example P1.12.30. For a quartic, $\omega_C \cong \mathcal{O}_C(1)$, so the canonical forms are the restrictions of the linear forms. The degree of $K_C$ is $e(e - 3)$, which by Riemann-Roch (Volume 3) is $2g - 2$ with $g = (e - 1)(e - 2)/2$.

**Example P3.12.34 (surfaces in $\mathbb{P}^3$).** For a smooth surface $S = V_+(F) \subseteq \mathbb{P}^3_k$ of degree $e$, Corollary P3.12.31 gives $\omega_S \cong \mathcal{O}_S(e - 4)$. For $e = 2$ the quadric $S \cong \mathbb{P}^1 \times \mathbb{P}^1$ (Example P3.9.12) has $\omega_S \cong \mathcal{O}_S(-2)$, and $\mathcal{O}_{\mathbb{P}^3}(1)|_S = \mathcal{O}(1, 1)$ by the Segre embedding, so $\omega_S \cong \mathcal{O}(-2, -2)$, in agreement with Example P3.12.26. For $e = 3$, $-K_S$ is a hyperplane section and is ample: a cubic surface is a del Pezzo surface. For $e = 4$, $\omega_S \cong \mathcal{O}_S$: a smooth quartic surface is a K3 surface. For $e \geq 5$, $K_S$ is very ample, and $S$ is a minimal surface of general type.

**Example P3.12.35 (the residue form of a plane curve).** Let $Y = V(f) \subseteq \mathbb{A}^2_k$ be the smooth curve of Example P3.12.19, $\sigma = dx \wedge dy$ and $\omega_X = \mathcal{O}\,\sigma$. Where $f_y$ is a unit, $dx \wedge df = f_y\, dx \wedge dy$, so $\sigma = (dx / f_y) \wedge df$ and the residue of $\sigma/f$ is $dx/f_y$; where $f_x$ is a unit, $dy \wedge df = -f_x\, dx \wedge dy$, and the residue is $-dy/f_x$. These agree on the overlap by Example P3.12.19, and they form the nowhere vanishing generator of $\Omega_Y$ found there. Theorem P3.12.30 says this is how every generator of $\omega_Y$ arises: $\omega_Y \cong (\omega_X \otimes \mathcal{O}(Y))|_Y$ is free on the class of $\sigma/f$.

**Example P3.12.36 (the plane blown up at a point).** Let $\pi \colon \tilde X \to \mathbb{P}^2_k$ be the blow-up of a $k$-point $p$, with exceptional curve $E$, and $H$ a line. By Corollary P3.12.22, $K_{\mathbb{P}^2} = -3H$, so by Theorem P3.12.32
$$
K_{\tilde X} = -3\pi^* H + E ,
$$
the formula stated in the notes of Section 11.3. Under the isomorphism $\tilde X \cong F_1$ of Theorem P3.11.26, $E$ is the negative section $C_0$ and $\pi^* H$ is the class of $C_0 + f$, where $f$ is a fibre, so $K_{F_1} = -2C_0 - 3f$. For the form $\omega = d(x/z) \wedge d(y/z)$, which by Example P1.12.28 has a pole of order $3$ along $V_+(z)$ and no zeros, choose $p = [0:0:1]$: the strict transform $\tilde L$ of the line $L = V_+(z)$ does not meet $E$, and $\operatorname{div}_{\tilde X}(\omega) = -3\tilde L + E$.

**Example P3.12.37 (the quadric cone is crepant).** Let $X = V(xy - z^2) \subseteq \mathbb{A}^3_k$ and $f = xy - z^2$. By Example P1.12.29 the residue form $\omega_0 = dz \wedge dx / f_y = dz \wedge dx / x$ generates $\omega_X$, so $K_X = \operatorname{div}(\omega_0) = 0$, which is Cartier. Let $\pi \colon \tilde X \to X$ be the blow-up of the vertex, the ideal $(x, y, z)$. By Proposition P3.11.2 it is covered by three charts. In the chart of $x$, the relation $x^2 (y/x) = x^2 (z/x)^2$ and the fact that $x$ is a nonzerodivisor give $y/x = (z/x)^2$, so with $w = z/x$ the chart is $\operatorname{Spec} k[x, w]$, a plane, with $y = x w^2$ and $z = x w$. There
$$
dz \wedge dx = (w\, dx + x\, dw) \wedge dx = x\, dw \wedge dx, \qquad \omega_0 = dw \wedge dx .
$$
The chart of $y$ is the same with $x$ and $y$ exchanged. In the chart of $z$, with $a = x/z$ and $b = y/z$, the relation is $ab = 1$, so the chart is $\operatorname{Spec} k[z, a, a^{-1}]$ with $x = za$, $y = z/a$, and $dz \wedge dx = dz \wedge (a\, dz + z\, da) = z\, dz \wedge da$, so $\omega_0 = dz \wedge da / a$. In each chart $\omega_0$ is a generator of $\Omega^2$, so $\tilde X$ is smooth and
$$
K_{\tilde X} = \operatorname{div}_{\tilde X}(\omega_0) = 0 = \pi^* K_X + 0 \cdot E .
$$
The exceptional curve is $V(x) = \operatorname{Spec} k[w]$ in the first chart and $V(z)$ in the third: it is the conic over which $X$ is the cone, a $\mathbb{P}^1_k$. The coefficient $0$ of $E$ is its *discrepancy*, against $1$ for the blow-up of a smooth point in Theorem P3.12.32. By Example P3.11.29, $\tilde X$ is isomorphic to $F_2 \setminus C_+$, with $E$ going to the negative section $C_-$.

### Proof

*Proof of Definition P3.12.28.* The local ring $\mathcal{O}_{X, \eta_P}$ is a normal Noetherian local domain of dimension $1$, hence a discrete valuation ring, and $\omega_X$ is invertible, so its stalk at $\eta_P$ is free of rank one with some generator $\omega_P$. The stalk at the generic point is $\omega_{X, \eta_P} \otimes K = \Omega^d_{K/k}$, so $\omega = g \omega_P$ for a unique $g \in K^*$. Another generator is $u \omega_P$ with $u$ a unit of $\mathcal{O}_{X, \eta_P}$, and $\operatorname{ord}_P(u^{-1} g) = \operatorname{ord}_P(g)$, so the order does not depend on the generator. That only finitely many orders are nonzero is part 1 of Proposition P3.12.29 with $U = X$. $\square$

*Proof of Proposition P3.12.29.* (1) The prime divisors of $U$ are the $P \cap U$: the generic point of a prime divisor $P$ of $X$ has codimension $1$, so it lies in $U$ by Proposition P3.12.13, and $P \cap U$ is a prime divisor of $U$ whose closure is $P$. Conversely the closure of a prime divisor of $U$ is a prime divisor of $X$. So $\operatorname{ord}_P(\omega)$ is the order of Definition P3.12.28 along $P \cap U$. Cover $U$ by finitely many affine opens $V_i$ on which $\omega_U$ is free with generator $\sigma_i$, which exist since $X$ is Noetherian and $\omega_U$ is invertible by Theorem P3.12.12 and Corollary P3.12.11. On $V_i$, $\omega = g_i \sigma_i$ with $g_i \in K^*$, and $\sigma_i$ generates the stalk at $\eta_P$ for every $P$ meeting $V_i$, so $\operatorname{ord}_P(\omega) = \operatorname{ord}_P(g_i)$ for these $P$. Every prime divisor meets $U$, hence some $V_i$, there are finitely many $V_i$, and $\operatorname{div}(g_i)|_{V_i}$ has finitely many nonzero coefficients. So only finitely many $\operatorname{ord}_P(\omega)$ are nonzero.

(2) If $\omega = h \omega_P$ at $P$, then $g\omega = (gh) \omega_P$, and $\operatorname{ord}_P(gh) = \operatorname{ord}_P(g) + \operatorname{ord}_P(h)$. So $\operatorname{div}(g\omega) = \operatorname{div}(g) + \operatorname{div}(\omega)$. Two nonzero rational $d$-forms differ by an element of $K^*$, since $\Omega^d_{K/k}$ has dimension one.

(3) First on $U$. Multiplication by $\omega$ maps the subsheaf $\mathcal{O}_U(K_X|_U) \subseteq \mathcal{K}$ into the constant sheaf $\Omega^d_{K/k}$, and it is injective. On $V_i$ it sends $h$ to $h g_i \sigma_i$. Now $h \in \mathcal{O}_U(K_X|_U)(V)$ for an open $V \subseteq V_i$ if and only if $\operatorname{div}(h) + \operatorname{div}(g_i) \geq 0$ on $V$, that is, $\operatorname{div}(h g_i)|_V \geq 0$, and this holds if and only if $h g_i \in \mathcal{O}_U(0)(V) = \mathcal{O}(V)$, by part 2 of Proposition P3.8.28. This is the condition $h \omega \in \omega_U(V) = \mathcal{O}(V) \sigma_i$. So multiplication by $\omega$ is an isomorphism $\mathcal{O}_U(K_X|_U) \to \omega_U$. Applying $j_*$, $j_* \mathcal{O}_U(K_X|_U) = \mathcal{O}_X(K_X)$ by part 5 of Proposition P3.8.28, since $X \setminus U$ has codimension at least $2$. So $\mathcal{O}_X(K_X) \cong \omega_X$. The sheaf $\mathcal{O}_X(K_X)$ is coherent by part 1 of Proposition P3.8.28, and invertible near $x$ exactly when $K_X$ is locally principal at $x$, by part 6. On the normal variety $X$, locally principal Weil divisors are the Cartier divisors (Theorem P3.9.10 and Proposition P3.9.9).

(4) By (3), $g\omega \in \omega_X(V)$ if and only if $g \in \mathcal{O}_X(K_X)(V)$, that is, $\operatorname{div}(g) + K_X \geq 0$ on $V$, which by (2) is $\operatorname{div}(g\omega) \geq 0$ on $V$. On $V = \operatorname{Spec} A$, a form $\theta \in \Omega^d_{K/k}$ has $\operatorname{ord}_P(\theta) \geq 0$ exactly when $\theta \in (\Omega^d_A)_\mathfrak{p}$ for the prime $\mathfrak{p}$ of $P$, by the definition of the order, since $\mathfrak{p} \in U$ and $(\Omega^d_A)_\mathfrak{p}$ is free of rank one. So $\omega_X(V) = \bigcap_{\operatorname{ht} \mathfrak{p} = 1} (\Omega^d_A)_\mathfrak{p}$, which is $\omega_A$ by part 3 of Proposition P1.12.26, as no height one prime lies outside $U$. Both $\omega_X|_V$ and $\widetilde{\omega_A}$ are quasi-coherent (part 3 and Proposition P1.12.26) with the same sections on every distinguished open $D(h) \subseteq V$, by the same computation for $A_h$, so they are equal.

(5) If $X$ is smooth, then $U = X$ and $j_* \omega_U = \Omega^d_X$. $\square$

*Proof of Theorem P3.12.30.* By part 3 of Theorem P3.12.14, $Y$ is an effective Cartier divisor with $\mathcal{C}_{Y/X} \cong \mathcal{O}_X(-Y)|_Y$, and by part 1 the conormal sequence
$$
0 \longrightarrow \mathcal{O}_X(-Y)|_Y \xrightarrow{\ \delta\ } i^* \Omega_X \longrightarrow \Omega_Y \longrightarrow 0
$$
is an exact sequence of locally free sheaves of ranks $1$, $n$ and $n - 1$. Lemma P3.12.21 gives an isomorphism
$$
\mathcal{O}_X(-Y)|_Y \otimes \bigwedge^{n-1} \Omega_Y \longrightarrow \bigwedge^n i^* \Omega_X = i^* \omega_X ,
$$
since pullback commutes with exterior powers. Tensor with $\mathcal{O}_X(Y)|_Y$. By part 2 of Proposition P3.9.3, $\mathcal{O}_X(Y) \otimes \mathcal{O}_X(-Y) \cong \mathcal{O}_X$, and $i^*$ commutes with tensor products, so $\mathcal{O}_X(Y)|_Y \otimes \mathcal{O}_X(-Y)|_Y \cong \mathcal{O}_Y$. This gives $\omega_Y \cong i^* \omega_X \otimes \mathcal{O}_X(Y)|_Y$.

For the explicit form, work near $y$ where $\mathcal{I}_Y = (f)$ and $\mathcal{O}_X(Y) = \mathcal{O}_X f^{-1}$ (part 1 of Proposition P3.9.3). The conormal sheaf is generated by the class $\bar f$ of $f$, with $\delta(\bar f) = df|_Y$, and $\bar f$ corresponds to $f \in \mathcal{O}_X(-Y)$. The map of Lemma P3.12.21, written with the factors in the order of the statement, sends $\bar f \otimes \tau|_Y$ to $df|_Y \wedge \tau|_Y = (-1)^{n-1} (\tau \wedge df)|_Y$. Composing with the identification above and absorbing the sign $(-1)^{n-1}$ into the isomorphism, $(\tau \wedge df) \otimes f^{-1}$ maps to $\tau|_Y$. This is well defined: if $\tau \wedge df = \tau' \wedge df$ near $y$, then $(\tau - \tau') \wedge df = 0$, so $(\tau - \tau')|_Y \wedge df|_Y = 0$ in $\bigwedge^n i^* \Omega_X$, and since $df|_Y$ is part of a local basis of $i^* \Omega_X$ by the local splitting of part 1 of Theorem P3.12.14, the image of $(\tau - \tau')|_Y$ in $\Omega^{n-1}_Y$ is zero. The last statement is the translation through part 3 of Proposition P3.12.29 and Theorem P3.9.4: the sheaf $\omega_X \otimes \mathcal{O}_X(Y)$ is $\mathcal{O}_X(K_X + Y)$, and its restriction to $Y$ is the class $(K_X + Y)|_Y$ in $\operatorname{Pic}(Y)$. $\square$

*Proof of Corollary P3.12.31.* By Corollary P3.12.22, $\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$. The ideal sheaf of $Y$ is generated by $F$, so $\mathcal{O}(-Y) \cong \mathcal{O}(-e)$ by Example P3.9.5, and $\mathcal{O}(Y) \cong \mathcal{O}(e)$. The hypersurface $Y$ is a smooth closed subscheme of pure dimension $n - 1$, so Theorem P3.12.30 applies; its proof does not use that $Y$ is irreducible. So $\omega_Y \cong (\mathcal{O}(-n-1) \otimes \mathcal{O}(e))|_Y = \mathcal{O}_Y(e - n - 1)$ by part 4 of Proposition P3.6.11. The general statement is the same computation. $\square$

*Proof of Theorem P3.12.32.* The statement is local on $X$ near $p$, since $\pi$ is an isomorphism over $X \setminus \{p\}$ by Theorem P3.11.3, and outside $E$ the two divisors $\operatorname{div}_{\tilde X}(\omega)$ and $\pi^* \operatorname{div}_X(\omega)$ agree. The scheme $\{p\} = \operatorname{Spec} k$ is smooth of dimension $0$, so by part 2 of Theorem P3.12.14 there is an affine open neighbourhood $W = \operatorname{Spec} B$ of $p$ on which the ideal of $p$ is generated by $x, y \in B$ with $dx, dy$ linearly independent in $\Omega_X(p)$. Then $B/(x, y) = \kappa(p) = k$. Shrinking $W$, by Nakayama (Proposition P3.5.25) $dx, dy$ form a basis of $\Omega_W$, which is locally free of rank $2$, so $\sigma = dx \wedge dy$ generates $\omega_W$. By part 2 of Theorem P3.12.14 again, applied to $V(x)$, which is smooth of dimension $1$ at $p$ by Theorem P3.12.9 since $dx \neq 0$ in $\Omega_X(p)$, we may shrink $W$ so that $B/(x)$ is smooth over $k$, hence reduced (Lemma P3.12.10), with only one irreducible component, the one through $p$: the local ring of $B/(x)$ at $p$ is regular of dimension $1$, a domain, so only one component passes through $p$, and the others can be removed. So $B/(x)$ is a domain, and $y \notin (x)$ since $B/(x, y) = k$ has dimension $0$. So $x, y$ is a regular sequence in $B$.

Let $C = B[t]/(xt - y)$. It has no $x$-torsion: if $x g = (xt - y) h$ in $B[t]$, then reducing modulo $x$ gives $-y h \equiv 0$ in $(B/(x))[t]$, so $h = x h'$ as $y$ is a nonzerodivisor on $B/(x)$, and then $g = (xt - y) h'$ since $B[t]$ is a domain. So $C \to C_x = B_x[t]/(xt - y) \cong B_x$ is injective, with image $B[y/x]$. By Proposition P3.11.2 the chart $D_+(xs)$ of $\pi^{-1}(W) = \operatorname{Bl}_{(x, y)} W$ is $\operatorname{Spec} B[y/x] \cong \operatorname{Spec} C$, with $t = y/x$. By the second exact sequence (Theorem P3.12.4) for $B[t] \to C$, $\Omega_C$ is generated by $dx, dy, dt$ with the single relation $d(xt - y) = t\, dx + x\, dt - dy = 0$. So $dy = t\, dx + x\, dt$, and $\Omega_C$ is free on $dx$ and $dt$, because $\Omega_{B[t]} = (\Omega_B \otimes B[t]) \oplus B[t]\, dt$ is free on $dx, dy, dt$. The chart is integral of dimension $2$, being birational to $W$, so it is smooth by Corollary P3.12.11, and $\omega$ on it is generated by $dx \wedge dt$. The other chart is the same with $x$ and $y$ exchanged. So $\tilde X$ is smooth, and it is a variety by Theorem P3.11.3.

On the chart, the exceptional divisor is $V(\mathcal{I}_p \mathcal{O}) = V(x, xt) = V(x)$, and $C/xC = (B/(x, y))[t] = k[t]$. So $E$ is covered by two copies of $\mathbb{A}^1_k$, with coordinates $t = y/x$ and $x/y$, glued along $t \mapsto 1/t$ as the projective line: $E \cong \mathbb{P}^1_k$, and $E$ is a prime divisor with $\operatorname{ord}_E(x) = 1$, since $x$ generates the ideal of the prime divisor $E$ in the chart. Now
$$
\pi^* \sigma = dx \wedge (t\, dx + x\, dt) = x\, dx \wedge dt .
$$
Write $\omega = g \sigma$ on $W$ with $g \in K^*$. Then $\operatorname{div}_X(\omega)|_W = \operatorname{div}(g)|_W$, and $\pi^*(\operatorname{div}_X \omega)$ is $\operatorname{div}(\pi^* g)$ on $\pi^{-1}(W)$ by Definition P3.9.26 and part 3 of Proposition P3.9.27, which apply because $\pi$ is birational, so the generic point of $\tilde X$ maps to the generic point of $X$, outside every support. On the chart, $\omega = g x \, dx \wedge dt$ with $dx \wedge dt$ a generator, so $\operatorname{div}_{\tilde X}(\omega) = \operatorname{div}(g) + \operatorname{div}(x) = \pi^* \operatorname{div}_X(\omega) + E$ there, as $\operatorname{div}(x) = E$ on the chart. By symmetry the same holds on the other chart, and outside $\pi^{-1}(W)$ there is nothing to prove. So $K_{\tilde X} = \pi^* K_X + E$. Taking sheaves, part 3 of Proposition P3.12.29 and part 2 of Proposition P3.9.3 give $\omega_{\tilde X} \cong \mathcal{O}(\pi^* K_X + E) \cong \pi^* \mathcal{O}_X(K_X) \otimes \mathcal{O}(E) \cong \pi^* \omega_X \otimes \mathcal{O}(E)$, where $\mathcal{O}(\pi^* D) \cong \pi^* \mathcal{O}(D)$ because both are given on $\pi^{-1}(U_i)$ by the inverses of the pulled back local equations. $\square$

### Exercises

1. (A) Use Theorem P3.12.30 to compute $\omega_C$ for the conic $C = V_+(xz - y^2) \subseteq \mathbb{P}^2_k$, and check the result against the parametrization $[s^2 : st : t^2]$ and Example P3.12.6.
2. (A) Let $X = V(xy - z^n) \subseteq \mathbb{A}^3_k$ with $n \geq 1$. Show that the residue form $dz \wedge dx / x$ generates $\omega_X$, so $K_X = 0$, although $X$ is not factorial for $n \geq 2$ (Example P3.9.14).
3. (B) Let $Y = V_+(F_1, \dots, F_c) \subseteq \mathbb{P}^n_k$ be a smooth complete intersection: each $Y_i = V_+(F_1, \dots, F_i)$ is smooth of pure dimension $n - i$, with $\deg F_i = e_i$. Show that $\omega_Y \cong \mathcal{O}_Y(e_1 + \dots + e_c - n - 1)$. Which smooth complete intersections of two quadrics have trivial canonical sheaf?
4. (B) Let $X$ be a smooth variety of dimension $n$ and $p$ a $k$-point. Show that $\operatorname{Bl}_p X$ is smooth and $K_{\operatorname{Bl}_p X} = \pi^* K_X + (n - 1) E$. Hint: in the chart of $x_1$, $x_i = x_1 t_i$ for $i \geq 2$, and $dx_1 \wedge \dots \wedge dx_n = x_1^{n-1}\, dx_1 \wedge dt_2 \wedge \dots \wedge dt_n$.
5. (B) More generally, let $Z \subseteq X$ be a smooth closed subvariety of codimension $r \geq 2$. Show that $K_{\operatorname{Bl}_Z X} = \pi^* K_X + (r - 1) E$, using part 2 of Theorem P3.12.14 and Theorem P3.11.4 for the local model.
6. (C) Let $F \in k[x, y, z]$ be homogeneous of degree $e \geq 1$, with $V_+(F) \subseteq \mathbb{P}^2_k$ smooth, and $X = V(F) \subseteq \mathbb{A}^3_k$ the affine cone. Show that $X$ is normal with $K_X = 0$, that the blow-up $\pi \colon \tilde X \to X$ of the vertex is smooth with $E \cong V_+(F)$, and that $K_{\tilde X} = \pi^* K_X + (2 - e) E$. Hint: in the chart $x = zu$, $y = zv$, the form $dy \wedge dz / F_x$ is $z^{2 - e}\, dv \wedge dz / g_u$ with $g(u, v) = F(u, v, 1)$. For $e = 1, 2, 3$ the discrepancy $2 - e$ is $1$, $0$ and $-1$.

### Lean

In mmp-lean the rational top forms are `MinimalModel.TopForm X`, the top exterior power of `KaehlerDifferential k (FF X)` over the function field, of dimension one as in the statement. The regularity of a form at a prime divisor $P$ is membership in `MinimalModel.formLattice` of the image of the stalk at the generic point of $P$, the lattice of forms $g\,da_1 \wedge \dots \wedge da_d$ with $g$ and the $a_i$ regular there; at the smooth points of Proposition P3.12.13 this is $\mathcal{O}_{X, \eta_P}\, \omega_P$. `MinimalModel.IsDivOfForm D ω` says that $g\omega$ is regular at $P$ exactly when $\operatorname{ord}_P(g) \geq -D(P)$, which is part 4 of Proposition P3.12.29, and a `MinimalModel.CanonicalDivisor` is a divisor with such a form. So the Lean definition is the definition through codimension one points, and it needs neither the sheaf $\omega_X$ nor Proposition P3.12.13. The log canonical divisor of a pair is `MinimalModel.Pair.KΔ`, the canonical divisor plus the boundary. Adjunction and Theorem P3.12.32 are not in Lean; the toric fidelity checks of `MinimalModel/Fidelity/ToricCone.lean` take the canonical divisor of a toric surface to be minus the sum of its torus invariant prime divisors, which is the divisor of the form $\frac{dx}{x} \wedge \frac{dy}{y}$. The handbook adds no `MinimalModel` node here.

### Notes and history

The canonical sheaf of a smooth variety and the adjunction formula are Hartshorne, Section II.8 (Proposition II.8.20 and Example II.8.20.3 for hypersurfaces), and Vakil, Chapter 21. The canonical sheaf of a normal variety through the smooth locus is standard in the minimal model program; see Kollár, *Singularities of the minimal model program*, Chapter 1. The formula for the blow-up of a point of a surface is Hartshorne, Proposition V.3.3, and its version for smooth centres of any codimension is Exercise 5. The literature state is theorem.

The coefficient of an exceptional divisor in $K_{\tilde X} - \pi^* K_X$ is its discrepancy, defined in Volume 4 for every pair $(X, \Delta)$ with $K_X + \Delta$ $\mathbb{R}$-Cartier. The examples of this section are the three basic cases: the blow-up of a smooth point has discrepancy $1$, so smooth surfaces are terminal; the quadric cone has discrepancy $0$, so it is canonical and not terminal, and its blow-up is crepant; the cone over a smooth plane cubic has discrepancy $-1$, so it is log canonical and not klt. Adjunction is the formula on which the induction on dimension in the minimal model program rests: inversion of adjunction (Volume 4) compares the singularities of $(X, S + B)$ near a divisor $S$ with those of $(S, B|_S)$.
