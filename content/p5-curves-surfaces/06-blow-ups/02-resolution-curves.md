---
title: Resolution of curve singularities by blow-ups
nodes: []
sources: [Har77, Bea96, Rei97]
reads_with: [Har77:V.3, Bea96:ch2]
requires: [P3.11, P5.1, P5.3, P5.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Resolution of curve singularities by blow-ups

### Statement

As in Section 6.1, $S$ is a smooth projective surface over an algebraically closed field $k$. A *sequence of blow-ups* of $S$ is a chain $S_n \to S_{n-1} \to \dots \to S_0 = S$ in which each $\pi_i \colon S_i \to S_{i-1}$ is the blow-up of a closed point $q_i \in S_{i-1}$, the *centre*, with exceptional curve $E_i$. By Theorem P5.6.2 every $S_i$ is again a smooth projective surface, so Section 6.1 applies at each step. For a curve $C$ on $S$, its *strict transform* $C_i$ on $S_i$ is the strict transform of $C_{i-1}$ under $\pi_i$, and its *total transform* is the pullback of $C$ to $S_i$. The strict transforms of $E_1, \dots, E_n$ on $S_n$ are the *exceptional curves* of $S_n \to S$. A point of some $S_i$ that maps to $p \in S$ is *infinitely near* to $p$.

**Definition P5.6.12 (simple normal crossings).** A reduced curve $D = D_1 + \dots + D_r$ on $S$, with distinct integral components $D_j$, has *simple normal crossings* if every $D_j$ is smooth, no point lies on three of the $D_j$, and $(D_i \cdot D_j)_q = 1$ at every point $q \in D_i \cap D_j$, $i \neq j$. By Proposition P5.5.5 the last condition means that $D_i$ and $D_j$ meet transversally at $q$. A curve $C$ has simple normal crossings *at $q$* if this holds for the components of $C_{\mathrm{red}}$ through $q$.

**Lemma P5.6.13 (blow-ups keep simple normal crossings).** Let $G$ be a reduced curve with simple normal crossings, $q \in S$ a closed point and $\pi \colon \tilde S \to S$ the blow-up of $q$. Then the reduced total transform $\tilde G + E$ has simple normal crossings, and $\tilde G \cdot E = m_q(G)$, the number of components of $G$ through $q$.

Lean: not in Lean as stated.

**Proposition P5.6.14 (the $\delta$-invariant under a blow-up).** Let $C$ be an integral curve on $S$ and $p \in C$ a point of multiplicity $m$. Then the strict transform $\tilde C$ is an integral curve with the same normalization as $C$, and
$$\delta_p(C) = \frac{m(m-1)}{2} + \sum_{q \in \tilde C \cap E} \delta_q(\tilde C).$$

Lean: not in Lean as stated.

**Theorem P5.6.15 (resolution of the singularities of a curve).** Let $C$ be an integral curve on $S$. Blow up a singular point of $C$, then a singular point of its strict transform, and so on. The process stops after at most $p_a(C) - g(\tilde C^\nu)$ blow-ups, where $g(\tilde C^\nu)$ is the geometric genus of $C$, and the last strict transform $C_n$ is smooth. The morphism $C_n \to C$ is the normalization of $C$.

Lean: not in Lean as stated.

**Corollary P5.6.16 (the $\delta$-invariant from infinitely near points).** In Theorem P5.6.15, let $p \in C$, let $q_{i_1}, \dots, q_{i_s}$ be the centres that lie over $p$, and let $m_j$ be the multiplicity of the strict transform $C_{i_j - 1}$ at $q_{i_j}$. Then
$$\delta_p(C) = \sum_{j = 1}^{s} \frac{m_j (m_j - 1)}{2} .$$
In particular $\delta_p(C) = m_p(C)(m_p(C) - 1)/2$ if and only if the strict transform $\tilde C$ is smooth at every point of $E$.

Lean: not in Lean as stated.

**Theorem P5.6.17 (embedded resolution of curves).** Let $C$ be a curve on $S$. There is a sequence of blow-ups $\pi \colon S' \to S$, each centre lying over a singular point of $C_{\mathrm{red}}$, such that the support of the total transform $\pi^* C$ is a curve with simple normal crossings. In particular $\pi$ is an isomorphism over the smooth locus of $C_{\mathrm{red}}$.

Lean: not in Lean as stated.

**Corollary P5.6.18 (Noether's formula for intersection multiplicities).** Let $C$ and $D$ be curves on $S$ with no common component, and $p \in C \cap D$. Blow up $p$, then the points over $p$ where the strict transforms of $C$ and $D$ meet, and so on. The process stops after finitely many steps, with strict transforms that do not meet over $p$, and
$$(C \cdot D)_p = \sum_{i} m_{q_i}(C_{i-1}) \, m_{q_i}(D_{i-1}),$$
the sum over the centres $q_i$, with $C_{i-1}$ and $D_{i-1}$ the strict transforms on $S_{i-1}$.

Lean: not in Lean as stated.

### Proof in words

Every blow-up of a singular point of an integral curve lowers the arithmetic genus of its strict transform by $m(m-1)/2 \geq 1$, and the arithmetic genus of an integral curve is at least its geometric genus, which does not change. So the singular points disappear after finitely many steps, and the $\delta$-invariant, which accounts for the drop of $p_a$ point by point, is the sum of the numbers $m(m-1)/2$ along the way. Embedded resolution adds two more counts. Blowing up a common point of two smooth components lowers their intersection number by $1$, so finitely many blow-ups separate the components. After that, every component meets the exceptional curves, which already have simple normal crossings, and a blow-up at a bad point lowers the local intersection number with the exceptional curves, or turns a tangency into a transverse triple point, which the next blow-up separates. Noether's formula is Proposition P5.6.6 applied at every common point until the curves come apart.

### Examples

**Example P5.6.19 (embedded resolution of the cusp).** Let $C \subseteq \mathbb{P}^2$ be the cuspidal cubic $y^2 z = x^3$, with the cusp at $p = [0 : 0 : 1]$, and work in the affine coordinates $x, y$. The first blow-up, in the chart $y = xt$, gives $\pi_1^* C = C_1 + 2E_1$ with $C_1 = V(t^2 - x)$ smooth and $E_1 = V(x)$. The two meet only at $q_2 = (0, 0)$, with $(C_1 \cdot E_1)_{q_2} = 2$: both have the tangent direction $x = 0$. Blowing up $q_2$, in the chart $x = tw$, gives $C_2 = V(w - t)$, the strict transform $V(w)$ of $E_1$, and $E_2 = V(t)$: three lines through $q_3 = (0, 0)$ with distinct directions. Since $q_2$ has multiplicity $1$ on $C_1$ and on $E_1$, the total transform is $C_2 + 2E_1 + 3E_2$. Blowing up $q_3$, which has multiplicity $1$ on all three curves, separates them, and
$$\pi^* C = C_3 + 2E_1 + 3E_2 + 6E_3 ,$$
writing $E_i$ also for the strict transforms on $S_3$. By part 4 of Proposition P5.6.4, $E_1^2 = -1 - 1 - 1 = -3$, $E_2^2 = -2$, $E_3^2 = -1$ and $C_3^2 = 9 - 4 - 1 - 1 = 3$. The curves $C_3$, $E_1$ and $E_2$ are disjoint, and each meets $E_3$ once, transversally: the support of $\pi^* C$ has simple normal crossings. As a check, $\pi^* C \cdot E_3 = 1 + 2 + 3 - 6 = 0$, $\pi^* C \cdot E_1 = 2 \cdot (-3) + 6 = 0$ and $\pi^* C \cdot E_2 = 3 \cdot (-2) + 6 = 0$, as Theorem P5.6.3 requires. Only the first centre is a singular point of the strict transform, so Corollary P5.6.16 gives $\delta_p = 1$, as in Example P5.3.7.

**Example P5.6.20 (two tangent conics).** Let $\operatorname{char} k \neq 2$, and let $A = V(yz - x^2)$ and $B = V(yz + x^2)$, which meet at $p = [0 : 0 : 1]$ with $(A \cdot B)_p = \dim_k k[x]_{(x)}/(2x^2) = 2$. Both are smooth at $p$ with tangent direction $y = 0$. After one blow-up, in the chart $y = xt$, $\tilde A = V(t - x)$ and $\tilde B = V(t + x)$ meet transversally at the point $t = 0$ of $E_1$, so Noether's formula reads $(A \cdot B)_p = 1 \cdot 1 + 1 \cdot 1$. At that point $\tilde A$, $\tilde B$ and $E_1 = V(x)$ are three curves with distinct tangent directions, and one more blow-up gives simple normal crossings, with total transform $\tilde A + \tilde B + 2E_1 + 4E_2$ over $p$, $E_1^2 = -2$ and $E_2^2 = -1$. The conics meet in the same way at $[0 : 1 : 0]$, which accounts for the rest of $A \cdot B = 4$.

**Example P5.6.21 (the singularity $y^3 = x^4$).** Let $C$ be the projective closure of $y^3 = x^4$, with $p$ the origin. It has multiplicity $3$ at $p$, and in the chart $y = xt$ the strict transform is $C_1 = V(t^3 - x)$, which is smooth. So $\delta_p = 3$ by Corollary P5.6.16, as in Example P5.3.7, and the bound $\delta_p \geq m(m-1)/2$ of Proposition P5.3.4 is an equality. The embedded resolution takes four blow-ups. The curve $C_1$ meets $E_1 = V(x)$ only at the origin, with $(C_1 \cdot E_1) = 3$. Blowing up the origin, with $x = tw$, gives $C_2 = V(w - t^2)$, the strict transform $V(w)$ of $E_1$, and $E_2 = V(t)$. Now $C_2$ is tangent to $E_1$ and transverse to $E_2$ at the origin. Blowing up the origin again, with $w = tu$, gives $C_3 = V(u - t)$, $E_1 = V(u)$ and $E_3 = V(t)$, three lines through a point, and one more blow-up separates them. The total transform is
$$C_4 + 3E_1 + 4E_2 + 8E_3 + 12E_4, \qquad E_1^2 = -4, \ E_2^2 = -2, \ E_3^2 = -2, \ E_4^2 = -1 .$$
The curve $E_4$ meets $C_4$, $E_1$ and $E_3$, and $E_3$ also meets $E_2$. The checks $\pi^* C \cdot E_i = 0$ read $1 + 3 + 8 - 12 = 0$, $4 - 16 + 12 = 0$, $-8 + 8 = 0$ and $-12 + 12 = 0$.

**Example P5.6.22 (an infinitely near double point).** Let $\operatorname{char} k \neq 2$ and $C$ the projective closure of $y^2 = x^4 + x^5$. The polynomial is irreducible, since $x^4(1 + x)$ is not a square in $k[x]$, so $C$ is integral. At the origin $m = 2$ with the single tangent direction $Y^2 = 0$. In the chart $y = xt$ the strict transform is $t^2 = x^2 + x^3$, which has a node at the point $t = 0$ of $E$, with multiplicity $2$. One more blow-up makes it smooth. So $\delta_0 = 1 + 1 = 2$ by Corollary P5.6.16, and $\delta_0 > m(m - 1)/2 = 1$. Over $k[[x]]$ the equation factors as $(y - x^2 u)(y + x^2 u)$ with $u^2 = 1 + x$, so near the origin $C$ has two smooth branches meeting like the conics of Example P5.6.20.

### Proof

*Lemma P5.6.13.* The components of $\tilde G$ are the strict transforms of those of $G$ (Proposition P5.6.4), and they are smooth by part 5 of that proposition. If $q$ lies on no component, nothing changes near $E$, and $\tilde G \cap E = \emptyset$. Let $G_1, \dots, G_s$ be the components through $q$, so $s \leq 2$ and $m_q(G) = s$, since each $G_j$ has multiplicity $1$ at $q$. By part 3 of Proposition P5.6.4, $\tilde G_j \cdot E = 1$, so $\tilde G_j$ meets $E$ in one point, transversally, at the tangent direction of $G_j$. If $s = 2$, then $(G_1 \cdot G_2)_q = 1$, and Proposition P5.6.6 gives $(G_1 \cdot G_2)_q = 1 \cdot 1 + \sum_{q' \in E} (\tilde G_1 \cdot \tilde G_2)_{q'}$. So $\tilde G_1$ and $\tilde G_2$ do not meet over $q$, and they meet $E$ at distinct points. Away from $E$ the configuration is that of $G$. So no point lies on three components of $\tilde G + E$, and all intersections are transverse. Finally $\tilde G \cdot E = \sum_j \tilde G_j \cdot E = s$. $\square$

*Proposition P5.6.14.* By Proposition P3.11.12, $\tilde C$ is integral and $\tilde C \to C$ is birational, so $\tilde C$ and $C$ have the same function field and, by Theorem P5.1.3, the same normalization, of genus $g$. The genus formula of Proposition P5.3.2 gives $p_a(C) = g + \sum_{P \in C} \delta_P(C)$ and $p_a(\tilde C) = g + \sum_{Q \in \tilde C} \delta_Q(\tilde C)$. The $\delta$-invariant of a point depends only on its local ring, and $\pi$ identifies the local rings of $\tilde C$ off $E$ with those of $C$ off $p$. Subtracting and using part 4 of Proposition P5.6.4 gives $m(m-1)/2 = p_a(C) - p_a(\tilde C) = \delta_p(C) - \sum_{q \in \tilde C \cap E} \delta_q(\tilde C)$. $\square$

*Theorem P5.6.15.* A singular point has multiplicity $m \geq 2$ (Definition P5.6.1), so each blow-up lowers the arithmetic genus of the strict transform by $m(m-1)/2 \geq 1$, by part 4 of Proposition P5.6.4. By Proposition P5.6.14 all strict transforms have the normalization of $C$, and by Proposition P5.3.2 their arithmetic genus is at least its genus $g$. So there are at most $p_a(C) - g$ blow-ups, and the process ends at a strict transform $C_n$ with no singular point. Then $C_n$ is a smooth projective curve with function field $K(C)$, so by Theorem P5.1.3 it is the normalization $\tilde C^\nu$, and the composite $C_n \to C$ is the normalization map, by the universal property of the normalization (Theorem P3.7.36). $\square$

*Corollary P5.6.16.* Apply Proposition P5.6.14 at each centre over $p$. The $\delta$-invariant of a point is $0$ exactly at smooth points (Proposition P5.3.2), and the process of Theorem P5.6.15 blows up every singular point of every strict transform over $p$, ending at a curve with $\delta = 0$ everywhere. So by induction on the number of centres over $p$, $\delta_p(C)$ is the sum of the terms $m_j(m_j - 1)/2$. The last statement is the case in which $p$ is the only centre over $p$, that is, $\delta_q(\tilde C) = 0$ for every $q \in \tilde C \cap E$. $\square$

*Theorem P5.6.17.* All centres below lie over singular points of $C_{\mathrm{red}}$: in the first two steps they are singular points of strict transforms of components of $C$, or points where two of them meet, and in the third step they lie on exceptional curves. Every centre lies on the total transform of $C$, so every exceptional curve lies in the support of the total transform, which is the union of the strict transforms of the components of $C$ and of the exceptional curves.

*Step 1.* Apply Theorem P5.6.15 to each component of $C$. Blowing up a point does not make a smooth strict transform singular, by part 5 of Proposition P5.6.4. So after finitely many blow-ups the strict transforms $D_1, \dots, D_r$ of the components of $C$ are smooth.

*Step 2.* Let $\sigma = \sum_{i < j} D_i \cdot D_j \geq 0$. If two of the $D_i$ meet at $q$, blow up $q$. By Proposition P5.6.6 with multiplicities $1$, or by Theorem P5.6.3, $\tilde D_i \cdot \tilde D_j = D_i \cdot D_j - 1$ for each pair through $q$, and the other numbers do not change. So $\sigma$ drops, and after finitely many steps $D_1, \dots, D_r$ are smooth and pairwise disjoint. Blow-ups keep these two properties.

*Step 3.* Let $G$ be the sum of the exceptional curves. It has simple normal crossings: it is empty on $S$, and Lemma P5.6.13 applies at each blow-up, since $\tilde G + E$ is the sum of the new exceptional curves. For $q \in D_i \cap G$ put $e_q = (D_i \cdot G)_q \geq 1$. Since $D_i$ is smooth, $e_q = 1$ exactly when one component of $G$ passes through $q$ and meets $D_i$ transversally there. So the support of the total transform, $D_1 + \dots + D_r + G$, has simple normal crossings exactly when $e_q = 1$ for all such $q$. Let
$$\Phi = \sum_{q \in D \cap G, \ e_q \geq 2} \bigl(2 e_q - m_q(G)\bigr), \qquad D = D_1 + \dots + D_r ,$$
a sum of positive integers, since $m_q(G) \leq 2$. If $\Phi > 0$, blow up a point $q \in D_i \cap G$ with $e_q \geq 2$. The new exceptional sum is $G' = \tilde G + E$. The strict transform $\tilde D_i$ meets $E$ in exactly one point $q'$, transversally, and by Proposition P5.6.6 the intersection of $\tilde D_i$ and $\tilde G$ over $q$ is concentrated at $q'$ and equals $e_q - m_q(G)$. So
$$e_{q'} = (\tilde D_i \cdot \tilde G)_{q'} + (\tilde D_i \cdot E)_{q'} = e_q - m_q(G) + 1 .$$
If $m_q(G) = 2$, then $e_{q'} = e_q - 1$, and the term of $q'$, if there is one, is at most $2(e_q - 1) - 1 < 2e_q - 2$. If $m_q(G) = 1$, then $e_{q'} = e_q \geq 2$, so $\tilde D_i$ meets $\tilde G$ at $q'$, and $q' \in \tilde G \cap E$ has $m_{q'}(G') = 2$. The term of $q'$ is then $2e_q - 2 < 2e_q - 1$. Other points of $D \cap G$ are not affected. In both cases $\Phi$ drops, so after finitely many blow-ups $\Phi = 0$, and the support of the total transform has simple normal crossings. $\square$

*Corollary P5.6.18.* Let $\sigma$ be the sum of the local intersection multiplicities of the strict transforms of $C$ and $D$ at the points over $p$. At the start $\sigma = (C \cdot D)_p$. A centre $q$ is a common point, so both strict transforms have multiplicity at least $1$ there, and by Proposition P5.6.6 the blow-up of $q$ lowers $\sigma$ by $m_q(C_{i-1}) \, m_q(D_{i-1}) \geq 1$. Points over $p$ that are not blown up keep their local multiplicities. Since $\sigma \geq 0$, the process stops, and it stops when $\sigma = 0$, that is, when the strict transforms do not meet over $p$. Summing the drops gives the formula. $\square$

### Exercises

1. (A) Let $C$ be the projective closure of $y^3 = x^5$. Show that its strict transforms have multiplicities $3$ and $2$ at the two centres over the origin, and deduce $\delta_0 = 4$. Compare with the count of gaps of the semigroup $\langle 3, 5 \rangle$ in Example P5.3.7.
2. (A) Let $k \geq 1$ and $C$ the projective closure of $y^2 = x^{2k+1}$. Show that the resolution of Theorem P5.6.15 blows up $k$ points over the origin, each a double point of the strict transform, and that $\delta_0 = k$.
3. (B) A point $p$ of a curve $C$ is an *ordinary $m$-fold point* if $m_p(C) = m$ and the leading form has $m$ distinct linear factors. Show that one blow-up gives simple normal crossings over $p$, with $E$ of multiplicity $m$ in the total transform. For integral $C$ show that $\delta_p = m(m - 1)/2$.
4. (B) Use Noether's formula to compute $(C \cdot D)_0$ for the cusp $y^2 = x^3$ and the line $y = 0$, and for the curves $y = x^a$ and $y = x^b$ with $1 \leq a < b$. Check the answers against Proposition P5.5.5.
5. (B) Let $\pi \colon S' \to S$ be a sequence of blow-ups with exceptional curves $F_1, \dots, F_n$. Show that $\pi^* D \cdot F_j = 0$ for every divisor $D$ on $S$ and every $j$, and that the intersection matrix $(F_i \cdot F_j)$ is negative definite. (Hint: the total transforms of $E_1, \dots, E_n$ are orthogonal with square $-1$ and span the same lattice as the $F_j$.)
6. (C) Let $k \geq 1$ and $C$ be the projective closure of $y^2 = x^{2k+1}$. Show that the procedure in the proof of Theorem P5.6.17 uses $k + 2$ blow-ups over the origin, and that the self-intersections of the exceptional curves, in the order of the blow-ups, are $-2$ for the first $k - 1$, then $-3$, $-2$ and $-1$. For $k = 1$ this is Example P5.6.19.

### Lean

Mathlib does not formalize blow-ups of schemes, strict transforms or the intersection pairing on a surface, so none of the results of this section can be stated there yet. The $\delta$-invariant is the length of a quotient of modules, which Mathlib can express with `Module.length`, but the integral closure of the local ring of a curve point and the genus formula are not connected to it. The handbook adds no `MinimalModel` node here.

### Notes and history

Resolution of plane curve singularities by quadratic transformations is due to Max Noether, in the 1870s, and the formula $\delta_p = \sum m_q(m_q - 1)/2$ over infinitely near points is in Noether's work and in Enriques and Chisini's *Lezioni sulla teoria geometrica delle equazioni*. Noether's formula for intersection multiplicities is Hartshorne, Exercise V.3.4, and the embedded resolution is Hartshorne, Theorem V.3.9. The literature state is theorem. The proof of Step 3 above follows the standard count of tangency orders. Hironaka's theorem of 1964 extends embedded resolution to all varieties in characteristic $0$, and it is the source of the log resolutions on which the discrepancies and the singularities of pairs of Volume 4 are defined. The resolution of Example P5.6.19 is the minimal log resolution of the cusp, and the coefficients $2, 3, 6$ of its exceptional curves, together with the discrepancies $1, 2, 4$ of $K$, give the log canonical threshold $5/6$ of the cusp, computed in Volume 4.
