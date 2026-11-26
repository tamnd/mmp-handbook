---
title: Presheaves, sheaves and stalks
nodes: []
sources: [Har77, Vak25, Gro57]
reads_with: [Har77:ch2, Vak25:ch2]
requires: [P2.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Presheaves, sheaves and stalks

### Statement

Throughout, $X$ is a topological space and $\operatorname{Op}(X)$ is the category whose objects are the open subsets of $X$ and whose maps are the inclusions $V \subseteq U$. The values of presheaves are sets, abelian groups, rings or modules. All these are sets with structure, and the definitions below use their elements.

**Definition P2.5.1 (presheaf).** A *presheaf* $\mathcal{F}$ on $X$ is a functor $\operatorname{Op}(X)^{\mathrm{op}} \to \mathsf{Set}$, or to $\mathsf{Ab}$, $\mathsf{Ring}$ or $\mathsf{Mod}_A$. So it gives a set $\mathcal{F}(U)$ for each open $U$, and a *restriction map* $\mathcal{F}(U) \to \mathcal{F}(V)$, $s \mapsto s|_V$, for each $V \subseteq U$, with $s|_U = s$ and $(s|_V)|_W = s|_W$. The elements of $\mathcal{F}(U)$ are *sections* over $U$, and $\Gamma(U, \mathcal{F}) = \mathcal{F}(U)$. A *morphism* $\varphi: \mathcal{F} \to \mathcal{G}$ is a natural transformation: maps $\varphi_U: \mathcal{F}(U) \to \mathcal{G}(U)$ that commute with restriction.

Lean: Mathlib `TopCat.Presheaf`.

**Definition P2.5.2 (sheaf).** A presheaf $\mathcal{F}$ is a *sheaf* if, for every open $U$ and every open cover $U = \bigcup_{i \in I} U_i$, two conditions hold.

1. (Locality.) If $s, t \in \mathcal{F}(U)$ and $s|_{U_i} = t|_{U_i}$ for all $i$, then $s = t$.
2. (Gluing.) If $s_i \in \mathcal{F}(U_i)$ and $s_i|_{U_i \cap U_j} = s_j|_{U_i \cap U_j}$ for all $i, j$, then there is $s \in \mathcal{F}(U)$ with $s|_{U_i} = s_i$ for all $i$.

Equivalently, for every cover the diagram
$$\mathcal{F}(U) \to \prod_i \mathcal{F}(U_i) \rightrightarrows \prod_{i,j} \mathcal{F}(U_i \cap U_j)$$
is an equalizer, the two maps sending $(s_i)$ to $(s_i|_{U_i \cap U_j})$ and to $(s_j|_{U_i \cap U_j})$. A morphism of sheaves is a morphism of presheaves. Write $\mathsf{Sh}(X)$ for the category of sheaves of sets and $\mathsf{Ab}(X)$ for the category of sheaves of abelian groups.

Lean: Mathlib `TopCat.Presheaf.IsSheaf`, `TopCat.Sheaf`, and `TopCat.Presheaf.isSheaf_iff_isSheafUniqueGluing` for the form with locality and gluing.

The empty cover of $U = \emptyset$ shows that $\mathcal{F}(\emptyset)$ is a one point set for a sheaf of sets, and $0$ for a sheaf of abelian groups. For sheaves of abelian groups, locality says that a section that restricts to $0$ on each $U_i$ is $0$.

**Definition P2.5.3 (stalk).** Let $x \in X$. The *stalk* of a presheaf $\mathcal{F}$ at $x$ is the colimit
$$\mathcal{F}_x = \operatorname*{colim}_{x \in U} \mathcal{F}(U)$$
over the open neighbourhoods of $x$, ordered by reverse inclusion. Concretely, an element of $\mathcal{F}_x$ is a pair $(U, s)$ with $x \in U$ and $s \in \mathcal{F}(U)$, and two pairs $(U, s)$ and $(V, t)$ are equal if $s|_W = t|_W$ for some open $W$ with $x \in W \subseteq U \cap V$. The class $s_x$ of $(U, s)$ is the *germ* of $s$ at $x$. A morphism $\varphi$ induces maps $\varphi_x: \mathcal{F}_x \to \mathcal{G}_x$, $s_x \mapsto \varphi_U(s)_x$.

Lean: Mathlib `TopCat.Presheaf.stalk`, `TopCat.Presheaf.germ` and `TopCat.Presheaf.stalkFunctor`.

The colimit is filtered, since two neighbourhoods of $x$ contain a third. So the stalk of a presheaf of abelian groups or rings is again an abelian group or a ring, computed on the underlying sets.

**Proposition P2.5.4 (sections are determined by germs).** Let $\mathcal{F}$ be a sheaf and $s, t \in \mathcal{F}(U)$. If $s_x = t_x$ for all $x \in U$, then $s = t$.

Lean: Mathlib `TopCat.Presheaf.section_ext`.

**Theorem P2.5.5 (morphisms of sheaves and stalks).** Let $\varphi: \mathcal{F} \to \mathcal{G}$ be a morphism of sheaves of sets on $X$.

1. Each $\varphi_U$ is injective if and only if each $\varphi_x$ is injective.
2. $\varphi$ is an isomorphism if and only if each $\varphi_x$ is bijective.
3. If $\psi: \mathcal{F} \to \mathcal{G}$ is a second morphism with $\varphi_x = \psi_x$ for all $x$, then $\varphi = \psi$.

Lean: Mathlib `TopCat.Presheaf.app_injective_of_stalkFunctor_map_injective` (one direction of part 1), `TopCat.Presheaf.isIso_iff_stalkFunctor_map_iso` (part 2).

The same statements hold for sheaves of abelian groups, rings and modules, since a morphism of such sheaves is an isomorphism if and only if it is bijective on each $\mathcal{F}(U)$. Surjectivity on stalks does not imply surjectivity on sections. Section 5.3 shows that it means surjectivity as a map of sheaves, which is weaker.

### Proof in words

A sheaf is a presheaf whose sections are local: a section is known when it is known near each point, and compatible local sections glue. Locality gives the proposition at once. If two sections have the same germ at $x$, they agree on some neighbourhood of $x$. These neighbourhoods cover $U$, so the sections agree. The theorem says that stalks see everything about morphisms of sheaves. Injectivity passes between sections and germs through the proposition. For surjectivity, a section $t$ of $\mathcal{G}$ is the image of a section of $\mathcal{F}$ near each point, because $\varphi_x$ is onto. Injectivity makes these local preimages agree on overlaps, and gluing produces a global preimage.

### Examples

**Example P2.5.6 (functions).** For a topological space $X$, the continuous real functions $U \mapsto C(U, \mathbb{R})$ form a sheaf of rings: continuity is local and continuous functions that agree on overlaps glue. The same holds for smooth functions on a manifold and for holomorphic functions on a complex manifold. For the holomorphic functions $\mathcal{O}_X$ on $\mathbb{C}^n$, the stalk at $0$ is the ring $\mathbb{C}\{z_1, \dots, z_n\}$ of convergent power series. For a variety $X$, the regular functions form the structure sheaf $\mathcal{O}_X$, and $\mathcal{O}_{X,x}$ is the local ring of $X$ at $x$ (P3).

**Example P2.5.7 (a presheaf that is not a sheaf).** The bounded continuous functions on open subsets of $\mathbb{R}$ form a presheaf. Locality holds, but gluing fails: the functions $f_n(x) = x$ on $(-n, n)$ agree on overlaps, but the glued function $x$ on $\mathbb{R}$ is not bounded. Boundedness is not a local condition.

**Example P2.5.8 (constant presheaf and constant sheaf).** Let $A$ be an abelian group. The *constant presheaf* gives $A$ on every nonempty open set and $0$ on $\emptyset$, with identity restrictions. It is not a sheaf if $X$ has two disjoint nonempty open sets $U$ and $V$: the sections $a$ on $U$ and $b \neq a$ on $V$ agree on $U \cap V = \emptyset$ but do not glue. The *constant sheaf* $\underline{A}$ gives the locally constant functions $U \to A$. Its stalks are all $A$. If $X$ is locally connected, $\underline{A}(U) = A^{\pi_0(U)}$, a product over the connected components of $U$. Section 5.2 shows that $\underline{A}$ is the sheafification of the constant presheaf.

**Example P2.5.9 (skyscraper sheaves).** Let $x \in X$ and $A$ an abelian group. The *skyscraper sheaf* $x_* A$ gives $A$ on the open sets that contain $x$ and $0$ on the others. Its stalk at $y$ is $A$ if $y$ is in the closure of $\{x\}$ and $0$ otherwise. If $x$ is a closed point, it is $A$ at $x$ and $0$ elsewhere.

**Example P2.5.10 (the sheaf of a divisor).** Let $X$ be a normal variety with function field $k(X)$, and $D$ a Weil divisor on $X$. For an open $U$ put
$$\mathcal{O}_X(D)(U) = \{ f \in k(X)^\times : (\operatorname{div} f + D)|_U \geq 0 \} \cup \{0\}.$$
The condition $\operatorname{div} f + D \geq 0$ on $U$ says that each prime divisor meeting $U$ has nonnegative coefficient, and this is local on $U$. So $\mathcal{O}_X(D)$ is a sheaf, a subsheaf of the constant sheaf $\underline{k(X)}$. The spaces of global sections $H^0(X, \mathcal{O}_X(mD))$ define the linear systems $|mD|$ of Volume 1. The base point free theorem of Volume 7 is a statement about these sheaves, and the restriction sequence $0 \to \mathcal{O}_X(mD - S) \to \mathcal{O}_X(mD) \to \mathcal{O}_S(mD|_S) \to 0$ in its proof is a short exact sequence of sheaves in the sense of Section 5.3.

**Example P2.5.11 (sheaves on a discrete space).** If $X$ has the discrete topology, a sheaf $\mathcal{F}$ is determined by its stalks: $\mathcal{F}_x = \mathcal{F}(\{x\})$, and gluing over the cover of $U$ by points gives $\mathcal{F}(U) = \prod_{x \in U} \mathcal{F}_x$. So $\mathsf{Sh}(X)$ is equivalent to the category of families of sets indexed by $X$.

### Proof

*Proof of the proposition.* For each $x \in U$, the equality $s_x = t_x$ gives an open $W_x$ with $x \in W_x \subseteq U$ and $s|_{W_x} = t|_{W_x}$. The sets $W_x$ cover $U$, so $s = t$ by locality. $\square$

*Proof of the theorem.* Part 1, first direction. Suppose each $\varphi_U$ is injective, and let $s_x, t_x \in \mathcal{F}_x$, represented by sections on a common neighbourhood $U$, with $\varphi_x(s_x) = \varphi_x(t_x)$. Then $\varphi_U(s)|_W = \varphi_U(t)|_W$ for some open $W \ni x$. So $\varphi_W(s|_W) = \varphi_W(t|_W)$, hence $s|_W = t|_W$ and $s_x = t_x$. Second direction. Suppose each $\varphi_x$ is injective and $\varphi_U(s) = \varphi_U(t)$. Then $\varphi_x(s_x) = \varphi_U(s)_x = \varphi_U(t)_x = \varphi_x(t_x)$ for all $x \in U$, so $s_x = t_x$, and $s = t$ by the proposition.

Part 2. An isomorphism induces bijections on stalks, since the stalk is a functor. Conversely, suppose each $\varphi_x$ is bijective. By part 1 each $\varphi_U$ is injective. For surjectivity, let $t \in \mathcal{G}(U)$. For each $x \in U$ choose a germ with $\varphi_x(\sigma) = t_x$. It is represented by a section $s^x \in \mathcal{F}(V_x)$ with $x \in V_x \subseteq U$, and $\varphi(s^x)_x = t_x$. After shrinking $V_x$, $\varphi(s^x) = t|_{V_x}$. On $V_x \cap V_y$, the sections $s^x$ and $s^y$ have the same image $t|_{V_x \cap V_y}$, so they are equal by injectivity of $\varphi_{V_x \cap V_y}$. By gluing there is $s \in \mathcal{F}(U)$ with $s|_{V_x} = s^x$. Then $\varphi(s)$ and $t$ agree on each $V_x$, so $\varphi(s) = t$ by locality. The inverse maps $\varphi_U^{-1}$ commute with restriction, since the $\varphi_U$ do, so they form an inverse morphism.

Part 3. Let $s \in \mathcal{F}(U)$. For each $x \in U$, $\varphi(s)_x = \varphi_x(s_x) = \psi_x(s_x) = \psi(s)_x$. By the proposition, applied to the sheaf $\mathcal{G}$, $\varphi(s) = \psi(s)$. $\square$

### Exercises

1. (A) Let $\mathcal{F}$ be a sheaf of sets. Show that $\mathcal{F}(\emptyset)$ is a one point set. Show that if $U$ and $V$ are disjoint, then $\mathcal{F}(U \cup V) = \mathcal{F}(U) \times \mathcal{F}(V)$.
2. (A) Let $\pi: E \to X$ be continuous. Show that the continuous sections $U \mapsto \{ s: U \to E \text{ continuous} : \pi s = 1_U \}$ form a sheaf of sets.
3. (A) Let $X = \mathbb{P}^1$ over an algebraically closed field, $p$ a point and $n \geq 0$. Show that $H^0(X, \mathcal{O}_X(n p))$ is the space of rational functions with a pole of order at most $n$ at $p$ and no other pole. Taking $p = \infty$, identify it with the polynomials of degree at most $n$ in an affine coordinate.
4. (B) Let $\mathcal{B}$ be a basis of the topology of $X$ and $\mathcal{F}$ a presheaf. Suppose that the sheaf condition holds for every open $U$ and every cover of $U$ by members of $\mathcal{B}$. Show that $\mathcal{F}$ is a sheaf.
5. (B) Let $\mathcal{O}$ be the sheaf of holomorphic functions and $\mathcal{O}^\times$ the sheaf of nowhere zero holomorphic functions on $X = \mathbb{C} \setminus \{0\}$. Show that $\exp: \mathcal{O} \to \mathcal{O}^\times$ is surjective on every stalk but not on $\Gamma(X, -)$.
6. (B) Show that the category $\mathsf{Ab}(X)$ has all limits, computed sectionwise: $(\lim \mathcal{F}_i)(U) = \lim \mathcal{F}_i(U)$. Show that the sectionwise cokernel of a morphism of sheaves need not be a sheaf.
7. (C) Show that the stalk functor $\mathcal{F} \mapsto \mathcal{F}_x$ on $\mathsf{Ab}(X)$ preserves finite limits. On $X = \mathbb{R}$, let $\mathcal{F}_n$ be the skyscraper sheaf $\mathbb{Z}$ at $1/n$. Show that $(\prod_n \mathcal{F}_n)_0 \cong \prod_n \mathbb{Z} / \bigoplus_n \mathbb{Z}$, while $\prod_n (\mathcal{F}_n)_0 = 0$.

### Lean

Mathlib has a full theory of presheaves and sheaves on topological spaces with values in a category, in `Mathlib/Topology/Sheaves`. A presheaf is `TopCat.Presheaf C X`, the sheaf condition `TopCat.Presheaf.IsSheaf` is stated with limits, and `TopCat.Presheaf.isSheaf_iff_isSheafUniqueGluing` translates it into locality and gluing for concrete categories. The consequences `TopCat.Sheaf.existsUnique_gluing` and `TopCat.Sheaf.eq_of_locally_eq` are the two axioms in use. Stalks and germs are `TopCat.Presheaf.stalk` and `TopCat.Presheaf.germ`, the skyscraper sheaf is `skyscraperSheaf`, and the theorem of this section is in `Mathlib/Topology/Sheaves/Stalks.lean`. The sheaf $\mathcal{O}_X(D)$ of a Weil divisor is not in Mathlib in this form. The handbook adds no `MinimalModel` node here.

### Notes and history

Leray introduced sheaves in 1946, for the cohomology of a space relative to a map, with a definition close to the étalé spaces of Section 5.2. Cartan's seminar of 1950 to 1951 gave the definition used today, and Serre's paper *Faisceaux algébriques cohérents* of 1955 brought sheaves into algebraic geometry with the Zariski topology. The description of a sheaf as a functor on open sets with the gluing condition, and the view of sheaves as objects of a category, are in Grothendieck's Tohoku paper of 1957 and in Godement's book of 1958.
