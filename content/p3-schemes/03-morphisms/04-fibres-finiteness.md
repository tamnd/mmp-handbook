---
title: Fibres and finiteness conditions on morphisms
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch7, Vak25:ch10, Har77:II.3, GW20:ch10, GW20:ch12]
requires: [P1.2, P1.4, P3.1, P3.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Fibres and finiteness conditions on morphisms

### Statement

**Definition P3.3.27 (fibre).** Let $f \colon X \to Y$ be a morphism and $y \in Y$. The *fibre* of $f$ over $y$ is the $\kappa(y)$-scheme $X_y = X \times_Y \operatorname{Spec} \kappa(y)$, where $\operatorname{Spec} \kappa(y) \to Y$ is the morphism with image $y$ given on an affine open $\operatorname{Spec} A \ni y$ by the ring map $A \to \kappa(y)$, as in Example P3.1.26. It does not depend on the choice of $\operatorname{Spec} A$, since the ring maps agree on basic open sets of both. If $Y$ is integral with generic point $\eta$, the fibre $X_\eta$ is the *generic fibre*.

Lean: Mathlib `AlgebraicGeometry.Scheme.Hom.fiber` (definition in Mathlib).

**Proposition P3.3.28 (the fibre as a space).** The projection $X_y \to X$ is a homeomorphism onto the subspace $f^{-1}(y)$. If $Y = \operatorname{Spec} A$, $X = \operatorname{Spec} B$ and $y = \mathfrak{p}$, then $X_y = \operatorname{Spec}(B_\mathfrak{p}/\mathfrak{p} B_\mathfrak{p})$, where $B_\mathfrak{p}$ is the localization of $B$ at the image of $A \setminus \mathfrak{p}$.

Lean: Mathlib `AlgebraicGeometry.Scheme.Hom.fiberHomeo` (proved in Mathlib).

**Definition P3.3.29 (finiteness conditions).** Let $f \colon X \to Y$ be a morphism of schemes.

1. $f$ is *quasi-compact* if $f^{-1}(V)$ is quasi-compact for every affine open $V \subseteq Y$.
2. $f$ is *affine* if $f^{-1}(V)$ is affine for every affine open $V \subseteq Y$.
3. $f$ is *finite* if it is affine and, for every affine open $V \subseteq Y$, the ring $\mathcal{O}_X(f^{-1}(V))$ is a finitely generated $\mathcal{O}_Y(V)$-module.
4. $f$ is *locally of finite type* if for every affine open $V \subseteq Y$ and every affine open $U \subseteq f^{-1}(V)$ the ring $\mathcal{O}_X(U)$ is a finitely generated $\mathcal{O}_Y(V)$-algebra.
5. $f$ is *of finite type* if it is locally of finite type and quasi-compact.

A scheme over $k$ is of finite type over $k$ if its structure morphism is, which matches Definition P3.2.25.

Lean: Mathlib `AlgebraicGeometry.QuasiCompact`, `AlgebraicGeometry.IsAffineHom`, `AlgebraicGeometry.IsFinite` and `AlgebraicGeometry.LocallyOfFiniteType` (definitions in Mathlib). Mathlib has no single class for finite type; it uses `LocallyOfFiniteType` together with `QuasiCompact`.

**Proposition P3.3.30 (affine and finite are local on the target).** Let $f \colon X \to Y$ be a morphism and $Y = \bigcup_j V_j$ an open cover by affine open sets.

1. If every $f^{-1}(V_j)$ is affine, then $f$ is affine.
2. If also every $\mathcal{O}_X(f^{-1}(V_j))$ is a finite $\mathcal{O}_Y(V_j)$-module, then $f$ is finite. In particular $\operatorname{Spec} B \to \operatorname{Spec} A$ is finite if and only if $B$ is a finite $A$-module.

Lean: Mathlib `AlgebraicGeometry.HasAffineProperty` instances for `IsAffineHom` and `IsFinite`, and `AlgebraicGeometry.IsFinite.SpecMap_iff` (proved in Mathlib).

**Proposition P3.3.31 (finite type is local).** Let $f \colon X \to Y$ be a morphism. Suppose $Y$ has an open cover by affine open sets $V_j = \operatorname{Spec} A_j$ and each $f^{-1}(V_j)$ has an open cover by affine open sets $U_{ij} = \operatorname{Spec} B_{ij}$ with $B_{ij}$ a finitely generated $A_j$-algebra. Then $f$ is locally of finite type.

Lean: Mathlib `AlgebraicGeometry.LocallyOfFiniteType` is defined through `HasRingHomProperty` with `RingHom.FiniteType`, and this instance contains the locality (proved in Mathlib).

**Proposition P3.3.32 (composition and base change).** Each of the classes quasi-compact, affine, finite and locally of finite type, and so also of finite type, contains the isomorphisms, is stable under composition, and is stable under base change: if $f \colon X \to Y$ is in the class and $Y' \to Y$ is any morphism, then $X \times_Y Y' \to Y'$ is in the class. Closed immersions are finite.

Lean: Mathlib `AlgebraicGeometry.quasiCompact_comp`, `AlgebraicGeometry.quasiCompact_isStableUnderBaseChange`, `AlgebraicGeometry.isAffineHom_isStableUnderBaseChange`, `AlgebraicGeometry.locallyOfFiniteType_comp`, `AlgebraicGeometry.locallyOfFiniteType_isStableUnderBaseChange`, and the instances `IsStableUnderComposition @IsFinite` and `IsStableUnderBaseChange @IsFinite` (proved in Mathlib).

### Proof in words

The fibre over $y$ is computed on an affine piece by two operations on rings: localize at $\mathfrak{p}$ to forget the points over the complement of the closure of $y$, then divide by $\mathfrak{p}$ to keep only the points over $y$. Both operations give homeomorphisms onto subspaces, and the fibre is the set $f^{-1}(y)$ with a scheme structure that can be non-reduced.

The finiteness conditions are defined for all affine open sets, and the work is to show that one cover is enough. For affine and finite morphisms the affineness criterion of Theorem P3.3.4 does this. For finite type the argument is the affine communication lemma with one more lemma from algebra: finite generation can be checked on a cover by basic open sets.

### Examples

**Example P3.3.33 (the fibres of the affine line over the integers).** Let $f \colon \mathbb{A}^1_{\mathbb{Z}} \to \operatorname{Spec} \mathbb{Z}$. By Proposition P3.3.28 the fibre over $(p)$ is $\operatorname{Spec}(\mathbb{Z}_{(p)}[x]/p\mathbb{Z}_{(p)}[x]) = \operatorname{Spec} \mathbb{F}_p[x] = \mathbb{A}^1_{\mathbb{F}_p}$, and the generic fibre is $\operatorname{Spec} \mathbb{Q}[x] = \mathbb{A}^1_{\mathbb{Q}}$. So the picture of Example P3.1.36, with one line over each prime and one line over the generic point, is the picture of the fibres.

**Example P3.3.34 (the family $xy = t$).** Let $X = \operatorname{Spec} k[x, y, t]/(xy - t)$ and $f \colon X \to \mathbb{A}^1_k = \operatorname{Spec} k[t]$. For $a \in k$ the fibre over $t = a$ is $\operatorname{Spec} k[x, y]/(xy - a)$. For $a \neq 0$ it is a hyperbola, isomorphic to $\mathbb{A}^1_k \setminus \{0\}$ by $x \mapsto (x, a/x)$. For $a = 0$ it is the union of the two axes. The generic fibre is $\operatorname{Spec} k(t)[x, y]/(xy - t) \cong \operatorname{Spec} k(t)[x, x^{-1}]$, a smooth curve over $k(t)$. The total space $X$ is $\mathbb{A}^2_k$ with coordinates $x, y$, since $t = xy$ is determined by $x, y$. So a smooth surface fibres over a line with smooth fibres that degenerate to a node. This is the local model of the nodal fibres of Chapter 7 and of the semistable families of P8.

**Example P3.3.35 (the family $t = x^2$).** Let $k$ be algebraically closed of characteristic not $2$, and let $f \colon \operatorname{Spec} k[x] \to \operatorname{Spec} k[t]$ be given by $t \mapsto x^2$. The ring $k[x]$ is a free $k[t]$-module with basis $1, x$, so $f$ is finite by Proposition P3.3.30. The fibre over $t = a \neq 0$ is $\operatorname{Spec} k[x]/(x^2 - a)$, two reduced points. The fibre over $t = 0$ is $\operatorname{Spec} k[x]/(x^2)$, one point with a nilpotent. The generic fibre is $\operatorname{Spec} k(t)[x]/(x^2 - t) = \operatorname{Spec} k(\sqrt{t})$, one point with a residue field of degree $2$. In every fibre the ring has dimension $2$ over the residue field of the base, which is the first instance of the constancy of the degree in flat families of Chapter 13.

**Example P3.3.36 (affine and of finite type, but not finite).** The open immersion $j \colon \mathbb{A}^1_k \setminus \{0\} = \operatorname{Spec} k[x, x^{-1}] \to \mathbb{A}^1_k$ has $j^{-1}(\mathbb{A}^1_k)$ affine, so $j$ is affine by Proposition P3.3.30. It is of finite type, since $k[x, x^{-1}] = k[x][y]/(xy - 1)$. It is not finite: $k[x, x^{-1}]$ is not a finitely generated $k[x]$-module, since a finitely generated submodule is contained in $x^{-n} k[x]$ for some $n$. Its fibres are finite, so finite fibres do not imply finite.

**Example P3.3.37 (a quasi-compact open immersion that is not affine).** The open immersion $j \colon U = \mathbb{A}^2_k \setminus \{0\} \to \mathbb{A}^2_k$ is quasi-compact and locally of finite type, so it is of finite type. It is not affine, since $j^{-1}(\mathbb{A}^2_k) = U$ is not affine by Example P3.1.20. Every open immersion is locally of finite type, since $U$ is covered by basic open sets $D(g) = \operatorname{Spec} A_g$ of affine open sets of the target, and $A_g = A[y]/(gy - 1)$.

**Example P3.3.38 (not of finite type).** The morphism $\operatorname{Spec} k(t) \to \operatorname{Spec} k[t]$ of the generic point is not locally of finite type. Suppose $k(t) = k[t][f_1/g_1, \dots, f_r/g_r]$. Every element of $k(t)$ then has a denominator that is a product of the $g_i$, up to a constant. An irreducible polynomial $h$ that divides none of the $g_i$ exists, since $k[t]$ has infinitely many irreducible polynomials, and $1/h$ has no such denominator. In the other direction, the disjoint union $\bigsqcup_{n \in \mathbb{N}} \operatorname{Spec} k \to \operatorname{Spec} k$ is locally of finite type but not quasi-compact.

### Proof

*Proof of Proposition P3.3.28.* Reduction to the affine case. Let $V = \operatorname{Spec} A$ be an affine open neighbourhood of $y$. The morphism $\operatorname{Spec} \kappa(y) \to Y$ factors through $V$, so $X_y = f^{-1}(V) \times_V \operatorname{Spec} \kappa(y)$ by part 1 of Proposition P3.3.20. Cover $f^{-1}(V)$ by affine open sets $U_i$. By the same part, $X_y$ is covered by the open sets $(U_i)_y = U_i \times_V \operatorname{Spec} \kappa(y)$, which are the preimages of the $U_i$ under the projection $X_y \to X$. If each $(U_i)_y \to U_i$ is a homeomorphism onto $U_i \cap f^{-1}(y)$, then the projection $X_y \to X$ is injective, with image $f^{-1}(y)$, and it is a homeomorphism onto its image, since this is a local property on an open cover of the target subspace.

The affine case. Let $\varphi \colon A \to B$ be the ring map and $y = \mathfrak{p}$. By Theorem P3.3.19, $X_y = \operatorname{Spec}(B \otimes_A \kappa(\mathfrak{p}))$, and $\kappa(\mathfrak{p}) = A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$ gives $B \otimes_A \kappa(\mathfrak{p}) = B_\mathfrak{p}/\mathfrak{p}B_\mathfrak{p}$ (P1 Ch. 1 and Ch. 2). Let $S = \varphi(A \setminus \mathfrak{p})$. The map $\operatorname{Spec} S^{-1}B \to \operatorname{Spec} B$ is a homeomorphism onto the set of primes $\mathfrak{q}$ with $\mathfrak{q} \cap S = \emptyset$: it is injective with this image by the correspondence of primes in a localization (P1 Ch. 2), and it is an embedding because the basic open set $D(b/s)$ of $S^{-1}B$ equals $D(b/1)$, which is the preimage of $D(b)$. The map $\operatorname{Spec} B_\mathfrak{p}/\mathfrak{p}B_\mathfrak{p} \to \operatorname{Spec} B_\mathfrak{p}$ is a homeomorphism onto $V(\mathfrak{p}B_\mathfrak{p})$ by Proposition P3.1.32. So $X_y \to X$ is a homeomorphism onto the set of primes $\mathfrak{q}$ of $B$ with $\varphi^{-1}(\mathfrak{q}) \subseteq \mathfrak{p}$ and $\varphi(\mathfrak{p}) \subseteq \mathfrak{q}$, that is, with $\varphi^{-1}(\mathfrak{q}) = \mathfrak{p}$. This is $f^{-1}(y)$. $\square$

*Proof of Proposition P3.3.30.* Let $V = \operatorname{Spec} A \subseteq Y$ be an affine open set, let $W = f^{-1}(V)$ and $B = \mathcal{O}_X(W)$. For each $y \in V$ choose $j$ with $y \in V_j$ and, by step 1 of the proof of Lemma P3.2.22, an open $D_A(g) = D_{A_j}(h)$ that contains $y$, where $A_j = \mathcal{O}_Y(V_j)$. Then $f^{-1}(D_A(g))$ is the basic open set of the affine scheme $f^{-1}(V_j)$ defined by the image of $h$, so it is affine, with ring $(B_j)_h$ where $B_j = \mathcal{O}_X(f^{-1}(V_j))$. Since $V$ is quasi-compact, finitely many such $D_A(g_1), \dots, D_A(g_r)$ cover $V$, and $(g_1, \dots, g_r) = A$ by Proposition P1.2.17.

Part 1. The images of the $g_k$ in $B$ generate the unit ideal, and $W_{g_k} = f^{-1}(D_A(g_k))$ is affine. By Theorem P3.3.4, $W$ is affine.

Part 2. Now $W = \operatorname{Spec} B$, and $B_{g_k} = \mathcal{O}_X(f^{-1}(D_A(g_k))) = (B_j)_h$ is a finite module over $(A_j)_h = A_{g_k}$, since $B_j$ is finite over $A_j$. Choose finitely many elements of $B$ whose images generate every $B_{g_k}$ over $A_{g_k}$; this is possible since each generator $b/g_k^n$ can be replaced by $b$. Let $M \subseteq B$ be the $A$-submodule they generate. Then $(B/M)_{g_k} = 0$ for every $k$, by exactness of localization. For a prime $\mathfrak{q}$ of $A$, some $g_k \notin \mathfrak{q}$, so $(B/M)_\mathfrak{q}$ is a localization of $(B/M)_{g_k} = 0$. Hence $B/M = 0$ (P1 Ch. 2), and $B$ is a finite $A$-module. For the last claim take the cover of $\operatorname{Spec} A$ by itself. $\square$

*Proof of Proposition P3.3.31.* Two facts from algebra. Let $A \to B$ be a ring map.

(a) If $B$ is a finitely generated $A$-algebra and $b \in B$, then $B_b = B[z]/(bz - 1)$ is a finitely generated $A$-algebra. If $a \in A$, then $B_a$ is a finitely generated $A_a$-algebra, with the same generators.

(b) Suppose $(b_1, \dots, b_r) = B$ and every $B_{b_k}$ is a finitely generated $A$-algebra. Then $B$ is a finitely generated $A$-algebra. Indeed, write $1 = \sum_k c_k b_k$, and choose generators $\beta_{kl}/b_k^{n}$ of $B_{b_k}$ with $\beta_{kl} \in B$. Let $C \subseteq B$ be the $A$-subalgebra generated by all $b_k$, $c_k$ and $\beta_{kl}$. For $\beta \in B$ and each $k$, the element $\beta/1$ of $B_{b_k}$ is a polynomial in the generators, so $b_k^{N} \beta \in C$ for some $N$, which can be taken the same for all $k$. Then $1 = (\sum_k c_k b_k)^{rN}$, and every monomial of the expansion contains some $b_k^{N}$. So $\beta = \sum (\text{elements of } C) \cdot b_k^N \beta \in C$.

Now let $V = \operatorname{Spec} A \subseteq Y$ be an affine open set and $U = \operatorname{Spec} B \subseteq f^{-1}(V)$ an affine open set. Call an affine open $U' \subseteq f^{-1}(V)$ good if $\mathcal{O}_X(U')$ is a finitely generated $A$-algebra.

Good sets cover $f^{-1}(V)$. Let $x \in f^{-1}(V)$, with $x \in U_{ij}$. By step 1 of the proof of Lemma P3.2.22 there is an open $D_A(g) = D_{A_j}(h)$ containing $f(x)$, and then $A_g = (A_j)_h$. The set $U_{ij} \cap f^{-1}(D_A(g))$ is the basic open set of $U_{ij}$ defined by the image of $h$, with ring $(B_{ij})_h$. By (a) this ring is finitely generated over $(A_j)_h = A_g$, and $A_g$ is finitely generated over $A$, so it is good.

Every affine open subset is good. The property "$\mathcal{O}_X(U')$ is a finitely generated $A$-algebra" passes to basic open sets of $U'$ by (a), and it holds for $U'$ if it holds for the sets of a cover of $U'$ by basic open sets, by (b) together with Proposition P1.2.17. These are the two hypotheses of Lemma P3.2.22, and its proof applies to the scheme $f^{-1}(V)$ word for word. So $U$ is good. $\square$

*Proof of Proposition P3.3.32.* Isomorphisms are in every class. Fix morphisms $f \colon X \to Y$, $g \colon Y \to Z$ and $u \colon Y' \to Y$, and write $X' = X \times_Y Y'$ with $f' \colon X' \to Y'$.

Composition. Let $V \subseteq Z$ be affine. If $f$ and $g$ are quasi-compact, $g^{-1}(V)$ is a finite union of affine open sets $V_k$ and $(gf)^{-1}(V) = \bigcup_k f^{-1}(V_k)$ is a finite union of quasi-compact sets. If both are affine, $(gf)^{-1}(V) = f^{-1}(g^{-1}(V))$ is affine. If both are finite, the ring of $(gf)^{-1}(V)$ is finite over that of $g^{-1}(V)$, which is finite over that of $V$, and a finite module over a finite algebra is finite. If both are locally of finite type, cover $g^{-1}(V)$ by affine open sets $V'$ and each $f^{-1}(V')$ by affine open sets $U$. Then $\mathcal{O}(U)$ is finitely generated over $\mathcal{O}(V')$, which is finitely generated over $\mathcal{O}(V)$. By Proposition P3.3.31, applied to the cover of $(gf)^{-1}(V)$ by these $U$, $gf$ is locally of finite type.

Base change. Let $V' \subseteq Y'$ be affine. Cover $V'$ by affine open sets $W'$ with $u(W')$ contained in an affine open $V \subseteq Y$; since $V'$ is quasi-compact, finitely many suffice. By part 1 of Proposition P3.3.20, $f'^{-1}(W') = f^{-1}(V) \times_V W'$. If $f$ is quasi-compact, $f^{-1}(V) = U_1 \cup \dots \cup U_n$ with $U_i$ affine, and $f^{-1}(V) \times_V W' = \bigcup_i U_i \times_V W'$ is a finite union of affine schemes by part 1 of Proposition P3.3.20 and Theorem P3.3.19. So $f'^{-1}(V')$ is quasi-compact. If $f$ is affine, $f^{-1}(V) = \operatorname{Spec} B$, and $f'^{-1}(W') = \operatorname{Spec}(B \otimes_A A')$ is affine, with $A = \mathcal{O}(V)$ and $A' = \mathcal{O}(W')$. If $f$ is finite, $B \otimes_A A'$ is a finite $A'$-module. The sets $W'$, for all $V'$, cover $Y'$, so $f'$ is affine or finite by Proposition P3.3.30. If $f$ is locally of finite type, $f'^{-1}(W')$ is covered by the sets $\operatorname{Spec}(B \otimes_A A')$ for affine open sets $\operatorname{Spec} B \subseteq f^{-1}(V)$, and $B \otimes_A A'$ is finitely generated over $A'$ by the images of generators of $B$. By Proposition P3.3.31, $f'$ is locally of finite type.

Closed immersions. A closed immersion is affine by part 2 of Proposition P3.3.11, and $A/I$ is generated by $1$ as an $A$-module, so it is finite. $\square$

### Exercises

1. (A) Compute the fibres of $\operatorname{Spec} \mathbb{Z}[i] \to \operatorname{Spec} \mathbb{Z}$ over $(2)$, $(3)$, $(5)$ and the generic point. Which are reduced, and how many points does each have?
2. (A) Let $f \colon \operatorname{Spec} k[x, y]/(y^2 - x^3) \to \operatorname{Spec} k[x]$ be the projection to the $x$-line. Show that $f$ is finite and compute all its fibres for $k$ algebraically closed.
3. (A) Show that the blow-up chart $\operatorname{Spec} k[x, u] \to \operatorname{Spec} k[x, y]$, $y \mapsto xu$, is of finite type but not finite, and compute its fibres over the origin and over a point $(a, b)$ with $a \neq 0$.
4. (B) Show that a finite morphism has finite fibres: every fibre is a finite discrete space. (Reduce to $\operatorname{Spec}$ of a finite-dimensional algebra over a field, and use P1 Ch. 4.)
5. (B) Show that a scheme of finite type over a Noetherian ring is Noetherian, using Proposition P3.2.23 and the Hilbert basis theorem.
6. (B) Let $X \to S$ and $Y \to S$ be of finite type. Show that $X \times_S Y \to S$ is of finite type. Deduce that a product of two schemes of finite type over $k$ is of finite type over $k$.
7. (C) Let $f \colon X \to Y$ be a morphism of schemes locally of finite type over a field $k$. Show that $f$ maps closed points to closed points. (Use P1.4.30: the residue fields of closed points are finite over $k$.) Give an example over a field that is not of finite type where this fails.

### Lean

The scheme-theoretic fibre is `AlgebraicGeometry.Scheme.Hom.fiber`, with the homeomorphism onto the set-theoretic fibre `AlgebraicGeometry.Scheme.Hom.fiberHomeo`. The finiteness classes are `AlgebraicGeometry.QuasiCompact`, `AlgebraicGeometry.IsAffineHom`, `AlgebraicGeometry.IsFinite` and `AlgebraicGeometry.LocallyOfFiniteType`. Mathlib proves locality on the target in the general framework `AlgebraicGeometry.HasAffineProperty`, and locality on both sides for `LocallyOfFiniteType` through `HasRingHomProperty` with `RingHom.FiniteType`. The stability results are instances. The handbook adds no `MinimalModel` node here.

### Notes and history

The finiteness conditions are in EGA I, Chapter I, with the systematic treatment in EGA II and IV. Hartshorne gives the definitions in Section II.3 with the local characterizations as exercises. The literature state is theorem. The families $xy = t$ and $t = x^2$ return throughout the program: the first in the local study of semistable degenerations, the second in the study of ramified covers and of the non-reduced fibres that a flat family can have.
