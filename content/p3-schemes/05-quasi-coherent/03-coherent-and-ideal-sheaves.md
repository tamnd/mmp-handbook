---
title: Quasi-coherent and coherent sheaves, ideal sheaves and Nakayama's lemma
nodes: []
sources: [Vak25, Har77, GW20, EGA1, Stacks]
reads_with: [Vak25:ch13, Har77:II.5, GW20:ch7]
requires: [P1.1, P1.2, P1.3, P2.6, P3.2, P3.3, P3.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Quasi-coherent and coherent sheaves, ideal sheaves and Nakayama's lemma

### Statement

Let $X$ be a scheme. By Corollary P3.5.13, a quasi-coherent sheaf on $X$ is a family of modules $\mathcal{F}(U)$ over the rings $\mathcal{O}_X(U)$ of the affine open sets, compatible with localization. Every question about kernels, cokernels and finiteness can then be asked on an affine open set and answered with modules.

**Theorem P3.5.20 (the abelian category of quasi-coherent sheaves).** Let $X$ be a scheme and $\varphi \colon \mathcal{F} \to \mathcal{G}$ a morphism of quasi-coherent sheaves.

1. The kernel, cokernel and image of $\varphi$ in $\mathsf{Mod}(\mathcal{O}_X)$ are quasi-coherent. On an affine open set $U$ they are the sheaves of the kernel, cokernel and image of $\varphi_U \colon \mathcal{F}(U) \to \mathcal{G}(U)$. So $\mathsf{QCoh}(X)$ is an abelian category, and the inclusion $\mathsf{QCoh}(X) \to \mathsf{Mod}(\mathcal{O}_X)$ is exact.
2. Arbitrary direct sums of quasi-coherent sheaves are quasi-coherent, and so is the tensor product of two quasi-coherent sheaves. On an affine open set $U$, $(\mathcal{F} \otimes \mathcal{G})(U) = \mathcal{F}(U) \otimes_{\mathcal{O}_X(U)} \mathcal{G}(U)$.

Lean: the abelian category of sheaves of modules is the Mathlib instance `Abelian (SheafOfModules R)`, and `SheafOfModules.isQuasicoherent` is the property whose full subcategory is $\mathsf{QCoh}(X)$. That this subcategory is closed under kernels and cokernels is not in Lean as stated.

Quasi-coherent sheaves are also closed under extensions in $\mathsf{Mod}(\mathcal{O}_X)$. The proof needs the vanishing of the first cohomology of a quasi-coherent sheaf on an affine scheme, and this chapter does not use the statement.

**Definition P3.5.21 (coherent sheaf).** Let $X$ be a locally Noetherian scheme. An $\mathcal{O}_X$-module is *coherent* if it is quasi-coherent and of finite type. Write $\mathsf{Coh}(X)$ for the full subcategory of coherent sheaves.

On a scheme that is not locally Noetherian, EGA and the Stacks project use a stronger definition, in which the kernel of every local map $\mathcal{O}_U^n \to \mathcal{F}|_U$ is also of finite type. On a locally Noetherian scheme the two definitions agree, and the handbook uses coherent sheaves only on locally Noetherian schemes.

**Proposition P3.5.22 (coherent sheaves on a locally Noetherian scheme).** Let $X$ be locally Noetherian and $\mathcal{F}$ quasi-coherent.

1. $\mathcal{F}$ is coherent if and only if $\mathcal{F}(U)$ is a finitely generated $\mathcal{O}_X(U)$-module for every affine open $U$, if and only if this holds for the members of one affine open cover. A coherent sheaf is of finite presentation. On $\operatorname{Spec} A$ with $A$ Noetherian, $M \mapsto \widetilde{M}$ is an equivalence between finitely generated $A$-modules and coherent sheaves.
2. Kernels, cokernels and images of morphisms of coherent sheaves are coherent, and so are finite direct sums and tensor products. So $\mathsf{Coh}(X)$ is an abelian category. A quasi-coherent subsheaf or quotient of a coherent sheaf is coherent.
3. If $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ is exact with $\mathcal{F}'$ and $\mathcal{F}''$ coherent and $\mathcal{F}$ quasi-coherent, then $\mathcal{F}$ is coherent.

Lean: not in Lean as stated. Mathlib has `SheafOfModules.IsFiniteType` and `SheafOfModules.IsFinitePresentation`, but no coherent sheaves on schemes.

**Proposition P3.5.23 (ideal sheaves and closed subschemes).** Let $X$ be a scheme.

1. Let $i \colon Z \to X$ be a closed immersion. The kernel $\mathcal{I}_Z$ of $i^\# \colon \mathcal{O}_X \to i_* \mathcal{O}_Z$ is a quasi-coherent sheaf of ideals, the *ideal sheaf* of $Z$, and $i_* \mathcal{O}_Z \cong \mathcal{O}_X / \mathcal{I}_Z$. On an affine open $U = \operatorname{Spec} A$, $\mathcal{I}_Z(U)$ is the ideal $I$ with $i^{-1}(U) \cong \operatorname{Spec} A/I$ of Theorem P3.3.10.
2. The map $Z \mapsto \mathcal{I}_Z$ is a bijection from the closed subschemes of $X$ to the quasi-coherent sheaves of ideals of $\mathcal{O}_X$. The closed subscheme of $\mathcal{I}$ has support $V(\mathcal{I}) = \operatorname{Supp}(\mathcal{O}_X/\mathcal{I})$ and structure sheaf the restriction of $\mathcal{O}_X/\mathcal{I}$ to this closed set.
3. $Z \subseteq Z'$ if and only if $\mathcal{I}_{Z'} \subseteq \mathcal{I}_Z$.
4. If $X$ is locally Noetherian, every quasi-coherent sheaf of ideals is coherent.

Lean: Mathlib `AlgebraicGeometry.Scheme.IdealSheafData` is a sheaf of ideals given by its ideals on the affine open sets, with the compatibility of part 2 of Corollary P3.5.13. The closed subscheme of $\mathcal{I}$ is `AlgebraicGeometry.Scheme.IdealSheafData.subschemeι`, the ideal sheaf of a morphism is `AlgebraicGeometry.Scheme.Hom.ker`, and `AlgebraicGeometry.Scheme.IdealSheafData.ker_subschemeι` says that the two constructions are inverse in one direction, all in Mathlib.

**Definition P3.5.24 (support, fibre and fibre dimension).** Let $\mathcal{F}$ be an $\mathcal{O}_X$-module and $x \in X$. The *support* of $\mathcal{F}$ is $\operatorname{Supp} \mathcal{F} = \{x : \mathcal{F}_x \neq 0\}$. The *fibre* of $\mathcal{F}$ at $x$ is the $\kappa(x)$-vector space $\mathcal{F}(x) = \mathcal{F}_x \otimes_{\mathcal{O}_{X,x}} \kappa(x) = \mathcal{F}_x / \mathfrak{m}_x \mathcal{F}_x$, and the *fibre dimension* is $\varphi_\mathcal{F}(x) = \dim_{\kappa(x)} \mathcal{F}(x)$.

**Proposition P3.5.25 (Nakayama's lemma for sheaves).** Let $\mathcal{F}$ be a quasi-coherent sheaf of finite type on a scheme $X$ and $x \in X$.

1. If $\mathcal{F}(x) = 0$, then $\mathcal{F}$ vanishes on a neighbourhood of $x$. In particular $\operatorname{Supp} \mathcal{F}$ is closed.
2. If $s_1, \dots, s_n$ are sections over a neighbourhood $U$ of $x$ whose images span $\mathcal{F}(x)$, then they generate $\mathcal{F}$ on a neighbourhood $V \subseteq U$ of $x$: the map $\mathcal{O}_V^n \to \mathcal{F}|_V$ is surjective.
3. The fibre dimension is upper semicontinuous: for every $n$ the set $\{y : \varphi_\mathcal{F}(y) \geq n\}$ is closed.
4. If $X$ is reduced and $\varphi_\mathcal{F}$ is locally constant, then $\mathcal{F}$ is locally free of finite rank.
5. If $\mathcal{F}$ is of finite presentation and $\mathcal{F}_x$ is a free $\mathcal{O}_{X,x}$-module, then $\mathcal{F}$ is free on a neighbourhood of $x$.

Lean: not in Lean as stated. Nakayama's lemma for modules is Mathlib `Submodule.eq_bot_of_le_smul_of_le_jacobson_bot`.

### Proof in words

All statements reduce to modules over the rings of affine open sets. A morphism of quasi-coherent sheaves is, on $\operatorname{Spec} A$, the sheaf of a module map, and $M \mapsto \widetilde{M}$ is exact. So kernels and cokernels of sheaves are the sheaves of kernels and cokernels of modules, and they are quasi-coherent. Over a Noetherian ring a submodule of a finitely generated module is finitely generated, and this gives the abelian category of coherent sheaves.

A closed subscheme is, on each affine open set, the spectrum of a quotient $A/I$. The ideals $I$ are compatible with localization, which is the statement that they form a quasi-coherent sheaf of ideals. Conversely a quasi-coherent sheaf of ideals gives quotient rings $A/I$ on each affine set, and the sheaf $\mathcal{O}_X/\mathcal{I}$ on its support is a scheme because it is $\operatorname{Spec} A/I$ on each piece.

Nakayama's lemma says that a finitely generated module over a local ring is generated by lifts of a basis of its fibre. A finite set of sections that generates the stalk at $x$ generates the module on a neighbourhood, because the cokernel is finitely generated and vanishes at $x$. So the number of generators needed near a point is at most the fibre dimension at the point, which is upper semicontinuity. If the fibre dimension is constant, the relations between the generators vanish at every point, and on a reduced scheme a function that vanishes at every point is zero.

### Examples

**Example P3.5.26 (a support that is not closed).** Let $k$ be an infinite field, $a_1, a_2, \dots \in k$ distinct, $A = k[x]$ and $M = \bigoplus_{n \geq 1} A/(x - a_n)$. Then $\widetilde{M}$ is quasi-coherent, and its support is the set of closed points $(x - a_n)$. This set is infinite, so it is not closed, since the proper closed subsets of $\mathbb{A}^1_k$ are finite. Part 1 of Proposition P3.5.25 fails because $\widetilde{M}$ is not of finite type. At the generic point, $\widetilde{M}(\eta) = M \otimes K = 0$, but $\widetilde{M}$ does not vanish on any neighbourhood of $\eta$.

**Example P3.5.27 (the fibre dimension jumps up).** Let $A = k[x, y]$ and $I = (x, y)$, as in Example P3.5.18. The fibre dimension of $\widetilde{I}$ is $2$ at the origin and $1$ at every other point, including the generic point: on $D(x)$ and $D(y)$ the sheaf is free of rank $1$. So $\{\varphi \geq 2\}$ is the origin, a closed set, as part 3 of Proposition P3.5.25 requires. The function can jump up at special points, never down. On the curve $\operatorname{Spec} k[x]$, the coherent sheaf of $M = k[x] \oplus k[x]/(x)$ has fibre dimension $2$ at the origin and $1$ elsewhere, and $\widetilde{M}$ is free on $D(x)$.

**Example P3.5.28 (part 4 needs reducedness).** Let $A = k[\epsilon]/(\epsilon^2)$ and $M = A/(\epsilon) = k$. The space $\operatorname{Spec} A$ is one point, and the fibre dimension of $\widetilde{M}$ is $1$, a constant function. But $M$ is not free: a free $A$-module of rank $r$ has dimension $2r$ over $k$, and $M$ has dimension $1$. In the proof of part 4 the relation $\epsilon$ vanishes at the point without being $0$.

**Example P3.5.29 (closed subschemes with one support).** In $\mathbb{A}^2_k$ the ideal sheaves of $(y)$, $(y^2)$ and $(y^2, xy)$ satisfy $(y^2) \subseteq (y^2, xy) \subseteq (y)$, so by part 3 of Proposition P3.5.23 the line $V(y)$ is contained in the line with an embedded point $V(y^2, xy)$ of Example P3.1.19, which is contained in the double line $V(y^2)$. All three have the same support, the $x$-axis. The reduced induced structure of Proposition P3.3.12 is the largest of the three ideals, $(y)$, the ideal of all functions that vanish on the axis.

**Example P3.5.30 (coherent sheaves on a curve).** Let $A$ be a principal ideal domain, for example $k[x]$, and $X = \operatorname{Spec} A$. By the structure theorem for finitely generated modules over a principal ideal domain, a coherent sheaf on $X$ is $\mathcal{O}_X^r \oplus \widetilde{T}$ with $T = \bigoplus_j A/(p_j^{e_j})$ a torsion module. The sheaf $\widetilde{T}$ is supported on the finite set of the primes $(p_j)$, and the sheaf is locally free if and only if $T = 0$. The fibre dimension is $r$ at the generic point and at the points outside the support of $T$, and $r$ plus the number of $j$ with $(p_j) = \mathfrak{p}$ at a point $\mathfrak{p}$ of the support.

**Example P3.5.31 (an ideal sheaf that is not of finite type).** Let $A = k[x_1, x_2, \dots]$ and $\mathfrak{m} = (x_1, x_2, \dots)$. The closed subscheme $\operatorname{Spec} A/\mathfrak{m}$ is the origin, a reduced point. Its ideal sheaf $\widetilde{\mathfrak{m}}$ is quasi-coherent but not of finite type, by part 1 of Proposition P3.5.14, since $\mathfrak{m}$ is not finitely generated (Example P3.5.16). Part 4 of Proposition P3.5.23 needs the Noetherian hypothesis.

### Proof

*Proof of Theorem P3.5.20.* (1) Let $U = \operatorname{Spec} A$ be an affine open set. By part 1 of Corollary P3.5.13, $\mathcal{F}|_U \cong \widetilde{M}$ and $\mathcal{G}|_U \cong \widetilde{N}$ with $M = \mathcal{F}(U)$ and $N = \mathcal{G}(U)$, and by part 1 of Theorem P3.5.2, $\varphi|_U = \widetilde{u}$ with $u = \varphi_U$. The sequences $0 \to \ker u \to M \to N \to \operatorname{coker} u \to 0$ and $0 \to \operatorname{im} u \to N$ are exact, so by part 2 of Proposition P3.5.1 their sheaves are exact. So $(\ker \varphi)|_U \cong (\ker u)^\sim$, $(\operatorname{coker} \varphi)|_U \cong (\operatorname{coker} u)^\sim$ and $(\operatorname{im} \varphi)|_U \cong (\operatorname{im} u)^\sim$, since kernels, cokernels and images in $\mathsf{Mod}(\mathcal{O}_X)$ commute with restriction to open sets. These sheaves are quasi-coherent on every affine open set, so they are quasi-coherent by part 1 of Corollary P3.5.13. A full subcategory of an abelian category that contains $0$, is closed under finite direct sums (part 2 below), and contains the kernel and the cokernel of each of its morphisms is abelian, with the same kernels and cokernels; so the inclusion is exact.

(2) On an affine open set $U = \operatorname{Spec} A$, a direct sum $\bigoplus_i \mathcal{F}_i$ restricts to $\bigoplus_i \widetilde{M_i} \cong (\bigoplus_i M_i)^\sim$ by part 3 of Proposition P3.5.1, and $\mathcal{F} \otimes \mathcal{G}$ restricts to $\widetilde{M} \otimes \widetilde{N} \cong (M \otimes_A N)^\sim$ by part 2 of Theorem P3.5.2, because direct sums and tensor products commute with restriction to open sets (part 5 of Theorem P2.6.13). Corollary P3.5.13 gives quasi-coherence, and Corollary P3.1.5 gives the sections over $U$. $\square$

*Proof of Proposition P3.5.22.* By Proposition P3.2.23, $\mathcal{O}_X(U)$ is Noetherian for every affine open $U$.

(1) By part 1 of Proposition P3.5.14, the quasi-coherent sheaf $\mathcal{F}|_U \cong \mathcal{F}(U)^\sim$ is of finite type if and only if $\mathcal{F}(U)$ is finitely generated. Finite type is a local condition, so it holds on $X$ if and only if it holds on the members of one affine open cover. Over a Noetherian ring a finitely generated module $M$ is finitely presented, since the kernel of $A^n \to M$ is a submodule of the Noetherian module $A^n$ (Corollary P1.3.6). So $\mathcal{F}|_U$ is of finite presentation by part 2 of Proposition P3.5.14, and $\mathcal{F}$ is of finite presentation. The last statement is Theorem P3.5.12 together with part 1 of Proposition P3.5.14.

(2) By Theorem P3.5.20, the kernel, cokernel and image of $\varphi$ are quasi-coherent, with sections over an affine $U$ the kernel, cokernel and image of $\varphi_U \colon M \to N$, a map of finitely generated modules over the Noetherian ring $\mathcal{O}_X(U)$. The kernel and image are submodules of finitely generated modules, so they are finitely generated by Corollary P1.3.6, and the cokernel is a quotient of $N$. Finite direct sums and tensor products of finitely generated modules are finitely generated. By part 1 these sheaves are coherent. The same argument applies to a quasi-coherent subsheaf or quotient, whose sections over $U$ are a submodule or a quotient of $\mathcal{F}(U)$ by Theorem P3.5.20.

(3) On an affine $U$, the sequence $0 \to \mathcal{F}'(U) \to \mathcal{F}(U) \to \mathcal{F}''(U) \to 0$ is exact by part 3 of Corollary P3.5.13. An extension of finitely generated modules is finitely generated: generators of $\mathcal{F}'(U)$ together with lifts of generators of $\mathcal{F}''(U)$ generate $\mathcal{F}(U)$. So $\mathcal{F}$ is coherent by part 1. $\square$

*Proof of Proposition P3.5.23.* (1) Let $U = \operatorname{Spec} A$ be affine. By part 2 of Proposition P3.3.11 and Theorem P3.3.10, $i^{-1}(U) \to U$ is isomorphic over $U$ to $\operatorname{Spec} A/I \to \operatorname{Spec} A$, with $I$ the kernel of $A \to \Gamma(i^{-1}U, \mathcal{O}_Z)$. By part 2 of Proposition P3.5.3, $(i_* \mathcal{O}_Z)|_U \cong (A/I)^\sim$, and $i^\#|_U$ is a morphism $\widetilde{A} \to (A/I)^\sim$ whose map on global sections is the quotient map $A \to A/I$. By part 1 of Theorem P3.5.2 it is the sheaf of this map. By exactness, the kernel of $i^\#$ on $U$ is $\widetilde{I}$, which is quasi-coherent, and $i^\#|_U$ is surjective with cokernel $0$. So $\mathcal{I}_Z$ is quasi-coherent by Corollary P3.5.13, $\mathcal{I}_Z(U) = I$, and $\mathcal{O}_X / \mathcal{I}_Z \cong i_* \mathcal{O}_Z$ because $i^\#$ is surjective.

(2) Injectivity. Let $i \colon Z \to X$ and $i' \colon Z' \to X$ be closed immersions with $\mathcal{I}_Z = \mathcal{I}_{Z'}$. For every affine open $U$, part 1 gives isomorphisms $i^{-1}(U) \cong \operatorname{Spec} A/I \cong i'^{-1}(U)$ over $U$, with the same ideal $I = \mathcal{I}_Z(U)$. A closed immersion is a monomorphism (part 4 of Proposition P3.3.11), so an isomorphism over $U$ between $i^{-1}(U)$ and $i'^{-1}(U)$ is unique if it exists. So the isomorphisms for two affine open sets agree on their intersection, which is covered by affine open sets, and they glue to an isomorphism $Z \cong Z'$ over $X$.

Surjectivity. Let $\mathcal{I} \subseteq \mathcal{O}_X$ be a quasi-coherent sheaf of ideals and $\mathcal{Q} = \mathcal{O}_X / \mathcal{I}$, a quasi-coherent sheaf of rings by Theorem P3.5.20. Let $U = \operatorname{Spec} A$ be affine and $I = \mathcal{I}(U)$, an ideal of $A$ since sections are left exact. By Theorem P3.5.20, $\mathcal{Q}|_U \cong (A/I)^\sim$, so $\operatorname{Supp} \mathcal{Q} \cap U = \{\mathfrak{p} : (A/I)_\mathfrak{p} \neq 0\} = V(I)$, a closed subset of $U$. So $Z = \operatorname{Supp} \mathcal{Q}$ is closed in $X$. Let $j \colon Z \to X$ be the inclusion and $\mathcal{O}_Z = j^{-1} \mathcal{Q}$, a sheaf of rings on $Z$ with stalks $\mathcal{O}_{Z,z} = \mathcal{Q}_z$. Since $\mathcal{Q}$ vanishes off $Z$, the natural map $\mathcal{Q} \to j_* j^{-1} \mathcal{Q}$ is an isomorphism, as one checks on stalks. On $U$, the closed immersion $\operatorname{Spec} A/I \to U$ is a homeomorphism onto $V(I) = Z \cap U$, and its pushforward of the structure sheaf is $(A/I)^\sim \cong \mathcal{Q}|_U$, by part 2 of Proposition P3.5.3. So $(Z \cap U, \mathcal{O}_Z|_{Z \cap U}) \cong \operatorname{Spec} A/I$ as locally ringed spaces. So $(Z, \mathcal{O}_Z)$ is a scheme, $j$ with $j^\# \colon \mathcal{O}_X \to \mathcal{Q} = j_* \mathcal{O}_Z$ is a morphism of locally ringed spaces and a closed immersion, and its ideal sheaf is $\mathcal{I}$.

(3) Let $i \colon Z \to X$ and $i' \colon Z' \to X$ be the closed immersions, and for an affine open $U = \operatorname{Spec} A$ let $I = \mathcal{I}_Z(U)$ and $I' = \mathcal{I}_{Z'}(U)$. If $i = i' h$, then over $U$ the quotient map $A \to A/I$ factors through $A \to A/I'$, so $I' \subseteq I$. Conversely, if $I' \subseteq I$ for every affine $U$, then the ring map $A/I' \to A/I$ gives a morphism $h_U \colon i^{-1}(U) \to i'^{-1}(U)$ with $i' h_U = i$ on $i^{-1}(U)$, by part 1. Since $i'$ is a monomorphism (part 4 of Proposition P3.3.11), the morphisms $h_U$ agree on overlaps and glue to $h$ with $i = i' h$.

(4) A quasi-coherent sheaf of ideals is a quasi-coherent subsheaf of the coherent sheaf $\mathcal{O}_X$, so it is coherent by part 2 of Proposition P3.5.22. $\square$

*Proof of Proposition P3.5.25.* The statements are local, so let $X = \operatorname{Spec} A$, $x = \mathfrak{p}$ and $\mathcal{F} = \widetilde{M}$ with $M$ finitely generated (Proposition P3.5.14). The stalk $\mathcal{F}_x = M_\mathfrak{p}$ is a finitely generated module over the local ring $A_\mathfrak{p}$.

(1) If $\mathcal{F}(x) = 0$, then $M_\mathfrak{p} = \mathfrak{p} M_\mathfrak{p}$, so $M_\mathfrak{p} = 0$ by Nakayama's lemma (Theorem P1.1.25). Each of the finitely many generators $m_i$ of $M$ is then killed by some $g_i \notin \mathfrak{p}$, and for $g = \prod g_i$, $M_g = 0$. So $\mathcal{F}|_{D(g)} = 0$. The complement of $\operatorname{Supp} \mathcal{F}$ is then open.

(2) Shrink $U$ to a basic open set that contains $x$, again written $\operatorname{Spec} A$, and let $u \colon A^n \to M$ send the basis vectors to the $s_i$, so that $\mathcal{O}^n \to \mathcal{F}$ is $\widetilde{u}$. Let $C = \operatorname{coker} u$, a finitely generated module. Tensoring $A^n \to M \to C \to 0$ with $\kappa(\mathfrak{p})$ gives an exact sequence $\kappa(\mathfrak{p})^n \to \mathcal{F}(x) \to C \otimes \kappa(\mathfrak{p}) \to 0$ (Theorem P1.1.35), and the first map is surjective by hypothesis. So $\widetilde{C}(x) = 0$, and by part 1 there is $g \notin \mathfrak{p}$ with $C_g = 0$. Then $u_g$ is surjective, and so is $\mathcal{O}^n \to \mathcal{F}$ on $D(g)$ by Proposition P3.5.1.

(3) Let $x$ be a point with $\varphi_\mathcal{F}(x) = r$. Choose a basis of $\mathcal{F}(x)$, lift it to elements of $\mathcal{F}_x$, and represent these by sections $s_1, \dots, s_r$ over one neighbourhood of $x$. By part 2 they generate $\mathcal{F}$ on a neighbourhood $V$ of $x$. For $y \in V$, $\kappa(y)^r \to \mathcal{F}(y)$ is then surjective, by right exactness of $- \otimes \kappa(y)$, so $\varphi_\mathcal{F}(y) \leq r$. So the set $\{\varphi_\mathcal{F} < n\}$ contains a neighbourhood of each of its points, it is open, and its complement $\{\varphi_\mathcal{F} \geq n\}$ is closed.

(4) Let $r = \varphi_\mathcal{F}(x)$. As in part 3, there is an affine neighbourhood $V = \operatorname{Spec} A$ of $x$ on which $\varphi_\mathcal{F}$ is constant, equal to $r$, and a surjection $u \colon A^r \to M = \mathcal{F}(V)$. The ring $A$ is reduced, since $V$ is an open subscheme of a reduced scheme. Let $K = \ker u$. For a prime $\mathfrak{q}$ of $A$, the sequence $K_\mathfrak{q} \to A_\mathfrak{q}^r \to M_\mathfrak{q} \to 0$ is exact by Theorem P1.2.5, and tensoring with $\kappa(\mathfrak{q})$ gives the exact sequence
$$K_\mathfrak{q} \otimes \kappa(\mathfrak{q}) \to \kappa(\mathfrak{q})^r \to \mathcal{F}(\mathfrak{q}) \to 0.$$
The last map is a surjection between vector spaces of the same dimension $r$, so it is an isomorphism, and the first map is $0$. Let $a = (a_1, \dots, a_r) \in K$. Its image in $\kappa(\mathfrak{q})^r$ is $(a_1(\mathfrak{q}), \dots, a_r(\mathfrak{q}))$, the values of the functions $a_i$ at $\mathfrak{q}$, and it is $0$. So every $a_i$ lies in every prime of $A$, so it is nilpotent by Theorem P1.1.9, and $a_i = 0$ since $A$ is reduced. So $K = 0$, $u$ is an isomorphism, and $\mathcal{F}|_V \cong \mathcal{O}_V^r$.

(5) By part 2 of Proposition P3.5.14, $M$ is finitely presented. The proof of the converse in part 3 of Proposition P3.5.14 uses only that $M$ is finitely presented and that $M_\mathfrak{p}$ is free at the one prime $\mathfrak{p}$, and it gives $f \notin \mathfrak{p}$ with $M_f$ free. So $\mathcal{F}$ is free on $D(f)$. $\square$

### Exercises

1. (A) Let $Z_1, Z_2 \subseteq X$ be closed subschemes with ideal sheaves $\mathcal{I}_1, \mathcal{I}_2$. Show that $\mathcal{I}_1 + \mathcal{I}_2$ and $\mathcal{I}_1 \cap \mathcal{I}_2$ are quasi-coherent, and that their closed subschemes are the scheme-theoretic intersection of Proposition P3.3.20 and a closed subscheme with support $Z_1 \cup Z_2$, the *scheme-theoretic union*.
2. (A) Compute the scheme-theoretic union of the two axes $V(x)$ and $V(y)$ in $\mathbb{A}^2_k$, and of the point $V(x, y)$ with itself. Compare $\mathcal{I}_1 \cap \mathcal{I}_2$ with $\mathcal{I}_1 \mathcal{I}_2$ in both cases.
3. (A) Let $\mathcal{F}$ be a coherent sheaf on a Noetherian scheme $X$. Show that $\varphi_\mathcal{F}$ takes finitely many values and that the set of points where $\mathcal{F}$ is not locally free is closed.
4. (B) Let $X$ be an integral scheme with generic point $\eta$ and $\mathcal{F}$ quasi-coherent of finite type. The *rank* of $\mathcal{F}$ is $\varphi_\mathcal{F}(\eta)$. Show that $\varphi_\mathcal{F}(x) \geq \operatorname{rank} \mathcal{F}$ for every $x$, and that $\mathcal{F}$ is locally free on the dense open set where equality holds.
5. (B) Let $X$ be a scheme and $\mathcal{F}$ a quasi-coherent sheaf. Show that the *annihilator* $\mathcal{A}nn(\mathcal{F})$, whose sections over $U$ are the $a \in \mathcal{O}_X(U)$ with $a \mathcal{F}|_U = 0$, is a quasi-coherent ideal sheaf when $\mathcal{F}$ is of finite type, and that its closed subscheme has support $\operatorname{Supp} \mathcal{F}$. Show that $\mathcal{F}$ is the pushforward of a quasi-coherent sheaf on this closed subscheme.
6. (B) Give an example of a quasi-coherent sheaf $\mathcal{F}$ of finite type on a reduced scheme that is not of finite presentation and whose fibre dimension is not locally constant, and an example on $\operatorname{Spec} k[x]$ of a coherent sheaf $\mathcal{F}$ with $\mathcal{F}_x$ free for every closed point $x$ that is not locally free. (One of the two requests is impossible; say which, and why.)
7. (C) Let $X$ be a Noetherian scheme, $U \subseteq X$ open, and $\mathcal{G}$ a coherent sheaf on $U$. Assume that $\mathcal{G} = \mathcal{F}|_U$ for some quasi-coherent sheaf $\mathcal{F}$ on $X$. Show that there is a coherent subsheaf $\mathcal{F}' \subseteq \mathcal{F}$ with $\mathcal{F}'|_U = \mathcal{G}$. (Work on a finite affine cover, and use that $\mathcal{F}(V)$ is the union of its finitely generated submodules.)

### Lean

Mathlib has the data `AlgebraicGeometry.Scheme.IdealSheafData` of a quasi-coherent sheaf of ideals, given by an ideal $I(U) \subseteq \Gamma(X, U)$ for every affine open $U$ with $I(D(f)) = I(U)_f$, the associated closed subscheme `AlgebraicGeometry.Scheme.IdealSheafData.subscheme` with its closed immersion `subschemeι`, and the support `AlgebraicGeometry.Scheme.IdealSheafData.support`. The ideal sheaf of a morphism is `AlgebraicGeometry.Scheme.Hom.ker`. The abelian category of quasi-coherent sheaves, coherent sheaves and the sheaf form of Nakayama's lemma are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Coherent sheaves come from the analytic theory of Oka and Cartan, and Serre, in *Faisceaux algébriques cohérents* (1955), introduced them in algebraic geometry, before schemes. Hartshorne, Proposition II.5.7 and Proposition II.5.9, proves the abelian category statements and the correspondence with closed subschemes, and Exercise II.5.8 asks for the semicontinuity and the reduced criterion of Proposition P3.5.25. The literature state is theorem. In the minimal model program, the non-free locus of a coherent sheaf is closed by part 3, and part 4 is used each time a sheaf of constant rank on a reduced base is shown to be a vector bundle, for instance for the direct images of a sheaf in a flat family over a reduced base.
