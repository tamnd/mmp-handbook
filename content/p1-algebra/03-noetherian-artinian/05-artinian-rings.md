---
title: Artinian rings
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch8, Mat86:ch1, Eis95:ch2]
requires: [P1.1, P1.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Artinian rings

### Statement

**Proposition P1.3.33 (primes in an Artinian ring).** Let $A$ be an Artinian ring. Then every prime ideal of $A$ is maximal, $A$ has finitely many maximal ideals, and the nilradical of $A$, which equals its Jacobson radical, is nilpotent.

Lean: Mathlib `IsArtinianRing.isMaximal_of_isPrime`, `IsArtinianRing.setOfPred_isMaximal_finite`, `IsArtinianRing.isNilpotent_jacobson_bot` and `IsArtinianRing.isNilpotent_nilradical` (proved in Mathlib).

*Proof.* Let $\mathfrak{p}$ be prime. Then $B = A/\mathfrak{p}$ is an Artinian domain. For $x \neq 0$ in $B$ the chain $(x) \supseteq (x^2) \supseteq \dots$ stops, so $x^n = x^{n+1}y$ for some $n$ and $y$. Cancelling $x^n$ gives $xy = 1$. So $B$ is a field and $\mathfrak{p}$ is maximal.

For finiteness, the set of finite intersections $\mathfrak{m}_1 \cap \dots \cap \mathfrak{m}_r$ of maximal ideals has a minimal element. For every maximal $\mathfrak{m}$, then $\mathfrak{m} \cap \mathfrak{m}_1 \cap \dots \cap \mathfrak{m}_r = \mathfrak{m}_1 \cap \dots \cap \mathfrak{m}_r$, so $\mathfrak{m} \supseteq \mathfrak{m}_1 \cdots \mathfrak{m}_r$. As $\mathfrak{m}$ is prime, $\mathfrak{m} \supseteq \mathfrak{m}_i$ for some $i$, and $\mathfrak{m} = \mathfrak{m}_i$.

Since all primes are maximal, the nilradical $\mathfrak{N}$ equals the Jacobson radical (Section 1.1). The chain $\mathfrak{N} \supseteq \mathfrak{N}^2 \supseteq \dots$ stops at some $I = \mathfrak{N}^k = \mathfrak{N}^{k+1} = \dots$, and $I^2 = I$. Suppose $I \neq 0$. The set of ideals $\mathfrak{a}$ with $\mathfrak{a} I \neq 0$ contains $I$, so it has a minimal element $\mathfrak{a}$. Choose $x \in \mathfrak{a}$ with $xI \neq 0$. Then $(x) \subseteq \mathfrak{a}$ is in the set, so $\mathfrak{a} = (x)$. Also $(xI) I = xI \neq 0$ and $xI \subseteq (x)$, so $xI = (x)$ by minimality. Hence $x = xy$ for some $y \in I$, and then $x = xy = xy^2 = \dots = xy^m$ for all $m$. Since $y$ is nilpotent, $x = 0$, which contradicts $xI \neq 0$. So $I = 0$. $\square$

**Lemma P1.3.34 (a product of maximal ideals is zero).** Let $A$ be a ring with $\mathfrak{m}_1 \mathfrak{m}_2 \cdots \mathfrak{m}_n = 0$ for some maximal ideals $\mathfrak{m}_i$, not necessarily distinct. Then $A$ is Noetherian if and only if it is Artinian.

Lean: not in Lean in this form; Mathlib reaches the same result through `IsSemiprimaryRing` in its proof of the Hopkins-Levitzki theorem.

*Proof.* Consider the chain $A \supseteq \mathfrak{m}_1 \supseteq \mathfrak{m}_1\mathfrak{m}_2 \supseteq \dots \supseteq \mathfrak{m}_1 \cdots \mathfrak{m}_n = 0$. Each quotient $V_i = \mathfrak{m}_1 \cdots \mathfrak{m}_{i-1}/\mathfrak{m}_1 \cdots \mathfrak{m}_i$ is killed by $\mathfrak{m}_i$, so it is a vector space over $A/\mathfrak{m}_i$, and its $A$-submodules are its subspaces. For a vector space, the ascending chain condition and the descending chain condition both mean finite dimension. By the proposition on exact sequences in Section 3.1, applied $n$ times, $A$ is Noetherian if and only if all $V_i$ have finite dimension, if and only if $A$ is Artinian. $\square$

**Theorem P1.3.35 (Akizuki-Hopkins).** A ring $A$ is Artinian if and only if it is Noetherian and every prime ideal is maximal, that is, $\dim A = 0$.

Lean: Mathlib `isArtinianRing_iff_isNoetherianRing_krullDimLE_zero`, and the instance from `IsArtinianRing` to `IsNoetherianRing` (proved in Mathlib).

*Proof.* Let $A$ be Artinian with maximal ideals $\mathfrak{m}_1, \dots, \mathfrak{m}_r$ and nilradical $\mathfrak{N}$, with $\mathfrak{N}^k = 0$. Then $(\mathfrak{m}_1 \cdots \mathfrak{m}_r)^k \subseteq (\mathfrak{m}_1 \cap \dots \cap \mathfrak{m}_r)^k = \mathfrak{N}^k = 0$, and the lemma shows that $A$ is Noetherian. Conversely, let $A$ be Noetherian of dimension $0$. By Section 3.3 it has finitely many minimal primes $\mathfrak{p}_1, \dots, \mathfrak{p}_r$, and these are maximal. The nilradical $\mathfrak{N} = \mathfrak{p}_1 \cap \dots \cap \mathfrak{p}_r$ is nilpotent by Section 3.3, so $(\mathfrak{p}_1 \cdots \mathfrak{p}_r)^k = 0$ for some $k$, and the lemma shows that $A$ is Artinian. $\square$

**Theorem P1.3.36 (structure of Artinian rings).** Let $A$ be Artinian with maximal ideals $\mathfrak{m}_1, \dots, \mathfrak{m}_r$, and let $k$ be such that the nilradical satisfies $\mathfrak{N}^k = 0$. Then
$$
A \cong A/\mathfrak{m}_1^k \times \dots \times A/\mathfrak{m}_r^k ,
$$
each $A/\mathfrak{m}_i^k$ is a local Artinian ring, and $A/\mathfrak{m}_i^k \cong A_{\mathfrak{m}_i}$. The decomposition of $A$ as a finite product of local rings is unique up to order and isomorphism.

Lean: Mathlib `IsArtinianRing.quotNilradicalPowEquivPi`, which gives $A/\mathfrak{N}^n \cong \prod_i A/\mathfrak{m}_i^n$, and `IsArtinianRing.equivPi` in the reduced case (proved in Mathlib).

*Proof.* For $i \neq j$ the ideals $\mathfrak{m}_i^k$ and $\mathfrak{m}_j^k$ are comaximal: a maximal ideal containing both contains $\mathfrak{m}_i$ and $\mathfrak{m}_j$, so it equals both. By the Chinese remainder theorem of Section 1.1, $\bigcap_i \mathfrak{m}_i^k = \prod_i \mathfrak{m}_i^k \subseteq \mathfrak{N}^k = 0$, and $A \to \prod_i A/\mathfrak{m}_i^k$ is an isomorphism. The ring $A/\mathfrak{m}_i^k$ is Artinian and its primes are the primes containing $\mathfrak{m}_i^k$, that is, $\mathfrak{m}_i$ only. The idempotent $e_i$ that is $1$ in the factor $A/\mathfrak{m}_i^k$ and $0$ in the others is not in $\mathfrak{m}_i$, so it becomes a unit in $A_{\mathfrak{m}_i}$. It kills the other factors, so $A_{\mathfrak{m}_i} \cong (A/\mathfrak{m}_i^k)_{\mathfrak{m}_i}$. This is $A/\mathfrak{m}_i^k$, since the elements outside $\mathfrak{m}_i$ are already units in this local ring. For uniqueness, if $A \cong \prod_j B_j$ with $B_j$ local, the primes of $A$ correspond to the maximal ideals of the factors, one for each $j$, and $B_j$ is the localization of $A$ at the corresponding prime. $\square$

### Proof in words

An Artinian domain is a field, because a decreasing chain of powers of an element must stop. So every prime of an Artinian ring is maximal, and a minimal intersection argument shows that there are finitely many. The nilradical is nilpotent, so some product of maximal ideals is zero. A ring with this property is filtered by vector spaces, and for vector spaces the two chain conditions agree. So Artinian means Noetherian of dimension $0$. Finally, the Chinese remainder theorem splits an Artinian ring into its local rings at its finitely many points.

Geometrically, $\operatorname{Spec} A$ of an Artinian ring is a finite discrete set of points, and each point carries a local Artinian ring, a fat point. A finite $k$-algebra is Artinian, so the fibre of a finite morphism over a point is a finite union of fat points. The length of the fibre is its degree, and the sum of the lengths of the local factors is constant in a flat finite family. This is how ramification looks in algebra: two points come together into one fat point of length $2$.

### Examples

**Example P1.3.37 (the integers modulo $n$).** For $n = \prod p_i^{e_i}$, $\mathbb{Z}/n \cong \prod \mathbb{Z}/p_i^{e_i}$. Each $\mathbb{Z}/p_i^{e_i}$ is a local Artinian ring with maximal ideal $(p_i)$ and length $e_i$.

**Example P1.3.38 (a fibre of the double cover).** Let $k$ be algebraically closed of characteristic not $2$, and consider $\mathbb{A}^1 \to \mathbb{A}^1$, $y \mapsto y^2 = x$. The fibre over $x = a$ has ring $k[y]/(y^2 - a)$. For $a = b^2 \neq 0$ it is $k[y]/(y - b) \times k[y]/(y + b) \cong k \times k$, two reduced points. For $a = 0$ it is $k[y]/(y^2)$, one fat point of length $2$. The total length is $2$ in both cases, and the branch point is where the two points come together.

**Example P1.3.39 (dimension zero without the chain condition).** Let $A = k[x_1, x_2, \dots]/(x_1^2, x_2^2, \dots)$. Every $x_i$ is nilpotent, so the only prime is $\mathfrak{m} = (x_1, x_2, \dots)$, and $\dim A = 0$. But $\mathfrak{m}$ is not finitely generated, so $A$ is not Noetherian, and by the theorem it is not Artinian. The nilradical $\mathfrak{m}$ is not nilpotent, since $x_1 x_2 \cdots x_n \neq 0$ for every $n$.

### Exercises

1. (A) Write $\mathbb{Z}/360$ and $\mathbb{Q}[x]/(x^3 - x^2)$ as products of local Artinian rings, and give the length of each factor.
2. (A) Show that a $k$-algebra that is finite dimensional as a $k$-vector space is Artinian, and that its spectrum is finite and discrete.
3. (B) Let $A$ be a local Artinian ring with principal maximal ideal $\mathfrak{m} = (t)$. Show that every ideal of $A$ is a power of $\mathfrak{m}$. Show that $k[x, y]/(x, y)^2$ is local Artinian and has an ideal that is not a power of its maximal ideal.
4. (B) Show that in an Artinian ring every element is a unit or a zero divisor, and that a reduced Artinian ring is a finite product of fields.
5. (B) Let $A$ be a Noetherian local ring with maximal ideal $\mathfrak{m}$. Show that $A$ is Artinian if and only if $\mathfrak{m}^n = 0$ for some $n$. Deduce that for an ideal $I$, the ring $A/I$ is Artinian if and only if $I$ is $\mathfrak{m}$-primary, and that $A/\mathfrak{m}^n$ has finite length for every $n$.
6. (C) Let $B$ be a finite dimensional $k$-algebra and $K/k$ a field extension. Show that $\dim_k B = \dim_K (B \otimes_k K)$, that $B \otimes_k K$ is Artinian, and give an example where $B$ is a field and $B \otimes_k K$ is not reduced.

### Lean

Mathlib proves that primes in a commutative Artinian ring are maximal (`IsArtinianRing.isMaximal_of_isPrime`), that there are finitely many (`IsArtinianRing.setOfPred_isMaximal_finite`), and that the Jacobson radical is nilpotent (`IsArtinianRing.isNilpotent_jacobson_bot`). The theorem of Akizuki and Hopkins is `isArtinianRing_iff_isNoetherianRing_krullDimLE_zero`, stated with `Ring.KrullDimLE 0`. The structure theorem appears as `IsArtinianRing.quotNilradicalPowEquivPi`; with $n = k$ the left side is $A$. Localizations of Artinian rings are Artinian by `IsArtinianRing.localization_artinian`. The handbook adds no `MinimalModel` node here.

### Notes and history

Artin studied rings with the descending chain condition in 1927, in the noncommutative setting of the Wedderburn theory. Akizuki proved in 1935 that a commutative Artinian ring is Noetherian, and Hopkins and Levitzki independently proved the noncommutative version in 1939. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 8.
