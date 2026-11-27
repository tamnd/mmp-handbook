---
title: Del Pezzo surfaces
nodes: []
sources: [Har77, Bea96, Rei97, KM98]
reads_with: [Har77:V.4, Bea96:ch4]
requires: [P3.10, P4.2, P5.1, P5.5, P5.6, P5.7, P5.12]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Del Pezzo surfaces

### Statement

For distinct points $p_1, \dots, p_r \in \mathbb{P}^2$ let $S_r = \operatorname{Bl}_{p_1, \dots, p_r} \mathbb{P}^2$, with $\operatorname{Pic}(S_r) = \mathbb{Z} \ell \oplus \bigoplus_i \mathbb{Z} E_i$, $\ell^2 = 1$, $E_i^2 = -1$ and $K = -3\ell + \sum_i E_i$, as in Example P5.6.8. Write $\Sigma_m$ for a sum of $m$ distinct classes $E_i$.

**Definition P5.9.24 (del Pezzo surfaces and general position).** A *del Pezzo surface* is a surface $S$ with $-K_S$ ample, and its *degree* is $d = K_S^2$. Distinct points $p_1, \dots, p_r \in \mathbb{P}^2$ with $r \leq 8$ are in *general position* if no three lie on a line, no six lie on a conic, and, for $r = 8$, there is no plane cubic through all eight that is singular at one of them.

**Proposition P5.9.25 (first properties).** Let $S$ be a del Pezzo surface of degree $d$.

1. $d \geq 1$, every integral curve $C$ on $S$ has $C^2 \geq -1$, and an integral curve with $C^2 < 0$ is a $(-1)$-curve.
2. If $E \subseteq S$ is a $(-1)$-curve and $\psi \colon S \to S'$ its contraction, then $S'$ is a del Pezzo surface of degree $d + 1$.
3. $\mathbb{P}^2$ is a del Pezzo surface of degree $9$, and $F_n$ is a del Pezzo surface if and only if $n \leq 1$, of degree $8$.

Lean: not in Lean as stated.

**Theorem P5.9.26 (the plane blown up in points in general position).** Let $p_1, \dots, p_r \in \mathbb{P}^2$, $r \leq 8$, be in general position.

1. $S_r$ is a del Pezzo surface of degree $9 - r$.
2. The $(-1)$-curves on a del Pezzo surface $S$ are exactly the integral curves whose class $D$ satisfies $D^2 = K \cdot D = -1$, and every class with these two properties is the class of exactly one curve, its unique effective representative. On $S_r$ these classes are, up to the numbering of the points,
$$E_i, \quad \ell - \Sigma_2, \quad 2\ell - \Sigma_5, \quad 3\ell - 2E_i - \Sigma_6, \quad 4\ell - 2\Sigma_3 - \Sigma_5, \quad 5\ell - 2\Sigma_6 - \Sigma_2, \quad 6\ell - 3E_i - 2\Sigma_7,$$
where the classes $E_j$ in each expression are distinct and the expression is allowed only when it involves at most $r$ of them. Their numbers for $r = 1, \dots, 8$ are $1, 3, 6, 10, 16, 27, 56, 240$.
3. $h^0(-K) = 10 - r$ and $h^1(-K) = 0$, and $|-K|$ is the linear system of strict transforms of the plane cubics through $p_1, \dots, p_r$.

Lean: not in Lean as stated.

**Theorem P5.9.27 (classification of del Pezzo surfaces).** A del Pezzo surface of degree $d$ is isomorphic to $\mathbb{P}^2$, with $d = 9$, to $\mathbb{P}^1 \times \mathbb{P}^1$, with $d = 8$, or to $S_r$ for $r = 9 - d \leq 8$ points in general position. In particular every del Pezzo surface is rational, and $1 \leq d \leq 9$.

Lean: not in Lean as stated.

**Theorem P5.9.28 (anticanonical models of degree at least three).** Let $S$ be a del Pezzo surface of degree $d \geq 3$. Then $-K$ is very ample, $h^0(-K) = d + 1$, and $|-K|$ embeds $S$ in $\mathbb{P}^d$ as a surface of degree $d$ contained in no hyperplane. For $d = 3$ the image is a smooth cubic surface in $\mathbb{P}^3$, and for $d = 4$ it is the scheme-theoretic intersection of two quadrics in $\mathbb{P}^4$.

Lean: not in Lean as stated.

### Proof in words

On a del Pezzo surface the genus formula and $-K \cdot C > 0$ leave a single kind of negative curve, the $(-1)$-curve, and contracting one keeps $-K$ positive on curves, as the contracted curve meets the others nonnegatively. For the plane blown up in points in general position, the anticanonical class is the class of cubics through the points, and $3a > \sum b_i$ for the strict transform of a curve of degree $a$ with multiplicities $b_i$: for $a \leq 3$ by the general position conditions, and for $a \geq 4$ by Bézout against a cubic through the points and one more point of the curve. Riemann-Roch makes every class with $D^2 = K \cdot D = -1$ effective, and $-K \cdot D = 1$ makes its member integral; listing these classes is the arithmetic of two equations $\sum b_i = 3a - 1$ and $\sum b_i^2 = a^2 + 1$.

Conversely, contracting $(-1)$-curves on a del Pezzo surface until none is left gives, by the cone theorem, $\mathbb{P}^2$ or a ruled surface with $K^2 > 0$, so $F_0$, and one more step replaces $F_0$ by the plane blown up in two points. Any failure of general position, or an infinitely near point, would produce a curve of square at most $-2$. For $d \geq 3$ the cubics through the points embed the surface, a classical theorem; for $d = 4$ a dimension count on a hyperplane section gives two quadrics through the surface, and Bézout shows that they cut it out.

### Examples

**Example P5.9.29 (the table of del Pezzo surfaces).** By Theorems P5.9.26 and P5.9.27, and Example P5.9.11 for $d = 8$, the del Pezzo surfaces have the following invariants, with $\rho = 10 - d$ by part 1 of Proposition P5.9.19 and $h^0(-K) = d + 1$ by part 3 of Theorem P5.9.26 (and $h^0(\mathcal{O}(2, 2)) = 3 \cdot 3 = 9$ on $\mathbb{P}^1 \times \mathbb{P}^1$, the dimension of the space of forms of bidegree $(2, 2)$).

| $d = K^2$ | surface | $\rho$ | $h^0(-K)$ | $(-1)$-curves |
|---|---|---|---|---|
| $9$ | $\mathbb{P}^2$ | $1$ | $10$ | $0$ |
| $8$ | $\mathbb{P}^1 \times \mathbb{P}^1$ | $2$ | $9$ | $0$ |
| $8$ | $S_1 \cong F_1$ | $2$ | $9$ | $1$ |
| $7$ | $S_2$ | $3$ | $8$ | $3$ |
| $6$ | $S_3$ | $4$ | $7$ | $6$ |
| $5$ | $S_4$ | $5$ | $6$ | $10$ |
| $4$ | $S_5$ | $6$ | $5$ | $16$ |
| $3$ | $S_6$ | $7$ | $4$ | $27$ |
| $2$ | $S_7$ | $8$ | $3$ | $56$ |
| $1$ | $S_8$ | $9$ | $2$ | $240$ |

The counts come from part 2 of Theorem P5.9.26. For $r = 6$ the $27$ classes are $6$ of type $E_i$, $\binom{6}{2} = 15$ of type $\ell - E_i - E_j$ and $6$ of type $2\ell - \Sigma_5$, the $27$ lines of the cubic surface of Chapter 10. For $r = 7$ they are $7 + 21 + 21 + 7 = 56$, and for $r = 8$ they are $8 + 28 + 56 + 56 + 56 + 28 + 8 = 240$, where the $56$ classes $4\ell - 2\Sigma_3 - \Sigma_5$ are counted by $\binom{8}{3} = 56$ choices of the three double points. Degree $8$ is the only degree with two surfaces, by Theorem P5.9.27, and they are distinguished by the presence of a $(-1)$-curve. For $d = 9$ and $d = 8$ the embeddings of Theorem P5.9.28 are the Veronese embedding of $\mathbb{P}^2$ by cubics in $\mathbb{P}^9$ and the embedding of $\mathbb{P}^1 \times \mathbb{P}^1$ by $\mathcal{O}(2, 2)$ in $\mathbb{P}^8$, the Segre embedding composed with Veronese embeddings (Theorems P3.10.19 and P3.10.20).

**Example P5.9.30 (degrees seven and six).** On $S_2$ the three $(-1)$-curves are $E_1$, $L = \ell - E_1 - E_2$ and $E_2$, with $E_1 \cdot L = L \cdot E_2 = 1$ and $E_1 \cdot E_2 = 0$, a chain, as in Example P5.7.18. On $S_3$, with $L_{ij} = \ell - E_i - E_j$, the six $(-1)$-curves satisfy $E_i \cdot L_{ij} = 1$, $E_k \cdot L_{ij} = 0$ for $k \notin \{i, j\}$, $E_i \cdot E_j = 0$ and $L_{ij} \cdot L_{ik} = 1 - 1 = 0$, so they form the hexagon $E_1, L_{12}, E_2, L_{23}, E_3, L_{13}$. Contracting the three $E_i$ gives $\mathbb{P}^2$, contracting the three disjoint $L_{ij}$ gives $\mathbb{P}^2$ again, and the composite is the standard Cremona transformation of Example P5.7.16.

**Example P5.9.31 (degree five and the Petersen graph).** On $S_4$ the ten $(-1)$-curves are $E_1, \dots, E_4$ and the six $L_{ij} = \ell - E_i - E_j$. The intersection numbers are $E_i \cdot E_j = 0$, $E_i \cdot L_{jk} = 1$ if $i \in \{j, k\}$ and $0$ otherwise, $L_{ij} \cdot L_{kl} = 1 - 0 = 1$ if $\{i, j\} \cap \{k, l\} = \emptyset$, and $L_{ij} \cdot L_{ik} = 0$. So every curve meets exactly three others. Label the $2$-element subsets of $\{1, \dots, 5\}$ by $E_i \mapsto \{i, 5\}$ and $L_{ij} \mapsto \{1, 2, 3, 4\} \setminus \{i, j\}$. Then $E_i \cdot L_{jk} = 1$ exactly when $i \in \{j, k\}$, that is, when $i$ is not in the complement of $\{j, k\}$, that is, when the labels are disjoint; $L_{ij} \cdot L_{kl} = 1$ exactly when the complementary labels $\{k, l\}$ and $\{i, j\}$ are disjoint; and two labels $\{i, 5\}$, $\{j, 5\}$ always meet. So the intersection graph is the Petersen graph, whose vertices are the $2$-subsets of a $5$-set, joined when disjoint. Its automorphism group $\mathfrak{S}_5$ is larger than the $\mathfrak{S}_4$ permuting the points, and the extra symmetries come from the Cremona transformations based at three of the four points.

**Example P5.9.32 (degree four: sixteen lines and ten conic bundles).** On $S_5$ the sixteen $(-1)$-curves are $E_1, \dots, E_5$, the ten $L_{ij}$ and the conic $Q = 2\ell - \sum_{i=1}^5 E_i$. Each meets exactly five others: $E_i$ meets the four $L_{ij}$ and $Q$, as $E_i \cdot Q = 1$; $L_{ij}$ meets $E_i$, $E_j$ and the three $L_{kl}$ with $\{k, l\} \subseteq \{1, \dots, 5\} \setminus \{i, j\}$, and $L_{ij} \cdot Q = 2 - 2 = 0$; $Q$ meets the five $E_i$. Under the embedding of Theorem P5.9.28 they are lines, as $-K \cdot D = 1$. The classes $F$ with $F^2 = 0$ and $K \cdot F = -2$ that are of the form $\ell - E_i$ or $2\ell - \sum_{j \neq i} E_j$ give ten pencils of conics, $F_i = \ell - E_i$ the lines through $p_i$ and $F'_i = 2\ell - \sum_{j \neq i} E_j$ the conics through the other four points. Each has $F \cdot (-K) = 2$, and by Proposition P5.9.16, whose fibration $|F_i|$ has a section $E_i$, each pencil has $\rho - 2 = 4$ reducible fibres, $L_{ij} + E_j$ for $j \neq i$ in $|F_i|$. They come in the five pairs with $F_i + F'_i = 3\ell - \sum_j E_j = -K$, and $F_i \cdot F'_i = 2 - 0 = 2$, so a conic of one pencil meets a conic of the other in two points.

**Example P5.9.33 (three collinear points).** Let $p_1, p_2, p_3$ lie on a line $M$ and $S = S_3$. The strict transform $\tilde M = \ell - E_1 - E_2 - E_3$ has $\tilde M^2 = 1 - 3 = -2$ and $K \cdot \tilde M = -3 + 3 = 0$. So $-K$ is not ample, by Lemma P5.5.20, and $S$ is not a del Pezzo surface, although $K^2 = 6 > 0$ and $h^0(-K) = 7$. Here $\tilde M$ is the $(-2)$-curve of part 3 of Corollary P5.5.15, and it is the reason for the general position conditions: three collinear points, six points on a conic, or eight points on a cubic singular at one of them give integral curves with $C^2 = -2$ and $K \cdot C = 0$, of classes $\ell - \Sigma_3$, $2\ell - \Sigma_6$ and $3\ell - 2E_i - \Sigma_7$.

### Proof

*Proof of Proposition P5.9.25.* (1) $d = (-K)^2 > 0$ by Lemma P5.5.20. Let $C$ be integral with $C^2 < 0$. Then $K \cdot C < 0$ by Lemma P5.5.20, so $C$ is a $(-1)$-curve by part 2 of Corollary P5.5.15.

(2) By Theorem P5.7.4 and Corollary P5.7.5, $S \cong \operatorname{Bl}_p S'$ with exceptional curve $E$, and $K_S = \psi^* K_{S'} + E$ by part 3 of Theorem P5.6.3. Then $K_{S'}^2 = K_S^2 + 1 = d + 1 > 0$. Let $C' \subseteq S'$ be an integral curve with strict transform $C$, so $\psi^* C' = C + mE$ with $m = C \cdot E \geq 0$ by Proposition P5.6.4. By part 2 of Theorem P5.6.3,
$$-K_{S'} \cdot C' = \psi^*(-K_{S'}) \cdot \psi^* C' = (-K_S + E) \cdot (C + mE) = -K_S \cdot C + m + m - m = -K_S \cdot C + m > 0,$$
using $-K_S \cdot E = 1$ and $E^2 = -1$. So $-K_{S'}$ is ample by the Nakai-Moishezon criterion (Theorem P5.12.5).

(3) On $\mathbb{P}^2$, $-K = 3\ell$ is ample with $(-K)^2 = 9$. For $F_n$, part 4 of Proposition P5.9.9 gives $-K$ ample if and only if $n \leq 1$, and $K^2 = 8$ by part 2. $\square$

*Proof of Theorem P5.9.26.* (1) By Example P5.6.8, $(-K)^2 = 9 - r > 0$. By the Nakai-Moishezon criterion (Theorem P5.12.5) it suffices to show $-K \cdot C > 0$ for every integral curve $C$. If $C = E_i$, then $-K \cdot E_i = 1$. Otherwise $C$ is the strict transform of the integral plane curve $C_0 = \pi(C)$ of some degree $a \geq 1$, with class $a\ell - \sum_i b_i E_i$, $b_i = m_{p_i}(C_0)$, by part 2 of Proposition P5.6.4 applied at each point, and $-K \cdot C = 3a - \sum_i b_i$. If $a = 1$, then $b_i \in \{0, 1\}$ and at most two $b_i$ are $1$, as no three points are collinear, so $\sum b_i \leq 2 < 3$. If $a = 2$, then $C_0$ is a smooth conic (Example P5.5.16), $b_i \leq 1$, and at most five $b_i$ are $1$, so $\sum b_i \leq 5 < 6$. If $a = 3$, then $C_0$ has at most one singular point, of multiplicity $2$, by the genus formula: $p_a(C_0) = 1$ and each singular point lowers the genus of the normalization by at least $m(m - 1)/2$ (Theorem P5.5.14 and Proposition P5.6.14). So $\sum b_i \leq r + 1 \leq 9$, with equality only if $r = 8$ and $C_0$ is singular at one $p_i$, which is excluded. If $a \geq 4$, choose a point $q \in C_0$ distinct from the $p_i$. The cubics through the $r + 1 \leq 9$ points $p_1, \dots, p_r, q$ form a subspace of $H^0(\mathcal{O}_{\mathbb{P}^2}(3))$ of dimension at least $10 - 9 = 1$, so there is a cubic $D_0$ through them. As $C_0$ is integral of degree $a > 3$, $C_0 \not\subseteq D_0$, and by Bézout (Example P5.5.8) and Proposition P5.6.6,
$$3a = \sum_{x \in C_0 \cap D_0} (C_0 \cdot D_0)_x \geq \sum_i m_{p_i}(C_0) \, m_{p_i}(D_0) + (C_0 \cdot D_0)_q \geq \sum_i b_i + 1.$$

(2) A $(-1)$-curve $C$ has $C^2 = -1$ and $K \cdot C = -1$ by the genus formula. Conversely let $D$ be a class with $D^2 = K \cdot D = -1$ on a del Pezzo surface $S$. By Riemann-Roch (Theorem P5.5.13), $h^0(D) + h^0(K - D) \geq \chi(\mathcal{O}_S) + \frac{1}{2} D \cdot (D - K) = \chi(\mathcal{O}_S)$. Here $\chi(\mathcal{O}_S) = 1$ by part 1 of Proposition P5.9.19, as $S$ is rational by Theorem P5.9.27, whose proof does not use the present part. Also $-K \cdot (K - D) = -K^2 - 1 < 0$, so $K - D$ is not effective by Lemma P5.5.20, and $h^0(D) \geq 1$. Write a member as $\sum n_j C_j$ with $C_j$ integral and $n_j \geq 1$. Then $1 = -K \cdot D = \sum_j n_j (-K \cdot C_j)$ with each $-K \cdot C_j \geq 1$, so the member is a single integral curve $C$, with $C^2 = K \cdot C = -1$, a $(-1)$-curve by part 2 of Corollary P5.5.15. Two distinct integral curves $C, C'$ in the class $D$ would have $C \cdot C' = D^2 = -1 < 0$, against Proposition P5.5.5. So $|D| = \{C\}$.

Now let $D = a\ell - \sum b_i E_i$ on $S_r$ with $D^2 = K \cdot D = -1$, so $D$ is a $(-1)$-curve $C$. The class $\ell$ is that of the preimage of a general line, which contains no component of $C$, so $a = \ell \cdot C \geq 0$ by Proposition P5.5.5. If $a = 0$ then $\sum b_i^2 = 1$ and $\sum b_i = -1$, so $D = E_i$. If $a \geq 1$, then $C$ is not an $E_i$ and $b_i = C \cdot E_i \geq 0$, and
$$\sum_i b_i = 3a - 1, \qquad \sum_i b_i^2 = a^2 + 1, \qquad \sum_i b_i (b_i - 1) = (a - 1)(a - 2).$$
By the Cauchy-Schwarz inequality with $r \leq 8$ terms, $(3a - 1)^2 \leq 8(a^2 + 1)$, that is, $(a - 7)(a + 1) \leq 0$, so $a \leq 7$, and $a = 7$ would need equality, all $b_i = 20/8$, which is not an integer. For each $a \leq 6$, the third equation bounds the entries $b_i \geq 2$, and the first then fixes the number of entries equal to $1$. For $a = 1, 2$ all $b_i \leq 1$, with $2$ and $5$ ones. For $a = 3$ there is one entry $2$ and six ones. For $a = 4$, $\sum b_i(b_i - 1) = 6$ allows three entries $2$, with five ones, or one entry $3$, which would need eight ones and nine points. For $a = 5$, the value $12$ allows six entries $2$ and two ones; the other ways to write $12$ as a sum of numbers $b(b - 1) \in \{2, 6, 12, \dots\}$ need at least nine points. For $a = 6$, the value $20$ allows one $3$ and seven $2$, with no ones; again the other decompositions need more than eight points. This gives the list. Each listed class satisfies the two equations, for instance $(6\ell - 3E_1 - 2\Sigma_7)^2 = 36 - 9 - 28 = -1$ and $K \cdot (6\ell - 3E_1 - 2\Sigma_7) = -18 + 3 + 14 = -1$, so it is a $(-1)$-curve on $S_r$ whenever $S_r$ is del Pezzo and the class involves at most $r$ of the $E_j$. Counting the choices of indices gives $r$, $\binom{r}{2}$, $\binom{r}{5}$, $r\binom{r - 1}{6}$, $\binom{r}{3}\binom{r - 3}{5}$, $\binom{r}{6}\binom{r - 6}{2}$ and $r \binom{r - 1}{7}$, and summing for $r = 1, \dots, 8$ gives the stated numbers.

(3) The identification of $|-K|$ is part 2 of Corollary P5.6.5, applied at each point, with $-K = 3\ell - \sum E_i$. For the dimensions, write $S_j$ for the blow-up of $p_1, \dots, p_j$, so $S_j = \operatorname{Bl}_{p_j} S_{j-1}$ with $-K_{S_j} = \pi^*(-K_{S_{j-1}}) - E_j$. The sequence $0 \to \mathcal{O}_{S_j}(-K_{S_j}) \to \pi^* \mathcal{O}(-K_{S_{j-1}}) \to \mathcal{O}_{E_j} \to 0$, part 4 of Theorem P5.6.2 and $h^1(\mathcal{O}_{E_j}) = 0$ give an exact sequence
$$0 \to H^0(-K_{S_j}) \to H^0(-K_{S_{j-1}}) \xrightarrow{\mathrm{ev}} k \to H^1(-K_{S_j}) \to H^1(-K_{S_{j-1}}) \to 0,$$
with $\mathrm{ev}$ the evaluation at $p_j$. It is surjective if some cubic passes through $p_1, \dots, p_{j-1}$ and not through $p_j$. Among $p_1, \dots, p_{j-1}$, at most seven points, choose at most five lying on a conic $Q$ and at most two lying on a line $M$, with the remaining freedom used to avoid $p_j$: if five points are used, $Q$ is the unique conic through them, which does not contain $p_j$ as no six points lie on a conic, and if two points are used, $M$ is the line through them, which does not contain $p_j$ as no three are collinear. Then $Q \cup M$ is the required cubic. Starting from $h^1(\mathcal{O}_{\mathbb{P}^2}(3)) = 0$ and $h^0 = 10$ (Theorem P4.2.1), induction gives $h^1(-K_{S_r}) = 0$ and $h^0(-K_{S_r}) = 10 - r$. $\square$

*Proof of Theorem P5.9.27.* Let $S$ be a del Pezzo surface. Contract $(-1)$-curves as long as there are any; by part 2 of Proposition P5.9.25 each step gives a del Pezzo surface, and the process stops after at most $\rho(S) - 1$ steps by part 3 of Corollary P5.7.14, at a del Pezzo surface $S_0$ with no $(-1)$-curve. As $-K_{S_0}$ is ample, $K_{S_0}$ is not nef, and the cone theorem P5.12.14 gives a $K$-negative extremal ray $R$, of type 2 or 3 in Theorem P5.12.15, since type 1 would be a $(-1)$-curve. In type 3, $S_0 \cong \mathbb{P}^2$. In type 2 there is a fibration $S_0 \to B$ with all fibres $\mathbb{P}^1$, which has a section by Theorem P5.9.18, so $S_0 \cong \mathbb{P}(\mathcal{E})$ over $B$ by Proposition P5.9.5, and $0 < K_{S_0}^2 = 8(1 - g(B))$ by Theorem P5.9.4 forces $B \cong \mathbb{P}^1$. Then $S_0 \cong F_n$ by Proposition P5.9.9, with $n \leq 1$ by part 3 of Proposition P5.9.25, and $n = 0$ as $F_1$ has a $(-1)$-curve. So $S_0$ is $\mathbb{P}^2$ or $F_0$, and $S$ is rational.

If $S = F_0$, the theorem holds. If $S_0 = F_0$ and $S \neq S_0$, the last step $S_1 \to F_0$ is the blow-up of a point and $S_1 \cong \operatorname{Bl}_{q_1, q_2} \mathbb{P}^2$ by Example P5.7.17. In all remaining cases there is a composite of point blow-ups $S = X_r \to X_{r-1} \to \cdots \to X_0 = \mathbb{P}^2$, with $r = K_{\mathbb{P}^2}^2 - K_S^2 = 9 - d$ by part 3 of Theorem P5.6.3, and $r \leq 8$ by part 1 of Proposition P5.9.25. Suppose the centre of $X_{j+1} \to X_j$ lies on the strict transform $\Gamma$ in $X_j$ of an exceptional curve of an earlier step. Then $\Gamma^2 \leq -1$, and by part 4 of Proposition P5.6.4 the strict transform of $\Gamma$ in $X_{j+1}$ has square at most $-2$, and squares of strict transforms do not increase in later steps. Its strict transform in $S$ would be an integral curve of square at most $-2$, against part 1 of Proposition P5.9.25. So every centre maps to a point of $\mathbb{P}^2$ distinct from the earlier ones, and $S \cong \operatorname{Bl}_{p_1, \dots, p_r} \mathbb{P}^2$ with distinct $p_i$, as in Example P5.6.8.

The points are in general position, since each failure gives an integral curve $C$ on $S$ with $C^2 \leq -2$. Three points on a line $M$ give $\tilde M^2 \leq 1 - 3$. Six points on a conic $Q$ give, if $Q$ is integral, $\tilde Q^2 \leq 4 - 6$, and if $Q$ is a pair of lines or a double line, three of the six points on a line. For $r = 8$, let $D_0$ be a cubic through all eight points, singular at $p_1$. If $D_0$ is reducible, it consists of a line and a conic, or of three lines counted with multiplicity, and with no three points collinear and no six on a conic its components contain at most $2 + 5$ or $2 + 2 + 2$ of the eight points; so $D_0$ is integral, and its strict transform has class $3\ell - 2E_1 - \sum_{i \geq 2} E_i$ and square $9 - 4 - 7 = -2$. $\square$

*Proof of Theorem P5.9.28.* By Theorem P5.9.27, $S$ is $\mathbb{P}^2$, $\mathbb{P}^1 \times \mathbb{P}^1$, or $S_r$ with $r = 9 - d \leq 6$ points in general position. For $\mathbb{P}^2$ and $\mathbb{P}^1 \times \mathbb{P}^1$, $-K$ is $\mathcal{O}(3)$ and $\mathcal{O}(2, 2)$, very ample by Theorems P3.10.19 and P3.10.20. For $S_r$, the linear system of cubics through $r \leq 6$ points with no three collinear and no six on a conic is very ample and embeds $S_r$ as a surface of degree $9 - r$ in $\mathbb{P}^{9 - r}$ by Hartshorne, Theorem V.4.6: the cubics through the points separate points and tangent vectors on $S_r$, which is the criterion of Theorem P3.10.12. In each case $h^0(-K) = d + 1$ by Example P5.9.29, the image lies in no hyperplane by part 3 of Theorem P3.10.9, and its degree is $(-K)^2 = d$. For $d = 3$ the image is a surface in $\mathbb{P}^3$ of degree $3$, hence a cubic surface $V(G)$ by Corollary P3.9.11, and it is smooth as it is isomorphic to $S$.

Let $d = 4$ and $X \subseteq \mathbb{P}^4$ the image. By Lemma P5.5.2 a general hyperplane section $C$ is a smooth member of $|-K|$. From $0 \to \mathcal{O}_X(K) \to \mathcal{O}_X \to \mathcal{O}_C \to 0$, $h^0(\mathcal{O}_X(K)) = 0$ by Lemma P5.5.20 and $h^1(\mathcal{O}_X) = 0$ by part 1 of Proposition P5.9.19, $h^0(\mathcal{O}_C) = 1$, so $C$ is connected, hence integral, and $2 p_a(C) - 2 = C \cdot (C + K) = 0$, so $C$ has genus $1$. The line bundle $\mathcal{O}_C(2)$ has degree $2(-K)^2 = 8$, so $h^0(\mathcal{O}_C(2)) = 8$ by Riemann-Roch on $C$ (Theorem P5.1.10). The sequence $0 \to \mathcal{O}_X(1) \to \mathcal{O}_X(2) \to \mathcal{O}_C(2) \to 0$ gives
$$h^0(\mathcal{O}_X(2)) \leq h^0(\mathcal{O}_X(1)) + h^0(\mathcal{O}_C(2)) = 5 + 8 = 13 < 15 = h^0(\mathcal{O}_{\mathbb{P}^4}(2)).$$
So two linearly independent quadrics $Q_1, Q_2$ contain $X$. A quadric containing $X$ is integral, since a reducible or nonreduced quadric is a union of hyperplanes and the integral surface $X$ would lie in one of them. So $Q_1$ and $Q_2$ are distinct integral hypersurfaces, without common component, and $Q_1 \cap Q_2$ has pure dimension $2$ and degree $4$ by Bézout's theorem (Hartshorne, Theorem I.7.7). It contains $X$, of degree $4$, so $X$ is its only component, with multiplicity $1$. A complete intersection has no embedded components, being Cohen-Macaulay (Hartshorne, Proposition II.8.23), and is generically reduced along $X$, so $Q_1 \cap Q_2 = X$ as schemes. $\square$

### Exercises

1. (A) On $S_6$, check that $2\ell - \Sigma_5$ and $\ell - E_i - E_j$ have square $-1$ and canonical degree $-1$, and that $(2\ell - \sum_{j \neq 6} E_j) \cdot E_6 = 0$ while $(2\ell - \sum_{j \neq 6} E_j) \cdot E_1 = 1$. Count the $(-1)$-curves meeting a given one.
2. (A) Show that the hexagon of Example P5.9.30 has exactly two triples of pairwise disjoint curves, and that contracting either triple gives $\mathbb{P}^2$.
3. (B) Show that the $56$ $(-1)$-curves of $S_7$ fall into $28$ pairs $\{D, -K - D\}$, and that $D \cdot (-K - D) = 2$ for each pair.
4. (B) Show that on $S_4$ the classes $F$ with $F^2 = 0$, $K \cdot F = -2$ and $F \cdot C \geq 0$ for every $(-1)$-curve $C$ are exactly $\ell - E_i$ and $2\ell - \sum_{i=1}^4 E_i$, and that each of the five pencils has exactly three reducible fibres.
5. (B) Let $p_1, \dots, p_6$ lie on a smooth conic $Q$, with no three collinear. Show that $\tilde Q^2 = -2$ and $-K \cdot \tilde Q = 0$, and that $-K \cdot C > 0$ for every other integral curve $C$ on $S_6$.
6. (C) Let $p_1, \dots, p_8$ be in general position. Show that $h^0(-K) = 2$, that two members of $|-K|$ meet in exactly one point of $S_8$, and that this point is a base point of $|-K|$, so $-K$ is ample but not base point free.

### Lean

Mathlib has neither blow-ups of surfaces nor the intersection pairing, so the theorems of this section are not formalized. The enumeration in part 2 of Theorem P5.9.26 is a finite computation with integer vectors, which a `decide` proof over bounded ranges could check once the bounds $a \leq 6$ and $b_i \leq 3$ are proved. The handbook adds no `MinimalModel` node here.

### Notes and history

Del Pezzo studied in 1887 the surfaces of degree $d$ in $\mathbb{P}^d$ that are not cones, and showed that they are the plane blown up in $9 - d$ points embedded by cubics, or the quadric surface embedded by $\mathcal{O}(2, 2)$. The modern treatment by the anticanonical class is due to Manin, *Cubic forms* (1972), and to Demazure's seminar of 1976, and the account here follows Hartshorne, Section V.4, and Beauville, Chapter IV. Manin observed that the orthogonal complement of $K$ in $\operatorname{Pic}(S_r)$ is a root lattice of type $A_1 \times A_2$, $A_4$, $D_5$, $E_6$, $E_7$, $E_8$ for $r = 3, \dots, 8$, whose Weyl group permutes the $(-1)$-curves; for $r = 6$ this is $W(E_6)$, of order $51840$, acting on the $27$ lines, and for $r = 8$ the $240$ $(-1)$-curves correspond to the $240$ roots of $E_8$. For $d = 2$ the anticanonical map is a double cover of $\mathbb{P}^2$ branched along a smooth quartic, and the $56$ $(-1)$-curves lie over its $28$ bitangents; for $d = 1$ the system $|-2K|$ is a double cover of a quadric cone in $\mathbb{P}^3$. The literature state is theorem. In the minimal model program, del Pezzo surfaces are the smooth Fano surfaces, and Theorem P5.9.27 shows that every run of the program on one ends at $\mathbb{P}^2$ or at $\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1$; Kollár and Mori, Section 1.3, give the classification from the cone theorem as here.
