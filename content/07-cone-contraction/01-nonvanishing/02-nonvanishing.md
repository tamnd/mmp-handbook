---
title: The nonvanishing theorem
nodes: []
sources: [Sho85, KM98, Kaw85, KMM87, Mat02]
reads_with: [KM98:3.4, KMM87:ch2, Mat02:ch6]
requires: [4.1, 4.2, 5.1, P4.2, P7.1, P7.3, P7.5, P7.7, P7.8]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The nonvanishing theorem

### Statement

The ground field $k$ is algebraically closed of characteristic $0$. For a proper birational morphism $f \colon Y \to X$ of normal varieties and a divisor $E = \sum_j e_j F_j$ on $Y$, the pushforward $f_* E$ is $\sum_j e_j f(F_j)$, the sum over the $F_j$ that are not $f$-exceptional. For $X$ smooth, $K_{Y/X} = K_Y - f^* K_X$ is the relative canonical divisor, effective and $f$-exceptional when $Y$ is smooth too.

**Lemma 7.1.6 (sections on a resolution).** Let $f \colon Y \to X$ be a proper birational morphism of normal varieties, $N$ a Cartier divisor on $X$ and $E$ a divisor on $Y$ with $f^* N + E$ Cartier.

1. $f_* \mathcal{O}_Y(f^* N + E) \subseteq \mathcal{O}_X(N + f_* E)$.
2. If $E$ is effective and $f$-exceptional, this is an equality, $f_* \mathcal{O}_Y(f^* N + E) = \mathcal{O}_X(N)$. Then $s \mapsto f^* s \cdot \sigma_E$, with $\sigma_E$ the canonical section of $\mathcal{O}_Y(E)$, is an isomorphism $H^0(X, N) \to H^0(Y, f^* N + E)$, and for a prime divisor $F_0 \not\subseteq \operatorname{Supp} E$ the section $f^* s \cdot \sigma_E$ vanishes along $F_0$ if and only if $f(F_0) \subseteq \operatorname{Supp}(\operatorname{div} s)$. In particular, some section of $f^* N + E$ does not vanish along $F_0$ if and only if $f(F_0) \not\subseteq \operatorname{Bs} |N|$.

Lean: not yet in Lean.

**Theorem 7.1.7 (nonvanishing, Shokurov).** Let $X$ be a smooth projective variety of dimension $n \ge 1$, $D$ a nef Cartier divisor and $G$ a $\mathbb{Q}$-divisor on $X$ with snc support and $\lceil G \rceil \ge 0$. Suppose that $aD + G - K_X$ is nef and big for some integer $a > 0$. Then
$$H^0(X, \mathcal{O}_X(mD + \lceil G \rceil)) \neq 0 \quad \text{for every } m \gg 0.$$

Lean: not yet in Lean.

**Corollary 7.1.8 (nonvanishing for klt pairs).** Let $(X, \Delta)$ be a projective klt pair, $D$ a nef Cartier divisor on $X$, and $a > 0$ a rational number with $aD - (K_X + \Delta)$ nef and big. Then $H^0(X, \mathcal{O}_X(mD)) \neq 0$ for every $m \gg 0$.

Lean: not yet in Lean.

The case $D = 0$ is allowed in Theorem 7.1.7 and gives nothing new, since $\lceil G \rceil$ is effective. The theorem is used in Chapters 2 and 3 on the divisor $F_0$ of the tie-breaking lemma, where $G$ is the restriction of $B + F_0$ and its round-up is the restriction of an effective exceptional divisor.

### Proof in words

Lemma 7.1.6 says that sections of $f^* N$ twisted by an effective exceptional divisor are the sections of $N$, so nonvanishing can be checked on a resolution.

For Theorem 7.1.7, first reduce to the case where $A = aD + G - K_X$ is ample, by Kodaira's lemma and a resolution that keeps $G$ snc. If $D \equiv 0$, Kawamata-Viehweg vanishing for the klt pair $(X, \lceil G \rceil - G)$ shows that $h^0(mD + \lceil G \rceil) = \chi(mD + \lceil G \rceil)$ for every integer $m$, a polynomial in $m$ that is nonnegative and is at least $1$ at $m = 0$, so it is positive for $m \gg 0$.

If $D \not\equiv 0$ and $n \ge 2$, then $(eD + A)^n$ grows linearly in $e$, so some $M \in |q(eD + A)|$ has multiplicity more than $nq$ at a point $x$ outside $\operatorname{Supp} G$. The blow-up of $x$ shows that the threshold $c_0$ of $M$ is less than $1/q$. Tie-breaking on a resolution gives a divisor $F_0$ and a decomposition $\lceil B \rceil = A_Y - F_0$ such that $f^* (bD) + B - K_Y$ is ample, because $c f^* M$ uses only a fraction $cq < 1$ of $A$ and $D$ absorbs the rest. Vanishing on $Y$ makes $H^0(Y, f^* bD + A_Y) \to H^0(F_0, \cdot)$ surjective, the hypothesis holds on $F_0$ in dimension $n - 1$ by adjunction, and the sections go down to $X$ by Lemma 7.1.6.

Corollary 7.1.8 is Theorem 7.1.7 on a log resolution with $G = K_Y - f^*(K_X + \Delta)$.

### Examples

**Example 7.1.9 (bigness is needed).** Let $X$ be an elliptic curve, so $K_X = 0$, and $D$ a divisor of degree $0$. Then $D$ is nef, and $aD - K_X = aD$ is not big for any $a$. If $D$ is not torsion in $\operatorname{Pic}(X)$, then $mD \not\sim 0$ and $H^0(X, mD) = 0$ for every $m \ge 1$. If $D$ is a point of order $2$, then $H^0(X, mD) \neq 0$ exactly for even $m$, so even when sections exist the conclusion "for every $m \gg 0$" fails.

**Example 7.1.10 (the numerically trivial case).** Let $X$ be an abelian variety, $D$ an algebraically trivial divisor that is not torsion, and $G = L$ an ample divisor. Then $K_X = 0$, $aD + G - K_X \equiv L$ is ample, and Step 1 of the proof gives $h^0(mD + L) = \chi(mD + L)$ for every $m \in \mathbb{Z}$, which is positive since $mD + L$ is ample. Without $L$, the divisor $aD - K_X \equiv 0$ is not big, and $H^0(mD) = 0$ for every $m \neq 0$.

**Example 7.1.11 ($m \gg 0$ is needed).** Let $X$ be a smooth projective curve of genus $g \ge 2$ and $D$ a divisor of degree $1$ with $h^0(D) = 0$; such $D$ exist since the effective classes of degree $1$ form a curve in the $g$-dimensional $\operatorname{Pic}^1(X)$. With $G = 0$ and $a > 2g - 2$, the divisor $aD - K_X$ has positive degree, so it is ample. Riemann-Roch gives $h^0(mD) \ge m + 1 - g > 0$ for $m \ge g$, while $h^0(D) = 0$.

### Proof

*Lemma 7.1.6.* Let $V \subseteq X$ be open and $\varphi$ a nonzero rational function with $\operatorname{div}_Y \varphi + f^* N + E \ge 0$ on $f^{-1} V$. Pushforward of divisors preserves effectivity, $f_* f^* N = N$, and $f_* \operatorname{div}_Y \varphi = \operatorname{div}_X \varphi$, since the valuation of $\varphi$ along a prime divisor of $X$ equals its valuation along the strict transform. So $\operatorname{div}_X \varphi + N + f_* E \ge 0$ on $V$, which is part 1. For part 2, $f_* E = 0$, and conversely if $\operatorname{div}_X \varphi + N \ge 0$ on $V$, then $f^*(\operatorname{div}_X \varphi + N) \ge 0$ on $f^{-1} V$ as the pullback of an effective Cartier divisor, and adding $E \ge 0$ keeps it effective. Taking global sections gives the isomorphism, and the section $f^* s \cdot \sigma_E$ has divisor $f^* \operatorname{div}(s) + E$. Since $F_0 \not\subseteq \operatorname{Supp} E$, it vanishes along $F_0$ if and only if $F_0 \subseteq f^{-1}(\operatorname{Supp} \operatorname{div} s)$, that is, $f(F_0) \subseteq \operatorname{Supp} \operatorname{div} s$. The base locus $\operatorname{Bs} |N|$ is the intersection of these supports, which gives the last statement.

*Theorem 7.1.7.* Write $G = G^+ - G^-$ with $G^+, G^-$ effective without common components. Since $\lceil G \rceil \ge 0$, every coefficient of $G$ is greater than $-1$, so $G^-$ has coefficients in $[0, 1)$ and snc support, and $(X, G^-)$ is klt by Corollary 4.2.13. This gives:

$(\ast)$ For every projective birational $\mu \colon X' \to X$ from a smooth variety, every coefficient of $K_{X'/X} + \mu^* G$ is greater than $-1$.

Indeed, along a $\mu$-exceptional prime $E$ the coefficient is $a(E, X, G^-) + \operatorname{mult}_E \mu^* G^+ \ge a(E, X, G^-) > -1$, and along the strict transform of a prime $P$ of $X$ it is the coefficient of $P$ in $G$. The proof of the theorem is by induction on $n$.

*Step 0: reduction to $A = aD + G - K_X$ ample.* By Lemma 5.1.9, over a point, there is an effective $\mathbb{Q}$-divisor $E$ with $aD + G - K_X - \varepsilon E$ ample for every rational $0 < \varepsilon \le 1$. Apply Theorem P7.8.15 to $\operatorname{Supp} G \cup \operatorname{Supp} E$: it gives $\mu \colon X' \to X$ with $X'$ smooth projective, $\mu^{-1}_*(\operatorname{Supp} G \cup \operatorname{Supp} E) + \operatorname{Exc}(\mu)$ snc, and an effective $\mu$-exceptional $F'$ with $\mu^*(aD + G - K_X - \varepsilon E) - \delta F'$ ample for $0 < \delta \le \delta_0(\varepsilon)$. Put
$$G' = K_{X'/X} + \mu^* G - \varepsilon \mu^* E - \delta F'.$$
By $(\ast)$, for $\varepsilon$ and then $\delta$ small every coefficient of $G'$ is greater than $-1$, so $\lceil G' \rceil \ge 0$, and $G'$ has snc support. Since $K_{X'} = \mu^* K_X + K_{X'/X}$,
$$a \mu^* D + G' - K_{X'} = \mu^*(aD + G - K_X - \varepsilon E) - \delta F'$$
is ample, and $\mu^* D$ is nef. Along the strict transform of a prime $P$ of $X$ the coefficient of $G'$ is at most that of $G$, so $\mu_* \lceil G' \rceil \le \lceil G \rceil$, and by part 1 of Lemma 7.1.6, $H^0(X', m \mu^* D + \lceil G' \rceil) \subseteq H^0(X, mD + \lceil G \rceil)$. So it suffices to prove the theorem for $(X', \mu^* D, G')$, and from now on $A = aD + G - K_X$ is ample.

*Step 1: $D \equiv 0$.* Put $\Theta = \lceil G \rceil - G$. It has snc support and coefficients in $[0, 1)$, so $(X, \Theta)$ is klt by Corollary 4.2.13. For every $m \in \mathbb{Z}$ the Cartier divisor $N_m = mD + \lceil G \rceil$ satisfies
$$N_m - (K_X + \Theta) = mD + G - K_X = A + (m - a) D,$$
which is numerically equivalent to $A$, hence ample by part 2 of Theorem P7.3.12. By part 1 of Corollary 5.1.14, $H^i(X, N_m) = 0$ for $i > 0$, so $h^0(X, N_m) = \chi(X, N_m) = P(m)$ for all $m \in \mathbb{Z}$, where $P$ is the polynomial of Theorem P7.1.4 for $\mathcal{F} = \mathcal{O}_X(\lceil G \rceil)$ and $L = \mathcal{O}_X(D)$. Then $P(m) \ge 0$ for all $m$, and $P(0) = h^0(X, \lceil G \rceil) \ge 1$ since $\lceil G \rceil$ is effective. So $P$ is a nonzero polynomial, it has finitely many roots, and $P(m) > 0$ for every $m \gg 0$.

*Step 2: $D \not\equiv 0$, and a divisor with high multiplicity.* If $n = 1$, then $\deg D > 0$, and Riemann-Roch gives $h^0(mD + \lceil G \rceil) \ge m \deg D + \deg \lceil G \rceil + 1 - g > 0$ for $m \gg 0$. Let $n \ge 2$. By part 2 of Lemma 7.1.1, $(D \cdot A^{n-1}) > 0$, and by part 1,
$$\bigl( (eD + A)^n \bigr) = \sum_{k=0}^n \binom{n}{k} e^k (D^k \cdot A^{n-k}) \ge (A^n) + n e (D \cdot A^{n-1}).$$
Fix an integer $e \ge 1$ with $((eD + A)^n) > n^n$, put $L = eD + A$, an ample $\mathbb{Q}$-divisor, and let $q_0 \ge 1$ with $q_0 L$ Cartier. Choose a point $x \notin \operatorname{Supp} G$. For $q = q_0 t$, part 3 of Theorem P7.1.17 gives $h^0(X, qL) = (L^n) q^n / n! + O(q^{n-1})$ as $t \to \infty$. Vanishing to order at least $nq + 1$ at the smooth point $x$ imposes at most $\dim \mathcal{O}_{X,x} / \mathfrak{m}_x^{nq+1} = \binom{nq + n}{n} = n^n q^n / n! + O(q^{n-1})$ linear conditions. Since $(L^n) > n^n$, for $t$ large there is $M \in |qL|$ with $\operatorname{mult}_x M \ge nq + 1$. Fix this $q$ and $M$.

*Step 3: the threshold.* Let $f \colon Y \to X$ and $P_A$ be given by Lemma 7.1.2 for $\Delta = 0$, $\mathfrak{b} = \mathcal{O}_X$, $H = A$ and $\Gamma = \operatorname{Supp} G \cup \operatorname{Supp} M$, with prime divisors $F_1, \dots, F_s$. Put
$$a_j = \operatorname{mult}_{F_j}(K_{Y/X} + f^* G), \qquad r_j = \operatorname{mult}_{F_j} f^* M.$$
Then $a_j > -1$ by $(\ast)$, $r_j \ge 0$, and some $r_j > 0$. Let $c_0$ be as in Lemma 7.1.3 and $c_1 = n / (nq + 1) < 1/q$. On $V = X \setminus \operatorname{Supp} G$, an open set containing $x$, the exceptional divisor $E_x$ of the blow-up of $x$ has $a(E_x, V, c_1 M) = n - 1 - c_1 \operatorname{mult}_x M \le -1$ by Lemma 4.1.20, so $(V, c_1 M|_V)$ is not klt. The restriction $f^{-1} V \to V$ is a log resolution of $(V, c_1 M|_V)$, and by Theorem 4.2.14 some $F_j$ meeting $f^{-1} V$ has $c_1 r_j - \operatorname{mult}_{F_j} K_{Y/X} \ge 1$. Since $f^* G = 0$ on $f^{-1} V$, this reads $1 + a_j \le c_1 r_j$, so $r_j > 0$ and $c_0 \le c_1 < 1/q$.

*Step 4: tie-breaking.* Put $\kappa_0 = 1 - c_0 q > 0$, $U = \kappa_0 f^* A$ and $P_0 = \kappa_0 P_A$, so $U - P_0 = \kappa_0 (f^* A - P_A)$ is ample. Lemma 7.1.3 with $\eta = c_0/2$ gives $c \in (c_0/2, c_0]$, $P = \sum_j p'_j F_j$ with $\kappa_0 f^* A - P$ ample, and $j_0$, with $F_0 = F_{j_0}$, $B = \sum_j b_j F_j = K_{Y/X} + f^* G - c f^* M - P$, and $A_Y$ and $\Theta$ as in that lemma. Since $M \sim_{\mathbb{Q}} q(eD + A)$, for every integer $b$
$$f^*(bD) + B - K_Y = f^*\bigl( (b - a) D + A \bigr) - c f^* M - P \sim_{\mathbb{Q}} f^*\bigl( (b - a - cqe) D \bigr) + (c_0 - c) q f^* A + (\kappa_0 f^* A - P).$$
For $b \ge b_1 = \lceil a + cqe \rceil$ this is a nef divisor plus an ample one, hence ample by part 3 of Theorem P7.3.12.

*Step 5: lifting from $F_0$.* Let $b \ge b_1$. The Cartier divisor $N = f^*(bD) + \lceil B \rceil = f^*(bD) + A_Y - F_0$ satisfies $N - (K_Y + \Theta) = f^*(bD) + B - K_Y$, which is ample, and $(Y, \Theta)$ is klt by part 2 of Lemma 7.1.3. By part 1 of Corollary 5.1.14, $H^1(Y, N) = 0$, and the sequence $0 \to \mathcal{O}_Y(N) \to \mathcal{O}_Y(N + F_0) \to \mathcal{O}_{F_0}(N + F_0) \to 0$ shows that
$$H^0(Y, f^*(bD) + A_Y) \to H^0(F_0, (f^*(bD) + A_Y)|_{F_0})$$
is surjective. On the smooth projective variety $F_0$ of dimension $n - 1 \ge 1$ put $D_0 = (f^* D)|_{F_0}$, which is nef and Cartier, and $G_0 = (B + F_0)|_{F_0}$, which has snc support and $\lceil G_0 \rceil = A_Y|_{F_0} \ge 0$ by part 3 of Lemma 7.1.3. By adjunction, $K_{F_0} = (K_Y + F_0)|_{F_0}$, so
$$b_1 D_0 + G_0 - K_{F_0} = \bigl( f^*(b_1 D) + B - K_Y \bigr)|_{F_0}$$
is ample. By induction, $H^0(F_0, b D_0 + \lceil G_0 \rceil) \neq 0$ for $b \gg 0$, and $b D_0 + \lceil G_0 \rceil = (f^*(bD) + A_Y)|_{F_0}$. So $H^0(Y, f^*(bD) + A_Y) \neq 0$ for $b \gg 0$.

*Step 6: descent to $X$.* By part 1 of Lemma 7.1.6, $H^0(Y, f^*(bD) + A_Y) \subseteq H^0(X, bD + f_* A_Y)$. Let $P$ be a prime divisor of $X$ with strict transform $F_j$ and coefficient $g_P$ in $G$. Then $a_j = g_P$, since $K_{Y/X}$ is exceptional. If $j = j_0$, the coefficient of $A_Y$ along $F_j$ is $0 \le \lceil g_P \rceil$; otherwise it is $\lceil b_j \rceil \le \lceil a_j \rceil = \lceil g_P \rceil$ by part 1 of Lemma 7.1.3. So $f_* A_Y \le \lceil G \rceil$ and $H^0(X, bD + \lceil G \rceil) \neq 0$ for $b \gg 0$.

*Corollary 7.1.8.* Replacing $a$ by $\lceil a \rceil$ keeps the hypothesis, since $(\lceil a \rceil - a) D$ is nef and a nef and big divisor plus a nef divisor is nef and big (Lemma P7.9.2). Let $f \colon Y \to X$ be a log resolution of $(X, \Delta)$ given by Lemma 7.1.2, and put $G = K_Y - f^*(K_X + \Delta) = \sum_j a_j F_j$. Since $(X, \Delta)$ is klt, every $a_j > -1$, so $\lceil G \rceil \ge 0$, and along the strict transform of a component of $\Delta$ the coefficient $a_j$ lies in $(-1, 0]$, so $\lceil G \rceil$ is $f$-exceptional. The divisor $f^* D$ is nef, and $a f^* D + G - K_Y = f^*(aD - (K_X + \Delta))$ is nef with $\bigl( f^*(aD - (K_X + \Delta)) \bigr)^n = \bigl( (aD - (K_X + \Delta))^n \bigr) > 0$ by Theorem P7.1.15 and Theorem P7.7.7, so it is big. Theorem 7.1.7 gives $H^0(Y, m f^* D + \lceil G \rceil) \neq 0$ for $m \gg 0$, and this is $H^0(X, mD)$ by part 2 of Lemma 7.1.6.

### Exercises

1. (A) Let $X$ be the blow-up of $\mathbb{P}^2$ at a point, with $h$ the pullback of a line and $e$ the exceptional curve, and $D = -e$. Show that $D - K_X = 3h - 2e$ is ample and $H^0(X, mD) = 0$ for every $m \ge 1$, so the hypothesis that $D$ is nef cannot be dropped.
2. (A) In Example 7.1.9 with $D$ of order $2$, check that $aD - K_X$ is not big for any $a$, and that $H^0(X, mD) \neq 0$ exactly for even $m$.
3. (A) Show that in Step 2 the inequality $((eD + A)^n) > n^n$ holds for every integer $e > n^{n-1} / (D \cdot A^{n-1})$.
4. (B) Let $(X, \Delta)$ be a projective klt pair and $D$ a Cartier divisor with $D \equiv 0$ and $-(K_X + \Delta)$ nef and big. Show, without resolution, that $h^0(X, mD) = \chi(X, mD)$ for every $m \in \mathbb{Z}$ and that this polynomial takes the value $1$ at $m = 0$. Deduce Corollary 7.1.8 for such $D$.
5. (B) Show that the conclusion of Theorem 7.1.7 holds for every $m \ge m_0$ with $m_0$ depending on $(X, D, G, a)$, and that in dimension $1$ one may take $m_0 = \lceil (g - \deg \lceil G \rceil) / \deg D \rceil$ when $\deg D > 0$.
6. (C) Let $X$ be smooth projective and $D$ a Cartier divisor with $D \equiv 0$ such that $aD + G - K_X$ is nef and big for some $G$ as in Theorem 7.1.7 with $\lceil G \rceil = 0$. Using Step 1 for $D$ and for $-D$, show that $mD \sim 0$ for all $m$ with $|m| \gg 0$, and deduce $D \sim 0$. (An effective divisor $E \neq 0$ has $(E \cdot A^{n-1}) > 0$ for $A$ ample.)

### Lean

The library has `MinimalModel.NonVanishing`, but it is a different statement: the non-vanishing conjecture, that $K_X + \Delta$ pseudo-effective on a projective lc pair implies $K_X + \Delta$ is $\mathbb{R}$-linearly equivalent to an effective divisor, as a statement without proof. Theorem 7.1.7 and Corollary 7.1.8 are not yet in Lean.

### Notes and history

Theorem 7.1.7 is Shokurov's (Sho85), proved as the first step towards the base point free theorem, which Kawamata had proved in Kaw85 under an additional hypothesis. The proof here follows KM98, Theorem 3.4, with the reduction of Step 0 and the descent of Step 6 written out. KMM87, Chapter 2, and Matsuki (Mat02) give the same argument with the threshold called the log canonical threshold. The generalisation to lc pairs with $K_X + \Delta$ pseudo-effective is the non-vanishing conjecture, open from dimension $4$ on; it is not used in this volume.
