---
title: Normal Noetherian domains and Krull's theorem
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch9, Mat86:ch4, Eis95:ch11]
requires: [P1.1, P1.2, P1.3, P1.4, P1.5, P1.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Normal Noetherian domains and Krull's theorem

### Statement

Throughout, $A$ is a Noetherian domain with fraction field $K$. For a prime $\mathfrak{p}$ of height $1$ such that $A_\mathfrak{p}$ is a DVR, $v_\mathfrak{p}: K^* \to \mathbb{Z}$ is the valuation of $A_\mathfrak{p}$, the order of vanishing along $\mathfrak{p}$ of Section 7.2. By Corollary P1.7.13 this valuation exists for every prime of height $1$ when $A$ is normal.

**Lemma P1.8.1 (associated primes of a principal ideal).** Let $A$ be a Noetherian normal domain and $b \in A$ a nonzero nonunit. Every associated prime of $A/bA$ has height $1$.

Lean: not in Mathlib in this form.

*Proof.* Let $\mathfrak{p} \in \operatorname{Ass}(A/bA)$. Then $\mathfrak{p} = (bA : c)$ for some $c \in A$, the annihilator of the class of $c$ in $A/bA$. First localize at $\mathfrak{p}$. Clearly $\mathfrak{p}A_\mathfrak{p} \subseteq (bA_\mathfrak{p} : c)$. Conversely, if $c \cdot y/s \in bA_\mathfrak{p}$ with $y \in A$ and $s \notin \mathfrak{p}$, then $u c y \in bA$ for some $u \notin \mathfrak{p}$, so $uy \in \mathfrak{p}$ and $y \in \mathfrak{p}$. Hence $\mathfrak{p}A_\mathfrak{p} = (bA_\mathfrak{p} : c)$, and $c \notin bA_\mathfrak{p}$, since $\mathfrak{p}A_\mathfrak{p}$ is a proper ideal. The ring $A_\mathfrak{p}$ is a Noetherian normal domain (Proposition P1.4.20), and $\operatorname{ht} \mathfrak{p} = \operatorname{ht} \mathfrak{p}A_\mathfrak{p}$ (Corollary P1.2.7). So it is enough to treat the case where $A$ is local with maximal ideal $\mathfrak{m} = \mathfrak{p} = (bA : c)$ and $c \notin bA$.

Put $y = c/b \in K$. Then $y \notin A$, since $c \notin bA$, and $y\mathfrak{m} \subseteq A$, since $c\mathfrak{m} \subseteq bA$. So $y\mathfrak{m}$ is an ideal of $A$. If $y\mathfrak{m} \subseteq \mathfrak{m}$, then $\mathfrak{m}$ is a faithful $A[y]$-module that is finitely generated over $A$, so $y$ is integral over $A$ by Proposition P1.4.2, and $y \in A$ by normality, a contradiction. So $y\mathfrak{m} = A$. Choose $t \in \mathfrak{m}$ with $yt = 1$. For $a \in \mathfrak{m}$, $a = t \cdot ya$ with $ya \in A$, so $\mathfrak{m} = tA$. The ideal $\mathfrak{m}$ is minimal over $tA$, so $\operatorname{ht} \mathfrak{m} \leq 1$ by the principal ideal theorem (Theorem P1.5.17), and $\mathfrak{m} \neq 0$ since $b \in \mathfrak{m}$. So $\operatorname{ht} \mathfrak{m} = 1$. $\square$

**Theorem P1.8.2 (Krull).** Let $A$ be a Noetherian normal domain. Then:

1. for every prime $\mathfrak{p}$ of height $1$, $A_\mathfrak{p}$ is a DVR;
2. every nonzero $f \in A$ lies in only finitely many primes of height $1$;
3. $A = \bigcap_{\operatorname{ht} \mathfrak{p} = 1} A_\mathfrak{p}$, the intersection taken in $K$.

Lean: not in Mathlib as one statement. Part (1) for Dedekind domains is `IsLocalization.AtPrime.isDiscreteValuationRing_of_dedekind_domain` (proved in Mathlib).

*Proof.* (1) is Corollary P1.7.13.

(2) Let $f \neq 0$, and let $\mathfrak{p}$ be a prime of height $1$ with $f \in \mathfrak{p}$. The prime $\mathfrak{p}$ contains a prime $\mathfrak{q}$ minimal over $fA$, and $\mathfrak{q} \neq 0$ since $f \neq 0$. As $\operatorname{ht} \mathfrak{p} = 1$, $\mathfrak{q} = \mathfrak{p}$. So $\mathfrak{p}$ is a minimal prime of $fA$, and $fA$ has only finitely many minimal primes (Theorem P1.3.20).

(3) Every $A_\mathfrak{p}$ contains $A$. Conversely, let $x \in K$ lie in every $A_\mathfrak{p}$ with $\operatorname{ht} \mathfrak{p} = 1$, and write $x = a/b$ with $a, b \in A$ and $b \neq 0$. If $b$ is a unit, then $x \in A$. Otherwise choose a primary decomposition $bA = \mathfrak{q}_1 \cap \dots \cap \mathfrak{q}_r$ (Theorem P1.2.40), and let $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$. The $\mathfrak{p}_i$ are associated primes of $A/bA$ (Theorem P1.2.47), so they have height $1$ by the lemma. Fix $i$. Since $x \in A_{\mathfrak{p}_i}$, the element $a = xb$ lies in $bA_{\mathfrak{p}_i} \subseteq \mathfrak{q}_i A_{\mathfrak{p}_i}$. Now $\mathfrak{q}_i A_{\mathfrak{p}_i} \cap A = \mathfrak{q}_i$: if $z \in A$ and $sz \in \mathfrak{q}_i$ with $s \notin \mathfrak{p}_i$, then $z \in \mathfrak{q}_i$, since $\mathfrak{q}_i$ is primary and no power of $s$ lies in $\mathfrak{q}_i$. So $a \in \mathfrak{q}_i$ for all $i$, hence $a \in bA$ and $x \in A$. $\square$

**Corollary P1.8.3 (algebraic Hartogs theorem).** Let $A$ be a Noetherian normal domain and $x \in K^*$. Then $x \in A$ if and only if $v_\mathfrak{p}(x) \geq 0$ for every prime $\mathfrak{p}$ of height $1$. The element $x$ is a unit of $A$ if and only if $v_\mathfrak{p}(x) = 0$ for every such $\mathfrak{p}$.

Lean: not in Mathlib in this form.

*Proof.* The valuation ring of $v_\mathfrak{p}$ is $A_\mathfrak{p}$, so the first claim is part (3) of the theorem. Apply it to $x$ and $x^{-1}$ for the second. $\square$

For $x \in K^*$, write $x = a/b$ with $a, b \in A$. By part (2) of the theorem, $v_\mathfrak{p}(a)$ and $v_\mathfrak{p}(b)$ are zero for all but finitely many $\mathfrak{p}$, so $v_\mathfrak{p}(x) \neq 0$ for only finitely many primes of height $1$. This finiteness and part (3) are the two properties that make a theory of divisors work, and they give a name to a class of rings.

**Definition P1.8.4 (Krull domain).** A domain $A$ with fraction field $K$ is a *Krull domain* if there is a family $(v_i)_{i \in I}$ of discrete valuations of $K$ such that $A = \bigcap_i \{x \in K : v_i(x) \geq 0\}$, and such that every $x \in K^*$ has $v_i(x) \neq 0$ for only finitely many $i$.

Lean: not in Mathlib.

By the theorem and the remark after the corollary, a Noetherian normal domain is a Krull domain, with the family $(v_\mathfrak{p})_{\operatorname{ht} \mathfrak{p} = 1}$. A Krull domain is normal, since a valuation ring is normal and an intersection of normal subrings of $K$ with fraction field $K$ is normal (Exercise 6). A unique factorization domain is a Krull domain, with the valuations $v_\pi$ given by the exponent of a prime element $\pi$ (Exercise 1). So the polynomial ring $k[x_1, x_2, \dots]$ in infinitely many variables is a Krull domain that is not Noetherian. Matsumura, Chapter 4, develops divisors for all Krull domains. This handbook needs only the Noetherian case.

The valuations also describe the symbolic powers of Section 5.2 and the principal ideals.

**Proposition P1.8.5 (symbolic powers and principal ideals).** Let $A$ be a Noetherian normal domain.

1. For a prime $\mathfrak{p}$ of height $1$ and $n \geq 1$, $\mathfrak{p}^{(n)} = \{a \in A : v_\mathfrak{p}(a) \geq n\}$.
2. For a nonzero $f \in A$,
$$
fA = \bigcap_{\operatorname{ht} \mathfrak{p} = 1,\ v_\mathfrak{p}(f) > 0} \mathfrak{p}^{(v_\mathfrak{p}(f))} ,
$$
a finite intersection, equal to $A$ when it is empty, which is a primary decomposition of $fA$. In particular a principal ideal has no embedded primes.

Lean: not in Mathlib.

*Proof.* (1) By Definition P1.5.14, $\mathfrak{p}^{(n)} = \mathfrak{p}^n A_\mathfrak{p} \cap A$, and in the DVR $A_\mathfrak{p}$ the ideal $\mathfrak{p}^nA_\mathfrak{p}$ is $\{y : v_\mathfrak{p}(y) \geq n\}$. (2) For $a \in A$, $a \in fA$ if and only if $a/f \in A$, if and only if $v_\mathfrak{p}(a) \geq v_\mathfrak{p}(f)$ for all $\mathfrak{p}$ of height $1$, by the corollary. For the $\mathfrak{p}$ with $v_\mathfrak{p}(f) = 0$ this holds for every $a \in A$. For the others it says $a \in \mathfrak{p}^{(v_\mathfrak{p}(f))}$ by (1). The intersection is finite by part (2) of the theorem, and each $\mathfrak{p}^{(n)}$ is $\mathfrak{p}$-primary (Section 5.2), with distinct radicals of height $1$. So none of them is embedded. $\square$

### Proof in words

The lemma is the same trick that proved that a normal local domain of dimension one is a DVR in Section 7.2. If an associated prime $\mathfrak{p}$ of $A/bA$ is the annihilator of $c$, the fraction $c/b$ multiplies $\mathfrak{p}$ into $A$ but is not in $A$. Normality prevents it from multiplying $\mathfrak{p}$ into $\mathfrak{p}$, so $\mathfrak{p}$ becomes principal after localization, and a principal prime has height one. Then Krull's theorem follows from primary decomposition: a principal ideal $bA$ is the intersection of its primary components, these sit at primes of height one, and each component is detected in the local ring at its prime.

Geometrically, let $X$ be a normal affine variety with coordinate ring $A$. A function $f$ vanishes along finitely many prime divisors, and a rational function that has no pole along any prime divisor is regular. This is the algebraic form of Hartogs' theorem in complex analysis: a holomorphic function on the complement of a subset of codimension two extends. Without normality the statement fails, and the failure is measured by the associated primes of height at least two. The proposition says that on a normal variety the ideal of a function $f$ is cut out by the orders of vanishing of $f$ along prime divisors and nothing more: it has no embedded components.

### Examples

**Example P1.8.6 (the plane minus a point).** Let $A = k[x, y]$. A prime of height one is $(\pi)$ for an irreducible polynomial $\pi$, by Proposition P1.5.23, and it cannot contain both $x$ and $y$, since $(x, y)$ is maximal of height $2$. If $x \notin (\pi)$, then $A_x \subseteq A_{(\pi)}$, and if $y \notin (\pi)$, then $A_y \subseteq A_{(\pi)}$. So $A_x \cap A_y \subseteq \bigcap A_{(\pi)} = A$ by Krull's theorem, and
$$
k[x, y]_x \cap k[x, y]_y = k[x, y] .
$$
The two open sets $D(x)$ and $D(y)$ cover $\mathbb{A}^2 \setminus \{0\}$, so every regular function on the punctured plane extends to the plane. The same argument works for the complement of any closed subset of codimension at least two in a normal affine variety (Exercise 3).

**Example P1.8.7 (the lemma fails without normality).** Let $B = k[s, t]$ and let $A = k[s^4, s^3t, st^3, t^4] \subseteq B$, the coordinate ring of the cone over the rational quartic curve $[s^4 : s^3t : st^3 : t^4]$ in $\mathbb{P}^3$. It is a domain of dimension $2$, since $B$ is integral over it. A monomial $s^a t^b$ with $a + b = 4d$ lies in $A$ for every $d \geq 2$, and for $d = 1$ exactly when $(a, b) \neq (2, 2)$: for $d = 2$ check the nine monomials one by one, and for $d \geq 3$ divide by $s^4$ or by $t^4$ and use induction. Let $\mathfrak{m} = (s^4, s^3t, st^3, t^4)$ and $c = s^6t^2 = (s^3t)^2$. Then $c \notin s^4 A$, since $c/s^4 = s^2t^2 \notin A$. But
$$
s^3t \cdot c = s^4 \cdot s^5t^3, \quad st^3 \cdot c = s^4 \cdot s^3 t^5, \quad t^4 \cdot c = s^4 \cdot s^2 t^6 ,
$$
and $s^5t^3$, $s^3t^5$ and $s^2t^6$ lie in $A$ because their degree is $8$. So $(s^4A : c) = \mathfrak{m}$, and the maximal ideal $\mathfrak{m}$, of height $2$, is an associated prime of $A/s^4A$. The ring $A$ is not normal: $s^2 t^2 = c/s^4$ lies in $K$ and $(s^2t^2)^2 = s^4 \cdot t^4$, so it is integral over $A$. Also $\mathfrak{m} \cdot s^2t^2 \subseteq A$, so $s^2 t^2 \in A_\mathfrak{p}$ for every prime $\mathfrak{p} \neq \mathfrak{m}$. In particular $s^2t^2$ lies in $A_\mathfrak{p}$ for every prime of height one but not in $A$, and part (3) of Krull's theorem fails for $A$. Exercise 5 shows that the integral closure of $A$ is $A + k \cdot s^2t^2$.

**Example P1.8.8 (a principal ideal on the quadric cone).** Let $A = k[x, y, z]/(xy - z^2)$, which is normal by Example P1.4.25 when $\operatorname{char} k \neq 2$, and by Section 8.2 in general. The primes of height one that contain $x$ contain $z^2 = xy$, so they contain $\mathfrak{p} = (x, z)$, and $\mathfrak{p}$ is the only one (Example P1.5.24). In $A_\mathfrak{p}$ the element $y$ is a unit, since $y \notin \mathfrak{p}$, so $x = z^2/y$ and $\mathfrak{p}A_\mathfrak{p} = (x, z) = (z)$. So $v_\mathfrak{p}(z) = 1$ and $v_\mathfrak{p}(x) = 2$, and the proposition gives $xA = \mathfrak{p}^{(2)}$. The ordinary power $\mathfrak{p}^2 = (x^2, xz, z^2) = (x^2, xz, xy) = x(x, y, z)$ is smaller: it has the embedded prime $(x, y, z)$ (Exercise 4). The line $V(\mathfrak{p})$ through the vertex is a prime divisor, and the function $x$ vanishes to order $2$ along it.

### Exercises

1. (A) Let $A$ be a unique factorization domain, and for a prime element $\pi$ let $v_\pi(x)$ be the exponent of $\pi$ in $x \in K^*$. Show that $A = \bigcap_\pi \{v_\pi \geq 0\}$ and that $A$ is a Krull domain. Show that $k[x_1, x_2, \dots]$ is a Krull domain that is not Noetherian.
2. (A) Let $A = k[x, y]$ and $f = x^2 y$. Find the primes of height one that contain $f$, the values $v_\mathfrak{p}(f)$, and the decomposition of $fA$ given by the proposition. Check it against a direct computation.
3. (B) Let $A$ be a Noetherian normal domain and $I = (g_1, \dots, g_r)$ an ideal with $\operatorname{ht} I \geq 2$. Show that $A_{g_1} \cap \dots \cap A_{g_r} = A$ in $K$. Interpret this as an extension statement for regular functions on $\operatorname{Spec} A \setminus V(I)$.
4. (B) Let $A = k[x, y, z]/(xy - z^2)$, $\mathfrak{p} = (x, z)$ and $\mathfrak{m} = (x, y, z)$. Show that $\mathfrak{p}^2 = x\mathfrak{m}$, that $(\mathfrak{p}^2 : x) = \mathfrak{m}$, and that $\mathfrak{p}^2 = \mathfrak{p}^{(2)} \cap \mathfrak{m}^2$ is a primary decomposition with embedded prime $\mathfrak{m}$. (Hint: $\mathfrak{m}^2 \supseteq x\mathfrak{m}$, and an element of $(x) \cap \mathfrak{m}^2$ is $xg$ with $g \in \mathfrak{m}$ by the grading.)
5. (B) In the example $A = k[s^4, s^3t, st^3, t^4]$, let $\bar{A}$ be the subring of $k[s, t]$ spanned by the monomials of degree divisible by $4$. Show that $\bar{A} = A + k \cdot s^2t^2$, that $\bar{A}$ is the integral closure of $A$, and that $A_\mathfrak{p} = \bar{A}_\mathfrak{p}$ is a DVR for every prime $\mathfrak{p}$ of height one of $A$. (Hint: for normality of $\bar{A}$, use the grading of $k[s, t]$ by $\mathbb{Z}/4$ and the argument of the Lemma on graded pieces in Section 8.2.)
6. (A) Let $(A_i)_{i \in I}$ be normal subrings of a field $K$, each with fraction field $K$, and suppose that $A = \bigcap_i A_i$ has fraction field $K$. Show that $A$ is normal. Deduce that every Krull domain is normal.
7. (B) Let $A$ be a Noetherian normal domain, $\mathfrak{p}$ a prime of height one and $r, s \geq 1$. Show that $\mathfrak{p}^{(r)}\mathfrak{p}^{(s)} \subseteq \mathfrak{p}^{(r + s)}$, and that equality can fail, using $\mathfrak{p}^{(1)}\mathfrak{p}^{(1)} = \mathfrak{p}^2 \neq \mathfrak{p}^{(2)}$ on the quadric cone.
8. (C) Let $A$ be a Noetherian domain such that $A_\mathfrak{p}$ is a DVR for every prime $\mathfrak{p}$ of height one, and such that $A/bA$ has only associated primes of height one for every nonzero nonunit $b$. Show that $A$ is normal. (Hint: repeat the proof of part (3) of the theorem, then use Exercise 6. Serre's criterion in Chapter 11 states this condition as $R_1$ and $S_2$.)

### Lean

Mathlib has normal domains as `IsIntegrallyClosed`, discrete valuation rings as `IsDiscreteValuationRing`, and associated primes as `associatedPrimes`, as in Section 2.4. It does not yet prove that the localization of a Noetherian normal domain at a prime of height one is a DVR outside the Dedekind case, nor Krull's intersection theorem $A = \bigcap A_\mathfrak{p}$, nor the notion of a Krull domain. Symbolic powers are not defined in `Mathlib/RingTheory`. The handbook adds no `MinimalModel` node here.

### Notes and history

Krull introduced the rings now called Krull domains in the early 1930s, under the name endliche diskrete Hauptordnungen, and proved that Noetherian normal domains belong to this class. The lemma on associated primes and the intersection theorem are in Matsumura, Chapter 4, in the section on Krull rings, and in Eisenbud, Chapter 11. Atiyah-Macdonald, Chapter 9, treats the dimension one case, and its exercises outline the general case. The literature state of every result here is theorem. The section follows Matsumura, Chapter 4, and Eisenbud, Chapter 11.
