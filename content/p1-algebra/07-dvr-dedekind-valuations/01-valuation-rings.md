---
title: Valuation rings
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch5, Mat86:ch4, Eis95:ch11]
requires: [P1.1, P1.2, P1.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Valuation rings

### Statement

Throughout, $K$ is a field. A subring of $K$ is a domain, and for a subring $A$ write $A^*$ for its group of units.

**Definition P1.7.1 (valuation ring).** A subring $V \subseteq K$ is a *valuation ring of $K$* if for every $x \in K^* = K \setminus \{0\}$, at least one of $x$ and $x^{-1}$ lies in $V$. A domain is a *valuation ring* if it is a valuation ring of its fraction field.

Lean: Mathlib `ValuationRing` (class on a domain) and `ValuationSubring` (valuation rings of a given field), with `ValuationRing.iff_isInteger_or_isInteger` for the form used here.

If $V$ is a valuation ring of $K$, then $K$ is the fraction field of $V$, since every $x \in K^*$ is $x/1$ or $1/x^{-1}$ with $x$ or $x^{-1}$ in $V$. The field $K$ itself is a valuation ring of $K$, the *trivial* one.

**Proposition P1.7.2 (first properties).** Let $V$ be a valuation ring of $K$.

1. The ideals of $V$ are totally ordered by inclusion. In particular $V$ is local, and its prime ideals form a chain.
2. Every finitely generated ideal of $V$ is principal.
3. $V$ is normal.
4. Every ring $W$ with $V \subseteq W \subseteq K$ is a valuation ring of $K$, and $W = V_\mathfrak{p}$ for the prime $\mathfrak{p} = \mathfrak{m}_W \cap V$, where $\mathfrak{m}_W$ is the maximal ideal of $W$.

Lean: Mathlib `ValuationRing.iff_ideal_total`, the instance `ValuationRing.isLocalRing`, `ValuationRing.iff_local_bezout_domain` and `Valuation.Integers.isIntegrallyClosed` (proved in Mathlib).

*Proof.* (1) Let $I, J$ be ideals with $I \not\subseteq J$, and pick $a \in I \setminus J$. Let $b \in J$ with $b \neq 0$. If $a/b \in V$, then $a = (a/b) b \in J$, which is false. So $b/a \in V$, and $b = (b/a) a \in I$. Hence $J \subseteq I$. A ring whose ideals form a chain has at most one maximal ideal, so $V$ is local. (2) If $I = (a_1, \dots, a_n)$, the principal ideals $(a_i)$ form a chain by (1), and $I$ is the largest of them. (3) Let $x \in K$ be integral over $V$, with $x^n + a_1 x^{n-1} + \dots + a_n = 0$ and $a_i \in V$. If $x \notin V$, then $x^{-1} \in V$, and multiplication of the equation by $x^{1-n}$ gives $x = -(a_1 + a_2 x^{-1} + \dots + a_n x^{1-n}) \in V$, a contradiction. (4) $W$ is a valuation ring, since it contains $V$. The ideal $\mathfrak{p} = \mathfrak{m}_W \cap V$ is prime. An element of $V \setminus \mathfrak{p}$ lies in $W$ and not in $\mathfrak{m}_W$, so it is a unit of $W$, and so $V_\mathfrak{p} \subseteq W$. Conversely let $x \in W \setminus V$. Then $x^{-1} \in V$. If $x^{-1} \in \mathfrak{m}_W$, then $1 = x \cdot x^{-1} \in \mathfrak{m}_W$, which is false. So $x^{-1} \in V \setminus \mathfrak{p}$, and $x = 1/x^{-1} \in V_\mathfrak{p}$. $\square$

**Definition P1.7.3 (valuation).** Let $\Gamma$ be a totally ordered abelian group, written additively. A *valuation* of $K$ with values in $\Gamma$ is a surjective group homomorphism $v: K^* \to \Gamma$ with
$$
v(x + y) \geq \min(v(x), v(y)) \quad \text{whenever } x, y, x + y \in K^* .
$$
One puts $v(0) = \infty$. The set $V_v = \{x \in K : v(x) \geq 0\}$ is the *valuation ring of $v$*, and $\Gamma$ is the *value group*. Two valuations are *equivalent* if they differ by an isomorphism of ordered groups. A *discrete valuation* is a valuation with value group $\mathbb{Z}$.

Lean: Mathlib `Valuation`, written multiplicatively with values in a `LinearOrderedCommGroupWithZero`, and `Valuation.integer` for its valuation ring.

**Proposition P1.7.4 (valuations and valuation rings).** For a valuation $v$ of $K$, $V_v$ is a valuation ring of $K$ with maximal ideal $\{x : v(x) > 0\}$ and units $\{x : v(x) = 0\}$. Conversely, let $V$ be a valuation ring of $K$ and put $\Gamma_V = K^*/V^*$, ordered by $xV^* \leq yV^*$ if $y/x \in V$. Then $\Gamma_V$ is a totally ordered abelian group, and the quotient map $v: K^* \to \Gamma_V$ is a valuation with $V_v = V$. The two constructions are inverse up to equivalence.

Lean: Mathlib `ValuationRing.ValueGroup` and `ValuationRing.valuation`, with `ValuationRing.range_algebraMap_eq` (proved in Mathlib).

*Proof.* Let $v$ be a valuation. Since $v(1) = 0$ and $v(-1) + v(-1) = v(1) = 0$ in a torsion free group, $v(-1) = 0$, and so $v(-x) = v(x)$. The rule for sums then shows that $V_v$ is closed under addition and subtraction, and it is closed under products since $v$ is a homomorphism. For $x \in K^*$, $v(x) \geq 0$ or $v(x^{-1}) = -v(x) \geq 0$. So $V_v$ is a valuation ring. An element $x \in V_v$ is a unit of $V_v$ exactly when $v(x^{-1}) \geq 0$, that is when $v(x) = 0$, and the nonunits form the maximal ideal.

Conversely let $V$ be a valuation ring. The relation on $\Gamma_V$ does not depend on the representatives, since units do not change membership in $V$. It is reflexive and transitive, it is antisymmetric since $y/x$ and $x/y$ in $V$ means that $y/x$ is a unit, and it is total since $y/x$ or $x/y$ lies in $V$. It is compatible with the group law, since $(yz)/(xz) = y/x$. Let $x, y, x + y \in K^*$, and suppose $v(x) \leq v(y)$, that is $y/x \in V$. Then $(x + y)/x = 1 + y/x \in V$, so $v(x + y) \geq v(x)$. Finally $v(x) \geq 0 = v(1)$ means $x/1 \in V$. So $V_v = V$. If $v$ is any valuation with $V_v = V$, then $v(x) \leq v(y)$ if and only if $v(y/x) \geq 0$, if and only if $y/x \in V$, so $v$ is equivalent to the quotient map. $\square$

For a local ring $(A, \mathfrak{m})$ and a local ring $(B, \mathfrak{n})$ with $A \subseteq B$, say that $B$ *dominates* $A$ if $\mathfrak{n} \cap A = \mathfrak{m}$.

**Theorem P1.7.5 (existence of valuation rings).** Let $A \subseteq K$ be a subring and $\mathfrak{p}$ a prime of $A$. Then there is a valuation ring $V$ of $K$ with $A \subseteq V$ and $\mathfrak{m}_V \cap A = \mathfrak{p}$. In particular every local subring of $K$ is dominated by a valuation ring of $K$.

Lean: Mathlib `LocalSubring.exists_le_valuationSubring` (proved in Mathlib), where the order on `LocalSubring` is domination.

*Proof.* The localization $A_\mathfrak{p}$ is a local subring of $K$ with maximal ideal $\mathfrak{p}A_\mathfrak{p}$, and $\mathfrak{p}A_\mathfrak{p} \cap A = \mathfrak{p}$ by Corollary P1.2.7. A valuation ring that dominates $A_\mathfrak{p}$ meets $A$ in $\mathfrak{p}$. So it suffices to prove the second claim for a local subring $(A, \mathfrak{m})$.

Let $\Sigma$ be the set of local subrings of $K$ that dominate $A$, ordered by domination. Domination is transitive, so this is a partial order. The union of a chain in $\Sigma$ is a subring $B$, and the union $\mathfrak{n}$ of the maximal ideals of the members is an ideal of $B$ whose complement consists of units. So $B$ is local with maximal ideal $\mathfrak{n}$, and $B$ dominates every member of the chain. By Zorn's lemma $\Sigma$ has a maximal element $(V, \mathfrak{n})$.

Let $x \in K^*$. The first claim is that $\mathfrak{n}V[x] \neq V[x]$ or $\mathfrak{n}V[x^{-1}] \neq V[x^{-1}]$. Suppose both are false. Then
$$
1 = u_0 + u_1 x + \dots + u_m x^m , \qquad 1 = w_0 + w_1 x^{-1} + \dots + w_r x^{-r}
$$
with all $u_i, w_j \in \mathfrak{n}$, and choose $m$ and $r$ least possible. By symmetry suppose $m \geq r$. Multiply the second equation by $x^r$: $(1 - w_0) x^r = w_1 x^{r-1} + \dots + w_r$. Here $1 - w_0$ is a unit of $V$, so $x^r$ is a combination of $1, x, \dots, x^{r-1}$ with coefficients in $\mathfrak{n}$. Multiply by $x^{m-r}$ and substitute the result for $x^m$ in the first equation. This gives an equation of the same form with $m$ replaced by $m - 1$, a contradiction.

So suppose $\mathfrak{n}V[x] \neq V[x]$. Then $\mathfrak{n}V[x]$ lies in a maximal ideal $\mathfrak{q}$ of $V[x]$, and $\mathfrak{q} \cap V$ is a proper ideal that contains $\mathfrak{n}$, so $\mathfrak{q} \cap V = \mathfrak{n}$. The local ring $V[x]_\mathfrak{q}$ dominates $V$, hence dominates $A$, and by the maximality of $V$ it equals $V$. So $x \in V$. In the other case $x^{-1} \in V$ in the same way. So $V$ is a valuation ring. $\square$

**Corollary P1.7.6 (integral closure).** Let $A \subseteq K$ be a subring. The integral closure of $A$ in $K$ is the intersection of all valuation rings of $K$ that contain $A$.

Lean: Mathlib `iInf_valuationSubring_superset` and `Subring.eq_iInf_of_isIntegrallyClosedIn` (proved in Mathlib).

*Proof.* Let $V \supseteq A$ be a valuation ring of $K$. An element of $K$ integral over $A$ is integral over $V$, so it lies in $V$ by part (3) of the first proposition. Conversely let $x \in K$ be not integral over $A$. Then $x \neq 0$. Put $y = x^{-1}$ and $A' = A[y]$. If $y$ were a unit of $A'$, then $x = a_0 + a_1 y + \dots + a_n y^n$ with $a_i \in A$, and multiplication by $x^n$ gives a monic equation for $x$ over $A$, which is false. So $y$ lies in a maximal ideal $\mathfrak{m}'$ of $A'$. By the theorem there is a valuation ring $V$ of $K$ with $A' \subseteq V$ and $\mathfrak{m}_V \cap A' = \mathfrak{m}'$. Then $y \in \mathfrak{m}_V$, so $x = y^{-1} \notin V$, while $A \subseteq V$. $\square$

In particular a domain is normal if and only if it is an intersection of valuation rings of its fraction field.

### Proof in words

A valuation ring is a ring in which every element of the fraction field is either a function without a pole or the inverse of one. This single condition forces the ideals into a chain, and it makes the ring normal, since a pole cannot be cancelled by a monic equation. A valuation ring is the same as a valuation, a way to assign to every nonzero element an order in a totally ordered group, with the order of a sum at least the smaller of the two orders.

The existence theorem is a Zorn's lemma argument. A local ring that is maximal for domination cannot be enlarged by adjoining $x$ or $x^{-1}$, and the computation with the two equations shows that one of the two can always be adjoined. So the maximal ring contains $x$ or $x^{-1}$ for every $x$. The corollary turns the existence theorem into a test for integrality: an element is integral over $A$ exactly when it has no pole at any valuation that is nonnegative on $A$.

In geometry a valuation ring of the function field $k(X)$ that contains $k$ is a point of the abstract Zariski-Riemann space of $X$. It is a limit of points on all blow-ups of $X$ at once. The existence theorem says that every point of $X$ is the center of some valuation, and the centers of a valuation on the blow-ups of $X$ form a compatible system of points. The valuations that the minimal model program uses most are the divisorial ones of Section 7.2, which have value group $\mathbb{Z}$, but valuations of higher rank and with value groups such as $\mathbb{Z} + \mathbb{Z}\sqrt{2}$ appear in the study of log canonical thresholds and of the valuative tree.

### Examples

**Example P1.7.7 (the order at a point).** Let $k$ be a field and $K = k(x)$. Every $f \in K^*$ is $x^n g/h$ with $n \in \mathbb{Z}$ and $g, h \in k[x]$ not divisible by $x$, and $v(f) = n$ is a discrete valuation, the order of zero or pole at $0$. Its valuation ring is $k[x]_{(x)}$. In the same way, $v_p(p^n a/b) = n$ for $a, b$ prime to $p$ is a discrete valuation of $\mathbb{Q}$ with valuation ring $\mathbb{Z}_{(p)}$. The degree gives one more discrete valuation of $k(x)$, $v_\infty(g/h) = \deg h - \deg g$, with valuation ring $k[x^{-1}]_{(x^{-1})}$, the order at the point at infinity of $\mathbb{P}^1$.

**Example P1.7.8 (a valuation of rank two).** Let $V = \{f \in k(x)[y]_{(y)} : f(0) \in k[x]_{(x)}\}$ be the ring of Example P1.5.26. Every $f \in k(x, y)^*$ is $f = y^a g$ with $a \in \mathbb{Z}$ and $g$ a unit of $k(x)[y]_{(y)}$, so $g(0) \in k(x)^*$. Put
$$
v(f) = \big(a, \operatorname{ord}_x g(0)\big) \in \mathbb{Z} \times \mathbb{Z} ,
$$
with the lexicographic order: $(a, b) < (a', b')$ if $a < a'$, or $a = a'$ and $b < b'$. This is a valuation, and $v(f) \geq (0, 0)$ if and only if $a > 0$, or $a = 0$ and $g(0) \in k[x]_{(x)}$. So $V$ is its valuation ring. The primes of $V$ are $0 \subsetneq P = yk(x)[y]_{(y)} \subsetneq \mathfrak{m}$, so $\dim V = 2$, and the value of $y$ is larger than every multiple of the value of $x$. The value group $\mathbb{Z}^2$ with this order is not a subgroup of $\mathbb{R}$.

**Example P1.7.9 (monomial valuations).** Let $K = k(x, y)$ and let $a, b > 0$ be real numbers. For a nonzero polynomial $f = \sum c_{ij} x^i y^j$ put $v(f) = \min\{a i + b j : c_{ij} \neq 0\}$. The part of $f$ where the minimum is reached is its initial form, and the initial form of $fg$ is the product of the initial forms, which is nonzero since $k[x, y]$ is a domain. So $v(fg) = v(f) + v(g)$, and clearly $v(f + g) \geq \min(v(f), v(g))$. Then $v(f/g) = v(f) - v(g)$ is a valuation of $K$ with value group $a\mathbb{Z} + b\mathbb{Z}$. For $a = b = 1$, $v(f)$ is the order of $f$ at the origin, the largest $n$ with $f \in (x, y)^n$. For $a = 1$ and $b = \sqrt{2}$, the value group $\mathbb{Z} + \mathbb{Z}\sqrt{2}$ is dense in $\mathbb{R}$, the valuation ring has dimension $1$, and it is not Noetherian (Exercise 4).

**Example P1.7.10 (the valuation rings of $\mathbb{Q}$).** The only valuation rings of $\mathbb{Q}$ are $\mathbb{Q}$ and the $\mathbb{Z}_{(p)}$. A valuation ring $V \neq \mathbb{Q}$ contains $\mathbb{Z}$, and $\mathfrak{m}_V \cap \mathbb{Z}$ is a nonzero prime $(p)$, since otherwise every nonzero integer, and so every nonzero rational number, is a unit of $V$. Then $\mathbb{Z}_{(p)} \subseteq V$ as in part (4) of the first proposition, and if $V$ contained an element $p^n u$ with $n < 0$ and $u$ a unit of $\mathbb{Z}_{(p)}$, it would contain $1/p$, which is false as $p \in \mathfrak{m}_V$. So $V = \mathbb{Z}_{(p)}$. The corollary on integral closure then gives again $\mathbb{Z} = \bigcap_p \mathbb{Z}_{(p)}$, the integral closure of $\mathbb{Z}$ in $\mathbb{Q}$ (Example P1.4.7).

### Exercises

1. (A) Show that a valuation ring of $K$ with value group $\{0\}$ is $K$. Show that the valuation $v_\infty$ of $k(x)$ in the first example satisfies $v_\infty(f + g) \geq \min(v_\infty(f), v_\infty(g))$.
2. (A) Let $V$ be a valuation ring of $K$ with valuation $v$. Show that for $x, y \in K^*$ with $v(x) \neq v(y)$, $v(x + y) = \min(v(x), v(y))$.
3. (A) Show that a domain $A$ is a valuation ring if and only if its ideals are totally ordered by inclusion, if and only if for all $a, b \in A$, $a \mid b$ or $b \mid a$.
4. (B) For the monomial valuation of $k(x, y)$ with $a = 1$ and $b = \sqrt{2}$, show that the maximal ideal of the valuation ring is not finitely generated, so that the ring is not Noetherian. Show that its residue field is $k$.
5. (B) Show that the valuation $v$ of the rank two example is a valuation, and that the ideal $\bigcap_{n \geq 1} x^n V$ equals the prime $P$.
6. (B) Let $A = k[x, y]_{(x, y)} \subseteq k(x, y)$. Find a valuation ring that dominates $A$ and contains $y/x$, and one that dominates $A$ and does not contain $y/x$.
7. (B) Let $\Gamma$ be a totally ordered abelian group and $k$ a field. Show that the group ring $k[\Gamma]$, with basis $t^\gamma$ for $\gamma \in \Gamma$, is a domain, and that $v(\sum c_\gamma t^\gamma) = \min\{\gamma : c_\gamma \neq 0\}$ extends to a valuation of its fraction field with value group $\Gamma$. So every totally ordered abelian group is a value group.
8. (C) Let $A = k[t^2, t^3] \subseteq K = k(t)$. Use the corollary on integral closure to show that $t$ lies in every valuation ring of $K$ that contains $A$, and describe these valuation rings when $k$ is algebraically closed.

### Lean

Mathlib has both forms of the definition. `ValuationRing` is a class on a domain, defined by divisibility, and `ValuationSubring K` is the type of valuation rings of a field $K$. Valuations are `Valuation K Γ₀`, written multiplicatively, with values in a linearly ordered group with zero, so a value $\gamma$ here corresponds to an element $e^{-\gamma}$ there. The value group of a valuation ring is `ValuationRing.ValueGroup`. The facts that valuation rings are local and Bézout are `ValuationRing.isLocalRing` and `ValuationRing.iff_local_bezout_domain`. The existence theorem is `LocalSubring.exists_le_valuationSubring`, proved by the same maximality argument, and the description of the integral closure is `iInf_valuationSubring_superset`. The handbook adds no `MinimalModel` node here.

### Notes and history

Valuations of number fields go back to Kürschák and Ostrowski, and Krull introduced general valuations with values in ordered groups in 1932. Zariski used valuation rings in his work on resolution of singularities of surfaces and threefolds, and the space of all valuation rings of a function field is called the Zariski-Riemann space after him. The existence theorem in the form given here is due to Chevalley. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 5, and Matsumura, Chapter 4.
