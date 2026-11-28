---
title: Normalization and the resolution of curves
nodes: []
sources: [Kol07, Har77, Cut04, Stacks]
reads_with: [Kol07:1.1, Har77:I.6, Cut04:2]
requires: [P1.7, P3.7, P4.6, P5.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Normalization and the resolution of curves

### Statement

In this chapter $k$ is a field, and a *curve* over $k$ is a separated scheme of finite type over $k$ of pure dimension $1$. Unless the text says otherwise $k$ is algebraically closed, but the first theorem needs only a perfect field.

**Definition P8.4.1 (resolution).** Let $X$ be a reduced separated scheme of finite type over $k$. A *resolution* of $X$ is a proper morphism $f \colon Y \to X$ with $Y$ smooth over $k$ for which there is a dense open set $V \subseteq X$ such that $f^{-1}(V)$ is dense in $Y$ and $f^{-1}(V) \to V$ is an isomorphism. So a resolution is a proper birational morphism from a smooth scheme. The *exceptional set* $\operatorname{Exc}(f)$ is the set of points $y \in Y$ such that no open neighbourhood of $y$ is mapped by $f$ isomorphically onto an open subset of $X$. The morphism $f$ is an *isomorphism over* an open set $U \subseteq X$ if $f^{-1}(U) \to U$ is an isomorphism.

If $X$ is integral, so is every resolution: $f^{-1}(V) \cong V$ is irreducible and dense, so $Y$ is irreducible, and $Y$ is reduced because it is smooth.

**Theorem P8.4.2 (normalization resolves curves).** Let $k$ be a perfect field, $X$ an integral curve over $k$, and $\nu \colon \widetilde{X} \to X$ its normalization.

1. The morphism $\nu$ is finite, surjective and birational, and $\widetilde{X}$ is a smooth curve. So $\nu$ is a resolution of $X$, and it is an isomorphism over the normal locus of $X$.
2. Let $f \colon Y \to X$ be a proper birational morphism with $Y$ a normal integral scheme. Then $f = \nu \circ g$ for a unique morphism $g \colon Y \to \widetilde X$, and $g$ is an isomorphism. In particular every resolution of $X$ is isomorphic over $X$ to $\nu$, by a unique isomorphism.
3. The normal locus of $X$ is the smooth locus of $X$, and its complement is a finite set of closed points.

Lean: not in Lean as stated.

**Corollary P8.4.3 (reduced curves).** Let $k$ be perfect and $X$ a reduced curve over $k$ with irreducible components $X_1, \dots, X_r$, each with its reduced structure. Then the morphism $\bigsqcup_i \widetilde{X}_i \to X$ induced by the normalizations $\widetilde X_i \to X_i$ is a finite resolution of $X$, and every resolution of $X$ is isomorphic to it over $X$, by a unique isomorphism.

Lean: not in Lean as stated.

### Proof in words

A local ring of the normalization at a closed point is a normal Noetherian local domain of dimension one, which is a discrete valuation ring, and over a perfect field a regular point is a smooth point. This gives existence. Uniqueness comes from the universal property of the normalization: a resolution factors through it, and the factor is proper with finite fibres, hence finite, and a finite birational morphism onto a normal curve is an isomorphism. In dimension one there is no room for exceptional curves, and that is why the resolution is unique; from dimension two on, blowing up a point of a resolution gives another one.

### Examples

**Example P8.4.4 (the node).** Let $\operatorname{char} k \neq 2$ and $X = V(y^2 - x^2(x + 1)) \subseteq \mathbb{A}^2$. As in Example P3.7.38 and Example P5.3.6, $t = y / x$ satisfies $t^2 = x + 1$, the normalization is $\mathbb{A}^1 \to X$, $t \mapsto (t^2 - 1, t(t^2 - 1))$, and the two points $t = \pm 1$ map to the origin. By Theorem P8.4.2 this is the only resolution. It is not an isomorphism over the origin, though the node is analytically the union of two smooth branches (Example P1.6.30): the branches are separated, not smoothed.

**Example P8.4.5 (the cusp and the curves $y^a = x^b$).** Let $a, b \geq 2$ be coprime and $X = V(y^a - x^b) \subseteq \mathbb{A}^2$. By Example P5.3.7 the normalization is $\mathbb{A}^1 \to X$, $t \mapsto (t^a, t^b)$. It is bijective, and it is a homeomorphism, but it is not an isomorphism, because $k[t^a, t^b] \neq k[t]$. For the cusp, $a = 2$ and $b = 3$, and the resolution of the curve is reached in one step. The resolution of the pair formed by the plane and the cusp needs three blow-ups, and is computed in Section 4.2.

**Example P8.4.6 (the three coordinate axes).** Let $X \subseteq \mathbb{A}^3$ be the union of the three coordinate axes, as in Example P5.3.9. Its components are three lines, and by Corollary P8.4.3 its resolution is the disjoint union of three copies of $\mathbb{A}^1$, mapping to the axes. The tangent space of $X$ at the origin has dimension $3$, so $X$ does not lie on any smooth surface near the origin, and the resolution of curves on a smooth surface of Section 6.2 of Volume P5 does not apply to it. Theorem P8.4.2 needs no ambient surface.

**Example P8.4.7 (a regular curve with no resolution).** Let $p > 2$, $k = \mathbb{F}_p(t)$, and $X = V(y^2 - x^p + t) \subseteq \mathbb{A}^2_k$, as in Example P3.7.29. The curve $X$ is regular, hence normal, so $\nu$ is the identity, but $X$ is not smooth at the point $P = (y, x^p - t)$. If $f \colon Y \to X$ were a resolution, part 2 of Theorem P8.4.2, whose proof does not use that $k$ is perfect, would make $f$ an isomorphism, and $X$ would be smooth. So $X$ has no resolution in the sense of Definition P8.4.1. Over an imperfect field the right notion asks for $Y$ regular, and then the normalization is again the unique resolution of a curve.

### Proof

*Theorem P8.4.2.* (1) By Theorem P3.7.36, part 3, $\nu$ is finite and surjective, $\widetilde X$ is of finite type over $k$ and $\dim \widetilde X = 1$. By part 2 of the same theorem, $\widetilde X$ is a normal integral scheme, $\nu$ induces an isomorphism of function fields, and $\nu$ is an isomorphism over every open set on which $X$ is normal. The cokernel of $\mathcal{O}_X \to \nu_* \mathcal{O}_{\widetilde X}$ is coherent and vanishes at the generic point, so its support is a closed set not containing the generic point, and $\nu$ is an isomorphism over its complement, which is dense. A finite morphism is proper, so $\nu$ is proper and birational. Let $\tilde x \in \widetilde X$ be a closed point. The local ring $\mathcal{O}_{\widetilde X, \tilde x}$ is a Noetherian local domain of dimension $1$, because $\widetilde X$ is an integral scheme of finite type over $k$ of dimension $1$, and it is normal. By Theorem P1.7.12 it is a discrete valuation ring, so it is regular. The residue field $\kappa(\tilde x)$ is a finite extension of $k$, and it is separable because $k$ is perfect. By the Jacobian criterion, Theorem P3.7.24, $\widetilde X$ is smooth at $\tilde x$. The smooth locus is open and contains every closed point, so it is all of $\widetilde X$.

(2) The scheme $Y$ is integral and normal, and $f$ is dominant, because its image contains the dense open set $V$ of Definition P8.4.1. By Definition P3.7.35, $f = \nu \circ g$ for a unique morphism $g \colon Y \to \widetilde X$. The morphism $g$ is proper, since $f$ is proper and $\nu$ is separated (Hartshorne, Corollary II.4.8). It is birational, because $f$ and $\nu$ are isomorphisms over dense open subsets of $X$, so $g$ is an isomorphism over the preimage in $\widetilde X$ of their intersection. Since $f^{-1}(V) \cong V$, $Y$ is an integral scheme of dimension $1$. A fibre of $g$ over a closed point is a closed subset of $Y$, and it is not all of $Y$ because $g$ is dominant, so it is finite. A proper morphism with finite fibres is finite (Grothendieck, EGA III, Proposition 4.4.2; for projective morphisms this is Corollary P4.6.17). So $g$ is finite, and $g_* \mathcal{O}_Y$ is a coherent sheaf of $\mathcal{O}_{\widetilde X}$-algebras. On an affine open $\operatorname{Spec} A \subseteq \widetilde X$, the ring $B = \Gamma(g^{-1} \operatorname{Spec} A, \mathcal{O}_Y)$ is a finite $A$-algebra contained in the common function field $K$, because $Y$ is integral and $g$ is birational. So $B$ is integral over $A$ and lies in $K$, and $B = A$ because $A$ is integrally closed. Since $g$ is affine, $g$ is an isomorphism. A resolution of $X$ is a proper birational morphism from a smooth, hence normal, integral scheme, so this applies to it, and the isomorphism is unique by the uniqueness in Definition P3.7.35.

(3) At a closed point $x \in X$, if $X$ is normal at $x$, then $\mathcal{O}_{X, x}$ is a discrete valuation ring by Theorem P1.7.12 and $X$ is smooth at $x$ by Theorem P3.7.24, as in part 1. Conversely a smooth point is regular, and a regular local ring is a normal domain. The normal locus is the complement of the support of the coherent sheaf $\nu_* \mathcal{O}_{\widetilde X} / \mathcal{O}_X$, which is closed and does not contain the generic point. A proper closed subset of an integral curve is a finite set of closed points.

*Corollary P8.4.3.* Each $X_i$ is an integral curve, so $\nu_i \colon \widetilde X_i \to X_i \to X$ is finite, and $\nu = \bigsqcup \nu_i$ is finite, hence proper. Let $V \subseteq X$ be the set of points that lie on exactly one component $X_i$ and at which $X_i$ is normal. Its complement is the union of the finite sets $X_i \cap X_j$, $i \neq j$, and of the non-normal points of the $X_i$, so $V$ is open and dense. Over $V$ the scheme $X$ equals the reduced scheme $X_i$ near each point, and $\nu$ is an isomorphism. So $\nu$ is a resolution, by Theorem P8.4.2 applied to each $X_i$. Let $f \colon Y \to X$ be a resolution. Since $Y$ is smooth, its local rings are domains, so its connected components $Y_1, \dots, Y_s$ are irreducible. The isomorphism $f^{-1}(V) \cong V$ with $f^{-1}(V)$ dense matches the components of $Y$ with those of $X$, so $s = r$ and, after renumbering, $f$ maps $Y_i$ into $X_i$. Since $Y_i$ is reduced, $f|_{Y_i}$ factors through the reduced closed subscheme $X_i$, and $Y_i \to X_i$ is a resolution, proper because $Y_i$ is closed in $Y$ and $X_i$ is closed in $X$. By Theorem P8.4.2 it is isomorphic to $\nu_i$ by a unique isomorphism, and these isomorphisms together give the isomorphism $Y \cong \bigsqcup \widetilde X_i$ over $X$.

### Exercises

1. (A) Let $\operatorname{char} k \neq 2$ and $X = V(y^2 - x^4 - x^5) \subseteq \mathbb{A}^2$. Show that $t = y / x^2$ satisfies $t^2 = 1 + x$, compute the normalization, and show that two points lie over the origin.
2. (A) Let $X \subseteq \mathbb{A}^3$ be the image of $t \mapsto (t^3, t^4, t^5)$. Show that $X$ is closed, that $\mathbb{A}^1 \to X$ is the normalization, and that $\dim_k k[t] / k[t^3, t^4, t^5] = 2$.
3. (A) Show that $V(y^2) \subseteq \mathbb{A}^2$ has no resolution in the sense of Definition P8.4.1, and that the resolution of its reduced curve is the identity.
4. (B) Let $X$ be a projective integral curve over an algebraically closed field. Show that $\chi(\mathcal{O}_{\widetilde X}) - \chi(\mathcal{O}_X) = \sum_{x} \dim_k (\nu_* \mathcal{O}_{\widetilde X} / \mathcal{O}_X)_x$, and compare with Proposition P5.3.2.
5. (B) Let $X$ be an integral curve over any field $k$. Show that the normalization $\widetilde X$ is regular, and that every proper birational morphism $Y \to X$ with $Y$ regular and integral is isomorphic to $\nu$ over $X$.
6. (C) In Example P8.4.7, let $k' = k(t^{1/p})$ and $s = t^{1/p}$. Show that $X \times_k k'$ is the reduced curve $y^2 = (x - s)^p$, that it is not normal at the point over $P$, and that its normalization is smooth over $k'$. Deduce that the projective closure of $X$, whose arithmetic genus does not change under the extension of the field, has a smooth model over $k'$ of smaller genus.

### Lean

The normalization of a curve and Theorem P8.4.2 are not in Lean. Section 5.2 explains why the definitions of the singularities of the program in the repository do not need resolutions.

### Notes and history

The normalization of a curve goes back to Dedekind and Weber's algebraic theory of function fields of one variable (1882), in which the points of the smooth projective model are the discrete valuations of the function field. Kollár, Chapter 1, gives several proofs of the resolution of curves, by normalization, by blowing up points and by the theory of valuations, and compares them. The failure of smoothness over imperfect fields, Example P8.4.7, is the first place where resolution in positive characteristic must speak of regular schemes rather than smooth ones; Lipman's theorem in Section 4.3 is stated in this form.
