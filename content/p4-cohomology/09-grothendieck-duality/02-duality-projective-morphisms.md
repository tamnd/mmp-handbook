---
title: Duality for projective morphisms
nodes: []
sources: [Har66, Har77, Stacks]
reads_with: [Har66:ch3, Har77:III.7]
requires: [P2.8, P4.2, P4.4, P4.7, P4.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Duality for projective morphisms

### Statement

Let $k$ be a field. In this section a *projective scheme* is a closed subscheme of some $\mathbb{P}^m_k$, and $\omega^\bullet_X$ is the dualizing complex of Proposition P4.9.7 for a chosen embedding. Write $\mathbb{D}_X = R\mathcal{H}om_{\mathcal{O}_X}(-, \omega^\bullet_X)$, and $H^i(X, K)$ for the hypercohomology of a complex $K$, the cohomology of $R\Gamma(X, K)$. For a vector space $V$ write $V^\vee = \operatorname{Hom}_k(V, k)$.

**Theorem P4.9.11 (Serre duality for complexes).** Let $X$ be a projective scheme.

1. For every $K \in D^b_{coh}(X)$ and every $i$ there is an isomorphism, natural in $K$ and compatible with the connecting maps of triangles,
$$\operatorname{Ext}^{-i}_X(K, \omega^\bullet_X) = H^{-i}(R\operatorname{Hom}_X(K, \omega^\bullet_X)) \cong H^i(X, K)^\vee.$$
2. In particular $H^{-i}(X, \omega^\bullet_X) \cong H^i(X, \mathcal{O}_X)^\vee$, and the element of $H^0(X, \omega^\bullet_X)^\vee \cong H^0(X, \mathcal{O}_X)$ corresponding to $1$ is the *trace* $t_X \colon H^0(X, \omega^\bullet_X) \to k$.
3. The pair $(\omega^\bullet_X, t_X)$ does not depend on the embedding: for two embeddings there is a unique isomorphism of the two dualizing complexes compatible with the traces.

Lean: not in Lean as stated.

**Definition P4.9.12 (trace and upper shriek).** Let $f \colon X \to Y$ be a morphism of projective schemes. The *trace* of $f$ is the map
$$\operatorname{Tr}_f \colon Rf_* \omega^\bullet_X \to \omega^\bullet_Y$$
that corresponds under Theorem P4.9.11 on $Y$ to $t_X \in H^0(Y, Rf_* \omega^\bullet_X)^\vee = H^0(X, \omega^\bullet_X)^\vee$. For $G \in D^b_{coh}(Y)$, set
$$f^! G = \mathbb{D}_X L f^* \mathbb{D}_Y G \in D^+_{coh}(X).$$

**Theorem P4.9.13 (duality for a morphism of projective schemes).** Let $f \colon X \to Y$ be a morphism of projective schemes.

1. For $K \in D^b_{coh}(X)$ the map
$$\phi_K \colon Rf_* \mathbb{D}_X K \to \mathbb{D}_Y Rf_* K,$$
adjoint to $Rf_* \mathbb{D}_X K \otimes^L Rf_* K \to Rf_*(\mathbb{D}_X K \otimes^L K) \to Rf_* \omega^\bullet_X \xrightarrow{\operatorname{Tr}_f} \omega^\bullet_Y$, is an isomorphism.
2. $f^! \omega^\bullet_Y \cong \omega^\bullet_X$, and the trace $\operatorname{Tr}_f$ is the counit of the adjunction in part 3 at $\omega^\bullet_Y$.
3. For $K \in D^b_{coh}(X)$ and $G \in D^b_{coh}(Y)$ such that $\mathbb{D}_Y G$ is perfect, that is, locally isomorphic to a bounded complex of free modules of finite rank, there is an isomorphism
$$Rf_* R\mathcal{H}om_X(K, f^! G) \cong R\mathcal{H}om_Y(Rf_* K, G),$$
and in particular $\operatorname{Hom}_X(K, f^! G) \cong \operatorname{Hom}_Y(Rf_* K, G)$. This applies to $G = \omega^\bullet_Y$ and, when $Y$ is smooth, to every $G$.
4. If $X$ is smooth over $k$ and equidimensional of dimension $n$, then $\omega^\bullet_X \cong \omega_X[n]$ with $\omega_X = \Omega^n_{X/k}$, and $Rf_* R\mathcal{H}om_X(K, \omega_X[n]) \cong \mathbb{D}_Y Rf_* K$.

Lean: not in Lean as stated.

The statements are local on $Y$, and they extend to an open subscheme $U$ of a projective scheme: set $\omega^\bullet_U = \omega^\bullet_X|_U$, which is again a dualizing complex. For a projective morphism $f \colon X' \to U$ to such a $U$, choose a closure $\bar{f} \colon \bar{X}' \to X$ of $f$, a morphism of projective schemes with $\bar{f}^{-1}(U) = X'$, and restrict Theorem P4.9.13 for $\bar{f}$ to $U$. Such a closure exists: $X' \subseteq \mathbb{P}^r \times U$ is closed, and its closure in $\mathbb{P}^r \times X$ works. The result does not depend on the closure, because $Rf_*$ and $\mathbb{D}$ commute with restriction to open sets.

**Corollary P4.9.14 (finite morphisms).** Let $f \colon X \to Y$ be a finite morphism of projective schemes. Then $f_*$ is exact, and $f_* f^! G \cong R\mathcal{H}om_{\mathcal{O}_Y}(f_* \mathcal{O}_X, G)$ for $G \in D^b_{coh}(Y)$. In particular $f_* \omega^\bullet_X \cong R\mathcal{H}om_{\mathcal{O}_Y}(f_* \mathcal{O}_X, \omega^\bullet_Y)$.

Lean: not in Lean as stated.

### Proof in words

On a projective scheme $X \subseteq P$, the dualizing complex is $R\mathcal{H}om_P(\mathcal{O}_X, \omega_P)[m]$, and the adjunction of a closed immersion reduces $\operatorname{Hom}$ into it to $\operatorname{Hom}$ into $\omega_P[m]$ on $P$. Serre duality on $P$ (Theorem P4.7.8) then gives Serre duality on $X$, first for sheaves and then for bounded complexes by induction on their length. This duality characterizes $\omega^\bullet_X$ by a universal property, so it does not depend on the embedding. For a morphism $f$, both sides of $Rf_* \mathbb{D}_X K \to \mathbb{D}_Y Rf_* K$ have the same hypercohomology after any twist, because each is dual to the cohomology of $K$ twisted the other way. A map of coherent complexes that is an isomorphism on hypercohomology after every large twist is an isomorphism. The adjunction for $f^!$ follows by formal manipulation of $\mathbb{D}_X$ and $\mathbb{D}_Y$, which are anti-equivalences.

### Examples

**Example P4.9.15 (the trace of projective space).** For $X = P = \mathbb{P}^m_k$ itself, $\omega^\bullet_P = \omega_P[m]$, and $t_P$ is the trace of Section P4.7.2, the map $H^m(P, \omega_P) \to k$ sending the class of $(x_0 \cdots x_m)^{-1}$ to $1$. For a point $x \colon \operatorname{Spec} k \to P$, Corollary P4.9.14 gives $x^! \omega^\bullet_P = R\mathcal{H}om_P(k(x), \omega_P)[m]$, which is $k[0]$ by the Koszul computation, as Example P4.7.13 found by other means.

**Example P4.9.16 (a hyperelliptic curve).** Let $k$ have characteristic not $2$ and $f \colon C \to \mathbb{P}^1_k$ be a double cover branched over $2g + 2$ points, from a smooth projective curve of genus $g$. Then $f_* \mathcal{O}_C = \mathcal{O} \oplus \mathcal{O}(-g-1)$. By Corollary P4.9.14 and part 4 of Theorem P4.9.13,
$$f_* \omega_C = \mathcal{H}om(\mathcal{O} \oplus \mathcal{O}(-g-1), \mathcal{O}(-2)) = \mathcal{O}(-2) \oplus \mathcal{O}(g - 1),$$
so $h^0(C, \omega_C) = h^0(\mathbb{P}^1, \mathcal{O}(g - 1)) = g$, as Serre duality on $C$ requires.

**Example P4.9.17 (the blow-up of a point of the plane).** Let $f \colon Y \to X = \mathbb{P}^2_k$ be the blow-up of a $k$-point, with exceptional curve $E$. By Proposition P4.4.16, $Rf_* \mathcal{O}_Y = \mathcal{O}_X$. Part 1 of Theorem P4.9.13 with $K = \mathcal{O}_Y$ gives
$$Rf_* \omega_Y[2] = Rf_* \mathbb{D}_Y \mathcal{O}_Y \cong \mathbb{D}_X Rf_* \mathcal{O}_Y = \omega_X[2].$$
So $f_* \omega_Y = \omega_X$ and $R^1 f_* \omega_Y = 0$. Since $\omega_Y = f^* \omega_X \otimes \mathcal{O}_Y(E)$, this is the statement $f_* \mathcal{O}_Y(E) = \mathcal{O}_X$, $R^1 f_* \mathcal{O}_Y(E) = 0$ of Example P4.4.19, by the projection formula.

### Proof

*Theorem P4.9.11, part 1.* Let $i \colon X \to P = \mathbb{P}^m_k$ be the embedding. By the adjunction of Proposition P2.8.23,
$$R\operatorname{Hom}_X(K, \omega^\bullet_X) = R\operatorname{Hom}_X(K, i^\flat \omega_P[m]) \cong R\operatorname{Hom}_P(i_* K, \omega_P[m]),$$
and $H^i(X, K) = H^i(P, i_* K)$ since $i_*$ is exact. So it suffices to prove $\operatorname{Ext}^{m-i}_P(L, \omega_P) \cong H^i(P, L)^\vee$ for $L \in D^b_{coh}(P)$. For a coherent sheaf $L$ this is Theorem P4.7.8. Both sides are cohomological functors of $L$ that turn triangles into long exact sequences, and the isomorphisms of Theorem P4.7.8 are compatible with connecting maps. For a complex $L$ with cohomology in an interval of length $\ell > 0$, the truncation triangle $\tau_{\leq a} L \to L \to \tau_{> a} L \to$ splits $L$ into two complexes of smaller length, and the five lemma gives the isomorphism for $L$. Naturality of the construction gives the naturality of the isomorphism.

*Part 2* is part 1 with $K = \mathcal{O}_X$.

*Part 3.* Let $(\omega', t')$ be the pair from a second embedding. By part 1 for $\omega'$, the map $\operatorname{Hom}_X(\omega^\bullet_X, \omega') \to H^0(X, \omega^\bullet_X)^\vee$, $\alpha \mapsto t' \circ H^0(\alpha)$, is an isomorphism, so there is a unique $\alpha$ with $t' \circ H^0(\alpha) = t_X$. By part 1 for both complexes, $\alpha$ induces isomorphisms $\operatorname{Hom}_X(K, \omega^\bullet_X[j]) \to \operatorname{Hom}_X(K, \omega'[j])$ for all $K$ and $j$, since both are identified with $H^{-j}(X, K)^\vee$ compatibly with $\alpha$. With $K = \omega'$, Yoneda's lemma shows that $\alpha$ is an isomorphism.

*Theorem P4.9.13, part 1.* First, a criterion. Let $\mathcal{O}_Y(1)$ be the very ample sheaf of the embedding of $Y$. If $C \in D^b_{coh}(Y)$ and $H^i(Y, C(q)) = 0$ for all $i$ and all $q \gg 0$, then $C = 0$. Indeed, let $j$ be the largest degree with $\mathcal{H}^j(C) \neq 0$. For $q$ large, every $\mathcal{H}^p(C)(q)$ has no higher cohomology and $\mathcal{H}^j(C)(q)$ has a nonzero global section, by Theorem P4.2.7. The hypercohomology spectral sequence $H^a(Y, \mathcal{H}^b(C)(q)) \Rightarrow H^{a+b}(Y, C(q))$ then degenerates, and $H^j(Y, C(q)) = H^0(Y, \mathcal{H}^j(C)(q)) \neq 0$. So a map in $D^b_{coh}(Y)$ is an isomorphism if it induces isomorphisms on $H^i(Y, -(q))$ for all $i$ and $q \gg 0$: apply the criterion to its cone.

Both sides of $\phi_K$ are in $D^b_{coh}(Y)$, by Theorem P4.4.8 and Theorem P4.9.4. Fix $q$ and $i$. By the projection formula (Proposition P4.4.10, extended to complexes) and Theorem P4.9.11 on $X$,
$$H^{-i}(Y, (Rf_* \mathbb{D}_X K)(q)) = H^{-i}(X, \mathbb{D}_X(K \otimes f^* \mathcal{O}_Y(-q))) \cong H^{i}(X, K \otimes f^* \mathcal{O}_Y(-q))^\vee,$$
and by the projection formula and Theorem P4.9.11 on $Y$,
$$H^{-i}(Y, (\mathbb{D}_Y Rf_* K)(q)) = H^{-i}(Y, \mathbb{D}_Y((Rf_* K)(-q))) \cong H^i(Y, (Rf_* K)(-q))^\vee = H^i(X, K \otimes f^* \mathcal{O}_Y(-q))^\vee.$$
The isomorphism of Theorem P4.9.11 on $X$ is given by the trace $t_X$, and the one on $Y$ by $t_Y$. By Definition P4.9.12, $t_Y \circ H^0(\operatorname{Tr}_f) = t_X$, and from this a diagram chase shows that the map induced by $\phi_K$ on $H^{-i}(Y, -(q))$ is the composite of the two isomorphisms. So $\phi_K$ is an isomorphism by the criterion.

*Part 3.* Let $P = \mathbb{D}_Y G$, a perfect complex, so $G \cong \mathbb{D}_Y P$ and $L f^* P$ is perfect on $X$. For complexes $K$, $M$ there is the natural isomorphism $R\mathcal{H}om(K, \mathbb{D}_X M) = \mathbb{D}_X(K \otimes^L M)$. Hence
$$Rf_* R\mathcal{H}om_X(K, f^! G) = Rf_* \mathbb{D}_X(K \otimes^L Lf^* P) \cong \mathbb{D}_Y Rf_*(K \otimes^L Lf^* P) \cong \mathbb{D}_Y(Rf_* K \otimes^L P),$$
by part 1 and the projection formula for the perfect complex $P$. The last term is $R\mathcal{H}om_Y(Rf_* K, \mathbb{D}_Y P) = R\mathcal{H}om_Y(Rf_* K, G)$. Taking $H^0 R\Gamma(Y, -)$ gives the statement for $\operatorname{Hom}$. For $G = \omega^\bullet_Y$, $P = \mathcal{O}_Y$. If $Y$ is smooth, every coherent complex is perfect, because the local rings are regular (Theorem P1.9.21).

*Part 2.* With $G = \omega^\bullet_Y$, $\mathbb{D}_Y G = \mathcal{O}_Y$ by Definition P4.9.2, $L f^* \mathcal{O}_Y = \mathcal{O}_X$, and $f^! \omega^\bullet_Y = \mathbb{D}_X \mathcal{O}_X = \omega^\bullet_X$. Under the adjunction of part 3, the identity of $\omega^\bullet_X$ corresponds to a map $Rf_* \omega^\bullet_X \to \omega^\bullet_Y$, and unwinding the construction with $K = \mathcal{O}_X$ shows that it is $\operatorname{Tr}_f$.

*Part 4.* A smooth scheme is Cohen-Macaulay, so $\omega^\bullet_X \cong \omega^\circ_X[n]$ by Proposition P4.9.7, and $\omega^\circ_X \cong \Omega^n_{X/k}$ by Corollary P4.7.21 when $k$ is perfect. For general $k$ the same identification follows from Theorem P4.7.20, since a smooth scheme is a local complete intersection in $\mathbb{P}^m_k$. The formula is part 1.

*Corollary P4.9.14.* A finite morphism is affine, so $f_*$ is exact on quasi-coherent sheaves and $Rf_* = f_*$ (Corollary P4.4.3). Part 3 of Theorem P4.9.13 does not need $\mathbb{D}_Y G$ perfect here: for finite $f$, $f_*$ identifies $\mathcal{O}_X$-modules with $f_* \mathcal{O}_X$-modules, and $R\mathcal{H}om_{\mathcal{O}_Y}(f_* \mathcal{O}_X, -)$ is right adjoint to $f_*$ on derived categories, as for the closed immersions of Proposition P2.8.23. By part 1 of Theorem P4.9.13 with $K = \mathcal{O}_X$, $f_* \omega^\bullet_X = f_* \mathbb{D}_X \mathcal{O}_X \cong \mathbb{D}_Y f_* \mathcal{O}_X$, which is the last statement. The general statement follows in the same way from the uniqueness of right adjoints, applied on $D^b_{coh}$.

### Exercises

1. (A) Let $X = \mathbb{P}^1_k$ and $K = \mathcal{O}(a) \oplus \mathcal{O}(b)[1]$. Compute both sides of Theorem P4.9.11 for every $i$.
2. (A) Let $f \colon \mathbb{P}^1_k \to \mathbb{P}^1_k$ be $[s : t] \mapsto [s^d : t^d]$, with $d$ prime to the characteristic. Compute $f_* \mathcal{O}$ and $f_* \omega$, and check part 1 of Theorem P4.9.13 for $K = \mathcal{O}$.
3. (B) Let $X$ be a projective scheme, $j \colon U \to X$ an open subscheme and $Z = X \setminus U$. Show that $\omega^\bullet_U = j^* \omega^\bullet_X$ is a dualizing complex on $U$, and that $j^*$ is the functor $j^!$ in the sense of Theorem P2.8.22, part 2.
4. (B) Let $f \colon X \to Y$ be a morphism of smooth projective varieties of dimensions $n$ and $m$. Show that $f^! \mathcal{O}_Y = \omega_X \otimes f^* \omega_Y^{-1}[n - m]$, and compute $f^! \mathcal{O}_Y$ for the projection $\mathbb{P}^r \times Y \to Y$.
5. (B) Let $X \subseteq \mathbb{P}^m_k$ be a projective scheme and $\mathcal{F}$ a coherent sheaf on $X$. Use Theorem P4.9.11 and the hypercohomology spectral sequence to construct a spectral sequence $E_2^{p,q} = \operatorname{Ext}^p_X(\mathcal{F}, \mathcal{H}^q(\omega^\bullet_X)) \Rightarrow H^{-p-q}(X, \mathcal{F})^\vee$, and explain how it recovers the maps $\theta^i$ of Theorem P4.7.18.
6. (C) Let $f \colon Y \to X$ be a morphism of projective varieties with $Rf_* \mathcal{O}_Y = \mathcal{O}_X$. Show that $Rf_* \omega^\bullet_Y \cong \omega^\bullet_X$ via the trace, and deduce that $H^i(Y, \omega^\bullet_Y) \cong H^i(X, \omega^\bullet_X)$ for every $i$.

### Lean

Mathlib has the derived category of an abelian category and the cohomology of sheaves on a site, but not the coherent duality of schemes. The handbook adds no `MinimalModel` node here. The general form of Grothendieck duality is a black box of the handbook, listed in the table of P0, with Lean hypothesis not yet named.

### Notes and history

Grothendieck announced coherent duality at the 1958 International Congress, and Hartshorne's *Residues and duality* (1966) wrote it up, with the functor $f^!$ built from the dualizing complexes and the residue symbol; the projective case of Theorem P4.9.13 is Hartshorne's Chapter III. Deligne gave the definition of $f^!$ as a right adjoint, and Neeman proved its existence in general by Brown representability in 1996. Conrad's book of 2000 checks the compatibilities of the trace in detail, and Lipman's notes of 2009 give the modern account. The literature state is theorem. In the minimal model program duality is used through the formula $Rf_* \omega^\bullet_Y \cong \mathbb{D}_X Rf_* \mathcal{O}_Y$ for a resolution or a contraction, which converts statements about $Rf_* \mathcal{O}_Y$ into statements about $Rf_* \omega_Y$ and back.
