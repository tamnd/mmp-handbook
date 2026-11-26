---
title: Multiplicity and the tangent cone of a hypersurface
nodes: []
sources: [Har92, Ful69, Sha13, Har77]
reads_with: [Har92:lecture20, Ful69:ch3, Sha13:ch2, Har77:I.5]
requires: [P0.3, P0.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Multiplicity and the tangent cone of a hypersurface

### Statement

Let $X = V(f) \subset \mathbb{A}^n$ be a hypersurface with $f$ nonconstant and irreducible, so that $I(X) = (f)$. Let $P \in X$, and choose coordinates with $P = 0$ by a translation. Write $f = f_m + f_{m+1} + \dots + f_d$ with $f_j$ homogeneous of degree $j$ and $f_m \neq 0$. Then $m \geq 1$, because $f(0) = 0$.

**Definition P0.6.31.** The *multiplicity* of $X$ at $P$ is $\operatorname{mult}_P X = m$, the degree of the lowest form of $f$ at $P$. The *tangent cone* of $X$ at $P$ is $C_P X = V(f_m) \subset \mathbb{A}^n$, a union of lines through $P$. A point of multiplicity $2$ is a *double point*, and a point of multiplicity $3$ a *triple point*.

Lean: not in Lean.

Let $M$ be the maximal ideal of $P$ in $k[x_1, \dots, x_n]$. Then $\operatorname{mult}_P X$ is the largest $m$ with $f \in M^m$, because $M^m$ is the set of polynomials whose terms at $P$ all have degree at least $m$. So the multiplicity does not depend on the choice of affine coordinates.

**Example P0.6.32.** The nodal cubic $y^2 = x^2 + x^3$ has $f = (y^2 - x^2) - x^3$, so $\operatorname{mult}_0 = 2$ and the tangent cone is $V(y^2 - x^2) = \{y = x\} \cup \{y = -x\}$ when $\operatorname{char} k \neq 2$. A double point whose tangent cone is two distinct lines is a *node*.

**Example P0.6.33.** The cusp $y^2 = x^3$ has $\operatorname{mult}_0 = 2$ and tangent cone $V(y^2)$, the line $y = 0$ counted twice. The tacnode $y^2 = x^4$ has the same multiplicity and the same tangent cone. So the multiplicity and the tangent cone do not distinguish the cusp from the tacnode.

**Definition P0.6.34.** Let $\ell = \{\tau v : \tau \in k\}$ be a line through $P = 0$ with direction $v \in k^n \setminus \{0\}$, and suppose that $\ell \not\subset X$. The *intersection multiplicity* of $\ell$ and $X$ at $P$ is the order of vanishing at $\tau = 0$ of the polynomial $g(\tau) = f(\tau v)$.

Lean: not in Lean; Mathlib has `Polynomial.rootMultiplicity` for the order of vanishing of a polynomial in one variable.

**Example P0.6.35.** For the line $\ell = \{(\tau, \tau)\}$ and the node, $g(\tau) = \tau^2 - \tau^2 - \tau^3 = -\tau^3$, of order $3$. The line $y = x$ is in the tangent cone.

**Example P0.6.36.** For the line $\ell = \{(\tau, 0)\}$ and the circle $V(x^2 + y^2 - 2y)$ through $0$, with $\operatorname{char} k \neq 2$, $g(\tau) = \tau^2$, of order $2$. The tangent line of the circle at $0$ is $y = 0$, and the multiplicity of the circle at $0$ is $1$.

**Theorem P0.6.37 (multiplicity and tangent cone).** Let $X = V(f)$ and $P = 0 \in X$ be as above, with $m = \operatorname{mult}_P X$.

1. $P$ is a nonsingular point of $X$ if and only if $m = 1$. In that case $C_P X = V(f_1)$ is the tangent space $T_P X$, embedded in $k^n$ as in Exercise 3 of Section 6.2.
2. Let $\ell$ be a line through $P$ with direction $v$, not contained in $X$. Its intersection multiplicity with $X$ at $P$ is at least $m$, and it equals $m$ if and only if $\ell \not\subset C_P X$, that is, $f_m(v) \neq 0$.
3. If $n = 2$, then $f_m$ is a product of $m$ linear forms, and $C_P X$ is the union of at least $1$ and at most $m$ lines through $P$, one for each factor. So $m$ is the number of tangent lines at $P$, counted with the multiplicities of the factors of $f_m$.

Lean: not in Lean.

*Proof.* Part 1. The partial derivative $\partial f/\partial x_i$ at $0$ is the coefficient of $x_i$ in $f$, which is the coefficient of $x_i$ in $f_1$ (and $0$ if $m \geq 2$). So the Jacobian matrix of the generator $f$ of $I(X)$ at $0$ is the coefficient vector of $f_1$. By the Jacobian criterion (Section 6.2) and $\dim X = n - 1$ (Section 6.1), $P$ is nonsingular if and only if this vector is not zero, that is, if and only if $f_1 \neq 0$, that is, $m = 1$. In that case the subspace of Exercise 3 of Section 6.2 is $\{v : \sum_i (\partial f/\partial x_i)(0) v_i = 0\} = V(f_1)$.

Part 2. Each $f_j$ is homogeneous of degree $j$, so $f_j(\tau v) = \tau^j f_j(v)$, and

$$ g(\tau) = f(\tau v) = \tau^m f_m(v) + \tau^{m+1} f_{m+1}(v) + \dots + \tau^d f_d(v). $$

The polynomial $g$ is not zero, because $\ell \not\subset X$. So its order at $0$ is at least $m$, and it equals $m$ exactly when $f_m(v) \neq 0$. The line $\ell$ lies in the cone $V(f_m)$ if and only if $f_m(\tau v) = \tau^m f_m(v) = 0$ for all $\tau$, that is, $f_m(v) = 0$.

Part 3. A nonzero binary form of degree $m$ over the algebraically closed field $k$ is a product of $m$ linear forms (Section 5.3), so $V(f_m)$ is the union of the corresponding lines through $0$. $\square$

### Proof in words

Everything comes from the expansion of $f$ into homogeneous parts at $P$. The linear part $f_1$ is the differential of $f$ at $P$, so the point is nonsingular exactly when $f_1 \neq 0$. Along a line through $P$ each homogeneous part $f_j$ contributes a term $\tau^j f_j(v)$, so the lowest possible order is $m$, and the lowest term survives exactly when the line is not in the cone $f_m = 0$. The only hypothesis to watch is $I(X) = (f)$: the multiplicity is defined by an equation, so the equation must be the generator of the ideal.

### Examples

**Example P0.6.38.** For the cusp $C = V(y^2 - x^3)$, compute the intersection multiplicity of each line through $0$. For $v = (1, \lambda)$, $g(\tau) = \lambda^2 \tau^2 - \tau^3$. If $\lambda \neq 0$, the order is $2 = m$, and indeed $f_2(v) = \lambda^2 \neq 0$. If $\lambda = 0$, the line is $y = 0$, $g(\tau) = -\tau^3$, the order is $3$, and $f_2(1, 0) = 0$: the line is the tangent cone. For $v = (0, 1)$, $g(\tau) = \tau^2$, of order $2$. So every line through the cusp meets it with multiplicity $2$, except the tangent line, which meets it with multiplicity $3$.

**Example P0.6.39.** The hypothesis $I(X) = (f)$ cannot be dropped. The polynomial $f = y^2$ defines the $x$-axis as a set, and its lowest form has degree $2$ at every point of the axis. But the axis is nonsingular, and its generator $y$ has multiplicity $1$ at every point. Part 1 fails for $f = y^2$, which is not irreducible.

### Exercises

1. (A) Find the multiplicity and the tangent cone at $0$ of the curves $y^3 = x^5$, $x^3 + y^3 = xy$, and $(x^2 + y^2)^2 = x^2 - y^2$ (with $\operatorname{char} k \neq 2$).
2. (A) Show that the quadric cone $Q = V(uw - v^2)$ of Section 6.3 has multiplicity $2$ at $0$ and that its tangent cone at $0$ is $Q$ itself.
3. (A) Show that $\operatorname{mult}_P X \leq \deg f$, and that equality at some point $P$ implies that $X$ is a cone with vertex $P$. Deduce that a plane curve of degree $d \geq 2$ with a point of multiplicity $d$ is not irreducible.
4. (B) Let $C$ be the cusp, and let $\widetilde{C} \subset \operatorname{Bl}_0 \mathbb{A}^2$ be its strict transform (Section 5.3). Show that the point of $\widetilde{C}$ over $0$ has multiplicity $1$, and that the curves $\widetilde{C}$ and $E$ meet there with intersection multiplicity $2$ in the sense of $\dim_k \mathcal{O}_{\operatorname{Bl}, Q}/(\widetilde{f}, x)$.
5. (B) Let $\operatorname{char} k = p > 0$ and $f = y^p - x^{p+1}$. Show that $\operatorname{mult}_0 V(f) = p$, that the tangent cone is the line $y = 0$, and that every other line through $0$ meets $V(f)$ with multiplicity $p$.

### Lean

Not in Lean. Mathlib has the homogeneous components of a multivariate polynomial, `MvPolynomial.homogeneousComponent`, and `Polynomial.rootMultiplicity` for the order of a polynomial in one variable, but no multiplicity or tangent cone of a variety.

### Notes and history

The study of multiple points of plane curves goes back to Newton and Cramer in the eighteenth century, and to Plücker in the nineteenth. Fulton's book treats them in Chapter 3, and Harris treats tangent cones and their degrees in his lectures on singular points. For a general variety the tangent cone is $\operatorname{Spec}$ of the graded ring $\bigoplus_j \mathfrak{m}^j/\mathfrak{m}^{j+1}$, and the multiplicity is its degree (the Hilbert-Samuel multiplicity, P1 Ch. 13 and P4 Ch. 3). The literature state is theorem. The cusp returns in P0 Ch. 7, P8 Ch. 4 resolves it by three blow-ups to a normal crossing divisor, and Volume 4 computes its log canonical threshold $\frac56$. Volume 4 also shows that a point of multiplicity $m$ on a hypersurface in $\mathbb{A}^n$ has log canonical threshold between $\frac1m$ and $\frac nm$, so the multiplicity is a first bound on how singular the point is.
