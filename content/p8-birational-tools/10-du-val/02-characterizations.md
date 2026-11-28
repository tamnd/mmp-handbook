---
title: Characterizations of Du Val singularities
nodes: []
sources: [Art66, Dur79, KM98, Rei87, DuV34]
reads_with: [Dur79:all, Art66:all, KM98:4.2]
requires: [P1.10, P1.11, P4.9, P5.5, P5.8, P8.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Characterizations of Du Val singularities

### Statement

Keep the conventions of Section 10.1: $X$ is a normal quasi-projective surface, $x \in X$ a singular point and $f \colon Y \to X$ the minimal resolution near $x$, with exceptional curves $E_1, \dots, E_r$. A normal surface is Cohen-Macaulay (Corollary P1.11.13), so $X$ is Gorenstein at $x$ if and only if $\omega_X$ is invertible near $x$, that is, if and only if $K_X$ is Cartier near $x$. When $K_X$ is Cartier near $x$, $f^* K_X$ is the divisor of the pullback of a local equation, and $K_Y = f^* K_X + \sum_i a_i E_i$ with integers $a_i$, after choosing $K_Y$ and $K_X$ as divisors of the same rational $2$-form as in Section P3.12. The singularity $x$ is *rational* if $(R^1 f_* \mathcal{O}_Y)_x = 0$, which agrees with Definition P5.8.14 and Definition P4.9.18 for surfaces, because $f_* \mathcal{O}_Y = \mathcal{O}_X$ by Theorem P4.6.8 and the fibres of $f$ have dimension at most one.

**Definition P8.10.10 (multiplicity and rational double points).** The *multiplicity* of a local ring $(\mathcal{O}, \mathfrak{m})$ of dimension $2$ with residue field $k$ is the integer $e$ such that $\dim_k \mathcal{O} / \mathfrak{m}^{n+1} = \frac{e}{2} n^2 + O(n)$. A point $x$ is a *rational double point* if it is a rational singularity and $\mathcal{O}_{X, x}$ has multiplicity $2$. For $\widehat{\mathcal{O}}_{X, x} \cong k[[x, y, z]]/(F)$ with $F$ of order $m$, that is, with lowest homogeneous part $F_m$ of degree $m$, the associated graded ring is $k[x, y, z]/(F_m)$, whose part of degree $n$ has dimension $\binom{n + 2}{2} - \binom{n - m + 2}{2} = m n + O(1)$, so the multiplicity is $m$.

**Lemma P8.10.11 (the minimal resolution is $K$-nef).** On the minimal resolution, $K_Y \cdot E_i \geq 0$ for every exceptional curve $E_i$.

Lean: not in Lean as stated.

**Theorem P8.10.12 (characterizations of Du Val singularities).** The following conditions on the singular point $x$ are equivalent.

1. $x$ is a Du Val singularity: every $E_i$ is a $(-2)$-curve.
2. $K_X$ is Cartier near $x$ and $f$ is crepant: $K_Y = f^* K_X$ near $f^{-1}(x)$.
3. $x$ is a rational double point.
4. $x$ is a rational singularity and $X$ is Gorenstein at $x$.

Lean: not in Lean as stated.

**Corollary P8.10.13 (Du Val singularities are double points of hypersurfaces).** Let $x$ be a Du Val singularity. Then $\widehat{\mathcal{O}}_{X, x} \cong k[[x, y, z]]/(F)$ with $F$ of order $2$, the embedding dimension is $3$, the fundamental cycle has $Z_f^2 = -2$, and $\mathfrak{m}_x \mathcal{O}_Y = \mathcal{O}_Y(-Z_f)$ near $f^{-1}(x)$. If $\operatorname{char} k \neq 2$, then $F$ can be taken of the form $x^2 + g(y, z)$.

Lean: not in Lean as stated.

The equivalence of the four conditions with the condition that $x$ is a canonical singularity is Theorem P8.13.13, once discrepancies are defined in Chapter 13; Volume 4 proves it again in Theorem 4.3.11. That every quotient $\mathbb{A}^2 / G$ with $G \subseteq SL_2(k)$ finite is Du Val is Corollary P8.11.6.

### Proof in words

A $(-2)$-curve has $K_Y \cdot E = 0$, so a resolution by $(-2)$-curves has $K_Y$ numerically trivial on the exceptional set, and negative definiteness forces $K_Y = f^* K_X$. Artin's theory of Volume P5 shows that such configurations contract to rational singularities whose fundamental cycle has square $-2$, which is the multiplicity, and a point of multiplicity $2$ and embedding dimension $3$ is a hypersurface, hence Gorenstein. Conversely, for a rational Gorenstein point the difference $f^* K_X - K_Y$ is an effective exceptional cycle, by the negativity lemma; if it were nonzero, its arithmetic genus would be $1$, which rationality forbids. So the minimal resolution is crepant, and adjunction makes every exceptional curve a $(-2)$-curve.

### Examples

**Example P8.10.14 (the fundamental cycle of $E_8$).** Label the $E_8$ graph by a centre $c$, a short arm $a$, a middle arm $b_1, b_2$ and a long arm $d_1, d_2, d_3, d_4$, each listed from the centre outwards. Laufer's algorithm (Proposition P5.8.13) starting from $\sum E_v$ ends at
$$Z_f = 6 E_c + 3 E_a + 4 E_{b_1} + 2 E_{b_2} + 5 E_{d_1} + 4 E_{d_2} + 3 E_{d_3} + 2 E_{d_4}.$$
Indeed $Z_f \cdot E_v = -2 z_v + \sum_{w \sim v} z_w$ is $-12 + 3 + 4 + 5 = 0$ at $c$, $-6 + 6 = 0$ at $a$, $-8 + 6 + 2 = 0$ at $b_1$, $-4 + 4 = 0$ at $b_2$, $-10 + 6 + 4 = 0$ at $d_1$, $-8 + 5 + 3 = 0$ at $d_2$, $-6 + 4 + 2 = 0$ at $d_3$ and $-4 + 3 = -1$ at $d_4$. So $Z_f^2 = \sum_v z_v (Z_f \cdot E_v) = 2 \cdot (-1) = -2$, as Corollary P8.10.13 requires, and the multiplicity of $x^2 + y^3 + z^5$ at the origin is indeed $2$. Since $\mathfrak{m}_x \mathcal{O}_Y = \mathcal{O}_Y(-Z_f)$, the general function of $\mathfrak{m}_x$ has a pullback whose strict transform meets only $E_{d_4}$, once.

**Example P8.10.15 (a rational point that is not a double point).** For $\frac{1}{3}(1, 1)$ the minimal resolution has one curve $E \cong \mathbb{P}^1$ with $E^2 = -3$, so $Z_f = E$, and by Example P5.8.19 the point is rational of multiplicity $3$ and embedding dimension $4$. By Theorem P8.9.23 the index of $K_X$ is $3$, so $X$ is not Gorenstein. Here $K_Y \cdot E = 1$ by adjunction, and writing $K_Y \equiv f^* K_X + a E$ numerically, in the sense of Mumford's pullback (Corollary P5.8.5), gives $-3a = 1$, $a = -\frac{1}{3}$. Conditions 1 to 4 all fail, consistently with Theorem P8.10.12.

**Example P8.10.16 (a Gorenstein point that is not rational).** Let $X = \{ x^3 + y^3 + z^3 = 0 \} \subseteq \mathbb{A}^3$, with $\operatorname{char} k \neq 3$, the affine cone over a smooth plane cubic $E_0$. It is a hypersurface, hence Gorenstein by Corollary P1.10.27, of multiplicity $3$. The blow-up of the vertex is the minimal resolution, with one exceptional curve $E \cong E_0$ of genus $1$ and $E^2 = -3$ (Example P5.8.21), and the vertex is not rational. Adjunction gives $K_Y \cdot E = 0 - E^2 = 3$, and $K_Y = f^* K_X + a E$ gives $-3a = 3$, so $a = -1$. The minimal resolution is not crepant, as Theorem P8.10.12 predicts.

**Example P8.10.17 (the $D_4$ singularity again).** For $x^2 + y^2 z + z^3$, Theorem P8.10.4 gives the $D_4$ graph with central curve $C'$ and three curves $F_\rho$, and Example P5.8.18 gives $Z_f = 2 C' + F_0 + F_i + F_{-i}$ with $Z_f^2 = -2$. The equation has order $2$, so the multiplicity is $2$, as part 3 of Theorem P8.10.12 requires. The coefficient $2$ on $C'$ matches the first blow-up. At the generic point of $C$, where $h(z_1) \neq 0$, the function $x_1$ is a local parameter of $X_1$ along $C$ and $y = -x_1^2 / h(z_1)$, so $y$ and $z = z_1 y$ vanish to order $2$ along $C$, and $x = x_1 y$ to order $3$. The general element of $\mathfrak{m}_x$ therefore vanishes to order $2$ along $C'$.

### Proof

*Lemma P8.10.11.* If $K_Y \cdot E_i < 0$, then since $E_i^2 < 0$ by Theorem P5.8.3, part 2 of Corollary P5.5.15 gives $E_i \cong \mathbb{P}^1$ and $E_i^2 = -1$, so $E_i$ is a $(-1)$-curve, which the minimal resolution does not contain.

*Theorem P8.10.12, 1 implies 3.* For a $(-2)$-curve, $K_Y \cdot E_i = 0$ by Theorem P5.5.14. The exceptional curves form a connected negative definite configuration (Theorem P5.8.3) of $(-2)$-curves, so part 3 of Proposition P5.8.17 shows that $x$ is a rational singularity of multiplicity $2$, that is, a rational double point.

*3 implies 4.* Let $x$ be a rational double point. By part 4 of Theorem P5.8.16 the multiplicity is $-Z_f^2 = 2$ and the embedding dimension is $3$. So $\widehat{\mathcal{O}}_{X, x}$, a complete local ring with residue field $k$ and embedding dimension $3$, is a quotient $k[[x, y, z]]/I$ by Cohen's structure theorem. Since $\mathcal{O}_{X, x}$ is a normal excellent local domain, its completion is a normal domain, of dimension $2$, so $I$ is a prime of height $1$ in the factorial ring $k[[x, y, z]]$, hence principal. By Corollary P1.10.27, $\widehat{\mathcal{O}}_{X, x}$ is Gorenstein, and a local ring is Gorenstein if its completion is (Matsumura, Commutative Ring Theory, Theorem 18.3). So $X$ is Gorenstein at $x$.

*4 implies 2.* Since $X$ is Gorenstein at $x$, $K_X$ is Cartier near $x$, and $K_Y = f^* K_X + A$ with $A = \sum_i a_i E_i$ an integral exceptional cycle. Since $f^* K_X$ is principal near $f^{-1}(x)$, $f^* K_X \cdot E_i = 0$, so $A \cdot E_i = K_Y \cdot E_i \geq 0$ for every $i$, by Lemma P8.10.11. Theorem P5.8.2 applied to $-A$, whose intersection numbers with all $E_i$ are $\leq 0$, gives $-A \geq 0$. Suppose $B = -A$ is nonzero; it is a positive cycle. Then $K_Y \cdot B = (f^* K_X - B) \cdot B = -B^2$, so the genus formula of Theorem P5.5.14 gives
$$p_a(B) = 1 + \tfrac{1}{2} (B^2 + K_Y \cdot B) = 1 + \tfrac{1}{2} (B^2 - B^2) = 1 > 0.$$
This contradicts Proposition P5.8.15, which gives $p_a(B) \leq 0$ for every positive cycle at a rational singularity. So $A = 0$ and $K_Y = f^* K_X$. Alternatively, part 2 of Corollary P4.9.22 gives $a_i \geq 0$ directly, and $a_i \leq 0$ was shown above.

*2 implies 1.* If $K_Y = f^* K_X$ near $f^{-1}(x)$, then $K_Y \cdot E_i = f^* K_X \cdot E_i = 0$, and $E_i^2 < 0$ by Theorem P5.8.3. By the genus formula of Theorem P5.5.14, $2 p_a(E_i) - 2 = E_i^2 + K_Y \cdot E_i = E_i^2 < 0$, and $p_a(E_i) = h^1(\mathcal{O}_{E_i}) \geq 0$ for the integral curve $E_i$. Hence $p_a(E_i) = 0$, $E_i^2 = -2$, and $E_i \cong \mathbb{P}^1$ by the equality case of part 1 of Corollary P5.5.15.

*Corollary P8.10.13.* By Theorem P8.10.12 the point is a rational double point, and the proof of 3 implies 4 gives $\widehat{\mathcal{O}}_{X, x} \cong k[[x, y, z]]/(F)$ with $F$ of order $2$ by Definition P8.10.10, and embedding dimension $3$. Part 3 of Proposition P5.8.17 gives $Z_f^2 = -2$, and part 4 of Theorem P5.8.16 gives $\mathfrak{m}_x \mathcal{O}_Y = \mathcal{O}_Y(-Z_f)$. If $\operatorname{char} k \neq 2$, the quadratic part $F_2 \neq 0$ can be diagonalized by a linear change of coordinates, so that $x^2$ occurs in $F_2$ with coefficient $1$. Then $\partial^2 F / \partial x^2 (0) = 2 \neq 0$, and the Weierstrass preparation theorem writes $F = u \cdot (x^2 + a(y, z) x + b(y, z))$ with $u$ a unit. Replacing $x$ by $x - a/2$ gives $x^2 + g(y, z)$ with $g = b - a^2/4$.

### Exercises

1. (A) For the $E_6$ graph, find the fundamental cycle by Laufer's algorithm, and check that $Z_f^2 = -2$.
2. (A) For $D_n$, $n \geq 5$, show that $Z_f = E_1 + 2 E_2 + \dots + 2 E_{n-2} + E_{n-1} + E_n$, where $E_1, \dots, E_{n-2}$ is the long arm with $E_{n-2}$ the centre and $E_{n-1}$, $E_n$ the two short arms.
3. (B) Let $x$ be a rational singularity with $K_X$ Cartier near $x$. Show that its multiplicity is $2$, and deduce, without toric geometry, that $K_X$ is not Cartier for $\frac{1}{n}(1, 1)$ with $n \geq 3$.
4. (B) Show that $x^2 + y^4 + z^4 = 0$ is Gorenstein of multiplicity $2$ but not a rational double point, by showing that its minimal resolution, obtained by blowing up the origin, has an exceptional curve of genus $1$.
5. (B) Let $x$ be a Du Val singularity and $h \in \mathfrak{m}_x$ general. Show that the curve $\{ h = 0 \}$ has a singular point at $x$ whose strict transform on $Y$ meets the exceptional locus exactly where $Z_f \cdot E_i < 0$.
6. (C) Prove the equivalence of conditions 1 and 4 of Theorem P8.10.12 without using Artin's multiplicity formula, by combining Corollary P4.9.22 with Lemma P8.10.11.

### Lean

Rational double points and Du Val singularities are not in the repository. Condition 2 of Theorem P8.10.12 says that the minimal resolution has all discrepancies zero; the predicates `MinimalModel.IsCanonical` and `MinimalModel.LogDiscrepancyIs` in `MinimalModel/Statements/Basic.lean` state the corresponding global conditions on discrepancies, which Chapter 13 relates to Du Val singularities.

### Notes and history

The equivalence of the conditions of Theorem P8.10.12 goes back to Du Val (DuV34), who studied the singularities not affecting adjunction, and to Artin (Art66), who introduced rational singularities and showed that the rational double points are the rational singularities of multiplicity $2$. Durfee (Dur79) collects fifteen characterizations, among them conditions 1 to 4 here, and Kollár and Mori, Section 4.2 (KM98), prove the equivalence with canonical singularities. In every dimension, part 2 of Corollary P4.9.22 is the analogue of the implication from 4 to 2: a Gorenstein singularity is rational exactly when the discrepancies of a resolution are nonnegative.
