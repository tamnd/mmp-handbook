---
title: The derived category
nodes: []
sources: [Wei94, Ver96, Huy06, Stacks]
reads_with: [Wei94:ch10]
requires: [P2.3, P2.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The derived category

### Statement

Let $\mathcal{A}$ be an abelian category. A quasi-isomorphism (Definition P2.3.2) need not have an inverse, even up to homotopy (Example P2.3.6). The derived category inverts all of them.

**Definition P2.8.8 (derived category).** The *derived category* $D(\mathcal{A})$ is the localization of $K(\mathcal{A})$ at the class of quasi-isomorphisms. It has the same objects as $K(\mathcal{A})$ and comes with a functor $Q: K(\mathcal{A}) \to D(\mathcal{A})$ that sends quasi-isomorphisms to isomorphisms, and it is universal with this property: every functor $K(\mathcal{A}) \to \mathcal{T}$ that sends quasi-isomorphisms to isomorphisms factors uniquely through $Q$. The categories $D^+(\mathcal{A})$, $D^-(\mathcal{A})$ and $D^b(\mathcal{A})$ are the localizations of $K^+$, $K^-$ and $K^b$ in the same way. The functor $\mathcal{A} \to D(\mathcal{A})$ sends an object $A$ to the complex $A[0]$, with $A$ in degree $0$. The cohomology functors $H^n$ factor through $D(\mathcal{A})$, since they send quasi-isomorphisms to isomorphisms.

Lean: Mathlib `DerivedCategory`, under the assumption `HasDerivedCategory`, with the localization functors `DerivedCategory.Q` from complexes and `DerivedCategory.Qh` from the homotopy category, and `DerivedCategory.homologyFunctor`; the bounded below version is `DerivedCategory.Plus`.

**Theorem P2.8.9 (calculus of fractions).** Let $S$ be the class of quasi-isomorphisms in $K(\mathcal{A})$.

1. $S$ contains the identities and is closed under composition.
2. (Ore condition) For a quasi-isomorphism $s: Y' \to Y$ and a map $f: X \to Y$ there are a quasi-isomorphism $t: X' \to X$ and a map $g: X' \to Y'$ with $s g = f t$. The dual statement also holds.
3. (Cancellation) If $s f = 0$ for a map $f: X \to Y$ and a quasi-isomorphism $s: Y \to Y'$, then $f t = 0$ for some quasi-isomorphism $t: X' \to X$. The dual statement also holds.

So every morphism $X \to Y$ in $D(\mathcal{A})$ is a *roof* $f s^{-1}$, with $X \xleftarrow{s} X' \xrightarrow{f} Y$ and $s$ a quasi-isomorphism, and
$$\operatorname{Hom}_{D(\mathcal{A})}(X, Y) = \operatorname{colim}_{s: X' \to X} \operatorname{Hom}_{K(\mathcal{A})}(X', Y),$$
the colimit over the quasi-isomorphisms with target $X$. Two roofs are equal when they agree after composition with a further quasi-isomorphism. The category $D(\mathcal{A})$ is additive and triangulated, with the images of the distinguished triangles of $K(\mathcal{A})$ as distinguished triangles, and $Q$ sends a map to an isomorphism if and only if the map is a quasi-isomorphism. The same holds for $D^+$, $D^-$ and $D^b$.

Lean: Mathlib `CategoryTheory.MorphismProperty.HasLeftCalculusOfFractions` and `CategoryTheory.MorphismProperty.HasRightCalculusOfFractions`, with instances for `HomotopyCategory.quasiIso`; the triangulated structure is the instance `CategoryTheory.IsTriangulated` on `DerivedCategory`, and the roof description is `DerivedCategory.right_fac` and `DerivedCategory.left_fac`.

**Theorem P2.8.10 (injective replacement).** Let $\mathcal{A}$ have enough injectives.

1. (Key lemma) Let $E$ be an exact complex and $I$ a bounded below complex of injective objects. Then every map of complexes $E \to I$ is homotopic to $0$, so $\operatorname{Hom}_{K(\mathcal{A})}(E, I) = 0$.
2. For every complex $X$ and every bounded below complex $I$ of injectives, $Q$ gives a bijection $\operatorname{Hom}_{K(\mathcal{A})}(X, I) \to \operatorname{Hom}_{D(\mathcal{A})}(X, I)$.
3. Every bounded below complex $K$ has a quasi-isomorphism $K \to I$ into a bounded below complex of injectives.
4. The functor $K^+(\mathcal{I}) \to D^+(\mathcal{A})$, from the homotopy category of bounded below complexes of injectives, is an equivalence of triangulated categories, and $D^+(\mathcal{A}) \to D(\mathcal{A})$ is fully faithful.

Lean: Mathlib `CochainComplex.IsKInjective` for complexes with the property of part 1, `CochainComplex.IsKInjective.Qh_map_bijective` for part 2, `CochainComplex.Plus.exists_quasiIso_injective` for part 3, and `DerivedCategory.Plus.exists_injective_nonempty_iso` for the essential surjectivity in part 4.

**Theorem P2.8.11 (objects, Ext and triangles).** Let $\mathcal{A}$ have enough injectives, and let $A$ and $B$ be objects of $\mathcal{A}$.

1. The functor $\mathcal{A} \to D(\mathcal{A})$ is fully faithful. Its essential image is the class of complexes $X$ with $H^n(X) = 0$ for $n \neq 0$.
2. $\operatorname{Hom}_{D(\mathcal{A})}(A, B[i]) \cong \operatorname{Ext}^i(A, B)$ for $i \geq 0$, and it is $0$ for $i < 0$. The composition in $D(\mathcal{A})$ gives the Yoneda product on Ext.
3. A short exact sequence $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$ in $\mathcal{A}$ gives a distinguished triangle $A \to B \to C \xrightarrow{\delta} A[1]$ in $D(\mathcal{A})$. Under part 2, $\delta \in \operatorname{Ext}^1(C, A)$ is the class of the extension (Proposition P2.3.34), up to a sign fixed by the conventions.

Lean: Mathlib `DerivedCategory.singleFunctor`, with the instances that make it full and faithful; `CategoryTheory.Abelian.Ext`, defined as shifted morphisms in the derived category, with `CategoryTheory.Abelian.Ext.homEquiv`; `CategoryTheory.InjectiveResolution.extEquivCohomologyClass` for the comparison with an injective resolution; and `CategoryTheory.ShortComplex.ShortExact.singleTriangle_distinguished` for part 3.

### Proof in words

The calculus of fractions comes from the cone. A quasi-isomorphism is a map whose cone is exact, and a commutative square can be built by completing a map into a cone to a triangle. The key lemma is a degree by degree construction of a null homotopy, which uses that $E$ is exact and that each $I^n$ is injective. It shows that a complex of injectives cannot see an exact complex, and so it cannot see the difference between $X$ and a quasi-isomorphic complex $X'$. This makes morphisms into $I$ in $D(\mathcal{A})$ equal to morphisms in $K(\mathcal{A})$. With an injective resolution $B \to I_B$, the morphisms from $A$ to $B[i]$ are then homotopy classes of maps $A \to I_B[i]$, which compute $\operatorname{Ext}^i(A, B)$.

### Examples

**Example P2.8.12 (Example P2.3.6 revisited).** The quasi-isomorphism $s: K \to L$ of Example P2.3.6, from $\mathbb{Z} \xrightarrow{n} \mathbb{Z}$ to $\mathbb{Z}/n[-1]$, becomes an isomorphism in $D(\mathsf{Ab})$, with inverse the roof $L \xleftarrow{s} K \xrightarrow{1} K$. In $K(\mathsf{Ab})$ the group $\operatorname{Hom}(\mathbb{Z}/n, \mathbb{Z}[1])$ is $0$, while in $D(\mathsf{Ab})$ it is $\operatorname{Ext}^1(\mathbb{Z}/n, \mathbb{Z}) = \mathbb{Z}/n$ by Theorem P2.8.11. The generator is the roof $\mathbb{Z}/n \leftarrow \operatorname{Cone}(n) \xrightarrow{\pi} \mathbb{Z}[1]$, the third map of the triangle $\mathbb{Z} \xrightarrow{n} \mathbb{Z} \to \mathbb{Z}/n \to \mathbb{Z}[1]$. This answers Example P2.8.7: in $D(\mathsf{Ab})$ the sequence $0 \to \mathbb{Z} \to \mathbb{Z} \to \mathbb{Z}/2 \to 0$ is a triangle, and its third map is not $0$.

**Example P2.8.13 (complexes over a field).** Let $k$ be a field and $K$ a complex of $k$-vector spaces. Write $B^n \subseteq Z^n \subseteq K^n$ for the boundaries and cycles, and choose complements $K^n = Z^n \oplus C^n$ and $Z^n = B^n \oplus H^n$. Then $d$ maps $C^n$ isomorphically to $B^{n+1}$, so $K$ is the direct sum of the complexes $H^n[-n]$, with zero differential, and the contractible complexes $C^n \xrightarrow{\sim} B^{n+1}$. So $K \cong \bigoplus_n H^n(K)[-n]$ already in $K(k)$, and an object of $D(k)$ is determined by its cohomology. Morphisms are also determined: $\operatorname{Hom}_{D(k)}(K, L) = \prod_n \operatorname{Hom}_k(H^n(K), H^n(L))$. The same splitting holds in $D(\mathsf{Ab})$, because $\operatorname{Ext}^2$ vanishes over $\mathbb{Z}$ (Exercise 5), but morphisms are no longer determined by cohomology (Example P2.8.12).

**Example P2.8.14 (a non split triangle over $k[x]$).** Let $A = k[x]$ and $k = A/(x)$. The resolution $0 \to A \xrightarrow{x} A \to k \to 0$ gives the complex $\operatorname{Hom}_A(A, k) \xrightarrow{x} \operatorname{Hom}_A(A, k)$, which is $k \xrightarrow{0} k$. So $\operatorname{Hom}_{D(A)}(k, k) = k$ and $\operatorname{Hom}_{D(A)}(k, k[1]) = \operatorname{Ext}^1_A(k, k) = k$. The nonzero class corresponds to the extension $0 \to k \xrightarrow{x} A/(x^2) \to k \to 0$, which does not split, since $x$ acts as $0$ on $k \oplus k$ but not on $A/(x^2)$. So the triangle $k \to A/(x^2) \to k \xrightarrow{\delta} k[1]$ in $D(A)$ has $\delta \neq 0$. The object $A/(x^2)$ is not the direct sum of the outer terms, although both are modules with cohomology in degree $0$ only.

### Proof

*Theorem P2.8.9.* Part 1 is clear. For part 2, put $s$ in a distinguished triangle $Y' \xrightarrow{s} Y \xrightarrow{u} C \to Y'[1]$. Here $C$ is exact by Proposition P2.8.4. Put $u f: X \to C$ in a distinguished triangle $X' \xrightarrow{t} X \xrightarrow{u f} C \to X'[1]$, by TR1 and TR2. Then the cone of $t$ is $C$ up to isomorphism, so $t$ is a quasi-isomorphism by Proposition P2.8.4. The square formed by $f: X \to Y$ and $1_C$ commutes, so by TR2 and TR3 it extends to a map of rotated triangles, which gives $g: X' \to Y'$ with $s g = f t$.

For part 3, rotate the triangle of $s$ to $C[-1] \xrightarrow{v} Y \xrightarrow{s} Y' \to C$. Since $s f = 0$, exactness of $\operatorname{Hom}(X, -)$ (Proposition P2.8.4) gives $w: X \to C[-1]$ with $f = v w$. Put $w$ in a distinguished triangle $X' \xrightarrow{t} X \xrightarrow{w} C[-1] \to X'[1]$. Since $C[-1]$ is exact, $t$ is a quasi-isomorphism, and $w t = 0$ by Exercise 3 of Section 8.1. So $f t = v w t = 0$. The dual statements follow in the same way with the triangles turned around.

The description of $\operatorname{Hom}_{D(\mathcal{A})}$ by roofs, the facts on additivity, and the triangulated structure follow from parts 1 to 3 by the general theory of localization with a calculus of fractions; see Weibel, Chapter 10, or the Stacks project, chapter Derived categories. If $Q(f)$ is an isomorphism, then $H^n(f)$ is an isomorphism for all $n$, since $H^n$ factors through $Q$. So $f$ is a quasi-isomorphism. $\square$

*Theorem P2.8.10.* Part 1. Let $u: E \to I$ be a map, and let $N$ be such that $I^n = 0$ for $n < N$. Set $h^n = 0: E^n \to I^{n-1}$ for $n \leq N$. Then $u^m = d h^m + h^{m+1} d$ holds for $m < N$, since both sides are $0$. Suppose that $h^m$ is defined for $m \leq n$ and that $u^m = d h^m + h^{m+1} d$ for $m < n$. Let $g = u^n - d h^n: E^n \to I^n$. Then
$$g d = u^n d - d h^n d = d u^{n-1} - d(u^{n-1} - d h^{n-1}) = 0$$
on $E^{n-1}$, so $g$ vanishes on $B^n(E) = Z^n(E)$, where the equality is the exactness of $E$. So $g$ factors through $E^n/Z^n(E) \cong B^{n+1}(E) \subseteq E^{n+1}$. Since $I^n$ is injective, the induced map $B^{n+1}(E) \to I^n$ extends to $h^{n+1}: E^{n+1} \to I^n$, and then $h^{n+1} d = g$, which is $u^n = d h^n + h^{n+1} d$. By induction $u$ is null homotopic.

Part 2. Let $s: X' \to X$ be a quasi-isomorphism and put it in a triangle $X' \xrightarrow{s} X \to C \to X'[1]$, with $C$ exact. The complexes $C[m]$ are exact, so part 1 gives $\operatorname{Hom}_{K(\mathcal{A})}(C[m], I) = 0$ for all $m$. The exact sequence of $\operatorname{Hom}_{K(\mathcal{A})}(-, I)$ (Proposition P2.8.4) then shows that $s^*: \operatorname{Hom}_K(X, I) \to \operatorname{Hom}_K(X', I)$ is bijective. So every transition map in the colimit of Theorem P2.8.9 is bijective, and the colimit is $\operatorname{Hom}_K(X, I)$.

Part 3. Shift so that $K^n = 0$ for $n < 0$. By Proposition P2.4.22, $K$ has a Cartan-Eilenberg resolution $I^{\bullet,\bullet}$, and each column $K^p \to I^{p,\bullet}$ is an injective resolution. Let $I = \operatorname{Tot}(I^{\bullet,\bullet})$, a complex of injectives with $I^n = 0$ for $n < 0$. The map $K \to I$ is a quasi-isomorphism: its cone is the total complex of a first quadrant double complex with exact columns, after a shift, and such a total complex is exact by the spectral sequence of the filtration by columns (Section 4.2), or by a direct induction.

Part 4. By part 2, $\operatorname{Hom}_{K}(I, J) = \operatorname{Hom}_{D}(I, J)$ for bounded below complexes of injectives, so the functor is fully faithful. By part 3 it is essentially surjective. It sends triangles to triangles by construction. For $X, Y$ in $D^+(\mathcal{A})$, choose $Y \to J$ as in part 3. Then $\operatorname{Hom}_{D^+}(X, Y) = \operatorname{Hom}_K(X, J) = \operatorname{Hom}_D(X, Y)$, where the first equality is the same argument inside $K^+$ and the second is part 2. So $D^+(\mathcal{A}) \to D(\mathcal{A})$ is fully faithful. $\square$

*Theorem P2.8.11.* Part 2. Let $B \to I_B$ be an injective resolution, a quasi-isomorphism $B[0] \to I_B$. By Theorem P2.8.10,
$$\operatorname{Hom}_{D}(A, B[i]) = \operatorname{Hom}_D(A, I_B[i]) = \operatorname{Hom}_K(A, I_B[i]).$$
A map of complexes $A[0] \to I_B[i]$ is a map $\varphi: A \to I_B^i$ with $d \varphi = 0$, and it is null homotopic exactly when $\varphi = d \psi$ for some $\psi: A \to I_B^{i-1}$. So $\operatorname{Hom}_K(A, I_B[i]) = H^i(\operatorname{Hom}(A, I_B^\bullet)) = \operatorname{Ext}^i(A, B)$ for $i \geq 0$ (Definition P2.3.29), and it is $0$ for $i < 0$ since $I_B^i = 0$ then. The compatibility with the Yoneda product is a direct check with the comparison theorem P2.3.11; see Weibel, Chapter 10.

Part 1. For $i = 0$, part 2 gives $\operatorname{Hom}_D(A, B) = \operatorname{Ext}^0(A, B) = \operatorname{Hom}(A, B)$, and the map from $\operatorname{Hom}_{\mathcal{A}}(A, B)$ is the identification, so the functor is fully faithful. If $H^n(X) = 0$ for $n \neq 0$, the truncations give quasi-isomorphisms $X \leftarrow \tau_{\leq 0} X \to H^0(X)[0]$, where $\tau_{\leq 0} X$ is $\cdots \to X^{-1} \to Z^0(X) \to 0$. So $X \cong H^0(X)[0]$ in $D(\mathcal{A})$.

Part 3. The complex $\operatorname{Cone}(f)$ is $A \xrightarrow{f} B$ in degrees $-1$ and $0$. Let $c: \operatorname{Cone}(f) \to C$ be $g$ in degree $0$ and $0$ in degree $-1$. This is a map of complexes, since $g f = 0$. It is a quasi-isomorphism: $H^{-1}(\operatorname{Cone}(f)) = \ker f = 0$ and $H^0(\operatorname{Cone}(f)) = B/f(A) \cong C$. The map $c$ is compatible with $\iota: B \to \operatorname{Cone}(f)$ and $g$. So the standard triangle $A \to B \to \operatorname{Cone}(f) \to A[1]$ is isomorphic in $D(\mathcal{A})$ to $A \to B \to C \xrightarrow{\delta} A[1]$ with $\delta = \pi c^{-1}$, which is therefore distinguished. To identify $\delta$, apply $\operatorname{Hom}_D(-, A[1])$ and compare with the connecting map of Proposition P2.3.34; the comparison is in Weibel, Chapter 10. $\square$

### Exercises

1. (A) Show that a map $f$ in $K(\mathcal{A})$ satisfies $Q(f) = 0$ if and only if $s f = 0$ for some quasi-isomorphism $s$.
2. (A) Show that a morphism $\varphi$ in $D(\mathcal{A})$ is an isomorphism if and only if $H^n(\varphi)$ is an isomorphism for every $n$.
3. (A) Let $\mathcal{A}$ have enough injectives. Show that $\operatorname{Hom}_{D(\mathcal{A})}(X, Y[i]) = 0$ for $i < 0$ when $X$ and $Y$ are objects of $\mathcal{A}$, and give an example of complexes $X$ and $Y$ with $\operatorname{Hom}_{D}(X, Y[-1]) \neq 0$.
4. (B) In $D(\mathsf{Ab})$, show that the map $Q(2): \mathbb{Z} \to \mathbb{Z}$ is not a monomorphism, by composing it with a nonzero map $\mathbb{Z}/2[-1] \to \mathbb{Z}$. Deduce, with Exercise 6 of Section 8.1, that the monomorphisms of $\mathsf{Ab}$ and of $D(\mathsf{Ab})$ do not match.
5. (C) Let $K$ be a complex of free abelian groups. Show that $B^{n+1}(K)$ is free, so that $K^n \cong Z^n \oplus C^n$ with $d: C^n \cong B^{n+1}$. Deduce that $K$ is the direct sum of the two-term complexes $C^{n-1} \to Z^n$, and that $K \cong \bigoplus_n H^n(K)[-n]$ in $D(\mathsf{Ab})$. Every complex of abelian groups is quasi-isomorphic to a complex of free abelian groups (Section 8.3), so this holds for all complexes.
6. (B) Compute $\operatorname{Hom}_{D(\mathsf{Ab})}(\mathbb{Z}/m, \mathbb{Z}/n[i])$ for all $i$, and write down the triangle in $D(\mathsf{Ab})$ that the extension $0 \to \mathbb{Z}/p \to \mathbb{Z}/p^2 \to \mathbb{Z}/p \to 0$ gives.
7. (C) Let $\mathcal{A}$ have enough injectives, let $X$ be a bounded below complex and let $X \to I$ be as in Theorem P2.8.10. Let $F: \mathcal{A} \to \mathcal{B}$ be additive. Show that $F(I)$ is well defined up to a unique isomorphism in $K(\mathcal{B})$. This is the first step of the definition of $RF$ in Section 8.3.

### Lean

Mathlib constructs `DerivedCategory` for an abelian category with `HasDerivedCategory`, as the localization of the homotopy category, and proves that it is triangulated. The localization functors are `DerivedCategory.Q` and `DerivedCategory.Qh`, the roofs are `DerivedCategory.right_fac` and `DerivedCategory.left_fac`, and the calculus of fractions is `CategoryTheory.MorphismProperty.HasLeftCalculusOfFractions` and `CategoryTheory.MorphismProperty.HasRightCalculusOfFractions` for `HomotopyCategory.quasiIso`. Injective replacement is `CochainComplex.IsKInjective`, `CochainComplex.IsKInjective.Qh_map_bijective`, `CochainComplex.Plus.exists_quasiIso_injective` and `DerivedCategory.Plus.exists_injective_nonempty_iso`. In Mathlib, `CategoryTheory.Abelian.Ext` is defined as morphisms $A \to B[i]$ in the derived category, so part 2 of Theorem P2.8.11 is a definition there, and `CategoryTheory.InjectiveResolution.extEquivCohomologyClass` is the comparison with injective resolutions. The functor $\mathcal{A} \to D(\mathcal{A})$ is `DerivedCategory.singleFunctor`. The handbook adds no `MinimalModel` node here.

### Notes and history

Grothendieck asked for the derived category around 1960, for the duality theory of coherent sheaves, and Verdier built it in his thesis. Hartshorne's *Residues and duality* was its first systematic use. A morphism in $D(\mathcal{A})$ is in general a roof and not a map of complexes, and this is the price of inverting quasi-isomorphisms. Theorem P2.8.10 removes the price for bounded below complexes when there are enough injectives. For unbounded complexes, injective objects in each degree do not suffice, and K-injective complexes are needed (Section 8.3).
