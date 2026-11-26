---
title: Canonical surface singularities are Du Val
nodes: []
sources: [DuV34, Art66, KM98, Rei87]
reads_with: [KM98:ch4, Rei87:ch4]
requires: [P8.10, 4.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Canonical surface singularities are Du Val

### Statement

A *$(-2)$-curve* is a smooth rational curve $E$ with $E^2 = -2$. By adjunction, $K_Y \cdot E = 0$ for such a curve. A normal surface singularity is a *Du Val singularity* if every exceptional curve of its minimal resolution is a $(-2)$-curve. This section proves that the canonical surface singularities are exactly the Du Val singularities, and that their resolution graphs are the Dynkin diagrams $A_n$, $D_n$, $E_6$, $E_7$, $E_8$.

The *dual graph* of the exceptional curves has a vertex for each $E_i$ and $E_i \cdot E_j$ edges between $E_i$ and $E_j$ for $i \ne j$.

**Theorem 4.3.11 (canonical surface singularities).** Let $(X, x)$ be a normal surface germ with $K_X$ $\mathbb{Q}$-Cartier, and $f \colon Y \to X$ its minimal resolution. The following are equivalent.

1. $X$ is canonical.
2. $f$ is crepant: $K_Y = f^* K_X$.
3. Every exceptional curve of $f$ is a $(-2)$-curve.

In this case the exceptional curves meet pairwise transversally in at most one point, no three pass through a point, and $f$ is a log resolution of $(X, 0)$.

Lean: not yet in Lean.

**Proposition 4.3.12 (the graphs of Du Val singularities).** The dual graph of the exceptional curves of a Du Val singularity is a tree with simple edges, and it is one of the Dynkin diagrams $A_n$ ($n \ge 1$), $D_n$ ($n \ge 4$), $E_6$, $E_7$, $E_8$.

Lean: not yet in Lean.

The proposition finds the possible graphs from negative definiteness alone. The next theorem, which this volume uses as a black box, says that each graph occurs, for exactly one singularity, and gives the equations.

**Theorem 4.3.13 (the ADE classification).** Over $\mathbb{C}$, the Du Val singularities are, up to analytic isomorphism, the hypersurface germs at the origin of $\mathbb{C}^3$

| type | equation | group $G \subset SL_2(\mathbb{C})$ |
|---|---|---|
| $A_n$, $n \ge 1$ | $x^2 + y^2 + z^{n+1} = 0$ | cyclic of order $n + 1$ |
| $D_n$, $n \ge 4$ | $x^2 + y^2 z + z^{n-1} = 0$ | binary dihedral of order $4(n-2)$ |
| $E_6$ | $x^2 + y^3 + z^4 = 0$ | binary tetrahedral, order 24 |
| $E_7$ | $x^2 + y^3 + y z^3 = 0$ | binary octahedral, order 48 |
| $E_8$ | $x^2 + y^3 + z^5 = 0$ | binary icosahedral, order 120 |

The resolution graph of each is the Dynkin diagram of its name, and each is isomorphic to $\mathbb{C}^2 / G$ for the finite subgroup $G$ of $SL_2(\mathbb{C})$ in the last column. Every finite subgroup of $SL_2(\mathbb{C})$ is conjugate to one of these. In particular every Du Val singularity is Gorenstein, a quotient singularity, and a rational singularity.

Lean: not yet in Lean.

This is the work of Du Val (DuV34), and of Artin (Art66), who proved that the rational double points are the Du Val singularities. KM98, Chapter 4, gives a proof.

### Proof in words

On the minimal resolution every discrepancy is at most 0 (Section 3.1). Canonical means every discrepancy is at least 0. So canonical forces every discrepancy on the minimal resolution to be 0, and then adjunction with $K_Y \cdot E = 0$ and $E^2 < 0$ leaves only $(-2)$-curves. Conversely, $(-2)$-curves have $K_Y \cdot E = 0$, so the numerical discrepancies solve a linear system with right side 0, and negative definiteness gives 0. The configuration of $(-2)$-curves is snc because any bad configuration, two curves meeting twice, three curves through a point, or a cycle, gives a nonzero divisor of square at least 0. So $f$ is a log resolution with $\Delta_Y = 0$, and Section 2.2 gives $\operatorname{discrep} = 0$.

For the graphs, the same trick rules out every graph that contains one of the extended Dynkin diagrams $\tilde A_n$, $\tilde D_n$, $\tilde E_6$, $\tilde E_7$, $\tilde E_8$: each carries a positive divisor $N$ with $N \cdot E = 0$ for every curve $E$ in it, so $N^2 = 0$. A tree that contains none of them is a Dynkin diagram.

### Examples

**Example 4.3.14 (the $A_n$ singularity, two ways).** Let $X = \{xy = z^{n+1}\}$. Exercise 5 of Section 1.1 resolves it by blow-ups: each blow-up of the singular point adds two $(-2)$-curves, or one at the last step, and the result is a chain of $n$ curves with $a = 0$, as in Example 4.3.8. So $X$ is canonical and not terminal. In Volume 3, $X$ is the toric variety of $\operatorname{Cone}(e_2, (n+1)e_1 - n e_2)$, the quotient $\frac{1}{n+1}(1, n)$. The equations $\langle m, e_2 \rangle = 1$ and $\langle m, (n+1)e_1 - n e_2 \rangle = 1$ give $m_\sigma = (1, 1)$. The rays of the minimal resolution are $(k, 1 - k)$ for $1 \le k \le n$, and $\langle m_\sigma, (k, 1-k) \rangle - 1 = 0$, so Volume 3, Theorem 3.3.34, gives $a = 0$ for every exceptional curve.

**Example 4.3.15 (the $D_4$ singularity).** Let $X = \{x^2 + y^3 + z^3 = 0\}$. The cubic $y^3 + z^3$ is a product of three distinct linear forms, so this is the $D_4$ singularity after a linear change of coordinates. Blow up the origin. The tangent cone is the double plane $x^2 = 0$, so the exceptional set of the strict transform is one line $E_0$. The strict transform has three $A_1$ points on $E_0$, at the zeros of $y^3 + z^3$ on $E_0$ (Problem 3). Their resolutions add three $(-2)$-curves, each meeting $E_0$ once. The graph is the star with centre $E_0$ and three arms of length 1, the diagram $D_4$, and $E_0^2 = -2$.

**Counterexample 4.3.16 (a klt germ that is not Du Val).** For $\frac15(1,2)$ the minimal resolution has a $(-3)$-curve, and its discrepancies are $-\frac25$ and $-\frac15$ (Example 4.3.10). It is klt and not canonical. Its index is 5, as in Volume 3, Chapter 3: no multiple $mK_X$ with $1 \le m \le 4$ is Cartier.

**Counterexample 4.3.17 (Gorenstein, not Du Val).** The cone over a plane cubic has $K_X$ Cartier, and its minimal resolution has one elliptic curve with $E^2 = -3$. It is not canonical: $a = -1$ (Example 4.2.22). So Gorenstein alone does not imply Du Val. With klt it does (Exercise 6).

### Proof

*The theorem.* Let $a_i$ be the discrepancies on the minimal resolution. By Proposition 4.3.5, $a_i \le 0$.

$1 \Rightarrow 2$. If $X$ is canonical, $a_i \ge 0$, so $a_i = 0$ for every $i$, and $K_Y = f^*K_X$.

$2 \Rightarrow 3$. If $a_i = 0$ for every $i$, then $K_Y \cdot E_i = f^*K_X \cdot E_i = 0$. Adjunction gives $E_i^2 = 2p_a(E_i) - 2$, and $E_i^2 < 0$, so $p_a(E_i) = 0$ and $E_i^2 = -2$. An integral curve with $p_a = 0$ is a smooth rational curve.

$3 \Rightarrow 2$. Each $E_i$ has $K_Y \cdot E_i = -2 - E_i^2 = 0$. Write $K_Y = f^*K_X + A$ with $A = \sum_j a_j E_j$. Then $A \cdot E_i = K_Y \cdot E_i = 0$ for every $i$, so $A^2 = 0$, and $A = 0$ by Theorem 4.3.1.

$2$ and $3 \Rightarrow 1$. First the configuration. Let $E_1$, $E_2$ be distinct exceptional curves. Then
$$(E_1 + E_2)^2 = -4 + 2 E_1 \cdot E_2 < 0,$$
so $E_1 \cdot E_2 \le 1$: two curves meet at most once, and transversally. If $E_1$, $E_2$, $E_3$ pass through one point, they meet pairwise, and
$$(E_1 + E_2 + E_3)^2 = -6 + 2(E_1 \cdot E_2 + E_1 \cdot E_3 + E_2 \cdot E_3) = 0,$$
which contradicts negative definiteness. The same computation shows that the graph has no cycle: for a cycle $E_1, \dots, E_k$ with $k \ge 3$, $\big(\sum_i E_i\big)^2 \ge -2k + 2k = 0$. So the exceptional curves are smooth, meet transversally, and no three meet at a point. The exceptional set is a divisor with simple normal crossings, and $f$ is a log resolution of $(X, 0)$ with $\Delta_Y = 0$ by 2. By Theorem 4.2.14 and Theorem 4.2.12,
$$\operatorname{discrep}(X, 0) = \min\{0, \operatorname{discrep}(Y, 0)\} = \min\{0, 1\} = 0.$$
So $X$ is canonical, and the last claim of the theorem is proved on the way.

*The proposition.* The theorem shows that the graph is a simple graph with no cycles, and $f^{-1}(x)$ is connected, so it is a tree. The matrix of a subset of the curves is a principal submatrix of $M$, so it is also negative definite. Hence the graph contains no subgraph that carries a nonzero divisor $N = \sum n_i E_i$ with $N^2 \ge 0$. The following divisors have $N \cdot E_i = 0$ for every curve $E_i$ in their support, so $N^2 = 0$. In each, the numbers are the coefficients $n_i$, and every curve is a $(-2)$-curve, so $N \cdot E_i = -2n_i + \sum_{j \text{ adjacent}} n_j$.

- $\tilde D_4$: a centre with coefficient 2 and four neighbours with coefficient 1. So no vertex has four or more neighbours.
- $\tilde D_n$ for $n \ge 5$: two vertices of valence 3, joined by a chain, all with coefficient 2, and the four end vertices with coefficient 1. So there is at most one vertex of valence 3.
- $\tilde E_6$: a centre with coefficient 3, three arms of two vertices with coefficients 2, 1.
- $\tilde E_7$: a centre with coefficient 4, one arm of one vertex with coefficient 2, and two arms of three vertices with coefficients 3, 2, 1.
- $\tilde E_8$: a centre with coefficient 6, an arm of one vertex with coefficient 3, an arm of two vertices with coefficients 4, 2, and an arm of five vertices with coefficients 5, 4, 3, 2, 1.

So the tree is a chain, which is $A_n$, or it has one vertex of valence 3 with three arms of $p \le q \le r$ vertices. By $\tilde E_6$, $p = 1$. If $q = 1$, the graph is $D_n$. If $q \ge 3$, it contains $\tilde E_7$. So $q = 2$, and $r \le 4$ by $\tilde E_8$: the graph is $E_6$, $E_7$ or $E_8$ for $r = 2, 3, 4$. $\square$

### Exercises

1. (A) Check that each divisor $N$ in the proof of the proposition has $N \cdot E_i = 0$ for every curve of its support.
2. (A) Show that the intersection matrix of the chain $A_n$ of $(-2)$-curves has determinant $(-1)^n (n+1)$. Compare with the order of the group $\mathbb{Z}/(n+1)$ in the table.
3. (B) Resolve $\{xy = z^3\}$ by one blow-up and one more blow-up, and check that the exceptional set is two $(-2)$-curves meeting once.
4. (B) Show that $D_4$ is $\mathbb{C}^2 / Q_8$, where $Q_8 \subset SL_2(\mathbb{C})$ is the quaternion group of order 8, by checking that the invariants $u = (xy)^2$, $v = x^4 + y^4$ and $w = xy(x^4 - y^4)$ satisfy one relation. Find it.
5. (B) Show that a $(-2)$-curve $E_0$ meeting four disjoint $(-2)$-curves once each cannot be the exceptional set of a resolution. Now let $E_0^2 = -3$ instead. Show by the method of Theorem 4.3.1 that the matrix is negative definite, and that the numerical discrepancies are $-1$ for $E_0$ and $-\frac12$ for the other four curves.
6. (C) Let $(X, x)$ be a klt surface germ with $K_X$ Cartier. Show that every discrepancy on the minimal resolution is an integer in $(-1, 0]$, and deduce that $X$ is Du Val. This is the step of Section 3.3 that identifies the index one cover.

### Lean

The theorems of this section are not yet in Lean. `MinimalModel.IsCanonical` states condition 1 for any variety, and the names of the other conditions are not yet in the library.

### Notes and history

Du Val (DuV34) studied the singularities that "do not affect the conditions of adjunction", which are the canonical ones in the language of this section, and found the ADE list. Artin (Art66) characterized them as the rational double points, and Brieskorn (Bri68) related them to the quotients by subgroups of $SL_2$ and to simple Lie algebras. Reid's name "canonical" comes from the generalization to higher dimension (Rei80). The ADE list appears again in Chapter 4: the general hyperplane section through a terminal 3-fold singularity of index 1 is a Du Val singularity.
