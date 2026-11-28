---
title: Relative Kawamata-Viehweg vanishing
nodes: []
sources: [KM98, Laz04, EV92, Har77]
reads_with: [KM98:2.4, Laz04:4.3, EV92:5]
requires: [P2.4, P4.2, P4.4, P7.1, P7.3, P7.8, 1.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Relative Kawamata-Viehweg vanishing

### Statement

Throughout, $k$ has characteristic $0$, and $f \colon X \to Z$ is a morphism of projective varieties. The language of $\mathbb{Q}$-divisors is that of Definition P7.8.1.

**Definition P7.9.1 (relative positivity).** Let $D$ be a $\mathbb{Q}$-Cartier $\mathbb{Q}$-divisor on $X$.

1. $D$ is *$f$-nef* if $D \cdot C \geq 0$ for every curve $C \subseteq X$ with $f(C)$ a point.
2. $D$ is *$f$-ample* if $D + f^* (m H)$ is ample for some ample divisor $H$ on $Z$ and some $m \geq 0$.
3. $D$ is *$f$-big* if its restriction to the generic fibre of $f$ is big.

If $D$ is $f$-ample, then $D + f^*(m' H')$ is ample for every ample $H'$ and $m' \gg 0$, by part 3 of Theorem P7.3.12, since $f^* H'$ is nef. A nef divisor is $f$-nef, and an $f$-ample divisor is $f$-nef and $f$-big. When $f$ is birational every divisor is $f$-big, and when $Z$ is a point the three notions are nef, ample and big.

**Lemma P7.9.2 (nef and big plus nef).** Let $X$ be a normal projective variety, $B$ a nef and big $\mathbb{Q}$-Cartier divisor and $P$ a nef $\mathbb{Q}$-Cartier divisor. Then $B + P$ is nef and big. In particular, for a generically finite surjective morphism $f \colon X \to Z$ and an ample $H$ on $Z$, $f^* H$ is nef and big.

Lean: not in Lean as stated.

**Theorem P7.9.3 (relative Kawamata-Viehweg vanishing).** Let $X$ be smooth, $N$ a Cartier divisor on $X$ and $\Delta = \sum_j a_j D_j$ a $\mathbb{Q}$-divisor with snc support and $0 \leq a_j < 1$. Suppose that $N - \Delta + f^* H$ is nef and big for some ample $\mathbb{Q}$-divisor $H$ on $Z$. Then
$$R^j f_* \mathcal{O}_X(K_X + N) = 0 \quad \text{for } j > 0,$$
and $H^i(Z, f_* \mathcal{O}_X(K_X + N) \otimes \mathcal{O}_Z(A)) = 0$ for $i > 0$ and every ample Cartier divisor $A$ on $Z$ with $A - H$ nef.

Lean: not in Lean as stated.

**Corollary P7.9.4 (the $f$-ample case).** Let $X$, $N$ and $\Delta$ be as in Theorem P7.9.3, and suppose that $N - \Delta$ is $f$-ample. Then $R^j f_* \mathcal{O}_X(K_X + N) = 0$ for $j > 0$.

Lean: not in Lean as stated.

**Theorem P7.9.5 (the relative klt form, black box).** Let $f \colon X \to Z$ be a proper morphism of varieties, $(X, \Delta)$ a klt pair and $N$ a Weil divisor on $X$ that is $\mathbb{Q}$-Cartier, such that $N - (K_X + \Delta)$ is $f$-nef and $f$-big. Then $R^j f_* \mathcal{O}_X(N) = 0$ for $j > 0$.

Lean: `MinimalModel.KawamataViehweg` is this statement, after Kollár and Mori, Theorem 2.70, without proof.

### Proof in words

Relative vanishing is absolute vanishing after twisting by the pullback of a sufficiently ample divisor from the base. If $N - \Delta$ becomes nef and big after adding $f^* H$, then it stays nef and big after adding $f^*(mA)$ for every ample $A$ with $mA - H$ nef, because adding a nef class to a nef and big class keeps it big, by Kodaira's lemma. The absolute theorem then kills $H^i(X, \mathcal{O}(K_X + N) \otimes f^* A^m)$ for all large $m$, and the comparison of Lemma P7.8.16 through the Leray spectral sequence turns this into the vanishing of $R^j f_*$. The same spectral sequence gives a vanishing theorem on the base for the direct image $f_* \mathcal{O}(K_X + N)$, which is a first form of Kollár's vanishing theorem of Section 9.3.

The form used in the minimal model program allows a klt pair in place of a smooth variety with an snc boundary, a proper morphism in place of a projective one, and the relative conditions $f$-nef and $f$-big in place of the global condition. Kollár and Mori deduce it from the absolute theorem by the same steps as in Theorem P7.8.18: a log resolution turns the klt pair into an snc pair whose round-down is absorbed by the relative canonical divisor, Chow's lemma reduces to projective morphisms, and a relative form of Kodaira's lemma handles $f$-big divisors. Here it is a black box.

### Examples

**Example P7.9.6 (the blow-up of a point).** Let $\mu \colon X \to \mathbb{P}^2$ be the blow-up of a point, with exceptional curve $E$, so that $K_X = \mu^* K_{\mathbb{P}^2} + E$. Write $H$ also for the pullback of a line. The divisor $-E$ is $\mu$-ample, since $-E + 2\mu^* H = 2H - E$ is ample by Example P7.3.16. For $b \geq 1$, $-bE$ is $\mu$-ample, and Corollary P7.9.4 with $N = -bE$ and $\Delta = 0$ gives $R^1 \mu_* \mathcal{O}_X(K_X - bE) = 0$, that is, $R^1 \mu_* \mathcal{O}_X((1 - b)E) = 0$ by the projection formula, which agrees with part 1 of Proposition P4.4.16. For $N = bE$ with $b \geq 1$ the divisor $N$ is not $\mu$-nef, since $bE \cdot E = -b$, and $R^1 \mu_* \mathcal{O}_X(K_X + bE) = R^1 \mu_* \mathcal{O}_X((b+1)E) \otimes \mathcal{O}(K_{\mathbb{P}^2})$ has length $b(b+1)/2 > 0$ by part 2 of Proposition P4.4.16. So the relative positivity cannot be dropped.

**Example P7.9.7 (a product).** Let $f \colon X = \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1$ be the first projection, $\omega_X = \mathcal{O}(-2, -2)$, and $N = \mathcal{O}(0, b)$, of degree $b$ on the fibres. For $b \geq 1$, $N$ is $f$-ample, and $R^1 f_* \mathcal{O}(K_X + N) = R^1 f_* \mathcal{O}(-2, b - 2) = \mathcal{O}(-2) \otimes H^1(\mathbb{P}^1, \mathcal{O}(b - 2)) = 0$, by flat base change or Example P4.4.17. For $b = 0$, $N$ is $f$-nef and not $f$-big, and $R^1 f_* \omega_X = \mathcal{O}(-2) \otimes H^1(\mathbb{P}^1, \mathcal{O}(-2)) = \omega_{\mathbb{P}^1}$, which is not zero. This is the top direct image of Example P7.9.18.

### Proof

*Lemma P7.9.2.* $B + P$ is nef by part 2 of Proposition P7.3.9. Choose $m \geq 1$ with $mB$ and $mP$ Cartier. By Lemma 1.3.12 there are $m' \geq 1$, a very ample $A_0$ and an effective divisor $E_0 \sim m' m B - A_0$. Then $m'm(B + P) \sim A_0 + m' m P + E_0$, and $A' = A_0 + m'm P$ is ample by part 3 of Theorem P7.3.12. Multiplication by the $l$-th power of a section defining $E_0$ embeds $H^0(X, \mathcal{O}(lA'))$ into $H^0(X, \mathcal{O}(l m' m (B + P)))$, and $h^0(X, \mathcal{O}(lA')) = \chi(\mathcal{O}(lA')) = \frac{(A'^n)}{n!} l^n + O(l^{n-1})$ for $l \gg 0$ by Theorem P4.2.7 and Theorem P7.1.17, with $(A'^n) > 0$ by part 5 of Theorem P7.3.12. So $B + P$ is big. For the second statement, $f^* H$ is nef by part 3 of Proposition P7.3.9, and $(f^* H)^n = \deg(f) (H^n) > 0$ by the projection formula, Theorem P7.1.15, so the nef divisor $f^* H$ is big (Definition P7.8.1).

*Theorem P7.9.3.* Let $A$ be an ample Cartier divisor on $Z$ with $A - H$ nef; one exists, since a large multiple of an ample Cartier divisor minus $H$ is ample. For every $m \geq 1$, the divisor $mA - H = (m - 1)A + (A - H)$ is nef, so
$$(N + f^*(mA)) - \Delta = (N - \Delta + f^* H) + f^*(mA - H)$$
is nef and big by Lemma P7.9.2 and part 3 of Proposition P7.3.9. Theorem P7.8.18 gives $H^i(X, \mathcal{O}_X(K_X + N) \otimes f^* \mathcal{O}_Z(mA)) = 0$ for $i > 0$ and $m \geq 1$. By Lemma P7.8.16 with $m_0 = 1$, $R^j f_* \mathcal{O}_X(K_X + N) = 0$ for $j > 0$ and $H^i(Z, f_* \mathcal{O}_X(K_X + N) \otimes \mathcal{O}_Z(mA)) = 0$ for $i > 0$ and $m \geq 1$; the case $m = 1$ is the second statement.

*Corollary P7.9.4.* If $N - \Delta + f^*(mH)$ is ample, it is nef and big, and Theorem P7.9.3 applies with the ample divisor $mH$.

*Theorem P7.9.5.* This is Kollár and Mori, Theorem 2.70 (KM98), proved there from their Theorem 2.64, which is the Serre dual of Proposition P7.8.17, by a log resolution and the arguments of Theorem P7.8.18; it is a black box here. When $X$ is smooth and projective, $Z$ is projective, $\Delta$ has snc support with coefficients in $[0, 1)$, and $N - (K_X + \Delta) + f^* H$ is nef and big for an ample $H$, it is Theorem P7.9.3 applied to $N - K_X$.

### Exercises

1. (A) Let $f \colon X \to Z$ be a finite surjective morphism of projective varieties and $D$ a Cartier divisor on $X$. Show that $D$ is $f$-ample, so Corollary P7.9.4 gives $R^j f_* \mathcal{O}_X(K_X + D) = 0$ for $j > 0$, and check this against Corollary P4.4.3.
2. (A) In Example P7.9.6, compute $\mu_* \mathcal{O}_X(K_X - bE)$ for $b \geq 1$ and verify the second statement of Theorem P7.9.3 for $A = H$.
3. (B) Let $X$ be a smooth projective variety and $L$ a line bundle such that $L^m$ is generated by global sections and defines a morphism $f \colon X \to Z$ with $L^m = f^* \mathcal{O}_Z(1)$. Show that $R^j f_* (\omega_X \otimes L) = 0$ for $j > 0$, without assuming $L$ big.
4. (B) Show that Lemma P7.9.2 fails for $B$ big and not nef: on the blow-up of a point of $\mathbb{P}^2$, find a big $B$ and a nef $P$ such that $B + P$ is not nef.
5. (B) Let $f \colon X \to Z$ be a morphism of projective varieties with $X$ smooth, and $D$ an $f$-ample divisor. Show that $D + f^* H$ is nef and big for some ample $H$, and deduce the hypothesis of Theorem P7.9.3 for $N - \Delta = D$.
6. (C) Prove the following special case of Theorem P7.9.5: $X$ smooth projective, $\Delta$ snc with coefficients in $[0, 1)$, $Z$ projective and $N - (K_X + \Delta)$ $f$-ample, by reducing to Corollary P7.9.4. Then explain why $f$-nef and $f$-big is harder: produce, for a birational $f$, a divisor that is $f$-nef and $f$-big and not of the form nef and big plus the pullback of a divisor from $Z$.

### Lean

`MinimalModel.KawamataViehweg` in the project library is the relative klt statement of Theorem P7.9.5, without proof, attached to node MM7MQT1KEA. Theorem P7.9.3 is not stated there. Mathlib has no higher direct images of coherent sheaves. The handbook adds no `MinimalModel` node here.

### Notes and history

The relative form of the vanishing theorem appears in Kawamata's paper (Kaw82) and in Kawamata, Matsuda and Matsuki, Theorem 1-2-5 (KMM87), where it is the starting point of the cone and contraction theorems. The literature state is theorem. Kollár and Mori, Theorem 2.70 (KM98), is the form cited in the minimal model program, and Volume 1 uses it in the base point free theorem. The trick of twisting by $f^* A^m$ and using Leray is standard; Lemma P7.8.16 is in Kollár and Mori, Section 2.5, and in Lazarsfeld, Section 4.3 (Laz04). The vanishing of $H^i(Z, f_* \mathcal{O}_X(K_X + N) \otimes A)$ in Theorem P7.9.3 is a special case of Kollár's vanishing theorem, Theorem P7.9.13, and of Ambro's and Fujino's vanishing theorems for quasi-log schemes.
