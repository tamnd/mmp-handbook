---
title: Three cones computed with rational curves
nodes: []
sources: [KM98, Deb01, Mor82]
reads_with: [KM98:1.3, Deb01:ch6]
requires: [1.5, P7.3, P7.4, 6.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Three cones computed with rational curves

### Statement

This section computes the cone of curves, the extremal rays, their lengths and the minimal rational curves on three varieties, and checks each against Theorem 6.2.9. On $\mathbb{P}^a \times \mathbb{P}^b$ write $H_1$, $H_2$ for the pullbacks of $\mathcal{O}(1)$ and $\ell_1$, $\ell_2$ for a line in $\mathbb{P}^a \times \{ y \}$ and a line in $\{ x \} \times \mathbb{P}^b$, as in Example P7.3.15, so $H_i \cdot \ell_j = \delta_{ij}$. On a blow-up $\pi \colon X \to \mathbb{P}^n$ at points $p_i$, $n \ge 2$, write $H = \pi^* \mathcal{O}(1)$, $E_i$ for the exceptional divisors, $e_i$ for a line in $E_i \cong \mathbb{P}^{n-1}$ and $\ell$ for the pullback of a general line, so that $H \cdot \ell = 1$, $H \cdot e_i = 0$, $E_i \cdot \ell = 0$ and $E_i \cdot e_j = -\delta_{ij}$, and $K_X = -(n + 1) H + (n - 1) \sum_i E_i$ by Example 1.5.15.

**Proposition 6.2.16 (the cone of $\mathbb{P}^1 \times \mathbb{P}^2$).** Let $X = \mathbb{P}^1 \times \mathbb{P}^2$, with projections $p_1$, $p_2$.

1. $-K_X = 2 H_1 + 3 H_2$, and $\overline{NE}(X) = \langle [\ell_1], [\ell_2] \rangle$ has two extremal rays, both $K_X$-negative, with $-K_X \cdot \ell_1 = 2$ and $-K_X \cdot \ell_2 = 3$.
2. The set $\mathcal{R}$ of Definition 6.2.3 consists of the fibres $\ell_1$ of $p_2$ and the lines $\ell_2$ in the fibres of $p_1$. The ray $\mathbb{R}_{\ge 0} [\ell_1]$ has length $2$ and is the face of $p_2$; the ray $\mathbb{R}_{\ge 0} [\ell_2]$ has length $3$ and is the face of $p_1$.
3. A rational curve of class $[\ell_1] + [\ell_2]$ has $-K_X$-degree $5 = n + 2$, and it breaks into $\ell_1 + \ell_2$.

Lean: not yet in Lean.

**Proposition 6.2.17 (the blow-up of $\mathbb{P}^n$ at a point).** Let $X = \operatorname{Bl}_p \mathbb{P}^n$ with $n \ge 2$, $E = E_1$, $e = e_1$, and $\tilde\ell$ the strict transform of a line through $p$, so $[\tilde\ell] = [\ell] - [e]$.

1. $\overline{NE}(X) = \langle [e], [\tilde\ell] \rangle$, with $-K_X \cdot e = n - 1$ and $-K_X \cdot \tilde\ell = 2$, so $X$ is Fano.
2. The ray $\mathbb{R}_{\ge 0} [e]$ has length $n - 1$, equal to the discrepancy $a(E, \mathbb{P}^n) = n - 1$, and its contraction is $\pi$. The ray $\mathbb{R}_{\ge 0} [\tilde\ell]$ has length $2$, and its contraction is the projection $q \colon X \to \mathbb{P}^{n-1}$ from $p$, a $\mathbb{P}^1$-bundle.

Lean: not yet in Lean.

**Proposition 6.2.18 (the blow-up of $\mathbb{P}^n$ at two points).** Let $X = \operatorname{Bl}_{p_1, p_2} \mathbb{P}^n$ with $n \ge 2$, and $\ell_{12}$ the strict transform of the line through $p_1$ and $p_2$, so $[\ell_{12}] = [\ell] - [e_1] - [e_2]$.

1. $\overline{NE}(X) = \langle [e_1], [e_2], [\ell_{12}] \rangle$ and $\operatorname{Nef}(X) = \langle H, H - E_1, H - E_2 \rangle$, two simplicial cones in dual bases.
2. $-K_X \cdot e_i = n - 1$ and $K_X \cdot \ell_{12} = n - 3$. So the ray of $\ell_{12}$ is $K_X$-negative for $n = 2$, $K_X$-trivial for $n = 3$ and $K_X$-positive for $n \ge 4$, and $X$ is Fano only for $n = 2$.
3. $N_{\ell_{12}/X} \cong \mathcal{O}(-1)^{\oplus (n - 1)}$.
4. The divisor $2H - E_1 - E_2$ is base point free, and its morphism contracts $\ell_{12}$ and no other curve.

Lean: not yet in Lean.

### Proof in words

In each case the cone is squeezed between the cone spanned by explicit curves and the dual of the cone spanned by explicit base point free divisors; when the two are dual simplicial cones, both are the answer. The anticanonical degrees follow from the formula for $K_X$, and the lengths from the observation that a curve whose class lies on a ray is contracted by the morphism that the ray's supporting divisor defines, so it lies in a fibre, and the fibres are known. The normal bundle of $\ell_{12}$ is the normal bundle $\mathcal{O}(1)^{\oplus (n-1)}$ of a line, twisted down once at each of the two blown-up points.

### Examples

**Example 6.2.19 (the del Pezzo surface of degree $7$).** For $n = 2$, Proposition 6.2.18 is Proposition P7.4.20: the three $(-1)$-curves $e_1$, $e_2$, $\ell_{12}$ span the cone, each of length $1$, and $X$ is a del Pezzo surface. The contraction of $\ell_{12}$ is the morphism to $\mathbb{P}^1 \times \mathbb{P}^1$ given by the two projections from $p_1$ and $p_2$.

**Example 6.2.20 (a flopping curve).** For $n = 3$, $\ell_{12}$ is a smooth rational curve with normal bundle $\mathcal{O}(-1) \oplus \mathcal{O}(-1)$ and $K_X \cdot \ell_{12} = 0$, the local picture of the Atiyah flop. Theorem 6.2.9 says nothing about this ray: it lies in $\overline{NE}(X)_{K_X \ge 0}$, which here is exactly the ray of $\ell_{12}$, and the decomposition reads $\overline{NE}(X) = \mathbb{R}_{\ge 0}[\ell_{12}] + \mathbb{R}_{\ge 0} [e_1] + \mathbb{R}_{\ge 0} [e_2]$.

**Example 6.2.21 (a breaking in $\mathbb{P}^1 \times \mathbb{P}^2$).** Let $L \subseteq \mathbb{P}^2$ be a line. The curves of class $[\ell_1] + [\ell_2]$ in $\mathbb{P}^1 \times L \cong \mathbb{P}^1 \times \mathbb{P}^1$ are the members of $|\mathcal{O}(1, 1)| \cong \mathbb{P}^3$, and those through two fixed general points form a pencil. The pencil contains reducible members, the union of the fibre of each projection through one of the two points, and this is the breaking $[\ell_1] + [\ell_2]$ of part 3 of Proposition 6.2.16.

### Proof

*Proposition 6.2.16.* By Example P7.3.15, $\overline{NE}(X) = \langle [\ell_1], [\ell_2] \rangle$. The canonical class is $K_X = p_1^* K_{\mathbb{P}^1} + p_2^* K_{\mathbb{P}^2} = -2 H_1 - 3 H_2$, so $-K_X \cdot \ell_1 = 2$ and $-K_X \cdot \ell_2 = 3$. An integral curve $C$ has class $a [\ell_1] + b [\ell_2]$ with $a = H_1 \cdot C$ and $b = H_2 \cdot C$ nonnegative, and $-K_X \cdot C = 2a + 3b$. If $C \in \mathcal{R}$, then $2a + 3b \le 4$, so $(a, b) \in \{ (1, 0), (2, 0), (0, 1) \}$. If $b = 0$, $C$ is contracted by $p_2$, so it is a fibre $\mathbb{P}^1 \times \{ y \}$ and $a = 1$. If $a = 0$, $C$ lies in a fibre $\{ x \} \times \mathbb{P}^2$ and has degree $b = 1$ there, so it is a line. The same argument shows that the integral curves with class on the ray of $\ell_1$, respectively $\ell_2$, are the fibres of $p_2$, respectively curves in the fibres of $p_1$, which gives the lengths $2$ and $3$ and identifies the faces, as in Example P7.4.17. For part 3, $-K_X \cdot (\ell_1 + \ell_2) = 5 = n + 2$, so Corollary 6.1.4 applies, and Example 6.2.21 exhibits the breaking.

*Proposition 6.2.17.* This is Proposition P7.4.18 for the cone. With $K_X = -(n + 1) H + (n - 1) E$, $-K_X \cdot e = (n - 1)(-E \cdot e) = n - 1$ and $-K_X \cdot \tilde\ell = (n + 1) - (n - 1) E \cdot \tilde\ell = 2$, since $E \cdot \tilde\ell = E \cdot \ell - E \cdot e = 1$. Both rays are $K_X$-negative and $\overline{NE}(X)$ is spanned by them, so $-K_X$ is ample by Kleiman's criterion, Theorem P7.3.13. A curve with class on the ray of $e$ has $H \cdot C = 0$, so it lies in $E \cong \mathbb{P}^{n-1}$, with class $d [e]$ for its degree $d$ there, and the least degree $-K_X \cdot C = d (n - 1)$ is $n - 1$, attained by lines. The face of $\pi$ is this ray by Proposition P7.4.11. A curve with class on the ray of $\tilde\ell$ has $(H - E) \cdot C = 0$, so it is contracted by $q$, whose fibres are the lines $\tilde\ell$, and the length is $2$. The discrepancy of $E$ over $\mathbb{P}^n$ is $n - 1$ by Example 1.5.15.

*Proposition 6.2.18.* The divisors $H$, $H - E_1$, $H - E_2$ are base point free: $H$ is the pullback of $\mathcal{O}(1)$, and $H - E_i$ is the pullback of $\mathcal{O}(1)$ by the projection $X \to \mathbb{P}^{n-1}$ from $p_i$, which is a morphism on $\operatorname{Bl}_{p_i} \mathbb{P}^n$ by Proposition P7.4.18 and so on $X$. Their intersection numbers with $e_1$, $e_2$, $\ell_{12}$ are
$$H \colon (0, 0, 1), \qquad H - E_1 \colon (1, 0, 0), \qquad H - E_2 \colon (0, 1, 0),$$
using $E_i \cdot \ell_{12} = E_i \cdot \ell - E_i \cdot e_1 - E_i \cdot e_2 = 1$. So the two triples are dual bases of $N^1(X)$ and $N_1(X)$, both of dimension $3$. Since the three divisors are nef, $\overline{NE}(X) \subseteq \langle H, H - E_1, H - E_2 \rangle^\vee = \langle [e_1], [e_2], [\ell_{12}] \rangle$, and the right side is spanned by curves, so it is contained in $NE(X)$. This proves the first equality, and the second follows by duality, Theorem P7.4.9.

For part 2, $-K_X \cdot e_i = n - 1$ as before, and $-K_X \cdot \ell_{12} = (n + 1) - (n - 1)(E_1 + E_2) \cdot \ell_{12} = 3 - n$. If $n \ge 3$, then $K_X \cdot \ell_{12} \ge 0$ and $-K_X$ is not ample.

For part 3, let $L \subseteq \mathbb{P}^n$ be the line, with $N_{L/\mathbb{P}^n} \cong \mathcal{O}(1)^{\oplus (n-1)}$. If $C$ is a smooth curve in a smooth variety and $p \in C$, the strict transform $\tilde C$ of $C$ in the blow-up at $p$ has $N_{\tilde C} \cong N_C \otimes \mathcal{O}_C(-p)$, the standard formula for the strict transform of a smooth curve through the centre, since $\tilde C \cong C$ meets the exceptional divisor transversally at one point. Applying this at $p_1$ and $p_2$ gives $N_{\ell_{12}/X} \cong \mathcal{O}(-1)^{\oplus (n-1)}$. As a check, $\deg T_X|_{\ell_{12}} = 2 - (n - 1) = 3 - n = -K_X \cdot \ell_{12}$.

For part 4, $2H - E_1 - E_2 = (H - E_1) + (H - E_2)$ is a sum of base point free divisors, so it is base point free, and its morphism is $\varphi = (q_1, q_2) \colon X \to \mathbb{P}^{n-1} \times \mathbb{P}^{n-1}$ followed by the Segre embedding. A curve $C$ is contracted by $\varphi$ if and only if $(H - E_1) \cdot C = (H - E_2) \cdot C = 0$, that is, $[C] \in \mathbb{R}_{\ge 0} [\ell_{12}]$ by part 1. Such a curve is contracted by $q_1$, so it is the strict transform of a line through $p_1$, and by $q_2$, so the line also passes through $p_2$: it is $\ell_{12}$.

### Exercises

1. (A) Let $X = \mathbb{P}^a \times \mathbb{P}^b$. Compute $-K_X \cdot \ell_1$ and $-K_X \cdot \ell_2$, and show that the lengths of the two extremal rays are $a + 1$ and $b + 1$, both at most $n + 1 = a + b + 1$, with equality only if $a = 0$ or $b = 0$.
2. (A) In Proposition 6.2.17 for $n = 2$, identify $X$ with the Hirzebruch surface $\mathbb{F}_1$, and check the lengths $1$ and $2$ against Proposition P7.4.19.
3. (B) For $X = \operatorname{Bl}_{p_1, p_2} \mathbb{P}^n$ with $n \ge 4$, compute $\overline{NE}(X)_{K_X \ge 0}$ and show that it is a $3$-dimensional cone, spanned by $[\ell_{12}]$, $(n - 3) [e_1] + (n - 1) [\ell_{12}]$ and $(n - 3) [e_2] + (n - 1) [\ell_{12}]$. Write down the decomposition of part 3 of Theorem 6.2.9.
4. (B) Let $S$ be the blow-up of $\mathbb{P}^2$ at three collinear points, with $L$ the strict transform of the line. Show that $L^2 = -2$ and $K_S \cdot L = 0$, so $S$ is not del Pezzo, and find the $K_S$-negative extremal rays.
5. (B) Let $X = \operatorname{Bl}_p \mathbb{P}^n$. Show that the normal bundle of $\tilde\ell$ is $\mathcal{O}^{\oplus (n-1)}$ and the normal bundle of a line $e \subseteq E$ is $\mathcal{O}(1)^{\oplus (n-2)} \oplus \mathcal{O}(-1)$, and check both against the anticanonical degrees of Proposition 6.2.17.
6. (C) Let $X = \operatorname{Bl}_{p_1, \dots, p_r} \mathbb{P}^n$ for $r$ general points with $r \le n + 1$, $n \ge 3$. Show that the strict transforms $\ell_{ij}$ of the lines through two of the points satisfy $K_X \cdot \ell_{ij} = n - 3$, and show that $\langle [e_i], [\ell_{ij}] \rangle$ is the whole cone $\overline{NE}(X)$ by finding enough base point free divisors. (After a change of coordinates the points are coordinate points and $X$ is toric, so Theorem P8.8.18 gives another proof.)

### Lean

Nothing in this section is in Lean. The library has `MinimalModel.ExtremalRay`, the vocabulary of the rays computed here, and no computation of the cone of a specific variety.

### Notes and history

The examples are standard; see KM98, Section 1.3, and Debarre's Chapter 6 (Deb01). The two-point blow-up shows the limits of Theorem 6.2.9 from the other side: the cone theorem describes only the $K_X$-negative part, and for $n \ge 4$ the extremal ray of $\ell_{12}$ is $K_X$-positive and spanned by a rational curve of negative anticanonical degree. The small contraction of part 4 of Proposition 6.2.18 for $n = 3$ is the contraction of a flopping curve, and for $n \ge 4$ it is the contraction of a $K_X$-positive ray, so that $X$ is on the far side of a flip: near $\ell_{12}$ it is the standard flip of a $\mathbb{P}^{n-2}$ with normal bundle $\mathcal{O}(-1)^{\oplus 2}$, on which the canonical class has degree $3 - n < 0$ on a line.
