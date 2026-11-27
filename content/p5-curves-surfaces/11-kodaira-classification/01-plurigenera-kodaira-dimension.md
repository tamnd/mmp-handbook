---
title: Plurigenera and Kodaira dimension
nodes: []
sources: [Har77, Bea96, Laz04]
reads_with: [Bea96:ch7, Har77:V.6, Laz04:2.1]
requires: [P2.4, P2.7, P3.12, P4.2, P4.4, P4.5, P4.7, P5.1, P5.5, P5.6, P5.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Plurigenera and Kodaira dimension

### Statement

In this chapter $k$ is algebraically closed, a *curve* $C$ without further words is a smooth projective curve over $k$ of genus $g(C)$, and $S$ is a smooth projective surface over $k$ with canonical divisor $K = K_S$, in the notation of Chapter 5. For a divisor $D$ write $h^i(D) = h^i(\mathcal{O}(D))$. Since $k$ is algebraically closed, every regular function on a projective variety is constant, and a rational function that is algebraic over $k$ lies in $k$.

**Definition P5.11.1 (the Iitaka dimension of a divisor).** Let $X$ be a smooth projective curve or surface and $D$ a divisor on $X$. If $h^0(mD) = 0$ for every $m \geq 1$, put $\kappa(D) = -\infty$. Otherwise $\kappa(D)$ is the least integer $j \geq 0$ for which there is a constant $c$ with $h^0(mD) \leq c \, m^j$ for all $m \geq 1$. This integer exists by Proposition P5.11.3 below. The number $\kappa(D)$ is the *Iitaka dimension* of $D$, and $D$ is *big* if $\kappa(D) = \dim X$.

**Definition P5.11.2 (plurigenera and Kodaira dimension).** For $n \geq 1$ the *$n$-th plurigenus* of $X$ is $P_n(X) = h^0(nK_X)$. The *geometric genus* is $p_g(X) = P_1(X) = h^0(K_X)$, and for a surface the *irregularity* is $q(S) = h^1(\mathcal{O}_S)$. The *Kodaira dimension* of $X$ is $\kappa(X) = \kappa(K_X)$. With the convention $-\infty + j = -\infty$, the values of $\kappa$ are added as integers.

By Serre duality (Corollary P4.7.21), $h^2(\mathcal{O}_S) = h^0(K)$, so $\chi(\mathcal{O}_S) = 1 - q + p_g$.

**Proposition P5.11.3 (the growth of $h^0(mD)$).** Let $D$ be a divisor on $S$. By Corollary P5.5.3 there is a very ample divisor $H$ on $S$ such that $|H|$ contains a smooth integral curve; fix one.

1. If $D \cdot H < 0$, then $h^0(D) = 0$. If $D \cdot H \geq 0$, then $h^0(D) \leq (D \cdot H + 1)^2$. So $\kappa(D)$ is defined and lies in $\{-\infty, 0, 1, 2\}$. On a curve, $h^0(D) \leq \max(0, \deg D + 1)$, and $\kappa(D) \in \{-\infty, 0, 1\}$.
2. $\kappa(D)$ depends only on the linear equivalence class of $D$, and $\kappa(aD) = \kappa(D)$ for every $a \geq 1$.
3. $\kappa(D) \geq 1$ if and only if $h^0(mD) \geq 2$ for some $m \geq 1$. So $\kappa(D) = 0$ if and only if $h^0(mD) \leq 1$ for all $m \geq 1$, with equality for some $m$.
4. If $D^2 > 0$ and $D \cdot H' > 0$ for some ample $H'$, then there is $c > 0$ with $h^0(mD) \geq c \, m^2$ for all large $m$, and $\kappa(D) = 2$.
5. $\kappa(D) = 2$ if and only if $aD \sim A + F$ for some $a \geq 1$, some ample divisor $A$ and some effective divisor $F$.

Lean: not in Lean as stated.

**Lemma P5.11.4 (sections on a product).** Let $X$ and $Y$ be projective varieties over $k$, $p$ and $q$ the projections of $X \times Y$, and $\mathcal{L}$, $\mathcal{M}$ invertible sheaves on $X$ and $Y$. Write $\mathcal{L} \boxtimes \mathcal{M} = p^* \mathcal{L} \otimes q^* \mathcal{M}$. Then
$$H^0(X \times Y, \mathcal{L} \boxtimes \mathcal{M}) \cong H^0(X, \mathcal{L}) \otimes_k H^0(Y, \mathcal{M}).$$
If $X$ is a curve, then $h^n(\mathcal{L} \boxtimes \mathcal{M}) = \sum_{a + b = n} h^a(\mathcal{L}) \, h^b(\mathcal{M})$ for every $n$.

Lean: not in Lean as stated.

**Proposition P5.11.5 (curves and products of curves).**

1. For a curve $C$ of genus $g$: if $g = 0$, then $P_n(C) = 0$ for all $n \geq 1$ and $\kappa(C) = -\infty$; if $g = 1$, then $P_n(C) = 1$ for all $n$ and $\kappa(C) = 0$; if $g \geq 2$, then $P_1(C) = g$, $P_n(C) = (2n - 1)(g - 1)$ for $n \geq 2$, and $\kappa(C) = 1$.
2. Let $S = C_1 \times C_2$ with $g_i = g(C_i)$. Then $P_n(S) = P_n(C_1) P_n(C_2)$ for all $n \geq 1$, $p_g(S) = g_1 g_2$, $q(S) = g_1 + g_2$, $\chi(\mathcal{O}_S) = (1 - g_1)(1 - g_2)$, $K_S^2 = 8 (g_1 - 1)(g_2 - 1)$, and
$$\kappa(C_1 \times C_2) = \kappa(C_1) + \kappa(C_2).$$

Lean: not in Lean as stated.

**Theorem P5.11.6 (birational invariance).**

1. Let $\pi \colon \tilde S \to S$ be the blow-up of a point. Then $P_n(\tilde S) = P_n(S)$ for every $n \geq 1$, $q(\tilde S) = q(S)$, $\chi(\mathcal{O}_{\tilde S}) = \chi(\mathcal{O}_S)$ and $\kappa(\tilde S) = \kappa(S)$, while $K_{\tilde S}^2 = K_S^2 - 1$.
2. Let $S$ and $S'$ be smooth projective surfaces that are birational. Then $P_n(S) = P_n(S')$ for all $n \geq 1$, $p_g(S) = p_g(S')$, $q(S) = q(S')$, $\chi(\mathcal{O}_S) = \chi(\mathcal{O}_{S'})$ and $\kappa(S) = \kappa(S')$.

Lean: not in Lean as stated.

So the plurigenera, the irregularity and the Kodaira dimension are invariants of the function field $k(S)$, while $K^2$ is not.

### Proof in words

A section of $\mathcal{O}(D)$ restricts to a smooth curve $H$ in a very ample class, and the sections that vanish on $H$ are the sections of $D - H$. A line bundle of degree $d$ on a smooth curve has at most $d + 1$ sections, so each step of the chain $D \supseteq D - H \supseteq D - 2H \supseteq \cdots$ loses at most $D \cdot H + 1$ sections, and the chain reaches a divisor with negative degree on $H$, which has no sections, after at most $D \cdot H + 1$ steps. Applied to $mD$ this bounds $h^0(mD)$ by a multiple of $m^2$, so the Kodaira dimension of a surface is at most $2$. Riemann-Roch gives the matching lower bound $h^0(mD) \geq c\, m^2$ when $D^2 > 0$. Two independent sections $s, t$ of $mD$ give the $j + 1$ independent sections $s^{j - i} t^i$ of $jmD$, so the dimension is at least $1$ as soon as some $h^0(mD)$ exceeds $1$.

On a product of curves the canonical sheaf is $p_1^* \omega_{C_1} \otimes p_2^* \omega_{C_2}$, and the sections of an exterior product are products of sections, by flat base change over $\operatorname{Spec} k$. So the plurigenera of $C_1 \times C_2$ are products of the plurigenera of the curves, and growth rates multiply.

Birational invariance is a computation on one blow-up: $nK_{\tilde S} = \pi^*(nK_S) + nE$, and the fixed curve $nE$ adds no sections. Chapter 7 reduces every birational map between smooth projective surfaces to blow-ups: such a map is resolved by blow-ups of the source, and the resulting birational morphism is a composite of blow-ups.

### Examples

**Example P5.11.7 (the projective plane and rational surfaces).** On $\mathbb{P}^2$, $K = -3\ell$ (Corollary P3.12.22), so $nK \cdot \ell = -3n < 0$ and $P_n(\mathbb{P}^2) = h^0(\mathcal{O}(-3n)) = 0$ for $n \geq 1$, by Theorem P4.2.1, which also gives $q(\mathbb{P}^2) = 0$. So $\kappa(\mathbb{P}^2) = -\infty$, and by Theorem P5.11.6 every rational surface has $\kappa = -\infty$ and $p_g = q = 0$. The blow-up $S_r$ of $\mathbb{P}^2$ in $r$ points has $K^2 = 9 - r$ (Example P5.6.8): all the $S_r$ are birational to each other, with the same plurigenera, and with every value $K^2 \leq 9$.

**Example P5.11.8 (products with the projective line).** Let $C$ be a curve of genus $g$ and $S = C \times \mathbb{P}^1$. By Proposition P5.11.5, $P_n(S) = P_n(C) \cdot P_n(\mathbb{P}^1) = 0$, $q(S) = g$, $p_g(S) = 0$, $\chi(\mathcal{O}_S) = 1 - g$ and $K_S^2 = 8(1 - g)$. So $\kappa(S) = -\infty$ for every $C$. The irregularity separates these surfaces: for $g \neq g'$, $C \times \mathbb{P}^1$ and $C' \times \mathbb{P}^1$ are not birational by Theorem P5.11.6. A surface birational to some $C \times \mathbb{P}^1$ is *birationally ruled*, and it has $\kappa = -\infty$ and $q = g(C)$.

**Example P5.11.9 (abelian and K3 surfaces).** Let $E$ and $E'$ be elliptic curves (Definition P5.4.1) and $A = E \times E'$. By Proposition P5.1.13, $K_E \sim 0$ and $K_{E'} \sim 0$, so $K_A \sim 0$ and $P_n(A) = 1$ for all $n$: $\kappa(A) = 0$, with $p_g = 1$, $q = 2$, $\chi(\mathcal{O}_A) = 0$ and $K_A^2 = 0$. Let $X \subseteq \mathbb{P}^3$ be a smooth quartic surface. By Corollary P3.12.31, $\omega_X \cong \mathcal{O}_X$, so again $P_n(X) = 1$ and $\kappa(X) = 0$. From $0 \to \mathcal{O}_{\mathbb{P}^3}(-4) \to \mathcal{O}_{\mathbb{P}^3} \to \mathcal{O}_X \to 0$ and Theorem P4.2.1, $H^1(\mathcal{O}_X)$ sits between $H^1(\mathcal{O}_{\mathbb{P}^3}) = 0$ and $H^2(\mathcal{O}_{\mathbb{P}^3}(-4)) = 0$, so $q(X) = 0$, $p_g(X) = 1$ and $\chi(\mathcal{O}_X) = 2$. The two surfaces have the same plurigenera and different irregularities, so they are not birational.

**Example P5.11.10 (elliptic surfaces of product type).** Let $E$ be an elliptic curve, $C$ a curve of genus $g \geq 2$ and $S = E \times C$. By Proposition P5.11.5, $P_n(S) = P_n(C) = (2n - 1)(g - 1)$ for $n \geq 2$, $p_g(S) = g$, $q(S) = g + 1$, $\chi(\mathcal{O}_S) = 0$ and $K_S^2 = 0$, and $\kappa(S) = 0 + 1 = 1$. The canonical divisor is $K_S = q^* K_C$, a sum of $2g - 2$ fibres $E \times \{y\}$ of the projection to $C$, so $K_S$ is effective and nonzero while $K_S^2 = 0$: the plurigenera grow linearly although $K_S$ is not numerically trivial. Riemann-Roch is consistent with this: $\chi(nK_S) = \chi(\mathcal{O}_S) + \frac{1}{2} n(n - 1) K_S^2 = 0$, and by Lemma P5.11.4, $h^1(nK_S) = h^0(nK_E)\, h^1(nK_C) + h^1(nK_E)\, h^0(nK_C) = 0 + (2n-1)(g-1)$ for $n \geq 2$, so $h^0(nK_S) - h^1(nK_S) + h^2(nK_S) = 0$ with $h^2(nK_S) = h^0((1-n)K_S) = 0$.

**Example P5.11.11 (surfaces in $\mathbb{P}^3$).** Let $X = V_+(F) \subseteq \mathbb{P}^3$ be a smooth surface of degree $d$ and $H$ a plane section. By Corollary P3.12.31, $K_X = (d - 4) H$. For $d \leq 3$, $nK_X \cdot H = n(d - 4) d < 0$, so $P_n(X) = 0$ and $\kappa(X) = -\infty$. For $d = 4$, $\kappa(X) = 0$ by Example P5.11.9. For $d \geq 5$, $K_X$ is very ample with $K_X^2 = (d - 4)^2 d > 0$, so $\kappa(X) = 2$ by part 4 of Proposition P5.11.3. Explicitly, twisting $0 \to \mathcal{O}_{\mathbb{P}^3}(-d) \to \mathcal{O}_{\mathbb{P}^3} \to \mathcal{O}_X \to 0$ by $\mathcal{O}(m)$ and using $H^1(\mathbb{P}^3, \mathcal{O}(m - d)) = 0$ (Theorem P4.2.1) gives, for $m \geq 0$,
$$h^0(\mathcal{O}_X(m)) = h^0(\mathcal{O}_{\mathbb{P}^3}(m)) - h^0(\mathcal{O}_{\mathbb{P}^3}(m - d)),$$
and $P_n(X) = h^0(\mathcal{O}_X(n(d - 4)))$, a polynomial in $n$ of degree $2$ for $n$ large. For the quintic, $d = 5$: $p_g = h^0(\mathcal{O}_X(1)) = 4$, $P_2 = h^0(\mathcal{O}_X(2)) = 10$, $P_3 = 20$, $P_4 = 35$, $P_5 = \binom{8}{3} - \binom{3}{3} = 55$. As in Example P5.11.9, $q(X) = 0$, so $\chi(\mathcal{O}_X) = 1 + 4 = 5$, and Riemann-Roch (Theorem P5.5.13) predicts $P_n = \chi(nK) = 5 + \frac{1}{2} n (n - 1) \cdot 5$ for $n \geq 2$, using $h^2(nK) = h^0((1 - n)K) = 0$ and $h^1(\mathcal{O}_X(m)) = 0$, which holds because $H^1(\mathcal{O}_X(m))$ sits between $H^1(\mathbb{P}^3, \mathcal{O}(m)) = 0$ and $H^2(\mathbb{P}^3, \mathcal{O}(m - d)) = 0$. The values $10, 20, 35, 55$ for $n = 2, 3, 4, 5$ agree.

**Example P5.11.12 (products of curves of higher genus).** Let $g_1, g_2 \geq 2$ and $S = C_1 \times C_2$. By Proposition P5.11.5, $\kappa(S) = 2$, $K_S^2 = 8(g_1 - 1)(g_2 - 1) > 0$, $\chi(\mathcal{O}_S) = (g_1 - 1)(g_2 - 1)$, and for $n \geq 2$
$$P_n(S) = (2n - 1)^2 (g_1 - 1)(g_2 - 1) = \chi(\mathcal{O}_S) + \tfrac{1}{2} n(n - 1) K_S^2 ,$$
since $(2n - 1)^2 = 1 + 4n(n - 1)$. The second expression is Riemann-Roch for $nK_S$; it is equal to $h^0(nK_S)$ because $h^2(nK_S) = h^0((1 - n)K_S) = 0$ and, by Lemma P5.11.4, $h^1(nK_S) = 0$, as $h^1(nK_{C_i}) = h^0((1 - n)K_{C_i}) = 0$. For $g_1 = g_2 = 2$: $p_g = 4$, $q = 4$, $K^2 = 8$, $P_2 = 9$.

### Proof

*Proposition P5.11.3.* (1) On a smooth curve $C$, a line bundle $\mathcal{N}$ of negative degree has no nonzero section, since the divisor of a section is effective. If $\deg \mathcal{N} = d \geq 0$ and $x \in C$, the sequence $0 \to \mathcal{N}(-x) \to \mathcal{N} \to \mathcal{N} \otimes \kappa(x) \to 0$ gives $h^0(\mathcal{N}) \leq h^0(\mathcal{N}(-x)) + 1$, and by induction on $d$, $h^0(\mathcal{N}) \leq d + 1$. On a curve this gives $h^0(mD) \leq m \deg D + 1$ or $h^0(mD) = 0$, and $\kappa(D) \leq 1$.

On $S$, if $h^0(D) > 0$, then $D$ is linearly equivalent to an effective divisor, and $D \cdot H \geq 0$ by Lemma P5.5.20. This proves the first claim. Let $D \cdot H = d \geq 0$ and $e = H^2 \geq 1$. For every divisor $D'$ the sequence
$$0 \to \mathcal{O}_S(D' - H) \to \mathcal{O}_S(D') \to \mathcal{O}_H(D') \to 0$$
and the bound on the smooth integral curve $H$ give $h^0(D') \leq h^0(D' - H) + \max(0, D' \cdot H + 1)$, since $\deg \mathcal{O}_H(D') = D' \cdot H$ (Theorem P5.5.6). Apply this to $D' = D - iH$ for $i = 0, 1, \dots, t - 1$, where $t$ is the least integer with $(D - tH) \cdot H = d - te < 0$. Then $h^0(D - tH) = 0$, $t \leq d/e + 1 \leq d + 1$, and every term $\max(0, d - ie + 1)$ is at most $d + 1$, so $h^0(D) \leq t (d + 1) \leq (d + 1)^2$. Applied to $mD$, with $mD \cdot H = md$, this gives $h^0(mD) \leq (md + 1)^2 \leq (d + 1)^2 m^2$ for $m \geq 1$, so $\kappa(D) \leq 2$ when $\kappa(D) \neq -\infty$. If $D \cdot H < 0$, then $h^0(mD) = 0$ for all $m \geq 1$.

(2) Linearly equivalent divisors have isomorphic sheaves. For $a \geq 1$, the numbers $h^0(maD)$ are a subsequence of the $h^0(mD)$, so $\kappa(aD) \leq \kappa(D)$, and $\kappa(aD) = -\infty$ forces $\kappa(D) = -\infty$, since $h^0(mD) > 0$ implies $h^0(amD) > 0$ by taking the $a$-th power of a section. Conversely let $\kappa(aD) = j \geq 0$, with $h^0(maD) \leq c\, m^j$ for all $m \geq 1$. If $h^0(mD) > 0$, choose a nonzero section $s$ of $\mathcal{O}(mD)$. Multiplication by $s^{a - 1}$ is injective from $H^0(mD)$ to $H^0(amD)$, since $S$ is integral, so $h^0(mD) \leq h^0(amD) \leq c\, m^j$. If $h^0(mD) = 0$ the bound holds trivially. So $\kappa(D) \leq j$.

(3) If $s, t \in H^0(mD)$ are linearly independent, then $f = t/s$ is a nonconstant rational function, hence transcendental over $k$. The sections $s^{j - i} t^i = s^j f^i$, $0 \leq i \leq j$, of $\mathcal{O}(jmD)$ are then linearly independent, so $h^0(jmD) \geq j + 1$ is unbounded, and $\kappa(D) \geq 1$. Conversely, if $h^0(mD) \leq 1$ for every $m$, then $h^0(mD) \leq 1 \cdot m^0$ and $\kappa(D) \leq 0$.

(4) As in the proof of Lemma P5.5.21, $h^0(K - mD) = 0$ for $m > (H' \cdot K)/(H' \cdot D)$, and for those $m$ Theorem P5.5.13 gives $h^0(mD) \geq \chi(\mathcal{O}_S) + \frac{1}{2} m^2 D^2 - \frac{1}{2} m\, D \cdot K$, which is at least $\frac{1}{4} D^2 m^2$ for $m$ large. A bound $h^0(mD) \leq c\, m$ is then impossible, so $\kappa(D) = 2$ by (1).

(5) Suppose $aD \sim A + F$. Choose a nonzero section $\sigma$ of $\mathcal{O}(F)$. Multiplication by $\sigma^m$ embeds $H^0(mA)$ into $H^0(maD)$. By Lemma P5.5.20, $A^2 > 0$, so (4) with $H' = A$ gives $h^0(maD) \geq h^0(mA) \geq c\, m^2$ for large $m$, so $\kappa(aD) = 2$ and $\kappa(D) = 2$ by (2). Conversely let $\kappa(D) = 2$. Then $h^0(mD) \leq c\, m$ fails for every $c$, so there is $m \geq 1$ with $h^0(mD) > m\, D \cdot H + 1$ (in particular $h^0(mD) > 0$, so $D \cdot H \geq 0$). The sequence $0 \to \mathcal{O}(mD - H) \to \mathcal{O}(mD) \to \mathcal{O}_H(mD) \to 0$ and $h^0(\mathcal{O}_H(mD)) \leq mD \cdot H + 1$ give $h^0(mD - H) > 0$. So $mD - H \sim F$ with $F$ effective, and $mD \sim H + F$ with $H$ ample. $\square$

*Lemma P5.11.4.* The morphism $g \colon X \to \operatorname{Spec} k$ is flat, and $f \colon Y \to \operatorname{Spec} k$ is separated and quasi-compact. In the cartesian square formed by $p$, $q$, $f$ and $g$, flat base change (Theorem P4.5.1) gives $R^b p_* (q^* \mathcal{M}) \cong g^* R^b f_* \mathcal{M} = H^b(Y, \mathcal{M}) \otimes_k \mathcal{O}_X$ for every $b$. By the projection formula (Proposition P4.4.10),
$$R^b p_* (\mathcal{L} \boxtimes \mathcal{M}) \cong \mathcal{L} \otimes R^b p_* q^* \mathcal{M} \cong \mathcal{L} \otimes_k H^b(Y, \mathcal{M}),$$
a direct sum of $h^b(\mathcal{M})$ copies of $\mathcal{L}$; the dimension is finite by Theorem P4.2.7. For $b = 0$, taking global sections gives $H^0(X \times Y, \mathcal{L} \boxtimes \mathcal{M}) = H^0(X, p_*(\mathcal{L} \boxtimes \mathcal{M})) \cong H^0(X, \mathcal{L}) \otimes_k H^0(Y, \mathcal{M})$. If $X$ is a curve, the Leray spectral sequence (Corollary P2.4.26) has $E_2^{a, b} = H^a(X, \mathcal{L}) \otimes_k H^b(Y, \mathcal{M})$, which vanishes for $a \geq 2$ by Grothendieck vanishing (Theorem P2.7.13). Every differential $d_r$ with $r \geq 2$ raises $a$ by $r$, so it starts or ends at a zero term, and $E_2 = E_\infty$. The abutment $H^n$ has a filtration with quotients $E_\infty^{a, n - a}$, and since these are vector spaces, $h^n = \sum_{a + b = n} h^a(\mathcal{L})\, h^b(\mathcal{M})$. $\square$

*Proposition P5.11.5.* (1) If $g = 0$, then $\deg nK_C = -2n < 0$ and $P_n = 0$. If $g = 1$, then $K_C \sim 0$ by Proposition P5.1.13 and $P_n = 1$. If $g \geq 2$, $P_1 = g$ by definition of the genus, and for $n \geq 2$, $\deg nK_C = n(2g - 2) > 2g - 2$, so $\ell(K_C - nK_C) = 0$ and Theorem P5.1.10 gives $P_n = n(2g - 2) + 1 - g = (2n - 1)(g - 1)$. Then $(g - 1) n \leq P_n \leq 2(g - 1) n$ for $n \geq 2$, so $\kappa(C) = 1$, while for $g = 1$ the constant sequence gives $\kappa = 0$.

(2) By Proposition P3.12.23, $\omega_S \cong p_1^* \omega_{C_1} \otimes p_2^* \omega_{C_2}$, so $\omega_S^{\otimes n} \cong \omega_{C_1}^{\otimes n} \boxtimes \omega_{C_2}^{\otimes n}$, and Lemma P5.11.4 gives $P_n(S) = P_n(C_1) P_n(C_2)$, in particular $p_g(S) = g_1 g_2$. For $\mathcal{L} = \mathcal{O}_{C_1}$ and $\mathcal{M} = \mathcal{O}_{C_2}$, the second part of the lemma gives $h^1(\mathcal{O}_S) = g_1 \cdot 1 + 1 \cdot g_2$, so $\chi(\mathcal{O}_S) = 1 - g_1 - g_2 + g_1 g_2 = (1 - g_1)(1 - g_2)$. For $K_S^2$, write $K_S \sim p_1^* K_{C_1} + p_2^* K_{C_2}$. For a divisor $A$ on $C_1$, the restriction of $\mathcal{O}(p_1^* A)$ to a fibre $\{x\} \times C_2$ is trivial, and its restriction to a fibre $C_1 \times \{y\} \cong C_1$ is $\mathcal{O}_{C_1}(A)$. By Theorem P5.5.6 and bilinearity, writing $B$ as a difference of effective divisors, $p_1^* A \cdot p_1^* A' = 0$ and $p_1^* A \cdot p_2^* B = \deg A \cdot \deg B$ for divisors $A, A'$ on $C_1$ and $B$ on $C_2$. So
$$K_S^2 = 2 \deg K_{C_1} \deg K_{C_2} = 2 (2g_1 - 2)(2g_2 - 2) = 8(g_1 - 1)(g_2 - 1).$$

For the Kodaira dimension, if $\kappa(C_i) = -\infty$ for some $i$, then $P_n(S) = 0$ for all $n$ and $\kappa(S) = -\infty$. Otherwise the proof of (1) gives $j_i = \kappa(C_i) \in \{0, 1\}$ and constants $0 < a_i \leq b_i$ with $a_i n^{j_i} \leq P_n(C_i) \leq b_i n^{j_i}$ for all $n \geq 2$. Then $a_1 a_2 n^{j_1 + j_2} \leq P_n(S) \leq b_1 b_2 n^{j_1 + j_2}$ for $n \geq 2$. The upper bound shows $\kappa(S) \leq j_1 + j_2$, after enlarging the constant to cover $n = 1$, and the lower bound excludes every bound $P_n(S) \leq c\, n^{j}$ with $j < j_1 + j_2$. So $\kappa(S) = j_1 + j_2$. $\square$

*Theorem P5.11.6.* (1) By part 3 of Theorem P5.6.3, $nK_{\tilde S} = \pi^*(nK_S) + nE$, and by part 3 of Corollary P5.6.5, $h^0(\pi^*(nK_S) + nE) = h^0(nK_S)$. The same part of Theorem P5.6.3 gives $h^i(\mathcal{O}_{\tilde S}) = h^i(\mathcal{O}_S)$, hence $q$ and $\chi$ agree, and $K_{\tilde S}^2 = K_S^2 - 1$. Equal plurigenera give equal Kodaira dimensions.

(2) Let $\varphi \colon S \dashrightarrow S'$ be birational. By the elimination of indeterminacy of Chapter 7, there is a composite $f \colon S'' \to S$ of blow-ups of points such that $g = \varphi \circ f \colon S'' \to S'$ is a morphism. It is a birational morphism of smooth projective surfaces, so by the factorization theorem of Chapter 7 it is a composite of blow-ups of points. Applying (1) to each blow-up in $f$ and in $g$ gives the equalities between $S$ and $S''$ and between $S'$ and $S''$. $\square$

### Exercises

1. (A) Let $X \subseteq \mathbb{P}^4$ be a smooth complete intersection of a quadric and a cubic, and $Y \subseteq \mathbb{P}^5$ a smooth complete intersection of three quadrics. Use the second part of Corollary P3.12.31 twice or three times to show that $\omega_X \cong \mathcal{O}_X$ and $\omega_Y \cong \mathcal{O}_Y$, and deduce $\kappa = 0$ for both.
2. (A) Let $D$ be a divisor on $S$ with $2D \sim 0$ and $D \not\sim 0$. Show that $h^0(mD) = 1$ for $m$ even and $h^0(mD) = 0$ for $m$ odd, so $\kappa(D) = 0$ although $h^0(D) = 0$.
3. (B) Let $D$ be a divisor on $S$ and $F$ an effective divisor. Show that $\kappa(D + F) \geq \kappa(D)$, and give an example on $\mathbb{P}^1 \times \mathbb{P}^1$ with $\kappa(D) = 0$, $\kappa(D + F) = 1$ and $F$ a fibre.
4. (B) Compute $p_g$, $q$, $K^2$ and $P_2$ for $C_1 \times C_2$ with $g_1 = 2$ and $g_2 = 3$, both from Proposition P5.11.5 and from Riemann-Roch, and check that they agree.
5. (B) Let $X \subseteq \mathbb{P}^3$ be a smooth surface of degree $d \geq 5$. Show that $P_n(X) = \chi(\mathcal{O}_X) + \frac{1}{2} n(n - 1) d (d - 4)^2$ for $n \geq 2$, with $\chi(\mathcal{O}_X) = 1 + \binom{d - 1}{3}$, and check the formula for $d = 6$ and $n = 2$ against $h^0(\mathcal{O}_X(4))$.
6. (C) Let $S = E \times C$ with $E$ elliptic and $g(C) \geq 2$. Show that for $n \geq 2$ the rational map $\varphi_{|nK_S|}$ is the composite of the projection $S \to C$ with the morphism $\varphi_{|nK_C|} \colon C \to \mathbb{P}^{P_n - 1}$, so its image is a curve. Conclude that $\kappa(S)$ equals the dimension of the image of $\varphi_{|nK_S|}$ for $n \geq 2$.

### Lean

Mathlib does not formalize the cohomology of coherent sheaves on schemes, so neither the plurigenera nor the Iitaka dimension can be stated there; it has the canonical sheaf of neither a curve nor a surface. The growth notions of Definition P5.11.1 are elementary statements about sequences of natural numbers, and could be stated with `Asymptotics.IsBigO`. The handbook adds no `MinimalModel` node here.

### Notes and history

The plurigenera are due to Enriques, who characterized ruled surfaces by the vanishing of $P_{12}$, and to Castelnuovo, whose criterion of rationality of 1896 uses $P_2$. The Kodaira dimension was introduced by Iitaka in 1970, and Shafarevich's seminar on algebraic surfaces (1965) organized the classification by the growth of the plurigenera. For a divisor on a normal projective variety of any dimension, Lazarsfeld, Section 2.1, defines $\kappa(D)$ as the maximal dimension of the image of $\varphi_{|mD|}$ and shows that $h^0(mD)$ grows like $m^{\kappa(D)}$ for $m$ divisible enough, which is Definition P5.11.1 in the cases used here; Exercise 6 checks the agreement on an example. The literature state is theorem. Birational invariance of the plurigenera holds in every dimension, because a pluricanonical form on a smooth variety extends across a closed subset of codimension $2$; Hartshorne, Theorem II.8.19, proves it for $p_g$, and the same proof works for $P_n$. The factorization argument above is special to surfaces. Iitaka's conjecture $C_{n,m}$ on the subadditivity $\kappa(X) \geq \kappa(F) + \kappa(Y)$ for fibre spaces $X \to Y$ with general fibre $F$ generalizes the additivity of Proposition P5.11.5; it is open in general, and in characteristic $0$ it is a theorem when $\dim X \leq 6$ (Birkar, 2009).
