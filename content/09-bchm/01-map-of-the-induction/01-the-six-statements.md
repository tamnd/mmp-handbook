---
title: The six statements and the induction
nodes: [MM9399B0QP]
sources: [BCHM10, HM07, Cor07, KM98]
reads_with: [BCHM10:1, Cor07:2]
requires: [1.3, 1.5, 4.2, 7.2, 7.4, 8.1, 8.3, P7.7]
level: advanced
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The six statements and the induction

### Statement

The ground field $k$ is algebraically closed of characteristic $0$. Throughout, $\pi \colon X \to U$ is a projective morphism from a normal variety to a normal quasi-projective variety. Divisors are $\mathbb{R}$-divisors, as in BCHM10, and $\sim_{\mathbb{R}, U}$ is $\mathbb{R}$-linear equivalence over $U$: $D \sim_{\mathbb{R}, U} D'$ if $D - D'$ is an $\mathbb{R}$-linear combination of principal divisors and pullbacks of $\mathbb{R}$-Cartier divisors from $U$. Every example of the volume has rational coefficients, and on a first reading all coefficients may be taken rational, so that the results of Volumes 4, 7 and 8 apply as stated there. Discrepancies $a(F, X, \Delta)$ are those of Volume 4, so that a prime divisor $F$ on $X$ has $a(F, X, \Delta) = -\operatorname{mult}_F \Delta$.

**Definition 9.1.1 (models).** Let $(X, \Delta)$ be a log canonical pair, projective over $U$. A *birational contraction* is a birational map $\varphi \colon X \dashrightarrow Y$ over $U$ to a normal variety projective over $U$ whose inverse contracts no divisor: every prime divisor of $Y$ is the strict transform of a prime divisor of $X$. A prime divisor of $X$ whose strict transform is not a divisor of $Y$ is *$\varphi$-exceptional*. Put $\Gamma = \varphi_* \Delta$ and suppose $K_Y + \Gamma$ is $\mathbb{R}$-Cartier.

1. $Y$ is a *weak log canonical model* of $K_X + \Delta$ over $U$ if $K_Y + \Gamma$ is nef over $U$ and $a(F, X, \Delta) \le a(F, Y, \Gamma)$ for every $\varphi$-exceptional prime divisor $F$ of $X$.
2. $Y$ is a *log terminal model* of $K_X + \Delta$ over $U$ if it is a weak log canonical model, $Y$ is $\mathbb{Q}$-factorial, $(Y, \Gamma)$ is dlt, and $a(F, X, \Delta) < a(F, Y, \Gamma)$ for every $\varphi$-exceptional prime divisor $F$.
3. $Y$ is a *log canonical model* of $K_X + \Delta$ over $U$ if it is a weak log canonical model and $K_Y + \Gamma$ is ample over $U$.

**Definition 9.1.2 (general ample divisors and the sets $\mathcal{L}_A(V)$).** Let $V$ be a finite dimensional affine subspace of the real vector space of Weil $\mathbb{R}$-divisors on $X$, *defined over $\mathbb{Q}$*: a translate of a subspace spanned by integral divisors by a $\mathbb{Q}$-divisor. A $\mathbb{Q}$-divisor $A \ge 0$ is a *general ample $\mathbb{Q}$-divisor over $U$* if $A = \frac1m A'$, where $A'$ is a very general member of a linear system $|D|$ with $D$ very ample over $U$; how general depends on the data that come before $A$. For such $A$,
$$\mathcal{L}_A(V) = \{\Delta = A + B : B \in V, \ B \ge 0, \ (X, \Delta) \text{ is log canonical}\}, \qquad \mathcal{E}_{A}(V) = \{\Delta \in \mathcal{L}_A(V) : K_X + \Delta \text{ is pseudo-effective over } U\}.$$
Both are rational polytopes (BCHM10, Lemma 3.7.2 for $\mathcal{L}_A(V)$; Chapter 4 for $\mathcal{E}_A(V)$).

**Theorem 9.1.3 (Birkar, Cascini, Hacon and McKernan).** Let $(X, \Delta)$ be a klt pair, projective over $U$, and suppose that $\Delta$ is big over $U$ and $K_X + \Delta$ is pseudo-effective over $U$, or that $K_X + \Delta$ is big over $U$. Then:

1. $K_X + \Delta$ has a log terminal model over $U$;
2. if $K_X + \Delta$ is big over $U$, it has a log canonical model over $U$;
3. if $K_X + \Delta$ is $\mathbb{Q}$-Cartier, the $\mathcal{O}_U$-algebra $R(\pi, K_X + \Delta) = \bigoplus_{m \ge 0} \pi_* \mathcal{O}_X(\lfloor m(K_X + \Delta) \rfloor)$ is finitely generated.

Lean: not yet in Lean.

The proof is the induction on $n = \dim X$ of the following six statements, in the form of BCHM10, Section 1, with the notation of this volume.

**Theorem 9.1.4 ($A_n$, existence of pl flips).** Let $f \colon X \to Z$ be a pl flipping contraction of an $n$-dimensional pair $(X, S + B)$ in the sense of Definition 8.3.1. Then the flip of $f$ exists.

Lean: not yet in Lean.

**Theorem 9.1.5 ($B_n$, special finiteness).** Let $\dim X = n$, let $V$ be as in Definition 9.1.2, let $S_1, \dots, S_k$ be distinct prime divisors with $S = \sum_i S_i$, and let $A$ be a general ample $\mathbb{Q}$-divisor over $U$. Let $\mathcal{C} \subseteq \mathcal{L}_{S + A}(V)$ be a rational polytope such that $(X, \Delta)$ is dlt for every $\Delta \in \mathcal{C}$. Then there are finitely many birational maps $\varphi_j \colon X \dashrightarrow Z_j$ over $U$, $1 \le j \le l$, such that for every weak log canonical model $\varphi \colon X \dashrightarrow Z$ of $K_X + \Delta$ over $U$ with $\Delta \in \mathcal{C}$ that contracts no component of $S$, there is an index $j$ for which the induced birational map $Z_j \dashrightarrow Z$ is an isomorphism near the strict transform of $S$.

Lean: not yet in Lean.

**Theorem 9.1.6 ($C_n$, existence of log terminal models).** Let $(X, \Delta)$ be an $n$-dimensional klt pair, projective over $U$, with $\Delta$ big over $U$. If $K_X + \Delta \sim_{\mathbb{R}, U} D$ for some $\mathbb{R}$-divisor $D \ge 0$, then $K_X + \Delta$ has a log terminal model over $U$.

Lean: not yet in Lean.

**Theorem 9.1.7 ($D_n$, nonvanishing).** Let $(X, \Delta)$ be an $n$-dimensional klt pair, projective over $U$, with $\Delta$ big over $U$. If $K_X + \Delta$ is pseudo-effective over $U$, then $K_X + \Delta \sim_{\mathbb{R}, U} D$ for some $\mathbb{R}$-divisor $D \ge 0$.

Lean: not yet in Lean.

**Theorem 9.1.8 ($E_n$, finiteness of models).** Let $\dim X = n$, suppose $X$ carries a klt pair $(X, \Delta_0)$, and let $V$ and a general ample $\mathbb{Q}$-divisor $A$ over $U$ be as in Definition 9.1.2. Then there are finitely many birational maps $\psi_j \colon X \dashrightarrow Z_j$ over $U$, $1 \le j \le l$, such that every weak log canonical model $\psi \colon X \dashrightarrow Z$ of $K_X + \Delta$ over $U$, for some $\Delta \in \mathcal{L}_A(V)$, is $\xi \circ \psi_j$ for some $j$ and some isomorphism $\xi \colon Z_j \to Z$.

Lean: not yet in Lean.

**Theorem 9.1.9 ($F_n$, finite generation).** Let $U$ be affine and let $(X, \Delta = A + B)$ be an $n$-dimensional klt pair, projective over $U$, where $A \ge 0$ is a general ample $\mathbb{Q}$-divisor over $U$ and $B \ge 0$. Suppose $K_X + \Delta$ is pseudo-effective over $U$, let $V$ be the span of the components of $\Delta$, and let $W \subseteq V$ be the smallest affine subspace defined over $\mathbb{Q}$ that contains $\Delta$. Then:

1. $K_X + \Delta$ has a log terminal model over $U$, and if $K_X + \Delta$ is $\mathbb{Q}$-Cartier then $R(\pi, K_X + \Delta)$ is finitely generated;
2. there is $\delta > 0$ such that every prime divisor in the stable base locus $\mathbf{B}(K_X + \Delta)$ lies in $\mathbf{B}(K_X + \Xi)$ for every $\Xi \in \mathcal{L}_A(V)$ with $\lVert \Xi - \Delta \rVert < \delta$;
3. there are $\eta > 0$ and an integer $r > 0$ such that for every $\Xi \in W$ with $\lVert \Xi - \Delta \rVert < \eta$ and every integer $m > 0$ with $m(K_X + \Xi)/r$ Cartier, every component of the fixed divisor of $|m(K_X + \Xi)|$ over $U$ is a component of $\mathbf{B}(K_X + \Delta)$.

Lean: not yet in Lean.

Here $\lVert \cdot \rVert$ is the sup norm on the coefficients, and $\mathbf{B}$ is the stable base locus of Definition P7.7.12, read over $U$.

**Theorem 9.1.10 (the induction).** Let $n \ge 2$.

1. $F_{n-1}$ implies $A_n$ (Chapter 2).
2. $E_{n-1}$ implies $B_n$ (Chapter 3).
3. $A_n$ and $B_n$ imply $C_n$ (Chapter 3).
4. $D_{n-1}$, $B_n$ and $C_n$ imply $D_n$ (Chapter 4).
5. $C_n$ and $D_n$ imply $E_n$ (Chapter 4).
6. $C_n$ and $D_n$ imply $F_n$ (Chapter 5).

Lean: not yet in Lean.

**Lemma 9.1.11 (dimension one).** The statements $A_1$ to $F_1$ hold.

Lean: not yet in Lean.

**Corollary 9.1.12 (the six statements hold).** Granting Theorem 9.1.10, the statements $A_n$ to $F_n$ hold for every $n \ge 1$, and Theorem 9.1.3 holds.

Lean: not yet in Lean.

**Lemma 9.1.13 (sections on a weak log canonical model).** Let $\varphi \colon X \dashrightarrow Y$ be a weak log canonical model of $K_X + \Delta$ over $U$, with $\Gamma = \varphi_* \Delta$, and let $p \colon W \to X$ and $q \colon W \to Y$ be a common resolution. Then $p^*(K_X + \Delta) = q^*(K_Y + \Gamma) + E$ with $E \ge 0$ and $q$-exceptional, $a(G, X, \Delta) \le a(G, Y, \Gamma)$ for every divisor $G$ over $X$, and for every integer $m \ge 0$ such that $m(K_X + \Delta)$ and $m(K_Y + \Gamma)$ are Cartier,
$$\pi_* \mathcal{O}_X(m(K_X + \Delta)) = \pi_{Y*} \mathcal{O}_Y(m(K_Y + \Gamma))$$
as subsheaves of the constant sheaf $k(X)$ on $U$, where $\pi_Y \colon Y \to U$ is the structure morphism.

Lean: not yet in Lean.

The six statements are theorems of BCHM10, and Theorem 9.1.10 is the plan of their proof there. Lemma 9.1.11, Corollary 9.1.12 and Lemma 9.1.13 are proved in full below; Theorem 9.1.10 is the content of Chapters 2 to 5.

### Proof in words

A weak log canonical model is the output of a program that never makes $K_X + \Delta$ worse: the divisors it contracts have discrepancy at least as large on $Y$ as on $X$. The negativity lemma upgrades this to every divisor over $X$, and so the pluri-log-canonical sections on $X$ and on $Y$ are the same. That is the reason why the existence of a model with $K_Y + \Gamma$ nef and big gives finite generation: on $Y$ the base point free theorem applies.

The six statements feed each other. A pl flip is controlled by an algebra of sections on its plt centre $S$, of dimension $n - 1$, and finite generation in dimension $n - 1$ gives it ($F_{n-1} \Rightarrow A_n$). Running a program with scaling needs flips, which exist by Shokurov's reduction once pl flips do, and needs termination near the reduced boundary, which is special finiteness, a statement about models of the components of $S$, so of dimension $n - 1$ ($E_{n-1} \Rightarrow B_n$ and $A_n + B_n \Rightarrow C_n$). Nonvanishing is proved by cutting down to a log canonical centre and using the models of the previous statements ($D_n$). Once models exist and $K_X + \Delta$ is effective, the space of boundaries breaks into finitely many chambers with one model each ($E_n$), and on a log terminal model the canonical ring is the ring of a semiample divisor ($F_n$). In dimension $1$ every birational contraction is an isomorphism and every statement reduces to degrees on a curve.

### Examples

**Example 9.1.14 (models of a blown up plane).** Let $X$ be the blow-up of $\mathbb{P}^2$ at a point $p$, with exceptional curve $E$ and $L$ the pullback of a line, and let $G_1, G_2, G_3$ be general conics of $\mathbb{P}^2$, which miss $p$ and meet transversally; write $G_i$ also for their pullbacks. Put $\Delta = \frac23 (G_1 + G_2 + G_3)$. Then $(X, \Delta)$ is klt, $\Delta \equiv 4L$ is big, and $K_X + \Delta \equiv -3L + E + 4L = L + E$. Since $(L + E) \cdot E = -1$, the divisor $K_X + \Delta$ is not nef. Let $\varphi \colon X \to Y = \mathbb{P}^2$ be the blow-down and $\Gamma = \varphi_* \Delta$. Then $K_Y + \Gamma \equiv L$ is ample, $a(E, X, \Delta) = 0$ because $E \not\subseteq \operatorname{Supp} \Delta$, and $a(E, Y, \Gamma) = 1$ because $\Gamma$ misses $p$. So $Y$ is a log terminal model and the log canonical model of $K_X + \Delta$.

Now let $G_i'$ be general conics through $p$, with strict transforms $G_i' \sim 2L - E$, and $\Delta' = \frac23 (G_1' + G_2' + G_3')$. Then $(X, \Delta')$ is klt, as the $G_i'$ meet transversally and have distinct tangents at $p$, and $K_X + \Delta' \equiv -3L + E + 4L - 2E = L - E$, the class of the ruling of $X$ over $\mathbb{P}^1$. It is nef and not big. So $X$ is its own log terminal model, and $K_X + \Delta'$ has no log canonical model that is birational to $X$: it is not big, and part 2 of Theorem 9.1.3 does not apply.

**Example 9.1.15 (a polytope of boundaries on the line).** Let $X = \mathbb{P}^1$ over $U = \operatorname{Spec} k$, let $p_1, p_2$ be points, $V = \{b_1 p_1 + b_2 p_2 : b_1, b_2 \in \mathbb{R}\}$, and $A = \frac12 q$ for a general point $q$, a general ample $\mathbb{Q}$-divisor with $D = q$ and $m = 2$. A divisor $A + b_1 p_1 + b_2 p_2$ is lc if and only if $0 \le b_i \le 1$, so $\mathcal{L}_A(V)$ is the unit square in the coordinates $(b_1, b_2)$. On $\mathbb{P}^1$ a divisor is pseudo-effective if and only if its degree is at least $0$, and $\deg (K + A + b_1 p_1 + b_2 p_2) = b_1 + b_2 - \frac32$, so $\mathcal{E}_A(V)$ is the triangle $b_1 + b_2 \ge \frac32$ in the square, a rational polytope. Every weak log canonical model is the identity of $\mathbb{P}^1$, and $E_1$ holds with $l = 1$.

**Example 9.1.16 (the arrows in dimension 3).** For $n = 3$, $A_3$ is Shokurov's theorem on 3-fold pl flips, Theorem 8.3.9, and Theorem 8.3.10 gives 3-fold klt flips. The arrow $F_2 \Rightarrow A_3$ of part 1 of Theorem 9.1.10 is a second proof of it: the restricted algebra on the surface $S$ is an adjoint algebra of a klt surface pair with big boundary, which is finitely generated by Zariski decomposition, and Chapter 5 computes such an algebra by hand. Special termination in dimension 3, Theorem 8.4.20, is the form of $B_3$ that Volume 8 uses: the restriction of the program to a component of the boundary is a sequence of contractions of curves on a surface.

### Proof

*Lemma 9.1.13.* The question is local over $U$, so let $U$ be affine. Put $E = p^*(K_X + \Delta) - q^*(K_Y + \Gamma)$. As $\varphi$ is a birational contraction, $q_* p^*$ is the pushforward $\varphi_*$ on divisors, so $q_* E = (K_Y + \Gamma) - (K_Y + \Gamma) = 0$ and $E$ is $q$-exceptional. Write $K_W = p^*(K_X + \Delta) + \sum_G a(G, X, \Delta) G$ and $K_W = q^*(K_Y + \Gamma) + \sum_G a(G, Y, \Gamma) G$ over the prime divisors $G$ of $W$, so that $\operatorname{mult}_G E = a(G, Y, \Gamma) - a(G, X, \Delta)$. For $G$ not $p$-exceptional, $p(G)$ is a prime divisor of $X$: if it is not $\varphi$-exceptional, $G$ is not $q$-exceptional and the coefficient is $0$; if it is, the coefficient is at least $0$ by the definition of a weak log canonical model. So $p_* E \ge 0$. The divisor $-E \equiv_X q^*(K_Y + \Gamma)$ is nef over $X$: a curve contracted by $p$ maps to a point of $U$, and $K_Y + \Gamma$ is nef over $U$. The negativity lemma, Theorem 1.5.22, applied to $p$ and $-E$, gives $E \ge 0$, and so $a(G, X, \Delta) \le a(G, Y, \Gamma)$ for every prime divisor $G$ on $W$. Every divisor over $X$ appears on a higher common resolution, where the same argument applies.

For the sections, let $m(K_X + \Delta)$ and $m(K_Y + \Gamma)$ be Cartier. Then $mE = p^* m(K_X + \Delta) - q^* m(K_Y + \Gamma)$ is an integral divisor. Since $p_* \mathcal{O}_W = \mathcal{O}_X$, the projection formula gives $H^0(X, m(K_X + \Delta)) = H^0(W, p^* m(K_X + \Delta)) = H^0(W, q^* m(K_Y + \Gamma) + mE)$. A rational function $g$ with $\operatorname{div}(g) + q^* m(K_Y + \Gamma) + mE \ge 0$ has $\operatorname{div}(g) + m(K_Y + \Gamma) \ge 0$ on $Y$, since $q_* mE = 0$, and conversely a section on $Y$ pulls back to a section of $q^* m(K_Y + \Gamma) \le q^* m(K_Y + \Gamma) + mE$. So both spaces equal $H^0(Y, m(K_Y + \Gamma))$ inside $k(X)$.

*Lemma 9.1.11.* Let $\dim X = 1$. A birational map of normal curves projective over $U$ is an isomorphism, so every birational contraction from $X$ is an isomorphism and has no exceptional divisors. There is no small birational morphism $X \to Z$ of normal curves with nonempty exceptional set, so $A_1$ is empty. In $B_1$ and $E_1$ every weak log canonical model is $X$ itself up to a unique isomorphism, and $l = 1$ works. For $C_1$, $D_1$ and $F_1$, either $\pi$ is finite, or $U$ is a point of $\pi(X)$ after replacing $U$ by the image, which is a point or a curve. If $\pi(X)$ is a curve, $\pi$ is finite onto it, every divisor on $X$ is ample over $U$, and the identity is a log terminal model of $K_X + \Delta$; it is $\sim_{\mathbb{R}, U}$ to an effective divisor because adding the pullback of a sufficiently ample divisor on $\pi(X)$ makes its degree large. The algebra $R(\pi, K_X + \Delta)$ is then the algebra of a relatively ample $\mathbb{Q}$-divisor, finitely generated over $\mathcal{O}_U$ by the relative form of the finite generation of the section ring of an ample divisor (Har77; Lemma 8.1.5 handles the passage to a Veronese subalgebra). If $U$ is a point, $X$ is a smooth projective curve. For $D_1$: $K_X + \Delta$ pseudo-effective means $\deg(K_X + \Delta) \ge 0$; if the degree is positive, $K_X + \Delta$ is ample and $\mathbb{R}$-linearly equivalent to an effective divisor; if it is $0$, then $\deg K_X = -\deg \Delta < 0$ because $\Delta$ is big, so $X \cong \mathbb{P}^1$, where a divisor of degree $0$ is $\sim_{\mathbb{R}} 0$. For $C_1$: a divisor $\sim_{\mathbb{R}}$ to an effective one has degree at least $0$, so it is nef, and $X$ is its own log terminal model. For $F_1$: in the case of positive degree the ring is the section ring of an ample $\mathbb{Q}$-divisor, and in the case of degree $0$ on $\mathbb{P}^1$ with $K_X + \Delta$ a $\mathbb{Q}$-divisor, $r(K_X + \Delta) \sim 0$ for some $r > 0$ and the ring is $k[t]$ with $t$ in degree $r$; both are finitely generated. In both cases $K_X + \Delta$ is ample or $\mathbb{R}$-linearly trivial, so $\mathbf{B}(K_X + \Delta) = \emptyset$ and part 2 is empty. For part 3 take $r = 2g(X) + 1$: if $m(K_X + \Xi) = rD_0$ with $D_0$ Cartier and $|m(K_X + \Xi)| \neq \emptyset$, then either $\deg D_0 \ge 1$, so that $\deg m(K_X + \Xi) \ge 2g(X) + 1$ and the linear system is free, or $\deg D_0 = 0$ and $m(K_X + \Xi) \sim 0$; in neither case is there a fixed divisor.

*Corollary 9.1.12.* By induction on $n$. For $n = 1$ this is Lemma 9.1.11. Let $n \ge 2$ and suppose $A_m$ to $F_m$ for all $m < n$. Part 1 of Theorem 9.1.10 gives $A_n$, part 2 gives $B_n$, part 3 then gives $C_n$, part 4 gives $D_n$ from $D_{n-1}$, $B_n$ and $C_n$, and parts 5 and 6 give $E_n$ and $F_n$. No part uses a statement in dimension $n$ that is not already proved at that point, so the induction closes.

For Theorem 9.1.3, let $\dim X = n$. Suppose first $\Delta$ big over $U$ and $K_X + \Delta$ pseudo-effective over $U$. By $D_n$, $K_X + \Delta \sim_{\mathbb{R}, U} D \ge 0$, and by $C_n$ it has a log terminal model, which is part 1. Suppose next $K_X + \Delta$ big over $U$. By Kodaira's lemma over $U$ (Lemma 5.1.9 for $\mathbb{Q}$-divisors, and its $\mathbb{R}$-form, BCHM10, Section 3), $K_X + \Delta \sim_{\mathbb{R}, U} H + G$ with $H$ ample over $U$ and $G \ge 0$. For $0 < \varepsilon \ll 1$ and $H' \sim_{\mathbb{R}, U} H$ a general effective divisor, the pair $(X, \Delta' = \Delta + \varepsilon(H' + G))$ is klt, $\Delta'$ is big over $U$, and $K_X + \Delta' \sim_{\mathbb{R}, U} (1 + \varepsilon)(K_X + \Delta)$. A weak log canonical model, a log terminal model or a log canonical model of $K_X + \Delta'$ over $U$ is one of $K_X + \Delta$, because the conditions of Definition 9.1.1 depend only on the class of the divisor up to $\sim_{\mathbb{R}, U}$ and a positive multiple: the discrepancy differences in the proof of Lemma 9.1.13 are unchanged when a principal divisor or a pullback from $U$ is added, since $p^*$ and $q^*$ of such a divisor agree on $W$. So part 1 follows from the first case. For part 2, let $\varphi \colon X \dashrightarrow Y$ be a log terminal model. By Lemma 9.1.13, $a(G, Y, \Gamma) \ge a(G, X, \Delta) > -1$ for every divisor $G$ over $X$, so $(Y, \Gamma)$ is klt, and $K_Y + \Gamma$ is nef over $U$ and big over $U$, as $K_X + \Delta$ is. By the base point free theorem (Corollary 7.2.5, in its relative form over $U$, and BCHM10, Section 3, for $\mathbb{R}$-divisors) it is semiample over $U$, and the morphism over $U$ that it defines is the log canonical model. For part 3, by Lemma 9.1.13 the algebra $R(\pi, K_X + \Delta)$ has a Veronese subalgebra equal to that of $K_Y + \Gamma$ on a log terminal model, which is finitely generated: if $\Delta$ is big, write $\Delta \sim_{\mathbb{R}, U} A + B$ as in Theorem 9.1.9 after the perturbation above and apply part 1 of $F_n$ locally over $U$; if $K_X + \Delta$ is big, $K_Y + \Gamma$ is semiample and the algebra is that of a semiample divisor. Lemma 8.1.5 removes the Veronese.

*Theorem 9.1.10, where each arrow is proved.* Part 1 is Theorem 9.2.14 of Chapter 2: the restricted algebra of a pl flipping contraction is identified, by the extension theorem of Hacon and McKernan, with an adjoint algebra of a klt pair $(S, \Theta)$ of dimension $n - 1$ with big boundary, which part 1 of $F_{n-1}$ shows to be finitely generated, once parts 2 and 3 of $F_{n-1}$ show that $\Theta$ is rational. Part 2 is in Chapter 3: special finiteness is finiteness of models on the components of $S$, by adjunction. Part 3 is in Chapter 3: a program with scaling of an ample divisor exists by $A_n$ and Shokurov's reduction, and special termination, deduced from $B_n$, makes it stop. Parts 4 and 5 are in Chapter 4, and part 6 is in Chapter 5. The arguments are those of BCHM10, Sections 4 to 8.

### Exercises

1. (A) In Example 9.1.14, check that $(L + E)^2 = 0$, and use it to show that $K_X + \Delta$ is big but not nef.
2. (A) In Example 9.1.15, find all $\Delta \in \mathcal{L}_A(V)$ for which $K + \Delta$ is ample, and all for which it is numerically trivial.
3. (B) Let $\varphi \colon X \to Y$ be the blow-down of Example 9.1.14 and $\Delta_b = \Delta + bE$ for $0 \le b < 1$. For which $b$ is $Y$ a log terminal model of $K_X + \Delta_b$, and for which $b$ only a weak log canonical model? Compute $K_X + \Delta_b = \varphi^*(K_Y + \Gamma) + cE$ and the sign of $c$.
4. (B) Show that a log canonical model of $K_X + \Delta$ over $U$ is unique up to isomorphism when it exists, using Lemma 9.1.13 and the fact that $Y = \operatorname{\mathbf{Proj}}_U R(\pi_Y, K_Y + \Gamma)$ for $K_Y + \Gamma$ ample over $U$.
5. (B) Show that the conditions of Definition 9.1.1 are unchanged when $K_X + \Delta$ is replaced by a divisor $K_X + \Delta'$ with $\Delta' - \Delta \sim_{\mathbb{R}, U} 0$, as used in the proof of Corollary 9.1.12.
6. (C) Let $X$ be the blow-up of $\mathbb{P}^2$ at two points with exceptional curves $E_1, E_2$, and $\Delta = \frac23 (G_1 + G_2 + G_3)$ for three general conics. Find the log terminal model and the log canonical model of $K_X + \Delta$, and check Lemma 9.1.13 for $m = 3$ by computing $h^0(X, 3(K_X + \Delta))$ and $h^0(\mathbb{P}^2, 3(K_Y + \Gamma))$.

### Lean

The library states the main theorem as `MinimalModel.BCHM`, with the hypothesis on $\Delta$ or on $K + \Delta$ as a disjunction as in Theorem 9.1.3, the finiteness of models as `MinimalModel.FinitenessOfModels`, in the form of Theorem 9.1.8 over an uncountable field, and two corollaries, `MinimalModel.KltFlips` and `MinimalModel.FiniteGenerationCanonical`. These are statements, with no proofs. The six statements $A_n$ to $F_n$ and Theorem 9.1.10 are not stated in Lean: the library treats them as steps of a proof, not as results.

### Notes and history

The induction is that of BCHM10, which appeared as a preprint in 2006. Its arrows reorganise the earlier work: Shokurov's reduction of klt flips to pl flips and special termination (Sho92, with the account in Cor07), the extension theorems of Siu, Kawamata, Takayama and Hacon and McKernan, which gave pl flips in dimension $n$ from the minimal model program in dimension $n - 1$ (HM07), and the observation of BCHM that the program with scaling needs only the finiteness of models to terminate when the boundary is big. Theorems 9.1.4 to 9.1.9 follow the statements of BCHM10, Section 1, with simplified notation; the hypotheses on the base $U$, which BCHM take affine in some of the statements, and the generality conditions on $A$ should be checked against the source before use. Corti, Kaloghiros and Lazić give a shorter account of the existence of flips by the same induction, and Hacon and Kovács a textbook account. The route of Cascini and Lazić and of Corti and Lazić, which proves finite generation first and avoids the program, is outlined in Chapter 6.
