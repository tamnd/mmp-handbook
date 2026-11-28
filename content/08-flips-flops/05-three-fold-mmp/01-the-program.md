---
title: The program assembled
nodes: [MMMAM98WJQ]
sources: [KM98, Mor88, Kaw92, Sho92, Kol92]
reads_with: [KM98:3.7, Mor88:main]
requires: [1.5, 3.6, 4.4, 6.3, 6.4, 7.2, P8.13]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The program assembled

### Statement

Throughout, $f \colon X \to S$ is a projective morphism of quasi-projective varieties over an algebraically closed field of characteristic $0$, and $X$ is a normal 3-fold. Curves are curves contracted by $f$, $\overline{NE}(X/S)$ is the relative cone of curves and $\rho(X/S)$ the relative Picard number.

**Definition 8.5.1 (steps, minimal models, Mori fibre spaces).** Let $X$ be a $\mathbb{Q}$-factorial terminal 3-fold, projective over $S$. A *minimal model over $S$* is such an $X$ with $K_X$ nef over $S$. A *Mori fibre space over $S$* is a contraction $g \colon X \to Y$ over $S$ with $\dim Y < 3$, $\rho(X/Y) = 1$ and $-K_X$ ample over $Y$, as in Definition 6.4.17. If $K_X$ is not nef over $S$, let $R$ be a $K_X$-negative extremal ray of $\overline{NE}(X/S)$ and $\varphi = \operatorname{cont}_R \colon X \to Y$ its contraction over $S$. The *step* of the program defined by $R$ is:

1. if $\varphi$ is *divisorial*, that is birational with exceptional locus a prime divisor, the replacement of $X$ by $Y$;
2. if $\varphi$ is *small*, that is birational with exceptional locus of codimension at least $2$, the replacement of $X$ by the flip $X^+$ of $\varphi$;
3. if $\dim Y < 3$, the end of the program, with the Mori fibre space $\varphi \colon X \to Y$.

A *$K_X$-MMP over $S$* is a sequence of steps, each applied to the output of the previous one. It *terminates* if it reaches a minimal model over $S$ or a Mori fibre space over $S$ after finitely many steps.

**Lemma 8.5.2 (the steps stay in the class).** Let $X$ be a $\mathbb{Q}$-factorial terminal 3-fold, projective over $S$, and $\varphi \colon X \to Y$ the contraction of a $K_X$-negative extremal ray $R$ of $\overline{NE}(X/S)$.

1. If $\varphi$ is divisorial with exceptional divisor $E$, then $E \cdot R < 0$, $Y$ is $\mathbb{Q}$-factorial and terminal, $K_X = \varphi^* K_Y + c E$ with $c > 0$, and $\rho(Y/S) = \rho(X/S) - 1$.
2. If $\varphi$ is small and its flip $\varphi^+ \colon X^+ \to Y$ exists, then $X^+$ is $\mathbb{Q}$-factorial and terminal, projective over $S$, and $\rho(X^+/S) = \rho(X/S)$.

Lean: not yet in Lean.

**Theorem 8.5.3 (the 3-fold MMP, Mori).** Let $X$ be a $\mathbb{Q}$-factorial terminal 3-fold, projective over $S$. Every $K_X$-MMP over $S$ starting at $X$ terminates. In particular there is a finite sequence of steps $X = X_0 \dashrightarrow X_1 \dashrightarrow \cdots \dashrightarrow X_N$ such that $X_N$ is a minimal model over $S$ or carries a Mori fibre space $X_N \to Y$ over $S$. Each $X_i$ is $\mathbb{Q}$-factorial and terminal, and each map $X_i \dashrightarrow X_{i+1}$ is a divisorial contraction or a flip.

Lean: not yet in Lean.

**Theorem 8.5.4 (the lc 3-fold MMP; Kawamata, Shokurov, Kollár et al.; cited).** Let $(X, \Delta)$ be a $\mathbb{Q}$-factorial dlt pair of dimension $3$, projective over $S$. The $(K_X + \Delta)$-MMP over $S$ exists and terminates: there is a finite sequence of divisorial contractions and $(K + \Delta)$-flips over $S$ that ends with a pair $(X', \Delta')$ with $K_{X'} + \Delta'$ nef over $S$, or with a $(K_{X'} + \Delta')$-negative contraction of fibre type over $S$. The same holds for lc pairs, with the steps taken among lc pairs.

Node: MMMAM98WJQ · Lean: `MinimalModel.ThreefoldLcMMP`

**Corollary 8.5.5 (smooth projective 3-folds).** Let $X$ be a smooth projective 3-fold. Then $X$ is birational to a projective $\mathbb{Q}$-factorial terminal 3-fold $X'$ such that either $K_{X'}$ is nef or $X'$ carries a Mori fibre space. If $X$ is not uniruled, the first case holds for every $K_X$-MMP starting at $X$.

Lean: not yet in Lean.

### Proof in words

The cone theorem gives a $K$-negative extremal ray as soon as $K$ is not nef, and the contraction theorem contracts it. A divisorial contraction stays among $\mathbb{Q}$-factorial terminal 3-folds, because divisors on the target pull back after a correction by the exceptional divisor, and the exceptional divisor has positive discrepancy because $K$ and $E$ are both negative on the ray. A small contraction is followed by its flip, which exists by Mori's theorem, and the flip stays in the class because discrepancies go up (Lemma 8.4.2). A divisorial step lowers the Picard number, so there are at most $\rho(X/S)$ of them, and between two of them there are finitely many flips by the termination theorem of Chapter 4. So the program stops, and it can only stop at a minimal model or a Mori fibre space. A Mori fibre space is covered by rational curves, which gives the corollary.

### Examples

**Example 8.5.6 (the blow-up of $\mathbb{P}^3$ at a point).** Let $X = \operatorname{Bl}_p \mathbb{P}^3$ with exceptional divisor $E \cong \mathbb{P}^2$, $\ell_E$ a line in $E$ and $\ell'$ the strict transform of a line through $p$, as in Example 6.3.19. Then $K_X = \pi^* K_{\mathbb{P}^3} + 2E$ and $E \cdot \ell_E = -1$, $E \cdot \ell' = 1$, so $K_X \cdot \ell_E = -2$ and $K_X \cdot \ell' = -4 + 2 = -2$. Both rays are $K_X$-negative. The ray of $\ell_E$ is divisorial: the step is $X \to \mathbb{P}^3$, followed by the Mori fibre space $\mathbb{P}^3 \to \mathrm{pt}$. The ray of $\ell'$ is of fibre type: it is the $\mathbb{P}^1$-bundle $X \to \mathbb{P}^2$ given by the lines through $p$, and the program stops at once. Two programs from the same $X$ end with different Mori fibre spaces.

**Example 8.5.7 (the blow-up of $\mathbb{P}^3$ along a line).** Let $X = \operatorname{Bl}_L \mathbb{P}^3$, with exceptional divisor $E \cong \mathbb{P}^1 \times \mathbb{P}^1$, $f$ a fibre of $E \to L$ and $h$ the pull-back of a line, as in Example 6.3.20. Then $K_X = \pi^* K_{\mathbb{P}^3} + E$, $E \cdot f = -1$, and $K_X \cdot f = -1$. The strict transform $\ell$ of a line meeting $L$ in one point has class $h - f$ and $K_X \cdot \ell = -4 + 1 = -3$. The ray of $f$ gives the step $X \to \mathbb{P}^3$; the ray of $\ell$ gives the $\mathbb{P}^2$-bundle $X \to \mathbb{P}^1$ defined by the planes through $L$, a Mori fibre space over a curve.

**Example 8.5.8 (the program leaves the smooth category).** Let $Y$ be the total space of $\mathcal{O}_{\mathbb{P}^2}(-2)$ and $\pi \colon Y \to X$ the contraction of the zero section $E \cong \mathbb{P}^2$ to the point $\frac12(1,1,1)$, as in Example 4.4.8. Then $K_Y = \pi^* K_X + \frac12 E$, and for a line $\ell \subset E$, $E \cdot \ell = -2$ and $K_Y \cdot \ell = -1$. So $\pi$ is a $K_Y$-negative divisorial contraction over $S = X$ with $\rho(Y/X) = 1$, and the $K_Y$-MMP of the smooth 3-fold $Y$ over $X$ is the single step $Y \to X$. Its output is terminal and $\mathbb{Q}$-factorial, as Lemma 8.5.2 predicts, and not Gorenstein: the class in Definition 8.5.1 has to contain singular 3-folds even if the program starts at a smooth one. A projective example of the same kind is a smooth projective 3-fold containing a plane with normal bundle $\mathcal{O}(-2)$.

**Example 8.5.9 (a toric program).** Let $X$ be the toric weighted blow-up of Example 3.6.17. There the only $K_X$-negative ray is that of the exceptional divisor $E$, while the curve $C_{23}$ has $K_X \cdot C_{23} = 1$. So the $K_X$-MMP of $X$ is unique, $X \to \mathbb{P}^3 \to \mathrm{pt}$, as in Theorem 3.6.8. The flip of $C_{23}$ exists, but it is a $D$-flip for $D = -K_X$ and not a step of the $K_X$-MMP: the program only contracts $K$-negative rays.

### Proof

*Proof of Lemma 8.5.2.* Part 1. Let $C$ be a curve with $[C] \in R$. By Corollary 1.5.23, $E$ is not numerically trivial over $Y$, so $E \cdot R \ne 0$. If $E \cdot R > 0$, then $E$ is $\varphi$-nef since $\rho(X/Y) = 1$, and the negativity lemma, Theorem 1.5.22, applied to $B = -E$ with $\varphi_* B = 0$ gives $-E \ge 0$, which is absurd. So $E \cdot R < 0$. Let $D$ be a prime divisor on $Y$ and $D'$ its strict transform. Since $X$ is $\mathbb{Q}$-factorial, $mD'$ is Cartier for some $m > 0$. Choose integers $k > 0$ and $a$ with $(k m D' + a E) \cdot R = 0$. By the contraction theorem of Volume 7 (KM98, Theorem 3.7, part 4, relative form KM98, Theorem 3.25), a Cartier divisor on $X$ that is zero on $R$ is the pull-back of a Cartier divisor $L$ on $Y$, so $k m D' + a E = \varphi^* L$ and $kmD = \varphi_* \varphi^* L = L$ is Cartier. Hence $Y$ is $\mathbb{Q}$-factorial, $K_Y$ is $\mathbb{Q}$-Cartier, and $K_X = \varphi^* K_Y + cE$ for some $c \in \mathbb{Q}$, because $K_X - \varphi^* K_Y$ is supported on $E$. Then $K_X \cdot C = c\, E \cdot C$ with both intersection numbers negative, so $c > 0$. For a divisor $F$ exceptional over $X$, Lemma P8.13.3 gives $a(F, Y) = a(F, X) + c \operatorname{ord}_F E \ge a(F, X) > 0$, and $a(E, Y) = c > 0$. So $Y$ is terminal. The same descent shows that $\varphi^* \colon N^1(Y/S) \to N^1(X/S)$ is injective with image the classes that vanish on $R$, a hyperplane since $K_X \cdot R \ne 0$. So $\rho(Y/S) = \rho(X/S) - 1$.

Part 2. The flip $X^+$ is projective over $Y$ and so over $S$. Let $D^+$ be a prime divisor on $X^+$ and $D$ its strict transform on $X$, with $mD$ Cartier. Choose $k > 0$ and $a$ with $(kmD - aK_X) \cdot R = 0$. By descent, $kmD - aK_X = \varphi^* L$ with $L$ Cartier on $Y$, at least after multiplying by the index of $K_X$. The divisors $kmD^+ - aK_{X^+}$ and $(\varphi^+)^* L$ agree outside the exceptional locus of $\varphi^+$, which has codimension $2$, so they are linearly equivalent, and $kmD^+$ is $\mathbb{Q}$-Cartier because $K_{X^+}$ is $\mathbb{Q}$-Cartier by the definition of the flip. So $X^+$ is $\mathbb{Q}$-factorial. The map $X \dashrightarrow X^+$ is an isomorphism in codimension one, so the divisors exceptional over $X$ and over $X^+$ are the same, and Lemma 8.4.2 gives $a(F, X^+) \ge a(F, X) > 0$ for each of them. So $X^+$ is terminal. Finally the argument just given shows $N^1(X/S) = \varphi^* N^1(Y/S) \oplus \mathbb{R} K_X$ and $N^1(X^+/S) = (\varphi^+)^* N^1(Y/S) \oplus \mathbb{R} K_{X^+}$, where $(\varphi^+)^*$ is injective because $\varphi^+$ is surjective and $K_{X^+}$ is not a pull-back because it is $\varphi^+$-ample. So both Picard numbers equal $\rho(Y/S) + 1$. $\square$

*Proof of Theorem 8.5.3.* Let $X_i$ be the $i$-th model of a $K$-MMP over $S$. By induction and Lemma 8.5.2, each $X_i$ is a $\mathbb{Q}$-factorial terminal 3-fold, projective over $S$, as long as the flips exist. If $K_{X_i}$ is nef over $S$, $X_i$ is a minimal model. Otherwise the relative cone theorem (KM98, Theorem 3.25, the relative form of the cone theorem of Volume 7) gives a $K_{X_i}$-negative extremal ray $R$ of $\overline{NE}(X_i/S)$, and the contraction theorem gives $\varphi = \operatorname{cont}_R$. If $\dim Y < 3$, then $\rho(X_i/Y) = 1$ and $-K_{X_i}$ is ample over $Y$ because it is positive on the only ray of $\overline{NE}(X_i/Y)$, so $X_i \to Y$ is a Mori fibre space. If $\varphi$ is birational, its exceptional locus is either a prime divisor or has codimension at least $2$: if it contains a prime divisor $E$, then $E \cdot R < 0$ as in the proof of Lemma 8.5.2, every contracted curve has class in $R$ because $\rho(X_i/Y) = 1$, and a curve $C$ with $E \cdot C < 0$ lies in $E$, so the exceptional locus is $E$. And in the small case the flip exists by Mori's flip theorem, proved in Chapter 2 (Mor88). So every step can be carried out. By Lemma 8.5.2, $\rho(X_{i+1}/S) = \rho(X_i/S) - 1$ at a divisorial step and $\rho(X_{i+1}/S) = \rho(X_i/S)$ at a flip. Since $\rho \ge 0$, there are at most $\rho(X/S)$ divisorial steps. Between two consecutive divisorial steps, and after the last one, the program is a sequence of flips of terminal 3-folds, which is finite by Theorem 8.4.11. So the program terminates. $\square$

*Proof of Corollary 8.5.5.* Apply Theorem 8.5.3 with $S = \operatorname{Spec} k$. If the program ends with a Mori fibre space $X' \to Y$, then by Proposition 6.3.15 every fibre is covered by rational curves contracted by it, so $X'$ is uniruled, and so is $X$, which is birational to $X'$. So a non-uniruled $X$ ends with a minimal model. $\square$

### Exercises

1. (A) In Example 8.5.6, find the classes of $\ell_E$ and $\ell'$ in terms of $h$ and $\ell_E$, where $h$ is the pull-back of the class of a line, and check that $\overline{NE}(X)$ is spanned by $\ell_E$ and $\ell'$ and that both rays are $K_X$-negative.
2. (A) In Example 8.5.8, compute $K_Y \cdot \ell$ from $K_Y|_E = K_E - E|_E$ and adjunction, and check that $\rho(Y/X) = 1$.
3. (A) Let $f \colon X \to S$ be birational. Show that a $K_X$-MMP over $S$ never reaches a Mori fibre space, so that it ends with a minimal model over $S$.
4. (B) Let $X$ be a smooth projective 3-fold. Show, using Corollary 6.3.4, Corollary 8.4.13 and Lemma 8.5.2, that the first small step of a $K_X$-MMP, if there is one, comes after a divisorial step whose output is not Gorenstein.
5. (B) In Example 8.5.7, show that the two Mori fibre spaces $\mathbb{P}^3 \to \mathrm{pt}$ and $X \to \mathbb{P}^1$ produced by the two programs are not isomorphic, and that $X \to \mathbb{P}^1$ is not obtained from $\mathbb{P}^3 \to \mathrm{pt}$ by any sequence of steps.
6. (C) Let $\varphi \colon X \to Y$ be a divisorial step of a terminal 3-fold. Show that $d(Y) \le d(X) + 1$, with $d$ the difficulty of Definition 8.4.8, and deduce that a $K_X$-MMP over $S$ has at most $d(X) + 2\rho(X/S)$ steps.

### Lean

`MinimalModel.IsMinimalModel`, `MinimalModel.IsTerminal` and `MinimalModel.IsQFactorial` give the notions of Definition 8.5.1. `MinimalModel.ThreefoldLcMMP` states Theorem 8.5.4 without proof; it combines `MinimalModel.ThreefoldFlips` and `MinimalModel.ThreefoldTermination`. Theorem 8.5.3 and Lemma 8.5.2 are not yet in Lean.

### Notes and history

Theorem 8.5.3 is Mori's (Mor88), who proved the existence of flips; termination for terminal 3-folds is Shokurov's (Sho85), and the assembly is in KM98, Chapter 3 and Section 6.1. Theorem 8.5.4 combines Shokurov's log flips (Sho92), Kawamata's termination (Kaw92) and the lc version worked out in Kol92. The program depends on choices: Examples 8.5.6 and 8.5.7 show that the output is not unique. Minimal models are unique up to flops, which is the subject of Section 3; Mori fibre spaces are related by Sarkisov links, which are discussed in Volume 10. The converse of the last statement of Corollary 8.5.5, that a uniruled 3-fold has no minimal model, follows from the fact that a general member $C$ of a covering family of rational curves on a terminal 3-fold lies in the smooth locus, by Theorem 4.4.15, and is free there (Volume 6), so that $K \cdot C \le -2$ and $K$ is not nef.
