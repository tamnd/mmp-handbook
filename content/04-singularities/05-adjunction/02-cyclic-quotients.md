---
title: The different at a cyclic quotient point
nodes: []
sources: [KM98, Kol13, Kol92]
reads_with: [KM98:ch5, Kol13:ch4]
requires: [4.1, 4.2, 4.3, 2.3, P5.5, P5.6, P5.7, P5.8]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The different at a cyclic quotient point

### Statement

On a surface the different is a finite computation on a resolution. When the resolution graph near $S$ is a chain of rational curves, the computation has a closed form, and its answer is the formula that the rest of the chapter uses: the coefficient of the different at a cyclic quotient point of order $m$ is $1 - \frac1m$, plus a correction from $B$ with denominators $m$.

The arithmetic of a chain is governed by continuants. Let $a_1, \dots, a_k$ be integers with $a_i \ge 2$. Define $p_0 = 0$, $p_1 = 1$ and

$$p_{i+1} = a_i p_i - p_{i-1} \quad (1 \le i \le k).$$

Let $M$ be the $k \times k$ tridiagonal matrix with $a_1, \dots, a_k$ on the diagonal and $-1$ in the entries $(i, i+1)$ and $(i+1, i)$, and $D_i$ the determinant of its leading $i \times i$ minor, with $D_0 = 1$. The continued fraction notation is that of Theorem 4.3.19: $[a_1, \dots, a_k] = a_1 - 1/[a_2, \dots, a_k]$ and $[a_k] = a_k$.

**Lemma 4.5.11 (continuants).** In this setting:

1. $p_{i+1} = D_i$ for $0 \le i \le k$. In particular $m := p_{k+1} = \det M$.
2. $0 = p_0 < p_1 < p_2 < \dots < p_{k+1} = m$, and $\gcd(p_i, p_{i+1}) = 1$.
3. $p_{k+1}/p_k = [a_k, a_{k-1}, \dots, a_1]$, and $\det M$ is also the numerator of $[a_1, \dots, a_k]$ in lowest terms. So if $E_1, \dots, E_k$ is the exceptional chain of the minimal resolution of the cyclic quotient singularity $\frac1n(1,q)$, with $E_i^2 = -a_i$ as in Theorem 4.3.19, then $m = n$.

Lean: not yet in Lean.

Now let $X$ be a normal surface, $P \in X$ a closed point, $S$ an integral curve through $P$, and $B = \sum_j b_j B_j$ an $\mathbb{R}$-divisor with no component equal to $S$. Suppose that $f \colon Y \to X$ is a resolution, an isomorphism over $X \setminus P$, with exceptional curves $E_1, \dots, E_k$ forming a chain: each $E_i$ is a smooth rational curve, $E_i^2 = -a_i \le -2$, $E_i$ meets $E_{i+1}$ transversally in one point and no other pairs meet. Suppose that $S'$ is smooth near $f^{-1}(P)$ and meets $f^{-1}(P)$ in one point $q \in E_1$, transversally, and meets no other $E_i$. The case $k = 0$, in which $X$ is smooth at $P$ and $f$ is the identity, is allowed, with $m = 1$.

**Theorem 4.5.12 (the coefficient formula).** In this setting, let $m = \det M$. The coefficient of $\operatorname{Diff}_{S^\nu}(B)$ at $q$ is

$$1 - \frac1m + \sum_j \frac{m_j b_j}{m},$$

where $m_j = m \cdot (f^*B_j \cdot S')_q$ is a nonnegative integer, and $m_j > 0$ if and only if $P \in B_j$. If $P \in B_j$ and $B_j'$ does not pass through $q$, then $m_j = m \, e_{1,j}$, where $e_{1,j}$ is the coefficient of $E_1$ in $f^*B_j$. The coefficients of the exceptional curves in $\Delta_Y$ for $B = 0$ are

$$c_i = 1 - \frac{p_i}{m} \quad (1 \le i \le k).$$

Lean: not yet in Lean.

The formula applies whenever the minimal resolution near $S$ is such a chain. The classification of plt surface pairs says that this is the only case that occurs for plt pairs. The proof uses the classification of the dual graphs of lc and klt surface singularities, and this chapter takes it as a black box.

**Theorem 4.5.13 (plt surface pairs).** Let $X$ be a normal surface, $S$ an integral curve and $B \ge 0$ an $\mathbb{R}$-divisor with no component equal to $S$, and suppose that $(X, S + B)$ is plt near a singular point $P \in S$ of $X$. Then $S$ is smooth at $P$, the point $P$ is a cyclic quotient singularity $\frac1n(1,q)$ of $X$, and on the minimal resolution the strict transform of $S$ meets the exceptional chain in one point, transversally, on one of the two end curves. In particular $\operatorname{Diff}_S(0) = \sum_P (1 - \frac1{n_P}) P$, where the sum runs over the singular points of $X$ on $S$ and $n_P$ is the order of the cyclic quotient singularity at $P$.

Lean: not yet in Lean.

*Status.* Theorem 4.5.13 is a black box in this chapter. It is KM98, Section 4.1, and Kol13, Chapter 3. Section 4 of this chapter proves the part of it that says $S$ is normal at $P$ (Theorem 4.5.25), from connectedness.

### Proof in words

The coefficients of the exceptional curves are determined by the linear system $(K_Y + \Delta_Y) \cdot E_j = 0$, whose matrix is the negative definite intersection matrix of the chain. Along a chain the system is a three-term recursion, and the continuants solve it: the guess $c_i = 1 - p_i/m$ satisfies the recursion because the $p_i$ satisfy the same recursion with the constant term removed, and the two boundary conditions $c_0 = 1$ (the curve $S'$) and $c_{k+1} = 0$ (nothing beyond the chain) pin down $m = p_{k+1}$.

The different at $q$ only sees $c_1$, which is $1 - \frac1m$. The part from $B$ is the pullback $f^*B_j$, whose exceptional coefficients are the solution of a linear system with matrix $M$; Cramer's rule puts $\det M = m$ in the denominator.

### Examples

**Example 4.5.14 (a line through $\frac1n(1,1)$).** Let $X$ be the cyclic quotient singularity $\frac1n(1,1)$, $n \ge 2$, the cone over the rational normal curve of degree $n$ (Example 4.2.24), and $S$ the image of a coordinate axis, a ruling of the cone. The minimal resolution has one curve $E$, with $E^2 = -n$, and $S'$ is a fibre of $\mathcal{O}_{\mathbb{P}^1}(-n)$, so it meets $E$ once, transversally. Here $k = 1$, $a_1 = n$, $p_1 = 1$ and $m = p_2 = n$, so $c_1 = 1 - \frac1n$ and

$$\operatorname{Diff}_S(0) = \Big(1 - \frac1n\Big) P.$$

Directly: $K_Y \cdot E = n - 2$ by adjunction, and $(K_Y + S' + cE) \cdot E = n - 2 + 1 - nc = 0$ gives $c = \frac{n-1}{n}$. For $n = 2$ this is Example 4.5.8.

**Example 4.5.15 (the point $\frac17(1,3)$, from both ends).** Here $\frac73 = [3, 2, 2]$, since $3 - 1/(2 - \frac12) = 3 - \frac23 = \frac73$. Let $S$ be the toric curve whose strict transform meets the end curve $E_1$ with $E_1^2 = -3$. The continuants are $p = 0, 1, 3, 5, 7$, since $p_2 = 3$, $p_3 = 2 \cdot 3 - 1 = 5$ and $p_4 = 2 \cdot 5 - 3 = 7$. So $m = 7$ and

$$\Delta_Y = S' + \tfrac67 E_1 + \tfrac47 E_2 + \tfrac27 E_3.$$

Check at $E_1$: $K_Y \cdot E_1 = 1$, and $1 + 1 - 3 \cdot \frac67 + \frac47 = 2 - 2 = 0$. Check at $E_3$: $0 + \frac47 - 2 \cdot \frac27 = 0$. The other toric curve $T$ meets the other end $E_3$, with $E_3^2 = -2$. Read from that end the chain is $[2, 2, 3]$, the continuants are $p = 0, 1, 2, 3, 7$, and the coefficients of $E_3, E_2, E_1$ are $\frac67, \frac57, \frac47$. The two answers differ on the interior of the chain, but both differents are $\frac67 P$: the coefficient only depends on the order $m = 7$ of the group.

**Example 4.5.16 (a second line).** In Example 4.5.14, let $L$ be another ruling and $B = bL$. Then $L'$ meets $E$ transversally at a point other than $q$, and $f^*L = L' + \frac1n E$, since $(L' + eE) \cdot E = 1 - ne = 0$. So $m_1 = n \cdot \frac1n = 1$, and the coefficient formula gives

$$\operatorname{Diff}_S(bL) = \Big(1 - \frac1n + \frac bn\Big) P.$$

Directly: $(K_Y + S' + bL' + cE) \cdot E = n - 2 + 1 + b - nc = 0$ gives $c = \frac{n - 1 + b}{n}$. The coefficient is at most 1 exactly when $b \le 1$, and less than 1 exactly when $b < 1$. Section 4 shows that this is the lc and plt condition for $(X, S + bL)$.

### Proof

*Proof of Lemma 4.5.11.* (1) Expanding the determinant of the leading $(i+1) \times (i+1)$ minor along its last row gives $D_{i+1} = a_{i+1} D_i - D_{i-1}$, with $D_0 = 1$ and $D_1 = a_1$. The sequence $p_{i+1}$ satisfies the same recursion, with $p_1 = 1 = D_0$ and $p_2 = a_1 = D_1$. So $p_{i+1} = D_i$ for all $i$, and $p_{k+1} = D_k = \det M$.

(2) By induction, $p_{i+1} - p_i = (a_i - 1) p_i - p_{i-1} \ge p_i - p_{i-1} > 0$, using $a_i \ge 2$ and $p_i \ge 0$. A common divisor of $p_i$ and $p_{i+1}$ divides $p_{i-1} = a_i p_i - p_{i+1}$, and by descent it divides $p_1 = 1$.

(3) The recursion gives $p_{i+1}/p_i = a_i - p_{i-1}/p_i = a_i - 1/(p_i/p_{i-1})$ for $i \ge 2$, and $p_2/p_1 = a_1$. By induction $p_{i+1}/p_i = [a_i, a_{i-1}, \dots, a_1]$, and the fraction is in lowest terms by part 2. Reversing the order of the $a_i$ conjugates $M$ by the permutation matrix that reverses the basis, so it does not change $\det M$. Applying the first statement to the reversed chain shows that $\det M$ is the numerator of $[a_1, \dots, a_k]$ in lowest terms. For the chain of $\frac1n(1,q)$, Theorem 4.3.19 gives $[a_1, \dots, a_k] = n/q$ with $\gcd(n, q) = 1$, so $\det M = n$. $\square$

*Proof of Theorem 4.5.12.* Take $B = 0$ first, and write $\Delta_Y = S' + \sum_i c_i E_i$. The curve $S'$ is the only non-exceptional component of $\Delta_Y$ near $f^{-1}(P)$. Since $f^*(K_X + S) \cdot E_j = 0$, the coefficients satisfy $(K_Y + \Delta_Y) \cdot E_j = 0$ for every $j$. By adjunction on $Y$, $K_Y \cdot E_j = -2 - E_j^2 = a_j - 2$. The curve $E_j$ meets $E_{j-1}$ and $E_{j+1}$ once each, when they exist, and $S'$ meets only $E_1$, once. With the conventions $c_0 = 1$ and $c_{k+1} = 0$, the equations become

$$a_j - 2 + c_{j-1} - a_j c_j + c_{j+1} = 0 \quad (1 \le j \le k).$$

The intersection matrix $-M$ is negative definite (Theorem 4.3.1), so this linear system for $c_1, \dots, c_k$ has at most one solution. Set $c_i = 1 - p_i/m$ for $0 \le i \le k+1$. Then $c_0 = 1$ because $p_0 = 0$, and $c_{k+1} = 0$ because $p_{k+1} = m$. Substituting,

$$a_j - 2 + 1 - a_j + 1 + \frac{-p_{j-1} + a_j p_j - p_{j+1}}{m} = 0,$$

by the recursion. So these are the coefficients. The curve $S'$ meets only $E_1$ near $f^{-1}(P)$, at $q$ with $(E_1 \cdot S')_q = 1$, so the coefficient of $\operatorname{Diff}_{S^\nu}(0)$ at $q$ is $c_1 = 1 - p_1/m = 1 - \frac1m$. When $k = 0$, the coefficient is $0 = 1 - \frac11$.

For general $B$, part 1 of Proposition 4.5.4 gives $\operatorname{Diff}_{S^\nu}(B) = \operatorname{Diff}_{S^\nu}(0) + \sum_j b_j (f^*B_j)|_{S'}$. Write $f^*B_j = B_j' + \sum_i e_{i,j} E_i$. The vector $e_j = (e_{1,j}, \dots, e_{k,j})$ solves $M e_j = v_j$, where $v_j$ is the vector of the integers $(B_j' \cdot E_i)$, since $f^*B_j \cdot E_i = 0$. By Cramer's rule, $m e_{i,j} \in \mathbb{Z}$. So $m (f^*B_j \cdot S')_q = m e_{1,j} + m (B_j' \cdot S')_q$ is an integer. It is nonnegative because $f^*B_j \ge 0$ (Corollary P5.8.5) does not contain $S'$. If $P \notin B_j$, then $B_j'$ does not meet $f^{-1}(P)$, $v_j = 0$, $e_j = 0$ and $m_j = 0$. If $P \in B_j$, then $v_j \ne 0$ and $v_j \ge 0$. The entries of $e_j$ are nonnegative by Corollary P5.8.5. If $e_{1,j} = 0$, then the first equation $a_1 e_{1,j} - e_{2,j} = (v_j)_1$ forces $e_{2,j} = 0$ and $(v_j)_1 = 0$, and inductively along the chain $e_j = 0$ and $v_j = 0$, a contradiction. So $e_{1,j} > 0$ and $m_j > 0$. $\square$

### Exercises

1. (A) Compute the continuants and the coefficients $c_i$ for the chain $[2, 2, \dots, 2]$ of length $k$, the $A_k$ singularity $\frac1{k+1}(1, k)$. Show that $\operatorname{Diff}_S(0) = \frac{k}{k+1} P$ for $S$ the image of a curve meeting an end curve transversally.
2. (A) Verify that $\frac{12}{7} = [2, 4, 2]$ and compute the coefficients for $\frac1{12}(1,7)$, with $S'$ meeting the first curve. Check one of the equations $(K_Y + \Delta_Y) \cdot E_j = 0$ directly.
3. (B) For the $A_k$ singularity of Exercise 1, let $S'$ meet the middle curve $E_j$, $1 < j < k$, transversally. Compute $\Delta_Y$ for $B = 0$ and show that the coefficient of the different is $j(k+1-j)/(k+1)$, which is at least 1, with equality only for $k = 3$ and $j = 2$. (This configuration is not plt, consistent with Theorem 4.5.13.)
4. (B) In the setting of Theorem 4.5.12, let $B = b B_1$, where $B_1'$ meets the other end curve $E_k$ transversally in one point. Show that $m_1 = 1$, so the coefficient of the different is $1 - \frac{1 - b}{m}$. (Use the adjugate of $M$: the $(1, k)$ entry of $M^{-1}$ is $1/m$.)
5. (B) Let $X = \frac1n(1, q)$, with $n/q = [a_1, \dots, a_k]$, and let $S$ and $T$ be the two toric curves. Show that $\Delta_Y$ for the toric pair $(X, S + T)$ is $S' + T' + \sum_i E_i$, and deduce that $c_i(S) + c_i(T) = 1 - a(E_i, X, 0)$ for the coefficients $c_i$ computed from the two ends. Use Example 4.5.15 to show that the discrepancies of $\frac17(1,3)$ are $-\frac37, -\frac27, -\frac17$, and check them against $K_Y \cdot E_j = a_j - 2$.
6. (C) Let $p_i$ be the continuants of $[a_1, \dots, a_k]$ and $r_i$ those of the reversed chain. Show that $p_k \, r_k \equiv 1 \pmod m$, and deduce from Theorem 4.3.19 that the reversed chain is the chain of $\frac1n(1, q')$, where $q q' \equiv 1 \pmod n$.

### Lean

Continuants and the coefficient formula are elementary arithmetic and could be stated in Lean over `ℚ` with Mathlib's matrices. The library has no resolution of surface singularities and no different, so the geometric statement is not in Lean.

### Notes and history

The formula $1 - \frac1m + \sum_j m_j b_j/m$ is the starting point of the theory of complements and of the boundedness results of Shokurov and of Prokhorov, where the coefficients $1 - \frac1m$ are the "standard coefficients". The formula appears in Sho92 and Kol92, Chapter 16, and in the form used here in KM98, Section 4.1, and Kol13, Chapter 3. The classification of plt surface pairs in Theorem 4.5.13 rests on the classification of the dual graphs of log terminal surface singularities, which goes back to the 1980s; KM98, Section 4.1, gives a complete account.
