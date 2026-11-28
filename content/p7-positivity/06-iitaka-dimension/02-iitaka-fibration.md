---
title: The Iitaka fibration and the Kodaira dimension
nodes: []
sources: [Laz04, Iit71, Har77]
reads_with: [Laz04:2.1.C, Har77:II.8]
requires: [P3.7, P3.10, P3.12, P4.4, P4.6, P5.1, P5.11, P7.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Iitaka fibration and the Kodaira dimension

### Statement

Throughout, $X$ is a projective variety over $k$ of dimension $n \geq 1$ and $L$ is a line bundle on $X$, with $N(L)$, $\varphi_m$, $Y_m$ and $K_\infty$ as in Section 6.1. A *fibre space* is a surjective projective morphism $f \colon X' \to Y'$ of varieties with $f_* \mathcal{O}_{X'} = \mathcal{O}_{Y'}$.

**Theorem P7.6.11 (the Iitaka fibration).** Let $\kappa = \kappa(L) \geq 0$.

1. For all large $m, m' \in N(L)$ there is a birational map $\beta \colon Y_m \dashrightarrow Y_{m'}$ with $\beta \circ \varphi_m = \varphi_{m'}$, and the function field of $Y_m$ is identified with $K_\infty$ by $\varphi_m^*$.
2. There are a normal projective variety $X_\infty$ with a birational morphism $\mu \colon X_\infty \to X$, a normal projective variety $Y_\infty$ of dimension $\kappa$ and a surjective morphism $f_\infty \colon X_\infty \to Y_\infty$ with $f_\infty^* k(Y_\infty) = K_\infty$, such that for every large $m \in N(L)$ there is a birational map $\nu_m \colon Y_\infty \dashrightarrow Y_m$ with $\varphi_m \circ \mu = \nu_m \circ f_\infty$.
3. If $k$ has characteristic $0$ and $X$ is normal, then $X_\infty$ can be chosen smooth and $f_\infty$ a fibre space, and for a very general point $y \in Y_\infty$ the fibre $F = f_\infty^{-1}(y)$ is a smooth projective variety with $\kappa(F, \mu^* L|_F) = 0$.

Lean: not in Lean as stated.

The fibre space $f_\infty$ of part 3 is the *Iitaka fibration* of $L$; it is unique up to birational equivalence of fibre spaces.

**Proposition P7.6.12 (pullback by a fibre space).** Let $f \colon X' \to X$ be a surjective morphism of projective varieties with $f_* \mathcal{O}_{X'} = \mathcal{O}_X$. Then pullback is an isomorphism $H^0(X, L^m) \cong H^0(X', f^* L^m)$ for every $m \in \mathbb{Z}$, so $R(X', f^* L) \cong R(X, L)$ and $\kappa(X', f^* L) = \kappa(X, L)$. This applies to every birational morphism $f$ onto a normal $X$.

Lean: not in Lean as stated.

**Definition P7.6.13 (plurigenera and Kodaira dimension).** Let $X$ be a smooth projective variety of dimension $n$, with canonical sheaf $\omega_X = \det \Omega_X$ and canonical divisor $K_X$. The *$m$-th plurigenus* is $P_m(X) = h^0(X, \omega_X^m)$, the *canonical ring* is $R(X, K_X) = \bigoplus_{m \geq 0} H^0(X, \omega_X^m)$, and the *Kodaira dimension* is $\kappa(X) = \kappa(X, \omega_X)$. The variety $X$ is *of general type* if $\kappa(X) = n$, that is, if $K_X$ is big.

By part 5 of Corollary P7.6.6, for curves and surfaces these are the plurigenera and the Kodaira dimension of Definition P5.11.2.

**Theorem P7.6.14 (birational invariance).** Let $X$ and $X'$ be smooth projective varieties that are birational. Then for every $m \geq 0$ a birational map $X \dashrightarrow X'$ induces an isomorphism $H^0(X', \omega_{X'}^m) \cong H^0(X, \omega_X^m)$, and these isomorphisms form an isomorphism of graded rings $R(X', K_{X'}) \cong R(X, K_X)$. In particular $P_m(X) = P_m(X')$ for all $m$ and $\kappa(X) = \kappa(X')$.

Lean: `MinimalModel.kodairaDim` and `MinimalModel.canonicalRing`, in the project library, are the Kodaira dimension and the canonical ring; their birational invariance is not stated there.

### Proof in words

All the maps $\varphi_m$ for large $m$ in the semigroup have the same function field $K_\infty$ on the image, so their images are birational to each other and to one normal model $Y_\infty$. Resolving the indeterminacy of one of them by the normalized graph gives a morphism $X_\infty \to Y_\infty$ that represents all of them at once, and this is the Iitaka fibration up to birational modification. The two deeper properties, connected fibres and Iitaka dimension $0$ on the general fibre, express that $K_\infty$ is algebraically closed in $k(X)$ and that the sections of the multiples of $L$ restricted to a general fibre are constant; they are stated here with a reference.

For the canonical bundle the Iitaka dimension is a birational invariant. A birational map between smooth projective varieties is defined outside a closed set of codimension at least $2$, so it pulls back pluricanonical forms on that open set, and a section of a line bundle on a normal variety extends over a set of codimension $2$. Applying this to the map and its inverse gives an isomorphism of canonical rings. This is the reason the canonical ring, and not the section ring of an arbitrary divisor, is the object of the minimal model program.

### Examples

**Example P7.6.15 (curves).** Let $C$ be a smooth projective curve of genus $g$. By part 1 of Proposition P5.11.5, $\kappa(C) = -\infty$ for $g = 0$, $\kappa(C) = 0$ for $g = 1$ and $\kappa(C) = 1$ for $g \geq 2$, with $P_m(C) = (2m - 1)(g - 1)$ for $m \geq 2$ in the last case. For $g \geq 2$ and $m \geq 3$, $\deg(mK) = m(2g - 2) \geq 2g + 1$, so $mK$ is very ample by part 2 of Corollary P5.1.20, $\varphi_m$ is an embedding, and the Iitaka fibration is the identity of $C$. For $g = 1$, $Y_m$ is a point and the Iitaka fibration is $C \to \operatorname{Spec} k$.

**Example P7.6.16 (hypersurfaces).** Let $Y \subseteq \mathbb{P}^{n+1}$, $n \geq 1$, be a smooth integral hypersurface of degree $e$. By Corollary P3.12.31, $\omega_Y \cong \mathcal{O}_Y(e - n - 2)$. If $e \leq n + 1$, every $\omega_Y^m = \mathcal{O}_Y(m(e - n - 2))$, $m \geq 1$, has negative degree with respect to the ample class $h = [\mathcal{O}_Y(1)]$, namely $m(e - n - 2) \, (h^n) < 0$, so it has no nonzero section by part 1 of Proposition P7.5.13, and $\kappa(Y) = -\infty$. If $e = n + 2$, then $\omega_Y \cong \mathcal{O}_Y$, every $P_m(Y) = 1$ and $\kappa(Y) = 0$. If $e \geq n + 3$, $\omega_Y$ is ample, hence big by part 1 of Corollary P7.5.4, and $\kappa(Y) = n$ by part 4 of Corollary P7.6.6: $Y$ is of general type. For $n = 1$ this is the trichotomy of plane curves of degree at most $2$, $3$ and at least $4$; for $n = 2$, quadrics and cubics, quartic K3 surfaces, and surfaces of general type.

**Example P7.6.17 (products).** Let $X$ and $Y$ be smooth projective varieties with projections $p$ and $q$. Since $\Omega_{X \times Y} \cong p^* \Omega_X \oplus q^* \Omega_Y$ (Hartshorne, Exercise II.8.3, in Har77), $\omega_{X \times Y} \cong p^* \omega_X \otimes q^* \omega_Y$, and Lemma P5.11.4 gives $P_m(X \times Y) = P_m(X) \, P_m(Y)$ for all $m \geq 1$. If one factor has $\kappa = -\infty$, so does the product. Otherwise the upper bounds of Theorem P7.6.5 multiply, and the lower bounds hold for all large $m$ divisible by both exponents, so $\kappa(X \times Y) = \kappa(X) + \kappa(Y)$ by the last sentence of Theorem P7.6.5. For example $C_1 \times C_2 \times C_3$ with all $g(C_i) \geq 2$ is of general type, and $E \times \mathbb{P}^1$ has $\kappa = -\infty$ for every elliptic curve $E$.

**Example P7.6.18 (surfaces).** By Theorem P5.11.26 and part 5 of Corollary P7.6.6, a smooth projective surface $S$ has $\kappa(S) = -\infty$ exactly when it is birationally ruled. If $\kappa(S) = 0$, its minimal model $S_0$ has $12 K_{S_0} \sim 0$; for an Enriques surface $K_{S_0} \not\sim 0$ and $2 K_{S_0} \sim 0$ (Definition P5.11.23), so $N(\omega_{S_0}) = 2 \mathbb{Z}_{> 0}$, $e(\omega_{S_0}) = 2$, $P_1 = 0$ and $P_2 = 1$, and $\kappa = 0$ is reached only on even multiples. If $\kappa(S) = 1$, part 3 of Theorem P5.11.26 gives an elliptic or quasi-elliptic fibration $f \colon S_0 \to B$ with $n K_{S_0} \sim f^* D$, $\deg D > 0$, and $\varphi_{|n K_{S_0}|}$ is $f$ followed by an embedding of $B$ for $n$ large and divisible: $f$ is the Iitaka fibration, and its fibres, curves of arithmetic genus $1$ with $K_{S_0}$ restricting to a torsion bundle, have Iitaka dimension $0$. If $\kappa(S) = 2$, $S$ is of general type. By Theorem P7.6.14 these values are the same for $S$ and for every surface birational to it. Example P5.11.27 lists the invariants of each class.

**Example P7.6.19 (an Iitaka fibration with elliptic fibres).** Let $X = C_1 \times E$ with $g(C_1) \geq 2$ and $E$ an elliptic curve, with projection $p \colon X \to C_1$. Since $\omega_E \cong \mathcal{O}_E$, $\omega_X \cong p^* \omega_{C_1}$, and by Lemma P5.11.4 pullback is an isomorphism $H^0(C_1, \omega_{C_1}^m) \cong H^0(X, \omega_X^m)$. So $\varphi_m = \varphi_{|mK_{C_1}|} \circ p$, which for $m \geq 3$ is $p$ followed by an embedding of $C_1$ (Example P7.6.15). The Iitaka fibration is $p$, its fibres are copies of $E$, and $\omega_X|_E \cong \mathcal{O}_E$ has Iitaka dimension $0$, as part 3 of Theorem P7.6.11 predicts. Here $\kappa(X) = 1 = \kappa(C_1) + \kappa(E)$.

### Proof

*Theorem P7.6.11.* Part 1. By part 3 of Proposition P7.6.4, $k(\varphi_m) = K_\infty$ for all large $m \in N(L)$, and by part 1 the isomorphism $\varphi_m^* \colon k(Y_m) \to k(\varphi_m)$ identifies $k(Y_m)$ with $K_\infty$. For two such $m, m'$, the composite isomorphism $k(Y_{m'}) \cong K_\infty \cong k(Y_m)$ is induced by a unique birational map $\beta \colon Y_m \dashrightarrow Y_{m'}$ (Hartshorne, Corollary I.4.5, in Har77), and $\beta \circ \varphi_m$ and $\varphi_{m'}$ are dominant rational maps $X \dashrightarrow Y_{m'}$ inducing the same map of function fields $k(Y_{m'}) \to k(X)$, so they agree.

Part 2. Take $m_1$, $X_\infty$, $\mu$, $Y_\infty$ and $f = f_\infty$ as in the proof of the upper bound in Theorem P7.6.5. There $X_\infty$ and $Y_\infty$ are normal projective varieties, $\mu$ is birational, $f_\infty$ is surjective, $f_\infty^* k(Y_\infty) = K_\infty$, and $\dim Y_\infty = \dim Y_{m_1} = \kappa$ by part 4 of Proposition P7.6.4. By construction $\varphi_{m_1} \circ \mu = \nu_{m_1} \circ f_\infty$, where $\nu_{m_1}$ is the normalization morphism $Y_\infty \to Y_{m_1}$. For large $m \in N(L)$ put $\nu_m = \beta \circ \nu_{m_1}$ with $\beta \colon Y_{m_1} \dashrightarrow Y_m$ from part 1, which applies after enlarging $m_1$ if necessary; then $\varphi_m \circ \mu = \beta \circ \varphi_{m_1} \circ \mu = \nu_m \circ f_\infty$ as rational maps.

Part 3. This is Lazarsfeld, Theorem 2.1.33 (Laz04), going back to Iitaka (Iit71), and is not proved here. The proof shows that $K_\infty$ is algebraically closed in $k(X)$, which in characteristic $0$ gives a model of $f_\infty$ with connected fibres after Stein factorization (Theorem P4.6.15) and a resolution of singularities of $X_\infty$, and then that a section of a multiple of $\mu^* L$ on a very general fibre extends to a section on a neighbourhood whose ratio with a fixed section lies in $K_\infty$, so is constant on the fibre.

*Proposition P7.6.12.* By Proposition P4.4.10 with $q = 0$ and $\mathcal{E} = L^m$, $f_* (f^* L^m) \cong f_* \mathcal{O}_{X'} \otimes L^m = L^m$, and the isomorphism is given on sections by pullback. Taking global sections, $H^0(X', f^* L^m) = H^0(X, f_* f^* L^m) \cong H^0(X, L^m)$. These isomorphisms are compatible with products, so they form an isomorphism of graded rings, and the Iitaka dimensions agree because $\kappa$ depends only on the numbers $h^0$, by the last sentence of Theorem P7.6.5, or directly because the maps $\varphi_m$ correspond. If $f$ is birational and $X$ is normal, $f_* \mathcal{O}_{X'} = \mathcal{O}_X$ by Theorem P4.6.8.

*Theorem P7.6.14.* Let $\varphi \colon X \dashrightarrow X'$ be birational. Since $X'$ is projective, it is a closed subscheme of some $\mathbb{P}^N$, and by part 2 of Theorem P3.10.29 $\varphi$ is defined on an open set $U \subseteq X$ whose complement has codimension at least $2$. The morphism $\varphi|_U \colon U \to X'$ gives a map of sheaves $\varphi|_U^* \Omega_{X'} \to \Omega_U$ (Hartshorne, Proposition II.8.12, in Har77), of locally free sheaves of the same rank $n$, and taking determinants and $m$-th tensor powers a map $\varphi|_U^* \omega_{X'}^m \to \omega_U^m$. So a section $s \in H^0(X', \omega_{X'}^m)$ pulls back to a section $\varphi^* s$ of $\omega_X^m$ on $U$. On an open set $V \subseteq X$ where $\omega_X$ is trivial, a section of $\omega_X^m$ over $V \cap U$ is a regular function on $V \cap U$, and $V \setminus U$ has codimension at least $2$ in the normal variety $V$, so by Theorem P3.7.33 it extends uniquely to $V$. These extensions glue, and $\varphi^* s$ extends uniquely to a section of $\omega_X^m$ on $X$. The map $s \mapsto \varphi^* s$ is linear and multiplicative. It is injective: there are dense open sets $V_0 \subseteq U$ and $V'_0 \subseteq X'$ with $\varphi|_{V_0} \colon V_0 \to V'_0$ an isomorphism, under which $\varphi^*$ is an isomorphism of sheaves, so $\varphi^* s = 0$ forces $s|_{V'_0} = 0$, and then $s = 0$ because a section of a line bundle on an integral scheme that vanishes on a dense open set is zero. Applying the same construction to $\varphi^{-1}$ gives an injection in the other direction, so $P_m(X) = P_m(X')$ and $\varphi^*$ is an isomorphism in each degree. The graded ring isomorphism and the equality of Kodaira dimensions follow.

### Exercises

1. (A) Let $X = \mathbb{P}^1 \times \mathbb{P}^1$ and $L = \mathcal{O}(1, 0)$. Show that the Iitaka fibration of $L$ is the first projection, and that its fibres have $\kappa(F, L|_F) = 0$.
2. (A) Show that every smooth projective rational variety has $P_m = 0$ for all $m \geq 1$, using Theorem P7.6.14 and $\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n - 1)$.
3. (A) Compute the Kodaira dimension of a smooth complete intersection of two quadrics in $\mathbb{P}^4$, and of a smooth complete intersection of a quadric and a cubic in $\mathbb{P}^4$, using the general form of Corollary P3.12.31.
4. (B) Let $X = \operatorname{Bl}_p \mathbb{P}^2$ and $L = \mathcal{O}(H - E)$. Show that $\varphi_1$ is the morphism to $\mathbb{P}^1$ given by projection from $p$, that it is a fibre space, and that it is the Iitaka fibration of $L$. Compute $\kappa(F, L|_F)$ for a fibre $F$.
5. (B) Let $X$ be a smooth projective surface and $\pi \colon \tilde X \to X$ the blow-up of a point. Using part 3 of Theorem P5.6.3 and part 3 of Corollary P5.6.5, compute $H^0(\tilde X, \omega_{\tilde X}^m)$ directly and check Theorem P7.6.14 in this case.
6. (C) Let $L$ be a line bundle with $\kappa(L) = 0$. Show that for each $m \in N(L)$ the linear system $|L^m|$ has exactly one member $D_m$, that $D_{m + m'} = D_m + D_{m'}$, and that the Iitaka fibration is the map to a point. Compute $D_m$ for $L = \mathcal{O}(E)$ on $\operatorname{Bl}_p \mathbb{P}^2$ and for $L = \omega_X^{-1}$ on the surface $X_9$ of Example P7.6.9.

### Lean

The project library defines `MinimalModel.kodairaDim` as `MinimalModel.iitakaDim` of the canonical divisor, and `MinimalModel.canonicalRing` as the $k$-subalgebra of $k(X)[t]$ generated by the elements $\varphi t^m$ with $\varphi$ a section of $mK_X$. The Iitaka fibration, the pullback statement of Proposition P7.6.12 and the birational invariance of Theorem P7.6.14 are not stated there. Mathlib has differentials of rings, `KaehlerDifferential`, but no canonical sheaf of a variety. The handbook adds no `MinimalModel` node here.

### Notes and history

Iitaka constructed the fibration in 1971 (Iit71), and Lazarsfeld, Section 2.1.C (Laz04), gives the modern statement used in part 3 of Theorem P7.6.11, for normal complex projective varieties. The literature state is theorem in characteristic $0$; parts 1 and 2 hold over any algebraically closed field, while in positive characteristic the general fibre of $f_\infty$ need not be reduced, and the form of part 3 needs care. The birational invariance of plurigenera is classical, going back to the Italian school for surfaces. Iitaka's conjecture $C_{n,m}$, that $\kappa(X) \geq \kappa(F) + \kappa(Y)$ for a fibre space $X \to Y$ with general fibre $F$, is one of the central open problems connected with the minimal model program; it is known in many cases, for example when the base is a curve or is of general type.
