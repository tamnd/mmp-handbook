---
title: Numerical classes of divisors and curves
nodes: []
sources: [Laz04, Kle66, Deb01, Har77]
reads_with: [Laz04:1.1.C, Deb01:ch1, Kle66:I.2]
requires: [P3.4, P3.7, P3.8, P3.9, P5.4, P5.5, P7.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Numerical classes of divisors and curves

### Statement

Throughout, $k$ is algebraically closed and $X$ is a projective scheme over $k$. A *curve on $X$* is an integral closed subscheme of dimension $1$. For a line bundle $L$ and a curve $C$, the number $(L \cdot C)$ of Definition P7.1.5 is $\deg (L|_C)$ by part 2 of Proposition P7.1.7.

**Definition P7.2.1 (numerical equivalence).** A line bundle $L$ on $X$ is *numerically trivial*, written $L \equiv 0$, if $(L \cdot C) = 0$ for every curve $C$ on $X$. Two line bundles $L$, $M$ are *numerically equivalent*, $L \equiv M$, if $L \otimes M^{-1} \equiv 0$. The numerically trivial line bundles form a subgroup $\operatorname{Pic}^\tau(X)$ of $\operatorname{Pic}(X)$, and the quotient
$$N^1(X)_\mathbb{Z} = \operatorname{Pic}(X) / \operatorname{Pic}^\tau(X)$$
is the group of *numerical classes* of line bundles. The class of $L$ is written $[L]$, and for a Cartier divisor $D$ on a variety, $[D] = [\mathcal{O}_X(D)]$.

**Proposition P7.2.2 (numerically trivial line bundles).** Let $L_1 \equiv 0$. Then $(L_1 \cdot L_2 \cdots L_r \cdot \mathcal{F}) = 0$ for all line bundles $L_2, \dots, L_r$ and every coherent sheaf $\mathcal{F}$ with $\dim \operatorname{Supp} \mathcal{F} \leq r$. Consequently every intersection number $(L_1 \cdots L_r \cdot \mathcal{F})$ depends only on the numerical classes $[L_1], \dots, [L_r]$.

Lean: not in Lean as stated.

**Definition P7.2.3 (real divisor classes).** Let $\operatorname{Pic}(X)_\mathbb{R} = \operatorname{Pic}(X) \otimes_\mathbb{Z} \mathbb{R}$. For $\delta = \sum_i a_i \otimes L_i$ in it and a curve $C$, put $(\delta \cdot C) = \sum_i a_i (L_i \cdot C)$, which is well defined because $L \mapsto (L \cdot C)$ is additive. The *real Néron-Severi space* is
$$N^1(X) = \operatorname{Pic}(X)_\mathbb{R} / \{ \delta : (\delta \cdot C) = 0 \text{ for every curve } C \}.$$
Its elements are *numerical classes* or simply *classes*, and $N^1(X)_\mathbb{Q}$ is defined in the same way from $\operatorname{Pic}(X) \otimes \mathbb{Q}$. When $X$ is a variety, every line bundle is $\mathcal{O}_X(D)$ for a Cartier divisor $D$ (Theorem P3.9.4), and an *$\mathbb{R}$-Cartier divisor* is an element $D = \sum_i a_i D_i$ of $\operatorname{CaDiv}(X) \otimes \mathbb{R}$; its class is $[D] = \sum_i a_i [\mathcal{O}_X(D_i)]$. Two $\mathbb{R}$-Cartier divisors $D$, $D'$ are *numerically equivalent*, $D \equiv D'$, if $[D] = [D']$. When $X$ is normal, a $\mathbb{Q}$-Cartier Weil $\mathbb{Q}$-divisor $\Delta$ in the sense of part 4 of Definition P3.9.18 has the class $[\Delta] = \frac{1}{m} [m\Delta]$ for any $m \geq 1$ with $m\Delta$ Cartier.

**Definition P7.2.4 (curves and the space $N_1$).** Let $Z_1(X)_\mathbb{R}$ be the real vector space with basis the curves on $X$; its elements are *real $1$-cycles* $\gamma = \sum_j b_j C_j$. Put $(L \cdot \gamma) = \sum_j b_j (L \cdot C_j)$ for $L \in \operatorname{Pic}(X)_\mathbb{R}$. A $1$-cycle $\gamma$ is *numerically trivial*, $\gamma \equiv 0$, if $(L \cdot \gamma) = 0$ for every line bundle $L$, and
$$N_1(X) = Z_1(X)_\mathbb{R} / \{ \gamma : \gamma \equiv 0 \}.$$
The class of a curve $C$ is written $[C]$. For a coherent sheaf $\mathcal{F}$ with $\dim \operatorname{Supp} \mathcal{F} \leq 1$, the class $[\mathcal{F}] \in N_1(X)$ is the class of its $1$-cycle $[\mathcal{F}]_1$ of Definition P7.1.12. The image of the integral $1$-cycles is a subgroup $N_1(X)_\mathbb{Z}$.

**Proposition P7.2.5 (the pairing).**

1. The intersection number defines a bilinear pairing $N^1(X) \times N_1(X) \to \mathbb{R}$, $(\xi, \gamma) \mapsto \xi \cdot \gamma$. It is nondegenerate: a class $\xi$ with $\xi \cdot \gamma = 0$ for all $\gamma$ is zero, and a class $\gamma$ with $\xi \cdot \gamma = 0$ for all $\xi$ is zero.
2. $N^1(X)_\mathbb{Z}$ is torsion-free, and the map $N^1(X)_\mathbb{Z} \to N^1(X)$, $[L] \mapsto [1 \otimes L]$, is injective with image spanning $N^1(X)$.
3. If $N^1(X)$ has finite dimension $\rho$, then $N_1(X)$ has dimension $\rho$ and the pairing is perfect, that is, it identifies each space with the dual of the other.

Lean: not in Lean as stated.

**Lemma P7.2.6 (lifting curves).** Let $f \colon Y \to X$ be a surjective morphism of projective schemes over $k$ and $C$ a curve on $X$. There is a curve $C'$ on $Y$ with $f(C') = C$.

Lean: not in Lean as stated.

**Proposition P7.2.7 (pullback and pushforward).** Let $f \colon Y \to X$ be a morphism of projective schemes over $k$.

1. Pullback of line bundles induces a linear map $f^* \colon N^1(X) \to N^1(Y)$.
2. For a curve $C'$ on $Y$, put $f_*[C'] = [K(C') : K(f(C'))] \, [f(C')]$ if $f(C')$ is a curve and $f_*[C'] = 0$ if $f(C')$ is a point. This extends linearly to $Z_1(Y)_\mathbb{R}$, descends to a linear map $f_* \colon N_1(Y) \to N_1(X)$, and satisfies the projection formula $f^* \xi \cdot \gamma = \xi \cdot f_* \gamma$.
3. If $f$ is surjective, then $f_* \colon N_1(Y) \to N_1(X)$ is surjective and $f^* \colon N^1(X) \to N^1(Y)$ is injective. The same holds for $N^1(X)_\mathbb{Z} \to N^1(Y)_\mathbb{Z}$.

Lean: not in Lean as stated.

**Proposition P7.2.8 (agreement on surfaces).** Let $S$ be a smooth projective surface. A line bundle $L$ on $S$ is numerically trivial in the sense of Definition P7.2.1 if and only if it is numerically trivial in the sense of Definition P5.5.7. So $N^1(S)_\mathbb{Z} = \operatorname{Num}(S)$, and $N^1(S)$ is the space $N^1(S)$ of Definition P5.12.1. The map $Z_1(S)_\mathbb{R} \to N^1(S)$, $C \mapsto [\mathcal{O}_S(C)]$, induces an isomorphism $N_1(S) \cong N^1(S)$ under which the pairing of Proposition P7.2.5 becomes the intersection form of $S$.

Lean: not in Lean as stated.

### Proof in words

A numerically trivial line bundle has degree $0$ on every curve. To see that it has zero intersection numbers with surfaces and higher-dimensional subvarieties, cut the subvariety by a section of one of the other line bundles, after writing that bundle as a difference of very ample ones. The cycle formula expresses the result through subvarieties of one dimension less, and induction ends at curves. So intersection numbers are functions of numerical classes, and all the constructions of the chapter make sense.

The two spaces $N^1(X)$ and $N_1(X)$ are quotients of $\operatorname{Pic}(X)_\mathbb{R}$ and $Z_1(X)_\mathbb{R}$ by the kernels of the intersection pairing, so the induced pairing is nondegenerate by construction. Nondegeneracy alone gives injections of each space into the dual of the other, and once one of them is finite-dimensional, counting dimensions shows that both injections are isomorphisms. The theorem of the base of Section 2.2 provides the finite dimension.

A morphism pulls back line bundles and pushes forward curves, with the degree of the field extension as multiplicity. The projection formula of Chapter 1 for curves says that the two operations are adjoint, which is what makes them well defined on numerical classes. When the morphism is surjective, every curve downstairs is the image of a curve upstairs, found by cutting the preimage with hyperplanes, so pushforward is onto and pullback is injective.

### Examples

**Example P7.2.9 (curves).** Let $X = C$ be an integral projective curve. The only curve on $C$ is $C$ itself, so $L \equiv 0$ if and only if $\deg L = 0$, and $\deg \colon N^1(C)_\mathbb{Z} \to \mathbb{Z}$ is injective. It is surjective: a smooth closed point $x$ of $C$ is an effective Cartier divisor, its local ring being a discrete valuation ring, and $\deg \mathcal{O}_C(x) = (\cdot \mathcal{O}_x) = 1$ by part 6 of Theorem P7.1.6 and part 1 of Proposition P7.1.7. So $N^1(C)_\mathbb{Z} = \mathbb{Z}$, $N^1(C) = \mathbb{R}$, $N_1(C) = \mathbb{R}[C]$ and $\rho(C) = 1$. The kernel $\operatorname{Pic}^\tau(C)$ is the group $\operatorname{Pic}^0(C)$ of line bundles of degree $0$, which is in general very large.

**Example P7.2.10 (an elliptic curve).** Let $(E, O)$ be an elliptic curve. By Definition P5.4.1, $P \mapsto [P - O]$ is a bijection from the closed points of $E$ onto $\operatorname{Pic}^0(E) = \operatorname{Pic}^\tau(E)$. So for $P \neq O$ the line bundle $\mathcal{O}_E(P - O)$ is numerically trivial and not trivial. Over $k = \mathbb{C}$ the group $\operatorname{Pic}^0(E)$ is uncountable and contains elements of infinite order. Over $k = \overline{\mathbb{F}}_p$ every element of $\operatorname{Pic}^0(E)$ is torsion. Indeed, a Weierstrass equation of $E$ (Theorem P5.4.2) has its coefficients in some finite field $\mathbb{F}_q$, and every point $P$ has coordinates in some $\mathbb{F}_{q'}$ with $\mathbb{F}_q \subseteq \mathbb{F}_{q'}$. By the last part of Theorem P5.4.4, the line through two points with coordinates in $\mathbb{F}_{q'}$ meets the cubic in a third point with coordinates in $\mathbb{F}_{q'}$, so the points with coordinates in $\mathbb{F}_{q'}$ form a finite subgroup, and $P$ has finite order. In both cases $N^1(E)_\mathbb{Z} = \mathbb{Z}$: numerical equivalence forgets all of $\operatorname{Pic}^0$, torsion or not.

**Example P7.2.11 (two lines).** Let $Q = \mathbb{P}^1 \times \mathbb{P}^1$, embedded in $\mathbb{P}^3$ as $V_+(xw - yz)$ by the Segre map, and let $X = \ell_1 \cup \ell_2$ be the union of the fibres $\ell_1 = \{a\} \times \mathbb{P}^1$ and $\ell_2 = \mathbb{P}^1 \times \{b\}$, with its reduced structure. For $a = b = [1 : 0]$, $X$ is the section of $Q$ by the plane $x = 0$, namely $V_+(x, yz)$, so $X$ is also the plane conic $V_+(yz)$ of two crossing lines. The curves on $X$ are $\ell_1$ and $\ell_2$, so $L \mapsto (\deg L|_{\ell_1}, \deg L|_{\ell_2})$ is an injection $N^1(X)_\mathbb{Z} \to \mathbb{Z}^2$. The restrictions of $\mathcal{O}(1, 0)$ and $\mathcal{O}(0, 1)$ have degrees $(0, 1)$ and $(1, 0)$, so $N^1(X)_\mathbb{Z} = \mathbb{Z}^2$ and $\rho(X) = 2$. The restriction of $\mathcal{O}_{\mathbb{P}^2}(1)$ to the conic has degrees $(1, 1)$, so the image of $N^1(\mathbb{P}^2)_\mathbb{Z} = \mathbb{Z}$ (Proposition P7.2.21) is a proper subgroup: restriction to a subscheme need not be surjective on numerical classes, and the Picard number of a reducible curve is the number of its components.

### Proof

*Proposition P7.2.2.* By Theorem P7.1.13 and additivity in the cycle, it suffices to prove $(L_1 \cdots L_r \cdot V) = 0$ for an integral closed subscheme $V$ of dimension $r$; if $\dim \operatorname{Supp} \mathcal{F} < r$ the number is $0$ anyway by part 2 of Theorem P7.1.6. Induct on $r$. For $r = 0$ there is no $L_1$ and nothing to prove; for $r = 1$, $V$ is a curve and $(L_1 \cdot V) = 0$ by definition. Let $r \geq 2$. By part 2 of Lemma P7.1.1, $L_r \cong A \otimes B^{-1}$ with $A$, $B$ very ample, and by multilinearity (part 4 of Theorem P7.1.6) it suffices to treat $L_r$ very ample. By part 1 of Lemma P7.1.1 there is $\sigma \in H^0(X, L_r)$ not vanishing at the generic point of $V$, the only associated point of $\mathcal{O}_V$. By part 6 of Theorem P7.1.6,
$$(L_1 \cdots L_r \cdot V) = (L_1 \cdots L_{r-1} \cdot (\mathcal{O}_V)_\sigma),$$
and $(\mathcal{O}_V)_\sigma$ has support of dimension at most $r - 1$ by part 3 of Lemma P7.1.2. By Theorem P7.1.13 the right side is $\sum_W m_W (L_1 \cdots L_{r-1} \cdot W)$ over integral $W$ of dimension $r - 1$, and each term vanishes by induction. For the last statement, if $L_i \equiv L_i'$ for all $i$, replace the $L_i$ by the $L_i'$ one at a time and use multilinearity and symmetry (parts 1 and 4 of Theorem P7.1.6). $\square$

*Proposition P7.2.5.* Part 1. By Definition P7.2.3, $(\delta \cdot C)$ depends only on the class of $\delta$ in $N^1(X)$, so $(\delta \cdot \gamma)$ depends only on the classes of $\delta$ and $\gamma$ by bilinearity and Definition P7.2.4. If $\xi \cdot \gamma = 0$ for all $\gamma$, then $\xi \cdot [C] = 0$ for every curve, so $\xi = 0$ by Definition P7.2.3. If $\xi \cdot \gamma = 0$ for all $\xi$, then $(L \cdot \gamma) = 0$ for every line bundle, so $\gamma = 0$ by Definition P7.2.4.

Part 2. If $L^m \equiv 0$ with $m \geq 1$, then $m (L \cdot C) = 0$ for every curve, so $L \equiv 0$. If $1 \otimes L$ is zero in $N^1(X)$, then $(L \cdot C) = 0$ for every curve, so $[L] = 0$ in $N^1(X)_\mathbb{Z}$. The elements $1 \otimes L$ span $\operatorname{Pic}(X)_\mathbb{R}$ over $\mathbb{R}$.

Part 3. By part 1 the maps $N_1(X) \to N^1(X)^\vee$ and $N^1(X) \to N_1(X)^\vee$ are injective. The first gives $\dim N_1(X) \leq \rho$, so $N_1(X)$ is finite-dimensional and $N_1(X)^\vee$ has the same dimension. The second gives $\rho \leq \dim N_1(X)$. So the dimensions are equal, and both injections are isomorphisms. $\square$

*Lemma P7.2.6.* The morphism $f$ is proper, since $Y$ is proper over $k$ and $X$ is separated. Give $f^{-1}(C)$ its reduced structure and let $W_1, \dots, W_s$ be its irreducible components. Their images are closed and irreducible, and their union is $C$, which is irreducible; so $f(W_i) = C$ for some $i$. Let $W = W_i$, an integral closed subscheme of $Y$ with $f(W) = C$, and $w = \dim W \geq 1$. If $w = 1$, take $C' = W$. Let $w \geq 2$ and fix a closed immersion $Y \subseteq \mathbb{P}^N$. It suffices to find an integral closed subscheme $W' \subseteq W$ of dimension $w - 1$ with $f(W') = C$, and to repeat.

Every component of every nonempty fibre of $f|_W \colon W \to C$ over a closed point has dimension at least $w - 1 \geq 1$, by part 2 of Theorem P3.7.6. Choose a hyperplane $H \subseteq \mathbb{P}^N$ that does not contain $W$. Each irreducible component of $W \cap H$ is a proper closed subset of $W$, so it has dimension at most $w - 1$, and at least $w - 1$ by part 2 of Proposition P3.7.5 applied on the affine charts. Suppose that no component of $W \cap H$ maps onto $C$. Then their images are finitely many closed points, and there is a closed point $c \in C$ outside them. The fibre $W_c$ is nonempty, so it has an irreducible component $Z$ of dimension at least $1$, and $Z \cap H = \emptyset$. Then $Z$ with its reduced structure is a closed subscheme of the affine space $\mathbb{P}^N \setminus H$, so it is affine, and it is proper over $k$. By Example P3.4.27 its ring of global functions is $k$, so $Z$ is a point, a contradiction. So some component $W'$ of $W \cap H$ maps onto $C$, and it has dimension $w - 1$. $\square$

*Proposition P7.2.7.* Part 1. If $L \equiv 0$ on $X$ and $C'$ is a curve on $Y$, Theorem P7.1.15 with $r = 1$ gives $(f^* L \cdot C') = [K(C') : K(f(C'))] (L \cdot f(C'))$ if $f(C')$ is a curve, and $0$ if it is a point. In both cases the number is $0$, so $f^* L \equiv 0$. So $f^*$ is well defined on $N^1(X)_\mathbb{Z}$, and tensoring with $\mathbb{R}$ and passing to the quotient gives the linear map on $N^1(X)$, by the same computation for $\delta \in \operatorname{Pic}(X)_\mathbb{R}$.

Part 2. The computation of part 1 is the projection formula $(f^* L \cdot C') = (L \cdot f_* C')$ for curves, and it extends by linearity to $1$-cycles and to $\operatorname{Pic}(X)_\mathbb{R}$. If $\gamma \equiv 0$ on $Y$, then $(L \cdot f_* \gamma) = (f^* L \cdot \gamma) = 0$ for every $L$, so $f_* \gamma \equiv 0$ and $f_*$ descends.

Part 3. By Lemma P7.2.6 every curve $C$ on $X$ is $f(C')$ for a curve $C'$ on $Y$, and then $[C] = \frac{1}{d} f_*[C']$ with $d = [K(C') : K(C)] \geq 1$. So $f_*$ is surjective. If $f^* \xi = 0$, then $\xi \cdot f_* \gamma = f^* \xi \cdot \gamma = 0$ for all $\gamma$, so $\xi$ pairs to zero with $N_1(X)$ and $\xi = 0$ by part 1 of Proposition P7.2.5. For integral classes, if $f^* L \equiv 0$, then $d (L \cdot C) = (f^* L \cdot C') = 0$ for every curve $C$, with $C'$ as above. $\square$

*Proposition P7.2.8.* By part 3 of Proposition P7.1.7 and Theorem P5.5.6, $(L \cdot C) = (L \cdot \mathcal{O}_S(C))$, the intersection pairing of $S$, for every integral curve $C$. If $L \cdot E = 0$ for every divisor $E$, then in particular $(L \cdot C) = 0$ for every curve. Conversely, if $(L \cdot C) = 0$ for every curve, then $L \cdot E = 0$ for every divisor $E$, since by Corollary P5.5.3 every divisor is linearly equivalent to a difference of two integral curves. So the two notions agree, and $N^1(S)_\mathbb{Z} = \operatorname{Num}(S)$, whose tensor product with $\mathbb{R}$ is the space of Definition P5.12.1 by part 3 of Proposition P7.2.5 once $\operatorname{Num}(S)$ is finitely generated, a case of Theorem P7.2.12. Let $\psi \colon Z_1(S)_\mathbb{R} \to N^1(S)$ send $C$ to $[\mathcal{O}_S(C)]$. For every $\xi \in N^1(S)$ and $\gamma \in Z_1(S)_\mathbb{R}$, $\xi \cdot \gamma = \xi \cdot \psi(\gamma)$, the right side being the intersection form. The form is nondegenerate on $N^1(S)$ by Definition P5.5.7, so $\gamma \equiv 0$ if and only if $\psi(\gamma) = 0$, and $\psi$ induces an injection $N_1(S) \to N^1(S)$. It is surjective by Corollary P5.5.3. $\square$

### Exercises

1. (A) Let $X$ be a projective scheme and $X_{\mathrm{red}}$ its reduction. Show that the curves on $X$ and on $X_{\mathrm{red}}$ are the same, that $L \equiv 0$ if and only if $L|_{X_{\mathrm{red}}} \equiv 0$, and that $N_1(X_{\mathrm{red}}) \to N_1(X)$ is an isomorphism.
2. (A) Let $X = X_1 \cup X_2$ be a projective scheme with two irreducible components. Show that $N_1(X)$ is spanned by the images of $N_1(X_1)$ and $N_1(X_2)$, and that $N^1(X) \to N^1(X_1) \oplus N^1(X_2)$ is injective.
3. (B) Show that $L \equiv 0$ if and only if $(L \cdot L_2 \cdots L_r \cdot V) = 0$ for every integral $V$ of dimension $r$ and every choice of $L_2, \dots, L_r$, and give an example of a line bundle $L$ on a surface with $L^2 = 0$ and $L \not\equiv 0$.
4. (B) Let $f \colon Y \to X$ be a finite surjective morphism of degree $d$ of projective varieties of dimension $n$, and $L$ a line bundle on $X$. Show that $(f^* L)^n = d \, (L^n)$, and prove that $f^* L \equiv 0$ implies $L \equiv 0$ without Lemma P7.2.6, using that $f^{-1}(C)$ is a curve for every curve $C$ on $X$.
5. (B) Let $C$ be a smooth projective curve and $f \colon C \to \mathbb{P}^1$ of degree $d$. Compute $f^* \colon N^1(\mathbb{P}^1) \to N^1(C)$ and $f_* \colon N_1(C) \to N_1(\mathbb{P}^1)$ in the bases $[\mathcal{O}(1)]$, $[\text{point}]$, $[C]$, $[\mathbb{P}^1]$, and check the projection formula.
6. (C) Let $X$ be the union of three lines in $\mathbb{P}^3$ through one point, not in a plane, with its reduced structure. Show that $\rho(X) = 3$ and that the restriction $N^1(\mathbb{P}^3) \to N^1(X)$ has image of rank $1$. What happens for three lines in a plane through one point?

### Lean

Mathlib has no numerical equivalence of line bundles. The project library models the numerical class of an $\mathbb{R}$-divisor as the function of its intersection numbers with curves: `MinimalModel.numClass` sends $D$ to $C \mapsto D \cdot C$, and `MinimalModel.N1` is the real span of the classes of the Cartier divisors, which is $N^1(X)$ of Definition P7.2.3 by construction. On the curve side, `MinimalModel.IntersectionData.curveClass` sends a curve to the function $D \mapsto D \cdot C$ on $\mathbb{R}$-Cartier divisors, and `MinimalModel.IntersectionData.N₁` is the span of these functions, which is $N_1(X)$ of Definition P7.2.4. The nondegeneracy of part 1 of Proposition P7.2.5 is built into both definitions. The handbook adds no `MinimalModel` node here.

### Notes and history

Numerical equivalence of divisors goes back to Severi, who compared algebraic and numerical equivalence on surfaces, and the systematic use of $N^1(X)$ and $N_1(X)$ as dual real vector spaces is Kleiman's, in *Toward a numerical theory of ampleness* (1966). The literature state is theorem. Lazarsfeld, Section 1.1.C, defines $N^1(X)$ as the quotient of the Cartier divisors by numerically trivial ones, as here, and remarks that intersection numbers of numerically trivial bundles vanish in all dimensions, Proposition P7.2.2. The lifting of curves through a surjective morphism, Lemma P7.2.6, is standard, and the same hyperplane argument proves a version relative to a base. On a smooth projective surface, Proposition P7.2.8 identifies the space here with the numerical group of P5 Ch. 5 and the cone language of P5 Ch. 12.
