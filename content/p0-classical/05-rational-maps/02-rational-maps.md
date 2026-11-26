---
title: Rational maps and birational equivalence
nodes: []
sources: [Rei88, Har77, Sha13, Har92]
reads_with: [Rei88:ch5, Har77:I.4, Sha13:ch1, Har92:lecture7]
requires: [P0.3, P0.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Rational maps and birational equivalence

### Statement

**Definition P0.5.8.** Let $X$ and $Y$ be varieties. A *rational map* $\varphi : X \dashrightarrow Y$ is an equivalence class of pairs $(U, \varphi_U)$, where $U \subset X$ is a nonempty open set and $\varphi_U : U \to Y$ is a morphism. Two pairs $(U, \varphi_U)$ and $(V, \varphi_V)$ are equivalent when $\varphi_U$ and $\varphi_V$ agree on $U \cap V$. The *domain of definition* of $\varphi$ is the union of all the open sets $U$ of the pairs in the class. The map $\varphi$ is *dominant* if $\varphi_U(U)$ is dense in $Y$ for one (and so for every) pair.

Lean: Mathlib `AlgebraicGeometry.Scheme.RationalMap`, with the domain `AlgebraicGeometry.Scheme.RationalMap.domain`.

The relation is an equivalence relation, and the domain of definition carries a morphism. Both facts come from one lemma: two morphisms $U \to Y$ that agree on a nonempty open subset of the variety $U$ agree on $U$. The set where they agree is closed, because $Y$ is a variety (it is separated, P3), and a nonempty open subset of an irreducible space is dense.

**Example P0.5.9.** The map $\mathbb{P}^2 \dashrightarrow \mathbb{P}^1$, $(x : y : z) \mapsto (x : y)$, is the projection from $p = (0 : 0 : 1)$. It is a morphism on $\mathbb{P}^2 \setminus \{p\}$. Its domain of definition is $\mathbb{P}^2 \setminus \{p\}$: on a line through $p$ the map is constant, and the lines through $p$ have all the values of $\mathbb{P}^1$, so no value at $p$ makes the map continuous there.

**Example P0.5.10.** Let $C = V(xz - y^2) \subset \mathbb{P}^2$ and $p = (1 : 0 : 0) \in C$. The projection $(x : y : z) \mapsto (y : z)$ is defined on $C \setminus \{p\}$. On $C$ the relation $xz = y^2$ gives $(y : z) = (x : y)$ where both sides are defined, and $(x : y)$ is defined at $p$. So the domain of definition is all of $C$. The morphism $C \to \mathbb{P}^1$ has the inverse $(s : t) \mapsto (s^2 : st : t^2)$, so $C \cong \mathbb{P}^1$.

**Definition P0.5.11.** A dominant rational map $\varphi : X \dashrightarrow Y$ gives a homomorphism of $k$-algebras $\varphi^* : k(Y) \to k(X)$: for $f \in k(Y)$, the function $f \circ \varphi_U$ is regular on the open set $\varphi_U^{-1}(\operatorname{dom} f)$, which is not empty because $\varphi$ is dominant. The map $\varphi$ is *birational* if there is a dominant rational map $\psi : Y \dashrightarrow X$ with $\psi \circ \varphi = \mathrm{id}_X$ and $\varphi \circ \psi = \mathrm{id}_Y$ as rational maps. Then $X$ and $Y$ are *birational*. A variety birational to $\mathbb{P}^n$ is *rational*.

Lean: Mathlib `AlgebraicGeometry.Scheme.Birational` (the existence of an isomorphism between dense open subschemes).

**Theorem P0.5.12 (birational equivalence and function fields).** The rule $X \mapsto k(X)$, $\varphi \mapsto \varphi^*$, is a contravariant equivalence from the category of varieties over $k$ with dominant rational maps to the category of finitely generated field extensions of $k$ with $k$-homomorphisms. In particular, $X$ and $Y$ are birational if and only if $k(X) \cong k(Y)$ over $k$, and this holds if and only if $X$ and $Y$ have isomorphic nonempty open subsets.

Lean: not in Lean as an equivalence of categories. Mathlib has `AlgebraicGeometry.Scheme.RationalMap.equivFunctionField`, which identifies the rational maps from an integral $X$ to $Y$ with the points of $Y$ over the function field of $X$.

*Proof.* The rule is a functor: $(\psi \circ \varphi)^* = \varphi^* \circ \psi^*$ holds on a dense open set, so it holds. A homomorphism of fields is injective, and $k(X)$ is finitely generated over $k$ by the coordinate functions of an affine open set. It remains to show that the functor is fully faithful and essentially surjective.

Essentially surjective. Let $K = k(t_1, \dots, t_n)$ be a finitely generated field extension of $k$. The $k$-algebra $B = k[t_1, \dots, t_n] \subset K$ is a domain of finite type, so $B \cong k[x_1, \dots, x_n]/\mathfrak{p}$ for a prime ideal $\mathfrak{p}$. Then $X = V(\mathfrak{p})$ is an affine variety with $k[X] \cong B$ by the Nullstellensatz, and $k(X) = \operatorname{Frac}(B) = K$.

Full. Every variety has a nonempty affine open subset, and restriction to it does not change the function field or the rational maps. So assume that $X$ and $Y$ are affine, with $Y \subset \mathbb{A}^m$ and $k[Y] = k[y_1, \dots, y_m]/I(Y)$. Let $\theta : k(Y) \to k(X)$ be a $k$-homomorphism. The functions $\theta(y_1), \dots, \theta(y_m)$ are regular on a nonempty open set $U \subset X$, the intersection of their domains. Define $\varphi_U : U \to \mathbb{A}^m$ by $\varphi_U = (\theta(y_1), \dots, \theta(y_m))$. For $g \in I(Y)$ the function $g \circ \varphi_U = g(\theta(y_1), \dots, \theta(y_m)) = \theta(g(y_1, \dots, y_m))$ is $\theta(0) = 0$. So $\varphi_U(U) \subset Y$. If $h \in k[Y]$ vanishes on $\varphi_U(U)$, then $\theta(h) = h \circ \varphi_U = 0$, and $h = 0$ because $\theta$ is injective. So $\varphi_U(U)$ is dense in $Y$, and $\varphi$ is dominant. By construction $\varphi^*$ and $\theta$ agree on the generators $y_i$ of $k(Y)$, so $\varphi^* = \theta$.

Faithful. If $\varphi^* = \psi^*$, then the coordinate functions $y_i \circ \varphi$ and $y_i \circ \psi$ are equal rational functions on $X$. So $\varphi$ and $\psi$ agree on a nonempty open set, and they are the same rational map.

An equivalence of categories sends isomorphisms to isomorphisms and back, so $X$ and $Y$ are birational exactly when $k(X) \cong k(Y)$. Suppose that $\varphi$ is birational with inverse $\psi$, that $\varphi$ is a morphism on $U$ and that $\psi$ is a morphism on $V$. The morphism $\psi \circ \varphi$ on $\varphi^{-1}(V) \subset U$ is the identity on a nonempty open set, so it is the inclusion $\varphi^{-1}(V) \to X$ by the lemma above. In the same way $\varphi \circ \psi$ is the inclusion on $\psi^{-1}(U) \subset V$. Put $U' = \varphi^{-1}(\psi^{-1}(U))$ and $V' = \psi^{-1}(\varphi^{-1}(V))$. These open sets are not empty, because $\varphi$ and $\psi$ are dominant. For $x \in U'$ the point $\varphi(x)$ lies in $\psi^{-1}(U)$, and $\psi(\varphi(x)) = x \in \varphi^{-1}(V)$, so $\varphi(x) \in V'$. So $\varphi$ maps $U'$ to $V'$, and in the same way $\psi$ maps $V'$ to $U'$. The two morphisms are inverse to each other. The converse is clear: an isomorphism of nonempty open subsets is a birational map. $\square$

### Proof in words

A rational map is fixed by finitely many rational functions, its coordinates. So a rational map into an affine variety is the same as a homomorphism of its coordinate ring into the function field, and dominance makes this homomorphism injective, so it extends to the fraction field. Every finitely generated field is the function field of the affine variety of its generators. There is no real difficulty: the work is in the bookkeeping of open sets, and the Nullstellensatz enters only to identify $k[X]$ with $B$.

### Examples

**Example P0.5.13.** The cuspidal cubic $C = V(y^2 - x^3)$ is rational. The morphism $\nu : \mathbb{A}^1 \to C$, $t \mapsto (t^2, t^3)$, is bijective, and its inverse on $C \setminus \{0\}$ is $(x, y) \mapsto y/x$. So $\nu$ is birational and $k(C) = k(t)$. But $\nu$ is not an isomorphism: $\nu^* : k[C] \to k[t]$ has image $k[t^2, t^3] \neq k[t]$. Birational varieties need not be isomorphic. The map $\nu$ is the normalization of $C$ (P1 and P3).

**Example P0.5.14.** Composition needs dominance. Let $\varphi : \mathbb{A}^1 \to \mathbb{A}^2$, $t \mapsto (t, 0)$, and $\psi : \mathbb{A}^2 \dashrightarrow \mathbb{A}^1$, $(x, y) \mapsto x/y$. The domain of definition of $\psi$ contains $\{y \neq 0\}$, and $\psi$ is not regular at any point of the line $y = 0$ other than the origin, since $y/x$ is regular and zero there. The image of $\varphi$ lies in $\{y = 0\}$, so $\psi \circ \varphi$ is not defined on any open set. Here $\varphi$ is not dominant, and the conclusion "$\varphi^*$ exists" fails with it: the function $1/y \in k(\mathbb{A}^2)$ has no pullback by $\varphi$.

### Exercises

1. (A) Show that the twisted cubic $\{(s^3 : s^2 t : s t^2 : t^3)\} \subset \mathbb{P}^3$ is rational, and find the inverse map on an open set.
2. (A) Show that a smooth conic $C \subset \mathbb{P}^2$ with a point $p$ is birational to $\mathbb{P}^1$ by the projection from $p$. Show that the projection extends to an isomorphism $C \to \mathbb{P}^1$.
3. (B) Show that $\mathbb{P}^1 \times \mathbb{P}^1$ and $\mathbb{P}^2$ are birational. Show that they are not isomorphic, using the fact that two curves in $\mathbb{P}^2$ always meet (Chapter 7).
4. (B) Let $X = V(x^2 + y^2 + z^2 - 1) \subset \mathbb{A}^3$, with $\operatorname{char} k \neq 2$. Show that the projection from $(0, 0, 1)$ to the plane $z = 0$ is birational, and write its inverse.
5. (B) Show that a dominant rational map $\varphi : X \dashrightarrow Y$ with $\dim X = \dim Y$ makes $k(X)$ a finite extension of $\varphi^* k(Y)$. Use the transcendence degree of Chapter 6.

### Lean

Mathlib has rational maps between schemes, `AlgebraicGeometry.Scheme.RationalMap`, with the domain of definition and the identification `AlgebraicGeometry.Scheme.RationalMap.equivFunctionField` with points over the function field. It has `AlgebraicGeometry.Scheme.Birational` for schemes with isomorphic dense open subschemes. The equivalence of categories of the theorem is not stated. The `MinimalModel` statements of tamnd/mmp-lean use birational morphisms of normal varieties, not rational maps, for the steps of the program.

### Notes and history

The theorem is classical, and its literature state is theorem. Hartshorne proves it as Theorem I.4.4 and Corollary I.4.5, and Reid treats it in Chapter 5. The minimal model program works inside one birational class: it replaces a variety by another variety with the same function field and a better canonical divisor (Chapter 2 of this volume, and Volume 0). The steps of the program, divisorial contractions and flips, are birational maps (Volume 1, Chapter 1).
