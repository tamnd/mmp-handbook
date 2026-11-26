---
title: Limits and colimits
nodes: []
sources: [Vak25, Mac98]
reads_with: [Vak25:ch1, Mac98:ch3, Mac98:ch5, Mac98:ch9]
requires: [P1.1, P1.2, P2.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Limits and colimits

### Statement

**Definition P2.1.39 (limit).** Let $I$ be a small category and $D: I \to \mathcal{C}$ a functor, called a *diagram* of shape $I$. A *cone* over $D$ is an object $L$ with maps $\pi_i: L \to D(i)$, one for each $i$, such that $D(u) \circ \pi_i = \pi_j$ for every $u: i \to j$. A *limit* of $D$ is a cone $(L, \pi)$ such that for every cone $(T, \tau)$ there is a unique $f: T \to L$ with $\pi_i \circ f = \tau_i$ for all $i$. It is written $\varprojlim D$ or $\lim_I D$. A *colimit* is a limit in $\mathcal{C}^{\mathrm{op}}$: a *cocone* $\iota_i: D(i) \to C$ with $\iota_j \circ D(u) = \iota_i$ through which every cocone factors uniquely. It is written $\varinjlim D$ or $\operatorname{colim}_I D$.

Lean: Mathlib `CategoryTheory.Limits.Cone`, `CategoryTheory.Limits.IsLimit`, `CategoryTheory.Limits.limit` and `CategoryTheory.Limits.colimit`.

The cones over $D$ with vertex $T$ form a set $\operatorname{Cone}(T, D)$, and $T \mapsto \operatorname{Cone}(T, D)$ is a functor $\mathcal{C}^{\mathrm{op}} \to \mathsf{Set}$. A limit is a representing object of this functor, with the cone $\pi$ as universal element. So by the Yoneda lemma a limit, if it exists, is unique up to a unique isomorphism that respects the cones. In other words, for a limit $L$,
$$\operatorname{Hom}(T, \varprojlim D) \cong \varprojlim_i \operatorname{Hom}(T, D(i)),$$
where the right side is the limit in $\mathsf{Set}$, the set of compatible families.

**Example P2.1.40 (the basic shapes).** The limit over a discrete category $I$ (only identity maps) is the *product* $\prod_i D(i)$. The colimit is the *coproduct* $\coprod_i D(i)$. The limit over the empty category is a terminal object, and the colimit is an initial object. For $I = \{1 \rightrightarrows 2\}$, a diagram is a pair $u, v: A \to B$, and its limit is the *equalizer*: a map $e: E \to A$ with $u e = v e$, universal among such. The colimit is the *coequalizer*. For $I = \{1 \to 3 \leftarrow 2\}$, a diagram is a pair $A \to C \leftarrow B$, and its limit is the *fibre product* $A \times_C B$. In $\mathsf{Mod}_A$ the kernel of $u: M \to N$ is the equalizer of $u$ and $0$, and the cokernel is the coequalizer.

**Example P2.1.41 (sets and modules).** In $\mathsf{Set}$ the product is the cartesian product, the coproduct is the disjoint union, the equalizer of $u, v: A \to B$ is $\{a : u(a) = v(a)\}$ and the fibre product is $\{(a, b) : f(a) = g(b)\}$. In $\mathsf{Mod}_A$ the product is the cartesian product, the coproduct is the direct sum $\bigoplus_i M_i$, the equalizer is $\ker(u - v)$ and the coequalizer is $B/\operatorname{im}(u - v)$. Finite products and finite coproducts of modules agree. Infinite ones do not.

**Theorem P2.1.42 (limits from products and equalizers).** If $\mathcal{C}$ has all small products and all equalizers, then every diagram $D: I \to \mathcal{C}$ with $I$ small has a limit. It is the equalizer of the two maps
$$\textstyle \prod_{i} D(i) \rightrightarrows \prod_{u: i \to j} D(j)$$
whose components at $u: i \to j$ are $\operatorname{pr}_j$ and $D(u) \circ \operatorname{pr}_i$. In particular $\mathsf{Set}$ and $\mathsf{Mod}_A$ have all small limits, and dually all small colimits.

Lean: Mathlib `CategoryTheory.Limits.has_limits_of_hasEqualizers_and_products` (proved in Mathlib).

**Theorem P2.1.43 (right adjoints preserve limits).** Let $F \dashv G$ with $G: \mathcal{D} \to \mathcal{C}$. If $(L, \pi)$ is a limit of $D: I \to \mathcal{D}$, then $(G(L), G(\pi))$ is a limit of $G \circ D$. Dually, a left adjoint preserves colimits.

Lean: Mathlib `CategoryTheory.Adjunction.rightAdjoint_preservesLimits` and `CategoryTheory.Adjunction.leftAdjoint_preservesColimits` (proved in Mathlib).

**Corollary P2.1.44 (right exactness of the tensor product).** For an $A$-module $N$, the functor $- \otimes_A N$ preserves all colimits: direct sums and cokernels. So it is right exact. The functor $\operatorname{Hom}_A(N, -)$ preserves all limits: products and kernels. So it is left exact.

Lean: Mathlib proves the right exactness as `lTensor_exact` and `rTensor_exact` in `Mathlib.LinearAlgebra.TensorProduct.RightExactness` (proved in Mathlib).

**Definition P2.1.45 (filtered category, filtered colimit).** A small category $I$ is *filtered* if it is nonempty, for any $i, j$ there are maps $i \to k$ and $j \to k$ to some $k$, and for any $u, v: i \to j$ there is $w: j \to k$ with $w u = w v$. A *filtered colimit* is a colimit over a filtered category. A directed set, seen as a category, is filtered, and a colimit over it is a *direct limit*.

Lean: Mathlib `CategoryTheory.IsFiltered`.

**Theorem P2.1.46 (filtered colimits of modules are exact).** Let $I$ be filtered and let $D' \to D \to D''$ be maps of diagrams $I \to \mathsf{Mod}_A$ such that $D'(i) \to D(i) \to D''(i)$ is exact for every $i$. Then $\operatorname{colim} D' \to \operatorname{colim} D \to \operatorname{colim} D''$ is exact. In particular a filtered colimit of injective maps is injective.

Lean: Mathlib `CategoryTheory.AB5` with the instance for `ModuleCat R` (proved in Mathlib), and `CategoryTheory.Limits.colimitLimitToLimitColimit_isIso` for filtered colimits and finite limits of sets.

### Proof in words

A limit is a universal cone, and the formula $\operatorname{Hom}(T, \varprojlim D) = \varprojlim \operatorname{Hom}(T, D(i))$ is its definition. A right adjoint $G$ turns maps into $G(L)$ into maps out of $F(T)$, where the universal property of $L$ applies. This proves that $G$ preserves limits, with no computation. The construction from products and equalizers says that a compatible family is a family in the product that satisfies one equation for each arrow of $I$.

Exactness of filtered colimits rests on a concrete description. An element of $\operatorname{colim} D$ comes from some $D(i)$, and it is zero there exactly when it becomes zero at some later stage $D(i) \to D(k)$. So a finite question about the colimit, such as whether an element lies in a kernel or an image, is decided at one stage. Colimits over other shapes, such as cokernels, are not exact, and limits, even over the natural numbers, are not exact either.

### Examples

**Example P2.1.47 (the $p$-adic integers and completion).** Let $p$ be a prime and let $D: \mathbb{N}^{\mathrm{op}} \to \mathsf{Ring}$ be the diagram $\cdots \to \mathbb{Z}/p^3 \to \mathbb{Z}/p^2 \to \mathbb{Z}/p$. Its limit is the ring $\mathbb{Z}_p$ of $p$-adic integers: sequences $(a_n)$ with $a_n \in \mathbb{Z}/p^n$ and $a_{n+1} \equiv a_n \bmod p^n$. In the same way the completion of P1 Ch. 6 is $\hat{M} = \varprojlim M/I^n M$. The theorem on formal functions of P4 Ch. 6, which proves Zariski's main theorem and gives Stein factorization in the contraction theorem of Volume 7, is a statement about such limits.

**Example P2.1.48 (stalks are filtered colimits).** Let $X$ be a space, $x \in X$, and $\mathcal{F}$ a presheaf of abelian groups on $X$. The open neighbourhoods of $x$, ordered by reverse inclusion, form a directed set, and the *stalk* is $\mathcal{F}_x = \varinjlim_{U \ni x} \mathcal{F}(U)$. An element is a germ: a section on some $U \ni x$, with two sections equal when they agree on a smaller neighbourhood. By the theorem, $\mathcal{F} \mapsto \mathcal{F}_x$ is exact on presheaves. Chapter 5 builds the exactness of sequences of sheaves on this fact.

**Example P2.1.49 (limits are not exact).** For each $n$ the sequence $0 \to p^n \mathbb{Z} \to \mathbb{Z} \to \mathbb{Z}/p^n \to 0$ is exact, and the three terms form diagrams over $\mathbb{N}^{\mathrm{op}}$ with the inclusions and the projections as maps. The limits are $\bigcap_n p^n \mathbb{Z} = 0$, then $\mathbb{Z}$ with the identity maps, then $\mathbb{Z}_p$. The sequence $0 \to 0 \to \mathbb{Z} \to \mathbb{Z}_p \to 0$ is not exact on the right, since $\mathbb{Z}_p$ is uncountable. The hypothesis of the theorem that fails is that the index category is filtered and the functor is a colimit. The defect is measured by the derived functor $\varprojlim^1$, and the Mittag-Leffler condition of P4 Ch. 6 makes it vanish.

**Example P2.1.50 (cokernels are not left exact).** Coequalizers are colimits over a category that is not filtered. Consider the map of diagrams from $\mathbb{Z} \xrightarrow{2} \mathbb{Z}$ to $\mathbb{Z} \xrightarrow{1} \mathbb{Z}$ given by multiplication by $2$ on the first term and the identity on the second. The square commutes, since both ways around send $x$ to $2x$. It is injective at each term. The cokernels are $\mathbb{Z}/2$ and $0$, and $\mathbb{Z}/2 \to 0$ is not injective.

### Proof

*Proof of the construction from products and equalizers.* Write $P = \prod_i D(i)$ and $Q = \prod_{u: i \to j} D(j)$, and let $s, t: P \to Q$ have components $s_u = \operatorname{pr}_j$ and $t_u = D(u) \circ \operatorname{pr}_i$ at $u: i \to j$. Let $e: L \to P$ be the equalizer of $s$ and $t$, and $\pi_i = \operatorname{pr}_i \circ e$. The equation $s e = t e$ says $\pi_j = D(u) \circ \pi_i$ for every $u$, so $(L, \pi)$ is a cone. A cone $(T, \tau)$ gives a map $\tau: T \to P$ by the universal property of the product, and the cone condition says $s \tau = t \tau$. So $\tau$ factors uniquely through $e$, which is the universal property of the limit. $\square$

*Proof that right adjoints preserve limits.* Let $\tau: \operatorname{Hom}(F(-), -) \cong \operatorname{Hom}(-, G(-))$ be the adjunction. The family $G(\pi_i)$ is a cone over $G \circ D$ because $G$ is a functor. Let $(T, \sigma)$ be a cone over $G \circ D$, with $\sigma_i: T \to G(D(i))$. By naturality of $\tau^{-1}$ in the second variable, the maps $\tau^{-1}(\sigma_i): F(T) \to D(i)$ form a cone over $D$: for $u: i \to j$, $D(u) \circ \tau^{-1}(\sigma_i) = \tau^{-1}(G(D(u)) \circ \sigma_i) = \tau^{-1}(\sigma_j)$. So there is a unique $g: F(T) \to L$ with $\pi_i \circ g = \tau^{-1}(\sigma_i)$. Put $f = \tau(g): T \to G(L)$. Then $G(\pi_i) \circ f = \tau(\pi_i \circ g) = \sigma_i$. If $f'$ is a second map with this property, then $g' = \tau^{-1}(f')$ satisfies $\pi_i \circ g' = \tau^{-1}(\sigma_i)$, so $g' = g$ and $f' = f$. The dual statement is the same argument in the opposite categories. $\square$

*Proof of the corollary.* By Section 1.3, $- \otimes_A N$ is left adjoint to $\operatorname{Hom}_A(N, -)$. So it preserves colimits, in particular cokernels. Let $M' \xrightarrow{f} M \xrightarrow{g} M'' \to 0$ be exact. Then $M''$ is the cokernel of $f$, so $M'' \otimes N$ is the cokernel of $f \otimes 1$, which is the exactness of $M' \otimes N \to M \otimes N \to M'' \otimes N \to 0$. The statement for $\operatorname{Hom}$ is the dual, with kernels. $\square$

*Proof that filtered colimits of modules are exact.* First a description of a filtered colimit $C = \operatorname{colim} D$ in $\mathsf{Mod}_A$. Let $\iota_i: D(i) \to C$ be the maps of the colimit. For a filtered $I$:

- (a) every element of $C$ is $\iota_i(x)$ for some $i$ and some $x \in D(i)$;
- (b) $\iota_i(x) = 0$ if and only if $D(u)(x) = 0$ for some $u: i \to k$.

To see this, let $C'$ be the set of pairs $(i, x)$ with $x \in D(i)$, modulo the relation $(i, x) \sim (j, y)$ if $D(u)(x) = D(v)(y)$ for some $u: i \to k$, $v: j \to k$. The relation is an equivalence relation: transitivity uses the two axioms of a filtered category to bring two stages to a common later stage and to make two parallel maps equal. Define $(i, x) + (j, y)$ as $(k, D(u)(x) + D(v)(y))$ for any $u: i \to k$, $v: j \to k$. By the same axioms this does not depend on the choices, and it makes $C'$ an $A$-module. The maps $x \mapsto [(i, x)]$ form a cocone, and a cocone $\kappa_i: D(i) \to T$ factors through $C'$ by $[(i, x)] \mapsto \kappa_i(x)$, uniquely since every element of $C'$ is a class $[(i, x)]$. So $C' = C$, and (a) and (b) hold by construction.

Now let $f: D' \to D$ and $g: D \to D''$ be maps of diagrams, with $D'(i) \to D(i) \to D''(i)$ exact for every $i$, and write $\bar f, \bar g$ for the maps of colimits. Then $\bar g \bar f = 0$, since $g_i f_i = 0$ for every $i$ and every element of $\operatorname{colim} D'$ comes from some stage. Let $z \in \operatorname{colim} D$ with $\bar g(z) = 0$. By (a), $z = \iota_i(x)$ with $x \in D(i)$. Then $\iota''_i(g_i(x)) = 0$, so by (b) there is $u: i \to k$ with $D''(u)(g_i(x)) = 0$. Since $g$ is natural, $g_k(D(u)(x)) = 0$. By exactness at stage $k$, $D(u)(x) = f_k(y)$ for some $y \in D'(k)$. Then $z = \iota_k(D(u)(x)) = \bar f(\iota'_k(y))$. So $\ker \bar g = \operatorname{im} \bar f$. For the last claim take $D' = 0$. $\square$

### Exercises

1. (A) Show that a limit of a diagram is unique up to a unique isomorphism that respects the cones, directly from the definition.
2. (A) Show that in $\mathsf{Top}$ the fibre product of $f: X \to Z$ and $g: Y \to Z$ is the subspace $\{(x, y) : f(x) = g(y)\}$ of $X \times Y$. Show that for $g$ the inclusion of a subspace, it is $f^{-1}(Y)$.
3. (A) Show that the forgetful functor $\mathsf{Mod}_A \to \mathsf{Set}$ preserves limits and does not preserve coproducts. Use Section 1.3 to explain both facts.
4. (B) Let $A$ be a ring, $f \in A$, and let $D: \mathbb{N} \to \mathsf{Mod}_A$ be the diagram $A \xrightarrow{f} A \xrightarrow{f} A \to \cdots$. Show that $\varinjlim D \cong A_f$. Generalize to $M_f$ for a module $M$.
5. (B) Show that for every $A$-module $M$, $M \cong \varinjlim M_\lambda$, the filtered colimit of its finitely generated submodules. Deduce from the theorem and Section 1.3 that $M \otimes_A N \cong \varinjlim M_\lambda \otimes_A N$, and that $N$ is flat if $- \otimes_A N$ is exact on finitely generated modules.
6. (B) Show that $\operatorname{Hom}_A(N, -)$ need not preserve filtered colimits. (Hint: take $N = \bigoplus_{n \geq 1} A$ and the colimit of the submodules $\bigoplus_{n \leq m} A$.) Show that it does when $N$ is finitely presented.
7. (B) A diagram $\cdots \to M_2 \to M_1$ of modules satisfies the *Mittag-Leffler condition* if all its maps are surjective. Show that then $\varprojlim$ is exact on short exact sequences $0 \to M'_n \to M_n \to M''_n \to 0$ of such diagrams.
8. (C) Let $I$ be filtered and $J$ finite. Show that for a functor $D: I \times J \to \mathsf{Set}$ the natural map $\operatorname{colim}_I \lim_J D \to \lim_J \operatorname{colim}_I D$ is a bijection. Explain why the theorem of this section is the case of a kernel.

### Lean

Mathlib has the general theory in `CategoryTheory.Limits`: cones `Cone`, the property `IsLimit`, the classes `HasLimits` and `HasColimits`, and the chosen objects `limit` and `colimit`. The construction from products and equalizers is `has_limits_of_hasEqualizers_and_products`. The preservation of limits by right adjoints is `Adjunction.rightAdjoint_preservesLimits`, and its dual is `Adjunction.leftAdjoint_preservesColimits`. Filtered categories are `CategoryTheory.IsFiltered`. The exactness of filtered colimits in $\mathsf{Mod}_A$ is the Grothendieck axiom `AB5`, with an instance for `ModuleCat R` in `Mathlib.Algebra.Category.ModuleCat.AB`. The commutation of filtered colimits with finite limits in sets is `colimitLimitToLimitColimit_isIso`. The handbook adds no `MinimalModel` node here.

### Notes and history

Inverse and direct limits of groups go back to the algebraic topology of the 1930s, in the Čech theory of homology. Kan defined limits and colimits in a general category in 1958, with adjoint functors. The axiom that filtered colimits are exact is Grothendieck's axiom AB5 from the Tohoku paper, which Chapter 2 meets again. Every statement here is classical.
