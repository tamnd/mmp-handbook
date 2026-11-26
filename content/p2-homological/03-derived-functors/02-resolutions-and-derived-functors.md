---
title: Resolutions and derived functors
nodes: []
sources: [Wei94, Har77]
reads_with: [Wei94:ch2, Har77:ch3]
requires: [P2.2, P2.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Resolutions and derived functors

### Statement

Throughout, $\mathcal{A}$ and $\mathcal{B}$ are abelian categories and $F: \mathcal{A} \to \mathcal{B}$ is an additive functor.

**Definition P2.3.9 (resolutions).** An *injective resolution* of an object $A$ is a complex $I^\bullet$ with $I^n = 0$ for $n < 0$, each $I^n$ injective, and a map $\varepsilon: A \to I^0$ such that the augmented sequence $0 \to A \xrightarrow{\varepsilon} I^0 \to I^1 \to I^2 \to \cdots$ is exact. Equivalently, $\varepsilon$ is a quasi-isomorphism from $A$, seen as a complex in degree $0$, to $I^\bullet$. A *projective resolution* of $A$ is dually an exact sequence $\cdots \to P_2 \to P_1 \to P_0 \to A \to 0$ with each $P_n$ projective.

Lean: Mathlib `CategoryTheory.InjectiveResolution` and `CategoryTheory.ProjectiveResolution`.

**Proposition P2.3.10 (existence of resolutions).** If $\mathcal{A}$ has enough injectives, every object has an injective resolution. If $\mathcal{A}$ has enough projectives, every object has a projective resolution.

Lean: Mathlib `CategoryTheory.InjectiveResolution.of` and `CategoryTheory.ProjectiveResolution.of` (proved in Mathlib).

*Proof.* Choose a monomorphism $\varepsilon: A \to I^0$ with $I^0$ injective. Let $C^0 = \operatorname{coker} \varepsilon$, choose a monomorphism $C^0 \to I^1$ with $I^1$ injective, and let $d^0$ be the composite $I^0 \to C^0 \to I^1$. Continue with $C^1 = \operatorname{coker} d^0$. At each step the kernel of $d^n$ is the kernel of $I^n \to C^n$, since $C^n \to I^{n+1}$ is a monomorphism, and that is the image of $d^{n-1}$. So the sequence is exact. The projective case is dual. $\square$

**Theorem P2.3.11 (comparison theorem).** Let $f: A \to B$ be a map. Let $0 \to A \to E^\bullet$ be an exact augmented complex, with $E^n = 0$ for $n < 0$, and let $0 \to B \to I^\bullet$ be an augmented complex with each $I^n$ injective. Then there is a map of complexes $\tilde{f}: E^\bullet \to I^\bullet$ that is compatible with $f$ and the augmentations. Any two such maps are homotopic.

Lean: Mathlib `CategoryTheory.InjectiveResolution.desc` and `CategoryTheory.InjectiveResolution.descHomotopy` (proved in Mathlib, for two injective resolutions).

**Corollary P2.3.12 (uniqueness of resolutions).** Any two injective resolutions $I^\bullet$, $J^\bullet$ of $A$ are homotopy equivalent, by a homotopy equivalence compatible with the augmentations and unique up to homotopy.

Lean: Mathlib `CategoryTheory.InjectiveResolution.homotopyEquiv` (proved in Mathlib).

*Proof.* The comparison theorem gives maps $u: I^\bullet \to J^\bullet$ and $v: J^\bullet \to I^\bullet$ over $1_A$. Then $v u$ and $1_I$ are both maps $I^\bullet \to I^\bullet$ over $1_A$, so $v u \simeq 1_I$ by the uniqueness part. In the same way $u v \simeq 1_J$. $\square$

**Definition P2.3.13 (derived functors).** Let $\mathcal{A}$ have enough injectives and let $F$ be left exact. For each object $A$ choose an injective resolution $A \to I^\bullet_A$. The *right derived functors* of $F$ are
$$R^i F(A) = H^i(F(I^\bullet_A)), \quad i \geq 0.$$
For a map $f: A \to B$, let $R^i F(f) = H^i(F(\tilde{f}))$ for a lift $\tilde{f}: I^\bullet_A \to I^\bullet_B$ given by the comparison theorem. Dually, if $\mathcal{A}$ has enough projectives and $F$ is right exact, the *left derived functors* are $L_i F(A) = H_i(F(P_\bullet))$ for a projective resolution $P_\bullet \to A$. For a contravariant functor the same construction uses projective resolutions to define right derived functors and injective resolutions to define left derived functors.

Lean: Mathlib `CategoryTheory.Functor.rightDerived` and `CategoryTheory.Functor.leftDerived`, with `CategoryTheory.InjectiveResolution.isoRightDerivedObj`, which computes $R^i F(A)$ from any injective resolution.

**Proposition P2.3.14 (basic properties).** Let $\mathcal{A}$ have enough injectives and let $F$ be left exact.

1. Each $R^i F$ is a well defined additive functor. A different choice of resolutions gives isomorphic functors, by a unique natural isomorphism compatible with the constructions.
2. $R^0 F \cong F$.
3. If $I$ is injective, then $R^i F(I) = 0$ for $i > 0$.
4. If $F$ is exact, then $R^i F = 0$ for $i > 0$.

Lean: Mathlib `CategoryTheory.Functor.rightDerivedZeroIsoSelf` for 2 and `CategoryTheory.Functor.isZero_rightDerived_obj_injective_succ` for 3 (proved in Mathlib).

*Proof.* For 1: a lift $\tilde{f}$ is unique up to homotopy, $F$ sends homotopies to homotopies, and homotopic maps agree on cohomology (Section 3.1). So $R^i F(f)$ does not depend on the lift. The lift of a composite is homotopic to the composite of lifts, and the lift of $f + g$ is homotopic to the sum of lifts, by the uniqueness part. So $R^i F$ is an additive functor. For two choices of resolutions, the homotopy equivalences of the corollary give the natural isomorphism. For 2: $F$ is left exact and $0 \to A \to I^0 \to I^1$ is exact, so $0 \to F(A) \to F(I^0) \to F(I^1)$ is exact, and $H^0(F(I^\bullet)) = \ker(F(I^0) \to F(I^1)) \cong F(A)$. For 3: the complex $I$ in degree $0$ is an injective resolution of $I$. For 4: $F$ sends the exact sequence $0 \to A \to I^\bullet$ to an exact sequence, so $H^i(F(I^\bullet)) = 0$ for $i > 0$. $\square$

**Theorem P2.3.15 (long exact sequence of derived functors).** Let $\mathcal{A}$ have enough injectives, let $F$ be left exact, and let $0 \to A' \to A \to A'' \to 0$ be exact. There are maps $\delta^i: R^i F(A'') \to R^{i+1} F(A')$ such that the sequence
$$0 \to F(A') \to F(A) \to F(A'') \xrightarrow{\delta^0} R^1 F(A') \to R^1 F(A) \to R^1 F(A'') \xrightarrow{\delta^1} R^2 F(A') \to \cdots$$
is exact. The maps $\delta^i$ are natural for maps of short exact sequences.

Lean: not in Lean as stated for `Functor.rightDerived`. Mathlib has the long exact sequences of `CategoryTheory.Abelian.Ext`, Section 3.4.

The proof rests on the following lemma.

**Lemma P2.3.16 (horseshoe lemma).** Let $0 \to A' \to A \to A'' \to 0$ be exact, and let $I'^\bullet$ and $I''^\bullet$ be injective resolutions of $A'$ and $A''$. Then $A$ has an injective resolution $I^\bullet$ with $I^n = I'^n \oplus I''^n$, such that the inclusions and projections form a short exact sequence of complexes $0 \to I'^\bullet \to I^\bullet \to I''^\bullet \to 0$ over the given sequence.

Lean: not in Lean as stated.

### Proof in words

An injective resolution replaces an object by a complex of injective objects with the same cohomology. Injective objects are the objects on which every left exact functor behaves as an exact functor, in the sense that $\operatorname{Hom}(-, I)$ is exact. So $F$ applied to the resolution is a complex whose cohomology measures how far $F$ is from exact. The comparison theorem says that the resolution is unique up to homotopy, so the cohomology does not depend on the choice. The construction uses only that the target consists of injective objects and that the source is exact: each map extends along a monomorphism, one degree at a time. For the long exact sequence, the horseshoe lemma resolves the three terms of a short exact sequence compatibly, with direct sums in each degree. The additive functor $F$ keeps these split sequences exact, and the long exact sequence of Section 3.1 does the rest.

### Examples

**Example P2.3.17 (derived functors of $\operatorname{Hom}(\mathbb{Z}/n, -)$).** Let $F = \operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/n, -)$ on abelian groups, with $n \geq 2$. An injective resolution of $\mathbb{Z}$ is $0 \to \mathbb{Z} \to \mathbb{Q} \to \mathbb{Q}/\mathbb{Z} \to 0$, by Section 2.4. Apply $F$: since $\operatorname{Hom}(\mathbb{Z}/n, \mathbb{Q}) = 0$ and $\operatorname{Hom}(\mathbb{Z}/n, \mathbb{Q}/\mathbb{Z}) \cong \mathbb{Z}/n$, the complex $F(I^\bullet)$ is $0 \to \mathbb{Z}/n$ in degrees $0$ and $1$. So $R^0 F(\mathbb{Z}) = 0$, $R^1 F(\mathbb{Z}) \cong \mathbb{Z}/n$ and $R^i F(\mathbb{Z}) = 0$ for $i \geq 2$. Section 3.4 names these groups $\operatorname{Ext}^i(\mathbb{Z}/n, \mathbb{Z})$.

**Example P2.3.18 (left derived functors of the tensor product).** Let $F = - \otimes_{\mathbb{Z}} M$, right exact. A projective resolution of $\mathbb{Z}/n$ is $0 \to \mathbb{Z} \xrightarrow{n} \mathbb{Z} \to \mathbb{Z}/n \to 0$. Applying $F$ gives the complex $M \xrightarrow{n} M$ in degrees $1$ and $0$. So $L_0 F(\mathbb{Z}/n) = M/nM$, $L_1 F(\mathbb{Z}/n) = M[n] = \{m \in M : n m = 0\}$ and $L_i F(\mathbb{Z}/n) = 0$ for $i \geq 2$. These are the groups $\operatorname{Tor}_i(\mathbb{Z}/n, M)$ of Section 3.4. The long exact sequence for $0 \to \mathbb{Z} \to \mathbb{Q} \to \mathbb{Q}/\mathbb{Z} \to 0$ then gives $L_1 F(\mathbb{Q}/\mathbb{Z}) = \ker(M \to \mathbb{Q} \otimes M)$, the torsion subgroup of $M$, once Section 3.4 shows that $L_1 F(\mathbb{Q}) = 0$ because $\mathbb{Q}$ is flat.

**Example P2.3.19 (sheaf cohomology, a preview).** For a topological space $X$, Chapter 7 shows that the sheaves of abelian groups on $X$ form an abelian category with enough injectives, and that the global sections functor $\Gamma(X, -)$ is left exact. Its derived functors are the sheaf cohomology groups $H^i(X, \mathcal{F}) = R^i \Gamma(X, \mathcal{F})$. The long exact sequence of the theorem, for $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$, is the long exact sequence of cohomology used throughout the minimal model program. For a morphism $f: X \to Y$ the derived functors of $f_*$ are the higher direct images $R^i f_*$ of P4 Ch. 4.

### Proof

*Proof of the comparison theorem.* Write $E^{-1} = A$, $I^{-1} = B$, $f^{-1} = f$, and let $d^{-1}$ be the augmentations. Suppose $f^{-1}, \dots, f^n$ are constructed, with $d_I f^{k} = f^{k+1} d_E$ for $k < n$. The map $d_I^n f^n: E^n \to I^{n+1}$ vanishes on the image of $d_E^{n-1}$, since $d_I^n f^n d_E^{n-1} = d_I^n d_I^{n-1} f^{n-1} = 0$. For $n = -1$ use $E^{-2} = 0$. So $d_I^n f^n$ factors through $E^n/\operatorname{im} d_E^{n-1}$. By exactness of $E$ at $E^n$, the map $d_E^n$ induces a monomorphism $E^n / \operatorname{im} d_E^{n-1} \to E^{n+1}$. Since $I^{n+1}$ is injective, the map extends along it to $f^{n+1}: E^{n+1} \to I^{n+1}$ with $f^{n+1} d_E^n = d_I^n f^n$.

For uniqueness, the difference of two lifts is a lift $g$ of $0$, so it is enough to show that such a $g$ is null homotopic. Construct $h^{n}: E^{n} \to I^{n-1}$ with $g^n = d_I^{n-1} h^n + h^{n+1} d_E^n$ for all $n \geq -1$, starting with $h^{-1} = 0$ and $h^0 = 0$ (the maps into $I^{-2} = 0$ and $I^{-1} = B$). The equation in degree $-1$ holds since $g^{-1} = 0$. Suppose $h^{n}$ and $h^{n+1}$ are constructed and the equation holds in degree $n$. Consider $u = g^{n+1} - d_I^n h^{n+1}: E^{n+1} \to I^{n+1}$. On the image of $d_E^n$,
$$u\, d_E^n = d_I^n g^n - d_I^n h^{n+1} d_E^n = d_I^n (g^n - h^{n+1} d_E^n) = d_I^n d_I^{n-1} h^n = 0.$$
So $u$ factors through $E^{n+1}/\operatorname{im} d_E^n$, which embeds in $E^{n+2}$. Since $I^{n+1}$ is injective, there is $h^{n+2}: E^{n+2} \to I^{n+1}$ with $h^{n+2} d_E^{n+1} = u$. This is the equation in degree $n+1$. In degrees $n \geq 0$ these equations say that $g \simeq 0$ as maps of complexes. $\square$

*Proof of the horseshoe lemma.* Write $i: A' \to A$ and $p: A \to A''$, and let $\varepsilon': A' \to I'^0$ and $\varepsilon'': A'' \to I''^0$ be the augmentations. Since $I'^0$ is injective and $i$ is a monomorphism, there is $\alpha: A \to I'^0$ with $\alpha i = \varepsilon'$. Let $\varepsilon = (\alpha, \varepsilon'' p): A \to I'^0 \oplus I''^0$. Then the diagram with rows $0 \to A' \to A \to A'' \to 0$ and $0 \to I'^0 \to I'^0 \oplus I''^0 \to I''^0 \to 0$ and vertical maps $\varepsilon', \varepsilon, \varepsilon''$ commutes. The snake lemma gives an exact sequence $0 \to \ker \varepsilon' \to \ker \varepsilon \to \ker \varepsilon'' \to \operatorname{coker} \varepsilon' \to \operatorname{coker} \varepsilon \to \operatorname{coker} \varepsilon'' \to 0$. The outer kernels are $0$, so $\varepsilon$ is a monomorphism, and $0 \to \operatorname{coker} \varepsilon' \to \operatorname{coker} \varepsilon \to \operatorname{coker} \varepsilon'' \to 0$ is exact. The cokernels of $\varepsilon'$ and $\varepsilon''$ embed in $I'^1$ and $I''^1$, by exactness of the resolutions. Repeat the construction with this new short exact sequence and the resolutions $I'^{\geq 1}$ and $I''^{\geq 1}$ of the two cokernels. By induction this builds the differentials of $I^\bullet$. Each $I^n$ is a direct sum of two injectives, so it is injective. The resulting complex is exact by construction, and the inclusions and projections commute with the differentials, since the differential has the triangular form $\begin{pmatrix} d' & * \\ 0 & d'' \end{pmatrix}$. $\square$

*Proof of the theorem.* Choose injective resolutions $I'^\bullet$ and $I''^\bullet$ of $A'$ and $A''$, and let $I^\bullet$ be the resolution of $A$ from the horseshoe lemma. The sequence $0 \to I'^n \to I^n \to I''^n \to 0$ is split in each degree. An additive functor keeps split exact sequences (Section 2.4), so $0 \to F(I'^\bullet) \to F(I^\bullet) \to F(I''^\bullet) \to 0$ is a short exact sequence of complexes. Its long exact sequence of cohomology (Section 3.1) is the sequence of the theorem, with $R^0 F = F$. Naturality follows from the naturality in Section 3.1 together with the comparison theorem, which lifts a map of short exact sequences to a map of horseshoe resolutions up to homotopy. The details of this last step are in Weibel, Chapter 2. $\square$

### Exercises

1. (A) Show that $R^i F(A \oplus B) \cong R^i F(A) \oplus R^i F(B)$.
2. (A) Let $F$ be left exact and suppose $R^1 F(A) = 0$ for every $A$. Show that $F$ is exact.
3. (A) Let $m, n \geq 1$. Use the injective resolution $0 \to \mathbb{Z}/m \to \mathbb{Q}/\mathbb{Z} \xrightarrow{m} \mathbb{Q}/\mathbb{Z} \to 0$ to show that the right derived functors of $\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/n, -)$ at $\mathbb{Z}/m$ are $\mathbb{Z}/\gcd(m, n)$ in degrees $0$ and $1$, and $0$ in higher degrees.
4. (B) *Dimension shifting.* Let $0 \to A \to I \to C \to 0$ be exact with $I$ injective. Show that $R^1 F(A) \cong \operatorname{coker}(F(I) \to F(C))$ and that $R^{i+1} F(A) \cong R^i F(C)$ for $i \geq 1$.
5. (B) Let $A$ be any object and $F = \operatorname{Hom}(A, -)$. Show that $A$ is projective if and only if $R^1 F(B) = 0$ for every $B$.
6. (B) Show that a bounded below exact complex of injective objects is contractible. (Hint: split off the first term and induct.)
7. (C) Let $k$ be a field and $A = k[x]/(x^2)$. Show that $0 \to k \to A \xrightarrow{x} A \xrightarrow{x} A \to \cdots$ is an injective resolution of the $A$-module $k$, using Section 2.4, Exercise 4. Deduce that the right derived functors of $\operatorname{Hom}_A(k, -)$ at $k$ are $k$ in every degree $i \geq 0$.

### Lean

Mathlib has injective and projective resolutions as `InjectiveResolution` and `ProjectiveResolution`, their existence `InjectiveResolution.of`, the comparison maps `InjectiveResolution.desc` with the homotopies `descHomotopy`, and the homotopy equivalence `InjectiveResolution.homotopyEquiv` between two resolutions. Derived functors are `Functor.rightDerived` and `Functor.leftDerived`. Mathlib defines them as the composite of an injective resolution functor into the homotopy category with cohomology, `Functor.rightDerivedToHomotopyCategory`, which is the proof of part 1 of the proposition. The identification $R^0 F \cong F$ is `Functor.rightDerivedZeroIsoSelf`. The long exact sequence for `rightDerived` is not yet in Mathlib; the long exact sequences of `Abelian.Ext` are. The handbook adds no `MinimalModel` node here.

### Notes and history

Derived functors were defined by Cartan and Eilenberg in *Homological algebra* (1956), with projective and injective resolutions of modules. The horseshoe lemma has its name from the shape of its diagram. Grothendieck's Tohoku paper of 1957 extended the construction to abelian categories with enough injectives, so that it applies to sheaves, and this is the setting of Hartshorne, Chapter III.
