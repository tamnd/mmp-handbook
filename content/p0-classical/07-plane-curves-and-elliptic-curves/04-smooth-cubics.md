---
title: Smooth cubics, the group law and the j-invariant
nodes: []
sources: [Sil09, Rei88, Ful69, Har77]
reads_with: [Sil09:ch3, Rei88:ch2, Ful69:ch5]
requires: [P0.4, P0.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Smooth cubics, the group law and the j-invariant

### Statement

In this section $\operatorname{char} k \neq 2, 3$. A *flex* of a plane curve $F$ is a smooth point $P$ with $I(P, F \cap T_P) \ge 3$, where $T_P$ is the tangent line at $P$.

**Definition P0.7.23.** A *Weierstrass cubic* is the projective curve
$$
E_{a, b} : \ Y^2 Z = X^3 + a X Z^2 + b Z^3, \qquad a, b \in k,
$$
with the affine equation $y^2 = x^3 + ax + b$ and the point $O = [0 : 1 : 0]$ at infinity. Its *discriminant* is $\Delta = -16(4a^3 + 27b^2)$. If $\Delta \neq 0$, its *j-invariant* is
$$
j = 1728 \cdot \frac{4a^3}{4a^3 + 27b^2} .
$$

Lean: Mathlib `WeierstrassCurve`, `WeierstrassCurve.Δ` and `WeierstrassCurve.j`; Mathlib uses the general form with $a_1, \dots, a_6$ and $j = c_4^3/\Delta$, which gives the formula above for $a_1 = a_2 = a_3 = 0$.

**Example P0.7.24.** The curve $y^2 = x^3 + 1$ has $a = 0$, $b = 1$, $\Delta = -432 \neq 0$ and $j = 0$.

**Example P0.7.25.** The curve $y^2 = x^3 - x$ has $a = -1$, $b = 0$, $\Delta = 64$ and $j = 1728$.

**Proposition P0.7.26 (smoothness of a Weierstrass cubic).** The curve $E_{a, b}$ is smooth if and only if $4a^3 + 27b^2 \neq 0$. The point $O$ is a smooth flex of $E_{a, b}$ for all $a, b$, with tangent line $Z = 0$.

Lean: Mathlib `WeierstrassCurve.IsElliptic` is the condition that $\Delta$ is a unit.

*Proof.* In the chart $Y = 1$ the equation is $z = x^3 + a x z^2 + b z^3$. Its linear part is $z$, so $O$ is smooth with tangent line $z = 0$. On $z = 0$ the equation is $x^3 = 0$, so $I(O, E \cap \{Z = 0\}) = 3$ and $O$ is a flex. It is the only point with $Z = 0$. In the chart $Z = 1$, let $p(x) = x^3 + ax + b$. A singular point satisfies $2y = 0$, $p'(x) = 0$ and $y^2 = p(x)$, so $y = 0$ and $x$ is a multiple root of $p$. The cubic $p$ has a multiple root if and only if its discriminant $-(4a^3 + 27b^2)$ is 0. $\square$

**Theorem P0.7.27 (Weierstrass normal form).** Let $F$ be a smooth plane cubic with a flex $O$. Then there is a projective change of coordinates that sends $O$ to $[0 : 1 : 0]$ and $F$ to a Weierstrass cubic $E_{a, b}$ with $4a^3 + 27b^2 \neq 0$.

Lean: not in Lean; Mathlib has the change of variables `WeierstrassCurve.VariableChange` between general Weierstrass equations.

*Proof.* Choose coordinates with $O = [0 : 1 : 0]$ and the tangent line $T_O = \{Z = 0\}$. The curve $F$ is irreducible by Section 7.2, so $Z$ does not divide $F$. By the Proposition on a curve and a line in Section 7.2, $F(X, Y, 0)$ is a binary cubic form with a root of order 3 at $[0 : 1]$, so $F(X, Y, 0) = c X^3$ with $c \neq 0$. Hence
$$
F = c X^3 + Z \, Q(X, Y, Z)
$$
with $Q$ a quadratic form. In the chart $Y = 1$, the linear part of $F$ at $O$ is $Q(0, 1, 0)\, z$, so smoothness at $O$ gives $Q(0, 1, 0) \neq 0$: the coefficient of $Y^2$ in $Q$ is not 0. Divide $F$ by this coefficient and replace $X$ by $\mu X$ with a suitable $\mu \in k$. This gives
$$
F = Y^2 Z + a_1 XYZ + a_3 Y Z^2 - (X^3 + a_2 X^2 Z + a_4 X Z^2 + a_6 Z^3).
$$
As $\operatorname{char} k \neq 2$, replace $Y$ by $Y - \frac12 (a_1 X + a_3 Z)$ to remove the terms $XYZ$ and $YZ^2$. As $\operatorname{char} k \neq 3$, replace $X$ by $X - \frac13 a_2' Z$, where $a_2'$ is the new coefficient of $X^2 Z$, to remove it. The result is $Y^2 Z = X^3 + aXZ^2 + bZ^3$. These substitutions fix $O$ and the line $Z = 0$. The curve is smooth, so $4a^3 + 27b^2 \neq 0$ by the Proposition. $\square$

**Remark P0.7.28.** Every smooth plane cubic has a flex. If $\operatorname{char} k = 0$, the flexes are the points of $F$ on the Hessian curve $\det(\partial^2 F/\partial X_i \partial X_j) = 0$, which has degree 3 and meets $F$ by Bézout's theorem; a smooth cubic has exactly 9 flexes. A flex exists in every characteristic. Silverman (Ch. III) gets the Weierstrass form of an elliptic curve from the Riemann-Roch theorem, without a Hessian.

**Definition P0.7.29.** Let $E$ be a smooth cubic with a flex $O$. For $P, Q \in E$, let $P * Q$ be the third point of $E$ on the line $PQ$, or on the tangent line at $P$ if $P = Q$. By Section 7.2 this point exists and is unique, counted with multiplicity. Put
$$
P + Q = O * (P * Q).
$$

Lean: Mathlib defines the addition on `WeierstrassCurve.Affine.Point`, the type of $O$ and the smooth affine points, by the formulas below.

**Theorem P0.7.30 (group law).** With this addition, $E$ is an abelian group with identity $O$. On $E_{a, b}$ the inverse of $P = (x, y)$ is $-P = (x, -y)$. For $P_1 = (x_1, y_1)$ and $P_2 = (x_2, y_2)$ with $P_2 \neq -P_1$, the sum $P_1 + P_2 = (x_3, y_3)$ is
$$
x_3 = \lambda^2 - x_1 - x_2, \qquad y_3 = -\bigl(\lambda (x_3 - x_1) + y_1\bigr),
$$
where $\lambda = \frac{y_2 - y_1}{x_2 - x_1}$ if $x_1 \neq x_2$, and $\lambda = \frac{3x_1^2 + a}{2y_1}$ if $P_1 = P_2$.

Lean: Mathlib `WeierstrassCurve.Affine.Point` has an `AddCommGroup` instance (proved in Mathlib, associativity included).

*Proof.* The operation is symmetric in $P$ and $Q$, so it is commutative. As $O$ is a flex, $O * O = O$. The line through $O$ and $O * P$ meets $E$ in $O$, $O * P$ and $P$, so $P + O = O * (O * P) = P$. The projective line $X = x_0 Z$ passes through $O$ and meets $E_{a, b}$ at $(x_0, \pm y_0)$. So $P * (x_0, -y_0) = O$ for $P = (x_0, y_0)$, and $P + (x_0, -y_0) = O * O = O$. This gives the inverse. For the formulas, let $y = \lambda x + \nu$ be the line through $P_1$ and $P_2$, or the tangent line at $P_1$ (by implicit differentiation, $2y\, y' = 3x^2 + a$ gives the slope). Substitution gives
$$
x^3 - \lambda^2 x^2 + (a - 2\lambda\nu) x + (b - \nu^2) = 0,
$$
whose three roots are $x_1$, $x_2$ and the $x$-coordinate of $P_1 * P_2$. Their sum is $\lambda^2$, so $P_1 * P_2 = (x_3, \lambda(x_3 - x_1) + y_1)$, and $P_1 + P_2$ is its reflection in the $x$-axis. Associativity is the hard part. Silverman (Ch. III) proves it with the Riemann-Roch theorem and the Picard group, and Fulton (Ch. 5) proves it with a theorem on cubics through eight points; a direct check with the formulas is long. Mathlib proves it with the class group of the coordinate ring. $\square$

**Proposition P0.7.31 (j-invariant).** Let $E_{a, b}$ and $E_{a', b'}$ be smooth. Then $j(E_{a, b}) = j(E_{a', b'})$ if and only if there is $u \in k^*$ with $a' = u^{-4} a$ and $b' = u^{-6} b$. In this case $(x, y) \mapsto (u^{-2} x, u^{-3} y)$ is an isomorphism $E_{a, b} \to E_{a', b'}$ that fixes $O$.

Lean: Mathlib `WeierstrassCurve.variableChange_j` (invariance) and `WeierstrassCurve.exists_variableChange_of_j_eq` (the converse, over a separably closed field), both proved in Mathlib.

*Proof.* If $a' = u^{-4} a$ and $b' = u^{-6} b$, then $a'^3 = u^{-12} a^3$ and $b'^2 = u^{-12} b^2$, so $j$ does not change. Substitute $x = u^2 x'$ and $y = u^3 y'$ in $y^2 = x^3 + ax + b$ and divide by $u^6$: this gives $y'^2 = x'^3 + u^{-4} a x' + u^{-6} b$, so the map is an isomorphism. Conversely, suppose the $j$-invariants are equal. If $a = 0$, then $j = 0$, so $a' = 0$, and $b, b' \neq 0$ by smoothness; choose $u$ with $u^6 = b/b'$. If $b = 0$, then $j = 1728$, so $b' = 0$ and $a, a' \neq 0$; choose $u$ with $u^4 = a/a'$. Otherwise $a, b, a', b'$ are all nonzero, and equal $j$ gives $a^3 b'^2 = a'^3 b^2$. Put $v = \frac{a' b}{a b'}$. Then
$$
v^2 = \frac{a'^2 b^2}{a^2 b'^2} = \frac{a'^2 \cdot a^3 b'^2 / a'^3}{a^2 b'^2} = \frac{a}{a'}, \qquad v^3 = v \cdot v^2 = \frac{a' b}{a b'} \cdot \frac{a}{a'} = \frac{b}{b'} .
$$
Choose $u$ with $u^2 = v$. Then $u^4 = a/a'$ and $u^6 = b/b'$. $\square$

Silverman (Ch. III) shows that every isomorphism of smooth cubics that fixes $O$ has this form. So $j$ classifies smooth cubics with a marked flex up to isomorphism, and every $j_0 \in k$ occurs (Exercise 5).

### Proof in words

A flex with tangent line $Z = 0$ makes the equation $cX^3 + Z \cdot Q$. Smoothness at the flex gives a $Y^2 Z$ term. Completing the square in $Y$ and the cube in $X$ gives the Weierstrass form; this is where $\operatorname{char} k \neq 2, 3$ is needed. The chord and tangent construction gives the group law. Identity, inverse and commutativity follow at once from Bézout's theorem on lines, and associativity is the real theorem.

The scaling $(x, y) \mapsto (u^2 x, u^3 y)$ is the only freedom left in the Weierstrass form. It multiplies $a^3$ and $b^2$ by the same factor, so the ratio $a^3 : b^2$, which is $j$ in other coordinates, is the invariant.

### Examples

A point of order 6. Let $\operatorname{char} k = 0$ and $E : y^2 = x^3 + 1$. The point $P = (2, 3)$ is on $E$ since $9 = 8 + 1$. Doubling: $\lambda = \frac{3 \cdot 4 + 0}{2 \cdot 3} = 2$, so $x_3 = 4 - 2 - 2 = 0$ and $y_3 = -(2(0 - 2) + 3) = 1$. So $2P = (0, 1)$. Next, $2(0, 1)$ has $\lambda = 0$, so $x_3 = 0$ and $y_3 = -1$: $4P = (0, -1) = -2P$. Hence $6P = O$. Also $3P = P + 2P$ has $\lambda = \frac{1 - 3}{0 - 2} = 1$, $x_3 = 1 - 2 - 0 = -1$ and $y_3 = -(1 \cdot (-1 - 2) + 3) = 0$. So $3P = (-1, 0)$, which is its own inverse, and $P$ has order exactly 6.

A hypothesis that fails: the cusp. Let $C : y^2 = x^3$, with $a = b = 0$, so $\Delta = 0$ and $C$ is not smooth. The chord and tangent construction still works on the smooth points $(t^2, t^3)$, $t \neq 0$, and $O$. Three such points with parameters $t_1, t_2, t_3$ lie on a line $y = \lambda x + \nu$ if and only if they are the roots of $t^3 - \lambda t^2 - \nu = 0$. The coefficient of $t$ is 0, so $t_1 t_2 + t_2 t_3 + t_3 t_1 = 0$, that is, $u_1 + u_2 + u_3 = 0$ for $u = 1/t = x/y$. The point $O$ has $u = 0$. So $P + Q$ has $u = u_P + u_Q$, and the smooth locus is the additive group $(k, +)$. This group is not a projective curve, and $C$ has no $j$-invariant.

### Exercises

1. (A) Show that the points of order 2 on a smooth $E_{a, b}$ are the three points $(e_i, 0)$ with $p(e_i) = 0$. Find them for $y^2 = x^3 - x$.
2. (A) On $y^2 = x^3 - 2$ over $\mathbb{Q}$, compute $2P$ for $P = (3, 5)$.
3. (A) Show that $(x, y) \mapsto (-x, iy)$ with $i^2 = -1$ is an automorphism of $y^2 = x^3 - x$ that fixes $O$, and find an automorphism of order 3 of $y^2 = x^3 + 1$.
4. (B) Show that a point $P \neq O$ of $E$ is a flex if and only if $3P = O$. Show that the line through two flexes of $E$ meets $E$ in a third flex.
5. (B) Show that for every $j_0 \in k$ there is a smooth Weierstrass cubic with $j = j_0$. Treat $j_0 = 0$, $j_0 = 1728$ and the other values separately.
6. (B) Let $N$ be the nodal cubic $y^2 = x^2(x + 1)$ with the parametrization $t \mapsto (t^2 - 1, t(t^2 - 1))$ of Section 7.3. Put $s = \frac{t - 1}{t + 1}$. Show that three smooth points are collinear if and only if $s_1 s_2 s_3 = 1$, and deduce that the smooth locus of $N$ is the multiplicative group $(k^*, \cdot)$.

### Lean

Mathlib has `WeierstrassCurve`, the condition `WeierstrassCurve.IsElliptic`, the invariant `WeierstrassCurve.j`, and the group `WeierstrassCurve.Affine.Point` with its `AddCommGroup` instance. The points are the smooth points, so the instance also covers the groups $\mathbb{G}_a$ and $\mathbb{G}_m$ of the singular cubics. Mathlib works with the equation and does not prove that every smooth plane cubic has a Weierstrass form.

### Notes and history

The chord and tangent construction goes back to Newton and to Fermat's work on rational points; Poincaré described the group structure on rational points in 1901. Weierstrass found the normal form in his work on elliptic functions, where a smooth cubic over $\mathbb{C}$ is the torus $\mathbb{C}/\Lambda$. Silverman (Ch. III) is the standard reference for the group law and the $j$-invariant, and the literature state is "theorem". The genus formula $\frac{(d - 1)(d - 2)}{2}$ for a smooth plane curve of degree $d$ is in P5; it gives genus 1 for a smooth cubic.
