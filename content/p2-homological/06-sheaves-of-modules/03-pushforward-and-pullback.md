---
title: Pushforward and pullback
nodes: []
sources: [Har77, Vak25, Stacks]
reads_with: [Har77:ch2, Vak25:ch2]
requires: [P1.1, P2.1, P2.2, P2.5, P2.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Pushforward and pullback

### Statement

Let $f: (X, \mathcal{O}_X) \to (Y, \mathcal{O}_Y)$ be a morphism of ringed spaces. Section 5.4 gives the functors $f_*: \mathsf{Ab}(X) \to \mathsf{Ab}(Y)$ and $f^{-1}: \mathsf{Ab}(Y) \to \mathsf{Ab}(X)$, the adjunction $f^{-1} \dashv f_*$ and the stalks $(f^{-1} \mathcal{G})_x = \mathcal{G}_{f(x)}$. Write $f^\flat: f^{-1} \mathcal{O}_Y \to \mathcal{O}_X$ for the morphism of sheaves of rings that corresponds to $f^\#: \mathcal{O}_Y \to f_* \mathcal{O}_X$ under this adjunction. On stalks it is the map $f^\#_x: \mathcal{O}_{Y, f(x)} \to \mathcal{O}_{X,x}$ of Section 6.1.

**Definition P2.6.18 (pushforward and pullback of modules).** Let $\mathcal{F}$ be an $\mathcal{O}_X$-module. Each $(f_* \mathcal{F})(V) = \mathcal{F}(f^{-1} V)$ is a module over $\mathcal{O}_X(f^{-1} V)$, and so over $\mathcal{O}_Y(V)$ through $f^\#$. This makes $f_* \mathcal{F}$ an $\mathcal{O}_Y$-module, the *pushforward*. Let $\mathcal{G}$ be an $\mathcal{O}_Y$-module. Then $f^{-1} \mathcal{G}$ is an $f^{-1} \mathcal{O}_Y$-module, and $\mathcal{O}_X$ is an $f^{-1} \mathcal{O}_Y$-algebra through $f^\flat$. The *pullback* of $\mathcal{G}$ is the $\mathcal{O}_X$-module
$$f^* \mathcal{G} = f^{-1} \mathcal{G} \otimes_{f^{-1} \mathcal{O}_Y} \mathcal{O}_X.$$
A morphism $\mathcal{G} \to \mathcal{G}'$ induces $f^* \mathcal{G} \to f^* \mathcal{G}'$, so $f^*$ is a functor $\mathsf{Mod}(\mathcal{O}_Y) \to \mathsf{Mod}(\mathcal{O}_X)$.

Lean: Mathlib `SheafOfModules.pushforward` and `SheafOfModules.pullback`; for schemes `AlgebraicGeometry.Scheme.Modules.pushforward` and `AlgebraicGeometry.Scheme.Modules.pullback`.

The module structure on $f^{-1} \mathcal{G}$ comes from that of the presheaf $V \mapsto \varinjlim_{W \supseteq f(V)} \mathcal{G}(W)$ of Section 5.4, which is a module over the analogous presheaf of rings, and part 1 of Theorem P2.6.3. On stalks the action is that of $\mathcal{O}_{Y, f(x)}$ on $\mathcal{G}_{f(x)}$.

**Theorem P2.6.19 (pullback and pushforward).** Let $f: X \to Y$ be a morphism of ringed spaces, $\mathcal{F}$ an $\mathcal{O}_X$-module and $\mathcal{G}$ an $\mathcal{O}_Y$-module.

1. There is an isomorphism, natural in $\mathcal{F}$ and $\mathcal{G}$,
$$\operatorname{Hom}_{\mathcal{O}_X}(f^* \mathcal{G}, \mathcal{F}) \cong \operatorname{Hom}_{\mathcal{O}_Y}(\mathcal{G}, f_* \mathcal{F}).$$
So $f^*$ is left adjoint to $f_*$.
2. For every $x \in X$ there is a natural isomorphism of $\mathcal{O}_{X,x}$-modules
$$(f^* \mathcal{G})_x \cong \mathcal{G}_{f(x)} \otimes_{\mathcal{O}_{Y, f(x)}} \mathcal{O}_{X,x}.$$
3. The functor $f^*$ is right exact and commutes with direct sums. The functor $f_*$ is left exact and commutes with products.
4. There are natural isomorphisms $f^* \mathcal{O}_Y \cong \mathcal{O}_X$, $f^*(\mathcal{O}_Y^{(I)}) \cong \mathcal{O}_X^{(I)}$ and $f^*(\mathcal{G} \otimes_{\mathcal{O}_Y} \mathcal{G}') \cong f^* \mathcal{G} \otimes_{\mathcal{O}_X} f^* \mathcal{G}'$.
5. For a second morphism $g: Y \to Z$, $(g f)_* = g_* f_*$ and $(g f)^* \cong f^* g^*$.

Lean: Mathlib `SheafOfModules.pullbackPushforwardAdjunction` and `AlgebraicGeometry.Scheme.Modules.pullbackPushforwardAdjunction` for part 1; `SheafOfModules.pushforwardComp`, `SheafOfModules.pullbackComp`, `AlgebraicGeometry.Scheme.Modules.pushforwardComp` and `AlgebraicGeometry.Scheme.Modules.pullbackComp` for part 5. Parts 2 and 4 are not in Lean as stated.

The adjunction of part 1 is the one announced in Chapter 1. Its unit is a map $\mathcal{G} \to f_* f^* \mathcal{G}$, and its counit is a map $f^* f_* \mathcal{F} \to \mathcal{F}$.

### Proof in words

The pullback is built in two steps, and each step has a right adjoint. The functor $f^{-1}$ moves a module from $Y$ to $X$ as a module over $f^{-1} \mathcal{O}_Y$, and its right adjoint is $f_*$ by Section 5.4. Linearity is a property of maps on stalks, and the stalks of $f^{-1}$ are those of $\mathcal{G}$, so the adjunction of Section 5.4 respects linear maps. The tensor product with $\mathcal{O}_X$ turns an $f^{-1} \mathcal{O}_Y$-module into an $\mathcal{O}_X$-module, and its right adjoint forgets the $\mathcal{O}_X$-structure, as for extension of scalars in commutative algebra. The composite of two left adjoints is left adjoint to the composite of the right adjoints. The rest follows from the adjunction, from the stalk formulas of Sections 5.4 and 6.2 and from the general facts of Chapter 2 on adjoint functors.

### Examples

**Example P2.6.20 (morphisms of affine schemes).** Let $\varphi: A \to B$ be a ring map and $f: Y = \operatorname{Spec} B \to X = \operatorname{Spec} A$ the corresponding morphism. P3 Ch. 5 attaches to an $A$-module $M$ the $\mathcal{O}_X$-module $\widetilde{M}$ with $\widetilde{M}(D(a)) = M_a$, and proves that $\operatorname{Hom}_{\mathcal{O}_X}(\widetilde{M}, \mathcal{F}) \cong \operatorname{Hom}_A(M, \Gamma(X, \mathcal{F}))$ for every $\mathcal{O}_X$-module $\mathcal{F}$. Then:

1. For a $B$-module $N$, $f_* \widetilde{N} \cong \widetilde{N_A}$, where $N_A$ is $N$ viewed as an $A$-module. Indeed $f^{-1}(D(a)) = D(\varphi(a))$, and $\widetilde{N}(D(\varphi(a))) = N_{\varphi(a)} = (N_A)_a$, compatibly with restriction. The basic open sets form a basis, so Theorem P2.5.34 gives the isomorphism.
2. For an $A$-module $M$, $f^* \widetilde{M} \cong (M \otimes_A B)^\sim$. Indeed, for every $\mathcal{O}_Y$-module $\mathcal{F}$, part 1 of the theorem and the fact above give
$$\operatorname{Hom}(f^* \widetilde{M}, \mathcal{F}) \cong \operatorname{Hom}(\widetilde{M}, f_* \mathcal{F}) \cong \operatorname{Hom}_A(M, \Gamma(Y, \mathcal{F})) \cong \operatorname{Hom}_B(M \otimes_A B, \Gamma(Y, \mathcal{F})) \cong \operatorname{Hom}((M \otimes_A B)^\sim, \mathcal{F}),$$
naturally in $\mathcal{F}$, and the Yoneda lemma (Corollary P2.1.24) gives the isomorphism.

This is the pullback and pushforward of quasi-coherent sheaves along $\operatorname{Spec} B \to \operatorname{Spec} A$ promised in Chapter 1. The adjunction of part 1 becomes the adjunction between extension and restriction of scalars.

**Example P2.6.21 (the map to a point).** Let $k$ be a ring and $X$ a ringed space with a ring map $k \to \Gamma(X, \mathcal{O}_X)$, that is, a morphism $p: X \to (\mathrm{pt}, k)$ (Exercise 5 of Section 6.1). Then $p_* \mathcal{F} = \Gamma(X, \mathcal{F})$ and $p^* V = \underline{V} \otimes_{\underline{k}} \mathcal{O}_X$ for a $k$-module $V$. For $V = k^{(I)}$ this is the free module $\mathcal{O}_X^{(I)}$, and part 1 becomes Proposition P2.6.4.

**Example P2.6.22 (the fibre at a point).** Let $X$ be a locally ringed space and $x \in X$. The inclusion $i_x: \{x\} \to X$, with the ring $\kappa(x)$ on the point and $f^\#$ given by $\mathcal{O}_X(U) \to \mathcal{O}_{X,x} \to \kappa(x)$ for $U \ni x$, is a morphism of locally ringed spaces. By part 2, $i_x^* \mathcal{F}$ is the vector space $\mathcal{F}_x \otimes_{\mathcal{O}_{X,x}} \kappa(x) = \mathcal{F}(x)$, the fibre of Exercise 3 of Section 6.1. If $\mathcal{F}$ is generated near $x$ by finitely many sections, then $\mathcal{F}_x$ is a finitely generated $\mathcal{O}_{X,x}$-module, and Nakayama's lemma (P1 Ch. 1) shows that $\mathcal{F}(x) = 0$ if and only if $\mathcal{F}_x = 0$, and that sections whose images span $\mathcal{F}(x)$ generate $\mathcal{F}_x$. For a morphism $f: X \to Y$ and $y = f(x)$, part 2 gives $(f^* \mathcal{G})(x) \cong \mathcal{G}(y) \otimes_{\kappa(y)} \kappa(x)$: pullback sends fibres to fibres.

**Example P2.6.23 (closed immersions).** Let $X$ be a variety, $Z \subseteq X$ a closed subvariety with ideal sheaf $\mathcal{I}$, and $i: Z \to X$ the inclusion, with $\mathcal{O}_Z = i^{-1}(\mathcal{O}_X/\mathcal{I})$. Then the unit $\mathcal{O}_X/\mathcal{I} \to i_* i^{-1}(\mathcal{O}_X/\mathcal{I}) = i_* \mathcal{O}_Z$ is an isomorphism, since both sides have stalk $\mathcal{O}_{X,x}/\mathcal{I}_x$ at $x \in Z$ and $0$ off $Z$ (Proposition P2.5.32). The functor $i_*$ is exact, by the same stalk computation. For an $\mathcal{O}_X$-module $\mathcal{F}$, part 2 gives $(i^* \mathcal{F})_x = \mathcal{F}_x/\mathcal{I}_x \mathcal{F}_x$ for $x \in Z$, and the unit $\mathcal{F} \to i_* i^* \mathcal{F}$ induces an isomorphism $\mathcal{F}/\mathcal{I} \mathcal{F} \cong i_* i^* \mathcal{F}$. Here $\mathcal{F}/\mathcal{I} \mathcal{F} \cong \mathcal{F} \otimes \mathcal{O}_X/\mathcal{I}$. For a divisor $S \subseteq X$ and a sheaf $\mathcal{O}_X(D)$, this is the sheaf $\mathcal{O}_S(D|_S)$ of Example P2.5.10, when $\mathcal{O}_X(D)$ is a line bundle.

**Example P2.6.24 (pullback is not left exact).** Let $i: \{0\} \to \mathbb{A}^1$ be the inclusion of the origin, a closed immersion. Apply $i^*$ to the exact sequence $0 \to \mathcal{O} \xrightarrow{x} \mathcal{O} \to k(0) \to 0$. Since $i^* \mathcal{O} = k$ and $x$ maps to $0$ in $\kappa(0) = k$, the result is $k \xrightarrow{0} k \to k \to 0$. The first map is not injective. Chapter 8 replaces $i^*$ by its left derived functor $\mathbf{L} i^*$, and computes $\mathbf{L} i^* k(0) \cong k \oplus k[1]$.

**Example P2.6.25 (open immersions).** Let $j: U \to X$ be the inclusion of an open set, with $\mathcal{O}_U = \mathcal{O}_X|_U$. Then $j^{-1} \mathcal{O}_X = \mathcal{O}_U$, so $j^* \mathcal{F} = \mathcal{F}|_U$, and $j^*$ is exact. Part 1 says that a map $\mathcal{F}|_U \to \mathcal{H}$ of $\mathcal{O}_U$-modules is the same as a map $\mathcal{F} \to j_* \mathcal{H}$. The unit $\mathcal{F} \to j_* (\mathcal{F}|_U)$ is not injective in general: for $\mathcal{F} = k(p)$ with $p \notin U$ it is zero. The functor $j_*$ is left exact but not right exact. Exercise 5 gives a surjection on $U$ whose pushforward is not surjective.

### Proof

The proof uses one lemma.

*Lemma.* Let $\mathcal{A}$ be a sheaf of rings and $\varphi: \mathcal{F} \to \mathcal{G}$ a morphism of sheaves between $\mathcal{A}$-modules. If every stalk map $\varphi_x$ is $\mathcal{A}_x$-linear, then $\varphi$ is $\mathcal{A}$-linear. Indeed, for $a \in \mathcal{A}(U)$ and $s \in \mathcal{F}(U)$, the sections $\varphi(a s)$ and $a \varphi(s)$ have the same germ $a_x \varphi_x(s_x)$ at every $x \in U$, so they are equal by Proposition P2.5.4.

*Part 1.* Step one: extension of scalars. Let $\rho: \mathcal{A} \to \mathcal{B}$ be a morphism of sheaves of rings, $\mathcal{M}$ an $\mathcal{A}$-module and $\mathcal{F}$ a $\mathcal{B}$-module, viewed as an $\mathcal{A}$-module through $\rho$. Then
$$\operatorname{Hom}_{\mathcal{B}}(\mathcal{M} \otimes_{\mathcal{A}} \mathcal{B}, \mathcal{F}) \cong \operatorname{Hom}_{\mathcal{A}}(\mathcal{M}, \mathcal{F}), \qquad \psi \mapsto (m \mapsto \psi(m \otimes 1)).$$
To see this, note that by part 1 of Theorem P2.6.3 a $\mathcal{B}$-linear map out of $\mathcal{M} \otimes_{\mathcal{A}} \mathcal{B}$ is a $\mathcal{B}$-linear map of presheaves out of $U \mapsto \mathcal{M}(U) \otimes_{\mathcal{A}(U)} \mathcal{B}(U)$. By the universal property of extension of scalars of modules (P1 Ch. 1), this is a family of $\mathcal{A}(U)$-linear maps $\mathcal{M}(U) \to \mathcal{F}(U)$, compatible with restriction, that is, an $\mathcal{A}$-linear map $\mathcal{M} \to \mathcal{F}$.

Step two: the inverse image. Let $\mathcal{G}$ be an $\mathcal{O}_Y$-module and $\mathcal{F}$ an $\mathcal{O}_X$-module, viewed as an $f^{-1} \mathcal{O}_Y$-module through $f^\flat$. The bijection $\operatorname{Hom}_{\mathsf{Ab}(X)}(f^{-1} \mathcal{G}, \mathcal{F}) \cong \operatorname{Hom}_{\mathsf{Ab}(Y)}(\mathcal{G}, f_* \mathcal{F})$ of Theorem P2.5.28 sends $\alpha$ to $f_*(\alpha) \circ \eta$, where $\eta: \mathcal{G} \to f_* f^{-1} \mathcal{G}$ is the unit, and sends $\beta$ to $\varepsilon \circ f^{-1}(\beta)$, where $\varepsilon: f^{-1} f_* \mathcal{F} \to \mathcal{F}$ is the counit. It suffices to show that $\alpha$ is $f^{-1} \mathcal{O}_Y$-linear if and only if $f_*(\alpha) \circ \eta$ is $\mathcal{O}_Y$-linear. If $\alpha$ is linear, then $f_*(\alpha)$ is linear over $f_* f^{-1} \mathcal{O}_Y$, so over $\mathcal{O}_Y$. The unit $\eta$ sends $s \in \mathcal{G}(V)$ to the section $(s_{f(x)})_{x \in f^{-1} V}$ of $f^{-1} \mathcal{G}$, and so it is $\mathcal{O}_Y$-linear. Conversely, let $\beta$ be $\mathcal{O}_Y$-linear. On the stalk at $x$, with $y = f(x)$, the map $f^{-1}(\beta)$ is $\beta_y: \mathcal{G}_y \to (f_* \mathcal{F})_y$, and $\varepsilon_x: (f_* \mathcal{F})_y \to \mathcal{F}_x$ sends the germ of a section over $f^{-1}(V)$ to its germ at $x$. Both are $\mathcal{O}_{Y,y}$-linear, where $\mathcal{O}_{Y,y}$ acts on $\mathcal{F}_x$ through $f^\#_x$. By the lemma, $\varepsilon \circ f^{-1}(\beta)$ is linear. So
$$\operatorname{Hom}_{f^{-1} \mathcal{O}_Y}(f^{-1} \mathcal{G}, \mathcal{F}) \cong \operatorname{Hom}_{\mathcal{O}_Y}(\mathcal{G}, f_* \mathcal{F}).$$
Compose with step one for $\mathcal{A} = f^{-1} \mathcal{O}_Y$, $\mathcal{B} = \mathcal{O}_X$ and $\mathcal{M} = f^{-1} \mathcal{G}$. Both bijections are natural, so their composite is natural.

*Part 2.* By part 2 of Theorem P2.6.13 and Proposition P2.5.29,
$$(f^* \mathcal{G})_x \cong (f^{-1} \mathcal{G})_x \otimes_{(f^{-1} \mathcal{O}_Y)_x} \mathcal{O}_{X,x} = \mathcal{G}_{f(x)} \otimes_{\mathcal{O}_{Y, f(x)}} \mathcal{O}_{X,x}.$$

*Part 3.* A left adjoint is right exact and commutes with all colimits, in particular with direct sums, and a right adjoint is left exact and commutes with limits (Proposition P2.2.30 and Theorem P2.1.43).

*Part 4.* By part 5 of Theorem P2.6.13, $f^* \mathcal{O}_Y = f^{-1} \mathcal{O}_Y \otimes_{f^{-1} \mathcal{O}_Y} \mathcal{O}_X \cong \mathcal{O}_X$. Since $f^*$ commutes with direct sums, $f^*(\mathcal{O}_Y^{(I)}) \cong \mathcal{O}_X^{(I)}$. For the tensor product, first note that $f_* \mathcal{H}om_{\mathcal{O}_X}(f^* \mathcal{G}', \mathcal{F}) \cong \mathcal{H}om_{\mathcal{O}_Y}(\mathcal{G}', f_* \mathcal{F})$. Indeed, over an open $V \subseteq Y$ both sides are the two sides of part 1 for the restriction $f^{-1}(V) \to V$ of $f$, and $f^*$ commutes with restriction to $f^{-1}(V)$, since every step of its construction does. Then, for every $\mathcal{O}_X$-module $\mathcal{F}$, part 1 and part 3 of Theorem P2.6.13 give natural isomorphisms
$$\begin{aligned} \operatorname{Hom}(f^* \mathcal{G} \otimes f^* \mathcal{G}', \mathcal{F}) &\cong \operatorname{Hom}(f^* \mathcal{G}, \mathcal{H}om(f^* \mathcal{G}', \mathcal{F})) \cong \operatorname{Hom}(\mathcal{G}, f_* \mathcal{H}om(f^* \mathcal{G}', \mathcal{F})) \\ &\cong \operatorname{Hom}(\mathcal{G}, \mathcal{H}om(\mathcal{G}', f_* \mathcal{F})) \cong \operatorname{Hom}(\mathcal{G} \otimes \mathcal{G}', f_* \mathcal{F}) \cong \operatorname{Hom}(f^*(\mathcal{G} \otimes \mathcal{G}'), \mathcal{F}). \end{aligned}$$
By the Yoneda lemma (Corollary P2.1.24), $f^* \mathcal{G} \otimes f^* \mathcal{G}' \cong f^*(\mathcal{G} \otimes \mathcal{G}')$.

*Part 5.* The equality $(g f)_* = g_* f_*$ holds on sections, and the module structures agree, since $(g f)^\# = g_*(f^\#) \circ g^\#$. Then $f^* g^*$ is left adjoint to $g_* f_* = (g f)_*$, as is $(g f)^*$. Two left adjoints of the same functor are isomorphic (Theorem P2.1.32). $\square$

### Exercises

1. (A) Let $f: X \to Y$ be a morphism of ringed spaces. Show that $f_*$ sends ideal sheaves of $\mathcal{O}_X$ to $f_* \mathcal{O}_X$-submodules of $f_* \mathcal{O}_X$, and that the unit $\mathcal{O}_Y \to f_* f^* \mathcal{O}_Y = f_* \mathcal{O}_X$ of the adjunction is $f^\#$.
2. (A) Show that $f^*$ sends a surjection $\mathcal{O}_Y^n \to \mathcal{G}$ to a surjection $\mathcal{O}_X^n \to f^* \mathcal{G}$. Deduce that if $\mathcal{G}$ is generated by finitely many global sections, then so is $f^* \mathcal{G}$.
3. (A) Let $i: Z \to X$ be a closed immersion as in Example P2.6.23. Show that the counit $i^* i_* \mathcal{G} \to \mathcal{G}$ is an isomorphism for every $\mathcal{O}_Z$-module $\mathcal{G}$.
4. (B) Let $\pi: \mathbb{A}^1 \to \operatorname{Spec} k$ be the structure map. Show that $\pi_* \mathcal{O}_{\mathbb{A}^1}$ is the vector space $k[x]$. Let $X = \mathbb{R}$ with its continuous functions, $p: X \to (\mathrm{pt}, \mathbb{R})$ and $\mathcal{F} = \bigoplus_{n \geq 1} n_* \mathbb{R}$, a sum of skyscraper sheaves at the positive integers. Show that $p_* \mathcal{F} = \Gamma(X, \mathcal{F}) \cong \prod_n \mathbb{R}$, so that $p_*$ does not commute with infinite direct sums.
5. (B) Let $X = \mathbb{A}^2$, $U = X \setminus \{0\}$ and $j: U \to X$ the inclusion. Show that $j_* \mathcal{O}_U = \mathcal{O}_X$, using that a regular function on $U$ extends to $X$ (P3 Ch. 8). Let $Z \subseteq X$ be the line $x = 0$. Show that $\mathcal{O}_U \to \mathcal{O}_{Z \cap U}$ is surjective while $j_* \mathcal{O}_U \to j_* \mathcal{O}_{Z \cap U}$ is not, by looking at the section $1/y$.
6. (B) Let $f: X \to Y$ be a morphism of locally ringed spaces and $\mathcal{L}$ an $\mathcal{O}_Y$-module with $\mathcal{L}_y \cong \mathcal{O}_{Y,y}$ for all $y$. Show that $(f^* \mathcal{L})_x \cong \mathcal{O}_{X,x}$ for all $x$. Give an example where $f_* \mathcal{O}_X$ has stalks that are not free of rank one, with $f$ a finite map of curves.
7. (C) Let $f: X \to Y$ be a morphism of ringed spaces. Show that the natural map $f^* \mathcal{H}om(\mathcal{G}, \mathcal{G}') \to \mathcal{H}om(f^* \mathcal{G}, f^* \mathcal{G}')$ exists, and that it is an isomorphism if $\mathcal{G} \cong \mathcal{O}_Y^n$. Show by an example with $f$ the inclusion of a point that it is not an isomorphism in general.

### Lean

Mathlib defines `SheafOfModules.pushforward` and `SheafOfModules.pullback` for a continuous functor of sites with a morphism of sheaves of rings, and proves the adjunction `SheafOfModules.pullbackPushforwardAdjunction`, with `SheafOfModules.pullbackComp` and `SheafOfModules.pushforwardComp` for composites. For schemes the same functors are `AlgebraicGeometry.Scheme.Modules.pushforward` and `AlgebraicGeometry.Scheme.Modules.pullback`, with the adjunction `AlgebraicGeometry.Scheme.Modules.pullbackPushforwardAdjunction`, and for an open immersion `AlgebraicGeometry.Scheme.Modules.restrictFunctorIsoPullback` identifies pullback with restriction as in Example P2.6.25. The sheaf $\widetilde{M}$ of Example P2.6.20 is `AlgebraicGeometry.tilde`, with the adjunction to global sections `AlgebraicGeometry.tilde.adjunction`. The stalk formula of part 2 and the compatibility with tensor products are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

The inverse image of a module as $f^{-1} \mathcal{G} \otimes_{f^{-1} \mathcal{O}_Y} \mathcal{O}_X$ is Grothendieck's definition in EGA. Pullback is the sheaf form of base change of modules, and pushforward is the sheaf form of restriction of scalars. Their failure to be exact on the wrong side is the source of the derived functors $\mathbf{R} f_*$ and $\mathbf{L} f^*$ of Chapter 8, and of the higher direct images used throughout P4.
