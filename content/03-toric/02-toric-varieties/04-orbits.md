---
title: The orbit-cone correspondence
nodes: []
sources: [CLS11, Ful93]
reads_with: [CLS11:ch3, Ful93:3.1]
requires: [P8.6, 3.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The orbit-cone correspondence

### Statement

**Definition 3.2.28 (distinguished points, orbits, orbit closures).** Let $\Sigma$ be a fan and $\sigma \in \Sigma$. The *distinguished point* $\gamma_\sigma \in U_\sigma$ is the homomorphism of semigroups $S_\sigma \to k$ with $\gamma_\sigma(m) = 1$ for $m \in \sigma^\perp \cap M$ and $\gamma_\sigma(m) = 0$ otherwise. Put $O(\sigma) = T_N \cdot \gamma_\sigma$, and let $V(\sigma)$ be the closure of $O(\sigma)$ in $X_\Sigma$. Let $N_\sigma = \operatorname{span}(\sigma) \cap N$ and $N(\sigma) = N / N_\sigma$. The dual lattice of $N(\sigma)$ is $\sigma^\perp \cap M$. The *star* of $\sigma$ is the set of the images in $N(\sigma)_{\mathbb{R}}$ of the cones of $\Sigma$ that contain $\sigma$.

The map $\gamma_\sigma$ is a homomorphism because $\sigma^\perp \cap \sigma^\vee$ is a face of $\sigma^\vee$: if $m, m' \in \sigma^\vee$ and $m + m' \in \sigma^\perp$, then $m, m' \in \sigma^\perp$.

**Theorem 3.2.29 (orbit-cone correspondence).** Let $\Sigma$ be a fan in $N_{\mathbb{R}}$.

1. The map $\sigma \mapsto O(\sigma)$ is a bijection from the cones of $\Sigma$ to the $T_N$-orbits of $X_\Sigma$.
2. $O(\sigma) \cong T_{N(\sigma)} = \operatorname{Hom}(\sigma^\perp \cap M, k^*)$, so $\dim O(\sigma) = n - \dim \sigma$.
3. $U_\sigma$ is the disjoint union of the orbits $O(\tau)$ for the faces $\tau$ of $\sigma$.
4. $V(\tau)$ is the disjoint union of the orbits $O(\sigma)$ for the cones $\sigma \in \Sigma$ that contain $\tau$. So $O(\sigma) \subset V(\tau)$ if and only if $\tau \subset \sigma$.
5. $V(\tau)$ is a normal toric variety with torus $O(\tau)$, and its fan is the star of $\tau$ in $N(\tau)_{\mathbb{R}}$.

Lean: not yet in Lean.

**Lemma 3.2.30 (limits find the orbit).** Let $\sigma \in \Sigma$, let $u \in N$ lie in the relative interior of $\sigma$, and let $\tau$ be a face of $\sigma$. Then $\lim_{t \to 0} \lambda^u(t) \cdot \gamma_\tau = \gamma_\sigma$ in $U_\sigma$. In particular $\lim_{t \to 0} \lambda^u(t) = \gamma_\sigma$.

Lean: not yet in Lean.

So the cone that contains $u$ in its relative interior is the cone whose orbit receives the limit of $\lambda^u$. For a complete fan, every $u$ lies in the relative interior of exactly one cone, and the fan is the picture of where the one-parameter subgroups go.

### Proof in words

A point of $U_\sigma$ is a homomorphism $p \colon S_\sigma \to k$. The set of $m$ where $p(m) \neq 0$ is closed under sums, and it contains $m$ and $m'$ whenever it contains $m + m'$. Such a subset of $S_\sigma$ is the set of lattice points of a face of $\sigma^\vee$, so it is $\tau^\perp \cap S_\sigma$ for a face $\tau$ of $\sigma$. On it, $p$ is a homomorphism to $k^*$, and it extends to the group $\tau^\perp \cap M$. The torus acts on these homomorphisms through the surjection $T_N \to T_{N(\tau)}$, transitively and with the stabilizer $T_{N_\tau}$. So the points with a given face $\tau$ form one orbit, the orbit of $\gamma_\tau$. The limit lemma is a computation in coordinates, and it gives the closure relations.

### Examples

**Example 3.2.31 (affine space).** In $\mathbb{A}^2$ the four faces of the orthant give the four orbits: the torus $\{xy \neq 0\}$ for $\{0\}$, the punctured axes $\{x = 0, y \neq 0\}$ and $\{y = 0, x \neq 0\}$ for the rays $e_1$ and $e_2$, and the origin for the orthant. The ray $e_1$ gives the axis $x = 0$, because $\gamma_{\operatorname{Cone}(e_1)}$ sends $\chi^{e_1^*} = x$ to $0$ and $y$ to $1$. In general the ray $\operatorname{Cone}(e_i)$ of $\mathbb{A}^n$ gives the divisor $V(e_i) = \{x_i = 0\}$.

**Example 3.2.32 (the projective plane).** The fan of $\mathbb{P}^2$ has 7 cones, and $\mathbb{P}^2$ has 7 orbits: the torus, the three coordinate lines minus the coordinate points, and the three coordinate points. The ray $u_i$ gives the line $V(u_i) = \{x_i = 0\}$, and the cone $\operatorname{Cone}(u_i, u_j)$ gives the point $\{x_i = x_j = 0\}$. For example $u_1 = e_1$ lies in the relative interior of $\operatorname{Cone}(u_1)$, and $\lambda^{u_1}(t) = (1 : t : 1)$ tends to $(1 : 0 : 1)$, a point of the line $x_1 = 0$. The star of $u_1$ in $N / \mathbb{Z} u_1 \cong \mathbb{Z}$ has the two rays, the images of $u_2$ and $u_0$, which are $1$ and $-1$. It is the fan of $\mathbb{P}^1$, and $V(u_1) \cong \mathbb{P}^1$, as part 5 says. For $\mathbb{P}^n$ there are $\binom{n+1}{k}$ orbits of dimension $n - k$ for $0 \le k \le n$, and $2^{n+1} - 1$ orbits in all.

**Example 3.2.33 (the quadric cone and $\frac1n(1,1)$).** The cone $\sigma_n$ has four faces, so $U_{\sigma_n}$ has four orbits: the torus, two curves and the vertex $\gamma_{\sigma_n}$. The vertex is the point where all the coordinates $x y^j$ vanish. The two curves are the images of the two coordinate axes of $\mathbb{A}^2$ under the quotient map of Example 3.2.15. The orbit closures of the rays are the two lines $V(e_2)$ and $V(n e_1 - e_2)$ through the vertex. For the quadric cone $xz = y^2$ they are the lines $x = y = 0$ and $y = z = 0$.

**Example 3.2.34 (the cone over a square).** The cone $\sigma$ of Example 3.1.7 has 10 faces: itself, 4 facets, 4 rays and $\{0\}$. So $xz = yw$ has 10 orbits: the vertex $\gamma_\sigma$, 4 orbits of dimension 1, 4 orbits of dimension 2 and the torus. The orbit closure of the ray $u_1$ is the plane $V(u_1) = \{z = w = 0\}$. Indeed, $\gamma_{\operatorname{Cone}(u_1)}$ kills $\chi^m$ exactly when $\langle m, u_1 \rangle > 0$, and among the generators this holds for $m_3$ and $m_4$, with $\langle m_3, u_1 \rangle = \langle m_4, u_1 \rangle = 1$. In the same way $V(u_2) = \{x = w = 0\}$, $V(u_3) = \{x = y = 0\}$ and $V(u_4) = \{y = z = 0\}$. The four planes meet in pairs along the four lines $V(\operatorname{Cone}(u_i, u_{i+1}))$, and all four meet at the vertex. Chapter 3 shows that these planes are not $\mathbb{Q}$-Cartier.

**Example 3.2.35 (orbit closures through a singular point).** In $\mathbb{P}(1,1,n)$ with $n \ge 2$ (Example 3.1.26), the only cone that is not smooth is $\operatorname{Cone}(u_1, u_3)$. So the only singular point is the fixed point $\gamma_{\operatorname{Cone}(u_1, u_3)}$, by Theorem 3.2.13 and part 3. The cones that contain $u_4$ are $\operatorname{Cone}(u_3, u_4)$ and $\operatorname{Cone}(u_4, u_1)$, so $V(u_4)$ does not pass through the singular point. The curves $V(u_1)$ and $V(u_3)$ do pass through it. By part 5 each of the three curves is $\mathbb{P}^1$: for example the star of $u_1$ in $N / \mathbb{Z} u_1 \cong \mathbb{Z}$ has the rays spanned by the images $n$ and $-1$ of $u_3$ and $u_4$. So an orbit closure can be smooth while the variety is singular at a point of it. The divisors of Chapter 3 see the difference: $V(u_4)$ is Cartier, and $V(u_1)$ is not.

### Proof

*Proof of Lemma 3.2.30.* For $m \in S_\sigma$, the point $\lambda^u(t) \cdot \gamma_\tau$ takes the value $t^{\langle m, u \rangle} \gamma_\tau(m)$ at $\chi^m$. This is $t^{\langle m, u \rangle}$ if $m \in \tau^\perp$ and $0$ otherwise. For $m \in S_\sigma$, $\langle m, u \rangle \ge 0$, and since $u$ is in the relative interior of $\sigma$, $\langle m, u \rangle = 0$ if and only if $m \in \sigma^\perp$. As $\sigma^\perp \subset \tau^\perp$, the limit at $t = 0$ is $1$ for $m \in \sigma^\perp$ and $0$ otherwise, which is $\gamma_\sigma$. For $\tau = \{0\}$, $\gamma_{\{0\}}$ is the identity of $T_N$. $\square$

*Proof of Theorem 3.2.29.* Fix $\sigma$ and a point $p \in U_\sigma$, seen as a homomorphism $p \colon S_\sigma \to k$. Let $F = \{m \in S_\sigma : p(m) \neq 0\}$. It contains $0$, it is closed under sums, and $m + m' \in F$ with $m, m' \in S_\sigma$ forces $m, m' \in F$. Let $g_1, \dots, g_s$ generate $S_\sigma$, let $m_0$ be the sum of the $g_i$ that lie in $F$, and let $\tau = \sigma \cap m_0^\perp$, a face of $\sigma$. Each $m \in F$ is a nonnegative integer combination of the $g_i$, and by the property of $F$ only the $g_i$ in $F$ appear. Each of these is a summand of $m_0$, so $0 \le \langle g_i, u \rangle \le \langle m_0, u \rangle = 0$ for $u \in \tau$. So $F \subset \tau^\perp$. Conversely, let $G$ be the smallest face of $\sigma^\vee$ that contains $m_0$. By Proposition 3.1.4, part 5, $G = \tau'^*$ for a face $\tau'$ of $\sigma$, and $m_0 \in \tau'^\perp$ gives $\tau' \subset \tau$, so $\tau^* \subset G$. Since $m_0 \in \tau^*$, $G = \tau^*$, and $m_0$ lies in the relative interior of $\tau^*$. For $m \in S_\sigma \cap \tau^\perp$, the point $k m_0 - m$ then lies in $\tau^*$ for $k \gg 0$. So $k m_0 = m + (k m_0 - m)$ is a sum in $S_\sigma$, and since $k m_0 \in F$, also $m \in F$. So $F = S_\sigma \cap \tau^\perp$. The cone $\tau^*$ has dimension $n - \dim \tau = \dim \tau^\perp$, so it has a lattice point $m_1$ in its interior relative to $\tau^\perp$. For $m \in \tau^\perp \cap M$ and $k \gg 0$, $m + k m_1 \in F$, so $F$ generates the group $\tau^\perp \cap M$. So $p|_F$ extends to a unique homomorphism $\tau^\perp \cap M \to k^*$, a point of $T_{N(\tau)}$.

Conversely every homomorphism $\tau^\perp \cap M \to k^*$, extended by $0$, is a point of $U_\sigma$. So the points of $U_\sigma$ with face $\tau$ are in bijection with $T_{N(\tau)}$, and $\gamma_\tau$ corresponds to $1$. The torus acts by $(t \cdot p)(m) = \chi^m(t) p(m)$, which is the action of $T_N$ on $T_{N(\tau)}$ through the surjection $T_N \to T_{N(\tau)}$ dual to $\tau^\perp \cap M \subset M$. So these points form the single orbit $O(\tau) \cong T_{N(\tau)}$. This proves parts 2 and 3. The point $\gamma_\tau$ of $U_\sigma$ restricts to the point $\gamma_\tau$ of $U_\tau$, so $O(\tau)$ does not depend on the chart, and part 1 follows from part 3 because the $U_\sigma$ cover $X_\Sigma$ and different faces give different subsets $F$.

For part 4, let $\tau \subset \sigma$. By Lemma 3.2.30, $\gamma_\sigma$ is a limit of points of $O(\tau)$, so $O(\sigma) \subset V(\tau)$. Conversely, if $O(\sigma) \subset V(\tau)$, then $V(\tau)$ meets the open set $U_\sigma$, so $O(\tau)$ meets it. Since $U_\sigma$ is invariant, $O(\tau) \subset U_\sigma$, and part 3 gives $\tau \subset \sigma$. The closed invariant set $V(\tau)$ is a union of orbits, so it is the union of the $O(\sigma)$ with $\sigma \supset \tau$. Part 5 is cited without proof (Cox-Little-Schenck, Chapter 3): for $\sigma \supset \tau$, the ring of $V(\tau) \cap U_\sigma$ is $k[S_\sigma \cap \tau^\perp]$, which is the semigroup ring of the image of $\sigma$ in $N(\tau)_{\mathbb{R}}$. $\square$

### Exercises

1. (A) List the 9 orbits of $\mathbb{F}_n$, their dimensions, and the inclusions between their closures.
2. (A) Show that the fixed points of $T_N$ on $X_\Sigma$ correspond to the cones of dimension $n$, and that $X_\Sigma$ has a fixed point if and only if $\Sigma$ has a cone of dimension $n$.
3. (B) For the fan of $\mathbb{F}_n$, compute the star of $u_2$ and of $u_1$, and show that $V(u_2) \cong V(u_1) \cong \mathbb{P}^1$.
4. (B) Show that the singular locus of $X_\Sigma$ is the union of the orbits $O(\sigma)$ for the cones $\sigma$ that are not smooth, and that it is closed.

### Lean

- Status: the Lean library has the rays of a fan, `MinimalModel.Toric.Fan.rays`, as the cones of dimension one, and their type `MinimalModel.Toric.Fan.Ray`, with `MinimalModel.Toric.Fan.rays_finite`. These index the orbit closures of dimension $n - 1$. Distinguished points, orbits, stars and Theorem 3.2.29 are not yet in Lean.
- Fidelity: the Lean rays are cones of the form `latticeCone {v}` with $v \neq 0$ (`MinimalModel.Toric.IsRay`). The lattice point $v$ need not be primitive. The minimal generator $u_\rho$ is `MinimalModel.Toric.Fan.generator`, and `MinimalModel.Toric.IsRay.eq_rayGenerator` says that it is the only primitive lattice point of the ray that spans it.
- No node of the map covers this section.

### Notes and history

The orbit-cone correspondence is in Kempf, Knudsen, Mumford and Saint-Donat (1973) and in Fulton's book, Chapter 3. The description of the points of $U_\sigma$ as semigroup homomorphisms makes it a statement about faces of semigroups. The limits of one-parameter subgroups are a toric case of the Hilbert-Mumford criterion of geometric invariant theory, which the later chapters of this volume use for variation of GIT.
