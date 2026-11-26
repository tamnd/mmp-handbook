---
title: Quasi-coherent and locally free sheaves
nodes: []
sources: [Har77, Vak25, Stacks, Ser55]
reads_with: [Har77:ch2, Vak25:ch2]
requires: [P1.1, P2.5, P2.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Quasi-coherent and locally free sheaves

### Statement

Let $(X, \mathcal{O}_X)$ be a ringed space and $\mathcal{F}$ an $\mathcal{O}_X$-module. By Proposition P2.6.4, a map $\mathcal{O}_X^{(I)} \to \mathcal{F}$ is a family $(s_i)_{i \in I}$ of global sections. The family *generates* $\mathcal{F}$ if the map is surjective, that is, if the germs $s_{i,x}$ generate every stalk $\mathcal{F}_x$.

**Definition P2.6.26 (finiteness conditions).** The $\mathcal{O}_X$-module $\mathcal{F}$ is

1. *of finite type* if every point has an open neighbourhood $U$ with a surjection $\mathcal{O}_U^n \to \mathcal{F}|_U$ for some $n$;
2. *quasi-coherent* if every point has an open neighbourhood $U$ with an exact sequence $\mathcal{O}_U^{(J)} \to \mathcal{O}_U^{(I)} \to \mathcal{F}|_U \to 0$, for some sets $I$ and $J$;
3. *of finite presentation* if the same holds with $I$ and $J$ finite;
4. *locally free* if every point has an open neighbourhood $U$ with $\mathcal{F}|_U \cong \mathcal{O}_U^{(I)}$. It is *locally free of rank $r$* if $I$ can be taken with $r$ elements for every point. An *invertible sheaf*, or *line bundle*, is a locally free sheaf of rank $1$.

Lean: Mathlib `SheafOfModules.IsFiniteType`, `SheafOfModules.IsQuasicoherent` (with the data `SheafOfModules.QuasicoherentData` and `SheafOfModules.Presentation`), `SheafOfModules.QuasicoherentData.IsFinitePresentation` and `SheafOfModules.IsLocallyFree`.

On a scheme the quasi-coherent sheaves are those of the form $\widetilde{M}$ on every affine open set, and a coherent sheaf on a noetherian scheme is a quasi-coherent sheaf of finite type (P3 Ch. 5). On a general ringed space the definition above is the right one, and this section uses only it.

**Proposition P2.6.27 (stability).** Let $\mathcal{F}$ and $\mathcal{G}$ be $\mathcal{O}_X$-modules and $f: Y \to X$ a morphism of ringed spaces.

1. A locally free sheaf is quasi-coherent. A locally free sheaf of rank $r$ is of finite presentation.
2. If $\mathcal{F}$ is of finite type, quasi-coherent, of finite presentation, locally free, or locally free of rank $r$, then $f^* \mathcal{F}$ has the same property.
3. If $\mathcal{F}$ and $\mathcal{G}$ are quasi-coherent, then so are $\mathcal{F} \oplus \mathcal{G}$ and $\mathcal{F} \otimes \mathcal{G}$. The same holds for finite presentation and for locally free sheaves of finite rank.
4. If $\mathcal{F}$ is of finite type, the natural map $\mathcal{H}om(\mathcal{F}, \mathcal{G})_x \to \operatorname{Hom}_{\mathcal{O}_{X,x}}(\mathcal{F}_x, \mathcal{G}_x)$ is injective for every $x$. If $\mathcal{F}$ is of finite presentation, it is an isomorphism.

Lean: Mathlib has the instance that a locally free sheaf is quasi-coherent, in `Mathlib/Algebra/Category/ModuleCat/Sheaf/LocallyFree.lean`, and `SheafOfModules.Presentation.map` for presentations under a functor. Parts 3 and 4 are not in Lean as stated.

**Proposition P2.6.28 (transition functions).** Let $\mathcal{E}$ be locally free of rank $r$, $(U_i)$ an open cover and $\varphi_i: \mathcal{E}|_{U_i} \to \mathcal{O}_{U_i}^r$ isomorphisms. Then $g_{ij} = \varphi_i \circ \varphi_j^{-1}$ is an invertible $r \times r$ matrix of functions on $U_{ij} = U_i \cap U_j$, and
$$g_{ii} = 1, \qquad g_{ij} g_{jk} = g_{ik} \text{ on } U_{ijk}.$$
Conversely, every family $g_{ij} \in \mathrm{GL}_r(\mathcal{O}_X(U_{ij}))$ that satisfies these conditions comes from a locally free sheaf of rank $r$, unique up to isomorphism. Two families $(g_{ij})$ and $(g'_{ij})$ on the same cover give isomorphic sheaves if and only if there are $h_i \in \mathrm{GL}_r(\mathcal{O}_X(U_i))$ with $g'_{ij} = h_i g_{ij} h_j^{-1}$.

Lean: not in Lean as stated.

For $r = 1$ the matrices are units $g_{ij} \in \mathcal{O}_X(U_{ij})^\times$, and the proposition says that line bundles trivial on the $U_i$ correspond to Čech $1$-cocycles of $\mathcal{O}_X^\times$ modulo coboundaries. Chapter 7 turns this into $\operatorname{Pic}(X) \cong H^1(X, \mathcal{O}_X^\times)$.

**Theorem P2.6.29 (line bundles and the Picard group).** Let $\mathcal{L}$ and $\mathcal{M}$ be invertible sheaves and $\mathcal{E}$ a locally free sheaf of finite rank.

1. $\mathcal{L} \otimes \mathcal{M}$ and $\mathcal{L}^\vee$ are invertible, and the evaluation map $\mathcal{L} \otimes \mathcal{L}^\vee \to \mathcal{O}_X$, $s \otimes \varphi \mapsto \varphi(s)$, is an isomorphism.
2. The isomorphism classes of invertible sheaves form an abelian group $\operatorname{Pic}(X)$, the *Picard group*, with product $\otimes$, identity $\mathcal{O}_X$ and inverse $\mathcal{L}^{-1} = \mathcal{L}^\vee$.
3. A morphism $f: Y \to X$ induces a group homomorphism $f^*: \operatorname{Pic}(X) \to \operatorname{Pic}(Y)$.
4. The natural maps $\mathcal{E}^\vee \otimes \mathcal{G} \to \mathcal{H}om(\mathcal{E}, \mathcal{G})$ and $\mathcal{E} \to \mathcal{E}^{\vee\vee}$ are isomorphisms, and $\mathcal{E}^\vee$ is locally free of the same rank.

Lean: Mathlib `CommRing.Pic` is the Picard group of a commutative ring, the group of invertible modules `Module.Invertible`; the Picard group of a ringed space is not in Lean as stated.

**Theorem P2.6.30 (projection formula).** Let $f: X \to Y$ be a morphism of ringed spaces, $\mathcal{F}$ an $\mathcal{O}_X$-module and $\mathcal{E}$ a locally free $\mathcal{O}_Y$-module of finite rank. There is a natural isomorphism
$$f_* \mathcal{F} \otimes_{\mathcal{O}_Y} \mathcal{E} \cong f_*(\mathcal{F} \otimes_{\mathcal{O}_X} f^* \mathcal{E}).$$
In particular, if $f_* \mathcal{O}_X = \mathcal{O}_Y$, then $f_* f^* \mathcal{E} \cong \mathcal{E}$, $\Gamma(X, f^* \mathcal{E}) \cong \Gamma(Y, \mathcal{E})$, and $f^*: \operatorname{Pic}(Y) \to \operatorname{Pic}(X)$ is injective.

Lean: not in Lean as stated.

### Proof in words

Every property in the definition is local and is stated by free modules, so it is kept by every functor that is right exact, commutes with direct sums and sends $\mathcal{O}$ to $\mathcal{O}$. Pullback and tensor product are such functors. For Hom, a presentation of $\mathcal{F}$ turns $\mathcal{H}om(\mathcal{F}, \mathcal{G})$ into a kernel of a map $\mathcal{G}^n \to \mathcal{G}^m$, and stalks commute with kernels and finite sums. A locally free sheaf is glued from free pieces, and the gluing maps are the transition matrices. For line bundles, every claim is local, and on a small open set every line bundle is $\mathcal{O}$, where the claims are clear. The projection formula comes from a natural map that is an isomorphism for $\mathcal{E} = \mathcal{O}_Y$, hence for $\mathcal{E} = \mathcal{O}_Y^r$, hence for every locally free $\mathcal{E}$ of finite rank, since the question is local on $Y$.

### Examples

**Example P2.6.31 (the Picard group of $\mathbb{P}^1$).** The sheaves $\mathcal{O}(n)$ of Example P2.6.9 are invertible, with transition function $g_{01} = t^n$ on $U_{01}$. By Example P2.6.16, $\mathcal{O}(a) \otimes \mathcal{O}(b) \cong \mathcal{O}(a+b)$, so $n \mapsto \mathcal{O}(n)$ is a group homomorphism $\mathbb{Z} \to \operatorname{Pic}(\mathbb{P}^1)$. It is injective. If $\mathcal{O}(n) \cong \mathcal{O}$ with $n \neq 0$, then either $n > 0$ and $\dim \Gamma(\mathcal{O}(n)) = n + 1 \neq 1$, or $n < 0$ and $\Gamma(\mathcal{O}(n)) = 0 \neq k$, by Example P2.6.9. So the $\mathcal{O}(n)$ are pairwise non-isomorphic. Chapter 7 shows by a Čech computation that every line bundle on $\mathbb{P}^1$ is one of them.

**Example P2.6.32 (quasi-coherent sheaves on an affine scheme).** Let $M$ be a module over a ring $A$, with a presentation $A^{(J)} \to A^{(I)} \to M \to 0$. P3 Ch. 5 shows that $M \mapsto \widetilde{M}$ is exact and commutes with direct sums, with $\widetilde{A} = \mathcal{O}_{\operatorname{Spec} A}$. So $\mathcal{O}^{(J)} \to \mathcal{O}^{(I)} \to \widetilde{M} \to 0$ is exact, and $\widetilde{M}$ is quasi-coherent in the sense of Definition P2.6.26. It is of finite presentation if $M$ is finitely presented, and locally free if $M$ is projective. P3 Ch. 5 proves the converse: every quasi-coherent sheaf on $\operatorname{Spec} A$ has the form $\widetilde{M}$.

**Example P2.6.33 (a sheaf that is not quasi-coherent).** Let $X = \mathbb{A}^1$ over a field, $U = X \setminus \{0\}$, $j: U \to X$ the inclusion and $\mathcal{F} = j_! \mathcal{O}_U$, the extension by zero of Section 5.4. It is an $\mathcal{O}_X$-module with $\mathcal{F}_x = \mathcal{O}_{X,x}$ for $x \neq 0$ and $\mathcal{F}_0 = 0$. A section of $\mathcal{F}$ over an open $W \ni 0$ is a regular function on $W \setminus \{0\}$ that vanishes near $0$. Since $W \setminus \{0\}$ is irreducible, a regular function that vanishes on a nonempty open subset vanishes, so $\Gamma(W, \mathcal{F}) = 0$. If $\mathcal{F}$ were quasi-coherent, there would be an open $W \ni 0$ and a surjection $\mathcal{O}_W^{(I)} \to \mathcal{F}|_W$. By Proposition P2.6.4 this map is given by sections in $\Gamma(W, \mathcal{F}) = 0$, so it is zero, and $\mathcal{F}|_W = 0$. This is false, since $W$ contains points $x \neq 0$ with $\mathcal{F}_x \neq 0$. So $\mathcal{F}$ is not quasi-coherent. It is a subsheaf of $\mathcal{O}_X$, so subsheaves of quasi-coherent sheaves need not be quasi-coherent.

**Example P2.6.34 (Hom and stalks).** Let $X = \mathbb{R}$ with its sheaf $C_X$ of continuous functions and $\mathcal{F} = C_X^{(\mathbb{N})}$, a free module that is not of finite type. Then $\mathcal{H}om(\mathcal{F}, C_X) \cong \prod_{n} C_X$. Let $f_n(x) = \max(|x| - 1/n, 0)$. The family $(f_n)$ is a section of $\prod_n C_X$ over $\mathbb{R}$. Each $f_n$ vanishes on $(-1/n, 1/n)$, so its image in $\operatorname{Hom}(\mathcal{F}_0, C_{X,0}) = \prod_n C_{X,0}$ is $0$. But on every neighbourhood of $0$ some $f_n$ is not zero, so the germ of $(f_n)$ at $0$ is not zero. So the map of part 4 is not injective without a finiteness hypothesis.

**Example P2.6.35 (a divisor that is $\mathbb{Q}$-Cartier but not Cartier).** Let $k$ be a field and $X = \operatorname{Spec} A$ the quadric cone, $A = k[x, y, z]/(x y - z^2)$, a normal surface (P3 Ch. 8). Let $D$ be the line $x = z = 0$, a prime divisor through the vertex $0$. Its ideal is $\mathfrak{p} = (x, z)$, a prime with $A/\mathfrak{p} = k[y]$. By Example P2.6.10, $\mathcal{O}_X(-D)$ is the ideal sheaf $\widetilde{\mathfrak{p}}$, and its fibre at the vertex is $\mathfrak{p}/\mathfrak{m} \mathfrak{p}$ with $\mathfrak{m} = (x, y, z)$. The ring $A$ is graded with $x, y, z$ of degree $1$, $\mathfrak{p}$ is generated by $x$ and $z$ in degree $1$, and $\mathfrak{m} \mathfrak{p}$ lies in degrees at least $2$. So the images of $x$ and $z$ in $\mathfrak{p}/\mathfrak{m} \mathfrak{p}$ are independent, and the fibre has dimension $2$. By Nakayama's lemma, $\mathfrak{p}_{\mathfrak{m}}$ is not generated by one element, so $\mathcal{O}_X(-D)$ is not invertible near the vertex, and $D$ is not Cartier. On the other hand, $\operatorname{div}(x) = 2D$. Indeed $x = 0$ forces $z^2 = 0$, so $x$ vanishes exactly on $D$. At the generic point of $D$ the function $y$ is a unit, $z$ is a uniformizer, and $x = z^2/y$ has order $2$. So $\mathcal{O}_X(-2D) = x \mathcal{O}_X$ is invertible, and $2D$ is Cartier. The divisor $D$ is $\mathbb{Q}$-Cartier of index $2$. The cone is the simplest klt singularity that is not smooth, and this example is the model for the index of $K_X$ in Volume 1.

### Proof

*Proposition P2.6.27.* Part 1. If $\mathcal{F}|_U \cong \mathcal{O}_U^{(I)}$, then $0 \to \mathcal{O}_U^{(I)} \to \mathcal{F}|_U \to 0$ is a presentation with $J$ empty.

Part 2. The functor $f^*$ commutes with restriction to open sets: for $V \subseteq X$ open, $(f^* \mathcal{F})|_{f^{-1} V} \cong (f|_{f^{-1} V})^* (\mathcal{F}|_V)$, since inverse image, tensor product and sheafification are all compatible with restriction. It is right exact and sends $\mathcal{O}_V^{(I)}$ to $\mathcal{O}_{f^{-1} V}^{(I)}$ (Theorem P2.6.19). So it sends a surjection $\mathcal{O}_V^n \to \mathcal{F}|_V$, a presentation of $\mathcal{F}|_V$, or an isomorphism $\mathcal{F}|_V \cong \mathcal{O}_V^{(I)}$ to the same kind of object over $f^{-1}(V)$. The sets $f^{-1}(V)$ cover $Y$.

Part 3. Let $x \in X$. Choose a neighbourhood $U$ of $x$ on which both sheaves have presentations $\mathcal{A}_1 \to \mathcal{A}_0 \to \mathcal{F}|_U \to 0$ and $\mathcal{B}_1 \to \mathcal{B}_0 \to \mathcal{G}|_U \to 0$ with free $\mathcal{A}_i$ and $\mathcal{B}_i$. This is possible because the intersection of two neighbourhoods is a neighbourhood. The direct sum of the two sequences is a presentation of $\mathcal{F} \oplus \mathcal{G}$ on $U$. For the tensor product, the sequence
$$(\mathcal{A}_1 \otimes \mathcal{B}_0) \oplus (\mathcal{A}_0 \otimes \mathcal{B}_1) \to \mathcal{A}_0 \otimes \mathcal{B}_0 \to \mathcal{F} \otimes \mathcal{G} \to 0$$
is exact on $U$. To see this, check it on stalks with part 2 of Theorem P2.6.13: it is the standard presentation of the tensor product of two presented modules, which follows from right exactness of $- \otimes N$ in each variable (Proposition P2.2.30). The tensor product of free modules is free, $\mathcal{O}^{(I)} \otimes \mathcal{O}^{(I')} \cong \mathcal{O}^{(I \times I')}$, since $\otimes$ commutes with direct sums. So $\mathcal{F} \otimes \mathcal{G}$ is quasi-coherent, and of finite presentation if both are. If $\mathcal{F}|_U \cong \mathcal{O}_U^r$ and $\mathcal{G}|_U \cong \mathcal{O}_U^s$, then $(\mathcal{F} \otimes \mathcal{G})|_U \cong \mathcal{O}_U^{rs}$.

Part 4. The question is local, so suppose there is an exact sequence $\mathcal{O}^m \to \mathcal{O}^n \to \mathcal{F} \to 0$ on $X$, with $m = 0$ allowed if only a surjection $\mathcal{O}^n \to \mathcal{F}$ is given. By part 4 of Theorem P2.6.13 and part 5 there, applying $\mathcal{H}om(-, \mathcal{G})$ gives an exact sequence
$$0 \to \mathcal{H}om(\mathcal{F}, \mathcal{G}) \to \mathcal{G}^n \to \mathcal{G}^m.$$
Taking stalks is exact, so $0 \to \mathcal{H}om(\mathcal{F}, \mathcal{G})_x \to \mathcal{G}_x^n \to \mathcal{G}_x^m$ is exact. The stalk sequence $\mathcal{O}_x^m \to \mathcal{O}_x^n \to \mathcal{F}_x \to 0$ is exact, and applying $\operatorname{Hom}_{\mathcal{O}_x}(-, \mathcal{G}_x)$ gives an exact sequence $0 \to \operatorname{Hom}(\mathcal{F}_x, \mathcal{G}_x) \to \mathcal{G}_x^n \to \mathcal{G}_x^m$. The natural map of the proposition commutes with the maps to $\mathcal{G}_x^n$. Both of these maps are injective, so the natural map is injective. If a presentation exists, both groups are the kernel of the same map $\mathcal{G}_x^n \to \mathcal{G}_x^m$, so the natural map is an isomorphism. $\square$

*Proposition P2.6.28.* The composite $\varphi_i \varphi_j^{-1}$ is an automorphism of $\mathcal{O}_{U_{ij}}^r$, which is an invertible matrix of functions by Proposition P2.6.4. The identities $\varphi_i \varphi_i^{-1} = 1$ and $(\varphi_i \varphi_j^{-1})(\varphi_j \varphi_k^{-1}) = \varphi_i \varphi_k^{-1}$ give the cocycle conditions. Conversely, given a cocycle, Theorem P2.5.35 glues the sheaves $\mathcal{O}_{U_i}^r$ along the isomorphisms $g_{ij}$ to a sheaf $\mathcal{E}$ with isomorphisms $\mathcal{E}|_{U_i} \cong \mathcal{O}_{U_i}^r$. The gluing maps are $\mathcal{O}$-linear, so the glued sheaf is an $\mathcal{O}_X$-module: a section is a family of sections $s_i$ of $\mathcal{O}_{U_i}^r$ with $s_i = g_{ij} s_j$, and multiplication by a function keeps this condition. Uniqueness up to isomorphism is the uniqueness part of Theorem P2.5.35. An isomorphism $\psi: \mathcal{E} \to \mathcal{E}'$ between two glued sheaves is given on $U_i$ by $h_i = \varphi'_i \psi \varphi_i^{-1}$, and $\psi$ is compatible with the gluing if and only if $g'_{ij} h_j = h_i g_{ij}$. $\square$

*Theorem P2.6.29.* Part 1. On a neighbourhood $U$ of a point where $\mathcal{L}|_U \cong \mathcal{O}_U$ and $\mathcal{M}|_U \cong \mathcal{O}_U$, part 5 of Theorem P2.6.13 gives $(\mathcal{L} \otimes \mathcal{M})|_U \cong \mathcal{O}_U$ and $\mathcal{L}^\vee|_U \cong \mathcal{H}om(\mathcal{O}_U, \mathcal{O}_U) \cong \mathcal{O}_U$. The evaluation map is defined on the presheaf tensor product and sheafified. On $U$, under these isomorphisms, it is the multiplication map $\mathcal{O}_U \otimes \mathcal{O}_U \to \mathcal{O}_U$, an isomorphism. An isomorphism is a local property, by Theorem P2.5.5.

Part 2. Associativity, commutativity and the unit come from part 5 of Theorem P2.6.13, and inverses from part 1. The isomorphism classes form a set, because every invertible sheaf is glued from the sheaves $\mathcal{O}_{U_i}$ along units on some open cover, by Proposition P2.6.28.

Part 3. By Proposition P2.6.27, $f^*$ sends invertible sheaves to invertible sheaves, and by part 4 of Theorem P2.6.19 it commutes with tensor products.

Part 4. The map $\mathcal{E}^\vee \otimes \mathcal{G} \to \mathcal{H}om(\mathcal{E}, \mathcal{G})$ sends $\varphi \otimes g$ to $e \mapsto \varphi(e) g$, and $\mathcal{E} \to \mathcal{E}^{\vee\vee}$ sends $e$ to $\varphi \mapsto \varphi(e)$. Both are natural and additive in $\mathcal{E}$ and commute with restriction. Locally $\mathcal{E} \cong \mathcal{O}^r$, and both maps become the identity of $\mathcal{G}^r$ and of $\mathcal{O}^r$ after the isomorphisms of Exercise 1 of Section 6.2. So they are isomorphisms. The dual $\mathcal{E}^\vee$ is locally $(\mathcal{O}^r)^\vee \cong \mathcal{O}^r$. $\square$

*Theorem P2.6.30.* First build a natural map. For $\mathcal{O}_X$-modules $\mathcal{P}$ and $\mathcal{Q}$, the maps
$$\mathcal{P}(f^{-1} V) \otimes_{\mathcal{O}_Y(V)} \mathcal{Q}(f^{-1} V) \to (\mathcal{P} \otimes_{\mathcal{O}_X} \mathcal{Q})(f^{-1} V), \qquad p \otimes q \mapsto p \otimes q,$$
are well defined, because $\mathcal{O}_Y(V)$ acts through $\mathcal{O}_X(f^{-1} V)$. They commute with restriction, and sheafify to a map $\mu: f_* \mathcal{P} \otimes f_* \mathcal{Q} \to f_*(\mathcal{P} \otimes \mathcal{Q})$. Define the map of the theorem as the composite
$$f_* \mathcal{F} \otimes \mathcal{E} \xrightarrow{1 \otimes \eta} f_* \mathcal{F} \otimes f_* f^* \mathcal{E} \xrightarrow{\mu} f_*(\mathcal{F} \otimes f^* \mathcal{E}),$$
where $\eta$ is the unit of the adjunction of Theorem P2.6.19. It is natural in $\mathcal{E}$ and commutes with restriction to an open $V \subseteq Y$ and to $f^{-1}(V)$. So it suffices to prove that it is an isomorphism on each $V$ of an open cover of $Y$, and to take $V$ with $\mathcal{E}|_V \cong \mathcal{O}_V^r$. For $\mathcal{E} = \mathcal{O}_Y$, the unit is $f^\#: \mathcal{O}_Y \to f_* \mathcal{O}_X$, and the composite is the isomorphism $f_* \mathcal{F} \otimes \mathcal{O}_Y \cong f_* \mathcal{F} \cong f_*(\mathcal{F} \otimes \mathcal{O}_X)$ of part 5 of Theorem P2.6.13. Both sides are additive functors of $\mathcal{E}$ and commute with finite direct sums, since $f^*$, $f_*$ and $\otimes$ do. So the map is an isomorphism for $\mathcal{E} = \mathcal{O}_Y^r$.

If $f_* \mathcal{O}_X = \mathcal{O}_Y$, take $\mathcal{F} = \mathcal{O}_X$: then $f_* f^* \mathcal{E} \cong f_* \mathcal{O}_X \otimes \mathcal{E} = \mathcal{E}$, and taking global sections gives $\Gamma(X, f^* \mathcal{E}) = \Gamma(Y, f_* f^* \mathcal{E}) \cong \Gamma(Y, \mathcal{E})$. If $f^* \mathcal{L} \cong \mathcal{O}_X$ for an invertible $\mathcal{L}$, then $\mathcal{L} \cong f_* f^* \mathcal{L} \cong f_* \mathcal{O}_X = \mathcal{O}_Y$, so $f^*$ is injective on $\operatorname{Pic}$. $\square$

### Exercises

1. (A) Show that the rank of a locally free sheaf of finite rank is a locally constant function on $X$, so it is constant on a connected space. Show that for a locally ringed space the rank at $x$ is $\dim_{\kappa(x)} \mathcal{E}(x)$.
2. (A) Let $\mathcal{L}$ be invertible with transition functions $g_{ij}$. Show that $\mathcal{L}^\vee$ has transition functions $g_{ij}^{-1}$ and $\mathcal{L} \otimes \mathcal{M}$ has transition functions $g_{ij} h_{ij}$, where $h_{ij}$ are those of $\mathcal{M}$ on the same cover.
3. (A) On $\mathbb{P}^1$, show that $\mathcal{O}(n)^\vee \cong \mathcal{O}(-n)$ and $\mathcal{H}om(\mathcal{O}(a), \mathcal{O}(b)) \cong \mathcal{O}(b - a)$. Compute $\dim_k \operatorname{Hom}(\mathcal{O}(a), \mathcal{O}(b))$ for all $a, b$.
4. (B) Let $X$ be a locally ringed space and $\mathcal{F}$ of finite type. Show that the support $\{ x : \mathcal{F}_x \neq 0 \}$ is closed, and that $x \mapsto \dim_{\kappa(x)} \mathcal{F}(x)$ is upper semicontinuous. (Hint: lift a basis of $\mathcal{F}(x)$ to sections near $x$ and use Nakayama's lemma.)
5. (B) Let $X$ be a locally ringed space and $\mathcal{F}$ of finite presentation with $\mathcal{F}_x \cong \mathcal{O}_{X,x}^r$. Show that $\mathcal{F}|_U \cong \mathcal{O}_U^r$ on some neighbourhood $U$ of $x$. (Hint: lift a basis of $\mathcal{F}_x$ to sections on a neighbourhood, and show that the kernel and cokernel of the resulting map $\mathcal{O}_U^r \to \mathcal{F}|_U$ vanish near $x$, using that the kernel is of finite type by the presentation.)
6. (B) Let $p: \{\mathrm{pt}\} \to \mathbb{P}^1$ be the inclusion of a closed point. Show that $p^* \mathcal{O}(n)$ is trivial for all $n$, so $p^*: \operatorname{Pic}(\mathbb{P}^1) \to \operatorname{Pic}(\mathrm{pt})$ is not injective. Which hypothesis of Theorem P2.6.30 fails?
7. (C) Let $A$ be a local ring and $L$, $L'$ finitely generated $A$-modules with $L \otimes_A L' \cong A$. Show that $L \cong A$. (Hint: tensor with the residue field and use Nakayama's lemma, then show that a surjection $A \to L$ is injective.) Deduce that if $\mathcal{L}$ and $\mathcal{L}'$ are $\mathcal{O}_X$-modules of finite presentation on a locally ringed space with $\mathcal{L} \otimes \mathcal{L}' \cong \mathcal{O}_X$, then $\mathcal{L}$ is invertible.

### Lean

Mathlib defines finite type, quasi-coherence and local freeness for sheaves of modules on a site: `SheafOfModules.IsFiniteType`, `SheafOfModules.IsQuasicoherent`, `SheafOfModules.IsLocallyFree`, with the data `SheafOfModules.QuasicoherentData`, `SheafOfModules.Presentation` and the finiteness condition `SheafOfModules.QuasicoherentData.IsFinitePresentation`. The implication from locally free to quasi-coherent is an instance. The Picard group of a commutative ring is `CommRing.Pic`, built from `Module.Invertible`. Transition functions, the Picard group of a ringed space, the stalk formula for $\mathcal{H}om$ and the projection formula are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Serre introduced coherent sheaves in *Faisceaux algébriques cohérents*. The definitions of quasi-coherent sheaves and of sheaves of finite presentation on an arbitrary ringed space are from EGA 0. The correspondence between vector bundles and locally free sheaves through transition functions goes back to the topology of fibre bundles. The projection formula has a derived form, $\mathbf{R} f_* \mathcal{F} \otimes^{\mathbf{L}} \mathcal{E} \cong \mathbf{R} f_*(\mathcal{F} \otimes^{\mathbf{L}} \mathbf{L} f^* \mathcal{E})$, stated in Chapter 8. Its consequence $\Gamma(X, f^* \mathcal{L}) = \Gamma(Y, \mathcal{L})$ for $f_* \mathcal{O}_X = \mathcal{O}_Y$ is used in the minimal model program every time a line bundle is pulled back along a contraction.
