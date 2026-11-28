---
title: Torus-invariant divisors and the class group
nodes: []
sources: [CLS11, Ful93, Oda88]
reads_with: [CLS11:ch4, Ful93:3.3]
requires: [P3.8, P3.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Torus-invariant divisors and the class group

### Statement

Let $\Sigma$ be a fan in $N_\mathbb{R}$ over an algebraically closed field $k$, with toric variety $X_\Sigma$ of dimension $n$ (Theorem P8.6.15). Write $\Sigma(1)$ for the set of rays of $\Sigma$ and $u_\rho \in N$ for the primitive generator of the ray $\rho$. The function field of $X_\Sigma$ is $k(M) = \operatorname{Frac} k[M]$, and $X_\Sigma$ is normal, so it has Weil divisors, principal divisors and a class group (Definition P3.8.10).

**Definition P8.7.1 (torus-invariant divisors).** For $\rho \in \Sigma(1)$, the *torus-invariant prime divisor* of $\rho$ is $D_\rho = V(\rho)$, the closure of the orbit $O(\rho)$. A *torus-invariant divisor* is a finite sum $D = \sum_{\rho} a_\rho D_\rho$ with $a_\rho \in \mathbb{Z}$, and these form the free group $\operatorname{Div}_T(X_\Sigma) = \bigoplus_{\rho \in \Sigma(1)} \mathbb{Z} D_\rho$. For $D \in \operatorname{Div}_T(X_\Sigma)$ put
$$P_D = \{ m \in M_\mathbb{R} : \langle m, u_\rho \rangle \geq -a_\rho \text{ for all } \rho \in \Sigma(1) \},$$
a rational polyhedron in $M_\mathbb{R}$.

**Lemma P8.7.2 (orders along the invariant divisors).** Let $\rho \in \Sigma(1)$.

1. $D_\rho$ is a prime divisor of $X_\Sigma$, $D_\rho \cap U_\rho = O(\rho)$, and the local ring of $X_\Sigma$ at the generic point of $D_\rho$ is a discrete valuation ring with uniformizer $\chi^{m_1}$, for any $m_1 \in M$ with $\langle m_1, u_\rho \rangle = 1$.
2. For a nonzero Laurent polynomial $f = \sum_m c_m \chi^m \in k[M]$, $\operatorname{ord}_{D_\rho}(f) = \min \{ \langle m, u_\rho \rangle : c_m \neq 0 \}$.
3. The prime divisors of $X_\Sigma$ contained in $X_\Sigma \setminus T_N$ are exactly the $D_\rho$, and they are distinct for distinct rays. For $m \in M$,
$$\operatorname{div}(\chi^m) = \sum_{\rho \in \Sigma(1)} \langle m, u_\rho \rangle D_\rho .$$

Lean: not in Lean as stated.

**Proposition P8.7.3 (sections of a torus-invariant divisor).** Let $D = \sum_\rho a_\rho D_\rho$. Inside $k(M)$,
$$\Gamma(X_\Sigma, \mathcal{O}_{X_\Sigma}(D)) = \bigoplus_{m \in P_D \cap M} k \, \chi^m .$$
The same holds on $U_\sigma$ for $\sigma \in \Sigma$, with $P_D$ replaced by $\{ m : \langle m, u_\rho \rangle \geq -a_\rho \text{ for } \rho \in \sigma(1) \}$, where $\sigma(1)$ is the set of rays of $\sigma$.

Lean: not in Lean as stated.

**Theorem P8.7.4 (the class group).** The sequence
$$M \xrightarrow{\ m \mapsto \operatorname{div}(\chi^m)\ } \operatorname{Div}_T(X_\Sigma) \longrightarrow \operatorname{Cl}(X_\Sigma) \longrightarrow 0$$
is exact. If the $u_\rho$ span $N_\mathbb{R}$, the first map is injective, and $\operatorname{Cl}(X_\Sigma)$ is a finitely generated group of rank $|\Sigma(1)| - n$. In particular every Weil divisor on $X_\Sigma$ is linearly equivalent to a torus-invariant one.

Lean: `MinimalModel.Toric.Fan.TDivisor` is the group $\operatorname{Div}_T$, with coefficients in any ring; the theorem is not in Lean as stated.

### Proof in words

Along $D_\rho$ the variety looks like $\mathbb{A}^1 \times \mathbb{G}_m^{n-1}$, with $D_\rho$ the zero set of one coordinate $x$, and a character $\chi^m$ is $x^{\langle m, u_\rho \rangle}$ times a unit. Distinct characters are distinct monomials, so the order of a Laurent polynomial is the least exponent of $x$ that occurs. A rational function with no zeros or poles on the torus is a unit of the Laurent polynomial ring, hence a multiple of a character, and the torus has trivial class group, so excision of the complement of the torus gives the exact sequence. The space of sections of $\mathcal{O}(D)$ is read off in the same way: a function regular on the torus is a Laurent polynomial, and the condition $\operatorname{div} f + D \geq 0$ is a condition on each monomial separately.

### Examples

**Example P8.7.5 (projective space).** For the fan of $\mathbb{P}^n$ of Example P8.6.18, with rays $e_0, \dots, e_n$ and $e_0 = -e_1 - \dots - e_n$, the divisor $D_i = D_{\operatorname{Cone}(e_i)}$ is the hyperplane $V_+(x_i)$, since $\chi^{e_i^*} = x_i / x_0$ for $i \geq 1$. By Lemma P8.7.2, $\operatorname{div}(x_i / x_0) = D_i - D_0$, because $\langle e_i^*, e_j \rangle = \delta_{ij}$ for $j \geq 1$ and $\langle e_i^*, e_0 \rangle = -1$. So Theorem P8.7.4 gives $\operatorname{Cl}(\mathbb{P}^n) = \mathbb{Z}^{n+1} / \langle D_i - D_0 \rangle \cong \mathbb{Z}$, with every $D_i$ mapping to $1$, as in Corollary P3.9.11. For $D = d D_0$ the polyhedron is $P_D = \{ m : m_i \geq 0, \ m_1 + \dots + m_n \leq d \}$, the simplex $d \Delta_n$, and the characters $\chi^m = x_1^{m_1} \cdots x_n^{m_n} / x_0^{m_1 + \dots + m_n}$ for $m \in d \Delta_n \cap M$ correspond, after multiplying by $x_0^d$, to the monomials of degree $d$, so Proposition P8.7.3 recovers $\Gamma(\mathbb{P}^n, \mathcal{O}(d))$.

**Example P8.7.6 (the Hirzebruch surfaces).** For the fan of $F_n$ of Example P8.6.20, with rays $u_1 = (1, 0)$, $u_2 = (0, 1)$, $u_3 = (-1, n)$ and $u_4 = (0, -1)$, the divisors are $D_1 = F_0$, $D_2 = C_-$, $D_3 = F_\infty$ and $D_4 = C_+$ in the notation of Theorem P3.11.25. The basis $e_1^*$, $e_2^*$ of $M$ gives
$$\operatorname{div}(\chi^{(1, 0)}) = D_1 - D_3, \qquad \operatorname{div}(\chi^{(0, 1)}) = D_2 + n D_3 - D_4 .$$
So $F_0 \sim F_\infty$, which is the class $F$ of a fibre, and $C_+ \sim C_- + n F$. The rays span $\mathbb{R}^2$, so $\operatorname{Cl}(F_n) \cong \mathbb{Z}^4 / \mathbb{Z}^2 \cong \mathbb{Z}^2$, with basis $[C_-]$ and $[F]$; the quotient is free because the two relations express $D_3$ and $D_4$ in terms of $D_1$ and $D_2$.

**Example P8.7.7 (affine toric surfaces).** Let $d \geq 1$ and $0 \leq k < d$ with $\gcd(d, k) = 1$, and let $\sigma = \operatorname{Cone}(e_2, d e_1 - k e_2)$, with rays $u_1 = e_2$ and $u_2 = d e_1 - k e_2$. Every strongly convex two-dimensional cone in $\mathbb{R}^2$ has this form in a suitable basis of $N$ (Exercise 4), and $U_\sigma$ is the cyclic quotient singularity $\frac{1}{d}(1, k)$ of Example P8.6.9. The map $M \to \mathbb{Z}^2$, $m \mapsto (\langle m, u_1 \rangle, \langle m, u_2 \rangle)$, sends $e_1^* \mapsto (0, d)$ and $e_2^* \mapsto (1, -k)$. In $\operatorname{Cl}(U_\sigma)$ this gives $D_1 \sim k D_2$ and $d D_2 \sim 0$, and the cokernel of the map, with determinant $-d$, has order $d$. So
$$\operatorname{Cl}(U_\sigma) \cong \mathbb{Z}/d, \quad \text{generated by } [D_2],$$
and also by $[D_1] = k [D_2]$, as $\gcd(d, k) = 1$. By Corollary P8.7.11, $\operatorname{Pic}(U_\sigma) = 0$. For $k = 1$, $U_\sigma$ is the cone $xy = z^d$ of Example P8.6.30, and this recovers $\operatorname{Cl} = \mathbb{Z}/d$ and $\operatorname{Pic} = 0$ of Example P3.9.14, with $D_1$ and $D_2$ the two lines through the vertex.

**Example P8.7.8 (the cone over a square).** For the cone $\sigma$ of Example P8.6.10, with rays $u_1 = (0, 0, 1)$, $u_2 = (1, 0, 1)$, $u_3 = (1, 1, 1)$ and $u_4 = (0, 1, 1)$, a form $m = (a, b, c)$ takes the values $c$, $a + c$, $a + b + c$ and $b + c$. The relations are
$$e_1^* \colon D_2 + D_3 \sim 0, \qquad e_2^* \colon D_3 + D_4 \sim 0, \qquad e_3^* \colon D_1 + D_2 + D_3 + D_4 \sim 0 .$$
So $D_4 \sim D_2$ and $D_1 \sim D_3 \sim -D_2$. The $3 \times 3$ minor of the relation matrix in the columns of $D_2$, $D_3$, $D_4$ is $1$, so the cokernel is free and $\operatorname{Cl}(U_\sigma) \cong \mathbb{Z}$, generated by $[D_2]$. In the coordinates $xz = yw$ of Example P8.6.31, $D_1$ is the plane $z = w = 0$, $D_3$ is the plane $x = y = 0$, $D_2$ is $x = w = 0$ and $D_4$ is $y = z = 0$; two planes through the vertex of the cone over a quadric surface, in the same family of planes, are linearly equivalent, and the planes of the other family are their negatives.

### Proof

*Lemma P8.7.2.* (1) The generator $u_\rho$ is primitive, so it is part of a basis $u_\rho = e_1, e_2, \dots, e_n$ of $N$ (a primitive vector of $\mathbb{Z}^n$ can be completed to a basis, by the elementary divisor theorem). With the dual basis $m_1, \dots, m_n$, $S_\rho = \mathbb{Z}_{\geq 0} m_1 \oplus \mathbb{Z} m_2 \oplus \dots \oplus \mathbb{Z} m_n$, so
$$k[S_\rho] = k[x, y_2^{\pm 1}, \dots, y_n^{\pm 1}], \qquad x = \chi^{m_1}, \ y_i = \chi^{m_i}.$$
By Theorem P8.6.25, $O(\rho)$ is the closed subset $V(x)$ of $U_\rho$, which is irreducible of dimension $n - 1$, and $V(\rho) \cap U_\rho = O(\rho)$ because the only cone of $\Sigma$ containing $\rho$ that is a face of $\rho$ is $\rho$. So $D_\rho$ is a prime divisor, its generic point is that of $V(x) \subseteq U_\rho$, and the local ring there is $k[S_\rho]_{(x)}$, a localization of a polynomial ring at a principal prime, which is a discrete valuation ring with uniformizer $x$. If $\langle m_1', u_\rho \rangle = 1$, then $m_1' - m_1 \in u_\rho^\perp$, so $\chi^{m_1'} = x \cdot \chi^{m_1' - m_1}$ with $\chi^{m_1' - m_1}$ a unit of $k[S_\rho]$.

(2) In these coordinates $\chi^m = x^{\langle m, u_\rho \rangle} y_2^{\langle m, e_2 \rangle} \cdots y_n^{\langle m, e_n \rangle}$, and distinct $m$ give distinct monomials. Let $a$ be the minimum of $\langle m, u_\rho \rangle$ over the support of $f$. Then $g = x^{-a} f$ lies in $k[S_\rho]$, and $g$ modulo $x$ is the sum of the terms with $\langle m, u_\rho \rangle = a$, a nonzero Laurent polynomial in the $y_i$. So $x \nmid g$ in the localization, $g$ is a unit of the discrete valuation ring, and $\operatorname{ord}_{D_\rho}(f) = a$.

(3) By Theorem P8.6.25, $X_\Sigma \setminus T_N$ is the union of the orbits $O(\tau)$ with $\tau \neq \{0\}$, and each such $\tau$ has a ray $\rho \preceq \tau$, with $O(\tau) \subseteq V(\rho)$. So $X_\Sigma \setminus T_N = \bigcup_\rho D_\rho$, a finite union of closed irreducible subsets of dimension $n - 1$, and the prime divisors contained in it are these. Distinct rays give disjoint orbits $O(\rho)$, so distinct divisors. The function $\chi^m$ is a unit on $T_N$, so its divisor is supported on $\bigcup_\rho D_\rho$, and the coefficients are given by (2).

*Proposition P8.7.3.* By Definition P3.8.27, a nonzero $f \in k(M)$ is a global section of $\mathcal{O}(D)$ if and only if $\operatorname{div}(f) + D \geq 0$. If so, $f$ has no poles along the prime divisors meeting $T_N$, which are the prime divisors of $T_N$, so $f \in \mathcal{O}(T_N) = k[M]$ by Proposition P3.8.4, and $f = \sum_m c_m \chi^m$. By Lemma P8.7.2, $\operatorname{ord}_{D_\rho}(f) + a_\rho \geq 0$ if and only if $\langle m, u_\rho \rangle \geq -a_\rho$ for every $m$ with $c_m \neq 0$. So $f$ is a section exactly when its support lies in $P_D$. On $U_\sigma$ the same argument applies, as the invariant prime divisors of $U_\sigma$ are the $D_\rho \cap U_\sigma$ for $\rho \in \sigma(1)$.

*Theorem P8.7.4.* By Lemma P8.7.2 (3), the closed set $Z = X_\Sigma \setminus T_N$ has the $D_\rho$ as its irreducible components of codimension one. Theorem P3.8.13 gives the exact sequence $\bigoplus_\rho \mathbb{Z} D_\rho \to \operatorname{Cl}(X_\Sigma) \to \operatorname{Cl}(T_N) \to 0$. The ring $k[M] \cong k[t_1^{\pm 1}, \dots, t_n^{\pm 1}]$ is a localization of a polynomial ring, so it is factorial, and $\operatorname{Cl}(T_N) = 0$ by Proposition P3.8.12. So $\operatorname{Div}_T(X_\Sigma) \to \operatorname{Cl}(X_\Sigma)$ is surjective, and the image of $M$ lies in its kernel. Conversely let $D \in \operatorname{Div}_T(X_\Sigma)$ with $D = \operatorname{div}(f)$. Then $\operatorname{div}(f)$ and $\operatorname{div}(1/f)$ restrict to $0$ on $T_N$, so $f$ is a unit of $k[M]$ by Proposition P3.8.11. A unit of a Laurent polynomial ring over a field is a monomial: order the monomials lexicographically, and note that the product of the highest terms, and of the lowest terms, of $f$ and $f^{-1}$ are the highest and the lowest terms of $1$, so $f$ has one term. So $f = c \chi^m$ with $c \in k^*$, and $D = \operatorname{div}(\chi^m)$. If $\operatorname{div}(\chi^m) = 0$, then $\langle m, u_\rho \rangle = 0$ for all $\rho$, and $m = 0$ when the $u_\rho$ span $N_\mathbb{R}$. The rank is then $|\Sigma(1)| - n$.

### Exercises

1. (A) Compute $\operatorname{Cl}(\mathbb{P}^1 \times \mathbb{P}^1)$ from its fan, and identify the four invariant divisors with fibres of the two projections.
2. (A) Show that for the fan of $\mathbb{A}^n$ the sequence of Theorem P8.7.4 is $0 \to \mathbb{Z}^n \to \mathbb{Z}^n \to 0 \to 0$, and that for the torus $T_N$, whose fan is $\{ 0 \}$, the first map is not injective.
3. (B) For the Hirzebruch surface $F_n$, use Proposition P8.7.3 to show that $h^0(F_n, \mathcal{O}(a C_- + b F)) = \sum_{j = 0}^{a} \max(b - nj + 1, 0)$ for $a, b \geq 0$. Hint: compute $P_D$ for $D = a D_2 + b D_1$.
4. (B) Let $\sigma \subseteq \mathbb{R}^2$ be a strongly convex rational cone of dimension $2$. Show that there is a basis of $N = \mathbb{Z}^2$ in which $\sigma = \operatorname{Cone}(e_2, d e_1 - k e_2)$ with $d \geq 1$, $0 \leq k < d$ and $\gcd(d, k) = 1$, and that $d$ is the index of the sublattice generated by the two ray generators.
5. (B) Let $\Sigma$ be a fan whose rays do not span $N_\mathbb{R}$, with $W$ the span of the rays. Show that $X_\Sigma \cong X_{\Sigma'} \times \mathbb{G}_m^{n - \dim W}$ for a fan $\Sigma'$ in $W$, and compare the class groups.
6. (C) Show that every torus-invariant prime divisor of $X_\Sigma$, meaning a prime divisor stable under the action of $T_N$, is one of the $D_\rho$.

### Lean

The group of torus-invariant divisors with coefficients in $R$ is `MinimalModel.Toric.Fan.TDivisor`, a finitely supported function on the type of rays `MinimalModel.Toric.Fan.Ray`; the set $\Sigma(1)$ is `MinimalModel.Toric.Fan.rays`, the primitive generator $u_\rho$ is `MinimalModel.Toric.Fan.generator`, and $D_\rho$ is `MinimalModel.Toric.Fan.primeDivisor`. These are combinatorial objects: the repository has no scheme $X_\Sigma$, so the divisor of a character, Proposition P8.7.3 and Theorem P8.7.4 are not in Lean.

### Notes and history

The description of the class group of a toric variety by the rays of its fan goes back to Demazure and to Kempf, Knudsen, Mumford and Saint-Donat, and the exact sequence is Cox, Little and Schenck, Theorem 4.1.3, and Fulton, Section 3.4. The sequence is the starting point of Cox's construction of $X_\Sigma$ as a quotient of an open subset of $\mathbb{A}^{\Sigma(1)}$ by the group $\operatorname{Hom}(\operatorname{Cl}(X_\Sigma), \mathbb{G}_m)$, which is Chapter 5 of Cox, Little and Schenck and is not used here.
