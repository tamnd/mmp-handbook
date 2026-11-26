---
title: Dedekind domains and the class group
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch9, Mat86:ch4, Eis95:ch11]
requires: [P1.1, P1.2, P1.3, P1.4, P1.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Dedekind domains and the class group

### Statement

**Definition P1.7.20 (Dedekind domain).** A *Dedekind domain* is a Noetherian normal domain of dimension at most $1$.

Lean: Mathlib `IsDedekindDomain` (class, with the same three conditions, so that a field is a Dedekind domain).

A Dedekind domain that is not a field has dimension $1$, so every nonzero prime is maximal and has height $1$. The main examples are $\mathbb{Z}$ and every principal ideal domain, the ring of integers of a number field, and the coordinate ring of a normal affine curve.

**Theorem P1.7.21 (local characterization).** Let $A$ be a Noetherian domain of dimension $1$. The following are equivalent:

1. $A$ is a Dedekind domain;
2. $A_\mathfrak{p}$ is a DVR for every nonzero prime $\mathfrak{p}$;
3. every nonzero primary ideal of $A$ is a power of a prime.

Lean: Mathlib `isDedekindDomain_iff_isDiscreteValuationRing_atPrime` for the equivalence of (1) and (2) (proved in Mathlib).

*Proof.* Two facts are used. If $\mathfrak{p}$ is a nonzero prime, then $\mathfrak{p}$ is maximal, and $A_\mathfrak{p}$ is a Noetherian local domain of dimension $1$. If $\mathfrak{q}$ is $\mathfrak{p}$-primary, then $\mathfrak{q}A_\mathfrak{p} \cap A = \mathfrak{q}$: if $sa \in \mathfrak{q}$ with $s \notin \mathfrak{p}$, then no power of $s$ lies in $\mathfrak{q}$, so $a \in \mathfrak{q}$.

(1) and (2) are equivalent by Proposition P1.4.20, since normality is local, and the characterization of DVRs in Section 7.2.

(2) implies (3): let $\mathfrak{q} \neq 0$ be primary with radical $\mathfrak{p}$. Then $\mathfrak{p} \neq 0$, and $\mathfrak{q}A_\mathfrak{p} = \mathfrak{p}^n A_\mathfrak{p}$ for some $n$, since every nonzero ideal of the DVR $A_\mathfrak{p}$ is a power of its maximal ideal. The ideal $\mathfrak{p}^n$ is $\mathfrak{p}$-primary by Proposition P1.2.28. By the second fact, $\mathfrak{q} = \mathfrak{q}A_\mathfrak{p} \cap A = \mathfrak{p}^nA_\mathfrak{p} \cap A = \mathfrak{p}^n$.

(3) implies (2): let $\mathfrak{p} \neq 0$ be prime and $I$ a nonzero proper ideal of $A_\mathfrak{p}$. Its radical is the maximal ideal, so it is primary by Proposition P1.2.28, and its preimage $J = I \cap A$ is $\mathfrak{p}$-primary, with $I = JA_\mathfrak{p}$ (Theorem P1.2.6). By (3), $J$ is a power of a prime, and the prime is $\sqrt{J} = \mathfrak{p}$. So $I = (\mathfrak{p}A_\mathfrak{p})^n$, and $A_\mathfrak{p}$ is a DVR by condition (5) of the characterization of DVRs. $\square$

**Theorem P1.7.22 (unique factorization of ideals).** Let $A$ be a Dedekind domain. Every nonzero ideal $I$ of $A$ is a product
$$
I = \mathfrak{p}_1^{n_1} \cdots \mathfrak{p}_r^{n_r}
$$
of distinct nonzero primes with $n_i \geq 1$, and the factorization is unique up to order. The exponent of $\mathfrak{p}$ is the integer $v_\mathfrak{p}(I)$ with $IA_\mathfrak{p} = (\mathfrak{p}A_\mathfrak{p})^{v_\mathfrak{p}(I)}$.

Lean: Mathlib `Ideal.uniqueFactorizationMonoid` (instance, proved in Mathlib).

*Proof.* If $A$ is a field, or $I = A$, take the empty product. Otherwise let $I = \mathfrak{q}_1 \cap \dots \cap \mathfrak{q}_r$ be a minimal primary decomposition (Theorem P1.2.40), with distinct radicals $\mathfrak{p}_i$. These are nonzero, since they contain $I \neq 0$, so they are maximal and pairwise comaximal. Then the $\mathfrak{q}_i$ are pairwise comaximal too: from $1 = a + b$ with $a^n \in \mathfrak{q}_i$ and $b^n \in \mathfrak{q}_j$ one gets $1 = (a + b)^{2n} \in \mathfrak{q}_i + \mathfrak{q}_j$. By the Chinese remainder theorem P1.1.12, $I = \mathfrak{q}_1 \cdots \mathfrak{q}_r$, and $\mathfrak{q}_i = \mathfrak{p}_i^{n_i}$ by the local characterization. For uniqueness, localize a factorization $I = \prod \mathfrak{p}_i^{n_i}$ at a nonzero prime $\mathfrak{p}$. For $\mathfrak{p}_i \neq \mathfrak{p}$ the ideal $\mathfrak{p}_i$ contains an element outside $\mathfrak{p}$, so $\mathfrak{p}_iA_\mathfrak{p} = A_\mathfrak{p}$. Hence $IA_\mathfrak{p} = (\mathfrak{p}A_\mathfrak{p})^{n}$, where $n = n_i$ if $\mathfrak{p} = \mathfrak{p}_i$ and $n = 0$ otherwise. In the DVR $A_\mathfrak{p}$ the powers of the maximal ideal are distinct, so $n = v_\mathfrak{p}(I)$ is determined by $I$. $\square$

Let $K$ be the fraction field of a domain $A$. A *fractional ideal* is a nonzero $A$-submodule $M \subseteq K$ with $dM \subseteq A$ for some nonzero $d \in A$. Every nonzero ideal is one, and so is $xA$ for $x \in K^*$, a *principal* fractional ideal. If $A$ is Noetherian, then $dM$ is an ideal, so $M$ is finitely generated. Products $MN$ of fractional ideals are fractional ideals. A fractional ideal $M$ is *invertible* if $MN = A$ for some fractional ideal $N$. Then $N = (A : M) = \{x \in K : xM \subseteq A\}$, since $N \subseteq (A : M) = (A : M)MN \subseteq N$.

**Theorem P1.7.23 (the group of fractional ideals).** Let $A$ be a Dedekind domain. Every fractional ideal of $A$ is invertible, so the fractional ideals form an abelian group $I(A)$ under multiplication. It is the free abelian group on the nonzero primes: every fractional ideal is uniquely $M = \prod_\mathfrak{p} \mathfrak{p}^{v_\mathfrak{p}(M)}$ with $v_\mathfrak{p}(M) \in \mathbb{Z}$, almost all zero.

Lean: Mathlib `FractionalIdeal` (definition), `isDedekindDomain_iff_isDedekindDomainInv` (every nonzero fractional ideal is invertible, proved in Mathlib).

*Proof.* Let $M$ be a fractional ideal and $N = (A : M)$. Then $MN$ is an ideal of $A$. Suppose $MN \neq A$, and let $\mathfrak{p}$ be a maximal ideal that contains it. The module $MA_\mathfrak{p}$ is a finitely generated $A_\mathfrak{p}$-submodule of $K$, so $dMA_\mathfrak{p}$ is an ideal of the DVR $A_\mathfrak{p}$ for some $d \neq 0$, and $MA_\mathfrak{p} = yA_\mathfrak{p}$ for some $y \in K^*$. Write $y = m/u$ with $m \in M$ and $u \notin \mathfrak{p}$. Let $x_1, \dots, x_n$ generate $M$. Each $y^{-1}x_i$ lies in $A_\mathfrak{p}$, so there is $s \notin \mathfrak{p}$ with $sy^{-1}x_i \in A$ for all $i$, and then $sy^{-1} \in N$. But $sy^{-1} \cdot m = su$ lies in $MN$ and not in $\mathfrak{p}$, a contradiction. So $MN = A$.

The fractional ideals form a commutative monoid with identity $A$ in which every element is invertible, hence a group. For a fractional ideal $M$ with $dM \subseteq A$, $M = (dM)(dA)^{-1}$, and factoring the ideals $dM$ and $dA$ by the previous theorem writes $M$ as a product of powers of primes with integer exponents. If two such products are equal, move the negative exponents to the other side. This gives two factorizations of one ideal, which agree by the previous theorem. $\square$

**Definition P1.7.24 (class group).** Let $A$ be a Dedekind domain with fraction field $K$. The principal fractional ideals form a subgroup $P(A) \subseteq I(A)$, the image of $K^* \to I(A)$, $x \mapsto xA$. The *class group* is $\operatorname{Cl}(A) = I(A)/P(A)$. The kernel of $K^* \to I(A)$ is $A^*$, so there is an exact sequence
$$
1 \to A^* \to K^* \to I(A) \to \operatorname{Cl}(A) \to 0 .
$$

Lean: Mathlib `ClassGroup` (definition, for any domain, by invertible fractional ideals modulo principal ones), with `ClassGroup.mk0` and `ClassGroup.mk0_eq_one_iff`.

**Proposition P1.7.25 (trivial class group).** For a Dedekind domain $A$ the following are equivalent: $\operatorname{Cl}(A) = 0$; $A$ is a principal ideal domain; $A$ is a unique factorization domain.

Lean: Mathlib `card_classGroup_eq_one_iff` for the first two conditions (proved in Mathlib).

*Proof.* If $\operatorname{Cl}(A) = 0$, every nonzero ideal $I$ is $xA$ with $x \in K^*$, and $x = x \cdot 1 \in I \subseteq A$. So $A$ is a principal ideal domain. Conversely, if every ideal is principal, every fractional ideal $M = (dM)(dA)^{-1}$ is principal. A principal ideal domain is a unique factorization domain. Finally, if $A$ is a unique factorization domain, every prime of height $1$ is principal by Proposition P1.5.23. Every nonzero prime of $A$ has height $1$, and every nonzero ideal is a product of primes, so it is principal. $\square$

So the class group measures the failure of unique factorization of elements in a ring that has unique factorization of ideals.

**Theorem P1.7.26 (integral closure in a finite separable extension).** Let $A$ be a Dedekind domain with fraction field $K$, let $L/K$ be a finite separable extension, and let $B$ be the integral closure of $A$ in $L$. Then $B$ is a Dedekind domain with fraction field $L$, and it is a finite $A$-module.

Lean: Mathlib `IsIntegralClosure.isDedekindDomain` (proved in Mathlib).

*Proof.* For $b \in L$, a relation $a_0 b^n + a_1 b^{n-1} + \dots + a_n = 0$ with $a_i \in A$ and $a_0 \neq 0$ shows that $a_0 b$ is integral over $A$. So every element of $L$ is $b'/a_0$ with $b' \in B$ and $a_0 \in A$, and $\operatorname{Frac} B = L$. The ring $B$ is normal by Proposition P1.4.4, and $\dim B = \dim A \leq 1$ by Corollary P1.4.14. For finiteness, use the trace argument in the proof of Theorem P1.4.32 with $A$ in place of the polynomial ring $R$: choose a basis $v_1, \dots, v_n$ of $L/K$ in $B$ and the dual basis $w_j$ for the trace form, which is nondegenerate as $L/K$ is separable. For $b \in B$ the traces $\operatorname{Tr}(bv_j)$ lie in $A$ by Exercise 5 of Section 4.3, so $B \subseteq \sum_j Aw_j$. Since $A$ is Noetherian, $B$ is a finite $A$-module, hence a Noetherian ring. $\square$

### Proof in words

A Dedekind domain is a ring that is a DVR at every nonzero prime. Each nonzero ideal $I$ is then known through its orders $v_\mathfrak{p}(I)$ at the finitely many primes that contain it, and the ideal is the product of the primes with these exponents. The proof uses primary decomposition: in dimension one the primary components have maximal radicals, so they are comaximal and their intersection is their product, and the local rings are DVRs, so each component is a prime power.

Since each local ring is a DVR, every fractional ideal is locally principal, and a locally principal fractional ideal is invertible. So the fractional ideals form a group, the free abelian group on the primes. This is the group of divisors of the curve $X = \operatorname{Spec} A$: the ideal $\prod \mathfrak{p}^{n_\mathfrak{p}}$ is the divisor $\sum n_\mathfrak{p} [\mathfrak{p}]$, and the fractional ideal $fA$ is the divisor of the rational function $f$. The class group is the group of divisors modulo principal divisors. Since every fractional ideal is an invertible module, the class group is also the group of line bundles on $X$, its Picard group. Chapter 8 defines the class group of every Noetherian normal domain by height one primes, and there the class group and the Picard group differ in general.

### Examples

**Example P1.7.27 (the integers of $\mathbb{Q}(\sqrt{-5})$).** Let $A = \mathbb{Z}[\sqrt{-5}]$. It is the integral closure of $\mathbb{Z}$ in $\mathbb{Q}(\sqrt{-5})$ (Exercise 2), so it is a Dedekind domain by the theorem on finite separable extensions. The element $6$ has two factorizations into irreducible elements,
$$
6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5}) ,
$$
so $A$ is not factorial, and $\operatorname{Cl}(A) \neq 0$. The ideals factor further. Put $\mathfrak{p} = (2, 1 + \sqrt{-5})$, $\mathfrak{q} = (3, 1 + \sqrt{-5})$ and $\mathfrak{q}' = (3, 1 - \sqrt{-5})$. These are maximal, with $A/\mathfrak{p} \cong \mathbb{F}_2$ and $A/\mathfrak{q} \cong A/\mathfrak{q}' \cong \mathbb{F}_3$. One computes
$$
\mathfrak{p}^2 = (4, 2 + 2\sqrt{-5}, -4 + 2\sqrt{-5}) = (2) ,
$$
since the generators are multiples of $2$ and the difference of the last two is $6$, and $\mathfrak{p}\mathfrak{q} = (6, 2 + 2\sqrt{-5}, 3 + 3\sqrt{-5}, -4 + 2\sqrt{-5}) = (1 + \sqrt{-5})$, since $(3 + 3\sqrt{-5}) - (2 + 2\sqrt{-5}) = 1 + \sqrt{-5}$ and every generator is a multiple of $1 + \sqrt{-5}$. In the same way $\mathfrak{p}\mathfrak{q}' = (1 - \sqrt{-5})$ and $\mathfrak{q}\mathfrak{q}' = (3)$. So both factorizations of $6$ give the ideal factorization $(6) = \mathfrak{p}^2\mathfrak{q}\mathfrak{q}'$. The ideal $\mathfrak{p}$ is not principal (Example P1.2.11), and $\mathfrak{p}^2$ is, so the class of $\mathfrak{p}$ has order $2$ in $\operatorname{Cl}(A)$. A computation with the Minkowski bound of algebraic number theory shows $\operatorname{Cl}(A) \cong \mathbb{Z}/2$.

**Example P1.7.28 (principal ideal domains).** The rings $\mathbb{Z}$, $k[x]$ and $\mathbb{Z}[i]$ are Euclidean, hence principal ideal domains, and so Dedekind domains with trivial class group. In $\mathbb{Z}[i]$, $(5) = (2 + i)(2 - i)$ and $(2) = (1 + i)^2$, while $(3)$ stays prime, as in Example P1.4.15.

**Example P1.7.29 (an affine elliptic curve).** Let $k$ be algebraically closed of characteristic not $2$, and $A = k[x, y]/(y^2 - x^3 + x)$, the affine part of the elliptic curve $E: y^2 = x^3 - x$. It is a Noetherian domain of dimension $1$. At every point the gradient $(1 - 3x^2, 2y)$ of the equation is nonzero on the curve, so after a translation of the point to the origin, the equation has a nonzero linear term, and as in the first example of Section 7.2 the local ring has $\dim_k \mathfrak{m}/\mathfrak{m}^2 = 1$. So every local ring at a maximal ideal is a DVR, and $A$ is a Dedekind domain by the local characterization. For the point $(0, 0)$ with ideal $\mathfrak{m} = (x, y)$,
$$
\mathfrak{m}^2 = (x^2, xy, y^2) = (x^2, xy, x(x^2 - 1)) = x \cdot (x, y, x^2 - 1) = (x) ,
$$
since $x^2 - (x^2 - 1) = 1$. So the class of $\mathfrak{m}$ in $\operatorname{Cl}(A)$ has order dividing $2$, and in fact $\mathfrak{m}$ is not principal (Exercise 8). The theory of elliptic curves shows that $\operatorname{Cl}(A)$ is isomorphic to the group $E(k)$ of points of the projective curve, with the class of the ideal of a point $P$ going to $P$. So the class group of the coordinate ring of a smooth affine curve can be very large, unlike the class group of a ring of integers, which is finite.

**Example P1.7.30 (a ring that is not Dedekind).** Let $A = \mathbb{Z}[\sqrt{-3}]$, a Noetherian domain of dimension $1$. The element $\omega = (-1 + \sqrt{-3})/2$ satisfies $\omega^2 + \omega + 1 = 0$, so it is integral over $A$, and it is not in $A$. So $A$ is not normal and not a Dedekind domain. The defect is at the single prime $\mathfrak{p} = (2, 1 + \sqrt{-3})$, where $A_\mathfrak{p}$ is not a DVR (Exercise 5). The integral closure $\mathbb{Z}[\omega]$ is a principal ideal domain.

### Exercises

1. (A) Factor the ideals $(2)$, $(3)$, $(5)$ and $(13)$ of $\mathbb{Z}[i]$ into primes, using $\mathbb{Z}[i]/(p) \cong \mathbb{F}_p[x]/(x^2 + 1)$.
2. (A) Show that $a + b\sqrt{-5}$ with $a, b \in \mathbb{Q}$ is integral over $\mathbb{Z}$ if and only if $a, b \in \mathbb{Z}$. (Hint: the trace $2a$ and the norm $a^2 + 5b^2$ are integers.) Show that $\mathfrak{q} = (3, 1 + \sqrt{-5})$ is not principal.
3. (A) Let $A$ be a Dedekind domain and $I, J$ nonzero ideals. Show that $I \subseteq J$ if and only if $I = JJ'$ for an ideal $J'$: to contain is to divide. Deduce that $v_\mathfrak{p}(I + J) = \min(v_\mathfrak{p}(I), v_\mathfrak{p}(J))$ for every $\mathfrak{p}$.
4. (B) Show that a Dedekind domain with finitely many maximal ideals is a principal ideal domain. (Hint: for each prime $\mathfrak{p}_i$ choose, by the Chinese remainder theorem, an element in $\mathfrak{p}_i \setminus \mathfrak{p}_i^2$ that lies outside the other $\mathfrak{p}_j$.)
5. (B) Let $A = \mathbb{Z}[\sqrt{-3}]$ and $\mathfrak{p} = (2, 1 + \sqrt{-3})$. Show that $A/\mathfrak{p} \cong \mathbb{F}_2$, that $\mathfrak{p}^2 = 2\mathfrak{p}$ and that $\mathfrak{p} \neq (2)$. Deduce that $\mathfrak{p}$ is not invertible and that $A_\mathfrak{p}$ is not a DVR.
6. (B) Let $A$ be a Dedekind domain and $S \subseteq A$ a multiplicative set with $0 \notin S$. Show that $S^{-1}A$ is a Dedekind domain, and that $\operatorname{Cl}(A) \to \operatorname{Cl}(S^{-1}A)$, $[I] \mapsto [S^{-1}I]$, is surjective with kernel generated by the classes of the primes that meet $S$. Compute $\operatorname{Cl}(\mathbb{Z}[\sqrt{-5}][1/2])$, using $\operatorname{Cl}(\mathbb{Z}[\sqrt{-5}]) \cong \mathbb{Z}/2$.
7. (B) Let $A$ be a Dedekind domain. Show that every nonzero ideal $I$ is generated by two elements, one of which can be any nonzero $a \in I$. (Hint: $A/aA$ is a product of quotients of DVRs, and every ideal of it is principal.)
8. (C) In the affine elliptic curve example, let $\sigma$ be the automorphism $y \mapsto -y$ of $A$ and $N(h) = h\sigma(h) \in k[x]$. Show that $A^* = k^*$. Show that if $\mathfrak{m} = (h)$, then $h^2 = cx$ with $c \in k^*$, and derive a contradiction by writing $h = a(x) + b(x)y$ and comparing degrees. So $\mathfrak{m}$ is not principal and its class has order $2$.

### Lean

Mathlib defines `IsDedekindDomain` as a Noetherian domain of dimension at most one that is integrally closed, as here, and proves its equivalence with two other definitions: `isDedekindDomain_iff_isDedekindDomainInv`, every nonzero fractional ideal is invertible, and `isDedekindDomain_iff_isDiscreteValuationRing_atPrime`, every localization at a nonzero prime is a DVR. The ideals of a Dedekind domain form a unique factorization monoid, `Ideal.uniqueFactorizationMonoid`. Fractional ideals are `FractionalIdeal`, and `ClassGroup` is defined for every domain by invertible fractional ideals, with `card_classGroup_eq_one_iff` for principal ideal domains. Mathlib proves that the integral closure of a Dedekind domain in a finite separable extension is Dedekind, `IsIntegralClosure.isDedekindDomain`, and that the class group of a ring of integers is finite. The handbook adds no `MinimalModel` node here.

### Notes and history

Kummer introduced ideal numbers in the 1840s to restore unique factorization in cyclotomic integers, and Dedekind replaced them by ideals in 1871, in his supplements to Dirichlet's lectures on number theory. Dedekind and Weber transferred the theory to algebraic functions of one variable in 1882. Emmy Noether gave the axiomatic characterization of Dedekind domains as Noetherian normal domains of dimension one in 1927. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 9, Matsumura, Chapter 4, and Eisenbud, Chapter 11.
