---
title: Lefschetz linear algebra and the Kähler identities
nodes: []
sources: [Huy05, Voi02, GH78, Wel80, Wei58]
reads_with: [Huy05:1.2, Huy05:3.1, Voi02:6.1, GH78:0.7, Wel80:V.3, Wel80:V.4]
requires: [P6.1, P6.2, P6.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Lefschetz linear algebra and the Kähler identities

### Statement

Let $V$ be a real vector space of dimension $2n$ with a complex structure $J$ and a compatible inner product $g$, with fundamental form $\omega$ (Definition P6.3.1). Write $\Lambda^k = \Lambda^k V^* \otimes \mathbb{C}$ and $\Lambda^{p,q}$ for its subspace of type $(p,q)$. The inner product $g$ induces an inner product on $\Lambda^k V^*$, for which the wedge products of an orthonormal basis of $V^*$ are orthonormal, and its Hermitian extension $\langle \ , \ \rangle$ to $\Lambda^k$, linear in the first variable. Choosing a unitary basis identifies $V$ with $\mathbb{C}^n$ and $\omega$ with $\omega_0 = \sum_j dx_j \wedge dy_j$ (Proposition P6.3.2). Then $dx_1, dy_1, \dots, dx_n, dy_n$ is orthonormal, $\langle dz_j, dz_k \rangle = 2\delta_{jk}$, $\langle dz_j, d\bar z_k \rangle = 0$, and the forms $dz_I \wedge d\bar z_J$ are pairwise orthogonal with $|dz_I \wedge d\bar z_J|^2 = 2^{|I| + |J|}$. In particular the decomposition $\Lambda^k = \bigoplus_{p+q=k} \Lambda^{p,q}$ is orthogonal. The space $V$ is oriented by $J$, with volume form $\operatorname{vol} = \omega^n/n! = dx_1 \wedge dy_1 \wedge \dots \wedge dx_n \wedge dy_n$.

**Definition P6.4.7 (the operators star, L and Lambda).** In the situation above:

1. The *Hodge star* is the $\mathbb{C}$-linear map $* \colon \Lambda^k \to \Lambda^{2n-k}$ with $\alpha \wedge *\bar\beta = \langle \alpha, \beta \rangle \operatorname{vol}$ for all $\alpha, \beta \in \Lambda^k$. It is the complex linear extension of the real Hodge star of $g$, so $\overline{*\beta} = *\bar\beta$.
2. The *Lefschetz operator* is $L \colon \Lambda^k \to \Lambda^{k+2}$, $L\alpha = \omega \wedge \alpha$, and $\Lambda \colon \Lambda^{k+2} \to \Lambda^k$ is its adjoint, $\langle L\alpha, \beta \rangle = \langle \alpha, \Lambda\beta \rangle$.
3. The *counting operator* is $H = \sum_k (k - n)\Pi^k$, and the *Weil operator* is $\mathbf{I} = \sum_{p,q} i^{p-q}\Pi^{p,q}$, where $\Pi^k$ and $\Pi^{p,q}$ are the projections to $\Lambda^k$ and $\Lambda^{p,q}$.

On a Hermitian manifold $(X, h)$ of dimension $n$ these operators act pointwise on $T_xX$ and so define $\mathcal{A}_X$-linear maps between the sheaves of forms, with the same names. The operators $L$, $\Lambda$ and $H$ are real, $L$ has type $(1,1)$ and $\Lambda$ has type $(-1,-1)$, since $\omega$ is a real $(1,1)$-form and the type decomposition is orthogonal.

**Definition P6.4.8 (primitive forms).** A form $\alpha \in \Lambda^k$ is *primitive* if $\Lambda\alpha = 0$. Write $P^k = \ker(\Lambda) \cap \Lambda^k$ and $P^{p,q} = P^k \cap \Lambda^{p,q}$ for $p + q = k$. A form on a Hermitian manifold is primitive if it is primitive at every point.

**Theorem P6.4.9 (Lefschetz decomposition of forms).** In the situation above:

1. $[L, \Lambda] = H$, $[H, L] = 2L$ and $[H, \Lambda] = -2\Lambda$. For $\alpha \in P^k$ and $j \geq 1$, $\Lambda L^j\alpha = j(n - k - j + 1)L^{j-1}\alpha$.
2. $P^k = 0$ for $k > n$. For $0 \neq \alpha \in P^k$ with $k \leq n$, $L^j\alpha \neq 0$ for $0 \leq j \leq n - k$ and $L^{n-k+1}\alpha = 0$.
3. There is an orthogonal decomposition $\Lambda^k = \bigoplus_{j \geq 0} L^j P^{k-2j}$. The map $L^j \colon P^{k-2j} \to \Lambda^k$ is injective if $j \geq k - n$ and zero if $j < k - n$, so every $\alpha \in \Lambda^k$ is uniquely $\alpha = \sum_{j \geq \max(0, k-n)} L^j\alpha_j$ with $\alpha_j \in P^{k-2j}$. The decomposition is compatible with types: $P^k = \bigoplus_{p+q=k} P^{p,q}$ and $\Lambda^{p,q} = \bigoplus_j L^j P^{p-j, q-j}$.
4. For $k \leq n$, $L^{n-k} \colon \Lambda^k \to \Lambda^{2n-k}$ is an isomorphism.
5. For $k \leq n$ and $\alpha \in \Lambda^k$, $\alpha$ is primitive if and only if $L^{n-k+1}\alpha = 0$.

Lean: not yet in Lean.

**Proposition P6.4.10 (Weil's formula).** In the situation above:

1. If $V = V' \oplus V''$ is an orthogonal decomposition into $J$-stable subspaces of dimensions $2n'$ and $2n''$, then $*(\alpha' \wedge \alpha'') = (-1)^{k'k''}\, {*'}\alpha' \wedge {*''}\alpha''$ for $\alpha' \in \Lambda^{k'}V'^*_{\mathbb{C}}$ and $\alpha'' \in \Lambda^{k''}V''^*_{\mathbb{C}}$, where $*'$ and $*''$ are the stars of the summands.
2. $*$ is an isometry, $** = (-1)^k$ on $\Lambda^k$, $*(\Lambda^{p,q}) = \Lambda^{n-q,n-p}$, $*$ commutes with $\mathbf{I}$, and $\Lambda = *^{-1}L*$.
3. (Weil's formula.) For $\alpha \in P^k$ and $0 \leq j \leq n - k$,
$$*L^j\alpha = (-1)^{k(k+1)/2} \frac{j!}{(n-k-j)!} L^{n-k-j}\mathbf{I}(\alpha).$$

For $n = 1$ the formula gives $*1 = \omega$, $*\omega = 1$, $*dz = -i\, dz$ and $*d\bar z = i\, d\bar z$, which is what the real star gives directly from $*dx = dy$ and $*dy = -dx$.

Lean: not yet in Lean.

**Definition P6.4.11 (adjoint operators and Laplacians).** Let $(X, h)$ be a Hermitian manifold of dimension $n$ with volume form $\operatorname{vol} = \omega^n/n!$. For forms $\alpha$, $\beta$ of the same degree, one of them with compact support, put $(\alpha, \beta) = \int_X \langle \alpha, \beta \rangle \operatorname{vol} = \int_X \alpha \wedge *\bar\beta$. Define
$$d^* = -{*}d{*}, \qquad \partial^* = -{*}\bar\partial{*}, \qquad \bar\partial^* = -{*}\partial{*},$$
so that $d^* = \partial^* + \bar\partial^*$, $\partial^*$ has type $(-1, 0)$ and $\bar\partial^*$ has type $(0, -1)$, and the *Laplacians*
$$\Delta_d = dd^* + d^*d, \qquad \Delta_\partial = \partial\partial^* + \partial^*\partial, \qquad \Delta_{\bar\partial} = \bar\partial\bar\partial^* + \bar\partial^*\bar\partial.$$
A form is *harmonic*, or $\Delta$-harmonic for one of these Laplacians, if $\Delta$ kills it. The operators $d^*$, $\partial^*$ and $\bar\partial^*$ are the *formal adjoints* of $d$, $\partial$ and $\bar\partial$: for instance $(\partial\alpha, \beta) = (\alpha, \partial^*\beta)$ whenever $\alpha$ or $\beta$ has compact support. This is verified in the proof section.

**Theorem P6.4.12 (the Kähler identities).** Let $(X, \omega)$ be a Kähler manifold. Then, as operators on $A^\bullet(X)$:

1. $[\Lambda, \bar\partial] = -i\partial^*$, $[\Lambda, \partial] = i\bar\partial^*$, $[\bar\partial^*, L] = i\partial$ and $[\partial^*, L] = -i\bar\partial$.
2. $\partial\bar\partial^* + \bar\partial^*\partial = 0$ and $\bar\partial\partial^* + \partial^*\bar\partial = 0$.
3. $\Delta_d = 2\Delta_\partial = 2\Delta_{\bar\partial}$.
4. $\Delta_d$ commutes with $*$, $\partial$, $\bar\partial$, $\partial^*$, $\bar\partial^*$, $L$ and $\Lambda$, and maps $A^{p,q}(X)$ to $A^{p,q}(X)$.

Lean: not yet in Lean.

### Proof in words

The linear algebra is the representation theory of $\mathfrak{sl}_2$ in one concrete case. The space $V$ is an orthogonal sum of $n$ complex lines, and the exterior algebra of $V$ is the graded tensor product of the exterior algebras of the lines. On one line everything is a $1$, $2$, $1$-dimensional computation, and $L$, $\Lambda$, $H$ and the star are additive or multiplicative along the sum. This gives $[L, \Lambda] = H$. The commutation relation then forces the shape of the strings $\alpha, L\alpha, L^2\alpha, \dots$ that start at a primitive form, and these strings give the Lefschetz decomposition.

For Weil's formula, the element $w = e^L e^{-\Lambda} e^L$ of the group generated by $L$ and $\Lambda$ conjugates $L$ to $-\Lambda$ and $\Lambda$ to $-L$, so it reverses each string. It is multiplicative along orthogonal sums, and so is the Hodge star up to a sign that the factor $(-1)^{k(k+1)/2}$ absorbs. Comparing the two on one line, where both are written down, shows that $*$ equals $(-1)^{k(k+1)/2} w\mathbf{I}$ on $k$-forms. Weil's formula is then the action of $w$ on a string.

The Kähler identities compare first-order differential operators. On $\mathbb{C}^n$ with the flat metric, $\partial = \sum_j dz_j \wedge \partial_j$, $\partial^*$ is minus the sum of the contractions with $dz_j$ composed with $\bar\partial_j$, and $\Lambda$ is a sum of double contractions. The identity $[\Lambda, \bar\partial] = -i\partial^*$ is the anticommutation relation between wedge and contraction. On a Kähler manifold, normal coordinates make the metric flat to first order at a point, and a first-order operator built from the metric only sees its value and first derivatives at that point, so the identity holds. The other identities follow by conjugation and adjunction. Then $\Delta_d = 2\Delta_{\bar\partial}$ is a short formal computation.

### Examples

**Example P6.4.13 (the identities on $\mathbb{C}$ and on a torus).** On $\mathbb{C}$ with $\omega_0 = \frac{i}{2}dz \wedge d\bar z = dx \wedge dy$:

1. $*1 = dx \wedge dy$, $*(dz \wedge d\bar z) = *(-2i\, dx \wedge dy) = -2i$, $*dz = -i\, dz$, $*d\bar z = i\, d\bar z$. The adjoint $\Lambda$ kills functions and $1$-forms, and $\Lambda(f\, dz \wedge d\bar z) = -2i f$, since $\Lambda(dx \wedge dy) = 1$.
2. For smooth $g$ with compact support, $\partial^*(g\, dz) = -{*}\bar\partial(-i g\, dz) = i\frac{\partial g}{\partial \bar z} *(d\bar z \wedge dz) = -2\frac{\partial g}{\partial \bar z}$, and in the same way $\bar\partial^*(g\, d\bar z) = -2\frac{\partial g}{\partial z}$, $\partial^*(g\, dz \wedge d\bar z) = -2\frac{\partial g}{\partial \bar z} d\bar z$ and $\bar\partial^*(g\, dz \wedge d\bar z) = 2\frac{\partial g}{\partial z} dz$. As a check, $(\partial f, g\, dz) = \int 2 f_z \bar g\, dx\, dy = -\int 2 f\, \overline{g_{\bar z}}\, dx\, dy = (f, -2g_{\bar z})$.
3. On $g\, dz$: $[\Lambda, \bar\partial](g\, dz) = \Lambda(g_{\bar z}\, d\bar z \wedge dz) = \Lambda(-g_{\bar z}\, dz \wedge d\bar z) = 2i g_{\bar z} = -i\partial^*(g\, dz)$. On $g\, d\bar z$: $[\Lambda, \partial](g\, d\bar z) = \Lambda(g_z\, dz \wedge d\bar z) = -2i g_z = i\bar\partial^*(g\, d\bar z)$. On a function $f$: $[\bar\partial^*, L]f = \bar\partial^*(\frac{i}{2} f\, dz \wedge d\bar z) = i f_z\, dz = i\partial f$, and $[\partial^*, L]f = \partial^*(\frac{i}{2} f\, dz \wedge d\bar z) = -i f_{\bar z}\, d\bar z = -i\bar\partial f$. All four signs of Theorem P6.4.12 are confirmed.
4. On functions $\Delta_d f = d^*df = -(f_{xx} + f_{yy}) = -4 f_{z\bar z}$ and $\Delta_{\bar\partial} f = \bar\partial^*(f_{\bar z}\, d\bar z) = -2 f_{z\bar z}$, so $\Delta_d = 2\Delta_{\bar\partial}$.

On $\mathbb{C}^n$ with $\omega_0$, the proof below gives $\Delta_{\bar\partial} = -2\sum_j \partial_j\bar\partial_j = -\frac12 \sum_j (\partial_{x_j}^2 + \partial_{y_j}^2)$ acting on each coefficient of $\sum f_{IJ}\, dz_I \wedge d\bar z_J$. The same holds on a torus $X = \mathbb{C}^n/\Lambda$ with the flat metric, whose charts differ by translations. For the character $e_\xi(x) = e^{2\pi i \langle \xi, x \rangle}$, with $\xi$ in the dual lattice $\{\xi : \langle \xi, \lambda \rangle \in \mathbb{Z} \text{ for all } \lambda \in \Lambda\}$, one gets $\Delta_d e_\xi = 4\pi^2|\xi|^2 e_\xi$ and $\Delta_{\bar\partial} e_\xi = 2\pi^2|\xi|^2 e_\xi$. A form on $X$ is harmonic if and only if each coefficient $f$ is harmonic, and on a compact manifold this forces $f$ to be constant, since $0 = \int_X \bar f \Delta_d f = \int_X |df|^2$. So the harmonic $(p,q)$-forms are the forms $\sum c_{IJ}\, dz_I \wedge d\bar z_J$ with constant coefficients, a space of dimension $\binom{n}{p}\binom{n}{q}$, which is the Dolbeault group computed in Theorem P6.2.29.

Weil's formula on $\mathbb{C}^2$ can be checked by hand in the orthonormal basis $e_1 = dx_1$, $e_2 = dy_1$, $e_3 = dx_2$, $e_4 = dy_2$, with $*(e_1e_3) = -e_2e_4$, $*(e_2e_4) = -e_1e_3$, $*(e_1e_4) = e_2e_3$, $*(e_2e_3) = e_1e_4$, $*(e_1e_2) = e_3e_4$. The form $\alpha = dz_1 \wedge d\bar z_2 = e_1e_3 - ie_1e_4 + ie_2e_3 + e_2e_4$ is primitive of type $(1,1)$, since $\Lambda$ of a $(1,1)$-form $\sum a_{jk}\, dz_j \wedge d\bar z_k$ is $-2i\sum_j a_{jj}$. The formula with $k = 2$, $j = 0$ predicts $*\alpha = -\alpha$, and indeed $*\alpha = -e_2e_4 - ie_2e_3 + ie_1e_4 - e_1e_3 = -\alpha$. The formula with $k = 1$, $j = 0$ predicts $*dz_1 = -\frac{1}{1!} L(i\, dz_1) = -i\omega_0 \wedge dz_1$. Directly, $*dz_1 = *e_1 + i*e_2 = e_2e_3e_4 - ie_1e_3e_4$, while $\omega_0 \wedge dz_1 = (e_1e_2 + e_3e_4) \wedge (e_1 + ie_2) = e_1e_3e_4 + ie_2e_3e_4$, and $-i$ times this is $e_2e_3e_4 - ie_1e_3e_4$. The primitivity hypothesis cannot be dropped: $\omega_0 = e_1e_2 + e_3e_4$ has degree $2$ and type $(1,1)$, and the formula with $k = 2$, $j = 0$ would give $*\omega_0 = -\omega_0$, while $*\omega_0 = \omega_0$. The correct formula for $\omega_0 = L(1)$ is the case $k = 0$, $j = 1$, which gives $*L1 = \frac{1!}{1!}L1$.

The Kähler hypothesis cannot be dropped from Theorem P6.4.12. On $\mathbb{C}^2$ let $\omega' = e^{2u}\omega_0$ with $u = x_1$, a Hermitian metric with $d\omega' = 2e^{2u}dx_1 \wedge \omega_0 \neq 0$. For $k$-forms in real dimension $4$ the new pointwise inner product is $e^{-2ku}$ times the old one and $\operatorname{vol}' = e^{4u}\operatorname{vol}$, so $*' = e^{(4-2k)u}*$ on $k$-forms. Also $\Lambda' = e^{-2u}\Lambda$. For a $1$-form $\beta$, $\partial'^*\beta = -e^{-4u}{*}\bar\partial(e^{2u}{*}\beta) = e^{-2u}(\partial^*\beta - 2*(\bar\partial u \wedge *\beta))$. Take $\beta = dz_1$, with constant coefficients, so that $\partial^*\beta = 0$ and $[\Lambda', \bar\partial]\beta = 0$. With $\bar\partial u = \frac12 d\bar z_1$ and $*dz_1 = -i\omega_0 \wedge dz_1$ from the check above,
$$\bar\partial u \wedge *dz_1 = \tfrac14\, d\bar z_1 \wedge dz_2 \wedge d\bar z_2 \wedge dz_1 = -\tfrac14 (dz_1 \wedge d\bar z_1) \wedge (dz_2 \wedge d\bar z_2) = \operatorname{vol},$$
so $-i\partial'^*dz_1 = 2ie^{-2x_1} \neq 0 = [\Lambda', \bar\partial]dz_1$.

### Proof

*Reduction to $\mathbb{C}^n$ and products.* Fix a unitary basis, so that $V = V_1 \oplus \dots \oplus V_n$ orthogonally, with $V_j$ the complex line spanned by $\partial/\partial x_j$ and $\partial/\partial y_j$ and $\omega = \sum_j \omega_j$, $\omega_j = dx_j \wedge dy_j$. Every element of $\Lambda^\bullet$ is a sum of products $\alpha_1 \wedge \dots \wedge \alpha_n$ with $\alpha_j \in \Lambda^\bullet V_j^*$, and $\langle \alpha_1 \wedge \dots \wedge \alpha_n, \beta_1 \wedge \dots \wedge \beta_n \rangle = \prod_j \langle \alpha_j, \beta_j \rangle$ when $\deg\alpha_j = \deg\beta_j$ for all $j$, since this holds for the orthonormal monomials. Let $L_j$ be wedge product with $\omega_j$ and $\Lambda_j$ its adjoint. Because $\omega_j$ has even degree, $L_j$ acts on the $j$-th factor only, and so does $\Lambda_j$, which on $\Lambda^\bullet V_j^*$ kills $1$, $dx_j$ and $dy_j$ and sends $\omega_j$ to $1$. Then $L = \sum_j L_j$, $\Lambda = \sum_j \Lambda_j$, and $L_j$, $\Lambda_j$ commute with $L_l$, $\Lambda_l$ for $l \neq j$.

*Theorem P6.4.9.* (1) On one line, $[L_j, \Lambda_j]$ is $-1$ on $1$, $0$ on $dx_j$ and $dy_j$, and $+1$ on $\omega_j$, that is, multiplication by $\deg - 1$. On a product with factors of degrees $k_1, \dots, k_n$, $[L, \Lambda] = \sum_j [L_j, \Lambda_j]$ acts by $\sum_j (k_j - 1) = k - n$. The relations with $H$ hold since $L$ raises degree by $2$ and $\Lambda$ lowers it by $2$. For $\alpha \in P^k$, $[L^j, \Lambda] = \sum_{i=0}^{j-1} L^i[L, \Lambda]L^{j-1-i}$, and $[L, \Lambda]$ acts on $L^{j-1-i}\alpha$ by $k + 2(j - 1 - i) - n$. Summing over $i$ gives $[L^j, \Lambda]\alpha = j(k - n + j - 1)L^{j-1}\alpha$. Since $\Lambda\alpha = 0$, $\Lambda L^j\alpha = -[L^j, \Lambda]\alpha = j(n - k - j + 1)L^{j-1}\alpha$.

(2) Let $0 \neq \alpha \in P^k$ and let $m \geq 0$ be the largest integer with $L^m\alpha \neq 0$, which exists because $\Lambda^\ell = 0$ for $\ell > 2n$. By part 1, $0 = \Lambda L^{m+1}\alpha = (m+1)(n - k - m)L^m\alpha$, so $m = n - k$. Hence $k \leq n$, $L^j\alpha \neq 0$ for $j \leq n - k$ and $L^{n-k+1}\alpha = 0$.

(3) Since $\Lambda$ is the adjoint of $L$, $\Lambda^k = \ker(\Lambda|_{\Lambda^k}) \oplus L(\Lambda^{k-2})$ orthogonally, that is, $\Lambda^k = P^k \oplus L\Lambda^{k-2}$. By induction on $k$, $\Lambda^{k-2} = \sum_j L^j P^{k-2-2j}$, so $\Lambda^k = \sum_{j \geq 0} L^jP^{k-2j}$. For $j < l$, $\alpha \in P^{k-2j}$ and $\beta \in P^{k-2l}$, $\langle L^j\alpha, L^l\beta \rangle = \langle \Lambda^l L^j\alpha, \beta \rangle = 0$, because by part 1 $\Lambda^{j+1}L^j\alpha$ is a multiple of $\Lambda\alpha = 0$. So the sum is orthogonal, hence direct. By part 2 applied to $P^{k-2j}$, $L^j$ is injective on $P^{k-2j}$ if $j \leq n - (k - 2j)$, that is, $j \geq k - n$, and $L^j P^{k-2j} = 0$ otherwise. As $L$ and $\Lambda$ have types $(1,1)$ and $(-1,-1)$, $\Lambda$ commutes with the projections $\Pi^{p,q}$ up to the shift of type, so $P^k = \bigoplus P^{p,q}$, and the decomposition refines by type.

(4) Let $k \leq n$ and $\alpha = \sum_j L^j\alpha_j$ with $\alpha_j \in P^{k-2j}$. Then $L^{n-k}\alpha = \sum_j L^{n-k+j}\alpha_j$, the $j$-th term lies in the summand $L^{n-k+j}P^{k-2j}$ of $\Lambda^{2n-k}$, and $L^{n-k+j}\alpha_j \neq 0$ if $\alpha_j \neq 0$, because $n - k + j \leq n - (k - 2j)$. So $L^{n-k}$ is injective, and it is an isomorphism because $\dim\Lambda^k = \binom{2n}{k} = \dim\Lambda^{2n-k}$.

(5) With the same notation, $L^{n-k+1}\alpha = \sum_j L^{n-k+1+j}\alpha_j$. For $j \geq 1$ the exponent satisfies $n - k + 1 + j \leq n - (k - 2j)$, so these terms are nonzero when $\alpha_j \neq 0$ and lie in distinct summands, while the term $j = 0$ vanishes by part 2. So $L^{n-k+1}\alpha = 0$ if and only if $\alpha_j = 0$ for all $j \geq 1$, that is, $\alpha \in P^k$.

*Proposition P6.4.10.* (1) Here $\operatorname{vol} = \operatorname{vol}' \wedge \operatorname{vol}''$, since $\omega^n = (\omega' + \omega'')^n = \binom{n}{n'}\omega'^{n'} \wedge \omega''^{n''}$. For a real orthonormal monomial $m$ of degree $k$, $*m$ is characterized by $m_1 \wedge *m = \delta_{m_1 m}\operatorname{vol}$ for all orthonormal monomials $m_1$ of degree $k$. Let $m = e_A \wedge f_B$ with $e_A$ a monomial in $V'^*$ of degree $k'$ and $f_B$ a monomial in $V''^*$ of degree $k''$. Then
$$e_{A_1} \wedge f_{B_1} \wedge {*'}e_A \wedge {*''}f_B = (-1)^{k''(2n' - k')}(e_{A_1} \wedge {*'}e_A) \wedge (f_{B_1} \wedge {*''}f_B) = (-1)^{k'k''}\delta_{A_1A}\delta_{B_1B}\operatorname{vol},$$
which proves the formula on monomials, and it extends by linearity.

(2) On one line, the real star sends $1 \mapsto dx \wedge dy$, $dx \mapsto dy$, $dy \mapsto -dx$, $dx \wedge dy \mapsto 1$, which gives the values $*1 = \omega$, $*\omega = 1$, $*dz = -i\, dz$, $*d\bar z = i\, d\bar z$ stated after the proposition. So on one line $*$ is an isometry, $** = (-1)^k$, $*$ maps $\Lambda^{p,q}$ to $\Lambda^{1-q,1-p}$ and commutes with $\mathbf{I}$. Part 1 propagates these statements to $V = V_1 \oplus \dots \oplus V_n$. For $**$ the sign is $(-1)^{k'k''}(-1)^{(2n'-k')(2n''-k'')}(-1)^{k'}(-1)^{k''} = (-1)^{k}$. For types, $(p', q') + (p'', q'')$ goes to $(n' - q', n' - p') + (n'' - q'', n'' - p'')$. Since $\mathbf{I}$ is multiplicative and commutes with $*$ on each factor, it commutes with $*$. For $\Lambda$, since $L$ and $*$ are real, $\langle L\alpha, \beta \rangle\operatorname{vol} = \omega \wedge \alpha \wedge *\bar\beta = \alpha \wedge *(*^{-1}L*\bar\beta) = \langle \alpha, *^{-1}L*\beta \rangle\operatorname{vol}$.

(3) Let $w = e^L e^{-\Lambda} e^L$, a finite sum since $L$ and $\Lambda$ are nilpotent. Let $\epsilon_k = (-1)^{k(k+1)/2}$ and $T = \sum_k \epsilon_k w\mathbf{I}\Pi^k$. The first claim is that $* = T$. On one line, $w(1) = e^Le^{-\Lambda}(1 + \omega) = e^L\omega = \omega$, $w(\omega) = e^L(\omega - 1) = -1$ and $w$ is the identity on $1$-forms. So $T(1) = \omega$, $T(\omega) = \epsilon_2 w(\omega) = -w(\omega) = 1$, $T(dz) = -w(i\, dz) = -i\, dz$ and $T(d\bar z) = -w(-i\, d\bar z) = i\, d\bar z$. These are the values of $*$. For an orthogonal sum $V' \oplus V''$, $L = L' + L''$ and $\Lambda = \Lambda' + \Lambda''$ with every primed operator commuting with every double-primed one, so $w(\alpha' \wedge \alpha'') = w'\alpha' \wedge w''\alpha''$. Likewise $\mathbf{I}$ is multiplicative, and $\epsilon_{k'+k''} = \epsilon_{k'}\epsilon_{k''}(-1)^{k'k''}$. So $T(\alpha' \wedge \alpha'') = (-1)^{k'k''}T'\alpha' \wedge T''\alpha''$, the same rule as $*$ in part 1. By induction on $n$, $* = T$.

The second claim is that $wLw^{-1} = -\Lambda$ and $w\Lambda w^{-1} = -L$. For nilpotent $X$, $e^X Y e^{-X} = \sum_m \frac{1}{m!}\operatorname{ad}_X^m(Y)$, since both sides solve $f'(t) = [X, f(t)]$, $f(0) = Y$, after replacing $X$ by $tX$. With $[L, \Lambda] = H$, $[H, L] = 2L$ and $[H, \Lambda] = -2\Lambda$ this gives $e^L\Lambda e^{-L} = \Lambda + H - L$, $e^{-\Lambda}He^{\Lambda} = H - 2\Lambda$, $e^{-\Lambda}Le^{\Lambda} = L + H - \Lambda$ and $e^LHe^{-L} = H - 2L$. Hence $e^{-\Lambda}(\Lambda + H - L)e^{\Lambda} = \Lambda + (H - 2\Lambda) - (L + H - \Lambda) = -L$, which $e^L$ fixes, so $w\Lambda w^{-1} = -L$. Similarly $e^LLe^{-L} = L$, $e^{-\Lambda}Le^{\Lambda} = L + H - \Lambda$ and $e^L(L + H - \Lambda)e^{-L} = L + (H - 2L) - (\Lambda + H - L) = -\Lambda$.

Now let $\alpha \in P^k$, $m = n - k$ and $v_j = L^j\alpha$, so that $Lv_j = v_{j+1}$, $v_{m+1} = 0$ and $\Lambda v_j = j(m - j + 1)v_{j-1}$ by Theorem P6.4.9. The span $S$ of $v_0, \dots, v_m$ is stable under $L$, $\Lambda$ and $w$, and since the $v_j$ are nonzero of distinct degrees, the elements of $S$ killed by $L$ are the multiples of $v_m$. As $Lwv_0 = -w\Lambda v_0 = 0$, $wv_0 = \lambda v_m$. Then $e^{-\Lambda}e^Lv_0 = e^{-L}wv_0 = \lambda v_m$, and the component of degree $k + 2m$ of the left side is $v_m/m!$, because $\Lambda$ lowers degree. So $\lambda = 1/m!$ and
$$wv_j = (wLw^{-1})^j wv_0 = \frac{(-1)^j}{m!}\Lambda^jv_m = \frac{(-1)^j}{m!}\prod_{i=m-j+1}^{m} i(m - i + 1)\; v_{m-j} = (-1)^j\frac{j!}{(m-j)!}v_{m-j}.$$
Finally $\mathbf{I}$ commutes with $L$ and $\Lambda$, so $\mathbf{I}\alpha \in P^k$, and $\epsilon_{k+2j} = \epsilon_k(-1)^j$. Therefore $*L^j\alpha = \epsilon_{k+2j}wL^j\mathbf{I}\alpha = \epsilon_k(-1)^j(-1)^j\frac{j!}{(m-j)!}L^{m-j}\mathbf{I}\alpha$, which is Weil's formula.

*Definition P6.4.11, the adjoint property.* Let $\alpha$ have type $(p-1, q)$ and $\beta$ type $(p, q)$, with $k = p + q$ and one of them compactly supported. The form $\alpha \wedge *\bar\beta$ has type $(n-1, n)$, so $d(\alpha \wedge *\bar\beta) = \partial(\alpha \wedge *\bar\beta) = \partial\alpha \wedge *\bar\beta + (-1)^{k-1}\alpha \wedge \partial{*}\bar\beta$, and its integral is $0$ by Stokes. Using $** = (-1)^{k-1}$ on forms of degree $2n - k + 1$,
$$(\partial\alpha, \beta) = (-1)^k\int_X \alpha \wedge \partial{*}\bar\beta = -\int_X \alpha \wedge *({*}\partial{*}\bar\beta) = \int_X \alpha \wedge *\overline{(-{*}\bar\partial{*}\beta)} = (\alpha, \partial^*\beta).$$
The same computation with $\bar\partial$ or $d$ in place of $\partial$ gives the other two cases.

*Theorem P6.4.12.* (1) First let $X = \mathbb{C}^n$ with $\omega_0$. For a constant $1$-form $\theta$ let $\epsilon_\theta = \theta \wedge$ and $\iota_\theta$ its adjoint. For real orthonormal $e_a$, $\iota_{e_a}$ is contraction with the dual basis vector, an antiderivation, and $\epsilon_{e_a}\iota_{e_b} + \iota_{e_b}\epsilon_{e_a} = \delta_{ab}$. By sesquilinearity, $\epsilon_\theta\iota_\eta + \iota_\eta\epsilon_\theta = \langle \theta, \eta \rangle$ for complex $\theta$, $\eta$. Write $e_j = \epsilon_{dz_j}$, $\bar e_j = \epsilon_{d\bar z_j}$ and $e_j^*$, $\bar e_j^*$ for the adjoints. Then
$$e_je_k^* + e_k^*e_j = 2\delta_{jk}, \qquad \bar e_j\bar e_k^* + \bar e_k^*\bar e_j = 2\delta_{jk}, \qquad \bar e_k e_j^* + e_j^*\bar e_k = 0.$$
Now $L = \frac{i}{2}\sum_j e_j\bar e_j$, so $\Lambda = -\frac{i}{2}\sum_j \bar e_j^*e_j^*$, and $\partial = \sum_j e_j\partial_j$, $\bar\partial = \sum_j \bar e_j\bar\partial_j$ with $\partial_j = \partial/\partial z_j$ and $\bar\partial_j = \partial/\partial\bar z_j$ acting on coefficients. Integration by parts gives $(\partial_j f, g) = -(f, \bar\partial_j g)$ for compactly supported functions, so $\partial^* = -\sum_j e_j^*\bar\partial_j$ and $\bar\partial^* = -\sum_j \bar e_j^*\partial_j$. These agree with $-{*}\bar\partial{*}$ and $-{*}\partial{*}$, because a differential operator is determined by its formal adjoint. Using the anticommutation relations,
$$\bar e_j^*e_j^*\bar e_k = -\bar e_j^*\bar e_ke_j^* = -(2\delta_{jk} - \bar e_k\bar e_j^*)e_j^*, \quad\text{so}\quad [\bar e_j^*e_j^*, \bar e_k] = -2\delta_{jk}e_j^*.$$
Hence $[\Lambda, \bar e_k] = ie_k^*$ and, since constant-coefficient operators commute with $\bar\partial_k$, $[\Lambda, \bar\partial] = i\sum_k e_k^*\bar\partial_k = -i\partial^*$.

Now let $(X, \omega)$ be Kähler and let $P = [\Lambda, \bar\partial] + i\partial^*$. In local coordinates, $\Lambda$ and $*$ have coefficients that are polynomials in the $h_{jk}$, their conjugates and $(\det(h_{jk}))^{-1}$, so $P$ is a differential operator of order at most $1$, and $(P\alpha)(x)$ depends only on the values and first derivatives at $x$ of $\alpha$ and of the $h_{jk}$. Choose normal coordinates at $x$ (Proposition P6.4.2). Then the $h_{jk}$ have the same value and first derivatives at $x$ as the flat metric, so $(P\alpha)(x)$ equals the value at $x$ of the flat operator applied to $\alpha$, which is $0$ by the computation on $\mathbb{C}^n$. As $x$ is arbitrary, $P = 0$.

Complex conjugation satisfies $\overline{\bar\partial\bar\alpha} = \partial\alpha$, $\overline{\Lambda\bar\alpha} = \Lambda\alpha$ and $\overline{\partial^*\bar\alpha} = \bar\partial^*\alpha$, since $*$ and $\Lambda$ are real. Conjugating $[\Lambda, \bar\partial]\bar\alpha = -i\partial^*\bar\alpha$ gives $[\Lambda, \partial]\alpha = i\bar\partial^*\alpha$. Taking formal adjoints, with $(AB)^* = B^*A^*$ and $L^* = \Lambda$, $[\Lambda, \bar\partial]^* = [\bar\partial^*, L]$ and $(-i\partial^*)^* = i\partial$, so $[\bar\partial^*, L] = i\partial$. In the same way $[\partial^*, L] = (i\bar\partial^*)^* = -i\bar\partial$.

(2) By part 1, $i(\partial\bar\partial^* + \bar\partial^*\partial) = \partial[\Lambda, \partial] + [\Lambda, \partial]\partial = \partial\Lambda\partial - \partial^2\Lambda + \Lambda\partial^2 - \partial\Lambda\partial = 0$, and $-i(\bar\partial\partial^* + \partial^*\bar\partial) = \bar\partial[\Lambda, \bar\partial] + [\Lambda, \bar\partial]\bar\partial = 0$ in the same way.

(3) Expanding $\Delta_d = (\partial + \bar\partial)(\partial^* + \bar\partial^*) + (\partial^* + \bar\partial^*)(\partial + \bar\partial)$ and using part 2 gives $\Delta_d = \Delta_\partial + \Delta_{\bar\partial}$. With $\partial^* = i[\Lambda, \bar\partial]$ and $\bar\partial^* = -i[\Lambda, \partial]$, and with $\partial\bar\partial = -\bar\partial\partial$,
$$\Delta_\partial = i(\partial\Lambda\bar\partial - \partial\bar\partial\Lambda + \Lambda\bar\partial\partial - \bar\partial\Lambda\partial), \qquad \Delta_{\bar\partial} = -i(\bar\partial\Lambda\partial - \bar\partial\partial\Lambda + \Lambda\partial\bar\partial - \partial\Lambda\bar\partial),$$
and the second expression equals the first term by term. So $\Delta_\partial = \Delta_{\bar\partial} = \frac12\Delta_d$.

(4) $\Delta_\partial$ commutes with $\partial$ and $\partial^*$, since $\partial\Delta_\partial = \partial\partial^*\partial = \Delta_\partial\partial$ and $\partial^*\Delta_\partial = \partial^*\partial\partial^* = \Delta_\partial\partial^*$. In the same way $\Delta_{\bar\partial}$ commutes with $\bar\partial$ and $\bar\partial^*$, and part 3 transfers all four to $\Delta_d$. The operator $\Delta_{\bar\partial}$ has type $(0,0)$. For $*$, let $\alpha$ have degree $k$. Using $d^* = -{*}d{*}$ and $** = (-1)^{\deg}$, both $*\Delta_d\alpha$ and $\Delta_d{*}\alpha$ equal $-{*}d{*}d{*}\alpha - (-1)^k d{*}d\alpha$. For $L$, $[L, d] = 0$ because $d\omega = 0$, and part 1 gives $[L, d^*] = [L, \partial^*] + [L, \bar\partial^*] = i\bar\partial - i\partial$. So
$$[L, \Delta_d] = d[L, d^*] + [L, d^*]d = i\big((\partial + \bar\partial)(\bar\partial - \partial) + (\bar\partial - \partial)(\partial + \bar\partial)\big) = 0,$$
using $\partial^2 = \bar\partial^2 = 0$ and $\partial\bar\partial + \bar\partial\partial = 0$. Finally $\Lambda = *^{-1}L*$ by Proposition P6.4.10, so $\Delta_d$ commutes with $\Lambda$. $\square$

### Exercises

1. (A) On $\mathbb{C}^2$ write $dz_1 \wedge d\bar z_1 = \frac12(dz_1 \wedge d\bar z_1 - dz_2 \wedge d\bar z_2) - i\omega_0$ and check that the first summand is primitive. Use Weil's formula to compute $*(dz_1 \wedge d\bar z_1)$, and check the answer against the basis computation of the examples.
2. (A) Show that $\dim P^k = \binom{2n}{k} - \binom{2n}{k-2}$ for $k \leq n$. For $n = 2$ list bases of $P^{1,1}$, $P^{2,0}$ and $P^{0,2}$.
3. (B) Prove directly from $\Lambda = *^{-1}L*$ that for $\alpha \in P^k$ the form $*L^{n-k}\alpha$ is primitive of degree $k$, and that $*$ maps $L^jP^k$ onto $L^{n-k-j}P^k$. Explain how Weil's formula refines this.
4. (B) On $\mathbb{C}^n$ with $\omega_0$, use the anticommutation relations of the proof to show $\Delta_{\bar\partial} = -2\sum_j \partial_j\bar\partial_j$ on each coefficient, and deduce $\Delta_d = 2\Delta_{\bar\partial}$ without the Kähler identities.
5. (B) Let $d^c = i(\bar\partial - \partial)$ on a complex manifold. Show that $d^c$ is real, that $dd^c = 2i\partial\bar\partial$, and that on a Kähler manifold the identities of Theorem P6.4.12, part 1, are equivalent to $[\Lambda, d] = -(d^c)^*$ together with their conjugates.
6. (C) Let $h$ be an arbitrary Hermitian metric on a complex manifold. Show that $P = [\Lambda, \bar\partial] + i\partial^*$ is of order $0$, that is, $\mathcal{A}_X$-linear, by comparing its first-order part at $x$ with the flat case in coordinates with $h_{jk}(x) = \delta_{jk}$. For the metric $e^{2x_1}\omega_0$ of the examples, compute $P(\beta)$ for every constant $(1,0)$-form $\beta$ on $\mathbb{C}^2$.

### Lean

Mathlib has exterior algebras, alternating maps, inner product spaces and the representation theory of Lie algebras in general form, including $\mathfrak{sl}_2$-triples. It has no Hodge star on complex inner product spaces, no Lefschetz operator and no formal adjoints of differential operators on manifolds, so none of the statements of this section is formalized. The handbook adds no `MinimalModel` node here.

### Notes and history

The decomposition of forms into primitive pieces goes back to Lefschetz's topological work and to Hodge (Hod41). Weil gave the linear algebra its present form in his book on Kähler manifolds (Wei58), including the formula for the star on primitive forms, and the formula is often called Weil's formula. The proof here, through the element $w = e^Le^{-\Lambda}e^L$, follows Huybrechts, Section 1.2 (Huy05), and Wells, Section V.3 (Wel80), which develop the $\mathfrak{sl}_2$ point of view. Signs in this subject vary between books with the normalization of the inner product on forms and the sign of $\Lambda$, and the explicit checks in the examples fix the conventions of this handbook. The Kähler identities are due to Hodge and to the school of Weil and Chern. The proof by normal coordinates is that of Griffiths and Harris, Section 0.7 (GH78), and Voisin, Section 6.1 (Voi02).
