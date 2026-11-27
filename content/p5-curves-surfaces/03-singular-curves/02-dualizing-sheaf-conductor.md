---
title: The dualizing sheaf of a singular curve and the conductor
nodes: []
sources: [Har77, Ser88, Liu02]
reads_with: [Har77:III.7, Ser88:IV]
requires: [P1.3, P1.10, P4.7, P4.8, P4.9, P5.1, P5.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The dualizing sheaf of a singular curve and the conductor

### Statement

Let $C$ be a curve as in Section 3.1, with normalization $\nu \colon \widetilde{C} \to C$ and $\mathcal{Q} = \nu_* \mathcal{O}_{\widetilde{C}} / \mathcal{O}_C$. Every local ring of $C$ is a one-dimensional domain, so Cohen-Macaulay, and $C$ has a dualizing sheaf $\omega^\circ_C$ satisfying Serre duality (Theorem P4.7.17 and Theorem P4.7.18). For an invertible sheaf $\mathcal{L}$ on $C$ define $\deg \mathcal{L} = \deg \nu^* \mathcal{L}$, the degree on the smooth curve $\widetilde{C}$.

**Theorem P5.3.10 (Riemann-Roch on an integral curve).** For every invertible sheaf $\mathcal{L}$ on $C$,
$$\chi(\mathcal{L}) = \deg \mathcal{L} + 1 - p_a(C), \qquad h^1(\mathcal{L}) = \dim \operatorname{Hom}(\mathcal{L}, \omega^\circ_C) = h^0(\mathcal{L}^{-1} \otimes \omega^\circ_C).$$
So $h^0(\mathcal{L}) - h^0(\mathcal{L}^{-1} \otimes \omega^\circ_C) = \deg \mathcal{L} + 1 - p_a(C)$.

Lean: not in Lean as stated.

**Proposition P5.3.11 (the dualizing sheaf and the normalization).**

1. $\omega^\circ_C$ is torsion free of rank $1$: $\mathcal{H}om(\mathcal{T}, \omega^\circ_C) = 0$ for every coherent $\mathcal{T}$ with finite support.
2. $\nu_* \omega_{\widetilde{C}} \cong \mathcal{H}om_{\mathcal{O}_C}(\nu_* \mathcal{O}_{\widetilde{C}}, \omega^\circ_C)$, and restriction along $\mathcal{O}_C \to \nu_* \mathcal{O}_{\widetilde{C}}$ embeds $\nu_* \omega_{\widetilde{C}}$ in $\omega^\circ_C$.
3. The quotient $\omega^\circ_C / \nu_* \omega_{\widetilde{C}}$ is isomorphic to $\mathcal{E}xt^1(\mathcal{Q}, \omega^\circ_C)$, and its length at $P$ is $\delta_P$.

Lean: not in Lean as stated.

**Definition P5.3.12 (conductor and Gorenstein points).** The *conductor* of $C$ at $P$ is
$$\mathfrak{c}_P = \operatorname{Ann}_{\mathcal{O}_P}(\widetilde{\mathcal{O}}_P / \mathcal{O}_P) = \{ a \in K : a \widetilde{\mathcal{O}}_P \subseteq \mathcal{O}_P \}.$$
It is an ideal of $\mathcal{O}_P$ and of $\widetilde{\mathcal{O}}_P$, the largest ideal of $\widetilde{\mathcal{O}}_P$ contained in $\mathcal{O}_P$. In this section $P$ is a *Gorenstein point* of $C$ if $\omega^\circ_C$ is invertible near $P$, and $C$ is *Gorenstein* if every point is.

**Theorem P5.3.13 (Serre's conductor formula).** Let $P$ be a Gorenstein point of $C$. Then $(\nu_* \omega_{\widetilde{C}})_P \cong \mathfrak{c}_P$ as $\widetilde{\mathcal{O}}_P$-modules, and
$$\ell(\mathcal{O}_P / \mathfrak{c}_P) = \delta_P, \qquad \ell(\widetilde{\mathcal{O}}_P / \mathfrak{c}_P) = 2 \delta_P.$$

Lean: not in Lean as stated.

**Corollary P5.3.14 (Gorenstein curves).** A curve whose local rings are complete intersections, for instance a plane curve, is Gorenstein. On a Gorenstein curve, $\omega^\circ_C$ is invertible of degree $2 p_a(C) - 2$, $h^0(\omega^\circ_C) = p_a(C)$, and for every invertible $\mathcal{L}$,
$$h^0(\mathcal{L}) - h^0(\omega^\circ_C \otimes \mathcal{L}^{-1}) = \deg \mathcal{L} + 1 - p_a(C).$$

Lean: not in Lean as stated.

### Proof in words

Riemann-Roch on $C$ follows from Riemann-Roch on $\widetilde{C}$: tensoring the normalization sequence with $\mathcal{L}$ shows that $\chi(\mathcal{L})$ differs from $\chi(\nu^* \mathcal{L})$ by $\sum \delta_P$, which turns $g(\widetilde{C})$ into $p_a(C)$. Duality for the finite morphism $\nu$ identifies $\nu_* \omega_{\widetilde{C}}$ with the homomorphisms from $\nu_* \mathcal{O}_{\widetilde{C}}$ to $\omega^\circ_C$, and duality for the inclusion of a point shows that a module of length $\ell$ has $\mathcal{E}xt^1$ into $\omega^\circ_C$ of length $\ell$ and no other $\mathcal{E}xt$. Applying $\mathcal{H}om(-, \omega^\circ_C)$ to the normalization sequence then gives the quotient $\omega^\circ_C / \nu_* \omega_{\widetilde{C}}$ of length $\delta_P$. When $\omega^\circ_C$ is invertible, homomorphisms from $\widetilde{\mathcal{O}}_P$ to $\mathcal{O}_P$ are multiplications by elements of the conductor, so the quotient is $\mathcal{O}_P / \mathfrak{c}_P$.

### Examples

**Example P5.3.15 (the node).** At a node, $\widetilde{\mathcal{O}}_P$ has two maximal ideals $\mathfrak{q}_1, \mathfrak{q}_2$, and $\mathcal{O}_P = k + \mathfrak{q}_1 \mathfrak{q}_2$, the functions taking the same value on the two branches. So $\mathfrak{c}_P = \mathfrak{q}_1 \mathfrak{q}_2 = \mathfrak{m}_P$, with $\ell(\widetilde{\mathcal{O}}_P / \mathfrak{c}_P) = 2 = 2\delta_P$. For the nodal cubic of Example P5.3.6, $\omega^\circ_C \cong \mathcal{O}_C(0) = \mathcal{O}_C$ by Example P4.7.23, and its generator pulls back to the differential $dx / 2y = dt / (t^2 - 1)$ on $\mathbb{P}^1$. This has simple poles at the two branches $t = \pm 1$ with residues $\pm 1/2$, which sum to zero, and no other zeros or poles. On global sections, $H^0(\nu_* \omega_{\mathbb{P}^1}) = 0$ has codimension $1 = \delta_P$ in $H^0(\omega^\circ_C) = k$, as part 3 of Proposition P5.3.11 predicts.

**Example P5.3.16 (the singularities $y^a = x^b$).** In Example P5.3.7, $\mathcal{O}_P$ is spanned by the $t^n$ with $n \in \langle a, b \rangle$, and $t^n \widetilde{\mathcal{O}}_P \subseteq \mathcal{O}_P$ if and only if every integer $\geq n$ lies in the semigroup. So $\mathfrak{c}_P = t^c \widetilde{\mathcal{O}}_P$ with $c = (a-1)(b-1)$ by Exercise 2 of Section 3.1, and $\ell(\widetilde{\mathcal{O}}_P / \mathfrak{c}_P) = c = 2 \delta_P$. Theorem P5.3.13 for this plane curve is the symmetry of the semigroup: exactly half of $0, \dots, c - 1$ are gaps. For the cusp, $\mathfrak{c}_P = t^2 k[t]_{(t)}$, matching the description of $K_A$ as $A \, dt / t^2$ in Example P4.8.26.

**Example P5.3.17 (a non-Gorenstein point).** For the semigroup $\langle 3, 4, 5 \rangle$ of Exercise 4 of Section 3.1, the gaps are $1, 2$, so $\delta_P = 2$, and every integer $\geq 3$ lies in the semigroup, so $\mathfrak{c}_P = t^3 \widetilde{\mathcal{O}}_P = \mathfrak{m}_P$ and $\ell(\widetilde{\mathcal{O}}_P / \mathfrak{c}_P) = 3 \neq 4$. By Theorem P5.3.13 this point is not Gorenstein, and the curve $t \mapsto [1 : t^3 : t^4 : t^5]$ is not a local complete intersection at $P$. The same count for the three coordinate axes of Example P5.3.9 gives $\mathfrak{c} = \mathfrak{m}$, $\ell(\widetilde{\mathcal{O}} / \mathfrak{c}) = 3$ and $\delta = 2$.

**Example P5.3.18 (canonical maps of singular curves).** Let $C$ be a plane quartic with one node, so $p_a = 3$ and $g(\widetilde{C}) = 2$. By Example P4.7.23, $\omega^\circ_C = \mathcal{O}_C(1)$, and $H^0(\omega^\circ_C)$ is spanned by $x, y, z$, the canonical map being the plane embedding. Its pullback $\nu^* \mathcal{O}_C(1)$ has degree $4$ on $\widetilde{C}$, and $\nu^* \omega^\circ_C \cong \omega_{\widetilde{C}}(Q_1 + Q_2)$ for the two branches $Q_1, Q_2$ over the node (Exercise 4), of degree $2 + 2 = 4 = 2 p_a - 2$, as Corollary P5.3.14 predicts. So a line through the node cuts $Q_1 + Q_2$ plus a canonical divisor of $\widetilde{C}$: these are the *adjoint* lines, and they give the canonical system of the genus $2$ curve $\widetilde{C}$.

### Proof

*Theorem P5.3.10.* Tensoring $0 \to \mathcal{O}_C \to \nu_* \mathcal{O}_{\widetilde{C}} \to \mathcal{Q} \to 0$ with the locally free $\mathcal{L}$ is exact, and $\mathcal{L} \otimes \nu_* \mathcal{O}_{\widetilde{C}} \cong \nu_* \nu^* \mathcal{L}$ by the projection formula. Since $\mathcal{Q}$ has finite support and $\mathcal{L}$ is trivial near each point, $\mathcal{L} \otimes \mathcal{Q} \cong \mathcal{Q}$. By Proposition P4.1.19 and Theorem P5.1.10,
$$\chi(\mathcal{L}) = \chi(\widetilde{C}, \nu^* \mathcal{L}) - \sum_P \delta_P = \deg \mathcal{L} + 1 - g(\widetilde{C}) - \sum_P \delta_P = \deg \mathcal{L} + 1 - p_a(C),$$
the last step by Proposition P5.3.2. The duality statement is Corollary P4.7.19 with $n = 1$, $i = 1$, $\mathcal{E} = \mathcal{L}$.

*Proposition P5.3.11.* By Proposition P4.9.7 and part 2 of Theorem P4.7.18, the dualizing complex of the Cohen-Macaulay curve $C$ has a single cohomology sheaf, and $\omega^\bullet_C \cong \omega^\circ_C[1]$. For the smooth curve $\widetilde{C}$, $\omega^\bullet_{\widetilde{C}} \cong \omega_{\widetilde{C}}[1]$ by Corollary P4.7.21.

Part 1. Let $i \colon \operatorname{Spec} k \to C$ be the inclusion of a closed point $P$, a finite morphism of projective schemes. The dualizing complex of a point is $k[0]$, so by part 2 of Theorem P4.9.13 and Corollary P4.9.14,
$$R\mathcal{H}om(k(P), \omega^\circ_C[1]) \cong i_* i^! \omega^\bullet_C \cong i_* \omega^\bullet_{\operatorname{Spec} k} = k(P)[0].$$
So $\mathcal{E}xt^j(k(P), \omega^\circ_C)$ is $k(P)$ for $j = 1$ and zero otherwise. A coherent sheaf $\mathcal{T}$ with finite support has a filtration with quotients $k(P)$, by Proposition P1.3.28 applied to each stalk, and the long exact sequences of $\mathcal{E}xt$ show by induction on the length that $\mathcal{H}om(\mathcal{T}, \omega^\circ_C) = 0$, $\mathcal{E}xt^j(\mathcal{T}, \omega^\circ_C) = 0$ for $j \geq 2$, and $\ell(\mathcal{E}xt^1(\mathcal{T}, \omega^\circ_C)_P) = \ell(\mathcal{T}_P)$. The rank of $\omega^\circ_C$ is $1$ because $\omega^\circ_C$ is isomorphic to $\omega_U$ on the smooth open set $U$ (Corollary P4.7.21 and the uniqueness of Proposition P4.7.15 applied on $U$).

Part 2. Corollary P4.9.14 for the finite morphism $\nu$ gives
$$\nu_* \omega_{\widetilde{C}}[1] \cong R\mathcal{H}om(\nu_* \mathcal{O}_{\widetilde{C}}, \omega^\circ_C[1]).$$
Comparing cohomology sheaves, $\nu_* \omega_{\widetilde{C}} \cong \mathcal{H}om(\nu_* \mathcal{O}_{\widetilde{C}}, \omega^\circ_C)$ and $\mathcal{E}xt^1(\nu_* \mathcal{O}_{\widetilde{C}}, \omega^\circ_C) = 0$.

Part 3. Apply $\mathcal{H}om(-, \omega^\circ_C)$ to $0 \to \mathcal{O}_C \to \nu_* \mathcal{O}_{\widetilde{C}} \to \mathcal{Q} \to 0$:
$$0 \to \mathcal{H}om(\mathcal{Q}, \omega^\circ_C) \to \nu_* \omega_{\widetilde{C}} \to \omega^\circ_C \to \mathcal{E}xt^1(\mathcal{Q}, \omega^\circ_C) \to \mathcal{E}xt^1(\nu_* \mathcal{O}_{\widetilde{C}}, \omega^\circ_C).$$
The first term is zero by part 1 and the last by part 2. So $\nu_* \omega_{\widetilde{C}} \to \omega^\circ_C$ is injective with cokernel $\mathcal{E}xt^1(\mathcal{Q}, \omega^\circ_C)$, of length $\ell(\mathcal{Q}_P) = \delta_P$ at $P$ by part 1.

*Theorem P5.3.13.* Write $\mathcal{O} = \mathcal{O}_P$ and $\widetilde{\mathcal{O}} = \widetilde{\mathcal{O}}_P$, and fix an isomorphism $\omega^\circ_{C,P} \cong \mathcal{O}$. By part 2 of Proposition P5.3.11, $(\nu_* \omega_{\widetilde{C}})_P \cong \operatorname{Hom}_{\mathcal{O}}(\widetilde{\mathcal{O}}, \mathcal{O})$, embedded in $\mathcal{O}$ by $\varphi \mapsto \varphi(1)$. An $\mathcal{O}$-linear $\varphi \colon \widetilde{\mathcal{O}} \to \mathcal{O}$ extends to a $K$-linear map $K = \widetilde{\mathcal{O}} \otimes_{\mathcal{O}} K \to K$, which is multiplication by $a = \varphi(1)$, and $a \widetilde{\mathcal{O}} = \varphi(\widetilde{\mathcal{O}}) \subseteq \mathcal{O}$, so $a \in \mathfrak{c}_P$. Conversely every $a \in \mathfrak{c}_P$ defines such a $\varphi$. So the image of $(\nu_* \omega_{\widetilde{C}})_P$ in $\omega^\circ_{C,P} = \mathcal{O}$ is $\mathfrak{c}_P$, and it is an $\widetilde{\mathcal{O}}$-module isomorphism since $\widetilde{\mathcal{O}}$ acts on $\operatorname{Hom}_{\mathcal{O}}(\widetilde{\mathcal{O}}, \mathcal{O})$ through its argument. Part 3 of Proposition P5.3.11 gives $\ell(\mathcal{O} / \mathfrak{c}_P) = \delta_P$, and additivity of length on $\mathfrak{c}_P \subseteq \mathcal{O} \subseteq \widetilde{\mathcal{O}}$ gives $\ell(\widetilde{\mathcal{O}} / \mathfrak{c}_P) = \delta_P + \delta_P$.

*Corollary P5.3.14.* Let $P \in C$ and embed $C \subseteq \mathbb{P}^m$, with $R = \mathcal{O}_{\mathbb{P}^m, P}$ regular local of dimension $m$ and $\mathcal{O}_P = R/J$. By Proposition P4.9.7 and Theorem P4.7.18, $\omega^\circ_{C,P} \cong \operatorname{Ext}^{m-1}_R(\mathcal{O}_P, R)$, the canonical module $K_{\mathcal{O}_P}$ of Definition P4.8.22, up to the twist by the invertible $\omega_{\mathbb{P}^m}$. If $J$ is generated by a regular sequence, $K_{\mathcal{O}_P} \cong \mathcal{O}_P$ by part 3 of Proposition P4.8.23, so $\omega^\circ_C$ is invertible at $P$. A plane curve is a hypersurface, so this applies. On a Gorenstein curve, Serre duality gives $h^0(\omega^\circ_C) = h^1(\mathcal{O}_C) = p_a(C)$ and $h^1(\omega^\circ_C) = h^0(\mathcal{O}_C) = 1$, so $\chi(\omega^\circ_C) = p_a(C) - 1$, and Theorem P5.3.10 for $\mathcal{L} = \omega^\circ_C$ gives $\deg \omega^\circ_C = 2 p_a(C) - 2$. The last formula is Theorem P5.3.10.

### Exercises

1. (A) Show that $\deg(\mathcal{L} \otimes \mathcal{M}) = \deg \mathcal{L} + \deg \mathcal{M}$, and that $\deg \mathcal{O}_C(D) = \ell(\mathcal{O}_D)$ for an effective Cartier divisor $D$ on $C$.
2. (A) Compute the conductor of $y^2 = x^4 + x^5$ at the origin and check Theorem P5.3.13.
3. (B) Show that an invertible sheaf of degree $> 2 p_a(C) - 2$ on a Gorenstein curve has $h^1 = 0$, and that one of degree $\geq 2 p_a(C)$ is generated by global sections.
4. (B) Let $P$ be a node with branches $Q_1, Q_2$. Show that $\nu^* \omega^\circ_C \cong \omega_{\widetilde{C}}(Q_1 + Q_2)$ near $P$, and that a local section of $\omega_{\widetilde{C}}(Q_1 + Q_2)$ comes from $\omega^\circ_C$ if and only if its residues at $Q_1$ and $Q_2$ sum to zero.
5. (B) Show that a curve with $p_a(C) = 1$ that is Gorenstein has $\omega^\circ_C \cong \mathcal{O}_C$, and deduce that the nodal and cuspidal cubics have trivial dualizing sheaf, while their normalizations have $\omega \cong \mathcal{O}(-2)$.
6. (C) Prove the converse of Theorem P5.3.13: if $\ell(\widetilde{\mathcal{O}}_P / \mathfrak{c}_P) = 2 \delta_P$, then $P$ is a Gorenstein point. Use that $\omega^\circ_{C,P}$ is generated by one element if and only if $\omega^\circ_{C,P} / \mathfrak{m}_P \omega^\circ_{C,P}$ is one-dimensional, and compare with the dual of $\mathcal{O}_P / \mathfrak{c}_P$.

### Lean

Mathlib has the annihilator of a module and the integral closure, so the conductor of an extension of rings can be stated, but not the dualizing sheaf of a singular curve or Riemann-Roch on it. The handbook adds no `MinimalModel` node here.

### Notes and history

Rosenlicht described the dualizing sheaf of a singular curve in 1952 as the sheaf of *regular differentials*, the meromorphic differentials $\eta$ on $\widetilde{C}$ with $\sum_{Q \mapsto P} \operatorname{res}_Q(f \eta) = 0$ for every $f \in \mathcal{O}_P$, and proved Riemann-Roch in this form. Serre's *Algebraic groups and class fields* uses this description to define generalized Jacobians, and proves there that $\ell(\widetilde{\mathcal{O}}_P / \mathfrak{c}_P) \leq 2 \delta_P$, with equality exactly at Gorenstein points; the equivalence of this notion with Definition P1.10.24 is the theorem of Herzog and Kunz cited in the notes to Section 8.3 of P4. The literature state is theorem. In the minimal model program, the singular curves that occur as log canonical centres in dimension one are nodal, and the Gorenstein condition, that $\omega^\circ$ be invertible, is the one-dimensional case of the condition that $K_X$ be Cartier, which Volume 4 relaxes to $\mathbb{Q}$-Cartier.
