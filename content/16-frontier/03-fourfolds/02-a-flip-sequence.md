---
title: A sequence of 4-fold flips, checked by hand
nodes: [MMAWP4SA44, MMFAWNT87R]
sources: [FS04, Rei83, CLS11, KM98, KMM87]
reads_with: []
requires: ["3.3", "3.5", "3.6", "3.7"]
level: research
kind: survey
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## A sequence of 4-fold flips, checked by hand

### Statement

This section works one example with the toric tools of Volume 3: a projective $\mathbb{Q}$-factorial terminal toric 4-fold $X_0$ of Picard number 2 with two curves of quotient singularities, and its $K$-programs. One program is a single Mori fibre space. The other is a sequence of two flips followed by a Mori fibre space. Its termination is checked by hand in two ways: by listing all programs through the chambers of the secondary fan, and by a count of toric valuations of small log discrepancy that drops at each flip.

Let $N = \mathbb{Z}^4$ and take the six primitive vectors
$$v_1 = (-1, -1, -1, 0), \quad v_2 = e_1, \quad v_3 = e_2, \quad v_4 = e_3, \quad v_5 = (0, -2, -3, -1), \quad v_6 = e_4.$$
They satisfy the two relations
$$v_1 + v_2 + v_3 + v_4 = 0, \qquad 2 v_3 + 3 v_4 + v_5 + v_6 = 0,$$
and these span the space of relations, which has dimension $6 - 4 = 2$. So the Gale dual of Definition 3.7.1 is $G_U = \mathbb{R}^2$ with
$$\beta_1 = \beta_2 = (1, 0), \quad \beta_3 = (1, 2), \quad \beta_4 = (1, 3), \quad \beta_5 = \beta_6 = (0, 1).$$
The effective cone is $\operatorname{Cone}(B)$, the closed first quadrant, and the vectors $\beta_\rho$ cut it into three chambers (Theorem 3.7.9):
$$\Gamma_0 = \operatorname{Cone}((1,0), (1,2)), \qquad \Gamma_1 = \operatorname{Cone}((1,2), (1,3)), \qquad \Gamma_2 = \operatorname{Cone}((1,3), (0,1)).$$
For a chamber $\Gamma$, the maximal cones of its fan are the cones $\sigma_I = \operatorname{Cone}(v_i : i \in I)$ with $|I| = 4$ such that the interior of $\Gamma$ lies in the interior of $\operatorname{Cone}(\beta_j : j \notin I)$, by Definition 3.7.7, Theorem 3.7.8 and Lemma 3.7.2. The index of $\sigma_I$, the order of $N / \sum_{i \in I} \mathbb{Z} v_i$, is $|\det(\beta_j, \beta_k)|$ for $\{j, k\}$ the complement of $I$. Let $X_k$ be the toric variety of $\Gamma_k$. The class of $-K = \sum_\rho D_\rho$ is $\sum_\rho \beta_\rho = (4, 7)$, of slope $\frac74$, in the interior of $\Gamma_0$.

**Proposition 16.3.13 (the programs of $X_0$).** The variety $X_0$ is a $\mathbb{Q}$-factorial terminal Fano 4-fold of Picard number 2, singular exactly along two disjoint curves: one with transversal type $\frac13(1, 1, 2)$ and one with transversal type $\frac12(1, 1, 1)$. Every $K$-program from $X_0$ is one of the two sequences
$$X_0 \to \mathbb{P}^1, \qquad X_0 \dashrightarrow X_1 \dashrightarrow X_2 \to \mathbb{P}^1.$$
The first is a Mori fibre space with fibre $\mathbb{P}(1, 1, 2, 3)$. In the second, the first flip replaces the $\frac12(1,1,1)$ curve by a plane $\mathbb{P}^2$ in the smooth locus of $X_1$, the second flip replaces a surface that contains the $\frac13(1,1,2)$ curve by a smooth rational curve, $X_2$ is smooth, and $X_2 \to \mathbb{P}^1$ is a $\mathbb{P}^3$-bundle. Let $d(X)$ be the number of points $w \in N$ that are not among $v_1, \dots, v_6$ and have log discrepancy $\psi_{K_X}(w) < 2$. Then
$$d(X_0) = 3, \qquad d(X_1) = 2, \qquad d(X_2) = 0.$$

Lean: not yet in Lean.

### Proof in words

**The fans.** For $\Gamma_0$, take the interior point $(1, 1)$. A pair $\{j, k\}$ has $(1, 1)$ in the interior of $\operatorname{Cone}(\beta_j, \beta_k)$ exactly when one of $\beta_j, \beta_k$ has slope less than 1 and the other slope greater than 1, so $j \in \{1, 2\}$ and $k \in \{3, 4, 5, 6\}$. This gives eight maximal cones. Their indices are
$$|\det(\beta_1, \beta_3)| = 2, \quad |\det(\beta_1, \beta_4)| = 3, \quad |\det(\beta_1, \beta_5)| = |\det(\beta_1, \beta_6)| = 1,$$
and the same with $\beta_2$. So the singular maximal cones are $\sigma_{\{2,4,5,6\}}$ and $\sigma_{\{1,4,5,6\}}$ of index 2, and $\sigma_{\{2,3,5,6\}}$ and $\sigma_{\{1,3,5,6\}}$ of index 3. Their common faces $\operatorname{Cone}(v_4, v_5, v_6)$, of index 2, and $\operatorname{Cone}(v_3, v_5, v_6)$, of index 3, are the singular 3-dimensional cones, and all their other faces are smooth. So $X_0$ is singular exactly along the curves $V(\operatorname{Cone}(v_4, v_5, v_6))$ and $V(\operatorname{Cone}(v_3, v_5, v_6))$, which are disjoint since no cone contains $v_3, v_4, v_5, v_6$.

For $\Gamma_1$, with the interior point $(2, 5)$ of slope $\frac52$, the pairs are $\{1, 2, 3\} \times \{4, 5, 6\}$: nine cones. The only singular face is $\operatorname{Cone}(v_3, v_5, v_6)$, of index 3, from $|\det(\beta_1, \beta_4)| = 3$. For $\Gamma_2$, with the point $(1, 4)$, the pairs are $\{1, 2, 3, 4\} \times \{5, 6\}$, and every determinant $|\det(\beta_j, \beta_5)|$ is 1. So $X_2$ is smooth.

**The singularities.** The point $\frac13 (2 v_3 + v_5 + v_6) = (0, 0, -1, 0)$ lies in $N$, so $\operatorname{Cone}(v_3, v_5, v_6)$ has the transversal type $\frac13(2, 1, 1)$, which is $\frac13(1, 1, 2)$ after the order of the coordinates is changed. The point $\frac12 (v_4 + v_5 + v_6) = (0, -1, -1, 0)$ lies in $N$, so $\operatorname{Cone}(v_4, v_5, v_6)$ has type $\frac12(1, 1, 1)$. Both types are terminal quotient singularities of 3-folds, of the form $\frac1r(1, -1, a)$. A transversal type times a smooth curve is terminal, so $X_0$ and $X_1$ are terminal; this is also part of the count below, by Theorem 3.3.36.

**The walls.** By Theorem 3.7.13, a facet of a chamber on the ray of $g$ has the wall relation $b$ with $\langle \cdot, b \rangle$ vanishing on $g$ and nonnegative on the chamber, and for $D = \sum_\rho a_\rho D_\rho$ the number $D \cdot V(\tau)$ is a positive multiple of $\langle [a], b \rangle$. In the coordinates $g = (g_1, g_2)$ of $G_U$, the relation $b = c_1 r_1 + c_2 r_2$, with $r_1 = (1,1,1,1,0,0)$ and $r_2 = (0,0,2,3,1,1)$ the two relations above, pairs as $\langle g, b \rangle = c_1 g_1 + c_2 g_2$. The facets are:

| Chamber | Facet | Relation $b$ | $\langle (4,7), b \rangle$ | Step |
|---|---|---|---|---|
| $\Gamma_0$ | $(1, 0)$ | $r_2 = (0,0,2,3,1,1)$ | $7$ | Mori fibre space to $\mathbb{P}^1$ |
| $\Gamma_0$ | $(1, 2)$ | $2r_1 - r_2 = (2,2,0,-1,-1,-1)$ | $1$ | flip to $X_1$ |
| $\Gamma_1$ | $(1, 2)$ | $r_2 - 2r_1$ | $-1$ | $K$-positive |
| $\Gamma_1$ | $(1, 3)$ | $3r_1 - r_2 = (3,3,1,0,-1,-1)$ | $5$ | flip to $X_2$ |
| $\Gamma_2$ | $(1, 3)$ | $r_2 - 3r_1$ | $-5$ | $K$-positive |
| $\Gamma_2$ | $(0, 1)$ | $r_1 = (1,1,1,1,0,0)$ | $4$ | Mori fibre space to $\mathbb{P}^1$ |

A ray is $K$-negative exactly when $\langle (4,7), b \rangle > 0$, since $-K$ has class $(4,7)$. The facets $(1,0)$ and $(0,1)$ lie on the boundary of $\operatorname{Cone}(B)$, so they are of fibre type (Theorem 3.7.13, part 5). The facets on $(1,2)$ and $(1,3)$ meet the interior of $\operatorname{Cone}(B)$, so by part 5 their rays are not of fibre type. They are not divisorial either: by part 4 the chamber across a divisorial facet belongs to a fan that leaves out a vector, while the chambers across these two facets are $\Gamma_1$ and $\Gamma_2$, whose fans use all six vectors, and by Theorem 3.7.9 a general class near the facet lies in one chamber only. So these rays are small and give flips (part 3). The table lists every ray of every model, so every program is one of the two sequences of the proposition (Corollary 3.7.14). Each flip crosses a wall to the side where $\langle (4,7), b \rangle$ is negative, so the walk moves away from the class of $-K$.

**The flips.** The relation $2 v_1 + 2 v_2 = v_4 + v_5 + v_6$ of the first flip says that the cones of $X_0$ that contain $\operatorname{Cone}(v_4, v_5, v_6)$ are replaced by the cones of $X_1$ that contain $\operatorname{Cone}(v_1, v_2)$ (Theorem 3.5.20). So the flipping curve is the $\frac12(1,1,1)$ curve $C_0 = V(\operatorname{Cone}(v_4, v_5, v_6))$, with $-K \cdot C_0$ a positive multiple of $2 + 2 - 1 - 1 - 1 = 1$. The flipped locus is $S_1 = V(\operatorname{Cone}(v_1, v_2))$. The three cones of $X_1$ that contain it, $\sigma_{\{1,2,5,6\}}$, $\sigma_{\{1,2,4,6\}}$ and $\sigma_{\{1,2,4,5\}}$, are smooth, and the images of $v_4, v_5, v_6$ in $N / (\mathbb{Z} v_1 + \mathbb{Z} v_2) \cong \mathbb{Z}^2$ are $(1, 0)$, $(-1, -1)$ and $(0, 1)$. So $S_1 \cong \mathbb{P}^2$ lies in the smooth locus. For a line $\ell \subset S_1$, the numbers $D_\rho \cdot \ell$ are $(-2, -2, 0, 1, 1, 1)$, so $\mathcal{N}_{S_1} = \mathcal{O}(-2)^{\oplus 2}$ and $K_{X_1} \cdot \ell = 1$: the plane is $K$-positive, as a flip requires.

The relation $3 v_1 + 3 v_2 + v_3 = v_5 + v_6$ of the second flip replaces the cones of $X_1$ that contain $\operatorname{Cone}(v_5, v_6)$, namely $\sigma_{\{2,3,5,6\}}$, $\sigma_{\{1,3,5,6\}}$ and $\sigma_{\{1,2,5,6\}}$, by the cones of $X_2$ that contain $\operatorname{Cone}(v_1, v_2, v_3)$. So it replaces the surface $S' = V(\operatorname{Cone}(v_5, v_6))$, which contains the $\frac13(1,1,2)$ curve $V(\operatorname{Cone}(v_3, v_5, v_6))$, by the curve $\Gamma = V(\operatorname{Cone}(v_1, v_2, v_3)) \cong \mathbb{P}^1$ in the smooth variety $X_2$. On $\Gamma$ the numbers $D_\rho \cdot \Gamma$ are $(-3, -3, -1, 0, 1, 1)$, so $K_{X_2} \cdot \Gamma = 5$.

**The two Mori fibre spaces.** The facet $(1, 0)$ of $\Gamma_0$ is spanned by $\beta_1 = \beta_2$, and the contraction is given by the two sections $x_1, x_2$ of the class $(1, 0)$ of the Cox ring: $X_0 \to \mathbb{P}^1$. Its fibre is the quotient of the coordinates $(x_3, x_4, x_5, x_6)$ by the second weights $(2, 3, 1, 1)$, that is $\mathbb{P}(1, 1, 2, 3)$. In the same way $X_2 \to \mathbb{P}^1$ is given by $x_5, x_6$, and its fibre is the quotient of $(x_1, x_2, x_3, x_4)$ by the first weights $(1, 1, 1, 1)$, that is $\mathbb{P}^3$.

**The count.** By Proposition 3.3.35, $\psi_{K_X}(w) = \sum_i \lambda_i$ for $w = \sum_i \lambda_i v_i$ in a cone of the fan with all $\lambda_i \ge 0$. In a smooth cone the $\lambda_i$ of a lattice point are integers, so $\psi < 2$ forces $w = 0$ or $w = v_i$. Hence only the singular cones contribute, and in a simplicial cone a lattice point with $\psi < 2$ is a nonzero point of the box $\{\sum_i \lambda_i v_i : 0 \le \lambda_i < 1\}$, or such a point plus one $v_i$ when its $\psi$ is less than 1, which does not happen here. The box points are:

- in $\operatorname{Cone}(v_3, v_5, v_6)$, of index 3: $\frac23 v_3 + \frac13 v_5 + \frac13 v_6 = (0, 0, -1, 0)$ with $\psi = \frac43$, and $\frac13 v_3 + \frac23 v_5 + \frac23 v_6 = (0, -1, -2, 0)$ with $\psi = \frac53$;
- in $\operatorname{Cone}(v_4, v_5, v_6)$, of index 2: $\frac12 (v_4 + v_5 + v_6) = (0, -1, -1, 0)$ with $\psi = \frac32$.

The singular maximal cones have the same index as these faces, so they have no other box points. This gives $d(X_0) = 3$. After the first flip, $(0, -1, -1, 0) = v_1 + v_2$ has $\psi_{K_{X_1}} = 2$, and the other two points are unchanged, so $d(X_1) = 2$. After the second flip, $(0, 0, -1, 0) = v_1 + v_2 + v_3$ has $\psi = 3$ and $(0, -1, -2, 0) = 2 v_1 + 2 v_2 + v_3$ has $\psi = 5$, so $d(X_2) = 0$. All values of $\psi$ at points other than the $v_i$ are greater than 1, which is the terminal criterion of Theorem 3.3.36. $\square$

**Why the count is a termination argument here.** By Corollary 3.6.2 a $K$-flip does not lower $\psi_K$ at any point and raises it at each point of a cone that is not common to the two fans. So $d$ never goes up along a program, and it drops at a flip whenever a point counted by $d$ lies in the flipping locus. In this example each flip passes through a singular curve and $d$ drops: by 1 at the first flip and by 2 at the second. Since $d \ge 0$, a sequence of flips from $X_0$ that drops $d$ each time has length at most $d(X_0) = 3$. The example in Section 16.3.1 of a smooth flip shows that $d$ alone does not prove termination of toric flips in general; Theorem 3.6.3 does, by a different argument.

### Examples

**Example 16.3.14 (the Mori fibre space ends the program at once).** From $X_0$ the facet $(1, 0)$ gives $X_0 \to \mathbb{P}^1$, and the program stops there, with no flip. So two programs from one variety can have different lengths and different end points: the fibre $\mathbb{P}(1, 1, 2, 3)$ is singular, while the fibre $\mathbb{P}^3$ of $X_2 \to \mathbb{P}^1$ is smooth. Which program is run depends on the choice of extremal ray at $X_0$, or, for the program with scaling of an ample class $H$, on the position of $[H]$ in $\Gamma_0$: by Corollary 3.7.14 the program with scaling follows the segment from $[H]$ toward the class of $K$, and the first facet that this segment meets decides the first step.

**Example 16.3.15 (the program with scaling).** Take $H$ with class $h = (h_1, h_2)$ in the interior of $\Gamma_0$, so $0 < h_2 < 2 h_1$. The segment $h + t (-4, -7)$, $t \ge 0$, meets the line of slope 2 when $h_2 - 7t = 2(h_1 - 4t)$, that is $t = 2 h_1 - h_2 > 0$, and the line of slope 0 when $t = h_2 / 7$. So the program with scaling of $H$ starts with the flip when $2 h_1 - h_2 < h_2 / 7$, that is $h_2 > \frac74 h_1$, and with the Mori fibre space when $h_2 < \frac74 h_1$. The threshold is the slope $\frac74$ of $-K$ itself, as it must be, since for $H = -K$ the segment runs through the origin.

### Lean

The toric program is statement S39, stated in the library mmp-lean as a `def` with no proof:

Node: MMAWP4SA44 · Lean: `MinimalModel.ToricMMP`

It says that each toric $D$-program from a complete simplicial projective fan terminates and ends with a nef divisor or a Mori fibre space. The library has a proof of the wall relation for smooth adjacent cones:

Node: MMFAWNT87R · Lean: `MinimalModel.Toric.Fan.exists_unique_wall_relation`

It applies to the smooth walls of $X_2$, but not to the walls of $X_0$ and $X_1$ through singular cones. The example of this section, its fans, its walls and its count, is not in Lean on 2026-11-28.

### Notes and history

The method is that of Volume 3: the secondary fan and the walk through chambers (Chapter 3.7 and FS04), the toric flip (Rei83; Theorem 3.5.20), the discrepancy formula on a simplicial cone (CLS11, Chapter 11), and the toric negativity lemma (Corollary 3.6.2; KM98, Lemma 3.38). Termination of all toric flips is Theorem 3.6.3 (FS04, Theorem 4.9). Since $X_0$ is terminal of dimension 4, termination of its flips also follows from KMM87; the point of the example is that both the list of programs and the drop of the count can be checked by hand.

The data of the proposition were also checked by a short computer search before this section was written: the two relations, the cones of the three fans and their indices, the singular 3-dimensional faces, and the lattice points with $\psi < 2$, searched over the box $[-6, 6]^4$, which contains all such points since each $|v_i|_\infty \le 3$. The script is not part of the handbook. Its output agreed with each number above.

**Questions for a reader.**

- Which toric 4-folds of Picard number 2 have a $K$-program with three flips, and what is the smallest $d(X_0)$ among them?
- Can a sequence of toric 4-fold flips keep $d$ constant at a positive value for one step, and then drop?
