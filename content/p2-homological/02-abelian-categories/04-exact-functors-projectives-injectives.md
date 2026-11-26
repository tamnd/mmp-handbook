---
title: Exact functors, projective and injective objects
nodes: []
sources: [Wei94, Vak25, AM69]
reads_with: [Wei94:ch2, Vak25:ch1]
requires: [P1.1, P2.1, P2.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Exact functors, projective and injective objects

### Statement

Throughout, $\mathcal{A}$ and $\mathcal{B}$ are abelian categories and functors between them are additive.

**Definition P2.2.29 (exact functors).** A functor $F: \mathcal{A} \to \mathcal{B}$ is *left exact* if for every exact sequence $0 \to A \to B \to C$ the sequence $0 \to F(A) \to F(B) \to F(C)$ is exact. It is *right exact* if for every exact sequence $A \to B \to C \to 0$ the sequence $F(A) \to F(B) \to F(C) \to 0$ is exact. It is *exact* if it is both. A contravariant functor is left exact if it sends $A \to B \to C \to 0$ to $0 \to F(C) \to F(B) \to F(A)$.

Lean: Mathlib `CategoryTheory.Limits.PreservesFiniteLimits` (left exact) and `CategoryTheory.Limits.PreservesFiniteColimits` (right exact).

A left exact functor is one that preserves kernels: the sequence $0 \to A \to B \to C$ is exact exactly when $A$ is the kernel of $B \to C$. An additive functor preserves finite biproducts (Section 2.1). An additive functor that preserves kernels preserves all finite limits, since finite limits are built from finite products and kernels (Section 1.4). This is why Mathlib states left exactness as the preservation of finite limits. An exact functor sends every exact sequence to an exact sequence, since exactness at $B$ in $A \to B \to C$ is a statement about the kernel of $B \to C$ and the cokernel of $A \to B$.

**Proposition P2.2.30 (the basic exact functors).**

1. For every object $T$ the functor $\operatorname{Hom}(T, -): \mathcal{A} \to \mathsf{Ab}$ is left exact, and the contravariant functor $\operatorname{Hom}(-, T)$ is left exact.
2. A left adjoint is right exact and a right adjoint is left exact.
3. For an $A$-module $N$ the functor $- \otimes_A N$ is right exact. It is exact if and only if $N$ is flat.
4. Every additive functor sends a split short exact sequence to a split short exact sequence.

Lean: Mathlib `CategoryTheory.Adjunction.rightAdjoint_preservesLimits` and `CategoryTheory.Adjunction.leftAdjoint_preservesColimits` for 2, and `CategoryTheory.ShortComplex.Splitting.map` for 4 (proved in Mathlib).

*Proof.* For 1, a map $T \to A$ with zero composite to $C$ is, by the definition of a kernel, a unique map to the kernel. This is the exactness of $0 \to \operatorname{Hom}(T, A) \to \operatorname{Hom}(T, B) \to \operatorname{Hom}(T, C)$ when $A = \ker(B \to C)$. The contravariant case is the dual. For 2, a left adjoint preserves all colimits by Section 1.4, in particular cokernels, and a right adjoint preserves kernels. Statement 3 is the corollary of Section 1.4, and the second half is the definition of flatness in P1 Ch. 1. For 4, a split sequence is isomorphic to $0 \to A \to A \oplus C \to C \to 0$, and it is described by the equations of a biproduct, which an additive functor keeps. $\square$

**Definition P2.2.31 (projective and injective objects).** An object $P$ is *projective* if $\operatorname{Hom}(P, -)$ is exact. Equivalently, for every epimorphism $g: B \to C$ and every map $u: P \to C$ there is a map $v: P \to B$ with $g v = u$. An object $I$ is *injective* if $\operatorname{Hom}(-, I)$ is exact. Equivalently, for every monomorphism $f: A \to B$ and every map $u: A \to I$ there is $v: B \to I$ with $v f = u$. The category $\mathcal{A}$ has *enough projectives* if every object is a quotient of a projective object, and *enough injectives* if every object is a subobject of an injective object.

Lean: Mathlib `CategoryTheory.Projective`, `CategoryTheory.Injective`, `CategoryTheory.EnoughProjectives` and `CategoryTheory.EnoughInjectives`; for modules, `Module.Projective` and `Module.Injective`.

The equivalence of the two forms holds because $\operatorname{Hom}(P, -)$ is left exact by the proposition, so its exactness is the surjectivity of $\operatorname{Hom}(P, B) \to \operatorname{Hom}(P, C)$ for every epimorphism $B \to C$. A short exact sequence $0 \to A \to B \to P \to 0$ with $P$ projective splits: lift $1_P$ to $B$. Dually, a short exact sequence that starts with an injective object splits.

**Proposition P2.2.32 (projective modules).** An $A$-module is projective if and only if it is a direct summand of a free module. The category $\mathsf{Mod}_A$ has enough projectives.

Lean: Mathlib `Module.Projective.of_free`, `Module.Projective.of_split` and `Module.projective_lifting_property` (proved in Mathlib).

*Proof.* A free module $A^{(S)}$ is projective: to lift $u: A^{(S)} \to C$ along an onto map $B \to C$, lift the image of each basis vector and extend linearly. A direct summand of a projective module is projective, since a lift for $P \oplus Q$ restricts to a lift for $P$. Conversely, let $P$ be projective and choose a surjection $A^{(S)} \to P$, for example with $S = P$. The sequence $0 \to K \to A^{(S)} \to P \to 0$ splits since $P$ is projective, so $P$ is a direct summand of $A^{(S)}$. The same surjection shows that every module is a quotient of a free module, hence of a projective one. $\square$

**Theorem P2.2.33 (Baer's criterion).** An $A$-module $I$ is injective if and only if for every ideal $J \subseteq A$, every linear map $J \to I$ extends to a linear map $A \to I$.

Lean: Mathlib `Module.Baer` (the condition) and `Module.Baer.injective` (proved in Mathlib).

**Corollary P2.2.34 (injective abelian groups).** Let $A$ be a principal ideal domain. An $A$-module $D$ is injective if and only if it is *divisible*: for every $d \in D$ and every $a \neq 0$ in $A$ there is $e \in D$ with $a e = d$. In particular $\mathbb{Q}$ and $\mathbb{Q}/\mathbb{Z}$ are injective abelian groups.

Lean: Mathlib `Module.Baer.of_divisible` and `AddCommGrpCat.injective_of_divisible` (proved in Mathlib, for abelian groups).

**Theorem P2.2.35 (enough injectives).** The category $\mathsf{Mod}_A$ has enough injectives.

Lean: Mathlib `ModuleCat.enoughInjectives` (proved in Mathlib).

### Proof in words

Projective modules are easy to find, since free modules are projective. Injective modules are harder, and they are what sheaf cohomology needs, because the category of sheaves has enough injectives but in general not enough projectives (Chapter 7). Baer's criterion reduces the extension problem for all submodules to the extension problem for ideals. Its proof extends a map one element at a time and uses Zorn's lemma to reach the whole module. For a principal ideal domain the criterion becomes divisibility, so $\mathbb{Q}/\mathbb{Z}$ is injective. Then every abelian group sits inside a divisible group, and the adjunction between restriction and coextension of scalars from Section 1.3 moves the injective abelian group $D$ to the injective $A$-module $\operatorname{Hom}_{\mathbb{Z}}(A, D)$.

### Examples

**Example P2.2.36 (projective and not projective).** The $\mathbb{Z}$-module $\mathbb{Z}/n$, $n \geq 2$, is not projective: the sequence $0 \to \mathbb{Z} \xrightarrow{n} \mathbb{Z} \to \mathbb{Z}/n \to 0$ does not split, since $\mathbb{Z}$ has no torsion. The module $\mathbb{Q}$ is flat over $\mathbb{Z}$ (P1 Ch. 1) but not projective: a projective $\mathbb{Z}$-module is a summand of a free module, so it has no nonzero element divisible by every integer, while $\mathbb{Q}$ is divisible. Over $A = \mathbb{Z}/6 = \mathbb{Z}/2 \times \mathbb{Z}/3$ the module $\mathbb{Z}/2$ is projective but not free, since $A = \mathbb{Z}/2 \oplus \mathbb{Z}/3$. In geometry the projective modules over $A$ are the vector bundles on $\operatorname{Spec} A$ (P3 Ch. 5), and $\mathbb{Z}/2$ is the bundle of rank $1$ on one of the two points of $\operatorname{Spec} \mathbb{Z}/6$ and of rank $0$ on the other.

**Example P2.2.37 ($\mathbb{Z}$ is not injective).** Let $J = 2\mathbb{Z}$ and let $u: 2\mathbb{Z} \to \mathbb{Z}$ send $2$ to $1$. An extension $v: \mathbb{Z} \to \mathbb{Z}$ would satisfy $2 v(1) = v(2) = 1$, which has no solution. So Baer's condition fails, and $\mathbb{Z}$ is not injective, as the corollary predicts since $\mathbb{Z}$ is not divisible. The embedding of the theorem replaces $\mathbb{Z}$ by $\mathbb{Q}$, and $0 \to \mathbb{Z} \to \mathbb{Q} \to \mathbb{Q}/\mathbb{Z} \to 0$ is an *injective resolution* of $\mathbb{Z}$ of length one. Chapter 3 computes derived functors with such resolutions.

**Example P2.2.38 (Hom is not right exact).** Apply $\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/2, -)$ to $0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z} \to \mathbb{Z}/2 \to 0$. The result is $0 \to 0 \to 0 \to \mathbb{Z}/2$, which is not exact on the right. Apply $\operatorname{Hom}_{\mathbb{Z}}(-, \mathbb{Z})$ to the same sequence: it gives $0 \to 0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z}$, again not onto at the end. The missing cokernels are $\operatorname{Ext}^1$ groups, computed in Chapter 3.

### Proof

*Proof of Baer's criterion.* An injective module has the property, since $J \to A$ is injective. Conversely, assume the property. Let $f: M \to N$ be injective and $u: M \to I$. Identify $M$ with $f(M) \subseteq N$. Consider pairs $(M', u')$ with $M \subseteq M' \subseteq N$ and $u': M' \to I$ extending $u$, ordered by extension. Every chain has an upper bound, the union of the submodules with the map defined on the union. By Zorn's lemma there is a maximal pair $(M', u')$. Suppose $M' \neq N$ and pick $x \in N \setminus M'$. Let $J = \{a \in A : a x \in M'\}$, an ideal. The map $J \to I$, $a \mapsto u'(a x)$, is linear, so it extends to $g: A \to I$. Define $u''$ on $M' + A x$ by $u''(m + a x) = u'(m) + a\, g(1)$. It is well defined: if $m + a x = 0$, then $a \in J$ and $a x = -m$, so $a\, g(1) = g(a) = u'(a x) = -u'(m)$. So $(M' + A x, u'')$ is a larger pair, a contradiction. So $M' = N$. $\square$

*Proof of the corollary.* If $D$ is injective, $d \in D$ and $a \neq 0$, the map $(a) \to D$, $a \mapsto d$, is well defined since $A$ is a domain, and an extension $v: A \to D$ gives $e = v(1)$ with $a e = d$. Conversely, let $D$ be divisible, and let $u: J \to D$ with $J = (a)$. If $a = 0$ the zero map extends $u$. Otherwise pick $e$ with $a e = u(a)$ and set $v(1) = e$. By Baer's criterion $D$ is injective. A quotient of a divisible group is divisible, so $\mathbb{Q}/\mathbb{Z}$ is injective. $\square$

*Proof of the theorem.* Step 1: every abelian group $M$ embeds in a divisible group. Write $M = \mathbb{Z}^{(S)}/K$. Then $M \subseteq \mathbb{Q}^{(S)}/K$, and $\mathbb{Q}^{(S)}/K$ is divisible since $\mathbb{Q}^{(S)}$ is.

Step 2: if $D$ is an injective abelian group, then $\operatorname{Hom}_{\mathbb{Z}}(A, D)$ is an injective $A$-module, with $(a \varphi)(b) = \varphi(b a)$. By the adjunction between restriction of scalars and coextension of scalars (Section 1.3, Exercise 4, for the ring map $\mathbb{Z} \to A$),
$$\operatorname{Hom}_A(N, \operatorname{Hom}_{\mathbb{Z}}(A, D)) \cong \operatorname{Hom}_{\mathbb{Z}}(N, D), \quad \psi \mapsto (n \mapsto \psi(n)(1)),$$
naturally in $N$. The right side is an exact functor of $N$, since $D$ is injective. So the left side is exact, and $\operatorname{Hom}_{\mathbb{Z}}(A, D)$ is injective.

Step 3: let $M$ be an $A$-module. By Step 1 there is an injective group map $\varphi: M \to D$ with $D$ divisible, hence injective by the corollary. Define $\iota: M \to \operatorname{Hom}_{\mathbb{Z}}(A, D)$ by $\iota(m)(a) = \varphi(a m)$. It is $A$-linear: $\iota(b m)(a) = \varphi(a b m) = \iota(m)(a b) = (b\, \iota(m))(a)$. It is injective, since $\iota(m)(1) = \varphi(m)$. By Step 2 its target is injective. $\square$

### Exercises

1. (A) Show that a direct sum of projective modules is projective and that a product of injective modules is injective.
2. (A) Show that the functor $\mathsf{Mod}_A \to \mathsf{Mod}_{S^{-1}A}$, $M \mapsto S^{-1}M$, is exact, and that it sends projective modules to projective modules.
3. (A) Show that an exact functor sends exact sequences of any length to exact sequences, and that a left exact functor need not.
4. (B) Let $k$ be a field and $A = k[x]/(x^2)$. Show that $A$ is an injective $A$-module, with Baer's criterion. Show that the module $k = A/(x)$ is neither projective nor injective.
5. (B) Show that the category of finite abelian groups has no nonzero projective objects and no nonzero injective objects. (Hint: a direct summand of a projective or injective object is projective or injective. A nonzero finite abelian group has a summand $\mathbb{Z}/p^k$ with $k \geq 1$. Use the surjection $\mathbb{Z}/p^{k+1} \to \mathbb{Z}/p^k$ and the injection $\mathbb{Z}/p^k \to \mathbb{Z}/p^{k+1}$.)
6. (B) Let $A$ be a Noetherian ring. Show that a direct sum of injective $A$-modules is injective. (Hint: an ideal is finitely generated, so a map from an ideal to a direct sum lands in a finite sum.)
7. (B) Let $f: A \to B$ be a ring map and $I$ an injective $A$-module. Show that $\operatorname{Hom}_A(B, I)$ is an injective $B$-module. Show that if $B$ is flat over $A$ then restriction of scalars sends injective $B$-modules to injective $A$-modules.
8. (C) Show that the functor $\mathsf{Mod}_A \to \mathsf{Ab}$, $M \mapsto \operatorname{Hom}_{\mathbb{Z}}(M, \mathbb{Q}/\mathbb{Z})$, is exact and faithful, and that a sequence of $A$-modules is exact if and only if its image is exact. Deduce that $N$ is flat if and only if $\operatorname{Hom}_{\mathbb{Z}}(N, \mathbb{Q}/\mathbb{Z})$ is an injective $A$-module.

### Lean

Left and right exactness are `PreservesFiniteLimits` and `PreservesFiniteColimits`. Projective and injective objects are `CategoryTheory.Projective` and `CategoryTheory.Injective`, with `EnoughProjectives` and `EnoughInjectives`. For modules Mathlib has `Module.Projective`, `Module.Injective`, Baer's criterion `Module.Baer.injective` and its converse `Module.Baer.iff_injective`, and the divisible case `Module.Baer.of_divisible`. The existence of enough injectives is `ModuleCat.enoughInjectives`. Mathlib proves it with the character module $\operatorname{Hom}_{\mathbb{Z}}(M, \mathbb{Q}/\mathbb{Z})$ of Exercise 8, which is also the tool of the flatness criterion of P1 Ch. 1. The handbook adds no `MinimalModel` node here.

### Notes and history

Baer proved his criterion in 1940, and he proved that every module embeds in an injective one. Projective modules were named by Cartan and Eilenberg in their book of 1956, which built homological algebra on projective and injective resolutions. Eckmann and Schopf proved in 1953 that every module has an injective hull, a minimal injective extension. Every statement here is classical.
