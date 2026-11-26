---
title: Rings and modules of fractions
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch3, Mat86:ch1, Eis95:ch2]
requires: [P1.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Rings and modules of fractions

### Statement

**Definition P1.2.1 (ring of fractions).** A subset $S \subseteq A$ is *multiplicative* if $1 \in S$ and $st \in S$ for $s, t \in S$. On $A \times S$ put $(a, s) \sim (b, t)$ if $u(at - bs) = 0$ for some $u \in S$. This is an equivalence relation; the class of $(a, s)$ is written $a/s$. The set $S^{-1}A$ of classes is a ring with $a/s + b/t = (at + bs)/st$ and $(a/s)(b/t) = ab/st$, and $a \mapsto a/1$ is a ring homomorphism $A \to S^{-1}A$. For an $A$-module $M$ the module $S^{-1}M$ is defined in the same way, with pairs $(m, s)$ and $m/s = n/t$ if $u(tm - sn) = 0$ for some $u \in S$.

Lean: Mathlib `Localization`, with the characteristic predicate `IsLocalization`, and `LocalizedModule` with `IsLocalizedModule` (definitions).

The element $u$ in the relation is needed for transitivity when $A$ has zero divisors. If $A$ is a domain and $0 \notin S$, one can drop it, and $S^{-1}A$ is a subring of the fraction field.

**Example P1.2.2.** For $f \in A$ the set $S = \{1, f, f^2, \dots\}$ is multiplicative, and $A_f = S^{-1}A$. One checks that $A_f \cong A[t]/(ft - 1)$. If $f$ is nilpotent then $0 \in S$ and $A_f = 0$.

**Example P1.2.3.** For a prime $\mathfrak{p}$ the set $S = A \setminus \mathfrak{p}$ is multiplicative, and $A_\mathfrak{p} = S^{-1}A$. For $A = \mathbb{Z}$ and $\mathfrak{p} = (p)$ this is the ring $\mathbb{Z}_{(p)}$ of fractions with denominator prime to $p$. For $\mathfrak{p} = (0)$ in a domain it is the fraction field.

**Proposition P1.2.4 (universal property).** Let $\varphi: A \to B$ be a ring homomorphism with $\varphi(s)$ a unit for every $s \in S$. Then there is a unique ring homomorphism $\psi: S^{-1}A \to B$ with $\psi(a/1) = \varphi(a)$, namely $\psi(a/s) = \varphi(a)\varphi(s)^{-1}$.

Lean: Mathlib `IsLocalization.lift` (a definition, with its properties proved in Mathlib).

*Proof.* Uniqueness: $\psi(a/s)\psi(s/1) = \psi(a/1)$, so $\psi(a/s) = \varphi(a)\varphi(s)^{-1}$. Existence: the formula is well defined, since $u(at - bs) = 0$ gives $\varphi(u)(\varphi(a)\varphi(t) - \varphi(b)\varphi(s)) = 0$, and $\varphi(u)$ is a unit. It is a ring homomorphism by a direct check. $\square$

**Theorem P1.2.5 (exactness of localization).** If $M' \xrightarrow{f} M \xrightarrow{g} M''$ is exact, then $S^{-1}M' \to S^{-1}M \to S^{-1}M''$ is exact. The map $S^{-1}A \otimes_A M \to S^{-1}M$, $(a/s) \otimes m \mapsto am/s$, is an isomorphism. Hence $S^{-1}A$ is a flat $A$-module.

Lean: Mathlib `IsLocalizedModule.map_exact`, `LocalizedModule.equivTensorProduct` and `IsLocalization.flat` (proved in Mathlib).

*Proof.* The composition is $0$. Let $m/s \in S^{-1}M$ with $g(m)/s = 0$. Then $u g(m) = 0$ for some $u \in S$, so $g(um) = 0$ and $um = f(m')$ for some $m' \in M'$. So $m/s = um/us$ is the image of $m'/us$. For the second claim, the map $(a/s, m) \mapsto am/s$ is well defined and bilinear, so the linear map exists. In the other direction send $m/s$ to $(1/s) \otimes m$. This is well defined: if $u(tm - sn) = 0$, then $(1/s) \otimes m = (1/stu) \otimes tum = (1/stu) \otimes sun = (1/t) \otimes n$. The two maps are inverse to each other on the elements $m/s$ and $(1/s) \otimes m$, and every element of $S^{-1}A \otimes M$ has the form $(1/s) \otimes m$, by bringing a finite sum to a common denominator. Flatness follows: an injective $M' \to M$ stays injective after $S^{-1}$, which is $S^{-1}A \otimes -$. $\square$

So localization commutes with kernels, cokernels, images, finite sums and finite intersections of submodules, and with quotients: $S^{-1}(M/N) \cong S^{-1}M/S^{-1}N$. For a finite intersection, apply exactness to $0 \to N \cap P \to M \to M/N \oplus M/P$.

**Theorem P1.2.6 (prime ideals of a localization).** Let $\varphi: A \to S^{-1}A$. The maps $\mathfrak{p} \mapsto S^{-1}\mathfrak{p}$ and $\mathfrak{q} \mapsto \varphi^{-1}(\mathfrak{q})$ are inverse bijections, preserving inclusion, between the prime ideals of $A$ that do not meet $S$ and the prime ideals of $S^{-1}A$.

Lean: Mathlib `IsLocalization.orderIsoOfPrime` and `IsLocalization.isPrime_iff_isPrime_disjoint` (proved in Mathlib).

*Proof.* Let $\mathfrak{q}$ be a prime of $S^{-1}A$. Then $\varphi^{-1}(\mathfrak{q})$ is prime, and it misses $S$ because $\varphi(s)$ is a unit. Every ideal $J$ of $S^{-1}A$ satisfies $J = S^{-1}\varphi^{-1}(J)$, since $a/s \in J$ if and only if $a/1 \in J$. Now let $\mathfrak{p}$ be a prime of $A$ with $\mathfrak{p} \cap S = \emptyset$. If $a/1 \in S^{-1}\mathfrak{p}$, then $a/1 = b/s$ with $b \in \mathfrak{p}$, so $u(sa - b) = 0$ for some $u \in S$. Then $usa \in \mathfrak{p}$ and $us \notin \mathfrak{p}$, so $a \in \mathfrak{p}$. This shows $\varphi^{-1}(S^{-1}\mathfrak{p}) = \mathfrak{p}$. In particular $1/1 \notin S^{-1}\mathfrak{p}$. If $(a/s)(b/t) \in S^{-1}\mathfrak{p}$, then $ab/1 \in S^{-1}\mathfrak{p}$, so $ab \in \mathfrak{p}$, and $a$ or $b$ is in $\mathfrak{p}$. So $S^{-1}\mathfrak{p}$ is prime. $\square$

**Corollary P1.2.7 (local rings at primes).** The ring $A_\mathfrak{p}$ is local with maximal ideal $\mathfrak{p}A_\mathfrak{p}$. Its primes correspond to the primes of $A$ contained in $\mathfrak{p}$. Its residue field $\kappa(\mathfrak{p}) = A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$ is the fraction field of $A/\mathfrak{p}$.

Lean: Mathlib `Localization.AtPrime`, the instance `Localization.AtPrime.isLocalRing`, and `Ideal.ResidueField` (proved in Mathlib).

*Proof.* The primes of $A$ disjoint from $A \setminus \mathfrak{p}$ are the primes contained in $\mathfrak{p}$. They all lie in $\mathfrak{p}$, so their images all lie in $\mathfrak{p}A_\mathfrak{p}$, which is the unique maximal ideal. Since localization commutes with quotients, $A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$ is the localization of $A/\mathfrak{p}$ at the image of $A \setminus \mathfrak{p}$, which is the set of nonzero elements of the domain $A/\mathfrak{p}$. $\square$

**Theorem P1.2.8 (local properties).** Let $M$ be an $A$-module. The following are equivalent: (a) $M = 0$; (b) $M_\mathfrak{p} = 0$ for every prime $\mathfrak{p}$; (c) $M_\mathfrak{m} = 0$ for every maximal ideal $\mathfrak{m}$. A linear map $u: M \to N$ is injective, or surjective, if and only if $u_\mathfrak{m}: M_\mathfrak{m} \to N_\mathfrak{m}$ is injective, or surjective, for every maximal $\mathfrak{m}$.

Lean: Mathlib `Module.subsingleton_of_localization_maximal`, `injective_of_isLocalized_maximal` and `surjective_of_isLocalized_maximal` (proved in Mathlib).

*Proof.* Clearly (a) implies (b) and (b) implies (c). Assume (c) and let $x \in M$ with $x \neq 0$. The annihilator $\operatorname{Ann}(x)$ is a proper ideal, so it lies in a maximal ideal $\mathfrak{m}$ by Krull's theorem. In $M_\mathfrak{m}$ the element $x/1$ is zero, so $sx = 0$ for some $s \notin \mathfrak{m}$. But $s \in \operatorname{Ann}(x) \subseteq \mathfrak{m}$, a contradiction. For the map $u$, the exactness of localization gives $(\ker u)_\mathfrak{m} = \ker(u_\mathfrak{m})$ and $(\operatorname{coker} u)_\mathfrak{m} = \operatorname{coker}(u_\mathfrak{m})$. Apply the first part to $\ker u$ and $\operatorname{coker} u$. $\square$

### Proof in words

A ring of fractions inverts the elements of $S$ and does nothing else. It is exact because a fraction that maps to zero is killed by an element of $S$, which one can absorb into the numerator. Its primes are the primes that $S$ does not meet, because the primes that meet $S$ become the unit ideal. A module is zero if it is zero near every point, since a nonzero element has a proper annihilator and a maximal ideal above it.

In geometry, let $X$ be an affine variety with $A = k[X]$. The ring $A_f$ is the coordinate ring of the open set $D(f) = \{x : f(x) \neq 0\}$, which is again affine: it is the closed subset $ft = 1$ of $X \times \mathbb{A}^1$. The local ring $A_\mathfrak{m}$ at the point $x$ is the ring $\mathcal{O}_{X, x}$ of rational functions regular at $x$. For a prime $\mathfrak{p}$ with irreducible zero set $Z$, the ring $A_\mathfrak{p}$ is the ring of rational functions defined at some point of $Z$, and hence on an open dense subset of $Z$. The residue field $\kappa(\mathfrak{p})$ is the function field $k(Z)$. When $Z$ is a prime divisor on a normal variety, $A_\mathfrak{p}$ is a discrete valuation ring (P1 Ch. 7), and the order of vanishing along $Z$ is its valuation. This is where the discrepancies of Volume 4 are computed.

### Examples

**Example P1.2.9 (germs at a point).** Let $A = k[x]$ and $\mathfrak{m} = (x)$. Then $A_\mathfrak{m} = \{f/g : g(0) \neq 0\}$, the rational functions regular at $0$. Its maximal ideal is $xA_\mathfrak{m}$ and every nonzero element is $x^n u$ with $u$ a unit. The primes of $A_\mathfrak{m}$ are $(0)$ and $(x)$: the primes $(x - a)$ with $a \neq 0$ become the unit ideal, because $x - a$ is a unit.

**Example P1.2.10 (localization of a product).** Let $A = k \times k$ and $e = (1, 0)$. Then $A_e \cong k$, by $(a, b)/e^n \mapsto a$, since $(1 - e) \cdot e = 0$ kills the second factor. The two primes of $A$ are $k \times 0$ and $0 \times k$, and the localization at each is $k$. So every localization of $A$ is a domain, but $A$ is not. Being a domain is not a local property.

**Example P1.2.11 (locally free but not free).** Let $A = \mathbb{Z}[\sqrt{-5}]$ and $\mathfrak{p} = (2, 1 + \sqrt{-5})$. The map $A \to \mathbb{Z}/2$, $a + b\sqrt{-5} \mapsto a + b \bmod 2$, is onto with kernel $\mathfrak{p}$, so $\mathfrak{p}$ is maximal. For a maximal $\mathfrak{m} \neq \mathfrak{p}$ one has $\mathfrak{p}_\mathfrak{m} = A_\mathfrak{m}$. In $A_\mathfrak{p}$ the element $3$ is a unit, as $3 \notin \mathfrak{p}$, and $2 = (1 + \sqrt{-5})(1 - \sqrt{-5})/3$. So $\mathfrak{p}A_\mathfrak{p} = (1 + \sqrt{-5})$. Thus $\mathfrak{p}$ is locally free of rank $1$. It is not free. A free nonzero ideal of a domain has rank $1$, since any two elements $a, b$ satisfy $b \cdot a - a \cdot b = 0$, so it is principal. If $\mathfrak{p} = (\alpha)$, the norm $N(\alpha) = \alpha\bar\alpha$ divides $N(2) = 4$ and $N(1 + \sqrt{-5}) = 6$, so $N(\alpha) \in \{1, 2\}$. No element $a + b\sqrt{-5}$ has norm $a^2 + 5b^2 = 2$, and norm $1$ makes $\alpha$ a unit, which is false as $\mathfrak{p} \neq A$. Freeness is not a local property, while local freeness is the notion that sheaf theory sees: $\mathfrak{p}$ is a line bundle on $\operatorname{Spec} A$ that is not trivial.

**Example P1.2.12 (an algebraic form of the punctured line).** Let $A = k[x]$. Then $A_x = k[x, x^{-1}]$, the coordinate ring of $\mathbb{A}^1 \setminus \{0\}$. Its maximal ideals are the $(x - a)$ with $a \neq 0$, as the theorem on primes predicts.

### Exercises

1. (A) Show that $S^{-1}A = 0$ if and only if $0 \in S$. Show that $A_f \cong A[t]/(ft - 1)$.
2. (A) Show that $S^{-1}\sqrt{I} = \sqrt{S^{-1}I}$. Deduce that $A$ is reduced if and only if $A_\mathfrak{p}$ is reduced for every prime $\mathfrak{p}$.
3. (A) Show that $S^{-1}(N + P) = S^{-1}N + S^{-1}P$ and $S^{-1}(N \cap P) = S^{-1}N \cap S^{-1}P$ for submodules $N, P \subseteq M$. Show by an example that $S^{-1}$ does not commute with infinite intersections.
4. (B) Let $A$ be a domain with fraction field $K$. Show that $A = \bigcap_\mathfrak{m} A_\mathfrak{m}$ inside $K$, over all maximal ideals.
5. (B) Let $M$ be finitely generated. Show that $S^{-1}M = 0$ if and only if $sM = 0$ for some $s \in S$. The *support* of $M$ is the set of primes $\mathfrak{p}$ with $M_\mathfrak{p} \neq 0$. Deduce that for $M$ finitely generated the support is the set of primes that contain $\operatorname{Ann}(M)$.
6. (B) Let $A = k[x, y]/(xy)$ and $\mathfrak{p} = (x)$. Show that $A_\mathfrak{p} \cong k(y)$, a field. Interpret: near a general point of the line $x = 0$, the other line is not seen.
7. (C) Let $M$ be finitely presented and $N$ any module. Show that $S^{-1}\operatorname{Hom}_A(M, N) \cong \operatorname{Hom}_{S^{-1}A}(S^{-1}M, S^{-1}N)$. Give an example where this fails for $M$ not finitely generated.

### Lean

Mathlib builds the ring of fractions as `Localization`, with the characteristic predicate `IsLocalization` and the universal map `IsLocalization.lift`. The localization at a prime is `Localization.AtPrime`, local by the instance `Localization.AtPrime.isLocalRing`. The module of fractions is `LocalizedModule`, with exactness `IsLocalizedModule.map_exact` and the tensor description `LocalizedModule.equivTensorProduct`. Flatness is `IsLocalization.flat`. The prime correspondence is `IsLocalization.orderIsoOfPrime`. The local criteria are in `Mathlib.RingTheory.LocalProperties`, for example `Module.subsingleton_of_localization_maximal` and `injective_of_isLocalized_maximal`. The handbook adds no `MinimalModel` node here.

### Notes and history

Localization at a prime goes back to Krull's work on local rings in the 1930s and to Grell's rings of fractions of 1927. Chevalley and Zariski made the local ring the main tool of birational geometry in the 1940s. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 3. P3 glues the rings $A_f$ into the structure sheaf of $\operatorname{Spec} A$, and P1 Ch. 7 studies $A_\mathfrak{p}$ when $\mathfrak{p}$ has height one.
