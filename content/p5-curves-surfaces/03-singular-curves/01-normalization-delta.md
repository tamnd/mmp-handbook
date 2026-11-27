---
title: Normalization and the delta-invariant
nodes: []
sources: [Har77, Ser88, Liu02]
reads_with: [Har77:IV.1, Liu02:7.5]
requires: [P1.3, P1.4, P1.7, P1.9, P3.7, P4.1, P4.3, P4.7, P5.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Normalization and the delta-invariant

### Statement

In this chapter $k$ is algebraically closed, and a *curve* is an integral projective scheme $C$ of dimension $1$ over $k$, possibly singular. By Theorem P3.7.36 and Theorem P1.4.32, $C$ has a normalization $\nu \colon \widetilde{C} \to C$ which is finite and birational, and $\widetilde{C}$ is a normal curve, so a smooth projective curve by Theorem P1.7.12 and Theorem P5.1.3. For a closed point $P \in C$ write $\mathcal{O}_P = \mathcal{O}_{C,P}$ and $\widetilde{\mathcal{O}}_P = (\nu_* \mathcal{O}_{\widetilde{C}})_P$, the integral closure of $\mathcal{O}_P$ in $K = K(C)$. The points of $\widetilde{C}$ over $P$ are the *branches* of $C$ at $P$.

**Definition P5.3.1 (the $\delta$-invariant).** The *$\delta$-invariant* of $C$ at $P$ is $\delta_P = \dim_k \widetilde{\mathcal{O}}_P / \mathcal{O}_P$. The *geometric genus* of $C$ is $g(\widetilde{C})$.

**Proposition P5.3.2 (the genus formula).** $\delta_P$ is finite, it is zero if and only if $P$ is a smooth point of $C$, and
$$p_a(C) = g(\widetilde{C}) + \sum_{P \in C} \delta_P.$$

Lean: not in Lean as stated.

**Corollary P5.3.3.**

1. $p_a(C) \geq g(\widetilde{C}) \geq 0$, and $p_a(C) = 0$ if and only if $C \cong \mathbb{P}^1$.
2. A curve with $p_a(C) = 1$ is a smooth curve of genus $1$ or a rational curve with exactly one singular point $P$, with $\delta_P = 1$.
3. An integral plane curve $C$ of degree $d$ satisfies $g(\widetilde{C}) + \sum_P \delta_P = (d-1)(d-2)/2$.

Lean: not in Lean as stated.

For a plane curve $C = V(f) \subseteq \mathbb{A}^2$ and a point $P$, the *multiplicity* $m_P$ is the order of $f$ at $P$: the least $m$ with $f \in \mathfrak{m}_P^m \setminus \mathfrak{m}_P^{m+1}$ in $k[x, y]$, where $\mathfrak{m}_P$ is the maximal ideal of $P$. The lowest form $f_m$ of $f$ at $P$ is the *tangent cone*, a product of $m$ linear forms, the *tangent lines*.

**Proposition P5.3.4 (the multiplicity bound).** Let $P$ be a point of multiplicity $m$ on an integral plane curve $C$, with branches $Q_1, \dots, Q_s$. Then
$$m = \sum_{i=1}^s \min\bigl(v_{Q_i}(x), v_{Q_i}(y)\bigr), \qquad \delta_P \geq \frac{m(m-1)}{2},$$
for local coordinates $x, y$ vanishing at $P$. In particular $s \leq m$.

Lean: not in Lean as stated.

**Corollary P5.3.5.** An integral plane curve of degree $d$ with singular points of multiplicities $m_1, \dots, m_r$ satisfies
$$g(\widetilde{C}) \leq \frac{(d-1)(d-2)}{2} - \sum_{j=1}^r \frac{m_j(m_j-1)}{2}.$$
In particular it has at most $(d-1)(d-2)/2$ singular points, and a point of multiplicity $d - 1$ forces $C$ to be rational.

Lean: not in Lean as stated.

### Proof in words

The quotient $\nu_* \mathcal{O}_{\widetilde{C}} / \mathcal{O}_C$ is a coherent sheaf supported on the finitely many singular points, so it has finite length, the sum of the $\delta_P$. Since $\nu$ is finite, the cohomology of $\nu_* \mathcal{O}_{\widetilde{C}}$ on $C$ is that of $\mathcal{O}_{\widetilde{C}}$ on $\widetilde{C}$. Taking Euler characteristics in the exact sequence $0 \to \mathcal{O}_C \to \nu_* \mathcal{O}_{\widetilde{C}} \to \mathcal{Q} \to 0$ gives the genus formula. For the multiplicity bound, the local ring of a plane curve at a point of multiplicity $m$ has $\dim \mathcal{O}_P / \mathfrak{m}^n = mn - m(m-1)/2$ for $n \geq m$, while its normalization, a semilocal principal ideal domain, has $\dim \widetilde{\mathcal{O}}_P / \mathfrak{m}^n \widetilde{\mathcal{O}}_P = mn$. The difference is at most $\delta_P$.

### Examples

**Example P5.3.6 (the node).** Let $C$ be the projective closure of $y^2 = x^2(x + 1)$ in characteristic $\neq 2$, the nodal cubic, with $P$ the origin. With $t = y/x$, $t^2 = x + 1$, so $x = t^2 - 1$ and $y = t(t^2 - 1)$, and $\widetilde{C} = \mathbb{P}^1$ with coordinate $t$. The two branches at $P$ are $t = \pm 1$, and $\widetilde{\mathcal{O}}_P = \mathcal{O}_P[t]$, generated over $\mathcal{O}_P$ by $1$ and $t$, with $\widetilde{\mathcal{O}}_P / \mathcal{O}_P \cong k$ spanned by $t$ (Example P1.7.18). So $\delta_P = 1$, $m_P = 2$, and $p_a(C) = 0 + 1 = 1$, as for every plane cubic.

**Example P5.3.7 (the cusp and the singularities $y^a = x^b$).** Let $a, b \geq 2$ be coprime and $C$ the closure of $y^a = x^b$, with $P$ the origin. The map $t \mapsto (t^a, t^b)$ is the normalization near $P$, with one branch, and $\mathcal{O}_P$ is the localization of $k[t^a, t^b]$. So $\widetilde{\mathcal{O}}_P / \mathcal{O}_P$ has basis the powers $t^j$ for $j$ in the set of *gaps* of the semigroup $\langle a, b \rangle = \{ ia + jb : i, j \geq 0 \}$, and $\delta_P$ is the number of gaps, $(a-1)(b-1)/2$ by Sylvester's count (Exercise 2). For the cusp $y^2 = x^3$ the only gap is $1$, so $\delta_P = 1$ (Example P1.7.17). For $y^3 = x^4$, $\delta_P = 3 = m(m-1)/2$ with $m = 3$. For $y^2 = x^5$, $\delta_P = 2 > m(m-1)/2 = 1$: the bound of Proposition P5.3.4 is not sharp when the singularity is not ordinary.

**Example P5.3.8 (rational plane quartics).** A plane quartic has $p_a = 3$, so by Corollary P5.3.3 an integral quartic with three singular points of $\delta = 1$ is rational. An example is the image of a general conic under the quadratic transformation $[x : y : z] \mapsto [yz : xz : xy]$, a quartic with nodes at the three coordinate points. The quartic $z x^3 = y^4$ has one singular point, $[0 : 0 : 1]$, where it is the singularity $x^3 = y^4$ of Example P5.3.7, with $m = 3$ and $\delta = 3$; at $[1 : 0 : 0]$ the affine equation is $z = y^4$, which is smooth. So it is rational, as Corollary P5.3.5 also predicts from $m = d - 1$. A *tacnode*, locally $y^2 = x^4 + (\text{higher terms})$, has $m = 2$ and $\delta = 2$ (Exercise 1), and a quartic with a tacnode and a node is rational.

**Example P5.3.9 (three coordinate axes).** Let $C \subseteq \mathbb{A}^3$ be the union of the three coordinate axes. It is not integral, but the computation of $\delta$ is local. The ring $\mathcal{O} = k[x,y,z]/(xy, yz, zx)$ has normalization $k[x] \times k[y] \times k[z]$, and $\mathcal{O}$ is the subring of triples of polynomials with equal constant terms, so $\delta = 2$ while the multiplicity is $3$. This does not contradict Proposition P5.3.4, which is about plane curves: three lines through a point in the plane have $\delta = 3$ (Exercise 3). By Proposition P5.3.2, an integral projective curve with normalization $\mathbb{P}^1$ whose only singular point is locally of this form has arithmetic genus $2$.

### Proof

*Proposition P5.3.2.* The set of singular points of $C$ is finite (Theorem P0.7.8), and at a smooth point $\mathcal{O}_P$ is a DVR, so integrally closed and $\delta_P = 0$. At a singular point, $\mathcal{O}_P$ is a Noetherian local domain of dimension $1$ that is not regular, so it is not normal by Theorem P1.7.12, and $\delta_P > 0$. Let $\mathcal{Q} = \nu_* \mathcal{O}_{\widetilde{C}} / \mathcal{O}_C$. It is coherent, since $\nu$ is finite, and its stalk at $P$ is $\widetilde{\mathcal{O}}_P / \mathcal{O}_P$, which vanishes away from the singular points. A coherent sheaf with finite support is a finite direct sum of its stalks, each a finitely generated module of finite length over a local ring with residue field $k$, so $\delta_P = \ell(\mathcal{Q}_P) < \infty$ by Corollary P1.3.29, and $h^0(\mathcal{Q}) = \sum_P \delta_P$, $h^1(\mathcal{Q}) = 0$.

Since $\nu$ is finite, hence affine, and $C$ is separated, $H^i(C, \nu_* \mathcal{O}_{\widetilde{C}}) \cong H^i(\widetilde{C}, \mathcal{O}_{\widetilde{C}})$ by Proposition P4.1.19, so $\chi(\nu_* \mathcal{O}_{\widetilde{C}}) = 1 - g(\widetilde{C})$. Additivity of $\chi$ on $0 \to \mathcal{O}_C \to \nu_* \mathcal{O}_{\widetilde{C}} \to \mathcal{Q} \to 0$ gives
$$1 - g(\widetilde{C}) = \chi(\mathcal{O}_C) + \sum_P \delta_P = 1 - p_a(C) + \sum_P \delta_P,$$
using $p_a(C) = 1 - \chi(\mathcal{O}_C)$ from Definition P4.3.9.

*Corollary P5.3.3.* Part 1: $p_a(C) = 0$ forces $g(\widetilde{C}) = 0$ and all $\delta_P = 0$, so $C$ is smooth, and $C \cong \mathbb{P}^1$ by Proposition P5.1.12. Part 2 is the same count with total $1$. Part 3 is Proposition P5.3.2 together with $p_a(C) = (d-1)(d-2)/2$ from Example P4.7.23.

*Proposition P5.3.4.* Choose coordinates with $P = (0, 0)$, so $\mathcal{O}_P = A/(f)$ for $A = k[x, y]_{(x, y)}$ with maximal ideal $\mathfrak{n} = (x, y)$, and $f \in \mathfrak{n}^m \setminus \mathfrak{n}^{m+1}$. Write $\mathfrak{m} = \mathfrak{n} \mathcal{O}_P$.

*Step 1: $\dim_k \mathcal{O}_P / \mathfrak{m}^n = mn - m(m-1)/2$ for $n \geq m$.* We have $\mathcal{O}_P / \mathfrak{m}^n = A / (\mathfrak{n}^n + fA)$. If $g \in A$ and $fg \in \mathfrak{n}^n$, then $g \in \mathfrak{n}^{n-m}$: the associated graded ring of $A$ is the polynomial ring $k[X, Y]$ (Theorem P1.9.2), a domain, so the order of $fg$ is the sum of the orders of $f$ and $g$. So $(fA + \mathfrak{n}^n)/\mathfrak{n}^n \cong A/\mathfrak{n}^{n-m}$ by $g \mapsto fg$, and
$$\dim_k \mathcal{O}_P / \mathfrak{m}^n = \binom{n+1}{2} - \binom{n-m+1}{2} = mn - \frac{m(m-1)}{2}.$$

*Step 2: $\widetilde{\mathcal{O}}_P$ is a principal ideal domain.* It is a Dedekind domain with finitely many maximal ideals $\mathfrak{q}_1, \dots, \mathfrak{q}_s$, one for each branch. By the Chinese remainder theorem choose $\pi_i \in \mathfrak{q}_i \setminus \mathfrak{q}_i^2$ with $\pi_i \notin \mathfrak{q}_j$ for $j \neq i$. Then $\pi_i$ generates $\mathfrak{q}_i$ locally at every maximal ideal, so $\mathfrak{q}_i = (\pi_i)$, and by Theorem P1.7.22 every nonzero ideal is principal. So $\mathfrak{m} \widetilde{\mathcal{O}}_P = \prod_i \mathfrak{q}_i^{m_i}$ with $m_i = \min(v_{Q_i}(x), v_{Q_i}(y))$, and $\dim_k \widetilde{\mathcal{O}}_P / \mathfrak{m}^n \widetilde{\mathcal{O}}_P = n \sum_i m_i$, since each $\widetilde{\mathcal{O}}_P / \mathfrak{q}_i^{n m_i}$ has dimension $n m_i$ by Proposition P1.7.14.

*Step 3: $\sum_i m_i = m$.* Choose a linear form $\ell = \alpha x + \beta y$ that is not a tangent line at $P$ and such that $v_{Q_i}(\ell) = m_i$ for every $i$. This excludes finitely many ratios $[\alpha : \beta]$: on the branch $Q_i$, $v(\alpha x + \beta y) > m_i$ for at most one ratio. Let $\mathcal{Q}_P = \widetilde{\mathcal{O}}_P / \mathcal{O}_P$. Multiplication by $\ell$ is injective on the domains $\mathcal{O}_P$ and $\widetilde{\mathcal{O}}_P$, so the snake lemma applied to it on $0 \to \mathcal{O}_P \to \widetilde{\mathcal{O}}_P \to \mathcal{Q}_P \to 0$ gives an exact sequence
$$0 \to \ker(\ell \mid \mathcal{Q}_P) \to \mathcal{O}_P / \ell \mathcal{O}_P \to \widetilde{\mathcal{O}}_P / \ell \widetilde{\mathcal{O}}_P \to \mathcal{Q}_P / \ell \mathcal{Q}_P \to 0.$$
Multiplication by $\ell$ on the finite-dimensional space $\mathcal{Q}_P$ has kernel and cokernel of the same dimension, so $\dim \mathcal{O}_P / \ell \mathcal{O}_P = \dim \widetilde{\mathcal{O}}_P / \ell \widetilde{\mathcal{O}}_P$. The left term is $\sum_i v_{Q_i}(\ell) = \sum_i m_i$. For the right term, $\mathcal{O}_P / \ell \mathcal{O}_P = A / (\ell, f)$ is the local ring at $P$ of the line $\ell = 0$ cut by $f$. Parametrizing the line by $u$, the restriction of $f$ has order exactly $m$ in $u$, since the restriction of $f_m$ is nonzero because $\ell$ is not a tangent line, and the local ring of the line at $P$ is a DVR, so this dimension is $m$.

*Step 4.* The module $\mathcal{Q}_P$ has finite length, so $\mathfrak{m}^N \mathcal{Q}_P = 0$ for some $N$, that is, $\mathfrak{m}^N \widetilde{\mathcal{O}}_P \subseteq \mathcal{O}_P$. For $n \geq \max(N, m)$, additivity of length on $\mathfrak{m}^n \widetilde{\mathcal{O}}_P \subseteq \mathcal{O}_P \subseteq \widetilde{\mathcal{O}}_P$ and the inclusion $\mathfrak{m}^n \subseteq \mathfrak{m}^n \widetilde{\mathcal{O}}_P$ give
$$\delta_P = \dim \widetilde{\mathcal{O}}_P / \mathfrak{m}^n \widetilde{\mathcal{O}}_P - \dim \mathcal{O}_P / \mathfrak{m}^n \widetilde{\mathcal{O}}_P \geq mn - \dim \mathcal{O}_P / \mathfrak{m}^n = mn - \Bigl(mn - \frac{m(m-1)}{2}\Bigr) = \frac{m(m-1)}{2}.$$
The bound $s \leq m$ follows from $m_i \geq 1$.

*Corollary P5.3.5.* Combine Corollary P5.3.3, part 3, with Proposition P5.3.4, using $m_j(m_j - 1)/2 \geq 1$ at a singular point. If $m_P = d - 1$, the bound gives $g(\widetilde{C}) \leq (d-1)(d-2)/2 - (d-1)(d-2)/2 = 0$.

### Exercises

1. (A) Compute $\delta_P$, $m_P$ and the branches of $y^2 = x^4 + x^5$ and of $x^3 = y^2 x + y^4$ at the origin.
2. (A) Let $a, b \geq 2$ be coprime. Show that every integer $n \geq (a-1)(b-1)$ lies in $\langle a, b \rangle$, that $(a-1)(b-1) - 1$ does not, and that exactly half of $0, 1, \dots, (a-1)(b-1) - 1$ lie in $\langle a, b \rangle$, using the involution $n \mapsto (a-1)(b-1) - 1 - n$.
3. (B) Show that an ordinary $m$-fold point of a plane curve, one with $m$ distinct tangent lines, has $\delta_P = m(m-1)/2$, by showing that $\mathfrak{m}^{m-1} \widetilde{\mathcal{O}}_P \subseteq \mathcal{O}_P$.
4. (B) Show that the curve $t \mapsto [1 : t^3 : t^4 : t^5]$ in $\mathbb{P}^3$ has one singular point with $\delta = 2$, find its arithmetic genus, and show that it is not contained in any plane.
5. (B) Let $C$ be an integral curve and $f \colon \mathbb{P}^1 \to C$ a nonconstant morphism. Show that $f$ factors through the normalization and that $\widetilde{C} \cong \mathbb{P}^1$.
6. (C) Show that a curve $C \subseteq \mathbb{P}^3$ of degree $d$ not contained in a plane satisfies $p_a(C) \leq \lfloor (d-2)^2/4 \rfloor$, Castelnuovo's bound, in the case where $C$ lies on a smooth quadric, using the divisors of bidegree $(a, b)$ of Chapter 9.

### Lean

Mathlib has the integral closure of a ring and the length of a module, but not the normalization of a projective curve, its $\delta$-invariant or the genus formula. The handbook adds no `MinimalModel` node here.

### Notes and history

The genus formula for plane curves with ordinary singularities is due to Plücker and Clebsch, and for arbitrary singularities to Noether, through his resolution by quadratic transformations, the subject of Chapter 6. The $\delta$-invariant in its algebraic form is due to Rosenlicht and Serre. The literature state is theorem. In the minimal model program the arithmetic genus of a rational curve bounds how singular it can be, and the curves with $p_a = 1$ and one node or cusp are the singular fibres of the elliptic fibrations of Chapter 11.
