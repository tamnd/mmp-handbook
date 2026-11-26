---
title: Properties of separated morphisms
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch11, Har77:II.4, GW20:ch9]
requires: [P3.2, P3.3, P3.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Properties of separated morphisms

### Statement

**Proposition P3.4.9 (stability of separated morphisms).** Let $f \colon X \to Y$ and $g \colon Y \to Z$ be morphisms of schemes.

1. A monomorphism is separated. In particular open immersions and closed immersions are separated.
2. If $f$ and $g$ are separated, then $g f$ is separated.
3. If $f$ is separated and $Y' \to Y$ is any morphism, then the base change $X \times_Y Y' \to Y'$ is separated.
4. If $g f$ is separated, then $f$ is separated.
5. If $X$ and $Y$ are separated over a scheme $S$, then $X \times_S Y$ is separated over $S$.

Lean: Mathlib `AlgebraicGeometry.isSeparated_of_mono`, the instances `IsStableUnderComposition @IsSeparated` and `IsStableUnderBaseChange @IsSeparated`, and `AlgebraicGeometry.IsSeparated.of_comp` (proved in Mathlib).

**Proposition P3.4.10 (equalizers and graphs).** Let $Y$ be separated over a scheme $S$, and let $f, g \colon X \to Y$ be morphisms over $S$.

1. There is a closed subscheme $E \subseteq X$ such that a morphism $h \colon T \to X$ factors through $E$ if and only if $f h = g h$. It is the fibre product of $(f, g) \colon X \to Y \times_S Y$ and the diagonal $\Delta_{Y/S}$.
2. The graph $\Gamma_f = (\mathrm{id}_X, f) \colon X \to X \times_S Y$ is a closed immersion.

Lean: Mathlib `AlgebraicGeometry.isClosedImmersion_equalizer_ι_left`, for the equalizer in the category of schemes over $S$ (proved in Mathlib); the graph statement is not in Lean as stated.

**Theorem P3.4.11 (reduced to separated).** Let $X$ be a reduced scheme and $Y$ a separated scheme over a scheme $S$. Let $f, g \colon X \to Y$ be morphisms over $S$, and let $U \subseteq X$ be a dense open subset with $f|_U = g|_U$. Then $f = g$.

Lean: Mathlib `AlgebraicGeometry.ext_of_isDominant_of_isSeparated'` (proved in Mathlib), stated for a dominant morphism into $X$ in place of a dense open subset.

**Proposition P3.4.12 (preimages of affine open sets).** Let $f \colon X \to Y$ be a morphism with $Y$ separated. For affine open sets $U \subseteq X$ and $V \subseteq Y$, the set $U \cap f^{-1}(V)$ is affine. In particular every morphism from an affine scheme to a separated scheme is affine, and the intersection of two affine open sets of a separated scheme is affine.

Lean: Mathlib proves that a morphism from an affine scheme to a separated scheme is affine through `AlgebraicGeometry.IsAffineHom.of_comp` (proved in Mathlib); the statement for $U \cap f^{-1}(V)$ is not in Lean as stated.

### Proof in words

Every statement comes from one fact: the diagonal behaves well under composition and base change. For $X \to Y \to Z$, the natural morphism $X \times_Y X \to X \times_Z X$ is a base change of the diagonal of $Y$ over $Z$. So closed immersions of diagonals pass along compositions and base changes.

The locus where two morphisms agree is the preimage of the diagonal, so it is closed when the target is separated. On a reduced scheme a closed subscheme that contains a dense open set is everything. So two morphisms from a reduced scheme to a separated scheme that agree on a dense open set agree everywhere. This rigidity fails without either hypothesis, and the examples show both failures.

### Examples

**Example P3.4.13 (failure for a non-separated target).** Let $Y$ be the affine line with a doubled origin, glued from $U = \operatorname{Spec} k[x]$ and $V = \operatorname{Spec} k[y]$. The two open immersions $\mathbb{A}^1_k \to U \subseteq Y$ and $\mathbb{A}^1_k \to V \subseteq Y$ agree on the dense open set $\mathbb{A}^1_k \setminus \{0\}$ and send $0$ to the two different origins. So Theorem P3.4.11 fails without the separatedness of $Y$.

**Example P3.4.14 (failure for a non-reduced source).** Let $X = \operatorname{Spec} k[x, y]/(y^2, xy)$, the line with an embedded point at the origin, and let $f, g \colon X \to \mathbb{A}^1_k = \operatorname{Spec} k[t]$ be given by $t \mapsto y$ and $t \mapsto 0$. The open set $D(x)$ is dense, since its complement is the single point at the origin and $X$ is irreducible with generic point $(y)$. On $D(x)$ the element $y$ is $0$, since $xy = 0$ and $x$ is a unit. So $f|_{D(x)} = g|_{D(x)}$, but $f \neq g$ since $y \neq 0$ in $k[x, y]/(y^2, xy)$. So Theorem P3.4.11 fails without the reducedness of $X$. For $X = \operatorname{Spec} k[x]/(x^2)$ the only dense open set is $X$, so this smaller example does not show the failure.

**Example P3.4.15 (quasi-projective schemes are separated).** Let $A$ be a ring and $X$ a locally closed subscheme of $\mathbb{P}^n_A$, that is, an immersion $X \to \mathbb{P}^n_A$. The immersion is a composite of a closed and an open immersion, both separated by part 1 of Proposition P3.4.9, and $\mathbb{P}^n_A$ is separated over $A$ by Example P3.4.6. So $X$ is separated over $A$, by part 2. In particular every affine, projective and quasi-projective variety is a variety in the sense of Definition P3.2.25.

**Example P3.4.16 (base change keeps non-separatedness).** Let $X$ be the affine line with a doubled origin over $k$, and $Y = X \times_k \mathbb{A}^1_k$. The projection $Y \to \mathbb{A}^1_k$ has fibres all equal to the doubled origin over the residue fields. The scheme $Y$ is the plane with a doubled line $\{0\} \times \mathbb{A}^1_k$, and it is not separated over $k$. Indeed, $X \cong Y \times_{\mathbb{A}^1_k} \operatorname{Spec} k$, the fibre over the origin, is a closed subscheme of $Y$ by part 2 of Proposition P3.3.20. If $Y$ were separated over $k$, the composite $X \to Y \to \operatorname{Spec} k$ of a closed immersion and a separated morphism would be separated by parts 1 and 2 of Proposition P3.4.9, which fails.

**Example P3.4.17 (the graph of the Frobenius).** Let $k$ be a field of characteristic $p$ and $F \colon \mathbb{A}^1_k \to \mathbb{A}^1_k$, $x \mapsto x^p$. Its graph is the closed subscheme $V(y - x^p) \subseteq \mathbb{A}^2_k$, a smooth curve isomorphic to $\mathbb{A}^1_k$ by the first projection. Part 2 of Proposition P3.4.10 says the same for every morphism to a separated scheme: the graph is a closed subscheme isomorphic to the source.

### Proof

The proof uses one lemma. Let $f \colon X \to Y$ and $g \colon Y \to Z$ be morphisms, and let $j \colon X \times_Y X \to X \times_Z X$ be the natural morphism. Then the square with $j$, the diagonal $\Delta_{Y/Z} \colon Y \to Y \times_Z Y$, the morphism $f \times f \colon X \times_Z X \to Y \times_Z Y$ and $f \circ p_1 \colon X \times_Y X \to Y$ is a fibre product square. Indeed, by Definition P3.3.18 the $T$-points of the fibre product of $f \times f$ and $\Delta_{Y/Z}$ are the triples $(a, b, y)$ with $a, b \colon T \to X$, $g f a = g f b$, $y \colon T \to Y$ and $(f a, f b) = (y, y)$. These are the pairs $(a, b)$ with $f a = f b$, which are the $T$-points of $X \times_Y X$. By the Yoneda lemma P2.1.23 the fibre product is $X \times_Y X$ with the morphism $j$. Also $\Delta_{X/Z} = j \circ \Delta_{X/Y}$, since both have components $(\mathrm{id}, \mathrm{id})$.

*Proof of Proposition P3.4.9.* Part 1. If $f$ is a monomorphism, the scheme $X$ with the projections $\mathrm{id}, \mathrm{id}$ is a fibre product $X \times_Y X$: for $a, b \colon T \to X$ with $f a = f b$, $a = b$, and $a$ is the unique morphism to $X$. So $\Delta$ is an isomorphism, and an isomorphism is a closed immersion. An open immersion is a monomorphism, since a morphism into an open subscheme is determined by the morphism into the whole scheme. A closed immersion is a monomorphism by part 4 of Proposition P3.3.11.

Part 2. In the lemma, $j$ is a base change of the closed immersion $\Delta_{Y/Z}$, so it is a closed immersion by part 2 of Proposition P3.3.20. Then $\Delta_{X/Z} = j \Delta_{X/Y}$ is a closed immersion by part 3 of Proposition P3.3.11.

Part 3. Let $X' = X \times_Y Y'$. The $T$-points of $X' \times_{Y'} X'$ are the pairs of $T$-points $(a, y')$ and $(b, y')$ of $X'$ with the same $Y'$-component, so they are the triples $(a, b, y')$ with $(a, b)$ a $T$-point of $X \times_Y X$ over the image of $y'$. A triple lies in the image of $\Delta_{X'/Y'}$ if and only if $a = b$, that is, if and only if $(a, b)$ factors through $\Delta_{X/Y}$. So $\Delta_{X'/Y'}$ is the base change of $\Delta_{X/Y}$ along the natural morphism $X' \times_{Y'} X' \to X \times_Y X$, and it is a closed immersion by part 2 of Proposition P3.3.20.

Part 4. By Proposition P3.4.2, $\Delta_{Y/Z}$ is an immersion, so its base change $j$ is an immersion, by part 2 of Proposition P3.3.20 for the closed part and Exercise 4 of Section 3.3 for the open part. So $j$ is injective. Then $\Delta_{X/Y}(X) = j^{-1}(\Delta_{X/Z}(X))$, which is closed since $\Delta_{X/Z}$ is a closed immersion. By part 2 of Proposition P3.4.2, $f$ is separated.

Part 5. The projection $X \times_S Y \to Y$ is a base change of $X \to S$, so it is separated by part 3, and its composite with $Y \to S$ is separated by part 2. $\square$

*Proof of Proposition P3.4.10.* Part 1. Let $E = X \times_{Y \times_S Y} Y$, the fibre product of $(f, g)$ and $\Delta_{Y/S}$. Then $E \to X$ is a base change of the closed immersion $\Delta_{Y/S}$, so it is a closed immersion by part 2 of Proposition P3.3.20. A $T$-point of $E$ is a pair $(h, y)$ with $(f h, g h) = (y, y)$, that is, a morphism $h \colon T \to X$ with $f h = g h$, and then $y = f h$ is determined. Since $E \to X$ is a monomorphism, $h$ factors through $E$ in at most one way.

Part 2. The square with $\Gamma_f$, $\Delta_{Y/S}$, the morphism $f \times \mathrm{id} \colon X \times_S Y \to Y \times_S Y$ and $f \colon X \to Y$ is a fibre product square. Its $T$-points are the triples $(a, b, y)$ with $a \colon T \to X$, $b \colon T \to Y$ over $S$ and $(f a, b) = (y, y)$, so they are determined by $a$. So $\Gamma_f$ is a base change of $\Delta_{Y/S}$, and it is a closed immersion by part 2 of Proposition P3.3.20. $\square$

*Proof of Theorem P3.4.11.* Let $i \colon E \to X$ be the closed subscheme of part 1 of Proposition P3.4.10. The inclusion $U \to X$ satisfies $f|_U = g|_U$, so it factors through $E$, and $i(E) \supseteq U$. Since $i(E)$ is closed and $U$ is dense, $i(E) = X$. Now let $\operatorname{Spec} A \subseteq X$ be an affine open set. By part 2 of Proposition P3.3.11, $E \cap \operatorname{Spec} A = \operatorname{Spec} A/I$ for an ideal $I$ with $V(I) = \operatorname{Spec} A$. Then $I \subseteq \operatorname{nil}(A)$ by Theorem P1.1.9, and $\operatorname{nil}(A) = 0$ since $X$ is reduced. So $I = 0$, and $i$ is an isomorphism over every affine open set, hence an isomorphism. The identity of $X$ factors through $E$, so $f = g$. $\square$

*Proof of Proposition P3.4.12.* Apply part 2 of Proposition P3.4.10 with $S = \operatorname{Spec} \mathbb{Z}$: the graph $\Gamma_f \colon X \to X \times_{\mathbb{Z}} Y$ is a closed immersion. The open set $U \times_{\mathbb{Z}} V = p_1^{-1}(U) \cap p_2^{-1}(V)$ is affine by Theorem P3.3.19 and part 1 of Proposition P3.3.20, and $\Gamma_f^{-1}(U \times_{\mathbb{Z}} V) = U \cap f^{-1}(V)$. The preimage of an affine open set under a closed immersion is affine by part 2 of Proposition P3.3.11. For the second claim take $U = X$; for the third take $f = \mathrm{id}_Y$. $\square$

### Exercises

1. (A) Show that an affine morphism is separated. (Use Proposition P3.4.2 and Exercise 3 of Section 4.1.)
2. (A) Let $X$ be an integral scheme and $Y$ a separated scheme, and let $f, g \colon X \to Y$ be morphisms that agree on a nonempty open set. Show that $f = g$.
3. (A) Show that the closed subscheme $E$ of Proposition P3.4.10 for $f, g \colon \mathbb{A}^1_k \to \mathbb{A}^1_k$, $f(x) = x^2$ and $g(x) = x$, is $V(x^2 - x)$, and compute it for $f(x) = x^3$, $g(x) = x$ over a field of characteristic $2$.
4. (B) Give an example of a separated scheme $X$ and two affine open sets $U, V$ such that $U \cup V$ is not affine, and an example of a non-separated scheme in which the intersection of two affine open sets is affine.
5. (B) Let $X$ be separated over $S$ and $\sigma \colon S \to X$ a section of the structure morphism $\pi$, that is, $\pi \sigma = \mathrm{id}_S$. Show that $\sigma$ is a closed immersion. (Apply part 2 of Proposition P3.4.10 to $\sigma$, or use part 4 of Proposition P3.4.9.)
6. (B) Let $X$ be a reduced scheme and $Y$ a separated scheme. A *rational map* $X \dashrightarrow Y$ is an equivalence class of morphisms $U \to Y$ from dense open sets, where two are equivalent if they agree on a dense open subset of the intersection. Show that a rational map has a largest open set on which it is defined by a morphism.
7. (C) Let $k$ be a field and $X$, $Y$ schemes of finite type over $k$, with $X$ reduced and $Y$ separated. Let $f, g \colon X \to Y$ be morphisms over $k$ such that $f \circ x = g \circ x$ for every closed point $x \colon \operatorname{Spec} \kappa(x) \to X$. Show that $f = g$. (Use Proposition P3.4.10 and the density of closed points of Proposition P3.1.35.) Show by an example that the conclusion fails if only $f(x) = g(x)$ is known for every closed point.

### Lean

Mathlib proves that monomorphisms are separated (`AlgebraicGeometry.isSeparated_of_mono`), the stability under composition and base change as instances, and the cancellation `AlgebraicGeometry.IsSeparated.of_comp`. The equalizer of two morphisms into a separated scheme over $S$ is a closed immersion, `AlgebraicGeometry.isClosedImmersion_equalizer_ι_left`. The reduced-to-separated theorem is `AlgebraicGeometry.ext_of_isDominant_of_isSeparated'`, with the variant `AlgebraicGeometry.ext_of_isDominant` over $\operatorname{Spec} \mathbb{Z}$. The handbook adds no `MinimalModel` node here.

### Notes and history

The stability properties are in EGA I, Chapter I, and in Hartshorne, Section II.4, where several are exercises. The literature state is theorem. Theorem P3.4.11 is the reason why a rational map between varieties has a well-defined domain, which is used for the birational maps of the program: the flips of P5, the indeterminacy locus of a rational map in P4, and the uniqueness of the extension of a rational map across a set of codimension two on a normal variety into a proper target.
