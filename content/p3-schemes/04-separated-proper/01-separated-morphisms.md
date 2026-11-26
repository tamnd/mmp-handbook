---
title: The diagonal and separated morphisms
nodes: []
sources: [Vak25, Har77, GW20, EGA1, Stacks]
reads_with: [Vak25:ch11, Har77:II.4, GW20:ch9]
requires: [P1.1, P3.1, P3.2, P3.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The diagonal and separated morphisms

### Statement

**Definition P3.4.1 (diagonal, separated, quasi-separated).** Let $f \colon X \to Y$ be a morphism of schemes. The *diagonal* of $f$ is the morphism $\Delta = \Delta_{X/Y} = (\mathrm{id}_X, \mathrm{id}_X) \colon X \to X \times_Y X$. The morphism $f$ is *separated* if $\Delta$ is a closed immersion, and *quasi-separated* if $\Delta$ is quasi-compact. A scheme $X$ is separated if $X \to \operatorname{Spec} \mathbb{Z}$ is separated, and an $S$-scheme is separated over $S$ if its structure morphism is.

Lean: Mathlib `CategoryTheory.Limits.pullback.diagonal`, `AlgebraicGeometry.IsSeparated` and `AlgebraicGeometry.QuasiSeparated` (definitions in Mathlib).

**Proposition P3.4.2 (the diagonal is an immersion).** Let $f \colon X \to Y$ be a morphism.

1. If $X$ and $Y$ are affine, then $\Delta_{X/Y}$ is a closed immersion. So every morphism of affine schemes is separated.
2. In general, $\Delta_{X/Y}$ is a closed immersion into an open subscheme of $X \times_Y X$. So $\Delta_{X/Y}$ is an immersion, and $f$ is separated if and only if $\Delta(X)$ is closed in $X \times_Y X$.

Lean: Mathlib `AlgebraicGeometry.isSeparated_eq_diagonal_isClosedImmersion`, and the instance `IsSeparated (Spec.map f)` (proved in Mathlib).

**Proposition P3.4.3 (separatedness with affine open sets).** Let $X$ be a scheme over a ring $A$.

1. Let $U, V \subseteq X$ be affine open sets. Then $\Delta^{-1}(U \times_A V) = U \cap V$.
2. $X$ is separated over $A$ if and only if, for every pair of affine open sets $U, V \subseteq X$, the intersection $U \cap V$ is affine and the map $\mathcal{O}_X(U) \otimes_A \mathcal{O}_X(V) \to \mathcal{O}_X(U \cap V)$, $b \otimes c \mapsto b|_{U \cap V} \, c|_{U \cap V}$, is surjective.
3. It is enough to check the condition of part 2 for the pairs $U_i, U_j$ of one affine open cover $X = \bigcup_i U_i$.

Lean: Mathlib `AlgebraicGeometry.IsSeparated.hasAffineProperty` gives the reduction to an affine base; the criterion of parts 2 and 3 is not in Lean as stated.

### Proof in words

The diagonal is a closed immersion on affine pieces because multiplication $B \otimes_A B \to B$ is surjective. So the only question is whether the image of the diagonal is closed, and this is the analogue of the classical fact that a space is Hausdorff exactly when its diagonal is closed.

The preimage of a product $U \times_A V$ under the diagonal is $U \cap V$. So the diagonal is a closed immersion over $U \times_A V$ exactly when $U \cap V$ is a closed subscheme of the affine scheme $U \times_A V$, that is, when $U \cap V$ is affine and its ring is a quotient of $\mathcal{O}(U) \otimes_A \mathcal{O}(V)$. In words: on a separated scheme, the functions on $U$ and on $V$ together generate the functions on $U \cap V$.

### Examples

**Example P3.4.4 (the doubled origin is not separated).** Let $X$ be the affine line with a doubled origin of Example P3.2.5, glued from $U = \operatorname{Spec} k[x]$ and $V = \operatorname{Spec} k[y]$ along $U \cap V = \operatorname{Spec} k[x, x^{-1}]$, with $y = x$. Then $U \cap V$ is affine, but the image of $k[x] \otimes_k k[y] \to k[x, x^{-1}]$, $x \mapsto x$, $y \mapsto x$, is $k[x]$. So $X$ is not separated over $k$ by Proposition P3.4.3. In terms of the diagonal: $U \times_k V = \mathbb{A}^2_k$, and $\Delta^{-1}(U \times_k V) = U \cap V$ embeds in $\mathbb{A}^2_k$ as the diagonal minus the origin, which is not closed in $\mathbb{A}^2_k$. The missing point is the pair $(0_U, 0_V)$ of the two origins.

**Example P3.4.5 (the plane with a doubled origin).** Glue two copies of $\mathbb{A}^2_k$ along $\mathbb{A}^2_k \setminus \{0\}$ by the identity. The intersection of the two affine charts is $\mathbb{A}^2_k \setminus \{0\}$, which is not affine by Example P3.1.20. So this scheme is not separated, and it shows that the intersection of two affine open sets of a scheme need not be affine.

**Example P3.4.6 (projective space is separated).** Let $A$ be a ring and $U_i = \operatorname{Spec} A[x_0/x_i, \dots, x_n/x_i]$ the charts of $\mathbb{P}^n_A$. Then $U_i \cap U_j = \operatorname{Spec} A[x_0/x_i, \dots, x_n/x_i][x_i/x_j]$, an affine scheme. Its ring is generated over $A$ by the elements $x_k/x_i$, which come from $\mathcal{O}(U_i)$, and by $x_i/x_j$, which comes from $\mathcal{O}(U_j)$. So the map of Proposition P3.4.3 is surjective, and $\mathbb{P}^n_A$ is separated over $A$ by part 3.

**Example P3.4.7 (a scheme that is not quasi-separated).** Let $A = k[x_1, x_2, \dots]$, a polynomial ring in infinitely many variables, and glue two copies of $\operatorname{Spec} A$ along the open set $W = \operatorname{Spec} A \setminus V(x_1, x_2, \dots)$ by the identity. The set $W = \bigcup_i D(x_i)$ is not quasi-compact, since no finite union $D(x_1) \cup \dots \cup D(x_m)$ contains the point $V(x_1, \dots, x_m, x_{m+1} - 1, x_{m+2}, \dots)$, which lies in $D(x_{m+1})$. The two affine charts are quasi-compact, but their intersection $W$ is not, so the diagonal is not quasi-compact (Exercise 4).

**Example P3.4.8 (open subsets of affine schemes).** Every open subscheme $X$ of an affine scheme $\operatorname{Spec} A$ is separated, by Proposition P3.4.9 below: an open immersion is separated, and a composite of separated morphisms is separated. For $X = \mathbb{A}^2_k \setminus \{0\} = D(x) \cup D(y)$ the criterion reads as follows. The intersection $D(x) \cap D(y) = D(xy)$ is affine, and $k[x, y]_x \otimes_k k[x, y]_y \to k[x, y]_{xy}$ is surjective. So the intersection of two affine open sets can be affine while their union is not.

### Proof

*Proof of Proposition P3.4.2.* Part 1. Let $Y = \operatorname{Spec} A$ and $X = \operatorname{Spec} B$. By Theorem P3.3.19, $X \times_Y X = \operatorname{Spec}(B \otimes_A B)$, and $\Delta$ corresponds by Theorem P3.1.22 to the ring map $\mu \colon B \otimes_A B \to B$, $b \otimes c \mapsto bc$, since its composites with the two maps $B \to B \otimes_A B$ are the identity. The map $\mu$ is surjective, since $\mu(b \otimes 1) = b$. By Proposition P3.1.32, $\Delta$ is a closed immersion.

Part 2. Cover $Y$ by affine open sets $V_j$, and cover each $f^{-1}(V_j)$ by affine open sets $U_{ij}$. Let $p_1, p_2 \colon X \times_Y X \to X$ be the projections. By part 1 of Proposition P3.3.20, $W_{ij} = p_1^{-1}(U_{ij}) \cap p_2^{-1}(U_{ij})$ is the affine scheme $U_{ij} \times_{V_j} U_{ij}$. A point $x \in U_{ij}$ has $\Delta(x) \in W_{ij}$, and $\Delta^{-1}(W_{ij}) = U_{ij} \cap U_{ij} = U_{ij}$, since $p_1 \Delta = p_2 \Delta = \mathrm{id}$. So $\Delta$ maps $X$ into the open set $W = \bigcup W_{ij}$. The restriction $\Delta^{-1}(W_{ij}) \to W_{ij}$ is the diagonal of $U_{ij} \to V_j$, which is a closed immersion by part 1. By part 1 of Proposition P3.3.11, $\Delta \colon X \to W$ is a closed immersion. If $\Delta(X)$ is closed in $X \times_Y X$, then $\Delta$ is a homeomorphism onto a closed set, and the surjectivity of $\mathcal{O}_{X \times_Y X} \to \Delta_* \mathcal{O}_X$ is a condition on stalks: at points of $W$ it holds since $\Delta \colon X \to W$ is a closed immersion, and at points outside $\Delta(X)$ the target stalk is $0$. So $\Delta$ is a closed immersion. The converse is clear. $\square$

*Proof of Proposition P3.4.3.* Part 1. A point $z \in X$ has $\Delta(z) \in U \times_A V = p_1^{-1}(U) \cap p_2^{-1}(V)$ if and only if $p_1 \Delta(z) = z \in U$ and $p_2 \Delta(z) = z \in V$.

Part 2. Let $B = \mathcal{O}_X(U)$ and $C = \mathcal{O}_X(V)$, so $U \times_A V = \operatorname{Spec}(B \otimes_A C)$ by Theorem P3.3.19. The restriction $\Delta_{UV} \colon U \cap V \to U \times_A V$ of the diagonal has components the two inclusions $U \cap V \to U$ and $U \cap V \to V$. By Theorem P3.1.22, it corresponds on global sections to the map $B \otimes_A C \to \mathcal{O}_X(U \cap V)$ of the statement.

If $X$ is separated over $A$, the restriction $\Delta_{UV}$ is a closed immersion into the affine scheme $U \times_A V$. By Theorem P3.3.10, $U \cap V$ is affine and the map on global sections is surjective.

Conversely, suppose the condition holds for all pairs from an affine open cover $\{U_i\}$; this also proves part 3. The open sets $U_i \times_A U_j$ cover $X \times_A X$: a point $z$ of the product has $p_1(z) \in U_i$ and $p_2(z) \in U_j$ for some $i, j$. Over $U_i \times_A U_j$, the diagonal is $\Delta_{U_i U_j} \colon U_i \cap U_j \to U_i \times_A U_j$, by part 1. By hypothesis $U_i \cap U_j$ is affine and $\Delta_{U_i U_j}$ is $\operatorname{Spec}$ of a surjective ring map, so it is a closed immersion by Proposition P3.1.32. By part 1 of Proposition P3.3.11, $\Delta$ is a closed immersion. $\square$

### Exercises

1. (A) Show that the affine line with a doubled origin satisfies: there are two morphisms $\mathbb{A}^1_k \to X$ that agree on $\mathbb{A}^1_k \setminus \{0\}$ and are different. Compute the preimage of $\Delta(X)$ under the morphism $\mathbb{A}^1_k \to X \times_k X$ that they define.
2. (A) The projective line $\mathbb{P}^1_k$ and the affine line with a doubled origin are both glued from two copies of $\mathbb{A}^1_k$ along $\mathbb{A}^1_k \setminus \{0\}$, by $x \mapsto 1/x$ and by $x \mapsto x$. Explain in terms of Proposition P3.4.3 why one is separated and the other is not.
3. (A) Show that a morphism $f \colon X \to Y$ is separated if and only if $f^{-1}(V) \to V$ is separated for every $V$ in an open cover of $Y$.
4. (B) Let $X$ be a scheme over a ring $A$. Show that $X \to \operatorname{Spec} A$ is quasi-separated if and only if the intersection of any two affine open sets of $X$ is quasi-compact. Deduce that the scheme of Example P3.4.7 is not quasi-separated.
5. (B) Show that every Noetherian scheme is quasi-separated, and that every affine scheme is quasi-separated over $\operatorname{Spec} \mathbb{Z}$.
6. (B) Let $X$ be a separated scheme. Show that for any affine open sets $U, V \subseteq X$ the intersection $U \cap V$ is affine, by applying Proposition P3.4.3 over $A = \mathbb{Z}$.
7. (C) Let $X$ be the plane with a doubled origin of Example P3.4.5. Show that the diagonal $\Delta(X)$ is not closed in $X \times_k X$, and describe its closure.

### Lean

Mathlib defines `AlgebraicGeometry.IsSeparated` by the condition that `CategoryTheory.Limits.pullback.diagonal f` is a closed immersion, with the equation `AlgebraicGeometry.isSeparated_eq_diagonal_isClosedImmersion`. Morphisms of affine schemes are separated by an instance for `Spec.map`, and `AlgebraicGeometry.IsSeparated.hasAffineProperty` reduces separatedness to an affine base. The class `AlgebraicGeometry.QuasiSeparated` is the quasi-compactness of the diagonal. The handbook adds no `MinimalModel` node here.

### Notes and history

In EGA I a "scheme" is separated, and a not necessarily separated scheme is a "prescheme"; the modern usage drops the separatedness. Hartshorne treats separated morphisms in Section II.4. The criterion of Proposition P3.4.3 is in Vakil and in the Stacks project. The literature state is theorem. Every variety of the program is separated, and the non-separated schemes of this section return only as warnings: a moduli functor that is not separated, such as the functor of all curves without stability conditions, has a doubled-origin phenomenon, and the stability conditions of P8 are chosen to remove it.
