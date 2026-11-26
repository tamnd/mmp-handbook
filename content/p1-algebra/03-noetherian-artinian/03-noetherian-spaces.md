---
title: Noetherian spaces and irreducible components
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch6, Mat86:ch1, Eis95:ch1]
requires: [P1.1, P1.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Noetherian spaces and irreducible components

### Statement

**Definition P1.3.17 (Noetherian space).** A topological space $X$ is *Noetherian* if every decreasing chain $Z_1 \supseteq Z_2 \supseteq \dots$ of closed subsets is eventually constant. Equivalently, every increasing chain of open subsets is eventually constant, and every nonempty set of closed subsets has a minimal element.

Lean: Mathlib `TopologicalSpace.NoetherianSpace` (definition).

**Proposition P1.3.18 (first properties).** Let $X$ be a Noetherian space. (a) Every subspace of $X$ is Noetherian. (b) Every subset of $X$ is quasi-compact. (c) (Noetherian induction.) Let $P$ be a property of closed subsets of $X$. Suppose that a closed set $Z$ has $P$ whenever every proper closed subset of $Z$ has $P$. Then every closed subset of $X$ has $P$.

Lean: Mathlib `TopologicalSpace.NoetherianSpace.set`, `TopologicalSpace.NoetherianSpace.isCompact` and `TopologicalSpace.noetherianSpace_iff_isCompact` (proved in Mathlib).

*Proof.* (a) A closed subset of a subspace $Y$ is $Y \cap Z$ for a closed $Z \subseteq X$, and it is $Y \cap \overline{Y \cap Z}$. So a decreasing chain of closed subsets of $Y$ comes from the decreasing chain of their closures in $X$, which stops. (b) By (a) it suffices to show that $X$ is quasi-compact. Let $(U_i)$ be an open cover. The set of finite unions of the $U_i$ has a maximal element $U$, by the ascending chain condition on opens. For every $i$, $U \cup U_i$ is a finite union containing $U$, so $U_i \subseteq U$, and $U = X$. (c) If some closed set fails $P$, the set of such closed sets has a minimal element $Z$. Every proper closed subset of $Z$ has $P$, so $Z$ has $P$, which is a contradiction. $\square$

**Theorem P1.3.19 (irreducible components).** Let $X$ be a Noetherian space. Every closed subset $Z \subseteq X$ is a finite union $Z = Z_1 \cup \dots \cup Z_r$ of irreducible closed subsets. If $Z_i \not\subseteq Z_j$ for $i \neq j$, the $Z_i$ are unique up to order, and they are the irreducible components of $Z$. In particular $X$ has finitely many irreducible components.

Lean: Mathlib `TopologicalSpace.NoetherianSpace.exists_finite_set_isClosed_irreducible` and `TopologicalSpace.NoetherianSpace.finite_irreducibleComponents` (proved in Mathlib).

*Proof.* Existence is by Noetherian induction. The empty set is the empty union. If $Z$ is irreducible, there is nothing to prove. If not, $Z = Z' \cup Z''$ with $Z', Z''$ proper closed subsets, and both are finite unions of irreducible closed sets by induction. For uniqueness, let $Z = Z_1 \cup \dots \cup Z_r = W_1 \cup \dots \cup W_s$ be two irredundant decompositions. Then $Z_1 = \bigcup_j (Z_1 \cap W_j)$, and since $Z_1$ is irreducible, $Z_1 \subseteq W_j$ for some $j$. In the same way $W_j \subseteq Z_i$ for some $i$. Then $Z_1 \subseteq Z_i$, so $i = 1$ and $Z_1 = W_j$. Induction on $r$ finishes the proof. Every irreducible closed subset $W \subseteq Z$ lies in some $Z_i$ by the same argument, so the $Z_i$ are the maximal irreducible closed subsets of $Z$, that is, its irreducible components. $\square$

P0 Ch. 3 states this theorem for algebraic sets in $\mathbb{A}^n$ and uses it there. The proof is the same.

**Theorem P1.3.20 (the spectrum of a Noetherian ring).** If $A$ is a Noetherian ring, then $\operatorname{Spec} A$ is a Noetherian space. Every closed subset $V(I)$ has finitely many irreducible components, namely the sets $V(\mathfrak{p})$ for the primes $\mathfrak{p}$ minimal over $I$. In particular $A$ has finitely many minimal primes.

Lean: Mathlib has the instance `TopologicalSpace.NoetherianSpace (PrimeSpectrum R)` for Noetherian `R`, and `minimalPrimes.finite_of_isNoetherianRing` and `Ideal.finite_minimalPrimes_of_isNoetherianRing` (proved in Mathlib).

*Proof.* By Section 2.2, $I \mapsto V(I)$ is an inclusion reversing bijection from radical ideals to closed subsets. A decreasing chain of closed subsets gives an increasing chain of radical ideals, which stops. By Section 2.2, $V(\mathfrak{p})$ is irreducible for a prime $\mathfrak{p}$, and the irreducible closed subsets are exactly these sets. So the components of $V(I)$ are the maximal sets $V(\mathfrak{p})$ inside $V(I)$, and these come from the minimal primes over $I$. $\square$

**Proposition P1.3.21 (powers of the radical).** Let $I$ be an ideal of a ring $A$ with $\sqrt{I}$ finitely generated. Then $(\sqrt{I})^n \subseteq I$ for some $n$. In particular, if $A$ is Noetherian, the nilradical of $A$ is nilpotent.

Lean: Mathlib `Ideal.exists_radical_pow_le_of_fg` and `IsNoetherianRing.isNilpotent_nilradical` (proved in Mathlib).

*Proof.* Let $\sqrt{I} = (a_1, \dots, a_k)$ with $a_i^{m} \in I$ for all $i$. The ideal $(\sqrt{I})^n$ is generated by the monomials $a_1^{e_1} \cdots a_k^{e_k}$ with $\sum e_i = n$. If $n \geq k(m - 1) + 1$, some $e_i \geq m$, so every such monomial lies in $I$. The nilradical is $\sqrt{0}$. $\square$

### Proof in words

A Noetherian ring has a Noetherian spectrum, because closed sets correspond to radical ideals with the order reversed. In a Noetherian space, an induction on closed subsets works: assume the result for all proper closed subsets and prove it for the whole. This gives the decomposition of every closed set into finitely many irreducible pieces. On the ring side, these pieces are the minimal primes over an ideal.

For varieties, every algebraic set is a finite union of irreducible varieties, and an affine variety has finitely many components. In the MMP, many sets are closed: the exceptional locus of a morphism, the non-klt locus of a pair, the stable base locus of a divisor. Each of them has finitely many irreducible components, and arguments often treat one component at a time. Noetherian induction also gives stratifications: a property that holds on a dense open subset of every irreducible closed set holds on each stratum of a finite partition into locally closed pieces.

### Examples

**Example P1.3.22 (the spectrum of $\mathbb{Z}$).** The closed subsets of $\operatorname{Spec} \mathbb{Z}$ are the whole space and the finite sets of nonzero primes. A decreasing chain of these stops, so $\operatorname{Spec} \mathbb{Z}$ is Noetherian, and it is irreducible with generic point $(0)$.

**Example P1.3.23 (a plane and a line).** In $\mathbb{A}^3$ take $Z = V(xz, yz)$. A point lies in $Z$ when $z = 0$, or when $x = y = 0$. So $Z = V(z) \cup V(x, y)$, the union of a plane and a line meeting at the origin. In the ring $k[x, y, z]$, $(xz, yz) = (z) \cap (x, y)$, and the minimal primes over $(xz, yz)$ are $(z)$ and $(x, y)$.

**Example P1.3.24 (a non-Noetherian ring with a Noetherian spectrum).** The ring $A = k[x_1, x_2, \dots]/(x_1, x_2, \dots)^2$ of Section 3.1 has one prime, so $\operatorname{Spec} A$ is a point and is Noetherian. But $A$ is not Noetherian. The spectrum only sees radical ideals, and the nilpotent structure of $A$ is where the chain condition fails.

**Example P1.3.25 (a non-Noetherian spectrum).** For $A = k[x_1, x_2, \dots]$, the closed sets $V(x_1) \supsetneq V(x_1, x_2) \supsetneq \dots$ form a chain that does not stop. So $\operatorname{Spec} A$ is not Noetherian.

### Exercises

1. (A) Show that a Noetherian Hausdorff space is finite and discrete.
2. (A) Find the irreducible components of $V(xy, xz, yz) \subseteq \mathbb{A}^3$ and of $V(x^2 - yz, xz - x) \subseteq \mathbb{A}^3$, and the minimal primes over the two ideals.
3. (B) Show that $\operatorname{Spec} A$ is Noetherian if and only if the radical ideals of $A$ satisfy the ascending chain condition.
4. (B) Let $X$ be a Noetherian space with irreducible components $Z_1, \dots, Z_r$. Show that $U = X \setminus \bigcup_{i \neq j} (Z_i \cap Z_j)$ is open and dense, and that $U$ is the disjoint union of the open sets $U \cap Z_i$.
5. (C) Let $A$ be a ring with $\operatorname{Spec} A$ Noetherian. Show that every prime $\mathfrak{p}$ of $A$ is the radical of a finitely generated ideal. (Hint: take a maximal element among the radicals $\sqrt{J}$ with $J \subseteq \mathfrak{p}$ finitely generated.)

### Lean

Mathlib defines `TopologicalSpace.NoetherianSpace` through the well-foundedness of the open subsets. The decomposition into irreducible closed sets is `TopologicalSpace.NoetherianSpace.exists_finite_set_isClosed_irreducible`, and the finiteness of `irreducibleComponents` is `TopologicalSpace.NoetherianSpace.finite_irreducibleComponents`. The spectrum of a Noetherian ring is a Noetherian space by an instance on `PrimeSpectrum`. The nilradical of a Noetherian ring is nilpotent by `IsNoetherianRing.isNilpotent_nilradical`. The handbook adds no `MinimalModel` node here.

### Notes and history

The decomposition of an algebraic set into irreducible components goes back to Lasker and Noether, in the language of ideals. Noetherian spaces and Noetherian induction in this form appear in the work of Zariski, Serre and Grothendieck, who used them in the theory of schemes. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 6, and Matsumura, Chapter 1.
