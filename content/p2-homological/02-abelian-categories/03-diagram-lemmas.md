---
title: The five lemma and the snake lemma
nodes: []
sources: [Wei94, Vak25, Mac98]
reads_with: [Wei94:ch1, Vak25:ch1, Mac98:ch8]
requires: [P1.1, P2.1, P2.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The five lemma and the snake lemma

### Statement

Throughout, $\mathcal{A}$ is an abelian category. A diagram is *commutative* if any two composites of maps between the same two objects agree.

**Theorem P2.2.22 (snake lemma).** Consider a commutative diagram with exact rows
$$\begin{array}{ccccccc} & A' & \xrightarrow{i'} & B' & \xrightarrow{p'} & C' & \to 0 \\ & \downarrow a & & \downarrow b & & \downarrow c & \\ 0 \to & A & \xrightarrow{i} & B & \xrightarrow{p} & C & \end{array}$$
in $\mathcal{A}$. There is a map $\delta: \ker c \to \operatorname{coker} a$, the *connecting map*, such that the sequence
$$\ker a \to \ker b \to \ker c \xrightarrow{\delta} \operatorname{coker} a \to \operatorname{coker} b \to \operatorname{coker} c$$
is exact. If $i'$ is a monomorphism, then so is $\ker a \to \ker b$. If $p$ is an epimorphism, then so is $\operatorname{coker} b \to \operatorname{coker} c$. The map $\delta$ is natural: a map of two such diagrams gives a commutative square between their connecting maps.

Lean: Mathlib `CategoryTheory.ShortComplex.SnakeInput` and `CategoryTheory.ShortComplex.SnakeInput.δ` (proved in Mathlib).

**Theorem P2.2.23 (five lemma).** Consider a commutative diagram with exact rows
$$\begin{array}{ccccccccc} A_1 & \to & A_2 & \to & A_3 & \to & A_4 & \to & A_5 \\ \downarrow f_1 & & \downarrow f_2 & & \downarrow f_3 & & \downarrow f_4 & & \downarrow f_5 \\ B_1 & \to & B_2 & \to & B_3 & \to & B_4 & \to & B_5 \end{array}$$
If $f_2$ and $f_4$ are isomorphisms, $f_1$ is an epimorphism and $f_5$ is a monomorphism, then $f_3$ is an isomorphism. More precisely: if $f_2, f_4$ are monomorphisms and $f_1$ is an epimorphism, then $f_3$ is a monomorphism; if $f_2, f_4$ are epimorphisms and $f_5$ is a monomorphism, then $f_3$ is an epimorphism.

Lean: Mathlib `CategoryTheory.Abelian.isIso_of_epi_of_isIso_of_isIso_of_mono`, with the two halves `CategoryTheory.Abelian.mono_of_epi_of_mono_of_mono` and `CategoryTheory.Abelian.epi_of_epi_of_epi_of_mono` (proved in Mathlib).

**Corollary P2.2.24 (short five lemma).** Let a map of short exact sequences $0 \to A \to B \to C \to 0$ and $0 \to A' \to B' \to C' \to 0$ be given, with components $f_A, f_B, f_C$. If $f_A$ and $f_C$ are isomorphisms, so is $f_B$.

Lean: Mathlib `CategoryTheory.ShortComplex.isIso₂_of_shortExact_of_isIso₁₃` (proved in Mathlib).

*Proof.* Extend both sequences by zeros on the left and on the right and apply the five lemma. $\square$

### Proof in words

Both lemmas are proved by a *diagram chase*: one follows elements around the diagram, using exactness to lift an element along a map and commutativity to move it from one row to the other. The connecting map of the snake lemma is the most important example. Start with $z \in \ker c$ in the top right corner. Lift it to $y \in B'$, push it down to $b(y) \in B$, notice that $b(y)$ maps to $c(z) = 0$ in $C$, so pull it back to $x \in A$, and take the class of $x$ in $\operatorname{coker} a$. The path has the shape of a snake. The whole content of the lemma is that this is well defined and that the long sequence is exact, and each step is a short chase.

In a general abelian category the objects have no elements. There are two ways around this. The first is the Freyd-Mitchell theorem of Section 2.2: the diagram lies in a small abelian subcategory, which embeds in a category of modules by an exact, fully faithful functor, and the chase is done there. The second is to replace elements by maps $T \to B$ from a variable object and to replace "lift an element" by "pass to an epimorphism $T' \to T$ and lift there". This second method is the one that Mathlib uses, and it gives proofs that do not depend on the embedding theorem.

### Examples

**Example P2.2.25 (multiplication by an integer).** Let $0 \to M' \to M \to M'' \to 0$ be a short exact sequence of abelian groups and $n \geq 1$. Apply the snake lemma to the map of the sequence to itself given by multiplication by $n$. Write $M[n] = \ker(n: M \to M)$. The lemma gives the exact sequence
$$0 \to M'[n] \to M[n] \to M''[n] \xrightarrow{\delta} M'/nM' \to M/nM \to M''/nM'' \to 0.$$
For $0 \to \mathbb{Z} \xrightarrow{p} \mathbb{Z} \to \mathbb{Z}/p \to 0$ and $n = p$ it reads $0 \to 0 \to 0 \to \mathbb{Z}/p \xrightarrow{\delta} \mathbb{Z}/p \xrightarrow{0} \mathbb{Z}/p \to \mathbb{Z}/p \to 0$. Here $\delta$ is an isomorphism: it sends the class of $1 \in \mathbb{Z}/p$ to the class of $1$, as the chase shows, since $1 \in \mathbb{Z}$ lifts it and $p \cdot 1 = p \cdot 1$. The middle map is zero since $\mathbb{Z}/p\mathbb{Z} \to \mathbb{Z}/p\mathbb{Z}$ is induced by multiplication by $p$. In Chapter 3 this sequence becomes the long exact sequence of $\operatorname{Tor}(-, \mathbb{Z}/n)$.

**Example P2.2.26 (restriction to a divisor).** Let $A$ be a ring, $f \in A$, and $u: M \to N$ a map of $A$-modules such that $f$ is a nonzerodivisor on $M$ and on $N$. Then $u$ is a map from the exact sequence $0 \to M \xrightarrow{f} M \to M/fM \to 0$ to the same sequence for $N$, with components $u$, $u$ and $\bar u: M/fM \to N/fN$. The snake lemma gives the exact sequence
$$0 \to \ker u \xrightarrow{f} \ker u \to \ker \bar u \to \operatorname{coker} u \xrightarrow{f} \operatorname{coker} u \to \operatorname{coker} \bar u \to 0.$$
So $\operatorname{coker} \bar u = \operatorname{coker} u / f \operatorname{coker} u$, and if $u$ is injective, $\ker \bar u$ is the submodule of $\operatorname{coker} u$ killed by $f$. In geometry, $M/fM$ is the restriction of $M$ to the divisor $S = \{f = 0\}$, and the sequence compares a map with its restriction to $S$. Chapter 3 applies the snake lemma to complexes and gets the long exact sequence of cohomology. For $0 \to \mathcal{O}_X(mD - S) \to \mathcal{O}_X(mD) \to \mathcal{O}_S(mD) \to 0$ it contains $H^0(X, \mathcal{O}_X(mD)) \to H^0(S, \mathcal{O}_S(mD)) \to H^1(X, \mathcal{O}_X(mD - S))$. So the sections on $S$ lift to $X$ when the $H^1$ vanishes. This is the lifting step of the base point free theorem in Volume 7.

**Example P2.2.27 (the five lemma needs the middle map).** The sequences $0 \to \mathbb{Z}/2 \to \mathbb{Z}/4 \to \mathbb{Z}/2 \to 0$ and $0 \to \mathbb{Z}/2 \to \mathbb{Z}/2 \oplus \mathbb{Z}/2 \to \mathbb{Z}/2 \to 0$ are exact and have isomorphic outer terms, but $\mathbb{Z}/4 \not\cong \mathbb{Z}/2 \oplus \mathbb{Z}/2$. The five lemma does not apply, since there is no map $\mathbb{Z}/4 \to \mathbb{Z}/2 \oplus \mathbb{Z}/2$ that makes both squares commute with the identity on the ends. The hypothesis that fails is the existence of $f_3$. Extensions with the same ends are classified by $\operatorname{Ext}^1$ (Chapter 3), and here $\operatorname{Ext}^1(\mathbb{Z}/2, \mathbb{Z}/2) = \mathbb{Z}/2$ has two elements.

**Example P2.2.28 (the five lemma needs exact rows).** Take the top row $0 \to 0 \to \mathbb{Z} \to 0 \to 0$, the bottom row $0 \to 0 \to 0 \to 0 \to 0$, and the zero maps between them. All outer vertical maps are isomorphisms between zero objects, and $f_3: \mathbb{Z} \to 0$ is not a monomorphism. The top row is not exact at $\mathbb{Z}$.

### Proof

The proofs are written for $\mathsf{Mod}_R$. For a general abelian category $\mathcal{A}$, the finitely many objects and maps of the diagram, with their kernels and cokernels, lie in a small full abelian subcategory $\mathcal{A}_0$ (Section 2.2), and $\mathcal{A}_0$ has an exact, fully faithful functor $F: \mathcal{A}_0 \to \mathsf{Mod}_R$. An exact functor preserves kernels, cokernels, images and exact sequences. A fully faithful functor lets the maps built in $\mathsf{Mod}_R$, such as $\delta$, be pulled back to $\mathcal{A}_0$. An exact faithful functor reflects exactness: if $F(A) \to F(B) \to F(C)$ is exact, then the image of $g f$ under $F$ is zero, so $g f = 0$, and $F$ of the homology object $\ker g / \operatorname{im} f$ is zero, so the object is zero (an object $X$ with $F(X) = 0$ has $F(1_X) = 0 = F(0)$, so $1_X = 0$). So the statements in $\mathsf{Mod}_R$ give the statements in $\mathcal{A}$.

*Proof of the snake lemma.* The maps $\ker a \to \ker b \to \ker c$ are the restrictions of $i'$ and $p'$: if $a(x) = 0$ then $b(i'(x)) = i(a(x)) = 0$. The maps $\operatorname{coker} a \to \operatorname{coker} b \to \operatorname{coker} c$ are induced by $i$ and $p$, since $i(a(A')) = b(i'(A'))$.

Definition of $\delta$. Let $z \in \ker c$. Since $p'$ is onto, $z = p'(y)$ for some $y \in B'$. Then $p(b(y)) = c(p'(y)) = c(z) = 0$, so $b(y) = i(x)$ for a unique $x \in A$, since the bottom row is exact and $i$ is injective. Put $\delta(z) = [x] \in \operatorname{coker} a$. If $y_1$ is another lift of $z$, then $y_1 - y \in \ker p' = i'(A')$, say $y_1 - y = i'(x')$. Then $b(y_1) = b(y) + i(a(x'))$, so $x$ changes to $x + a(x')$, with the same class. So $\delta$ is well defined, and it is linear since all choices can be made linearly.

Exactness at $\ker b$. The composite $\ker a \to \ker b \to \ker c$ is zero since $p' i' = 0$. If $y \in \ker b$ and $p'(y) = 0$, then $y = i'(x')$ with $x' \in A'$, and $i(a(x')) = b(y) = 0$, so $a(x') = 0$ because $i$ is injective. So $x' \in \ker a$.

Exactness at $\ker c$. If $z = p'(y)$ with $y \in \ker b$, then $b(y) = 0 = i(0)$ and $\delta(z) = 0$. Conversely, let $\delta(z) = 0$, so $x = a(x')$ for some $x' \in A'$. Then $y - i'(x')$ is another lift of $z$, and $b(y - i'(x')) = i(x) - i(a(x')) = 0$. So $z$ comes from $\ker b$.

Exactness at $\operatorname{coker} a$. The image of $\delta(z)$ in $\operatorname{coker} b$ is the class of $i(x) = b(y)$, which is zero. Conversely, let $x \in A$ have $i(x) = b(y)$ for some $y \in B'$. Put $z = p'(y)$. Then $c(z) = p(b(y)) = p(i(x)) = 0$, so $z \in \ker c$, and $\delta(z) = [x]$ by the definition, with the lift $y$.

Exactness at $\operatorname{coker} b$. The composite is zero since $p i = 0$. Let $w \in B$ map to zero in $\operatorname{coker} c$, so $p(w) = c(z')$ for some $z' \in C'$. Write $z' = p'(y')$. Then $p(w - b(y')) = 0$, so $w - b(y') = i(x)$ for some $x \in A$, and $[w] = [i(x)]$ in $\operatorname{coker} b$ is the image of $[x]$.

The two extra statements are clear: if $i'$ is injective, so is its restriction to $\ker a$; if $p$ is onto, so is the map it induces on cokernels. For naturality, a map of diagrams sends a choice of $y$ and $x$ for $z$ to a valid choice for the image of $z$, so the square commutes. $\square$

*Proof of the five lemma.* Write $\alpha_k: A_k \to A_{k+1}$ and $\beta_k: B_k \to B_{k+1}$ for the maps of the rows.

Suppose $f_2, f_4$ are injective and $f_1$ is onto, and let $f_3(x) = 0$ with $x \in A_3$. Then $f_4(\alpha_3(x)) = \beta_3(f_3(x)) = 0$, so $\alpha_3(x) = 0$ and $x = \alpha_2(w)$ for some $w \in A_2$. Now $\beta_2(f_2(w)) = f_3(x) = 0$, so $f_2(w) = \beta_1(v)$ for some $v \in B_1$, and $v = f_1(u)$ for some $u \in A_1$. Then $f_2(\alpha_1(u)) = \beta_1(f_1(u)) = f_2(w)$, so $w = \alpha_1(u)$ since $f_2$ is injective. So $x = \alpha_2(\alpha_1(u)) = 0$.

Suppose $f_2, f_4$ are onto and $f_5$ is injective, and let $y \in B_3$. Write $\beta_3(y) = f_4(t)$ with $t \in A_4$. Then $f_5(\alpha_4(t)) = \beta_4(\beta_3(y)) = 0$, so $\alpha_4(t) = 0$ and $t = \alpha_3(x)$ for some $x \in A_3$. Now $\beta_3(y - f_3(x)) = f_4(t) - f_4(\alpha_3(x)) = 0$, so $y - f_3(x) = \beta_2(s)$ with $s \in B_2$, and $s = f_2(r)$ with $r \in A_2$. Then $y = f_3(x + \alpha_2(r))$. So $f_3$ is onto. In an abelian category a monomorphism that is an epimorphism is an isomorphism (Section 2.2). $\square$

### Exercises

1. (A) In the snake lemma, compute every term and every map for the diagram whose rows are both $0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z} \to \mathbb{Z}/2 \to 0$ and whose vertical maps are multiplication by $3$.
2. (A) Use the snake lemma to show: in a map of short exact sequences with components $f_A, f_B, f_C$, if $f_A$ and $f_C$ are injective then so is $f_B$, and if $f_A$ and $f_C$ are onto then so is $f_B$.
3. (B) Prove the nine lemma: in a commutative $3 \times 3$ diagram of objects whose three columns are short exact, if the bottom two rows are short exact, then so is the top row. (Hint: apply the snake lemma to the bottom two rows.)
4. (B) Let $f: A \to B$ and $g: B \to C$ be maps in an abelian category. Show that there is an exact sequence $0 \to \ker f \to \ker g f \to \ker g \to \operatorname{coker} f \to \operatorname{coker} g f \to \operatorname{coker} g \to 0$.
5. (B) Let $A$ be a local ring with maximal ideal $\mathfrak{m}$ and residue field $k$, and let $u: M \to N$ be a map of finitely generated modules with $N$ free. Show: if $u \otimes k$ is injective, then $u$ is injective and $\operatorname{coker} u$ is free. (Hint: extend the images of a minimal set of generators of $M$ to a basis of $N/\mathfrak{m}N$ and use Nakayama's lemma.) (This is the local criterion behind the freeness of the cokernel of a map of vector bundles of constant rank.)
6. (C) Prove the snake lemma in an abelian category without the embedding theorem. Construct $\delta$ from the fibre product $B' \times_{C'} \ker c$ and the pushout $\operatorname{coker} a \sqcup_A B$, and prove exactness with the method of maps from a variable object.

### Lean

The snake lemma is `CategoryTheory.ShortComplex.SnakeInput` in `Mathlib.Algebra.Homology.ShortComplex.SnakeLemma`. The structure records the diagram, and `SnakeInput.δ` is the connecting map, built from a fibre product as in Exercise 6. The exactness statements are lemmas `SnakeInput.L₀_exact`, `SnakeInput.L₁'_exact`, `SnakeInput.L₂'_exact` and `SnakeInput.L₃_exact`. The five lemma and its halves are in `Mathlib.CategoryTheory.Abelian.DiagramLemmas.Four`, stated for composable arrows: `Abelian.isIso_of_epi_of_isIso_of_isIso_of_mono`, `Abelian.mono_of_epi_of_mono_of_mono` and `Abelian.epi_of_epi_of_epi_of_mono`. These proofs use the method of maps from a variable object (in `Mathlib.CategoryTheory.Abelian.Refinements`), not the Freyd-Mitchell theorem. The handbook adds no `MinimalModel` node here.

### Notes and history

The five lemma and diagram chasing come from algebraic topology. Eilenberg and Steenrod used them in their axiomatic treatment of homology in 1952. The connecting map is older: it is the boundary map of the long exact sequence of a pair, from Hurewicz and from Kelley and Pitcher in the 1940s. The name "snake lemma" is standard in English and French (lemme du serpent). Every statement here is classical.
