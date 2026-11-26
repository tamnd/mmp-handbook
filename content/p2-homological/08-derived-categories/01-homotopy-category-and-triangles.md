---
title: The homotopy category and triangles
nodes: []
sources: [Wei94, Ver96, Stacks]
reads_with: [Wei94:ch10]
requires: [P2.2, P2.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The homotopy category and triangles

### Statement

Let $\mathcal{A}$ be an abelian category and $\mathsf{C}(\mathcal{A})$ its category of complexes, indexed by $\mathbb{Z}$, with cohomological differentials. Homotopic maps induce the same maps on cohomology (Proposition P2.3.4). So the first step is to identify them.

**Definition P2.8.1 (homotopy category).** The *homotopy category* $K(\mathcal{A})$ has the complexes in $\mathcal{A}$ as objects, and
$$\operatorname{Hom}_{K(\mathcal{A})}(K^\bullet, L^\bullet) = \operatorname{Hom}_{\mathsf{C}(\mathcal{A})}(K^\bullet, L^\bullet)/\{\text{maps homotopic to } 0\}.$$
The full subcategories $K^+(\mathcal{A})$, $K^-(\mathcal{A})$ and $K^b(\mathcal{A})$ consist of the complexes with $K^n = 0$ for $n \ll 0$, for $n \gg 0$, and for $|n| \gg 0$. The *shift* of a complex is $K[1]^n = K^{n+1}$, with differential $-d_K$, and $K[m]$ is the $m$-fold shift. For an object $A$, $A[m]$ is the complex with $A$ in degree $-m$ and $0$ elsewhere.

Lean: Mathlib `HomotopyCategory`, with the quotient functor `HomotopyCategory.quotient` and the cohomology functors `HomotopyCategory.homologyFunctor`.

**Definition P2.8.2 (mapping cone and triangles).** Let $f: K^\bullet \to L^\bullet$ be a map of complexes. The *mapping cone* of $f$ is the complex
$$\operatorname{Cone}(f)^n = K^{n+1} \oplus L^n, \qquad d(k, l) = (-d k, \ f(k) + d l),$$
as in Exercise 4 of Section 3.1. It comes with the maps $\iota: L \to \operatorname{Cone}(f)$, $\iota(l) = (0, l)$, and $\pi: \operatorname{Cone}(f) \to K[1]$, $\pi(k, l) = k$. A *triangle* in $K(\mathcal{A})$ is a diagram $X \to Y \to Z \to X[1]$. The *standard triangle* of $f$ is $K \xrightarrow{f} L \xrightarrow{\iota} \operatorname{Cone}(f) \xrightarrow{\pi} K[1]$. A triangle is *distinguished* if it is isomorphic in $K(\mathcal{A})$ to a standard triangle.

Lean: Mathlib `CochainComplex.mappingCone`, with the standard triangles `CochainComplex.mappingCone.triangle` and `CochainComplex.mappingCone.triangleh`; triangles are `CategoryTheory.Pretriangulated.Triangle`.

**Theorem P2.8.3 ($K(\mathcal{A})$ is triangulated).** The category $K(\mathcal{A})$ is additive, the shift is an additive automorphism, and the distinguished triangles satisfy:

1. (TR1) Every map $f: X \to Y$ lies in a distinguished triangle $X \to Y \to Z \to X[1]$. The triangle $X \xrightarrow{1} X \to 0 \to X[1]$ is distinguished, and a triangle isomorphic to a distinguished triangle is distinguished.
2. (TR2) A triangle $X \xrightarrow{f} Y \xrightarrow{g} Z \xrightarrow{h} X[1]$ is distinguished if and only if its rotation $Y \xrightarrow{g} Z \xrightarrow{h} X[1] \xrightarrow{-f[1]} Y[1]$ is distinguished.
3. (TR3) A commutative square between the first two terms of two distinguished triangles extends, not uniquely, to a map of triangles.
4. (TR4) The octahedral axiom: for maps $X \xrightarrow{f} Y \xrightarrow{g} Z$, the cones of $f$, $g f$ and $g$ fit in a distinguished triangle $\operatorname{Cone}(f) \to \operatorname{Cone}(g f) \to \operatorname{Cone}(g) \to \operatorname{Cone}(f)[1]$, compatible with the given maps.

An additive category with a shift and a class of triangles with these properties is a *triangulated category*. The subcategories $K^+$, $K^-$ and $K^b$ are triangulated in the same way.

Lean: Mathlib `CategoryTheory.Pretriangulated` for TR1 to TR3 and `CategoryTheory.IsTriangulated` for TR4, with instances for `HomotopyCategory` on cochain complexes indexed by $\mathbb{Z}$.

**Proposition P2.8.4 (the long exact sequence of a triangle).** Let $X \xrightarrow{f} Y \xrightarrow{g} Z \xrightarrow{h} X[1]$ be a distinguished triangle in $K(\mathcal{A})$. Then the sequence
$$\cdots \to H^n(X) \xrightarrow{H^n(f)} H^n(Y) \xrightarrow{H^n(g)} H^n(Z) \xrightarrow{H^n(h)} H^{n+1}(X) \xrightarrow{H^{n+1}(f)} H^{n+1}(Y) \to \cdots$$
is exact. In particular a map $f$ is a quasi-isomorphism if and only if $\operatorname{Cone}(f)$ is exact. Also, for every object $W$ the sequences of abelian groups obtained by applying $\operatorname{Hom}_{K(\mathcal{A})}(W, -)$ and $\operatorname{Hom}_{K(\mathcal{A})}(-, W)$ to the triangle and its rotations are exact.

Lean: Mathlib proves the long exact sequence of cohomology for triangles in the derived category through `DerivedCategory.homologyFunctor`; the statement for $K(\mathcal{A})$ in this form is not in Lean as stated.

### Proof in words

Homotopy is compatible with sums and composition, so $K(\mathcal{A})$ is additive. The standard triangle sits in a short exact sequence of complexes $0 \to L \to \operatorname{Cone}(f) \to K[1] \to 0$ that splits in each degree. Its long exact sequence of cohomology has connecting map $H(f)$, which gives the long exact sequence of the triangle. The rotation axiom comes from an explicit homotopy equivalence between the cone of $\iota$ and $K[1]$. The extension axiom TR3 is a matrix formula, and the octahedral axiom is a longer computation with cones of the same kind.

### Examples

**Example P2.8.5 (contractible complexes are zero).** The complex $0 \to A \xrightarrow{1} A \to 0$, with $A$ in degrees $0$ and $1$, is contractible: the homotopy $h^1 = 1: A \to A$ gives $1 = d h + h d$. So it is isomorphic to $0$ in $K(\mathcal{A})$. More generally, $\operatorname{Cone}(1_K)$ is contractible for every complex $K$, which is the statement that $K \xrightarrow{1} K \to 0 \to K[1]$ is distinguished.

**Example P2.8.6 (the cone of multiplication by $n$).** Let $f = n: \mathbb{Z} \to \mathbb{Z}$, a map of complexes concentrated in degree $0$. Then $\operatorname{Cone}(f)$ is the complex $\mathbb{Z} \xrightarrow{n} \mathbb{Z}$ in degrees $-1$ and $0$. Its cohomology is $\mathbb{Z}/n$ in degree $0$, and the long exact sequence of the triangle is $0 \to \mathbb{Z} \xrightarrow{n} \mathbb{Z} \to \mathbb{Z}/n \to 0$. The cone is the complex $K$ of Example P2.3.6, shifted by one, and it is not isomorphic in $K(\mathsf{Ab})$ to $\mathbb{Z}/n$ in degree $0$, since a map of complexes from $\mathbb{Z}/n$ to $\mathbb{Z}$ is $0$. Section 8.2 inverts the quasi-isomorphism $\operatorname{Cone}(f) \to \mathbb{Z}/n$.

**Example P2.8.7 (short exact sequences need not give triangles in $K(\mathcal{A})$).** The sequence $0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z} \to \mathbb{Z}/2 \to 0$, with each term a complex in degree $0$, does not come from a distinguished triangle $\mathbb{Z} \to \mathbb{Z} \to \mathbb{Z}/2 \to \mathbb{Z}[1]$ in $K(\mathsf{Ab})$. The only map $\mathbb{Z}/2 \to \mathbb{Z}[1]$ of complexes is $0$, and a distinguished triangle with third map $0$ splits (Exercise 4), while $\mathbb{Z}$ is not $\mathbb{Z} \oplus \mathbb{Z}/2$. A short exact sequence that splits in each degree does give a triangle (Exercise 5). In the derived category every short exact sequence gives a triangle, and the third map is the extension class (Section 8.2).

### Proof

*Theorem P2.8.3.* If $f \simeq f'$ by $h$ and $g: L \to M$, then $g f \simeq g f'$ by $g h$, and similarly on the other side. Sums of null homotopic maps are null homotopic. So composition is well defined on homotopy classes, and $K(\mathcal{A})$ is additive with the direct sum of complexes. The shift is a functor, since a homotopy $h$ for $f$ gives the homotopy $-h$ for $f[1]$ with the shifted differentials, and $[1]$ has inverse $[-1]$.

TR1. The standard triangle of $f$ contains $f$. The cone of $1_X$ is contractible: $h(k, l) = (l, 0)$, from $\operatorname{Cone}(1_X)^n$ to $\operatorname{Cone}(1_X)^{n-1}$, satisfies $d h + h d = 1$, since $d h(k, l) = (-d l, l)$ and $h d(k, l) = (k + d l, 0)$. So $X \to X \to 0 \to X[1]$ is isomorphic to the standard triangle of $1_X$. The last claim is part of the definition.

TR2. It suffices to treat a standard triangle and to show one direction. The other direction follows by rotating three times, since the triple rotation is the triangle shifted by $[1]$ with all signs changed, which is isomorphic to it through the map $-1$ on one term. Let $f: K \to L$ and consider $\iota: L \to C = \operatorname{Cone}(f)$. Then $\operatorname{Cone}(\iota)^n = L^{n+1} \oplus K^{n+1} \oplus L^n$ with $d(l', k, l) = (-d l', -d k, f(k) + d l + l')$. Define
$$\alpha: \operatorname{Cone}(\iota) \to K[1], \ \alpha(l', k, l) = k, \qquad \beta: K[1] \to \operatorname{Cone}(\iota), \ \beta(k) = (-f(k), k, 0).$$
Both are maps of complexes: $\alpha d(l', k, l) = -d k = d_{K[1]} \alpha(l', k, l)$, and $d \beta(k) = (f(d k), -d k, 0) = \beta(-d k)$. Then $\alpha \beta = 1$, and $1 - \beta \alpha$ sends $(l', k, l)$ to $(l' + f(k), 0, l)$. With $h(l', k, l) = (l, 0, 0)$,
$$d h(l', k, l) + h d(l', k, l) = (-d l, 0, l) + (f(k) + d l + l', 0, 0) = (l' + f(k), 0, l).$$
So $\beta \alpha \simeq 1$, and $\alpha$ is an isomorphism in $K(\mathcal{A})$. Under $\alpha$, the map $C \to \operatorname{Cone}(\iota)$, $(k, l) \mapsto (0, k, l)$, becomes $\pi$, and the map $\operatorname{Cone}(\iota) \to L[1]$, $(l', k, l) \mapsto l'$, composed with $\beta$, becomes $-f$. So the standard triangle of $\iota$ is isomorphic to $L \xrightarrow{\iota} C \xrightarrow{\pi} K[1] \xrightarrow{-f[1]} L[1]$, which is therefore distinguished.

TR3 and TR4. For TR3, given standard triangles of $f: K \to L$ and $f': K' \to L'$ and maps $a: K \to K'$, $b: L \to L'$ with a homotopy $s$ from $f' a$ to $b f$, the map $(k, l) \mapsto (a(k), b(l) + s(k))$ from $\operatorname{Cone}(f)$ to $\operatorname{Cone}(f')$ completes the map of triangles, by a direct check. The octahedral axiom is a similar but longer computation with the cones of $f$, $g f$ and $g$; see Weibel, Chapter 10, or the Stacks project, chapter Derived categories. $\square$

*Proposition P2.8.4.* Isomorphic triangles give isomorphic sequences, so take the standard triangle of $f: K \to L$. The sequence $0 \to L \xrightarrow{\iota} \operatorname{Cone}(f) \xrightarrow{\pi} K[1] \to 0$ is exact in each degree. By Theorem P2.3.5 it gives a long exact sequence. Its connecting map $H^n(K[1]) = H^{n+1}(K) \to H^{n+1}(L)$ is computed by lifting a cocycle $k$ to $(k, 0)$ and applying $d$, which gives $(0, f(k))$, the image of $f(k)$. So the connecting map is $H^{n+1}(f)$, and the long exact sequence is the sequence of the proposition. If $\operatorname{Cone}(f)$ is exact, the sequence makes every $H^n(f)$ an isomorphism, and conversely.

For the functor $\operatorname{Hom}(W, -)$, it suffices by TR2 to show exactness at $\operatorname{Hom}(W, L)$ for the standard triangle. The composite $\iota f$ is null homotopic by $h(k) = (k, 0)$. If $\iota u \simeq 0$ for $u: W \to L$, say $\iota u = d s + s d$ with $s(w) = (s_1(w), s_2(w))$, then the first component gives $0 = -d s_1 + s_1 d$, so $s_1: W \to K$ is a map of complexes, and the second component gives $u = f s_1 + d s_2 + s_2 d$. So $u \simeq f s_1$, which is exactness. The case of $\operatorname{Hom}(-, W)$ is dual. $\square$

### Exercises

1. (A) Show that a map of complexes that is homotopic to $0$ induces $0$ on cohomology, and deduce that $H^n$ is a functor on $K(\mathcal{A})$.
2. (A) Show that $\operatorname{Cone}(f)[1]$ is not $\operatorname{Cone}(f[1])$ on the nose, and write down an isomorphism of complexes between them.
3. (A) Show that the composite of two consecutive maps in a distinguished triangle is $0$ in $K(\mathcal{A})$.
4. (B) Let $X \xrightarrow{f} Y \xrightarrow{g} Z \xrightarrow{0} X[1]$ be distinguished in a triangulated category. Using Proposition P2.8.4 for $\operatorname{Hom}(Z, -)$, show that $g$ has a right inverse and that $Y \cong X \oplus Z$.
5. (B) Let $0 \to K \xrightarrow{f} L \xrightarrow{g} M \to 0$ be an exact sequence of complexes that splits in each degree, with $L^n = K^n \oplus M^n$. Write $d_L(k, m) = (d k + \tau(m), d m)$. Show that $\tau: M \to K[1]$ is a map of complexes and that $K \to L \to M \xrightarrow{\tau} K[1]$ is distinguished, possibly after a sign.
6. (B) Show that in a triangulated category, a monomorphism is a split monomorphism. Deduce that $K(\mathsf{Ab})$ is not abelian.
7. (C) Let $\mathcal{A} = \mathsf{Ab}$ and let $P$ be a bounded above complex of projective modules. Show that every exact complex $E$ satisfies $\operatorname{Hom}_{K(\mathcal{A})}(P, E) = 0$, by constructing a null homotopy degree by degree, from the top. This is the dual of the key lemma of Section 8.2.

### Lean

Mathlib has the homotopy category `HomotopyCategory` with its quotient functor `HomotopyCategory.quotient` and cohomology functors `HomotopyCategory.homologyFunctor`. The mapping cone is `CochainComplex.mappingCone`, with the standard triangles `CochainComplex.mappingCone.triangle` and `CochainComplex.mappingCone.triangleh`. Triangles are `CategoryTheory.Pretriangulated.Triangle`, pretriangulated categories are `CategoryTheory.Pretriangulated`, and the octahedral axiom is `CategoryTheory.IsTriangulated`. Mathlib proves that the homotopy category of cochain complexes indexed by $\mathbb{Z}$ is triangulated. The handbook adds no `MinimalModel` node here.

### Notes and history

Triangulated categories were introduced by Verdier in his thesis, written under Grothendieck around 1963 and published in full only in 1996, and at the same time by Puppe in stable homotopy theory. The axiom TR3 does not give a unique map, and this lack of functoriality of the cone is the main technical defect of the theory. Enhancements by differential graded or stable infinity categories repair it. The handbook needs only the triangulated structure.
