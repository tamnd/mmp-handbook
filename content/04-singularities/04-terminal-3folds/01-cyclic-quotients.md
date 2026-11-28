---
title: Terminal cyclic quotient singularities
nodes: []
sources: [KM98, Rei87, MS84, Whi64, CLS11]
reads_with: [Rei87:ch5, KM98:ch5]
requires: [3.1, 3.3, 4.1, 4.2, 4.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Terminal cyclic quotient singularities

### Statement

Throughout the chapter the field is $\mathbb{C}$. A variety is terminal when every exceptional divisor over it has positive discrepancy (Definition 4.2.1). This section starts with surfaces, where terminal means smooth, and then computes the classes of all cyclic quotient singularities by the toric formula of Volume 3. In dimension 3 the computation leads to the terminal lemma, the first step of the classification of terminal 3-fold singularities.

**Proposition 4.4.1 (terminal surface singularities are smooth).** A normal surface is terminal if and only if it is smooth.

Lean: not yet in Lean.

**Definition 4.4.2 (cyclic quotient singularities).** Let $r \ge 2$ and $a_1, \dots, a_n \in \mathbb{Z}$, and let $\zeta = e^{2\pi i / r}$. The group $\mu_r$ of $r$-th roots of unity acts on $\mathbb{A}^n$ by
$$\zeta \cdot (x_1, \dots, x_n) = (\zeta^{a_1} x_1, \dots, \zeta^{a_n} x_n).$$
The quotient $\mathbb{A}^n / \mu_r$, with the image of the origin, is the *cyclic quotient singularity* $\frac1r(a_1, \dots, a_n)$. The numbers $a_i$ are the *weights*. The action is faithful if and only if $\gcd(r, a_1, \dots, a_n) = 1$. The element $\zeta^k$ is a pseudo-reflection if and only if it fixes a coordinate hyperplane $\{x_i = 0\}$ pointwise and is not the identity, so the action has no pseudo-reflections if and only if
$$\gcd(r, a_1, \dots, \widehat{a_i}, \dots, a_n) = 1 \quad \text{for each } i,$$
where the hat means that $a_i$ is left out. For $k \in \mathbb{Z}$ write $\{x\} = x - \lfloor x \rfloor$ for the fractional part, and put
$$v_k = \Big( \Big\{ \frac{k a_1}{r} \Big\}, \dots, \Big\{ \frac{k a_n}{r} \Big\} \Big) \in \mathbb{Q}^n, \qquad S(k) = \sum_{i=1}^n \Big\{ \frac{k a_i}{r} \Big\}.$$
Replacing $\zeta$ by another primitive root $\zeta^b$, with $\gcd(b, r) = 1$, replaces the weights $a_i$ by $b a_i$ and does not change the image of $\mu_r$ in $GL_n(\mathbb{C})$, so $\frac1r(a_1, \dots, a_n) \cong \frac1r(b a_1, \dots, b a_n)$. A permutation of the coordinates permutes the weights. The weights only matter modulo $r$.

**Lemma 4.4.3 (the toric description).** Let $X = \frac1r(a_1, \dots, a_n)$ with a faithful action and no pseudo-reflections. Let
$$N = \mathbb{Z}^n + \mathbb{Z} \cdot \tfrac1r(a_1, \dots, a_n), \qquad \sigma = \operatorname{Cone}(e_1, \dots, e_n).$$
Then $X \cong U_\sigma$, the minimal generators of the rays of $\sigma$ are $e_1, \dots, e_n$, and
$$\sigma \cap N = \{ v_k + w : 0 \le k \le r - 1, \ w \in \mathbb{Z}^n_{\ge 0} \}.$$
The vector $v_k$ is $0$ only for $k = 0$.

Lean: not yet in Lean.

**Theorem 4.4.4 (the fractional part criterion).** Let $X = \frac1r(a_1, \dots, a_n)$ with $n \ge 2$, a faithful action and no pseudo-reflections. Then:

1. $X$ is $\mathbb{Q}$-factorial and klt, and the index of $K_X$ is $r / \gcd(r, a_1 + \dots + a_n)$.
2. The toric divisor of a primitive vector $v = (v_1, \dots, v_n) \in \sigma \cap N$ over $X$ has discrepancy $a(v) = v_1 + \dots + v_n - 1$.
3. $X$ is canonical if and only if $S(k) \ge 1$ for $k = 1, \dots, r - 1$.
4. $X$ is terminal if and only if $S(k) > 1$ for $k = 1, \dots, r - 1$.

Lean: not yet in Lean.

**Lemma 4.4.5 (complementary sums).** For $1 \le k \le r - 1$,
$$S(k) + S(r - k) = \#\{ i : k a_i \not\equiv 0 \pmod r \}.$$
In the situation of Theorem 4.4.4:

1. If $n = 2$, then $X$ is not terminal.
2. If $n = 3$ and $X$ is terminal, then every $a_i$ is coprime to $r$, and $1 < S(k) < 2$ for $k = 1, \dots, r - 1$. In particular $\mu_r$ acts freely on $\mathbb{A}^3 \setminus 0$, and $X$ has an isolated singular point.

Lean: not yet in Lean.

**Theorem 4.4.6 (the terminal lemma).** Let $X = \frac1r(a_1, a_2, a_3)$ with $r \ge 2$, a faithful action and no pseudo-reflections. Then $X$ is terminal if and only if every $a_i$ is coprime to $r$ and $a_i + a_j \equiv 0 \pmod r$ for some $i \ne j$. In that case
$$X \cong \tfrac1r(1, -1, a) \quad \text{with } \gcd(a, r) = 1,$$
the index of $K_X$ is $r$, and the singular point of $X$ is isolated.

Lean: not yet in Lean.

The proof reduces the theorem to the following statement about fractional parts. Its proof is not reproduced here.

**Lemma 4.4.7 (the number-theoretic step).** Let $r \ge 2$, and let $a_1, a_2, a_3, a_4$ be integers coprime to $r$ with
$$\sum_{i=1}^4 \Big\{ \frac{k a_i}{r} \Big\} = 2 \quad \text{for } k = 1, \dots, r - 1.$$
Then, after renumbering, $a_1 + a_2 \equiv 0$ and $a_3 + a_4 \equiv 0 \pmod r$.

Lean: not yet in Lean.

This is the main lemma of Morrison and Stevens (MS84), whose proof is elementary and uses the distribution of the multiples $k a_i$ modulo $r$. Reid (Rei87, (5.4) Theorem) proves a general form for the weights of a hyperquotient, and deduces the terminal lemma as Rei87, (5.6) Corollary. The geometric form is White's theorem on lattice tetrahedra (Whi64): a lattice tetrahedron whose only lattice points are its vertices lies between two adjacent parallel lattice planes. The converse of the lemma is easy: if $a_1 + a_2 \equiv 0$ and $a_3 + a_4 \equiv 0$, then each pair contributes $\{x\} + \{-x\} = 1$ for $x \notin \mathbb{Z}$.

### Proof in words

A cyclic quotient is a toric variety: its cone is the positive orthant, in the lattice generated by $\mathbb{Z}^n$ and the vector $\frac1r(a_1, \dots, a_n)$. The canonical divisor has the linear form $\psi_K(v) = v_1 + \dots + v_n$ on the orthant, and Volume 3 says that a toric singularity is terminal when every lattice point of the cone other than $0$ and the generators has $\psi_K > 1$. The lattice points of the orthant are the points $v_k$ in the unit cube, plus integer vectors, so only the $r - 1$ points $v_k$ matter, and $\psi_K(v_k) = S(k)$.

The sum $S(k) + S(-k)$ counts the coordinates with $k a_i \not\equiv 0$, because $\{x\} + \{-x\} = 1$ when $x$ is not an integer. In dimension 2 this count is at most 2, so $S(k)$ and $S(-k)$ cannot both exceed 1: terminal cyclic quotient surfaces are smooth. In dimension 3 the count is 3, and the terminal condition squeezes every $S(k)$ into the open interval $(1, 2)$. Adding a fourth weight $a_4 = -(a_1 + a_2 + a_3)$ turns this into the condition that four fractional parts sum to exactly 2 for every $k$. That condition forces the weights to come in two pairs of opposite residues, which is the number-theoretic step. A pair inside $\{a_1, a_2, a_3\}$ gives $\frac1r(1, -1, a)$ after a change of the generator.

### Examples

**Example 4.4.8 (the quotient $\frac12(1,1,1)$, by a weighted blow-up).** Let $X = \frac12(1,1,1) = \mathbb{A}^3 / \pm 1$. Here $N = \mathbb{Z}^3 + \mathbb{Z} v$ with $v = \frac12(1,1,1)$, and $M = \{ m \in \mathbb{Z}^3 : m_1 + m_2 + m_3 \text{ even} \}$. Let $f \colon Y \to X$ be the star subdivision of $\sigma$ at $v$, the weighted blow-up of the origin with weights $\frac12(1,1,1)$. It has three cones, $\sigma_1 = \operatorname{Cone}(v, e_2, e_3)$ and the two others obtained by permuting the coordinates, and each is smooth by Volume 3, Example 3.1.34. The basis of $M$ dual to $(v, e_2, e_3)$ is
$$m_1 = (2, 0, 0), \qquad m_2 = (-1, 1, 0), \qquad m_3 = (-1, 0, 1),$$
since $\langle m_1, v \rangle = 1$, $\langle m_2, v \rangle = \langle m_3, v \rangle = 0$, and $\langle m_i, e_j \rangle = \delta_{ij}$ for $i, j \in \{2, 3\}$. So $U_{\sigma_1} = \mathbb{A}^3$ with coordinates
$$u = x_1^2, \qquad s = \frac{x_2}{x_1}, \qquad t = \frac{x_3}{x_1},$$
and $f$ is given by $x_1^2 = u$, $x_1 x_2 = u s$, $x_2 x_3 = u s t$, and so on for the other invariant monomials of degree 2. The exceptional divisor $E$ is the divisor of the ray $v$, which is $\{u = 0\}$ in this chart. It is $\mathbb{P}^2$, and $Y$ is the total space of $\mathcal{O}_{\mathbb{P}^2}(-2)$.

Now compute the canonical divisor. The form $\omega = dx_1 \wedge dx_2 \wedge dx_3$ has weight $(-1)^3 = -1$, so it is not invariant, but $\omega^{\otimes 2}$ is invariant, and it descends to a generator of $\mathcal{O}_X(2K_X)$ near the origin, since $\mathbb{A}^3 \to X$ is étale outside the origin. In the function field of $\mathbb{A}^3$, which contains the function field of $Y$, write $x_1 = u^{1/2}$, $x_2 = s u^{1/2}$ and $x_3 = t u^{1/2}$. Then
$$dx_1 = \tfrac12 u^{-1/2} du, \qquad dx_2 = u^{1/2} ds + \tfrac12 s u^{-1/2} du, \qquad dx_3 = u^{1/2} dt + \tfrac12 t u^{-1/2} du,$$
so
$$\omega = \tfrac12 u^{1/2} \, du \wedge ds \wedge dt, \qquad \omega^{\otimes 2} = \tfrac14 u \, (du \wedge ds \wedge dt)^{\otimes 2}.$$
The right side is a section of $\mathcal{O}_Y(2K_Y)$ with divisor $E$ on this chart, and the same holds on the other two charts by symmetry. So $2K_Y = f^*(2K_X) + E$, that is
$$K_Y = f^* K_X + \tfrac12 E, \qquad a(E, X) = \tfrac12.$$
This agrees with Volume 3, Proposition 3.3.35: $v = \frac12 e_1 + \frac12 e_2 + \frac12 e_3$, and $a(v) = \frac32 - 1 = \frac12$. Since $Y$ is smooth and its exceptional set is the smooth divisor $E$, $f$ is a log resolution, with $\Delta_Y = -\frac12 E$. By Theorem 4.2.14 and Theorem 4.2.12,
$$\operatorname{discrep}(X) = \min\Big\{ \tfrac12, \ \min\big\{ 1, 1 + \tfrac12 \big\} \Big\} = \tfrac12.$$
So $X$ is terminal, as in Example 4.2.25 and Example 4.2.32. The fractional part criterion agrees: $r = 2$, $S(1) = \frac32 > 1$. In the form of the terminal lemma, $\frac12(1,1,1) = \frac12(1, -1, 1)$, since $-1 \equiv 1 \pmod 2$.

**Example 4.4.9 (the quotient $\frac13(1,1,1)$, by a weighted blow-up).** Let $X = \frac13(1,1,1)$, so $N = \mathbb{Z}^3 + \mathbb{Z} v$ with $v = \frac13(1,1,1)$ and $M = \{ m \in \mathbb{Z}^3 : m_1 + m_2 + m_3 \equiv 0 \pmod 3 \}$. The star subdivision of $\sigma$ at $v$ has the three cones $\operatorname{Cone}(v, e_2, e_3)$ and its permutations. Each is smooth: $e_1 = 3v - e_2 - e_3$, so $(v, e_2, e_3)$ is a basis of $N$. The dual basis is
$$m_1 = (3, 0, 0), \qquad m_2 = (-1, 1, 0), \qquad m_3 = (-1, 0, 1),$$
all in $M$, and the chart has coordinates $u = x_1^3$, $s = x_2 / x_1$, $t = x_3 / x_1$. The exceptional divisor is $E = \{u = 0\} \cong \mathbb{P}^2$, and $Y$ is the total space of $\mathcal{O}_{\mathbb{P}^2}(-3)$. This time $\omega = dx_1 \wedge dx_2 \wedge dx_3$ has weight $\zeta^3 = 1$, so $\omega$ itself is invariant and generates $\mathcal{O}_X(K_X)$: the point is Gorenstein. With $x_1 = u^{1/3}$, $x_2 = s u^{1/3}$, $x_3 = t u^{1/3}$,
$$dx_1 = \tfrac13 u^{-2/3} du, \qquad \omega = \tfrac13 u^{-2/3} du \wedge u^{1/3} ds \wedge u^{1/3} dt = \tfrac13 \, du \wedge ds \wedge dt.$$
The form has no zero and no pole on the chart, so
$$K_Y = f^* K_X + 0 \cdot E, \qquad a(E, X) = 0.$$
The map $f$ is a crepant log resolution, and Theorem 4.2.14 gives $\operatorname{discrep}(X) = \min\{0, 1\} = 0$. So $X$ is canonical and not terminal. The fractional part criterion agrees: $S(1) = 1$ and $S(2) = 2$. The terminal lemma agrees as well: $1 + 1 = 2 \not\equiv 0 \pmod 3$. As a check by the cover, the blow-up of the origin of $\mathbb{A}^3$ has $A(E') = 3$, and $\mu_3$ acts trivially on $E'$ with ramification index $e = 3$, so Theorem 4.2.29 gives $A(E) = \frac{3}{3} = 1$ and $a(E) = 0$. The same computation for $\frac1r(1,1,1)$ gives $\omega = \frac1r u^{3/r - 1} \, du \wedge ds \wedge dt$, so $a(E) = \frac3r - 1$, as in Volume 3, Example 3.3.40.

**Example 4.4.10 (the quotients $\frac1r(1, -1, a)$).** Let $X = \frac1r(1, -1, a)$ with $\gcd(a, r) = 1$. For $1 \le k \le r - 1$ write $\overline{ka}$ for the residue of $ka$ in $\{1, \dots, r - 1\}$. Then
$$v_k = \Big( \frac{k}{r}, \frac{r - k}{r}, \frac{\overline{ka}}{r} \Big), \qquad S(k) = 1 + \frac{\overline{ka}}{r} > 1.$$
So $X$ is terminal by Theorem 4.4.4, and the index is $r$, since $1 - 1 + a = a$ is coprime to $r$. Each $v_k$ is primitive: if $v_k = d w$ with $d \ge 2$ and $w \in N$, then $w \in \sigma$ has coordinates in $[0, \frac12)$, so $w = v_j$ for some $j$, and $k = dj$, $r - k = d(r - j)$, which give $r = dr$. So the toric divisor of $v_k$ has discrepancy $a(v_k) = \overline{ka} / r$. As $k$ runs over $1, \dots, r - 1$, the residue $\overline{ka}$ runs over $1, \dots, r - 1$, so these discrepancies are $\frac1r, \frac2r, \dots, \frac{r-1}{r}$, each once. The smallest, $\frac1r$, occurs at $k \equiv a^{-1} \pmod r$. So $\operatorname{discrep}(X) \le \frac1r$, and a terminal point can have discrepancies arbitrarily close to 0.

**Example 4.4.11 (the quotient $\frac17(1,2,4)$).** The weights $1, 2, 4$ are coprime to 7, and the multiples are
$$k = 1, \dots, 6: \quad v_k = \tfrac17(1,2,4), \ \tfrac17(2,4,1), \ \tfrac17(3,6,5), \ \tfrac17(4,1,2), \ \tfrac17(5,3,6), \ \tfrac17(6,5,3),$$
so $S(k) = 1, 1, 2, 1, 2, 2$. By Theorem 4.4.4, $X$ is canonical and not terminal, and since $1 + 2 + 4 = 7$, it is Gorenstein. The singular point is isolated, since every weight is coprime to 7. No two weights sum to 0 modulo 7, since $1 + 2 = 3$, $1 + 4 = 5$ and $2 + 4 = 6$, as the terminal lemma requires. The toric divisors of $v_1$, $v_2$ and $v_4$ are crepant.

**Example 4.4.12 (two quotients of order 5).** For $\frac15(1,2,3)$ the weights 2 and 3 are opposite, and
$$S(1) = \tfrac65, \quad S(2) = \tfrac{2 + 4 + 1}{5} = \tfrac75, \quad S(3) = \tfrac{3 + 1 + 4}{5} = \tfrac85, \quad S(4) = \tfrac{4 + 3 + 2}{5} = \tfrac95.$$
So it is terminal. With the generator $\zeta^3$ the weights become $3, 6, 9 \equiv 3, 1, 4$, and after a permutation the point is $\frac15(1, -1, 3)$. For $\frac15(1,1,2)$, instead, $S(1) = \frac45 < 1$, so it is not canonical. It is klt by Theorem 4.4.4, and the toric divisor of $v_1$ has discrepancy $-\frac15$.

### Proof

*Proof of Proposition 4.4.1.* A smooth variety is terminal: by Theorem 4.2.12 with $\Delta = 0$, its discrepancy is 1. Conversely, a terminal surface is smooth by Proposition 4.3.5, part 3. For the cyclic quotients there is a second proof, by Lemma 4.4.5, part 1, below. $\square$

*Proof of Lemma 4.4.3.* The dual lattice of $N$ is
$$M = \{ m \in \mathbb{Z}^n : a_1 m_1 + \dots + a_n m_n \equiv 0 \pmod r \},$$
since $m \in \mathbb{Q}^n$ pairs integrally with $\mathbb{Z}^n$ exactly when $m \in \mathbb{Z}^n$, and with $\frac1r(a_1, \dots, a_n)$ exactly when $\sum_i a_i m_i \in r\mathbb{Z}$. The group $\mu_r$ acts on the monomial $x^m$ by $\zeta^{\sum a_i m_i}$, so the invariant monomials are the $x^m$ with $m \in \sigma^\vee \cap M = \mathbb{Z}^n_{\ge 0} \cap M$. Since the action is diagonal, the invariant ring $\mathbb{C}[x_1, \dots, x_n]^{\mu_r}$ is spanned by the invariant monomials, so it is $\mathbb{C}[\sigma^\vee \cap M]$, and $X \cong U_\sigma$.

The points of $N$ are $\frac{k}{r}(a_1, \dots, a_n) + w'$ with $0 \le k \le r - 1$ and $w' \in \mathbb{Z}^n$, and subtracting the integer parts writes each as $v_k + w$ with $w \in \mathbb{Z}^n$. The coordinates of $v_k$ lie in $[0, 1)$, so $v_k + w \in \sigma$ if and only if every $w_i \ge 0$. The vector $v_k$ is $0$ exactly when $k a_i \equiv 0$ for all $i$, which for a faithful action means $k = 0$.

Suppose that $\frac1d e_i \in N$ for some $d \ge 2$. Then $\frac1d e_i = v_k + w$ for some $k$ and $w$, and since the coordinates of $v_k$ other than the $i$-th must be integers, $k a_j \equiv 0$ for all $j \ne i$, and $k a_i \not\equiv 0$. Then $\zeta^k$ fixes the hyperplane $\{x_i = 0\}$ and is not the identity: a pseudo-reflection. So with no pseudo-reflections, each $e_i$ is primitive, and it is the minimal generator of its ray. Conversely, if $g = \gcd(r, a_j : j \ne i) > 1$, then $k = r / g$ has $k a_j \equiv 0$ for $j \ne i$, and $k a_i \not\equiv 0$ by faithfulness, which justifies the criterion for pseudo-reflections in Definition 4.4.2. $\square$

*Proof of Theorem 4.4.4.* The cone $\sigma$ is simplicial, so $X$ is $\mathbb{Q}$-factorial, and it is klt by Volume 3, Theorem 3.3.36, part 1, or by Theorem 4.2.30. The vector $m_\sigma \in M_{\mathbb{Q}}$ with $\langle m_\sigma, e_i \rangle = 1$ for all $i$ is $(1, \dots, 1)$. Since $\sigma$ has full dimension, $\sigma^\perp = 0$, and by Volume 3, Corollary 3.3.27, part 3, the index is the least $m \ge 1$ with $m (1, \dots, 1) \in M$, that is with $m (a_1 + \dots + a_n) \equiv 0 \pmod r$. This least $m$ is $r / \gcd(r, a_1 + \dots + a_n)$, which proves part 1. Part 2 is Volume 3, Proposition 3.3.35, with $u_i = e_i$ and $\lambda_i = v_i$.

For parts 3 and 4, apply Volume 3, Theorem 3.3.36, which asks for $\langle m_\sigma, v \rangle \ge 1$ at every nonzero $v \in \sigma \cap N$ for canonical, and $\langle m_\sigma, v \rangle > 1$ at every $v \in \sigma \cap N$ other than $0$ and $e_1, \dots, e_n$ for terminal. By Lemma 4.4.3, such a $v$ is $v_k + w$ with $w \in \mathbb{Z}^n_{\ge 0}$, and
$$\langle m_\sigma, v_k + w \rangle = S(k) + w_1 + \dots + w_n.$$
For $k = 0$, $v = w$ is a nonzero integer vector with nonnegative coordinates. Then $\langle m_\sigma, w \rangle \ge 1$, with equality only at the $e_i$, and $\langle m_\sigma, w \rangle \ge 2$ at the other points. For $1 \le k \le r - 1$, the least value over $w$ is $S(k)$, at $w = 0$. So the condition for canonical is $S(k) \ge 1$ for $k = 1, \dots, r - 1$, and the condition for terminal is $S(k) > 1$ for the same $k$. $\square$

*Proof of Lemma 4.4.5.* For $x \in \mathbb{R}$, $\{x\} + \{-x\} = 0$ if $x \in \mathbb{Z}$ and $1$ otherwise. Apply this to $x = k a_i / r$, for which $\{-x\} = \{(r - k) a_i / r\}$, and sum over $i$.

For part 1, let $n = 2$ and suppose that $X$ is terminal. For $1 \le k \le r - 1$, Theorem 4.4.4 gives $S(k) > 1$ and $S(r - k) > 1$, so $S(k) + S(r - k) > 2$. This contradicts the identity, whose right side is at most 2. Note that $r \ge 2$, so such a $k$ exists.

For part 2, let $n = 3$ and $X$ terminal. If $d = \gcd(a_i, r) > 1$ for some $i$, put $k = r / d$. Then $k a_i \equiv 0$, so the identity gives $S(k) + S(r - k) \le 2$, while terminal gives $S(k) + S(r - k) > 2$. So every $a_i$ is coprime to $r$, and then the identity reads $S(k) + S(r - k) = 3$ for every $k$. Since $S(r - k) > 1$, $S(k) < 2$. The element $\zeta^k$ with $1 \le k \le r - 1$ multiplies each coordinate by $\zeta^{k a_i} \ne 1$, so it fixes only the origin, and $\mu_r$ acts freely on $\mathbb{A}^3 \setminus 0$. The quotient map is then étale over $X \setminus 0$, which is smooth. $\square$

*Proof of Theorem 4.4.6.* Suppose first that every $a_i$ is coprime to $r$ and that $a_1 + a_2 \equiv 0$, after a permutation. Choose $b$ with $b a_1 \equiv 1 \pmod r$, and replace $\zeta$ by $\zeta^b$, as in Definition 4.4.2. The weights become $(1, -1, a)$ with $a = b a_3$, which is coprime to $r$. By Example 4.4.10, $\frac1r(1, -1, a)$ is terminal of index $r$, and its singular point is isolated by Lemma 4.4.5, part 2, or directly since all weights are units modulo $r$.

Conversely, suppose that $X$ is terminal. By Lemma 4.4.5, part 2, every $a_i$ is coprime to $r$, and $1 < S(k) < 2$ for $1 \le k \le r - 1$. Since $S(k) \equiv k(a_1 + a_2 + a_3)/r$ modulo $\mathbb{Z}$, and $S(k)$ is not an integer,
$$k(a_1 + a_2 + a_3) \not\equiv 0 \pmod r \quad \text{and} \quad \Big\{ \frac{-k(a_1 + a_2 + a_3)}{r} \Big\} = 1 - \{S(k)\} = 1 - (S(k) - 1) = 2 - S(k).$$
The first statement, for every $k$ from 1 to $r - 1$, says that $a_4 = -(a_1 + a_2 + a_3)$ is coprime to $r$. The second says
$$\sum_{i=1}^4 \Big\{ \frac{k a_i}{r} \Big\} = S(k) + 2 - S(k) = 2 \quad \text{for } k = 1, \dots, r - 1.$$
By Lemma 4.4.7, the four weights split into two pairs of opposite residues. If one pair is $\{a_i, a_j\}$ with $i, j \le 3$, this is the claim. Otherwise the pairs are $\{a_i, a_4\}$ and $\{a_j, a_l\}$ with $\{i, j, l\} = \{1, 2, 3\}$, and the second pair lies in $\{a_1, a_2, a_3\}$. In either case some $a_i + a_j \equiv 0$ with $i, j \le 3$, and the first part of the proof applies. $\square$

### Exercises

1. (A) Check the table of $S(k)$ for $\frac17(1,2,4)$ in Example 4.4.11. Show that the generator $\zeta^2$ maps the weights $(1, 2, 4)$ to a permutation of themselves, and explain the symmetry $S(2k) = S(k)$ of the table.
2. (A) Write down the coordinates of the chart $\operatorname{Cone}(e_1, v, e_3)$ of the star subdivision in Example 4.4.9, and check that the form $\omega$ is a unit multiple of the standard volume form there, so that $a(E) = 0$ is computed in every chart.
3. (B) Show that $\frac1r(1,1,1)$ is terminal if and only if $r = 2$, and canonical if and only if $r \le 3$, both by the formula $a(E) = \frac3r - 1$ and by the fractional part criterion.
4. (B) Let $X = \frac1r(a_1, a_2, a_3)$ with a faithful action and no pseudo-reflections, and suppose that $d = \gcd(a_3, r) > 1$. Show directly that $v_{r/d}$ has third coordinate 0 and that $S(r/d) + S(r - r/d) = 2$, so that $X$ is not terminal. Check this on $\frac14(1,1,2)$, where $S(2) = 1$.
5. (B) Use Lemma 4.4.5 to show that a cyclic quotient surface $\frac1r(1, q)$ with $\gcd(q, r) = 1$ is canonical if and only if $q \equiv -1 \pmod r$, and compare with Theorem 4.3.19 and Example 4.3.21.
6. (C) Prove Lemma 4.4.7 for $r \le 5$ by hand. Replace the generator so that $a_1 = 1$, and show that the condition for $k = 1$ and $k = r - 1$ already forces $a_1 + a_2 + a_3 + a_4 \equiv 0$. Then list the possibilities for $(a_2, a_3, a_4)$ modulo $r$ and check the condition for the remaining $k$.

### Lean

The theorems of this section are not yet in Lean. The library defines the classes as `MinimalModel.IsTerminal`, `MinimalModel.IsCanonical` and `MinimalModel.IsKlt`, by log discrepancies of divisorial valuations, but it has no quotient varieties, no cyclic group actions and no toric description of a quotient. The fractional part criterion is a finite computation for fixed weights, and it would be a natural first target once the toric discrepancy formula of Volume 3 is in Lean.

### Notes and history

The fractional part criterion is the toric criterion of Reid (Rei87, Section 4) for cyclic quotients, and Volume 3, Chapter 3, explains its origin in Reid's work on toric singularities. The terminal lemma has several independent proofs. White (Whi64) classified the lattice tetrahedra with no lattice points other than their vertices, which is the geometric form of the lemma, since a cyclic quotient $\frac1r(a_1, a_2, a_3)$ is terminal exactly when the tetrahedron with vertices $0, e_1, e_2, e_3$ contains no other point of $N$. Frumkin, and Morrison and Stevens (MS84), found number-theoretic proofs, and Morrison and Stevens also classified the Gorenstein terminal cyclic quotients of dimension 4, which is Lemma 4.4.7 in another guise. Reid (Rei87, Section 5) proves a version of the number-theoretic step that applies to hyperquotients, and uses it as one step of Mori's classification in Section 3 of this chapter.
