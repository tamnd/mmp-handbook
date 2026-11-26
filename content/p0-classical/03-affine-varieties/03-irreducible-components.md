---
title: Irreducible components and the dictionary
nodes: []
sources: [Rei88, Har77, Sha13]
reads_with: [Rei88:ch3, Har77:I.1, Sha13:ch1]
requires: [P1.3, P0.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Irreducible components and the dictionary

### Statement

**Definition P0.3.15 (irreducible space).** A topological space $X$ is irreducible if $X \neq \emptyset$ and $X$ is not the union $X = X_1 \cup X_2$ of two closed subsets $X_1, X_2 \neq X$. A subset of a space is irreducible if it is irreducible in the induced topology. An affine variety is an irreducible algebraic set in $\mathbb{A}^n$.

Lean: Mathlib `IsIrreducible` (a definition in `Mathlib.Topology.Irreducible`).

**Example P0.3.16.** The line $\mathbb{A}^1$ is irreducible, because its proper closed subsets are finite and $k$ is infinite.

**Example P0.3.17.** The set $V(xy) \subset \mathbb{A}^2$ is not irreducible: it is the union of the two axes $V(x)$ and $V(y)$, and each axis is a proper closed subset.

In an irreducible space, every nonempty open subset is dense, and two nonempty open subsets meet. To see this, let $U \neq \emptyset$ be open. Then $X = \overline{U} \cup (X \setminus U)$ is a union of two closed sets, and $X \setminus U \neq X$, so $\overline{U} = X$. An open subset of an irreducible space is irreducible, and the closure of an irreducible subset is irreducible.

**Proposition P0.3.18 (irreducible and prime).** Let $X \subseteq \mathbb{A}^n$ be an algebraic set. Then $X$ is irreducible if and only if $I(X)$ is a prime ideal.

Lean: Mathlib `PrimeSpectrum.isIrreducible_iff_vanishingIdeal_isPrime` (proved in Mathlib, for the spectrum of a ring; the classical form follows from the Nullstellensatz).

*Proof.* Suppose $X$ is irreducible and $fg \in I(X)$. Then $X = (X \cap V(f)) \cup (X \cap V(g))$, and both parts are closed in $X$. So one part is $X$, say $X \subseteq V(f)$, and then $f \in I(X)$. Also $I(X) \neq (1)$ because $X \neq \emptyset$. So $I(X)$ is prime. Conversely suppose $I(X)$ is prime and $X = X_1 \cup X_2$ with $X_1, X_2$ closed. Then $I(X) = I(X_1) \cap I(X_2)$. If $X_1 \neq X$ and $X_2 \neq X$, then $I(X_i) \neq I(X)$, because $V(I(X_i)) = X_i$. Choose $f \in I(X_1) \setminus I(X)$ and $g \in I(X_2) \setminus I(X)$. Then $fg \in I(X_1) \cap I(X_2) = I(X)$, which contradicts primality. Also $X \neq \emptyset$ since $I(X) \neq (1)$. So $X$ is irreducible. $\square$

**Definition P0.3.19 (Noetherian space).** A topological space $X$ is Noetherian if every descending chain of closed subsets $Z_1 \supseteq Z_2 \supseteq \cdots$ is eventually constant. Equivalently, every nonempty set of closed subsets has a minimal element.

Lean: Mathlib `TopologicalSpace.NoetherianSpace` (a class in `Mathlib.Topology.NoetherianSpace`).

**Example P0.3.20.** The space $\mathbb{A}^n$ is Noetherian: a descending chain of algebraic sets $Z_i$ gives an ascending chain of ideals $I(Z_i)$, which is eventually constant because $k[x_1, \dots, x_n]$ is Noetherian, and $Z_i = V(I(Z_i))$. Every subspace of a Noetherian space is Noetherian, so every algebraic set is Noetherian.

**Example P0.3.21.** A space with infinitely many points and the discrete topology is not Noetherian: for distinct points $p_1, p_2, \dots$ the closed sets $Z_i = X \setminus \{p_1, \dots, p_i\}$ form a strictly descending chain.

**Theorem P0.3.22 (irreducible decomposition).** Let $X$ be a Noetherian topological space and let $Z \subseteq X$ be a nonempty closed subset. Then there are irreducible closed subsets $Z_1, \dots, Z_r$ with

$$Z = Z_1 \cup \dots \cup Z_r, \qquad Z_i \not\subseteq Z_j \text{ for } i \neq j.$$

The sets $Z_i$ are unique up to order. They are the irreducible components of $Z$, that is, the maximal irreducible closed subsets of $Z$.

Lean: Mathlib `TopologicalSpace.NoetherianSpace.finite_irreducibleComponents` (proved in Mathlib: a Noetherian space has finitely many irreducible components).

*Proof.* Existence. Let $\Sigma$ be the set of nonempty closed subsets of $X$ that are not a finite union of irreducible closed subsets. Suppose $\Sigma \neq \emptyset$. Since $X$ is Noetherian, $\Sigma$ has a minimal element $W$. The set $W$ is not irreducible, so $W = W_1 \cup W_2$ with $W_1, W_2$ closed and different from $W$. If $W_i = \emptyset$, then $W = W_{3-i}$, which is false. So $W_1$ and $W_2$ are nonempty and smaller than $W$, hence not in $\Sigma$. Each is a finite union of irreducible closed subsets, so $W$ is one too. This is a contradiction, so $\Sigma = \emptyset$. Remove each $Z_i$ that lies in some other $Z_j$ to get the condition $Z_i \not\subseteq Z_j$.

Uniqueness. Suppose also $Z = Z'_1 \cup \dots \cup Z'_s$ with the same properties. Then $Z'_1 = \bigcup_i (Z'_1 \cap Z_i)$, a finite union of closed sets. Since $Z'_1$ is irreducible, $Z'_1 \subseteq Z_i$ for some $i$. By the same argument $Z_i \subseteq Z'_j$ for some $j$. So $Z'_1 \subseteq Z'_j$, hence $j = 1$ and $Z'_1 = Z_i$. Each $Z'_l$ is thus equal to some $Z_i$, and by symmetry the two lists agree up to order.

Maximality. Let $W \subseteq Z$ be irreducible and closed. As above $W \subseteq Z_i$ for some $i$. So every irreducible closed subset lies in some $Z_i$, and each $Z_i$ is maximal because $Z_i \not\subseteq Z_j$ for $j \neq i$. $\square$

**Corollary P0.3.23 (dictionary).** Let $k$ be algebraically closed. The maps $V$ and $I$ give inclusion reversing bijections:

1. between radical ideals of $k[x_1, \dots, x_n]$ and algebraic subsets of $\mathbb{A}^n$;
2. between prime ideals and irreducible algebraic subsets;
3. between maximal ideals and points.

Every radical ideal $J$ is a finite intersection $J = \mathfrak{p}_1 \cap \dots \cap \mathfrak{p}_r$ of prime ideals, and the minimal such $\mathfrak{p}_i$ correspond to the irreducible components of $V(J)$.

Lean: Mathlib `PrimeSpectrum.isIrreducible_zeroLocus_iff` (proved in Mathlib, for the spectrum of a ring).

*Proof.* For an algebraic set $X$, $V(I(X)) = X$ by the proposition on closures in Section 1. For a radical ideal $J$, $I(V(J)) = \sqrt{J} = J$ by the Nullstellensatz. This gives 1. Statement 2 is the proposition above. For 3, the maximal ideals are the ideals $\mathfrak{m}_a$, by the weak Nullstellensatz, and $V(\mathfrak{m}_a) = \{a\}$. For the last statement write $V(J) = Z_1 \cup \dots \cup Z_r$ as in the theorem. Then $J = I(V(J)) = I(Z_1) \cap \dots \cap I(Z_r)$, and each $I(Z_i)$ is prime. $\square$

### Proof in words

Irreducible means "not a union of two smaller closed pieces". An ideal is prime when a product lies in it only if a factor does, and the zero set of a product is the union of the zero sets. So the two conditions are one condition, read on the two sides of the dictionary. The decomposition into components uses only the Noetherian property: if some closed set has no finite decomposition, then there is a minimal such set, and splitting it once gives two smaller sets that do have decompositions. Uniqueness holds because an irreducible set inside a finite union of closed sets lies in one of them.

### Examples

The set $X = V(xz, yz) \subset \mathbb{A}^3$ is the union of the plane $V(z)$ and the line $V(x, y)$. Both are irreducible, because $(z)$ and $(x, y)$ are prime: the quotients $k[x, y]$ and $k[z]$ are domains. Neither contains the other. So these are the two irreducible components of $X$, and $(xz, yz) = (z) \cap (x, y)$. The components have different dimensions, 2 and 1.

For $f \in k[x_1, \dots, x_n]$ nonconstant, factor $f = c f_1^{m_1} \cdots f_r^{m_r}$ into distinct irreducible polynomials. The ring is a unique factorization domain, so each $(f_i)$ is prime, and $\sqrt{(f)} = (f_1 \cdots f_r)$. The irreducible components of the hypersurface $V(f)$ are $V(f_1), \dots, V(f_r)$. For example $V(x^2 y - x y^2) = V(x) \cup V(y) \cup V(x - y)$, three lines through the origin.

The twisted cubic $C = \{(t, t^2, t^3)\} \subset \mathbb{A}^3$ is irreducible. Its ideal is $I(C) = (y - x^2, z - x^3)$. Modulo this ideal every polynomial is equal to a polynomial in $x$ alone, and such a polynomial vanishes on $C$ only if it is $0$. So $k[x, y, z]/I(C) \cong k[x]$, a domain, and $I(C)$ is prime.

### Exercises

1. (A) Find the irreducible components of $V(x^2 - yz, xz - x) \subset \mathbb{A}^3$. (Hint: split into the cases $x = 0$ and $z = 1$.)
2. (A) Show that a Hausdorff space with at least two points is not irreducible. Show that every finite set of points in $\mathbb{A}^n$ with at least two points is reducible.
3. (A) Show that the closure of an irreducible subset of a topological space is irreducible, and that a nonempty open subset of an irreducible space is irreducible.
4. (B) Let $X$ be a Noetherian space. Show that every open subset of $X$ is quasi-compact, that is, every open cover has a finite subcover.
5. (B) Let $f, g \in k[x, y]$ be irreducible and not associate. Show that $V(f) \cap V(g)$ is finite, and deduce that the irreducible algebraic subsets of $\mathbb{A}^2$ are $\mathbb{A}^2$, the points, and the curves $V(f)$ with $f$ irreducible.
6. (B) Show that the ideal $(x^2, xy) \subset k[x, y]$ is not radical, compute its radical, and find primary ideals $\mathfrak{q}_1, \mathfrak{q}_2$ with $(x^2, xy) = \mathfrak{q}_1 \cap \mathfrak{q}_2$. Explain why this decomposition is not visible in $V(x^2, xy)$.

### Lean

Mathlib has irreducible sets (`IsIrreducible`), Noetherian spaces (`TopologicalSpace.NoetherianSpace`) and the finiteness of irreducible components (`TopologicalSpace.NoetherianSpace.finite_irreducibleComponents`). The link between irreducible closed sets and prime ideals is proved for the prime spectrum as `PrimeSpectrum.isIrreducible_iff_vanishingIdeal_isPrime`. The handbook uses these Mathlib names and adds no `MinimalModel` node here.

### Notes and history

The Noetherian condition is named after Emmy Noether, who in 1921 studied ascending chains of ideals and proved the primary decomposition in Noetherian rings. The decomposition into irreducible components is the geometric form of the statement that a radical ideal is a finite intersection of primes. Primary decomposition (Exercise 6) carries more information, namely the embedded components, and P3 uses it for schemes that are not reduced. The literature state of the theorem is theorem.
