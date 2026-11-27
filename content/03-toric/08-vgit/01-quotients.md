---
title: Quotients of affine space by the multiplicative group
nodes: []
sources: [CLS11]
reads_with: [CLS11:ch14]
requires: [3.1, 3.2, P1.4, P3.6]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Quotients of affine space by the multiplicative group

### Statement

Throughout the chapter $k$ is an algebraically closed field, $r \ge 1$, $R = k[x_1, \dots, x_r]$, and $q = (q_1, \dots, q_r) \in \mathbb{Z}^r$ is a nonzero vector of *weights*. The multiplicative group acts on $\mathbb{A}^r$ by
$$t \cdot x = (t^{q_1} x_1, \dots, t^{q_r} x_r), \qquad t \in k^*.$$
A monomial $x^m$, $m \in \mathbb{N}^r$, satisfies $x^m(t \cdot x) = t^{\langle q, m \rangle} x^m(x)$, where $\langle q, m \rangle = \sum_i q_i m_i$ is its *weight*. This chapter works with the grading by weight rather than with the group action, so that nothing depends on the characteristic of $k$. Put
$$J_+ = \{ i : q_i > 0 \}, \qquad J_0 = \{ i : q_i = 0 \}, \qquad J_- = \{ i : q_i < 0 \}.$$

**Definition 3.8.1 (semi-invariants and the three quotients).** For $\chi \in \mathbb{Z}$, let $R_\chi \subseteq R$ be the span of the monomials of weight $\chi$, the *semi-invariants of weight $\chi$*, so that $R = \bigoplus_{\chi \in \mathbb{Z}} R_\chi$ is a graded ring. The elements of $R_0$ are the *invariants*.

1. The *affine quotient* is $X_0 = \operatorname{Spec} R_0$.
2. The *quotients with character $\pm 1$* are
$$X_+ = \operatorname{Proj} \bigoplus_{k \ge 0} R_k, \qquad X_- = \operatorname{Proj} \bigoplus_{k \ge 0} R_{-k},$$
where $R_{\pm k}$ sits in degree $k$. Their degree $0$ parts are $R_0$, which gives morphisms $\pi_\pm \colon X_\pm \to X_0$. More generally, for $\chi \in \mathbb{Z}$ the *GIT quotient* is $X_\chi = \operatorname{Proj} \bigoplus_{k \ge 0} R_{k\chi}$.
3. A point $x \in \mathbb{A}^r(k)$ is *semistable for $\pm$* if $f(x) \neq 0$ for some $f \in R_{\pm k}$ with $k > 0$, and *unstable* otherwise. Write $\mathbb{A}^r_\pm$ for the set of semistable points.

Lean: not yet in Lean.

**Proposition 3.8.2 (the charts of the quotient).**

1. $R_0$ and $\bigoplus_{k \ge 0} R_{\pm k}$ are finitely generated $k$-algebras.
2. $\mathbb{A}^r_+ = \{ x : x_j \neq 0 \text{ for some } j \in J_+ \}$, the complement of the linear subspace $V(x_j : j \in J_+)$.
3. $X_+$ is covered by the open sets $D_+(x_j)$, $j \in J_+$, and $D_+(x_j) = \operatorname{Spec} A_j$, where $A_j = (R_{x_j})_0$ is the span of the Laurent monomials $x^m$ with $\langle q, m \rangle = 0$, $m_i \ge 0$ for $i \neq j$, and $m_j \in \mathbb{Z}$. In particular $X_+ = \emptyset$ if and only if $J_+ = \emptyset$.
4. For $\chi > 0$, $X_\chi \cong X_+$, and for $\chi < 0$, $X_\chi \cong X_-$. For $\chi = 0$, $X_\chi = X_0$.
5. The same statements hold for $X_-$ with $J_+$ replaced by $J_-$.

Lean: not yet in Lean.

For $j \in J_+$ the inclusion $A_j \subseteq R_{x_j}$ gives a morphism $\{x_j \neq 0\} = \operatorname{Spec} R_{x_j} \to D_+(x_j)$. On $\{x_j x_{j'} \neq 0\}$ these morphisms agree, since both come from the inclusion of the invariants of $R_{x_j x_{j'}}$. So they glue to a morphism $\phi_+ \colon \mathbb{A}^r_+ \to X_+$, the *quotient map*, and $\pi_+ \phi_+$ is the restriction of the map $\mathbb{A}^r \to X_0$ given by $R_0 \subseteq R$.

**Theorem 3.8.3 (points of the quotient are orbits).** Assume $J_+ \neq \emptyset$.

1. The map $\phi_+ \colon \mathbb{A}^r_+(k) \to X_+(k)$ is surjective.
2. For $x, y \in \mathbb{A}^r_+(k)$, $\phi_+(x) = \phi_+(y)$ if and only if $y = t \cdot x$ for some $t \in k^*$.

So the $k$-points of $X_+$ are the orbits of $k^*$ on the semistable points. The same holds for $X_-$.

Lean: not yet in Lean.

### Proof in words

A semi-invariant of positive weight is a sum of monomials of positive weight, and each of these contains a variable of positive weight. So the semistable points are the points with a nonzero coordinate of positive weight, and on the open set where $x_j \neq 0$ the quotient is the spectrum of the invariant Laurent polynomials. Setting $x_j = 1$ identifies these invariants with the polynomials in the other variables whose weight is divisible by $q_j$; the polynomial ring is finite over this ring, so every point of the chart comes from a point of the slice $x_j = 1$. Two points of the slice with the same invariants differ by a root of unity, acting through the weights, and this is the statement that their orbits agree.

### Examples

**Example 3.8.4 (projective space).** Let $q = (1, \dots, 1)$. Then $R_k$ is the space of forms of degree $k$, $X_+ = \operatorname{Proj} R = \mathbb{P}^{r-1}$, $X_0 = \operatorname{Spec} k$ and $X_- = \emptyset$, since $J_- = \emptyset$. The semistable points are $\mathbb{A}^r \setminus \{0\}$, and the orbits are the lines through the origin with the origin removed, the points of $\mathbb{P}^{r-1}$. The chart $D_+(x_j)$ is $\operatorname{Spec} k[x_i/x_j : i \neq j]$, the standard chart. The weights $(-1, \dots, -1)$ give the same quotient as $X_-$.

**Example 3.8.5 (the weighted projective plane).** Let $q = (1, 1, 2)$ with variables $x, y, z$. Then $X_+ = \operatorname{Proj} k[x, y, z]$ with degrees $1, 1, 2$, the weighted projective plane $\mathbb{P}(1, 1, 2)$, which is the quadric cone in $\mathbb{P}^3$ by Example P3.6.7. Its charts are
$$A_x = k[y/x, z/x^2], \qquad A_y = k[x/y, z/y^2], \qquad A_z = k[x^2/z, xy/z, y^2/z] \cong k[u, v, w]/(uw - v^2).$$
The first two are planes, and the third is the cone $\frac12(1,1)$ of Example 3.2.15. On the slice $z = 1$, the points $(x, y, 1)$ and $(-x, -y, 1)$ lie in the same orbit, as $t = -1$ has $t^2 = 1$: this is the group of order $2$ that makes the singular point.

**Example 3.8.6 (the hyperbola).** Let $q = (1, -1)$, with variables $x, y$. Then $R_0 = k[xy]$ and $X_0 = \mathbb{A}^1$. The orbits in $\mathbb{A}^2$ are the hyperbolas $xy = c$ for $c \neq 0$, the two punctured axes $\{y = 0, x \neq 0\}$ and $\{x = 0, y \neq 0\}$, and the origin. The map $\mathbb{A}^2 \to X_0$, $(x, y) \mapsto xy$, sends the three orbits in $xy = 0$ to the same point: the invariants cannot separate orbits whose closures meet, and both punctured axes contain the origin in their closures. The semistable points for $+$ are $\{x \neq 0\}$, and $X_+ = \operatorname{Spec} A_x = \operatorname{Spec} k[xy] = X_0$. So $\pi_+$ is an isomorphism, and the point $0$ of $X_+$ is the orbit $\{y = 0, x \neq 0\}$. For $-$ the semistable points are $\{y \neq 0\}$, and the point $0$ of $X_-$ is the other punctured axis. The three quotients are all $\mathbb{A}^1$, but the orbits they record over $0$ differ.

### Proof

*Proof of Proposition 3.8.2.* Part 1. The algebra $\bigoplus_{k \ge 0} R_k$ is the semigroup algebra of $S = \{ m \in \mathbb{N}^r : \langle q, m \rangle \ge 0 \}$, the lattice points of the rational polyhedral cone $\{ m \in \mathbb{R}^r_{\ge 0} : \langle q, m \rangle \ge 0 \}$. By Gordan's lemma (Theorem 3.1.10, applied to the dual cone with Theorem 3.1.3) $S$ is a finitely generated semigroup, and the monomials of a set of generators generate the algebra. The same argument applies to $R_0$, with the cone $\langle q, m \rangle = 0$, and to the negative weights.

Part 2. If $x_j \neq 0$ with $j \in J_+$, then $x_j \in R_{q_j}$ with $q_j > 0$ does not vanish at $x$. Conversely, let $f \in R_k$, $k > 0$, with $f(x) \neq 0$. Then some monomial $x^m$ of $f$ has $x^m(x) \neq 0$ and weight $k > 0$, so some $j$ with $m_j > 0$ has $q_j > 0$, and $x_j \neq 0$.

Part 3. Write $R^+ = \bigoplus_{k \ge 0} R_k$. By Theorem P3.6.3, $D_+(f) = \operatorname{Spec} R^+_{(f)}$ for homogeneous $f$ of positive degree, and these sets cover $X_+$. A homogeneous element of positive degree is a sum of monomials of positive weight, so $D_+(f)$ lies in the union of the $D_+(x^m)$ for the monomials of $f$, and it suffices to show $D_+(x^m) \subseteq D_+(x_j)$ for a monomial of weight $w > 0$ and some $j \in J_+$. Choose $j$ with $m_j > 0$ and $q_j > 0$. The element $g = x_j^w / (x^m)^{q_j}$ lies in $R^+_{(x^m)}$, and so does $x^{q_j m - w e_j} = 1/g$, because the exponent $q_j m - w e_j$ has weight $0$ and is negative at most in the coordinate $j$, where $m_j > 0$; a Laurent monomial $x^n$ of weight $0$ with $n_i \ge 0$ outside the support of $m$ is $x^{n + l m}/(x^m)^l$ with $n + lm \in \mathbb{N}^r$ for large $l$. So $g$ is a unit on $D_+(x^m)$, and by Theorem P3.6.3, $D_+(x^m) \cap D_+(x_j) = D_+(x^m)_g = D_+(x^m)$. The ring $R^+_{(x_j)}$ is spanned by the quotients $x^{m'} / x_j^l$ with $m' \in \mathbb{N}^r$ of weight $l q_j$, which are the Laurent monomials of weight $0$ that are negative at most in the coordinate $j$. This is $A_j$. If $J_+ = \emptyset$, then $R_k = 0$ for $k > 0$ and $\operatorname{Proj} R^+ = \emptyset$; if $j \in J_+$, then $A_j \neq 0$ and $D_+(x_j) \neq \emptyset$.

Part 4. For $\chi > 0$, $\bigoplus_k R_{k \chi}$ is the Veronese ring $(R^+)^{(\chi)}$, and part 5 of Proposition P3.6.4 gives $X_\chi \cong X_+$. For $\chi < 0$ apply this to $-\chi$ and the negative weights. For $\chi = 0$ the ring is $R_0[s]$ with $\deg s = 1$, the polynomial ring over $R_0$ in the variable $s = 1 \in R_0$ placed in degree $1$, and its Proj is $\operatorname{Spec} R_0$ by Example P3.6.6. Part 5 is the same proof for the weights $-q$. $\square$

*Proof of Theorem 3.8.3.* Fix $j \in J_+$ and let $\rho_j \colon R_{x_j} \to R' = k[x_i : i \neq j]$ be the substitution $x_j \mapsto 1$. A Laurent monomial $x^m$ of weight $0$ is determined by its coordinates $m_i$, $i \neq j$, since $q_j m_j = -\sum_{i \neq j} q_i m_i$. So $\rho_j$ is injective on $A_j$, and its image $B_j$ is spanned by the monomials $x^{m'}$, $m' \in \mathbb{N}^{r-1}$, with $q_j \mid \sum_{i \ne j} q_i m'_i$. It contains $x_i^{q_j}$ for every $i \neq j$, so $R'$ is integral over $B_j$. By lying over (Theorem P1.4.12) and Corollary P1.4.10, every maximal ideal of $B_j$ is the intersection of a maximal ideal of $R'$ with $B_j$. So every $k$-point of $D_+(x_j) = \operatorname{Spec} B_j$ is the image of a point of the slice $\{x_j = 1\} = \operatorname{Spec} R'$. The slice lies in $\mathbb{A}^r_+$, and the composite of $\{x_j = 1\} \subseteq \{x_j \neq 0\}$ with $\phi_+$ is the map given by $\rho_j|_{A_j}$. As the $D_+(x_j)$ cover $X_+$, part 1 follows.

Part 2. If $y = t \cdot x$, every invariant Laurent monomial takes the same value at $x$ and $y$, so $\phi_+(x) = \phi_+(y)$. Conversely let $\phi_+(x) = \phi_+(y) \in D_+(x_j)$, so that $x_j \neq 0$ and $y_j \neq 0$. As $k$ is algebraically closed, there are $s, s'$ with $s^{q_j} = x_j^{-1}$ and $s'^{q_j} = y_j^{-1}$, so after replacing $x, y$ by $s \cdot x, s' \cdot y$ one may assume $x_j = y_j = 1$. Then $x^m = y^m$ for all $x^m \in A_j$. For $i \neq j$, the monomial $x_i^{q_j} x_j^{-q_i}$ lies in $A_j$, so $x_i^{q_j} = y_i^{q_j}$, and $x_i = 0$ if and only if $y_i = 0$. Let $I = \{ i : x_i \neq 0 \}$, which contains $j$, and let $L = \{ m \in \mathbb{Z}^I : \sum_{i \in I} q_i m_i = 0 \}$. Let $\psi \colon \mathbb{Z}^I \to k^*$ be the homomorphism $m \mapsto \prod_{i \in I} (y_i/x_i)^{m_i}$. If $m \in L$ has $m_i \ge 0$ for $i \neq j$, then $x^m \in A_j$ takes the same nonzero value at $x$ and $y$, so $\psi(m) = 1$. Every $m \in L$ is a difference of two such vectors: add $N \sum_{i \in I \setminus \{j\}} (q_j e_i - q_i e_j)$ for large $N$, a vector of $L$ of the same kind when $j \in J_+$. So $\psi$ is trivial on $L$. Let $g = \gcd(q_i : i \in I)$. The map $m \mapsto \frac1g \sum_{i \in I} q_i m_i$ identifies $\mathbb{Z}^I / L$ with $\mathbb{Z}$, so $\psi(m) = c^{\langle q, m \rangle / g}$ for $c = \psi(m_0)$, where $m_0$ is any vector with $\langle q, m_0 \rangle = g$. Choose $t$ with $t^g = c$. Then $y_i / x_i = \psi(e_i) = t^{q_i}$ for $i \in I$, and $y_i = 0 = t^{q_i} x_i$ for $i \notin I$. So $y = t \cdot x$. $\square$

### Exercises

1. (A) Let $q = (2, 3)$. Compute the charts $A_1$ and $A_2$ and show that $X_+ \cong \mathbb{P}^1$, while the slice $x_2 = 1$ meets each orbit in up to three points.
2. (A) Show that the quotients $X_\pm$ for the weights $-q$ are the quotients $X_\mp$ for $q$.
3. (A) Let $q_r = 0$. Show that $X_\pm(q) \cong X_\pm(q_1, \dots, q_{r-1}) \times \mathbb{A}^1$.
4. (B) Show that $x \in \mathbb{A}^r(k)$ is unstable for $+$ if and only if the map $k^* \to \mathbb{A}^r$, $t \mapsto t \cdot x$, extends to a morphism $\mathbb{P}^1 \setminus \{0\} \to \mathbb{A}^r$, that is, the limit of $t \cdot x$ as $t \to \infty$ exists. This is the Hilbert-Mumford criterion for $\mathbb{G}_m$.
5. (B) Let $J_0 = \emptyset$. Show that the orbit of $x$ is closed in $\mathbb{A}^r$ if and only if $x = 0$ or both $x_{J_+}$ and $x_{J_-}$ are nonzero, and that two points have the same image in $X_0$ if and only if the closures of their orbits meet.
6. (C) Let $\operatorname{char} k = 0$ and $j \in J_+$. Show that $B_j$ is the ring of invariants of the group $\mu_{q_j}$ of roots of unity of order $q_j$, acting on $k[x_i : i \neq j]$ by $\zeta \cdot x_i = \zeta^{q_i} x_i$. So the chart $D_+(x_j)$ is the quotient singularity $\frac{1}{q_j}(q_i : i \ne j)$, and it is smooth if $q_j = 1$.

### Lean

- Status: not yet in Lean. Mathlib has graded rings and the homogeneous localization `HomogeneousLocalization.Away` used for the charts of Proj, and `AlgebraicGeometry.Proj` of a graded ring, but no actions of $\mathbb{G}_m$ on affine space and no GIT quotients.
- Fidelity: Definition 3.8.1 uses only the $\mathbb{Z}$-grading of $R$ by weight, which Mathlib can express as a `GradedAlgebra`, so a Lean statement of Proposition 3.8.2 would not need group actions.
- No node of the map covers this section.

### Notes and history

Mumford's *Geometric invariant theory* (1965) constructs quotients by reductive groups through the invariants of a linearized action, and the quotient by $\mathbb{G}_m$ with a character is its simplest case. The description of the semistable points by the signs of the weights is the Hilbert-Mumford criterion of Exercise 4, which for $\mathbb{G}_m$ is elementary. Cox-Little-Schenck, Chapter 14, treat these quotients for an arbitrary torus as part of the quotient construction of toric varieties. The proofs here use only the grading, so that they hold in every characteristic; in characteristic dividing $q_j$ the group of Exercise 6 is not reduced, and the slice description of Theorem 3.8.3 is the statement that survives.
