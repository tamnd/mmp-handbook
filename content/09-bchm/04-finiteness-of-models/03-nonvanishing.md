---
title: Nonvanishing for a big boundary and Diophantine approximation
nodes: []
sources: [BCHM10, HK10, Cor07, Laz04]
reads_with: [BCHM10:8, HK10:5]
requires: [4.2, 5.5, 7.2]
level: advanced
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Nonvanishing for a big boundary and Diophantine approximation

### Statement

**Theorem 9.4.12 (nonvanishing for a big boundary, BCHM Theorem D).** Let $(X, \Delta)$ be a projective klt pair with $\Delta$ an $\mathbb{R}$-divisor. If $\Delta$ is big and $K_X + \Delta$ is pseudo-effective, then there is an effective $\mathbb{R}$-divisor $D$ with $K_X + \Delta \sim_{\mathbb{R}} D$.

Lean: not yet in Lean.

Without the hypothesis that $\Delta$ is big the statement is the nonvanishing conjecture, which is open in dimension $4$ and higher; it is part of the abundance problem of Volume 10.

For $x \in \mathbb{R}^d$ write $|x| = \max_i |x_i|$. An affine subspace of $\mathbb{R}^d$ is *rational* if it is cut out by linear equations with rational coefficients, equivalently if it is the affine span of rational points. The intersection of rational affine subspaces is rational, so every $x$ lies in a smallest rational affine subspace $W_x$.

**Lemma 9.4.13 (Dirichlet's simultaneous approximation).** Let $y \in \mathbb{R}^e$ and let $N \ge 1$ be an integer. There are an integer $1 \le k \le N^e$ and $q \in \mathbb{Z}^e$ with $|k y - q| < 1/N$.

Lean: not yet in Lean.

**Lemma 9.4.14 (Diophantine approximation in the minimal rational subspace).** Let $x \in \mathbb{R}^d$, let $W = W_x$, and fix $\varepsilon > 0$ and an integer $k_0 \ge 1$. There are finitely many rational points $x_1, \ldots, x_s \in W$, positive integers $k_1, \ldots, k_s$ divisible by $k_0$, and positive real numbers $r_1, \ldots, r_s$ with $\sum_i r_i = 1$, such that
$$x = \sum_i r_i x_i, \qquad k_i x_i \in \mathbb{Z}^d, \qquad |x_i - x| < \frac{\varepsilon}{k_i}.$$

Lean: not yet in Lean.

**Lemma 9.4.15 (rational conditions and convex combinations).** Let $x \in \mathbb{R}^d$.

1. If $\lambda$ is an affine function on $\mathbb{R}^d$ with rational coefficients and $\lambda(x) = 0$, then $\lambda$ vanishes on $W_x$. If $x$ lies in a rational polytope $Q$, then a neighbourhood of $x$ in $W_x$ is contained in $Q$.
2. Let $D_1, \ldots, D_s$ be $\mathbb{Q}$-Cartier $\mathbb{Q}$-divisors on a normal variety with $D_i \sim_{\mathbb{Q}} E_i$ for effective $\mathbb{Q}$-divisors $E_i$, and $r_i > 0$ real. Then $\sum r_i D_i \sim_{\mathbb{R}} \sum r_i E_i \ge 0$.

Lean: not yet in Lean.

**Proposition 9.4.16 (nonvanishing for a nef log canonical divisor).** Let $(X, \Delta)$ be a projective klt pair with $X$ $\mathbb{Q}$-factorial and $\Delta$ a big $\mathbb{R}$-divisor, and suppose that $K_X + \Delta$ is nef. Then $K_X + \Delta \sim_{\mathbb{R}} D$ for an effective $\mathbb{R}$-divisor $D$. More precisely, $\Delta = \sum_i r_i \Delta_i$ with $r_i > 0$, $\sum r_i = 1$, each $\Delta_i$ a big $\mathbb{Q}$-divisor with $(X, \Delta_i)$ klt and $K_X + \Delta_i$ nef and semiample, and $\Delta_i$ as close to $\Delta$ as desired.

Lean: not yet in Lean.

### Proof in words

Theorem 9.4.12 is cited from BCHM; its proof is outlined below. The point of this section is the step that removes real coefficients. A real boundary $\Delta$ is a point of the coefficient space $\mathbb{R}^d$; it lies in a smallest rational affine subspace $W$, and every rational linear condition that $\Delta$ satisfies, every rational polytope it lies in, is shared by the rational points of $W$ near $\Delta$. Lemma 9.4.14 writes $\Delta$ as a convex combination of such rational points $\Delta_i$, with the extra feature that $k_i(\Delta_i - \Delta)$ is small for a denominator $k_i$ of $\Delta_i$. Then $k_i(K_X + \Delta_i)$ is an integral divisor that differs from $k_i(K_X + \Delta)$ by less than $\varepsilon$ in each coefficient, which is what one needs in order to lift sections from a divisor $S$ with the extension theorem of Chapter 2.

The proof of Lemma 9.4.14 has two steps. Dirichlet's theorem gives good approximations in $W$, with $k |x_i - x|$ as small as wanted. Their convex hull contains $x$ in its interior: if all good approximations lay on one side of a hyperplane through $x$, a reflection $(2 k_2 x_2 - k_1 x_1)/(2 k_2 - k_1)$ of an approximation $x_1$ through a much better one $x_2$ would be a good approximation on the other side, unless all of them lay on the hyperplane, which would put $x$ in a smaller rational subspace.

Proposition 9.4.16 shows the method at work: the nef locus of a rational polytope of boundaries is a rational polytope by Theorem 9.4.5, so the approximations $\Delta_i$ can be taken with $K_X + \Delta_i$ nef, and for rational big boundaries the base point free theorem gives sections.

*Outline of the proof of Theorem 9.4.12 in BCHM.* This paragraph is an outline. One works by induction on the dimension, with the existence of log terminal models and nonvanishing in dimension $n - 1$ available. After replacing $\Delta$ by an $\mathbb{R}$-linearly equivalent boundary one may assume $\Delta = A + B$ with $A$ a general ample $\mathbb{Q}$-divisor and $B \ge 0$. Nakayama's $\sigma$-decomposition $K_X + \Delta \equiv P_\sigma + N_\sigma$ splits off the divisorial part of the diminished base locus. The case where $K_X + \Delta$ is numerically equivalent to the effective divisor $N_\sigma$ is handled directly. Otherwise a tie-breaking construction on a log resolution produces a pair $(Y, \Delta_Y)$, crepant up to an effective exceptional term and up to adding a multiple of $K_X + \Delta$, which is plt with $\lfloor \Delta_Y \rfloor = S$ a single prime divisor not contained in the stable base locus. Induction gives nonvanishing for $(S, \Delta_S)$ with $(K_Y + \Delta_Y)|_S = K_S + \Delta_S$, the Diophantine step Lemma 9.4.14 reduces to rational boundaries with controlled denominators, and the extension theorem of Hacon and McKernan, treated in Chapter 2, lifts the resulting sections from $S$ to $Y$.

### Examples

**Example 9.4.17 (five lines with irrational coefficients).** Let $L_1, \ldots, L_5 \subseteq \mathbb{P}^2$ be lines in general position, so that no three are concurrent and $L_1 + \cdots + L_5$ has simple normal crossings, and put
$$\Delta = a L_1 + (1 - a) L_2 + \tfrac{2}{3}(L_3 + L_4 + L_5), \qquad a = \tfrac{\sqrt 2}{2}.$$
All coefficients lie in $(0, 1)$, so $(\mathbb{P}^2, \Delta)$ is klt by Theorem 4.2.14 with the identity as log resolution, $\Delta$ is big, being a positive combination of lines, and $\deg \Delta = a + (1 - a) + 2 = 3$, so $K_{\mathbb{P}^2} + \Delta \equiv 0$ is nef. In the coefficient space $\mathbb{R}^5$ the point $x = (a, 1 - a, \frac{2}{3}, \frac{2}{3}, \frac{2}{3})$ satisfies the rational equations $x_1 + x_2 = 1$ and $x_3 = x_4 = x_5 = \frac{2}{3}$, and since $a$ is irrational no further rational affine equation holds. So
$$W_x = \{ (c, 1 - c, \tfrac{2}{3}, \tfrac{2}{3}, \tfrac{2}{3}) : c \in \mathbb{R} \}.$$
Take $k_0 = 3$ and $\varepsilon = \frac{1}{4}$. With $a = 0.7071068$ to seven places, the rational points $x_1 = (\frac{5}{7}, \frac{2}{7}, \frac{2}{3}, \frac{2}{3}, \frac{2}{3})$ with $k_1 = 21$ and $x_2 = (\frac{7}{10}, \frac{3}{10}, \frac{2}{3}, \frac{2}{3}, \frac{2}{3})$ with $k_2 = 30$ satisfy $k_1 x_1 = (15, 6, 14, 14, 14)$ and $k_2 x_2 = (21, 9, 20, 20, 20)$, and
$$k_1 |x_1 - x| = 21 \, (\tfrac{5}{7} - a) = 0.1508, \qquad k_2 |x_2 - x| = 30 \, (a - \tfrac{7}{10}) = 0.2132,$$
both less than $\varepsilon$, to four places. Since $\frac{7}{10} < a < \frac{5}{7}$, $x = r_1 x_1 + r_2 x_2$ with $r_1 = (a - \frac{7}{10}) / (\frac{5}{7} - \frac{7}{10}) = 0.4975$ and $r_2 = 1 - r_1$, both positive. This is the conclusion of Lemma 9.4.14 with $s = 2$. The corresponding boundaries $\Delta_1$, $\Delta_2$ are klt with $K_{\mathbb{P}^2} + \Delta_i \sim_{\mathbb{Q}} 0$, so $K_{\mathbb{P}^2} + \Delta = r_1(K_{\mathbb{P}^2} + \Delta_1) + r_2(K_{\mathbb{P}^2} + \Delta_2) \sim_{\mathbb{R}} 0$, the nonvanishing of Proposition 9.4.16 with $D = 0$. Rational approximations off $W_x$ would not do: a rational point of $\mathbb{R}^5$ near $x$ with coefficient sum less than $3$ gives a boundary with $K_{\mathbb{P}^2} + \Delta'$ anti-ample, which has no effective $\mathbb{Q}$-divisor in its class.

**Example 9.4.18 (a rational point is its own subspace).** If $x \in \mathbb{Q}^d$, then $W_x = \{ x \}$ and Lemma 9.4.14 holds with $s = 1$, $x_1 = x$, $r_1 = 1$ and $k_1$ any common multiple of $k_0$ and the denominators of $x$, since $|x_1 - x| = 0$. For $x = (\frac{1}{2}, \frac{1}{3})$ and $k_0 = 1$ one may take $k_1 = 6$.

### Proof

*Proof of Theorem 9.4.12.* This is Theorem D of BCHM, proved there for a projective morphism $X \to U$; the statement above is the case $U = \operatorname{Spec} k$. It is cited, and its proof is outlined above. $\square$

*Proof of Lemma 9.4.13.* For $j = 0, 1, \ldots, N^e$ let $\{ j y \} \in [0, 1)^e$ be the vector of fractional parts of the coordinates of $j y$. Divide $[0, 1)^e$ into the $N^e$ half-open boxes $\prod_i [c_i / N, (c_i + 1)/N)$ with $c_i \in \{0, \ldots, N - 1\}$. The $N^e + 1$ points $\{ j y \}$ lie in these $N^e$ boxes, so two of them, for $j_1 < j_2$, lie in the same box. Put $k = j_2 - j_1$, so $1 \le k \le N^e$, and $q = \lfloor j_2 y \rfloor - \lfloor j_1 y \rfloor \in \mathbb{Z}^e$, the floors taken coordinatewise. Then $k y - q = \{ j_2 y \} - \{ j_1 y \}$ has all coordinates of absolute value less than $1/N$. $\square$

*Proof of Lemma 9.4.14.* If $x \in \mathbb{Q}^d$, Example 9.4.18 applies. Assume $x \notin \mathbb{Q}^d$, so $e = \dim W \ge 1$. Write $W = \{ w_0 + M y : y \in \mathbb{R}^e \}$ with $w_0 \in \mathbb{Q}^d$ and $M$ a rational $d \times e$ matrix of rank $e$, and let $D \ge 1$ be an integer with $D w_0 \in \mathbb{Z}^d$ and $D M$ integral. Let $x = w_0 + M y_0$ and let $\| M \|$ be the operator norm for $| \cdot |$. Call $z \in W \cap \mathbb{Q}^d$ a *$\delta$-approximation* if there is an integer $k \ge 1$ divisible by $k_0$ with $k z \in \mathbb{Z}^d$ and $k |z - x| < \delta$, and let $G_\delta$ be the set of $\delta$-approximations.

*Step 1: approximations exist.* Let $\delta > 0$ and $N > \|M\| k_0 D / \delta$. Lemma 9.4.13 gives $1 \le k' \le N^e$ and $q \in \mathbb{Z}^e$ with $|k' y_0 - q| < 1/N$. Put $k = k_0 D k'$ and $z = w_0 + M q / k'$. Then $z \in W \cap \mathbb{Q}^d$, $k z = k_0 k' (D w_0) + k_0 (DM) q \in \mathbb{Z}^d$, and
$$k |z - x| = k_0 D \, |M(q - k' y_0)| \le k_0 D \|M\| / N < \delta.$$
So $z \in G_\delta$, and $|z - x| < \delta$. In particular $x$ lies in the closure of $G_\delta$ for every $\delta > 0$.

*Step 2: $x$ is an interior point of $\operatorname{conv}(G_\delta)$ in $W$.* Suppose not, for some $\delta > 0$. Since $\operatorname{conv}(G_\delta)$ is a convex subset of the finite-dimensional affine space $W$ and $x$ is not in its interior, the supporting hyperplane theorem gives a nonzero linear form $\ell$ on the direction space of $W$ with $\ell(z - x) \ge 0$ for all $z \in G_\delta$. The affine span $H$ of $G_{\delta/2}$ is spanned by rational points, so it is a rational affine subspace, and it contains $x$ because $x$ lies in the closure of $G_{\delta/2}$ by Step 1 and $H$ is closed. By minimality of $W$, $H = W$, so $G_{\delta/2}$ is not contained in the proper affine subspace $\{ z \in W : \ell(z - x) = 0 \}$. As $G_{\delta/2} \subseteq G_\delta$, there is $z_1 \in G_{\delta/2}$ with $\ell(z_1 - x) > 0$; let $k_1$ be an integer as in the definition, with $k_1 |z_1 - x| < \delta/2$. Since $x \notin \mathbb{Q}^d$, the number $c = \min_{1 \le j \le k_1} \operatorname{dist}(x, \frac{1}{j} \mathbb{Z}^d)$ is positive. Choose $\eta > 0$ with
$$\eta < \delta / 4, \qquad \eta < c, \qquad 2 \|\ell\| \eta < k_1 \ell(z_1 - x),$$
where $\|\ell\|$ is the norm of $\ell$ for $|\cdot|$. Step 1 gives $z_2 \in G_\eta$ with an integer $k_2$; then $|z_2 - x| < \eta / k_2 \le \eta < c$, so $k_2 > k_1$. Put $k_3 = 2 k_2 - k_1 > 0$, which is divisible by $k_0$, and $z_3 = (2 k_2 z_2 - k_1 z_1)/k_3$. Then $z_3$ is an affine combination of points of $W$, so $z_3 \in W \cap \mathbb{Q}^d$, and $k_3 z_3 = 2 k_2 z_2 - k_1 z_1 \in \mathbb{Z}^d$. Since $k_3 (z_3 - x) = 2 k_2 (z_2 - x) - k_1 (z_1 - x)$,
$$k_3 |z_3 - x| \le 2 k_2 |z_2 - x| + k_1 |z_1 - x| < 2 \eta + \delta / 2 < \delta,$$
so $z_3 \in G_\delta$, and
$$k_3 \, \ell(z_3 - x) = 2 k_2 \, \ell(z_2 - x) - k_1 \, \ell(z_1 - x) \le 2 \|\ell\| \eta - k_1 \ell(z_1 - x) < 0.$$
This contradicts $\ell(z_3 - x) \ge 0$.

*Step 3: conclusion.* Take $\delta = \varepsilon$. By Step 2 there is a simplex in $W$ with vertices in $\operatorname{conv}(G_\varepsilon)$ containing a neighbourhood of $x$ in $W$; each vertex is a convex combination of finitely many points of $G_\varepsilon$, so there is a finite set $F = \{x_1, \ldots, x_s\} \subseteq G_\varepsilon$ with $x$ in the interior of $\operatorname{conv}(F)$ relative to $W$. Let $b = \frac{1}{s} \sum x_i$. For small $\tau > 0$ the point $x' = x - \tau (b - x)$ still lies in $\operatorname{conv}(F)$, say $x' = \sum \mu_i x_i$ with $\mu_i \ge 0$, and then
$$x = \frac{1}{1 + \tau} x' + \frac{\tau}{1 + \tau} b = \sum_i \Bigl( \frac{\mu_i}{1 + \tau} + \frac{\tau}{s(1 + \tau)} \Bigr) x_i,$$
with all coefficients $r_i$ positive and summing to $1$. For each $x_i \in G_\varepsilon$ choose $k_i$ as in the definition; then $k_i$ is divisible by $k_0$, $k_i x_i \in \mathbb{Z}^d$ and $|x_i - x| < \varepsilon / k_i$. $\square$

*Proof of Lemma 9.4.15.* For part 1, the set $\{ \lambda = 0 \}$ is a rational affine subspace containing $x$, so it contains $W_x$. A rational polytope $Q$ containing $x$ has a unique face $Q_0$ containing $x$ in its relative interior; $Q_0$ is a rational polytope, its affine span is a rational affine subspace containing $x$ and hence $W_x$, and $Q_0$ contains a neighbourhood of $x$ in its affine span, so a neighbourhood of $x$ in $W_x$. For part 2, $D_i - E_i$ is a $\mathbb{Q}$-linear combination of principal divisors, so $\sum r_i (D_i - E_i)$ is an $\mathbb{R}$-linear combination of principal divisors. $\square$

*Proof of Proposition 9.4.16.* Let $S_1, \ldots, S_d$ be the components of $\Delta$ and identify divisors supported on them with $\mathbb{R}^d$; let $x$ be the point of $\Delta$ and $W = W_x$. Since $X$ is $\mathbb{Q}$-factorial there is an integer $k_0 \ge 1$ such that $k_0 K_X$ and every $k_0 S_j$ are Cartier. By the proof of Lemma 9.4.2, with a log resolution of $(X, \sum S_j)$, the klt condition on boundaries supported on the $S_j$ is a finite system of strict rational affine inequalities, so the klt boundaries form an open subset of $\mathbb{R}_{\ge 0}^d$. Bigness is an open condition on the class, so there is a rational box $Q \subseteq \mathbb{R}_{> 0}^d$ around $x$ such that every $\Delta' \in Q$ is a big klt boundary. Put $\mathcal{P} = Q \cap W$, a rational polytope of klt boundaries. By Theorem 9.4.5, $\mathcal{N}(\mathcal{P})$ is a rational polytope, and it contains $x$. By Lemma 9.4.15, part 1, there is $\rho > 0$ such that every point of $W$ within $\rho$ of $x$ lies in $\mathcal{N}(\mathcal{P})$.

Apply Lemma 9.4.14 to $x$ with the integer $k_0$ and with $\varepsilon = \min(\rho, 1)/k_0$, and multiply each $k_i$ by $k_0$: this gives rational $x_i \in W$, integers $k_i$ divisible by $k_0$, and $r_i > 0$ with $\sum r_i = 1$, $x = \sum r_i x_i$, $k_i x_i \in k_0 \mathbb{Z}^d$ and $|x_i - x| < \rho$. Let $\Delta_i$ be the divisor of $x_i$. Then $\Delta_i \in \mathcal{N}(\mathcal{P})$, so $\Delta_i$ is a big $\mathbb{Q}$-divisor, $(X, \Delta_i)$ is klt, $K_X + \Delta_i$ is nef, and $D_i = k_i(K_X + \Delta_i)$ is Cartier, as an integral combination of $k_0 K_X$ and the $k_0 S_j$.

It remains to show that $K_X + \Delta_i$ is semiample. Since $\Delta_i$ is big, Kodaira's lemma gives an ample $\mathbb{Q}$-divisor $H$ and an effective $\mathbb{Q}$-divisor $B$ with $\Delta_i \sim_{\mathbb{Q}} H + B$. For rational $\tau \in (0, 1)$ put $\Delta_i^\tau = (1 - \tau) \Delta_i + \tau B$. On a log resolution of $(X, \Delta_i + B)$ the coefficients of the crepant pullback of $K_X + \Delta_i^\tau$ are affine in $\tau$ and less than $1$ at $\tau = 0$, so by Theorem 4.2.14 the pair $(X, \Delta_i^\tau)$ is klt for small $\tau > 0$. Then
$$\tfrac{1}{k_i} D_i - (K_X + \Delta_i^\tau) = \tau (\Delta_i - B) \sim_{\mathbb{Q}} \tau H$$
is ample, so nef and big, and the base point free theorem, Theorem 7.2.1, applied to $(X, \Delta_i^\tau)$, $D_i$ and $a = 1/k_i$, shows that $|b D_i|$ is free for $b \gg 0$. In particular $K_X + \Delta_i \sim_{\mathbb{Q}} E_i$ for an effective $\mathbb{Q}$-divisor $E_i$, and $K_X + \Delta = \sum r_i (K_X + \Delta_i) \sim_{\mathbb{R}} \sum r_i E_i$ by Lemma 9.4.15, part 2. $\square$

### Exercises

1. (B) Find $k \le 100$ and $q$ with $|k \sqrt 2 - q| < \frac{1}{10}$ by the pigeonhole argument of Lemma 9.4.13, and compare with the continued fraction convergents $\frac{7}{5}$, $\frac{17}{12}$, $\frac{41}{29}$ of $\sqrt 2$.
2. (B) Let $x = (\sqrt 2, \sqrt 3, \sqrt 2 + \sqrt 3) \in \mathbb{R}^3$. Determine $W_x$, and show that a rational point near $x$ but off $W_x$ never satisfies the rational equation that $x$ satisfies.
3. (B) In Example 9.4.17 replace $L_1$ and $L_2$ by a smooth conic $Q$ with coefficient $a$ and a line with coefficient $1 - 2a$, for irrational $a \in (0, \frac{1}{2})$, and adjust the other coefficients so that $K + \Delta \equiv 0$. Write down $W_x$ and two approximations as in Lemma 9.4.14 with $k_0 = 2$.
4. (B) Show that the reflection $z_3 = (2k_2 z_2 - k_1 z_1)/(2k_2 - k_1)$ in Step 2 of the proof of Lemma 9.4.14 lies on the opposite side of $x$ from $z_1$ along the line through $z_1$ and $z_2$ when $z_2 = x$, and compute $k_3 |z_3 - x|$ in that case.
5. (C) Prove Proposition 9.4.16 without assuming that $X$ is $\mathbb{Q}$-factorial, under the assumption that $K_X$ and every component of $\Delta$ are $\mathbb{Q}$-Cartier. Which step uses that hypothesis?
6. (C) Let $(X, \Delta)$ be a projective klt pair with $\Delta$ a big $\mathbb{Q}$-divisor and $K_X + \Delta \sim_{\mathbb{R}} D \ge 0$. Show that there is an effective $\mathbb{Q}$-divisor $D'$ with $K_X + \Delta \sim_{\mathbb{Q}} D'$. Hint: the set of effective $\mathbb{R}$-divisors supported on $\operatorname{Supp} D$ and $\mathbb{R}$-linearly equivalent to $K_X + \Delta$ is cut out by rational linear conditions.

### Lean

None of the statements of this section is formalised.

### Notes and history

Nonvanishing for a big boundary is Theorem D of BCHM, whose Section 8 contains the proof outlined above; the version for $\mathbb{Q}$-divisors and $K_X + \Delta$ nef is a direct consequence of the base point free theorem, as in Proposition 9.4.16. The approximation lemma is in BCHM, Section 3.7, and Hacon and Kovács (HK10) give an exposition of the induction with the role of real coefficients explained. Dirichlet's theorem is classical. The general nonvanishing conjecture, without the bigness of $\Delta$, is open in dimension $4$ and higher and is known in dimension at most $3$, as part of abundance for 3-folds.
