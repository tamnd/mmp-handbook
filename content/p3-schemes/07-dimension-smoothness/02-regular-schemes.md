---
title: Tangent spaces and regular schemes
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch12, Har77:I.5, GW20:ch6]
requires: [P1.5, P1.7, P1.9, P3.1, P3.2, P3.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Tangent spaces and regular schemes

### Statement

**Definition P3.7.12 (tangent space, regular point).** Let $X$ be a scheme and $x \in X$, with local ring $(\mathcal{O}_{X, x}, \mathfrak{m}_x)$ and residue field $\kappa(x)$.

1. The *Zariski cotangent space* of $X$ at $x$ is the $\kappa(x)$-vector space $\mathfrak{m}_x/\mathfrak{m}_x^2$, and the *Zariski tangent space* is its dual $T_x X = \operatorname{Hom}_{\kappa(x)}(\mathfrak{m}_x/\mathfrak{m}_x^2, \kappa(x))$.
2. The point $x$ is *regular* if $\mathcal{O}_{X, x}$ is a Noetherian regular local ring (Definition P1.9.1), that is, if $\dim_{\kappa(x)} \mathfrak{m}_x/\mathfrak{m}_x^2 = \dim \mathcal{O}_{X, x}$. Otherwise $x$ is *singular*.
3. A scheme $X$ is *regular* if it is locally Noetherian and every point is regular. It is *regular in codimension one*, or satisfies $R_1$, if every point $x$ with $\dim \mathcal{O}_{X, x} \leq 1$ is regular.

Lean: Mathlib `IsLocalRing.CotangentSpace`, `IsRegularLocalRing` and `IsRegularRing` (definitions). There is no regular scheme in Mathlib; it is not in Lean as stated.

**Proposition P3.7.13 (tangent vectors as morphisms).** Let $X$ be a scheme over a field $k$, and let $x \in X$ be a point with $\kappa(x) = k$. Let $k[\varepsilon] = k[t]/(t^2)$. Then the $k$-morphisms $v \colon \operatorname{Spec} k[\varepsilon] \to X$ that map the point to $x$ are in natural bijection with the vectors of $T_x X$. If $f \colon X \to Y$ is a $k$-morphism, composition with $f$ is a $k$-linear map $df_x \colon T_x X \to T_{f(x)} Y$, dual to the map $\mathfrak{m}_{f(x)}/\mathfrak{m}_{f(x)}^2 \to \mathfrak{m}_x/\mathfrak{m}_x^2$ induced by $f^\#$.

Lean: not in Lean as stated.

**Proposition P3.7.14 (the tangent space of an affine scheme).** Let $X = \operatorname{Spec} k[x_1, \dots, x_n]/(f_1, \dots, f_r)$ and let $p = (a_1, \dots, a_n) \in k^n$ be a point of $X$, the maximal ideal $(x_1 - a_1, \dots, x_n - a_n)$. Let $J(p) = (\partial f_j/\partial x_i (p))$ be the $r \times n$ Jacobian matrix at $p$. Then
$$T_p X \cong \ker\big(J(p) \colon k^n \to k^r\big), \qquad \dim_k T_p X = n - \operatorname{rank} J(p).$$

Lean: not in Lean as stated.

**Proposition P3.7.15 (first properties of regular points).** Let $X$ be a locally Noetherian scheme.

1. For every $x \in X$, $\dim_{\kappa(x)} \mathfrak{m}_x/\mathfrak{m}_x^2 \geq \dim \mathcal{O}_{X, x}$.
2. A regular point lies on exactly one irreducible component of $X$, and $X$ is reduced at it: $\mathcal{O}_{X, x}$ is a domain.
3. If $x$ is regular and $x'$ is a generization of $x$, that is, $x \in \overline{\{x'\}}$, then $x'$ is regular.
4. If $X$ is locally of finite type over a field, then $X$ is regular if and only if every closed point is regular.
5. If $X$ is integral of dimension $1$, then $X$ is regular if and only if $\mathcal{O}_{X, x}$ is a discrete valuation ring for every closed point $x$.

Lean: Mathlib `IsRegularLocalRing.iff_finrank_cotangentSpace` for the definition in terms of the cotangent space, the instance that a local principal ideal domain is a regular local ring, and the instance that a Dedekind domain is a regular ring (proved in Mathlib). The algebraic input of part 3, that localizations of regular local rings are regular, is listed in Mathlib as a TODO. The statements for schemes are not in Lean as stated.

### Proof in words

A tangent vector at a rational point is a first order path: a morphism from the scheme with one point and one infinitesimal direction. On functions it is $a \mapsto a(x) + D(a) \varepsilon$, and $D$ is a derivation at $x$, which is a linear form on $\mathfrak{m}_x/\mathfrak{m}_x^2$. In coordinates the cotangent space of a polynomial ring at $p$ is free on the $dx_i$, and each equation $f_j$ contributes the relation $df_j(p)$, its linear part, which is a row of the Jacobian matrix. Regularity says that the tangent space is as small as the dimension allows, and the algebra of P1 Ch. 9 makes it a domain and stable under localization. Since every point of a scheme of finite type over a field specializes to a closed point, regularity can be tested at closed points.

### Examples

**Example P3.7.16 (affine and projective space).** At a rational point $p$ of $\mathbb{A}^n_k$ the Jacobian matrix is empty, so $T_p \mathbb{A}^n_k = k^n$, and $\dim \mathcal{O}_{\mathbb{A}^n, p} = n$ by Theorem P3.7.4. At a closed point with any residue field, $k[x_1, \dots, x_n]_\mathfrak{m}$ is regular by Example P1.9.6. So $\mathbb{A}^n_k$ is regular by part 4 of Proposition P3.7.15, and so is $\mathbb{P}^n_k$, which is covered by copies of $\mathbb{A}^n_k$. The same holds for $\mathbb{A}^n_\mathbb{Z}$ and $\mathbb{P}^n_\mathbb{Z}$, since polynomial rings over a regular ring are regular (Mathlib `MvPolynomial.isRegularRing_of_isRegularRing`).

**Example P3.7.17 (the node and the cusp).** Let $X = V(y^2 - x^2(x + 1))$ and $X' = V(y^2 - x^3)$ in $\mathbb{A}^2_k$. Both are integral curves, by Example P3.2.17 and Example P3.3.15. For $f = y^2 - x^2 - x^3$, $J = (-2x - 3x^2, \ 2y)$, which vanishes at the origin, so $\dim T_0 X = 2 > 1$ and the origin is singular. For $f' = y^2 - x^3$, $J = (-3x^2, \ 2y)$ also vanishes at the origin. The two tangent spaces have the same dimension, but the quadratic parts of the equations, $y^2 - x^2 = (y - x)(y + x)$ and $y^2$, distinguish them: the node has two branches with distinct tangent lines and the cusp has one. P1 Example P1.6.30 and Example P1.6.31 make this precise in the completion.

**Example P3.7.18 (the quadric cone).** Let $X = V(xy - z^2) \subseteq \mathbb{A}^3_k$. At the origin $J = (y, x, -2z) = 0$, so $\dim T_0 X = 3 > 2 = \dim X$, and the vertex is singular. At a rational point $p \neq 0$ of $X$ the row $J(p)$ is not zero: if $x = y = 0$ at $p$, then $z^2 = 0$, so $p = 0$. So $\dim T_p X = 2$ and $p$ is regular. This is the simplest surface singularity of the minimal model program, the $A_1$ singularity. It is canonical and not terminal, and for $\operatorname{char} k \neq 2$ it is the quotient of $\mathbb{A}^2_k$ by $\{\pm 1\}$, via $x = s^2$, $y = t^2$, $z = st$.

**Example P3.7.19 (non-reduced points).** Let $X = \operatorname{Spec} k[\varepsilon]$. Its one point has $\mathfrak{m} = (\varepsilon)$, $\mathfrak{m}^2 = 0$, so $\dim T X = 1$ while $\dim X = 0$. So $X$ is not regular, as part 2 of Proposition P3.7.15 predicts. The scheme $V(y^2) \subseteq \mathbb{A}^2_k$, the doubled line, has tangent space of dimension $2$ at every rational point and dimension $1$: it is singular everywhere. Its reduced subscheme, the line, is regular.

**Example P3.7.20 (an arithmetic singular point).** Let $A = \mathbb{Z}[\sqrt{-3}] = \mathbb{Z}[x]/(x^2 + 3)$ and $\mathfrak{m} = (2, x + 1)$. Then $A/\mathfrak{m} = \mathbb{F}_2$, so $\mathfrak{m}$ is maximal, of height $1$ as $\dim A = 1$. In $\mathbb{Z}[x]$, with $\mathfrak{M} = (2, x + 1)$,
$$x^2 + 3 = (x + 1)^2 - 2(x + 1) + 4 \in \mathfrak{M}^2,$$
so $\mathfrak{m}/\mathfrak{m}^2 = \mathfrak{M}/\mathfrak{M}^2$, which has dimension $2$ over $\mathbb{F}_2$, with basis the classes of $2$ and $x + 1$. So $\operatorname{Spec} A$ is singular at $\mathfrak{m}$, and $A_\mathfrak{m}$ is not a discrete valuation ring. The ring $\mathbb{Z}[\omega]$ with $\omega = (1 + \sqrt{-3})/2$ is its normalization, and it is regular (Section 7.4).

### Proof

*Proof of Proposition P3.7.13.* The scheme $\operatorname{Spec} k[\varepsilon]$ has one point. A morphism $v$ that maps it to $x$ factors through every open set that contains $x$, so through an affine open $U = \operatorname{Spec} A \ni x$, and $k$-morphisms $\operatorname{Spec} k[\varepsilon] \to U$ are $k$-algebra maps $\varphi \colon A \to k[\varepsilon]$ (Theorem P3.1.22). The image of the point is $\varphi^{-1}((\varepsilon))$, so the condition is that $\varphi^{-1}((\varepsilon)) = \mathfrak{p}_x$, that is, that $\varphi$ followed by $k[\varepsilon] \to k$ is the evaluation $A \to \kappa(x) = k$, $a \mapsto a(x)$. Then $\varphi$ maps $A \setminus \mathfrak{p}_x$ to units of $k[\varepsilon]$, and it extends uniquely to a local $k$-algebra map $\mathcal{O}_{X, x} = A_{\mathfrak{p}_x} \to k[\varepsilon]$. So the set in question is the set of local $k$-algebra maps $\varphi \colon \mathcal{O}_{X, x} \to k[\varepsilon]$, and it does not depend on $U$.

Write $\varphi(a) = a(x) + D(a) \varepsilon$. Then $\varphi$ is a $k$-algebra map if and only if $D$ is $k$-linear, $D(1) = 0$, and $D(ab) = a(x) D(b) + b(x) D(a)$, since $\varepsilon^2 = 0$. Such a $D$ kills $k$ and $\mathfrak{m}_x^2$: for $a, b \in \mathfrak{m}_x$, $a(x) = b(x) = 0$. So it restricts to a linear form $\lambda$ on $\mathfrak{m}_x/\mathfrak{m}_x^2$. Conversely, for a linear form $\lambda$ put $D(a) = \lambda(a - a(x))$, where $a - a(x) \in \mathfrak{m}_x$ since $\kappa(x) = k$. Then $ab - a(x) b(x) = a(x)(b - b(x)) + b(x)(a - a(x)) + (a - a(x))(b - b(x))$, and the last term lies in $\mathfrak{m}_x^2$, so $D$ satisfies the product rule. The two constructions are inverse. For $f \colon X \to Y$, $y = f(x)$ has $\kappa(y) = k$, as $k \subseteq \kappa(y) \subseteq \kappa(x) = k$. The composite $f \circ v$ corresponds to $\varphi \circ f^\#_x$, and its form is $\lambda \circ \bar f^\#$ with $\bar f^\# \colon \mathfrak{m}_y/\mathfrak{m}_y^2 \to \mathfrak{m}_x/\mathfrak{m}_x^2$. This is linear in $\lambda$. $\square$

*Proof of Proposition P3.7.14.* Let $R = k[x_1, \dots, x_n]$, $\mathfrak{M} = (x_1 - a_1, \dots, x_n - a_n)$, $I = (f_1, \dots, f_r)$ and $A = R/I$, with $\mathfrak{m} = \mathfrak{M}/I$. Localization does not change the cotangent space at a maximal ideal: $\mathfrak{m}/\mathfrak{m}^2 = \mathfrak{m}A_\mathfrak{m}/\mathfrak{m}^2 A_\mathfrak{m}$, since $\mathfrak{m}/\mathfrak{m}^2$ is already an $A/\mathfrak{m}$-module and elements outside $\mathfrak{m}$ act on it as units. Then $\mathfrak{m}/\mathfrak{m}^2 = \mathfrak{M}/(\mathfrak{M}^2 + I)$. The space $\mathfrak{M}/\mathfrak{M}^2$ has basis the classes of $x_i - a_i$, as $R = k[x_1 - a_1, \dots, x_n - a_n]$. Since $p \in X$, $I \subseteq \mathfrak{M}$, and by Taylor expansion at $p$,
$$f_j \equiv \sum_i \frac{\partial f_j}{\partial x_i}(p) \, (x_i - a_i) \pmod{\mathfrak{M}^2}.$$
So the image of $I$ in $\mathfrak{M}/\mathfrak{M}^2 \cong k^n$ is the span of the rows of $J(p)$. Hence $\mathfrak{m}/\mathfrak{m}^2 \cong k^n/\operatorname{row} J(p)$, and its dual is the space of $v \in k^n$ with $J(p) v = 0$. $\square$

*Proof of Proposition P3.7.15.* (1) Let $e = \dim \mathfrak{m}_x/\mathfrak{m}_x^2$. By Nakayama's lemma (Theorem P1.1.25), $\mathfrak{m}_x$ is generated by $e$ elements, and by Krull's height theorem (Theorem P1.5.18), $\dim \mathcal{O}_{X, x} = \operatorname{ht} \mathfrak{m}_x \leq e$.

(2) A regular local ring is a domain (Corollary P1.9.3). So $\mathcal{O}_{X, x}$ is reduced and has one minimal prime. The minimal primes of $\mathcal{O}_{X, x}$ are the generic points of the irreducible components of $X$ through $x$, by the bijection in the proof of part 4 of Proposition P3.7.2.

(3) Let $U = \operatorname{Spec} A$ be an affine open containing $x$; it contains $x'$, as every open set that contains $x$ contains its generizations. Then $x' = \mathfrak{p}' \subseteq \mathfrak{p} = x$, and $\mathcal{O}_{X, x'} = A_{\mathfrak{p}'}$ is the localization of $A_\mathfrak{p}$ at the prime $\mathfrak{p}' A_\mathfrak{p}$. It is regular by Corollary P1.9.22.

(4) Let every closed point be regular, and let $x \in X$. The closure $\overline{\{x\}}$ contains a closed point $y$ of $X$ by part 3 of Proposition P3.7.3, so $x$ is a generization of $y$, and it is regular by part 3. The converse is clear.

(5) Let $X$ be integral of dimension $1$. For a closed point $x$, $\mathcal{O}_{X, x}$ is a Noetherian local domain, of dimension $1$: it is not $0$, as $x$ is not the generic point, and at most $\dim X = 1$. By Theorem P1.7.12, it is regular if and only if it is a discrete valuation ring. The generic point has local ring $K(X)$, a field, which is regular. Every other point $x$ is closed. Indeed, $\overline{\{x\}} \neq X$, and as $\dim X = 1$ it contains no smaller irreducible closed set. For $y \in \overline{\{x\}}$ this gives $\overline{\{y\}} = \overline{\{x\}}$, so $y = x$ by the uniqueness of generic points (Theorem P3.2.20). $\square$

### Exercises

1. (A) Compute $\dim T_p X$ at every rational point $p$ of $X = V(x^2 + y^2 - z^2) \subseteq \mathbb{A}^3_k$, for $\operatorname{char} k \neq 2$. Which points are singular?
2. (A) Let $X = V(xy) \subseteq \mathbb{A}^2_k$. Show that the origin is singular, using both Proposition P3.7.14 and part 2 of Proposition P3.7.15.
3. (A) Describe the morphisms $\operatorname{Spec} k[\varepsilon] \to \mathbb{P}^n_k$ that map the point to $[1 : 0 : \dots : 0]$, and show that they form a vector space of dimension $n$.
4. (B) Let $X = V(y^2 - x^3) \subseteq \mathbb{A}^2_k$ and $\nu \colon \mathbb{A}^1_k \to X$, $t \mapsto (t^2, t^3)$. Show that $d\nu_0 \colon T_0 \mathbb{A}^1 \to T_0 X$ is zero, although $\nu$ is a homeomorphism.
5. (B) Let $X = \operatorname{Spec} \mathbb{R}[x]/(x^2 + 1)$ over $\mathbb{R}$. Show that its point is regular with $T X = 0$, and that there are no $\mathbb{R}$-morphisms $\operatorname{Spec} \mathbb{R}[\varepsilon] \to X$. Explain why this does not contradict Proposition P3.7.13.
6. (B) Let $p$ be a prime with $p = 2$ or $p \equiv 3 \bmod 4$, and $A = \mathbb{Z}[x]/(x^2 - p)$. Show that $\operatorname{Spec} A$ is regular. Show that for $p \equiv 1 \bmod 4$ the point $(2, x - 1)$ is singular, as in Example P3.7.20. Let $B = \mathbb{Z}[x]/(x^2 - p^2)$ with $p$ odd. Show that $\operatorname{Spec} B$ has two irreducible components and find the points where they meet.
7. (C) Let $X$ be a scheme of finite type over a perfect field $k$. Show that the set of regular points of $X$ is open, using Corollary P1.9.13 and part 3 of Proposition P3.7.15. Give an example of a subset of $\operatorname{Spec} k[x]$ that is stable under generization and not open, to show that part 3 alone does not imply openness.

### Lean

Mathlib defines regular local rings by `IsRegularLocalRing`, with `IsRegularLocalRing.iff_finrank_cotangentSpace` relating the definition to the dimension of `IsLocalRing.CotangentSpace`, and regular rings by `IsRegularRing`. It proves that polynomial rings over regular rings are regular, `MvPolynomial.isRegularRing_of_isRegularRing`, and that Dedekind domains are regular. Mathlib has no notion of a regular scheme and no tangent space of a scheme, and the description of tangent vectors by dual numbers is not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Zariski introduced the tangent space $(\mathfrak{m}/\mathfrak{m}^2)^\vee$ and the notion of a simple point in 1947, and proved that for varieties over a perfect field it agrees with the Jacobian criterion of the next section. Hartshorne, Section I.5, treats nonsingular varieties over an algebraically closed field, and the description of tangent vectors by $k[\varepsilon]$ is Hartshorne, Exercise II.2.8. The literature state is theorem. In the minimal model program singular points are the subject: terminal, canonical, log terminal and log canonical singularities are classes of singular points defined through a resolution, and the singularities of a minimal model are terminal, which in dimension two means regular.
