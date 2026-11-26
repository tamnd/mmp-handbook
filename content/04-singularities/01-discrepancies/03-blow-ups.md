---
title: Blow-ups and the bound -1
nodes: []
sources: [KM98, Kol13]
reads_with: [KM98:ch2, Kol13:ch2]
requires: [P3.11, P5.6, 4.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Blow-ups and the bound -1

### Statement

The blow-up of a smooth centre is the one model where every discrepancy can be read off by hand. This section computes it and uses it to prove the first structural fact about discrepancies: in dimension at least 2 the number $-1$ is a threshold. Above it, the discrepancies are bounded below by $-1$. Below it, they are not bounded at all.

Let $(X, \Delta)$ be a sub-pair, $\Delta = \sum_i d_i D_i$, and $Z \subset X$ a closed irreducible subset of codimension $c \ge 2$ such that $X$ and $Z$ are smooth at the generic point of $Z$. Then $\mathcal{O}_{X,Z}$ is a regular local ring of dimension $c$ with maximal ideal $\mathfrak{m}_Z$, and each $D_i$ has a local equation $g_i$ in it. Put $\operatorname{mult}_Z D_i = \max\{m : g_i \in \mathfrak{m}_Z^m\}$ and $\operatorname{mult}_Z \Delta = \sum_i d_i \operatorname{mult}_Z D_i$. Let $E_Z$ be the divisor over $X$ given by the exceptional divisor of the blow-up of $Z$. To get a model in the sense of Section 1.2, blow up the ideal of $Z$ and normalize: this is proper and birational, and near the generic point of $Z$ it is the blow-up of a smooth centre in a smooth variety. The valuation of $E_Z$ is $v_Z(g) = \max\{m : g \in \mathfrak{m}_Z^m\}$.

**Lemma 4.1.20 (the blow-up of a smooth centre).** With this notation,

$$a(E_Z, X, \Delta) = c - 1 - \operatorname{mult}_Z \Delta.$$

Lean: not yet in Lean.

**Theorem 4.1.21 (the bound $-1$).** Let $(X, \Delta)$ be a sub-pair with $\dim X \ge 2$.

1. $\operatorname{discrep}(X, \Delta) \le 1$, and $\operatorname{discrep}(X, \Delta) \le 1 - \operatorname{mult}_D \Delta$ for each prime divisor $D$ of $X$.
2. If $a(E, X, \Delta) < -1$ for one divisor $E$ over $X$, exceptional or not, then $\operatorname{discrep}(X, \Delta) = -\infty$.
3. So either $\operatorname{discrep}(X, \Delta) = -\infty$, or
$$-1 \le \operatorname{totaldiscrep}(X, \Delta) \le \operatorname{discrep}(X, \Delta) \le 1,$$
and in the second case every coefficient of $\Delta$ is at most 1.

Lean: not yet in Lean. The definition `MinimalModel.mld` uses the theorem: it is $\bot$ when one log discrepancy is negative, because the log discrepancies are then not bounded below.

This is KM98, Corollary 2.31. Part 3 is the reason that the klt and lc conditions of Chapter 2 need only a bound on discrepancies and no separate bound on the coefficients, once $\dim X \ge 2$.

### Proof in words

For the lemma, take local coordinates in which $Z$ is a coordinate subspace. One chart of the blow-up computes everything: the form $dx_1 \wedge \dots \wedge dx_n$ picks up the factor $y_1^{c-1}$, and the equation of $D_i$ picks up the factor $y_1^{\operatorname{mult}_Z D_i}$.

For part 1 of the theorem, blow up a general codimension 2 subset, either outside the support of $\Delta$ or inside one component $D$. The lemma with $c = 2$ gives $1$ and $1 - \operatorname{mult}_D \Delta$.

For part 2, pass to a model where $E$ is a divisor, and take the crepant pullback. There $E$ is a component of the boundary with coefficient $1 + \varepsilon$ for some $\varepsilon > 0$. Blow up a codimension 2 subset of $E$: the new divisor $F_1$ has coefficient $\varepsilon$. Now $E$ and $F_1$ meet along a codimension 2 subset, and its blow-up gives $F_2$ with coefficient $(1 + \varepsilon) + \varepsilon - 1 = 2\varepsilon$. Each further blow-up of the intersection of $E$ with the last divisor adds $\varepsilon$. So the discrepancies $-\varepsilon, -2\varepsilon, -3\varepsilon, \dots$ appear, and they go to $-\infty$.

### Examples

**Example 4.1.22 (a point on a smooth surface).** Let $X$ be a smooth surface, $p \in X$, and $\Delta = \sum_i d_i D_i$. The lemma with $c = 2$ gives

$$a(E_p, X, \Delta) = 1 - \operatorname{mult}_p \Delta = 1 - \sum_i d_i \operatorname{mult}_p D_i.$$

For $\Delta = 0$ this is 1, the discrepancy of Volume 0, Chapter 3. For a line it is $1 - c$, and for two lines $1 - 2c$, as in Example 4.1.9.

**Example 4.1.23 (three concurrent lines).** Let $\Delta = c(L_1 + L_2 + L_3)$ with three lines through the origin of $\mathbb{A}^2$. The blow-up of the origin has $a(E) = 1 - 3c$. For $c = 1$ this is $-2 < -1$, so by part 2 the discrepancies are not bounded below. The proof gives them explicitly. With $\varepsilon = 1$, blow up a point of $E$ off the $L_i'$: $a(F_1) = 1 - 2 = -1$. Blow up $F_1 \cap E'$: $a(F_2) = 1 - 2 - 1 = -2$. The next blow-up gives $-3$, and so on. For $c \le \frac23$ the first blow-up gives $a(E) \ge -1$, and Section 2.2 shows that then every discrepancy is at least $-1$.

**Example 4.1.24 (a boundary with a coefficient above 1).** Let $\Delta = 2L$ with $L = \{x = 0\} \subset \mathbb{A}^2$. Here the divisor $L$ itself has $a(L, \mathbb{A}^2, 2L) = -2 < -1$, and part 2 applies with $E = L$ not exceptional. The divisors $F_k$ of the proof are the monomial valuations with weights $(k, 1)$ (Exercise 3), and $a(F_k) = -k$.

**Counterexample 4.1.25 (dimension 1).** Let $X$ be a smooth curve. Every proper birational morphism from a normal curve to $X$ is an isomorphism, so no divisor over $X$ is exceptional and $\operatorname{discrep}(X, \Delta) = +\infty$ for every $\Delta$. For $\Delta = 2p$ the divisor $p$ has $a = -2 < -1$, and the discrepancies are still bounded below. Part 2 fails in dimension 1. This is why the definitions of klt and lc in Chapter 2, and in the Lean library, state the bound for all divisors over $X$, including the prime divisors of $X$. The Lean library proves that $(\mathbb{A}^1, 2[0])$ is not lc and that $(\mathbb{A}^1, [0])$ is not klt from the coefficient alone.

### Proof

*Proof of the lemma.* By Corollary 4.1.15 it is enough to compute near a general point $p$ of $Z$. At $p$ choose local parameters $x_1, \dots, x_n$ with $Z = \{x_1 = \dots = x_c = 0\}$; they exist because $Z$ is smooth at $p$ and so its ideal is generated by part of a regular system of parameters. On a neighbourhood $U$ of $p$ the forms $dx_i$ are a basis of $\Omega^1_U$, so $\omega = dx_1 \wedge \dots \wedge dx_n$ has $\operatorname{div}_U(\omega) = 0$. Shrink $U$ so that only the $D_i$ that contain $Z$ meet it and each is $\operatorname{div}_U(g_i)$. Then $(K_X + \Delta)|_U = \sum_i d_i \operatorname{div}_U(g_i)$, and Theorem 4.1.12 gives

$$a(E_Z, X, \Delta) = \operatorname{ord}_{v_Z}(\omega) - \sum_i d_i \, v_Z(g_i).$$

In the chart $x_1 = y_1$, $x_j = y_1 y_j$ for $2 \le j \le c$, $x_j = y_j$ for $j > c$, the divisor $E_Z$ is $\{y_1 = 0\}$ and $\omega = y_1^{c-1} \, dy_1 \wedge \dots \wedge dy_n$, as in Example 4.1.7. So $\operatorname{ord}_{v_Z}(\omega) = c - 1$. A function $g \in \mathfrak{m}_Z^m \setminus \mathfrak{m}_Z^{m+1}$ pulls back to $y_1^m \tilde g$, where $\tilde g$ restricted to $E_Z$ is the leading form of $g$, which is not zero. So $v_Z(g_i) = \operatorname{mult}_Z D_i$, and the formula follows. $\square$

*Proof of the theorem.* Part 1. Let $B = \operatorname{Sing} X \cup \operatorname{Supp} \Delta$, a proper closed subset of $X$. Since $\dim X \ge 2$, there is an irreducible $Z$ of codimension 2 whose generic point lies outside $B$. Then $\operatorname{mult}_Z \Delta = 0$ and the lemma gives $a(E_Z) = 1$, so $\operatorname{discrep} \le 1$. For a prime divisor $D$ with $\operatorname{mult}_D \Delta = d$, the set $B_D = D \cap (\operatorname{Sing} X \cup \operatorname{Sing} D \cup \text{the other components of } \Delta)$ is a proper closed subset of $D$, and $\dim D \ge 1$. Take an irreducible $Z \subset D$ of codimension 1 in $D$ whose generic point lies outside $B_D$. Then $X$ and $Z$ are smooth at the generic point of $Z$, $\operatorname{mult}_Z D = 1$, $\operatorname{mult}_Z \Delta = d$, and the lemma gives $a(E_Z) = 1 - d$.

Part 2. Let $a(E, X, \Delta) = -1 - \varepsilon$ with $\varepsilon > 0$, and let $f \colon Y \to X$ be a model on which $E$ is a prime divisor. Let $(Y, \Delta_Y)$ be the crepant pullback. Then $\operatorname{mult}_E \Delta_Y = 1 + \varepsilon$. By Proposition 4.1.14, $a(F, X, \Delta) = a(F, Y, \Delta_Y)$ for every $F$ over $Y$. A divisor $F$ that is exceptional over $Y$ is exceptional over $X$, because $c_X(F) = f(c_Y(F))$ has dimension at most $\dim c_Y(F) \le n - 2$. So it is enough to find divisors $F_k$, exceptional over $Y$, with $a(F_k, Y, \Delta_Y) \to -\infty$.

By Corollary 4.1.15 it is enough to work on an open set $V \subset Y$ that meets $E$, on which $Y$ and $E$ are smooth and $E$ is the only component of $\Delta_Y$. On $V$, $\Delta_Y = (1 + \varepsilon)E$. Since $\dim E \ge 1$, there is an irreducible $Z_0 \subset E \cap V$ of codimension 1 in $E$, smooth at its generic point. Near a general point of $Z_0$ take coordinates with $E = \{x_1 = 0\}$ and $Z_0 = \{x_1 = x_2 = 0\}$. Let $Y_1$ be the blow-up of $Z_0$ and $F_1$ its exceptional divisor. The lemma gives $a(F_1, Y, \Delta_Y) = 1 - (1 + \varepsilon) = -\varepsilon$. In the chart $x_1 = y_1 y_2$, $x_2 = y_2$, the divisor $F_1$ is $\{y_2 = 0\}$ and the strict transform $E'$ is $\{y_1 = 0\}$. So near the generic point of $Z_1 = E' \cap F_1$ the crepant pullback is $(1 + \varepsilon) E' + \varepsilon F_1$, with $E'$ and $F_1$ two coordinate hyperplanes.

Suppose that after $k$ steps $Y_k$ has, near the generic point of $Z_k = E' \cap F_k$, the boundary $(1 + \varepsilon)E' + k\varepsilon F_k$ with $E'$ and $F_k$ coordinate hyperplanes. Blow up $Z_k$, of codimension 2. The lemma, applied to the crepant pullback $(Y_k, \Delta_{Y_k})$, gives

$$a(F_{k+1}, Y_k, \Delta_{Y_k}) = 1 - (1 + \varepsilon) - k\varepsilon = -(k+1)\varepsilon.$$

The same chart shows that $E'$ and $F_{k+1}$ are again coordinate hyperplanes near $Z_{k+1} = E' \cap F_{k+1}$, and the coefficient of $F_{k+1}$ in the crepant pullback is $(k+1)\varepsilon$. By Proposition 4.1.14 applied to $Y_k \to Y$, $a(F_{k+1}, Y, \Delta_Y) = -(k+1)\varepsilon$. This goes to $-\infty$.

Part 3. If $\operatorname{discrep}(X, \Delta) > -\infty$, part 2 says that $a(E, X, \Delta) \ge -1$ for every $E$ over $X$, so $\operatorname{totaldiscrep} \ge -1$. For $E$ the strict transform of $D$ this reads $\operatorname{mult}_D \Delta \le 1$. The other inequalities are the definition and part 1. $\square$

### Exercises

1. (A) Let $\Delta = \frac12(L_1 + L_2 + L_3 + L_4)$ for four lines through the origin of $\mathbb{A}^2$. Compute $a(E)$ for the blow-up of the origin.
2. (A) Let $H = \{xy = 0\} \subset \mathbb{A}^3$ and $0 \le c \le 1$. Compute $a(E_Z, \mathbb{A}^3, cH)$ for $Z$ the line $\{x = y = 0\}$ and for $Z$ the origin. Which is smaller?
3. (B) For $\Delta = 2L$, $L = \{x = 0\} \subset \mathbb{A}^2$, show that the divisors $F_k$ of the proof of part 2, starting from a point of $L$, are the monomial valuations with weights $(k, 1)$, and check $a(F_k) = -k$ with the formula of the monomial valuations in Section 1.2.
4. (B) Let $D_1$, $D_2$ be prime divisors of $X$ that meet along a $Z$ of codimension 2, with $X$, $D_1$ and $D_2$ smooth and transversal at the generic point of $Z$. Show that $\operatorname{discrep}(X, d_1D_1 + d_2 D_2) \le 1 - d_1 - d_2$.
5. (B) Show that part 3 of the theorem gives: if $\dim X \ge 2$ and $\operatorname{discrep}(X, \Delta) \ge -1$, then $\operatorname{totaldiscrep}(X, \Delta) \ge -1$. Give an example in dimension 1 where $\operatorname{discrep} \ge -1$ and $\operatorname{totaldiscrep} < -1$.
6. (C) Let $X$ be a smooth surface. Use Exercise 6 of Section 1.2 to show that $\operatorname{discrep}(X, 0) = 1$.

### Lean

The lemma and the theorem are not yet in Lean. The docstring of `MinimalModel.mld` cites the theorem to justify the value $\bot$. The Lean file `MinimalModel/Fidelity/AffineLine.lean` builds the pairs $(\mathbb{A}^1, c[0])$ as `MinimalModel.affineLinePair` and proves `MinimalModel.affineLinePair_two_not_isLc` and `MinimalModel.affineLinePair_one_not_isKlt` by the lemmas `MinimalModel.not_isLc_of_one_lt` and `MinimalModel.not_isKlt_of_one_le`, which read the coefficient condition of the definitions. This is the counterexample in dimension 1: there the coefficient condition is not a consequence of the bound on discrepancies, so the definitions must state it.

### Notes and history

The computation of the blow-up of a smooth centre is classical, and it is the basis of all later computations of discrepancies. The trick of part 2, to blow up again and again along the intersection with a divisor of coefficient above 1, is in KM98, Chapter 2. The same theorem explains why the minimal log discrepancy of a pair that is not lc is $-\infty$ by convention.
