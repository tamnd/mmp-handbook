---
title: Krull dimension and height
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch11, Mat86:ch5, Eis95:ch8]
requires: [P1.2, P1.3, P1.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Krull dimension and height

### Statement

**Definition P1.5.1 (Krull dimension).** A *chain* of length $n$ in a topological space $X$ is a sequence $Z_0 \subsetneq Z_1 \subsetneq \dots \subsetneq Z_n$ of irreducible closed subsets. The *dimension* $\dim X$ is the supremum of the lengths of the chains in $X$. The *Krull dimension* $\dim A$ of a ring $A$ is the dimension of $\operatorname{Spec} A$. Since $\mathfrak{p} \mapsto V(\mathfrak{p})$ is an inclusion reversing bijection from primes to irreducible closed subsets (Section 2.2), $\dim A$ is the supremum of the lengths $n$ of the chains of primes
$$
\mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \dots \subsetneq \mathfrak{p}_n .
$$
The zero ring has no primes, and its dimension is $-\infty$ by convention. The dimension may be infinite.

Lean: Mathlib `ringKrullDim` (definition), with values in `WithBot ℕ∞`, so that the zero ring has dimension $\bot$ and an infinite dimension is $\top$. The dimension of a topological space is `topologicalKrullDim`.

**Example P1.5.2.** A field has dimension $0$, and so has every Artinian ring (Section 3.5). A principal ideal domain that is not a field has dimension $1$: its nonzero primes are the ideals $(p)$ with $p$ irreducible, and they are maximal, so the longest chains are $0 \subsetneq (p)$. So $\dim \mathbb{Z} = \dim k[x] = \dim k[[x]] = 1$.

**Example P1.5.3.** By Theorem P1.4.31, $\dim k[x_1, \dots, x_n] = n$, and more generally a finitely generated $k$-domain has dimension equal to the transcendence degree of its fraction field. The ring $\mathbb{Z}[x]$ has the chain $0 \subsetneq (p) \subsetneq (p, x)$, so $\dim \mathbb{Z}[x] \geq 2$. Section 5.4 proves equality.

**Definition P1.5.4 (height, codimension).** The *height* $\operatorname{ht} \mathfrak{p}$ of a prime $\mathfrak{p}$ is the supremum of the lengths of the chains of primes that end at $\mathfrak{p}$. The *height* of an ideal $I \neq A$ is the least height of a prime that contains $I$; it is the least height of a minimal prime over $I$. For an irreducible closed subset $Z = V(\mathfrak{p})$ of $\operatorname{Spec} A$, the *codimension* of $Z$ is $\operatorname{ht} \mathfrak{p}$. The *dimension* of a module $M$ is the dimension of the closed set $\operatorname{Supp} M$.

Lean: Mathlib `Ideal.height` (definition), the infimum of the heights of the minimal primes, with `Ideal.height_eq_inf_minimalPrimes`; the dimension of a module is `Module.supportDim`.

**Example P1.5.5.** In $k[x, y]$ the prime $(x)$ has height $1$: a chain $0 \subsetneq \mathfrak{q} \subsetneq (x)$ would give a nonzero prime $\mathfrak{q}$ properly inside $(x)$, and $\mathfrak{q}$ contains an irreducible factor of one of its elements, which must be a multiple of $x$ and hence an associate of $x$, so $\mathfrak{q} = (x)$. The maximal ideal $(x, y)$ has height at least $2$, from the chain $0 \subsetneq (x) \subsetneq (x, y)$, and Section 5.2 shows that it is exactly $2$. The ideal $(xy)$ has height $1$: its minimal primes are $(x)$ and $(y)$.

**Example P1.5.6.** In $A = k[x, y]/(xy)$, the union of the two axes, the minimal primes are $(x)$ and $(y)$, of height $0$. The maximal ideal $(x, y)$ of the origin has height $1$, and so does $(x, y - 1)$. So $\dim A = 1$. The ideal $(x)$ of $A$ is prime of height $0$, but $x$ is not nilpotent: a prime of height $0$ in a ring with several components is a component, not the zero ideal.

**Proposition P1.5.7 (first properties).** Let $A$ be a ring, $\mathfrak{p}$ a prime and $I$ an ideal.

1. $\operatorname{ht} \mathfrak{p} = \dim A_{\mathfrak{p}}$.
2. Every prime contains a minimal prime. Hence $\dim A = \sup_{\mathfrak{m}} \operatorname{ht} \mathfrak{m}$ over the maximal ideals, and $\dim A = \sup_{\mathfrak{p}} \dim A/\mathfrak{p}$ over the minimal primes.
3. $\operatorname{ht} \mathfrak{p} + \dim A/\mathfrak{p} \leq \dim A$.
4. $\dim A/I \leq \dim A$, and $\dim A = \dim A/\mathfrak{N}$ for the nilradical $\mathfrak{N}$.
5. If $A$ is Noetherian and $M$ is finitely generated, then $\dim M = \dim A/\operatorname{Ann} M$.

Lean: Mathlib `IsLocalization.AtPrime.ringKrullDim_eq_height`, `Ideal.sup_isMaximal_height_eq_ringKrullDim` and `ringKrullDim_quotient_le` (proved in Mathlib).

*Proof.* (1) The primes of $A_{\mathfrak{p}}$ correspond to the primes of $A$ inside $\mathfrak{p}$, with the order kept (Theorem P1.2.6). So the chains of primes of $A_{\mathfrak{p}}$ are the chains of primes of $A$ that end inside $\mathfrak{p}$, and a chain that ends inside $\mathfrak{p}$ does not become shorter when $\mathfrak{p}$ is added at its top.

(2) Let $\mathfrak{p}$ be prime. The set of primes inside $\mathfrak{p}$, ordered by reverse inclusion, is not empty, and the intersection of a chain of primes is prime: if $ab$ lies in every member and $a$ does not lie in $\mathfrak{q}_1$, then for every $\mathfrak{q}_2 \subseteq \mathfrak{q}_1$ of the chain $a \notin \mathfrak{q}_2$, so $b \in \mathfrak{q}_2$, and $b$ also lies in the members that contain $\mathfrak{q}_1$. By Zorn's lemma there is a minimal prime inside $\mathfrak{p}$. Every chain of primes can be extended at the top to a maximal ideal (Theorem P1.1.4) and at the bottom to a minimal prime, without loss of length. This gives both formulas.

(3) A chain of length $r$ that ends at $\mathfrak{p}$, followed by a chain of length $s$ of primes that start at $\mathfrak{p}$, is a chain of length $r + s$ in $A$. The primes of $A/\mathfrak{p}$ are the primes of $A$ that contain $\mathfrak{p}$.

(4) The primes of $A/I$ are the primes of $A$ that contain $I$, and every prime contains $\mathfrak{N}$.

(5) This is $\operatorname{Supp} M = V(\operatorname{Ann} M)$, Theorem P1.2.48. $\square$

**Definition P1.5.8 (catenary ring).** A chain of primes $\mathfrak{p} = \mathfrak{p}_0 \subsetneq \dots \subsetneq \mathfrak{p}_n = \mathfrak{q}$ is *saturated* if no prime lies strictly between $\mathfrak{p}_{i-1}$ and $\mathfrak{p}_i$ for any $i$. A Noetherian ring $A$ is *catenary* if for all primes $\mathfrak{p} \subseteq \mathfrak{q}$, all saturated chains from $\mathfrak{p}$ to $\mathfrak{q}$ have the same length.

Lean: not in Lean.

**Example P1.5.9.** Every Noetherian ring of dimension at most $1$ is catenary, and so is every Noetherian domain of dimension $2$ (Exercise 5). Section 5.4 proves that every finitely generated algebra over a field is catenary. Nagata found in 1956 a Noetherian local domain of dimension $3$ that is not catenary: it has a saturated chain of length $2$ from $0$ to the maximal ideal, and also chains of length $3$.

**Example P1.5.10 (Nagata's ring).** A Noetherian local ring has finite dimension, by Section 5.2. A Noetherian ring need not: Nagata constructed a Noetherian domain $A$ with maximal ideals $\mathfrak{m}_1, \mathfrak{m}_2, \dots$ of heights $\operatorname{ht} \mathfrak{m}_i \to \infty$. Every local ring $A_{\mathfrak{m}_i}$ has finite dimension, but $\dim A = \infty$. The construction localizes $k[x_1, x_2, \dots]$ at the complement of the union of the primes $(x_{n_i + 1}, \dots, x_{n_{i+1}})$, for a sequence $n_i$ with $n_{i+1} - n_i \to \infty$.

### Proof in words

The Krull dimension is the longest chain of irreducible closed sets: a point inside a curve inside a surface, and so on. For a variety this is the dimension of P0 Ch. 6, and Theorem P1.4.31 computes it as a transcendence degree. The height of a prime is the codimension of its closed set, measured inside the local ring, and the dimension of $A/\mathfrak{p}$ is the dimension of the closed set itself. The inequality $\operatorname{ht} \mathfrak{p} + \dim A/\mathfrak{p} \leq \dim A$ is the gluing of two chains; it is an equality for varieties that are irreducible (Section 5.4), but not in general.

The proofs here are formal, and the content is in the examples. The dimension is a global supremum, and different points can have local rings of different dimensions. This happens when a variety has components of different dimensions, and also for some irreducible schemes that are not of finite type over a field.

### Examples

**Example P1.5.11 (a plane and a line).** Let $A = k[x, y, z]/(xz, yz)$, so that $\operatorname{Spec} A$ is the union of the plane $z = 0$ and the line $x = y = 0$ (Example P1.3.23). The minimal primes are $(z)$ and $(x, y)$, with $\dim A/(z) = 2$ and $\dim A/(x, y) = 1$, so $\dim A = 2$. The maximal ideal $\mathfrak{m} = (x, y, z - 1)$ of the point $(0, 0, 1)$ on the line lies over only one minimal prime, $(x, y)$, and $\operatorname{ht} \mathfrak{m} = 1$. So $\operatorname{ht} \mathfrak{m} + \dim A/\mathfrak{m} = 1 < 2 = \dim A$. The prime $(x, y)$ itself gives $\operatorname{ht} (x, y) + \dim A/(x, y) = 0 + 1 < 2$.

**Example P1.5.12 (an irreducible scheme with a short maximal ideal).** Let $R$ be a discrete valuation ring with uniformizer $\pi$, for example $R = \mathbb{Z}_{(p)}$ with $\pi = p$, or $R = k[s]_{(s)}$ with $\pi = s$, and let $K$ be its fraction field. Let $A = R[t]$, a domain. The chain $0 \subsetneq (\pi) \subsetneq (\pi, t)$ gives $\dim A \geq 2$. Let $\mathfrak{m} = (\pi t - 1)$. Then $A/\mathfrak{m} \cong R[1/\pi] = K$, since $t$ maps to $1/\pi$, so $\mathfrak{m}$ is maximal. Let $\mathfrak{q}$ be a nonzero prime inside $\mathfrak{m}$. Then $\mathfrak{q} \cap R$ is a prime of $R$, so it is $0$ or $(\pi)$; it is not $(\pi)$, since $\pi \in \mathfrak{m}$ and $\pi t - 1 \in \mathfrak{m}$ would give $1 \in \mathfrak{m}$. So $\mathfrak{q}$ misses $R \setminus 0$, and it corresponds to a nonzero prime of $K[t]$ inside $\mathfrak{m}K[t]$ (Theorem P1.2.6). Nonzero primes of $K[t]$ are maximal, so $\mathfrak{q} K[t] = \mathfrak{m} K[t]$ and $\mathfrak{q} = \mathfrak{m}$. Hence $\operatorname{ht} \mathfrak{m} = 1$, and
$$
\operatorname{ht} \mathfrak{m} + \dim A/\mathfrak{m} = 1 < 2 \leq \dim A .
$$
Geometrically, $\operatorname{Spec} A$ is the line over $\operatorname{Spec} R$. The point $t = 1/\pi$ of the generic fibre, the line over $K$, is closed in the whole space, because no point of the special fibre lies in its closure. The ring $A$ is a Noetherian domain, so the failure is not caused by components. It is caused by the fact that $A$ is not of finite type over a field, which is the hypothesis of Section 5.4.

**Example P1.5.13 (a non-Noetherian ring of dimension zero).** The ring $A = k[x_1, x_2, \dots]/(x_1^2, x_2^2, \dots)$ of Example P1.3.39 has one prime, so $\dim A = 0$, but its maximal ideal is not nilpotent and not finitely generated. Dimension zero does not give the structure theory of Section 3.5 without the Noetherian hypothesis.

### Exercises

1. (A) Compute the dimension of $k[x, y]/(x^2, xy)$, of $\mathbb{Z}/12$, of $\mathbb{Z} \times k[x, y]$ and of $k[x, y, z]/(xy, z^2)$. For each ring list the minimal primes and their heights.
2. (A) Compute the height of the ideals $(xy, xz)$ and $(x, y) \cap (z, w)$ of $k[x, y, z, w]$. You may use the results of Section 5.2.
3. (A) Let $X$ be a topological space and $U \subseteq X$ open. Show that $\dim U \leq \dim X$. Show that the open point of $\operatorname{Spec} \mathbb{Z}_{(p)}$ is a dense open set of dimension $0$ in a space of dimension $1$.
4. (B) Let $A$ be a ring and $S$ a multiplicative set. Show that $\dim S^{-1} A \leq \dim A$. Give a domain $A$ and an element $f \neq 0$ with $\dim A_f < \dim A$, and show that for $A = k[x_1, \dots, x_n]$ and $f \neq 0$ the dimension of $A_f$ is $n$. (For the last claim, use Theorem P1.4.31: $A_f$ is a finitely generated $k$-domain.)
5. (B) Show that every Noetherian ring of dimension at most $1$ and every Noetherian domain of dimension $2$ is catenary. Show that the ring $R[t]$ of the example above is catenary, so that catenary rings can still fail the formula $\operatorname{ht} \mathfrak{p} + \dim A/\mathfrak{p} = \dim A$.
6. (B) In the ring $A = R[t]$ of the example above, show that every maximal ideal that contains $\pi$ has height $2$, and that every maximal ideal $\mathfrak{m}$ with $\mathfrak{m} \cap R = 0$ has height $1$. Give a prime $\mathfrak{p}$ with $\mathfrak{p} \cap R = 0$ that is not maximal. Show that $\operatorname{Spec} A/\pi A$ and $\operatorname{Spec} K[t]$ are disjoint subsets of $\operatorname{Spec} A$ whose union is everything.

### Lean

Mathlib defines `ringKrullDim` as the Krull dimension of the poset of primes, with values in `WithBot ℕ∞`, and `Ideal.height` for ideals. The localization formula is `IsLocalization.AtPrime.ringKrullDim_eq_height`, and the supremum over maximal ideals is `Ideal.sup_isMaximal_height_eq_ringKrullDim`. Catenary rings are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

Krull defined the dimension of a ring through chains of primes in 1937 and 1938, in his papers on the dimension theory of local rings, Krull asked whether every Noetherian domain satisfies the chain condition that is now called catenary, and Nagata answered no in 1956. The name catenary is from EGA IV. Nagata's Noetherian ring of infinite dimension appears in the appendix of his book *Local rings* of 1962. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 11, Matsumura, Chapter 5, and Eisenbud, Chapter 8.
