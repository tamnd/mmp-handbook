---
title: The class group, the canonical class and the discrepancy of a cone
nodes: []
sources: [Kol13, KM98, Rei87]
reads_with: [Kol13:3.1, KM98:3.1, Rei87:all]
requires: [P3.8, P3.9, P3.12, P5.5, P8.7, P8.8, P8.9, P8.11]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The class group, the canonical class and the discrepancy of a cone

### Statement

Keep the notation of Section 12.1: $V$ is smooth projective of dimension $n - 1 \geq 1$, $L$ is ample, $X = C(V, L)$ with vertex $0$, and $f \colon Y \to X$ is the resolution of Proposition P8.12.3, with exceptional divisor $E \cong V$ and projection $p \colon Y \to V$. Since $V$ is smooth, $\operatorname{Cl}(V) = \operatorname{Pic}(V)$. For a divisor $D$ on $V$ the *cone over $D$* is the Weil divisor $C_D = f_* p^* D$ on $X$; for $D$ a prime divisor it is the closure of the union of the lines of the cone over the points of $D$.

For a $\mathbb{Q}$-Cartier divisor $B$ on $X$, $f^* B$ is the $\mathbb{Q}$-divisor of Proposition P3.9.28. If $K_X$ is $\mathbb{Q}$-Cartier and $K_Y$ is chosen with $f_* K_Y = K_X$, there is a unique rational number $a(E, X)$ with
$$K_Y = f^* K_X + a(E, X) E,$$
the *discrepancy* of $E$. Chapter 13 shows that it depends only on $E$ and treats discrepancies in general; this chapter needs only the one number.

**Proposition P8.12.8 (the class group of a cone).** The map $D \mapsto C_D$ induces an isomorphism
$$\operatorname{Pic}(V) / \mathbb{Z} L \xrightarrow{\ \sim\ } \operatorname{Cl}(X).$$

Lean: not in Lean as stated.

**Proposition P8.12.9 (the Cartier criterion for cones).** Let $D$ be a divisor on $V$ and $m \geq 1$. Then $m C_D$ is Cartier on $X$ if and only if $m D \sim b L$ for some $b \in \mathbb{Z}$, and in that case $f^*(m C_D) = m \, p^* D + b E$ as divisors. In particular $C_D$ is $\mathbb{Q}$-Cartier if and only if $D \sim_\mathbb{Q} c L$ for some $c \in \mathbb{Q}$, and then $f^* C_D = p^* D + c E$.

Lean: not in Lean as stated.

**Theorem P8.12.10 (the canonical class of a cone).** The canonical divisor of $X$ is $K_X = C_{K_V}$.

1. $K_X$ is $\mathbb{Q}$-Cartier if and only if $K_V \sim_\mathbb{Q} r L$ for some $r \in \mathbb{Q}$, and Cartier if and only if $K_V \sim r L$ for some $r \in \mathbb{Z}$.
2. In that case $f^* K_X = p^* K_V + r E$ and
$$a(E, X) = -1 - r.$$

Lean: not in Lean as stated.

**Theorem P8.12.11 (cones over curves).** Let $n = 2$, so $V$ is a smooth projective curve of genus $g$, and let $d = \deg L \geq 1$.

1. $\operatorname{Cl}(X) \cong \operatorname{Pic}(V) / \mathbb{Z} L$, an extension of $\mathbb{Z}/d$ by the group $\operatorname{Pic}^0(V)$ of divisor classes of degree $0$.
2. $K_X$ is $\mathbb{Q}$-Cartier if and only if $d K_V - (2g - 2) L$ is a torsion element of $\operatorname{Pic}^0(V)$; this holds whenever $g \leq 1$. Then
$$a(E, X) = -1 - \frac{2g - 2}{d}.$$
3. The vertex is a rational singularity if and only if $g = 0$, and then $X \cong \frac{1}{d}(1, 1)$.

Lean: not in Lean as stated.

### Proof in words

The punctured cone is the complement of the zero section in a line bundle over $V$, so its class group is that of $V$ modulo the class of the zero section, which is $-L$. A Cartier divisor pulled back to $Y$ is trivial on the contracted divisor $E$, so restricting to $E \cong V$ shows that $m C_D$ can be Cartier only if $m D$ is a multiple of $L$, and the multiple is the coefficient of $E$ in the pullback. Applied to $K_X = C_{K_V}$ and compared with $K_Y = p^* K_V - E$, this gives $a(E, X) = -1 - r$. For curves, degrees force $r = (2g - 2)/d$, and Artin's criterion decides rationality from the genus of the single exceptional curve.

### Examples

**Example P8.12.12 (the singularities $\frac{1}{n}(1, 1)$).** By Example P8.12.4, $\frac{1}{n}(1, 1) = C(\mathbb{P}^1, \mathcal{O}(n))$. Here $g = 0$, $d = n$, $\operatorname{Cl}(X) = \mathbb{Z} / n$, as in Theorem P8.9.23, and $K_{\mathbb{P}^1} = \mathcal{O}(-2) = -\frac{2}{n} L$, so
$$a(E, X) = -1 + \frac{2}{n} = -\frac{n - 2}{n}.$$
This is $0$ for the quadric cone $n = 2$, where $K_X$ is Cartier, and lies in $(-1, 0)$ for $n \geq 3$. The index of $K_X$ is the least $m$ with $\frac{2m}{n} \in \mathbb{Z}$, which is $n$ for $n$ odd and $\frac{n}{2}$ for $n$ even, in agreement with Theorem P8.9.23.

**Example P8.12.13 (the singularities $\frac{1}{d}(1, \dots, 1)$).** By Example P8.12.5, $\frac{1}{d}(1, \dots, 1) = C(\mathbb{P}^{n-1}, \mathcal{O}(d))$, and $K_{\mathbb{P}^{n-1}} = \mathcal{O}(-n) = -\frac{n}{d} L$. So $\operatorname{Cl}(X) = \mathbb{Z}/d$ and $a(E, X) = \frac{n}{d} - 1$, which is positive for $d < n$, zero for $d = n$ and negative for $d > n$. For $\frac{1}{2}(1, 1, 1)$ this gives $\operatorname{Cl}(X) = \mathbb{Z}/2$ and $a(E, X) = \frac{1}{2}$, and since $K_{\mathbb{P}^2} = \mathcal{O}(-3)$ is not a multiple of $\mathcal{O}(2)$, $K_X$ is not Cartier while $2 K_X$ is.

**Example P8.12.14 (cones over hypersurfaces).** Let $V \subseteq \mathbb{P}^n$ be a smooth hypersurface of degree $e$ and $L = \mathcal{O}_V(1)$, as in Example P8.12.6. By Corollary P3.12.31, $K_V = (e - n - 1) L$, so $K_X$ is Cartier, as it must be on a hypersurface, and
$$a(E, X) = n - e.$$
For a plane curve of degree $e$ this is $2 - e$: $0$ for the conic, $-1$ for the elliptic cone and $-2$ for the cone over a plane quartic. For $V = \mathbb{P}^1 \times \mathbb{P}^1$ in $\mathbb{P}^3$ it is $1$, and for a smooth cubic surface it is $0$.

**Example P8.12.15 (the cone over a smooth quadric surface).** For $X = \{ xy = zw \} = C(\mathbb{P}^1 \times \mathbb{P}^1, \mathcal{O}(1, 1))$, Proposition P8.12.8 gives $\operatorname{Cl}(X) = \mathbb{Z}^2 / \mathbb{Z}(1, 1) \cong \mathbb{Z}$, generated by the cone over a line of one ruling, which is a plane in $X$. By Proposition P8.12.9 this plane is not $\mathbb{Q}$-Cartier, since $(1, 0)$ is not a rational multiple of $(1, 1)$; this is the toric computation of Example P8.7.14. By Theorem P8.12.10, $K_X$ is Cartier and $a(E, X) = 1$, since $K_V = \mathcal{O}(-2, -2) = -2 L$.

**Example P8.12.16 (a cone whose canonical class is not $\mathbb{Q}$-Cartier).** Let $V$ be a smooth projective curve of genus $2$, $P \in \operatorname{Pic}^0(V)$ and $L = K_V + P$, of degree $d = 2$. Then $d K_V - (2g - 2) L = -2P$, so by Theorem P8.12.11, $K_X$ is $\mathbb{Q}$-Cartier if and only if $P$ is a torsion point. If $k$ is uncountable, the torsion points of the two-dimensional abelian variety $\operatorname{Pic}^0(V)$ form a countable set while $\operatorname{Pic}^0(V)$ is uncountable, so a general $P$ gives a cone on which $K_X$ is not $\mathbb{Q}$-Cartier and $a(E, X)$ is not defined. For $P = 0$, that is $L = K_V$, $K_X$ is Cartier and $a(E, X) = -2$. Over the algebraic closure of a finite field every point of $\operatorname{Pic}^0(V)$ is torsion, and then $K_X$ is $\mathbb{Q}$-Cartier for every cone over a curve.

**Example P8.12.17 (the toric computation for $\frac{1}{n}(1, 1)$).** By Proposition P8.9.21, $\frac{1}{n}(1, 1)$ is the affine toric surface of $\sigma = \operatorname{Cone}(e_2, n e_1 - e_2)$. By Theorem P8.7.17, $K_X = -D_1 - D_2$, and $m = (\frac{2}{n}, 1)$ satisfies $\langle m, e_2 \rangle = \langle m, n e_1 - e_2 \rangle = 1$, so $n m = (2, n) \in M$ and $n K_X = \operatorname{div}(\chi^{-n m})$. The minimal resolution adds the ray through $e_1$, by Theorem P8.8.3 with $\frac{n}{1} = [n]$, and the order of $\chi^{n m}$ along the new divisor $E$ is $\langle n m, e_1 \rangle = 2$. So $f^* K_X = -D_1' - D_2' - \frac{2}{n} E$, while $K_Y = -D_1' - D_2' - E$ by Theorem P8.7.17 on the resolution, and $a(E, X) = -1 + \frac{2}{n}$, as in Example P8.12.12.

### Proof

*Proposition P8.12.8.* Since $\dim X = n \geq 2$, the vertex has codimension at least $2$, and Theorem P3.8.13 gives $\operatorname{Cl}(X) \cong \operatorname{Cl}(X \setminus \{ 0 \})$. By Proposition P8.12.2, $X \setminus \{ 0 \} \cong Y \setminus E$, and Theorem P3.8.13 again gives $\operatorname{Cl}(Y \setminus E) \cong \operatorname{Cl}(Y) / \mathbb{Z} E$.

It remains to show that $p^* \colon \operatorname{Pic}(V) \to \operatorname{Cl}(Y)$ is an isomorphism. It is injective, since the zero section $s \colon V \to Y$ satisfies $s^* p^* = \operatorname{id}$ on line bundles. For surjectivity let $D$ be a prime divisor on $Y$. The generic fibre of $p$ is $\mathbb{A}^1_{k(V)}$, whose class group is zero, so there is $\varphi \in k(Y)^*$ such that $D - \operatorname{div}(\varphi)$ has no component meeting the generic fibre. Each such component $D'$ maps into a proper closed subset of $V$, and since the fibres of $p$ are irreducible curves, $D' \subseteq p^{-1}(\overline{p(D')})$ with $p^{-1}(\overline{p(D')})$ irreducible of dimension $\dim \overline{p(D')} + 1$. So $\overline{p(D')}$ is a prime divisor $\Gamma$ of $V$ and $D' = p^{-1}(\Gamma) = p^* \Gamma$. This is the argument of Theorem P3.8.14. Under $p^*$, the class of $E$ is $-L$ by part 1 of Proposition P8.12.3, so $\operatorname{Cl}(X) \cong \operatorname{Pic}(V) / \mathbb{Z} L$. Following the isomorphisms, the class of $D$ goes to the class of the closure in $X$ of $p^* D|_{Y \setminus E}$, which is $f_* p^* D = C_D$.

*Proposition P8.12.9.* On $X \setminus \{ 0 \} \cong Y \setminus E$, which is smooth, every Weil divisor is Cartier, so only the vertex matters. Suppose $m C_D$ is Cartier on $X$. Then $f^*(m C_D)$ is a Cartier divisor on $Y$ which agrees with $m \, p^* D$ on $Y \setminus E$, so $f^*(m C_D) = m \, p^* D + b E$ for some $b \in \mathbb{Z}$. The line bundle $\mathcal{O}_Y(f^*(m C_D)) = f^* \mathcal{O}_X(m C_D)$ is trivial on $E = f^{-1}(0)$, since it is pulled back from a neighbourhood of the point $0$ on which $\mathcal{O}_X(m C_D)$ is trivial. Restricting to $E \cong V$ and using $\mathcal{O}_Y(E)|_E \cong L^{-1}$ gives $\mathcal{O}_V(m D) \otimes L^{-b} \cong \mathcal{O}_V$, that is, $m D \sim b L$. Conversely, if $m D \sim b L$, then $m C_D \sim b C_L$ by Proposition P8.12.8, and $C_L \sim 0$ there, so $m C_D$ is principal, hence Cartier. The integer $b$ is determined by $D$ and $m$, because $L$ has infinite order in $\operatorname{Pic}(V)$: its degree on any curve in $V$ is positive. Dividing by $m$ gives the statement for $\mathbb{Q}$-Cartier divisors with $c = b / m$.

*Theorem P8.12.10.* By part 2 of Proposition P8.12.3, $K_Y \sim p^* K_V - E$, and choosing $K_Y = p^* K_V - E$ for a fixed canonical divisor $K_V$, the restriction of $K_Y$ to $Y \setminus E \cong X \setminus \{ 0 \}$ is a canonical divisor there. By Proposition P3.12.29 a canonical divisor of the normal variety $X$ is determined by its restriction to the smooth locus, so $K_X = f_* K_Y = C_{K_V}$. Part 1 is Proposition P8.12.9 with $D = K_V$. For part 2, Proposition P8.12.9 gives $f^* K_X = p^* K_V + r E$, hence
$$K_Y = p^* K_V - E = f^* K_X - (1 + r) E,$$
and $a(E, X) = -1 - r$.

*Theorem P8.12.11.* (1) This is Proposition P8.12.8; the degree map $\operatorname{Pic}(V) \to \mathbb{Z}$ is surjective with kernel $\operatorname{Pic}^0(V)$, and it sends $\mathbb{Z} L$ onto $d \mathbb{Z}$. (2) If $K_V \sim_\mathbb{Q} r L$, then taking degrees, $2g - 2 = r d$, so $r = \frac{2g - 2}{d}$ and $d K_V - (2g - 2) L$ is torsion. Conversely, if $N (d K_V - (2g - 2) L) \sim 0$, then $K_V \sim_\mathbb{Q} \frac{2g - 2}{d} L$. For $g = 0$, $\operatorname{Pic}^0(V) = 0$, and for $g = 1$, $K_V \sim 0 = 0 \cdot L$. Theorem P8.12.10 gives the discrepancy. As a check, by Theorem P5.5.14 on $Y$, $K_Y \cdot E = 2g - 2 - E^2 = 2g - 2 + d$, while $K_Y \cdot E = a(E, X) E^2 = -a(E, X) d$ because $f^* K_X \cdot E = 0$, and the two agree. (3) The resolution $f$ has one exceptional curve $E$, smooth of genus $g$, so $Z_f = E$ and $p_a(Z_f) = g$. By Theorem P8.11.10 the vertex is rational if and only if $g = 0$. If $g = 0$, then $V = \mathbb{P}^1$, $L = \mathcal{O}(d)$, and $X \cong \frac{1}{d}(1, 1)$ by Example P8.12.4.

### Exercises

1. (A) Compute $\operatorname{Cl}(X)$, the index of $K_X$ and $a(E, X)$ for the cone over $\mathbb{P}^1 \times \mathbb{P}^1$ with $L = \mathcal{O}(1, 2)$, and decide whether $K_X$ is $\mathbb{Q}$-Cartier.
2. (A) Let $V \subseteq \mathbb{P}^3$ be a smooth quartic surface and $L = \mathcal{O}_V(1)$. Show that $a(E, X) = -1$ and that the vertex is not rational, using Proposition P4.9.23.
3. (B) Let $V$ be a smooth projective curve of genus $g \geq 2$ and $L = K_V$. Show that $R(V, K_V)$ is the canonical ring, that $K_X$ is Cartier and that $a(E, X) = -2$.
4. (B) Show that for every $\mathbb{Q}$-Cartier Weil divisor $C_D$ on $X$, the pullback $f^* C_D$ has $E$-coefficient $c$ with $D \sim_\mathbb{Q} c L$, and deduce that $X$ is $\mathbb{Q}$-factorial if and only if $\operatorname{Pic}(V) \otimes \mathbb{Q}$ is spanned by $L$.
5. (B) Let $V$ be a del Pezzo surface of degree $d$, that is, a smooth projective surface with $-K_V$ ample and $K_V^2 = d$, and let $L = -K_V$. Show that $K_X$ is Cartier, that $a(E, X) = 0$ and that $\operatorname{Cl}(X)$ has rank $9 - d$.
6. (C) Let $V$ be a smooth projective variety with $K_V \sim_\mathbb{Q} r L$. Show that $a(E, X) > -1$ if and only if $V$ is a Fano variety, $a(E, X) = -1$ if and only if $K_V \sim_\mathbb{Q} 0$, and $a(E, X) < -1$ if and only if $K_V$ is ample.

### Lean

The discrepancy relation $K_Y = f^* K_X + \sum a_i E_i$ underlies the predicates `MinimalModel.IsTerminal`, `MinimalModel.IsCanonical`, `MinimalModel.IsKlt` and `MinimalModel.IsLc` in `MinimalModel/Statements/Basic.lean`. Cones are not in the repository.

### Notes and history

The computation of the discrepancy of a cone is classical, and Reid (Rei87) uses it to show that the cones over del Pezzo surfaces are canonical Gorenstein singularities and that cones give examples of every class in Chapter 13. Kollár (Kol13), Section 3.1, proves the analogue of Theorem P8.12.10 for normal $V$ and $\mathbb{Q}$-divisors $L$, and shows that when $K_X$ is $\mathbb{Q}$-Cartier the vertex is terminal, canonical, klt or log canonical exactly when $a(E, X)$ is $> 0$, $\geq 0$, $> -1$ or $\geq -1$, so the single divisor $E$ decides the class of the singularity. Example P8.12.16 shows that $\mathbb{Q}$-Cartier is a real condition already for normal surfaces; Chapter 13 assumes it in the definitions.
