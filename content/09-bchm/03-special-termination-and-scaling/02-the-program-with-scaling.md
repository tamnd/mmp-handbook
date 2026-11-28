---
title: The program with scaling
nodes: [MM07D8FAVG]
sources: [BCHM10, KM98, Bir12, HM07]
reads_with: [BCHM10:3, KM98:3]
requires: [1.1, 1.3, 1.5, 7.4, 7.5, 8.1, 8.4]
level: advanced
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The program with scaling

### Statement

The program with scaling chooses at each step the extremal ray that a second divisor, the scaling divisor, selects. Its thresholds are a decreasing parameter, and each of its models is a weak log canonical model of a divisor of the form $K_X + \Delta + tC$. That property is what links the program to the finiteness of models and gives termination when the boundary is big. Throughout, $\pi \colon X \to U$ is projective, $(X, \Delta)$ is a $\mathbb{Q}$-factorial klt pair and all divisors are $\mathbb{Q}$-divisors; the cone theorem, the contraction theorem and the length bound are used in their relative forms over $U$ (Theorem 7.4.6, Theorem 7.4.13 and Corollary 7.5.4).

**Definition 9.3.6 (the program with scaling).** Let $C \ge 0$ be a $\mathbb{Q}$-divisor with $K_X + \Delta + C$ nef over $U$. Put $(X_0, \Delta_0, C_0) = (X, \Delta, C)$, $\lambda_{-1} = 1$, and given $(X_i, \Delta_i, C_i)$ let
$$\lambda_i = \inf \{ t \ge 0 : K_{X_i} + \Delta_i + t C_i \text{ is nef over } U \}.$$
If $\lambda_i = 0$, stop. Otherwise let $R_i$ be an extremal ray of $\overline{NE}(X_i / U)$ with $(K_{X_i} + \Delta_i) \cdot R_i < 0$ and $(K_{X_i} + \Delta_i + \lambda_i C_i) \cdot R_i = 0$, and $\varphi_i \colon X_i \to Y_i$ its contraction over $U$. If $\varphi_i$ is of fibre type, stop with the Mori fibre space $\varphi_i$. If it is divisorial, put $X_{i+1} = Y_i$; if it is small and its flip exists, let $X_{i+1}$ be the flip. Let $\Delta_{i+1}$ and $C_{i+1}$ be the strict transforms. This is the *$(K_X + \Delta)$-program with scaling of $C$ over $U$*, and the $\lambda_i$ are its *thresholds*.

**Lemma 9.3.7 (the ray exists).** In Definition 9.3.6, suppose $K_{X_i} + \Delta_i + \lambda_{i-1} C_i$ is nef over $U$ and $\lambda_i > 0$. Then $K_{X_i} + \Delta_i + \lambda_i C_i$ is nef over $U$, and there is an extremal ray $R_i$ as in the definition; every such ray has $C_i \cdot R_i > 0$.

Lean: not yet in Lean.

**Lemma 9.3.8 (the thresholds decrease).** In Definition 9.3.6, each $(X_i, \Delta_i)$ is a $\mathbb{Q}$-factorial klt pair, $K_{X_i} + \Delta_i + \lambda_{i-1} C_i$ is nef over $U$, and $\lambda_i \le \lambda_{i-1}$. In particular the hypotheses of Lemma 9.3.7 hold at every step, and the program is defined as long as the flips exist.

Lean: not yet in Lean.

**Lemma 9.3.9 (non-positive steps raise discrepancies).** Let $D_i = K_{X_i} + \Delta_i + t C_i$ with $D_i \cdot R_i \le 0$, and let $D_{i+1}$ be its strict transform on $X_{i+1}$, for a divisorial or a flipping step of Definition 9.3.6. Then $a(G, X_i, \Delta_i + tC_i) \le a(G, X_{i+1}, \Delta_{i+1} + tC_{i+1})$ for every divisor $G$ over $X_i$, and if $D_i \cdot R_i < 0$ the inequality is strict whenever the centre of $G$ on $X_i$ lies in the exceptional locus of $\varphi_i$.

Lean: not yet in Lean.

**Proposition 9.3.10 (the models are weak log canonical models).** In Definition 9.3.6, let $\phi_i \colon X \dashrightarrow X_i$ be the composite of the first $i$ steps. Then $\phi_i$ is a birational contraction, and for every $t \in [\lambda_i, \lambda_{i-1}]$ it is a weak log canonical model of $K_X + \Delta + tC$ over $U$. If the program stops with $\lambda_i = 0$, then $\phi_i$ is a log terminal model of $K_X + \Delta$ over $U$.

Lean: not yet in Lean.

**Theorem 9.3.11 (termination with scaling for a big boundary).** Suppose Theorem 9.1.8 holds in dimension $n$. Let $(X, \Delta)$ be an $n$-dimensional $\mathbb{Q}$-factorial klt pair, projective over $U$, with $\Delta$ big over $U$, and let $C \ge 0$ be a $\mathbb{Q}$-divisor such that $(X, \Delta + C)$ is klt and $K_X + \Delta + C$ is nef over $U$. Then every $(K_X + \Delta)$-program with scaling of $C$ over $U$ whose flips exist terminates after finitely many steps.

Lean: not yet in Lean.

**Corollary 9.3.12 (the two outcomes).** In Theorem 9.3.11 the program ends with a log terminal model of $K_X + \Delta$ over $U$ if $K_X + \Delta$ is pseudo-effective over $U$, and with a Mori fibre space otherwise.

Lean: not yet in Lean.

**Theorem 9.3.13 ($A_n + B_n \Rightarrow C_n$).** Let $n \ge 2$. If Theorems 9.1.4 and 9.1.5 hold in dimension $n$, then Theorem 9.1.6 holds in dimension $n$.

Lean: not yet in Lean.

### Proof in words

The threshold is the largest of the ratios $-(K + \Delta) \cdot \Gamma / C \cdot \Gamma$ over the curves of the negative extremal rays; the length bound and the integrality of intersection numbers of $\mathbb{Q}$-divisors with a fixed denominator leave only finitely many ratios above any positive number, so the largest is attained. After a step, the divisor $K + \Delta + \lambda_i C$, which was zero on the contracted ray, is a pullback from the base, so it is still nef, and the next threshold is no larger.

For $t$ between two consecutive thresholds, every step so far was non-positive for $K + \Delta + tC$, so discrepancies of $K + \Delta + tC$ only went up, and the current model is a weak log canonical model of it. With a big boundary these divisors are, up to $\mathbb{Q}$-linear equivalence, in a set $\mathcal{L}_A(V)$ with a general ample part, where Theorem 9.1.8 allows only finitely many weak log canonical models. An infinite program would visit one model twice; but each step strictly raises the discrepancy of some divisor, and discrepancies never come down, so no model repeats.

### Examples

**Example 9.3.14 (a program on the plane blown up twice).** Let $X$ be the blow-up of $\mathbb{P}^2$ at two points, with exceptional curves $E_1, E_2$, line class $L$ and $\ell = L - E_1 - E_2$ the strict transform of the line through the two points. The cone $\overline{NE}(X)$ is spanned by $E_1, E_2, \ell$, three $(-1)$-curves with $K_X \cdot E_1 = K_X \cdot E_2 = K_X \cdot \ell = -1$. Let $H$ be a general member of $|6L - 2E_1 - 3E_2|$ and scale by $C = H$. For the steps of the program only the class of $C$ matters; the klt condition of Theorem 9.3.11 holds for $\frac1N H$ with $N$ large, and scaling by $\frac1N H$ multiplies every threshold by $N$ without changing the models. Here $H \cdot E_1 = 2$, $H \cdot E_2 = 3$ and $H \cdot \ell = 1$, so $H$ is ample, and the ratios $-K \cdot \Gamma / H \cdot \Gamma$ are $\frac12$, $\frac13$ and $1$. So $\lambda_0 = 1$ and the first step contracts $\ell$, with $K + H = 3L - E_1 - 2E_2$, which is zero on $\ell$. The target is $\mathbb{P}^1 \times \mathbb{P}^1$, with rulings $f_1, f_2$ pulled back to $F_1 = L - E_1$ and $F_2 = L - E_2$. From $L = F_1 + F_2 - \ell$, $E_1 = F_2 - \ell$ and $E_2 = F_1 - \ell$ one gets $H = 3F_1 + 4F_2 - \ell$, so $H_1 = 3f_1 + 4f_2$, and $K_{X_1} + tH_1 = (3t - 2) f_1 + (4t - 2) f_2$. This is nef if and only if $t \ge \frac23$, so $\lambda_1 = \frac23$, and the ray on which $K_{X_1} + \frac23 H_1 = \frac23 f_2$ vanishes is that of the curves of class $f_2$, the fibres of the projection $p_2 \colon \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1$ along which $f_2$ is trivial. The program ends with the Mori fibre space $p_2$, as $K_X$ is not pseudo-effective, with thresholds $1 > \frac23$.

**Example 9.3.15 (a repeated threshold).** On the same $X$ take $H = 5L - E_1 - E_2$, with $H \cdot E_1 = H \cdot E_2 = 1$ and $H \cdot \ell = 3$. The ratios are $1, 1, \frac13$, so $\lambda_0 = 1$ and $K + H = 2L$ vanishes on the face spanned by $E_1$ and $E_2$. The program contracts one of the two rays, say $E_1$, to $X_1 = \operatorname{Bl}_{p_2} \mathbb{P}^2$, with $H_1 = 5L - E_2$. There the cone is spanned by $E_2$ and the fibre class $L - E_2$, with ratios $1$ and $\frac{2}{4} = \frac12$, so $\lambda_1 = 1$ again, and the program contracts $E_2$. On $\mathbb{P}^2$, $H_2 = 5L$ and $\lambda_2 = \frac35$, with the Mori fibre space $\mathbb{P}^2 \to \mathrm{pt}$. The thresholds are $1 = 1 > \frac35$: Lemma 9.3.8 allows equality, and equality occurs when $K + \lambda_i C$ vanishes on a face of dimension at least two.

**Example 9.3.16 (the toric program as weak log canonical models).** In Proposition 9.1.19 the thresholds are $1, \frac56, \frac45$. By Proposition 9.3.10, whose proof uses only the discrepancy computations and not the klt condition on $\Delta + C$, the composites from $X^+$ give weak log canonical models: $X^+$ itself for $K + tH$ with $t \ge 1$, the flip $X$ for $t \in [\frac56, 1]$, and $\mathbb{P}^3$ for $t \in [\frac45, \frac56]$. For $t < \frac45$ the divisor $K + tH$ is not pseudo-effective and has no weak log canonical model. These intervals are the chambers crossed in Example 9.1.21.

### Proof

*Lemma 9.3.7.* Write $D = K_{X_i} + \Delta_i$ and $N = D + \lambda_{i-1} C_i$, nef over $U$ by hypothesis. Fix an ample $H$ over $U$. By the relative cone theorem and the length bound, $\overline{NE}(X_i / U) = \overline{NE}(X_i / U)_{D \ge 0} + \sum_j R_j$, where the $R_j$ are the $D$-negative extremal rays, countably many and accumulating only at the hyperplane $D^{\perp}$, and each $R_j$ is spanned by a rational curve $\Gamma_j$ with $0 < -D \cdot \Gamma_j \le 2n$. For $s \in [0, 1]$ and $t = s \lambda_{i-1}$, $D + tC_i = (1 - s) D + s N$ is non-negative on $\overline{NE}(X_i/U)_{D \ge 0}$. So for $t \in [0, \lambda_{i-1}]$, $D + tC_i$ is nef over $U$ if and only if it is non-negative on every $\Gamma_j$. On $\Gamma_j$, $N \cdot \Gamma_j \ge 0 > D \cdot \Gamma_j$ forces $C_i \cdot \Gamma_j > 0$, and the condition reads $t \ge r_j = -D \cdot \Gamma_j / C_i \cdot \Gamma_j$. Hence $\lambda_i = \sup_j r_j$.

Let $m$ be a positive integer with $mD$ and $mC_i$ Cartier. Then $-D \cdot \Gamma_j \in \frac1m \mathbb{Z} \cap (0, 2n]$, a finite set, and $C_i \cdot \Gamma_j \in \frac1m \mathbb{Z}_{> 0}$. If $r_j \ge \frac12 \lambda_i > 0$, then $C_i \cdot \Gamma_j \le 4n / \lambda_i$, so $C_i \cdot \Gamma_j$ also lies in a finite set. So only finitely many values $r_j \ge \frac12 \lambda_i$ occur, and the supremum is a maximum, attained on some $R_j$. Then $D + \lambda_i C_i$ is nef over $U$, and $R_i = R_j$ has the required properties; any ray with them has $C_i \cdot R_i = -D \cdot R_i / \lambda_i > 0$.

*Lemma 9.3.8.* By induction on $i$; for $i = 0$ the divisor $K_X + \Delta + C$ is nef by hypothesis and $(X, \Delta)$ is a $\mathbb{Q}$-factorial klt pair. Suppose the statement holds for $i$ and $\lambda_i > 0$, and let $M = K_{X_i} + \Delta_i + \lambda_i C_i$, nef over $U$ by Lemma 9.3.7 and zero on $R_i$. If $\varphi_i$ is divisorial, Proposition 7.5.11 shows that $(X_{i+1}, \Delta_{i+1})$ is a $\mathbb{Q}$-factorial klt pair, and Theorem 1.1.12 in its relative form gives $M \sim_{\mathbb{Q}} \varphi_i^* M'$ with $M' = \varphi_{i*} M = K_{X_{i+1}} + \Delta_{i+1} + \lambda_i C_{i+1}$, which is nef over $U$ because its pullback is. If $\varphi_i$ is small, part 1 of Proposition 8.1.17 with $B = M$ gives $c = 0$, as $M \cdot R_i = 0$ and $D \cdot R_i < 0$, so $M \sim_{\mathbb{Q}} \varphi_i^* L$ and its strict transform $K_{X_{i+1}} + \Delta_{i+1} + \lambda_i C_{i+1} \sim_{\mathbb{Q}} \varphi_i^{+*} L$ is nef over $U$; part 2 of Proposition 8.1.17 and Lemma 8.1.19 show that $(X_{i+1}, \Delta_{i+1})$ is a $\mathbb{Q}$-factorial klt pair. So $\lambda_{i+1} \le \lambda_i$.

*Lemma 9.3.9.* Write $D = K_{X_i} + \Delta_i$, so $D \cdot R_i < 0$, and $D_i = D + tC_i$. In the divisorial case, with exceptional divisor $E$ and $E \cdot R_i < 0$, the divisor $D_i - \varphi_i^* \varphi_{i*} D_i$ is $\varphi_i$-exceptional, so equal to $\alpha E$, and intersecting with a curve of $R_i$ gives $\alpha = D_i \cdot R_i / E \cdot R_i \ge 0$, positive if $D_i \cdot R_i < 0$. Then for $G$ over $X_i$, $a(G, X_{i+1}, \Delta_{i+1} + tC_{i+1}) - a(G, X_i, \Delta_i + tC_i) = \alpha \operatorname{mult}_G E$, where $\operatorname{mult}_G E$ is the coefficient of $G$ in the pullback of $E$ to a model where $G$ is a divisor, which is positive exactly when the centre of $G$ lies in $E$. In the flipping case, part 1 of Proposition 8.1.17 gives $D_i \sim_{\mathbb{Q}} cD + \varphi_i^* L$ with $c = D_i \cdot R_i / D \cdot R_i \ge 0$, positive if $D_i \cdot R_i < 0$, and the same on $X_{i+1}$ with the same $c$ and $L$. On a common resolution $p \colon W \to X_i$, $q \colon W \to X_{i+1}$, the difference $p^* D_i - q^* D_{i+1} = c(p^* D - q^* D^+)$, where $D^+ = K_{X_{i+1}} + \Delta_{i+1}$, and the coefficient of $G$ in $p^* D - q^* D^+$ is $a(G, X_{i+1}, \Delta_{i+1}) - a(G, X_i, \Delta_i)$, which is non-negative and positive over the flipping locus by Lemma 8.1.19. Multiplying by $c$ gives the claim.

*Proposition 9.3.10.* Each step contracts a divisor or is an isomorphism in codimension one, so $\phi_i$ is a birational contraction, and $(X_i, \Delta_i)$ is $\mathbb{Q}$-factorial klt by Lemma 9.3.8. Let $t \in [\lambda_i, \lambda_{i-1}]$. The divisor $K_{X_i} + \Delta_i + tC_i$ is a convex combination of $K_{X_i} + \Delta_i + \lambda_i C_i$ and $K_{X_i} + \Delta_i + \lambda_{i-1} C_i$, both nef over $U$ by Lemmas 9.3.7 and 9.3.8, so it is nef over $U$. For each step $k < i$, $t \le \lambda_{i-1} \le \lambda_k$ by Lemma 9.3.8, and as $C_k \cdot R_k > 0$ by Lemma 9.3.7,
$$(K_{X_k} + \Delta_k + tC_k) \cdot R_k \le (K_{X_k} + \Delta_k + \lambda_k C_k) \cdot R_k = 0.$$
By Lemma 9.3.9 applied to each step, $a(G, X, \Delta + tC) \le a(G, X_i, \Delta_i + tC_i)$ for every divisor $G$, in particular for every $\phi_i$-exceptional prime divisor, so $\phi_i$ is a weak log canonical model of $K_X + \Delta + tC$.

If the program stops with $\lambda_i = 0$, take $t = 0$. Each $\phi_i$-exceptional prime divisor $G$ is the exceptional divisor of a divisorial step $k < i$, which is $(K_{X_k} + \Delta_k)$-negative, so by Lemma 9.3.9 its discrepancy goes up strictly at step $k$, and it does not go down at the other steps. So $a(G, X, \Delta) < a(G, X_i, \Delta_i)$; as $X_i$ is $\mathbb{Q}$-factorial and $(X_i, \Delta_i)$ is klt, hence dlt, $\phi_i$ is a log terminal model.

*Theorem 9.3.11.* Suppose the program does not terminate. Divisorial steps lower the Picard number by Proposition 7.5.11, so all but finitely many steps are flips; and no step is of fibre type, so $\lambda_i > 0$ for all $i$. As $\Delta$ is big over $U$, Kodaira's lemma over a base, Lemma 5.1.9, gives $\Delta \sim_{\mathbb{Q}, U} A + B$ with $A$ ample over $U$ and $B \ge 0$, and $A$ may be replaced by a general member of its $\mathbb{Q}$-linear system, by a Bertini argument. For a rational $\varepsilon > 0$ and $t \in [0, 1]$ put
$$\Delta_{\varepsilon, t} = (1 - \varepsilon) \Delta + \varepsilon B + \varepsilon A + tC \sim_{\mathbb{Q}, U} \Delta + tC.$$
For $\varepsilon$ small, $(X, \Delta_{\varepsilon, t})$ is klt for every $t \in [0, 1]$, because $(X, \Delta + C)$ is klt, so $(X, \Delta + tC)$ is klt for $t \in [0, 1]$, klt is an open condition on the coefficients of the finitely many components involved, and $\varepsilon A$ is general. Let $V$ be the span of the components of $\Delta$, $B$ and $C$. Then $\Delta_{\varepsilon, t} \in \mathcal{L}_{\varepsilon A}(V)$ with $\varepsilon A$ a general ample $\mathbb{Q}$-divisor over $U$.

The conditions of Definition 9.1.1 for $K_X + \Delta + tC$ and for $K_X + \Delta_{\varepsilon, t}$ are the same, as the two divisors differ by a divisor $\mathbb{Q}$-linearly equivalent to $0$ over $U$, whose pullbacks to a common resolution cancel in the differences of discrepancies. So by Proposition 9.3.10 every $\phi_i$ is a weak log canonical model of $K_X + \Delta_{\varepsilon, t}$ for $t = \lambda_i \in (0, 1]$. By Theorem 9.1.8 there are finitely many maps $\psi_j$ such that each $\phi_i = \xi_i \circ \psi_{j(i)}$ with $\xi_i$ an isomorphism. So there are $i < k$ with $j(i) = j(k)$, and then $\phi_k \circ \phi_i^{-1} = \xi_k \circ \xi_i^{-1}$ is an isomorphism $X_i \to X_k$ that carries $\Delta_i = \phi_{i*} \Delta$ to $\Delta_k = \phi_{k*} \Delta$. Hence $a(G, X_i, \Delta_i) = a(G, X_k, \Delta_k)$ for every divisor $G$. But step $i$ is $(K_{X_i} + \Delta_i)$-negative, so for a divisor $G$ with centre in the exceptional locus of $\varphi_i$, for example the exceptional divisor of the blow-up of a general point of that locus, Lemma 9.3.9 with $t = 0$ gives $a(G, X_i, \Delta_i) < a(G, X_{i+1}, \Delta_{i+1})$, and the later steps do not lower it, so $a(G, X_i, \Delta_i) < a(G, X_k, \Delta_k)$. This contradiction proves termination.

*Corollary 9.3.12.* By Theorem 9.3.11 the program stops, either with $\lambda_i = 0$ or with a Mori fibre space. In the first case $\phi_i$ is a log terminal model by Proposition 9.3.10, and $K_X + \Delta$ is pseudo-effective over $U$: on a common resolution $p \colon W \to X$, $q \colon W \to X_i$, $p^*(K_X + \Delta) = q^*(K_{X_i} + \Delta_i) + E$ with $E \ge 0$ by the discrepancy inequality, and the pushforward to $X$ of a nef divisor plus an effective one is pseudo-effective. In the second case $K_{X_i} + \Delta_i$ is negative on the curves of a covering family, the fibres of $\varphi_i$, so it is not pseudo-effective over $U$; as $\phi_i$ is a birational contraction, $K_{X_i} + \Delta_i = \phi_{i*}(K_X + \Delta)$, and the pushforward of a pseudo-effective divisor is pseudo-effective, so $K_X + \Delta$ is not pseudo-effective. The two cases are therefore distinguished by the pseudo-effectivity of $K_X + \Delta$.

*Theorem 9.3.13.* An outline, following BCHM10, Section 5. Let $(X, \Delta)$ be klt with $\Delta$ big and $K_X + \Delta \sim_{\mathbb{R}, U} D \ge 0$.

1. *Reduction.* Passing to a log resolution and adding exceptional divisors, one may assume that $X$ is smooth, the support of $\Delta + D$ has simple normal crossings and $\Delta$ is of the form $A + B$ with $A$ general ample; a log terminal model of the new pair gives one of the old.
2. *A dlt pair with the support of $D$ in the boundary.* Let $S$ be the sum of the components of $D$ and choose $\Delta' = \Delta + aS$ with the coefficients of $\Delta'$ in $S$ equal to $1$ where possible, so that $(X, \Delta')$ is dlt and $K_X + \Delta' \sim_{\mathbb{R}, U} D + aS$ is supported in $\lfloor \Delta' \rfloor$, after a further perturbation that does not change the log terminal models.
3. *Run the program with scaling.* Run the $(K_X + \Delta')$-program with scaling of an ample divisor. The flips exist: each flipping contraction is, after a perturbation, a pl flipping contraction with respect to a component of $\lfloor \Delta' \rfloor$ that is negative on the flipping curves, because $K_X + \Delta'$ is supported on $\lfloor \Delta' \rfloor$; so $A_n$ applies.
4. *Special termination.* By Theorem 9.3.4, which uses $B_n$, after finitely many steps the flipping loci are disjoint from $\lfloor \Delta' \rfloor$. But every flipping curve is $(K_X + \Delta')$-negative, and $K_X + \Delta'$ is supported on $\lfloor \Delta' \rfloor$, so a flipping curve disjoint from $\lfloor \Delta' \rfloor$ would have intersection number zero. So the program terminates, with a log terminal model of $K_X + \Delta'$.
5. *Back to $\Delta$.* A log terminal model of $K_X + \Delta'$ with the support of $D$ removed again gives a log terminal model of $K_X + \Delta$, by a second program with scaling that removes the extra boundary $aS$; its termination uses the same argument.

### Exercises

1. (A) In Example 9.3.14 check that $H$ is ample and that $K + \frac23 H_1$ is nef but not ample on $\mathbb{P}^1 \times \mathbb{P}^1$.
2. (A) Run the $K$-program with scaling of $H = 4L - E_1 - 2E_2$ on the plane blown up at two points, and find the thresholds and the models.
3. (B) Show that in Lemma 9.3.7 the hypothesis that $D$ and $C_i$ are $\mathbb{Q}$-divisors can be replaced by the assumption that $C_i$ is a $\mathbb{Q}$-divisor and $D$ an $\mathbb{R}$-divisor with finitely many $D$-negative extremal rays.
4. (B) Show that the conclusion of Proposition 9.3.10 can fail for $t > \lambda_{i-1}$: find an example on a surface where $\phi_i$ is not a weak log canonical model of $K_X + \Delta + tC$ for some $t > \lambda_{i-1}$.
5. (B) Show that in the proof of Theorem 9.3.11 the isomorphism $X_i \to X_k$ also carries $C_i$ to $C_k$, and deduce directly from Lemma 9.3.8 that $\lambda_i = \lambda_k$.
6. (C) Show that a $K$-program with scaling of an ample divisor on a smooth projective surface $X$ with $K_X$ not pseudo-effective ends with $\mathbb{P}^2 \to \mathrm{pt}$ or with a $\mathbb{P}^1$-bundle over a curve, and that the last threshold is $3 / \deg H_k$ in the first case and $2 / (H_k \cdot f)$ for a fibre $f$ in the second.

### Lean

The library defines one step of the program with scaling as `MinimalModel.IsScalingStep` and states the termination of the program with scaling for a big boundary as `MinimalModel.TerminationScalingBig`. Both are definitions without proofs; the second has the shape of Theorem 9.3.11 without the hypothesis $E_n$, which in the library is not stated separately.

### Notes and history

The program with scaling appears in Shokurov's work and is the program of BCHM10, Section 3.10, where Lemma 9.3.7, Lemma 9.3.8 and Proposition 9.3.10 are proved. The termination for a big boundary from the finiteness of models, Theorem 9.3.11, is the core of the BCHM10 strategy: termination is not proved by a decreasing invariant but by the finiteness of the models the program can visit. Birkar, Bir12, extends termination with scaling to some pseudo-effective cases and uses it for the existence of log minimal models of lc pairs. The implication $A_n + B_n \Rightarrow C_n$, Theorem 9.3.13, is BCHM10, Section 5; the trick of putting the support of $D$ into the reduced boundary, so that the program is forced to stop near it, is due to Hacon and McKernan and to Shokurov.
