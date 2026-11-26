---
title: Tensor product and sheaf Hom
nodes: []
sources: [Har77, Vak25, Stacks]
reads_with: [Har77:ch2, Vak25:ch2]
requires: [P1.1, P2.2, P2.5, P2.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Tensor product and sheaf Hom

### Statement

In this section $\mathcal{A}$ is a sheaf of rings on a space $X$, for example the structure sheaf of a ringed space. Everything in Section 6.1 holds for $\mathcal{A}$-modules. For an open $U$, write $\mathcal{F}|_U$ for the restriction of $\mathcal{F}$ to $U$, an $\mathcal{A}|_U$-module.

**Definition P2.6.11 (tensor product).** Let $\mathcal{F}$ and $\mathcal{G}$ be $\mathcal{A}$-modules. The *tensor product* $\mathcal{F} \otimes_{\mathcal{A}} \mathcal{G}$ is the sheafification of the presheaf of $\mathcal{A}$-modules
$$U \mapsto \mathcal{F}(U) \otimes_{\mathcal{A}(U)} \mathcal{G}(U),$$
with restriction maps $s \otimes t \mapsto s|_V \otimes t|_V$. For a section $s$ of $\mathcal{F}$ and $t$ of $\mathcal{G}$ over $U$, write $s \otimes t$ also for the image of $s \otimes t$ in $(\mathcal{F} \otimes_{\mathcal{A}} \mathcal{G})(U)$.

Lean: Mathlib `PresheafOfModulesOfCommRing.Monoidal.tensorObj` is the presheaf tensor product; the sheaf tensor product is not in Lean as stated.

**Definition P2.6.12 (sheaf Hom and dual).** Let $\mathcal{F}$ and $\mathcal{G}$ be $\mathcal{A}$-modules. The *sheaf Hom* is the presheaf
$$\mathcal{H}om_{\mathcal{A}}(\mathcal{F}, \mathcal{G})(U) = \operatorname{Hom}_{\mathcal{A}|_U}(\mathcal{F}|_U, \mathcal{G}|_U),$$
with restriction of morphisms as restriction maps. For $\mathcal{A} = \mathcal{O}_X$, the *dual* of $\mathcal{F}$ is $\mathcal{F}^\vee = \mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, \mathcal{O}_X)$.

Lean: Mathlib `CategoryTheory.sheafHom` is the sheaf of morphisms between sheaves of types or of objects of a category; for modules it is not in Lean as stated.

**Theorem P2.6.13 (tensor product and sheaf Hom).** Let $\mathcal{F}$, $\mathcal{G}$ and $\mathcal{H}$ be $\mathcal{A}$-modules.

1. $\mathcal{H}om_{\mathcal{A}}(\mathcal{F}, \mathcal{G})$ is a sheaf, and it is an $\mathcal{A}$-module with $(a \varphi)(s) = a|_V \, \varphi(s)$ for $a \in \mathcal{A}(U)$ and $s \in \mathcal{F}(V)$, $V \subseteq U$. Its global sections are $\operatorname{Hom}_{\mathcal{A}}(\mathcal{F}, \mathcal{G})$.
2. For every $x \in X$ the natural map is an isomorphism of $\mathcal{A}_x$-modules
$$(\mathcal{F} \otimes_{\mathcal{A}} \mathcal{G})_x \cong \mathcal{F}_x \otimes_{\mathcal{A}_x} \mathcal{G}_x.$$
3. There are natural isomorphisms
$$\operatorname{Hom}_{\mathcal{A}}(\mathcal{F} \otimes_{\mathcal{A}} \mathcal{G}, \mathcal{H}) \cong \operatorname{Hom}_{\mathcal{A}}(\mathcal{F}, \mathcal{H}om_{\mathcal{A}}(\mathcal{G}, \mathcal{H})), \qquad \mathcal{H}om_{\mathcal{A}}(\mathcal{F} \otimes_{\mathcal{A}} \mathcal{G}, \mathcal{H}) \cong \mathcal{H}om_{\mathcal{A}}(\mathcal{F}, \mathcal{H}om_{\mathcal{A}}(\mathcal{G}, \mathcal{H})).$$
4. The functor $- \otimes_{\mathcal{A}} \mathcal{G}$ is right exact. The functor $\mathcal{H}om_{\mathcal{A}}(\mathcal{G}, -)$ is left exact, and the contravariant functor $\mathcal{H}om_{\mathcal{A}}(-, \mathcal{G})$ sends an exact sequence $\mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ to an exact sequence $0 \to \mathcal{H}om(\mathcal{F}'', \mathcal{G}) \to \mathcal{H}om(\mathcal{F}, \mathcal{G}) \to \mathcal{H}om(\mathcal{F}', \mathcal{G})$.
5. There are natural isomorphisms $\mathcal{A} \otimes_{\mathcal{A}} \mathcal{F} \cong \mathcal{F}$, $\mathcal{F} \otimes \mathcal{G} \cong \mathcal{G} \otimes \mathcal{F}$, $(\mathcal{F} \otimes \mathcal{G}) \otimes \mathcal{H} \cong \mathcal{F} \otimes (\mathcal{G} \otimes \mathcal{H})$ and $\mathcal{H}om_{\mathcal{A}}(\mathcal{A}, \mathcal{F}) \cong \mathcal{F}$. Tensor product and sheaf Hom commute with restriction to an open set.

Lean: not in Lean as stated for sheaves; for presheaves of modules Mathlib has the monoidal structure of `PresheafOfModulesOfCommRing.Monoidal` and the fact that tensoring preserves colimits.

### Proof in words

A morphism of sheaves can be glued from local pieces, so morphisms between restrictions form a sheaf. Sheafification does not change stalks, and the tensor product of modules commutes with the direct limit that defines a stalk, which gives part 2. The adjunction of part 3 is the adjunction between tensor and Hom of modules, applied one open set at a time. A morphism out of a sheafification is a morphism out of the presheaf, so it is a compatible family of bilinear maps. Exactness is checked on stalks, so part 2 reduces the right exactness of the tensor product to that of modules. Left exactness of $\mathcal{H}om$ holds on sections over each open set.

### Examples

**Example P2.6.14 (intersection of subschemes).** Let $X$ be a variety and $\mathcal{I}, \mathcal{J} \subseteq \mathcal{O}_X$ ideal sheaves. By part 2, the stalk of $\mathcal{O}_X/\mathcal{I} \otimes_{\mathcal{O}_X} \mathcal{O}_X/\mathcal{J}$ at $x$ is $\mathcal{O}_{X,x}/\mathcal{I}_x \otimes \mathcal{O}_{X,x}/\mathcal{J}_x = \mathcal{O}_{X,x}/(\mathcal{I}_x + \mathcal{J}_x)$. So
$$\mathcal{O}_X/\mathcal{I} \otimes_{\mathcal{O}_X} \mathcal{O}_X/\mathcal{J} \cong \mathcal{O}_X/(\mathcal{I} + \mathcal{J}),$$
the structure sheaf of the scheme theoretic intersection, through the natural surjection $\mathcal{O}_X/\mathcal{I} \otimes \mathcal{O}_X/\mathcal{J} \to \mathcal{O}_X/(\mathcal{I} + \mathcal{J})$, which is an isomorphism on stalks. On $X = \mathbb{A}^2$ with coordinates $x, y$, let $\mathcal{I}$ be the ideal sheaf of the line $y = 0$ and $\mathcal{J}$ that of the parabola $y = x^2$. The tensor product is supported at the origin, with stalk $\mathcal{O}_{X,0}/(y, x^2)$ of dimension $2$ over $k$. The number $2$ is the intersection multiplicity of the tangent line and the parabola.

**Example P2.6.15 (tensor product is not left exact).** On $X = \mathbb{A}^1 = \operatorname{Spec} k[x]$, the sequence $0 \to \mathcal{O}_X \xrightarrow{x} \mathcal{O}_X \to k(0) \to 0$ is exact by Example P2.6.8. Tensor it with $k(0)$. By part 2 and part 5 the result is $k(0) \xrightarrow{0} k(0) \to k(0) \to 0$, since $x$ acts as $0$ on $\kappa(0)$. The first map is not injective. The kernel $k(0)$ is the sheaf $\mathcal{T}or_1(k(0), k(0))$, and Chapter 8 recovers it as a cohomology sheaf of the derived tensor product.

**Example P2.6.16 (tensor products of the sheaves $\mathcal{O}(n)$).** Keep the notation of Example P2.6.9. On $U_i$, $\mathcal{O}(a)|_{U_i} = \mathcal{O}_{U_i}$, so by part 5, $(\mathcal{O}(a) \otimes \mathcal{O}(b))|_{U_i} \cong \mathcal{O}_{U_i} \otimes \mathcal{O}_{U_i} \cong \mathcal{O}_{U_i}$ through $f \otimes g \mapsto f g$. On $U_{01}$ a section $f \otimes g$ given in the chart $U_1$ is $t^a f \otimes t^b g = t^{a+b} f g$ in the chart $U_0$. So $\mathcal{O}(a) \otimes \mathcal{O}(b)$ is glued from $\mathcal{O}_{U_0}$ and $\mathcal{O}_{U_1}$ by multiplication by $t^{a+b}$, and $\mathcal{O}(a) \otimes \mathcal{O}(b) \cong \mathcal{O}(a+b)$. In particular $\mathcal{O}(1) \otimes \mathcal{O}(-1) \cong \mathcal{O}$. The presheaf tensor product of Definition P2.6.11 has value $\Gamma(\mathcal{O}(1)) \otimes_k \Gamma(\mathcal{O}(-1)) = k^2 \otimes 0 = 0$ on $X = \mathbb{P}^1$, while $\Gamma(\mathbb{P}^1, \mathcal{O}) = k$. So the presheaf tensor product is not a sheaf, and global sections do not commute with tensor products.

**Example P2.6.17 (the dual of a torsion sheaf).** On $X = \mathbb{A}^1$, $\mathcal{H}om(k(0), \mathcal{O}_X) = 0$. Indeed, a map $k(0)|_U \to \mathcal{O}_U$ sends a section $c$ to a regular function $f$ with $x f = 0$, since $x$ kills $c$, and so $f = 0$. Apply the contravariant functor $\mathcal{H}om(-, \mathcal{O}_X)$ to the sequence of Example P2.6.15. By part 4 and part 5 the result is the exact sequence $0 \to 0 \to \mathcal{O}_X \xrightarrow{x} \mathcal{O}_X$. The last map is not surjective, so $\mathcal{H}om(-, \mathcal{O}_X)$ is not right exact. Its failure is measured by $\mathcal{E}xt^1(k(0), \mathcal{O}_X) \cong k(0)$ (Chapter 8 and P4 Ch. 8). Local duality and the dualizing complex of Chapter 8 are built from these sheaves.

### Proof

*Part 1.* Let $U = \bigcup U_i$ be an open cover and $\varphi_i: \mathcal{F}|_{U_i} \to \mathcal{G}|_{U_i}$ linear maps that agree on each $U_i \cap U_j$. For $V \subseteq U$ open and $s \in \mathcal{F}(V)$, the sections $\varphi_i(s|_{V \cap U_i}) \in \mathcal{G}(V \cap U_i)$ agree on overlaps, so they glue to a unique $\varphi(s) \in \mathcal{G}(V)$. The map $s \mapsto \varphi(s)$ commutes with restriction and is linear, because each property can be checked after restriction to the $V \cap U_i$, where it holds by locality of $\mathcal{G}$. It restricts to $\varphi_i$ on $U_i$. If two maps $\varphi, \psi$ on $U$ agree on each $U_i$, then $\varphi(s)$ and $\psi(s)$ agree on each $V \cap U_i$, so they are equal. So $\mathcal{H}om_{\mathcal{A}}(\mathcal{F}, \mathcal{G})$ is a sheaf. For $a \in \mathcal{A}(U)$, the map $s \mapsto a|_V \varphi(s)$ is again linear because $\mathcal{A}$ is commutative, and it commutes with restriction. The module axioms hold section by section. The global sections are the morphisms over $X$ by definition.

*Part 2.* Write $P$ for the presheaf tensor product. Sheafification keeps stalks (Theorem P2.5.12), so $(\mathcal{F} \otimes \mathcal{G})_x = P_x = \varinjlim_{U \ni x} \mathcal{F}(U) \otimes_{\mathcal{A}(U)} \mathcal{G}(U)$. The maps $\mathcal{F}(U) \otimes_{\mathcal{A}(U)} \mathcal{G}(U) \to \mathcal{F}_x \otimes_{\mathcal{A}_x} \mathcal{G}_x$, $s \otimes t \mapsto s_x \otimes t_x$, are compatible with restriction, so they define $\alpha: P_x \to \mathcal{F}_x \otimes \mathcal{G}_x$. For the inverse, define $\beta(s_x, t_x)$ as the class of $s|_W \otimes t|_W$, where $s$ and $t$ are representatives on a common neighbourhood $W$ of $x$. A different choice of representatives agrees with the first on a smaller neighbourhood, so $\beta$ is well defined. It is additive in each variable, and for $a_x \in \mathcal{A}_x$ represented by $a$ on $W$, $\beta(a_x s_x, t_x)$ and $\beta(s_x, a_x t_x)$ are both the class of $a s \otimes t = s \otimes a t$. So $\beta$ is $\mathcal{A}_x$-balanced and gives a map $\mathcal{F}_x \otimes \mathcal{G}_x \to P_x$. Both composites are the identity on generators, so $\alpha$ is an isomorphism. It is $\mathcal{A}_x$-linear by construction.

*Part 3.* By part 1 of Theorem P2.6.3, a linear map $\mathcal{F} \otimes \mathcal{G} \to \mathcal{H}$ is the same as a linear map of presheaves $P \to \mathcal{H}$. By the universal property of the tensor product of modules, this is a family of $\mathcal{A}(U)$-bilinear maps $b_U: \mathcal{F}(U) \times \mathcal{G}(U) \to \mathcal{H}(U)$ that commute with restriction. Given such a family, and $s \in \mathcal{F}(U)$, define $\varphi(s): \mathcal{G}|_U \to \mathcal{H}|_U$ by $t \mapsto b_V(s|_V, t)$ for $t \in \mathcal{G}(V)$, $V \subseteq U$. It is linear and commutes with restriction, so it is a section of $\mathcal{H}om(\mathcal{G}, \mathcal{H})$ over $U$, and $s \mapsto \varphi(s)$ is a linear map of sheaves $\mathcal{F} \to \mathcal{H}om(\mathcal{G}, \mathcal{H})$. Conversely, a linear $\varphi: \mathcal{F} \to \mathcal{H}om(\mathcal{G}, \mathcal{H})$ gives the bilinear maps $b_U(s, t) = \varphi(s)(t)$. The two constructions are inverse and natural in $\mathcal{F}$, $\mathcal{G}$ and $\mathcal{H}$, which gives the first isomorphism. Restriction to an open set commutes with sheafification, since both can be computed with germs, and so with tensor products. It commutes with $\mathcal{H}om$ by definition. Apply the first isomorphism on every open $U$ to obtain the second.

*Part 4.* Let $\mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ be exact. On the stalk at $x$, by part 2, the sequence $\mathcal{F}' \otimes \mathcal{G} \to \mathcal{F} \otimes \mathcal{G} \to \mathcal{F}'' \otimes \mathcal{G} \to 0$ becomes the tensor product of an exact sequence of $\mathcal{A}_x$-modules with $\mathcal{G}_x$, which is exact (Proposition P2.2.30). By part 3 of Theorem P2.6.3 the sequence is exact. For the second claim, let $0 \to \mathcal{H}' \to \mathcal{H} \to \mathcal{H}''$ be exact. Over each open $U$, the sequence $0 \to \operatorname{Hom}(\mathcal{G}|_U, \mathcal{H}'|_U) \to \operatorname{Hom}(\mathcal{G}|_U, \mathcal{H}|_U) \to \operatorname{Hom}(\mathcal{G}|_U, \mathcal{H}''|_U)$ is exact by Proposition P2.2.30 in the abelian category $\mathsf{Mod}(\mathcal{A}|_U)$, since restriction to $U$ is exact. Kernels of sheaves are computed on sections, so the sequence of sheaves is exact. The contravariant claim has the same proof with the contravariant functor $\operatorname{Hom}(-, \mathcal{G}|_U)$.

*Part 5.* The presheaf maps $\mathcal{A}(U) \otimes_{\mathcal{A}(U)} \mathcal{F}(U) \to \mathcal{F}(U)$, $a \otimes s \mapsto a s$, sheafify to a map $\mathcal{A} \otimes \mathcal{F} \to \mathcal{F}$. On stalks it is $\mathcal{A}_x \otimes \mathcal{F}_x \to \mathcal{F}_x$, an isomorphism, so it is an isomorphism by Theorem P2.5.5. The symmetry and associativity maps are built the same way from those of modules, and are isomorphisms on stalks by part 2. The isomorphism $\mathcal{H}om(\mathcal{A}, \mathcal{F}) \cong \mathcal{F}$ is Proposition P2.6.4 applied on each open set. Restriction was treated in part 3. $\square$

### Exercises

1. (A) Show that $\mathcal{H}om_{\mathcal{A}}(\mathcal{A}^n, \mathcal{G}) \cong \mathcal{G}^n$ and $\mathcal{A}^m \otimes_{\mathcal{A}} \mathcal{A}^n \cong \mathcal{A}^{mn}$.
2. (A) Show that tensor products commute with arbitrary direct sums: $(\bigoplus_i \mathcal{F}_i) \otimes \mathcal{G} \cong \bigoplus_i (\mathcal{F}_i \otimes \mathcal{G})$. Show that $\mathcal{H}om(\bigoplus_i \mathcal{F}_i, \mathcal{G}) \cong \prod_i \mathcal{H}om(\mathcal{F}_i, \mathcal{G})$.
3. (A) Let $p \neq q$ be closed points of a variety $X$. Show that $k(p) \otimes_{\mathcal{O}_X} k(q) = 0$ and $k(p) \otimes_{\mathcal{O}_X} k(p) \cong k(p)$.
4. (B) Let $X = \mathbb{A}^2$ and $\mathfrak{m} \subseteq \mathcal{O}_X$ the ideal sheaf of the origin. Show that $\mathfrak{m} \otimes_{\mathcal{O}_X} k(0)$ is $k(0)^2$, so the stalk of $\mathfrak{m}$ at the origin needs two generators. Show that $\mathfrak{m} \otimes \mathfrak{m} \to \mathcal{O}_X$, $f \otimes g \mapsto f g$, is not injective, by looking at $x \otimes y - y \otimes x$.
5. (B) Let $\mathcal{F}$ and $\mathcal{G}$ be $\mathcal{A}$-modules. Show that the natural map $\mathcal{H}om(\mathcal{F}, \mathcal{G})_x \to \operatorname{Hom}_{\mathcal{A}_x}(\mathcal{F}_x, \mathcal{G}_x)$ need not be injective: on $X = \mathbb{R}$ with $\mathcal{A} = \underline{\mathbb{Z}}$, take $\mathcal{F} = \mathcal{G} = \bigoplus_{n \geq 1} (1/n)_* \mathbb{Z}$ and look at the germ of the identity at $0$. Section 6.4 shows that it is an isomorphism when $\mathcal{F}$ is finitely presented.
6. (B) Define an $\mathcal{A}$-bilinear map $\mathcal{F} \times \mathcal{G} \to \mathcal{H}$ as a family of $\mathcal{A}(U)$-bilinear maps on sections that commutes with restriction. Show that $\mathcal{F} \otimes_{\mathcal{A}} \mathcal{G}$, with $(s, t) \mapsto s \otimes t$, is the universal $\mathcal{A}$-bilinear map.
7. (C) On $X = \mathbb{P}^1$, show that the multiplication map $\Gamma(\mathcal{O}(a)) \otimes_k \Gamma(\mathcal{O}(b)) \to \Gamma(\mathcal{O}(a+b))$ is surjective for $a, b \geq 0$, but not for $a = -1$, $b = 1$. Interpret the first claim in terms of polynomials in two variables.

### Lean

Mathlib builds the monoidal structure on presheaves of modules over a presheaf of commutative rings in `Mathlib/Algebra/Category/ModuleCat/Presheaf/Monoidal.lean`, with `PresheafOfModulesOfCommRing.Monoidal.tensorObj` as the sectionwise tensor product, and proves that tensoring preserves colimits. The monoidal closed structure on modules over a ring is an instance in `Mathlib/Algebra/Category/ModuleCat/Monoidal/Closed.lean`. The sheaf of morphisms `CategoryTheory.sheafHom` exists for sheaves with values in a category, but the sheaf tensor product, the sheaf $\mathcal{H}om$ of modules and the stalk formula are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Tensor products and Hom of sheaves of modules appear in Serre's *Faisceaux algébriques cohérents* and in Godement's book of 1958. The need to sheafify the tensor product, shown by Example P2.6.16, is one reason the sections over an affine open set play a special role: on an affine scheme the presheaf tensor product of quasi-coherent sheaves is already a sheaf (P3 Ch. 5). Hartshorne leaves most of the statements of this section as exercises in Chapter II, Section 5.
