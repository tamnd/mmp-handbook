---
title: Existence of pl flips
nodes: [MMP51FQ005]
sources: [HM07, Cor07, BCHM10, Sho92, Sho04]
reads_with: [HM07:5, Cor07:2, BCHM10:5]
requires: [4.2, 4.5, 5.5, 8.1, 8.3]
level: advanced
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Existence of pl flips

### Statement

This section proves the first arrow of Theorem 9.1.10: finite generation in dimension $n - 1$, Theorem 9.1.9, gives pl flips in dimension $n$, Theorem 9.1.4. With Lemma 9.2.2, the restricted algebra of $K_X + S + B$ must be shown finitely generated, and with Corollary 9.2.9 that algebra is an adjoint algebra on $S$ once two technical points are settled: the pair must be moved to a log resolution with an ample part in the boundary, and the boundary $\Theta$ of the extension theorem must be rational. The first is proved below; the second is where the full strength of $F_{n-1}$ is used, and its proof is outlined.

**Lemma 9.2.13 (restricted algebras on a log resolution).** Let $(X, S + B)$ be a $\mathbb{Q}$-factorial plt pair, projective over an affine variety $Z$, with $S$ prime and $\lfloor B \rfloor = 0$, and let $g \colon Y \to X$ be a log resolution of $(X, S + B)$ with strict transform $S_Y$ of $S$. Write
$$K_Y + S_Y + g^{-1}_* B = g^*(K_X + S + B) + \sum_i a_i E_i$$
with $E_i$ the exceptional prime divisors, and put $\Delta_Y = S_Y + g^{-1}_* B + \sum_{a_i < 0} (-a_i) E_i$ and $E = \sum_{a_i > 0} a_i E_i$. Then $\lfloor \Delta_Y - S_Y \rfloor = 0$, $K_Y + \Delta_Y = g^*(K_X + S + B) + E$, and for every $m$ with $m(K_X + S + B)$ Cartier, pullback by $g$ is an isomorphism
$$H^0(X, \mathcal{O}_X(m(K_X + S + B))) \cong H^0(Y, \mathcal{O}_Y(m(K_Y + \Delta_Y)))$$
compatible with restriction to $S$ and $S_Y$. So for $k$ with $k(K_X + S + B)$ Cartier the restricted algebras $\operatorname{res}_S R(X, k(K_X + S + B))$ and $\operatorname{res}_{S_Y} R(Y, k(K_Y + \Delta_Y))$ are isomorphic.

Lean: not yet in Lean.

**Theorem 9.2.14 (Hacon and McKernan, $F_{n-1} \Rightarrow A_n$).** Let $n \ge 2$ and suppose Theorem 9.1.9 holds in dimension $n - 1$. Then Theorem 9.1.4 holds in dimension $n$: every pl flipping contraction $f \colon X \to Z$ of an $n$-dimensional pair $(X, S + B)$ has a flip.

Lean: not yet in Lean.

**Corollary 9.2.15 (pl flips in dimension 3 again).** Pl flips exist in dimension $3$, and so klt flips exist in dimension $3$.

Lean: not yet in Lean.

### Proof in words

The pl flip exists if the restricted algebra of $K_X + S + B$ is finitely generated. Pass to a log resolution: the restricted algebra does not change, because the exceptional divisors with positive discrepancy contribute fixed components that carry no sections. On the resolution the boundary has simple normal crossings, and after a perturbation that does not change the algebra up to a Veronese subalgebra it has the form $S + A + B$ with $A$ general and ample over $Z$, as the extension theorem requires. The extension theorem identifies the restricted algebra with the adjoint algebra of $K_S + \Theta$, where $\Theta$ is defined by an asymptotic limit and so is a priori only real. Finite generation in dimension $n - 1$ is used twice: its parts 2 and 3, on the stable base loci of nearby boundaries, show that the limit is attained and $\Theta$ is rational, and its part 1 shows that the adjoint algebra of the klt pair $(S, \Theta)$, which has an ample part, is finitely generated.

### Examples

**Example 9.2.16 (the 4-fold flip through the theorem).** In Example 9.2.4 the pair is $(X^-, S)$ with $B = 0$, so $\Omega = 0$ and $\Theta = 0$ whatever $F$ is, and the theorem predicts that the restricted algebra of $K_{X^-} + S$ is the adjoint algebra $R(S / \mathbb{A}^3, K_S)$ in large divisible degrees. Both sides were computed: the class group of $X^-$ is $\mathbb{Z}$ through $D \mapsto D \cdot C^-$, so $K_{X^-} + S \sim 2S$, and the degree $j$ part of $\operatorname{res}_S R(X^-, K_{X^-} + S)$ is $(R_S)_{2j} \cong k[x, y, z]$, while $H^0(S, \mathcal{O}_S(jK_S)) = H^0(S, \mathcal{O}_S(2jE)) = k[x, y, z]$ because $E$ is exceptional over $\mathbb{A}^3$. So the two algebras agree in every degree, both are $k[x, y, z][t]$, and their Proj over $\mathbb{A}^3$ is $\mathbb{A}^3 = S^+$, the log canonical model of $K_S$ over $\mathbb{A}^3$. The flip restricts on $S$ to the log canonical model of the pair $(S, \Theta)$, which is the general pattern.

**Example 9.2.17 (the Francia flip through the theorem).** In Example 9.2.5, $B = 0$ and $\Theta$ is $0$ up to the perturbation in step 2 of the proof below. The adjoint algebra is $R(S / \mathbb{A}^2, K_S)$ with $K_S = 2C^-$, which in each degree $m$ with $mK_S$ Cartier is $H^0(S, \mathcal{O}_S(2mC^-)) = k[x, y]$; it is finitely generated, and its Proj over $\mathbb{A}^2$ is $\mathbb{A}^2 = S^+$. Here finite generation in dimension $2$ is elementary, as the divisor is exceptional, and Theorem 9.2.14 gives the Francia flip without the complements of Volume 8.

### Proof

*Lemma 9.2.13.* Since $(X, S + B)$ is plt and the $E_i$ are exceptional, $a_i > -1$ for every $i$, so the coefficients $-a_i$ of $\Delta_Y - S_Y - g^{-1}_* B$ lie in $(0, 1)$; with $\lfloor B \rfloor = 0$ this gives $\lfloor \Delta_Y - S_Y \rfloor = 0$. The formula $K_Y + \Delta_Y = g^*(K_X + S + B) + E$ is the definition rearranged. Let $M = m(K_X + S + B)$, a Cartier divisor. Then $m(K_Y + \Delta_Y) = g^* M + mE$ with $mE \ge 0$ exceptional, and $g_* \mathcal{O}_Y(g^* M + mE) = \mathcal{O}_X(M)$: a rational function $\phi$ with $\operatorname{div} \phi + g^*M + mE \ge 0$ on $g^{-1}(U)$ has $\operatorname{div} \phi + M \ge 0$ on $U$ outside a set of codimension at least $2$, which suffices on the normal variety $X$, and the converse holds because $mE \ge 0$. So pullback is an isomorphism on global sections. A section of $\mathcal{O}_X(M)$ given by $\phi$ restricts on $S$ to the restriction of $\phi$ times a local generator, and on $S_Y$ to the restriction of $g^* \phi$ times the pulled back generator; as $S_Y$ is not a component of $E$ and $g|_{S_Y} \colon S_Y \to S$ is birational, these restrictions correspond under the isomorphism of function fields $k(S) \cong k(S_Y)$. So the restriction maps commute with the isomorphism, and their images, the graded pieces of the two restricted algebras, are identified compatibly with products.

*Theorem 9.2.14.* This is an outline, following HM07 and Cor07, Chapters 2 and 4; the steps are proved where they are short.

1. *Reduction to the restricted algebra.* The question is local over $Z$, so take $Z$ affine. By part 3 of Lemma 9.2.2 it is enough to show that $\operatorname{res}_S R(X, k(K_X + S + B))$ is finitely generated for some $k$ with $k(K_X + S + B)$ Cartier.
2. *An ample part.* As $f$ is birational, every divisor on $X$ is big over $Z$, so by Kodaira's lemma over a base, Lemma 5.1.9, $B \sim_{\mathbb{Q}, Z} A + B''$ with $A$ ample over $Z$ and $B'' \ge 0$. For small rational $\varepsilon > 0$ the divisor $B_\varepsilon = (1 - \varepsilon) B + \varepsilon (A + B'')$ satisfies $K_X + S + B_\varepsilon \sim_{\mathbb{Q}, Z} K_X + S + B$, the pair $(X, S + B_\varepsilon)$ is plt for $A$ general, and a Veronese subalgebra of the restricted algebra is unchanged, as $Z$ is affine. On a log resolution as in Lemma 9.2.13, the pullback of $A$ is only big and nef, and a further perturbation, using that the exceptional divisors are negative over $X$, gives a boundary of the form $S_Y + A_Y + B_Y$ with $A_Y$ general and ample over $Z$ and simple normal crossing support, with the same restricted algebra up to a Veronese subalgebra. This is HM07, Section 5, and Cor07, Chapter 2.
3. *The extension theorem.* The relative form of Corollary 9.2.9 over $Z$ identifies the restricted algebra on $S_Y$ with the adjoint algebra $R(S_Y / T, r(K_{S_Y} + \Theta))$, where $T$ is the image of $S$ in $Z$, provided $\Theta$ is rational.
4. *$\Theta$ is rational.* The divisor $\Theta$ is the limit of $\Theta_m = \Omega - \Omega \wedge \frac1m F_m$. Parts 2 and 3 of Theorem 9.1.9 in dimension $n - 1$, applied to the pairs $(S_Y, \Theta_m)$ near $\Theta$ inside the polytope spanned by the components of $\Omega$, show that the stable base loci of $K_{S_Y} + \Xi$ are constant near $\Theta$ and that $\Theta$ lies in a rational polytope on which the fixed divisor is controlled; it follows that $\Theta$ is rational and $\Theta_m = \Theta$ for $m$ divisible enough. This is the step that uses the geometry of the Shokurov polytope, treated in Chapter 4, and it is not proved here.
5. *Finite generation on $S$.* The pair $(S_Y, \Theta)$ is klt, as $0 \le \Theta \le \Omega$ and $\Omega$ has simple normal crossing support with coefficients in $[0, 1)$, and $\Theta \ge A_Y|_{S_Y}$, a general ample $\mathbb{Q}$-divisor over $T$, since a general $A_Y$ shares no component with the fixed divisors. The divisor $K_{S_Y} + \Theta$ is pseudo-effective over $T$, because $|m(K_{S_Y} + \Theta)|$ is not empty for $m$ divisible enough, by Corollary 9.2.9 and $S \not\subseteq \mathbf{B}(K_X + S + B)$. The last holds because $K_X + S + B \sim_{\mathbb{Q}, Z} aS$ with $a > 0$, and for every $j \ge 1$ the coherent sheaf $\mathcal{O}_Z(jf_*S)$ on the affine variety $Z$ is generated by global sections, so some section of it generates it at the generic point of $f_* S$; as $f$ is small, its pullback is a section of $\mathcal{O}_X(jS)$ that does not vanish on $S$. Part 1 of Theorem 9.1.9 in dimension $n - 1$ gives the finite generation of $R(S_Y / T, r(K_{S_Y} + \Theta))$.
6. *Conclusion.* By steps 3 and 5 and Corollary 9.2.9 the restricted algebra on $S_Y$ is finitely generated, by Lemma 9.2.13 and step 2 so is the restricted algebra on $S$, and by step 1 the pl flip exists.

*Corollary 9.2.15.* Theorem 9.1.9 holds in dimension $2$: for surfaces it is finite generation of adjoint rings of klt surface pairs, proved by hand in Chapter 5. Theorem 9.2.14 with $n = 3$ gives pl flips in dimension $3$, which is Theorem 8.3.9, and Corollary 9.2.3 with special termination in dimension $3$, Theorem 8.4.20, gives klt flips, Theorem 8.3.10.

### Exercises

1. (A) Check the claim of Lemma 9.2.13 that $a_i > -1$ for a plt pair and an exceptional divisor $E_i$, and show by an example that some $a_i$ can be negative.
2. (A) In Example 9.2.16 show directly that $\operatorname{Proj}_{\mathbb{A}^3} R(S / \mathbb{A}^3, K_S) = \mathbb{A}^3$.
3. (B) Show that the converse of step 1 also holds in the sense of part 2 of Lemma 9.2.2, and deduce that if pl flips exist in dimension $n$ then the adjoint algebras $R(S / T, K_S + \Theta)$ that arise in step 3 are finitely generated.
4. (B) In step 2, show that $K_X + S + B_\varepsilon \sim_{\mathbb{Q}, Z} K_X + S + B$ and that $(X, S + B_\varepsilon)$ is plt for $\varepsilon$ small and $A$ general.
5. (B) Let $f \colon X \to Z$ be the pl flipping contraction of Example 9.2.4 and let $B = \frac12 D_1$. Decide whether $(X^-, D_4 + B)$ is still a pl flipping contraction, compute $\Omega$, and describe the adjoint algebra on $S$ predicted by Theorem 9.2.14.
6. (C) Prove step 4 in the case where $S_Y$ is a smooth curve, by showing that $\Theta_m$ is eventually constant.

### Lean

The library states the existence of klt flips as `MinimalModel.KltFlips`, a statement with no proof, which is the conclusion of Corollary 9.2.3 combined with Theorem 9.2.14 and Chapter 3. Pl flips and the extension theorem are not in Lean.

### Notes and history

The existence of pl flips in all dimensions, assuming finite generation in lower dimension, is the theorem of Hacon and McKernan in HM07, written up in Cor07 and incorporated in BCHM10, where it is the implication $F_{n-1} \Rightarrow A_n$. In dimension $3$ it recovers Shokurov's theorem, Sho92, and in dimension $4$ Shokurov had proved the existence of pl flips by other means in Sho04. The rationality of $\Theta$ in step 4 is the point at which the induction needs the full statement of $F_{n-1}$ about nearby boundaries and not only finite generation for a single pair; without it the extension theorem identifies the restricted algebra with an adjoint ring only for a real boundary, whose finite generation is not even well posed.
