---
title: Coordinate rings and morphisms
nodes: []
sources: [Rei88, Har77, Sha13]
reads_with: [Rei88:ch4, Har77:I.3, Sha13:ch1]
requires: [P1.1, P0.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Coordinate rings and morphisms

### Statement

**Definition P0.3.24 (coordinate ring).** Let $X \subseteq \mathbb{A}^n$ be an algebraic set. The coordinate ring of $X$ is the $k$-algebra

$$k[X] = k[x_1, \dots, x_n] / I(X).$$

Two polynomials have the same image in $k[X]$ if and only if they agree as functions on $X$. So $k[X]$ is the ring of polynomial functions $X \to k$.

Lean: not in Lean as stated; Mathlib has the quotient `MvPolynomial σ k ⧸ MvPolynomial.vanishingIdeal k X` and the affine scheme `AlgebraicGeometry.Spec`.

**Example P0.3.25.** The coordinate ring of $\mathbb{A}^n$ is $k[x_1, \dots, x_n]$, because $I(\mathbb{A}^n) = 0$ for $k$ infinite. The coordinate ring of a point is $k$.

**Example P0.3.26.** For the parabola $P = V(y - x^2)$, the ideal $(y - x^2)$ is prime, so $I(P) = (y - x^2)$ and $k[P] = k[x, y]/(y - x^2) \cong k[x]$. For the two axes $X = V(xy)$, $k[X] = k[x, y]/(xy)$. This ring is not a domain: the functions $x$ and $y$ are nonzero on $X$, but their product is $0$.

**Proposition P0.3.27 (properties of $k[X]$).** Let $X$ be an algebraic set.

1. The ring $k[X]$ is a finitely generated $k$-algebra and it is reduced: it has no nonzero nilpotent elements.
2. The ring $k[X]$ is a domain if and only if $X$ is irreducible.
3. The points of $X$ correspond to the maximal ideals of $k[X]$, by $a \mapsto \mathfrak{m}_a / I(X)$.

Lean: not in Lean as stated; Mathlib has `IsReduced` and the correspondence of ideals in a quotient, `Ideal.Quotient.mk` with `Ideal.map`.

*Proof.* The images of $x_1, \dots, x_n$ generate $k[X]$. If $f^m \in I(X)$, then $f^m$ vanishes on $X$, so $f$ does and $f \in I(X)$. This is 1. Statement 2 holds because $k[X]$ is a domain if and only if $I(X)$ is prime, and by the proposition of Section 3 this holds if and only if $X$ is irreducible. For 3, maximal ideals of $k[X]$ correspond to maximal ideals $\mathfrak{m}$ of $k[x_1, \dots, x_n]$ that contain $I(X)$. By the weak Nullstellensatz $\mathfrak{m} = \mathfrak{m}_a$ for one point $a$, and $I(X) \subseteq \mathfrak{m}_a$ if and only if $a \in V(I(X)) = X$. $\square$

**Definition P0.3.28 (morphism).** Let $X \subseteq \mathbb{A}^n$ and $Y \subseteq \mathbb{A}^m$ be algebraic sets. A morphism $\varphi \colon X \to Y$ is a map of the form $\varphi(a) = (f_1(a), \dots, f_m(a))$ with $f_1, \dots, f_m \in k[X]$ and $\varphi(X) \subseteq Y$. A morphism $\varphi$ is an isomorphism if there is a morphism $\psi \colon Y \to X$ with $\psi \circ \varphi = \mathrm{id}_X$ and $\varphi \circ \psi = \mathrm{id}_Y$. The pullback of $\varphi$ is the map

$$\varphi^* \colon k[Y] \to k[X], \qquad g \mapsto g \circ \varphi.$$

Lean: not in Lean as stated; the scheme version is a morphism of schemes `AlgebraicGeometry.Spec.map` between affine schemes.

**Example P0.3.29.** A linear map $\mathbb{A}^n \to \mathbb{A}^m$ is a morphism. The projection $V(y - x^2) \to \mathbb{A}^1$, $(x, y) \mapsto x$, is a morphism.

**Example P0.3.30.** The map $\varphi \colon \mathbb{A}^1 \to \mathbb{A}^2$, $t \mapsto (t^2, t^3)$, is a morphism with image in the cuspidal cubic $C = V(y^2 - x^3)$, because $(t^3)^2 = (t^2)^3$.

The pullback $\varphi^*$ is well defined. If $g \in k[y_1, \dots, y_m]$ vanishes on $Y$, then $g \circ \varphi$ vanishes on $X$ because $\varphi(X) \subseteq Y$. In terms of polynomials, $\varphi^*(g) = g(f_1, \dots, f_m)$. So $\varphi^*$ is a homomorphism of $k$-algebras. A morphism is continuous in the Zariski topology, because $\varphi^{-1}(Y \cap V(g)) = X \cap V(\varphi^* g)$ for every $g$.

**Theorem P0.3.31 (anti-equivalence).** Let $k$ be algebraically closed.

1. For algebraic sets $X$ and $Y$, the map $\varphi \mapsto \varphi^*$ is a bijection from the set of morphisms $X \to Y$ to the set of $k$-algebra homomorphisms $k[Y] \to k[X]$. It satisfies $(\psi \circ \varphi)^* = \varphi^* \circ \psi^*$ and $\mathrm{id}_X^* = \mathrm{id}$.
2. Every finitely generated reduced $k$-algebra $A$ is isomorphic to $k[X]$ for some algebraic set $X$.

So $X \mapsto k[X]$ is an anti-equivalence from the category of affine algebraic sets over $k$ to the category of finitely generated reduced $k$-algebras. It restricts to an anti-equivalence from affine varieties to finitely generated $k$-algebras that are domains. In particular, $\varphi$ is an isomorphism if and only if $\varphi^*$ is an isomorphism.

Lean: Mathlib `AlgebraicGeometry.AffineScheme.equivCommRingCat` (proved in Mathlib, as the anti-equivalence of affine schemes with commutative rings; the classical form is not in Lean as stated).

*Proof.* The rule $(\psi \circ \varphi)^* g = g \circ \psi \circ \varphi = \varphi^*(\psi^* g)$ is direct. Let $y_1, \dots, y_m$ be the coordinates on $\mathbb{A}^m$ and $\bar y_i$ their images in $k[Y]$. Injectivity: $\varphi$ is determined by its components $f_i = \varphi^*(\bar y_i)$. Surjectivity: let $\alpha \colon k[Y] \to k[X]$ be a homomorphism of $k$-algebras. Put $f_i = \alpha(\bar y_i)$ and let $\varphi = (f_1, \dots, f_m) \colon X \to \mathbb{A}^m$. For $g \in I(Y)$ the function $g \circ \varphi = g(f_1, \dots, f_m)$ is equal to $\alpha(g(\bar y_1, \dots, \bar y_m)) = \alpha(0) = 0$ in $k[X]$. So $g$ vanishes on $\varphi(X)$, and $\varphi(X) \subseteq V(I(Y)) = Y$. Then $\varphi^*$ and $\alpha$ agree on the generators $\bar y_i$, so $\varphi^* = \alpha$. This proves 1.

For 2, choose generators $a_1, \dots, a_n$ of $A$. The homomorphism $k[x_1, \dots, x_n] \to A$, $x_i \mapsto a_i$, is surjective with kernel $J$, so $A \cong k[x_1, \dots, x_n]/J$. Since $A$ is reduced, $J$ is radical. Put $X = V(J)$. By the Nullstellensatz $I(X) = \sqrt{J} = J$, so $k[X] \cong A$.

A functor that is bijective on sets of morphisms and surjective on objects up to isomorphism is an equivalence of categories. With 1 and 2 this gives the anti-equivalence. Section 3 shows that $X$ is irreducible if and only if $k[X]$ is a domain, which gives the restriction to affine varieties. An equivalence preserves and reflects isomorphisms, which gives the last statement. $\square$

### Proof in words

A morphism to $Y \subseteq \mathbb{A}^m$ is a list of $m$ functions on $X$, and these are the images of the $m$ coordinates under the pullback. A homomorphism $k[Y] \to k[X]$ is also fixed by the images of the $m$ coordinates. The only thing to check is that a list that comes from a homomorphism maps $X$ into $Y$, and this holds because the homomorphism sends the equations of $Y$ to $0$. The Nullstellensatz enters at one point: it makes every reduced algebra the full ring of functions on its zero set, with no extra relations.

### Examples

The parabola $P = V(y - x^2)$ is isomorphic to $\mathbb{A}^1$. The morphisms $t \mapsto (t, t^2)$ and $(x, y) \mapsto x$ are inverse to each other. On coordinate rings they give the isomorphism $k[x, y]/(y - x^2) \cong k[t]$.

The cuspidal cubic $C = V(y^2 - x^3)$ is not isomorphic to $\mathbb{A}^1$, although the morphism $\varphi \colon t \mapsto (t^2, t^3)$ from $\mathbb{A}^1$ to $C$ is a bijection. Its inverse on points is $(x, y) \mapsto y/x$ for $x \neq 0$ and $(0, 0) \mapsto 0$, and this map is not a morphism. On rings, $\varphi^* \colon k[C] \to k[t]$ sends $x \mapsto t^2$ and $y \mapsto t^3$. It is injective with image $k[t^2, t^3] \neq k[t]$, so $\varphi^*$ is not an isomorphism and $\varphi$ is not an isomorphism. To see that no isomorphism $C \cong \mathbb{A}^1$ exists, compare the maximal ideals. In $B = k[t^2, t^3]$ the ideal $\mathfrak{m}$ of the origin is spanned by $t^i$ for $i \geq 2$, and $\mathfrak{m}^2$ is spanned by $t^i$ for $i \geq 4$. So $\dim_k \mathfrak{m}/\mathfrak{m}^2 = 2$. In $k[t]$ every maximal ideal is $(t - c)$, and $\dim_k (t - c)/(t - c)^2 = 1$. An isomorphism of $k$-algebras maps maximal ideals to maximal ideals and preserves this dimension. So $k[C] \not\cong k[t]$.

The hyperbola $H = V(xy - 1)$ has $k[H] \cong k[x, x^{-1}]$. The element $x$ is a unit that is not constant. In $k[t]$ the units are the nonzero constants. So $H$ is not isomorphic to $\mathbb{A}^1$, although the projection $(x, y) \mapsto x$ is a bijection from $H$ onto the open set $\mathbb{A}^1 \setminus \{0\}$.

### Exercises

1. (A) Show that the morphism $\mathbb{A}^1 \to V(y - x^3) \subset \mathbb{A}^2$, $t \mapsto (t, t^3)$, is an isomorphism, and write its pullback on coordinate rings.
2. (A) Let $\varphi \colon X \to Y$ be a morphism. Show that $\varphi^*$ is injective if and only if $\varphi(X)$ is dense in $Y$.
3. (A) Show that the coordinate ring of $V(xy) \subset \mathbb{A}^2$ embeds in $k[x] \times k[y]$, and describe its image. Show that $V(xy)$ is not isomorphic to $\mathbb{A}^1$.
4. (B) Let $\mathrm{char}\, k = p > 0$. Show that the Frobenius map $\mathbb{A}^1 \to \mathbb{A}^1$, $t \mapsto t^p$, is a bijective morphism that is not an isomorphism.
5. (B) Show that the nodal cubic $N = V(y^2 - x^2(x + 1))$ is not isomorphic to $\mathbb{A}^1$, and that $t \mapsto (t^2 - 1, t(t^2 - 1))$ is a surjective morphism $\mathbb{A}^1 \to N$ that is not injective.
6. (B) Let $X \subseteq \mathbb{A}^n$ be an algebraic set and $f \in k[X]$. Show that $X_f = \{a \in X : f(a) \neq 0\}$ is in bijection with the algebraic set $V(I(X), tf - 1) \subseteq \mathbb{A}^{n+1}$, and that its coordinate ring is $k[X][1/f]$.

### Lean

Mathlib does not have classical affine varieties as sets of points with coordinate rings. It has the scheme version: the affine scheme `AlgebraicGeometry.Spec` of a ring and the anti-equivalence `AlgebraicGeometry.AffineScheme.equivCommRingCat` between affine schemes and commutative rings. The classical theorem is the special case of finitely generated reduced $k$-algebras, restricted to closed points. The handbook uses these Mathlib names and adds no `MinimalModel` node here.

### Notes and history

The view of a variety through its ring of functions goes back to Dedekind and Weber (1882) for curves and to Hilbert and Noether for the general case. The anti-equivalence of this section is the model for P3: a scheme is built by gluing the spaces $\operatorname{Spec} A$ for all commutative rings $A$, so that nilpotents and fields that are not algebraically closed are allowed. The cuspidal cubic shows that a bijective morphism need not be an isomorphism. In P0 Chapter 7 the same curve appears as a singular curve whose normalization is $\mathbb{A}^1$. Exercise 6 gives the principal open sets, which form a base of the Zariski topology and are again affine. The literature state is theorem.
