---
title: The sheaf of relative differentials
nodes: []
sources: [Vak25, Har77, Stacks]
reads_with: [Vak25:ch21, Har77:II.8]
requires: [P1.12, P3.2, P3.3, P3.5, P3.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The sheaf of relative differentials

### Statement

Let $f \colon X \to S$ be a morphism of schemes. A *pair of affine opens* for $f$ is a pair $(U, V)$ of affine opens $V = \operatorname{Spec} A \subseteq S$ and $U = \operatorname{Spec} B \subseteq f^{-1}(V)$, so that $B$ is an $A$-algebra. For an $\mathcal{O}_X$-module $\mathcal{F}$, an *$S$-derivation* $D \colon \mathcal{O}_X \to \mathcal{F}$ is a morphism of sheaves of abelian groups with $D(gh) = g D(h) + h D(g)$ for local sections $g, h$ of $\mathcal{O}_X$, and with $D(f^\sharp a) = 0$ for every local section $a$ of $f^{-1} \mathcal{O}_S$. The $S$-derivations form a group $\operatorname{Der}_S(\mathcal{O}_X, \mathcal{F})$. Write $\Omega_{B/A}$ for the module of Kähler differentials of Definition P1.12.2.

**Lemma P3.12.1 (open immersions have no differentials).** Let $A \to B \to C$ be ring maps such that $\operatorname{Spec} C \to \operatorname{Spec} B$ is an open immersion. Then $\Omega_{C/B} = 0$, and the natural map $\Omega_{B/A} \otimes_B C \to \Omega_{C/A}$ is an isomorphism.

Lean: Mathlib `KaehlerDifferential.isLocalizedModule` is the case $C = B_g$ (proved in Mathlib). The lemma is not in Lean as stated.

**Theorem P3.12.2 (the sheaf of relative differentials).** Let $f \colon X \to S$ be a morphism of schemes.

1. There is a quasi-coherent $\mathcal{O}_X$-module $\Omega_{X/S}$ with an $S$-derivation $d \colon \mathcal{O}_X \to \Omega_{X/S}$ such that for every pair of affine opens $(U, V)$, $U = \operatorname{Spec} B$, $V = \operatorname{Spec} A$, there is an isomorphism $\Omega_{X/S}|_U \cong \widetilde{\Omega_{B/A}}$ under which $d$ on global sections is $d \colon B \to \Omega_{B/A}$.
2. For every $\mathcal{O}_X$-module $\mathcal{F}$, composition with $d$ is a bijection $\operatorname{Hom}_{\mathcal{O}_X}(\Omega_{X/S}, \mathcal{F}) \cong \operatorname{Der}_S(\mathcal{O}_X, \mathcal{F})$. So the pair $(\Omega_{X/S}, d)$ is unique up to a unique isomorphism.
3. If $f$ is locally of finite type, $\Omega_{X/S}$ is of finite type. If $f$ is locally of finite presentation, $\Omega_{X/S}$ is of finite presentation. In particular, if $X$ is locally Noetherian and $f$ is locally of finite type, $\Omega_{X/S}$ is coherent.
4. Let $S' \to S$ be a morphism, $X' = X \times_S S'$, and $g \colon X' \to X$ the projection. Then $g^* \Omega_{X/S} \cong \Omega_{X'/S'}$. In particular, for $s \in S$ the restriction of $\Omega_{X/S}$ to the fibre $X_s$ is $\Omega_{X_s/\kappa(s)}$.
5. $\Omega_{\mathbb{A}^n_S/S}$ is free with basis $dx_1, \dots, dx_n$.

Lean: Mathlib has the module `KaehlerDifferential` with notation `Ω[B⁄A]`, the derivation `KaehlerDifferential.D`, the base change `KaehlerDifferential.tensorKaehlerEquiv` and the basis `KaehlerDifferential.mvPolynomialBasis` of part 5 for rings (all in Mathlib). The sheaf $\Omega_{X/S}$ on a scheme is not in Mathlib.

The module $\Omega_{X/S}$ is the *sheaf of relative differentials* of $X$ over $S$. When $S = \operatorname{Spec} A$ write $\Omega_{X/A}$, and when the base is clear, $\Omega_X$. For $x \in X$ write $\Omega_{X/S}(x) = \Omega_{X/S, x} \otimes \kappa(x)$ for the fibre.

**Definition P3.12.3 (conormal sheaf).** Let $i \colon Z \to X$ be a closed immersion with ideal sheaf $\mathcal{I}$ (Proposition P3.5.23). The *conormal sheaf* of $Z$ in $X$ is the quasi-coherent $\mathcal{O}_Z$-module $\mathcal{C}_{Z/X} = i^*\mathcal{I} = i^{-1}(\mathcal{I}/\mathcal{I}^2)$. If $\mathcal{C}_{Z/X}$ is locally free, its dual $\mathcal{N}_{Z/X} = \mathcal{H}om(\mathcal{C}_{Z/X}, \mathcal{O}_Z)$ is the *normal sheaf*.

Lean: not in Lean as stated.

**Theorem P3.12.4 (the two exact sequences).**

1. For morphisms $X \xrightarrow{f} Y \xrightarrow{g} S$ the sequence
$$
f^* \Omega_{Y/S} \longrightarrow \Omega_{X/S} \longrightarrow \Omega_{X/Y} \longrightarrow 0
$$
is exact, where the first map sends $1 \otimes dh$ to $d(f^\sharp h)$ and the second sends $dh$ to $dh$.
2. Let $X \to S$ be a morphism and $i \colon Z \to X$ a closed immersion with ideal sheaf $\mathcal{I}$. Then the sequence
$$
\mathcal{C}_{Z/X} \xrightarrow{\ \delta\ } i^* \Omega_{X/S} \longrightarrow \Omega_{Z/S} \longrightarrow 0
$$
is exact, where $\delta$ sends the class of a local section $h$ of $\mathcal{I}$ to $1 \otimes dh$. This is the *conormal sequence*.

Lean: Mathlib `KaehlerDifferential.exact_mapBaseChange_map` is the first fundamental sequence and `KaehlerDifferential.exact_kerCotangentToTensor_mapBaseChange` is the conormal sequence for rings, with the map `KaehlerDifferential.kerCotangentToTensor` (proved in Mathlib). The sheaf versions are not in Lean.

### Proof in words

On an affine piece the sheaf is the module of differentials, and the only point is that these modules agree on overlaps. Shrinking an affine open to a smaller one is a localization, and a localization has no differentials of its own: $d(1/g) = -dg/g^2$ is forced. The same is true on the base. So the modules of differentials of two affine pieces restrict to the same module on each common distinguished open, and they glue. The universal property, the base change and the exact sequences are the statements of P1 Ch. 12, which are local and so pass to the sheaf.

### Examples

**Example P3.12.5 (the fibres of a family).** Let $k$ be a field, $S = \operatorname{Spec} k[t]$, and $X = V(xy - t) \subseteq \mathbb{A}^2_S$, so $X = \operatorname{Spec} B$ with $B = k[t, x, y]/(xy - t) \cong k[x, y]$. By parts 2 and 5 of Theorem P3.12.4 and Theorem P3.12.2,
$$
\Omega_{X/S} = (B\,dx \oplus B\,dy)/(y\,dx + x\,dy) ,
$$
since $dt = 0$ in $\Omega_{X/S}$. Over a point $t = c \neq 0$ the fibre is the smooth conic $xy = c$, and at each of its points $x$ or $y$ is a unit, so $\Omega_{X/S}$ restricted to the fibre is free of rank one, in agreement with part 4. Over $t = 0$ the fibre is the pair of lines $xy = 0$, and at the origin the relation $y\,dx + x\,dy$ vanishes in the fibre, so $\Omega_{X/S}(0) = \kappa(0)^2$ has dimension $2$. The fibre dimension of $\Omega_{X/S}$ jumps at the singular point of the singular fibre. As an absolute scheme $X \cong \mathbb{A}^2_k$ and $\Omega_{X/k}$ is free of rank $2$; the first sequence of Theorem P3.12.4 is $B\,dt \to \Omega_{X/k} \to \Omega_{X/S} \to 0$, with $dt \mapsto y\,dx + x\,dy$.

**Example P3.12.6 (the projective line).** Let $k$ be a field and $\mathbb{P}^1_k = \operatorname{Proj} k[x_0, x_1]$, with $t = x_1/x_0$ on $U_0 = D_+(x_0)$ and $s = x_0/x_1$ on $U_1 = D_+(x_1)$. By part 5 of Theorem P3.12.2, $\Omega = \Omega_{\mathbb{P}^1/k}$ is free on $U_0$ with basis $dt$ and on $U_1$ with basis $ds$. On $U_0 \cap U_1 = \operatorname{Spec} k[t, t^{-1}]$, $s = t^{-1}$ and
$$
ds = -t^{-2}\,dt .
$$
So $\Omega$ is invertible. By Example P3.6.16 the sheaf $\mathcal{O}(-2)$ is free on $U_0$ with generator $x_0^{-2}$ and on $U_1$ with generator $x_1^{-2} = t^{-2} x_0^{-2}$. The map that sends $dt \mapsto x_0^{-2}$ and $ds \mapsto -x_1^{-2}$ agrees on the overlap, so $\Omega_{\mathbb{P}^1_k/k} \cong \mathcal{O}(-2)$. A global section is a form $a(t)\,dt$ with $a \in k[t]$ that is regular on $U_1$; there it is $-a(s^{-1}) s^{-2}\,ds$, which is regular in $s$ only if $a = 0$. So $\Gamma(\mathbb{P}^1_k, \Omega) = 0$, as $\Gamma(\mathcal{O}(-2)) = 0$ by Theorem P3.6.12.

**Example P3.12.7 (the node).** Let $\operatorname{char} k \neq 2$ and $X = V(y^2 - x^2 - x^3) \subseteq \mathbb{A}^2_k$, $X = \operatorname{Spec} B$. By the conormal sequence,
$$
\Omega_{X/k} = (B\,dx \oplus B\,dy)/\big(2y\,dy - (2x + 3x^2)\,dx\big) .
$$
At a point of $X$ other than the origin, $y$ or $2x + 3x^2$ is a unit, so $\Omega_{X/k}$ is free of rank one near the point. At the origin the relation lies in $\mathfrak{m}(B\,dx \oplus B\,dy)$, so $\Omega_{X/k}(0)$ has dimension $2$, which is the dimension of the cotangent space $\mathfrak{m}/\mathfrak{m}^2$ (Proposition P1.12.9 and Example P1.12.10). The fibre dimension is $1$ on a dense open set and $2$ at the node.

**Example P3.12.8 (the Frobenius morphism).** Let $k$ have characteristic $p > 0$ and $F \colon \mathbb{A}^1_k = \operatorname{Spec} k[t] \to \mathbb{A}^1_k = \operatorname{Spec} k[u]$ the morphism with $F^\sharp(u) = t^p$. Then $\Omega_{\mathbb{A}^1/\mathbb{A}^1} = k[t]\,dt/(d(t^p)) = k[t]\,dt$, since $d(t^p) = p t^{p-1}\,dt = 0$. So $F$ is finite and bijective on points, and its relative differentials are free of rank one. In the first sequence of Theorem P3.12.4 the map $F^* \Omega_{\mathbb{A}^1/k} \to \Omega_{\mathbb{A}^1/k}$ sends $1 \otimes du$ to $d(t^p) = 0$: the Frobenius kills all differentials. In characteristic $0$ the morphism $u \mapsto t^p$ has $\Omega_{\mathbb{A}^1/\mathbb{A}^1} = k[t]/(t^{p-1})\,dt$, supported at the one point where $F$ is ramified.

### Proof

*Proof of Lemma P3.12.1.* First let $C = B_g$. Then $\Omega_{B_g/A} \cong \Omega_{B/A} \otimes_B B_g$ by Proposition P1.12.8, and $\Omega_{B_g/B} = \Omega_{B/B} \otimes_B B_g = 0$ by the same proposition. In general let $W = \operatorname{Spec} C$, viewed as an open subset of $\operatorname{Spec} B$. Choose $g_1, \dots, g_m \in B$ with $W = \bigcup_i D(g_i)$; this is possible as $W$ is quasi-compact. The image $\bar g_i$ of $g_i$ in $C$ defines $D(\bar g_i) = D(g_i) \subseteq W$, and both $C_{\bar g_i}$ and $B_{g_i}$ are the ring of this affine open, so $C_{\bar g_i} = B_{g_i}$. Since the $D(\bar g_i)$ cover $\operatorname{Spec} C$, the $\bar g_i$ generate the unit ideal of $C$. Localize the map $\varphi \colon \Omega_{B/A} \otimes_B C \to \Omega_{C/A}$ at $\bar g_i$. By the first case applied to $C$ and to $B$,
$$
(\Omega_{C/A})_{\bar g_i} \cong \Omega_{C_{\bar g_i}/A} = \Omega_{B_{g_i}/A} \cong \Omega_{B/A} \otimes_B B_{g_i} = (\Omega_{B/A} \otimes_B C)_{\bar g_i} ,
$$
and this composite is $\varphi_{\bar g_i}$, as both send $db \otimes 1$ to $db$. So $\varphi_{\bar g_i}$ is an isomorphism for every $i$, and $\varphi$ is an isomorphism: its kernel and cokernel are $C$-modules that vanish after inverting each $\bar g_i$, so they are zero. In the same way $(\Omega_{C/B})_{\bar g_i} = \Omega_{B_{g_i}/B} = 0$ for every $i$, so $\Omega_{C/B} = 0$. $\square$

*Proof of Theorem P3.12.2.* We first compare two pairs of affine opens. Let $(U, V)$ and $(U', V')$ be pairs with $U' \subseteq U$ and $V' \subseteq V$, $U = \operatorname{Spec} B$, $U' = \operatorname{Spec} B'$, $V = \operatorname{Spec} A$, $V' = \operatorname{Spec} A'$. We claim that the natural map
$$
\Omega_{B/A} \otimes_B B' \longrightarrow \Omega_{B'/A'} , \qquad db \otimes b' \mapsto b'\,db , \tag{$*$}
$$
is an isomorphism. It factors as $\Omega_{B/A} \otimes_B B' \to \Omega_{B'/A} \to \Omega_{B'/A'}$. The first map is an isomorphism by Lemma P3.12.1 for $A \to B \to B'$. For the second, the first fundamental sequence (Theorem P1.12.5) for $A \to A' \to B'$ is
$$
\Omega_{A'/A} \otimes_{A'} B' \to \Omega_{B'/A} \to \Omega_{B'/A'} \to 0 ,
$$
and $\Omega_{A'/A} = 0$ by Lemma P3.12.1 for $A \to A \to A'$. So the second map is an isomorphism as well, which proves the claim.

(1) For each pair of affine opens $(U, V)$ we have the quasi-coherent sheaf $\mathcal{F}_{U,V} = \widetilde{\Omega_{B/A}}$ on $U$. For a pair $(U', V')$ as above, $(*)$ and part 2 of Proposition P3.5.3, applied to the open immersion $U' \to U$, give an isomorphism $\mathcal{F}_{U,V}|_{U'} \cong \mathcal{F}_{U',V'}$, since the restriction of $\widetilde{M}$ to the affine open $U'$ is $(M \otimes_B B')^\sim$. These isomorphisms are compatible with each other for three nested pairs, since each sends $db$ to $db$, and the elements $db$ generate. The sheaf does not depend on $V$: for two pairs $(U, V_1)$ and $(U, V_2)$, $f(U) \subseteq V_1 \cap V_2$, so every point of $U$ has an affine neighbourhood $U' \subseteq U$ with $f(U')$ in an affine open $V' \subseteq V_1 \cap V_2$, and on $U'$ both sheaves are identified with $\mathcal{F}_{U',V'}$ by $(*)$. Now the pairs of affine opens cover $X$, and for two of them, $(U_1, V_1)$ and $(U_2, V_2)$, the intersection $U_1 \cap U_2$ is covered by affine opens $U'$ with $f(U')$ in an affine open $V' \subseteq V_1 \cap V_2$. On each such $U'$ both $\mathcal{F}_{U_1, V_1}$ and $\mathcal{F}_{U_2, V_2}$ are identified with $\mathcal{F}_{U', V'}$, and these identifications agree on smaller pairs. So the sheaves glue (Theorem P2.5.35) to a quasi-coherent sheaf $\Omega_{X/S}$ with $\Omega_{X/S}|_U \cong \mathcal{F}_{U,V}$. The derivations $d \colon B \to \Omega_{B/A}$ are compatible with $(*)$, so they glue to a morphism of sheaves $d \colon \mathcal{O}_X \to \Omega_{X/S}$, which is an $S$-derivation, as the Leibniz rule and $d(f^\sharp a) = 0$ hold on each $U$.

(2) Let $D \colon \mathcal{O}_X \to \mathcal{F}$ be an $S$-derivation. For a pair $(U, V)$, $D$ on sections over $U$ is an $A$-derivation $B \to \mathcal{F}(U)$, so by Proposition P1.12.3 there is a unique $B$-linear map $\Omega_{B/A} \to \mathcal{F}(U)$ with $db \mapsto D(b)$. By Theorem P3.5.2 it corresponds to a unique morphism $\psi_U \colon \Omega_{X/S}|_U \to \mathcal{F}|_U$. On a smaller pair $(U', V')$ the restriction of $\psi_U$ and $\psi_{U'}$ both send $db$ to $D(b)$ for $b \in B'$, and these generate, so they agree. So the $\psi_U$ glue to $\psi \colon \Omega_{X/S} \to \mathcal{F}$ with $\psi \circ d = D$, and $\psi$ is unique because it is determined on each $U$. Conversely $\psi \mapsto \psi \circ d$ sends morphisms to $S$-derivations. So the map of part 2 is a bijection. Uniqueness up to unique isomorphism is the Yoneda lemma.

(3) If $B$ is generated as an $A$-algebra by $b_1, \dots, b_n$, then $\Omega_{B/A}$ is generated by $db_1, \dots, db_n$ by Corollary P1.12.7. If $B = A[x_1, \dots, x_n]/(g_1, \dots, g_m)$, then $\Omega_{B/A}$ is the cokernel of the Jacobian matrix $B^m \to B^n$ by the same corollary, so it is finitely presented. If $X$ is locally Noetherian, a quasi-coherent sheaf of finite type is coherent by Proposition P3.5.22.

(4) Let $(U, V)$ be a pair for $f$, $V' = \operatorname{Spec} A' \subseteq S'$ an affine open mapping into $V$, and $U' = U \times_V V' = \operatorname{Spec} (B \otimes_A A')$, an affine open of $X'$ (Theorem P3.3.19). By Proposition P1.12.8, $\Omega_{B \otimes_A A' / A'} \cong \Omega_{B/A} \otimes_A A' = \Omega_{B/A} \otimes_B (B \otimes_A A')$, with $d(b \otimes a') \mapsto a'\,db$. The right side is the module of $g^* \Omega_{X/S}$ on $U'$ (Proposition P3.5.32). These isomorphisms send $d(b \otimes 1)$ to $1 \otimes db$, so they agree on overlaps and glue. For the fibre take $S' = \operatorname{Spec} \kappa(s)$.

(5) This is Proposition P1.12.4 on each affine open of $S$, glued by part 4. $\square$

*Proof of Theorem P3.12.4.* Both sequences are sequences of quasi-coherent sheaves (Theorem P3.5.20), so exactness can be checked on the affine opens of a cover (Theorem P3.5.20). Over a pair of affine opens they become the first fundamental sequence $\Omega_{C/A} \otimes_C B \to \Omega_{B/A} \to \Omega_{B/C} \to 0$ for $A \to C \to B$ and the conormal sequence $I/I^2 \to \Omega_{B/A} \otimes_B B/I \to \Omega_{(B/I)/A} \to 0$, which are exact by Theorems P1.12.5 and P1.12.6. Here for part 1 the affine opens are chosen with $U = \operatorname{Spec} B \subseteq f^{-1}(W)$, $W = \operatorname{Spec} C \subseteq g^{-1}(V)$, and the module of $f^* \Omega_{Y/S}$ on $U$ is $\Omega_{C/A} \otimes_C B$ by Proposition P3.5.32. For part 2, the module of $\mathcal{C}_{Z/X}$ on $Z \cap U = \operatorname{Spec} B/I$ is $I \otimes_B B/I = I/I^2$. The maps are the ones of P1 Ch. 12 on each affine open, so they glue. $\square$

### Exercises

1. (A) Let $X = V(y^2 - x^3) \subseteq \mathbb{A}^2_k$ be the cusp. Compute $\Omega_{X/k}$ and its fibre dimension at every point. Show that $\Omega_{X/k}$ has torsion: the element $2x\,dy - 3y\,dx$ is nonzero and killed by a power of the maximal ideal of the origin (Example P1.12.11).
2. (A) Let $L/k$ be a finite separable field extension. Show that $\Omega_{\operatorname{Spec} L/\operatorname{Spec} k} = 0$, and that for every $k$-scheme $X$ the projection $X_L \to X$ satisfies $\Omega_{X_L/X} = 0$.
3. (A) Let $A$ be a ring and $s \colon \operatorname{Spec} A \to \mathbb{A}^n_A$ the zero section, with ideal $I = (x_1, \dots, x_n)$. Show that the conormal sequence of $s$ over $A$ gives an isomorphism $I/I^2 \cong s^* \Omega_{\mathbb{A}^n_A/A}$, and that both are free with bases $x_i$ and $dx_i$.
4. (B) Let $X \to S$ be separated and $\Delta \colon X \to X \times_S X$ the diagonal, a closed immersion with ideal $\mathcal{I}$. Show that $\Omega_{X/S} \cong \Delta^*(\mathcal{I}/\mathcal{I}^2)$, with $dh$ corresponding to the class of $1 \otimes h - h \otimes 1$. Hint: on affine opens, P1 Ch. 12 describes $\Omega_{B/A}$ as $J/J^2$ for the kernel $J$ of $B \otimes_A B \to B$.
5. (B) Let $f \colon X \to Y$ be an open immersion of schemes over $S$. Show that $\Omega_{X/Y} = 0$ and that $f^* \Omega_{Y/S} \to \Omega_{X/S}$ is an isomorphism. Show that the same holds for the morphism $\operatorname{Spec} k[t, t^{-1}] \to \operatorname{Spec} k[u]$, $u \mapsto t^2$, over a field with $\operatorname{char} k \neq 2$, which is not an open immersion.
6. (B) Let $X = \operatorname{Spec} k[t]/(t^2)$ and $Y = \operatorname{Spec} k$. Compute $\Omega_{X/Y}$, and show that in characteristic $2$ it is free of rank one over $k[t]/(t^2)$, while in characteristic not $2$ it is $k\,dt$, which is not free.
7. (C) Let $X = V(F) \subseteq \mathbb{P}^n_k$ be a hypersurface of degree $e$. Show that the conormal sheaf of $X$ is $\mathcal{O}_X(-e)$, and write the conormal sequence of $X$ in $\mathbb{P}^n_k$ on the chart $D_+(x_0)$.

### Lean

Mathlib has the module of Kähler differentials `Ω[B⁄A]`, its universal property through `Derivation`, the base change `KaehlerDifferential.tensorKaehlerEquiv`, the localization `KaehlerDifferential.isLocalizedModule`, the two exact sequences `KaehlerDifferential.exact_mapBaseChange_map` and `KaehlerDifferential.exact_kerCotangentToTensor_mapBaseChange`, and the bases of `KaehlerDifferential.mvPolynomialBasis` and `KaehlerDifferential.polynomialEquiv`, all proved. Mathlib does not glue these modules into a sheaf on a scheme. The statements of mmp-lean do not use the sheaf either: `MinimalModel.TopForm` is the top exterior power of `Ω[k(X)⁄k]` for the function field, and the canonical divisor of Section 12.4 is defined from it. The handbook adds no `MinimalModel` node here.

### Notes and history

Kähler differentials on schemes are EGA IV, Section 16, and Hartshorne, Section II.8. Hartshorne defines $\Omega_{X/S}$ as $\Delta^*(\mathcal{I}/\mathcal{I}^2)$ for the diagonal, which is Exercise 4, and Vakil glues the affine modules, as here. The Stacks Project does both, in its chapter on morphisms of schemes. The literature state is theorem. The sheaf $\Omega_{X/S}$ is the first piece of the cotangent complex $L_{X/S}$ of Illusie, whose next piece measures the failure of the conormal sequence to be exact on the left. For a smooth morphism the cotangent complex is $\Omega_{X/S}$ alone, and Section 12.2 proves the form of this that the handbook needs: for a smooth subvariety of a smooth variety the conormal sequence is exact on the left.
