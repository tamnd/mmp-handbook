---
title: Discrepancies of surface singularities
nodes: []
sources: [KM98, Rei87, Kol13]
reads_with: [KM98:4.1, Rei87:all]
requires: [P5.5, P5.8, P8.7, P8.8, P8.9, P8.10, P8.11, P8.12]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Discrepancies of surface singularities

### Statement

In this section $X$ is a normal surface, $x \in X$ a singular point at which $K_X$ is $\mathbb{Q}$-Cartier, and $f \colon Y \to X$ the minimal resolution near $x$, with exceptional curves $E_1, \dots, E_r$, as in Section 10.1. Write $a_i = a(E_i, X)$, so that $K_Y = f^* K_X + \sum_i a_i E_i$ near $f^{-1}(x)$. As in Section 10.1, intersection numbers of curves over $x$ are computed on a compactification, and they do not depend on it.

**Proposition P8.13.12 (discrepancies on the minimal resolution).** The discrepancies $a_1, \dots, a_r$ are the unique solution of the linear system
$$\sum_{j = 1}^{r} a_j \, (E_j \cdot E_i) = K_Y \cdot E_i = 2 p_a(E_i) - 2 - E_i^2, \qquad i = 1, \dots, r,$$
and every $a_i \leq 0$. In particular a singular point of a normal surface is never terminal, and a normal surface is terminal if and only if it is smooth.

Lean: not in Lean as stated.

**Theorem P8.13.13 (Du Val is canonical).** A singular point $x$ of a normal surface is canonical if and only if it is a Du Val singularity. In that case $K_X$ is Cartier near $x$, every $a_i = 0$, and every exceptional divisor $F$ over $X$ with centre $x$ that is not one of the $E_i$ has $a(F, X) \geq 1$.

Lean: not in Lean as stated.

**Proposition P8.13.14 (discrepancies of toric surface singularities).** Let $\sigma = \operatorname{Cone}(u_1, u_2) \subseteq N_\mathbb{R} = \mathbb{R}^2$ be a strongly convex two-dimensional cone with primitive ray generators $u_1, u_2$, and $X = U_\sigma$. Let $m_\sigma \in M_\mathbb{Q}$ be the unique element with $\langle m_\sigma, u_1 \rangle = \langle m_\sigma, u_2 \rangle = 1$. Then $K_X$ is $\mathbb{Q}$-Cartier, and for every refinement $\Sigma'$ of $\sigma$ and every ray of $\Sigma'$ with primitive generator $v$,
$$a(D_v, X) = \langle m_\sigma, v \rangle - 1.$$
Every primitive $v \in N$ in the interior of $\sigma$ is a ray of the refinement obtained by subdividing $\sigma$ at $v$, so it gives a divisor over $X$ with this discrepancy.

Lean: not in Lean as stated.

**Corollary P8.13.15 (cyclic quotient surface singularities are klt).** Let $x$ be the singularity $\frac{1}{r}(1, q)$ with $0 < q < r$ and $\gcd(r, q) = 1$. Then $x$ is klt, the discrepancies of its minimal resolution lie in $(-1, 0]$, and they are all $0$ if and only if $q = r - 1$, that is, $x$ is the Du Val singularity $A_{r-1}$.

Lean: not in Lean as stated.

### Proof in words

On the minimal resolution the pullback of $K_X$ has degree $0$ on every exceptional curve, so the discrepancies solve a linear system with the negative definite intersection matrix, and since $K_Y$ is nef over $X$ the negativity lemma makes them nonpositive. If they are all zero, $K_Y$ has degree $0$ on every exceptional curve, and the genus formula forces $(-2)$-curves; conversely a Du Val resolution is crepant, and every further divisor has discrepancy at least $1$ because it lies over the smooth surface $Y$. For a toric surface the canonical divisor is minus the sum of the invariant divisors on every refinement, and its pullback is read off from the linear form $m_\sigma$; points in the interior of $\sigma$ have positive value, which gives discrepancies greater than $-1$.

### Examples

**Example P8.13.16 (the singularity $\frac{1}{5}(1, 2)$).** By Proposition P8.9.21 this is $U_\sigma$ for $\sigma = \operatorname{Cone}(e_2, 5 e_1 - 2 e_2)$, and $m_\sigma = (\frac{3}{5}, 1)$, since $\langle m_\sigma, 5 e_1 - 2 e_2 \rangle = 3 - 2 = 1$. The minimal resolution of Example P8.8.5 adds the rays $v_1 = e_1$ and $v_2 = 3 e_1 - e_2$, so by Proposition P8.13.14
$$a_1 = \tfrac{3}{5} - 1 = -\tfrac{2}{5}, \qquad a_2 = \left( \tfrac{9}{5} - 1 \right) - 1 = -\tfrac{1}{5}.$$
As a check, by Example P8.8.15, $E_1^2 = -3$, $E_2^2 = -2$ and $E_1 \cdot E_2 = 1$, so the system of Proposition P8.13.12 reads $-3 a_1 + a_2 = 1$ and $a_1 - 2 a_2 = 0$, and $\frac{6}{5} - \frac{1}{5} = 1$, $-\frac{2}{5} + \frac{2}{5} = 0$.

**Example P8.13.17 (the singularities $A_{r-1}$ and $\frac{1}{8}(1, 5)$).** For $A_{r-1} = \frac{1}{r}(1, r - 1)$, $\sigma = \operatorname{Cone}(e_2, r e_1 - (r - 1) e_2)$ and $m_\sigma = (1, 1)$. The rays of the minimal resolution are $v_j = j e_1 - (j - 1) e_2$ for $1 \leq j \leq r - 1$, with $\langle m_\sigma, v_j \rangle = 1$, so all discrepancies are $0$, as Theorem P8.13.13 requires. For $\frac{1}{8}(1, 5)$, $\frac{8}{5} = [2, 3, 2]$, the rays are $e_1$, $2 e_1 - e_2$ and $5 e_1 - 3 e_2$, and $m_\sigma = (\frac{3}{4}, 1)$. So the discrepancies are $-\frac{1}{4}, -\frac{1}{2}, -\frac{1}{4}$, the middle one on the $(-3)$-curve. The linear system of Proposition P8.13.12 for the chain of Example P8.11.16 gives the same numbers: $-2 a_1 + a_0 = 0$, $a_1 - 3 a_0 + a_2 = 1$ and $a_0 - 2 a_2 = 0$ have the solution $a_0 = -\frac{1}{2}$, $a_1 = a_2 = -\frac{1}{4}$.

**Example P8.13.18 (the elliptic cone and $D_4$).** For the cone over a plane cubic, the minimal resolution has a single exceptional curve $E$ of genus $1$, and $K_Y \cdot E = -E^2$ by the genus formula, so Proposition P8.13.12 gives $a(E, X) = -1$, as in Example P8.13.10. For the singularity $D_4$ of Theorem P8.10.4 the four exceptional curves are $(-2)$-curves, $K_Y \cdot E_i = 0$, and the linear system has the solution $a_i = 0$: the singularity is canonical, as Theorem P8.13.13 says.

**Example P8.13.19 (a tree of rational curves that is not log canonical).** Let $x$ be a singularity whose minimal resolution has the graph of Example P8.11.15, a central $(-2)$-curve $E_0$ meeting four disjoint $(-3)$-curves $E_1, \dots, E_4$, and assume that $K_X$ is $\mathbb{Q}$-Cartier near $x$. Then $K_Y \cdot E_0 = 0$ and $K_Y \cdot E_i = 1$, and the system of Proposition P8.13.12 reads $-2 a_0 + \sum_{i \geq 1} a_i = 0$ and $a_0 - 3 a_i = 1$ for $i \geq 1$. So $a_i = \frac{a_0 - 1}{3}$ and $-2 a_0 + \frac{4 (a_0 - 1)}{3} = 0$, which gives $a_0 = -2$ and $a_i = -1$. The exceptional curves form a divisor with simple normal crossings, and by Proposition P8.13.6 the point is not log canonical.

**Example P8.13.20 (two quotients of order three).** The singularities $\frac{1}{3}(1, 1)$ and $\frac{1}{3}(1, 2)$ are both quotients of $\mathbb{A}^2$ by $\mu_3$. The first has one $(-3)$-curve and discrepancy $-\frac{1}{3}$, by Example P8.13.9, so it is klt but not canonical. The second is $A_2$, with two $(-2)$-curves and discrepancies $0$, so it is canonical, and it is the quotient by the subgroup $\mu_3 \subseteq SL_2$, as Corollary P8.11.6 predicts.

### Proof

*Proposition P8.13.12.* Let $m \geq 1$ with $m K_X$ Cartier near $x$. The line bundle $\mathcal{O}_Y(f^*(m K_X)) = f^* \mathcal{O}_X(m K_X)$ is trivial on a neighbourhood of $f^{-1}(x)$, since $\mathcal{O}_X(m K_X)$ is trivial near $x$, so $f^* K_X \cdot E_i = 0$ for every $i$. Intersecting $K_Y = f^* K_X + \sum_j a_j E_j$ with $E_i$ gives $K_Y \cdot E_i = \sum_j a_j (E_j \cdot E_i)$, and Theorem P5.5.14 gives $K_Y \cdot E_i = 2 p_a(E_i) - 2 - E_i^2$. The intersection matrix of the $E_i$ is negative definite by Theorem P5.8.3, hence invertible, so the solution is unique. By Lemma P8.10.11, $K_Y \cdot E_i \geq 0$ for every $i$, since $f$ is minimal. So $B = -\sum_j a_j E_j$ satisfies $f_* B = 0$ and $B \cdot E_i = -K_Y \cdot E_i \leq 0$, and Corollary P5.8.4 gives $B \geq 0$, that is, every $a_i \leq 0$. Since $x$ is singular, $r \geq 1$ and $a(E_1, X) \leq 0$, so $x$ is not terminal. Conversely smooth surfaces are terminal by Example P8.13.7.

*Theorem P8.13.13.* Suppose $x$ is canonical. Then $a_i \geq 0$ by Definition P8.13.5 and $a_i \leq 0$ by Proposition P8.13.12, so every $a_i = 0$, and the linear system of Proposition P8.13.12 gives $K_Y \cdot E_i = 0$, that is, $E_i^2 = 2 p_a(E_i) - 2$. Since $E_i^2 < 0$ by Theorem P5.8.3 and $p_a(E_i) \geq 0$, this forces $p_a(E_i) = 0$ and $E_i^2 = -2$, and $E_i \cong \mathbb{P}^1$ by part 1 of Corollary P5.5.15. So every $E_i$ is a $(-2)$-curve, and $x$ is Du Val by Definition P8.10.1.

Conversely, let $x$ be Du Val. By Theorem P8.10.12, condition 1 implies condition 2 there: $K_X$ is Cartier near $x$ and $K_Y = f^* K_X$, so every $a_i = 0$. Let $F$ be a divisor over $X$ with centre $x$. If $F$ is a prime divisor on $Y$, it is one of the $E_i$, since these are the curves of $Y$ over $x$. Otherwise $F$ is exceptional over the smooth surface $Y$, and Lemma P8.13.3 with $A = 0$ and part 2 of Proposition P8.13.4 give $a(F, X) = a(F, Y) \geq 1$. After shrinking $X$ so that $x$ is its only singular point, every other exceptional divisor over $X$ has its centre in the smooth locus and discrepancy at least $1$ by Proposition P8.13.4. So $x$ is canonical.

*Proposition P8.13.14.* Choose $m \geq 1$ with $m m_\sigma \in M$. By Theorem P8.7.10, $m K_X = -m D_{u_1} - m D_{u_2}$ is Cartier on $U_\sigma$, with $m K_X = \operatorname{div}(\chi^{-m m_\sigma})$; so $K_X$ is $\mathbb{Q}$-Cartier. Let $\pi \colon X_{\Sigma'} \to U_\sigma$ be the morphism of Proposition P8.8.2, and $\omega$ the form of Theorem P8.7.17, which is the same rational form on $X_{\Sigma'}$ and on $U_\sigma$. Then $K_{X_{\Sigma'}} = \operatorname{div}(\omega) = -\sum_v D_v$ and $K_X = \operatorname{div}(\omega)$ on $U_\sigma$. By Lemma P8.7.2,
$$\pi^*(m K_X) = \operatorname{div}_{X_{\Sigma'}}(\chi^{-m m_\sigma}) = -\sum_v m \langle m_\sigma, v \rangle D_v,$$
so $K_{X_{\Sigma'}} - \pi^* K_X = \sum_v (\langle m_\sigma, v \rangle - 1) D_v$, which is the formula. For $v$ primitive in the interior of $\sigma$, the cones $\operatorname{Cone}(u_1, v)$ and $\operatorname{Cone}(v, u_2)$ with their faces form a fan refining $\sigma$, with $v$ as a ray.

*Corollary P8.13.15.* By Proposition P8.9.21, $x$ is $U_\sigma$ with $\sigma = \operatorname{Cone}(e_2, r e_1 - q e_2)$, and by Theorem P8.8.3 its minimal resolution is the toric refinement with rays $v_1, \dots, v_s$ in the interior of $\sigma$ (the curves have self-intersection $-b_i \leq -2$, so there is no $(-1)$-curve). Each $v_i = \lambda_1 u_1 + \lambda_2 u_2$ with $\lambda_1, \lambda_2 > 0$, so $\langle m_\sigma, v_i \rangle = \lambda_1 + \lambda_2 > 0$ and $a_i > -1$ by Proposition P8.13.14; $a_i \leq 0$ by Proposition P8.13.12. The exceptional curves form a chain of smooth rational curves meeting transversally, a divisor with simple normal crossings, so $x$ is klt by Proposition P8.13.6. All $a_i = 0$ means that $x$ is canonical, hence Du Val by Theorem P8.13.13, so all $b_i = 2$, and $\frac{r}{q} = [2, \dots, 2] = \frac{s + 1}{s}$ gives $r = s + 1$ and $q = r - 1$, by Example P8.8.6. Conversely $A_{r-1}$ is Du Val, so canonical.

### Exercises

1. (A) Compute the discrepancies of the minimal resolutions of $\frac{1}{7}(1, 2)$ and $\frac{1}{7}(1, 3)$ in two ways, by Proposition P8.13.14 and by the linear system of Proposition P8.13.12.
2. (A) Show that $\frac{1}{r}(1, 1)$ has the smallest discrepancy among all $\frac{1}{r}(1, q)$ with $0 < q < r$, by comparing $\langle m_\sigma, e_1 \rangle$ for the different cones.
3. (B) Show that the singularity of Exercise 5 of Section 11.2, a central $(-2)$-curve with three $(-3)$-curves attached, has discrepancies $a_0 = -1$ and $a_i = -\frac{2}{3}$ if $K_X$ is $\mathbb{Q}$-Cartier, so that it is rational and log canonical but not klt.
4. (B) Show that a normal surface singularity is log canonical but not klt if its minimal resolution is a single smooth curve of genus $1$, and that it is then not rational.
5. (B) Let $x$ be a klt surface singularity. Using Proposition P8.13.12 and the genus formula, show that every exceptional curve of the minimal resolution is a smooth rational curve.
6. (C) Use Proposition P8.13.14 to show that the minimal discrepancy over a cyclic quotient surface singularity $\frac{1}{r}(1, q)$ is attained on the minimal resolution, and that it is at least $-1 + \frac{2}{r}$.

### Lean

`MinimalModel.IsCanonical` and `MinimalModel.IsKlt` in `MinimalModel/Statements/Basic.lean` state the conditions of Theorem P8.13.13 and Corollary P8.13.15 for pairs, and the refinements of Proposition P8.13.14 are `MinimalModel.Toric.Fan.Refines`. The statements of this section are not in Lean as stated.

### Notes and history

Theorem P8.13.13 is the reason the Du Val singularities appear in the minimal model program: the canonical model of a surface of general type has exactly these singularities, and Reid (Rei87) took canonical singularities in higher dimension as their generalization. Together with Theorem P8.10.12 and Corollary P8.11.6 it shows that for a singular point of a surface the conditions Du Val, crepant minimal resolution, rational double point, rational and Gorenstein, canonical, and, over $\mathbb{C}$, quotient by a finite subgroup of $SL_2$, all agree; the last uses the classification of Theorem P8.10.5. Kollár and Mori, Section 4.1 (KM98), classify the klt surface singularities in characteristic $0$: they are the quotient singularities, and their resolution graphs are chains or star-shaped trees with three arms. Volume 4 proves that classification as Theorem 4.3.18.
