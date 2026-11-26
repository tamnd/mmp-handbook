---
title: Cartier divisors and the Picard group
nodes: []
sources: [CLS11, Ful93]
reads_with: [CLS11:ch4, CLS11:ch6, Ful93:3.3, Ful93:3.4]
requires: [P7.4, P8.6, 3.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Cartier divisors and the Picard group

### Statement

**Definition 3.3.11 (Cartier data).** Let $D = \sum_\rho a_\rho D_\rho$ be a torus-invariant divisor on $X_\Sigma$. *Cartier data* for $D$ is a family $\{m_\sigma\}_{\sigma \in \Sigma}$ with $m_\sigma \in M$ and

$$\langle m_\sigma, u_\rho \rangle = -a_\rho \quad \text{for all } \rho \in \sigma(1).$$

Let $\operatorname{CDiv}_T(X_\Sigma) \subset \operatorname{Div}_T(X_\Sigma)$ be the subgroup of the torus-invariant divisors that are Cartier.

Lean: `MinimalModel.Toric.Fan.IsCartier` is the existence of Cartier data, with $\langle m, u \rangle = \sum_i m_i u_i$ on $\mathbb{Z}^n$ and $u_\rho$ = `MinimalModel.Toric.Fan.generator`.

**Theorem 3.3.12 (the Cartier criterion).** A torus-invariant divisor $D$ is Cartier if and only if it has Cartier data. In that case $D|_{U_\sigma} = \operatorname{div}(\chi^{-m_\sigma})|_{U_\sigma}$ for each $\sigma$, the class of $m_\sigma$ modulo $\sigma^\perp \cap M$ is unique, and $m_\sigma - m_\tau \in \tau^\perp$ when $\tau$ is a face of $\sigma$.

Lean: not yet in Lean. The Lean library takes the existence of Cartier data as its definition of a Cartier divisor on the fan, `MinimalModel.Toric.Fan.IsCartier`, so the content of the theorem, the comparison with the Cartier divisors of the scheme $X_\Sigma$, is still open.

**Theorem 3.3.13 (the Picard group).** Every Cartier divisor on $X_\Sigma$ is linearly equivalent to a torus-invariant Cartier divisor, and

$$M \longrightarrow \operatorname{CDiv}_T(X_\Sigma) \longrightarrow \operatorname{Pic}(X_\Sigma) \longrightarrow 0$$

is exact, with the same kernel on the left as in Theorem 3.3.4. So $\operatorname{Pic}(X_\Sigma) \subset \operatorname{Cl}(X_\Sigma)$. Also, $\operatorname{Pic}(U_\sigma) = 0$ for every cone $\sigma$, and $\operatorname{Pic}(X_\Sigma) = \operatorname{Cl}(X_\Sigma)$ when $\Sigma$ is smooth.

Lean: not yet in Lean.

**Proposition 3.3.14 (self-intersections on a smooth toric surface).** Let $\Sigma$ be a smooth fan in $\mathbb{R}^2$, and let $\rho_i$ be a ray that lies in two cones $\operatorname{Cone}(u_{i-1}, u_i)$ and $\operatorname{Cone}(u_i, u_{i+1})$ of $\Sigma$. Then $D_i = D_{\rho_i} \cong \mathbb{P}^1$, there is an integer $b_i$ with $u_{i-1} + u_{i+1} = b_i u_i$, and

$$D_i^2 = -b_i, \qquad D_i \cdot D_{i \pm 1} = 1, \qquad D_i \cdot D_j = 0 \text{ for the other } j \neq i.$$

Lean: not yet in Lean.

### Proof in words

On the affine chart $U_\sigma$, a divisor $\operatorname{div}(\chi^{-m})$ has the coefficient $-\langle m, u_\rho \rangle$ along $D_\rho$. So Cartier data says that $D$ is principal on each chart, given by a character, which makes $D$ Cartier. The converse needs that a Cartier divisor that is invariant under the torus is given on $U_\sigma$ by one character. The reason is that $U_\sigma$ has the fixed orbit $O(\sigma)$ in the closure of every other orbit. A local equation at $\gamma_\sigma$ can be chosen to be an eigenvector of the torus, so a character, and the set where a character is a local equation is open and invariant, so it is all of $U_\sigma$.

For a smooth surface, the intersection number $D_i \cdot D_j$ of two neighbours is $1$, since they are the two coordinate axes of the chart of their common cone. For $D_i^2$, move $D_i$ by a character: pick $m$ with $\langle m, u_i \rangle = 1$, intersect $\operatorname{div}(\chi^m) = 0$ in $\operatorname{Pic}$ with $D_i$, and use the relation $u_{i-1} + u_{i+1} = b_i u_i$.

### Examples

**Example 3.3.15 (projective space and the Hirzebruch surface).** On $\mathbb{P}^n$ the divisor $D_0$ has the Cartier data $m_{\sigma_i} = e_i^*$ on the cone $\sigma_i$ that omits $u_i$ (for $i \ge 1$), since $\langle e_i^*, u_0 \rangle = -1$ and $\langle e_i^*, u_j \rangle = 0$ for $j \neq 0, i$, and $m_{\sigma_0} = 0$. On $\{x_i \neq 0\}$ the local equation $\chi^{-e_i^*} = x_0 / x_i$ cuts out $D_0 = \{x_0 = 0\}$. Both $\mathbb{P}^n$ and $\mathbb{F}_n$ are smooth, so $\operatorname{Pic}(\mathbb{P}^n) = \operatorname{Cl}(\mathbb{P}^n) = \mathbb{Z}$ and $\operatorname{Pic}(\mathbb{F}_n) = \mathbb{Z}^2$. On $\mathbb{F}_n$, Proposition 3.3.14 and the relations $u_1 + u_3 = n u_2$, $u_2 + u_4 = 0 \cdot u_1 = 0 \cdot u_3$, $u_3 + u_1 = -n u_4$ give

$$D_2^2 = -n, \qquad D_4^2 = n, \qquad D_1^2 = D_3^2 = 0.$$

So $D_2$ is the negative section, $D_4$ is a positive section, and $D_1$, $D_3$ are fibres. On $\mathbb{P}^2$, $u_0 + u_2 = -u_1$, so $D_1^2 = 1$, the self-intersection of a line.

**Example 3.3.16 (the quadric cone and $\frac1n(1,1)$).** On $U_{\sigma_n}$, the divisor $a D_1$ is Cartier if and only if there is $m = (c, d) \in \mathbb{Z}^2$ with $\langle m, e_2 \rangle = d = -a$ and $\langle m, n e_1 - e_2 \rangle = nc - d = 0$. This means $nc = -a$, so $a D_1$ is Cartier exactly when $n \mid a$. So $D_1$ is a Weil divisor that is not Cartier, $n D_1 = \operatorname{div}(\chi^{(1, n)})$ is Cartier, and $\operatorname{Pic}(U_{\sigma_n}) = 0$ inside $\operatorname{Cl}(U_{\sigma_n}) = \mathbb{Z}/n$. For the quadric cone, the line $y = z = 0$ is not Cartier, and twice it is the divisor of $z$.

**Example 3.3.17 (the weighted projective plane).** On $\mathbb{P}(1,1,n)$ the cones $\operatorname{Cone}(u_3, u_4)$ and $\operatorname{Cone}(u_4, u_1)$ are smooth, so the only condition is on $\sigma = \operatorname{Cone}(u_1, u_3)$. The divisor $a D_1$ is Cartier on $U_\sigma$ if and only if there is $m = (c, d)$ with $\langle m, u_1 \rangle = c = -a$ and $\langle m, u_3 \rangle = -c + nd = 0$, so if and only if $n \mid a$. The divisor $D_4$ is Cartier on $U_\sigma$ with $m_\sigma = 0$, since its coefficients on $u_1$ and $u_3$ are zero. So with $D_0 = [D_1]$,

$$\operatorname{Pic}(\mathbb{P}(1,1,n)) = n \mathbb{Z} D_0 \subset \operatorname{Cl}(\mathbb{P}(1,1,n)) = \mathbb{Z} D_0,$$

generated by $[D_4] = n D_0$. The curve $D_4$ misses the singular point, which is why it is Cartier.

**Example 3.3.18 (a divisor with no Cartier multiple).** On the cone over a square, let $a D_1$ be Cartier on $U_\sigma$. Then there is $m \in M$ with $\langle m, u_1 \rangle = -a$ and $\langle m, u_2 \rangle = \langle m, u_3 \rangle = \langle m, u_4 \rangle = 0$. The vectors $u_2, u_3, u_4$ span $\mathbb{R}^3$, so $m = 0$ and $a = 0$. So no nonzero multiple of the plane $D_1 = \{z = w = 0\}$ is Cartier, and $\operatorname{Pic}(U_\sigma) = 0$ inside $\operatorname{Cl}(U_\sigma) = \mathbb{Z}$.

### Proof

*Proof of Theorem 3.3.12.* By Theorem 3.2.29, $D_\rho$ meets $U_\sigma$ if and only if $\rho \in \sigma(1)$. Suppose that $D$ has Cartier data. By Proposition 3.3.3, $\operatorname{div}(\chi^{-m_\sigma})|_{U_\sigma} = \sum_{\rho \in \sigma(1)} -\langle m_\sigma, u_\rho \rangle D_\rho|_{U_\sigma} = D|_{U_\sigma}$. So $D$ is principal on each $U_\sigma$, and it is Cartier.

The converse is sketched, after Cox-Little-Schenck, Chapter 4. Let $D$ be Cartier. The module $\Gamma(U_\sigma, \mathcal{O}(D)) = \{f : \operatorname{div}(f) + D \ge 0 \text{ on } U_\sigma\}$ is graded by $M$, because $D$ is invariant: it is spanned by the $\chi^m$ with $\langle m, u_\rho \rangle + a_\rho \ge 0$ for $\rho \in \sigma(1)$. Since $D$ is Cartier, the stalk of $\mathcal{O}(D)$ at $\gamma_\sigma$ is free of rank one over the local ring, and the graded form of Nakayama's lemma gives a homogeneous generator $\chi^{-m}$. The set of points where $\chi^{-m}$ generates $\mathcal{O}(D)$ is open, contains $\gamma_\sigma$ and is invariant under $T_N$. Every orbit of $U_\sigma$ contains $\gamma_\sigma$ in its closure (Theorem 3.2.29, part 4), so this set is $U_\sigma$. Hence $D|_{U_\sigma} = \operatorname{div}(\chi^{-m})|_{U_\sigma}$, and $m_\sigma = m$ is Cartier data on $\sigma$.

If $m$ and $m'$ both work on $\sigma$, then $\langle m - m', u_\rho \rangle = 0$ for $\rho \in \sigma(1)$, so $m - m' \in \sigma^\perp$. If $\tau$ is a face of $\sigma$, then $m_\sigma$ is also Cartier data on $\tau$, so $m_\sigma - m_\tau \in \tau^\perp$. $\square$

*Proof of Theorem 3.3.13.* Let $D$ be a Cartier divisor. By Theorem 3.3.4 there is $f$ with $D + \operatorname{div}(f)$ torus-invariant, and $D + \operatorname{div}(f)$ is Cartier. Two torus-invariant Cartier divisors are linearly equivalent if and only if they differ by some $\operatorname{div}(f)$, and as in the proof of Theorem 3.3.4 such an $f$ is $c \chi^m$. So $\operatorname{Pic}(X_\Sigma) = \operatorname{CDiv}_T(X_\Sigma) / \{\operatorname{div}(\chi^m)\}$, which is the exact sequence, and it embeds in $\operatorname{Cl}(X_\Sigma)$. On $U_\sigma$, Theorem 3.3.12 says that every torus-invariant Cartier divisor is $\operatorname{div}(\chi^{-m_\sigma})$, so $\operatorname{Pic}(U_\sigma) = 0$. If $\Sigma$ is smooth, the $u_\rho$ for $\rho \in \sigma(1)$ are part of a basis of $N$, so the equations $\langle m_\sigma, u_\rho \rangle = -a_\rho$ have an integer solution for every $D$, and every $D$ is Cartier. $\square$

*Proof of Proposition 3.3.14.* The star of $\rho_i$ in $N / \mathbb{Z} u_i \cong \mathbb{Z}$ has two rays, the images of $u_{i-1}$ and $u_{i+1}$, which point in opposite directions. So $D_i \cong \mathbb{P}^1$ by Theorem 3.2.29, part 5, and it is a complete curve. Since both cones are smooth with the same orientation, $\det(u_{i-1}, u_i) = \det(u_i, u_{i+1}) = \pm 1$, and as in the proof of Proposition 3.1.30, part 3, $u_{i-1} + u_{i+1} = b_i u_i$ with $b_i \in \mathbb{Z}$. On the chart of $\operatorname{Cone}(u_i, u_{i+1}) \cong \mathbb{A}^2$, $D_i$ and $D_{i+1}$ are the two coordinate axes, which meet transversally in one point, so $D_i \cdot D_{i+1} = 1$, and the same for $D_{i-1}$. For any other $j \neq i$, no cone contains both $\rho_i$ and $\rho_j$, so $D_i \cap D_j = \emptyset$ by Theorem 3.2.29, part 4, and $D_i \cdot D_j = 0$. Now pick $m \in M$ with $\langle m, u_i \rangle = 1$, which exists since $u_i$ is primitive. Since $\operatorname{div}(\chi^m)$ is principal and $D_i$ is complete,

$$0 = \operatorname{div}(\chi^m) \cdot D_i = \langle m, u_{i-1} \rangle + \langle m, u_i \rangle D_i^2 + \langle m, u_{i+1} \rangle = \langle m, b_i u_i \rangle + D_i^2 = b_i + D_i^2. \qquad \square$$

### Exercises

1. (A) Let $\Sigma$ be the fan with the six rays $e_1$, $e_1 + e_2$, $e_2$, $-e_1$, $-e_1 - e_2$, $-e_2$ and the six cones between consecutive rays. Show that every $D_i^2 = -1$.
2. (A) Find Cartier data for $D_4$ on $\mathbb{F}_n$, and check that the data on two adjacent cones differ by an element of the common face's $\tau^\perp$.
3. (B) Let $\Sigma$ be a smooth complete fan in $\mathbb{R}^2$ with $r$ rays. Show that $\sum_i D_i^2 = 12 - 3r$.
4. (B) Let $\sigma = \operatorname{Cone}(e_2, n e_1 - q e_2)$ with $\gcd(n, q) = 1$, and let $X \to U_\sigma$ be its minimal resolution (Proposition 3.1.30). Show that the exceptional curves $E_1, \dots, E_s$ have $E_i^2 = -b_i \le -2$.
5. (C) Show that a torus-invariant divisor on a complete $X_\Sigma$ is Cartier if and only if there is a continuous function $\varphi \colon N_{\mathbb{R}} \to \mathbb{R}$, linear on each cone and integral on $N$, with $\varphi(u_\rho) = -a_\rho$ for all $\rho$.

### Lean

- Status: the Lean library has torus-invariant divisors on a fan (`MinimalModel.Toric.Fan.TDivisor`), the existence of Cartier data (`MinimalModel.Toric.Fan.IsCartier`) and its real form (`MinimalModel.Toric.Fan.IsRCartier`). It has support functions, `MinimalModel.Toric.Fan.IsSupportFunction` and `MinimalModel.Toric.Fan.IsSupportFunctionOf`, which are the functions $\varphi$ of Exercise 5, and `MinimalModel.Toric.Fan.IsSupportFunctionOf.isRCartier` turns a support function into real Cartier data. Theorem 3.3.12, the Picard group and intersection numbers are not yet in Lean.
- Fidelity: in Lean the dual lattice $M$ is $\mathbb{Z}^n$ with the pairing $\sum_i m_i u_i$, and the sign is the one of Definition 3.3.11, $\langle m_\sigma, u_\rho \rangle = -a_\rho$. `MinimalModel.Toric.Fan.IsCartier` is a definition on the fan; Theorem 3.3.12 is what makes it agree with the Cartier property on $X_\Sigma$.
- No node of the map covers this section.

### Notes and history

The Cartier criterion and the description of $\operatorname{Pic}$ are in Kempf, Knudsen, Mumford and Saint-Donat (1973) and in Fulton's book, Chapter 3. The function $\varphi$ of Exercise 5 is the support function of $D$. Cox-Little-Schenck, Chapter 6, shows that $D$ is ample if and only if $\varphi$ is strictly convex, and nef if and only if $\varphi$ is convex; the toric cone theorem of the later chapters of this volume starts from this. The formula of Exercise 3 is the toric case of Noether's formula $12 \chi(\mathcal{O}) = K^2 + e$.
