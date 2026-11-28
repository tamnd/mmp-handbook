---
title: Rational surface singularities
nodes: []
sources: [Art66, Lip69, KM98, Bri68]
reads_with: [Art66:all, Lip69:all, KM98:4.1]
requires: [P4.6, P5.5, P5.8, P8.9, P8.10]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Rational surface singularities

### Statement

In this section $k$ is algebraically closed of any characteristic, $X$ is a normal quasi-projective surface, $x \in X$ a singular point and $f \colon Y \to X$ a resolution near $x$ with exceptional curves $E_1, \dots, E_r$, as in Section 10.1. A *positive cycle* is a nonzero divisor $Z = \sum z_i E_i$ with all $z_i \geq 0$, its arithmetic genus is $p_a(Z) = 1 + \frac{1}{2}(Z^2 + K_Y \cdot Z)$, and $Z_f$ is the fundamental cycle of Proposition P5.8.13. The point $x$ is *rational* if $(R^1 f_* \mathcal{O}_Y)_x = 0$; by Exercise 5 of Section P5.8.2 this does not depend on $f$, and in characteristic $0$ it agrees with Definition P4.9.18.

**Theorem P8.11.10 (Artin's criterion).** The following are equivalent.

1. $x$ is a rational singularity.
2. $p_a(Z) \leq 0$ for every positive cycle $Z$ supported on $f^{-1}(x)$.
3. $p_a(Z_f) = 0$.

Lean: not in Lean as stated.

**Theorem P8.11.11 (the exceptional set of a rational singularity).** Let $x$ be a rational singularity and $f$ any resolution near $x$. Then

1. every $E_i$ is isomorphic to $\mathbb{P}^1$;
2. $E_i \cdot E_j \in \{ 0, 1 \}$ for $i \neq j$, so two exceptional curves meet transversally in at most one point;
3. the dual graph is a tree; in particular no three exceptional curves pass through one point.

Lean: not in Lean as stated.

**Proposition P8.11.12 (multiplicity and embedding dimension).** Let $x$ be a rational singularity. Then $Z_f^2 = -2 - K_Y \cdot Z_f$, the multiplicity of $\mathcal{O}_{X, x}$ is $-Z_f^2$, and its embedding dimension is $1 - Z_f^2$. On the minimal resolution $K_Y \cdot Z_f \geq 0$, so the multiplicity is at least $2$, with equality exactly for the Du Val singularities.

Lean: not in Lean as stated.

**Theorem P8.11.13 (cyclic quotient surface singularities are rational).** Let $x$ be the singularity $\frac{1}{r}(1, q)$, with $0 < q < r$, $\gcd(r, q) = 1$ and $\frac{r}{q} = [b_1, \dots, b_s]$, and let $E_1, \dots, E_s$ be the chain of Theorem P8.9.23. Then $Z_f = E_1 + \dots + E_s$, $p_a(Z_f) = 0$, and $x$ is a rational singularity of multiplicity and embedding dimension
$$\operatorname{mult}_x X = 2 + \sum_{i = 1}^{s} (b_i - 2), \qquad \operatorname{edim}_x X = 3 + \sum_{i = 1}^{s} (b_i - 2).$$

Lean: not in Lean as stated.

### Proof in words

Artin's theory, developed in Chapter 8 of Volume P5, turns rationality into arithmetic on exceptional cycles: the singularity is rational exactly when no positive cycle has positive arithmetic genus, and it suffices to test the fundamental cycle. Applied to a single curve, to two curves and to a cycle of curves, the inequality $p_a \leq 0$ forces smooth rational components, transversal intersections in at most one point and a tree. Since $p_a(Z_f) = 0$, the multiplicity $-Z_f^2$ is $2 + K_Y \cdot Z_f$. For a chain of rational curves with self-intersections $-b_i \leq -2$ the reduced cycle is already antinef, and the genus formula gives $0$.

### Examples

**Example P8.11.14 (cyclic quotients, checked against Chapter 9).** For $\frac{1}{n}(1, 1)$ the chain is one curve with $b_1 = n$, so the multiplicity is $n$ and the embedding dimension $n + 1$, matching the $n + 1$ generators of Example P8.9.25 and Example P5.8.19. For $\frac{1}{5}(1, 2)$, $\frac{5}{2} = [3, 2]$, so the multiplicity is $2 + 1 + 0 = 3$ and the embedding dimension $4$, matching the four generators $x^5, x^3 y, x y^2, y^5$ of Example P8.9.26. For $A_{r-1}$ all $b_i = 2$, and the multiplicity is $2$, as for every Du Val singularity.

**Example P8.11.15 (a tree of rational curves that is not rational).** Let $E_0, E_1, \dots, E_4$ be smooth rational curves with $E_0^2 = -2$, $E_i^2 = -3$ for $i \geq 1$, $E_0 \cdot E_i = 1$ and $E_i \cdot E_j = 0$ for $1 \leq i < j$. The intersection matrix is negative definite: for $z = \sum z_i E_i$,
$$-z^2 = 2 z_0^2 + 3 \sum_{i \geq 1} z_i^2 - 2 z_0 \sum_{i \geq 1} z_i = \sum_{i \geq 1} 3 \left( z_i - \tfrac{z_0}{3} \right)^2 + \left( 2 - \tfrac{4}{3} \right) z_0^2 > 0$$
for $z \neq 0$. By adjunction $K_Y \cdot E_0 = 0$ and $K_Y \cdot E_i = 1$. Laufer's algorithm starts with $Z_0 = \sum_{i = 0}^{4} E_i$, which has $Z_0 \cdot E_0 = -2 + 4 = 2 > 0$, so $Z_1 = 2 E_0 + E_1 + \dots + E_4$, with $Z_1 \cdot E_0 = -4 + 4 = 0$ and $Z_1 \cdot E_i = 2 - 3 = -1$. So $Z_f = Z_1$, $Z_f^2 = \sum z_i (Z_f \cdot E_i) = -4$, $K_Y \cdot Z_f = 4$ and
$$p_a(Z_f) = 1 + \tfrac{1}{2}(-4 + 4) = 1.$$
By Theorem P8.11.10, a singularity with this resolution graph is not rational, although its exceptional curves satisfy all three conclusions of Theorem P8.11.11. The conditions of Theorem P8.11.11 are necessary, not sufficient.

**Example P8.11.16 (the fundamental cycle of a rational triple point).** Let $E_0$ be a $(-3)$-curve and $E_1$, $E_2$ two $(-2)$-curves, each meeting $E_0$ once and disjoint from each other. Then $Z_0 = E_0 + E_1 + E_2$ has $Z_0 \cdot E_0 = -3 + 2 = -1$ and $Z_0 \cdot E_i = 1 - 2 = -1$, so $Z_f = Z_0$, $Z_f^2 = -3$, $K_Y \cdot Z_f = 1 + 0 + 0 = 1$ and $p_a(Z_f) = 1 + \frac{1}{2}(-3 + 1) = 0$. By Theorem P8.11.10 such a configuration contracts to a rational singularity, and by Proposition P8.11.12 it has multiplicity $3$ and embedding dimension $4$. The graph is the chain $E_1, E_0, E_2$ with $[2, 3, 2] = 2 - \frac{1}{3 - \frac{1}{2}} = \frac{8}{5}$, so by Theorem P8.9.23 the cyclic quotient $\frac{1}{8}(1, 5)$ has this resolution, and Theorem P8.11.13 gives the multiplicity $2 + 0 + 1 + 0 = 3$ again.

**Example P8.11.17 (the cone over a plane cubic).** For the cone over a smooth plane cubic, $Z_f = E$ is a curve of genus $1$ and $p_a(Z_f) = 1$, so Theorem P8.11.10 confirms that the vertex is not rational (Example P5.8.21). Here $E$ is not rational, so part 1 of Theorem P8.11.11 fails as well.

### Proof

*Theorem P8.11.10.* Apply Theorem P5.8.16 to $f$ and the point $x$ to which $f$ contracts the curves $E_i$. Part 1 there is the equivalence of 2 and 3, part 2 shows that 2 implies 1, and part 3 shows that 1 implies 2. Proposition P5.8.15 gives a direct proof that 1 implies 2.

*Theorem P8.11.11.* By Theorem P8.11.10, $p_a(Z) \leq 0$ for every positive cycle. (1) For $Z = E_i$, $p_a(E_i) = h^1(\mathcal{O}_{E_i}) \geq 0$, so $p_a(E_i) = 0$, and $E_i \cong \mathbb{P}^1$ by Corollary P5.5.15. (2) For positive cycles $A$, $B$ the genus formula gives
$$p_a(A + B) = p_a(A) + p_a(B) + A \cdot B - 1.$$
For $A = E_i$, $B = E_j$, $i \neq j$, this is $E_i \cdot E_j - 1 \leq 0$, so $E_i \cdot E_j \leq 1$, and an intersection number $1$ of two curves on a smooth surface means one transversal intersection point (Proposition P5.5.5). (3) The fibre $f^{-1}(x)$ is connected by Theorem P4.6.8 (or part 2 of Theorem P5.8.3), so the dual graph is connected. Suppose it contains a cycle, and choose one of minimal length $m$; by (2) the graph has simple edges, so $m \geq 3$, and by minimality the cycle $E_1, \dots, E_m$ has no chords, so $E_i \cdot E_j = 1$ for exactly $m$ pairs $i < j$ among these curves. Applying the formula of (2) $m - 1$ times,
$$p_a(E_1 + \dots + E_m) = \sum_{i = 1}^{m} p_a(E_i) + \sum_{i < j} E_i \cdot E_j - (m - 1) = 0 + m - (m - 1) = 1,$$
which contradicts $p_a \leq 0$. So the graph is a tree. Three curves through a common point would meet pairwise, forming a cycle of length $3$, which is excluded.

*Proposition P8.11.12.* By Theorem P8.11.10, $p_a(Z_f) = 0$, which is $Z_f^2 + K_Y \cdot Z_f = -2$. Part 4 of Theorem P5.8.16 gives the multiplicity $-Z_f^2$ and, when $-Z_f^2 \geq 2$, the embedding dimension $1 - Z_f^2$. On the minimal resolution, $K_Y \cdot E_i \geq 0$ for every $i$ by Lemma P8.10.11, so $K_Y \cdot Z_f \geq 0$ and $-Z_f^2 = 2 + K_Y \cdot Z_f \geq 2$. Equality means multiplicity $2$, which is a rational double point, hence Du Val by Theorem P8.10.12.

*Theorem P8.11.13.* By Theorem P8.9.23 the curves $E_i$ are smooth rational curves forming a chain, with $E_i^2 = -b_i \leq -2$. Let $Z = E_1 + \dots + E_s$. Then $Z \cdot E_i = -b_i + \#\{ j : |j - i| = 1 \} \leq -2 + 2 = 0$ for every $i$. Every positive cycle $Z'$ with $Z' \cdot E_i \leq 0$ for all $i$ has all coefficients at least $1$, by part 1 of Proposition P5.8.13, so $Z' \geq Z$ and $Z_f = Z$. By the formula in the proof of Theorem P8.11.11, applied along the chain, $p_a(Z) = 0 + (s - 1) - (s - 1) = 0$. So $x$ is rational by Theorem P8.11.10. Finally
$$-Z_f^2 = \sum_i b_i - 2(s - 1) = 2 + \sum_i (b_i - 2) \geq 2,$$
and Proposition P8.11.12 gives the multiplicity and the embedding dimension.

### Exercises

1. (A) Compute the multiplicity and embedding dimension of $\frac{1}{7}(1, 3)$ and $\frac{1}{7}(1, 2)$, and compare with the Hilbert bases of Exercise 1 of Section 9.3.
2. (A) Show that a $(-n)$-curve $E \cong \mathbb{P}^1$, $n \geq 2$, together with two $(-2)$-curves attached to it, is the resolution graph of a rational singularity of multiplicity $n$.
3. (B) Show that a rational singularity whose minimal resolution has a single exceptional curve $E$ is $\frac{1}{n}(1, 1)$ for $n = -E^2$, given that the analytic type is determined by the resolution graph for cyclic quotients (Brieskorn, Bri68).
4. (B) Let $x$ be a rational singularity. Show that every positive cycle $Z$ with $Z \cdot E_i \leq 0$ for all $i$ has $H^1(\mathcal{O}_Z) = 0$, and that $\mathcal{O}_Y(-Z)$ is generated by global sections near $f^{-1}(x)$ for $Z = Z_f$, using Theorem P5.8.16.
5. (B) Show that the star-shaped graph with a central $(-2)$-curve and three $(-3)$-curves attached is the graph of a rational singularity, and compute its multiplicity. Compare with Example P8.11.15.
6. (C) Show that rational surface singularities are $\mathbb{Q}$-factorial: for every exceptional cycle the intersection matrix can be inverted over $\mathbb{Q}$, and Lipman (Lip69) proves that the local class group is finite. Verify the finiteness for $\frac{1}{r}(1, q)$ by Theorem P8.9.23.

### Lean

Rational surface singularities, cycles and fundamental cycles are not in the repository.

### Notes and history

Artin (Art66) introduced rational surface singularities, proved the criterion of Theorem P8.11.10 and the formulas for the multiplicity and embedding dimension, and showed that the rational double points are the Du Val singularities. Brieskorn (Bri68) studied the quotients of $\mathbb{C}^2$ and proved that the rational singularities are taut in many cases, and Lipman (Lip69) extended the theory to two-dimensional schemes and proved that rational surface singularities have finite local class groups. Kollár and Mori, Section 4.1 (KM98), use these facts to classify the log terminal surface singularities as quotient singularities, which Volume 4 proves as Theorem 4.3.18.
