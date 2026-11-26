---
title: The Lasker-Noether theorem and associated primes
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch7, Mat86:ch2, Eis95:ch3]
requires: [P1.1, P1.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Lasker-Noether theorem and associated primes

### Statement

This section uses the Noetherian condition, which Chapter 3 studies in detail. A ring $A$ is *Noetherian* if every nonempty set of ideals of $A$ has a maximal element. Equivalently, every increasing chain $I_1 \subseteq I_2 \subseteq \dots$ of ideals is eventually constant: a chain without a last term would be a set without a maximal element, and conversely a nonempty set without a maximal element contains such a chain, by dependent choice. Fields, principal ideal domains and quotients of Noetherian rings are Noetherian. By the Hilbert basis theorem of Chapter 3, so is every finitely generated algebra over a Noetherian ring, for example $k[X]$ for an affine variety $X$.

**Definition P1.2.39 (irreducible ideal).** An ideal $I \neq A$ is *irreducible* if $I = J \cap K$ implies $I = J$ or $I = K$.

Lean: Mathlib `InfIrred` (a definition, for elements of any lattice).

**Theorem P1.2.40 (Lasker-Noether).** In a Noetherian ring every ideal $I \neq A$ is a finite intersection of irreducible ideals, and every irreducible ideal is primary. So every ideal has a primary decomposition, and a minimal one.

Lean: Mathlib `Submodule.isLasker` and `InfIrred.isPrimary` (proved in Mathlib).

*Proof.* Suppose the set of proper ideals that are not finite intersections of irreducible ideals is nonempty, and let $I$ be a maximal element. Then $I$ is not irreducible, so $I = J \cap K$ with $J \neq I \neq K$. Then $J, K$ strictly contain $I$, they are proper, and by maximality they are finite intersections of irreducible ideals. So $I$ is one too, a contradiction.

Now let $\mathfrak{q}$ be irreducible. Pass to $B = A/\mathfrak{q}$, where $(0)$ is irreducible. Let $xy = 0$ in $B$ with $y \neq 0$; the task is to show that $x$ is nilpotent. The chain $\operatorname{Ann}(x) \subseteq \operatorname{Ann}(x^2) \subseteq \dots$ is eventually constant, say $\operatorname{Ann}(x^n) = \operatorname{Ann}(x^{n+1})$. Then $(x^n) \cap (y) = 0$. Indeed, an element $a$ of the intersection satisfies $ax = 0$, since $a \in (y)$ and $xy = 0$. Write $a = bx^n$. Then $bx^{n+1} = 0$, so $b \in \operatorname{Ann}(x^{n+1}) = \operatorname{Ann}(x^n)$, and $a = bx^n = 0$. Since $(0)$ is irreducible and $(y) \neq 0$, $(x^n) = 0$. $\square$

**Definition P1.2.41 (associated prime, support).** Let $M$ be an $A$-module. A prime $\mathfrak{p}$ is *associated* to $M$ if $\mathfrak{p} = \operatorname{Ann}(x)$ for some $x \in M$; equivalently, $A/\mathfrak{p}$ is isomorphic to a submodule of $M$. The set of these primes is $\operatorname{Ass}(M)$. The *support* $\operatorname{Supp}(M)$ is the set of primes $\mathfrak{p}$ with $M_\mathfrak{p} \neq 0$.

Lean: Mathlib `IsAssociatedPrime`, `associatedPrimes` and `Module.support` (definitions).

**Example P1.2.42.** $\operatorname{Ass}(A/\mathfrak{p}) = \{\mathfrak{p}\}$ for a prime $\mathfrak{p}$, since every nonzero element of the domain $A/\mathfrak{p}$ has annihilator $\mathfrak{p}$. $\operatorname{Ass}(\mathbb{Z}/12) = \{(2), (3)\}$, from the elements $6$ and $4$.

**Example P1.2.43.** For $A = k[x, y]$ and $M = A/(x^2, xy)$, $\operatorname{Ann}(1) = (x^2, xy)$ is not prime, $\operatorname{Ann}(y) = (x)$ and $\operatorname{Ann}(x) = (x, y)$. So $\operatorname{Ass}(M) \supseteq \{(x), (x, y)\}$, and the theorems below show equality.

**Proposition P1.2.44 (existence and zero divisors).** Let $A$ be Noetherian and $M$ an $A$-module. Every maximal element of the set $\{\operatorname{Ann}(x) : x \in M, x \neq 0\}$ is prime. Hence $\operatorname{Ass}(M) \neq \emptyset$ if $M \neq 0$, and the set of zero divisors on $M$, the $a \in A$ with $ax = 0$ for some $x \neq 0$, is the union of the associated primes.

Lean: Mathlib `associatedPrimes.nonempty` and `biUnion_associatedPrimes_eq_zero_divisors` (proved in Mathlib).

*Proof.* Let $\operatorname{Ann}(x)$ be maximal in the set. It is proper since $x \neq 0$. Let $ab \in \operatorname{Ann}(x)$ with $b \notin \operatorname{Ann}(x)$. Then $bx \neq 0$, and $\operatorname{Ann}(bx)$ contains $\operatorname{Ann}(x)$ and $a$. By maximality, $\operatorname{Ann}(bx) = \operatorname{Ann}(x)$, so $a \in \operatorname{Ann}(x)$. If $ax = 0$ with $x \neq 0$, the set of $\operatorname{Ann}(y)$, $y \neq 0$, that contain $\operatorname{Ann}(x)$ is nonempty and has a maximal element, which is maximal in the whole set and is a prime that contains $a$. Conversely every element of an associated prime $\operatorname{Ann}(x)$ kills $x \neq 0$. $\square$

**Lemma P1.2.45 (exact sequences).** Let $0 \to M' \to M \to M'' \to 0$ be exact. Then $\operatorname{Ass}(M') \subseteq \operatorname{Ass}(M) \subseteq \operatorname{Ass}(M') \cup \operatorname{Ass}(M'')$.

Lean: Mathlib `associatedPrimes.subset_of_injective` and `associatedPrimes.subset_union_of_exact` (proved in Mathlib).

*Proof.* The first inclusion is clear. Let $\mathfrak{p} = \operatorname{Ann}(x) \in \operatorname{Ass}(M)$, so $Ax \cong A/\mathfrak{p}$. If $Ax \cap M' \neq 0$, pick $ax \neq 0$ in it. Then $a \notin \mathfrak{p}$, and $bax = 0$ if and only if $ba \in \mathfrak{p}$, if and only if $b \in \mathfrak{p}$. So $\operatorname{Ann}(ax) = \mathfrak{p}$ and $\mathfrak{p} \in \operatorname{Ass}(M')$. If $Ax \cap M' = 0$, then $Ax$ maps injectively to $M''$ and the image of $x$ has annihilator $\mathfrak{p}$. $\square$

**Theorem P1.2.46 (finiteness of associated primes).** Let $A$ be Noetherian and $M$ a finitely generated $A$-module. There is a chain $0 = M_0 \subsetneq M_1 \subsetneq \dots \subsetneq M_n = M$ with $M_i/M_{i-1} \cong A/\mathfrak{p}_i$ for primes $\mathfrak{p}_i$. For any such chain, $\operatorname{Ass}(M) \subseteq \{\mathfrak{p}_1, \dots, \mathfrak{p}_n\}$. In particular $\operatorname{Ass}(M)$ is finite.

Lean: Mathlib `associatedPrimes.finite` and `IsNoetherianRing.exists_relSeries_isQuotientEquivQuotientPrime` (proved in Mathlib).

*Proof.* First, $M$ has the ascending chain condition on submodules. For $A^m$ this follows by induction on $m$: given a chain $N_1 \subseteq N_2 \subseteq \dots$ in $A^m$, the chains $N_j \cap A^{m-1}$ and the images of $N_j$ under the last coordinate $A^m \to A$ are eventually constant, and if $N \subseteq N'$ have the same intersection with $A^{m-1}$ and the same image, then $N = N'$. A quotient of $A^m$ inherits the condition. Now if $M \neq 0$, the proposition gives $x_1 \in M$ with $\operatorname{Ann}(x_1) = \mathfrak{p}_1$ prime; put $M_1 = Ax_1 \cong A/\mathfrak{p}_1$. Repeat with $M/M_1$, and so on. The chain $M_1 \subsetneq M_2 \subsetneq \dots$ of submodules of $M$ must stop, and it stops only when $M_n = M$. For the second claim apply the lemma $n - 1$ times: $\operatorname{Ass}(M) \subseteq \bigcup_i \operatorname{Ass}(M_i/M_{i-1}) = \{\mathfrak{p}_1, \dots, \mathfrak{p}_n\}$. $\square$

**Theorem P1.2.47 (associated primes and primary decomposition).** Let $A$ be Noetherian and $I = \mathfrak{q}_1 \cap \dots \cap \mathfrak{q}_n$ a minimal primary decomposition with $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$. Then $\operatorname{Ass}(A/I) = \{\mathfrak{p}_1, \dots, \mathfrak{p}_n\}$. In particular the zero divisors of $A/I$ are the elements of $\mathfrak{p}_1 \cup \dots \cup \mathfrak{p}_n$, modulo $I$.

Lean: Mathlib `Submodule.IsMinimalPrimaryDecomposition.image_radical_eq_associated_primes` and `associatedPrimes.eq_singleton_of_isPrimary` (proved in Mathlib).

*Proof.* First, if $\mathfrak{q}$ is $\mathfrak{p}$-primary, then $\operatorname{Ass}(A/\mathfrak{q}) = \{\mathfrak{p}\}$. The set is nonempty. An associated prime is $\operatorname{Ann}(\bar x) = (\mathfrak{q} : x)$ for some $x \notin \mathfrak{q}$, which is $\mathfrak{p}$-primary by the lemma of Section 2.3. A prime that is $\mathfrak{p}$-primary equals its radical $\mathfrak{p}$.

Now $A/I$ embeds in $\bigoplus_i A/\mathfrak{q}_i$, so by the lemma on exact sequences, applied to the summands, $\operatorname{Ass}(A/I) \subseteq \{\mathfrak{p}_1, \dots, \mathfrak{p}_n\}$. Conversely fix $i$ and choose $x \in \bigcap_{j \neq i} \mathfrak{q}_j$ with $x \notin \mathfrak{q}_i$, by minimality. Then $Q = (I : x) = (\mathfrak{q}_i : x)$ is $\mathfrak{p}_i$-primary. As $A$ is Noetherian, $\mathfrak{p}_i$ is finitely generated, by $a_1, \dots, a_r$ say, with $a_j^{e} \in Q$ for all $j$. Then $\mathfrak{p}_i^{r(e - 1) + 1} \subseteq Q$, since each monomial of that degree in the $a_j$ has some exponent $\geq e$. Let $m \geq 1$ be least with $\mathfrak{p}_i^m \subseteq Q$ ($m \geq 1$ because $Q \neq A$), and choose $y \in \mathfrak{p}_i^{m-1}$ with $y \notin Q$. Then $(I : xy) = (Q : y)$ contains $\mathfrak{p}_i$, since $\mathfrak{p}_i y \subseteq \mathfrak{p}_i^m \subseteq Q$, and it is $\mathfrak{p}_i$-primary, hence contained in $\mathfrak{p}_i$. So $\operatorname{Ann}(\overline{xy}) = \mathfrak{p}_i$. The last claim is the proposition on zero divisors. $\square$

**Theorem P1.2.48 (minimal primes of the support).** Let $A$ be Noetherian and $M$ finitely generated. Then $\operatorname{Supp}(M) = V(\operatorname{Ann} M)$, and the minimal elements of $\operatorname{Supp}(M)$ are associated primes of $M$. So $\operatorname{Ass}(M)$ consists of the generic points of the irreducible components of $\operatorname{Supp}(M)$, which are the *minimal* associated primes, and possibly further *embedded* primes.

Lean: Mathlib `Module.support_eq_zeroLocus` and `Module.associatedPrimes.minimalPrimes_annihilator_subset_associatedPrimes` (proved in Mathlib).

*Proof.* The first claim is Exercise 5 of Section 2.1. Let $\mathfrak{p}$ be minimal in $\operatorname{Supp}(M)$. By the proposition on existence, applied over the Noetherian ring $A_\mathfrak{p}$, there is $x/s \in M_\mathfrak{p}$ whose annihilator $Q$ is prime; replacing $x/s$ by $x/1$ does not change $Q$. Let $\mathfrak{q} = Q \cap A$, a prime contained in $\mathfrak{p}$, generated by $a_1, \dots, a_r$. Since $a_jx/1 = 0$ there are $t_j \notin \mathfrak{p}$ with $t_ja_jx = 0$. Put $t = t_1 \cdots t_r$. Then $\operatorname{Ann}(tx) \supseteq \mathfrak{q}$. If $btx = 0$, then $bx/1 = 0$ and $b \in \mathfrak{q}$. So $\operatorname{Ann}(tx) = \mathfrak{q}$ and $\mathfrak{q} \in \operatorname{Ass}(M)$. Then $M_\mathfrak{q} \supseteq (A/\mathfrak{q})_\mathfrak{q} \neq 0$ by exactness of localization, so $\mathfrak{q} \in \operatorname{Supp}(M)$, and $\mathfrak{q} = \mathfrak{p}$ by minimality. $\square$

**Proposition P1.2.49 (flatness over a principal ideal domain).** Let $R$ be a principal ideal domain, $B$ a Noetherian $R$-algebra and $M$ a $B$-module. Then $M$ is flat over $R$ if and only if $\mathfrak{P} \cap R = 0$ for every $\mathfrak{P} \in \operatorname{Ass}_B(M)$.

Lean: Mathlib proves the ingredients, `Module.Flat.flat_iff_torsion_eq_bot_of_isBezout` and `biUnion_associatedPrimes_eq_zero_divisors`; the handbook does not name a single declaration.

*Proof.* By Section 1.4, $M$ is flat over $R$ if and only if no nonzero $a \in R$ is a zero divisor on $M$. By the proposition on zero divisors over the Noetherian ring $B$, the image of $a$ is a zero divisor on $M$ if and only if it lies in some $\mathfrak{P} \in \operatorname{Ass}_B(M)$, that is, $a \in \mathfrak{P} \cap R$. $\square$

### Proof in words

In a Noetherian ring, an ideal that cannot be written as a finite intersection of irreducible ideals would have a largest such counterexample, which is impossible. An irreducible ideal is primary, by a chain of annihilators that must stop. The associated primes of a module are the primes that occur as annihilators of single elements. They exist because a largest annihilator is prime, they are finite because a finitely generated module is built from finitely many pieces $A/\mathfrak{p}$, and for $M = A/I$ they are the primes of any minimal primary decomposition.

In geometry, the associated primes of $A/I$ are the generic points of the irreducible components of $V(I)$, together with the embedded points. A family $\operatorname{Spec} B \to C$ over a smooth affine curve with coordinate ring a principal ideal domain is flat exactly when every associated point of $\operatorname{Spec} B$ lies over the generic point of $C$. In words: no component and no embedded component sits inside a fibre. The same holds over any smooth curve, with a Dedekind domain in place of a principal ideal domain (P1 Ch. 7). This is the criterion that the stable reduction of Volume 13 checks for a family over a curve.

### Examples

**Example P1.2.50 (a line with an embedded point).** Let $M = A/(x^2, xy)$ over $A = k[x, y]$. The decomposition $(x^2, xy) = (x) \cap (x, y)^2$ and the theorem on decompositions give $\operatorname{Ass}(M) = \{(x), (x, y)\}$. The support is $V(x)$, the line, with generic point $(x)$, and $(x, y)$ is embedded. The zero divisors on $M$ are the elements of $(x, y)$.

**Example P1.2.51 (an embedded point breaks flatness).** Let $R = k[t]$ and $B = k[t, x]/(tx, x^2)$. The reduced space of $\operatorname{Spec} B$ is the $t$-line, so every fibre is a single point. But the class of $x$ is nonzero and has annihilator $(t, x)$, so $(t, x) \in \operatorname{Ass}(B)$, and $(t, x) \cap R = (t) \neq 0$. By the proposition, $B$ is not flat over $R$. Indeed the fibre over $t = a \neq 0$ is $k[x]/(x)$, of dimension $1$, and the fibre over $t = 0$ is $k[x]/(x^2)$, of dimension $2$.

**Example P1.2.52 (associated primes need not exist).** Let $A$ be the ring of all $\sum c_q t^q$, finite sums over exponents $q \in \mathbb{Q}_{\geq 0}$. It is not Noetherian: the ideals $(t^{1/n})$ increase strictly. Let $M = A/(t)$, which is nonzero. A nonzero $x \in M$ is the class of an $f$ whose lowest exponent $a$ is $< 1$. Then $t^{1-a} \in \operatorname{Ann}(x)$, while $t^{(1-a)/2} \notin \operatorname{Ann}(x)$, since $t^{(1-a)/2}f$ has lowest exponent $(1 + a)/2 < 1$. So no annihilator is prime and $\operatorname{Ass}(M) = \emptyset$. Note that $(t)$ has radical the maximal ideal $(t^q : q > 0)$, so it is primary, and the formula $\operatorname{Ass}(A/\mathfrak{q}) = \{\sqrt{\mathfrak{q}}\}$ fails. The Noetherian hypothesis is needed.

### Exercises

1. (A) Compute $\operatorname{Ass}$ and $\operatorname{Supp}$ of $\mathbb{Z}/60$, of $\mathbb{Q}/\mathbb{Z}$ over $\mathbb{Z}$, and of $k[x, y]/(x^2y)$.
2. (A) Show that $\operatorname{Ass}(M \oplus N) = \operatorname{Ass}(M) \cup \operatorname{Ass}(N)$.
3. (A) Show that in a Noetherian ring a radical ideal is the intersection of finitely many primes, and that $V(I)$ has finitely many irreducible components.
4. (B) Show that $(x, y)^2 \subseteq k[x, y]$ is primary but not irreducible. Show that $(x, y^2)$ is irreducible.
5. (B) Let $A$ be Noetherian and $S$ multiplicative. Show that $\operatorname{Ass}_{S^{-1}A}(S^{-1}M)$ is the set of $S^{-1}\mathfrak{p}$ with $\mathfrak{p} \in \operatorname{Ass}(M)$ and $\mathfrak{p} \cap S = \emptyset$.
6. (B) Let $R = k[t]$ and $B = k[t, x, y]/(xy, t x)$. Find $\operatorname{Ass}(B)$ and decide whether $B$ is flat over $R$. Describe the fibres.
7. (C) Let $A$ be Noetherian and $M$ finitely generated. Show that $\operatorname{Ass}(M) = \{\mathfrak{p}\}$ for a single prime $\mathfrak{p}$ if and only if $(0)$ is a $\mathfrak{p}$-primary submodule of $M$, that is, every zero divisor on $M$ is nilpotent on $M$ and lies in $\mathfrak{p}$.

### Lean

Mathlib proves the Lasker-Noether theorem for submodules of Noetherian modules as `Submodule.isLasker`, with `InfIrred.isPrimary` for the step from irreducible to primary. Associated primes are `IsAssociatedPrime` and `associatedPrimes`, with `associatedPrimes.nonempty`, `associatedPrimes.finite` and `biUnion_associatedPrimes_eq_zero_divisors`. The prime filtration is `IsNoetherianRing.exists_relSeries_isQuotientEquivQuotientPrime`. The handbook adds no `MinimalModel` node here.

### Notes and history

Noether proved the decomposition into irreducible ideals and the step from irreducible to primary in her 1921 paper. Associated primes of modules and the language of $\operatorname{Ass}$ come from Bourbaki's Algèbre commutative and from the work of Serre and Grothendieck in the 1950s. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapters 4 and 7, and Matsumura, Chapter 2. P1 Ch. 10 uses associated primes to define depth, and P1 Ch. 11 uses them for Serre's conditions.
