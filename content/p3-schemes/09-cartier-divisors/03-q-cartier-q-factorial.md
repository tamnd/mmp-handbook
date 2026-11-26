---
title: Q-Cartier divisors and Q-factoriality
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch14, Har77:II.6, GW20:ch11]
requires: [P1.8, P3.7, P3.8]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Q-Cartier divisors and Q-factoriality

### Statement

As in Section 9.2, $X$ is a normal integral Noetherian scheme with function field $K$. For $x \in X$ write $\mathcal{O} = \mathcal{O}_{X, x}$, a Noetherian normal domain with fraction field $K$, and $\operatorname{Cl}(\mathcal{O})$ for its class group, the *local class group* of $X$ at $x$. By part 3 of Proposition P3.8.2, the prime divisors $P$ of $X$ through $x$ correspond to the primes $\mathfrak{p}_P$ of height $1$ of $\mathcal{O}$, with $\mathcal{O}_{X, P} = \mathcal{O}_{\mathfrak{p}_P}$. Let
$$
\rho_x \colon \operatorname{Div}(X) \to \operatorname{Div}(\mathcal{O}), \qquad \sum_P n_P P \mapsto \sum_{P \ni x} n_P [\mathfrak{p}_P] .
$$

**Definition P3.9.18 (Cartier, $\mathbb{Q}$-Cartier, index, $\mathbb{Q}$-factorial).** Let $D$ be a Weil divisor and $x \in X$.

1. $D$ is *Cartier at* $x$ if it is locally principal at $x$, and *Cartier* if it is locally principal, that is, in the image of Proposition P3.9.9.
2. $D$ is *$\mathbb{Q}$-Cartier at* $x$ if $mD$ is Cartier at $x$ for some integer $m \geq 1$. The least such $m$ is the *index* $r_x(D)$ of $D$ at $x$. $D$ is *$\mathbb{Q}$-Cartier* if $mD$ is Cartier for some $m \geq 1$, and the least such $m$ is its *index* $r(D)$.
3. $X$ is *$\mathbb{Q}$-factorial at* $x$ if every Weil divisor is $\mathbb{Q}$-Cartier at $x$, and *$\mathbb{Q}$-factorial* if every Weil divisor is $\mathbb{Q}$-Cartier.
4. A $\mathbb{Q}$-divisor $\Delta$ is *$\mathbb{Q}$-Cartier* if $m \Delta$ is a Weil divisor that is Cartier for some integer $m \geq 1$, and the least such $m$ is its *index*. Two $\mathbb{Q}$-divisors are *$\mathbb{Q}$-linearly equivalent*, $\Delta \sim_\mathbb{Q} \Delta'$, if $m(\Delta - \Delta')$ is a principal Weil divisor for some $m \geq 1$.

Lean: not in Lean as stated.

**Proposition P3.9.19 (the local class group and the index).** Let $D$ be a Weil divisor and $x \in X$.

1. $\rho_x$ maps $\operatorname{div}(f)$ to the divisor $\operatorname{div}_\mathcal{O}(f)$ of $f$ on $\operatorname{Spec} \mathcal{O}$, it is surjective, and it induces a surjection $\operatorname{Cl}(X) \to \operatorname{Cl}(\mathcal{O})$.
2. $D$ is Cartier at $x$ if and only if $[\rho_x(D)] = 0$ in $\operatorname{Cl}(\mathcal{O})$. So $D$ is $\mathbb{Q}$-Cartier at $x$ if and only if $[\rho_x(D)]$ is torsion, and then $r_x(D)$ is its order. The integers $m$ with $mD$ Cartier at $x$ are the multiples of $r_x(D)$.
3. The set of points where $D$ is Cartier is open. It contains every point outside $\operatorname{Supp} D$, every point with factorial local ring, and every point of codimension at most $1$. So its complement is a closed subset of $\operatorname{Supp} D$ of codimension at least $2$.
4. If $D$ is $\mathbb{Q}$-Cartier at every point, then it is $\mathbb{Q}$-Cartier, the local indices take finitely many values, and $r(D) = \operatorname{lcm}_x r_x(D)$. The integers $m$ with $mD$ Cartier are the multiples of $r(D)$.
5. The $\mathbb{Q}$-Cartier divisors form a subgroup of $\operatorname{Div}(X)$ that contains the Cartier divisors. For $\mathbb{Q}$-Cartier $D, E$ and Cartier $C$, $r(D + C) = r(D) = r(-D)$ and $r(D + E)$ divides $\operatorname{lcm}(r(D), r(E))$.

Lean: not in Lean as stated.

**Theorem P3.9.20 ($\mathbb{Q}$-factoriality).** The following are equivalent.

1. $X$ is $\mathbb{Q}$-factorial.
2. $X$ is $\mathbb{Q}$-factorial at every closed point.
3. $\operatorname{Cl}(\mathcal{O}_{X, x})$ is a torsion group for every closed point $x$.
4. The quotient $\operatorname{Cl}(X)/\operatorname{Pic}(X)$, with $\operatorname{Pic}(X) \subseteq \operatorname{Cl}(X)$ by Proposition P3.9.9, is a torsion group.

A locally factorial scheme is $\mathbb{Q}$-factorial, a normal scheme with torsion class group is $\mathbb{Q}$-factorial, and every nonempty open subscheme of a $\mathbb{Q}$-factorial scheme is $\mathbb{Q}$-factorial.

Lean: not in Lean as stated.

### Proof in words

A divisor is Cartier at a point when it is principal on a neighbourhood, and only the prime divisors through the point matter for this. So the question lives in the class group of the local ring, and the index at the point is the order of the class there. Being principal near a point is an open condition, so a single multiple works on a neighbourhood, and by quasi-compactness a single multiple works on all of $X$. A scheme is $\mathbb{Q}$-factorial when all local class groups are torsion, and this is the same as asking that every Weil divisor class has a multiple that is a line bundle.

### Examples

**Example P3.9.21 (the cones $xy = z^n$).** Let $k$ be perfect, $n \geq 2$, and $X_n = V(xy - z^n) \subseteq \mathbb{A}^3_k$ with $L = V(x, z)$ and $M = V(y, z)$. By Example P3.9.13, $L$ has index $n$ at the vertex, and by part 2 of Proposition P3.9.19 its image in $\operatorname{Cl}(\mathcal{O}_{X_n, 0})$ has order $n$. Since $\operatorname{Cl}(X_n) = \mathbb{Z}/n$ is generated by $[L]$ and maps onto $\operatorname{Cl}(\mathcal{O}_{X_n, 0})$, the local class group at the vertex is $\mathbb{Z}/n$. So $X_n$ is $\mathbb{Q}$-factorial, every Weil divisor has index dividing $n$, and $\operatorname{Cl}(X_n)/\operatorname{Pic}(X_n) = \mathbb{Z}/n$. Since $\operatorname{div}(z) = L + M$, the divisor $M$ is linearly equivalent to $-L$, and it also has index $n$. For the $\mathbb{Q}$-divisor $\Delta = \frac{1}{2} L$ on $X_3$, $m\Delta$ is a Weil divisor exactly when $2 \mid m$, and $\frac{m}{2} L$ is Cartier exactly when $3 \mid \frac{m}{2}$. So $\Delta$ has index $6$.

**Example P3.9.22 (the projective quadric cone).** Let $Q_0 = V_+(xy - z^2) \subseteq \mathbb{P}^3_k$ over a perfect field, with vertex $v$, line $L$ and plane section $H \sim 2L$, as in Example P3.9.15. Away from $v$ the surface is locally factorial, and $\operatorname{Cl}(\mathcal{O}_{Q_0, v}) = \operatorname{Cl}(\mathcal{O}_{X_2, 0}) = \mathbb{Z}/2$. So $Q_0$ is $\mathbb{Q}$-factorial, $L$ has index $2$, and $\operatorname{Cl}(Q_0)/\operatorname{Pic}(Q_0) = \mathbb{Z}/2\mathbb{Z}$. The divisor $L$ is $\mathbb{Q}$-linearly equivalent to $\frac{1}{2} H$, although no integral multiple of $L$ smaller than $2L$ is a line bundle. This is the precise form of the statement at the end of Example P3.8.25.

**Example P3.9.23 (the cone over a smooth quadric surface).** Let $k$ be perfect, $X = V(xw - yz) \subseteq \mathbb{A}^4_k$, $P = V(x, y)$ and $P' = V(x, z)$. Then $X$ is normal, $\operatorname{div}(x) = P + P'$, and $\operatorname{Cl}(X) \cong \mathbb{Z}$ is generated by $[P]$ (Example P1.8.15). No multiple $aP$ with $a \neq 0$ is Cartier at the vertex (Example P1.8.23). So $X$ is not $\mathbb{Q}$-factorial at the vertex, $\operatorname{Pic}(X) = 0$, and $\operatorname{Cl}(X)/\operatorname{Pic}(X) = \mathbb{Z}$. The divisor $P + P'$ is Cartier while $P$ and $P'$ are not even $\mathbb{Q}$-Cartier. The complement of the vertex is covered by $D(x)$, $D(y)$, $D(z)$ and $D(w)$, and on $D(x)$ the ring is $k[x, x^{-1}, y, z]$ with $w = yz/x$, which is factorial, and similarly for the others. So $X \setminus \{0\}$ is locally factorial, and by excision, as the vertex has codimension $3$, $\operatorname{Pic}(X \setminus \{0\}) \cong \operatorname{Cl}(X \setminus \{0\}) \cong \operatorname{Cl}(X) \cong \mathbb{Z}$. The failure of $\mathbb{Q}$-factoriality is concentrated at one point.

**Example P3.9.24 (affine space and its open subsets).** Every open subset $U$ of $\mathbb{A}^n_k$ or of $\mathbb{P}^n_k$ is locally factorial, so $\mathbb{Q}$-factorial with every index equal to $1$. A $\mathbb{Q}$-divisor $\Delta = \sum a_i D_i$ on $U$ is $\mathbb{Q}$-Cartier, and its index is the least common denominator of the $a_i$. On $\mathbb{P}^2_k$ the divisor $\frac{1}{2}(\ell_1 + \ell_2 + \ell_3 + \ell_4)$ for four lines is $\mathbb{Q}$-linearly equivalent to $2\ell_1$. It is not a Weil divisor, and its index is $2$.

**Example P3.9.25 (the Cartier locus).** On $X_n$ with $n \geq 2$ the divisor $L$ is Cartier exactly on $X_n \setminus \{0\}$, since $X_n \setminus \{0\}$ is locally factorial by Example P3.9.14 and $L$ has index $n$ at the vertex. The complement of the Cartier locus is the vertex, a closed subset of $\operatorname{Supp} L$ of codimension $2$, as part 3 of Proposition P3.9.19 predicts. On the cone of Example P3.9.23 the divisor $P$ is Cartier exactly on $X \setminus \{0\}$, and it is not even $\mathbb{Q}$-Cartier at the vertex. So the $\mathbb{Q}$-Cartier locus of a Weil divisor can also be a proper open subset.

### Proof

*Proof of Proposition P3.9.19.* (1) For $f \in K^*$ and a prime divisor $P$ through $x$, $\operatorname{ord}_P(f)$ is the valuation of $f$ at $\mathfrak{p}_P$, since $\mathcal{O}_{X, P} = \mathcal{O}_{\mathfrak{p}_P}$. So $\rho_x(\operatorname{div}(f)) = \operatorname{div}_\mathcal{O}(f)$. Every prime of height $1$ of $\mathcal{O}$ is some $\mathfrak{p}_P$, so $\rho_x$ is surjective, and it induces a surjection on class groups.

(2) If $D|_U = \operatorname{div}(f)|_U$ for an open $U \ni x$, then every prime divisor through $x$ meets $U$, so $\rho_x(D) = \rho_x(\operatorname{div}(f)) = \operatorname{div}_\mathcal{O}(f)$. Conversely, let $\rho_x(D) = \operatorname{div}_\mathcal{O}(f)$ with $f \in K^*$. Then $E = D - \operatorname{div}(f)$ has $\rho_x(E) = 0$, that is, no component of $E$ passes through $x$. The support of $E$ is a finite union of prime divisors, a closed set not containing $x$, and $D = \operatorname{div}(f)$ on its complement. The statements on $\mathbb{Q}$-Cartier divisors follow, since $\rho_x(mD) = m \rho_x(D)$ and the $m$ with $m c = 0$ for an element $c$ of finite order are the multiples of its order.

(3) The set of points where $D$ is Cartier is open by definition. If $x \notin \operatorname{Supp} D$, then $D|_U = 0 = \operatorname{div}(1)|_U$ for $U = X \setminus \operatorname{Supp} D$. If $\mathcal{O}_{X, x}$ is factorial, $D$ is Cartier at $x$ by Theorem P3.9.10. If $\dim \mathcal{O}_{X, x} \leq 1$, then $\mathcal{O}_{X, x}$ is regular by part 4 of Proposition P3.7.32, so it is a field or a discrete valuation ring, and so factorial. So the complement is contained in $\operatorname{Supp} D$ and contains no point of codimension at most $1$, which is the claim on its codimension.

(4) For each $x$ choose an open $U_x \ni x$ on which $r_x(D) D$ is principal. Then $r_x(D) D$ is Cartier at every point of $U_x$, and by (2) $r_y(D)$ divides $r_x(D)$ for $y \in U_x$. As $X$ is quasi-compact, finitely many $U_{x_1}, \dots, U_{x_s}$ cover $X$. So every $r_y(D)$ divides $N = \operatorname{lcm}_j r_{x_j}(D)$, the local indices take finitely many values, and $ND$ is Cartier at every point. By (2), $mD$ is Cartier if and only if $r_y(D) \mid m$ for all $y$, that is, if and only if $\operatorname{lcm}_y r_y(D) \mid m$.

(5) Cartier divisors form a group (Exercise 4 of Section 9.2). If $mD$ and $m'E$ are Cartier, then $mm'(D + E)$ and $m(-D)$ are Cartier. Since $mC$ is Cartier for every $m$, $m(D + C)$ is Cartier if and only if $mD$ is, which gives $r(D + C) = r(D)$, and $r(-D) = r(D)$ is clear. If $m = \operatorname{lcm}(r(D), r(E))$, then $mD$ and $mE$ are Cartier by (4), so $m(D + E)$ is, and $r(D + E) \mid m$ by (4). $\square$

*Proof of Theorem P3.9.20.* (1) $\Rightarrow$ (2) is clear. (2) $\Leftrightarrow$ (3): by part 1 of Proposition P3.9.19 every class of $\operatorname{Cl}(\mathcal{O}_{X, x})$ is the image of a Weil divisor, and by part 2 that divisor is $\mathbb{Q}$-Cartier at $x$ if and only if its image is torsion.

(2) $\Rightarrow$ (1). Let $D$ be a Weil divisor and $y \in X$. The closure $\overline{\{y\}}$ is a nonempty closed subset of the quasi-compact scheme $X$, so it contains a closed point $x$ of $X$. By (2), $mD$ is Cartier at $x$ for some $m \geq 1$, so $mD$ is principal on an open $U \ni x$. As $x \in \overline{\{y\}}$, the open set $U$ contains $y$, so $D$ is $\mathbb{Q}$-Cartier at $y$. By part 4 of Proposition P3.9.19, $D$ is $\mathbb{Q}$-Cartier.

(1) $\Leftrightarrow$ (4). By Proposition P3.9.9, $\operatorname{Pic}(X)$ is the group of classes of Cartier divisors. If $X$ is $\mathbb{Q}$-factorial and $D$ is a Weil divisor, then $mD$ is Cartier for some $m \geq 1$, so $m[D] \in \operatorname{Pic}(X)$. Conversely, if $m[D] \in \operatorname{Pic}(X)$, then $mD = C + \operatorname{div}(g)$ with $C$ Cartier, and $mD$ is Cartier.

For the last statements: a locally factorial scheme has every Weil divisor Cartier (Theorem P3.9.10). If $\operatorname{Cl}(X)$ is torsion, so is its quotient in (4). Let $U \subseteq X$ be a nonempty open subscheme and $E$ a Weil divisor on $U$. By Theorem P3.8.13, $E = D|_U$ for a Weil divisor $D$ on $X$, obtained by taking closures of the components. If $mD$ is principal on an open $V$ of $X$, then $mE$ is principal on $V \cap U$, so $E$ is $\mathbb{Q}$-Cartier at every point of $U$. Part 4 of Proposition P3.9.19 applied to $U$ finishes the proof. $\square$

### Exercises

1. (A) On $X_n$ of Example P3.9.21 show that the index of $aL + bM$ at the vertex is $n/\gcd(n, a - b)$.
2. (A) On $Q_0$ of Example P3.9.22 compute the indices of the $\mathbb{Q}$-divisors $\frac{1}{2} L$, $\frac{1}{2} H$ and $\frac{1}{3}(L + H)$.
3. (A) Let $D$ be a Weil divisor and $C$ a Cartier divisor. Show that multiplication in $\mathcal{K}$ is an isomorphism $\mathcal{O}_X(D) \otimes \mathcal{O}_X(C) \to \mathcal{O}_X(D + C)$.
4. (B) On the quadric cone $X_2$ show that the multiplication map $\mathcal{O}(L) \otimes \mathcal{O}(L) \to \mathcal{O}(2L)$ is not surjective, using Example P3.8.32. So Exercise 3 needs $C$ to be Cartier.
5. (B) On the cone of Example P3.9.23 show that $aP + bP'$ is Cartier at the vertex if and only if $a = b$, and that it is $\mathbb{Q}$-Cartier at the vertex if and only if $a = b$.
6. (B) Let $X$ be $\mathbb{Q}$-factorial and $\pi \colon X \times \mathbb{A}^1 \to X$ the projection. Show that $X \times \mathbb{A}^1$ is $\mathbb{Q}$-factorial, using Theorem P3.8.14, the fact that $\pi^{-1}$ of a local equation is a local equation, and part 4 of Theorem P3.9.20.
7. (C) Let $X$ be normal and $D$ a Weil divisor. Show that the set of points at which $D$ is $\mathbb{Q}$-Cartier is open, and that it can be strictly larger than the set where $D$ is Cartier. Show that the set of points at which $X$ is $\mathbb{Q}$-factorial is stable under generization, and give an example where it is not all of $X$.

### Lean

Mathlib has no notion of a Cartier, $\mathbb{Q}$-Cartier or $\mathbb{Q}$-factorial divisor on a scheme, and no local class group. The order of vanishing `AlgebraicGeometry.Scheme.ord` and the Weil divisors `AlgebraicGeometry.AlgebraicCycle.weilDivisors` are the starting point, and `ClassGroup` covers the invertible fractional ideals of a domain. The statements of this section are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

The algebraic form of this section is P1 Ch. 8, Section 8.3, and Proposition P3.9.19 is its sheaf form. The literature state is theorem. In the minimal model program the canonical divisor $K_X$ of a normal variety is a Weil divisor, and the program asks that $K_X$ be $\mathbb{Q}$-Cartier, so that intersection numbers $K_X \cdot C$ with curves are defined as rational numbers. The index of $K_X$ is the index of the variety. The program is run in the category of $\mathbb{Q}$-factorial varieties, where every Weil divisor has this property, and the steps of Volume 4, divisorial contractions and flips, preserve $\mathbb{Q}$-factoriality. Example P3.9.23 shows why flops need care: the contraction of the curve in the standard flop of threefolds has the cone of that example as its target, and this cone is not $\mathbb{Q}$-factorial. The condition is local in the Zariski topology, by Theorem P3.9.20, and a theorem about it on a projective variety needs the global group $\operatorname{Cl}(X)/\operatorname{Pic}(X)$.
