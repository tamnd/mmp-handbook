---
title: Natural transformations, equivalences and the Yoneda lemma
nodes: []
sources: [Vak25, Mac98]
reads_with: [Vak25:ch1, Mac98:ch1, Mac98:ch3, Mac98:ch4]
requires: [P2.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Natural transformations, equivalences and the Yoneda lemma

### Statement

**Definition P2.1.17 (natural transformation).** Let $F, G: \mathcal{C} \to \mathcal{D}$ be functors. A *natural transformation* $\eta: F \Rightarrow G$ is a family of morphisms $\eta_A: F(A) \to G(A)$, one for each object $A$ of $\mathcal{C}$, such that for every $f: A \to B$ the square commutes: $G(f) \circ \eta_A = \eta_B \circ F(f)$. It is a *natural isomorphism* if every $\eta_A$ is an isomorphism. Then the inverses $\eta_A^{-1}$ form a natural transformation $G \Rightarrow F$.

Lean: Mathlib `CategoryTheory.NatTrans` (the morphisms of the functor category `C ⥤ D`), and `CategoryTheory.NatIso.isIso_of_isIso_app` for the inverse.

Natural transformations compose, one object at a time. For $\mathcal{C}$ small, the functors $\mathcal{C} \to \mathcal{D}$ and the natural transformations form a category, the *functor category* $\operatorname{Fun}(\mathcal{C}, \mathcal{D})$. Its isomorphisms are the natural isomorphisms.

**Example P2.1.18 (the double dual).** Let $k$ be a field and $V$ a vector space. The map $\eta_V: V \to V^{**}$, $\eta_V(v)(\lambda) = \lambda(v)$, is natural: for $f: V \to W$ and $\lambda \in W^*$, both $f^{**}(\eta_V(v))(\lambda)$ and $\eta_W(f(v))(\lambda)$ equal $\lambda(f(v))$. On finite dimensional spaces $\eta$ is a natural isomorphism. A finite dimensional $V$ is also isomorphic to $V^*$, since both have the same dimension. But the isomorphism depends on a basis, and there is no natural one: $V \mapsto V^*$ is contravariant, so the question does not even make sense as a natural transformation between functors of the same variance. This is the example that led Eilenberg and Mac Lane to the definition.

**Example P2.1.19 (the determinant).** For a commutative ring $R$, let $\operatorname{GL}_n(R)$ be the group of invertible $n \times n$ matrices and $R^\times$ the group of units. Both are functors $\mathsf{Ring} \to \mathsf{Grp}$. The determinant $\det_R: \operatorname{GL}_n(R) \to R^\times$ is a natural transformation, since a ring map $\varphi: R \to S$ commutes with the polynomial formula for the determinant.

**Definition P2.1.20 (equivalence of categories).** A functor $F: \mathcal{C} \to \mathcal{D}$ is an *equivalence* if there is a functor $G: \mathcal{D} \to \mathcal{C}$ and natural isomorphisms $G \circ F \cong 1_{\mathcal{C}}$ and $F \circ G \cong 1_{\mathcal{D}}$. Then $G$ is a *quasi-inverse* of $F$.

Lean: Mathlib `CategoryTheory.Equivalence` (the data, written `C ≌ D`) and `CategoryTheory.Functor.IsEquivalence` (the property).

An equivalence keeps every notion that is stated in terms of objects and morphisms and is invariant under isomorphism. It need not be a bijection on objects. The categories $\mathsf{Mat}_k$ and $\mathsf{Vect}_k^{\mathrm{fd}}$ of Section 1.1 are equivalent, and the first has a countable set of objects.

**Theorem P2.1.21 (a criterion for equivalence).** A functor $F: \mathcal{C} \to \mathcal{D}$ is an equivalence if and only if it is fully faithful and essentially surjective.

Lean: Mathlib defines `CategoryTheory.Functor.IsEquivalence` as the conjunction of `Faithful`, `Full` and `EssSurj`, and `CategoryTheory.Functor.asEquivalence` builds the quasi-inverse (proved in Mathlib).

**Definition P2.1.22 (representable functor).** For an object $A$ of $\mathcal{C}$, write $h_A = \operatorname{Hom}_{\mathcal{C}}(-, A): \mathcal{C}^{\mathrm{op}} \to \mathsf{Set}$. A functor $F: \mathcal{C}^{\mathrm{op}} \to \mathsf{Set}$ is *representable* if $F \cong h_A$ for some $A$. A pair $(A, \xi)$ with $\xi \in F(A)$ is a *universal element* if for every object $T$ and every $x \in F(T)$ there is a unique $f: T \to A$ with $F(f)(\xi) = x$. The dual notions, for covariant functors $\mathcal{C} \to \mathsf{Set}$ and $h^A = \operatorname{Hom}(A, -)$, have the same names.

Lean: Mathlib `CategoryTheory.yoneda` (the functor $A \mapsto h_A$), `CategoryTheory.Functor.IsRepresentable` and `CategoryTheory.Functor.reprX` (a representing object).

**Theorem P2.1.23 (Yoneda lemma).** Let $F: \mathcal{C}^{\mathrm{op}} \to \mathsf{Set}$ be a functor and $A$ an object of $\mathcal{C}$. The map
$$\Phi: \operatorname{Nat}(h_A, F) \to F(A), \quad \eta \mapsto \eta_A(1_A)$$
is a bijection. Its inverse sends $\xi \in F(A)$ to the transformation with $\eta_T(f) = F(f)(\xi)$ for $f: T \to A$. The bijection is natural in $A$ and in $F$.

Lean: Mathlib `CategoryTheory.yonedaEquiv` (proved in Mathlib).

**Corollary P2.1.24 (the Yoneda embedding).** The functor $h: \mathcal{C} \to \operatorname{Fun}(\mathcal{C}^{\mathrm{op}}, \mathsf{Set})$, $A \mapsto h_A$, is fully faithful. In particular, if $h_A \cong h_B$ then $A \cong B$, and each natural isomorphism $h_A \cong h_B$ comes from a unique isomorphism $A \cong B$. A representable functor has a universal element, and its representing object is unique up to a unique isomorphism.

Lean: Mathlib `CategoryTheory.Yoneda.fullyFaithful` (proved in Mathlib).

### Proof in words

A natural transformation out of $h_A$ is determined by what it does to the single element $1_A$ of $h_A(A)$. Every $f: T \to A$ is the image of $1_A$ under $h_A(f)$, so naturality forces $\eta_T(f) = F(f)(\eta_A(1_A))$. That is the whole lemma. Applied to $F = h_B$ it says that the maps $h_A \Rightarrow h_B$ are the maps $A \to B$. So an object is known, up to unique isomorphism, once the maps into it are known. This is why a universal property defines an object: the universal property names the functor $h_A$, and the Yoneda lemma recovers $A$ from it.

For the criterion for equivalence, the quasi-inverse $G$ is built by choice. For each object $B$ of $\mathcal{D}$, choose $A$ and an isomorphism $F(A) \cong B$, and put $G(B) = A$. Full faithfulness defines $G$ on morphisms and makes it a functor.

### Examples

**Example P2.1.25 (products and tensor products as representing objects).** In $\mathsf{Mod}_A$, the functor $T \mapsto \operatorname{Hom}(T, M) \times \operatorname{Hom}(T, N)$ is represented by $M \oplus N$, with universal element the two projections. The covariant functor $P \mapsto \{\text{bilinear maps } M \times N \to P\}$ is represented by $M \otimes_A N$, with universal element the map $(m, n) \mapsto m \otimes n$. This is the definition of the tensor product in P1 Ch. 1, and the Yoneda lemma is the reason the tensor product is unique up to unique isomorphism.

**Example P2.1.26 (the functor of points).** The covariant functor $\mathsf{Ring} \to \mathsf{Set}$ that sends $R$ to $R$ itself is represented by $\mathbb{Z}[x]$: a ring map $\mathbb{Z}[x] \to R$ is the choice of the image of $x$. The functor $R \mapsto R^\times$ is represented by $\mathbb{Z}[x, x^{-1}]$, and $R \mapsto \{(a, b) \in R^2 : b^2 = a^3\}$ is represented by $\mathbb{Z}[x, y]/(y^2 - x^3)$. In P3 the dual statement reads: the affine line $\mathbb{A}^1$ represents the functor of global functions on schemes, the group $\mathbb{G}_m$ represents the functor of invertible functions, and a scheme is determined by its functor of points $T \mapsto \operatorname{Hom}(T, X)$. P8 Ch. 1 defines the Hilbert scheme as the object that represents the functor of flat families of subschemes.

**Example P2.1.27 (a functor that is not representable).** Let $N: \mathsf{Ring} \to \mathsf{Set}$ send $R$ to its set of nilpotent elements. Suppose $N \cong h^B$ with universal element $\xi \in N(B)$. Then $\xi^n = 0$ for some $n \geq 1$. In $R = \mathbb{Z}[t]/(t^{n+1})$ the element $t$ is nilpotent, so $t = \varphi(\xi)$ for some ring map $\varphi: B \to R$. Then $t^n = \varphi(\xi^n) = 0$, a contradiction since $t^n \neq 0$ in $R$. So $N$ is not representable. Each functor $R \mapsto \{a \in R : a^n = 0\}$ is represented by $\mathbb{Z}[t]/(t^n)$, and $N$ is the union of these. The hypothesis that fails is that a single object carries all the nilpotents at once.

**Example P2.1.28 (a fully faithful functor that is not an equivalence).** The inclusion of the full subcategory of free modules into $\mathsf{Mod}_{\mathbb{Z}}$ is fully faithful but not essentially surjective, since $\mathbb{Z}/2$ is not free. So it is not an equivalence, as the criterion predicts.

### Proof

*Proof of the Yoneda lemma.* Let $\eta: h_A \Rightarrow F$ be natural and put $\xi = \eta_A(1_A)$. For $f: T \to A$, naturality applied to $f$ and to the element $1_A \in h_A(A)$ gives
$$\eta_T(h_A(f)(1_A)) = F(f)(\eta_A(1_A)).$$
The left side is $\eta_T(1_A \circ f) = \eta_T(f)$. So $\eta_T(f) = F(f)(\xi)$, and $\eta$ is determined by $\xi$. So $\Phi$ is injective. For surjectivity, let $\xi \in F(A)$ and define $\eta_T(f) = F(f)(\xi)$. For $g: S \to T$ and $f: T \to A$,
$$\eta_S(h_A(g)(f)) = \eta_S(f \circ g) = F(f \circ g)(\xi) = F(g)(F(f)(\xi)) = F(g)(\eta_T(f)),$$
using that $F$ is contravariant. So $\eta$ is natural, and $\Phi(\eta) = F(1_A)(\xi) = \xi$. Naturality of $\Phi$ in $F$ is the identity $(\theta \circ \eta)_A(1_A) = \theta_A(\eta_A(1_A))$ for $\theta: F \Rightarrow F'$. Naturality in $A$ is the same computation with $g: A' \to A$. $\square$

*Proof of the corollary.* Apply the lemma to $F = h_B$. It gives a bijection $\operatorname{Nat}(h_A, h_B) \to h_B(A) = \operatorname{Hom}(A, B)$. Its inverse sends $u: A \to B$ to the transformation $f \mapsto u \circ f$, which is $h(u)$. So $h$ is fully faithful. A fully faithful functor reflects isomorphisms (Section 1.1), so $h_A \cong h_B$ gives $A \cong B$, from a unique isomorphism. If $\eta: h_A \Rightarrow F$ is an isomorphism with $\xi = \eta_A(1_A)$, then $f \mapsto F(f)(\xi)$ is the bijection $\eta_T$, and that is the statement that $(A, \xi)$ is universal. Two representing objects $A, A'$ give $h_A \cong F \cong h_{A'}$, so a unique isomorphism $A \cong A'$ that matches the universal elements. $\square$

*Proof of the criterion for equivalence.* Let $F$ be an equivalence with quasi-inverse $G$ and isomorphisms $\alpha: G F \Rightarrow 1$, $\beta: F G \Rightarrow 1$. Each $B$ is isomorphic to $F(G(B))$, so $F$ is essentially surjective. For $f: A \to A'$, naturality gives $f = \alpha_{A'} \circ G(F(f)) \circ \alpha_A^{-1}$, so $f$ is determined by $F(f)$ and $F$ is faithful. By symmetry $G$ is faithful. Let $g: F(A) \to F(A')$ and put $f = \alpha_{A'} \circ G(g) \circ \alpha_A^{-1}$. Then $G(F(f)) = G(g)$ by the formula above applied to $f$, and faithfulness of $G$ gives $F(f) = g$. So $F$ is full.

Conversely, let $F$ be fully faithful and essentially surjective. For each $B$ choose $G(B)$ in $\mathcal{C}$ and an isomorphism $\beta_B: F(G(B)) \to B$. For $g: B \to B'$, the map $\beta_{B'}^{-1} \circ g \circ \beta_B: F(G(B)) \to F(G(B'))$ is $F$ of a unique map, which is $G(g)$. Uniqueness gives $G(1_B) = 1_{G(B)}$ and $G(g' \circ g) = G(g') \circ G(g)$, so $G$ is a functor, and $\beta: F G \Rightarrow 1$ is natural by the construction. For $A$ in $\mathcal{C}$, the isomorphism $\beta_{F(A)}: F(G(F(A))) \to F(A)$ is $F(\alpha_A)$ for a unique $\alpha_A: G(F(A)) \to A$. It is an isomorphism since $F$ reflects isomorphisms, and it is natural in $A$ because $F$ is faithful and $F(\alpha)$ is natural. $\square$

### Exercises

1. (A) Let $F, G: \mathcal{C} \to \mathcal{D}$ and $\eta: F \Rightarrow G$ be natural, with every $\eta_A$ an isomorphism. Show that the inverses form a natural transformation.
2. (A) Show that the covariant functor $\mathsf{Grp} \to \mathsf{Set}$ that sends a group to its underlying set is represented by $\mathbb{Z}$, and that $G \mapsto \{g \in G : g^n = 1\}$ is represented by $\mathbb{Z}/n$.
3. (B) Show that the natural transformations from the identity functor of $\mathsf{Ab}$ to itself are the maps $x \mapsto nx$ with $n \in \mathbb{Z}$. (Hint: the identity functor is represented by $\mathbb{Z}$.)
4. (B) Let $G$ be a group, seen as a category with one object. Show that a functor $G \to \mathsf{Set}$ is a $G$-set, that a natural transformation is a $G$-equivariant map, and that the Yoneda lemma says that the $G$-equivariant maps $G \to S$ are given by the elements of $S$.
5. (B) Let $A$ be a ring and $\mathcal{C}$ the full subcategory of $\mathsf{Mod}_A$ of the modules $A^n$, $n \geq 0$. Show that $\mathcal{C}$ is equivalent to the category of finitely generated free $A$-modules. For $A$ local, show that it is equivalent to the category of finitely generated projective modules (use P1 Ch. 1).
6. (B) Let $k$ be a field. Show that $V \mapsto V^*$ is an equivalence $(\mathsf{Vect}_k^{\mathrm{fd}})^{\mathrm{op}} \to \mathsf{Vect}_k^{\mathrm{fd}}$. Is it an equivalence on all vector spaces?
7. (B) Show that the functor $R \mapsto \{(a, b) \in R^2 : ab = 0\}$ on $\mathsf{Ring}$ is represented by $\mathbb{Z}[x, y]/(xy)$. Show that the rule that sends $R$ to its set of zero divisors is not a functor on $\mathsf{Ring}$, so the question of its representability does not arise.

### Lean

The Yoneda lemma is `CategoryTheory.yonedaEquiv`, an equivalence of types between the natural transformations `yoneda.obj X ⟶ F` and `F.obj (op X)`. The full faithfulness of the Yoneda embedding is `CategoryTheory.Yoneda.fullyFaithful`, and the covariant form is `CategoryTheory.Coyoneda.fullyFaithful`. Mathlib defines an equivalence of categories as a structure `CategoryTheory.Equivalence` with a unit and a counit that satisfy a triangle identity, and it defines `Functor.IsEquivalence` by the criterion of this section, so the theorem is the construction `Functor.asEquivalence`. Representable functors are `Functor.IsRepresentable`. The handbook adds no `MinimalModel` node here.

### Notes and history

The lemma is named after Nobuo Yoneda, who explained it to Mac Lane in Paris in 1954, in the course of his work on the Ext groups of modules. Grothendieck used it systematically: the functor of points and the theory of representable functors are the foundation of his construction of the Hilbert and Picard schemes in the Bourbaki talks of 1957 to 1962. The criterion for equivalence uses the axiom of choice for classes, and a careful treatment uses a universe. Every statement here is classical.
