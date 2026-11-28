---
title: "Corollaries: log canonical models, flips and Q-factorializations"
nodes: [MMP51FQ005]
sources: [BCHM10, KM98, Cor07, Kol13]
reads_with: [BCHM10:1.4, KM98:6.1]
requires: [1.5, 4.2, 7.2, 8.1]
level: advanced
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Corollaries: log canonical models, flips and Q-factorializations

### Statement

**Corollary 9.5.14 (log canonical models).** Let $(X, \Delta)$ be a projective klt pair with $\Delta$ a $\mathbb{Q}$-divisor and $K_X + \Delta$ big. Then $X_{\mathrm{can}} = \operatorname{Proj} R(X, K_X + \Delta)$ is a normal projective variety, the induced map $\psi \colon X \dashrightarrow X_{\mathrm{can}}$ is birational, and $K_{X_{\mathrm{can}}} + \psi_* \Delta$ is an ample $\mathbb{Q}$-Cartier divisor; $\psi$ is the ample model of $K_X + \Delta$ in the sense of Definition 9.4.3 of Chapter 4, and it is unique up to a unique isomorphism.

Lean: not yet in Lean.

**Corollary 9.5.15 (existence of klt flips, BCHM Corollary 1.4.1).** Let $(X, \Delta)$ be a klt pair and $f \colon X \to Z$ a flipping contraction: $f$ is a small projective birational morphism with relative Picard number $1$ and $-(K_X + \Delta)$ is $f$-ample. Then the flip $f^+ \colon X^+ \to Z$ of $f$ exists, and
$$X^+ = \operatorname{\mathbf{Proj}}_Z \bigoplus_{m \ge 0} f_* \mathcal{O}_X(\lfloor m(K_X + \Delta) \rfloor).$$

Node: MMP51FQ005 · Lean: `MinimalModel.KltFlips`

**Corollary 9.5.16 ($\mathbb{Q}$-factorializations).** Let $(X, \Delta)$ be a klt pair with $X$ quasi-projective. Then there is a small projective birational morphism $h \colon X' \to X$ with $X'$ $\mathbb{Q}$-factorial and $K_{X'} + h^{-1}_* \Delta = h^*(K_X + \Delta)$; in particular $(X', h^{-1}_* \Delta)$ is klt.

Lean: not yet in Lean.

### Proof in words

All three corollaries are read off Theorem 9.5.3. The log canonical model is the $\operatorname{Proj}$ of a finitely generated ring, and Theorem 9.5.4 already identified it with the semiample fibration on a log terminal model. A flipping contraction is birational, so every divisor is big over $Z$, and the relative log canonical ring over the affine pieces of $Z$ is finitely generated; by Theorem 8.1.6 of Volume 8, finite generation is exactly what produces the flip.

For a $\mathbb{Q}$-factorialization, take a log resolution and put coefficient $1 - \varepsilon$ on every exceptional divisor. The log canonical divisor is then, over $X$, an effective divisor whose support is the whole exceptional locus. Its log terminal model over $X$ is $\mathbb{Q}$-factorial, and the negativity lemma forces the pushforward of that effective exceptional divisor to vanish, so every exceptional divisor of the resolution is contracted and the model is small over $X$.

### Examples

**Example 9.5.17 (the cone over a quadric surface).** Let $Q \subseteq \mathbb{P}^3$ be a smooth quadric surface, $Q \cong \mathbb{P}^1 \times \mathbb{P}^1$, and let $X \subseteq \mathbb{P}^4$ be the projective cone over $Q$, with vertex $v$; locally at $v$ it is the affine 3-fold $xy = zw$. The blow-up $g \colon W \to X$ of $v$ is the $\mathbb{P}^1$-bundle $\mathbb{P}_Q(\mathcal{O} \oplus \mathcal{O}(1))$, smooth, with exceptional divisor $E \cong Q$ and $\mathcal{O}_E(E) = \mathcal{O}_Q(-1, -1)$; so $g$ is a log resolution of $(X, 0)$. By adjunction $(K_W + E)|_E = K_Q = \mathcal{O}_Q(-2, -2)$, so $K_W|_E = \mathcal{O}_Q(-1, -1)$; writing $K_W = g^* K_X + aE$ and restricting to $E$ gives $a = 1$. So $X$ has a terminal singularity at $v$.

Follow the proof of Corollary 9.5.16 with $\Delta = 0$ and $0 < \varepsilon < 2$: $\Delta_W = (1 - \varepsilon) E$ and $K_W + \Delta_W = g^* K_X + (2 - \varepsilon) E$. The curves contracted by $g$ lie in $E$, and $\overline{NE}(W/X)$ is spanned by the classes of the two rulings $\ell_1$, $\ell_2$ of $E$, with $E \cdot \ell_i = -1$. So $(K_W + \Delta_W) \cdot \ell_i = -(2 - \varepsilon) < 0$ for both rulings, both rays are negative, and the program over $X$ contracts one of them. Contracting $\ell_1$ blows $E$ down onto a curve $C \cong \mathbb{P}^1$: this is a smooth 3-fold $X_1'$ with $W$ the blow-up of $X_1'$ along $C$, and $h_1 \colon X_1' \to X$ is small, with exceptional locus $C$. On $X_1'$ the divisor $\psi_*((2 - \varepsilon) E)$ is zero, as the proof predicts, and $K_{X_1'} = h_1^* K_X$. Contracting $\ell_2$ instead gives the second small resolution $X_2'$. The two are the two $\mathbb{Q}$-factorializations of $X$, and $X_1' \dashrightarrow X_2'$ is the Atiyah flop. The variety $X$ itself is not $\mathbb{Q}$-factorial: a plane $\Pi \subseteq X$ through $v$, the cone over a line of the ruling $\ell_2$, has strict transform $\Pi'$ on $X_1'$ with $\Pi' \cdot C \ne 0$, while if $m\Pi$ were Cartier then $h_1^*(m \Pi) = m \Pi'$, because $h_1$ is small, would have degree $0$ on the contracted curve $C$.

**Example 9.5.18 (the canonical model of a blown-up quintic).** In Example 9.5.11 of the previous section, $S$ is a smooth quintic surface blown up at a point, and $R(S, K_S) \cong k[x_0, \ldots, x_3]/(f)$. By Corollary 9.5.14 with $\Delta = 0$, the canonical model is $\operatorname{Proj} R(S, K_S) = S_0 \subseteq \mathbb{P}^3$, and the map $\psi$ is the blow-down of the $(-1)$-curve: the program contracts the negative part $E$ of the Zariski decomposition, and $K_{S_0} = \mathcal{O}_{S_0}(1)$ is ample.

### Proof

*Proof of Corollary 9.5.14.* By Theorem 9.5.4, $R = R(X, K_X + \Delta)$ is finitely generated and $\operatorname{Proj} R$ is the target $Z$ of the semiample fibration $Y \to Z$ of $K_Y + \Gamma$ on a log terminal model $\varphi \colon X \dashrightarrow Y$. Since $K_Y + \Gamma$ is big, $Y \to Z$ is birational, so $\psi \colon X \dashrightarrow Z$ is birational. $Z$ is normal as the $\operatorname{Proj}$ of a Veronese subring of $R(Y, b r (K_Y + \Gamma))$, which is a normal domain, being the section ring of a divisor on a normal variety. With $br(K_Y + \Gamma) = \mu^* H$ for the semiample fibration $\mu \colon Y \to Z$ and $H$ very ample, $\mu_*(K_Y + \Gamma) = K_Z + \psi_* \Delta$ and $br(K_Z + \psi_*\Delta) = H$, so $K_Z + \psi_* \Delta$ is an ample $\mathbb{Q}$-Cartier divisor. For the ample model property, let $p \colon W \to X$ and $q \colon W \to Y$ be a common resolution and $q' = \mu \circ q$. By Lemma 9.4.4 for $\varphi$, $p^*(K_X + \Delta) = q'^*(\tfrac{1}{br} H) + E$ with $E \ge 0$ and $q$-exceptional, hence $q'$-exceptional. For $m$ divisible enough, Lemma 7.1.6, part 2, applied to $q'$ shows that every section of $m p^*(K_X + \Delta)$ is the pullback of a section of $\frac{m}{br} H$ times the canonical section of $\mathcal{O}_W(mE)$, so every effective $\mathbb{Q}$-divisor $B \sim_{\mathbb{Q}} p^*(K_X + \Delta)$ satisfies $B \ge E$. The same inequality for effective $B \sim_{\mathbb{R}} p^*(K_X + \Delta)$ follows by the rationality argument of BCHM, Section 3.6, and is cited. Uniqueness holds because $Z$ is determined by the ring $R$. $\square$

*Proof of Corollary 9.5.15.* The question is local on $Z$: by part 2 of Theorem 8.1.6, a flip over an open subset of $Z$ is unique up to unique isomorphism, so flips over the members of an affine open cover glue. Assume $Z = \operatorname{Spec} A$ affine. First suppose $\Delta$ is a $\mathbb{Q}$-divisor. Since $f$ is birational, $K_X + \Delta$ is $f$-big, and Theorem 9.5.3, part 3, with $\pi = f$ shows that $R(X/Z, K_X + \Delta) = \bigoplus_m H^0(X, \mathcal{O}_X(\lfloor m(K_X + \Delta) \rfloor))$ is a finitely generated $A$-algebra. Let $r \ge 1$ with $r \Delta$ integral and $D = r(K_X + \Delta)$, an integral Weil divisor. Then $R(X/Z, D)$ is the $r$-th Veronese subring of $R(X/Z, K_X + \Delta)$, which is finitely generated by part 2 of Lemma 8.1.5. By part 1 of Theorem 8.1.6, $X^+ = \operatorname{\mathbf{Proj}}_Z R(X/Z, D)$ is normal, $f^+ \colon X^+ \to Z$ is small and projective, and the strict transform $D^+ = r(K_{X^+} + \Delta^+)$ is $\mathbb{Q}$-Cartier and ample over $Z$, where $\Delta^+$ is the strict transform of $\Delta$. This is the flip, and $\operatorname{\mathbf{Proj}}$ is unchanged by passing to the Veronese subring, which gives the displayed formula.

If $\Delta$ has real coefficients, let $R$ be the extremal ray contracted by $f$. The klt condition is open in the coefficients by Theorem 4.2.14 and $(K_X + \Delta) \cdot R < 0$ is an open condition, so there is a $\mathbb{Q}$-divisor $\Delta'$ with the same support, $(X, \Delta')$ klt and $(K_X + \Delta') \cdot R < 0$. Since $\rho(X/Z) = 1$, the divisors $K_X + \Delta$ and $K_X + \Delta'$ are positive multiples of each other in $N^1(X/Z)$, so a small modification over $Z$ on which one strict transform is ample over $Z$ has the other ample over $Z$ as well. The flip of $(X, \Delta')$ is therefore the flip of $(X, \Delta)$. $\square$

*Proof of Corollary 9.5.16.* Let $g \colon W \to X$ be a log resolution of $(X, \Delta)$, which exists by Theorem 4.2.10 and may be taken projective, with exceptional prime divisors $E_1, \ldots, E_k$; by Definition 4.2.9 the exceptional set is the divisor $E_1 \cup \cdots \cup E_k$. Write $K_W = g^*(K_X + \Delta) - g^{-1}_* \Delta + \sum_i a_i E_i$ with $a_i = a(E_i, X, \Delta) > -1$, since $(X, \Delta)$ is klt. Fix $\varepsilon$ with $0 < \varepsilon < \min_i (1 + a_i)$ and $\varepsilon < 1$, and put
$$\Delta_W = g^{-1}_* \Delta + (1 - \varepsilon) \sum_i E_i, \qquad F = \sum_i (1 + a_i - \varepsilon) E_i.$$
Then $(W, \Delta_W)$ is klt, since $\operatorname{Supp} \Delta_W$ has simple normal crossings and all coefficients are less than $1$, and $K_W + \Delta_W = g^*(K_X + \Delta) + F$ with $F$ effective, $g$-exceptional and with support exactly $\operatorname{Exc}(g)$. Since $g$ is birational, $K_W + \Delta_W$ is $g$-big, so Theorem 9.5.3, part 1, with $\pi = g$, gives a log terminal model $\psi \colon W \dashrightarrow X'$ over $X$, with $h \colon X' \to X$ projective, $X'$ $\mathbb{Q}$-factorial, and $K_{X'} + \Delta' = \psi_*(K_W + \Delta_W)$ nef over $X$, where $\Delta' = \psi_* \Delta_W$.

Since $\psi$ is a birational contraction over $X$, $\psi_* g^*(K_X + \Delta) = h^*(K_X + \Delta)$: on a common resolution $p \colon V \to W$, $q \colon V \to X'$ one has $g \circ p = h \circ q$, so $\psi_* g^* = q_* p^* g^* = q_* q^* h^* = h^*$. Hence
$$K_{X'} + \Delta' = h^*(K_X + \Delta) + \psi_* F.$$
The divisor $\psi_* F$ is effective and $h$-exceptional, and it is $h$-nef because it differs from $K_{X'} + \Delta'$ by a pullback from $X$. Apply the negativity lemma, Theorem 1.5.22, to $h$ and $B = -\psi_* F$: $-B = \psi_* F$ is $h$-nef and $h_* B = 0 \ge 0$, so $B \ge 0$, that is $\psi_* F \le 0$. With $\psi_* F \ge 0$ this gives $\psi_* F = 0$. Every $E_i$ has positive coefficient in $F$, so every $E_i$ is contracted by $\psi$. An $h$-exceptional prime divisor of $X'$ would be the strict transform of a $g$-exceptional prime divisor of $W$, since $\psi^{-1}$ contracts no divisor; so $h$ has no exceptional divisors and is small. Then $\Delta' = h^{-1}_* \Delta$, and $K_{X'} + h^{-1}_* \Delta = h^*(K_X + \Delta)$, so $(X', h^{-1}_* \Delta)$ is klt because it has the same discrepancies as $(X, \Delta)$. $\square$

### Exercises

1. (B) Let $X$ be the cone over the Veronese surface $v_2(\mathbb{P}^2) \subseteq \mathbb{P}^5$. Compute the discrepancy of the exceptional divisor of the blow-up of the vertex, show that $X$ is $\mathbb{Q}$-factorial, and explain what the proof of Corollary 9.5.16 produces.
2. (B) In Example 9.5.17 compute $\Pi' \cdot C$ on $X_1'$ for the two families of planes through $v$, and verify that the classes of the strict transforms on $X_1'$ and $X_2'$ show that $X_1' \dashrightarrow X_2'$ is not an isomorphism over $X$.
3. (B) Let $f \colon X \to Z$ be a flipping contraction of a klt pair $(X, \Delta)$ with $\Delta$ a $\mathbb{Q}$-divisor and $Z$ affine. Show that $\operatorname{\mathbf{Proj}}_Z R(X/Z, m(K_X + \Delta))$ does not depend on the integer $m \ge 1$, and that for $m$ with $m(K_X + \Delta)$ Cartier on $X$ the pullback of $m(K_X + \Delta)$ to a common resolution of $X$ and $X^+$ is the pullback of $m(K_{X^+} + \Delta^+)$ plus an effective divisor.
4. (B) Let $(X, \Delta)$ be a projective klt pair with $K_X + \Delta$ big and $X_{\mathrm{can}}$ its log canonical model. Show that $(X_{\mathrm{can}}, \psi_* \Delta)$ is klt, using Lemma 9.4.4 and the fact that a nef and big divisor on a log terminal model is the pullback of the ample divisor on $X_{\mathrm{can}}$.
5. (C) Prove that a $\mathbb{Q}$-factorialization is unique up to isomorphism when $\rho(X'/X) = 1$ and $X$ has a unique non-$\mathbb{Q}$-factorial point, and show by Example 9.5.17 that uniqueness fails in general.
6. (C) Use Corollary 9.5.16 to show that for every klt pair $(X, \Delta)$ and every set of exceptional divisors $F_1, \ldots, F_s$ over $X$ with $a(F_j, X, \Delta) \le 0$, there is a projective birational $h \colon X'' \to X$ with $X''$ $\mathbb{Q}$-factorial whose exceptional divisors are exactly the $F_j$. Hint: put coefficient $1 - \varepsilon$ only on the other exceptional divisors.

### Lean

`MinimalModel.KltFlips` states Corollary 9.5.15 in the project library as a statement without proof. The log canonical model and $\mathbb{Q}$-factorializations are not formalised.

### Notes and history

The existence of klt flips in all dimensions is Corollary 1.4.1 of BCHM; before BCHM it was known in dimension $3$ by Mori and Shokurov and in dimension $4$ by Shokurov and Hacon and McKernan, through the reduction to pl flips of Volume 8 and Chapter 2. The construction of $\mathbb{Q}$-factorializations from a log terminal model over $X$ is standard and appears in BCHM, Section 1.4, together with the existence of terminal models; Kollár (Kol13) discusses it in the context of the singularities of the minimal model program. The cone over a quadric and the Atiyah flop are the basic example of two different small $\mathbb{Q}$-factorial modifications.
