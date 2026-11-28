---
title: Terminal models
nodes: []
sources: [KM98, Rei83b, Kaw88, Kol92]
reads_with: [KM98:6.3, Rei83b:main]
requires: [1.5, 3.5, 4.2, 4.4, P8.13]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Terminal models

### Statement

A canonical 3-fold need not be terminal or $\mathbb{Q}$-factorial, and the program of Section 1 needs both. This section shows that nothing is lost: a canonical 3-fold has a crepant model that is terminal and $\mathbb{Q}$-factorial, and a terminal 3-fold has a small one. The ground field is algebraically closed of characteristic $0$.

**Definition 8.5.10 (terminal models and $\mathbb{Q}$-factorializations).** Let $X$ be a normal quasi-projective variety with $K_X$ $\mathbb{Q}$-Cartier. A *crepant terminal model* of $X$ is a projective birational morphism $g \colon Y \to X$ such that $Y$ is $\mathbb{Q}$-factorial and terminal and $K_Y = g^* K_X$. A *$\mathbb{Q}$-factorialization* of $X$ is a small projective birational morphism $g \colon Y \to X$ with $Y$ $\mathbb{Q}$-factorial.

**Theorem 8.5.11 (crepant terminal models of canonical 3-folds).** Let $X$ be a quasi-projective canonical 3-fold. Then $X$ has a crepant terminal model $g \colon Y \to X$.

Lean: not yet in Lean.

**Proposition 8.5.12 (the exceptional divisors of a crepant terminal model).** Let $X$ be a canonical 3-fold and $g \colon Y \to X$ a crepant terminal model. The $g$-exceptional prime divisors are exactly the exceptional divisors $E$ over $X$ with $a(E, X) = 0$. In particular their number is finite and does not depend on $g$.

Lean: not yet in Lean.

**Corollary 8.5.13 (small $\mathbb{Q}$-factorializations of terminal 3-folds).** Let $X$ be a quasi-projective terminal 3-fold. Then $X$ has a $\mathbb{Q}$-factorialization $g \colon Y \to X$ with $Y$ terminal and $K_Y = g^* K_X$. If $X$ is $\mathbb{Q}$-factorial, every small projective birational morphism $Y \to X$ is an isomorphism.

Lean: not yet in Lean.

### Proof in words

Resolve $X$ and run the program of Section 1 over $X$. Over a birational base the program can only end with a minimal model, so its output $Y$ has $K_Y$ nef over $X$. The difference $K_Y - g^* K_X$ is effective, because $X$ is canonical and the program only pushes divisors forward, and it is nef over $X$ and exceptional, so the negativity lemma forces it to be zero. The divisors that survive on $Y$ are those of discrepancy $0$, and all of them must survive, since a divisor of discrepancy $0$ that is exceptional over $Y$ would contradict that $Y$ is terminal. For terminal $X$ there are no divisors of discrepancy $0$, so $Y \to X$ is small.

### Examples

**Example 8.5.14 (the ordinary double point).** Let $X = \{xy = zw\} \subset \mathbb{A}^4$, terminal by Example 4.4.20. Let $g \colon Y \to X$ be the blow-up of the plane $D = \{x = z = 0\}$, a small resolution with exceptional curve $C \cong \mathbb{P}^1$ and $N_{C/Y} = \mathcal{O}(-1)^{\oplus 2}$, as in Example 3.5.23. The ideal of $D$ becomes invertible on $Y$, equal to $\mathcal{O}_Y(-D_Y)$, and it is $g$-ample, so $D_Y \cdot C = -1$. If $mD$ were Cartier on $X$, then $m D_Y = g^*(mD)$ would have degree $0$ on $C$. So $D$ is not $\mathbb{Q}$-Cartier and $X$ is not $\mathbb{Q}$-factorial. Both $Y$ and the blow-up $Y'$ of $D' = \{x = w = 0\}$ are $\mathbb{Q}$-factorializations of $X$, and since $D + D' = \operatorname{div}(x)$, $D'_Y \cdot C = 1$. The two are related by the Atiyah flop: $\mathbb{Q}$-factorializations are not unique.

**Example 8.5.15 (a curve of $A_1$ points).** Let $X = S \times \mathbb{A}^1$ with $S$ the surface point $A_1$, canonical and not terminal by Example 4.4.21. The minimal resolution $\tilde S \to S$ has one exceptional curve $C$ with discrepancy $0$, and $g \colon \tilde S \times \mathbb{A}^1 \to X$ is a crepant terminal model, with the single exceptional divisor $C \times \mathbb{A}^1$. By Proposition 8.5.12, $C \times \mathbb{A}^1$ is the only divisor over $X$ with discrepancy $0$.

**Example 8.5.16 (the point $\frac13(1,1,1)$).** Let $X = \mathbb{A}^3 / \mu_3$ with weights $(1,1,1)$. The matrix $\zeta \cdot I_3$ has determinant $\zeta^3 = 1$, so $X$ is Gorenstein. The blow-up of the origin is $Y$, the total space of $\mathcal{O}_{\mathbb{P}^2}(-3)$, with exceptional divisor $E \cong \mathbb{P}^2$ and $a(E, X) = \frac{1 + 1 + 1}{3} - 1 = 0$ by Theorem 3.3.34. Since $Y$ is smooth, $g \colon Y \to X$ is a crepant terminal model, $X$ is canonical and not terminal, and $E$ is its only crepant divisor. For a line $\ell \subset E$, $K_Y \cdot \ell = 0$: the morphism $g$ is a $K_Y$-trivial contraction, not a step of the program.

**Example 8.5.17 (the cone over a cubic surface).** Let $X$ be the cone over a smooth cubic surface $S \subset \mathbb{P}^3$, as in Example 4.4.22. The blow-up of the vertex is the total space $Y$ of $\mathcal{O}_S(-1)$, and $K_Y = g^* K_X + aE$ with $E \cong S$; adjunction gives $K_E = (K_Y + E)|_E$, that is $\mathcal{O}_S(-1) = (a + 1) E|_E = \mathcal{O}_S(-(a+1))$, so $a = 0$. So $Y$ is a crepant terminal model and $X$ is canonical, not terminal.

**Example 8.5.18 (a klt point that is not canonical).** Let $X = \frac14(1,1,1)$ and $Y$ the total space of $\mathcal{O}_{\mathbb{P}^2}(-4)$. Then $K_Y = g^* K_X - \frac14 E$, and for a line $\ell \subset E$, $K_Y \cdot \ell = -\frac14 \cdot (-4) = 1 > 0$. So $K_Y$ is nef over $X$ and $Y$ is the output of the program over $X$, but it is not crepant: the divisor $A = -\frac14 E$ of the proof of Theorem 8.5.11 is not effective, which is where the canonical hypothesis enters.

### Proof

*Proof of Theorem 8.5.11.* By Hironaka's theorem, Theorem 4.2.10, there is a projective resolution $f \colon W \to X$ whose exceptional locus is a divisor $\sum E_i$. Write $K_W = f^* K_X + \sum a_i E_i$. Since $X$ is canonical, $a_i \ge 0$. The 3-fold $W$ is smooth, hence $\mathbb{Q}$-factorial and terminal, and projective over $S = X$. Run a $K_W$-MMP over $X$, which terminates by Theorem 8.5.3. Let $W = X_0 \dashrightarrow \cdots \dashrightarrow X_N$ be the steps and $g_i \colon X_i \to X$ the induced projective birational morphisms. The program cannot end with a Mori fibre space $X_N \to Z$ over $X$: the morphism $g_N$ would factor through $Z$, so $\dim Z \ge 3$. So $Y = X_N$ has $K_Y$ nef over $X$, and $Y$ is $\mathbb{Q}$-factorial and terminal by Lemma 8.5.2.

Let $A_i = K_{X_i} - g_i^* K_X$. Then $A_0 = \sum a_i E_i \ge 0$ and $A_{i+1}$ is the push-forward of $A_i$: at a divisorial step $\varphi$, $g_i^* K_X = \varphi^* g_{i+1}^* K_X$ and $\varphi_* K_{X_i} = K_{X_{i+1}}$; at a flip both divisors are strict transforms. So $A = A_N$ is effective, and its components are $f$-exceptional divisors that survive on $Y$, hence $g$-exceptional. Also $A \equiv_X K_Y$ is nef over $X$. Apply the negativity lemma, Theorem 1.5.22, to $B = -A$: $-B$ is $g$-nef and $g_* B = 0$, so $B \ge 0$, that is $A \le 0$. Hence $A = 0$ and $K_Y = g^* K_X$. $\square$

*Proof of Proposition 8.5.12.* Since $K_Y = g^* K_X$, Lemma P8.13.3 gives $a(F, X) = a(F, Y)$ for every divisor $F$ over $X$, where for a divisor $F$ on $Y$ the right side is $0$. So a $g$-exceptional prime divisor has $a(F, X) = 0$. Conversely let $F$ be exceptional over $X$ with $a(F, X) = 0$. If $F$ is not a divisor on $Y$, it is exceptional over $Y$ with $a(F, Y) = 0$, which contradicts that $Y$ is terminal. So $F$ is a divisor on $Y$, $g$-exceptional because it is exceptional over $X$. The set of exceptional divisors with discrepancy $0$ over a canonical 3-fold is finite by Lemma 8.4.9. $\square$

*Proof of Corollary 8.5.13.* Let $g \colon Y \to X$ be the model of Theorem 8.5.11. A $g$-exceptional prime divisor would have $a(F, X) = 0$ by Proposition 8.5.12, which is impossible for terminal $X$. So $g$ is small. Now let $X$ be $\mathbb{Q}$-factorial and $g \colon Y \to X$ small, projective and birational, with $H$ a $g$-ample Cartier divisor on $Y$. Then $g_* H$ is $\mathbb{Q}$-Cartier, and $g^* g_* H$ and $H$ agree outside the exceptional locus of $g$, which has codimension at least $2$, so $g^* g_* H \sim_{\mathbb{Q}} H$. The left side has degree $0$ on every curve contracted by $g$ and the right side is positive on it, so $g$ contracts no curve. A projective birational morphism with finite fibres onto a normal variety is an isomorphism by Zariski's main theorem. $\square$

### Exercises

1. (A) In Example 8.5.14, write the two charts of the blow-up of $(x, z)$ and check that $Y$ is smooth, that $C \cong \mathbb{P}^1$ and that $N_{C/Y} = \mathcal{O}(-1)^{\oplus 2}$.
2. (A) In Example 8.5.16, check that the total space of $\mathcal{O}_{\mathbb{P}^2}(-3)$ is the blow-up of $\frac13(1,1,1)$ at the origin, and compute $K_Y \cdot \ell$ from adjunction.
3. (B) Show that the birational map $Y \dashrightarrow Y'$ of Example 8.5.14 over $X$ is not a morphism, so that $X$ has two non-isomorphic $\mathbb{Q}$-factorializations.
4. (B) Let $X$ be a canonical 3-fold and $g_1 \colon Y_1 \to X$, $g_2 \colon Y_2 \to X$ two crepant terminal models. Show, with Proposition 8.5.12, that the birational map $Y_1 \dashrightarrow Y_2$ over $X$ is an isomorphism in codimension one.
5. (B) Let $X$ be the cone over a smooth surface $S \subset \mathbb{P}^3$ of degree $d$. Compute the discrepancy of the blow-up of the vertex, and show that $X$ has a crepant terminal model if and only if $d \le 3$, and that it is terminal if and only if $d \le 2$.
6. (C) Let $X$ be a quasi-projective klt 3-fold and $Y \to X$ the output of a $K_W$-MMP over $X$ from a resolution $W$. Show that $K_Y = g^* K_X + A$ with $A \le 0$ and $g$-exceptional, and that $A = 0$ if and only if $X$ is canonical. Compute $A$ in Example 8.5.18.

### Lean

`MinimalModel.IsTerminal`, `MinimalModel.IsQFactorial` and `MinimalModel.DiscrepancyCompare` give the notions used here. Theorem 8.5.11 and Corollary 8.5.13 are not yet in Lean.

### Notes and history

Theorem 8.5.11 is due to Reid (Rei83b) for the partial resolution of canonical 3-folds by crepant blow-ups, and in the form given here, with the program over $X$, to Kawamata (Kaw88) and KM98, Section 6.3. Corollary 8.5.13 is in Kaw88 and KM98, Section 6.3. Reid's construction of the crepant model came before the existence of flips: he blew up the curves of $cDV$ points and the non-cDV points by hand, with the classification of canonical 3-fold points as the input. The same argument with the program over $X$ works in every dimension once the MMP is available, and in that generality it is a consequence of BCHM10, discussed in Volume 9.
