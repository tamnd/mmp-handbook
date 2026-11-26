---
title: Lying over, going up and incomparability
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch5, Mat86:ch3, Eis95:ch4]
requires: [P1.1, P1.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Lying over, going up and incomparability

### Statement

Throughout, $A \subseteq B$ are rings with $B$ integral over $A$. For a prime $\mathfrak{q}$ of $B$, the prime $\mathfrak{q} \cap A$ of $A$ is its *contraction*, and $\mathfrak{q}$ *lies over* $\mathfrak{q} \cap A$.

**Proposition P1.4.9 (fields in integral extensions).** Let $A \subseteq B$ be domains with $B$ integral over $A$. Then $A$ is a field if and only if $B$ is a field.

Lean: Mathlib `Algebra.IsIntegral.isField_iff_isField` (proved in Mathlib).

*Proof.* Let $A$ be a field and $0 \neq b \in B$. Choose an integral equation $b^n + a_1 b^{n-1} + \dots + a_n = 0$ of least degree. Then $a_n \neq 0$: otherwise $b(b^{n-1} + \dots + a_{n-1}) = 0$, and since $B$ is a domain an equation of degree $n - 1$ holds. So $b^{-1} = -a_n^{-1}(b^{n-1} + a_1 b^{n-2} + \dots + a_{n-1}) \in B$. Conversely, let $B$ be a field and $0 \neq a \in A$. Then $a^{-1} \in B$ is integral over $A$: $a^{-m} + c_1 a^{-m+1} + \dots + c_m = 0$. Multiply by $a^{m-1}$: $a^{-1} = -(c_1 + c_2 a + \dots + c_m a^{m-1}) \in A$. $\square$

**Corollary P1.4.10 (maximal ideals).** Let $\mathfrak{q}$ be a prime of $B$ and $\mathfrak{p} = \mathfrak{q} \cap A$. Then $\mathfrak{q}$ is maximal if and only if $\mathfrak{p}$ is maximal.

Lean: Mathlib `Ideal.isMaximal_of_isIntegral_of_isMaximal_under` and `Ideal.isMaximal_under_of_isIntegral_of_isMaximal` (proved in Mathlib).

*Proof.* The domain $B/\mathfrak{q}$ is integral over $A/\mathfrak{p}$, by Section 4.1. Apply the proposition. $\square$

**Theorem P1.4.11 (incomparability).** Let $\mathfrak{q} \subseteq \mathfrak{q}'$ be primes of $B$ with $\mathfrak{q} \cap A = \mathfrak{q}' \cap A$. Then $\mathfrak{q} = \mathfrak{q}'$.

Lean: Mathlib `Ideal.IsIntegral.under_lt_under` (proved in Mathlib), in the form: $\mathfrak{q} \subsetneq \mathfrak{q}'$ implies $\mathfrak{q} \cap A \subsetneq \mathfrak{q}' \cap A$.

*Proof.* Let $\mathfrak{p} = \mathfrak{q} \cap A$ and $S = A \setminus \mathfrak{p}$. Then $S^{-1}B$ is integral over $A_{\mathfrak{p}}$, and the primes $\mathfrak{n} = S^{-1}\mathfrak{q} \subseteq \mathfrak{n}' = S^{-1}\mathfrak{q}'$ both contract to $\mathfrak{p}A_{\mathfrak{p}}$, which is maximal. By the corollary, $\mathfrak{n}$ is maximal, so $\mathfrak{n} = \mathfrak{n}'$. By the correspondence of primes in Section 2.1, $\mathfrak{q} = \mathfrak{q}'$. $\square$

**Theorem P1.4.12 (lying over).** For every prime $\mathfrak{p}$ of $A$ there is a prime $\mathfrak{q}$ of $B$ with $\mathfrak{q} \cap A = \mathfrak{p}$.

Lean: Mathlib `Ideal.exists_ideal_over_prime_of_isIntegral` (proved in Mathlib).

*Proof.* Let $S = A \setminus \mathfrak{p}$. Then $A_{\mathfrak{p}} \to S^{-1}B$ is injective, since localization is exact (Section 2.1), and $S^{-1}B$ is integral over $A_{\mathfrak{p}}$. In particular $S^{-1}B \neq 0$, so it has a maximal ideal $\mathfrak{n}$. By the corollary, $\mathfrak{n} \cap A_{\mathfrak{p}}$ is maximal, so it is $\mathfrak{p}A_{\mathfrak{p}}$. The contraction $\mathfrak{q}$ of $\mathfrak{n}$ to $B$ is prime, and $\mathfrak{q} \cap A$ is the contraction of $\mathfrak{p}A_{\mathfrak{p}}$ to $A$, which is $\mathfrak{p}$. $\square$

**Theorem P1.4.13 (going up).** Let $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$ be primes of $A$ and $\mathfrak{q}_1$ a prime of $B$ over $\mathfrak{p}_1$. Then there is a prime $\mathfrak{q}_2 \supseteq \mathfrak{q}_1$ of $B$ over $\mathfrak{p}_2$.

Lean: Mathlib `Algebra.HasGoingUp`, with the instance `Algebra.HasGoingUp.of_isIntegral` (proved in Mathlib).

*Proof.* The ring $\bar{B} = B/\mathfrak{q}_1$ is integral over $\bar{A} = A/\mathfrak{p}_1$, and $\bar{A} \subseteq \bar{B}$. By lying over, the prime $\mathfrak{p}_2/\mathfrak{p}_1$ of $\bar{A}$ has a prime of $\bar{B}$ over it. Its preimage $\mathfrak{q}_2$ in $B$ contains $\mathfrak{q}_1$ and lies over $\mathfrak{p}_2$. $\square$

**Corollary P1.4.14 (dimension).** If $B$ is integral over $A \subseteq B$, then $\dim A = \dim B$.

Lean: not in Lean in this form; Mathlib proves the ingredients `Ideal.IsIntegral.under_lt_under` and `Algebra.HasGoingUp.of_isIntegral`.

*Proof.* A chain $\mathfrak{q}_0 \subsetneq \dots \subsetneq \mathfrak{q}_n$ in $B$ contracts to a chain in $A$, which is strict by incomparability. So $\dim A \geq \dim B$. A chain $\mathfrak{p}_0 \subsetneq \dots \subsetneq \mathfrak{p}_n$ in $A$ lifts by lying over and going up to a chain $\mathfrak{q}_0 \subseteq \dots \subseteq \mathfrak{q}_n$ with $\mathfrak{q}_i \cap A = \mathfrak{p}_i$, which is strict since the contractions differ. So $\dim B \geq \dim A$. $\square$

### Proof in words

All three theorems reduce to one fact: in an integral extension of domains, one ring is a field exactly when the other is. Localizing at a prime $\mathfrak{p}$ of $A$ makes $\mathfrak{p}$ maximal, and the primes of $B$ over it become maximal too. So the primes over $\mathfrak{p}$ exist, and no two of them are contained in each other. Passing to quotients gives going up.

Geometrically, let $f: X = \operatorname{Spec} B \to Y = \operatorname{Spec} A$. Lying over says that $f$ is surjective. Going up says that $f$ is closed: in general $f(V(J)) = V(J \cap A)$ (Exercise 4). Incomparability says that no point of a fibre is a specialization of another, so the fibres have dimension $0$. For a finite morphism the fibre over $\mathfrak{p}$ is the spectrum of the finite $\kappa(\mathfrak{p})$-algebra $B \otimes_A \kappa(\mathfrak{p})$, a finite set by Section 3.5. Finite morphisms preserve dimension. In the MMP, a finite morphism $X' \to X$ lets properties pass between $X'$ and $X$: the index one cover of Volume 4 is finite, and $X$ is klt if the cover is.

### Examples

**Example P1.4.15 (Gaussian integers).** Let $A = \mathbb{Z} \subseteq B = \mathbb{Z}[i]$, which is integral since $i^2 + 1 = 0$. The primes over $(p)$ are the primes of $\mathbb{Z}[i]/(p) \cong \mathbb{F}_p[x]/(x^2 + 1)$.

- For $p = 2$: $x^2 + 1 = (x + 1)^2$ in $\mathbb{F}_2[x]$, so there is one prime $(1 + i)$ over $(2)$, and $(2) = (1 + i)^2$ up to a unit. The prime $2$ is ramified.
- For $p = 3$: $x^2 + 1$ is irreducible in $\mathbb{F}_3[x]$, so $(3)$ stays prime in $\mathbb{Z}[i]$, with residue field $\mathbb{F}_9$. It is inert.
- For $p = 5$: $x^2 + 1 = (x - 2)(x + 2)$, so there are two primes $(2 + i)$ and $(2 - i)$ over $(5)$. It splits.

In every case the fibre is the spectrum of an algebra of dimension $2$ over $\mathbb{F}_p$. The map $\operatorname{Spec} \mathbb{Z}[i] \to \operatorname{Spec} \mathbb{Z}$ is a double cover branched over $(2)$, like the double cover $y^2 = x$ of Section 3.5.

**Example P1.4.16 (lying over fails without integrality).** For $A = k[x] \subseteq B = k[x, 1/x]$, no prime of $B$ lies over $(x)$, since $x$ is a unit in $B$. The image of $\operatorname{Spec} B \to \operatorname{Spec} A$ is the open set $D(x)$, which is not closed. The extension is not integral, as Section 4.1 showed.

**Example P1.4.17 (dimension can drop).** Let $A = k[x]_{(x)}$, a local domain of dimension $1$, and $B = k(x)$, its fraction field. Then $B$ is not integral over $A$. The zero ideal of $B$ lies over $(0)$, and no prime of $B$ lies over the maximal ideal. Here $\dim B = 0 < 1 = \dim A$.

### Exercises

1. (A) Find the primes of $\mathbb{Z}[\sqrt{-5}]$ over $(2)$, $(3)$ and $(5)$, and say which are ramified.
2. (A) Let $A = k[x^2] \subseteq B = k[x]$ with $k$ algebraically closed of characteristic not $2$. Describe the fibre of $\operatorname{Spec} B \to \operatorname{Spec} A$ over every prime of $A$, including the generic point.
3. (B) Let $A \subseteq B$ be integral and $\mathfrak{p}$ a prime of $A$. Show that $\mathfrak{p}B \cap A = \mathfrak{p}$. Show by an example that $\mathfrak{p}B$ need not be prime.
4. (B) Let $A \subseteq B$ be integral and $J$ an ideal of $B$. Show that the image of $V(J)$ in $\operatorname{Spec} A$ is $V(J \cap A)$. Deduce that $\operatorname{Spec} B \to \operatorname{Spec} A$ is a closed map.
5. (C) Let $B$ be a finite $A$-algebra, not necessarily containing $A$. Show that $\operatorname{Spec} B \to \operatorname{Spec} A$ has finite fibres, and that the number of primes over $\mathfrak{p}$ is at most the number of generators of $B$ as an $A$-module. (Hint: $B \otimes_A \kappa(\mathfrak{p})$.)

### Lean

Mathlib proves lying over as `Ideal.exists_ideal_over_prime_of_isIntegral` and incomparability as `Ideal.IsIntegral.under_lt_under`. Going up is the class `Algebra.HasGoingUp`, with the instance `Algebra.HasGoingUp.of_isIntegral` for integral algebras. The statements on maximal ideals are `Ideal.isMaximal_of_isIntegral_of_isMaximal_under` and `Ideal.isMaximal_under_of_isIntegral_of_isMaximal`. The handbook adds no `MinimalModel` node here.

### Notes and history

Krull proved forms of these theorems in the 1930s. Cohen and Seidenberg proved them in general in their 1946 paper "Prime ideals and integral dependence", which is the source of the terms lying over, going up and going down. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 5.
