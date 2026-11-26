---
title: Discrepancies of toric divisors
nodes: []
sources: [CLS11, Rei83, KM98, FS04]
reads_with: [CLS11:ch11, KM98:ch2]
requires: [P8.6, 3.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Discrepancies of toric divisors

### Statement

Let $\Sigma$ be a fan with $K_{X_\Sigma}$ $\mathbb{Q}$-Cartier, and let $m_\sigma \in M_{\mathbb{Q}}$ be the data of Corollary 3.3.27, with $\langle m_\sigma, u_\rho \rangle = 1$ for $\rho \in \sigma(1)$. Write $\psi_K$ for the function on $|\Sigma|$ that is $\langle m_\sigma, \cdot \rangle$ on each cone $\sigma$. It is well defined, since $m_\sigma$ and $m_{\sigma'}$ take the same values on the rays of $\sigma \cap \sigma'$ and so on all of $\sigma \cap \sigma'$.

**Definition 3.3.33 (toric discrepancy).** For a primitive vector $v \in |\Sigma| \cap N$, the *discrepancy* of $v$ over $X_\Sigma$ is

$$a(v) = \psi_K(v) - 1 = \langle m_\sigma, v \rangle - 1 \quad \text{for any } \sigma \in \Sigma \text{ with } v \in \sigma.$$

**Theorem 3.3.34 (the discrepancy formula).** Let $\Sigma'$ be a refinement of $\Sigma$ and $f \colon X_{\Sigma'} \to X_\Sigma$ the toric morphism of Corollary 3.2.39. If $K_{X_\Sigma}$ is $\mathbb{Q}$-Cartier, then

$$K_{X_{\Sigma'}} = f^* K_{X_\Sigma} + \sum_{\rho' \in \Sigma'(1) \setminus \Sigma(1)} a(u_{\rho'}) \, D_{\rho'}.$$

So the discrepancy $a(D_{\rho'}, X_\Sigma)$ in the sense of Kollár-Mori, Chapter 2, of the exceptional divisor $D_{\rho'}$ is $a(u_{\rho'}) = \langle m_\sigma, u_{\rho'} \rangle - 1$.

Lean: not yet in Lean.

**Proposition 3.3.35 (discrepancies on a simplicial cone).** Let $\sigma = \operatorname{Cone}(u_1, \dots, u_d)$ be simplicial and $v = \sum_i \lambda_i u_i$ with all $\lambda_i \ge 0$. Then $\langle m_\sigma, v \rangle = \sum_i \lambda_i$, and $a(v) = \lambda_1 + \dots + \lambda_d - 1$.

Lean: not yet in Lean.

**Theorem 3.3.36 (canonical and terminal toric singularities).** Let $K_{X_\Sigma}$ be $\mathbb{Q}$-Cartier. Then:

1. $X_\Sigma$ is klt.
2. $X_\Sigma$ is canonical if and only if $\langle m_\sigma, v \rangle \ge 1$ for every $\sigma \in \Sigma$ and every $v \in \sigma \cap N$, $v \neq 0$.
3. $X_\Sigma$ is terminal if and only if $\langle m_\sigma, v \rangle > 1$ for every $\sigma \in \Sigma$ and every $v \in \sigma \cap N$ other than $0$ and the minimal generators $u_\rho$, $\rho \in \sigma(1)$.

Lean: not yet in Lean.

This theorem is cited from Reid (1983) and Cox-Little-Schenck, Chapter 11. Later chapters of this volume return to it. The point is that a smooth refinement is a log resolution whose exceptional divisors are all toric, so the toric discrepancies $a(v)$ already decide the class of the singularity. In words: for canonical, the set $\{v \in |\Sigma| : \psi_K(v) < 1\}$ contains no lattice point other than $0$; for terminal, the set $\{\psi_K \le 1\}$ contains no lattice points other than $0$ and the $u_\rho$.

### Proof in words

On $U_\sigma$, some multiple $rK_{X_\Sigma}$ is the divisor of the character $\chi^{-r m_\sigma}$. The morphism $f$ is the identity on the torus, so $f^*(rK)$ is the divisor of the same character on $f^{-1}(U_\sigma)$. That divisor is $-\sum_{\rho'} \langle r m_\sigma, u_{\rho'} \rangle D_{\rho'}$, a sum over all rays of $\Sigma'$ in $\sigma$. The canonical divisor of $X_{\Sigma'}$ is $-\sum_{\rho'} D_{\rho'}$, so the difference has coefficient $\langle m_\sigma, u_{\rho'} \rangle - 1$ on each $D_{\rho'}$. On the old rays this is $0$.

### Examples

**Example 3.3.37 (the blow-up of a point).** Let $\sigma = \operatorname{Cone}(e_1, \dots, e_n)$, so $m_\sigma = (1, \dots, 1)$. The star subdivision at $v = e_1 + \dots + e_n$ is the blow-up of the origin of $\mathbb{A}^n$ (Chapter 2, Section 5), and $a(v) = n - 1$. This is the classical formula $K_{\mathrm{Bl}} = f^* K_{\mathbb{A}^n} + (n - 1) E$. The star subdivision at $e_1 + e_2$ is the blow-up of the codimension 2 plane $\{x_1 = x_2 = 0\}$, with $a = 1$.

**Example 3.3.38 (the cones $\sigma_n$).** On $\sigma_n = \operatorname{Cone}(e_2, n e_1 - e_2)$, Example 3.3.30 gives $m_{\sigma_n} = (2/n, 1)$. The minimal resolution adds the one ray $e_1 = \frac1n e_2 + \frac1n (n e_1 - e_2)$ (Example 3.1.31). So

$$a(e_1) = \tfrac{2}{n} - 1 = -\tfrac{n-2}{n}.$$

Check by adjunction: the exceptional curve $E \cong \mathbb{P}^1$ has $E^2 = -n$ (Example 3.3.16), so $K_{X'} \cdot E = -2 - E^2 = n - 2$. Since $f^* K \cdot E = 0$, the coefficient $a$ satisfies $a E^2 = n - 2$, and $a = -(n-2)/n$. For $n = 1$ the cone is smooth and $a = 1$, the blow-up of a smooth point. For $n = 2$, the quadric cone, $a = 0$: the resolution is crepant, and the quadric cone is canonical but not terminal. For $n = 3$, $a = -\frac13$, and $U_{\sigma_3}$ is klt but not canonical.

**Example 3.3.39 (the cone over a square).** With $m_\sigma = (0, 0, 1)$ (Example 3.3.31), $\psi_K(x, y, z) = z$. The two small resolutions $X_{\Sigma_\pm}$ add no ray, so $K_{X_{\Sigma_\pm}} = f^* K$: both are crepant. The star subdivision at $w = (1, 1, 2)$ has $a(w) = 2 - 1 = 1$. The lattice points of $\sigma$ at height $z = 1$ are the four vertices $u_1, \dots, u_4$ of the unit square, and every other nonzero lattice point of $\sigma$ has $z \ge 2$. So by Theorem 3.3.36 the cone $xz = yw$ is terminal, though it is not $\mathbb{Q}$-factorial (Example 3.3.23).

**Example 3.3.40 (the quotients $\frac1n(1, \dots, 1)$).** Let $N = \mathbb{Z}^d + \mathbb{Z} \cdot \frac1n (1, \dots, 1)$ and $\sigma = \operatorname{Cone}(e_1, \dots, e_d)$, so $U_\sigma = \mathbb{A}^d / \mu_n$ with $\mu_n$ acting by scalars. The minimal generators are $e_1, \dots, e_d$, so $m_\sigma = (1, \dots, 1)$ and, by Proposition 3.3.35, $\langle m_\sigma, v \rangle = v_1 + \dots + v_d$. The lattice points of $\sigma$ other than $0$ and the $e_i$ are the points $\frac{k}{n}(1, \dots, 1) + w$ with $1 \le k \le n - 1$ and $w \in \mathbb{Z}^d_{\ge 0}$, and the integer points $w \neq 0$ other than the $e_i$. The least value of $\psi_K$ among them is $d/n$, at $v = \frac1n (1, \dots, 1)$, when $d < 2n$. So:

- for $d = 2$ this is $\sigma_n$ again, with $a(v) = \frac2n - 1$;
- for $d = 3$ and $n = 2$, the point $\frac12(1,1,1)$ of Example 3.3.24 has $a(v) = \frac12$, and $U_\sigma$ is terminal;
- for $d = n = 3$, $a(v) = 0$, and $U_\sigma$ is canonical but not terminal.

In each case the star subdivision at $v$ is a resolution with exceptional divisor $\mathbb{P}^{d-1}$, the total space of $\mathcal{O}_{\mathbb{P}^{d-1}}(-n)$, and its discrepancy is $\frac{d}{n} - 1$.

### Proof

*Proof of Theorem 3.3.34.* Choose $r \ge 1$ with $r K_{X_\Sigma}$ Cartier, so that $r m_\sigma \in M$ can be chosen for each $\sigma$ (part 3 of Corollary 3.3.27; change $r m_\sigma$ by an element of $\sigma^\perp$ if needed). On $U_\sigma$, $r K_{X_\Sigma} = \operatorname{div}(\chi^{-r m_\sigma})$ by Theorem 3.3.12. The preimage $f^{-1}(U_\sigma)$ is the toric variety of the fan $\Sigma'_\sigma = \{\sigma' \in \Sigma' : \sigma' \subseteq \sigma\}$, by the construction of $f$ in Chapter 2, Section 5. The morphism $f$ restricts to the identity of $T_N$, so $f^* \chi^m = \chi^m$ as rational functions, and the pullback of a principal Cartier divisor is the divisor of the pulled back function. By Proposition 3.3.3 applied on $X_{\Sigma'_\sigma}$,

$$f^*(rK_{X_\Sigma})|_{f^{-1}(U_\sigma)} = \operatorname{div}(\chi^{-r m_\sigma}) = -\sum_{\rho' \in \Sigma'_\sigma(1)} \langle r m_\sigma, u_{\rho'} \rangle D_{\rho'}.$$

Divide by $r$. Theorem 3.3.26 gives $K_{X_{\Sigma'}} = -\sum_{\rho'} D_{\rho'}$, so on $f^{-1}(U_\sigma)$

$$K_{X_{\Sigma'}} - f^* K_{X_\Sigma} = \sum_{\rho' \in \Sigma'_\sigma(1)} (\langle m_\sigma, u_{\rho'} \rangle - 1) D_{\rho'}.$$

If $\rho' \in \Sigma(1)$, then $u_{\rho'}$ is a minimal generator of a ray of $\sigma$ and the coefficient is $0$. The sets $f^{-1}(U_\sigma)$ cover $X_{\Sigma'}$, and the coefficient of $D_{\rho'}$ does not depend on the cone $\sigma \ni u_{\rho'}$, by the remark before Definition 3.3.33. $\square$

*Proof of Proposition 3.3.35.* The form $m_\sigma$ is linear and takes the value 1 at each $u_i$. $\square$

*On Theorem 3.3.36.* Part 1 follows from the formula once a log resolution is known to be toric: $m_\sigma$ is positive on the generators of $\sigma$, so $\langle m_\sigma, v \rangle > 0$ and $a(v) > -1$ for every $v \in \sigma \cap N$, $v \neq 0$. Parts 2 and 3 compare the discrepancies of all divisors over $X_\Sigma$ with those of toric divisors. The full argument is in Cox-Little-Schenck, Chapter 11, and in Reid (1983).

### Exercises

1. (A) Use Theorem 3.3.34 to compute the discrepancy of the blow-up of $\mathbb{A}^3$ along a coordinate axis, and compare it with Example 3.3.37.
2. (B) Find all $n$ and $q$ with $\gcd(n, q) = 1$ such that the cone of $\frac1n(1, q)$ is canonical. Show that the answer is $q \equiv -1 \pmod n$, the $A_{n-1}$ singularities.
3. (B) Show that a 2-dimensional toric singularity is terminal only if it is smooth. (Hint: if $\sigma = \operatorname{Cone}(u_1, u_2)$ is not smooth, there is a lattice point $v = \lambda_1 u_1 + \lambda_2 u_2$ with $0 \le \lambda_i < 1$ and $v \neq 0$. Then $u_1 + u_2 - v$ is also one, and one of the two has $\lambda_1 + \lambda_2 \le 1$.)
4. (B) Let $P \subset \mathbb{R}^2$ be a lattice polygon and $\sigma \subset \mathbb{R}^3$ the cone over $P \times \{1\}$. Show that $U_\sigma$ is Gorenstein and canonical, and that it is terminal if and only if the only lattice points of $P$ are its vertices.
5. (C) Use Exercise 4 and the fact that a convex lattice pentagon has an interior lattice point to show that, up to $\mathrm{GL}_3(\mathbb{Z})$, the only Gorenstein terminal affine toric 3-folds $U_\sigma$ with $\dim \sigma = 3$ are $\mathbb{A}^3$ and the cone over a square. (Use Pick's formula for the case of four vertices.)

### Lean

- Status: not yet in Lean. The Lean library has the toric canonical divisor on a fan (`MinimalModel.Toric.Fan.canonical`), its real form (`MinimalModel.Toric.Fan.canonicalReal`), and the rational Cartier data of Theorem 3.3.20 (`MinimalModel.Toric.Fan.isQCartier_iff`), which gives the vectors $m_\sigma$ when $K$ is $\mathbb{Q}$-Cartier. It has no refinements, no toric morphisms and no discrepancies yet.
- Fidelity: in Lean the vectors $m_\sigma$ appear as rational vectors in $\mathbb{Q}^n$ for each cone, with the sign convention $\langle m_\sigma, u_\rho \rangle = -a_\rho$; for the canonical divisor $a_\rho = -1$, which gives $\langle m_\sigma, u_\rho \rangle = 1$ as here.
- No node of the map covers this section.

### Notes and history

The formula $a(v) = \langle m_\sigma, v \rangle - 1$ and the criteria of Theorem 3.3.36 are in Reid's paper on the toric MMP (1983), and they go back to his work on canonical 3-folds. Cox-Little-Schenck, Chapter 11, gives a textbook proof. Example 3.3.40 for $d = 3$, $n = 2$ is the simplest terminal quotient singularity. The terminal cyclic quotient 3-fold singularities are the $\frac1r(1, -1, a)$ with $\gcd(a, r) = 1$, by White's theorem on lattice tetrahedra with no other lattice points and the work of Morrison and Stevens (1984). This extends Exercise 5 beyond the Gorenstein case.
