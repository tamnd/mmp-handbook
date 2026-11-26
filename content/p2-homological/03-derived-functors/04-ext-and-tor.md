---
title: Ext and Tor
nodes: []
sources: [Wei94, Har77, AM69]
reads_with: [Wei94:ch3, Har77:ch3]
requires: [P1.1, P2.2, P2.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Ext and Tor

### Statement

Throughout, $A$ is a commutative ring and modules are $A$-modules. By Section 2.4 the category $\mathsf{Mod}_A$ has enough projectives and enough injectives.

**Definition P2.3.29 (Ext and Tor).** For modules $M$ and $N$ and $i \geq 0$, let
$$\operatorname{Ext}^i_A(M, N) = R^i \operatorname{Hom}_A(M, -)(N), \qquad \operatorname{Tor}_i^A(M, N) = L_i(M \otimes_A -)(N).$$
So $\operatorname{Ext}^i_A(M, N)$ is the cohomology of $\operatorname{Hom}_A(M, I^\bullet)$ for an injective resolution $N \to I^\bullet$, and $\operatorname{Tor}_i^A(M, N)$ is the homology of $M \otimes_A P_\bullet$ for a projective resolution $P_\bullet \to N$. Both are $A$-modules, since $A$ is commutative. For an abelian category $\mathcal{A}$ with enough injectives, $\operatorname{Ext}^i(X, Y) = R^i \operatorname{Hom}(X, -)(Y)$ is defined in the same way.

Lean: Mathlib `CategoryTheory.Abelian.Ext` and `CategoryTheory.Tor`.

By Section 3.2, $\operatorname{Ext}^0(M, N) = \operatorname{Hom}(M, N)$ and $\operatorname{Tor}_0(M, N) = M \otimes N$, and each short exact sequence in $N$ gives a long exact sequence of $\operatorname{Ext}$ and of $\operatorname{Tor}$.

**Theorem P2.3.30 (balance of Ext).** Let $P_\bullet \to M$ be a projective resolution. Then there are isomorphisms
$$\operatorname{Ext}^i_A(M, N) \cong H^i(\operatorname{Hom}_A(P_\bullet, N)),$$
natural in $N$ and compatible with the connecting maps. As a consequence, $\operatorname{Ext}^i(M, N) = 0$ for $i > 0$ if $M$ is projective or $N$ is injective, and each short exact sequence $0 \to M' \to M \to M'' \to 0$ gives a long exact sequence
$$0 \to \operatorname{Hom}(M'', N) \to \operatorname{Hom}(M, N) \to \operatorname{Hom}(M', N) \to \operatorname{Ext}^1(M'', N) \to \operatorname{Ext}^1(M, N) \to \cdots.$$

Lean: Mathlib `CategoryTheory.Abelian.Ext.covariantSequence_exact`, `CategoryTheory.Abelian.Ext.contravariantSequence_exact`, `CategoryTheory.Abelian.Ext.eq_zero_of_projective` and `CategoryTheory.Abelian.Ext.eq_zero_of_injective` (proved in Mathlib, for `Abelian.Ext`).

**Theorem P2.3.31 (balance of Tor).** Let $Q_\bullet \to M$ be a resolution of $M$ by flat modules. Then there are isomorphisms
$$\operatorname{Tor}_i^A(M, N) \cong H_i(Q_\bullet \otimes_A N),$$
natural in $N$ and compatible with the connecting maps. As a consequence, $\operatorname{Tor}_i(M, N) \cong \operatorname{Tor}_i(N, M)$; $\operatorname{Tor}_i(M, N) = 0$ for $i > 0$ if $M$ or $N$ is flat; and $\operatorname{Tor}_i(-, N)$ is a homological $\delta$-functor in the first variable that commutes with filtered colimits.

Lean: Mathlib `CategoryTheory.Tor`, `CategoryTheory.Tor'` and `CategoryTheory.isZero_Tor_succ_of_projective` (the vanishing, proved in Mathlib).

**Theorem P2.3.32 (flatness and Tor).** For a module $N$ the following are equivalent.

1. $N$ is flat.
2. $\operatorname{Tor}_i(M, N) = 0$ for every module $M$ and every $i > 0$.
3. $\operatorname{Tor}_1(M, N) = 0$ for every module $M$.
4. $\operatorname{Tor}_1(A/I, N) = 0$ for every finitely generated ideal $I$.
5. For every finitely generated ideal $I$ the map $I \otimes N \to N$ is injective.

In particular this proves the ideal criterion of P1 Ch. 1.

Lean: Mathlib `Module.Flat.iff_rTensor_injective'` for the equivalence of 1 and 5 (proved in Mathlib, with character modules).

**Proposition P2.3.33 (a nonzerodivisor).** Let $f \in A$ be a nonzerodivisor and $N$ a module, and write $N[f] = \{n \in N : f n = 0\}$. Then $\operatorname{Tor}_0(A/f, N) = N/fN$, $\operatorname{Tor}_1(A/f, N) \cong N[f]$, $\operatorname{Ext}^0(A/f, N) \cong N[f]$, $\operatorname{Ext}^1(A/f, N) \cong N/fN$, and all higher $\operatorname{Tor}_i$ and $\operatorname{Ext}^i$ vanish.

Lean: not in Lean as stated.

*Proof.* The sequence $0 \to A \xrightarrow{f} A \to A/f \to 0$ is a free resolution of $A/f$. Tensoring with $N$ gives the complex $N \xrightarrow{f} N$ in degrees $1$ and $0$, and $\operatorname{Hom}(-, N)$ gives $N \xrightarrow{f} N$ in degrees $0$ and $1$. Their kernels and cokernels are $N[f]$ and $N/fN$. The two balance theorems identify these with $\operatorname{Tor}$ and $\operatorname{Ext}$. $\square$

**Proposition P2.3.34 (Ext$^1$ and extensions).** An *extension* of $C$ by $B$ is a short exact sequence $0 \to B \to E \to C \to 0$. Two extensions are *equivalent* if there is a map $E \to E'$ that restricts to $1_B$ and induces $1_C$; such a map is an isomorphism by the short five lemma. Send an extension to $\delta(1_B) \in \operatorname{Ext}^1(C, B)$, where $\delta: \operatorname{Hom}(B, B) \to \operatorname{Ext}^1(C, B)$ is the connecting map of the long exact sequence of $\operatorname{Hom}(-, B)$. This is a bijection from the set of equivalence classes of extensions to $\operatorname{Ext}^1(C, B)$. The split extension $B \oplus C$ goes to $0$.

Lean: Mathlib `CategoryTheory.ShortComplex.ShortExact.extClass`, the class of an extension.

*Proof.* The class $\delta(1_B)$ depends only on the equivalence class, by naturality of $\delta$. By exactness of $\operatorname{Hom}(E, B) \to \operatorname{Hom}(B, B) \xrightarrow{\delta} \operatorname{Ext}^1(C, B)$, the class is $0$ if and only if $1_B$ extends to a map $E \to B$, that is, if and only if the extension splits. The proof of bijectivity uses a projective presentation $0 \to K \to P \to C \to 0$. The balance theorem gives $\operatorname{Ext}^1(C, B) = \operatorname{coker}(\operatorname{Hom}(P, B) \to \operatorname{Hom}(K, B))$. The inverse map sends the class of $\varphi: K \to B$ to the pushout of $0 \to K \to P \to C \to 0$ along $\varphi$. The check that the two maps are inverse is a diagram chase. See Weibel, Chapter 3. $\square$

### Proof in words

$\operatorname{Ext}$ is defined by resolving the second variable by injectives, and $\operatorname{Tor}$ by resolving the second variable by projectives. Balance says that the first variable may be resolved instead. The proof is Grothendieck's theorem of Section 3.3: resolving the first variable also gives a $\delta$-functor in the second variable, it agrees with $\operatorname{Hom}$ or $\otimes$ in degree $0$, and it vanishes on injective or projective objects. So it is the universal $\delta$-functor. For $\operatorname{Tor}$ the same argument works with flat resolutions, because tensoring with a flat module is exact. The flatness criterion then follows from the long exact sequence of $\operatorname{Tor}$ in the first variable: the vanishing of $\operatorname{Tor}_1(A/I, N)$ for ideals passes to all finitely generated modules by induction on the number of generators, and to all modules by filtered colimits.

### Examples

**Example P2.3.35 (Ext and Tor of cyclic groups).** Over $\mathbb{Z}$, with $n \geq 2$, the proposition on a nonzerodivisor gives $\operatorname{Ext}^1(\mathbb{Z}/n, \mathbb{Z}) \cong \mathbb{Z}/n$ and $\operatorname{Hom}(\mathbb{Z}/n, \mathbb{Z}) = 0$, as in the first example of Section 3.2. It gives $\operatorname{Tor}_1(\mathbb{Z}/n, N) \cong N[n]$ and $\operatorname{Ext}^1(\mathbb{Z}/n, N) \cong N/nN$. Since $\mathbb{Z}$ is a principal ideal domain, every submodule of a free module is free, so every module has a free resolution of length $1$, and $\operatorname{Ext}^i_{\mathbb{Z}}$ and $\operatorname{Tor}_i^{\mathbb{Z}}$ vanish for $i \geq 2$. For $N = \mathbb{Z}/p$ and $n = p$ prime, $\operatorname{Ext}^1(\mathbb{Z}/p, \mathbb{Z}/p) \cong \mathbb{Z}/p$. Its $p$ elements are the split extension $\mathbb{Z}/p \oplus \mathbb{Z}/p$ and the $p - 1$ extensions $0 \to \mathbb{Z}/p \xrightarrow{a p} \mathbb{Z}/p^2 \to \mathbb{Z}/p \to 0$, $a = 1, \dots, p - 1$. These $p - 1$ extensions have isomorphic middle terms but are not equivalent (Exercise 6). So $\operatorname{Ext}^1$ classifies extensions up to equivalence, and not middle terms up to isomorphism.

**Example P2.3.36 (Tor and intersection multiplicity).** Let $A = k[x, y]$, $f = y$ and $g = y - x^2$. The curves $f = 0$ and $g = 0$ are a line and a parabola, tangent at the origin. By the proposition, $\operatorname{Tor}_1(A/f, A/g) \cong (A/g)[f]$. In $A/g \cong k[x]$ the element $y$ acts as $x^2$, a nonzerodivisor, so $\operatorname{Tor}_1 = 0$, and $\operatorname{Tor}_0 = A/(y, y - x^2) \cong k[x]/(x^2)$ has dimension $2$. Serre's formula defines the intersection multiplicity of two subvarieties at a point as the alternating sum $\sum_i (-1)^i \operatorname{length} \operatorname{Tor}_i$ of the local rings. For two curves on a smooth surface with no common component, only $\operatorname{Tor}_0$ survives, and the multiplicity here is $2$, as expected for a tangency. The higher $\operatorname{Tor}$ terms matter for subvarieties that do not meet properly or are not Cohen-Macaulay. The intersection numbers of curves and divisors (P5 Ch. 5, P7 Ch. 1) agree with this definition.

**Example P2.3.37 (the conormal module).** For an ideal $I$ the long exact sequence of $0 \to I \to A \to A/I \to 0$, tensored with $A/I$, gives $\operatorname{Tor}_1(A/I, A/I) \cong I/I^2$ (Exercise 3). For an effective Cartier divisor $D$ on a variety $X$, with ideal sheaf $\mathcal{O}_X(-D)$, this is the conormal sheaf $\mathcal{O}_D(-D)$. The adjunction formula $K_D = (K_X + D)|_D$, used in Volume 1 and in the base point free theorem of Volume 7, comes from this conormal sheaf and the conormal sequence of P3 Ch. 12.

### Proof

*Proof of the balance of Ext.* Let $T^i(N) = H^i(\operatorname{Hom}(P_\bullet, N))$. A short exact sequence $0 \to N' \to N \to N'' \to 0$ gives a sequence of complexes $0 \to \operatorname{Hom}(P_\bullet, N') \to \operatorname{Hom}(P_\bullet, N) \to \operatorname{Hom}(P_\bullet, N'') \to 0$, which is exact since each $P_n$ is projective. By Section 3.1 it has a long exact sequence of cohomology, natural in the short exact sequence. So $(T^i)$ is a $\delta$-functor. In degree $0$, the sequence $P_1 \to P_0 \to M \to 0$ is exact and $\operatorname{Hom}(-, N)$ is left exact, so $T^0(N) = \ker(\operatorname{Hom}(P_0, N) \to \operatorname{Hom}(P_1, N)) \cong \operatorname{Hom}(M, N)$. If $N$ is injective, $\operatorname{Hom}(-, N)$ is exact. It sends the exact complex $\cdots \to P_1 \to P_0 \to M \to 0$ to an exact complex, so $T^i(N) = 0$ for $i > 0$. Every module embeds in an injective module, so $(T^i)$ is effaceable. By Grothendieck's theorem (Section 3.3) it is universal, and so is $(\operatorname{Ext}^i(M, -))$. Both start with $\operatorname{Hom}(M, -)$, so they are isomorphic as $\delta$-functors.

For the consequences: if $M$ is projective, take $P_\bullet = M$ in degree $0$. If $N$ is injective, $\operatorname{Ext}^i(M, N) = R^i \operatorname{Hom}(M, -)(N) = 0$ by Section 3.2. For the long exact sequence in the first variable, take projective resolutions of $M'$ and $M''$ and combine them with the horseshoe lemma for projective resolutions, the dual of the lemma of Section 3.2. This gives a short exact sequence of projective resolutions, split in each degree. Applying $\operatorname{Hom}(-, N)$ keeps it exact, and Section 3.1 gives the long exact sequence. $\square$

*Proof of the balance of Tor.* Let $T_i(N) = H_i(Q_\bullet \otimes N)$. Each $Q_n$ is flat, so a short exact sequence in $N$ gives a short exact sequence of complexes $0 \to Q_\bullet \otimes N' \to Q_\bullet \otimes N \to Q_\bullet \otimes N'' \to 0$, and $(T_i)$ is a homological $\delta$-functor. In degree $0$, right exactness of $\otimes$ gives $T_0(N) = \operatorname{coker}(Q_1 \otimes N \to Q_0 \otimes N) \cong M \otimes N$. If $N$ is projective, it is flat (P1 Ch. 1), so $- \otimes N$ is exact and $Q_\bullet \otimes N$ is exact in positive degrees: $T_i(N) = 0$ for $i > 0$. Every module is a quotient of a projective module, so the dual of Grothendieck's theorem shows that $(T_i)$ is universal. So $T_i \cong \operatorname{Tor}_i(M, -)$.

For the consequences: take $Q_\bullet$ a projective resolution of $M$. Then $H_i(Q_\bullet \otimes N)$ is by definition $\operatorname{Tor}_i(N, M)$, up to the symmetry of the tensor product, so $\operatorname{Tor}_i(M, N) \cong \operatorname{Tor}_i(N, M)$. If $M$ is flat, take $Q_\bullet = M$ in degree $0$. If $N$ is flat, $Q_\bullet \otimes N$ is exact in positive degrees, as above. For the first variable, fix a projective resolution $P_\bullet \to N$. Then $\operatorname{Tor}_i(M, N) = H_i(M \otimes P_\bullet)$ by definition. Each $P_n$ is flat, so $M \mapsto H_i(M \otimes P_\bullet)$ is a homological $\delta$-functor in $M$, by Section 3.1. The functor $M \mapsto M \otimes P_n$ commutes with all colimits, being a left adjoint (Section 1.3), and filtered colimits of modules are exact (Section 1.4), so they commute with homology. $\square$

*Proof of the flatness theorem.* The implication from 1 to 2 is the balance of $\operatorname{Tor}$. The implications from 2 to 3 and from 3 to 4 are clear. For 3 implies 1: let $0 \to M' \to M \to M'' \to 0$ be exact. The long exact sequence in the first variable gives $\operatorname{Tor}_1(M'', N) \to M' \otimes N \to M \otimes N$, and the first term is $0$. So $M' \otimes N \to M \otimes N$ is injective. Every injective map $M' \to M$ is the first map of such a sequence, so $N$ is flat.

For 4 if and only if 5: the long exact sequence of $0 \to I \to A \to A/I \to 0$ reads $\operatorname{Tor}_1(A, N) \to \operatorname{Tor}_1(A/I, N) \to I \otimes N \to A \otimes N = N$. The first term is $0$ since $A$ is free. So $\operatorname{Tor}_1(A/I, N)$ is the kernel of $I \otimes N \to N$.

For 4 implies 3, in three steps. First, every ideal $I$ is the filtered union of its finitely generated subideals $I_\lambda$, so $A/I = \operatorname{colim} A/I_\lambda$ is a filtered colimit, and $\operatorname{Tor}_1(A/I, N) = \operatorname{colim} \operatorname{Tor}_1(A/I_\lambda, N) = 0$. Second, let $M$ be generated by $m_1, \dots, m_r$, and argue by induction on $r$. The case $r = 0$ is clear. Let $M'$ be the submodule generated by $m_1, \dots, m_{r-1}$. Then $M/M'$ is generated by one element, so $M/M' \cong A/I$ for an ideal $I$. The exact sequence $\operatorname{Tor}_1(M', N) \to \operatorname{Tor}_1(M, N) \to \operatorname{Tor}_1(A/I, N)$ has outer terms $0$, by induction and by the first step. So $\operatorname{Tor}_1(M, N) = 0$. Third, every module is the filtered union of its finitely generated submodules, and $\operatorname{Tor}_1(-, N)$ commutes with filtered colimits. $\square$

### Exercises

1. (A) Let $m, n \geq 1$ and $d = \gcd(m, n)$. Show that $\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/m, \mathbb{Z}/n)$, $\operatorname{Ext}^1_{\mathbb{Z}}(\mathbb{Z}/m, \mathbb{Z}/n)$, $\mathbb{Z}/m \otimes \mathbb{Z}/n$ and $\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/m, \mathbb{Z}/n)$ are all isomorphic to $\mathbb{Z}/d$. Compare with Section 3.2, Exercise 3.
2. (A) Let $A$ be a principal ideal domain. Show that $\operatorname{Ext}^i_A$ and $\operatorname{Tor}_i^A$ vanish for $i \geq 2$, and that $\operatorname{Tor}_1^A(M, N)$ is torsion for all $M$, $N$.
3. (A) Let $I, J$ be ideals of $A$. Show that $\operatorname{Tor}_1(A/I, A/J) \cong (I \cap J)/IJ$. Deduce that $\operatorname{Tor}_1(A/I, A/I) \cong I/I^2$, and that $\operatorname{Tor}_1^{k[x, y]}(k[x, y]/(x), k[x, y]/(y)) = 0$.
4. (B) Let $S \subseteq A$ be multiplicative. Show that $S^{-1} \operatorname{Tor}_i^A(M, N) \cong \operatorname{Tor}_i^{S^{-1}A}(S^{-1}M, S^{-1}N)$. Show that if $A$ is Noetherian and $M$ is finitely generated, then $S^{-1} \operatorname{Ext}^i_A(M, N) \cong \operatorname{Ext}^i_{S^{-1}A}(S^{-1}M, S^{-1}N)$. (Hint: resolve $M$ by finitely generated free modules. This is the local nature of the $\mathcal{E}xt$ sheaves of P4 Ch. 8.)
5. (B) Let $k$ be a field, $A = k[x, y]$, and $f, g \in A$ with no common factor. Show that $g$ is a nonzerodivisor on $A/f$, that $\operatorname{Tor}_i(A/f, A/g) = 0$ for $i \geq 1$, and compute $\dim_k \operatorname{Tor}_0$ for $f = y$, $g = y - x^3$.
6. (B) Let $p$ be a prime. For $a \in \{1, \dots, p - 1\}$ let $E_a$ be the extension $0 \to \mathbb{Z}/p \xrightarrow{a p} \mathbb{Z}/p^2 \to \mathbb{Z}/p \to 0$, with the reduction map on the right. Show that $E_a$ and $E_b$ are equivalent only if $a = b$, and compute the class of $E_a$ in $\operatorname{Ext}^1(\mathbb{Z}/p, \mathbb{Z}/p) \cong \mathbb{Z}/p$.
7. (C) Show that $\operatorname{Ext}^1_{\mathbb{Z}}(\mathbb{Q}, \mathbb{Z}) \neq 0$, although $\mathbb{Q}$ is flat. (Hint: the long exact sequence of $0 \to \mathbb{Z} \to \mathbb{Q} \to \mathbb{Q}/\mathbb{Z} \to 0$ gives $\operatorname{Ext}^1(\mathbb{Q}, \mathbb{Z}) \cong \operatorname{coker}(\operatorname{Hom}(\mathbb{Q}, \mathbb{Q}) \to \operatorname{Hom}(\mathbb{Q}, \mathbb{Q}/\mathbb{Z}))$. Write $\mathbb{Q}$ as the union of the groups $\frac{1}{n!}\mathbb{Z}$ and show that $\operatorname{Hom}(\mathbb{Q}, \mathbb{Q}/\mathbb{Z})$ is uncountable.)
8. (C) Let $G$ be a cyclic group of order $m$ with generator $t$, and $N = 1 + t + \cdots + t^{m-1}$ in $\mathbb{Z}[G]$. Show that $\cdots \xrightarrow{N} \mathbb{Z}[G] \xrightarrow{t - 1} \mathbb{Z}[G] \xrightarrow{N} \mathbb{Z}[G] \xrightarrow{t - 1} \mathbb{Z}[G] \to \mathbb{Z} \to 0$ is a free resolution of $\mathbb{Z}$ with the trivial action. Deduce that the group cohomology $H^i(G, \mathbb{Z}) = \operatorname{Ext}^i_{\mathbb{Z}[G]}(\mathbb{Z}, \mathbb{Z})$ is $\mathbb{Z}$ for $i = 0$, $0$ for $i$ odd and $\mathbb{Z}/m$ for $i > 0$ even. (The ring $\mathbb{Z}[G]$ is commutative, so the definitions above apply.)

### Lean

Mathlib has two constructions of $\operatorname{Ext}$. The functor `Ext R C n` in `Mathlib/CategoryTheory/Abelian/Ext.lean` derives $\operatorname{Hom}$ in the first variable with projective resolutions. The groups `CategoryTheory.Abelian.Ext X Y n` in `Mathlib/Algebra/Homology/DerivedCategory/Ext` are morphisms in the derived category of Chapter 8, with composition, the two long exact sequences `Abelian.Ext.covariantSequence_exact` and `Abelian.Ext.contravariantSequence_exact`, and the vanishing `Abelian.Ext.eq_zero_of_projective` and `Abelian.Ext.eq_zero_of_injective`. The class of an extension is `ShortComplex.ShortExact.extClass`. $\operatorname{Tor}$ is `CategoryTheory.Tor` in a monoidal abelian category, with `Tor'` the version derived in the other variable; the isomorphism of the two is the balance theorem, which Mathlib does not yet prove. The flatness criterion is `Module.Flat.iff_rTensor_injective'`. The handbook adds no `MinimalModel` node here.

### Notes and history

$\operatorname{Ext}$ first appeared in Eilenberg and Mac Lane's work of 1942 on group extensions and the universal coefficient theorem, which is where the name comes from. $\operatorname{Tor}$, from *torsion*, appeared in the Künneth formula. Cartan and Eilenberg's book of 1956 defined both as derived functors and proved the balance theorems. Serre gave the $\operatorname{Tor}$ formula for intersection multiplicities in his course *Algèbre locale, multiplicités* of 1957 and 1958.
