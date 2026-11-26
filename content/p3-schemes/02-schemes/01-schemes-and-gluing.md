---
title: Schemes and gluing
nodes: []
sources: [Vak25, Har77, GW20, EGA1, Stacks]
reads_with: [Vak25:ch4, Har77:II.2, GW20:ch3]
requires: [P2.5, P2.6, P3.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Schemes and gluing

### Statement

**Definition P3.2.1 (scheme).** A *scheme* is a locally ringed space $(X, \mathcal{O}_X)$ in which every point has an open neighbourhood $U$ such that $(U, \mathcal{O}_X|_U)$ is an affine scheme. A *morphism of schemes* is a morphism of locally ringed spaces. An open set $U$ with $(U, \mathcal{O}_X|_U)$ affine is an *affine open set*. Schemes and their morphisms form a category $\mathsf{Sch}$.

So affine schemes are a full subcategory of schemes, and by Corollary P3.1.23 it is equivalent to $\mathsf{Ring}^{\mathrm{op}}$. For a scheme $X$ and an open set $U$, write $\Gamma(U, \mathcal{O}_X)$ or $\mathcal{O}_X(U)$ for the ring of sections.

Lean: Mathlib `AlgebraicGeometry.Scheme` (a structure that extends `LocallyRingedSpace` with an affine cover).

**Proposition P3.2.2 (open subschemes).** Let $X$ be a scheme and $U \subseteq X$ an open set. Then $(U, \mathcal{O}_X|_U)$ is a scheme, the *open subscheme* on $U$. The affine open subsets of $X$ form a basis of the topology. A morphism $j \colon Y \to X$ that is an isomorphism onto an open subscheme is an *open immersion*.

Lean: Mathlib `AlgebraicGeometry.Scheme.restrict`, `AlgebraicGeometry.IsOpenImmersion` and `AlgebraicGeometry.Scheme.isBasis_affineOpens` (proved in Mathlib).

**Theorem P3.2.3 (gluing schemes).** Let $(X_i)_{i \in I}$ be schemes. For all $i, j$ let $U_{ij} \subseteq X_i$ be open, and let $\varphi_{ij} \colon U_{ij} \to U_{ji}$ be isomorphisms of schemes such that:

1. $U_{ii} = X_i$ and $\varphi_{ii} = 1$;
2. $\varphi_{ij}(U_{ij} \cap U_{ik}) = U_{ji} \cap U_{jk}$ for all $i, j, k$;
3. $\varphi_{jk} \circ \varphi_{ij} = \varphi_{ik}$ on $U_{ij} \cap U_{ik}$ (the cocycle condition).

Then there are a scheme $X$ and open immersions $\psi_i \colon X_i \to X$ such that the sets $\psi_i(X_i)$ cover $X$, $\psi_i(U_{ij}) = \psi_i(X_i) \cap \psi_j(X_j)$, and $\psi_j \circ \varphi_{ij} = \psi_i$ on $U_{ij}$. The scheme $X$ with the maps $\psi_i$ is unique up to a unique isomorphism.

Lean: Mathlib `AlgebraicGeometry.Scheme.GlueData`, with the glued scheme `AlgebraicGeometry.Scheme.GlueData.glued` (proved in Mathlib).

**Proposition P3.2.4 (gluing morphisms).** Let $X$ and $Y$ be schemes and $X = \bigcup_i V_i$ an open cover. Let $f_i \colon V_i \to Y$ be morphisms with $f_i|_{V_i \cap V_j} = f_j|_{V_i \cap V_j}$ for all $i, j$. Then there is exactly one morphism $f \colon X \to Y$ with $f|_{V_i} = f_i$ for all $i$. In other words, $U \mapsto \operatorname{Hom}(U, Y)$ is a sheaf of sets on $X$.

Lean: Mathlib `AlgebraicGeometry.Scheme.Cover.glueMorphisms` for existence and `AlgebraicGeometry.Scheme.Cover.hom_ext` for uniqueness (proved in Mathlib).

### Proof in words

A scheme is glued from affine schemes, and gluing works because both the space and the sheaf can be glued. The space is the disjoint union of the $X_i$ modulo the relation $x \sim \varphi_{ij}(x)$; the cocycle condition makes this an equivalence relation. The sheaf is glued by Theorem P2.5.35. The glued space is locally ringed because each point has a neighbourhood isomorphic to an open set of some $X_i$, and it is a scheme for the same reason.

Gluing morphisms is a statement about sheaves too. The continuous maps glue, and the maps of sheaves glue, because a map of sheaves is determined on an open cover.

### Examples

**Example P3.2.5 (the affine line with a doubled origin).** Let $k$ be a field, $X_1 = X_2 = \mathbb{A}^1_k = \operatorname{Spec} k[x]$, $U_{12} = U_{21} = D(x) = \operatorname{Spec} k[x, x^{-1}]$ and $\varphi_{12} = \varphi_{21} = 1$. The conditions of the theorem hold trivially, and the glued scheme $X$ is the line with two origins $0_1, 0_2$. Every other point lies in both charts.

The global functions are pairs $(f_1, f_2)$ in $k[x] \times k[x]$ with the same image in $k[x, x^{-1}]$. Since $k[x] \to k[x, x^{-1}]$ is injective, $f_1 = f_2$, so $\Gamma(X, \mathcal{O}_X) = k[x]$. The map $c_X \colon X \to \operatorname{Spec} k[x]$ of Corollary P3.1.24 sends $0_1$ and $0_2$ to $(x)$, because $x$ vanishes at both. So $c_X$ is not injective, and $X$ is not affine. Both inclusions $\mathbb{A}^1_k \to X$ are open immersions, and they agree on the dense open set $D(x)$ without being equal. Chapter 4 shows that this cannot happen for maps into a separated scheme.

**Example P3.2.6 (the projective line).** Let $X_1 = \operatorname{Spec} k[x]$, $X_2 = \operatorname{Spec} k[y]$, $U_{12} = D(x) = \operatorname{Spec} k[x, x^{-1}]$, $U_{21} = D(y) = \operatorname{Spec} k[y, y^{-1}]$, and let $\varphi_{12}$ be the isomorphism of the ring map $k[y, y^{-1}] \to k[x, x^{-1}]$, $y \mapsto x^{-1}$. The glued scheme is $\mathbb{P}^1_k$. A global function is a pair $(f(x), g(y))$ with $f(x) = g(x^{-1})$ in $k[x, x^{-1}]$. The left side has only exponents $\geq 0$ and the right side only exponents $\leq 0$, so both are a constant. So $\Gamma(\mathbb{P}^1_k, \mathcal{O}) = k$. Since $\mathbb{P}^1_k$ has infinitely many points and $\operatorname{Spec} k$ has one, $\mathbb{P}^1_k$ is not affine. The only difference from Example P3.2.5 is the gluing map. Section 2.2 treats $\mathbb{P}^n_A$ in the same way.

**Example P3.2.7 (disjoint unions).** For schemes $X_i$, take all $U_{ij} = \emptyset$ for $i \neq j$. The glued scheme is the disjoint union $\bigsqcup_i X_i$. By Proposition P3.2.4 it is the coproduct in $\mathsf{Sch}$. A finite disjoint union of affine schemes is affine, $\operatorname{Spec} A_1 \sqcup \dots \sqcup \operatorname{Spec} A_n = \operatorname{Spec}(A_1 \times \dots \times A_n)$, by Proposition P1.2.20 and the idempotents of the product. An infinite disjoint union of nonempty schemes is not affine, since it is not quasi-compact, while $\operatorname{Spec} A$ is quasi-compact (P1 Ch. 2).

**Example P3.2.8 (the punctured plane).** The open subscheme $U = \mathbb{A}^2_k \setminus \{(x, y)\}$ is the union of the affine open sets $D(x)$ and $D(y)$, so it is a scheme by Proposition P3.2.2. Example P3.1.10 computed $\Gamma(U, \mathcal{O}) = k[x, y]$, and Example P3.1.20 showed that $U$ is not affine. So an open subscheme of an affine scheme need not be affine. The two affine charts meet in $D(xy)$, and gluing $D(x)$ and $D(y)$ along it recovers $U$.

**Example P3.2.9 (gluing two lines at a point).** Gluing is along open sets only. To identify two closed points of two lines, as in the union of the axes of Example P3.1.39, one needs a different construction: the pushout $\operatorname{Spec}(k[x] \times_k k[y])$, where $k[x] \times_k k[y]$ is the ring of pairs with the same value at $0$. This ring is $k[x, y]/(xy)$, by the map $x \mapsto (x, 0)$, $y \mapsto (0, y)$. Pushouts along closed subschemes exist in some cases, and they are not given by the gluing theorem.

### Proof

*Proof of Proposition P3.2.2.* Let $x \in U$ and let $V = \operatorname{Spec} A$ be an affine open neighbourhood of $x$ in $X$. The set $U \cap V$ is open in $\operatorname{Spec} A$, so it contains a basic open set $D(f)$ with $x \in D(f)$, since the basic open sets form a basis (Proposition P1.2.17). By Proposition P3.1.13, $(D(f), \mathcal{O}_X|_{D(f)}) \cong \operatorname{Spec} A_f$ is affine. So $U$ is a scheme, and every neighbourhood of every point contains an affine open neighbourhood of the point. $\square$

*Proof of Theorem P3.2.3.* The space. Let $\tilde X = \bigsqcup_i X_i$, and for $x \in X_i$ and $y \in X_j$ say $x \sim y$ if $x \in U_{ij}$ and $\varphi_{ij}(x) = y$. Condition 1 gives reflexivity. For symmetry, apply condition 3 with $k = i$: $\varphi_{ji} \circ \varphi_{ij} = \varphi_{ii} = 1$ on $U_{ij} = U_{ij} \cap U_{ii}$, and condition 2 with $k = i$ gives $\varphi_{ij}(U_{ij}) = U_{ji}$. For transitivity, let $x \sim y \sim z$ with $z \in X_k$. Then $y \in U_{ji} \cap U_{jk}$, so $x = \varphi_{ji}(y) \in U_{ij} \cap U_{ik}$ by condition 2, and $\varphi_{ik}(x) = \varphi_{jk}(\varphi_{ij}(x)) = z$ by condition 3. Let $X = \tilde X/\sim$ with the quotient topology and $\psi_i \colon X_i \to X$ the induced maps. For $W \subseteq X_i$ open, the preimage of $\psi_i(W)$ in $X_j$ is $\varphi_{ij}(W \cap U_{ij})$, which is open in $U_{ji}$ and so in $X_j$. So $\psi_i(W)$ is open, and $\psi_i$ is an open map. It is injective since $\varphi_{ii} = 1$ and the relation identifies no two points of the same $X_i$. So $\psi_i$ is a homeomorphism onto the open set $\psi_i(X_i)$, and $\psi_i(X_i) \cap \psi_j(X_j) = \psi_i(U_{ij})$ by the definition of the relation.

The sheaf. Write $V_i = \psi_i(X_i)$ and $\mathcal{F}_i = (\psi_i)_* \mathcal{O}_{X_i}$, a sheaf of rings on $V_i$. On $V_i \cap V_j$ the isomorphism $\varphi_{ij}$ gives an isomorphism of sheaves $\theta_{ij} \colon \mathcal{F}_j|_{V_i \cap V_j} \to \mathcal{F}_i|_{V_i \cap V_j}$, namely $\varphi_{ij}^\#$ transported by $\psi_j$. Condition 3 gives the cocycle condition $\theta_{ij} \theta_{jk} = \theta_{ik}$ on triple overlaps, since $(\varphi_{jk} \varphi_{ij})^\# = \varphi_{ij}^\# \varphi_{jk}^\#$. By Theorem P2.5.35 there is a sheaf of rings $\mathcal{O}_X$ on $X$ with isomorphisms $\mathcal{O}_X|_{V_i} \cong \mathcal{F}_i$ compatible with the $\theta_{ij}$. (The theorem is stated for sheaves of abelian groups; the same proof works for sheaves of rings, since the glued sections over $W$ are the compatible families, which form a subring of $\prod_i \mathcal{F}_i(W \cap V_i)$.)

The scheme. Each $\psi_i \colon (X_i, \mathcal{O}_{X_i}) \to (V_i, \mathcal{O}_X|_{V_i})$ is an isomorphism of ringed spaces. So the stalks of $\mathcal{O}_X$ are local rings, $X$ is a locally ringed space, and every point has a neighbourhood isomorphic to an open subscheme of some $X_i$. By Proposition P3.2.2 such a neighbourhood contains an affine open neighbourhood, so $X$ is a scheme. The identity $\psi_j \circ \varphi_{ij} = \psi_i$ on $U_{ij}$ is the compatibility of the gluing isomorphisms.

Uniqueness. Let $(X', \psi'_i)$ be another solution. Define $h_i = \psi'_i \circ \psi_i^{-1} \colon V_i \to X'$. On $V_i \cap V_j$, $h_i = h_j$ since $\psi'_j \varphi_{ij} = \psi'_i$ and $\psi_j \varphi_{ij} = \psi_i$. By Proposition P3.2.4 the $h_i$ glue to a morphism $h \colon X \to X'$, and in the same way to an inverse. Uniqueness of $h$ follows from the uniqueness in Proposition P3.2.4. $\square$

*Proof of Proposition P3.2.4.* The continuous maps $f_i$ agree on overlaps, so they define a continuous map $f \colon X \to Y$. For an open $W \subseteq Y$, the maps $f_i^\# \colon \mathcal{O}_Y(W) \to \mathcal{O}_X(f^{-1}(W) \cap V_i)$ agree on the overlaps $f^{-1}(W) \cap V_i \cap V_j$, so by the sheaf property of $\mathcal{O}_X$ they define a unique map $f^\#_W \colon \mathcal{O}_Y(W) \to \mathcal{O}_X(f^{-1}(W))$, and these maps form a morphism of sheaves $\mathcal{O}_Y \to f_* \mathcal{O}_X$. The map on the stalk at $x \in V_i$ is the stalk map of $f_i$, which is local. So $f$ is a morphism of schemes with $f|_{V_i} = f_i$. If $g$ is another such morphism, then $g$ and $f$ agree as maps of sets, and the maps $g^\#_W$ and $f^\#_W$ have the same restrictions to every $f^{-1}(W) \cap V_i$, so they are equal. $\square$

### Exercises

1. (A) Let $X$ be a scheme and $U \subseteq X$ open. Show that for every open $V \subseteq U$ the open subschemes $V$ of $U$ and $V$ of $X$ are the same, and that $U \to X$ is a morphism of schemes.
2. (A) Show that the affine line with a doubled origin is quasi-compact, and that it is irreducible.
3. (A) Glue two copies of $\operatorname{Spec} k[x, y]$ along $D(x) \cup D(y)$ by the identity. Show that the global functions of the result are $k[x, y]$ and that the result is not affine. (Use Example P3.1.10.)
4. (B) Let $A$ be a ring and $f, g \in A$ with $(f, g) = A$. Show that $\operatorname{Spec} A$ is obtained by gluing $\operatorname{Spec} A_f$ and $\operatorname{Spec} A_g$ along $\operatorname{Spec} A_{fg}$, and use this with Proposition P3.2.4 to recover the sheaf property of Theorem P3.1.3 for a cover by two basic open sets.
5. (B) Show that in Example P3.2.6 the point $(x)$ of $X_1$ and the point $(y)$ of $X_2$ are distinct points of $\mathbb{P}^1_k$, and that the complement of $X_1$ in $\mathbb{P}^1_k$ is the single point $(y)$. Show that $\mathbb{P}^1_k \setminus \{(x), (y)\} \cong \mathbb{G}_{m, k}$.
6. (B) Let $X$ be the scheme glued from $\operatorname{Spec} k[x]$ and $\operatorname{Spec} k[y]$ along $D(x)$ and $D(y)$ by $y \mapsto x$. Compute $\Gamma(X, \mathcal{O}_X)$ and compare with Example P3.2.5.
7. (C) Let $X$ be a scheme and $A$ a ring. Combine Theorem P3.1.22 with Proposition P3.2.4 to show that $\operatorname{Hom}(X, \operatorname{Spec} A) = \operatorname{Hom}(A, \Gamma(X, \mathcal{O}_X))$ directly, using an affine open cover of $X$. (This is a special case of the theorem, which holds for every locally ringed space.)

### Lean

Mathlib defines `AlgebraicGeometry.Scheme` as a locally ringed space with an affine cover, and open subschemes as `AlgebraicGeometry.Scheme.restrict` with the class `AlgebraicGeometry.IsOpenImmersion`. The affine open sets form a basis by `AlgebraicGeometry.Scheme.isBasis_affineOpens`. Gluing data are `AlgebraicGeometry.Scheme.GlueData` and the glued scheme is `AlgebraicGeometry.Scheme.GlueData.glued`; gluing morphisms along an open cover is `AlgebraicGeometry.Scheme.Cover.glueMorphisms`, with uniqueness `AlgebraicGeometry.Scheme.Cover.hom_ext`. The handbook adds no `MinimalModel` node here.

### Notes and history

Schemes and the gluing construction are in EGA I, Chapter I, where a scheme is called a "prescheme" and a scheme is a separated prescheme; the modern usage follows the second edition of EGA I and Hartshorne. Hartshorne gives the gluing of schemes as an exercise in Section II.2 and constructs the doubled origin and the projective line as examples in the same section. The literature state of every statement is theorem. Vakil develops the examples of this section in Chapter 4 and treats gluing first for sheaves and then for schemes.
