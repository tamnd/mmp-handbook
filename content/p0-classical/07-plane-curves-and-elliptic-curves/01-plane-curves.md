---
title: Plane curves and their singular points
nodes: []
sources: [Ful69, Rei88, Har77]
reads_with: [Ful69:ch3, Rei88:ch1, Har77:I.5]
requires: [P0.3, P0.4, P0.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Plane curves and their singular points

### Statement

**Definition P0.7.1.** An *affine plane curve* is a nonconstant polynomial $f \in k[x, y]$, up to multiplication by a nonzero constant. Its *degree* is the degree of $f$, and its set of points is $V(f) \subset \mathbb{A}^2$. A *projective plane curve* of degree $d \ge 1$ is a nonzero homogeneous polynomial $F \in k[X, Y, Z]$ of degree $d$, up to a nonzero constant, with the set of points $V(F) \subset \mathbb{P}^2$. The curve is *irreducible* when the polynomial is irreducible. If $f = \prod f_i^{e_i}$ with distinct irreducible factors $f_i$, the curves $f_i$ are the *components* of $f$ and $e_i$ is the multiplicity of $f_i$.

Lean: not in Lean; Mathlib has `MvPolynomial.zeroLocus` for the set $V(f)$.

**Example P0.7.2.** The line $y = ax + b$ is the curve $y - ax - b$ of degree 1. The conic $XZ - Y^2$ is an irreducible projective curve of degree 2. The curve $f = (y - x^2)^2$ has the same points as the parabola $y = x^2$, but it is a different curve: its only component is the parabola, with multiplicity 2.

**Definition P0.7.3.** Let $P = (0, 0)$ and write $f = f_m + f_{m+1} + \dots + f_d$ with $f_j$ homogeneous of degree $j$ and $f_m \neq 0$. The integer $m = m_P(f)$ is the *multiplicity* of $f$ at $P$. The form $f_m$ is the *tangent cone* of $f$ at $P$. For another point $P$, move $P$ to the origin by a translation. The point $P$ is *smooth* on $f$ if $m_P(f) = 1$ and *singular* if $m_P(f) \ge 2$. A point with $m_P(f) = 2$ is a *double point*.

Lean: not in Lean.

Over the algebraically closed field $k$, a homogeneous form in two variables is a product of linear forms. So $f_m = \prod L_i^{r_i}$ with distinct lines $L_i$ through $P$, and $\sum r_i = m$. The lines $L_i$ are the *tangent lines* of $f$ at $P$.

**Definition P0.7.4.** A double point $P$ of $f$ is a *node* if $f_2$ has two distinct tangent lines, and a *cusp* if $f_2 = L^2$ for one line $L$.

Lean: not in Lean.

**Example P0.7.5.** The nodal cubic $f = y^2 - x^2 - x^3$ has $f_2 = y^2 - x^2 = (y - x)(y + x)$ at the origin. If $\operatorname{char} k \neq 2$, the two tangent lines $y = x$ and $y = -x$ are distinct, and the origin is a node. The cuspidal cubic $f = y^2 - x^3$ has $f_2 = y^2$, so the origin is a cusp with the tangent line $y = 0$.

**Proposition P0.7.6 (Jacobian criterion for plane curves).** Let $P \in V(f)$. Then $P$ is singular on $f$ if and only if $\frac{\partial f}{\partial x}(P) = \frac{\partial f}{\partial y}(P) = 0$.

Lean: not in Lean; Mathlib has the partial derivative `MvPolynomial.pderiv`.

*Proof.* Move $P$ to the origin by a translation. A translation does not change the vanishing of the partial derivatives at $P$, by the chain rule. Write $f = f_1 + f_2 + \dots$ with $f_0 = f(P) = 0$. The linear part is $f_1 = \frac{\partial f}{\partial x}(0, 0)\, x + \frac{\partial f}{\partial y}(0, 0)\, y$, because every term of degree at least 2 has partial derivatives that vanish at the origin. So $m_P(f) \ge 2$ if and only if $f_1 = 0$, that is, if and only if both partial derivatives vanish at $P$. $\square$

**Lemma P0.7.7.** Let $f, g \in k[x, y]$ have no common factor. Then $V(f) \cap V(g)$ is finite.

Lean: not in Lean.

*Proof.* The ring $k(x)[y]$ is a principal ideal domain. By Gauss's lemma, $f$ and $g$ have no common factor in $k(x)[y]$, so $af + bg = 1$ for some $a, b \in k(x)[y]$. Multiply by a common denominator $d(x) \neq 0$ of $a$ and $b$. This gives $a' f + b' g = d(x)$ with $a', b' \in k[x, y]$. A common zero $(x_0, y_0)$ of $f$ and $g$ has $d(x_0) = 0$, so $x_0$ is one of the finitely many roots of $d$. The same argument with $x$ and $y$ exchanged gives finitely many values of $y_0$. $\square$

**Theorem P0.7.8 (finiteness of singular points).** Let $f \in k[x, y]$ be irreducible. Then $f$ has only finitely many singular points.

Lean: not in Lean.

*Proof.* Suppose first that $\frac{\partial f}{\partial x} \neq 0$. Its degree in $x$ is smaller than the degree of $f$ in $x$, so $f$ does not divide it. As $f$ is irreducible, $f$ and $\frac{\partial f}{\partial x}$ have no common factor. By the Lemma, $V(f, \frac{\partial f}{\partial x})$ is finite, and by the Proposition it contains every singular point. The case $\frac{\partial f}{\partial y} \neq 0$ is the same. Suppose now that both partial derivatives are 0. Then $f$ is a polynomial in $x^p$ and $y^p$, where $p = \operatorname{char} k > 0$. Each coefficient of $f$ has a $p$-th root in $k$, so $f = g^p$ for some $g \in k[x, y]$. This contradicts the irreducibility of $f$. $\square$

### Proof in words

A point is singular when the linear part of the Taylor expansion vanishes, and the linear part is the gradient. So the singular points are the common zeros of $f$ and its two partial derivatives. A partial derivative has smaller degree, so it cannot share a factor with an irreducible $f$, and two curves with no common factor meet in finitely many points. The only difficulty is characteristic $p$, where both partial derivatives can be 0; then $f$ is a $p$-th power and is not irreducible.

### Examples

The folium of Descartes $f = x^3 + y^3 - xy$, with $\operatorname{char} k = 0$. The partial derivatives are $f_x = 3x^2 - y$ and $f_y = 3y^2 - x$. A common zero has $y = 3x^2$ and $x = 3y^2 = 27x^4$, so $x = 0$ or $x^3 = \frac{1}{27}$. If $x = 0$, then $y = 0$, and $(0, 0)$ lies on the curve. If $x = \frac{\omega}{3}$ with $\omega^3 = 1$, then $y = \frac{\omega^2}{3}$ and $f(x, y) = \frac{1}{27} + \frac{1}{27} - \frac{\omega^3}{9} = -\frac{1}{27} \neq 0$, so the point is not on the curve. The only singular point in $\mathbb{A}^2$ is the origin. There $f_2 = -xy$, with the two tangent lines $x = 0$ and $y = 0$, so the origin is a node.

A curve that is not reduced. Let $f = (y - x^2)^2$. Then $\frac{\partial f}{\partial x} = -4x(y - x^2)$ and $\frac{\partial f}{\partial y} = 2(y - x^2)$. Both vanish on all of $V(f)$, so every point of the parabola is a singular point of $f$. The Theorem fails because $f$ is not irreducible. This is why a plane curve is a polynomial and not only a set of points.

### Exercises

1. (A) Show that every point of a line is smooth.
2. (A) Find the multiplicity and the tangent cone at the origin of $y^2 = x^5$, of $y^3 = x^4$ and of $x^4 + y^4 = x^2 y$.
3. (A) Show that the folium $X^3 + Y^3 - XYZ$ is smooth at its three points on the line $Z = 0$.
4. (B) Let $F$ be homogeneous of degree $d$ and let $\operatorname{char} k$ not divide $d$. Prove Euler's formula $X F_X + Y F_Y + Z F_Z = d F$, and deduce that a point of $\mathbb{P}^2$ where $F_X$, $F_Y$ and $F_Z$ vanish lies on $V(F)$.
5. (B) Show that a curve of degree $d$ with a point of multiplicity $d$ is a union of $d$ lines through that point, counted with multiplicity.
6. (B) Let $\operatorname{char} k = 2$. Show that every point of the conic $y = x^2$ is smooth, and that the tangent lines at all its points meet in one point of $\mathbb{P}^2$.

### Lean

Mathlib has polynomials in several variables, their zero sets (`MvPolynomial.zeroLocus`) and partial derivatives (`MvPolynomial.pderiv`). It has no notion of the multiplicity of a plane curve at a point. Not in Lean in `MinimalModel`; the handbook does not need it as a node.

### Notes and history

The tangent cone and the multiplicity are classical. Fulton treats a curve as a polynomial up to a constant, as here, so that a curve can have multiple components (Fulton, Ch. 3). The Jacobian criterion in all dimensions is Theorem I.5.1 of Hartshorne, and Chapter 6 of this volume proves it. The statements of this section are theorems in the literature. In characteristic $p$ a curve can have strange behaviour, as in Exercise 6: all tangent lines of a smooth conic in characteristic 2 pass through one point.
