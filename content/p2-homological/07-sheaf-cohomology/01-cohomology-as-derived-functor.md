---
title: Cohomology as a derived functor
nodes: []
sources: [Har77, God58, Stacks, Wei94]
reads_with: [Har77:ch3, Wei94:ch2]
requires: [P2.3, P2.5, P2.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Cohomology as a derived functor

### Statement

By Theorem P2.5.23 the category $\mathsf{Ab}(X)$ has enough injectives, and by Proposition P2.5.22 the functor $\Gamma(X, -)$ is left exact. So Section 3.2 gives right derived functors.

**Definition P2.7.1 (sheaf cohomology and higher direct images).** Let $X$ be a topological space and $\mathcal{F}$ a sheaf of abelian groups on $X$. The *cohomology groups* of $\mathcal{F}$ are
$$H^i(X, \mathcal{F}) = R^i \Gamma(X, -)(\mathcal{F}), \qquad i \geq 0,$$
computed in $\mathsf{Ab}(X)$. For an open $U \subseteq X$ put $H^i(U, \mathcal{F}) = H^i(U, \mathcal{F}|_U)$. For a continuous map $f: X \to Y$, the *higher direct images* $R^i f_* \mathcal{F}$ are the right derived functors of the left exact functor $f_*: \mathsf{Ab}(X) \to \mathsf{Ab}(Y)$.

Lean: Mathlib `CategoryTheory.Sheaf.H`, defined as $\operatorname{Ext}^n(\underline{\mathbb{Z}}, \mathcal{F})$ in the category of sheaves, and the functor `CategoryTheory.Sheaf.functorH`.

Since $\operatorname{Hom}(\underline{\mathbb{Z}}, \mathcal{F}) = \Gamma(X, \mathcal{F})$, the Mathlib definition as Ext from the constant sheaf agrees with the derived functor definition (Section 3.4 and Chapter 8). For a ringed space, the derived functors of $\Gamma(X, -)$ and $f_*$ on $\mathsf{Mod}(\mathcal{O}_X)$ exist by the next theorem. Section 7.2 proves that they agree with those computed in $\mathsf{Ab}(X)$, so the notation $H^i(X, \mathcal{F})$ is not ambiguous.

**Theorem P2.7.2 (enough injectives for modules).** Let $(X, \mathcal{O}_X)$ be a ringed space. For each $x \in X$ choose an injective $\mathcal{O}_{X,x}$-module $I_x$ and an injective map $\mathcal{F}_x \to I_x$. Then the induced map $\mathcal{F} \to \prod_{x \in X} x_* I_x$ is a monomorphism of $\mathcal{O}_X$-modules into an injective $\mathcal{O}_X$-module. So $\mathsf{Mod}(\mathcal{O}_X)$ has enough injectives.

Lean: for a scheme, Mathlib has the instance `IsGrothendieckAbelian` on `AlgebraicGeometry.Scheme.Modules`, and `CategoryTheory.IsGrothendieckAbelian.enoughInjectives` gives enough injectives; the explicit product of skyscrapers is not in Lean as stated.

**Theorem P2.7.3 (first properties).** Let $X$ be a space, or a ringed space, and $\mathcal{F}$ a sheaf in $\mathsf{Ab}(X)$, or in $\mathsf{Mod}(\mathcal{O}_X)$.

1. $H^0(X, \mathcal{F}) = \Gamma(X, \mathcal{F})$, and $H^i(X, \mathcal{I}) = 0$ for $i > 0$ if $\mathcal{I}$ is injective.
2. A short exact sequence $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ gives a long exact sequence, natural in the sequence,
$$0 \to H^0(X, \mathcal{F}') \to H^0(X, \mathcal{F}) \to H^0(X, \mathcal{F}'') \xrightarrow{\delta} H^1(X, \mathcal{F}') \to H^1(X, \mathcal{F}) \to \cdots.$$
The same holds for $R^i f_*$, with $R^0 f_* = f_*$.
3. For an open $U \subseteq X$, the restriction of an injective sheaf to $U$ is injective. So an injective resolution $\mathcal{F} \to \mathcal{I}^\bullet$ restricts to an injective resolution of $\mathcal{F}|_U$, and there are restriction maps $H^i(X, \mathcal{F}) \to H^i(U, \mathcal{F})$ that make $U \mapsto H^i(U, \mathcal{F})$ a presheaf.
4. $R^i f_* \mathcal{F}$ is the sheafification of the presheaf $V \mapsto H^i(f^{-1}(V), \mathcal{F})$ on $Y$.
5. Every class $\xi \in H^i(X, \mathcal{F})$ with $i > 0$ vanishes locally: every $x \in X$ has an open neighbourhood $U$ with $\xi|_U = 0$.

Lean: Mathlib `CategoryTheory.Sheaf.H.longSequence_exact`, with the connecting map `CategoryTheory.Sheaf.H.δ`, for part 2; parts 3 to 5 are not in Lean as stated.

**Proposition P2.7.4 (closed subspaces).** Let $i: Z \to X$ be the inclusion of a closed subset and $\mathcal{E}$ a sheaf on $Z$. Then $R^q i_* \mathcal{E} = 0$ for $q > 0$ and $H^n(X, i_* \mathcal{E}) \cong H^n(Z, \mathcal{E})$ for all $n$. The same holds for a closed subvariety $Z$ of a variety and an $\mathcal{O}_Z$-module $\mathcal{E}$.

Lean: not in Lean as stated.

### Proof in words

A map into a skyscraper sheaf $x_* M$ is the same as a map of stalks into $M$. So a product of skyscrapers of injective modules is injective, and it receives every sheaf with an injective map, since a sheaf is determined by its stalks. This gives enough injectives, and the long exact sequence is Theorem P2.3.15. Restriction to an open set has an exact left adjoint, extension by zero, so it keeps injectives. Then $H^i(f^{-1}(V), \mathcal{F})$ is the cohomology of the sections over $f^{-1}(V)$ of one injective resolution, and sheafifying the cohomology of sections gives the cohomology sheaves of $f_* \mathcal{I}^\bullet$. For local vanishing, embed $\mathcal{F}$ in an injective sheaf. A class of degree $1$ is a section of the quotient, which lifts locally, and higher degrees follow by dimension shifting.

### Examples

**Example P2.7.5 (spaces with exact global sections).** On a one point space, $\mathsf{Ab}(X) = \mathsf{Ab}$ and $\Gamma$ is the identity, so $H^i = 0$ for $i > 0$. On a discrete space, $\Gamma(X, \mathcal{F}) = \prod_x \mathcal{F}_x$, a product of stalks, which is exact. So again $H^i(X, \mathcal{F}) = 0$ for $i > 0$. On the space $X = \{a, b\}$ whose open sets are $\emptyset$, $\{a\}$ and $X$, the only open set containing $b$ is $X$, so $\Gamma(X, \mathcal{F}) = \mathcal{F}_b$, and $\Gamma$ is exact. This space is $\operatorname{Spec}$ of a discrete valuation ring (Exercise 6 of Section 6.1). Cohomology detects how far the space is from being covered by such simple pieces.

**Example P2.7.6 (the exponential sequence).** Let $X$ be a complex manifold. The exponential sequence $0 \to \underline{\mathbb{Z}} \to \mathcal{O}_X \to \mathcal{O}_X^\times \to 0$ of Example P2.5.24, with $\mathcal{O}_X \to \mathcal{O}_X^\times$ given by $f \mapsto \exp(2 \pi i f)$, gives the long exact sequence
$$0 \to H^0(X, \mathbb{Z}) \to H^0(X, \mathcal{O}_X) \to H^0(X, \mathcal{O}_X^\times) \to H^1(X, \mathbb{Z}) \to H^1(X, \mathcal{O}_X) \to H^1(X, \mathcal{O}_X^\times) \xrightarrow{c_1} H^2(X, \mathbb{Z}) \to H^2(X, \mathcal{O}_X).$$
For $X = \mathbb{C} \setminus \{0\}$, the cokernel of $H^0(\mathcal{O}_X) \to H^0(\mathcal{O}_X^\times)$ is $\mathbb{Z}$, generated by the class of $z$ (Exercise 5 of Section 5.3). By exactness it injects into $H^1(X, \mathbb{Z})$. So $H^1(X, \mathbb{Z}) \neq 0$: the obstruction to a logarithm of $z$ is a cohomology class. If $X$ is compact and connected, then $H^0(X, \mathcal{O}_X) = \mathbb{C}$, $H^0(X, \mathcal{O}_X^\times) = \mathbb{C}^\times$ and the map between them is onto. So $H^1(X, \mathbb{Z}) \to H^1(X, \mathcal{O}_X)$ is injective. Section 7.4 identifies $H^1(X, \mathcal{O}_X^\times)$ with $\operatorname{Pic}(X)$, and the map $c_1: \operatorname{Pic}(X) \to H^2(X, \mathbb{Z})$ is the first Chern class.

**Example P2.7.7 (two points on $\mathbb{P}^1$).** Let $Z = \{p, q\}$ be two distinct points of $\mathbb{P}^1$ over an algebraically closed field $k$, with ideal sheaf $\mathcal{I}$. The exact sequence $0 \to \mathcal{I} \to \mathcal{O} \to i_* \mathcal{O}_Z \to 0$ of Example P2.5.25 and Proposition P2.7.4 give
$$0 \to H^0(\mathcal{I}) \to H^0(\mathcal{O}) \to H^0(Z, \mathcal{O}_Z) \to H^1(\mathcal{I}) \to H^1(\mathcal{O}) \to H^1(Z, \mathcal{O}_Z).$$
Here $H^0(\mathcal{O}) = k$, $H^0(Z, \mathcal{O}_Z) = k^2$, and the map is the diagonal. Section 7.3 shows $H^1(\mathbb{P}^1, \mathcal{O}) = 0$. So $H^1(\mathbb{P}^1, \mathcal{I}) \cong k^2/k \cong k$. This is the value $H^1(\mathbb{P}^1, \mathcal{O}(-2)) \cong k$ quoted in Example P2.5.25, since $\mathcal{I} \cong \mathcal{O}(-2)$ (Example P2.7.31). The nonzero group is the reason that a function on $Z$ does not extend to $\mathbb{P}^1$. In the base point free theorem a vanishing theorem kills the analogous group, and then sections extend.

**Example P2.7.8 (an open immersion with higher direct images).** Let $X = \mathbb{C}$, $U = X \setminus \{0\}$ and $j: U \to X$ the inclusion. By part 4, the stalk of $R^1 j_* \underline{\mathbb{Z}}$ at $0$ is $\varinjlim_D H^1(D \setminus \{0\}, \mathbb{Z})$ over the open discs $D$ centred at $0$. On each punctured disc the argument of Example P2.7.6, with the winding number around $0$, gives an injection $\mathbb{Z} \to H^1(D \setminus \{0\}, \mathbb{Z})$ that sends $1$ to the class of the obstruction to a logarithm of $z$, compatibly with restriction to smaller discs. So $(R^1 j_* \underline{\mathbb{Z}})_0 \neq 0$, while $j_*$ itself sees only sections. At points $x \neq 0$ the stalk is $0$ by part 5, since small discs around $x$ lie in $U$.

### Proof

*Theorem P2.7.2.* Let $M$ be an $\mathcal{O}_{X,x}$-module. The skyscraper $x_* M$ is an $\mathcal{O}_X$-module (Example P2.6.8). For an $\mathcal{O}_X$-module $\mathcal{G}$, a linear map $\varphi: \mathcal{G} \to x_* M$ gives a linear map $\varphi_x$ from $\mathcal{G}_x$ to $(x_* M)_x \to M$, where the second map sends the germ of a section over $U \ni x$ to its value in $M$. Conversely, a linear map $\psi: \mathcal{G}_x \to M$ gives $\mathcal{G}(U) \to M$, $s \mapsto \psi(s_x)$, for $U \ni x$, which is linear over $\mathcal{O}_X(U)$ and commutes with restriction. These constructions are inverse, as in the proof of Theorem P2.5.23, so
$$\operatorname{Hom}_{\mathcal{O}_X}(\mathcal{G}, x_* M) \cong \operatorname{Hom}_{\mathcal{O}_{X,x}}(\mathcal{G}_x, M).$$
If $M = I_x$ is injective, the right side is an exact functor of $\mathcal{G}$, because taking stalks is exact (part 3 of Theorem P2.6.3). So $x_* I_x$ is injective in $\mathsf{Mod}(\mathcal{O}_X)$. A product of injective objects is injective, since $\operatorname{Hom}(-, \prod_x J_x) = \prod_x \operatorname{Hom}(-, J_x)$ and a product of exact sequences of abelian groups is exact. The category of $\mathcal{O}_{X,x}$-modules has enough injectives (Theorem P2.2.35), so the maps $\mathcal{F}_x \to I_x$ exist. They define $\mathcal{F} \to \prod_x x_* I_x$. If a section $s$ of $\mathcal{F}$ over $U$ maps to $0$, then each germ $s_x$ maps to $0$ in $I_x$, so $s_x = 0$ for all $x \in U$, and $s = 0$ by Proposition P2.5.4. So the map is a monomorphism. $\square$

*Theorem P2.7.3.* Part 1 is Proposition P2.3.14, and part 2 is Theorem P2.3.15 applied to $\Gamma(X, -)$ and to $f_*$.

Part 3. Let $j: U \to X$ be the inclusion. Extension by zero $j_!$ (Definition P2.5.31) is exact by part 1 of Proposition P2.5.32, and it is left adjoint to restriction: a morphism from $j_! \mathcal{G}$ to $\mathcal{F}$ is, by the universal property of sheafification, a morphism from the presheaf that is $\mathcal{G}(V)$ for $V \subseteq U$ and $0$ otherwise, that is, a compatible family $\mathcal{G}(V) \to \mathcal{F}(V)$ for $V \subseteq U$, that is, a morphism $\mathcal{G} \to \mathcal{F}|_U$. For $\mathcal{O}_U$-modules the same holds with linear maps, since $j_! \mathcal{G}$ is an $\mathcal{O}_X$-module by part 1 of Theorem P2.6.3. A functor with an exact left adjoint sends injectives to injectives (Exercise 4 of Section 3.3). Restriction is exact, so it sends an injective resolution of $\mathcal{F}$ to an injective resolution of $\mathcal{F}|_U$. The restriction maps of sections $\Gamma(X, \mathcal{I}^\bullet) \to \Gamma(U, \mathcal{I}^\bullet)$ are a map of complexes, and they induce the maps $H^i(X, \mathcal{F}) \to H^i(U, \mathcal{F})$. Different resolutions give the same maps up to the canonical isomorphisms of Proposition P2.3.14.

Part 4. Let $\mathcal{F} \to \mathcal{I}^\bullet$ be an injective resolution. Then $R^i f_* \mathcal{F} = \mathcal{H}^i(f_* \mathcal{I}^\bullet)$, the $i$-th cohomology sheaf of the complex of sheaves $f_* \mathcal{I}^\bullet$. For any complex of sheaves $\mathcal{K}^\bullet$ on $Y$, the cohomology sheaf $\mathcal{H}^i(\mathcal{K}^\bullet)$ is the sheafification of the presheaf $V \mapsto H^i(\mathcal{K}^\bullet(V))$. Indeed, there is a natural map from this presheaf to $\mathcal{H}^i(\mathcal{K}^\bullet)$, and on stalks both sides are $H^i(\mathcal{K}^\bullet_y)$, because stalks are exact and commute with kernels, images and quotients. Now $(f_* \mathcal{I}^\bullet)(V) = \mathcal{I}^\bullet(f^{-1}(V))$, and by part 3 the cohomology of this complex is $H^i(f^{-1}(V), \mathcal{F})$.

Part 5. Embed $\mathcal{F}$ into an injective $\mathcal{I}$, and let $\mathcal{Q} = \mathcal{I}/\mathcal{F}$. For every open $U$, part 3 and the long exact sequence on $U$ give an exact sequence $\Gamma(U, \mathcal{I}) \to \Gamma(U, \mathcal{Q}) \to H^1(U, \mathcal{F}) \to 0$ and isomorphisms $H^{i-1}(U, \mathcal{Q}) \cong H^i(U, \mathcal{F})$ for $i \geq 2$, compatible with restriction by naturality. For $i = 1$, a class $\xi$ is the image of a section $q \in \Gamma(X, \mathcal{Q})$. Since $\mathcal{I} \to \mathcal{Q}$ is an epimorphism of sheaves, every $x$ has a neighbourhood $U$ on which $q|_U$ lifts to $\Gamma(U, \mathcal{I})$. Then $\xi|_U = 0$. For $i \geq 2$, $\xi$ comes from a class in $H^{i-1}(X, \mathcal{Q})$, which vanishes locally by induction on $i$, and so $\xi$ vanishes locally. $\square$

*Proposition P2.7.4.* The functor $i_*$ is exact by part 2 of Proposition P2.5.32. Its left adjoint $i^{-1}$ is exact (Corollary P2.5.30), so $i_*$ sends injectives to injectives. An exact functor has no higher derived functors, so $R^q i_* \mathcal{E} = 0$ for $q > 0$. If $\mathcal{E} \to \mathcal{J}^\bullet$ is an injective resolution on $Z$, then $i_* \mathcal{E} \to i_* \mathcal{J}^\bullet$ is an injective resolution on $X$, and $\Gamma(X, i_* \mathcal{J}^\bullet) = \Gamma(Z, \mathcal{J}^\bullet)$. Taking cohomology gives the isomorphism. For modules, $i_*$ from $\mathcal{O}_Z$-modules to $\mathcal{O}_X$-modules is exact by the same stalk computation, and Section 7.2 shows that cohomology may be computed in $\mathsf{Ab}$. $\square$

### Exercises

1. (A) Show that $H^i(X, \mathcal{F} \oplus \mathcal{G}) \cong H^i(X, \mathcal{F}) \oplus H^i(X, \mathcal{G})$.
2. (A) Let $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ be exact with $H^1(X, \mathcal{F}') = 0$. Show that $\Gamma(X, \mathcal{F}) \to \Gamma(X, \mathcal{F}'')$ is surjective.
3. (A) Let $X = Y \sqcup Z$ with $Y$ and $Z$ open. Show that $H^i(X, \mathcal{F}) \cong H^i(Y, \mathcal{F}) \oplus H^i(Z, \mathcal{F})$.
4. (B) Let $f: X \to Y$ be continuous and $V \subseteq Y$ open. Show that $(R^i f_* \mathcal{F})|_V \cong R^i (f|_{f^{-1} V})_* (\mathcal{F}|_{f^{-1} V})$.
5. (B) Let $\mathcal{F}$ be a sheaf with $H^1(U, \mathcal{F}) = 0$ for every open $U$. Show that for every exact sequence $0 \to \mathcal{F} \to \mathcal{G} \to \mathcal{H} \to 0$, the presheaf cokernel of $\mathcal{F} \to \mathcal{G}$ is already a sheaf.
6. (B) Let $X$ be a space with a point $x$ whose only open neighbourhood is $X$. Show that $\Gamma(X, -) = (-)_x$ is exact and that $H^i(X, \mathcal{F}) = 0$ for all $i > 0$ and all $\mathcal{F}$. Deduce that $H^i(\operatorname{Spec} A, \mathcal{F}) = 0$ for $i > 0$ when $A$ is a local ring and $\mathcal{F}$ is any sheaf.
7. (C) Let $j: U \to X$ be the inclusion of an open set and $\mathcal{F}$ a sheaf on $U$. Using parts 4 and 5, show that $(R^i j_* \mathcal{F})_x = 0$ for $x \in U$ and $i > 0$. For $U = \mathbb{C} \setminus \{0\} \subset \mathbb{C}$, deduce from Example P2.7.8 that $R^1 j_* \underline{\mathbb{Z}}$ is the skyscraper sheaf at $0$ of its stalk, and that this stalk contains $\mathbb{Z}$.

### Lean

Mathlib defines sheaf cohomology on any site as Ext groups from the constant sheaf, `CategoryTheory.Sheaf.H`, with the functor `CategoryTheory.Sheaf.functorH`, the connecting map `CategoryTheory.Sheaf.H.δ` and the exactness of the long sequence `CategoryTheory.Sheaf.H.longSequence_exact`. For a scheme, the category `AlgebraicGeometry.Scheme.Modules` has an `IsGrothendieckAbelian` instance, and `CategoryTheory.IsGrothendieckAbelian.enoughInjectives` gives enough injectives. The comparison of the Ext definition with $R^i \Gamma$ in the style of Hartshorne, higher direct images of sheaves on spaces and the local vanishing of classes are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Sheaf cohomology was first defined by Leray in the 1940s and was developed by Cartan's seminar with fine resolutions on paracompact spaces. Grothendieck's Tohoku paper of 1957 defined it as a derived functor, with injective resolutions, on an arbitrary space, and proved that sheaves have enough injectives with the argument used here. Godement's book of 1958 gave the treatment by flasque sheaves of Section 7.2. The definition as a derived functor makes the long exact sequence automatic and gives the uniqueness statements of Section 3.3.
