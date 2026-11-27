---
title: The cone theorem for surface pairs
nodes: []
sources: [KM98, Mat02, Mum61]
reads_with: [KM98:ch3, Mat02:ch1]
requires: [P5.5, P5.8, P5.12, 2.3, 3.3, 3.5, 4.2, 4.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The cone theorem for surface pairs

### Statement

The cone theorem for a smooth projective surface, Theorem P5.12.14, describes the $K$-negative part of the cone of curves. This section proves the same description for a pair $(X, \Delta)$ on a normal $\mathbb{Q}$-factorial surface. The proof does not repeat the bend-and-break argument. It moves the question to the minimal resolution, applies Theorem P5.12.14 there, and pushes the answer down. The rays that the boundary makes negative are found by hand: they are spanned by components of $\Delta$ of negative square.

Throughout the chapter $k$ is an algebraically closed field of characteristic $0$, and a *surface* is a normal projective surface over $k$. For a surface $X$, $f \colon Y \to X$ denotes its minimal resolution (Definition 4.3.4), and $E_1, \dots, E_r$ are all the exceptional curves of $f$. Intersection numbers of Weil divisors on $X$ are Mumford's numbers of Corollary P5.8.5: $D \cdot D' = f^*D \cdot f^*D'$, where $f^*$ is Mumford's pullback. Definition 2.3.1 and Theorem 2.3.4 develop this intersection theory for normal surfaces; only the facts listed in Lemma 2.4.2 are used here. For an integral curve $C \subset X$, $\tilde C = f^{-1}_* C$ is its strict transform, and $f^*C = \tilde C + \sum_i c_i E_i$ with every $c_i \ge 0$, by Corollary P5.8.5.

**Definition 2.4.1 (surface pairs and their cones).**

1. A *surface pair* $(X, \Delta)$ is a $\mathbb{Q}$-factorial surface $X$ with a $\mathbb{Q}$-divisor $\Delta = \sum_j \delta_j D_j$ whose coefficients satisfy $0 \le \delta_j \le 1$, a *boundary*. Since $X$ is $\mathbb{Q}$-factorial, $K_X + \Delta$ is $\mathbb{Q}$-Cartier, and the pair is klt or lc in the sense of Definition 4.2.1.
2. $N^1(X)$ is the real vector space of $\mathbb{R}$-Weil divisors on $X$ modulo numerical equivalence for Mumford's product: $D \equiv 0$ if $D \cdot D' = 0$ for every Weil divisor $D'$. Its dimension is the *Picard number* $\rho(X)$. An integral curve is a Weil divisor, so curves have classes in $N^1(X)$, and Mumford's product is a nondegenerate symmetric bilinear form on $N^1(X)$.
3. $NE(X) \subseteq N^1(X)$ is the convex cone spanned by the classes of integral curves, and $\overline{NE}(X)$ is its closure. For a class $D$, $\overline{NE}(X)_{D \ge 0} = \{ z \in \overline{NE}(X) : D \cdot z \ge 0 \}$. A class $D$ is *nef* if $D \cdot z \ge 0$ on $\overline{NE}(X)$. *Extremal rays* are defined as in Definition P5.12.1, and a ray $R$ is $D$-negative if $D \cdot z < 0$ for $z \in R \setminus \{0\}$.

For a Cartier divisor $D$, Corollary P5.8.5 says that $f^*D$ is the usual pullback, so $D \cdot C = \deg(\mathcal{O}_X(D)|_C)$ for an integral curve $C$, by the projection formula on $Y$. Since $X$ is $\mathbb{Q}$-factorial, every Weil divisor has a multiple that is Cartier. So $N^1(X)$ is the usual space of $\mathbb{R}$-Cartier divisors modulo numerical equivalence, and Mumford's pairing identifies it with the space $N_1(X)$ of curves of KM98, Chapter 1. Under this identification $NE(X)$ is the cone of curves of KM98.

**Lemma 2.4.2 (the dictionary with the minimal resolution).** Let $X$ be a $\mathbb{Q}$-factorial surface with minimal resolution $f \colon Y \to X$, and $H$ an ample Cartier divisor on $X$.

1. Mumford's pullback induces an injective linear map $f^* \colon N^1(X) \to N^1(Y)$ with $f^*x \cdot f^*x' = x \cdot x'$. Its image is the orthogonal complement of $E_1, \dots, E_r$. The classes $E_i$ are linearly independent, and $\rho(Y) = \rho(X) + r$. In particular $\rho(X)$ is finite.
2. The pushforward of divisors induces a linear map $f_* \colon N^1(Y) \to N^1(X)$ with $f_* f^* = \mathrm{id}$ and $f^*x \cdot z = x \cdot f_* z$ for $x \in N^1(X)$ and $z \in N^1(Y)$. It satisfies $f_* NE(Y) = NE(X)$ and $f_* \overline{NE}(Y) \subseteq \overline{NE}(X)$, and $f^* \overline{NE}(X) \subseteq \overline{NE}(Y)$. A class $x$ is nef on $X$ if and only if $f^*x$ is nef on $Y$.
3. The form on $N^1(X)$ has signature $(1, \rho(X) - 1)$. Every nef class $x$ has $x^2 \ge 0$. The positive cone $\mathcal{P}(X) = \{ x : x^2 > 0, \ H \cdot x > 0 \}$ is open and contained in $\overline{NE}(X)$.
4. Distinct integral curves $C, C'$ on $X$ satisfy $C \cdot C' \ge 0$, and $C \cdot C' > 0$ if $C \cap C' \ne \emptyset$.
5. $H \cdot y > 0$ for every $y \in \overline{NE}(X) \setminus \{0\}$. There is a constant $c > 0$, for a fixed norm on $N^1(X)$, with $|y| \le c \, H \cdot y$ on $\overline{NE}(X)$, so the slice $\Sigma_H = \{ y \in \overline{NE}(X) : H \cdot y = 1 \}$ is compact.
6. There is an integer $d \ge 1$ such that $f^*C$ has coefficients in $\frac1d \mathbb{Z}$ for every integral curve $C$. The set $\Lambda = \{ x \in N^1(X) : f^*x \in \frac1d \operatorname{Num}(Y) \}$ is a discrete subgroup of $N^1(X)$ that contains the class of every integral curve, where $\operatorname{Num}(Y) \subset N^1(Y)$ is the lattice of classes of Cartier divisors.
7. Write $K_Y = f^*K_X + \sum_i a_i E_i$. Then every $a_i \le 0$, $K_Y \cdot f^*x = K_X \cdot x$ for every $x$, and for every integral curve $C$ on $X$, $K_X \cdot C \ge K_Y \cdot \tilde C$ and $C^2 \ge \tilde C^2$. If $(X, \Delta)$ is a surface pair, the divisor $\Delta_Y$ defined by $K_Y + \Delta_Y = f^*(K_X + \Delta)$ is effective, and the coefficient of $\tilde C$ in $\Delta_Y$ is the coefficient of $C$ in $\Delta$.

Lean: not yet in Lean.

**Lemma 2.4.3 (curves of negative square on a singular surface).** Let $X$ be a $\mathbb{Q}$-factorial surface and $R = \mathbb{R}_{\ge 0} x$ an extremal ray of $\overline{NE}(X)$.

1. If $C$ is an integral curve with $C^2 < 0$, then $\overline{NE}(X) = \mathbb{R}_{\ge 0}[C] + \overline{NE}(X)_{C \ge 0}$, the ray $\mathbb{R}_{\ge 0}[C]$ is extremal, and $C$ is the only integral curve with class in it.
2. If $C$ is an integral curve with $C \cdot x < 0$, then $C^2 < 0$ and $R = \mathbb{R}_{\ge 0}[C]$.
3. If $x^2 < 0$, then $R = \mathbb{R}_{\ge 0}[C]$ for an integral curve $C$ with $C^2 < 0$.
4. If $x^2 > 0$, then $\rho(X) = 1$.

Lean: not yet in Lean.

**Theorem 2.4.4 (the cone theorem for surface pairs).** Let $(X, \Delta)$ be a surface pair, $H$ an ample Cartier divisor on $X$, and $\{R_i\}_{i \in I}$ the set of $(K_X + \Delta)$-negative extremal rays of $\overline{NE}(X)$.

1. Each $R_i$ is spanned by the class of a rational curve $\Gamma_i$ with $0 < -(K_X + \Delta) \cdot \Gamma_i \le 3$. If $\Delta \cdot \Gamma_i < 0$, then $\Gamma_i$ is a component of $\Delta$ with $\Gamma_i^2 < 0$ and $-(K_X + \Delta) \cdot \Gamma_i \le 2$.
2. $\overline{NE}(X) = \overline{NE}(X)_{K_X + \Delta \ge 0} + \sum_{i \in I} \mathbb{R}_{\ge 0}[\Gamma_i]$.
3. For every $\varepsilon > 0$ only finitely many $i$ have $(K_X + \Delta + \varepsilon H) \cdot \Gamma_i < 0$, and $\overline{NE}(X) = \overline{NE}(X)_{K_X + \Delta + \varepsilon H \ge 0} + \sum_{(K_X + \Delta + \varepsilon H) \cdot \Gamma_i < 0} \mathbb{R}_{\ge 0}[\Gamma_i]$.
4. $K_X + \Delta$ is nef if and only if $I$ is empty.

Lean: not yet in Lean.

The theorem does not assume that $(X, \Delta)$ is klt or lc: $\mathbb{Q}$-factoriality and the bound $\delta_j \le 1$ on the coefficients are enough. The singularities enter in Section 2, where the rays are contracted.

### Proof in words

Every question about curves on $X$ becomes a question on the smooth surface $Y$. Pulling back is an isometry onto the orthogonal complement of the exceptional curves, and pushing forward undoes it. On $Y$ the canonical class differs from $f^*K_X$ by $\sum a_i E_i$ with $a_i \le 0$, because the resolution is minimal. A $(K_X + \Delta)$-negative ray $R$ has one of two kinds. If $\Delta$ is negative on $R$, some component $D$ of $\Delta$ is negative on $R$, and the negativity of $D$ on its own ray forces $R = \mathbb{R}_{\ge 0}[D]$. The adjunction formula on $Y$ then bounds $-(K_X + \Delta) \cdot D$ by $2$. If $\Delta$ is not negative on $R$, then $K_X$ is, and the pullback of a generator is $K_Y$-negative. The cone theorem on $Y$ writes it as a $K_Y$-nonnegative class plus rational curves of degree at most $3$, and extremality of $R$ forces one of these curves to push forward to a generator of $R$. The finiteness in part 3 comes from a lattice: the classes of curves on $X$ have pullbacks with denominators bounded by the determinants of the exceptional configurations.

### Examples

**Example 2.4.5 (the plane with a line arrangement).** Let $X = \mathbb{P}^2$, $\ell$ the class of a line, and $\Delta = \sum_{i=1}^m a_i L_i$ for distinct lines $L_i$ and $0 \le a_i \le 1$. Then $N^1(X) = \mathbb{R}\ell$, $\overline{NE}(X) = \mathbb{R}_{\ge 0}\ell$ and $K_X + \Delta \equiv (\sum_i a_i - 3)\ell$. So the cone has one ray, spanned by a line $\Gamma$ with $-(K_X + \Delta) \cdot \Gamma = 3 - \sum_i a_i$. It is $(K_X + \Delta)$-negative if and only if $\sum_i a_i < 3$, and then the bound $3$ of Theorem 2.4.4 is attained only for $\Delta = 0$. To decide the singularities, let $P$ be the set of points lying on at least three of the lines, and for $p \in P$ let $S_p$ be the sum of the $a_i$ over the lines through $p$. Let $g \colon W \to \mathbb{P}^2$ be the blow-up of the points of $P$, with exceptional curves $G_p$. A line through $p$ has multiplicity $1$ at $p$, so $g^*L_i = g^{-1}_* L_i + \sum_{p \in L_i} G_p$ and $K_W = g^*K_X + \sum_p G_p$. So the crepant pullback is $\Delta_W = \sum_i a_i g^{-1}_* L_i + \sum_{p \in P} (S_p - 1) G_p$. The strict transforms of the lines through $p$ have distinct tangent directions, so they meet $G_p$ transversally at distinct points and are disjoint over $p$. Two lines meeting at a point outside $P$ meet transversally there. So $g$ is a log resolution, and Theorem 4.2.14 shows: $(\mathbb{P}^2, \Delta)$ is klt if and only if every $a_i < 1$ and $S_p < 2$ for every $p \in P$, and lc if and only if every $a_i \le 1$ and $S_p \le 2$ for every $p \in P$. For four lines in general position with $a_i = \frac34$, $P$ is empty, the pair is klt and $K_X + \Delta \equiv 0$. For $m$ lines through one point $p$, klt forces $\sum_i a_i = S_p < 2$, so $K_X + \Delta$ is anti-ample.

**Example 2.4.6 (the Hirzebruch surface with its negative section).** Let $X = F_n$ with $n \ge 1$, $C_-$ the negative section and $F$ a fibre, as in Example P5.12.8: $C_-^2 = -n$, $C_- \cdot F = 1$, $F^2 = 0$, $\overline{NE}(F_n) = \mathbb{R}_{\ge 0}[C_-] + \mathbb{R}_{\ge 0}[F]$, $K \cdot C_- = n - 2$ and $K \cdot F = -2$. Let $\Delta = b C_-$ with $0 \le b \le 1$. Then
$$(K + bC_-) \cdot C_- = n - 2 - bn, \qquad (K + bC_-) \cdot F = b - 2.$$
The ray of $F$ is always negative, with $-(K + \Delta) \cdot F = 2 - b \le 2$. The ray of $C_-$ is negative if and only if $b > 1 - \frac2n$. For $n \ge 3$ and $b \le 1 - \frac2n$ the cone is $\overline{NE}(X)_{K + \Delta \ge 0} + \mathbb{R}_{\ge 0}[F]$. For $n \ge 3$ and $1 - \frac2n < b \le 1$, the ray of $C_-$ is $K$-positive and $(K + \Delta)$-negative: it is the case $\Delta \cdot \Gamma < 0$ of part 1 of Theorem 2.4.4, and the boundary creates it. For $b = 1$, $-(K + C_-) \cdot C_- = 2$, so the bound $2$ of part 1 is attained. By adjunction $(K + C_-) \cdot C_- = 2p_a(C_-) - 2 = -2$ for every $n$, which explains the value.

**Example 2.4.7 (a singular surface with Picard number one).** Contracting $C_-$ on $F_n$, $n \ge 2$, gives the weighted projective plane $\mathbb{P}(1,1,n)$, with one singular point of type $\frac1n(1,1)$, as in Example 3.5.7 and Section 2. It is a toric surface, every fan in the plane is simplicial, so it is $\mathbb{Q}$-factorial by Theorem 3.3.20, and $\rho = 1$. The image $\ell$ of a fibre satisfies $f^*\ell = F + \frac1n C_-$, so $\ell^2 = (F + \frac1n C_-) \cdot F = \frac1n$, and $\overline{NE} = \mathbb{R}_{\ge 0}\ell$. Here $f^*\ell$ has the denominator $n = |\det(-n)|$ of part 6 of Lemma 2.4.2: the class $\ell$ is not Cartier, while $n\ell$ is. Section 3 computes $K \equiv -(n+2)\ell$, so the single ray is $K$-negative with $-K \cdot \ell = \frac{n+2}{n} \le 3$.

### Proof

*Lemma 2.4.2.* (1) Mumford's pullback is linear, and $f^*D \cdot f^*D' = D \cdot D'$ by the definition of Corollary P5.8.5. Every $\mathbb{R}$-divisor $Z$ on $Y$ is $f^*f_*Z$ plus an exceptional divisor, since $f_*(Z - f^*f_*Z) = 0$. So $f^*D \cdot Z = f^*D \cdot f^*f_*Z = D \cdot f_*Z$, because $f^*D \cdot E_i = 0$. Since $f_*$ is surjective on divisors, $f^*D \equiv 0$ on $Y$ if and only if $D \equiv 0$ on $X$. So $f^*$ is well defined and injective on $N^1$, its image lies in the orthogonal complement $E^\perp$ of the $E_i$, and it is an isometry. If $Z \in E^\perp$, then $Z - f^*f_*Z$ is exceptional and orthogonal to every $E_i$, so it is $0$ by Corollary P5.8.4, and $Z = f^*f_*Z$ lies in the image. The intersection matrix of the $E_i$ is negative definite by Theorem P5.8.3, so the $E_i$ are independent and $N^1(Y) = E^\perp \oplus \bigoplus_i \mathbb{R} E_i$. Hence $\rho(Y) = \rho(X) + r$.

(2) The proof of (1) shows $f^*x \cdot z = x \cdot f_*z$ for divisors, and so $f_*$ preserves numerical equivalence: if $z \equiv 0$, then $x \cdot f_*z = 0$ for every $x$. Also $f_*f^*D = D$ by Corollary P5.8.5. For an integral curve $\Gamma \subset Y$, $f_*\Gamma$ is $0$ if $\Gamma$ is exceptional and the integral curve $f(\Gamma)$ otherwise, and every integral curve $C$ on $X$ is $f_*\tilde C$. So $f_*NE(Y) = NE(X)$, and $f_*\overline{NE}(Y) \subseteq \overline{NE}(X)$ by continuity. For an integral curve $C$, $f^*C = \tilde C + \sum c_i E_i$ with $c_i \ge 0$ lies in $NE(Y)$, so $f^*NE(X) \subseteq NE(Y)$, and $f^*\overline{NE}(X) \subseteq \overline{NE}(Y)$ by continuity. Finally $f^*x \cdot \tilde C = x \cdot C$ and $f^*x \cdot E_i = 0$, so $f^*x$ is nef if and only if $x$ is.

(3) By Lemma P5.12.3 the form on $N^1(Y)$ has signature $(1, \rho(Y) - 1)$. The span of the $E_i$ is negative definite of dimension $r$, and $N^1(Y)$ is its orthogonal sum with $E^\perp = f^*N^1(X)$, so the form on $N^1(X)$ has signature $(1, \rho(Y) - 1 - r) = (1, \rho(X) - 1)$. If $x$ is nef, $f^*x$ is nef by (2), and $x^2 = (f^*x)^2 \ge 0$ by Lemma P5.12.4. The set $\mathcal{P}(X)$ is open, as it is defined by strict inequalities. Let $x \in \mathcal{P}(X)$. Then $(f^*x)^2 = x^2 > 0$, so by Lemma P5.12.3 the class $f^*x$ lies in the closed positive cone of $Y$ or in its negative, and both are in $\pm \overline{NE}(Y)$. If $f^*x \in -\overline{NE}(Y)$, then $f^*H \cdot f^*x \le 0$, since $f^*H$ is nef by (2); but $f^*H \cdot f^*x = H \cdot x > 0$. So $f^*x \in \overline{NE}(Y)$, and $x = f_*f^*x \in \overline{NE}(X)$ by (2).

(4) $C \cdot C' = f^*C \cdot f^*C' = f^*C \cdot \tilde C' = \tilde C \cdot \tilde C' + \sum_i c_i E_i \cdot \tilde C'$, and every term is $\ge 0$. Let $p \in C \cap C'$. If $p$ is not the image of an exceptional curve, $f$ is an isomorphism near $p$ and $\tilde C \cdot \tilde C' > 0$. Otherwise let $E_1, \dots, E_s$ be the curves over $p$, which form a connected configuration by Theorem P5.8.3. The vector $(c_1, \dots, c_s)$ satisfies $\sum_i c_i E_i \cdot E_j = -\tilde C \cdot E_j \le 0$ for $j \le s$, and this is nonzero, because $\tilde C$ is not contained in $f^{-1}(p)$ but meets it. By part 1 of Lemma P5.8.1, every $c_i$ with $i \le s$ is positive. The curve $\tilde C'$ meets some $E_j$ with $j \le s$ for the same reason, so $\sum_i c_i E_i \cdot \tilde C' \ge c_j E_j \cdot \tilde C' > 0$.

(5) By the identification after Definition 2.4.1, this is Kleiman's criterion for the projective variety $X$ (KM98, Theorem 1.18): an ample Cartier divisor is positive on $\overline{NE}(X) \setminus \{0\}$. The function $y \mapsto H \cdot y$ is continuous and positive on the compact set of $y \in \overline{NE}(X)$ with $|y| = 1$, so it has a minimum $m > 0$ there, and $|y| \le m^{-1} H \cdot y$. The slice $\Sigma_H$ is closed and bounded.

(6) For each point $p$ that is the image of exceptional curves, let $M_p$ be the intersection matrix of the curves over $p$, an integer matrix with $\det M_p \ne 0$. For an integral curve $C$, the coefficients of $f^*C$ over $p$ solve $M_p c = -(\tilde C \cdot E_j)_j$, an integer vector, so by Cramer's rule they lie in $\frac{1}{|\det M_p|}\mathbb{Z}$. Take $d = \prod_p |\det M_p|$. Then $f^*C$ is $\frac1d$ times a Cartier divisor on the smooth surface $Y$, so $[C] \in \Lambda$. The group $\operatorname{Num}(Y)$ is a lattice in $N^1(Y)$, as in the proof of Theorem P5.12.14, and $f^*$ is injective and linear, so $\Lambda = (f^*)^{-1}(\frac1d \operatorname{Num}(Y))$ is discrete.

(7) The numbers $a_i$ are the numerical discrepancies of Definition 4.3.3, and $a_i \le 0$ by part 2 of Proposition 4.3.5. Since $K_X$ is $\mathbb{Q}$-Cartier, the relation $K_Y = f^*K_X + \sum a_i E_i$ holds up to linear equivalence of $\mathbb{Q}$-divisors. Then $K_Y \cdot f^*x = K_X \cdot x + \sum a_i E_i \cdot f^*x = K_X \cdot x$. For an integral curve $C$, $K_X \cdot C = f^*K_X \cdot \tilde C = K_Y \cdot \tilde C - \sum_i a_i E_i \cdot \tilde C \ge K_Y \cdot \tilde C$, and $C^2 = f^*C \cdot \tilde C = \tilde C^2 + \sum_i c_i E_i \cdot \tilde C \ge \tilde C^2$. For a pair, $\Delta_Y = f^*\Delta - \sum_i a_i E_i$. Here $f^*\Delta \ge 0$ by Corollary P5.8.5 and $-a_i \ge 0$, so $\Delta_Y \ge 0$, and the strict transform part of $\Delta_Y$ is $f^{-1}_*\Delta$.

*Lemma 2.4.3.* (1) By part 4 of Lemma 2.4.2, every integral curve $\Gamma \ne C$ has $C \cdot \Gamma \ge 0$, so $NE(X) \subseteq \mathbb{R}_{\ge 0}[C] + \overline{NE}(X)_{C \ge 0}$. The right side is closed: if $t_m [C] + y_m \to z$ with $t_m \ge 0$ and $y_m \in \overline{NE}(X)_{C \ge 0}$, then $t_m H \cdot C \le H \cdot (t_m[C] + y_m)$ is bounded, so after passing to a subsequence $t_m \to t$ and $y_m \to z - t[C]$, which lies in the closed set $\overline{NE}(X)_{C \ge 0}$. So the right side contains $\overline{NE}(X)$, and the reverse inclusion is clear. Let $u + v \in \mathbb{R}_{\ge 0}[C]$ with $u, v \in \overline{NE}(X)$, and write $u = s[C] + u'$, $v = t[C] + v'$ with $u', v' \in \overline{NE}(X)_{C \ge 0}$. Then $u' + v' = \lambda [C]$ for some real $\lambda$. If $\lambda > 0$, then $0 \le C \cdot (u' + v') = \lambda C^2 < 0$, which is absurd. If $\lambda < 0$, then $u' + v' + |\lambda|[C] = 0$ is a sum of elements of $\overline{NE}(X)$, and $H$ is positive on its last term by part 5 of Lemma 2.4.2, which is absurd. So $\lambda = 0$ and $u' + v' = 0$, which forces $u' = v' = 0$ by part 5 of Lemma 2.4.2, and $u, v \in \mathbb{R}_{\ge 0}[C]$. So the ray is extremal. If $\Gamma \ne C$ is an integral curve with $[\Gamma] = t[C]$, then $t > 0$ and $0 \le C \cdot \Gamma = tC^2 < 0$, a contradiction.

(2) If $C^2 \ge 0$, then $C \cdot \Gamma \ge 0$ for every integral curve $\Gamma$, by part 4 of Lemma 2.4.2 for $\Gamma \ne C$, so $C$ is nef, against $C \cdot x < 0$. So $C^2 < 0$, and by (1) $x = t[C] + y$ with $t \ge 0$ and $y \in \overline{NE}(X)_{C \ge 0}$. Both terms lie in $\overline{NE}(X)$, and their sum lies in $R$, so by extremality $y = \lambda x$ with $\lambda \ge 0$. If $\lambda > 0$, then $0 \le C \cdot y = \lambda C \cdot x < 0$. So $y = 0$, and $x = t[C]$ with $t > 0$.

(3) Since $x^2 < 0$, the class $x$ is not nef, by part 3 of Lemma 2.4.2. As $\overline{NE}(X)$ is the closure of the cone spanned by integral curves, some integral curve $C$ has $x \cdot C < 0$. Apply (2).

(4) Since $x \in \overline{NE}(X) \setminus \{0\}$, part 5 of Lemma 2.4.2 gives $H \cdot x > 0$, so $x \in \mathcal{P}(X)$. By part 3 of Lemma 2.4.2, $\mathcal{P}(X)$ is an open subset of $\overline{NE}(X)$. If $\rho(X) \ge 2$, choose $v \notin \mathbb{R}x$. For small $t > 0$ both $x + tv$ and $x - tv$ lie in $\mathcal{P}(X)$, their sum $2x$ lies in $R$, and extremality puts both in $R$. Then $tv \in \mathbb{R}x$, a contradiction.

*Theorem 2.4.4.* (1) Let $R = \mathbb{R}_{\ge 0}x$ be a $(K_X + \Delta)$-negative extremal ray. There are two cases.

Suppose first $\Delta \cdot x < 0$. Then some component $D$ of $\Delta$, with coefficient $\delta > 0$, has $D \cdot x < 0$. By part 2 of Lemma 2.4.3, $D^2 < 0$ and $R = \mathbb{R}_{\ge 0}[D]$. Every other component $D_j$ of $\Delta$ has $D_j \cdot D \ge 0$, and $\delta \le 1$ with $D^2 < 0$ gives $\delta D^2 \ge D^2$. So
$$(K_X + \Delta) \cdot D \ge K_X \cdot D + D^2 \ge K_Y \cdot \tilde D + \tilde D^2 = 2p_a(\tilde D) - 2 \ge -2,$$
by part 7 of Lemma 2.4.2 and the adjunction formula, Theorem P5.5.14. So $0 < -(K_X + \Delta) \cdot D \le 2$, and $2p_a(\tilde D) - 2 < 0$ gives $p_a(\tilde D) = 0$, so $\tilde D \cong \mathbb{P}^1$ by Corollary P5.5.15, and $D$ is rational. Put $\Gamma = D$.

Suppose now $\Delta \cdot x \ge 0$. Then $K_X \cdot x < 0$, and $K_Y \cdot f^*x = K_X \cdot x < 0$ by part 7 of Lemma 2.4.2, with $f^*x \in \overline{NE}(Y)$ by part 2. By part 1 of Theorem P5.12.14 on $Y$,
$$f^*x = z_0 + \sum_{i=1}^{s} b_i [C_i],$$
with $z_0 \in \overline{NE}(Y)_{K_Y \ge 0}$, $b_i > 0$, and $C_i$ rational curves with $0 < -K_Y \cdot C_i \le 3$. Since $K_Y \cdot z_0 \ge 0 > K_Y \cdot f^*x$, the sum is not empty. No $C_i$ is exceptional, because $K_Y \cdot E_j \ge 0$ for every $j$ by part 1 of Proposition 4.3.5. Apply $f_*$: $x = f_*z_0 + \sum_i b_i [f(C_i)]$, a sum of elements of $\overline{NE}(X)$ by part 2 of Lemma 2.4.2. By extremality every term lies in $R$. The class of the integral curve $\Gamma = f(C_1)$ is nonzero, since $H \cdot \Gamma > 0$, so $R = \mathbb{R}_{\ge 0}[\Gamma]$, and $\Gamma$ is rational. Now $\Delta \cdot \Gamma \ge 0$, as $[\Gamma] \in R$, and $\tilde \Gamma = C_1$, so
$$-(K_X + \Delta) \cdot \Gamma \le -K_X \cdot \Gamma = -K_Y \cdot C_1 + \sum_j a_j E_j \cdot C_1 \le -K_Y \cdot C_1 \le 3,$$
using $a_j \le 0$ and $E_j \cdot C_1 \ge 0$. The left side is positive because $R$ is $(K_X + \Delta)$-negative.

In both cases $R$ is spanned by a rational curve $\Gamma$ with $0 < -(K_X + \Delta) \cdot \Gamma \le 3$, and the first case is the only one in which $\Delta \cdot \Gamma < 0$.

(2) Let $V$ be the right side, a subcone of $\overline{NE}(X)$. By part 5 of Lemma 2.4.2 the slice $\Sigma_H$ is compact and convex, and the argument of the proof of Theorem P5.12.14 (1) applies word for word: by Minkowski's theorem (Rockafellar, *Convex analysis*, Corollary 18.5.1), every $z \in \overline{NE}(X) \setminus \{0\}$ is a finite sum of generators of extremal rays. An extremal ray either lies in $\overline{NE}(X)_{K_X + \Delta \ge 0}$ or is some $R_i$. So $z \in V$.

(3) If $(K_X + \Delta + \varepsilon H) \cdot \Gamma_i < 0$, then $\varepsilon H \cdot \Gamma_i < -(K_X + \Delta) \cdot \Gamma_i \le 3$, so $|[\Gamma_i]| \le 3c/\varepsilon$ by part 5 of Lemma 2.4.2. The classes $[\Gamma_i]$ lie in the discrete group $\Lambda$ of part 6, which has finitely many points in a bounded set, and distinct rays have distinct generators $[\Gamma_i]$. So there are finitely many such $i$. In a decomposition $z = z_0 + \sum b_i [\Gamma_i]$ given by (2), the term $z_0$ and the $[\Gamma_i]$ with $(K_X + \Delta + \varepsilon H) \cdot \Gamma_i \ge 0$ add up to an element of $\overline{NE}(X)_{K_X + \Delta + \varepsilon H \ge 0}$, and the remaining terms belong to the finite list.

(4) If $K_X + \Delta$ is nef, no ray is negative. If not, some $z \in \overline{NE}(X)$ has $(K_X + \Delta) \cdot z < 0$, and the decomposition of (2) of $z$ contains some $\Gamma_i$.

### Exercises

1. (A) On $\mathbb{P}^2$ let $\Delta = \frac12 (L_1 + L_2 + L_3 + L_4)$ with $L_1, L_2, L_3$ through one point $p$ and $L_4$ not through $p$. Decide whether $(\mathbb{P}^2, \Delta)$ is klt and whether $K + \Delta$ is nef, using Example 2.4.5.
2. (A) Let $X = \mathbb{P}^1 \times \mathbb{P}^1$ with rulings $F_1, F_2$, and $\Delta = a F_1 + b(G_1 + G_2)$ for a fibre $F_1$ of the first ruling and two fibres $G_1, G_2$ of the second, with $0 \le a, b \le 1$. Compute $(K + \Delta) \cdot F_1$ and $(K + \Delta) \cdot G_1$, and list the $(K + \Delta)$-negative extremal rays.
3. (B) Let $X$ be a $\mathbb{Q}$-factorial surface, $D$ an integral curve with $D^2 < 0$, and $\Delta = D$. Show that $(K_X + D) \cdot D \ge -2$, with equality only if $\tilde D \cong \mathbb{P}^1$, $\tilde D$ meets no exceptional curve with $a_i < 0$, and $D^2 = \tilde D^2$. What does the last condition say about the singular points of $X$ on $D$?
4. (B) Let $X$ be a $\mathbb{Q}$-factorial surface with $\rho(X) = 1$. Show that $\overline{NE}(X)$ is a single ray, that every integral curve $C$ has $C^2 > 0$, and that $K_X + \Delta$ is either ample, numerically trivial or anti-ample for every boundary $\Delta$.
5. (B) In Example 2.4.7 with $n = 3$, show that the integer $d$ of part 6 of Lemma 2.4.2 is $3$ and that $\Lambda = \mathbb{Z}\ell$, although $\ell^2 = \frac13$. Deduce that the class of every integral curve is a positive integer multiple of $\ell$.
6. (C) Let $X$ be a $\mathbb{Q}$-factorial surface with $\rho(X) \ge 2$ and $R$ a $(K_X + \Delta)$-negative extremal ray. Show that the square of every integral curve with class in $R$ has the sign of $x^2$, and that if $x^2 < 0$ there is exactly one such curve, while if $x^2 = 0$ there may be infinitely many.

### Lean

The lemmas and the theorem are not yet in Lean. The library states the cone theorem as `MinimalModel.ConeTheoremKlt` for klt pairs and `MinimalModel.ConeTheoremLc` for lc pairs, both through `MinimalModel.ConeDecomposition`, and `MinimalModel.SurfaceConeTheorem` states the case of smooth surfaces. Theorem 2.4.4 for klt surface pairs is the case of dimension $2$ of `MinimalModel.ConeTheoremKlt`, with the rationality and the bound on the length added. Mumford's intersection product on a normal surface is not yet in the library.

### Notes and history

The cone theorem for log surfaces is due to Fujino, *Minimal model theory for log surfaces* (Publ. RIMS 48, 2012), who proved it for a normal projective surface $X$ with a boundary $\Delta$ such that $K_X + \Delta$ is $\mathbb{R}$-Cartier and either $X$ is $\mathbb{Q}$-factorial or $(X, \Delta)$ is lc. The proof here reduces the theorem to the smooth case on the minimal resolution. Tanaka, *Minimal models and abundance for positive characteristic log surfaces* (Nagoya Math. J. 216, 2014), extended it to every characteristic. In higher dimension the cone theorem for klt pairs is KM98, Theorem 3.7, proved with the basepoint-free and rationality theorems, and Matsuki, Chapter 1, presents the surface case as the model for it. Mumford's intersection theory on normal surfaces is from Mum61. The theorem above is weaker than Fujino's in one respect: it does not treat lc pairs on surfaces that are not $\mathbb{Q}$-factorial. Section 3 sketches that case.
