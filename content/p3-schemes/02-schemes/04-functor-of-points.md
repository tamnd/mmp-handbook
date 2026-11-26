---
title: The functor of points
nodes: []
sources: [Vak25, GW20, EGA1, Stacks, Mum99]
reads_with: [Vak25:ch6, GW20:ch4, Mum99:II.6]
requires: [P2.1, P3.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The functor of points

### Statement

**Definition P3.2.32 (functor of points).** Let $X$ be a scheme. The *functor of points* of $X$ is $h_X = \operatorname{Hom}_{\mathsf{Sch}}(-, X) \colon \mathsf{Sch}^{\mathrm{op}} \to \mathsf{Set}$. For a scheme $T$, an element of $X(T) = h_X(T)$ is a *$T$-point* of $X$. For a ring $R$, write $X(R) = X(\operatorname{Spec} R)$; then $R \mapsto X(R)$ is a functor $\mathsf{Ring} \to \mathsf{Set}$, since $\operatorname{Spec}$ reverses arrows. Over a base scheme $S$, the same definitions in the category $\mathsf{Sch}/S$ of $S$-schemes give $X(T)$ for $S$-schemes $T$.

**Theorem P3.2.33 (Yoneda for schemes).** The functor $X \mapsto h_X$ from $\mathsf{Sch}$ to functors $\mathsf{Sch}^{\mathrm{op}} \to \mathsf{Set}$ is fully faithful. In particular, schemes $X$ and $Y$ are isomorphic if and only if $h_X \cong h_Y$, and every natural transformation $h_X \to h_Y$ is $h_f$ for exactly one morphism $f \colon X \to Y$.

Lean: Mathlib `CategoryTheory.yoneda` and `CategoryTheory.Yoneda.fullyFaithful` (proved in Mathlib, for any category).

**Theorem P3.2.34 (affine points are enough).** The functor that sends a scheme $X$ to the functor $R \mapsto X(R)$ on rings is fully faithful. So a scheme is determined by its points with values in all rings, and a morphism $X \to Y$ is the same as a family of maps $X(R) \to Y(R)$, natural in $R$.

Lean: not in Lean as stated.

**Proposition P3.2.35 (the Zariski sheaf property).** Let $X$ be a scheme, $R$ a ring and $f_1, \dots, f_r \in R$ elements that generate the unit ideal. Then the sequence
$$X(R) \to \prod_i X(R_{f_i}) \rightrightarrows \prod_{i, j} X(R_{f_i f_j})$$
is an equalizer: a family $(t_i) \in \prod_i X(R_{f_i})$ comes from an element of $X(R)$ if and only if $t_i$ and $t_j$ have the same image in $X(R_{f_i f_j})$ for all $i, j$, and then it comes from exactly one element.

Lean: not in Lean as stated. The underlying fact is Proposition P3.2.4, which is `AlgebraicGeometry.Scheme.Cover.glueMorphisms` with `AlgebraicGeometry.Scheme.Cover.hom_ext`.

### Proof in words

Theorem P3.2.33 is Corollary P2.1.24 for the category of schemes. The content of Theorem P3.2.34 is that schemes are glued from affine schemes, so the maps out of a scheme are glued from maps out of affine schemes. A natural family of maps $X(R) \to Y(R)$ acts on the inclusion of each affine chart $\operatorname{Spec} A_i \subseteq X$, an element of $X(A_i)$, and gives morphisms $\operatorname{Spec} A_i \to Y$. Naturality, applied to affine open sets of the overlaps, shows that these morphisms agree on overlaps, and Proposition P3.2.4 glues them.

The Zariski sheaf property says that a functor on rings that comes from a scheme satisfies a gluing condition. The Grassmannian and the Hilbert scheme are constructed in Chapter 13 and in P8 by first checking this condition for a functor and then covering the functor by affine pieces.

### Examples

**Example P3.2.36 (affine space and the multiplicative group).** By Example P3.1.30, $\mathbb{A}^n_\mathbb{Z}(T) = \Gamma(T, \mathcal{O}_T)^n$ for every scheme $T$. By Exercise 4 of Section 1.3, $\mathbb{G}_m(T) = \Gamma(T, \mathcal{O}_T)^\times$, for $\mathbb{G}_m = \operatorname{Spec} \mathbb{Z}[x, x^{-1}]$. The multiplication of the ring $\Gamma(T, \mathcal{O}_T)$ and of its unit group is natural in $T$, so by Theorem P3.2.33 it is given by morphisms $\mathbb{A}^1 \times \mathbb{A}^1 \to \mathbb{A}^1$ and $\mathbb{G}_m \times \mathbb{G}_m \to \mathbb{G}_m$, once Chapter 3 constructs products. This is how the functor of points defines group schemes: $\mathbb{G}_m$ is a group in $\mathsf{Sch}$ because its functor of points takes values in groups. The ring maps are $x \mapsto x \otimes x$ for $\mathbb{G}_m$, and $x \mapsto x \otimes 1 + 1 \otimes x$ for the additive group $\mathbb{G}_a = \mathbb{A}^1$.

**Example P3.2.37 (the points of a variety).** Let $X = \operatorname{Spec} k[x_1, \dots, x_n]/I$. For a $k$-algebra $R$, the $k$-morphisms $\operatorname{Spec} R \to X$ are the $k$-algebra maps $k[x]/I \to R$, that is, the solutions $a \in R^n$ of the equations $f(a) = 0$ for $f \in I$. So $X(R)$ is the set of solutions of the defining equations in $R$. For $R = k$ algebraically closed this is the classical variety of P0. For $R = k[\epsilon]/(\epsilon^2)$ it is the set of pairs of a point and a tangent vector, by Example P3.1.27. So the functor of points contains the classical points, the tangent vectors and all the higher order data.

**Example P3.2.38 (the points of the doubled origin).** Let $X$ be the affine line with a doubled origin over $k$ and $K$ a field over $k$. A morphism $\operatorname{Spec} K \to X$ lands in one of the two charts, so $X(K)$ is the set $K \sqcup K$ modulo the identification of $a$ in the first copy with $a$ in the second for $a \neq 0$. It is $K$ with the point $0$ doubled. The functor $K \mapsto K$ of $\mathbb{A}^1_k$ and the functor of $X$ differ only in the value at $0$, and Theorem P3.2.34 says that this difference is enough to tell the schemes apart.

**Example P3.2.39 (projective space as a functor on local rings).** By Proposition P3.2.13, for every local ring $R$, $\mathbb{P}^n_\mathbb{Z}(R) = \mathrm{Um}(R)/R^\times$, the set of lines in $R^{n+1}$ spanned by a vector with a unit coordinate. For a general ring $R$, an element of $\mathbb{P}^n(R)$ is given locally on $\operatorname{Spec} R$ by such a vector, and the local data glue by Proposition P3.2.35. Chapter 6 identifies $\mathbb{P}^n(R)$ with the set of quotients $R^{n+1} \to L$ onto an invertible $R$-module $L$.

**Example P3.2.40 (functors that are not schemes).** Let $F(R) = \{0, 1\}$ for every ring $R$, with every ring map acting as the identity. The zero ring has $\operatorname{Spec} 0 = \emptyset$, and for every scheme $X$ the set $X(0) = \operatorname{Hom}(\emptyset, X)$ has exactly one element. Since $F(0)$ has two elements, $F$ is not of the form $R \mapsto X(R)$. Changing $F(0)$ to a single point does not help: Exercise 7 shows that the new functor fails the Zariski sheaf property, so it is not a scheme either. The functor of idempotents $R \mapsto \{e \in R : e^2 = e\}$ is the closest scheme, by Exercise 3. Chapter 13 meets the same problem for moduli functors, where the failure of the sheaf property comes from automorphisms.

### Proof

*Proof of Theorem P3.2.33.* This is Corollary P2.1.24 for $\mathcal{C} = \mathsf{Sch}$. The natural transformation $\eta \colon h_X \to h_Y$ comes from $f = \eta_X(1_X) \in Y(X)$, and an isomorphism $h_X \cong h_Y$ comes from an isomorphism $X \cong Y$ because a fully faithful functor reflects isomorphisms. $\square$

*Proof of Proposition P3.2.35.* The basic open sets $D(f_i)$ cover $\operatorname{Spec} R$ since the $f_i$ generate the unit ideal, $D(f_i) = \operatorname{Spec} R_{f_i}$ by Proposition P3.1.13, and $D(f_i) \cap D(f_j) = D(f_i f_j) = \operatorname{Spec} R_{f_i f_j}$. An element of $X(R_{f_i})$ is a morphism $D(f_i) \to X$, and its image in $X(R_{f_i f_j})$ is its restriction to $D(f_i f_j)$. So the statement is Proposition P3.2.4 for the cover of $\operatorname{Spec} R$ by the sets $D(f_i)$. $\square$

*Proof of Theorem P3.2.34.* Write $\mathsf{Aff}$ for the full subcategory of affine schemes, and $h_X|_{\mathsf{Aff}}$ for the restriction of $h_X$. By Corollary P3.1.23, functors on $\mathsf{Aff}^{\mathrm{op}}$ are the same as functors on $\mathsf{Ring}$, so it suffices to show that $\operatorname{Hom}(X, Y) \to \operatorname{Hom}(h_X|_{\mathsf{Aff}}, h_Y|_{\mathsf{Aff}})$ is bijective.

Injectivity. Let $f, g \colon X \to Y$ induce the same transformation. For every affine open $U \subseteq X$ with inclusion $\iota_U \in X(U)$, $f \circ \iota_U = g \circ \iota_U$, that is, $f|_U = g|_U$. The affine open sets cover $X$, so $f = g$ by Proposition P3.2.4.

Surjectivity. Let $\eta \colon h_X|_{\mathsf{Aff}} \to h_Y|_{\mathsf{Aff}}$ be natural. For each affine open $U \subseteq X$ let $f_U = \eta_U(\iota_U) \colon U \to Y$. If $W \subseteq U$ are affine open sets, with inclusion $\iota_{W, U} \colon W \to U$, then $\iota_W = \iota_U \circ \iota_{W, U}$, and naturality gives
$$f_W = \eta_W(\iota_U \circ \iota_{W, U}) = \eta_U(\iota_U) \circ \iota_{W, U} = f_U|_W.$$
For two affine open sets $U, U'$, the intersection $U \cap U'$ is covered by affine open sets $W$, and on each of them $f_U|_W = f_W = f_{U'}|_W$. By the uniqueness part of Proposition P3.2.4, applied to the open subscheme $U \cap U'$, $f_U$ and $f_{U'}$ agree on $U \cap U'$. By its existence part, the $f_U$ glue to a morphism $f \colon X \to Y$ with $f|_U = f_U$.

It remains to show $\eta_T(t) = f \circ t$ for every affine scheme $T$ and every $t \colon T \to X$. Cover $T$ by basic open sets $T_\alpha$ such that each $t(T_\alpha)$ lies in an affine open set $U_\alpha$ of $X$; this is possible since the preimages of affine open sets are open and the basic open sets form a basis. The sets $T_\alpha$ are affine by Proposition P3.1.13. Write $t_\alpha \colon T_\alpha \to U_\alpha$ for the restriction and $j_\alpha \colon T_\alpha \to T$ for the inclusion, so that $t \circ j_\alpha = \iota_{U_\alpha} \circ t_\alpha$. By naturality, applied twice,
$$\eta_T(t) \circ j_\alpha = \eta_{T_\alpha}(t \circ j_\alpha) = \eta_{T_\alpha}(\iota_{U_\alpha} \circ t_\alpha) = \eta_{U_\alpha}(\iota_{U_\alpha}) \circ t_\alpha = f_{U_\alpha} \circ t_\alpha = f \circ t \circ j_\alpha.$$
So $\eta_T(t)$ and $f \circ t$ agree on every $T_\alpha$, and they are equal by Proposition P3.2.4. $\square$

### Exercises

1. (A) Let $X$ be a scheme over a field $k$ and $K \supseteq k$ a field. Show that $X(K)$, the set of $k$-morphisms $\operatorname{Spec} K \to X$, is the set of pairs of a point $x \in X$ and a $k$-embedding $\kappa(x) \to K$. (Use Example P3.1.26 on an affine chart.)
2. (A) Compute $X(\mathbb{F}_p)$ and $X(\mathbb{F}_{p^2})$ for $X = \operatorname{Spec} \mathbb{Z}[x]/(x^2 + 1)$, for $p = 3$ and $p = 5$.
3. (A) Show that the functor $R \mapsto \{a \in R : a^2 = 0\}$ is represented by $\operatorname{Spec} \mathbb{Z}[x]/(x^2)$, and that the functor $R \mapsto \{e \in R : e^2 = e\}$ is represented by $\operatorname{Spec} \mathbb{Z} \sqcup \operatorname{Spec} \mathbb{Z}$.
4. (B) Show that $\mu_n(R) = \{a \in R : a^n = 1\}$ is represented by $\operatorname{Spec} \mathbb{Z}[x]/(x^n - 1)$, and describe the fibre of $\mu_p \to \operatorname{Spec} \mathbb{Z}$ over $(p)$. Show that it has one point and is not reduced.
5. (B) Let $\operatorname{GL}_n(R)$ be the group of invertible $n \times n$ matrices over $R$. Show that $\operatorname{GL}_n$ is represented by the affine scheme $\operatorname{Spec} \mathbb{Z}[x_{ij}, 1/\det]$, and that $\det$ is a natural transformation $\operatorname{GL}_n \to \mathbb{G}_m$.
6. (B) Show that two morphisms $f, g \colon X \to Y$ are equal if they agree on $K$-points for every field $K$ and $X$ is reduced, and give an example with $X = \operatorname{Spec} k[\epsilon]/(\epsilon^2)$ where they agree on all $K$-points and are not equal.
7. (C) Let $F(R) = \{0, 1\}$ for $R \neq 0$ and $F(0) = \{\ast\}$, with every map between nonzero rings acting as the identity. Show that $F$ is a functor. Take $R = \mathbb{Z} \times \mathbb{Z}$, $f_1 = (1, 0)$ and $f_2 = (0, 1)$, and show that the sequence of Proposition P3.2.35 is not an equalizer, since $R_{f_1 f_2} = 0$. Conclude that $F$ is not representable, and compare $F$ with the functor of idempotents of Exercise 3.

### Lean

Mathlib has the Yoneda embedding `CategoryTheory.yoneda` and its full faithfulness `CategoryTheory.Yoneda.fullyFaithful` for every category, so Theorem P3.2.33 is a special case. The statement that points with values in rings determine a scheme, and the Zariski sheaf property of a scheme as a functor on rings, are not in Lean as stated; the gluing of morphisms that underlies both is `AlgebraicGeometry.Scheme.Cover.glueMorphisms`. The handbook adds no `MinimalModel` node here.

### Notes and history

The functor of points is due to Grothendieck and is used throughout EGA, from EGA I, Chapter 0, on. Mumford's *Red book*, Section II.6, and Vakil, Chapter 6, give the first examples, and Görtz-Wedhorn treat representable functors in Chapter 4 and again in Chapter 8. The literature state is theorem. The functor point of view is the base of the moduli theory that the program uses: the Hilbert scheme and the Chow variety in P8 Ch. 1, the moduli of stable curves, and the boundedness results of Volume 10 are statements about the representability of functors.
