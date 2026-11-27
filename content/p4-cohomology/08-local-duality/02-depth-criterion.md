---
title: The depth criterion
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:III.3, Har77:III.7]
requires: [P1.5, P1.10, P1.11, P3.6, P3.13, P4.2, P4.3, P4.7, P4.8]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The depth criterion

### Statement

Let $(A, \mathfrak{m}, k)$ be a Noetherian local ring and $M \neq 0$ a finitely generated $A$-module, with depth $t = \operatorname{depth} M$ (Definition P1.10.5) and dimension $d = \dim M = \dim A/\operatorname{Ann}(M)$. By Proposition P1.10.6, $t \leq d$.

**Theorem P4.8.10 (Grothendieck's depth and dimension theorem).**

1. $H^i_\mathfrak{m}(M) = 0$ for $i < t$ and for $i > d$.
2. $H^t_\mathfrak{m}(M) \neq 0$.
3. $H^d_\mathfrak{m}(M) \neq 0$.

So the depth of $M$ is the least $i$ and the dimension of $M$ the largest $i$ with $H^i_\mathfrak{m}(M) \neq 0$. Part 3 is proved in Section 8.3 (Corollary P4.8.21), by local duality.

Lean: not in Mathlib.

**Corollary P4.8.11 (the Cohen-Macaulay criterion).** $M$ is Cohen-Macaulay if and only if $H^i_\mathfrak{m}(M) = 0$ for all $i < \dim M$, that is, if and only if $H^i_\mathfrak{m}(M)$ is nonzero in exactly one degree. In particular, a point $x$ of a Noetherian scheme $X$ is a Cohen-Macaulay point if and only if $H^i_{\mathfrak{m}_x}(\mathcal{O}_{X,x}) = 0$ for $i < \dim \mathcal{O}_{X,x}$.

Lean: not in Mathlib.

**Corollary P4.8.12 (depth and the punctured spectrum).** Let $U = \operatorname{Spec} A \setminus \{\mathfrak{m}\}$ be the punctured spectrum, and $t \geq 2$ an integer.

1. $\operatorname{depth} A \geq 1$ if and only if the restriction $A \to \Gamma(U, \mathcal{O}_U)$ is injective, and $\operatorname{depth} A \geq 2$ if and only if it is bijective.
2. $\operatorname{depth} A \geq t$ if and only if $A \to \Gamma(U, \mathcal{O}_U)$ is bijective and $H^i(U, \mathcal{O}_U) = 0$ for $1 \leq i \leq t - 2$.

If $\operatorname{depth} A \geq 2$, then $U$ is connected.

Lean: not in Mathlib.

**Corollary P4.8.13 (cones).** Let $k$ be a field, $X \subseteq \mathbb{P}^n_k$ a closed subscheme of dimension $r \geq 1$, $I = \bigoplus_n \Gamma(\mathbb{P}^n, \mathcal{I}_X(n))$ its saturated homogeneous ideal, $S = k[x_0, \dots, x_n]/I$, and $A = S_\mathfrak{m}$ the local ring of the affine cone over $X$ at the vertex, $\mathfrak{m} = S_+$. Then $\dim A = r + 1$, $\operatorname{depth} A \geq 1$, and:

1. $\operatorname{depth} A \geq 2$ if and only if $S_n \to \Gamma(X, \mathcal{O}_X(n))$ is surjective for every $n \in \mathbb{Z}$;
2. $A$ is Cohen-Macaulay if and only if, in addition, $H^i(X, \mathcal{O}_X(n)) = 0$ for every $n \in \mathbb{Z}$ and $1 \leq i \leq r - 1$.

More precisely, $H^0_\mathfrak{m}(A) = 0$, $H^1_\mathfrak{m}(A) = \bigoplus_n \operatorname{coker}(S_n \to \Gamma(X, \mathcal{O}_X(n)))$ and $H^{i+1}_\mathfrak{m}(A) = \bigoplus_n H^i(X, \mathcal{O}_X(n))$ for $i \geq 1$.

Lean: not in Mathlib.

### Proof in words

Local cohomology turns a nonzerodivisor $x$ on $M$ into a long exact sequence for $0 \to M \xrightarrow{x} M \to M/xM \to 0$. Every class in $H^i_\mathfrak{m}(M)$ is killed by a power of $x$, so multiplication by $x$ on $H^i_\mathfrak{m}(M)$ can be injective only if $H^i_\mathfrak{m}(M) = 0$. By induction on the depth this gives the vanishing below the depth, and the sequence also injects $H^{t-1}_\mathfrak{m}(M/xM)$ into $H^t_\mathfrak{m}(M)$, which gives the nonvanishing at the depth. Above the dimension, the module $M$ lives over $A/\operatorname{Ann}(M)$, whose maximal ideal is the radical of an ideal with $d$ generators, and the local Čech complex for $d$ elements has length $d$. The corollaries read these statements through the comparison of Section 8.1: in low degrees local cohomology is the cohomology of the punctured spectrum, and for a cone it is the cohomology of the twists of $\mathcal{O}_X$.

### Examples

**Example P4.8.14 (two planes meeting in a point).** Let $A = k[x, y, z, w]/(xz, xw, yz, yw)$, the coordinate ring of the union of the planes $P_1 = V(z, w)$ and $P_2 = V(x, y)$ in $\mathbb{A}^4_k$, which meet only at the origin, and let $\mathfrak{m} = (x, y, z, w)$. The ideal is $(x, y) \cap (z, w)$, which gives the exact sequence
$$0 \to A \to k[x, y] \times k[z, w] \to k \to 0.$$
By part 4 of Theorem P4.8.4, the local cohomology of $k[x, y]$ for $\mathfrak{m}$ is its local cohomology for $(x, y)$, which is concentrated in degree $2$ by Example P4.8.8, and the same holds for $k[z, w]$. The module $k$ is $\mathfrak{m}$-torsion, so $H^0_\mathfrak{m}(k) = k$ and $H^i_\mathfrak{m}(k) = 0$ for $i > 0$. The long exact sequence gives
$$H^0_\mathfrak{m}(A) = 0, \qquad H^1_\mathfrak{m}(A) \cong k, \qquad H^2_\mathfrak{m}(A) \cong H^2_{(x, y)}(k[x, y]) \oplus H^2_{(z, w)}(k[z, w]).$$
So the local ring at the origin has depth $1$ and dimension $2$, as in Example P1.10.11, and it is not Cohen-Macaulay. In the language of Corollary P4.8.12, the punctured spectrum is disconnected: it is the disjoint union of the two punctured planes, and $\Gamma(U, \mathcal{O}_U) = k[x, y] \times k[z, w]$ is larger than $A$ by the one constant $k$. The projective version is Example P4.7.25: by Corollary P4.8.13, the cone over the two planes $X \subseteq \mathbb{P}^4$ is not Cohen-Macaulay at its vertex since $H^1(X, \mathcal{O}_X(n)) \neq 0$ for $n < 0$.

**Example P4.8.15 (cones over plane curves).** Let $C = V_+(F) \subseteq \mathbb{P}^2_k$ be a curve of degree $e \geq 1$ and $S = k[x, y, z]/(F)$. Its local ring at the vertex is a hypersurface, so it is Cohen-Macaulay by Corollary P1.10.15, and Corollary P4.8.13 confirms it: the restriction maps $S_n \to \Gamma(C, \mathcal{O}_C(n))$ are surjective by the sequence $0 \to \mathcal{O}(n - e) \to \mathcal{O}(n) \to \mathcal{O}_C(n) \to 0$ and $H^1(\mathbb{P}^2, \mathcal{O}(n - e)) = 0$, and $r - 1 = 0$. The only nonzero local cohomology is
$$H^2_\mathfrak{m}(S) = \bigoplus_n H^1(C, \mathcal{O}_C(n)), \qquad H^1(C, \mathcal{O}_C(n)) \cong \Gamma(C, \mathcal{O}_C(e - 3 - n))',$$
by Serre duality with $\omega^\circ_C = \mathcal{O}_C(e - 3)$ (Example P4.7.23). It is nonzero exactly in the degrees $n \leq e - 3$. For a smooth cubic, $e = 3$, the top degree is $0$ and $H^2_\mathfrak{m}(S)_0 = H^1(C, \mathcal{O}_C)$ is a line.

**Example P4.8.16 (the cone over an abelian surface).** Let $B \subseteq \mathbb{P}^n_k$ be an abelian surface, embedded so that the restriction maps $S_m \to \Gamma(B, \mathcal{O}_B(m))$ are surjective for every $m$. Such embeddings exist: the third power of an ample line bundle gives one, by a theorem of Koizumi. Then the local ring $A$ of the cone at the vertex is normal, and $\dim A = 3$. By Corollary P4.8.13, $H^0_\mathfrak{m}(A) = H^1_\mathfrak{m}(A) = 0$ and
$$H^2_\mathfrak{m}(A) = \bigoplus_m H^1(B, \mathcal{O}_B(m)) \supseteq H^1(B, \mathcal{O}_B),$$
which is a vector space of dimension $2$. So $\operatorname{depth} A = 2 < 3$, and $A$ is normal but not Cohen-Macaulay. This is the proof promised in Example P1.11.19. In the minimal model program this cone is the standard log canonical singularity that is not Cohen-Macaulay. Rational singularities are Cohen-Macaulay (Chapter 9), so this cone is not rational.

**Example P4.8.17 (a curve that is not projectively normal).** Let $C \subseteq \mathbb{P}^3_k$ be the image of $\mathbb{P}^1_k$ under $[s : t] \mapsto [s^4 : s^3 t : s t^3 : t^4]$. Its homogeneous coordinate ring $S$ is the subring of $k[s, t]$ generated by $s^4, s^3 t, s t^3, t^4$, a domain, so the ideal of $C$ is prime and saturated. The degree $1$ part $S_1$ has dimension $4$, while $\Gamma(C, \mathcal{O}_C(1)) = \Gamma(\mathbb{P}^1, \mathcal{O}(4))$ has dimension $5$, and the monomial $s^2 t^2$ is missing. By Corollary P4.8.13, $H^1_\mathfrak{m}(S) \neq 0$, so the cone over $C$ has depth $1$ and dimension $2$ at its vertex. It is not Cohen-Macaulay, and so not normal either: by Serre's criterion (Theorem P1.11.12) a normal local ring of dimension $2$ is Cohen-Macaulay. The smooth curve $C$ has a cone that is singular in a worse way than the cone over the rational normal quartic in $\mathbb{P}^4$, which is Cohen-Macaulay (Exercise 3).

### Proof

*Theorem P4.8.10.* Vanishing below the depth, by induction on $t$. For $t = 0$ there is nothing to prove. For $t \geq 1$, choose $x \in \mathfrak{m}$ that is a nonzerodivisor on $M$. Then $\operatorname{depth}(M/xM) = t - 1$, by Theorem P1.10.4, since an $M$-sequence of maximal length can start with $x$. The exact sequence $0 \to M \xrightarrow{x} M \to M/xM \to 0$ gives the exact sequence
$$H^{i-1}_\mathfrak{m}(M/xM) \to H^i_\mathfrak{m}(M) \xrightarrow{x} H^i_\mathfrak{m}(M).$$
For $i < t$, the left term vanishes by induction, so $x$ acts injectively on $H^i_\mathfrak{m}(M)$. Every element of $H^i_\mathfrak{m}(M)$ is killed by a power of $\mathfrak{m}$, hence by a power of $x$ (part 3 of Theorem P4.8.4). An element killed by $x^s$, with $x$ injective, is zero. So $H^i_\mathfrak{m}(M) = 0$ for $i < t$.

Nonvanishing at the depth, by induction on $t$. If $t = 0$, then $\mathfrak{m} \in \operatorname{Ass}(M)$, so $k \subseteq M$ and $H^0_\mathfrak{m}(M) = \Gamma_\mathfrak{m}(M) \supseteq k$ is nonzero. If $t \geq 1$, choose $x$ as above. The sequence
$$0 = H^{t-1}_\mathfrak{m}(M) \to H^{t-1}_\mathfrak{m}(M/xM) \to H^t_\mathfrak{m}(M)$$
is exact, and $M/xM \neq 0$ by Nakayama's lemma, with depth $t - 1$. By induction $H^{t-1}_\mathfrak{m}(M/xM) \neq 0$, so $H^t_\mathfrak{m}(M) \neq 0$.

Vanishing above the dimension. Let $B = A/\operatorname{Ann}(M)$, a Noetherian local ring of dimension $d$. By Corollary P1.5.22 there are $y_1, \dots, y_d$ in the maximal ideal $\mathfrak{m}B$ that generate an ideal with radical $\mathfrak{m}B$. By part 4 of Theorem P4.8.4, $H^i_\mathfrak{m}(M) \cong H^i_{\mathfrak{m}B}(M)$, computed over $B$, and by part 3 of the same theorem this is $H^i_{(y_1, \dots, y_d)}(M)$, which vanishes for $i > d$.

*Corollary P4.8.11.* If $M$ is Cohen-Macaulay, then $t = d$, and part 1 of Theorem P4.8.10 leaves only degree $d$. Conversely, if $H^i_\mathfrak{m}(M) = 0$ for $i < d$, then $t \geq d$ by part 2, so $t = d$. By part 3 the degree $d$ is always present, which gives the reformulation. The statement for schemes is the case $A = \mathcal{O}_{X,x}$.

*Corollary P4.8.12.* Apply part 6 of Theorem P4.8.4 to $\operatorname{Spec} A$ and $I = \mathfrak{m}$. The kernel of $A \to \Gamma(U, \mathcal{O}_U)$ is $H^0_\mathfrak{m}(A)$, its cokernel is $H^1_\mathfrak{m}(A)$, and $H^i(U, \mathcal{O}_U) = H^{i+1}_\mathfrak{m}(A)$ for $i \geq 1$. By parts 1 and 2 of Theorem P4.8.10, $\operatorname{depth} A \geq t$ if and only if $H^i_\mathfrak{m}(A) = 0$ for all $i < t$, which gives parts 1 and 2. If $\operatorname{depth} A \geq 2$, then $\Gamma(U, \mathcal{O}_U) = A$ is local and has no idempotents other than $0$ and $1$. A decomposition $U = U_1 \sqcup U_2$ into nonempty open sets would give the idempotent that is $1$ on $U_1$ and $0$ on $U_2$, so $U$ is connected. Part 1 is the case $I = \mathfrak{m}$ of Proposition P1.11.4, since $\Gamma(U, \mathcal{O}_U) = \operatorname{Hom}_A(\mathfrak{m}, A)$ when $\operatorname{depth} A \geq 1$ (Exercise 2).

*Corollary P4.8.13.* The dimension: the length of $A/\mathfrak{m}^n A$ is $\sum_{j < n} \dim_k S_j$, and $\dim_k S_j$ is the Hilbert polynomial of $X$ for large $j$ (Definition P3.13.12), of degree $r$ by Theorem P4.3.4. So $n \mapsto \ell(A/\mathfrak{m}^n A)$ is eventually a polynomial of degree $r + 1$, and $\dim A = r + 1$ by the dimension theorem (Theorem P1.5.35).

The local cohomology: by part 5 of Theorem P4.8.4, $H^i_{\mathfrak{m}A}(A) = H^i_\mathfrak{m}(S)$, since these modules are $\mathfrak{m}$-torsion. Proposition P4.8.6 with $M = S$ and $\widetilde{S} = \mathcal{O}_X$ gives the exact sequence $0 \to H^0_\mathfrak{m}(S) \to S \to \bigoplus_n \Gamma(X, \mathcal{O}_X(n)) \to H^1_\mathfrak{m}(S) \to 0$ and the isomorphisms in degrees $\geq 2$. The ideal $I$ is saturated: by the sequence $0 \to \mathcal{I}_X(n) \to \mathcal{O}(n) \to \mathcal{O}_X(n) \to 0$ and $\Gamma(\mathbb{P}^n, \mathcal{O}(n)) = k[x_0, \dots, x_n]_n$ (Theorem P4.2.1), the kernel of $k[x_0, \dots, x_n]_n \to \Gamma(X, \mathcal{O}_X(n))$ is $I_n$. So $S \to \bigoplus_n \Gamma(X, \mathcal{O}_X(n))$ is injective, and $H^0_\mathfrak{m}(A) = 0$, so $\operatorname{depth} A \geq 1$. The criteria now follow from Theorem P4.8.10 and Corollary P4.8.11.

### Exercises

1. (A) Let $M \neq 0$ have finite length. Show directly from the definitions that $H^0_\mathfrak{m}(M) = M$ and $H^i_\mathfrak{m}(M) = 0$ for $i > 0$, which is Theorem P4.8.10 with $t = d = 0$.
2. (A) Suppose $\operatorname{depth} A \geq 1$. Show that $\Gamma(U, \mathcal{O}_U) = \varinjlim_n \operatorname{Hom}_A(\mathfrak{m}^n, A)$, and that this equals $\operatorname{Hom}_A(\mathfrak{m}, A)$ when $\operatorname{depth} A \geq 2$.
3. (B) Let $C_r \subseteq \mathbb{P}^r_k$ be the rational normal curve of degree $r$ (Example P4.3.13). Show that $S_n \to \Gamma(C_r, \mathcal{O}(n))$ is surjective for all $n$, and deduce from Corollary P4.8.13 that the cone over $C_r$ is Cohen-Macaulay at its vertex.
4. (B) Let $X \subseteq \mathbb{P}^3_k$ be the union of two skew lines, with $S = k[x, y, z, w]/((x, y) \cap (z, w))$. Show that $H^1_\mathfrak{m}(S) \cong k$, concentrated in degree $0$, and that the cone over $X$ has depth $1$ at the vertex.
5. (B) Show that $\operatorname{depth} M = \operatorname{depth} \hat{M}$ and $\dim M = \dim \hat{M}$ for a finitely generated module over a Noetherian local ring, using Theorem P4.8.10 and part 5 of Theorem P4.8.4 for the depth and the Hilbert-Samuel function for the dimension.
6. (C) (Hartshorne's connectedness theorem) Let $A$ be a Noetherian local ring with $\operatorname{depth} A \geq 2$, and let $V(I)$, $V(J)$ be closed subsets of $\operatorname{Spec} A$ with $V(I) \cup V(J) = \operatorname{Spec} A$ and $V(I) \cap V(J) = \{\mathfrak{m}\}$. Show that $V(I)$ or $V(J)$ is $\{\mathfrak{m}\}$ or all of $\operatorname{Spec} A$. Deduce that a Cohen-Macaulay local ring of dimension at least $2$ is not the union of two components that meet only at the closed point, as in Example P4.8.14.

### Lean

Mathlib has depth through regular sequences and the Ext characterization of Theorem P1.10.4. The comparison of depth and dimension with local cohomology is not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

Theorem P4.8.10 is due to Grothendieck, in the 1961 seminar written up as *Local cohomology* (1967), where it is the first application of the theory. The criterion for cones goes back to the study of projectively normal varieties by Zariski, and the cone over an abelian surface appears in this role in the work of Kollár and others on singularities of the minimal model program. Koizumi proved in 1976 that the third power of an ample line bundle on an abelian variety is projectively normal. Hartshorne proved Exercise 6 in *Complete intersections and connectedness* (1962). The literature state is theorem. In the minimal model program, Corollary P4.8.13 is the test for the Cohen-Macaulay property of a cone over a Fano or Calabi-Yau variety, and Corollary P4.8.12 is the form of the $S_2$ condition used for extending sections over a closed set of codimension $2$.
