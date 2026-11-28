---
title: Du Val singularities and the ADE graphs
nodes: []
sources: [DuV34, KM98, Rei87, Dur79, Art66]
reads_with: [KM98:4.2, Rei87:ch1, Dur79:all]
requires: [P1.11, P3.12, P5.5, P5.8, P8.8, P8.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Du Val singularities and the ADE graphs

### Statement

Throughout this chapter $k$ is algebraically closed, $X$ is a normal quasi-projective surface and $x \in X$ a closed point. A *resolution of $X$ near $x$* is a projective birational morphism $f \colon Y \to X$ from a smooth surface that is an isomorphism over $X \setminus \{ x \}$, after shrinking $X$ to a neighbourhood of $x$; resolutions of surfaces exist (Lipman, Annals of Mathematics 107, 1978). The curves $E_1, \dots, E_r$ of $f^{-1}(x)$ are the *exceptional curves*. To apply Chapter 8 of Volume P5, which is stated for projective surfaces, replace $X$ by the normalization of its closure in a projective space and resolve the singular points other than $x$; this changes nothing near $x$. By Theorem P5.8.3 the intersection matrix $(E_i \cdot E_j)$ is negative definite. The resolution is *minimal* if no $E_i$ is a $(-1)$-curve; contracting $(-1)$-curves by Corollary P5.7.5 produces a minimal resolution, and it is unique up to isomorphism (Volume 4, Definition 4.3.4 and Proposition 4.3.5; Kollár and Mori, Section 4.1).

**Definition P8.10.1 ($(-2)$-curves, dual graphs, Du Val singularities).** A *$(-2)$-curve* on a smooth surface is a curve $E \cong \mathbb{P}^1$ with $E^2 = -2$; by Theorem P5.5.14, $K_Y \cdot E = 0$ for such a curve. The *dual graph* of the exceptional curves has a vertex for each $E_i$ and $E_i \cdot E_j$ edges between $E_i$ and $E_j$ for $i \neq j$. The point $x$ is a *Du Val singularity* if it is singular and has a resolution all of whose exceptional curves are $(-2)$-curves. Such a resolution contains no $(-1)$-curve, so it is the minimal resolution.

For a graph $\Gamma$ that is a tree with simple edges, let $C_\Gamma = 2I - A_\Gamma$, where $A_\Gamma$ is the adjacency matrix. For a configuration of $(-2)$-curves with dual graph $\Gamma$ the intersection matrix is $-C_\Gamma$.

**Lemma P8.10.2 (the extended diagrams).** Each of the following trees $\Gamma$ carries a vector $z > 0$ with $C_\Gamma z = 0$, so $C_\Gamma$ is not positive definite.

1. $\widetilde{D}_4$: a centre with four neighbours; $z = 2$ at the centre and $1$ at the four leaves.
2. $\widetilde{D}_m$, $m \geq 5$: a chain $c_1, \dots, c_{m-3}$ with two further leaves attached to $c_1$ and two to $c_{m-3}$; $z = 2$ on the chain and $1$ on the four leaves.
3. $\widetilde{E}_6$: a centre with three arms of two vertices each; $z = 3$ at the centre and $2, 1$ along each arm.
4. $\widetilde{E}_7$: a centre with arms of $1$, $3$ and $3$ vertices; $z = 4$ at the centre, $2$ on the short arm, and $3, 2, 1$ along each long arm.
5. $\widetilde{E}_8$: a centre with arms of $1$, $2$ and $5$ vertices; $z = 6$ at the centre, $3$ on the short arm, $4, 2$ on the middle arm and $5, 4, 3, 2, 1$ on the long arm.

Lean: not in Lean as stated.

**Proposition P8.10.3 (Du Val graphs are ADE).** Let $x$ be a Du Val singularity. The dual graph of the exceptional curves of its minimal resolution is a tree with simple edges, and it is one of the Dynkin diagrams

1. $A_n$, $n \geq 1$: a chain of $n$ vertices;
2. $D_n$, $n \geq 4$: a centre with arms of $1$, $1$ and $n - 3$ vertices;
3. $E_6$, $E_7$, $E_8$: a centre with arms of $1$, $2$ and $2$, $3$ or $4$ vertices.

Lean: not in Lean as stated.

**Theorem P8.10.4 (the singularities $A_n$ and $D_4$).** Let $\operatorname{char} k \neq 2$.

1. The surface $\{ xy = z^{n+1} \} \subseteq \mathbb{A}^3$, $n \geq 1$, which is isomorphic to $\{ x^2 + y^2 + z^{n+1} = 0 \}$, has a Du Val singularity at the origin with dual graph $A_n$.
2. The surface $X = \{ x^2 + y^2 z + z^3 = 0 \} \subseteq \mathbb{A}^3$ has a Du Val singularity at the origin with dual graph $D_4$. The blow-up of the origin is a surface $X_1$ with three singular points of type $A_1$ on the exceptional curve $C \cong \mathbb{P}^1$, and blowing these up gives the minimal resolution, with $C$ becoming the central curve.

Lean: not in Lean as stated.

**Theorem P8.10.5 (the ADE classification).** Let $k = \mathbb{C}$. Every Du Val singularity is analytically isomorphic to the origin of exactly one of the following surfaces in $\mathbb{C}^3$, the type being the dual graph of the minimal resolution, and to $\mathbb{C}^2 / G$ for the finite subgroup $G \subseteq SL_2(\mathbb{C})$ listed, which is unique up to conjugacy.

| type | equation | group $G$ |
|---|---|---|
| $A_n$, $n \geq 1$ | $x^2 + y^2 + z^{n+1} = 0$ | cyclic of order $n + 1$ |
| $D_n$, $n \geq 4$ | $x^2 + y^2 z + z^{n-1} = 0$ | binary dihedral of order $4(n - 2)$ |
| $E_6$ | $x^2 + y^3 + z^4 = 0$ | binary tetrahedral, order $24$ |
| $E_7$ | $x^2 + y^3 + y z^3 = 0$ | binary octahedral, order $48$ |
| $E_8$ | $x^2 + y^3 + z^5 = 0$ | binary icosahedral, order $120$ |

Lean: not in Lean as stated.

Parts of this theorem are proved in this volume: the graphs are among the ADE diagrams by Proposition P8.10.3, the types $A_n$ and $D_4$ arise from the listed equations by Theorem P8.10.4, the cyclic case of the group column is Example P8.9.27, and Corollary P8.11.6 proves that every $\mathbb{C}^2 / G$ with $G \subseteq SL_2$ finite is Du Val. The rest is cited from Kollár and Mori, Theorem 4.22 (KM98), and from Durfee (Dur79), whose survey proves the equivalence of fifteen characterizations of these singularities.

### Proof in words

A positive definite form stays positive definite on every coordinate subspace, and each extended diagram has a null vector, so the dual graph of a Du Val singularity contains none of them. A tree that avoids them has at most one branch point, of degree three, and short arms, which leaves exactly the ADE list. The $A_n$ case is the toric resolution of Chapter 8. For $D_4$, one blow-up of the origin produces a line through three ordinary double points, each of which is resolved by one $(-2)$-curve; the residue of the volume form pulls back to a form without zeros, so the canonical class is trivial on the resolution and adjunction forces the strict transform of the line to be a $(-2)$-curve.

### Examples

**Example P8.10.6 (the $A_1$ singularity).** The quadric cone $xy = z^2$ of Example P8.9.8 is $\frac{1}{2}(1, 1)$, and its blow-up has one exceptional curve $E \cong \mathbb{P}^1$ with $E^2 = -2$ (Example P5.8.9). So the vertex is a Du Val singularity of type $A_1$, and the dual graph is a single vertex. The quotient group is $\{ \pm 1 \} \subseteq SL_2$, cyclic of order $2$, as the table predicts.

**Example P8.10.7 (the $A_n$ chain).** By Example P8.9.27 with $r = n + 1$, the resolution of $xy = z^{n+1}$ is a chain $E_1, \dots, E_n$ of $(-2)$-curves with $E_i \cdot E_{i+1} = 1$. In terms of $C_{A_n}$, the vector $z = (1, \dots, 1)$ has $(C_{A_n} z)_i = 2 - 2 = 0$ for $1 < i < n$ and $1$ at the ends, so $(E_1 + \dots + E_n) \cdot E_i \leq 0$ for all $i$, as in Example P5.8.18. Adding one more vertex joined to both ends gives the cycle $\widetilde{A}_n$, on which $z = (1, \dots, 1)$ is a null vector; it is excluded from Proposition P8.10.3 because the graph is a tree, a fact from part 1 of Proposition P5.8.17.

**Example P8.10.8 (a configuration that cannot be contracted).** Let $C_0, C_1, \dots, C_4$ be $(-2)$-curves on a smooth projective surface with $C_0 \cdot C_i = 1$ for $i \geq 1$ and the $C_i$, $i \geq 1$, disjoint, for instance the components of a fibre of type $I_0^*$ of an elliptic fibration. The cycle $Z = 2 C_0 + C_1 + C_2 + C_3 + C_4$ has $Z \cdot C_0 = -4 + 4 = 0$ and $Z \cdot C_i = 2 - 2 = 0$, so $Z^2 = 0$, which is the null vector of $\widetilde{D}_4$ in Lemma P8.10.2. By Theorem P5.8.3 the configuration is not the exceptional locus of any birational morphism, since its intersection matrix is not negative definite. Removing $C_4$ leaves the $D_4$ configuration of Theorem P8.10.4, with $Z_f = 2 C_0 + C_1 + C_2 + C_3$ (Example P5.8.18).

**Example P8.10.9 (a cyclic quotient that is not Du Val).** The singularity $\frac{1}{3}(1, 1)$ has minimal resolution with one curve $E \cong \mathbb{P}^1$, $E^2 = -3$, by Example P8.9.25. So it is not Du Val. More generally $\frac{1}{r}(1, q)$ is Du Val exactly when every entry of $\frac{r}{q} = [b_1, \dots, b_s]$ is $2$, that is, when $\frac{r}{q} = \frac{s + 1}{s}$, which forces $q = r - 1$ and the type $A_{r-1}$.

### Proof

*Lemma P8.10.2.* The entry of $C_\Gamma z$ at a vertex $v$ is $2 z_v - \sum_{w \sim v} z_w$. (1) At the centre $4 - 4 = 0$, at a leaf $2 - 2 = 0$. (2) At an interior chain vertex $4 - 2 - 2 = 0$, at an end of the chain $4 - 1 - 1 - 2 = 0$, since the chain has $m - 3 \geq 2$ vertices, and at a leaf $2 - 2 = 0$. (3) At the centre $6 - 3 \cdot 2 = 0$, at the middle of an arm $4 - 3 - 1 = 0$, at the end $2 - 2 = 0$. (4) At the centre $8 - 2 - 3 - 3 = 0$, on the short arm $4 - 4 = 0$, along a long arm $6 - 4 - 2 = 0$, $4 - 3 - 1 = 0$, $2 - 2 = 0$. (5) At the centre $12 - 3 - 4 - 5 = 0$, on the short arm $6 - 6 = 0$, along the middle arm $8 - 6 - 2 = 0$ and $4 - 4 = 0$, along the long arm $10 - 6 - 4 = 0$, $8 - 5 - 3 = 0$, $6 - 4 - 2 = 0$, $4 - 3 - 1 = 0$, $2 - 2 = 0$. In each case $z^T C_\Gamma z = 0$ with $z \neq 0$.

*Proposition P8.10.3.* By part 1 of Proposition P5.8.17, applied to the exceptional curves of the minimal resolution, which are $(-2)$-curves with $K_Y \cdot E_i = 0$, the dual graph $\Gamma$ is a tree with simple edges. Its intersection matrix $-C_\Gamma$ is negative definite by Theorem P5.8.3, so $C_\Gamma$ is positive definite. For a set $S$ of vertices, the matrix of the induced subgraph is the principal submatrix of $C_\Gamma$ on $S$, because $\Gamma$ has simple edges, and it is positive definite. In a tree, every connected subgraph is induced on its vertex set. So $\Gamma$ contains none of the graphs of Lemma P8.10.2 as a subgraph.

A vertex of degree at least $4$ with four of its neighbours forms $\widetilde{D}_4$. If $\Gamma$ has two vertices $u \neq v$ of degree $3$, the path from $u$ to $v$ together with two neighbours of $u$ and two neighbours of $v$ off the path forms $\widetilde{D}_m$ for some $m \geq 5$; the neighbours are distinct and off the path because $\Gamma$ is a tree. So either $\Gamma$ has no vertex of degree $3$, and is a chain $A_n$, or it has exactly one, a centre with three arms of $p \leq q \leq r$ vertices. If $p \geq 2$ the arms contain $\widetilde{E}_6$, so $p = 1$. If $q = 1$, $\Gamma = D_{r + 3}$. If $q \geq 3$ the arms contain $\widetilde{E}_7$, so $q = 2$, and then $r \geq 5$ would give $\widetilde{E}_8$. So $r \in \{ 2, 3, 4 \}$, which are $E_6$, $E_7$, $E_8$.

*Theorem P8.10.4.* (1) The substitution $u = x + i y$, $v = x - i y$, with $i^2 = -1$, turns $x^2 + y^2 + z^{n+1}$ into $uv + z^{n+1}$, and $z \mapsto \lambda z$ with $\lambda^{n+1} = -1$ turns this into $uv - z^{n+1}$. By Example P8.9.27 with $r = n + 1$, $xy = z^{n+1}$ is the cyclic quotient $\frac{1}{n+1}(1, n)$, whose resolution by Theorem P8.9.23 is a chain of $n$ curves $E_i \cong \mathbb{P}^1$ with $E_i^2 = -2$. So it is Du Val of type $A_n$.

(2) The partial derivatives of $F = x^2 + y^2 z + z^3$ are $2x$, $2yz$ and $y^2 + 3z^2$. At a common zero on $X$, $x = 0$, and $yz = 0$; if $y = 0$ then $F = z^3 = 0$, and if $z = 0$ then $y^2 = 0$. So the origin is the only singular point, and $X$ is normal by Corollary P1.11.14.

*The blow-up.* Let $\beta \colon B \to \mathbb{A}^3$ be the blow-up of the origin and $X_1$ the strict transform of $X$. In the chart $x = x_1 y$, $z = z_1 y$ the total transform is $y^2 (x_1^2 + y h(z_1))$ with $h(z_1) = z_1 + z_1^3 = z_1 (1 + z_1^2)$, so $X_1$ is $F_1 = x_1^2 + y h(z_1) = 0$, and $X_1 \cap \beta^{-1}(0)$ is the line $C = \{ x_1 = y = 0 \}$. In the chart $x = x_2 z$, $y = y_2 z$ the strict transform is $x_2^2 + z (y_2^2 + 1) = 0$, and in the chart $y = y_3 x$, $z = z_3 x$ it is $1 + x (y_3^2 z_3 + z_3^3) = 0$, which does not meet $x = 0$. So $C \cong \mathbb{P}^1$ is the whole exceptional locus of $\pi \colon X_1 \to X$. The singular points of $F_1 = 0$ satisfy $2 x_1 = 0$, $h(z_1) = 0$ and $y h'(z_1) = 0$. The roots $0, \pm i$ of $h$ are simple because $\operatorname{char} k \neq 2$, so $y = 0$, and the singular points in this chart are $p_\rho = (0, 0, \rho)$ for $\rho \in \{ 0, i, -i \}$. In the second chart the only new point of $C$ is $y_2 = 0$, where $\partial / \partial z$ of the equation is $y_2^2 + 1 = 1 \neq 0$. So $X_1$ has exactly three singular points, on $C$.

*The double points.* Near $p_\rho$ write $t = z_1 - \rho$ and $h(z_1) = t u(t)$ with $u(0) = h'(\rho) \neq 0$. Then $x_1$, $y' = y u$, $t$ form a regular system of parameters of $B$ at $p_\rho$, in which $X_1$ is $x_1^2 + y' t = 0$, and $C$ is $x_1 = y' = 0$. The map given by $(x_1, y', t)$ is étale at $p_\rho$, and blowing up commutes with étale base change, so the blow-up of $X_1$ at $p_\rho$ is computed by the charts of Example P5.8.9: it is smooth near the exceptional curve $F_\rho \cong \mathbb{P}^1$, $F_\rho^2 = -2$, and the strict transform of the ruling $x_1 = y' = 0$ meets $F_\rho$ transversally in one point. Let $g \colon Y \to X$ be the composite of $\pi$ and the blow-up of the three points, and $C'$ the strict transform of $C$, which is isomorphic to $C$ because $C$ is a smooth curve. The exceptional curves of $g$ are $C'$, $F_0$, $F_i$, $F_{-i}$.

*The canonical class.* By Theorem P3.12.30 the residue $\omega = dy \wedge dz / (2x)$, extended by the analogous expressions $dz \wedge dx / (2yz)$ and $dx \wedge dy / (y^2 + 3z^2)$ where those denominators are nonzero, generates $\omega_X$ on $X \setminus \{ 0 \}$, so $K_X = \operatorname{div}(\omega) = 0$. In the first chart $dy \wedge dz = dy \wedge (y \, dz_1 + z_1 \, dy) = y \, dy \wedge dz_1$ and $2x = 2 x_1 y$, so
$$\pi^* \omega = \frac{dy \wedge dz_1}{2 x_1},$$
which is the residue form of $F_1$ since $\partial F_1 / \partial x_1 = 2 x_1$. The same holds in the second chart. So $\pi^* \omega$ generates $\omega_{X_1}$ on the smooth locus of $X_1$, which contains the generic point of $C$. On $Y$, $K_Y = \operatorname{div}(g^* \omega)$ is supported on the exceptional curves, and its coefficient on $C'$ is $0$. Near $F_\rho$ it is $c_\rho F_\rho$; adjunction (Theorem P5.5.14) gives $K_Y \cdot F_\rho = -2 - F_\rho^2 = 0$, so $c_\rho F_\rho^2 = 0$ and $c_\rho = 0$. Hence $K_Y = 0$ near $g^{-1}(0)$, and $K_Y \cdot C' = 0$. By Theorem P5.5.14, $C'^2 = -2 - K_Y \cdot C' = -2$. So all four exceptional curves are $(-2)$-curves, $x$ is Du Val, and the graph is $C'$ joined to $F_0$, $F_i$, $F_{-i}$, which is $D_4$.

*Theorem P8.10.5.* The equations and groups are classical: Du Val (DuV34) found the configurations, Klein the quotients $\mathbb{C}^2 / G$ and their invariants, and Artin (Art66) and Brieskorn proved that the rational double points are exactly these hypersurfaces; see Kollár and Mori, Section 4.2 (KM98), and Durfee (Dur79, Section 1 and the list of characterizations A to O). The uniqueness of the type follows from the uniqueness of the minimal resolution.

### Exercises

1. (A) Compute $\det C_\Gamma$ for $A_n$, $D_n$, $E_6$, $E_7$, $E_8$, and check that for $A_n$ the value $n + 1$ is the order of the class group computed in Theorem P8.9.23.
2. (A) Show that $x^2 + y^2 z + z^3$ and $x^2 + y^3 + z^3$ define isomorphic singularities when $\operatorname{char} k \neq 2, 3$, by a linear change of $y, z$.
3. (B) Blow up the origin of $xy = z^{n+1}$, $n \geq 2$, and show that the strict transform has two exceptional lines meeting in a point of type $A_{n-2}$ (smooth for $n = 2$). Deduce the $A_n$ chain by induction, without toric geometry.
4. (B) Find the null vector of $\widetilde{A}_n$, and show that a cycle of $(-2)$-curves on a smooth projective surface is never negative definite.
5. (B) Show that the leading principal minors of $C_{E_8}$, in a suitable order of the vertices, are all positive, so that $C_{E_8}$ is positive definite.
6. (C) Let $k = \mathbb{C}$. Blow up the origin of $x^2 + y^3 + z^5 = 0$ and show that the strict transform has a single singular point, of type $E_7$. Explain how this is consistent with the fundamental cycle of Example P8.10.14.

### Lean

Du Val singularities and Dynkin diagrams are not in the repository. The notion of a canonical singularity, `MinimalModel.IsCanonical`, is stated in `MinimalModel/Statements/Basic.lean`, and Chapter 13 explains how it applies to Du Val singularities.

### Notes and history

Du Val (DuV34) characterized these singularities, in 1934, as the isolated surface singularities that do not affect the conditions of adjunction, which is the condition $K_Y = f^* K_X$ of Section 10.2. Their names come from the root systems: the matrix $C_\Gamma$ is the Cartan matrix, and the fundamental cycle is the highest root. Reid's Young Person's Guide (Rei87) starts from them as the canonical singularities of surfaces, and Kollár and Mori, Section 4.2 (KM98), give the classification. Durfee's survey (Dur79) lists fifteen characterizations, including simple critical points in Arnold's sense and quotients by finite subgroups of $SL_2(\mathbb{C})$.
