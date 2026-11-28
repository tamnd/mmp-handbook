---
title: Flipping curves of terminal 3-folds
nodes: []
sources: [KM98, Mor88, Kol96, KM92, Stacks, SGA1]
reads_with: [Kol96:II.1, KM92:1]
requires: [1.5, 4.4, 5.1, 6.3, P8.1, P7.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Flipping curves of terminal 3-folds

### Statement

The ground field is $\mathbb{C}$ when analytic germs appear, and otherwise an algebraically closed field of characteristic $0$. The index of a point of a normal variety with $\mathbb{Q}$-Cartier canonical class is as in Definition 4.4.13; a point of index $1$ is a Gorenstein point.

**Definition 8.2.1 (extremal neighbourhoods).** An *extremal neighbourhood* is a proper bimeromorphic morphism $f \colon (X \supset C) \to (Z \ni z)$ from the germ of a complex analytic 3-fold $X$ with terminal singularities along a connected compact curve $C$ to the germ of a normal 3-fold $Z$ at a point $z$, such that $f^{-1}(z) = C$ as sets and $-K_X$ is ample over $Z$. It is *flipping* if $\operatorname{Exc}(f) = C$, and *divisorial* if $\operatorname{Exc}(f)$ is a divisor. If $f \colon X \to Z$ is a flipping contraction of an algebraic 3-fold with terminal singularities and $z \in f(\operatorname{Exc}(f))$, the germ of $X$ along the fibre over $z$ is a flipping extremal neighbourhood.

**Proposition 8.2.2 (flipping curves are trees of rational curves).** Let $(X, \Delta)$ be a klt pair and $f \colon X \to Z$ a projective morphism onto a normal variety with $f_* \mathcal{O}_X = \mathcal{O}_Z$ and $-(K_X + \Delta)$ ample over $Z$. Then $R^j f_* \mathcal{O}_X = 0$ for $j > 0$. If a fibre $f^{-1}(z)$ has dimension $1$ and $C = f^{-1}(z)_{\mathrm{red}}$, then $H^1(C, \mathcal{O}_C) = 0$; every irreducible component of $C$ is isomorphic to $\mathbb{P}^1$, and the dual graph of $C$ has no cycles.

Lean: not yet in Lean.

**Proposition 8.2.3 (a flipping curve passes through a non-Gorenstein point).** Let $X$ be a 3-fold with terminal singularities and $f \colon X \to Z$ a flipping contraction of $X$. Then every connected component of $\operatorname{Exc}(f)$ contains a point of index at least $2$. In particular a 3-fold with terminal Gorenstein singularities, for instance a smooth 3-fold, has no flipping contractions.

Lean: not yet in Lean.

**Lemma 8.2.4 (finite generation is a local property at finitely many points).** Let $f \colon X \to Z$ be a small contraction of normal varieties, $D$ a Weil divisor on $X$, and suppose that $D_Z = f_* D$ is $\mathbb{Q}$-Cartier outside a finite set $S \subset Z$. For $z \in S$ let $R_z$ be the stalk of $R(X/Z, D)$ at $z$ and $\widehat{A}_z$ the completion of $A_z = \mathcal{O}_{Z,z}$. Then $R(X/Z, D)$ is finitely generated if and only if $R_z \otimes_{A_z} \widehat{A}_z$ is a finitely generated $\widehat{A}_z$-algebra for every $z \in S$.

Lean: not yet in Lean.

For a flipping contraction of a 3-fold, $\operatorname{Exc}(f)$ is a curve and $S = f(\operatorname{Exc}(f))$ is finite; outside $S$ the morphism $f$ is an isomorphism (Lemma 8.1.18), so $K_Z = f_* K_X$ is $\mathbb{Q}$-Cartier on $Z \setminus S$, as $K_X$ is $\mathbb{Q}$-Cartier on the terminal $X$. So Lemma 8.2.4 applies to $D = K_X$, and the existence of the flip is a question about the formal, or analytic, germ of $f$ over each point of $S$: the completion of $\bigoplus_m f_* \mathcal{O}_X(mK_X)$ at $z$ is the corresponding algebra of the formal germ, by the theorem on formal functions applied to each graded piece, and the comparison of formal and analytic germs (SGA1, Exposé XII) identifies it with the algebra of the analytic extremal neighbourhood. This is how Mori's theorem in Section 2, which is proved for analytic germs, gives algebraic flips.

### Proof in words

Kawamata-Viehweg vanishing over $Z$ kills $R^1 f_* \mathcal{O}_X$, and by the theorem on formal functions the first cohomology of every thickening of the fibre vanishes; on a curve the restriction maps on $H^1$ are surjective, so $H^1(\mathcal{O}_C) = 0$, which forces rational components and no cycles.

If $X$ were Gorenstein along a flipping curve $C$, it would be a local complete intersection there, by Reid's description of terminal Gorenstein points as isolated cDV hypersurface points. The deformation theory of maps $\mathbb{P}^1 \to X$ then gives a family of deformations of $C$ of dimension at least $-K_X \cdot C + 3 \ge 4$, and after dividing by the three-dimensional automorphism group of $\mathbb{P}^1$ a positive dimensional family of curves. These curves stay in the fibres of $f$, which contain only finitely many curves. This is the argument of Corollary 6.3.4 for smooth 3-folds, which works on any local complete intersection.

For Lemma 8.2.4, completion is faithfully flat, so generators of the completed algebra chosen in the algebra itself generate it; and a Veronese subalgebra generated in degree $1$ at the finitely many bad points is generated in degree $1$ everywhere, because elsewhere $D_Z$ is $\mathbb{Q}$-Cartier.

### Examples

**Example 8.2.5 (the Francia flipping curve).** In Proposition 8.1.13 the flipping curve $C^- \cong \mathbb{P}^1$ passes through one point of index $2$, the $\frac12(1,1,1)$ point, and $-K_{X^-} \cdot C^- = \frac12$. As $2K_{X^-}$ is Cartier, $-K_{X^-} \cdot C^- \in \frac12 \mathbb{Z}_{>0}$, and the Francia flip realises the least possible value. If $X^-$ were Gorenstein along $C^-$, the number $-K \cdot C^-$ would be a positive integer, and the estimate in the proof of Proposition 8.2.3 would apply.

**Example 8.2.6 (higher index).** In Example 8.1.14 the flipping curve passes through one point of type $\frac1n(1,1,-1)$, of index $n$, and $-K_{X^-} \cdot C^- = \frac{n-1}{n}$. So for every $n \ge 2$ there are flipping curves through a point of index $n$, and $-K \cdot C$ takes values in $(0, 1)$ arbitrarily close to $1$.

**Example 8.2.7 (the estimate is sharp).** In the Atiyah flop of Proposition 8.1.11, $X_1$ is smooth along $C_1$ and $K_{X_1} \cdot C_1 = 0$, so the estimate gives $\dim_{[\nu]} \operatorname{Hom}(\mathbb{P}^1, X_1) \ge 3$, which is just the automorphisms of $\mathbb{P}^1$. Indeed $H^0(C_1, N_{C_1/X_1}) = H^0(\mathcal{O}(-1)^{\oplus 2}) = 0$, so $C_1$ does not move, and the curve can be contracted by a small contraction. The contraction is a flopping one, not a flipping one: with $-K \cdot C \ge 1$ the curve would move.

### Proof

*Proposition 8.2.2.* The divisor $N = 0$ is Cartier and $N - (K_X + \Delta) = -(K_X + \Delta)$ is ample over $Z$, so it is $f$-nef and $f$-big, and Theorem 5.1.13 gives $R^j f_* \mathcal{O}_X = 0$ for $j > 0$.

Let $f^{-1}(z)$ have dimension $1$, let $\mathfrak{m} \subset \mathcal{O}_{Z,z}$ be the maximal ideal and $X_n \subset X$ the closed subscheme defined by $\mathfrak{m}^n \mathcal{O}_X$, for $n \ge 1$; these schemes have support $C$. By the theorem on formal functions (Stacks, the chapter on cohomology of schemes, the theorem on formal functions), $0 = (R^1 f_* \mathcal{O}_X)^\wedge_z = \varprojlim_n H^1(X_n, \mathcal{O}_{X_n})$. For $n \ge 1$ the surjection $\mathcal{O}_{X_{n+1}} \to \mathcal{O}_{X_n}$ has a coherent kernel supported on the curve $C$, whose $H^2$ vanishes, so $H^1(\mathcal{O}_{X_{n+1}}) \to H^1(\mathcal{O}_{X_n})$ is surjective. Likewise $H^1(\mathcal{O}_{X_1}) \to H^1(\mathcal{O}_C)$ is surjective. An inverse limit of a sequence of surjections maps onto each term, so $H^1(\mathcal{O}_C)$ is a quotient of $\varprojlim_n H^1(\mathcal{O}_{X_n}) = 0$.

Let $C' \subseteq C$ be a reduced subcurve. Then $\mathcal{O}_C \to \mathcal{O}_{C'}$ is surjective with kernel supported on a curve, so $H^1(\mathcal{O}_{C'}) = 0$. For an irreducible component $C' = C_i$, an integral projective curve with $H^1(\mathcal{O}_{C_i}) = 0$ has arithmetic genus $0$, and its normalisation $\nu \colon \mathbb{P}^1 \to C_i$ satisfies $h^1(\mathcal{O}_{C_i}) = \dim(\nu_* \mathcal{O}_{\mathbb{P}^1} / \mathcal{O}_{C_i}) = 0$, so $C_i \cong \mathbb{P}^1$. If the dual graph had a cycle, let $C'$ be the union of the components $C_1, \dots, C_k$ of the cycle, with $k \ge 2$, and $\nu \colon \bigsqcup_i C_i \to C'$ the normalisation of the configuration. The sequence $0 \to \mathcal{O}_{C'} \to \bigoplus_i \mathcal{O}_{C_i} \to Q \to 0$ has $Q$ a skyscraper sheaf with $h^0(Q) \ge k$, one for each edge of the cycle, so $h^1(\mathcal{O}_{C'}) \ge h^0(Q) - k + 1 \ge 1$, using $h^0(\mathcal{O}_{C'}) = 1$ for the connected $C'$ and $h^0(\bigoplus_i \mathcal{O}_{C_i}) = k$. This contradicts $H^1(\mathcal{O}_{C'}) = 0$.

*Proposition 8.2.3.* Suppose that a connected component $C'$ of $\operatorname{Exc}(f)$ consists of Gorenstein points of $X$. By Theorem 4.4.15 and Theorem 4.4.17, every point of $C'$ is a smooth point or an isolated cDV point (Definition 4.4.16), which is a hypersurface singularity; so a neighbourhood $U$ of $C'$ is a local complete intersection, and $K_X|_U$ is Cartier. Since $f$ is small, $\operatorname{Exc}(f)$ has dimension $1$, and by Proposition 8.2.2 every component of $C'$ is a smooth rational curve. Let $C$ be one of them and $\nu \colon \mathbb{P}^1 \to C \subset X$ the inclusion. As $-K_X$ is ample over $Z$ and Cartier along $C$, $-K_X \cdot C$ is a positive integer.

By the dimension estimate for local complete intersections (Kol96, Theorem II.1.3, the analogue of Corollary P8.1.12), every irreducible component of the Hom scheme $\operatorname{Hom}(\mathbb{P}^1, X)$ (Theorem P8.1.4) through $[\nu]$ has dimension at least
$$-K_X \cdot C + 3 \chi(\mathcal{O}_{\mathbb{P}^1}) = -K_X \cdot C + 3 \ge 4.$$
Let $H$ be such a component, with its reduced structure. Fix an ample Cartier divisor $A$ on the quasi-projective variety $Z$. For $[h] \in H$, the degree of $h^* f^* A$ is constant in the connected family $H$, and it is $0$ at $[\nu]$; so $f \circ h$ is constant for every $[h] \in H$, and $h(\mathbb{P}^1) \subseteq f^{-1}(f(h(\mathbb{P}^1)))$. The image $h(\mathbb{P}^1)$ is a curve contracted by $f$, so the point $f(h(\mathbb{P}^1))$ lies in the finite set $f(\operatorname{Exc}(f))$; as it depends continuously on $[h]$ in the connected $H$, it is $f(C)$, and every $h(\mathbb{P}^1)$ is contained in the fibre $f^{-1}(f(C))$, which has finitely many irreducible components $C_1, \dots, C_s$. A morphism $h$ near $[\nu]$ is birational onto its image, so the image is one of the curves $C_j$, and on the set of $[h] \in H$ with $h$ birational onto $C_j$ the group $\operatorname{Aut}(\mathbb{P}^1)$ acts transitively, as $h$ is then the normalisation of $C_j$ followed by an automorphism of $\mathbb{P}^1$. So a dense open subset of $H$ is a finite union of orbits of the 3-dimensional group $\operatorname{Aut}(\mathbb{P}^1)$, and $\dim H \le 3$. This contradicts $\dim H \ge 4$.

*Lemma 8.2.4.* Write $R = R(X/Z, D)$ and $R_m = f_* \mathcal{O}_X(mD)$, a coherent sheaf, as $f$ is proper. If $R$ is finitely generated near $z$, so is its base change $R_z \otimes \widehat{A}_z$.

Conversely, let $z \in S$ and suppose $R_z \otimes \widehat{A}_z$ is generated by finitely many homogeneous elements. Each graded piece $(R_m)_z \otimes \widehat{A}_z$ is generated over $\widehat{A}_z$ by elements of $(R_m)_z$, so there are homogeneous $x_1, \dots, x_r \in R_z$ whose images generate $R_z \otimes \widehat{A}_z$. Let $T = A_z[x_1, \dots, x_r] \subseteq R_z$. In each degree $m$, the cokernel $Q_m$ of $T_m \to (R_m)_z$ is a finite $A_z$-module with $Q_m \otimes \widehat{A}_z = 0$, since the monomials in the $x_i$ span $(R_m)_z \otimes \widehat{A}_z$ and $\widehat{A}_z$ is flat over $A_z$. As $\widehat{A}_z$ is faithfully flat over the local ring $A_z$, $Q_m = 0$. So $R_z = T$ is finitely generated.

Now suppose that $R_z$ is finitely generated for every $z \in S$. By part 3 of Lemma 8.1.5, applied to the stalks, which are again rings of the form of that lemma over $A_z$, and since $S$ is finite, there is $d \ge 1$ such that $(R_{kd})_z = (R_d)_z^k$ for every $k \ge 1$ and every $z \in S$, and such that $dD_Z$ is Cartier on $Z \setminus S$. On $Z \setminus S$, by Lemma 8.1.4, $R_{kd} = \mathcal{O}_Z(kdD_Z) = \mathcal{O}_Z(dD_Z)^{\otimes k}$ is invertible, so the multiplication map $\operatorname{Sym}^k R_d \to R_{kd}$ is surjective on $Z \setminus S$. It is surjective at the points of $S$ by the choice of $d$. So it is a surjective map of sheaves, and $R^{(d)}$ is generated over $\mathcal{O}_Z$ by the coherent sheaf $R_d$; it is finitely generated. By part 2 of Lemma 8.1.5, $R$ is finitely generated.

### Exercises

1. (A) Let $X$ be a 3-fold with terminal singularities, $f$ a flipping contraction and $C$ an irreducible flipping curve through exactly one singular point, of index $m$. Show that $-K_X \cdot C \in \frac1m \mathbb{Z}_{>0}$.
2. (A) Show that the dual graph argument in the proof of Proposition 8.2.2 also excludes two components meeting in two distinct points, and two components meeting in a single point with intersection scheme of length $2$.
3. (A) In Example 8.2.7, show that $H^1(C_1, N_{C_1/X_1}) = 0$, so that $\operatorname{Hom}(\mathbb{P}^1, X_1)$ is smooth of dimension $3$ at the inclusion.
4. (B) Let $C = C^+$ be the flipped curve of the Francia flip, with $N_{C/X^+} = \mathcal{O}(-1) \oplus \mathcal{O}(-2)$. Compute $h^0$ and $h^1$ of $N_{C/X^+}$, and explain why the estimate $-K \cdot C + 3$ is not useful for the flipped curve.
5. (B) Let $f \colon X \to Z$ be the contraction of the zero section of the total space of $\mathcal{O}(-1) \oplus \mathcal{O}(-2)$ over $\mathbb{P}^1$, which exists by Example 8.1.14 with $n = 2$. Show that the zero section is $K$-positive, so $f$ is not a flipping contraction, in accordance with Proposition 8.2.3.
6. (C) Let $X$ be the toric 3-fold of a circuit $u_1 + u_2 - a u_3 - b u_4 = 0$ with $a, b \ge 1$ coprime to each other and with $X^+$ smooth. Determine for which $(a, b)$ the other side $X^-$ is terminal and $K$-negative on $C^-$, and check Proposition 8.2.3 in each case.

### Lean

Nothing in this section is in Lean. The Hom scheme and the dimension estimate of Corollary P8.1.12 are not formalised in the project library.

### Notes and history

Proposition 8.2.2 is a standard consequence of Kawamata-Viehweg vanishing, and for terminal 3-folds it is in Mor88. Proposition 8.2.3 is due to Mori; it is the reason the 3-fold minimal model program cannot stay among Gorenstein varieties, and the reason Mori's flip theorem is about index at least $2$. The estimate of Kol96, Theorem II.1.3, is the deformation theory version of bend and break, which in Volume 6 gave Corollary 6.3.4. The reduction to analytic germs is used throughout Mor88 and KM92.
