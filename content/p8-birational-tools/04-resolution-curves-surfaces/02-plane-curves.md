---
title: Embedded resolution of plane curves and log resolutions
nodes: []
sources: [Kol07, Har77, Cut04, KM98]
reads_with: [Kol07:1.4, Har77:V.3, Cut04:3, KM98:1.4]
requires: [P3.11, P5.6, P5.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Embedded resolution of plane curves and log resolutions

### Statement

As in Section 6.2 of Volume P5, $S$ is a smooth projective surface over an algebraically closed field $k$, a *curve* on $S$ is an effective divisor, and a sequence of blow-ups $S_n \to \dots \to S_0 = S$ has centres $q_i \in S_{i-1}$ and exceptional curves $E_i \subseteq S_i$. For $S = \mathbb{P}^2$ these are the plane curves; every statement is local over $S$, so it applies to a curve in $\mathbb{A}^2$ through its projective closure. The embedded resolution of Theorem P5.6.17 is the starting point: after finitely many blow-ups over the singular points of $C_{\mathrm{red}}$, the support of the total transform of $C$ has simple normal crossings in the sense of Definition P5.6.12. This section proves the numerical rules that compute such a sequence and shows that the shortest one is unique.

**Definition P8.4.8 (log resolution of a curve on a surface).** Let $C \neq 0$ be a curve on $S$. A *log resolution* of $(S, C)$ is a birational morphism $\pi \colon S' \to S$ from a smooth projective surface such that the reduced curve $\pi^{-1}(C) \cup \operatorname{Exc}(\pi)$ has simple normal crossings. By Theorem P5.7.12, $\pi$ is a composite of point blow-ups, and $\operatorname{Exc}(\pi)$ is the union of the curves contracted by $\pi$. For the pair $(S, C_{\mathrm{red}})$ this is Definition 4.2.9 of Volume 4, since $\pi^{-1}(C) \cup \operatorname{Exc}(\pi)$ is the union of the strict transform of $C$ and the exceptional curves.

**Proposition P8.4.9 (the numerical data of a sequence of blow-ups).** Let $S_n \to \dots \to S_0 = S$ be a sequence of blow-ups with composite $\pi$, let $C$ be a curve on $S$ with strict transforms $C_i$ on $S_i$, and let $F_j^{(i)}$ be the strict transform of $E_j$ on $S_i$ for $j \leq i$. Write $q_i \in F_j$ for $q_i \in F_j^{(i-1)}$, and $F_j = F_j^{(n)}$. Define integers by the recursions
$$N_i = m_{q_i}(C_{i-1}) + \sum_{j < i, \ q_i \in F_j} N_j, \qquad k_i = 1 + \sum_{j < i, \ q_i \in F_j} k_j .$$

1. $\pi^* C = C_n + \sum_{i=1}^n N_i F_i$.
2. $K_{S_n} = \pi^* K_S + \sum_{i=1}^n k_i F_i$.
3. $F_j^2 = -1 - \#\{ i > j : q_i \in F_j \}$, and each $F_j$ is a smooth rational curve.

The number $N_i$ is the multiplicity of $E_i$ in the total transform of $C$, and $k_i$ is its discrepancy over $S$, in the sense of Chapter 13.

Lean: not in Lean as stated.

**Theorem P8.4.10 (the minimal log resolution).** Let $C \neq 0$ be a curve on $S$. Put $S_0 = S$, and let $D_i$ be the reduced total transform of $C$ on $S_i$, that is, the reduced curve with support the preimage of $C$. As long as $D_i$ does not have simple normal crossings, let $S_{i+1} \to S_i$ be the blow-up of a point $q_{i+1}$ at which $D_i$ does not have simple normal crossings.

1. The process stops, at some $S_n$, and $\pi \colon S_n \to S$ is a log resolution of $(S, C)$. It is an isomorphism over the open set of points of $S$ at which $C_{\mathrm{red}}$ has simple normal crossings.
2. Every log resolution $\pi' \colon S' \to S$ of $(S, C)$ factors as $\pi' = \pi \circ h$ for a unique morphism $h \colon S' \to S_n$, and $h$ is a composite of point blow-ups.
3. So $\pi$ does not depend on the choice of the points $q_i$ up to a unique isomorphism over $S$, and $n = \rho(S_n) - \rho(S)$ is the smallest number of blow-ups in a log resolution. It is called the *minimal log resolution* of $(S, C)$.

Lean: not in Lean as stated.

### Proof in words

Each blow-up pulls back a curve to its strict transform plus its multiplicity times the new exceptional curve, and pulls back the canonical class to itself plus the exceptional curve. Pushing these two rules through the sequence gives the recursions for $N_i$ and $k_i$. For the minimal log resolution, the point is that a log resolution cannot be an isomorphism over a point where the reduced total transform fails to have simple normal crossings, because near that point it would be the same curve. So by the factorization theorem of Volume P5 it factors through the blow-up of that point, and by induction through every step of the process. The Picard number of a log resolution, which exists by Theorem P5.6.17, bounds the length of the process.

### Examples

**Example P8.4.11 (the cusp).** Let $C = V(y^2 - x^3)$, near the origin of $\mathbb{A}^2 \subseteq \mathbb{P}^2$. The blow-ups are those of Example P5.6.19. The origin is not a point of simple normal crossings, because $C$ is not smooth there, so $q_1 = 0$. After one blow-up the strict transform $C_1$ is smooth and tangent to $E_1$ at $q_2$, so $(C_1 \cdot E_1)_{q_2} = 2$ and $D_1$ is not snc at $q_2$. After the second, $C_2$, $F_1^{(2)}$ and $E_2$ pass through $q_3$ with distinct tangents, and three components through one point are not allowed. After the third, the support of the total transform has simple normal crossings. So the minimal log resolution has $n = 3$. The centre $q_1$ has multiplicity $2$ on $C$ and lies on no earlier exceptional curve; $q_2$ has multiplicity $1$ on $C_1$ and lies on $F_1$; $q_3$ has multiplicity $1$ on $C_2$ and lies on $F_1$ and $F_2$. Proposition P8.4.9 gives
$$N_1 = 2, \quad N_2 = 1 + 2 = 3, \quad N_3 = 1 + 2 + 3 = 6, \qquad k_1 = 1, \quad k_2 = 1 + 1 = 2, \quad k_3 = 1 + 1 + 2 = 4,$$
so $\pi^* C = C_3 + 2F_1 + 3F_2 + 6F_3$ and $K_{S_3} = \pi^* K_S + F_1 + 2F_2 + 4F_3$, with $F_1^2 = -3$, $F_2^2 = -2$, $F_3^2 = -1$ by part 3. The ratios $(k_i + 1)/N_i$ are $1$, $1$ and $5/6$, and the strict transform has $(0 + 1)/1 = 1$. By Theorem 4.2.14 of Volume 4, the pair $(\mathbb{A}^2, tC)$ is log canonical near the origin exactly when $t \leq 5/6$, which is the log canonical threshold of Example 4.6.7 of Volume 4; the log resolution used there is Example 4.2.16 of Volume 4.

**Example P8.4.12 (the node, and normal crossings that are not simple).** Let $\operatorname{char} k \neq 2$ and $C = V(y^2 - x^2(x + 1))$, the nodal cubic near the origin. The curve $C$ is integral and not smooth at the origin, so it does not have simple normal crossings there, although its two analytic branches cross transversally. One blow-up at the origin gives, in the chart $y = xt$, $C_1 = V(t^2 - x - 1)$, which is smooth and meets $E_1 = V(x)$ transversally at the two points $t = \pm 1$. So $n = 1$, $N_1 = 2$ and $k_1 = 1$, with ratio $(k_1 + 1)/N_1 = 1$. For the reducible curve $C' = V(xy)$, the two components are smooth and meet transversally, $C'$ has simple normal crossings, and the minimal log resolution is the identity. The two curves have isomorphic completed local rings at the origin, but only $C'$ has simple normal crossings; this is the difference between normal crossings and simple normal crossings, which in Definition P5.6.12 asks the components themselves to be smooth.

**Example P8.4.13 (the tacnode).** Let $\operatorname{char} k \neq 2$ and $C = V(y^2 - x^4) = V(y - x^2) \cup V(y + x^2)$, two smooth branches tangent at the origin with $(V(y - x^2) \cdot V(y + x^2))_0 = 2$. Here $q_1 = 0$, with $m_{q_1}(C) = 2$. In the chart $y = xt$, $\pi_1^*(y^2 - x^4) = x^2 (t^2 - x^2)$, so $C_1 = V(t - x) \cup V(t + x)$ consists of two lines through $q_2 = (0, 0)$, which also lies on $E_1 = V(x)$. The three curves have distinct tangents, so $D_1$ is not snc at $q_2$, and $m_{q_2}(C_1) = 2$. After the second blow-up the two branches and $F_1$ meet $E_2$ at three distinct points, transversally, and the process stops with $n = 2$. Proposition P8.4.9 gives $N_1 = 2$, $N_2 = 2 + 2 = 4$, $k_1 = 1$, $k_2 = 1 + 1 = 2$, so
$$\pi^* C = C_2 + 2F_1 + 4F_2, \qquad K_{S_2} = \pi^* K_S + F_1 + 2F_2, \qquad F_1^2 = -2, \quad F_2^2 = -1 .$$
This is the configuration of the two tangent conics of Example P5.6.20, as it must be, since only the contact order of the branches enters. The ratios $(k_i + 1)/N_i$ are $1$ and $3/4$, so the log canonical threshold of the tacnode is $3/4$, smaller than the $5/6$ of the cusp: in the sense of Volume 4 the tacnode is the worse singularity.

**Example P8.4.14 (an ordinary $m$-fold point).** Let $C$ be the union of $m \geq 3$ lines through the origin of $\mathbb{A}^2$ with distinct directions. The origin is not snc, since at least three components pass through it. One blow-up separates the lines: their strict transforms meet $E_1$ at the $m$ distinct points of $E_1$ that correspond to their directions, transversally, and do not meet each other. So $n = 1$, $N_1 = m$, $k_1 = 1$ and the ratio is $2/m$. For $m = 2$ the curve is already snc and the minimal log resolution is the identity, although one blow-up also gives a log resolution, with ratio $2/2 = 1$.

### Proof

*Proposition P8.4.9.* Induction on $n$, the case $n = 0$ being empty. Each $F_j^{(i)}$ is smooth: $E_j \cong \mathbb{P}^1$ by Theorem P5.6.2, and the strict transform of a smooth curve under a point blow-up is isomorphic to it by part 5 of Proposition P5.6.4. So $m_q(F_j^{(i)}) = 1$ if $q \in F_j^{(i)}$ and $0$ otherwise. Suppose that on $S_{i-1}$ the total transform of $C$ is $C_{i-1} + \sum_{j < i} N_j F_j^{(i-1)}$ and $K_{S_{i-1}} = \pi_{\leq i-1}^* K_S + \sum_{j < i} k_j F_j^{(i-1)}$, where $\pi_{\leq i - 1} \colon S_{i-1} \to S$. Apply $\pi_i^*$, using part 2 of Proposition P5.6.4, $\pi_i^* D = \tilde D + m_{q_i}(D) E_i$, for $D = C_{i-1}$ and for $D = F_j^{(i-1)}$:
$$\pi_i^* \Bigl( C_{i-1} + \sum_{j < i} N_j F_j^{(i-1)} \Bigr) = C_i + \sum_{j < i} N_j F_j^{(i)} + \Bigl( m_{q_i}(C_{i-1}) + \sum_{j < i, \ q_i \in F_j} N_j \Bigr) E_i ,$$
and the coefficient of $E_i = F_i^{(i)}$ is $N_i$. For the canonical class, $K_{S_i} = \pi_i^* K_{S_{i-1}} + E_i$ by part 3 of Corollary P5.7.5, so
$$K_{S_i} = \pi_{\leq i}^* K_S + \sum_{j < i} k_j F_j^{(i)} + \Bigl( 1 + \sum_{j < i, \ q_i \in F_j} k_j \Bigr) E_i ,$$
with coefficient $k_i$ of $E_i$. Later blow-ups are at points, so they replace each $F_j^{(i)}$ by $F_j^{(i+1)}$ plus a multiple of $E_{i+1}$ and do not change the coefficients already computed. This proves parts 1 and 2. For part 3, $E_j^2 = -1$ on $S_j$ by Theorem P5.6.3, and by part 4 of Proposition P5.6.4 the self-intersection of the strict transform drops by $m_{q_i}(F_j^{(i-1)})^2$, which is $1$ when $q_i \in F_j$ and $0$ otherwise; $F_j \cong E_j \cong \mathbb{P}^1$.

*Theorem P8.4.10.* Write $\pi_i \colon S_i \to S$ for the composite of the first $i$ blow-ups. Every centre $q_i$ lies on $D_{i-1}$, so $\operatorname{Exc}(\pi_i) \subseteq D_i$ and $D_i = \pi_i^{-1}(C) \cup \operatorname{Exc}(\pi_i)$.

Let $W \subseteq S$ be the open set of points at which $C_{\mathrm{red}}$ has simple normal crossings. By induction on $i$, $\pi_i$ is an isomorphism over $W$: if this holds for $i$, then $D_i \cap \pi_i^{-1}(W) \cong C_{\mathrm{red}} \cap W$ has simple normal crossings, so $q_{i+1} \notin \pi_i^{-1}(W)$, and the blow-up of $q_{i+1}$ is an isomorphism over $\pi_i^{-1}(W)$.

Let $\pi' \colon S' \to S$ be a log resolution of $(S, C)$, and suppose that the process has run for $i$ steps and that $\pi' = \pi_i \circ h_i$ for a birational morphism $h_i \colon S' \to S_i$. Assume that $D_i$ is not snc at $q = q_{i+1}$. If the rational map $h_i^{-1}$ were defined near $q$, given by a morphism $u$ on a neighbourhood $U$ of $q$, then $h_i \circ u$ would be the identity of $U$ and $u \circ h_i$ would be the identity on a dense open subset of $h_i^{-1}(U)$, hence on $h_i^{-1}(U)$, because $S'$ is reduced and separated. So $h_i$ would be an isomorphism over $U$. Then $h_i^{-1}(D_i \cap U) = (\pi'^{-1}(C) \cup \operatorname{Exc}(\pi')) \cap h_i^{-1}(U)$, because $h_i$ has no exceptional curves over $U$, and this curve has simple normal crossings, while its image $D_i \cap U$ under the isomorphism $h_i$ does not. This is a contradiction, so $h_i^{-1}$ is not defined at $q$, and by Proposition P5.7.11 $h_i = \beta \circ h_{i+1}$ for the blow-up $\beta \colon S_{i+1} \to S_i$ of $q$ and a morphism $h_{i+1} \colon S' \to S_{i+1}$, which is birational. So $\pi' = \pi_{i+1} \circ h_{i+1}$.

There is a log resolution: by Theorem P5.6.17 there is a sequence of blow-ups $\pi'$ with centres over the singular points of $C_{\mathrm{red}}$ for which the support of $\pi'^* C$ has simple normal crossings, and since every centre lies on the preimage of $C$, $\operatorname{Exc}(\pi') \subseteq \pi'^{-1}(C)$. By the last paragraph, as long as the process runs, $\pi'$ factors through $S_i$, and by part 2 of Theorem P5.7.12, $\rho(S') = \rho(S_i) + \#\{ \text{curves contracted by } h_i \} \geq \rho(S) + i$. So the process stops after at most $\rho(S') - \rho(S)$ steps, at $S_n$ with $D_n$ snc. Then $\pi = \pi_n$ is a log resolution, since $D_n = \pi^{-1}(C) \cup \operatorname{Exc}(\pi)$, and it is an isomorphism over $W$. This proves part 1.

For part 2, the induction above, applied until the process stops, gives $\pi' = \pi \circ h$ with $h = h_n$, and $h$ is a composite of point blow-ups by part 1 of Theorem P5.7.12. Two morphisms $h, h'$ with $\pi \circ h = \pi \circ h'$ agree on the dense open set where $\pi$ is an isomorphism, hence everywhere, because $S'$ is reduced and $S_n$ is separated.

For part 3, let $\pi^\flat \colon S^\flat \to S$ be the result of another run of the process. Both are log resolutions, so by part 2 $\pi^\flat = \pi \circ h$ and $\pi = \pi^\flat \circ h^\flat$. Then $\pi \circ (h \circ h^\flat) = \pi$, so $h \circ h^\flat$ is the identity by the uniqueness in part 2, and likewise $h^\flat \circ h$; so $h$ is an isomorphism over $S$, unique by part 2. For every log resolution $\pi'$, part 2 and Theorem P5.7.12 give $\rho(S') \geq \rho(S_n) = \rho(S) + n$, and the number of blow-ups in $\pi'$ is $\rho(S') - \rho(S)$.

### Exercises

1. (A) Let $C = V(y^2 - x^5)$. Show that the minimal log resolution has four blow-ups, with $N = (2, 4, 5, 10)$ and $k = (1, 2, 3, 6)$, and that the smallest ratio $(k_i + 1)/N_i$ is $7/10$.
2. (A) Let $C$ be the union of two smooth curves through a point $p$ with contact order $r \geq 1$, that is, $(C_1 \cdot C_2)_p = r$. Show that the minimal log resolution blows up $r$ points over $p$ when $r \geq 2$, with $N_i = 2i$ and $k_i = i$, and that the smallest ratio is $(r + 1)/(2r)$.
3. (B) Let $a, b \geq 2$ be coprime and $C = V(y^a - x^b)$. Show that the last exceptional curve of the minimal log resolution has $N = ab$ and $k = a + b - 1$, and that its ratio $(k + 1)/N = 1/a + 1/b$ is the smallest one.
4. (B) In Proposition P8.4.9, show that the intersection matrix $(F_i \cdot F_j)$ has determinant $(-1)^n$, using the orthogonal decomposition of part 2 of Theorem P5.7.12.
5. (B) Show that the minimal log resolution of $(S, C)$ and the shortest sequence of blow-ups after which the strict transform of $C$ is smooth (Theorem P5.6.15) differ for the cusp, and agree for an ordinary $m$-fold point with $m \geq 3$.
6. (C) Show that the dual graph of the exceptional curves of any sequence of point blow-ups over one point is a tree, and that in the minimal log resolution of an integral curve germ the last exceptional curve meets exactly three other components of $D_n$ when the curve is singular.

### Lean

Blow-ups of points, strict transforms and the minimal log resolution are not in Lean. The predicate `MinimalModel.IsSncAt` of Section 5.1 is the condition on $D_n$.

### Notes and history

Infinitely near points and the rule $N_i = m_{q_i}(C_{i-1}) + \sum N_j$, under the name of the proximity relations, go back to Max Noether and to Enriques and Chisini; the point $q_i$ is *proximate* to $q_j$ when $q_i \in F_j$. Zariski showed that for a branch of a plane curve over $\mathbb{C}$ the resolution graph and the numbers $N_i$ are determined by the Puiseux characteristic, and conversely. The numbers $N_i$ and $k_i$ of the minimal log resolution compute the log canonical threshold of Volume 4, and also the poles of Igusa's zeta function and the jumping numbers of multiplier ideals. Kollár, Section 1.4, and Hartshorne, Section V.3, treat embedded resolution of plane curves; the minimality statement is the two-dimensional case of the uniqueness questions discussed in Section 5.1.
