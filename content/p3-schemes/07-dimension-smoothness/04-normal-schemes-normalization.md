---
title: Normal schemes, finite morphisms and the normalization
nodes: []
sources: [Vak25, Har77, GW20, EGA1, Stacks]
reads_with: [Vak25:ch9, Har77:II.6, GW20:ch12]
requires: [P1.4, P1.8, P1.11, P3.3, P3.4, P3.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Normal schemes, finite morphisms and the normalization

### Statement

**Definition P3.7.31 (normal scheme).** A scheme $X$ is *normal* if every local ring $\mathcal{O}_{X, x}$ is a normal domain, that is, a domain that is integrally closed in its fraction field (Definition P1.4.18). For a locally Noetherian scheme, $X$ satisfies *Serre's condition $S_2$* if $\operatorname{depth} \mathcal{O}_{X, x} \geq \min(2, \dim \mathcal{O}_{X, x})$ for every $x$.

Lean: Mathlib `IsIntegrallyClosed` for rings (definition). There is no normal scheme in Mathlib; it is not in Lean as stated.

**Proposition P3.7.32 (first properties of normal schemes).** Let $X$ be a scheme.

1. If $X = \operatorname{Spec} A$ with $A$ a domain, then $X$ is normal if and only if $A$ is normal. Normality is local: $X$ is normal if and only if it has an open cover by normal schemes.
2. A normal scheme is reduced. If $X$ is normal and locally Noetherian, its irreducible components are open and pairwise disjoint, they are its connected components, and each is an integral normal scheme.
3. A regular scheme is normal.
4. Let $X$ be integral and locally Noetherian. Then $X$ is normal if and only if it satisfies $R_1$ and $S_2$. In particular the singular points of a normal scheme have codimension at least $2$: every $x$ with $\dim \mathcal{O}_{X, x} \leq 1$ is regular.
5. An integral locally Noetherian scheme of dimension $1$ is normal if and only if it is regular.

Lean: not in Lean as stated. Mathlib `isIntegrallyClosed_of_isLocalization` and `IsIntegrallyClosed.of_localization_maximal` are the algebraic input of part 1 (proved in Mathlib).

**Theorem P3.7.33 (Hartogs property).** Let $X$ be a normal integral Noetherian scheme and $Z \subseteq X$ a closed subset of codimension at least $2$, that is, $\operatorname{codim}(W, X) \geq 2$ for every irreducible component $W$ of $Z$. Then the restriction $\mathcal{O}_X(X) \to \mathcal{O}_X(X \setminus Z)$ is an isomorphism.

Lean: not in Lean as stated.

**Proposition P3.7.34 (finite morphisms).** Let $f \colon X \to Y$ be a finite morphism.

1. Every fibre $f^{-1}(y)$ is a finite discrete set.
2. $f$ is proper, in particular closed.
3. If $Y$ is locally Noetherian, then $\dim X \leq \dim Y$, with equality if $f$ is surjective.
4. If $Y = \operatorname{Spec} A$ and $\mathcal{O}_X(X) = B$ with $A \to B$ injective, then $f$ is surjective.

Lean: Mathlib `AlgebraicGeometry.IsFinite` and the instance that a finite morphism is proper (definitions and proved in Mathlib). Parts 1, 3 and 4 are not in Lean as stated for schemes; Mathlib `Ideal.exists_ideal_over_prime_of_isIntegral` is the lying over theorem behind part 4.

**Definition P3.7.35 (normalization).** Let $X$ be an integral scheme. A *normalization* of $X$ is a dominant morphism $\nu \colon \widetilde{X} \to X$ from a normal integral scheme with the following property: every dominant morphism $f \colon Y \to X$ from a normal integral scheme $Y$ factors as $f = \nu \circ g$ for a unique morphism $g \colon Y \to \widetilde{X}$.

Lean: Mathlib `AlgebraicGeometry.Scheme.Hom.normalization` is the relative normalization of a quasi-compact and quasi-separated morphism, with `toNormalization`, `fromNormalization` and the factorization `normalizationDesc` through integral morphisms (definitions and proved in Mathlib). The normalization of an integral scheme as defined here is not in Lean as stated.

**Theorem P3.7.36 (existence of the normalization).** Let $X$ be an integral scheme with function field $K$.

1. There is a quasi-coherent $\mathcal{O}_X$-algebra $\widetilde{\mathcal{O}}_X$ with $\widetilde{\mathcal{O}}_X(U) = \widetilde{A}$, the integral closure of $A$ in $K$, for every affine open $U = \operatorname{Spec} A$.
2. The morphism $\nu \colon \widetilde{X} = \operatorname{\mathbf{Spec}}_X \widetilde{\mathcal{O}}_X \to X$ is a normalization of $X$. It is affine, integral and dominant, it induces an isomorphism of function fields, and it is an isomorphism over every open set on which $X$ is normal.
3. If $X$ is of finite type over a field, then $\nu$ is finite and surjective, $\widetilde{X}$ is of finite type over the field, and $\dim \widetilde{X} = \dim X$.

Lean: Mathlib `AlgebraicGeometry.Scheme.Hom.normalization`, applied to the morphism from the spectrum of the function field, is the construction of part 2 (definition). The theorem as stated is not in Lean as stated.

### Proof in words

Normality is a property of local rings, so it is local, and the algebra of P1 Ch. 4 and Ch. 11 translates directly: a normal domain is the intersection of its localizations at height one primes, which are discrete valuation rings. That intersection is the Hartogs property: a function defined away from codimension two extends. The normalization is built affine by affine as the spectrum of the integral closure, and it glues because integral closure commutes with localization. Its universal property comes from the same fact read in the function field of the source: an element integral over the coordinate ring maps to an element integral over a normal ring, which lies in that ring. Over a field the integral closure is a finite module, so the normalization is finite.

### Examples

**Example P3.7.37 (the cones $xy = z^n$).** Let $n \geq 1$ and $X = V(xy - z^n) \subseteq \mathbb{A}^3_k$. By Example P1.11.15, $X$ is normal over a perfect field. It is smooth away from the origin, and for $n \geq 2$ the origin is singular, as $xy - z^n \in \mathfrak{m}^2$. The singular locus has codimension $2$, as part 4 of Proposition P3.7.32 requires. These are the $A_{n-1}$ singularities, and $X$ is the quotient of $\mathbb{A}^2_k$ by the group $\mu_n$ acting by $(s, t) \mapsto (\zeta s, \zeta^{-1} t)$, with $x = s^n$, $y = t^n$ and $z = st$, when $\operatorname{char} k \nmid n$. Chapter 8 computes $\operatorname{Cl}(X) = \mathbb{Z}/n$, generated by the line $V(x, z)$, as in Example P1.8.14. The cone $V(xw - yz) \subseteq \mathbb{A}^4_k$ over a smooth quadric surface is normal for the same reason, and its class group is $\mathbb{Z}$ (Example P1.8.15).

**Example P3.7.38 (the node).** Let $\operatorname{char} k \neq 2$ and $A = k[x, y]/(y^2 - x^2(x + 1))$. In $K = \operatorname{Frac}(A)$ put $t = y/x$. Then $t^2 = x + 1$, so $t$ is integral over $A$, and $x = t^2 - 1$, $y = tx = t(t^2 - 1)$. So $A \subseteq k[t] \subseteq K$, and $k[t]$ is the integral closure, as it is normal (Proposition P1.4.19) with fraction field $K$ and integral over $A$. The normalization is $\nu \colon \mathbb{A}^1_k \to X$, $t \mapsto (t^2 - 1, t(t^2 - 1))$. It is finite and surjective, an isomorphism over $X \setminus \{0\}$, and the fibre over the node is $\operatorname{Spec} k[t]/(t^2 - 1, t(t^2 - 1)) = \{t = 1\} \cup \{t = -1\}$, the two branches.

**Example P3.7.39 (the cusp).** For $A = k[x, y]/(y^2 - x^3)$ the element $t = y/x$ satisfies $t^2 = x$ and $t^3 = y$, and the normalization is $\mathbb{A}^1_k \to X$, $t \mapsto (t^2, t^3)$, as in Example P3.3.15. It is a bijection, and a homeomorphism, as a finite morphism is closed, but it is not an isomorphism: the map on local rings at the origin is $k[t^2, t^3]_{(t^2, t^3)} \to k[t]_{(t)}$, which is not surjective. This is the standard example of a finite birational morphism that is bijective and not an isomorphism.

**Example P3.7.40 (the Whitney umbrella).** Let $\operatorname{char} k \neq 2$ and $X = V(x^2 - y^2 z) \subseteq \mathbb{A}^3_k$. The element $t = x/y$ satisfies $t^2 = z$, so it is integral, and $A = k[x, y, z]/(x^2 - y^2 z) \cong k[y, yt, t^2] \subseteq k[y, t]$. The normalization is $\mathbb{A}^2_k \to X$, $(y, t) \mapsto (yt, y, t^2)$. The scheme $X$ is singular along the line $x = y = 0$, which has codimension $1$, so it fails $R_1$, as Example P1.11.16 shows. Over a point $(0, 0, c)$ of this line with $c \neq 0$ a square, $c = a^2$, the fibre consists of the two points $(0, \pm a)$. Over the origin it is one point.

**Example P3.7.41 (Hartogs on the plane).** Let $X = \mathbb{A}^2_k$ and $Z$ the origin. Then $\mathcal{O}(X \setminus Z) = k[x, y]$ by Example P3.1.10, as Theorem P3.7.33 predicts, and so $X \setminus Z$ is not affine. On the other hand, on the union $X = V(x, y) \cup V(z, w) \subseteq \mathbb{A}^4_k$ of two planes meeting at the origin, the function that is $1$ on one plane and $0$ on the other, away from the origin, does not extend. This $X$ is reduced, and it is not normal at the origin, where it fails $S_2$ (Example P1.11.8).

### Proof

*Proof of Proposition P3.7.32.* (1) The local rings of $\operatorname{Spec} A$ are the $A_\mathfrak{p}$, and Proposition P1.4.20 shows that $A$ is normal if and only if all of them are normal domains. The second statement holds because normality is a condition on local rings.

(2) A domain is reduced, so all local rings are reduced and $X$ is reduced (Definition P3.2.19). Let $X$ be locally Noetherian. Since $\mathcal{O}_{X, x}$ is a domain, it has one minimal prime, so $x$ lies on exactly one irreducible component, by the bijection of Proposition P3.7.2. So the components are pairwise disjoint. Every point has a Noetherian affine neighbourhood, which meets only finitely many components, so each component is the complement of a locally finite union of closed sets, hence open. Open, closed, connected and pairwise disjoint sets that cover $X$ are the connected components. A component $Z$ is an open subscheme that is reduced and irreducible, hence integral (Proposition P3.2.21), and its local rings are those of $X$.

(3) A regular local ring $R$ is a domain (Corollary P1.9.3), and its localizations are regular (Corollary P1.9.22), so $R$ is a regular domain. It is normal by Corollary P1.9.26.

(4) On an affine open $\operatorname{Spec} A$ with $A$ a Noetherian domain, $X$ satisfies $R_1$ and $S_2$ if and only if $A$ does (Definition P1.11.1), because both conditions are conditions on the $A_\mathfrak{p}$, and $\dim A_\mathfrak{p} = \operatorname{ht} \mathfrak{p}$. By Theorem P1.11.12, $A$ satisfies them if and only if $A$ is normal. Part 1 gives the statement for $X$.

(5) If $X$ is regular, it is normal by part 3. Let $X$ be normal. For a closed point $x$, $\mathcal{O}_{X, x}$ is a Noetherian normal local domain. Its dimension is $\operatorname{codim}(\{x\}, X)$, which is at most $\dim X = 1$ and is positive, as $x$ is not the generic point. So it is a Noetherian normal local domain of dimension $1$, hence a discrete valuation ring (Theorem P1.7.12), hence regular. By part 5 of Proposition P3.7.15, $X$ is regular. $\square$

*Proof of Theorem P3.7.33.* The restriction map is injective, as $X$ is integral (Proposition P3.2.24). Let $s \in \mathcal{O}_X(X \setminus Z)$, viewed as an element of the function field $K$. Let $U = \operatorname{Spec} A$ be a nonempty affine open of $X$. Then $A$ is a Noetherian normal domain with fraction field $K$, by part 1 of Proposition P3.7.32. Let $\mathfrak{p}$ be a prime of $A$ of height $1$. Then $\mathfrak{p} \notin Z$: otherwise the closure of $\mathfrak{p}$ in $X$, of codimension $1$ by Proposition P3.7.2, lies in a component $W$ of $Z$, and $\operatorname{codim}(W, X) \leq 1$. So $\mathfrak{p} \in U \setminus Z$, and the germ of $s$ at $\mathfrak{p}$ lies in $\mathcal{O}_{X, \mathfrak{p}} = A_\mathfrak{p}$. That is, $v_\mathfrak{p}(s) \geq 0$ for the discrete valuation of the discrete valuation ring $A_\mathfrak{p}$ (Corollary P1.7.13). By the algebraic Hartogs theorem (Corollary P1.8.3), $s \in A$. So $s$ extends to every affine open $U$, and the extensions agree on overlaps, since all of them are the element $s$ of $K$ and the restriction maps are injective. By the sheaf property they glue to an element of $\mathcal{O}_X(X)$ that restricts to $s$. $\square$

*Proof of Proposition P3.7.34.* By Proposition P3.3.30, for every affine open $V = \operatorname{Spec} A$ of $Y$, $f^{-1}(V) = \operatorname{Spec} B$ with $B$ finite over $A$.

(1) For $y = \mathfrak{p} \in V$, the fibre is $\operatorname{Spec} B \otimes_A \kappa(\mathfrak{p})$ (Proposition P3.3.28), and $C = B \otimes_A \kappa(\mathfrak{p})$ is a $\kappa(\mathfrak{p})$-algebra of finite dimension $r$. It is integral over a field, so it has dimension $0$ by Corollary P1.4.14, and every prime of $C$ is maximal. For distinct maximal ideals $\mathfrak{m}_1, \ldots, \mathfrak{m}_s$ the map $C \to \prod_i C/\mathfrak{m}_i$ is surjective by the Chinese remainder theorem, so $s \leq r$. So the fibre is a finite set of closed points, hence finite and discrete.

(2) This is part 2 of Proposition P3.4.19.

(3) Let $\mathfrak{a}$ be the kernel of $A \to B$. Then $B$ is integral over $A/\mathfrak{a} \subseteq B$, so $\dim B = \dim A/\mathfrak{a} \leq \dim A$ by Corollary P1.4.14 and Proposition P1.5.7. If $f$ is surjective, the image of $\operatorname{Spec} B \to \operatorname{Spec} A$ is all of $\operatorname{Spec} A$ and lies in $V(\mathfrak{a})$, so every prime contains $\mathfrak{a}$, and $\mathfrak{a}$ is contained in the nilradical (Theorem P1.1.9). Then $\dim A/\mathfrak{a} = \dim A$. As the $f^{-1}(V)$ cover $X$ and the $V$ cover $Y$, part 2 of Proposition P3.7.2 gives the statement.

(4) $B$ is integral over $A \subseteq B$, and by lying over (Theorem P1.4.12) every prime of $A$ is the contraction of a prime of $B$. $\square$

*Proof of Theorem P3.7.36.* (1) For an affine open $U = \operatorname{Spec} A$ and $g \in A$, the integral closure of $A_g$ in $K$ is $(\widetilde{A})_g$, by part 3 of Proposition P1.4.5 with $B = K$ and $S = \{g^m\}$. Define $\widetilde{\mathcal{O}}_U = (\widetilde{A})^\sim$, a quasi-coherent $\mathcal{O}_U$-algebra. For affine $U' \subseteq U$, cover $U'$ by open sets basic in both $U$ and $U'$ (Lemma P3.2.22); on each such $D(g) = D(g')$ both sheaves have sections $\widetilde{A}_g = \widetilde{A'}_{g'}$, the integral closure of $A_g = A'_{g'}$ in $K$, as subrings of $K$. These identifications agree on overlaps, as all are equalities of subrings of $K$, so the sheaves $\widetilde{\mathcal{O}}_U$ glue (Theorem P2.5.35) to a quasi-coherent $\mathcal{O}_X$-algebra with the stated sections.

(2) By Theorem P3.5.35, $\nu^{-1}(U) = \operatorname{Spec} \widetilde{A}$ for every affine open $U = \operatorname{Spec} A$, so $\nu$ is affine, and integral, as $\widetilde{A}$ is integral over $A$. The ring $\widetilde{A}$ is a normal domain with fraction field $K$, and for $U' \subseteq U$ the open sets $\operatorname{Spec} \widetilde{A'} \subseteq \operatorname{Spec} \widetilde{A}$ share the generic point $(0)$. So $\widetilde{X}$ is integral with function field $K$, and normal by part 1 of Proposition P3.7.32. The map $A \to \widetilde{A}$ is injective, so $\nu$ maps the generic point to the generic point and is dominant. If $A$ is normal, $\widetilde{A} = A$, which gives the statement on the normal locus, as the open sets on which $X$ is normal are covered by such $U$.

For the universal property, let $f \colon Y \to X$ be dominant with $Y$ normal and integral. Then $f$ maps the generic point of $Y$ to that of $X$, and it induces an injective map of fields $f^\# \colon K \to K(Y)$. For an affine open $U = \operatorname{Spec} A$ of $X$ and an affine open $V = \operatorname{Spec} C \subseteq f^{-1}(U)$, the map $A \to C$ is the restriction of $f^\#$ to $A \subseteq K$, followed by $C \subseteq K(Y)$. If $a \in \widetilde{A}$ satisfies a monic equation over $A$, then $f^\#(a)$ satisfies the image equation over $C$, so $f^\#(a) \in C$, as $C$ is normal. So $f^\#$ maps $\widetilde{A}$ into $C$, for every such $V$. As $\mathcal{O}_Y(f^{-1}(U))$ is the intersection of these $C$ inside $K(Y)$, by the sheaf property and the injectivity of restriction maps, $f^\#$ maps $\widetilde{A}$ into $\mathcal{O}_Y(f^{-1}(U))$. By Theorem P3.1.22 this ring map is a morphism $g_U \colon f^{-1}(U) \to \operatorname{Spec} \widetilde{A} = \nu^{-1}(U)$ with $\nu \circ g_U = f$ on $f^{-1}(U)$. The $g_U$ agree on overlaps, since all are given by $f^\#$, and they glue (Proposition P3.2.4). For uniqueness, let $g$ be any factorization. Over $U$, it is given by a ring map $\varphi \colon \widetilde{A} \to \mathcal{O}_Y(f^{-1}(U))$ that extends $A \to \mathcal{O}_Y(f^{-1}(U))$. For $a/s \in \widetilde{A}$ with $a, s \in A$, $s \neq 0$, $\varphi(s) \varphi(a/s) = \varphi(a)$, and $\varphi(s) \neq 0$ in the domain $\mathcal{O}_Y(f^{-1}(U))$. So $\varphi(a/s) = f^\#(a)/f^\#(s)$ is determined, and $g = g_U$ over $U$.

(3) Let $X$ be of finite type over $k$. For an affine open $U = \operatorname{Spec} A$, $A$ is a finitely generated $k$-algebra and a domain, so $\widetilde{A}$ is a finite $A$-module and a finitely generated $k$-algebra by Theorem P1.4.32. So $\nu$ is finite, by Proposition P3.3.30, and $\widetilde{X}$ is of finite type over $k$, as $X$ is quasi-compact. It is surjective by part 4 of Proposition P3.7.34, and $\dim \widetilde{X} = \dim X$ by part 3. $\square$

### Exercises

1. (A) Find the normalization of the curve $y^2 = x^5$ and of the curve $y^3 = x^4$ over a field $k$, and describe the fibre over the origin.
2. (A) Show that $\mathbb{Z}[\omega]$ with $\omega = (1 + \sqrt{-3})/2$ is the normalization of $\mathbb{Z}[\sqrt{-3}]$ of Example P3.7.20, and that $\operatorname{Spec} \mathbb{Z}[\omega] \to \operatorname{Spec} \mathbb{Z}[\sqrt{-3}]$ is a bijection that is not an isomorphism.
3. (A) Show that the normalization of the union $X = V(xy) \subseteq \mathbb{A}^2_k$ of the two axes, defined componentwise, is the disjoint union of two lines, and explain why Definition P3.7.35 does not apply to $X$.
4. (B) Let $X$ be a normal integral Noetherian scheme and $f$ a rational function, an element of $K(X)$. Show that the set of points where $f$ is not regular, the complement of the largest open set on which $f$ is a section of $\mathcal{O}_X$, is empty or of pure codimension $1$.
5. (B) Let $X$ be an integral scheme of finite type over $k$ and $L$ a finite extension of $K(X)$. Construct the normalization of $X$ in $L$, a finite morphism $\widetilde{X}^L \to X$ from a normal integral scheme with function field $L$, and state its universal property. Compute it for $X = \mathbb{A}^1_k = \operatorname{Spec} k[x]$ and $L = k(x)(\sqrt{x})$, with $\operatorname{char} k \neq 2$.
6. (B) Let $X$ be a normal variety and $\nu \colon \widetilde{Y} \to Y$ the normalization of a variety $Y$. Show that a finite birational morphism $f \colon X \to Y$ is the normalization. Deduce Zariski's main theorem in the weak form: a finite birational morphism onto a normal variety is an isomorphism.
7. (C) Let $X$ be a normal integral Noetherian scheme and $\mathcal{L}$ an invertible sheaf. Show that $\Gamma(X, \mathcal{L}) \to \Gamma(X \setminus Z, \mathcal{L})$ is an isomorphism for every closed $Z$ of codimension at least $2$. Deduce that the punctured cone $X \setminus \{0\}$, for $X = V(xy - z^2)$, has the same global functions as $X$, and that $X \setminus \{0\}$ is not affine.

### Lean

Mathlib constructs the relative normalization of a quasi-compact and quasi-separated morphism $f \colon X \to Y$ in `Mathlib/AlgebraicGeometry/Normalization.lean`: `AlgebraicGeometry.Scheme.Hom.normalization` is glued from the spectra of the integral closures of $\mathcal{O}_Y(U)$ in $\mathcal{O}_X(f^{-1}(U))$, and `normalizationDesc` gives the factorization through integral morphisms. Normal schemes, the Hartogs property and Serre's criterion for schemes are not in Lean as stated. Finite morphisms are `AlgebraicGeometry.IsFinite`, and the instance that they are proper is in `Mathlib/AlgebraicGeometry/Morphisms/Proper.lean`. The handbook adds no `MinimalModel` node here.

### Notes and history

Normal varieties go back to Zariski, who proved that the normalization of a projective variety is projective and that normal surfaces have isolated singularities, which is part 4 of Proposition P3.7.32 in dimension two. Grothendieck treats the normalization of a scheme, and the normalization in a finite extension of the function field, in EGA II. Hartshorne gives the construction as Exercise II.3.8. The finiteness in part 3 of Theorem P3.7.36 fails for general Noetherian integral schemes, by Nagata's examples, and holds for excellent schemes. The literature state is theorem. In the minimal model program normality is the standing hypothesis: Weil divisors, the canonical divisor $K_X$ and the discrepancies of Volume 4 are defined on normal varieties, and the Hartogs property is the reason why a small modification, an isomorphism in codimension one such as a flip, does not change the space of sections of a divisor.
