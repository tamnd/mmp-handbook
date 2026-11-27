---
title: Stein factorization and contractions
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:III.11, Vak25:ch29]
requires: [P1.4, P3.5, P3.6, P3.7, P4.2, P4.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Stein factorization and contractions

### Statement

**Definition P4.6.14 (contraction).** A *contraction* is a projective morphism $f \colon X \to Y$ of Noetherian schemes with $f_* \mathcal{O}_X = \mathcal{O}_Y$.

By Theorem P4.6.7 a contraction is surjective with connected fibres, and by Theorem P4.6.8 every projective birational morphism of integral schemes onto a normal scheme is a contraction. The structure morphism of a projective variety $X$ over an algebraically closed field $k$ is a contraction onto $\operatorname{Spec} k$ exactly when $H^0(X, \mathcal{O}_X) = k$, which holds when $X$ is connected and reduced (Theorem P3.4.21).

**Theorem P4.6.15 (Stein factorization).** Let $f \colon X \to Y$ be projective, with $Y$ Noetherian. Let $Y' = \operatorname{Spec}_Y f_* \mathcal{O}_X$ be the relative spectrum of the coherent $\mathcal{O}_Y$-algebra $f_* \mathcal{O}_X$ (Theorem P3.5.35), with $g \colon Y' \to Y$. Then $f$ factors as
$$X \xrightarrow{f'} Y' \xrightarrow{g} Y,$$
where $g$ is finite and $f'$ is a contraction. For every $y \in Y$ the connected components of $X_y$ are the nonempty fibres $X'_{y'} = f'^{-1}(y')$ for $y' \in g^{-1}(y)$, so they are in bijection with the points of $g^{-1}(y)$ in the image of $f'$, which is all of $g^{-1}(y)$.

Lean: not in Lean as stated.

**Corollary P4.6.16 (when $f$ is already a contraction).** Let $f \colon X \to Y$ be a projective surjective morphism of integral schemes, with $Y$ Noetherian and normal. If $K(Y)$ is algebraically closed in $K(X)$, then $f$ is a contraction.

Lean: not in Lean as stated.

**Corollary P4.6.17 (quasi-finite projective morphisms are finite).** A projective morphism $f \colon X \to Y$, with $Y$ Noetherian, all of whose fibres are finite, is finite.

Lean: not in Lean as stated.

So every projective morphism is a contraction followed by a finite morphism, and the finite part records how the fibres break into connected pieces. The minimal model program works with contractions: the morphisms it produces from the cone theorem, the fibrations at the end of it, and the Iitaka fibration are all contractions, and a projective morphism is replaced by its Stein factorization whenever only the contraction part matters.

### Proof in words

The sheaf $f_* \mathcal{O}_X$ is a coherent $\mathcal{O}_Y$-algebra, so its relative spectrum is finite over $Y$, and $f$ factors through it by the universal property of the relative spectrum. Over $Y'$, the pushforward of $\mathcal{O}_X$ is the sheaf on $Y'$ associated with $f_* \mathcal{O}_X$ itself, which is $\mathcal{O}_{Y'}$. Connectedness of the fibres of $f'$ comes from Theorem P4.6.7. Since $g$ has finite fibres, the fibre $X_y$ is the disjoint union of the finitely many connected fibres of $f'$ over the points of $g^{-1}(y)$. For the corollaries, $f_* \mathcal{O}_X$ is integral over $\mathcal{O}_Y$ and sits inside $K(X)$, so the hypotheses of Corollary P4.6.16 force it to be $\mathcal{O}_Y$, and if every fibre of $f$ is finite then every fibre of $f'$ is a single point, which makes $f'$ finite by Proposition P4.6.9, and then an isomorphism.

### Examples

**Example P4.6.18 (a double cover followed by a projection).** Let $k$ be algebraically closed of characteristic not $2$, $C = V(v^2 - u) \subseteq \mathbb{A}^2_k$ with the finite map $g \colon C \to \mathbb{A}^1_k$, $(u, v) \mapsto u$, and $X = \mathbb{P}^1_k \times C$ with $f = g \circ \operatorname{pr}_2 \colon X \to \mathbb{A}^1_k$. Then $f_* \mathcal{O}_X = g_* \operatorname{pr}_{2*} \mathcal{O}_X = g_* \mathcal{O}_C$ by Theorem P4.2.1, so $Y' = C$ and the Stein factorization is $X \to C \to \mathbb{A}^1$. The fibre of $f$ over $u \neq 0$ is two disjoint lines, matching the two points $v = \pm \sqrt{u}$ of $g^{-1}(u)$, and over $u = 0$ it is one line, doubled in the scheme structure of $g^{-1}(0) = \operatorname{Spec} k[v]/(v^2)$.

**Example P4.6.19 (a connected fibre that is not geometrically connected).** Let $X = \mathbb{P}^1_{\mathbb{C}}$, viewed as a scheme over $Y = \operatorname{Spec} \mathbb{R}$. Then $f$ is projective, $f_* \mathcal{O}_X = \mathbb{C}$, and $Y' = \operatorname{Spec} \mathbb{C}$. The single fibre $X$ is connected, as Theorem P4.6.15 predicts since $g^{-1}(y)$ is one point, but $f$ is not a contraction, and $X \times_{\mathbb{R}} \mathbb{C} \cong \mathbb{P}^1_{\mathbb{C}} \sqcup \mathbb{P}^1_{\mathbb{C}}$ is disconnected. Exercise 6 of Section 6.2 shows that the fibres of a contraction are geometrically connected, so this cannot happen for a contraction.

**Example P4.6.20 (a finite morphism).** Let $k$ have characteristic not $2$ and $f \colon \mathbb{P}^1_k \to \mathbb{P}^1_k$, $[s : t] \mapsto [s^2 : t^2]$. It is finite, $f_* \mathcal{O} = \mathcal{O} \oplus \mathcal{O}(-1)$, a rank-$2$ algebra, so $Y' = \mathbb{P}^1_k$ (the source) and $f'$ is the identity. The fibres have two points, or one non-reduced point over $0$ and $\infty$, and each point is its own connected component. In general, for $f$ finite, $Y' = X$ and the Stein factorization says nothing new.

### Proof

*Theorem P4.6.15.* By Theorem P4.4.8, $\mathcal{A} = f_* \mathcal{O}_X$ is a coherent $\mathcal{O}_Y$-algebra. By Theorem P3.5.35 its relative spectrum $g \colon Y' \to Y$ is affine with $g_* \mathcal{O}_{Y'} = \mathcal{A}$, so $g$ is finite. The identity of $\mathcal{A} = f_* \mathcal{O}_X$, an $\mathcal{O}_Y$-algebra map, corresponds by the universal property of the relative spectrum (Theorem P3.5.35) to a $Y$-morphism $f' \colon X \to Y'$ with $g \circ f' = f$.

*$f'$ is projective.* The closed immersion $X \to \mathbb{P}^r_Y$ and $f'$ give a morphism $X \to \mathbb{P}^r_Y \times_Y Y' = \mathbb{P}^r_{Y'}$ over $Y'$. It is the composition of the graph $X \to X \times_Y Y'$ of $f'$, a closed immersion because $Y' \to Y$ is separated, with the closed immersion $X \times_Y Y' \to \mathbb{P}^r_{Y'}$. So $f'$ is projective.

*$f'_* \mathcal{O}_X = \mathcal{O}_{Y'}$.* The question is local on $Y$, so let $Y = \operatorname{Spec} A$, $B = H^0(X, \mathcal{O}_X)$ and $Y' = \operatorname{Spec} B$. For $b \in B$, $f'^{-1}(D(b)) = X_b$, the open set where the global function $b$ is invertible. By Proposition P3.5.11, applied to the quasi-compact and separated scheme $X$, $H^0(X_b, \mathcal{O}_X) = B_b$. So $f'_* \mathcal{O}_X$ and $\mathcal{O}_{Y'}$ agree on the basis of opens $D(b)$, compatibly with restriction, and they are equal. So $f'$ is a contraction.

*Fibres.* Let $y \in Y$. The fibre $g^{-1}(y)$ is $\operatorname{Spec}$ of the finite $k(y)$-algebra $\mathcal{A}_y \otimes k(y)$, a finite discrete set $\{y'_1, \ldots, y'_m\}$. Then $X_y = \bigsqcup_i f'^{-1}(y'_i)$ set-theoretically, and each $f'^{-1}(y'_i)$ is closed in $X_y$. A finite disjoint union of closed subsets is a decomposition into open and closed subsets. Each $f'^{-1}(y'_i)$ is nonempty and connected by Theorem P4.6.7 applied to the contraction $f'$. So these are the connected components of $X_y$. $\square$

*Corollary P4.6.16.* The question is local on $Y$, so let $Y = \operatorname{Spec} A$ with $A$ a normal Noetherian domain, and $B = H^0(X, \mathcal{O}_X)$, a finitely generated $A$-module by Theorem P4.2.7 and a domain since $X$ is integral. Since $f$ is surjective, $f$ is dominant, so $A \to B$ is injective and $B \subseteq K(X)$, with every element of $B$ integral over $A$ (Section P1.4). An element $b \in B$ satisfies a monic polynomial over $A \subseteq K(Y)$, so it is algebraic over $K(Y)$, and by the hypothesis $b \in K(Y)$. Then $b \in K(Y)$ is integral over the integrally closed domain $A$, so $b \in A$. So $B = A$. $\square$

*Corollary P4.6.17.* Let $f = g \circ f'$ be the Stein factorization. The fibres of $f'$ are nonempty and connected by Theorem P4.6.15, and contained in the finite fibres of $f$, so every fibre of $f'$ is a single point. By Proposition P4.6.9 applied to $f'$ at every point of $Y'$, $f'$ is finite, and then $f'$ is a finite morphism with $f'_* \mathcal{O}_X = \mathcal{O}_{Y'}$, which means $f'$ is affine with $\mathcal{O}_{Y'} \to f'_* \mathcal{O}_X$ an isomorphism, so $f'$ is an isomorphism. So $f$ is isomorphic to $g$, which is finite. $\square$

### Exercises

1. (A) Show that a contraction $f \colon X \to Y$ with $X$ integral has $Y$ integral, and $X$ normal implies $Y$ normal.
2. (A) Let $f \colon X \to Y$ be projective with $Y$ Noetherian. Show that the fibres of $f$ are connected if and only if the stalks of $f_* \mathcal{O}_X$ at the points of $Y$ are local rings.
3. (B) Compute the Stein factorization of the projection $V(y^2 - x(x - 1)(x - t)) \subseteq \mathbb{P}^2 \times \mathbb{A}^1_t \to \mathbb{A}^1_t$, with $\operatorname{char} k \neq 2$, and of the composite $\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1 \to \mathbb{P}^1$ of a projection and $[s : t] \mapsto [s^3 : t^3]$.
4. (B) Let $X$ be a normal projective variety over an algebraically closed field and $f \colon X \to \mathbb{P}^n$ a morphism. Show that $Y'$ in the Stein factorization is the normalization of the image $f(X)$ in $K(X)$, in the sense of Section P3.7.
5. (B) Let $f \colon X \to Y$ be a projective surjective morphism of normal varieties over an algebraically closed field of characteristic $0$, with general fibre connected. Show that $f$ is a contraction.
6. (C) Let $X$ be a normal projective variety over an algebraically closed field $k$, and $L$ a line bundle on $X$ with $L^{\otimes m}$ globally generated for some $m \geq 1$. Show that the Stein factorizations of the morphisms $\varphi_m \colon X \to \mathbb{P}(H^0(L^{\otimes m}))$, over all such $m$, have a common contraction part $X \to Y$ for $m$ divisible enough, with $L^{\otimes m}$ the pullback of an ample line bundle on $Y$. (This is the contraction defined by a semiample line bundle, used in Volume 1.)

### Lean

Mathlib has affine morphisms (`AlgebraicGeometry.IsAffineHom`), finite morphisms (`AlgebraicGeometry.IsFinite`) and integral closure of domains. The Stein factorization is not in Mathlib, since it needs the coherence of $f_* \mathcal{O}_X$. The handbook adds no `MinimalModel` node here.

### Notes and history

Karl Stein introduced the factorization in 1956 for proper holomorphic maps of complex spaces, in *Analytische Zerlegungen komplexer Räume*. Grothendieck gave the algebraic version for proper morphisms of locally Noetherian schemes in EGA III.4.3.1, together with Corollary P4.6.17 in the form that proper quasi-finite morphisms are finite (EGA III.4.4.2). Hartshorne III.11.5 states the projective case. The literature state is theorem. In the minimal model program, every extremal contraction, Mori fibre space, and semiample fibration is a contraction in the sense of Definition P4.6.14, and the Stein factorization is the step that turns a morphism defined by a linear system into one.
