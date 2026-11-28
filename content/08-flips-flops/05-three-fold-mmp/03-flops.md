---
title: Flops connect minimal models
nodes: []
sources: [Kol89, Kaw08, Rei83b, KM98, Kaw92, Sho92]
reads_with: [Kol89:main, Rei83b:main, KM98:6]
requires: [1.5, 3.5, 4.4, 7.2, P8.13]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Flops connect minimal models

### Statement

Section 1 showed that the program depends on choices. This section shows that minimal models depend on them only up to flops. As in Section 1, $S$ is a quasi-projective variety over an algebraically closed field of characteristic $0$, and minimal models over $S$ are those of Definition 8.5.1.

**Definition 8.5.19 (flopping contractions and flops).** Let $X$ be a terminal 3-fold, projective over $S$. A *flopping contraction* over $S$ is a small contraction $\varphi \colon X \to Z$ over $S$ with $\rho(X/Z) = 1$ and $K_X \equiv_Z 0$. Let $D$ be a $\mathbb{Q}$-Cartier divisor on $X$ with $-D$ $\varphi$-ample. The *$D$-flop* of $\varphi$ is the $D$-flip of $\varphi$, as in Chapter 1: a small projective birational morphism $\varphi^+ \colon X^+ \to Z$ with $X^+$ normal, $D^+$ $\mathbb{Q}$-Cartier and $\varphi^+$-ample, where $D^+$ is the strict transform of $D$.

**Proposition 8.5.20 (minimal models agree in codimension one).** Let $X_1$ and $X_2$ be terminal 3-folds, projective over $S$, with $K_{X_1}$ and $K_{X_2}$ nef over $S$, and $\psi \colon X_1 \dashrightarrow X_2$ a birational map over $S$. Then $\psi$ is an isomorphism in codimension one, and $a(E, X_1) = a(E, X_2)$ for every divisor $E$ over $X_1$.

Lean: not yet in Lean.

**Proposition 8.5.21 (a flop of a minimal model is a minimal model).** Let $X$ be a minimal model over $S$, $\varphi \colon X \to Z$ a flopping contraction over $S$ and $X^+$ a $D$-flop. Then $K_X \sim_{\mathbb{Q}} \varphi^* K_Z$ for a $\mathbb{Q}$-Cartier $K_Z$, $K_{X^+} \sim_{\mathbb{Q}} (\varphi^+)^* K_Z$, and $X^+$ is a minimal model over $S$.

Lean: not yet in Lean.

**Theorem 8.5.22 (flops connect minimal models, Kollár).** Let $X_1$ and $X_2$ be minimal models over $S$ and $\psi \colon X_1 \dashrightarrow X_2$ a birational map over $S$. Then $\psi$ is a composite of finitely many flops over $S$.

Lean: not yet in Lean.

**Theorem 8.5.23 (Kawamata, all dimensions; cited).** Let $X_1$ and $X_2$ be $\mathbb{Q}$-factorial terminal varieties of any dimension, projective over $S$, with $K$ nef over $S$, and birational over $S$. Then $X_1 \dashrightarrow X_2$ is a composite of finitely many flops over $S$.

Lean: not yet in Lean.

**Proposition 8.5.24 (Reid's pagoda).** For $n \ge 1$ let $X_n = \{xy = wv\} \subset \mathbb{A}^4_{x, y, w, t}$ with $v = w + 2t^n$, and let $D = \{x = w = 0\}$ and $D' = \{x = v = 0\}$.

1. $X_n$ has an isolated singular point of type $cA_1$ at the origin and is terminal and Gorenstein.
2. The blow-up $g \colon Y_n \to X_n$ of the ideal $(x, w)$ is smooth and small, with exceptional curve $C \cong \mathbb{P}^1$, and $N_{C/Y_n} \cong \mathcal{O} \oplus \mathcal{O}(-2)$ for $n \ge 2$, $N_{C/Y_1} \cong \mathcal{O}(-1)^{\oplus 2}$.
3. $D_Y \cdot C = -1$ and $D'_Y \cdot C = 1$, and $g$ is a flopping contraction. The blow-up $Y_n^+$ of $(x, v)$ is the $D$-flop of $g$, and $Y_n \dashrightarrow Y_n^+$ is not an isomorphism over $X_n$.
4. Let $W \to Y_n$ be the blow-up of $C$, with exceptional divisor $E_1$. Then $E_1 \cong \mathbb{F}_2$ for $n \ge 2$ and $E_1 \cong \mathbb{P}^1 \times \mathbb{P}^1$ for $n = 1$, and $W$ contains an open subset isomorphic to $Y_{n-1}$ in which the exceptional curve of $Y_{n-1} \to X_{n-1}$ is the negative section of $E_1$.

Lean: not yet in Lean.

### Proof in words

Two minimal models compared on a common resolution have canonical divisors that differ by a divisor that is exceptional for both maps and, by the negativity lemma applied twice, both effective and anti-effective, hence zero. So neither contracts a divisor that the other keeps. For Kollár's theorem, take an ample divisor $H_2$ on $X_2$ and its strict transform $H_1$ on $X_1$. If $H_1$ is nef the two models are equal. If not, run the program for the pair $(X_1, \delta H_1)$ with $\delta$ small: every step is negative on $H_1$ and, for $\delta$ small, trivial on $K$, so it is a flop, and the sequence stops by termination of log flips. At the end $K + \delta H$ is nef, and the comparison of the two models on a common resolution, now for $K + \delta H$, shows that the last model is $X_2$. Reid's pagoda is the basic example of a flop that is not an Atiyah flop: blowing up the flopping curve produces the same situation with $n$ replaced by $n - 1$.

### Examples

**Example 8.5.25 (the case $n = 1$).** For $n = 1$, $xy = w(w + 2t)$ becomes $xy = u^2 - t^2$ with $u = w + t$, an ordinary double point, and $g \colon Y_1 \to X_1$ is the small resolution of Example 8.5.14. The flop $Y_1 \dashrightarrow Y_1^+$ is the Atiyah flop of Example 3.5.23: one blow-up of $C$ with $E_1 \cong \mathbb{P}^1 \times \mathbb{P}^1$, followed by the contraction of $E_1$ along the other ruling.

**Example 8.5.26 (the pagoda for $n = 2$).** For $n = 2$, $X_2 = \{xy = u^2 - t^4\}$ with $u = w + t^2$, and $N_{C/Y_2} = \mathcal{O} \oplus \mathcal{O}(-2)$. By part 4 the blow-up of $C$ contains $Y_1$, whose exceptional curve $C_1$ is the $(-2)$-section of $E_1 \cong \mathbb{F}_2$. Blowing up $C_1$ produces $E_2 \cong \mathbb{P}^1 \times \mathbb{P}^1$. Reid (Rei83b) shows that contracting $E_2$ along the other ruling and then the strict transform of $E_1$ along its ruling gives $Y_2^+$. In general $Y_n \dashrightarrow Y_n^+$ factors into $n$ blow-ups of curves followed by $n$ blow-downs; the picture of the exceptional divisors, stacked one above the other with $E_n \cong \mathbb{P}^1 \times \mathbb{P}^1$ on top, is the pagoda. This factorization is quoted here, not proved.

**Example 8.5.27 (discrepancies across the pagoda).** The divisor $E_1$ of part 4 has $a(E_1, Y_n) = 1$, since it is the blow-up of a smooth curve in a smooth 3-fold. By Proposition 8.4.3, $a(E_1, Y_n^+) = 1$ as well. Its centre on $Y_n^+$ lies over the origin of $X_n$, so it is $C^+$ or a point of $C^+$, and by Proposition P8.13.4 a divisor centred at a point of a smooth 3-fold has discrepancy at least $2$. So the centre is $C^+$. At the generic point of $C^+$ the local ring of $Y_n^+$ is a 2-dimensional regular local ring, over which the only divisor of discrepancy $1$ is the blow-up of the closed point. So $E_1$ is, as a valuation, the exceptional divisor of the blow-up of $C^+$: the two blow-ups $\operatorname{Bl}_C Y_n$ and $\operatorname{Bl}_{C^+} Y_n^+$ share their exceptional divisor, but for $n \ge 2$ they are not isomorphic over $X_n$, since the rulings of $E_1$ over $C$ and over $C^+$ are different.

### Proof

*Proof of Proposition 8.5.20.* Let $p \colon W \to X_1$ and $q \colon W \to X_2$ be a common resolution, with $q = \psi \circ p$. Write $K_W = p^* K_{X_1} + E_p = q^* K_{X_2} + E_q$, where $E_p$ is $p$-exceptional and $E_q$ is $q$-exceptional. Since $X_1$ is terminal, $E_p = \sum a(F, X_1) F$ over the $p$-exceptional prime divisors $F$ has every coefficient positive, so its support is the whole $p$-exceptional divisor, and similarly for $E_q$. Let $B = E_p - E_q = q^* K_{X_2} - p^* K_{X_1}$. A curve contracted by $q$ maps to a point of $S$, so $p^* K_{X_1}$ is nef on it, and $q^* K_{X_2}$ is zero on it: so $-B$ is $q$-nef. Also $q_* B = q_* E_p \ge 0$. By the negativity lemma, Theorem 1.5.22, $B \ge 0$. Exchanging the roles of $X_1$ and $X_2$ gives $-B \ge 0$. So $E_p = E_q$, and since their supports are the $p$-exceptional and the $q$-exceptional divisors, these are the same. A prime divisor on $X_1$ that is not a divisor on $X_2$ would have a strict transform on $W$ that is $q$-exceptional and not $p$-exceptional, which is impossible; so $\psi$ and $\psi^{-1}$ contract no divisor, and $\psi$ is an isomorphism in codimension one. For a divisor $E$ over $W$, Lemma P8.13.3 gives $a(E, X_1) = a(E, W) + \operatorname{ord}_E E_p = a(E, W) + \operatorname{ord}_E E_q = a(E, X_2)$. $\square$

*Proof of Proposition 8.5.21.* Since $K_X$ is $\varphi$-nef, and $2K_X - K_X = K_X$ is $\varphi$-nef and $\varphi$-big because $\varphi$ is birational, the relative base point free theorem (Theorem 7.2.1 in its relative form, KM98, Theorem 3.24) shows that $mK_X$ is $\varphi$-free for $m$ divisible enough. Since $K_X \equiv_Z 0$ and $\varphi_* \mathcal{O}_X = \mathcal{O}_Z$, $mK_X = \varphi^* L$ with $L$ Cartier, and $K_Z = \frac1m L$ is $\mathbb{Q}$-Cartier. The divisors $m K_{X^+}$ and $(\varphi^+)^* L$ agree outside the exceptional locus of $\varphi^+$, which has codimension $2$, so $K_{X^+} \sim_{\mathbb{Q}} (\varphi^+)^* K_Z$. Every curve $\Gamma \subset Z$ contracted to a point of $S$ is the image of a curve $\Gamma' \subset X$ contracted to the same point, and $K_Z \cdot \Gamma = \frac{1}{\deg(\Gamma' / \Gamma)} K_X \cdot \Gamma' \ge 0$; so $K_Z$ is nef over $S$, and so is its pull-back $K_{X^+}$. The 3-fold $X^+$ is terminal by Proposition 8.4.3 and $\mathbb{Q}$-factorial by the argument of Lemma 8.5.2, part 2, with $D$ in place of $K_X$. $\square$

*Proof of Theorem 8.5.22 (sketch).* By Proposition 8.5.20, $\psi$ is an isomorphism in codimension one. Let $H_2$ be a general member of a very ample linear system on $X_2$ over $S$, and $H_1$ its strict transform on $X_1$, which is $\mathbb{Q}$-Cartier because $X_1$ is $\mathbb{Q}$-factorial. Choose $\varepsilon > 0$ with $(X_1, \varepsilon H_1)$ klt, and let $r$ be such that $rK_{X_1}$ is Cartier.

*Step 1: the steps are flops.* Let $0 < \delta < \varepsilon / (1 + 6r)$ and let $R$ be a $(K_{X_1} + \delta H_1)$-negative extremal ray. Since $K_{X_1}$ is nef over $S$, $H_1 \cdot R < 0$, so $R$ is also $(K_{X_1} + \varepsilon H_1)$-negative, and by the cone theorem for the klt pair $(X_1, \varepsilon H_1)$ it is spanned by a curve $C$ with $-(K_{X_1} + \varepsilon H_1) \cdot C \le 6$. If $K_{X_1} \cdot C > 0$ then $K_{X_1} \cdot C \ge \frac1r$, and writing $K + \delta H = (1 - \frac{\delta}{\varepsilon}) K + \frac{\delta}{\varepsilon} (K + \varepsilon H)$ gives $(K + \delta H) \cdot C \ge \frac{1}{r}(1 - \frac{\delta}{\varepsilon}) - \frac{6\delta}{\varepsilon} > 0$, a contradiction. So $K_{X_1} \cdot R = 0$. The contraction of $R$ is not of fibre type, since curves in $R$ have $H_1 \cdot C < 0$ and so lie in $H_1$. It is not divisorial: an exceptional divisor $E$ would be covered by curves of $R$, hence contained in $H_1$, while $H_1$ is a prime divisor different from $E$ because $\psi$ is an isomorphism at the generic point of $E$ and $H_2$ is general. So the contraction is small, a flopping contraction, and the $(K + \delta H_1)$-flip, which exists by Shokurov's theorem on 3-fold log flips (Chapter 3), is an $H_1$-flop. By Proposition 8.5.21 the result is again a minimal model over $S$, isomorphic to $X_2$ in codimension one.

*Step 2: uniformity.* For a flop, $a(F, X^+, \varepsilon H^+) \ge a(F, X, \varepsilon H)$ by Lemma 8.4.2, since the flop is a $(K + \varepsilon H)$-flip as well. So the new pair is klt with the same $\varepsilon$. By Kollár's theorem that a flop of terminal 3-folds does not change the analytic type of the singular points (Kol89), the index $r$ does not change either. So Step 1 applies with the same $\delta$ to every model, and the program for $(X_1, \delta H_1)$ over $S$ consists of flops.

*Step 3: termination and the last model.* By Theorem 8.4.21 the program stops, at a minimal model $X'$ with $K_{X'} + \delta H'$ nef over $S$. On $X_2$, $K_{X_2} + \delta H_2$ is ample over $S$. The argument of Proposition 8.5.20, with $K + \delta H$ in place of $K$ and the strict transforms of $H$ on a common resolution $p \colon W \to X'$, $q \colon W \to X_2$, gives $p^*(K_{X'} + \delta H') = q^*(K_{X_2} + \delta H_2)$, because the difference is exceptional for both maps. The right side is semiample, so $K_{X'} + \delta H'$ is semiample over $S$, with the same sections in every multiple as $K_{X_2} + \delta H_2$, and the morphism it defines is a small birational morphism $X' \to X_2$. By Corollary 8.5.13, $X' \cong X_2$. $\square$

*Proof of Proposition 8.5.24.* Part 1. With $u = w + t^n$, the equation is $xy = u^2 - t^{2n}$, a hypersurface whose hyperplane section $t = 0$ is the $A_1$ point $xy = u^2$, and whose singular locus is the origin, since the partial derivatives $y$, $x$, $2u$ and $-2n t^{2n-1}$ vanish together only there. So it is an isolated $cA_1$ point, terminal by Theorem 4.4.17, and Gorenstein as a hypersurface.

Part 2. The blow-up of $(x, w)$ is covered by two charts. In the first, $x = \lambda w$, and the strict transform of $xy = wv$ gives $v = \lambda y$; so $w = \lambda y - 2t^n$ and $x = \lambda(\lambda y - 2t^n)$, and the chart is $\mathbb{A}^3$ with coordinates $(\lambda, y, t)$. In the second, $w = \mu x$, $y = \mu v = \mu(\mu x + 2t^n)$, and the chart is $\mathbb{A}^3$ with coordinates $(\mu, x, t)$. They are glued by $\mu = \lambda^{-1}$ and $x = \lambda^2 y - 2\lambda t^n$. So $Y_n$ is smooth. The fibre over the origin is $C = \{y = t = 0\} \cup \{x = t = 0\} \cong \mathbb{P}^1$, and $g$ is an isomorphism elsewhere, so $g$ is small. The normal bundle has fibre coordinates $(y, t)$ and $(x, t)$, with $x \equiv \lambda^2 y - 2\lambda t^n$ modulo $(y, t)^2$. For $n \ge 2$ the transition matrix is $\operatorname{diag}(\lambda^2, 1)$, which gives $\mathcal{O}(-2) \oplus \mathcal{O}$. For $n = 1$, $X_1$ is an ordinary double point and $N_{C/Y_1} = \mathcal{O}(-1)^{\oplus 2}$ as in Example 8.5.14.

Part 3. The ideal $(x, w)$ becomes invertible and $g$-ample on $Y_n$, and it equals $\mathcal{O}_{Y_n}(-D_Y)$ because $g$ is small, so $D_Y \cdot C = -1$. Since $D + D' = \operatorname{div}(x)$, $D'_Y \cdot C = 1$. As $X_n$ is Gorenstein and $g$ is small, $K_{Y_n} = g^* K_{X_n}$, so $K_{Y_n} \equiv_{X_n} 0$, and $\rho(Y_n/X_n) = 1$ since $C$ is irreducible. So $g$ is a flopping contraction, and $-D_Y$ is $g$-ample. The same computation for $(x, v)$ shows that $Y_n^+$ is smooth, small over $X_n$ with exceptional curve $C^+$, and $D'_{Y^+} \cdot C^+ = -1$, so $D_{Y^+} \cdot C^+ = 1$ and $D_{Y^+}$ is ample over $X_n$: $Y_n^+$ is the $D$-flop. If $Y_n \dashrightarrow Y_n^+$ were an isomorphism over $X_n$, it would carry $D_Y$ to $D_{Y^+}$ and $C$ to $C^+$, which is impossible since the degrees have opposite signs.

Part 4. In the first chart blow up $(y, t)$ and take the chart $y = st$; in the second blow up $(x, t)$ and take the chart $x = s't$. On the overlap $s' t = \lambda^2 s t - 2\lambda t^n$, so $s' = \lambda^2 s - 2\lambda t^{n-1}$. These two charts, with coordinates $(\lambda, s, t)$ and $(\mu, s', t)$, form a copy of $Y_{n-1}$ by Part 2. In it $E_1 = \{t = 0\}$, glued by $s' = \lambda^2 s$ for $n \ge 2$: the total space of $\mathcal{O}_{\mathbb{P}^1}(-2)$, which is $\mathbb{F}_2$ minus a section; the remaining charts add that section, so $E_1 \cong \mathbb{P}(N_{C/Y_n}) \cong \mathbb{F}_2$, and the exceptional curve $\{s = t = 0\}$ of $Y_{n-1}$ is the zero section, the $(-2)$-curve. For $n = 1$, $E_1 = \mathbb{P}(\mathcal{O}(-1)^{\oplus 2}) \cong \mathbb{P}^1 \times \mathbb{P}^1$. $\square$

### Exercises

1. (A) Check that the two charts of Proposition 8.5.24, part 2, map into $X_n$, and that the gluing $x = \lambda^2 y - 2\lambda t^n$ is compatible with $w = \mu x$.
2. (A) For $n = 1$, find a change of fibre coordinates that turns the transition matrix $\begin{pmatrix} \lambda^2 & -2\lambda \\ 0 & 1 \end{pmatrix}$ into $\operatorname{diag}(\lambda, \lambda)$, and conclude $N_{C/Y_1} \cong \mathcal{O}(-1)^{\oplus 2}$.
3. (A) Show that the automorphism $\sigma(x, y, w, t) = (x, y, -v, t)$ of $\mathbb{A}^4$ preserves $X_n$, exchanges $D$ and $D'$, and induces an isomorphism $Y_n \cong Y_n^+$ compatible with $\sigma$ on $X_n$.
4. (B) Let $X_1$, $X_2$ be terminal minimal models over $S$ and $\psi \colon X_1 \dashrightarrow X_2$ birational over $S$. Show with Proposition 8.5.20 that $\rho(X_1/S) = \rho(X_2/S)$ when both are $\mathbb{Q}$-factorial.
5. (B) In Step 1 of the proof of Theorem 8.5.22, show that the constant $6$ can be replaced by any bound on $-(K + \varepsilon H) \cdot C$ for the curves spanning the extremal rays, and explain why some such bound is needed.
6. (C) Let $X_1$ and $X_2$ be canonical 3-folds, projective over $S$, with $K$ nef over $S$, and $\psi \colon X_1 \dashrightarrow X_2$ birational over $S$. Show, by the proof of Proposition 8.5.20, that $E_p = E_q$ still holds and that every prime divisor on $X_1$ that is not a divisor on $X_2$ has discrepancy $0$ over $X_2$. Illustrate with Example 8.5.16, taking $S = X$.

### Lean

`MinimalModel.IsFlopOver` gives Definition 8.5.19 and `MinimalModel.IsMinimalModel` the notion of minimal model. Theorems 8.5.22 and 8.5.23 are not yet in Lean.

### Notes and history

Theorem 8.5.22 is Kollár's (Kol89), who also proved that flops of terminal 3-folds exist and preserve the analytic singularities; the proof sketched here follows KM98, Chapter 6, where the result appears with the comparison of Proposition 8.5.20 and the argument by a perturbation $K + \delta H$. Theorem 8.5.23 is Kawamata's (Kaw08); it uses the termination of the MMP with scaling from BCHM10, which is the subject of Volume 9. The pagoda is Reid's (Rei83b), who introduced it to show that flops of curves with normal bundle $\mathcal{O} \oplus \mathcal{O}(-2)$ are not single blow-ups and blow-downs.
