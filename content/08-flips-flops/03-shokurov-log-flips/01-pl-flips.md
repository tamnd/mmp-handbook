---
title: Pl flips and the restricted algebra
nodes: []
sources: [Sho92, Cor07, KM98, Fuj11]
reads_with: [Cor07:2, KM98:3.7]
requires: [1.1, 3.5, 4.2, 4.5, 5.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Pl flips and the restricted algebra

### Statement

The ground field $k$ is algebraically closed of characteristic $0$. For a prime divisor $S$ on a normal variety $X$ and a $\mathbb{Q}$-divisor $B$ with no component equal to $S$, the different $\operatorname{Diff}_S(B)$ is as in Definition 4.5.5, so that $(K_X + S + B)|_S = K_S + \operatorname{Diff}_S(B)$ when $K_X + S + B$ is $\mathbb{Q}$-Cartier and $S$ is normal (Theorem 4.5.17).

**Definition 8.3.1 (pl flipping contractions).** A *pl flipping contraction* is a small contraction $f \colon X \to Z$ of normal varieties with $\operatorname{Exc}(f) \ne \emptyset$, together with a pair $(X, S + B)$ with the following properties: $X$ is $\mathbb{Q}$-factorial, $S$ is a prime divisor, $\lfloor B \rfloor = 0$, $(X, S + B)$ is plt, $\rho(X/Z) = 1$, and both $-(K_X + S + B)$ and $-S$ are ample over $Z$. Its *pl flip* is the flip of $f$ as a flipping contraction of $(X, S + B)$.

**Lemma 8.3.2 (the pl flip is the flip of $S$).** Let $f$ be a pl flipping contraction with $X$ projective. Then $K_X + S + B \sim_{\mathbb{Q}} aS + f^* L$ for a rational number $a > 0$ and a $\mathbb{Q}$-Cartier divisor $L$ on $Z$, and the pl flip exists if and only if the $S$-flip exists, and then they are equal. So the pl flip exists if and only if $R(X/Z, S)$ is finitely generated.

Lean: not yet in Lean.

**Definition 8.3.3 (the restricted algebra).** Let $f \colon X \to Z$ be a small contraction with $Z = \operatorname{Spec} A$ affine, $S$ a prime divisor on $X$, $R = R(X/Z, S)(Z) = \bigoplus_m H^0(X, \mathcal{O}_X(mS)) t^m$, and $\sigma = 1 \cdot t \in R_1$, the section of $\mathcal{O}_X(S)$ that cuts out $S$. The *restricted algebra* of $S$ is the graded $A$-algebra $R_S = R / \sigma R$, with
$$(R_S)_m = H^0(X, \mathcal{O}_X(mS)) / H^0(X, \mathcal{O}_X((m-1)S)).$$
If $mS$ is Cartier, $(R_S)_m$ is the image of the restriction map $H^0(X, \mathcal{O}_X(mS)) \to H^0(S, \mathcal{O}_X(mS)|_S)$.

**Theorem 8.3.4 (finite generation can be checked on $S$).** In the situation of Definition 8.3.3, $R$ is a finitely generated $A$-algebra if and only if the restricted algebra $R_S$ is.

Lean: not yet in Lean.

**Theorem 8.3.5 (reduction to pl flips).** Let $n \ge 2$. Suppose that pl flips exist for $n$-dimensional pl flipping contractions, and that special termination holds in dimension $n$ in the sense of Theorem 8.3.6. Then the flip of every flipping contraction of an $n$-dimensional $\mathbb{Q}$-factorial klt pair exists.

Lean: not yet in Lean.

**Theorem 8.3.6 (special termination for 3-folds).** Let $(X, B)$ be a $\mathbb{Q}$-factorial dlt 3-fold pair and $X = X_0 \dashrightarrow X_1 \dashrightarrow X_2 \dashrightarrow \cdots$ a sequence of flips of extremal rays for the pairs $(X_i, B_i)$, with $B_i$ the strict transforms of $B$. Then after finitely many steps the flipping loci are disjoint from $\lfloor B_i \rfloor$.

Lean: not yet in Lean.

Theorem 8.3.4 is proved in full. Theorems 8.3.5 and 8.3.6 are due to Shokurov; they are given with outlines of the proofs, and the details are in Cor07, in the chapters of Corti and of Fujino, and in Fuj11 for the general setting.

### Proof in words

Since $K_X + S + B$ and $S$ are both negative on the single ray contracted by $f$, they are proportional up to a pullback from $Z$, and Corollary 8.1.7 identifies the two flips. The restricted algebra is the quotient of $R$ by a single homogeneous element of degree $1$, so generators of the quotient together with that element generate $R$, by induction on the degree. The quotient is an algebra of sections on $S$, which is a normal variety of one dimension less with the klt pair $(S, \operatorname{Diff}_S(B))$ given by adjunction.

For the reduction, one passes to a log resolution of the klt flipping contraction and puts all exceptional divisors in the boundary with coefficient $1$. A minimal model program over $Z$ for this dlt pair only ever contracts rays that are negative on a component of the reduced boundary, so all its flips are pl flips; special termination stops it, and its output is the flip.

Special termination for 3-folds is a statement about surfaces: by adjunction a flip of the 3-fold restricts on each component of $\lfloor B \rfloor$ to a birational map of surfaces, and since surfaces have no flips this map is a composition of contractions of curves, which can only happen finitely often.

### Examples

**Example 8.3.7 (the Francia flip is a pl flip).** In Proposition 8.1.13 take $S = D_1$ and $B = 0$. The toric pair $(X^-, D_1)$ has log discrepancy at a primitive vector $w$ of $N$ equal to $\psi(w)$, where $\psi$ is the piecewise linear function on the fan with $\psi(u_1) = 0$ and $\psi(u_2) = \psi(u_3) = \psi(u_4) = 1$; this function is positive on every primitive vector not on the ray of $u_1$, so $(X^-, D_1)$ is plt, and $X^-$ is $\mathbb{Q}$-factorial as its fan is simplicial. From the computation in the proof of Proposition 8.1.13, $D_1 \cdot C^- = -\frac12$ and $(K_{X^-} + D_1) \cdot C^- = -\frac12 - \frac12 = -1$, so $f^-$ is a pl flipping contraction, and its pl flip is the Francia flip $X^+$.

On $S = D_1$, the toric surface of the star of $u_1$ in $N / \mathbb{Z} u_1$, the images $\bar u_3, \bar u_4$ form a basis and $\bar u_2 = \bar u_3 + 2 \bar u_4$, since $u_2 \equiv u_3 + 2u_4$ modulo $u_1$. So $S$ has the cones $(\bar u_2, \bar u_3)$, a point of type $A_1$ at the $\frac12(1,1,1)$ point of $X^-$, and $(\bar u_2, \bar u_4)$, a smooth point, and $f$ restricts to the morphism $S \to T = f(S) \cong \mathbb{A}^2$ that subdivides $\operatorname{Cone}(\bar u_3, \bar u_4)$ at $\bar u_3 + 2 \bar u_4$: the weighted blow-up of a smooth surface point with weights $(1, 2)$. Its exceptional curve is $C^- \subset S$, with $(C^-)^2_S = -\frac12$ and $K_S \cdot C^- = -1$, which matches $(K_{X^-} + D_1) \cdot C^- = -1$ by adjunction, as $X^-$ is singular only at a point and the different is $0$. On the other side, the star of $u_1$ in the fan of $X^+$ is the single cone $\operatorname{Cone}(\bar u_3, \bar u_4)$, so $D_1^+ \cong T$: the flip restricts to the divisorial contraction $S \to T$ on the plt centre, which is the mechanism of special termination.

**Example 8.3.8 (the restricted algebra of the Atiyah flop).** In Proposition 8.1.11 take $S = \Pi_1'$ on $X_1$. This is a flop, not a pl flip, but the restricted algebra is computed in the same way. The preimage of $\Pi_1$ is $\{z = 0\}$ in the chart $(s, y, z)$, mapping by $(s, y) \mapsto (y, w) = (y, sy)$ to $\Pi_1 \cong \mathbb{A}^2_{y, w}$, and $\{x = 0\}$ in the chart $(t, x, w)$, mapping by $(t, w) \mapsto (tw, w)$. So $S$ is the blow-up of $\Pi_1$ at the origin, with exceptional curve $C_1$. On $S$, $\operatorname{Pic}(S) = \mathbb{Z} C_1$ and $S|_S \cdot C_1 = S \cdot C_1 = -1 = C_1^2$, so $\mathcal{O}_X(S)|_S \cong \mathcal{O}_S(C_1)$, and $H^0(S, \mathcal{O}_S(mC_1)) = k[y, w]$ for every $m \ge 0$, since a function with a pole along $C_1$ only is regular on $\mathbb{A}^2 \setminus \{0\}$, hence on $\mathbb{A}^2$. The restriction maps are surjective (Exercise 5), so $R_S \cong k[y, w][\tau]$ with $\tau$ of degree $1$, and $\operatorname{Proj} R_S = \Pi_1$. This is the strict transform of $\Pi_1$ on $X_2$, which is isomorphic to $\Pi_1$, since $\Pi_1$ meets the centre $\Pi_2$ of the blow-up $X_2 \to Z$ in the line $\{x = z = w = 0\}$, a Cartier divisor on $\Pi_1$. As in Example 8.3.7, the flop restricts on $S$ to a contraction of a curve.

### Proof

*Lemma 8.3.2.* Fix a curve $C$ contracted by $f$. As $\rho(X/Z) = 1$, the curves contracted by $f$ span an extremal ray $R$ of $\overline{NE}(X)$, and $f$ is its contraction. Let $a = (K_X + S + B) \cdot C / (S \cdot C)$, a positive rational number since both intersection numbers are negative. The pair $(X, (1 - \varepsilon) S + B)$ is klt for $0 < \varepsilon < 1$, since $(X, S + B)$ is plt and $X$ is $\mathbb{Q}$-factorial, and it is negative on $R$ for small $\varepsilon$. So Theorem 1.1.12 applies to it and to the divisor $K_X + S + B - aS$, which is zero on $R$, and gives $K_X + S + B - aS \sim_{\mathbb{Q}} f^* L$. By part 2 of Corollary 8.1.7, the $(K_X + S + B)$-flip and the $S$-flip agree, and by Theorem 8.1.6 the $S$-flip exists if and only if $R(X/Z, S)$ is finitely generated. Without the projectivity of $X$, the same holds by the relative contraction theorem (KM98, Theorem 3.25).

*Definition 8.3.3, the restriction map.* Let $mS$ be Cartier. A section $s \in H^0(X, \mathcal{O}_X(mS))$ restricts to $0$ on $S$ if and only if it lies in $\mathcal{I}_S \cdot \mathcal{O}_X(mS) = \mathcal{O}_X(-S) \otimes \mathcal{O}_X(mS) = \mathcal{O}_X((m-1)S)$, where the equality uses that $\mathcal{O}_X(mS)$ is invertible. The inclusion $\mathcal{O}_X((m-1)S) \subseteq \mathcal{O}_X(mS)$ is multiplication by $\sigma$, so the kernel of the restriction is $\sigma R_{m-1}$.

*Theorem 8.3.4.* The element $\sigma$ is homogeneous of degree $1$. If $R$ is generated by $x_1, \dots, x_r$, then $R_S$ is generated by their images. Conversely, suppose $R_S$ is generated over $A$ by the images of homogeneous elements $x_1, \dots, x_r \in R$ of positive degree; this is possible since $(R_S)_0 = R_0 = A$. Let $T = A[\sigma, x_1, \dots, x_r] \subseteq R$. Prove $R_m \subseteq T$ by induction on $m$. For $m = 0$, $R_0 = A$. Let $m \ge 1$ and $y \in R_m$. The image of $y$ in $(R_S)_m$ is $P(\bar x_1, \dots, \bar x_r)$ for a polynomial $P$ over $A$ that is homogeneous of degree $m$ for the grading $\deg x_i$, so $y - P(x_1, \dots, x_r) \in \sigma R \cap R_m = \sigma R_{m-1}$, as $\sigma R$ is a graded ideal and $R$ is a domain. By induction $R_{m-1} \subseteq T$, so $y \in T$. Hence $R = T$ is finitely generated.

*Theorem 8.3.5, outline.* Let $f \colon X \to Z$ be a flipping contraction of an $n$-dimensional $\mathbb{Q}$-factorial klt pair $(X, \Delta)$. The flip is local over $Z$ by Corollary 8.1.7, so assume $Z$ affine. Let $g \colon Y \to X$ be a log resolution of $(X, \Delta)$ (Definition 4.2.9 and Theorem 4.2.10), with exceptional divisors $E_1, \dots, E_k$, and let $B_Y = g^{-1}_* \Delta + \sum_i E_i$. The pair $(Y, B_Y)$ is dlt, and $K_Y + B_Y = g^*(K_X + \Delta) + \sum_i (1 + a(E_i, X, \Delta)) E_i$ with every coefficient $1 + a(E_i, X, \Delta) > 0$, as $(X, \Delta)$ is klt. The relative log canonical model of $(Y, B_Y)$ over $Z$, if it exists, is the flip of $f$: it is $\operatorname{\mathbf{Proj}}_Z \bigoplus_m h_* \mathcal{O}_Y(\lfloor m(K_Y + B_Y) \rfloor)$ for $h = f \circ g$, and the exceptional divisors contribute nothing to these sheaves, so the algebra is the relative canonical algebra of $(X, \Delta)$ over $Z$. One runs a $(K_Y + B_Y)$-minimal model program over $Z$ with scaling of a suitable divisor. Because $K_Y + B_Y$ is a positive combination of the $E_i$ plus a divisor whose pushforward to $Z$ is anti-ample on the flipping curves, after a perturbation of the boundary every negative extremal ray of each step is negative on some component of the reduced boundary; so each divisorial contraction is harmless and each flip is a pl flip, which exists by hypothesis. Special termination shows that after finitely many steps no flip meets the reduced boundary, so the program stops; at the end all the $E_i$ are contracted, and the result is the flip of $f$. The details, including the choice of the scaling divisor and the perturbation, are in Cor07 in Fujino's chapter, and in Fuj11.

*Theorem 8.3.6, outline.* Step 1, the lc centres. The lc centres of the dlt pair $(X_i, B_i)$ are the strata of $\lfloor B_i \rfloor$, the components of intersections of its components, and there are finitely many. A flip creates no new lc centre, since discrepancies do not decrease (Lemma 8.1.19), and an lc centre contained in a flipping locus disappears, since the discrepancy $-1$ of a divisor over it increases strictly. So after finitely many steps no flipping locus contains an lc centre. In particular the flips are eventually isomorphisms near the strata of dimension $0$.

Step 2, the surfaces. Each component $S_i$ of $\lfloor B_i \rfloor$ is normal (Theorem 4.5.18, applied after lowering the coefficients of the other components), and the flip induces a birational map $S_i \dashrightarrow S_{i+1}$ onto the corresponding component of $\lfloor B_{i+1} \rfloor$. By adjunction (Theorem 4.5.17), $(S_i, \operatorname{Diff}_{S_i}(B_i - S_i))$ is a dlt surface pair, and by Lemma 8.1.19 its discrepancies do not decrease along the sequence and increase strictly over the points where a flipping locus meets $S_i$. A divisor on $S_{i+1}$ that is exceptional over $S_i$ has discrepancy at most $0$ over $S_i$, and over a surface pair of this kind there are only finitely many exceptional divisors with discrepancy at most $0$ that are not lc places. A count of these divisors, of the kind used for the difficulty in Chapter 4, shows that after finitely many steps the maps $S_i \dashrightarrow S_{i+1}$ extract no divisors, so they are morphisms that contract curves, and then that the Picard numbers of the $S_i$ stop dropping, so the maps are isomorphisms. Finally a flipping curve that meets $S_i$ but is not contained in it meets it in finitely many points, where the discrepancies of the surface pair increase strictly; as they take values in a finite set below $1$ near the points that matter, this also stops. The complete argument, which also handles the curve strata, is in Cor07, in Fujino's chapter, and in Fuj11.

### Exercises

1. (A) In Example 8.3.7, compute the discrepancy of $D_v$, $v = u_3 + u_4$, with respect to $(X^-, D_1)$ and $(X^+, D_1^+)$, and check that it increases.
2. (A) Show that in Example 8.3.7 the divisor $D_3$ cannot be used as $S$: compute $D_3 \cdot C^-$ and decide which conditions of Definition 8.3.1 fail.
3. (A) Let $R = A[\sigma, x]$ with $\deg \sigma = 1$ and $\deg x = 2$. Compute $R / \sigma R$ and check Theorem 8.3.4 in this case.
4. (B) For the weighted blow-up $S \to T = \mathbb{A}^2$ with weights $(1, 2)$ in Example 8.3.7, compute the algebra $\bigoplus_m H^0(S, \mathcal{O}_S(-mC^-))$, with $C^-$ the exceptional curve and $mC^-$ read as $\lfloor mC^- \rfloor$ on the singular surface, as an algebra of ideals in $k[x, y]$.
5. (B) In Example 8.3.8, show directly that the restriction maps $\mathcal{O}_Z(m \Pi_1) \to H^0(S, \mathcal{O}_S(mC_1))$ are surjective, by restricting the generator $u^m$ of $\mathcal{O}_Z(m\Pi_1)$ modulo $\mathcal{O}_Z((m-1)\Pi_1)$.
6. (C) Let $(X, S + B)$ be a pl flipping contraction with $S$ normal. Using Theorem 5.1.13, show that $H^1(X, \mathcal{O}_X(mS - S)) = 0$ for $m \ge 1$ such that $mS$ is Cartier and $mS - S - (K_X + S + B)$ is ample over $Z$, and deduce that for such $m$ the restriction map in Definition 8.3.3 is surjective onto $H^0(S, \mathcal{O}_X(mS)|_S)$.

### Lean

Nothing in this section is in Lean. The library has `MinimalModel.SpecialTermination` for the special termination hypothesis and `MinimalModel.LcFlips` for the existence of lc flips, as statements; the reduction of Theorem 8.3.5 is not formalised.

### Notes and history

The notion of pl flip and the reduction of Theorem 8.3.5 are Shokurov's (Sho92), who also proved special termination for 3-folds; the reduction is explained in Cor07, and Fujino extended special termination and the reduction to all dimensions (Fuj11). Theorem 8.3.4 is the elementary starting point of the method: it turns a question about a flip in dimension $n$ into a question about an algebra of sections on a variety of dimension $n - 1$. Hacon and McKernan proved the finite generation of the restricted algebra in all dimensions by an extension theorem for sections, which together with BCHM10 gives klt flips in every dimension.
