---
title: Minimal models, non-vanishing and abundance
nodes: [MMY4HT1Q8M, MM9399B0QP, MM193HWD2S, MMZ5XGBW5M, MMPTP8SV13, MM5ECX1RGZ]
sources: [KM98, BCHM10, Kol92, Laz04, BDPP13, Bir12]
reads_with: [KM98:ch3, Laz04:ch2, Bir12:ch1]
requires: [P4, P7]
level: background
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Minimal models, non-vanishing and abundance

### Statement

**Definition 1.1.25.** Let $(X, \Delta)$ be a projective lc pair. Let $\varphi \colon X \dashrightarrow Y$ be a birational map to a projective normal variety such that $\varphi^{-1}$ contracts no divisor, and let $\Delta_Y = \varphi_* \Delta$. Then $(Y, \Delta_Y)$ is a *minimal model* of $(X, \Delta)$ if

1. $(Y, \Delta_Y)$ is lc and $K_Y + \Delta_Y$ is nef, and
2. $a(E, X, \Delta) < a(E, Y, \Delta_Y)$ for every prime divisor $E$ of $X$ that $\varphi$ contracts.

Lean: `MinimalModel.IsMinimalModel`, in the project library.

This is KM98, Definition 3.50. Condition 2 makes the minimal model a result of the program: each divisorial contraction and each flip raises the discrepancies of the divisors in the exceptional locus. Some authors also ask $Y$ to be $\mathbb{Q}$-factorial.

**Definition 1.1.26.** Let $D$ be an $\mathbb{R}$-Cartier divisor on a normal projective variety $X$. Then $D$ is *pseudo-effective* if $D + \varepsilon A$ is big for every ample $A$ and every $\varepsilon > 0$, and *$\mathbb{R}$-effective* if it is $\mathbb{R}$-linearly equivalent to an effective $\mathbb{R}$-divisor. It is *semiample* if it is $\mathbb{R}$-linearly equivalent to a nonnegative combination of Cartier divisors that have a base point free multiple. For a $\mathbb{Q}$-Cartier $D$, the *Iitaka dimension* $\kappa(X, D)$ is $-\infty$ if $H^0(X, \mathcal{O}_X(mD)) = 0$ for all $m \ge 1$, and otherwise the largest dimension of the image of the rational maps given by $|mD|$. The *Kodaira dimension* of a smooth projective $X$ is $\kappa(X) = \kappa(X, K_X)$.

Lean: `MinimalModel.IsPseudoEffective`, `MinimalModel.IsREffective` and `MinimalModel.IsSemiample`, in the project library.

A semiample divisor is nef, and an $\mathbb{R}$-effective divisor is pseudo-effective. The conjectures below say that for $K_X + \Delta$ the converse implications hold.

**Conjecture 1.1.27 (Existence of minimal models).** Let $(X, \Delta)$ be a projective lc pair of dimension $n$ with $K_X + \Delta$ pseudo-effective. Then $(X, \Delta)$ has a minimal model.

Node: MMY4HT1Q8M · Lean: `MinimalModel.MinimalModelConj`

**Theorem 1.1.28 (Birkar, Cascini, Hacon and McKernan).** Let $(X, \Delta)$ be a projective klt pair with $\Delta$ big and $K_X + \Delta$ pseudo-effective. Then $(X, \Delta)$ has a minimal model. The same holds when $K_X + \Delta$ is big.

Node: MM9399B0QP

**Theorem 1.1.29 (Finite generation).** Let $X$ be a smooth projective variety. Then the canonical ring $R(X, K_X) = \bigoplus_{m \ge 0} H^0(X, \mathcal{O}_X(mK_X))$ is a finitely generated $k$-algebra.

Node: MM193HWD2S · Lean: `MinimalModel.FiniteGenerationCanonical`

**Conjecture 1.1.30 (Non-vanishing).** Let $(X, \Delta)$ be a projective lc pair of dimension $n$ with $K_X + \Delta$ pseudo-effective. Then $K_X + \Delta$ is $\mathbb{R}$-effective.

Node: MMZ5XGBW5M · Lean: `MinimalModel.NonVanishing`

**Conjecture 1.1.31 (Abundance).** Let $(X, \Delta)$ be a projective lc pair of dimension $n$ with $K_X + \Delta$ nef. Then $K_X + \Delta$ is semiample.

Node: MMPTP8SV13 · Lean: `MinimalModel.Abundance`

**Theorem 1.1.32 (Abundance for 3-folds).** The abundance conjecture holds for $n \le 3$.

Node: MM5ECX1RGZ

The three conjectures are theorems for $n \le 3$ and open for $n \ge 4$. For a minimal model, abundance gives a morphism $Y \to Z$ by $|m(K_Y + \Delta_Y)|$, the *Iitaka fibration*, with $\dim Z = \kappa(Y, K_Y + \Delta_Y)$. So the program together with abundance would sort every variety with $\kappa \ge 0$ into a fibration with $K$ numerically trivial on the general fibre over a base of general type in the log sense.

### Proof in words

The theorem of BCHM10 is an induction on the dimension. It proves at once the existence of klt flips, the existence of minimal models for a big boundary, and the termination of the program with scaling of an ample divisor in that case. The big boundary is what makes the induction work: it gives a finite set of models through which the program can pass, and so termination with scaling holds. The finite generation of the canonical ring follows. If $X$ is of general type, a minimal model $Y$ of $X$ exists, and $K_Y$ is nef and big, so the base point free theorem makes $K_Y$ semiample and $R(X, K_X) = R(Y, K_Y)$ finitely generated. If $X$ is not of general type, a reduction of Fujino and Mori turns the question into a klt pair of general type on the base of the Iitaka fibration.

For abundance in dimension 3 the proof has two steps. The first is non-vanishing, $\kappa \ge 0$, which Miyaoka proved with the generic semipositivity of the cotangent sheaf. The second shows that the Iitaka dimension equals the numerical dimension $\nu$, the largest $d$ with $(K_X + \Delta)^d \not\equiv 0$; Kawamata showed that this equality is equivalent to abundance for a nef $K_X + \Delta$. In higher dimension both steps are open. Non-vanishing is the hard part: it would give the existence of minimal models, by a theorem of Birkar, when the program in lower dimension is known.

### Examples

Curves, computed in full. Let $C$ be a smooth projective curve of genus $g$. Then $\deg K_C = 2g - 2$. For $g = 0$, $K_C$ is not pseudo-effective, and $C = \mathbb{P}^1$ is a Mori fibre space over a point. For $g = 1$, $K_C \sim 0$ is semiample, and $\kappa(C) = 0$. For $g \ge 2$, $K_C$ is ample, and $\kappa(C) = 1$. So all three conjectures hold in dimension 1.

A product, computed in full. Let $X = C \times E$ with $g(C) \ge 2$ and $E$ an elliptic curve, and let $p \colon X \to C$ be the projection. Then $K_X = p^* K_C$, because $K_E \sim 0$. So $K_X$ is nef, $K_X^2 = 0$ and $\nu(K_X) = 1$. The sections of $mK_X$ are the pullbacks of the sections of $mK_C$, so $\kappa(X) = 1$, and $|mK_X|$ for large $m$ is free and gives the projection $p$. Here $X$ is its own minimal model, abundance holds, and the Iitaka fibration is $p$, with elliptic fibres.

A hypothesis that fails. Let $E$ be an elliptic curve and $L$ a divisor of degree 0 that is not torsion in $\operatorname{Pic}(E)$. Then $L$ is nef and pseudo-effective. No multiple $mL$ has a section, because a section of a degree 0 bundle gives $mL \sim 0$. So $L$ is not semiample and not $\mathbb{R}$-effective, and the conclusions of abundance and non-vanishing fail for $L$. The hypothesis that fails is the form of the divisor: $L = K_E + \Delta$ would need an effective $\Delta \sim L$ of degree 0, so $\Delta = 0$ and $L \sim 0$, which is false. The conjectures are about the log canonical divisor only.

### Exercises

1. (A) Let $(Y, \Delta_Y)$ be a minimal model of $(X, \Delta)$. Show that $K_X + \Delta$ is pseudo-effective, with a common resolution of $X$ and $Y$.
2. (A) Let $X = C \times E$ as in the Examples. Compute $\kappa(X)$ and $\nu(K_X)$ when $g(C) = 1$, and check abundance.
3. (A) Show that a semiample $\mathbb{R}$-divisor is nef, and that an $\mathbb{R}$-effective divisor is pseudo-effective.
4. (B) Let $(Y, \Delta_Y)$ be a minimal model of $(X, \Delta)$. Use condition 2 of the definition and a common resolution to show that $H^0(X, \mathcal{O}_X(m(K_X + \Delta))) \cong H^0(Y, \mathcal{O}_Y(m(K_Y + \Delta_Y)))$ for every $m$ with $m\Delta$ integral, and conclude that the Iitaka dimensions agree.
5. (B) Let $X$ be smooth projective with $K_X$ semiample. Show that $R(X, K_X)$ is finitely generated: first show that a Veronese subring is the section ring of an ample divisor on the image of $|mK_X|$.
6. (B) Show that the divisor $L$ of the last example is not $\mathbb{R}$-linearly equivalent to 0. Use that $\operatorname{Pic}^0(E) \otimes_{\mathbb{Z}} \mathbb{Q}$ is a $\mathbb{Q}$-vector space in which the class of $L$ is not zero.

### Lean

`MinimalModel.IsMinimalModel` follows KM98, Definition 3.50, without $\mathbb{Q}$-factoriality: the map $X \dashrightarrow Y$ is given by an isomorphism of function fields, every prime divisor of $Y$ comes from one of $X$ with the same coefficient, $K_Y + \Delta_Y$ is nef, and the contracted divisors have a smaller log discrepancy on $X$. `MinimalModel.FiniteGenerationCanonical` states finite generation for the subalgebra of $k(X)[t]$ spanned by the elements $\varphi t^m$ with $\varphi \in H^0(X, mK)$, using Mathlib's `Subalgebra.FG`. BCHM and abundance for 3-folds are nodes of the map with no Lean statement yet.

### Notes and history

The existence of minimal models for 3-folds came from Mori's flips (Mor88) and Shokurov's termination. Miyaoka and Kawamata proved abundance for terminal 3-folds around 1987 to 1992, and Keel, Matsuki and McKernan proved it for lc 3-fold pairs in 1994 (see Kol92 for the earlier steps). Birkar, Cascini, Hacon and McKernan proved the existence of minimal models for klt pairs with a big boundary and the finite generation of the canonical ring in 2010 (BCHM10). Siu gave an analytic proof of finite generation. Boucksom, Demailly, Paun and Peternell showed that $K_X$ is pseudo-effective if and only if $X$ is not uniruled (BDPP13), so a smooth projective $X$ is uniruled exactly when the program ends at a Mori fibre space. The existence of minimal models, non-vanishing and abundance are open conjectures in general in dimension 4 and higher. A 2026 preprint of Ajit (arXiv 2610.09270) constructs terminal 4-folds $X$ with $3K_X \sim 0$ and an ample Cartier divisor $D$ with $H^0(X, \mathcal{O}_X(D)) = 0$. If it is right, it refutes the effective non-vanishing conjecture of Ambro and Kawamata in dimension 4 and higher; that conjecture is a stronger statement than the non-vanishing conjecture of this section, which stays open. Volume 9 gives BCHM, Volume 10 gives abundance in dimension 3, and Volumes 16 and 17 report on dimension 4 and the open cases.
