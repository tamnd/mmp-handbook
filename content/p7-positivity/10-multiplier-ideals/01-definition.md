---
title: Multiplier ideals and thresholds
nodes: []
sources: [Laz04, KM98, Hir64, Har77]
reads_with: [Laz04:9.1, Laz04:9.2, Laz04:9.3, KM98:2.4]
requires: [P1.8, P4.4, P5.6, P7.8, P8.13, 4.2, 4.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Multiplier ideals and thresholds

### Statement

Throughout, $k$ has characteristic $0$ and $X$ is a smooth variety of dimension $n$. For a proper birational morphism $\mu \colon X' \to X$ from a smooth variety, $K_{X'/X} = \sum_E k_E E$ is the relative canonical divisor, effective and exceptional, as in Section 8.3.

**Definition P7.10.1 (log resolutions).** Let $\mathfrak{a} \subseteq \mathcal{O}_X$ be a nonzero ideal and $D$ an effective $\mathbb{Q}$-divisor. A *log resolution* of $\mathfrak{a}$ is a proper birational morphism $\mu \colon X' \to X$ from a smooth variety such that $\mathfrak{a} \mathcal{O}_{X'} = \mathcal{O}_{X'}(-F)$ for an effective divisor $F$ and $F + \operatorname{Exc}(\mu)$ has snc support, with $\operatorname{Exc}(\mu)$ a divisor. A *log resolution* of $D$ is a log resolution of the pair $(X, D)$ in the sense of Definition 4.2.9 such that $\mu^* D + \operatorname{Exc}(\mu)$ has snc support. Both exist by Theorem 4.2.10 and the remarks after Definition 4.6.2.

**Definition P7.10.2 (multiplier ideals).** Let $D$ be an effective $\mathbb{Q}$-divisor on $X$, $\mathfrak{a}$ a nonzero ideal and $c \geq 0$ rational. With log resolutions $\mu$ of $D$ and of $\mathfrak{a}$, put
$$\mathcal{J}(X, D) = \mu_* \mathcal{O}_{X'}(K_{X'/X} - \lfloor \mu^* D \rfloor), \qquad \mathcal{J}(X, \mathfrak{a}^c) = \mu_* \mathcal{O}_{X'}(K_{X'/X} - \lfloor c F \rfloor).$$
These are the *multiplier ideals* of $D$ and of $\mathfrak{a}^c$, written $\mathcal{J}(D)$ and $\mathcal{J}(\mathfrak{a}^c)$ when $X$ is understood.

**Lemma P7.10.3 (snc divisors).** Let $B$ be a $\mathbb{Q}$-divisor on $X$ with snc support, not necessarily effective, and $\mu \colon X' \to X$ a proper birational morphism from a smooth variety. Then
$$\mu_* \mathcal{O}_{X'}(K_{X'/X} - \lfloor \mu^* B \rfloor) = \mathcal{O}_X(-\lfloor B \rfloor).$$

Lean: not in Lean as stated.

**Proposition P7.10.4 (first properties).** Let $D$, $D'$ be effective $\mathbb{Q}$-divisors and $\mathfrak{a}$, $\mathfrak{b}$ nonzero ideals.

1. $\mathcal{J}(D)$ and $\mathcal{J}(\mathfrak{a}^c)$ do not depend on the log resolution, and they are ideals of $\mathcal{O}_X$. In the definition of $\mathcal{J}(\mathfrak{a}^c)$ it is enough that $\mu$ is a proper birational morphism from a smooth variety with $\mathfrak{a} \mathcal{O}_{X'} = \mathcal{O}_{X'}(-F)$ and $F$ of snc support.
2. If $D$ has snc support, then $\mathcal{J}(D) = \mathcal{O}_X(-\lfloor D \rfloor)$. If $D$ is integral, $\mathcal{J}(D) = \mathcal{O}_X(-D)$.
3. If $D \leq D'$, then $\mathcal{J}(D') \subseteq \mathcal{J}(D)$; if $\mathfrak{a} \subseteq \mathfrak{b}$ and $c \leq c'$, then $\mathcal{J}(\mathfrak{a}^{c'}) \subseteq \mathcal{J}(\mathfrak{b}^{c})$.
4. If $\mathfrak{a} = \mathcal{O}_X(-A)$ for an effective divisor $A$, then $\mathcal{J}(\mathfrak{a}^c) = \mathcal{J}(cA)$.
5. For every $c$ there is $\varepsilon > 0$ with $\mathcal{J}(\mathfrak{a}^{c'}) = \mathcal{J}(\mathfrak{a}^c)$ for $c \leq c' < c + \varepsilon$.

Lean: not in Lean as stated.

**Proposition P7.10.5 (the log canonical threshold).** Let $\mathfrak{a} \neq \mathcal{O}_X$ be a nonzero ideal with a log resolution $\mu$, $F = \sum_i e_i F_i$ and $K_{X'/X} = \sum_i k_i F_i$, where the $F_i$ are the prime divisors in the support of $F + \operatorname{Exc}(\mu)$. For rational $c \geq 0$, the following are equivalent:

1. $\mathcal{J}(\mathfrak{a}^c) = \mathcal{O}_X$;
2. $c e_i < k_i + 1$ for every $i$;
3. $c < \operatorname{lct}(X; \mathfrak{a})$, the log canonical threshold of Definition 4.6.2.

So $\operatorname{lct}(X; \mathfrak{a}) = \min\{ c : \mathcal{J}(\mathfrak{a}^c) \neq \mathcal{O}_X \}$, the minimum is attained, and the same holds for an effective divisor $D$ with $\mathcal{J}(cD)$ and $\operatorname{lct}(X; D)$. If $\mathcal{J}(\mathfrak{a}^c) \neq \mathcal{O}_X$, its zero set is the union of the centres $\mu(F_i)$ with $\lfloor c e_i \rfloor > k_i$.

Lean: not in Lean as stated.

### Proof in words

The multiplier ideal of an snc divisor is computed on $X$ itself: a boundary with snc support and coefficients less than $1$ is absorbed by the relative canonical divisor of any further blow-up, because Lemma P7.8.14 bounds the multiplicities of its pullback by $k_E + 1$. The integral part of the divisor comes out by the projection formula. Independence of the resolution follows: two log resolutions are dominated by a third, and the comparison of the third with either of them is the snc case on the first resolution, applied to the pulled back divisor, after the integral divisor $K_{X'/X}$ is taken out by the projection formula. The comparison needs no log resolution upstairs, only a smooth variety, so the multiplier ideal may be computed on any smooth model on which the divisor has snc support, a toric model for instance.

The multiplier ideal is trivial exactly when the divisor $K_{X'/X} - \lfloor c F \rfloor$ is effective, since then it is an effective exceptional divisor whose push-forward is $\mathcal{O}_X$, and otherwise every function in the ideal vanishes along the centre of a divisor with negative coefficient. Effectivity of the coefficients is the inequality $c e_i < k_i + 1$, which is the klt condition, and by Theorem 4.6.3 the first $c$ at which it fails is the log canonical threshold. So the threshold is where the multiplier ideal first jumps, and the jump is attained: the triple is lc at the threshold, and its multiplier ideal is already nontrivial there.

### Examples

**Example P7.10.6 (snc divisors).** On $X = \mathbb{A}^2$, let $D = \frac12 \{x = 0\} + \frac43 \{y = 0\}$. By part 2 of Proposition P7.10.4, $\mathcal{J}(D) = \mathcal{O}(-\lfloor D \rfloor) = (y)$, and $\mathcal{J}(cD) = \mathcal{O}$ for $c < \frac34$, $(y)$ for $\frac34 \leq c < \frac32$, $(y^2)$ for $\frac32 \leq c < 2$, and $(x y^2)$ at $c = 2$. The first jump is at $\frac34 = \min\{2, \frac34\}$, which is $\operatorname{lct}(\mathbb{A}^2; D)$ by Example 4.6.6.

**Example P7.10.7 (the cusp).** Let $C = \{y^2 = x^3\} \subseteq \mathbb{A}^2$ with the log resolution of Example 4.6.7: $\mu^* C = C_3 + 2E_1 + 3E_2 + 6E_3$ and $K_{X'/X} = E_1 + 2E_2 + 4E_3$. For $0 \leq c < 1$,
$$K_{X'/X} - \lfloor c \mu^* C \rfloor = (1 - \lfloor 2c \rfloor) E_1 + (2 - \lfloor 3c \rfloor) E_2 + (4 - \lfloor 6c \rfloor) E_3.$$
The first two coefficients are nonnegative for $c < 1$, and the third is nonnegative if and only if $c < \frac56$. So $\mathcal{J}(cC) = \mathcal{O}$ for $c < \frac56$. For $\frac56 \leq c < 1$ the divisor is $P - E_3$ with $P$ effective and exceptional, and a function $g$ lies in $\mathcal{J}(cC)$ if and only if it is regular, by the argument in the proof, and $\operatorname{ord}_{E_3}(g) \geq 1$, that is, $g(0) = 0$. So $\mathcal{J}(cC) = \mathfrak{m}_0$ for $\frac56 \leq c < 1$, and $\mathcal{J}(C) = \mathcal{O}(-C)$ by part 2 of Proposition P7.10.4. The first jump is at $\operatorname{lct} = \frac56$, as Proposition P7.10.5 says.

**Example P7.10.8 (powers of the maximal ideal).** Let $\mathfrak{m} \subseteq k[x_1, \dots, x_n]$ be the ideal of the origin, $n \geq 2$, and $\mu \colon X' \to \mathbb{A}^n$ the blow-up of the origin, with exceptional divisor $E$. Then $\mathfrak{m} \mathcal{O}_{X'} = \mathcal{O}_{X'}(-E)$ and $K_{X'/X} = (n - 1)E$ (Section P5.6), and $\mu$ is a log resolution of $\mathfrak{m}$. So
$$\mathcal{J}(\mathfrak{m}^c) = \mu_* \mathcal{O}_{X'}((n - 1 - \lfloor c \rfloor) E) = \mathfrak{m}^{\lfloor c \rfloor - n + 1},$$
with the convention $\mathfrak{m}^j = \mathcal{O}$ for $j \leq 0$: for $j \geq 0$, $\mu_* \mathcal{O}_{X'}(-jE)$ consists of the functions with $\operatorname{ord}_E \geq j$, which are those vanishing to order $j$ at the origin, since $\operatorname{ord}_E(g)$ is the multiplicity of $g$ at the origin, and for $j < 0$ it is $\mathcal{O}$ by the argument for effective exceptional divisors. The first jump is at $c = n = \operatorname{lct}(\mathbb{A}^n; \mathfrak{m})$, in agreement with Example 4.6.15 for $k = 1$.

### Proof

*Lemma P7.10.3.* Write $B = \lfloor B \rfloor + \{B\}$. Since $\mu^* \lfloor B \rfloor$ is an integral divisor, $\lfloor \mu^* B \rfloor = \mu^* \lfloor B \rfloor + \lfloor \mu^* \{B\} \rfloor$, and the projection formula reduces the statement to $\mu_* \mathcal{O}_{X'}(P) = \mathcal{O}_X$ for $P = K_{X'/X} - \lfloor \mu^* \{B\} \rfloor$. Write $\{B\} = \sum_j a_j D_j$ with $0 < a_j < 1$ and the $D_j$ the components of $\operatorname{Supp} B$ that carry a nonintegral coefficient, smooth since the support is snc. Along the strict transform of $D_j$, $P$ has coefficient $-\lfloor a_j \rfloor = 0$. Along an exceptional prime $E$, Lemma P7.8.14, whose proof is local on $X$ and does not use projectivity, gives $\operatorname{ord}_E(\mu^* \{B\}) < k_E + 1$, so $\lfloor \operatorname{ord}_E(\mu^* \{B\}) \rfloor \leq k_E$, and the coefficient of $P$ along $E$ is at least $0$. Every other prime divisor of $X'$ has coefficient $0$. So $P$ is effective and exceptional. For an open set $U \subseteq X$ and a rational function $\varphi$ with $\operatorname{div}(\varphi) + P \geq 0$ on $\mu^{-1}(U)$, the divisor $\operatorname{div}(\varphi)$ is effective on $U$ minus the codimension $2$ set $\mu(\operatorname{Exc}(\mu))$, because $\mu$ is an isomorphism there and $\mu_* P = 0$, so $\varphi$ is regular on $U$ by Corollary P1.8.3; conversely every regular function is a section since $P \geq 0$. So $\mu_* \mathcal{O}_{X'}(P) = \mathcal{O}_X$.

*Proposition P7.10.4, part 1.* Let $\mu_1 \colon X_1 \to X$ and $\mu_2 \colon X_2 \to X$ be two proper birational morphisms from smooth varieties with $\mathfrak{a} \mathcal{O}_{X_i} = \mathcal{O}_{X_i}(-F_i)$ and $F_i$ of snc support. Let $X_3$ be a resolution of the closure of the graph of $X_1 \dashrightarrow X_2$, by Theorem 4.2.10, with $g_i \colon X_3 \to X_i$ and $\mu_3 = \mu_i \circ g_i$. Then $\mathfrak{a} \mathcal{O}_{X_3} = \mathcal{O}_{X_3}(-g_i^* F_i)$, so $g_1^* F_1 = g_2^* F_2 = F_3$, and $K_{X_3/X} = g_i^* K_{X_i/X} + K_{X_3/X_i}$. Lemma P7.10.3 on the smooth variety $X_i$, applied to $g_i$ and the $\mathbb{Q}$-divisor $c F_i$ with snc support, together with the projection formula for the integral divisor $K_{X_i/X}$, gives
$$g_{i*} \mathcal{O}_{X_3}(K_{X_3/X} - \lfloor c F_3 \rfloor) = \mathcal{O}_{X_i}(K_{X_i/X}) \otimes g_{i*} \mathcal{O}_{X_3}(K_{X_3/X_i} - \lfloor g_i^*(c F_i) \rfloor) = \mathcal{O}_{X_i}(K_{X_i/X} - \lfloor c F_i \rfloor).$$
Pushing forward by $\mu_i$ gives $\mu_{3*} \mathcal{O}_{X_3}(K_{X_3/X} - \lfloor c F_3 \rfloor) = \mu_{i*} \mathcal{O}_{X_i}(K_{X_i/X} - \lfloor c F_i \rfloor)$ for $i = 1, 2$, so the two definitions agree. The same argument with $\mu_i^* D$ in place of $c F_i$ gives independence for $\mathcal{J}(D)$. Since $K_{X'/X} - \lfloor \mu^* D \rfloor \leq K_{X'/X}$ and $\mu_* \mathcal{O}_{X'}(K_{X'/X}) = \mathcal{O}_X$ by Lemma P7.10.3 with $B = 0$, the multiplier ideal is a subsheaf of $\mathcal{O}_X$, coherent since $\mu$ is proper (Theorem P4.4.8), and an ideal.

*Part 2.* Lemma P7.10.3 with $B = D$ and $\mu$ the identity, which is a log resolution of an snc divisor, or any other log resolution. An integral divisor has snc support after a log resolution, and $\lfloor \mu^* D \rfloor = \mu^* D$, so the projection formula gives $\mathcal{J}(D) = \mathcal{O}_X(-D) \otimes \mu_* \mathcal{O}_{X'}(K_{X'/X}) = \mathcal{O}_X(-D)$.

*Part 3.* A log resolution of $D + D'$ is one of $D$ and of $D'$. A log resolution of $\mathfrak{a} \mathfrak{b}$ computes both $\mathcal{J}(\mathfrak{a}^{c'})$ and $\mathcal{J}(\mathfrak{b}^c)$ by part 1: an ideal whose product with another ideal is locally principal in a domain is itself locally principal, so $\mathfrak{a} \mathcal{O}_{X'}$ and $\mathfrak{b} \mathcal{O}_{X'}$ are invertible, with supports in the snc support of $(\mathfrak{a} \mathfrak{b}) \mathcal{O}_{X'}$ (Laz04, Section 9.1). Then $\lfloor \mu^* D \rfloor \leq \lfloor \mu^* D' \rfloor$, and $\mathfrak{a} \subseteq \mathfrak{b}$ gives $F_{\mathfrak{b}} \leq F_{\mathfrak{a}}$, so $\lfloor c F_{\mathfrak{b}} \rfloor \leq \lfloor c' F_{\mathfrak{a}} \rfloor$. The sheaves $\mathcal{O}_{X'}(K_{X'/X} - \cdot)$ are nested, and so are their push-forwards.

*Part 4.* A log resolution of $\mathfrak{a}$ has $F = \mu^* A$, and the two definitions agree.

*Part 5.* There are finitely many $e_i$, and $\lfloor c' e_i \rfloor = \lfloor c e_i \rfloor$ for $c \leq c' < c + \varepsilon$ when $\varepsilon e_i$ is smaller than the distance from $c e_i$ to the next integer above it, for every $i$ with $e_i > 0$.

*Proposition P7.10.5.* If $c e_i < k_i + 1$ for every $i$, then $\lfloor c e_i \rfloor \leq k_i$, so $P = K_{X'/X} - \lfloor c F \rfloor$ is effective. It is exceptional: a non-exceptional $F_i$ has $k_i = 0$ and $c e_i < 1$, so coefficient $0$. By the last step of the proof of Lemma P7.10.3, $\mu_* \mathcal{O}_{X'}(P) = \mathcal{O}_X$. Conversely, suppose $c e_i \geq k_i + 1$ for some $i$, so the coefficient of $F_i$ in $P$ is $k_i - \lfloor c e_i \rfloor \leq -1$. A local section $g$ of $\mathcal{J}(\mathfrak{a}^c)$ near a point of $\mu(F_i)$ satisfies $\operatorname{div}(\mu^* g) + P \geq 0$, so $\operatorname{ord}_{F_i}(\mu^* g) \geq 1$, and $g$ vanishes on $\mu(F_i)$. So $\mathcal{J}(\mathfrak{a}^c) \neq \mathcal{O}_X$, and its zero set contains every $\mu(F_i)$ with $\lfloor c e_i \rfloor > k_i$; it is contained in their union since off that union $P$ is effective on the preimage and the first argument applies. This proves that 1 and 2 are equivalent.

For 2 and 3, apply Theorem 4.6.3 to the pair $(X, 0)$, which is lc since $X$ is smooth. Here $K_{X'} + \Delta_{X'} = \mu^* K_X$ gives $\Delta_{X'} = -K_{X'/X}$, so $b_i = -k_i$, and part 2 of that theorem gives $\operatorname{lct}(X; \mathfrak{a}) = \min\{ (k_i + 1)/e_i : e_i > 0 \}$. The condition $c e_i < k_i + 1$ for all $i$ with $e_i > 0$ is $c < (k_i + 1)/e_i$ for all such $i$, that is, $c < \operatorname{lct}(X; \mathfrak{a})$; for $e_i = 0$ it holds since $k_i \geq 0$. At $c = \operatorname{lct}(X; \mathfrak{a})$ condition 2 fails for the $i$ attaining the minimum, so the minimum of the set $\{c : \mathcal{J}(\mathfrak{a}^c) \neq \mathcal{O}_X\}$ exists and equals the threshold. For a divisor, use part 4 of Proposition P7.10.4 and the agreement of the two thresholds in Definition 4.6.2.

### Exercises

1. (A) Compute $\mathcal{J}(c \{x^a y^b = 0\})$ on $\mathbb{A}^2$ for all $c \geq 0$, and find all the values of $c$ at which it jumps.
2. (A) Let $D$ be an effective $\mathbb{Q}$-divisor and $A$ an effective integral divisor. Show that $\mathcal{J}(D + A) = \mathcal{J}(D) \otimes \mathcal{O}_X(-A)$.
3. (B) Let $D$ be an effective $\mathbb{Q}$-divisor and $x \in X$ a point with $\operatorname{mult}_x D \geq n$. Show that $\mathcal{J}(D)_x \subseteq \mathfrak{m}_x$, by looking at the exceptional divisor of the blow-up of $x$. Show that $\operatorname{mult}_x D < 1$ implies $\mathcal{J}(D)_x = \mathcal{O}_{X, x}$ (Laz04, Section 9.5).
4. (B) Show that $\mathcal{J}((\mathfrak{a}^m)^{c}) = \mathcal{J}(\mathfrak{a}^{mc})$ for every integer $m \geq 1$, and that $\mathcal{J}(\mathfrak{a}^c)$ depends only on the integral closure of $\mathfrak{a}$.
5. (B) For the cusp, compute $\mathcal{J}(c C)$ for $1 \leq c < 2$ and check that $\mathcal{J}(cC) = \mathcal{J}((c - 1)C) \otimes \mathcal{O}(-C)$ there.
6. (C) Let $\mathfrak{a} \subseteq \mathcal{O}_X$ be generated by $f_1, \dots, f_r$ and $g = \sum_j \lambda_j f_j$ with general $\lambda \in k^r$. Show that $\mathcal{J}(\mathfrak{a}^c) = \mathcal{J}(c \operatorname{div}(g))$ for $0 \leq c < 1$, by Bertini on a log resolution of $\mathfrak{a}$. Compare with Corollary 4.6.12.

### Lean

The project library has no multiplier ideals. The log canonical threshold of a divisor is the definition `MinimalModel.lct`, and Proposition P7.10.5 relates it to the multiplier ideal; neither the ideal nor the relation is stated in Lean. Mathlib has no log resolutions. The handbook adds no `MinimalModel` node here.

### Notes and history

Multiplier ideals arose in complex analysis, in the work of Nadel (Nad90) on Kähler-Einstein metrics, where $\mathcal{J}(\varphi)$ is the ideal of holomorphic functions $g$ with $|g|^2 e^{-2\varphi}$ locally integrable; for $\varphi = \sum_j c_j \log |f_j|$ the algebraic and analytic ideals agree (Laz04, Section 9.3). The literature state is theorem. The algebraic theory is Lazarsfeld's Chapter 9 (Laz04), which follows Esnault and Viehweg and Ein. The description of the threshold as the first jump of the multiplier ideal is in Lazarsfeld, Section 9.3, and in Kollár and Mori, Section 2.4 (KM98) under the name of klt pairs; Volume 4, Chapter 6 computes the threshold without multiplier ideals.
