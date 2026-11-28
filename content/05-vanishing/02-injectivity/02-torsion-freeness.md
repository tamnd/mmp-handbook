---
title: Torsion freeness and Kollár vanishing
nodes: []
sources: [Kol86a, Kol86b, EV92, Fuj11, KM98, Laz04, Har77]
reads_with: [Kol86a:theorem-2-1, Fuj11:ch3, Laz04:ch4]
requires: [P2.4, P4.2, P4.4, P7.8, P7.9, 1.3, 4.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Torsion freeness and Kollár vanishing

### Statement

Let $(X, \Delta)$ be a klt pair with $X$ projective, $f \colon X \to Z$ a surjective morphism onto a projective variety and $d = \dim X - \dim Z$. The three theorems concern a $\mathbb{Q}$-Cartier Weil divisor $N$ on $X$ whose adjoint part $N - (K_X + \Delta)$ comes from $Z$. They generalize Theorem P7.9.13, which is the case $X$ smooth, $\Delta = 0$ and $N = K_X$.

**Theorem 5.2.8 (torsion freeness).** Let $X$ be a normal projective variety, $(X, \Delta)$ a klt pair, $f \colon X \to Z$ a surjective morphism onto a projective variety, $N$ a $\mathbb{Q}$-Cartier Weil divisor on $X$ and $A$ a $\mathbb{Q}$-Cartier $\mathbb{Q}$-divisor on $Z$ with $N - (K_X + \Delta) \sim_\mathbb{Q} f^* A$. Then $R^j f_* \mathcal{O}_X(N)$ is torsion free for every $j \geq 0$.

Lean: not yet in Lean. `MinimalModel.KollarTorsionFreeness` states the case $X$ smooth, $\Delta$ with snc support and $\lfloor \Delta \rfloor = 0$, and $A = 0$.

**Theorem 5.2.9 (vanishing above the relative dimension).** In the situation of Theorem 5.2.8, $R^j f_* \mathcal{O}_X(N) = 0$ for $j > d$.

Lean: not yet in Lean.

**Theorem 5.2.10 (Kollár vanishing).** In the situation of Theorem 5.2.8, assume that $A$ is ample. Then $H^i(Z, R^j f_* \mathcal{O}_X(N)) = 0$ for every $i > 0$ and every $j \geq 0$.

Lean: not yet in Lean.

**Corollary 5.2.11 (the canonical sheaf).** Let $X$ be a normal projective variety with klt singularities and $f \colon X \to Z$ a surjective morphism onto a projective variety. Then the sheaves $R^j f_* \mathcal{O}_X(K_X)$ are torsion free, they vanish for $j > d$, and $H^i(Z, R^j f_* \mathcal{O}_X(K_X) \otimes \mathcal{O}_Z(A)) = 0$ for every ample Cartier divisor $A$ on $Z$, every $i > 0$ and every $j$. For $X$ smooth this is Theorem P7.9.13.

Lean: not yet in Lean.

### Proof in words

A torsion section of $R^j f_* \mathcal{O}_X(N)$ is supported on a proper closed subset $W$ of $Z$, so it is killed by every function vanishing to high order along $W$. After twisting by a large multiple of an ample divisor on $Z$, the Leray spectral sequence identifies $H^j(X, \mathcal{O}_X(N))$ with $H^0(Z, R^j f_* \mathcal{O}_X(N))$, and a section $s$ of a power of an ample divisor that vanishes along $W$ pulls back to a divisor $B = f^* \operatorname{div}(s)$ proportional to the semiample class $f^* A$. Kollár injectivity says multiplication by $f^* s$ is injective on $H^j(X, \cdot)$, while it kills the torsion section. So there is no torsion. Over a dense open subset of $Z$ the fibres have dimension $d$, so the higher direct images above $d$ are torsion, hence zero.

Kollár vanishing is proved by induction on $\dim Z$. After passing to a log resolution, a general member $D$ of a very ample multiple of $A$ pulls back to a smooth divisor $X_D$, and torsion freeness turns the restriction sequence into short exact sequences $0 \to R^j f_* \mathcal{O}_X(N) \to R^j f_* \mathcal{O}_X(N) (D) \to R^j f_{D*} \mathcal{O}_{X_D}(N_D) \to 0$, to whose last term the induction applies. This gives the vanishing of $H^i$ for $i \geq 2$ after a large twist. The remaining group $H^1$ is the only obstruction to the degeneration of the Leray spectral sequence, and injectivity again kills it.

### Examples

**Example 5.2.12 (a product with an elliptic curve).** Let $E$ be an elliptic curve, $X = E \times \mathbb{P}^1$ and $f = p_2 \colon X \to Z = \mathbb{P}^1$, so $d = 1$ and $\omega_X = p_2^* \mathcal{O}(-2)$. By cohomology and base change for the product, $f_* \omega_X = \mathcal{O}(-2)$ and $R^1 f_* \omega_X = H^1(E, \mathcal{O}_E) \otimes \mathcal{O}(-2) \cong \mathcal{O}(-2)$, both locally free, and $R^j f_* \omega_X = 0$ for $j \geq 2$. For an ample $\mathcal{O}(a)$, $a \geq 1$, Theorem P4.2.1 gives $H^1(\mathbb{P}^1, \mathcal{O}(a - 2)) = 0$, as Corollary 5.2.11 predicts. For $a = 0$ the group $H^1(\mathbb{P}^1, \mathcal{O}(-2)) \cong k$ is nonzero, so the ampleness of $A$ in Theorem 5.2.10 is needed.

**Example 5.2.13 (the hypothesis on $N$ is needed).** Let $\mu \colon X \to \mathbb{P}^2$ be the blow-up of a point $p$, with exceptional curve $E$, and $N = 2E$. By Example P4.4.19, $R^1 \mu_* \mathcal{O}_X(2E) \cong k(p)$, a nonzero torsion sheaf. This does not contradict Theorem 5.2.8: since $K_X = \mu^* K_{\mathbb{P}^2} + E$, the class $N - K_X = E - \mu^* K_{\mathbb{P}^2}$ has degree $-1$ on $E$, while every pullback from $\mathbb{P}^2$ has degree $0$ on $E$, so $(N - K_X) \cdot E = -1$. If $N - (K_X + \Delta)$ were $\mathbb{Q}$-linearly equivalent to a pullback, then $\Delta \cdot E = -1$; writing $\Delta = aE + \Delta'$ with $E \not\subseteq \operatorname{Supp} \Delta'$ gives $-a + \Delta' \cdot E = -1$, so $a \geq 1$ and $(X, \Delta)$ is not klt. For $N = K_X + E$ the class $N - K_X = E$ is not a pullback either, and indeed $R^1 \mu_* \mathcal{O}_X(K_X + E) = R^1 \mu_* \mathcal{O}_X(\mu^* K_{\mathbb{P}^2} + 2E) \cong k(p)$ by the projection formula.

### Proof

*Theorem 5.2.8.* Fix $j$ and let $\mathcal{T} \subseteq R^j f_* \mathcal{O}_X(N)$ be the torsion subsheaf. The sheaf $R^j f_* \mathcal{O}_X(N)$ is coherent by Theorem P4.4.8, so $\mathcal{T}$ is coherent. Suppose $\mathcal{T} \neq 0$. Its support is a proper closed subset $W \subsetneq Z$, and $\mathcal{I}_W^r \mathcal{T} = 0$ for some $r \geq 1$. Let $H$ be a very ample divisor on $Z$. By Theorem P4.2.7 choose $\ell \geq 1$ such that $A_\ell = A + \ell H$ is ample, $\mathcal{T}(\ell H)$ is generated by global sections, and $H^p(Z, R^q f_* \mathcal{O}_X(N) \otimes \mathcal{O}_Z(\ell H)) = 0$ for $p > 0$ and all $q$. Put
$$N' = N + f^* (\ell H), \qquad M = f^* A_\ell.$$
Then $N'$ is a $\mathbb{Q}$-Cartier Weil divisor, $N' - (K_X + \Delta) \sim_\mathbb{Q} M$, and $M$ is semiample because $A_\ell$ is ample. By the projection formula, Proposition P4.4.10, $R^q f_* \mathcal{O}_X(N') = R^q f_* \mathcal{O}_X(N) \otimes \mathcal{O}_Z(\ell H)$.

Let $c \geq 1$ be an integer with $c A_\ell$ Cartier. Choose $k \geq 1$ such that $H^p(Z, R^q f_* \mathcal{O}_X(N') \otimes \mathcal{O}_Z(k c A_\ell)) = 0$ for $p > 0$ and all $q$, and such that $\mathcal{I}_W^r \otimes \mathcal{O}_Z(k c A_\ell)$ has a nonzero global section $s$; both hold for $k$ large by Theorem P4.2.7. Since $Z$ is integral and $f$ is surjective, $B = f^* \operatorname{div}(s)$ is an effective Cartier divisor on $X$, and $B \sim k c\, M$. Theorem 5.2.3 applied to $N'$, $M$ and $B$ with $t = kc$ says that multiplication by $f^* s$,
$$H^j(X, \mathcal{O}_X(N')) \to H^j(X, \mathcal{O}_X(N' + B)),$$
is injective. By the choice of $\ell$ and $k$, the Leray spectral sequences of $\mathcal{O}_X(N')$ and $\mathcal{O}_X(N' + B)$, Theorem P2.4.26, have $E_2^{p,q} = 0$ for $p > 0$, so the edge maps are isomorphisms $H^j(X, \mathcal{O}_X(N')) \cong H^0(Z, R^j f_* \mathcal{O}_X(N'))$ and $H^j(X, \mathcal{O}_X(N' + B)) \cong H^0(Z, R^j f_* \mathcal{O}_X(N') \otimes \mathcal{O}_Z(kcA_\ell))$. The edge maps are natural in the sheaf, and by the projection formula $R^j f_*$ of multiplication by $f^* s$ is multiplication by $s$. So multiplication by $s$,
$$H^0(Z, R^j f_* \mathcal{O}_X(N')) \to H^0(Z, R^j f_* \mathcal{O}_X(N') \otimes \mathcal{O}_Z(kcA_\ell)),$$
is injective. Let $\sigma$ be a nonzero global section of $\mathcal{T}(\ell H) \subseteq R^j f_* \mathcal{O}_X(N')$, which exists because $\mathcal{T}(\ell H)$ is nonzero and generated by global sections. Then $s \sigma$ is a section of $\mathcal{I}_W^r \mathcal{T}(\ell H) \otimes \mathcal{O}_Z(kcA_\ell) = 0$, a contradiction. So $\mathcal{T} = 0$.

*Theorem 5.2.9.* The morphism $f$ is projective, since $X$ is projective. There is a dense open subset $U \subseteq Z$ over which every fibre of $f$ has dimension $d$ (Har77, Exercise II.3.22). By Har77, Corollary III.11.2, $R^j f_* \mathcal{F}|_U = 0$ for every coherent $\mathcal{F}$ and $j > d$. So for $j > d$ the sheaf $R^j f_* \mathcal{O}_X(N)$ is supported on $Z \setminus U$, it is torsion, and it is zero by Theorem 5.2.8. This is the argument of Proposition P7.9.16.

*Theorem 5.2.10.* Step 1: reduction to a smooth $X$. Let $\mu \colon Y \to X$ be a projective log resolution of $(X, \Delta + \lambda N)$ as in Corollary 5.1.16, with $N_Y$ and $\Theta$ as there. By part 3 of that corollary and the Leray spectral sequence for $f \circ \mu$, Theorem P2.4.26, $R^j (f \circ \mu)_* \mathcal{O}_Y(N_Y) = R^j f_* \mathcal{O}_X(N)$. By parts 1 and 2, $(Y, \Theta)$ is klt with snc support and $N_Y - (K_Y + \Theta) \sim_\mathbb{Q} (f \circ \mu)^* A$. So it suffices to prove the theorem when $X$ is smooth, $\Delta$ has snc support and coefficients in $[0, 1)$ and $N$ is Cartier. The proof below uses the hypotheses on $X$ only through Theorems 5.2.2 and 5.2.8, so it applies verbatim when $X$ is a disjoint union of smooth projective varieties each mapping onto $Z$, and the statement is proved in that generality by induction on $\dim Z$. For $\dim Z = 0$ there is nothing to prove.

Step 2: a general divisor. Let $\dim Z \geq 1$. Choose $m \geq 1$ such that $mA$ is a very ample Cartier divisor and $D \in |mA|$ general. Write $\mathcal{R}^j = R^j f_* \mathcal{O}_X(N)$ and $X_D = f^* D$. By Lemma P7.8.8, applied to the free linear system $f^* |mA|$, $X_D$ is smooth, it has no component in common with $\Delta$, and $\operatorname{Supp} \Delta + X_D$ is snc. Every component of $X_D$ maps onto a component of $D$. Indeed, for each $e$ let $Z_e \subseteq Z$ be the closed set of points whose fibre has dimension at least $e$; since $D$ is general it contains no component of any $Z_e$. If a component $C$ of $X_D$, of dimension $\dim X - 1$, mapped onto $V \subsetneq D'$ for a component $D'$ of $D$, with general fibre dimension $e$, then $V$ lies in $Z'' \cap D$ for a component $Z''$ of $Z_e$, so $\dim Z'' \geq \dim V + 1$ and $\dim f^{-1}(Z'') \geq \dim V + 1 + e = \dim C + 1$. So $f^{-1}(Z'')$ contains the component of $X$ containing $C$, which maps onto $Z$, hence $Z'' = Z$ and $e \leq d$. But $\dim V \leq \dim D' - 1 = \dim Z - 2$ gives $e = \dim C - \dim V \geq d + 1$, a contradiction. By adjunction $K_{X_D} = (K_X + X_D)|_{X_D}$, so $N_D = (N + X_D)|_{X_D}$ and $\Delta_D = \Delta|_{X_D}$ satisfy
$$N_D - (K_{X_D} + \Delta_D) \sim_\mathbb{Q} (f^* A)|_{X_D} = f_D^* (A|_D),$$
with $f_D \colon X_D \to D$ the restriction, $(X_D, \Delta_D)$ klt with snc support, and $A|_D$ ample. The sequence $0 \to \mathcal{O}_X(N) \to \mathcal{O}_X(N + X_D) \to \mathcal{O}_{X_D}(N_D) \to 0$ and the projection formula give a long exact sequence
$$\cdots \to \mathcal{R}^j \xrightarrow{\ s_D\ } \mathcal{R}^j \otimes \mathcal{O}_Z(D) \to R^j f_{D*} \mathcal{O}_{X_D}(N_D) \to \mathcal{R}^{j+1} \xrightarrow{\ s_D\ } \cdots.$$
Multiplication by $s_D \neq 0$ is injective on the torsion free sheaves $\mathcal{R}^j$ (Theorem 5.2.8), so the sequence splits into short exact sequences
$$0 \to \mathcal{R}^j \to \mathcal{R}^j \otimes \mathcal{O}_Z(D) \to R^j f_{D*} \mathcal{O}_{X_D}(N_D) \to 0.$$

Step 3: $i \geq 2$. By induction, applied to each component of $X_D$ over the component of $D$ it maps onto, $H^i(D, R^j f_{D*} \mathcal{O}_{X_D}(N_D)) = 0$ for $i > 0$. For $i \geq 2$ the cohomology sequence then gives an injection $H^i(Z, \mathcal{R}^j) \to H^i(Z, \mathcal{R}^j \otimes \mathcal{O}_Z(D))$. The divisor $N + X_D$ satisfies the hypotheses with $A$ replaced by the ample class $(1 + m) A$, and its higher direct images are $\mathcal{R}^j \otimes \mathcal{O}_Z(mA)$. Repeating the argument with a new general member of $|mA|$ gives injections $H^i(Z, \mathcal{R}^j) \to H^i(Z, \mathcal{R}^j \otimes \mathcal{O}_Z(lmA))$ for every $l \geq 1$, and the target is zero for $l$ large by Theorem P4.2.7. So $H^i(Z, \mathcal{R}^j) = 0$ for $i \geq 2$ and all $j$.

Step 4: $i = 1$. Choose $l \geq 1$ with $H^p(Z, \mathcal{R}^q \otimes \mathcal{O}_Z(lmA)) = 0$ for $p > 0$ and all $q$, and a general $B \in f^* |lmA|$, so $B \sim lm\, f^* A$ and $\operatorname{Supp}(\Delta + B)$ is snc by Lemma P7.8.8. The divisor $f^* A$ is semiample, and Theorem 5.2.2 with $M = f^* A$ and $t = lm$ shows that $H^n(X, \mathcal{O}_X(N)) \to H^n(X, \mathcal{O}_X(N + B))$ is injective for every $n$. Consider the Leray spectral sequences $E_2^{p,q} = H^p(Z, \mathcal{R}^q)$ and $'E_2^{p,q} = H^p(Z, \mathcal{R}^q \otimes \mathcal{O}_Z(lmA))$, and the map between them induced by $s_B$. By Step 3, $E_2^{p,q} = 0$ unless $p \in \{0, 1\}$, so all differentials $d_r$ with $r \geq 2$ vanish and $E_2 = E_\infty$. The abutment $H^n(X, \mathcal{O}_X(N))$ has a two-step filtration with subobject $E_\infty^{1, n-1} = H^1(Z, \mathcal{R}^{n-1})$ and quotient $E_\infty^{0, n} = H^0(Z, \mathcal{R}^n)$. The map of spectral sequences sends the subobject to $'E_\infty^{1, n-1} = 0$, so $H^1(Z, \mathcal{R}^{n-1})$ lies in the kernel of the injective map $H^n(X, \mathcal{O}_X(N)) \to H^n(X, \mathcal{O}_X(N + B))$. So $H^1(Z, \mathcal{R}^{n-1}) = 0$ for every $n \geq 1$.

*Corollary 5.2.11.* Apply Theorems 5.2.8 and 5.2.9 with $\Delta = 0$, $N = K_X$ and $A = 0$. For Kollár vanishing apply Theorem 5.2.10 to $N = K_X + f^* A$, which satisfies $N - K_X = f^* A$, and use the projection formula, Proposition P4.4.10: $R^j f_* \mathcal{O}_X(K_X + f^* A) = R^j f_* \mathcal{O}_X(K_X) \otimes \mathcal{O}_Z(A)$. For $X$ smooth, $\mathcal{O}_X(K_X) = \omega_X$.

### Exercises

1. (A) In Example 5.2.12, compute $H^i(Z, f_* \omega_X \otimes \mathcal{O}(a))$ and $H^i(Z, R^1 f_* \omega_X \otimes \mathcal{O}(a))$ for all $a$, and check the decomposition $h^1(X, \omega_X \otimes f^* \mathcal{O}(a)) = h^1(Z, f_* \omega_X(a)) + h^0(Z, R^1 f_* \omega_X(a))$ for $a \geq 1$.
2. (A) Let $f \colon X \to Z$ be a finite surjective morphism with $X$ klt and $Z$ normal projective. Show that $f_* \mathcal{O}_X(K_X)$ is torsion free, and that Theorem 5.2.10 for $f$ follows from Kawamata-Viehweg vanishing on $X$ and Theorem P4.4.8 together with the vanishing of $R^j f_*$ for $j > 0$.
3. (B) Show that the torsion freeness in Theorem 5.2.8 fails for $\mathcal{O}_X$ in place of $\mathcal{O}_X(K_X)$ on the compactified cone of Example P7.9.19, and explain which hypothesis of Theorem 5.2.8 fails for $N = 0$.
4. (B) Let $f \colon X \to Z$ be birational, with $(X, \Delta)$ klt and $X$, $Z$ projective. Show that Theorem 5.2.9 gives $R^j f_* \mathcal{O}_X(N) = 0$ for $j > 0$ whenever $N - (K_X + \Delta) \sim_\mathbb{Q} f^* A$, and compare with Corollary 5.1.15.
5. (B) Let $f \colon X \to C$ be a surjective morphism from a smooth projective surface onto a smooth projective curve, with general fibre $F$. Show that $f_* \omega_X$ and $R^1 f_* \omega_X$ are locally free of ranks $g(F)$ and $1$, and that $h^1(X, \omega_X \otimes f^* \mathcal{O}_C(A)) = h^0(C, R^1 f_* \omega_X \otimes \mathcal{O}_C(A))$ and $h^2(X, \omega_X \otimes f^* \mathcal{O}_C(A)) = 0$ for every ample divisor $A$ on $C$.
6. (C) Let $X$ be the blow-up of $\mathbb{P}^2$ at a point $p$, with exceptional curve $E$, and $f \colon X \to \mathbb{P}^1$ the projection from $p$, with fibre $F$. Show that $K_X \sim -2E - 3F$ and that $N = aE + bF$ satisfies the hypothesis of Theorem 5.2.10 with $\Delta = 0$ if and only if $a = -2$ and $b \geq -2$. Show that $f_* \mathcal{O}_X(-2E + bF) = 0$ and $R^1 f_* \mathcal{O}_X(-2E + bF) \cong \mathcal{O}_{\mathbb{P}^1}(b + 1)$, using $\omega_{X/\mathbb{P}^1} = \mathcal{O}_X(-2E - F)$ and $R^1 f_* \omega_{X/\mathbb{P}^1} \cong \mathcal{O}_{\mathbb{P}^1}$, and check that the vanishing of $H^1$ holds exactly for $b \geq -2$.

### Lean

`MinimalModel.KollarTorsionFreeness` is the statement of Theorem 5.2.8 for $X$ smooth, $\Delta$ an snc divisor with $\lfloor \Delta \rfloor = 0$ and $N - (K_X + \Delta) \sim_\mathbb{Q} 0$, after Fujino, Theorem 3.4 (i) (Fuj11); `MinimalModel.KollarTorsionFree` is its conjunction with `MinimalModel.KollarInjectivity`. Both are stated without proof. Theorems 5.2.9 and 5.2.10 are not in the library.

### Notes and history

Kollár proved the three statements for $\omega_X$ on a smooth projective variety in Kol86a, Theorem 2.1, from the injectivity theorem, and extended them in Kol86b to the decomposition of $Rf_* \omega_X$. The versions for klt pairs and $\mathbb{Q}$-divisors are in Kol92 and in Fujino's treatment (Fuj11, Section 3), which also covers log canonical pairs with conditions on the lc centres. The induction on $\dim Z$ in Step 3 and the degeneration argument in Step 4 are Kollár's. Lazarsfeld, Section 4.3 (Laz04), gives the case $\Delta = 0$ with the same structure. Volume P7 states the three statements for $\omega_X$ as Theorem P7.9.13 and derives only part 2 from part 1; this section derives all three from Theorem 5.2.1.
