---
title: Direct image, inverse image, sheaves on a base and gluing
nodes: []
sources: [Har77, Vak25, Gro57]
reads_with: [Har77:ch2, Vak25:ch2]
requires: [P2.1, P2.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Direct image, inverse image, sheaves on a base and gluing

### Statement

Let $f: X \to Y$ be a continuous map. Sheaves are sheaves of abelian groups unless stated otherwise.

**Definition P2.5.27 (direct image and inverse image).**

1. For a sheaf $\mathcal{F}$ on $X$, the *direct image* $f_* \mathcal{F}$ is the sheaf on $Y$ with $(f_* \mathcal{F})(V) = \mathcal{F}(f^{-1}(V))$.
2. For a sheaf $\mathcal{G}$ on $Y$, the *inverse image* $f^{-1} \mathcal{G}$ is the sheafification of the presheaf
$$f^{p} \mathcal{G}: U \mapsto \operatorname*{colim}_{V \supseteq f(U)} \mathcal{G}(V),$$
where the colimit runs over the open sets $V \subseteq Y$ that contain $f(U)$, ordered by reverse inclusion.

The direct image is a sheaf, because $f^{-1}$ takes an open cover of $V$ to an open cover of $f^{-1}(V)$ and keeps intersections. For an open subset $j: U \to X$, the inverse image $j^{-1} \mathcal{F}$ is the restriction $\mathcal{F}|_U$, since $U$ is the smallest open set that contains $U$. For the map $\pi: X \to \mathrm{pt}$, $\pi_* \mathcal{F} = \Gamma(X, \mathcal{F})$ and $\pi^{-1} A$ is the constant sheaf $\underline{A}$.

Lean: Mathlib `TopCat.Sheaf.pushforward`, `TopCat.Sheaf.pushforward_sheaf_of_sheaf`, `TopCat.Presheaf.pullback` and `TopCat.Sheaf.pullback`.

**Theorem P2.5.28 (adjunction).** The functor $f^{-1}$ is left adjoint to $f_*$: there is a bijection
$$\operatorname{Hom}_X(f^{-1} \mathcal{G}, \mathcal{F}) \cong \operatorname{Hom}_Y(\mathcal{G}, f_* \mathcal{F}),$$
natural in the sheaf $\mathcal{G}$ on $Y$ and the sheaf $\mathcal{F}$ on $X$.

Lean: Mathlib `TopCat.Sheaf.pullbackPushforwardAdjunction`, and `TopCat.Presheaf.pullbackPushforwardAdjunction` for presheaves.

**Proposition P2.5.29 (stalks of the inverse image).** For every $x \in X$ there is a natural isomorphism $(f^{-1} \mathcal{G})_x \cong \mathcal{G}_{f(x)}$.

Lean: Mathlib `TopCat.Presheaf.stalkPullbackIso`, for the presheaf inverse image.

**Corollary P2.5.30 (exactness).**

1. The functor $f^{-1}: \mathsf{Ab}(Y) \to \mathsf{Ab}(X)$ is exact.
2. The functor $f_*: \mathsf{Ab}(X) \to \mathsf{Ab}(Y)$ is left exact.
3. The functor $f_*$ takes injective sheaves to injective sheaves.

Lean: not in Lean as stated.

**Definition P2.5.31 (extension by zero).** Let $j: U \to X$ be the inclusion of an open set and $\mathcal{F}$ a sheaf on $U$. The *extension by zero* $j_! \mathcal{F}$ is the sheafification of the presheaf that is $\mathcal{F}(V)$ on open sets $V \subseteq U$ and $0$ on the other open sets of $X$.

**Proposition P2.5.32 (open and closed pieces).** Let $j: U \to X$ be the inclusion of an open set, and $i: Z \to X$ the inclusion of its closed complement $Z = X \setminus U$.

1. For a sheaf $\mathcal{F}$ on $U$, $(j_! \mathcal{F})_x = \mathcal{F}_x$ for $x \in U$ and $(j_! \mathcal{F})_x = 0$ for $x \notin U$.
2. For a sheaf $\mathcal{E}$ on $Z$, $(i_* \mathcal{E})_x = \mathcal{E}_x$ for $x \in Z$ and $(i_* \mathcal{E})_x = 0$ for $x \notin Z$. So $i_*$ is exact.
3. For a sheaf $\mathcal{F}$ on $X$ there is an exact sequence
$$0 \to j_! j^{-1} \mathcal{F} \to \mathcal{F} \to i_* i^{-1} \mathcal{F} \to 0.$$

Lean: Mathlib has `TopCat.Presheaf.stalkPushforward.stalkPushforward_iso_of_isInducing` for the stalks of $i_*$ at points of $Z$. Extension by zero is not in Lean as stated.

**Definition P2.5.33 (sheaf on a base).** Let $\mathcal{B}$ be a basis of the topology of $X$ that is closed under finite intersections. A *sheaf on $\mathcal{B}$* is a functor $\mathcal{F}_{\mathcal{B}}: \mathcal{B}^{\mathrm{op}} \to \mathsf{Ab}$ with the following property: for every $W \in \mathcal{B}$ and every cover $W = \bigcup_k W_k$ by members of $\mathcal{B}$, and every family $s_k \in \mathcal{F}_{\mathcal{B}}(W_k)$ with $s_k|_{W_k \cap W_l} = s_l|_{W_k \cap W_l}$, there is exactly one $s \in \mathcal{F}_{\mathcal{B}}(W)$ with $s|_{W_k} = s_k$ for all $k$.

**Theorem P2.5.34 (sheaves on a base).** Let $\mathcal{B}$ be a basis closed under finite intersections.

1. Every sheaf $\mathcal{F}_{\mathcal{B}}$ on $\mathcal{B}$ is the restriction to $\mathcal{B}$ of a sheaf $\mathcal{F}$ on $X$, unique up to a unique isomorphism that is the identity on $\mathcal{B}$.
2. For sheaves $\mathcal{F}, \mathcal{G}$ on $X$, restriction is a bijection $\operatorname{Hom}(\mathcal{F}, \mathcal{G}) \to \operatorname{Hom}(\mathcal{F}|_{\mathcal{B}}, \mathcal{G}|_{\mathcal{B}})$.

Lean: Mathlib `TopCat.Sheaf.restrictHomEquivHom` and `TopCat.Sheaf.isIso_iff_isIso_basis` for part 2. Part 1 is not in Lean as stated.

**Theorem P2.5.35 (gluing sheaves).** Let $X = \bigcup_i U_i$ be an open cover, write $U_{ij} = U_i \cap U_j$ and $U_{ijk} = U_i \cap U_j \cap U_k$, and let $\mathcal{F}_i$ be a sheaf on $U_i$ for each $i$. Let $\varphi_{ij}: \mathcal{F}_j|_{U_{ij}} \to \mathcal{F}_i|_{U_{ij}}$ be isomorphisms with $\varphi_{ii} = 1$ and $\varphi_{ij} \varphi_{jk} = \varphi_{ik}$ on $U_{ijk}$. Then there are a sheaf $\mathcal{F}$ on $X$ and isomorphisms $\psi_i: \mathcal{F}|_{U_i} \to \mathcal{F}_i$ with $\psi_i = \varphi_{ij} \psi_j$ on $U_{ij}$. The pair $(\mathcal{F}, (\psi_i))$ is unique up to a unique isomorphism.

Lean: not in Lean as stated.

### Proof in words

A map $f^{-1} \mathcal{G} \to \mathcal{F}$ must send a section of $\mathcal{G}$ near $f(U)$ to a section of $\mathcal{F}$ on $U$. The largest open set whose image lies in a given $V$ is $f^{-1}(V)$, so this is the same as a map $\mathcal{G}(V) \to \mathcal{F}(f^{-1}(V))$, which is a map $\mathcal{G} \to f_* \mathcal{F}$. The stalk of $f^{-1} \mathcal{G}$ at $x$ only sees small neighbourhoods of $f(x)$, so it is $\mathcal{G}_{f(x)}$, and $f^{-1}$ is exact because exactness is checked on stalks. Then $f_*$ is left exact and keeps injectives, as every right adjoint of an exact functor does.

Extension by zero and direct image along a closed embedding have the stalks one expects, and the sequence of part 3 is exact on stalks: at a point of $U$ it is $0 \to \mathcal{F}_x \to \mathcal{F}_x \to 0 \to 0$, and at a point of $Z$ it is $0 \to 0 \to \mathcal{F}_x \to \mathcal{F}_x \to 0$.

A sheaf is determined by its values on a basis, because the sheaf axiom computes $\mathcal{F}(U)$ from the basic open sets in $U$. So one can define $\mathcal{F}(U)$ as the compatible families of sections on the basic open sets in $U$. Gluing is the same idea: a section of the glued sheaf is a family of local sections that match under the given identifications.

### Examples

**Example P2.5.36 (the structure sheaf of an affine scheme).** Let $A$ be a ring and $X = \operatorname{Spec} A$. The basic open sets $D(g)$ form a basis closed under finite intersections, since $D(g) \cap D(h) = D(gh)$. The rule $D(g) \mapsto A_g$ is a sheaf on this basis, and the theorem on sheaves on a base gives the structure sheaf $\mathcal{O}_X$. In the same way an $A$-module $M$ gives the sheaf $\widetilde{M}$ with $\widetilde{M}(D(g)) = M_g$. These are the quasi-coherent sheaves of P3 and P4 Ch. 1. Gluing then defines $\mathcal{O}_X$ and the quasi-coherent sheaves on any scheme, from affine pieces.

**Example P2.5.37 (the restriction sequence).** Let $X$ be a variety and $S \subseteq X$ a closed subvariety with inclusion $i: S \to X$. Since $i_*$ is exact, it takes an injective resolution of a sheaf $\mathcal{E}$ on $S$ to a resolution of $i_* \mathcal{E}$, and it keeps injectives by the corollary. Since $\Gamma(X, i_* -) = \Gamma(S, -)$, this gives $H^n(X, i_* \mathcal{E}) = H^n(S, \mathcal{E})$ once cohomology is defined in Chapter 7. This is how the restriction sequence $0 \to \mathcal{O}_X(mD - S) \to \mathcal{O}_X(mD) \to i_* \mathcal{O}_S(mD|_S) \to 0$, for a Cartier divisor $S$ and a Cartier divisor $D$, relates cohomology on $X$ to cohomology on $S$. The base point free theorem (Volume 7) and the induction on dimension in the minimal model program use it in this form.

**Example P2.5.38 (the Leray spectral sequence needs injectives).** Let $f: X \to Y$ and $g: Y \to Z$ be continuous. Then $(g f)_* = g_* f_*$, and $f_*$ takes injectives to injectives by the corollary. These are the hypotheses of the Grothendieck spectral sequence of Section 4.3, applied to $g_*$ and $f_*$. For $Z$ a point, it is the Leray spectral sequence $H^p(Y, R^q f_* \mathcal{F}) \Rightarrow H^{p+q}(X, \mathcal{F})$.

**Example P2.5.39 (inverse image of a constant sheaf).** For any continuous $f: X \to Y$ and abelian group $A$, $f^{-1} \underline{A}_Y \cong \underline{A}_X$, because both are inverse images of $A$ from a point and $\pi_Y f = \pi_X$. More generally $(g f)^{-1} \cong f^{-1} g^{-1}$, since both are left adjoint to $(g f)_* = g_* f_*$ (Section 1.3).

**Example P2.5.40 (direct image is not exact).** For $\pi: X \to \mathrm{pt}$, $\pi_* = \Gamma(X, -)$, which is not right exact by Section 5.3. For a closed embedding the direct image is exact. For an open embedding $j: U \to X$ it is not: on $X = \mathbb{C}$ and $U = \mathbb{C} \setminus \{0\}$, the exponential sequence on $U$ is exact, but $j_* \mathcal{O}_U \to j_* \mathcal{O}_U^\times$ is not surjective on the stalk at $0$, since $z$ has no logarithm on any punctured disc.

### Proof

*Proof of the theorem on adjunction.* First compare presheaves. A morphism $\alpha: f^p \mathcal{G} \to \mathcal{F}$ gives, for each open $V \subseteq Y$, the composite
$$\mathcal{G}(V) \to (f^p \mathcal{G})(f^{-1}(V)) \xrightarrow{\alpha} \mathcal{F}(f^{-1}(V)) = (f_* \mathcal{F})(V),$$
where the first map is the canonical map into the colimit, defined because $f(f^{-1}(V)) \subseteq V$. These maps commute with restriction, so they form a morphism $\beta: \mathcal{G} \to f_* \mathcal{F}$. Conversely, given $\beta$, let $U \subseteq X$ be open and $V \supseteq f(U)$. Then $U \subseteq f^{-1}(V)$, and the maps $\mathcal{G}(V) \xrightarrow{\beta} \mathcal{F}(f^{-1}(V)) \to \mathcal{F}(U)$ are compatible as $V$ shrinks. So they induce a map $(f^p \mathcal{G})(U) \to \mathcal{F}(U)$, and these form a morphism $\alpha$. The two constructions are inverse to each other. Starting from $\beta$, the composite at $V$ uses $U = f^{-1}(V)$ and gives back $\beta_V$. Starting from $\alpha$, the new map agrees with $\alpha$ on the image of each $\mathcal{G}(V)$ in the colimit, because $\alpha$ commutes with restriction from $f^{-1}(V)$ to $U$, and these images generate the colimit. Both constructions are natural in $\mathcal{G}$ and $\mathcal{F}$. So $\operatorname{Hom}(f^p \mathcal{G}, \mathcal{F}) \cong \operatorname{Hom}(\mathcal{G}, f_* \mathcal{F})$. Since $\mathcal{F}$ is a sheaf, the theorem of Section 5.2 gives $\operatorname{Hom}(f^{-1} \mathcal{G}, \mathcal{F}) \cong \operatorname{Hom}(f^p \mathcal{G}, \mathcal{F})$, and the theorem follows. $\square$

*Proof of the proposition on stalks.* Sheafification does not change stalks (Section 5.2), so it suffices to compute the stalk of $f^p \mathcal{G}$. It is a colimit over the pairs $(U, V)$ with $x \in U$ open in $X$, $V$ open in $Y$ and $f(U) \subseteq V$, of the groups $\mathcal{G}(V)$. Every such $V$ contains $f(x)$. Conversely, every open $V \ni f(x)$ occurs, with $U = f^{-1}(V)$. So the colimit is $\operatorname*{colim}_{V \ni f(x)} \mathcal{G}(V) = \mathcal{G}_{f(x)}$. $\square$

*Proof of the corollary.* Part 1: a sequence in $\mathsf{Ab}(Y)$ that is exact at every stalk $\mathcal{G}_y$ is exact at every $\mathcal{G}_{f(x)}$, and these are the stalks of the inverse images. Exactness is checked on stalks (Section 5.3). Part 2: $f_*$ is a right adjoint, so it keeps kernels (Section 1.4). Concretely, $(f_* \ker \varphi)(V) = \ker(\varphi_{f^{-1}(V)})$. Part 3: let $\mathcal{I}$ be injective on $X$. Then $\operatorname{Hom}_Y(-, f_* \mathcal{I}) \cong \operatorname{Hom}_X(f^{-1}(-), \mathcal{I})$ is the composite of the exact functor $f^{-1}$ and the exact functor $\operatorname{Hom}_X(-, \mathcal{I})$. So it is exact, and $f_* \mathcal{I}$ is injective. $\square$

*Proof of the proposition on open and closed pieces.* Part 1. Let $x \in U$. The open sets $V$ with $x \in V \subseteq U$ are cofinal among the neighbourhoods of $x$, and on them the presheaf is $\mathcal{F}(V)$. So the stalk is $\mathcal{F}_x$. Let $x \notin U$. No neighbourhood of $x$ lies in $U$, so the presheaf is $0$ on every neighbourhood of $x$, and the stalk is $0$. Sheafification does not change stalks.

Part 2. Let $x \notin Z$. Then $U = X \setminus Z$ is a neighbourhood of $x$ and $(i_* \mathcal{E})(U) = \mathcal{E}(\emptyset) = 0$. So the stalk is $0$. Let $x \in Z$. The open neighbourhoods of $x$ in $Z$ are the sets $V \cap Z$ with $V$ an open neighbourhood of $x$ in $X$. So $\operatorname*{colim}_{V \ni x} \mathcal{E}(V \cap Z) = \mathcal{E}_x$. A sequence of sheaves on $Z$ that is exact on stalks then gives a sequence on $X$ that is exact on stalks, so $i_*$ is exact.

Part 3. The map $j_! j^{-1} \mathcal{F} \to \mathcal{F}$ is induced, through sheafification, by the identity of $\mathcal{F}(V)$ for $V \subseteq U$ and by $0$ on the other open sets. It is a morphism of presheaves because a restriction from a set not contained in $U$ to a set contained in $U$ starts from $0$. The map $\mathcal{F} \to i_* i^{-1} \mathcal{F}$ is the unit of the adjunction. By part 1 and the proposition on stalks, the first map is the identity of $\mathcal{F}_x$ on the stalks at $x \in U$, and the zero map from $0$ at $x \in Z$. By part 2 and the proposition on stalks, the stalk of $i_* i^{-1} \mathcal{F}$ is $0$ at $x \in U$ and $\mathcal{F}_x$ at $x \in Z$. At $x \in Z$, the stalk of the unit is the canonical identification of $\mathcal{F}_x$ with $(i^{-1} \mathcal{F})_x$. So the sequence on stalks is $0 \to \mathcal{F}_x \to \mathcal{F}_x \to 0 \to 0$ at $x \in U$ and $0 \to 0 \to \mathcal{F}_x \to \mathcal{F}_x \to 0$ at $x \in Z$, both exact. By Section 5.3 the sequence is exact. $\square$

*Proof of the theorem on sheaves on a base.* For an open $U \subseteq X$, let $\mathcal{B}_U$ be the set of members of $\mathcal{B}$ contained in $U$, and define
$$\mathcal{F}(U) = \Big\{ (s_W) \in \prod_{W \in \mathcal{B}_U} \mathcal{F}_{\mathcal{B}}(W) : s_W|_{W'} = s_{W'} \text{ whenever } W' \subseteq W \Big\},$$
with restriction maps given by forgetting the members of the family. This is a presheaf.

It is a sheaf. Let $U = \bigcup_k U_k$ and let $(s^{(k)}) \in \mathcal{F}(U_k)$ agree on overlaps. Locality: if $(s_W) \in \mathcal{F}(U)$ restricts to $0$ on each $U_k$, then $s_W = 0$ for each $W \in \mathcal{B}$ contained in some $U_k$. For a general $W \in \mathcal{B}_U$, the members of $\mathcal{B}$ contained in $W \cap U_k$ for some $k$ cover $W$, and $s_W$ restricts to $0$ on each of them. By the sheaf property on $\mathcal{B}$, $s_W = 0$. Gluing: for $W \in \mathcal{B}_U$, cover $W$ by the members $W'$ of $\mathcal{B}$ contained in $W \cap U_k$ for some $k$, with the sections $s^{(k)}_{W'}$. These do not depend on $k$, by the agreement on overlaps. They agree on the intersections, which lie in $\mathcal{B}$. So they glue to a unique $s_W \in \mathcal{F}_{\mathcal{B}}(W)$. The uniqueness in the sheaf property on $\mathcal{B}$ shows that $(s_W)$ is compatible and restricts to $s^{(k)}$ on each $U_k$.

On $\mathcal{B}$ it agrees with $\mathcal{F}_{\mathcal{B}}$. For $W \in \mathcal{B}$, the map $\mathcal{F}_{\mathcal{B}}(W) \to \mathcal{F}(W)$, $s \mapsto (s|_{W'})$, is bijective: a compatible family $(s_{W'})_{W' \in \mathcal{B}_W}$ contains $s_W$ itself, and $s_W$ restricts to the other members. This proves existence in part 1.

For uniqueness and part 2, let $\mathcal{G}$ be any sheaf on $X$. The same argument with the sheaf axiom for $\mathcal{G}$ shows that $\mathcal{G}(U) \to \{ \text{compatible families } (t_W)_{W \in \mathcal{B}_U} \}$ is bijective: injective by locality, since $\mathcal{B}_U$ covers $U$, and surjective by gluing, since the intersections of members of $\mathcal{B}_U$ lie in $\mathcal{B}_U$. So every sheaf is recovered from its restriction to $\mathcal{B}$ by the formula above, naturally in the sheaf. A morphism on $\mathcal{B}$ then extends uniquely by acting on each member of a family. This proves part 2. An isomorphism $\mathcal{G}|_{\mathcal{B}} \cong \mathcal{F}_{\mathcal{B}}$ extends to a unique isomorphism $\mathcal{G} \cong \mathcal{F}$ by part 2, which gives uniqueness in part 1. $\square$

*Proof of the theorem on gluing.* First, $\varphi_{ii} = 1$ and the cocycle condition with $k = i$ give $\varphi_{ij} \varphi_{ji} = 1$, so $\varphi_{ji} = \varphi_{ij}^{-1}$. For an open $U \subseteq X$, let
$$\mathcal{F}(U) = \Big\{ (s_i) \in \prod_i \mathcal{F}_i(U \cap U_i) : s_i|_{U \cap U_{ij}} = \varphi_{ij}(s_j|_{U \cap U_{ij}}) \text{ for all } i, j \Big\}.$$
This is the kernel of a morphism between products of the sheaves $u_{i*} \mathcal{F}_i$, where $u_i: U_i \to X$ is the inclusion. Products and kernels of sheaves are sheaves (Section 5.3), so $\mathcal{F}$ is a sheaf.

Define $\psi_i: \mathcal{F}|_{U_i} \to \mathcal{F}_i$ by $(s_k) \mapsto s_i$, for $U \subseteq U_i$. It is bijective. Given $t \in \mathcal{F}_i(U)$ with $U \subseteq U_i$, set $s_k = \varphi_{ki}(t|_{U \cap U_k})$. Then on $U \cap U_{kl}$, $\varphi_{kl}(s_l) = \varphi_{kl} \varphi_{li}(t) = \varphi_{ki}(t) = s_k$ by the cocycle condition, so $(s_k) \in \mathcal{F}(U)$, and $s_i = t$ since $\varphi_{ii} = 1$. Every $(s_k) \in \mathcal{F}(U)$ has this form with $t = s_i$, since $s_k = \varphi_{ki}(s_i)$ on $U \cap U_k = U \cap U_{ki}$. So $\psi_i$ is an isomorphism. By definition of $\mathcal{F}$, $\psi_i = \varphi_{ij} \psi_j$ on $U_{ij}$.

Uniqueness. Let $(\mathcal{F}', (\psi'_i))$ be a second solution. The isomorphisms $\psi_i^{-1} \psi'_i: \mathcal{F}'|_{U_i} \to \mathcal{F}|_{U_i}$ agree on $U_{ij}$, because $\psi_i^{-1} \psi'_i = \psi_j^{-1} \varphi_{ij}^{-1} \varphi_{ij} \psi'_j = \psi_j^{-1} \psi'_j$ there. Morphisms of sheaves glue (Exercise 4), so they define an isomorphism $\mathcal{F}' \to \mathcal{F}$, which is the only one compatible with the $\psi$. $\square$

### Exercises

1. (A) Show that $(g f)_* = g_* f_*$ for continuous maps $f: X \to Y$ and $g: Y \to Z$, and that $f_*$ of a flasque sheaf is flasque.
2. (A) Let $x \in X$ and $i_x: \{x\} \to X$ the inclusion. Show that $i_x^{-1} \mathcal{F} = \mathcal{F}_x$ and that $i_{x*} A$ is the skyscraper sheaf $x_* A$. Deduce the adjunction $\operatorname{Hom}(\mathcal{F}, x_* A) \cong \operatorname{Hom}(\mathcal{F}_x, A)$ of Section 5.3 from the theorem on adjunction.
3. (A) Show that $j_!$ is exact and that $j_!$ is left adjoint to $j^{-1}$ for an open inclusion $j: U \to X$. For $Z \subseteq X$ closed and $\mathcal{E}$ a sheaf on $Z$, show that the counit $i^{-1} i_* \mathcal{E} \to \mathcal{E}$ is an isomorphism.
4. (B) Let $X = \bigcup_i U_i$ be an open cover and $\mathcal{F}, \mathcal{G}$ sheaves on $X$. Show that morphisms $\alpha_i: \mathcal{F}|_{U_i} \to \mathcal{G}|_{U_i}$ that agree on each $U_{ij}$ glue to a unique morphism $\alpha: \mathcal{F} \to \mathcal{G}$. In other words, $U \mapsto \operatorname{Hom}(\mathcal{F}|_U, \mathcal{G}|_U)$ is a sheaf, the sheaf $\mathcal{H}om(\mathcal{F}, \mathcal{G})$.
5. (B) Show that $\mathbb{Z}_U = j_! \underline{\mathbb{Z}}_U$ is the sheaf of Exercise 4 of Section 5.3, and deduce $\operatorname{Hom}(\mathbb{Z}_U, \mathcal{F}) = \mathcal{F}(U)$ from Exercise 3.
6. (B) For $Z \subseteq X$ closed with complement $U$, let $\Gamma_Z(X, \mathcal{F}) = \ker(\mathcal{F}(X) \to \mathcal{F}(U))$, the sections with support in $Z$. Show that $\Gamma_Z(X, -)$ is left exact, and that $\Gamma_Z(X, \mathcal{F}) \cong \operatorname{Hom}(i_* \underline{\mathbb{Z}}_Z, \mathcal{F})$. Its derived functors are the local cohomology groups $H^n_Z(X, \mathcal{F})$, which measure depth (P3).
7. (C) Show that a basis that is not closed under finite intersections also suffices for the theorem on sheaves on a base, if the sheaf condition on $\mathcal{B}$ requires agreement on all members of $\mathcal{B}$ contained in $W_k \cap W_l$ rather than on $W_k \cap W_l$.
8. (C) Give an example of a continuous map $f$ and an injective sheaf $\mathcal{J}$ on $Y$ such that $f^{-1} \mathcal{J}$ is not injective. (Hint: take $f: \mathbb{R} \to \mathrm{pt}$ and $\mathcal{J} = \mathbb{Q}/\mathbb{Z}$, and show that the constant sheaf $\underline{\mathbb{Q}/\mathbb{Z}}$ on $\mathbb{R}$ is not flasque. An injective sheaf is flasque: apply $\operatorname{Hom}(-, \mathcal{J})$ to the monomorphism $\mathbb{Z}_V \to \mathbb{Z}_U$ for open $V \subseteq U$ and use Exercise 5.)

### Lean

Mathlib defines direct image and inverse image of presheaves and of sheaves (`TopCat.Presheaf.pushforward`, `TopCat.Presheaf.pullback`, `TopCat.Sheaf.pushforward`, `TopCat.Sheaf.pullback`), proves the adjunction (`TopCat.Sheaf.pullbackPushforwardAdjunction`) and computes stalks of the inverse image (`TopCat.Presheaf.stalkPullbackIso`). For a basis of the topology, `TopCat.Sheaf.restrictHomEquivHom` is part 2 of the theorem on sheaves on a base. The comparison lemma `CategoryTheory.Functor.IsDenseSubsite.sheafEquiv` gives an equivalence of sheaf categories for a dense subsite, which covers sheaves on a basis with the induced topology. Extension by zero, the exact sequence of part 3 and the gluing of sheaves are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Direct and inverse images, extension by zero and the six operations around them were organized by Grothendieck. The adjunction $f^{-1} \dashv f_*$ appears in Godement's book of 1958 and in the Tohoku paper. Sheaves on a base are how Grothendieck defines the structure sheaf of an affine scheme in EGA I, and the same construction is in Hartshorne, Chapter II, and Vakil, Chapter 2. Gluing of sheaves along a cocycle is how schemes and their quasi-coherent sheaves are put together from affine pieces.
