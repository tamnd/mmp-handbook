---
title: Divisors over X and the independence of the model
nodes: []
sources: [KM98, Kol13, Rei87]
reads_with: [KM98:ch2, Kol13:ch2]
requires: [P3.11, P8.13, 4.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Divisors over X and the independence of the model

### Statement

Let $X$ be a normal variety of dimension $n$. The classes of singularities ask for a bound on $a(E, X, \Delta)$ for every divisor on every model. This section makes "every divisor over $X$" precise and proves that the discrepancy depends only on the divisor, not on the model where it appears.

**Definition 4.1.11 (divisor over $X$).** A *divisor over $X$* is a prime divisor $E$ on a normal variety $Y$ with a proper birational morphism $f \colon Y \to X$. Its valuation is $\operatorname{ord}_E \colon k(X)^* \to \mathbb{Z}$, the valuation of the discrete valuation ring $\mathcal{O}_{Y,E}$. Two divisors over $X$ are the same if they have the same valuation. The *centre* of $E$ on $X$ is $c_X(E) = f(E)$, a closed irreducible subset. The divisor $E$ is *exceptional* over $X$ if $c_X(E)$ has codimension at least 2.

The centre does not depend on the model. It is the closure of the point $x \in X$ whose local ring is dominated by the valuation ring: $\mathcal{O}_{X,x} \subset \mathcal{O}_{Y,E}$, and the maximal ideal of $\mathcal{O}_{X,x}$ lies in that of $\mathcal{O}_{Y,E}$. A divisor that is not exceptional is the strict transform of a prime divisor $D$ of $X$, and its valuation is $\operatorname{ord}_D$. The definition does not lose anything by asking $f$ to be proper. If $Y \to X$ is only birational, Nagata's compactification gives a proper $\bar Y \to X$ with $Y$ open in $\bar Y$, and the normalization of $\bar Y$ is an isomorphism over $Y$.

A theorem of Zariski describes the valuations that arise (KM98, Chapter 2). A valuation $v$ of $k(X)$ is $\operatorname{ord}_E$ for a divisor $E$ over $X$ if and only if $v$ is discrete with value group $\mathbb{Z}$, trivial on $k$, has a centre on $X$, and its residue field has transcendence degree $n - 1$ over $k$. Such a valuation is *divisorial*. This section uses the theorem only to compare with the Lean definitions.

Let $\omega$ be a nonzero rational top form and $v = \operatorname{ord}_E$. The valuation ring $R_v = \mathcal{O}_{Y,E}$ is a regular local ring essentially of finite type over $k$, so $\Omega^n_{R_v/k}$ is free of rank 1. Define $\operatorname{ord}_v(\omega)$ as the largest $m$ with $\omega \in t^m \Omega^n_{R_v/k}$, for a uniformizer $t$. It depends only on $R_v$, so only on $v$. It equals $\operatorname{ord}_E(\omega)$, the coefficient of $E$ in $\operatorname{div}_Y(\omega)$.

**Theorem 4.1.12 (independence of the model).** Let $(X, \Delta)$ be a sub-pair with $K_X = \operatorname{div}_X(\omega)$, and let $E$ be a divisor over $X$ with valuation $v$. Let $U \subset X$ be an open set that meets $c_X(E)$, with

$$(K_X + \Delta)|_U = \sum_i r_i \operatorname{div}_U(h_i), \qquad r_i \in \mathbb{R}, \quad h_i \in k(X)^*.$$

Then

$$a(E, X, \Delta) = \operatorname{ord}_v(\omega) - \sum_i r_i \, v(h_i), \qquad A(E, X, \Delta) = 1 + \operatorname{ord}_v(\omega) - \sum_i r_i \, v(h_i).$$

In particular $a(E, X, \Delta)$ depends only on $v$: two models $Y \to X$ and $Y' \to X$ on which $v$ is a prime divisor give the same discrepancy.

Lean: not yet in Lean. The definition `MinimalModel.LogDiscrepancyIs` takes the second formula as the definition of the log discrepancy, so the theorem says that the Lean definition agrees with Definition 4.1.4.

An $U$ as in the theorem exists. Write $K_X + \Delta = \sum_i r_i H_i$ with $H_i$ Cartier, pick a point $x \in c_X(E)$, and let $U$ be an open neighbourhood of $x$ on which each $H_i$ is principal, $H_i|_U = \operatorname{div}_U(h_i)$.

**Definition 4.1.13 (discrep and totaldiscrep).** For a sub-pair $(X, \Delta)$,

$$\operatorname{discrep}(X, \Delta) = \inf\{a(E, X, \Delta) : E \text{ exceptional over } X\}, \qquad \operatorname{totaldiscrep}(X, \Delta) = \inf\{a(E, X, \Delta) : E \text{ over } X\}.$$

The infimum of the empty set is $+\infty$. Since the non-exceptional divisors are the prime divisors $D$ of $X$, with $a = -\operatorname{mult}_D \Delta$,

$$\operatorname{totaldiscrep}(X, \Delta) = \min\bigl(\operatorname{discrep}(X, \Delta), \ \min_D (-\operatorname{mult}_D \Delta)\bigr),$$

where the minimum over $D$ counts $D$ with coefficient 0 as well, so the second term is at most 0.

Let $f \colon Y \to X$ be proper birational, $Y$ normal, and $K_Y + \Delta_Y = f^*(K_X + \Delta)$ as in Definition 4.1.4. The sub-pair $(Y, \Delta_Y)$ is the *crepant pullback* of $(X, \Delta)$. It is a sub-pair because $K_Y + \Delta_Y$ is the pullback of an $\mathbb{R}$-Cartier divisor. Every divisor over $Y$ is a divisor over $X$, by composition. Every divisor over $X$ is a divisor over $Y$: given $E$ on $Y'$, the normalization of the closure of the graph of the birational map $Y' \dashrightarrow Y$ is a model over both, and it is an isomorphism at the generic point of $E$ over $Y'$, so $E$ appears on it.

**Proposition 4.1.14 (crepant pullback).** Let $(Y, \Delta_Y)$ be the crepant pullback of $(X, \Delta)$ by $f$. Then $a(E, X, \Delta) = a(E, Y, \Delta_Y)$ for every divisor $E$ over $X$.

Lean: not yet in Lean.

**Corollary 4.1.15 (discrepancies are local).** Let $U \subset X$ be open, and let $E$ be a divisor over $X$ whose centre meets $U$. Then $E$ restricts to a divisor over $U$, and $a(E, X, \Delta) = a(E, U, \Delta|_U)$. So a statement of the form "$a(E, X, \Delta) > c$ for all $E$ with centre through $x$" depends only on a neighbourhood of $x$.

Lean: not yet in Lean.

### Proof in words

On a model $Y$ where $E$ is a divisor, the divisor $\Delta_Y$ is the difference $f^*(K_X + \Delta) - K_Y$. Near the generic point of $E$, the first term is $\sum_i r_i \operatorname{div}_Y(h_i)$, because the pullback of a principal divisor is the divisor of the pulled back function. The second term is $\operatorname{div}_Y(\omega)$. Read off the coefficient of $E$: it is $\sum_i r_i \operatorname{ord}_E(h_i) - \operatorname{ord}_E(\omega)$. Every quantity in this expression is computed in the local ring $\mathcal{O}_{Y,E}$, which is the valuation ring of $v$. The model has gone. For the crepant pullback, the pullback of $K_X + \Delta$ to a model over $Y$ is the same as the pullback of $K_Y + \Delta_Y$, and the form is the same, so the two discrepancies are the same coefficient of the same divisor.

### Examples

**Example 4.1.16 (the second blow-up).** Let $X = \mathbb{A}^2$, $\omega = dx \wedge dy$. Blow up the origin to get $E_1$, and in the chart $x = u$, $y = uv$ blow up the point $u = v = 0$ of $E_1$, in the chart $u = s$, $v = st$. The new exceptional curve $E_2$ is $\{s = 0\}$, and $x = s$, $y = s^2 t$. So $v_2 = \operatorname{ord}_{E_2}$ has $v_2(x) = 1$, $v_2(y) = 2$, and

$$dx \wedge dy = ds \wedge (2st \, ds + s^2 \, dt) = s^2 \, ds \wedge dt, \qquad a(E_2, \mathbb{A}^2, 0) = 2.$$

On the second model $Y_2$, the classical computation reads $K_{Y_2} = g^* K_{Y_1} + E_2 = g^*E_1 + E_2 = E_1' + 2E_2$, where $E_1'$ is the strict transform of $E_1$. The two computations agree, as the theorem says they must. The valuation $v_2$ also appears on the weighted blow-up of $\mathbb{A}^2$ with weights $(1, 2)$, a different model with a singular point, and gives the same number there.

**Example 4.1.17 (monomial valuations).** Let $w = (w_1, \dots, w_n)$ be a primitive vector of positive integers, and $v_w$ the valuation of $k(\mathbb{A}^n)$ with $v_w(\sum_\alpha c_\alpha x^\alpha) = \min\{\langle w, \alpha \rangle : c_\alpha \ne 0\}$. It is the valuation of the torus-invariant divisor of the star subdivision of the positive orthant at $w$. Write

$$dx_1 \wedge \dots \wedge dx_n = x_1 \cdots x_n \cdot \frac{dx_1}{x_1} \wedge \dots \wedge \frac{dx_n}{x_n}.$$

On a toric chart of the subdivision with monomial coordinates $y_1, \dots, y_n$, where $E_w = \{y_1 = 0\}$, the $x_i$ are monomials in the $y_j$ with an exponent matrix of determinant $\pm 1$. So the logarithmic form $\frac{dx_1}{x_1} \wedge \dots \wedge \frac{dx_n}{x_n}$ is $\pm \frac{dy_1}{y_1} \wedge \dots \wedge \frac{dy_n}{y_n}$, with a simple pole along $E_w$. Hence $\operatorname{ord}_{v_w}(\omega) = \sum_i w_i - 1$ and

$$a(E_w, \mathbb{A}^n, 0) = w_1 + \dots + w_n - 1.$$

This is Volume 3, Theorem 3.3.34, for the cone of $\mathbb{A}^n$, where $m_\sigma = (1, \dots, 1)$. The weights $(1, 1)$ and $(1, 2)$ give the first and second blow-ups above.

**Example 4.1.18 (a valuation with no centre).** Let $X = \mathbb{A}^2 \subset \mathbb{P}^2$ and let $v$ be the valuation of the line at infinity. Then $v(x) = -1$. A function $x \in \mathcal{O}(X)$ with negative value means that no local ring of $X$ lies in the valuation ring, so $v$ has no centre on $X$. It is a divisorial valuation of $k(X)$ but not a divisor over $X$, and it plays no part in the classes of singularities of $X$. The Lean definitions skip it in the same way: `MinimalModel.LogDiscrepancyIs` needs a centre.

**Example 4.1.19 (a crepant pullback).** Let $(X, \Delta) = (\mathbb{A}^2, c(L_1 + L_2))$ and let $f$ be the blow-up of the origin. By Example 4.1.9 the crepant pullback is $(Y, c(L_1' + L_2') + (2c - 1)E)$. The proposition says that every divisor over $\mathbb{A}^2$ has the same discrepancy for both. For instance, the divisor $F$ of the blow-up of $E \cap L_1'$ has, by Exercise 4 of Section 1.1, $a(F, Y, \Delta_Y) = 1 - c - (2c - 1) = 2 - 3c$. The same $F$ is the monomial valuation with weights $(2, 1)$ in coordinates where $L_1 = \{x = 0\}$ and $L_2 = \{y = 0\}$, and the theorem gives $a = (2 + 1 - 1) - c(2 + 1) = 2 - 3c$.

### Proof

*Proof of the theorem.* Let $f \colon Y \to X$ be a model where $E$ is a prime divisor, so $v = \operatorname{ord}_E$. Since $f(E) = c_X(E)$ meets $U$, the open set $E \cap f^{-1}(U)$ of $E$ is not empty. On $f^{-1}(U)$ the pullback of the principal Cartier divisor $\operatorname{div}_U(h_i)$ is $\operatorname{div}_{f^{-1}(U)}(h_i)$. By Lemma 4.1.2,

$$f^*(K_X + \Delta)|_{f^{-1}(U)} = \sum_i r_i \operatorname{div}_{f^{-1}(U)}(h_i).$$

With $K_Y = \operatorname{div}_Y(\omega)$, the definition $\Delta_Y = f^*(K_X + \Delta) - K_Y$ gives on $f^{-1}(U)$

$$\Delta_Y = \sum_i r_i \operatorname{div}(h_i) - \operatorname{div}(\omega).$$

Take the coefficient of $E$, which is visible on $f^{-1}(U)$: $\operatorname{mult}_E \Delta_Y = \sum_i r_i \operatorname{ord}_E(h_i) - \operatorname{ord}_E(\omega)$. So $a(E, X, \Delta) = \operatorname{ord}_v(\omega) - \sum_i r_i v(h_i)$. The right side uses only $v$, the form $\omega$ and the data $(U, r_i, h_i)$. The left side does not depend on $(U, r_i, h_i)$, by Lemma 4.1.2, and not on $\omega$, by Lemma 4.1.5. So neither side depends on any choice, and two models give the same value. $\square$

*Proof of the proposition.* Let $g \colon Z \to Y$ be a model where $E$ is a prime divisor, so $f \circ g \colon Z \to X$ is a model over $X$. Use the same $\omega$ on $X$, $Y$ and $Z$, so $K_Y = \operatorname{div}_Y(\omega)$ and $K_Z = \operatorname{div}_Z(\omega)$. Pullback of Cartier divisors is functorial, $g^* f^* = (f \circ g)^*$, and so it is for $\mathbb{R}$-Cartier divisors. Then

$$K_Z + (\Delta_Y)_Z = g^*(K_Y + \Delta_Y) = g^* f^*(K_X + \Delta) = (f \circ g)^*(K_X + \Delta) = K_Z + \Delta_Z.$$

So $(\Delta_Y)_Z = \Delta_Z$, and the coefficients of $E$ agree. $\square$

*Proof of the corollary.* Take $U' \subset U$ as in the theorem, with $U'$ meeting $c_X(E)$. The same $U'$, $r_i$, $h_i$ and $\omega$ serve for $(U, \Delta|_U)$, and the valuation of $E$ is the same. The formula gives the same number. $\square$

### Exercises

1. (A) Let $v$ be the monomial valuation of $\mathbb{A}^3$ with weights $(1, 1, 2)$. Compute $a(E_v, \mathbb{A}^3, 0)$ and $a(E_v, \mathbb{A}^3, H)$ for $H = \{z = 0\}$.
2. (A) Show that $\operatorname{totaldiscrep}(X, \Delta) \le 0$ for every sub-pair, and that $\operatorname{discrep}(X, \Delta) = +\infty$ when $\dim X = 1$.
3. (B) Let $(X, \Delta)$ be a sub-pair and $D$ an effective $\mathbb{R}$-Cartier divisor. Show that $a(E, X, \Delta + D) = a(E, X, \Delta) - v_E(D)$, where $v_E(D) = \sum_i r_i v_E(h_i)$ for a local presentation $D = \sum_i r_i \operatorname{div}(h_i)$ near the centre. Deduce that discrepancies go down when the boundary goes up.
4. (B) Let $p \in \mathbb{A}^2$ and $E_1$, $E_2$ the divisors of the first and the second blow-up in Example 4.1.16. Show that the centre of $E_2$ on the first blow-up $Y_1$ is a point of $E_1$, and that the centre of $E_2$ on $\mathbb{A}^2$ is $p$.
5. (B) Let $(X, \Delta)$ be a sub-pair and $\phi \colon X \to X$ an automorphism with $\phi^* \Delta = \Delta$. Show that $a(\phi^* E, X, \Delta) = a(E, X, \Delta)$ for every divisor $E$ over $X$, where $\phi^*E$ is the divisor with valuation $v_E \circ \phi^*$.
6. (C) Let $v$ be a divisorial valuation of $\mathbb{A}^2$ with centre the origin, and $E$ a prime divisor with valuation $v$ on a smooth model. Write $dx \wedge dy = xy \cdot \frac{dx}{x} \wedge \frac{dy}{y}$, and show that the logarithmic form has at most a simple pole along $E$. Deduce $a(E, \mathbb{A}^2, 0) \ge v(x) + v(y) - 1$, with equality for the monomial valuations. Section 2.2 proves this bound in general.

### Lean

`MinimalModel.IsDivisorial` is the condition of Zariski's theorem: value group $\mathbb{Z}$, trivial on $k$, and $n - 1$ elements of the valuation ring that stay algebraically independent in the residue field. `MinimalModel.IsCentre` says that a point is the centre of a valuation, and `MinimalModel.IsExceptional` says that no centre is a prime divisor of $X$. `MinimalModel.FormOrd` is $\operatorname{ord}_v(\omega)$, defined by the forms $g\omega$ that are regular on the valuation ring. `MinimalModel.LogDiscrepancyIs` is the formula of the theorem for the log discrepancy $A$, with an open set $U$ that contains the centre and on which $K + \Delta = \sum_i r_i \operatorname{div}(h_i)$. The theorem itself, the agreement with a model, is not yet in Lean, and neither is the proposition on crepant pullbacks.

### Notes and history

The idea that a discrepancy belongs to a valuation and not to a divisor on one model is in Reid's work and in KM98, Chapter 2, where the divisors over $X$ are defined up to the equivalence of their valuations. Zariski's theorem on divisorial valuations is from his work on the resolution of surfaces and 3-folds in the 1940s. The formula with $\operatorname{ord}_v(\omega)$ is the one that the Lean library chose, because it needs no resolution of singularities and no model, and so it can be stated before the library has blow-ups.
