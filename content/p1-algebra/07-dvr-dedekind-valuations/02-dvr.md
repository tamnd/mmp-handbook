---
title: Discrete valuation rings and the order of vanishing
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch9, Mat86:ch4, Eis95:ch11]
requires: [P1.1, P1.2, P1.3, P1.4, P1.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Discrete valuation rings and the order of vanishing

### Statement

**Definition P1.7.11 (discrete valuation ring).** A *discrete valuation ring*, or DVR, is the valuation ring of a discrete valuation $v: K^* \to \mathbb{Z}$ of a field $K$. An element $t$ with $v(t) = 1$ is a *uniformizer*.

Lean: Mathlib `IsDiscreteValuationRing` (class, defined as a local principal ideal domain that is not a field), with `IsDiscreteValuationRing.addVal` for the valuation.

Let $A$ be a DVR with valuation $v$ and uniformizer $t$. For $x \in K^*$ the element $u = x t^{-v(x)}$ has value $0$, so it is a unit of $A$ and $x = u t^{v(x)}$. Hence the nonzero ideals of $A$ are the $(t^n) = \{x : v(x) \geq n\}$ for $n \geq 0$: an ideal $I \neq 0$ contains an element $x$ of least value $n$, so $t^n \in I$, and every element of $I$ is a multiple of $t^n$. So $A$ is a local principal ideal domain with maximal ideal $(t)$, and its primes are $0$ and $(t)$. In particular $A$ is Noetherian of dimension $1$.

**Theorem P1.7.12 (characterization of DVRs).** Let $(A, \mathfrak{m}, k)$ be a Noetherian local domain of dimension $1$. The following are equivalent:

1. $A$ is a DVR;
2. $A$ is normal;
3. $\mathfrak{m}$ is principal;
4. $\dim_k \mathfrak{m}/\mathfrak{m}^2 = 1$;
5. every nonzero ideal of $A$ is a power of $\mathfrak{m}$;
6. there is $t \in A$ such that every nonzero ideal of $A$ is $(t^n)$ for some $n \geq 0$.

Lean: Mathlib `IsDiscreteValuationRing.TFAE` and `tfae_of_isNoetherianRing_of_isLocalRing_of_isDomain`, with the steps `maximalIdeal_isPrincipal_of_isDedekindDomain` and `exists_maximalIdeal_pow_eq_of_principal` (proved in Mathlib).

*Proof.* Two facts are used throughout. Since $\dim A = 1$ and $A$ is a domain, the primes of $A$ are $0$ and $\mathfrak{m}$. So every ideal $I \neq 0$ has $\sqrt{I} = \mathfrak{m}$, and by Proposition P1.3.21 it contains a power of $\mathfrak{m}$. Second, $\mathfrak{m}^n \neq \mathfrak{m}^{n+1}$ for all $n$: otherwise $\mathfrak{m}^n = 0$ by Nakayama's lemma (Theorem P1.1.25), which is false in a domain with $\mathfrak{m} \neq 0$.

(1) implies (2): a valuation ring is normal (Section 7.1).

(2) implies (3): let $a \in \mathfrak{m}$ be nonzero. There is $n \geq 1$ with $\mathfrak{m}^n \subseteq (a)$ and $\mathfrak{m}^{n-1} \not\subseteq (a)$. Choose $b \in \mathfrak{m}^{n-1} \setminus (a)$ and put $x = a/b \in K$. Then $x^{-1} = b/a \notin A$, since $b \notin (a)$. But $b\mathfrak{m} \subseteq \mathfrak{m}^n \subseteq (a)$, so $x^{-1}\mathfrak{m} \subseteq A$, and $x^{-1}\mathfrak{m}$ is an ideal of $A$. If $x^{-1}\mathfrak{m} \subseteq \mathfrak{m}$, then $\mathfrak{m}$ is a faithful $A[x^{-1}]$-module that is finitely generated over $A$, so $x^{-1}$ is integral over $A$ by Proposition P1.4.2, and $x^{-1} \in A$ by normality, a contradiction. Hence $x^{-1}\mathfrak{m} = A$, that is $\mathfrak{m} = xA$, and $x = x \cdot 1 \in \mathfrak{m}$.

(3) implies (4): if $\mathfrak{m} = (t)$, then $\mathfrak{m}/\mathfrak{m}^2$ is spanned by the class of $t$, and it is nonzero since $\mathfrak{m} \neq \mathfrak{m}^2$.

(4) implies (5) and (6): by Proposition P1.1.26, $\mathfrak{m} = (t)$ for any $t \in \mathfrak{m} \setminus \mathfrak{m}^2$, and so $\mathfrak{m}^r = (t^r)$. Let $I$ be a nonzero proper ideal, with $\mathfrak{m}^n \subseteq I$. Since $\mathfrak{m}^{n+1} \subsetneq \mathfrak{m}^n \subseteq I$, the largest $r$ with $I \subseteq \mathfrak{m}^r$ exists, and $1 \leq r \leq n$. Choose $a \in I \setminus \mathfrak{m}^{r+1}$. Then $a = u t^r$ with $u \in A$, and $u \notin \mathfrak{m}$, since otherwise $a \in \mathfrak{m}^{r+1}$. So $u$ is a unit and $t^r \in I$. Hence $I = (t^r) = \mathfrak{m}^r$.

(5) implies (6): choose $t \in \mathfrak{m} \setminus \mathfrak{m}^2$. Then $(t) = \mathfrak{m}^r$ with $r \geq 1$, and $r = 1$ since $t \notin \mathfrak{m}^2$. So $\mathfrak{m} = (t)$ and every nonzero ideal is $\mathfrak{m}^n = (t^n)$.

(6) implies (1): $A$ is not a field, so $t$ is not a unit and $(t) \subseteq \mathfrak{m}$. Also $\mathfrak{m} = (t^r) \subseteq (t)$ for some $r$. So $\mathfrak{m} = (t)$. The ideals $(t^n)$ are distinct, since $(t^n) = (t^{n+1})$ gives $t^n = c t^{n+1}$ and $1 = ct$. So for $a \neq 0$ there is a unique $n = v(a)$ with $(a) = (t^n)$, and then $a = u t^n$ with $u$ a unit. Every $x \in K^*$ is then $u t^m$ with $u \in A^*$ and a unique $m \in \mathbb{Z}$. Put $v(x) = m$. This is a surjective homomorphism $K^* \to \mathbb{Z}$, and for $x = ut^m$ and $y = u't^{m'}$ with $m \leq m'$, $x + y = t^m(u + u't^{m' - m})$ has value at least $m$. So $v$ is a discrete valuation, and $x \in A$ if and only if $v(x) \geq 0$. $\square$

**Corollary P1.7.13 (height one primes of a normal domain).** Let $A$ be a Noetherian normal domain and $\mathfrak{p}$ a prime of height $1$. Then $A_\mathfrak{p}$ is a DVR.

Lean: not in Lean in this generality. For a Dedekind domain it is `IsLocalization.AtPrime.isDiscreteValuationRing_of_dedekind_domain` (proved in Mathlib).

*Proof.* The ring $A_\mathfrak{p}$ is a Noetherian local domain of dimension $\operatorname{ht} \mathfrak{p} = 1$ (Corollary P1.2.7), and it is normal by Proposition P1.4.20. Apply the theorem. $\square$

The valuation $v_\mathfrak{p}$ of $K = \operatorname{Frac} A$ with valuation ring $A_\mathfrak{p}$ is the *order of vanishing along* $\mathfrak{p}$. If $A = k[X]$ for a normal affine variety $X$, then $\mathfrak{p}$ is the ideal of a prime divisor $D \subseteq X$, $A_\mathfrak{p} = \mathcal{O}_{X, D}$ is the local ring at its generic point, and $v_\mathfrak{p}(f) = \operatorname{ord}_D(f)$.

**Proposition P1.7.14 (order of vanishing as a length).** Let $A$ be a Noetherian local domain of dimension $1$ with fraction field $K$. For $a \in A$ nonzero put $\operatorname{ord}(a) = \ell_A(A/aA)$. Then:

1. $\operatorname{ord}(a)$ is finite, and $\operatorname{ord}(a) = 0$ if and only if $a$ is a unit;
2. $\operatorname{ord}(ab) = \operatorname{ord}(a) + \operatorname{ord}(b)$;
3. $\operatorname{ord}(a/b) = \operatorname{ord}(a) - \operatorname{ord}(b)$ is a well defined homomorphism $K^* \to \mathbb{Z}$;
4. if $A$ is a DVR, then $\operatorname{ord} = v$.

Lean: Mathlib `Ring.ord` (definition, the length of $R/(x)$), `Ring.ord_mul`, `Ring.ord_of_irreducible` and `Ring.ordFrac` for the extension to the fraction field (proved in Mathlib).

*Proof.* (1) The only prime that contains $a$ is $\mathfrak{m}$, so $A/aA$ is Noetherian of dimension $0$, hence Artinian by Theorem P1.3.35, and of finite length by Proposition P1.3.28. Its length is $0$ exactly when $aA = A$. (2) Multiplication by $a$ gives a map $A/bA \to A/abA$. It is injective: if $ax = aby$, then $x = by$, as $A$ is a domain. Its cokernel is $A/aA$. So $0 \to A/bA \to A/abA \to A/aA \to 0$ is exact, and Proposition P1.3.28 gives (2). (3) If $a/b = c/d$, then $ad = bc$, and (2) gives $\operatorname{ord}(a) + \operatorname{ord}(d) = \operatorname{ord}(b) + \operatorname{ord}(c)$. So the value does not depend on the fraction, and it is a homomorphism by (2). (4) For $a = u t^n$, the chain $A \supsetneq tA \supsetneq \dots \supsetneq t^nA$ has quotients $t^iA/t^{i+1}A \cong k$, so $\ell(A/t^nA) = n = v(a)$. $\square$

For a DVR the order of vanishing is the valuation. Without normality $\operatorname{ord}$ is still a homomorphism on $K^*$, but it need not satisfy the rule for sums (the node below).

### Proof in words

A Noetherian local domain of dimension one is a curve germ, or the germ of a variety along a prime divisor. It is a DVR, the best case, exactly when it is normal, or when the maximal ideal has one generator, which says that the germ is smooth. Normality gives a principal maximal ideal by a short trick: some fraction $b/a$ with a pole multiplies the maximal ideal into the ring, and normality prevents it from multiplying the maximal ideal into itself. Once $\mathfrak{m} = (t)$, every element is a unit times a power of $t$, and the exponent is the valuation.

The corollary gives every height one prime of a normal Noetherian domain a discrete valuation. Geometrically, a normal variety is smooth at the generic point of each prime divisor, and a rational function has a well defined order of zero or pole along each prime divisor. This is the integer $\operatorname{ord}_D(f)$ that builds Weil divisors in Chapter 8.

The length $\ell(A/aA)$ counts the zeros of $a$ with multiplicity, as the intersection numbers of Section 3.4 do. It is additive for all one dimensional local domains, and it agrees with the valuation for DVRs. At a singular point of a curve the length adds up the orders along the branches of the normalization, and the rule for sums can fail.

### Examples

**Example P1.7.15 (a smooth point of a curve).** Let $\operatorname{char} k \neq 2$, let $C$ be the curve $y^2 = x^3 - x$, and let $A$ be its local ring at the origin, $A = k[x, y]_{(x, y)}/(y^2 - x^3 + x)$. It is a Noetherian local domain of dimension $1$. The equation has the linear term $x$, so $x = x^3 - y^2 \in \mathfrak{m}^2$, and $\mathfrak{m}/\mathfrak{m}^2$ is spanned by $y$. By the theorem $A$ is a DVR with uniformizer $y$. From $x(1 - x^2) = -y^2$ and $1 - x^2 \in A^*$ one gets $v(x) = 2$: the function $x$ vanishes to order $2$ at the origin, because the vertical line $x = 0$ is tangent to $C$ there.

**Example P1.7.16 (the $p$-adic integers).** By Section 6.1 every element of $\mathbb{Z}_p$ is $\sum_{j \geq 0} c_j p^j$ with digits $0 \leq c_j < p$. An element $x$ with $c_0 \neq 0$ is a unit: its image in each $\mathbb{Z}/p^n$ is prime to $p$, hence a unit, and the inverses modulo $p^n$ are compatible, so they define an inverse of $x$ in $\mathbb{Z}_p = \varprojlim \mathbb{Z}/p^n$. If $x \neq 0$ and $c_n$ is its first nonzero digit, then $x = p^n u$ with $u$ a unit. A product $p^n u \cdot p^m u' = p^{n + m} uu'$ is nonzero, so $\mathbb{Z}_p$ is a domain, and every nonzero ideal is $(p^n)$ for the least $n$ that occurs in it. This is Exercise 4 of Section 6.1. By condition (6), $\mathbb{Z}_p$ is a DVR with uniformizer $p$. In the same way $k[[x]]$ is a DVR with uniformizer $x$.

**Example P1.7.17 (the cusp).** Let $A = k[t^2, t^3]_{(t^2, t^3)}$, the local ring of the cusp $y^2 = x^3$ at the origin. Its maximal ideal $(t^2, t^3)$ needs two generators, so $\dim_k \mathfrak{m}/\mathfrak{m}^2 = 2$ and $A$ is not a DVR. This agrees with Example P1.4.24: $t = t^3/t^2$ is integral over $A$ and not in $A$. The ring $A/t^2A$ has $k$-basis $1, t^3$, and $A/t^3A$ has $k$-basis $1, t^2, t^4$. So $\operatorname{ord}(t^2) = 2$ and $\operatorname{ord}(t^3) = 3$. These are the orders in $t$, the uniformizer of the normalization $k[t]_{(t)}$ (Exercise 5).

**Example P1.7.18 (the node).** Let $\operatorname{char} k \neq 2$ and let $A = k[x, y]_{(x, y)}/(y^2 - x^2 - x^3)$, the local ring of the nodal cubic at the node. It is a Noetherian local domain of dimension $1$, with $\dim_k \mathfrak{m}/\mathfrak{m}^2 = 2$. Setting $y = x$ in the equation gives $A/(y - x)A \cong k[x]_{(x)}/(x^3)$, so $\operatorname{ord}(y - x) = 3$. In the same way $\operatorname{ord}(y + x) = 3$, and $A/yA \cong k[x]_{(x)}/(x^2)$ gives $\operatorname{ord}(2y) = \operatorname{ord}(y) = 2$. So
$$
\operatorname{ord}\big((y - x) + (y + x)\big) = 2 < 3 = \min\big(\operatorname{ord}(y - x), \operatorname{ord}(y + x)\big) ,
$$
and $\operatorname{ord}$ is not a valuation. The line $y = x$ is tangent to one branch of the node and meets the other transversally, so its order $3$ is $2 + 1$, a sum over the two branches.

**Example P1.7.19 (the valuation of an exceptional divisor).** Let $K = k(x, y)$ and let $X' \to \mathbb{A}^2$ be the blow-up of the origin, with exceptional curve $E$. On the chart with coordinates $x$ and $y' = y/x$, the blow-up is $\operatorname{Spec} k[x, y']$ and $E$ is the line $x = 0$. The prime $(x)$ of the normal domain $k[x, y']$ has height $1$, and by the corollary $k[x, y']_{(x)}$ is a DVR of $K$, with valuation $\operatorname{ord}_E$. For a polynomial $f = f_n + f_{n+1} + \dots$ with homogeneous parts $f_i$ and $f_n \neq 0$,
$$
f(x, xy') = x^n \big(f_n(1, y') + x f_{n+1}(1, y') + \dots\big) ,
$$
and $f_n(1, y') \neq 0$ is not divisible by $x$. So $\operatorname{ord}_E(f) = n$ is the order of $f$ at the origin, the monomial valuation with weights $(1, 1)$ of Section 7.1. This is the simplest divisorial valuation. In Volume 4 the discrepancy of $E$ over $\mathbb{A}^2$ is $\operatorname{ord}_E$ of the Jacobian of the blow-up, $\operatorname{ord}_E(x) = 1$, since $dx \wedge dy = x \, dx \wedge dy'$.

### Exercises

1. (A) Show that $k[x]_{(x)}$ and $\mathbb{Z}_{(p)}$ are DVRs, and compute $\operatorname{ord}$ of $x^2(1 + x)$ and of $12$ in the two rings, for $p = 2$.
2. (A) Let $\operatorname{char} k \neq 2$. Show that the local ring of $y^2 = x^3 - x$ at the point $(1, 0)$ is a DVR, and find a uniformizer and the value of $x - 1$.
3. (A) Show that a Noetherian valuation ring is a field or a DVR.
4. (B) Show that a local principal ideal domain that is not a field is a DVR, so that the definition in Mathlib agrees with the one here.
5. (B) Let $(A, \mathfrak{m})$ be a Noetherian local domain of dimension $1$ whose normalization $\bar{A}$ is a finite $A$-module. Show that $\ell_A(A/aA) = \ell_A(\bar{A}/a\bar{A})$ for $a \neq 0$. (Hint: apply the snake lemma to multiplication by $a$ on $0 \to A \to \bar{A} \to \bar{A}/A \to 0$, and use that $\bar{A}/A$ has finite length.) Deduce that on the cusp $\operatorname{ord}(f)$ is the order of $f$ in $t$.
6. (B) Show that $\operatorname{ord}_E(y^2 - x^3) = 2$ for the exceptional divisor $E$, and compute the valuation of the exceptional divisor of the blow-up of the origin in the chart $x' = x/y$, $y$.
7. (B) Let $A$ be a DVR with uniformizer $t$ and residue field $k$. Show that the completion $\hat{A}$ is a DVR with uniformizer $t$ and residue field $k$. (Hint: use the Krull intersection theorem of Section 6.1 and $\dim \hat{A} = 1$ from Section 6.2.)
8. (C) In the setting of Exercise 5, suppose $k$ is algebraically closed and let $\mathfrak{n}_1, \dots, \mathfrak{n}_r$ be the maximal ideals of $\bar{A}$, with valuations $v_i$. Show that $\operatorname{ord}(a) = \sum_i v_i(a)$. For the node, identify the two valuations and recover the example.

### Lean

Mathlib defines `IsDiscreteValuationRing` as a local principal ideal domain that is not a field, and recovers the valuation as `IsDiscreteValuationRing.addVal`. The theorem of this section is `IsDiscreteValuationRing.TFAE`, together with `tfae_of_isNoetherianRing_of_isLocalRing_of_isDomain`, which adds the condition of being a valuation ring and a Dedekind domain to the list. The criterion with $\mathfrak{m}/\mathfrak{m}^2$ is stated in terms of the cotangent space, as in `IsLocalRing.finrank_CotangentSpace_eq_one_iff`. The order of vanishing `Ring.ord` is defined for any ring as the length of $R/(x)$, with the extension `Ring.ordFrac` to the fraction field; Mathlib refers to this as Stacks tag 02MD. The handbook adds no `MinimalModel` node here.

### Notes and history

Discrete valuations appear in the work of Dedekind and Weber of 1882 on algebraic functions of one variable, where the points of a Riemann surface are described by the valuations of its function field. The characterization by normality is the one of Atiyah-Macdonald, Chapter 9, and the definition of the order of vanishing as a length is the one used by Fulton and in the Stacks project for intersection theory. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 9, Matsumura, Chapter 4, and Eisenbud, Chapter 11.
