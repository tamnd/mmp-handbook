---
title: The rationality theorem
nodes: []
sources: [Kaw84, KM98, KMM87, Mat02, Fuj17d]
reads_with: [KM98:3.5, KMM87:ch4, Mat02:ch7]
requires: [4.2, 5.1, 7.1, 7.2, P4.2, P7.1, P7.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The rationality theorem

### Statement

The ground field $k$ is algebraically closed of characteristic $0$. Let $(X, \Delta)$ be a projective klt pair of dimension $n \ge 1$ and $H$ an ample Cartier divisor. If $K_X + \Delta$ is not nef, the *nef threshold* of $H$ is
$$r(H) = \max \{ t \in \mathbb{R} : H + t(K_X + \Delta) \text{ is nef} \}.$$
It exists and is positive: the set of $t \ge 0$ with $H + t(K_X + \Delta)$ nef is convex and closed, since the nef cone is a closed convex cone (Proposition P7.3.9), it contains a neighbourhood of $0$ in $[0, \infty)$, since the ample cone is open (Theorem P7.3.12), and it is bounded, since $(H + t(K_X + \Delta)) \cdot C < 0$ for $t$ large and a curve $C$ with $(K_X + \Delta) \cdot C < 0$. For $0 \le t < r(H)$ the divisor $H + t(K_X + \Delta) = (1 - t/r) H + (t/r)(H + r(K_X + \Delta))$ is ample, by part 3 of Theorem P7.3.12, and $H + r(K_X + \Delta)$ is nef but not ample.

**Theorem 7.3.4 (rationality theorem, Kawamata).** Let $(X, \Delta)$ be a projective klt pair of dimension $n$ with $K_X + \Delta$ not nef, $a \ge 1$ an integer with $a(K_X + \Delta)$ Cartier, and $H$ an ample Cartier divisor. Then $r(H)$ is rational, and $r(H) = u/v$ with $u, v$ coprime positive integers and
$$v \le a(n + 1).$$

Lean: not yet in Lean.

**Corollary 7.3.5 (the nef value morphism).** In the situation of Theorem 7.3.4, with $r = u/v$, the divisor $L = avH + ua(K_X + \Delta)$ is Cartier, nef and not ample, and it is semiample. The contraction $\varphi_H \colon X \to Z$ defined by $L$ (Corollary 7.2.4) is not finite, and every curve $C$ contracted by $\varphi_H$ satisfies
$$(K_X + \Delta) \cdot C = -\frac{H \cdot C}{r} < 0.$$

Lean: not yet in Lean.

KM98, Theorem 3.5, allows $H$ nef and big, in which case $r(H) = 0$ is possible. The ample case is the one Chapter 4 needs, and the proof below is written for it.

### Proof in words

Put $D(p, q) = pH + qa(K_X + \Delta)$ for integers $p, q$, so $D(p, q)$ is nef exactly when $aq \le rp$ and $p \ge 0$. On the lattice points with $p \ge 1$, $q \ge 1$ and $aq - rp < 1$, the divisor $D(p, q) - (K_X + \Delta)$ is ample, so vanishing makes $h^0(D(p, q))$ a polynomial $P(p, q)$ of degree at most $n$, and $P$ is nonzero because it counts sections of ample divisors below the line $aq = rp$. On the strip $0 < aq - rp < 1$, above the line, the divisors $D(p, q)$ are not nef, so their base loci are nonempty.

Suppose $r$ is not of the stated form. Lemma 7.3.1 makes $P$ nonzero at strip points as far out as wanted, so some strip divisors have sections, and among their base loci there is a minimal one, $L_1 = \operatorname{Bs} |D(p_1, q_1)|$. Resolve its base ideal and break ties. Vanishing on the resolution, with a small loss $\lambda_0$ of $H$ paid for by the slack $c\delta_1$ that the strip point $(p_1, q_1)$ has above the line, shows that on all far strip points the sections on the chosen divisor $F_0$ lift, and their number is a polynomial $Q$ of degree at most $n - 1$. The polynomial $Q$ is nonzero by nonvanishing on $F_0$ along a ray of nef divisors, so Lemma 7.3.1 again gives a far strip point $(p', q')$ where some section of $D(p', q')$ does not vanish on $f(F_0) \subseteq L_1$. Far out, $(p', q')$ is a multiple of $(p_1, q_1)$ plus a point where $D$ is free, so $\operatorname{Bs} |D(p', q')| \subseteq L_1$, and the inclusion is strict, contradicting minimality.

### Examples

**Example 7.3.6 (projective space).** Let $X = \mathbb{P}^n$, $\Delta = 0$, $a = 1$ and $H = \mathcal{O}(1)$. Then $K_X = \mathcal{O}(-n - 1)$ and $H + tK_X = \mathcal{O}(1 - t(n + 1))$ is nef exactly for $t \le 1/(n + 1)$. So $r = 1/(n + 1)$ and $v = n + 1 = a(n + 1)$: the bound of Theorem 7.3.4 is attained. The nef value morphism maps $\mathbb{P}^n$ to a point, and a line $C$ has $K_X \cdot C = -(n + 1) = -(H \cdot C)/r$.

**Example 7.3.7 (a boundary).** Let $X = \mathbb{P}^2$, $\ell$ a line, $m \ge 1$ and $\Delta = (1 - 1/m)\ell$, which is klt. Then $K_X + \Delta \equiv -(2 + 1/m)\ell$, so $a = m$ is the least integer with $a(K_X + \Delta) \sim -(2m + 1)\ell$ Cartier. For $H = \ell$, $H + t(K_X + \Delta) \equiv (1 - t(2m + 1)/m)\ell$, and $r = m/(2m + 1)$. Its denominator $2m + 1$ satisfies $2m + 1 \le 3m = a(n + 1)$, with equality only for $m = 1$.

**Example 7.3.8 (two rulings).** Let $X = \mathbb{P}^1 \times \mathbb{P}^1$, $\Delta = 0$, $a = 1$ and $H$ of bidegree $(1, 2)$. Then $K_X$ has bidegree $(-2, -2)$, and $H + tK_X$ of bidegree $(1 - 2t, 2 - 2t)$ is nef exactly for $t \le 1/2$. So $r = 1/2$, and $L = 2H + K_X$ has bidegree $(0, 2)$. Its contraction is the second projection, which contracts the curves $C = \mathbb{P}^1 \times \{y\}$, with $H \cdot C = 1$ and $K_X \cdot C = -2 = -(H \cdot C)/r$.

**Example 7.3.9 (one surface, two thresholds).** Let $X = \operatorname{Bl}_x \mathbb{P}^2$ with $h$ the pullback of a line and $e$ the exceptional curve, so $K_X = -3h + e$, and $xh - ye$ is nef exactly when $x \ge y \ge 0$. For $H = 2h - e$, $H + tK_X = (2 - 3t) h - (1 - t) e$ is nef exactly for $t \le 1/2$, so $r = 1/2$, $L = 2H + K_X = h - e$, and $\varphi_H$ is the ruling $X \to \mathbb{P}^1$, a fibre type contraction. For $H = 4h - e$, $H + tK_X = (4 - 3t) h - (1 - t) e$ is nef exactly for $t \le 1$, so $r = 1$, $L = H + K_X = h$, and $\varphi_H$ is the blow-down $X \to \mathbb{P}^2$, a divisorial contraction with $K_X \cdot e = -1 = -(H \cdot e)/r$. Different ample divisors pick out different extremal rays, which is how Chapter 4 uses the theorem.

**Example 7.3.10 (the quadric cone).** Let $X \subseteq \mathbb{P}^3$ be the quadric cone $\{x_0 x_1 = x_2^2\}$, isomorphic to $\mathbb{P}(1, 1, 2)$, with vertex $o$. It is normal and Gorenstein, and adjunction for the hypersurface gives $K_X = \mathcal{O}_X(-2)$, so $a = 1$. The minimal resolution is $\mathbb{F}_2 \to X$, contracting the $(-2)$-curve $\sigma$, and $K_{\mathbb{F}_2} \cdot \sigma = 0$ gives discrepancy $0$, so $X$ is canonical, in particular klt. For $H = \mathcal{O}_X(1)$, $H + tK_X = \mathcal{O}_X(1 - 2t)$, so $r = 1/2$ and $\varphi_H$ maps $X$ to a point. A line $C$ of the cone has $H \cdot C = 1$ and $K_X \cdot C = -2$.

### Proof

*Theorem 7.3.4.* Write $r = r(H)$ and $D(p, q) = pH + qa(K_X + \Delta)$ for $(p, q) \in \mathbb{Z}^2$. For $p > 0$, $D(p, q) = p(H + (aq/p)(K_X + \Delta))$ is nef if and only if $aq \le rp$.

*Step 1: the polynomial $P$.* Let $R_0$ be the set of $(p, q) \in \mathbb{Z}^2$ with $p \ge 1$, $q \ge 1$ and $aq - rp < 1$. For $(p, q) \in R_0$,
$$D(p, q) - (K_X + \Delta) = p \Bigl( H + \frac{aq - 1}{p} (K_X + \Delta) \Bigr)$$
with $0 \le (aq - 1)/p < r$, so it is ample. By part 1 of Corollary 5.1.14, $H^i(X, D(p, q)) = 0$ for $i > 0$, and $h^0(X, D(p, q)) = P(p, q)$, where $P$ is the polynomial of Theorem P7.1.4 for $\mathcal{O}_X$, $\mathcal{O}_X(H)$ and $\mathcal{O}_X(a(K_X + \Delta))$, of degree at most $n$. The points $(p, 1)$ with $p > (a - 1)/r$ lie in $R_0$, and by part 2 of Theorem P7.1.17, applied to $\mathcal{F} = \mathcal{O}_X(a(K_X + \Delta))$ and $H$, $P(p, 1) = (H^n) p^n / n! + O(p^{n-1})$ with $(H^n) > 0$. So $P \neq 0$.

The *strip* is the set $S_0$ of $(p, q) \in \mathbb{Z}^2$ with $p \ge 1$ and $0 < aq - rp < 1$. It lies in $R_0$, since $aq > rp > 0$ forces $q \ge 1$. For $(p, q) \in S_0$ the divisor $D(p, q)$ is not nef, so $|D(p, q)|$ is not free, since a free system is nef by part 1 of Proposition P7.3.9.

Suppose, for a contradiction, that $r$ is irrational or $r = u/v$ with $v > a(n + 1)$.

*Step 2: a minimal base locus.* Let $S$ be the set of $(p, q) \in S_0$ with $H^0(X, D(p, q)) \neq 0$, and $L(p, q) = \operatorname{Bs} |D(p, q)|$ for $(p, q) \in S$, a nonempty closed subset of $X$. By Lemma 7.3.1, applied to $P \neq 0$ with $x_0 = 1$, there is a point of $S_0$ where $P$ does not vanish, so $S \neq \emptyset$. Since $X$ is Noetherian, there is $(p_1, q_1) \in S$ such that $L_1 = L(p_1, q_1)$ is minimal for inclusion among the $L(p, q)$, $(p, q) \in S$. Put $D_1 = D(p_1, q_1)$ and $\delta_1 = aq_1 - rp_1 \in (0, 1)$.

*Step 3: resolution and tie-breaking.* Let $f \colon Y \to X$ and $P_H$ be given by Lemma 7.1.2 for $\Delta$, $\Gamma = 0$, the base ideal $\mathfrak{b}$ of $|D_1|$ and $H$. As in Step 1 of the proof of Theorem 7.2.1, $f^* D_1 = M + F_{\mathfrak{b}}$ with $M$ free and $F_{\mathfrak{b}} = \sum_j r_j F_j \neq 0$, $\operatorname{Supp} F_{\mathfrak{b}} = f^{-1}(L_1)$, and $K_Y = f^*(K_X + \Delta) + \sum_j a_j F_j$ with $a_j > -1$, and $a_j \le 0$ along non-exceptional $F_j$. Let $c_0$ be the threshold of Lemma 7.1.3 and put $\lambda_0 = c_0 \delta_1 / (2r)$. Apply Lemma 7.1.3 with $U = \lambda_0 f^* H$, $P_0 = \lambda_0 P_H$ and $\eta = c_0/4$. It gives $c \in (3c_0/4, c_0]$, $P$ with $\lambda_0 f^* H - P$ ample, $F_0 = F_{j_0}$ with $r_{j_0} > 0$, and
$$B = K_Y - f^*(K_X + \Delta) - c F_{\mathfrak{b}} - P, \qquad \lceil B \rceil = A_Y - F_0,$$
with $\Theta = \lceil B \rceil - B$. As in the proof of Theorem 7.2.1, $A_Y$ is effective and $f$-exceptional, and $f(F_0) \subseteq L_1$.

For $(p', q') \in \mathbb{Z}^2$, using $F_{\mathfrak{b}} = f^* D_1 - M$,
$$f^* D(p', q') + B - K_Y = f^*\bigl( p'' H + t''(K_X + \Delta) \bigr) + cM + (\lambda_0 f^* H - P),$$
with $p'' = p' - cp_1 - \lambda_0$ and $t'' = aq' - 1 - caq_1$. If $p'' > 0$ and $0 \le t'' \le r p''$, the first term is nef, and the sum is ample. The condition $t'' \le rp''$ reads $aq' - rp' \le 1 + c\delta_1 - r\lambda_0$, and $1 + c\delta_1 - r\lambda_0 > 1 + c_0\delta_1/4$. Let $R'$ be the set of $(p', q') \in \mathbb{Z}^2$ with
$$p' > cp_1 + \lambda_0, \qquad aq' \ge 1 + caq_1, \qquad aq' - rp' \le 1 + c_0 \delta_1/4.$$
For $(p', q') \in R'$ the divisor $f^* D(p', q') + B - K_Y$ is ample.

*Step 4: the polynomial $Q$.* Let $(p', q') \in R'$ and $N' = f^* D(p', q') + A_Y$. Part 1 of Corollary 5.1.14 for $(Y, \Theta)$ and $N' - F_0 = f^* D(p', q') + \lceil B \rceil$ gives $H^1(Y, N' - F_0) = 0$, so $H^0(Y, N') \to H^0(F_0, N'|_{F_0})$ is surjective. If $n = 1$, $F_0$ is a point and $h^0(F_0, N'|_{F_0}) = 1$. If $n \ge 2$, then $(F_0, \Theta|_{F_0})$ is klt by part 3 of Lemma 7.1.3 and Corollary 4.2.13, and by adjunction
$$N'|_{F_0} - (K_{F_0} + \Theta|_{F_0}) = \bigl( f^* D(p', q') + B - K_Y \bigr)|_{F_0}$$
is ample, so $H^i(F_0, N'|_{F_0}) = 0$ for $i > 0$ by Corollary 5.1.14 again. In both cases $h^0(F_0, N'|_{F_0}) = Q(p', q')$, where $Q$ is the polynomial of Theorem P7.1.4 on $Y$ for the sheaf $\mathcal{O}_{F_0}(A_Y|_{F_0})$ and the line bundles $f^* \mathcal{O}_X(H)$ and $f^* \mathcal{O}_X(a(K_X + \Delta))$, of degree at most $n - 1$.

$Q \neq 0$: choose an integer $p_3 \ge a/r$, so $D(p_3, 1)$ is nef. For $m$ large, $m(p_3, 1) \in R'$, since $m(a - rp_3) \le 0$. If $n = 1$, $Q = 1$. If $n \ge 2$, fix such an $m_3$ and apply Theorem 7.1.7 on $F_0$ to $D_0 = (f^* D(p_3, 1))|_{F_0}$, which is nef, and $G_0 = (B + F_0)|_{F_0}$, for which $\lceil G_0 \rceil = A_Y|_{F_0} \ge 0$ and $m_3 D_0 + G_0 - K_{F_0} = (f^* D(m_3 p_3, m_3) + B - K_Y)|_{F_0}$ is ample. It gives $Q(m p_3, m) = h^0(F_0, m D_0 + \lceil G_0 \rceil) \neq 0$ for $m \gg 0$.

*Step 5: far strip points lie below $L_1$.* Choose an integer $s > a/r$, so $D(s, 1)$ is ample. By Theorem P4.2.1 there are $e_0$ and $x_H$ such that $|e D(s, 1)| = |D(es, e)|$ is free for $e \ge e_0$ and $|xH|$ is free for $x \ge x_H$. So $D(x, y) = D(sy, y) + (x - sy) H$ is free on
$$W = \{ (x, y) \in \mathbb{Z}^2 : y \ge e_0, \; x - sy \ge x_H \}.$$
Put $\alpha = sq_1 - p_1$, which is positive since $sq_1 > aq_1/r > p_1$. Let $(p', q') \in S_0$ and $k = \lceil (x_H + sq' - p')/\alpha \rceil$. Since $aq' > rp'$, $sq' - p' > (sr/a - 1)p'$, which tends to infinity with $p'$, so $k \ge 1$ for $p'$ large. With $(x, y) = (p', q') - k(p_1, q_1)$,
$$x - sy = p' - sq' + k\alpha \ge x_H, \qquad y \ge q' - q_1 \Bigl( \frac{x_H + sq' - p'}{\alpha} + 1 \Bigr) = \frac{q_1 p' - p_1 q'}{\alpha} - q_1 \Bigl( \frac{x_H}{\alpha} + 1 \Bigr).$$
Since $aq' < rp' + 1$, $q_1 p' - p_1 q' > (\delta_1 p' - p_1)/a$, which tends to infinity with $p'$. So there is $x_2$ such that every $(p', q') \in S_0$ with $p' \ge x_2$ lies in $k(p_1, q_1) + W$ for some $k \ge 1$, and also in $R'$, since $p'$ is large, $aq' > rp'$ is large and $aq' - rp' < 1$. For such a point, products of sections give
$$\operatorname{Bs} |D(p', q')| \subseteq \operatorname{Bs} |k D_1| \cup \operatorname{Bs} |D(x, y)| \subseteq L_1.$$

*Step 6: the contradiction.* By Lemma 7.3.1, applied to $Q \neq 0$ of degree at most $n - 1 \le n$ with $x_0 = x_2$, there is $(p', q') \in S_0$ with $p' \ge x_2$ and $Q(p', q') \neq 0$. By Step 4 some section of $f^* D(p', q') + A_Y$ does not vanish along $F_0$, so by part 2 of Lemma 7.1.6, $H^0(X, D(p', q')) \neq 0$ and $f(F_0) \not\subseteq L(p', q')$. So $(p', q') \in S$, and $L(p', q') \subseteq L_1$ by Step 5, while $f(F_0) \subseteq L_1$. Hence $L(p', q') \subsetneq L_1$, which contradicts the minimality of $L_1$. So $r = u/v$ with $v \le a(n + 1)$.

*Corollary 7.3.5.* The divisor $L = D(av, u) = av(H + r(K_X + \Delta))$ is Cartier, nef and not ample. For an integer $a' \ge 1$,
$$a' L - (K_X + \Delta) = a'av \Bigl( H + \frac{a'ua - 1}{a'av} (K_X + \Delta) \Bigr), \qquad 0 \le \frac{a'ua - 1}{a'av} < r,$$
which is ample. So Theorem 7.2.1 applies to $L$, $L$ is semiample, and Corollary 7.2.4 gives the contraction $\varphi_H$ with $L \cong \varphi_H^* A_Z$ for an ample $A_Z$. If $\varphi_H$ were finite, $L$ would be ample by part 5 of Proposition P7.3.9; so $\varphi_H$ has a positive-dimensional fibre, which contains a curve. A curve $C$ is contracted exactly when $L \cdot C = 0$, that is, $H \cdot C + r(K_X + \Delta) \cdot C = 0$, which is the displayed formula, and $H \cdot C > 0$ gives $(K_X + \Delta) \cdot C < 0$.

### Exercises

1. (A) Compute $r(H)$ for $X = \mathbb{P}^1 \times \mathbb{P}^1$ and $H$ of bidegree $(p, q)$ with $p, q > 0$, and identify the nef value morphism in each case.
2. (A) Let $X = \mathbb{P}^n$ and $\Delta = \sum_{i=0}^{n} (1 - 1/m) H_i$ for the coordinate hyperplanes. Compute $a$ and $r(\mathcal{O}(1))$, and check the bound.
3. (A) In Example 7.3.9 take $H = xh - ye$ with $x > y > 0$. Show that $r(H) = \min\{ (x - y)/2, \, y \}$ and find which contraction occurs on each side of $x = 3y$.
4. (B) Let $X = \mathbb{P}^n$, $\ell$ a hyperplane, $m \ge 1$ and $\Delta = (1 - 1/m)\ell$. Show that $a = m$, that $r(\mathcal{O}(1)) = m/(mn + 1)$, and compare the denominator $mn + 1$ with the bound $m(n + 1)$.
5. (B) Let $X$ be smooth, $\Delta = 0$ and $a = 1$, and suppose the nef value morphism contracts a curve $C$ with $H \cdot C = 1$. Show that $r(H) = 1/(-K_X \cdot C)$, and deduce from Theorem 7.3.4 that $-K_X \cdot C \le n + 1$.
6. (C) Let $(X, \Delta)$ be klt, $K_X + \Delta$ not nef, and $H$ nef and big but not ample. Show that $r(H) = 0$ is possible, and that if $r(H) > 0$ the proof of Theorem 7.3.4 goes through after replacing the ampleness of $H$ by Kodaira's lemma, Lemma 5.1.9.

### Lean

The library states the cone theorem for klt pairs as `MinimalModel.ConeTheoremKlt`, which this volume derives from Theorem 7.3.4 in Chapter 4. The rationality theorem and the nef value morphism are not yet in Lean.

### Notes and history

Theorem 7.3.4 is Kawamata's (Kaw84), and with the base point free theorem it gives the cone theorem for klt pairs. The proof is KM98, Theorem 3.5, with the strip, the minimal base locus and the second polynomial $Q$ as there; KMM87, Chapter 4, gives the same proof, and Matsuki (Mat02) explains the role of the two polynomials. The relative version over a base, KM98, Theorem 3.24, is not proved here. Fujino (Fuj17d) proves the rationality theorem for lc pairs and quasi-log schemes, and Chapter 6 sketches that version.
