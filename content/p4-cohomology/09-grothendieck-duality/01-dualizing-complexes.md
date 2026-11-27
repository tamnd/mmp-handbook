---
title: Dualizing complexes
nodes: []
sources: [Har66, Har77, Stacks]
reads_with: [Har66:ch5, Har77:III.7]
requires: [P1.9, P1.10, P2.2, P2.8, P4.7, P4.8]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Dualizing complexes

### Statement

Let $A$ be a Noetherian ring. Write $D^b_{coh}(A)$ for the derived category of bounded complexes of $A$-modules with finitely generated cohomology, and $D^-_{coh}(A)$, $D^+_{coh}(A)$ for the bounded above and bounded below versions (Section P2.8.2). A complex $K$ has *finite injective dimension* if it is quasi-isomorphic to a bounded complex of injective modules.

**Lemma P4.9.1 (a test for injective dimension).** Let $M$ be an $A$-module and $n \geq 0$. If $\operatorname{Ext}^{n+1}_A(A/I, M) = 0$ for every ideal $I$, then $M$ has an injective resolution of length at most $n$. The same holds for a complex $K \in D^+(A)$ with $H^j(K) = 0$ for $j > n$: if $\operatorname{Ext}^{j}_A(A/I, K) = 0$ for all $j > n$ and all $I$, then $K$ is quasi-isomorphic to a complex of injectives that vanishes in degrees above $n$. In particular, a regular local ring $R$ of dimension $N$ has an injective resolution of length $N$.

Lean: not in Mathlib.

**Definition P4.9.2 (dualizing complex).** A *dualizing complex* for $A$ is a complex $D \in D^b_{coh}(A)$ of finite injective dimension for which the natural map $A \to R\operatorname{Hom}_A(D, D)$ is an isomorphism. The *duality functor* of $D$ is $\mathbb{D} = R\operatorname{Hom}_A(-, D)$.

**Proposition P4.9.3 (existence).**

1. If $A$ has finite injective dimension as a module over itself, then $A[0]$ is a dualizing complex. This holds for every regular local ring, by Lemma P4.9.1.
2. If $D$ is a dualizing complex for $A$ and $A \to B$ is a finite ring map, then $R\operatorname{Hom}_A(B, D)$ is a dualizing complex for $B$.
3. If $D$ is a dualizing complex for $A$ and $S \subseteq A$ is multiplicative, then $S^{-1} D$ is a dualizing complex for $S^{-1}A$.

So a quotient $A = R/J$ of a regular local ring, and its localizations, have the dualizing complex $R\operatorname{Hom}_R(A, R)$. By the Cohen structure theorem (Theorem P1.6.27), the completion of every Noetherian local ring is such a quotient.

Lean: not in Mathlib.

**Theorem P4.9.4 (duality, uniqueness and normalization).** Let $D$ be a dualizing complex for $A$.

1. $\mathbb{D}$ maps $D^-_{coh}(A)$ to $D^+_{coh}(A)$, $D^+_{coh}(A)$ to $D^-_{coh}(A)$ and $D^b_{coh}(A)$ to itself, and the natural map $K \to \mathbb{D}\mathbb{D}K$ is an isomorphism for $K \in D^b_{coh}(A)$. So $\mathbb{D}$ is an anti-equivalence of $D^b_{coh}(A)$ with itself.
2. Let $(A, \mathfrak{m}, k)$ be local. If $D'$ is a second dualizing complex, then $D' \cong D[n]$ for a unique integer $n$.
3. Let $(A, \mathfrak{m}, k)$ be local. Exactly one shift of $D$ satisfies $R\operatorname{Hom}_A(k, D) \cong k[0]$. It is the *normalized* dualizing complex $D_A$, unique up to isomorphism.

Lean: not in Mathlib.

**Theorem P4.9.5 (the cohomology of the normalized dualizing complex).** Let $A = R/J$ with $(R, \mathfrak{n}, k)$ regular local of dimension $N$, and let $d = \dim A$ and $t = \operatorname{depth} A$.

1. $D_A \cong R\operatorname{Hom}_R(A, R)[N]$, so $H^{-i}(D_A) \cong \operatorname{Ext}^{N-i}_R(A, R)$.
2. (Local duality) For a finitely generated $A$-module $M$, $H^i_\mathfrak{m}(M) \cong \operatorname{Hom}_A(\operatorname{Ext}^{-i}_A(M, D_A), E_A)$, and $\operatorname{Ext}^{-i}_A(M, D_A) \cong H^i_\mathfrak{m}(M)^\vee$ if $A$ is complete.
3. $H^j(D_A) \neq 0$ only for $-d \leq j \leq -t$, and $H^{-d}(D_A)$ and $H^{-t}(D_A)$ are nonzero. The lowest cohomology module is the canonical module, $H^{-d}(D_A) = K_A$ (Definition P4.8.22).
4. $A$ is Cohen-Macaulay if and only if $D_A \cong K_A[d]$.
5. $A$ has finite injective dimension over itself if and only if $D_A \cong A[d]$, if and only if $A$ is Cohen-Macaulay with $K_A \cong A$.

Lean: not in Mathlib.

By the theorem of Bass recalled after Definition P1.10.24, part 5 says that $A$ is Gorenstein if and only if $D_A \cong A[d]$.

**Definition P4.9.6 (dualizing complex on a scheme).** Let $X$ be a Noetherian scheme. A *dualizing complex* on $X$ is a complex $\omega^\bullet \in D^b_{coh}(\mathcal{O}_X)$ whose restriction to every affine open $\operatorname{Spec} A$ is given by a dualizing complex for $A$. This is Definition P2.8.24.

**Proposition P4.9.7 (projective schemes).** Let $k$ be a field, $P = \mathbb{P}^m_k$ with $\omega_P = \mathcal{O}_P(-m-1)$, and $i \colon X \to P$ a closed subscheme. Set
$$\omega^\bullet_X = R\mathcal{H}om_{\mathcal{O}_P}(i_* \mathcal{O}_X, \omega_P)[m],$$
regarded as a complex of $\mathcal{O}_X$-modules.

1. $\omega^\bullet_X$ is a dualizing complex on $X$, and $\mathcal{H}^{-j}(\omega^\bullet_X) = \mathcal{E}xt^{m-j}_P(\mathcal{O}_X, \omega_P)$.
2. For a closed point $x \in X$, the stalk $\omega^\bullet_{X,x}$ is the normalized dualizing complex of $\mathcal{O}_{X,x}$.
3. If $X$ is equidimensional of dimension $n$, then $\mathcal{H}^j(\omega^\bullet_X) = 0$ for $j < -n$ and $j > 0$, and $\mathcal{H}^{-n}(\omega^\bullet_X) = \omega^\circ_X$ is the dualizing sheaf of Theorem P4.7.17. The scheme $X$ is Cohen-Macaulay if and only if $\omega^\bullet_X \cong \omega^\circ_X[n]$.

Lean: not in Mathlib.

### Proof in words

A dualizing complex is a complex $D$ such that $\operatorname{Hom}$ into $D$ is a perfect duality on coherent complexes. Finite injective dimension makes $\mathbb{D}$ way out in both directions, so the comparison $K \to \mathbb{D}\mathbb{D}K$ reduces to $K = A$, where it is the definition. Over a regular local ring, $A$ itself is dualizing, and a finite ring map transports a dualizing complex by $R\operatorname{Hom}_A(B, -)$, the right adjoint of restriction of scalars. Over a local ring a dualizing complex is unique up to shift, and the shift is fixed by asking $R\operatorname{Hom}(k, D) = k$. With this normalization, the cohomology modules of $D$ are the modules $\operatorname{Ext}^{N-i}_R(A, R)$ of Chapter 8, so local duality says that $H^i_\mathfrak{m}$ is dual to $H^{-i}$ of $D$, and the depth, the dimension, the Cohen-Macaulay property and the canonical module are all read from the cohomology of $D$. On a projective scheme the same construction, with $R$ replaced by projective space, gives $\omega^\bullet_X$, whose cohomology sheaves are the Ext sheaves of Chapter 7.

### Examples

**Example P4.9.8 (hypersurfaces and complete intersections).** If $A = R/(f_1, \dots, f_c)$ for an $R$-regular sequence in a regular local ring $R$ of dimension $N$, then $d = N - c$ and part 3 of Proposition P4.8.23 gives $D_A = R\operatorname{Hom}_R(A, R)[N] = A[-c][N] = A[d]$. For the node $A = k[[x, y]]/(xy)$, $D_A = A[1]$. A complete intersection is Gorenstein, as Corollary P1.10.27 already said.

**Example P4.9.9 (two planes meeting in a point).** For $A = k[[x, y, z, w]]/((x, y) \cap (z, w))$, Example P4.8.25 gives
$$H^{-2}(D_A) = K_A \cong R/(z, w) \oplus R/(x, y), \qquad H^{-1}(D_A) \cong k,$$
and $H^j(D_A) = 0$ for the other $j$. The depth is $1$ and the dimension $2$, which are the two ends of the range in part 3 of Theorem P4.9.5. On the projective scheme $X = P_1 \cup P_2 \subseteq \mathbb{P}^4_k$ of Example P4.7.25, $\omega^\bullet_X$ has $\mathcal{H}^{-2} = \omega^\circ_X$ and $\mathcal{H}^{-1}$ a skyscraper sheaf at the singular point, which is the obstruction to full Serre duality found there.

**Example P4.9.10 (a curve with an embedded point).** Let $R = k[[x, y]]$ and $A = R/(x^2, xy)$, the line $V(x)$ with an embedded point at the origin. Then $d = 1$ and $H^0_\mathfrak{m}(A) = xA = kx$, a line, so $t = 0$. By local duality $H^0(D_A) = \operatorname{Ext}^2_R(A, R) \cong k$, and $H^{-1}(D_A) = K_A \cong \operatorname{Ext}^1_R(A, R)$. The local cohomology $H^1_\mathfrak{m}(A) \cong H^1_\mathfrak{m}(A/xA) = H^1_\mathfrak{m}(k[[y]])$, since $xA$ has finite length, so $K_A \cong k[[y]]$, the canonical module of the line. The embedded point appears only in $H^0(D_A)$.

### Proof

*Lemma P4.9.1.* Choose an injective resolution $0 \to M \to I^0 \to \dots \to I^{n-1} \to C \to 0$, where $C$ is the cokernel of $I^{n-2} \to I^{n-1}$. By dimension shifting, $\operatorname{Ext}^1_A(A/I, C) \cong \operatorname{Ext}^{n+1}_A(A/I, M) = 0$ for every ideal $I$. So every map $I \to C$ extends to $A$, and $C$ is injective by Baer's criterion (Theorem P2.2.33). For a complex $K$, choose an injective replacement $I^\bullet$ (Theorem P2.8.10), and replace it by its truncation $\tau_{\leq n}$, which is $\dots \to I^{n-1} \to Z^n \to 0$ with $Z^n = \ker(I^n \to I^{n+1})$. It is quasi-isomorphic to $K$ because $H^j(K) = 0$ for $j > n$. The complex $I^n \to I^{n+1} \to \dots$ is an injective resolution of $Z^n$ by the vanishing of $H^j$ for $j > n$, so $\operatorname{Ext}^1_A(A/I, Z^n) = \operatorname{Ext}^{n+1}_A(A/I, K) = 0$, and $Z^n$ is injective by Baer's criterion. For a regular local ring $R$, every finitely generated module has a free resolution of length at most $N$ (Theorem P1.9.21), so $\operatorname{Ext}^{N+1}_R(R/I, R) = 0$.

*Proposition P4.9.3.* Part 1: $R\operatorname{Hom}_A(A, A) = A$, and $A$ has finite injective dimension by hypothesis. Part 2: let $D_B = R\operatorname{Hom}_A(B, D)$, computed by $\operatorname{Hom}_A(B, I^\bullet)$ for a bounded injective replacement $I^\bullet$ of $D$. Each $\operatorname{Hom}_A(B, I^j)$ is an injective $B$-module, by the adjunction $\operatorname{Hom}_B(N, \operatorname{Hom}_A(B, I)) = \operatorname{Hom}_A(N, I)$, so $D_B$ has finite injective dimension. Its cohomology modules $\operatorname{Ext}^j_A(B, D)$ are finitely generated, since $B$ is a finitely generated $A$-module and $D \in D^b_{coh}(A)$. The same adjunction, derived, gives
$$R\operatorname{Hom}_B(D_B, D_B) = R\operatorname{Hom}_A(D_B, D) = \mathbb{D}\mathbb{D}(B),$$
which is $B$ by part 1 of Theorem P4.9.4, applied to the finitely generated $A$-module $B$. Part 3: localization is exact and takes injective modules over a Noetherian ring to injective modules, and $R\operatorname{Hom}$ between complexes with finitely generated cohomology commutes with localization.

*Theorem P4.9.4, part 1.* Let $D$ be quasi-isomorphic to a complex of injectives in degrees $[a, b]$. Then $H^j(\mathbb{D}K)$ depends only on the part of $K$ in degrees $[a - j, b - j]$, so $\mathbb{D}$ shifts bounds by a fixed amount, and its values have finitely generated cohomology because $\operatorname{Ext}^j_A(M, D)$ is finitely generated for finitely generated $M$. The map $K \to \mathbb{D}\mathbb{D}K$ is an isomorphism for $K = A$ by definition, hence for finitely generated free modules and, by the five lemma on triangles, for bounded complexes of them. For $K \in D^-_{coh}(A)$, choose a resolution $F^\bullet \to K$ by finitely generated free modules (Lemma P1.9.19). In a fixed degree, $H^j(\mathbb{D}\mathbb{D}F)$ and $H^j(F)$ agree with the same groups for the bounded complex $\sigma_{\geq -m}F$ of terms in degrees $\geq -m$, once $m$ is large compared with $j$, $a$ and $b$. So the map is an isomorphism in every degree.

*Part 2.* Let $L = R\operatorname{Hom}_A(D, D')$ and $L' = R\operatorname{Hom}_A(D', D)$. Both lie in $D^b_{coh}(A)$, and part 1 for $D$ and for $D'$, applied to the evaluation maps, gives $D' \cong D \otimes^L_A L$ and $A \cong L \otimes^L_A L'$. Hartshorne, *Residues and duality*, V.3.1, checks these two isomorphisms in detail. Apply $- \otimes^L_A k$: the complexes $L \otimes^L_A k$ and $L' \otimes^L_A k$ are complexes of $k$-vector spaces, isomorphic in $D(k)$ to their cohomology, with finite total dimension, and their tensor product is $k[0]$. So each has total dimension $1$, and $L \otimes^L_A k \cong k[n]$ for some $n$. Choose a minimal free resolution of $L$ (Lemma P1.9.19): its terms are $A^{b_j}$ with $b_j = \dim_k H^j(L \otimes^L_A k)$, so it is a single copy of $A$ in degree $-n$, and $L \cong A[n]$. Then $D' \cong D[n]$. The shift is unique, since $H^j(D) \neq 0$ for some $j$ and $D$ is bounded.

*Part 3.* Compute $W = R\operatorname{Hom}_A(k, D)$ by $\operatorname{Hom}_A(k, I^\bullet)$, a bounded complex of $k$-vector spaces, so $W \cong \bigoplus_j H^j(W)[-j]$ with $w_j = \dim_k H^j(W)$ finite. For a complex $V$ of $k$-vector spaces, $R\operatorname{Hom}_A(V, D) = R\operatorname{Hom}_k(V, W)$ by adjunction. With $V = W$ and part 1, $k \cong \mathbb{D}\mathbb{D}k = R\operatorname{Hom}_k(W, W)$, whose total dimension is $(\sum_j w_j)^2$. So exactly one $w_j$ is nonzero, and it equals $1$: $W \cong k[-j]$. The shift $D[j]$ satisfies $R\operatorname{Hom}_A(k, D[j]) = k[0]$, and by part 2 no other shift does.

*Theorem P4.9.5, part 1.* By Proposition P4.9.3, $D = R\operatorname{Hom}_R(A, R)$ is a dualizing complex for $A$. By adjunction, $R\operatorname{Hom}_A(k, D) = R\operatorname{Hom}_R(k, R)$, which is $k[-N]$ by the Koszul computation in the proof of Theorem P4.8.20. So $D[N]$ is normalized.

*Part 2.* By adjunction, $\operatorname{Ext}^{-i}_A(M, D_A) = \operatorname{Ext}^{N-i}_R(M, R)$. Apply part 1 of Corollary P4.8.21, and part 3 of Theorem P4.8.20 together with part 3 of Proposition P4.8.18 when $A$ is complete.

*Part 3.* By part 2 with $M = A$, $H^{-i}(D_A) = 0$ if and only if $H^i_\mathfrak{m}(A) = 0$, using that $\operatorname{Hom}_A(-, E_A)$ is faithful (part 4 of Proposition P4.8.18). Theorem P4.8.10 and part 3 of Corollary P4.8.21 give the range and the nonvanishing at both ends. The identification $H^{-d}(D_A) = \operatorname{Ext}^{N-d}_R(A, R) = K_A$ is Definition P4.8.22.

*Part 4.* A complex with a single nonzero cohomology module $H$ in degree $-d$ is isomorphic to $H[d]$. By part 3, $D_A$ has cohomology in one degree if and only if $t = d$.

*Part 5.* If $A$ has finite injective dimension, $A[0]$ is dualizing by Proposition P4.9.3, so $D_A \cong A[n]$ by part 2 of Theorem P4.9.4, and part 3 forces $n = d$. Conversely, $D_A \cong A[d]$ has finite injective dimension, so $A$ does. The last equivalence is part 4.

*Proposition P4.9.7.* The question is local, and on an affine open $\operatorname{Spec} R'$ of $P$ on which $\omega_P$ is trivial, the complex is $R\operatorname{Hom}_{R'}(A', R')[m]$ for $A' = R'/J'$ (Proposition P4.7.3). The ring $R'$ is regular of dimension $m$ at every closed point and its localizations are regular (Corollary P1.9.22), so $R'_\mathfrak{q}$ has finite injective dimension at every prime $\mathfrak{q}$ by Lemma P4.9.1. Since $R'$ has finite Krull dimension, $\operatorname{Ext}^{j}_{R'}(R'/I, R') = 0$ for $j > m$ and every $I$, by checking at every localization, so $R'$ has finite injective dimension by Lemma P4.9.1. Proposition P4.9.3 gives part 1, and the computation of $\mathcal{H}^{-j}$ is Proposition P4.7.3. For part 2, the stalk at a closed point $x$ is $R\operatorname{Hom}_R(A, R)[m]$ with $R = \mathcal{O}_{P,x}$ regular of dimension $m$, which is normalized by part 1 of Theorem P4.9.5. Part 3: at a closed point $x$, $\dim \mathcal{O}_{X,x} = n$ (Theorem P3.7.4), so part 3 of Theorem P4.9.5 gives the range at closed points, and every point specializes to a closed point. The identification $\mathcal{H}^{-n}(\omega^\bullet_X) = \mathcal{E}xt^{m-n}_P(\mathcal{O}_X, \omega_P) = \omega^\circ_X$ is the definition in Theorem P4.7.17, and the Cohen-Macaulay criterion is part 4 of Theorem P4.9.5 at the closed points.

### Exercises

1. (A) Show that $k[x]/(x^2)$ has finite injective dimension over itself, and that $k[x, y]/(x^2, xy, y^2)$ does not. Compute $D_A$ for both.
2. (A) Let $D$ be a dualizing complex for a Noetherian local ring $A$ and $M$ a module of finite length. Show that $\mathbb{D}(M) \cong M^\vee[0]$ when $D$ is normalized, using part 3 of Theorem P4.9.4 and induction on the length.
3. (B) Let $A = R/J$ be as in Theorem P4.9.5 and $\mathfrak{p}$ a prime of $A$. Show that $(D_A)_\mathfrak{p} \cong D_{A_\mathfrak{p}}[\dim A/\mathfrak{p}]$, using Corollary P4.8.21 to locate the lowest nonzero cohomology. Deduce that the Cohen-Macaulay locus of $A$ is open.
4. (B) In Example P4.9.10, compute $D_A$ by the resolution $0 \to R \to R^2 \to R \to A \to 0$ given by the generators $x^2, xy$ and the relation $y \cdot x^2 - x \cdot xy = 0$, and confirm $H^0(D_A) \cong k$ and $H^{-1}(D_A) \cong k[[y]]$.
5. (B) Let $X \subseteq \mathbb{P}^m_k$ be a closed subscheme of dimension $n$ and $Z \subseteq X$ the set of points $x$ with $\mathcal{H}^j(\omega^\bullet_X)_x \neq 0$ for some $j \neq -n$. Show that $Z$ is closed and that it is the non Cohen-Macaulay locus when $X$ is equidimensional.
6. (C) Let $A$ be a Noetherian local ring with a dualizing complex $D$. Show that the completion $\hat{A}$ has the dualizing complex $D \otimes_A \hat{A}$, and deduce from part 2 of Theorem P4.9.5 that local duality holds for $A$ after completion, which is part 2 of Theorem P2.8.25.

### Lean

Mathlib has injective modules, Baer's criterion and the derived category of an abelian category. Dualizing complexes are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

Dualizing complexes were introduced by Grothendieck and written up by Hartshorne in *Residues and duality* (1966), Chapter V, where Theorem P4.9.4 is proved for any Noetherian ring of finite Krull dimension. The criterion of Lemma P4.9.1 is Baer's criterion in the form of Bass. Kawasaki proved in 2002 that a Noetherian ring has a dualizing complex if and only if it is a quotient of a Gorenstein ring of finite dimension. The literature state is theorem. In the minimal model program the dualizing complex is the object that makes duality statements about singular varieties possible without first proving the Cohen-Macaulay property, and Kempf's criterion in Section 9.3 is the main example.
