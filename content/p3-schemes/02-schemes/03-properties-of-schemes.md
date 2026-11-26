---
title: Properties of schemes and varieties
nodes: []
sources: [Vak25, Har77, GW20, Stacks]
reads_with: [Vak25:ch5, Har77:II.3, GW20:ch3]
requires: [P1.2, P1.3, P1.4, P3.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Properties of schemes and varieties

### Statement

**Definition P3.2.19 (first properties).** A scheme $X$ is

1. *quasi-compact* if its space is quasi-compact, that is, if $X$ is a finite union of affine open sets;
2. *reduced* if $\mathcal{O}_X(U)$ has no nonzero nilpotents for every open $U$, or equivalently if every local ring $\mathcal{O}_{X, x}$ is reduced;
3. *irreducible* if its space is irreducible, and *connected* if its space is connected;
4. *integral* if $X \neq \emptyset$ and $\mathcal{O}_X(U)$ is a domain for every nonempty open $U$;
5. *locally Noetherian* if $X$ has a cover by open sets $\operatorname{Spec} A_i$ with every $A_i$ Noetherian, and *Noetherian* if it is locally Noetherian and quasi-compact.

Lean: Mathlib `AlgebraicGeometry.IsReduced`, `AlgebraicGeometry.IsIntegral`, `AlgebraicGeometry.IsLocallyNoetherian` and `AlgebraicGeometry.IsNoetherian`; quasi-compactness of the space is `CompactSpace`.

**Theorem P3.2.20 (generic points).** Let $X$ be a scheme. Every irreducible closed subset $Z \subseteq X$ has exactly one point $\eta$ with $\overline{\{\eta\}} = Z$, the *generic point* of $Z$. So $x \mapsto \overline{\{x\}}$ is a bijection from the points of $X$ to its irreducible closed subsets.

Lean: Mathlib proves that the space of a scheme is quasi-sober and $T_0$ (instances in `Mathlib/AlgebraicGeometry/Properties.lean`); the generic point is `genericPoint`, with `genericPoint_spec` (proved in Mathlib).

**Proposition P3.2.21 (integral is reduced and irreducible).** A scheme is integral if and only if it is reduced and irreducible.

Lean: Mathlib `AlgebraicGeometry.isIntegral_iff_irreducibleSpace_and_isReduced` (proved in Mathlib).

**Lemma P3.2.22 (affine communication lemma).** Let $P$ be a property of rings with these two properties: if $A$ has $P$ then $A_f$ has $P$ for every $f \in A$; and if $f_1, \dots, f_r \in A$ generate the unit ideal and every $A_{f_i}$ has $P$, then $A$ has $P$. Let $X$ be a scheme with an affine open cover $X = \bigcup_i \operatorname{Spec} A_i$ in which every $A_i$ has $P$. Then $B$ has $P$ for every affine open set $\operatorname{Spec} B \subseteq X$.

Lean: Mathlib `AlgebraicGeometry.of_affine_open_cover`, with the key step `AlgebraicGeometry.exists_basicOpen_le_affine_inter` (proved in Mathlib).

**Proposition P3.2.23 (Noetherian is local).** Let $X$ be a locally Noetherian scheme. Then $\mathcal{O}_X(U)$ is Noetherian for every affine open $U$. In particular $\operatorname{Spec} A$ is locally Noetherian if and only if $A$ is Noetherian. The space of a Noetherian scheme is a Noetherian space.

Lean: Mathlib `AlgebraicGeometry.isNoetherianRing_of_away` for the gluing step and `AlgebraicGeometry.isLocallyNoetherian_of_affine_cover` (proved in Mathlib).

**Proposition P3.2.24 (the function field).** Let $X$ be an integral scheme with generic point $\eta$. The local ring $K(X) = \mathcal{O}_{X, \eta}$ is a field, the *function field* of $X$. For every nonempty affine open $\operatorname{Spec} A \subseteq X$, $K(X) = \operatorname{Frac}(A)$. For every nonempty open $U$, the map $\mathcal{O}_X(U) \to K(X)$ is injective, and for nonempty opens $V \subseteq U$ the restriction $\mathcal{O}_X(U) \to \mathcal{O}_X(V)$ is injective.

Lean: Mathlib `AlgebraicGeometry.Scheme.functionField` and `AlgebraicGeometry.germ_injective_of_isIntegral` (proved in Mathlib).

**Definition P3.2.25 (schemes of finite type and varieties).** Let $k$ be a field. A *scheme over $k$* is a scheme $X$ with a morphism $X \to \operatorname{Spec} k$, that is, by Example P3.1.29, a $k$-algebra structure on $\mathcal{O}_X$. It is *locally of finite type* over $k$ if it has an affine open cover by spectra of finitely generated $k$-algebras, and *of finite type* if this cover can be taken finite. A *variety over $k$* is an integral separated scheme of finite type over $k$. Separatedness is defined in Chapter 4; it excludes the doubled origin of Example P3.2.5.

Lean: Mathlib `AlgebraicGeometry.LocallyOfFiniteType` and `AlgebraicGeometry.IsSeparated` for the structure morphism; the handbook definition of a variety is not in Lean as stated.

### Proof in words

A point of $\operatorname{Spec} A$ is a prime, and its closure is the set of primes that contain it, so the irreducible closed subsets of $\operatorname{Spec} A$ are the sets $V(\mathfrak{p})$, each with one generic point. For a scheme the same holds, because an irreducible closed set meets some affine open set in a dense subset. Points of schemes are therefore not only the closed points of classical geometry: every subvariety has its own point.

The affine communication lemma lets one define a property of schemes by a property of rings that is local in the sense of the lemma. The key step is that the intersection of two affine open sets is covered by open sets that are basic in both. The lemma applies to being Noetherian, reduced and finitely generated over $k$, and the later chapters use it for normality, regularity and many properties of morphisms.

### Examples

**Example P3.2.26 (generic points of the plane).** The scheme $\mathbb{A}^2_k$ has three kinds of points: the closed points, the generic points of the irreducible curves $V(f)$ with $f$ irreducible, and the generic point $(0)$ of the plane. The closure of the generic point $(y)$ of the $x$-axis is the axis, and $(y)$ lies in every nonempty open subset of the axis. A morphism from $\mathbb{A}^2_k$ to a scheme $Y$ sends the generic point of a curve to the generic point of the closure of its image.

**Example P3.2.27 (reduced and not irreducible, irreducible and not reduced).** The scheme $\operatorname{Spec} k[x, y]/(xy)$ is reduced and not irreducible: it has two irreducible components, and $\Gamma = k[x, y]/(xy)$ has the zero divisor $x$. The scheme $\operatorname{Spec} k[x]/(x^2)$ is irreducible and not reduced, and $\operatorname{Spec} k[x, y]/(y^2)$, the double line of Example P3.1.40, is irreducible, not reduced, and has function ring with the zero divisor $y$. So neither condition of Proposition P3.2.21 can be dropped.

**Example P3.2.28 (an integral scheme that is not Noetherian).** The ring $A = k[x_1, x_2, \dots]$ is a domain that is not Noetherian, since the chain $(x_1) \subset (x_1, x_2) \subset \cdots$ does not stop. So $\operatorname{Spec} A$ is integral, quasi-compact and not Noetherian. Its point $(x_1, x_2, \dots)$ is closed, with local ring of infinite dimension. Schemes of this kind do not appear in the program, which works with schemes of finite type over a field.

**Example P3.2.29 (a locally Noetherian scheme that is not Noetherian).** The disjoint union $\bigsqcup_{n \in \mathbb{N}} \operatorname{Spec} k$ is locally Noetherian and not quasi-compact, so not Noetherian. A Noetherian scheme has finitely many irreducible components by Theorem P1.3.19.

**Example P3.2.30 (the doubled origin is a scheme of finite type).** The affine line with a doubled origin of Example P3.2.5 is integral and of finite type over $k$, with function field $k(x)$, but it is not a variety in the sense of the handbook: Chapter 4 shows that it is not separated. Projective space $\mathbb{P}^n_k$ is a variety: it is of finite type with the $n + 1$ charts, integral since it is covered by the integral open sets $U_i$ that pairwise meet (Exercise 4), and separated by Chapter 4.

**Example P3.2.31 (the function field of projective space).** By Proposition P3.2.24 and the chart $U_0$, $K(\mathbb{P}^n_k) = k(x_1/x_0, \dots, x_n/x_0)$. In the homogeneous coordinates of Section 2.2, it is the field of fractions $G/H$ with $G, H$ homogeneous of the same degree and $H \neq 0$. A rational function on $\mathbb{P}^n$ in the sense of P0 is an element of this field.

### Proof

*Proof of Theorem P3.2.20.* Existence. Let $Z$ be an irreducible closed subset and $U = \operatorname{Spec} A$ an affine open set with $U \cap Z \neq \emptyset$. A nonempty open subset of an irreducible space is irreducible and dense, so $U \cap Z$ is irreducible and its closure in $X$ is $Z$. It is closed in $U$, so $U \cap Z = V(I)$ for an ideal $I$ with $\sqrt{I}$ prime, since $V(I)$ is irreducible exactly when $\sqrt{I}$ is prime (P1 Ch. 2). Let $\mathfrak{p} = \sqrt{I}$. The closure of $\mathfrak{p}$ in $U$ is $V(\mathfrak{p}) = U \cap Z$ by Proposition P1.2.18. So the closure of $\mathfrak{p}$ in $X$ contains $U \cap Z$, and it is $Z$.

Uniqueness. Let $\eta, \eta'$ be two generic points of $Z$. A point whose closure is $Z$ lies in every nonempty open subset of $Z$: if $W$ is open in $Z$ and misses $\eta$, then $Z \setminus W$ is a closed set that contains $\eta$, hence contains $Z$, so $W = \emptyset$. So $\eta$ and $\eta'$ both lie in $U \cap Z$, and both are generic points of the irreducible closed subset $U \cap Z$ of $\operatorname{Spec} A$. By Proposition P1.2.18, $\overline{\{\mathfrak{q}\}} = V(\mathfrak{q})$ in $\operatorname{Spec} A$, and $V(\mathfrak{q}) = V(\mathfrak{q}')$ for primes implies $\mathfrak{q} = \mathfrak{q}'$, since each is the smallest element of its $V$. So $\eta = \eta'$. $\square$

*Proof of Proposition P3.2.21.* Let $X$ be integral. Every $\mathcal{O}_X(U)$ is a domain or zero, so it is reduced. If $X$ were reducible, there would be nonempty disjoint open sets $U_1, U_2$: write $X = Z_1 \cup Z_2$ with proper closed $Z_i$ and take $U_i = X \setminus Z_{3-i}$. Then $\mathcal{O}_X(U_1 \sqcup U_2) = \mathcal{O}_X(U_1) \times \mathcal{O}_X(U_2)$ is a product of two nonzero rings, which has the zero divisor $(1, 0)$. Here $\mathcal{O}_X(U_i) \neq 0$, since $U_i$ contains a point with a local ring and $1 \neq 0$ there. This contradicts integrality.

Conversely, let $X$ be reduced and irreducible, $U$ nonempty open and $f, g \in \mathcal{O}_X(U)$ with $fg = 0$. Then $U$ is irreducible. For $s \in \mathcal{O}_X(U)$ let $V(s) = \{x \in U : s(x) = 0\}$, which is closed by Proposition P3.1.14. Then $U = V(f) \cup V(g)$, since $f(x) g(x) = 0$ in the field $\kappa(x)$. So $U = V(f)$, say. On an affine open $\operatorname{Spec} A \subseteq U$, $f|_{\operatorname{Spec} A} \in A$ vanishes at every point, so it is nilpotent by Proposition P3.1.14, and it is $0$ since $A$ is reduced. The affine open sets cover $U$, so $f = 0$. And $\mathcal{O}_X(U) \neq 0$ since $U \neq \emptyset$. So $\mathcal{O}_X(U)$ is a domain. $\square$

*Proof of Lemma P3.2.22.* Step 1. Let $\operatorname{Spec} A$ and $\operatorname{Spec} B$ be affine open sets of $X$ and $x \in \operatorname{Spec} A \cap \operatorname{Spec} B$. There is an open set $W \ni x$ that is basic in both. Choose $f \in A$ with $x \in D_A(f) \subseteq \operatorname{Spec} A \cap \operatorname{Spec} B$, and then $g \in B$ with $x \in D_B(g) \subseteq D_A(f)$. The restriction of $g$ to the affine scheme $D_A(f) = \operatorname{Spec} A_f$ is an element $a/f^m$ of $A_f$. The set $D_B(g)$ is the set of points of $\operatorname{Spec} B$ where $g$ does not vanish. Since $D_B(g) \subseteq D_A(f)$, it is the set of points of $\operatorname{Spec} A_f$ where $a/f^m$ does not vanish, which is $D_A(af)$. So $W = D_B(g) = D_A(af)$ works.

Step 2. Let $\operatorname{Spec} B \subseteq X$ be an affine open set. Each point of $\operatorname{Spec} B$ lies in some $\operatorname{Spec} A_i$, and by step 1 in some $W = D_{A_i}(h) = D_B(g)$. By the first hypothesis $(A_i)_h$ has $P$, and $(A_i)_h \cong \mathcal{O}_X(W) \cong B_g$ by Proposition P3.1.13. So $\operatorname{Spec} B$ is covered by sets $D_B(g)$ with $B_g$ having $P$. Since $\operatorname{Spec} B$ is quasi-compact, finitely many $D_B(g_1), \dots, D_B(g_r)$ cover it, and then $(g_1, \dots, g_r) = B$ by Proposition P1.2.17. By the second hypothesis $B$ has $P$. $\square$

*Proof of Proposition P3.2.23.* Apply Lemma P3.2.22 to the property "Noetherian". Localizations of Noetherian rings are Noetherian (P1 Ch. 3). For the second hypothesis, let $(f_1, \dots, f_r) = A$ with every $A_{f_i}$ Noetherian, and let $I_1 \subseteq I_2 \subseteq \cdots$ be ideals of $A$. For an ideal $I$, $I = \{a \in A : a/1 \in I A_{f_i} \text{ for all } i\}$: if $a/1 \in I A_{f_i}$ for all $i$, then $f_i^{m} a \in I$ for some $m$ that works for all $i$; the elements $f_i^m$ generate the unit ideal, since $D(f_i^m) = D(f_i)$; so $1 = \sum c_i f_i^m$ and $a = \sum c_i f_i^m a \in I$. The chains $I_n A_{f_i}$ stop for each $i$, so the chain $I_n$ stops. So $A$ is Noetherian. If $X$ is Noetherian, it is a finite union of spaces $\operatorname{Spec} A_i$ with $A_i$ Noetherian. Each is a Noetherian space by P1 Ch. 3, and a finite union of Noetherian open subspaces is Noetherian: a descending chain of closed sets stops on each piece. $\square$

*Proof of Proposition P3.2.24.* Let $U = \operatorname{Spec} A$ be a nonempty affine open set. By Proposition P3.2.21 and the definition, $A$ is a domain. The generic point of $X$ lies in $U$, as in the proof of Theorem P3.2.20, and it is the generic point $(0)$ of $\operatorname{Spec} A$. So $\mathcal{O}_{X, \eta} = A_{(0)} = \operatorname{Frac}(A)$ by Theorem P3.1.11. For the injectivity, let $U$ be nonempty open and $s \in \mathcal{O}_X(U)$ with germ $0$ at $\eta$. For each affine open $\operatorname{Spec} A \subseteq U$, the restriction of $s$ is an element of $A$ with image $0$ in $\operatorname{Frac}(A)$, so it is $0$. The affine open sets cover $U$, so $s = 0$. For $V \subseteq U$, the germ at $\eta \in V$ of $s|_V$ is the germ of $s$, so restriction is injective too. $\square$

### Exercises

1. (A) Show that a scheme $X$ is reduced if and only if every local ring $\mathcal{O}_{X, x}$ is reduced, and that $X$ is reduced if it has an affine open cover by spectra of reduced rings.
2. (A) Show that $\operatorname{Spec} \mathbb{Z}$ and $\mathbb{A}^n_\mathbb{Z}$ are integral and Noetherian, and identify the generic point and function field of each.
3. (A) Show that every nonempty quasi-compact scheme has a closed point. (Take a closed point of an affine chart, and use quasi-compactness to reduce to finitely many charts.)
4. (B) Let $X$ be a scheme with an open cover by integral open sets $U_i$ such that $U_i \cap U_j \neq \emptyset$ for all $i, j$. Show that $X$ is irreducible, and hence integral by Proposition P3.2.21 and Exercise 1.
5. (B) Show that the property "finitely generated $k$-algebra" satisfies the two hypotheses of Lemma P3.2.22. Conclude that if $X$ is locally of finite type over $k$, then $\mathcal{O}_X(U)$ is a finitely generated $k$-algebra for every affine open $U$. (For the second hypothesis, take generators of each $A_{f_i}$ of the form $a/f_i^m$, and show that the elements $a$, $f_i$ and $c_i$ with $\sum c_i f_i = 1$ generate $A$.)
6. (B) Let $X$ be a scheme of finite type over $k$. Show that a point $x$ is closed if and only if $\kappa(x)$ is finite over $k$. (Use Theorem P1.4.30 on an affine chart, and show that a point closed in every affine chart that contains it is closed in $X$.)
7. (C) Let $X$ be a Noetherian scheme. Show that $X$ has finitely many irreducible components and that their generic points are the points $\eta$ with $\dim \mathcal{O}_{X, \eta} = 0$. Show that $X$ is connected if and only if its components cannot be split into two nonempty families with no common point.

### Lean

Mathlib has the classes `AlgebraicGeometry.IsReduced`, `AlgebraicGeometry.IsIntegral`, `AlgebraicGeometry.IsLocallyNoetherian` and `AlgebraicGeometry.IsNoetherian`. Proposition P3.2.21 is `AlgebraicGeometry.isIntegral_iff_irreducibleSpace_and_isReduced`. The affine communication lemma is `AlgebraicGeometry.of_affine_open_cover`, whose docstring names Vakil's lemma, and Proposition P3.2.23 rests on `AlgebraicGeometry.isNoetherianRing_of_away`, whose docstring cites Hartshorne. The function field is `AlgebraicGeometry.Scheme.functionField`, with `AlgebraicGeometry.germ_injective_of_isIntegral`. Generic points are `genericPoint` for quasi-sober spaces. The handbook adds no `MinimalModel` node here.

### Notes and history

Integral schemes, generic points and function fields are in EGA I, Chapter I. Hartshorne proves Propositions P3.2.21 and P3.2.23 in Section II.3, and Vakil names the affine communication lemma in Chapter 5. The literature state of every statement is theorem. The handbook definition of a variety follows the convention of the guide: integral, separated and of finite type over $k$. Some references drop integrality or separatedness, and Hartshorne in Section II.4 requires $k$ algebraically closed. The program works with varieties, with normal varieties from Chapter 7 on, and with schemes of finite type over a field when it needs non-reduced fibres.
