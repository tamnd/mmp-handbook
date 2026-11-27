---
title: The cone of curves of a del Pezzo surface
nodes: []
sources: [KM98, Mat02, Har77, Rei97]
reads_with: [KM98:ch1, Har77:V.4, Rei97:ch2]
requires: [P5.5, P5.6, P5.9, P5.10, P5.12]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The cone of curves of a del Pezzo surface

### Statement

In this chapter $k$ is an algebraically closed field of characteristic $0$, and a surface is a smooth projective surface over $k$. For a surface $S$, $NE(S) \subseteq N^1(S)$ is the cone of effective $1$-cycles, $\overline{NE}(S)$ its closure, and $\operatorname{Nef}(S)$ the nef cone, as in Chapter P5.12. A *del Pezzo surface* is a surface with $-K_S$ ample, and its *degree* is $K_S^2$ (Definition P5.9.24).

**Definition 2.2.1 (the surfaces $S_r$).** Let $0 \leq r \leq 8$ and let $p_1, \dots, p_r \in \mathbb{P}^2$ be points in general position in the sense of Definition P5.9.24. Write $S_r = \operatorname{Bl}_{p_1, \dots, p_r} \mathbb{P}^2$, with $S_0 = \mathbb{P}^2$, let $\ell$ be the pullback of a line and $E_1, \dots, E_r$ the exceptional curves. Then $\operatorname{Num}(S_r) = I^{1,r} = \mathbb{Z}\ell \oplus \mathbb{Z}E_1 \oplus \dots \oplus \mathbb{Z}E_r$ with $\ell^2 = 1$, $E_i^2 = -1$, the other products $0$, and $K = -3\ell + E_1 + \dots + E_r$ (Example P5.6.8). A class $a\ell - \sum_i b_i E_i$ is written $(a; b_1, \dots, b_r)$ when convenient. Let $N_r$ be the number of $(-1)$-curves on $S_r$.

By Theorem P5.9.26, $S_r$ is a del Pezzo surface of degree $9 - r$, its $(-1)$-curves are the integral curves whose classes are the exceptional classes $D^2 = K \cdot D = -1$, and $N_1, \dots, N_8 = 1, 3, 6, 10, 16, 27, 56, 240$. By Theorem P5.9.27 every del Pezzo surface is $\mathbb{P}^2$, $\mathbb{P}^1 \times \mathbb{P}^1$ or some $S_r$. This section reads these facts through the cone theorem.

**Theorem 2.2.2 (the cone of a del Pezzo surface).** Let $S$ be a del Pezzo surface.

1. $NE(S) = \overline{NE}(S)$, the cone is rational polyhedral, and every extremal ray of it is $K$-negative.
2. If $\rho(S) \geq 3$, then $S$ has finitely many $(-1)$-curves $C_1, \dots, C_N$, each spans an extremal ray, these are all the extremal rays, and $NE(S) = \sum_{i=1}^N \mathbb{R}_{\geq 0} [C_i]$. For $S = S_r$ with $2 \leq r \leq 8$ the number of extremal rays is $N_r = 3, 6, 10, 16, 27, 56, 240$.
3. If $\rho(S) \leq 2$, then $S$ is $\mathbb{P}^2$, with the single ray $\mathbb{R}_{\geq 0} \ell$; or $S_1 = F_1$, with the two rays spanned by $E_1$ and by the class $\ell - E_1$ of a fibre; or $\mathbb{P}^1 \times \mathbb{P}^1$, with the two rays of the two rulings.

Lean: not yet in Lean.

**Corollary 2.2.3 (the nef and ample cones).** Let $S$ be a del Pezzo surface with $\rho(S) \geq 3$ and $(-1)$-curves $C_1, \dots, C_N$. Then
$$\operatorname{Nef}(S) = \{ x \in N^1(S) : x \cdot C_i \geq 0 \text{ for } i = 1, \dots, N \}, \qquad \operatorname{Amp}(S) = \{ x : x \cdot C_i > 0 \text{ for all } i \}.$$
So $\operatorname{Nef}(S)$ is a rational polyhedral cone with at most $N$ facets, a divisor is nef if and only if it has nonnegative degree on every $(-1)$-curve, and it is ample if and only if it has positive degree on every $(-1)$-curve.

Lean: not yet in Lean.

### Proof in words

The cone theorem writes $\overline{NE}(S)$ as the $K$-nonnegative part plus the $K$-negative extremal rays. When $-K$ is ample, the $K$-nonnegative part is $0$, since an ample class is positive on the closed cone minus the origin. Taking $H = -K$ and $\varepsilon = \frac12$ in the finiteness statement of the cone theorem, every $K$-negative ray $R_i$ has $(K + \frac12 H) \cdot C_i = \frac12 K \cdot C_i < 0$, so there are finitely many rays. The three types of extremal contractions then decide what the rays are. A ray of square $0$ or of positive square forces $\rho \leq 2$, so for $\rho \geq 3$ every ray is spanned by a $(-1)$-curve. Conversely every $(-1)$-curve spans an extremal ray, as every curve of negative square does. The finitely many generators are classes of curves, so the closed cone equals the cone of curves.

### Examples

**Example 2.2.4 (degrees $9$ and $8$).** On $\mathbb{P}^2$, $NE = \mathbb{R}_{\geq 0}\ell$ and the single ray is of type 3 (Example P5.12.18). On $F_1 = S_1$, the cone is spanned by $E_1$, of type 1, and $\ell - E_1$, of type 2 (Example P5.12.7). On $\mathbb{P}^1 \times \mathbb{P}^1$ both rays are of type 2 (Example P5.12.8). In each case the cone and the nef cone are polyhedral, as Theorem 2.2.2 says, and $-K$ is positive on the generators: $-K \cdot \ell = 3$; $-K \cdot E_1 = 1$ and $-K \cdot (\ell - E_1) = 2$; $-K \cdot F_i = 2$. The ray spanned by $\ell - E_1$ on $S_1$ is a ray of square $0$, which is possible only because $\rho(S_1) = 2$.

**Example 2.2.5 (the plane blown up at three points: a triangular prism).** Let $S = S_3$, with $\rho = 4$. Its six $(-1)$-curves are $E_1, E_2, E_3$ and $L_{ij} = \ell - E_i - E_j$ (Theorem P5.9.26), so $NE(S)$ is a cone over a polytope with six vertices in the $3$-dimensional slice $-K \cdot x = 1$. The intersection numbers are $E_i \cdot E_j = 0$ and $L_{ij} \cdot L_{ik} = 1 - 1 = 0$ for distinct indices, $E_i \cdot L_{ij} = 1$ and $E_i \cdot L_{jk} = 0$ for $\{i, j, k\} = \{1, 2, 3\}$. So the six curves form a hexagon $E_1, L_{12}, E_2, L_{23}, E_3, L_{13}$ of meeting pairs, and there are $15 - 6 = 9$ disjoint pairs. By Corollary 2.2.3 a class $x = (a; b_1, b_2, b_3)$ is nef if and only if $b_i \geq 0$ and $a \geq b_i + b_j$ for $i \neq j$. A direct computation shows that the nef cone has the five rays
$$\ell = (1; 0, 0, 0), \qquad \ell - E_i = (1; 1, 0, 0) \text{ and its permutations}, \qquad 2\ell - E_1 - E_2 - E_3 = (2; 1, 1, 1).$$
For example $\ell - E_1$ is nef, since $(\ell - E_1) \cdot E_1 = 1$, $(\ell - E_1) \cdot E_j = 0$ for $j \neq 1$, $(\ell - E_1) \cdot L_{1j} = 0$ and $(\ell - E_1) \cdot L_{23} = 1$, and it vanishes on the four curves $E_2, E_3, L_{12}, L_{13}$, which span a $3$-dimensional face because the matrix of their classes has rank $3$. By the duality of Theorem P5.12.6 (3), the facets of $NE(S)$ are the orthogonal complements of these five rays. The facet $\ell^\perp$ contains $E_1, E_2, E_3$; the facet $(2\ell - \sum E_i)^\perp$ contains $L_{12}, L_{13}, L_{23}$, since $2 - 1 - 1 = 0$; and the facet $(\ell - E_i)^\perp$ contains the four curves $E_j, E_k, L_{ij}, L_{ik}$. So the slice of $NE(S)$ is a triangular prism, with two triangles and three quadrilaterals. Its nine edges are $E_iE_j$, $L_{ij}L_{ik}$ and $E_iL_{jk}$, which are exactly the nine disjoint pairs. The facet $(\ell - E_1)^\perp$ is the face of the conic bundle $|\ell - E_1|$, whose two reducible fibres are $L_{12} + E_2$ and $L_{13} + E_3$.

**Example 2.2.6 (three collinear points: a $K$-trivial ray).** Let $p_1, p_2, p_3$ lie on a line $M$ and $S = \operatorname{Bl}_{p_1, p_2, p_3} \mathbb{P}^2$. By Example P5.9.33 the strict transform $\tilde M = \ell - E_1 - E_2 - E_3$ is a $(-2)$-curve with $K \cdot \tilde M = 0$, so $S$ is not del Pezzo. By Lemma P5.12.11 the ray $\mathbb{R}_{\geq 0}[\tilde M]$ is extremal, and it is $K$-trivial, so it is not one of the rays of the cone theorem, and Theorem 2.2.2 does not apply. The curves $L_{ij}$ of Example 2.2.5 are now reducible: the line through $p_1$ and $p_2$ is $M$, so the class $\ell - E_1 - E_2 = \tilde M + E_3$ is no longer the class of a $(-1)$-curve, and the $(-1)$-curves of $S$ are $E_1, E_2, E_3$ only, each meeting $\tilde M$ once. The class $\tilde M$ is a root in the sense of Section 2, $\tilde M^2 = -2$ and $\tilde M \cdot K = 0$, and on a del Pezzo surface no root is effective, because $-K$ is positive on every nonzero effective class.

### Proof

*Theorem 2.2.2.* Let $H = -K$, which is ample. By Lemma P5.12.2 (2), $K \cdot y = -H \cdot y < 0$ for every $y \in \overline{NE}(S) \setminus \{0\}$, so $\overline{NE}(S)_{K \geq 0} = \{0\}$ and every extremal ray is $K$-negative. Let $\{R_i\}_{i \in I}$ be the $K$-negative extremal rays, spanned by rational curves $C_i$ as in Theorem P5.12.14 (1). Apply Theorem P5.12.14 (2) with $\varepsilon = \frac12$. Since $(K + \frac12 H) \cdot C_i = \frac12 K \cdot C_i < 0$ for every $i$, the set $I$ is finite, and
$$\overline{NE}(S) = \overline{NE}(S)_{\frac12 K \geq 0} + \sum_{i \in I} \mathbb{R}_{\geq 0}[C_i] = \sum_{i \in I} \mathbb{R}_{\geq 0}[C_i],$$
because $\overline{NE}(S)_{\frac12 K \geq 0} = \overline{NE}(S)_{K \geq 0} = \{0\}$. The right side is a finite sum of rays spanned by classes of curves, so it is contained in $NE(S)$, and $NE(S) \subseteq \overline{NE}(S)$ gives equality. The generators are integral classes, so the cone is rational polyhedral. This proves (1).

(2) Let $\rho(S) \geq 3$. By Theorem P5.12.15 each $R_i$ is of type 1, 2 or 3, and types 2 and 3 require $\rho(S) = 2$ and $\rho(S) = 1$. So each $R_i$ is of type 1, spanned by a $(-1)$-curve, which is the only integral curve with class in $R_i$. Conversely let $C$ be a $(-1)$-curve. By Lemma P5.12.11, $\mathbb{R}_{\geq 0}[C]$ is an extremal ray, and it is $K$-negative since $K \cdot C = -1$, so it is some $R_i$, and $C = C_i$. Hence the $(-1)$-curves are in bijection with the extremal rays, there are finitely many of them, and they generate $NE(S)$ by (1). For $S = S_r$ the number of rays is $N_r$, and the values are those of Theorem P5.9.26 (2), recomputed from the root systems in Corollary 2.2.10 below.

(3) By Theorem P5.9.27 a del Pezzo surface with $\rho \leq 2$ is $\mathbb{P}^2$, $\mathbb{P}^1 \times \mathbb{P}^1$ or $S_1$, since $\rho(S_r) = r + 1$. The cones are computed in Examples P5.12.18, P5.12.8 and P5.12.7. $\square$

*Corollary 2.2.3.* By Theorem P5.12.6 (3) and its proof, $\operatorname{Nef}(S)$ is the dual of $\overline{NE}(S)$, so a class $x$ is nef if and only if $x \cdot y \geq 0$ for every $y \in \overline{NE}(S)$. By Theorem 2.2.2 (2), $\overline{NE}(S)$ is generated by the $[C_i]$, and $x \cdot y \geq 0$ for all $y$ if and only if $x \cdot C_i \geq 0$ for all $i$. This is the first equality, and it shows that $\operatorname{Nef}(S)$ is cut out by $N$ rational linear inequalities, so it is rational polyhedral with at most $N$ facets. By Theorem P5.12.6 (1), $x$ is ample if and only if $x \cdot y > 0$ for every $y \in \overline{NE}(S) \setminus \{0\}$. Such a $y$ is $\sum_i c_i [C_i]$ with $c_i \geq 0$ not all $0$, so $x \cdot y > 0$ for all such $y$ if and only if $x \cdot C_i > 0$ for all $i$. $\square$

### Exercises

1. (A) On $S_2$, show that the nef cone has the three rays $\ell$, $\ell - E_1$ and $\ell - E_2$, and that each of them is the class of the pullback of a morphism: $S_2 \to \mathbb{P}^2$, and the two conic bundles $S_2 \to \mathbb{P}^1$.
2. (A) On $S_3$, write $-K$ as $(\ell - E_1) + (\ell - E_2) + (\ell - E_3)$ and as $\ell + (2\ell - E_1 - E_2 - E_3)$, sums of nef classes of Example 2.2.5. Check that $-K \cdot C = 1$ for each of the six $(-1)$-curves, and conclude from Corollary 2.2.3 that $-K$ lies in the interior of $\operatorname{Nef}(S_3)$.
3. (B) On $S_4$, list the ten $(-1)$-curves and show that $D = 2\ell - E_1 - E_2 - E_3 - E_4$ is nef, with $D^2 = 0$, and not ample. Show that the $(-1)$-curves orthogonal to $D$ are the six curves $L_{ij}$, and that $|D|$ is the pencil of conics through the four points, a conic bundle $S_4 \to \mathbb{P}^1$ with the three reducible fibres $L_{12} + L_{34}$, $L_{13} + L_{24}$ and $L_{14} + L_{23}$.
4. (B) Let $S$ be a del Pezzo surface with $\rho(S) \geq 3$, $C$ a $(-1)$-curve and $\pi \colon S \to S'$ its contraction. Show that the $(-1)$-curves of $S'$ are exactly the images of the $(-1)$-curves of $S$ disjoint from $C$. Use Proposition P5.9.25 (1) to rule out a $(-1)$-curve of $S'$ through the point $\pi(C)$. Check the resulting equality $N_{r-1} = \#\{D : D \cdot E_r = 0, D \neq E_r\}$ on $S_3$, where the curves disjoint from $E_3$ are $E_1$, $E_2$ and $L_{12}$.
5. (B) Let $S$ be a del Pezzo surface of degree $d$ and $C$ an integral curve. Show that $-K \cdot C \leq 3$ if $C$ spans an extremal ray, and that equality holds only for $S = \mathbb{P}^2$.
6. (C) Let $S$ be the blow-up of $\mathbb{P}^2$ at three points on a line $M$, as in Example 2.2.6. Show that $NE(S)$ is the simplicial cone spanned by $E_1, E_2, E_3$ and $\tilde M$, by writing the class $(a; b_1, b_2, b_3)$ of any other integral curve as $a \tilde M + \sum_i (a - b_i) E_i$. Show that $\operatorname{Nef}(S)$ is spanned by $\ell$ and $\ell - E_i$, and that $-K$ is nef and not ample.

### Lean

Nothing of this section is in Lean. The project library has no cone of curves of a surface and no del Pezzo surfaces.

### Notes and history

Del Pezzo described the surfaces of degree $d$ in $\mathbb{P}^d$ in 1887, and the description of their lines by exceptional classes is due to Manin, Cubic forms, Chapter IV, and Demazure, Surfaces de del Pezzo, Séminaire sur les singularités des surfaces, 1980. The point of view of this section, that the cone of curves of a Fano variety is rational polyhedral, comes from Mori's cone theorem (Mor82, KM98, Theorem 3.7) and holds in every dimension for Fano varieties with klt singularities. For surfaces the proof only needs Chapter P5.12. Reid, Chapters on algebraic surfaces, Rei97, presents the del Pezzo cones in this way.
