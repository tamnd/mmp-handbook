---
title: The canonical class of a normal surface
nodes: []
sources: [KM98, Kol13, Rei87, Har77]
reads_with: [KM98:ch4, Rei87:ch4]
requires: [P5.5, P5.8, P5.12, P3.11, 4.1, 4.2, 4.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The canonical class of a normal surface

### Statement

Let $X$ be a normal projective surface and $f \colon Y \to X$ a resolution. Fix a nonzero rational 2-form $\omega$ on $X$; it is also a rational 2-form on $Y$, since $f$ is birational. For $x \in T_0$ let $E_1, \dots, E_r$ be the curves over $x$, with matrix $M_x$, and write $p_a(E_j)$ for the arithmetic genus of $E_j$.

**Definition 2.3.19 (the canonical class and the discrepancy divisor).** The *canonical divisor* of $X$ is the Weil divisor $K_X = \operatorname{div}_X(\omega)$ of Definition 4.1.1, and $K_Y = \operatorname{div}_Y(\omega)$, so that $K_X = f_*K_Y$. The *discrepancy divisor* of $f$ is the exceptional $\mathbb{Q}$-divisor
$$A = K_Y - f^*K_X = \sum_i a_i E_i,$$
the sum over all exceptional curves, where $f^*$ is the Mumford pullback of Corollary P5.8.5. The numbers $a_i$ are the *numerical discrepancies* of the $E_i$, and $A_x$ is the part of $A$ over $x$.

The divisor $K_X$ depends on $\omega$ only up to a principal divisor, and replacing $\omega$ by $h\omega$ changes $K_Y$ by $\operatorname{div}_Y(h) = f^*\operatorname{div}_X(h)$. So $A$ does not depend on $\omega$. The numbers $a_i$ are the numerical discrepancies of Definition 4.3.3 computed on the germ of $X$ at $x$.

**Theorem 2.3.20 (computing the canonical class).** Let $k_j = K_Y \cdot E_j = 2p_a(E_j) - 2 - E_j^2$ for the curves $E_j$ over $x$, and $a = (a_1, \dots, a_r)$.

1. $M_x a = k$. So $a = M_x^{-1} k$ is determined by the intersection matrix and the genera, and $(\det M_x) \, a \in \mathbb{Z}^r$.
2. $K_X^2 = K_Y^2 - A^2$, where $A^2 = \sum_x A_x^2$ and $A_x^2 = \sum_j a_j k_j \le 0$, with equality if and only if $A_x = 0$. So $K_X^2 \ge K_Y^2$.
3. For every integral curve $C$ on $X$ with strict transform $\tilde C$, $K_X \cdot C = K_Y \cdot \tilde C - A \cdot \tilde C$.
4. If $f$ is the minimal resolution (Definition 4.3.4), then $A \le 0$, so $K_X \cdot C \ge K_Y \cdot \tilde C$ for every integral curve $C$. In this case $A_x = 0$ if and only if every $E_j$ over $x$ is a $(-2)$-curve, that is, $x$ is a rational double point.
5. If $x$ is a rational singularity, then $K_X$ is $\mathbb{Q}$-Cartier at $x$, its index at $x$ is the order of $a$ in $\mathbb{Q}^r / \mathbb{Z}^r$, which divides $|\det M_x|$, and the $a_i$ are the discrepancies $a(E_i, X, 0)$ of Volume 4.

Lean: not yet in Lean.

**Corollary 2.3.21 (klt surfaces are $\mathbb{Q}$-factorial).** Let $k = \mathbb{C}$ and let $X$ be a normal projective surface that is klt. Then every singular point of $X$ is a quotient singularity and a rational singularity, $X$ is $\mathbb{Q}$-factorial, and $K_X$ and every Weil divisor have a multiple that is Cartier, of the form given in Corollary 2.3.14.

Lean: not yet in Lean.

### Proof in words

The canonical class is the one Weil divisor that every surface carries, and Mumford's pullback lifts it: $f^*K_X$ is $K_Y$ corrected by the exceptional divisor $A$ that makes it orthogonal to the exceptional curves. Orthogonality is a linear system $M_x a = k$, and adjunction on each $E_j$ gives the right side from the genus and the self-intersection. The same orthogonality gives $K_Y \cdot A = A^2$, and then $K_X^2 = (K_Y - A)^2 = K_Y^2 - A^2$; the matrix is negative definite, so the canonical square goes up under contraction. On the minimal resolution the discrepancies are at most 0, which is the inequality $K_X \cdot C \ge K_Y \cdot \tilde C$ used when the program passes from a surface to its contraction. At a rational singularity Section 2 turns the numerical statement into a statement about Cartier divisors. For a klt surface the singularities are quotients, hence rational, so the whole of Section 2 applies.

### Examples

**Example 2.3.22 (the cone $X_n$).** In Example 2.3.8, $K_{F_n} = -2C_- - (n+2)F$ by Example P5.12.8, and $f_*C_- = 0$, so $K_{X_n} = -(n+2)\ell$. Here $k = K_{F_n} \cdot C_- = 2n - (n+2) = n - 2$, and $-na = n - 2$ gives
$$a = -\frac{n-2}{n}, \qquad f^*K_{X_n} = K_{F_n} + \frac{n-2}{n} C_- = -\frac{n+2}{n} (C_- + nF) = -\frac{n+2}{n} f^*H,$$
in accordance with Example 4.3.7 and $K_{X_n} = -(n+2)\ell \equiv -\frac{n+2}{n} H$. Then
$$K_{X_n}^2 = \frac{(n+2)^2}{n^2} \, n = \frac{(n+2)^2}{n} = 8 + \frac{(n-2)^2}{n} = K_{F_n}^2 - A^2,$$
with $A^2 = a k = -\frac{(n-2)^2}{n}$. For a line, $K_{X_n} \cdot \ell = -\frac{n+2}{n}$ and $K_{F_n} \cdot F - A \cdot F = -2 + \frac{n-2}{n}$, the same number. The index of $K_{X_n}$ at $v$ is the order of $\frac{n-2}{n}$ in $\mathbb{Q}/\mathbb{Z}$, which is $\frac{n}{\gcd(n, 2)}$. It is $n$ for $n$ odd and $\frac n2$ for $n$ even; for $n = 4$ it is $2$, as in Example 4.3.23. The surface $X_n$ is the weighted projective plane $\mathbb{P}(1, 1, n)$, and $\frac{(n+2)^2}{n}$ is the formula $\frac{(1 + 1 + n)^2}{1 \cdot 1 \cdot n}$ for the anticanonical degree of a weighted projective plane; this identification is not used here.

**Example 2.3.23 (the quadric cone).** For $n = 2$, $a = 0$ and $K_{X_2} = -4\ell \sim -2H$ is Cartier, with $K_{X_2}^2 = 8 = K_{F_2}^2$. The vertex is the $A_1$ singularity of Example 4.1.8, the first case of part 4 of Theorem 2.3.20.

**Example 2.3.24 (the elliptic cone).** In Counterexample 2.3.18, $E$ has genus 1 and $E^2 = -d$, so $k = 0 - (-d) = d$ and $a = \frac{d}{-d} = -1$, as Corollary 4.2.20 says with $g = 1$. Here $K_X \sim 0$ is Cartier although the vertex is not rational, so part 5 of Theorem 2.3.20 is a sufficient condition only. Every coefficient of $A_x = -E$ is an integer, consistent with $K_X$ being Cartier, but numerically Cartier does not imply Cartier for other divisors at this point. For the projective cone over a plane cubic, Problem 6 computes $K_X^2 = 3$ from $K_Y^2 = 0$ and $A^2 = -3$.

**Example 2.3.25 (the $E_8$ singularity).** In Example 2.3.17 every $E_j$ is a $(-2)$-curve, so $k = 0$, $a = 0$ and $A_x = 0$. The canonical divisor is Cartier at $x$, as every Weil divisor is, and $f^*K_X = K_Y$ near the fibre. More generally, part 4 of Theorem 2.3.20 says that the rational double points are exactly the points where the minimal resolution is crepant, which is Theorem 4.3.11 in the language of discrepancies.

**Counterexample 2.3.26 (a resolution that is not minimal).** Let $X$ be a smooth projective surface and $f \colon Y \to X$ the blow-up of a point $p$, with exceptional $(-1)$-curve $E$. Then $k = -2 + 1 = -1$ and $a = \frac{-1}{-1} = 1$, so $K_Y = f^*K_X + E$, as in Theorem P5.6.3. For a curve $C$ through $p$ of multiplicity $m$, $\tilde C \cdot E = m$ and part 3 gives $K_X \cdot C = K_Y \cdot \tilde C - m < K_Y \cdot \tilde C$. So the inequality of part 4 needs the resolution to be minimal, and $K_X^2 = K_Y^2 - A^2 = K_Y^2 + 1$ is the familiar change of $K^2$ under a blow-up.

### Proof

*Theorem 2.3.20.* (1) By Corollary P5.8.5, $f^*K_X \cdot E_j = 0$ for every $j$. So $K_Y \cdot E_j = A \cdot E_j = \sum_i a_i E_i \cdot E_j$, the curves over other points being disjoint from $E_j$. This is $M_x a = k$. The adjunction formula of Theorem P5.5.14 gives $K_Y \cdot E_j + E_j^2 = 2p_a(E_j) - 2$, which is the formula for $k_j$. The matrix $M_x$ is invertible by Theorem P5.8.3, and Cramer's rule gives $M_x^{-1} = (\det M_x)^{-1} \operatorname{adj}(M_x)$, with $\operatorname{adj}(M_x)$ an integer matrix. So $(\det M_x) a = \operatorname{adj}(M_x) k \in \mathbb{Z}^r$.

(2) By the definition of Mumford's pairing, $K_X^2 = (f^*K_X)^2 = (K_Y - A)^2 = K_Y^2 - 2 K_Y \cdot A + A^2$. By (1), $K_Y \cdot A = \sum_i a_i K_Y \cdot E_i = \sum_i a_i A \cdot E_i = A^2$. So $K_X^2 = K_Y^2 - A^2$. The parts $A_x$ for distinct $x$ are orthogonal, and $A_x^2 = \sum_j a_j A \cdot E_j = \sum_j a_j k_j$. By negative definiteness, $A_x^2 \le 0$ with equality only for $A_x = 0$.

(3) By part 5 of Theorem 2.3.4, $K_X \cdot C = f^*K_X \cdot f^*C = f^*K_X \cdot \tilde C$, since $f^*C - \tilde C$ is exceptional. And $f^*K_X \cdot \tilde C = K_Y \cdot \tilde C - A \cdot \tilde C$.

(4) By Proposition 4.3.5, $K_Y \cdot E_j \ge 0$ for every $j$ on the minimal resolution, so $A \cdot E_j = k_j \ge 0$, that is $(-A) \cdot E_j \le 0$, and Theorem P5.8.2 gives $-A \ge 0$. Then $-A \cdot \tilde C \ge 0$ by Proposition P5.5.5, since $\tilde C$ is not exceptional, and (3) gives the inequality. If $A_x = 0$, then $k_j = 0$ for every $j$ over $x$, so $E_j^2 = 2p_a(E_j) - 2$; since $E_j^2 < 0$ and $p_a(E_j) \ge 0$, this forces $p_a(E_j) = 0$ and $E_j^2 = -2$, and an integral curve of arithmetic genus 0 is a smooth rational curve. So every $E_j$ is a $(-2)$-curve, and Proposition P5.8.17 says that $x$ is a rational double point. Conversely, if every $E_j$ is a $(-2)$-curve, then $k = 0$ and $a = M_x^{-1} 0 = 0$.

(5) Choose $\omega$ so that $K_X$ is a Weil divisor and let $b_j \in \mathbb{Z}$ be the coefficient of $E_j$ in $K_Y = \operatorname{div}_Y(\omega)$. Then $c_x(K_X) = b - a$, which lies in $\mathbb{Z}^r$ exactly when $a$ does, and more generally $c_x(mK_X) = mb - ma$. By part 3 of Theorem 2.3.13, the index of $K_X$ at $x$ is the least $m \ge 1$ with $ma \in \mathbb{Z}^r$, the order of $a$ in $\mathbb{Q}^r/\mathbb{Z}^r$, and it divides $|\det M_x|$ by (1). By Corollary 2.3.14, near $x$ the Mumford pullback $f^*K_X$ is $\frac1m f^*(mK_X)$, the pullback used in the definition of discrepancies in Volume 4, so $K_Y = f^*K_X + \sum_i a_i E_i$ near $f^{-1}(x)$ is the defining relation of the discrepancies $a(E_i, X, 0)$. $\square$

*Corollary 2.3.21.* Let $x$ be a singular point. The germ of $X$ at $x$ is klt, so by Theorem 4.3.18 it is analytically isomorphic to a quotient $(\mathbb{C}^2/G, 0)$. A klt pair is dlt, and dlt singularities are rational by KM98, Theorem 5.22. So every singular point of $X$ is rational, and Corollary 2.3.14 gives the rest. $\square$

### Exercises

1. (A) For the singularity $\frac15(1,2)$, whose minimal resolution is a chain of a $(-3)$-curve $E_1$ and a $(-2)$-curve $E_2$ (Example 4.3.21), compute $k$, $a$, $A_x^2$ and the index of $K_X$ at $x$.
2. (A) A single smooth curve $E$ of genus $g$ with $E^2 = -d$ is contracted to a point $x$. Show that $a = -1 - \frac{2g-2}{d}$ and $A_x^2 = -\frac{(2g - 2 + d)^2}{d}$, and compare with Corollary 4.2.20.
3. (A) Let $X$ be a normal projective surface with only rational double points. Show that $K_X$ is Cartier, that $K_X^2 = K_Y^2$ for the minimal resolution, and that $K_X \cdot C = K_Y \cdot \tilde C$ for every curve $C$.
4. (B) Let $f \colon Y \to X$ be the minimal resolution and $g \colon Y' \to Y$ the blow-up of a point of an exceptional curve. Compute the discrepancy divisor of $f \circ g$ in terms of $A$, and check part 2 of Theorem 2.3.20 for $f \circ g$ directly.
5. (B) Let $x$ be a point whose minimal resolution has a single exceptional curve, a smooth rational curve $E$ with $E^2 = -n$ and $n \ge 2$. Show that $K_X$ is Cartier at $x$ if and only if $n = 2$, and that $2K_X$ is Cartier at $x$ if and only if $n \in \{2, 4\}$.
6. (C) Let $X$ be a normal projective surface, $f \colon Y \to X$ the minimal resolution, and $C \subset X$ an integral curve with $K_X \cdot C < 0$ and $C^2 < 0$. Show that $\tilde C^2 \le C^2$, using $f^*C = \tilde C + Z$ with $Z \ge 0$ exceptional. Deduce from part 4 of Theorem 2.3.20 and the adjunction formula $K_Y \cdot \tilde C + \tilde C^2 = 2p_a(\tilde C) - 2$ that $\tilde C$ is a $(-1)$-curve on $Y$. Give an example with $X = X_n$ for some $n$, or explain why none exists there.

### Lean

Nothing in this section is in Lean. The canonical divisor of a normal surface and its discrepancies need Weil divisors on singular schemes and Kähler differentials on a resolution, which the project library does not have. The linear algebra of part 1 of Theorem 2.3.20, that $(\det M) M^{-1}$ has integer entries, is `Matrix.adjugate` and `Matrix.mul_adjugate` in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

The relation $K_Y = f^*K_X + \sum a_i E_i$ with $a$ computed from $M a = k$ appears in Mumford's 1961 paper for the Mumford pullback of the canonical divisor, and it is the starting point of the classification of log terminal and log canonical surface singularities in KM98, Section 4.1, and in Kollár's book (Kol13, Chapter 3). Reid's young person's guide (Rei87) treat the Du Val case and the identity $K_X^2 = K_Y^2$ for crepant resolutions. The formula $K_X^2 = K_Y^2 - A^2$ is the reason that the contraction of a $K$-negative extremal curve in the log minimal model program for surfaces increases $K^2$ by a positive rational number, and part 4 of Theorem 2.3.20 compares $K_X$ with $K_Y$ on curves, which is how the program for a surface with quotient singularities is related to the classical program on its minimal resolution. The facts about ruled surfaces used in Problem 6 are in Har77, Section V.2. KM98, Proposition 4.11, shows that a numerically dlt surface, defined by the numerical discrepancies of Definition 2.3.19 without assuming that $K_X$ is $\mathbb{Q}$-Cartier, is $\mathbb{Q}$-factorial, which extends Corollary 2.3.21.
