---
title: Restriction and subadditivity
nodes: []
sources: [Laz04, DEL00, Har77]
reads_with: [Laz04:9.5, Laz04:9.2, DEL00:sec2]
requires: [P2.4, P4.4, P7.8, P7.9, P7.10, 4.2, 4.6]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Restriction and subadditivity

### Statement

Throughout the chapter $k$ is an algebraically closed field of characteristic $0$ and $X$ is a smooth variety of dimension $n$, not necessarily projective. The multiplier ideals $\mathcal{J}(X, D)$ and $\mathcal{J}(X, \mathfrak{a}^c)$ are those of Definition P7.10.2. That definition is local on $X$, and so are the proofs of Lemma P7.10.3 and of part 1 of Proposition P7.10.4, so both hold on every smooth variety. Chapter P7.10 states the restriction theorem and the subadditivity theorem as black boxes (Theorems P7.10.11 and P7.10.12). This section proves both. The proofs need three lemmas: local vanishing on a smooth variety that need not be projective, the freedom to compute a multiplier ideal on any smooth model, and the replacement of an ideal by general members.

**Lemma 5.4.1 (local vanishing on a smooth variety).** Let $D$ be an effective $\mathbb{Q}$-divisor on $X$ with a log resolution $\mu \colon X' \to X$, and $\mathfrak{a}$ a nonzero ideal with a log resolution $\mu$ and $\mathfrak{a} \mathcal{O}_{X'} = \mathcal{O}_{X'}(-F)$. Then for $j > 0$ and every rational $c \geq 0$,
$$R^j \mu_* \mathcal{O}_{X'}(K_{X'/X} - \lfloor \mu^* D \rfloor) = 0, \qquad R^j \mu_* \mathcal{O}_{X'}(K_{X'/X} - \lfloor c F \rfloor) = 0.$$

Lean: not yet in Lean.

**Lemma 5.4.2 (any smooth model computes the multiplier ideal).** Let $D$ be an effective $\mathbb{Q}$-divisor on $X$ and $f \colon Y \to X$ a proper birational morphism from a smooth variety such that $f^* D$ has snc support. Then
$$\mathcal{J}(X, D) = f_* \mathcal{O}_Y(K_{Y/X} - \lfloor f^* D \rfloor).$$

Lean: not yet in Lean.

The exceptional locus of $f$ need not be a divisor, and $f^* D + \operatorname{Exc}(f)$ need not have snc support. For ideals the same freedom is part 1 of Proposition P7.10.4.

**Lemma 5.4.3 (general members).** Let $X$ be affine, $\mathfrak{a}_1, \dots, \mathfrak{a}_r$ nonzero ideals with generators $g_{i1}, \dots, g_{is_i}$ of $\mathfrak{a}_i$, and $\mu \colon X' \to X$ a proper birational morphism from a smooth variety with $\mathfrak{a}_i \mathcal{O}_{X'} = \mathcal{O}_{X'}(-F_i)$ such that $\sum_i F_i + \operatorname{Exc}(\mu)$ has snc support. Fix an integer $k \geq 1$. For $1 \leq i \leq r$ and $1 \leq j \leq k$ let $h_{ij} = \sum_l \lambda_{ijl} g_{il}$ be a linear combination of the generators. Then there is a dense open set $\Omega$ of the space of coefficients $(\lambda_{ijl})$ such that for $(\lambda_{ijl}) \in \Omega$:

1. $\mu^* \operatorname{div}(h_{ij}) = F_i + M_{ij}$, where the $M_{ij}$ are reduced divisors, no two with a common component, none with a component in $\sum_i F_i + \operatorname{Exc}(\mu)$, and $\sum_i F_i + \operatorname{Exc}(\mu) + \sum_{i, j} M_{ij}$ has snc support;
2. for all rational $c_1, \dots, c_r$ with $0 \leq c_i < k$, the divisor $D = \sum_i \frac{c_i}{k} \sum_j \operatorname{div}(h_{ij})$ has
$$\mathcal{J}(X, D) = \mu_* \mathcal{O}_{X'}\Big(K_{X'/X} - \Big\lfloor \sum_i c_i F_i \Big\rfloor\Big) = \mathcal{J}(\mathfrak{a}_1^{c_1} \cdots \mathfrak{a}_r^{c_r}).$$

Lean: not yet in Lean.

The right side is the mixed multiplier ideal of Theorem P7.10.12, computed on $\mu$. For $r = 1$ and $\mu$ a log resolution of $\mathfrak{a}_1$, part 2 says $\mathcal{J}(\mathfrak{a}^c) = \mathcal{J}(\frac{c}{k} \sum_j \operatorname{div}(h_j))$ for $k$ general members $h_j$ of $\mathfrak{a}$, with one open set that works for every $c < k$.

**Theorem 5.4.4 (restriction).** Let $H \subset X$ be a smooth prime divisor and $D$ an effective $\mathbb{Q}$-divisor whose support does not contain $H$.

1. $\mathcal{J}(H, D|_H) \subseteq \mathcal{J}(X, D) \cdot \mathcal{O}_H$.
2. Let $V$ be a finite-dimensional base point free linear system on $X$ whose general member is irreducible. For $H$ a general member of $V$, equality holds: $\mathcal{J}(H, D|_H) = \mathcal{J}(X, D) \cdot \mathcal{O}_H$.
3. If $\mathfrak{a}$ is a nonzero ideal with $\mathfrak{a} \mathcal{O}_H \neq 0$ and $c \geq 0$ is rational, then $\mathcal{J}(H, (\mathfrak{a} \mathcal{O}_H)^c) \subseteq \mathcal{J}(X, \mathfrak{a}^c) \cdot \mathcal{O}_H$.

Lean: not yet in Lean.

Part 1 is Theorem P7.10.11. In part 2, Bertini's theorem (Har77, Corollary III.10.9 and Remark III.10.9.2) gives irreducibility when the morphism defined by $V$ has an image of dimension at least $2$.

**Corollary 5.4.5 (thresholds go down under restriction).** In the setting of Theorem 5.4.4, let $x \in H$. If $\mathcal{J}(H, c D|_H)$ is trivial at $x$, so is $\mathcal{J}(X, cD)$. In particular $\operatorname{lct}_x(H; D|_H) \leq \operatorname{lct}_x(X; D)$, and the same holds for an ideal $\mathfrak{a}$ with $\mathfrak{a} \mathcal{O}_H \neq 0$.

Lean: not yet in Lean.

**Lemma 5.4.6 (products).** Let $X_1$, $X_2$ be smooth varieties and $D_1$, $D_2$ effective $\mathbb{Q}$-divisors on them, with projections $p_i \colon X_1 \times X_2 \to X_i$. Then
$$\mathcal{J}(X_1 \times X_2, p_1^* D_1 + p_2^* D_2) = p_1^{-1} \mathcal{J}(X_1, D_1) \cdot p_2^{-1} \mathcal{J}(X_2, D_2) \cdot \mathcal{O}_{X_1 \times X_2}.$$

Lean: not yet in Lean.

**Theorem 5.4.7 (subadditivity; Demailly, Ein and Lazarsfeld).** Let $D_1$, $D_2$ be effective $\mathbb{Q}$-divisors on $X$, $\mathfrak{a}$, $\mathfrak{b}$ nonzero ideals and $c, d \geq 0$ rational. Then
$$\mathcal{J}(D_1 + D_2) \subseteq \mathcal{J}(D_1) \cdot \mathcal{J}(D_2), \qquad \mathcal{J}(\mathfrak{a}^c \mathfrak{b}^d) \subseteq \mathcal{J}(\mathfrak{a}^c) \cdot \mathcal{J}(\mathfrak{b}^d).$$

Lean: not yet in Lean.

This is Theorem P7.10.12.

**Corollary 5.4.8 (powers).** For every nonzero ideal $\mathfrak{a}$, rational $c \geq 0$ and integer $m \geq 1$, $\mathcal{J}(\mathfrak{a}^{mc}) \subseteq \mathcal{J}(\mathfrak{a}^c)^m$, and $\mathcal{J}(mD) \subseteq \mathcal{J}(D)^m$ for every effective $\mathbb{Q}$-divisor $D$.

Lean: not yet in Lean.

### Proof in words

Local vanishing is the relative Kawamata-Viehweg theorem for the birational morphism $\mu$, applied to the klt pair $(X', \{\mu^* D\})$: the divisor $-\mu^* D$ is numerically trivial over $X$, and every divisor is big over $X$ because $\mu$ is birational. The freedom of the model comes from comparing two models on a third one, where Lemma P7.10.3 says that further blow-ups do not change the push-forward. General members of an ideal pull back to the fixed part $F$ plus a smooth moving part in general position, and with a coefficient below $1$ the moving part disappears from the round-down.

For restriction, take a log resolution of $D + H$. The strict transform $H'$ of $H$ is smooth, and adjunction on both sides, written with residues, gives $K_{H'/H} = (K_{X'/X} - \sum_j b_j E_j)|_{H'}$, where $\mu^* H = H' + \sum_j b_j E_j$. The sheaf $\mathcal{O}_{X'}(K_{X'/X} - \lfloor \mu^* D \rfloor - \sum_j b_j E_j)$ restricts onto the sheaf whose push-forward is $\mathcal{J}(H, D|_H)$, and the kernel of the restriction is the sheaf of local vanishing for $D + H$. So the push-forward of the restriction map is onto, and its source lies in $\mathcal{J}(X, D)$. For a general $H$ all the $b_j$ vanish and the source is $\mathcal{J}(X, D)$ itself.

Subadditivity is restriction to the diagonal. On $X \times X$ the multiplier ideal of $p_1^* D_1 + p_2^* D_2$ is the product of the two ideals, and the diagonal is cut out, near each point, by $n$ functions whose successive zero loci are smooth. Restriction along this chain of $n$ smooth divisors gives the inclusion. Ideals reduce to divisors by general members.

### Examples

**Example 5.4.9 (restricting the cusp).** Let $C = \{y^2 = x^3\} \subset \mathbb{A}^2$, so $\mathcal{J}(\mathbb{A}^2, cC) = \mathcal{O}$ for $c < \frac56$ and $\mathcal{J}(\mathbb{A}^2, cC) = \mathfrak{m} = (x, y)$ for $\frac56 \leq c < 1$, by Example P7.10.7. Let $H = \{x = 0\}$ with coordinate $y$. Then $C|_H = \operatorname{div}(y^2) = 2[0]$, and Proposition P7.10.4, part 2, gives $\mathcal{J}(H, c C|_H) = (y^{\lfloor 2c \rfloor})$. At $c = \frac12$ the left side of Theorem 5.4.4 is $(y)$ and the right side is $\mathcal{O}_H$: the inclusion is strict. At $c = \frac56$ the left side is $(y^{\lfloor 5/3 \rfloor}) = (y)$ and the right side is $\mathfrak{m} \mathcal{O}_H = (y)$: equality. Corollary 5.4.5 reads $\frac12 = \operatorname{lct}_0(H; C|_H) \leq \operatorname{lct}_0(\mathbb{A}^2; C) = \frac56$. For $H = \{y = 0\}$, $C|_H = 3[0]$ and the bound is $\frac13 \leq \frac56$. For the general line $H = \{x = \lambda\}$ with $\lambda \neq 0$, $C|_H = \operatorname{div}(y^2 - \lambda^3)$ is two reduced points, $\mathcal{J}(H, cC|_H) = \mathcal{O}_H$ for $c < 1$, and $\mathcal{J}(\mathbb{A}^2, cC) \cdot \mathcal{O}_H = \mathcal{O}_H$ because $H$ misses the origin: part 2 of the theorem.

**Example 5.4.10 (subadditivity in the plane).** Let $\mathfrak{m} \subset k[x, y]$ be the ideal of the origin. By Example P7.10.8, $\mathcal{J}(\mathfrak{m}^c) = \mathfrak{m}^{\lfloor c \rfloor - 1}$, read as $\mathcal{O}$ when $c < 2$. Corollary 5.4.8 with $m = 2$ says $\mathfrak{m}^{\lfloor 2c \rfloor - 1} \subseteq \mathfrak{m}^{2 \lfloor c \rfloor - 2}$, which holds because $\lfloor 2c \rfloor \geq 2 \lfloor c \rfloor$. At $c = 2$ it reads $\mathfrak{m}^3 \subseteq \mathfrak{m}^2$, strict. For the cusp $C = \{f = 0\}$, $f = y^2 - x^3$, $\mathcal{J}(\frac53 C) = (f) \cdot \mathcal{J}(\frac23 C) = (f)$ by Lemma 5.4.22 below and Example P7.10.7, while $\mathcal{J}(\frac56 C)^2 = \mathfrak{m}^2$. The inclusion $(f) \subseteq \mathfrak{m}^2$ of Corollary 5.4.8 holds since $f$ has order $2$ at the origin.

### Proof

*Proof of Lemma 5.4.1.* The divisor $\Delta = \{\mu^* D\}$ has snc support and coefficients in $[0, 1)$, so $(X', \Delta)$ is klt by Proposition 4.2.13. Put $N = K_{X'} - \lfloor \mu^* D \rfloor$, a Cartier divisor on the smooth variety $X'$. Then $N - (K_{X'} + \Delta) = -\mu^* D$, which has degree $0$ on every curve contracted by $\mu$, so it is $\mu$-nef. It is $\mu$-big because $\mu$ is birational: the generic fibre is a point. Theorem P7.9.5 gives $R^j \mu_* \mathcal{O}_{X'}(N) = 0$ for $j > 0$. Choose a canonical divisor $K_X$ and $K_{X'}$ with $K_{X'/X} = K_{X'} - \mu^* K_X$. By the projection formula, Proposition P4.4.10, $R^j \mu_* \mathcal{O}_{X'}(K_{X'/X} - \lfloor \mu^* D \rfloor) = R^j \mu_* \mathcal{O}_{X'}(N) \otimes \mathcal{O}_X(-K_X) = 0$. For the ideal take $\Delta = \{cF\}$ and $N = K_{X'} - \lfloor cF \rfloor$, so $N - (K_{X'} + \Delta) = -cF$. The sheaf $\mathcal{O}_{X'}(-F) = \mathfrak{a} \mathcal{O}_{X'}$ is generated by the pull-backs of local generators of $\mathfrak{a}$, so it is generated by its sections over $\mu^{-1}(U)$ for affine $U \subseteq X$, and so it has nonnegative degree on every curve contracted by $\mu$. Hence $-cF$ is $\mu$-nef, and it is $\mu$-big as before. The same argument applies. $\square$

*Proof of Lemma 5.4.2.* Let $\mu \colon X' \to X$ be a log resolution of $D$, and let $Z$ be a resolution of the closure of the graph of the birational map $X' \dashrightarrow Y$, with proper birational morphisms $p \colon Z \to X'$ and $q \colon Z \to Y$ such that $\mu p = f q =: g$. Write $G = K_{Z/X} - \lfloor g^* D \rfloor$. Since $K_{Z/X} = p^* K_{X'/X} + K_{Z/X'}$ and $p^* K_{X'/X}$ is integral,
$$G = p^* K_{X'/X} + K_{Z/X'} - \lfloor p^* (\mu^* D) \rfloor.$$
Lemma P7.10.3 on $X'$, for the snc divisor $B = \mu^* D$, and the projection formula give $p_* \mathcal{O}_Z(G) = \mathcal{O}_{X'}(K_{X'/X} - \lfloor \mu^* D \rfloor)$, so $g_* \mathcal{O}_Z(G) = \mathcal{J}(X, D)$. The same computation with $q$ and the snc divisor $f^* D$ on $Y$ gives $q_* \mathcal{O}_Z(G) = \mathcal{O}_Y(K_{Y/X} - \lfloor f^* D \rfloor)$, so $g_* \mathcal{O}_Z(G) = f_* \mathcal{O}_Y(K_{Y/X} - \lfloor f^* D \rfloor)$. $\square$

*Proof of Lemma 5.4.3.* Let $V_i \subseteq H^0(X', \mathcal{O}_{X'}(-F_i))$ be the span of the $\mu^* g_{il}$. Since $\mathfrak{a}_i \mathcal{O}_{X'} = \mathcal{O}_{X'}(-F_i)$, the sections in $V_i$ generate $\mathcal{O}_{X'}(-F_i)$, so $V_i$ is a base point free linear system, and the divisor of $\mu^* h$ as a section of $\mathcal{O}_{X'}(-F_i)$ is $M = \mu^* \operatorname{div}(h) - F_i$. Let $\mathcal{S}$ be the finite set of strata of the snc divisor $\sum_i F_i + \operatorname{Exc}(\mu)$: the connected components of the intersections of its components, together with $X'$ itself, each a smooth locally closed subvariety. By Bertini's theorem (Har77, Corollary III.10.9), applied to the restriction of $V_i$ to each stratum, a general member of $V_i$ meets every stratum in a smooth divisor of the stratum or not at all. So $M_{11}$ is smooth, has no component in $\sum_i F_i + \operatorname{Exc}(\mu)$, and the sum is snc; this is the argument of Proposition P7.8.8. Add the components of $M_{11}$ to the divisor and repeat for $M_{12}$, and so on. Each step is an open condition on the coefficients of one $h_{ij}$, and a smooth divisor that meets the previous ones transversally has no common component with them. The intersection of the finitely many open sets is the set $\Omega$, and part 1 follows. For part 2, $\mu^* D = \sum_i c_i F_i + \sum_{i, j} \frac{c_i}{k} M_{ij}$ has snc support. The $M_{ij}$ are reduced, have no component in common with each other or with the $F_i$, and have coefficient $\frac{c_i}{k} < 1$, so $\lfloor \mu^* D \rfloor = \lfloor \sum_i c_i F_i \rfloor$. Lemma 5.4.2 gives the first equality, and the second is the definition. $\square$

*Proof of Theorem 5.4.4.* Part 1. Let $\mu \colon X' \to X$ be a log resolution of $D + H$, and write $\mu^* H = H' + \sum_j b_j E_j$ with $H'$ the strict transform and $E_j$ exceptional, $b_j \geq 0$. The divisor $H'$ is irreducible and is a component of an snc divisor, so it is smooth, and $\mu_H = \mu|_{H'} \colon H' \to H$ is proper and birational. Since $H \not\subseteq \operatorname{Supp} D$, $H'$ is not a component of $\mu^* D$, and the other components of the snc divisor $\mu^*(D + H) + \operatorname{Exc}(\mu)$ meet $H'$ transversally. So $\mu_H^*(D|_H) = (\mu^* D)|_{H'}$ has snc support on $H'$, and distinct components of $\mu^* D$ restrict to reduced divisors of $H'$ with no common component. Hence
$$\lfloor \mu_H^* (D|_H) \rfloor = \lfloor \mu^* D \rfloor |_{H'}.$$
Next, the relative canonical divisors. Near a point of $H$ let $\omega$ be a generator of $\omega_X$ and $h$ an equation of $H$. The residue $\operatorname{Res}_H(\omega / h)$ generates $\omega_H$. On $X'$ the rational form $\mu^*(\omega / h)$ has divisor $K_{X'/X} - H' - \sum_j b_j E_j$, a simple pole along $H'$, so its residue along $H'$ is a rational form on $H'$ with divisor $(K_{X'/X} - \sum_j b_j E_j)|_{H'}$. Over the open set where $\mu$ is an isomorphism, which meets $H$ because $\mu$ is an isomorphism off a closed set of codimension at least $2$, the residues agree: $\operatorname{Res}_{H'} \mu^*(\omega/h) = \mu_H^* \operatorname{Res}_H(\omega/h)$, so they agree everywhere. Its divisor is therefore $K_{H'/H}$, and
$$K_{H'/H} = \Big( K_{X'/X} - \sum_j b_j E_j \Big) \Big|_{H'}.$$
Put $P = K_{X'/X} - \lfloor \mu^* D \rfloor - \sum_j b_j E_j$. Then $P|_{H'} = K_{H'/H} - \lfloor \mu_H^*(D|_H) \rfloor$ and $P - H' = K_{X'/X} - \lfloor \mu^*(D + H) \rfloor$, because $\mu^* H$ is integral. The exact sequence
$$0 \to \mathcal{O}_{X'}(P - H') \to \mathcal{O}_{X'}(P) \to \mathcal{O}_{H'}(P|_{H'}) \to 0$$
and $R^1 \mu_* \mathcal{O}_{X'}(P - H') = 0$, Lemma 5.4.1 for $D + H$, show that $\mu_* \mathcal{O}_{X'}(P) \to \mu_{H*} \mathcal{O}_{H'}(P|_{H'})$ is onto. The target is $\mathcal{J}(H, D|_H)$ by Lemma 5.4.2. Since $P \leq K_{X'/X} - \lfloor \mu^* D \rfloor$, the source lies in $\mathcal{J}(X, D) \subseteq \mathcal{O}_X$. A local section of the source is a regular function $\varphi$ on $X$, and the map sends it to $\varphi|_{H'} = \mu_H^*(\varphi|_H)$. So $\mathcal{J}(H, D|_H)$ is the image of $\mu_* \mathcal{O}_{X'}(P)$ in $\mathcal{O}_H$, which lies in $\mathcal{J}(X, D) \cdot \mathcal{O}_H$.

Part 2. Let $\mu$ be a log resolution of $D$. The pull-back of $V$ to $X'$ is base point free. By Bertini's theorem, applied on $X$ and on each stratum of $\mu^* D + \operatorname{Exc}(\mu)$, a general $H \in V$ is smooth and irreducible, is not a component of $D$, and $\mu^* H$ is smooth and meets the snc divisor transversally. Then $\mu^* H = H'$ has no exceptional component, $\mu$ is a log resolution of $D + H$, all $b_j = 0$, and $P = K_{X'/X} - \lfloor \mu^* D \rfloor$. The proof of part 1 shows that $\mathcal{J}(X, D) = \mu_* \mathcal{O}_{X'}(P)$ maps onto $\mathcal{J}(H, D|_H)$, and the image of $\mathcal{J}(X, D)$ in $\mathcal{O}_H$ is $\mathcal{J}(X, D) \cdot \mathcal{O}_H$.

Part 3. The statement is local, so let $X$ be affine with generators $g_l$ of $\mathfrak{a}$, and choose an integer $k > c$. Apply Lemma 5.4.3 to $\mathfrak{a}$ on $X$, with a log resolution, and to $\mathfrak{a} \mathcal{O}_H$ on $H$, with the generators $g_l|_H$ and a log resolution of $\mathfrak{a} \mathcal{O}_H$. Restriction of coefficients is the identity on the coefficient space, so the two dense open sets meet, and for $k$ general members $h_j$ the divisor $D = \frac{c}{k} \sum_j \operatorname{div}(h_j)$ has $\mathcal{J}(X, D) = \mathcal{J}(X, \mathfrak{a}^c)$ and $\mathcal{J}(H, D|_H) = \mathcal{J}(H, (\mathfrak{a} \mathcal{O}_H)^c)$. Since $\mathfrak{a} \mathcal{O}_H \neq 0$, a general $h_j$ does not vanish on $H$, so $H \not\subseteq \operatorname{Supp} D$, and part 1 applies. $\square$

*Proof of Corollary 5.4.5.* Let $I = \mathcal{J}(X, cD)$. If $\mathcal{J}(H, cD|_H)_x = \mathcal{O}_{H, x}$, then $I \cdot \mathcal{O}_{H, x} = \mathcal{O}_{H,x}$ by Theorem 5.4.4, so $I_x \not\subseteq \mathfrak{m}_x$ and $I_x = \mathcal{O}_{X, x}$. By Proposition P7.10.5 and Corollary 4.6.4, $\operatorname{lct}_x$ is the supremum of the $c$ with $\mathcal{J}(cD)$ trivial at $x$, on $H$ and on $X$, and the inequality follows. For ideals use part 3. $\square$

*Proof of Lemma 5.4.6.* Let $\mu_i \colon X_i' \to X_i$ be log resolutions of $D_i$ and $\mu = \mu_1 \times \mu_2$. It is proper and birational, $X_1' \times X_2'$ is smooth, and $\mu^*(p_1^* D_1 + p_2^* D_2) = q_1^* \mu_1^* D_1 + q_2^* \mu_2^* D_2$, with $q_i$ the projections of $X_1' \times X_2'$. In local coordinates $(s, t)$ adapted to the two snc divisors, its components are $\{s_a = 0\}$ and $\{t_b = 0\}$, so it has snc support. Pull-backs of the components of $\mu_1^* D_1$ and of $\mu_2^* D_2$ have no common component, so $\lfloor \mu^*(p_1^* D_1 + p_2^* D_2) \rfloor = q_1^* \lfloor \mu_1^* D_1 \rfloor + q_2^* \lfloor \mu_2^* D_2 \rfloor$. With $K_{X_1' \times X_2' / X_1 \times X_2} = q_1^* K_{X_1'/X_1} + q_2^* K_{X_2'/X_2}$ this gives
$$\mathcal{O}(K_{X'/X} - \lfloor \mu^* D \rfloor) = q_1^* \mathcal{G}_1 \otimes q_2^* \mathcal{G}_2, \qquad \mathcal{G}_i = \mathcal{O}_{X_i'}(K_{X_i'/X_i} - \lfloor \mu_i^* D_i \rfloor).$$
Over affine opens $U_1 \times U_2$, the Künneth formula in degree $0$ gives $H^0(\mu_1^{-1} U_1 \times \mu_2^{-1} U_2, q_1^* \mathcal{G}_1 \otimes q_2^* \mathcal{G}_2) = H^0(\mu_1^{-1} U_1, \mathcal{G}_1) \otimes_k H^0(\mu_2^{-1} U_2, \mathcal{G}_2)$: the Čech complex of the product for the product cover is the tensor product of the two Čech complexes, and the kernel of the first differential of a tensor product over a field is the tensor product of the kernels. By Lemma 5.4.2 the left side of the lemma is $\mathcal{J}(D_1)(U_1) \otimes_k \mathcal{J}(D_2)(U_2)$, a subspace of $\mathcal{O}(U_1) \otimes_k \mathcal{O}(U_2)$, and this subspace is the product ideal of the right side. $\square$

*Proof of Theorem 5.4.7.* The statement is local. Let $x \in X$ and choose an irreducible affine open $U \ni x$ and $t_1, \dots, t_n \in \mathcal{O}(U)$ whose differentials form a basis of $\Omega_U$. Replace $X$ by $U$. On $Y = X \times X$ put $f_i = p_1^* t_i - p_2^* t_i$ and $Z_l = V(f_1, \dots, f_l)$. The differentials $df_1, \dots, df_n$ are linearly independent at every point of $Y$, so each $Z_l$ is smooth of dimension $2n - l$ by the Jacobian criterion. The scheme $Z_n = X \times_{\mathbb{A}^n} X$ is étale over $X$ by base change, so the diagonal $\Delta_X \subseteq Z_n$ is open, because $t$ is unramified, and closed, because $X$ is separated. Let $W_l$ be the connected component of $Z_l$ that contains the connected set $\Delta_X$. Then $W_0 = Y$, $W_n = \Delta_X$, each $W_l$ is smooth and irreducible, and $W_{l+1}$ is a connected component of $V(f_{l+1}) \cap W_l$, a smooth divisor of $W_l$; so $W_{l+1}$ is a smooth prime divisor of $W_l$. Let $D = p_1^* D_1 + p_2^* D_2$. Its restriction to $\Delta_X \cong X$ is $D_1 + D_2$, a divisor, so $\Delta_X \not\subseteq \operatorname{Supp} D$, and hence no $W_l$ lies in $\operatorname{Supp} D$. Theorem 5.4.4 for $W_{l+1} \subset W_l$ gives
$$\mathcal{J}(W_{l+1}, D|_{W_{l+1}}) \subseteq \mathcal{J}(W_l, D|_{W_l}) \cdot \mathcal{O}_{W_{l+1}},$$
and by induction $\mathcal{J}(\Delta_X, D|_{\Delta_X}) \subseteq \mathcal{J}(Y, D) \cdot \mathcal{O}_{\Delta_X}$. Under $\Delta_X \cong X$ the left side is $\mathcal{J}(D_1 + D_2)$, and by Lemma 5.4.6 the right side is $\mathcal{J}(D_1) \cdot \mathcal{J}(D_2)$.

For ideals, let $X$ be affine and $\mu$ a proper birational morphism from a smooth variety with $\mathfrak{a} \mathcal{O}_{X'} = \mathcal{O}(-F_{\mathfrak{a}})$, $\mathfrak{b} \mathcal{O}_{X'} = \mathcal{O}(-F_{\mathfrak{b}})$ and $F_{\mathfrak{a}} + F_{\mathfrak{b}} + \operatorname{Exc}(\mu)$ of snc support. Such a $\mu$ exists: take a log resolution $\mu_1$ of $\mathfrak{a}$, then a log resolution $\mu_2$ of the ideal $\mathfrak{b} \mathcal{O}_{X_1} \cdot \mathcal{O}_{X_1}(-E)$, where $E$ is the reduced divisor on $F_{\mathfrak{a}} + \operatorname{Exc}(\mu_1)$, and put $\mu = \mu_1 \mu_2$. Choose $k > \max(c, d)$ and general members as in Lemma 5.4.3 with $r = 2$, and put $D_1 = \frac{c}{k} \sum_j \operatorname{div}(h_{1j})$, $D_2 = \frac{d}{k} \sum_j \operatorname{div}(h_{2j})$. Part 2 of the lemma, with $(c_1, c_2)$ equal to $(c, d)$, $(c, 0)$ and $(0, d)$, gives $\mathcal{J}(\mathfrak{a}^c \mathfrak{b}^d) = \mathcal{J}(D_1 + D_2)$, $\mathcal{J}(\mathfrak{a}^c) = \mathcal{J}(D_1)$ and $\mathcal{J}(\mathfrak{b}^d) = \mathcal{J}(D_2)$, and the divisor case applies. $\square$

*Proof of Corollary 5.4.8.* On a log resolution of $\mathfrak{a}$, $\mathcal{J}(\mathfrak{a}^{c} \mathfrak{a}^{c'}) = \mu_* \mathcal{O}(K_{X'/X} - \lfloor (c + c') F \rfloor) = \mathcal{J}(\mathfrak{a}^{c + c'})$. Theorem 5.4.7 and induction on $m$ give $\mathcal{J}(\mathfrak{a}^{mc}) \subseteq \mathcal{J}(\mathfrak{a}^{(m-1)c}) \cdot \mathcal{J}(\mathfrak{a}^c) \subseteq \mathcal{J}(\mathfrak{a}^c)^m$. The divisor case is the same. $\square$

### Exercises

1. (A) Let $D = \frac32 \{y = 0\}$ on $\mathbb{A}^2$ and $H = \{y = x^2\}$. Compute $D|_H$, the two sides of Theorem 5.4.4, and decide whether the inclusion is strict.
2. (A) Let $C = \{y^2 = x^3\}$ and $H = \{y = \lambda x\}$ with $\lambda \neq 0$. Show that $C|_H$ is $2[0] + [\lambda^2]$ in the coordinate $x$ of $H$, and compute $\operatorname{lct}_0(H; C|_H)$. Compare with Corollary 5.4.5.
3. (B) Let $\mathfrak{a} = (x^2, y^3) \subset k[x, y]$, and $H = \{x = 0\}$. Compute $\mathfrak{a} \mathcal{O}_H$, both sides of part 3 of Theorem 5.4.4 for $c = 1$, and check the inclusion with Theorem P7.10.17.
4. (B) Show that subadditivity can be strict for divisors with no common component: on $\mathbb{A}^2$ take $D_1 = \frac34 \{x = 0\} + \frac34 \{y = 0\}$ and $D_2 = \frac34 \{x = y\}$. Compute $\mathcal{J}(D_1)$, $\mathcal{J}(D_2)$ and $\mathcal{J}(D_1 + D_2)$ by one blow-up.
5. (B) Prove that $\mathcal{J}(X, D)$ is compatible with étale maps: if $\phi \colon X_1 \to X$ is étale, then $\mathcal{J}(X_1, \phi^* D) = \phi^{-1} \mathcal{J}(X, D) \cdot \mathcal{O}_{X_1}$. Hint: base change a log resolution, and use flat base change, Theorem P4.5.1.
6. (C) Let $\mathfrak{a} \subseteq \mathfrak{m} = (x_1, \dots, x_n)$ be a nonzero ideal of $k[x_1, \dots, x_n]$ and $l \geq 1$ an integer. Show that $\mathcal{J}(\mathfrak{a}^c) \subseteq \mathfrak{m}^l$ for every rational $c \geq l n$. Hint: Corollary 5.4.8 gives $\mathcal{J}(\mathfrak{a}^c) \subseteq \mathcal{J}(\mathfrak{a}^{c/l})^l$, and $\mathcal{J}(\mathfrak{a}^{n}) \subseteq \mathfrak{a}$ by Theorem P7.10.13. For $\mathfrak{a} = \mathfrak{m}$ and $n = 2$, compare with Example 5.4.10.

### Lean

None of the statements of this section is in Lean. The Lean library has no multiplier ideals and no log resolutions.

### Notes and history

Local vanishing and the restriction theorem in this form are in Lazarsfeld, Theorem 9.4.1 and Theorem 9.5.1 (Laz04). The restriction theorem is the algebraic shadow of the Ohsawa-Takegoshi extension theorem, through which Siu and later Hacon and McKernan extend pluricanonical forms; Chapter 5 returns to it. Subadditivity was proved by Demailly, Ein and Lazarsfeld (DEL00) with the diagonal argument used here, and applied to Fujita's conjecture and to the asymptotic invariants of linear series. The reduction of ideals to general members is Lazarsfeld, Proposition 9.2.26 (Laz04).
