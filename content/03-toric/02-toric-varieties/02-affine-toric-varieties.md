---
title: The affine toric variety of a cone
nodes: []
sources: [CLS11, Ful93]
reads_with: [CLS11:ch1, Ful93:1.3, Ful93:2.1]
requires: [P8.6, 3.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The affine toric variety of a cone

### Statement

**Definition 3.2.10 (the affine toric variety $U_\sigma$).** Let $\sigma \subset N_{\mathbb{R}}$ be a strongly convex rational polyhedral cone and $S_\sigma = \sigma^\vee \cap M$ (Definition 3.1.9). The *affine toric variety of $\sigma$* is $U_\sigma = \operatorname{Spec} k[S_\sigma]$, where $k[S_\sigma] \subset k[M]$ is the semigroup algebra. A $k$-point of $U_\sigma$ is the same as a homomorphism of semigroups $S_\sigma \to (k, \cdot)$ that sends $0$ to $1$.

**Theorem 3.2.11 (normality).** $U_\sigma$ is a normal affine toric variety of dimension $n$ with torus $T_N$. Every normal affine toric variety with torus $T_N$ is isomorphic to $U_\sigma$ for a unique strongly convex rational polyhedral cone $\sigma \subset N_{\mathbb{R}}$, by an isomorphism that is the identity on $T_N$.

Lean: not yet in Lean.

**Proposition 3.2.12 (faces give open sets).** Let $\tau$ be a face of $\sigma$, and let $m \in S_\sigma$ with $\tau = \sigma \cap m^\perp$. Such an $m$ exists: any lattice point in the relative interior of the rational face $\tau^* = \sigma^\vee \cap \tau^\perp$ of Proposition 3.1.4 works. Then

$$S_\tau = S_\sigma + \mathbb{Z}_{\ge 0} (-m), \qquad k[S_\tau] = k[S_\sigma]_{\chi^m},$$

and the inclusion $k[S_\sigma] \subset k[S_\tau]$ makes $U_\tau$ the principal open subset $\{\chi^m \neq 0\}$ of $U_\sigma$. For $\tau = \{0\}$ this is the torus $T_N \subset U_\sigma$.

Lean: not yet in Lean.

**Theorem 3.2.13 (smoothness).** Let $\dim \sigma = k$. The following are equivalent.

1. $U_\sigma$ is smooth.
2. $\sigma$ is smooth (Definition 3.1.19).
3. $U_\sigma \cong \mathbb{A}^k \times (k^*)^{n-k}$.

Lean: not yet in Lean.

### Proof in words

The dual cone is the intersection of the half-spaces $\{\langle m, u_\rho \rangle \ge 0\}$ for the rays $\rho$ of $\sigma$. So $k[S_\sigma]$ is the intersection of the rings of these half-spaces. Each of them is a polynomial ring in one variable over a Laurent polynomial ring, and an intersection of normal domains with one fraction field is normal. The torus is the open set where a character from the interior of $\sigma^\vee$ does not vanish.

For smoothness, a smooth cone is the orthant in a suitable basis, and its chart is visibly $\mathbb{A}^k \times (k^*)^{n-k}$. For the converse, split off the torus factor and reduce to a cone of full dimension. Then $U_\sigma$ has a distinguished fixed point, at which every nonconstant character vanishes. The cotangent space at this point has a basis given by the Hilbert basis of $S_\sigma$. If $U_\sigma$ is smooth, the Hilbert basis has $n$ elements, so it is a basis of $M$, and the cone is smooth.

### Examples

**Example 3.2.14 (affine space).** For the orthant $\sigma = \operatorname{Cone}(e_1, \dots, e_n)$, $\sigma^\vee$ is the orthant of $M_{\mathbb{R}}$, $S_\sigma = \mathbb{N}^n$ and $U_\sigma = \mathbb{A}^n$. For $\sigma = \operatorname{Cone}(e_1, \dots, e_k)$ with $k < n$, $S_\sigma = \mathbb{N}^k \times \mathbb{Z}^{n-k}$ and $U_\sigma = \mathbb{A}^k \times (k^*)^{n-k}$. The faces $\operatorname{Cone}(e_i : i \in I)$ of the orthant give the open sets $\{x_j \neq 0 \text{ for } j \notin I\}$ of $\mathbb{A}^n$, as Proposition 3.2.12 says with $m = \sum_{j \notin I} e_j^*$.

**Example 3.2.15 (the cone of $\frac1n(1,1)$).** Let $\sigma_n = \operatorname{Cone}(e_2, n e_1 - e_2)$ with $n \ge 2$. By Example 3.1.14 the Hilbert basis of $S_{\sigma_n}$ is $\{(1, j) : 0 \le j \le n\}$. Put $x = \chi^{(1,0)}$ and $y = \chi^{(0,1)}$. Then

$$k[S_{\sigma_n}] = k[x, xy, xy^2, \dots, xy^n],$$

and $U_{\sigma_n}$ is the cone over the rational normal curve of degree $n$ of Example 3.2.7. There is a second description. Let $\mu_n$ act on $\mathbb{A}^2 = \operatorname{Spec} k[a, b]$ by $\zeta \cdot (a, b) = (\zeta a, \zeta b)$, with $\operatorname{char} k \nmid n$. The invariant ring is spanned by the monomials $a^i b^j$ with $n \mid i + j$. The map $(c, d) \mapsto a^{nc - d} b^d$ is an isomorphism of semigroups from $S_{\sigma_n} = \{(c, d) : 0 \le d \le nc\}$ to these monomials. So $U_{\sigma_n} \cong \mathbb{A}^2 / \mu_n$, the quotient singularity $\frac1n(1,1)$. For $n = 2$ it is the quadric cone $xz = y^2$. By Theorem 3.2.13 it is singular for $n \ge 2$, since $\operatorname{mult}(\sigma_n) = n$.

**Example 3.2.16 (the cone over a square).** Let $\sigma$ be the cone of Example 3.1.7. By Example 3.1.15 the Hilbert basis of $S_\sigma$ is $m_1 = (1,0,0)$, $m_2 = (0,1,0)$, $m_3 = (-1,0,1)$, $m_4 = (0,-1,1)$, with the relation $m_1 + m_3 = m_2 + m_4$. Put $x, y, z, w = \chi^{m_1}, \chi^{m_2}, \chi^{m_3}, \chi^{m_4}$. Then

$$k[S_\sigma] \cong k[x, y, z, w] / (xz - yw).$$

The proof: the ring on the right is a domain of dimension 3, since $xz - yw$ is irreducible. It maps onto $k[S_\sigma]$, which is a domain of dimension 3. A surjection of domains of the same finite dimension is an isomorphism, because its kernel is a prime ideal of height 0. So $U_\sigma$ is the affine cone over the smooth quadric surface, the base of the Atiyah flop. Each proper face of $\sigma$ is smooth: for example $u_1, u_2$ and $e_2$ form a basis of $\mathbb{Z}^3$. By Proposition 3.2.12 the open sets $U_\tau$ for the proper faces $\tau$ are smooth. Section 4 shows that they cover $U_\sigma$ minus the vertex, so the vertex is the only singular point.

**Example 3.2.17 (strong convexity is needed).** Let $\sigma = \mathbb{R} e_1 \subset \mathbb{R}^2$, a line and not a strongly convex cone. Then $\sigma^\vee = \mathbb{R} e_2^*$ and $k[\sigma^\vee \cap M] = k[y^{\pm 1}]$, whose spectrum has dimension 1. It does not contain the torus $(k^*)^2$. This is why Definition 3.2.10 asks for strong convexity, and why Proposition 3.1.11 matters: $S_\sigma$ generates $M$ as a group exactly when $\sigma$ is strongly convex.

### Proof

*Proof of Theorem 3.2.11.* By Gordan's lemma (Theorem 3.1.10), $S_\sigma$ is finitely generated, so $k[S_\sigma]$ is a finitely generated $k$-algebra. It is a domain, as a subring of $k[M]$. Since $\sigma$ is strongly convex, $\sigma^\vee$ has dimension $n$, so there is $m_0 \in M$ in the interior of $\sigma^\vee$. For each $m \in M$ the point $m + p m_0$ lies in $\sigma^\vee$ for $p \gg 0$, so $k[S_\sigma]_{\chi^{m_0}} = k[M]$. So $T_N$ is the principal open set $\{\chi^{m_0} \neq 0\}$ of $U_\sigma$, and $\dim U_\sigma = n$. The comorphism $\chi^m \mapsto \chi^m \otimes \chi^m$ maps $k[S_\sigma]$ into $k[S_\sigma] \otimes k[M]$. So it defines an action $T_N \times U_\sigma \to U_\sigma$ that extends the multiplication of $T_N$.

For normality, let $u_\rho$ be the minimal generators of the rays of $\sigma$. By duality (Theorem 3.1.3), $\sigma^\vee = \bigcap_\rho H_\rho$ with $H_\rho = \{m : \langle m, u_\rho \rangle \ge 0\}$. A Laurent polynomial lies in $k[S]$ for a subset $S \subset M$ exactly when all its exponents lie in $S$. So $k[S_\sigma] = \bigcap_\rho k[H_\rho \cap M]$ inside $k[M]$. Since $u_\rho$ is primitive, it extends to a basis of $N$. In the dual basis $H_\rho \cap M = \mathbb{Z}_{\ge 0} \times \mathbb{Z}^{n-1}$, and $k[H_\rho \cap M] \cong k[x_1, x_2^{\pm 1}, \dots, x_n^{\pm 1}]$. This ring is a localization of a polynomial ring, so it is normal. All these rings have the fraction field $k(M)$, and an intersection of normal domains with one fraction field is normal. If $\sigma = \{0\}$, $k[S_\sigma] = k[M]$, which is normal. The converse statement is cited without proof (Cox-Little-Schenck, Chapter 1). Its proof writes the coordinate ring as $k[S]$ for a finitely generated semigroup $S \subset M$, and shows that normality forces $S$ to be saturated, so that $S = \sigma^\vee \cap M$ with $\sigma^\vee = \operatorname{Cone}(S)$. $\square$

*Proof of Proposition 3.2.12.* Since $-m$ vanishes on $\tau$, $-m \in \tau^\vee$, and $S_\sigma \subset S_\tau$ because $\tau \subset \sigma$. So $S_\sigma + \mathbb{Z}_{\ge 0}(-m) \subset S_\tau$. Conversely, let $m' \in S_\tau$ and let $u_1, \dots, u_r$ generate $\sigma$. For $u_i \in \tau$, $\langle m', u_i \rangle \ge 0$ and $\langle m, u_i \rangle = 0$. For $u_i \notin \tau$, $\langle m, u_i \rangle > 0$. So there is an integer $p \ge 0$ with $\langle m' + p m, u_i \rangle \ge 0$ for all $i$. Then $m' + p m \in S_\sigma$ and $m' = (m' + pm) + p(-m)$. So $S_\tau = S_\sigma + \mathbb{Z}_{\ge 0}(-m)$, and on the rings this says $k[S_\tau] = k[S_\sigma][\chi^{-m}] = k[S_\sigma]_{\chi^m}$. $\square$

*Proof of Theorem 3.2.13.* Suppose that $\sigma$ is smooth, with minimal generators $u_1, \dots, u_k$. Extend them to a basis $u_1, \dots, u_n$ of $N$ and let $m_1, \dots, m_n$ be the dual basis. Then $\sigma^\vee$ is generated by $m_1, \dots, m_k$ and $\pm m_{k+1}, \dots, \pm m_n$, so $S_\sigma = \mathbb{N}^k \times \mathbb{Z}^{n-k}$ and $U_\sigma \cong \mathbb{A}^k \times (k^*)^{n-k}$. This proves that 2 implies 3, and 3 implies 1 is clear.

Suppose that $U_\sigma$ is smooth. The lattice $N_\sigma = \operatorname{span}(\sigma) \cap N$ is saturated, so $N = N_\sigma \oplus N'$ for some $N'$. With the dual splitting $M = M_\sigma \oplus M'$, the dual of $\sigma$ in $M_{\mathbb{R}}$ is the product of its dual in $(M_\sigma)_{\mathbb{R}}$ and all of $M'_{\mathbb{R}}$. So $U_\sigma \cong U_{\sigma, N_\sigma} \times T_{N'}$, and $U_{\sigma, N_\sigma}$ is smooth, since a product $X \times T$ with a torus $T$ is smooth exactly when $X$ is. So one may assume $\dim \sigma = n$. Then $\sigma^\vee$ is strongly convex, so a sum of two nonzero elements of $S_\sigma$ is nonzero. Hence $m \mapsto 1$ for $m = 0$ and $m \mapsto 0$ for $m \neq 0$ is a homomorphism of semigroups, and so a point $x_\sigma \in U_\sigma$. Its maximal ideal $\mathfrak{m}$ is spanned by the $\chi^m$ with $m \neq 0$, and $\mathfrak{m}^2$ is spanned by the $\chi^{m + m'}$ with $m, m' \neq 0$. So $\mathfrak{m}/\mathfrak{m}^2$ has a basis given by the irreducible elements of $S_\sigma$, which form the Hilbert basis $\mathcal{H}$ (Proposition 3.1.12). Smoothness at $x_\sigma$ gives $|\mathcal{H}| = \dim \mathfrak{m}/\mathfrak{m}^2 = n$. The set $\mathcal{H}$ generates $S_\sigma$, and $S_\sigma$ generates $M$ as a group (Proposition 3.1.11). So $\mathcal{H}$ is a set of $n$ elements that generates $M \cong \mathbb{Z}^n$, and so it is a basis. Then $\sigma^\vee = \operatorname{Cone}(\mathcal{H})$ is smooth, and $\sigma = (\sigma^\vee)^\vee$ is generated by the dual basis, so $\sigma$ is smooth. $\square$

### Exercises

1. (A) Let $\sigma = \operatorname{Cone}(e_1, e_1 + 2 e_2) \subset \mathbb{R}^2$. Find $S_\sigma$, its Hilbert basis and the equation of $U_\sigma$. Which known surface is it?
2. (A) For each face $\tau$ of the cone over a square, find $m \in S_\sigma$ with $\tau = \sigma \cap m^\perp$, and describe $U_\tau$ as an open subset of $xz = yw$.
3. (B) Let $0 < q < n$ with $\gcd(n, q) = 1$, and let $\operatorname{char} k \nmid n$. Show that $U_\sigma$ for $\sigma = \operatorname{Cone}(e_2, n e_1 - q e_2)$ is the quotient of $\mathbb{A}^2$ by $\zeta \cdot (a, b) = (\zeta a, \zeta^q b)$.
4. (B) Show that the embedding dimension of $U_\sigma$ at the point $x_\sigma$ of the proof of Theorem 3.2.13 is the number of elements of the Hilbert basis of $S_\sigma$, when $\dim \sigma = n$. Compute it for $\frac15(1,2)$.
5. (C) Use the Jacobian criterion to show directly that $xz = yw$ is singular only at the origin, and that the cone over the rational normal curve of degree $n \ge 2$ is singular only at the vertex.

### Lean

- Status: not yet in Lean. The Lean library has cones with lattice generators (`MinimalModel.Toric.latticeCone`) and strong convexity (`MinimalModel.Toric.IsStronglyConvex`), which are the hypotheses of Definition 3.2.10. It has no dual cone, no semigroup $S_\sigma$, no semigroup algebra and no scheme $U_\sigma$ yet.
- Fidelity: the Lean notion of a smooth cone is still missing; `MinimalModel.Toric.IsSimplicial` is the closest notion in Lean.
- No node of the map covers this section.

### Notes and history

The normality criterion and the smoothness criterion are in Kempf, Knudsen, Mumford and Saint-Donat (1973) and in Oda's book. The argument with the cotangent space at the fixed point follows Cox-Little-Schenck, Chapter 1. Hochster (1972) proved more: the ring $k[S_\sigma]$ is Cohen-Macaulay. Chapter 3 uses this to identify the toric varieties with Cartier canonical divisor as the Gorenstein ones. The quotient description of Example 3.2.15 is the start of the study of cyclic quotient singularities, which Volume 4 of this handbook takes up.
