---
title: Global sections and base points
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch16, Har77:II.7, GW20:ch13]
requires: [P3.6, P3.8, P3.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Global sections and base points

### Statement

Throughout this chapter $k$ is a field and $X$ is a scheme over $k$. For an invertible sheaf $\mathcal{L}$ on $X$, a point $x \in X$ and $s \in \Gamma(X, \mathcal{L})$, write $s(x)$ for the image of $s$ in the fibre $\mathcal{L}(x) = \mathcal{L}_x \otimes \kappa(x)$, a vector space of dimension $1$ over $\kappa(x)$. So $s(x) = 0$ means $s_x \in \mathfrak{m}_x \mathcal{L}_x$. If $X$ is projective over $k$, then $\Gamma(X, \mathcal{L})$ has finite dimension over $k$ (Hartshorne, Theorem II.5.19). If $X$ is integral, every nonzero $s \in \Gamma(X, \mathcal{L})$ has a divisor of zeros $Z(s)$, the effective Cartier divisor with local equations $s / e_i$ for local generators $e_i$ of $\mathcal{L}$ (Exercise 7 of Section 9.1).

For $\mathcal{L} = \mathcal{O}_X(D)$ with $D$ a Cartier divisor on an integral $X$, the sections are the $g \in K$ with $\operatorname{div}(g) + D \geq 0$ (Proposition P3.9.3), and $Z(g) = \operatorname{div}(g) + D$.

**Definition P3.10.1 (linear system, base locus).** Let $\mathcal{L}$ be invertible on $X$.

1. A *linear system* of $\mathcal{L}$ is a finite dimensional $k$-subspace $V \subseteq \Gamma(X, \mathcal{L})$. If $\Gamma(X, \mathcal{L})$ has finite dimension, $V = \Gamma(X, \mathcal{L})$ is the *complete* linear system. If $X$ is integral, the set of divisors $|V| = \{ Z(s) : s \in V \setminus 0 \}$ is also called the linear system, and $|\mathcal{L}|$ or $|D|$ is the complete one.
2. The *base locus* of $V$ is $\operatorname{Bs}(V) = \{ x \in X : s(x) = 0 \text{ for all } s \in V \}$, and its points are the *base points*. $V$ is *base point free* if $\operatorname{Bs}(V) = \emptyset$.
3. Let $X$ be normal, integral and Noetherian, and $D$ a Weil divisor. For a finite dimensional subspace $V \subseteq \Gamma(X, \mathcal{O}_X(D))$ put $|V| = \{ \operatorname{div}(g) + D : g \in V \setminus 0 \}$ and $\operatorname{Bs}(V) = \bigcap_{E \in |V|} \operatorname{Supp} E$. The *fixed part* of $V \neq 0$ is the Weil divisor $F$ whose coefficient at each prime divisor $P$ is $\min_{E \in |V|} \operatorname{mult}_P E$, and $|V|$ has *no fixed component* if $F = 0$.
4. For $\mathcal{L}$ invertible with $\Gamma(X, \mathcal{L}^m)$ finite dimensional for all $m \geq 1$, the *stable base locus* is $\mathbf{B}(\mathcal{L}) = \bigcap_{m \geq 1} \operatorname{Bs}(\Gamma(X, \mathcal{L}^m))$. The same definition applies to a Cartier divisor $D$, using $|mD|$.

Lean: not in Lean as stated.

**Proposition P3.10.2 (first properties of base loci).** Let $\mathcal{L}$ and $\mathcal{M}$ be invertible on $X$ and $V \subseteq \Gamma(X, \mathcal{L})$, $W \subseteq \Gamma(X, \mathcal{M})$ linear systems.

1. If $s_0, \dots, s_n$ span $V$, then $\operatorname{Bs}(V) = \{x : s_0(x) = \dots = s_n(x) = 0\} = X \setminus (X_{s_0} \cup \dots \cup X_{s_n})$. It is closed, and $V$ is base point free if and only if $s_0, \dots, s_n$ generate $\mathcal{L}$. If $X$ is integral, $\operatorname{Bs}(V) = \bigcap_i \operatorname{Supp} Z(s_i)$ for $V \neq 0$.
2. If $V \subseteq V'$, then $\operatorname{Bs}(V') \subseteq \operatorname{Bs}(V)$.
3. Let $V \cdot W \subseteq \Gamma(X, \mathcal{L} \otimes \mathcal{M})$ be the span of the products $s \otimes t$. Then $\operatorname{Bs}(V \cdot W) = \operatorname{Bs}(V) \cup \operatorname{Bs}(W)$. In particular $\operatorname{Bs}(\Gamma(\mathcal{L}^{a + b})) \subseteq \operatorname{Bs}(\Gamma(\mathcal{L}^a)) \cup \operatorname{Bs}(\Gamma(\mathcal{L}^b))$ and $\operatorname{Bs}(\Gamma(\mathcal{L}^{ma})) \subseteq \operatorname{Bs}(\Gamma(\mathcal{L}^a))$, when these spaces are finite dimensional.
4. If $X$ is Noetherian and the stable base locus is defined, there is $m_0 \geq 1$ with $\mathbf{B}(\mathcal{L}) = \operatorname{Bs}(\Gamma(X, \mathcal{L}^{k m_0}))$ for all $k \geq 1$.
5. In the situation of part 3 of Definition P3.10.1, $\operatorname{Bs}(V)$ is closed, it contains every point at which $D$ is not Cartier, and it contains $\operatorname{Supp} F$. If $D$ is Cartier, then $\operatorname{Bs}(V)$ agrees with the base locus of $V \subseteq \Gamma(X, \mathcal{O}_X(D))$ in part 2.

Lean: not in Lean as stated.

**Theorem P3.10.3 (linear systems as projective spaces).** Let $X$ be integral, $D$ a Cartier divisor, and assume $\Gamma(X, \mathcal{O}_X) = k$. This holds when $X$ is proper over an algebraically closed $k$, by Theorem P3.4.21.

1. For $g, g' \in \Gamma(X, \mathcal{O}_X(D)) \setminus 0$, $Z(g) = Z(g')$ if and only if $g' = c g$ with $c \in k^*$. So for every linear system $V$ the map $g \mapsto Z(g)$ is a bijection from $(V \setminus 0)/k^*$, the set of $k$-points of the projective space $\mathbb{P}(V)$ of lines in $V$, to $|V|$.
2. The complete linear system $|D|$ is the set of effective Cartier divisors linearly equivalent to $D$.
3. If $X$ is normal and Noetherian, $V \neq 0$ has fixed part $F$, and $g_0, \dots, g_n$ is a basis, then $\operatorname{mult}_P F = \min_i \operatorname{mult}_P Z(g_i)$ for every prime divisor $P$, $F$ is effective, $V \subseteq \Gamma(X, \mathcal{O}_X([D] - F))$, and $V$ has no fixed component as a linear system of $[D] - F$.

Lean: not in Lean as stated.

### Proof in words

A section of a line bundle vanishes at a point if its value in the fibre is zero. A linear system has a base point where all its sections vanish, and it is enough to test a basis. Products of sections vanish exactly where one factor vanishes, which gives the behaviour of base loci under sums and multiples. A section is determined by its divisor up to a nowhere vanishing function, and on a proper connected reduced scheme over an algebraically closed field these functions are the constants. So the divisors of a linear system form a projective space.

### Examples

**Example P3.10.4 (hypersurfaces).** On $\mathbb{P}^n_k$, $\Gamma(\mathcal{O}(d))$ is the space of forms of degree $d$ for $d \geq 0$ (Theorem P3.6.12), of dimension $\binom{n + d}{d}$. The members of $|\mathcal{O}(d)|$ are the hypersurfaces $V_+(F)$ of degree $d$, and $\Gamma(\mathcal{O}_{\mathbb{P}^n}) = k$. The system is base point free for $d \geq 0$, since $x_i^d$ does not vanish on $D_+(x_i)$. For $d < 0$ the system is empty and every point is a base point.

**Example P3.10.5 (a pencil of lines).** On $\mathbb{P}^2_k$ let $V = \langle x, y \rangle \subseteq \Gamma(\mathcal{O}(1))$. Its members are the lines $V_+(ax + by)$ through $p = [0 : 0 : 1]$, and $\operatorname{Bs}(V) = V_+(x, y) = \{p\}$ by part 1 of Proposition P3.10.2. The complete system $|\mathcal{O}(1)|$ contains $V$ and is base point free.

**Example P3.10.6 (a fixed component).** On $\mathbb{P}^2_k$ let $V = \langle x^2, xy \rangle \subseteq \Gamma(\mathcal{O}(2))$. Every member is $V_+(x(ax + by)) = V_+(x) + V_+(ax + by)$, so the fixed part is the line $F = V_+(x)$, and $\operatorname{Bs}(V) = V_+(x)$. Removing it gives the pencil of Example P3.10.5, with one base point.

**Example P3.10.7 (the quadric cone).** Let $k$ be perfect and $Q_0 = V_+(xy - z^2) \subseteq \mathbb{P}^3_k$, with vertex $v = [0 : 0 : 0 : 1]$, a line $L$ through $v$ and $H \sim 2L$ a plane section (Example P3.9.22). Take $L = V_+(x, z)$ and, for $a \in k^*$, the line $L_a = V_+(z - ax, y - a^2 x)$ through $v$. The plane $V_+(z - ax)$ meets $Q_0$ in $L + L_a$, and the plane $V_+(x)$ meets it in $2L$, so $L_a \sim L$ and $L_a \in |L|$. Since $L \cap L_a = \{v\}$, the base locus of $|L|$ is contained in $\{v\}$. By part 5 of Proposition P3.10.2, $v \in \operatorname{Bs}|L|$, as $L$ is not Cartier at $v$. On the other hand $|2L| = |H|$ contains all plane sections of $Q_0$, and every point of $Q_0$ lies outside some plane, so $|2L|$ is base point free. So $\operatorname{Bs}|L| = \{v\}$ while $\operatorname{Bs}|2L| = \emptyset$. If the stable base locus of a Weil divisor is defined by the same formula with $|mL|$, then it is empty for $L$, although $|L|$ has a base point.

**Example P3.10.8 (an incomplete system on the line).** On $\mathbb{P}^1_k$ let $V = \langle s^2, t^2 \rangle \subseteq \Gamma(\mathcal{O}(2))$. It is base point free, as $s^2$ and $t^2$ have no common zero, and it is not complete: $st \notin V$. Its members are $V_+(a s^2 + b t^2)$, and Example P3.9.30 with $d = 2$ is the morphism that it defines.

### Proof

*Proof of Proposition P3.10.2.* (1) If $s = \sum c_i s_i$ with $c_i \in k$, then $s(x) = \sum c_i s_i(x)$, so $s(x) = 0$ for all $s \in V$ if and only if $s_i(x) = 0$ for all $i$. By Nakayama's lemma, $s_i(x) \neq 0$ if and only if $s_{i, x}$ generates $\mathcal{L}_x$, that is, $x \in X_{s_i}$, an open set (Section 6.2). So the base locus is the complement of $\bigcup_i X_{s_i}$, it is closed, and it is empty if and only if the $s_i$ generate $\mathcal{L}_x$ at every point. For $X$ integral and $s \neq 0$, $x \in \operatorname{Supp} Z(s)$ if and only if the local equation $s/e_i$ is not a unit at $x$, that is, $s(x) = 0$. A section $s_i = 0$ has $s_i(x) = 0$ everywhere and can be dropped from the basis.

(2) is clear. (3) $(s \otimes t)(x) = s(x) \otimes t(x)$ in the line $\mathcal{L}(x) \otimes \mathcal{M}(x)$, which vanishes if and only if $s(x) = 0$ or $t(x) = 0$. If $x \notin \operatorname{Bs}(V) \cup \operatorname{Bs}(W)$, choose $s \in V$ and $t \in W$ with $s(x) \neq 0 \neq t(x)$, and then $x \notin \operatorname{Bs}(V \cdot W)$. If $x \in \operatorname{Bs}(V)$, then every product $s \otimes t$, and so every element of $V \cdot W$, vanishes at $x$. The rest follows from $\Gamma(\mathcal{L}^a) \cdot \Gamma(\mathcal{L}^b) \subseteq \Gamma(\mathcal{L}^{a + b})$, part 2, and induction on $m$.

(4) The closed sets $\operatorname{Bs}(\Gamma(\mathcal{L}^m))$, $m \geq 1$, form a nonempty family of closed subsets of a Noetherian space, so the family has a minimal element $B_0 = \operatorname{Bs}(\Gamma(\mathcal{L}^{m_0}))$. For $k, m \geq 1$, part 3 gives $\operatorname{Bs}(\Gamma(\mathcal{L}^{k m_0 m})) \subseteq \operatorname{Bs}(\Gamma(\mathcal{L}^{m_0})) \cap \operatorname{Bs}(\Gamma(\mathcal{L}^{m}))$. By minimality, $\operatorname{Bs}(\Gamma(\mathcal{L}^{k m_0 m})) = B_0$, and so $B_0 \subseteq \operatorname{Bs}(\Gamma(\mathcal{L}^m))$ for every $m$. So $\mathbf{B}(\mathcal{L}) = B_0$, and the same argument with $m = 1$ gives $\operatorname{Bs}(\Gamma(\mathcal{L}^{k m_0})) = B_0$.

(5) Each $\operatorname{Supp} E$ is closed, so $\operatorname{Bs}(V)$ is closed. If $x \notin \operatorname{Bs}(V)$, there is $E = \operatorname{div}(g) + D \in |V|$ with $x \notin \operatorname{Supp} E$. Then $D = E - \operatorname{div}(g)$ equals $-\operatorname{div}(g) = \operatorname{div}(g^{-1})$ on the open set $X \setminus \operatorname{Supp} E$, so $D$ is Cartier at $x$. If $P$ is a component of $F$, then $\operatorname{mult}_P E \geq \operatorname{mult}_P F > 0$ for all $E \in |V|$, so $P \subseteq \operatorname{Bs}(V)$. If $D$ is Cartier, then $Z(g)$ is the Cartier divisor $\operatorname{div}(g) + D$, its Weil divisor is $\operatorname{div}(g) + [D]$, and both have the same support (proof of Proposition P3.9.28), so the two base loci agree by part 1. $\square$

*Proof of Theorem P3.10.3.* (1) If $Z(g) = Z(g')$, then $\operatorname{div}(g'/g) = Z(g') - Z(g) = 0$, so $g'/g$ is a unit of $\Gamma(X, \mathcal{O}_X)$ by the exact sequence of Theorem P3.9.4, that is, $g'/g \in k^*$. Conversely $Z(cg) = Z(g)$ for $c \in k^*$, as $\operatorname{div}(c) = 0$.

(2) Every $Z(g)$ is effective and $Z(g) - D = \operatorname{div}(g)$. If $E \geq 0$ and $E = D + \operatorname{div}(g)$, then $g \in \Gamma(X, \mathcal{O}_X(D))$ by part 5 of Proposition P3.9.3, and $E = Z(g)$.

(3) Every $g \in V \setminus 0$ is $g = \sum c_i g_i$, and $\operatorname{ord}_P(g) \geq \min_i \operatorname{ord}_P(g_i)$ for the valuation $\operatorname{ord}_P$, so $\operatorname{mult}_P Z(g) \geq \min_i \operatorname{mult}_P Z(g_i)$, which gives the formula. Only finitely many $P$ lie in some $\operatorname{Supp} Z(g_i)$, so $F$ is a Weil divisor, and it is effective since every $Z(g_i)$ is. For $g \in V \setminus 0$, $\operatorname{div}(g) + [D] - F = [Z(g)] - F \geq 0$, so $g \in \Gamma(\mathcal{O}_X([D] - F))$ by Theorem P3.8.29. The members of $V$ as a system of $[D] - F$ are the $[Z(g)] - F$, and the minimum of their multiplicities at each $P$ is $0$. $\square$

### Exercises

1. (A) On $\mathbb{P}^2_k$ find the base locus and the fixed part of $\langle x^2, y^2, xy \rangle$ and of $\langle xy, xz \rangle$ in $\Gamma(\mathcal{O}(2))$.
2. (A) Show that $\langle x_0^d, \dots, x_n^d \rangle \subseteq \Gamma(\mathbb{P}^n_k, \mathcal{O}(d))$ is base point free, and that $\langle x_1^d, \dots, x_n^d \rangle$ has the single base point $[1 : 0 : \dots : 0]$.
3. (A) Let $X$ be an integral scheme and $D, E$ Cartier divisors. Show that $|D|, |E| \neq \emptyset$ implies $|D + E| \neq \emptyset$. Show on $\mathbb{P}^1_k$ that $|D| = \emptyset$ and $E \geq 0$ do not imply $|D + E| = \emptyset$.
4. (B) On $\mathbb{P}^1_k \times_k \mathbb{P}^1_k$ show that the sections of the line bundle $\mathcal{O}(1, 0) = p_1^* \mathcal{O}(1)$ form a base point free system whose members are the fibres $\{a\} \times \mathbb{P}^1$.
5. (B) Let $X$ be integral with $\Gamma(X, \mathcal{O}_X) = k$, $D$ a Cartier divisor and $E \in |D|$. Show that $\operatorname{Bs}|D| \subseteq \operatorname{Supp} E$, and that $\operatorname{Bs}|D| = \emptyset$ if and only if for every $x \in X$ there is $E \in |D|$ with $x \notin \operatorname{Supp} E$.
6. (B) On the cone $X_n = V(xy - z^n) \subseteq \mathbb{A}^3_k$ of Example P3.9.21 with $k$ perfect, show that the vertex is a base point of the linear system $\langle 1, y/z \rangle \subseteq \Gamma(\mathcal{O}_{X_n}(L))$, and that $\Gamma(\mathcal{O}_{X_n}(nL))$ is base point free.
7. (C) Let $X$ be a projective scheme over $k$ and $\mathcal{L}$ invertible. Show that $\mathbf{B}(\mathcal{L}) = \mathbf{B}(\mathcal{L}^m)$ for every $m \geq 1$. Deduce that the stable base locus of a $\mathbb{Q}$-Cartier divisor is well defined.

### Lean

Mathlib has global sections of sheaves of modules on a scheme and the open sets $X_s$ for sections of the structure sheaf, `AlgebraicGeometry.Scheme.basicOpen`, but no linear systems or base loci. The statements of this section are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Linear systems go back to the Italian school, which studied families of curves on surfaces cut by hypersurfaces. The scheme form, with sections of an invertible sheaf, is Hartshorne, Section II.7. The literature state is theorem. In the minimal model program the stable base locus decides which curves a divisor cannot avoid. Section generation of $mK_X$ is the content of the base point free theorem of Volume 4, and the decomposition of $|V|$ into a fixed part and a moving part is the first step of Zariski's study of linear systems on surfaces and of the finite generation problem.
