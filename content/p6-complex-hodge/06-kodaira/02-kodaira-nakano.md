---
title: The Kodaira-Akizuki-Nakano vanishing theorem
nodes: []
sources: [Huy05, GH78, Voi02a, Dem97a, Kod53, AN54a, Ser55a]
reads_with: [Huy05:4.1, Huy05:5.2, GH78:1.2, Voi02a:5, Dem97a:VII]
requires: [P2.7, P6.2, P6.3, P6.4, P6.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Kodaira-Akizuki-Nakano vanishing theorem

### Statement

Let $X$ be a compact complex manifold of dimension $n$ with a Hermitian metric $\omega$ and $(E, h)$ a Hermitian holomorphic vector bundle, with the operators of Definition P6.6.1. A form $u \in A^{p,q}(X, E)$ is *harmonic* if $\Delta'' u = 0$, and $\mathcal{H}^{p,q}(X, E)$ denotes the space of harmonic forms. The Dolbeault cohomology $H^{p,q}(X, E)$ of Chapter 2 is the cohomology of $(A^{p,\bullet}(X, E), \bar\partial_E)$, and the Dolbeault isomorphism of Chapter 2 identifies it with the sheaf cohomology $H^q(X, \Omega^p_X \otimes E)$.

**Theorem P6.6.10 (Hodge theory with coefficients, cited).** Let $X$ be compact. Then:

1. $\mathcal{H}^{p,q}(X, E)$ is finite-dimensional, and a form $u$ is harmonic if and only if $\bar\partial_E u = 0$ and $\bar\partial_E^* u = 0$;
2. there is an orthogonal decomposition $A^{p,q}(X, E) = \mathcal{H}^{p,q}(X, E) \oplus \bar\partial_E A^{p,q-1}(X, E) \oplus \bar\partial_E^* A^{p,q+1}(X, E)$;
3. every class in $H^{p,q}(X, E) \cong H^q(X, \Omega^p_X \otimes E)$ has exactly one harmonic representative, so $\mathcal{H}^{p,q}(X, E) \cong H^q(X, \Omega^p_X \otimes E)$.

Lean: not in Lean as stated.

The Hodge theorem for the trivial bundle is the black box of Chapter 4; the proof for bundle-valued forms is the same, since $\Delta''$ is again an elliptic operator of second order with the principal symbol of the flat Laplacian.

**Theorem P6.6.11 (Serre duality).** Let $X$ be compact and $E$ a holomorphic vector bundle. For all $p, q$ the pairing
$$H^{p,q}(X, E) \times H^{n-p, n-q}(X, E^*) \to \mathbb{C}, \qquad ([\alpha], [\beta]) \mapsto \int_X \alpha \wedge \beta,$$
where $\alpha \wedge \beta$ contracts $E \otimes E^* \to \mathbb{C}$, is well defined and perfect. In particular $H^q(X, \Omega^p_X \otimes E) \cong H^{n-q}(X, \Omega^{n-p}_X \otimes E^*)^*$ and $H^q(X, E) \cong H^{n-q}(X, K_X \otimes E^*)^*$.

Lean: not in Lean as stated.

**Theorem P6.6.12 (Kodaira-Akizuki-Nakano vanishing).** Let $X$ be a compact complex manifold of dimension $n$ and $L$ a positive holomorphic line bundle on $X$. Then
$$H^q(X, \Omega^p_X \otimes L) = 0 \qquad \text{for } p + q > n.$$

Lean: not in Lean as stated.

**Corollary P6.6.13 (Kodaira vanishing).** Let $X$ be a compact complex manifold of dimension $n$ and $L$ a positive holomorphic line bundle. Then
$$H^q(X, K_X \otimes L) = 0 \quad \text{for } q > 0, \qquad H^q(X, L^{-1}) = 0 \quad \text{for } q < n.$$

Lean: not in Lean as stated.

**Corollary P6.6.14 (vanishing for negative line bundles).** Let $X$ be a compact complex manifold of dimension $n$ and $L$ a positive holomorphic line bundle. Then $H^q(X, \Omega^p_X \otimes L^{-1}) = 0$ for $p + q < n$.

Lean: not in Lean as stated.

### Proof in words

Hodge theory represents each Dolbeault class by a harmonic form, and the harmonic forms for $E$ and for $E^*$ in complementary degrees are exchanged by a conjugate-linear Hodge star twisted by the metric. Pairing a harmonic form with its own star gives its squared norm, which proves Serre duality.

For the vanishing theorem, a positive line bundle $L$ has a metric whose curvature form $\omega = i\Theta(L)$ is a Kähler form, and this is the Kähler metric to use. With this choice the curvature term $[i\Theta(L), \Lambda]$ of the Bochner-Kodaira-Nakano identity is $[L, \Lambda]$, which acts on $(p,q)$-forms as multiplication by $p + q - n$. For a harmonic form the left side of the identity vanishes, while the right side is the sum of a nonnegative term and $(p + q - n) \|u\|^2$. So the form is zero when $p + q > n$. The case $p = n$ is Kodaira's theorem, and Serre duality turns it into the vanishing for $L^{-1}$ below the middle degree.

### Examples

**Example P6.6.15 (projective space).** On $\mathbb{P}^n$, $K_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$ (Chapter 2) and $\mathcal{O}(1)$ is positive (Proposition P6.5.20). For $k \geq -n$, write $\mathcal{O}(k) = K_{\mathbb{P}^n} \otimes \mathcal{O}(k + n + 1)$ with $k + n + 1 > 0$; Corollary P6.6.13 gives $H^q(\mathbb{P}^n, \mathcal{O}(k)) = 0$ for $q > 0$. For $k < 0$ the second statement of Corollary P6.6.13 with $L = \mathcal{O}(-k)$ gives $H^q(\mathbb{P}^n, \mathcal{O}(k)) = 0$ for $q < n$. So $H^q(\mathbb{P}^n, \mathcal{O}(k)) = 0$ for $0 < q < n$ and every $k$, and $H^n(\mathbb{P}^n, \mathcal{O}(k)) = 0$ for $k \geq -n$. For $n = 1$ this says $H^1(\mathbb{P}^1, \mathcal{O}(k)) = 0$ for $k \geq -1$, in agreement with $h^1(\mathcal{O}(k)) = -k - 1$ for $k \leq -1$ from Chapter 2. The bound $k \geq -n$ is sharp: by Theorem P6.6.11, $H^n(\mathbb{P}^n, \mathcal{O}(-n-1)) = H^n(\mathbb{P}^n, K_{\mathbb{P}^n}) \cong H^0(\mathbb{P}^n, \mathcal{O})^* \cong \mathbb{C}$. Theorem P6.6.12 also gives $H^q(\mathbb{P}^n, \Omega^p(k)) = 0$ for $k > 0$ and $p + q > n$.

**Example P6.6.16 (the bound $p + q > n$ is sharp).** On $\mathbb{P}^n$ take $p = n$, $q = 0$ and $L = \mathcal{O}(k)$ with $k \geq n + 1$. Then $H^0(\mathbb{P}^n, \Omega^n \otimes \mathcal{O}(k)) = H^0(\mathbb{P}^n, \mathcal{O}(k - n - 1))$ is the space of homogeneous polynomials of degree $k - n - 1 \geq 0$ (Chapter 2), which is nonzero, although $L$ is positive and $p + q = n$. With $q > 0$: on a compact Riemann surface $X$ of genus $2$ and $L = \mathcal{O}_X(x)$, Example P6.6.9 showed $H^1(X, L) \neq 0$; here $p = 0$, $q = 1$ and $p + q = 1 = n$. So the condition $p + q > n$ cannot be replaced by $p + q \geq n$, either with $q = 0$ or with $q > 0$.

**Example P6.6.17 (semipositive is not enough).** The trivial bundle $\mathcal{O}_X$ with the constant metric has $i\Theta = 0$, which is semipositive. On any compact $X$, Theorem P6.6.11 gives $H^n(X, \Omega^n_X) = H^n(X, K_X) \cong H^0(X, \mathcal{O}_X)^* \cong \mathbb{C}$, although $p + q = 2n > n$. A less degenerate example: let $X = \mathbb{P}^1 \times \mathbb{P}^1$ with projections $\mathrm{pr}_1, \mathrm{pr}_2$, and $L = \mathrm{pr}_1^* \mathcal{O}(2)$ with the pulled back metric $\mathrm{pr}_1^* h_{\mathrm{FS}}^2$. Its curvature form $\frac{i}{2\pi}\Theta = 2\, \mathrm{pr}_1^* \omega_{\mathrm{FS}}$ is semipositive, and it vanishes on the vertical tangent vectors, so it is not positive. Let $c \in H^1(\mathbb{P}^1, \mathcal{O}(-2))$ be nonzero; this group is $\mathbb{C}$ by Chapter 2. For $y \in \mathbb{P}^1$ let $\iota_y \colon \mathbb{P}^1 \to X$, $t \mapsto (t, y)$. Then $\mathrm{pr}_1 \circ \iota_y = \mathrm{id}$, so $\iota_y^* \mathrm{pr}_1^* c = c \neq 0$ in Dolbeault cohomology, and $\mathrm{pr}_1^* c$ is a nonzero class in $H^1(X, L^{-1})$. Since $1 < n = 2$, the second statement of Corollary P6.6.13 fails for $L$, and by Theorem P6.6.11 so does the first: $H^1(X, K_X \otimes L) \cong H^1(X, L^{-1})^* \neq 0$.

### Proof

*Theorem P6.6.10.* This is the Hodge theorem for the elliptic operator $\Delta''$ acting on sections of the Hermitian bundle $\Lambda^{p,q} T^*X \otimes E$ over a compact manifold: Huybrechts, Section 4.1 and Appendix A (Huy05), Voisin, Chapter 5 (Voi02a), Griffiths and Harris, Chapter 0, Section 6 (GH78), or Demailly, Chapter VI (Dem97a). These references prove finiteness of $\mathcal{H}^{p,q}(X, E)$ and the orthogonal decomposition 2. The remaining statements follow from 2 by the following argument. For any $u$, $\langle\langle \Delta'' u, u \rangle\rangle = \|\bar\partial_E u\|^2 + \|\bar\partial_E^* u\|^2$, so $\Delta'' u = 0$ if and only if $\bar\partial_E u = 0 = \bar\partial_E^* u$, which is part 1. If $\bar\partial_E u = 0$, then $u$ is orthogonal to $\bar\partial_E^* A^{p,q+1}$, because $\langle\langle u, \bar\partial_E^* v \rangle\rangle = \langle\langle \bar\partial_E u, v \rangle\rangle = 0$. So by 2 the $\bar\partial_E$-closed forms are $\mathcal{H}^{p,q} \oplus \bar\partial_E A^{p,q-1}$, and $\mathcal{H}^{p,q} \to H^{p,q}(X, E)$ is an isomorphism. The identification with sheaf cohomology is the Dolbeault isomorphism of Chapter 2.

*Theorem P6.6.11.* Fix a Hermitian metric $h$ on $E$ and a Hermitian metric on $X$. Let $\star$ be the complex-linear Hodge star of Chapter 4, characterized by $\alpha \wedge \star \bar\beta = \langle \alpha, \beta \rangle \, dV$ for forms of the same type, mapping $(p,q)$-forms to $(n-q, n-p)$-forms, with $\star\star = (-1)^k$ on forms of degree $k$. Define the conjugate-linear map
$$\bar\star_E \colon \Lambda^{p,q} T^*_x X \otimes E_x \to \Lambda^{n-p,n-q} T^*_x X \otimes E^*_x, \qquad \bar\star_E(\alpha \otimes e) = \star\bar\alpha \otimes h(\cdot, e),$$
where $h(\cdot, e) \in E^*_x$ is the functional $v \mapsto h(v, e)$. In an orthonormal frame $e_\lambda$ with dual frame $e^\lambda = h(\cdot, e_\lambda)$, $\bar\star_E (\sum_\lambda \alpha_\lambda \otimes e_\lambda) = \sum_\lambda \star \bar\alpha_\lambda \otimes e^\lambda$. It follows that $\bar\star_E$ is bijective, that $u \wedge \bar\star_E v = \langle u, v \rangle \, dV$, and, using the dual metric on $E^*$ for which $e^\lambda$ is orthonormal with $\bar\star_{E^*}(\beta \otimes e^\lambda) = \star\bar\beta \otimes e_\lambda$, that $\bar\star_{E^*} \bar\star_E = \star\star = (-1)^{p+q}$ on $\Lambda^{p,q} \otimes E$.

The pairing is well defined. If $\alpha \in A^{p,q}(X, E)$ and $\beta \in A^{n-p,n-q}(X, E^*)$ are $\bar\partial$-closed and $\gamma \in A^{p,q-1}(X, E)$, then $\gamma \wedge \beta$ is a scalar form of type $(n, n-1)$, so $d(\gamma\wedge\beta) = \bar\partial(\gamma \wedge \beta) = \bar\partial_E \gamma \wedge \beta \pm \gamma \wedge \bar\partial_{E^*} \beta$, by the Leibniz rule for the contraction, which holds because the contraction of holomorphic sections of $E$ and $E^*$ is holomorphic. By Stokes, $\int_X \bar\partial_E \gamma \wedge \beta = 0$. The same holds with the roles exchanged.

Next, $\bar\star$ maps harmonic forms to harmonic forms. For $\alpha \in A^{p,q-1}(X, E)$ and $\beta \in A^{p,q}(X, E)$, Stokes and the Leibniz rule $\bar\partial(\alpha \wedge \eta) = \bar\partial_E \alpha \wedge \eta + (-1)^{p+q-1} \alpha \wedge \bar\partial_{E^*} \eta$ for $\eta = \bar\star_E \beta$ give
$$\langle\langle \bar\partial_E \alpha, \beta \rangle\rangle = \int_X \bar\partial_E \alpha \wedge \bar\star_E \beta = (-1)^{p+q} \int_X \alpha \wedge \bar\partial_{E^*} \bar\star_E \beta.$$
Write $\bar\partial_{E^*} \bar\star_E \beta = \bar\star_E \gamma$ with $\gamma \in A^{p,q-1}(X, E)$. The right side is $(-1)^{p+q} \langle\langle \alpha, \gamma \rangle\rangle$, so $\bar\partial_E^* \beta = (-1)^{p+q} \gamma$, that is,
$$\bar\star_E \, \bar\partial_E^* = (-1)^{p+q} \, \bar\partial_{E^*} \, \bar\star_E \quad \text{on } A^{p,q}(X, E).$$
The same holds for $E^*$ in place of $E$, since $E^{**} = E$. Let $\beta \in \mathcal{H}^{p,q}(X, E)$. Then $\bar\partial_{E^*} \bar\star_E \beta = \pm \bar\star_E \bar\partial_E^* \beta = 0$, and $\bar\star_{E^*} \bar\partial^*_{E^*} (\bar\star_E \beta) = \pm \bar\partial_E \bar\star_{E^*} \bar\star_E \beta = \pm \bar\partial_E \beta = 0$, so $\bar\partial_{E^*}^* \bar\star_E \beta = 0$ because $\bar\star_{E^*}$ is injective. By part 1 of Theorem P6.6.10, $\bar\star_E \beta \in \mathcal{H}^{n-p,n-q}(X, E^*)$.

Finally, for a nonzero $\beta \in \mathcal{H}^{p,q}(X, E)$, $\int_X \beta \wedge \bar\star_E \beta = \|\beta\|^2 > 0$. By part 3 of Theorem P6.6.10 the map $H^{p,q}(X, E) \to H^{n-p,n-q}(X, E^*)^*$ induced by the pairing is injective. By the same argument for $E^*$ the map in the other direction is injective too. Both spaces are finite-dimensional, so the dimensions agree and both maps are isomorphisms. The last two statements are the Dolbeault isomorphism together with $\Omega^n_X = K_X$.

*Theorem P6.6.12.* Let $h$ be a metric on $L$ with $i\Theta(L) > 0$. Locally $\Theta(L) = -\partial\bar\partial \log |e|^2_h$ (Chapter 3), so $\omega := i\Theta(L)$ is a closed real positive $(1,1)$-form, a Kähler form. Give $X$ the Kähler metric with fundamental form $\omega$. At every point all eigenvalues of $i\Theta(L)$ with respect to $\omega$ equal $1$, so Proposition P6.6.5 gives $[i\Theta(L), \Lambda] = (p + q - n) \operatorname{id}$ on $A^{p,q}(X, L)$. Let $c \in H^q(X, \Omega^p_X \otimes L)$ with $p + q > n$, and let $u$ be its harmonic representative (Theorem P6.6.10). By Theorem P6.6.4,
$$0 = \langle\langle \Delta'' u, u \rangle\rangle = \|D' u\|^2 + \|D'^* u\|^2 + (p + q - n) \|u\|^2 \geq (p + q - n) \|u\|^2.$$
Since $p + q - n > 0$, $u = 0$ and $c = 0$.

*Corollary P6.6.13.* The first statement is Theorem P6.6.12 with $p = n$, since $\Omega^n_X = K_X$. For the second, Theorem P6.6.11 gives $H^q(X, L^{-1}) \cong H^{n-q}(X, K_X \otimes L)^*$, which vanishes for $n - q > 0$ by the first statement.

*Corollary P6.6.14.* By Theorem P6.6.11, $H^q(X, \Omega^p_X \otimes L^{-1}) \cong H^{n-q}(X, \Omega^{n-p}_X \otimes L)^*$. Since $(n - p) + (n - q) > n$ exactly when $p + q < n$, Theorem P6.6.12 gives the vanishing.

### Exercises

1. (A) Using Corollary P6.6.13, show that for $n \geq 2$, $H^q(\mathbb{P}^n, \mathcal{O}(k)) = 0$ for $0 < q < n$ and all $k$, and compute $h^n(\mathbb{P}^n, \mathcal{O}(k))$ for $k \leq -n-1$ with Theorem P6.6.11.
2. (A) Let $X$ be a compact Riemann surface of genus $g$ and $L$ a line bundle of degree $d > 2g - 2$. Show that $H^1(X, L) = 0$. Hint: $\deg K_X = 2g - 2$, and $L \otimes K_X^{-1}$ is positive by Example P6.5.25.
3. (B) Let $X \subseteq \mathbb{P}^{n+1}$ be a smooth hypersurface of degree $d$, with $K_X \cong \mathcal{O}_X(d - n - 2)$ by adjunction (Chapter 2). Show that $H^q(X, \mathcal{O}_X(m)) = 0$ for $q > 0$ and $m > d - n - 2$, and for $q < n$ and $m < 0$.
4. (B) Prove Corollary P6.6.14 directly from Theorem P6.6.4 without Serre duality: give $X$ the Kähler metric $\omega = i\Theta(L)$, compute $[i\Theta(L^{-1}), \Lambda]$ on $(p,q)$-forms, and show that harmonic $L^{-1}$-valued $(p,q)$-forms vanish for $p + q < n$.
5. (B) Let $L$ be positive and $F$ any holomorphic line bundle on a compact complex manifold $X$. Show that there is $k_0$ with $H^q(X, K_X \otimes L^k \otimes F) = 0$ for all $q > 0$ and $k \geq k_0$. Hint: with metrics $h_L, h_F$ and compactness, $k\, i\Theta(L) + i\Theta(F) > 0$ for $k$ large.
6. (C) Use the Euler sequence $0 \to \Omega^1_{\mathbb{P}^n}(k) \to \mathcal{O}(k-1)^{\oplus (n+1)} \to \mathcal{O}(k) \to 0$ of Chapter 2 and Example P6.6.15 to show that $H^q(\mathbb{P}^n, \Omega^1(k)) = 0$ for all $q > 0$ and $k > 0$, and that $H^1(\mathbb{P}^n, \Omega^1) \cong \mathbb{C}$. Compare with Theorem P6.6.12, which gives the vanishing only for $q \geq n$.

### Lean

Mathlib has no Dolbeault cohomology, no Hodge theory for elliptic operators on compact manifolds and no Hermitian line bundles, so neither Serre duality in this analytic form nor the vanishing theorems are formalized, and the project library has no node here.

### Notes and history

Kodaira proved the vanishing theorem for $K_X \otimes L$ in 1953 (Kod53), as the main step towards his embedding theorem, by the integral method of Bochner. Akizuki and Nakano extended it to $\Omega^p_X \otimes L$ in 1954 (AN54a). Serre duality for vector bundles on compact complex manifolds is Serre's (Ser55a), proved there with the theory of distributions; the harmonic proof given here follows Huybrechts, Section 4.1 (Huy05). The proof of the vanishing theorem follows Huybrechts, Section 5.2 (Huy05), Griffiths and Harris, Chapter 1, Section 2 (GH78), and Demailly, Chapter VII (Dem97a). Theorem P7.8.2 of P7 states Kodaira vanishing for ample line bundles on smooth projective varieties as a black box; it can now cite Corollary P6.6.13, together with Corollary P6.7.17 of Chapter 7, which transports the statement through GAGA from positive line bundles on $X^{\mathrm{an}}$ to ample line bundles on $X$. The algebraic proof in characteristic $0$ by Deligne and Illusie, and the failure of Kodaira vanishing in characteristic $p$ found by Raynaud, are outside the scope of this volume.
