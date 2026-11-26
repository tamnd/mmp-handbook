---
title: Adjoint functors
nodes: []
sources: [Vak25, Mac98]
reads_with: [Vak25:ch1, Mac98:ch4]
requires: [P1.1, P1.2, P2.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Adjoint functors

### Statement

**Definition P2.1.29 (adjunction).** Let $F: \mathcal{C} \to \mathcal{D}$ and $G: \mathcal{D} \to \mathcal{C}$ be functors. An *adjunction* $F \dashv G$ is a bijection
$$\tau_{A, B}: \operatorname{Hom}_{\mathcal{D}}(F(A), B) \to \operatorname{Hom}_{\mathcal{C}}(A, G(B))$$
for each object $A$ of $\mathcal{C}$ and $B$ of $\mathcal{D}$, natural in $A$ and in $B$. Then $F$ is a *left adjoint* of $G$ and $G$ is a *right adjoint* of $F$.

Lean: Mathlib `CategoryTheory.Adjunction` (written `F ⊣ G`), with the bijection `CategoryTheory.Adjunction.homEquiv`.

Naturality in $B$ says that $\tau(v \circ g) = G(v) \circ \tau(g)$ for $g: F(A) \to B$ and $v: B \to B'$. Naturality in $A$ says that $\tau(g \circ F(u)) = \tau(g) \circ u$ for $u: A' \to A$.

**Definition P2.1.30 (unit and counit).** Given $F \dashv G$, the *unit* is $\eta_A = \tau(1_{F(A)}): A \to G F(A)$ and the *counit* is $\varepsilon_B = \tau^{-1}(1_{G(B)}): F G(B) \to B$. They are natural transformations $\eta: 1_{\mathcal{C}} \Rightarrow G F$ and $\varepsilon: F G \Rightarrow 1_{\mathcal{D}}$.

Lean: Mathlib `CategoryTheory.Adjunction.unit` and `CategoryTheory.Adjunction.counit`.

**Theorem P2.1.31 (unit, counit and the triangle identities).** Let $F \dashv G$ with unit $\eta$ and counit $\varepsilon$.

1. For $g: F(A) \to B$ and $f: A \to G(B)$, $\tau(g) = G(g) \circ \eta_A$ and $\tau^{-1}(f) = \varepsilon_B \circ F(f)$.
2. The *triangle identities* hold: $\varepsilon_{F(A)} \circ F(\eta_A) = 1_{F(A)}$ and $G(\varepsilon_B) \circ \eta_{G(B)} = 1_{G(B)}$.
3. Conversely, natural transformations $\eta: 1 \Rightarrow G F$ and $\varepsilon: F G \Rightarrow 1$ that satisfy the triangle identities define an adjunction $F \dashv G$ by the formulas of 1.

Lean: Mathlib `CategoryTheory.Adjunction.left_triangle_components`, `CategoryTheory.Adjunction.right_triangle_components` and `CategoryTheory.Adjunction.mkOfUnitCounit` (proved in Mathlib).

**Theorem P2.1.32 (uniqueness of adjoints).** If $F \dashv G$ and $F' \dashv G$, then there is a unique natural isomorphism $F \cong F'$ compatible with the two bijections. Dually, a right adjoint is unique up to a unique natural isomorphism.

Lean: Mathlib `CategoryTheory.Adjunction.leftAdjointUniq` and `CategoryTheory.Adjunction.rightAdjointUniq` (proved in Mathlib).

**Proposition P2.1.33 (left adjoints preserve initial objects).** An object $I$ is *initial* if $\operatorname{Hom}(I, B)$ has exactly one element for every $B$, and *terminal* if $\operatorname{Hom}(B, I)$ has one element for every $B$. A left adjoint sends initial objects to initial objects, and a right adjoint sends terminal objects to terminal objects.

Lean: Mathlib `CategoryTheory.Limits.IsInitial` and `CategoryTheory.Limits.IsTerminal`; the statement is a case of `CategoryTheory.Adjunction.leftAdjoint_preservesColimits` (proved in Mathlib).

*Proof.* If $F \dashv G$ and $I$ is initial in $\mathcal{C}$, then $\operatorname{Hom}(F(I), B) \cong \operatorname{Hom}(I, G(B))$ has one element for each $B$. The dual argument applies to $G$. $\square$

Section 1.4 proves the general form: a left adjoint preserves all colimits and a right adjoint preserves all limits.

### Proof in words

An adjunction is a universal property in families. For each $A$ the pair $(G F(A), \eta_A)$ is a universal arrow from $A$ to $G$: every map $A \to G(B)$ factors as $G(g) \circ \eta_A$ for a unique $g: F(A) \to B$. So $F(A)$ is the object that represents the functor $B \mapsto \operatorname{Hom}(A, G(B))$. By the Yoneda lemma, the value $F(A)$ is determined up to unique isomorphism by $G$, and this is the uniqueness of adjoints. The triangle identities say that the two ways of passing between $\operatorname{Hom}(F(A), B)$ and $\operatorname{Hom}(A, G(B))$ are inverse to each other. Every formula about adjunctions is a short computation with naturality.

### Examples

**Example P2.1.34 (free and forgetful).** Let $U: \mathsf{Mod}_A \to \mathsf{Set}$ be the forgetful functor and $F(S) = A^{(S)}$ the free module. A linear map $A^{(S)} \to M$ is the same as a map of sets $S \to U(M)$, the images of the basis vectors. So $F \dashv U$. The unit $S \to U(A^{(S)})$ sends $s$ to $e_s$. The counit $A^{(U(M))} \to M$ sends $e_m$ to $m$, and it is surjective. That is the statement that every module is a quotient of a free module.

**Example P2.1.35 (tensor and Hom).** Let $N$ be an $A$-module. For modules $M$ and $P$, the map
$$\operatorname{Hom}_A(M \otimes_A N, P) \to \operatorname{Hom}_A(M, \operatorname{Hom}_A(N, P)), \quad g \mapsto (m \mapsto (n \mapsto g(m \otimes n)))$$
is a bijection, natural in $M$ and $P$. Both sides are the $A$-bilinear maps $M \times N \to P$. So $- \otimes_A N$ is left adjoint to $\operatorname{Hom}_A(N, -)$. Section 1.4 deduces that $- \otimes_A N$ preserves cokernels, which is the right exactness of P1 Ch. 1.

**Example P2.1.36 (extension and restriction of scalars).** Let $\varphi: A \to B$ be a ring map. Restriction of scalars $\varphi_*: \mathsf{Mod}_B \to \mathsf{Mod}_A$ has the left adjoint $M \mapsto B \otimes_A M$:
$$\operatorname{Hom}_B(B \otimes_A M, P) \cong \operatorname{Hom}_A(M, \varphi_* P), \quad g \mapsto (m \mapsto g(1 \otimes m)).$$
It also has a right adjoint $M \mapsto \operatorname{Hom}_A(B, M)$, with $B$ acting through the source. For $B = S^{-1}A$ the left adjoint is localization. In P3 and Chapter 6 these become the pullback $f^*$ and the pushforward $f_*$ of quasicoherent sheaves along $f: \operatorname{Spec} B \to \operatorname{Spec} A$, and the adjunction $f^* \dashv f_*$.

**Example P2.1.37 (a functor with no right adjoint).** The forgetful functor $U: \mathsf{Mod}_A \to \mathsf{Set}$ has a left adjoint, but no right adjoint. The zero module is initial in $\mathsf{Mod}_A$, and $U(0)$ is a set with one element, which is not initial in $\mathsf{Set}$: the empty set is the initial object. By the proposition, $U$ is not a left adjoint. The hypothesis that fails is the preservation of colimits, which every left adjoint has.

**Example P2.1.38 (adjunctions ahead).** Chapter 5 proves that sheafification $\mathcal{F} \mapsto \mathcal{F}^{\mathrm{sh}}$ is left adjoint to the inclusion of sheaves into presheaves, and that for a continuous map $f: X \to Y$ the inverse image $f^{-1}$ is left adjoint to the direct image $f_*$. Each adjunction gives, by the uniqueness of adjoints, a definition of the left adjoint that does not depend on its construction.

### Proof

*Proof of the theorem on units and counits.* For 1, apply naturality in $B$ to $1_{F(A)}$ and $g: F(A) \to B$: $\tau(g) = \tau(g \circ 1_{F(A)}) = G(g) \circ \tau(1_{F(A)}) = G(g) \circ \eta_A$. The formula for $\tau^{-1}$ is the dual, from naturality of $\tau^{-1}$ in $A$. Naturality of $\eta$: for $u: A' \to A$, $G F(u) \circ \eta_{A'} = \tau(F(u))$ by 1, and $\eta_A \circ u = \tau(1_{F(A)}) \circ u = \tau(F(u))$ by naturality in $A$. The same argument applies to $\varepsilon$.

For 2, put $f = \eta_A = \tau(1_{F(A)})$ in 1: $1_{F(A)} = \tau^{-1}(\eta_A) = \varepsilon_{F(A)} \circ F(\eta_A)$. Put $g = \varepsilon_B = \tau^{-1}(1_{G(B)})$: $1_{G(B)} = \tau(\varepsilon_B) = G(\varepsilon_B) \circ \eta_{G(B)}$.

For 3, define $\tau(g) = G(g) \circ \eta_A$ and $\sigma(f) = \varepsilon_B \circ F(f)$. Both are natural, since $\eta$ and $\varepsilon$ are natural and $F, G$ are functors. Then
$$\sigma(\tau(g)) = \varepsilon_B \circ F G(g) \circ F(\eta_A) = g \circ \varepsilon_{F(A)} \circ F(\eta_A) = g,$$
by naturality of $\varepsilon$ and the first triangle identity. In the same way $\tau(\sigma(f)) = G(\varepsilon_B) \circ G F(f) \circ \eta_A = G(\varepsilon_B) \circ \eta_{G(B)} \circ f = f$, by naturality of $\eta$ and the second identity. So $\tau$ is a natural bijection. $\square$

*Proof of the uniqueness of adjoints.* For each $A$, the two adjunctions give natural isomorphisms of functors of $B$,
$$h^{F(A)} = \operatorname{Hom}(F(A), -) \cong \operatorname{Hom}(A, G(-)) \cong \operatorname{Hom}(F'(A), -) = h^{F'(A)}.$$
By the covariant Yoneda lemma this composite is induced by a unique isomorphism $\theta_A: F'(A) \to F(A)$. Naturality in $A$ follows from the fact that the isomorphisms are natural in $A$ and from the faithfulness of the Yoneda embedding. The statement for right adjoints is the dual. $\square$

### Exercises

1. (A) Write down the unit and the counit of the adjunction $- \otimes_A N \dashv \operatorname{Hom}_A(N, -)$, and check the triangle identities.
2. (A) Show that the abelianization $G \mapsto G/[G, G]$ is left adjoint to the inclusion $\mathsf{Ab} \to \mathsf{Grp}$.
3. (B) Show that the functor $\mathsf{Ring} \to \mathsf{Set}$, $R \mapsto R$, has the left adjoint $S \mapsto \mathbb{Z}[x_s : s \in S]$, and that $R \mapsto R^\times$, from $\mathsf{Ring}$ to $\mathsf{Ab}$, has the left adjoint that sends $G$ to the group ring $\mathbb{Z}[G]$.
4. (B) Let $\varphi: A \to B$ be a ring map. Prove that $\operatorname{Hom}_A(B, -)$ is right adjoint to restriction of scalars.
5. (B) Let $U$ be the forgetful functor $\mathsf{Top} \to \mathsf{Set}$. Show that $U$ has a left adjoint (the discrete topology) and a right adjoint (the indiscrete topology).
6. (B) Let $F \dashv G$. Show that $G$ is fully faithful if and only if the counit $\varepsilon$ is an isomorphism. Apply this to the inclusion of $\mathsf{Ab}$ into $\mathsf{Grp}$ and to the inclusion of sheaves into presheaves (Chapter 5).

### Lean

Mathlib defines `CategoryTheory.Adjunction` by a unit and a counit with the triangle identities, and gives the bijection `Adjunction.homEquiv` and the constructors `Adjunction.mkOfHomEquiv` and `Adjunction.mkOfUnitCounit`. The uniqueness of adjoints is `Adjunction.leftAdjointUniq` and `Adjunction.rightAdjointUniq`. The free and forgetful adjunction for modules is `ModuleCat.adj`. The handbook adds no `MinimalModel` node here.

### Notes and history

Kan introduced adjoint functors in 1958, with the tensor and Hom pair as the model case. The notion took some years to spread, and Freyd's adjoint functor theorem of 1964 gave the general existence criterion. Mac Lane, Chapter IV, says that adjoint functors arise everywhere, and the algebraic geometry of P3 to P8 bears this out: pullback and pushforward, sheafification, the functors $f^!$ of Grothendieck duality in P4 Ch. 9, and the adjoint pairs of the derived category in Chapter 8. Every statement here is classical.
