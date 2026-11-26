---
title: Morphisms and the affineness criterion
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch7, Har77:II.2, GW20:ch3]
requires: [P1.2, P3.1, P3.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Morphisms and the affineness criterion

### Statement

**Definition P3.3.1 (schemes over a base).** Let $S$ be a scheme. An *$S$-scheme* is a scheme $X$ with a morphism $X \to S$, the *structure morphism*. A *morphism of $S$-schemes* is a morphism $X \to Y$ that commutes with the structure morphisms. Write $\mathsf{Sch}/S$ for this category and $\operatorname{Hom}_S(X, Y)$ for its sets of morphisms. For a ring $R$, an *$R$-scheme* is a $\operatorname{Spec} R$-scheme, that is, by Theorem P3.1.22, a scheme with an $R$-algebra structure on $\mathcal{O}_X$. For an $S$-scheme $T$, the set $X(T) = \operatorname{Hom}_S(T, X)$ is the set of *$T$-points of $X$ over $S$*.

Every scheme is a $\mathbb{Z}$-scheme in exactly one way, by Example P3.1.29, so $\mathsf{Sch} = \mathsf{Sch}/\operatorname{Spec} \mathbb{Z}$.

**Proposition P3.3.2 (morphisms are locally ring maps).** Let $f \colon X \to Y$ be a morphism of schemes and $x \in X$. For every affine open $V = \operatorname{Spec} A$ that contains $f(x)$ there is an affine open $U = \operatorname{Spec} B$ that contains $x$ with $f(U) \subseteq V$, and then $f|_U = \operatorname{Spec} \varphi$ for the ring map $\varphi = f^\#_V$ followed by restriction, $A \to \mathcal{O}_X(f^{-1}V) \to B$.

Lean: Mathlib proves this through `AlgebraicGeometry.ΓSpec.adjunction`; the statement as given is not in Lean as stated.

**Lemma P3.3.3 (sections over the locus where a function does not vanish).** Let $X$ be a scheme, $f \in \Gamma(X, \mathcal{O}_X)$ and $X_f = \{x \in X : f(x) \neq 0\}$, an open set.

1. If $X$ is quasi-compact and $s \in \Gamma(X, \mathcal{O}_X)$ has $s|_{X_f} = 0$, then $f^n s = 0$ for some $n \geq 0$.
2. If $X$ has a finite cover by affine open sets $U_1, \dots, U_r$ such that every $U_i \cap U_j$ is quasi-compact, then the map $\Gamma(X, \mathcal{O}_X)_f \to \Gamma(X_f, \mathcal{O}_X)$ is an isomorphism.

Lean: Mathlib `AlgebraicGeometry.isLocalization_basicOpen_of_qcqs` for part 2 (proved in Mathlib).

**Theorem P3.3.4 (affineness criterion).** Let $X$ be a scheme and $B = \Gamma(X, \mathcal{O}_X)$. Let $f_1, \dots, f_r \in B$ generate the unit ideal, and assume that every $X_{f_i}$ is affine. Then $X$ is affine.

Lean: Mathlib `AlgebraicGeometry.isAffine_of_isAffineOpen_basicOpen` (proved in Mathlib).

### Proof in words

A morphism is a map of locally ringed spaces, and over an affine open set Theorem P3.1.22 makes it a ring map. So every local question about morphisms is a question about ring maps.

The lemma on $X_f$ says that functions on $X_f$ are fractions $s/f^n$ of global functions, as on $D(f) \subseteq \operatorname{Spec} A$. The proof covers $X$ by affine sets, uses Corollary P3.1.5 on each, and needs finiteness twice: once to choose one exponent $n$ for all charts, and once more on the overlaps.

The affineness criterion compares $X$ with $\operatorname{Spec} B$ through the canonical morphism $c_X$ of Corollary P3.1.24. The preimage of $D(f_i)$ is $X_{f_i}$, and by the lemma the map $X_{f_i} \to D(f_i)$ is the morphism of affine schemes of the isomorphism $B_{f_i} \to \Gamma(X_{f_i})$. So $c_X$ is an isomorphism over each $D(f_i)$, and these sets cover $\operatorname{Spec} B$.

### Examples

**Example P3.3.5 (the criterion needs the unit ideal).** Let $U = \mathbb{A}^2_k \setminus \{0\}$. Then $\Gamma(U, \mathcal{O}) = k[x, y]$ by Example P3.1.10, and $U_x = D(x)$, $U_y = D(y)$ are affine. But $x, y$ generate the ideal $(x, y)$, not the unit ideal, and $U$ is not affine. The open sets $U_x$ and $U_y$ cover $U$, so the condition on the ideal is not a condition on the cover.

**Example P3.3.6 (the lemma needs finiteness).** Let $X = \bigsqcup_{n \geq 1} \operatorname{Spec} k[t]$ and $f = (t, t, \dots) \in \Gamma(X, \mathcal{O}) = \prod_n k[t]$. Then $X_f = \bigsqcup_n \operatorname{Spec} k[t, t^{-1}]$ and $\Gamma(X_f) = \prod_n k[t, t^{-1}]$. The element $(t^{-1}, t^{-2}, t^{-3}, \dots)$ is not of the form $s/f^m$, since that would need the bound $m$ on the exponents. So $\Gamma(X)_f \to \Gamma(X_f)$ is not surjective. Part 1 also fails without quasi-compactness. On $Y = \bigsqcup_{n \geq 1} \operatorname{Spec} k[t]/(t^n)$ the function $f = (t, t, \dots)$ vanishes at every point, so $Y_f = \emptyset$ and $s = 1$ restricts to $0$ on $Y_f$. But $f^m \cdot 1 \neq 0$ for every $m$, since $t^m \neq 0$ in $k[t]/(t^n)$ for $n > m$.

**Example P3.3.7 (points over a base).** Let $S = \operatorname{Spec} \mathbb{R}$ and $X = \operatorname{Spec} \mathbb{R}[x, y]/(x^2 + y^2 + 1)$. Then $X(\mathbb{R}) = \emptyset$, since $a^2 + b^2 + 1 > 0$ for real $a, b$, while $X(\mathbb{C})$ is the complex conic. The scheme $X$ is not empty: its closed points have residue field $\mathbb{C}$. Over the base $\operatorname{Spec} \mathbb{C}$, the scheme $\operatorname{Spec} \mathbb{C}$ has two $\mathbb{R}$-morphisms to itself, the identity and complex conjugation, and only one $\mathbb{C}$-morphism. So the set of morphisms depends on the base.

**Example P3.3.8 (a morphism to projective space).** Let $k$ be a field. The morphism $\nu \colon \mathbb{P}^1_k \to \mathbb{P}^2_k$, $[s : t] \mapsto [s^2 : st : t^2]$, is given on the chart $U_0 = \operatorname{Spec} k[t/s]$ of $\mathbb{P}^1$ by the ring map from the chart $\operatorname{Spec} k[x_1/x_0, x_2/x_0]$ of $\mathbb{P}^2$ with $x_1/x_0 \mapsto t/s$ and $x_2/x_0 \mapsto (t/s)^2$, and on the chart $U_1$ in the same way through the chart where $x_2 \neq 0$. The two morphisms agree on $U_0 \cap U_1$, so they glue by Proposition P3.2.4. Its image is the conic $x_0 x_2 = x_1^2$ of Exercise 6 of Section 2.2. This is the Veronese map of Chapter 10.

### Proof

*Proof of Proposition P3.3.2.* The set $f^{-1}(V)$ is an open neighbourhood of $x$, and it contains an affine open neighbourhood $U$ of $x$ by Proposition P3.2.2. Then $f|_U \colon U \to V$ is a morphism of affine schemes, so it is $\operatorname{Spec}$ of its map on global sections by Corollary P3.1.23, and this map is the composite of $f^\#_V$ with the restriction to $U$. $\square$

*Proof of Lemma P3.3.3.* The set $X_f$ is open by Proposition P3.1.14. On an affine open $U = \operatorname{Spec} A$, with $g = f|_U \in A$, $X_f \cap U = D(g)$, since $f(\mathfrak{p}) = 0$ means $g \in \mathfrak{p}$.

Part 1. Cover $X$ by finitely many affine open sets $U_i = \operatorname{Spec} A_i$ and write $g_i = f|_{U_i}$, $s_i = s|_{U_i}$. Then $s_i$ restricts to $0$ in $\mathcal{O}(D(g_i)) = (A_i)_{g_i}$ by Corollary P3.1.5, so $g_i^{n_i} s_i = 0$ in $A_i$ for some $n_i$. With $n = \max_i n_i$, $f^n s$ restricts to $0$ on every $U_i$, so $f^n s = 0$.

Part 2. Write $B = \Gamma(X, \mathcal{O}_X)$. Since $f$ is a unit on $X_f$ by Proposition P3.1.14, the restriction $B \to \Gamma(X_f)$ extends to $\beta \colon B_f \to \Gamma(X_f)$. It is injective: if $s/f^m$ maps to $0$, then $s|_{X_f} = 0$, so $f^n s = 0$ by part 1, and $s/f^m = 0$ in $B_f$.

It is surjective. Let $t \in \Gamma(X_f)$. On $U_i = \operatorname{Spec} A_i$, $t|_{D(g_i)} = a_i/g_i^{m}$ with $a_i \in A_i$, where one $m$ works for all $i$ since there are finitely many. So the sections $a_i \in A_i$ satisfy $a_i|_{D(g_i)} = f^m t|_{D(g_i)}$. On $U_i \cap U_j$, the section $a_i - a_j$ restricts to $0$ on $(U_i \cap U_j)_f$. The scheme $U_i \cap U_j$ is quasi-compact by hypothesis, so part 1 for $U_i \cap U_j$ gives $f^{p}(a_i - a_j) = 0$ on $U_i \cap U_j$, with one $p$ for all pairs. So the sections $f^p a_i$ agree on overlaps and glue to $s \in B$, with $s|_{X_f} = f^{p + m} t$. So $t = \beta(s/f^{p+m})$. $\square$

*Proof of Theorem P3.3.4.* The sets $X_{f_i}$ cover $X$: at each $x$, the values $f_i(x)$ generate the unit ideal of $\kappa(x)$, so some $f_i(x) \neq 0$. So $X$ is a finite union of the affine open sets $X_{f_i}$. Their intersections $X_{f_i} \cap X_{f_j} = (X_{f_i})_{f_j}$ are basic open sets of the affine schemes $X_{f_i}$, so they are affine and quasi-compact. By part 2 of Lemma P3.3.3, $B_{f_i} \to \Gamma(X_{f_i})$ is an isomorphism for every $i$.

Let $c = c_X \colon X \to \operatorname{Spec} B$ be the morphism of Corollary P3.1.24, with $c(x) = \{s \in B : s(x) = 0\}$. Then $c^{-1}(D(f_i)) = X_{f_i}$. The restriction $c_i \colon X_{f_i} \to D(f_i) = \operatorname{Spec} B_{f_i}$ is a morphism between affine schemes. Its map on global sections is the map $B_{f_i} \to \Gamma(X_{f_i})$ that extends the restriction from $B$, by the naturality in Theorem P3.1.22, and this is the isomorphism above. By Corollary P3.1.23, $c_i$ is an isomorphism. Since $f_1, \dots, f_r$ generate the unit ideal of $B$, the sets $D(f_i)$ cover $\operatorname{Spec} B$. A morphism that is an isomorphism over each set of an open cover of the target, with these sets pulled back to a cover of the source, is a homeomorphism and an isomorphism of sheaves, so it is an isomorphism. So $c$ is an isomorphism, and $X$ is affine. $\square$

### Exercises

1. (A) Let $k$ be a field. Show that a morphism of $k$-schemes $\operatorname{Spec} k \to X$ is the same as a point $x \in X$ with $\kappa(x) = k$, and that such a point is closed if $X$ is of finite type over $k$.
2. (A) Let $X$ be a scheme and $f \in \Gamma(X, \mathcal{O}_X)$. Show that $X_f = \emptyset$ if and only if $f$ is locally nilpotent, and that $X_f = X$ if and only if $f$ is a unit.
3. (A) Show that the morphism $\mathbb{A}^1_k \to \mathbb{A}^2_k$, $t \mapsto (t^2, t^3)$, factors through the cuspidal cubic, and write it as $\operatorname{Spec}$ of a ring map. Do the same for $t \mapsto (t^2 - 1, t(t^2 - 1))$ and the nodal cubic.
4. (B) Let $X$ be a quasi-compact scheme with $\Gamma(X, \mathcal{O}_X) = B$ such that every point lies in an affine set $X_f$ with $f \in B$. Show that $X$ is affine. (Show that the $f$ needed generate the unit ideal: otherwise they lie in a maximal ideal $\mathfrak{m}$ of $B$, and derive a contradiction with the covering.)
5. (B) Let $X = \operatorname{Spec} A \sqcup \operatorname{Spec} B$. Use Theorem P3.3.4 with the idempotents $(1, 0)$ and $(0, 1)$ of $\Gamma(X) = A \times B$ to show again that $X \cong \operatorname{Spec}(A \times B)$.
6. (B) Show that the affine line with a doubled origin satisfies the hypothesis of part 2 of Lemma P3.3.3, so that $\Gamma(X_f) = k[x]_f$ for every $f \in k[x]$. Explain why this does not contradict Theorem P3.3.4. (Which $f$ make $X_f$ affine?)
7. (C) Let $X$ be a scheme and $B = \Gamma(X, \mathcal{O}_X)$. Show that $X$ is affine if and only if $X$ is quasi-compact, every intersection of two affine open sets is quasi-compact, and there are $f_1, \dots, f_r \in B$ generating the unit ideal with every $X_{f_i}$ affine. Find a quasi-compact scheme in which two affine open sets meet in a set that is not quasi-compact. (Glue two copies of $\operatorname{Spec} k[x_1, x_2, \dots]$ along the complement of the origin.)

### Lean

Mathlib proves the localization statement for quasi-compact and quasi-separated opens as `AlgebraicGeometry.isLocalization_basicOpen_of_qcqs`, and the affineness criterion as `AlgebraicGeometry.isAffine_of_isAffineOpen_basicOpen`, tagged with the Stacks project. Proposition P3.3.2 is not in Lean as stated; it follows from the adjunction `AlgebraicGeometry.ΓSpec.adjunction`. The handbook adds no `MinimalModel` node here.

### Notes and history

The affineness criterion is in EGA I, Chapter I, and Hartshorne states it as an exercise in Section II.2 together with Lemma P3.3.3. Vakil proves it in the chapter on morphisms and calls the hypothesis of part 2 "quasi-separated", a word Chapter 4 defines. The literature state is theorem. The criterion is the tool that shows in Section 3.4 that affine morphisms can be checked on one affine cover of the target, and in Chapter 5 it is the base of the cohomological criterion of Serre for affineness.
