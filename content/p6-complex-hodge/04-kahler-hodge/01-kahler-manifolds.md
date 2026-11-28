---
title: Kähler manifolds
nodes: []
sources: [Huy05, Voi02, GH78, Wel80, Kah33, BT82]
reads_with: [Huy05:3.1, Voi02:3.1, GH78:0.7, Wel80:V.4]
requires: [P6.1, P6.2, P6.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Kähler manifolds

### Statement

Throughout the chapter a Hermitian metric $h$ on a complex manifold $X$ of dimension $n$ is written in local holomorphic coordinates as in Definition P6.3.5: with $h_{jk} = h(\partial/\partial z_j, \partial/\partial z_k)$, the fundamental form is
$$\omega = \frac{i}{2} \sum_{j,k} h_{jk}\, dz_j \wedge d\bar z_k,$$
a real positive $(1,1)$-form, and $\omega$ determines $h$ (Proposition P6.3.4). The flat metric $h_{jk} = \delta_{jk}$ has fundamental form $\omega_0 = \frac{i}{2} \sum_j dz_j \wedge d\bar z_j = \sum_j dx_j \wedge dy_j$.

**Definition P6.4.1 (Kähler manifolds).** A Hermitian metric on a complex manifold $X$ is *Kähler* if its fundamental form $\omega$ is closed, $d\omega = 0$. Its fundamental form is then called a *Kähler form*. A *Kähler manifold* is a complex manifold together with a Kähler metric. A complex manifold is *of Kähler type* if it admits some Kähler metric. For a Kähler form $\omega$ the de Rham class $[\omega] \in H^2(X, \mathbb{R})$ is the *Kähler class*.

By Proposition P6.3.4, part 3, a Kähler metric is the same thing as a closed real $(1,1)$-form that is positive at every point. Since $\omega$ is real and $d\omega = \partial\omega + \bar\partial\omega$ with the two terms of types $(2,1)$ and $(1,2)$, the conditions $d\omega = 0$, $\partial\omega = 0$ and $\bar\partial\omega = 0$ are equivalent, as $\bar\partial\omega = \overline{\partial\omega}$.

**Proposition P6.4.2 (characterizations of the Kähler condition).** Let $h$ be a Hermitian metric on a complex manifold $X$ with fundamental form $\omega$. The following are equivalent.

1. $d\omega = 0$.
2. Every point of $X$ has an open neighbourhood $U$ and a smooth real function $\varphi$ on $U$ with $\omega|_U = i\partial\bar\partial\varphi$.
3. Every point $x \in X$ has holomorphic coordinates $z_1, \dots, z_n$ centred at $x$ in which $h_{jk} = \delta_{jk} + O(|z|^2)$, that is, $h_{jk}(0) = \delta_{jk}$ and all first partial derivatives of the $h_{jk}$ vanish at $0$.

Coordinates as in part 3 are *normal coordinates* at $x$. The function $\varphi$ of part 2 is a *local potential*.

Lean: not yet in Lean.

**Example P6.4.3 (first Kähler manifolds).** Each of the following is Kähler, and in each case closedness is checked directly.

1. $\mathbb{C}^n$ with $\omega_0$. The coefficients are constant, so $d\omega_0 = 0$. A global potential is $\varphi = \frac12 |z|^2$: $i\partial\bar\partial(\frac12 \sum_j z_j \bar z_j) = \frac{i}{2} \sum_j dz_j \wedge d\bar z_j = \omega_0$. The linear coordinates are normal at every point.
2. A complex torus $X = \mathbb{C}^n/\Lambda$ (Example P6.2.3). The transition maps are translations, which preserve $\omega_0$, so $\omega_0$ descends to a Kähler form on $X$ with constant coefficients in every chart. Its volume is $\int_X \omega_0^n/n! = \operatorname{vol}(\mathbb{C}^n/\Lambda) = |\det(\lambda_1, \dots, \lambda_{2n})|$ in real coordinates. For $E_\tau = \mathbb{C}/(\mathbb{Z} + \mathbb{Z}\tau)$ this is $\int_{E_\tau} \omega_0 = \operatorname{Im}\tau$.
3. A Riemann surface $X$, that is, a complex manifold of dimension $1$. It has a Hermitian metric by Proposition P6.3.6, and every such metric is Kähler, because $d\omega$ is a $3$-form on a real surface and so is $0$.
4. $\mathbb{P}^n$ with the Fubini-Study form $\omega_{FS} = \frac{i}{2\pi}\partial\bar\partial \log \|Z\|^2$ of Example P6.3.8, which is real, closed and positive. In the chart $U_0$ with $z_j = Z_j/Z_0$, $\omega_{FS} = \frac{i}{2\pi}\partial\bar\partial\log(1 + |z|^2)$, and
$$\partial\bar\partial \log(1 + |z|^2) = \sum_{j,k} \Big( \frac{\delta_{jk}}{1 + |z|^2} - \frac{\bar z_j z_k}{(1 + |z|^2)^2} \Big) dz_j \wedge d\bar z_k,$$
so $h_{jk} = \frac{1}{\pi}(\delta_{jk} + O(|z|^2))$. In the coordinates $w = z/\sqrt{\pi}$ one has $dz_j \wedge d\bar z_k = \pi\, dw_j \wedge d\bar w_k$, so the coefficients become $\pi h_{jk} = \delta_{jk} + O(|w|^2)$, and $w$ is a system of normal coordinates at $[1 : 0 : \dots : 0]$. The unitary group $U(n+1)$ acts transitively on $\mathbb{P}^n$ and preserves $\|Z\|^2$, hence $\omega_{FS}$, so the same holds at every point. For $n = 1$, with $z = re^{i\theta}$, $\omega_{FS} = \frac{1}{\pi}(1 + r^2)^{-2}\, dx \wedge dy$ and $\int_{\mathbb{P}^1} \omega_{FS} = \frac{1}{\pi} \cdot 2\pi \int_0^\infty r(1 + r^2)^{-2}\, dr = 1$.

**Proposition P6.4.4 (submanifolds and products).** Let $(X, \omega)$ be a Kähler manifold.

1. If $Y \subseteq X$ is a complex submanifold with inclusion $\iota$, then $\iota^*\omega$ is a Kähler form on $Y$, and it is the fundamental form of the restricted metric $h|_{T^{1,0}Y}$. More generally, $f^*\omega$ is a Kähler form for every holomorphic map $f \colon Y \to X$ whose differential is injective at every point.
2. If $(X', \omega')$ is another Kähler manifold, with projections $p \colon X \times X' \to X$ and $p' \colon X \times X' \to X'$, then $p^*\omega + p'^*\omega'$ is a Kähler form on $X \times X'$.
3. Every complex submanifold of $\mathbb{P}^N$ is Kähler, with Kähler form $\omega_{FS}|_Y$. In particular every smooth projective hypersurface (Proposition P6.2.6) is Kähler.

Lean: not yet in Lean.

**Proposition P6.4.5 (volumes and powers of the Kähler class).** Let $(X, \omega)$ be a compact Kähler manifold of dimension $n$, nonempty.

1. For every compact complex submanifold $Y \subseteq X$ of dimension $d$ (connected or not, of pure dimension $d$),
$$\int_Y \omega^d = d! \operatorname{vol}(Y) > 0,$$
where $\operatorname{vol}(Y)$ is the Riemannian volume of $Y$ for the restricted metric. In particular $\int_X \omega^n = n! \operatorname{vol}(X) > 0$.
2. For $0 \leq k \leq n$ the class $[\omega]^k = [\omega^k] \in H^{2k}(X, \mathbb{R})$ is nonzero. Hence $b_{2k}(X) \geq 1$ for $0 \leq k \leq n$.
3. For $Y$ as in part 1, the linear form $H^{2d}(X, \mathbb{R}) \to \mathbb{R}$, $[\beta] \mapsto \int_Y \beta$, is well defined and nonzero, since it takes the value $\int_Y \omega^d > 0$ on $[\omega]^d$. In particular, $Y$ is not the boundary of any compact oriented real submanifold of dimension $2d + 1$ with boundary.

Lean: not yet in Lean.

### Proof in words

A closed real $(1,1)$-form is locally $i\partial\bar\partial\varphi$ by the local $\partial\bar\partial$-lemma of Chapter 1, and conversely $i\partial\bar\partial\varphi$ is closed because $d\partial\bar\partial = 0$. Normal coordinates come from a holomorphic change of coordinates with quadratic terms, which can be chosen to remove the first-order part of the metric. Closedness is exactly the symmetry that makes this possible: the first derivatives $\partial h_{jk}/\partial z_l$ must be symmetric in $j$ and $l$, and a quadratic change of coordinates can only cancel symmetric first-order terms. In normal coordinates a Kähler metric agrees with the flat metric to first order at the chosen point. So any identity between first-order operators that holds on $\mathbb{C}^n$ also holds on a Kähler manifold, and Section 4.2 uses this for the Kähler identities.

Pullback by a holomorphic immersion keeps a form of type $(1,1)$, closed and positive. So complex submanifolds of a Kähler manifold are Kähler. Projective space is Kähler with the Fubini-Study form, and therefore every projective manifold is Kähler. Products are Kähler with the sum of the pulled-back forms.

The volume statement is Wirtinger's formula: $\omega^d/d!$ restricted to a complex submanifold is its volume form. If $\omega^k$ were exact, then $\omega^n = \omega^k \wedge \omega^{n-k}$ would be exact, and Stokes would give $\int_X \omega^n = 0$. This contradicts positivity of the volume. So a compact Kähler manifold has nonzero even Betti numbers up to degree $2n$. The Hopf surface has $b_2 = 0$, so it carries no Kähler metric, although it carries a Hermitian metric and, as Exercise 4 shows, a closed semipositive $(1,1)$-form.

### Examples

A Hermitian metric need not be Kähler. On $\mathbb{C}^2$ let $\omega = \frac{i}{2}(dz_1 \wedge d\bar z_1 + (1 + |z_1|^2)\, dz_2 \wedge d\bar z_2)$. It is positive, and
$$d\omega = \frac{i}{2}(\bar z_1\, dz_1 + z_1\, d\bar z_1) \wedge dz_2 \wedge d\bar z_2,$$
which is nonzero wherever $z_1 \neq 0$. This metric has no normal coordinates at such points, and no local potential.

**Example P6.4.6 (the Hopf surface is not Kähler).** Let $X = (\mathbb{C}^2 \setminus \{0\})/\langle z \mapsto 2z \rangle$ be the Hopf surface of Example P6.2.4, a compact connected complex surface with $b_2(X) = 0$. By Proposition P6.4.5, part 2, a Kähler surface has $b_2 \geq 1$, so $X$ admits no Kähler metric. Concretely, if $\omega$ were a Kähler form on $X$, then $[\omega] \in H^2(X, \mathbb{R}) = 0$, so $\omega = d\eta$, $\omega^2 = d(\eta \wedge \omega)$, and $\int_X \omega^2 = 0$ by Stokes, while $\int_X \omega^2 = 2\operatorname{vol}(X) > 0$.

The surface does carry Hermitian metrics. The form $\omega_H = \frac{i}{2} |z|^{-2} \sum_j dz_j \wedge d\bar z_j$ on $\mathbb{C}^2 \setminus \{0\}$ is positive and invariant under $z \mapsto 2z$, since $dz_j \wedge d\bar z_j$ is multiplied by $4$ and $|z|^{-2}$ by $\frac14$, so it descends to $X$. It is not closed:
$$d\omega_H = -|z|^{-4} \sum_l (\bar z_l\, dz_l + z_l\, d\bar z_l) \wedge \omega_0,$$
which at $z = (1, 0)$ equals $-\frac{i}{2}(dz_1 + d\bar z_1) \wedge dz_2 \wedge d\bar z_2 \neq 0$. The image $E$ of the punctured line $\{z_2 = 0\}$ is a compact complex curve in $X$, the elliptic curve $\mathbb{C}^*/2^{\mathbb{Z}}$. Since $H^2(X, \mathbb{R}) = 0$, every closed $2$-form on $X$ is exact and so integrates to $0$ over $E$. Proposition P6.4.5, part 3, therefore gives a second reason why $X$ is not Kähler.

### Proof

*Proposition P6.4.2.* (1) implies (2). Let $x \in X$ and choose a chart around $x$ whose image is a polydisc $D$. On $D$ the form $\omega$ is a real $d$-closed $(1,1)$-form, so by Corollary P6.1.38 there is a smooth real $\varphi$ on $D$ with $\omega = i\partial\bar\partial\varphi$.

(2) implies (1). By Proposition P6.1.33, $\partial^2 = 0$, $\bar\partial^2 = 0$ and $\partial\bar\partial = -\bar\partial\partial$, so $d(i\partial\bar\partial\varphi) = i\partial\partial\bar\partial\varphi + i\bar\partial\partial\bar\partial\varphi = 0 - i\partial\bar\partial\bar\partial\varphi = 0$.

(3) implies (1). In normal coordinates at $x$, $d\omega = \frac{i}{2}\sum_{j,k} dh_{jk} \wedge dz_j \wedge d\bar z_k$ vanishes at $x$, since $dh_{jk}(x) = 0$. As $x$ is arbitrary, $d\omega = 0$.

(1) implies (3). Fix $x$ and holomorphic coordinates $z$ centred at $x$. A complex linear change of coordinates replaces the matrix $H(0) = (h_{jk}(0))$ by $A^{T} H(0) \bar A$ for an invertible matrix $A$. Choosing the columns of $A$ to be the coordinate vectors of a unitary basis of $(T^{1,0}_x X, h_x)$ gives $h_{jk}(0) = \delta_{jk}$. Write
$$a_{jkl} = \frac{\partial h_{jk}}{\partial z_l}(0).$$
Since $h_{kj} = \overline{h_{jk}}$, also $\frac{\partial h_{jk}}{\partial \bar z_l}(0) = \overline{a_{kjl}}$, so $h_{jk} = \delta_{jk} + \sum_l (a_{jkl} z_l + \overline{a_{kjl}}\, \bar z_l) + O(|z|^2)$. The $(2,1)$-part of $d\omega$ is $\partial\omega = \frac{i}{2} \sum_{j,k,l} \frac{\partial h_{jk}}{\partial z_l} dz_l \wedge dz_j \wedge d\bar z_k$, and its vanishing at $0$ says that $a_{jkl} = a_{lkj}$ for all $j, k, l$. Define new coordinates
$$w_k = z_k + \frac12 \sum_{j,l} a_{jkl} z_j z_l, \qquad k = 1, \dots, n.$$
The Jacobian at $0$ is the identity, so this is a holomorphic change of coordinates near $0$ (Theorem P6.1.10). Using the symmetry of $a_{jkl}$ in $j$ and $l$, $dw_k = dz_k + \sum_{j,l} a_{jkl} z_l\, dz_j$, hence $dz_k = dw_k - \sum_{j,l} a_{jkl} w_l\, dw_j + O(|w|^2)$ and $z = w + O(|w|^2)$. Substituting and discarding terms of order $2$,
$$\sum_{j,k} h_{jk}\, dz_j \wedge d\bar z_k = \sum_k dw_k \wedge d\bar w_k + \sum_{j,k,l} \big(a_{jkl} w_l + \overline{a_{kjl}}\, \bar w_l\big) dw_j \wedge d\bar w_k - \sum_{j,k,l} a_{jkl} w_l\, dw_j \wedge d\bar w_k - \sum_{j,k,l} \overline{a_{kjl}}\, \bar w_l\, dw_j \wedge d\bar w_k + O(|w|^2).$$
Here the last sum comes from $dw_j \wedge \overline{(-\sum_{m,l} a_{mkl} w_l dw_m)}$ after renaming indices. The two middle sums cancel the first-order terms, so in the coordinates $w$ the coefficients are $\delta_{jk} + O(|w|^2)$.

*Proposition P6.4.4.* (1) Let $f \colon Y \to X$ be holomorphic with injective differential. Pullback by a holomorphic map preserves type and commutes with $d$ (Proposition P6.1.33), so $f^*\omega$ is a closed real $(1,1)$-form. At $y \in Y$, for a nonzero real tangent vector $v$, $f_*v \neq 0$ and $f_*(Jv) = J f_* v$, so $(f^*\omega)(v, Jv) = \omega(f_*v, Jf_*v) > 0$ by Proposition P6.3.4, part 3. Hence $f^*\omega$ is positive. For the inclusion of a submanifold, $\iota^*\omega(u, v) = g(Ju, v)$ for $u, v \in T_yY$, which is the fundamental form of $g|_{T_yY}$, the real part of $h|_{T^{1,0}Y}$.

(2) The form $p^*\omega + p'^*\omega'$ is closed, real and of type $(1,1)$. In product coordinates $(z, z')$ its matrix is block diagonal with blocks $(h_{jk}(z))$ and $(h'_{jk}(z'))$, which is positive definite.

(3) The form $\omega_{FS}$ is a Kähler form on $\mathbb{P}^N$ by Example P6.4.3, part 4, and part 1 applies.

*Proposition P6.4.5.* (1) Let $Y$ have dimension $d$ and let $\omega_Y = \iota^*\omega$, the fundamental form of the restricted metric by Proposition P6.4.4. By Proposition P6.3.2, part 3, applied in each tangent space of $Y$, $\omega_Y^d/d!$ is the Riemannian volume form of $Y$ for its complex orientation. So $\int_Y \omega^d = \int_Y \omega_Y^d = d!\operatorname{vol}(Y)$, which is positive since $Y$ is nonempty and of pure dimension $d$.

(2) Suppose $\omega^k = d\eta$ for some $k \leq n$. Then $\omega^n = d\eta \wedge \omega^{n-k} = d(\eta \wedge \omega^{n-k})$, since $d\omega = 0$. By Stokes on the compact manifold $X$ without boundary, $\int_X \omega^n = 0$, which contradicts part 1 with $Y = X$. So $[\omega]^k \neq 0$ and $b_{2k}(X) \geq 1$.

(3) If $\beta = d\gamma$ is exact, then $\int_Y \beta = \int_Y d(\iota^*\gamma) = 0$ by Stokes on $Y$, so the linear form is well defined on de Rham classes. Its value on $[\omega^d]$ is positive by part 1. If $Y = \partial M$ for a compact oriented manifold $M \subseteq X$ of dimension $2d + 1$, then Stokes gives $\int_Y \omega^d = \int_M d(\omega^d) = 0$, a contradiction. $\square$

### Exercises

1. (A) On $\mathbb{C}$ let $\omega = \frac{i}{2\pi}\partial\bar\partial\log(1 + |z|^2)$. Show that $\omega = \frac{1}{\pi}(1 + |z|^2)^{-2}\, dx \wedge dy$, that it is positive, and that $\int_{\mathbb{C}} \omega = 1$. Explain why this is the volume of $\mathbb{P}^1$ for $\omega_{FS}$ although $\mathbb{C}$ is not compact.
2. (A) Let $U \subseteq \mathbb{C}^n$ be open and connected and $u$ a smooth real function on $U$. Show that $e^{2u}\omega_0$ is a Kähler form if $n = 1$, and that for $n \geq 2$ it is Kähler if and only if $u$ is constant. Use that $du \wedge \omega_0 = 0$ forces $du = 0$ when $n \geq 2$.
3. (B) Let $Y \subseteq \mathbb{C}^N$ be a compact complex submanifold. Use the global potential $\omega_0 = i\partial\bar\partial(\frac12|z|^2)$ and Proposition P6.4.5, part 1, to show that $Y$ is a finite set. Compare with Corollary P6.2.8.
4. (B) On $\mathbb{C}^2 \setminus \{0\}$ let $\beta = i\partial\bar\partial\log|z|^2$. Show that $\beta$ is closed, real and invariant under $z \mapsto 2z$, so that it descends to the Hopf surface. Compute its matrix and show that it is semipositive of rank $1$ at every point, with kernel spanned by the radial vector $z$. Explain why this does not contradict Example P6.4.6.
5. (B) For $n \geq 2$ let $X_n = (\mathbb{C}^n \setminus \{0\})/\langle z \mapsto 2z\rangle$. Show as in Example P6.2.4 that $X_n$ is diffeomorphic to $S^1 \times S^{2n-1}$ and, using the Künneth formula and the cohomology of spheres (BT82, Chapter I), that $b_2(X_n) = 0$. Deduce that $X_n$ is not Kähler. For $n = 1$ show that $X_1$ is the elliptic curve $\mathbb{C}/(2\pi i\mathbb{Z} + \mathbb{Z}\log 2)$, which is Kähler.
6. (C) Let $\omega = \frac{i}{2} h\, dz \wedge d\bar z$ be a Hermitian metric on a disc around $0$ in $\mathbb{C}$. Show that under a holomorphic change of coordinate $w = w(z)$ the coefficient becomes $h_w = h\, |dz/dw|^2$, and deduce that $|dz/dw|^{-2} \partial_w\partial_{\bar w}\log h_w = \partial_z\partial_{\bar z}\log h$ away from zeros of $dw/dz$. For $\omega_{FS}$ in the normal coordinate $w = z/\sqrt{\pi}$ of Example P6.4.3, compute $\partial_w\partial_{\bar w}\log h_w(0) = -2\pi$. Conclude that no holomorphic coordinate centred at $0$ gives $h = 1 + O(|w|^3)$, so normal coordinates cannot be improved to third order in general.

### Lean

Mathlib has smooth manifolds, differential forms on normed spaces and Riemannian metrics in development, and it has complex manifolds as charted spaces with holomorphic transition maps. It has no Hermitian metrics on complex manifolds, no Kähler forms and no Fubini-Study metric. The handbook adds no `MinimalModel` node here.

### Notes and history

Kähler introduced the condition $d\omega = 0$ in 1933 (Kah33), noting the local potential and the resulting simplifications of curvature; the name and the systematic use came with Weil and Chern in the 1940s and 1950s. Hodge had already used the Fubini-Study metric on projective manifolds in his work on harmonic integrals (Hod41), and Proposition P6.4.4 is the reason Hodge theory applies to every smooth projective variety. Normal coordinates as in Proposition P6.4.2 are in Griffiths and Harris, Section 0.7 (GH78), and Huybrechts, Section 3.1 (Huy05). The Hopf surface is the standard compact complex manifold that is not Kähler. Every compact complex surface with even $b_1$ is Kähler, a theorem of Kodaira, Miyaoka and Siu, so for surfaces the parity of $b_1$, which Section 4.3 proves necessary, is also sufficient. In higher dimensions no topological criterion is known.
