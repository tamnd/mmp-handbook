---
title: Primary ideals and the uniqueness theorems
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch4, Mat86:ch2, Eis95:ch3]
requires: [P1.1, P1.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Primary ideals and the uniqueness theorems

### Statement

**Definition P1.2.25 (primary ideal).** An ideal $\mathfrak{q} \neq A$ is *primary* if $xy \in \mathfrak{q}$ and $x \notin \mathfrak{q}$ imply $y^n \in \mathfrak{q}$ for some $n \geq 1$. Equivalently, $A/\mathfrak{q} \neq 0$ and every zero divisor of $A/\mathfrak{q}$ is nilpotent. Then $\mathfrak{p} = \sqrt{\mathfrak{q}}$ is prime, and $\mathfrak{q}$ is called $\mathfrak{p}$-*primary*.

Lean: Mathlib `Ideal.IsPrimary` and `Ideal.isPrime_radical` (a definition and a theorem proved in Mathlib).

*Proof that the radical is prime.* $\sqrt{\mathfrak{q}} \neq A$ since $1 \notin \mathfrak{q}$. If $xy \in \sqrt{\mathfrak{q}}$, then $x^m y^m \in \mathfrak{q}$ for some $m$. Either $x^m \in \mathfrak{q}$, or $y^{mn} \in \mathfrak{q}$ for some $n$. So $x$ or $y$ is in $\sqrt{\mathfrak{q}}$. $\square$

**Example P1.2.26.** A prime ideal is primary. In $\mathbb{Z}$ the primary ideals are $(0)$ and $(p^n)$ for $p$ prime and $n \geq 1$.

**Example P1.2.27.** In $k[x, y]$ the ideal $\mathfrak{q} = (x, y^2)$ is primary: $k[x, y]/\mathfrak{q} \cong k[y]/(y^2)$, where the zero divisors are the multiples of $y$, which are nilpotent. Its radical is $\mathfrak{m} = (x, y)$, and $\mathfrak{m}^2 \subsetneq \mathfrak{q} \subsetneq \mathfrak{m}$. So a primary ideal need not be a power of its radical.

**Proposition P1.2.28 (radical maximal implies primary).** If $\sqrt{I}$ is a maximal ideal $\mathfrak{m}$, then $I$ is $\mathfrak{m}$-primary. In particular every power $\mathfrak{m}^n$ of a maximal ideal is $\mathfrak{m}$-primary.

Lean: Mathlib `Ideal.isPrimary_of_isMaximal_radical` (proved in Mathlib).

*Proof.* The image of $\mathfrak{m}$ in $A/I$ is the nilradical, and it is the only prime of $A/I$, by the theorem on the nilradical. So $A/I$ is local with maximal ideal $\mathfrak{m}/I$. Every element of $A/I$ is a unit or lies in $\mathfrak{m}/I$, and so it is a unit or nilpotent. A zero divisor is not a unit, so it is nilpotent. $\square$

A power of a prime need not be primary. Let $A = k[x, y, z]/(xy - z^2)$ and $\mathfrak{p} = (x, z)$, a prime with $A/\mathfrak{p} \cong k[y]$. Then $xy = z^2 \in \mathfrak{p}^2$. Here $x \notin \mathfrak{p}^2$, since $A$ is graded and $\mathfrak{p}^2$ lies in degrees $\geq 2$, and no power of $y$ lies in $\mathfrak{p}^2 \subseteq \mathfrak{p}$. So $\mathfrak{p}^2$ is not primary. Geometrically, $\operatorname{Spec} A$ is the quadric cone, $\mathfrak{p}$ is a line through the vertex, and $\mathfrak{p}^2$ has an embedded point at the vertex.

**Lemma P1.2.29 (primary ideals and quotients).** Let $\mathfrak{q}$ be $\mathfrak{p}$-primary.

1. If $\mathfrak{q}_1, \dots, \mathfrak{q}_n$ are $\mathfrak{p}$-primary, so is $\mathfrak{q}_1 \cap \dots \cap \mathfrak{q}_n$.
2. For $x \in A$: if $x \in \mathfrak{q}$ then $(\mathfrak{q} : x) = A$; if $x \notin \mathfrak{q}$ then $(\mathfrak{q} : x)$ is $\mathfrak{p}$-primary; if $x \notin \mathfrak{p}$ then $(\mathfrak{q} : x) = \mathfrak{q}$.

Here $(I : x) = \{a \in A : ax \in I\}$.

Lean: Mathlib `Ideal.IsPrimary.inf` and `Submodule.colon` (proved in Mathlib, and a definition).

*Proof.* For 1, the radical of the intersection is $\bigcap \sqrt{\mathfrak{q}_i} = \mathfrak{p}$. If $xy \in \bigcap \mathfrak{q}_i$ and $x \notin \bigcap \mathfrak{q}_i$, then $x \notin \mathfrak{q}_j$ for some $j$, so $y \in \sqrt{\mathfrak{q}_j} = \mathfrak{p}$, and a power of $y$ lies in the intersection. For 2, the first case is clear. Let $x \notin \mathfrak{q}$. If $y \in (\mathfrak{q} : x)$, then $xy \in \mathfrak{q}$ and $y \in \mathfrak{p}$. So $\mathfrak{q} \subseteq (\mathfrak{q} : x) \subseteq \mathfrak{p}$, and taking radicals gives $\sqrt{(\mathfrak{q} : x)} = \mathfrak{p}$. If $yz \in (\mathfrak{q} : x)$ with $y \notin \mathfrak{p}$, then $(xz)y \in \mathfrak{q}$, so $xz \in \mathfrak{q}$ and $z \in (\mathfrak{q} : x)$. This shows $(\mathfrak{q} : x)$ is $\mathfrak{p}$-primary. If $x \notin \mathfrak{p}$ and $xy \in \mathfrak{q}$, then $y \in \mathfrak{q}$, as no power of $x$ lies in $\mathfrak{q}$. $\square$

**Definition P1.2.30 (primary decomposition).** A *primary decomposition* of an ideal $I$ is an expression $I = \mathfrak{q}_1 \cap \dots \cap \mathfrak{q}_n$ with each $\mathfrak{q}_i$ primary. It is *minimal* if the radicals $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$ are distinct and no $\mathfrak{q}_i$ contains $\bigcap_{j \neq i} \mathfrak{q}_j$. An ideal with a primary decomposition is *decomposable*.

Lean: Mathlib `Submodule.IsMinimalPrimaryDecomposition` (a definition).

A decomposition can always be made minimal. First merge the $\mathfrak{q}_i$ with the same radical, which is allowed by part 1 of the lemma. Then drop the components that contain the intersection of the others.

**Example P1.2.31.** In $\mathbb{Z}$, $(60) = (4) \cap (3) \cap (5)$. In $k[x, y]$, $(xy) = (x) \cap (y)$: the union of the two axes.

**Example P1.2.32.** In $k[x, y]$, $(x^2, xy) = (x) \cap (x, y)^2$. Both components are primary, the radicals $(x)$ and $(x, y)$ differ, and neither component contains the other. So this is a minimal primary decomposition.

**Theorem P1.2.33 (first uniqueness theorem).** Let $I = \bigcap_{i=1}^n \mathfrak{q}_i$ be a minimal primary decomposition, with $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$. Then the $\mathfrak{p}_i$ are exactly the prime ideals among the ideals $\sqrt{(I : x)}$, $x \in A$. So the set $\{\mathfrak{p}_1, \dots, \mathfrak{p}_n\}$ depends only on $I$. It is called the set of primes *associated* to $I$.

Lean: Mathlib `Submodule.IsMinimalPrimaryDecomposition.image_radical_eq_associated_primes` (proved in Mathlib).

*Proof.* For $x \in A$, $(I : x) = \bigcap_i (\mathfrak{q}_i : x)$, so by part 2 of the lemma $\sqrt{(I : x)} = \bigcap_{x \notin \mathfrak{q}_i} \mathfrak{p}_i$. If this is a prime $\mathfrak{p}$, then $\mathfrak{p}$ contains the product of the $\mathfrak{p}_i$ in the intersection, hence one of them, and it is contained in each of them. So $\mathfrak{p} = \mathfrak{p}_i$ for some $i$. Conversely, by minimality there is $x_i \in \bigcap_{j \neq i} \mathfrak{q}_j$ with $x_i \notin \mathfrak{q}_i$, and then $\sqrt{(I : x_i)} = \mathfrak{p}_i$. $\square$

**Proposition P1.2.34 (minimal primes).** Let $I$ be decomposable, with associated primes $\mathfrak{p}_1, \dots, \mathfrak{p}_n$. Then $\sqrt{I} = \bigcap \mathfrak{p}_i$, and every prime $\mathfrak{p} \supseteq I$ contains some $\mathfrak{p}_i$. So the minimal elements of $\{\mathfrak{p}_1, \dots, \mathfrak{p}_n\}$ are the minimal primes over $I$, and $V(I) = V(\mathfrak{p}_1) \cup \dots \cup V(\mathfrak{p}_n)$.

Lean: Mathlib `Ideal.IsMinimalPrimaryDecomposition.minimalPrimes_subset_image_radical` and `Ideal.minimalPrimes` (proved in Mathlib, and a definition).

*Proof.* The radical of a finite intersection is the intersection of the radicals. If $\mathfrak{p} \supseteq I = \bigcap \mathfrak{q}_i \supseteq \prod \mathfrak{q}_i$, then $\mathfrak{p} \supseteq \mathfrak{q}_i$ for some $i$, and taking radicals, $\mathfrak{p} \supseteq \mathfrak{p}_i$. $\square$

The minimal elements are the *isolated* primes of $I$; the others are *embedded*. In the example $(x^2, xy) = (x) \cap (x, y)^2$, the prime $(x)$ is isolated and $(x, y)$ is embedded. The embedded component is not unique: also $(x^2, xy) = (x) \cap (x^2, y)$. The isolated components are unique, by the next theorem.

**Theorem P1.2.35 (second uniqueness theorem).** Let $I = \bigcap_{i=1}^n \mathfrak{q}_i$ be a minimal primary decomposition and let $\mathfrak{p}_i$ be an isolated prime. Then $\mathfrak{q}_i = \varphi^{-1}(IA_{\mathfrak{p}_i})$, where $\varphi: A \to A_{\mathfrak{p}_i}$. So the isolated primary components depend only on $I$.

Lean: Mathlib `Submodule.IsMinimalPrimaryDecomposition.comap_localized₀_eq_ite` (proved in Mathlib, in a form for all components).

*Proof.* Put $\mathfrak{p} = \mathfrak{p}_i$. For $j \neq i$, $\mathfrak{p}_j \not\subseteq \mathfrak{p}$, since $\mathfrak{p}$ is minimal among the associated primes and $\mathfrak{p}_j \neq \mathfrak{p}$. Pick $s \in \mathfrak{p}_j \setminus \mathfrak{p}$. Some power $s^m$ lies in $\mathfrak{q}_j$ and is a unit in $A_\mathfrak{p}$, so $\mathfrak{q}_j A_\mathfrak{p} = A_\mathfrak{p}$. Localization commutes with finite intersections (Section 2.1), so $IA_\mathfrak{p} = \bigcap_j \mathfrak{q}_j A_\mathfrak{p} = \mathfrak{q}_i A_\mathfrak{p}$. Finally $\varphi^{-1}(\mathfrak{q}_iA_\mathfrak{p}) = \mathfrak{q}_i$: if $a/1 \in \mathfrak{q}_iA_\mathfrak{p}$, then $sa \in \mathfrak{q}_i$ for some $s \notin \mathfrak{p}$, and $a \in \mathfrak{q}_i$ by part 2 of the lemma. $\square$

### Proof in words

A primary ideal is the algebraic form of an irreducible closed set with a structure of nilpotents spread evenly over it: every zero divisor of $A/\mathfrak{q}$ vanishes on all of $V(\mathfrak{q})$. A primary decomposition writes $I$ as an intersection of such pieces. The primes that occur are determined by $I$, since they are the primes of the form $\sqrt{(I : x)}$. Among them, the minimal ones give the irreducible components of $V(I)$, and their components are determined by localizing at the generic point of the component. The embedded primes are smaller closed sets inside a component, where $I$ carries extra nilpotents, and their components are not unique.

For the minimal model program, the embedded primes are the obstruction to good behaviour. A scheme has no embedded points if and only if the structure is determined by its generic points, and Serre's condition $S_1$ says exactly this. The condition $S_2$ of P1 Ch. 11 is the next step, and it is the condition that lets one extend sections over subsets of codimension two, which the MMP uses every time it defines $\mathcal{O}_X(D)$ for a Weil divisor $D$.

### Examples

**Example P1.2.36 (a line with an embedded point).** Let $I = (x^2, xy) \subseteq k[x, y]$. Then $V(I)$ is the line $x = 0$. The decomposition $I = (x) \cap (x, y)^2$ shows that $I$ is the ideal of the line with extra structure at the origin. The function $x$ vanishes on $V(I)$ and $x \notin I$, but $xy \in I$: $x$ is killed by $y$, which is not zero on the line. So $x$ is a nilpotent supported at the origin only, and $\sqrt{(I : x)} = (x, y)$ is the embedded prime. For each $\lambda \in k$ also $I = (x) \cap (x^2, y + \lambda x)$, which gives infinitely many minimal decompositions with the same isolated component $(x)$.

**Example P1.2.37 (three axes).** In $k[x, y, z]$, $(xy, yz, zx) = (x, y) \cap (y, z) \cap (z, x)$. All four ideals are generated by monomials, so a polynomial lies in one of them if and only if each of its monomials does, and it is enough to compare monomials. A monomial lies in all three ideals on the right if and only if it involves at least two of the variables, and that holds if and only if it is divisible by $xy$, $yz$ or $zx$. The ideal defines the union of the three coordinate axes, with no embedded points.

**Example P1.2.38 (a non-decomposable ideal).** Let $A = k[x_1, x_2, \dots]/(x_ix_j : i \neq j)$, the union of infinitely many coordinate axes through one point. For each $i$ the ideal $P_i = (x_j : j \neq i)$ is prime, with $A/P_i \cong k[x_i]$. Every prime of $A$ contains all the products $x_ix_j$, so it contains all the $x_j$ except at most one, and hence contains some $P_i$. So the $P_i$ are the minimal primes of $(0)$, and there are infinitely many. A decomposable ideal has only finitely many minimal primes, by the proposition on minimal primes. So $(0)$ is not decomposable. Section 2.4 shows that in a Noetherian ring every ideal is decomposable.

### Exercises

1. (A) Find minimal primary decompositions of $(x^2y) \subseteq k[x, y]$ and of $(x(x - 1), xy) \subseteq k[x, y]$. Describe the zero sets.
2. (A) Show that $(x^2, xy, y^2) = (x, y)^2$ is primary in $k[x, y]$ and that it equals $(x, y^2) \cap (x^2, y)$.
3. (A) Show that if $\mathfrak{q}$ is $\mathfrak{p}$-primary, then $\mathfrak{q}A_\mathfrak{p} \cap A = \mathfrak{q}$, and that $S^{-1}\mathfrak{q} = S^{-1}A$ if $S$ meets $\mathfrak{p}$.
4. (B) In $A = k[x, y, z]/(xy - z^2)$ with $\mathfrak{p} = (x, z)$ and $\mathfrak{m} = (x, y, z)$, show that $\mathfrak{p}^2 = (x) \cap \mathfrak{m}^2$, that this is a minimal primary decomposition, and that the $\mathfrak{p}$-primary component of $\mathfrak{p}^2$ is $(x)$.
5. (B) Let $\mathfrak{p}$ be prime. The $n$-th *symbolic power* is $\mathfrak{p}^{(n)} = \varphi^{-1}(\mathfrak{p}^nA_\mathfrak{p})$. Show that it is $\mathfrak{p}$-primary, and that it is the $\mathfrak{p}$-primary component of $\mathfrak{p}^n$ when $\mathfrak{p}^n$ is decomposable.
6. (B) Let $I$ be decomposable and $S$ multiplicative. Show that $S^{-1}I$ is decomposable in $S^{-1}A$, with associated primes the $S^{-1}\mathfrak{p}_i$ for the $\mathfrak{p}_i$ that miss $S$.
7. (C) Show that a radical decomposable ideal has no embedded primes, and that it is the intersection of its minimal primes.

### Lean

Mathlib defines primary ideals as `Ideal.IsPrimary`, the special case of `Submodule.IsPrimary`, with `Ideal.isPrime_radical`, `Ideal.isPrimary_of_isMaximal_radical` and `Ideal.IsPrimary.inf`. Minimal primary decompositions are `Submodule.IsMinimalPrimaryDecomposition`. The first uniqueness theorem is `Submodule.IsMinimalPrimaryDecomposition.image_radical_eq_associated_primes`, stated with the associated primes of Section 2.4, and the localization formula behind the second is `Submodule.IsMinimalPrimaryDecomposition.comap_localized₀_eq_ite`. The handbook adds no `MinimalModel` node here.

### Notes and history

Lasker proved the existence of primary decompositions in polynomial rings in 1905, motivated by the geometry of intersections, and Macaulay studied them for the elimination theory of 1916. Emmy Noether proved existence in every ring with the ascending chain condition in 1921, and she gave the uniqueness theorems in this generality. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 4. P1 Ch. 11 uses the absence of embedded primes as the condition $S_1$, and Volume 13 uses it for slc pairs.
