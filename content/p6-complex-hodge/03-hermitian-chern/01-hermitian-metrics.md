---
title: Hermitian metrics
nodes: []
sources: [Huy05, Voi02, GH78, Wel80]
reads_with: [Huy05:1.2, Huy05:4.1, Voi02:3, GH78:0.2]
requires: [P6.1, P6.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Hermitian metrics

### Statement

Throughout the chapter $X$ is a complex manifold of dimension $n$ with the conventions of Chapters 1 and 2: $z_j = x_j + i y_j$ are local holomorphic coordinates, $dz_j \wedge d\bar z_j = -2i\, dx_j \wedge dy_j$, and $\omega_0 = \frac{i}{2} \sum_j dz_j \wedge d\bar z_j = \sum_j dx_j \wedge dy_j$ is the standard form on $\mathbb{C}^n$. The real tangent bundle carries the almost complex structure $J$ of Definition P6.2.9, and the $\mathbb{R}$-linear map $v \mapsto v^{1,0} = \frac{1}{2}(v - iJv)$ identifies $(T_xX, J)$ with the holomorphic tangent space $T^{1,0}_x X$ as complex vector spaces; it sends $\partial/\partial x_j$ to $\partial/\partial z_j$. For a real tangent vector $v$ and a $(1,0)$-form $\varphi$, $\varphi(v) = \varphi(v^{1,0})$ and $\varphi(Jv) = i \varphi(v)$.

**Definition P6.3.1 (Hermitian structures on a vector space).** Let $V$ be a real vector space of dimension $2n$ with a complex structure $J$, that is, an endomorphism with $J^2 = -1$, so that $V$ is a complex vector space with $i v = Jv$.

1. A *Hermitian form* on $V$ is a map $h: V \times V \to \mathbb{C}$ that is $\mathbb{C}$-linear in the first variable, satisfies $h(v, u) = \overline{h(u, v)}$, and is positive definite: $h(v, v) > 0$ for $v \neq 0$.
2. A Riemannian inner product $g$ on $V$ is *compatible with $J$* if $g(Ju, Jv) = g(u, v)$ for all $u, v$. Its *fundamental form* is the real bilinear form $\omega(u, v) = g(Ju, v)$.
3. An ordered basis $e_1, \dots, e_n$ of the complex vector space $V$ is *unitary* for $h$ if $h(e_j, e_k) = \delta_{jk}$.

**Proposition P6.3.2 (the metric, the Hermitian form and the fundamental form).** Let $(V, J)$ be as in Definition P6.3.1.

1. If $g$ is compatible with $J$, then $\omega$ is alternating and $J$-invariant, $g(u, v) = \omega(u, Jv)$, and $h = g - i\omega$ is a Hermitian form. Conversely, every Hermitian form $h$ arises in this way from exactly one compatible $g$, namely $g = \operatorname{Re} h$, and then $\omega = -\operatorname{Im} h$.
2. Let $V = \mathbb{C}^n$ and let $h(u, v) = \sum_{j,k} h_{jk} u_j \bar v_k$ with $H = (h_{jk})$ a positive definite Hermitian matrix. Then, as a form on $\mathbb{C}^n$ with the linear coordinates $z_j$,
$$\omega = \frac{i}{2} \sum_{j,k} h_{jk}\, dz_j \wedge d\bar z_k.$$
For the standard Hermitian form, $H = I$, this is $\omega_0$, and $g$ is the Euclidean inner product.
3. With $V$ oriented by its complex structure, $\omega^n / n!$ is the volume form of $g$. In the situation of part 2, $\omega^n / n! = \det(H)\, dx_1 \wedge dy_1 \wedge \dots \wedge dx_n \wedge dy_n$.

Lean: not yet in Lean.

**Definition P6.3.3 (real and positive $(1,1)$-forms).** Let $\alpha$ be a $(1,1)$-form on $X$, written locally as $\alpha = i \sum_{j,k} a_{jk}\, dz_j \wedge d\bar z_k$. The form $\alpha$ is *real* if $\bar\alpha = \alpha$. A real $(1,1)$-form is *positive* at $x$ if the Hermitian matrix $(a_{jk}(x))$ is positive definite, and *semipositive* at $x$ if it is positive semidefinite; it is positive or semipositive if it is so at every point. A real $(1,1)$-form $\alpha$ is *negative* if $-\alpha$ is positive.

**Proposition P6.3.4 (positive $(1,1)$-forms and Hermitian matrices).** Let $\alpha = i \sum a_{jk}\, dz_j \wedge d\bar z_k$ be a $(1,1)$-form at a point $x$ and $A = (a_{jk})$.

1. $\alpha$ is real if and only if $A$ is Hermitian, $a_{kj} = \overline{a_{jk}}$. For a real smooth function $\varphi$, the form $i \partial\bar\partial \varphi$ is real, with matrix $(\partial^2 \varphi / \partial z_j \partial \bar z_k)$.
2. For a real tangent vector $v$ with $\xi_j = dz_j(v)$, $\alpha(v, Jv) = 2 \sum_{j,k} a_{jk} \xi_j \bar\xi_k$.
3. For real $\alpha$ the following are equivalent: $\alpha$ is positive at $x$; $\alpha(v, Jv) > 0$ for every nonzero real $v \in T_xX$; $\alpha$ is the fundamental form of a compatible inner product on $(T_xX, J)$, namely $g(u, v) = \alpha(u, Jv)$; there is a basis $\theta_1, \dots, \theta_n$ of $(1,0)$-covectors with $\alpha = i \sum_j \theta_j \wedge \bar\theta_j$.
4. Positivity does not depend on the coordinates, and positive forms at $x$ form an open convex cone in the real vector space of real $(1,1)$-covectors.

Lean: not yet in Lean.

**Definition P6.3.5 (Hermitian metrics on bundles and manifolds).** Let $E$ be a smooth complex vector bundle of rank $r$ on a smooth manifold $X$. A *Hermitian metric* on $E$ is a family of Hermitian forms $h_x$ on the fibres $E_x$ such that for every local frame $e_1, \dots, e_r$ of $E$ the functions $h(e_j, e_k)$ are smooth. A *Hermitian metric on a complex manifold* $X$ is a Hermitian metric $h$ on the holomorphic tangent bundle $T^{1,0} X$. Through the identification $v \mapsto v^{1,0}$ it is the same as a Riemannian metric $g = \operatorname{Re} h$ compatible with $J$, and its *fundamental form* is $\omega(u, v) = g(Ju, v)$. In coordinates, with $h_{jk} = h(\partial/\partial z_j, \partial/\partial z_k)$,
$$\omega = \frac{i}{2} \sum_{j,k} h_{jk}\, dz_j \wedge d\bar z_k.$$

**Proposition P6.3.6 (existence of Hermitian metrics).** Let $X$ be a smooth manifold, Hausdorff and second countable.

1. Every smooth complex vector bundle $E$ on $X$ has a Hermitian metric, and the Hermitian metrics on $E$ form a convex set. Every complex manifold has a Hermitian metric.
2. Metrics $h_E$, $h_F$ on $E$ and $F$ induce metrics on $E^*$, $E \oplus F$, $E \otimes F$, $\Lambda^k E$ and $f^* E$ for a smooth map $f: Y \to X$. A metric on $E$ restricts to every subbundle $S$ and identifies a quotient $E/S$ with the orthogonal complement $S^\perp$, which gives $E/S$ a metric.
3. Under the map $h \mapsto \omega$ of Definition P6.3.5, Hermitian metrics on a complex manifold $X$ correspond bijectively to real $(1,1)$-forms on $X$ that are positive at every point.

Lean: not yet in Lean.

### Proof in words

A compatible inner product, a Hermitian form and a positive $(1,1)$-covector are three descriptions of one object. The real part of a Hermitian form is an inner product preserved by $J$, and minus its imaginary part is the fundamental form; conversely the inner product is recovered from the fundamental form by $g(u, v) = \omega(u, Jv)$. In linear coordinates the fundamental form of $\sum h_{jk} u_j \bar v_k$ is $\frac{i}{2} \sum h_{jk}\, dz_j \wedge d\bar z_k$, which is checked by evaluating both sides on a pair of vectors. A unitary basis turns any Hermitian form into the standard one, and for the standard form $\omega^n / n!$ is visibly the Euclidean volume form. Positivity of $\alpha$ is the statement that $\alpha(v, Jv) > 0$, because this number is twice the Hermitian form of the matrix $A$ on the vector $\xi = dz(v)$. Partitions of unity glue local flat metrics into a global one, since a convex combination of positive definite matrices is positive definite.

### Examples

**Example P6.3.7 (flat metrics on $\mathbb{C}^n$ and on tori).** On $\mathbb{C}^n$ every positive definite Hermitian matrix $H$ with constant entries gives a Hermitian metric with fundamental form $\omega_H = \frac{i}{2} \sum h_{jk}\, dz_j \wedge d\bar z_k$, and $H = I$ gives $\omega_0$. Let $X = \mathbb{C}^n / \Lambda$ be a complex torus as in Example P6.2.3, with $\Lambda$ a lattice of rank $2n$. Translations preserve $dz_j$, so $\omega_H$ descends to a positive closed $(1,1)$-form on $X$, and every Hermitian matrix $H > 0$ gives a Hermitian metric on $X$. By Proposition P6.3.2, $\int_X \omega_H^n / n! = \det(H) \operatorname{vol}(\mathbb{C}^n / \Lambda)$, where $\operatorname{vol}$ is the Euclidean volume of a fundamental parallelepiped. For the elliptic curve $X = \mathbb{C} / (\mathbb{Z} + \mathbb{Z}\tau)$ with $\operatorname{Im} \tau > 0$, the fundamental parallelogram spanned by $1$ and $\tau$ has area $\operatorname{Im} \tau$, so $\int_X \omega_0 = \operatorname{Im} \tau$.

**Example P6.3.8 (the Fubini-Study form).** On $\mathbb{P}^n$ with homogeneous coordinates $Z_0, \dots, Z_n$ and $\|Z\|^2 = \sum |Z_j|^2$, put $\varphi_i = \log(\|Z\|^2 / |Z_i|^2)$ on $U_i = \{Z_i \neq 0\}$. This is a well-defined smooth real function on $U_i$, since the quotient is invariant under $Z \mapsto \lambda Z$. On $U_i \cap U_j$, $\varphi_i - \varphi_j = \log |Z_j / Z_i|^2 = \log |g_{ij}|^2$ with $g_{ij} = Z_j / Z_i$ holomorphic and nowhere zero. For a nowhere zero holomorphic $g$, locally $\log |g|^2 = \ell + \bar\ell$ with $\ell$ a holomorphic logarithm of $g$, and $\partial\bar\partial \ell = 0$ and $\partial\bar\partial \bar\ell = -\bar\partial \partial \bar\ell = -\bar\partial(\overline{\bar\partial \ell}) = 0$. So $\partial\bar\partial \varphi_i = \partial\bar\partial \varphi_j$ on $U_i \cap U_j$, and
$$\omega_{FS} = \frac{i}{2\pi} \partial\bar\partial \varphi_i \quad \text{on } U_i$$
is a global $(1,1)$-form, written $\omega_{FS} = \frac{i}{2\pi} \partial\bar\partial \log \|Z\|^2$: its pullback to $\mathbb{C}^{n+1} \setminus \{0\}$ is $\frac{i}{2\pi} \partial\bar\partial \log \|Z\|^2$. It is real by Proposition P6.3.4 and closed, since $d \partial\bar\partial = (\partial + \bar\partial) \partial\bar\partial = 0$ by Proposition P6.1.33. In the chart $U_0$ with $z_j = Z_j / Z_0$, $\varphi_0 = \log(1 + |z|^2)$ and $\bar\partial \varphi_0 = \sum_k z_k\, d\bar z_k / (1 + |z|^2)$, so
$$\omega_{FS} = \frac{i}{2\pi} \frac{(1 + |z|^2) \sum_j dz_j \wedge d\bar z_j - \sum_{j,k} \bar z_j z_k\, dz_j \wedge d\bar z_k}{(1 + |z|^2)^2}.$$
Its matrix is $a_{jk} = \frac{1}{2\pi} ((1 + |z|^2)\delta_{jk} - \bar z_j z_k) / (1 + |z|^2)^2$, and for $\xi \in \mathbb{C}^n$, $\sum a_{jk} \xi_j \bar\xi_k = \frac{1}{2\pi} ((1 + |z|^2) |\xi|^2 - |\sum_j \bar z_j \xi_j|^2) / (1 + |z|^2)^2 \geq \frac{1}{2\pi} |\xi|^2 / (1 + |z|^2)^2$ by the Cauchy-Schwarz inequality. So $\omega_{FS}$ is positive on $U_0$, and by symmetry of the coordinates on every $U_i$: it is the fundamental form of a Hermitian metric on $\mathbb{P}^n$, the *Fubini-Study metric*. For $n = 1$, with $z = x + iy$ and $r = |z|$,
$$\omega_{FS} = \frac{i}{2\pi} \frac{dz \wedge d\bar z}{(1 + |z|^2)^2} = \frac{1}{\pi} \frac{dx \wedge dy}{(1 + r^2)^2}, \qquad \int_{\mathbb{P}^1} \omega_{FS} = \frac{1}{\pi} \int_0^\infty \frac{2\pi r\, dr}{(1 + r^2)^2} = \Big[ -\frac{1}{1 + r^2} \Big]_0^\infty = 1,$$
since the complement of $U_0$ is one point. A linear embedding $\mathbb{P}^1 \to \mathbb{P}^n$ given by an isometric linear map $\mathbb{C}^2 \to \mathbb{C}^{n+1}$ preserves $\|Z\|^2$, so it pulls $\omega_{FS}$ back to $\omega_{FS}$, and every line in $\mathbb{P}^n$ has area $1$. The unitary group $U(n+1)$ preserves $\|Z\|^2$ and so preserves $\omega_{FS}$.

**Example P6.3.9 (induced metrics on $\mathcal{O}(-1)$ and $\mathcal{O}(1)$).** The tautological line bundle $\mathcal{O}(-1) \subset \mathbb{P}^n \times \mathbb{C}^{n+1}$ has fibre the line $\mathbb{C} Z$ over $[Z]$ and frames $\varepsilon_i([Z]) = Z / Z_i$ on $U_i$. Since $\varepsilon_j = (Z_i / Z_j) \varepsilon_i$, its transition functions are $Z_i / Z_j$. The standard Hermitian form of $\mathbb{C}^{n+1}$ restricts to a metric with
$$|\varepsilon_i|^2 = \frac{\|Z\|^2}{|Z_i|^2}.$$
A linear form $\ell$ on $\mathbb{C}^{n+1}$ restricts to every line $\mathbb{C} Z$, so it is a holomorphic section of the dual bundle $\mathcal{O}(-1)^*$. Let $e_i$ be the section given by $Z_i$; it satisfies $e_i(\varepsilon_i) = 1$, so it is the dual frame on $U_i$, and $e_j = (Z_j / Z_i) e_i$. These are the transition functions $g_{ij} = Z_j / Z_i$ of $\mathcal{O}(1)$ in Definition P6.2.16, and the section given by $\ell$ has components $\ell / Z_i$, which satisfy $\ell / Z_i = g_{ij} \cdot \ell / Z_j$; so $\mathcal{O}(-1)^* = \mathcal{O}(1)$ with $\ell$ the section of Proposition P6.2.17. The dual metric has $h_i = |e_i|^2 = 1 / |\varepsilon_i|^2$, so
$$h_i = \frac{|Z_i|^2}{\|Z\|^2}, \qquad |s|^2_h = \frac{|\ell(Z)|^2}{\|Z\|^2} \text{ for the section } s \text{ given by } \ell,$$
and indeed $h_j = |Z_j|^2 / \|Z\|^2 = |g_{ij}|^2 h_i$. On $\mathcal{O}(d) = \mathcal{O}(1)^{\otimes d}$, $d \geq 0$, the tensor product metric is $|s|^2 = |s(Z)|^2 / \|Z\|^{2d}$ for a homogeneous polynomial $s$ of degree $d$; both sides are invariant under $Z \mapsto \lambda Z$.

**Example P6.3.10 (a closed real $(1,1)$-form that is not positive).** Let $X = \mathbb{P}^1 \times \mathbb{P}^1$ with projections $p_1$, $p_2$ and $\alpha = p_1^* \omega_{FS} - p_2^* \omega_{FS}$. It is real, closed and of type $(1,1)$, since pullback by holomorphic maps preserves all three properties (Proposition P6.1.33). In the coordinates $(z, w)$ of $U_0 \times U_0$ its matrix is $\frac{1}{2\pi} \operatorname{diag}((1 + |z|^2)^{-2}, -(1 + |w|^2)^{-2})$, which is indefinite at every point. More is true: no positive closed form $\beta$ is cohomologous to $\alpha$. Indeed, if $\alpha - \beta = d\gamma$, then by Stokes $\int_{\{p\} \times \mathbb{P}^1} \beta = \int_{\{p\} \times \mathbb{P}^1} \alpha = -1$, while the restriction of a positive $(1,1)$-form to the complex curve $C = \{p\} \times \mathbb{P}^1$ is positive on $C$, since the condition $\beta(v, Jv) > 0$ of Proposition P6.3.4 restricts to the tangent vectors of $C$; in a local coordinate $w$ on $C$ it is a positive function times $\frac{i}{2} dw \wedge d\bar w = du \wedge dv$, so its integral is positive. Semipositivity is also weaker than positivity in a single point: $i \partial\bar\partial |z|^4 = 4 |z|^2\, i\, dz \wedge d\bar z$ on $\mathbb{C}$ is semipositive and vanishes at $0$.

### Proof

*Proof of Proposition P6.3.2.* 1. Let $g$ be compatible. Then $g(Jv, u) = g(J^2 v, Ju) = -g(v, Ju) = -g(Ju, v)$, so $\omega(v, u) = -\omega(u, v)$. Next $\omega(Ju, Jv) = g(J^2 u, Jv) = -g(u, Jv)$, and $g(u, Jv) = g(Ju, J^2 v) = -g(Ju, v)$, so $\omega(Ju, Jv) = \omega(u, v)$. Also $\omega(u, Jv) = g(Ju, Jv) = g(u, v)$. Put $h = g - i\omega$. It is real bilinear, and
$$h(Ju, v) = g(Ju, v) - i g(J^2 u, v) = g(Ju, v) + i g(u, v) = i (g(u, v) - i g(Ju, v)) = i h(u, v),$$
so $h$ is $\mathbb{C}$-linear in $u$. From $\omega(v, u) = -\omega(u, v)$ and the symmetry of $g$, $h(v, u) = g(u, v) + i\omega(u, v) = \overline{h(u, v)}$, and $h(v, v) = g(v, v) > 0$ for $v \neq 0$ since $\omega(v, v) = 0$. Conversely let $h$ be Hermitian and $g = \operatorname{Re} h$. It is symmetric since $h(v, u) = \overline{h(u, v)}$ has the same real part, positive definite since $h(v, v) > 0$ is real, and $J$-invariant since $h(Ju, Jv) = i \cdot \bar i\, h(u, v) = h(u, v)$. Also $-\operatorname{Im} h(u, v) = \operatorname{Re}(i h(u, v)) = \operatorname{Re} h(Ju, v) = g(Ju, v) = \omega(u, v)$, so $h = g - i\omega$, which also shows that $g$ is determined by $h$.

2. For $u, v \in \mathbb{C}^n$ regarded as real vectors, $dz_j(u) = u_j$ and $d\bar z_k(v) = \bar v_k$. Hence
$$\frac{i}{2} \sum_{j,k} h_{jk} (dz_j \wedge d\bar z_k)(u, v) = \frac{i}{2} \sum_{j,k} h_{jk} (u_j \bar v_k - v_j \bar u_k) = \frac{i}{2} (h(u, v) - h(v, u)) = \frac{i}{2} \cdot 2i \operatorname{Im} h(u, v) = -\operatorname{Im} h(u, v),$$
which is $\omega(u, v)$ by part 1. For $H = I$ the right side of the formula is $\omega_0$, and $g = \operatorname{Re} \sum u_j \bar v_j$ is the Euclidean inner product.

3. By Gram-Schmidt for $h$ there is a unitary basis $e_1, \dots, e_n$. The complex linear isomorphism $\mathbb{C}^n \to V$ it defines carries the standard Hermitian form to $h$, hence the Euclidean $g$ and $\omega_0$ to $g$ and $\omega$, and it preserves the complex orientation. For the standard structure, $\omega_0^n = (\sum_j dx_j \wedge dy_j)^n = n!\, dx_1 \wedge dy_1 \wedge \dots \wedge dx_n \wedge dy_n$, since the $2$-forms $dx_j \wedge dy_j$ commute and square to $0$, and this is $n!$ times the Euclidean volume form for the complex orientation. In the situation of part 2 write $\omega = \frac{i}{2} \sum h_{jk} dz_j \wedge d\bar z_k$. Expanding $\omega^n$, only terms with distinct $j$'s and distinct $k$'s survive, and reordering gives $\omega^n = n! \det(H) \prod_j (\frac{i}{2} dz_j \wedge d\bar z_j)$, the factors taken in the order $j = 1, \dots, n$; with $\frac{i}{2} dz_j \wedge d\bar z_j = dx_j \wedge dy_j$ this is the formula. $\square$

*Proof of Proposition P6.3.4.* 1. Conjugation gives $\bar\alpha = -i \sum \bar a_{jk}\, d\bar z_j \wedge dz_k = i \sum \bar a_{jk}\, dz_k \wedge d\bar z_j$, so $\bar\alpha = \alpha$ if and only if $a_{kj} = \bar a_{jk}$ for all $j, k$. For real $\varphi$, $i\partial\bar\partial \varphi = i \sum (\partial^2 \varphi / \partial z_j \partial \bar z_k)\, dz_j \wedge d\bar z_k$, and $\overline{\partial^2 \varphi / \partial z_j \partial \bar z_k} = \partial^2 \varphi / \partial \bar z_j \partial z_k$, which is the $(k, j)$ entry.

2. Since $dz_j(Jv) = i \xi_j$ and $d\bar z_k(Jv) = \overline{dz_k(Jv)} = -i \bar\xi_k$,
$$\alpha(v, Jv) = i \sum_{j,k} a_{jk} (dz_j(v) d\bar z_k(Jv) - dz_j(Jv) d\bar z_k(v)) = i \sum_{j,k} a_{jk} (-i \xi_j \bar\xi_k - i \xi_j \bar\xi_k) = 2 \sum_{j,k} a_{jk} \xi_j \bar\xi_k.$$

3. The map $v \mapsto \xi = (dz_j(v))$ is a real isomorphism $T_xX \to \mathbb{C}^n$, so the first two conditions are equivalent by part 2. If they hold, put $g(u, v) = \alpha(u, Jv)$. Since $\alpha$ is real and of type $(1,1)$, it is $J$-invariant: $(dz_j \wedge d\bar z_k)(Ju, Jv) = (i)(-i)(dz_j \wedge d\bar z_k)(u, v)$. Then $g(v, u) = \alpha(v, Ju) = \alpha(Jv, J^2 u) = -\alpha(Jv, u) = \alpha(u, Jv) = g(u, v)$, $g$ is $J$-invariant because $\alpha$ is, $g(v, v) = \alpha(v, Jv) > 0$, and $g(Ju, v) = \alpha(Ju, Jv) = \alpha(u, v)$, so $\alpha$ is the fundamental form of $g$. Conversely the fundamental form of a compatible $g$ has $\omega(v, Jv) = g(Jv, Jv) > 0$. If $A$ is positive definite, the matrix $\bar A = A^T$ is also positive definite, so $\bar A = P^* P$ with $P$ invertible (Cholesky), and $A = P^T \bar P$; then with $\theta_l = \sum_j p_{lj} dz_j$, $i \sum_l \theta_l \wedge \bar\theta_l = i \sum_{j,k} (\sum_l p_{lj} \bar p_{lk})\, dz_j \wedge d\bar z_k = i \sum a_{jk}\, dz_j \wedge d\bar z_k$. Conversely, $i \sum \theta_l \wedge \bar\theta_l$ with $\theta_l = \sum_j p_{lj} dz_j$, $P$ invertible, has matrix $P^T \bar P$, which is positive definite since $\xi^T P^T \bar P \bar\xi = |P\xi|^2$.

4. If $z_j = z_j(w)$ is a holomorphic change of coordinates with $dz_j = \sum_l q_{jl}\, dw_l$ and $Q = (q_{jl})$ invertible at $x$, the matrix of $\alpha$ in the coordinates $w$ is $Q^T A \bar Q$, and $\eta^T Q^T A \bar Q \bar\eta = (Q\eta)^T A \overline{(Q\eta)}$, so positivity is preserved. The second condition of part 3 is preserved by positive linear combinations and is open, since the unit sphere of $T_xX$ is compact. $\square$

*Proof of Proposition P6.3.6.* 1. Let $\{U_a\}$ be a cover of $X$ by open sets over which $E$ has frames $e^{(a)}_1, \dots, e^{(a)}_r$, and let $h^{(a)}$ be the metric on $E|_{U_a}$ in which that frame is unitary. Since $X$ is Hausdorff and second countable, there is a smooth partition of unity $\{\rho_a\}$ subordinate to the cover. Put $h = \sum_a \rho_a h^{(a)}$. In any local frame the matrix of $h$ is a locally finite sum of smooth positive semidefinite matrices, positive definite at each point because some $\rho_a$ is positive there; so $h$ is a Hermitian metric. The same argument shows that a convex combination of metrics is a metric. For a complex manifold apply this to $T^{1,0} X$.

2. Put $h_{E^*}(\lambda, \mu) = h_E(v_\mu, v_\lambda)$, where $v_\lambda \in E_x$ is the vector with $\lambda = h_E(\cdot, v_\lambda)$; $h_{E \oplus F} = h_E + h_F$ on the two summands, orthogonal to each other; $h_{E \otimes F}(u \otimes v, u' \otimes v') = h_E(u, u') h_F(v, v')$; $h_{\Lambda^k E}(u_1 \wedge \dots \wedge u_k, u'_1 \wedge \dots \wedge u'_k) = \det(h_E(u_a, u'_b))$; and $(f^*h)_y = h_{f(y)}$. In local frames unitary at a point, each is the standard form in the induced frame at that point, hence positive definite, and its matrices in smooth frames are smooth. The restriction of $h$ to $S$ is a metric. The orthogonal complement $S^\perp_x$ of $S_x$ has constant rank $r - \operatorname{rk} S$, and it is a smooth subbundle: if $s_1, \dots, s_m$ is a local frame of $S$ completed to a frame of $E$, Gram-Schmidt for $h$ produces a smooth frame whose last $r - m$ vectors span $S^\perp$. The composite $S^\perp \to E \to E/S$ is an isomorphism on every fibre, and transporting $h|_{S^\perp}$ gives the quotient metric.

3. By Proposition P6.3.2 applied in each tangent space, $\omega$ determines $g$ by $g(u, v) = \omega(u, Jv)$ and hence $h$; by Proposition P6.3.4, part 3, a real $(1,1)$-form that is positive at every point is the fundamental form of a compatible $g$, which is smooth when $\omega$ is. The coordinate formula of Definition P6.3.5 is part 2 of Proposition P6.3.2 in the basis $\partial/\partial z_j$ of $T^{1,0}_x X$, whose dual basis is $dz_j$. $\square$

### Exercises

1. (A) Compute the Fubini-Study form on $\mathbb{P}^1$ in the chart $U_1$ with coordinate $w = Z_0 / Z_1$, and check that it agrees with the formula of Example P6.3.8 under $w = 1/z$.
2. (A) Show that the fundamental form of the metric $h = \sum h_{jk}\, dz_j \otimes d\bar z_k$ on $\mathbb{C}^n$ satisfies $\omega(\partial/\partial x_j, \partial/\partial y_j) = h_{jj}$, and that $\omega_0(\partial/\partial x_j, \partial/\partial y_k) = \delta_{jk}$.
3. (B) Show that a real $(1,1)$-form $\alpha$ is semipositive if and only if $\alpha \wedge \beta_1 \wedge \dots \wedge \beta_{n-1} \geq 0$ for all positive $(1,1)$-forms of the form $\beta_l = i \theta_l \wedge \bar\theta_l$, where $\geq 0$ means a nonnegative multiple of the volume form.
4. (B) Show that the Fubini-Study metric is invariant under $U(n+1)$ and that $U(n+1)$ acts transitively on $\mathbb{P}^n$; deduce positivity of $\omega_{FS}$ from its value $\frac{i}{2\pi} \sum dz_j \wedge d\bar z_j$ at $[1 : 0 : \dots : 0]$.
5. (B) Let $X = \mathbb{C}^n / \Lambda$ be a torus. Show that a closed real $(1,1)$-form with constant coefficients is cohomologous to no other form with constant coefficients, using the de Rham cohomology of tori in Theorem P6.2.29.
6. (C) Let $\omega$ be a closed positive $(1,1)$-form on a compact complex manifold $X$ of dimension $n \geq 1$. Show that $\int_X \omega^n > 0$ and deduce from Stokes that $[\omega]^k \neq 0$ in $H^{2k}(X, \mathbb{R})$ for $0 \leq k \leq n$. Conclude that the Hopf surface of Example P6.2.4, which has $b_2 = 0$, has Hermitian metrics but none with closed fundamental form.

### Lean

Mathlib has inner product spaces over $\mathbb{C}$, positive definite Hermitian matrices, smooth manifolds and smooth vector bundles over them. It has no Hermitian metrics on bundles over complex manifolds, no positive $(1,1)$-forms and no Fubini-Study form. The handbook adds no `MinimalModel` node here.

### Notes and history

The metric of projective space was introduced by Fubini in 1904 and Study in 1905, as the metric invariant under the unitary group. Hermitian metrics on complex manifolds, and the description of a metric by its fundamental form, go back to Kähler (Kah33), who singled out the metrics with closed fundamental form; these are the subject of Chapter 4. The linear algebra of this section is Huybrechts, Section 1.2 (Huy05), and Voisin, Chapter 3 (Voi02); Griffiths and Harris, Section 0.2 (GH78), use the same normalization $\omega = \frac{i}{2} \sum h_{jk}\, dz_j \wedge d\bar z_k$. The normalization of $\omega_{FS}$ with the factor $\frac{1}{2\pi}$, chosen so that a line has area $1$, is the one that makes $\omega_{FS}$ represent the integral class $c_1(\mathcal{O}(1))$ in Section 3.3; many texts use $\frac{i}{2} \partial\bar\partial \log \|Z\|^2$ instead, for which a line has area $\pi$.
