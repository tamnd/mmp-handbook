---
title: Cartier divisors and the Picard group
nodes: []
sources: [CLS11, Ful93]
reads_with: [CLS11:ch4, Ful93:3.3, Ful93:3.4]
requires: [P3.8, P3.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Cartier divisors and the Picard group

### Statement

Let $\Sigma$ be a fan in $N_\mathbb{R}$ and $D = \sum_\rho a_\rho D_\rho$ a torus-invariant divisor on $X_\Sigma$. For $\sigma \in \Sigma$, write $\sigma(1)$ for the set of rays of $\sigma$.

**Definition P8.7.9 (Cartier data and support functions).** *Cartier data* for $D$ is a family $(m_\sigma)_{\sigma \in \Sigma}$ of elements of $M$ with
$$\langle m_\sigma, u_\rho \rangle = -a_\rho \quad \text{for all } \rho \in \sigma(1).$$
A *support function* of $\Sigma$ is a function $\varphi \colon |\Sigma| \to \mathbb{R}$ that is linear on each cone of $\Sigma$, and it is *integral* if it takes integer values on $|\Sigma| \cap N$. The support function of $D$, when it exists, is the support function $\varphi_D$ with $\varphi_D(u_\rho) = -a_\rho$ for all $\rho$. The group of torus-invariant Cartier divisors is $\operatorname{CDiv}_T(X_\Sigma)$.

**Theorem P8.7.10 (the Cartier criterion).** Let $\sigma \in \Sigma$. The divisor $D$ is Cartier on $U_\sigma$ if and only if there is $m_\sigma \in M$ with $\langle m_\sigma, u_\rho \rangle = -a_\rho$ for all $\rho \in \sigma(1)$. Then $D|_{U_\sigma} = \operatorname{div}(\chi^{-m_\sigma})|_{U_\sigma}$, $\mathcal{O}(D)|_{U_\sigma} = \chi^{m_\sigma} \mathcal{O}_{U_\sigma}$, and $m_\sigma$ is unique modulo $\sigma^\perp \cap M$. Consequently the following are equivalent:

1. $D$ is Cartier;
2. $D$ has Cartier data;
3. there is an integral support function $\varphi_D$ with $\varphi_D(u_\rho) = -a_\rho$ for all $\rho$, given on each $\sigma$ by $\varphi_D = \langle m_\sigma, \cdot \rangle$.

It is enough to check the condition on the maximal cones of $\Sigma$.

Lean: `MinimalModel.Toric.Fan.IsCartier` takes condition 2 as the definition of a Cartier divisor, and `MinimalModel.Toric.Fan.IsSupportFunctionOf` is condition 3 with real values; the equivalence with the scheme-theoretic notion is not in Lean as stated.

**Corollary P8.7.11 (the Picard group).**

1. Every Cartier divisor on $X_\Sigma$ is linearly equivalent to a torus-invariant Cartier divisor, and $\operatorname{Pic}(X_\Sigma) \cong \operatorname{CDiv}_T(X_\Sigma) / \{ \operatorname{div}(\chi^m) : m \in M \}$.
2. If the $u_\rho$ span $N_\mathbb{R}$, there is an exact sequence $0 \to M \to \operatorname{CDiv}_T(X_\Sigma) \to \operatorname{Pic}(X_\Sigma) \to 0$.
3. $\operatorname{Pic}(U_\sigma) = 0$ for every cone $\sigma$.

Lean: not in Lean as stated.

**Corollary P8.7.12 (smooth and simplicial fans).**

1. If $\Sigma$ is smooth, every Weil divisor on $X_\Sigma$ is Cartier and $\operatorname{Pic}(X_\Sigma) = \operatorname{Cl}(X_\Sigma)$.
2. A torus-invariant divisor $D$ is $\mathbb{Q}$-Cartier if and only if for each $\sigma \in \Sigma$ there is $m_\sigma \in M_\mathbb{Q}$ with $\langle m_\sigma, u_\rho \rangle = -a_\rho$ for $\rho \in \sigma(1)$.
3. $X_\Sigma$ is $\mathbb{Q}$-factorial if and only if $\Sigma$ is simplicial.

Lean: part 2 is `MinimalModel.Toric.Fan.isQCartier_iff`, for the combinatorial definition `MinimalModel.Toric.Fan.IsQCartier`; parts 1 and 3 are not in Lean as stated.

### Proof in words

If $D$ is Cartier at the distinguished point of $\sigma$, then $\mathcal{O}(D)$ is free of rank one at the generic point of the orbit $O(\sigma)$. The module of sections over $U_\sigma$ is spanned by characters, by Proposition P8.7.3, so its fibre there is graded by $M$ modulo $\sigma^\perp$, and a graded module of rank one has one generating degree. That degree is a character $\chi^{m_\sigma}$ generating the whole module, which forces $D = \operatorname{div}(\chi^{-m_\sigma})$ on $U_\sigma$. The rest is linear algebra: on a smooth cone the ray generators are part of a basis, so the equations for $m_\sigma$ can always be solved over $\mathbb{Z}$, and on a simplicial cone they are linearly independent, so they can be solved over $\mathbb{Q}$; conversely solvability for every divisor forces independence.

### Examples

**Example P8.7.13 (cyclic quotient singularities).** Let $\sigma = \operatorname{Cone}(e_2, d e_1 - k e_2)$ as in Example P8.7.7, with $u_1 = e_2$, $u_2 = d e_1 - k e_2$. For $D = a_1 D_1 + a_2 D_2$ a solution $m = (x, y)$ of $y = -a_1$, $dx - ky = -a_2$ is $x = -(a_2 + k a_1)/d$, so $D$ is Cartier if and only if $d \mid a_2 + k a_1$, and every $D$ is $\mathbb{Q}$-Cartier, as Corollary P8.7.12 predicts for a simplicial cone. For the canonical divisor $K = -D_1 - D_2$ of Theorem P8.7.17 the condition is $d \mid k + 1$. For $\frac{1}{n}(1, 1)$, that is $k = 1$, $K$ is Cartier exactly when $n \leq 2$: the quadric cone is Gorenstein, and the cones over the rational normal curves of degree $n \geq 3$ are not. In general $K$ has index $d / \gcd(d, k + 1)$, and the singularities $\frac{1}{d}(1, d - 1)$, the du Val singularities of type $A_{d-1}$, are the Gorenstein ones.

**Example P8.7.14 (the cone over a square).** For the cone $\sigma$ of Example P8.7.8, a form $m = (a, b, c)$ with $\langle m, u_1 \rangle = -1$ and $\langle m, u_i \rangle = 0$ for $i = 2, 3, 4$ would satisfy $c = -1$, $a + c = 0$, $b + c = 0$ and $a + b + c = 0$, which is impossible, and the same equations with $-r$ in place of $-1$ force $r = 0$. So $D_1$ is not $\mathbb{Q}$-Cartier, and $U_\sigma$ is not $\mathbb{Q}$-factorial, as Corollary P8.7.12 predicts for a cone with four rays in dimension three. On the other hand $m = e_3^*$ takes the value $1$ on all four rays, so $K = -\sum D_i = \operatorname{div}(\chi^{-e_3^*})$ is Cartier, and even principal, as for any hypersurface singularity.

**Example P8.7.15 (projective space and the Hirzebruch surfaces).** The fans of $\mathbb{P}^n$ and $F_n$ are smooth, so by Corollary P8.7.12 their Picard groups are their class groups, $\operatorname{Pic}(\mathbb{P}^n) = \mathbb{Z}$ and $\operatorname{Pic}(F_n) = \mathbb{Z}[C_-] \oplus \mathbb{Z}[F]$, as in Examples P8.7.5 and P8.7.6. For $D = b D_1 + a D_2$ on $F_n$, Cartier data on the four maximal cones is
$$m_{12} = (-b, -a), \quad m_{23} = (-na, -a), \quad m_{34} = (0, 0), \quad m_{41} = (-b, 0),$$
where $m_{ij}$ belongs to $\operatorname{Cone}(u_i, u_j)$; for instance $\langle (-na, -a), (-1, n) \rangle = na - na = 0$.

**Example P8.7.16 (the weighted projective plane $\mathbb{P}(1, 1, n)$).** By Exercise 6 of Section 6.2, $\mathbb{P}(1, 1, n)$ is the toric variety of the fan with rays $u_1 = (1, 0)$, $u_3 = (-1, n)$ and $u_4 = (0, -1)$. The relations $\operatorname{div}(\chi^{(1, 0)}) = D_1 - D_3$ and $\operatorname{div}(\chi^{(0, 1)}) = n D_3 - D_4$ give $\operatorname{Cl} \cong \mathbb{Z}$, generated by $[D_1]$, with $D_3 \sim D_1$ and $D_4 \sim n D_1$. The cones $\operatorname{Cone}(u_3, u_4)$ and $\operatorname{Cone}(u_4, u_1)$ are smooth. On $\operatorname{Cone}(u_1, u_3)$, which is the cone $\frac{1}{n}(1, 1)$ in another basis, $a D_1$ needs $m = (x, y)$ with $x = -a$ and $-x + ny = 0$, so $y = -a/n$. So $a D_1$ is Cartier if and only if $n \mid a$, and $\operatorname{Pic}(\mathbb{P}(1, 1, n)) = n \mathbb{Z} \subseteq \operatorname{Cl} = \mathbb{Z}$, generated by the class of $D_4$, which is the curve $x_2 = 0$ and corresponds to $\mathcal{O}(n)$.

### Proof

*Theorem P8.7.10.* If $m_\sigma$ exists, Lemma P8.7.2 gives $\operatorname{div}(\chi^{-m_\sigma})|_{U_\sigma} = \sum_{\rho \in \sigma(1)} \langle -m_\sigma, u_\rho \rangle D_\rho = D|_{U_\sigma}$, since the invariant prime divisors meeting $U_\sigma$ are the $D_\rho$ with $\rho \in \sigma(1)$. So $D$ is principal, hence Cartier, on $U_\sigma$, and $\mathcal{O}(D)|_{U_\sigma} = \chi^{m_\sigma} \mathcal{O}_{U_\sigma}$. Two choices differ by an $m$ vanishing on all $u_\rho$, $\rho \in \sigma(1)$, that is by an element of $\sigma^\perp \cap M$.

Conversely, suppose $D$ is Cartier on $U_\sigma$. Let $A = k[S_\sigma]$, $P = \Gamma(U_\sigma, \mathcal{O}(D))$ and
$$Q_D = \{ m \in M : \langle m, u_\rho \rangle \geq -a_\rho \text{ for } \rho \in \sigma(1) \},$$
so $P = \bigoplus_{m \in Q_D} k \chi^m$ by Proposition P8.7.3. Put $L = \sigma^\perp \cap M$ and let $I \subseteq A$ be the span of the $\chi^s$ with $s \in S_\sigma \setminus L$. By the proof of Theorem P8.6.25, $I$ is the prime ideal of the orbit $O(\sigma)$, with $A / I = k[L]$, and $\gamma_\sigma \in O(\sigma)$. Near $\gamma_\sigma$, $D = \operatorname{div}(f)$ and $\mathcal{O}(D) = f^{-1} \mathcal{O}$ is invertible (Proposition P3.9.3), so it is free of rank one at the generic point $\eta$ of $O(\sigma)$, a generization of $\gamma_\sigma$. So $P_I$ is free of rank one over $A_I$, and $P \otimes_A \kappa(\eta)$ is one-dimensional over $\kappa(\eta) = \operatorname{Frac} k[L]$.

The submodule $IP$ is spanned by the $\chi^{m + s}$ with $m \in Q_D$ and $s \in S_\sigma \setminus L$, so the $k[L]$-module $\bar P = P / IP$ has a basis of the classes of $\chi^m$ for $m$ in
$$\operatorname{Min} = Q_D \setminus \big( Q_D + (S_\sigma \setminus L) \big).$$
This set is stable under adding elements of $L$: if $m \in \operatorname{Min}$ and $l \in L$, then $m + l \in Q_D$, and $m + l = m' + s$ with $s \in S_\sigma \setminus L$ would give $m = m' + (s - l)$ with $s - l \in S_\sigma \setminus L$. So $\bar P$ is the free $k[L]$-module with one basis element $\chi^{m}$ for each class of $\operatorname{Min}$ modulo $L$, and its rank, which is $\dim_{\kappa(\eta)} P \otimes_A \kappa(\eta) = 1$, is the number of classes. So $\operatorname{Min} = m_0 + L$ for some $m_0 \in Q_D$.

Every $m \in Q_D$ lies in $m_0 + S_\sigma$. Indeed, let $u_\sigma = \sum_{\rho \in \sigma(1)} u_\rho$. For $s \in S_\sigma \setminus L$, $\langle s, u_\sigma \rangle$ is a positive integer, since $s$ is nonnegative on each $u_\rho$ and nonzero on one of them, and $\langle m, u_\sigma \rangle \geq -\sum_{\rho \in \sigma(1)} a_\rho$ on $Q_D$. So writing $m = m' + s$ with $m' \in Q_D$, $s \in S_\sigma \setminus L$ as long as $m \notin \operatorname{Min}$ stops after finitely many steps, and $m \in \operatorname{Min} + S_\sigma = m_0 + S_\sigma$. Hence $Q_D = m_0 + S_\sigma$ and $P = \chi^{m_0} A$.

It remains to compute $\langle m_0, u_\rho \rangle$ for $\rho \in \sigma(1)$. By Proposition P8.6.13 (3) there is $m_1 \in S_\sigma$ with $\sigma \cap m_1^\perp = \rho$, so $\langle m_1, u_{\rho'} \rangle > 0$ for the other rays $\rho'$ of $\sigma$. Choose $m' \in M$ with $\langle m', u_\rho \rangle = -a_\rho$, possible as $u_\rho$ is primitive. For a large integer $c$, $m' + c m_1 \in Q_D$ and $\langle m' + c m_1, u_\rho \rangle = -a_\rho$. On $Q_D = m_0 + S_\sigma$ the minimum of $\langle \cdot, u_\rho \rangle$ is $\langle m_0, u_\rho \rangle$, and it is at least $-a_\rho$ and attained at $-a_\rho$, so $\langle m_0, u_\rho \rangle = -a_\rho$. So $m_\sigma = m_0$ works.

For the equivalence, (1) and (2) are the local statement on the open cover by the $U_\sigma$. Given Cartier data, the linear functions $\langle m_\sigma, \cdot \rangle$ on the cones agree on common faces, since for $\tau = \sigma \cap \sigma'$ both $m_\sigma$ and $m_{\sigma'}$ restrict to Cartier data on $\tau$, which is unique modulo $\tau^\perp$. So they glue to an integral support function. Conversely, the linear function of an integral support function on $\sigma$ is $\langle m', \cdot \rangle$ for some $m' \in M_\mathbb{R}$, and it takes integer values on $\sigma \cap N$. The lattice points of $\sigma$ generate the group $N_\sigma = N \cap \operatorname{span}(\sigma)$, by the argument of Lemma P8.6.23 (1) applied to $\sigma$ in $\operatorname{span}(\sigma)$, so $m'$ restricts to a homomorphism $N_\sigma \to \mathbb{Z}$. Since $N_\sigma$ is a direct summand of $N$ (Lemma P8.6.24), this homomorphism extends to some $m_\sigma \in M$, which agrees with $m'$ on $\sigma$. So $m_\sigma$ can be chosen in $M$. Finally, every cone is a face of a maximal cone, and Cartier data on $\sigma$ restricts to Cartier data on its faces.

*Corollary P8.7.11.* (1) A Cartier divisor $E$ is linearly equivalent to a torus-invariant divisor $D$ by Theorem P8.7.4, and $D = E + \operatorname{div}(f)$ is Cartier. For $X_\Sigma$ normal, $\operatorname{Pic}(X_\Sigma)$ is the group of Cartier divisors modulo principal divisors (Theorem P3.9.4) and maps injectively to $\operatorname{Cl}(X_\Sigma)$ (Proposition P3.9.9). The principal torus-invariant divisors are the $\operatorname{div}(\chi^m)$, by the proof of Theorem P8.7.4. (2) follows from (1) and the injectivity in Theorem P8.7.4. (3) By Theorem P8.7.10, a torus-invariant Cartier divisor on $U_\sigma$ is $\operatorname{div}(\chi^{-m_\sigma})$, which is principal, and by (1) every Cartier divisor is linearly equivalent to one.

*Corollary P8.7.12.* (1) If $\sigma$ is smooth, its ray generators are part of a basis of $N$, and with the dual basis of $M$ the equations $\langle m, u_\rho \rangle = -a_\rho$ have an integral solution. So every torus-invariant divisor is Cartier, and every Weil divisor is linearly equivalent to one, by Theorem P8.7.4. (2) If $rD$ is Cartier with Cartier data $m_\sigma$, then $m_\sigma / r \in M_\mathbb{Q}$ works. Conversely, given $m_\sigma \in M_\mathbb{Q}$ for the finitely many cones, let $r$ be a common denominator; then $r m_\sigma \in M$ is Cartier data for $rD$. (3) If $\Sigma$ is simplicial, the $u_\rho$, $\rho \in \sigma(1)$, are linearly independent, so the equations of (2) have a solution in $M_\mathbb{Q}$ for every $D$. Every invariant divisor is then $\mathbb{Q}$-Cartier, and every Weil divisor is linearly equivalent to one, so $X_\Sigma$ is $\mathbb{Q}$-factorial (Definition P3.9.18). Conversely, if $X_\Sigma$ is $\mathbb{Q}$-factorial, each $D_\rho$ is $\mathbb{Q}$-Cartier, so by (2) the map $M_\mathbb{Q} \to \mathbb{Q}^{\sigma(1)}$, $m \mapsto (\langle m, u_\rho \rangle)_\rho$, hits every standard basis vector, up to sign. It is surjective, so the $u_\rho$, $\rho \in \sigma(1)$, are linearly independent, and $\sigma$ is simplicial.

### Exercises

1. (A) Show that every torus-invariant divisor on $\mathbb{P}^1 \times \mathbb{P}^1$ is Cartier, and write down the support function of $D_1 + D_2$ for two rays $u_1 = e_1$, $u_2 = e_2$.
2. (A) Show that the divisor $D_1$ of Example P8.7.13 has index $d$, and that for $d$ prime every nonzero class in $\operatorname{Cl}(U_\sigma)$ has index $d$.
3. (B) Compute $\operatorname{Cl}$ and $\operatorname{Pic}$ of the weighted projective plane $\mathbb{P}(1, 2, 3)$, the toric variety of the fan with rays $u_0 = -2 e_1 - 3 e_2$, $u_1 = e_1$ and $u_2 = e_2$, and the index of $K = -D_0 - D_1 - D_2$.
4. (B) Show that a support function of $\Sigma$ is determined by its values on the $u_\rho$ when $\Sigma$ is simplicial, and give an example of a fan where a function on $\Sigma(1)$ does not extend to a support function.
5. (B) Let $\Sigma$ be the fan of the faces of the cone over a square together with the subdivision along the diagonal $\operatorname{Cone}(u_1, u_3)$. Show that the result is a simplicial fan, that $D_1$ is Cartier on it, and compute its Picard group.
6. (C) Show that a toric variety $X_\Sigma$ whose fan has a cone of dimension $n$ satisfies $\mathcal{O}(X_\Sigma)^* = k^*$ when the $u_\rho$ span $N_\mathbb{R}$, and deduce that $\operatorname{Pic}(X_\Sigma)$ is free when $\Sigma$ has a cone of dimension $n$. Hint: a Cartier divisor with Cartier data $m_\sigma$ that is principal is $\operatorname{div}(\chi^m)$, and compare $m$ with $m_\sigma$ for a cone of dimension $n$.

### Lean

The repository takes the Cartier criterion as the definition: `MinimalModel.Toric.Fan.IsCartier` asks for $m_\sigma \in M$ on every cone, `MinimalModel.Toric.Fan.IsQCartier` asks that a positive multiple be Cartier, and `MinimalModel.Toric.Fan.isQCartier_iff` is part 2 of Corollary P8.7.12. The real version `MinimalModel.Toric.Fan.IsRCartier` allows $m_\sigma \in M_\mathbb{R}$; `MinimalModel.Toric.Fan.IsSupportFunction` and `MinimalModel.Toric.Fan.IsSupportFunctionOf` are support functions of the fan and of a divisor, and `MinimalModel.Toric.Fan.isRCartier_iff_exists_isSupportFunctionOf` is the equivalence of conditions 2 and 3 of Theorem P8.7.10 over $\mathbb{R}$. The example `MinimalModel.Toric.P2.isCartier_canonical` checks that the canonical divisor of $\mathbb{P}^2$ satisfies the criterion. Since there is no scheme $X_\Sigma$ in the repository, the comparison with locally principal divisors is not in Lean.

### Notes and history

The Cartier criterion and the description of $\operatorname{Pic}(X_\Sigma)$ by piecewise linear functions are due to Demazure for smooth complete fans and to Kempf, Knudsen, Mumford and Saint-Donat in general. The proof given here, through the graded fibre of $\mathcal{O}(D)$ along the closed orbit, is a variant of Cox, Little and Schenck, Proposition 4.2.2 and Theorem 4.2.8, and of Fulton, Section 3.3. The statement that $\mathbb{Q}$-factoriality is simpliciality is Cox, Little and Schenck, Proposition 4.2.7; it is the reason the toric minimal model program of Volume 3 runs within simplicial fans.
