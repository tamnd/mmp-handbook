---
title: Regular rings and factoriality
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [Mat86:ch7, Eis95:ch17, Eis95:ch19]
requires: [P1.1, P1.2, P1.3, P1.4, P1.5, P1.7, P1.8]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Regular rings and factoriality

### Statement

Throughout, $(A, \mathfrak{m}, k)$ is a Noetherian local ring of dimension $d$, and all modules are finitely generated unless stated otherwise. The section uses the functors $\operatorname{Tor}^A_i$, the derived functors of the tensor product, computed from a projective resolution of either variable, as in the appendix on homological algebra in Eisenbud. A finitely generated projective module over $A$ is flat (Proposition P1.1.45) and finitely presented, so it is free by Theorem P1.1.50.

**Definition P1.9.18 (projective and global dimension).** The *projective dimension* $\operatorname{pd}_A M$ of a module $M$ is the least $n$ such that $M$ has a projective resolution $0 \to P_n \to \dots \to P_0 \to M \to 0$, or $\infty$ if there is none. The *global dimension* $\operatorname{gl.dim} A$ is the supremum of $\operatorname{pd}_A M$ over all $A$-modules $M$.

Lean: Mathlib `CategoryTheory.projectiveDimension` (definition, in an abelian category), with `CategoryTheory.HasProjectiveDimensionLE`.

**Lemma P1.9.19 (minimal resolutions).** Let $M$ be finitely generated. Then $M$ has a resolution $\dots \to F_1 \to F_0 \to M \to 0$ by finitely generated free modules $F_i = A^{b_i}$ such that every differential has image in $\mathfrak{m}F_{i-1}$. For such a resolution $b_i = \dim_k \operatorname{Tor}^A_i(M, k)$, and
$$
\operatorname{pd}_A M = \sup\{ i : \operatorname{Tor}^A_i(M, k) \neq 0 \} .
$$
If this number $n$ is finite, then $F_i = 0$ for $i > n$.

Lean: not in Mathlib in this form.

*Proof.* Let $b_0$ be the least number of generators of $M$ and $F_0 = A^{b_0} \to M$ the map given by minimal generators. By Corollary P1.1.26, $F_0 \otimes k \to M \otimes k$ is an isomorphism, so the kernel $K_1$ lies in $\mathfrak{m}F_0$. The module $K_1$ is finitely generated since $A$ is Noetherian. Repeat with $K_1$ in place of $M$. In the complex $F \otimes_A k$ all differentials are zero, since their images lie in $\mathfrak{m}F_{i-1} \otimes k = 0$. So $\operatorname{Tor}^A_i(M, k) = F_i \otimes k \cong k^{b_i}$.

If $M$ has a projective resolution of length $n$, then $\operatorname{Tor}_i^A(M, k) = 0$ for $i > n$, computed from that resolution. Conversely, if $\operatorname{Tor}_{n+1}^A(M, k) = 0$, then $b_{n+1} = 0$, so $F_{n+1} = 0$, the map $F_n \to F_{n-1}$ is injective, and $0 \to F_n \to \dots \to F_0 \to M \to 0$ is a resolution of length $n$. $\square$

For $x_1, \dots, x_d \in A$ the *Koszul complex* $K(x_1, \dots, x_d)$ has $K_i = \Lambda^i A^d$, the free module with basis $e_{j_1} \wedge \dots \wedge e_{j_i}$ for $j_1 < \dots < j_i$, and the differential
$$
e_{j_1} \wedge \dots \wedge e_{j_i} \longmapsto \sum_{s=1}^{i} (-1)^{s+1} x_{j_s}\, e_{j_1} \wedge \dots \wedge \widehat{e_{j_s}} \wedge \dots \wedge e_{j_i} .
$$
For $d = 1$ it is $0 \to A \xrightarrow{x_1} A \to 0$, and for $d = 2$ it is $0 \to A \to A^2 \to A \to 0$ with the maps $1 \mapsto (-x_2, x_1)$ and $(a, b) \mapsto a x_1 + b x_2$. Its zeroth homology is $A/(x_1, \dots, x_d)$.

**Lemma P1.9.20 (the Koszul complex of a regular sequence).** Suppose that for each $j < d$ the image of $x_{j+1}$ is a nonzerodivisor in $A/(x_1, \dots, x_j)$. Then $K(x_1, \dots, x_d)$ is a free resolution of $A/(x_1, \dots, x_d)$ of length $d$.

Lean: not in Mathlib in this form. Mathlib `RingTheory.Sequence.IsRegular` (definition of a regular sequence) and `ModuleCat.projectiveDimension_quotient_eq_length`, which says that the projective dimension of $A/(x_1, \dots, x_d)$ for a regular sequence in the maximal ideal is $d$ (proved in Mathlib).

*Proof sketch.* Write $K^{(j)} = K(x_1, \dots, x_j)$. The complex $K^{(j+1)}$ is the mapping cone of multiplication by $x_{j+1}$ on $K^{(j)}$, so there is a long exact sequence
$$
\dots \to H_i(K^{(j)}) \xrightarrow{\pm x_{j+1}} H_i(K^{(j)}) \to H_i(K^{(j+1)}) \to H_{i-1}(K^{(j)}) \xrightarrow{\pm x_{j+1}} H_{i-1}(K^{(j)}) \to \dots
$$
(Eisenbud, Chapter 17). By induction $H_i(K^{(j)}) = 0$ for $i > 0$ and $H_0(K^{(j)}) = A/(x_1, \dots, x_j)$, on which $x_{j+1}$ is injective. The sequence gives $H_i(K^{(j+1)}) = 0$ for $i \geq 1$. $\square$

**Theorem P1.9.21 (Serre's characterization).** For a Noetherian local ring $(A, \mathfrak{m}, k)$ the following are equivalent:

1. $A$ is regular;
2. $\operatorname{gl.dim} A < \infty$;
3. $\operatorname{pd}_A k < \infty$.

In that case $\operatorname{gl.dim} A = \operatorname{pd}_A k = \dim A$, and every finitely generated module has a resolution of length at most $\dim A$ by finitely generated free modules.

Lean: not in Mathlib.

*Proof of (1) implies (2).* Let $x_1, \dots, x_d$ be a regular system of parameters. By the proposition on quotients by parameters in Section 9.1, it satisfies the hypothesis of the Koszul lemma, so $K(x_1, \dots, x_d)$ resolves $A/\mathfrak{m} = k$, and $\operatorname{pd}_A k \leq d$. For a finitely generated $M$, computing Tor from this resolution gives $\operatorname{Tor}^A_i(M, k) = H_i(M \otimes K(x)) = 0$ for $i > d$, so $\operatorname{pd}_A M \leq d$ by the lemma on minimal resolutions. In $K(x) \otimes k$ the differentials are zero, since the $x_j$ lie in $\mathfrak{m}$, so $\operatorname{Tor}^A_d(k, k) \cong \Lambda^d k^d = k \neq 0$ and $\operatorname{pd}_A k = d$. The global dimension of a Noetherian ring is the supremum of $\operatorname{pd}_A A/I$ over its ideals $I$, by a standard argument with Ext (Matsumura, Chapter 7), so $\operatorname{gl.dim} A = d$. The implication (2) to (3) is clear. $\square$

*Sketch of (3) implies (1).* Use induction on the embedding dimension. If $\mathfrak{m}$ is an associated prime of $A$, then $sA \cong k$ for some $s \neq 0$, and the last map $F_n \to F_{n-1}$ of a finite minimal resolution of $k$ is injective with image in $\mathfrak{m}F_{n-1}$, while $s$ kills $\mathfrak{m}F_{n-1}$ and not $F_n$. This forces $n = 0$, so $k$ is free and $\mathfrak{m} = 0$. Otherwise prime avoidance (Proposition P1.1.11) gives a nonzerodivisor $x \in \mathfrak{m} \setminus \mathfrak{m}^2$. A lemma of Nagata shows that $\mathfrak{m}/x\mathfrak{m}$ has $k$ as a direct summand over $A/xA$, which gives $\operatorname{pd}_{A/xA} k < \infty$, so $A/xA$ is regular by induction, and $A$ is regular by Exercise 4 of Section 9.1. The details are in Matsumura, Chapter 7, and Eisenbud, Chapter 19. $\square$

**Corollary P1.9.22 (localization).** If $A$ is a regular local ring and $\mathfrak{p}$ is a prime of $A$, then $A_\mathfrak{p}$ is a regular local ring.

Lean: not in Mathlib. The file `Mathlib/RingTheory/RegularLocalRing/Defs.lean` lists it as a TODO.

*Proof.* By Serre's theorem, $A/\mathfrak{p}$ has a finite resolution $0 \to F_n \to \dots \to F_0 \to A/\mathfrak{p} \to 0$ by free modules. Localization is exact (Theorem P1.2.5), so $0 \to (F_n)_\mathfrak{p} \to \dots \to (F_0)_\mathfrak{p} \to A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p} \to 0$ is a finite free resolution of the residue field of $A_\mathfrak{p}$. By Serre's theorem, (3) implies (1), $A_\mathfrak{p}$ is regular. $\square$

**Definition P1.9.23 (regular ring).** A Noetherian ring $A$ is *regular* if $A_\mathfrak{p}$ is a regular local ring for every prime $\mathfrak{p}$. By the corollary, it suffices that $A_\mathfrak{m}$ is regular for every maximal ideal $\mathfrak{m}$, and a regular local ring is a regular ring.

Lean: Mathlib `IsRegularRing` (definition: a Noetherian ring whose localizations at all primes are regular local rings) and `IsRegularLocalRing.of_isRegularRing_of_isLocalRing` (proved in Mathlib).

For example, $k[x_1, \dots, x_n]$ is regular by the example on affine space in Section 9.1, and a Dedekind domain is regular, since its localizations at nonzero primes are discrete valuation rings. If $A$ is regular, so is $A[x]$ (Exercise 7), hence $\mathbb{Z}[x_1, \dots, x_n]$ is regular.

**Lemma P1.9.24 (stably free modules of rank one).** Let $B$ be a Noetherian domain and $P$ a finitely generated projective $B$-module with a finite resolution $0 \to F_n \to \dots \to F_0 \to P \to 0$ by finitely generated free modules. Then $P \oplus F \cong G$ for finitely generated free modules $F$ and $G$. If $P_\mathfrak{q} \cong B_\mathfrak{q}$ for every prime $\mathfrak{q}$, then $P \cong B$.

Lean: not in Mathlib in this form.

*Proof.* Use induction on $n$. For $n = 0$, $P \cong F_0$. For $n \geq 1$ let $K = \ker(F_0 \to P)$. Since $P$ is projective, $F_0 \cong P \oplus K$, so $K$ is projective, and $0 \to F_n \to \dots \to F_1 \to K \to 0$ is a resolution of length $n - 1$. By induction $K \oplus F' \cong G'$ with $F', G'$ free. Then $P \oplus G' \cong P \oplus K \oplus F' \cong F_0 \oplus F'$.

Now suppose $P_\mathfrak{q} \cong B_\mathfrak{q}$ for every $\mathfrak{q}$, and add a free module to $F$ and $G$ so that $P \oplus B^m \cong B^{m'}$. Tensoring with the fraction field gives $m' = m + 1$. Exterior powers commute with localization and with direct sums in the form $\Lambda^s(M \oplus N) \cong \bigoplus_{i+j=s} \Lambda^i M \otimes \Lambda^j N$ (Eisenbud, appendix on multilinear algebra). Since $\Lambda^i(B_\mathfrak{q}) = 0$ for $i \geq 2$, Theorem P1.2.8 gives $\Lambda^i P = 0$ for $i \geq 2$. So
$$
B \cong \Lambda^{m+1} B^{m+1} \cong \Lambda^{m+1}(P \oplus B^m) \cong (\Lambda^1 P \otimes \Lambda^m B^m) \oplus (\Lambda^0 P \otimes \Lambda^{m+1} B^m) \cong P \oplus 0 = P . \qquad \square
$$

**Theorem P1.9.25 (Auslander-Buchsbaum).** A regular local ring is a unique factorization domain.

Lean: not in Mathlib.

*Proof.* Use induction on $d = \dim A$. If $d = 0$, then $A$ is a field. Let $d \geq 1$ and choose $x \in \mathfrak{m} \setminus \mathfrak{m}^2$. By the proposition on quotients by parameters in Section 9.1, $A/xA$ is a regular local ring, hence a domain, so $x$ is a prime element. By Nagata's criterion (Exercise 6 of Section 8.2), it suffices to show that the Noetherian domain $B = A_x$ is factorial, and by Proposition P1.5.23 that every prime $P$ of height one of $B$ is principal.

Let $\mathfrak{q}$ be a prime of $B$. Then $\mathfrak{q} = \mathfrak{q}'B$ for a prime $\mathfrak{q}'$ of $A$ with $x \notin \mathfrak{q}'$ (Theorem P1.2.6), and $B_\mathfrak{q} = A_{\mathfrak{q}'}$. Since $x \in \mathfrak{m}$, $\mathfrak{q}' \neq \mathfrak{m}$, so $\dim A_{\mathfrak{q}'} = \operatorname{ht} \mathfrak{q}' < d$. By the corollary on localization, $A_{\mathfrak{q}'}$ is regular, and by induction it is factorial. In the factorial ring $B_\mathfrak{q}$, the ideal $PB_\mathfrak{q}$ is either the unit ideal or a prime of height one, and in both cases it is principal and nonzero, so $P_\mathfrak{q} \cong B_\mathfrak{q}$. By Proposition P1.8.18, $P$ is an invertible ideal. An invertible ideal is projective: if $1 = \sum_{i=1}^s a_i b_i$ with $a_i \in P$ and $b_i \in (B : P)$, then $B^s \to P$, $e_i \mapsto a_i$, and $P \to B^s$, $y \mapsto (b_i y)_i$, compose to the identity of $P$, so $P$ is a direct summand of $B^s$.

The ideal $\mathfrak{p} = P \cap A$ of $A$ has a finite resolution by finitely generated free $A$-modules, by Serre's theorem. Localizing at $x$ gives such a resolution of $\mathfrak{p}B = P$ over $B$. The lemma on stably free modules gives $P \cong B$. If $f \in P$ is the image of $1$, then $P = fB$. $\square$

**Corollary P1.9.26 (smooth varieties are locally factorial).** A regular ring is locally factorial, and a regular domain is normal. If $A$ is a regular domain, then every Weil divisor on $\operatorname{Spec} A$ is Cartier and $\operatorname{Pic}(A) \cong \operatorname{Cl}(A)$. This applies to the coordinate ring of a smooth affine variety over a perfect field.

Lean: not in Mathlib.

*Proof.* For each maximal ideal $\mathfrak{m}$, $A_\mathfrak{m}$ is factorial by the theorem of Auslander and Buchsbaum, hence normal by Proposition P1.4.19. For a regular domain, normality follows from Proposition P1.4.20, and Theorem P1.8.20 gives $\operatorname{Pic}(A) \cong \operatorname{Cl}(A)$. By the Jacobian criterion of Section 9.2, the coordinate ring of a smooth affine variety over a perfect field has regular localizations at all maximal ideals, so it is regular by the corollary on localization. $\square$

### Proof in words

A regular system of parameters is a regular sequence, and its Koszul complex is a finite free resolution of the residue field. So over a regular local ring every module has a finite free resolution, and Serre showed that this property characterizes regular local rings. Since a finite resolution localizes to a finite resolution, regularity passes to localizations, which is hard to see from the definition. For factoriality, invert a prime element $x \in \mathfrak{m} \setminus \mathfrak{m}^2$. On the smaller ring $A_x$ every local ring is regular of smaller dimension, hence factorial, so every height one prime of $A_x$ is a line bundle. It has a finite free resolution, so it is stably free, and the top exterior power shows that a stably free line bundle is trivial. Nagata's criterion brings factoriality back from $A_x$ to $A$.

### Examples

**Example P1.9.27 (a regular ring that is not factorial).** The ring $A = \mathbb{Z}[\sqrt{-5}]$ is a Dedekind domain with $\operatorname{Cl}(A) \cong \mathbb{Z}/2$ (Example P1.7.27). It is regular and locally factorial, since its local rings are discrete valuation rings, but it is not factorial. The theorem of Auslander and Buchsbaum is local: a regular ring has trivial local class groups, and its global class group is its Picard group. The same holds for an affine elliptic curve, whose class group is the group of rational points of the elliptic curve (Example P1.7.29).

**Example P1.9.28 (nonzero local class groups detect singular points).** The local class group of the quadric cone at the vertex is $\mathbb{Z}/2$, and that of the cone $xw = yz$ is $\mathbb{Z}$, by Section 8.3. By the theorem of Auslander and Buchsbaum, neither local ring is regular, which agrees with the computation of the embedding dimensions in Section 9.1. The converse fails: for $k = \mathbb{C}$, the local ring of the surface $x^2 + y^3 + z^5 = 0$ at the origin is factorial but not regular, a classical result that this handbook does not prove. This $E_8$ singularity is a Du Val singularity of Volume 4.

**Example P1.9.29 (the singular locus of a normal variety).** Let $X = \operatorname{Spec} A$ be a normal affine variety over a perfect field. By Section 8.1, $A_\mathfrak{p}$ is a discrete valuation ring, hence regular, for every prime $\mathfrak{p}$ of height one. With the corollary on localization, the singular locus contains no prime of height at most one, so it has codimension at least two. For the cone $xy = z^n$ it is the vertex, of codimension two. The Whitney umbrella of Section 9.2 has a singular line in a surface, so it is not normal.

**Example P1.9.30 (the residue field of a non-regular ring).** Let $A = k[x]/(x^2)$. The minimal resolution of $k$ is
$$
\dots \xrightarrow{x} A \xrightarrow{x} A \xrightarrow{x} A \to k \to 0 ,
$$
with every $b_i = 1$, so $\operatorname{pd}_A k = \infty$, as Serre's theorem predicts for a ring of dimension $0$ that is not a field.

### Exercises

1. (A) For $A = k[[x, y]]$, write out the Koszul complex $0 \to A \to A^2 \to A \to k \to 0$ of $x, y$ and check its exactness directly.
2. (A) Let $A$ be a regular local ring and $M$ a finitely generated module with $\operatorname{Tor}^A_1(M, k) = 0$. Show that $M$ is free.
3. (A) Use the theorem of Auslander and Buchsbaum and Section 8.3 to show again that the vertex of the cone $xy = z^n$, $n \geq 2$, is not a regular point.
4. (B) Verify the minimal resolution of $k$ over $k[x]/(x^2)$ and compute $\operatorname{Tor}^A_i(k, k)$ for all $i$. Do the same for $A = k[x, y]/(xy)$ localized at the origin.
5. (B) Let $R = k[x_1, \dots, x_n]$ and let $M$ be a maximal ideal. Show that every finitely generated $R_M$-module has a free resolution of length at most $n$ by finitely generated free modules, a local form of Hilbert's syzygy theorem.
6. (B) Let $A$ be a regular local ring and $\mathfrak{p}$ a prime with $A/\mathfrak{p}$ regular. Using Exercise 7 of Section 9.1, show that $A_\mathfrak{p}$ is regular without Serre's theorem.
7. (C) Let $A$ be a regular ring. Show that $A[x]$ is regular. (Hint: for a maximal ideal $\mathfrak{n}$ of $A[x]$ put $\mathfrak{p} = \mathfrak{n} \cap A$. Show that $\mathfrak{n}A_\mathfrak{p}[x] = \mathfrak{p}A_\mathfrak{p}[x] + gA_\mathfrak{p}[x]$ for one polynomial $g$, and compute $\dim A[x]_\mathfrak{n} = \operatorname{ht}\mathfrak{p} + 1$ with Theorem P1.5.45, since $A[x]$ is flat over $A$.)
8. (B) Let $X$ be a normal affine surface over an algebraically closed field. Show that the singular locus of $X$ is a finite set of closed points. Compute the singular locus of the surfaces $xy = z^n$ and $x^2 + y^3 + z^5 = 0$ in characteristic $0$.

### Lean

Mathlib defines `IsRegularRing` and proves `IsRegularLocalRing.of_isRegularRing_of_isLocalRing`. It has an instance that a Dedekind domain is a regular ring, and the instances `Polynomial.isRegularRing_of_isRegularRing` and `MvPolynomial.isRegularRing_of_isRegularRing` for polynomial rings over a regular ring. Regular sequences are `RingTheory.Sequence.IsRegular`, projective dimension is `CategoryTheory.projectiveDimension`, and `ModuleCat.projectiveDimension_quotient_eq_length` computes the projective dimension of the quotient by a regular sequence. Serre's characterization, the localization theorem, which Mathlib lists as a TODO, and the theorem of Auslander and Buchsbaum are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

Whether a localization of a regular local ring is regular was an open question of the 1940s, and Serre answered it in 1956 with the homological characterization, which Auslander and Buchsbaum found independently at the same time. Auslander and Buchsbaum proved in 1959 that regular local rings are factorial. The proof here, with Nagata's criterion and stably free modules, is the one in Matsumura, Chapter 7, a simplification usually credited to Kaplansky. The literature state of every result here is theorem. The section follows Matsumura, Chapter 7, and Eisenbud, Chapters 17 and 19.
