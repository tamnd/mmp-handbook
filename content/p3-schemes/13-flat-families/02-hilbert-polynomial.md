---
title: The Hilbert polynomial in flat families
nodes: []
sources: [Vak25, Har77, Stacks]
reads_with: [Vak25:ch24, Har77:III.9]
requires: [P1.1, P1.3, P1.4, P1.5, P1.7, P1.13, P3.6, P3.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Hilbert polynomial in flat families

### Statement

Let $k$ be a field, $S = k[x_0, \dots, x_n]$ with $n \geq 1$, and $X \subseteq \mathbb{P}^n_k$ a closed subscheme. By part 2 of Corollary P3.6.15, $X = \operatorname{Proj} S/I_X$ for a unique saturated homogeneous ideal $I_X = \Gamma_*(\mathcal{I}_X)$, the *ideal of $X$*.

**Definition P3.13.12 (Hilbert function and Hilbert polynomial).** The *Hilbert function* of $X$ is $h_X(m) = \dim_k (S/I_X)_m$. The *Hilbert polynomial* $P_X \in \mathbb{Q}[m]$ is the polynomial with $h_X(m) = P_X(m)$ for all large $m$, which exists by Theorem P1.5.30. The *arithmetic genus* of a curve $X$ is $p_a(X) = 1 - P_X(0)$.

Lean: Mathlib `Polynomial.hilbertPoly` (definition) is the polynomial attached to a rational power series $p(t)/(1 - t)^d$, the algebraic step from a Hilbert series to its polynomial. The Hilbert polynomial of a closed subscheme of projective space is not in Lean as stated.

**Lemma P3.13.13 (first properties).** Let $X \subseteq \mathbb{P}^n_k$ be a closed subscheme.

1. If $J$ is a homogeneous ideal with $\operatorname{Proj} S/J = X$, then $\dim_k (S/J)_m = P_X(m)$ for all large $m$.
2. Let $A \to A'$ be a ring homomorphism and $I \subseteq A[x_0, \dots, x_n]$ a homogeneous ideal. Then $\operatorname{Proj}(A[x]/I) \times_A A' = \operatorname{Proj}(A'[x]/IA'[x])$ as closed subschemes of $\mathbb{P}^n_{A'}$. In particular, for a field extension $k \subseteq k'$, $P_{X \times_k k'} = P_X$.
3. $P_X = 0$ if and only if $X = \emptyset$.
4. If $X_1, X_2 \subseteq \mathbb{P}^n_k$ are disjoint closed subschemes with ideals $I_1, I_2$, and $X_1 \cup X_2 = \operatorname{Proj} S/(I_1 \cap I_2)$, then $P_{X_1 \cup X_2} = P_{X_1} + P_{X_2}$.

Lean: not in Lean as stated.

For a ring $A$ and a closed subscheme $X \subseteq \mathbb{P}^n_A$, the fibre over a point $p$ of $\operatorname{Spec} A$ is the closed subscheme $X_p = X \times_A \kappa(p)$ of $\mathbb{P}^n_{\kappa(p)}$, and by part 2 it is $\operatorname{Proj}$ of $\kappa(p)[x]$ modulo the image of the ideal of $X$. For a morphism $X \to Y$ with $X \subseteq \mathbb{P}^n_Y$ closed, the fibre $X_y$ is a closed subscheme of $\mathbb{P}^n_{\kappa(y)}$ in the same way.

**Theorem P3.13.14 (flatness over a discrete valuation ring).** Let $R$ be a discrete valuation ring with uniformizer $t$, fraction field $K$ and residue field $\kappa$. Let $S = R[x_0, \dots, x_n]$, let $X \subseteq \mathbb{P}^n_R$ be a closed subscheme with saturated ideal $I = \Gamma_*(\mathcal{I}_X)$, and let $X_K$ and $X_\kappa$ be its fibres. Let $I' = \{s \in S : t^l s \in I \text{ for some } l\}$.

1. $IS_K$ is the ideal of $X_K$ in $S_K = K[x_0, \dots, x_n]$, and $I' = IS_K \cap S$. The ideal $I'$ is saturated, and $X' = \operatorname{Proj} S/I'$ is the only closed subscheme of $\mathbb{P}^n_R$ that is flat over $R$ with generic fibre $X_K$, the *flat closure* of $X_K$.
2. $X$ is flat over $R$ if and only if $t$ is a nonzerodivisor on $S/I$, if and only if $I = I'$. More generally, if $J$ is a homogeneous ideal and $t$ is a nonzerodivisor on $S/J$, then $\operatorname{Proj} S/J$ is flat over $R$.
3. Let $N = I'/I$, a finitely generated graded $S$-module, and let $Q$ be the Hilbert polynomial of the graded $\kappa[x_0, \dots, x_n]$-module $N/tN$. Then $P_{X_\kappa} = P_{X_K} + Q$. In particular $P_{X_\kappa}(m) \geq P_{X_K}(m)$ for all large $m$.
4. $X$ is flat over $R$ if and only if $P_{X_\kappa} = P_{X_K}$.

Lean: not in Lean as stated.

**Lemma P3.13.15 (specializations come from discrete valuation rings).** Let $Y$ be a scheme locally of finite type over a field $k$, and let $y, y' \in Y$ with $y \in \overline{\{y'\}}$ and $y \neq y'$. There are points $y' = y_0, y_1, \dots, y_r = y$ and, for each $i$, a discrete valuation ring $R_i$ and a morphism $\operatorname{Spec} R_i \to Y$ that maps the generic point to $y_{i - 1}$ and the closed point to $y_i$.

Lean: not in Lean as stated.

**Theorem P3.13.16 (constancy of the Hilbert polynomial).** Let $Y$ be a connected scheme locally of finite type over a field $k$, and let $X \subseteq \mathbb{P}^n_Y$ be a closed subscheme that is flat over $Y$. Then the Hilbert polynomial $P_{X_y}$ of the fibre $X_y \subseteq \mathbb{P}^n_{\kappa(y)}$ does not depend on $y \in Y$.

Lean: not in Lean as stated.

### Proof in words

The Hilbert polynomial only sees large degrees, so any ideal with the right saturation computes it, and base change of the field does not change dimensions of graded pieces. Over a discrete valuation ring a closed subscheme of projective space is flat exactly when its homogeneous coordinate ring has no $t$-torsion, and the $t$-torsion is the module $N = I'/I$. In each degree, the coordinate ring of the flat closure is a free $R$-module, whose rank is the Hilbert function of the generic fibre and whose reduction is the Hilbert function of the special fibre. The torsion adds the Hilbert polynomial of $N/tN$ to the special fibre and nothing to the generic fibre. So the special fibre can only grow, and it grows exactly when the family is not flat.

For a flat family over a connected base it is enough to compare a point with a point in its closure. A specialization in a scheme of finite type over a field is a chain of steps of codimension one. Each step comes from a discrete valuation ring, the local ring of the normalization at a prime of height one, and the pullback of the family to it is flat, with the same fibres up to an extension of the field. The Hilbert polynomial is then the same at the two ends of each step, so it is constant on irreducible components, and so on the connected base.

### Examples

**Example P3.13.17 (hypersurfaces).** Let $F \in S_d$ be nonzero and $X = V_+(F)$. Since $S$ is a domain, $0 \to S(-d) \xrightarrow{F} S \to S/(F) \to 0$ is exact, so by part 1 of Lemma P3.13.13
$$
P_X(m) = \binom{m + n}{n} - \binom{m + n - d}{n} =: P_d(m).
$$
The polynomial $P_d$ has degree $n - 1$ and leading coefficient $d/(n - 1)!$: the coefficient of $m^{n-1}$ in $\prod_{j=1}^n (m + j)$ is $\sum_j j$, and in $\prod_{j=1}^n (m + j - d)$ it is $\sum_j (j - d)$, and their difference is $nd$, which is divided by $n!$.

**Example P3.13.18 (plane curves and their genus).** For $n = 2$,
$$
P_d(m) = \binom{m + 2}{2} - \binom{m + 2 - d}{2} = dm - \frac{d(d - 3)}{2} = dm + 1 - g, \qquad g = \frac{(d - 1)(d - 2)}{2}.
$$
So a plane curve of degree $d$ has arithmetic genus $p_a = (d-1)(d-2)/2$: a line or a conic has $p_a = 0$, a cubic has $p_a = 1$, a quartic has $p_a = 3$. The arithmetic genus is the same for a smooth cubic, a nodal cubic and three concurrent lines, since all are hypersurfaces of degree $3$. By Theorem P3.13.16 the genus of a smooth plane curve does not change in a flat family, whatever the singularities of the limit.

**Example P3.13.19 (linear subspaces).** For a linear subspace $L = V_+(x_{r+1}, \dots, x_n) \cong \mathbb{P}^r_k$, $S/I_L = k[x_0, \dots, x_r]$ and $P_L(m) = \binom{m + r}{r}$. A point has $P = 1$, a line $m + 1$, a plane $\binom{m + 2}{2}$.

**Example P3.13.20 (the skew lines again).** Two skew lines $L_1, L_2$ in $\mathbb{P}^3_k$ have $P_{L_1 \cup L_2} = 2(m + 1) = 2m + 2$ by part 4 of Lemma P3.13.13. Two lines that meet span a plane, and their union is a conic in that plane, the complete intersection $V_+(xy, z)$, with Hilbert polynomial $2m + 1$ by Example P3.13.18 and part 1 of Lemma P3.13.13 applied to $k[x, y, w]/(xy)$. In the family of Example P3.13.11 the generic fibre is two skew lines. By part 4 of Theorem P3.13.14, the flat limit has Hilbert polynomial $2m + 2$, so it is not the union of the two limit lines. The count in Example P3.13.11 confirms this: the basis of $S/I_0$ has $(m + 1) + m + 1 = 2m + 2$ monomials in degree $m \geq 1$, one more than the crossing lines, and the extra monomial $w^{m-1}z$ is the embedded point. Theorem P3.13.14 also tells us that the family whose fibre over $t$ is $L_1 \cup L_2$ for $t \neq 0$ and the crossing lines for $t = 0$ is not flat.

**Example P3.13.21 (conics that degenerate).** Over $R = k[t]_{(t)}$ let $F \in S_d$ with $t \nmid F$, that is, $F$ has a coefficient that is a unit. Then $t$ is a nonzerodivisor on $S/(F)$: if $tg = Fh$, then reducing modulo $t$ gives $\bar F \bar h = 0$ in the domain $\kappa[x]$ with $\bar F \neq 0$, so $h = th'$ and $g = Fh'$. By part 2 of Theorem P3.13.14, $V_+(F)$ is flat over $R$, with Hilbert polynomial $P_d$ on both fibres. For $d = 2$, $n = 2$: the family $xy - tz^2$ has a smooth conic as generic fibre and the two lines $xy = 0$ as special fibre; the family $x^2 - tyz$ has a smooth conic as generic fibre and the double line $x^2 = 0$ as special fibre. All have Hilbert polynomial $2m + 1$. The double line is not reduced, and it is still a conic, the flat limit of smooth conics.

**Example P3.13.22 (a family that jumps).** Over $R = k[t]_{(t)}$ let $X = V_+(tx_1) \subseteq \mathbb{P}^n_R$. The ideal $I = (tx_1)$ is saturated: if $x_0^l s \in (tx_1)$ then $t x_1$ divides $s$ in the factorial ring $S$. The generic fibre is the hyperplane $x_1 = 0$, with $P_{X_K} = \binom{m + n - 1}{n - 1}$, and the special fibre is all of $\mathbb{P}^n_\kappa$, with $P_{X_\kappa} = \binom{m + n}{n}$. Here $I' = (x_1)$ and $N = (x_1)/(tx_1) \cong (S/tS)(-1)$ by $x_1 s \mapsto s$, so $N/tN = N$ has Hilbert polynomial $\binom{m - 1 + n}{n}$. Part 3 of Theorem P3.13.14 is Pascal's rule $\binom{m + n}{n} = \binom{m + n - 1}{n - 1} + \binom{m + n - 1}{n}$.

### Proof

*Proof of Lemma P3.13.13.* Part 1. By part 2 of Corollary P3.6.15, $J$ and $I_X$ have the same saturation, so $J \subseteq J^{\mathrm{sat}} = I_X$. Let $a_1, \dots, a_r$ be homogeneous generators of $I_X$, which exist as $S$ is Noetherian (Theorem P1.3.10). There is $l$ with $x_i^l a_j \in J$ for all $i, j$. Every monomial of degree $(n + 1)(l - 1) + 1$ is divisible by some $x_i^l$, so $S_e a_j \subseteq J$ for $e \geq (n + 1)(l - 1) + 1$. Hence $(I_X/J)_m = 0$ for $m \geq (n + 1)(l - 1) + 1 + \max_j \deg a_j$, and $\dim_k (S/J)_m = h_X(m)$ for such $m$.

Part 2. Put $T = A[x]/I$ and $T' = T \otimes_A A' = A'[x]/IA'[x]$. For each $i$, $T_{(x_i)} \otimes_A A' = T'_{(x_i)}$: an element of $T_{(x_i)}$ is $a/x_i^m$ with $a \in T_m$, and $A'$ sits in degree $0$, so both sides are the degree $0$ part of $T_{x_i} \otimes_A A' = T'_{x_i}$. The charts $D_+(x_i)$ cover both Proj's (part 1 of Proposition P3.6.4), and these isomorphisms are compatible with the gluing maps, which are localizations. So $\operatorname{Proj} T \times_A A'$, glued from $\operatorname{Spec}(T_{(x_i)} \otimes_A A')$ by Theorem P3.3.19, is $\operatorname{Proj} T'$, compatibly with the closed immersions into $\mathbb{P}^n_{A'}$. For $k \subseteq k'$, $X \times_k k' = \operatorname{Proj} S'/I_X S'$ with $S' = k'[x]$, and $(S'/I_X S')_m = (S/I_X)_m \otimes_k k'$ has the same dimension. Part 1 over $k'$ gives $P_{X \times_k k'} = P_X$.

Part 3. If $X = \emptyset$, its ideal sheaf is $\mathcal{O}_{\mathbb{P}^n}$, and $I_X = \Gamma_*(\mathcal{O}) = S$ by Theorem P3.6.12, so $P_X = 0$. If $P_X = 0$, then $(S/I_X)_m = 0$ for $m \geq m_0$, so $x_i^{m_0} \in I_X$ for every $i$ and $S_+ \subseteq \sqrt{I_X}$. Part 4 of Proposition P3.6.2 gives $X = V_+(I_X) = \emptyset$.

Part 4. The sequence $0 \to S/(I_1 \cap I_2) \to S/I_1 \oplus S/I_2 \to S/(I_1 + I_2) \to 0$, with maps $a \mapsto (a, a)$ and $(a, b) \mapsto a - b$, is exact. Since $V_+(I_1 + I_2) = X_1 \cap X_2 = \emptyset$, part 4 of Proposition P3.6.2 gives $S_+ \subseteq \sqrt{I_1 + I_2}$, so $(S/(I_1 + I_2))_m = 0$ for large $m$, as in part 3. So $\dim (S/(I_1 \cap I_2))_m = h_{X_1}(m) + h_{X_2}(m)$ for large $m$, and part 1 gives the claim. $\square$

*Proof of Theorem P3.13.14.* Write $M = S/I$. The scheme $X$ is covered by the affine opens $D_+(x_i) \cap X = \operatorname{Spec} M_{(x_i)}$, and $X$ is Noetherian.

Part 2. By Theorem P3.13.4 and part 2 of Proposition P3.13.2, $X$ is flat over $R$ if and only if every $M_{(x_i)}$ is torsion free over $R$, that is, $t$ is a nonzerodivisor on it, since every nonzero element of $R$ is a unit times a power of $t$. Let $J$ be any homogeneous ideal with $t$ a nonzerodivisor on $S/J$. If $t \cdot (a/x_i^m) = 0$ in $(S/J)_{(x_i)}$, then $x_i^l t a = 0$ in $S/J$ for some $l$, so $x_i^l a = 0$ and $a / x_i^m = 0$. This proves the last sentence of part 2, and with $J = I$ the implication from "$t$ is a nonzerodivisor on $S/I$" to "$X$ is flat". Conversely let $X$ be flat, and let $a \in M$ be homogeneous of degree $d$ with $ta = 0$. For each $i$, $t \cdot a/x_i^d = 0$ in $M_{(x_i)}$, so $a/x_i^d = 0$ and $x_i^l a = 0$ in $M$ for some $l$, that is, $x_i^l a \in I$ for all $i$ after enlarging $l$. As $I$ is saturated, $a \in I$, that is, $a = 0$ in $M$. Since $t$ has degree $0$, an element $a$ with $ta = 0$ has all its homogeneous components killed by $t$, so $t$ is a nonzerodivisor on $M$. Finally $t$ is a nonzerodivisor on $S/I$ if and only if $t^l s \in I$ implies $s \in I$, that is, $I' = I$.

Part 1. By part 2 of Lemma P3.13.13, $X_K = \operatorname{Proj} S_K/IS_K$. The ring $S$ is a domain, so $S \subseteq S_K = S_t$, and $s \in S$ lies in $IS_K$ if and only if $t^l s \in I$ for some $l$. So $I' = IS_K \cap S$. The ideal $IS_K$ is saturated: if $s \in S_K$ and $x_i^l s \in IS_K$ for all $i$, write $s = s_0/t^e$ with $s_0 \in S$; then $x_i^l s_0 \in I'$, so $t^{l'} x_i^l s_0 \in I$ for all $i$ and some $l'$, so $t^{l'} s_0 \in I$ by saturation of $I$, so $s_0 \in I'$ and $s \in IS_K$. So $IS_K$ is the ideal of $X_K$. The ideal $I'$ is saturated by the same argument, and $t$ is a nonzerodivisor on $S/I'$, since $ts \in I'$ gives $t^{l + 1} s \in I$. By part 2, $X'$ is flat. Since $I \subseteq I' \subseteq IS_K$, $I'S_K = IS_K$, so $X'_K = X_K$. If $X''$ is another closed subscheme, flat over $R$ with $X''_K = X_K$, with saturated ideal $I''$, then by the argument above $I''S_K$ is the ideal of $X''_K = X_K$, so $I''S_K = IS_K$, and $I'' = I''S_K \cap S$ by part 2. So $I'' = I'$ and $X'' = X'$.

Part 3. Write $M' = S/I'$. The module $N = I'/I$ is the submodule of $M$ of elements killed by a power of $t$, and $0 \to N \to M \to M' \to 0$ is exact. Fix $m$. The $R$-modules $M_m$, $M'_m$ and $N_m$ are finitely generated, since $S_m$ is free of finite rank. $M'_m$ is torsion free, so it is flat (Proposition P1.1.47) and free (Theorem P1.1.50), of rank $r_m = \dim_K M'_m \otimes_R K$. As $N_m \otimes_R K = 0$ and localization is exact, $r_m = \dim_K M_m \otimes_R K = \dim_K (S_K/IS_K)_m$. By Lemma P1.1.48 the sequence
$$
0 \to N_m/tN_m \to M_m/tM_m \to M'_m/tM'_m \to 0
$$
is exact, and $\dim_\kappa M'_m/tM'_m = r_m$. Now $M_m / tM_m = (\kappa[x]/I\kappa[x])_m$, and $X_\kappa = \operatorname{Proj} \kappa[x]/I\kappa[x]$ by part 2 of Lemma P3.13.13. Part 1 of Lemma P3.13.13 over $K$ and over $\kappa$ gives, for large $m$,
$$
P_{X_\kappa}(m) = \dim_\kappa M_m/tM_m = r_m + \dim_\kappa (N/tN)_m = P_{X_K}(m) + Q(m).
$$
The module $N/tN$ is finitely generated over $\kappa[x] = S/tS$, as $I'$ is finitely generated, so $Q$ exists by Theorem P1.5.30. Its values at large $m$ are dimensions, hence nonnegative.

Part 4. If $X$ is flat, $N = 0$ by part 2 and $Q = 0$. Conversely let $Q = 0$. Then $(N/tN)_m = 0$ for $m \geq m_0$, so $N_m = tN_m$, and $N_m = 0$ by Nakayama's lemma (Theorem P1.1.25) over the local ring $R$. Let $s \in I'$ be homogeneous. Then $x_i^{m_0} s \in I'$ has degree at least $m_0$, so $x_i^{m_0} s \in I$ for every $i$, and $s \in I$ by saturation. So $I' = I$ and $X$ is flat by part 2. $\square$

*Proof of Lemma P3.13.15.* Every open set that contains $y$ contains $y'$. Let $\operatorname{Spec} A$ be an affine open containing $y$, with $A$ a finitely generated $k$-algebra, and let $\mathfrak{p}' \subsetneq \mathfrak{p}$ be the primes of $y'$ and $y$. The chains of primes between $\mathfrak{p}'$ and $\mathfrak{p}$ have length at most $\dim A$, which is finite (Theorem P3.7.4), so there is a chain $\mathfrak{p}' = \mathfrak{q}_0 \subsetneq \mathfrak{q}_1 \subsetneq \dots \subsetneq \mathfrak{q}_r = \mathfrak{p}$ that cannot be refined. Let $y_i$ be the point $\mathfrak{q}_i$. It suffices to construct $R_i$ for one step, so let $D = A/\mathfrak{q}_{i-1}$, a finitely generated $k$-algebra that is a domain, and $\mathfrak{q} = \mathfrak{q}_i/\mathfrak{q}_{i-1}$, a nonzero prime with no prime strictly between $0$ and $\mathfrak{q}$, so of height $1$.

Let $D'$ be the integral closure of $D$ in its fraction field. By Theorem P1.4.32 it is a finite $D$-module, so it is a Noetherian normal domain. By lying over (Theorem P1.4.12) there is a prime $\mathfrak{Q}$ of $D'$ with $\mathfrak{Q} \cap D = \mathfrak{q}$, and $\mathfrak{Q} \neq 0$. If $0 \subsetneq \mathfrak{Q}_1 \subsetneq \mathfrak{Q}$, then by incomparability (Theorem P1.4.11) $0 \subsetneq \mathfrak{Q}_1 \cap D \subsetneq \mathfrak{q}$, as the contractions of $0 \subsetneq \mathfrak{Q}_1$ and of $\mathfrak{Q}_1 \subsetneq \mathfrak{Q}$ must be different. This contradicts $\operatorname{ht} \mathfrak{q} = 1$. So $\operatorname{ht} \mathfrak{Q} = 1$, and $R_i = D'_\mathfrak{Q}$ is a discrete valuation ring by Corollary P1.7.13. The composite $A \to D \to D' \to R_i$ sends the zero ideal of $R_i$ to $\mathfrak{q}_{i-1}$ and its maximal ideal to the inverse image of $\mathfrak{q}$, which is $\mathfrak{q}_i$. So $\operatorname{Spec} R_i \to \operatorname{Spec} A \subseteq Y$ is the required morphism. $\square$

*Proof of Theorem P3.13.16.* Write $P_y = P_{X_y}$. First let $y \in \overline{\{y'\}}$. Take the chain and the discrete valuation rings of Lemma P3.13.15, and fix one step $g \colon \operatorname{Spec} R \to Y$, with generic point $\xi \mapsto y_{i-1}$ and closed point $c \mapsto y_i$. The base change $X_R = X \times_Y \operatorname{Spec} R$ is a closed subscheme of $\mathbb{P}^n_R$, flat over $R$ by part 3 of Proposition P3.13.3. Its fibres are $(X_R)_\xi = X_{y_{i-1}} \times_{\kappa(y_{i-1})} K$ and $(X_R)_c = X_{y_i} \times_{\kappa(y_i)} \kappa$, by associativity of fibre products. By part 4 of Theorem P3.13.14 and part 2 of Lemma P3.13.13, $P_{y_{i-1}} = P_{y_i}$. So $P_{y'} = P_y$.

For a polynomial $P$ let $Y_P = \{y : P_y = P\}$. Each $Y_P$ is open. Let $y \in Y_P$, and let $U$ be an affine open containing $y$. It is Noetherian, so it has finitely many irreducible components $Z_1, \dots, Z_s$. Let $V$ be $U$ minus the union of the $Z_j$ that do not contain $y$, an open set containing $y$. A point $z \in V$ lies in some $Z_j$ with $y \in Z_j$, and the generic point $\zeta$ of $Z_j$ has $z, y \in \overline{\{\zeta\}}$. By the first step $P_z = P_\zeta = P_y$. So $V \subseteq Y_P$. The sets $Y_P$ are disjoint and open and cover $Y$, and $Y$ is connected, so only one of them is nonempty. $\square$

### Exercises

1. (A) Let $C \subseteq \mathbb{P}^3_k$ be the twisted cubic, $\operatorname{Proj}$ of $S/I$ with $I$ the kernel of $k[x_0, \dots, x_3] \to k[s, u]$, $x_i \mapsto s^{3 - i}u^i$. Show that $I$ is saturated and, with Example P1.13.20, that $P_C = 3m + 1$, so $p_a(C) = 0$.
2. (A) Let $F, G \in k[x_0, \dots, x_3]$ be quadrics with no common factor and $X = V_+(F, G)$. Show that $F, G$ is a regular sequence, and use Corollary P1.13.14 to prove $P_X = 4m$. So $X$ is a curve of degree $4$ and arithmetic genus $1$.
3. (A) Over $R = k[t]_{(t)}$ let $I = (tx_1, x_1^2) \subseteq R[x_0, \dots, x_n]$. Show that $I = (x_1) \cap (t, x_1^2)$ and that $I$ is saturated. Find the fibres, compute $I'$ and $N = I'/I$, and check part 3 of Theorem P3.13.14.
4. (B) Let $Y$ be connected and locally of finite type over $k$, and $X \subseteq \mathbb{P}^n_Y$ closed and flat over $Y$. Show that if one fibre of $X$ is empty, then $X = \emptyset$. Show by an example that flatness is needed.
5. (B) Let $\operatorname{char} k \neq 2$. Over $R = k[t]$, find the flat limit in $\mathbb{A}^2$ of the three collinear points $(0, 0)$, $(t, 0)$, $(2t, 0)$, and show that it is $V(y, x^3)$. Compare with Exercise 4 of Section 13.1: both limits have length $3$, but one lies on a smooth curve and the other does not.
6. (C) Let $X \subseteq \mathbb{P}^3_{k[a]}$ be the flat closure of the projective closure of the twisted cubics of Exercise 6 of Section 13.1, with coordinates $x, y, z, w$. Using Theorem P3.13.16, show that its special fibre has Hilbert polynomial $3m + 1$. Show that the ideal $I_0 = (xz, yz, z^2, y^2 w - x^2(x + w))$ has $\dim (S/I_0)_m = 3m + 1$ for $m \geq 1$, and that $\operatorname{Proj} S/I_0$ is a plane nodal cubic, with Hilbert polynomial $3m$, together with an embedded point at $[0 : 0 : 0 : 1]$.

### Lean

Mathlib has the polynomial `Polynomial.hilbertPoly` attached to a rational power series, but not the Hilbert polynomial of a closed subscheme of projective space, nor flatness of a projective family. None of the statements of this section is in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Hilbert proved in 1890 that the Hilbert function of a graded module is eventually a polynomial. The constancy in flat families is Hartshorne, Theorem III.9.9, proved there with cohomology: $P_{X_y}(m) = \chi(\mathcal{O}_{X_y}(m))$, and the Euler characteristic is locally constant in a flat family. The proof here over a discrete valuation ring uses only graded algebra, and the passage to a connected base uses the normalization, which is why it is stated over a base of finite type over a field. For an arbitrary locally Noetherian base, the same proof works with the Krull and Akizuki theorem in place of Theorem P1.4.32. Hartshorne also proves the converse over a reduced base: if $Y$ is integral and the Hilbert polynomials of the fibres are constant, then $X$ is flat. Part 4 of Theorem P3.13.14 is this converse over a discrete valuation ring. The literature state is theorem.

The Hilbert polynomial is the discrete invariant that cuts the Hilbert scheme into pieces of finite type, $\operatorname{Hilb}^P$ for each $P$ (Section 13.4). In bend and break (Volume 2) the curves have bounded degree, and the Hilbert polynomials of their graphs lie in a finite set, so finitely many pieces of the Hilbert scheme suffice.
