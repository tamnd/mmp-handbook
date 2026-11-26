---
title: Universally closed and proper morphisms
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch11, Har77:II.4, GW20:ch12]
requires: [P1.4, P3.2, P3.3, P3.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Universally closed and proper morphisms

### Statement

**Definition P3.4.18 (universally closed, proper).** A morphism $f \colon X \to Y$ is *closed* if the map of spaces sends closed sets to closed sets. It is *universally closed* if for every morphism $Y' \to Y$ the base change $X \times_Y Y' \to Y'$ is closed. It is *proper* if it is separated, of finite type and universally closed. A scheme $X$ over $S$ is proper over $S$ if its structure morphism is proper.

Lean: Mathlib `AlgebraicGeometry.UniversallyClosed` and `AlgebraicGeometry.IsProper` (definitions in Mathlib). Mathlib asks for locally of finite type, and quasi-compactness follows from universal closedness.

**Proposition P3.4.19 (stability of proper morphisms).**

1. Universally closed morphisms and proper morphisms are stable under composition and under base change, and each property is local on the target.
2. Closed immersions and finite morphisms are proper.

Lean: Mathlib instances `IsStableUnderComposition @UniversallyClosed` via `AlgebraicGeometry.universallyClosed_isStableUnderComposition`, `AlgebraicGeometry.universallyClosed_isStableUnderBaseChange`, `AlgebraicGeometry.IsProper.isStableUnderBaseChange`, `AlgebraicGeometry.IsProper.stableUnderComposition`, and the instance that a finite morphism is proper (proved in Mathlib).

**Proposition P3.4.20 (morphisms out of a proper scheme).** Let $X$ be proper over a scheme $S$, let $Y$ be separated over $S$, and let $f \colon X \to Y$ be a morphism over $S$. Then $f$ is proper. In particular $f(X)$ is closed in $Y$, and $f(Z)$ is closed for every closed subset $Z \subseteq X$.

Lean: Mathlib `AlgebraicGeometry.IsProper.of_comp` (proved in Mathlib).

**Theorem P3.4.21 (global functions on a proper scheme).** Let $k$ be an algebraically closed field and $X$ a nonempty, connected, reduced scheme that is proper over $k$. Then $\Gamma(X, \mathcal{O}_X) = k$.

Lean: not in Lean as stated. Mathlib `AlgebraicGeometry.finite_appTop_of_universallyClosed` proves that for an integral scheme universally closed and locally of finite type over a field $K$, the ring of global functions is finite over $K$, and `AlgebraicGeometry.isField_of_universallyClosed` that it is a field.

**Corollary P3.4.22 (proper and affine).** Let $k$ be algebraically closed and $X$ a nonempty, connected, reduced scheme that is proper over $k$.

1. Every morphism from $X$ to an affine $k$-scheme has image a single closed point.
2. If $X$ is affine, then $X \cong \operatorname{Spec} k$.

Lean: not in Lean as stated.

### Proof in words

Universal closedness is a topological condition, so its stability follows from the formal properties of base change. A finite morphism is closed by the lying over theorem: the image of $V(J)$ under $\operatorname{Spec} B \to \operatorname{Spec} A$ is $V(J \cap A)$ when $B$ is integral over $A$. Base change keeps finite morphisms finite, so finite morphisms are universally closed.

A morphism out of a proper scheme factors through its graph, which is closed by Section 4.2, followed by a projection, which is a base change of a proper morphism. So it is proper. A global function on $X$ is a morphism to $\mathbb{A}^1_k \subseteq \mathbb{P}^1_k$, and its image is closed in $\mathbb{P}^1_k$ and misses the point at infinity. So the image is finite, and on a connected reduced scheme the function is constant. This is the algebraic form of Liouville's theorem: a holomorphic function on a compact connected complex manifold is constant.

### Examples

**Example P3.4.23 (the affine line is not proper).** The morphism $\mathbb{A}^1_k \to \operatorname{Spec} k$ is closed, since the target is a point. It is not universally closed. Its base change along $\mathbb{A}^1_k \to \operatorname{Spec} k$ is the projection $\mathbb{A}^2_k = \operatorname{Spec} k[x, y] \to \mathbb{A}^1_k = \operatorname{Spec} k[y]$, and the image of the closed hyperbola $V(xy - 1)$ is $D(y)$, which is not closed. Section 4.4 shows that the hyperbola acquires the missing point over $y = 0$ in $\mathbb{P}^1_k \times_k \mathbb{A}^1_k$.

**Example P3.4.24 (affine and of finite type, not proper).** The open immersion $\mathbb{A}^1_k \setminus \{0\} \to \mathbb{A}^1_k$ is separated, affine and of finite type, but its image is not closed, so it is not proper. Compare Example P3.3.36, where it is shown not to be finite.

**Example P3.4.25 (the normalization of the cusp).** The morphism $\nu \colon \mathbb{A}^1_k \to C = \operatorname{Spec} k[t^2, t^3]$ of Example P3.3.15 is finite, since $k[t] = k[t^2, t^3] \cdot 1 + k[t^2, t^3] \cdot t$. So it is proper by Proposition P3.4.19. A proper morphism that is a homeomorphism need not be an isomorphism, or even a closed immersion.

**Example P3.4.26 (universally closed but not separated).** Let $X$ be the projective line with a doubled point: glue two copies $P_1, P_2$ of $\mathbb{P}^1_k$ along $\mathbb{P}^1_k \setminus \{0\}$ by the identity. Then $X$ is of finite type over $k$ and not separated, by the argument of Example P3.4.4. It is universally closed over $k$, once Section 4.4 shows that $\mathbb{P}^1_k$ is. For a base change $X_T = (P_1)_T \cup (P_2)_T$ over a $k$-scheme $T$ and a closed set $C \subseteq X_T$, the image of $C$ in $T$ is the union of the images of the closed sets $C \cap (P_i)_T \subseteq (P_i)_T$, and each of them is closed.

**Example P3.4.27 (proper varieties have no nonconstant functions).** By Theorem P3.4.21, every global function on $\mathbb{P}^n_k$ is constant, for $k$ algebraically closed; this agrees with Proposition P3.2.11, which proves $\Gamma(\mathbb{P}^n_A, \mathcal{O}) = A$ for every ring $A$ by direct computation. The theorem needs reducedness: on $X = \operatorname{Spec} k[\varepsilon]/(\varepsilon^2)$, which is finite and so proper over $k$, the global functions form a ring of dimension $2$. It needs connectedness: on $\operatorname{Spec} k \sqcup \operatorname{Spec} k$ they form $k \times k$.

### Proof

*Proof of Proposition P3.4.19.* Part 1, composition. Let $f \colon X \to Y$ and $g \colon Y \to Z$ be universally closed and $Z' \to Z$ a morphism. Let $Y' = Y \times_Z Z'$. Then $X \times_Z Z' = X \times_Y Y'$, since both have as $T$-points the pairs of a $T$-point of $X$ and a $T$-point of $Z'$ with the same image in $Z$. So the base change of $g f$ is the composite $X \times_Y Y' \to Y' \to Z'$ of two closed maps, which is closed. Proper morphisms are then stable under composition by Proposition P3.4.9 and Proposition P3.3.32.

Base change. A base change of $X \times_Y Y' \to Y'$ along $Y'' \to Y'$ is the base change of $X \to Y$ along $Y'' \to Y$, by the same computation with $T$-points. So a base change of a universally closed morphism is universally closed, and the same holds for proper morphisms by Proposition P3.4.9 and Proposition P3.3.32.

Locality. Let $Y = \bigcup_j V_j$ be an open cover such that each $f^{-1}(V_j) \to V_j$ is universally closed, and let $Y' \to Y$ be a morphism with preimages $V'_j$. By part 1 of Proposition P3.3.20, the preimage of $V'_j$ in $X \times_Y Y'$ is $f^{-1}(V_j) \times_{V_j} V'_j$. A map of spaces is closed if its restrictions over the sets of an open cover of the target are closed. So $X \times_Y Y' \to Y'$ is closed. Separatedness is local on the target: the open sets $f^{-1}(V_j) \times_{V_j} f^{-1}(V_j)$ cover $X \times_Y X$, since the two projections of a point have the same image in $Y$, and over each of them the diagonal of $f$ is the diagonal of $f^{-1}(V_j) \to V_j$, so part 1 of Proposition P3.3.11 applies. Finite type is local on the target by Proposition P3.3.31.

Part 2. A closed immersion is finite by Proposition P3.3.32, so it suffices to treat a finite morphism $f \colon X \to Y$. It is of finite type: on affine pieces, module generators of $B$ over $A$ also generate $B$ as an $A$-algebra. It is separated, by the locality of separatedness just shown, since over an affine cover $\{V_j\}$ of $Y$ each $f^{-1}(V_j) \to V_j$ is a morphism of affine schemes, which is separated by Proposition P3.4.2. A base change of a finite morphism is finite by Proposition P3.3.32, so it remains to show that a finite morphism is closed. By locality on the target, let $Y = \operatorname{Spec} A$, $X = \operatorname{Spec} B$ with $\varphi \colon A \to B$ finite. Then $B$ is integral over $A$ (P1.4.2). Let $J \subseteq B$ be an ideal and $I = \varphi^{-1}(J)$. The induced map $A/I \to B/J$ is injective and integral. By the lying over theorem P1.4.12, every prime of $A/I$ is the contraction of a prime of $B/J$. So the image of $V(J)$ is $V(I)$, which is closed. $\square$

*Proof of Proposition P3.4.20.* Write $f = p_2 \circ \Gamma_f$ with $\Gamma_f \colon X \to X \times_S Y$ and $p_2 \colon X \times_S Y \to Y$. By part 2 of Proposition P3.4.10, $\Gamma_f$ is a closed immersion, so it is proper by Proposition P3.4.19. The projection $p_2$ is the base change of $X \to S$ along $Y \to S$, so it is proper by Proposition P3.4.19. So $f$ is proper by Proposition P3.4.19, and in particular closed. $\square$

*Proof of Theorem P3.4.21.* The closed sets of $\mathbb{P}^1_k$. Cover $\mathbb{P}^1_k$ by the charts $U_0 = \operatorname{Spec} k[t]$ and $U_1$, both isomorphic to $\mathbb{A}^1_k$. A closed subset $C \subseteq U_0$ is $V(I)$ for an ideal $I$ of the principal ideal domain $k[t]$, so either $C = U_0$ or $C$ is a finite set of closed points. Let $C \subseteq \mathbb{P}^1_k$ be closed and $C \neq \mathbb{P}^1_k$. If $C \supseteq U_0$, then $C$ contains the closure of $U_0$, which is $\mathbb{P}^1_k$ since $\mathbb{P}^1_k$ is irreducible with generic point in $U_0$. So $C \cap U_0$ is finite, and in the same way $C \cap U_1$ is finite. So $C$ is a finite set of closed points.

The function. The map $k \to \Gamma(X, \mathcal{O}_X)$ is injective, since $X \neq \emptyset$. Let $s \in \Gamma(X, \mathcal{O}_X)$. By Theorem P3.1.22, $s$ defines a morphism $\varphi \colon X \to \mathbb{A}^1_k = U_0$ over $k$ with $t \mapsto s$. Let $\psi \colon X \to \mathbb{P}^1_k$ be its composite with the open immersion $U_0 \to \mathbb{P}^1_k$. Since $\mathbb{P}^1_k$ is separated over $k$ (Example P3.4.6), $\psi$ is proper by Proposition P3.4.20, so $\psi(X)$ is closed. It does not contain the point at infinity, so it is a finite set of closed points by the first step. A finite set of closed points is discrete in the subspace topology, and $\psi(X)$ is connected and nonempty, so $\psi(X)$ is one closed point of $U_0$. Since $k$ is algebraically closed, this point is $(t - c)$ for some $c \in k$.

Let $\operatorname{Spec} A \subseteq X$ be an affine open set. The morphism $\varphi|_{\operatorname{Spec} A}$ corresponds to the ring map $k[t] \to A$ with $t \mapsto s|_{\operatorname{Spec} A}$, and it sends every prime $\mathfrak{q}$ of $A$ to $(t - c)$. So $s - c \in \mathfrak{q}$ for every prime $\mathfrak{q}$, and $s - c$ is nilpotent in $A$ by Theorem P1.1.9. Since $X$ is reduced, $s - c = 0$ on $\operatorname{Spec} A$. The affine open sets cover $X$, so $s = c$. $\square$

*Proof of Corollary P3.4.22.* Part 1. Let $X \to \operatorname{Spec} B$ be a morphism over $k$. By Theorem P3.1.22 it corresponds to a $k$-algebra map $B \to \Gamma(X, \mathcal{O}_X) = k$, so it factors through a morphism $\operatorname{Spec} k \to \operatorname{Spec} B$, whose image is the closed point given by the kernel of $B \to k$.

Part 2. If $X = \operatorname{Spec} A$, then $A = \Gamma(X, \mathcal{O}_X) = k$. $\square$

### Exercises

1. (A) Show that a closed subscheme of a scheme proper over $S$ is proper over $S$.
2. (A) Show that $\operatorname{Spec} k[x, y]/(xy - 1) \to \operatorname{Spec} k[x]$ is not finite, by computing its image.
3. (A) Show that the fibres of a proper morphism $f \colon X \to Y$ are proper over the residue fields $\kappa(y)$.
4. (B) Let $f \colon X \to Y$ and $g \colon Y \to Z$ be morphisms with $g f$ proper and $g$ separated. Show that $f$ is proper. Deduce that a morphism between schemes proper over $S$ is proper.
5. (B) Show that a proper open immersion $U \to X$ with $X$ connected and $U \neq \emptyset$ is an isomorphism.
6. (B) Let $k$ be algebraically closed and $X$ a connected reduced scheme proper over $k$. Show that every morphism $X \to \mathbb{A}^n_k$ is constant, and that every morphism $\mathbb{P}^1_k \to \mathbb{A}^n_k \setminus \{0\}$ is constant.
7. (C) Let $k$ be any field and $X$ an integral scheme proper over $k$. Show that $\Gamma(X, \mathcal{O}_X)$ is a field that is algebraic over $k$. (Follow the proof of Theorem P3.4.21: the image of $X$ in $\mathbb{P}^1_k$ is one closed point $V(h)$ with $h$ irreducible, and then $h(s) = 0$.) The finiteness over $k$ is proved in Mathlib as `AlgebraicGeometry.finite_appTop_of_universallyClosed`.

### Lean

Mathlib defines `AlgebraicGeometry.UniversallyClosed` as `universally (topologically IsClosedMap)` (`AlgebraicGeometry.universallyClosed_eq`) and `AlgebraicGeometry.IsProper` as separated, universally closed and locally of finite type. The stability results are instances; finite morphisms are proper by an instance in `Mathlib/AlgebraicGeometry/Morphisms/Proper.lean`, and the cancellation is `AlgebraicGeometry.IsProper.of_comp`. The integral version of Theorem P3.4.21 over an arbitrary field is `AlgebraicGeometry.isField_of_universallyClosed` together with `AlgebraicGeometry.finite_appTop_of_universallyClosed`. The handbook adds no `MinimalModel` node here.

### Notes and history

Proper morphisms are defined in EGA II, Section 5.4, and in Hartshorne, Section II.4. Hartshorne, EGA and the Stacks project use the same three conditions. The literature state is theorem. In the program a contraction $\varphi \colon X \to Z$ of an extremal ray is a proper morphism with $\varphi_* \mathcal{O}_X = \mathcal{O}_Z$, and Theorem P3.4.21 is the case $Z = \operatorname{Spec} k$ of this condition. The relative version, the Stein factorization, needs the coherence of direct images and comes in a later volume.
