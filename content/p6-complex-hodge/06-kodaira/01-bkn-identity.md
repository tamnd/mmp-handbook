---
title: The Bochner-Kodaira-Nakano identity
nodes: []
sources: [Huy05, GH78, Dem97a, Dem12a, Kod53, AN54a, Nak55a]
reads_with: [Huy05:5.2, Dem97a:VII, GH78:1.2]
requires: [P6.2, P6.3, P6.4, P6.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Bochner-Kodaira-Nakano identity

### Statement

Let $X$ be a complex manifold of dimension $n$ with a Hermitian metric whose fundamental form is $\omega$, and let $(E, h)$ be a holomorphic vector bundle with a Hermitian metric. Write $D = D' + D''$ for the Chern connection of $(E, h)$ (Theorem P6.3.16), so that $D'' = \bar\partial_E$ is the Dolbeault operator of the holomorphic structure. Operators on forms are graded by total degree, and the graded commutator of operators $A$ and $B$ of degrees $a$ and $b$ is $[A, B] = AB - (-1)^{ab} BA$.

**Definition P6.6.1 (operators on bundle-valued forms).** Let $A^{p,q}(X, E)$ be the space of smooth $(p,q)$-forms with values in $E$. The metrics $\omega$ and $h$ give a pointwise Hermitian inner product $\langle u, v \rangle$ on $\Lambda^{p,q} T^*_x X \otimes E_x$ and, for forms with compact support, the $L^2$ inner product
$$\langle\langle u, v \rangle\rangle = \int_X \langle u, v \rangle \, dV, \qquad dV = \frac{\omega^n}{n!}, \qquad \|u\|^2 = \langle\langle u, u \rangle\rangle.$$
The *Lefschetz operator* is $L u = \omega \wedge u$, of degree $2$, and $\Lambda$ is its pointwise adjoint, of degree $-2$. The *curvature operator* is $u \mapsto \Theta(E) \wedge u$, where $\Theta(E) = D^2 \in A^{1,1}(X, \operatorname{End} E)$ acts by wedge product on the form part and by composition on $E$; it has degree $2$, and $i\Theta(E)$ denotes $i$ times it. The operators $D' \colon A^{p,q}(X,E) \to A^{p+1,q}(X,E)$ and $\bar\partial_E \colon A^{p,q}(X, E) \to A^{p,q+1}(X, E)$ have degree $1$, and their *formal adjoints* $D'^*$ and $\bar\partial_E^*$ are the first order differential operators of degree $-1$ with $\langle\langle D'u, v\rangle\rangle = \langle\langle u, D'^*v\rangle\rangle$ and $\langle\langle \bar\partial_E u, v\rangle\rangle = \langle\langle u, \bar\partial_E^* v\rangle\rangle$ whenever $u$ or $v$ has compact support. The two *Laplacians* are
$$\Delta' = [D', D'^*] = D' D'^* + D'^* D', \qquad \Delta'' = [\bar\partial_E, \bar\partial_E^*] = \bar\partial_E \bar\partial_E^* + \bar\partial_E^* \bar\partial_E.$$

For the trivial line bundle with the constant metric, $D' = \partial$, $\bar\partial_E = \bar\partial$, and these are the operators of Definition P6.4.11.

**Lemma P6.6.2 (osculating frames).** Let $x \in X$ and let $z_1, \dots, z_n$ be holomorphic coordinates centred at $x$. There is a holomorphic frame $e_1, \dots, e_r$ of $E$ on a neighbourhood of $x$ with
$$h(e_\lambda, e_\mu) = \delta_{\lambda\mu} + O(|z|^2).$$
In such a frame the connection forms of $D$ vanish at $x$: if $D e_\lambda = \sum_\mu \theta_{\mu\lambda} e_\mu$, then $\theta_{\mu\lambda}(x) = 0$.

Lean: not in Lean as stated.

**Proposition P6.6.3 (twisted Kähler identities).** If $\omega$ is a Kähler form, then on $A^{\bullet,\bullet}(X, E)$
$$[\Lambda, \bar\partial_E] = -i D'^*, \qquad [\Lambda, D'] = i \bar\partial_E^*,$$
and, taking adjoints, $[\bar\partial_E^*, L] = i D'$ and $[D'^*, L] = -i \bar\partial_E$.

Lean: not in Lean as stated.

**Theorem P6.6.4 (Bochner-Kodaira-Nakano identity).** If $\omega$ is a Kähler form, then
$$\Delta'' = \Delta' + [i\Theta(E), \Lambda]$$
as operators on $A^{p,q}(X, E)$ for all $p, q$.

Lean: not in Lean as stated.

The operator $[i\Theta(E), \Lambda]$ is of order zero: it is a Hermitian endomorphism of each fibre $\Lambda^{p,q} T^*_x X \otimes E_x$. For a line bundle it can be diagonalized explicitly. At a point $x$ the real $(1,1)$-form $i\Theta(L)_x$ is a Hermitian form on $T_x X$, and since $\omega_x$ is positive definite the two forms can be diagonalized simultaneously.

**Proposition P6.6.5 (the curvature term for a line bundle).** Let $(L, h)$ be a Hermitian holomorphic line bundle and $x \in X$. There is a basis $\zeta_1, \dots, \zeta_n$ of $T^{*1,0}_x X$ and real numbers $\gamma_1 \leq \dots \leq \gamma_n$, the eigenvalues of $i\Theta(L)_x$ with respect to $\omega_x$, with
$$\omega_x = i \sum_{j=1}^n \zeta_j \wedge \bar\zeta_j, \qquad i\Theta(L)_x = i \sum_{j=1}^n \gamma_j \, \zeta_j \wedge \bar\zeta_j.$$
For multi-indices $J, K \subseteq \{1, \dots, n\}$ with $|J| = p$, $|K| = q$, and a vector $e \in L_x$,
$$[i\Theta(L), \Lambda] (\zeta_J \wedge \bar\zeta_K \otimes e) = \Big( \sum_{j \in J} \gamma_j + \sum_{k \in K} \gamma_k - \sum_{j=1}^n \gamma_j \Big) \zeta_J \wedge \bar\zeta_K \otimes e.$$
In particular, on $(n, q)$-forms the eigenvalues are the sums $\sum_{k \in K} \gamma_k$, so $\langle [i\Theta(L), \Lambda] u, u \rangle \geq (\gamma_1 + \dots + \gamma_q) |u|^2$ for $u \in \Lambda^{n,q} T^*_x X \otimes L_x$; and if $i\Theta(L) = \omega$, then $[i\Theta(L), \Lambda] = (p + q - n) \operatorname{id}$ on $(p,q)$-forms.

Lean: not in Lean as stated.

**Corollary P6.6.6 (the Bochner-Kodaira-Nakano inequality).** Let $(X, \omega)$ be a Kähler manifold and $(L, h)$ a Hermitian holomorphic line bundle. For every $u \in A^{p,q}(X, L)$ with compact support,
$$\|\bar\partial_L u\|^2 + \|\bar\partial_L^* u\|^2 = \|D' u\|^2 + \|D'^* u\|^2 + \int_X \langle [i\Theta(L), \Lambda] u, u \rangle \, dV \geq \int_X \langle [i\Theta(L), \Lambda] u, u \rangle \, dV.$$
If $p = n$ and $\gamma_1(x) \leq \dots \leq \gamma_n(x)$ are the eigenvalues of $i\Theta(L)$ at $x$, the right side is at least $\int_X (\gamma_1 + \dots + \gamma_q) |u|^2 \, dV$.

Lean: not in Lean as stated.

When $X$ is compact every form has compact support, and the inequality applies to all of $A^{p,q}(X, L)$.

### Proof in words

The Kähler identities (Theorem P6.4.12) relate $\Lambda$ to the adjoints of $\partial$ and $\bar\partial$. Each identity compares first order differential operators, and the value of such an operator at a point depends only on the first derivatives of the metrics there. A Kähler metric agrees with the flat metric to second order in suitable coordinates, and a holomorphic frame of $E$ can be chosen orthonormal to second order at the point. In these coordinates and this frame every operator in the identity agrees at the point with its counterpart for the flat trivial bundle on $\mathbb{C}^n$, where the identities hold componentwise. This proves the twisted Kähler identities.

The Bochner-Kodaira-Nakano identity then follows by formal algebra. Replace $\bar\partial_E^*$ by $-i[\Lambda, D']$ in $\Delta''$, expand with the graded Jacobi identity, and use $[\bar\partial_E, D'] = \Theta(E)$, which holds because $D'^2$ and $\bar\partial_E^2$ vanish for the Chern connection. The terms that come out are $\Delta'$ and $[i\Theta(E), \Lambda]$.

For a line bundle the two operators $\omega \wedge$ and $i\Theta \wedge$ split, in a basis that diagonalizes both forms, into sums of commuting pieces, one for each coordinate direction. On each piece the commutator with $\Lambda$ is $+1$, $-1$ or $0$ on the basis forms, according to whether $dz_j \wedge d\bar z_j$ divides the form, $dz_j$ and $d\bar z_j$ are both absent, or exactly one of them occurs. Summing with the weights $\gamma_j$ gives the eigenvalue formula. Integrating the identity against $u$ gives the inequality, since $\langle\langle \Delta' u, u\rangle\rangle = \|D'u\|^2 + \|D'^*u\|^2 \geq 0$.

### Examples

**Example P6.6.7 (a weight on the plane).** Let $X = \mathbb{C}$ with $\omega_0 = \frac{i}{2} dz \wedge d\bar z = dx \wedge dy$, and let $L$ be the trivial line bundle with frame $e = 1$ and metric $|e|^2_h = e^{-\varphi}$ for a smooth real function $\varphi$. The Chern connection is $D' u = (u_z - \varphi_z u)\, dz$ on functions, the curvature is $\Theta = -\partial\bar\partial \log e^{-\varphi} = \partial \bar\partial \varphi = \varphi_{z\bar z} \, dz \wedge d\bar z$, and $i\Theta = 2 \varphi_{z \bar z} \, \omega_0$. Since $\Lambda u = 0$ for a function and $\Lambda \omega_0 = 1$, Proposition P6.6.5 predicts $(\Delta'' - \Delta') u = [i\Theta, \Lambda] u = -2 \varphi_{z\bar z} u$. Here is the direct check. With $|d\bar z|^2 = |dz|^2 = 2$ and $u, f$ of compact support, integration by parts gives
$$\langle\langle \bar\partial u, f\, d\bar z \rangle\rangle = 2\int u_{\bar z} \bar f e^{-\varphi} \, dV = -2 \int u \, \overline{\partial_z (f e^{-\varphi})} \, dV,$$
so $\bar\partial^*(f \, d\bar z) = -2 e^{\varphi} \partial_z(f e^{-\varphi}) = -2(f_z - \varphi_z f)$. Similarly $\langle\langle D'u, g \, dz \rangle\rangle = 2\int (u_z - \varphi_z u) \bar g e^{-\varphi} dV = -2 \int u \, \overline{g_{\bar z}} \, e^{-\varphi} dV$, so $D'^*(g\, dz) = -2 g_{\bar z}$. Hence
$$\Delta'' u = \bar\partial^* \bar\partial u = -2(u_{z\bar z} - \varphi_z u_{\bar z}), \qquad \Delta' u = D'^* D' u = -2(u_{z \bar z} - \varphi_{z\bar z} u - \varphi_z u_{\bar z}),$$
and $\Delta'' u - \Delta' u = -2 \varphi_{z \bar z} u$, as predicted. For $\varphi = |z|^2$ the eigenvalue of $i\Theta$ relative to $\omega_0$ is $\gamma = 2$. On $\mathbb{C}^n$ with $\varphi = |z|^2$ one has $i\Theta = i \sum_j dz_j \wedge d\bar z_j = 2\omega_0$, all $\gamma_j = 2$, and Corollary P6.6.6 gives $\|\bar\partial u\|^2 + \|\bar\partial^*_\varphi u\|^2 \geq 2q \|u\|^2_\varphi$ for compactly supported $(n,q)$-forms $u$, the estimate that Chapter 8 develops into Hörmander's theorem.

**Example P6.6.8 (line bundles on a curve).** Let $X$ be a compact Riemann surface with a Kähler form $\omega$ and $(L, h)$ a Hermitian line bundle with $i\Theta(L) = \gamma \omega$ for a smooth real function $\gamma$. With $n = 1$ and $\zeta$ as in Proposition P6.6.5, the eigenvalue of $[i\Theta, \Lambda]$ is $-\gamma$ on $1$ ($J = K = \emptyset$), $0$ on $\zeta$ and on $\bar\zeta$, and $\gamma$ on $\zeta \wedge \bar\zeta$. If $\deg L > 0$, then $L$ has a metric with $\gamma > 0$ everywhere (Example P6.5.25), and for an $L$-valued $(1,1)$-form $u$, Corollary P6.6.6 gives $\|\bar\partial_L^* u\|^2 \geq \int_X \gamma |u|^2 dV$, since $\bar\partial_L u = 0$ for degree reasons. So no nonzero $L$-valued $(1,1)$-form satisfies $\bar\partial_L^* u = 0$; with the Hodge theory of Section 6.2 this says $H^1(X, K_X \otimes L) = 0$. The hypothesis cannot be dropped: for the trivial bundle with the constant metric, $\gamma = 0$, and $\omega$ itself is a $(1,1)$-form with $\bar\partial^* \omega = 0$ (it is harmonic, since $\partial^*\omega = 0$ and $\bar\partial^*\omega = 0$ follow from $d\omega = 0$ and Theorem P6.4.12); correspondingly $H^1(X, K_X) \cong H^{1,1}(X) \cong \mathbb{C}$.

**Example P6.6.9 ($(n,q)$-forms and $(0,q)$-forms).** In the notation of Proposition P6.6.5, the eigenvalue on $\zeta_J \wedge \bar\zeta_K$ with $J = \{1, \dots, n\}$ is $\sum_{k \in K} \gamma_k$, and with $J = \emptyset$ it is $-\sum_{j \notin K} \gamma_j$. So for a positive line bundle, where all $\gamma_j > 0$, the curvature term is positive on $(n, q)$-forms with $q \geq 1$ and negative on $(0, q)$-forms with $q < n$. The inequality therefore says nothing about $H^q(X, L)$ for a positive $L$, and these groups need not vanish. On a compact Riemann surface $X$ of genus $2$ let $L = \mathcal{O}_X(x)$ for a point $x$, positive since $\deg L = 1$. Serre duality (Section 6.2) gives $H^1(X, L) \cong H^0(X, K_X \otimes L^{-1})^*$, the dual of the space of holomorphic $1$-forms vanishing at $x$. Since $h^0(K_X) = 2$ and vanishing at $x$ is one linear condition, this space is nonzero, so $H^1(X, L) \neq 0$. For $n = 1$ and $J = \emptyset$, $K = \{1\}$ the eigenvalue $\gamma_1 - \gamma_1 = 0$ is consistent with this.

### Proof

*Lemma P6.6.2.* Start with any holomorphic frame and apply a constant linear change so that it is orthonormal at $x$. Write $H = (h_{\lambda\mu})$ with $h_{\lambda\mu} = h(e_\lambda, e_\mu)$. Taylor expansion gives
$$h_{\lambda\mu} = \delta_{\lambda\mu} + \sum_j \big( a_{j\lambda\mu} z_j + \overline{a_{j\mu\lambda}} \, \bar z_j \big) + O(|z|^2),$$
where the coefficient of $\bar z_j$ is forced by $h_{\mu\lambda} = \overline{h_{\lambda\mu}}$. Put $e'_\lambda = e_\lambda - \sum_{j, \nu} a_{j\lambda\nu} z_j e_\nu$, a holomorphic frame near $x$ equal to $e_\lambda$ at $x$. Then
$$h(e'_\lambda, e'_\mu) = h_{\lambda\mu} - \sum_{j} a_{j\lambda\mu} z_j - \sum_j \overline{a_{j\mu\lambda}} \, \bar z_j + O(|z|^2) = \delta_{\lambda\mu} + O(|z|^2).$$
For the second claim, metric compatibility gives $d h(e_\lambda, e_\mu) = h(D e_\lambda, e_\mu) + h(e_\lambda, D e_\mu)$. Since $e_\lambda$ is holomorphic, $D'' e_\lambda = 0$ and $D e_\lambda = \sum_\nu \theta_{\nu\lambda} e_\nu$ with $\theta_{\nu\lambda}$ of type $(1,0)$. Comparing $(1,0)$ parts, $\partial h_{\lambda\mu} = \sum_\nu \theta_{\nu\lambda} h_{\nu\mu}$. At $x$ the left side is $0$ and $h_{\nu\mu}(x) = \delta_{\nu\mu}$, so $\theta_{\mu\lambda}(x) = 0$.

*Proposition P6.6.3.* Fix $x \in X$. Since $\omega$ is Kähler, part 3 of Proposition P6.4.2 gives holomorphic coordinates centred at $x$ with $\omega = \frac{i}{2} \sum_{j,k} g_{j\bar k} \, dz_j \wedge d\bar z_k$ and $g_{j\bar k} = \delta_{jk} + O(|z|^2)$. Take a frame as in Lemma P6.6.2. Write $u = \sum_{J, K, \lambda} u_{JK\lambda} \, dz_J \wedge d\bar z_K \otimes e_\lambda$, and let $G$ be the Hermitian matrix of the pointwise inner product in the basis $dz_J \wedge d\bar z_K \otimes e_\lambda$ and $\rho$ the density of $dV$ against Lebesgue measure. Both are built algebraically from $(g_{j \bar k})$ and $(h_{\lambda\mu})$, so $G = G_0 + O(|z|^2)$ and $\rho = \rho_0 + O(|z|^2)$, where $G_0, \rho_0$ are the constant values for the flat model: $\mathbb{C}^n$ with $\omega_0 = \frac{i}{2}\sum dz_j \wedge d\bar z_j$ and the trivial bundle $\mathbb{C}^r$ with its standard metric. Now compare each operator at the point $x$ with its flat counterpart, acting on the coefficient functions $u_{JK\lambda}$.

The operator $\bar\partial_E$ acts on the coefficients by $\bar\partial$, since the $e_\lambda$ are holomorphic; this is the flat operator. The operator $D'$ is $\partial$ on the coefficients plus the zeroth order term $\theta \wedge$, which vanishes at $x$. The operators $L$ and $\Lambda$ are zeroth order with coefficients built from $(g_{j\bar k})$; their values and first derivatives at $x$ are the flat ones. For a first order operator $P = \sum_m a_m \partial_m + b$ in the real coordinates of $\mathbb{R}^{2n}$, integration by parts against $\rho \, \bar v^{T} G u$ gives the formal adjoint
$$P^* v = -\rho^{-1} G^{-1} \sum_m \partial_m \big( \rho\, a_m^{\dagger} G v \big) + G^{-1} b^{\dagger} G v,$$
where $\dagger$ is the conjugate transpose. At $x$ this involves the values and first derivatives of $a_m$, $b$, $G$ and $\rho$. For $P = \bar\partial_E$ and $P = \partial$ the $a_m$ are constant matrices and $b = 0$, and the first derivatives of $G$ and $\rho$ vanish at $x$, so $\bar\partial_E^*$ and the adjoint of the $\partial$ part of $D'$ agree at $x$ with the flat adjoints. The adjoint of $\theta \wedge$ is the pointwise adjoint, which vanishes at $x$. Finally, $[\Lambda, \bar\partial_E] u = \Lambda \bar\partial_E u - \bar\partial_E (\Lambda u)$, and $\bar\partial_E(\Lambda u)$ at $x$ involves $\Lambda$ and its first derivatives at $x$, which are flat. The same holds for $[\Lambda, D']$.

So at $x$ both sides of each identity equal the corresponding sides for the flat model, applied to the coefficients $u_{JK\lambda}$ for $\lambda = 1, \dots, r$. On the flat model the identities are the Kähler identities $[\Lambda, \bar\partial] = -i\partial^*$ and $[\Lambda, \partial] = i\bar\partial^*$ of Theorem P6.4.12 for $\mathbb{C}^n$ with $\omega_0$, applied to each component. So the identities hold at $x$, and $x$ was arbitrary. Taking formal adjoints, $([\Lambda, \bar\partial_E])^* = [\bar\partial_E^*, L]$, since $\Lambda^* = L$ and $(AB)^* = B^* A^*$; so $[\bar\partial_E^*, L] = (-iD'^*)^* = i D'$. In the same way $[D'^*, L] = (i \bar\partial_E^*)^* = -i\bar\partial_E$.

*Theorem P6.6.4.* For the Chern connection the curvature has type $(1,1)$ (Theorem P6.3.16), so the $(2,0)$ and $(0,2)$ parts of $D^2 = (D' + \bar\partial_E)^2$ vanish: $D'^2 = 0$, $\bar\partial_E^2 = 0$, and
$$\Theta(E) = D' \bar\partial_E + \bar\partial_E D' = [\bar\partial_E, D'].$$
By Proposition P6.6.3, $\bar\partial_E^* = -i[\Lambda, D']$, so $\Delta'' = [\bar\partial_E, \bar\partial_E^*] = -i [\bar\partial_E, [\Lambda, D']]$. The graded Jacobi identity $[A, [B, C]] = [[A, B], C] + (-1)^{ab} [B, [A, C]]$ with $A = \bar\partial_E$ of degree $1$, $B = \Lambda$ of degree $-2$ and $C = D'$ gives
$$[\bar\partial_E, [\Lambda, D']] = [[\bar\partial_E, \Lambda], D'] + [\Lambda, [\bar\partial_E, D']].$$
Since $\Lambda$ has even degree, $[\bar\partial_E, \Lambda] = -[\Lambda, \bar\partial_E] = i D'^*$, so the first term is $i[D'^*, D'] = i \Delta'$. The second term is $[\Lambda, \Theta(E)]$. Hence
$$\Delta'' = -i \big( i\Delta' + [\Lambda, \Theta(E)] \big) = \Delta' - i[\Lambda, \Theta(E)] = \Delta' + [i\Theta(E), \Lambda],$$
where the last step uses that $\Theta(E)$ and $\Lambda$ have even degree, so $[\Lambda, \Theta(E)] = -[\Theta(E), \Lambda]$.

*Proposition P6.6.5.* Two Hermitian forms on $T_x X$, one positive definite, are diagonalized by a common basis, which gives the $\zeta_j$ and $\gamma_j$. Write $\zeta_j = (\alpha_j + i\beta_j)/\sqrt{2}$ with $\alpha_j, \beta_j$ real. Then $i \zeta_j \wedge \bar\zeta_j = \alpha_j \wedge \beta_j$, so $\omega_x = \sum_j \alpha_j \wedge \beta_j$ and $\alpha_1, \beta_1, \dots, \alpha_n, \beta_n$ is an orthonormal basis of $T_x^* X$ for the Riemannian metric of $\omega$. In the Hermitian extension of this metric, $|\zeta_j|^2 = |\bar\zeta_j|^2 = 1$ and $\langle \zeta_j, \bar\zeta_j \rangle = \frac12 (\langle \alpha_j, \alpha_j \rangle + i \cdot \overline{(-i)} \langle \beta_j, \beta_j \rangle) = \frac12(1 - 1) = 0$, so $\zeta_1, \bar\zeta_1, \dots, \zeta_n, \bar\zeta_n$ is an orthonormal basis of $T^*_x X \otimes \mathbb{C}$, and the forms $\zeta_J \wedge \bar \zeta_K$ are orthonormal. Since $L$ is a line bundle, the factor $e \in L_x$ plays no role, and it can be dropped.

Put $\sigma_j = i\zeta_j \wedge \bar\zeta_j$, a $2$-form; the $\sigma_j$ commute with all forms. For pairwise disjoint subsets $A, B, C$ of $\{1, \dots, n\}$ put $b_{A,B,C} = \sigma_A \wedge \zeta_B \wedge \bar\zeta_C$, with $\sigma_A = \bigwedge_{j \in A} \sigma_j$. Moving factors shows that $\zeta_J \wedge \bar\zeta_K = c \, b_{J \cap K, J \setminus K, K \setminus J}$ with $|c| = 1$, so the $b_{A,B,C}$ form an orthonormal basis. Let $L_j$ be the operator $\sigma_j \wedge$ and $\Lambda_j$ its adjoint. Then $L_j b_{A,B,C} = b_{A \cup \{j\}, B, C}$ if $j \notin A \cup B \cup C$ and $L_j b_{A,B,C} = 0$ otherwise. So $L_j$ maps the orthonormal basis to itself or to $0$, injectively where it is nonzero, and its adjoint is $\Lambda_j b_{A,B,C} = b_{A \setminus \{j\}, B, C}$ if $j \in A$ and $0$ otherwise. Hence:

- for $j \neq k$, both $L_j \Lambda_k$ and $\Lambda_k L_j$ send $b_{A,B,C}$ to $b_{(A \setminus \{k\}) \cup \{j\}, B, C}$ when $k \in A$ and $j \notin A \cup B \cup C$, and to $0$ otherwise, so $[L_j, \Lambda_k] = 0$;
- $[L_j, \Lambda_j] b_{A,B,C}$ is $b_{A,B,C}$ if $j \in A$, $-b_{A,B,C}$ if $j \notin A \cup B \cup C$, and $0$ if $j \in B \cup C$.

Now $\Lambda = \sum_k \Lambda_k$, because $L = \sum_j L_j$, and the curvature operator is $\sum_j \gamma_j L_j$. So
$$[i\Theta(L), \Lambda] \, b_{A,B,C} = \sum_{j,k} \gamma_j [L_j, \Lambda_k] \, b_{A,B,C} = \Big( \sum_{j \in A} \gamma_j - \sum_{j \notin A \cup B \cup C} \gamma_j \Big) b_{A,B,C}.$$
With $A = J \cap K$ and $A \cup B \cup C = J \cup K$, and using $\sum_J + \sum_K = \sum_{J \cup K} + \sum_{J \cap K}$, the coefficient is $\sum_{j \in J}\gamma_j + \sum_{k \in K} \gamma_k - \sum_{j=1}^n \gamma_j$. For $J = \{1, \dots, n\}$ it is $\sum_{k \in K} \gamma_k \geq \gamma_1 + \dots + \gamma_q$, since the $\gamma_j$ are increasing and $|K| = q$. Since the basis is orthonormal and the operator is diagonal in it, $\langle [i\Theta, \Lambda] u, u \rangle \geq (\gamma_1 + \dots + \gamma_q) |u|^2$ on $(n,q)$-forms. If all $\gamma_j = 1$, the coefficient is $p + q - n$.

*Corollary P6.6.6.* For compactly supported $u$, $\langle\langle \Delta'' u, u \rangle\rangle = \|\bar\partial_L u\|^2 + \|\bar\partial_L^* u\|^2$ and $\langle\langle \Delta' u, u \rangle\rangle = \|D' u\|^2 + \|D'^* u\|^2$ by the definition of the formal adjoints. Pair Theorem P6.6.4 with $u$. The bound for $p = n$ is the pointwise bound of Proposition P6.6.5, integrated.

### Exercises

1. (A) Use the operators $L_j$ and $\Lambda_j$ from the proof of Proposition P6.6.5 to show that $[L, \Lambda] = (p + q - n)\operatorname{id}$ on $(p,q)$-forms at a point, which is the identity $[L, \Lambda] = H$ of Theorem P6.4.9 on forms of degree $k$.
2. (A) In Example P6.6.7, compute $\Delta'' u - \Delta' u$ for an $L$-valued $(1,1)$-form $u = g\,\omega_0$ on $\mathbb{C}$ with compact support, and check that it equals $2\varphi_{z\bar z} u$, as Proposition P6.6.5 predicts for $J = K = \{1\}$.
3. (B) Let $(L, h)$ be a Hermitian line bundle and $e$ a holomorphic frame with $|e|^2_h = 1 + O(|z|^2)$ at $x$, as in Lemma P6.6.2. Show that $\Theta(L)_x = -\partial\bar\partial |e|^2_h (x)$, and deduce that if $\Theta(L)_x \neq 0$ there is no holomorphic frame with $|e|^2_h = 1 + O(|z|^3)$ at $x$.
4. (B) Let $(E, h)$ be a flat Hermitian holomorphic vector bundle on a compact Kähler manifold, that is, $\Theta(E) = 0$. Show that $\Delta' = \Delta''$ on $A^{p,q}(X, E)$, and deduce that a form with values in $E$ is $\Delta''$-harmonic if and only if it is $\Delta'$-harmonic. For the trivial bundle this is the equality $\Delta_\partial = \Delta_{\bar\partial}$ of Theorem P6.4.12.
5. (B) Let $(X, \omega)$ be compact Kähler and $(L, h)$ a Hermitian line bundle with $i\Theta(L) \leq 0$ everywhere. Show that every holomorphic section $s$ of $L$ satisfies $D's = 0$, so that $|s|^2_h$ is constant, and that $s$ is either zero or nowhere zero. Hint: for $u = s$ of type $(0,0)$ the curvature term is $-\sum_j \gamma_j \geq 0$.
6. (C) Let $X$ be a compact Kähler manifold and $L$ a Hermitian line bundle with $i\Theta(L) \geq 0$ everywhere and with at least $n - q + 1$ positive eigenvalues at every point, for some $q \geq 1$. Show that every $\Delta''$-harmonic $L$-valued $(n, q')$-form with $q' \geq q$ is zero, and deduce with Theorem P6.6.10 that $H^{q'}(X, K_X \otimes L) = 0$ for $q' \geq q$. This is Girbau's theorem.

### Lean

Mathlib has smooth manifolds, complex manifolds in the sense of holomorphic charts, and inner product spaces, but it has no Hermitian holomorphic vector bundles, Chern connections or formal adjoints of differential operators. The statements of this section are not formalized, and the project library has no node here.

### Notes and history

The method of proving vanishing by an integral identity between two Laplacians goes back to Bochner, who used Weitzenböck formulas on Riemannian manifolds in the 1940s. Kodaira applied it to line bundles on Kähler manifolds (Kod53), and Akizuki and Nakano (AN54a) and Nakano (Nak55a) extended it to forms of type $(p,q)$ and to vector bundles; the identity of Theorem P6.6.4 is often named after all three. The derivation from the twisted Kähler identities by the graded Jacobi identity follows Demailly, Chapter VII (Dem97a), and Demailly's lectures (Dem12a), where the identity is also proved for non-Kähler metrics with additional torsion terms; Huybrechts, Section 5.2 (Huy05), and Griffiths and Harris, Chapter 1, Section 2 (GH78), give the proof in the form used here. Exercise 6 is due to Girbau, and Chapter 8 uses Corollary P6.6.6 for $(n,q)$-forms with singular weights.
