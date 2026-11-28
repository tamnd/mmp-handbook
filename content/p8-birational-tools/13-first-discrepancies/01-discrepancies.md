---
title: Discrepancies and the classes of singularities
nodes: []
sources: [KM98, Rei87, Kol13]
reads_with: [KM98:2.3, Rei87:all, Kol13:2.1]
requires: [P3.9, P3.12, P8.9, P8.12]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Discrepancies and the classes of singularities

### Statement

In this chapter $X$ is a normal variety of dimension $n$ over the algebraically closed field $k$, and $K_X$ is $\mathbb{Q}$-Cartier, so that some multiple $m K_X$ with $m \geq 1$ is Cartier (Definition P3.9.18). A *model* of $X$ is a proper birational morphism $g \colon Y \to X$ from a normal variety. Fix a nonzero rational $n$-form $\omega$ on $X$; since $k(Y) = k(X)$, it is also a rational $n$-form on every model, and by Proposition P3.12.29 its divisors $K_X = \operatorname{div}_X(\omega)$ and $K_Y = \operatorname{div}_Y(\omega)$ are canonical divisors with $g_* K_Y = K_X$. For a $\mathbb{Q}$-Cartier divisor $B$ on $X$, $g^* B$ is the $\mathbb{Q}$-divisor of Proposition P3.9.28.

**Definition P8.13.1 (divisors over $X$ and discrepancies).** A *divisor over $X$* is a prime divisor $F$ on some model $g \colon Y \to X$. Two divisors over $X$ are identified when they define the same valuation $\operatorname{ord}_F$ of $k(X)$, that is, when their local rings $\mathcal{O}_{Y, F} \subseteq k(X)$ coincide. The *centre* of $F$ is the closure $c_X(F) = \overline{g(F)}$, and $F$ is *exceptional* if $c_X(F)$ has codimension at least $2$. The *discrepancy* of $F$ is the coefficient
$$a(F, X) = \operatorname{ord}_F (K_Y - g^* K_X),$$
so that $K_Y = g^* K_X + \sum_F a(F, X) F$, the sum running over the prime divisors of $Y$, with $a(F, X) = 0$ for every non-exceptional $F$.

**Lemma P8.13.2 (independence of the model).** The number $a(F, X)$ depends only on the valuation $\operatorname{ord}_F$, not on the model $Y$ on which $F$ appears and not on $\omega$. In particular the discrepancy $a(E, X)$ of the exceptional divisor of a cone in Section 12.2, computed on the total space of $L^{-1}$, is an invariant of the valuation $\operatorname{ord}_E$.

Lean: not in Lean as stated.

**Lemma P8.13.3 (discrepancies over a model).** Let $f \colon Y \to X$ be a model with $Y$ smooth, and write $K_Y = f^* K_X + A$ with $A = \sum_i a(E_i, X) E_i$. For every divisor $F$ over $Y$, which is also a divisor over $X$,
$$a(F, X) = a(F, Y) + \operatorname{ord}_F(A).$$

Lean: not in Lean as stated.

**Proposition P8.13.4 (discrepancies over smooth varieties).** Let $X$ be smooth.

1. If $Z \subseteq X$ is a smooth closed subvariety of codimension $c \geq 2$ and $E$ the exceptional divisor of $\operatorname{Bl}_Z X \to X$, then $a(E, X) = c - 1$.
2. Every exceptional divisor $F$ over $X$ has $a(F, X) \geq 1$.

Lean: not in Lean as stated.

**Definition P8.13.5 (terminal, canonical, klt and log canonical).** The variety $X$, with $K_X$ $\mathbb{Q}$-Cartier, is

1. *terminal* if $a(F, X) > 0$ for every exceptional divisor $F$ over $X$;
2. *canonical* if $a(F, X) \geq 0$ for every exceptional divisor $F$ over $X$;
3. *klt* (Kawamata log terminal) if $a(F, X) > -1$ for every divisor $F$ over $X$;
4. *log canonical* if $a(F, X) \geq -1$ for every divisor $F$ over $X$.

A point $x \in X$ has one of these properties if some neighbourhood of $x$ does. Terminal implies canonical implies klt implies log canonical; for the middle implication, non-exceptional divisors have discrepancy $0$.

**Proposition P8.13.6 (the test on a log resolution).** Let $f \colon Y \to X$ be a resolution whose exceptional set is a divisor $E_1 \cup \dots \cup E_r$ with simple normal crossings, and $a_i = a(E_i, X)$. Then $X$ is terminal, canonical, klt or log canonical if and only if every $a_i$ is $> 0$, $\geq 0$, $> -1$ or $\geq -1$ respectively.

Lean: not in Lean as stated.

### Proof in words

A discrepancy compares two divisors attached to the same rational form, the divisor of the form on a model and the pullback of its divisor on $X$; both are orders of vanishing in the discrete valuation ring of $F$, so only the valuation matters. Pulling back in two steps gives the transitivity formula. On a smooth variety a regular top form pulls back to a form that vanishes along every exceptional divisor, because the morphism cannot be étale at a point of a positive-dimensional fibre; the local computation of a blow-up gives the exact value $c - 1$. On a log resolution the transitivity formula and the inequality $a(F, Y) \geq \sum_i \operatorname{ord}_F(E_i) - 1$ reduce all divisors over $X$ to the $E_i$.

### Examples

**Example P8.13.7 (smooth varieties).** By part 2 of Proposition P8.13.4 every smooth variety is terminal. The blow-up of a point of a smooth $n$-fold has discrepancy $n - 1$; for $n = 2$ this is $K_{\tilde X} = \pi^* K_X + E$ of Theorem P3.12.32.

**Example P8.13.8 (the quadric cone).** Let $X = \frac{1}{2}(1, 1) = \{ xz = y^2 \}$. By Example P8.12.12 the resolution $Y$ of Proposition P8.12.3 has one exceptional curve $E \cong \mathbb{P}^1$ and $a(E, X) = 0$. A single smooth curve is a divisor with simple normal crossings, so by Proposition P8.13.6, $X$ is canonical, and it is not terminal because $a(E, X) = 0$.

**Example P8.13.9 (the singularities $\frac{1}{n}(1, 1)$).** By Example P8.12.12, $a(E, X) = -\frac{n - 2}{n}$ for $\frac{1}{n}(1, 1)$. By Proposition P8.13.6 the vertex is klt for every $n \geq 2$, canonical only for $n = 2$, and never terminal. The discrepancies $-\frac{1}{3}, -\frac{1}{2}, -\frac{3}{5}, \dots$ accumulate at $-1$ as $n \to \infty$.

**Example P8.13.10 (cones over plane curves).** By Example P8.12.14 the cone over a smooth plane curve of degree $e$ has $a(E, X) = 2 - e$. By Proposition P8.13.6 the elliptic cone, $e = 3$, is log canonical but not klt, and for $e \geq 4$ the cone is not log canonical. The cone over a plane quartic has $a(E, X) = -2$.

**Example P8.13.11 (the singularity $\frac{1}{2}(1, 1, 1)$).** By Example P8.12.13, the resolution of $\frac{1}{2}(1, 1, 1)$ by the total space of $\mathcal{O}_{\mathbb{P}^2}(-2)$ has one exceptional divisor $E \cong \mathbb{P}^2$ with $a(E, X) = \frac{1}{2}$, and $E$ is smooth. By Proposition P8.13.6, $X$ is terminal. Its canonical class has index $2$, so terminal singularities need not be Gorenstein. More generally $\frac{1}{d}(1, \dots, 1)$ in dimension $n$ is terminal for $d < n$, canonical for $d = n$, and klt for all $d$.

### Proof

*Lemma P8.13.2.* Let $F$ be a prime divisor on a model $g \colon Y \to X$, and $\mathcal{O} = \mathcal{O}_{Y, F}$, a discrete valuation ring because $Y$ is normal. Since $Y$ is normal, it is regular, hence smooth over the algebraically closed field $k$, at the generic point of $F$, so $\Omega^n_{\mathcal{O}/k}$ is free of rank one; the coefficient of $F$ in $K_Y = \operatorname{div}_Y(\omega)$ is the order in $\mathcal{O}$ of $\omega$ relative to a generator. This depends only on the subring $\mathcal{O} \subseteq k(X)$. Let $x$ be the generic point of $c_X(F)$, the image of the generic point of $F$, and $\varphi \in k(X)$ a local equation of $m K_X$ at $x$. Then $g^*(m K_X) = \operatorname{div}_Y(\varphi)$ near the generic point of $F$ (Definition P3.9.26), so the coefficient of $F$ in $g^* K_X$ is $\frac{1}{m} \operatorname{ord}_F(\varphi)$, and $\varphi$ depends only on $x$. The point $x$ is determined by $\mathcal{O}$: it is the unique point of the separated scheme $X$ whose local ring is dominated by $\mathcal{O}$, the centre of the valuation. So $a(F, X)$ depends only on $\mathcal{O}$. Replacing $\omega$ by $h \omega$ with $h \in k(X)^*$ adds $\operatorname{div}_Y(h)$ to $K_Y$ and $\operatorname{div}_X(h)$ to $K_X$, and $g^* \operatorname{div}_X(h) = \operatorname{div}_Y(h)$, so the difference does not change. In Section 12.2 the canonical divisors were chosen with $f_* K_Y = K_X$, and any two such choices differ by $\operatorname{div}(h)$ as above.

*Lemma P8.13.3.* Let $h \colon Y' \to Y$ be a model of $Y$ on which $F$ is a prime divisor; then $g = f \circ h$ is a model of $X$. With all canonical divisors defined by the same $\omega$, Proposition P3.9.28 gives $g^* K_X = h^* f^* K_X$, and $h^* A$ is defined because $Y$ is smooth. So
$$K_{Y'} - g^* K_X = (K_{Y'} - h^* K_Y) + h^*(K_Y - f^* K_X) = (K_{Y'} - h^* K_Y) + h^* A,$$
and taking the coefficient of $F$ gives the formula.

*Proposition P8.13.4.* (1) The statement is local, so let $x_1, \dots, x_n$ be local coordinates on $X$ near a point of $Z$ with $Z = \{ x_1 = \dots = x_c = 0 \}$, and $\omega = dx_1 \wedge \dots \wedge dx_n$, so $K_X = 0$ near the point. One chart of the blow-up has coordinates $y_1, \dots, y_n$ with $x_1 = y_1$, $x_i = y_1 y_i$ for $2 \leq i \leq c$ and $x_i = y_i$ for $i > c$, and $E = \{ y_1 = 0 \}$ there. Then $dx_i = y_1 \, dy_i + y_i \, dy_1$ for $2 \leq i \leq c$, and
$$dx_1 \wedge \dots \wedge dx_n = y_1^{c - 1} \, dy_1 \wedge \dots \wedge dy_n,$$
so $K_Y = (c - 1) E$ on the chart and $a(E, X) = c - 1$.

(2) Let $F$ be a prime divisor on a model $g \colon Y \to X$ with $Z = c_X(F)$ of codimension at least $2$, $\eta$ the generic point of $F$ and $x = g(\eta)$ the generic point of $Z$. Near $x$ take $\omega = dx_1 \wedge \dots \wedge dx_n$ for local coordinates, so $K_X = 0$ there, and $a(F, X) = \operatorname{ord}_F(g^* \omega)$. The pullback $g^* \omega$ is a regular $n$-form at $\eta$, so $a(F, X) \geq 0$. If $a(F, X) = 0$, then $g^* \omega$ generates $\Omega^n_{Y, \eta}$, so the map $g^* \Omega_X \to \Omega_Y$ of free modules of rank $n$ at $\eta$ has unit determinant and is an isomorphism, and $\Omega_{Y/X, \eta} = 0$. Then $g$ is unramified at $\eta$, so $\eta$ is an isolated point of its fibre $g^{-1}(x)$. But $F \subseteq g^{-1}(Z)$ and $\dim F = n - 1 > \dim Z$, so the fibre of $F \to Z$ over $x$ has dimension $\dim F - \dim Z \geq 1$ at $\eta$, a contradiction. So $a(F, X) \geq 1$.

*Proposition P8.13.6.* The conditions are necessary, since the $E_i$ are exceptional divisors over $X$. For sufficiency, let $F$ be a divisor over $X$. If $F$ is a divisor on $Y$, it is some $E_i$ or non-exceptional, with discrepancy $0$. Otherwise $F$ is exceptional over $Y$, with centre $W$ on $Y$, and Lemma P8.13.3 gives
$$a(F, X) = a(F, Y) + \sum_i a_i \operatorname{ord}_F(E_i),$$
where $\operatorname{ord}_F(E_i) \geq 1$ exactly for the set $I$ of indices with $W \subseteq E_i$ and is $0$ otherwise. Since $\sum_i E_i$ has simple normal crossings on the smooth variety $Y$, Kollár and Mori, Section 2.3 (KM98, Lemma 2.29 and Corollary 2.31), give
$$a(F, Y) \geq \sum_{i \in I} \operatorname{ord}_F(E_i) - 1,$$
and part 2 of Proposition P8.13.4 gives $a(F, Y) \geq 1$, which is the bound when $I$ is empty. Hence
$$a(F, X) \geq -1 + \sum_{i \in I} (1 + a_i) \operatorname{ord}_F(E_i) \quad \text{if } I \neq \emptyset, \qquad a(F, X) \geq 1 \quad \text{if } I = \emptyset.$$
If every $a_i \geq -1$, the right side is at least $-1$. If every $a_i > -1$ and $I \neq \emptyset$, it is greater than $-1$. If every $a_i \geq 0$, it is at least $-1 + |I| \geq 0$. If every $a_i > 0$, then for $I = \{ i \}$ it is at least $-1 + (1 + a_i) = a_i > 0$, and for $|I| \geq 2$ it is at least $1$. In each case $a(F, X)$ satisfies the required inequality.

### Exercises

1. (A) Let $X$ be smooth and $F$ the exceptional divisor of the blow-up of a point $p$ on the exceptional divisor $E$ of $\operatorname{Bl}_q X \to X$, with $\dim X = 2$. Using Lemma P8.13.3, show that $a(F, X) = 2$.
2. (A) Show that $\frac{1}{3}(1, 1, 1)$ is canonical but not terminal, and that $\frac{1}{4}(1, 1, 1)$ is klt but not canonical.
3. (B) Let $X$ be a normal surface and $x \in X$ a log canonical point whose minimal resolution has a single exceptional curve $E$. Show that $K_Y \cdot E = a(E, X) E^2$, deduce from the genus formula that $p_a(E) \leq 1$, and show that $a(E, X) = -1$ if $p_a(E) = 1$.
4. (B) In the situation of Proposition P8.13.6 with every $a_i > -1$, show that every exceptional divisor $F$ over $X$ satisfies $a(F, X) \geq \min(1, a_1, \dots, a_r)$.
5. (B) Show that if $a(F, X) < -1$ for one divisor $F$ over $X$, then $\inf_F a(F, X) = -\infty$, by blowing up a general point of $F$ repeatedly and using Lemma P8.13.3 and part 1 of Proposition P8.13.4.
6. (C) Show that a Gorenstein variety with rational singularities is canonical, using part 2 of Corollary P4.9.22 and Proposition P8.13.6, and that the cone over a smooth quadric surface is terminal.

### Lean

The predicates `MinimalModel.IsTerminal`, `MinimalModel.IsCanonical`, `MinimalModel.IsKlt` and `MinimalModel.IsLc` in `MinimalModel/Statements/Basic.lean` state Definition P8.13.5 for pairs $(X, \Delta)$ in terms of divisorial valuations, through `MinimalModel.LogDiscrepancyIs`, which records the log discrepancy $1 + a(F, X)$. For $\Delta = 0$ the conditions there, log discrepancy $> 1$, $\geq 1$, $> 0$ and $\geq 0$, are the four conditions of Definition P8.13.5. The statements of this section are not in Lean as stated.

### Notes and history

Discrepancies were introduced by Reid in the study of canonical models of threefolds, and Reid's Young Person's Guide (Rei87) gives the first systematic account; the names terminal and canonical come from the singularities of terminal and canonical models. Kollár and Mori, Section 2.3 (KM98), treat discrepancies of pairs, prove Proposition P8.13.6 in that generality, and show that if some $a(F, X) < -1$ then the discrepancies are unbounded below, which is Exercise 5. Kollár (Kol13), Chapter 2, collects the later theory, including the minimal log discrepancy.
