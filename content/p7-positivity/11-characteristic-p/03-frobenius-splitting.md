---
title: Frobenius splitting
nodes: []
sources: [MR85, BK05, CLS11, Har77]
reads_with: [BK05:1, MR85:1]
requires: [P4.2, P4.4, P4.7, P4.9, P8.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Frobenius splitting

### Statement

Throughout, $k$ is algebraically closed of characteristic $p > 0$ and $X$ is a variety over $k$. The *absolute Frobenius* $F \colon X \to X$ is the identity on the underlying space and $f \mapsto f^p$ on $\mathcal{O}_X$. It is finite, since $k$ is perfect and $X$ is of finite type, so $F_* \mathcal{O}_X$ is a coherent $\mathcal{O}_X$-module, with $f \cdot g = f^p g$. For a line bundle $L$, $F^* L \cong L^p$, since $F$ raises the transition functions to the $p$-th power.

**Definition P7.11.15 (Frobenius splitting).** A *Frobenius splitting* of $X$ is an $\mathcal{O}_X$-linear map $\varphi \colon F_* \mathcal{O}_X \to \mathcal{O}_X$ with $\varphi(1) = 1$, that is, an additive map on local sections with $\varphi(f^p g) = f \varphi(g)$ and $\varphi(1) = 1$. It is a splitting of the map $F^\# \colon \mathcal{O}_X \to F_* \mathcal{O}_X$, $f \mapsto f^p$. The variety $X$ is *Frobenius split*, or *F-split*, if it has a Frobenius splitting.

**Lemma P7.11.16 (injectivity of Frobenius).** Let $X$ be F-split and $L$ a line bundle on $X$. Then the map $H^i(X, L) \to H^i(X, L^p)$ induced by $F$ is injective for every $i$, and so is $H^i(X, L) \to H^i(X, L^{p^N})$ for every $N \geq 1$.

Lean: not in Lean as stated.

**Theorem P7.11.17 (vanishing on F-split varieties).** Let $X$ be an F-split projective variety and $L$ an ample line bundle on $X$.

1. $H^i(X, L) = 0$ for $i > 0$.
2. If $X$ is smooth of dimension $d$, then $H^i(X, L^{-1}) = 0$ for $i < d$ and $H^i(X, \omega_X \otimes L) = 0$ for $i > 0$. So Kodaira vanishing holds on $X$.

Lean: not in Lean as stated.

**Proposition P7.11.18 (toric varieties are F-split).** Let $X_\Sigma$ be the toric variety of a fan $\Sigma$ in $N_\mathbb{R}$, with character lattice $M$. There is a unique additive map $\varphi \colon k[M] \to k[M]$ with
$$\varphi(c \chi^m) = c^{1/p} \chi^{m/p} \text{ if } m \in pM, \qquad \varphi(c \chi^m) = 0 \text{ if } m \notin pM,$$
for $c \in k$, and it maps $k[S_\sigma]$ into itself for every $\sigma \in \Sigma$. The restrictions glue to a Frobenius splitting of $X_\Sigma$.

Lean: not in Lean as stated.

**Proposition P7.11.19 (F-split curves).** Let $C$ be a smooth projective curve of genus $g$.

1. $\mathbb{P}^1$ is F-split.
2. If $g \geq 2$, then $C$ is not F-split.
3. If $g = 1$ and $C$ is F-split, then $F^* \colon H^1(C, \mathcal{O}_C) \to H^1(C, \mathcal{O}_C)$ is nonzero, that is, $C$ is ordinary in the sense of Hartshorne, Section IV.4 (Har77). Conversely, an ordinary elliptic curve is F-split (black box).

Lean: not in Lean as stated.

### Proof in words

A Frobenius splitting makes $\mathcal{O}_X$ a direct summand of $F_* \mathcal{O}_X$, and after twisting by a line bundle, $L$ a direct summand of $F_* L^p$. So Frobenius is injective on cohomology, and iterating, the cohomology of $L$ embeds into the cohomology of $L^{p^N}$. For $L$ ample this vanishes in positive degree for $N$ large, by Serre vanishing, and for $L^{-1}$ on a smooth variety it vanishes in degree below the dimension, by Serre duality. This is the Frobenius iteration of Section 11.2 without the de Rham complex.

On a toric variety the splitting is explicit: keep the monomials whose exponent is divisible by $p$, take their $p$-th roots, and kill the others. On a curve of genus at least $2$, Frobenius kills the class of $H^1(\omega_C)$, since $H^1(\omega_C^p) = 0$, so there is no splitting; on an elliptic curve the splitting is detected by Frobenius on $H^1(\mathcal{O})$.

### Examples

**Example P7.11.20 (projective space and smooth toric varieties).** By Proposition P7.11.18, $\mathbb{P}^n$, the Hirzebruch surfaces and every smooth projective toric variety are F-split, so Theorem P7.11.17 gives Kodaira vanishing on them in every characteristic. For $\mathbb{P}^n$ and $L = \mathcal{O}(1)$ the splitting is the map with $\varphi(x_1^{a_1} \cdots x_n^{a_n}) = x_1^{a_1/p} \cdots x_n^{a_n/p}$ if $p$ divides every $a_i$ and $0$ otherwise, on each standard chart $\mathbb{A}^n$, and the conclusion agrees with the computation of Theorem P4.2.1.

**Example P7.11.21 (an elliptic curve that is F-split for half of the primes).** Let $p$ be odd and $E \subset \mathbb{P}^2$ the elliptic curve $y^2 = x^3 - x$. By Hartshorne, Section IV.4 (Har77), $E$ is ordinary if and only if the coefficient of $x^{p-1}$ in $(x^3 - x)^{(p-1)/2}$ is nonzero. Now $(x^3 - x)^{(p-1)/2} = x^{(p-1)/2} (x^2 - 1)^{(p-1)/2}$, and $x^{p-1}$ appears only from $x^{2j}$ in $(x^2 - 1)^{(p-1)/2}$ with $2j = (p-1)/2$. If $p \equiv 3 \pmod 4$, then $(p-1)/2$ is odd and there is no such $j$, so $E$ is supersingular and, by Proposition P7.11.19, not F-split. If $p \equiv 1 \pmod 4$, the coefficient is $\pm \binom{(p-1)/2}{(p-1)/4}$, nonzero mod $p$ since $(p-1)/2 < p$, so $E$ is ordinary and F-split. For $p = 3$, $(x^3 - x)^1$ has coefficient $0$ at $x^2$; for $p = 5$, $(x^3 - x)^2 = x^6 - 2x^4 + x^2$ has coefficient $-2 \neq 0$ at $x^4$.

**Example P7.11.22 (Raynaud's surface is not F-split).** The surface $X$ of Theorem P7.11.4 is smooth and projective and carries an ample $\mathcal{L}$ with $H^1(X, \mathcal{L}^{-1}) \neq 0$. By Theorem P7.11.17, part 2, $X$ is not F-split. The base of its fibration is a Tango curve $C$, and $2g - 2 = \deg \operatorname{div}(df) = p \deg D > 0$ by Definition P7.11.1, so $C$ has genus at least $2$ and is not F-split by Proposition P7.11.19 either.

### Proof

*Lemma P7.11.16.* Tensor $F^\# \colon \mathcal{O}_X \to F_* \mathcal{O}_X$ and its splitting $\varphi$ with $L$. By the projection formula, $L \otimes F_* \mathcal{O}_X \cong F_* F^* L \cong F_* L^p$, so $L \to F_* L^p$ is split by $1 \otimes \varphi$, and $H^i(X, L) \to H^i(X, F_* L^p)$ is split injective. Since $F$ is affine, $H^i(X, F_* L^p) = H^i(X, L^p)$ by Corollary P4.4.3, and the composite is the map induced by $F$. Applying this to $L^p, L^{p^2}, \dots$ and composing gives the second statement.

*Theorem P7.11.17.* Let $L^r$ be very ample, giving $X \subseteq \mathbb{P}^s$ with $L^r = \mathcal{O}(1)|_X$. By Theorem P4.2.7 applied to the finitely many sheaves $L^t$, $0 \leq t < r$, there is $m_0$ with $H^i(X, L^m) = 0$ for $i > 0$ and $m \geq m_0$. By Lemma P7.11.16, $H^i(X, L) \hookrightarrow H^i(X, L^{p^N})$, which is $0$ for $p^N \geq m_0$. This is part 1. For part 2, Lemma P7.11.16 for $L^{-1}$ gives $H^i(X, L^{-1}) \hookrightarrow H^i(X, L^{-p^N})$, and by Corollary P4.7.21, $H^i(X, L^{-p^N}) \cong H^{d - i}(X, \omega_X \otimes L^{p^N})'$. For $i < d$ this is $0$ for $N$ large, by Theorem P4.2.7 applied to the sheaves $\omega_X \otimes L^t$, $0 \leq t < r$. The statement for $\omega_X \otimes L$ is the dual one, $H^i(X, \omega_X \otimes L) \cong H^{d - i}(X, L^{-1})'$, again by Corollary P4.7.21.

*Proposition P7.11.18.* The map is well defined on the basis $\chi^m$, $m \in M$, extended additively, and $c \mapsto c^{1/p}$ is defined since $k$ is perfect. For $f = a \chi^u$ and $g = c \chi^m$, $f^p g = a^p c \chi^{pu + m}$, and $pu + m \in pM$ if and only if $m \in pM$, in which case $\varphi(f^p g) = a c^{1/p} \chi^{u + m/p} = f \varphi(g)$; otherwise both sides are $0$. By additivity in $f$ and $g$, $\varphi(f^p g) = f \varphi(g)$ for all $f, g \in k[M]$, and $\varphi(1) = 1$. If $m \in S_\sigma = \sigma^\vee \cap M$ and $m = p m'$ with $m' \in M$, then $m' = m/p \in \sigma^\vee$ since $\sigma^\vee$ is a cone, so $m' \in S_\sigma$; hence $\varphi(k[S_\sigma]) \subseteq k[S_\sigma]$, and the restriction $\varphi_\sigma$ is a Frobenius splitting of $U_\sigma$ (Proposition P8.6.13). For $\tau = \sigma \cap \sigma'$ the open subsets $U_\tau \subseteq U_\sigma$ and $U_\tau \subseteq U_{\sigma'}$ correspond to the inclusions $k[S_\sigma] \subseteq k[S_\tau] \supseteq k[S_{\sigma'}]$ inside $k[M]$ (Theorem P8.6.15), and $\varphi_\sigma$, $\varphi_\tau$ and $\varphi_{\sigma'}$ are restrictions of the same map $\varphi$ of $k[M]$. So the $\varphi_\sigma$ agree on overlaps and glue to a map $F_* \mathcal{O}_{X_\Sigma} \to \mathcal{O}_{X_\Sigma}$, which is a Frobenius splitting since it is one on each $U_\sigma$.

*Proposition P7.11.19.* Part 1 is Proposition P7.11.18 for the fan of $\mathbb{P}^1$ of Example P8.6.18. For part 2, suppose $C$ is F-split. By Lemma P7.11.16 with $L = \omega_C$, $H^1(C, \omega_C) \hookrightarrow H^1(C, \omega_C^p)$. By Corollary P4.7.21, $H^1(C, \omega_C) \cong H^0(C, \mathcal{O}_C)' = k$ and $H^1(C, \omega_C^p) \cong H^0(C, \omega_C^{1-p})'$, which is $0$ since $\deg \omega_C^{1-p} = (1 - p)(2g - 2) < 0$ for $g \geq 2$. This is a contradiction. For part 3, Lemma P7.11.16 with $L = \mathcal{O}_C$ shows that $F^*$ is injective on $H^1(C, \mathcal{O}_C) \cong k$, hence nonzero. The converse is in Brion and Kumar, Chapter 1 (BK05), where $\operatorname{Hom}(F_* \mathcal{O}_C, \mathcal{O}_C)$ is identified, through duality for the finite morphism $F$ (compare Corollary P4.9.14), with $H^0(C, \omega_C^{1-p}) \cong k$, and evaluation at $1$ is shown to be dual to $F^*$ on $H^1(C, \mathcal{O}_C)$; it is a black box here.

### Exercises

1. (A) Show that an F-split variety is reduced: if $f^p = 0$, then $f = \varphi(f^p) = 0$.
2. (A) For $\mathbb{A}^1 = \operatorname{Spec} k[x]$, check directly that the map of Proposition P7.11.18 satisfies $\varphi(f^p g) = f \varphi(g)$, and find a second Frobenius splitting of $\mathbb{A}^1$.
3. (B) Show that an open subset of an F-split variety is F-split, and that a product of two F-split varieties is F-split.
4. (B) Let $X = \operatorname{Spec} R$ be affine. Show that $X$ is F-split if and only if the evaluation map $\operatorname{Hom}_R(F_* R, R) \to R$, $\varphi \mapsto \varphi(1)$, is surjective.
5. (B) Use Corollary P4.9.14 to identify $\operatorname{Hom}(F_* \mathcal{O}_C, \mathcal{O}_C)$ with $H^0(C, \omega_C^{1-p})$ for a smooth projective curve $C$, and give a second proof of Proposition P7.11.19, part 2. Compute the dimension of this space for $C = \mathbb{P}^1$.
6. (C) Let $X$ be an F-split projective variety that is Cohen-Macaulay of dimension $d$, with dualizing sheaf $\omega_X$. Prove that $H^i(X, L^{-1}) = 0$ for $i < d$ and $L$ ample, using Serre duality for Cohen-Macaulay projective schemes in place of Corollary P4.7.21.

### Lean

The project library has no statements in characteristic $p$: no Frobenius splitting and no vanishing in positive characteristic. The toric side has `MinimalModel.Toric.Fan.canonical`, which is about the canonical divisor of a fan and does not involve the base field. The handbook adds no `MinimalModel` node here.

### Notes and history

Frobenius splitting was introduced by Mehta and Ramanathan in 1985 (MR85), who proved that Schubert varieties are F-split and deduced vanishing theorems for them. The literature state is theorem. Brion and Kumar (BK05) give the systematic account, including the toric case, flag varieties and the criterion for curves. Monomial maps of the same kind, with $p$ replaced by an integer $\ell \geq 2$, are used in Cox, Little and Schenck (CLS11) to prove Demazure vanishing on toric varieties. The singular analogues, F-pure and strongly F-regular singularities, and the test ideal, which plays the role of the multiplier ideal of Chapter 10, are the starting point of the minimal model program in positive characteristic; they are outside this volume.
