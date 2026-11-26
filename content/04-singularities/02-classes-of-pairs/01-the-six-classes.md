---
title: The six classes
nodes: []
sources: [KM98, Kol13, Sza94, Rei87]
reads_with: [KM98:ch2, Kol13:ch2]
requires: [4.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The six classes

### Statement

Let $(X, \Delta)$ be a pair: $X$ is normal, $\Delta = \sum_i d_i D_i$ is an effective $\mathbb{R}$-divisor, and $K_X + \Delta$ is $\mathbb{R}$-Cartier. The numbers $\operatorname{discrep}(X, \Delta)$ and $\operatorname{totaldiscrep}(X, \Delta)$ are those of Section 1.2: the infimum of $a(E, X, \Delta)$ over the exceptional divisors $E$ over $X$, and over all divisors $E$ over $X$.

**Definition 4.2.1 (the five classes of KM98).** The pair $(X, \Delta)$ is

1. *terminal* if $\operatorname{discrep}(X, \Delta) > 0$;
2. *canonical* if $\operatorname{discrep}(X, \Delta) \ge 0$;
3. *klt* (Kawamata log terminal) if $\operatorname{totaldiscrep}(X, \Delta) > -1$;
4. *plt* (purely log terminal) if $\operatorname{discrep}(X, \Delta) > -1$;
5. *lc* (log canonical) if $\operatorname{totaldiscrep}(X, \Delta) \ge -1$.

For a sub-pair the same conditions define sub-terminal, sub-canonical, sub-klt, sub-plt and sub-lc. A variety $X$ is terminal, canonical, klt or lc if $(X, 0)$ is, which includes the condition that $K_X$ is $\mathbb{Q}$-Cartier.

These are the definitions of KM98, Definition 2.34. By the box of Volume 0, Chapter 3: klt and lc test every divisor over $X$, exceptional or not, and so they include a condition on the coefficients of $\Delta$; terminal, canonical and plt test only the exceptional divisors.

The sixth class needs the notion of simple normal crossings. A pair $(X, \Delta)$ is *snc at* a point $x$ if $X$ is smooth at $x$ and the local equations at $x$ of the components of $\Delta$ through $x$ are part of a regular system of parameters of $\mathcal{O}_{X,x}$. The set of points where $(X, \Delta)$ is snc is open. Its complement is the *non-snc locus*.

**Definition 4.2.2 (dlt).** The pair $(X, \Delta)$ is *dlt* (divisorially log terminal) if every coefficient of $\Delta$ is at most 1 and there is a closed subset $Z \subset X$ such that $(X, \Delta)$ is snc at every point of $X \setminus Z$, and $a(E, X, \Delta) > -1$ for every divisor $E$ over $X$ with $c_X(E) \subset Z$.

This is the definition of Szabó (Sza94), which KM98, Chapter 2, also gives. Szabó proved that it is equivalent to the existence of a log resolution $f \colon Y \to X$ such that $a(E, X, \Delta) > -1$ for every $f$-exceptional divisor $E$. That theorem uses the resolution theorems of Hironaka in a strong form, and this volume uses it only as a black box (Sza94; KM98, Chapter 2).

**Theorem 4.2.3 (the implications).** Let $(X, \Delta)$ be a pair with $\dim X \ge 2$.

1. If $(X, \Delta)$ is terminal, every coefficient of $\Delta$ is less than 1. If it is canonical, plt or lc, every coefficient is at most 1.
2. Terminal implies canonical, and canonical implies plt.
3. Klt implies plt, plt implies dlt, and klt implies lc.
4. $(X, \Delta)$ is klt if and only if it is plt and every coefficient of $\Delta$ is less than 1. It is lc if and only if $\operatorname{discrep}(X, \Delta) \ge -1$.
5. If $(X, \Delta)$ is in one of the six classes and $0 \le \Delta' \le \Delta$ with $K_X + \Delta'$ $\mathbb{R}$-Cartier, then $(X, \Delta')$ is in the same class.

Lean: `MinimalModel.IsKlt.isLc` and `MinimalModel.IsTerminal.isCanonical` prove two of the implications of parts 2 and 3. The rest is not yet in Lean.

Corollary 4.2.15 in Section 2.2 completes the chain

$$\text{terminal} \Rightarrow \text{canonical} \Rightarrow \text{plt}, \qquad \text{klt} \Rightarrow \text{plt} \Rightarrow \text{dlt} \Rightarrow \text{lc}.$$

Canonical does not imply klt: $(\mathbb{A}^2, L)$ is canonical and not klt (Example below). With $\Delta = 0$, canonical implies klt, and klt, plt and dlt are the same (Exercise 4 of Section 2.2).

### Proof in words

Part 1 is the bound $\operatorname{discrep} \le 1 - d$ of Section 1.3, applied to the blow-up of a general codimension 2 subset of a component $D$: a positive discrepancy forces $d < 1$, a discrepancy at least 0 forces $d \le 1$. For plt and lc, a coefficient above 1 makes the discrepancies go to $-\infty$ by the bound $-1$. Parts 2 and 3 compare infima over smaller and larger sets of divisors. For plt implies dlt, take $Z$ to be the non-snc locus. It has codimension at least 2, so every divisor with centre in $Z$ is exceptional, and plt gives the bound on it. Part 5 holds because a smaller boundary has larger discrepancies.

### Examples

**Example 4.2.4 (a line in the plane).** The pair $(\mathbb{A}^2, L)$ is canonical, plt and dlt, and not klt and not terminal. The divisor $L$ has $a = -1$, so the pair is not klt. The blow-up of a point of $L$ has $a = 1 - 1 = 0$ by Lemma 4.1.20, so it is not terminal. Section 2.2 shows that every exceptional divisor has $a \ge 0$.

**Example 4.2.5 (two lines).** The pair $(\mathbb{A}^2, L_1 + L_2)$ with two lines through the origin has $a(E) = -1$ for the blow-up of the origin (Example 4.1.9). So it is not plt and not canonical. It is snc at every point, so $Z = \emptyset$ in the definition of dlt, and it is dlt. It is lc by Section 2.2. This is the standard example of a dlt pair that is not plt: the two components of $\lfloor \Delta \rfloor$ meet.

**Example 4.2.6 (the nodal cubic).** Let $C = \{y^2 = x^2(x + 1)\} \subset \mathbb{A}^2$. The pair $(\mathbb{A}^2, C)$ is lc and not dlt. The curve has a node at the origin, so it is not snc there: a prime divisor with a singular point is never snc at that point. The blow-up of the origin has $a(E) = 1 - 2 = -1$, and its centre is the origin, which lies in every $Z$ of the definition of dlt. So the pair is not dlt. On the blow-up the strict transform $C'$ meets $E$ in two points, transversally, and the crepant pullback $C' + E$ is snc. Section 2.2 shows that this makes the pair lc. Compare the two lines: analytically the node is the same, but the two branches belong to one prime divisor.

**Example 4.2.7 (three lines).** The pair $(\mathbb{A}^2, L_1 + L_2 + L_3)$ with three concurrent lines has $a(E) = -2$, so it is not lc. With coefficients $c$ the first blow-up gives $1 - 3c$, and the pair is lc if and only if $c \le \frac23$ (Exercise 1 of Section 2.2).

**Example 4.2.8 (the $A_1$ singularity and $\frac13(1,1)$).** The quadric cone $X = \{xy = z^2\}$ has a resolution with one exceptional curve and $a = 0$ (Example 4.1.8). Section 2.2 shows that this is the minimum, so $X$ is canonical and not terminal. The quotient $\frac13(1,1)$ has $a = -\frac13$ on its minimal resolution, so it is klt and not canonical (Section 2.3).

### Proof

Part 1. Let $D$ be a component of $\Delta$ with coefficient $d$. By Theorem 4.1.21, part 1, $\operatorname{discrep}(X, \Delta) \le 1 - d$. If the pair is terminal, $0 < 1 - d$, so $d < 1$. If it is canonical, $0 \le 1 - d$. If it is plt, then $\operatorname{discrep} > -1 > -\infty$, so part 3 of the same theorem gives $d \le 1$. If it is lc, $-d = a(D) \ge -1$.

Part 2. If $\operatorname{discrep} > 0$ then $\operatorname{discrep} \ge 0$, and if $\operatorname{discrep} \ge 0$ then $\operatorname{discrep} > -1$.

Part 3. $\operatorname{totaldiscrep} \le \operatorname{discrep}$, so klt implies plt, and $\operatorname{totaldiscrep} > -1$ implies $\operatorname{totaldiscrep} \ge -1$. Let $(X, \Delta)$ be plt and let $Z$ be the non-snc locus, a closed set. At the generic point $\eta$ of a component $D$ of $\Delta$, the local ring $\mathcal{O}_{X,\eta}$ is a discrete valuation ring since $X$ is normal, the local equation of $D$ is a uniformizer, and no other component passes. So the pair is snc at $\eta$, and $\eta \notin Z$. So $Z$ contains no prime divisor, and every divisor $E$ over $X$ with $c_X(E) \subset Z$ is exceptional. Plt gives $a(E) > -1$ for these. The coefficients are at most 1 by part 1. So the pair is dlt.

Part 4. Klt is the condition $\operatorname{discrep} > -1$ and $-d > -1$ for every component, since the divisors that are not exceptional are the prime divisors of $X$. That is plt and $d < 1$. For lc, $\operatorname{totaldiscrep} \ge -1$ implies $\operatorname{discrep} \ge -1$. Conversely, if $\operatorname{discrep} \ge -1$, part 3 of Theorem 4.1.21 gives $\operatorname{totaldiscrep} \ge -1$.

Part 5. Write $D = \Delta - \Delta' \ge 0$. It is $\mathbb{R}$-Cartier, as the difference of $K_X + \Delta$ and $K_X + \Delta'$. Near the centre of $E$, write $D = \sum_j s_j \operatorname{div}(g_j)$. Exercise 3 of Section 1.2 gives $a(E, X, \Delta') = a(E, X, \Delta) + \sum_j s_j v_E(g_j)$. On a model $Y$ where $E$ appears, $\sum_j s_j v_E(g_j)$ is the coefficient of $E$ in the effective divisor $f^*D$, so it is at least 0. So every discrepancy goes up or stays the same, and each of the five conditions of KM98 is kept. For dlt, the same $Z$ works: the snc condition outside $Z$ holds for every boundary supported in $\operatorname{Supp} \Delta$, and the bound on divisors with centre in $Z$ is kept. $\square$

### Exercises

1. (A) Let $(X, \Delta)$ be lc with $\dim X \ge 2$. Show that $-1 \le \operatorname{discrep}(X, \Delta) \le 1$.
2. (A) Show that $(\mathbb{A}^2, \frac12(L_1 + L_2 + L_3))$, for three concurrent lines, is not canonical.
3. (B) Let $(X, \Delta)$ be plt, and let $D_1$, $D_2$ be components of coefficient 1. Suppose that $D_1 \cap D_2$ contains a $Z$ of codimension 2 at whose generic point $X$, $D_1$ and $D_2$ are smooth and meet transversally. Show that this contradicts plt. Use Exercise 4 of Section 1.3.
4. (B) Show that the six classes are local: $(X, \Delta)$ is in a class if and only if every point has an open neighbourhood $U$ with $(U, \Delta|_U)$ in that class. Use Corollary 4.1.15.
5. (B) Let $X = \{xz = yw\}$ and $\Delta = D_1 + D_2$, where $\{x = 0\} \cap X = D_1 + D_2$ is the union of the planes $D_1 = \{x = y = 0\}$ and $D_2 = \{x = w = 0\}$. Show that $K_X + \Delta$ is Cartier and that $K_X + D_1$ is not $\mathbb{R}$-Cartier, so that the hypothesis of part 5 on $\Delta'$ is needed. Use Counterexample 4.1.10.

### Lean

The library defines four of the six classes. `MinimalModel.IsKlt` asks that every coefficient of $\Delta$ is less than 1 and that every divisorial valuation with a centre has positive log discrepancy. `MinimalModel.IsLc` asks for coefficients at most 1 and log discrepancies at least 0. These match klt and lc here: the divisorial valuations with a centre on $X$ are the divisors over $X$, including the prime divisors of $X$, and the explicit coefficient condition is needed in dimension 1 (Section 1.3). `MinimalModel.IsTerminal` and `MinimalModel.IsCanonical` ask for log discrepancy more than 1, or at least 1, at every exceptional divisorial valuation, with no condition on the coefficients, as in KM98. `MinimalModel.IsDlt` is Szabó's definition, written with `MinimalModel.IsSncAt`: the pair is lc, and there is a closed $Z$ outside which the pair is snc and over which every centre has positive log discrepancy. It includes lc as a hypothesis, which is a consequence in the definition here. Plt is not yet in Lean.

The file `MinimalModel/Fidelity/PointPairs.lean` checks the definitions on the pair of a point: `MinimalModel.pointPair_isKlt`, `MinimalModel.pointPair_isLc`, `MinimalModel.pointPair_isTerminal`, `MinimalModel.pointPair_isCanonical` and `MinimalModel.pointPair_isDlt`. A point has no divisorial valuations (`MinimalModel.pointVariety_not_isDivisorial`), so it is in every class.

### Notes and history

Reid defined canonical singularities in 1980 and terminal singularities in 1983, for $\Delta = 0$. Kawamata introduced the log terminal condition, and Shokurov the log canonical and purely log terminal conditions, in the 1980s, for the log minimal model program and the cone theorem with a boundary. The word dlt and the equivalence of the definitions are due to Szabó (Sza94). KM98, Chapter 2, explains why the program needs all of them: klt is the class of the cone and contraction theorems, terminal is the class that the program keeps for $\Delta = 0$ with $\mathbb{Q}$-factorial $X$, dlt is the class that adjunction to a component of $\lfloor \Delta \rfloor$ needs, and lc is the largest class in which the theorems still hold.
