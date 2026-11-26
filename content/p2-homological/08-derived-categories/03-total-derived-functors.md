---
title: Total derived functors
nodes: []
sources: [Har66, Wei94, Huy06, Spa88, Lip09, Stacks]
reads_with: [Wei94:ch10, Huy06:ch2]
requires: [P2.3, P2.4, P2.6, P2.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Total derived functors

### Statement

Let $F: \mathcal{A} \to \mathcal{B}$ be an additive functor between abelian categories. It acts on complexes degree by degree and on homotopies, so it gives an exact functor $K(F): K(\mathcal{A}) \to K(\mathcal{B})$ of triangulated categories. If $F$ is not exact, $K(F)$ does not send quasi-isomorphisms to quasi-isomorphisms, and it does not descend to $D(\mathcal{A})$. The total derived functor is the best approximation that does.

**Definition P2.8.15 (total derived functors).** A *total right derived functor* of $F$ on $D^+(\mathcal{A})$ is an exact functor $RF: D^+(\mathcal{A}) \to D(\mathcal{B})$ of triangulated categories with a natural transformation $\eta: Q K(F) \to RF\, Q$ of functors on $K^+(\mathcal{A})$, with this universal property: for every exact functor $G: D^+(\mathcal{A}) \to D(\mathcal{B})$ and every natural transformation $\zeta: Q K(F) \to G Q$ there is a unique $\theta: RF \to G$ with $\zeta = \theta Q \circ \eta$. So $RF$ is unique up to a unique isomorphism. The objects $R^i F(X) = H^i(RF(X))$ are the *hyperderived functors* of $F$. A *total left derived functor* $LF: D^-(\mathcal{A}) \to D(\mathcal{B})$ is defined dually, with $\eta: LF\, Q \to Q K(F)$, and $L_i F(X) = H^{-i}(LF(X))$.

Lean: Mathlib `CategoryTheory.Functor.IsRightDerivedFunctor` for the universal property, with `CategoryTheory.Functor.totalRightDerived` and `CategoryTheory.Functor.totalLeftDerived` for the derived functors along a localization.

**Theorem P2.8.16 (existence and computation).** Let $\mathcal{A}$ have enough injectives and let $F: \mathcal{A} \to \mathcal{B}$ be left exact.

1. $RF: D^+(\mathcal{A}) \to D^+(\mathcal{B})$ exists, and $RF(X) = F(I)$ for every quasi-isomorphism $X \to I$ into a bounded below complex of injectives.
2. For an object $A$, $H^i(RF(A)) = R^i F(A)$, the derived functor of Definition P2.3.13. For a nonnegative complex $X$, $H^i(RF(X)) = \mathbb{R}^i F(X)$, the hyperderived functor of Definition P2.4.23. A short exact sequence in $\mathcal{A}$ gives a triangle in $D^+(\mathcal{B})$ whose long exact sequence is that of Theorem P2.3.15.
3. (Acyclic resolutions) If $X \to J$ is a quasi-isomorphism into a bounded below complex of $F$-acyclic objects (Definition P2.3.24), then $RF(X) \cong F(J)$.
4. (Composition) Let $G: \mathcal{C} \to \mathcal{A}$ be left exact, with $\mathcal{C}$ having enough injectives, and suppose that $G$ sends injective objects to $F$-acyclic objects. Then $R(F G) \cong RF \circ RG$.
5. (Unbounded complexes, Spaltenstein) Let $(X, \mathcal{O}_X)$ be a ringed space. Every complex of $\mathcal{O}_X$-modules has a quasi-isomorphism into a K-injective complex $I$, one for which $\operatorname{Hom}_{K}(E, I) = 0$ for every exact $E$. So every additive functor $F$ on $\mathsf{Mod}(\mathcal{O}_X)$ has a total right derived functor $RF: D(\mathcal{O}_X) \to D(\mathcal{B})$ on the whole derived category, with $RF(X) = F(I)$.

Dually, if $\mathcal{A}$ has enough projectives and $F$ is right exact, then $LF: D^-(\mathcal{A}) \to D^-(\mathcal{B})$ exists and is computed by bounded above complexes of projectives, or of $F$-acyclic objects. More generally, a class of objects of $\mathcal{A}$ that is closed under finite sums, such that every object is a quotient of one of its members, and on whose bounded above exact complexes $F$ is exact, computes $LF$ in the same way (Hartshorne, *Residues and duality*, Chapter I).

Lean: Mathlib `CategoryTheory.Functor.rightDerivedFunctorPlus`, the derived functor $D^+(\mathcal{A}) \to D^+(\mathcal{B})$ for enough injectives, with an instance of `CategoryTheory.Functor.IsRightDerivedFunctor`; `CategoryTheory.Functor.mapDerivedCategory` for an exact functor; `CochainComplex.IsKInjective` and `CochainComplex.IsKProjective` for part 5. Parts 3 and 4, and the existence of K-injective resolutions for sheaves, are not in Lean as stated.

**Definition P2.8.17 (the derived functors of geometry).** Let $f: X \to Y$ be a morphism of ringed spaces. By Theorem P2.7.2 and Theorem P2.8.16 the following exist.

1. $R\Gamma(X, -): D^+(\mathcal{O}_X) \to D^+(\mathsf{Ab})$, with $H^i(R\Gamma(X, \mathcal{F})) = H^i(X, \mathcal{F})$ and, for a complex, $H^i(R\Gamma(X, K)) = \mathbb{H}^i(X, K)$, the hypercohomology.
2. $Rf_*: D^+(\mathcal{O}_X) \to D^+(\mathcal{O}_Y)$, with $H^i(Rf_* \mathcal{F}) = R^i f_* \mathcal{F}$.
3. $R\operatorname{Hom}(K, -): D^+(\mathcal{O}_X) \to D^+(\mathsf{Ab})$ and $R\mathcal{H}om(K, -): D^+(\mathcal{O}_X) \to D^+(\mathcal{O}_X)$, for a complex $K$: if $L \to I$ is an injective replacement, these are the total complexes $\operatorname{Hom}^\bullet(K, I)$ and $\mathcal{H}om^\bullet(K, I)$, with $\operatorname{Hom}^n(K, I) = \prod_p \operatorname{Hom}(K^p, I^{p+n})$. They are exact in $K$ as well, and $H^i(R\operatorname{Hom}(K, L)) = \operatorname{Hom}_{D(\mathcal{O}_X)}(K, L[i])$. For sheaves, $H^i(R\mathcal{H}om(\mathcal{F}, \mathcal{G})) = \mathcal{E}xt^i(\mathcal{F}, \mathcal{G})$ and $H^i(R\operatorname{Hom}(\mathcal{F}, \mathcal{G})) = \operatorname{Ext}^i(\mathcal{F}, \mathcal{G})$.
4. $\otimes^L: D^-(\mathcal{O}_X) \times D^-(\mathcal{O}_X) \to D^-(\mathcal{O}_X)$, with $K \otimes^L L = \operatorname{Tot}(K \otimes P)$ for a quasi-isomorphism $P \to L$ from a bounded above complex of flat $\mathcal{O}_X$-modules. On stalks, $H^{-i}(\mathcal{F} \otimes^L \mathcal{G})_x = \operatorname{Tor}_i^{\mathcal{O}_{X,x}}(\mathcal{F}_x, \mathcal{G}_x)$.
5. $Lf^*: D^-(\mathcal{O}_Y) \to D^-(\mathcal{O}_X)$, with $Lf^* L = f^* P$ for $P$ as in part 4, and $L_i f^* \mathcal{G} = H^{-i}(Lf^* \mathcal{G})$.

For parts 4 and 5, every $\mathcal{O}_X$-module is a quotient of a sum of sheaves $j_! \mathcal{O}_U$ (Proposition P2.5.32), which are flat since their stalks are $\mathcal{O}_{X,x}$ or $0$, and the flat modules form a class as at the end of Theorem P2.8.16 for $\otimes$ and $f^*$. With K-injective and K-flat complexes (part 5 of Theorem P2.8.16), all five functors extend to the unbounded derived categories.

Lean: not in Lean as stated. Mathlib has no derived category of sheaves of modules, no $Rf_*$, no $Lf^*$ and no $\otimes^L$; the Hom complex of two cochain complexes is `CochainComplex.HomComplex`.

**Theorem P2.8.18 (identities between derived functors).** Let $f: X \to Y$ and $g: Y \to Z$ be morphisms of ringed spaces.

1. (Composition) $R(g f)_* \cong Rg_* \circ Rf_*$ and $R\Gamma(Y, -) \circ Rf_* \cong R\Gamma(X, -)$ on $D^+(\mathcal{O}_X)$. The Leray spectral sequence (Corollary P2.4.26) is the hypercohomology spectral sequence of $Rf_* \mathcal{F}$.
2. (Adjunction) For $K$ in $D^-(\mathcal{O}_Y)$ and $L$ in $D^+(\mathcal{O}_X)$, $\operatorname{Hom}_{D(\mathcal{O}_X)}(Lf^* K, L) \cong \operatorname{Hom}_{D(\mathcal{O}_Y)}(K, Rf_* L)$. With unbounded complexes, $Lf^*$ is left adjoint to $Rf_*$ on the whole derived categories.
3. (Projection formula, locally free case) For a locally free $\mathcal{O}_Y$-module $\mathcal{E}$ of finite rank and $K$ in $D^+(\mathcal{O}_X)$, $Rf_*(K \otimes f^* \mathcal{E}) \cong Rf_* K \otimes \mathcal{E}$. In particular $R^i f_*(\mathcal{F} \otimes f^* \mathcal{E}) \cong R^i f_* \mathcal{F} \otimes \mathcal{E}$ for a sheaf $\mathcal{F}$.
4. (Projection formula) If $f$ is a quasi-compact and quasi-separated morphism of schemes, $K$ is in $D(\mathcal{O}_X)$ with quasi-coherent cohomology and $L$ is in $D(\mathcal{O}_Y)$, then $Rf_* K \otimes^L L \cong Rf_*(K \otimes^L Lf^* L)$.
5. (Flat base change) Let $f: X \to Y$ be a quasi-compact and quasi-separated morphism of schemes, $u: Y' \to Y$ flat, and $f': X' = X \times_Y Y' \to Y'$ and $u': X' \to X$ the projections. Then $u^* Rf_* K \cong Rf'_* u'^* K$ for $K$ with quasi-coherent cohomology. For a quasi-coherent sheaf, $u^* R^i f_* \mathcal{F} \cong R^i f'_*(u'^* \mathcal{F})$.

Lean: not in Lean as stated.

### Proof in words

Injective replacement makes $D^+(\mathcal{A})$ equivalent to $K^+$ of the injectives, where $F$ is defined, and $RF$ is $F$ applied to the replacement. The universal property holds because an injective complex is its own replacement. A bounded below exact complex of $F$-acyclic objects stays exact under $F$, by splitting it into short exact sequences, and this gives the acyclic resolutions and the composition rule. For geometry, injective sheaves are flasque, and flasque sheaves stay flasque under $f_*$ and are acyclic for every pushforward and for $\Gamma$, which gives the composition of pushforwards. The projection formula reduces to the underived formula of Chapter 6, because tensoring with a locally free sheaf preserves injective sheaves locally.

### Examples

**Example P2.8.19 (the derived restriction to a point).** Let $X = \mathbb{A}^1_k = \operatorname{Spec} k[x]$, $i: \{0\} \to X$ the origin, and $\mathcal{F} = i_* k$, the skyscraper sheaf $k[x]/(x)$. The resolution $0 \to k[x] \xrightarrow{x} k[x] \to k \to 0$ is a flat resolution. Applying $i^* = - \otimes_{k[x]} k$ gives $k \xrightarrow{0} k$ in degrees $-1$ and $0$. So
$$L i^* i_* k \cong k \oplus k[1], \qquad L_0 i^* i_* k = k, \qquad L_1 i^* i_* k = \operatorname{Tor}_1^{k[x]}(k, k) = k.$$
So $L i^* i_*$ is not the identity on $D(k)$, while $i^* i_*$ is the identity on sheaves. The extra term is the conormal space $(x)/(x^2)$ of the point, placed in degree $-1$ (Exercise 4).

**Example P2.8.20 (rational singularities).** Let $X$ be a normal variety over a field of characteristic $0$ and $f: Y \to X$ a resolution of singularities. The variety $X$ has *rational singularities* if the natural map $\mathcal{O}_X \to Rf_* \mathcal{O}_Y$ is an isomorphism in $D(\mathcal{O}_X)$, that is, $f_* \mathcal{O}_Y = \mathcal{O}_X$ and $R^i f_* \mathcal{O}_Y = 0$ for $i > 0$. Then for a locally free sheaf $\mathcal{E}$ on $X$, Theorem P2.8.18 gives
$$R\Gamma(Y, f^* \mathcal{E}) \cong R\Gamma(X, Rf_*(\mathcal{O}_Y \otimes f^* \mathcal{E})) \cong R\Gamma(X, Rf_* \mathcal{O}_Y \otimes \mathcal{E}) \cong R\Gamma(X, \mathcal{E}),$$
so $H^i(Y, f^* \mathcal{E}) \cong H^i(X, \mathcal{E})$ for all $i$. The quadric cone $x y = z^2$ in $\mathbb{A}^3$ has rational singularities, and the cone over a plane cubic curve does not: there $R^1 f_* \mathcal{O}_Y$ is a skyscraper of length $1$ at the vertex. Volume 4 proves both statements and shows that the definition does not depend on the resolution. Klt singularities are rational (Volume 4), and this is one reason that the minimal model program can work in a class of singular varieties without losing cohomological control.

**Example P2.8.21 (Tor of two lines).** Let $A = k[x, y]$ and consider the lines $L_1 = V(y)$ and $L_2 = V(x)$ in $\mathbb{A}^2$. The resolution $A \xrightarrow{y} A$ of $\mathcal{O}_{L_1} = A/(y)$ gives
$$\mathcal{O}_{L_1} \otimes^L \mathcal{O}_{L_2} = \big(k[y] \xrightarrow{y} k[y]\big) \cong k[0],$$
since $y$ is injective on $A/(x) = k[y]$. So the higher Tor sheaves vanish, and the intersection is the reduced point. For $L_1$ with itself the same resolution gives $k[x] \xrightarrow{0} k[x]$, so $\mathcal{O}_{L_1} \otimes^L \mathcal{O}_{L_1}$ has $H^0 = \mathcal{O}_{L_1}$ and $H^{-1} = \mathcal{O}_{L_1}$, the conormal sheaf $(y)/(y^2)$. Serre's formula $\sum_i (-1)^i \operatorname{length} \operatorname{Tor}_i$ for intersection multiplicities is the Euler characteristic of the derived tensor product.

### Proof

*Theorem P2.8.16.* Part 1. By Theorem P2.8.10 the functor $\Phi: K^+(\mathcal{I}) \to D^+(\mathcal{A})$ is an equivalence. Choose an inverse $\Psi$, which sends $X$ to an injective replacement $X \to I_X$, and let $RF = Q K(F) \Psi$. This is exact, since $K(F)$ sends standard triangles to standard triangles. The maps $X \to I_X$ give $\eta_X: F(X) \to F(I_X) = RF(X)$. Given $G$ and $\zeta$, let $\theta_X$ be the composite $RF(X) = F(I_X) \xrightarrow{\zeta_{I_X}} G(I_X) \cong G(X)$, where the last map is $G$ of the inverse of the isomorphism $X \to I_X$ in $D(\mathcal{A})$. Then $\zeta = \theta \circ \eta$ by naturality of $\zeta$. If $X = I$ is a complex of injectives, $\eta_I$ is an isomorphism, so $\theta_I$ is forced, and every $X$ is isomorphic to such an $I$. So $\theta$ is unique.

Part 2. For an object $A$ the replacement is an injective resolution, so $H^i(RF(A)) = H^i(F(I_A)) = R^i F(A)$. For a nonnegative complex, the total complex of a Cartan-Eilenberg resolution is a replacement (proof of Theorem P2.8.10), so $H^i(RF(X)) = \mathbb{R}^i F(X)$. A short exact sequence gives a triangle in $D^+(\mathcal{A})$ by Theorem P2.8.11, $RF$ sends it to a triangle, and Proposition P2.8.4 gives the long exact sequence. The identification of its connecting maps with those of Theorem P2.3.15 uses the horseshoe lemma; see Weibel, Chapter 10.

Part 3. First, let $C$ be a bounded below exact complex of $F$-acyclic objects, with $C^n = 0$ for $n < N$. Let $Z^n = \ker(d: C^n \to C^{n+1})$. Then $Z^N = 0$, and the sequences $0 \to Z^n \to C^n \to Z^{n+1} \to 0$ are exact. By induction on $n$, every $Z^n$ is $F$-acyclic: the long exact sequence of Theorem P2.3.15 gives $R^i F(Z^{n+1}) \cong R^{i+1} F(Z^n) = 0$ for $i \geq 1$. So $0 \to F(Z^n) \to F(C^n) \to F(Z^{n+1}) \to 0$ is exact, since $R^1 F(Z^n) = 0$, and $F(C)$ is exact.

Now let $X \to J$ and $X \to I$ be quasi-isomorphisms, with $I$ injective. By Theorem P2.8.10 part 2 the isomorphism $J \cong I$ in $D(\mathcal{A})$ is a map of complexes $u: J \to I$, a quasi-isomorphism. Its cone has terms $J^{n+1} \oplus I^n$, which are $F$-acyclic, and it is bounded below and exact. So $F(\operatorname{Cone}(u)) = \operatorname{Cone}(F(u))$ is exact, and $F(u): F(J) \to F(I) = RF(X)$ is a quasi-isomorphism.

Part 4. Let $X$ be in $D^+(\mathcal{C})$ and $X \to I$ an injective replacement. Then $RG(X) = G(I)$ is a bounded below complex of $F$-acyclic objects, so $RF(RG(X)) = F(G(I))$ by part 3, which is $R(F G)(X)$.

Part 5 is due to Spaltenstein; K-injective replacements are built as limits of injective replacements of the truncations. See Spaltenstein's paper and the Stacks project, chapter Derived categories. $\square$

*Theorem P2.8.18.* Part 1. Let $\mathcal{I}$ be an injective $\mathcal{O}_X$-module. It is flasque, and $f_* \mathcal{I}$ is flasque (Theorem P2.7.11, parts 1 and 3). A flasque sheaf $\mathcal{G}$ on $Y$ is acyclic for $\Gamma(Y, -)$ (Theorem P2.7.11 part 2) and for $g_*$ (Theorem P2.7.11 part 3). So part 4 of Theorem P2.8.16 applies to $g_* \circ f_* = (g f)_*$ and to $\Gamma(Y, -) \circ f_* = \Gamma(X, -)$. For a sheaf $\mathcal{F}$, the complex $Rf_* \mathcal{F} = f_* I$ is bounded below with cohomology $R^q f_* \mathcal{F}$, and the second hypercohomology spectral sequence of Theorem P2.4.24 for $\Gamma(Y, -)$ and this complex is the Leray spectral sequence.

Part 2 is in Spaltenstein's paper and in Lipman's notes, Chapter 3. On sheaves it is Theorem P2.6.19, and the derived statement follows by choosing a flat replacement of $K$ and a K-injective replacement of $L$ and checking that $f^*$ of the first and $f_*$ of the second are the derived functors.

Part 3. The functor $- \otimes f^* \mathcal{E}$ is exact, since $f^* \mathcal{E}$ is locally free. Let $K \to I$ be an injective replacement. Then $K \otimes f^* \mathcal{E} \to I \otimes f^* \mathcal{E}$ is a quasi-isomorphism. Each $\mathcal{J} = I^n \otimes f^* \mathcal{E}$ is $f_*$-acyclic. Indeed, let $V \subseteq Y$ be open with $\mathcal{E}|_V \cong \mathcal{O}_V^r$. Then $\mathcal{J}|_{f^{-1} V} \cong (I^n|_{f^{-1} V})^r$, which is injective by Theorem P2.7.3 part 3. By Exercise 4 of Section 7.1, $(R^i f_* \mathcal{J})|_V = R^i(f|_{f^{-1}V})_*(\mathcal{J}|_{f^{-1} V}) = 0$ for $i > 0$. Such $V$ cover $Y$, so $R^i f_* \mathcal{J} = 0$. By part 3 of Theorem P2.8.16 and the projection formula P2.6.30,
$$Rf_*(K \otimes f^* \mathcal{E}) \cong f_*(I \otimes f^* \mathcal{E}) \cong f_* I \otimes \mathcal{E} = Rf_* K \otimes \mathcal{E}.$$
Taking $H^i$, and using that $- \otimes \mathcal{E}$ is exact, gives the statement for sheaves.

Parts 4 and 5 need the theory of quasi-coherent sheaves on schemes and are proved in Lipman's notes, Chapter 3, and in the Stacks project, chapter Derived categories of schemes. For a quasi-coherent sheaf and $f$ separated, part 5 also follows from Čech cohomology (Section 7.3): a finite affine cover of $X$ pulls back to an affine cover of $X'$, and the Čech complex commutes with the flat map $u$, since $u^*$ is exact; see Hartshorne, *Algebraic geometry*, Chapter III. $\square$

### Exercises

1. (A) Show that $R\Gamma(X, -)$ sends a short exact sequence of $\mathcal{O}_X$-modules to a triangle whose long exact sequence is that of Theorem P2.7.3.
2. (A) Let $f: X \to Y$ be flat, that is, $\mathcal{O}_{X,x}$ is flat over $\mathcal{O}_{Y, f(x)}$ for all $x$. Show that $Lf^* = f^*$ and that $L_i f^* \mathcal{G} = 0$ for $i > 0$.
3. (B) Let $A = k[x, y]$ and $k = A/(x, y)$. Use the Koszul complex $A \to A^2 \to A$ to compute $k \otimes_A^L k$, and show that its cohomology is $k$, $k^2$ and $k$ in degrees $0$, $-1$ and $-2$.
4. (B) Let $i: Z \to X$ be the inclusion of an effective Cartier divisor, with ideal sheaf $\mathcal{O}_X(-Z)$, and let $\mathcal{F}$ be an $\mathcal{O}_Z$-module. Show that $H^0(L i^* i_* \mathcal{F}) = \mathcal{F}$, $H^{-1}(L i^* i_* \mathcal{F}) \cong \mathcal{F} \otimes \mathcal{O}_Z(-Z)$, and $H^{-j} = 0$ for $j \geq 2$. Compare with Example P2.8.19.
5. (B) Let $f: Y \to X$ and $g: X \to W$ be morphisms with $Rf_* \mathcal{O}_Y = \mathcal{O}_X$. Show that $R(g f)_* \mathcal{O}_Y = Rg_* \mathcal{O}_X$. Deduce that if $g: X \to W$ is a resolution of a normal variety $W$ and $f: Y \to X$ is a proper birational morphism of smooth varieties with $Rf_* \mathcal{O}_Y = \mathcal{O}_X$, then $W$ satisfies the condition of Example P2.8.20 for $g$ if and only if it satisfies it for $g f$.
6. (C) Let $A = k[x, y]/(x y)$ and $k = A/(x, y)$. Construct a free resolution of $k$ over $A$ and show that $\operatorname{Tor}_i^A(k, k) \cong k^2$ for all $i \geq 1$. Deduce that $- \otimes_A^L k$ does not send $D^b$ to $D^b$, and compare with a regular ring, where every finitely generated module has a finite free resolution.

### Lean

Mathlib has the general theory of derived functors along a localization: `CategoryTheory.Functor.IsRightDerivedFunctor`, `CategoryTheory.Functor.totalRightDerived` and `CategoryTheory.Functor.totalLeftDerived`. For an abelian category with enough injectives it constructs `CategoryTheory.Functor.rightDerivedFunctorPlus`, the right derived functor $D^+(\mathcal{A}) \to D^+(\mathcal{B})$. An exact functor induces `CategoryTheory.Functor.mapDerivedCategory`. K-injective and K-projective complexes are `CochainComplex.IsKInjective` and `CochainComplex.IsKProjective`. Mathlib does not yet have the derived category of sheaves of modules, $Rf_*$, $Lf^*$, $\otimes^L$, the projection formula or flat base change. The handbook adds no `MinimalModel` node here.

### Notes and history

The total derived functor and the composition rule $R(F G) = RF \circ RG$ replace the Grothendieck spectral sequence of Chapter 4 by one isomorphism, and the spectral sequence is recovered by applying the cohomology functors. Spaltenstein in 1988 removed the boundedness assumptions, which matter for $\otimes^L$ and for the adjunction $Lf^* \dashv Rf_*$. Example P2.8.20 is the definition of rational singularities that the minimal model program uses; it goes back to Artin for surfaces and to Kempf and his coauthors in general.
