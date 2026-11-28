---
title: Injectivity theorems
nodes: []
sources: [EV92, Kol86a, Kol86b, Kol92, Fuj11, KM98, Laz04, Har77]
reads_with: [EV92:lecture-5, KM98:ch2, Fuj11:ch3]
requires: [P2.4, P4.4, P7.8, P7.9, 4.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Injectivity theorems

### Statement

Throughout the chapter $k$ is algebraically closed of characteristic $0$. A $\mathbb{Q}$-Cartier divisor $M$ on a projective variety is *semiample* if some multiple $mM$ is a Cartier divisor whose linear system has no base points. For an effective Cartier divisor $B$ with canonical section $s_B$, and a Weil divisor $N$ on a normal variety, multiplication by $s_B$ is the inclusion $\mathcal{O}_X(N) \subseteq \mathcal{O}_X(N + B)$ of reflexive sheaves, and it induces maps $H^i(X, \mathcal{O}_X(N)) \to H^i(X, \mathcal{O}_X(N + B))$. The injectivity theorems say when these maps are injective. The first is the analytic input, proved by Esnault and Viehweg from the degeneration of the logarithmic Hodge to de Rham spectral sequence on a cyclic cover; it is cited.

**Theorem 5.2.1 (Esnault-Viehweg injectivity, black box).** Let $X$ be a smooth projective variety, $L$ a line bundle and $D = \sum_j \nu_j D_j$ an effective divisor with snc support such that $L^m \cong \mathcal{O}_X(D)$ for an integer $m$ with $0 < \nu_j < m$ for every $j$. Let $B$ be an effective divisor with $\operatorname{Supp} B \subseteq \operatorname{Supp} D$. Then for every $i$ the map
$$H^i(X, \omega_X \otimes L) \to H^i(X, \omega_X \otimes L \otimes \mathcal{O}_X(B))$$
given by $s_B$ is injective.

Lean: not yet in Lean.

**Theorem 5.2.2 (injectivity for snc pairs).** Let $X$ be a smooth projective variety, $\Delta$ a $\mathbb{Q}$-divisor with coefficients in $[0, 1)$, $N$ a Cartier divisor and $M$ a semiample $\mathbb{Q}$-Cartier divisor with $N - (K_X + \Delta) \sim_\mathbb{Q} M$. Let $B$ be an effective Cartier divisor with $B \sim_\mathbb{Q} t M$ for a rational $t > 0$, such that $\operatorname{Supp}(\Delta + B)$ is snc. Then $H^i(X, \mathcal{O}_X(N)) \to H^i(X, \mathcal{O}_X(N + B))$ is injective for every $i$.

Lean: not yet in Lean.

**Theorem 5.2.3 (Kollár injectivity for klt pairs).** Let $X$ be a normal projective variety, $(X, \Delta)$ a klt pair, $N$ a $\mathbb{Q}$-Cartier Weil divisor and $M$ a semiample $\mathbb{Q}$-Cartier divisor with $N - (K_X + \Delta) \sim_\mathbb{Q} M$. Let $B$ be an effective Cartier divisor with $B \sim_\mathbb{Q} t M$ for a rational $t > 0$. Then $H^i(X, \mathcal{O}_X(N)) \to H^i(X, \mathcal{O}_X(N + B))$ is injective for every $i$.

Lean: not yet in Lean.

**Corollary 5.2.4 (Kollár's theorem).** Let $X$ be a smooth projective variety, $L$ a semiample line bundle and $s \in H^0(X, L^k)$ a nonzero section, $k \geq 1$. Then multiplication by $s$, $H^i(X, \omega_X \otimes L^l) \to H^i(X, \omega_X \otimes L^{l + k})$, is injective for every $l \geq 1$ and every $i$. This is Theorem P7.9.14.

Lean: not yet in Lean. The statement is `MinimalModel.KollarInjectivity`.

### Proof in words

Theorem 5.2.1 is used once, to prove the snc case. The class $M$ is split as a small multiple of $B$ plus the rest, which is still semiample, and the rest is replaced by a general member of a free linear system. Then $N - K_X$ is, up to $\mathbb{Q}$-linear equivalence, a $\mathbb{Q}$-divisor with snc support whose coefficients lie strictly between $0$ and $1$ and whose support contains $B$. Clearing denominators puts it in the form $L^m \cong \mathcal{O}_X(D)$ of Theorem 5.2.1.

For a klt pair, the resolution of Corollary 5.1.16 replaces $N$ by a Cartier divisor $N_Y$ on a log resolution, with an snc boundary $\Theta$ and with $N_Y - (K_Y + \Theta)$ the pullback of $M$. Pullbacks of semiample divisors are semiample, and the pullback of $B$ is still proportional to it. The higher direct images of $\mathcal{O}_Y(N_Y)$ and $\mathcal{O}_Y(N_Y + \mu^* B)$ vanish, and their push-forwards are $\mathcal{O}_X(N)$ and $\mathcal{O}_X(N + B)$, so the cohomology on $Y$ is the cohomology on $X$, compatibly with multiplication by $s_B$. Kollár's theorem is the case $\Delta = 0$, $N = K_X + lL$.

### Examples

**Example 5.2.5 (injectivity without vanishing).** Let $E$ be an elliptic curve, $X = E \times \mathbb{P}^1$ with projections $p_1$ and $p_2$, and $F = p_2^*[\text{pt}]$, a fibre of $p_2$. Then $K_X = p_2^* K_{\mathbb{P}^1} = -2F$, since $K_E = 0$, and $L = \mathcal{O}_X(F)$ is semiample and not big, so Kawamata-Viehweg vanishing does not apply to $\omega_X \otimes L^l$. By the Künneth formula,
$$H^1(X, \omega_X \otimes L^2) = H^1(X, \mathcal{O}_X) \cong k, \qquad H^1(X, \omega_X \otimes L^3) = H^1(E, \mathcal{O}_E) \otimes H^0(\mathbb{P}^1, \mathcal{O}(1)) \cong k^2,$$
and both are nonzero. For a nonzero $s \in H^0(X, L) = H^0(\mathbb{P}^1, \mathcal{O}(1))$, the map of Corollary 5.2.4 with $l = 2$, $k = 1$ is $H^1(E, \mathcal{O}_E) \otimes (H^0(\mathbb{P}^1, \mathcal{O}) \to H^0(\mathbb{P}^1, \mathcal{O}(1)))$, multiplication by $s$ on the second factor, which is injective.

**Example 5.2.6 (proportionality is needed).** Let $X = \mathbb{P}^1$, $\Delta = 0$, $N = K_X$ and $B$ a point. Then $N - K_X = 0$, so the only possible $M$ is $\mathbb{Q}$-linearly trivial, and no effective $B \neq 0$ satisfies $B \sim_\mathbb{Q} t M$. The conclusion fails: $H^1(\mathbb{P}^1, \mathcal{O}(-2)) \cong k$ maps to $H^1(\mathbb{P}^1, \mathcal{O}(-1)) = 0$.

**Example 5.2.7 (failure for a log canonical pair).** Let $\mu \colon X \to \mathbb{P}^2$ be the blow-up of a point $p$, $E$ the exceptional curve, $H = \mu^* \ell$, and $L'$ the strict transform of a line through $p$, so $H \sim L' + E$. Let $\Delta = E$, which is lc and not klt, $M = H$, semiample, $B = E + L' \in |H|$, so $B \sim M$ with $t = 1$, and $N = K_X + E + H = -2H + 2E$, using $K_X = -3H + E$. The support of $\Delta + B$ is $E + L'$, which is snc. By Example 5.1.17, $h^1(X, \mathcal{O}_X(N)) = 1$. The divisor $N + B = -H + 2E$ has $\mu_* \mathcal{O}_X(-H + 2E) = \mathcal{O}(-1)$, so $h^0(N + B) = 0$. Consider
$$0 \to \mathcal{O}_X(N) \to \mathcal{O}_X(N + B) \to \mathcal{O}_B(N + B) \to 0.$$
The line bundle $\mathcal{O}_B(-H + 2E)$ has degree $(-H + 2E) \cdot E = -2$ on $E$ and degree $(-H + 2E) \cdot L' = -1 + 2 = 1$ on $L'$, and $B$ is two smooth rational curves meeting transversally in one point. A section is a section of $\mathcal{O}_{\mathbb{P}^1}(1)$ on $L'$ and a section of $\mathcal{O}_{\mathbb{P}^1}(-2)$ on $E$, that is $0$, agreeing at the node; so $H^0(B, \mathcal{O}_B(N + B)) \cong k$. Since $H^0(X, \mathcal{O}_X(N + B)) = 0$, the connecting map embeds this $k$ into $H^1(X, \mathcal{O}_X(N)) \cong k$, so it is onto, and the map $H^1(X, \mathcal{O}_X(N)) \to H^1(X, \mathcal{O}_X(N + B))$ is zero. Injectivity fails, although every hypothesis of Theorem 5.2.2 holds except that $\Delta$ has a coefficient equal to $1$.

### Proof

*Theorem 5.2.1.* This is EV92, Lecture 5, Corollary 5.2, the case $\Omega^0$ of Theorem 5.1 there. The proof takes the cyclic cover obtained by extracting an $m$-th root of the section of $L^m$ with divisor $D$, decomposes the logarithmic de Rham complex of a resolution of it into eigensheaves, and uses the degeneration at $E_1$ of the logarithmic Hodge to de Rham spectral sequence (Deligne) to show that the restriction maps $H^i(X, \omega_X \otimes L) \to H^i(X, \omega_X \otimes L(B))$ are injective. The bound $0 < \nu_j < m$ makes $L^{-1}$ an eigensheaf whose logarithmic connection has residues in $(0, 1)$ along every $D_j$, and this is where the hypothesis $\operatorname{Supp} B \subseteq \operatorname{Supp} D$ enters.

*Theorem 5.2.2.* Choose a rational $\varepsilon$ with $0 < \varepsilon < 1/t$ such that $\Delta + \varepsilon B$ has every coefficient less than $1$; this is possible since $\Delta$ has coefficients less than $1$ and $B$ has finitely many components. Then $M \sim_\mathbb{Q} \varepsilon B + (1 - \varepsilon t) M$. Choose an integer $m \geq 2$ such that $m \Delta$ and $m \varepsilon B$ are integral, $m(1 - \varepsilon t) M$ is a Cartier divisor with a free linear system, and the $\mathbb{Q}$-linear equivalences become linear equivalences after multiplying by $m$:
$$m(N - K_X - \Delta) \sim m M \sim m \varepsilon B + m(1 - \varepsilon t) M.$$
Let $G$ be a general member of $|m(1 - \varepsilon t) M|$. By Lemma P7.8.8, applied to the reduced snc divisor $\operatorname{Supp}(\Delta + B)$, $G$ is smooth and reduced, it has no component in common with $\Delta + B$, and $\operatorname{Supp}(\Delta + B) + G$ is snc. Put $L = \mathcal{O}_X(N - K_X)$ and
$$D = m \Delta + m \varepsilon B + G.$$
Then $L^m \cong \mathcal{O}_X(D)$, $D$ is effective with snc support, its coefficients are $m(a + \varepsilon b)$ along the components of $\Delta + B$, where $a$ and $b$ are the coefficients of $\Delta$ and $B$ with $0 < a + \varepsilon b < 1$, and $1$ along the components of $G$, with $1 < m$. So $0 < \nu_j < m$ for every component. Since $\varepsilon > 0$, $\operatorname{Supp} B \subseteq \operatorname{Supp} D$. Theorem 5.2.1 gives the injectivity of $H^i(X, \omega_X \otimes L) \to H^i(X, \omega_X \otimes L(B))$, and $\omega_X \otimes L = \mathcal{O}_X(N)$.

*Theorem 5.2.3.* Choose a rational $\lambda$ with $\operatorname{Supp}(\Delta + B + \lambda N) = \operatorname{Supp} \Delta \cup \operatorname{Supp} B \cup \operatorname{Supp} N$, and let $\mu \colon Y \to X$ be a projective log resolution of $(X, \Delta + B + \lambda N)$. It is also a log resolution of $(X, \Delta + \lambda' N)$ for a rational $\lambda'$ with $\operatorname{Supp}(\Delta + \lambda' N) = \operatorname{Supp} \Delta \cup \operatorname{Supp} N$, since $\operatorname{Exc}(\mu) + \mu^{-1}_* \operatorname{Supp}(\Delta + \lambda' N)$ is part of an snc divisor. Let $N_Y$ and $\Theta$ be as in Corollary 5.1.16. By its parts 1 and 2, $\Theta$ has snc support and coefficients in $[0, 1)$, and $N_Y - (K_Y + \Theta) = \mu^*(N - K_X - \Delta) \sim_\mathbb{Q} \mu^* M$, which is semiample. The divisor $\mu^* B$ is effective and Cartier, $\mu^* B \sim_\mathbb{Q} t \mu^* M$, and $\operatorname{Supp}(\Theta + \mu^* B)$ lies in $\operatorname{Exc}(\mu) \cup \mu^{-1}(\operatorname{Supp}(\Delta + B + \lambda N))$, which is an snc divisor. So Theorem 5.2.2 gives the injectivity of
$$H^i(Y, \mathcal{O}_Y(N_Y)) \to H^i(Y, \mathcal{O}_Y(N_Y + \mu^* B)).$$
By Corollary 5.1.16, parts 3 and 4, $\mu_*$ of the map $\mathcal{O}_Y(N_Y) \to \mathcal{O}_Y(N_Y + \mu^* B)$, which is multiplication by $\mu^* s_B$, is the map $\mathcal{O}_X(N) \to \mathcal{O}_X(N + B)$ given by $s_B$, and both sheaves have no higher direct images. By Corollary P2.4.27, part 1, and the naturality of the Leray spectral sequence in the sheaf, the square formed by the two maps on cohomology and the isomorphisms $H^i(X, \mu_* \mathcal{F}) \cong H^i(Y, \mathcal{F})$ commutes. So the map on $X$ is injective.

*Corollary 5.2.4.* Let $X$ be smooth projective, $\Delta = 0$, $N = K_X + lL$, $M = lL$, which is semiample, and $B = \operatorname{div}(s)$, effective Cartier with $B \sim kL = \frac{k}{l} M$. The pair $(X, 0)$ is klt, and Theorem 5.2.3 gives the injectivity of $H^i(X, \mathcal{O}_X(K_X + lL)) \to H^i(X, \mathcal{O}_X(K_X + (l + k) L))$, which is multiplication by $s$.

### Exercises

1. (A) In Example 5.2.5, compute $H^2(X, \omega_X \otimes L^l)$ for every $l \geq 1$ and check Corollary 5.2.4 for $i = 2$.
2. (A) Prove Corollary 5.2.4 for $i = \dim X$ directly: by Serre duality the dual of the map is multiplication by $s$, $H^0(X, L^{-l-k}) \to H^0(X, L^{-l})$. Show that both groups vanish for a semiample $L$ unless $L$ is trivial, and that in the trivial case $s$ is a nonzero constant.
3. (B) Let $X = \mathbb{P}^1$, $P$ a point, $N = K_X + aP$ with $a \geq 0$, $M = aP$ and $B = bP$ with $b \geq 1$. Show that the hypotheses of Theorem 5.2.2 hold if and only if $a > 0$, and verify the conclusion directly from Theorem P4.2.1 in that case. For $a = 0$ compare with Example 5.2.6.
4. (B) Let $f \colon X \to C$ be a surjective morphism from a smooth projective surface to a smooth curve. Use Corollary 5.2.4 with $L = f^* \mathcal{O}_C(P)$ to show that $H^1(X, \omega_X \otimes L^l) \to H^1(X, \omega_X \otimes L^{l+1})$ is injective for $l \geq 1$, and deduce that $h^1(X, \omega_X \otimes L^l)$ is non-decreasing in $l$.
5. (B) In Example 5.2.7, replace $\Delta = E$ by $\Delta = (1 - \varepsilon) E$ with $0 < \varepsilon < 1$ rational. Show that no Cartier divisor $N$ satisfies $N - (K_X + \Delta) \sim_\mathbb{Q} H$, and that for $N = -2H + 2E$ the class $N - (K_X + \Delta) = H + \varepsilon E$ is not nef, so not semiample. Conclude that Theorem 5.2.2 says nothing about this $N$.
6. (C) Prove Theorem 5.2.2 when $M$ is semiample and $B \in |kM_0|$ for a free Cartier divisor $M_0$ with $M \sim_\mathbb{Q} M_0$, $k \geq 1$, without the assumption that $\operatorname{Supp}(\Delta + B)$ is snc, by passing to a log resolution of $(X, \Delta + B)$ and using Lemma P7.10.3 for the push-forward.

### Lean

`MinimalModel.KollarInjectivity` in the project library is the statement of Corollary 5.2.4, after Kollár, Theorem 2.2, in the form of Fujino, stated without proof. Theorems 5.2.1 to 5.2.3 are not in the library, and there is no Hodge theory or de Rham cohomology of varieties to prove Theorem 5.2.1.

### Notes and history

Kollár proved the injectivity theorem for $\omega_X \otimes L^l$ with $L$ semiample in Kol86a, Theorem 2.2, by Hodge theory on a resolution of the cyclic cover, and deduced the torsion freeness and vanishing of Section 2. Esnault and Viehweg generalized it to the logarithmic form of Theorem 5.2.1 (EV92, Lecture 5), which is the form that passes to pairs. The version for klt pairs and $\mathbb{Q}$-divisors is in Kol92 and in the survey Kol97; Fujino (Fuj11, Section 3) extends injectivity to log canonical pairs under the hypothesis that $B$ contains no lc centre, which is exactly what fails in Example 5.2.7, where $B$ contains the lc centre $E$. Volume P7 uses Corollary 5.2.4 as a black box; the proof above derives it from Theorem 5.2.1 and Chapter 1.
