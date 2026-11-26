---
title: Additive categories
nodes: []
sources: [Wei94, Vak25, Mac98]
reads_with: [Wei94:appA, Vak25:ch1, Mac98:ch8]
requires: [P1.1, P2.1]
level: prereq
kind: background
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Additive categories

### Statement

**Definition P2.2.1 (preadditive category).** A category $\mathcal{A}$ is *preadditive* if each set $\operatorname{Hom}(A, B)$ is an abelian group and composition is bilinear: $(g + g') \circ f = g \circ f + g' \circ f$ and $g \circ (f + f') = g \circ f + g \circ f'$.

Lean: Mathlib `CategoryTheory.Preadditive`.

**Definition P2.2.2 (zero object).** An object $0$ is a *zero object* if it is both initial and terminal. In a preadditive category this holds if and only if $1_0 = 0$ in the group $\operatorname{Hom}(0, 0)$. Between any two objects $A, B$ the *zero map* is $A \to 0 \to B$. In a preadditive category with a zero object it is the neutral element of $\operatorname{Hom}(A, B)$.

Lean: Mathlib `CategoryTheory.Limits.HasZeroObject` and `CategoryTheory.Limits.HasZeroMorphisms`.

*Proof of the claim.* If $1_0 = 0$, then every $f: 0 \to B$ equals $f \circ 1_0 = f \circ 0 = 0$, so $\operatorname{Hom}(0, B) = \{0\}$, and dually $\operatorname{Hom}(A, 0) = \{0\}$. Conversely, if $0$ is initial then $\operatorname{Hom}(0, 0)$ has one element, so $1_0 = 0$. The map $A \to 0 \to B$ is $0 \circ 0 = 0$ by bilinearity. $\square$

**Definition P2.2.3 (biproduct).** Let $\mathcal{A}$ be preadditive. A *biproduct* of $A_1$ and $A_2$ is an object $A_1 \oplus A_2$ with maps $\iota_k: A_k \to A_1 \oplus A_2$ and $p_k: A_1 \oplus A_2 \to A_k$ such that
$$p_1 \iota_1 = 1_{A_1}, \quad p_2 \iota_2 = 1_{A_2}, \quad p_1 \iota_2 = 0, \quad p_2 \iota_1 = 0, \quad \iota_1 p_1 + \iota_2 p_2 = 1_{A_1 \oplus A_2}.$$

Lean: Mathlib `CategoryTheory.Limits.BinaryBiproduct` and `CategoryTheory.Limits.biprod` (written `X ⊞ Y`).

**Proposition P2.2.4 (products are biproducts).** In a preadditive category, a biproduct $(A_1 \oplus A_2, \iota, p)$ is a product with the projections $p_k$ and a coproduct with the inclusions $\iota_k$. Conversely, if a product $A_1 \times A_2$ exists, it is a biproduct, with $\iota_1 = (1, 0)$ and $\iota_2 = (0, 1)$.

Lean: Mathlib `CategoryTheory.Limits.HasBinaryBiproducts.of_hasBinaryProducts` and `CategoryTheory.Limits.biprod.isoProd` (proved in Mathlib).

*Proof.* Let $f_k: T \to A_k$. The map $f = \iota_1 f_1 + \iota_2 f_2$ satisfies $p_k f = f_k$. If $g$ also does, then $g = (\iota_1 p_1 + \iota_2 p_2) g = \iota_1 f_1 + \iota_2 f_2 = f$. So the biproduct is a product. The coproduct statement is the dual. Conversely, let $P = A_1 \times A_2$ with projections $p_1, p_2$, and define $\iota_1, \iota_2$ by the universal property, so that $p_1 \iota_1 = 1$, $p_2 \iota_1 = 0$, $p_1 \iota_2 = 0$ and $p_2 \iota_2 = 1$. Then $p_k (\iota_1 p_1 + \iota_2 p_2) = p_k$ for $k = 1, 2$, so $\iota_1 p_1 + \iota_2 p_2 = 1_P$ by the uniqueness in the universal property. $\square$

**Definition P2.2.5 (additive category, additive functor).** A preadditive category is *additive* if it has a zero object and a biproduct of any two objects. A functor $F: \mathcal{A} \to \mathcal{B}$ between preadditive categories is *additive* if each map $\operatorname{Hom}(A, B) \to \operatorname{Hom}(F(A), F(B))$ is a group homomorphism.

Lean: Mathlib `CategoryTheory.Functor.Additive`; an additive category is `Preadditive` with `HasZeroObject` and `HasFiniteBiproducts`.

An additive functor preserves biproducts, since the biproduct is defined by equations among maps that an additive functor keeps. So it preserves finite products and finite coproducts.

**Definition P2.2.6 (kernel, cokernel).** Let $\mathcal{A}$ be preadditive with a zero object and let $f: A \to B$. A *kernel* of $f$ is a map $k: K \to A$ with $f k = 0$ such that every $g: T \to A$ with $f g = 0$ factors as $g = k h$ for a unique $h: T \to K$. A *cokernel* of $f$ is a map $c: B \to C$ with $c f = 0$ such that every $g: B \to T$ with $g f = 0$ factors uniquely through $c$. A kernel is the equalizer of $f$ and $0$, so it is unique up to unique isomorphism.

Lean: Mathlib `CategoryTheory.Limits.kernel` and `CategoryTheory.Limits.cokernel`, with the maps `kernel.ι` and `cokernel.π`.

A kernel is a monomorphism: if $k u = k v$, then both $u$ and $v$ are the factorization of $k u$ through $k$, so $u = v$. Dually a cokernel is an epimorphism. In a preadditive category, $f$ is a monomorphism if and only if $f g = 0$ implies $g = 0$, since $f u = f v$ means $f(u - v) = 0$.

### Examples

**Example P2.2.7 (modules and their subcategories).** The category $\mathsf{Mod}_A$ is additive: $\operatorname{Hom}_A(M, N)$ is an abelian group, the zero module is a zero object, and $M \oplus N$ is the biproduct. The kernel of $f$ is the inclusion of $\ker f$, and the cokernel is the projection $N \to N/f(M)$. The full subcategory of free modules is additive, and so is the full subcategory of finitely generated projective modules. Kernels and cokernels in a full subcategory can differ from those in $\mathsf{Mod}_A$. Let $\mathcal{F}$ be the full subcategory of finitely generated free abelian groups, and let $f = 2: \mathbb{Z} \to \mathbb{Z}$. A map $g: \mathbb{Z} \to T$ in $\mathcal{F}$ with $g f = 0$ satisfies $2 g(1) = 0$, so $g(1) = 0$ since $T$ has no torsion. So $g = 0$, and the zero map $\mathbb{Z} \to 0$ is a cokernel of $f$ in $\mathcal{F}$. The cokernel $\mathbb{Z}/2$ in $\mathsf{Mod}_{\mathbb{Z}}$ is not in $\mathcal{F}$, and $\mathcal{F}$ replaces it by $0$. Section 2.2 uses this example to show that $\mathcal{F}$ is not abelian.

**Example P2.2.8 (vector bundles and presheaves).** For a topological space $X$, the presheaves of abelian groups on $X$ (functors $\operatorname{Op}(X)^{\mathrm{op}} \to \mathsf{Ab}$) form an additive category, with all operations taken one open set at a time. The real vector bundles on $X$, with the bundle maps, form an additive category. A map of bundles need not have a kernel that is a bundle: the map $X \times \mathbb{R} \to X \times \mathbb{R}$, $(x, v) \mapsto (x, xv)$ on $X = \mathbb{R}$ has rank $0$ at $x = 0$ and rank $1$ elsewhere, so its pointwise kernel is a line at $x = 0$ and zero elsewhere, and it is not a vector bundle. This is why algebraic geometry works with coherent sheaves and not only with vector bundles: Chapter 6 shows that the sheaf of sections of a bundle is a sheaf of modules, and the kernel and cokernel of a map of such sheaves exist as sheaves.

**Example P2.2.9 (a category that is not preadditive).** The category $\mathsf{Set}$ is not preadditive: $\operatorname{Hom}(\{*\}, \emptyset)$ is empty, so it is not a group. The category $\mathsf{Grp}$ has a zero object, the trivial group, but the set of homomorphisms between two nonabelian groups is not a group under pointwise product, since the product of two homomorphisms need not be a homomorphism.

### Exercises

1. (A) Show that in a preadditive category $f: A \to B$ is an epimorphism if and only if $g f = 0$ implies $g = 0$.
2. (A) Let $\mathcal{A}$ be additive. Show that the map $\operatorname{Hom}(A, B) \times \operatorname{Hom}(A, B) \to \operatorname{Hom}(A, B)$, $(f, g) \mapsto f + g$, is the composite $A \xrightarrow{\Delta} A \oplus A \xrightarrow{f \oplus g} B \oplus B \xrightarrow{\nabla} B$. Deduce that the group structure on the Hom sets of an additive category is determined by the category.
3. (A) Show that the opposite of an additive category is additive, and that kernels in $\mathcal{A}^{\mathrm{op}}$ are cokernels in $\mathcal{A}$.
4. (B) Show that a functor between additive categories that preserves finite biproducts is additive.
5. (B) Let $\mathcal{A}$ be additive and $A$ an object. Show that $\operatorname{End}(A) = \operatorname{Hom}(A, A)$ is a ring, and that $\operatorname{Hom}(A, -)$ is an additive functor to the category of right $\operatorname{End}(A)$-modules.
6. (B) Let $\mathcal{F}$ be the category of finitely generated free abelian groups. Show that every map in $\mathcal{F}$ has a kernel and a cokernel in $\mathcal{F}$, and compute the cokernel of $\mathbb{Z}^2 \to \mathbb{Z}^2$ given by the matrix with rows $(2, 0)$ and $(0, 3)$. (Hint: the cokernel in $\mathcal{F}$ is the quotient of the module cokernel by its torsion.)

### Lean

Mathlib has `CategoryTheory.Preadditive` for the group structure on Hom sets, `Limits.HasZeroObject` and `Limits.HasZeroMorphisms` for zero objects and zero maps, `Limits.biprod` for binary biproducts, and `Functor.Additive` for additive functors. The construction of biproducts from products in a preadditive category is `HasBinaryBiproducts.of_hasBinaryProducts`. Kernels and cokernels are `Limits.kernel` and `Limits.cokernel`. Mathlib has no single class for additive categories; it uses the combination of these classes. The handbook adds no `MinimalModel` node here.

### Notes and history

Additive categories appear in Mac Lane's paper of 1950 on duality for groups and in Buchsbaum's thesis of 1955. Grothendieck's Tohoku paper of 1957 made the axioms standard. The fact that the addition of maps is determined by the category, in Exercise 2, explains why the handbook can speak of an additive category as a category with a property and not with an extra structure.
