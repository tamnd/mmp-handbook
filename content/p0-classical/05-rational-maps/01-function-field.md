---
title: Rational functions and the function field
nodes: []
sources: [Rei88, Har77, Sha13]
reads_with: [Rei88:ch4, Har77:I.3, Sha13:ch1]
requires: [P0.3, P0.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Rational functions and the function field

### Statement

**Definition P0.5.1.** Let $X$ be an affine variety with coordinate ring $k[X]$. The coordinate ring is a domain, because $I(X)$ is prime. The *function field* $k(X)$ is the field of fractions of $k[X]$. An element of $k(X)$ is a *rational function* on $X$. Let $X \subset \mathbb{P}^n$ be a projective variety with homogeneous ideal $I(X)$. Then $k(X)$ is the set of quotients $g/h$ of homogeneous polynomials of the same degree with $h \notin I(X)$, where $g/h = g'/h'$ when $gh' - g'h \in I(X)$.

Lean: Mathlib `AlgebraicGeometry.Scheme.functionField` (the function field of an integral scheme).

**Example P0.5.2.** The function field of $\mathbb{A}^n$ is $k(x_1, \dots, x_n)$. The function field of $\mathbb{P}^n$ is the set of quotients of forms of the same degree in $x_0, \dots, x_n$. The map $g/h \mapsto g(1, x_1, \dots, x_n)/h(1, x_1, \dots, x_n)$ is an isomorphism onto $k(x_1, \dots, x_n)$, with inverse given by the substitution $x_i \mapsto x_i/x_0$.

**Example P0.5.3.** Let $C = V(y^2 - x^3) \subset \mathbb{A}^2$ be the cuspidal cubic. The map $k[x, y] \to k[t]$, $x \mapsto t^2$, $y \mapsto t^3$, has kernel $(y^2 - x^3)$ and image $k[t^2, t^3]$. So $k[C] \cong k[t^2, t^3]$, and $k(C) = k(t)$ with $t = y/x$.

**Definition P0.5.4.** Let $X$ be a variety and $P \in X$. A rational function $f$ is *regular at* $P$ if $f = g/h$ with $h(P) \neq 0$, where $g, h \in k[X]$ for $X$ affine, and $g, h$ are forms of the same degree for $X$ projective. The *local ring* $\mathcal{O}_{X,P}$ is the subring of $k(X)$ of the functions regular at $P$. The *domain of definition* $\operatorname{dom}(f)$ is the set of points where $f$ is regular.

Lean: not in Lean in this form. Mathlib has the stalks of the structure sheaf of a scheme, which play the role of $\mathcal{O}_{X,P}$.

The set $\operatorname{dom}(f)$ is open: if $f = g/h$ with $h(P) \neq 0$, then $f$ is regular on the open set $\{h \neq 0\}$. It is not empty, because every $f$ has some expression $g/h$ with $h \neq 0$ in $k[X]$.

**Theorem P0.5.5 (regular functions on an affine variety).** Let $X$ be an affine variety. A rational function that is regular at every point of $X$ lies in $k[X]$.

Lean: not in Lean.

*Proof.* Let $f \in k(X)$ be regular at every point. Let $D_f = \{h \in k[X] : hf \in k[X]\}$. This is an ideal of $k[X]$. For each $P \in X$ there is an expression $f = g/h$ with $h(P) \neq 0$. Then $h \in D_f$ and $h(P) \neq 0$, so $P \notin V(D_f)$. So $V(D_f)$ is empty. Let $J \subset k[x_1, \dots, x_n]$ be the inverse image of $D_f$. Then $V(J) = V(D_f) = \emptyset$, and the Nullstellensatz of Chapter 3 gives $1 \in J$. So $1 \in D_f$, that is, $f = 1 \cdot f \in k[X]$. $\square$

### Proof in words

A function that is regular everywhere has, near each point, a denominator that does not vanish there. These denominators generate an ideal with no common zero. The Nullstellensatz then says that the ideal contains 1, and 1 is a denominator: so the function is a polynomial function. The whole difficulty is in the Nullstellensatz. Over a field that is not algebraically closed the argument fails, as Exercise 4 shows.

### Examples

**Example P0.5.6.** On the cuspidal cubic $C$, take $t = y/x \in k(C)$. At a point $(a^2, a^3)$ with $a \neq 0$ the function $t$ is regular, because $x(a^2, a^3) = a^2 \neq 0$. The function $t$ is not regular at the origin. Suppose that $t = g/h$ with $g, h \in k[t^2, t^3]$ and $h(0) \neq 0$. Then $h$ has a constant term $c \neq 0$ and no term in $t$. So $th = g$ has the coefficient $c$ at $t$. But no element of $k[t^2, t^3]$ has a term in $t$. This is a contradiction. So $\operatorname{dom}(t) = C \setminus \{0\}$, while $t^2 = x$ and $t^3 = y$ are regular everywhere. The function $t$ is integral over $k[C]$ and is not in $k[C]$, so $k[C]$ is not integrally closed.

**Example P0.5.7.** On the projective line the theorem fails: $\mathbb{P}^1$ is not affine. A rational function on $\mathbb{P}^1$ is $g(x_0, x_1)/h(x_0, x_1)$ with $g, h$ forms of degree $d$ and no common factor. If $h$ has a linear factor $\ell$, then $f$ is not regular at the zero of $\ell$, because $g$ does not vanish there. So a function regular everywhere has $h$ constant, and then $d = 0$ and $f$ is a constant. The global regular functions are only the constants, and they do not form a ring of coordinates for $\mathbb{P}^1$.

### Exercises

1. (A) Show that $k(V(xy - 1)) \cong k(x)$. Find $\operatorname{dom}(y)$ and $\operatorname{dom}(1/x)$.
2. (A) Let $X = V(y^2 - x^2 - x^3) \subset \mathbb{A}^2$ be the nodal cubic. Show that $t = y/x$ generates $k(X)$ over $k$, and write $x$ and $y$ as rational functions of $t$.
3. (B) Show that $\mathcal{O}_{X,P}$ is the localization of $k[X]$ at the maximal ideal $\mathfrak{m}_P$ of the functions that vanish at $P$, for $X$ affine.
4. (B) Over $\mathbb{R}$, show that $1/(1 + x^2)$ is regular at every real point of $\mathbb{A}^1$ and is not a polynomial. Say which step of the proof of the theorem fails.
5. (B) Let $X$ be the quadric cone $V(xy - z^2) \subset \mathbb{A}^3$. Show that $x/z = z/y$ in $k(X)$, and that $\operatorname{dom}(x/z)$ is $X \setminus V(y, z)$, which is the complement of a line on the cone.

### Lean

Mathlib defines the function field of an integral scheme as `AlgebraicGeometry.Scheme.functionField`. The handbook uses varieties in the classical sense of Chapters 3 and 4. A variety is the integral scheme of finite type over $k$ that it defines (P3), and $k(X)$ is then the same field. The theorem of this section is the statement that $\Gamma(X, \mathcal{O}_X) = k[X]$ for an affine variety. It is not stated in this form in Lean.

### Notes and history

The theorem is classical, and its literature state is theorem. Hartshorne proves it as part of Theorem I.3.2, and Reid proves it in Chapter 4. Example 2 of the Examples part is the first sign of the cusp as a singular point: the coordinate ring is not integrally closed. Chapter 7 studies the cusp as a plane curve, P8 resolves it, and Volume 4 computes its log canonical threshold $\frac{5}{6}$.
