---
title: Jumping numbers
nodes: []
sources: [ELSV04, Laz04]
reads_with: [ELSV04:sec1, Laz04:9.3]
requires: [P7.10, 4.6]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Jumping numbers

### Statement

The multiplier ideals $\mathcal{J}(\mathfrak{a}^c)$ decrease as $c$ grows, and by part 5 of Proposition P7.10.4 they are constant on intervals $[c, c + \varepsilon)$. So they change only at isolated values of $c$. The log canonical threshold is the first of them. This section studies all of them, following Ein, Lazarsfeld, Smith and Varolin (ELSV04). As before, $X$ is a smooth variety of dimension $n$ over $k$ of characteristic $0$.

**Definition 5.4.19 (jumping numbers).** Let $\mathfrak{a}$ be a nonzero ideal and $x \in X$. A rational number $\xi > 0$ is a *jumping number* of $\mathfrak{a}$ at $x$ if $\mathcal{J}(\mathfrak{a}^\xi)_x \neq \mathcal{J}(\mathfrak{a}^{\xi - \varepsilon})_x$ for every $\varepsilon > 0$. It is a jumping number of $\mathfrak{a}$ if $\mathcal{J}(\mathfrak{a}^\xi) \neq \mathcal{J}(\mathfrak{a}^{\xi - \varepsilon})$ for every $\varepsilon > 0$. For an effective $\mathbb{Q}$-divisor $D$, the jumping numbers of $D$ are defined in the same way with $\mathcal{J}(\xi D)$.

The definition uses rational $\xi$ only, since multiplier ideals are defined for rational exponents. Proposition 5.4.20 shows that nothing is lost: the jumps happen at rational numbers.

**Proposition 5.4.20 (discreteness and rationality).** Let $\mu$ be a log resolution of $\mathfrak{a}$ with $\mathfrak{a} \mathcal{O}_{X'} = \mathcal{O}_{X'}(-F)$, $F = \sum_i e_i F_i$. Every jumping number of $\mathfrak{a}$ lies in the discrete set
$$S(\mu) = \{ c > 0 : c \, e_i \in \mathbb{Z} \text{ for some } i \text{ with } e_i > 0 \} = \bigcup_{e_i > 0} \tfrac{1}{e_i} \mathbb{Z}_{> 0}.$$
The same holds for an effective $\mathbb{Q}$-divisor $D$, with $\mu^* D = \sum_i e_i F_i$ and $e_i \in \mathbb{Q}$. In particular the jumping numbers form a discrete set of rational numbers, and $\mathcal{J}(\mathfrak{a}^c)$ is constant on the intervals between consecutive jumping numbers.

Lean: not yet in Lean.

**Proposition 5.4.21 (the first jumping number).** Let $x \in X$ be a point with $\mathfrak{a}_x \neq \mathcal{O}_{X,x}$. Then $\mathcal{J}(\mathfrak{a}^c)_x = \mathcal{O}_{X,x}$ if and only if $c < \operatorname{lct}_x(\mathfrak{a})$, and the smallest jumping number of $\mathfrak{a}$ at $x$ is $\operatorname{lct}_x(\mathfrak{a})$. The smallest jumping number of $\mathfrak{a}$ is $\operatorname{lct}(\mathfrak{a})$.

Lean: not yet in Lean.

**Lemma 5.4.22 (adding an integral divisor).** Let $D$ be an effective $\mathbb{Q}$-divisor and $A$ an effective integral divisor. Then $\mathcal{J}(D + A) = \mathcal{J}(D) \cdot \mathcal{O}_X(-A)$.

Lean: not yet in Lean.

**Lemma 5.4.23 (the valuative description).** With $\mu$ and $F$ as in Proposition 5.4.20 and $K_{X'/X} = \sum_i k_i F_i$, where the $F_i$ are the prime divisors of $F + \operatorname{Exc}(\mu)$,
$$\mathcal{J}(\mathfrak{a}^c) = \{ \varphi \in \mathcal{O}_X : \operatorname{ord}_{F_i}(\varphi) \geq \lfloor c e_i \rfloor - k_i \text{ for all } i \}.$$
In particular $\mathcal{J}(\mathfrak{a}^c)$ is integrally closed. If $I \subseteq I'$ are ideals, $I$ is integrally closed and $\mathfrak{a} I = \mathfrak{a} I'$, then $I = I'$.

Lean: not yet in Lean.

**Proposition 5.4.24 (periodicity).**

1. Let $D$ be a nonzero effective integral divisor and $x \in \operatorname{Supp} D$. Then $\mathcal{J}((c + 1) D) = \mathcal{J}(cD) \cdot \mathcal{O}_X(-D)$ for every rational $c \geq 0$, a rational $\xi > 0$ is a jumping number of $D$ at $x$ if and only if $\xi + 1$ is, and every positive integer is a jumping number of $D$ at $x$.
2. Let $\mathfrak{a}$ be a nonzero ideal, $x \in X$ and $\xi > n - 1$ rational. Then $\xi$ is a jumping number of $\mathfrak{a}$ at $x$ if and only if $\xi + 1$ is.

Lean: not yet in Lean.

So the jumping numbers of a principal ideal are determined by those in $(0, 1]$, and those of any ideal by those in $(0, n]$.

### Proof in words

On a log resolution, $\lfloor cF \rfloor$ changes only when some $c e_i$ crosses an integer, so the multiplier ideal can change only there. The first jump is the threshold, by the criterion $c e_i < k_i + 1$ of Proposition P7.10.5 applied near $x$. For periodicity of a divisor, adding $D$ to $cD$ multiplies the multiplier ideal by the invertible ideal $\mathcal{O}_X(-D)$, which preserves strict inclusions. For an ideal, Skoda's theorem multiplies by $\mathfrak{a}$ above $n - 1$, and a cancellation law for integrally closed ideals, proved by the determinant trick, preserves strict inclusions as well.

### Examples

**Example 5.4.25 (an snc divisor).** Let $D = \frac12 \{x = 0\} + \frac43 \{y = 0\}$ on $\mathbb{A}^2$, as in Example P7.10.6. By part 2 of Proposition P7.10.4, $\mathcal{J}(cD) = (x^{\lfloor c/2 \rfloor} y^{\lfloor 4c/3 \rfloor})$. The jumping numbers at the origin are the $c$ with $\frac c2 \in \mathbb{Z}$ or $\frac{4c}{3} \in \mathbb{Z}$: the set $\frac34 \mathbb{Z}_{>0} \cup 2 \mathbb{Z}_{>0} = \{\frac34, \frac32, 2, \frac94, 3, \frac{15}4, 4, \dots\}$. Here $S(\mu)$ for $\mu = \operatorname{id}$ is exactly this set. The first jump is $\frac34 = \operatorname{lct}_0(D)$, and at a point of $\{x = 0\}$ away from the origin the jumping numbers are $2, 4, 6, \dots$, with first jump $2$. The divisor is not integral, and its jumping numbers are not periodic with period $1$.

**Example 5.4.26 (the maximal ideal).** Let $\mathfrak{m} = (x_1, \dots, x_n)$. By Example P7.10.8, $\mathcal{J}(\mathfrak{m}^c) = \mathfrak{m}^{\lfloor c \rfloor - n + 1}$, read as $\mathcal{O}$ when $\lfloor c \rfloor < n$. The jumping numbers at the origin are the integers $n, n+1, n+2, \dots$, and the first is $\operatorname{lct}_0(\mathfrak{m}) = n$. On the blow-up of the origin $e = 1$, so $S(\mu) = \mathbb{Z}_{>0}$, and the integers $1, \dots, n-1$ are candidates of Proposition 5.4.20 that do not jump. Part 2 of Proposition 5.4.24 is visible: above $n - 1$ the set is invariant under $\xi \mapsto \xi + 1$.

**Example 5.4.27 (the cusp).** Let $C = \{f = 0\}$ with $f = y^2 - x^3$. By Example P7.10.7, $\mathcal{J}(cC) = \mathcal{O}$ for $c < \frac56$ and $\mathfrak{m}$ for $\frac56 \leq c < 1$, and $\mathcal{J}(C) = (f)$ by part 2 of Proposition P7.10.4. So the jumping numbers in $(0, 1]$ are $\frac56$ and $1$, and by Proposition 5.4.24 all jumping numbers at the origin are $\frac56 + m$ and $1 + m$ for $m \geq 0$. On the log resolution with $e = (1, 2, 3, 6)$ for $C_3, E_1, E_2, E_3$, the set $S(\mu)$ also contains $\frac16$, $\frac13$, $\frac12$ and $\frac23$, none of which is a jump: by Lemma 5.4.23 at $c < \frac56$ the bounds $\lfloor c e_i \rfloor - k_i$ are $\lfloor 2c \rfloor - 1$, $\lfloor 3c \rfloor - 2$ and $\lfloor 6c \rfloor - 4$, all at most $0$.

### Proof

*Proof of Proposition 5.4.20.* Let $c > 0$ with $c \notin S(\mu)$. Since $S(\mu)$ is discrete, there is $\varepsilon > 0$ with $(c - \varepsilon, c] \cap S(\mu) = \emptyset$. For $t \in (c - \varepsilon, c]$ and every $i$ with $e_i > 0$, no integer lies in $(t e_i, c e_i]$, because such an integer $m$ would give $\frac{m}{e_i} \in (t, c] \cap S(\mu)$. So $\lfloor t e_i \rfloor = \lfloor c e_i \rfloor$ for all $i$, $\lfloor tF \rfloor = \lfloor cF \rfloor$, and $\mathcal{J}(\mathfrak{a}^t) = \mathcal{J}(\mathfrak{a}^c)$. Hence $c$ is not a jumping number, globally or at any point. The set $S(\mu)$ is a finite union of the discrete sets $\frac{1}{e_i} \mathbb{Z}_{>0}$, so it is discrete and consists of rational numbers. The same proof works for $D$. Between two consecutive jumping numbers $\xi < \xi'$ the ideals are constant on $[\xi, \xi')$: for $t \in (\xi, \xi')$ the ideal does not change near $t$ from the left, and by part 5 of Proposition P7.10.4 it does not change from the right, so it is locally constant on $[\xi, \xi')$, which is connected. $\square$

*Proof of Proposition 5.4.21.* Let $F_1, \dots, F_N$ be the prime divisors of $F + \operatorname{Exc}(\mu)$. The sets $\mu(F_i)$ are closed because $\mu$ is proper. Let $U$ be the complement of the union of the $\mu(F_i)$ that do not contain $x$. Over $U$, $\mu$ is a log resolution of $\mathfrak{a}|_U$ whose divisors are the $F_i$ with $x \in \mu(F_i)$. By Proposition P7.10.5 on $U$, whose proof is local over the base, $\mathcal{J}(\mathfrak{a}^c)|_U = \mathcal{O}_U$ if and only if $c e_i < k_i + 1$ for every $i$ with $x \in \mu(F_i)$. By Theorem 4.6.3 and Corollary 4.6.4, $\operatorname{lct}_x(\mathfrak{a}) = \min \{ \frac{k_i + 1}{e_i} : x \in \mu(F_i), e_i > 0 \}$, and the minimum is over a nonempty set because $\mathfrak{a}_x \neq \mathcal{O}_{X,x}$. So $\mathcal{J}(\mathfrak{a}^c)$ is trivial near $x$ for $c < \operatorname{lct}_x(\mathfrak{a})$. At $c = \operatorname{lct}_x(\mathfrak{a})$, attained by $F_i$ with $x \in \mu(F_i)$, the condition fails, so $\lfloor c e_i \rfloor > k_i$, and by the last sentence of Proposition P7.10.5 on $U$ the zero set of $\mathcal{J}(\mathfrak{a}^c)|_U$ contains $\mu(F_i) \cap U \ni x$. So the stalk at $x$ is not trivial. So $\operatorname{lct}_x(\mathfrak{a})$ is a jumping number at $x$, and no smaller number is. The global statement follows from $\operatorname{lct}(\mathfrak{a}) = \min_x \operatorname{lct}_x(\mathfrak{a})$, Corollary 4.6.4. $\square$

*Proof of Lemma 5.4.22.* Let $\mu$ be a log resolution of $D + A$; it is a log resolution of $D$ too. Since $\mu^* A$ is integral, $\lfloor \mu^*(D + A) \rfloor = \lfloor \mu^* D \rfloor + \mu^* A$, and the projection formula, Proposition P4.4.10, gives $\mu_* \mathcal{O}_{X'}(K_{X'/X} - \lfloor \mu^* D \rfloor - \mu^* A) = \mathcal{J}(D) \otimes \mathcal{O}_X(-A) = \mathcal{J}(D) \cdot \mathcal{O}_X(-A)$. $\square$

*Proof of Lemma 5.4.23.* Since $K_{X'/X} \geq 0$ is exceptional and $X$ is normal, $\mu_* \mathcal{O}_{X'}(K_{X'/X}) = \mathcal{O}_X$, so $\mathcal{J}(\mathfrak{a}^c) \subseteq \mathcal{O}_X$. For $\varphi \in \mathcal{O}_X$ the divisor $\operatorname{div}(\mu^* \varphi)$ is effective, and the divisor $K_{X'/X} - \lfloor cF \rfloor$ has coefficient $k_i - \lfloor c e_i \rfloor$ on $F_i$ and $0$ on every other prime divisor. So $\operatorname{div}(\mu^* \varphi) + K_{X'/X} - \lfloor cF \rfloor \geq 0$ if and only if $\operatorname{ord}_{F_i}(\varphi) \geq \lfloor c e_i \rfloor - k_i$ for all $i$. This is the description. Let $\varphi \in \mathcal{O}_X$ satisfy $\varphi^d + a_1 \varphi^{d-1} + \cdots + a_d = 0$ with $a_j \in \mathcal{J}(\mathfrak{a}^c)^j$, fix $i$, and put $t = \lfloor c e_i \rfloor - k_i$ and $v = \operatorname{ord}_{F_i}$. If $t \leq 0$ the condition $v(\varphi) \geq t$ holds. If $t > 0$, then $v(a_j) \geq jt$, and $v(\varphi) < t$ would give $v(a_j \varphi^{d-j}) > d \, v(\varphi)$ for all $j \geq 1$, which contradicts the equation. So $\varphi \in \mathcal{J}(\mathfrak{a}^c)$, and the ideal is integrally closed. For the cancellation, work on an affine open with generators $g_1, \dots, g_s$ of $\mathfrak{a}$, and let $\varphi \in I'$. Then $\varphi g_l \in \mathfrak{a} I' = \mathfrak{a} I$, so $\varphi g_l = \sum_m c_{lm} g_m$ with $c_{lm} \in I$. The matrix $\varphi \cdot \mathrm{Id} - (c_{lm})$ kills the vector $(g_m)$, so its determinant $\delta$ satisfies $\delta g_m = 0$ for all $m$. As $\mathfrak{a} \neq 0$ and $X$ is integral, $\delta = 0$. Expanding the determinant gives an equation $\varphi^s + a_1 \varphi^{s-1} + \cdots + a_s = 0$ with $a_j \in I^j$. So $\varphi \in \overline{I} = I$. $\square$

*Proof of Proposition 5.4.24.* Part 1. The identity is Lemma 5.4.22 with $A = D$. Let $f$ be a local equation of $D$ at $x$. For ideals $I, I'$ of the domain $\mathcal{O}_{X,x}$, $f I = f I'$ implies $I = I'$. So $\mathcal{J}((\xi + 1) D)_x = \mathcal{J}((\xi + 1 - \varepsilon) D)_x$ if and only if $\mathcal{J}(\xi D)_x = \mathcal{J}((\xi - \varepsilon) D)_x$, for $0 < \varepsilon \leq \xi$, and this gives the equivalence for $\xi > 0$. For the integers it suffices to show that $1$ is a jumping number at $x$. Write $D = \sum_j d_j D_j$ with $x \in D_1$ and $d_1 \geq 1$, and let $0 < \varepsilon < \frac{1}{d_1}$. At a point $y \in D_1$ where $D_1$ is smooth and no other $D_j$ passes, part 2 of Proposition P7.10.4 gives $\mathcal{J}((1 - \varepsilon) D)_y = \mathcal{O}(-(d_1 - 1) D_1)_y$ and $\mathcal{J}(D)_y = \mathcal{O}(-d_1 D_1)_y$, which differ. If the stalks at $x$ agreed, the two coherent ideals would agree on a neighbourhood of $x$, which contains such points $y$. So they differ at $x$.

Part 2. By Proposition 5.4.20 choose $\varepsilon > 0$ with $\xi - \varepsilon \geq n - 1$ such that $\mathcal{J}(\mathfrak{a}^t)$ is constant for $t \in [\xi - \varepsilon, \xi)$ and for $t \in [\xi + 1 - \varepsilon, \xi + 1)$. By Corollary 5.4.13, for $t \geq n - 1$, $\mathcal{J}(\mathfrak{a}^{t+1}) = \mathfrak{a} \cdot \mathcal{J}(\mathfrak{a}^t)$. Put $I = \mathcal{J}(\mathfrak{a}^\xi)_x \subseteq I' = \mathcal{J}(\mathfrak{a}^{\xi - \varepsilon})_x$. Then $\mathcal{J}(\mathfrak{a}^{\xi+1})_x = \mathfrak{a}_x I$ and $\mathcal{J}(\mathfrak{a}^{\xi + 1 - \varepsilon})_x = \mathfrak{a}_x I'$. If $I = I'$, these agree. If they agree, then $I = I'$ by Lemma 5.4.23, applied in the local ring $\mathcal{O}_{X,x}$, where $I$ is integrally closed by the valuative description and the same determinant argument works. So $\xi$ is a jumping number at $x$ if and only if $\xi + 1$ is. $\square$

### Exercises

1. (A) Find all jumping numbers at the origin of $D = \frac23 \{x = 0\} + \frac25 \{y = 0\}$ in $(0, 3]$, and show that they are not periodic.
2. (A) Let $\mathfrak{a} = (x^2, y^3)$. Using Example 5.4.16, list the jumping numbers of $\mathfrak{a}$ in $(0, 3]$, and check part 2 of Proposition 5.4.24 for $\xi > 1$.
3. (B) Let $L_1, L_2, L_3$ be three distinct lines through the origin of $\mathbb{A}^2$ and $D = L_1 + L_2 + L_3$. Using the blow-up of the origin, show that the jumping numbers of $D$ at the origin in $(0, 1]$ are $\frac23$ and $1$, and compare with Example P7.10.15.
4. (B) Show by an example that part 2 of Proposition 5.4.24 can fail for $\xi \leq n - 1$: take $\mathfrak{m} \subset k[x, y, z]$ and $\xi = 2$, or $\xi = 1$ with $\mathfrak{m} \subset k[x, y]$.
5. (B) Let $\mathfrak{a} = (x^a, y^b)$. Show that the jumping numbers of $\mathfrak{a}$ are the numbers $\frac{i+1}{a} + \frac{j+1}{b}$ with $i, j \geq 0$. Hint: Theorem P7.10.17.
6. (C) Let $D$ be an effective $\mathbb{Q}$-divisor and $\xi$ a jumping number of $D$ at $x$. Show that there is a prime divisor $E$ over $X$, with centre containing $x$, such that $\xi \operatorname{ord}_E(D) - \operatorname{ord}_E(K_{X'/X})$ is a positive integer. Such a divisor is said to *compute* $\xi$ (ELSV04, Definition 1.4 and Lemma 1.6, as cited in Laz04).

### Lean

None of the statements of this section is in Lean.

### Notes and history

Jumping numbers were introduced by Ein, Lazarsfeld, Smith and Varolin (ELSV04), who proved discreteness, rationality and periodicity, and related them to the roots of the Bernstein-Sato polynomial: if $\xi \in (0, 1]$ is a jumping number of $f$ at $x$, then $-\xi$ is a root of the local Bernstein-Sato polynomial of $f$. Analytic versions of the same numbers, as jumps of integrability of $|f|^{-2c}$, go back to Libgober's constants of quasiadjunction and to Loeser and Vaquié. The determinant trick in Lemma 5.4.23 is the standard proof that an element is integral over an ideal when it multiplies a faithful finitely generated module into the product.
