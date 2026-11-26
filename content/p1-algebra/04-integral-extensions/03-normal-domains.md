---
title: Normal domains and going down
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
## Normal domains and going down

### Statement

**Definition P1.4.18 (normal domain).** A domain $A$ with fraction field $K$ is *integrally closed*, or *normal*, if every element of $K$ that is integral over $A$ lies in $A$. The integral closure $\bar{A}$ of $A$ in $K$ is the *normalization* of $A$; it is a normal domain by the transitivity of Section 4.1. A variety is normal if its local rings are normal domains.

Lean: Mathlib `IsIntegrallyClosed` (definition).

**Proposition P1.4.19 (factorial rings are normal).** A unique factorization domain is normal.

Lean: Mathlib `UniqueFactorizationMonoid.instIsIntegrallyClosed` (proved in Mathlib).

*Proof.* Let $x = a/b \in K$ with $a, b \in A$ without common prime factor, and suppose $x^n + c_1 x^{n-1} + \dots + c_n = 0$ with $c_i \in A$. Multiply by $b^n$: $a^n = -b(c_1 a^{n-1} + c_2 a^{n-2} b + \dots + c_n b^{n-1})$. A prime factor of $b$ would divide $a^n$, hence $a$. So $b$ is a unit and $x \in A$. $\square$

**Proposition P1.4.20 (normality is local).** For a domain $A$ the following are equivalent: (a) $A$ is normal; (b) $S^{-1}A$ is normal for every multiplicative set $S \not\ni 0$; (c) $A_{\mathfrak{p}}$ is normal for every prime $\mathfrak{p}$; (d) $A_{\mathfrak{m}}$ is normal for every maximal ideal $\mathfrak{m}$.

Lean: Mathlib `isIntegrallyClosed_of_isLocalization` and `IsIntegrallyClosed.of_localization_maximal` (proved in Mathlib).

*Proof.* (a) implies (b): by Section 4.1, the integral closure of $S^{-1}A$ in $K$ is $S^{-1}\bar{A} = S^{-1}A$. (b) implies (c) implies (d) is clear. (d) implies (a): consider the $A$-module $\bar{A}/A$. By Section 4.1, $(\bar{A}/A)_{\mathfrak{m}} = \overline{A_{\mathfrak{m}}}/A_{\mathfrak{m}} = 0$ for every maximal $\mathfrak{m}$. A module whose localizations at all maximal ideals vanish is zero (Section 2.1). So $\bar{A} = A$. $\square$

**Proposition P1.4.21 (rings of invariants).** Let $B$ be a normal domain and $G$ a finite group acting on $B$ by ring automorphisms. Then $A = B^G$ is a normal domain, and $B$ is integral over $A$.

Lean: not in Lean in this form.

*Proof.* For $b \in B$, $b$ is a root of the monic polynomial $\prod_{g \in G}(X - gb)$, whose coefficients are $G$-invariant. So $B$ is integral over $A$. Let $x \in \operatorname{Frac}(A)$ be integral over $A$. Then $x \in \operatorname{Frac}(B)$ is integral over $B$, so $x \in B$. Write $x = a/a'$ with $a, a' \in A$; then $gx = x$ for all $g$, since $g$ fixes $a$ and $a'$. So $x \in B^G = A$. $\square$

**Theorem P1.4.22 (going down).** Let $A \subseteq B$ be domains with $A$ normal and $B$ integral over $A$. Let $\mathfrak{p}_1 \supseteq \mathfrak{p}_2$ be primes of $A$ and $\mathfrak{q}_1$ a prime of $B$ over $\mathfrak{p}_1$. Then there is a prime $\mathfrak{q}_2 \subseteq \mathfrak{q}_1$ of $B$ over $\mathfrak{p}_2$.

Lean: Mathlib `Algebra.HasGoingDown`, with an instance for integral extensions of an integrally closed domain, and `Ideal.exists_ideal_le_liesOver_of_le` to apply it (proved in Mathlib).

*Proof sketch.* The full argument is in Atiyah-Macdonald, Chapter 5. There are three steps.

1. An element $x$ of an extension of $A$ is *integral over an ideal* $I$ if it satisfies $x^n + a_1 x^{n-1} + \dots + a_n = 0$ with all $a_i \in I$. If $A$ is normal and $x$ is algebraic over $K$ and integral over $I$, then the coefficients of the minimal polynomial of $x$ over $K$ lie in $\sqrt{I}$. The reason: the conjugates of $x$ in a normal closure satisfy the same equation, the coefficients of the minimal polynomial are polynomials in the conjugates, so they are integral over $I$ and lie in $K$, and normality puts them in $A$, and then in $\sqrt{I}$.
2. It suffices to show that $\mathfrak{p}_2 B_{\mathfrak{q}_1} \cap A = \mathfrak{p}_2$. Then $\mathfrak{p}_2 B_{\mathfrak{q}_1}$ does not meet $S = A \setminus \mathfrak{p}_2$, so its extension to $S^{-1}B_{\mathfrak{q}_1}$ is a proper ideal and lies in a maximal ideal $\mathfrak{n}$. The contraction of $\mathfrak{n}$ to $A$ contains $\mathfrak{p}_2$ and does not meet $S$, so it is $\mathfrak{p}_2$. The contraction $\mathfrak{q}_2$ of $\mathfrak{n}$ to $B$ lies in $\mathfrak{q}_1$ and over $\mathfrak{p}_2$.
3. Let $x \in \mathfrak{p}_2 B_{\mathfrak{q}_1} \cap A$, $x \neq 0$. Write $x = y/s$ with $y \in \mathfrak{p}_2 B$ and $s \in B \setminus \mathfrak{q}_1$. The element $y$ is integral over $\mathfrak{p}_2$, so by step 1 its minimal polynomial is $y^r + u_1 y^{r-1} + \dots + u_r$ with $u_i \in \mathfrak{p}_2$. Dividing by $x^r$, the minimal polynomial of $s = y/x$ is $s^r + v_1 s^{r-1} + \dots + v_r$ with $v_i = u_i/x^i$. Since $s$ is integral over $A$, step 1 with $I = A$ gives $v_i \in A$. If $x \notin \mathfrak{p}_2$, then $x^i v_i = u_i \in \mathfrak{p}_2$ forces $v_i \in \mathfrak{p}_2$, so $s^r \in \mathfrak{p}_2 B \subseteq \mathfrak{q}_1$ and $s \in \mathfrak{q}_1$, a contradiction. So $x \in \mathfrak{p}_2$. $\square$

### Proof in words

A normal domain is one that contains every element of its fraction field that satisfies a monic equation. Factorial rings are normal by the rational root test. Normality is a local property, so it makes sense for varieties. Rings of invariants of normal domains under finite groups are normal, which gives many normal singularities.

Going down is the converse of going up: a chain of primes can be lifted downwards. It needs a normal base, and the proof uses minimal polynomials, whose coefficients a normal ring controls. Geometrically, let $X \to Y$ be a finite surjective morphism of irreducible varieties with $Y$ normal. Going down says that if $W \subseteq Z$ are irreducible closed subsets of $Y$ and $W'$ is an irreducible component of the preimage of $W$, then some irreducible closed $Z' \supseteq W'$ maps onto $Z$. This is the algebra behind the fact that such a morphism is open. Going down also holds for flat extensions (Section 1.4), and this is the algebra behind the openness of flat morphisms. In Volume 4, the finite cover of a normal singularity and the normalization of a pair use exactly these properties.

### Examples

**Example P1.4.23 (the node).** Let $A = k[x, y]/(y^2 - x^2(x + 1))$, the coordinate ring of the nodal cubic, with $\operatorname{char} k \neq 2$. Put $t = y/x \in \operatorname{Frac}(A)$. Then $t^2 = x + 1$, so $t$ is integral over $A$, and $x = t^2 - 1$, $y = tx = t^3 - t$. So $A \subseteq k[t]$, both have the fraction field $k(t)$, and $k[t]$ is integral over $A$ and normal. Hence $\bar{A} = k[t]$. The normalization $\mathbb{A}^1 \to C$, $t \mapsto (t^2 - 1, t^3 - t)$, sends $t = 1$ and $t = -1$ to the node: it separates the two branches. The element $t$ is not in $A$, so $A$ is not normal.

**Example P1.4.24 (the cusp).** For $A = k[t^2, t^3]$ the element $t = t^3/t^2$ lies in $\operatorname{Frac}(A)$ and is integral, so $\bar{A} = k[t]$. The normalization of the cuspidal cubic is a bijection, but not an isomorphism.

**Example P1.4.25 (the quadric cone).** Let $\operatorname{char} k \neq 2$, and let $G = \{\pm 1\}$ act on $B = k[u, v]$ by $(u, v) \mapsto (-u, -v)$. The invariants are spanned by the monomials of even degree, so $B^G = k[u^2, uv, v^2] \cong k[x, y, z]/(xy - z^2)$. By the proposition on invariants, the cone $xy = z^2$ is normal. It is not factorial: $xy = z^2$ gives two factorizations of the same element into irreducibles, as Chapter 8 explains with the class group. The cone is the quotient singularity $\mathbb{A}^2/\{\pm 1\}$, the simplest singularity of the surface MMP, and Volume 2 and Volume 4 meet it often.

**Example P1.4.26 (going down fails without normality).** Let $B = k[x, y]$ and
$$
A = \{f \in k[x, y] : f(0, y) = f(1, y)\} = k[x^2 - x, \, x^3 - x^2, \, y] .
$$
The element $x$ satisfies $X^2 - X - (x^2 - x) = 0$ with $x^2 - x \in A$, so $B = A + Ax$ is integral over $A$. Also $x = (x^3 - x^2)/(x^2 - x) \in \operatorname{Frac}(A)$, so $A$ is not normal; $\operatorname{Spec} A$ is the plane with the lines $x = 0$ and $x = 1$ glued along $(0, y) \sim (1, y)$. Let $\mathfrak{q}_1 = (x - 1, y)$, the point $(1, 0)$, and $\mathfrak{p}_1 = \mathfrak{q}_1 \cap A$, the image of $(1, 0)$, which is also the image of $(0, 0)$. Let $C = V(y - x)$, the diagonal, and $\mathfrak{p}_2 = (y - x) \cap A$, the prime of its image. The image of $C$ passes through the image of $(0, 0)$, so $\mathfrak{p}_2 \subseteq \mathfrak{p}_1$. The map $\operatorname{Spec} B \to \operatorname{Spec} A$ is a bijection outside the two lines, so $C$ is the only curve over the image of $C$, and the only prime of $B$ over $\mathfrak{p}_2$ is $(y - x)$. But $(1, 0) \notin C$, so $(y - x) \not\subseteq \mathfrak{q}_1$. Going down fails.

### Exercises

1. (A) Show that $\mathbb{Z}[\sqrt{-3}]$ is not normal, and that its normalization is $\mathbb{Z}[(1 + \sqrt{-3})/2]$.
2. (A) Find the normalization of $k[x, y]/(y^2 - x^5)$ and of $k[x, y]/(y^3 - x^4)$, and describe the normalization maps.
3. (B) Show that $k[x, y, z]/(z^2 - xy)$ is not a unique factorization domain by showing that $x$, $y$ and $z$ are irreducible and pairwise not associated. (Use the grading.)
4. (B) In the last example, show that $A = k[x^2 - x, x^3 - x^2, y]$, that $\operatorname{Frac}(A) = k(x, y)$, and that $B$ is the normalization of $A$.
5. (C) Let $A$ be a normal domain with fraction field $K$, let $L/K$ be a finite extension, and let $B$ be the integral closure of $A$ in $L$. Show that the minimal polynomial over $K$ of every $b \in B$ has coefficients in $A$. Deduce that the trace $\operatorname{Tr}_{L/K}(b)$ and the norm $N_{L/K}(b)$ lie in $A$.

### Lean

Mathlib defines `IsIntegrallyClosed` for a domain with respect to its fraction field. Factorial rings are integrally closed by `UniqueFactorizationMonoid.instIsIntegrallyClosed`. Localization preserves normality by `isIntegrallyClosed_of_isLocalization`, and the local criterion is `IsIntegrallyClosed.of_localization_maximal`. Going down is the class `Algebra.HasGoingDown`; Mathlib provides it for integral extensions of an integrally closed domain, and `Algebra.HasGoingDown.of_flat` for flat algebras. The handbook adds no `MinimalModel` node here.

### Notes and history

Dedekind used integral closure to define the rings of integers of number fields, and the normalization of curves goes back to the nineteenth century theory of Riemann surfaces. Zariski introduced normal varieties in 1939 and proved that the normalization of an affine variety is finite. Cohen and Seidenberg proved the going down theorem in 1946. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 5.
