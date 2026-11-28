---
title: Log canonical pairs with a klt boundary
nodes: [MMDZBZY2BV, MMQ2K4RSHT]
sources: [KM98, Fuj11, Fuj17d]
reads_with: [KM98:2.35, KM98:3.7, Fuj11:1.1]
requires: [4.1, 4.2, 7.4, 7.5]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Log canonical pairs with a klt boundary

### Statement

The cone and contraction theorems of Chapters 4 and 5 assume that $(X, \Delta)$ is klt. Many lc pairs are close to klt ones: if $X$ carries some klt boundary $\Delta_0$, a small move from $\Delta$ towards $\Delta_0$ makes the pair klt and changes $K_X + \Delta$ by an arbitrarily small class. This section proves that both theorems survive the limit. It is the case of lc pairs that the methods of this volume reach without new vanishing theorems; Section 2 sketches the general case. Throughout, $X$ is a normal projective variety of dimension $d$ over a field of characteristic $0$, $\Delta$ is an effective $\mathbb{Q}$-divisor with $a (K_X + \Delta)$ Cartier, and $K_\Delta$ is the class of $K_X + \Delta$.

**Lemma 7.6.1 (discrepancies are affine in the boundary).** Let $\Delta_1$, $\Delta_2$ be effective $\mathbb{Q}$-divisors with $K_X + \Delta_1$ and $K_X + \Delta_2$ $\mathbb{Q}$-Cartier, and for rational $t \in [0, 1]$ put $\Delta_t' = (1 - t) \Delta_1 + t \Delta_2$. For every divisor $G$ over $X$,
$$a(G, X, \Delta_t') = (1 - t) \, a(G, X, \Delta_1) + t \, a(G, X, \Delta_2).$$
In particular, if $(X, \Delta_1)$ is lc and $(X, \Delta_2)$ is klt, then $(X, \Delta_t')$ is klt for every rational $t \in (0, 1]$.

Lean: not yet in Lean.

**Theorem 7.6.2 (cone and contraction theorems with a klt boundary).** Suppose $(X, \Delta)$ is lc and there is an effective $\mathbb{Q}$-divisor $\Delta_0$ such that $(X, \Delta_0)$ is klt. Let $H$ be ample.

1. For every $\varepsilon > 0$ there are finitely many $K_\Delta$-negative extremal rays $R_1, \ldots, R_m$ with $\overline{NE}(X) = \overline{NE}(X)_{K_\Delta + \varepsilon H \ge 0} + \sum_{i=1}^m R_i$.
2. The $K_\Delta$-negative extremal rays are countable, and $\overline{NE}(X) = \overline{NE}(X)_{K_\Delta \ge 0} + \sum_i R_i$.
3. Every $K_\Delta$-negative extremal ray is spanned by a rational curve $\Gamma$ with $0 < -K_\Delta \cdot \Gamma \le 2d$.
4. Every $K_\Delta$-negative extremal face $F$ has a contraction $\varphi_F \colon X \to Y$ with the properties 1 to 4 of Theorem 7.5.2.

Lean: not yet in Lean.

**Corollary 7.6.3 (lc pairs on klt varieties).** If $X$ is klt, in particular if $X$ is smooth, and $(X, \Delta)$ is lc, then the conclusions of Theorem 7.6.2 hold for $(X, \Delta)$. This applies to every pair $(X, \Delta)$ with $X$ smooth and $\Delta$ a reduced snc divisor.

Lean: not yet in Lean.

### Proof in words

Lemma 7.6.1 is linearity of pullback. For the theorem, move $\Delta$ a small step $t$ towards $\Delta_0$. The pair $(X, \Delta_t)$ is klt, and for $t$ small compared to $\varepsilon$ the difference $K_\Delta - K_{\Delta_t}$ is dominated by $\frac{\varepsilon}{2} H$. So every $(K_\Delta + \varepsilon H)$-negative class is $(K_{\Delta_t} + \frac{\varepsilon}{2} H)$-negative, and the cone theorem for the klt pair, with $\frac{\varepsilon}{2}$, gives part 1. Part 2 follows from part 1 exactly as for klt pairs. The curves of part 3 come from Kawamata's theorem for $(X, \Delta_t)$; their degrees against $-K_\Delta$ exceed $2d$ by at most an error that tends to $0$ with $t$, and since these degrees lie in the discrete set $\frac1a \mathbb{Z}$, a subsequence has degree at most $2d$. For part 4, a negative face of the lc pair is a negative face of $(X, \Delta_t)$ for small $t$, and the contraction theorem does not refer to the boundary.

### Examples

**Example 7.6.4 (a Hirzebruch surface with its negative section).** Let $X = \mathbb{F}_n$, $n \ge 1$, and $\Delta = C_-$, lc and not klt by Corollary 4.2.13, with the klt boundary $\Delta_0 = 0$. By adjunction $(K_X + C_-) \cdot C_- = -2$, and $(K_X + C_-) \cdot F = -2 + 1 = -1$. So both rays of $\overline{NE}(X) = \langle C_-, F \rangle$ are $K_\Delta$-negative and $-K_\Delta$ is ample, with lengths $2$ and $1$, within $2d = 4$. The contractions are the ruling $q$ and $\pi \colon \mathbb{F}_n \to \mathbb{P}(1, 1, n)$, and by Example 7.4.21,
$$K_X + C_- = \pi^* K_Y + \Bigl( 1 - \frac{n-2}{n} \Bigr) C_- = \pi^* K_Y + \frac2n C_-,$$
so $(Y, 0)$ is klt although $(X, C_-)$ is not, as in part 3 of Proposition 7.5.11, whose proof uses only that discrepancies increase.

**Example 7.6.5 (the cone over a plane cubic).** Let $E \subseteq \mathbb{P}^2$ be a smooth cubic and $X \subseteq \mathbb{P}^3$ the projective cone over $E$, with vertex $v$. Then $X$ is a normal cubic surface, $K_X = \mathcal{O}_X(-1)$ is Cartier, and $-K_X$ is ample. The blow-up $\mu \colon Y \to X$ of $v$ is the $\mathbb{P}^1$-bundle $\mathbb{P}(\mathcal{O} \oplus \mathcal{O}(1)|_E)$ over $E$, with exceptional curve $E_0 \cong E$ and $E_0^2 = -3$. Adjunction gives $(K_Y + E_0) \cdot E_0 = 2 g(E) - 2 = 0$, so $K_Y \cdot E_0 = 3$ and $K_Y = \mu^* K_X - E_0$: the discrepancy of $E_0$ is $-1$, and $X$ is lc and not klt. No boundary helps: for an effective $\Delta_0$ with $K_X + \Delta_0$ $\mathbb{Q}$-Cartier, $\Delta_0$ is $\mathbb{Q}$-Cartier since $K_X$ is, $\mu^* \Delta_0 = \mu^{-1}_* \Delta_0 + m E_0$ with $m \ge 0$, and $a(E_0, X, \Delta_0) = -1 - m \le -1$. So Theorem 7.6.2 does not apply to $(X, 0)$. Here the conclusion is still true and easy: $\rho(X) = \rho(Y) - 1 = 1$, the cone is the ray of a line $\ell$ through $v$, with $-K_X \cdot \ell = 1$, and its contraction is $X \to \operatorname{Spec} k$. The general statement for lc pairs is the theorem of Ambro and Fujino in Section 2.

**Example 7.6.6 (the bound in the limit).** Let $X = \mathbb{P}^2$, $\Delta = \ell_1 + \ell_2 + \ell_3$ three lines in general position, lc and not klt, $K_\Delta \equiv 0$, and $\Delta_0 = 0$. The perturbed pairs $\Delta_t = (1 - t) \Delta$ are klt, with $-K_{\Delta_t} \cdot \ell = 3 t$ on a line $\ell$, tending to $0 = -K_\Delta \cdot \ell$. There are no $K_\Delta$-negative rays, and Theorem 7.6.2 asserts nothing beyond $\overline{NE}(X) = \overline{NE}(X)_{K_\Delta \ge 0}$. With $\Delta = \ell_1 + \ell_2$ instead, $-K_\Delta \cdot \ell = 1$ and $-K_{\Delta_t} \cdot \ell = 1 + 2 t$, which decreases to the limit $1 \le 2d$, as in the proof of part 3.

### Proof

*Lemma 7.6.1.* Fix a proper birational morphism $f \colon X' \to X$ from a normal variety on which $G$ is a divisor, and $K_{X'}$ and $K_X$ defined by the same rational form, as in Definition 4.1.4. Define $\Delta_{1, X'}$ and $\Delta_{2, X'}$ by $K_{X'} + \Delta_{j, X'} = f^*(K_X + \Delta_j)$. Pullback of $\mathbb{Q}$-Cartier divisors is linear, so
$$f^*(K_X + \Delta_t') = (1 - t) f^*(K_X + \Delta_1) + t f^*(K_X + \Delta_2) = K_{X'} + (1 - t) \Delta_{1, X'} + t \Delta_{2, X'},$$
and taking $-\operatorname{mult}_G$ gives the formula. If $(X, \Delta_1)$ is lc and $(X, \Delta_2)$ is klt, then $a(G, X, \Delta_1) \ge -1$ and $a(G, X, \Delta_2) \ge b$ for all $G$, where $b = \operatorname{totaldiscrep}(X, \Delta_2) > -1$. For $t \in (0, 1]$ the formula gives $a(G, X, \Delta_t') \ge -(1 - t) + t b > -1$ uniformly in $G$, so $\operatorname{totaldiscrep}(X, \Delta_t') > -1$ and $(X, \Delta_t')$ is klt by Definition 4.2.1.

*Theorem 7.6.2.* For rational $t \in (0, 1]$ put $\Delta_t = (1 - t) \Delta + t \Delta_0$, klt by Lemma 7.6.1, and $D = \Delta_0 - \Delta$, a $\mathbb{Q}$-Cartier divisor because $K_X + \Delta$ and $K_X + \Delta_0$ are. Then $K_{\Delta_t} = K_\Delta + t D$.

*Part 1.* Given $\varepsilon > 0$, choose $t$ so small that $\frac{\varepsilon}{2} H - t D$ is ample, which is possible because the ample cone is open. Then
$$K_\Delta + \varepsilon H = \Bigl( K_{\Delta_t} + \frac{\varepsilon}{2} H \Bigr) + \Bigl( \frac{\varepsilon}{2} H - t D \Bigr),$$
so $(K_\Delta + \varepsilon H) \cdot z \ge (K_{\Delta_t} + \frac{\varepsilon}{2} H) \cdot z$ for $z \in \overline{NE}(X)$, and $\overline{NE}(X)_{K_{\Delta_t} + \frac{\varepsilon}{2} H \ge 0} \subseteq \overline{NE}(X)_{K_\Delta + \varepsilon H \ge 0}$. Part 1 of Theorem 7.4.6 for $(X, \Delta_t)$ and $\frac{\varepsilon}{2}$ gives finitely many extremal rays $R_i$ with $\overline{NE}(X) = \overline{NE}(X)_{K_{\Delta_t} + \frac{\varepsilon}{2} H \ge 0} + \sum_i R_i$. Discard the $R_i$ with $(K_\Delta + \varepsilon H) \cdot R_i \ge 0$, which lie in the convex cone $\overline{NE}(X)_{K_\Delta + \varepsilon H \ge 0}$. The remaining rays are extremal rays of $\overline{NE}(X)$ on which $K_\Delta + \varepsilon H$, hence $K_\Delta$, is negative.

*Part 2.* Part 1 implies that every $K_\Delta$-negative extremal ray is one of the finitely many rays of part 1 for some $\varepsilon = 1/j$, by the argument of Step 3 of the proof of Theorem 7.4.6, which uses only part 1 and the extremality of the ray. So they are countable. The decomposition follows from part 3 of Proposition P7.4.5 as in that step.

*Part 3.* Let $R$ be a $K_\Delta$-negative extremal ray with a generator $z$. For every small rational $t > 0$, $K_{\Delta_t} \cdot z = K_\Delta \cdot z + t D \cdot z < 0$, so $R$ is a $K_{\Delta_t}$-negative extremal ray, and Theorem 7.4.13 for the klt pair $(X, \Delta_t)$ gives a rational curve $\Gamma_t$ with $[\Gamma_t] = \lambda_t z$, $\lambda_t > 0$, and $\lambda_t (-K_{\Delta_t} \cdot z) \le 2d$. Hence
$$-K_\Delta \cdot \Gamma_t = \lambda_t (-K_\Delta \cdot z) \le 2d \, \frac{-K_\Delta \cdot z}{-K_\Delta \cdot z - t D \cdot z},$$
and the right side tends to $2d$ as $t \to 0$. Since $a (K_X + \Delta)$ is Cartier, $-K_\Delta \cdot \Gamma_t$ lies in $\frac1a \mathbb{Z}_{> 0}$, and for small $t$ it is at most $2d + 1$, so it takes only finitely many values. Choose a sequence $t_j \to 0$ along which it is constant, equal to $\beta$. Then $\beta \le 2d \, (-K_\Delta \cdot z) / (-K_\Delta \cdot z - t_j D \cdot z)$ for all $j$, so $\beta \le 2d$, and $\Gamma = \Gamma_{t_1}$ is the required curve.

*Part 4.* Let $F$ be a $K_\Delta$-negative extremal face and $\Sigma = \{ z \in F : H \cdot z = 1 \}$, compact by Corollary P7.3.14. Then $K_\Delta \le -\delta$ on $\Sigma$ for some $\delta > 0$, and $|D \cdot z| \le c$ on $\Sigma$, so for $t < \delta / c$ the class $K_{\Delta_t}$ is negative on $\Sigma$ and $F$ is a $K_{\Delta_t}$-negative extremal face. Theorem 7.5.2 for $(X, \Delta_t)$ gives $\varphi_F$, and its properties 1 to 4 do not mention the boundary.

*Corollary 7.6.3.* Take $\Delta_0 = 0$. A smooth variety is klt, and a reduced snc divisor $\Delta$ on smooth $X$ gives an lc pair by Corollary 4.2.13.

### Exercises

1. (A) Let $X = \mathbb{P}^2$ and $\Delta = \ell_1 + \ell_2$ for two distinct lines. Show that $(X, \Delta)$ is lc and not klt, and that the cone theorem of this section applies; compute the length of the ray.
2. (A) In Example 7.6.4, check that $-K_\Delta$ is ample and compute the threshold $r(H)$ for $H = C_- + (n + 1) F$.
3. (B) Show that the hypothesis of Theorem 7.6.2 holds when $X$ is $\mathbb{Q}$-factorial and $(X, \Delta)$ is dlt, by taking $\Delta_0 = (1 - t) \Delta$ for small $t$.
4. (B) In Example 7.6.5, compute $\operatorname{Pic}(X)$ and show that $X$ is not $\mathbb{Q}$-factorial, by exhibiting a Weil divisor $\ell - \ell'$, for lines $\ell, \ell'$ through $v$, with no Cartier multiple.
5. (B) Let $X$ be the cone over a smooth plane conic, $\mathbb{P}(1, 1, 2)$, and $\Delta = \ell$ a line through the vertex. Show that $(X, \ell)$ is lc, that $X$ is klt, and apply Corollary 7.6.3.
6. (B) Show that the conclusion of part 3 cannot be improved to $-K_\Delta \cdot \Gamma \le 2d - 1$ by perturbation alone: give an lc pair with a klt boundary and a negative ray of length exactly $2$ in dimension $1$.

### Lean

The library has `MinimalModel.ConeTheoremLc`, the cone theorem for lc pairs of Section 2, as a statement without proof; it implies parts 1 to 3 of Theorem 7.6.2. Lemma 7.6.1 and the perturbation argument are not yet in Lean.

### Notes and history

The perturbation argument is standard; in KM98 it is the reason that Theorem 3.7 is stated for klt pairs while most applications in Chapter 3 allow dlt pairs on $\mathbb{Q}$-factorial varieties. The integrality trick in part 3 is the one used by Fujino to pass length bounds to limits (Fuj11 and Fuj17d). Pairs like the cone over an elliptic curve, which carry no klt boundary, need the theory of Section 2.
