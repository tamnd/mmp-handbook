---
title: Refinements, star subdivisions and smooth fans
nodes: []
sources: [CLS11, Ful93, Oda88]
reads_with: [CLS11:ch10, CLS11:ch11, Ful93:2.6, Oda88:1.6]
requires: [P8.8, 3.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Refinements, star subdivisions and smooth fans

### Statement

**Definition 3.1.28.** A fan $\Sigma'$ *refines* a fan $\Sigma$ in the same $N_{\mathbb{R}}$ if every cone of $\Sigma'$ lies in a cone of $\Sigma$ and $|\Sigma'| = |\Sigma|$. Let $v \in |\Sigma| \cap N$ be primitive. The *star subdivision* $\Sigma^*(v)$ of $\Sigma$ at $v$ is the set of the cones $\sigma \in \Sigma$ with $v \notin \sigma$, together with the cones $\operatorname{Cone}(\tau, v)$, where $\tau \in \Sigma$, $v \notin \tau$, and $\tau$ and $v$ lie in a common cone of $\Sigma$. It is a fan that refines $\Sigma$, and its rays are the rays of $\Sigma$ and the ray of $v$ (Cox-Little-Schenck, Chapters 3 and 11).

Lean: not yet in Lean.

**Theorem 3.1.29 (smooth refinements).** Let $\Sigma$ be a fan.

1. $\Sigma$ has a simplicial refinement with the same rays.
2. $\Sigma$ has a smooth refinement, obtained from a simplicial refinement by a finite sequence of star subdivisions. The smooth cones of $\Sigma$ stay cones of the refinement.

Lean: not yet in Lean.

**Proposition 3.1.30 (dimension 2).** Let $\sigma \subset \mathbb{R}^2$ be a cone of dimension 2, with $N = \mathbb{Z}^2$. Let $P$ be the convex hull of $\sigma \cap N \setminus \{0\}$, and let $v_0, v_1, \dots, v_{s+1}$ be the lattice points on the bounded edges of the boundary of $P$, in order from one ray of $\sigma$ to the other.

1. The cones $\operatorname{Cone}(v_i, v_{i+1})$ for $0 \le i \le s$, with their faces, form a smooth refinement of the fan of the faces of $\sigma$.
2. $\{v_0, \dots, v_{s+1}\}$ is the Hilbert basis of the semigroup $\sigma \cap N$, and every smooth refinement of $\sigma$ has a ray through each $v_i$.
3. For $1 \le i \le s$ there is an integer $b_i \ge 2$ with $v_{i-1} + v_{i+1} = b_i v_i$.

Lean: not yet in Lean.

So in dimension 2 a cone has a unique minimal smooth refinement. In Chapter 2 it gives the minimal resolution of a cyclic quotient singularity, and in Chapter 3 the numbers $b_i$ become the negatives of the self-intersections of the exceptional curves.

### Proof in words

A simplicial cone that is not smooth has a lattice point $v$ in the half-open box $\{\sum \lambda_\rho u_\rho : 0 \le \lambda_\rho < 1\}$ other than $0$, because the box is a set of coset representatives for $N_\sigma$ modulo the sublattice spanned by the $u_\rho$. The star subdivision at $v$ replaces $\sigma$ by cones whose multiplicities are $\lambda_\rho \operatorname{mult}(\sigma) < \operatorname{mult}(\sigma)$. Induction on the multiplicity ends the proof. The difficulty in all dimensions is to make the choices compatible on the common faces of different cones, which is why one subdivides at one vector at a time.

In dimension 2 there is a canonical choice. The boundary of the convex hull $P$ is a broken line from one ray to the other. Each triangle between $0$ and two consecutive lattice points on it has no other lattice points. By Pick's theorem its area is $\frac12$, so the two points form a basis. A smooth refinement must have a ray through each irreducible lattice point of $\sigma$, because a lattice point of a smooth cone is a nonnegative integer combination of its two generators.

### Examples

**Example 3.1.31 (the resolution of $\frac1n(1,1)$).** Let $\sigma = \operatorname{Cone}(e_2, n e_1 - e_2)$ with $n \ge 2$; this is the cone $\sigma_n$ of Example 3.1.6. A lattice point $(a, b)$ lies in $\sigma$ if and only if $a \ge 0$ and $a + nb \ge 0$. The bounded edges of $P$ are the segments from $e_2$ to $e_1$ and from $e_1$ to $(n, -1)$; neither segment has other lattice points. So $v_0 = e_2$, $v_1 = e_1$, $v_2 = n e_1 - e_2$, and $v_0 + v_2 = n v_1$, so $b_1 = n$. The smooth refinement has the two cones $\operatorname{Cone}(e_2, e_1)$ and $\operatorname{Cone}(e_1, n e_1 - e_2)$. It is the star subdivision of $\sigma$ at $e_1$. Chapter 2 shows that it is the minimal resolution of the cone over the rational normal curve, with one exceptional curve of self-intersection $-n$. For $n = 2$ it resolves the quadric cone.

**Example 3.1.32 (the cone of $\frac15(1,2)$).** Let $\sigma = \operatorname{Cone}(e_2, 5 e_1 - 2 e_2)$. A point $(a, b)$ lies in $\sigma$ if and only if $a \ge 0$ and $2a + 5b \ge 0$. The lattice points on the bounded part of the boundary of $P$ are

$$v_0 = (0, 1), \quad v_1 = (1, 0), \quad v_2 = (3, -1), \quad v_3 = (5, -2).$$

The points $v_1, v_2, v_3$ lie on one segment. Then $v_0 + v_2 = 3 v_1$ and $v_1 + v_3 = 2 v_2$, so $(b_1, b_2) = (3, 2)$. Each pair of consecutive points has determinant $-1$. The Hirzebruch-Jung continued fraction is $5/2 = 3 - 1/2$, as Exercise 3 predicts.

**Example 3.1.33 (two triangulations of a square).** Let $\sigma = \operatorname{Cone}(u_1, u_2, u_3, u_4)$ be the cone over a square of Example 3.1.7. Its two diagonals give two simplicial refinements with no new rays:

$$\Sigma_+ : \operatorname{Cone}(u_1, u_2, u_3), \ \operatorname{Cone}(u_1, u_3, u_4), \qquad \Sigma_- : \operatorname{Cone}(u_1, u_2, u_4), \ \operatorname{Cone}(u_2, u_3, u_4).$$

All four cones have determinant $1$, so both refinements are smooth. Neither refines the other. The star subdivision of $\sigma$ at $w = u_1 + u_3 = u_2 + u_4 = (1, 1, 2)$ gives four smooth cones $\operatorname{Cone}(u_i, u_{i+1}, w)$, and it refines both $\Sigma_+$ and $\Sigma_-$. Later in this volume, $\Sigma_+$ and $\Sigma_-$ are the two sides of the Atiyah flop, and the star subdivision is their common blow-up.

**Example 3.1.34 (uniqueness fails in dimension 3).** The proof of part 2 of Proposition 3.1.30 works in every dimension: a smooth refinement of $\sigma$ has a ray through each element of the Hilbert basis of $\sigma \cap N$. What fails in dimension 3 is uniqueness. For the cone over a square, the cones of $\Sigma_+$ are smooth and cover $\sigma$, so every lattice point of $\sigma$ is a nonnegative integer combination of $u_1, \dots, u_4$, and the Hilbert basis is $\{u_1, u_2, u_3, u_4\}$. Both $\Sigma_+$ and $\Sigma_-$ are smooth refinements with exactly these rays, and neither refines the other. So there is no smallest smooth refinement. A second example shows that new rays can be needed even for a simplicial cone. Let $N = \mathbb{Z}^3 + \mathbb{Z} \cdot \frac12(1,1,1)$ and $\sigma = \operatorname{Cone}(e_1, e_2, e_3)$. Then $\operatorname{mult}(\sigma) = 2$, and the only simplicial refinement with the same rays is $\sigma$ itself. The star subdivision at $w = \frac12(1,1,1)$ is smooth: $\{w, e_2, e_3\}$ is a basis of $N$, because $e_1 = 2w - e_2 - e_3$, and the same holds for the other two cones. This is the cone of the terminal singularity $\frac12(1,1,1)$, and Chapter 3 computes the discrepancy $\frac12$ of this star subdivision.

### Proof

*Proof of Proposition 3.1.30.* Since $\sigma$ is strongly convex of dimension 2, $0 \notin P$, and each bounded edge $[v_i, v_{i+1}]$ of $P$ has a form $\ell_i$ with $\ell_i(v_i) = \ell_i(v_{i+1}) = c_i > 0$ and $\ell_i \ge c_i$ on $P$. The rays of $\sigma$ contain $v_0$ and $v_{s+1}$, which are the minimal generators.

For part 1, let $T_i$ be the triangle with vertices $0$, $v_i$, $v_{i+1}$. On $T_i$, $\ell_i \le c_i$, with equality only on the edge $[v_i, v_{i+1}]$. A lattice point of $T_i$ other than $0$ lies in $P$, so it lies on this edge. The lattice points of the edge are consecutive points in the list, so they are $v_i$ and $v_{i+1}$. By Pick's theorem the area of $T_i$ is $0 + \frac32 - 1 = \frac12$, so $|\det(v_i, v_{i+1})| = 1$ and $\operatorname{Cone}(v_i, v_{i+1})$ is smooth. The cones $\operatorname{Cone}(v_i, v_{i+1})$ cover $\sigma$ and meet along the rays of the $v_i$, so they form a smooth refinement.

For part 2, each lattice point of $\sigma$ lies in some $\operatorname{Cone}(v_i, v_{i+1})$, and so it is a nonnegative integer combination of $v_i$ and $v_{i+1}$. So the $v_i$ generate $\sigma \cap N$. Each $v_i$ is irreducible: if $v_i = a + b$ with $a, b \in \sigma \cap N \setminus 0$, then $\frac12 v_i = \frac12 (a + b) \in P$, but $\ell(\frac12 v_i) = \frac12 c < c$ for the form $\ell$ of an edge through $v_i$. Proposition 3.1.12 then says that the $v_i$ form the Hilbert basis. Now let $\Sigma'$ be a smooth refinement, and let $\operatorname{Cone}(w, w')$ be a cone of $\Sigma'$ that contains $v_i$. Then $v_i = a w + b w'$ with $a, b \in \mathbb{Z}_{\ge 0}$, since $w, w'$ is a basis. Since $v_i$ is irreducible, $v_i = w$ or $v_i = w'$.

For part 3, both $(v_{i-1}, v_i)$ and $(v_i, v_{i+1})$ are bases with the same orientation, so $\det(v_{i-1}, v_i) = \det(v_i, v_{i+1}) = \pm 1$. Write $v_{i+1} = \alpha v_{i-1} + \beta v_i$ with $\alpha, \beta \in \mathbb{Z}$. Then $\det(v_i, v_{i+1}) = \alpha \det(v_i, v_{i-1})$, so $\alpha = -1$ and $v_{i-1} + v_{i+1} = \beta v_i$. Put $b_i = \beta$. The point $\frac12(v_{i-1} + v_{i+1}) = \frac{b_i}{2} v_i$ lies in $P$. A point $t v_i$ with $t < 1$ is not in $P$, by the form $\ell$ as above, so $b_i \ge 2$. $\square$

*Proof of Theorem 3.1.29.* This is cited from Cox-Little-Schenck, Chapter 11, and Fulton, Section 2.6. For part 1, one orders the rays and adds them one at a time in a pulling triangulation, so that no new ray appears. For part 2, the multiplicity of a simplicial cone $\sigma$ is the number of lattice points of the half-open box $\{\sum_{\rho \in \sigma(1)} \lambda_\rho u_\rho : 0 \le \lambda_\rho < 1\}$. If it is greater than 1, the box contains a lattice point $v = \sum \lambda_\rho u_\rho \neq 0$, and one may take $v$ primitive. In the star subdivision at $v$, the cone that replaces $u_\rho$ by $v$ has multiplicity $\lambda_\rho \operatorname{mult}(\sigma)$, which is smaller. The cones of $\Sigma$ that contain $v$ are subdivided too, and their multiplicities do not grow. An induction on the largest multiplicity and the number of cones of that multiplicity ends the proof. $\square$

### Exercises

1. (A) Find the minimal smooth refinement of $\operatorname{Cone}(e_2, 7 e_1 - 3 e_2)$ and the numbers $b_i$.
2. (A) Check that the four cones of $\Sigma_+$ and $\Sigma_-$ in Example 3.1.33, and the four cones of the star subdivision at $w$, are smooth.
3. (B) Let $\sigma = \operatorname{Cone}(e_2, n e_1 - q e_2)$ with $0 < q < n$ and $\gcd(n, q) = 1$, and let $b_1, \dots, b_s$ be the numbers of Proposition 3.1.30. Show that $n/q = b_1 - 1/(b_2 - 1/(\cdots - 1/b_s))$.
4. (B) Show that the star subdivision of the orthant $\operatorname{Cone}(e_1, \dots, e_n)$ at $e_1 + \dots + e_n$ is a smooth fan with $n$ maximal cones.
5. (B) Show that every simplicial refinement of the cone over a square with no new rays is $\Sigma_+$ or $\Sigma_-$.
6. (B) Let $\sigma = \operatorname{Cone}(u_1, \dots, u_k)$ be simplicial and $v = \sum \lambda_i u_i$ with $0 \le \lambda_i < 1$. Show that $\operatorname{mult}(\operatorname{Cone}(u_1, \dots, u_{i-1}, v, u_{i+1}, \dots, u_k)) = \lambda_i \operatorname{mult}(\sigma)$ when $\lambda_i > 0$.

### Lean

- Status: the Lean library proves that faces of simplicial cones are simplicial, `MinimalModel.Toric.IsSimplicial.of_isFaceOf`, and so that the fan of a simplicial cone is simplicial, `MinimalModel.Toric.Fan.isSimplicialFan_ofCone`. It proves that the zero cone, a ray and the orthant are simplicial (`MinimalModel.Toric.isSimplicial_bot`, `MinimalModel.Toric.isSimplicial_latticeCone_singleton`, `MinimalModel.Toric.isSimplicial_orthant`), and so that the fan of $\mathbb{A}^n$ is simplicial, `MinimalModel.Toric.Fan.isSimplicialFan_affine`. Refinements, star subdivisions and Theorem 3.1.29 are not yet in Lean.
- Fidelity: the Lean library has no smooth cones yet, so a smooth fan is not yet a Lean notion.
- No node of the map covers this section. Toric resolution enters the map through the toric MMP node of the later chapters.

### Notes and history

The resolution of toric singularities by subdivision is due to Kempf, Knudsen, Mumford and Saint-Donat (1973). In dimension 2 it goes back to the resolution of cyclic quotient singularities by Jung (1908) and Hirzebruch (1953), and the continued fraction of Exercise 3 carries both names. Pick's theorem is from 1899. In dimension 3 and higher a cone has many minimal smooth refinements, and they differ by flops: Example 3.1.33 is the first case, and the later chapters of this volume return to it.
