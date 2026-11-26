---
title: The canonical divisor
nodes: []
sources: [CLS11, Ful93, FS04]
reads_with: [CLS11:ch8, Ful93:ch4]
requires: [P8.6, P8.7, 3.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The canonical divisor

### Statement

**Theorem 3.3.26 (the toric canonical divisor).** Let $\Sigma$ be a fan in $N_{\mathbb{R}}$ and $m_1, \dots, m_n$ a basis of $M$. The rational $n$-form

$$\omega = \frac{d\chi^{m_1}}{\chi^{m_1}} \wedge \dots \wedge \frac{d\chi^{m_n}}{\chi^{m_n}}$$

does not depend on the basis up to sign, it is invariant under $T_N$, and its divisor is

$$K_{X_\Sigma} = \operatorname{div}(\omega) = -\sum_{\rho \in \Sigma(1)} D_\rho.$$

Lean: `MinimalModel.Toric.Fan.canonical`, defined as $-\sum_\rho D_\rho$ on the fan, with `MinimalModel.Toric.Fan.canonical_apply`; the identification with the canonical divisor of $X_\Sigma$ is not yet in Lean.

**Corollary 3.3.27 (Gorenstein and $\mathbb{Q}$-Gorenstein).** Let $\Sigma$ be a fan.

1. $K_{X_\Sigma}$ is Cartier if and only if for each $\sigma \in \Sigma$ there is $m_\sigma \in M$ with $\langle m_\sigma, u_\rho \rangle = 1$ for all $\rho \in \sigma(1)$. Since $X_\Sigma$ is Cohen-Macaulay, this is the condition that $X_\Sigma$ is Gorenstein.
2. $K_{X_\Sigma}$ is $\mathbb{Q}$-Cartier if and only if for each $\sigma$ there is $m_\sigma \in M_{\mathbb{Q}}$ with $\langle m_\sigma, u_\rho \rangle = 1$ for all $\rho \in \sigma(1)$, that is, the minimal generators of the rays of each cone lie on an affine hyperplane $\{\langle m_\sigma, \cdot \rangle = 1\}$. This holds when $\Sigma$ is simplicial.
3. When $K_{X_\Sigma}$ is $\mathbb{Q}$-Cartier, its *index*, the least $r \ge 1$ with $r K_{X_\Sigma}$ Cartier, is the least $r$ with $r m_\sigma \in M + (\sigma^\perp \cap M_{\mathbb{Q}})$ for all $\sigma$.

Lean: on the fan, part 1 is the condition `MinimalModel.Toric.Fan.IsCartier` for `MinimalModel.Toric.Fan.canonical`, and part 2 is `MinimalModel.Toric.Fan.isQCartier_iff` for it. For $\mathbb{P}^2$ they are `MinimalModel.Toric.P2.isCartier_canonical` and `MinimalModel.Toric.P2.isQCartier_canonical`. The Gorenstein property and the index are not yet in Lean.

Here $m_\sigma$ is the Cartier data of $K$ in the sense of Definition 3.3.11: the coefficients of $K$ are $a_\rho = -1$, so the condition $\langle m_\sigma, u_\rho \rangle = -a_\rho$ reads $\langle m_\sigma, u_\rho \rangle = 1$. On $U_\sigma$, $K = \operatorname{div}(\chi^{-m_\sigma})$. The vector $m_\sigma$ is the main tool of the toric singularity theory of Section 5.

### Proof in words

On the torus, $\omega$ is the standard invariant volume form $\frac{dx_1}{x_1} \wedge \dots \wedge \frac{dx_n}{x_n}$, with no zeros and no poles. A change of basis of $M$ multiplies it by the determinant of a matrix in $\mathrm{GL}_n(\mathbb{Z})$, which is $\pm 1$. To find its order along $D_\rho$, choose the basis adapted to $u_\rho$, so that $D_\rho = \{x_1 = 0\}$ in the chart $U_\rho$. The factor $dx_1 / x_1$ has a simple pole along $x_1 = 0$, and the other factors are regular and nonvanishing. So $\omega$ has a pole of order exactly one along each $D_\rho$.

The corollary is the Cartier criterion of Section 2 applied to $K$, with coefficients $a_\rho = -1$.

### Examples

**Example 3.3.28 (projective space and the projective line in Lean).** On $\mathbb{P}^n$, $K = -D_0 - D_1 - \dots - D_n \sim -(n+1) H$, the classical formula. On $\mathbb{P}^1$, $K = -D_0 - D_\infty$ has degree $-2$. The Lean library checks the combinatorial half of this: the fan of $\mathbb{P}^1$ has two rays (`MinimalModel.Toric.P1.card_ray`), and the sum of the coefficients of `MinimalModel.Toric.Fan.canonical` for it is $-2$ (`MinimalModel.Toric.P1.coeffSum_canonical`). For $\mathbb{P}^2$, with rays $e_1$, $e_2$ and $e_0 = (-1, -1)$, the library has three rays (`MinimalModel.Toric.P2.card_ray`), the sum $-3$ (`MinimalModel.Toric.P2.coeffSum_canonical`) and the Cartier data $m_\sigma = (1, 1)$, $(-2, 1)$ and $(1, -2)$ on the cones $\operatorname{Cone}(e_1, e_2)$, $\operatorname{Cone}(e_2, e_0)$ and $\operatorname{Cone}(e_0, e_1)$ (`MinimalModel.Toric.P2.isCartier_canonical`). So $K_{\mathbb{P}^2}$ is Cartier, as it must be on a smooth variety. In general the sum of the coefficients of $K$ is minus the number of rays (`MinimalModel.Toric.Fan.coeffSum_canonical`).

**Example 3.3.29 (the Hirzebruch surface).** On $\mathbb{F}_n$, with $f = [D_1] = [D_3]$ and $[D_4] = [D_2] + n f$ from Example 3.3.6,

$$K_{\mathbb{F}_n} = -D_1 - D_2 - D_3 - D_4 \sim -2 D_2 - (n + 2) f.$$

With $D_2^2 = -n$, $D_2 \cdot f = 1$ and $f^2 = 0$ (Example 3.3.15), $K^2 = 4(-n) + 4(n+2) + 0 = 8$, and $K \cdot D_2 = 2n - (n + 2) = n - 2$. So for $n \ge 1$ the negative section is $K$-negative only for $n = 1$, where it is the $(-1)$-curve of $\mathbb{F}_1 \to \mathbb{P}^2$, it is $K$-trivial for $n = 2$, and it is $K$-positive for $n \ge 3$.

**Example 3.3.30 (the cone of $\frac1n(1,1)$).** On $\sigma_n = \operatorname{Cone}(e_2, n e_1 - e_2)$ the equations $\langle m, e_2 \rangle = 1$ and $\langle m, n e_1 - e_2 \rangle = 1$ give

$$m_{\sigma_n} = \left(\tfrac{2}{n}, 1\right).$$

So $K$ is $\mathbb{Q}$-Cartier, and it is Cartier if and only if $n \mid 2$, that is, $n \le 2$. The index is the least $r$ with $n \mid 2r$, which is $n / \gcd(n, 2)$. For $n = 2$, the quadric cone is Gorenstein with $m_\sigma = (1, 1)$, and $K = \operatorname{div}(\chi^{-(1,1)})$ on it. For $n = 3$ the index is 3, and for $n = 4$ it is 2.

**Example 3.3.31 (the cone over a square and $\mathbb{P}(1,1,n)$).** The four generators $u_1, \dots, u_4$ of the cone over a square all have third coordinate 1, so $m_\sigma = (0, 0, 1)$ works, and $U_\sigma$ is Gorenstein even though it is not $\mathbb{Q}$-factorial. On $\mathbb{P}(1,1,n)$, $K = -D_1 - D_3 - D_4 \sim -(n + 2) D_0$. On the singular cone $\operatorname{Cone}(u_1, u_3)$ the equations $\langle m, (1, 0) \rangle = 1$ and $\langle m, (-1, n) \rangle = 1$ give $m = (1, 2/n)$, so the index is again $n / \gcd(n, 2)$.

**Example 3.3.32 (a canonical divisor that is not $\mathbb{Q}$-Cartier).** Let $\sigma = \operatorname{Cone}(e_1, e_2, e_3, v) \subset \mathbb{R}^3$ with $v = (1, 1, -2)$. The form $(2, 2, 1)$ is positive on all four generators, so $\sigma$ is strongly convex. None of the four generators is in the cone of the other three: for example $e_3 = \frac12(e_1 + e_2 - v)$ has a negative coefficient, and so does $v = e_1 + e_2 - 2 e_3$. So $\sigma$ has four rays. An $m = (a, b, c)$ with $\langle m, e_i \rangle = 1$ for $i = 1, 2, 3$ is $(1, 1, 1)$, and then $\langle m, v \rangle = 0 \neq 1$. So $K_{U_\sigma}$ is not $\mathbb{Q}$-Cartier, and $U_\sigma$ is a normal toric 3-fold that is not $\mathbb{Q}$-Gorenstein. Such varieties are outside the MMP of Kollár-Mori, where $K$ must be $\mathbb{Q}$-Cartier for discrepancies to make sense.

### Proof

*Proof of Theorem 3.3.26.* If $m'_j = \sum_i c_{ij} m_i$ is another basis, then $\chi^{m'_j} = \prod_i (\chi^{m_i})^{c_{ij}}$ and $d\chi^{m'_j} / \chi^{m'_j} = \sum_i c_{ij} \, d\chi^{m_i}/\chi^{m_i}$. So the wedge product changes by $\det(c_{ij}) = \pm 1$. The form is invariant under $T_N$ because each factor is: for $t \in T_N$, $\chi^m(t x) = \chi^m(t) \chi^m(x)$, and $\chi^m(t)$ is a constant that cancels in $d\chi^m / \chi^m$. On $T_N = \operatorname{Spec} k[x_1^{\pm 1}, \dots, x_n^{\pm 1}]$, $\omega = (x_1 \cdots x_n)^{-1} dx_1 \wedge \dots \wedge dx_n$ is a generator of $\Omega^n$, so $\operatorname{div}(\omega)$ is supported on $\bigcup_\rho D_\rho$. Fix $\rho$, and choose the basis $m_1, \dots, m_n$ of the proof of Proposition 3.3.3, so that $U_\rho = \operatorname{Spec} k[x_1, x_2^{\pm 1}, \dots, x_n^{\pm 1}]$ and $D_\rho \cap U_\rho = \{x_1 = 0\}$. On $U_\rho$, the sheaf $\Omega^n$ is free with generator $dx_1 \wedge \dots \wedge dx_n$, and $x_2, \dots, x_n$ are units there. So $\omega = x_1^{-1} \cdot (\text{unit}) \cdot dx_1 \wedge \dots \wedge dx_n$, and $\operatorname{ord}_{D_\rho}(\omega) = -1$. Since $X_\Sigma$ is normal, its canonical divisor is the divisor of a rational $n$-form, computed on the smooth locus, which contains the generic points of all $D_\rho$. So $K_{X_\Sigma} = -\sum_\rho D_\rho$. $\square$

*Proof of Corollary 3.3.27.* Parts 1 and 2 are Theorem 3.3.12 and part 1 of Theorem 3.3.20 for $D = K$, with $a_\rho = -1$. A simplicial cone has linearly independent $u_\rho$, so the equations have a rational solution. The ring $k[S_\sigma]$ is Cohen-Macaulay by Hochster's theorem (Cox-Little-Schenck, Chapter 9), and a Cohen-Macaulay variety is Gorenstein exactly when its canonical divisor is Cartier. For part 3, $rK$ is Cartier on $U_\sigma$ if and only if some $m \in M$ has $\langle m, u_\rho \rangle = r$ for $\rho \in \sigma(1)$, which says that $m - r m_\sigma$ vanishes on $\sigma$, that is, $r m_\sigma \in M + \sigma^\perp_{\mathbb{Q}}$. $\square$

### Exercises

1. (A) Compute $K$ for $\mathbb{P}^1 \times \mathbb{P}^1$ and for the blow-up of $\mathbb{P}^2$ in three fixed points (the fan with six rays), and check that $K^2 = 8$ and $K^2 = 6$.
2. (A) Find the index of $K$ for the cone of $\frac1n(1,q)$ in terms of $n$ and $q$.
3. (B) Show that for a smooth complete toric surface with $r$ rays, $K^2 = 12 - r$. Compare with Noether's formula.
4. (B) Show that $U_\sigma$ is Gorenstein if and only if the minimal generators of the rays of $\sigma$ lie on a lattice hyperplane $\{\langle m, \cdot \rangle = 1\}$ with $m \in M$, and deduce that a 2-dimensional Gorenstein cone is, up to $\mathrm{GL}_2(\mathbb{Z})$, $\operatorname{Cone}(e_2, n e_1 - (n-1) e_2)$, the $A_{n-1}$ singularity.
5. (C) Let $\Sigma$ be a complete fan. Show that $-K_{X_\Sigma}$ is Cartier and ample if and only if the minimal generators $u_\rho$ are the vertices of a convex polytope $P$ whose polar polytope $P^\circ$ has its vertices in $M$. (Use the ampleness criterion of Cox-Little-Schenck, Chapter 6.)

### Lean

- Status: the Lean library defines the toric canonical divisor on a fan, `MinimalModel.Toric.Fan.canonical`, as $-\sum_\rho D_\rho$, with every coefficient equal to $-1$ (`MinimalModel.Toric.Fan.canonical_apply`). Its real version is `MinimalModel.Toric.Fan.canonicalReal`, with `MinimalModel.Toric.Fan.canonicalReal_apply`. The sum of its coefficients is minus the number of rays, `MinimalModel.Toric.Fan.coeffSum_canonical`, where `MinimalModel.Toric.Fan.coeffSum` is the sum of the coefficients. The trivial fan has no rays (`MinimalModel.Toric.Fan.rays_trivial`), so its canonical divisor is zero. For $\mathbb{P}^2$, `MinimalModel.Toric.P2.isCartier_canonical` gives Cartier data for $K$, and `MinimalModel.Toric.P2.coeffSum_canonical` gives $-3$. For $\mathbb{P}^1$, `MinimalModel.Toric.P1.rays_fan` says that the rays of the fan are the two rays `pos` and `neg`, the cones on $1$ and $-1$, and `MinimalModel.Toric.P1.coeffSum_canonical` gives $-2$.
- Fidelity: in Lean, `MinimalModel.Toric.Fan.canonical` is a definition on the fan, not a theorem. Theorem 3.3.26, which says that this divisor is the divisor of the invariant form $\omega$ on $X_\Sigma$, is not yet in Lean; it waits for the scheme $X_\Sigma$ of route R3. The sum of the coefficients is a statement about the divisor on the fan; on $\mathbb{P}^1$ it equals the degree of $K$, but in higher dimension it is not an intersection number.
- No node of the map covers this section.

### Notes and history

The formula $K = -\sum_\rho D_\rho$ is in Danilov's survey (1978) and in Oda's book, and Cox-Little-Schenck, Chapter 8, proves it with the form $\omega$. The Gorenstein criterion in terms of a hyperplane goes back to Reid, who used it in *Canonical 3-folds* (1980) and in the toric MMP (1983). Reflexive polytopes, the polytopes of Exercise 5, give the Gorenstein toric Fano varieties, and Batyrev used them for mirror symmetry.
