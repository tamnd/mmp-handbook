---
title: Categories and functors
nodes: []
sources: [Vak25, Mac98]
reads_with: [Vak25:ch1, Mac98:ch1]
requires: [P1.1]
level: prereq
kind: background
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Categories and functors

### Statement

**Definition P2.1.1 (category).** A *category* $\mathcal{C}$ consists of the following data.

- A collection $\operatorname{Ob}(\mathcal{C})$ of *objects*.
- For each pair of objects $A, B$, a set $\operatorname{Hom}_{\mathcal{C}}(A, B)$ of *morphisms* (or *maps*, or *arrows*) from $A$ to $B$. A morphism $f \in \operatorname{Hom}(A, B)$ is written $f: A \to B$.
- For each triple $A, B, C$, a *composition* $\operatorname{Hom}(B, C) \times \operatorname{Hom}(A, B) \to \operatorname{Hom}(A, C)$, $(g, f) \mapsto g \circ f$.
- For each object $A$, an *identity* $1_A \in \operatorname{Hom}(A, A)$.

The composition is associative, $h \circ (g \circ f) = (h \circ g) \circ f$, and the identities are units, $f \circ 1_A = f = 1_B \circ f$ for $f: A \to B$. The category is *small* if its objects form a set.

Lean: Mathlib `CategoryTheory.Category` (a class on a type of objects, with a type of morphisms for each pair; the size is controlled by universe levels).

**Example P2.1.2 (categories of sets and of algebraic objects).** The category $\mathsf{Set}$ has sets as objects and maps of sets as morphisms. The category $\mathsf{Grp}$ has groups and group homomorphisms, $\mathsf{Ab}$ has abelian groups, and $\mathsf{Ring}$ has commutative rings with $1$ and ring homomorphisms. For a ring $A$, the category $\mathsf{Mod}_A$ has $A$-modules and $A$-linear maps, as in P1 Ch. 1. The category $\mathsf{Top}$ has topological spaces and continuous maps. In each case composition is composition of maps.

**Example P2.1.3 (categories that are not categories of maps).** A partially ordered set $(P, \leq)$ is a category with one morphism $a \to b$ when $a \leq b$ and none otherwise. Transitivity gives the composition and reflexivity gives the identities. The main case in this volume is the set $\operatorname{Op}(X)$ of open subsets of a space $X$, ordered by inclusion: there is one map $U \to V$ when $U \subseteq V$. A group $G$ is a category with one object $*$ and $\operatorname{Hom}(*, *) = G$, with the group law as composition.

**Definition P2.1.4 (isomorphism, monomorphism, epimorphism).** A morphism $f: A \to B$ is an *isomorphism* if there is $g: B \to A$ with $g \circ f = 1_A$ and $f \circ g = 1_B$. Then $g$ is unique, and it is written $f^{-1}$. The morphism $f$ is a *monomorphism* if $f \circ u = f \circ v$ implies $u = v$ for all $u, v: T \to A$, and an *epimorphism* if $u \circ f = v \circ f$ implies $u = v$ for all $u, v: B \to T$.

Lean: Mathlib `CategoryTheory.Iso`, `CategoryTheory.IsIso`, `CategoryTheory.Mono` and `CategoryTheory.Epi`.

The inverse is unique because $g = g \circ (f \circ g') = (g \circ f) \circ g' = g'$ for two inverses $g, g'$.

**Example P2.1.5.** In $\mathsf{Set}$, $\mathsf{Grp}$ and $\mathsf{Mod}_A$ the monomorphisms are the injective maps. For $\mathsf{Mod}_A$: if $f$ is injective then $f u = f v$ gives $u = v$; if $f$ is not injective, take $T = \ker f$, $u$ the inclusion and $v = 0$. In $\mathsf{Set}$ and $\mathsf{Mod}_A$ the epimorphisms are the surjective maps: for $\mathsf{Mod}_A$, if $f$ is not onto, the projection $B \to B/f(A)$ and the zero map agree after $f$ but differ.

**Example P2.1.6 (an epimorphism that is not surjective).** In $\mathsf{Ring}$ the inclusion $\mathbb{Z} \to \mathbb{Q}$ is an epimorphism. Two ring maps $u, v: \mathbb{Q} \to T$ that agree on $\mathbb{Z}$ agree on $1/n$, since $u(1/n)$ is the inverse of $u(n) = v(n)$ in $T$. So $u = v$. The map is not onto, and it is not an isomorphism. A morphism that is both a monomorphism and an epimorphism need not be an isomorphism. Chapter 2 shows that in an abelian category it must be.

**Definition P2.1.7 (opposite category).** The *opposite* $\mathcal{C}^{\mathrm{op}}$ of $\mathcal{C}$ has the same objects and $\operatorname{Hom}_{\mathcal{C}^{\mathrm{op}}}(A, B) = \operatorname{Hom}_{\mathcal{C}}(B, A)$, with the composition reversed.

Lean: Mathlib `CategoryTheory.Opposite` (written `Cᵒᵖ`).

Every notion has a dual, obtained by passing to $\mathcal{C}^{\mathrm{op}}$. A monomorphism of $\mathcal{C}^{\mathrm{op}}$ is an epimorphism of $\mathcal{C}$. A theorem proved for all categories gives its dual for free.

**Definition P2.1.8 (functor).** A (covariant) *functor* $F: \mathcal{C} \to \mathcal{D}$ sends each object $A$ of $\mathcal{C}$ to an object $F(A)$ of $\mathcal{D}$ and each morphism $f: A \to B$ to a morphism $F(f): F(A) \to F(B)$, so that $F(1_A) = 1_{F(A)}$ and $F(g \circ f) = F(g) \circ F(f)$. A *contravariant* functor from $\mathcal{C}$ to $\mathcal{D}$ is a functor $\mathcal{C}^{\mathrm{op}} \to \mathcal{D}$: it reverses the direction of morphisms. Functors compose, and the identity functor $1_{\mathcal{C}}$ is a unit for the composition.

Lean: Mathlib `CategoryTheory.Functor` (written `C ⥤ D`).

A functor sends an isomorphism to an isomorphism, with $F(f)^{-1} = F(f^{-1})$. So two objects whose images under some functor are not isomorphic are not isomorphic. This is the basic use of the functors of algebraic topology and of the cohomology functors of Chapter 7.

**Example P2.1.9 (forgetful and free functors).** The *forgetful functor* $\mathsf{Mod}_A \to \mathsf{Set}$ sends a module to its underlying set. The *free functor* $\mathsf{Set} \to \mathsf{Mod}_A$ sends a set $S$ to the free module $A^{(S)} = \bigoplus_{s \in S} A$ and a map $S \to S'$ to the linear map that sends the basis vector $e_s$ to $e_{f(s)}$. A ring map $A \to B$ gives *restriction of scalars* $\mathsf{Mod}_B \to \mathsf{Mod}_A$ and *extension of scalars* $M \mapsto B \otimes_A M$, from $\mathsf{Mod}_A$ to $\mathsf{Mod}_B$.

**Example P2.1.10 (Hom functors).** For an object $T$ of $\mathcal{C}$ there is a covariant functor $h^T = \operatorname{Hom}(T, -): \mathcal{C} \to \mathsf{Set}$ that sends $f: A \to B$ to $f \circ -: \operatorname{Hom}(T, A) \to \operatorname{Hom}(T, B)$, and a contravariant functor $h_T = \operatorname{Hom}(-, T): \mathcal{C}^{\mathrm{op}} \to \mathsf{Set}$ that sends $f$ to $- \circ f$. On $\mathsf{Mod}_A$ both take values in $\mathsf{Mod}_A$. For a module $N$ the functor $- \otimes_A N: \mathsf{Mod}_A \to \mathsf{Mod}_A$ is covariant.

**Example P2.1.11 (the spectrum and the open sets).** The prime spectrum of P1 Ch. 2 is a contravariant functor $\operatorname{Spec}: \mathsf{Ring}^{\mathrm{op}} \to \mathsf{Top}$. A ring map $\varphi: A \to B$ gives the continuous map $\operatorname{Spec} B \to \operatorname{Spec} A$, $\mathfrak{q} \mapsto \varphi^{-1}(\mathfrak{q})$. A continuous map $f: X \to Y$ gives a functor $f^{-1}: \operatorname{Op}(Y) \to \operatorname{Op}(X)$, $V \mapsto f^{-1}(V)$, since $V \subseteq V'$ implies $f^{-1}(V) \subseteq f^{-1}(V')$. A *presheaf* of abelian groups on $X$ is a functor $\operatorname{Op}(X)^{\mathrm{op}} \to \mathsf{Ab}$ (Chapter 5).

**Definition P2.1.12 (faithful, full, essentially surjective).** A functor $F: \mathcal{C} \to \mathcal{D}$ is *faithful* if each map $\operatorname{Hom}(A, B) \to \operatorname{Hom}(F(A), F(B))$ is injective, *full* if each is surjective, and *fully faithful* if each is bijective. It is *essentially surjective* if every object of $\mathcal{D}$ is isomorphic to $F(A)$ for some $A$. A *subcategory* $\mathcal{C}' \subseteq \mathcal{C}$ is *full* if the inclusion is full.

Lean: Mathlib `CategoryTheory.Functor.Faithful`, `CategoryTheory.Functor.Full`, `CategoryTheory.Functor.FullyFaithful` and `CategoryTheory.Functor.EssSurj`.

**Proposition P2.1.13 (fully faithful functors reflect isomorphisms).** Let $F$ be fully faithful. Then $f: A \to B$ is an isomorphism if and only if $F(f)$ is one.

Lean: Mathlib `CategoryTheory.Functor.FullyFaithful.isIso_of_isIso_map` (proved in Mathlib).

*Proof.* If $F(f)$ has an inverse $g'$, then $g' = F(g)$ for a unique $g: B \to A$, since $F$ is full. Now $F(g \circ f) = g' \circ F(f) = 1_{F(A)} = F(1_A)$, and faithfulness gives $g \circ f = 1_A$. In the same way $f \circ g = 1_B$. The converse holds for every functor. $\square$

### Examples

**Example P2.1.14 (a forgetful functor is faithful, not full).** The forgetful functor $\mathsf{Mod}_A \to \mathsf{Set}$ is faithful, since a linear map is determined by its values. It is not full, since most maps of sets between modules are not linear. The forgetful functor $\mathsf{Ab} \to \mathsf{Grp}$ is fully faithful: a group homomorphism between abelian groups is a morphism of $\mathsf{Ab}$. It is not essentially surjective.

**Example P2.1.15 (matrices).** Let $k$ be a field. The category $\mathsf{Mat}_k$ has the natural numbers as objects, and $\operatorname{Hom}(m, n)$ is the set of $n \times m$ matrices, with matrix product as composition. The functor $\mathsf{Mat}_k \to \mathsf{Vect}_k^{\mathrm{fd}}$, $n \mapsto k^n$, to finite dimensional vector spaces is fully faithful, since a linear map $k^m \to k^n$ is a matrix. It is essentially surjective, since every finite dimensional space has a basis. Section 1.2 shows that such a functor is an equivalence. The two categories have very different sizes, but they carry the same linear algebra.

**Example P2.1.16 (a functor that is not faithful).** The functor $\mathsf{Mod}_A \to \mathsf{Mod}_A$, $M \mapsto M \otimes_A A/I$, kills the map $M \to M$ given by multiplication by $a \in I$. So it is not faithful unless $I = 0$.

### Exercises

1. (A) Show that a composition of monomorphisms is a monomorphism, and that if $g \circ f$ is a monomorphism then $f$ is a monomorphism. State and prove the dual statements.
2. (A) Show that a functor between two posets, seen as categories, is the same as a map that preserves the order. Which such functors are fully faithful?
3. (A) Show that in $\mathsf{Grp}$ a morphism is a monomorphism if and only if it is injective. (Hint: use $T = \mathbb{Z}$.)
4. (B) Show that for every multiplicative set $S$ of a ring $A$, the map $A \to S^{-1}A$ is an epimorphism in $\mathsf{Ring}$. Deduce that the epimorphisms of $\mathsf{Ring}$ need not be surjective even for Noetherian rings.
5. (B) Show that the inclusion $\mathbb{Q} \to \mathbb{R}$ is a monomorphism and an epimorphism in the category of Hausdorff spaces, and that it is not an isomorphism.
6. (B) Let $k$ be a field. Show that $V \mapsto V^{**}$ is a covariant functor on $\mathsf{Vect}_k$, and that $V \mapsto V^*$ is a contravariant functor. Show that the second is faithful.

### Lean

Mathlib builds category theory on `CategoryTheory.Category`, with objects a type and morphisms a family of types. The opposite category is `Cᵒᵖ`, built on `Opposite`. Functors are `CategoryTheory.Functor`, and the properties of this section are the classes `Functor.Faithful`, `Functor.Full` and `Functor.EssSurj`, with the structure `Functor.FullyFaithful` for the data of the inverse maps. The categories of the examples are `ModuleCat R`, `AddCommGrpCat`, `TopCat` and `TopologicalSpace.Opens X`. The handbook adds no `MinimalModel` node here.

### Notes and history

Eilenberg and Mac Lane introduced categories, functors and natural transformations in 1945, to make precise the word "natural" in algebraic topology. Grothendieck made categories the working language of algebraic geometry, in the Tohoku paper of 1957 and in EGA. Mac Lane's book is the standard reference for the general theory, and Vakil, Chapter 1, gives the part that algebraic geometry needs. Every statement in this section is classical.
