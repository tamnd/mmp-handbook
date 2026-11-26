---
title: The 27 lines of the Fermat cubic
nodes: []
sources: [Rei88, Har77]
reads_with: [Rei88:ch7, Har77:V.4]
requires: [P0.4, P0.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The 27 lines of the Fermat cubic

### Statement

In this section $\operatorname{char} k \neq 3$, and $S \subset \mathbb{P}^3$ is the Fermat cubic
$$
x^3 + y^3 + z^3 + w^3 = 0 .
$$
Let $\mu = \{\alpha \in k : \alpha^3 = -1\}$. As $\operatorname{char} k \neq 3$, the polynomial $t^3 + 1$ has nonzero derivative at its roots, so $\mu$ has exactly 3 elements.

**Definition P0.8.8.** A *pairing* of the coordinates is a partition of $\{x, y, z, w\}$ into two pairs. There are three pairings: $xy|zw$, $xz|yw$ and $xw|yz$. For the pairing $xy|zw$ and $\alpha, \beta \in \mu$, put
$$
L_{\alpha, \beta} = \{x = \alpha y, \ z = \beta w\},
$$
and define the lines $L'_{\gamma, \delta} = \{x = \gamma z, \ y = \delta w\}$ and $L''_{\varepsilon, \theta} = \{x = \varepsilon w, \ y = \theta z\}$ for the other two pairings in the same way.

Lean: not in Lean.

**Example P0.8.9.** The line $L_{\alpha, \beta}$ lies on $S$: on it, $x^3 + y^3 = (\alpha^3 + 1) y^3 = 0$ and $z^3 + w^3 = (\beta^3 + 1) w^3 = 0$. It is spanned by the points $[\alpha : 1 : 0 : 0]$ and $[0 : 0 : \beta : 1]$.

**Example P0.8.10.** For $k = \mathbb{C}$, $\mu = \{-1, -\omega, -\omega^2\}$ with $\omega = e^{2\pi i/3}$. The nine lines of the pairing $xy|zw$ include $\{x = -y, \ z = -w\}$, which is defined over $\mathbb{Q}$.

**Theorem P0.8.11 (lines of the Fermat cubic).** The Fermat cubic contains exactly 27 lines: the 9 lines of each of the three pairings.

Lean: not in Lean.

*Proof.* The 27 lines are distinct. Two lines of the same pairing with different indices are different, and a line of one pairing is not a line of another: for example $[\alpha : 1 : 0 : 0] \in L_{\alpha, \beta}$ does not satisfy $x = \gamma z$, since $\alpha \neq 0$.

Let $L \subset S$ be a line. Let $A = \{z = w = 0\}$ and $B = \{x = y = 0\}$.

Case 1: $L \cap A = \emptyset$. Then the projection $[x : y : z : w] \mapsto [z : w]$ is defined on all of $L$, and it is a linear isomorphism $L \to \mathbb{P}^1$. So $L$ is the graph of a linear map: $L = \{x = az + bw, \ y = cz + dw\}$ for some $a, b, c, d \in k$. The condition $L \subset S$ is that
$$
(az + bw)^3 + (cz + dw)^3 + z^3 + w^3 = 0
$$
as a polynomial in $z$ and $w$. Its four coefficients give
$$
a^3 + c^3 = -1, \qquad 3(a^2 b + c^2 d) = 0, \qquad 3(a b^2 + c d^2) = 0, \qquad b^3 + d^3 = -1 .
$$
As $\operatorname{char} k \neq 3$, the middle equations are $a^2 b = -c^2 d$ and $a b^2 = -c d^2$. If $a = 0$, then $c^3 = -1$, so $c \neq 0$. Then $c^2 d = 0$ gives $d = 0$ and $b^3 = -1$, and $L = \{x = bw, \ y = cz\}$ is a line $L''$. If $b = 0$, then $d^3 = -1$, so $d \neq 0$. Then $c d^2 = 0$ gives $c = 0$ and $a^3 = -1$, and $L = \{x = az, \ y = dw\}$ is a line $L'$. If $a \neq 0$ and $b \neq 0$, then $a^2 b \neq 0$, so $c \neq 0$ and $d \neq 0$. Divide the two middle equations: $a/b = c/d$. Put $r = a/b$. Then $a^2 b = r^2 b^3$ and $c^2 d = r^2 d^3$, so $r^2 (b^3 + d^3) = 0$. As $r \neq 0$, this gives $b^3 + d^3 = 0$, which contradicts $b^3 + d^3 = -1$. So Case 1 gives exactly the 18 lines $L'$ and $L''$.

Case 2: $L \cap B = \emptyset$. Exchange $(x, y)$ with $(z, w)$. The argument of Case 1 shows that $L$ is again one of the 18 lines $L'$ and $L''$. So Case 2 gives no new line. (Each of these 18 lines is disjoint from both $A$ and $B$: on $L'_{\gamma, \delta}$, $z = w = 0$ gives $x = y = 0$.)

Case 3: $L$ meets both $A$ and $B$. The lines $A$ and $B$ are disjoint, so $L$ meets them in two different points $P = [p : q : 0 : 0]$ and $Q = [0 : 0 : r : s]$, and $L = PQ$. These points lie on $S$, so $p^3 + q^3 = 0$ and $r^3 + s^3 = 0$. Then $q \neq 0$ and $s \neq 0$, and $\alpha = p/q$ and $\beta = r/s$ lie in $\mu$. So $L = L_{\alpha, \beta}$.

Each line falls in at least one of the three cases. So the lines on $S$ are exactly the 27 lines of the statement. $\square$

**Proposition P0.8.12 (incidences on the Fermat cubic).** Each of the 27 lines meets exactly 10 of the others: 4 of its own pairing and 3 of each other pairing. Two lines $L_{\alpha, \beta}$ and $L_{\alpha', \beta'}$ meet if and only if exactly one of $\alpha = \alpha'$, $\beta = \beta'$ holds. The lines $L_{\alpha, \beta}$ and $L'_{\gamma, \delta}$ meet if and only if $\gamma \beta = \alpha \delta$.

Lean: not in Lean.

*Proof.* The lines $L_{\alpha, \beta}$ and $L_{\alpha', \beta'}$ meet if and only if the four linear equations $x = \alpha y$, $x = \alpha' y$, $z = \beta w$, $z = \beta' w$ have a nonzero common solution. If $\alpha \neq \alpha'$, they force $x = y = 0$, and if $\beta \neq \beta'$, they force $z = w = 0$. So the lines meet if and only if $\alpha = \alpha'$ or $\beta = \beta'$, and they are different if and only if not both hold. This gives $2 + 2 = 4$ lines of the same pairing. Next, a common point of $L_{\alpha, \beta}$ and $L'_{\gamma, \delta}$ satisfies $x = \alpha y = \alpha \delta w$ and $x = \gamma z = \gamma \beta w$. If $w = 0$, all coordinates are 0. So there is a common point if and only if $\gamma \beta = \alpha \delta$, and then it is $[\alpha \delta : \delta : \beta : 1]$. For fixed $\alpha$, $\beta$ and each $\delta \in \mu$, the value $\gamma = \alpha \delta / \beta$ satisfies $\gamma^3 = (-1)(-1)/(-1) = -1$, so $\gamma \in \mu$. This gives exactly 3 lines $L'$ that meet $L_{\alpha, \beta}$. The third pairing is the same after a change of names, and the symmetry of $S$ that permutes the coordinates permutes the pairings. $\square$

### Proof in words

A line in $\mathbb{P}^3$ either misses the line $A = \{z = w = 0\}$, and then it is a graph over the $(z, w)$ line, or it meets $A$. In the first case the condition to lie on $S$ is four polynomial equations in four unknowns, and they can be solved by hand. In the second case the same argument with $B$ in place of $A$ applies, unless the line meets both $A$ and $B$; then it joins a point of $S \cap A$ to a point of $S \cap B$, and each of these sets has three points.

The characteristic enters twice: the set $\mu$ has three elements, and the factor 3 in the middle equations can be cancelled. Both fail in characteristic 3.

### Examples

A plane with three lines through one point. The plane $x = \alpha y$ meets $S$ where $(\alpha^3 + 1) y^3 + z^3 + w^3 = 0$, that is, where $z^3 + w^3 = \prod_{\beta \in \mu} (z - \beta w) = 0$. So the plane section is the union of the three lines $L_{\alpha, \beta}$, $\beta \in \mu$, and all three pass through the point $[\alpha : 1 : 0 : 0]$. A point of a smooth cubic surface where three of its lines meet is an *Eckardt point*. The Fermat cubic has many of them, so three coplanar lines on a smooth cubic surface can meet in one point.

A hypothesis that fails: characteristic 3. If $\operatorname{char} k = 3$, then
$$
x^3 + y^3 + z^3 + w^3 = (x + y + z + w)^3,
$$
since the Frobenius map is additive. So $S$ is the plane $x + y + z + w = 0$ counted three times. Every point of it is singular, and it contains infinitely many lines. The Theorem fails because $S$ is not smooth.

### Exercises

1. (A) Show that the 27 lines of the Fermat cubic over $\mathbb{C}$ are defined over $\mathbb{Q}(\omega)$, and find the lines that are defined over $\mathbb{Q}$.
2. (A) Show that the permutations of the coordinates and the maps $(x, y, z, w) \mapsto (\zeta_1 x, \zeta_2 y, \zeta_3 z, w)$ with $\zeta_i^3 = 1$ act on the 27 lines, and that this group acts transitively on them.
3. (A) Show that the plane $x + y + z + w = 0$ meets $S$ in three lines of $S$, and find them.
4. (B) Count the Eckardt points of the Fermat cubic. (Each plane $x = \alpha y$ gives one; find all of them, and show that there are 18.)
5. (B) Let $p \equiv 1 \pmod 3$ be a prime. Show that all 27 lines of the Fermat cubic over $\overline{\mathbb{F}}_p$ are defined over $\mathbb{F}_p$. What happens for $p \equiv 2 \pmod 3$?

### Lean

Not in Lean. The proof is a finite computation with cube roots of $-1$. A formal version would check the coefficient equations of Case 1 with the Mathlib tactic `linear_combination`.

### Notes and history

The 27 lines of the Fermat cubic are a standard example (Reid, Ch. 7). The literature state is "theorem". The Fermat cubic has the largest group of symmetries of all smooth cubic surfaces in characteristic 0, and its Eckardt points are named after F. E. Eckardt, who studied them in 1876. Section 8.1 uses this Theorem to prove that every cubic surface contains a line.
