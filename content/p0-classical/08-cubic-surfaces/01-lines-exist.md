---
title: Every cubic surface contains a line
nodes: []
sources: [Rei88, Har92, Sha13, Har77]
reads_with: [Rei88:ch7, Sha13:ch1, Har77:V.4]
requires: [P0.4, P0.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Every cubic surface contains a line

### Statement

**Definition P0.8.1.** A *cubic surface* is a nonzero cubic form $F \in k[x_0, x_1, x_2, x_3]$, up to a nonzero constant, with the set of points $S = V(F) \subset \mathbb{P}^3$. The cubic forms make a vector space of dimension $\binom{6}{3} = 20$, so the cubic surfaces are the points of $\mathbb{P}^{19}$. The surface is *smooth* if the four partial derivatives of $F$ have no common zero on $S$.

Lean: not in Lean; Mathlib has `MvPolynomial.zeroLocus` for the set $V(F)$ and `Projectivization` for $\mathbb{P}^3$.

**Example P0.8.2.** The Fermat cubic $x_0^3 + x_1^3 + x_2^3 + x_3^3$ is smooth if $\operatorname{char} k \neq 3$: the partial derivatives $3x_i^2$ vanish together only at 0.

**Example P0.8.3.** The cone $x_0^3 + x_1^3 + x_2^3$ is not smooth: all partial derivatives vanish at $[0 : 0 : 0 : 1]$. It contains the line through $[0 : 0 : 0 : 1]$ and each point of the plane cubic $x_0^3 + x_1^3 + x_2^3 = 0$ in $\{x_3 = 0\}$, so it contains infinitely many lines.

**Definition P0.8.4.** The *Grassmannian* $G(1, 3)$ is the set of lines in $\mathbb{P}^3$, that is, of 2-dimensional subspaces $W \subset k^4$. The Plücker map sends $W = \langle u, v \rangle$ to the point $[u \wedge v] \in \mathbb{P}(\wedge^2 k^4) = \mathbb{P}^5$. Its image is the quadric $p_{01} p_{23} - p_{02} p_{13} + p_{03} p_{12} = 0$, a smooth projective variety of dimension 4.

Lean: Mathlib has `Module.Grassmannian` (the functor $G(k, M; A)$ of quotients of rank $k$), not the Plücker embedding.

**Example P0.8.5.** The lines that do not meet $\{x_0 = x_1 = 0\}$ are the row spaces of the matrices
$$
\begin{pmatrix} 1 & 0 & a & b \\ 0 & 1 & c & d \end{pmatrix}, \qquad (a, b, c, d) \in k^4 .
$$
This is an open subset of $G(1, 3)$ isomorphic to $\mathbb{A}^4$. Six charts of this kind cover $G(1, 3)$.

**Lemma P0.8.6 (cubics through a line).** Let $L \subset \mathbb{P}^3$ be a line. The cubic surfaces that contain $L$ form a linear subspace $\mathbb{P}^{15} \subset \mathbb{P}^{19}$.

Lean: not in Lean.

*Proof.* Choose coordinates with $L = \{x_2 = x_3 = 0\}$. Then $L \subset V(F)$ if and only if $F(x_0, x_1, 0, 0) = 0$. This is the vanishing of the four coefficients of $x_0^3$, $x_0^2 x_1$, $x_0 x_1^2$ and $x_1^3$. These are four independent linear conditions on the 20 coefficients of $F$, so the solutions form a vector space of dimension 16. $\square$

**Theorem P0.8.7 (lines on cubic surfaces).** Every cubic surface in $\mathbb{P}^3$ contains at least one line.

Lean: not in Lean.

*Proof.* Let $\Sigma = \{(L, F) : L \subset V(F)\} \subset G(1, 3) \times \mathbb{P}^{19}$. In the chart of the Example above, the line $L$ is $\{[s : t : sa + tc : sb + td]\}$. The condition $L \subset V(F)$ is that the four coefficients of the binary cubic $F(s, t, sa + tc, sb + td)$ vanish. These coefficients are polynomials in $(a, b, c, d)$ and linear forms in the coefficients of $F$. So $\Sigma$ is closed, and over this chart it is a bundle of linear spaces $\mathbb{P}^{15}$, by the Lemma. The same holds on each chart. Hence $\Sigma$ is irreducible of dimension $4 + 15 = 19$.

Let $\pi : \Sigma \to \mathbb{P}^{19}$ be the second projection. As $G(1, 3)$ is projective, $\pi(\Sigma)$ is closed and irreducible. Suppose $\dim \pi(\Sigma) = m < 19$. By the theorem on the dimension of fibres (Shafarevich, Ch. 1), every nonempty fibre of $\Sigma \to \pi(\Sigma)$ has dimension at least $19 - m \ge 1$. The fibre over $F$ is the set of lines on $V(F)$. Section 8.2 shows that the Fermat cubic contains exactly 27 lines, a nonempty finite set, if $\operatorname{char} k \neq 3$. In every characteristic, Section 8.4 gives a smooth cubic surface with exactly 27 lines: the blow-up of $\mathbb{P}^2$ at six points in general position. Either surface gives a contradiction, so $\pi(\Sigma) = \mathbb{P}^{19}$. $\square$

### Proof in words

Count dimensions. A line moves in a family of dimension 4, and containing a given line is 4 linear conditions on a cubic surface. So the pairs (line, cubic containing it) form a variety of dimension $4 + 15 = 19$, the same as the dimension of all cubic surfaces. The map to the space of cubic surfaces is then surjective if one fibre is finite and nonempty, and the Fermat cubic gives such a fibre.

The difficulty is that a dimension count alone gives only "at most": the map could have positive dimensional fibres everywhere and miss most surfaces. One explicit surface with finitely many lines closes this gap.

### Examples

The cubics through a line, computed directly. Let $L = \{x_2 = x_3 = 0\}$. A cubic contains $L$ if and only if it lies in the ideal $(x_2, x_3)$, that is, $F = x_2 A + x_3 B$ with quadrics $A$ and $B$. The pairs $(A, B)$ form a space of dimension $10 + 10 = 20$. The pair $(x_3 C, -x_2 C)$ with $C$ linear gives $F = 0$, and these pairs are the full kernel, of dimension 4. So the cubics through $L$ form a space of dimension $20 - 4 = 16$, as in the Lemma.

A hypothesis that fails: degree 4. Quartic forms in four variables make a space of dimension $\binom{7}{3} = 35$, so the quartic surfaces are the points of $\mathbb{P}^{34}$. Containing a line is now 5 linear conditions, so the incidence variety has dimension $4 + 29 = 33 < 34$. Its image in $\mathbb{P}^{34}$ is a proper closed subset, and a general quartic surface contains no line. The Fermat quartic $\sum x_i^4$ still contains lines, for example $x_0 = \varepsilon x_1$, $x_2 = \varepsilon x_3$ with $\varepsilon^4 = -1$.

### Exercises

1. (A) Find the dimension of the space of cubic surfaces that contain two given skew lines, and of those that contain two given lines that meet.
2. (A) Show that the smooth quadric $x_0 x_1 = x_2 x_3$ contains two families of lines, each of dimension 1, and that two lines of the same family do not meet.
3. (A) Show that a plane meets a cubic surface in a plane cubic curve or is contained in it, and that a smooth cubic surface contains no plane.
4. (B) Show that a general surface of degree $d \ge 4$ in $\mathbb{P}^3$ contains no line.
5. (B) Let $\operatorname{char} k \neq 3$. Show that the cubic surface $x_0 x_1 x_2 = x_3^3$ is singular at three points, and that it contains the three lines $\{x_i = x_3 = 0\}$ for $i = 0, 1, 2$.

### Lean

Not in Lean. Mathlib has `Module.Grassmannian` and `Projectivization`, and `MvPolynomial.zeroLocus` for the set of a form, but no incidence variety and no theorem on the dimension of fibres of a morphism of varieties.

### Notes and history

Cayley and Salmon found in 1849 that a smooth cubic surface contains exactly 27 lines; the existence of one line is the first step. Harris uses the same incidence variety for the Fano variety of lines of a hypersurface, and Reid (Ch. 7) treats the lines of a cubic surface with explicit equations. The literature state is "theorem". The variety of lines on a hypersurface is its Fano scheme. Section 8.4 explains the lines as curves with self-intersection $-1$.
