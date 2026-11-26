---
title: Complexes, cohomology and homotopy
nodes: []
sources: [Wei94, Har77]
reads_with: [Wei94:ch1, Har77:ch3]
requires: [P2.1, P2.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Complexes, cohomology and homotopy

### Statement

Throughout, $\mathcal{A}$ is an abelian category. The chapter uses cohomological indexing, since sheaf cohomology is the main application. A chain complex $\cdots \to K_1 \to K_0 \to \cdots$ becomes a cochain complex by the rule $K^n = K_{-n}$.

**Definition P2.3.1 (complexes).** A *complex* $K^\bullet$ in $\mathcal{A}$ is a family of objects $K^n$, $n \in \mathbb{Z}$, with maps $d^n: K^n \to K^{n+1}$, the *differentials*, such that $d^{n+1} d^n = 0$ for all $n$. A *map of complexes* $f: K^\bullet \to L^\bullet$ is a family of maps $f^n: K^n \to L^n$ with $d_L^n f^n = f^{n+1} d_K^n$. The complexes form a category $\mathsf{C}(\mathcal{A})$. The complex is *bounded below* if $K^n = 0$ for $n$ small enough. For an integer $k$, the *shift* $K[k]$ is the complex with $K[k]^n = K^{n+k}$ and differential $(-1)^k d^{n+k}$.

Lean: Mathlib `HomologicalComplex`, with `CochainComplex` and `ChainComplex` for the two indexings.

The category $\mathsf{C}(\mathcal{A})$ is abelian. Kernels and cokernels are taken degree by degree, and a sequence of complexes is exact if and only if it is exact in each degree (Exercise 1).

**Definition P2.3.2 (cohomology).** Let $Z^n = \ker d^n$, the *cocycles*, and $B^n = \operatorname{im} d^{n-1}$, the *coboundaries*. Since $d^n d^{n-1} = 0$, the map $d^{n-1}$ factors through $Z^n$ and $B^n \subseteq Z^n$. The *$n$-th cohomology* is $H^n(K^\bullet) = Z^n / B^n$, the cokernel of $B^n \to Z^n$. A map of complexes sends cocycles to cocycles and coboundaries to coboundaries, so it induces maps $H^n(f): H^n(K^\bullet) \to H^n(L^\bullet)$, and $H^n$ is an additive functor $\mathsf{C}(\mathcal{A}) \to \mathcal{A}$. The complex is *exact*, or *acyclic*, if $H^n(K^\bullet) = 0$ for all $n$. A map $f$ is a *quasi-isomorphism* if every $H^n(f)$ is an isomorphism.

Lean: Mathlib `HomologicalComplex.homology` and `QuasiIso`.

**Definition P2.3.3 (homotopy).** Two maps $f, g: K^\bullet \to L^\bullet$ are *homotopic*, written $f \simeq g$, if there are maps $h^n: K^n \to L^{n-1}$ with
$$f^n - g^n = d_L^{n-1} h^n + h^{n+1} d_K^n \quad \text{for all } n.$$
The family $h$ is a *homotopy*. A map $f: K^\bullet \to L^\bullet$ is a *homotopy equivalence* if there is $g: L^\bullet \to K^\bullet$ with $g f \simeq 1_K$ and $f g \simeq 1_L$. The complex $K^\bullet$ is *contractible* if $1_K \simeq 0$.

Lean: Mathlib `Homotopy` and `HomotopyEquiv`.

Homotopy is an equivalence relation, and it is compatible with sums and composites: if $f \simeq g$ by $h$, then $u f v \simeq u g v$ by $u h v$. An additive functor $F: \mathcal{A} \to \mathcal{B}$ applied degree by degree sends complexes to complexes and homotopies to homotopies, since the formula for a homotopy uses only sums and composites.

**Proposition P2.3.4 (homotopic maps).** If $f \simeq g$, then $H^n(f) = H^n(g)$ for all $n$. A homotopy equivalence is a quasi-isomorphism, and a contractible complex is exact.

Lean: Mathlib `Homotopy.homologyMap_eq` and `HomotopyEquiv.toHomologyIso` (proved in Mathlib).

*Proof.* By additivity of $H^n$ it is enough to show that $u = f - g = d h + h d$ induces $0$. Restrict $u^n$ to $Z^n$, through the inclusion $\iota: Z^n \to K^n$. Then $h^{n+1} d^n \iota = 0$, so $u^n \iota = d_L^{n-1} h^n \iota$. This map factors through $B^n(L) = \operatorname{im} d_L^{n-1}$, so its image in $H^n(L) = Z^n(L)/B^n(L)$ is $0$. So $H^n(u) = 0$. If $g f \simeq 1$ and $f g \simeq 1$, then $H^n(g) H^n(f) = 1$ and $H^n(f) H^n(g) = 1$. If $1_K \simeq 0$, then $1_{H^n(K)} = 0$, so $H^n(K) = 0$. $\square$

**Theorem P2.3.5 (long exact sequence of cohomology).** Let $0 \to K^\bullet \xrightarrow{f} L^\bullet \xrightarrow{g} M^\bullet \to 0$ be a short exact sequence of complexes. There are maps $\delta^n: H^n(M^\bullet) \to H^{n+1}(K^\bullet)$, the *connecting maps*, such that the sequence
$$\cdots \to H^n(K) \xrightarrow{H^n(f)} H^n(L) \xrightarrow{H^n(g)} H^n(M) \xrightarrow{\delta^n} H^{n+1}(K) \xrightarrow{H^{n+1}(f)} H^{n+1}(L) \to \cdots$$
is exact. The maps $\delta^n$ are natural: a map of short exact sequences of complexes gives a map of long exact sequences.

Lean: Mathlib `CategoryTheory.ShortComplex.ShortExact.δ`, with exactness `CategoryTheory.ShortComplex.ShortExact.homology_exact₁`, `homology_exact₂` and `homology_exact₃` (proved in Mathlib).

For modules the connecting map has a direct description. Let $m \in M^n$ be a cocycle. Lift it to $l \in L^n$. Then $g(d l) = d m = 0$, so $d l = f(k)$ for a unique $k \in K^{n+1}$. Then $f(d k) = d d l = 0$ and $f$ is injective, so $d k = 0$. Set $\delta^n [m] = [k]$.

### Proof in words

Cohomology is the defect of exactness of a complex. A homotopy is the algebraic form of a deformation of maps, and it does not change the induced maps on cohomology, because it changes a cocycle only by a coboundary. The long exact sequence is the snake lemma of Section 2.3, applied once in each degree. The snake lemma needs two exact rows with maps between them. The rows are the cokernels of $d^{n-1}$ and the kernels of $d^{n+1}$, and the vertical maps are induced by $d^n$. The kernels and cokernels of these vertical maps are exactly the cohomology objects $H^n$ and $H^{n+1}$, so the snake sequence is a six-term piece of the long exact sequence.

### Examples

**Example P2.3.6 (a quasi-isomorphism with no inverse).** Let $K^\bullet$ be the complex $\mathbb{Z} \xrightarrow{n} \mathbb{Z}$ in degrees $0$ and $1$, with $n \geq 2$. Then $H^0(K) = 0$ and $H^1(K) = \mathbb{Z}/n$. Let $L^\bullet$ be $\mathbb{Z}/n$ in degree $1$ and $0$ elsewhere. The projection $K^1 = \mathbb{Z} \to \mathbb{Z}/n$ is a map of complexes $K^\bullet \to L^\bullet$, and it is a quasi-isomorphism. A map $L^\bullet \to K^\bullet$ is a map $\mathbb{Z}/n \to \mathbb{Z}$ in degree $1$, so it is $0$. So there is no map of complexes in the other direction that induces an isomorphism, and $K^\bullet \to L^\bullet$ is not a homotopy equivalence. The derived category of Chapter 8 inverts all quasi-isomorphisms, and in it $K^\bullet$ and $L^\bullet$ become isomorphic.

**Example P2.3.7 (the de Rham complex of the line).** Let $k$ be a field and $K^\bullet$ the complex $k[x] \xrightarrow{d} k[x]\, dx$ in degrees $0$ and $1$, with $d f = f'\, dx$. If $k$ has characteristic $0$, then $H^0 = k$, the constants, and $H^1 = 0$, since $x^m dx = d(x^{m+1}/(m+1))$. If $k$ has characteristic $p > 0$, then $H^0 = k[x^p]$ and $x^{p-1} dx$ is not exact. Indeed $d$ sends each monomial $x^m$ to a multiple of $x^{m-1} dx$, so only $x^p$ could have $x^{p-1} dx$ as its image, and $d(x^p) = p x^{p-1} dx = 0$. So $H^1 \neq 0$ (Exercise 7). This failure of the Poincaré lemma in characteristic $p$ is the start of the theory of the Cartier operator, which P7 Ch. 11 uses for the Deligne-Illusie proof of Kodaira vanishing.

**Example P2.3.8 (the Bockstein sequence).** Let $p$ be a prime and $K^\bullet$ a complex of abelian groups with no torsion. Multiplication by $p$ gives a short exact sequence of complexes $0 \to K^\bullet \xrightarrow{p} K^\bullet \to K^\bullet/p \to 0$. The long exact sequence reads
$$\cdots \to H^n(K) \xrightarrow{p} H^n(K) \to H^n(K/p) \xrightarrow{\delta} H^{n+1}(K) \xrightarrow{p} H^{n+1}(K) \to \cdots.$$
For $K^\bullet = (\mathbb{Z} \xrightarrow{p} \mathbb{Z})$ in degrees $0$ and $1$, the complex $K/p$ is $\mathbb{Z}/p \xrightarrow{0} \mathbb{Z}/p$. So $H^0(K/p) = H^1(K/p) = \mathbb{Z}/p$, while $H^0(K) = 0$ and $H^1(K) = \mathbb{Z}/p$. The sequence is $0 \to 0 \to \mathbb{Z}/p \xrightarrow{\delta} \mathbb{Z}/p \xrightarrow{0} \mathbb{Z}/p \to \mathbb{Z}/p \to 0$. So $\delta$ is an isomorphism. The recipe for $\delta$ confirms it: lift $1 \in (K/p)^0$ to $1 \in K^0$, apply $d$ to get $p \in K^1$, and divide by $p$ to get the class of $1$ in $H^1(K)$.

### Proof

*Proof of the theorem.* Fix $n$. Write $C^n(K) = \operatorname{coker}(d^{n-1}: K^{n-1} \to K^n) = K^n/B^n$. Apply the snake lemma of Section 2.3 to the map of short exact sequences from degree $n-1$ to degree $n$ given by $d^{n-1}$. Its cokernel part gives an exact sequence $C^n(K) \to C^n(L) \to C^n(M) \to 0$. Apply the snake lemma to the map from degree $n+1$ to degree $n+2$ given by $d^{n+1}$. Its kernel part gives an exact sequence $0 \to Z^{n+1}(K) \to Z^{n+1}(L) \to Z^{n+1}(M)$, where the first map is a monomorphism since $f^{n+1}$ is.

The differential $d^n$ vanishes on $B^n$ and lands in $Z^{n+1}$, since $d^{n+1} d^n = 0$. So it induces $\bar{d}^n: C^n \to Z^{n+1}$ for each of $K$, $L$, $M$, and these maps form a commutative diagram
$$\begin{array}{ccccccc} & C^n(K) & \to & C^n(L) & \to & C^n(M) & \to 0 \\ & \downarrow \bar{d} & & \downarrow \bar{d} & & \downarrow \bar{d} & \\ 0 \to & Z^{n+1}(K) & \to & Z^{n+1}(L) & \to & Z^{n+1}(M) & \end{array}$$
with exact rows. The kernel of $\bar{d}^n: K^n/B^n \to Z^{n+1}$ is $Z^n/B^n = H^n(K)$. Its cokernel is $Z^{n+1}/\operatorname{im} d^n = H^{n+1}(K)$. The same holds for $L$ and $M$. The snake lemma gives an exact sequence
$$H^n(K) \to H^n(L) \to H^n(M) \xrightarrow{\delta^n} H^{n+1}(K) \to H^{n+1}(L) \to H^{n+1}(M).$$
The maps other than $\delta^n$ are the maps $H^n(f)$ and $H^n(g)$, by construction. These six-term sequences overlap for consecutive $n$, so they join into the long exact sequence. Naturality of $\delta^n$ follows from the naturality of the connecting map of the snake lemma, since a map of short exact sequences of complexes induces maps of the two rows above. $\square$

### Exercises

1. (A) Show that $\mathsf{C}(\mathcal{A})$ is an abelian category, with kernels and cokernels computed degree by degree, and that a sequence of complexes is exact if and only if it is exact in each degree.
2. (A) Show that a contractible complex is exact. Show that over a field every exact complex of vector spaces is contractible, and that the complex $0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z} \to \mathbb{Z}/2 \to 0$ is exact but not contractible.
3. (A) Check that the description of $\delta^n$ for modules is well defined: the class $[k]$ does not depend on the choice of the lift $l$ or of the representative $m$.
4. (B) Let $f: K^\bullet \to L^\bullet$ be a map of complexes. The *mapping cone* is the complex $\operatorname{Cone}(f)^n = K^{n+1} \oplus L^n$ with $d(k, l) = (-d k, f(k) + d l)$. Show that $d^2 = 0$, that there is a short exact sequence $0 \to L^\bullet \to \operatorname{Cone}(f) \to K[1]^\bullet \to 0$, and that its connecting map $H^n(K[1]) = H^{n+1}(K) \to H^{n+1}(L)$ is $H^{n+1}(f)$. Deduce that $f$ is a quasi-isomorphism if and only if $\operatorname{Cone}(f)$ is exact.
5. (B) Consider a map of short exact sequences of complexes. Show that if two of the three maps are quasi-isomorphisms, then so is the third.
6. (B) Let $A = k[x, y]$. The *Koszul complex* of $(x, y)$ is $0 \to A \xrightarrow{(-y, x)} A^2 \xrightarrow{(x, y)} A \to 0$ in degrees $0, 1, 2$. Show that it is a complex, that $H^0 = H^1 = 0$, and that $H^2 = k$.
7. (C) Let $k$ have characteristic $p > 0$. Compute the cohomology of the de Rham complex $k[x] \to k[x]\, dx$. Show that $H^0 = k[x^p]$ and that $H^1$ is a free $k[x^p]$-module of rank $1$ with basis the class of $x^{p-1} dx$.

### Lean

Complexes in Mathlib are `HomologicalComplex V c` for a shape `c`, with `CochainComplex V ℤ` for the indexing used here. Cohomology is `HomologicalComplex.homology`. Homotopies are `Homotopy`, homotopy equivalences are `HomotopyEquiv`, and the invariance of cohomology is `Homotopy.homologyMap_eq`. The long exact sequence is built from the snake lemma, as in the proof above: `HomologicalComplex.HomologySequence.snakeInput` is the snake diagram, `ShortComplex.ShortExact.δ` is the connecting map, and the three exactness statements are `ShortComplex.ShortExact.homology_exact₁`, `homology_exact₂` and `homology_exact₃`. Mapping cones are in `Algebra/Homology/HomotopyCofiber.lean`. The handbook adds no `MinimalModel` node here.

### Notes and history

Complexes and their homology come from algebraic topology, where Poincaré defined the Betti numbers through chains on a simplicial complex. Emmy Noether proposed around 1925 to work with the homology groups and not only with their ranks. The connecting map and the long exact sequence were made systematic by Eilenberg and Steenrod in their axioms for homology of 1945 and 1952. The algebraic form used here is the one of Cartan and Eilenberg.
