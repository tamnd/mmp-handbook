---
title: The different
nodes: []
sources: [Sho92, Kol92, Kol13, KM98, Har77]
reads_with: [KM98:ch5, Kol13:ch4]
requires: [4.1, 4.2, 4.3, 2.3, P5.5, P5.6, P5.7, P5.8]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The different

### Statement

Let $X$ be a normal variety, $S \subset X$ a prime divisor and $B$ an $\mathbb{R}$-divisor with no component equal to $S$. If $X$ and $S$ are smooth, adjunction gives $(K_X + S)|_S = K_S$, and so $(K_X + S + B)|_S = K_S + B|_S$. In general $K_X + S$ need not be Cartier along $S$, and $S$ need not be normal. The *different* is the correction term that restores the formula, on the normalization of $S$. It was introduced by Shokurov (Sho92).

The surface case comes first, because there the different has a definition with no hypothesis at all. Let $X$ be a normal surface, $S \subset X$ an integral curve, $\nu \colon S^\nu \to S$ its normalization, and $B$ an $\mathbb{R}$-divisor on $X$ with no component equal to $S$. A resolution $f \colon Y \to X$ is *adapted to $S$* if the strict transform $S'$ of $S$ is smooth. Adapted resolutions exist: start from any resolution and blow up the singular points of the strict transform of $S$ until it is smooth (Theorem P5.6.17). For an adapted resolution, $f|_{S'} \colon S' \to S$ is finite and birational and $S'$ is smooth, so $f|_{S'}$ factors through an isomorphism $S' \cong S^\nu$. This section identifies $S'$ with $S^\nu$.

Fix a canonical divisor $K_X$ and choose $K_Y$ with $f_* K_Y = K_X$. Mumford's numerical pullback (Definition 4.3.3, Corollary P5.8.5) defines an $\mathbb{R}$-divisor $\Delta_Y$ on $Y$ by

$$K_Y + \Delta_Y = f^*(K_X + S + B).$$

The divisor $\Delta_Y$ does not depend on the choice of $K_X$: replacing $K_X$ by $K_X + \operatorname{div}(\varphi)$ replaces $K_Y$ by $K_Y + \operatorname{div}(\varphi)$ and $f^*(K_X + S + B)$ by $f^*(K_X + S + B) + \operatorname{div}(\varphi)$, since the numerical pullback of a principal divisor is its usual pullback. The coefficient of $S'$ in $\Delta_Y$ is 1, and every other non-exceptional component is the strict transform of a component of $B$, with the same coefficient. If $K_X + S + B$ is $\mathbb{R}$-Cartier, the numerical pullback is the usual one, and $(Y, \Delta_Y)$ is the crepant pullback of $(X, S + B)$ of Definition 4.1.4.

**Definition 4.5.1 (the different on a surface).** In this setting, the *different* of $B$ on $S^\nu$ is the $\mathbb{R}$-divisor

$$\operatorname{Diff}_{S^\nu}(B) = (\Delta_Y - S')|_{S'}$$

on $S' = S^\nu$. Explicitly, if $\Delta_Y = S' + \sum_D d_D D$ with $D \ne S'$, the coefficient of $\operatorname{Diff}_{S^\nu}(B)$ at a point $q \in S'$ is $\sum_D d_D \, (D \cdot S')_q$, a sum of local intersection numbers. When $S$ is normal, $S^\nu = S$ and the different is written $\operatorname{Diff}_S(B)$.

**Proposition 4.5.2 (independence of the resolution).** The divisor $\operatorname{Diff}_{S^\nu}(B)$ does not depend on the adapted resolution $f$.

Lean: not yet in Lean.

**Theorem 4.5.3 (the adjunction formula on a surface).** In this setting, suppose that $K_X + S + B$ is $\mathbb{R}$-Cartier. Then

$$K_{S^\nu} + \operatorname{Diff}_{S^\nu}(B) \sim_{\mathbb{R}} \nu^*(K_X + S + B).$$

If $S$ is proper, then $\deg\big(K_{S^\nu} + \operatorname{Diff}_{S^\nu}(B)\big) = (K_X + S + B) \cdot S$, with Mumford's intersection number, and this holds without the hypothesis that $K_X + S + B$ is $\mathbb{R}$-Cartier.

Lean: not yet in Lean.

**Proposition 4.5.4 (first properties on a surface).** In this setting:

1. $\operatorname{Diff}_{S^\nu}(B) = \operatorname{Diff}_{S^\nu}(0) + (f^*B)|_{S'}$. So the different is affine in $B$, and $\operatorname{Diff}_{S^\nu}(B) \ge \operatorname{Diff}_{S^\nu}(B')$ if $B \ge B'$.
2. $\operatorname{Diff}_{S^\nu}(0) \ge 0$, and so $\operatorname{Diff}_{S^\nu}(B) \ge 0$ if $B \ge 0$.
3. If $X$ and $S$ are smooth at a point $P$, then near $P$ the different is $B|_S$, and its coefficient at $P$ is the local intersection number $(B \cdot S)_P$.
4. $\operatorname{Diff}_{S^\nu}(0)$ is a $\mathbb{Q}$-divisor supported on $\nu^{-1}(\operatorname{Sing} X \cup \operatorname{Sing} S)$.

Lean: not yet in Lean.

In higher dimension the definition uses a log resolution. Let $X$ be a normal variety of dimension $n \ge 2$ over a field of characteristic 0, $S$ a prime divisor, $\nu \colon S^\nu \to S$ its normalization, and $B$ an $\mathbb{R}$-divisor with no component equal to $S$, such that $K_X + S + B$ is $\mathbb{R}$-Cartier. Let $f \colon Y \to X$ be a log resolution of $(X, S + B)$ (Theorem 4.2.10), and $K_Y + \Delta_Y = f^*(K_X + S + B)$ the crepant pullback. The strict transform $S'$ is a component of an snc divisor, so it is smooth, and $f|_{S'}$ is birational onto $S$. It factors through a birational morphism $g \colon S' \to S^\nu$, by the universal property of the normalization. For each component $D \ne S'$ of $\Delta_Y$, the restriction $D|_{S'}$ is a reduced smooth divisor, and different $D$ give divisors with no common component.

**Definition 4.5.5 (the different).** In this setting, the *different* is

$$\operatorname{Diff}_{S^\nu}(B) = g_*\big((\Delta_Y - S')|_{S'}\big),$$

an $\mathbb{R}$-divisor on $S^\nu$. When $S$ is normal it is written $\operatorname{Diff}_S(B)$.

**Proposition 4.5.6 (the different in higher dimension).** In this setting:

1. $\operatorname{Diff}_{S^\nu}(B)$ does not depend on the log resolution $f$. In dimension 2 it is the different of Definition 4.5.1.
2. (*Adjunction formula.*) $K_{S^\nu} + \operatorname{Diff}_{S^\nu}(B) \sim_{\mathbb{R}} \nu^*(K_X + S + B)$, and the sub-pair $(S', (\Delta_Y - S')|_{S'})$ is the crepant pullback of $(S^\nu, \operatorname{Diff}_{S^\nu}(B))$ by $g$.
3. If $X$ is smooth and $S$ is smooth near a point, then near that point $\operatorname{Diff}_S(B) = B|_S$.

Lean: not yet in Lean.

If $B \ge 0$, the different is effective in every dimension (Kol13, Chapter 4). On surfaces this is part 2 of Proposition 4.5.4, and this chapter uses it only there.

### Proof in words

The different on a surface is read off from the coefficients of the curves of $Y$ that meet $S'$. A further blow-up at a point $p$ of $S'$ changes $\Delta_Y - S'$ by the pullback of $\Delta_Y - S'$ and by a multiple of the new curve $F$, and that multiple is $\operatorname{mult}_p S' - 1 = 0$ because $S'$ is smooth. So nothing changes on $S'$, and any two adapted resolutions are compared through a common blow-up.

The adjunction formula is the adjunction formula on the smooth surface $Y$, restricted to $S'$: the class $(K_Y + S')|_{S'}$ is $K_{S'}$, and the rest of $f^*(K_X + S + B)$ restricts to the different.

Effectivity comes from the minimal resolution, on which $f^*K_X - K_Y$ is effective by the negativity lemma. Blowing up singular points of the strict transform of $S$ only adds effective terms, with multiplicity $\operatorname{mult}_p - 1 \ge 0$.

In higher dimension, the coefficient of the different along a prime divisor $Q$ of $S^\nu$ is a statement about a neighbourhood of the generic point of the image of $Q$, which has codimension 2 in $X$. General hyperplane sections through a general point of that image cut $X$ to a surface and $f$ to a log resolution of the surface, and the coefficient becomes a coefficient of a surface different. So independence in higher dimension follows from the surface case.

### Examples

**Example 4.5.7 (curves in the plane).** Let $X = \mathbb{A}^2$, $S = \{y = 0\}$ and $P$ the origin. For $B = b\{x = 0\}$, part 3 of Proposition 4.5.4 gives $\operatorname{Diff}_S(B) = bP$, and for $B = b\{y = x^k\}$ it gives $\operatorname{Diff}_S(B) = kbP$, since $\{y = x^k\}$ meets $S$ at $P$ with multiplicity $k$. With $X$ and $S$ smooth, the different only records the intersection of $B$ with $S$.

**Example 4.5.8 (the quadric cone).** Let $X = \{xy = z^2\} \subset \mathbb{A}^3$, the $A_1$ singularity, and $S = \{x = z = 0\}$, a line through the vertex $P$. The minimal resolution $f \colon Y \to X$ is the blow-up of $P$. It has one exceptional curve $E \cong \mathbb{P}^1$ with $E^2 = -2$, and $Y$ is the total space of $\mathcal{O}_{\mathbb{P}^1}(-2)$, in which $S'$ is a fibre. So $S'$ is smooth and meets $E$ once, transversally (Problem 4 of Chapter 2). The point $P$ is Du Val, so $K_Y = f^*K_X$ and $K_Y \cdot E = 0$. Write $\Delta_Y = S' + cE$. The condition $(K_Y + \Delta_Y) \cdot E = 0$ reads $0 + 1 - 2c = 0$, so $c = \frac12$. The different is

$$\operatorname{Diff}_S(0) = \tfrac12 P.$$

Check of the adjunction formula. Let $\bar X \subset \mathbb{P}^3$ be the projective quadric cone and $\bar S$ the closure of $S$, a line through the vertex. A plane tangent to $\bar X$ along $\bar S$ cuts $2\bar S$, so $\bar S \equiv \frac12 H$ with $H$ the hyperplane class, and $K_{\bar X} = -2H$ by adjunction for the quadric in $\mathbb{P}^3$. So $(K_{\bar X} + \bar S) \cdot \bar S = -\frac32 H \cdot \bar S = -\frac32$. On the other side, $\deg(K_{\mathbb{P}^1} + \frac12 P) = -2 + \frac12 = -\frac32$, as Theorem 4.5.3 predicts. The term $\frac12 P$ is exactly what the formula $(K + S)|_S = K_S$ misses at the singular point.

**Example 4.5.9 (the node: the different lives on the normalization).** Let $X = \mathbb{A}^2$ and $S = \{y^2 = x^2(x + 1)\}$, the nodal cubic, with node $P$. The blow-up $f$ of $P$ has $f^*S = S' + 2E$ and $K_Y = f^*K_X + E$, so $\Delta_Y = S' + 2E - E = S' + E$. The curve $S'$ is smooth and meets $E$ transversally at two points $q_1$, $q_2$, the two branches of the node (Example 4.2.17). So

$$\operatorname{Diff}_{S^\nu}(0) = q_1 + q_2,$$

the preimage of the node on $S^\nu \cong \mathbb{A}^1$, with the parametrization $t \mapsto (t^2 - 1, t(t^2 - 1))$ and $q_{1,2} = \{t = \pm 1\}$. This is the conductor of $\nu$. For the projective nodal cubic $\bar S \subset \mathbb{P}^2$, $(K_{\mathbb{P}^2} + \bar S) \cdot \bar S = 0$ and $\deg(K_{\mathbb{P}^1} + q_1 + q_2) = 0$. The different cannot be defined on $S$ itself: $S$ is not normal, and the formula holds on $S^\nu$, where the conductor appears as part of the different.

**Example 4.5.10 (the cusp).** Let $X = \mathbb{A}^2$ and $S = \{y^2 = x^3\}$. One blow-up $f$ of the origin already makes $S'$ smooth, with $f^*S = S' + 2E$ and $\Delta_Y = S' + E$, and $S'$ meets $E$ at one point $q$ with $(E \cdot S')_q = 2$, since $S'$ is tangent to $E$. So $\operatorname{Diff}_{S^\nu}(0) = 2q$, even though $q$ is the only point over $P$. The adjunction check on the projective cuspidal cubic is $0 = -2 + 2$. The log resolution of Example 4.2.16, with $t = 1$, gives $\Delta_Y = S' + E_1 + E_2 + 2E_3$ with $S'$ meeting only $E_3$, transversally: the same different $2q$, as Proposition 4.5.2 requires.

### Proof

*Proof of Proposition 4.5.2.* Let $f \colon Y \to X$ be adapted, $p \in Y$ a point, and $h \colon Y'' \to Y$ the blow-up of $p$, with exceptional curve $F$. Then $f \circ h$ is again a resolution, by Proposition 2.3.3 its numerical pullback is $h^* f^*$, and $K_{Y''} = h^* K_Y + F$ (Theorem P5.6.3). So $\Delta_{Y''} = h^*\Delta_Y - F$. By Proposition P5.6.4, $h^*S' = S'' + \mu F$ with $\mu = \operatorname{mult}_p S' \in \{0, 1\}$, since $S'$ is smooth. Hence

$$\Delta_{Y''} - S'' = h^*(\Delta_Y - S') + (\mu - 1) F.$$

If $\mu = 0$, then $h$ is an isomorphism near $S''$ and the two restrictions agree. If $\mu = 1$, then $h|_{S''} \colon S'' \to S'$ is an isomorphism, the coefficient of $F$ is 0, and for every divisor $D$ not containing $S'$ the projection formula gives $(h^*D)|_{S''} = (h|_{S''})^*(D|_{S'})$. So the restrictions agree again, and the different of $f \circ h$ is the different of $f$. Since $S''$ is smooth, $f \circ h$ is adapted.

Now let $f_1 \colon Y_1 \to X$ and $f_2 \colon Y_2 \to X$ be adapted. The birational map $Y_1 \dashrightarrow Y_2$ over $X$ becomes a morphism after finitely many point blow-ups of $Y_1$, and the resulting morphism to $Y_2$ is a composite of point blow-ups (Theorem P5.7.13, whose proof by elimination of indeterminacy is local over $X$). So there are a resolution $Y_3$ and composites of point blow-ups $Y_3 \to Y_1$ and $Y_3 \to Y_2$ over $X$. By the first paragraph, applied one blow-up at a time, $f_1$, $f_3$ and $f_2$ give the same different. $\square$

*Proof of Theorem 4.5.3.* Write $L = K_X + S + B$, an $\mathbb{R}$-Cartier divisor, so $L \sim_{\mathbb{R}} \sum_i r_i L_i$ with $L_i$ Cartier, and $f^*L$ and $\nu^*L$ are defined in $\operatorname{Pic} \otimes \mathbb{R}$. Since $f|_{S'} = \nu$ under the identification $S' = S^\nu$, functoriality of pullback gives $(f^*L)|_{S'} = \nu^* L$. On the other side,

$$f^*L = K_Y + S' + (\Delta_Y - S'),$$

and $S'$ is not a component of $\Delta_Y - S'$, so the class of $\Delta_Y - S'$ restricts to the divisor $(\Delta_Y - S')|_{S'} = \operatorname{Diff}_{S^\nu}(B)$. The adjunction formula on the smooth surface $Y$ (Theorem P5.5.14) gives $(K_Y + S')|_{S'} \sim K_{S'}$. Adding the two restrictions proves the formula.

For the degree, $\deg (K_Y + \Delta_Y)|_{S'} = f^*L \cdot S'$. The divisor $f^*S - S'$ is exceptional and $f^*L \cdot E = 0$ for every exceptional curve $E$, so $f^*L \cdot S' = f^*L \cdot f^*S = L \cdot S$, Mumford's intersection number. By the genus formula, $\deg (K_Y + S')|_{S'} = 2p_a(S') - 2 = \deg K_{S^\nu}$. Subtracting gives $\deg \operatorname{Diff}_{S^\nu}(B) = L \cdot S - \deg K_{S^\nu}$, which uses only numerical pullback. $\square$

*Proof of Proposition 4.5.4.* (1) The numerical pullback is linear (Corollary P5.8.5), so $\Delta_Y(B) = \Delta_Y(0) + f^*B$. The divisor $f^*B$ is $f^{-1}_*B$ plus an exceptional divisor, so it does not contain $S'$, and restricting gives the formula. If $B \ge B'$, then $f^*(B - B') \ge 0$ by Corollary P5.8.5, and its restriction to $S'$ is effective.

(2) The question is local near the singular points of $X$ on $S$, and the different does not depend on the resolution. Let $f_0 \colon Y_0 \to X$ be the minimal resolution (Definition 4.3.4) and $S_0$ the strict transform of $S$. By Proposition 4.3.5, the numerical discrepancies satisfy $a_i \le 0$, so $f_0^*K_X - K_{Y_0} = -\sum_i a_i E_i \ge 0$. By Corollary P5.8.5, $f_0^*S \ge 0$, and $f_0^*S - S_0$ is its exceptional part, so it is effective. So $\Delta_{Y_0} - S_0 = (f_0^*K_X - K_{Y_0}) + (f_0^*S - S_0) \ge 0$. The curve $S_0$ may be singular. Blow up a singular point $p$ of $S_0$, with $\mu = \operatorname{mult}_p S_0 \ge 2$. The computation in the proof of Proposition 4.5.2 gives $\Delta'' - S'' = h^*(\Delta_{Y_0} - S_0) + (\mu - 1)F \ge 0$. By Theorem P5.6.15, finitely many such blow-ups make the strict transform smooth, and at each step $\Delta - S'$ stays effective. On the resulting adapted resolution, $\Delta_Y - S' \ge 0$ and it does not contain $S'$, so its restriction to $S'$ is effective. With part 1, $B \ge 0$ gives $\operatorname{Diff}_{S^\nu}(B) \ge \operatorname{Diff}_{S^\nu}(0) \ge 0$.

(3) Near $P$, the identity is an adapted resolution, $\Delta_Y = S + B$, and $(\Delta_Y - S)|_S = B|_S$, whose coefficient at $P$ is $(B \cdot S)_P$.

(4) The numerical pullback of the integral divisor $K_X + S$ is a $\mathbb{Q}$-divisor (Corollary P5.8.5), so the different of $0$ has rational coefficients. By part 3 with $B = 0$, it vanishes over the points where $X$ and $S$ are smooth. $\square$

*Proof of Proposition 4.5.6 (a sketch).* (2) The divisor $S'$ is smooth, and adjunction on the smooth variety $Y$ gives $(K_Y + S')|_{S'} \sim K_{S'}$ (Har77, Chapter II, Proposition 8.20). As in the proof of Theorem 4.5.3, restricting $f^*(K_X + S + B) = K_Y + S' + (\Delta_Y - S')$ to $S'$ gives

$$K_{S'} + (\Delta_Y - S')|_{S'} \sim_{\mathbb{R}} g^* \nu^*(K_X + S + B).$$

Push forward by $g$. Choose $K_{S'}$ with $g_* K_{S'} = K_{S^\nu}$; the pushforward of a principal divisor is principal, and $g_* g^* M = M$ for an $\mathbb{R}$-Cartier $M$ on the normal variety $S^\nu$. This gives the adjunction formula. The difference $G = K_{S'} + (\Delta_Y - S')|_{S'} - g^*(K_{S^\nu} + \operatorname{Diff}_{S^\nu}(B))$ is then $g$-exceptional and $\mathbb{R}$-linearly trivial, hence numerically trivial over $S^\nu$. By the negativity lemma (KM98, Lemma 3.39) it is zero, which is the crepant statement.

(1) Let $Q$ be a prime divisor of $S^\nu$, and $Q'$ its strict transform on $S'$. The coefficient of $\operatorname{Diff}_{S^\nu}(B)$ along $Q$ is the coefficient of $Q'$ in $(\Delta_Y - S')|_{S'}$. By the snc condition, $Q'$ lies in $D \cap S'$ for at most one component $D \ne S'$ of $\Delta_Y$, and then the coefficient is $d_D$, and otherwise it is 0. The image $Z = \nu(Q)$ has codimension 2 in $X$. The question is local near a general point $z$ of $Z$, so take $X$ quasi-projective, and let $H_1, \dots, H_{n-2}$ be general members of a very ample linear system through $z$. By the Bertini theorems (Har77, Chapter III, Theorem 10.9 and Remark 10.9.2) and the argument in the proof of Theorem 4.4.15, near $z$ the intersection $X_H = X \cap H_1 \cap \dots \cap H_{n-2}$ is a normal surface, $S_H = S \cap X_H$ is a curve, $Y_H = f^{-1}(X_H)$ is a smooth surface, and $f_H = f|_{Y_H}$ is a log resolution of $(X_H, S_H + B_H)$ near $z$, where $B_H = B|_{X_H}$. Adjunction for the $H_i$ on $X$ and for their pullbacks on $Y$ gives $K_{Y_H} + \Delta_Y|_{Y_H} = f_H^*(K_{X_H} + S_H + B_H)$, so the crepant pullback of the surface pair is $\Delta_Y|_{Y_H}$, in which every curve of $D \cap Y_H$ has coefficient $d_D$. So the coefficient of $\operatorname{Diff}_{S^\nu}(B)$ along $Q$ is the coefficient at each point of $Q' \cap Y_H$ of the surface different of $B_H$ on $S_H^\nu$. That surface different depends only on $(X_H, S_H, B_H)$, by Proposition 4.5.2, and a general choice of the $H_i$ works for two log resolutions at once. So the coefficient does not depend on $f$. In dimension 2, a log resolution is adapted to $S$ and the two definitions agree, since then $g$ is an isomorphism.

(3) Both sides are divisors on $S$, so it suffices to compare their coefficients along each prime divisor $Q$ of $S$ near the given point. By the proof of part 1, the coefficient of $\operatorname{Diff}_S(B)$ along $Q$ is the coefficient of a surface different on a general surface section $X_H$ through a general point of $Q$. There $X_H$ and $S_H$ are smooth, and part 3 of Proposition 4.5.4 gives the coefficient of $B_H|_{S_H}$, which is the coefficient of $B|_S$ along $Q$. $\square$

### Exercises

1. (A) Let $X = \mathbb{A}^2$, $S = \{y = 0\}$ and $B = \frac12\{y = x^2\} + \frac13\{x = 0\}$. Compute $\operatorname{Diff}_S(B)$, and check it on a log resolution of $(X, S + B)$.
2. (A) Let $S = \{y^2 = x^5\} \subset \mathbb{A}^2$. Blow up until the strict transform is smooth, and show that $\operatorname{Diff}_{S^\nu}(0) = 4q$, where $q$ is the point over the origin. Check the degree of Theorem 4.5.3 on the closure of $S$ in $\mathbb{P}^2$, a quintic with one singular point.
3. (B) Let $X$ be a normal surface and $S$ a curve with $S \subset X$ Cartier and $X$ smooth along $S$. Show that $\operatorname{Diff}_{S^\nu}(0)$ is the conductor divisor of $\nu$ in the sense that its degree over a point $P$ is $2\delta_P$ for a curve with only nodes and ordinary cusps, where $\delta_P$ is the $\delta$-invariant (Proposition P5.6.14). Check the formula on Examples 4.5.9 and 4.5.10.
4. (B) In Example 4.5.8, blow up the point $S' \cap E$ and verify directly that the new resolution gives the same different $\frac12 P$, as in the proof of Proposition 4.5.2.
5. (B) Let $X = \frac13(1,1)$, the cone over the twisted cubic, and $S$ the image of a line through the origin. Show that the minimal resolution has one curve $E$ with $E^2 = -3$, that $K_Y \cdot E = 1$, and that $\operatorname{Diff}_S(0) = \frac23 P$.
6. (C) Let $X$ be a normal surface, $S$ an integral curve and $P \in S$ a point. Show that the coefficient of $\operatorname{Diff}_{S^\nu}(0)$ at a point $q$ over $P$ is 0 if and only if $X$ is smooth at $P$ and $S$ is smooth at $P$. (Use the minimal resolution and the proof of part 2 of Proposition 4.5.4: if $X$ is singular at $P$, every coefficient of $f_0^*S - S_0$ over $P$ is positive.)

### Lean

The different is not in Lean. The library has `MinimalModel.IsKlt` and `MinimalModel.IsLc`, which this section does not use, and no Mumford pullback, no normalization of a divisor and no restriction of divisors to a divisor.

### Notes and history

Shokurov introduced the different in his paper on 3-dimensional log flips (Sho92), as the correction term that makes adjunction hold for a pair. The name comes from the different of algebraic number theory, which measures ramification in the same way. Kollár's chapter in Kol92, Chapter 16, gives the definition by residues of forms, and Kol13, Chapter 4, treats the different on a normal or demi-normal divisor in general, with the proof that it is effective. The surface definition by Mumford's pullback is in KM98, Section 4.1, and in Kol13, Chapter 3. The examples of the node and the cusp show the two ways the normalization enters: the conductor is part of the different, and the different can exceed 1 when the pair is not lc.
