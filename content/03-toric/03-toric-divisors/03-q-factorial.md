---
title: Q-factorial means simplicial
nodes: []
sources: [CLS11, FS04, KM98]
reads_with: [CLS11:ch4, KM98:ch2]
requires: [P8.6, P8.7, 3.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## $\mathbb{Q}$-factorial means simplicial

### Statement

**Definition 3.3.19 ($\mathbb{Q}$-Cartier, $\mathbb{Q}$-factorial).** A Weil divisor $D$ on a normal variety $X$ is *$\mathbb{Q}$-Cartier* if $rD$ is Cartier for some integer $r \ge 1$. The variety $X$ is *$\mathbb{Q}$-factorial* if every Weil divisor on $X$ is $\mathbb{Q}$-Cartier.

**Theorem 3.3.20 ($\mathbb{Q}$-factorial means simplicial).** Let $\Sigma$ be a fan. Then $X_\Sigma$ is $\mathbb{Q}$-factorial if and only if $\Sigma$ is simplicial. More precisely, let $D = \sum_\rho a_\rho D_\rho$.

1. $D$ is $\mathbb{Q}$-Cartier if and only if for each $\sigma \in \Sigma$ there is $m_\sigma \in M_{\mathbb{Q}}$ with $\langle m_\sigma, u_\rho \rangle = -a_\rho$ for all $\rho \in \sigma(1)$.
2. If $\sigma$ is simplicial, then $\operatorname{mult}(\sigma) \cdot D$ is Cartier on $U_\sigma$.
3. If $\Sigma$ is simplicial, then $\operatorname{Pic}(X_\Sigma) \otimes \mathbb{Q} = \operatorname{Cl}(X_\Sigma) \otimes \mathbb{Q}$, and $r D$ is Cartier for every $D$, where $r$ is the least common multiple of the multiplicities of the cones.

Lean: on the fan, part 1 is `MinimalModel.Toric.Fan.isQCartier_iff`, where `MinimalModel.Toric.Fan.IsQCartier` says that a positive multiple of $D$ has Cartier data. Parts 2 and 3 and the equivalence with $\mathbb{Q}$-factoriality are not yet in Lean.

**Corollary 3.3.21.** A smooth fan gives a factorial variety, and a fan in $\mathbb{R}^2$ always gives a $\mathbb{Q}$-factorial surface. The affine toric variety $U_\sigma$ is $\mathbb{Q}$-factorial if and only if $\sigma$ is simplicial, and then $\operatorname{Cl}(U_\sigma)$ is finite.

Lean: `MinimalModel.Toric.Fan.IsSimplicialFan` is the simplicial condition on a fan; the corollary itself is not yet in Lean.

The minimal model program in the sense of Kollár-Mori works with $\mathbb{Q}$-factorial varieties, so the toric MMP works with simplicial fans. Theorem 3.3.20 is the dictionary entry that makes this possible, and the fact that flips stay inside simplicial fans is the reason why the toric MMP of the later chapters never leaves the toric world.

### Proof in words

By Theorem 3.3.12 applied to $rD$, $D$ is $\mathbb{Q}$-Cartier when the linear equations $\langle m_\sigma, u_\rho \rangle = -a_\rho$, $\rho \in \sigma(1)$, have a rational solution on each cone. If $\sigma$ is simplicial, the $u_\rho$ are linearly independent, so these equations have a rational solution for every choice of the $a_\rho$, and the denominators divide $\operatorname{mult}(\sigma)$. If $\sigma$ is not simplicial, it has more rays than its dimension. Then the map $M_{\mathbb{Q}} \to \mathbb{Q}^{\sigma(1)}$, $m \mapsto (\langle m, u_\rho \rangle)_\rho$, has rank $\dim \sigma < |\sigma(1)|$, so it is not onto. Some coordinate vector, which is the coefficient vector of a single $D_\rho$, is not in its image, and that $D_\rho$ is not $\mathbb{Q}$-Cartier.

### Examples

**Example 3.3.22 (the cone of $\frac1n(1,1)$ and $\mathbb{P}(1,1,n)$).** The cone $\sigma_n$ is simplicial of multiplicity $n$. So $U_{\sigma_n}$ is $\mathbb{Q}$-factorial, and $n D$ is Cartier for every $D$, as Example 3.3.16 found by hand. The fan of $\mathbb{P}(1,1,n)$ is simplicial with multiplicities $n, 1, 1$, so $\mathbb{P}(1,1,n)$ is $\mathbb{Q}$-factorial and $n D$ is Cartier for every $D$. Here $r = n$ is the least possible: $D_1$ is not Cartier for $n \ge 2$ (Example 3.3.17).

**Example 3.3.23 (the cone over a square is not $\mathbb{Q}$-factorial).** The cone $\sigma$ of Example 3.1.7 has 4 rays in dimension 3, so it is not simplicial. Example 3.3.18 shows that the plane $D_1 = \{z = w = 0\}$ is not $\mathbb{Q}$-Cartier. Its two smooth refinements $\Sigma_+$ and $\Sigma_-$ (Example 3.1.33) give small resolutions $X_{\Sigma_\pm} \to U_\sigma$, each with exceptional locus a curve $C_\pm \cong \mathbb{P}^1$. On $X_{\Sigma_+}$ the divisor $D_1$ is Cartier, since $X_{\Sigma_+}$ is smooth. This is the pattern of a flip or a flop: a small contraction $X_{\Sigma_+} \to U_\sigma$ from a $\mathbb{Q}$-factorial variety has a target that is not $\mathbb{Q}$-factorial, so the MMP cannot stop at $U_\sigma$, and it passes to the other side $X_{\Sigma_-}$.

**Example 3.3.24 (the terminal quotient $\frac12(1,1,1)$).** Let $N = \mathbb{Z}^3 + \mathbb{Z} \cdot \frac12(1,1,1)$ and $\sigma = \operatorname{Cone}(e_1, e_2, e_3)$, as in Example 3.1.34. The cone is simplicial of multiplicity 2, so $U_\sigma$ is $\mathbb{Q}$-factorial and $2D$ is Cartier for every $D$. The dual lattice is $M = \{m \in \mathbb{Z}^3 : m_1 + m_2 + m_3 \text{ is even}\}$, so the divisor $D_1$ of the ray $e_1$ is Cartier only if some $m \in M$ has $m_1 = -1$ and $m_2 = m_3 = 0$, which fails. So $\operatorname{Cl}(U_\sigma) = \mathbb{Z}/2$, generated by $D_1$, and $U_\sigma$ is $\mathbb{Q}$-factorial but not factorial. As a variety it is $\mathbb{A}^3 / \mu_2$ with $\mu_2$ acting by $-1$, when $\operatorname{char} k \neq 2$.

**Example 3.3.25 (a complete simplicial fan that is not smooth).** Let $\Sigma$ be the fan in $\mathbb{R}^3$ with rays $e_1$, $e_2$, $e_3$, $-e_1 - e_2 - 2 e_3$ and the four cones spanned by three of the rays. It is simplicial and complete, and the relation is $u_1 + u_2 + 2 u_3 + u_0 = 0$ with $u_0 = -e_1 - e_2 - 2e_3$. This is the fan of the weighted projective space $\mathbb{P}(1,1,1,2)$. The cone $\operatorname{Cone}(e_1, e_2, u_0)$ has determinant $\pm 2$, and the other three have determinant $\pm 1$. So $X_\Sigma$ is $\mathbb{Q}$-factorial with one singular point, and $2D$ is Cartier for every $D$.

### Proof

*Proof of Theorem 3.3.20.* For part 1, $D$ is $\mathbb{Q}$-Cartier if and only if $rD$ has Cartier data for some $r \ge 1$ (Theorem 3.3.12), which means $\langle m'_\sigma, u_\rho \rangle = -r a_\rho$ with $m'_\sigma \in M$. Put $m_\sigma = m'_\sigma / r$. Conversely, if rational solutions $m_\sigma$ exist, let $r$ be a common denominator of all the $m_\sigma$; then $r m_\sigma \in M$ is Cartier data for $rD$.

For part 2, let $\sigma$ be simplicial with minimal generators $u_1, \dots, u_k$. Let $N_\sigma = \operatorname{span}(\sigma) \cap N$ and $N' = \mathbb{Z} u_1 + \dots + \mathbb{Z} u_k$, a sublattice of $N_\sigma$ of index $\operatorname{mult}(\sigma)$. So $\operatorname{mult}(\sigma) \cdot N_\sigma \subset N'$. Define $\ell \colon N' \to \mathbb{Z}$ by $\ell(u_i) = -a_i$, which is possible since the $u_i$ are a basis of $N'$. Then $\operatorname{mult}(\sigma) \cdot \ell$ extends to a homomorphism $N_\sigma \to \mathbb{Z}$, by $x \mapsto \ell(\operatorname{mult}(\sigma) x)$. Since $N_\sigma$ is saturated in $N$, it is a direct summand, so this homomorphism extends to some $m \in M$. Then $\langle m, u_i \rangle = -\operatorname{mult}(\sigma) a_i$, so $m$ is Cartier data on $\sigma$ for $\operatorname{mult}(\sigma) D$.

Now the main statement. Every Weil divisor is linearly equivalent to a torus-invariant one (Theorem 3.3.4), and $\mathbb{Q}$-Cartier is preserved by linear equivalence. If $\Sigma$ is simplicial, part 2 on each cone and a common multiple $r$ give Cartier data for $rD$ on every cone, so $X_\Sigma$ is $\mathbb{Q}$-factorial; this also proves part 3. Suppose that some $\sigma \in \Sigma$ is not simplicial, so $|\sigma(1)| > \dim \sigma$. The linear map $M_{\mathbb{Q}} \to \mathbb{Q}^{\sigma(1)}$, $m \mapsto (\langle m, u_\rho \rangle)_{\rho \in \sigma(1)}$, has rank $\dim \sigma$, so its image is a proper subspace. A proper subspace does not contain all the coordinate vectors, so some coordinate vector $-e_{\rho_0}$ is not in the image. By part 1, applied to the cone $\sigma$, the divisor $D_{\rho_0}$ is not $\mathbb{Q}$-Cartier. $\square$

*Proof of Corollary 3.3.21.* A smooth cone has multiplicity 1, so every divisor is Cartier by part 2, and the local rings, which are normal with trivial class group, are unique factorization domains. Every cone of dimension at most 2 is simplicial. For $U_\sigma$, apply the theorem to the fan of the faces of $\sigma$. If $\sigma$ is simplicial of dimension $k$, then $\operatorname{Cl}(U_\sigma) \otimes \mathbb{Q} = \operatorname{Pic}(U_\sigma) \otimes \mathbb{Q} = 0$ by Theorem 3.3.13, and $\operatorname{Cl}(U_\sigma)$ is finitely generated, so it is finite. $\square$

### Exercises

1. (A) Decide which of the following fans give $\mathbb{Q}$-factorial varieties: the fan of $\mathbb{P}^1 \times \mathbb{P}^1 \times \mathbb{P}^1$, the fan of the faces of the cone over a square, and the fan of the faces of $\operatorname{Cone}(e_1, e_2, e_1 + e_3, e_2 + e_3)$.
2. (A) For the fan of Example 3.3.25, show that the divisor $D_0$ of $u_0$ is not Cartier and find the Cartier data of $2 D_0$ on the singular cone.
3. (B) Let $\sigma = \operatorname{Cone}(u_1, \dots, u_k)$ be simplicial. Show that the least $r$ with $r D_\rho$ Cartier on $U_\sigma$ for all $\rho$ is the exponent of the finite group $N_\sigma / (\mathbb{Z} u_1 + \dots + \mathbb{Z} u_k)$.
4. (B) Show that the small resolution $X_{\Sigma_+} \to U_\sigma$ of the cone over a square is not the blow-up of the vertex, and that it is the blow-up of the ideal of the plane $D_1$ or of $D_2$ for a suitable choice.

### Lean

- Status: the Lean library has simplicial cones, `MinimalModel.Toric.IsSimplicial`, simplicial fans, `MinimalModel.Toric.Fan.IsSimplicialFan`, and the facts that faces of simplicial cones are simplicial (`MinimalModel.Toric.IsSimplicial.of_isFaceOf`) and that the fan of $\mathbb{P}^1$ is simplicial (`MinimalModel.Toric.P1.isSimplicialFan`). On the fan, `MinimalModel.Toric.Fan.IsQCartier` says that a positive multiple of $D$ has Cartier data, `MinimalModel.Toric.Fan.IsCartier.isQCartier` says that Cartier data gives $\mathbb{Q}$-Cartier, `MinimalModel.Toric.Fan.isQCartier_iff` is part 1 of Theorem 3.3.20, and `MinimalModel.Toric.Fan.IsQCartier.isRCartier` passes to real data. Parts 2 and 3 are not yet in Lean.
- Fidelity: in Lean, `MinimalModel.Toric.IsSimplicial` is the condition that a cone is spanned by a finite set of lattice vectors that is linearly independent over $\mathbb{R}$, which is the condition of Definition 3.1.19. The other side of Theorem 3.3.20, $\mathbb{Q}$-factoriality, is not yet a Lean notion.
- No node of the map covers this section. The toric MMP node MMAWP4SA44 assumes a simplicial fan.

### Notes and history

The equivalence of $\mathbb{Q}$-factoriality and simpliciality is in Cox-Little-Schenck, Chapter 4, and it is the first step in Reid's toric MMP (1983) and in the account of Fujino and Sato (2004). Kollár and Mori, Chapter 2, explain why the MMP needs $\mathbb{Q}$-factorial varieties. Example 3.3.23 is the toric shadow of the Atiyah flop, which Volume 8 treats in full.
