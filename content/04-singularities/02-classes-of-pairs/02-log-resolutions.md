---
title: Log resolutions decide the class
nodes: []
sources: [KM98, Hir64, Kol13]
reads_with: [KM98:ch2, Kol13:ch2]
requires: [P8.5, 4.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Log resolutions decide the class

### Statement

The definitions of Section 2.1 test infinitely many divisors. This section proves that, after one good model, finitely many numbers decide everything. The model is a log resolution, and the numbers are the coefficients of the crepant pullback.

**Definition 4.2.9 (log resolution).** Let $(X, \Delta)$ be a sub-pair. A *log resolution* of $(X, \Delta)$ is a proper birational morphism $f \colon Y \to X$ such that $Y$ is smooth, the exceptional set $\operatorname{Exc}(f)$ is a divisor, and $f^{-1}_* \Delta + \operatorname{Exc}(f)$ is a divisor with simple normal crossings. Here $f^{-1}_* \Delta$ is the strict transform of $\Delta$, and "simple normal crossings" means that the pair $(Y, f^{-1}_*\Delta + \operatorname{Exc}(f))$, with reduced boundary, is snc at every point.

Write $K_Y + \Delta_Y = f^*(K_X + \Delta)$ for the crepant pullback. Then $\Delta_Y = \sum_i b_i F_i$, where the $F_i$ are the components of $f^{-1}_*\Delta$ and the $f$-exceptional prime divisors. So $\Delta_Y$ has snc support. The coefficient of the strict transform of a component $D$ of $\Delta$ is the coefficient of $D$ in $\Delta$, and the coefficient of an $f$-exceptional $F_i$ is $-a(F_i, X, \Delta)$.

**Theorem 4.2.10 (Hironaka).** Let $k$ have characteristic 0. Every sub-pair $(X, \Delta)$ has a log resolution, and it can be chosen to be an isomorphism over the set of points where $(X, \operatorname{Supp} \Delta)$ is snc.

Lean: not yet in Lean.

This is the resolution theorem of Hironaka (Hir64). KM98, Chapter 0, states the form used here. This volume uses it as a black box.

**Lemma 4.2.11 (the logarithmic bound).** Let $Y$ be a smooth variety, $\Delta_Y = \sum_i b_i F_i$ an $\mathbb{R}$-divisor with snc support, and $E$ a divisor over $Y$ with centre $W$ of codimension $c$. Let $F_1, \dots, F_k$ be the components that contain $W$. Then $k \le c$, there are $x_1, \dots, x_c$ in $\mathcal{O}_{Y,W}$ that form a regular system of parameters with $F_i = \{x_i = 0\}$ near the generic point of $W$ for $i \le k$, and for any such choice

$$a(E, Y, \Delta_Y) \ge \sum_{i=1}^{k} (1 - b_i) \, v_E(x_i) + \sum_{j=k+1}^{c} v_E(x_j) - 1.$$

Each $v_E(x_j)$ with $j \le c$ is at least 1. Equality holds when $E$ is the monomial valuation with weights $v_E(x_j)$ in these coordinates.

Lean: not yet in Lean.

**Theorem 4.2.12 (the discrepancy of an snc pair).** Let $Y$ be a smooth variety of dimension at least 2, and $\Delta_Y = \sum_i b_i F_i$ an $\mathbb{R}$-divisor with snc support and every $b_i \le 1$. Then

$$\operatorname{discrep}(Y, \Delta_Y) = \min\Big\{ 1, \ \min_i (1 - b_i), \ \min_{i \ne j, \ F_i \cap F_j \ne \emptyset} (1 - b_i - b_j) \Big\}.$$

Lean: not yet in Lean.

This is KM98, Corollary 2.31, part 3. The coefficients $b_i$ may be negative, so the theorem applies to sub-pairs.

**Corollary 4.2.13 (the classes of an snc pair).** In the theorem, without the condition $b_i \le 1$:

1. $(Y, \Delta_Y)$ is sub-klt if and only if every $b_i < 1$, and sub-lc if and only if every $b_i \le 1$;
2. it is sub-plt if and only if every $b_i \le 1$ and no two components with coefficient 1 meet;
3. it is sub-canonical if and only if every $b_i \le 1$ and $b_i + b_j \le 1$ whenever $F_i \cap F_j \ne \emptyset$, and sub-terminal if and only if every $b_i < 1$ and $b_i + b_j < 1$ whenever $F_i \cap F_j \ne \emptyset$.

Lean: not yet in Lean.

**Theorem 4.2.14 (one log resolution decides).** Let $(X, \Delta)$ be a sub-pair with $\dim X \ge 2$, $f \colon Y \to X$ a log resolution, and $\Delta_Y = \sum_i b_i F_i$ the crepant pullback.

1. $(X, \Delta)$ is sub-klt if and only if every $b_i < 1$. It is sub-lc if and only if every $b_i \le 1$.
2. If every $b_i \le 1$, then
$$\operatorname{discrep}(X, \Delta) = \min\Big\{ \min_{F_i \ f\text{-exceptional}} (-b_i), \ \operatorname{discrep}(Y, \Delta_Y) \Big\},$$
and the second term is given by Theorem 4.2.12.
3. If some $b_i > 1$, then $\operatorname{discrep}(X, \Delta) = -\infty$.

Lean: not yet in Lean.

**Corollary 4.2.15 (dlt implies lc).** Every dlt pair is lc.

Lean: not yet in Lean. The Lean definition `MinimalModel.IsDlt` includes `MinimalModel.IsLc` as a hypothesis, so in Lean the corollary holds by definition.

### Proof in words

For the lemma, write the volume form as $x_1 \cdots x_c$ times a logarithmic form. On any model where $E$ appears, each $\frac{dx_j}{x_j}$ has at most a simple pole along $E$, of the shape $m \frac{dt}{t}$ plus a regular form. A wedge product of such forms has at most a simple pole, because $\frac{dt}{t} \wedge \frac{dt}{t} = 0$. So the order of the volume form along $E$ is at least $\sum_j v_E(x_j) - 1$, and the boundary takes away $\sum_i b_i v_E(x_i)$.

For the theorem on snc pairs, three blow-ups of codimension 2 centres give the three kinds of values: a general centre gives 1, a general centre in $F_i$ gives $1 - b_i$, and a component of $F_i \cap F_j$ gives $1 - b_i - b_j$. The lemma shows that no divisor does better. If $W$ lies in no component, the bound is $c - 1 \ge 1$. If $W$ lies in one, it is at least $1 - b_1$. If $W$ lies in two or more, it is at least $1 - b_1 - b_2$.

For the main theorem, the crepant pullback does not change any discrepancy, and the divisors over $X$ are the divisors over $Y$. The exceptional divisors over $X$ are the exceptional divisors over $Y$ and the $f$-exceptional prime divisors of $Y$. The second kind has discrepancy $-b_i$, and the first kind is controlled by the snc theorem on $Y$.

For dlt implies lc, a divisor with centre in $Z$ has discrepancy above $-1$ by the definition. Any other divisor has a centre that meets the snc locus, and there the snc theorem gives at least $-1$.

### Examples

**Example 4.2.16 (the cusp and its log resolution).** Let $C = \{y^2 = x^3\} \subset \mathbb{A}^2$ and $0 \le t \le 1$. The minimal log resolution of $(\mathbb{A}^2, C)$ needs three blow-ups. The first blow-up, of the origin, gives $E_1$, and the strict transform $C_1$ is tangent to $E_1$. The second, of the point $C_1 \cap E_1$, gives $E_2$, and then $E_2$, the strict transform of $E_1$ and $C_2$ pass through one point. The third, of that point, gives $E_3$. On the result $Y$, the curve $E_3$ meets each of $E_1$, $E_2$ and $C_3$ once, transversally, at three different points, and $E_1 \cap E_2 = \emptyset$. So $f \colon Y \to \mathbb{A}^2$ is a log resolution. Problem 1 of Chapter 1 gives the discrepancies, and

$$\Delta_Y = tC_3 + (2t - 1)E_1 + (3t - 2)E_2 + (6t - 4)E_3.$$

By the theorem, $(\mathbb{A}^2, tC)$ is lc if and only if $6t - 4 \le 1$, that is $t \le \frac56$, and klt if and only if $t < \frac56$. The number $\frac56$ is the log canonical threshold of the cusp (Chapter 6).

**Example 4.2.17 (the nodal cubic, on its resolution).** For $C = \{y^2 = x^2(x+1)\}$, one blow-up of the origin is a log resolution of $(\mathbb{A}^2, C)$, with $\Delta_Y = C' + E$, and $C'$ meets $E$ transversally in two points. Every coefficient is 1, so the pair is lc and not klt. Part 2 gives $\operatorname{discrep} = \min\{-1, 1 - 1 - 1\} = -1$, so it is not plt.

**Example 4.2.18 (the $A_1$ singularity and the ordinary double point).** The minimal resolution of $X = \{xy = z^2\}$ has one exceptional curve $E \cong \mathbb{P}^1$ and $K_Y = f^*K_X$ (Example 4.1.8). It is a log resolution of $(X, 0)$, with $\Delta_Y = 0$. Part 2 gives $\operatorname{discrep}(X, 0) = \min\{0, 1\} = 0$. So $X$ is canonical and not terminal. For the ordinary double point $X$ of dimension 3, the blow-up of the origin is a log resolution, with $E \cong \mathbb{P}^1 \times \mathbb{P}^1$ and $a(E) = 1$ (Problem 3 of Chapter 1). So $\Delta_Y = -E$ and $\operatorname{discrep}(X, 0) = \min\{1, 1, 1 - (-1)\} = 1$. The 3-fold ordinary double point is terminal.

### Proof

*The lemma.* The pair is snc at the generic point of $W$, so the local equations of $F_1, \dots, F_k$ are part of a regular system of parameters of $\mathcal{O}_{Y,W}$. This gives $k \le c$, and the system extends to $x_1, \dots, x_c$. The other components do not contain $W$, so their local equations are units at the generic point of $W$ and have $v_E = 0$. Each $x_j$ with $j \le c$ vanishes on $W$, so $v_E(x_j) \ge 1$. Choose a point of $W$ where $W$ is smooth and extend $x_1, \dots, x_c$ to a system of local coordinates $x_1, \dots, x_n$ of $Y$ on an open set $U$ that meets $W$. Take $\omega = dx_1 \wedge \dots \wedge dx_n$, so that $K_Y = 0$ on $U$, and

$$\omega = x_1 \cdots x_c \cdot \eta, \qquad \eta = \frac{dx_1}{x_1} \wedge \dots \wedge \frac{dx_c}{x_c} \wedge dx_{c+1} \wedge \dots \wedge dx_n.$$

Let $g \colon Y' \to Y$ be a model on which $E$ is a prime divisor. At a general point $p$ of $E$, $Y'$ is smooth, and there are local coordinates $t, y_2, \dots, y_n$ with $E = \{t = 0\}$. Near $p$, $g^* x_j = t^{m_j} u_j$ with $m_j = v_E(x_j)$ and $u_j$ a unit, since the divisor of $g^*x_j$ near a general point of $E$ is $m_j E$. Then

$$\frac{dx_j}{x_j} = m_j \frac{dt}{t} + \frac{du_j}{u_j},$$

and $\frac{du_j}{u_j}$ and $dx_j$ for $j > c$ are regular at $p$. Expand the wedge product $\eta$. Each term has at most one factor $\frac{dt}{t}$, because $\frac{dt}{t} \wedge \frac{dt}{t} = 0$. So $t \eta$ is regular at $p$, and $\operatorname{ord}_E(\eta) \ge -1$. Hence $\operatorname{ord}_E(\omega) \ge \sum_{j=1}^{c} m_j - 1$. Shrink $U$ so that it meets no component other than $F_1, \dots, F_k$. It still meets $W$, and on it $K_Y + \Delta_Y = \sum_{i=1}^{k} b_i \operatorname{div}(x_i)$. So Theorem 4.1.12 gives

$$a(E, Y, \Delta_Y) = \operatorname{ord}_E(\omega) - \sum_{i=1}^{k} b_i m_i \ge \sum_{i=1}^{k} (1 - b_i) m_i + \sum_{j=k+1}^{c} m_j - 1.$$

For a monomial valuation in the coordinates $x_1, \dots, x_n$, the formula of Example 4.1.17 is this bound with equality.

*The theorem on snc pairs.* Call the minimum $\mu$. First, $\operatorname{discrep} \le \mu$. Let $Z$ be a general codimension 2 smooth subvariety, not in any $F_i$; Lemma 4.1.20 gives $a(E_Z) = 1$. Let $Z$ be a general codimension 1 smooth subvariety of $F_i$, in no other component; it gives $1 - b_i$. If $F_i \cap F_j \ne \emptyset$, let $Z$ be a component of $F_i \cap F_j$. It has codimension 2 since the support is snc, and both $F_i$ and $F_j$ have multiplicity 1 along it, so the lemma on blow-ups gives $1 - b_i - b_j$.

Next, $a(E) \ge \mu$ for every exceptional $E$ over $Y$. Let $W$ be its centre, of codimension $c \ge 2$, and use the logarithmic bound with $m_j = v_E(x_j) \ge 1$ and $1 - b_i \ge 0$.

- If $k = 0$, then $a(E) \ge \sum_{j=1}^{c} m_j - 1 \ge c - 1 \ge 1 \ge \mu$.
- If $k = 1$, then $a(E) \ge (1 - b_1) m_1 + (c - 1) - 1 \ge 1 - b_1 \ge \mu$, since $c \ge 2$ and $m_1 \ge 1$.
- If $k \ge 2$, drop all terms but the first two: $a(E) \ge (1 - b_1) + (1 - b_2) - 1 = 1 - b_1 - b_2 \ge \mu$, since $F_1 \cap F_2 \supset W$ is not empty.

*The corollary.* If some $b_i > 1$, the prime divisor $F_i$ has $a = -b_i < -1$, so the pair is not sub-lc, and part 2 of Theorem 4.1.21 gives $\operatorname{discrep} = -\infty$, so it is not sub-plt, sub-canonical or sub-terminal. So assume every $b_i \le 1$. The divisors over $Y$ that are not exceptional are the prime divisors of $Y$, with discrepancy $-b_i$ for $F_i$ and $0$ for the others. Each part follows from the formula for $\operatorname{discrep}$. For part 1, every term of $\mu$ is greater than $-1$ when every $b_i < 1$, and at least $-1$ when every $b_i \le 1$. For part 2, the condition $\mu > -1$ fails only through a term $1 - b_i - b_j = -1$, that is $b_i = b_j = 1$ with $F_i \cap F_j \ne \emptyset$. Part 3 is the condition $\mu \ge 0$ or $\mu > 0$, term by term.

*The main theorem.* Every divisor over $X$ is a divisor over $Y$, and conversely, because $f$ is proper and birational: the valuation has a centre on $Y$ by the valuative criterion of properness. By Proposition 4.1.14, $a(E, X, \Delta) = a(E, Y, \Delta_Y)$ for all of them. A divisor $E$ over $X$ is exceptional over $X$ if and only if either it is exceptional over $Y$, or it is an $f$-exceptional prime divisor of $Y$. In the first case its centre on $X$ is the image of a subset of codimension at least 2, so it has codimension at least 2. The $f$-exceptional prime divisors are among the $F_i$, with discrepancy $-b_i$. This proves part 2. If some $b_i > 1$, then $a(F_i, X, \Delta) < -1$, and part 2 of Theorem 4.1.21, applied to $(X, \Delta)$ with $\dim X \ge 2$, gives part 3. For part 1, $\operatorname{totaldiscrep}(X, \Delta) = \operatorname{totaldiscrep}(Y, \Delta_Y)$, and the corollary decides it.

*Dlt implies lc.* Let $(X, \Delta)$ be dlt, with $Z$ as in the definition. Every coefficient is at most 1, so every prime divisor of $X$ has $a \ge -1$. Let $E$ be an exceptional divisor over $X$. If $c_X(E) \subset Z$, then $a(E) > -1$ by the definition. Otherwise $c_X(E)$ meets the open set $U = X \setminus Z$, where $(U, \Delta|_U)$ is snc with coefficients at most 1. By Corollary 4.1.15 and Theorem 4.2.12, $a(E, X, \Delta) = a(E, U, \Delta|_U) \ge \min\{1, 1 - b_i, 1 - b_i - b_j\} \ge -1$. In dimension 1 there are no exceptional divisors. $\square$

### Exercises

1. (A) Let $\Delta = c(L_1 + L_2 + L_3)$ with three concurrent lines in $\mathbb{A}^2$ and $0 \le c \le 1$. Show that one blow-up is a log resolution, that $\Delta_Y = c(L_1' + L_2' + L_3') + (3c - 1)E$, and that the pair is lc if and only if $c \le \frac23$ and klt if and only if $c < \frac23$.
2. (A) In the example of the cusp, show that $(\mathbb{A}^2, tC)$ is canonical if and only if $t \le \frac12$, and terminal if and only if $t < \frac12$.
3. (B) Let $(X, \Delta)$ be a pair with $\dim X \ge 2$ and $f$ a log resolution. Show that $(X, \Delta)$ is plt if and only if every $b_i \le 1$, every $f$-exceptional $F_i$ has $b_i < 1$, and the components of $\Delta_Y$ with coefficient 1 are disjoint. Deduce that the components of $\lfloor \Delta \rfloor$ of a plt pair do not meet on $Y$.
4. (B) Let $X$ be a normal variety with $K_X$ $\mathbb{Q}$-Cartier. Show that if $X$ is canonical, then it is klt. Show that $(X, 0)$ is klt if and only if it is plt, if and only if it is dlt.
5. (B) Let $\Delta = H_1 + H_2 + H_3$ be the three coordinate planes of $\mathbb{A}^3$. Compute $\operatorname{discrep}(\mathbb{A}^3, \Delta)$ and $a(E)$ for the blow-up of the origin. Show that the pair is dlt and lc, and not plt.
6. (C) Let $Y$ be smooth and $\Delta_Y = \sum_i b_i F_i$ with snc support and every $b_i \le 1$. Let $E$ be a divisor over $Y$ with $a(E, Y, \Delta_Y) = -1$. Use the logarithmic bound to show that the centre of $E$ is a component of $F_{i_1} \cap \dots \cap F_{i_c}$ for some components with $b_{i_1} = \dots = b_{i_c} = 1$, where $c$ is the codimension of the centre.

### Lean

The theorems of this section are not yet in Lean. The library has the snc condition `MinimalModel.IsSncAt`, which `MinimalModel.IsDlt` uses, and no notion of a log resolution. Because `MinimalModel.IsDlt` asks for `MinimalModel.IsLc`, the corollary that dlt implies lc is part of the Lean definition and not a theorem there.

### Notes and history

The formula for the discrepancy of an snc pair is KM98, Corollary 2.31. The proof by the logarithmic form is standard. It also shows the deeper fact of Exercise 6: on an snc pair with coefficients at most 1, the divisors with discrepancy $-1$ have as centres the strata of the coefficient 1 part. Kollár calls these centres the lc centres, and Kol13, Chapter 4, studies them. The reduction of every question about the classes to one log resolution is the reason that the theory of singularities of pairs needs Hironaka's theorem, and the reason that it is harder in positive characteristic.
