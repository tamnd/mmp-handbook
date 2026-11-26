---
title: Klt surface germs are quotients
nodes: []
sources: [KM98, Kol13, Bri68, Mum61, Rei87]
reads_with: [KM98:ch4, Kol13:ch3]
requires: [P8.10, 4.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Klt surface germs are quotients

### Statement

Section 2.4 proved that every quotient singularity is klt. In dimension 2 the converse holds. This section sketches its proof, computes the discrepancies of the cyclic quotients, and states the classification of the lc surface germs. Throughout, the field is $\mathbb{C}$, since the proof uses the local fundamental group.

Let $(X, x)$ be a normal surface germ with $K_X$ $\mathbb{Q}$-Cartier. The *index* of $X$ at $x$ is the smallest $r \ge 1$ such that $r K_X$ is Cartier at $x$. Choose a local generator $s$ of $\mathcal{O}_X(r K_X)$ near $x$. The *index one cover* is
$$\pi \colon \tilde X = \operatorname{Spec}_X \bigoplus_{i=0}^{r-1} \mathcal{O}_X(-i K_X) \to X,$$
where the multiplication uses the isomorphism $\mathcal{O}_X(-r K_X) \cong \mathcal{O}_X$ given by $s$. Here $\mathcal{O}_X(D)$ for a Weil divisor $D$ is the reflexive sheaf of $D$. The group $\mu_r$ acts on $\tilde X$, with weight $i$ on the summand $\mathcal{O}_X(-iK_X)$, and $X = \tilde X / \mu_r$. The cover is étale over $X \setminus \{x\}$, so it is étale in codimension 1, and $K_{\tilde X}$ is Cartier (KM98, Chapter 5).

**Theorem 4.3.18 (klt surface germs are quotients).** A normal surface germ $(X, x)$ is klt if and only if it is analytically isomorphic to $(\mathbb{C}^2 / G, 0)$ for a finite subgroup $G \subset GL_2(\mathbb{C})$. The group can be chosen to contain no pseudo-reflections, and then it is unique up to conjugation.

Lean: not yet in Lean.

**Theorem 4.3.19 (Hirzebruch-Jung).** Let $0 < q < n$ with $\gcd(n, q) = 1$, and let $\frac1n(1,q)$ be the quotient of $\mathbb{C}^2$ by $\mu_n$ acting by $\zeta \cdot (x, y) = (\zeta x, \zeta^q y)$. Write
$$\frac{n}{q} = b_1 - \cfrac{1}{b_2 - \cfrac{1}{\ddots - \cfrac{1}{b_k}}} = [b_1, \dots, b_k], \qquad b_i \ge 2.$$
The minimal resolution of $\frac1n(1,q)$ is a chain $E_1, \dots, E_k$ of smooth rational curves with $E_i^2 = -b_i$ and $E_i \cdot E_{i+1} = 1$. The numerical discrepancies $a_i$ are the solution of
$$-b_i a_i + a_{i-1} + a_{i+1} = b_i - 2, \qquad i = 1, \dots, k,$$
with $a_0 = a_{k+1} = 0$. They lie in $(-1, 0]$. In the toric coordinates of Volume 3, where $\frac1n(1,q)$ is the cone $\operatorname{Cone}(e_2, n e_1 - q e_2)$, they are
$$a(v) = \langle m_\sigma, v \rangle - 1, \qquad m_\sigma = \Big(\frac{1 + q}{n}, 1\Big),$$
for the rays $v$ of the minimal resolution.

Lean: not yet in Lean.

**Theorem 4.3.20 (lc surface germs).** Let $(X, x)$ be a normal surface germ with $K_X$ $\mathbb{Q}$-Cartier that is lc and not klt.

1. If $K_X$ is Cartier, then $X$ is a *simple elliptic* singularity, whose minimal resolution has one smooth elliptic curve as exceptional set, or a *cusp* singularity, whose minimal resolution has a cycle of smooth rational curves, or one rational curve with a node, as exceptional set. In both cases $K_Y = f^*K_X - \sum_i E_i$.
2. In general, the index one cover of $X$ is a simple elliptic or a cusp singularity, and $X$ is its quotient by the cyclic group $\mu_r$, which acts freely outside the singular point.

Lean: not yet in Lean.

KM98, Chapter 4, and Kol13, Chapter 3, list the dual graphs of the minimal resolutions in part 2. This volume uses the theorem as a black box.

### Proof in words

Start with a klt germ of index $r$. Its index one cover is étale in codimension 1, so by Theorem 4.2.29 it is klt, and it has $K$ Cartier. A klt germ with Cartier canonical divisor has integer discrepancies above $-1$, so it is canonical, and by Section 3.2 it is a Du Val singularity $\mathbb{C}^2 / H$ with $H \subset SL_2(\mathbb{C})$. Now take the topology. The punctured germ $\mathbb{C}^2 \setminus 0$ is simply connected, so the local fundamental group of $\tilde X$ at its point is $H$, and the local fundamental group of $X$ is an extension $G$ of $\mu_r$ by $H$, a finite group. The universal cover of the punctured germ of $X$ is $\mathbb{C}^2 \setminus 0$, and $G$ acts on it holomorphically. Holomorphic functions extend over the origin by Hartogs' theorem, so $G$ acts on the germ $(\mathbb{C}^2, 0)$, with quotient $X$. Cartan's lemma linearizes a finite group action at a fixed point, so $G \subset GL_2(\mathbb{C})$.

For the cyclic quotients, the minimal resolution is toric, and Volume 3 builds it from the lattice points on the boundary of the convex hull of the nonzero lattice points of the cone. The continued fraction records the relations $v_{i-1} + v_{i+1} = b_i v_i$ among the rays, which are the self-intersections. The discrepancies then come from adjunction, or from $m_\sigma$.

### Examples

**Example 4.3.21 (the cyclic quotients $\frac1n(1,1)$ and $\frac1n(1, n-1)$).** For $q = 1$, $\frac{n}{1} = [n]$: one curve with $E^2 = -n$ and $a = -\frac{n-2}{n}$, as in Section 3.1. For $q = n - 1$, $\frac{n}{n-1} = [2, \dots, 2]$ with $n - 1$ entries: the chain $A_{n-1}$ of $(-2)$-curves, with every $a_i = 0$. Here $m_\sigma = (1, 1)$ is integral, so $K_X$ is Cartier. The action $(\zeta, \zeta^{-1})$ has determinant 1, so $\mu_n \subset SL_2(\mathbb{C})$, as the table of Section 3.2 says.

**Example 4.3.22 (the cyclic quotient $\frac17(1,3)$).** Here $\frac73 = 3 - \frac{2}{3}$ and $\frac32 = 2 - \frac12$, so $\frac73 = [3, 2, 2]$. The resolution is a chain with self-intersections $-3, -2, -2$. With $m_\sigma = (\frac47, 1)$ and the rays $(1, 0)$, $(3, -1)$, $(5, -2)$, the formula gives
$$a_1 = \frac47 - 1 = -\frac37, \qquad a_2 = \frac{12}{7} - 2 = -\frac27, \qquad a_3 = \frac{20}{7} - 3 = -\frac17.$$
Check by the linear system: $-3a_1 + a_2 = \frac97 - \frac27 = 1 = b_1 - 2$, $a_1 - 2a_2 + a_3 = -\frac37 + \frac47 - \frac17 = 0$, and $a_2 - 2a_3 = 0$. The rays satisfy $(0, 1) + (3, -1) = 3 \cdot (1, 0)$, $(1, 0) + (5, -2) = 2 \cdot (3, -1)$ and $(3, -1) + (7, -3) = 2 \cdot (5, -2)$, which recovers $[3, 2, 2]$.

**Example 4.3.23 (the index one cover of $\frac14(1,1)$).** The form $dx \wedge dy$ has weight $\zeta^2$ under $\mu_4$, so $(dx \wedge dy)^2$ is invariant and the index is 2. The subgroup of $\mu_4$ that acts with determinant 1 is $\{\pm 1\}$, and the index one cover is $\mathbb{C}^2 / \pm 1$, the $A_1$ singularity. The quotient map is $\mathbb{C}^2 / \pm 1 \to \mathbb{C}^2 / \mu_4$, of degree 2. This matches the proof: $\tilde X$ is Du Val, and $X = \tilde X / \mu_2$.

**Example 4.3.24 (a cusp).** Let the exceptional set of a resolution be a cycle of $k \ge 3$ smooth rational curves $E_i$ with $E_i^2 = -b_i$, all $b_i \ge 2$ and some $b_i \ge 3$. Exercise 5 of Section 3.1 shows that the matrix is negative definite and that every numerical discrepancy is $-1$. Such a cycle is contractible to a normal point, and when $K_X$ is $\mathbb{Q}$-Cartier the point is lc and not klt: the exceptional set is snc, and Theorem 4.2.14 applies with $\Delta_Y = \sum_i E_i$. The cone over an elliptic curve is the other case of part 1 of the theorem on lc germs, with one curve and $a = -1$.

### Proof

*Klt implies quotient (a sketch).* Let $(X, x)$ be klt of index $r$, and $\pi \colon \tilde X \to X$ the index one cover. It is étale in codimension 1, so $R = 0$ and $K_{\tilde X} = \pi^* K_X$. By Theorem 4.2.29, part 3, $\tilde X$ is klt. Its canonical divisor is Cartier, so on any resolution its discrepancies are integers, and they are greater than $-1$, so they are at least 0. So $\tilde X$ is canonical, and by Theorem 4.3.11 and Theorem 4.3.13, $\tilde X \cong \mathbb{C}^2 / H$ with $H \subset SL_2(\mathbb{C})$ finite. The rest of the proof uses two black boxes, Hartogs' extension theorem and Cartan's lemma, as described in the proof in words, and the fact that the local fundamental group of a quotient by a group with no pseudo-reflections is the group (Mum61; Bri68). The uniqueness of $G$ also comes from this fact. The converse is the theorem on quotients of Section 2.4.

*Hirzebruch-Jung.* The toric minimal resolution and the relations $v_{i-1} + v_{i+1} = b_i v_i$, with $v_0 = e_2$ and $v_{k+1} = n e_1 - q e_2$, are in Volume 3, Chapter 1, Section 4, with its Exercise 3; Example 3.1.32 treats $\frac15(1,2)$. Every $b_i$ is at least 2, so the chain has no $(-1)$-curve, and the resolution is minimal. In a smooth complete toric surface the relation $v_{i-1} + v_{i+1} = b_i v_i$ gives $E_i^2 = -b_i$, and the same holds in the resolution, which is a toric surface with the two noncompact curves $v_0$, $v_{k+1}$. Adjunction gives $K_Y \cdot E_i = b_i - 2$, and the system for $A = \sum_j a_j E_j$ is $A \cdot E_i = K_Y \cdot E_i$, which is the system in the statement. Its solution is unique by Theorem 4.3.1. For the toric form, the vector $m_\sigma$ is defined by $\langle m_\sigma, e_2 \rangle = 1$ and $\langle m_\sigma, n e_1 - q e_2 \rangle = 1$, which give $m_2 = 1$ and $n m_1 - q = 1$. So $m_\sigma = (\frac{1+q}{n}, 1)$, and Volume 3, Theorem 3.3.34, gives $a(v) = \langle m_\sigma, v \rangle - 1$. Every $a_i$ is at most 0 by Proposition 4.3.5, and greater than $-1$ since $\langle m_\sigma, v \rangle > 0$ on the interior of $\sigma$.

*Lc germs.* This is a black box (KM98, Chapter 4; Kol13, Chapter 3). The reduction of part 2 to part 1 follows the same steps as the klt case: the index one cover is lc by Theorem 4.2.29, it is not klt by the same theorem, and it has Cartier canonical divisor. Part 1 then comes from the classification of the minimal resolutions with $K_Y = f^*K_X - \sum_i E_i$, by adjunction on the exceptional curves. $\square$

### Exercises

1. (A) Compute the continued fraction of $\frac72$ and the discrepancies of $\frac17(1,2)$. Check the answer by the toric formula.
2. (A) Show that $\frac15(1,2) \cong \frac15(1,3)$ by exchanging the coordinates and replacing $\zeta$ by $\zeta^3$. Check that $\frac53 = [2, 3]$ is $\frac52 = [3, 2]$ in reverse order.
3. (B) Show that the index of $\frac1n(1,q)$ is $\frac{n}{\gcd(n, 1+q)}$, and that its index one cover is the $A_{d-1}$ singularity $\frac1d(1, -1)$ with $d = \gcd(n, 1+q)$, smooth when $d = 1$.
4. (B) Show that the discrepancies $a_i$ of $\frac1n(1,q)$ satisfy $n a_i \in \mathbb{Z}$, and that the minimum of the $a_i$ tends to $-1$ along $\frac1n(1,1)$ as $n \to \infty$.
5. (C) Let $X$ be klt of index $r$ and $\pi \colon \tilde X \to X$ the index one cover. Show that the discrepancies of $X$ satisfy $A(E) = \frac1e A(\tilde E)$, where $\tilde E$ lies over $E$ with ramification index $e$ dividing $r$. Deduce in a second way that $r \cdot a(E) \in \mathbb{Z}$ for every divisor $E$ over $X$, and check this on $\frac17(1,3)$.

### Lean

The theorems of this section are not yet in Lean. The library has no local fundamental group, no finite group actions, and no toric surfaces in the form used here. Volume 3 describes the Lean status of the toric computation.

### Notes and history

Hirzebruch resolved the cyclic quotients by continued fractions in 1953, after Jung's work on the resolution of surfaces. Brieskorn (Bri68) classified the finite subgroups of $GL_2(\mathbb{C})$ with no pseudo-reflections and the quotient singularities of surfaces. The characterization of klt surface germs as quotients is in KM98, Chapter 4. The classification of the lc surface germs goes back to the 1980s, and KM98, Chapter 4, and Kol13, Chapter 3, give modern treatments, the second with a boundary. The same strategy, index one cover first and then a classification of the Gorenstein case, is the strategy of Chapter 4 for terminal 3-fold singularities.
