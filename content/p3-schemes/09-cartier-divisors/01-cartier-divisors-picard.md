---
title: Cartier divisors and the Picard group
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch14, Har77:II.6, GW20:ch11]
requires: [P1.8, P2.6, P2.7, P3.5, P3.6, P3.8]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Cartier divisors and the Picard group

### Statement

Throughout this chapter $X$ is an integral scheme with generic point $\eta$ and function field $K = \mathcal{O}_{X, \eta}$. For every nonempty open $U$, $\mathcal{O}_X(U)$ and every local ring $\mathcal{O}_{X, x}$ are subrings of $K$, and the restriction maps are inclusions (Proposition P3.2.24). So for an open cover $U = \bigcup_i U_i$ the sheaf axiom reads $\mathcal{O}_X(U) = \bigcap_i \mathcal{O}_X(U_i)$ inside $K$. Write $\mathcal{K}$ for the constant sheaf $K$, the quasi-coherent sheaf of Example P3.5.5. The space $X$ is irreducible, so every nonempty open set is connected, and $\mathcal{K}(U) = K$ for $U \neq \emptyset$.

**Definition P3.9.1 (Cartier divisor).** A *Cartier datum* on $X$ is a family $\{(U_i, f_i)\}$ of an open cover $(U_i)$ of $X$ and elements $f_i \in K^*$ such that $f_i/f_j \in \mathcal{O}_X(U_i \cap U_j)^*$ for all $i, j$. Two data are *equivalent* if their union is again a Cartier datum. A *Cartier divisor* is an equivalence class. The $f_i$ are *local equations* of $D$.

1. The Cartier divisors form an abelian group $\operatorname{CaDiv}(X)$, written additively: $\{(U_i, f_i)\} + \{(V_j, g_j)\} = \{(U_i \cap V_j, f_i g_j)\}$, with $0 = \{(X, 1)\}$ and $-\{(U_i, f_i)\} = \{(U_i, f_i^{-1})\}$.
2. For $g \in K^*$ the *principal* Cartier divisor is $\operatorname{div}(g) = \{(X, g)\}$. The map $g \mapsto \operatorname{div}(g)$ is a homomorphism $K^* \to \operatorname{CaDiv}(X)$. Two Cartier divisors are *linearly equivalent*, $D \sim D'$, if $D - D'$ is principal, and the quotient is the *Cartier class group* $\operatorname{CaCl}(X)$.
3. $D$ is *effective*, $D \geq 0$, if it has a datum with $f_i \in \mathcal{O}_X(U_i)$ for all $i$.
4. The *support* $\operatorname{Supp} D$ is the set of $x \in U_i$ with $f_i \notin \mathcal{O}_{X, x}^*$.

A Cartier divisor is the same as a global section of the quotient sheaf $\mathcal{K}^*/\mathcal{O}_X^*$ (Exercise 5). Every datum has the same support, and every datum of an effective divisor has $f_i \in \mathcal{O}_X(U_i)$ (Exercise 1).

Lean: not in Lean as stated.

**Proposition P3.9.2 (effective Cartier divisors).** Let $D = \{(U_i, f_i)\}$ be effective.

1. The ideal sheaves $f_i \mathcal{O}_{U_i} \subseteq \mathcal{O}_{U_i}$ glue to an ideal sheaf $\mathcal{I}_D \subseteq \mathcal{O}_X$, which is invertible. The closed subscheme it defines is also written $D$. Its underlying set is $\operatorname{Supp} D$.
2. $D \mapsto \mathcal{I}_D$ is a bijection from the effective Cartier divisors to the invertible ideal sheaves $\mathcal{I} \subseteq \mathcal{O}_X$, and so to the closed subschemes whose ideal sheaf is invertible.
3. $\mathcal{I}_{D + E} = \mathcal{I}_D \mathcal{I}_E$ for effective $D, E$, and $E - D$ is effective if and only if $\mathcal{I}_E \subseteq \mathcal{I}_D$.

Lean: not in Lean as stated.

**Proposition P3.9.3 (the invertible sheaf of a Cartier divisor).** For $D = \{(U_i, f_i)\}$ let $\mathcal{O}_X(D) \subseteq \mathcal{K}$ be the sub-$\mathcal{O}_X$-module with $\mathcal{O}_X(D)|_{U_i} = f_i^{-1} \mathcal{O}_{U_i}$.

1. $\mathcal{O}_X(D)$ is well defined and invertible, and $a \mapsto a f_i^{-1}$ is an isomorphism $\mathcal{O}_{U_i} \to \mathcal{O}_X(D)|_{U_i}$.
2. $\mathcal{O}_X(0) = \mathcal{O}_X$, $\mathcal{O}_X(D + E) = \mathcal{O}_X(D) \cdot \mathcal{O}_X(E)$ inside $\mathcal{K}$, and multiplication is an isomorphism $\mathcal{O}_X(D) \otimes \mathcal{O}_X(E) \to \mathcal{O}_X(D + E)$. In particular $\mathcal{O}_X(-D) \cong \mathcal{O}_X(D)^\vee$.
3. If $D$ is effective, then $\mathcal{O}_X(-D) = \mathcal{I}_D$ and $\mathcal{O}_X \subseteq \mathcal{O}_X(D)$.
4. For $g \in K^*$, multiplication by $g$ is an isomorphism $\mathcal{O}_X(D) \to \mathcal{O}_X(D - \operatorname{div}(g))$.
5. $\Gamma(X, \mathcal{O}_X(D)) = \{ g \in K : g f_i \in \mathcal{O}_X(U_i) \text{ for all } i \}$. For $g \neq 0$ the condition says that $D + \operatorname{div}(g)$ is effective.

Lean: not in Lean as stated.

**Theorem P3.9.4 (Cartier divisors and line bundles).** The map $D \mapsto \mathcal{O}_X(D)$ induces an isomorphism of groups
$$
\operatorname{CaCl}(X) \xrightarrow{\ \sim\ } \operatorname{Pic}(X)
$$
onto the Picard group of Theorem P2.6.29. Equivalently, the sequence
$$
1 \to \mathcal{O}_X(X)^* \to K^* \xrightarrow{\operatorname{div}} \operatorname{CaDiv}(X) \to \operatorname{Pic}(X) \to 0
$$
is exact. Every invertible sheaf on $X$ is isomorphic to a subsheaf of $\mathcal{K}$.

Lean: Mathlib `ClassGroup.equivPic` is the affine case for a domain $R$: it identifies the group `ClassGroup R` of invertible fractional ideals modulo principal ones with `CommRing.Pic R` (definition and proved in Mathlib). `Submodule.mulExact_unitsMap_spanSingleton_unitsToPic` is the exactness of the affine sequence at the group of invertible submodules. The statement for schemes is not in Lean as stated.

### Proof in words

A Cartier divisor is a hypersurface given near each point by one equation, where two equations are identified when they differ by a unit. The equations of an effective divisor generate an ideal sheaf that is locally free of rank one, and their inverses generate an invertible subsheaf of the function field. Every line bundle on an integral scheme embeds into the function field, since a section is determined by its germ at the generic point. A local generator of the embedded line bundle is then the inverse of a local equation, and an isomorphism with the trivial bundle is a global equation. So Cartier divisors up to linear equivalence and line bundles up to isomorphism are the same thing.

### Examples

**Example P3.9.5 (hypersurfaces in projective space).** Let $X = \mathbb{P}^n_k$ and $F \in k[x_0, \dots, x_n]$ homogeneous of degree $d \geq 1$ and nonzero. Then $D_F = \{(D_+(x_i), F/x_i^d)\}$ is a Cartier datum: on $D_+(x_i) \cap D_+(x_j)$ the ratio $(F/x_i^d)/(F/x_j^d) = (x_j/x_i)^d$ is a unit. It is effective, and on $D_+(x_i)$ the ideal of $D_F$ is generated by $F/x_i^d$, which is the ideal of $V_+(F)$ in the chart (Corollary P3.6.15). So $D_F$ is the closed subscheme $V_+(F)$. It need not be reduced: $D_{x_0^2} = 2 D_{x_0}$ is the double hyperplane. The sheaf $\mathcal{O}_X(D_F)$ is generated by $x_i^d/F$ on $D_+(x_i)$, and $G \mapsto G/F$ on homogeneous elements of degree $d$ of the $S_{x_i}$ is an isomorphism $\mathcal{O}_X(d) \to \mathcal{O}_X(D_F)$, as in Proposition P3.8.30. In particular the hyperplane $H = D_{x_0}$ has $\mathcal{O}_X(H) \cong \mathcal{O}_X(1)$, and $D_F \sim dH$ because $D_F - dH = \operatorname{div}(F/x_0^d)$.

**Example P3.9.6 (affine schemes).** Let $X = \operatorname{Spec} A$ with $A$ a Noetherian domain. For a Cartier divisor $D$ the module $I = \Gamma(X, \mathcal{O}_X(D)) \subseteq K$ is a fractional ideal with $\widetilde{I} = \mathcal{O}_X(D)$, by Theorem P3.5.12, and it is invertible by Proposition P1.8.18, since it is locally principal. Exercise 3 shows that $D \mapsto I$ identifies $\operatorname{CaDiv}(X)$ with the group of invertible fractional ideals and $\operatorname{CaCl}(X)$ with $\operatorname{Pic}(A)$ of Definition P1.8.17. For $A = \mathbb{Z}[\sqrt{-5}]$ the ideal $\mathfrak{p} = (2, 1 + \sqrt{-5})$ is locally principal and not principal, so the line bundle $\widetilde{\mathfrak{p}}$ of Example P3.5.17 is $\mathcal{O}_X(-D)$ for the effective Cartier divisor $D$ with $\mathcal{I}_D = \widetilde{\mathfrak{p}}$, and $D$ is not principal.

**Example P3.9.7 (subschemes that are and are not Cartier divisors).** In $X = \mathbb{A}^2_k$ the subscheme $V(x^2)$, the doubled line, is the effective Cartier divisor $\operatorname{div}(x^2) = 2 \operatorname{div}(x)$. The origin $V(x, y)$ is not an effective Cartier divisor: its ideal $(x, y)$ is not invertible (Example P3.5.18). The same happens on the quadric cone $Y = \operatorname{Spec} A$, $A = k[x, y, z]/(xy - z^2)$. The function $x$ defines the effective Cartier divisor $\operatorname{div}(x)$, whose subscheme $V(x) = \operatorname{Spec} k[y, z]/(z^2)$ is a doubled line. Its reduced subscheme is the line $L = V(x, z)$, which is not an effective Cartier divisor, since the ideal $(x, z)$ needs two generators at the vertex (Example P3.8.32). So the subscheme of an effective Cartier divisor can be nonreduced while its reduction is not a Cartier divisor.

**Example P3.9.8 (the line with a doubled origin).** Let $X$ be the line with a doubled origin over $k$, glued from $U_0 = \operatorname{Spec} k[t]$ and $U_1 = \operatorname{Spec} k[t]$ along $U_0 \cap U_1 = \operatorname{Spec} k[t, t^{-1}]$, with function field $k(t)$. Then $D = \{(U_0, t), (U_1, 1)\}$ is a Cartier datum, as $t$ is a unit on $U_0 \cap U_1$. It is effective, and its subscheme is the origin $0$ of $U_0$, while it does not meet $U_1$. It is not principal. If $D = \operatorname{div}(g)$, then $g/t \in k[t]^* = k^*$ on $U_0$ and $g \in k[t]^* = k^*$ on $U_1$, which is impossible. Exercise 6 shows that $nD$ is not principal for $n \neq 0$, so $\operatorname{Pic}(X)$ contains a copy of $\mathbb{Z}$. Section 9.2 shows that $\operatorname{Pic}(X) = \mathbb{Z}$, in agreement with $\operatorname{Cl}(X) = \mathbb{Z}$ (Example P3.8.18).

### Proof

*Remarks on Definition P3.9.1.* The union of two data is a datum if and only if the ratios of their local equations are units on the overlaps. This relation is reflexive and symmetric. It is transitive: let $(U_i, f_i)$, $(V_j, g_j)$ and $(W_l, h_l)$ be data with the first two and the last two equivalent. On $U_i \cap W_l$ the element $f_i/h_l$ is a unit on each $U_i \cap W_l \cap V_j$, so $f_i/h_l$ and $h_l/f_i$ lie in $\bigcap_j \mathcal{O}_X(U_i \cap W_l \cap V_j) = \mathcal{O}_X(U_i \cap W_l)$. The sum of data is a datum, as the ratios $(f_i g_j)/(f_{i'} g_{j'})$ are products of units, and it respects equivalence for the same reason. So $\operatorname{CaDiv}(X)$ is an abelian group, and $\operatorname{div}$ is a homomorphism. The support does not depend on the datum, because local equations at a point differ by a unit of $\mathcal{O}_{X, x}$. It is closed: the set of $x \in U_i$ with $f_i \in \mathcal{O}_{X, x}^*$ is open, since an element of $K$ that lies in $\mathcal{O}_{X, x}$ lies in $\mathcal{O}_X(V)$ for an open $V \ni x$. It does not contain $\eta$, as $f_i \in K^* = \mathcal{O}_{X, \eta}^*$.

*Proof of Proposition P3.9.2.* (1) On $U_i \cap U_j$ write $f_i = u f_j$ with $u$ a unit. Then $f_i \mathcal{O}_{U_i \cap U_j} = f_j \mathcal{O}_{U_i \cap U_j}$. So the subsheaves $f_i \mathcal{O}_{U_i}$ agree on the overlaps, and they glue to a subsheaf $\mathcal{I}_D$ of $\mathcal{O}_X$: a section $s$ over $V$ lies in $\mathcal{I}_D(V)$ if $s|_{V \cap U_i} \in f_i \mathcal{O}_X(V \cap U_i)$ for all $i$. It is an ideal sheaf. The map $\mathcal{O}_{U_i} \to \mathcal{I}_D|_{U_i}$, $a \mapsto a f_i$, is surjective by definition and injective since every $\mathcal{O}_X(V)$ is a domain and $f_i \neq 0$. So $\mathcal{I}_D$ is invertible, and in particular quasi-coherent. Equivalent data give the same ideal sheaf, since on the overlaps the generators differ by units. On $U_i \cap \operatorname{Spec} B$ with $B$ affine, the subscheme is $V(f_i)$, and a point $x$ lies on it if and only if $f_i \in \mathfrak{m}_x$, that is, $f_i \notin \mathcal{O}_{X, x}^*$, as $f_i \in \mathcal{O}_{X, x}$.

(2) Let $\mathcal{I} \subseteq \mathcal{O}_X$ be an invertible ideal sheaf. Choose an open cover $(U_i)$ by nonempty open sets with $\mathcal{I}|_{U_i} \cong \mathcal{O}_{U_i}$, and let $s_i \in \mathcal{I}(U_i)$ be the image of $1$, so that $\mathcal{I}|_{U_i} = s_i \mathcal{O}_{U_i}$. Then $s_i \neq 0$. On $U_i \cap U_j$ both $s_i$ and $s_j$ generate $\mathcal{I}$, so $s_i = a s_j$ and $s_j = b s_i$ with $a, b \in \mathcal{O}_X(U_i \cap U_j)$. As this ring is a domain, $ab = 1$, and $s_i/s_j$ is a unit. So $\{(U_i, s_i)\}$ is an effective Cartier datum with ideal sheaf $\mathcal{I}$. Another choice of generators $s'_i$ differs by units, so it gives an equivalent datum. If $\mathcal{I}_D = \mathcal{I}_{D'}$ for effective $D = \{(U_i, f_i)\}$ and $D' = \{(V_j, g_j)\}$, then $f_i$ and $g_j$ generate the same ideal sheaf on $U_i \cap V_j$, so their ratio is a unit by the same argument, and $D = D'$. Closed subschemes correspond to ideal sheaves by Proposition P3.5.23.

(3) Locally $\mathcal{I}_{D + E}$ is generated by $f_i g_j$, which generates $\mathcal{I}_D \mathcal{I}_E$. If $E - D$ is effective, with local equations $g_j/f_i \in \mathcal{O}_X(U_i \cap V_j)$, then $g_j \in f_i \mathcal{O}$, so $\mathcal{I}_E \subseteq \mathcal{I}_D$. Conversely, if $\mathcal{I}_E \subseteq \mathcal{I}_D$, then $g_j = c f_i$ on $U_i \cap V_j$ with $c$ regular, and $c = g_j/f_i$ is a regular local equation of $E - D$. $\square$

*Proof of Proposition P3.9.3.* (1) On $U_i \cap U_j$, $f_i^{-1} \mathcal{O} = f_j^{-1} \mathcal{O}$, since $f_i/f_j$ is a unit. So the subsheaves $f_i^{-1} \mathcal{O}_{U_i} \subseteq \mathcal{K}|_{U_i}$ glue, as in the proof of Proposition P3.9.2, and an equivalent datum gives the same subsheaf. The map $a \mapsto a f_i^{-1}$ is surjective by definition and injective since the $\mathcal{O}_X(V)$ are subrings of the field $K$.

(2) $\mathcal{O}_X(0) = 1 \cdot \mathcal{O}_X$. On $U_i \cap V_j$ the product $\mathcal{O}_X(D) \cdot \mathcal{O}_X(E)$ is generated by $f_i^{-1} g_j^{-1}$, which generates $\mathcal{O}_X(D + E)$. The multiplication map sends the generator $f_i^{-1} \otimes g_j^{-1}$ of the free module $\mathcal{O}_X(D) \otimes \mathcal{O}_X(E)$ of rank one to the generator $(f_i g_j)^{-1}$ of $\mathcal{O}_X(D + E)$, so it is an isomorphism on each $U_i \cap V_j$, and so an isomorphism. For $E = -D$ it gives $\mathcal{O}_X(D) \otimes \mathcal{O}_X(-D) \cong \mathcal{O}_X$, and so $\mathcal{O}_X(-D) \cong \mathcal{O}_X(D)^\vee$ by part 1 of Theorem P2.6.29.

(3) $\mathcal{O}_X(-D)$ is generated by $f_i$ on $U_i$, as is $\mathcal{I}_D$. If $f_i \in \mathcal{O}_X(U_i)$, then $1 = f_i \cdot f_i^{-1} \in f_i^{-1} \mathcal{O}_X(U_i)$.

(4) Multiplication by $g$ is an automorphism of $\mathcal{K}$, and it maps $f_i^{-1} \mathcal{O}_{U_i}$ onto $(f_i/g)^{-1} \mathcal{O}_{U_i}$, the restriction of $\mathcal{O}_X(D - \operatorname{div}(g))$, as $D - \operatorname{div}(g) = \{(U_i, f_i/g)\}$.

(5) By the sheaf axiom, $g \in K$ is a global section if and only if $g \in f_i^{-1} \mathcal{O}_X(U_i)$ for every $i$, that is, $g f_i \in \mathcal{O}_X(U_i)$. For $g \neq 0$ the $g f_i$ are local equations of $D + \operatorname{div}(g)$. $\square$

*Proof of Theorem P3.9.4.* *A homomorphism.* By Proposition P3.9.3, $\mathcal{O}_X(D)$ is invertible, $\mathcal{O}_X(D + E) \cong \mathcal{O}_X(D) \otimes \mathcal{O}_X(E)$, and $\mathcal{O}_X(\operatorname{div}(g)) = g^{-1} \mathcal{O}_X \cong \mathcal{O}_X$. So $D \mapsto [\mathcal{O}_X(D)]$ is a homomorphism $\operatorname{CaDiv}(X) \to \operatorname{Pic}(X)$ that vanishes on principal divisors.

*Injective on $\operatorname{CaCl}(X)$.* Let $\psi \colon \mathcal{O}_X \to \mathcal{O}_X(D)$ be an isomorphism, and $g = \psi(1) \in \Gamma(X, \mathcal{O}_X(D)) \subseteq K$. Then $\mathcal{O}_X(D) = g \mathcal{O}_X$ and $g \neq 0$. On $U_i$ this says $f_i^{-1} \mathcal{O}_{U_i} = g \mathcal{O}_{U_i}$, so $g f_i$ and its inverse are regular on $U_i$. Then $f_i/g^{-1}$ is a unit on $U_i$, and $D = \operatorname{div}(g^{-1})$.

*Surjective.* Let $\mathcal{L}$ be invertible. First, for a nonempty open $U$, the map $\mathcal{L}(U) \to \mathcal{L}_\eta$ is injective. Indeed, let $s_\eta = 0$. Cover $U$ by nonempty open sets $V$ with $\mathcal{L}|_V \cong \mathcal{O}_V$. Under this isomorphism the map $\mathcal{L}(V) \to \mathcal{L}_\eta$ becomes the inclusion $\mathcal{O}_X(V) \subseteq K$, so $s|_V = 0$ for all $V$, and $s = 0$. The stalk $\mathcal{L}_\eta$ is a $K$-vector space of dimension one. Choose a basis $e$, and for $s \in \mathcal{L}(U)$ let $\varphi_U(s) \in K$ be the element with $s_\eta = \varphi_U(s) e$. The maps $\varphi_U$ are $\mathcal{O}_X(U)$-linear, injective and compatible with restriction, so they define an injective morphism $\varphi \colon \mathcal{L} \to \mathcal{K}$ of $\mathcal{O}_X$-modules, and $\mathcal{L}$ is isomorphic to its image $\mathcal{L}' \subseteq \mathcal{K}$. This proves the last claim. Let $(U_i)$ be a cover by nonempty open sets with $\mathcal{L}|_{U_i} = s_i \mathcal{O}_{U_i}$, and $g_i = \varphi(s_i) \in K^*$. Then $\mathcal{L}'|_{U_i} = g_i \mathcal{O}_{U_i}$. On $U_i \cap U_j$ both $g_i$ and $g_j$ generate $\mathcal{L}'$, so $g_i/g_j$ is a unit, as in the proof of Proposition P3.9.2. Thus $D = \{(U_i, g_i^{-1})\}$ is a Cartier divisor with $\mathcal{O}_X(D) = \mathcal{L}' \cong \mathcal{L}$.

*The exact sequence.* $\operatorname{div}(g) = 0$ means that $\{(X, g)\}$ and $\{(X, 1)\}$ are equivalent, that is, $g \in \mathcal{O}_X(X)^*$. The rest is the isomorphism just proved. $\square$

### Exercises

1. (A) Let $D$ be a Cartier divisor. Show that every datum of $D$ gives the same support, that $D = 0$ if and only if $\operatorname{Supp} D = \emptyset$, and that if $D$ is effective, then every datum $\{(V_j, g_j)\}$ of $D$ has $g_j \in \mathcal{O}_X(V_j)$.
2. (A) On $\mathbb{P}^n_k$ let $F$ and $G$ be nonzero forms of degrees $d$ and $e$. Show that $D_{FG} = D_F + D_G$, and that $D_F - D_G = \operatorname{div}(F/G)$ if $d = e$, in the notation of Example P3.9.5. Deduce $\mathcal{O}(D_F) \cong \mathcal{O}(D_G)$ when $d = e$.
3. (B) Let $X = \operatorname{Spec} A$ with $A$ a Noetherian domain. Show that $D \mapsto \Gamma(X, \mathcal{O}_X(D))$ is an isomorphism from $\operatorname{CaDiv}(X)$ onto the group of invertible fractional ideals, that it maps $\operatorname{div}(g)$ to $g^{-1} A$, and that it induces $\operatorname{CaCl}(X) \cong \operatorname{Pic}(A)$ in the sense of Definition P1.8.17.
4. (B) Let $D$ be an effective Cartier divisor with closed subscheme $i \colon D \to X$, and $\mathcal{L}$ an invertible sheaf. Show that $0 \to \mathcal{L} \otimes \mathcal{O}_X(-D) \to \mathcal{L} \to i_* i^* \mathcal{L} \to 0$ is exact.
5. (B) Show that a Cartier divisor is the same as a global section of the sheaf $\mathcal{K}^*/\mathcal{O}_X^*$, the sheaf associated to $U \mapsto K^*/\mathcal{O}_X(U)^*$, and that the exact sequence of sheaves $1 \to \mathcal{O}_X^* \to \mathcal{K}^* \to \mathcal{K}^*/\mathcal{O}_X^* \to 1$ gives the sequence of Theorem P3.9.4 together with Theorem P2.7.28, using that $\mathcal{K}^*$ is constant on an irreducible space and so has $H^1 = 0$.
6. (B) On the line with a doubled origin of Example P3.9.8 put $D' = \{(U_0, 1), (U_1, t)\}$. Show that $D + D' = \operatorname{div}(t)$, so that $D' \sim -D$, and that $nD$ is not principal for $n \neq 0$.
7. (C) Let $\mathcal{L}$ be invertible and $s \in \Gamma(X, \mathcal{L})$ nonzero. Show that the ideal sheaf generated locally by the image of $s$ under local trivializations defines an effective Cartier divisor $Z(s)$, its *divisor of zeros*, with $\mathcal{O}_X(Z(s)) \cong \mathcal{L}$. Show that every effective $D$ with $\mathcal{O}_X(D) \cong \mathcal{L}$ is $Z(s)$ for some $s$, and that $Z(s) = Z(s')$ if and only if $s' = us$ with $u \in \mathcal{O}_X(X)^*$.

### Lean

Mathlib has the Picard group of a commutative ring, `CommRing.Pic`, the group of isomorphism classes of invertible modules (`Module.Invertible`), in `Mathlib/RingTheory/PicardGroup.lean`. The same file has the homomorphism `Submodule.unitsToPic` from invertible submodules of an algebra to the Picard group, the exactness lemma `Submodule.mulExact_unitsMap_spanSingleton_unitsToPic`, and `ClassGroup.equivPic`, the isomorphism between `ClassGroup R` and `CommRing.Pic R` for a domain $R$. Together these are the affine case of Theorem P3.9.4 and of Exercise 3. Locally free sheaves of modules are `SheafOfModules.IsLocallyFree`. Cartier divisors, their sheaves and the Picard group of a scheme are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

The definition by local equations is due to Cartier, and the sheaf $\mathcal{K}^*/\mathcal{O}_X^*$ is the form in EGA IV. For a scheme that is not integral, $\mathcal{K}$ is replaced by the sheaf of total quotient rings, and the local equations are required to be nonzerodivisors. The map $\operatorname{CaCl}(X) \to \operatorname{Pic}(X)$ is then injective, and Hartshorne, Proposition II.6.13, proves this. Surjectivity needs hypotheses, and Hartshorne, Proposition II.6.15, proves it for integral schemes, which is Theorem P3.9.4. The literature state is theorem. In the minimal model program the varieties are integral, so line bundles and Cartier divisors up to linear equivalence are the same thing, and the language of divisors is used for both. The effective Cartier divisors of Proposition P3.9.2 are the subschemes that the program can restrict to: adjunction in Chapter 12 and the lifting of sections in P2 Ch. 7 both use the sequence of Exercise 4.
