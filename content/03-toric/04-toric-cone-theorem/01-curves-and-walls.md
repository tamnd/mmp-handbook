---
title: Invariant curves and the wall relation
nodes: [MMFAWNT87R]
sources: [CLS11, Rei83, FS04, Oda88]
reads_with: [CLS11:ch6, Rei83:1, FS04:4]
requires: [P8.6, 3.2, 3.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Invariant curves and the wall relation

### Statement

Let $\Sigma$ be a fan in $N_{\mathbb{R}} \cong \mathbb{R}^n$. For a cone $\tau \in \Sigma$, $V(\tau)$ is the closure of the orbit $O(\tau)$, of dimension $n - \dim \tau$ (Theorem 3.2.29). So the torus-invariant curves of $X_\Sigma$ are the $V(\tau)$ with $\dim \tau = n - 1$. This section computes the intersection numbers of divisors with these curves.

**Definition 3.4.1 (walls and wall pairs).** A *wall pair* of $\Sigma$ is a pair $(\sigma, \sigma')$ of different cones of $\Sigma$ of dimension $n$ such that $\tau = \sigma \cap \sigma'$ has dimension $n - 1$. The cone $\tau$ is then the *wall* between $\sigma$ and $\sigma'$, and $V(\tau)$ is its *wall curve*. If $\sigma$ and $\sigma'$ are simplicial, we write

$$\tau = \operatorname{Cone}(u_1, \dots, u_{n-1}), \qquad \sigma = \operatorname{Cone}(u_1, \dots, u_{n-1}, u_n), \qquad \sigma' = \operatorname{Cone}(u_1, \dots, u_{n-1}, u_{n+1}),$$

with the $u_i$ the minimal generators of the rays. These are the *standard labels* of the wall.

**Lemma 3.4.2 (walls of a complete fan).** Let $\Sigma$ be complete. Every cone $\tau \in \Sigma$ of dimension $n - 1$ lies in exactly two cones of $\Sigma$ of dimension $n$, one on each side of the hyperplane $\operatorname{span}(\tau)$. So every such $\tau$ is the wall of exactly one wall pair, up to order.

Lean: not yet in Lean.

**Lemma 3.4.3 (the curve of a wall).** Let $(\sigma, \sigma')$ be a wall pair with wall $\tau$. Then $V(\tau) \cong \mathbb{P}^1$. It is the union of $O(\tau) \cong k^*$ and the two fixed points $\gamma_\sigma$ and $\gamma_{\sigma'}$. If $\sigma$ and $\sigma'$ are simplicial with the standard labels, write $u_{n+1} = \sum_{i=1}^n c_i u_i$ with $c_i \in \mathbb{Q}$. Then $c_n < 0$, and

$$\operatorname{mult}(\sigma') = k \cdot \operatorname{mult}(\tau), \qquad \operatorname{mult}(\sigma) = k' \cdot \operatorname{mult}(\tau),$$

where $k$ and $k'$ are the positive integers with $\bar u_{n+1} = k w'$ and $\bar u_n = k' w$ in $N(\tau)$, and $w$, $w' = -w$ are the two primitive vectors of the rank one lattice $N(\tau)$.

Lean: not yet in Lean.

**Theorem 3.4.4 (intersection with a wall curve).** Let $(\sigma, \sigma')$ be a wall pair with wall $\tau$, and let $D = \sum_\rho a_\rho D_\rho$ be a torus-invariant $\mathbb{Q}$-Cartier divisor with data $m_\sigma, m_{\sigma'} \in M_{\mathbb{Q}}$ on $\sigma$ and $\sigma'$ (Definition 3.3.11, with $\langle m_\sigma, u_\rho \rangle = -a_\rho$ for $\rho \in \sigma(1)$). Then $m_\sigma - m_{\sigma'} \in \tau^\perp$, and

$$D \cdot V(\tau) = \langle m_\sigma - m_{\sigma'}, w' \rangle,$$

where $w'$ is the primitive vector of $N(\tau)$ on the side of $\sigma'$, and $\tau^\perp$ pairs with $N(\tau)$. If $\sigma$ and $\sigma'$ are simplicial with the standard labels and $u_{n+1} = \sum_{i=1}^n c_i u_i$, then

$$D \cdot V(\tau) = \frac{\operatorname{mult}(\tau)}{\operatorname{mult}(\sigma')} \Big( a_{n+1} - \sum_{i=1}^n c_i a_i \Big).$$

Lean: not yet in Lean. The number in the large brackets is the degree `MinimalModel.Toric.Fan.WallData.degree` of the Lean library, so the Lean degree is $\operatorname{mult}(\sigma') / \operatorname{mult}(\tau)$ times $D \cdot V(\tau)$.

**Theorem 3.4.5 (the wall relation).** Let $(\sigma, \sigma')$ be a wall pair of simplicial cones with wall $\tau$ and the standard labels.

1. The numbers $b_\rho = D_\rho \cdot V(\tau)$ satisfy $\sum_{\rho} b_\rho u_\rho = 0$. They vanish for $\rho \notin \sigma(1) \cup \sigma'(1)$, and

$$b_{u_n} = \frac{\operatorname{mult}(\tau)}{\operatorname{mult}(\sigma)} > 0, \qquad b_{u_{n+1}} = \frac{\operatorname{mult}(\tau)}{\operatorname{mult}(\sigma')} > 0.$$

These conditions determine the $b_\rho$: they are the unique linear relation among $u_1, \dots, u_{n+1}$ with the given coefficient at $u_{n+1}$.

2. If $\sigma$ and $\sigma'$ are smooth, then $D_{u_n} \cdot V(\tau) = D_{u_{n+1}} \cdot V(\tau) = 1$, and there are unique integers $b_1, \dots, b_{n-1}$ with

$$u_n + u_{n+1} = \sum_{i=1}^{n-1} b_i u_i.$$

Then $D_{u_i} \cdot V(\tau) = -b_i$ for $i \le n - 1$.

3. For the canonical divisor, $K_{X_\Sigma} \cdot V(\tau) = -\sum_\rho b_\rho$.

Node: MMFAWNT87R · Lean: `MinimalModel.Toric.Fan.exists_unique_wall_relation`

The relation of part 1 is the *wall relation* of $\tau$. In the smooth case it is the relation $u_n + u_{n+1} - \sum b_i u_i = 0$ of part 2. Part 2 is the statement of the node, and the Lean theorem proves the existence and uniqueness of the integers $b_i$. The identification $D_{u_i} \cdot V(\tau) = -b_i$ is not in Lean.

### Proof in words

A wall curve is the toric variety of the star of $\tau$, a fan in the line $N(\tau)_{\mathbb{R}}$. That fan has two rays, the images of $\sigma$ and $\sigma'$, and they point in opposite directions. So the curve is $\mathbb{P}^1$, with one fixed point for each of the two cones.

To intersect $D$ with $V(\tau)$, move $D$ by a character so that its data on $\sigma'$ becomes zero. The new divisor has no component through the chart $U_{\sigma'}$, so near $\gamma_{\sigma'}$ it does not meet the curve. On $U_\sigma$ it is the divisor of the character $\chi^{m_{\sigma'} - m_\sigma}$. That character is trivial on $\tau$, so it is a character of the torus $O(\tau)$ of the curve, and its order at the point $\gamma_\sigma$ is read off with Proposition 3.3.3 on the curve. The result is a single pairing in the rank one lattice $N(\tau)$. In the simplicial case the data $m_\sigma$ is the solution of a linear system, and the pairing becomes the expression in the $a_i$ and $c_i$.

The wall relation is that formula applied to each $D_\rho$. The vector $(D_\rho \cdot V(\tau))_\rho$ is a linear relation among the $u_\rho$ because a principal divisor $\operatorname{div}(\chi^m)$ has degree zero on every curve.

### Examples

**Example 3.4.6 (projective space).** Let $\Sigma$ be the fan of $\mathbb{P}^n$, with rays $u_0, \dots, u_n$ and $u_0 + u_1 + \dots + u_n = 0$. A wall is spanned by all the rays but two, say $u_i$ and $u_j$, and the two cones on its sides add $u_i$ and $u_j$. All cones are smooth, and the relation is $u_i + u_j + \sum_{l \neq i, j} u_l = 0$. So $D_l \cdot V(\tau) = 1$ for every $l$, as for a line, and $K \cdot V(\tau) = -(n + 1)$. Every wall curve of $\mathbb{P}^n$ is a coordinate line.

**Example 3.4.7 (the Hirzebruch surface).** Let $\mathbb{F}_n$ have the rays $u_1 = (1, 0)$, $u_2 = (0, 1)$, $u_3 = (-1, n)$, $u_4 = (0, -1)$ and the four cones of consecutive rays. In dimension 2 the walls are the rays, and $V(\rho_i) = D_i$. The four wall relations are

$$u_1 + u_3 - n u_2 = 0, \qquad u_2 + u_4 + 0 \cdot u_1 = 0, \qquad u_1 + u_3 + n u_4 = 0, \qquad u_2 + u_4 + 0 \cdot u_3 = 0,$$

for the walls $u_2$, $u_1$, $u_4$ and $u_3$. So $D_2^2 = -n$, $D_4^2 = n$ and $D_1^2 = D_3^2 = 0$, and neighbours meet with intersection number $1$. This recovers Proposition 3.3.14 and Example 3.3.15. In general, for a smooth complete surface the wall relation at $u_i$ is $u_{i-1} + u_{i+1} = b_i u_i$, and part 2 of Theorem 3.4.5 gives $D_i^2 = -b_i$.

**Example 3.4.8 (a singular point on the curve).** Let $\Sigma$ be the fan of $\mathbb{P}(1,1,n)$ of Example 3.1.26, with rays $u_1 = (1, 0)$, $u_3 = (-1, n)$, $u_4 = (0, -1)$ and $u_1 + u_3 + n u_4 = 0$. The cone $\operatorname{Cone}(u_1, u_3)$ has multiplicity $n$ and the other two are smooth. At the wall $u_4$, both cones are smooth, so the relation is normalized with coefficient $1$ at $u_1$ and $u_3$. It is $u_1 + u_3 + n u_4 = 0$, so $D_4^2 = n$. At the wall $u_1$, the cones are $\sigma = \operatorname{Cone}(u_1, u_4)$ of multiplicity $1$ and $\sigma' = \operatorname{Cone}(u_1, u_3)$ of multiplicity $n$. Part 1 asks for the coefficient $1$ at $u_4$ and $\frac1n$ at $u_3$, so the relation is

$$\tfrac1n u_1 + \tfrac1n u_3 + u_4 = 0, \qquad D_1^2 = \tfrac1n, \quad D_3 \cdot D_1 = \tfrac1n, \quad D_4 \cdot D_1 = 1.$$

In $\operatorname{Cl}(\mathbb{P}(1,1,n)) \cong \mathbb{Z}$, $D_1 \sim D_3$ is the generator and $D_4 \sim n D_1$, so these numbers agree with $D_1^2 = \frac1n$. The formula of Theorem 3.4.4 gives the same: on the wall $u_1$, $u_3 = c_1 u_1 + c_4 u_4$ with $c_1 = -1$ and $c_4 = -n$, so $D_1 \cdot D_1 = \frac{1}{n}(0 - (-1) \cdot 1) = \frac1n$.

**Example 3.4.9 (the curve of a small resolution).** Let $\Sigma_+$ be the fan with the maximal cones $\operatorname{Cone}(u_1, u_2, u_3)$ and $\operatorname{Cone}(u_1, u_3, u_4)$ of Example 3.1.33, where $u_1 = (0,0,1)$, $u_2 = (1,0,1)$, $u_3 = (1,1,1)$, $u_4 = (0,1,1)$. The fan is not complete, but the two cones form a wall pair with wall $\tau = \operatorname{Cone}(u_1, u_3)$, and Lemma 3.4.3 and Theorem 3.4.4 apply. Both cones are smooth, and $u_2 + u_4 = u_1 + u_3$. So $b_1 = b_3 = 1$ in part 2, and

$$D_2 \cdot C = D_4 \cdot C = 1, \qquad D_1 \cdot C = D_3 \cdot C = -1, \qquad K \cdot C = 0$$

for $C = V(\tau)$. This solves Problem 5 of Chapter 3. The curve $C$ is the exceptional curve of the small resolution of the cone over a square, and Chapter 5 shows that it is the curve of the Atiyah flop.

**Example 3.4.10 (the weighted projective space $\mathbb{P}(1,1,1,2)$).** Take the fan of Example 3.3.25: rays $u_1 = e_1$, $u_2 = e_2$, $u_3 = e_3$, $u_0 = -e_1 - e_2 - 2 e_3$, relation $u_0 + u_1 + u_2 + 2 u_3 = 0$, and the four cones of three rays. Only $\operatorname{Cone}(u_0, u_1, u_2)$ is singular, of multiplicity $2$. All six walls are smooth cones of dimension 2: for example $\operatorname{span}(u_0, u_1) \cap \mathbb{Z}^3$ is generated by $e_1$ and $e_2 + 2 e_3$, and $u_0 = -e_1 - (e_2 + 2e_3)$. At the wall $\operatorname{Cone}(u_1, u_2)$, the cone $\sigma = \operatorname{Cone}(u_1, u_2, u_3)$ is smooth and $\sigma' = \operatorname{Cone}(u_0, u_1, u_2)$ has multiplicity 2. So the coefficient of $u_3$ is $1$ and that of $u_0$ is $\frac12$:

$$\tfrac12 u_0 + \tfrac12 u_1 + \tfrac12 u_2 + u_3 = 0, \qquad K \cdot V(\tau) = -\tfrac52.$$

At the wall $\operatorname{Cone}(u_1, u_3)$ both cones are smooth, the relation is $u_0 + u_1 + u_2 + 2 u_3 = 0$, and $K \cdot V(\tau) = -5$. With $H = D_0$, $\operatorname{Cl} = \mathbb{Z} H$, and $K \sim -5H$, the first curve has $H \cdot C = \frac12$ and the second has $H \cdot C = 1$.

### Proof

*Proof of Lemma 3.4.2.* Let $\tau$ have dimension $n - 1$, let $x$ be a point of its relative interior, and let $H = \operatorname{span}(\tau)$, a hyperplane. Let $\gamma \in \Sigma$ be a cone of dimension $n$ that contains $\tau$. Then $\gamma \cap H$ is a face of $\gamma$ (cut out by a form vanishing on $H$ that is nonnegative on $\gamma$), and it contains $\tau$, so $\tau = \gamma \cap H$ is a facet of $\gamma$, since $\tau$ is a cone of the fan and a face of $\gamma$. Hence $\gamma$ lies in one closed half-space $H^+$ of $H$. Since $x$ is in the relative interior of the facet $\tau$, only the inequality of this facet is tight at $x$, so $\gamma$ contains $B \cap H^+$ for a small ball $B$ around $x$. Two cones $\gamma \neq \gamma'$ of dimension $n$ on the same side would then share the interior points of $B \cap H^+$, and $\gamma \cap \gamma'$ would be a face of both of dimension $n$, so $\gamma = \gamma'$. For existence, take $y \notin H$. The points $x + t y$, for $t > 0$ small, lie in cones of $\Sigma$ since $\Sigma$ is complete, and there are finitely many cones, so one cone $\gamma$ contains $x + t y$ for a sequence $t \to 0$. It is closed, so $x \in \gamma$. Then $\gamma \cap \tau$ is a face of $\tau$ that contains the relative interior point $x$, so $\tau \subset \gamma$, and $\gamma \not\subset H$, so $\gamma \neq \tau$. If $\dim \gamma < n$ we replace $\gamma$ by a cone of dimension $n$ that contains it: the cones of dimension $n$ cover $N_{\mathbb{R}}$, since their union is closed and contains every point outside the finitely many proper subspaces $\operatorname{span}(\delta)$ with $\dim \delta < n$. The same argument with $-y$ gives the second cone. $\square$

*Proof of Lemma 3.4.3.* By Theorem 3.2.29, part 5, $V(\tau)$ is the toric variety of the star of $\tau$ in $N(\tau)_{\mathbb{R}} \cong \mathbb{R}$. The cones of $\Sigma$ that contain $\tau$ are $\tau$, $\sigma$ and $\sigma'$: a cone that contains $\tau$ properly has dimension $n$ and is $\sigma$ or $\sigma'$ by the argument of Lemma 3.4.2, which only used the cones near $x$. The images are $\{0\}$ and the two rays $\mathbb{R}_{\ge 0} \bar u_n$ and $\mathbb{R}_{\ge 0} \bar u_{n+1}$, and these rays are different, since the images of $\sigma$ and $\sigma'$ lie on the two sides of $H$. So they are opposite, and the star is the fan of $\mathbb{P}^1$. The orbits are $O(\tau)$, $O(\sigma) = \{\gamma_\sigma\}$ and $O(\sigma') = \{\gamma_{\sigma'}\}$ (Theorem 3.2.29, part 4).

In the simplicial case, $c_n \neq 0$ since $u_{n+1} \notin \operatorname{span}(\tau)$. Suppose $c_n > 0$. Choose $s > 0$ with $c_i + s > 0$ for all $i \le n - 1$, and put $x = u_{n+1} + s(u_1 + \dots + u_{n-1})$. Then $x \in \sigma'$, and $x = \sum_{i < n} (c_i + s) u_i + c_n u_n \in \sigma$. So $x \in \sigma \cap \sigma' = \tau \subset H$. But the $u_n$-coordinate of $x$ in the basis $u_1, \dots, u_n$ is $c_n \neq 0$, so $x \notin H$, a contradiction. So $c_n < 0$, which is the statement that $\bar u_{n+1} = c_n \bar u_n$ points away from $\bar u_n$.

For the multiplicities, let $L' = \mathbb{Z} u_1 + \dots + \mathbb{Z} u_{n-1} + \mathbb{Z} u_{n+1}$ and $N_\tau = \operatorname{span}(\tau) \cap N$. The exact sequence $0 \to N_\tau \to N \to N(\tau) \to 0$ restricts to $0 \to L' \cap N_\tau \to L' \to \mathbb{Z} \bar u_{n+1} \to 0$. An element of $L'$ lies in $\operatorname{span}(\tau)$ only if its coefficient at $u_{n+1}$ is zero, so $L' \cap N_\tau = \mathbb{Z} u_1 + \dots + \mathbb{Z} u_{n-1}$. The index is multiplicative in such sequences, so

$$\operatorname{mult}(\sigma') = [N : L'] = [N_\tau : L' \cap N_\tau] \cdot [N(\tau) : \mathbb{Z} \bar u_{n+1}] = \operatorname{mult}(\tau) \cdot k.$$

The same argument with $u_n$ gives $\operatorname{mult}(\sigma) = \operatorname{mult}(\tau) \cdot k'$. $\square$

*Proof of Theorem 3.4.4.* Both $m_\sigma$ and $m_{\sigma'}$ take the value $-a_\rho$ on the rays of $\tau$, which span $\operatorname{span}(\tau)$, so $m_\sigma - m_{\sigma'} \in \tau^\perp$. Both sides of the formula are linear in $D$, so we may replace $D$ by $rD$ and assume that $D$ is Cartier and $m_\sigma, m_{\sigma'} \in M$. Put $D' = D + \operatorname{div}(\chi^{m_{\sigma'}})$. It is linearly equivalent to $D$, so $D' \cdot V(\tau) = D \cdot V(\tau)$. By Proposition 3.3.3 its coefficient at $\rho$ is $a_\rho + \langle m_{\sigma'}, u_\rho \rangle$, and its data on $\sigma$ and $\sigma'$ are $m = m_\sigma - m_{\sigma'}$ and $0$. So $D'|_{U_{\sigma'}} = 0$ by Theorem 3.3.12, and $D'|_{U_\sigma} = \operatorname{div}(\chi^{-m})|_{U_\sigma}$. In particular no component of $D'$ contains $V(\tau)$, because every component of $D'$ is a $D_\rho$ with $\rho \notin \sigma'(1)$ and $V(\tau)$ meets $U_{\sigma'}$. So $D' \cdot V(\tau)$ is the degree of the restricted Cartier divisor $D'|_{V(\tau)}$. Its local equation is $1$ near $\gamma_{\sigma'}$, and $\chi^{-m}$ on $U_\sigma \cap V(\tau)$. Since $m \in \tau^\perp \cap M$, the function $\chi^{-m}$ restricts to the character $\chi^{-m}$ of the torus $O(\tau) = T_{N(\tau)}$, by the construction of $V(\tau)$ in Theorem 3.2.29. Now $U_\sigma \cap V(\tau)$ is the affine line of the ray $\mathbb{R}_{\ge 0} w$ of the star, and by Proposition 3.3.3 on $V(\tau)$ the order of $\chi^{-m}$ at the point $\gamma_\sigma$ is $\langle -m, w \rangle$. So

$$D \cdot V(\tau) = \langle -m, w \rangle = \langle m_\sigma - m_{\sigma'}, w' \rangle,$$

using $w' = -w$. In the simplicial case, $\bar u_{n+1} = k w'$, and $k = \operatorname{mult}(\sigma') / \operatorname{mult}(\tau)$ by Lemma 3.4.3. So

$$D \cdot V(\tau) = \frac1k \langle m_\sigma - m_{\sigma'}, u_{n+1} \rangle = \frac1k \Big( \sum_{i=1}^n c_i \langle m_\sigma, u_i \rangle + a_{n+1} \Big) = \frac1k \Big( a_{n+1} - \sum_{i=1}^n c_i a_i \Big). \qquad \square$$

*Proof of Theorem 3.4.5.* For part 1, apply Theorem 3.4.4 to $D = D_\rho$. The coefficient $a_{n+1}$ is $1$ for $\rho = u_{n+1}$, and $a_i$ is $1$ for $\rho = u_i$; all others vanish. So $b_{u_{n+1}} = \frac1k$, $b_{u_i} = -\frac{c_i}{k}$ for $i \le n$, and $b_\rho = 0$ for the other rays. Then

$$\sum_\rho b_\rho u_\rho = \frac1k \Big( u_{n+1} - \sum_{i=1}^n c_i u_i \Big) = 0.$$

The value $b_{u_{n+1}} = \frac1k = \operatorname{mult}(\tau) / \operatorname{mult}(\sigma')$ comes from the formula of Lemma 3.4.3. The formula for $b_{u_n}$ follows by exchanging the roles of $\sigma$ and $\sigma'$, since $D_{u_n} \cdot V(\tau)$ does not depend on the labels. The vectors $u_1, \dots, u_{n+1}$ span $N_{\mathbb{R}}$ and are $n + 1$ in number, so their relations form a line. A relation is fixed by its coefficient at $u_{n+1}$, which is not zero on this line, since $u_1, \dots, u_n$ are independent.

For part 2, all multiplicities are $1$, so $b_{u_n} = b_{u_{n+1}} = 1$, and the relation of part 1 reads $u_n + u_{n+1} + \sum_{i < n} (D_{u_i} \cdot V(\tau)) u_i = 0$. The numbers $D_{u_i} \cdot V(\tau) = -c_i$ are integers: $u_{n+1}$ is a lattice point and $u_1, \dots, u_n$ is a basis of $N$. So $b_i = -D_{u_i} \cdot V(\tau)$ are integers with $u_n + u_{n+1} = \sum b_i u_i$. They are unique since $u_1, \dots, u_{n-1}$ are independent.

Part 3 follows from $K_{X_\Sigma} = -\sum_\rho D_\rho$ (Theorem 3.3.26) and linearity. $\square$

### Exercises

1. (A) Check the four wall relations of Example 3.4.7 and the intersection numbers $D_1 \cdot D_2 = D_2 \cdot D_3 = 1$ on $\mathbb{F}_n$.
2. (A) Let $\Sigma$ be the fan of $\mathbb{P}^1 \times \mathbb{P}^1 \times \mathbb{P}^1$, with rays $\pm e_1, \pm e_2, \pm e_3$. Write the wall relation of each of the 12 walls, and show that each wall curve is a fibre of one of the three projections to $\mathbb{P}^1 \times \mathbb{P}^1$.
3. (A) In Example 3.4.10, compute the wall relations of all six walls of $\mathbb{P}(1,1,1,2)$. Show that the three curves through the singular point have $H \cdot C = \frac12$ and the other three have $H \cdot C = 1$.
4. (B) Let $(\sigma, \sigma')$ be a wall pair of simplicial cones. Show that $D_{u_n} \cdot V(\tau) \cdot \operatorname{mult}(\sigma) = D_{u_{n+1}} \cdot V(\tau) \cdot \operatorname{mult}(\sigma')$, and interpret it with the two points $\gamma_\sigma$, $\gamma_{\sigma'}$ of $V(\tau)$ and the cyclic quotient singularities there.
5. (B) Let $\sigma_n = \operatorname{Cone}(e_2, n e_1 - e_2)$ and let $\Sigma$ be its star subdivision at $e_1$, the minimal resolution of $\frac1n(1,1)$ (Example 3.2.41). Show that the exceptional curve $E = V(\mathbb{R}_{\ge 0} e_1)$ has the wall relation $e_2 + (n e_1 - e_2) - n e_1 = 0$, so $E^2 = -n$ and $K \cdot E = n - 2$.
6. (C) Drop the simplicial hypothesis. Let $\sigma$, $\sigma'$ be a wall pair with $\sigma'$ simplicial and $\sigma$ arbitrary of dimension $n$. Show that the second formula of Theorem 3.4.4 still holds, with $m_\sigma$ any data of $D$ on $\sigma$ and $u_{n+1} = \sum c_i u_i$ any expression in the rays of $\sigma$.

### Lean

- Status: the wall relation for two smooth cones is `MinimalModel.Toric.Fan.exists_unique_wall_relation`, proved. Its hypotheses are two cones of the fan spanned by lattice bases $v, u_1, \dots, u_k$ and $v', u_1, \dots, u_k$ with $v \neq v'$. It does not assume that the cones meet in a wall, because the proof does not need it. The fan of $\mathbb{P}^2$ checks the hypotheses (`MinimalModel.Toric.P2.wall_c12_c20`, with $e_1 + e_0 = (-1) \cdot e_2$). The Lean structure `MinimalModel.Toric.Fan.WallData` records the relation $u_{n+1} = \sum c_i u_i$ of a simplicial wall, and `MinimalModel.Toric.Fan.WallData.degree` is the number $a_{n+1} - \sum c_i a_i$. Lemmas 3.4.2 and 3.4.3 and Theorem 3.4.4 are not in Lean, since the curves $V(\tau)$ and their intersection numbers need the toric variety as a scheme.
- Fidelity: the Lean theorem states $v + v' = \sum b_i u_i$, so its $b_i$ are the integers of part 2, and $D_{u_i} \cdot V(\tau) = -b_i$. The Lean degree is $\operatorname{mult}(\sigma') / \operatorname{mult}(\tau)$ times the intersection number, and the two agree for smooth cones. For the cone theorem of Section 2 only the sign of the degree matters, so the factor is harmless there.
- Node MMFAWNT87R is the wall relation of part 2. The fan itself is node MMH8EFW2JT, `MinimalModel.Toric.Fan`.

### Notes and history

The wall relation goes back to the first papers on toric varieties. Oda's book (1988) uses it for smooth complete surfaces, where the relation $u_{i-1} + u_{i+1} = b_i u_i$ is the toric form of the self-intersection numbers. The map cites Reid (1983, Section 1) for the relation on a simplicial fan, with rational coefficients. Cox-Little-Schenck, Chapter 6, prove the intersection formula, and Fujino and Sato (2004, Section 4) use it in their account of the toric MMP.
