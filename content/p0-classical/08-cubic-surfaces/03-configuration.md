---
title: The configuration of the 27 lines
nodes: []
sources: [Rei88, Har77, Bea96]
reads_with: [Rei88:ch7, Har77:V.4, Bea96:ch4]
requires: [P0.4, P0.6, P0.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The configuration of the 27 lines

### Statement

In this section $S \subset \mathbb{P}^3$ is a smooth cubic surface. For $P \in S$, $T_P S$ is the projective tangent plane of $S$ at $P$ (Chapter 6).

**Definition P0.8.13.** A *tritangent plane* of $S$ is a plane $H$ with $H \cap S = L \cup M \cup N$ for three lines $L$, $M$ and $N$.

Lean: not in Lean.

**Example P0.8.14.** On the Fermat cubic, the plane $x = \alpha y$ with $\alpha^3 = -1$ is a tritangent plane: Section 8.2 shows that it meets $S$ in the three lines $L_{\alpha, \beta}$, $\beta \in \mu$.

**Example P0.8.15.** On the Fermat cubic, the plane $x + y + z + w = 0$ contains the lines $\{x = -y, z = -w\}$, $\{x = -z, y = -w\}$ and $\{x = -w, y = -z\}$. These three lines are not concurrent, and the plane is a tritangent plane.

**Lemma P0.8.16 (lines through a point).** Let $P \in S$ and let $L$ be a line with $P \in L \subset S$. Then $L \subset T_P S$. Hence at most three lines of $S$ pass through $P$, and if three lines pass through $P$, they lie in the plane $T_P S$.

Lean: not in Lean.

*Proof.* The tangent space of the subvariety $L$ at $P$ is contained in the tangent space of $S$ at $P$. For a line, the projective tangent line is $L$ itself, so $L \subset T_P S$. The plane $T_P S$ is not contained in $S$, since a smooth cubic surface contains no plane (Exercise 3 of Section 8.1), so $T_P S \cap S$ is a plane cubic curve. It contains at most three lines. $\square$

**Proposition P0.8.17 (planes through a line).** Let $L \subset S$ be a line. Each plane $H \supset L$ meets $S$ in $L \cup Q_H$, where $Q_H$ is a conic in $H$. There are exactly five planes $H \supset L$ for which $Q_H$ is a pair of lines. For these planes the two lines are distinct and different from $L$.

Lean: not in Lean.

*Proof.* As $H \not\subset S$, $H \cap S$ is a plane cubic curve that contains $L$, so it is $L$ plus a conic $Q_H$. The rest is Reid (Ch. 7). The proof chooses coordinates with $L = \{z = w = 0\}$ and writes the planes through $L$ as $H_{[\lambda : \mu]} = \{\mu z = \lambda w\}$. If $\operatorname{char} k \neq 2$, the conic $Q_H$ is singular exactly where the determinant of its symmetric $3 \times 3$ matrix vanishes. This determinant is a binary form $\Delta(\lambda, \mu)$ of degree 5. Smoothness of $S$ at the points of $L$ shows that $\Delta$ is not 0, that its five roots are distinct, and that $Q_H$ is never a double line or a conic that contains $L$. Hartshorne (Section V.4) gets the same result in every characteristic from the model of Section 8.4. $\square$

**Theorem P0.8.18 (configuration of the 27 lines).** Let $S$ be a smooth cubic surface.

1. Each line $L \subset S$ meets exactly 10 other lines of $S$. They form 5 pairs, and the two lines of a pair meet each other.
2. $S$ contains exactly 27 lines.
3. Two skew lines of $S$ have exactly 5 common transversals among the lines of $S$.
4. $S$ has exactly 45 tritangent planes. Of the $\binom{27}{2} = 351$ pairs of lines, 135 meet and 216 are skew.

Lean: not in Lean.

*Proof.* (1) A line $M \neq L$ of $S$ that meets $L$ spans a plane $H$ with $L$, and $H \cap S$ contains $L$ and $M$, so $Q_H$ is a pair of lines. Hence $M$ lies in one of the five planes of the Proposition. Each such plane contributes two lines that meet each other and meet $L$. Two different planes through $L$ meet only in $L$, so the ten lines are distinct.

(2) Section 8.1 gives a line $L$, and (1) gives a tritangent plane $H$ with $H \cap S = L \cup M \cup N$. Let $X$ be a line of $S$ that is not $L$, $M$ or $N$. Then $X \not\subset H$, so $X$ meets $H$ in one point $P$, and $P \in L \cup M \cup N$. Suppose $P$ lies on two of the lines, say $L$ and $M$. Then $L$, $M$ and $X$ pass through $P$, and by the Lemma all three lie in the plane $T_P S$. This plane contains $L$ and $M$, so it is $H$, and $X \subset H$, a contradiction. So $X$ meets exactly one of $L$, $M$ and $N$. By (1), each of $L$, $M$ and $N$ meets exactly $10 - 2 = 8$ lines outside $\{L, M, N\}$. So $S$ contains $3 + 3 \cdot 8 = 27$ lines.

(3) Let $L_1$ and $L_2$ be skew. Every common transversal meets $L_1$, so by (1) it lies in one of the five tritangent planes $H$ through $L_1$. Fix such a plane, with $H \cap S = L_1 \cup M \cup M'$. The line $L_2$ is not in $H$, since it does not meet $L_1$. So $L_2$ meets $H$ in one point, which lies on $M$ or $M'$ but not on $L_1$. The argument of (2) shows that it does not lie on both. So each of the five planes gives exactly one common transversal.

(4) By (1) and (2), there are $27 \cdot 10 / 2 = 135$ pairs of lines that meet, and $351 - 135 = 216$ skew pairs. A tritangent plane contains three pairs that meet. Each pair that meets spans one plane, and that plane is tritangent. So there are $135 / 3 = 45$ tritangent planes. $\square$

**Definition P0.8.19.** A *double six* on $S$ is a pair of ordered sets of six lines $(a_1, \dots, a_6)$ and $(b_1, \dots, b_6)$ such that the $a_i$ are pairwise skew, the $b_j$ are pairwise skew, and $a_i$ meets $b_j$ if and only if $i \neq j$.

Lean: not in Lean.

**Example P0.8.20.** Section 8.4 shows that the six exceptional curves $E_i$ of the blow-up of $\mathbb{P}^2$ and the six conics $C_j$ through five of the points form a double six $(E_1, \dots, E_6)$, $(C_1, \dots, C_6)$.

**Example P0.8.21.** In the notation of Section 8.4, $(E_1, E_2, E_3, F_{45}, F_{46}, F_{56})$ and $(F_{23}, F_{13}, F_{12}, C_6, C_5, C_4)$ form a double six. A smooth cubic surface has 36 double sixes.

### Proof in words

Through a line $L$ of $S$ there is a pencil of planes, and each plane cuts out $L$ and a conic. The conic degenerates for exactly five planes, the roots of a quintic, and smoothness makes the roots distinct. This gives the ten lines that meet $L$. A tritangent plane $L \cup M \cup N$ then sorts all other lines: each other line meets the plane in one point, which lies on exactly one of the three lines. The count $3 + 3 \cdot 8 = 27$ follows.

The hard step is the quintic: its degree is 5 and its roots are simple. The rest is the Lemma that a line through $P$ lies in the tangent plane at $P$, used in several places.

### Examples

The Fermat cubic, checked against the Theorem. Take $L = L_{\alpha, \beta}$ of Section 8.2. The four lines of its own pairing that meet it lie in the two planes $x = \alpha y$ and $z = \beta w$, two lines in each. The three lines $L'$ and the three lines $L''$ that meet $L$ lie in three more planes. Two lines $L'_{\gamma, \delta}$ and $L'_{\gamma', \delta'}$ that meet $L$ have $\gamma \beta = \alpha \delta$ and $\gamma' \beta = \alpha \delta'$, so they differ in both indices and are skew. So each of the three planes contains one $L'$ and one $L''$. This gives $2 + 3 = 5$ tritangent planes through $L$ and $2 \cdot 5 = 10$ lines that meet $L$. In the two planes $x = \alpha y$ and $z = \beta w$, the three lines are concurrent, at $[\alpha : 1 : 0 : 0]$ and at $[0 : 0 : \beta : 1]$.

A hypothesis that fails: a cone. Let $S = \{x_0^3 + x_1^3 + x_2^3 = 0\} \subset \mathbb{P}^3$, the cone over a smooth plane cubic $C$ with vertex $v = [0 : 0 : 0 : 1]$. For every point $c \in C$, the line $vc$ lies on $S$, so $S$ contains infinitely many lines. The surface is singular at $v$. The Proposition fails: a plane $H$ through $L = vc$ passes through $v$, and it is the cone over a line $\ell \subset \mathbb{P}^2$ through $c$. So $H \cap S$ is the cone over the three points of $\ell \cap C$, that is, three lines through $v$, counted with multiplicity. Every plane through $L$ meets $S$ in lines, not only five of them. A cubic surface with one ordinary double point contains exactly 21 lines; Section 8.4 explains this number.

### Exercises

1. (A) Let $H$ be a plane that contains a line $L$ of $S$. Show that $H \cap S = L \cup Q_H$ with $Q_H$ a conic of $H$, and that $Q_H$ meets $L$ in two points, counted with multiplicity.
2. (A) Show that every pair of lines of $S$ that meet lies in exactly one tritangent plane, and that every line lies in exactly 5 tritangent planes. Check $45 \cdot 3 = 27 \cdot 5$.
3. (B) Let $L_1$ and $L_2$ be skew lines of $S$, and let $M_1, \dots, M_5$ be their common transversals. Show that the lines $M_i$ are pairwise skew. (If $M_1$ and $M_2$ meet, show that $L_1$ and $L_2$ lie in the plane of $M_1$ and $M_2$.)
4. (B) Show that a point $P \in S$ lies on 0, 1, 2 or 3 lines of $S$, and that $P$ lies on 2 or 3 lines if and only if $T_P S$ is a tritangent plane.
5. (B) (M) Use Macaulay2 or Sage. Take a random cubic form $F$ in four variables with coefficients in $\mathbb{F}_{101}$, and compute the Fano scheme of lines on $V(F)$ (in Macaulay2, the function `Fano`). Check that it has dimension 0 and degree 27. Then do the same for the Fermat cubic over $\mathbb{Q}$, and for the cubic $x_0 x_1 x_2 = x_3^3$, and explain the answers.

### Lean

Not in Lean. A formal proof would need the projective tangent plane of a hypersurface and the discriminant of a pencil of conics; Mathlib has neither for projective varieties.

### Notes and history

Cayley and Salmon found the 27 lines in 1849, and Schläfli found the double six in 1858. The proof by the quintic of a pencil of conics is in Reid (Ch. 7), and Hartshorne proves the count in every characteristic as Theorem V.4.9. Beauville (Ch. IV) treats the configuration with the model of Section 8.4. The literature state is "theorem". The symmetry group of the configuration is the Weyl group $W(E_6)$, of order 51840. Volumes 2, 6, 7, 12 and 14 come back to the cubic surface and its lines.
