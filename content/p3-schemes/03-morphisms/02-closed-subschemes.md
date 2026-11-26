---
title: Closed immersions and closed subschemes
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch8, Har77:II.3, GW20:ch3]
requires: [P1.2, P3.1, P3.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Closed immersions and closed subschemes

### Statement

**Definition P3.3.9 (closed immersion, closed subscheme, immersion).** A morphism $i \colon Z \to X$ of schemes is a *closed immersion* if its map of spaces is a homeomorphism onto a closed subset of $X$ and $i^\# \colon \mathcal{O}_X \to i_* \mathcal{O}_Z$ is surjective. A *closed subscheme* of $X$ is a closed immersion into $X$, up to isomorphism over $X$. For closed subschemes $Z, Z'$, write $Z \subseteq Z'$ if $Z \to X$ factors through $Z' \to X$. A morphism is an *immersion* if it is a closed immersion followed by an open immersion, and a *locally closed subscheme* is an immersion up to isomorphism.

Lean: Mathlib `AlgebraicGeometry.IsClosedImmersion` and `AlgebraicGeometry.IsImmersion`.

**Theorem P3.3.10 (closed subschemes of an affine scheme).** Let $A$ be a ring and $i \colon Z \to \operatorname{Spec} A$ a closed immersion. Then $Z$ is affine, the map $A \to \Gamma(Z, \mathcal{O}_Z)$ is surjective, and with $I$ its kernel, $Z \cong \operatorname{Spec} A/I$ over $\operatorname{Spec} A$. So $I \mapsto \operatorname{Spec} A/I$ is a bijection from the ideals of $A$ to the closed subschemes of $\operatorname{Spec} A$, and it reverses inclusions.

Lean: Mathlib `AlgebraicGeometry.IsClosedImmersion.Spec_iff` and `AlgebraicGeometry.IsClosedImmersion.isAffine_surjective_of_isAffine` (proved in Mathlib).

**Proposition P3.3.11 (closed immersions are local).** Let $i \colon Z \to X$ be a morphism.

1. If $X = \bigcup_j V_j$ is an open cover and every $i^{-1}(V_j) \to V_j$ is a closed immersion, then $i$ is a closed immersion.
2. If $i$ is a closed immersion, then for every affine open $V \subseteq X$ the preimage $i^{-1}(V)$ is affine, and $i^{-1}(V) \cong \operatorname{Spec} \mathcal{O}_X(V)/I_V$ for a unique ideal $I_V$.
3. A composite of closed immersions is a closed immersion.
4. A closed immersion $i$ is a monomorphism: if $g, h \colon T \to Z$ satisfy $i g = i h$, then $g = h$. So an isomorphism between two closed subschemes over $X$ is unique if it exists.

Lean: Mathlib proves these as instances and lemmas for `AlgebraicGeometry.IsClosedImmersion`; part 2 is `AlgebraicGeometry.isClosedImmersion_iff_isAffineHom` together with the affine case (proved in Mathlib).

**Proposition P3.3.12 (reduced induced structure).** Let $X$ be a scheme and $Z \subseteq X$ a closed subset. There is exactly one reduced closed subscheme of $X$ with support $Z$. Over an affine open $U = \operatorname{Spec} A$ it is $\operatorname{Spec} A/I_U$, where $I_U = \bigcap_{\mathfrak{p} \in Z \cap U} \mathfrak{p}$ is the ideal of functions that vanish at every point of $Z \cap U$. For $Z = X$ it is the reduction $X_{\mathrm{red}}$, glued from the schemes $\operatorname{Spec} A/\operatorname{nil}(A)$.

Lean: Mathlib `AlgebraicGeometry.Scheme.IdealSheafData.vanishingIdeal` with `AlgebraicGeometry.Scheme.IdealSheafData.subscheme` (definitions in Mathlib); the uniqueness is not in Lean as stated.

### Proof in words

A closed immersion into $\operatorname{Spec} A$ is cut by the affineness criterion into affine pieces, so its source is affine. Its ring of global sections is then a quotient of $A$, because surjectivity of a map of $A$-modules can be checked after localizing at each prime, and the stalks of the sheaf map are these localizations. So a closed subscheme of an affine scheme is given by an ideal.

On a general scheme, a closed subscheme is a compatible family of ideals, one for each affine open set. Chapter 5 says this with quasi-coherent ideal sheaves. Here the reduced induced structure is the one case built by hand: the ideal of functions that vanish on $Z$ is radical, and it is compatible with localization, so the affine pieces glue.

### Examples

**Example P3.3.13 (closed points).** Let $x$ be a closed point of a scheme $X$. The reduced induced structure on $\{x\}$ is $\operatorname{Spec} \kappa(x) \to X$: on an affine open $\operatorname{Spec} A$ that contains $x = \mathfrak{m}$, it is $\operatorname{Spec} A/\mathfrak{m}$. If $x$ is not closed, the morphism $\operatorname{Spec} \kappa(x) \to X$ is not a closed immersion, since its image is not closed. For the generic point of $\mathbb{A}^1_k$ the morphism $\operatorname{Spec} k(t) \to \mathbb{A}^1_k$ is injective and is not an immersion of any kind: its image is not locally closed, since every nonempty open subset of $\mathbb{A}^1_k$ is infinite.

**Example P3.3.14 (fat points of the plane).** The ideals $(x, y)$, $(x, y^2)$, $(x^2, y)$ and $(x, y)^2$ of $k[x, y]$ have radical $(x, y)$. By Theorem P3.3.10 they define four closed subschemes with support the origin. Their rings have dimension $1$, $2$, $2$ and $3$ over $k$. The subscheme $V(x, y^2) = \operatorname{Spec} k[y]/(y^2)$ is the origin with a tangent vector along the $y$-axis, and it lies in the $y$-axis $V(x)$ and in the parabola $V(x - y^2)$, but not in the $x$-axis. The subscheme $V((x, y)^2)$ is the first order neighbourhood of the origin, and it contains every subscheme of length $2$ supported at the origin. The Hilbert scheme of $2$ points of the plane, in P8 Ch. 1, parametrizes the subschemes of length $2$, and its points over the origin are the tangent directions.

**Example P3.3.15 (a homeomorphism that is not a closed immersion).** Let $k$ be algebraically closed and $\nu \colon \mathbb{A}^1_k \to C = \operatorname{Spec} k[t^2, t^3]$ the normalization of the cusp of Example P3.1.38. Then $\nu$ is a homeomorphism onto the closed set $C$, but the ring map $k[t^2, t^3] \to k[t]$ is not surjective, so $\nu$ is not a closed immersion by Theorem P3.3.10. The composite $\mathbb{A}^1_k \to C \to \mathbb{A}^2_k$ is a homeomorphism onto the closed set $C$, and it is not a closed immersion either. So the condition on sheaves is not implied by the condition on spaces.

**Example P3.3.16 (the reduction).** For $X = \operatorname{Spec} k[x, y]/(y^2)$, the double line, $X_{\mathrm{red}}$ is the line $\operatorname{Spec} k[x]$. For a scheme $X$ the closed immersion $X_{\mathrm{red}} \to X$ is a homeomorphism, and it is an isomorphism exactly when $X$ is reduced. Every morphism from a reduced scheme to $X$ factors uniquely through $X_{\mathrm{red}}$ (Exercise 6).

**Example P3.3.17 (two points as a closed subscheme).** The closed subscheme $V(x(x - 1)) \subseteq \mathbb{A}^1_k$ is $\operatorname{Spec} k[x]/(x(x-1)) \cong \operatorname{Spec} k \sqcup \operatorname{Spec} k$, by the Chinese remainder theorem. The closed subscheme $V(x^2 - t)$ of $\mathbb{A}^1_{k(t)} = \operatorname{Spec} k(t)[x]$ is one point with residue field $k(\sqrt{t})$, while $V(x^2)$ of $\mathbb{A}^1_k$ is one point with a nilpotent. Section 3.4 puts these schemes in one family over the $t$-line.

### Proof

*Proof of Theorem P3.3.10.* Write $X = \operatorname{Spec} A$ and $B = \Gamma(Z, \mathcal{O}_Z)$, and let $\varphi \colon A \to B$ be the map $i^\#$ on global sections.

$Z$ is affine. Let $x \in X$. If $x \notin i(Z)$, there is $f \in A$ with $x \in D(f)$ and $D(f) \cap i(Z) = \emptyset$, since $i(Z)$ is closed; then $i^{-1}(D(f)) = \emptyset$. If $x = i(z)$, let $V$ be an affine open neighbourhood of $z$. Since $i$ is a homeomorphism onto $i(Z)$, $i(V) = i(Z) \cap W$ for an open $W \subseteq X$. Choose $f \in A$ with $x \in D(f) \subseteq W$. Then $i^{-1}(D(f)) = V \cap i^{-1}(D(f))$, which is the set of points of $V$ where $\varphi(f)|_V$ does not vanish, a basic open subset of $V$ and so affine. In both cases $i^{-1}(D(f)) = Z_{\varphi(f)}$ is affine. Finitely many such $D(f_1), \dots, D(f_r)$ cover $X$, since $X$ is quasi-compact, and then $(f_1, \dots, f_r) = A$. The elements $\varphi(f_k)$ generate the unit ideal of $B$, and every $Z_{\varphi(f_k)}$ is affine. By Theorem P3.3.4, $Z$ is affine, so $Z = \operatorname{Spec} B$ and $i = \operatorname{Spec} \varphi$ by Corollary P3.1.23.

$\varphi$ is surjective. For $f \in A$, $i^{-1}(D(f)) = D(\varphi(f))$, so $(i_* \mathcal{O}_Z)(D(f)) = B_{\varphi(f)} = B_f$, the localization of the $A$-module $B$. The stalk of $i_* \mathcal{O}_Z$ at $\mathfrak{p}$ is the colimit of $B_f$ over $f \notin \mathfrak{p}$, which is the localization $B_\mathfrak{p}$ of the $A$-module $B$, and the stalk of $i^\#$ is $\varphi_\mathfrak{p} \colon A_\mathfrak{p} \to B_\mathfrak{p}$. By hypothesis it is surjective for every $\mathfrak{p}$. Let $C$ be the cokernel of $\varphi$ as a map of $A$-modules. Localization is exact (P1 Ch. 2), so $C_\mathfrak{p} = 0$ for every prime $\mathfrak{p}$, and $C = 0$ since a module with all localizations zero is zero (P1 Ch. 2). So $\varphi$ is surjective, and with $I = \ker \varphi$, $B \cong A/I$ compatibly with the maps from $A$.

The bijection. By Proposition P3.1.32 every $\operatorname{Spec} A/I \to \operatorname{Spec} A$ is a closed immersion, and different ideals give different closed subschemes. The proof above shows that every closed subscheme is of this form. If $I \subseteq J$, then $A \to A/J$ factors through $A/I$, so $V(J) \subseteq V(I)$. Conversely, if $\operatorname{Spec} A/J \to \operatorname{Spec} A$ factors through $\operatorname{Spec} A/I$, then by Corollary P3.1.23 the map $A \to A/J$ factors through $A/I$, so $I \subseteq J$. $\square$

*Proof of Proposition P3.3.11.* Part 1. Each condition is local on $X$. The image $i(Z)$ is closed if $i(Z) \cap V_j$ is closed in $V_j$ for every $j$. The map $i$ is injective and closed onto its image if each restriction is, since a set $F \subseteq Z$ is closed if every $F \cap i^{-1}(V_j)$ is closed. Surjectivity of a map of sheaves is a condition on stalks (P2 Ch. 5), and the stalks of $i_* \mathcal{O}_Z$ at points of $V_j$ are those of $(i|_{i^{-1}V_j})_* \mathcal{O}$.

Part 2. The restriction $i^{-1}(V) \to V$ is a closed immersion, since the conditions restrict to open subsets of $X$. Theorem P3.3.10 applies.

Part 3. Let $j \colon W \to Z$ and $i \colon Z \to X$ be closed immersions. Then $i j$ is a homeomorphism onto the closed set $i(j(W))$. The map $\mathcal{O}_X \to (ij)_* \mathcal{O}_W$ is the composite of $\mathcal{O}_X \to i_* \mathcal{O}_Z$ and $i_*(j^\#) \colon i_* \mathcal{O}_Z \to i_* j_* \mathcal{O}_W$. The first is surjective. For the second, the stalk of $i_* \mathcal{F}$ at $i(z)$ is $\mathcal{F}_z$, since $i$ is a homeomorphism onto a closed set, and it is $0$ at points outside $i(Z)$. So $i_*$ preserves surjections of sheaves, and the composite is surjective.

Part 4. Let $i g = i h$. On spaces $g = h$, since $i$ is injective. The question on sheaves is local, so by part 2 it suffices to treat $X = \operatorname{Spec} A$ and $Z = \operatorname{Spec} A/I$, and then by covering $T$ with affine open sets, $T = \operatorname{Spec} R$. Then $g$ and $h$ are ring maps $A/I \to R$ whose composites with $A \to A/I$ agree, so they agree since $A \to A/I$ is surjective. $\square$

*Proof of Proposition P3.3.12.* The affine case. Let $U = \operatorname{Spec} A$ and $Z \cap U = V(J)$. By Theorem P1.1.9, $I_U = \sqrt{J}$, so $V(I_U) = Z \cap U$ and $A/I_U$ is reduced, since $I_U$ is radical. A reduced closed subscheme $\operatorname{Spec} A/I$ with support $Z \cap U$ has $I$ radical and $V(I) = V(J)$, so $I = \sqrt{J} = I_U$ by Theorem P1.1.9. This proves existence and uniqueness on $U$.

Compatibility. For $f \in A$, the open set $D(f) = \operatorname{Spec} A_f$ meets $Z$ in $V(J A_f)$, and $I_{D(f)} = \sqrt{J A_f} = (\sqrt{J})_f = (I_U)_f$: if $(a/f^m)^n \in J A_f$, then $f^p a^n \in J$ for some $p$, so $(fa)^{n + p} \in J$ and $a/f^m = fa/f^{m+1} \in (\sqrt J)_f$; the other inclusion is clear. So the closed subscheme $Z_U = \operatorname{Spec} A/I_U$ restricts on $D(f)$ to $Z_{D(f)}$, since $A_f/(I_U)_f = (A/I_U)_f$.

Gluing. Let $U, U'$ be affine open sets. The open set $U \cap U'$ is covered by sets $W$ that are basic in both (Lemma P3.2.22, step 1). On each $W$, the restrictions of $Z_U$ and $Z_{U'}$ are both $Z_W$, so there is an isomorphism over $W$, unique by part 4 of Proposition P3.3.11. These isomorphisms agree on overlaps by the same uniqueness, so they glue to an isomorphism between the restrictions of $Z_U$ and $Z_{U'}$ to $U \cap U'$. The cocycle condition on triple overlaps holds by uniqueness. By Theorem P3.2.3 the $Z_U$ glue to a scheme $Z_{\mathrm{red}}$ with a morphism to $X$, by Proposition P3.2.4, which is a closed immersion by part 1 of Proposition P3.3.11. It is reduced since each $A/I_U$ is reduced, and it is unique since a reduced closed subscheme with support $Z$ restricts on each $U$ to the unique one there. For $Z = X$, $I_U = \operatorname{nil}(A)$ by Theorem P1.1.9. $\square$

### Exercises

1. (A) Show that $V(F) \to \mathbb{P}^n_A$ of Example P3.2.16 is a closed immersion, using part 1 of Proposition P3.3.11.
2. (A) Show that an open immersion that is also a closed immersion is an isomorphism onto a union of connected components of the target. Give an example where the target is not connected.
3. (A) List the closed subschemes of $\operatorname{Spec} k[x]/(x^3)$ and the inclusions between them.
4. (B) Let $X$ be a scheme and $i \colon Z \to X$ a closed immersion. Show that $Z$ is reduced if and only if, for every affine open $\operatorname{Spec} A$, the ideal $I_{\operatorname{Spec} A}$ of part 2 of Proposition P3.3.11 is radical.
5. (B) Let $Z_1 = V(I)$ and $Z_2 = V(J)$ be closed subschemes of $\operatorname{Spec} A$. Show that $V(I + J)$ is the largest closed subscheme contained in both, and that $V(I \cap J)$ is the smallest closed subscheme that contains both. Compute both for $I = (y)$ and $J = (y - x^2)$ in $k[x, y]$.
6. (B) Let $X$ be a scheme and $T$ a reduced scheme. Show that every morphism $T \to X$ factors uniquely through $X_{\mathrm{red}} \to X$. More generally, if the image of $T \to X$ lies in a closed set $Z$, show that the morphism factors uniquely through the reduced induced structure on $Z$.
7. (C) Show that a morphism $i \colon Z \to X$ is an immersion if and only if it is a homeomorphism onto a locally closed subset and the stalk maps $\mathcal{O}_{X, i(z)} \to \mathcal{O}_{Z, z}$ are surjective. (For the converse, find an open $U \subseteq X$ in which $i(Z)$ is closed, and use part 1 of Proposition P3.3.11.)

### Lean

Mathlib has the classes `AlgebraicGeometry.IsClosedImmersion` and `AlgebraicGeometry.IsImmersion`. The description of closed immersions into an affine scheme is `AlgebraicGeometry.IsClosedImmersion.Spec_iff`, with `AlgebraicGeometry.IsClosedImmersion.isAffine_surjective_of_isAffine` for the affineness of the source and the surjectivity on global sections. Closed subschemes are treated through ideal sheaves, `AlgebraicGeometry.Scheme.IdealSheafData`, with the subscheme `AlgebraicGeometry.Scheme.IdealSheafData.subscheme` and the vanishing ideal of a closed set `AlgebraicGeometry.Scheme.IdealSheafData.vanishingIdeal`. The handbook adds no `MinimalModel` node here.

### Notes and history

Closed subschemes and the reduced induced structure are in EGA I, Chapter I. Hartshorne defines closed immersions in Section II.3 and proves Theorem P3.3.10 in Section II.5 with quasi-coherent sheaves; the proof here uses the affineness criterion instead and follows the Stacks project and Vakil. The literature state is theorem. The program uses non-reduced closed subschemes in several places: the scheme-theoretic fibres of contractions, the divisors $mD$, and the subschemes of length $2$ behind the Hilbert schemes of points.
