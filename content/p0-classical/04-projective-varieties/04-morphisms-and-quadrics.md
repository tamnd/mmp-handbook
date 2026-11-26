---
title: Veronese and Segre embeddings, projections and quadrics
nodes: []
sources: [Har92, Har77, Rei88, Sha13]
reads_with: [Har92:lecture2, Har77:I.3, Rei88:ch1, Sha13:ch1]
requires: [P0.3, P0.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Veronese and Segre embeddings, projections and quadrics

### Statement

**Definition P0.4.28 (morphism of projective algebraic sets).** Let $X \subseteq \mathbb{P}^n$ and $Y \subseteq \mathbb{P}^m$ be projective algebraic sets. A map $\varphi \colon X \to Y$ is a morphism if each point of $X$ has an open neighbourhood $U \subseteq X$ and homogeneous polynomials $F_0, \dots, F_m$ of one degree with no common zero on $U$, such that $\varphi(p) = [F_0(p) : \dots : F_m(p)]$ for $p \in U$. An isomorphism is a morphism with an inverse morphism. A closed embedding is a morphism that is an isomorphism onto a closed subset.

Lean: not in Lean as stated; the scheme version is a morphism of schemes over $k$ between closed subschemes of `AlgebraicGeometry.Proj`.

**Example P0.4.29.** A projective transformation $[v] \mapsto [Av]$ is an isomorphism $\mathbb{P}^n \to \mathbb{P}^n$, with one formula on all of $\mathbb{P}^n$. The map $\mathbb{P}^1 \to \mathbb{P}^2$, $[s : t] \mapsto [s^2 : st : t^2]$, is a morphism, because $s^2$ and $t^2$ have no common zero.

**Example P0.4.30.** On the conic $C = V(x_0 x_2 - x_1^2)$ the map $C \to \mathbb{P}^1$ given by $[x_0 : x_1]$ on $C \setminus \{[0 : 0 : 1]\}$ and by $[x_1 : x_2]$ on $C \setminus \{[1 : 0 : 0]\}$ is a morphism. The two formulas agree where both are defined, because $x_0 x_2 = x_1^2$ on $C$. No single pair of linear forms defines it at every point.

A morphism is continuous. On $U$ as above, the preimage of $V(G)$ is $U \cap V(G(F_0, \dots, F_m))$, where $G(F_0, \dots, F_m)$ is homogeneous.

**Theorem P0.4.31 (Veronese embedding).** Let $d \geq 1$ and $N = \binom{n+d}{d} - 1$. Index the coordinates $z_I$ of $\mathbb{P}^N$ by the multi-indices $I = (I_0, \dots, I_n)$ with $I_j \geq 0$ and $\sum_j I_j = d$, and write $x^I = x_0^{I_0} \cdots x_n^{I_n}$. The Veronese map

$$v_d \colon \mathbb{P}^n \to \mathbb{P}^N, \qquad [x] \mapsto [x^I]_I$$

is a closed embedding. Its image is $Z = V(z_I z_J - z_K z_L : I + J = K + L)$.

Lean: not in Lean as stated.

*Proof.* The monomials $x_i^d$ have no common zero, so $v_d$ is a morphism. Its image lies in $Z$, because $x^I x^J = x^{I+J} = x^K x^L$. Let $e_i$ be the multi-index with $1$ in place $i$.

Step 1: every $z \in Z$ has some $z_{de_i} \neq 0$. Among the $I$ with $z_I \neq 0$, choose one with the largest entry $I_i = m$. If $m < d$, there is $j \neq i$ with $I_j \geq 1$. The relation $2I = (I + e_i - e_j) + (I - e_i + e_j)$ gives $z_I^2 = z_{I + e_i - e_j}\, z_{I - e_i + e_j}$, so $z_{I + e_i - e_j} \neq 0$. Its $i$-th entry is $m + 1$, a contradiction. So $m = d$ and $z_{de_i} \neq 0$.

Step 2: inverse on $Z_i = Z \cap \{z_{de_i} \neq 0\}$. Take $i = 0$, the other cases are the same. Define $\psi_0 \colon Z_0 \to \mathbb{P}^n$ by $\psi_0(z) = [z_{de_0} : z_{(d-1)e_0 + e_1} : \dots : z_{(d-1)e_0 + e_n}]$, a morphism, since the first entry is $z_{de_0} \neq 0$. Then $\psi_0(v_d[x]) = [x_0^{d-1} x_0 : \dots : x_0^{d-1} x_n] = [x]$ when $x_0 \neq 0$. Conversely let $z \in Z_0$, scaled so that $z_{de_0} = 1$, and let $a = (1, a_1, \dots, a_n)$ with $a_j = z_{(d-1)e_0 + e_j}$. Then $z_J = a^J$ for all $J$, by induction on $d - J_0$. The cases $d - J_0 \leq 1$ hold by definition. If $d - J_0 \geq 2$, choose $j \neq 0$ with $J_j \geq 1$. The relation $J + de_0 = (J - e_j + e_0) + ((d-1)e_0 + e_j)$ gives $z_J = z_{J - e_j + e_0}\, a_j = a^{J - e_j + e_0} a_j = a^J$. So $z = v_d(\psi_0(z))$.

By Step 1 the open sets $Z_i$ cover $Z$, and on each $Z_i$ the morphism $\psi_i$ is inverse to $v_d$. Two inverses agree on overlaps, so the $\psi_i$ glue to a morphism $Z \to \mathbb{P}^n$ inverse to $v_d$. $\square$

**Theorem P0.4.32 (Segre embedding).** Let $N = (n+1)(m+1) - 1$, with coordinates $z_{ij}$ of $\mathbb{P}^N$ for $0 \leq i \leq n$, $0 \leq j \leq m$. The Segre map

$$\sigma \colon \mathbb{P}^n \times \mathbb{P}^m \to \mathbb{P}^N, \qquad ([x], [y]) \mapsto [x_i y_j]_{i,j}$$

is well defined and injective. Its image is the closed set $\Sigma = V(z_{ij} z_{kl} - z_{il} z_{kj})$ of matrices of rank $1$. On $\Sigma \cap \{z_{ij} \neq 0\}$ the inverse is the morphism $z \mapsto ([z_{0j} : \dots : z_{nj}], [z_{i0} : \dots : z_{im}])$.

Lean: not in Lean as stated.

*Proof.* The matrix $(x_i y_j) = x y^{\mathsf{T}}$ is nonzero and does not change in $\mathbb{P}^N$ when $x$ or $y$ is scaled. It has rank $1$, so its $2 \times 2$ minors vanish, and $\sigma$ maps into $\Sigma$. A nonzero matrix $z$ with all $2 \times 2$ minors zero has rank $1$, so $z = x y^{\mathsf{T}}$ for nonzero $x$ and $y$. Its column $j$ is $y_j x$ and its row $i$ is $x_i y^{\mathsf{T}}$. When $z_{ij} = x_i y_j \neq 0$, column $j$ gives $[x]$ and row $i$ gives $[y]$. So $\sigma$ is a bijection onto $\Sigma$ with the stated inverse. $\square$

This handbook gives $\mathbb{P}^n \times \mathbb{P}^m$ the structure of the projective algebraic set $\Sigma$. Its Zariski topology is not the product topology, as in the affine case.

**Definition P0.4.33 (projection from a point).** Let $p \in \mathbb{P}^n$ and let $H \cong \mathbb{P}^{n-1}$ be a hyperplane with $p \notin H$. The projection from $p$ to $H$ sends $q \neq p$ to the point where the line through $p$ and $q$ meets $H$. In coordinates with $p = [0 : \dots : 0 : 1]$ and $H = V(x_n)$, it is the morphism

$$\pi_p \colon \mathbb{P}^n \setminus \{p\} \to \mathbb{P}^{n-1}, \qquad [x_0 : \dots : x_n] \mapsto [x_0 : \dots : x_{n-1}].$$

Lean: not in Lean as stated.

**Example P0.4.34.** For a projective algebraic set $X$ with $p \notin X$, the restriction $\pi_p \colon X \to \mathbb{P}^{n-1}$ is a morphism. Its fibres are the sets $X \cap L$ for the lines $L$ through $p$. Projecting the twisted cubic $[s^3 : s^2 t : s t^2 : t^3]$ from $[0 : 1 : 0 : 0]$, which is not on the curve, gives the plane curve $[s^3 : s t^2 : t^3]$, the cuspidal cubic $x_0 x_2^2 = x_1^3$.

**Example P0.4.35.** Projecting the conic $C = V(x_0 x_2 - x_1^2)$ from its own point $p = [0 : 0 : 1]$ gives $[x_0 : x_1]$ on $C \setminus \{p\}$. This extends to a morphism on all of $C$, as in the second example of a morphism above. It is the isomorphism $C \cong \mathbb{P}^1$, with inverse $v_2 \colon [s : t] \mapsto [s^2 : st : t^2]$.

**Theorem P0.4.36 (classification of quadrics).** Let $\mathrm{char}\, k \neq 2$ and let $Q \neq 0$ be a quadratic form in $x_0, \dots, x_n$, with symmetric matrix $A$, so $Q(x) = x^{\mathsf{T}} A x$. Let $r + 1$ be the rank of $A$. Then there is a projective transformation after which

$$Q = x_0^2 + x_1^2 + \dots + x_r^2.$$

The rank does not depend on the coordinates. So, up to projective transformation and nonzero scalars, there are exactly $n + 1$ nonzero quadratic forms in $x_0, \dots, x_n$, one for each rank $r + 1 = 1, \dots, n + 1$. A quadric is nondegenerate if its rank is $n + 1$.

Lean: Mathlib `QuadraticForm.equivalent_weightedSumSquares_of_isAlgClosed` (proved in Mathlib, for nondegenerate forms over an algebraically closed field with 2 invertible; the degenerate case is not in Lean as stated).

*Proof.* Let $B(u, v) = u^{\mathsf{T}} A v$, so $Q(v) = B(v, v)$ and $B(u, v) = \frac{1}{2}(Q(u + v) - Q(u) - Q(v))$. Induction on $n$. If $Q(v) = 0$ for all $v$, then $B = 0$ and $Q = 0$. Otherwise choose $v_0$ with $Q(v_0) \neq 0$ and scale it by a square root of $Q(v_0)^{-1}$, which exists in $k$, so that $Q(v_0) = 1$. The space $W = \{u : B(u, v_0) = 0\}$ has dimension $n$, and $k^{n+1} = k v_0 \oplus W$. Apply induction to $Q|_W$ to get a basis $v_1, \dots, v_n$ of $W$ with $Q(\sum_{i \geq 1} c_i v_i) = c_1^2 + \dots + c_s^2$ for some $s$. In the basis $v_0, \dots, v_n$ the form is $c_0^2 + \dots + c_s^2$. A change of basis replaces $A$ by $P^{\mathsf{T}} A P$ with $P$ invertible, and this does not change the rank. So $s = r$. $\square$

**Corollary P0.4.37 (conics and quadric surfaces).** Let $\mathrm{char}\, k \neq 2$.

1. A nondegenerate conic in $\mathbb{P}^2$ is isomorphic to $\mathbb{P}^1$, by a projective transformation to $V(x_0 x_2 - x_1^2)$ and the inverse of $v_2$. A conic of rank 2 is a pair of distinct lines, and a conic of rank 1 is a line (a double line).
2. A nondegenerate quadric surface in $\mathbb{P}^3$ is isomorphic to $\mathbb{P}^1 \times \mathbb{P}^1$, by a projective transformation to $V(z_{00} z_{11} - z_{01} z_{10})$ and the inverse of the Segre map. It contains two families of lines, the images of $\{a\} \times \mathbb{P}^1$ and $\mathbb{P}^1 \times \{b\}$. Two lines of one family are disjoint, and two lines of different families meet in one point.

Lean: not in Lean as stated.

*Proof.* The form $x_0 x_2 - x_1^2$ has rank $3$ and $z_{00} z_{11} - z_{01} z_{10}$ has rank $4$: in each case the symmetric matrix has nonzero determinant. By the theorem every nondegenerate quadric is a projective transformation away from these forms. For $n = 2$, $V(x_0 x_2 - x_1^2)$ is the image $Z$ of $v_2 \colon \mathbb{P}^1 \to \mathbb{P}^2$: the relations of the Veronese theorem reduce to $z_{(2,0)} z_{(0,2)} = z_{(1,1)}^2$. For $n = 3$, the Segre image $\Sigma$ for $\mathbb{P}^1 \times \mathbb{P}^1$ has the single equation $z_{00} z_{11} - z_{01} z_{10}$. A rank 2 form is $x_0^2 + x_1^2 = (x_0 + i x_1)(x_0 - i x_1)$ with $i^2 = -1$, a product of two independent linear forms, and a rank 1 form is $x_0^2$. For the lines, $\sigma(\{a\} \times \mathbb{P}^1)$ is the image of $\mathbb{P}^1$ under the injective linear map $b \mapsto a b^{\mathsf{T}}$, so it is a line in $\mathbb{P}^3$, and the same holds for $\sigma(\mathbb{P}^1 \times \{b\})$. Two such lines for $a \neq a'$ are disjoint, because $\sigma$ is injective, and $\sigma(\{a\} \times \mathbb{P}^1)$ meets $\sigma(\mathbb{P}^1 \times \{b\})$ in $\sigma(a, b)$ alone. $\square$

### Proof in words

The Veronese map lists all monomials of degree $d$, and the Segre map lists all products $x_i y_j$. In both cases the equations of the image say that the coordinates multiply like monomials, and the inverse map is read off from a few coordinates where one of them is nonzero. Projection from a point forgets one coordinate. Quadrics reduce to linear algebra: over an algebraically closed field of characteristic not 2, a symmetric bilinear form is a sum of squares, and only the rank remains. The two nondegenerate quadrics of small dimension are images of the two embeddings.

### Examples

The rational normal curve of degree $d$ is $v_d(\mathbb{P}^1) \subset \mathbb{P}^d$, the image of $[s : t] \mapsto [s^d : s^{d-1} t : \dots : t^d]$. For $d = 2$ it is a conic, and for $d = 3$ it is the twisted cubic of Section 3. The Veronese surface $v_2(\mathbb{P}^2) \subset \mathbb{P}^5$ is the set of symmetric $3 \times 3$ matrices of rank 1, $[x] \mapsto x x^{\mathsf{T}}$.

The Veronese map turns hypersurfaces into hyperplane sections. A form $F = \sum_I c_I x^I$ of degree $d$ is the linear form $\sum_I c_I z_I$ composed with $v_d$, so $v_d(V(F)) = Z \cap V(\sum_I c_I z_I)$. For example, the conics in $\mathbb{P}^2$ through a point form a hyperplane in the $\mathbb{P}^5$ of all conics, and five general points fix one conic.

In characteristic 2 the theorem fails as stated. Over $k$ of characteristic 2 the form $x_0 x_1 + x_2^2$ is not a sum of squares, because a sum of squares $\sum (\sum_j a_{ij} x_j)^2 = (\sum_{i,j} a_{ij} x_j)^2$ is the square of a linear form.

### Exercises

1. (A) Write the equations of the twisted cubic $v_3(\mathbb{P}^1) \subset \mathbb{P}^3$ from the Veronese theorem, and check that they are the three minors of Section 3.
2. (A) Show that the projection of the twisted cubic from the point $[1 : 0 : 0 : 1]$, which is not on the curve, is a plane cubic with a node.
3. (A) Show that the Segre image of $\mathbb{P}^1 \times \mathbb{P}^2$ lies in $\mathbb{P}^5$, and that it is cut out by three quadrics.
4. (B) Show that a nondegenerate conic in $\mathbb{P}^2$ and a line not tangent to it meet in exactly two points, and that through five points of $\mathbb{P}^2$, no three on a line, there is exactly one conic.
5. (B) Show that a nondegenerate quadric surface in $\mathbb{P}^3$ contains no lines other than those of the two families. (Hint: a line in $\Sigma$ is a line of rank 1 matrices; show that all its matrices share a row space or a column space.)
6. (B) Let $X \subseteq \mathbb{P}^n$ be a projective algebraic set and $F$ homogeneous of degree $d \geq 1$. Show that $X \setminus V(F)$ is isomorphic to a closed subset of an affine chart of $\mathbb{P}^N$, using $v_d$. Deduce that $X \setminus V(F)$ is affine.

### Lean

Mathlib has the diagonalization of quadratic forms: `QuadraticForm.equivalent_weightedSumSquares` over any field with 2 invertible, and `QuadraticForm.equivalent_weightedSumSquares_of_isAlgClosed` and `QuadraticForm.equivalent_of_isAlgClosed` for nondegenerate forms over an algebraically closed field. It has no Veronese or Segre embedding and no projection from a point in the classical form. The handbook uses these Mathlib names and adds no `MinimalModel` node here.

### Notes and history

Veronese studied the surface $v_2(\mathbb{P}^2) \subset \mathbb{P}^5$ in 1882, and Segre introduced the product embedding in 1891. The diagonalization of quadratic forms goes back to Lagrange and Sylvester's law of inertia (1852) over the reals. The literature state is theorem. In the minimal model program these maps reappear in three ways. The Veronese embedding shows that $\mathcal{O}(d)$ is very ample on $\mathbb{P}^n$ for every $d \geq 1$. The Segre embedding makes products of projective varieties projective. The quadric surface $\mathbb{P}^1 \times \mathbb{P}^1$ is the simplest variety with two extremal rays, one for each ruling, and later volumes use it as a first example of the cone theorem.
