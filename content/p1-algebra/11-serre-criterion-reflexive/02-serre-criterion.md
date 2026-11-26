---
title: Serre's criterion for normality
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [Mat86:ch8, Eis95:ch11]
requires: [P1.1, P1.2, P1.4, P1.7, P1.8, P1.9, P1.10]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Serre's criterion for normality

### Statement

Throughout, $A$ is a Noetherian ring, and Serre's conditions $R_k$ and $S_k$ are as in Section 11.1.

**Theorem P1.11.11 (Serre's criterion for reducedness).** $A$ is reduced if and only if it satisfies $R_0$ and $S_1$.

Lean: not in Mathlib. Mathlib has `IsReduced` as a definition.

*Proof.* Suppose $A$ is reduced, and let $\mathfrak{p} = \operatorname{Ann}(a)$ be an associated prime, with $a \neq 0$. The nilradical is $0$, and it is the intersection of the minimal primes, so there is a minimal prime $\mathfrak{q}$ with $a \notin \mathfrak{q}$. Since $\mathfrak{p}a = 0 \in \mathfrak{q}$, $\mathfrak{p} \subseteq \mathfrak{q}$, so $\mathfrak{p} = \mathfrak{q}$ is minimal. By the lemma on associated primes and localization in Section 11.1, $\operatorname{depth} A_\mathfrak{p} \geq 1$ for every prime $\mathfrak{p}$ of positive height, which is $S_1$. For a minimal prime $\mathfrak{p}$, the ring $A_\mathfrak{p}$ is reduced and of dimension $0$, so its maximal ideal is its nilradical, which is $0$, and $A_\mathfrak{p}$ is a field. This is $R_0$.

Conversely, assume $R_0$ and $S_1$, and let $a \in A$ be nilpotent. For each minimal prime $\mathfrak{p}$, the image of $a$ in the field $A_\mathfrak{p}$ is nilpotent, hence $0$, so $sa = 0$ for some $s \notin \mathfrak{p}$, and $\operatorname{Ann}(a) \not\subseteq \mathfrak{p}$. By $S_1$ the associated primes of $A$ are minimal primes, so $\operatorname{Ann}(a)$ is contained in no associated prime. By prime avoidance (Proposition P1.1.11) and Proposition P1.2.44, $\operatorname{Ann}(a)$ contains a nonzerodivisor $c$. Then $ca = 0$ gives $a = 0$. $\square$

**Theorem P1.11.12 (Serre's criterion for normality).** Let $A$ be a Noetherian domain. Then $A$ is normal if and only if it satisfies $R_1$ and $S_2$.

Lean: not in Mathlib. Mathlib has `IsIntegrallyClosed` and `IsDiscreteValuationRing` as definitions.

*Proof.* Let $A$ be normal. For a prime $\mathfrak{p}$ of height $1$, $A_\mathfrak{p}$ is a DVR by Krull's theorem (Theorem P1.8.2), hence a regular local ring of dimension $1$ by Theorem P1.7.12, and $A_{(0)} = K$ is a field. This is $R_1$. For $S_2$, a domain has depth at least $1$ at every prime of positive height, so let $\operatorname{ht} \mathfrak{p} \geq 2$. The ring $A_\mathfrak{p}$ is a Noetherian normal domain by Proposition P1.4.20. Take $x \in \mathfrak{p}A_\mathfrak{p}$ nonzero. By Lemma P1.8.1, every associated prime of $A_\mathfrak{p}/xA_\mathfrak{p}$ has height $1$, so the maximal ideal $\mathfrak{p}A_\mathfrak{p}$, of height at least $2$, is not associated. So $\operatorname{depth} A_\mathfrak{p}/xA_\mathfrak{p} \geq 1$ and $\operatorname{depth} A_\mathfrak{p} \geq 2$.

Conversely, assume $R_1$ and $S_2$. For every prime $\mathfrak{p}$ of height $1$, $A_\mathfrak{p}$ is a regular local ring of dimension $1$, hence a DVR by Theorem P1.7.12. A DVR is a valuation ring and so is normal (Chapter 7). By the algebraic Hartogs property of Section 11.1, $A = \bigcap_{\operatorname{ht} \mathfrak{p} = 1} A_\mathfrak{p}$. If $f \in K$ is integral over $A$, then it is integral over each $A_\mathfrak{p}$, so $f \in A_\mathfrak{p}$ for every such $\mathfrak{p}$, and $f \in A$. $\square$

The same statement holds for a Noetherian ring that is not a domain, if *normal* means that every localization $A_\mathfrak{p}$ is a normal domain (Matsumura, Chapter 8, and Eisenbud, Chapter 11). This is the form of the criterion used for schemes.

**Corollary P1.11.13 (normal rings in small dimension).** Let $A$ be a Noetherian normal domain.

1. For every prime $\mathfrak{p}$ with $\operatorname{ht} \mathfrak{p} \leq 2$, the local ring $A_\mathfrak{p}$ is Cohen-Macaulay. In particular a Noetherian normal domain of dimension at most $2$ is Cohen-Macaulay, and so is the coordinate ring of a normal affine surface.
2. For every prime $\mathfrak{p}$ with $\operatorname{ht} \mathfrak{p} \geq 2$, $\operatorname{depth} A_\mathfrak{p} \geq 2$.

Lean: not in Mathlib.

*Proof.* Both parts are the condition $S_2$ of the theorem: for $\operatorname{ht} \mathfrak{p} \leq 2$ it says $\operatorname{depth} A_\mathfrak{p} \geq \operatorname{ht} \mathfrak{p} = \dim A_\mathfrak{p}$. $\square$

**Corollary P1.11.14 (normality of complete intersections).** Let $A$ be a Noetherian domain that is Cohen-Macaulay, for example a complete intersection or a hypersurface. Then $A$ is normal if and only if it satisfies $R_1$. If $k$ is perfect and $A = k[x_1, \dots, x_n]/(f)$ is a hypersurface domain whose singular closed points form a closed set $V(J_A)$ of codimension at least $2$, as in Corollary P1.9.13, then $A$ is normal.

Lean: not in Mathlib.

*Proof.* A Cohen-Macaulay ring satisfies every $S_k$ by Section 11.1, so the theorem gives the first statement. For the second, let $\mathfrak{p}$ be a prime of height $1$. Since $V(J_A)$ has codimension at least $2$, $J_A \not\subseteq \mathfrak{p}$, and $V(\mathfrak{p}) \setminus V(\mathfrak{p} + J_A)$ is a nonempty open subset of the irreducible closed set $V(\mathfrak{p})$. By Theorem P1.4.30 it contains a maximal ideal $\mathfrak{m}$, and $A_\mathfrak{m}$ is regular by Corollary P1.9.13. Then $A_\mathfrak{p}$ is a localization of $A_\mathfrak{m}$, so it is regular by Corollary P1.9.22. So $A$ satisfies $R_1$, and it is a hypersurface, so it is normal by the first statement. $\square$

Conversely, a normal hypersurface has singular locus of codimension at least $2$, by $R_1$ and the openness of the regular locus, which follows from the full Jacobian criterion (Eisenbud, Chapter 16).

### Proof in words

A ring is reduced when its generic points are reduced and nothing is hidden at embedded points, and these are $R_0$ and $S_1$. A domain is normal when it is a discrete valuation ring at each prime divisor and every function regular in codimension one is regular, and these are $R_1$ and, by the Hartogs property of Section 11.1, $S_2$. In the other direction, Krull's theorem gives $R_1$, and the fact that principal ideals of a normal domain have only height one associated primes gives $S_2$. For a Cohen-Macaulay ring the condition $S_2$ is automatic, so only the codimension of the singular locus matters.

### Examples

**Example P1.11.15 (the cones $xy = z^n$).** Let $A = k[x, y, z]/(xy - z^n)$ with $n \geq 1$ and $k$ perfect. The gradient $(y, x, -nz^{n-1})$ vanishes on the surface only where $x = y = 0$, and then $z^n = xy = 0$, so the only singular point is the origin, of codimension $2$. So $A$ is normal by the corollary on complete intersections, in every characteristic. This is the normality used in Example P1.8.14.

**Example P1.11.16 (the Whitney umbrella).** Let $A = k[x, y, z]/(x^2 - y^2z)$ with $\operatorname{char} k \neq 2$. It is a hypersurface, so it satisfies $S_2$, and by Example P1.9.15 it is singular along the $z$-axis, a closed subset of codimension $1$. So $A$ fails $R_1$, and it is not normal. The element $x/y$ is integral over $A$, and it does not lie in $A_\mathfrak{p}$ for the prime $\mathfrak{p} = (x, y)$ of height one, since $x \notin yA_\mathfrak{p}$.

**Example P1.11.17 (a surface that fails only $S_2$).** Let $A = k[s^4, s^3t, st^3, t^4]$. By Exercise 6 of Section 11.1, the rings $A_{s^4}$ and $A_{t^4}$ are normal, and they are regular, since each is isomorphic to $k[u, u^{-1}, w]$, a localization of a polynomial ring in two variables. So $A$ satisfies $R_1$. It is not normal (Example P1.8.7), so by the theorem it fails $S_2$, and it does so at the vertex, where its depth is $1$ (Section 10.2). Its normalization $k[s, t]^{(4)}$ is normal and Cohen-Macaulay.

**Example P1.11.18 (reduced and not reduced).** The node $k[x, y]/(xy)$ is a hypersurface, so it satisfies $S_1$, and its localizations at the minimal primes $(x)$ and $(y)$ are fields, so it is reduced. The ring $k[x, y]/(x^2, xy)$ satisfies $R_0$ by the example of an embedded point in Section 11.1, but not $S_1$, and it is not reduced. The ring $k[x, y]/(x^2)$ satisfies $S_1$, as a hypersurface, but not $R_0$, since its localization at $(x)$ is $k(y)[x]/(x^2)$.

**Example P1.11.19 (normal but not Cohen-Macaulay).** In dimension $3$ the condition $S_2$ does not give the Cohen-Macaulay property. The standard example is the affine cone over an abelian surface in a projectively normal embedding: it is normal, and its depth at the vertex is $2$, because the first cohomology of the structure sheaf of an abelian surface is not zero. The proof uses sheaf cohomology and is not given here. In the minimal model program this cone is log canonical but not klt, and the klt singularities of Volume 4 are Cohen-Macaulay.

### Exercises

1. (A) Show that a Noetherian domain of dimension $1$ is normal if and only if it satisfies $R_1$, and deduce the characterization of Dedekind domains in Chapter 7.
2. (A) Decide which of the following are normal, for $k$ algebraically closed of characteristic $0$: $k[x, y, z]/(x^2 + y^3 + z^5)$, $k[x, y, z]/(x^2 - yz^2)$, $k[x, y, z, w]/(xw - yz)$, $k[x, y]/(y^2 - x^3)$.
3. (A) Show that $k[x, y, z]/(xy, z)$ satisfies $R_0$ and $S_1$, and find the minimal primes.
4. (B) Let $A$ be a Noetherian normal domain and $x \in A$ nonzero and not a unit. Show that $A/xA$ satisfies $S_1$. Show that $A/xA$ is reduced if and only if $v_\mathfrak{p}(x) \leq 1$ for every prime $\mathfrak{p}$ of height one.
5. (B) Let $f \in k[x_1, \dots, x_n]$ be irreducible with $n \geq 3$, $k$ perfect, and suppose that $f$ and all $\partial f/\partial x_i$ vanish together only at the origin. Show that $k[x_1, \dots, x_n]/(f)$ is normal. Apply this to the du Val equations $A_n$, $D_n$, $E_6$, $E_7$, $E_8$ of Volume 4 in characteristic $0$.
6. (B) Let $A$ be a Noetherian normal local domain of dimension $2$ and $x, y$ a system of parameters. Show that $x, y$ is a regular sequence, and that $(x) : y = (x)$.
7. (C) Let $A$ be an affine domain that satisfies $R_1$, with normalization $\bar{A}$. Show that $\bar{A} = \bigcap_{\operatorname{ht} \mathfrak{p} = 1} A_\mathfrak{p}$, and compute both sides for $A = k[s^4, s^3t, st^3, t^4]$. (Hint: for a prime $\mathfrak{Q}$ of height one of $\bar{A}$, the prime $\mathfrak{Q} \cap A$ has height one by Section 5.4, and a DVR $A_\mathfrak{p}$ contained in a local ring $\bar{A}_\mathfrak{Q} \neq K$ with $\mathfrak{Q}\bar{A}_\mathfrak{Q} \cap A_\mathfrak{p} = \mathfrak{p}A_\mathfrak{p}$ is equal to it, by Chapter 7.)
8. (C) Let $A = k[x, y, z, w]/((x, y) \cap (z, w))$, the two planes of Example P1.5.50. Show that $A$ is reduced and satisfies $R_1$ and $S_1$ but not $S_2$, and that $A$ is not normal in the sense of the remark after the theorem. (Hint: localize at the origin and look for an idempotent of the normalization.)

### Lean

Mathlib has `IsReduced`, `IsIntegrallyClosed` and `IsDiscreteValuationRing` as definitions, and Krull dimension and depth, but it has neither Serre's conditions nor Serre's criteria for reducedness and normality. The corollaries are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

Serre's criterion for normality is due to Serre, and it appears in Grothendieck's EGA IV in the form for schemes. Its first half contains Krull's theorem of Chapter 8 on normal domains. The literature state of every result here is theorem. The section follows Matsumura, Chapter 8, and Eisenbud, Chapter 11.
