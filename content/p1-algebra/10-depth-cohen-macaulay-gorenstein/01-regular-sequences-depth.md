---
title: Regular sequences and depth
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [Mat86:ch6, Eis95:ch17, Eis95:ch18]
requires: [P1.1, P1.2, P1.3, P1.5, P1.6, P1.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Regular sequences and depth

### Statement

Throughout, $A$ is a Noetherian ring, $M$ and $N$ are finitely generated $A$-modules and $I$ is an ideal. The section uses the functors $\operatorname{Ext}^i_A(N, M)$, computed as the cohomology of $\operatorname{Hom}_A(P_\bullet, M)$ for a projective resolution $P_\bullet$ of $N$. The standard facts used are these (Eisenbud, appendix on homological algebra): $\operatorname{Ext}^0_A(N, M) = \operatorname{Hom}_A(N, M)$; a short exact sequence in either variable gives a long exact sequence; $\operatorname{Ext}^i_A(N, M)$ is a finitely generated $A$-module, and for $a \in A$ multiplication by $a$ on it is the map induced by multiplication by $a$ on $N$, and also the map induced by multiplication by $a$ on $M$; and for a flat ring map $A \to B$ with $B$ Noetherian, $\operatorname{Ext}^i_B(N \otimes_A B, M \otimes_A B) \cong \operatorname{Ext}^i_A(N, M) \otimes_A B$.

**Definition P1.10.1 (regular sequence).** A sequence $x_1, \dots, x_n \in A$ is *$M$-regular*, or an *$M$-sequence*, if

1. for each $i$, the element $x_i$ is a nonzerodivisor on $M/(x_1, \dots, x_{i-1})M$, and
2. $M/(x_1, \dots, x_n)M \neq 0$.

An $M$-sequence in $I$ is *maximal* if it cannot be extended by an element of $I$ to a longer $M$-sequence.

Lean: Mathlib `RingTheory.Sequence.IsWeaklyRegular` (condition 1) and `RingTheory.Sequence.IsRegular` (conditions 1 and 2), as definitions.

If $x_1, \dots, x_n$ is an $M$-sequence in $I$, then $x_{i+1} \notin (x_1, \dots, x_i)$, since $x_{i+1}$ acts as zero on the nonzero module $M/(x_1, \dots, x_i)M$. So the ideals $(x_1) \subsetneq (x_1, x_2) \subsetneq \dots$ form a strictly increasing chain, and since $A$ is Noetherian every $M$-sequence in $I$ extends to a maximal one.

**Lemma P1.10.2 (homomorphisms and zero divisors).** If $N \neq 0$, then $\operatorname{Hom}_A(N, M) = 0$ if and only if $\operatorname{Ann}(N)$ contains a nonzerodivisor on $M$.

Lean: Mathlib `IsSMulRegular.subsingleton_linearMap_iff` (proved in Mathlib).

*Proof.* If $r \in \operatorname{Ann}(N)$ is a nonzerodivisor on $M$ and $f : N \to M$ is linear, then $r f(n) = f(rn) = 0$, so $f(n) = 0$. Conversely, suppose every element of $\operatorname{Ann}(N)$ is a zero divisor on $M$. By Proposition P1.2.44 and Theorem P1.2.46, the zero divisors on $M$ form the finite union of the associated primes of $M$, so prime avoidance (Proposition P1.1.11) gives $\operatorname{Ann}(N) \subseteq \mathfrak{p}$ for some $\mathfrak{p} \in \operatorname{Ass}(M)$. There is an injection $A/\mathfrak{p} \to M$, and localizing gives an injection $\kappa(\mathfrak{p}) \to M_\mathfrak{p}$. Since $\mathfrak{p} \supseteq \operatorname{Ann}(N)$, $N_\mathfrak{p} \neq 0$, and by Nakayama's lemma $N_\mathfrak{p}/\mathfrak{p}N_\mathfrak{p} \neq 0$. A nonzero linear form on this $\kappa(\mathfrak{p})$-vector space gives a nonzero map $N_\mathfrak{p} \to \kappa(\mathfrak{p}) \to M_\mathfrak{p}$. Since $N$ is finitely presented, $\operatorname{Hom}_A(N, M)_\mathfrak{p} \cong \operatorname{Hom}_{A_\mathfrak{p}}(N_\mathfrak{p}, M_\mathfrak{p}) \neq 0$, so $\operatorname{Hom}_A(N, M) \neq 0$. $\square$

**Lemma P1.10.3 (Ext and a regular element).** Let $x \in \operatorname{Ann}(N)$ be a nonzerodivisor on $M$. Then for every $i \geq 0$ there is an exact sequence
$$
0 \to \operatorname{Ext}^i_A(N, M) \to \operatorname{Ext}^i_A(N, M/xM) \to \operatorname{Ext}^{i+1}_A(N, M) \to 0 .
$$

Lean: not in Mathlib in this form.

*Proof.* The sequence $0 \to M \xrightarrow{x} M \to M/xM \to 0$ is exact and gives a long exact sequence of Ext. The map $\operatorname{Ext}^i_A(N, M) \to \operatorname{Ext}^i_A(N, M)$ induced by $x$ on $M$ is multiplication by $x$, which is also the map induced by $x$ on $N$, and this is zero since $xN = 0$. So the long exact sequence breaks into the short exact sequences of the statement. $\square$

**Theorem P1.10.4 (Rees).** Suppose $IM \neq M$. Then every maximal $M$-sequence in $I$ has the same length $n$, and
$$
n = \min\{ i : \operatorname{Ext}^i_A(A/I, M) \neq 0 \} .
$$
For every $M$-sequence $x_1, \dots, x_r$ in $I$, $\operatorname{Ext}^i_A(A/I, M) = 0$ for $i < r$ and $\operatorname{Ext}^r_A(A/I, M) \cong \operatorname{Hom}_A(A/I, M/(x_1, \dots, x_r)M)$.

Lean: Mathlib `ModuleCat.exists_isRegular_tfae` (proved in Mathlib), which shows that an $M$-sequence of length $n$ in $I$ exists if and only if $\operatorname{Ext}^i(A/I, M) = 0$ for $i < n$, and `Ideal.depth_eq_sSup_length_isRegular`.

*Proof.* First the second statement, by induction on $r$. For $r = 0$ it is the identity $\operatorname{Ext}^0 = \operatorname{Hom}$. Let $r \geq 1$ and $M' = M/x_1M$. Then $x_2, \dots, x_r$ is an $M'$-sequence in $I$, and by induction $\operatorname{Ext}^i_A(A/I, M') = 0$ for $i < r - 1$ and $\operatorname{Ext}^{r-1}_A(A/I, M') \cong \operatorname{Hom}_A(A/I, M/(x_1, \dots, x_r)M)$. Apply the lemma on Ext with $N = A/I$ and $x = x_1$. It gives $\operatorname{Ext}^{i+1}_A(A/I, M) = 0$ for $i < r - 1$, and $\operatorname{Ext}^0_A(A/I, M) = 0$ by the lemma on homomorphisms, since $x_1 \in I = \operatorname{Ann}(A/I)$. So $\operatorname{Ext}^i_A(A/I, M) = 0$ for $i < r$. In the lemma for $i = r - 1$ the left term is now zero, so $\operatorname{Ext}^{r}_A(A/I, M) \cong \operatorname{Ext}^{r-1}_A(A/I, M')$, which is the claimed module.

Now let $x_1, \dots, x_r$ be a maximal $M$-sequence in $I$ and $\bar{M} = M/(x_1, \dots, x_r)M \neq 0$. Maximality means that every element of $I$ is a zero divisor on $\bar{M}$, so by the lemma on homomorphisms, $\operatorname{Hom}_A(A/I, \bar{M}) \neq 0$. So $\operatorname{Ext}^r_A(A/I, M) \neq 0$, while $\operatorname{Ext}^i_A(A/I, M) = 0$ for $i < r$. Hence $r$ is the least $i$ with $\operatorname{Ext}^i_A(A/I, M) \neq 0$, which does not depend on the sequence. $\square$

**Definition P1.10.5 (depth).** If $IM \neq M$, the common length of the maximal $M$-sequences in $I$ is the *depth of $M$ in $I$*, written $\operatorname{depth}_I(M)$, also called the *grade*. For a Noetherian local ring $(A, \mathfrak{m}, k)$ and $M \neq 0$, the *depth* of $M$ is $\operatorname{depth} M = \operatorname{depth}_\mathfrak{m}(M)$. By Rees's theorem it is the least $i$ with $\operatorname{Ext}^i_A(k, M) \neq 0$.

Lean: Mathlib `Ideal.depth` and `IsLocalRing.depth` (definitions through Ext), with `IsLocalRing.depth_eq_sSup_length_isRegular` (proved in Mathlib).

For local $A$ the condition $\mathfrak{m}M \neq M$ holds for $M \neq 0$ by Nakayama's lemma. The depth is $0$ exactly when $\mathfrak{m}$ is an associated prime of $M$, that is, when $M$ has a nonzero element killed by $\mathfrak{m}$. If $x \in \mathfrak{m}$ is a nonzerodivisor on $M$, then $\operatorname{depth} M/xM = \operatorname{depth} M - 1$, since $x$ followed by a maximal $M/xM$-sequence is a maximal $M$-sequence.

**Proposition P1.10.6 (depth and dimension).** Let $(A, \mathfrak{m})$ be local and $M \neq 0$. Then $\operatorname{depth} M \leq \dim A/\mathfrak{p}$ for every $\mathfrak{p} \in \operatorname{Ass}(M)$. In particular $\operatorname{depth} M \leq \dim M$, where $\dim M = \dim A/\operatorname{Ann}(M)$.

Lean: not in Mathlib.

*Proof.* Use induction on $\operatorname{depth} M$, the case $0$ being clear. Let $\operatorname{depth} M \geq 1$, let $x \in \mathfrak{m}$ be a nonzerodivisor on $M$, and let $\mathfrak{p} \in \operatorname{Ass}(M)$. Then $x \notin \mathfrak{p}$, since $\mathfrak{p}$ consists of zero divisors on $M$. The module $H = \operatorname{Hom}_A(A/\mathfrak{p}, M)$ is nonzero and finitely generated, and applying $\operatorname{Hom}_A(A/\mathfrak{p}, -)$ to $0 \to M \xrightarrow{x} M \to M/xM \to 0$ gives an exact sequence $0 \to H \xrightarrow{x} H \to \operatorname{Hom}_A(A/\mathfrak{p}, M/xM)$. By Nakayama's lemma $xH \neq H$, so there is a nonzero map $A/\mathfrak{p} \to M/xM$. Its image is a nonzero submodule of $M/xM$ killed by $\mathfrak{p} + xA$, and an associated prime $\mathfrak{q}$ of this submodule is an associated prime of $M/xM$ that contains $\mathfrak{p} + xA$. Since $x \notin \mathfrak{p}$, $\mathfrak{q} \supsetneq \mathfrak{p}$, and $\dim A/\mathfrak{q} \leq \dim A/\mathfrak{p} - 1$. By induction, $\operatorname{depth} M - 1 = \operatorname{depth} M/xM \leq \dim A/\mathfrak{q} \leq \dim A/\mathfrak{p} - 1$.

For the last claim, the minimal primes of $\operatorname{Supp} M = V(\operatorname{Ann} M)$ are associated primes of $M$ by Theorem P1.2.48, and $\dim M$ is the largest $\dim A/\mathfrak{p}$ over them. $\square$

**Proposition P1.10.7 (depth and completion).** Let $(A, \mathfrak{m}, k)$ be local and $M \neq 0$. Then $\operatorname{depth}_A M = \operatorname{depth}_{\hat{A}} \hat{M}$.

Lean: not in Mathlib.

*Proof.* By Theorem P1.6.18, $\hat{A}$ is flat over $A$, Noetherian and local with residue field $k$, and $\hat{M} = M \otimes_A \hat{A}$ by Theorem P1.6.13. Flat base change gives $\operatorname{Ext}^i_{\hat{A}}(k, \hat{M}) \cong \operatorname{Ext}^i_A(k, M) \otimes_A \hat{A}$. The module $E = \operatorname{Ext}^i_A(k, M)$ is killed by $\mathfrak{m}$, so it is a finite dimensional $k$-vector space, and $E \otimes_A \hat{A} \cong E \otimes_k (\hat{A}/\mathfrak{m}\hat{A}) \cong E$. So the two Ext modules vanish for the same $i$, and Rees's theorem gives the claim. $\square$

**Theorem P1.10.8 (Auslander-Buchsbaum formula).** Let $(A, \mathfrak{m})$ be local and $M \neq 0$ with $\operatorname{pd}_A M < \infty$. Then
$$
\operatorname{pd}_A M + \operatorname{depth} M = \operatorname{depth} A .
$$

Lean: not in Mathlib.

*Proof sketch.* If $\operatorname{pd} M = 0$, then $M$ is free by Theorem P1.1.50, and $\operatorname{depth} M = \operatorname{depth} A$, since an $A$-sequence is the same as an $A^b$-sequence. If $\operatorname{pd} M \geq 1$ and $\operatorname{depth} A = 0$, a minimal resolution $0 \to F_n \to F_{n-1} \to \dots$ as in Section 9.3 has its last map injective with entries in $\mathfrak{m}$, and an element $s \neq 0$ with $s\mathfrak{m} = 0$ kills the image while not killing $F_n$, a contradiction. So $\operatorname{depth} A \geq 1$. If also $\operatorname{depth} M \geq 1$, choose $x \in \mathfrak{m}$ regular on both $A$ and $M$ by prime avoidance. Then $\operatorname{pd}_{A/xA} M/xM = \operatorname{pd}_A M$, and the formula for $A/xA$ gives the formula for $A$. If $\operatorname{depth} M = 0$, a syzygy $0 \to K \to F \to M \to 0$ has $\operatorname{depth} K = 1$ and $\operatorname{pd} K = \operatorname{pd} M - 1$, and the formula for $K$ gives the formula for $M$. The details are in Eisenbud, Chapter 19, and Matsumura, Chapter 7. $\square$

For a regular local ring every finitely generated module has finite projective dimension by Section 9.3, so the formula says that $\operatorname{pd} M = \dim A - \operatorname{depth} M$.

### Proof in words

A regular sequence peels off one dimension at a time: each element cuts the module by a hypersurface that meets no associated component. The vanishing of $\operatorname{Hom}(A/I, -)$ detects whether one more element of $I$ can be added, and the exact sequence of Ext for a regular element shifts the index by one. So the first nonvanishing $\operatorname{Ext}^i(A/I, M)$ is the length of every maximal sequence, which is the depth. Since each element cuts every associated component properly, the depth is bounded by the dimension of the smallest one. Ext commutes with completion, so depth is a formal invariant. The formula of Auslander and Buchsbaum trades projective dimension for depth.

### Examples

**Example P1.10.9 (regular local rings).** Let $A$ be regular of dimension $d$. By the proposition on quotients by parameters in Section 9.1, a regular system of parameters is an $A$-sequence, so $\operatorname{depth} A \geq d$, and the proposition on depth and dimension gives $\operatorname{depth} A = d$. For $A = k[[x_1, \dots, x_d]]$ the variables form a maximal $A$-sequence.

**Example P1.10.10 (an embedded point).** Let $A = k[x, y]_{(x, y)}/(x^2, xy)$, the line $x = 0$ with an embedded point at the origin as in Example P1.2.36. The element $x$ is nonzero and $\mathfrak{m}x = (x^2, xy) = 0$, so $\mathfrak{m}$ is associated and $\operatorname{depth} A = 0$, while $\dim A = 1$. The bound of the proposition is attained at $\mathfrak{p} = \mathfrak{m}$.

**Example P1.10.11 (two planes meeting in a point).** Let $A = k[x, y, z, w]/((x, y) \cap (z, w))$ as in Example P1.5.50, localized at the origin, with maximal ideal $\mathfrak{m}$. Then $\dim A = 2$ and $\operatorname{depth} A = 1$. Put $B = k[x, y] \times k[z, w]$, localized at the two origins, the coordinate rings of the two planes. The map $A \to B$, $f \mapsto (f \bmod (z, w), f \bmod (x, y))$, is injective since $(x, y) \cap (z, w) = 0$ in $A$, and its image is the set of pairs with the same value at the origin. So there is an exact sequence of $A$-modules
$$
0 \to A \to B \to k \to 0 .
$$
The elements $s = x + z$ and $t = y + w$ act on $B$ as $(x, z)$ and $(y, w)$, so they form a $B$-sequence and $\operatorname{depth}_A B \geq 2$. Rees's theorem gives $\operatorname{Ext}^0_A(k, B) = \operatorname{Ext}^1_A(k, B) = 0$, and the long exact sequence gives $\operatorname{Ext}^1_A(k, A) \cong \operatorname{Hom}_A(k, k) = k \neq 0$. So $\operatorname{depth} A \leq 1$. The element $s$ is a nonzerodivisor on $B$, hence on $A \subseteq B$, so $\operatorname{depth} A = 1$.

**Example P1.10.12 (the order of a regular sequence matters).** Let $A = k[x, y, z]$. The sequence $x, y(1 - x), z(1 - x)$ is $A$-regular: $x$ is a nonzerodivisor, $A/xA = k[y, z]$, and the images of the other two elements are $y$ and $z$. The permuted sequence $y(1 - x), z(1 - x), x$ is not regular: in $A/(y(1-x))$, the element $y$ is nonzero, since $y \notin (y(1 - x))$, and $z(1-x) \cdot y = 0$. In a local ring, and for modules over a local ring, every permutation of a regular sequence in $\mathfrak{m}$ is regular (Exercise 6). Here $1 - x$ is a unit near the origin but not near the plane $x = 1$.

### Exercises

1. (A) Show that $x_1, \dots, x_d$ is a regular sequence in $k[x_1, \dots, x_d]$ and in $k[[x_1, \dots, x_d]]$.
2. (A) Let $A$ be a Noetherian local ring with $\operatorname{depth} A = 0$ and $\dim A \geq 1$. Show that $A$ has an embedded associated prime.
3. (A) Let $A = k[x, y]_{(x, y)}/(x^2, xy)$. Compute $\operatorname{Hom}_A(k, A)$ and check that $\operatorname{Ext}^0_A(k, A) \neq 0$.
4. (B) Let $(A, \mathfrak{m})$ be local and $0 \to M' \to M \to M'' \to 0$ exact with all three modules nonzero. Show that $\operatorname{depth} M \geq \min(\operatorname{depth} M', \operatorname{depth} M'')$ and $\operatorname{depth} M' \geq \min(\operatorname{depth} M, \operatorname{depth} M'' + 1)$.
5. (B) Let $A$ be a Noetherian domain and $I \neq A$ a nonzero ideal. Show that $\operatorname{depth}_I(A) \geq 1$, and that $\operatorname{depth}_I(A) \leq \operatorname{ht} I$. (Hint: localize at a minimal prime of $I$ and use the proposition on depth and dimension.)
6. (B) Let $(A, \mathfrak{m})$ be local and $x, y \in \mathfrak{m}$ an $M$-sequence. Show that $y, x$ is an $M$-sequence. (Hint: if $yu = 0$ in $M$, write $u = xv$ and use Krull's intersection theorem to show that $u = 0$.)
7. (B) Let $A$ be a regular local ring of dimension $d$ and $M$ finitely generated. Show that $M$ is free if and only if $\operatorname{depth} M = d$.
8. (C) Let $A = k[s^4, s^3t, st^3, t^4]$ localized at the ideal $\mathfrak{m}$ generated by the four monomials. Show that $x = s^4$ is a nonzerodivisor, that $u = s^3t$ satisfies $u^2 \notin xA$ and $t^4u^2 \in xA$, and deduce that $s^4, t^4$ is not an $A$-sequence. Show that $\operatorname{depth} A = 1$. (Hint: show that every element of $\mathfrak{m}$ is a zero divisor on $A/xA$ by exhibiting an element of $A/xA$ killed by $\mathfrak{m}$.)

### Lean

Mathlib defines regular sequences as `RingTheory.Sequence.IsWeaklyRegular` and `RingTheory.Sequence.IsRegular`, and proves `IsLocalRing.isRegular_of_perm`, the invariance under permutation for Noetherian modules over a local ring. It defines depth through Ext as `ModuleCat.depth`, `Ideal.depth` and `IsLocalRing.depth`, and proves Rees's theorem as `ModuleCat.exists_isRegular_tfae` and `Ideal.depth_eq_sSup_length_isRegular`. The bound by the dimension, the invariance under completion and the Auslander-Buchsbaum formula are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

Regular sequences go back to Macaulay's work on unmixed polynomial ideals of 1916. The homological definition of depth and its comparison with regular sequences are due to Auslander and Buchsbaum and to Rees in the 1950s, and Rees's theorem is from 1957. The formula of Auslander and Buchsbaum is from their paper of 1957 on homological dimension. The literature state of every result here is theorem. The section follows Matsumura, Chapter 6, and Eisenbud, Chapters 17 and 18.
