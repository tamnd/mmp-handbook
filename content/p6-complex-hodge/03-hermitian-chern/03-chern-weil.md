---
title: Chern classes by Chern-Weil theory
nodes: []
sources: [Huy05, GH78, Wel80, BT82, Che46, Voi02]
reads_with: [Huy05:4.4, GH78:1.1, Wel80:III, BT82:IV]
requires: [P2.3, P2.7, P6.1, P6.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Chern classes by Chern-Weil theory

### Statement

Let $E$ be a smooth complex vector bundle of rank $r$ on a smooth manifold $X$, Hausdorff and second countable, with the matrix conventions of Section 3.2. The even forms $A^{\mathrm{ev}}(U) = \bigoplus_k A^{2k}(U)$ form a commutative $\mathbb{C}$-algebra, and they commute with forms of odd degree. De Rham cohomology is $H^k_{dR}(X, \mathbb{C})$ of Definition P6.2.22, and $H^k_{dR}(X, \mathbb{R}) \subseteq H^k_{dR}(X, \mathbb{C})$ is the subspace of classes of real forms.

**Definition P6.3.22 (invariant polynomials).** An *invariant polynomial* of degree $k$ on $\mathfrak{gl}_r(\mathbb{C})$ is a homogeneous polynomial function $P$ of degree $k$ in the entries $a_{jl}$ of $A \in M_r(\mathbb{C})$ with $P(g A g^{-1}) = P(A)$ for all $g \in \mathrm{GL}_r(\mathbb{C})$. For a commutative $\mathbb{C}$-algebra $R$ and $A \in M_r(R)$, $P(A) \in R$ is defined by substituting the entries; in particular $P(F) \in A^{2k}(U)$ for a matrix $F$ of $2$-forms. The *elementary invariant polynomials* $\sigma_k$ are defined by $\det(I + tA) = \sum_{k=0}^r \sigma_k(A) t^k$; thus $\sigma_1 = \operatorname{tr}$ and $\sigma_r = \det$. For $A \in M_r(R)$ and $B \in M_r(R')$ with $R'$ an $R$-module, $P'(A)(B) = \sum_{j,l} (\partial P / \partial a_{jl})(A)\, B_{jl}$ is the derivative of $P$ at $A$ in the direction $B$.

**Theorem P6.3.23 (Chern-Weil).** Let $P$ be an invariant polynomial of degree $k$.

1. For a connection $\nabla$ on $E$ with curvature matrices $F$ in local frames, the local forms $P(F)$ glue to a global form $P(F_\nabla) \in A^{2k}(X)$, and $d P(F_\nabla) = 0$.
2. For two connections $\nabla_0$, $\nabla_1$, put $\eta = \nabla_1 - \nabla_0$, $\nabla_t = \nabla_0 + t\eta$ with curvature $F_t$, and $T = \int_0^1 P'(F_t)(\eta)\, dt \in A^{2k-1}(X)$. Then $P(F_{\nabla_1}) - P(F_{\nabla_0}) = dT$. So the class $[P(F_\nabla)] \in H^{2k}_{dR}(X, \mathbb{C})$ does not depend on $\nabla$.
3. For a smooth map $f: Y \to X$, $P(F_{f^*\nabla}) = f^* P(F_\nabla)$.

Lean: not yet in Lean.

**Definition P6.3.24 (Chern forms and Chern classes).** For a connection $\nabla$ on $E$ the *total Chern form* is
$$c(E, \nabla) = \det\Big(I + \frac{i}{2\pi} F_\nabla\Big) = \sum_{k=0}^r c_k(E, \nabla), \qquad c_k(E, \nabla) = \sigma_k\Big(\frac{i}{2\pi} F_\nabla\Big) \in A^{2k}(X),$$
and the *Chern classes* are $c_k(E) = [c_k(E, \nabla)]$, which by Theorem P6.3.23 do not depend on $\nabla$; the *total Chern class* is $c(E) = \sum_k c_k(E)$. For a holomorphic bundle with a Hermitian metric $h$, $c_k(E, h)$ denotes the Chern form of the Chern connection; it has type $(k, k)$ by Theorem P6.3.16, and for a line bundle $c_1(L, h)$ is the form of Corollary P6.3.17.

**Proposition P6.3.25 (properties of Chern classes).** Let $E$, $E'$ be smooth complex vector bundles on $X$.

1. (Reality) $c_k(E, \nabla)$ is a real form for every metric connection $\nabla$, metric connections exist, and so $c_k(E) \in H^{2k}_{dR}(X, \mathbb{R})$. Also $c_0(E) = 1$, and $c_k(E) = 0$ for $k > r$.
2. (Naturality) Isomorphic bundles have the same Chern classes, and $c_k(f^* E) = f^* c_k(E)$ for a smooth map $f: Y \to X$.
3. (Whitney formula) $c(E \oplus E') = c(E)\, c(E')$. If $0 \to S \to E \to Q \to 0$ is an exact sequence of smooth complex bundles, for example of holomorphic bundles, then $c(E) = c(S)\, c(Q)$.
4. (Determinant) $c_1(E) = c_1(\det E) = [\frac{i}{2\pi} \operatorname{tr} F_\nabla]$.
5. (Dual) $c_k(E^*) = (-1)^k c_k(E)$.
6. (Twisting) For a line bundle $L$, $c(E \otimes L) = \sum_{j=0}^r c_j(E) (1 + c_1(L))^{r-j}$; in particular $c_1(E \otimes L) = c_1(E) + r\, c_1(L)$.
7. (Trivial bundles) If $E$ has a flat connection, for example if $E = X \times \mathbb{C}^r$, then $c(E) = 1$.

Lean: not yet in Lean.

**Definition P6.3.26 (the integral first Chern class).** Let $X$ be a complex manifold and $L$ a holomorphic line bundle with class $[L] \in H^1(X, \mathcal{O}_X^*)$ (Theorem P6.2.15, with the convention of Theorem P2.7.28). Let $\delta: H^1(X, \mathcal{O}_X^*) \to H^2(X, \mathbb{Z})$ be the connecting map of the exponential sequence $0 \to \mathbb{Z} \to \mathcal{O}_X \xrightarrow{\exp(2\pi i \cdot)} \mathcal{O}_X^* \to 0$ of Example P2.7.6. The *first Chern class* of $L$ is
$$c_1(L) = -\delta([L]) \in H^2(X, \mathbb{Z}).$$
The sign is the one that makes $c_1(\mathcal{O}(1))$ positive, in the sense of Example P6.3.29. Example P2.7.32 writes $c_1$ for $\delta$ itself, which differs from this definition by the sign; the two agree up to sign, the image is the same subgroup $\mathrm{NS}(X)$, and from now on $c_1$ always means $-\delta$.

**Theorem P6.3.27 (the integral class and the Chern-Weil class).** Let $L$ be a holomorphic line bundle on a complex manifold $X$ and $\nabla$ a connection on $L$, for example the Chern connection of a Hermitian metric $h$. Under $H^2(X, \mathbb{Z}) \to H^2(X, \mathbb{C}) \cong H^2_{dR}(X, \mathbb{C})$, induced by $\mathbb{Z} \subset \mathbb{C}$ and the de Rham isomorphism of Theorem P6.2.25, the integral class $c_1(L)$ maps to the Chern-Weil class $[\frac{i}{2\pi} F_\nabla]$. In particular $[c_1(L, h)]$ is the image of an integral class, and it depends only on the isomorphism class of $L$.

Lean: not yet in Lean.

**Theorem P6.3.28 (degree on a compact Riemann surface).** Let $X$ be a compact connected Riemann surface, oriented by its complex structure, $L$ a holomorphic line bundle on $X$ and $s$ a meromorphic section of $L$ that is not identically zero. Then
$$\int_X c_1(L) = \sum_{p \in X} \operatorname{ord}_p(s),$$
where $\int_X c_1(L)$ is the integral of any closed form representing the image of $c_1(L)$ in $H^2_{dR}(X, \mathbb{R})$. This integer is the *degree* $\deg L$; in particular the number of zeros minus the number of poles of $s$, counted with multiplicity, does not depend on $s$.

Lean: not yet in Lean.

Here a meromorphic section is given in each holomorphic frame $e_i$ by $s = f_i e_i$ with $f_i$ meromorphic, and $\operatorname{ord}_p(s) = \operatorname{ord}_p(f_i)$ does not depend on $i$ because $f_i = g_{ij} f_j$ with $g_{ij}$ nowhere zero. Since $X$ is connected and compact and $s \not\equiv 0$, the zeros and poles of $s$ are finite in number and the sum is finite. The integral $\int_X$ on $H^2_{dR}(X, \mathbb{R})$ is well defined by Stokes, since $\int_X d\gamma = 0$ on a compact manifold without boundary.

### Proof in words

In a frame where the connection matrix vanishes at a point, the Bianchi identity says that $dF$ vanishes at that point, so every polynomial in the entries of $F$ is closed there; invariance makes the polynomial independent of the frame, so it is closed everywhere. Moving the connection along a segment changes $F$ by the covariant derivative of $\eta$, and the same trick at a point shows that the change of $P(F)$ is exact. The properties of Chern classes then follow from the behaviour of curvature under operations on bundles, and the Whitney formula for exact sequences reduces to direct sums because Chern classes do not see holomorphic structure. For the integral class, the logarithmic derivative maps the exponential sequence to the sequence $0 \to \mathbb{C} \to \mathcal{A}^0 \to \mathcal{Z}^1 \to 0$ of closed $1$-forms; along this map the cocycle $g_{ij}$ of $L$ becomes the cocycle $\frac{1}{2\pi i} d \log g_{ij}$, and the connection forms $\frac{i}{2\pi}\theta_i$ are local primitives of $\frac{i}{2\pi} F$ whose differences are $-\frac{1}{2\pi i} d\log g_{ij}$. Chasing these through the connecting maps gives $-\delta[L] = [\frac{i}{2\pi} F]$. On a Riemann surface, $\frac{i}{2\pi} F = -\frac{i}{2\pi}\partial\bar\partial \log |s|^2_h$ away from the zeros and poles of $s$ is exact, and Stokes turns its integral into residues of $d\log$ of the local components of $s$.

### Examples

**Example P6.3.29 (projective space).** On $\mathbb{P}^n$, Example P6.3.19 and Theorem P6.3.27 give that $c_1(\mathcal{O}(d))$ maps to $d[\omega_{FS}]$ for every $d \in \mathbb{Z}$; write $h = [\omega_{FS}] \in H^2_{dR}(\mathbb{P}^n, \mathbb{R})$. In the chart $U_0$ the matrix of $\omega_{FS} = i \sum a_{jk}\, dz_j \wedge d\bar z_k$ is $A = \frac{1}{2\pi}((1 + |z|^2) I - \bar z z^T)/(1 + |z|^2)^2$ by Example P6.3.8, where $(\bar z z^T)_{jk} = \bar z_j z_k$. The rank one matrix $\bar z z^T$ has the eigenvalue $|z|^2$ once and $0$ otherwise, so $\det((1 + |z|^2) I - \bar z z^T) = (1 + |z|^2)^{n-1}$ and $\det A = (2\pi)^{-n} (1 + |z|^2)^{-n-1}$. By Proposition P6.3.2, applied to $\omega_{FS} = \frac{i}{2} \sum 2 a_{jk}\, dz_j \wedge d\bar z_k$,
$$\omega_{FS}^n = n! \det(2A)\, dV = \frac{n!}{\pi^n} \frac{dV}{(1 + |z|^2)^{n+1}},$$
with $dV$ the Lebesgue measure. In polar coordinates, with the area $2\pi^n / (n-1)!$ of the unit sphere $S^{2n-1}$ and $u = \rho^2$,
$$\int_{\mathbb{C}^n} \frac{dV}{(1 + |z|^2)^{n+1}} = \frac{2\pi^n}{(n-1)!} \int_0^\infty \frac{\rho^{2n-1}\, d\rho}{(1 + \rho^2)^{n+1}} = \frac{\pi^n}{(n-1)!} \int_0^\infty \frac{u^{n-1}\, du}{(1 + u)^{n+1}} = \frac{\pi^n}{(n-1)!} \cdot \frac{1}{n} = \frac{\pi^n}{n!},$$
using $\int_0^\infty u^{n-1} (1 + u)^{-n-1} du = B(n, 1) = 1/n$. The complement of $U_0$ has measure zero, so $\int_{\mathbb{P}^n} \omega_{FS}^n = 1$ and $\int_{\mathbb{P}^n} c_1(\mathcal{O}(d))^n = d^n$. Since $b_{2k}(\mathbb{P}^n) = 1$ for $0 \leq k \leq n$ (Example P6.2.31) and $h^k \neq 0$ because $h^n \neq 0$, $H^{2k}_{dR}(\mathbb{P}^n, \mathbb{R}) = \mathbb{R} h^k$. For $n = 1$ and $d \geq 0$ this agrees with Theorem P6.3.28: the section $Z_0^d$ has component $(Z_0 / Z_1)^d = w^d$ in the frame $e_1^d$, so it has one zero, of order $d$, at $[0 : 1]$. For $d < 0$, the meromorphic section $Z_0^d$ has one pole of order $-d$.

**Example P6.3.30 (the tangent bundle of projective space).** The Euler sequence $0 \to \mathcal{O} \to \mathcal{O}(1)^{\oplus(n+1)} \to T_{\mathbb{P}^n} \to 0$ of Proposition P6.2.18 and the Whitney formula give $c(T_{\mathbb{P}^n}) \cdot c(\mathcal{O}) = c(\mathcal{O}(1))^{n+1}$, so with $h = c_1(\mathcal{O}(1))$ as in Example P6.3.29,
$$c(T_{\mathbb{P}^n}) = (1 + h)^{n+1}, \qquad c_k(T_{\mathbb{P}^n}) = \binom{n+1}{k} h^k, \qquad \int_{\mathbb{P}^n} c_n(T_{\mathbb{P}^n}) = n + 1.$$
The number $n + 1$ is the Euler characteristic $\sum_k (-1)^k b_k$ of $\mathbb{P}^n$ by Example P6.2.31, as the Gauss-Bonnet theorem $\int_X c_n(T_X) = \chi_{\mathrm{top}}(X)$ predicts (Bott and Tu, Chapter IV (BT82), cited as a black box). The first Chern class is $c_1(T_{\mathbb{P}^n}) = (n+1) h$, consistent with $K_{\mathbb{P}^n} = \det T^*_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$ of Proposition P6.2.18 and parts 4 and 5 of Proposition P6.3.25. For $n = 1$ the holomorphic vector field $\partial/\partial z$ on $U_0$ is $-w^2\, \partial/\partial w$ in the coordinate $w = 1/z$, so it has one zero, of order $2$, at $\infty$; Theorem P6.3.28 gives $\deg T_{\mathbb{P}^1} = 2$, in accordance with $c_1 = 2h$.

**Example P6.3.31 (plane curves and tori).** Let $C \subset \mathbb{P}^2$ be a smooth curve of degree $d \geq 1$, the zero set of a homogeneous polynomial $F$ of degree $d$ as in Proposition P6.2.6. Since $C \neq \mathbb{P}^2$ there is a point $q \notin C$, and among the lines through $q$, of which there are infinitely many, at most $d$ are contained in $C$, since the linear form of such a line divides $F$. The unitary group acts transitively on pairs of a point and a line through it and preserves $\omega_{FS}$, so after a unitary change of coordinates $q = [0 : 0 : 1]$ and the line $\ell = \{Z_0 = 0\}$ is not contained in $C$. Then $g(t) = F(0, 1, t)$ has degree exactly $d$, because the coefficient of $t^d$ is $F(0, 0, 1) \neq 0$; let $t_m$ be its roots, with multiplicities $\mu_m$, $\sum_m \mu_m = d$. The points of $C \cap \ell$ are the $[0 : 1 : t_m]$. In the chart $Z_1 = 1$ with coordinates $x = Z_0 / Z_1$, $y = Z_2 / Z_1$, the curve is $f(x, y) = F(x, 1, y) = 0$ and the section $Z_0$ of $\mathcal{O}(1)$ has component $x$ in the frame $e_1$. Write $f = x\, a(x, y) + g(y)$ and let $p = (0, t_m)$. If $a(p) = \partial f / \partial x(p) \neq 0$, then near $p$ the curve is a graph $x = \psi(y)$, $y$ is a local coordinate on $C$, and $\psi = -g / a(\psi, y)$ vanishes to order $\mu_m$ at $t_m$. If $a(p) = 0$, smoothness gives $g'(t_m) = \partial f / \partial y(p) \neq 0$, so $\mu_m = 1$, the curve is a graph $y = \phi(x)$, and $x|_C$ vanishes to order $1$. So the section $Z_0|_C$ of $\mathcal{O}_C(1)$ has zeros of total order $d$, and Theorem P6.3.28 on each connected component of $C$, with naturality (Proposition P6.3.25), gives
$$\int_C \omega_{FS}|_C = \deg \mathcal{O}_C(1) = d, \qquad \int_C c_1(K_C) = (d - 3)\, d,$$
since $K_C \cong \mathcal{O}_C(d - 3)$ by Example P6.2.20. For $d = 1, 2, 3, 4$ this is $-2, -2, 0, 4$. For a cubic, $\deg K_C = 0$; for a conic, $C \cong \mathbb{P}^1$ and $\deg K_C = -2 = -\deg T_{\mathbb{P}^1}$ as in Example P6.3.30. With the Gauss-Bonnet theorem (BT82, Chapter IV) and $\deg T_C = -\deg K_C$, this gives $\chi_{\mathrm{top}}(C) = d(3 - d)$, the classical genus formula $g = (d-1)(d-2)/2$ for connected $C$. For a complex torus $X = \mathbb{C}^n / \Lambda$ the tangent bundle is holomorphically trivial with the holomorphic frame $\partial/\partial z_j$ (Example P6.2.14). For the flat metric of Example P6.3.7 the matrix $H$ is constant, so $\theta = H^{-1}\partial H = 0$, $F = 0$ and $c(T_X, h) = 1$ as a form, not only as a class. In particular $\int_X c_n(T_X) = 0$, which is $\chi_{\mathrm{top}}(X) = \sum_k (-1)^k \binom{2n}{k} = 0$ by Theorem P6.2.29.

**Example P6.3.32 (a polynomial that is not invariant).** Let $P(A) = a_{11}$ on $\mathfrak{gl}_2(\mathbb{C})$, which is not invariant: it is not preserved by the permutation matrix that swaps the two basis vectors. On the trivial bundle $E = \mathbb{P}^1 \times \mathbb{C}^2$ with its global frame, $P(F)$ is a global form for every connection, but its class depends on the connection. Let $\rho$ be a smooth function with compact support in $U_0$, not identically zero, $\alpha = \rho\, dz$, and $\nabla = d + \theta$ with
$$\theta = \begin{pmatrix} 0 & \alpha \\ \bar\alpha & 0 \end{pmatrix}, \qquad F = d\theta + \theta \wedge \theta = \begin{pmatrix} \alpha \wedge \bar\alpha & d\alpha \\ d\bar\alpha & \bar\alpha \wedge \alpha \end{pmatrix}.$$
Then $P(F) = \alpha \wedge \bar\alpha = |\rho|^2 dz \wedge d\bar z = -2i |\rho|^2 dx \wedge dy$, and $\int_{\mathbb{P}^1} P(F) = -2i \int |\rho|^2 dx\, dy \neq 0$, while for the trivial connection $d$, $P(F) = 0$. Forms with different integrals on a compact surface are not cohomologous, so the conclusion of Theorem P6.3.23 fails for $P$. For the invariant polynomial $\operatorname{tr}$ the same connection gives $\operatorname{tr} F = \alpha \wedge \bar\alpha + \bar\alpha \wedge \alpha = 0$, and for $\det$ it gives $(\alpha \wedge \bar\alpha) \wedge (\bar\alpha \wedge \alpha) - d\alpha \wedge d\bar\alpha = 0$, since all are $4$-forms on a surface. The global frame also hides the second defect: on $E = \mathcal{O} \oplus \mathcal{O}(1)$ with the direct sum of the trivial metric and that of Example P6.3.9, $P(F) = 0$ in the frame $(1, e_i)$ and $P(F) = F_{\mathcal{O}(1)}$ in the frame $(e_i, 1)$, so $P(F)$ is not even a well-defined form.

### Proof

*Proof of Theorem P6.3.23.* The identity $P(g A g^{-1}) = P(A)$ holds for all complex matrices $A$ and invertible $g$, so it is an identity of polynomials in the entries of $A$, the entries of $g$ and $\det(g)^{-1}$, and therefore it holds for matrices over any commutative $\mathbb{C}$-algebra. Differentiating in $A$ gives $P'(g A g^{-1})(g B g^{-1}) = P'(A)(B)$ for $B$ over the same algebra, and hence for $B$ a matrix of $1$-forms, since such a $B$ is locally $\sum_a dx_a B_a$ with $B_a$ matrices of functions and the expression is linear in $B$.

1. By Proposition P6.3.14, $F' = g^{-1} F g$ under a change of frame, so the local forms $P(F)$ agree on overlaps. To show $dP(F) = 0$ at a point $x_0$, choose a frame with $\theta(x_0) = 0$: if $\theta(x_0) = \sum_a \Gamma_a\, dx_a$ in local coordinates $x_a$ centred at $x_0$, the frame $e' = e g$ with $g = I - \sum_a \Gamma_a x_a$, invertible near $x_0$, has $\theta'(x_0) = dg(x_0) + \theta(x_0) = 0$ by Proposition P6.3.12. Since even forms commute with all forms, $d P(F) = \sum_{j,l} (\partial P / \partial a_{jl})(F)\, dF_{jl} = P'(F)(dF)$, and $dF(x_0) = (F \wedge \theta - \theta \wedge F)(x_0) = 0$ by the Bianchi identity. So $dP(F)(x_0) = 0$.

2. $\eta$ is a section of $\mathcal{A}^1(\operatorname{End} E)$ by Proposition P6.3.12, with matrix $\eta$ in a frame, and $\nabla_t$ has matrix $\theta_t = \theta_0 + t\eta$. Then $\frac{d}{dt} F_t = d\eta + \theta_t \wedge \eta + \eta \wedge \theta_t$ and $\frac{d}{dt} P(F_t) = P'(F_t)(d\eta + \theta_t \wedge \eta + \eta \wedge \theta_t)$. The form $T_t = P'(F_t)(\eta)$ is global, because both $F_t$ and $\eta$ change by conjugation under a change of frame. Fix $t$ and $x_0$ and choose a frame with $\theta_t(x_0) = 0$. At $x_0$, $dF_t = 0$ by the Bianchi identity, so
$$d T_t(x_0) = \sum_{j,l} d\big((\partial P/\partial a_{jl})(F_t)\big) \wedge \eta_{jl} + P'(F_t)(d\eta) = P'(F_t)(d\eta) = \frac{d}{dt} P(F_t)(x_0),$$
the first sum vanishing because $d$ of a polynomial in the entries of $F_t$ is a combination of the entries of $dF_t$. Both sides are global forms, so $\frac{d}{dt} P(F_t) = dT_t$ everywhere. Integrating in $t$, and using that $d$ commutes with $\int_0^1 dt$ for a smooth family of forms, $P(F_1) - P(F_0) = d \int_0^1 T_t\, dt$.

3. The pulled back connection has matrix $f^*\theta$ in the pulled back frame, so curvature $d f^*\theta + f^*\theta \wedge f^*\theta = f^* F$, and $P(f^* F) = f^* P(F)$. $\square$

*Proof of Proposition P6.3.25.* 1. Cover $X$ by open sets with unitary frames, which exist by Gram-Schmidt. The connection $d$ in a unitary frame is metric, and since compatibility with $h$ is preserved by convex combinations, Proposition P6.3.12 glues these into a metric connection. For a metric connection the matrix $A = \frac{i}{2\pi} F$ in a unitary frame satisfies $A^* = A$ by Theorem P6.3.16, part 3, whose proof uses only metric compatibility; that is, $\bar A = A^T$. Hence $\overline{\det(I + tA)} = \det(I + t\bar A) = \det(I + tA^T) = \det(I + tA)$ for real $t$, and each $c_k(E, \nabla)$ is real. Since $\det(I + tA)$ has degree at most $r$ in $t$, $c_k = 0$ for $k > r$, and $c_0 = 1$.

2. An isomorphism $\phi: E' \to E$ carries a connection $\nabla$ on $E$ to $\phi^{-1} \circ \nabla \circ \phi$ on $E'$, whose matrix in the frame $\phi^{-1}(e)$ is $\theta$, so the Chern forms agree. Naturality is part 3 of Theorem P6.3.23.

3. The direct sum connection has block diagonal curvature $\operatorname{diag}(F, F')$, and $\det$ of a block diagonal matrix is the product. For an exact sequence, choose a Hermitian metric on $E$; by Proposition P6.3.6, $S^\perp \to Q$ is an isomorphism of smooth bundles and $E = S \oplus S^\perp$, so $E \cong S \oplus Q$ as smooth complex bundles, and the claim follows from parts 2 and the direct sum case. A holomorphic exact sequence is in particular an exact sequence of smooth bundles.

4. The induced connection on $\det E$ has matrix $\operatorname{tr}\theta$ by Proposition P6.3.12, so curvature $d \operatorname{tr}\theta = \operatorname{tr} d\theta = \operatorname{tr}(F - \theta\wedge\theta) = \operatorname{tr} F$, because $\operatorname{tr}(\theta \wedge \theta) = \sum_{j,l} \theta_{jl} \wedge \theta_{lj} = -\sum_{j,l} \theta_{lj} \wedge \theta_{jl} = -\operatorname{tr}(\theta\wedge\theta)$. Both $c_1(E, \nabla)$ and $c_1(\det E)$ are therefore $\frac{i}{2\pi} \operatorname{tr} F$.

5. The dual connection has matrix $-\theta^T$, and $(\theta\wedge\theta)^T = -\theta^T \wedge \theta^T$, so $F_{E^*} = -d\theta^T + \theta^T \wedge \theta^T = -F^T$. With commuting entries $\det(I - tA^T) = \det(I - tA)$, so $c_k(E^*, \nabla^*) = \sigma_k(-A) = (-1)^k \sigma_k(A)$.

6. In the frame $e \otimes e_L$ the tensor connection has matrix $\theta + \lambda I$, where $\lambda$ is the connection form of $L$. Since $(\lambda I) \wedge \theta + \theta \wedge (\lambda I) = 0$, $\lambda$ being a $1$-form, and $\lambda \wedge \lambda = 0$, the curvature is $F + d\lambda\, I = F + F_L I$. With $A = \frac{i}{2\pi} F$ and the central even form $\mu = \frac{i}{2\pi} F_L$,
$$\det((1 + \mu) I + A) = \sum_{j=0}^r \sigma_j(A) (1 + \mu)^{r-j},$$
as one sees by expanding $\det(sI + A) = \sum_j \sigma_j(A) s^{r-j}$, a polynomial identity.

7. A flat connection has $F = 0$, so $c(E, \nabla) = 1$; the trivial bundle has the flat connection $d$ in its global frame. $\square$

*Proof of Theorem P6.3.27.* Let $\{U_i\}$ be an open cover with holomorphic frames $e_i$ and transition functions $g_{ij}$, $e_j = g_{ij} e_i$, so that $[L]$ is the image of the Čech cocycle $(g_{ij})$ (Theorem P2.7.28). Write $\nabla e_i = \theta_i e_i$. Then $\nabla e_j = dg_{ij}\, e_i + g_{ij} \theta_i e_i$, so
$$\theta_j = \theta_i + d\log g_{ij} \quad \text{on } U_i \cap U_j, \qquad d \log g_{ij} = dg_{ij} / g_{ij},$$
and $F = d\theta_i$ on $U_i$. Put $\Theta = \frac{i}{2\pi} F$ and $a_i = \frac{i}{2\pi} \theta_i$. Then $da_i = \Theta$ and $a_j - a_i = \frac{i}{2\pi} d\log g_{ij} = -\frac{1}{2\pi i} d\log g_{ij}$.

Let $\mathcal{Z}^k$ be the sheaf of closed complex $k$-forms. By the Poincaré lemma (Theorem P6.1.34) the sequences $0 \to \mathbb{C} \to \mathcal{A}^0 \xrightarrow{d} \mathcal{Z}^1 \to 0$ and $0 \to \mathcal{Z}^1 \to \mathcal{A}^1 \xrightarrow{d} \mathcal{Z}^2 \to 0$ are exact, with connecting maps $\delta_1: H^1(X, \mathcal{Z}^1) \to H^2(X, \mathbb{C})$ and $\delta_2: H^0(X, \mathcal{Z}^2) \to H^1(X, \mathcal{Z}^1)$. Since the $\mathcal{A}^k$ are acyclic (Lemma P6.2.23), $\delta_1$ is an isomorphism and $\delta_2$ is surjective with kernel $d A^1(X)$. The de Rham isomorphism of Theorem P6.2.25 in degree $2$ is the isomorphism of Theorem P2.3.25 for the acyclic resolution $\mathbb{C} \to \mathcal{A}^\bullet$, which by dimension shifting along these two sequences is
$$H^2_{dR}(X, \mathbb{C}) = H^0(X, \mathcal{Z}^2) / dA^1(X) \xrightarrow{\ \delta_2\ } H^1(X, \mathcal{Z}^1) \xrightarrow{\ \delta_1\ } H^2(X, \mathbb{C}).$$

The diagram
$$\begin{array}{ccccccccc} 0 & \to & \mathbb{Z} & \to & \mathcal{O}_X & \xrightarrow{\exp(2\pi i \cdot)} & \mathcal{O}_X^* & \to & 0 \\ & & \downarrow & & \downarrow & & \downarrow & & \\ 0 & \to & \mathbb{C} & \to & \mathcal{A}^0 & \xrightarrow{d} & \mathcal{Z}^1 & \to & 0 \end{array}$$
with vertical maps the inclusion $\mathbb{Z} \subset \mathbb{C}$, the inclusion $f \mapsto f$, and $\lambda(u) = \frac{1}{2\pi i} du / u$, commutes: the left square trivially, and the right square because $\frac{1}{2\pi i} d(e^{2\pi i f}) / e^{2\pi i f} = df$. By naturality of connecting maps (Theorem P2.3.15), the image of $\delta[L]$ in $H^2(X, \mathbb{C})$ is $\delta_1(\lambda_*[L])$, where $\lambda_*[L] \in H^1(X, \mathcal{Z}^1)$ is the image of the Čech class of the cocycle $(\frac{1}{2\pi i} d\log g_{ij})$, by naturality of the map from Čech cohomology (Proposition P2.7.19).

On the other hand, $\delta_2[\Theta]$ is computed by local lifts: as in the proof of Theorem P2.7.22 and in Example P2.7.25, a global section $\Theta$ of $\mathcal{Z}^2$ with local preimages $a_i \in \mathcal{A}^1(U_i)$ has $\delta_2(\Theta)$ equal to the image of the Čech $1$-cocycle $(a_j - a_i)$ of $\mathcal{Z}^1$. By the first paragraph this cocycle is $-\frac{1}{2\pi i} d\log g_{ij}$, so $\delta_2[\Theta] = -\lambda_*[L]$. Applying $\delta_1$, the de Rham isomorphism sends $[\Theta]$ to $-\delta_1 \lambda_*[L]$, which is the image of $-\delta[L] = c_1(L)$. Since $\Theta = c_1(L, \nabla)$, this is the claim. $\square$

*Proof of Theorem P6.3.28.* Choose a Hermitian metric $h$ on $L$ (Proposition P6.3.6); by Theorem P6.3.27, $\int_X c_1(L) = \int_X \frac{i}{2\pi} F_h$. Let $p_1, \dots, p_m$ be the zeros and poles of $s$, and around each $p_l$ choose a coordinate $z$ centred at $p_l$ on a disc $D$ with a holomorphic frame $e$, so that $s = z^{k_l} u\, e$ with $k_l = \operatorname{ord}_{p_l}(s)$ and $u$ holomorphic and nowhere zero on $D$. For small $\varepsilon > 0$ let $X_\varepsilon$ be $X$ minus the discs $\{|z| < \varepsilon\}$ around the $p_l$, a compact surface with boundary. On $X_\varepsilon$, $\psi = \log |s|^2_h$ is smooth, and by Corollary P6.3.17, whose proof applies to meromorphic sections away from zeros and poles, $\frac{i}{2\pi} F_h = -\frac{i}{2\pi} \partial\bar\partial \psi$. Since $d(\partial\psi) = \bar\partial\partial\psi = -\partial\bar\partial\psi$, this is $d(\frac{i}{2\pi}\partial\psi)$, and Stokes gives
$$\int_{X_\varepsilon} \frac{i}{2\pi} F_h = \frac{i}{2\pi} \int_{\partial X_\varepsilon} \partial\psi = -\frac{i}{2\pi} \sum_l \oint_{|z| = \varepsilon} \partial\psi,$$
the circles oriented counterclockwise in $z$, which is the opposite of their orientation as boundary of $X_\varepsilon$. Near $p_l$, $\psi = k_l \log |z|^2 + \log |u|^2 + \log |e|^2_h$ and $\partial \log |z|^2 = \bar z\, dz / |z|^2 = dz / z$. The other two terms have smooth $\partial$ on $D$, so their integrals over $|z| = \varepsilon$ tend to $0$, and $\oint_{|z|=\varepsilon} k_l\, dz/z = 2\pi i\, k_l$. Letting $\varepsilon \to 0$, the left side tends to $\int_X \frac{i}{2\pi} F_h$ because $F_h$ is smooth on $X$, and the right side to $-\frac{i}{2\pi} \sum_l 2\pi i\, k_l = \sum_l k_l$. $\square$

### Exercises

1. (A) Show that $c_2(E, \nabla) = \frac{1}{2}((\operatorname{tr} A)^2 - \operatorname{tr}(A^2))$ with $A = \frac{i}{2\pi} F_\nabla$, and that $\operatorname{tr}(A^k)$ is an invariant polynomial for every $k$.
2. (A) On $\mathbb{P}^1 \times \mathbb{P}^1$ let $\mathcal{O}(a, b) = p_1^* \mathcal{O}(a) \otimes p_2^* \mathcal{O}(b)$. Show that $\int c_1(\mathcal{O}(a, b))^2 = 2ab$, and compute $c(T_{\mathbb{P}^1 \times \mathbb{P}^1})$ and $\int c_2$.
3. (A) For a smooth plane curve $C$ of degree $d$, show with Proposition P6.2.19 that the normal bundle has degree $d^2$, and check $\deg T_{\mathbb{P}^2}|_C = \deg T_C + \deg N_{C}$ with Examples P6.3.30 and P6.3.31.
4. (B) Let $X \subset \mathbb{P}^3$ be a smooth quartic surface. Use the normal bundle sequence $0 \to T_X \to T_{\mathbb{P}^3}|_X \to \mathcal{O}_X(4) \to 0$ of Proposition P6.2.19 and the Whitney formula to show $c(T_X) = 1 + 6 h^2|_X$ and $\int_X c_2(T_X) = 24$, using that $\int_X h^2 = 4$.
5. (B) Let $L$ be a smooth complex line bundle with transition functions $g_{ij}$ in $\mathcal{A}^*$. Define $c_1(L) = -\delta_{\mathcal{A}}[L]$ with the connecting map of $0 \to \mathbb{Z} \to \mathcal{A} \xrightarrow{\exp(2\pi i \cdot)} \mathcal{A}^* \to 0$, show that the proof of Theorem P6.3.27 applies verbatim, and that for a holomorphic line bundle the two definitions agree.
6. (C) Prove part 2 of Theorem P6.3.23 by applying part 1 on $X \times \mathbb{R}$ to the connection $(1 - t) \operatorname{pr}^*\nabla_0 + t \operatorname{pr}^*\nabla_1$ and integrating over the fibre $[0, 1]$, and show that the resulting transgression form is $T$.

### Lean

Mathlib has determinants and characteristic polynomials of matrices over commutative rings, and smooth manifolds. It has no de Rham cohomology of manifolds, no curvature of connections, no Chern classes and no exponential sequence of sheaves. The handbook adds no `MinimalModel` node here.

### Notes and history

Chern defined his classes for Hermitian manifolds by curvature in 1946 (Che46), and Weil, in unpublished notes of 1949, showed that every invariant polynomial in the curvature of an arbitrary connection gives a closed form whose class does not depend on the connection; Chern-Weil theory is named after these two works. The sign in the comparison of the integral class from the exponential sequence with the curvature class is a frequent source of confusion: Griffiths and Harris, Section 1.1 (GH78), and Huybrechts, Section 4.4 (Huy05), use conventions under which $c_1(\mathcal{O}(1))$ is positive, and this volume fixes $c_1 = -\delta$ with the Čech conventions of P2 so that the same holds here. The Gauss-Bonnet theorem $\int_X c_n(T_X) = \chi_{\mathrm{top}}(X)$ for compact complex manifolds is cited from Bott and Tu, Chapter IV (BT82), and is not proved in this handbook. The degree theorem P6.3.28 is the analytic form of the statement that a meromorphic function on a compact Riemann surface has as many zeros as poles, which P5 uses in its algebraic form for Riemann-Roch (Theorem P5.1.10).
