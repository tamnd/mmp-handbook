---
title: Rings, ideals and radicals
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch1, Mat86:ch1, Eis95:ch1]
requires: [P0.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Rings, ideals and radicals

### Statement

**Definition P1.1.1 (prime and maximal ideals).** Let $A$ be a ring. An ideal $\mathfrak{p} \subseteq A$ is *prime* if $\mathfrak{p} \neq A$ and $ab \in \mathfrak{p}$ implies $a \in \mathfrak{p}$ or $b \in \mathfrak{p}$. An ideal $\mathfrak{m}$ is *maximal* if $\mathfrak{m} \neq A$ and no ideal lies strictly between $\mathfrak{m}$ and $A$. Equivalently, $\mathfrak{p}$ is prime if and only if $A/\mathfrak{p}$ is an integral domain, and $\mathfrak{m}$ is maximal if and only if $A/\mathfrak{m}$ is a field. So a maximal ideal is prime.

Lean: Mathlib `Ideal.IsPrime` and `Ideal.IsMaximal` (classes in `Mathlib.RingTheory.Ideal.Prime` and `Mathlib.RingTheory.Ideal.Maximal`).

**Example P1.1.2.** In $\mathbb{Z}$ the prime ideals are $(0)$ and $(p)$ for $p$ a prime number, and the maximal ideals are the $(p)$. In $k[x]$ with $k$ a field the prime ideals are $(0)$ and $(f)$ for $f$ irreducible. When $k$ is algebraically closed the maximal ideals are the ideals $(x - a)$, one for each point $a$ of the line $\mathbb{A}^1$.

**Example P1.1.3.** In $k[x, y]$ with $k$ algebraically closed, the ideals $(0)$, $(f)$ with $f$ irreducible, and $(x - a, y - b)$ are prime. They correspond to the plane, the irreducible curve $V(f)$ and the point $(a, b)$. Chapter 2 shows that every prime ideal of $k[x, y]$ is of one of these three kinds. The ideal $(xy)$ is not prime: $x \cdot y \in (xy)$, and neither factor is in $(xy)$. Its zero set is the union of the two axes, which is not irreducible.

**Theorem P1.1.4 (Krull).** Let $A$ be a ring and let $I \neq A$ be an ideal. Then $I$ is contained in a maximal ideal of $A$. In particular a ring $A \neq 0$ has a maximal ideal, and every element of $A$ that is not a unit lies in a maximal ideal.

Lean: Mathlib `Ideal.exists_le_maximal` (proved in Mathlib).

*Proof.* Let $\Sigma$ be the set of ideals $J$ with $I \subseteq J \neq A$, ordered by inclusion. It is not empty, since $I \in \Sigma$. Let $(J_\lambda)$ be a chain in $\Sigma$. The union $J = \bigcup J_\lambda$ is an ideal, because any two elements of $J$ lie in one $J_\lambda$. It does not contain $1$, because no $J_\lambda$ does. So $J \in \Sigma$ is an upper bound of the chain. By Zorn's lemma $\Sigma$ has a maximal element $\mathfrak{m}$. An ideal strictly larger than $\mathfrak{m}$ contains $I$ and is not in $\Sigma$, so it is $A$. Thus $\mathfrak{m}$ is maximal. For the last claim, a nonunit $a$ generates an ideal $(a) \neq A$. $\square$

**Definition P1.1.5 (local ring).** A ring $A$ is *local* if it has exactly one maximal ideal $\mathfrak{m}$. The field $k = A/\mathfrak{m}$ is its *residue field*. One writes $(A, \mathfrak{m})$ or $(A, \mathfrak{m}, k)$.

Lean: Mathlib `IsLocalRing`, with maximal ideal `IsLocalRing.maximalIdeal` and residue field `IsLocalRing.ResidueField`.

**Proposition P1.1.6 (local rings).** Let $A$ be a ring and $\mathfrak{m} \neq A$ an ideal.

1. If every element of $A \setminus \mathfrak{m}$ is a unit, then $A$ is local with maximal ideal $\mathfrak{m}$.
2. If $\mathfrak{m}$ is maximal and every element of $1 + \mathfrak{m}$ is a unit, then $A$ is local.

Lean: Mathlib `IsLocalRing.of_nonunits_add` and `IsLocalRing.of_isUnit_or_isUnit_one_sub_self` (proved in Mathlib; they give two other forms of the criterion).

*Proof.* 1. A proper ideal consists of nonunits, so it lies in $\mathfrak{m}$. Hence $\mathfrak{m}$ is the only maximal ideal. 2. Let $x \notin \mathfrak{m}$. Since $\mathfrak{m}$ is maximal, $(x) + \mathfrak{m} = A$, so $xy + t = 1$ with $t \in \mathfrak{m}$. Then $xy = 1 - t \in 1 + \mathfrak{m}$ is a unit, so $x$ is a unit. Now apply 1. $\square$

**Example P1.1.7 (local rings).** A field is local with maximal ideal $0$. The ring $k[[x]]$ of formal power series is local with maximal ideal $(x)$, because a power series with nonzero constant term has an inverse. The ring $\mathbb{Z}_{(p)}$ of fractions $a/b$ with $p \nmid b$ is local with maximal ideal $p\mathbb{Z}_{(p)}$. The ring of rational functions on a variety that are regular at a point $P$ is local. Its maximal ideal is the set of functions that vanish at $P$. Chapter 2 constructs all of these rings by localization.

**Definition P1.1.8 (radicals).** An element $a \in A$ is *nilpotent* if $a^n = 0$ for some $n \geq 1$. The set $\operatorname{nil}(A)$ of nilpotent elements is the *nilradical*, and $A$ is *reduced* if $\operatorname{nil}(A) = 0$. The *radical* of an ideal $I$ is $\sqrt{I} = \{a \in A : a^n \in I \text{ for some } n\}$, and $I$ is *radical* if $I = \sqrt{I}$. The *Jacobson radical* $\operatorname{Jac}(A)$ is the intersection of all maximal ideals of $A$.

Lean: Mathlib `nilradical`, `Ideal.radical`, `Ideal.IsRadical`, `IsReduced` and `Ideal.jacobson` (the Jacobson radical of $A$ is `Ideal.jacobson ⊥`).

The nilradical is an ideal. If $a^m = 0$ and $b^n = 0$, every term of $(a + b)^{m + n - 1}$ in the binomial formula contains $a^i b^j$ with $i \geq m$ or $j \geq n$, so it is zero. The radical $\sqrt{I}$ is the inverse image of $\operatorname{nil}(A/I)$, so it is an ideal too.

**Theorem P1.1.9 (nilradical).** The nilradical of $A$ is the intersection of all prime ideals of $A$. For an ideal $I$, $\sqrt{I}$ is the intersection of the prime ideals that contain $I$.

Lean: Mathlib `nilradical_eq_sInf` and `Ideal.radical_eq_sInf` (proved in Mathlib).

*Proof.* A nilpotent element $a$ satisfies $a^n = 0 \in \mathfrak{p}$ for every prime $\mathfrak{p}$, so $a \in \mathfrak{p}$. Conversely let $f$ be not nilpotent. Let $\Sigma$ be the set of ideals $J$ with $f^n \notin J$ for all $n \geq 0$. It contains $0$, and the union of a chain in $\Sigma$ is in $\Sigma$. By Zorn's lemma $\Sigma$ has a maximal element $\mathfrak{p}$. It is a proper ideal since $f^0 = 1 \notin \mathfrak{p}$. Suppose $a \notin \mathfrak{p}$ and $b \notin \mathfrak{p}$. Then $\mathfrak{p} + (a)$ and $\mathfrak{p} + (b)$ are strictly larger than $\mathfrak{p}$, so they are not in $\Sigma$: $f^m \in \mathfrak{p} + (a)$ and $f^n \in \mathfrak{p} + (b)$ for some $m, n$. Then $f^{m+n} \in \mathfrak{p} + (ab)$, so $\mathfrak{p} + (ab) \notin \Sigma$ and $ab \notin \mathfrak{p}$. Thus $\mathfrak{p}$ is prime and $f \notin \mathfrak{p}$. For the second claim, apply the first to $A/I$, whose primes are the $\mathfrak{p}/I$ with $\mathfrak{p} \supseteq I$. $\square$

**Proposition P1.1.10 (Jacobson radical).** An element $x \in A$ is in $\operatorname{Jac}(A)$ if and only if $1 - xy$ is a unit for every $y \in A$.

Lean: Mathlib `Ideal.mem_jacobson_bot` (proved in Mathlib, in the form that $xy + 1$ is a unit for every $y$).

*Proof.* Let $x \in \operatorname{Jac}(A)$ and suppose $1 - xy$ is not a unit. By Krull's theorem it lies in a maximal ideal $\mathfrak{m}$. Also $xy \in \mathfrak{m}$, so $1 \in \mathfrak{m}$, which is false. Conversely suppose $x \notin \mathfrak{m}$ for some maximal $\mathfrak{m}$. Then $\mathfrak{m} + (x) = A$, so $t + xy = 1$ with $t \in \mathfrak{m}$. The element $1 - xy = t$ is not a unit. $\square$

**Proposition P1.1.11 (prime avoidance).** Let $\mathfrak{p}_1, \dots, \mathfrak{p}_n$ be prime ideals and let $I$ be an ideal with $I \subseteq \bigcup_{i} \mathfrak{p}_i$. Then $I \subseteq \mathfrak{p}_i$ for some $i$. Dually, if $I_1, \dots, I_n$ are ideals and $\mathfrak{p}$ is a prime with $\mathfrak{p} \supseteq \bigcap_i I_i$, then $\mathfrak{p} \supseteq I_i$ for some $i$, and if $\mathfrak{p} = \bigcap_i I_i$ then $\mathfrak{p} = I_i$ for some $i$.

Lean: Mathlib `Ideal.subset_union_prime` (proved in Mathlib, in a form that allows two of the ideals not to be prime).

*Proof.* Induction on $n$. The case $n = 1$ is clear. Let $n > 1$ and suppose $I \not\subseteq \mathfrak{p}_i$ for every $i$. By induction, for each $i$ the ideal $I$ is not in the union of the $\mathfrak{p}_j$ with $j \neq i$, so there is $x_i \in I$ with $x_i \notin \mathfrak{p}_j$ for all $j \neq i$. Then $x_i \in \mathfrak{p}_i$, since $I \subseteq \bigcup \mathfrak{p}_j$. Put $y = x_n + x_1 x_2 \cdots x_{n-1} \in I$. For $j < n$, $x_n \notin \mathfrak{p}_j$ and $x_1 \cdots x_{n-1} \in \mathfrak{p}_j$, so $y \notin \mathfrak{p}_j$. Also $x_n \in \mathfrak{p}_n$ and $x_1 \cdots x_{n-1} \notin \mathfrak{p}_n$, because $\mathfrak{p}_n$ is prime and no factor is in it. So $y \notin \mathfrak{p}_n$, a contradiction. For the dual claim, suppose $\mathfrak{p} \not\supseteq I_i$ for all $i$ and choose $x_i \in I_i \setminus \mathfrak{p}$. Then $x_1 \cdots x_n \in \prod I_i \subseteq \bigcap I_i \subseteq \mathfrak{p}$, so some $x_i \in \mathfrak{p}$, a contradiction. If $\mathfrak{p} = \bigcap I_i$, then $\mathfrak{p} \subseteq I_i \subseteq \mathfrak{p}$ for the $i$ just found. $\square$

**Theorem P1.1.12 (Chinese remainder theorem).** Let $I_1, \dots, I_n$ be ideals of $A$ with $I_i + I_j = A$ for $i \neq j$. Then $I_1 \cap \cdots \cap I_n = I_1 I_2 \cdots I_n$, and the map $A \to \prod_i A/I_i$ is surjective with kernel $\bigcap_i I_i$. So $A / \bigcap_i I_i \cong \prod_i A/I_i$.

Lean: Mathlib `Ideal.quotientInfRingEquivPiQuotient` (proved in Mathlib).

*Proof.* First let $n = 2$ and write $1 = a + b$ with $a \in I_1$, $b \in I_2$. For $c \in I_1 \cap I_2$, $c = ca + cb \in I_1 I_2$, and $I_1 I_2 \subseteq I_1 \cap I_2$ always. The element $b$ maps to $(1, 0)$ in $A/I_1 \times A/I_2$ and $a$ maps to $(0, 1)$, so the map is surjective. For $n > 2$, the ideal $I_1$ is comaximal with $J = I_2 \cdots I_n$: for each $i \geq 2$ write $1 = a_i + b_i$ with $a_i \in I_1$, $b_i \in I_i$. Then $1 = \prod_{i \geq 2}(a_i + b_i) \in I_1 + J$. By induction $J = I_2 \cap \cdots \cap I_n$ and $A/J \cong \prod_{i \geq 2} A/I_i$. The case $n = 2$ for $I_1$ and $J$ finishes the proof. $\square$

### Proof in words

Two tools carry this section. The first is Zorn's lemma, which produces maximal ideals and, applied to the ideals that avoid the powers of one element $f$, produces a prime ideal that does not contain $f$. So an element that is not nilpotent is nonzero in some integral domain $A/\mathfrak{p}$. The second is the identity $1 = a + b$ for comaximal ideals, which gives the idempotents of $A/(I \cap J)$ and proves the Chinese remainder theorem.

Geometrically, Krull's theorem says that a nonempty closed set of $\operatorname{Spec} A$ (Chapter 2) contains a closed point. The nilradical theorem says that a function that vanishes at every point is nilpotent, which is the algebraic heart of the Nullstellensatz of P0 Ch. 3. Prime avoidance says that if an ideal $I$ lies in no one of the primes $\mathfrak{p}_1, \dots, \mathfrak{p}_n$, then one element of $I$ lies in no one of them. So one function from $I$ can be chosen that vanishes identically on none of finitely many given irreducible closed sets. This is the form in which later chapters choose a general element. The Chinese remainder theorem says that functions can be prescribed independently on disjoint closed sets.

### Examples

**Example P1.1.13 (a ring with nilpotents).** Let $A = k[x, y]/(x^2, xy)$, with $k$ a field. The element $x$ is nonzero in $A$ and $x^2 = 0$, so $x \in \operatorname{nil}(A)$. The quotient $A/(x) = k[x, y]/(x) \cong k[y]$ is a domain, so $(x)$ is a prime of $A$ and $\operatorname{nil}(A) \subseteq (x)$. Hence $\operatorname{nil}(A) = (x)$ and $A_{\text{red}} = A/\operatorname{nil}(A) \cong k[y]$. The zero set of $(x^2, xy)$ in $\mathbb{A}^2$ is the line $x = 0$. The ring $A$ remembers more than the line: the function $x$ is zero on the line and is not zero in $A$. Chapter 2 shows that this extra structure sits at the origin, as an embedded point.

**Example P1.1.14 (radicals in $\mathbb{Z}$).** In $\mathbb{Z}/12$ the primes are $(2)$ and $(3)$, both maximal. So $\operatorname{nil}(\mathbb{Z}/12) = \operatorname{Jac}(\mathbb{Z}/12) = (6)$, and indeed $6^2 = 36 \equiv 0$. The Chinese remainder theorem gives $\mathbb{Z}/12 \cong \mathbb{Z}/4 \times \mathbb{Z}/3$. In $\mathbb{Z}$ itself the nilradical is $0$ and the Jacobson radical is also $0$, since no nonzero integer is divisible by every prime. In $k[[x]]$ the nilradical is $0$ and the Jacobson radical is $(x)$. So the two radicals can differ, and they differ for a local ring that is a domain and not a field.

**Example P1.1.15 (failure of prime avoidance).** The proposition needs the $\mathfrak{p}_i$ to be prime. Let $A = \mathbb{F}_2[x, y]/(x, y)^2$. Its maximal ideal $\mathfrak{m} = (x, y)$ has four elements $0, x, y, x + y$. It is the union of the three ideals $(x) = \{0, x\}$, $(y) = \{0, y\}$ and $(x + y) = \{0, x + y\}$, and it is contained in no one of them. Here none of the three ideals is prime. Over an infinite residue field this cannot happen: a vector space over an infinite field is not a finite union of proper subspaces.

**Example P1.1.16 (failure of the Chinese remainder theorem).** The comaximality is needed. In $k[x]$ take $I_1 = I_2 = (x)$. Then $I_1 \cap I_2 = (x)$, and $k[x]/(x) \cong k$ is not isomorphic to $k \times k$, since $k$ has no idempotents other than $0$ and $1$. Geometrically, the two closed sets $V(I_1)$ and $V(I_2)$ are the same point, so values cannot be prescribed on them independently. For $I_1 = (x)$ and $I_2 = (x^2)$ the product is $(x^3)$ and the intersection is $(x^2)$, so $I_1 \cap I_2 \neq I_1 I_2$.

### Exercises

1. (A) Find the nilradical and the Jacobson radical of $\mathbb{Z}/n$ for $n = 8, 30, 72$, and write each ring as a product of local rings by the Chinese remainder theorem.
2. (A) Let $x$ be a nilpotent element of $A$. Show that $1 + x$ is a unit. Deduce that the sum of a unit and a nilpotent element is a unit.
3. (A) Show that a polynomial $a_0 + a_1 t + \cdots + a_n t^n \in A[t]$ is a unit if and only if $a_0$ is a unit and $a_1, \dots, a_n$ are nilpotent. (Atiyah-Macdonald, Chapter 1, Exercise 2.)
4. (B) Show that the Jacobson radical of $A[t]$ equals its nilradical. (Hint: if $f$ is in the Jacobson radical, then $1 + tf$ is a unit; use Exercise 3.)
5. (B) Let $e \in A$ be an idempotent, $e^2 = e$. Show that $A \cong A/(e) \times A/(1 - e)$. Show that a local ring has no idempotents other than $0$ and $1$.
6. (B) Let $k$ be an infinite field and let $V$ be a vector space over $k$. Show that $V$ is not the union of finitely many proper subspaces. Use this to prove prime avoidance for ideals $\mathfrak{a}_1, \dots, \mathfrak{a}_n$ that need not be prime, in a ring that contains an infinite field.

### Lean

Mathlib has all the statements of this section. Prime and maximal ideals are the classes `Ideal.IsPrime` and `Ideal.IsMaximal`; Krull's theorem is `Ideal.exists_le_maximal`; the nilradical is `nilradical`, with `nilradical_eq_sInf`; the radical of an ideal is `Ideal.radical`, with `Ideal.radical_eq_sInf`; the Jacobson radical is `Ideal.jacobson`; prime avoidance is `Ideal.subset_union_prime`; the Chinese remainder theorem is `Ideal.quotientInfRingEquivPiQuotient`. The handbook adds no `MinimalModel` node here, and the map has no node for these results.

### Notes and history

Dedekind introduced ideals in the 1870s to restore unique factorization in rings of algebraic integers, and Emmy Noether gave the abstract theory of ideals in commutative rings in the 1920s. Krull proved the existence of maximal ideals in 1929 with a form of the axiom of choice. The Chinese remainder theorem goes back to Sunzi for integers. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 1. The Jacobson radical returns in Section 1.2 as the hypothesis of Nakayama's lemma, and in Chapter 3, where the Jacobson radical of an Artinian ring is nilpotent. For a finitely generated algebra over a field the two radicals agree. This is the Nullstellensatz in the form of a Jacobson ring, and Chapter 4 proves it.
