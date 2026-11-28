---
title: Finiteness of models and the geography of models
nodes: [MM8GY5VB02]
sources: [BCHM10, Cor07, HK10, KM98]
reads_with: [BCHM10:7, Cor07:6]
requires: [1.3, 1.5, 7.4]
level: advanced
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Finiteness of models and the geography of models

### Statement

Keep the notation of the previous section: $X$ is a normal projective variety, $S_1, \ldots, S_k$ are prime divisors on $X$, $V \subseteq \operatorname{WDiv}_{\mathbb{R}}(S)$ is an affine subspace defined over the rationals, and $A$ is a general ample $\mathbb{Q}$-divisor, so that every $\Delta \in \mathcal{L}_A(V)$ has the form $A + B$ with $B \ge 0$ and is big.

**Theorem 9.4.9 (finiteness of models, BCHM Theorem E).** Let $\mathcal{C} \subseteq \mathcal{L}_A(V)$ be a rational polytope such that $(X, \Delta)$ is klt for every $\Delta \in \mathcal{C}$. Then there are finitely many birational contractions $\varphi_j \colon X \dashrightarrow Y_j$, $1 \le j \le l$, with the following property. If $\Delta \in \mathcal{C}$ and $\psi \colon X \dashrightarrow Y$ is a log terminal model of $(X, \Delta)$, then there are an index $j$ and an isomorphism $\xi \colon Y_j \to Y$ with $\psi = \xi \circ \varphi_j$.

Node: MM8GY5VB02 · Lean: `MinimalModel.FinitenessOfModels`

**Theorem 9.4.10 (the geography of models).** In the setting of Theorem 9.4.9 suppose in addition that $X$ is $\mathbb{Q}$-factorial, and discard the $\varphi_j$ that are not log terminal models of any $(X, \Delta)$ with $\Delta \in \mathcal{C}$. Put $\mathcal{C}_{\mathrm{psef}} = \{ \Delta \in \mathcal{C} : K_X + \Delta \text{ is pseudo-effective} \}$. Then:

1. each $\mathcal{W}_{\varphi_j}(\mathcal{C})$ is a rational polytope;
2. $\mathcal{C}_{\mathrm{psef}} = \bigcup_{j = 1}^{l} \mathcal{W}_{\varphi_j}(\mathcal{C})$;
3. $\mathcal{C}_{\mathrm{psef}}$ is a rational polytope.

Lean: not yet in Lean.

### Proof in words

Theorem 9.4.9 is cited from BCHM, where it is one step of the induction mapped in Chapter 1: in dimension $n$ it is deduced from the existence of log terminal models and from nonvanishing in dimension $n$. The deduction is local on the compact polytope $\mathcal{C}$. Near a point $\Delta_0$ with $K_X + \Delta_0$ pseudo-effective, fix a log terminal model $\varphi_0 \colon X \dashrightarrow Y_0$ and the ample model $Y_0 \to Z_0$ of $K_{Y_0} + \varphi_{0*}\Delta_0$, which exists because $K_{Y_0} + \varphi_{0*} \Delta_0$ is nef and, by the base point free theorem with nonvanishing, semiample. For $\Delta$ close to $\Delta_0$ the divisor $K_{Y_0} + \varphi_{0*}\Delta$ is close to the pullback of an ample divisor on $Z_0$, so any further program it requires runs over $Z_0$, and over $Z_0$ the divisor $K_{Y_0} + \varphi_{0*} \Delta_0$ is numerically trivial. Rescaling the difference $\Delta - \Delta_0$ reduces the problem over $Z_0$ to a polytope of smaller dimension, where induction applies. Compactness then gives finitely many models. This outline is given only as an outline.

The geography is a formal consequence. A weak log canonical model forces $K_X + \Delta$ to be pseudo-effective, by Lemma 9.4.4. Conversely, a big klt boundary with pseudo-effective log canonical divisor has a log terminal model by BCHM, and Theorem 9.4.9 says it is one of the $\varphi_j$. Each piece is a rational polytope by Proposition 9.4.6, and a finite union of polytopes that is convex is the convex hull of their vertices.

### Examples

**Example 9.4.11 (the geography of $\mathbb{F}_1$).** Keep the notation of Example 9.4.8: $X = \mathbb{F}_1$, $A = \frac{1}{2} A''$ with $A''$ general in $|6L - 3E|$, $V$ the span of $E$ and the fixed fibre $F$, and $\mathcal{C} = \{ \Delta_{s,u} = A + sE + uF : (s, u) \in [0, \frac{3}{4}]^2 \}$, with
$$K_X + \Delta_{s, u} \equiv uL - y E, \qquad y = \tfrac{1}{2} - s + u.$$
On $\mathbb{F}_1$ numerical and linear equivalence of $\mathbb{R}$-divisors agree, since $\operatorname{Pic} \mathbb{F}_1 = \mathbb{Z} L \oplus \mathbb{Z} E$ has no torsion and $H^1(\mathcal{O}) = 0$.

*Pseudo-effective locus.* By Example 1.3.22 the pseudo-effective cone of $\mathbb{F}_1$ is spanned by $E$ and $F \equiv L - E$. Writing $uL - yE = u(L - E) + (u - y) E$ with $u - y = s - \frac{1}{2}$, the class is pseudo-effective if and only if $s \ge \frac{1}{2}$. So $\mathcal{C}_{\mathrm{psef}} = [\frac{1}{2}, \frac{3}{4}] \times [0, \frac{3}{4}]$. For $s < \frac{1}{2}$ the fibration $\mathbb{F}_1 \to \mathbb{P}^1$ is a Mori fibre space for $K_X + \Delta_{s,u}$, since $(K_X + \Delta_{s,u}) \cdot F = s - \frac{1}{2} < 0$.

*The two models.* The identity is a weak log canonical model exactly on $\mathcal{N}(\mathcal{C})$, the quadrilateral $\{ s \ge \frac{1}{2}, \ u \ge s - \frac{1}{2} \}$ of Example 9.4.8. Let $\varphi \colon \mathbb{F}_1 \to \mathbb{P}^2$ be the blow-down and $\Gamma = \varphi_* \Delta_{s,u}$. Then $K_{\mathbb{P}^2} + \Gamma \equiv u \ell$ with $\ell$ a line, which is nef because $u \ge 0$, and
$$K_X + \Delta_{s, u} = \varphi^*(K_{\mathbb{P}^2} + \Gamma) - yE,$$
since both sides have the same class and $\varphi^* \varphi_*$ changes only the coefficient of $E$. The comparison divisor of Lemma 9.4.4 is $-yE$, so $\varphi$ is a weak log canonical model if and only if $y \le 0$, that is $u \le s - \frac{1}{2}$, and a log terminal model if and only if $u < s - \frac{1}{2}$. So $\mathcal{W}_\varphi(\mathcal{C})$ is the triangle with vertices $(\frac{1}{2}, 0)$, $(\frac{3}{4}, 0)$ and $(\frac{3}{4}, \frac{1}{4})$. The two polytopes $\mathcal{W}_{\mathrm{id}}(\mathcal{C})$ and $\mathcal{W}_\varphi(\mathcal{C})$ are rational, meet along the segment $u = s - \frac{1}{2}$, and their union is the rectangle $\mathcal{C}_{\mathrm{psef}}$, as Theorem 9.4.10 predicts. On the segment both maps are weak log canonical models, and only the identity is a log terminal model.

*Ample models.* If $s > \frac{1}{2}$ and $u > s - \frac{1}{2}$, then $u > y > 0$ and $K_X + \Delta_{s,u}$ is ample, with ample model $\mathbb{F}_1$ itself. If $s = \frac{1}{2}$ and $u > 0$, then $K_X + \Delta_{s, u} \equiv uF$ and the ample model is the fibration to $\mathbb{P}^1$. If $0 < u \le s - \frac{1}{2}$, the ample model is $\varphi$, with $H = u \ell$ ample on $\mathbb{P}^2$. If $u = 0$ and $s \ge \frac{1}{2}$, then $K_X + \Delta_{s,0} \equiv (s - \frac{1}{2}) E$ has Iitaka dimension $0$ (or is trivial at $s = \frac{1}{2}$), and the ample model is a point. So $\mathcal{C}_{\mathrm{psef}}$ is cut into four pieces by its ample models, with the open chambers $\{ u > s - \frac{1}{2} \}$ and $\{ u < s - \frac{1}{2} \}$ of the two log terminal models.

### Proof

*Proof of Theorem 9.4.9.* This is Theorem E of BCHM, proved there for a projective morphism $X \to U$ and with $\mathcal{C}$ any compact subset of $\mathcal{L}_A(V)$ consisting of klt boundaries; the statement above is the case $U = \operatorname{Spec} k$ with $\mathcal{C}$ a rational polytope. It is cited. $\square$

*Proof of Theorem 9.4.10.* Each $Y_j$ is $\mathbb{Q}$-factorial, since $\varphi_j$ is a log terminal model of some pair. Each $(X, \Delta)$ with $\Delta \in \mathcal{C}$ is klt and $\mathcal{C}$ is a rational polytope, so part 1 is Proposition 9.4.6.

For part 2, if $\Delta \in \mathcal{W}_{\varphi_j}(\mathcal{C})$, then $\varphi_j$ is a weak log canonical model of $(X, \Delta)$ and $K_X + \Delta$ is pseudo-effective by Lemma 9.4.4, part 4. Conversely let $\Delta \in \mathcal{C}_{\mathrm{psef}}$. Then $\Delta = A + B$ with $A$ ample and $B \ge 0$, so $\Delta$ is big, $(X, \Delta)$ is klt and $K_X + \Delta$ is pseudo-effective. By BCHM, Theorem 1.2, the pair $(X, \Delta)$ has a log terminal model $\psi \colon X \dashrightarrow Y$. By Theorem 9.4.9 there are $j$ and an isomorphism $\xi \colon Y_j \to Y$ with $\psi = \xi \circ \varphi_j$. The conditions of Definition 9.4.3 are invariant under composing with an isomorphism of the target, so $\varphi_j$ is a log terminal model, in particular a weak log canonical model, of $(X, \Delta)$, and $\Delta \in \mathcal{W}_{\varphi_j}(\mathcal{C})$.

For part 3, the pseudo-effective cone is a convex cone and $\Delta \mapsto K_X + \Delta$ is affine, so $\mathcal{C}_{\mathrm{psef}}$ is convex. Let $Q$ be the finite set of vertices of the rational polytopes $\mathcal{W}_{\varphi_j}(\mathcal{C})$. By part 2 and convexity, $\operatorname{conv}(Q) \subseteq \mathcal{C}_{\mathrm{psef}} = \bigcup_j \mathcal{W}_{\varphi_j}(\mathcal{C}) \subseteq \operatorname{conv}(Q)$. So $\mathcal{C}_{\mathrm{psef}} = \operatorname{conv}(Q)$ is a rational polytope. $\square$

### Exercises

1. (B) In Example 9.4.11 replace the coefficient $\frac{1}{2}$ of $A''$ by a parameter $c \in [\frac{1}{3}, \frac{2}{3}]$, treated as a third coordinate of the polytope. Compute the three-dimensional polytopes $\mathcal{W}_{\mathrm{id}}$ and $\mathcal{W}_\varphi$ in the coordinates $(c, s, u)$, and check part 3 of Theorem 9.4.10.
2. (B) On $\mathbb{F}_2$ with $A$ a general ample $\mathbb{Q}$-divisor and $V$ spanned by $C_-$ and a fibre, choose a square of boundaries meeting both the nef chamber and the chamber where $C_-$ is contracted, and compute the geography. Identify the ample model that is singular.
3. (B) Show that a finite union of convex polytopes that is convex equals the convex hull of the union of their vertex sets, and that it need not be the union of only those pieces that are full-dimensional.
4. (B) Give an example of a klt pair $(X, \Delta)$ on a smooth projective 3-fold with two non-isomorphic log terminal models, and explain why Theorem 9.4.9 still allows only finitely many.
5. (C) Show that for every $\Delta \in \mathcal{C}_{\mathrm{psef}}$ in Theorem 9.4.10 the divisor $K_X + \Delta$ has an ample model. Hint: on a log terminal model $(Y, \Gamma)$ the boundary $\Gamma$ is big; write $\Gamma \sim_{\mathbb{R}} \varepsilon H + \Gamma'$ with $H$ ample and $(Y, \Gamma')$ klt, reduce to rational coefficients with Theorem 9.4.5, and apply the base point free theorem of Volume 7.
6. (C) Prove that in the setting of Theorem 9.4.10, the set of $\Delta \in \mathcal{C}_{\mathrm{psef}}$ whose ample model is a fixed rational map $\psi \colon X \dashrightarrow Z$ is a finite union of relatively open rational polytopes, using Theorem 9.4.10 and Proposition 9.4.6 for the log terminal models.

### Lean

`MinimalModel.FinitenessOfModels` in the project library states Theorem 9.4.9 for klt boundaries in $\mathcal{L}_A(V)$, as a statement without proof. The geography of Theorem 9.4.10 is not formalised.

### Notes and history

Finiteness of models is Theorem E of Birkar, Cascini, Hacon and McKernan (BCHM10); the local argument near a fixed boundary, with the ample model and induction on the dimension of the polytope, is the heart of their Section 7. The picture of the pseudo-effective cone decomposed into chambers of log terminal models and ample models goes back to Shokurov's geography of log models, and the language of Mori chambers is that of Hu and Keel, treated in Chapter 6. Hacon and Kovács (HK10) and Corti (Cor07) give expositions of the induction.
