---
title: Fibre products of schemes
nodes: []
sources: [Vak25, Har77, GW20, EGA1, Stacks]
reads_with: [Vak25:ch10, Har77:II.3, GW20:ch4]
requires: [P1.1, P2.1, P3.1, P3.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Fibre products of schemes

### Statement

**Definition P3.3.18 (fibre product).** Let $f \colon X \to S$ and $g \colon Y \to S$ be morphisms of schemes. A *fibre product* of $X$ and $Y$ over $S$ is a scheme $X \times_S Y$ with morphisms $p \colon X \times_S Y \to X$ and $q \colon X \times_S Y \to Y$ such that $f p = g q$, which is universal: for every scheme $T$ and morphisms $a \colon T \to X$, $b \colon T \to Y$ with $f a = g b$, there is exactly one morphism $(a, b) \colon T \to X \times_S Y$ with $p (a, b) = a$ and $q (a, b) = b$. In the language of the functor of points, $h_{X \times_S Y} = h_X \times_{h_S} h_Y$. A fibre product is unique up to unique isomorphism, by the Yoneda lemma P2.1.23. For a morphism $S' \to S$ and an $S$-scheme $X$, the $S'$-scheme $X_{S'} = X \times_S S'$ is the *base change* of $X$.

Lean: Mathlib `CategoryTheory.Limits.pullback` in the category `AlgebraicGeometry.Scheme`, with the instance `HasPullbacks Scheme` (definitions in Mathlib).

**Theorem P3.3.19 (existence of fibre products).** Fibre products exist in the category of schemes. If $S = \operatorname{Spec} R$, $X = \operatorname{Spec} A$ and $Y = \operatorname{Spec} B$, then $X \times_S Y = \operatorname{Spec}(A \otimes_R B)$, with $p$ and $q$ given by $a \mapsto a \otimes 1$ and $b \mapsto 1 \otimes b$.

Lean: Mathlib `AlgebraicGeometry.pullbackSpecIso` for the affine case, and the instance `HasPullbacks Scheme` (proved in Mathlib).

**Proposition P3.3.20 (open pieces and base change of closed immersions).** Let $X \times_S Y$ be a fibre product with projections $p, q$.

1. For open sets $U \subseteq X$, $V \subseteq Y$ and $W \subseteq S$ with $f(U) \subseteq W$ and $g(V) \subseteq W$, the open subscheme $p^{-1}(U) \cap q^{-1}(V)$ is a fibre product $U \times_W V$.
2. If $Z \to X$ is a closed immersion, then $Z \times_X Y \to Y$ is a closed immersion. If $X = \operatorname{Spec} A$, $Y = \operatorname{Spec} B$ and $Z = \operatorname{Spec} A/I$, then $Z \times_X Y = \operatorname{Spec} B/IB$.
3. If $Z_1 = V(I)$ and $Z_2 = V(J)$ are closed subschemes of $\operatorname{Spec} A$, then $Z_1 \times_{\operatorname{Spec} A} Z_2 = V(I + J)$, the scheme-theoretic intersection $Z_1 \cap Z_2$.

Lean: Mathlib proves the stability of `AlgebraicGeometry.IsClosedImmersion` under base change as an instance; parts 1 and 3 are not in Lean as stated.

### Proof in words

In the affine case the fibre product is the spectrum of the tensor product: morphisms into an affine scheme are ring maps out of its ring of functions, by Theorem P3.1.22, and the tensor product is the pushout of rings. For general schemes the fibre product is glued. If $X$ is covered by open sets $X_i$, the products $X_i \times_S Y$ glue along the products $X_{ij} \times_S Y$. The gluing data exist because a fibre product, once it exists, has the correct open pieces.

The points of $X \times_S Y$ are not the pairs of points. Over a field $k$, a point of $X \times_k Y$ is a pair of points $x, y$ together with a point of $\operatorname{Spec}(\kappa(x) \otimes_k \kappa(y))$, and this ring can have many primes.

### Examples

**Example P3.3.21 (products of affine spaces).** Over a ring $R$, $\mathbb{A}^m_R \times_R \mathbb{A}^n_R = \operatorname{Spec}(R[x_1, \dots, x_m] \otimes_R R[y_1, \dots, y_n]) = \mathbb{A}^{m+n}_R$. Also $\mathbb{A}^n_R = \mathbb{A}^n_{\mathbb{Z}} \times_{\mathbb{Z}} \operatorname{Spec} R$, since $\mathbb{Z}[x_1, \dots, x_n] \otimes_{\mathbb{Z}} R = R[x_1, \dots, x_n]$.

**Example P3.3.22 (projective space by base change).** For a ring $A$, $\mathbb{P}^n_A \cong \mathbb{P}^n_{\mathbb{Z}} \times_{\mathbb{Z}} \operatorname{Spec} A$. Cover $\mathbb{P}^n_{\mathbb{Z}}$ by the charts $U_i = \operatorname{Spec} \mathbb{Z}[x_0/x_i, \dots, x_n/x_i]$ of Definition P3.2.10. By part 1 of Proposition P3.3.20 the product is covered by the open sets $U_i \times_{\mathbb{Z}} \operatorname{Spec} A = \operatorname{Spec} A[x_0/x_i, \dots, x_n/x_i]$, and they are glued by the same formulas as the charts of $\mathbb{P}^n_A$. So every property of $\mathbb{P}^n_A$ that is stable under base change can be proved over $\mathbb{Z}$.

**Example P3.3.23 (the product of two points can have two points).** $\operatorname{Spec} \mathbb{C} \times_{\operatorname{Spec} \mathbb{R}} \operatorname{Spec} \mathbb{C} = \operatorname{Spec}(\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C})$. Since $\mathbb{C} = \mathbb{R}[x]/(x^2 + 1)$, the tensor product is $\mathbb{C}[x]/(x^2 + 1) = \mathbb{C}[x]/((x - i)(x + i)) \cong \mathbb{C} \times \mathbb{C}$, by the Chinese remainder theorem. So the product of two one-point schemes has two points. For a finite Galois extension $L/K$ the same computation shows that $L \otimes_K L \cong L^{[L : K]}$, so $\operatorname{Spec}(L \otimes_K L)$ has $[L : K]$ points.

**Example P3.3.24 (the product is not the product of spaces).** The underlying space of $\mathbb{A}^1_k \times_k \mathbb{A}^1_k = \mathbb{A}^2_k$ is not the product of the spaces. The generic point of $\mathbb{A}^2_k$ and the generic point of the diagonal $V(x - y)$ both map to the pair (generic point, generic point). The topology is not the product topology either, even on the closed points when $k$ is algebraically closed: Example P0.3.9 shows that the diagonal is closed in $\mathbb{A}^2$ but not in the product topology.

**Example P3.3.25 (the points of a product over a field).** Let $k$ be a field and $X, Y$ schemes over $k$. For $x \in X$ and $y \in Y$, the points of $X \times_k Y$ that map to $x$ and $y$ correspond to the points of $\operatorname{Spec}(\kappa(x) \otimes_k \kappa(y))$ (Exercise 5). This ring is never zero, since a tensor product of two nonzero vector spaces is nonzero. For $x$ and $y$ the generic points of two copies of $\mathbb{A}^1_k$, the ring is $k(s) \otimes_k k(t)$, a localization of $k[s, t]$. Its primes are the primes $\mathfrak{q}$ of $k[s, t]$ with $\mathfrak{q} \cap k[s] = 0$ and $\mathfrak{q} \cap k[t] = 0$: the zero ideal and the irreducible curves that dominate both axes, such as $s - t$.

**Example P3.3.26 (intersections that are not reduced).** In $\mathbb{A}^2_k$ the parabola $V(y - x^2)$ and the line $V(y)$ meet in $V(y, y - x^2) = \operatorname{Spec} k[x, y]/(y, x^2) = \operatorname{Spec} k[x]/(x^2)$, by part 3 of Proposition P3.3.20. The intersection is a point with multiplicity $2$, and the dimension $2$ of its ring over $k$ is the intersection multiplicity of P0 Ch. 7. The reduced intersection is only the point, and it forgets the tangency.

### Proof

*Proof of Theorem P3.3.19.* Step 1, the affine case. Let $S = \operatorname{Spec} R$, $X = \operatorname{Spec} A$, $Y = \operatorname{Spec} B$ and $P = \operatorname{Spec}(A \otimes_R B)$, with $p, q$ as stated. Then $f p = g q$ since the two composites $R \to A \otimes_R B$ agree. For a scheme $T$, Theorem P3.1.22 gives natural bijections of $\operatorname{Hom}(T, P)$ with $\operatorname{Hom}(A \otimes_R B, \Gamma(T))$, and of pairs $(a, b)$ with $f a = g b$ with pairs of ring maps $A \to \Gamma(T)$, $B \to \Gamma(T)$ that agree on $R$. These sets are in bijection by the universal property of the tensor product of $R$-algebras (P1 Ch. 1). So $P$ is a fibre product.

Step 2, open pieces. Suppose $X \times_S Y$ exists, and let $U \subseteq X$ be open. Then $p^{-1}(U)$, with the restrictions of $p$ and $q$, is a fibre product $U \times_S Y$. Indeed, given $a \colon T \to U$ and $b \colon T \to Y$ with $f a = g b$, the morphism $(a, b) \colon T \to X \times_S Y$ has $p (a, b) = a$ with image in $U$, so it factors uniquely through the open subscheme $p^{-1}(U)$ of Proposition P3.2.2: a morphism with image in an open set factors uniquely through the open subscheme, by restriction of the sheaf maps. The same holds for open sets of $Y$, and for an open $W \subseteq S$ with $f(X) \subseteq W$ and $g(Y) \subseteq W$ the product over $W$ is the product over $S$, since a morphism to $S$ with image in $W$ is the same as a morphism to $W$. Together these prove part 1 of Proposition P3.3.20, once existence is known.

Step 3, gluing over $X$. Let $X = \bigcup_i X_i$ be an open cover and suppose that every $X_i \times_S Y$ exists, with projections $p_i, q_i$. Let $U_{ij} = p_i^{-1}(X_i \cap X_j) \subseteq X_i \times_S Y$. By step 2 both $U_{ij}$ and $U_{ji}$ are fibre products $(X_i \cap X_j) \times_S Y$, so there is a unique isomorphism $\varphi_{ji} \colon U_{ij} \to U_{ji}$ that commutes with the projections. On triple overlaps $\varphi_{kj} \varphi_{ji} = \varphi_{ki}$, because both sides are isomorphisms of fibre products $(X_i \cap X_j \cap X_k) \times_S Y$ compatible with the projections, and such an isomorphism is unique. By Theorem P3.2.3 the $X_i \times_S Y$ glue to a scheme $P$. The morphisms $p_i$ and $q_i$ agree on overlaps, so by Proposition P3.2.4 they glue to $p \colon P \to X$ and $q \colon P \to Y$. Given $a \colon T \to X$ and $b \colon T \to Y$ with $f a = g b$, let $T_i = a^{-1}(X_i)$. There is a unique $c_i \colon T_i \to X_i \times_S Y \subseteq P$ with the right projections. On $T_i \cap T_j$ the morphisms $c_i$ and $c_j$ both land in the open piece over $X_i \cap X_j$ and have the same projections, so they agree by uniqueness in step 2. They glue to $c \colon T \to P$ by Proposition P3.2.4, and $c$ is unique since its restriction to each $T_i$ is. So $P$ is a fibre product.

Step 4, $S$ affine. If $S$ and $Y$ are affine, cover $X$ by affine open sets $X_i$; the $X_i \times_S Y$ exist by step 1, so $X \times_S Y$ exists by step 3. If only $S$ is affine, cover $Y$ by affine open sets $Y_j$. The products $X \times_S Y_j$ exist, and step 3 with the roles of $X$ and $Y$ exchanged gives $X \times_S Y$.

Step 5, general $S$. Cover $S$ by affine open sets $S_i$, and let $X_i = f^{-1}(S_i)$ and $Y_i = g^{-1}(S_i)$. By step 4 the products $X_i \times_{S_i} Y_i$ exist. A morphism $T \to X_i$ and a morphism $T \to Y$ that agree over $S$ have the second one with image in $Y_i$. So $X_i \times_{S_i} Y_i$ is a fibre product $X_i \times_S Y$. The $X_i$ cover $X$, and step 3 gives $X \times_S Y$. $\square$

*Proof of Proposition P3.3.20.* Part 1 is step 2 of the proof above, applied twice.

Part 2. The question is local on $Y$, by part 1 of Proposition P3.3.11 and part 1 of the present proposition, and also local on $X$, since the preimage of an open $U \subseteq X$ in $Z$ is a closed subscheme of $U$. So let $X = \operatorname{Spec} A$, $Y = \operatorname{Spec} B$, and, by Theorem P3.3.10, $Z = \operatorname{Spec} A/I$. Then $Z \times_X Y = \operatorname{Spec}(A/I \otimes_A B) = \operatorname{Spec} B/IB$, since $A/I \otimes_A B \cong B/IB$ (P1 Ch. 1). The morphism to $Y$ is given by the surjection $B \to B/IB$, so it is a closed immersion by Proposition P3.1.32.

Part 3. By part 2, $Z_1 \times_{\operatorname{Spec} A} Z_2 = \operatorname{Spec}((A/I) \otimes_A (A/J)) = \operatorname{Spec} A/(I + J)$. It is the largest closed subscheme contained in $Z_1$ and in $Z_2$, by Theorem P3.3.10. $\square$

### Exercises

1. (A) Compute $\operatorname{Spec} \mathbb{Q}(\sqrt{2}) \times_{\mathbb{Q}} \operatorname{Spec} \mathbb{Q}(\sqrt{2})$ and $\operatorname{Spec} \mathbb{Q}(\sqrt[3]{2}) \times_{\mathbb{Q}} \operatorname{Spec} \mathbb{Q}(\sqrt[3]{2})$. How many points does each have, and what are the residue fields?
2. (A) Let $k$ be a field of characteristic $p > 0$ and $K = k(t)$, $L = K(t^{1/p})$. Show that $\operatorname{Spec}(L \otimes_K L)$ has one point and is not reduced.
3. (A) Show that $X \times_S S \cong X$, that $X \times_S Y \cong Y \times_S X$, and that $(X \times_S Y) \times_Y Z \cong X \times_S Z$ for $S$-morphisms $Z \to Y$.
4. (B) Let $f \colon X \to S$ be a morphism and $S' \to S$ any morphism. Show that if $f$ is an open immersion, then the base change $X \times_S S' \to S'$ is an open immersion onto the preimage of $f(X)$.
5. (B) Let $X, Y$ be schemes over a field $k$, and let $x \in X$, $y \in Y$. Show that the set of points of $X \times_k Y$ that map to $x$ and to $y$ is in bijection with $\operatorname{Spec}(\kappa(x) \otimes_k \kappa(y))$. (Use part 1 of Proposition P3.3.20 to reduce to affine schemes, and then compute the fibre of $\operatorname{Spec}(A \otimes_k B) \to \operatorname{Spec} A \times \operatorname{Spec} B$ over $(\mathfrak{p}, \mathfrak{q})$.)
6. (B) Show that if $X$ and $Y$ are of finite type over $k$ and $k$ is algebraically closed, then the closed points of $X \times_k Y$ are in bijection with the pairs of closed points of $X$ and $Y$.
7. (C) Show that $\mathbb{P}^1_k \times_k \mathbb{P}^1_k$ is not isomorphic to $\mathbb{P}^2_k$. (One approach: two closed curves in $\mathbb{P}^2_k$ always meet, by Corollary P0.7.16 or by a direct argument with $V(F) \cap V(G)$; find two disjoint closed curves in $\mathbb{P}^1_k \times_k \mathbb{P}^1_k$.)

### Lean

Mathlib constructs fibre products of schemes in `Mathlib/AlgebraicGeometry/Pullbacks.lean`. The gluing argument is the same as the one above, and the result is the instance `HasPullbacks Scheme`. The affine case is the isomorphism `AlgebraicGeometry.pullbackSpecIso` between the pullback of spectra and the spectrum of the tensor product. Stability of closed immersions under base change is an instance. The handbook adds no `MinimalModel` node here.

### Notes and history

The construction of fibre products by gluing is in EGA I, Chapter I, and in Hartshorne, Section II.3. The literature state is theorem. Fibre products give the fibres of a morphism in Section 3.4, base change of families over a base, and the diagonal that defines separated morphisms in Chapter 4. In the program every family of varieties, such as the families of the semistable reduction theorem in P8, is studied through its base changes.
