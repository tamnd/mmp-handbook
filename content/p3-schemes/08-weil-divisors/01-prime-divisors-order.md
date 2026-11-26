---
title: Prime divisors and the order of vanishing
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch14, Har77:II.6, GW20:ch11]
requires: [P1.5, P1.7, P1.8, P3.2, P3.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Prime divisors and the order of vanishing

### Statement

Throughout this chapter $X$ is an integral Noetherian scheme with function field $K = K(X)$ and generic point $\xi$. By Example P3.5.5, $K$ is the stalk $\mathcal{O}_{X, \xi}$, and every $\mathcal{O}_X(U)$ with $U \neq \emptyset$ and every local ring $\mathcal{O}_{X, x}$ is a subring of $K$ (Proposition P3.2.24).

**Definition P3.8.1 (prime divisor).** A *prime divisor* of $X$ is an irreducible closed subset $D \subseteq X$ of codimension $1$, with its reduced structure as an integral closed subscheme. Its generic point is $\eta_D$, and its *local ring* is $\mathcal{O}_{X, D} = \mathcal{O}_{X, \eta_D}$. By part 4 of Proposition P3.7.2 this is a Noetherian local domain of dimension $1$, and its fraction field is $K$.

Lean: Mathlib works with points instead of closed sets: a prime divisor corresponds to its generic point $z$, a point with `Order.coheight z = 1` (definition).

**Proposition P3.8.2 (the order of vanishing).** Let $D$ be a prime divisor of $X$, and write $\mathcal{O} = \mathcal{O}_{X, D}$.

1. For $f \in K^*$ write $f = a/b$ with $a, b \in \mathcal{O} \setminus \{0\}$ and put $\operatorname{ord}_D(f) = \ell_\mathcal{O}(\mathcal{O}/a\mathcal{O}) - \ell_\mathcal{O}(\mathcal{O}/b\mathcal{O})$. This is a well defined homomorphism $\operatorname{ord}_D \colon K^* \to \mathbb{Z}$. It is $\geq 0$ on $\mathcal{O} \setminus \{0\}$, and it vanishes exactly on the units of $\mathcal{O}$ among the elements of $\mathcal{O} \setminus \{0\}$.
2. If $\mathcal{O}$ is a discrete valuation ring, for instance if $X$ is normal, then $\operatorname{ord}_D$ is its normalized valuation. Then $\operatorname{ord}_D(f + g) \geq \min(\operatorname{ord}_D(f), \operatorname{ord}_D(g))$ when $f + g \neq 0$, and $\operatorname{ord}_D(f) \geq 0$ if and only if $f \in \mathcal{O}$.
3. Let $U = \operatorname{Spec} A$ be an affine open with $U \cap D \neq \emptyset$. Then $D \cap U = V(\mathfrak{p})$ for a prime $\mathfrak{p}$ of height $1$, and $\mathcal{O} = A_\mathfrak{p}$. The map $D \mapsto \mathfrak{p}$ is a bijection from the prime divisors of $X$ that meet $U$ to the primes of height $1$ of $A$. If $A$ is normal, $\operatorname{ord}_D = v_\mathfrak{p}$, the valuation of Definition P1.8.9.
4. Let $U \subseteq X$ be open with $U \cap D \neq \emptyset$ and $f \in \mathcal{O}_X(U)$ nonzero. Then $\operatorname{ord}_D(f) \geq 0$, and $\operatorname{ord}_D(f) > 0$ if and only if $D \cap U \subseteq V(f)$.

The integer $\operatorname{ord}_D(f)$ is the *order of vanishing* of $f$ along $D$. If it is negative, $f$ has a *pole* of order $-\operatorname{ord}_D(f)$ along $D$.

Lean: Mathlib `AlgebraicGeometry.Scheme.ord` and `AlgebraicGeometry.Scheme.ordHom` define the order of vanishing on a locally Noetherian integral scheme through the length function `Ring.ordFrac` of the stalk, with `AlgebraicGeometry.Scheme.ord_mul` for part 1 and `AlgebraicGeometry.Scheme.ord_add` for the inequality of part 2 when the stalk is a discrete valuation ring (definitions and proved in Mathlib).

**Lemma P3.8.3 (finiteness).** Let $f \in K^*$. Then $\operatorname{ord}_D(f) = 0$ for all but finitely many prime divisors $D$. More precisely, if $U \subseteq X$ is a nonempty open set, then the prime divisors of $X$ that do not meet $U$ are the irreducible components of $X \setminus U$ of codimension $1$ in $X$, so there are finitely many.

Lean: not in Lean as stated.

**Proposition P3.8.4 (functions without poles).** Let $X$ be normal, $U \subseteq X$ a nonempty open set and $f \in K^*$.

1. $f \in \mathcal{O}_X(U)$ if and only if $\operatorname{ord}_D(f) \geq 0$ for every prime divisor $D$ that meets $U$.
2. $f \in \mathcal{O}_X(U)^*$ if and only if $\operatorname{ord}_D(f) = 0$ for every prime divisor $D$ that meets $U$.
3. If $f \in \mathcal{O}_X(U)$, then $V(f) \subseteq U$ is the union of the sets $D \cap U$ over the prime divisors $D$ with $\operatorname{ord}_D(f) > 0$. In particular $V(f)$ is empty or of pure codimension $1$ in $U$.

Lean: not in Lean as stated.

### Proof in words

A prime divisor is a point of codimension one, its generic point, and the local ring there is one-dimensional. On a one-dimensional local domain the length of $\mathcal{O}/a\mathcal{O}$ counts how many times $a$ vanishes, and it is additive, so it extends to fractions. On a normal scheme the local ring is a discrete valuation ring and the order is a valuation. A rational function is a unit on a dense open set, so it can only vanish or have poles along the finitely many divisors in the complement. Finally, a normal Noetherian domain is the intersection of its localizations at height one primes, so a function without poles is regular: this is Krull's theorem read geometrically.

### Examples

**Example P3.8.5 (the projective line).** Let $X = \mathbb{P}^1_k$ with function field $k(t)$, where $t = x_1/x_0$. The prime divisors are the closed points. On $\mathbb{A}^1_k = \operatorname{Spec} k[t]$ a closed point is $P_\pi = V(\pi)$ for a monic irreducible polynomial $\pi$, and for $f = c \prod_\pi \pi^{n_\pi}$ with $c \in k^*$, $\operatorname{ord}_{P_\pi}(f) = n_\pi$. At the point $\infty = V_+(x_0)$ the local ring is $k[s]_{(s)}$ with $s = 1/t$, and for $f = g/h$ with $g, h \in k[t]$ one gets $\operatorname{ord}_\infty(f) = \deg h - \deg g$. Since $\deg \pi = [\kappa(P_\pi) : k]$, this gives
$$
\sum_{P} [\kappa(P) : k] \operatorname{ord}_P(f) = \sum_\pi n_\pi \deg \pi + \deg h - \deg g = 0 .
$$
A rational function on $\mathbb{P}^1_k$ has as many zeros as poles, counted with multiplicity and degree. Section 8.3 proves the same statement on $\mathbb{P}^n_k$.

**Example P3.8.6 (the integers).** Let $X = \operatorname{Spec} \mathbb{Z}$. The prime divisors are the closed points $(p)$, and $\operatorname{ord}_{(p)}$ is the $p$-adic valuation on $\mathbb{Q}^*$. Lemma P3.8.3 says that a nonzero rational number has finitely many primes in its numerator and denominator. Proposition P3.8.4 says that a rational number with no prime in its denominator is an integer, and that the units of $\mathbb{Z}$ are the rational numbers with no prime at all, $\pm 1$.

**Example P3.8.7 (a function on the plane).** Let $X = \mathbb{A}^2_k$ and $f = x^2/y$. The ring $k[x, y]$ is factorial, so its height one primes are the principal primes $(\pi)$ with $\pi$ irreducible, and $\operatorname{ord}_{V(\pi)}(f)$ is the exponent of $\pi$ in $f$. So $\operatorname{ord}_{V(x)}(f) = 2$, $\operatorname{ord}_{V(y)}(f) = -1$, and $\operatorname{ord}_D(f) = 0$ for the other prime divisors. The origin lies on both $V(x)$ and $V(y)$, and $f$ is neither regular nor a pole there in any sense, but the origin is not a prime divisor, and the orders along divisors do not see it.

**Example P3.8.8 (the quadric cone).** Let $X = \operatorname{Spec} A$ with $A = k[x, y, z]/(xy - z^2)$, a normal surface (Example P3.7.37), and let $L = V(x, z)$ and $M = V(y, z)$ be the two lines through the vertex. Example P1.8.14 with $n = 2$ gives $\operatorname{ord}_L(z) = 1$ and $\operatorname{ord}_L(x) = 2$, and $\operatorname{ord}_L(y) = 0$, since $y$ is a unit in $A_{(x, z)}$. By symmetry $\operatorname{ord}_M(z) = 1$, $\operatorname{ord}_M(y) = 2$ and $\operatorname{ord}_M(x) = 0$. Part 3 of Proposition P3.8.4 then shows that $V(x) = L$, $V(y) = M$ and $V(z) = L \cup M$, and that no other prime divisor carries a zero of $x$, $y$ or $z$.

**Example P3.8.9 (the node: orders without normality).** Let $\operatorname{char} k \neq 2$ and $X = \operatorname{Spec} A$, $A = k[x, y]/(y^2 - x^2(x + 1))$, with normalization $\mathbb{A}^1_k \to X$ given by $x = t^2 - 1$ and $y = t(t^2 - 1)$ (Example P3.7.38). The origin $P$ is a prime divisor, and $\mathcal{O}_{X, P}$ is not a discrete valuation ring. By part 1 of Proposition P3.8.2, $\operatorname{ord}_P(x) = \ell(A_P/xA_P) = \dim_k k[y]/(y^2) = 2$ and $\operatorname{ord}_P(y) = \dim_k k[x]/(x^2) = 2$, since $x + 1$ is a unit at $P$. So $\operatorname{ord}_P(t) = \operatorname{ord}_P(y/x) = 0$. The function $t$ is regular away from $P$, and $\operatorname{ord}_Q(t) \geq 0$ at every prime divisor $Q$, but $t \notin A$, as $t$ takes the two values $1$ and $-1$ on the two branches through $P$. So Proposition P3.8.4 fails without normality.

### Proof

*Proof of Proposition P3.8.2.* (1) This is Proposition P1.7.14 applied to the one-dimensional Noetherian local domain $\mathcal{O}$, whose fraction field is $K$: every $f \in K^*$ is a quotient $a/b$ with $a, b \in \mathcal{O}$, as $\mathcal{O}$ contains the coordinate ring of an affine open, and the length of $\mathcal{O}/a\mathcal{O}$ is zero exactly when $a$ is a unit.

(2) If $X$ is normal, $\mathcal{O}$ is a Noetherian normal local domain of dimension $1$, hence a discrete valuation ring (Theorem P1.7.12). For a discrete valuation ring with uniformizer $\pi$ and $a = u\pi^n$, $u$ a unit, the length of $\mathcal{O}/a\mathcal{O} = \mathcal{O}/\pi^n\mathcal{O}$ is $n$, by the chain $\pi^i\mathcal{O}/\pi^n\mathcal{O}$, $0 \leq i \leq n$, with simple quotients. So $\operatorname{ord}_D = v$, part 4 of Proposition P1.7.14. The two last statements are properties of a valuation and of its valuation ring (Proposition P1.7.4).

(3) The set $D \cap U$ is a nonempty open subset of the irreducible set $D$, so it is irreducible and closed in $U$, with generic point $\eta_D$, a prime $\mathfrak{p}$ of $A$. By part 2 of Proposition P3.7.2, $\operatorname{codim}(D \cap U, U) = 1$, and by part 1 this is $\operatorname{ht} \mathfrak{p}$. The stalk at $\mathfrak{p}$ is $A_\mathfrak{p}$. Conversely, for a prime $\mathfrak{p}$ of height $1$ the closure of the point $\mathfrak{p}$ in $X$ is an irreducible closed set with generic point $\mathfrak{p}$ and codimension $1$, by the same two parts. Generic points are unique (Theorem P3.2.20), so these maps are inverse to each other. If $A$ is normal, $A_\mathfrak{p}$ is a discrete valuation ring with valuation $v_\mathfrak{p}$, and part 2 applies.

(4) The germ of $f$ at $\eta_D$ lies in $\mathcal{O}$, so $\operatorname{ord}_D(f) \geq 0$, with equality if and only if $f$ is a unit in $\mathcal{O}$, that is, $f(\eta_D) \neq 0$. As $V(f)$ is closed in $U$ and $D \cap U$ is the closure of $\eta_D$ in $U$, $f(\eta_D) = 0$ holds if and only if $D \cap U \subseteq V(f)$. $\square$

*Proof of Lemma P3.8.3.* Let $D$ be a prime divisor with $D \cap U = \emptyset$. Then $D \subseteq X \setminus U$, a closed set that is not all of $X$. As $X$ is Noetherian, $X \setminus U$ has finitely many irreducible components, and $D$ lies in one of them, $W$. Since $W \neq X$ and $X$ is irreducible, $X \supsetneq W$ is a chain, so $\operatorname{codim}(W, X) \geq 1$. If $D \subsetneq W$, a chain $D \subsetneq W \subsetneq X$ shows $\operatorname{codim}(D, X) \geq 2$, which is false. So $D = W$ is a component of $X \setminus U$ of codimension $1$, and conversely such a component is a prime divisor that does not meet $U$, since it is not contained in another component.

For $f \in K^*$, choose a nonempty affine open $\operatorname{Spec} A$ and write $f = a/b$ with $a, b \in A \setminus \{0\}$. On $U = D(ab) \subseteq \operatorname{Spec} A$, nonempty since $A$ is a domain, $f$ is a unit of $\mathcal{O}_X(U)$. For every prime divisor $D$ meeting $U$, $f$ and $1/f$ lie in $\mathcal{O}_{X, D}$, so $\operatorname{ord}_D(f) = 0$ by part 1 of Proposition P3.8.2. The other prime divisors are finitely many by the first paragraph. $\square$

*Proof of Proposition P3.8.4.* (1) If $f \in \mathcal{O}_X(U)$, part 4 of Proposition P3.8.2 gives $\operatorname{ord}_D(f) \geq 0$. Conversely, let $\operatorname{ord}_D(f) \geq 0$ for every $D$ meeting $U$, and let $V = \operatorname{Spec} A \subseteq U$ be a nonempty affine open. Then $A$ is a Noetherian normal domain with fraction field $K$ (part 1 of Proposition P3.7.32). For every prime $\mathfrak{p}$ of $A$ of height $1$, part 3 of Proposition P3.8.2 gives a prime divisor $D$ meeting $V$ with $v_\mathfrak{p}(f) = \operatorname{ord}_D(f) \geq 0$, so $f \in A_\mathfrak{p}$. By Krull's theorem (Theorem P1.8.2, part 3), $f \in A$. So $f$ is a section over every affine open of $U$. All these sections are the element $f$ of $K$, so they agree on overlaps, and they glue to an element of $\mathcal{O}_X(U)$, as in the proof of Theorem P3.7.33.

(2) $f$ is a unit in $\mathcal{O}_X(U)$ if and only if $f$ and $1/f$ lie in $\mathcal{O}_X(U)$. By part 1 this holds if and only if $\operatorname{ord}_D(f) \geq 0$ and $-\operatorname{ord}_D(f) \geq 0$ for every $D$ meeting $U$.

(3) If $\operatorname{ord}_D(f) > 0$, then $D \cap U \subseteq V(f)$ by part 4 of Proposition P3.8.2. Conversely, let $x \in V(f)$ and let $V = \operatorname{Spec} A \subseteq U$ be an affine open containing $x$, a prime $\mathfrak{q}$ of $A$ that contains $f$. Then $\mathfrak{q}$ contains a minimal prime $\mathfrak{p}$ over $fA$, and $\operatorname{ht} \mathfrak{p} = 1$ by Krull's principal ideal theorem (Theorem P1.5.17), as $f$ is not zero, and is not a unit since $f \in \mathfrak{q}$. Let $D$ be the prime divisor with $D \cap V = V(\mathfrak{p})$. Then $x \in D$ and $f \in \mathfrak{p}A_\mathfrak{p}$, so $\operatorname{ord}_D(f) > 0$. As $X$ is Noetherian, $V(f)$ is a closed subset of $U$ whose irreducible components are among the $D \cap U$, so it is empty or of pure codimension $1$. $\square$

### Exercises

1. (A) On $\mathbb{A}^2_k$, find all prime divisors $D$ with $\operatorname{ord}_D(f) \neq 0$ for $f = x^2 (x - y)^3 / (y (x^2 + y^2 - 1))$, with $\operatorname{char} k \neq 2$, and give the orders.
2. (A) On $\mathbb{P}^1_\mathbb{R}$, compute $\operatorname{ord}_P(f)$ at every closed point $P$ for $f = (t^2 + 1)/t^3$, including the point at infinity, and check the formula of Example P3.8.5.
3. (A) On the cone $X = V(xy - z^3) \subseteq \mathbb{A}^3_k$, compute the orders of $x$, $y$ and $z$ along the lines $L = V(x, z)$ and $M = V(y, z)$, and show that these are the only prime divisors along which $x$, $y$ or $z$ vanishes.
4. (B) Let $U \subseteq X$ be a nonempty open set. Show that $D \mapsto D \cap U$ is a bijection from the prime divisors of $X$ that meet $U$ to the prime divisors of $U$, and that $\operatorname{ord}_{D \cap U}(f) = \operatorname{ord}_D(f)$ for $f \in K^*$.
5. (B) Let $R$ be a discrete valuation ring with uniformizer $\pi$ and valuation $v$, and $X = \operatorname{Spec} R[x]$. Show that $V(\pi)$ is a prime divisor and that $\operatorname{ord}_{V(\pi)}(g) = \min_i v(a_i)$ for $g = \sum_i a_i x^i \in R[x]$ nonzero. Deduce Gauss's lemma, $\operatorname{ord}_{V(\pi)}(gh) = \operatorname{ord}_{V(\pi)}(g) + \operatorname{ord}_{V(\pi)}(h)$, as a statement about the content of polynomials.
6. (B) On the node of Example P3.8.9, find $f, g \in K^*$ with $\operatorname{ord}_P(f) = \operatorname{ord}_P(g) = 2$ and $\operatorname{ord}_P(f + g) = 0$. So $\operatorname{ord}_P$ is not a valuation.
7. (C) Let $A$ be a one-dimensional Noetherian local domain, $B \supseteq A$ a finite extension inside $\operatorname{Frac} A$, and $\mathfrak{n}_1, \dots, \mathfrak{n}_r$ the maximal ideals of $B$. Show that $\ell_A(A/aA) = \ell_A(B/aB)$ for $a \in A$ nonzero, and deduce that $\operatorname{ord}_P(f) = \sum_i [\kappa(\mathfrak{n}_i) : \kappa(P)] \, v_{\mathfrak{n}_i}(f)$ when $B$ is the normalization. Check the formula on the node, where it gives $2 = 1 + 1$ for $x$.

### Lean

Mathlib defines the order of vanishing in `Mathlib/AlgebraicGeometry/OrderOfVanishing.lean`. For a locally Noetherian integral scheme and a point $z$ of coheight one, `AlgebraicGeometry.Scheme.ordHom` is the monoid homomorphism from the function field given by `Ring.ordFrac` of the stalk, the length construction of part 1 of Proposition P3.8.2, and `AlgebraicGeometry.Scheme.ord` is its integer version, with the junk value $0$ at other points. The lemmas `ord_mul`, `ord_of_isUnit` and `ord_add` cover parts 1, 4 and 2. The finiteness lemma and the characterization of regular functions by their orders are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

The order of a function along a hypersurface goes back to the theory of algebraic functions of one variable, where it is the order of a zero or a pole at a point. Hartshorne, Section II.6, works under the standing hypothesis that $X$ is Noetherian, integral, separated and regular in codimension one, and Lemma P3.8.3 is his Lemma II.6.1. The length definition of the order on a non-normal scheme is the one used in intersection theory, as in Fulton's book on intersection theory. The literature state is theorem. In the minimal model program the order of vanishing along a prime divisor, possibly a divisor on a blow-up of $X$, is the basic measurement: the discrepancy of a divisor over $X$ is the order of vanishing of the relative canonical divisor along it, and log canonical thresholds are ratios of such orders.
