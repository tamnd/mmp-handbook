---
title: Stalks and affine schemes
nodes: []
sources: [Vak25, Har77, GW20]
reads_with: [Vak25:ch4, Har77:II.2, GW20:ch2]
requires: [P1.2, P2.5, P2.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Stalks and affine schemes

### Statement

Let $A$ be a ring and $X = \operatorname{Spec} A$ with its structure sheaf $\mathcal{O}_X$ (Section 1.1). For a point $\mathfrak{p}$ write $A_\mathfrak{p}$ for the localization at the complement of $\mathfrak{p}$, a local ring with maximal ideal $\mathfrak{p} A_\mathfrak{p}$ (Corollary P1.2.7), and
$$\kappa(\mathfrak{p}) = A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p} = \operatorname{Frac}(A/\mathfrak{p})$$
for its residue field.

**Theorem P3.1.11 (stalks of the structure sheaf).** For every $\mathfrak{p} \in X$ and every $A$-module $M$, the map that sends the germ at $\mathfrak{p}$ of a section $m/f^n \in M_f$ over $D(f) \ni \mathfrak{p}$ to $m/f^n \in M_\mathfrak{p}$ is an isomorphism $\widetilde{M}_\mathfrak{p} \cong M_\mathfrak{p}$. For $M = A$ it is an isomorphism of rings $\mathcal{O}_{X, \mathfrak{p}} \cong A_\mathfrak{p}$. So $(X, \mathcal{O}_X)$ is a locally ringed space (Definition P2.6.1), with residue field $\kappa(\mathfrak{p})$ at $\mathfrak{p}$.

Lean: Mathlib `AlgebraicGeometry.Spec.stalkIso` and the instance `AlgebraicGeometry.StructureSheaf.IsLocalization.to_stalk` (proved in Mathlib); `AlgebraicGeometry.Spec.locallyRingedSpaceObj` is $\operatorname{Spec} A$ as a locally ringed space.

**Definition P3.1.12 (affine scheme).** The locally ringed space $(\operatorname{Spec} A, \mathcal{O}_{\operatorname{Spec} A})$ is the *spectrum* of $A$, written $\operatorname{Spec} A$. An *affine scheme* is a locally ringed space isomorphic to $\operatorname{Spec} A$ for some ring $A$. For a section $s \in \mathcal{O}_X(U)$ and a point $x \in U$, the *value* of $s$ at $x$ is the image $s(x)$ of the germ $s_x$ in the residue field $\kappa(x)$. The section *vanishes* at $x$ if $s(x) = 0$, that is, if $s_x \in \mathfrak{m}_x$.

Lean: Mathlib `AlgebraicGeometry.Spec` (the scheme), `AlgebraicGeometry.IsAffine` (a scheme is affine) and `AlgebraicGeometry.AffineScheme` (the category). The residue field of $\operatorname{Spec} A$ at $\mathfrak{p}$ is identified with $\kappa(\mathfrak{p})$ by `AlgebraicGeometry.Scheme.Spec.residueFieldIso`.

For $f \in A$ and $\mathfrak{p} \in X$, the value $f(\mathfrak{p})$ is the image of $f$ in $\kappa(\mathfrak{p})$. It is zero if and only if $f \in \mathfrak{p}$. So $V(f)$ is the zero set of $f$ and $D(f)$ is the set where $f$ does not vanish, which is the meaning of the notation. The values of $f$ lie in different fields at different points: the value of $15 \in \mathbb{Z}$ is $1$ in $\mathbb{F}_7$ at $(7)$, $0$ in $\mathbb{F}_5$ at $(5)$, and $15$ in $\mathbb{Q}$ at $(0)$.

**Proposition P3.1.13 (basic open sets are affine).** For $f \in A$, the open set $D(f)$ with the restricted sheaf $\mathcal{O}_X|_{D(f)}$ is isomorphic, as a locally ringed space, to $\operatorname{Spec} A_f$. The isomorphism is the homeomorphism $\operatorname{Spec} A_f \to D(f)$, $\mathfrak{q} \mapsto \mathfrak{q} \cap A$, of Proposition P1.2.19, together with the isomorphisms $\mathcal{O}_X(D(fg)) = A_{fg} \cong (A_f)_g$.

Lean: Mathlib `AlgebraicGeometry.basicOpenIsoSpecAway` (as schemes) and the instance `AlgebraicGeometry.Scheme.isOpenImmersion_SpecMap_localizationAway` (proved in Mathlib).

**Proposition P3.1.14 (units and nilpotents).** Let $U \subseteq X$ be open and $s \in \mathcal{O}_X(U)$.

1. $s$ is a unit in $\mathcal{O}_X(U)$ if and only if $s(x) \neq 0$ for all $x \in U$.
2. For $f \in A$, $f(\mathfrak{p}) = 0$ for all $\mathfrak{p} \in X$ if and only if $f$ is nilpotent.
3. The set $\{x \in U : s(x) \neq 0\}$ is open.

Part 1 holds on every locally ringed space, and so does part 3.

Lean: Mathlib `AlgebraicGeometry.RingedSpace.isUnit_of_isUnit_germ` for part 1 and `AlgebraicGeometry.LocallyRingedSpace.basicOpen_eq_bot_of_isNilpotent` for one direction of part 2, proved in Mathlib. Part 2 is `PrimeSpectrum.basicOpen_eq_bot_iff` on the level of spaces.

### Proof in words

A germ at $\mathfrak{p}$ is a fraction $m/f^n$ defined on some $D(f)$ with $f \notin \mathfrak{p}$, and two fractions have the same germ when they agree on a smaller $D(g)$. Every denominator $s \notin \mathfrak{p}$ defines its own basic open set $D(s) \ni \mathfrak{p}$, so every element of $M_\mathfrak{p}$ is a germ, and an element that dies in $M_\mathfrak{p}$ is killed by some $t \notin \mathfrak{p}$, so it dies on $D(t)$. That is the stalk theorem. The ring $A_\mathfrak{p}$ is local, so $\operatorname{Spec} A$ is a locally ringed space. Its residue field at $\mathfrak{p}$ is the field in which the values of functions at $\mathfrak{p}$ live.

Proposition P3.1.13 says that the open set $D(f)$ is again an affine scheme. This is what makes affine schemes a good local model: every point has a basis of neighbourhoods that are affine. The proposition on units says that a function is invertible where it does not vanish, as for continuous or holomorphic functions. The difference with those cases is part 2: a function can vanish at every point without being zero, if it is nilpotent.

### Examples

**Example P3.1.15 (a field).** For a field $K$, $\operatorname{Spec} K$ is one point $(0)$, with $\mathcal{O}((0)\text{ as a set}) = K$ and stalk $K$. Two fields give homeomorphic spaces, and the spectra are isomorphic as locally ringed spaces only if the fields are isomorphic, since $\Gamma(\operatorname{Spec} K, \mathcal{O}) = K$. So $\operatorname{Spec} \mathbb{Q}$, $\operatorname{Spec} \mathbb{F}_p$ and $\operatorname{Spec} \mathbb{C}$ are three different points. The structure sheaf carries the information that the topology does not.

**Example P3.1.16 (the dual numbers).** Let $k$ be a field and $A = k[\epsilon]/(\epsilon^2)$. The only prime is $(\epsilon)$, so $X = \operatorname{Spec} A$ is one point with $\mathcal{O}_X(X) = A = \mathcal{O}_{X, (\epsilon)}$ and residue field $k$. The function $\epsilon$ has value $0$ at the only point, and it is not zero. So part 2 of Proposition P3.1.14 cannot be strengthened: a function is not determined by its values. The scheme $\operatorname{Spec} k$ has the same space, and it is not isomorphic to $X$. The point of view of the program is that $X$ is a point with a tangent vector, the "first order neighbourhood" of a point on a line. In the same way $\operatorname{Spec} k[x]/(x^n)$ is a point with $n - 1$ orders of contact.

**Example P3.1.17 (a discrete valuation ring).** Let $R$ be a DVR with uniformizer $t$ and fraction field $K$, for example $\mathbb{Z}_{(p)}$ or $k[x]_{(x)}$. Then $\operatorname{Spec} R = \{(0), (t)\}$, the open sets are $\emptyset$, $\{(0)\} = D(t)$ and $X$, and $\mathcal{O}(D(t)) = R_t = K$, $\mathcal{O}(X) = R$. The closed point $(t)$ has stalk $R$, residue field $R/(t)$, and the generic point has stalk and residue field $K$. This two point space is the germ of a smooth curve. Chapter 4 uses it to test properness: a map from $\operatorname{Spec} R$ is a curve germ with its special point, and a map from $\operatorname{Spec} K$ is the same germ with the special point removed. This is P2 Exercise 6 of Section 6.1 in the language of schemes.

**Example P3.1.18 (the real line).** Let $X = \operatorname{Spec} \mathbb{R}[x]$. Its closed points are the ideals $(x - a)$, $a \in \mathbb{R}$, with residue field $\mathbb{R}$, and the ideals $(x^2 + bx + c)$ with $b^2 < 4c$, with residue field $\mathbb{C}$. A closed point of the second kind is a pair of complex conjugate points $\{z, \bar{z}\}$ of $\mathbb{C}$. The value of $f = x$ at the point $(x^2 + 1)$ is the class of $x$ in $\mathbb{R}[x]/(x^2 + 1) \cong \mathbb{C}$, which is $\pm i$ depending on the choice of the isomorphism. So the value of a function at a point is well defined, but its comparison with a number needs a choice when the residue field is larger than the base field.

**Example P3.1.19 (a ring that is not reduced, at a non-closed point).** Let $A = k[x, y]/(y^2, xy)$, the line $y = 0$ with an embedded point at the origin. The primes of $A$ contain $y$, so $\operatorname{Spec} A$ has the space of the line $\operatorname{Spec} k[x]$. At the generic point $\mathfrak{p} = (y)$, the stalk is $A_\mathfrak{p}$, and $x \notin \mathfrak{p}$ is a unit there, so $y = x^{-1} \cdot xy = 0$ in $A_\mathfrak{p}$, and $A_\mathfrak{p} = k(x)$ is a field. At the origin $(x, y)$ the element $y$ is not zero in the stalk, since no $s \notin (x, y)$ kills it. So the nilpotent $y$ is a section whose support is the single point $(x, y)$. Chapter 3 calls this point an embedded point.

**Example P3.1.20 (an open subset that is not affine).** Let $U = D(x) \cup D(y)$ in $X = \operatorname{Spec} k[x, y]$ (Example P3.1.10). Then $\mathcal{O}_X(U) = k[x, y]$ and the stalks of $\mathcal{O}_X|_U$ are those of $X$ at the points of $U$. Suppose that $U$ is affine, with an isomorphism of locally ringed spaces $U \cong \operatorname{Spec} B$. It identifies $B$ with $\mathcal{O}(U) = k[x, y]$, and a point $u \in U$ with a prime $\mathfrak{q}$ of $B$ such that a section vanishes at $u$ exactly when it lies in $\mathfrak{q}$. The ideal $(x, y)$ of $B = k[x, y]$ is proper, so it lies in a prime $\mathfrak{q}$, and at the corresponding point $u \in U$ both $x$ and $y$ vanish. But a point of $U$ lies in $D(x)$ or in $D(y)$, so $x$ or $y$ does not vanish there. This is a contradiction. So an open subset of an affine scheme need not be affine.

### Proof

*Proof of the theorem.* The basic open sets that contain $\mathfrak{p}$ form a cofinal family among all open neighbourhoods of $\mathfrak{p}$, so $\widetilde{M}_\mathfrak{p} = \operatorname{colim}_{f \notin \mathfrak{p}} M_f$, a filtered colimit (Example P2.1.48), with the maps $M_g \to M_f$ for $D(f) \subseteq D(g)$. For $f \notin \mathfrak{p}$, the map $M_f \to M_\mathfrak{p}$ exists because $f$ is a unit in $A_\mathfrak{p}$, and these maps are compatible with the maps $M_g \to M_f$ by the uniqueness in Lemma P3.1.1. So they define $\varphi \colon \widetilde{M}_\mathfrak{p} \to M_\mathfrak{p}$.

$\varphi$ is surjective: an element $m/s$ of $M_\mathfrak{p}$ with $s \notin \mathfrak{p}$ is the image of $m/s \in M_s$, a section over $D(s) \ni \mathfrak{p}$. $\varphi$ is injective: let $m/f^n \in M_f$ with $f \notin \mathfrak{p}$ map to $0$ in $M_\mathfrak{p}$. Then $t m = 0$ for some $t \notin \mathfrak{p}$. The set $D(ft)$ contains $\mathfrak{p}$, and in $M_{ft}$ the element $m/f^n = tm/(t f^n) = 0$. So the germ is $0$. For $M = A$ the maps are ring maps, so $\varphi$ is a ring isomorphism. By Corollary P1.2.7, $A_\mathfrak{p}$ is local with residue field $\kappa(\mathfrak{p})$. $\square$

*Proof of Proposition P3.1.13.* Write $j \colon \operatorname{Spec} A_f \to D(f)$ for the homeomorphism of Proposition P1.2.19. The basic open sets of $\operatorname{Spec} A_f$ are the $D(a/f^n) = D(a/1)$, and $j$ maps $D(a/1)$ onto $D(af)$. So $j$ matches the basis $\{D(a/1)\}$ of $\operatorname{Spec} A_f$ with the basis $\{D(g) : D(g) \subseteq D(f)\}$ of $D(f)$, since $D(g) \subseteq D(f)$ gives $D(g) = D(gf)$. On these, $\mathcal{O}_{\operatorname{Spec} A_f}(D(a/1)) = (A_f)_a$ and $\mathcal{O}_X(D(af)) = A_{af}$, and the natural map $A_{af} \to (A_f)_{a}$ is an isomorphism of rings, compatible with restriction by the uniqueness in Lemma P3.1.1. So $j^{-1}$ of the sheaf on the basis is isomorphic to the sheaf on the basis of $\operatorname{Spec} A_f$, and by Theorem P2.5.34 the isomorphism extends uniquely to an isomorphism of sheaves of rings $\mathcal{O}_X|_{D(f)} \cong j_* \mathcal{O}_{\operatorname{Spec} A_f}$. The maps on stalks are isomorphisms, so they are local, and $j$ is an isomorphism of locally ringed spaces. $\square$

*Proof of Proposition P3.1.14.* Part 1. If $s$ is a unit, its germs are units, so they lie outside $\mathfrak{m}_x$. Conversely, let $s(x) \neq 0$ for all $x \in U$. Then $s_x \notin \mathfrak{m}_x$, so $s_x$ is a unit of the local ring $\mathcal{O}_{X, x}$. Choose a neighbourhood $V_x \subseteq U$ of $x$ and $t^x \in \mathcal{O}(V_x)$ with $(s t^x)_x = 1$. Shrinking $V_x$, $s|_{V_x} t^x = 1$. On $V_x \cap V_y$ both $t^x$ and $t^y$ are inverses of $s$, so they agree, and they glue to $t \in \mathcal{O}(U)$ with $st = 1$ by the sheaf axiom. Part 3. If $s(x) \neq 0$, the open set $V_x$ of part 1 is a neighbourhood of $x$ on which $s$ is a unit, so $s(y) \neq 0$ for $y \in V_x$. Part 2. $f(\mathfrak{p}) = 0$ means $f \in \mathfrak{p}$, and the intersection of all primes is the nilradical (P1 Ch. 1). $\square$

### Exercises

1. (A) Describe the points, the open sets, the stalks and the residue fields of $\operatorname{Spec} \mathbb{Z}_{(p)}$, $\operatorname{Spec} \mathbb{Z}/(p^2)$ and $\operatorname{Spec} \mathbb{Z}/(6)$. Which of them are isomorphic as topological spaces?
2. (A) Show that a locally ringed space $X$ with one point is affine. (Its ring of global sections is the stalk, and it is local; compute $\operatorname{Spec}$ of a local ring with one prime.) Which local rings have exactly one prime?
3. (A) Let $X = \operatorname{Spec} \mathbb{C}[x, y]$ and $\mathfrak{p} = (y^2 - x^3)$. Describe the closure of the point $\mathfrak{p}$, its stalk and its residue field. Show that the value of $x$ at $\mathfrak{p}$ is $t^2$ under an isomorphism $\kappa(\mathfrak{p}) \cong \mathbb{C}(t)$.
4. (B) Prove that $\widetilde{M}_\mathfrak{p} \cong M_\mathfrak{p}$ gives: $\widetilde{M} = 0$ if and only if $M = 0$, and the support $\{\mathfrak{p} : \widetilde{M}_\mathfrak{p} \neq 0\}$ of a finitely generated module $M$ is $V(\operatorname{Ann} M)$. Give a module $M$ over $\mathbb{Z}$ whose support is not closed.
5. (B) Let $A = k[x, y]/(y^2, xy)$ as in Example P3.1.19. For each point $\mathfrak{p}$ of $\operatorname{Spec} A$, decide whether $\mathcal{O}_{X, \mathfrak{p}}$ is reduced. Show that the set of points where the stalk is not reduced is closed.
6. (B) Let $e \in A$ be idempotent. Show that $D(e) = V(1 - e)$ is open and closed, that $A_e \cong A/(1 - e)$, and that $\operatorname{Spec} A$ is the disjoint union of the affine schemes $\operatorname{Spec} A_e$ and $\operatorname{Spec} A_{1 - e}$ as locally ringed spaces.
7. (B) Let $X$ be an affine scheme and $f \in \Gamma(X, \mathcal{O}_X)$. Define $X_f = \{x : f(x) \neq 0\}$. Show that $X_f$ is affine with ring $\Gamma(X, \mathcal{O}_X)_f$. (Reduce to Proposition P3.1.13 by an isomorphism $X \cong \operatorname{Spec} A$.)

### Lean

Mathlib has the stalk isomorphism as `AlgebraicGeometry.Spec.stalkIso`, the locally ringed space $\operatorname{Spec} A$ as `AlgebraicGeometry.Spec.locallyRingedSpaceObj`, and the scheme as `AlgebraicGeometry.Spec`. A scheme is affine if the map to $\operatorname{Spec}$ of its global sections is an isomorphism, `AlgebraicGeometry.IsAffine`; this is equivalent to Definition P3.1.12 by the theorem of Section 1.3. The isomorphism of Proposition P3.1.13 is `AlgebraicGeometry.basicOpenIsoSpecAway`. The criterion for units is `AlgebraicGeometry.RingedSpace.isUnit_of_isUnit_germ`. The value of a section at a point and the residue field are `AlgebraicGeometry.Scheme.residueField` with the map `AlgebraicGeometry.Scheme.residue`. The handbook adds no `MinimalModel` node here.

### Notes and history

The local rings $A_\mathfrak{p}$ and their residue fields were used by Krull and by Chevalley in the 1940s. Chevalley defined the "schemas" of his 1955 seminar as sets of local rings in a function field, and Grothendieck's definition replaced the function field by an arbitrary ring and the set of local rings by the locally ringed space $\operatorname{Spec} A$. The insistence on all primes, and not only the maximal ideals, is what makes $\operatorname{Spec}$ a functor (P1.2.19). The literature state of every result here is theorem. Hartshorne proves the stalk theorem as part of Proposition II.2.2, and Vakil and Görtz-Wedhorn prove it in the same way as here.
