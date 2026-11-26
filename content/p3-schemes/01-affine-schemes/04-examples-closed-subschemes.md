---
title: Examples and closed subschemes
nodes: []
sources: [Vak25, Har77, GW20, Mum99, Stacks]
reads_with: [Vak25:ch4, Har77:II.2, GW20:ch2, Mum99:II.1]
requires: [P1.1, P1.2, P1.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Examples and closed subschemes

### Statement

A quotient $A \to A/I$ is the ring of functions on a closed piece of $\operatorname{Spec} A$, the piece where the functions in $I$ vanish. Different ideals with the same radical give the same closed set and different rings of functions. The scheme remembers the ring.

**Definition P3.1.31 (closed subscheme of an affine scheme).** Let $A$ be a ring and $I \subseteq A$ an ideal. The *closed subscheme* $V(I)$ of $X = \operatorname{Spec} A$ is the affine scheme $\operatorname{Spec} A/I$ with the morphism $i \colon \operatorname{Spec} A/I \to \operatorname{Spec} A$ of the quotient map. Its *support* is the closed set $V(I)$ of P1 Ch. 2. The *reduced subscheme* on $V(I)$ is $\operatorname{Spec} A/\sqrt{I}$, and $X_{\mathrm{red}} = \operatorname{Spec} A/\operatorname{nil}(A)$ is the *reduction* of $X$.

Chapter 3 defines closed subschemes of any scheme and proves that every closed subscheme of an affine scheme is of this form.

**Proposition P3.1.32 (the quotient morphism).** Let $I \subseteq A$ be an ideal and $i \colon \operatorname{Spec} A/I \to \operatorname{Spec} A$ the morphism of the quotient map.

1. The map $i$ is a homeomorphism onto the closed set $V(I)$.
2. The map of sheaves $i^\# \colon \mathcal{O}_{\operatorname{Spec} A} \to i_* \mathcal{O}_{\operatorname{Spec} A/I}$ is surjective. Its stalk at $\mathfrak{p}$ is $A_\mathfrak{p} \to A_\mathfrak{p}/I A_\mathfrak{p}$ for $\mathfrak{p} \in V(I)$, and the stalk of the target is $0$ for $\mathfrak{p} \notin V(I)$.
3. For ideals $I, J$, the closed subschemes $V(I)$ and $V(J)$ have the same support if and only if $\sqrt{I} = \sqrt{J}$, and they are equal as subschemes, that is, isomorphic over $\operatorname{Spec} A$, if and only if $I = J$.

Lean: Mathlib `PrimeSpectrum.isClosedEmbedding_comap_of_surjective` and `PrimeSpectrum.range_comap_of_surjective` for part 1, and `AlgebraicGeometry.IsClosedImmersion.spec_of_surjective` for the statement that the morphism is a closed immersion (proved in Mathlib). Part 3 on supports is `PrimeSpectrum.zeroLocus_radical` with `PrimeSpectrum.vanishingIdeal_zeroLocus_eq_radical`. The equality of subschemes is not in Lean as stated.

**Proposition P3.1.33 (reduced affine schemes).** The scheme $\operatorname{Spec} A$ is *reduced*, that is, every ring $\mathcal{O}(U)$ has no nonzero nilpotents, if and only if $A$ is reduced. The morphism $X_{\mathrm{red}} \to X$ is a homeomorphism, and $X_{\mathrm{red}}$ is reduced.

Lean: Mathlib `AlgebraicGeometry.IsReduced` and `AlgebraicGeometry.affine_isReduced_iff` (proved in Mathlib).

**Definition P3.1.34 (affine space).** Let $A$ be a ring. *Affine $n$-space over $A$* is $\mathbb{A}^n_A = \operatorname{Spec} A[x_1, \dots, x_n]$. For $A = \mathbb{Z}$ it is $\mathbb{A}^n_\mathbb{Z}$, which represents $n$-tuples of global functions by Example P3.1.30.

Lean: Mathlib `AlgebraicGeometry.AffineSpace`, with `AlgebraicGeometry.AffineSpace.toSpecMvPolyIntEquiv` for the universal property and `AlgebraicGeometry.AffineSpace.isoOfIsAffine` for the identification with $\operatorname{Spec}$ of a polynomial ring.

**Proposition P3.1.35 (closed points of affine space).** Let $k$ be an algebraically closed field. The closed points of $\mathbb{A}^n_k$ are the maximal ideals $(x_1 - a_1, \dots, x_n - a_n)$ with $a \in k^n$, and $a \mapsto (x_1 - a_1, \dots, x_n - a_n)$ is a bijection from $k^n$ to the closed points. For a finitely generated $k$-algebra $A = k[x_1, \dots, x_n]/I$, the closed points of $\operatorname{Spec} A$ are the points $a \in k^n$ with $f(a) = 0$ for all $f \in I$, and every nonempty locally closed subset of $\operatorname{Spec} A$ contains a closed point. So the closed points are dense in every closed subset.

Lean: not in Lean as stated. Mathlib has the Nullstellensatz in `Mathlib/RingTheory/Nullstellensatz.lean`.

### Proof in words

The first two parts are a computation. Primes of $A/I$ are primes of $A$ that contain $I$, and the quotient commutes with localization, so the stalks are quotients. The third part shows the difference between a set and a scheme: the support only sees the radical, but the global sections of $\operatorname{Spec} A/I$ are $A/I$, and the morphism to $\operatorname{Spec} A$ recovers $I$ as the kernel on global sections.

For closed points, a maximal ideal of a finitely generated $k$-algebra has residue field finite over $k$ by Theorem P1.4.30, so equal to $k$ when $k$ is algebraically closed. A maximal ideal is then the kernel of evaluation at a point. The same theorem shows that a maximal ideal of a localization $A_f$ contracts to a maximal ideal of $A$. So every nonempty open piece of a closed set contains a closed point, and the classical variety of P0 sits inside the scheme as its set of closed points, and it determines the open and closed sets.

### Examples

**Example P3.1.36 (the affine line over $\mathbb{Z}$).** The scheme $\mathbb{A}^1_\mathbb{Z} = \operatorname{Spec} \mathbb{Z}[x]$ has dimension $2$ (P1 Ch. 5). Its points are of four kinds: the generic point $(0)$; the points $(p)$ for each prime number $p$, whose closures are the lines $\mathbb{A}^1_{\mathbb{F}_p}$; the points $(f)$ for an irreducible $f \in \mathbb{Z}[x]$ of positive degree, whose closures are curves that map onto $\operatorname{Spec} \mathbb{Z}$ minus finitely many points; and the closed points $(p, g)$ with $g$ monic and irreducible mod $p$. The residue field of $(p, g)$ is $\mathbb{F}_p[x]/(\bar g)$, a finite field. This is Mumford's picture of the arithmetic surface. The morphism $\mathbb{A}^1_\mathbb{Z} \to \operatorname{Spec} \mathbb{Z}$ is a family of lines, with fibre $\mathbb{A}^1_{\mathbb{F}_p}$ over $(p)$ and $\mathbb{A}^1_\mathbb{Q}$ over $(0)$, as Chapter 3 shows.

**Example P3.1.37 (the nodal cubic).** Let $k$ be a field of characteristic not $2$ and $A = k[x, y]/(y^2 - x^2(x + 1))$. The polynomial $y^2 - x^2 - x^3$ is irreducible, since it is $y^2 - g$ with $g = x^2(x + 1)$ not a square in $k(x)$. So $A$ is a domain and $C = \operatorname{Spec} A$ is an integral closed subscheme of $\mathbb{A}^2_k$. The map $k[x, y] \to k[t]$, $x \mapsto t^2 - 1$, $y \mapsto t(t^2 - 1)$, kills $y^2 - x^2(x + 1)$, since $t^2 (t^2 - 1)^2 = (t^2 - 1)^2 t^2$. It gives a morphism $\nu \colon \mathbb{A}^1_k \to C$. The image of $A$ in $k[t]$ is the ring $k[t^2 - 1, t(t^2 - 1)]$, and the fraction fields agree, since $t = y/x$. The points $t = 1$ and $t = -1$ both map to the origin $(x, y)$. So $\nu$ is not injective on points, $A \to k[t]$ is injective and not surjective, and $C$ is not isomorphic to $\mathbb{A}^1_k$. The local ring of $C$ at the origin has $\mathfrak{m}/\mathfrak{m}^2$ of dimension $2$, while $C$ has dimension $1$. Chapter 7 calls such a point singular and $\nu$ the normalization.

**Example P3.1.38 (the cuspidal cubic).** Let $A = k[x, y]/(y^2 - x^3)$. The map $x \mapsto t^2$, $y \mapsto t^3$ identifies $A$ with the subring $k[t^2, t^3] \subseteq k[t]$: it is surjective onto that subring by definition, and injective since every element of $A$ has a unique form $a(x) + b(x) y$ and $a(t^2) + b(t^2) t^3$ has only even powers from $a$ and only odd powers from $b$. Let $k$ be algebraically closed. The morphism $\nu \colon \mathbb{A}^1_k \to C = \operatorname{Spec} A$ is a bijection on points and a homeomorphism, since both are irreducible curves whose proper closed sets are finite and $\nu$ is a bijection of closed points. It is not an isomorphism, since $t \notin k[t^2, t^3]$. So a morphism that is a homeomorphism need not be an isomorphism, a second instance of the lesson of Example P3.1.28.

**Example P3.1.39 (the union of the axes and an embedded point).** Let $A = k[x, y]/(xy)$. Then $\operatorname{Spec} A = V(x) \cup V(y)$ is the union of two lines, with two minimal primes $(x)$ and $(y)$ and intersection the reduced point $\operatorname{Spec} k[x, y]/(x, y)$. The scheme-theoretic intersection of $V(y)$ with the parabola $V(y - x^2)$ is $\operatorname{Spec} k[x, y]/(y, y - x^2) = \operatorname{Spec} k[x]/(x^2)$. It is a point of length $2$, which records that the line is tangent to the parabola. The intersection of $V(y)$ with $V(y - x(x - 1))$ is $\operatorname{Spec} k[x]/(x(x - 1)) \cong \operatorname{Spec} k \sqcup \operatorname{Spec} k$, two reduced points. In both cases the line meets a conic in a subscheme of length $2$, the scheme version of Bezout. Compare the ideal $(y^2, xy)$ of Example P3.1.19: it has the same support as the line $V(y)$, and the subscheme has an embedded point at the origin.

**Example P3.1.40 (multiple structures on a line).** In $\mathbb{A}^2_k$ the ideals $(y)$, $(y^2)$ and $(y^2, xy)$ all have radical $(y)$, so they define three closed subschemes with the same support, the $x$-axis. By part 3 of Proposition P3.1.32 they are distinct. The scheme $V(y^2)$ is the double line: its ring $k[x, y]/(y^2)$ is free over $k[x]$ with basis $1, y$, and it is the divisor $2L$ of Chapter 8 for the line $L = V(y)$. The scheme $V(y^2, xy)$ differs from $V(y)$ only at the origin. The program meets these schemes as fibres: the family $y^2 = t$ over the $t$-line has fibre two disjoint lines for $t \neq 0$, in characteristic not $2$ and over a field with $\sqrt{t}$, and the double line over $t = 0$.

**Example P3.1.41 (an open set with no closed point).** Let $R$ be a DVR. Then $\operatorname{Spec} R$ has a nonempty open set $\{(0)\}$ with no closed point of $\operatorname{Spec} R$ in it. So the last statement of Proposition P3.1.35 needs the finiteness hypothesis. For a variety over $k$ the closed points are dense in every closed set, and this is why the classical varieties of P0 lose no information.

### Proof

*Proof of Proposition P3.1.32.* Part 1 is P1 Ch. 2: primes of $A/I$ correspond to primes of $A$ that contain $I$, and the correspondence preserves inclusions and so closed sets: for $J \supseteq I$, the image of $V(J/I)$ is $V(J)$. A continuous bijection onto $V(I)$ that maps closed sets to closed sets is a homeomorphism onto $V(I)$.

Part 2. For $\mathfrak{p} \in V(I)$, the stalk of $i_* \mathcal{O}$ at $\mathfrak{p}$ is the colimit of $(A/I)_a$ over $a \notin \mathfrak{p}$, since the sets $i^{-1}(D(a)) = D(\bar a)$ have sections $(A/I)_a$ by Corollary P3.1.5. This colimit is $(A/I)_\mathfrak{p} = A_\mathfrak{p}/I A_\mathfrak{p}$, by exactness of localization (P1 Ch. 2), and the stalk map is the quotient map, which is surjective. For $\mathfrak{p} \notin V(I)$ there is $a \in I$ with $a \notin \mathfrak{p}$, and then $i^{-1}(D(a)) = D(\bar a) = \emptyset$ since $\bar a = 0$, so the stalk is $0$. A map of sheaves that is surjective on all stalks is surjective as a map of sheaves (P2 Ch. 5).

Part 3. The supports are $V(I)$ and $V(J)$, and $V(I) = V(J)$ if and only if $\sqrt{I} = \sqrt{J}$, since $\sqrt{I}$ is the intersection of the primes that contain $I$ (Theorem P1.1.9). For the subschemes, an isomorphism $\operatorname{Spec} A/I \to \operatorname{Spec} A/J$ over $\operatorname{Spec} A$ is, by Corollary P3.1.23, a ring isomorphism $A/J \to A/I$ compatible with the quotient maps from $A$. Such a map exists only if the kernels agree, so $I = J$. Conversely $I = J$ gives the identity. $\square$

*Proof of Proposition P3.1.33.* If $\operatorname{Spec} A$ is reduced, then $A = \mathcal{O}(\operatorname{Spec} A)$ is reduced. Conversely, let $A$ be reduced. Localizations of a reduced ring are reduced: if $(a/s)^n = 0$ in $A_\mathfrak{p}$, then $t a^n = 0$ for some $t \notin \mathfrak{p}$, so $(ta)^n = 0$ and $ta = 0$, and $a/s = 0$. So every stalk $A_\mathfrak{p}$ is reduced. If $s \in \mathcal{O}(U)$ has $s^n = 0$, then all germs $s_\mathfrak{p}$ are nilpotent, hence zero, and $s = 0$ since sections are determined by their germs. So $\operatorname{Spec} A$ is reduced. For the second statement, $V(\operatorname{nil}(A)) = \operatorname{Spec} A$ by Theorem P1.1.9, so part 1 of Proposition P3.1.32 gives a homeomorphism, and $A/\operatorname{nil}(A)$ is reduced since $\sqrt{\operatorname{nil}(A)} = \operatorname{nil}(A)$. $\square$

*Proof of Proposition P3.1.35.* Let $\mathfrak{m}$ be a maximal ideal of $k[x_1, \dots, x_n]$. By Theorem P1.4.30 the field $K = k[x_1, \dots, x_n]/\mathfrak{m}$ is finite over $k$, so $K = k$ since $k$ is algebraically closed. Let $a_i \in k$ be the image of $x_i$. Then $x_i - a_i \in \mathfrak{m}$, so $(x_1 - a_1, \dots, x_n - a_n) \subseteq \mathfrak{m}$, and the left side is maximal since its quotient is $k$. So they are equal. Distinct $a$ give distinct ideals, since $a$ is recovered as the images of the $x_i$. The closed points of $\operatorname{Spec} A$ are the maximal ideals of $A$, which are the maximal ideals of the polynomial ring that contain $I$, that is, the points $a$ with $I \subseteq \ker(\mathrm{ev}_a)$, that is, $f(a) = 0$ for $f \in I$. Let $Z = V(J) \cap D(f)$ be a nonempty locally closed subset. It is homeomorphic to $\operatorname{Spec} B$ with $B = A_f/J A_f$, by Proposition P3.1.13 and part 1 of Proposition P3.1.32, so $B$ is a nonzero finitely generated $k$-algebra. Let $\mathfrak{n}$ be a maximal ideal of $B$ and $\mathfrak{p}$ its preimage in $A$. By Theorem P1.4.30 the field $B/\mathfrak{n}$ is finite over $k$. The ring $A/\mathfrak{p}$ embeds in $B/\mathfrak{n}$, so it is a domain of finite dimension over $k$, hence a field. So $\mathfrak{p}$ is a closed point of $\operatorname{Spec} A$, and it lies in $Z$. If a closed set $W$ is not the closure of its closed points, then $W$ minus that closure is a nonempty locally closed set with no closed point, which is impossible. $\square$

### Exercises

1. (A) Show that $\operatorname{Spec} \mathbb{Z}[x]/(x^2 + 1) \to \operatorname{Spec} \mathbb{Z}$ has fibre over $(p)$ with two points if $p \equiv 1 \bmod 4$, one point with residue field $\mathbb{F}_{p^2}$ if $p \equiv 3 \bmod 4$, and one point with a nonzero nilpotent in its ring if $p = 2$. (Compare Example P1.4.15.)
2. (A) Let $A = k[x, y]/(y - x^2)$. Show that $A \cong k[x]$, so the parabola is isomorphic to the affine line. Show that the hyperbola $k[x, y]/(xy - 1)$ is isomorphic to $\mathbb{G}_{m, k} = \operatorname{Spec} k[t, t^{-1}]$ and not to $\mathbb{A}^1_k$.
3. (A) List the points of $\operatorname{Spec} \mathbb{R}[x]$ and their residue fields. Show that the closed points correspond to the orbits of complex conjugation on $\mathbb{C}$.
4. (B) In Example P3.1.38, compute $\mathfrak{m}/\mathfrak{m}^2$ for the maximal ideal $\mathfrak{m} = (x, y)$ of $A$, and show that its dimension is $2$. Show that at every other closed point of $C$, over an algebraically closed $k$, the dimension is $1$.
5. (B) Let $I = (y^2, xy) \subseteq k[x, y]$. Show that $I = (y) \cap (x, y)^2$ and that $I = (y) \cap (x, y^2)$, so a primary decomposition is not unique. Show that the associated primes, $(y)$ and $(x, y)$, are the same for both decompositions.
6. (B) Let $X = \operatorname{Spec} A$ and let $I, J$ be ideals. Show that the closed subscheme $V(I + J)$ is the scheme-theoretic intersection and $V(I \cap J)$ is the scheme-theoretic union in the following sense: $V(I + J)$ is the largest closed subscheme contained in both, and $V(I \cap J)$ is the smallest closed subscheme that contains both. Compute $V(I J)$ and $V(I \cap J)$ for $I = (x)$, $J = (x, y)$ in $k[x, y]$, and show they differ.
7. (C) Let $k$ be algebraically closed and $A$ a finitely generated $k$-algebra. Show that the map $Z \mapsto Z \cap \operatorname{Specm} A$ is a bijection from the closed sets of $\operatorname{Spec} A$ to the closed sets of the classical variety $\operatorname{Specm} A$ of P0, and that it identifies the irreducible closed sets with the points of $\operatorname{Spec} A$. (Use Proposition P3.1.35.)

### Lean

Mathlib proves that a surjective ring map gives a closed immersion, `AlgebraicGeometry.IsClosedImmersion.spec_of_surjective`, and on spaces `PrimeSpectrum.isClosedEmbedding_comap_of_surjective` with the image `PrimeSpectrum.range_comap_of_surjective`. Reduced schemes are `AlgebraicGeometry.IsReduced`, and `AlgebraicGeometry.affine_isReduced_iff` is Proposition P3.1.33. Affine space is `AlgebraicGeometry.AffineSpace`, defined by its universal property, with `AlgebraicGeometry.AffineSpace.isoOfIsAffine` comparing it with $\operatorname{Spec}$ of a polynomial ring. The description of closed points over an algebraically closed field is not in Lean as stated for schemes. The handbook adds no `MinimalModel` node here.

### Notes and history

The closed subschemes $\operatorname{Spec} A/I$ and the reduction $X_{\mathrm{red}}$ are in EGA I, Chapter I. Mumford's *Red book*, Section II.1, has the picture of $\operatorname{Spec} \mathbb{Z}[x]$, and Vakil reproduces it. The nodal and cuspidal cubics are the standard first examples of singular curves; Hartshorne uses them in Chapter I and again in Section II.6. The literature state of every statement is theorem. The non-reduced subschemes of this section return in Chapter 8 as divisors $mD$, in Chapter 11 as the centres of blow-ups, and in Chapter 13 as the special fibres of flat families.
