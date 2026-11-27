---
title: Čech cohomology and Leray's theorem
nodes: []
sources: [Har77, God58, Stacks, Ser55]
reads_with: [Har77:ch3, Ser55:ch1]
requires: [P2.3, P2.4, P2.5, P2.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Čech cohomology and Leray's theorem

### Statement

Derived functors give the right groups but no way to compute them. Čech cohomology uses one open cover and the sections over its finite intersections. It is a finite computation in good cases, and Leray's theorem says when it gives the derived functor groups.

**Definition P2.7.18 (Čech complex).** Let $X$ be a space, $\mathcal{F}$ a presheaf of abelian groups and $\mathcal{U} = (U_i)_{i \in I}$ an open cover, with a well ordering of $I$. Write $U_{i_0 \cdots i_p} = U_{i_0} \cap \cdots \cap U_{i_p}$. The *Čech complex* has terms
$$\check{C}^p(\mathcal{U}, \mathcal{F}) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0 \cdots i_p}), \qquad p \geq 0,$$
and differential
$$(d \alpha)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k \, \alpha_{i_0 \cdots \widehat{i_k} \cdots i_{p+1}} \big|_{U_{i_0 \cdots i_{p+1}}}.$$
The *Čech cohomology* of $\mathcal{F}$ on $\mathcal{U}$ is $\check{H}^p(\mathcal{U}, \mathcal{F}) = H^p(\check{C}^\bullet(\mathcal{U}, \mathcal{F}))$. It is convenient to extend a cochain $\alpha$ to all index tuples by the alternating rule: $\alpha$ is $0$ on a tuple with a repeated index and changes sign when two indices are exchanged.

Lean: Mathlib `CategoryTheory.cechComplexFunctor`, which uses all tuples $\mathrm{Fin}(p + 1) \to I$ and not only increasing ones.

The complex over all tuples, used in Mathlib, has the same cohomology as the ordered one (Exercise 6). The ordered complex is shorter: for a cover by $n + 1$ open sets, $\check{C}^p = 0$ for $p > n$.

**Proposition P2.7.19 (first properties).** Let $\mathcal{F}$ be a sheaf and $\mathcal{U}$ an open cover.

1. $d^2 = 0$ and $\check{H}^0(\mathcal{U}, \mathcal{F}) = \Gamma(X, \mathcal{F})$.
2. For each $i_0 < \cdots < i_p$ let $f: U_{i_0 \cdots i_p} \to X$ be the inclusion, and put $\mathcal{C}^p(\mathcal{U}, \mathcal{F}) = \prod_{i_0 < \cdots < i_p} f_* (\mathcal{F}|_{U_{i_0 \cdots i_p}})$, with the Čech differential. Then $0 \to \mathcal{F} \to \mathcal{C}^0(\mathcal{U}, \mathcal{F}) \to \mathcal{C}^1(\mathcal{U}, \mathcal{F}) \to \cdots$ is a resolution of $\mathcal{F}$, and $\Gamma(X, \mathcal{C}^\bullet(\mathcal{U}, \mathcal{F})) = \check{C}^\bullet(\mathcal{U}, \mathcal{F})$.
3. There is a natural map $\check{H}^p(\mathcal{U}, \mathcal{F}) \to H^p(X, \mathcal{F})$ for each $p$, functorial in $\mathcal{F}$, and an isomorphism for $p = 0$.

Lean: not in Lean as stated.

**Theorem P2.7.20 (Čech cohomology of flasque sheaves).** If $\mathcal{F}$ is flasque, then $\check{H}^p(\mathcal{U}, \mathcal{F}) = 0$ for every open cover $\mathcal{U}$ and every $p > 0$. In particular this holds for every injective sheaf.

Lean: not in Lean as stated.

**Theorem P2.7.21 (Leray).** Let $\mathcal{F}$ be a sheaf and $\mathcal{U}$ an open cover with $H^q(U_{i_0 \cdots i_p}, \mathcal{F}) = 0$ for all $q > 0$ and all finite intersections $U_{i_0 \cdots i_p}$. Then the natural maps $\check{H}^p(\mathcal{U}, \mathcal{F}) \to H^p(X, \mathcal{F})$ are isomorphisms for all $p$. In particular, if $X$ is a separated scheme, $\mathcal{U}$ is a cover by open affine subschemes and $\mathcal{F}$ is quasi-coherent, then $\check{H}^p(\mathcal{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$.

Lean: not in Lean as stated.

**Theorem P2.7.22 ($\check{H}^1$ inside $H^1$).** Let $\mathcal{F}$ be a sheaf and $\mathcal{U}$ any open cover. The map $\check{H}^1(\mathcal{U}, \mathcal{F}) \to H^1(X, \mathcal{F})$ is injective, with image
$$\ker\Big( H^1(X, \mathcal{F}) \to \prod_i H^1(U_i, \mathcal{F}) \Big).$$
Over the directed system of open covers ordered by refinement, $\varinjlim_{\mathcal{U}} \check{H}^1(\mathcal{U}, \mathcal{F}) \cong H^1(X, \mathcal{F})$.

Lean: Mathlib `CategoryTheory.PresheafOfGroups.H1` and `CategoryTheory.PresheafOfGroups.OneCocycle` define $\check{H}^1$ of a cover for a presheaf of groups; the comparison with $H^1$ is not in Lean as stated.

### Proof in words

The sheafified Čech complex is a resolution, by a homotopy that inserts a fixed index $j$ in front: near a point of $U_j$ the formula $(k \alpha)_{i_0 \cdots i_{p-1}} = \alpha_{j i_0 \cdots i_{p-1}}$ makes sense and gives $dk + kd = 1$. Its global sections are the Čech complex. For a flasque sheaf the resolution consists of flasque sheaves, so it computes $H^p$, which is $0$. For Leray's theorem, form the double complex of Čech cochains with values in an injective resolution. Its rows are exact by the flasque case, so its total complex computes sheaf cohomology. Its columns compute the cohomology of $\mathcal{F}$ on the intersections, which vanishes by hypothesis, so the total complex also computes Čech cohomology. For $\check{H}^1$, embed $\mathcal{F}$ in a flasque sheaf. A class of $H^1$ is then a section of the quotient, and it comes from a Čech class exactly when it lifts on each $U_i$.

### Examples

**Example P2.7.23 (the cohomology of $\mathcal{O}(n)$ on $\mathbb{P}^1$).** Keep the notation of Example P2.6.9: $U_0 = \operatorname{Spec} k[t]$, $U_1 = \operatorname{Spec} k[s]$, $s = t^{-1}$, and a section of $\mathcal{O}(n)$ is a pair $(f, g)$ with $f \in k[t]$, $g \in k[s]$ and $f = t^n g(t^{-1})$ on $U_{01} = \operatorname{Spec} k[t, t^{-1}]$. The scheme $\mathbb{P}^1$ is separated, so Leray's theorem applies to this affine cover. Identify sections of $\mathcal{O}(n)$ over $U_{01}$ with $k[t, t^{-1}]$ through the trivialization on $U_0$. The Čech complex is
$$0 \to k[t] \oplus k[s] \xrightarrow{d} k[t, t^{-1}] \to 0, \qquad d(f, g) = t^n g(t^{-1}) - f.$$
The image of $d$ is spanned by the monomials $t^m$ with $m \geq 0$, from $f$, and those with $m \leq n$, from $g$. The kernel is the space of pairs with $f = t^n g(t^{-1})$, which is $\Gamma(\mathbb{P}^1, \mathcal{O}(n))$ as in Example P2.6.9. So
$$\dim_k H^0(\mathbb{P}^1, \mathcal{O}(n)) = \max(n + 1, 0), \qquad \dim_k H^1(\mathbb{P}^1, \mathcal{O}(n)) = \max(-n - 1, 0),$$
with $H^1$ spanned by the classes of $t^m$ for $n < m < 0$, and $H^p = 0$ for $p \geq 2$ because the complex has length $1$. In particular $H^1(\mathbb{P}^1, \mathcal{O}) = 0$ and $H^1(\mathbb{P}^1, \mathcal{O}(-1)) = 0$, while $H^1(\mathbb{P}^1, \mathcal{O}(-2)) \cong k$, spanned by $t^{-1}$. This fills in the value quoted in Example P2.5.25 and used in Example P2.7.7. The equality $h^0(\mathcal{O}(n)) - h^1(\mathcal{O}(n)) = n + 1$ for all $n$ is the Riemann-Roch theorem on $\mathbb{P}^1$. The canonical sheaf of $\mathbb{P}^1$ is $\mathcal{O}(-2)$ (Chapter 8), and the pairing $H^0(\mathcal{O}(n)) \times H^1(\mathcal{O}(-n-2)) \to H^1(\mathcal{O}(-2)) = k$ of Exercise 4 is Serre duality.

**Example P2.7.24 (the circle).** Let $X = S^1$ with its classical topology and $\mathcal{F} = \underline{\mathbb{Z}}$. Cover $X$ by two open arcs $U_0$ and $U_1$, each homeomorphic to an open interval, whose intersection is a disjoint union of two open intervals $W$ and $W'$. A constant sheaf on an open interval has no higher cohomology (Godement, Chapter II). So the cover satisfies the hypothesis of Leray's theorem. The Čech complex is
$$0 \to \mathbb{Z} \oplus \mathbb{Z} \xrightarrow{d} \mathbb{Z} \oplus \mathbb{Z} \to 0, \qquad d(a_0, a_1) = (a_1 - a_0, \ a_1 - a_0),$$
where the target records the values on $W$ and $W'$. The kernel is $\mathbb{Z}$, the constant functions, and the cokernel is $\mathbb{Z}$, spanned by the class of $(1, 0)$. So $H^0(S^1, \mathbb{Z}) = \mathbb{Z}$ and $H^1(S^1, \mathbb{Z}) = \mathbb{Z}$, as in singular cohomology. The cover of $X$ by the single open set $X$ gives $\check{H}^1 = 0$. It does not satisfy the hypothesis, and Theorem P2.7.22 says only that its $\check{H}^1$ is the subgroup of classes that vanish on $X$, which is $0$.

**Example P2.7.25 (a nonzero class on $\mathbb{C} \setminus \{0\}$).** Let $X = \mathbb{C} \setminus \{0\}$ and cover it by $U_0 = X \setminus \mathbb{R}_{> 0}$ and $U_1 = X \setminus \mathbb{R}_{< 0}$. On each $U_i$ the function $z$ has a logarithm $\ell_i$, and on $U_{01}$, the union of the upper and lower half planes, $(\ell_1 - \ell_0)/(2 \pi i)$ is a locally constant integer function, equal to $0$ on one half plane and $\pm 1$ on the other. This is a Čech $1$-cocycle of $\underline{\mathbb{Z}}$, and its class is the image of $z$ under the connecting map of Example P2.7.6. As in Example P2.7.24 it generates $\check{H}^1(\mathcal{U}, \mathbb{Z}) \cong \mathbb{Z}$. Theorem P2.7.22 makes this a nonzero class of $H^1(X, \mathbb{Z})$ without any assumption on the cover.

### Proof

*Proposition P2.7.19.* Part 1. In $d^2 \alpha$, each term $\alpha_{i_0 \cdots \widehat{i_k} \cdots \widehat{i_l} \cdots i_{p+2}}$ with $k < l$ appears twice, once with sign $(-1)^k (-1)^{l-1}$ and once with sign $(-1)^l (-1)^k$, so the terms cancel. A $0$-cochain $(\alpha_i)$ is a cocycle when $\alpha_j|_{U_{ij}} - \alpha_i|_{U_{ij}} = 0$ for all $i < j$. By the sheaf axioms these families are the global sections of $\mathcal{F}$.

Part 2. The sections of $\mathcal{C}^p(\mathcal{U}, \mathcal{F})$ over $V$ are $\prod \mathcal{F}(V \cap U_{i_0 \cdots i_p})$, so this is the Čech complex of $\mathcal{F}|_V$ for the cover $(V \cap U_i)$ of $V$, and the global sections are $\check{C}^\bullet(\mathcal{U}, \mathcal{F})$. Part 1 applied on each $V$ shows that $\mathcal{F} \to \mathcal{C}^0 \to \mathcal{C}^1$ is exact on sections, so the augmented complex is a complex of sheaves, exact at $\mathcal{F}$ and at $\mathcal{C}^0$. For exactness in degree $p \geq 1$, check on stalks. Let $x \in X$ and choose $j$ with $x \in U_j$. For an open $V \subseteq U_j$ containing $x$, define $k: \mathcal{C}^p(\mathcal{U}, \mathcal{F})(V) \to \mathcal{C}^{p-1}(\mathcal{U}, \mathcal{F})(V)$ by $(k \alpha)_{i_0 \cdots i_{p-1}} = \alpha_{j i_0 \cdots i_{p-1}}$, with the alternating rule. This makes sense because $V \cap U_{i_0 \cdots i_{p-1}} = V \cap U_{j i_0 \cdots i_{p-1}}$. A direct computation gives
$$(d k \alpha + k d \alpha)_{i_0 \cdots i_p} = \alpha_{i_0 \cdots i_p},$$
since $(k d \alpha)_{i_0 \cdots i_p} = \alpha_{i_0 \cdots i_p} - \sum_m (-1)^m \alpha_{j i_0 \cdots \widehat{i_m} \cdots i_p}$ and the sum is $(d k \alpha)_{i_0 \cdots i_p}$. The maps $k$ commute with restriction to smaller $V$, so they pass to the stalk at $x$. So the identity of the stalk complex in positive degrees is null homotopic, and the stalk complex is exact there.

Part 3. Choose an injective resolution $\mathcal{F} \to \mathcal{I}^\bullet$. By the comparison theorem (Theorem P2.3.11) there is a map of resolutions $\mathcal{C}^\bullet(\mathcal{U}, \mathcal{F}) \to \mathcal{I}^\bullet$ over the identity of $\mathcal{F}$, unique up to homotopy. Applying $\Gamma(X, -)$ and taking cohomology gives the map. Uniqueness up to homotopy makes it independent of the choices and functorial in $\mathcal{F}$. In degree $0$ both sides are $\Gamma(X, \mathcal{F})$. $\square$

*Theorem P2.7.20.* If $\mathcal{F}$ is flasque, each restriction $\mathcal{F}|_{U_{i_0 \cdots i_p}}$ is flasque, its pushforward is flasque by part 3 of Theorem P2.7.11, and a product of flasque sheaves is flasque. So $\mathcal{C}^\bullet(\mathcal{U}, \mathcal{F})$ is a flasque resolution of $\mathcal{F}$, and by part 2 of Theorem P2.7.11 and Proposition P2.7.19,
$$\check{H}^p(\mathcal{U}, \mathcal{F}) = H^p(\Gamma(X, \mathcal{C}^\bullet(\mathcal{U}, \mathcal{F}))) \cong H^p(X, \mathcal{F}) = 0 \qquad (p > 0).$$
Injective sheaves are flasque by part 1 of Theorem P2.7.11. $\square$

*Theorem P2.7.21.* Let $\mathcal{F} \to \mathcal{I}^\bullet$ be an injective resolution and form the first quadrant double complex $C^{p,q} = \check{C}^p(\mathcal{U}, \mathcal{I}^q)$, with the Čech differential as $d_h$ and the differential of $\mathcal{I}^\bullet$ as $d_v$. This is the double complex of Example P2.4.20.

The rows. For fixed $q$, the row $\check{C}^\bullet(\mathcal{U}, \mathcal{I}^q)$ is exact in positive degrees by Theorem P2.7.20, and its kernel in degree $0$ is $\Gamma(X, \mathcal{I}^q)$ by Proposition P2.7.19. By Corollary P2.4.16, $\Gamma(X, \mathcal{I}^\bullet) \to \operatorname{Tot}(C)$ is a quasi-isomorphism. So $H^n(\operatorname{Tot} C) \cong H^n(X, \mathcal{F})$.

The columns. For fixed $p$, the column is $\prod_{i_0 < \cdots < i_p} \mathcal{I}^\bullet(U_{i_0 \cdots i_p})$. The restriction of $\mathcal{I}^\bullet$ to $U_{i_0 \cdots i_p}$ is an injective resolution of $\mathcal{F}|_{U_{i_0 \cdots i_p}}$ by part 3 of Theorem P2.7.3, so the cohomology of the column in degree $q$ is $\prod H^q(U_{i_0 \cdots i_p}, \mathcal{F})$. This is $0$ for $q > 0$ by hypothesis, and the kernel in degree $0$ is $\check{C}^p(\mathcal{U}, \mathcal{F})$. By Corollary P2.4.16 with rows and columns exchanged, $\check{C}^\bullet(\mathcal{U}, \mathcal{F}) \to \operatorname{Tot}(C)$ is a quasi-isomorphism.

So $\check{H}^p(\mathcal{U}, \mathcal{F}) \cong H^p(\operatorname{Tot} C) \cong H^p(X, \mathcal{F})$. The composite is the natural map of Proposition P2.7.19, since both are induced by maps of resolutions of $\mathcal{F}$ that agree up to homotopy. For the last claim, on a separated scheme a finite intersection of open affines is affine, and a quasi-coherent sheaf on an affine scheme has no higher cohomology (P4 Ch. 1). $\square$

*Theorem P2.7.22.* Embed $\mathcal{F}$ in a flasque sheaf $\mathcal{G}$, for example by Proposition P2.7.12, and put $\mathcal{Q} = \mathcal{G}/\mathcal{F}$. For each $p$, let $\check{C}'^p \subseteq \check{C}^p(\mathcal{U}, \mathcal{Q})$ be the image of $\check{C}^p(\mathcal{U}, \mathcal{G})$. These form a subcomplex, and
$$0 \to \check{C}^\bullet(\mathcal{U}, \mathcal{F}) \to \check{C}^\bullet(\mathcal{U}, \mathcal{G}) \to \check{C}'^\bullet \to 0$$
is exact, since sections of $\mathcal{F}$ are the sections of $\mathcal{G}$ that map to $0$ in $\mathcal{Q}$. By Theorem P2.3.5 and $\check{H}^1(\mathcal{U}, \mathcal{G}) = 0$ (Theorem P2.7.20),
$$\check{H}^1(\mathcal{U}, \mathcal{F}) \cong Z'/\operatorname{im} \Gamma(X, \mathcal{G}), \qquad Z' = H^0(\check{C}'^\bullet).$$
An element of $Z'$ is a family $(q_i)$, $q_i \in \mathcal{Q}(U_i)$, that agrees on overlaps and such that each $q_i$ lifts to $\mathcal{G}(U_i)$. So $Z'$ is the set of $q \in \Gamma(X, \mathcal{Q})$ whose restriction to each $U_i$ lifts to $\mathcal{G}(U_i)$. On the other hand, $H^1(X, \mathcal{G}) = 0$ by part 2 of Theorem P2.7.11, so $H^1(X, \mathcal{F}) \cong \Gamma(X, \mathcal{Q})/\operatorname{im} \Gamma(X, \mathcal{G})$, and the same holds on each $U_i$. By naturality of the connecting map, the class of $q$ restricts to the class of $q|_{U_i}$ in $H^1(U_i, \mathcal{F})$, and this vanishes exactly when $q|_{U_i}$ lifts to $\mathcal{G}(U_i)$. So the inclusion $Z' \subseteq \Gamma(X, \mathcal{Q})$ induces an injection $\check{H}^1(\mathcal{U}, \mathcal{F}) \to H^1(X, \mathcal{F})$ whose image is the kernel of $H^1(X, \mathcal{F}) \to \prod_i H^1(U_i, \mathcal{F})$. Both constructions are induced by maps of resolutions of $\mathcal{F}$, so this injection is the natural map of Proposition P2.7.19.

For the colimit, a refinement $\mathcal{V}$ of $\mathcal{U}$, with a choice of $\lambda: J \to I$ such that $V_j \subseteq U_{\lambda(j)}$, gives a map $\check{H}^1(\mathcal{U}, \mathcal{F}) \to \check{H}^1(\mathcal{V}, \mathcal{F})$. It commutes with the maps to $H^1(X, \mathcal{F})$, because both are restrictions of the natural map. Since those maps are injective, the refinement maps do not depend on $\lambda$, and the colimit maps injectively to $H^1(X, \mathcal{F})$. For surjectivity, let $\xi \in H^1(X, \mathcal{F})$. By part 5 of Theorem P2.7.3 there is a cover $\mathcal{U}$ with $\xi|_{U_i} = 0$ for all $i$, so $\xi$ lies in the image of $\check{H}^1(\mathcal{U}, \mathcal{F})$. $\square$

### Exercises

1. (A) Show that if $I$ has $n + 1$ elements, then $\check{H}^p(\mathcal{U}, \mathcal{F}) = 0$ for $p > n$. Write out the complex for a cover by two open sets, and show that $\check{H}^1(\mathcal{U}, \mathcal{F}) = \mathcal{F}(U_0 \cap U_1)/(\mathcal{F}(U_0) + \mathcal{F}(U_1))$.
2. (A) Suppose that $X$ itself is one of the sets of the cover $\mathcal{U}$. Show that $\check{H}^p(\mathcal{U}, \mathcal{F}) = 0$ for $p > 0$, using the homotopy of Proposition P2.7.19 on global sections.
3. (B) *Mayer-Vietoris.* Let $X = U \cup V$ with $U$, $V$ open. Show that for an injective sheaf $\mathcal{I}$ the sequence $0 \to \mathcal{I}(X) \to \mathcal{I}(U) \oplus \mathcal{I}(V) \to \mathcal{I}(U \cap V) \to 0$ is exact. Deduce a long exact sequence $0 \to H^0(X, \mathcal{F}) \to H^0(U, \mathcal{F}) \oplus H^0(V, \mathcal{F}) \to H^0(U \cap V, \mathcal{F}) \to H^1(X, \mathcal{F}) \to \cdots$ for every sheaf $\mathcal{F}$.
4. (B) In Example P2.7.23, multiplication of sections gives maps $H^0(\mathcal{O}(n)) \otimes H^1(\mathcal{O}(-n-2)) \to H^1(\mathcal{O}(-2)) \cong k$. Using the monomial bases, show that this pairing is perfect for every $n \geq 0$.
5. (B) Cover $S^1$ by three open arcs, any two of which meet in one interval and with empty triple intersection. Compute the Čech complex of $\underline{\mathbb{Z}}$ and check that it gives $H^1(S^1, \mathbb{Z}) \cong \mathbb{Z}$ again.
6. (C) Let $\check{C}^\bullet_{\mathrm{full}}(\mathcal{U}, \mathcal{F})$ be the complex with terms $\prod_{(i_0, \ldots, i_p) \in I^{p+1}} \mathcal{F}(U_{i_0 \cdots i_p})$, over all tuples, with the same differential. Show that its sheafified version is again a resolution of $\mathcal{F}$ by the same homotopy, that it is flasque when $\mathcal{F}$ is flasque, and deduce that it has the same cohomology as the ordered complex whenever the cover satisfies the hypothesis of Leray's theorem. For the general case see the Stacks project, chapter Cohomology of sheaves.
7. (C) Let $X$ be a separated scheme that is covered by $n + 1$ open affine subschemes. Show that $H^i(X, \mathcal{F}) = 0$ for all $i > n$ and all quasi-coherent $\mathcal{F}$. Deduce that $H^i(\mathbb{P}^n, \mathcal{F}) = 0$ for $i > n$, and compare with Grothendieck vanishing.

### Lean

Mathlib defines the Čech complex of a presheaf for a family of objects in a category with finite products, `CategoryTheory.cechComplexFunctor`, as the complex over all tuples $\mathrm{Fin}(n + 1) \to I$ rather than increasing ones. It has nonabelian $\check{H}^1$ for a presheaf of groups, `CategoryTheory.PresheafOfGroups.H1`, built from `CategoryTheory.PresheafOfGroups.OneCocycle`. The Mayer-Vietoris sequence of Exercise 3 is `CategoryTheory.GrothendieckTopology.MayerVietorisSquare.sequence_exact` in the setting of Grothendieck topologies. The comparison of Čech cohomology with sheaf cohomology, Leray's theorem and the computation on $\mathbb{P}^1$ are not in Lean as stated.

### Notes and history

Čech cohomology goes back to Čech's work of the 1930s on the homology of general spaces, and Leray introduced the condition on the cover in his work on sheaves and spectral sequences. Serre's paper *Faisceaux algébriques cohérents* of 1955 developed coherent sheaf cohomology entirely with Čech cochains on affine covers, and computed the cohomology of projective space in this way. The full computation of $H^i(\mathbb{P}^n, \mathcal{O}(d))$, with $H^n(\mathbb{P}^n, \mathcal{O}(-n-1)) \cong k$, is in P4 Ch. 2 and follows the pattern of Example P2.7.23. The minimal model program uses Čech cochains mostly through Leray's theorem, to reduce statements about coherent cohomology to affine pieces.
