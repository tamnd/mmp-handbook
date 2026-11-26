---
title: Negativity and the minimal resolution
nodes: []
sources: [Mum61, KM98, Kol13, Rei87]
reads_with: [KM98:ch4, Rei87:ch4]
requires: [P8.10, 4.1, 4.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Negativity and the minimal resolution

### Statement

Let $X$ be a normal surface and $x \in X$ a singular point. Since $X$ is normal, its singular points are isolated, and the study of $x$ is local. So assume that $x$ is the only singular point. A *resolution* of $X$ is a proper birational morphism $f \colon Y \to X$ from a smooth surface that is an isomorphism over $X \setminus \{x\}$. Its exceptional set $f^{-1}(x)$ is connected, by Zariski's main theorem, and it is a union of proper curves $E_1, \dots, E_r$. The *intersection matrix* is $M = (E_i \cdot E_j)$, a symmetric integer matrix with $M_{ij} \ge 0$ for $i \ne j$.

**Theorem 4.3.1 (the intersection matrix is negative definite).** The matrix $M$ is negative definite: $\big(\sum_i y_i E_i\big)^2 < 0$ for every nonzero $y \in \mathbb{R}^r$.

Lean: not yet in Lean.

**Lemma 4.3.2 (the negativity lemma for surfaces).** Let $B = \sum_i b_i E_i$ be an $\mathbb{R}$-divisor supported on the exceptional curves, with $B \cdot E_j \le 0$ for every $j$. Then $B \ge 0$.

Lean: not yet in Lean.

This is the case of surfaces of the negativity lemma of KM98, Chapter 3. It says: an exceptional divisor $B$ such that $-B$ is $f$-nef is effective.

The theorem gives an inverse of $M$, and that gives a pullback for every divisor.

**Definition 4.3.3 (numerical pullback).** Let $D$ be an $\mathbb{R}$-divisor on $X$, and $f^{-1}_* D$ its strict transform on $Y$. The *numerical pullback* is
$$f^* D = f^{-1}_* D + \sum_i c_i E_i,$$
where $c \in \mathbb{R}^r$ is the unique solution of the linear system $\big(f^{-1}_*D + \sum_i c_i E_i\big) \cdot E_j = 0$ for $j = 1, \dots, r$. If $D$ is $\mathbb{R}$-Cartier, this is the usual pullback, since then $f^*D \cdot E_j = 0$ by the projection formula. For $D = K_X$, write
$$K_Y \equiv f^* K_X + \sum_i a_i E_i,$$
and call $a_i$ the *numerical discrepancy* of $E_i$. When $K_X$ is $\mathbb{Q}$-Cartier, $a_i = a(E_i, X, 0)$.

This is Mumford's construction (Mum61). It gives intersection numbers $D \cdot D' = f^*D \cdot f^*D'$ on $X$, rational when $D$ and $D'$ are $\mathbb{Q}$-divisors, and it lets one speak of the discrepancies of a surface whose canonical divisor is not $\mathbb{Q}$-Cartier.

**Definition 4.3.4 (minimal resolution).** A resolution $f \colon Y \to X$ is *minimal* if no exceptional curve is a $(-1)$-curve, that is a smooth rational curve $E$ with $E^2 = -1$.

A $(-1)$-curve can be contracted to a smooth point by Castelnuovo's theorem, so every resolution maps to a minimal one. Every normal surface has a minimal resolution, unique up to isomorphism, and every resolution factors through it (KM98, Chapter 4). This section uses these facts as a black box.

**Proposition 4.3.5 (the minimal resolution).** Let $f \colon Y \to X$ be the minimal resolution.

1. $K_Y \cdot E_i \ge 0$ for every exceptional curve: $K_Y$ is $f$-nef.
2. Every numerical discrepancy satisfies $a_i \le 0$.
3. If $x$ is a singular point, then $X$ is not terminal at $x$. So a terminal surface is smooth, and a smooth surface is terminal.

Lean: not yet in Lean.

### Proof in words

For the theorem, take a function $h$ that vanishes at $x$. Its pullback has divisor $\sum_i n_i E_i + H'$ with all $n_i > 0$, and the divisor of a function has degree 0 on each proper curve. So the positive vector $n$ has $Mn \le 0$, with a strict inequality where $H'$ meets the exceptional set. A standard identity writes the quadratic form of $M$, in the variables $y_i = x_i / n_i$, as a sum of terms that are all at most 0. The connectedness of $f^{-1}(x)$ forces equality only at $y = 0$.

For the negativity lemma, split $B = B^+ - B^-$. The square $(B^-)^2$ is at least 0 by the hypothesis, and less than 0 by the theorem unless $B^- = 0$.

For the proposition, adjunction says $K_Y \cdot E + E^2 = 2p_a(E) - 2 \ge -2$, and $E^2 < 0$. So $K_Y \cdot E < 0$ forces $K_Y \cdot E = E^2 = -1$ and $p_a(E) = 0$, a $(-1)$-curve. On the minimal resolution none exist. Then $-\sum_i a_i E_i$ satisfies the hypothesis of the negativity lemma, so it is effective. A singular point has at least one exceptional curve, with $a \le 0$.

### Examples

**Example 4.3.6 (the cone over a curve, for every line bundle).** Let $V$ be a smooth projective curve of genus $g$, $L$ a line bundle of degree $d > 0$, and $X = C(V, L)$ the cone of Section 2.3. The resolution $Y = \operatorname{Tot}(L^{-1})$ has one exceptional curve $E \cong V$ with $E^2 = -d$. Adjunction gives $K_Y \cdot E = 2g - 2 - E^2 = 2g - 2 + d$. The numerical discrepancy solves $(K_Y - aE) \cdot E = 0$, so
$$a = \frac{K_Y \cdot E}{E^2} = -\frac{2g - 2 + d}{d} = -1 - \frac{2g - 2}{d}.$$
This holds for every $L$, also when $K_X$ is not $\mathbb{Q}$-Cartier (Counterexample 4.2.27). When $K_X$ is $\mathbb{Q}$-Cartier it agrees with Corollary 4.2.20. The resolution is minimal unless $g = 0$ and $d = 1$, and then $X = \mathbb{A}^2$.

**Example 4.3.7 (the quotients $\frac1n(1,1)$).** For $g = 0$ and $d = n$, the example gives $E^2 = -n$, $K_Y \cdot E = n - 2$ and $a = -\frac{n-2}{n}$, as in Example 4.2.24 and in Volume 3, Example 3.3.38. For $n = 2$, $E$ is a $(-2)$-curve and $a = 0$.

**Example 4.3.8 (a chain of $(-2)$-curves).** Let the exceptional set be a chain $E_1, \dots, E_r$ of smooth rational curves with $E_i^2 = -2$, $E_i \cdot E_{i+1} = 1$ and no other intersections. This is the minimal resolution of the $A_r$ singularity $\{xy = z^{r+1}\}$ (Problem 2 for $r = 3$). Adjunction gives $K_Y \cdot E_i = 0$ for all $i$, so the system $\big(\sum_i a_i E_i\big) \cdot E_j = 0$ and the theorem give $a_i = 0$ for all $i$. Exercise 2 of Section 1.1 gives $K_X = 0$, so $K_Y = f^*K_X$.

**Example 4.3.9 (a resolution that is not minimal).** Let $X = \mathbb{A}^2$, which is smooth, and $f$ the blow-up of the origin. Then $E$ is a $(-1)$-curve, $K_Y \cdot E = -1$, and $a = 1 > 0$. So part 2 of the proposition fails on a resolution that is not minimal. Blowing up a point of $E$ on top of this gives a second curve with $a = 2$.

**Example 4.3.10 (the cyclic quotient $\frac15(1,2)$).** Its minimal resolution is a chain $E_1$, $E_2$ of smooth rational curves with $E_1^2 = -3$, $E_2^2 = -2$ and $E_1 \cdot E_2 = 1$ (Volume 3, Example 3.1.32). Adjunction gives $K_Y \cdot E_1 = 1$ and $K_Y \cdot E_2 = 0$. The system for $A = a_1 E_1 + a_2 E_2$ is
$$-3a_1 + a_2 = 1, \qquad a_1 - 2a_2 = 0,$$
with solution $a_1 = -\frac25$, $a_2 = -\frac15$. This agrees with the toric computation in the problems of Volume 3, Chapter 3. Both are at most 0, as the proposition says.

### Proof

*The theorem.* Let $h$ be a regular function on a neighbourhood of $x$ with $h(x) = 0$, not identically 0. Then
$$\operatorname{div}(f^* h) = \sum_i n_i E_i + H',$$
where $H'$ is the strict transform of $\operatorname{div}(h)$, and $n_i = v_{E_i}(h) \ge 1$ because $h$ vanishes on $f(E_i) = x$. The divisor of a function has degree 0 on each proper curve, so $\operatorname{div}(f^*h) \cdot E_j = 0$, that is
$$(Mn)_j = -H' \cdot E_j \le 0.$$
The curve $\operatorname{div}(h)$ passes through $x$, and $f$ is proper, so $H'$ meets $f^{-1}(x)$. Hence $(Mn)_j < 0$ for at least one $j$.

For $y \in \mathbb{R}^r$ put $z_i = n_i y_i$. The identity
$$\sum_{i,j} M_{ij} z_i z_j = \sum_i (Mn)_i \, n_i y_i^2 - \frac12 \sum_{i \ne j} M_{ij} n_i n_j (y_i - y_j)^2$$
holds: expand $(y_i - y_j)^2 = y_i^2 + y_j^2 - 2y_i y_j$ and use $M_{ij} = M_{ji}$. The second sum is $\sum_{i \ne j} M_{ij} n_i n_j y_i^2 - \sum_{i \ne j} M_{ij} n_i n_j y_i y_j$, and the first sum is $\sum_i \sum_j M_{ij} n_j n_i y_i^2$. Their difference is $\sum_i M_{ii} n_i^2 y_i^2 + \sum_{i \ne j} M_{ij} n_i n_j y_i y_j$, the left side. Every term on the right is at most 0, since $(Mn)_i \le 0$, $n_i > 0$ and $M_{ij} \ge 0$ for $i \ne j$. So $M$ is negative semidefinite. If the form is 0 at $z$, every term is 0. Then $y_i = y_j$ whenever $E_i \cdot E_j > 0$, and $f^{-1}(x)$ is connected, so all $y_i$ are equal to one number $y_0$. And $(Mn)_j n_j y_0^2 = 0$ for the $j$ with $(Mn)_j < 0$, so $y_0 = 0$. Hence $z = 0$, and $M$ is negative definite.

*The negativity lemma.* Write $B = B^+ - B^-$, with $B^+, B^- \ge 0$ and no common component. Suppose $B^- \ne 0$. Then
$$(B^-)^2 = B^- \cdot B^+ - B^- \cdot B.$$
The first term is at least 0, since $B^+$ and $B^-$ have no common component. The second is $-\sum_j b_j^- (E_j \cdot B) \ge 0$, by the hypothesis, where $b_j^- \ge 0$ are the coefficients of $B^-$. So $(B^-)^2 \ge 0$, and the theorem gives $B^- = 0$, a contradiction.

*The numerical pullback.* The system is $Mc = -\big(f^{-1}_*D \cdot E_j\big)_j$, and $M$ is invertible by the theorem. If $D$ is $\mathbb{R}$-Cartier, the usual pullback has the form $f^{-1}_*D + \sum_i c_i E_i$ and satisfies the system by the projection formula, so it is the solution.

*The proposition.* Part 1. Let $E$ be an exceptional curve. By adjunction, $K_Y \cdot E + E^2 = 2p_a(E) - 2 \ge -2$, and $E^2 < 0$ by the theorem. If $K_Y \cdot E < 0$, then both $K_Y \cdot E$ and $E^2$ are negative integers with sum at least $-2$, so both are $-1$, and $p_a(E) = 0$. An integral curve of arithmetic genus 0 is smooth and rational, so $E$ is a $(-1)$-curve. The resolution is minimal, so this does not happen.

Part 2. Put $A = \sum_i a_i E_i \equiv K_Y - f^*K_X$. Then $A \cdot E_j = K_Y \cdot E_j \ge 0$ by part 1, since $f^*K_X \cdot E_j = 0$. So $B = -A$ has $B \cdot E_j \le 0$, and the negativity lemma gives $-A \ge 0$.

Part 3. If $x$ is singular, the minimal resolution is not an isomorphism, so it has an exceptional curve $E_1$. If $K_X$ is $\mathbb{Q}$-Cartier, $a(E_1, X, 0) = a_1 \le 0$ by part 2, so $\operatorname{discrep}(X, 0) \le 0$ and $X$ is not terminal. If $K_X$ is not $\mathbb{Q}$-Cartier, $X$ is not terminal by definition. A smooth surface has $\operatorname{discrep} = 1$ by Theorem 4.2.12. $\square$

### Exercises

1. (A) Let the exceptional set be one smooth curve $E$ of genus $g$ with $E^2 = -n$. Compute the numerical discrepancy of $E$. For which $(g, n)$ is it greater than $-1$, and for which is it 0?
2. (A) Show directly that the intersection matrix of the chain in the example of $\frac15(1,2)$ is negative definite, and that its determinant is 5.
3. (B) Strengthen the negativity lemma: if $B \cdot E_j \le 0$ for every $j$ and $B \ne 0$, then every coefficient $b_i$ is positive. Use the connectedness of $f^{-1}(x)$.
4. (B) Let $f \colon Y \to X$ be the minimal resolution with numerical discrepancies $a_i$, and $g \colon Y' \to Y$ the blow-up of a point $p$ of the exceptional set, with new curve $F$. Show that $a(F) = 1 + a_1$ if $p$ lies on $E_1$ only, and $a(F) = 1 + a_1 + a_2$ if $p \in E_1 \cap E_2$ is a transversal intersection point.
5. (B) Let $E_1, \dots, E_k$ with $k \ge 3$ be a cycle of smooth rational curves, $E_i \cdot E_{i+1} = 1$ with indices mod $k$, $E_i^2 = -b_i$ with every $b_i \ge 2$ and some $b_i \ge 3$. Show that the matrix is negative definite by the method of the theorem with $n = (1, \dots, 1)$, and that every numerical discrepancy is $-1$.
6. (C) Show that the numerical pullback does not depend on the resolution: if $g \colon Y' \to Y$ is the blow-up of a point on the exceptional set, the numerical pullback of $D$ to $Y'$ is $g^*$ of the numerical pullback to $Y$. Deduce that the numerical discrepancy of a divisor over $X$ does not depend on the resolution on which it appears.

### Lean

The results of this section are not yet in Lean. The library has no intersection numbers of curves on surfaces in the form needed here, and no minimal resolution.

### Notes and history

The negative definiteness of the exceptional curves goes back to Du Val and to Mumford (Mum61), who proved it, defined the numerical pullback, and used it to compute the local fundamental group of a normal surface singularity. Grauert proved the converse: a configuration of curves on a smooth surface with negative definite matrix can be contracted to a normal point, in the analytic category. Artin (Art66) studied the rational singularities, for which the contraction exists in the algebraic category. The negativity lemma in all dimensions is in KM98, Chapter 3, and it is one of the main tools of the program. The proposition that terminal surfaces are smooth explains why the minimal model program for surfaces needs no singularities when $\Delta = 0$: Volume 2 runs it on smooth surfaces only.
