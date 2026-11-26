---
title: Differentials of field extensions
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [Mat86:ch9, Eis95:ch16]
requires: [P1.1, P1.4, P1.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Differentials of field extensions

### Statement

Throughout, $K \subseteq L$ is a field extension and $p$ is the characteristic when it is positive. The module $\Omega_{L/K}$ is an $L$-vector space, and the section computes its dimension. For a field, every module is free, so the question is only about the dimension.

**Theorem P1.12.13 (finite separable extensions).** Let $L/K$ be a finite extension. Then $\Omega_{L/K} = 0$ if and only if $L/K$ is separable.

Lean: Mathlib `Algebra.FormallyUnramified.iff_isSeparable`, where `Algebra.FormallyUnramified K L` says that `Ω[L⁄K]` is a subsingleton (proved in Mathlib, for extensions that are essentially of finite type).

*Proof.* Let $L/K$ be separable. By the primitive element theorem $L = K(\alpha)$, so $L = K[x]/(g)$ with $g$ the minimal polynomial of $\alpha$. By Corollary P1.12.7, $\Omega_{L/K} = L\,dx / L\,g'(\alpha)\,dx$. Since $g$ is separable, $g'(\alpha) \neq 0$, so $\Omega_{L/K} = 0$.

Let $L/K$ be not separable, and let $K_s$ be the separable closure of $K$ in $L$. Then $K_s \neq L$, and $L/K_s$ is purely inseparable. The extension $L/K_s$ is finite, so there is an intermediate field $K_s \subseteq E \subsetneq L$ of maximal degree over $K_s$ among the proper intermediate fields. Take $\alpha \in L \setminus E$. Some power $\alpha^{p^e}$ lies in $E$, so there is a largest $j \geq 0$ with $\gamma = \alpha^{p^j} \notin E$, and then $\gamma^p \in E$. The field $E(\gamma)$ lies strictly between $E$ and $L$ or is equal to $L$, so $E(\gamma) = L$ by the choice of $E$. Put $a = \gamma^p$. In $L[x]$ the polynomial $x^p - a$ equals $(x - \gamma)^p$, so a monic factor in $E[x]$ of degree $m$ is $(x - \gamma)^m$, with constant term $\pm\gamma^m \in E$. If $0 < m < p$, then $\gamma \in E$, because $\gamma^p$ and $\gamma^m$ lie in $E$ and $\gcd(m, p) = 1$. So $x^p - a$ is irreducible over $E$, and $L = E[x]/(x^p - a)$. The derivative of $x^p - a$ is $0$, so $\Omega_{L/E} = L\,d\gamma \neq 0$. The first fundamental sequence for $K \to E \to L$ gives a surjection $\Omega_{L/K} \to \Omega_{L/E}$, so $\Omega_{L/K} \neq 0$. $\square$

**Theorem P1.12.14 (separably generated extensions).** Let $L/K$ be a finitely generated extension, and let $t_1, \dots, t_d \in L$ be algebraically independent over $K$ with $L/K(t_1, \dots, t_d)$ finite and separable. Then $dt_1, \dots, dt_d$ is a basis of the $L$-vector space $\Omega_{L/K}$. In particular $\dim_L \Omega_{L/K} = \operatorname{trdeg}_K L$.

Lean: not in Mathlib in this form. Mathlib has `KaehlerDifferential.mvPolynomialBasis` and `KaehlerDifferential.isLocalizedModule_of_isLocalizedModule` (proved in Mathlib), which give the case $L = K(t_1, \dots, t_d)$.

*Proof.* Let $F = K(t_1, \dots, t_d)$, the fraction field of the polynomial ring $K[t_1, \dots, t_d]$. By Propositions P1.12.4 and P1.12.8, $\Omega_{F/K}$ is the $F$-vector space with basis $dt_1, \dots, dt_d$. The first fundamental sequence for $K \to F \to L$ is
$$
L \otimes_F \Omega_{F/K} \xrightarrow{\ \alpha\ } \Omega_{L/K} \to \Omega_{L/F} \to 0 ,
$$
and $\Omega_{L/F} = 0$ by the last theorem, so $\alpha$ is surjective. For injectivity it is enough to show that every $K$-derivation $D : F \to M$ into an $L$-vector space $M$ extends to a $K$-derivation of $L$. Indeed, the dual of $\alpha$ is then surjective, by the universal property, and a linear map of vector spaces whose dual map is surjective for all $M$ is injective.

By the primitive element theorem $L = F(y)$, and $L = F[x]/(g)$ with $g = \sum_i c_i x^i$ the minimal polynomial of $y$, which is separable, so $g'(y) \neq 0$. Write $g^D(x) = \sum_i D(c_i) x^i$, with coefficients in $M$. For $v \in M$, the map $\tilde{D} : F[x] \to M$,
$$
\tilde{D}\Big( \sum_i a_i x^i \Big) = \sum_i D(a_i)\, y^i + \sum_i i\, a_i\, y^{i-1}\, v ,
$$
is a $K$-derivation, where $F[x]$ acts on $M$ through $x \mapsto y$. Its value on $g$ is $g^D(y) + g'(y)\,v$. Choose $v = -g^D(y)/g'(y)$. Then $\tilde{D}(g) = 0$, and $\tilde{D}(hg) = h(y)\tilde{D}(g) + g(y)\tilde{D}(h) = 0$ for every $h$, so $\tilde{D}$ factors through $L$ and extends $D$. $\square$

**Corollary P1.12.15 (the function field of an affine domain).** Let $k$ be a perfect field and $A = k[x_1, \dots, x_n]/(f_1, \dots, f_r)$ a domain of dimension $d$ with fraction field $K$. Let $J = (\partial f_j/\partial x_i)$, with entries in $K$. Then
$$
\Omega_{K/k} \cong K^n/\operatorname{row}(J), \qquad \dim_K \Omega_{K/k} = d, \qquad \operatorname{rank} J = n - d .
$$
So some $(n - d)$-minor of the Jacobian matrix is nonzero in $A$, that is, the ideal $J_A$ of Corollary P1.9.13 is not zero.

Lean: not in Mathlib.

*Proof.* By Corollary P1.12.7, $\Omega_{A/k}$ is the cokernel of the map $A^r \to A^n$ given by the transpose of $J$. Localization is exact and commutes with $\Omega$ (Section 12.1), so $\Omega_{K/k} = K \otimes_A \Omega_{A/k}$ is the quotient of $K^n$ by the span of the rows of $J$, and it has dimension $n - \operatorname{rank} J$. The field $K$ is finitely generated over the perfect field $k$, so it has a separating transcendence basis over $k$ (Matsumura, Chapter 9; Eisenbud, Chapter 16). Its transcendence degree is $\dim A = d$ by Theorem P1.4.31. By the theorem, $\dim_K \Omega_{K/k} = d$, so $\operatorname{rank} J = n - d$. A nonzero $(n-d)$-minor in $K$ is the image of the same minor computed in $A$, and $A \subseteq K$. $\square$

This keeps the promise of the sketch for $J_A \neq 0$ in Section 9.2, apart from the existence of a separating transcendence basis, which is cited.

**Theorem P1.12.16 (general extensions).** Let $L/K$ be a finitely generated field extension. Then $\dim_L \Omega_{L/K} \geq \operatorname{trdeg}_K L$, with equality if and only if $L/K$ is separably generated, that is, has a transcendence basis $t_1, \dots, t_d$ with $L/K(t_1, \dots, t_d)$ separable. If $K$ is perfect, every finitely generated extension is separably generated.

Lean: not in Mathlib.

*Proof sketch.* The direction "separably generated implies equality" is Theorem P1.12.14. For the rest, see Matsumura, Chapter 9, and Eisenbud, Chapter 16. $\square$

**Corollary P1.12.17 (differential test).** Let $L/K$ be finitely generated and $t_1, \dots, t_d \in L$ algebraically independent over $K$. Then $L/K(t_1, \dots, t_d)$ is finite and separable if and only if $dt_1, \dots, dt_d$ span $\Omega_{L/K}$.

Lean: not in Mathlib.

*Proof.* The direction "only if" is Theorem P1.12.14. Let the $dt_i$ span, and put $F = K(t_1, \dots, t_d)$. The first fundamental sequence for $K \to F \to L$ shows that $\Omega_{L/F}$ is the cokernel of $L \otimes_F \Omega_{F/K} \to \Omega_{L/K}$, and this map is surjective because its image contains the $dt_i$. So $\Omega_{L/F} = 0$. By Theorem P1.12.16, $\operatorname{trdeg}_F L \leq \dim_L \Omega_{L/F} = 0$, so $L/F$ is algebraic and finitely generated, hence finite. It is separable by Theorem P1.12.13. $\square$

### Proof in words

For a simple extension $K(\alpha) = K[x]/(g)$, the module of differentials is one copy of $L\,d\alpha$ modulo the relation $g'(\alpha)\,d\alpha = 0$. So it vanishes when $g$ is separable and is one dimensional when $g'$ is zero, which is the purely inseparable case $g = x^p - a$. A rational function field has the differentials $dt_i$ as a basis, and a finite separable extension adds no new differentials and kills none, because each derivation extends by the implicit function rule $dy = -g^D(y)/g'(y)$. So in the separably generated case the dimension of the differentials is the transcendence degree. Over a perfect field every function field is separably generated, and this gives the rank of the Jacobian matrix at the generic point.

### Examples

**Example P1.12.18 (a purely inseparable extension).** Let $K = \mathbb{F}_p(t)$ and $L = K(t^{1/p})$. With $\alpha = t^{1/p}$, $L = K[x]/(x^p - t)$ and $\Omega_{L/K} = L\,d\alpha$, of dimension $1$, while $\operatorname{trdeg}_K L = 0$. This is the field of Example P1.9.17, and it shows why the Jacobian criterion needs a separable residue field.

**Example P1.12.19 (a transcendence basis that is not separating).** Let $L = \mathbb{F}_p(x)$ and $K = \mathbb{F}_p$. Then $\Omega_{L/K} = L\,dx$ and $x$ is a separating transcendence basis. The element $x^p$ is also a transcendence basis, but $d(x^p) = p x^{p-1}\,dx = 0$, and $L/K(x^p)$ is purely inseparable of degree $p$. The differential test sees this.

**Example P1.12.20 (a finite extension that is not simple).** Let $K = \mathbb{F}_p(s, t)$ and $L = K(\alpha, \beta)$ with $\alpha^p = s$ and $\beta^p = t$. By the argument in the proof of Theorem P1.12.13, $x^p - s$ is irreducible over $K$, and $x^p - t$ is irreducible over $K(\alpha)$, since $t$ is not a $p$-th power in $K(\alpha) = \mathbb{F}_p(\alpha, t)$. So $L = K[x, y]/(x^p - s, y^p - t)$ has degree $p^2$. Both partial derivatives of both equations vanish, so $\Omega_{L/K} = L\,d\alpha \oplus L\,d\beta$ has dimension $2$. A simple extension $K(\gamma)$ has $\dim \Omega \leq 1$, since $d\gamma$ generates. So $L/K$ has no primitive element.

**Example P1.12.21 (an elliptic function field).** Let $k$ be a field of characteristic not $2$, and $K = k(x, y)$ with $y^2 = x^3 + x$. Then $\Omega_{K/k}$ is spanned by $dx$ and $dy$ with the relation $2y\,dy = (3x^2 + 1)\,dx$. Since $y \neq 0$ in $K$,
$$
dy = \frac{3x^2 + 1}{2y}\,dx ,
$$
and $\Omega_{K/k} = K\,dx$. The element $x$ is a separating transcendence basis: $K = k(x)[y]/(y^2 - x^3 - x)$, and $y^2 - x^3 - x$ is separable over $k(x)$ because its derivative $2y$ is nonzero. The differential $dx/y$ is the invariant differential of the elliptic curve, which has no zeros and no poles on the projective curve.

### Exercises

1. (A) Show that $\Omega_{L/\mathbb{Q}} = 0$ for $L = \mathbb{Q}(\sqrt{2}, \sqrt{3})$, both with Theorem P1.12.13 and by a direct computation from a presentation with two generators.
2. (A) Let $K = \mathbb{F}_p(t)$ and $L = K(t^{1/p^2})$. Compute $\Omega_{L/K}$ and show that it has dimension $1$.
3. (A) Let $K$ have characteristic $0$ and $L/K$ be finitely generated. Show that every transcendence basis of $L/K$ is separating and that $\dim_L \Omega_{L/K} = \operatorname{trdeg}_K L$.
4. (B) Let $L/K$ be a separable algebraic extension that need not be finite. Show that $\Omega_{L/K} = 0$. (Hint: each $\alpha \in L$ satisfies $g'(\alpha)\,d\alpha = 0$ for its minimal polynomial $g$.)
5. (B) Let $K = \mathbb{F}_p(t_1, \dots, t_n)$ and $L = K(t_1^{1/p}, \dots, t_n^{1/p})$. Show that $[L : K] = p^n$ and $\dim_L \Omega_{L/K} = n$.
6. (B) Let $k$ have characteristic not $2$ or $3$, and $K = k(x, y)$ with $y^2 = x^3 + ax + b$, where $4a^3 + 27b^2 \neq 0$. Show that $dx/(2y) = dy/(3x^2 + a)$ in $\Omega_{K/k}$, and that $x$ and $y$ are both separating transcendence bases of $K/k$.
7. (C) Let $L/K$ be an extension in characteristic $p$. Show that every $K$-derivation of $L$ kills $L^p$, so that $\Omega_{L/K} = \Omega_{L/K(L^p)}$, where $K(L^p)$ is the subfield generated by $K$ and $L^p$. Deduce that $\Omega_{L/K} = 0$ if $L = K(L^p)$.
8. (C) Let $L/K$ be finite in characteristic $p$. Show that $L/K$ is separable if and only if $L = K(L^p)$. With Exercise 7 and Theorem P1.12.13, this gives a second proof that $\Omega_{L/K} = 0$ for $L/K$ finite separable.

### Lean

Mathlib calls an algebra formally unramified, `Algebra.FormallyUnramified`, when its module of differentials is a subsingleton, and proves `Algebra.FormallyUnramified.iff_isSeparable`: a field extension that is essentially of finite type is formally unramified if and only if it is separable. The étale version is `Algebra.FormallyEtale.iff_isSeparable`. The theorem on separably generated extensions and the inequality $\dim_L \Omega_{L/K} \geq \operatorname{trdeg}_K L$ are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

Separating transcendence bases go back to Steinitz's algebraic theory of fields of 1910. MacLane studied separability for extensions that are not algebraic in 1939, and Teichmüller and Jacobson used $p$-bases and derivations to study inseparable extensions in characteristic $p$. The literature state of every result here is theorem. The section follows Matsumura, Chapter 9, and Eisenbud, Chapter 16.
