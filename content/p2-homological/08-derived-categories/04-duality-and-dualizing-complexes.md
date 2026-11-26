---
title: Duality and dualizing complexes
nodes: []
sources: [Har66, Con00, Lip09, Har77, KM98, GR70, KKMS73, Kov00, Huy06]
reads_with: [Har66:ch5, Har77:ch3]
requires: [P2.6, P2.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Duality and dualizing complexes

### Statement

All schemes in this section are noetherian and separated, and all morphisms are of finite type. $D_{qc}(X)$ and $D^b_{coh}(X)$ are the full subcategories of $D(\mathcal{O}_X)$ of complexes with quasi-coherent cohomology, and of bounded complexes with coherent cohomology. Section 8.3 gives $Rf_*$ for a morphism $f: X \to Y$. Grothendieck duality says that $Rf_*$ has a right adjoint when $f$ is proper, and it computes the adjoint.

**Theorem P2.8.22 (Grothendieck duality).** Let $f: X \to Y$ be a morphism of schemes as above.

1. If $f$ is proper, $Rf_*: D_{qc}(X) \to D_{qc}(Y)$ has a right adjoint $f^!$, and for $K$ in $D^-_{coh}(X)$ and $G$ in $D^+_{qc}(Y)$ the adjunction sheafifies to an isomorphism
$$Rf_* R\mathcal{H}om_{\mathcal{O}_X}(K, f^! G) \cong R\mathcal{H}om_{\mathcal{O}_Y}(Rf_* K, G).$$
2. The functor $f^!: D^+_{qc}(Y) \to D^+_{qc}(X)$ extends to all $f$ of finite type, with $(g f)^! \cong f^! g^!$, and with $f^! = f^*$ for an open immersion.
3. If $f$ is smooth of relative dimension $n$, then $f^! G \cong Lf^* G \otimes \omega_{X/Y}[n]$, where $\omega_{X/Y} = \Omega^n_{X/Y}$.
4. If $f = i: Z \to X$ is a closed immersion, then $i^! G = R\mathcal{H}om_{\mathcal{O}_X}(i_* \mathcal{O}_Z, G)$, viewed as a complex of $\mathcal{O}_Z$-modules.

Lean: not in Lean as stated.

**Proposition P2.8.23 (closed immersions).** Let $i: Z \to X$ be a closed immersion with ideal $\mathcal{I}$, and for $G$ in $D^+(\mathcal{O}_X)$ let $i^\flat G = R\mathcal{H}om_{\mathcal{O}_X}(i_* \mathcal{O}_Z, G)$, a complex of $\mathcal{O}_Z$-modules.

1. For $F$ in $D^-(\mathcal{O}_Z)$, $\operatorname{Hom}_{D(\mathcal{O}_X)}(i_* F, G) \cong \operatorname{Hom}_{D(\mathcal{O}_Z)}(F, i^\flat G)$. So $i^\flat$ is right adjoint to $i_*$.
2. If $Z$ is an effective Cartier divisor, so that $\mathcal{I} = \mathcal{O}_X(-Z)$ is invertible, and $\mathcal{G}$ is a locally free $\mathcal{O}_X$-module, then
$$i^\flat \mathcal{G} \cong (\mathcal{G} \otimes \mathcal{O}_X(Z))|_Z [-1].$$
3. (Adjunction formula) If also $X$ is smooth over a field $k$ of dimension $n + 1$ and $Z$ is smooth, then $\omega_Z \cong (\omega_X \otimes \mathcal{O}_X(Z))|_Z$.

Lean: not in Lean as stated.

**Definition P2.8.24 (dualizing complex and canonical sheaf).** A *dualizing complex* on a noetherian scheme $X$ is an object $\omega^\bullet$ of $D^b_{coh}(X)$ that has a bounded complex of injectives as a replacement and for which the natural map $\mathcal{O}_X \to R\mathcal{H}om(\omega^\bullet, \omega^\bullet)$ is an isomorphism. Then $\mathbb{D} = R\mathcal{H}om(-, \omega^\bullet)$ is an anti-equivalence of $D^b_{coh}(X)$ with $\mathbb{D} \mathbb{D} \cong 1$. For $\pi: X \to \operatorname{Spec} k$ of finite type over a field, the complex $\omega_X^\bullet = \pi^! k$ is a dualizing complex. If $X$ is equidimensional of dimension $n$, then $\omega_X^\bullet$ has cohomology in degrees $-n$ to $0$, and the *canonical sheaf* of $X$ is
$$\omega_X = \mathcal{H}^{-n}(\omega_X^\bullet).$$

Lean: not in Lean as stated.

**Theorem P2.8.25 (Serre duality and the canonical sheaf).** Let $X$ be equidimensional of dimension $n$ and of finite type over a field $k$.

1. (Serre duality) If $X$ is proper, then for $K$ in $D^b_{coh}(X)$,
$$R\operatorname{Hom}(K, \omega_X^\bullet) \cong R\operatorname{Hom}_k(R\Gamma(X, K), k), \qquad \operatorname{Ext}^{-i}(K, \omega_X^\bullet) \cong H^i(X, K)^\vee.$$
2. (Local duality) For a closed point $x$ with local ring $A = \mathcal{O}_{X,x}$ and maximal ideal $\mathfrak{m}$, and a finitely generated $A$-module $M$, the local cohomology $H^i_{\mathfrak{m}}(M)$ is the Matlis dual of $\operatorname{Ext}^{-i}_A(M, \omega^\bullet_{X,x})$, after completion.
3. (Cohen-Macaulay case) $X$ is Cohen-Macaulay if and only if $\mathcal{H}^j(\omega_X^\bullet) = 0$ for $j \neq -n$. Then $\omega_X^\bullet \cong \omega_X[n]$, and if $X$ is also proper, $H^i(X, \mathcal{F})^\vee \cong \operatorname{Ext}^{n-i}(\mathcal{F}, \omega_X)$ for coherent $\mathcal{F}$, which is $H^{n-i}(X, \mathcal{F}^\vee \otimes \omega_X)$ for $\mathcal{F}$ locally free.
4. (Smooth case) If $X$ is smooth, $\omega_X \cong \Omega^n_{X/k}$, the sheaf of top degree differential forms.
5. (Normal case) If $X$ is normal and $j: U \to X$ is the inclusion of the smooth locus, then $\omega_X$ is reflexive of rank $1$ and $\omega_X = j_* \omega_U = j_* \Omega^n_U$. So $\omega_X \cong \mathcal{O}_X(K_X)$ for a Weil divisor $K_X$, the *canonical divisor*, which is unique up to linear equivalence.

Lean: not in Lean as stated.

**Theorem P2.8.26 (vanishing and rationality).** Let $k$ have characteristic $0$ and let $f: Y \to X$ be a resolution of singularities of a variety $X$ of dimension $n$, that is, $f$ is proper and birational and $Y$ is smooth.

1. (Grauert-Riemenschneider vanishing) $R^i f_* \omega_Y = 0$ for $i > 0$.
2. (Kempf's criterion) $X$ has rational singularities (Example P2.8.20) if and only if $X$ is normal and Cohen-Macaulay and $f_* \omega_Y = \omega_X$.

Lean: not in Lean as stated.

### Proof in words

Neeman's form of duality comes from Brown representability. The category $D_{qc}(X)$ is compactly generated, $Rf_*$ preserves sums, and a sum preserving exact functor out of a compactly generated triangulated category has a right adjoint. The content of the theorem is the computation of the adjoint: for a closed immersion it is the sheaf of local sections killed by the ideal, derived, and for a smooth morphism it is a twist by the top differential forms, with the trace map built from residues. Applied to the structure map of a variety, duality gives the dualizing complex, Serre duality and the canonical sheaf. The Cohen-Macaulay condition is the condition that this complex is one sheaf. Kempf's criterion then follows by applying duality to $f$ and comparing $Rf_* \mathcal{O}_Y$ with $\mathcal{O}_X$.

### Examples

**Example P2.8.27 (projective space).** Let $X = \mathbb{P}^n_k$. The Euler sequence $0 \to \Omega^1_X \to \mathcal{O}_X(-1)^{n+1} \to \mathcal{O}_X \to 0$ gives $\omega_X = \det \Omega^1_X \cong \det(\mathcal{O}_X(-1)^{n+1}) = \mathcal{O}_X(-n-1)$. Serre duality then reads $H^i(\mathbb{P}^n, \mathcal{O}(m)) \cong H^{n-i}(\mathbb{P}^n, \mathcal{O}(-m-n-1))^\vee$. For $n = 1$ this is the symmetry between $H^0(\mathcal{O}(m))$ and $H^1(\mathcal{O}(-m-2))$ of Example P2.7.23, and the pairing is that of Exercise 4 of Section 7.3. For $m = -n-1$ it gives $H^n(\mathbb{P}^n, \omega_X) \cong k$, the trace.

**Example P2.8.28 (hypersurfaces).** Let $P = \mathbb{P}^{n+1}_k$ and $X \subseteq P$ a hypersurface of degree $d$, possibly singular, with inclusion $i$. By Theorem P2.8.22, $\omega^\bullet_P = \omega_P[n+1]$ and $\omega^\bullet_X = i^! \omega_P[n+1]$. Proposition P2.8.23 with $\mathcal{G} = \omega_P = \mathcal{O}_P(-n-2)$ gives
$$\omega^\bullet_X \cong \mathcal{O}_X(d - n - 2)[n].$$
So every hypersurface is Cohen-Macaulay, and $\omega_X = \mathcal{O}_X(d - n - 2)$ is invertible. A plane cubic curve has $\omega_X \cong \mathcal{O}_X$, so genus $1$, even when it is nodal. A cubic surface has $\omega_X = \mathcal{O}_X(-1)$, so $-K_X$ is ample, and it is a del Pezzo surface. A quartic surface has $\omega_X \cong \mathcal{O}_X$, a K3 surface when it is smooth. A quintic threefold has $\omega_X \cong \mathcal{O}_X$, a Calabi-Yau threefold when it is smooth. For $d > n + 2$, $K_X$ is ample. These three cases, $K_X$ negative, zero and positive, are the three outcomes that the minimal model program sorts varieties into.

**Example P2.8.29 (two planes meeting at a point).** Let $A = k[x, y, z, w]/(x z, x w, y z, y w)$, the coordinate ring of the union $X$ of the planes $P_1 = V(z, w)$ and $P_2 = V(x, y)$ in $\mathbb{A}^4$, which meet only at the origin. So $X$ has dimension $2$. Let $\mathfrak{m} = (x, y, z, w)$ and $B_1 = k[x, y]$, $B_2 = k[z, w]$. The sequence
$$0 \to A \to B_1 \oplus B_2 \to k \to 0, \qquad a \mapsto (a|_{P_1}, a|_{P_2}), \quad (b_1, b_2) \mapsto b_1(0) - b_2(0),$$
is exact. The local cohomology sequence gives $0 \to H^0_{\mathfrak{m}}(k) = k \to H^1_{\mathfrak{m}}(A) \to H^1_{\mathfrak{m}}(B_1) \oplus H^1_{\mathfrak{m}}(B_2)$, since $H^0_{\mathfrak{m}}(B_i) = 0$. The last group is $0$, since $B_i$ is a regular ring of dimension $2$ and $\mathfrak{m} B_i$ is its maximal ideal. So $H^1_{\mathfrak{m}}(A) = k$ and $A$ has depth $1$ at the origin, less than its dimension. So $X$ is not Cohen-Macaulay. By local duality, $\mathcal{H}^{-1}(\omega_X^\bullet)$ is a skyscraper with stalk $k$ at the origin, and $\omega^\bullet_X$ has two nonzero cohomology sheaves, $\omega_X$ in degree $-2$ and $k$ in degree $-1$. More directly, the function equal to $1$ on $P_1 \setminus 0$ and $0$ on $P_2 \setminus 0$ is regular on $X \setminus 0$ and does not extend, which is the failure of the condition $S_2$ (Exercise 6).

### Proof

*Theorem P2.8.22.* Part 1 is Neeman's theorem in the form of Lipman's notes, Chapter 4. Part 2 uses Nagata's compactification: write $f = \bar{f} j$ with $j$ an open immersion and $\bar{f}$ proper, set $f^! = j^* \bar{f}^!$, and check that this does not depend on the factorization. Parts 3 and 4 identify $f^!$ for smooth morphisms and closed immersions, and are proved in Hartshorne, *Residues and duality*, Chapter III, with the signs and the compatibility with base change corrected in Conrad's book. Part 4 for finite morphisms follows from part 1 by the argument of Proposition P2.8.23. $\square$

*Proposition P2.8.23.* Part 1. On sheaves, a map $\varphi: i_* \mathcal{F} \to \mathcal{G}$ of $\mathcal{O}_X$-modules lands in the subsheaf of sections killed by $\mathcal{I}$, since $\mathcal{I}$ kills $i_* \mathcal{F}$. That subsheaf is $\mathcal{H}om_{\mathcal{O}_X}(\mathcal{O}_X/\mathcal{I}, \mathcal{G})$, a module over $\mathcal{O}_X/\mathcal{I} = i_* \mathcal{O}_Z$. So $\operatorname{Hom}_{\mathcal{O}_X}(i_* \mathcal{F}, \mathcal{G}) = \operatorname{Hom}_{\mathcal{O}_Z}(\mathcal{F}, i^{-1} \mathcal{H}om(i_* \mathcal{O}_Z, \mathcal{G}))$, and the functor $\mathcal{G} \mapsto \mathcal{H}om(i_* \mathcal{O}_Z, \mathcal{G})$ is right adjoint to the exact functor $i_*$. A right adjoint of an exact functor sends injectives to injectives. So, for an injective replacement $G \to J$, the complex $\mathcal{H}om(i_* \mathcal{O}_Z, J)$ is a complex of injective $\mathcal{O}_Z$-modules that represents $i^\flat G$. Then
$$\operatorname{Hom}_{D(\mathcal{O}_X)}(i_* F, G) = \operatorname{Hom}_K(i_* F, J) = \operatorname{Hom}_K(F, \mathcal{H}om(i_* \mathcal{O}_Z, J)) = \operatorname{Hom}_{D(\mathcal{O}_Z)}(F, i^\flat G),$$
by Theorem P2.8.10 at both ends and the sheaf adjunction, applied in each degree, in the middle.

Part 2. The exact sequence $0 \to \mathcal{O}_X(-Z) \to \mathcal{O}_X \to i_* \mathcal{O}_Z \to 0$ is a resolution of $i_* \mathcal{O}_Z$ by locally free sheaves. Locally free sheaves are acyclic for $\mathcal{H}om(-, \mathcal{G})$ in the first variable, since $\mathcal{E}xt^q(\mathcal{E}, \mathcal{G}) = 0$ for $q > 0$ when $\mathcal{E}$ is locally free. So $i^\flat \mathcal{G}$ is the complex
$$\mathcal{H}om(\mathcal{O}_X, \mathcal{G}) \to \mathcal{H}om(\mathcal{O}_X(-Z), \mathcal{G}), \quad \text{that is,} \quad \mathcal{G} \xrightarrow{s} \mathcal{G} \otimes \mathcal{O}_X(Z),$$
in degrees $0$ and $1$, where $s$ is the canonical section of $\mathcal{O}_X(Z)$. Locally $s$ is a nonzerodivisor and $\mathcal{G}$ is free, so the map is injective and its cokernel is $(\mathcal{G} \otimes \mathcal{O}_X(Z))|_Z$. So the complex is quasi-isomorphic to this cokernel placed in degree $1$, which is the claim.

Part 3. Let $\pi: X \to \operatorname{Spec} k$. By parts 2 and 3 of Theorem P2.8.22, $\omega_X^\bullet = \pi^! k = \omega_X[n+1]$ and $\omega_Z^\bullet = (\pi i)^! k = i^! \omega_X^\bullet$. By part 4 of that theorem and part 2 above, $i^! \omega_X[n+1] = (\omega_X \otimes \mathcal{O}_X(Z))|_Z [n]$. Since $Z$ is smooth of dimension $n$, also $\omega_Z^\bullet = \omega_Z[n]$, and taking $\mathcal{H}^{-n}$ gives the formula. $\square$

*Theorem P2.8.25.* Part 1 is Theorem P2.8.22 for the proper map $\pi: X \to \operatorname{Spec} k$, with $R\pi_* = R\Gamma(X, -)$, after taking global sections. Part 2 is the local form of duality; see Hartshorne, *Residues and duality*, Chapter V. Part 3: $X$ is Cohen-Macaulay at $x$ if and only if $H^i_{\mathfrak{m}}(\mathcal{O}_{X,x}) = 0$ for $i < \dim \mathcal{O}_{X,x}$, and by part 2 with $M = A$ this is the vanishing of $\mathcal{H}^{-i}(\omega_X^\bullet)_x$ for those $i$; the normalization of $\pi^! k$ puts the top degree at $-\dim \mathcal{O}_{X,x}$ at closed points. Then a complex with one cohomology sheaf is that sheaf, shifted, and the formula for $H^i$ is part 1. Part 4 is part 3 of Theorem P2.8.22 for $X \to \operatorname{Spec} k$. Part 5: on $U$, part 4 gives $\omega_U = \Omega^n_U$, invertible. The sheaf $\omega_X$ satisfies Serre's condition $S_2$, and the complement of $U$ has codimension at least $2$ since $X$ is normal. An $S_2$ sheaf on a normal variety is determined by its restriction to such a $U$, so $\omega_X = j_* \omega_U$. A rational section of $\omega_U$ has a divisor on $U$, which extends to a Weil divisor $K_X$ on $X$ with $\mathcal{O}_X(K_X) = j_* \omega_U$. See Kollár-Mori, Chapter 5, and Hartshorne, *Algebraic geometry*, Chapter III. $\square$

*Theorem P2.8.26.* Part 1 is due to Grauert and Riemenschneider in the analytic setting; algebraic proofs reduce it to Kodaira vanishing. See Kollár-Mori, Chapter 2.

Part 2. Since $Y$ is smooth, $\omega_Y^\bullet = \omega_Y[n]$, and $\omega_Y^\bullet = f^! \omega_X^\bullet$ by part 2 of Theorem P2.8.22. Duality for the proper map $f$, with $K = \mathcal{O}_Y$, gives
$$Rf_* \omega_Y[n] = Rf_* R\mathcal{H}om(\mathcal{O}_Y, f^! \omega_X^\bullet) \cong R\mathcal{H}om(Rf_* \mathcal{O}_Y, \omega_X^\bullet). \tag{$*$}$$
By part 1, the left side is $f_* \omega_Y[n]$. Suppose $X$ has rational singularities. Then $Rf_* \mathcal{O}_Y = \mathcal{O}_X$, so $\omega_X^\bullet \cong f_* \omega_Y[n]$ has one cohomology sheaf. So $X$ is Cohen-Macaulay by Theorem P2.8.25, and $\omega_X = f_* \omega_Y$. It is normal, since $f_* \mathcal{O}_Y = \mathcal{O}_X$ with $Y$ normal. Conversely, suppose $X$ is normal and Cohen-Macaulay with $f_* \omega_Y = \omega_X$. Then $\omega_X^\bullet = \omega_X[n]$, and $(*)$ says that $\mathbb{D}(Rf_* \mathcal{O}_Y) \cong \omega_X[n] = \mathbb{D}(\mathcal{O}_X)$, compatibly with the map $\mathcal{O}_X \to Rf_* \mathcal{O}_Y$. Applying $\mathbb{D}$ and $\mathbb{D}\mathbb{D} \cong 1$ (Definition P2.8.24) gives $\mathcal{O}_X \cong Rf_* \mathcal{O}_Y$. $\square$

### Exercises

1. (A) Use Example P2.8.27 and Serre duality to compute $h^i(\mathbb{P}^2, \mathcal{O}(m))$ for $i = 1, 2$ and all $m$, from $h^0$.
2. (A) Use the adjunction formula to show that a smooth plane curve of degree $d$ has $\omega_C \cong \mathcal{O}_C(d - 3)$ and genus $(d-1)(d-2)/2$.
3. (B) Let $X \subseteq \mathbb{P}^N$ be a complete intersection of hypersurfaces of degrees $d_1, \ldots, d_r$. Show by induction with Proposition P2.8.23 that $\omega_X \cong \mathcal{O}_X(d_1 + \cdots + d_r - N - 1)$ and that $\omega_X^\bullet = \omega_X[N - r]$.
4. (B) Show that a reduced curve is Cohen-Macaulay, so that $\omega_C^\bullet = \omega_C[1]$. For the nodal cubic, show that $\omega_C \cong \mathcal{O}_C$ while $\Omega^1_C$ is not invertible at the node, so that $\omega_C$ and $\Omega^1_C$ differ.
5. (B) Let $X = V(x y - z^2) \subseteq \mathbb{A}^3$ and let $f: Y \to X$ be the blow-up of the vertex, with exceptional curve $E \cong \mathbb{P}^1$. Show that $\omega_X \cong \mathcal{O}_X$ and that $\omega_Y \cong f^* \omega_X$, using the adjunction formula on $Y$ and $E^2 = -2$. Granting $R^1 f_* \mathcal{O}_Y = 0$, verify Kempf's criterion.
6. (C) In Example P2.8.29, show directly that the function equal to $1$ on $P_1 \setminus 0$ and $0$ on $P_2 \setminus 0$ is regular on $X \setminus 0$ and does not lie in $A$. Deduce $H^1_{\mathfrak{m}}(A) \neq 0$ from the exact sequence $0 \to H^0_{\mathfrak{m}}(A) \to A \to \Gamma(X \setminus 0, \mathcal{O}_X) \to H^1_{\mathfrak{m}}(A) \to 0$. Show also that the normalization of $X$ is $P_1 \sqcup P_2$ and that $X$ has no rational singularities in the sense of Example P2.8.20.

### Lean

Mathlib has no Grothendieck duality, no functor $f^!$, no dualizing complex, no local cohomology of sheaves in this form, no Serre duality and no canonical sheaf of a singular variety. All statements of this section are marked "not in Lean as stated". The derived category of an abelian category exists in Mathlib (Section 8.2), but the derived category of quasi-coherent sheaves on a scheme, which duality needs, does not. The handbook adds no `MinimalModel` node here.

### Notes and history

Grothendieck found the duality theorem for coherent sheaves in the late 1950s, and it was the first motivation for derived categories. Hartshorne wrote it down in *Residues and duality* (1966) from Grothendieck's notes, and Deligne and Verdier gave the existence of $f^!$ by abstract arguments. Neeman's proof by Brown representability, written up by Lipman, is now standard, and Conrad's book corrects the signs and checks the compatibilities in the original approach. The criterion of Theorem P2.8.26 is due to Kempf, in the book of Kempf, Knudsen, Mumford and Saint-Donat. Kovács showed that $X$ has rational singularities as soon as $\mathcal{O}_X \to Rf_* \mathcal{O}_Y$ has a left inverse in $D(\mathcal{O}_X)$, which is the form used for the rationality of klt and log terminal singularities. P4 Ch. 9 develops duality for the applications, and Volumes 4 and 5 use it through the canonical sheaf and Theorem P2.8.26.
