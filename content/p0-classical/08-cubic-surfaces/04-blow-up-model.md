---
title: The cubic surface as the blow-up of the plane at six points
nodes: [MMRP5RX4JJ]
sources: [Har77, Bea96, Rei88]
reads_with: [Har77:V.4, Bea96:ch4, Rei88:ch7]
requires: [P0.4, P0.5, P0.6, P0.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The cubic surface as the blow-up of the plane at six points

### Statement

**Definition P0.8.22.** Six points $p_1, \dots, p_6 \in \mathbb{P}^2$ are in *general position* if no three of them lie on a line and the six do not lie on one conic.

Lean: not in Lean.

**Example P0.8.23.** If $\operatorname{char} k = 0$, the points $[1 : 0 : 0]$, $[0 : 1 : 0]$, $[0 : 0 : 1]$, $[1 : 1 : 1]$, $[1 : 2 : 3]$ and $[1 : 3 : 2]$ are in general position. The twenty $3 \times 3$ determinants of three of the points are $\pm 1$, $\pm 2$, $\pm 3$ or $\pm 5$, so they are not 0. The conics through the first five points are the multiples of $YZ - 4XZ + 3XY$, and its value at $[1 : 3 : 2]$ is $7 \neq 0$.

**Example P0.8.24.** Six points on the conic $XZ = Y^2$, for example $[1 : t : t^2]$ for six values of $t$, are not in general position. No three of them lie on a line, since a line meets the conic in at most two points.

**Definition P0.8.25.** Let $p = [0 : 0 : 1]$. The *blow-up* of $\mathbb{P}^2$ at $p$ is
$$
\mathrm{Bl}_p \mathbb{P}^2 = \{([x : y : z], [u : v]) : xv = yu\} \subset \mathbb{P}^2 \times \mathbb{P}^1,
$$
with the first projection $\pi : \mathrm{Bl}_p \mathbb{P}^2 \to \mathbb{P}^2$. The curve $E = \pi^{-1}(p) = \{p\} \times \mathbb{P}^1$ is the *exceptional curve*. For other points, move them to $p$ by a projective change of coordinates. The blow-up at finitely many points $p_1, \dots, p_r$ is the result of blowing up each point in turn; it has exceptional curves $E_1, \dots, E_r$. For a curve $D \subset \mathbb{P}^2$, the *strict transform* $\tilde D$ is the closure of $\pi^{-1}(D \setminus \{p_1, \dots, p_r\})$.

Lean: not in Lean; Mathlib has `ReesAlgebra`, the algebra behind a blow-up, but no blow-up of a variety.

**Example P0.8.26.** The map $\pi$ is an isomorphism over $\mathbb{P}^2 \setminus \{p\}$: for $(x, y) \neq (0, 0)$ the point $[u : v] = [x : y]$ is determined. So $\mathrm{Bl}_p \mathbb{P}^2$ is the closure of the graph of the projection $\mathbb{P}^2 \dashrightarrow \mathbb{P}^1$ from $p$ (Chapter 5), and the second projection makes it a family of lines over $\mathbb{P}^1$: the fibres are the strict transforms of the lines through $p$.

**Example P0.8.27.** Over the chart $z = 1$, $\mathrm{Bl}_p \mathbb{P}^2$ is covered by the two charts $(x, v) \mapsto ((x, xv), [1 : v])$ and $(u, y) \mapsto ((uy, y), [u : 1])$, each isomorphic to $\mathbb{A}^2$. In the first chart $E = \{x = 0\}$, and the strict transform of the line $y = cx$ is $\{v = c\}$.

**Proposition P0.8.28 (intersection numbers on the blow-up).** Let $X$ be the blow-up of $\mathbb{P}^2$ at $p_1, \dots, p_r$, let $\ell$ be the class of the inverse image of a general line, and let $E_i$ be the classes of the exceptional curves. Then the Picard group of $X$ is free with basis $\ell, E_1, \dots, E_r$, and the intersection pairing is
$$
\ell^2 = 1, \qquad E_i^2 = -1, \qquad \ell \cdot E_i = 0, \qquad E_i \cdot E_j = 0 \ (i \neq j).
$$
The canonical class is $K_X = -3\ell + \sum_i E_i$. A curve of degree $d$ with multiplicity $m_i$ at $p_i$ has strict transform of class $d\ell - \sum_i m_i E_i$. For distinct irreducible curves $C$ and $D$, $C \cdot D \ge 0$. For an irreducible curve $C \cong \mathbb{P}^1$, the adjunction formula gives $C^2 + K_X \cdot C = -2$.

Lean: not in Lean.

*Proof.* These facts are Hartshorne, Section V.3, and P5 proves them with the intersection pairing on a smooth projective surface. This section uses them without proof. $\square$

**Theorem P0.8.29 (cubic surfaces as blow-ups).** Let $p_1, \dots, p_6$ be in general position and let $X$ be the blow-up of $\mathbb{P}^2$ at these points. The plane cubics through $p_1, \dots, p_6$ form a vector space of dimension 4. They define an embedding $X \to \mathbb{P}^3$ whose image is a smooth cubic surface $S$, and the class of a plane section is
$$
H = 3\ell - \sum_{i = 1}^{6} E_i = -K_X, \qquad H^2 = 9 - 6 = 3 .
$$
Every smooth cubic surface in $\mathbb{P}^3$ arises in this way.

Lean: not in Lean.

*Proof.* Hartshorne (Section V.4) and Beauville (Ch. IV) prove the Theorem; this section gives the main steps. The cubic forms make a space of dimension 10, and vanishing at a point is one linear condition. For points in general position the six conditions are independent, so the cubics through them form a space of dimension 4. They give a rational map $\mathbb{P}^2 \dashrightarrow \mathbb{P}^3$, which extends to a morphism on $X$ with $H = 3\ell - \sum E_i$. The general position hypothesis is what makes this morphism an embedding: it separates points and tangent directions, also on the curves $E_i$. The degree of the image is $H^2 = 3$, so $S$ is a cubic surface, and it is smooth because $X$ is smooth. For the converse, the proofs in these books use the lines of $S$ (Section 8.3) and Castelnuovo's theorem below to map $S$ onto $\mathbb{P}^2$ as a blow-up at six points. $\square$

**Theorem P0.8.30 (the 27 lines as $(-1)$-curves).** Let $S \cong X$ be as in the previous Theorem. The lines of $S$ are exactly the following 27 curves of $X$:

1. the 6 exceptional curves $E_i$;
2. the 15 strict transforms $F_{ij}$ of the lines $p_i p_j$, of class $\ell - E_i - E_j$;
3. the 6 strict transforms $C_j$ of the conics through the five points $p_i$, $i \neq j$, of class $2\ell - \sum_{i \neq j} E_i$.

Each of them is a curve $C \cong \mathbb{P}^1$ with $C^2 = -1$ and $-K_X \cdot C = 1$.

Lean: not in Lean.

*Proof.* A curve $C \subset X$ maps to a line if and only if $H \cdot C = 1$, because $H \cdot C$ is the degree of the image curve and the embedding is an isomorphism onto the image. Let $C$ be a line of $S$. Then $C \cong \mathbb{P}^1$, and adjunction with $K_X = -H$ gives $C^2 - 1 = -2$, so $C^2 = -1$. Write $C = a\ell - \sum b_i E_i$ with integers $a, b_i$. The two conditions are
$$
3a - \sum_i b_i = 1, \qquad a^2 - \sum_i b_i^2 = -1 .
$$
By the Cauchy-Schwarz inequality, $(\sum b_i)^2 \le 6 \sum b_i^2$, so $(3a - 1)^2 \le 6(a^2 + 1)$, that is, $3a^2 - 6a - 5 \le 0$. The integer solutions of this inequality are $a = 0, 1, 2$. For $a = 0$: $\sum b_i = -1$ and $\sum b_i^2 = 1$, so one $b_i$ is $-1$ and the others are 0, and $C = E_i$. For $a = 1$: $\sum b_i = 2$ and $\sum b_i^2 = 2$, so two of the $b_i$ are 1 and the others are 0, and $C = \ell - E_i - E_j$. For $a = 2$: $\sum b_i = 5$ and $\sum b_i^2 = 5$, so five of the $b_i$ are 1 and one is 0, and $C = 2\ell - \sum_{i \neq j} E_i$. So the class of a line is one of the 27 classes of the statement.

Each of these classes contains at most one irreducible curve: two distinct irreducible curves $C$ and $D$ in one class would have $C \cdot D = C^2 = -1 < 0$. Each class contains an irreducible curve. The class $E_i$ is the exceptional curve. The line $p_i p_j$ contains no third point $p_k$, so its strict transform has class $\ell - E_i - E_j$. Five points with no three on a line lie on exactly one conic, which is irreducible, and it does not pass through $p_j$ by general position; its strict transform has class $2\ell - \sum_{i \neq j} E_i$. Finally, each of the 27 curves has $H \cdot C = 1$: for example $H \cdot F_{ij} = 3 - 1 - 1 = 1$ and $H \cdot C_j = 6 - 5 = 1$. So each of them is a line of $S$. $\square$

**Definition P0.8.31.** A *$(-1)$-curve* on a smooth projective surface $X$ is a curve $E \subset X$ with $E \cong \mathbb{P}^1$ and $E^2 = -1$.

Lean: not in Lean.

**Theorem P0.8.32 (Castelnuovo contraction).** Let $X$ be a smooth projective surface over $k$ and let $E \subset X$ be a $(-1)$-curve. Then there are a smooth projective surface $Y$, a point $p \in Y$ and an isomorphism $X \cong \mathrm{Bl}_p Y$ that sends $E$ to the exceptional curve.

Node: MMRP5RX4JJ · Lean: `MinimalModel.Castelnuovo`

*Proof.* This is Hartshorne, Theorem V.5.7. The handbook proves it in P5, and the Lean statement is stated without a proof. $\square$

### Proof in words

On the blow-up, the lines of the cubic surface are the curves with $H \cdot C = 1$ and $C^2 = -1$. These two conditions are a pair of equations in the integers $a, b_1, \dots, b_6$: one linear and one quadratic. The Cauchy-Schwarz inequality bounds $a$, and a short search gives the 27 solutions. Each solution class contains exactly one irreducible curve, because a curve of negative self-intersection is rigid.

The real work is in the Theorem on cubic surfaces as blow-ups: the cubics through six points in general position give an embedding, and every smooth cubic surface is of this form. That part uses the 27 lines of Section 8.3 and Castelnuovo's theorem in the other direction.

### Examples

The incidences of the 27 lines, computed. The intersection numbers follow from the Proposition on the blow-up:
$$
E_i \cdot F_{jk} = \begin{cases} 1 & i \in \{j, k\}, \\ 0 & \text{otherwise}, \end{cases} \qquad E_i \cdot C_j = \begin{cases} 1 & i \neq j, \\ 0 & i = j, \end{cases}
$$
$$
F_{ij} \cdot F_{kl} = \begin{cases} 1 & \{i, j\} \cap \{k, l\} = \emptyset, \\ 0 & \text{otherwise}, \end{cases} \qquad F_{ij} \cdot C_k = \begin{cases} 1 & k \in \{i, j\}, \\ 0 & \text{otherwise}, \end{cases}
$$
and $E_i \cdot E_j = C_i \cdot C_j = 0$ for $i \neq j$. For example, $F_{12} \cdot F_{34} = 1 - 0 - 0 = 1$, $F_{12} \cdot F_{13} = 1 - 1 = 0$, and $C_1 \cdot C_2 = 4 - 4 = 0$. So $E_1$ meets the 5 lines $F_{1j}$ and the 5 lines $C_j$ with $j \neq 1$, and $F_{1j} \cdot C_j = 1$. The 10 lines that meet $E_1$ form the 5 pairs $\{F_{1j}, C_j\}$, and the 5 tritangent planes through $E_1$ cut out $E_1 \cup F_{1j} \cup C_j$, as Section 8.3 says. The sets $(E_1, \dots, E_6)$ and $(C_1, \dots, C_6)$ form a double six.

A count of moduli. Six points in $\mathbb{P}^2$ have $12$ parameters, and the group $\mathrm{PGL}_3$ of dimension 8 acts on them, so the blow-ups depend on $12 - 8 = 4$ parameters. Cubic surfaces have $19$ parameters, and $\mathrm{PGL}_4$ has dimension 15, so they also depend on $19 - 15 = 4$ parameters.

A hypothesis that fails: six points on a conic. Let $p_1, \dots, p_6$ lie on a smooth conic $Q$, with no three on a line. The strict transform $\tilde Q$ has class $2\ell - \sum E_i$, so
$$
\tilde Q^2 = 4 - 6 = -2, \qquad -K_X \cdot \tilde Q = 6 - 6 = 0 .
$$
The cubics through the six points still give a morphism $X \to \mathbb{P}^3$ onto a cubic surface, but it contracts $\tilde Q$ to a point, so it is not an embedding. The image is a cubic surface with one ordinary double point, the singularity $A_1$ of the quadric cone of Chapter 6. The six classes $2\ell - \sum_{i \neq j} E_i$ are now $\tilde Q + E_j$, which is not irreducible. The lines of the singular surface are the images of the 6 curves $E_i$ and the 15 curves $F_{ij}$, so it contains $6 + 15 = 21$ lines.

### Exercises

1. (A) Let $X$ be the blow-up of $\mathbb{P}^2$ at two points. Show that the $(-1)$-curves of $X$ are $E_1$, $E_2$ and $\ell - E_1 - E_2$.
2. (A) Check that $H \cdot C = 1$ and $C^2 = -1$ for all 27 classes, and that each line meets exactly 10 others.
3. (B) Let $X$ be the blow-up of $\mathbb{P}^2$ at $r$ points in general position. Find all classes $C$ with $C^2 = -1$ and $-K_X \cdot C = 1$ for $r = 4$ and $r = 5$, and show that there are 10 and 16 of them.
4. (B) Show that the 45 tritangent planes of $S$ are the 30 planes with lines $\{E_i, F_{ij}, C_j\}$, $i \neq j$, and the 15 planes with lines $\{F_{ij}, F_{kl}, F_{mn}\}$, where $\{i, j, k, l, m, n\} = \{1, \dots, 6\}$.
5. (B) Contract the six curves $C_1, \dots, C_6$ with Castelnuovo's theorem. Show that the pull back $\ell'$ of a line from the new plane has class $5\ell - 2\sum_i E_i$. (Use $\ell' \cdot C_j = 0$, $\ell'^2 = 1$ and $K_X = -3\ell' + \sum_j C_j$.)

### Lean

Not in Lean. Mathlib has `ReesAlgebra` but no blow-up of a variety and no intersection pairing on a surface. The handbook records Castelnuovo's theorem as the node MMRP5RX4JJ with the Lean name `MinimalModel.Castelnuovo`; the Lean statement is stated, not proved.

### Notes and history

Clebsch showed in 1866 that a smooth cubic surface is the image of the plane by the cubics through six points. Castelnuovo proved the contraction theorem in the 1890s (Hartshorne, Theorem V.5.7). The literature state of both is "theorem". The blow-up of $\mathbb{P}^2$ at $r \le 8$ points in general position is a del Pezzo surface of degree $9 - r$, and the number of its $(-1)$-curves for $r = 1, \dots, 8$ is $1, 3, 6, 10, 16, 27, 56, 240$. In the minimal model program a $(-1)$-curve spans an extremal ray of the cone of curves of a surface, and its contraction is the first example of a divisorial contraction (Volume 1). Volumes 2, 6, 7, 12 and 14 come back to the cubic surface.
