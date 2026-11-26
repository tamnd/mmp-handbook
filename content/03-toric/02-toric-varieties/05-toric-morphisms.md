---
title: Toric morphisms and toric resolution
nodes: []
sources: [CLS11, Ful93, KKMS73]
reads_with: [CLS11:ch3, CLS11:ch11, Ful93:1.4, Ful93:2.6]
requires: [P8.6, P8.8, 3.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Toric morphisms and toric resolution

### Statement

**Definition 3.2.36 (compatible lattice maps, toric morphisms).** Let $\Sigma$ be a fan in $N_{\mathbb{R}}$ and $\Sigma'$ a fan in $N'_{\mathbb{R}}$. A homomorphism $\varphi \colon N \to N'$ is *compatible* with $\Sigma$ and $\Sigma'$ if for each $\sigma \in \Sigma$ there is $\sigma' \in \Sigma'$ with $\varphi_{\mathbb{R}}(\sigma) \subset \sigma'$. A morphism $f \colon X_\Sigma \to X_{\Sigma'}$ is *toric* if it maps $T_N$ into $T_{N'}$ and its restriction $T_N \to T_{N'}$ is a homomorphism of groups.

**Theorem 3.2.37 (toric morphisms are lattice maps).** Let $\varphi \colon N \to N'$ be compatible with $\Sigma$ and $\Sigma'$.

1. There is a unique toric morphism $\varphi_* \colon X_\Sigma \to X_{\Sigma'}$ whose restriction to the tori is $\varphi \otimes 1 \colon N \otimes k^* \to N' \otimes k^*$. It is equivariant: $\varphi_*(t \cdot x) = \varphi(t) \cdot \varphi_*(x)$.
2. Every toric morphism $X_\Sigma \to X_{\Sigma'}$ is $\varphi_*$ for a unique compatible $\varphi$.
3. If $\varphi_{\mathbb{R}}(\sigma) \subset \sigma'$, then $\varphi_*$ maps $O(\sigma)$ into $O(\sigma')$ for the smallest such cone $\sigma'$.

Lean: not yet in Lean.

**Theorem 3.2.38 (properness).** Let $\varphi \colon N \to N'$ be compatible with $\Sigma$ and $\Sigma'$. Then $\varphi_*$ is proper if and only if $\varphi_{\mathbb{R}}^{-1}(|\Sigma'|) = |\Sigma|$.

Lean: not yet in Lean.

**Corollary 3.2.39 (toric resolution).** Let $\Sigma'$ be a refinement of $\Sigma$ (Definition 3.1.28). The identity of $N$ gives a proper birational toric morphism $f \colon X_{\Sigma'} \to X_\Sigma$. It is an isomorphism over $U_\sigma$ for each $\sigma$ that is a cone of both fans. If $\Sigma'$ is a smooth refinement as in Theorem 3.1.29, then $f$ is a resolution of singularities, and it is an isomorphism over the union of the $U_\sigma$ with $\sigma$ smooth, which is the smooth locus of $X_\Sigma$.

Lean: not yet in Lean.

So every toric variety has a resolution of singularities in every characteristic, by a toric morphism. The star subdivision $\Sigma^*(v)$ gives a proper birational morphism whose only new divisor is $V(\operatorname{Cone}(v))$. When $\Sigma$ is smooth and $v = u_1 + \dots + u_k$ for a cone $\operatorname{Cone}(u_1, \dots, u_k)$ of $\Sigma$, it is the blow-up of the orbit closure $V(\operatorname{Cone}(u_1, \dots, u_k))$ (Cox-Little-Schenck, Chapter 3).

### Proof in words

A compatible lattice map sends each $\sigma$ into some $\sigma'$, so its dual map $M' \to M$ sends $S_{\sigma'}$ into $S_\sigma$. This gives a ring map $k[S_{\sigma'}] \to k[S_\sigma]$ and a morphism $U_\sigma \to U_{\sigma'}$. These morphisms agree on the overlaps, since all of them restrict to the same map of tori, so they glue. For the converse, the restriction to the tori is a group homomorphism, and so it is given by a lattice map $\varphi$. A limit argument with one-parameter subgroups shows that $\varphi$ is compatible: if $u$ is in the relative interior of $\sigma$, then $\lambda^u(t)$ tends to $\gamma_\sigma$, and its image $\lambda^{\varphi(u)}(t)$ must have a limit, which forces $\varphi(u)$ into a cone of $\Sigma'$.

Properness is again a question about limits. A one-parameter subgroup $\lambda^u$ of $T_N$ whose image has a limit in $X_{\Sigma'}$ must have a limit in $X_\Sigma$; this is the condition $\varphi_{\mathbb{R}}^{-1}(|\Sigma'|) \subset |\Sigma|$.

### Examples

**Example 3.2.40 (the blow-up of the origin of $\mathbb{A}^2$).** Let $\Sigma$ be the fan of $\mathbb{A}^2$ and $\Sigma' = \Sigma^*(e_1 + e_2)$, with the maximal cones $\operatorname{Cone}(e_1, e_1 + e_2)$ and $\operatorname{Cone}(e_1 + e_2, e_2)$. The first cone has the dual basis $(1, -1), (0, 1)$ and the chart $\operatorname{Spec} k[x/y, y]$. The second has the dual basis $(1, 0), (-1, 1)$ and the chart $\operatorname{Spec} k[x, y/x]$. These are the two charts of the blow-up $\operatorname{Bl}_0 \mathbb{A}^2$, and the toric morphism is the blow-down. The new divisor $E = V(e_1 + e_2)$ is the exceptional curve $\mathbb{P}^1$. The same construction with $e_1 + \dots + e_n$ gives $\operatorname{Bl}_0 \mathbb{A}^n$.

**Example 3.2.41 (the minimal resolution of $\frac1n(1,1)$).** Let $\Sigma'$ be the star subdivision of $\sigma_n = \operatorname{Cone}(e_2, n e_1 - e_2)$ at $e_1$ (Example 3.1.31). The cone $\operatorname{Cone}(e_1, e_2)$ gives the chart $\operatorname{Spec} k[x, y]$. The cone $\operatorname{Cone}(e_1, n e_1 - e_2)$ has the dual basis $(0, -1), (1, n)$, so its chart is $\operatorname{Spec} k[y^{-1}, x y^n]$. So $X_{\Sigma'}$ is covered by two planes with the coordinates $(y, x)$ and $(y^{-1}, x y^n)$. This is the total space of the line bundle $\mathcal{O}_{\mathbb{P}^1}(-n)$: $y$ is the coordinate on the base, and the fibre coordinate changes by $x \mapsto y^n x$. The zero section is the exceptional curve $E = V(e_1) = \{x = 0\}$. The morphism $X_{\Sigma'} \to U_{\sigma_n}$ is given on the first chart by $(x, y) \mapsto (x, xy, \dots, xy^n)$, and it contracts $E$ to the vertex. For $n = 2$ this is the resolution of the quadric cone by $T^* \mathbb{P}^1$, with one exceptional curve of self-intersection $-2$.

**Example 3.2.42 (the Hirzebruch surface as a bundle).** Let $\varphi \colon \mathbb{Z}^2 \to \mathbb{Z}$ be $(a, b) \mapsto a$. It maps the cones $\operatorname{Cone}(u_1, u_2)$ and $\operatorname{Cone}(u_4, u_1)$ of $\mathbb{F}_n$ into $\mathbb{R}_{\ge 0}$, and $\operatorname{Cone}(u_2, u_3)$ and $\operatorname{Cone}(u_3, u_4)$ into $\mathbb{R}_{\le 0}$, since $u_1 = (1, 0)$, $u_2 = (0, 1)$, $u_3 = (-1, n)$, $u_4 = (0, -1)$. So it is compatible with the fan of $\mathbb{P}^1$, and $\varphi_* \colon \mathbb{F}_n \to \mathbb{P}^1$ is a toric morphism. It is proper, since both fans are complete. The kernel of $\varphi$ is $\mathbb{Z} e_2$, and the cones of $\mathbb{F}_n$ in the kernel are the rays $\pm e_2$, which form the fan of $\mathbb{P}^1$. So the general fibre is $\mathbb{P}^1$. The curves $V(u_1)$ and $V(u_3)$ are the fibres over the two fixed points, and $V(u_2)$ and $V(u_4)$ are two sections. The map $(a, b) \mapsto b$ is not compatible: it maps $\operatorname{Cone}(u_3, u_4)$ onto $[-1, n] \cdot \mathbb{R}_{\ge 0} = \mathbb{R}$ for $n \ge 1$.

**Example 3.2.43 (the contraction of the negative section).** The fan of $\mathbb{F}_n$ refines the fan of $\mathbb{P}(1,1,n)$ of Example 3.1.26: $\operatorname{Cone}(u_1, u_2) \cup \operatorname{Cone}(u_2, u_3) = \operatorname{Cone}(u_1, u_3)$, because $u_2 = \frac1n(u_1 + u_3)$. So Corollary 3.2.39 gives a proper birational toric morphism $\mathbb{F}_n \to \mathbb{P}(1,1,n)$. It is an isomorphism over $U_{\operatorname{Cone}(u_3, u_4)}$ and $U_{\operatorname{Cone}(u_4, u_1)}$, and it contracts the curve $V(u_2)$ to the point $\gamma_{\operatorname{Cone}(u_1, u_3)}$. Over $U_{\operatorname{Cone}(u_1, u_3)} \cong U_{\sigma_n}$ it is the resolution of Example 3.2.41. For $n = 1$, $\mathbb{P}(1,1,1) = \mathbb{P}^2$ and the morphism $\mathbb{F}_1 \to \mathbb{P}^2$ is the blow-up of a point. This is the first divisorial contraction of a toric MMP: Chapter 3 computes $K_{\mathbb{F}_n} \cdot V(u_2) = n - 2$, and for $n = 1$ the curve is $K$-negative.

**Example 3.2.44 (maps that are not morphisms).** The identity of $\mathbb{Z}^2$ is not compatible with the fans of $\mathbb{P}^2$ and $\mathbb{A}^2$: the cone $\operatorname{Cone}(u_2, u_0)$ lies in no cone of the fan of $\mathbb{A}^2$. So the rational map $\mathbb{P}^2 \dashrightarrow \mathbb{A}^2$, $(x_0 : x_1 : x_2) \mapsto (x_1/x_0, x_2/x_0)$, is not a morphism. The projection $(a, b) \mapsto a$ is not compatible with the fans of $\mathbb{P}^2$ and $\mathbb{P}^1$, because it maps $\operatorname{Cone}(u_0, u_1) = \operatorname{Cone}(-e_1 - e_2, e_1)$ onto $\mathbb{R}$. It is the projection $(x_0 : x_1 : x_2) \mapsto (x_0 : x_1)$ from the point $(0 : 0 : 1) = \gamma_{\operatorname{Cone}(u_0, u_1)}$, which is not defined at that point. The star subdivision of $\operatorname{Cone}(u_0, u_1)$ at $u_0 + u_1 = -e_2$ blows up the point, and the projection becomes compatible with the new fan, which is the fan of $\mathbb{F}_1$ after a change of basis.

### Proof

*Proof of Theorem 3.2.37.* For part 1, let $\varphi^* \colon M' \to M$ be the dual map. If $\varphi_{\mathbb{R}}(\sigma) \subset \sigma'$ and $m' \in S_{\sigma'}$, then $\langle \varphi^* m', u \rangle = \langle m', \varphi(u) \rangle \ge 0$ for $u \in \sigma$, so $\varphi^*(S_{\sigma'}) \subset S_\sigma$. The ring map $\chi^{m'} \mapsto \chi^{\varphi^* m'}$ gives a morphism $U_\sigma \to U_{\sigma'}$. On $T_N$ it is $\varphi \otimes 1$. Two such morphisms for different choices of $\sigma'$ agree on $T_N$, which is dense, and $X_{\Sigma'}$ is separated, so they agree. So the morphisms glue to $\varphi_*$, and the uniqueness has the same proof. Equivariance holds on the dense torus, so it holds everywhere. For part 3, let $u$ be in the relative interior of $\sigma$ and let $\sigma'$ be the smallest cone of $\Sigma'$ that contains $\varphi(\sigma)$. Then $\varphi(u)$ is in the relative interior of $\sigma'$: otherwise $\varphi(u)$ lies in a proper face $\tau'$ of $\sigma'$, a form $m' \in S_{\sigma'}$ with $\tau' = \sigma' \cap m'^\perp$ vanishes at $\varphi(u)$, and so $\varphi^* m' \in S_\sigma$ vanishes at a relative interior point of $\sigma$, hence on $\sigma$, so $\varphi(\sigma) \subset \tau'$. By Lemma 3.2.30, $\varphi_*(\gamma_\sigma) = \lim_{t \to 0} \lambda^{\varphi(u)}(t) = \gamma_{\sigma'}$, and equivariance gives $\varphi_*(O(\sigma)) \subset O(\sigma')$.

Part 2 is cited without proof (Cox-Little-Schenck, Chapter 3). The restriction to the tori is a homomorphism $T_N \to T_{N'}$, which is $\varphi \otimes 1$ for a unique $\varphi$ by Proposition 3.2.2. For $u$ in the relative interior of $\sigma$, $\lambda^u(t)$ has the limit $\gamma_\sigma$, so $\lambda^{\varphi(u)}(t) = f(\lambda^u(t))$ has the limit $f(\gamma_\sigma)$. This limit lies in some $U_{\sigma'}$, and Lemma 3.2.21 gives $\varphi(u) \in \sigma'$. A further argument shows that one cone $\sigma'$ works for all of $\sigma$. $\square$

*Proof of Theorem 3.2.38 and Corollary 3.2.39.* Theorem 3.2.38 is cited without proof (Cox-Little-Schenck, Chapter 3). It is proved with the valuative criterion of properness, which for toric morphisms reduces to one-parameter subgroups. For Corollary 3.2.39, each cone of $\Sigma'$ lies in a cone of $\Sigma$, so the identity is compatible. The supports are equal, so $f$ is proper by Theorem 3.2.38, and $f$ is the identity on $T_N$, so it is birational. If $\sigma$ is a cone of both fans, then the cones of $\Sigma'$ inside $\sigma$ are the faces of $\sigma$, because $\Sigma'$ is a fan that contains $\sigma$ and covers $\sigma$ by its cones. So $f^{-1}(U_\sigma) = U_\sigma$, by Theorem 3.2.37, part 3, and $f$ is an isomorphism there. For a smooth refinement, $X_{\Sigma'}$ is smooth by Theorem 3.2.22, and Theorem 3.1.29 keeps the smooth cones of $\Sigma$. The smooth locus of $X_\Sigma$ is the union of the $U_\sigma$ with $\sigma$ smooth, by Theorem 3.2.13 and Theorem 3.2.29. $\square$

### Exercises

1. (A) Write down the charts of $\operatorname{Bl}_0 \mathbb{A}^3$ from the star subdivision of the orthant at $e_1 + e_2 + e_3$, and check that the exceptional divisor is $\mathbb{P}^2$.
2. (A) Show that the lattice map $\mathbb{Z} \to \mathbb{Z}^2$, $1 \mapsto (1, 1)$, gives the diagonal $\mathbb{P}^1 \to \mathbb{P}^1 \times \mathbb{P}^1$, and that multiplication by $d$ on $\mathbb{Z}$ gives the map $\mathbb{P}^1 \to \mathbb{P}^1$, $(x_0 : x_1) \mapsto (x_0^d : x_1^d)$.
3. (B) Find the toric morphism $\mathbb{F}_1 \to \mathbb{P}^2$ explicitly on the four charts of $\mathbb{F}_1$.
4. (B) Show that the minimal resolution of $\frac1n(1,q)$ given by Proposition 3.1.30 is a chain of $s$ curves $\mathbb{P}^1$, each meeting the next one in one point.
5. (C) Let $\Sigma$ be the fan of the cone over a square, and let $\Sigma_+$, $\Sigma_-$ be the two smooth refinements of Example 3.1.33. Show that $X_{\Sigma_\pm} \to U_\sigma$ are small resolutions, with exceptional locus a curve $\mathbb{P}^1$, and that the composite birational map $X_{\Sigma_+} \dashrightarrow X_{\Sigma_-}$ is not a morphism.

### Lean

- Status: not yet in Lean. The Lean library has no lattice maps between fans, no toric morphisms and no refinements yet.
- Fidelity: Corollary 3.2.39 rests on Theorem 3.1.29, which is not in Lean either.
- No node of the map covers this section. The toric MMP node of the map, MMAWP4SA44, uses toric morphisms, and the later chapters of this volume return to it.

### Notes and history

The correspondence between toric morphisms and compatible lattice maps is in Kempf, Knudsen, Mumford and Saint-Donat (1973), together with the resolution of toric singularities by subdivision. The properness criterion is in Oda's book and Fulton's book. The two small resolutions of Exercise 5 and the birational map between them form the Atiyah flop. Reid (1983) used toric morphisms of this kind to build the toric minimal model program, and Fujino and Sato (2004) gave a short account of it. Both are the spine of the later chapters of this volume.
