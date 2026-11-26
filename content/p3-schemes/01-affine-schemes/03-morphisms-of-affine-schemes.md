---
title: Morphisms into affine schemes
nodes: []
sources: [Vak25, Har77, GW20, EGA1, Stacks]
reads_with: [Vak25:ch6, Har77:II.2, GW20:ch3]
requires: [P1.2, P2.1, P2.5, P2.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Morphisms into affine schemes

### Statement

Morphisms of locally ringed spaces are those of Definition P2.6.1: a continuous map $f \colon X \to Y$ with a map of sheaves of rings $f^\# \colon \mathcal{O}_Y \to f_* \mathcal{O}_X$ whose maps on stalks $f^\#_x \colon \mathcal{O}_{Y, f(x)} \to \mathcal{O}_{X, x}$ are local. Taking global sections, a morphism gives a ring map $f^\#_Y \colon \Gamma(Y, \mathcal{O}_Y) \to \Gamma(X, \mathcal{O}_X)$, and this is a functor $\Gamma$ from locally ringed spaces to rings, with the arrows reversed.

**Definition P3.1.21 (the morphism of a ring map).** Let $\varphi \colon A \to B$ be a ring map. The morphism $\operatorname{Spec} \varphi \colon \operatorname{Spec} B \to \operatorname{Spec} A$ is the continuous map $\varphi^* \colon \mathfrak{q} \mapsto \varphi^{-1}(\mathfrak{q})$ of Proposition P1.2.19 with the map of sheaves given on basic open sets by the maps
$$A_a \to B_{\varphi(a)} = \mathcal{O}_{\operatorname{Spec} B}((\varphi^*)^{-1} D(a)), \qquad x/a^n \mapsto \varphi(x)/\varphi(a)^n.$$
Its map on the stalk at $\mathfrak{q}$ is the localization $\varphi_\mathfrak{q} \colon A_{\varphi^{-1}\mathfrak{q}} \to B_\mathfrak{q}$, which is local.

Lean: Mathlib `AlgebraicGeometry.Spec.map` (for schemes) and `AlgebraicGeometry.Spec.locallyRingedSpaceMap`.

**Theorem P3.1.22 (morphisms into an affine scheme).** Let $X$ be a locally ringed space and $A$ a ring. The map
$$\operatorname{Hom}_{\mathsf{LRS}}(X, \operatorname{Spec} A) \to \operatorname{Hom}_{\mathsf{Ring}}(A, \Gamma(X, \mathcal{O}_X)), \qquad (f, f^\#) \mapsto f^\#_{\operatorname{Spec} A},$$
is a bijection, natural in $X$ and in $A$. In the language of P2 Ch. 1, $\operatorname{Spec} \colon \mathsf{Ring}^{\mathrm{op}} \to \mathsf{LRS}$ is right adjoint to $\Gamma \colon \mathsf{LRS} \to \mathsf{Ring}^{\mathrm{op}}$.

Lean: Mathlib `AlgebraicGeometry.ΓSpec.locallyRingedSpaceAdjunction` and, for schemes, `AlgebraicGeometry.ΓSpec.adjunction` (proved in Mathlib).

**Corollary P3.1.23 (rings and affine schemes).** For rings $A$ and $B$ the map $\varphi \mapsto \operatorname{Spec} \varphi$ is a bijection $\operatorname{Hom}(A, B) \cong \operatorname{Hom}(\operatorname{Spec} B, \operatorname{Spec} A)$. So $\operatorname{Spec}$ is an equivalence from $\mathsf{Ring}^{\mathrm{op}}$ to the category of affine schemes, with quasi-inverse $\Gamma$.

Lean: Mathlib `AlgebraicGeometry.Spec.fullyFaithful`, `AlgebraicGeometry.Spec.homEquiv` and `AlgebraicGeometry.AffineScheme.equivCommRingCat` (proved in Mathlib).

**Corollary P3.1.24 (a test for affineness).** For every locally ringed space $X$ there is a canonical morphism $c_X \colon X \to \operatorname{Spec} \Gamma(X, \mathcal{O}_X)$, the one that corresponds to the identity of $\Gamma(X, \mathcal{O}_X)$. The space $X$ is affine if and only if $c_X$ is an isomorphism. A point $x$ maps to the prime $\{s \in \Gamma(X, \mathcal{O}_X) : s(x) = 0\}$.

Lean: Mathlib `AlgebraicGeometry.Scheme.toSpecΓ` is the map $c_X$ for a scheme, and `AlgebraicGeometry.IsAffine` is defined as the condition that it is an isomorphism; `AlgebraicGeometry.Scheme.isoSpec` is the isomorphism.

### Proof in words

A morphism $f \colon X \to \operatorname{Spec} A$ gives a ring map $\psi \colon A \to \Gamma(X, \mathcal{O}_X)$. The point is that $\psi$ determines everything else. The point $f(x)$ must be the prime of the functions $a \in A$ that vanish at $x$ after pulling back, because the map on stalks is local: $a$ lies in the maximal ideal at $f(x)$ exactly when its pullback lies in the maximal ideal at $x$. The map of sheaves on $D(a)$ must be the unique extension of $\psi$ to $A_a$, because $\psi(a)$ is a unit on $f^{-1}(D(a))$. Conversely, any $\psi$ defines a point map in this way, the preimage of $D(a)$ is the open set where $\psi(a)$ does not vanish, and the universal property of localization gives the map of sheaves.

The locality of the maps on stalks is used once, and it is essential. Without it, the point map is not determined by $\psi$, as Example P3.1.25 shows. This is the reason for working with locally ringed spaces and not with ringed spaces.

### Examples

**Example P3.1.25 (a morphism of ringed spaces that is not local).** Let $R$ be a DVR with uniformizer $t$ and fraction field $K$, and let $f \colon \operatorname{Spec} K \to \operatorname{Spec} R$ send the only point to the closed point $(t)$. Then $f_* \mathcal{O}_{\operatorname{Spec} K}$ is $K$ on $\operatorname{Spec} R$ and $0$ on the open set $\{(0)\}$, since the preimage of that open set is empty. The inclusion $R \to K$ on global sections and $0$ on $\{(0)\}$ define a map of sheaves of rings $\mathcal{O}_{\operatorname{Spec} R} \to f_* \mathcal{O}_{\operatorname{Spec} K}$, so $f$ is a morphism of ringed spaces. Its map on stalks at $(t)$ is $R \to K$, which sends $t$ to a unit, so it is not local. The ring map $R \to K$ also defines the morphism $\operatorname{Spec} K \to \operatorname{Spec} R$ onto the generic point, which is local. So the two morphisms of ringed spaces have the same map on global sections, and only one of them is a morphism of locally ringed spaces. The theorem fails for ringed spaces.

**Example P3.1.26 (points with values in a field).** Let $K$ be a field. By the theorem, morphisms $\operatorname{Spec} K \to \operatorname{Spec} A$ are ring maps $\psi \colon A \to K$. Such a map has a prime kernel $\mathfrak{p}$, the image of the point, and it factors as $A \to \kappa(\mathfrak{p}) \to K$, by the universal properties of the quotient and of the fraction field. So a morphism $\operatorname{Spec} K \to \operatorname{Spec} A$ is a point $\mathfrak{p}$ with a field embedding $\kappa(\mathfrak{p}) \to K$. For $A = \mathbb{R}[x]$ and $K = \mathbb{C}$, the point $(x^2 + 1)$ receives two morphisms from $\operatorname{Spec} \mathbb{C}$, through $x \mapsto i$ and $x \mapsto -i$, while the point $(x)$ receives one. Chapter 3 calls these the $\mathbb{C}$-points of the real line.

**Example P3.1.27 (tangent vectors).** Let $k$ be a field, $A$ a $k$-algebra and $D = \operatorname{Spec} k[\epsilon]/(\epsilon^2)$. A $k$-algebra map $\psi \colon A \to k[\epsilon]/(\epsilon^2)$ is $\psi(a) = \lambda(a) + \delta(a) \epsilon$, where $\lambda \colon A \to k$ is a $k$-algebra map, so a point $\mathfrak{m} = \ker \lambda$ with residue field $k$, and $\delta \colon A \to k$ is $k$-linear with $\delta(ab) = \lambda(a) \delta(b) + \lambda(b) \delta(a)$. Such a $\delta$ kills $k$ and $\mathfrak{m}^2$, so it is a linear form on $\mathfrak{m}/\mathfrak{m}^2$, and every linear form arises in this way. So the morphisms $D \to \operatorname{Spec} A$ over $k$ are the pairs of a $k$-point $\mathfrak{m}$ and a tangent vector in the Zariski tangent space $(\mathfrak{m}/\mathfrak{m}^2)^\vee$ of P0 Ch. 6. Deformation theory, and the bend-and-break of P8 Ch. 2, starts from this example.

**Example P3.1.28 (the Frobenius).** Let $p$ be a prime and $A$ a ring of characteristic $p$. The map $F \colon A \to A$, $a \mapsto a^p$, is a ring map. For a prime $\mathfrak{p}$, $F^{-1}(\mathfrak{p}) = \{a : a^p \in \mathfrak{p}\} = \mathfrak{p}$, so $\operatorname{Spec} F$ is the identity on the space. It is not the identity morphism unless $F = 1_A$, that is, unless $a^p = a$ for all $a$. For $A = \mathbb{F}_p[x]$ the map $F$ sends $x$ to $x^p$, so $\operatorname{Spec} F$ is a morphism that is the identity on points and is not an isomorphism, since $F$ is not surjective. So a morphism of schemes is not determined by its map of spaces. Volume 11 uses the Frobenius as the basic tool in characteristic $p$.

**Example P3.1.29 (the final object).** For every locally ringed space $X$ there is exactly one ring map $\mathbb{Z} \to \Gamma(X, \mathcal{O}_X)$. By the theorem there is exactly one morphism $X \to \operatorname{Spec} \mathbb{Z}$. So $\operatorname{Spec} \mathbb{Z}$ is a final object of locally ringed spaces, and of schemes (Chapter 2). In the same way, for a field $k$, a morphism $X \to \operatorname{Spec} k$ is a ring map $k \to \Gamma(X, \mathcal{O}_X)$, a $k$-algebra structure on $\mathcal{O}_X$.

**Example P3.1.30 (affine space).** Let $X$ be a locally ringed space. A morphism $X \to \mathbb{A}^n_{\mathbb{Z}} = \operatorname{Spec} \mathbb{Z}[x_1, \dots, x_n]$ is a ring map $\mathbb{Z}[x_1, \dots, x_n] \to \Gamma(X, \mathcal{O}_X)$, that is, an $n$-tuple of global functions. So $\mathbb{A}^n_{\mathbb{Z}}$ represents the functor $X \mapsto \Gamma(X, \mathcal{O}_X)^n$, and $\mathbb{A}^1_{\mathbb{Z}}$ represents the functor of global functions. This is the statement promised in Example P2.1.26.

### Proof

*Proof of the theorem.* Write $\Phi$ for the map of the theorem. Let $\psi \colon A \to \Gamma(X, \mathcal{O}_X)$ be a ring map. The steps below construct a morphism $f$ with $\Phi(f) = \psi$.

The point map. For $x \in X$, the composite $A \to \Gamma(X, \mathcal{O}_X) \to \mathcal{O}_{X, x} \to \kappa(x)$ is a ring map to a field, so its kernel
$$f(x) = \{a \in A : \psi(a)(x) = 0\}$$
is a prime. For $a \in A$, $f^{-1}(D(a)) = \{x : \psi(a)(x) \neq 0\}$, which is open by part 3 of Proposition P3.1.14. So $f$ is continuous.

The map of sheaves. Write $X_a = f^{-1}(D(a))$. By part 1 of Proposition P3.1.14, $\psi(a)|_{X_a}$ is a unit of $\mathcal{O}_X(X_a)$. By the universal property of localization there is a unique ring map $f^\#_{D(a)} \colon A_a \to \mathcal{O}_X(X_a) = (f_* \mathcal{O}_X)(D(a))$ that extends $A \to \mathcal{O}_X(X) \to \mathcal{O}_X(X_a)$. For $D(b) \subseteq D(a)$ the two ways from $A_a$ to $\mathcal{O}_X(X_b)$ both extend the map from $A$, so they agree by uniqueness. So these maps form a morphism of sheaves on the basis, and by part 2 of Theorem P2.5.34 they come from a unique morphism of sheaves of rings $f^\# \colon \mathcal{O}_{\operatorname{Spec} A} \to f_* \mathcal{O}_X$. On global sections it is $\psi$, since $D(1) = \operatorname{Spec} A$.

Locality. Let $x \in X$ and $\mathfrak{p} = f(x)$. The stalk map $f^\#_x \colon A_\mathfrak{p} \to \mathcal{O}_{X, x}$ is the colimit of the maps $A_a \to \mathcal{O}_X(X_a) \to \mathcal{O}_{X, x}$ over $a \notin \mathfrak{p}$, so it sends $b/a$ to $\psi(b)_x \psi(a)_x^{-1}$. If $b/a \in \mathfrak{p} A_\mathfrak{p}$, then $b/a = b'/a'$ for some $b' \in \mathfrak{p}$ and $a' \notin \mathfrak{p}$, so it is enough to take $b \in \mathfrak{p}$, and then $\psi(b)(x) = 0$, so $\psi(b)_x \in \mathfrak{m}_x$ and the image lies in $\mathfrak{m}_x$. So $f^\#_x$ is local, $f$ is a morphism of locally ringed spaces, and $\Phi$ is surjective.

Injectivity. Let $(g, g^\#)$ be a morphism $X \to \operatorname{Spec} A$ with $g^\#_{\operatorname{Spec} A} = \psi$. For $x \in X$ the square
$$A \to A_{g(x)} \xrightarrow{g^\#_x} \mathcal{O}_{X, x}, \qquad A \xrightarrow{\psi} \Gamma(X, \mathcal{O}_X) \to \mathcal{O}_{X, x}$$
commutes, by the definition of the stalk map. Since $g^\#_x$ is local, and a local map sends exactly the elements of the maximal ideal into the maximal ideal (it sends the other elements, which are units, to units), $a \in g(x)$ if and only if $a/1 \in \mathfrak{m}_{g(x)}$, if and only if $\psi(a)_x \in \mathfrak{m}_x$, if and only if $\psi(a)(x) = 0$. So $g(x) = f(x)$ for all $x$. The maps $g^\#_{D(a)} \colon A_a \to \mathcal{O}_X(X_a)$ are ring maps that extend $A \to \mathcal{O}_X(X_a)$, by compatibility with restriction from $\operatorname{Spec} A$ to $D(a)$, so they equal $f^\#_{D(a)}$ by the uniqueness in the universal property of localization. By part 2 of Theorem P2.5.34, $g^\# = f^\#$. So $\Phi$ is injective.

Naturality. For a morphism $h \colon X' \to X$, $\Phi(f \circ h) = h^\#_X \circ \Phi(f)$, since global sections of a composite are the composite of the global sections. For a ring map $\varphi \colon A' \to A$, $\Phi(\operatorname{Spec} \varphi \circ f) = \Phi(f) \circ \varphi$, since the map of $\operatorname{Spec} \varphi$ on global sections is $\varphi$ by Definition P3.1.21. $\square$

*Proof of Corollary P3.1.23.* Take $X = \operatorname{Spec} B$ in the theorem. Then $\Gamma(X, \mathcal{O}_X) = B$ by Corollary P3.1.5, so $\operatorname{Hom}(\operatorname{Spec} B, \operatorname{Spec} A) \cong \operatorname{Hom}(A, B)$. The morphism $\operatorname{Spec} \varphi$ has $\varphi$ as its map on global sections, so it is the morphism that corresponds to $\varphi$, and the bijection is $\varphi \mapsto \operatorname{Spec} \varphi$. So $\operatorname{Spec}$ is fully faithful, and it is essentially surjective onto affine schemes by Definition P3.1.12. By Theorem P2.1.21 it is an equivalence, and $\Gamma$ is a quasi-inverse since $\Gamma(\operatorname{Spec} A) = A$ naturally. $\square$

*Proof of Corollary P3.1.24.* The formula for $c_X$ on points is the construction of the point map in the proof of the theorem, with $\psi = 1$. If $c_X$ is an isomorphism, $X$ is affine by definition. Conversely let $u \colon X \to \operatorname{Spec} A$ be an isomorphism, and let $\alpha = u^\#_{\operatorname{Spec} A} \colon A \to \Gamma(X, \mathcal{O}_X)$, an isomorphism of rings. By naturality in $A$, the morphism that corresponds to $\alpha$ is $\operatorname{Spec}(\alpha) \circ c_X$, so $u = \operatorname{Spec}(\alpha) \circ c_X$. Both $u$ and $\operatorname{Spec}(\alpha)$ are isomorphisms, and so is $c_X$. $\square$

### Exercises

1. (A) Let $\varphi \colon A \to B$ be a ring map. Show that $\operatorname{Spec} \varphi$ maps $D(\varphi(a))$ into $D(a)$, and that $(\operatorname{Spec} \varphi)^{-1}(V(I)) = V(\varphi(I) B)$.
2. (A) List the morphisms $\operatorname{Spec} \mathbb{C} \to \operatorname{Spec} \mathbb{Q}[x]/(x^2 - 2)$ and $\operatorname{Spec} \mathbb{Q}(\sqrt{2}) \to \operatorname{Spec} \mathbb{Q}[x]/(x^2 - 2)$. How many points does the target have?
3. (A) Show that $\operatorname{Spec} \mathbb{F}_p \to \operatorname{Spec} \mathbb{Z}$ and $\operatorname{Spec} \mathbb{Q} \to \operatorname{Spec} \mathbb{Z}$ are the inclusions of a closed point and of the generic point, and compute their maps on stalks.
4. (B) Let $X$ be a locally ringed space. Show that a morphism $X \to \mathbb{G}_m = \operatorname{Spec} \mathbb{Z}[x, x^{-1}]$ is the same as a unit of $\Gamma(X, \mathcal{O}_X)$, and that a morphism $X \to \operatorname{Spec} \mathbb{Z}[x]/(x^2)$ is a global function $s$ with $s^2 = 0$.
5. (B) Let $k$ be a field and $A$ a finitely generated $k$-algebra. Compute the morphisms $\operatorname{Spec} k[\epsilon]/(\epsilon^2) \to \operatorname{Spec} A$ over $k$ that send the point to the origin, for $A = k[x, y]/(y^2 - x^3)$ and for $A = k[x, y]/(y^2 - x^2 - x^3)$. Compare the dimensions of the tangent spaces at the origin with the dimension of the curve.
6. (B) Let $X$ be a locally ringed space and $c_X$ as in Corollary P3.1.24. Show that $c_X$ is a homeomorphism onto its image when $X$ is $\operatorname{Spec} A \setminus \{\mathfrak{m}\}$ for $A = k[x, y]$ and $\mathfrak{m} = (x, y)$, and that its image is not all of $\operatorname{Spec} \Gamma(X, \mathcal{O}_X)$. Conclude again that $X$ is not affine.
7. (B) Show that the theorem gives a bijection between the morphisms $\operatorname{Spec} B \to \operatorname{Spec} A$ of locally ringed spaces and the ring maps $A \to B$, and that the morphisms of ringed spaces between them form a larger set when $B$ is a DVR and $A = B$. (Generalize Example P3.1.25.)

### Lean

Mathlib proves the adjunction between $\Gamma$ and $\operatorname{Spec}$ as `AlgebraicGeometry.ΓSpec.locallyRingedSpaceAdjunction` for locally ringed spaces and `AlgebraicGeometry.ΓSpec.adjunction` for schemes. The full faithfulness of $\operatorname{Spec}$ is `AlgebraicGeometry.Spec.fullyFaithful`, with the bijection `AlgebraicGeometry.Spec.homEquiv`, and the equivalence of affine schemes with the opposite of commutative rings is `AlgebraicGeometry.AffineScheme.equivCommRingCat`. The map $c_X$ is `AlgebraicGeometry.Scheme.toSpecΓ`, and Mathlib takes the condition that it is an isomorphism as the definition `AlgebraicGeometry.IsAffine`. The handbook adds no `MinimalModel` node here.

### Notes and history

The theorem is in EGA I, Chapter I, in the form that $\operatorname{Spec}$ is right adjoint to the global sections functor on locally ringed spaces. Hartshorne proves the case $X = \operatorname{Spec} B$ as Proposition II.2.3 and leaves the general case as an exercise; the Stacks project proves it in the chapter Schemes. The literature state is theorem. Example P3.1.25 is the standard reason for the locality condition, and it appears in Vakil and in Görtz-Wedhorn. The adjunction is the first instance of the principle that a scheme is known by the maps into it, which Chapter 2 makes precise with the functor of points.
