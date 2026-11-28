---
title: Log canonical thresholds
nodes: []
sources: [Kol97, KM98, Laz04, Mus06, Hir64]
reads_with: [Kol97:sec8, Laz04:ch9]
requires: [4.1, 4.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Log canonical thresholds

### Statement

Throughout the chapter $k$ is an algebraically closed field of characteristic 0, and varieties have dimension at least 2 unless the text says otherwise. A pair that is lc stays lc when a small multiple of an effective divisor is added to the boundary, and stops being lc when the multiple is large. The threshold between the two is the first number of this chapter.

**Definition 4.6.1 (log canonical threshold of a divisor).** Let $(X, \Delta)$ be an lc pair and $D$ an effective $\mathbb{R}$-Cartier divisor on $X$. The *log canonical threshold* of $D$ with respect to $(X, \Delta)$ is
$$\operatorname{lct}(X, \Delta; D) = \sup\{ t \ge 0 : (X, \Delta + tD) \text{ is lc} \}.$$
For a point $x \in X$, the *local threshold* $\operatorname{lct}_x(X, \Delta; D)$ is the supremum of the $t \ge 0$ such that $(X, \Delta + tD)$ is lc on some open neighbourhood of $x$. When $\Delta = 0$ the notation is $\operatorname{lct}(X; D)$. The set in the definition contains $t = 0$, so the threshold lies in $[0, \infty]$, and it is $\infty$ only if $D = 0$, or, for the local threshold, if $x \notin \operatorname{Supp} D$.

The pair $(X, \Delta + tD)$ is a pair for every $t \ge 0$, because $K_X + \Delta$ and $D$ are $\mathbb{R}$-Cartier. Toric and arrangement computations are easier with ideals than with divisors, so the definition also has a version for ideals. For a divisor $E$ over $X$ and a nonzero ideal $\mathfrak{a} \subset \mathcal{O}_X$, put $\operatorname{ord}_E \mathfrak{a} = \min\{ \operatorname{ord}_E(g) : g \in \mathfrak{a}_\eta \}$, where $\eta$ is the generic point of $c_X(E)$. The minimum is attained on any set of generators of $\mathfrak{a}_\eta$.

**Definition 4.6.2 (thresholds of ideals).** Let $(X, \Delta)$ be a pair, $\mathfrak{a} \subset \mathcal{O}_X$ a nonzero ideal and $c \ge 0$. The *discrepancy* of a divisor $E$ over $X$ with respect to the triple $(X, \Delta, \mathfrak{a}^c)$ is
$$a(E; X, \Delta, \mathfrak{a}^c) = a(E, X, \Delta) - c \operatorname{ord}_E \mathfrak{a},$$
and the triple is *lc* if $a(E; X, \Delta, \mathfrak{a}^c) \ge -1$ for every divisor $E$ over $X$. If $(X, \Delta)$ is lc, the *log canonical threshold* of $\mathfrak{a}$ is $\operatorname{lct}(X, \Delta; \mathfrak{a}) = \sup\{ c \ge 0 : (X, \Delta, \mathfrak{a}^c) \text{ is lc} \}$, and $\operatorname{lct}_x(X, \Delta; \mathfrak{a})$ is defined as for divisors.

If $\mathfrak{a} = \mathcal{O}_X(-D)$ for an effective Cartier divisor $D$, Theorem 4.1.12 gives $a(E, X, \Delta + cD) = a(E, X, \Delta) - c \operatorname{ord}_E(g)$ with $g$ a local equation of $D$ near the generic point of $c_X(E)$, and $\operatorname{ord}_E(g) = \operatorname{ord}_E \mathfrak{a}$. So $(X, \Delta, \mathfrak{a}^c)$ is lc if and only if $a(E, X, \Delta + cD) \ge -1$ for every $E$, that is, if and only if $(X, \Delta + cD)$ is lc (Theorem 4.2.3 and part 2 of Theorem 4.1.21), and the two thresholds agree.

A *log resolution* of the triple $(X, \Delta, \mathfrak{a})$ is a log resolution $f \colon Y \to X$ of $(X, \Delta)$ (Definition 4.2.9) such that $\mathfrak{a} \mathcal{O}_Y = \mathcal{O}_Y(-F)$ for an effective divisor $F$, and $f^{-1}_* \Delta + \operatorname{Exc}(f) + F$ has snc support. A log resolution of a pair $(X, \Delta + D)$ gives the same data for the divisor $D$ with $F = f^* D$: every component of $\operatorname{Supp} f^* D$ is either the strict transform of a component of $D$ or $f$-exceptional, because a component that is not exceptional maps onto a prime divisor inside $\operatorname{Supp} D$. Hironaka's theorem (Theorem 4.2.10) also gives log resolutions of triples, by a resolution of the pair followed by a principalization of the ideal (Hir64; Laz04, Chapter 9).

**Theorem 4.6.3 (thresholds on a log resolution).** Let $(X, \Delta)$ be a pair and $\mathfrak{a}$ a nonzero ideal, with a log resolution $f \colon Y \to X$ of $(X, \Delta, \mathfrak{a})$. Write $K_Y + \Delta_Y = f^*(K_X + \Delta)$, and let $F_1, \dots, F_N$ be the prime divisors in the support of $f^{-1}_* \Delta + \operatorname{Exc}(f) + F$, with
$$\Delta_Y = \sum_i b_i F_i, \qquad F = \sum_i e_i F_i.$$
For a divisor $D$ the same statements hold with $F = f^* D$ and $f$ a log resolution of $(X, \Delta + D)$.

1. For $c \ge 0$, the triple $(X, \Delta, \mathfrak{a}^c)$ is lc if and only if $b_i + c e_i \le 1$ for every $i$.
2. If $(X, \Delta)$ is lc, then
$$\operatorname{lct}(X, \Delta; \mathfrak{a}) = \min\Big\{ \frac{1 - b_i}{e_i} : e_i > 0 \Big\},$$
the triple is lc at $c = \operatorname{lct}(X, \Delta; \mathfrak{a})$, and the threshold is positive if and only if no $F_i$ with $b_i = 1$ has $e_i > 0$. In every case $\operatorname{lct}(X, \Delta; \mathfrak{a}) = \inf\{ A(E, X, \Delta) / \operatorname{ord}_E \mathfrak{a} \}$ over the divisors $E$ over $X$ with $\operatorname{ord}_E \mathfrak{a} > 0$, and the infimum is attained by one of the $F_i$.
3. For a closed point $x \in X$, $\operatorname{lct}_x(X, \Delta; \mathfrak{a})$ is the same minimum over the $i$ with $e_i > 0$ and $x \in f(F_i)$.

Lean: not yet in Lean. The threshold of a divisor is the definition `MinimalModel.lct`.

The proof uses only that $f$ is proper and birational, that $Y$ is smooth, that $\mathfrak{a} \mathcal{O}_Y = \mathcal{O}_Y(-F)$, and that $\Delta_Y + F$ has snc support. Section 2 applies the theorem in this form to a toric model, where the exceptional set need not be a divisor.

**Corollary 4.6.4 (the local threshold).** Let $(X, \Delta)$ be lc and $\mathfrak{a}$ a nonzero ideal. The function $x \mapsto \operatorname{lct}_x(X, \Delta; \mathfrak{a})$ on the closed points of $X$ takes finitely many values, it is lower semicontinuous, that is, $\{x : \operatorname{lct}_x \le t\}$ is closed for every $t$, and $\operatorname{lct}(X, \Delta; \mathfrak{a}) = \min_x \operatorname{lct}_x(X, \Delta; \mathfrak{a})$.

Lean: not yet in Lean.

**Proposition 4.6.5 (two upper bounds).** Let $(X, \Delta)$ be lc, $D = \sum_j r_j D_j$ an effective $\mathbb{R}$-Cartier divisor with prime components $D_j$, and $x \in X$ a closed point.

1. If $x \in D_j$ and $d_j$ is the coefficient of $D_j$ in $\Delta$, then $\operatorname{lct}_x(X, \Delta; D) \le (1 - d_j) / r_j$.
2. If $X$ is smooth at $x$, $n = \dim X$ and $x \notin \operatorname{Supp} \Delta$, then $\operatorname{lct}_x(X, \Delta; D) \le n / \operatorname{mult}_x D$, where $\operatorname{mult}_x D = \sum_j r_j \operatorname{mult}_x D_j$.

Lean: not yet in Lean.

### Proof in words

Pull everything back to the log resolution. The crepant pullback does not change discrepancies, and on $Y$ the ideal becomes the divisor $F$. So the triple on $X$ has the same discrepancies as the sub-pair $(Y, \Delta_Y + cF)$, whose boundary has snc support and coefficients $b_i + c e_i$. For an snc sub-pair, being lc is a condition on the coefficients alone. Each condition $b_i + c e_i \le 1$ is a bound $c \le (1 - b_i)/e_i$, so the threshold is the smallest of finitely many ratios. Near a point $x$ only the divisors $F_i$ whose image contains $x$ matter, which gives the local threshold, and the closed sets $f(F_i)$ show that it can only drop on closed subsets. The two upper bounds test the definition on one divisor each: a component of $D$, and the blow-up of the point.

### Examples

**Example 4.6.6 (snc divisors).** Let $X$ be smooth and $D = \sum_j r_j D_j$ with snc support and every $r_j > 0$. The identity is a log resolution of $(X, D)$, with $\Delta_Y = 0$ and $F = D$. Part 2 of the theorem gives $\operatorname{lct}(X; D) = \min_j 1 / r_j$, and part 3 gives $\operatorname{lct}_x(X; D) = \min\{ 1/r_j : x \in D_j \}$. For $D = \{x^2 y^3 = 0\}$ in $\mathbb{A}^2$ the threshold is $\frac13$. The bound of Proposition 4.6.5, part 2, gives $\frac25$ at the origin, so it is not sharp.

**Example 4.6.7 (the cusp).** Let $C = \{y^2 = x^3\} \subset \mathbb{A}^2$. Example 4.2.16 gives a log resolution $f$ with three exceptional curves. Its proof, from Problem 1 of Chapter 1, gives
$$f^* C = C_3 + 2E_1 + 3E_2 + 6E_3, \qquad K_Y = f^* K_{\mathbb{A}^2} + E_1 + 2E_2 + 4E_3,$$
so $\Delta_Y = -E_1 - 2E_2 - 4E_3$, and the log discrepancies are $A(E_1) = 2$, $A(E_2) = 3$, $A(E_3) = 5$. The ratios $\frac{1 - b_i}{e_i}$ are $1$ for $C_3$, $\frac22 = 1$ for $E_1$, $\frac33 = 1$ for $E_2$ and $\frac56$ for $E_3$. So
$$\operatorname{lct}(\mathbb{A}^2; C) = \operatorname{lct}_0(\mathbb{A}^2; C) = \frac56,$$
which matches the coefficients $tC_3 + (2t - 1)E_1 + (3t - 2)E_2 + (6t - 4)E_3$ of Example 4.2.16. At a point of $C \setminus \{0\}$ the curve is smooth, and the threshold is 1. So $\operatorname{lct}_x$ is $\frac56$ at the origin, $1$ on $C \setminus \{0\}$ and $\infty$ off $C$, a lower semicontinuous function, as Corollary 4.6.4 says. The bound $n / \operatorname{mult}_0 C = \frac22 = 1$ is not sharp: the divisor $E_3$ that computes the threshold appears only after three blow-ups.

**Example 4.6.8 (a generic central arrangement).** Let $\ell_1, \dots, \ell_d$ be linear forms on $\mathbb{A}^n$ with $d \ge n \ge 2$, such that any $n$ of them are linearly independent, and let $D = \sum_j H_j$ with $H_j = \{\ell_j = 0\}$. Then
$$\operatorname{lct}(\mathbb{A}^n; D) = \operatorname{lct}_0(\mathbb{A}^n; D) = \min\Big\{ 1, \frac{n}{d} \Big\}.$$
Let $f \colon Y \to \mathbb{A}^n$ be the blow-up of the origin, with exceptional divisor $E$. Then $f^* H_j = H_j' + E$, since each $\ell_j$ vanishes to order 1 at the origin, and $K_Y = f^* K + (n-1)E$ (Lemma 4.1.20). Check that $f$ is a log resolution. By symmetry it is enough to work in the chart $x_1 = u_1$, $x_i = u_1 u_i$ for $i \ge 2$, where $E = \{u_1 = 0\}$ and $f^* \ell_j = u_1 m_j$ with $m_j(u) = \ell_j(1, u_2, \dots, u_n)$, so that $H_j' = \{m_j = 0\}$. Let $p$ be a point of the chart and $S$ the set of $j$ with $m_j(p) = 0$. Then every $\ell_j$ with $j \in S$ vanishes at the nonzero vector $q = (1, p_2, \dots, p_n)$, so $|S| \le n - 1$ by the hypothesis, and the forms $\ell_j$ with $j \in S$ are independent. Their differentials $dm_j$ are the restrictions of the $\ell_j$ to $\{x_1 = 0\}$, in the coordinates $u_2, \dots, u_n$. If $\sum_{j \in S} c_j \ell_j$ vanishes on $\{x_1 = 0\}$, then it is $\lambda x_1$ for some $\lambda$, and evaluating at $q$ gives $\lambda = 0$, so every $c_j = 0$. Hence the $dm_j$ for $j \in S$ are independent and do not involve $du_1$, and $E + \sum_j H_j'$ is snc at $p$. So $f$ is a log resolution with
$$\Delta_Y = -(n-1)E, \qquad f^* D = \sum_j H_j' + dE.$$
The ratios are $1$ for each $H_j'$ and $\frac{n}{d}$ for $E$. For $n = 3$ and four general planes the threshold is $\frac34$, and for $d$ lines through the origin of $\mathbb{A}^2$ with distinct slopes it is $\frac2d$, in agreement with Example 4.2.7 for $d = 3$.

**Example 4.6.9 (a non-generic arrangement).** Let $D = \{xyz(x - y) = 0\} \subset \mathbb{A}^3$, the sum of the four planes $H_1 = \{x = 0\}$, $H_2 = \{y = 0\}$, $H_3 = \{z = 0\}$ and $H_4 = \{x = y\}$. The planes $H_1$, $H_2$ and $H_4$ contain the line $L = \{x = y = 0\}$, so the hypothesis of the last example fails. At the origin $\operatorname{mult}_0 D = 4$, and the blow-up of the origin gives the bound $\frac34$. The blow-up of $L$ does better. The line $L$ has codimension 2, and $\operatorname{mult}_L D = 3$, since $x$, $y$ and $x - y$ vanish to order 1 along $L$ and $z$ does not vanish on $L$. Lemma 4.1.20 gives $a(E_L, \mathbb{A}^3, tD) = 1 - 3t$, which is at least $-1$ only for $t \le \frac23$. So $\operatorname{lct}_0(\mathbb{A}^3; D) \le \frac23$.

The blow-up $f \colon Y \to \mathbb{A}^3$ of $L$ is a log resolution. It is covered by two charts. In the first, $x = u$, $y = us$, $z = z$, and
$$f^*(xyz(x - y)) = u^3 \, s \, (1 - s) \, z,$$
with $E = \{u = 0\}$, $H_2' = \{s = 0\}$, $H_4' = \{s = 1\}$ and $H_3' = \{z = 0\}$. At each point at most one of $s$ and $1 - s$ vanishes, and $u, s, z$ and $u, 1 - s, z$ are systems of coordinates, so the support is snc. In the second chart, $x = vt$, $y = v$, the pullback is $v^3 t (t - 1) z$, with $H_1' = \{t = 0\}$, and the same argument applies. The centre has codimension 2, so $K_Y = f^* K + E$, and
$$\Delta_Y = -E, \qquad f^* D = H_1' + H_2' + H_3' + H_4' + 3E.$$
The ratios are $1$ for each $H_j'$ and $\frac{1 + 1}{3} = \frac23$ for $E$. So $\operatorname{lct}(\mathbb{A}^3; D) = \frac23$, and by part 3 of the theorem $\operatorname{lct}_x(\mathbb{A}^3; D) = \frac23$ exactly for $x \in L = f(E)$. The threshold is reached along a line, not only at the origin, and the bound of the blow-up of the origin is not sharp.

### Proof

*The theorem.* Fix $c \ge 0$. The divisors over $X$ are the divisors over $Y$, because $f$ is proper and birational. Let $E$ be one of them. By Proposition 4.1.14, $a(E, X, \Delta) = a(E, Y, \Delta_Y)$. The generators of $\mathfrak{a} \mathcal{O}_Y$ near the generic point of $c_Y(E)$ are the pullbacks of the generators of $\mathfrak{a}$ near the generic point of $c_X(E)$, and $\mathfrak{a} \mathcal{O}_Y = \mathcal{O}_Y(-F)$ is generated there by one local equation $h$ of $F$. So $\operatorname{ord}_E \mathfrak{a} = \operatorname{ord}_E(h)$, and Theorem 4.1.12, applied on $Y$, gives
$$a(E; X, \Delta, \mathfrak{a}^c) = a(E, Y, \Delta_Y) - c \operatorname{ord}_E(h) = a(E, Y, \Delta_Y + cF).$$
So the triple is lc if and only if every divisor over $Y$ has $a(E, Y, \Delta_Y + cF) \ge -1$, that is, if and only if the sub-pair $(Y, \Delta_Y + cF)$ is sub-lc. Its boundary is $\sum_i (b_i + c e_i) F_i$, with snc support, and by Corollary 4.2.13, part 1, it is sub-lc if and only if every $b_i + c e_i \le 1$. This is part 1. For a divisor $D$ the same argument works with $\Delta + cD$ in place of the triple: $K_Y + \Delta_Y + c f^* D = f^*(K_X + \Delta + cD)$, so Proposition 4.1.14 gives $a(E, X, \Delta + cD) = a(E, Y, \Delta_Y + c f^*D)$, and $\operatorname{Supp}(\Delta_Y + f^* D)$ is snc.

For part 2, part 1 with $c = 0$ shows that every $b_i \le 1$. The set of $c \ge 0$ with $(X, \Delta, \mathfrak{a}^c)$ lc is then the set of $c \ge 0$ with $c e_i \le 1 - b_i$ for every $i$. The conditions with $e_i = 0$ always hold, so the set is the closed interval from 0 to the stated minimum, which is $\infty$ if every $e_i = 0$. The minimum is attained, so the triple is lc at the threshold. A ratio is 0 if and only if $b_i = 1$ and $e_i > 0$, which gives the criterion for positivity. For the last statement, the triple is lc if and only if $A(E, X, \Delta) - c \operatorname{ord}_E \mathfrak{a} \ge 0$ for every $E$. Since $(X, \Delta)$ is lc, $A(E, X, \Delta) \ge 0$, and the condition for $E$ with $\operatorname{ord}_E \mathfrak{a} = 0$ always holds. So the threshold is $\inf_E A(E, X, \Delta) / \operatorname{ord}_E \mathfrak{a}$. For $E = F_i$ the quotient is $(1 - b_i)/e_i$, so the infimum equals the minimum of part 2 and is attained by an $F_i$.

For part 3, let $U$ be an open neighbourhood of $x$. Then $f^{-1}(U) \to U$ is a log resolution of the restricted triple, and its divisors $F_i \cap f^{-1}(U)$ are those $F_i$ with $f(F_i) \cap U \ne \emptyset$. Every $F_i$ with $x \in f(F_i)$ is among them. By part 1 the triple is lc on $U$ only if $b_i + c e_i \le 1$ for the $i$ with $x \in f(F_i)$. Conversely, the sets $f(F_i)$ are closed, because $f$ is proper. Let $U_0$ be the complement of the union of the $f(F_i)$ that do not contain $x$. On $U_0$ only the $F_i$ with $x \in f(F_i)$ remain, so the triple is lc on $U_0$ if $b_i + c e_i \le 1$ for those $i$. Part 3 follows from the computation of part 2 on $U_0$.

*The corollary.* Fix a log resolution, which exists by Hironaka's theorem, and put $\lambda_i = (1 - b_i)/e_i$ for the $i$ with $e_i > 0$. By part 3, $\operatorname{lct}_x = \min\{\lambda_i : x \in f(F_i)\}$, with the minimum of the empty set equal to $\infty$. So it takes values in the finite set $\{\lambda_i\} \cup \{\infty\}$, and
$$\{ x : \operatorname{lct}_x \le t \} = \bigcup_{\lambda_i \le t} f(F_i)$$
is a finite union of closed sets. Part 2 gives $\operatorname{lct} = \min_i \lambda_i$. If the minimum is attained at $i$, any closed point $x \in f(F_i)$ has $\operatorname{lct}_x \le \lambda_i$. Every $\operatorname{lct}_x$ is at least $\min_i \lambda_i$, so $\operatorname{lct} = \min_x \operatorname{lct}_x$.

*The proposition.* For part 1, the prime divisor $D_j$ is a divisor over $X$ with $a(D_j, X, \Delta + tD) = -d_j - t r_j$. If $(X, \Delta + tD)$ is lc near $x \in D_j$, this is at least $-1$, so $t \le (1 - d_j)/r_j$. For part 2, take $Z = \{x\}$, of codimension $n \ge 2$, in Lemma 4.1.20, applied to $(X, \Delta + tD)$ on a neighbourhood of $x$ that misses $\operatorname{Supp} \Delta$. It gives $a(E_x, X, \Delta + tD) = n - 1 - t \operatorname{mult}_x D$, which is at least $-1$ only if $t \le n / \operatorname{mult}_x D$. $\square$

### Exercises

1. (A) Let $\Delta = \sum_i d_i \{x_i = 0\}$ and $D = \sum_i r_i \{x_i = 0\}$ on $\mathbb{A}^n$ with $0 \le d_i \le 1$ and $r_i \ge 0$, not all zero. Show that $\operatorname{lct}(\mathbb{A}^n, \Delta; D) = \min\{ (1 - d_i)/r_i : r_i > 0 \}$.
2. (A) Show that $\operatorname{lct}(X, \Delta; mD) = \frac1m \operatorname{lct}(X, \Delta; D)$ for every real $m > 0$, and that $D \le D'$ implies $\operatorname{lct}(X, \Delta; D') \le \operatorname{lct}(X, \Delta; D)$.
3. (A) For the arrangement of Example 4.6.9, compute $\operatorname{lct}_x(\mathbb{A}^3; D)$ at every closed point $x$, and check that the function is lower semicontinuous.
4. (B) Let $C \subset \mathbb{A}^2$ be a curve with an ordinary $d$-fold point at the origin: $d \ge 2$ smooth branches with distinct tangent lines. Show that one blow-up of the origin is a log resolution near the origin and that $\operatorname{lct}_0(\mathbb{A}^2; C) = \min\{1, \frac2d\}$. Deduce that the nodal cubic of Example 4.2.17 has threshold 1.
5. (B) Let $X$ be smooth of dimension $n$, $x \in X$ a closed point with maximal ideal $\mathfrak{m}$, and $k \ge 1$. Show that the blow-up of $x$ is a log resolution of $(X, 0, \mathfrak{m}^k)$ and that $\operatorname{lct}_x(X; \mathfrak{m}^k) = \frac{n}{k}$. Deduce that $\operatorname{lct}_x(X; \mathfrak{a}) \le \frac{n}{k}$ for every ideal $\mathfrak{a} \subset \mathfrak{m}^k$.
6. (C) In Example 4.6.9, let $t = \frac23$. Show that the coefficients of the crepant pullback of $(\mathbb{A}^3, \frac23 D)$ to $Y$ are $\frac23$ on each $H_j'$ and $1$ on $E$. Use Lemma 4.2.11 to show that $E$ is the only divisor over $\mathbb{A}^3$ with $a(E, \mathbb{A}^3, \frac23 D) = -1$. So the only lc centre of $(\mathbb{A}^3, \frac23 D)$ is the line $L$, and not the origin.

### Lean

The library defines the threshold of a divisor as `MinimalModel.lct`, the supremum of the $t \ge 0$ such that the pair with the same canonical divisor and boundary $\Delta + tD$ is lc in the sense of `MinimalModel.IsLc`. The library has no thresholds of ideals and no log resolutions, so Theorem 4.6.3 and its corollary are not yet in Lean.

### Notes and history

The log canonical threshold appears in Shokurov's work of 1992 on 3-fold log flips, as the coefficient at which a pair stops being lc. Kol97 studies it at length and proves many of its properties, including the computation on a log resolution and the semicontinuity. Laz04, Chapter 9, gives the same number as the first jumping number of the multiplier ideals $\mathcal{J}(X, \mathfrak{a}^c)$: the threshold is the least $c$ with $\mathcal{J}(X, \mathfrak{a}^c) \ne \mathcal{O}_X$. The threshold of the cusp, $\frac56$, is the first case of the formula $\frac1a + \frac1b$ of Section 2. For arrangements of hyperplanes, Mustaţă (Mus06) proved that the threshold is the minimum of $\operatorname{codim} W / \#\{ j : W \subset H_j \}$ over the nonempty intersections $W$ of the hyperplanes. For a central arrangement the origin is one of them, with ratio $\frac{n}{d}$. Example 4.6.9 is the simplest case where an intersection other than the origin gives the minimum: the line $L$ gives $\frac23$ and the origin gives $\frac34$.
