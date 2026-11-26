---
title: The toric variety of a fan
nodes: []
sources: [CLS11, Ful93, Sum74]
reads_with: [CLS11:ch3, Ful93:1.4, Ful93:2.4]
requires: [P8.6, 3.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The toric variety of a fan

### Statement

**Definition 3.2.18 (the toric variety $X_\Sigma$).** Let $\Sigma$ be a fan in $N_{\mathbb{R}}$. For $\sigma, \sigma' \in \Sigma$ the cone $\tau = \sigma \cap \sigma'$ is a face of both, so by Proposition 3.2.12 $U_\tau$ is an open subset of $U_\sigma$ and of $U_{\sigma'}$. The variety $X_\Sigma$ is obtained by gluing the $U_\sigma$, $\sigma \in \Sigma$, along these open subsets, by the identity of $U_\tau$. All the gluing maps are the identity on the torus $T_N = U_{\{0\}}$, so the cocycle condition holds.

**Theorem 3.2.19 (the toric variety of a fan).** $X_\Sigma$ is a normal separated toric variety of dimension $n$ with torus $T_N$. For $\sigma, \sigma' \in \Sigma$,

$$U_\sigma \cap U_{\sigma'} = U_{\sigma \cap \sigma'}, \qquad S_{\sigma \cap \sigma'} = S_\sigma + S_{\sigma'}.$$

Lean: not yet in Lean.

**Theorem 3.2.20 (Sumihiro).** Every normal separated toric variety with torus $T_N$ is isomorphic to $X_\Sigma$ for a unique fan $\Sigma$ in $N_{\mathbb{R}}$, by an isomorphism that is the identity on $T_N$.

Lean: not yet in Lean.

**Lemma 3.2.21 (limits of one-parameter subgroups).** Let $\sigma$ be a strongly convex rational polyhedral cone and $u \in N$. Then $\lim_{t \to 0} \lambda^u(t)$ exists in $U_\sigma$ if and only if $u \in \sigma$. Here the limit exists means that $\lambda^u \colon k^* \to T_N \subset U_\sigma$ extends to a morphism $\mathbb{A}^1 \to U_\sigma$.

Lean: not yet in Lean.

**Theorem 3.2.22 (smooth and complete).** Let $\Sigma$ be a fan.

1. $X_\Sigma$ is smooth if and only if every cone of $\Sigma$ is smooth.
2. $X_\Sigma$ is complete if and only if $\Sigma$ is complete.

Lean: not yet in Lean.

### Proof in words

The gluing is separated because of the separation lemma. A variety covered by affine open sets $U_i$ is separated when each $U_i \cap U_j$ is affine and the restriction maps $\mathcal{O}(U_i) \otimes \mathcal{O}(U_j) \to \mathcal{O}(U_i \cap U_j)$ are onto. For two cones, the form $m$ of Lemma 3.1.21 cuts out $\tau = \sigma \cap \sigma'$ in both, so $S_\tau = S_\sigma + \mathbb{Z}_{\ge 0}(-m)$, and $-m$ lies in $S_{\sigma'}$. So $S_\tau = S_\sigma + S_{\sigma'}$, and the map on rings is onto.

The criterion for completeness rests on Lemma 3.2.21. A point $\lambda^u(t)$ has the coordinates $t^{\langle m, u \rangle}$, $m \in S_\sigma$, and these have a limit at $t = 0$ exactly when all the exponents are nonnegative, which means $u \in (\sigma^\vee)^\vee = \sigma$. If $X_\Sigma$ is complete, every curve $\lambda^u$ has a limit, so every lattice point is in $|\Sigma|$. The converse uses the valuative criterion and the fact that a torus orbit closure meets the torus; it is cited.

### Examples

**Example 3.2.23 (the projective line).** The fan of $\mathbb{P}^1$ (Example 3.1.23) has the cones $\mathbb{R}_{\ge 0}$, $\mathbb{R}_{\le 0}$ and $\{0\}$. The charts are $\operatorname{Spec} k[x]$ and $\operatorname{Spec} k[x^{-1}]$, glued along $\operatorname{Spec} k[x^{\pm 1}]$. This is $\mathbb{P}^1$ with $x = x_1 / x_0$. The limits of $\lambda^{1}(t) = t$ and $\lambda^{-1}(t) = t^{-1}$ at $t = 0$ are the points $0$ and $\infty$.

**Example 3.2.24 (the projective plane).** The fan of $\mathbb{P}^2$ (Example 3.1.24) has rays $u_0 = -e_1 - e_2$, $u_1 = e_1$, $u_2 = e_2$. Put $x = \chi^{e_1^*}$ and $y = \chi^{e_2^*}$. The cone $\operatorname{Cone}(u_1, u_2)$ has the dual generators $e_1^*, e_2^*$ and the chart $\operatorname{Spec} k[x, y]$. The cone $\operatorname{Cone}(u_2, u_0)$ has the dual generators $(-1, 0)$ and $(-1, 1)$, which form a basis of $M$, and the chart $\operatorname{Spec} k[x^{-1}, x^{-1} y]$. The cone $\operatorname{Cone}(u_0, u_1)$ has the chart $\operatorname{Spec} k[y^{-1}, x y^{-1}]$. With $x = x_1/x_0$ and $y = x_2/x_0$ these are the three standard charts $\{x_0 \neq 0\}$, $\{x_1 \neq 0\}$, $\{x_2 \neq 0\}$ of $\mathbb{P}^2$, and the gluing is the usual one. The torus is $\{x_0 x_1 x_2 \neq 0\}$. The same computation with the fan of Example 3.1.24 in $\mathbb{R}^n$ gives $\mathbb{P}^n$.

**Example 3.2.25 (the Hirzebruch surface).** The fan of $\mathbb{F}_n$ (Example 3.1.25) has four smooth cones, so $X_\Sigma$ is a smooth complete surface covered by four copies of $\mathbb{A}^2$. The cones $\operatorname{Cone}(u_1, u_2)$ and $\operatorname{Cone}(u_2, u_3)$ give the charts $\operatorname{Spec} k[x, y]$ and $\operatorname{Spec} k[x^{-1}, x^n y]$, since $(-1, 0), (n, 1)$ is the dual basis of $u_3 = (-1, n), u_2 = (0, 1)$. Section 5 shows that the projection to the first coordinate makes $X_\Sigma$ a $\mathbb{P}^1$-bundle over $\mathbb{P}^1$, and it is the Hirzebruch surface $\mathbb{P}(\mathcal{O} \oplus \mathcal{O}(n))$ (Cox-Little-Schenck, Chapter 3).

**Example 3.2.26 (the line with a doubled origin).** Take two copies of $\mathbb{A}^1 = U_{\mathbb{R}_{\ge 0}}$ and glue them along $k^* = U_{\{0\}}$. The result is a toric variety with torus $k^*$, and it is not separated. It does not come from a fan, because the two cones are the same cone $\mathbb{R}_{\ge 0}$, and their intersection is not the face $\{0\}$ along which they are glued. On rings, $S_{\{0\}} = \mathbb{Z}$, but $S_{\mathbb{R}_{\ge 0}} + S_{\mathbb{R}_{\ge 0}} = \mathbb{Z}_{\ge 0}$, so the map $k[x] \otimes k[x] \to k[x^{\pm 1}]$ is not onto. The two curves $t \mapsto t$ into the two copies have two different limits at $t = 0$.

**Example 3.2.27 (a fan that is not complete).** Remove the cone $\operatorname{Cone}(u_0, u_1)$ from the fan of $\mathbb{P}^2$, but keep its rays. The new fan gives $\mathbb{P}^2$ minus the point $(0 : 0 : 1)$. The lattice point $u = (1, -1) = 2 u_1 + u_0$ is not in its support, and by Lemma 3.2.21 the curve $\lambda^u(t) = (1 : t : t^{-1})$ has no limit in it: in $\mathbb{P}^2$ the limit is $(0 : 0 : 1)$, which was removed.

### Proof

*Proof of Theorem 3.2.19.* The torus $T_N$ is an open subset of each $U_\sigma$, and the gluing maps are the identity on it. So $T_N$ is an open dense subset of the irreducible scheme $X_\Sigma$, and the actions of $T_N$ on the $U_\sigma$ (Theorem 3.2.11) agree on the overlaps, so they glue. Normality is local, so it holds by Theorem 3.2.11. By construction $U_\sigma \cap U_{\sigma'} = U_\tau$ with $\tau = \sigma \cap \sigma'$. By Lemma 3.1.21 there is $m \in \sigma^\vee \cap (-\sigma')^\vee \cap M$ with $\tau = \sigma \cap m^\perp = \sigma' \cap m^\perp$. By Proposition 3.2.12, $S_\tau = S_\sigma + \mathbb{Z}_{\ge 0}(-m)$, and $-m \in S_{\sigma'}$. So $S_\tau \subset S_\sigma + S_{\sigma'}$. The other inclusion holds because $\tau \subset \sigma$ and $\tau \subset \sigma'$. So the map $k[S_\sigma] \otimes k[S_{\sigma'}] \to k[S_\tau]$, $\chi^a \otimes \chi^b \mapsto \chi^{a + b}$, is onto. This map is the comorphism of the diagonal $U_\tau \to U_\sigma \times U_{\sigma'}$, so the diagonal is a closed immersion on each $U_\sigma \times U_{\sigma'}$, and $X_\Sigma$ is separated. $\square$

*Proof of Theorem 3.2.20.* This is cited without proof (Sumihiro 1974; Cox-Little-Schenck, Chapter 3). The key step is Sumihiro's theorem: every point of a normal variety with a torus action has an affine open neighbourhood that is invariant under the torus. Each invariant affine open set is $U_\sigma$ by Theorem 3.2.11, and the cones that arise form a fan. $\square$

*Proof of Lemma 3.2.21.* For $m \in S_\sigma$, the function $\chi^m \circ \lambda^u$ on $k^*$ is $t^{\langle m, u \rangle}$. The morphism $\lambda^u$ extends to $\mathbb{A}^1 \to U_\sigma$ exactly when the comorphism $k[S_\sigma] \to k[t^{\pm 1}]$ lands in $k[t]$, that is, when $\langle m, u \rangle \ge 0$ for all $m \in S_\sigma$. Since $S_\sigma$ spans the cone $\sigma^\vee$, this means $u \in (\sigma^\vee)^\vee = \sigma$ (Theorem 3.1.3). $\square$

*Proof of Theorem 3.2.22.* Part 1 follows from Theorem 3.2.13, since the $U_\sigma$ form an open cover and smoothness is local. For part 2, suppose that $X_\Sigma$ is complete and let $u \in N$. A morphism from $k^*$ to a complete variety extends to $\mathbb{A}^1$, by the valuative criterion of properness. The extension maps $0$ into some $U_\sigma$, and so it maps an open neighbourhood $V$ of $0$ into $U_\sigma$. Its comorphism sends each $\chi^m$, $m \in S_\sigma$, to $t^{\langle m, u \rangle}$, and this function is regular at $0$. So $\langle m, u \rangle \ge 0$ for all $m \in S_\sigma$, and $u \in \sigma$ as in the proof of Lemma 3.2.21. So $N \subset |\Sigma|$. Since $|\Sigma|$ is a finite union of closed cones, it is closed and stable under positive scaling, so $N_{\mathbb{Q}} \subset |\Sigma|$ and then $|\Sigma| = N_{\mathbb{R}}$. The converse is cited without proof (Cox-Little-Schenck, Chapter 3): when $|\Sigma| = N_{\mathbb{R}}$, the valuative criterion reduces to the existence of limits of one-parameter subgroups, and each such limit exists by Lemma 3.2.21. $\square$

### Exercises

1. (A) Write down the four charts of $\mathbb{F}_n$ and the gluing maps between them.
2. (A) Show that the fan of $\mathbb{P}^1 \times \mathbb{P}^1$ gives the product variety, and more generally that $X_{\Sigma_1 \times \Sigma_2} \cong X_{\Sigma_1} \times X_{\Sigma_2}$.
3. (B) Find a toric variety with torus $(k^*)^2$ that is glued from the charts of the cones $\operatorname{Cone}(e_1, e_2)$ and $\operatorname{Cone}(e_1 + e_2, -e_1 + e_2)$ of Example 3.1.27 along the torus, and show that it is not separated.
4. (B) In the proof of Theorem 3.2.19, why is the diagonal a closed immersion once each map $k[S_\sigma] \otimes k[S_{\sigma'}] \to k[S_\tau]$ is onto? State the criterion that is used.
5. (B) Let $\Sigma$ be the fan in $\mathbb{R}^2$ with the rays $e_1$, $e_2$, $-e_1$, $-e_2$ and only the three cones $\operatorname{Cone}(e_1, e_2)$, $\operatorname{Cone}(e_2, -e_1)$, $\operatorname{Cone}(-e_1, -e_2)$ of dimension 2. Identify $X_\Sigma$ as an open subset of $\mathbb{P}^1 \times \mathbb{P}^1$, and find a one-parameter subgroup with no limit.

### Lean

- Status: the Lean library has fans (`MinimalModel.Toric.Fan`) with the condition that two cones meet in a common face (the field `MinimalModel.Toric.Fan.inter_face`). It has complete fans, `MinimalModel.Toric.Fan.IsComplete`, and the fans of $\mathbb{P}^1$ and $\mathbb{P}^2$ are complete, `MinimalModel.Toric.P1.isComplete` and `MinimalModel.Toric.P2.isComplete`. The variety $X_\Sigma$, Theorem 3.2.19 and Theorem 3.2.22 are not yet in Lean.
- Fidelity: `MinimalModel.Toric.Fan.IsComplete` is the condition $|\Sigma| = N_{\mathbb{R}}$ on the fan. Part 2 of Theorem 3.2.22 is the statement that turns it into completeness of the variety; the Lean route states it as a later step.
- No node of the map covers this section.

### Notes and history

The construction of $X_\Sigma$ by gluing is due to Demazure (1970), for smooth fans, and to Kempf, Knudsen, Mumford and Saint-Donat (1973) in general. Sumihiro (1974) proved the theorem on invariant affine neighbourhoods. Without normality it fails: the nodal cubic curve has an action of $k^*$, and its node has no invariant affine neighbourhood other than the whole curve, which is not affine. A complete toric variety need not be projective. Fulton's book and Oda's book give examples in dimension 3, and Cox-Little-Schenck, Chapter 6, gives the criterion for projectivity by support functions.
