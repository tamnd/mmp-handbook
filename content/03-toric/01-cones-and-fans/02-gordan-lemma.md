---
title: Gordan's lemma and the semigroup of a cone
nodes: []
sources: [CLS11, Ful93]
reads_with: [CLS11:ch1, Ful93:1.2]
requires: [P8.6, 3.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Gordan's lemma and the semigroup of a cone

### Statement

**Definition 3.1.9.** An *affine semigroup* is a finitely generated subsemigroup $S \subseteq M$ with $0 \in S$. Its *semigroup algebra* $k[S]$ is the $k$-vector space with basis $\{\chi^m : m \in S\}$ and the product $\chi^m \chi^{m'} = \chi^{m + m'}$. It is a subalgebra of the Laurent polynomial ring $k[M]$. A subsemigroup $S \subseteq M$ is *saturated* if $km \in S$ with $k \ge 1$ and $m \in M$ gives $m \in S$. For a rational polyhedral cone $\sigma \subset N_{\mathbb{R}}$, put

$$S_\sigma = \sigma^\vee \cap M.$$

Lean: not yet in Lean.

**Theorem 3.1.10 (Gordan's lemma).** Let $\sigma \subset N_{\mathbb{R}}$ be a rational polyhedral cone. Then $S_\sigma$ is a finitely generated semigroup.

Lean: not yet in Lean.

**Proposition 3.1.11.** Let $\sigma$ be a rational polyhedral cone.

1. $S_\sigma$ is saturated.
2. $S_\sigma$ generates $M$ as a group if and only if $\sigma$ is strongly convex.

Lean: not yet in Lean.

**Proposition 3.1.12 (Hilbert basis).** Let $\sigma$ be a rational polyhedral cone of dimension $n$. Call $m \in S_\sigma \setminus \{0\}$ *irreducible* if $m = m' + m''$ with $m', m'' \in S_\sigma$ gives $m' = 0$ or $m'' = 0$. Then the set $\mathcal{H}$ of irreducible elements is finite, it generates $S_\sigma$, and it is contained in every generating set of $S_\sigma$. It is the *Hilbert basis* of $S_\sigma$.

Lean: not yet in Lean.

The same results hold for $\sigma \cap N$ in place of $\sigma^\vee \cap M$, since $\sigma = (\sigma^\vee)^\vee$ is itself the dual of a rational cone. Section 4 uses the Hilbert basis of $\sigma \cap N$ to resolve surface singularities.

### Proof in words

The cone $\sigma^\vee$ is spanned by finitely many lattice points $m_1, \dots, m_s$, by Theorem 3.1.3. Every lattice point of $\sigma^\vee$ is an integer combination of the $m_i$ plus a lattice point of the half-open box $\{\sum \lambda_i m_i : 0 \le \lambda_i < 1\}$. The box is bounded, so it has finitely many lattice points, and these together with the $m_i$ generate. The difficulty is only that the $m_i$ alone do not generate in general: the lattice points of the box are needed, as Example 3.1.14 shows.

For the Hilbert basis, a cone of full dimension has a dual cone that is strongly convex. So there is a lattice point $u$ of $\sigma$ that is positive on $S_\sigma \setminus \{0\}$, and $\langle \cdot, u \rangle$ is a degree with values in $\mathbb{Z}_{\ge 0}$. Induction on the degree writes each element as a sum of irreducible ones, and an irreducible element cannot be a sum of other elements of a generating set.

### Examples

**Example 3.1.13 (the orthant).** For $\sigma = \operatorname{Cone}(e_1, \dots, e_n)$, $S_\sigma = \mathbb{Z}_{\ge 0}^n$ in the dual basis. The Hilbert basis is $e_1^*, \dots, e_n^*$, and $k[S_\sigma] = k[x_1, \dots, x_n]$ with $x_i = \chi^{e_i^*}$. For a face $\operatorname{Cone}(e_1, \dots, e_r)$ of dimension $r < n$, the semigroup is $\mathbb{Z}_{\ge 0}^r \times \mathbb{Z}^{n-r}$ and the algebra is $k[x_1, \dots, x_r, x_{r+1}^{\pm 1}, \dots, x_n^{\pm 1}]$. Proposition 3.1.12 does not apply to it, and indeed a group $\mathbb{Z}^{n-r}$ has no irreducible elements.

**Example 3.1.14 (the cone $\sigma_n$).** By Example 3.1.6, $S_{\sigma_n} = \{(a, b) \in \mathbb{Z}^2 : 0 \le b \le na\}$. The generators of $\sigma_n^\vee$ are $(1, 0)$ and $(1, n)$, but for $n \ge 2$ they do not generate $S_{\sigma_n}$: the point $(1, 1)$ is not a sum of them. The Hilbert basis is

$$\mathcal{H} = \{(1, 0), (1, 1), \dots, (1, n)\}.$$

Each $(1, j)$ is irreducible, because a point of $S_{\sigma_n} \setminus 0$ has $a \ge 1$, and so a sum of two such points has $a \ge 2$. They generate: let $(a, b) \in S_{\sigma_n}$ with $a \ge 2$. Write $b = j + b'$ with $0 \le j \le n$ and $0 \le b' \le n(a-1)$, which is possible since $0 \le b \le na$. Then $(a, b) = (1, j) + (a - 1, b')$ and induction on $a$ ends the proof. So $k[S_{\sigma_n}] = k[x, xy, xy^2, \dots, xy^n]$ with $x = \chi^{e_1^*}$, $y = \chi^{e_2^*}$. For $n = 2$ put $u = x$, $v = xy$, $w = xy^2$. Then $uw = v^2$, and $k[S_{\sigma_2}] \cong k[u, v, w]/(uw - v^2)$, the coordinate ring of the quadric cone.

**Example 3.1.15 (the cone over a square).** For the cone $\sigma$ of Example 3.1.7, $\sigma^\vee$ is spanned by $m_1 = (1,0,0)$, $m_2 = (0,1,0)$, $m_3 = (-1,0,1)$, $m_4 = (0,-1,1)$. The four vectors lie on the plane $x + y + 2z = 1$, and $\det(m_1, m_2, m_3) = 1$. So the triangles $m_1 m_2 m_3$ and $m_1 m_3 m_4$ are unimodular, and every lattice point of $\sigma^\vee$ is a nonnegative integer combination of the vertices of one of them. The Hilbert basis is $\{m_1, m_2, m_3, m_4\}$. Write $x, y, z, w$ for the four characters. The relation $m_1 + m_3 = m_2 + m_4$ gives $xz = yw$. Chapter 2 proves that $k[S_\sigma] = k[x, y, z, w]/(xz - yw)$.

**Example 3.1.16 (an irrational cone).** The rationality in Theorem 3.1.10 is needed. Let $\tau = \operatorname{Cone}((0, 1), (\sqrt2, -1)) \subset \mathbb{R}^2$. Then $\tau \cap \mathbb{Z}^2$ is not finitely generated. Suppose that $g_1, \dots, g_s$ generate it. Then $\tau \cap \mathbb{Z}^2 \subseteq \operatorname{Cone}(g_1, \dots, g_s)$, a rational cone. Its boundary rays are rational, so they differ from the ray of $(\sqrt2, -1)$, and there is an open sector of $\tau$ along that ray which the cone of the $g_i$ misses. This sector contains lattice points. For $q \ge 1$ the point $(\lceil q\sqrt2 \rceil, -q)$ lies in $\tau$, and its distance to the line of $(\sqrt2, -1)$ is less than $1$, so its direction tends to that ray as $q$ grows. This is a contradiction. In the language of this section, $\tau = \sigma^\vee$ for the irrational cone $\sigma = \operatorname{Cone}((1, 0), (1, \sqrt2))$.

### Proof

*Proof of Theorem 3.1.10.* By Theorem 3.1.3, $\sigma^\vee = \operatorname{Cone}(m_1, \dots, m_s)$ with $m_i \in M$. Let $K = \{\sum_i \lambda_i m_i : 0 \le \lambda_i < 1\}$. It is a bounded set, so $K \cap M$ is finite. Let $m \in S_\sigma$ and write $m = \sum_i \lambda_i m_i$ with $\lambda_i \ge 0$. Then $m = \sum_i \lfloor \lambda_i \rfloor m_i + m'$, where $m' = \sum_i (\lambda_i - \lfloor \lambda_i \rfloor) m_i$ lies in $K$ and in $M$, because $m$ and the $m_i$ are in $M$. So $(K \cap M) \cup \{m_1, \dots, m_s\}$ generates $S_\sigma$. $\square$

*Proof of Proposition 3.1.11.* Part 1: if $km \in \sigma^\vee$ with $k \ge 1$ then $m \in \sigma^\vee$, since $\sigma^\vee$ is a cone. Part 2: suppose $\sigma$ is strongly convex. By Theorem 3.1.3, $\sigma^\vee$ has dimension $n$, so it has an interior point, and then also an interior lattice point $m_0$. For $m \in M$ the point $m + k m_0$ lies in $\sigma^\vee$ for large $k$, so $m = (m + km_0) - km_0$ is a difference of elements of $S_\sigma$. Conversely, if $S_\sigma$ generates $M$, then $\sigma^\vee$ spans $M_{\mathbb{R}}$, so $\dim \sigma^\vee = n$, and $\sigma$ is strongly convex by Theorem 3.1.3. $\square$

*Proof of Proposition 3.1.12.* Since $\dim \sigma = n$, the cone $\sigma$ has an interior point, and so an interior lattice point $u$. For $m \in \sigma^\vee \setminus \{0\}$, $\langle m, u \rangle > 0$: otherwise $m$ vanishes at an interior point and is nonnegative on a neighbourhood of it, so $m = 0$. Put $\deg m = \langle m, u \rangle \in \mathbb{Z}_{\ge 0}$ for $m \in S_\sigma$. It is additive, and it is $0$ only at $m = 0$. Induction on the degree shows that each $m \in S_\sigma \setminus 0$ is a sum of irreducible elements: if $m$ is not irreducible, $m = m' + m''$ with both terms of smaller degree. So $\mathcal{H}$ generates. Let $G$ be any generating set and $m \in \mathcal{H}$. Then $m$ is a sum of elements of $G \setminus 0$, and since it is irreducible the sum has one term, so $m \in G$. With $G$ finite (Theorem 3.1.10), $\mathcal{H}$ is finite. $\square$

The semigroup algebra has a presentation by binomials. If $m_1, \dots, m_s$ generate $S_\sigma$, the map $k[x_1, \dots, x_s] \to k[S_\sigma]$, $x_i \mapsto \chi^{m_i}$, is onto, and its kernel is spanned by the binomials $x^a - x^b$ with $\sum a_i m_i = \sum b_i m_i$ (Cox-Little-Schenck, Chapter 1). This is the toric ideal of the generators.

### Exercises

1. (A) Find the Hilbert basis of $S_\sigma$ for $\sigma = \operatorname{Cone}(e_1, e_1 + 2 e_2) \subset \mathbb{R}^2$, and the relations between its elements.
2. (A) Show that the semigroup $\mathbb{Z}_{\ge 0} \cdot 2 + \mathbb{Z}_{\ge 0} \cdot 3 \subset \mathbb{Z}$ is an affine semigroup that is not saturated. Show that it is not $S_\sigma$ for any cone $\sigma \subset \mathbb{R}$.
3. (A) Let $\sigma = \operatorname{Cone}(e_2, n e_1 - q e_2)$ with $0 < q < n$ and $\gcd(n, q) = 1$. Compute $\sigma^\vee$.
4. (B) For the cone of Exercise 3 with $(n, q) = (5, 2)$, find the Hilbert basis of $S_\sigma$. Compare its size with the case $(n, q) = (5, 1)$ of Example 3.1.14.
5. (B) Show that the toric ideal of the Hilbert basis of Example 3.1.14 is generated by the $2 \times 2$ minors of the matrix with rows $(z_0, z_1, \dots, z_{n-1})$ and $(z_1, z_2, \dots, z_n)$, with $z_j = xy^j$.
6. (B) Let $\sigma$ be a rational polyhedral cone that is not of full dimension. Show that $S_\sigma \cong S' \times \mathbb{Z}^{n - \dim \sigma}$ for a semigroup $S'$ that has a Hilbert basis.

### Lean

There is no Lean form of the dual semigroup or of Gordan's lemma yet. The Lean cones of this volume live in $\mathbb{R}^n$, and the semigroup algebra $k[S_\sigma]$ needs the dual lattice and the monoid algebra of Mathlib.

- Status: not yet in Lean.
- Fidelity: none to record.
- No node of the map covers this section.

### Notes and history

Gordan proved the lemma in 1873, in work on the invariants of binary forms, and it is a theorem. The name Hilbert basis comes from the theory of linear Diophantine inequalities and integer programming. The proof by the half-open box is the standard one (Fulton, Section 1.2). The toric ideal of an affine semigroup is a prime ideal generated by binomials, and Sturmfels' book on Gröbner bases and convex polytopes studies these ideals. Exercise 4 is the first case of the Hirzebruch-Jung continued fraction of Section 4.
