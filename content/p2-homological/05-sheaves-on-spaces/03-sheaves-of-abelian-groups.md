---
title: Sheaves of abelian groups and exactness
nodes: []
sources: [Har77, Vak25, Gro57]
reads_with: [Har77:ch2, Har77:ch3, Vak25:ch2]
requires: [P2.2, P2.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Sheaves of abelian groups and exactness

### Statement

Throughout, $X$ is a topological space and $\mathsf{Ab}(X)$ is the category of sheaves of abelian groups on $X$. It is additive: $\operatorname{Hom}(\mathcal{F}, \mathcal{G})$ is an abelian group under sectionwise addition, and $(\mathcal{F} \oplus \mathcal{G})(U) = \mathcal{F}(U) \oplus \mathcal{G}(U)$ is a sheaf and a biproduct.

**Definition P2.5.19 (kernel, image, cokernel).** Let $\varphi: \mathcal{F} \to \mathcal{G}$ be a morphism in $\mathsf{Ab}(X)$.

1. The *kernel* is the presheaf $(\ker \varphi)(U) = \ker(\varphi_U)$. It is a sheaf.
2. The *image* $\operatorname{im} \varphi$ is the sheafification of the presheaf $U \mapsto \operatorname{im}(\varphi_U)$.
3. The *cokernel* $\operatorname{coker} \varphi$ is the sheafification of the presheaf $U \mapsto \operatorname{coker}(\varphi_U)$.

A *subsheaf* of $\mathcal{G}$ is a sheaf $\mathcal{F}$ with $\mathcal{F}(U) \subseteq \mathcal{G}(U)$ for all $U$, compatibly with restriction. The image $\operatorname{im} \varphi$ is a subsheaf of $\mathcal{G}$: the presheaf image is a subpresheaf of the sheaf $\mathcal{G}$, and its sheafification consists of the sections of $\mathcal{G}$ that are locally in the presheaf image. For a subsheaf $\mathcal{F} \subseteq \mathcal{G}$, the *quotient sheaf* $\mathcal{G}/\mathcal{F}$ is the cokernel of the inclusion.

**Theorem P2.5.20 ($\mathsf{Ab}(X)$ is abelian).** The category $\mathsf{Ab}(X)$ is abelian. The kernel and cokernel of the definition are the kernel and cokernel in $\mathsf{Ab}(X)$, and for every $x \in X$,
$$(\ker \varphi)_x = \ker(\varphi_x), \qquad (\operatorname{im} \varphi)_x = \operatorname{im}(\varphi_x), \qquad (\operatorname{coker} \varphi)_x = \operatorname{coker}(\varphi_x).$$

Lean: Mathlib `CategoryTheory.sheafIsAbelian`, with the instance for `TopCat.Sheaf`.

**Corollary P2.5.21 (exactness on stalks).** A sequence $\mathcal{F}' \xrightarrow{\alpha} \mathcal{F} \xrightarrow{\beta} \mathcal{F}''$ in $\mathsf{Ab}(X)$ is exact if and only if $\mathcal{F}'_x \to \mathcal{F}_x \to \mathcal{F}''_x$ is exact for every $x \in X$. In particular:

1. $\varphi$ is a monomorphism if and only if every $\varphi_U$ is injective, if and only if every $\varphi_x$ is injective;
2. $\varphi: \mathcal{F} \to \mathcal{G}$ is an epimorphism if and only if every $\varphi_x$ is surjective, if and only if $\varphi$ is *locally surjective*: for every $t \in \mathcal{G}(U)$ and $x \in U$ there are an open $V$ with $x \in V \subseteq U$ and $s \in \mathcal{F}(V)$ with $\varphi(s) = t|_V$.

Lean: Mathlib `TopCat.Sheaf.exact_iff_stalkFunctor_map_exact`, `TopCat.Presheaf.mono_of_stalk_mono` and `TopCat.Presheaf.locally_surjective_iff_surjective_on_stalks`.

**Proposition P2.5.22 (global sections are left exact).** For every open $U$, the functor $\Gamma(U, -): \mathsf{Ab}(X) \to \mathsf{Ab}$ is left exact. It is not exact in general.

Lean: not in Lean as stated.

**Theorem P2.5.23 (enough injectives).** The category $\mathsf{Ab}(X)$ has enough injectives. Explicitly, for each $x \in X$ choose a monomorphism $\mathcal{F}_x \to I_x$ into an injective abelian group. Then the induced morphism $\mathcal{F} \to \prod_{x \in X} x_* I_x$ into a product of skyscraper sheaves is a monomorphism, and $\prod_x x_* I_x$ is injective.

Lean: Mathlib `CategoryTheory.IsGrothendieckAbelian.enoughInjectives`, through the instance that sheaves form a Grothendieck abelian category; `stalkSkyscraperSheafAdjunction` is the adjunction used below.

So Section 3.2 applies: every left exact functor on $\mathsf{Ab}(X)$ has right derived functors. Chapter 7 defines sheaf cohomology as $H^i(X, -) = R^i \Gamma(X, -)$.

### Proof in words

Stalks are filtered colimits, and filtered colimits of abelian groups are exact. So taking stalks commutes with kernels and cokernels of presheaves, and sheafification does not change stalks. This computes the stalks of kernels, images and cokernels. The axioms that make a category abelian, that a monomorphism is the kernel of its cokernel and an epimorphism the cokernel of its kernel, then say that certain morphisms of sheaves are isomorphisms. This can be checked on stalks, where it is the first isomorphism theorem for abelian groups. Exactness on stalks follows in the same way.

Global sections keep kernels, because the kernel is computed sectionwise. They need not keep surjectivity: an epimorphism of sheaves is only locally surjective, and local preimages may fail to glue. The obstruction is a cohomology class, and Chapter 7 makes this precise. For injectives, a map into a skyscraper sheaf $x_* A$ is the same as a map of stalks into $A$. So an injective group at each point gives an injective skyscraper sheaf, and their product catches every germ.

### Examples

**Example P2.5.24 (the exponential sequence).** Let $X$ be a complex manifold, $\mathcal{O}_X$ the sheaf of holomorphic functions and $\mathcal{O}_X^\times$ the sheaf of nowhere zero holomorphic functions, under multiplication. The sequence
$$0 \to \underline{\mathbb{Z}} \xrightarrow{2 \pi i} \mathcal{O}_X \xrightarrow{\exp} \mathcal{O}_X^\times \to 0$$
is exact in $\mathsf{Ab}(X)$. On stalks: a germ $f$ with $\exp f = 1$ is locally constant with values in $2 \pi i \mathbb{Z}$, and every nowhere zero germ has a logarithm on a small ball. It is not exact on global sections for $X = \mathbb{C} \setminus \{0\}$, since $z$ has no logarithm there. Chapter 7 gives the long exact sequence of cohomology, with a map $H^1(X, \mathcal{O}_X^\times) \to H^2(X, \mathbb{Z})$. Since $H^1(X, \mathcal{O}_X^\times)$ is the group of line bundles, this map is the first Chern class. For $X$ smooth and projective its image is the Néron-Severi group $\operatorname{NS}(X)$, and $\operatorname{NS}(X) \otimes \mathbb{R}$ is the space $N^1(X)$ of divisors up to numerical equivalence in which the cone theorem is stated (Volume 7).

**Example P2.5.25 (restriction to a subvariety).** Let $X$ be a variety, $Z \subseteq X$ a closed subvariety and $i: Z \to X$ the inclusion. The ideal sheaf $\mathcal{I}_Z \subseteq \mathcal{O}_X$ of functions vanishing on $Z$ gives an exact sequence $0 \to \mathcal{I}_Z \to \mathcal{O}_X \to i_* \mathcal{O}_Z \to 0$. Exactness at the right is surjectivity on stalks, since every germ of a regular function on $Z$ is locally the restriction of a regular function on $X$ (P3). On global sections it can fail. For two distinct points $p, q \in \mathbb{P}^1$, $\Gamma(\mathbb{P}^1, \mathcal{O}) = k$ maps to $\Gamma(\{p, q\}, \mathcal{O}) = k^2$ diagonally, which is not onto. The failure is measured by $H^1(\mathbb{P}^1, \mathcal{I}_{\{p,q\}}) = H^1(\mathbb{P}^1, \mathcal{O}(-2)) \cong k$. In the base point free theorem (Volume 7) the same sequence, with $Z = S$ a divisor and twisted by $\mathcal{O}_X(mD)$, is used with a vanishing theorem to lift sections from $S$ to $X$.

**Example P2.5.26 (skyscraper sheaves are injective).** Let $x \in X$ and let $A$ be an injective abelian group, such as $\mathbb{Q}/\mathbb{Z}$. The proof below shows $\operatorname{Hom}(\mathcal{G}, x_* A) = \operatorname{Hom}(\mathcal{G}_x, A)$. Since $\mathcal{G} \mapsto \mathcal{G}_x$ is exact and $\operatorname{Hom}(-, A)$ is exact, $x_* A$ is an injective object of $\mathsf{Ab}(X)$. Its global sections are $A$. Since it is injective, it has no higher cohomology once Chapter 7 defines cohomology.

### Proof

*Proof of the theorem that $\mathsf{Ab}(X)$ is abelian.* The kernel presheaf is a sheaf. Locality holds because it holds in $\mathcal{F}$. For gluing, sections $s_i \in \ker(\varphi_{U_i})$ that agree on overlaps glue to $s \in \mathcal{F}(U)$, and $\varphi(s)$ restricts to $0$ on each $U_i$, so $\varphi(s) = 0$. A morphism $\psi: \mathcal{H} \to \mathcal{F}$ with $\varphi \psi = 0$ lands sectionwise in $\ker \varphi$. So $\ker \varphi$ is the kernel in $\mathsf{Ab}(X)$. For the cokernel, a morphism $\mathcal{G} \to \mathcal{H}$ to a sheaf that kills $\varphi$ factors uniquely through the presheaf cokernel, and then uniquely through its sheafification by the theorem of Section 5.2. So $\operatorname{coker} \varphi$ is the cokernel in $\mathsf{Ab}(X)$.

Stalks. Filtered colimits of abelian groups are exact (Section 1.4). So the stalk of the presheaf kernel, image or cokernel is the kernel, image or cokernel of $\varphi_x$. Sheafification does not change stalks (Section 5.2). This proves the three formulas.

It remains to check the two axioms of Definition P2.2.10. Let $\varphi: \mathcal{F} \to \mathcal{G}$ be a monomorphism. In an additive category a morphism is a monomorphism if and only if its kernel is $0$. So $\ker \varphi = 0$, and by the formulas every $\varphi_x$ is injective. The kernel of $\operatorname{coker} \varphi$ is a subsheaf $\mathcal{K} \subseteq \mathcal{G}$, and $\varphi$ factors through a morphism $\mathcal{F} \to \mathcal{K}$. By the formulas, $\mathcal{K}_x = \ker(\mathcal{G}_x \to \mathcal{G}_x / \varphi_x(\mathcal{F}_x)) = \varphi_x(\mathcal{F}_x)$, so $\mathcal{F}_x \to \mathcal{K}_x$ is bijective. A morphism of sheaves that is bijective on stalks is an isomorphism (Section 5.1). So $\varphi$ is the kernel of its cokernel. Dually, let $\varphi$ be an epimorphism. Then $\operatorname{coker} \varphi = 0$, so every $\varphi_x$ is surjective. The morphism $\operatorname{coker}(\ker \varphi) \to \mathcal{G}$ induced by $\varphi$ has stalk $\mathcal{F}_x / \ker \varphi_x \to \mathcal{G}_x$ at $x$, which is bijective by the first isomorphism theorem. So it is an isomorphism, and $\varphi$ is the cokernel of its kernel. $\square$

*Proof of the corollary.* Exactness at $\mathcal{F}$ means that $\beta \alpha = 0$ and that the morphism $\operatorname{im} \alpha \to \ker \beta$ is an isomorphism. By the theorem both conditions can be checked on stalks: $\beta \alpha = 0$ if and only if its stalks vanish, by part 3 of the theorem of Section 5.1, and the stalks of $\operatorname{im} \alpha$ and $\ker \beta$ are $\operatorname{im} \alpha_x$ and $\ker \beta_x$.

Part 1. $\varphi$ is a monomorphism if and only if $\ker \varphi = 0$. Since the kernel is computed sectionwise, this says that each $\varphi_U$ is injective. Since the stalk of the kernel is the kernel of $\varphi_x$, and a sheaf with zero stalks is zero, it also says that each $\varphi_x$ is injective.

Part 2. $\varphi$ is an epimorphism if and only if $\operatorname{coker} \varphi = 0$, if and only if each $\operatorname{coker} \varphi_x = 0$. If each $\varphi_x$ is surjective, let $t \in \mathcal{G}(U)$ and $x \in U$. Then $t_x = \varphi_x(\sigma)$ for a germ $\sigma$ represented by $s \in \mathcal{F}(V)$, and after shrinking $V$, $\varphi(s) = t|_V$. Conversely, local surjectivity gives surjectivity on stalks, since every germ of $\mathcal{G}$ at $x$ is the germ of some $t \in \mathcal{G}(U)$. $\square$

*Proof of the proposition.* Let $0 \to \mathcal{F}' \xrightarrow{\alpha} \mathcal{F} \xrightarrow{\beta} \mathcal{F}''$ be exact. Then $\mathcal{F}' = \ker \beta$, and the kernel is computed sectionwise. So $0 \to \mathcal{F}'(U) \to \mathcal{F}(U) \to \mathcal{F}''(U)$ is exact. The example of the exponential sequence shows that $\Gamma(U, -)$ need not keep epimorphisms. $\square$

*Proof of the theorem on enough injectives.* First, for every sheaf $\mathcal{G}$ and abelian group $A$ there is a natural bijection $\operatorname{Hom}(\mathcal{G}, x_* A) \cong \operatorname{Hom}(\mathcal{G}_x, A)$. A morphism $\mathcal{G} \to x_* A$ is a family of homomorphisms $\mathcal{G}(U) \to A$, for the open sets $U$ that contain $x$, compatible with restriction, because $x_* A(U) = 0$ when $x \notin U$. Such a family is the same as a homomorphism from the colimit $\mathcal{G}_x$ to $A$.

Next, the product $\prod_x x_* I_x$, taken sectionwise, is a product in $\mathsf{Ab}(X)$, and
$$\operatorname{Hom}\Big(\mathcal{G}, \prod_x x_* I_x\Big) \cong \prod_x \operatorname{Hom}(\mathcal{G}, x_* I_x) \cong \prod_x \operatorname{Hom}(\mathcal{G}_x, I_x).$$
The functor $\mathcal{G} \mapsto \mathcal{G}_x$ is exact by the corollary, $\operatorname{Hom}(-, I_x)$ is exact since $I_x$ is injective, and a product of exact sequences of abelian groups is exact. So $\operatorname{Hom}(-, \prod_x x_* I_x)$ is exact, and the product is injective.

Finally, the morphism $\mathcal{F} \to \prod_x x_* I_x$ that corresponds to the family of maps $\mathcal{F}_x \to I_x$ sends $s \in \mathcal{F}(U)$ to the family of images of the germs $s_x$ in $I_x$, for $x \in U$. If this family is $0$, every germ $s_x$ is $0$, since $\mathcal{F}_x \to I_x$ is injective, and so $s = 0$ by Section 5.1. So the morphism is injective on sections, hence a monomorphism. Every abelian group embeds in an injective one (Section 2.4), so the theorem follows. $\square$

### Exercises

1. (A) Show that a morphism $\varphi$ in $\mathsf{Ab}(X)$ is an isomorphism if and only if it is a monomorphism and an epimorphism, using stalks.
2. (A) Show that if $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ is exact in $\mathsf{Ab}(X)$ and $U$ is open, then $0 \to \mathcal{F}'|_U \to \mathcal{F}|_U \to \mathcal{F}''|_U \to 0$ is exact in $\mathsf{Ab}(U)$.
3. (A) Show that a sequence of sheaves that is exact on sections over every open set is exact. Give an example showing that the converse fails.
4. (B) For an open $U \subseteq X$, let $\mathbb{Z}_U$ be the sheafification of the presheaf that is $\mathbb{Z}$ on open sets contained in $U$ and $0$ on the others. Show that $\operatorname{Hom}(\mathbb{Z}_U, \mathcal{F}) \cong \mathcal{F}(U)$. Deduce that the sheaves $\mathbb{Z}_U$ form a set of generators of $\mathsf{Ab}(X)$, and that $\mathsf{Ab}(X)$ is a Grothendieck abelian category, so that the theorem of Section 2.2 gives a second proof of enough injectives.
5. (B) On $X = \mathbb{C} \setminus \{0\}$, compute the cokernel of $\Gamma(X, \mathcal{O}) \xrightarrow{\exp} \Gamma(X, \mathcal{O}^\times)$ and show that it is isomorphic to $\mathbb{Z}$, through the winding number $\frac{1}{2 \pi i} \oint f'/f \, dz$ around $0$.
6. (B) Show that the direct sum of a family of sheaves in $\mathsf{Ab}(X)$ is the sheafification of the sectionwise direct sum, and that the sectionwise direct sum is already a sheaf if the family is finite or if $X$ is a noetherian space.
7. (C) A sheaf $\mathcal{F}$ is *flasque* if every restriction map $\mathcal{F}(U) \to \mathcal{F}(V)$ is surjective. Let $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ be exact with $\mathcal{F}'$ flasque. Show that $\mathcal{F}(U) \to \mathcal{F}''(U)$ is surjective for every $U$. (Hint: apply Zorn's lemma to the pairs $(V, s)$ with $V \subseteq U$ open and $s \in \mathcal{F}(V)$ a preimage of the restriction of the given section.)

### Lean

Mathlib proves that sheaves with values in an abelian category, on any site, form an abelian category (`CategoryTheory.sheafIsAbelian`), and that sheaves on a space form a Grothendieck abelian category when the values do, so that `CategoryTheory.IsGrothendieckAbelian.enoughInjectives` applies. Exactness on stalks is `TopCat.Sheaf.exact_iff_stalkFunctor_map_exact`, and the characterization of epimorphisms by stalks is `TopCat.Presheaf.locally_surjective_iff_surjective_on_stalks`. Flasque sheaves are `TopCat.Presheaf.IsFlasque`, and Exercise 7 is `TopCat.Sheaf.IsFlasque.epi_of_shortExact`. The explicit embedding into a product of skyscraper sheaves is not stated in this form. The handbook adds no `MinimalModel` node here.

### Notes and history

The category of sheaves of abelian groups was the first example, after modules, of an abelian category with enough injectives. Grothendieck proved enough injectives in the Tohoku paper of 1957 from his axioms AB5 and the existence of a generator, as in Exercise 4. The explicit embedding into skyscraper sheaves is Godement's. The exponential sequence and its connecting map to $H^2(X, \mathbb{Z})$ go back to Kodaira and Spencer's work on the first Chern class of line bundles in the early 1950s.
