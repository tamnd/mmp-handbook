---
title: Adjunction
nodes: []
sources: [KM98, Kol13, Kol92, Sho92]
reads_with: [KM98:ch5, Kol13:ch4]
requires: [4.1, 4.2, 4.3, 2.3, P5.5, P5.6, P5.7, P5.8]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Adjunction

### Statement

Adjunction passes singularities of a pair down to a divisor. If $(X, S + B)$ is lc near $S$, then the pair $(S^\nu, \operatorname{Diff}_{S^\nu}(B))$ is lc, and if $(X, S + B)$ is plt near $S$, then $S$ is normal and $(S, \operatorname{Diff}_S(B))$ is klt. This is the easy direction. Section 4 proves the converse on surfaces.

For a pair $(C, \Delta)$ on a smooth curve, the only divisors over $C$ are the points of $C$, and $a(P, C, \Delta) = -\operatorname{mult}_P \Delta$. So $(C, \Delta)$ is klt if and only if every coefficient of $\Delta$ is less than 1, and lc if and only if every coefficient is at most 1. This is how Definition 4.2.1 reads in dimension 1, where there are no exceptional divisors.

Throughout, $X$ is a normal variety of dimension $n \ge 2$ over a field of characteristic 0, $S$ is a prime divisor, $B \ge 0$ is an $\mathbb{R}$-divisor with no component equal to $S$, and $K_X + S + B$ is $\mathbb{R}$-Cartier. In dimension 2 the different is the one of Definition 4.5.1, and by Proposition 4.5.6 it is the same as the one of Definition 4.5.5.

**Theorem 4.5.17 (adjunction).** In this setting:

1. If $(X, S + B)$ is lc near $S$, then $(S^\nu, \operatorname{Diff}_{S^\nu}(B))$ is lc.
2. If $(X, S + B)$ is plt near $S$, then $(S^\nu, \operatorname{Diff}_{S^\nu}(B))$ is klt.

Lean: not yet in Lean.

The pair $(S^\nu, \operatorname{Diff}_{S^\nu}(B))$ is a pair in the sense of Volume 4: $\operatorname{Diff}_{S^\nu}(B) \ge 0$ (Proposition 4.5.4 on surfaces, Kol13, Chapter 4, in general), and $K_{S^\nu} + \operatorname{Diff}_{S^\nu}(B)$ is $\mathbb{R}$-Cartier by the adjunction formula of Proposition 4.5.6.

**Theorem 4.5.18 (plt centres are normal).** If $(X, S + B)$ is plt near $S$, then $S$ is normal. So in part 2 of Theorem 4.5.17, $S^\nu = S$ and $(S, \operatorname{Diff}_S(B))$ is klt.

Lean: not yet in Lean.

*Status.* Theorem 4.5.18 is a black box in this chapter: it is KM98, Proposition 5.51, whose proof uses the Kawamata-Viehweg vanishing theorem in the relative form proved in Volume 5. For surfaces it is part 2 of Theorem 4.5.25 in Section 4, with a complete proof from the vanishing theorem for a birational morphism of surfaces.

**Corollary 4.5.19 (adjunction on surfaces).** Let $X$ be a normal surface, $S$ an integral curve and $B \ge 0$ an $\mathbb{R}$-divisor with no component equal to $S$ (with no $\mathbb{R}$-Cartier hypothesis).

1. If $(X, S + B)$ is lc near $S$, every coefficient of $\operatorname{Diff}_{S^\nu}(B)$ is at most 1.
2. If $(X, S + B)$ is plt near $S$, then $S$ is a smooth curve and every coefficient of $\operatorname{Diff}_S(B)$ is less than 1.

Lean: not yet in Lean.

On a surface, lc and plt are read on Mumford's numerical pullback, as in Chapter 3; the proof below uses only the resolution. Normality of a curve is smoothness, so the second part says that a plt centre on a surface is a smooth curve.

### Proof in words

Take a log resolution. The different is the restriction of $\Delta_Y - S'$ to $S'$, and the restriction is again an snc divisor, now on the smooth variety $S'$, with the same coefficients as the components of $\Delta_Y$ that meet $S'$. The adjunction formula says that this restriction is the crepant pullback of the different, so the discrepancies of $(S^\nu, \operatorname{Diff})$ are the discrepancies of an snc sub-pair, which Corollary 4.2.13 reads off from coefficients. If $(X, S + B)$ is lc, every coefficient of $\Delta_Y$ is at most 1. If it is plt, the components meeting $S'$ have coefficient less than 1: exceptional ones by definition, and non-exceptional ones because two coefficient-1 components meeting would produce a divisor of discrepancy $-1$ over the intersection.

### Examples

**Example 4.5.20 (the quadric cone).** In Example 4.5.8, $(X, S)$ for $X$ the quadric cone and $S$ a line through the vertex has $\Delta_Y = S' + \frac12 E$ on the minimal resolution, which is a log resolution. So $(X, S)$ is plt: the only exceptional coefficient is $\frac12 < 1$, and $S'$ is the only coefficient-1 component. It is not klt, since $S$ has coefficient 1 (Problem 4 of Chapter 2). The different $\frac12 P$ has coefficient less than 1, so $(S, \operatorname{Diff}_S(0))$ is klt, as Theorem 4.5.17 predicts, and $S \cong \mathbb{A}^1$ is normal, as Theorem 4.5.18 predicts. A plt pair restricts to a klt pair, even though the pair itself is not klt.

**Counterexample 4.5.21 (dlt and not plt).** Let $X = \mathbb{A}^2$, $S = \{y = 0\}$ and $B = \{x = 0\}$. The pair $(X, S + B)$ is snc, so it is dlt. It is not plt: the blow-up of the origin has exceptional curve $E$ with $a(E, X, S + B) = 1 - 1 - 1 = -1$. The different is $\operatorname{Diff}_S(B) = P$, the origin, with coefficient 1, so $(S, \operatorname{Diff}_S(B))$ is lc and not klt. Part 1 of Theorem 4.5.17 applies, part 2 does not, and its conclusion fails. The same happens in dimension 3 for the three coordinate planes in $\mathbb{A}^3$: with $S = \{z = 0\}$ and $B = \{x = 0\} + \{y = 0\}$, the different is the union of the two coordinate axes of $S \cong \mathbb{A}^2$, and $(S, \operatorname{Diff}_S(B))$ is snc, dlt and lc, but not klt. The converse configuration, a pair that is plt and not dlt, does not exist: plt implies dlt by part 3 of Theorem 4.2.3. For a dlt pair the different is dlt and $S$ is normal (Kol13, Chapter 4; KM98, Corollary 5.52).

**Example 4.5.22 (the different does not see $B$ away from $S$).** Let $X = \mathbb{A}^2$, $S = \{y = 0\}$ and $B = 2L$, with $L = \{y = 1\}$. Then $L \cap S = \emptyset$, so $\operatorname{Diff}_S(B) = 0$ and $(S, 0)$ is klt. But $(X, S + 2L)$ is not lc, since $L$ has coefficient 2. Adjunction and inversion of adjunction are statements about a neighbourhood of $S$, and only a neighbourhood: $(X, S + 2L)$ is plt near $S$.

**Counterexample 4.5.23 (the node: failure without normality).** Let $X = \mathbb{A}^2$ and $S$ the nodal cubic of Example 4.5.9. One blow-up gives $\Delta_Y = S' + E$ with snc support, so $(X, S)$ is lc and not plt, and not dlt, since $E$ has discrepancy $-1$ and centre the non-snc point $P$ (Example 4.2.17). The different lives on $S^\nu$, where it is $q_1 + q_2$, and $(S^\nu, q_1 + q_2)$ is lc, as part 1 of Theorem 4.5.17 predicts. There is no version of the different on $S$ itself. The dualizing sheaf of $S$ is $\omega_S = \mathcal{O}_X(K_X + S)|_S$ (Theorem P5.5.14), so the naive formula $(K_X + S)|_S = K_S$ holds for line bundles, but $S$ is not normal and has no Weil divisors in the sense needed for a pair. Pulling back to the normalization gives $\nu^*\omega_S = \omega_{S^\nu}(q_1 + q_2)$, and the conductor $q_1 + q_2$ is the different. Normality is exactly what the plt hypothesis adds: Theorem 4.5.18 fails for lc pairs, and this is the basic example.

**Example 4.5.24 (coefficients above 1).** Two examples where the pair is not lc and the different detects it.

1. *The cusp.* For $S = \{y^2 = x^3\} \subset \mathbb{A}^2$, Example 4.5.10 gives $\operatorname{Diff}_{S^\nu}(0) = 2q$, with coefficient $2 > 1$. By part 1 of Theorem 4.5.17, $(\mathbb{A}^2, S)$ is not lc. This agrees with Example 4.2.16, where the lc threshold of the cusp is $\frac56 < 1$.
2. *The elliptic cone.* Let $X$ be the cone over a smooth plane cubic (Example 4.2.22), with minimal resolution $f$, exceptional elliptic curve $E$ with $E^2 = -3$, and $K_Y = f^*K_X - E$. Let $S$ be the ruling over a point of the cubic. Then $S'$ is a fibre of the line bundle $Y \to E$, so it meets $E$ once, transversally. Adjunction on $Y$ gives $K_Y \cdot E = -E^2 + 2g(E) - 2 = 3$. Writing $\Delta_Y = S' + cE$, the condition $(K_Y + S' + cE) \cdot E = 3 + 1 - 3c = 0$ gives $c = \frac43$. So $\operatorname{Diff}_S(0) = \frac43 P$, and $(X, S)$ is not lc, although $X$ is lc. The singularity of $X$ uses up the whole allowance of discrepancy $-1$, and adding any curve through the vertex destroys log canonicity.

### Proof

*Proof of Theorem 4.5.17.* The statements are local near $S$, so assume that $(X, S + B)$ is lc, or plt, on all of $X$. Let $f \colon Y \to X$ be a log resolution of $(X, S + B)$ (Theorem 4.2.10), $\Delta_Y = S' + \sum_D d_D D$ the crepant pullback, $g \colon S' \to S^\nu$ the induced morphism, and $\Delta_{S'} = (\Delta_Y - S')|_{S'}$. By part 2 of Proposition 4.5.6, $(S', \Delta_{S'})$ is the crepant pullback of $(S^\nu, \operatorname{Diff}_{S^\nu}(B))$ by $g$. By Proposition 4.1.14, $a(F, S^\nu, \operatorname{Diff}_{S^\nu}(B)) = a(F, S', \Delta_{S'})$ for every divisor $F$ over $S^\nu$, and the divisors over $S^\nu$ are the divisors over $S'$, since $g$ is birational. So it suffices to show that the sub-pair $(S', \Delta_{S'})$ is sub-lc, or sub-klt.

The support of $\Delta_Y$ is snc and contains $S'$. So each $D \cap S'$ is a smooth divisor on $S'$, possibly empty or disconnected, the divisors $D \cap S'$ for different $D$ have no common component, and their union has snc support on $S'$. Since $D$ and $S'$ meet transversally, $D|_{S'}$ is the reduced divisor $D \cap S'$. So

$$\Delta_{S'} = \sum_D d_D \, (D \cap S'),$$

an snc sub-boundary on $S'$ whose coefficients are the $d_D$ with $D \cap S' \ne \emptyset$.

(1) If $(X, S + B)$ is lc, then every $d_D \le 1$ by part 1 of Theorem 4.2.14. By part 1 of Corollary 4.2.13 (or, if $\dim S' = 1$, by the description of pairs on curves above), $(S', \Delta_{S'})$ is sub-lc.

(2) Suppose that $(X, S + B)$ is plt, and let $D$ meet $S'$. If $D$ is exceptional, then $d_D = -a(D, X, S + B) < 1$, by the definition of plt. If $D$ is not exceptional, it is the strict transform of a component of $B$, and $d_D \le 1$ by part 1 of Theorem 4.2.3. Suppose that $d_D = 1$. Then $S'$ and $D$ are two components of coefficient 1 of $\Delta_Y$ that meet. Let $W$ be a component of $S' \cap D$, of codimension 2 in $Y$, and $h$ the blow-up of $Y$ along $W$, near a general point of $W$, where $W$ is smooth. Its exceptional divisor $G$ has $a(G, Y, \Delta_Y) = 1 - 1 - 1 = -1$ by Lemma 4.1.20. So $a(G, X, S + B) = -1$ by Proposition 4.1.14, and $G$ is exceptional over $X$, which contradicts plt. So $d_D < 1$ for every $D$ meeting $S'$, and by part 1 of Corollary 4.2.13 $(S', \Delta_{S'})$ is sub-klt. $\square$

*Proof of Corollary 4.5.19.* On a surface the different is defined without an $\mathbb{R}$-Cartier hypothesis, and lc and plt are defined through the numerical pullback. Let $f$ be a log resolution of $(X, S + B)$; it is adapted to $S$, so the different is $(\Delta_Y - S')|_{S'}$, with coefficient $\sum_D d_D (D \cdot S')_q = d_D$ at a point $q \in D \cap S'$, since $D$ meets $S'$ transversally and at most one $D$ passes through $q$. The argument of the proof of Theorem 4.5.17 shows that $d_D \le 1$ in the lc case and $d_D < 1$ in the plt case, for every $D$ meeting $S'$. In the plt case $S$ is normal by part 2 of Theorem 4.5.25, and a normal curve is smooth. $\square$

*On Theorem 4.5.18.* The proof in KM98 is the higher-dimensional version of the proof of Theorem 4.5.25: on a log resolution, the relative Kawamata-Viehweg vanishing theorem makes $\mathcal{O}_X \to f_* \mathcal{O}_{S'}$ surjective, and $f_* \mathcal{O}_{S'}$ is the structure sheaf of the normalization. So $\mathcal{O}_S \to \nu_* \mathcal{O}_{S^\nu}$ is surjective and $S$ is normal.

### Exercises

1. (A) Let $X = \mathbb{A}^2$, $S = \{y = 0\}$ and $B = b\{y = x^2\}$ with $0 \le b \le 1$. Compute the different and decide, by Theorem 4.5.17, for which $b$ the conclusion of the theorem rules out lc. Compare with a log resolution of $(X, S + B)$.
2. (A) Let $X$ be the quadric cone and $S$ a line through the vertex. For which $b \ge 0$ is $(S, \operatorname{Diff}_S(bS_2))$ klt, where $S_2$ is a second line through the vertex? Use Example 4.5.16 with $n = 2$.
3. (B) Let $X = \mathbb{A}^3$, $S = \{z = 0\}$ and $B = \{z = xy\}$. Show that $\operatorname{Diff}_S(B)$ is the union of the two axes of $S \cong \mathbb{A}^2$, that $(S, \operatorname{Diff}_S(B))$ is lc and not klt, and conclude that $(X, S + B)$ is not plt. Is it lc near $S$? (Theorem 4.5.26 answers this.)
4. (B) Let $X$ be a smooth surface, $S$ an integral curve and $P \in S$ a point such that $(X, S)$ is lc near $P$. Show that $S$ is smooth or has a node at $P$. (Blow up $P$: a point of multiplicity $\mu$ gives an exceptional coefficient $\mu - 1$. For a double point with a single tangent line, blow up at most three times and find a coefficient greater than 1.)
5. (B) Let $X$ be the cone over a smooth projective curve $V$ of genus $g$ embedded by a line bundle of degree $d$, and $S$ a ruling. Using the minimal resolution, with $E \cong V$ and $E^2 = -d$, show that the coefficient of $\operatorname{Diff}_S(0)$ is $1 + \frac{2g - 1}{d}$ for $g \ge 1$. Deduce that $(X, S)$ is not lc for $g \ge 1$, and compare with Example 4.5.24.
6. (C) Let $(X, S + B)$ be a dlt pair with $\lfloor S + B \rfloor = S$. Show that $(X, S + B)$ is plt, and deduce from Theorem 4.5.17 that $(S^\nu, \operatorname{Diff}_{S^\nu}(B))$ is klt. (Over the snc locus, use Theorem 4.2.12 and the fact that $S$ is the only component of coefficient 1. Over the closed set $Z$ of Definition 4.2.2, use the definition.)

### Lean

Adjunction is not in Lean. The library has `MinimalModel.IsKlt`, `MinimalModel.IsLc` and `MinimalModel.IsDlt`, and `MinimalModel.IsSncAt`, but no plt, no different and no restriction of a pair to a divisor, so neither side of Theorem 4.5.17 can be stated.

### Notes and history

Adjunction for pairs is due to Shokurov (Sho92), who used it with inversion of adjunction as the main tool in his construction of 3-dimensional log flips. The normality of plt centres is KM98, Proposition 5.51, and its dlt version, KM98, Corollary 5.52, is used throughout the MMP with scaling, where the components of the boundary of a dlt pair have to be normal. Kol13, Chapter 4, extends adjunction to lc pairs and to lc centres of higher codimension, where the different is replaced by the different together with a moduli part, the subject of Kawamata's subadjunction and of the canonical bundle formula.
