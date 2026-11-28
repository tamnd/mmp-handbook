---
title: The volume of a divisor
nodes: []
sources: [Laz04, Fuj94, Har77]
reads_with: [Laz04:2.2.C, Laz04:11.4.A]
requires: [P3.6, P4.4, P5.1, P7.1, P7.2, P7.3, P7.4, P7.5, P7.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The volume of a divisor

### Statement

Throughout, $X$ is a projective variety over $k$ of dimension $n \geq 1$ and $h^0(L^m) = \dim_k H^0(X, L^m)$ for a line bundle $L$. A $\mathbb{Q}$-divisor is an element $D = \sum_i a_i D_i$ of $\operatorname{Div}(X) \otimes \mathbb{Q}$, with $a_i \in \mathbb{Q}$ and $D_i$ Cartier divisors; it is *effective* if $aD$ is an effective Cartier divisor for some integer $a \geq 1$, and two $\mathbb{Q}$-divisors are $\mathbb{Q}$-linearly equivalent if some positive multiples are linearly equivalent Cartier divisors.

**Definition P7.7.1 (volume).** The *volume* of a line bundle $L$ is
$$\operatorname{vol}(L) = \operatorname{vol}_X(L) = \limsup_{m \to \infty} \frac{h^0(X, L^m)}{m^n / n!}.$$
For a Cartier divisor $D$, $\operatorname{vol}(D) = \operatorname{vol}(\mathcal{O}_X(D))$. For a $\mathbb{Q}$-divisor $D$, $\operatorname{vol}(D) = \operatorname{vol}(aD) / a^n$ for any integer $a \geq 1$ with $aD$ a Cartier divisor; by part 2 of Proposition P7.7.3 this does not depend on $a$.

**Lemma P7.7.2 (twisting by a fixed bundle).** Let $L$ and $M$ be line bundles on $X$. There is a constant $C$ with
$$h^0(L^m \otimes M) \leq h^0(L^m) + C m^{n-1} \quad \text{for all } m \geq 1.$$
So $\limsup_m h^0(L^m \otimes M) / (m^n / n!) \leq \operatorname{vol}(L)$, with equality if $H^0(X, M) \neq 0$.

Lean: not in Lean as stated.

**Proposition P7.7.3 (first properties).** Let $L$ be a line bundle and $D$, $D'$ $\mathbb{Q}$-divisors on $X$.

1. $0 \leq \operatorname{vol}(L) < \infty$, and $\operatorname{vol}(L) > 0$ if and only if $L$ is big.
2. (Homogeneity.) $\operatorname{vol}(L^a) = a^n \operatorname{vol}(L)$ for every integer $a \geq 1$. Hence $\operatorname{vol}(D)$ is well defined, and $\operatorname{vol}(tD) = t^n \operatorname{vol}(D)$ for rational $t > 0$.
3. If $L$ is ample, $\operatorname{vol}(L) = (L^n)$. The same holds for an ample $\mathbb{Q}$-divisor.
4. (Monotonicity.) If $D' - D$ is effective, $\operatorname{vol}(D) \leq \operatorname{vol}(D')$. If $D$ and $D'$ are $\mathbb{Q}$-linearly equivalent, $\operatorname{vol}(D) = \operatorname{vol}(D')$.
5. (Birational invariance.) If $\mu \colon X' \to X$ is a birational morphism of projective varieties, $\operatorname{vol}_{X'}(\mu^* D) = \operatorname{vol}_X(D)$.

Lean: not in Lean as stated.

**Lemma P7.7.4 (numerically trivial twists).** There is a line bundle $B$ on $X$ such that $H^0(X, B \otimes N) \neq 0$ for every numerically trivial line bundle $N$ on $X$.

Lean: not in Lean as stated.

**Proposition P7.7.5 (numerical invariance).** If $D$ and $D'$ are numerically equivalent $\mathbb{Q}$-divisors, then $\operatorname{vol}(D) = \operatorname{vol}(D')$. So the volume is a function $\operatorname{vol} \colon N^1(X)_\mathbb{Q} \to \mathbb{R}_{\geq 0}$, with $\operatorname{vol}(t \xi) = t^n \operatorname{vol}(\xi)$ for rational $t > 0$.

Lean: not in Lean as stated.

For the next theorem fix very ample Cartier divisors $H_1, \dots, H_\rho$ whose classes form a basis of $N^1(X)$, which exist by the proof, and for $\xi = \sum_i x_i [H_i]$ put $\| \xi \| = \sum_i |x_i|$.

**Theorem P7.7.6 (continuity).**

1. For every integer $R \geq 1$ there is a constant $K_R$ such that $|\operatorname{vol}(\xi) - \operatorname{vol}(\xi')| \leq K_R \| \xi - \xi' \|$ for all rational classes $\xi$, $\xi'$ with $\| \xi \|, \| \xi' \| \leq R$.
2. The volume extends uniquely to a continuous function $\operatorname{vol} \colon N^1(X) \to \mathbb{R}_{\geq 0}$, and $\operatorname{vol}(t \xi) = t^n \operatorname{vol}(\xi)$ for all real $t > 0$.
3. If $\xi \in N^1(X)$ and $\varepsilon \in \overline{\operatorname{Eff}}(X)$, then $\operatorname{vol}(\xi + \varepsilon) \geq \operatorname{vol}(\xi)$.
4. $\operatorname{vol}(\xi) > 0$ if and only if $\xi \in \operatorname{Big}(X)$.
5. If $\mu \colon X' \to X$ is a birational morphism of projective varieties, $\operatorname{vol}(\mu^* \xi) = \operatorname{vol}(\xi)$ for every $\xi \in N^1(X)$.

Lean: not in Lean as stated.

**Theorem P7.7.7 (the volume of a nef class).** If $\xi \in N^1(X)$ is nef, then $\operatorname{vol}(\xi) = (\xi^n)$. In particular a nef class is big if and only if $(\xi^n) > 0$.

Lean: not in Lean as stated.

**Theorem P7.7.8 (Fujita's approximation theorem).** Let $k$ have characteristic $0$ and let $D$ be a big $\mathbb{Q}$-divisor on $X$. For every $\varepsilon > 0$ there are a birational morphism $\mu \colon X' \to X$ from a smooth projective variety and $\mathbb{Q}$-divisors $A$, $E$ on $X'$ with $A$ ample and $E$ effective, such that
$$\mu^* D \equiv A + E \qquad \text{and} \qquad \operatorname{vol}(D) - \varepsilon < (A^n) \leq \operatorname{vol}(D).$$

Lean: not in Lean as stated.

### Proof in words

A twist by a fixed line bundle changes $h^0(L^m)$ by at most a constant times $m^{n-1}$, because the difference is controlled by sections on a fixed divisor, where Lemma P7.5.1 gives the bound in one dimension less. This gives homogeneity, once Kodaira's lemma provides sections of all large powers of a big bundle, and numerical invariance, once a single bundle $B$ dominates every numerically trivial twist; that bundle comes from Fujita's vanishing theorem and is cited.

Continuity comes from the same estimate on a fixed divisor. Writing classes in a basis of very ample divisors, raising one coordinate by $t$ raises the volume by at most a constant times $t$, the constant depending only on a bound for the coordinates, and lowering a coordinate lowers the volume because the volume is monotone. So the volume is locally Lipschitz on rational classes and extends to $N^1(X)$. On ample classes it is the top self-intersection, and by continuity it is on the closure, the nef cone. Fujita's theorem, which is stated, says that the volume of a big class is approximated by top self-intersections of ample classes on birational models.

### Examples

**Example P7.7.9 (curves and projective space).** On a smooth projective curve $C$, a $\mathbb{Q}$-divisor of degree $d$ has $\operatorname{vol}(D) = \max(d, 0)$: for an integral $D$ with $d > 0$, Example P7.5.7 gives $md + 1 - g \leq h^0(mD) \leq md + 1$, and for $d \leq 0$, $h^0(mD) \leq 1$. On $\mathbb{P}^n$, $h^0(\mathcal{O}(md)) = \binom{md + n}{n}$ for $d \geq 0$, so $\operatorname{vol}(\mathcal{O}(d)) = d^n$, and the volume is $0$ for $d < 0$. In both cases the volume is the function $t \mapsto \max(t, 0)^n$ on $N^1 = \mathbb{R}$, continuous but not a polynomial.

**Example P7.7.10 (products of projective spaces).** Let $X = \mathbb{P}^a \times \mathbb{P}^b$, $n = a + b$, with $H_1$, $H_2$ as in Proposition P7.2.21, and write classes as $x H_1 + y H_2$. The curves $\ell_1$ and $\ell_2$ move in families covering $X$, so by part 2 of Proposition P7.4.15 every pseudo-effective class has $x, y \geq 0$, and these classes are nef by Example P7.3.15. So $\overline{\operatorname{Eff}}(X) = \operatorname{Nef}(X) = \{ x, y \geq 0 \}$ and $\operatorname{Big}(X) = \operatorname{Amp}(X) = \{ x, y > 0 \}$. A general intersection of $a$ pullbacks of hyperplanes of $\mathbb{P}^a$ and $b$ pullbacks of hyperplanes of $\mathbb{P}^b$ is one reduced point, while $a + 1$ general hyperplanes of $\mathbb{P}^a$ have empty intersection, so by part 3 of Proposition P7.1.14, $(H_1^i \cdot H_2^j)$ is $1$ for $(i, j) = (a, b)$ and $0$ otherwise when $i + j = n$. By Theorem P7.7.7,
$$\operatorname{vol}(x H_1 + y H_2) = \binom{a + b}{a} x^a y^b \quad \text{for } x, y \geq 0,$$
and the volume is $0$ elsewhere. For $a = b = 1$ this is $2xy$, the self-intersection on $\mathbb{P}^1 \times \mathbb{P}^1$.

**Example P7.7.11 (the blow-up of a point).** Let $\pi \colon X = \operatorname{Bl}_p \mathbb{P}^n \to \mathbb{P}^n$, $n \geq 2$, and write classes as $x H - y E$. By Proposition P7.4.18 and Example P7.5.15, $\operatorname{Nef}(X) = \{ 0 \leq y \leq x \}$ and $\operatorname{Big}(X) = \{ x > 0, \ y < x \}$. Then
$$\operatorname{vol}(xH - yE) = \begin{cases} x^n - y^n & \text{if } 0 \leq y \leq x, \\ x^n & \text{if } x \geq 0, \ y \leq 0, \\ 0 & \text{otherwise.} \end{cases}$$
On the nef cone this is Theorem P7.7.7 with Example P7.1.26. Off the pseudo-effective cone it is part 4 of Theorem P7.7.6. For $y \leq 0$, take integers $x \geq 0$ and $c \geq 1$. By part 1 of Proposition P7.1.23, $\mathcal{O}_E(E) \cong \mathcal{O}_{\mathbb{P}^{n-1}}(-1)$, and $\mathcal{O}_E(H)$ is trivial because $\pi$ maps $E$ to a point. So the sequence
$$0 \to \mathcal{O}_X(xH + (c - 1)E) \to \mathcal{O}_X(xH + cE) \to \mathcal{O}_{\mathbb{P}^{n-1}}(-c) \to 0$$
gives $h^0(xH + cE) = h^0(xH + (c - 1)E)$, and by induction $h^0(xH + cE) = h^0(xH) = \binom{x + n}{n}$, using Proposition P7.6.12. Applied to $m(xH + cE)$ this gives $\operatorname{vol}(xH + cE) = x^n$, and the rational and real cases follow by homogeneity and continuity. The volume is not a polynomial on $\operatorname{Big}(X)$: it is given by two polynomials on the two chambers separated by the ray of $H$, and the two agree to first order along that ray.

### Proof

*Lemma P7.7.2.* Let $A$ be ample. By part 2 of Definition P3.6.22, applied to $\mathcal{O}_X$ and to $M^{-1}$, there is $r \geq 1$ such that $H = A^r$ and $H \otimes M^{-1}$ are generated by global sections; both are nonzero sheaves, so they have nonzero sections $\sigma$ and $\tau$. Since $X$ is integral, multiplication by $\tau$ embeds $H^0(L^m \otimes M)$ in $H^0(L^m \otimes H)$. Let $E$ be the effective Cartier divisor of $\sigma$; it is a proper closed subscheme, so $\dim \operatorname{Supp} \mathcal{O}_E \leq n - 1$. The exact sequence $0 \to L^m \to L^m \otimes H \to L^m \otimes H \otimes \mathcal{O}_E \to 0$ gives
$$h^0(L^m \otimes M) \leq h^0(L^m \otimes H) \leq h^0(L^m) + h^0(\mathcal{O}_E \otimes L^m \otimes H),$$
and Lemma P7.5.1, applied to $\mathcal{F} = \mathcal{O}_E$ on $X$ with $d = n - 1$, bounds the last term by $C m^{n-1}$. Dividing by $m^n / n!$ gives the inequality of limits superior. If $M$ has a nonzero section, multiplication by it gives $h^0(L^m) \leq h^0(L^m \otimes M)$, hence equality.

*Proposition P7.7.3.* Part 1. By Lemma P7.5.1 with $\mathcal{F} = \mathcal{O}_X$, $h^0(L^m) \leq C m^n$, so $\operatorname{vol}(L) \leq n! \, C$. The second statement is Definition P7.5.2.

Part 2. Along the subsequence of multiples of $a$,
$$\frac{h^0(L^{am})}{m^n / n!} = a^n \, \frac{h^0(L^{am})}{(am)^n / n!},$$
so $\operatorname{vol}(L^a) \leq a^n \operatorname{vol}(L)$. For the reverse inequality, if $L$ is not big both sides are $0$ by part 1 and part 3 of Corollary P7.5.4. If $L$ is big, part 2 of Corollary P7.5.4 gives $p$ with $H^0(L^r) \neq 0$ for all $r \geq p$. For $m \geq 1$ choose $r_m \in \{ p, \dots, p + a - 1 \}$ with $a$ dividing $m + r_m$, and put $q_m = (m + r_m) / a$. Multiplication by a nonzero section of $L^{r_m}$ gives $h^0(L^m) \leq h^0((L^a)^{q_m})$, so
$$\frac{h^0(L^m)}{m^n / n!} \leq \Bigl( \frac{q_m}{m} \Bigr)^n \frac{h^0((L^a)^{q_m})}{q_m^n / n!}.$$
As $m \to \infty$, $q_m / m \to 1 / a$ and $q_m \to \infty$, each value being taken at most $a$ times, so $\operatorname{vol}(L) \leq a^{-n} \operatorname{vol}(L^a)$. If $aD$ and $bD$ are Cartier, then $\operatorname{vol}(abD) = b^n \operatorname{vol}(aD) = a^n \operatorname{vol}(bD)$, so $\operatorname{vol}(aD) / a^n = \operatorname{vol}(bD) / b^n$, and the formula for $tD$ follows.

Part 3. By part 3 of Theorem P7.1.17 with $\mathcal{F} = \mathcal{O}_X$, $h^0(L^m) = \frac{(L^n)}{n!} m^n + O(m^{n-1})$. For an ample $\mathbb{Q}$-divisor $D$ with $aD$ an ample Cartier divisor, $\operatorname{vol}(D) = (aD)^n / a^n = (D^n)$.

Part 4. Choose $a$ with $aD$, $aD'$ Cartier and $aD' - aD = G$ effective. Multiplication by $s_G^m$ embeds $H^0(maD)$ in $H^0(maD')$, so $\operatorname{vol}(aD) \leq \operatorname{vol}(aD')$, and part 2 gives the claim. Linearly equivalent Cartier divisors have isomorphic sheaves, so the second statement follows from part 2.

Part 5. By part 2 it suffices to treat a line bundle $L$. Since $X'$ is projective, $\mu$ is projective and $\mu_* \mathcal{O}_{X'}$ is coherent by Theorem P4.4.8. The map $\mathcal{O}_X \to \mu_* \mathcal{O}_{X'}$ is injective because $\mu$ is dominant and $X'$ is integral, and its cokernel $\mathcal{Q}$ is coherent and vanishes on a dense open subset of $X$ over which $\mu$ is an isomorphism, so $\dim \operatorname{Supp} \mathcal{Q} \leq n - 1$. By Proposition P4.4.10, $H^0(X', \mu^* L^m) = H^0(X, L^m \otimes \mu_* \mathcal{O}_{X'})$, so
$$h^0(X, L^m) \leq h^0(X', \mu^* L^m) \leq h^0(X, L^m) + h^0(X, \mathcal{Q} \otimes L^m),$$
and the last term is at most $C m^{n-1}$ by Lemma P7.5.1. If $X$ is normal, Proposition P7.6.12 gives equality of the first two terms directly.

*Lemma P7.7.4.* This is Lazarsfeld, Lemma 2.2.42 (Laz04), not proved here. In outline: let $A$ be very ample. Fujita's vanishing theorem (Laz04, Theorem 1.4.35), valid over any algebraically closed field, gives $r$ with $H^i(X, A^r \otimes P) = 0$ for all $i > 0$ and all nef line bundles $P$, in particular for all numerically trivial $P$. So $h^0(A^r \otimes N) = \chi(A^r \otimes N)$, and the Euler characteristic of a coherent sheaf does not change under a twist by a numerically trivial line bundle, so $h^0(A^r \otimes N) = \chi(A^r) = h^0(A^r) > 0$. Take $B = A^r$.

*Proposition P7.7.5.* Choose $a$ with $aD$ and $aD'$ Cartier; by part 2 of Proposition P7.7.3 it suffices to show $\operatorname{vol}(L') = \operatorname{vol}(L)$ for line bundles $L \equiv L'$. Let $N = L' \otimes L^{-1}$, which is numerically trivial, and $B$ as in Lemma P7.7.4. For every $m$, $N^{-m}$ is numerically trivial, so $B \otimes N^{-m}$ has a nonzero section, and multiplication by it embeds $H^0(L'^m)$ in $H^0(L'^m \otimes B \otimes N^{-m}) = H^0(L^m \otimes B)$. By Lemma P7.7.2, $\operatorname{vol}(L') \leq \operatorname{vol}(L)$, and by symmetry the two are equal. Every rational class is the class of a $\mathbb{Q}$-divisor by part 3 of Corollary P7.2.16, so the volume is defined on $N^1(X)_\mathbb{Q}$, and homogeneity is part 2 of Proposition P7.7.3.

*Theorem P7.7.6.* The divisors $H_i$. By part 1 of Theorem P7.3.12, $\operatorname{Amp}(X)$ is open, and it is nonempty since $X$ is projective, so it spans $N^1(X)$. It is spanned by classes of ample line bundles, so some ample line bundles $A_1, \dots, A_\rho$ have classes forming a basis. By Theorem P3.6.25 some powers $A_i^r$ are very ample, and their classes still form a basis. A very ample line bundle has a nonzero section; let $H_i$ be its divisor. For $x \in \mathbb{Q}^\rho$ put $D_x = \sum_i x_i H_i$. By Proposition P7.7.5, $\operatorname{vol}(\sum_i x_i [H_i]) = \operatorname{vol}(D_x)$.

Part 1. Fix $R$, let $M = (R + 1) \sum_l H_l$, and fix $j$. Applying Lemma P7.5.1 to $\mathcal{O}_{H_j}$ gives $C_j$ with $h^0(\mathcal{O}_{H_j} \otimes \mathcal{O}_X(M)^q) \leq C_j q^{n-1}$ for $q \geq 1$. First claim: for rational $x$ with $|x_l| \leq R$ for all $l$ and rational $t \in [0, 1]$,
$$\operatorname{vol}(D_x + t H_j) \leq \operatorname{vol}(D_x) + n! \, C_j \, t.$$
Choose $p \geq 1$ with $px$ integral and $q = pt$ integral, and put $G = p D_x$. For $m \geq 1$ and $1 \leq i \leq mq$ the exact sequence
$$0 \to \mathcal{O}_X(mG + (i - 1) H_j) \to \mathcal{O}_X(mG + i H_j) \to \mathcal{O}_{H_j}(mG + i H_j) \to 0$$
gives $h^0(mG + mq H_j) \leq h^0(mG) + \sum_{i = 1}^{mq} h^0(\mathcal{O}_{H_j}(mG + i H_j))$. The divisor $mpM - mG - iH_j$ is a combination of the $H_l$ with nonnegative integer coefficients, since $mp(R + 1 - x_l) \geq mp$ for every $l$ and $i \leq mq \leq mp$. Each $H_l$ is very ample, and $k$ is infinite, so $\mathcal{O}_X(H_l)$ has a section that vanishes at none of the finitely many associated points of $\mathcal{O}_{H_j}$; the corresponding product of such sections is a section of $\mathcal{O}_X(mpM - mG - iH_j)$ that is a nonzerodivisor on $\mathcal{O}_{H_j}$. Multiplication by it embeds $H^0(\mathcal{O}_{H_j}(mG + iH_j))$ in $H^0(\mathcal{O}_{H_j} \otimes \mathcal{O}_X(M)^{mp})$, of dimension at most $C_j (mp)^{n-1}$. Hence
$$h^0(m(G + qH_j)) \leq h^0(mG) + mq \, C_j \, (mp)^{n-1}.$$
Dividing by $(mp)^n / n!$ and taking limits superior gives $\operatorname{vol}(G + qH_j) / p^n \leq \operatorname{vol}(G) / p^n + n! \, C_j \, q / p$, which is the claim. Let $K_R = n! \max_j C_j$.

Second claim: if $x$, $y$ are rational with $|x_l|, |y_l| \leq R$ and $x_l \leq y_l$ for all $l$, then $0 \leq \operatorname{vol}(D_y) - \operatorname{vol}(D_x) \leq K_R \sum_l (y_l - x_l)$. The lower bound is part 4 of Proposition P7.7.3, since $D_y - D_x$ is effective. For the upper bound, pass from $x$ to $y$ by raising one coordinate at a time in steps of length at most $1$, all intermediate points lying in the same box, and add the first claim over the steps.

For arbitrary rational $\xi = [D_x]$, $\xi' = [D_y]$ with $\| \xi \|, \| \xi' \| \leq R$, let $z$ and $w$ be the coordinatewise minimum and maximum of $x$ and $y$, again in the box. By monotonicity $\operatorname{vol}(D_z) \leq \operatorname{vol}(D_x), \operatorname{vol}(D_y) \leq \operatorname{vol}(D_w)$, so
$$|\operatorname{vol}(D_x) - \operatorname{vol}(D_y)| \leq \operatorname{vol}(D_w) - \operatorname{vol}(D_z) \leq K_R \sum_l (w_l - z_l) = K_R \| \xi - \xi' \|.$$

Part 2. By part 1 the volume is uniformly continuous on the rational points of each bounded set, which are dense in it (Definition P7.2.15), so it has a unique continuous extension to $N^1(X)$, and the extension does not depend on the basis. Homogeneity for real $t$ follows from the rational case by continuity in $t$ and $\xi$.

Part 3. The cone $\operatorname{Eff}(X)$ is the set of nonnegative real combinations of classes of effective Cartier divisors, so the classes of effective $\mathbb{Q}$-divisors are dense in it, and hence in $\overline{\operatorname{Eff}}(X)$. For rational $\xi$ and the class $\varepsilon$ of an effective $\mathbb{Q}$-divisor the inequality is part 4 of Proposition P7.7.3 with Proposition P7.7.5. The general case follows by continuity.

Part 4. Let $\alpha$ be ample. If $\xi$ is big, then $\xi - \delta \alpha \in \operatorname{Big}(X)$ for small $\delta > 0$, since $\operatorname{Big}(X)$ is open (part 1 of Proposition P7.5.6), so the open set $\operatorname{Big}(X) \cap (\xi - \operatorname{Amp}(X))$ is not empty and contains a rational class $\zeta$. It is the class of a big $\mathbb{Q}$-divisor by part 2 of Proposition P7.5.6, so $\operatorname{vol}(\zeta) > 0$ by part 1 of Proposition P7.7.3, and $\xi - \zeta$ is ample, hence pseudo-effective by part 1 of Proposition P7.4.15. Part 3 gives $\operatorname{vol}(\xi) \geq \operatorname{vol}(\zeta) > 0$. Conversely let $\xi \notin \operatorname{Big}(X)$. If $\xi$ is not pseudo-effective, it has a neighbourhood of classes that are not pseudo-effective, hence not big by part 5 of Theorem P7.5.12, and the volume vanishes on the rational ones; so $\operatorname{vol}(\xi) = 0$. If $\xi$ is pseudo-effective, then $\xi - t\alpha$ is not pseudo-effective for $t > 0$, since otherwise $\xi = (\xi - t\alpha) + t\alpha$ would be big by part 3 of Theorem P7.5.12. So $\operatorname{vol}(\xi - t\alpha) = 0$ and $\operatorname{vol}(\xi) = \lim_{t \to 0} \operatorname{vol}(\xi - t\alpha) = 0$.

Part 5. The map $\mu^* \colon N^1(X) \to N^1(X')$ is linear, hence continuous, and both sides agree on rational classes by part 5 of Proposition P7.7.3 and Proposition P7.7.5.

*Theorem P7.7.7.* Let $\xi \in \operatorname{Amp}(X)$ be rational. Some multiple $a\xi$ is the class of a line bundle $L$, which is ample by part 2 of Theorem P7.3.12, and part 3 of Proposition P7.7.3 gives $\operatorname{vol}(\xi) = (L^n) / a^n = (\xi^n)$. The rational classes are dense in the open set $\operatorname{Amp}(X)$, and both $\operatorname{vol}$ and $\xi \mapsto (\xi^n)$ are continuous (part 2 of Theorem P7.7.6 and part 1 of Definition P7.3.8), so they agree on $\operatorname{Amp}(X)$, and hence on its closure $\operatorname{Nef}(X)$ by part 4 of Theorem P7.3.12. The last statement is part 4 of Theorem P7.7.6.

*Theorem P7.7.8.* This is Fujita's theorem (Fuj94), not proved here; Lazarsfeld, Theorem 11.4.4 (Laz04), gives a proof with multiplier ideals, and the variety $X'$ may be taken smooth by resolution of singularities. The upper bound $(A^n) \leq \operatorname{vol}(D)$ holds for every such decomposition: by Theorem P7.7.7, part 3 of Theorem P7.7.6 and part 5 of Theorem P7.7.6, $(A^n) = \operatorname{vol}(A) \leq \operatorname{vol}(A + E) = \operatorname{vol}(\mu^* D) = \operatorname{vol}(D)$.

### Exercises

1. (A) Show that the volume of a $\mathbb{Q}$-divisor of degree $d$ on a smooth projective curve is $\max(d, 0)$, and that on $\mathbb{P}^1 \times \mathbb{P}^1$ the volume of the class $(x, y)$ is $2 \max(x, 0) \max(y, 0)$.
2. (A) On $\operatorname{Bl}_p \mathbb{P}^2$, draw the chambers of Example P7.7.11 and check that the volume is continuous along the rays of $H$ and $H - E$. Show that it is not a polynomial on $\operatorname{Big}(X)$, and that its partial derivatives are continuous on $\operatorname{Big}(X)$.
3. (A) On $\operatorname{Bl}_p \mathbb{P}^3$, show that $(H + E)^3 = 2$ and $\operatorname{vol}(H + E) = 1$. So $\operatorname{vol}(D) < (D^n)$ can happen for a big divisor that is not nef.
4. (B) Let $\xi$ be a big class and $\alpha$ an ample class, and let $c > 0$ be such that $\xi - c \alpha$ is pseudo-effective. Show that $(1 + t/c)\xi - (\xi + t\alpha)$ and $(\xi - t\alpha) - (1 - t/c)\xi$ are pseudo-effective for $0 \leq t \leq c$, and deduce $(1 - t/c)^n \operatorname{vol}(\xi) \leq \operatorname{vol}(\xi \pm t\alpha) \leq (1 + t/c)^n \operatorname{vol}(\xi)$. This gives a second proof of continuity on the big cone.
5. (B) Let $\xi$, $\eta$ be nef classes. Show that $(\xi^i \cdot \eta^{n-i}) \geq 0$ for all $i$, by approximating with ample classes and cutting by divisors, and deduce $\operatorname{vol}(\xi + \eta) \geq \operatorname{vol}(\xi) + \operatorname{vol}(\eta)$.
6. (C) Assume Theorem P7.7.8 and let $L$ be a big line bundle. Show that the limit superior in Definition P7.7.1 is a limit. Choose $a$ with $aA$ integral and compare $h^0(L^{am})$ from below with $h^0(maA)$, up to a numerically trivial twist handled by Lemma P7.7.4; then treat the values of $m$ not divisible by $a$ with part 2 of Corollary P7.5.4.

### Lean

The project library defines `MinimalModel.h0`, `MinimalModel.IsBig` and `MinimalModel.IsPseudoEffective`, the nef cone `MinimalModel.nefCone` and the effective cone `MinimalModel.effCone`. It has no volume of a divisor, so Definition P7.7.1 and the results of this section are not stated there, and Fujita's approximation theorem is not recorded as a hypothesis. Mathlib has no volume of a line bundle. The handbook adds no `MinimalModel` node here.

### Notes and history

The volume appears in Fujita's work on Zariski decompositions and in the study of the growth of $h^0(mD)$ going back to Zariski; the systematic treatment of the volume as a function on $N^1(X)$ is Lazarsfeld's, Section 2.2.C (Laz04), whose proofs of homogeneity and numerical invariance are followed here. The proof of continuity through very ample coordinates and a fixed divisor is a variant of Lazarsfeld's Theorem 2.2.44, written to use only Lemma P7.5.1. The literature state is theorem. Everything in this section except Theorem P7.7.8 holds over any algebraically closed field; Fujita proved the approximation theorem in characteristic $0$ (Fuj94), and Takagi later extended it to positive characteristic. The volume is in fact differentiable on the big cone, a theorem of Boucksom, Favre and Jonsson, and this differentiability is the step that replaces analysis in the later proofs of Theorem P7.5.21 mentioned in Section 5.3.
