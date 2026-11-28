---
title: Semiampleness and the contraction of a nef divisor
nodes: []
sources: [KM98, Kaw85, KMM87, Laz04]
reads_with: [KM98:3.3, Laz04:2.1]
requires: [1.5, 7.1, P4.6, P7.1, P7.2, P7.3, P7.6]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Semiampleness and the contraction of a nef divisor

### Statement

The ground field $k$ is algebraically closed of characteristic $0$. A Cartier divisor $D$ is *semiample* if $|bD|$ is free for some $b \ge 1$ (Proposition P7.6.21). For a contraction $\varphi \colon X \to Z$ in the sense of Definition 1.5.1, a curve $C \subseteq X$ is *contracted* if $\varphi(C)$ is a point.

**Corollary 7.2.4 (the contraction defined by $D$).** In the situation of Theorem 7.2.1, there are a contraction $\varphi \colon X \to Z$ onto a normal projective variety and an ample Cartier divisor $A_Z$ on $Z$ with $\mathcal{O}_X(D) \cong \varphi^* \mathcal{O}_Z(A_Z)$. A curve $C \subseteq X$ is contracted by $\varphi$ if and only if $D \cdot C = 0$, and $\varphi$ is determined up to isomorphism by this property. For every $b \gg 0$, $\varphi$ is the Stein factorization of the morphism defined by $|bD|$.

Lean: not yet in Lean.

**Corollary 7.2.5 (a nef and big log canonical divisor is semiample).** Let $(X, \Delta)$ be a projective klt pair with $K_X + \Delta$ nef and big. Then $K_X + \Delta$ is semiample: $|b r (K_X + \Delta)|$ is free for $b \gg 0$, where $r(K_X + \Delta)$ is Cartier.

Lean: `MinimalModel.AbundanceBig`, in the project library, states this for klt pairs with real coefficients, which is due to BCHM, as a statement without proof.

**Corollary 7.2.6 (log Fano pairs).** Let $(X, \Delta)$ be a projective klt pair with $-(K_X + \Delta)$ nef and big.

1. Every nef Cartier divisor on $X$ is semiample.
2. A Cartier divisor $D$ with $D \equiv 0$ satisfies $D \sim 0$. So two Cartier divisors are linearly equivalent if and only if they are numerically equivalent, and $\operatorname{Pic}(X)$ embeds in $N^1(X)$.

Lean: not yet in Lean.

### Proof in words

For Corollary 7.2.4, the systems $|bD|$ and $|(b+1)D|$ are free, and their Stein factorizations contract the same curves, those with $D \cdot C = 0$. A contraction is determined by its contracted curves, by rigidity, so the two Stein factorizations are one contraction $\varphi$ with $bD$ and $(b+1)D$ pullbacks of ample divisors; then $D$ is the pullback of their difference. Corollary 7.2.5 is Theorem 7.2.1 for $D = r(K_X + \Delta)$ with $a = 2$. For Corollary 7.2.6, the hypothesis of Theorem 7.2.1 holds for every nef $D$ with every $a > 0$, and a free numerically trivial system defines a constant morphism.

### Examples

**Example 7.2.7 (three collinear points).** Let $X$ be the blow-up of $\mathbb{P}^2$ at three distinct points $x_1, x_2, x_3$ on a line $\ell$, with exceptional curves $E_i$, $h$ the pullback of a line, and $\ell' \sim h - E_1 - E_2 - E_3$ the strict transform of $\ell$. Then $\ell'^2 = -2$ and $-K_X = 3h - \sum_i E_i = \ell' + 2h$. For a curve $C \neq \ell'$, $-K_X \cdot C = \ell' \cdot C + 2h \cdot C \ge 0$, and $-K_X \cdot \ell' = 3 - 3 = 0$, so $-K_X$ is nef; $(K_X^2) = 9 - 3 = 6 > 0$, so it is big by Theorem P7.7.7. Theorem 7.2.1 applies to $D = -K_X$ with $\Delta = 0$ and $a = 1$, and Corollary 7.2.4 gives a contraction $\varphi \colon X \to Z$ contracting exactly the curves with $K_X \cdot C = 0$. If $K_X \cdot C = 0$, then $\ell' \cdot C = -2 h \cdot C \le 0$, so either $C = \ell'$ or $h \cdot C = 0$; in the second case $C$ is some $E_i$, and $\ell' \cdot E_i = 1 \neq 0$. So $\varphi$ contracts only $\ell'$, $Z$ is a normal surface with one singular point, and $-K_X = \varphi^* A_Z$ with $A_Z$ ample, so $Z$ is a singular del Pezzo surface of degree $6$. The singular point is the $A_1$ point, the cone over a conic: a contracted smooth rational curve of self-intersection $-2$ gives a rational double point of type $A_1$. The surface $X$ is not Fano, but its anticanonical model $Z$ is, and Example 7.2.2 shows that the smooth del Pezzo surface of degree $8$ has two contractions instead of one.

**Example 7.2.8 (a torsion class).** Corollary 7.2.6 fails without the hypothesis on $-(K_X + \Delta)$. On an Enriques surface $X$, $K_X \not\sim 0$ but $2K_X \sim 0$, so $K_X \equiv 0$ is not linearly trivial, and $-K_X$ is numerically trivial, not big.

### Proof

*Corollary 7.2.4.* By Theorem 7.2.1 there is $b_0$ with $|bD|$ free for every $b \ge b_0$. For such $b$ let $\phi_b \colon X \to \mathbb{P}^{N_b}$ be the morphism defined by $|bD|$, so $\mathcal{O}_X(bD) \cong \phi_b^* \mathcal{O}(1)$, and let $\phi_b = g_b \circ \varphi_b$ be its Stein factorization (Theorem 1.5.3), with $\varphi_b \colon X \to Z_b$ a contraction onto a normal variety and $g_b$ finite. Then $Z_b$ is projective, as it is finite over a closed subvariety of $\mathbb{P}^{N_b}$, and $A_b = g_b^* \mathcal{O}(1)$ is ample on $Z_b$ by part 5 of Proposition P7.3.9, with $\mathcal{O}_X(bD) \cong \varphi_b^* A_b$.

Let $C \subseteq X$ be a curve. If $\varphi_b(C)$ is a point, then $bD \cdot C = 0$. If $\varphi_b(C)$ is a curve $C_b$, then by the projection formula (Theorem P7.1.15) $bD \cdot C = \deg(C \to C_b) \, (A_b \cdot C_b) > 0$. So $\varphi_b$ contracts exactly the curves with $D \cdot C = 0$, for every $b \ge b_0$.

Let $b, b' \ge b_0$ and $y \in Z_b$. The fibre $X_y$ of $\varphi_b$ is connected, since $\varphi_b$ is a contraction. Its image $\varphi_{b'}(X_y)$ is connected and closed. If it had positive dimension, it would contain a curve $\Gamma$, and Lemma P7.2.6, applied to the surjection $X_y \cap \varphi_{b'}^{-1}(\Gamma) \to \Gamma$, would give a curve $C \subseteq X_y$ with $\varphi_{b'}(C) = \Gamma$. But $C$ is contracted by $\varphi_b$, so $D \cdot C = 0$, so $C$ is contracted by $\varphi_{b'}$, which is absurd. So $\varphi_{b'}(X_y)$ is a point, and by Lemma 1.5.4 there is $h \colon Z_b \to Z_{b'}$ with $\varphi_{b'} = h \circ \varphi_b$. In the same way $\varphi_b = h' \circ \varphi_{b'}$, and the uniqueness in Lemma 1.5.4 gives $h' h = \mathrm{id}$ and $h h' = \mathrm{id}$. So all the $\varphi_b$ are one contraction $\varphi \colon X \to Z$ up to isomorphism, and $\mathcal{O}_X(bD) \cong \varphi^* A_b$ for every $b \ge b_0$.

For a contraction, $\varphi_* \mathcal{O}_X = \mathcal{O}_Z$, so the projection formula gives $\varphi_* \varphi^* \mathcal{L} \cong \mathcal{L}$ for every line bundle $\mathcal{L}$ on $Z$, and $\varphi^* \colon \operatorname{Pic}(Z) \to \operatorname{Pic}(X)$ is injective. Let $A_Z$ be a Cartier divisor with $\mathcal{O}_Z(A_Z) \cong A_{b_0 + 1} \otimes A_{b_0}^{-1}$. Then $\varphi^* \mathcal{O}_Z(A_Z) \cong \mathcal{O}_X(D)$, and $\varphi^* \mathcal{O}_Z(b_0 A_Z) \cong \mathcal{O}_X(b_0 D) \cong \varphi^* A_{b_0}$, so $\mathcal{O}_Z(b_0 A_Z) \cong A_{b_0}$ is ample, and $A_Z$ is ample. Finally, a contraction $\psi \colon X \to Z'$ contracting exactly the curves with $D \cdot C = 0$ is isomorphic to $\varphi$ by the argument of the previous paragraph with $\psi$ in place of $\varphi_{b'}$.

*Corollary 7.2.5.* Let $r \ge 1$ with $D = r(K_X + \Delta)$ Cartier. Then $D$ is nef, and $2D - (K_X + \Delta) = (2r - 1)(K_X + \Delta)$ is nef and big. Theorem 7.2.1 with $a = 2$ gives the claim.

*Corollary 7.2.6.* Let $D$ be nef and Cartier. For every $a > 0$, $aD - (K_X + \Delta)$ is nef and big by Lemma P7.9.2, so Theorem 7.2.1 applies and $D$ is semiample, which is part 1. For part 2, $D$ and $-D$ are nef, and by Theorem 7.2.1 there is $b_0$ with $|bD|$ free for every $b \ge b_0$. Let $\phi_b$ be the morphism defined by $|bD|$. If $\phi_b(X)$ had positive dimension, it would contain a curve $\Gamma$, and Lemma P7.2.6 would give a curve $C$ with $\phi_b(C) = \Gamma$, so $bD \cdot C > 0$ by the projection formula, contradicting $D \equiv 0$. So $\phi_b$ is constant, and $\mathcal{O}_X(bD) \cong \phi_b^* \mathcal{O}(1)$ is trivial. Then $bD \sim 0$ and $(b + 1) D \sim 0$, so $D \sim 0$. The rest of part 2 follows by applying this to the difference of two numerically equivalent Cartier divisors.

### Exercises

1. (A) In Example 7.2.7, show that $|-K_X|$ itself is free and that it defines a morphism $X \to \mathbb{P}^6$ whose image is $Z$, embedded as a surface of degree $6$.
2. (A) Let $X = \mathbb{P}^1 \times \mathbb{P}^1$ and $D$ of bidegree $(1, 0)$. Find $\varphi$ and $A_Z$ of Corollary 7.2.4, and check the description of contracted curves.
3. (A) Show that in Example 7.2.7 the classes $E_1, E_2, E_3, \ell'$ are the only curves of negative self-intersection, and list the extremal rays of $\overline{NE}(X)$.
4. (B) Let $(X, \Delta)$ be klt and $D$ as in Theorem 7.2.1 with $D$ big. Show that the contraction $\varphi$ of Corollary 7.2.4 is birational and that $\varphi$ is an isomorphism exactly when $D$ is ample.
5. (B) Show that the conclusion of Corollary 7.2.4 that $D$ itself, and not only $bD$, is a pullback can fail for a semiample divisor that does not satisfy the hypothesis of Theorem 7.2.1: on an Enriques surface with an elliptic fibration, find a nef divisor $D$ such that $2D$ is a pullback from $\mathbb{P}^1$ but $D$ is not.
6. (C) Let $X$ be a smooth projective threefold with $-K_X$ nef and big, and $C \subseteq X$ a curve with $K_X \cdot C = 0$. Show that $C$ is contracted by the anticanonical model $X \to Z$ of Corollary 7.2.4, and that the exceptional locus of $X \to Z$ is the union of all such curves.

### Lean

The library has `MinimalModel.IsSemiample` and `MinimalModel.IsContraction` and the statement `MinimalModel.AbundanceBig`. Corollary 7.2.4 and Corollary 7.2.6 are not yet in Lean.

### Notes and history

Corollary 7.2.4 is the form of the base point free theorem used to construct contractions, KM98, Theorem 3.3 and the discussion after it. Corollary 7.2.5 is the reason the canonical model of a variety of general type with a minimal model is a projective variety with canonical singularities, Kawamata's application in Kaw85. Corollary 7.2.6, part 2, says that the Picard group of a log Fano pair is torsion free and injects into $N^1(X)$; the proof uses the base point free theorem for $D$ and $-D$ at once. Lazarsfeld (Laz04), Section 2.1, gives the general theory of semiample divisors and their Iitaka fibrations.
