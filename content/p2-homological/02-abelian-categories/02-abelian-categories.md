---
title: Abelian categories and exact sequences
nodes: []
sources: [Wei94, Vak25, Mac98, Fre64, Gro57]
reads_with: [Wei94:ch1, Wei94:appA, Vak25:ch1, Mac98:ch8]
requires: [P1.1, P1.3, P2.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Abelian categories and exact sequences

### Statement

**Definition P2.2.10 (abelian category).** An additive category $\mathcal{A}$ is *abelian* if every map has a kernel and a cokernel, every monomorphism is the kernel of its cokernel, and every epimorphism is the cokernel of its kernel.

Lean: Mathlib `CategoryTheory.Abelian` (an extension of `Preadditive` with normal monomorphisms and normal epimorphisms, finite products and finite coproducts, kernels and cokernels).

**Definition P2.2.11 (image and coimage).** Let $f: A \to B$ in an abelian category. The *image* of $f$ is $\operatorname{im} f = \ker(\operatorname{coker} f)$, a subobject of $B$. The *coimage* is $\operatorname{coim} f = \operatorname{coker}(\ker f)$, a quotient of $A$. Since $f \circ \ker f = 0$, the map $f$ factors through $A \to \operatorname{coim} f$. Since $\operatorname{coker} f \circ f = 0$, it factors through $\operatorname{im} f \to B$. So there is a unique map $\operatorname{coim} f \to \operatorname{im} f$ through which $f$ factors.

Lean: Mathlib `CategoryTheory.Abelian.image`, `CategoryTheory.Abelian.coimage` and `CategoryTheory.Abelian.coimageImageComparison`.

**Theorem P2.2.12 (the structure of maps in an abelian category).** Let $\mathcal{A}$ be abelian.

1. A map that is both a monomorphism and an epimorphism is an isomorphism.
2. Every map $f: A \to B$ factors as $f = m \circ e$ with $e$ an epimorphism and $m$ a monomorphism. Here $e$ is the map $A \to \operatorname{coim} f$ and $m$ is the map $\operatorname{im} f \to B$.
3. The canonical map $\operatorname{coim} f \to \operatorname{im} f$ is an isomorphism.

Lean: Mathlib `CategoryTheory.isIso_of_mono_of_epi` (abelian categories are balanced) and the instance `IsIso (Abelian.coimageImageComparison f)` (proved in Mathlib).

**Definition P2.2.13 (exact sequence).** In an abelian category, a sequence $A \xrightarrow{f} B \xrightarrow{g} C$ with $g f = 0$ is *exact at $B$* if the map $\operatorname{im} f \to \ker g$ induced by $g f = 0$ is an isomorphism. A *short exact sequence* is a sequence $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$ that is exact at $A$, $B$ and $C$: $f$ is a monomorphism, $g$ is an epimorphism and $f$ is a kernel of $g$.

Lean: Mathlib `CategoryTheory.ShortComplex.Exact` and `CategoryTheory.ShortComplex.ShortExact`.

**Proposition P2.2.14 (functor categories).** Let $\mathcal{C}$ be small and $\mathcal{A}$ abelian. The category $\operatorname{Fun}(\mathcal{C}, \mathcal{A})$ is abelian, with kernels, cokernels and sums computed object by object. A sequence of functors is exact if and only if it is exact at each object of $\mathcal{C}$. In particular the presheaves of abelian groups on a space $X$, the functors $\operatorname{Op}(X)^{\mathrm{op}} \to \mathsf{Ab}$, form an abelian category.

Lean: Mathlib `CategoryTheory.Abelian.functorCategoryAbelian` (proved in Mathlib).

*Proof.* For $\eta: F \Rightarrow G$, put $K(c) = \ker(\eta_c)$. A map $u: c \to c'$ gives $F(u)$, which sends $\ker \eta_c$ into $\ker \eta_{c'}$ by naturality, so $K$ is a functor and $K \to F$ is natural. It is a kernel of $\eta$, since a natural transformation $\theta: T \Rightarrow F$ with $\eta \theta = 0$ factors through $K$ at each $c$ uniquely, and the factorizations are natural by uniqueness. Cokernels are the same. A natural transformation is a monomorphism or an epimorphism if and only if each component is, by the same object by object description. So every axiom of an abelian category holds because it holds in $\mathcal{A}$ at each $c$. $\square$

**Theorem P2.2.15 (Freyd-Mitchell embedding).** Let $\mathcal{A}$ be a small abelian category. There is a ring $R$ and a functor $\mathcal{A} \to \mathsf{Mod}_R$ that is fully faithful and exact: it sends exact sequences to exact sequences. Also, every set of objects and maps of an abelian category lies in a small full abelian subcategory whose kernels, cokernels and biproducts are those of the large category.

Lean: Mathlib `CategoryTheory.Abelian.FreydMitchell.freyd_mitchell` (proved in Mathlib, for a ring in a suitable universe).

The proof of the embedding theorem is long and is not given here; see Freyd, Chapter 7, Mitchell's book *Theory of categories*, or Weibel, Section 1.6. The handbook does not use the theorem in an essential way. It uses it as a licence: a statement about a finite diagram in an abelian category, in terms of exactness and commutativity, holds if it holds for modules. Section 2.3 gives both kinds of proof of the snake lemma.

**Definition P2.2.16 (Grothendieck's axioms).** An abelian category satisfies *AB3* if it has all small coproducts, *AB4* if it also satisfies AB3 and a coproduct of short exact sequences is short exact, and *AB5* if it has all small colimits and filtered colimits are exact. A *generator* is an object $G$ such that $\operatorname{Hom}(G, -)$ is faithful. A *Grothendieck abelian category* is an abelian category that satisfies AB5 and has a generator.

Lean: Mathlib `CategoryTheory.AB4`, `CategoryTheory.AB5` and `CategoryTheory.IsGrothendieckAbelian`.

**Theorem P2.2.17 (Grothendieck).** A Grothendieck abelian category has enough injectives: every object is a subobject of an injective object (Section 2.4).

Lean: Mathlib `CategoryTheory.IsGrothendieckAbelian.enoughInjectives` (proved in Mathlib).

The proof is in the Tohoku paper, Section 1.10; see also the Stacks project. Section 2.4 proves the case of $\mathsf{Mod}_A$ in full, and Chapter 7 proves the case of sheaves directly from it. So the handbook does not need the general theorem.

### Proof in words

In a category of modules, the coimage $A/\ker f$ and the image $f(A)$ are isomorphic by the first isomorphism theorem. In a general additive category with kernels and cokernels they need not be, and the axioms of an abelian category are what make them agree. The key step is that the map $\operatorname{coim} f \to B$ is a monomorphism. This uses that every epimorphism is a cokernel. After it, the statement that a monomorphism and an epimorphism is an isomorphism is a formal consequence: a monomorphism is the kernel of its cokernel, and the cokernel of an epimorphism is zero.

### Examples

**Example P2.2.18 (modules and finitely generated modules).** The category $\mathsf{Mod}_A$ is abelian. A monomorphism $f: M \to N$ is injective, and it is the kernel of $N \to N/f(M)$. An epimorphism is surjective, and it is the cokernel of its kernel by the first isomorphism theorem. If $A$ is Noetherian, the full subcategory of finitely generated modules is abelian: a submodule of a finitely generated module is finitely generated (P1 Ch. 3), so kernels stay in the subcategory, and quotients are clear. The coherent sheaves on a Noetherian scheme, in P3 Ch. 5, form an abelian category for the same reason, and the vanishing theorems of the minimal model program are statements about objects of this category.

**Example P2.2.19 (a category that is additive but not abelian).** Let $\mathcal{F}$ be the category of finitely generated free abelian groups. By Section 2.1, every map in $\mathcal{F}$ has a kernel and a cokernel, and the map $f = 2: \mathbb{Z} \to \mathbb{Z}$ has kernel $0$ and cokernel $0$ in $\mathcal{F}$. So $f$ is a monomorphism and an epimorphism of $\mathcal{F}$, and it is not an isomorphism. Part 1 of the theorem fails, so $\mathcal{F}$ is not abelian. The axiom that fails is that $f$ is the kernel of its cokernel: the kernel of $\mathbb{Z} \to 0$ is $1_{\mathbb{Z}}$, not $f$.

**Example P2.2.20 (filtered vector spaces).** A filtered vector space is a vector space $V$ with subspaces $\cdots \supseteq F^p V \supseteq F^{p+1} V \supseteq \cdots$, and a map is a linear map with $f(F^p V) \subseteq F^p W$. This category is additive and has kernels and cokernels. Let $V = k$ with $F^p V = k$ for $p \leq 0$ and $F^p V = 0$ for $p \geq 1$, and let $W = k$ with $F^p W = k$ for $p \leq 1$ and $F^p W = 0$ for $p \geq 2$. The identity of $k$ is a map $V \to W$, since $F^p V \subseteq F^p W$ for every $p$. Its kernel and its cokernel are $0$, so it is a monomorphism and an epimorphism. Its inverse does not respect the filtrations, since $F^1 W = k$ and $F^1 V = 0$. So it is not an isomorphism. So the category is not abelian. This is the reason that the Hodge filtration of P6 and the filtrations of Chapter 4 are studied through the associated graded objects $F^p V / F^{p+1} V$, which live in an abelian category.

**Example P2.2.21 (exact sequences of functors).** In the abelian category of presheaves on $X$, a sequence $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ is exact if and only if $0 \to \mathcal{F}'(U) \to \mathcal{F}(U) \to \mathcal{F}''(U) \to 0$ is exact for every open $U$. Chapter 5 shows that sheaves form an abelian category too, but with a different notion of exactness: a map of sheaves can be an epimorphism without being surjective on each open set. The gap between the two notions is measured by sheaf cohomology.

### Proof

*Proof of the theorem.* For 1, let $f: A \to B$ be a monomorphism and an epimorphism. Since $f$ is an epimorphism, its cokernel is $B \to 0$. Since $f$ is a monomorphism, it is a kernel of its cokernel, that is, of $B \to 0$. But $1_B$ is also a kernel of $B \to 0$. Two kernels differ by a unique isomorphism, so there is an isomorphism $u: A \to B$ with $1_B \circ u = f$. So $f = u$ is an isomorphism.

For 2, let $k: K \to A$ be the kernel of $f$ and $e: A \to I$ the cokernel of $k$, so $I = \operatorname{coim} f$. Since $f k = 0$, there is a unique $m: I \to B$ with $f = m e$. The map $e$ is an epimorphism, since it is a cokernel. It remains to show that $m$ is a monomorphism. Let $g: T \to I$ with $m g = 0$. Let $q: I \to Q$ be the cokernel of $g$. Since $m g = 0$, there is $m': Q \to B$ with $m = m' q$. The map $q e$ is a composite of epimorphisms, so it is an epimorphism, and by the axiom it is the cokernel of its kernel $k': K' \to A$. Now $f k' = m' q e k' = 0$, so $k'$ factors through $k = \ker f$, and then $e k' = 0$ since $e k = 0$. So $e$ factors through the cokernel $q e$ of $k'$: $e = s q e$ for some $s: Q \to I$. Since $e$ is an epimorphism, $s q = 1_I$. So $q$ is a monomorphism. As $q g = 0$, this gives $g = 0$. So $m$ is a monomorphism.

For 3, take the factorization $f = m e$ of 2. Since $e$ is an epimorphism, a map $c$ satisfies $c f = 0$ if and only if $c m = 0$. So $\operatorname{coker} f = \operatorname{coker} m$. Since $m$ is a monomorphism, it is the kernel of its cokernel, so $m$ is a kernel of $\operatorname{coker} f$. That is, $m: I \to B$ is the image of $f$, and the canonical map $\operatorname{coim} f = I \to \operatorname{im} f$ is the isomorphism between two kernels of $\operatorname{coker} f$. $\square$

### Exercises

1. (A) Show that in an abelian category a sequence $0 \to A \xrightarrow{f} B \xrightarrow{g} C$ is exact if and only if $f$ is a kernel of $g$, and that $A \xrightarrow{f} B \xrightarrow{g} C \to 0$ is exact if and only if $g$ is a cokernel of $f$.
2. (A) Show that the opposite of an abelian category is abelian. Deduce that the dual of every theorem about abelian categories holds.
3. (B) Show that the category of finite abelian groups is abelian, and that $G \mapsto \operatorname{Hom}(G, \mathbb{Q}/\mathbb{Z})$ is an equivalence from its opposite to itself.
4. (B) Show that the category of torsion free abelian groups is additive and has kernels and cokernels, and that it is not abelian.
5. (B) Let $A$ be a ring that is not Noetherian. Show that the category of finitely generated $A$-modules is not abelian. (Hint: take an ideal $I$ that is not finitely generated and the map $A \to A/I$.)
6. (B) Show that a short exact sequence $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$ in an abelian category is *split*, that is, isomorphic to $0 \to A \to A \oplus C \to C \to 0$, if and only if $g$ has a section $s$, $g s = 1_C$, and if and only if $f$ has a retraction $r$, $r f = 1_A$.
7. (B) Let $X = \mathbb{R}$ and let $f$ be the map $(x, v) \mapsto (x, xv)$ of the trivial real line bundle on $X$. Show that the kernel and the cokernel of $f$ in the category of vector bundles are $0$. Deduce that this category is not abelian.

### Lean

Mathlib defines `CategoryTheory.Abelian` with the axioms of this section and proves that the coimage and the image agree, in the form of the instance `IsIso (Abelian.coimageImageComparison f)`. The category `ModuleCat R` is abelian by the instance `ModuleCat.abelian`, and a functor category into an abelian category is abelian by `Abelian.functorCategoryAbelian`. Exactness is stated with short complexes: `ShortComplex.Exact` and `ShortComplex.ShortExact`. The Freyd-Mitchell theorem is `Abelian.FreydMitchell.freyd_mitchell`, a recent formalization. Grothendieck's axioms are `AB4` and `AB5`, and the existence of enough injectives in a Grothendieck abelian category is `IsGrothendieckAbelian.enoughInjectives`. The handbook adds no `MinimalModel` node here.

### Notes and history

Buchsbaum defined exact categories in 1955, and Grothendieck gave the axioms of an abelian category in the Tohoku paper of 1957, with the axioms AB1 to AB6 and the existence of injectives. His aim was to treat the cohomology of sheaves and the cohomology of modules by one theory. The embedding theorem is due to Freyd and to Mitchell, independently, in 1964; Lubkin had a weaker form in 1960. Every statement here is classical.
