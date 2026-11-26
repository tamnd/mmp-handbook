---
title: The cuspidal and the nodal cubic
nodes: []
sources: [Rei88, Ful69, Har77]
reads_with: [Rei88:ch2, Ful69:ch5, Har77:I.5]
requires: [P0.4, P0.5, P0.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The cuspidal and the nodal cubic

### Statement

**Definition P0.7.18.** An irreducible curve $C$ is *rational* if there is a birational map $\mathbb{P}^1 \dashrightarrow C$, that is, if $k(C) \cong k(t)$ as extensions of $k$.

Lean: not in Lean.

**Example P0.7.19.** A line is rational. A smooth conic is rational: projection from a point $P$ of the conic sends a point $Q \neq P$ to the line $PQ$, and each line through $P$ meets the conic in one more point, by Bézout's theorem (Section 7.2).

**Example P0.7.20.** The cuspidal cubic $C = \{y^2 = x^3\}$ and the nodal cubic $N = \{y^2 = x^2(x + 1)\}$ are rational. The Proposition below gives the maps.

**Proposition P0.7.21 (the cuspidal cubic).** The map $\varphi : \mathbb{A}^1 \to C$, $t \mapsto (t^2, t^3)$, is a bijective morphism. It is not an isomorphism. Its inverse is the rational map $C \dashrightarrow \mathbb{A}^1$, $(x, y) \mapsto y/x$.

Lean: not in Lean; Mathlib has `WeierstrassCurve`, and $y^2 = x^3$ is a Weierstrass curve with discriminant 0.

*Proof.* The point $(t^2, t^3)$ satisfies $y^2 = t^6 = x^3$, so $\varphi$ is a morphism to $C$. Let $(x, y) \in C$. If $x = 0$, then $y = 0$, and $t = 0$ is the only $t$ with $t^2 = 0$. If $x \neq 0$, a preimage $t$ must satisfy $t = t^3/t^2 = y/x$. Conversely $t = y/x$ gives $t^2 = y^2/x^2 = x$ and $t^3 = t \cdot t^2 = (y/x)\, x = y$. So $\varphi$ is bijective, and $y/x$ is the inverse on $C \setminus \{0\}$. The coordinate ring $k[C] = k[x, y]/(y^2 - x^3)$ has every element in the form $a(x) + b(x)\, y$. Its image under $\varphi^*$ is $a(t^2) + b(t^2)\, t^3$, which has even part $a(t^2)$ and odd part $b(t^2)t^3$. So $\varphi^*$ is injective with image $k[t^2, t^3]$. This image does not contain $t$, so $\varphi^*$ is not an isomorphism, and $\varphi$ is not an isomorphism. $\square$

The projective closure of $C$ is $Y^2 Z = X^3$, with the parametrization $[s : t] \mapsto [s t^2 : t^3 : s^3]$. The point $s = 0$ maps to $O = [0 : 1 : 0]$. In the chart $Y = 1$ the curve is $z = x^3$, which is smooth at $O$ with tangent line $z = 0$, and $I(O, C \cap \{Z = 0\}) = 3$. So $O$ is a smooth flex of $C$, and the origin is the only singular point.

**Theorem P0.7.22 (singular cubics are rational).** Let $F$ be an irreducible plane cubic with a singular point $P$. Then $F$ is rational. Projection from $P$ is a birational map $F \dashrightarrow \mathbb{P}^1$.

Lean: not in Lean.

*Proof.* Choose coordinates with $P$ at the origin of the chart $Z \neq 0$, and write the affine equation as $f = f_2 + f_3$ with $f_j$ homogeneous of degree $j$. The constant and linear terms are 0 because $P$ is singular, and $f_2 \neq 0$: if $f = f_3$, then $f$ is a union of three lines through $P$ (Exercise 5 of Section 7.1), which is not irreducible. Also $f_3 \neq 0$, since $f$ has degree 3. Substitute the line $y = tx$:
$$
f(x, tx) = x^2 \bigl( f_2(1, t) + x f_3(1, t) \bigr).
$$
The polynomials $f_2(1, t)$ and $f_3(1, t)$ are not 0, because $f_j(x, y) = x^j f_j(1, y/x)$. So the line $y = tx$ meets $F$ at the origin and at one more point,
$$
\psi(t) = \left( -\frac{f_2(1, t)}{f_3(1, t)}, \ -\frac{t f_2(1, t)}{f_3(1, t)} \right),
$$
for all $t$ with $f_3(1, t) \neq 0$. This defines a rational map $\psi : \mathbb{A}^1 \dashrightarrow F$. Its image is not one point, because $y/x = t$ on the image. As $F$ is an irreducible curve, $\psi$ is dominant. The rational map $\pi : F \dashrightarrow \mathbb{A}^1$, $(x, y) \mapsto y/x$, satisfies $\pi \circ \psi = \mathrm{id}$. For a point $(x_0, y_0) \neq (0, 0)$ of $F$ with $x_0 \neq 0$, put $t_0 = y_0/x_0$. If $f_3(1, t_0) \neq 0$, the line $y = t_0 x$ meets $F$ at the origin and at $(x_0, y_0)$, so $\psi(t_0) = (x_0, y_0)$. Hence $\psi \circ \pi = \mathrm{id}$ on a dense open subset of $F$. So $\psi$ is birational. $\square$

### Proof in words

A line through a double point $P$ of a cubic meets the cubic twice at $P$. Bézout's theorem leaves room for exactly one more point. That point depends rationally on the slope of the line, because it is the root of a linear equation in $x$. So the slope is a coordinate on the cubic, and the cubic is rational.

The argument fails for a smooth cubic: a line through a smooth point meets the cubic in two more points, and the root of a quadratic equation is not a rational function of the slope.

### Examples

The two parametrizations by the Theorem. For the cusp, $f_2 = y^2$ and $f_3 = -x^3$, so $f(x, tx) = x^2 (t^2 - x)$ and $\psi(t) = (t^2, t^3)$. This is the map of the Proposition. For the node, $f_2 = y^2 - x^2$ and $f_3 = -x^3$, so $f(x, tx) = x^2 (t^2 - 1 - x)$ and
$$
\psi(t) = (t^2 - 1, \ t(t^2 - 1)).
$$
Here $\psi$ is a morphism $\mathbb{A}^1 \to N$. The two values $t = 1$ and $t = -1$ map to the origin, and these are the slopes of the two tangent lines $y = \pm x$ at the node. Every other point of $N$ has one preimage $t = y/x$. So $\psi$ is surjective but not injective. The node separates into two points, and the cusp does not.

A hypothesis that fails: no singular point. Let $E$ be the smooth cubic $y^2 = x^3 - x$, with $\operatorname{char} k \neq 2$, and project from the smooth point $P = (0, 0)$. The line $y = tx$ meets $E$ where $t^2 x^2 = x^3 - x$, that is, at $x = 0$ and at the two roots of $x^2 - t^2 x - 1 = 0$. So projection from $P$ is a map of degree 2 to $\mathbb{P}^1$, and the Theorem gives nothing. In fact $E$ is not rational: P5 shows that a smooth plane cubic has genus 1, and a rational smooth curve has genus 0.

### Exercises

1. (A) Show that the origin is the only singular point of $y^2 = x^2(x + 1)$ in $\mathbb{P}^2$, for $\operatorname{char} k \neq 2$.
2. (A) Show that the line $y = 0$ is the only line through the origin that meets $y^2 = x^3$ with multiplicity 3 at the origin. Show that both lines $y = \pm x$ meet $y^2 = x^2(x + 1)$ with multiplicity 3 at the origin.
3. (A) Show that $t = y/x$ is integral over $k[x, y]/(y^2 - x^3)$, and that $k[t]$ is the integral closure of $k[t^2, t^3]$ in $k(t)$.
4. (B) Let $F$ be an irreducible plane curve of degree $d$ with a point of multiplicity $d - 1$. Prove that $F$ is rational. Find a parametrization of $y^3 = x^4$.
5. (B) Let $\operatorname{char} k = 0$. Show that an irreducible cubic with a cusp is projectively equivalent to $Y^2 Z = X^3$, and an irreducible cubic with a node is projectively equivalent to $Y^2 Z = X^2 (X + Z)$.

### Lean

Not in Lean. Mathlib has `WeierstrassCurve` with discriminant `WeierstrassCurve.Δ`, which is 0 for the cusp and the node, but no rational parametrization of a singular cubic. A formal version would state the Theorem as an isomorphism of function fields.

### Notes and history

Newton classified real plane cubics in 1704, and the singular ones appear in that classification. The parametrization by lines through a double point is classical (Reid, Ch. 2). The literature state is "theorem". The cuspidal cubic is a running example of the handbook. P8 Ch. 4 resolves its singularity by blow-ups, and Volume 4 computes its log canonical threshold $\frac56$. Section 7.4 shows that the smooth points of the cusp form the additive group $\mathbb{G}_a$.
