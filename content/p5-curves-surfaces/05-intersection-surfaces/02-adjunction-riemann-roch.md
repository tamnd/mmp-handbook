---
title: Adjunction and Riemann-Roch on a surface
nodes: []
sources: [Har77, Bea96, Rei97]
reads_with: [Har77:V.1, Bea96:ch1]
requires: [P3.12, P4.3, P4.7, P5.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Adjunction and Riemann-Roch on a surface

### Statement

As in Section 5.1, $S$ is a smooth projective surface over an algebraically closed field $k$. Its *canonical sheaf* is $\omega_S = \bigwedge^2 \Omega_S$, and a *canonical divisor* $K = K_S$ is a divisor with $\mathcal{O}_S(K) \cong \omega_S$. For a curve $C$ on $S$, that is, a nonzero effective divisor, the *arithmetic genus* is $p_a(C) = 1 - \chi(\mathcal{O}_C)$. For an integral curve $h^0(\mathcal{O}_C) = 1$ (Example P3.4.27), so $p_a(C) = h^1(\mathcal{O}_C)$, as in Chapter 3. The dualizing sheaf $\omega^\circ_C$ is the one of Section P4.7.

**Proposition P5.5.12 (restriction to a curve).** For every curve $C$ on $S$ and every invertible $\mathcal{L}$,
$$(\mathcal{L} \cdot \mathcal{O}_S(C)) = \chi(\mathcal{L}|_C) - \chi(\mathcal{O}_C).$$

Lean: not in Lean as stated.

**Theorem P5.5.13 (Riemann-Roch for surfaces).** For every divisor $D$ on $S$,
$$\chi(\mathcal{O}_S(D)) = \chi(\mathcal{O}_S) + \tfrac{1}{2} D \cdot (D - K).$$
In particular $D \cdot (D - K)$ is even, and
$$h^0(\mathcal{O}_S(D)) + h^0(\mathcal{O}_S(K - D)) \geq \chi(\mathcal{O}_S) + \tfrac{1}{2} D \cdot (D - K).$$

Lean: not in Lean as stated.

**Theorem P5.5.14 (adjunction formula).** Let $C$ be a curve on $S$.

1. $\omega^\circ_C \cong \omega_S(C)|_C = \mathcal{O}_C(K + C)$. In particular $\omega^\circ_C$ is invertible.
2. (*Genus formula.*) $2 p_a(C) - 2 = C \cdot (C + K)$.
3. If $C$ is integral with normalization $\widetilde{C}$, then $\frac{1}{2} C \cdot (C + K) + 1 = g(\widetilde{C}) + \sum_P \delta_P$. If $C$ is smooth, $\omega_C \cong \mathcal{O}_C(K + C)$ and $\deg \omega_C = C^2 + K \cdot C$.

Lean: not in Lean as stated.

**Corollary P5.5.15 (curves of arithmetic genus $0$).** Let $C$ be an integral curve on $S$.

1. $C^2 + K \cdot C \geq -2$, with equality if and only if $C \cong \mathbb{P}^1$.
2. If $C^2 < 0$ and $K \cdot C < 0$, then $C \cong \mathbb{P}^1$ and $C^2 = K \cdot C = -1$.
3. If $C^2 < 0$ and $K \cdot C = 0$, then $C \cong \mathbb{P}^1$ and $C^2 = -2$.

A smooth rational curve with $C^2 = -1$ is a *$(-1)$-curve*, and one with $C^2 = -2$ is a *$(-2)$-curve*.

Lean: not in Lean as stated.

### Proof in words

Riemann-Roch is the definition of the intersection pairing read backwards. The number $-D \cdot (D - K)$ is a combination of four Euler characteristics, $\chi(\mathcal{O}_S)$, $\chi(\mathcal{O}_S(D))$, $\chi(\mathcal{O}_S(K - D))$ and $\chi(\mathcal{O}_S(K))$, and Serre duality pairs them off. The genus formula is Riemann-Roch for $-C$, through $\chi(\mathcal{O}_C) = \chi(\mathcal{O}_S) - \chi(\mathcal{O}_S(-C))$. The adjunction formula for the dualizing sheaf is the formula of Theorem P4.7.20 for a local complete intersection, applied to $C$ and to $S$ in the same projective space. Corollary P5.5.15 then combines the genus formula with $p_a \geq 0$ and the parity of $C^2 + K \cdot C$.

### Examples

**Example P5.5.16 (the projective plane).** On $\mathbb{P}^2$, $K = -3\ell$ by Corollary P3.12.22. A curve $C$ of degree $d$ has $C \cdot (C + K) = d(d - 3)$, so
$$p_a(C) = \tfrac{1}{2}(d - 1)(d - 2),$$
for every curve of degree $d$, reduced or not. A double line has $p_a = 0$ and a triple line $p_a = 1$, the same as a smooth conic and a smooth cubic. Riemann-Roch gives $\chi(\mathcal{O}(d)) = 1 + \frac{1}{2} d (d + 3) = \binom{d + 2}{2}$, as it must by Theorem P4.2.1. So the integral plane curves with $p_a = 0$ are the lines and the smooth conics, as Corollary P5.5.15 predicts. A rational cubic is singular, with $\sum_P \delta_P = 1$, a node or a cusp.

**Example P5.5.17 (curves on the quadric surface).** On $\mathbb{P}^1 \times \mathbb{P}^1$, with $F_1, F_2$ as in Example P5.5.9, Proposition P3.12.23 gives $\omega \cong p_1^* \omega_{\mathbb{P}^1} \otimes p_2^* \omega_{\mathbb{P}^1}$, so $K = -2F_1 - 2F_2$ and $K^2 = 8$. A curve $C$ of class $a F_1 + b F_2$ has $C^2 = 2ab$ and $K \cdot C = -2a - 2b$, so
$$p_a(C) = (a - 1)(b - 1).$$
The projection $p_1$ restricted to $C$ has fibres $F_1 \cap C$, of degree $C \cdot F_1 = b$. So a smooth curve of class $(g + 1) F_1 + 2 F_2$ has genus $g$ and a map of degree $2$ to $\mathbb{P}^1$: it is hyperelliptic when $g \geq 2$. Such smooth curves exist by Lemma P5.5.2: $\mathcal{O}(a, b)$ is very ample for $a, b \geq 1$, by the Segre embedding of the Veronese embeddings, and $H^1(\mathcal{O}(-a, -b)) = 0$ by the Künneth formula.

**Example P5.5.18 (lines on surfaces in $\mathbb{P}^3$).** Let $S \subseteq \mathbb{P}^3$ be a smooth surface of degree $d$, with plane section $H$. By Corollary P3.12.31, $\omega_S \cong \mathcal{O}_S(d - 4)$, so $K = (d - 4) H$. A line $L \subseteq S$ has $H \cdot L = 1$, and the genus formula with $p_a(L) = 0$ gives
$$L^2 = -2 - K \cdot L = 2 - d.$$
On a quadric $L^2 = 0$: lines are fibres of the two rulings, as in Example P5.5.9. On a smooth cubic surface each line is a $(-1)$-curve, the $27$ lines of Chapter 10. On a smooth quartic $K = 0$ and each line is a $(-2)$-curve. For instance, in characteristic different from $2$, the Fermat quartic $x_0^4 + x_1^4 + x_2^4 + x_3^4 = 0$ contains the line $x_0 = \zeta x_1$, $x_2 = \zeta' x_3$ for every pair of fourth roots $\zeta, \zeta'$ of $-1$.

**Example P5.5.19 (graphs on a product of curves).** Let $C$ be a smooth projective curve of genus $g$, $S = C \times C$, and $f_1 = \{x\} \times C$, $f_2 = C \times \{y\}$ the fibres of the projections. By Proposition P3.12.23, $K_S = p_1^* K_C + p_2^* K_C$. For a morphism $\varphi \colon C \to C$ of degree $d \geq 1$, let $\Gamma \subseteq S$ be its graph, isomorphic to $C$ through $p_1$, with $p_2|_\Gamma = \varphi$. By Theorem P5.5.6,
$$\Gamma \cdot f_1 = \deg \mathcal{O}_C(x) = 1, \qquad \Gamma \cdot f_2 = \deg \varphi^* \mathcal{O}_C(y) = d, \qquad K_S \cdot \Gamma = (2g - 2) + d (2g - 2).$$
The genus formula for the smooth curve $\Gamma$ of genus $g$ gives $2g - 2 = \Gamma^2 + K_S \cdot \Gamma$, so
$$\Gamma^2 = d (2 - 2g).$$
For the diagonal, $d = 1$ and $\Delta^2 = 2 - 2g$. This is $2$ on $\mathbb{P}^1 \times \mathbb{P}^1$ (Example P5.5.9) and $0$ on $E \times E$ (Example P5.4.9). The normal bundle of $\Gamma$ is the quotient of $T_S|_\Gamma = T_C \oplus \varphi^* T_C$ by the image of $v \mapsto (v, d\varphi(v))$, which is isomorphic to $\varphi^* T_C$ through $(a, b) \mapsto b - d\varphi(a)$. Its degree is $d(2 - 2g)$, the same answer.

### Proof

*Proposition P5.5.12.* The proof of Theorem P5.5.6 shows, for every curve $C$, integral or not, and every invertible $\mathcal{M}$, that $(\mathcal{M} \cdot \mathcal{O}_S(C)) = \chi(\mathcal{O}_C) - \chi(\mathcal{M}^{-1}|_C)$. Take $\mathcal{M} = \mathcal{L}^{-1}$, and use $(\mathcal{L}^{-1} \cdot \mathcal{O}_S(C)) = -(\mathcal{L} \cdot \mathcal{O}_S(C))$ from bilinearity. $\square$

*Theorem P5.5.13.* By Definition P5.5.4 with $\mathcal{L} = \mathcal{O}_S(-D)$ and $\mathcal{M} = \mathcal{O}_S(D - K)$,
$$(-D) \cdot (D - K) = \chi(\mathcal{O}_S) - \chi(\mathcal{O}_S(D)) - \chi(\mathcal{O}_S(K - D)) + \chi(\mathcal{O}_S(K)).$$
By Serre duality (Corollary P4.7.21), $h^i(\mathcal{O}_S(K - D)) = h^{2 - i}(\mathcal{O}_S(D))$ for every $i$, so $\chi(\mathcal{O}_S(K - D)) = \chi(\mathcal{O}_S(D))$, and in the same way $\chi(\mathcal{O}_S(K)) = \chi(\mathcal{O}_S)$. So $-D \cdot (D - K) = 2 \chi(\mathcal{O}_S) - 2 \chi(\mathcal{O}_S(D))$, which is the formula. Since both $\chi$ are integers, $D \cdot (D - K)$ is even. The inequality follows from $\chi(\mathcal{O}_S(D)) \leq h^0(\mathcal{O}_S(D)) + h^2(\mathcal{O}_S(D))$ and $h^2(\mathcal{O}_S(D)) = h^0(\mathcal{O}_S(K - D))$. $\square$

*Theorem P5.5.14.* Part 2 first. From $0 \to \mathcal{O}_S(-C) \to \mathcal{O}_S \to \mathcal{O}_C \to 0$ and Theorem P5.5.13 for $D = -C$,
$$\chi(\mathcal{O}_C) = \chi(\mathcal{O}_S) - \chi(\mathcal{O}_S(-C)) = -\tfrac{1}{2} (-C) \cdot (-C - K) = -\tfrac{1}{2} C \cdot (C + K).$$
So $2 p_a(C) - 2 = -2 \chi(\mathcal{O}_C) = C \cdot (C + K)$.

Part 1. Embed $S$ as a closed subscheme of $P = \mathbb{P}^N$. Near a point $x$ of $C$, the ideal of $S$ in $\mathcal{O}_P$ is generated by a regular sequence $h_1, \dots, h_{N-2}$, since $S$ is smooth of codimension $N - 2$: by Theorem P3.12.14 the ideal is generated near $x$ by $N - 2$ functions with independent differentials, which are part of a regular system of parameters of $\mathcal{O}_{P,x}$, hence a regular sequence (Proposition P1.9.4). The ideal of $C$ is generated by the $h_i$ together with a lift $h$ of a local equation $f$ of $C$ on $S$. Since $f$ is a nonzerodivisor on $\mathcal{O}_S$, the sequence $h_1, \dots, h_{N-2}, h$ is regular. So Theorem P4.7.20 applies to both $S$ and $C$:
$$\omega^\circ_S \cong \omega_P|_S \otimes \det \mathcal{N}_{S/P}, \qquad \omega^\circ_C \cong \omega_P|_C \otimes \det \mathcal{N}_{C/P},$$
and $\omega^\circ_S \cong \omega_S$ by Corollary P4.7.21. Let $\mathcal{I}_S \subseteq \mathcal{I}_C$ be the ideals in $\mathcal{O}_P$. The conormal sequence
$$\mathcal{I}_S / \mathcal{I}_S^2 \otimes \mathcal{O}_C \to \mathcal{I}_C / \mathcal{I}_C^2 \to \mathcal{O}_S(-C) / \mathcal{O}_S(-2C) \to 0$$
is right exact. Its terms are locally free on $C$, of ranks $N - 2$, $N - 1$ and $1$, the last one equal to $\mathcal{O}_C(-C)$. The kernel of the surjection on the right is locally free of rank $N - 2$, and the first map is a surjection of locally free sheaves of the same rank onto it, hence an isomorphism. So the sequence is exact on the left as well, and Lemma P3.12.21 gives $\det \mathcal{C}_{C/P} \cong \det \mathcal{C}_{S/P}|_C \otimes \mathcal{O}_C(-C)$. Dualizing, $\det \mathcal{N}_{C/P} \cong \det \mathcal{N}_{S/P}|_C \otimes \mathcal{O}_C(C)$, and
$$\omega^\circ_C \cong \big( \omega_P|_S \otimes \det \mathcal{N}_{S/P} \big)|_C \otimes \mathcal{O}_C(C) \cong \omega_S(C)|_C.$$

Part 3. For $C$ integral, $p_a(C) = g(\widetilde{C}) + \sum_P \delta_P$ by Proposition P5.3.2, and part 2 gives the formula. If $C$ is smooth, $\omega^\circ_C \cong \omega_C$ by Corollary P4.7.21, and Theorem P3.12.30 gives the same isomorphism directly. Then $\deg \omega_C = \deg \mathcal{O}_C(K + C) = (K + C) \cdot C$ by Theorem P5.5.6. $\square$

*Corollary P5.5.15.* By Corollary P5.3.3, $p_a(C) \geq 0$, with equality if and only if $C \cong \mathbb{P}^1$. By the genus formula $C^2 + K \cdot C = 2 p_a(C) - 2 \geq -2$, with the same case of equality, which is part 1. In part 2, $C^2 \leq -1$ and $K \cdot C \leq -1$, so $C^2 + K \cdot C \leq -2$. By part 1 equality holds, $C \cong \mathbb{P}^1$ and $C^2 = K \cdot C = -1$. In part 3, $C^2 + K \cdot C = C^2 \leq -1$ is even, so it is $-2$, and part 1 applies. $\square$

### Exercises

1. (A) Show that $K^2 = 9$ on $\mathbb{P}^2$ and $K^2 = 8$ on $\mathbb{P}^1 \times \mathbb{P}^1$. Check Noether's formula $12 \chi(\mathcal{O}_S) = K^2 + e(S)$ in both cases, with $e(\mathbb{P}^2) = 3$ and $e(\mathbb{P}^1 \times \mathbb{P}^1) = 4$.
2. (A) Let $S \subseteq \mathbb{P}^3$ be a smooth cubic surface, $L \subseteq S$ a line and $\Pi$ a plane through $L$, with $\Pi \cap S = L + C$. Show that $C \cdot L = 2$, $C^2 = 0$ and $K \cdot C = -2$, and that $C$ is a conic with $p_a(C) = 0$.
3. (B) Show that $D^2 \equiv K \cdot D \pmod 2$ for every divisor $D$. Deduce that if $K \equiv 0$, then $D^2$ is even for every $D$.
4. (B) Let $C$ and $D$ be curves on $S$. Show that $p_a(C + D) = p_a(C) + p_a(D) + C \cdot D - 1$. Deduce that a curve whose components are smooth rational curves, meeting transversally with dual graph a tree, has $p_a = 0$.
5. (B) Let $S$ be a smooth quartic surface in $\mathbb{P}^3$, so that $K = 0$ and $\chi(\mathcal{O}_S) = 2$. Let $C \subseteq S$ be an integral curve with $C^2 \geq 0$. Show that $h^0(\mathcal{O}_S(C)) \geq 2 + \frac{1}{2} C^2$, and that $C$ moves in its linear system.
6. (C) Let $C$ be a smooth curve of degree $d$ and genus $g$ on a smooth quadric $Q \subseteq \mathbb{P}^3$, of class $a F_1 + b F_2$. Show that $a + b = d$ and $g = (a - 1)(b - 1)$, and deduce $g \leq \lfloor d^2/4 \rfloor - d + 1$. Show that the twisted cubic lies on a quadric with class $F_1 + 2F_2$, and that no smooth curve of degree $4$ and genus $2$ lies on a quadric.

### Lean

Mathlib does not formalize Euler characteristics of sheaves on schemes, Serre duality or dualizing sheaves, so neither Riemann-Roch for surfaces nor the adjunction formula can be stated there yet. The handbook adds no `MinimalModel` node here.

### Notes and history

Riemann-Roch for surfaces was found by Castelnuovo and Enriques in the 1890s, in the form of an inequality for the dimension of a linear system, and the formula with $\chi$ is due to Zariski and to Serre. Noether's formula $12 \chi(\mathcal{O}_S) = K^2 + e(S)$, with $e(S)$ the topological Euler characteristic over $\mathbb{C}$ or the $\ell$-adic one in general, is the deeper half of Hirzebruch-Riemann-Roch on a surface and is not used in this volume. The literature state is theorem. In the minimal model program, the genus formula is the reason the curves the program contracts on a surface are smooth rational curves, and its higher-dimensional form, adjunction for a divisor with log canonical singularities, is the subject of Volume 4. Corollary P5.5.15 is the first appearance of the dichotomy between $(-1)$-curves, which the program contracts, and $(-2)$-curves, which are $K$-trivial and become the Du Val singularities of canonical models.
