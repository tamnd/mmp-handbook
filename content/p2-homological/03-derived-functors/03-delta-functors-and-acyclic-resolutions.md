---
title: Delta functors and acyclic resolutions
nodes: []
sources: [Gro57, Wei94, Har77]
reads_with: [Gro57:ch2, Wei94:ch2, Har77:ch3]
requires: [P2.2, P2.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Delta functors and acyclic resolutions

### Statement

Throughout, $\mathcal{A}$ and $\mathcal{B}$ are abelian categories.

**Definition P2.3.20 ($\delta$-functor).** A *cohomological $\delta$-functor* $T$ from $\mathcal{A}$ to $\mathcal{B}$ is a family of additive functors $T^i: \mathcal{A} \to \mathcal{B}$, $i \geq 0$, together with, for each short exact sequence $0 \to A' \to A \to A'' \to 0$ and each $i \geq 0$, a map $\delta^i: T^i(A'') \to T^{i+1}(A')$, such that two conditions hold.

1. The sequence $0 \to T^0(A') \to T^0(A) \to T^0(A'') \xrightarrow{\delta^0} T^1(A') \to T^1(A) \to \cdots$ is exact.
2. The maps $\delta^i$ are natural: a map of short exact sequences gives commutative squares $T^{i+1}(\alpha') \delta^i = \delta^i T^i(\alpha'')$.

A *morphism* $\varphi: T \to S$ of $\delta$-functors is a family of natural transformations $\varphi^i: T^i \to S^i$ that commute with the maps $\delta^i$. The $\delta$-functor $T$ is *universal* if for every $\delta$-functor $S$ and every natural transformation $\varphi^0: T^0 \to S^0$ there is a unique morphism $\varphi: T \to S$ that extends $\varphi^0$.

Lean: not in Lean as stated.

Condition 1 says that $T^0$ is left exact. Two universal $\delta$-functors $T$ and $S$ with $T^0 \cong S^0$ are isomorphic, by a unique isomorphism that extends the given one: the extensions of the isomorphism and of its inverse compose to extensions of the identities, and these are the identities by uniqueness. By Section 3.2, if $\mathcal{A}$ has enough injectives and $F$ is left exact, then $(R^i F)_{i \geq 0}$ is a $\delta$-functor with $R^0 F = F$.

**Definition P2.3.21 (effaceable).** A $\delta$-functor $T$ is *effaceable* if every object $A$ has a monomorphism $A \to M$ with $T^i(M) = 0$ for all $i > 0$.

**Theorem P2.3.22 (Grothendieck).** An effaceable $\delta$-functor is universal.

Lean: not in Lean as stated.

**Corollary P2.3.23 (derived functors are universal).** Let $\mathcal{A}$ have enough injectives and let $F$ be left exact. Then $(R^i F)$ is a universal $\delta$-functor. Every effaceable $\delta$-functor $T$ with $T^0 \cong F$ is isomorphic to $(R^i F)$.

Lean: not in Lean as stated.

*Proof.* Every object embeds in an injective object $I$, and $R^i F(I) = 0$ for $i > 0$ by Section 3.2. So $(R^i F)$ is effaceable, and the theorem applies. The second statement follows from the uniqueness of universal $\delta$-functors. $\square$

**Definition P2.3.24 (acyclic object).** Let $F: \mathcal{A} \to \mathcal{B}$ be left exact, with $\mathcal{A}$ having enough injectives. An object $J$ is *$F$-acyclic* if $R^i F(J) = 0$ for all $i > 0$. An *$F$-acyclic resolution* of $A$ is an exact sequence $0 \to A \to J^0 \to J^1 \to \cdots$ with each $J^n$ $F$-acyclic.

**Theorem P2.3.25 (acyclic resolutions compute derived functors).** Let $0 \to A \to J^\bullet$ be an $F$-acyclic resolution. Then there are isomorphisms $R^i F(A) \cong H^i(F(J^\bullet))$ for all $i \geq 0$.

Lean: not in Lean as stated.

The isomorphisms are natural, in the sense that a map of $F$-acyclic resolutions over a map $A \to B$ gives a commutative square (Weibel, Chapter 2). The dual statements hold for homological $\delta$-functors $(T_i)$, with maps $\delta_i: T_i(A'') \to T_{i-1}(A')$, for left derived functors, and for resolutions $\cdots \to Q_1 \to Q_0 \to A \to 0$ by $F$-acyclic objects for a right exact $F$.

### Proof in words

A $\delta$-functor is a family of functors with long exact sequences. If every object $A$ sits in a short exact sequence $0 \to A \to M \to C \to 0$ with $T^i(M) = 0$, then the long exact sequence identifies $T^{i+1}(A)$ with a quotient of $T^i(C)$. So $T^{i+1}$ is determined by $T^i$, and by induction the whole family is determined by $T^0$. This is *dimension shifting*, and it gives the universal property: a map defined on $T^0$ has only one possible extension, and the long exact sequences show that the extension exists. For derived functors, injective objects efface. Any other class of acyclic objects works as well for computing $R^i F$, again by dimension shifting along the resolution. In Chapter 7 the flasque sheaves play this role for sheaf cohomology.

### Examples

**Example P2.3.26 (a $\delta$-functor that is not universal).** Let $F: \mathcal{A} \to \mathcal{B}$ be exact and nonzero. Put $T^0 = T^1 = F$ and $T^i = 0$ for $i \geq 2$, with all $\delta^i = 0$. The sequence $0 \to F(A') \to F(A) \to F(A'') \xrightarrow{0} F(A') \to F(A) \to F(A'') \to 0$ is exact, since $F$ is exact. So $T$ is a $\delta$-functor. It is not universal: the identity of $T^0$ extends to the morphisms $T \to T$ with $\varphi^1 = 1_F$ and with $\varphi^1 = 0$, and both commute with $\delta = 0$. The universal $\delta$-functor with $T^0 = F$ is $(F, 0, 0, \dots)$. It is effaceable, with $M = A$, and it equals $(R^i F)$ by part 4 of the proposition in Section 3.2.

**Example P2.3.27 (Tor of $\mathbb{Q}/\mathbb{Z}$ by a flat resolution).** Let $F = - \otimes_{\mathbb{Z}} M$. Section 3.4 shows that flat modules are $F$-acyclic. The sequence $0 \to \mathbb{Z} \to \mathbb{Q} \to \mathbb{Q}/\mathbb{Z} \to 0$ is a resolution of $\mathbb{Q}/\mathbb{Z}$ by flat modules, though $\mathbb{Q}$ is not projective. By the dual of the theorem, $L_i F(\mathbb{Q}/\mathbb{Z})$ is the homology of $M \to \mathbb{Q} \otimes M$, in degrees $1$ and $0$. So $L_1 F(\mathbb{Q}/\mathbb{Z})$ is the torsion subgroup of $M$, and $L_0 F(\mathbb{Q}/\mathbb{Z}) = \mathbb{Q}/\mathbb{Z} \otimes M$ is the cokernel of $M \to \mathbb{Q} \otimes M$.

**Example P2.3.28 (higher direct images by acyclic sheaves).** Chapter 7 proves that flasque sheaves are acyclic for $\Gamma(X, -)$, and P4 Ch. 1 proves that quasi-coherent sheaves on an affine scheme are acyclic. The theorem then computes sheaf cohomology with the Godement resolution by flasque sheaves, and, with Chapter 7, with Čech complexes for an affine cover. The corollary gives another route to the same groups: any effaceable $\delta$-functor that starts with $\Gamma(X, -)$ is sheaf cohomology. For $f: X \to Y$ and an exact functor $G$ of the target, $G \circ R^i f_*$ is the derived functor of $G \circ f_*$ by the corollary (Exercise 3). The base change statements of P4 Ch. 5 use these identifications.

### Proof

*Proof of Grothendieck's theorem.* Let $T$ be effaceable, $S$ a $\delta$-functor, and $\varphi^0: T^0 \to S^0$ a natural transformation. The construction of $\varphi^1$ is given in four steps. The same steps with the indices raised by $n$ construct $\varphi^{n+1}$ from $\varphi^n$.

Call a short exact sequence $\sigma: 0 \to A \to M \to C \to 0$ *effacing* if $T^i(M) = 0$ for $i > 0$. Effacing sequences exist for every $A$ by assumption.

Step 1: the map for one effacing sequence. For an effacing $\sigma$ the sequence $T^0(M) \to T^0(C) \xrightarrow{\delta_T} T^1(A) \to T^1(M) = 0$ is exact. So $\delta_T$ is an epimorphism with kernel the image of $T^0(M)$. The map $\delta_S \varphi^0_C: T^0(C) \to S^1(A)$ vanishes on that image, since $\delta_S \varphi^0_C T^0(M \to C) = \delta_S S^0(M \to C) \varphi^0_M = 0$. So there is a unique $\varphi^1_\sigma: T^1(A) \to S^1(A)$ with $\varphi^1_\sigma \delta_T = \delta_S \varphi^0_C$.

Step 2: compatibility with maps of effacing sequences. Let $\sigma$ and $\tau: 0 \to B \to N \to D \to 0$ be effacing, and let $(\alpha, \beta, \gamma): \sigma \to \tau$ be a map of short exact sequences. Then $\varphi^1_\tau T^1(\alpha) = S^1(\alpha) \varphi^1_\sigma$. Indeed, compose both sides with the epimorphism $\delta_T: T^0(C) \to T^1(A)$. By naturality of $\delta$ and of $\varphi^0$,
$$\varphi^1_\tau T^1(\alpha) \delta_T = \varphi^1_\tau \delta_T T^0(\gamma) = \delta_S \varphi^0_D T^0(\gamma) = \delta_S S^0(\gamma) \varphi^0_C = S^1(\alpha) \delta_S \varphi^0_C = S^1(\alpha) \varphi^1_\sigma \delta_T.$$

Step 3: independence and naturality. Let $f: A \to B$, and let $\sigma: 0 \to A \xrightarrow{u} M \to C \to 0$ and $\tau: 0 \to B \xrightarrow{v} N \to D \to 0$ be effacing. The map $(u, v f): A \to M \oplus N$ is a monomorphism, since $u$ is. Let $\rho$ be the short exact sequence it defines, with $C'$ its cokernel. It is effacing, since $T^i(M \oplus N) = T^i(M) \oplus T^i(N) = 0$. The projection $M \oplus N \to M$ gives a map of short exact sequences $\rho \to \sigma$ over $1_A$, and the projection $M \oplus N \to N$ gives a map $\rho \to \tau$ over $f$. By Step 2, $\varphi^1_\rho = \varphi^1_\sigma$ and $\varphi^1_\tau T^1(f) = S^1(f) \varphi^1_\rho$. With $B = A$, $f = 1_A$, this shows that $\varphi^1_\sigma$ does not depend on $\sigma$. Write $\varphi^1_A$ for it. In general it shows that $\varphi^1$ is natural.

Step 4: compatibility with $\delta$. Let $0 \to A' \xrightarrow{i} A \to A'' \to 0$ be any short exact sequence. Choose a monomorphism $w: A \to N$ with $T^i(N) = 0$ for $i > 0$. Then $w i: A' \to N$ is a monomorphism, and $\tau: 0 \to A' \to N \to N/A' \to 0$ is effacing. The maps $1_{A'}$, $w$ and the induced map $\gamma: A'' \to N/A'$ form a map of short exact sequences. Naturality of $\delta$ gives $\delta_T = \delta_T^\tau T^0(\gamma)$ and $\delta_S = \delta_S^\tau S^0(\gamma)$, where $\delta^\tau$ are the maps of $\tau$. So
$$\varphi^1_{A'} \delta_T = \varphi^1_{A'} \delta_T^\tau T^0(\gamma) = \delta_S^\tau \varphi^0_{N/A'} T^0(\gamma) = \delta_S^\tau S^0(\gamma) \varphi^0_{A''} = \delta_S \varphi^0_{A''}.$$

Uniqueness: any $\varphi^1$ that commutes with $\delta$ satisfies $\varphi^1_A \delta_T = \delta_S \varphi^0_C$ for an effacing sequence, and $\delta_T$ is an epimorphism, so $\varphi^1_A$ is the map of Step 1.

For the induction, replace $(T^0, T^1)$ by $(T^n, T^{n+1})$ and $(S^0, S^1)$ by $(S^n, S^{n+1})$. For $n \geq 1$ and an effacing $\sigma$, the sequence $0 = T^n(M) \to T^n(C) \xrightarrow{\delta_T} T^{n+1}(A) \to T^{n+1}(M) = 0$ shows that $\delta_T$ is an isomorphism, so Step 1 applies. Steps 2 to 4 use only the naturality of $\delta$ and of $\varphi^n$, and the additivity of $T^{n+1}$. $\square$

*Proof of the theorem on acyclic resolutions.* Let $K^n = \ker(J^n \to J^{n+1})$. By exactness $K^0 = A$, and there are short exact sequences $0 \to K^n \to J^n \to K^{n+1} \to 0$. Since $J^n$ is acyclic, the long exact sequence of Section 3.2 gives
$$R^1 F(K^n) \cong \operatorname{coker}(F(J^n) \to F(K^{n+1})), \qquad R^{i+1} F(K^n) \cong R^i F(K^{n+1}) \text{ for } i \geq 1.$$
So for $i \geq 1$,
$$R^i F(A) = R^i F(K^0) \cong R^{i-1} F(K^1) \cong \cdots \cong R^1 F(K^{i-1}) \cong \operatorname{coker}(F(J^{i-1}) \to F(K^i)).$$
The sequence $0 \to K^i \to J^i \to J^{i+1}$ is exact and $F$ is left exact, so $F(K^i) = \ker(F(J^i) \to F(J^{i+1}))$. The map $F(J^{i-1}) \to F(J^i)$ factors through $F(K^i)$. So the last cokernel is $H^i(F(J^\bullet))$. For $i = 0$, left exactness gives $F(A) = \ker(F(J^0) \to F(J^1)) = H^0(F(J^\bullet))$. $\square$

### Exercises

1. (A) Show that an injective object is $F$-acyclic for every left exact $F$, and that a direct summand of an $F$-acyclic object is $F$-acyclic.
2. (A) Let $\eta: F \to G$ be a natural transformation of left exact functors $\mathcal{A} \to \mathcal{B}$, with $\mathcal{A}$ having enough injectives. Show that $\eta$ extends uniquely to maps $R^i F \to R^i G$ that commute with the connecting maps.
3. (B) Let $F: \mathcal{A} \to \mathcal{B}$ be left exact, $\mathcal{A}$ with enough injectives, and $G: \mathcal{B} \to \mathcal{C}$ exact. Show that $R^i(G F) \cong G \circ R^i F$.
4. (B) Let $L: \mathcal{B} \to \mathcal{A}$ be left adjoint to $F: \mathcal{A} \to \mathcal{B}$. Show that if $L$ is exact, then $F$ sends injective objects to injective objects. (This applies to $f_*$ on sheaves, whose left adjoint $f^{-1}$ is exact; see Chapter 5.)
5. (B) Let $F$ be left exact and $0 \to A \to J^0 \to J^1 \to 0$ an $F$-acyclic resolution of length one. Show that $R^i F(A) = 0$ for $i \geq 2$ and that $R^1 F(A) = \operatorname{coker}(F(J^0) \to F(J^1))$.
6. (C) A weaker definition calls $T$ effaceable if each $A$ has a monomorphism $u: A \to M$ with $T^i(u) = 0$ for all $i > 0$. Prove Grothendieck's theorem under this weaker assumption. (Hint: check that each step of the proof uses only that the maps $T^i(A) \to T^i(M)$ are zero, and that $T^i$ of the map $A \to M \oplus N$ of Step 3 is zero.)

### Lean

Mathlib has no general notion of a $\delta$-functor. It proves the effects of universality case by case: `Functor.rightDerived` with `InjectiveResolution.isoRightDerivedObj` shows that any injective resolution computes $R^i F$, and the theory of `Abelian.Ext` in `Mathlib/Algebra/Homology/DerivedCategory/Ext` proves the long exact sequences directly in the derived category of Chapter 8. Formalizing Grothendieck's theorem and the acyclic resolution theorem would serve the comparison of sheaf and Čech cohomology in Chapter 7. The handbook adds no `MinimalModel` node here.

### Notes and history

The notion of a $\delta$-functor and the universality theorem are in Grothendieck's Tohoku paper of 1957, Chapter II. Cartan and Eilenberg had characterized derived functors by axioms in 1956. The name *effaceable* and the method of dimension shifting are Grothendieck's. The use of flasque sheaves to compute cohomology is due to Godement, whose book of 1958 builds sheaf cohomology with the canonical flasque resolution.
