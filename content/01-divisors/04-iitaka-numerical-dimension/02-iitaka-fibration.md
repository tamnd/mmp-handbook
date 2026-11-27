---
title: The Iitaka fibration and the Kodaira dimension
nodes: []
sources: [Laz04, Har77, KM98, Bea96]
reads_with: [Laz04:ch2, Bea96:ch8]
requires: [P3.6, P3.7, P3.10, P3.12, P4.2, P4.4, P4.6, P5.1, P5.4, P5.6, P5.10, P5.11, P5.12, 1.1]
level: background
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Iitaka fibration and the Kodaira dimension

### Statement

Keep the notation of Section 1: $X$ is a projective variety of dimension $n$, $D$ a Cartier divisor, $N(D)$ its semigroup, $\varphi_m \colon X \dashrightarrow Y_m$ the maps of $|mD|$ and $K_\infty \subseteq k(X)$ the stable field of Proposition 1.4.4. A *contraction* is a projective surjective morphism $f \colon V \to W$ of varieties with $f_* \mathcal{O}_V = \mathcal{O}_W$; its fibres are connected (Theorem P4.6.15). A property holds for a *very general* point of a variety if it holds outside a countable union of proper closed subsets.

**Theorem 1.4.12 (the Iitaka fibration).** Let $X$ be normal and $\kappa = \kappa(D) \ge 0$. There are normal projective varieties $X_\infty$ and $Y_\infty$, a birational morphism $\mu \colon X_\infty \to X$ and a contraction $f \colon X_\infty \to Y_\infty$ with $\dim Y_\infty = \kappa$, such that:

1. $f^* k(Y_\infty) = K_\infty$ inside $k(X_\infty) = k(X)$, and $K_\infty$ is algebraically closed in $k(X)$;
2. for every large $m \in N(D)$ there is a birational map $\nu_m \colon Y_\infty \dashrightarrow Y_m$ with $\varphi_m \circ \mu = \nu_m \circ f$ as rational maps;
3. for a very general point $y \in Y_\infty$ the fibre $F = f^{-1}(y)$ is irreducible and $\kappa(F, \mu^* D|_F) = 0$.

The fibration is unique up to birational equivalence: if $\mu' \colon X'_\infty \to X$ and $f' \colon X'_\infty \to Y'_\infty$ also have properties 1 and 2, there is a birational map $\beta \colon Y_\infty \dashrightarrow Y'_\infty$ with $\beta \circ f = f' \circ \mu'^{-1} \circ \mu$.

Lean: not yet in Lean.

Parts 1 and 2 are proved below. Part 3 is Laz04, Theorem 2.1.33, and is cited.

**Definition 1.4.13 (Iitaka fibration, plurigenera, Kodaira dimension).** The contraction $f$ of Theorem 1.4.12, or any fibration birational to it, is the *Iitaka fibration* of $D$. For a smooth projective variety $X$ with canonical divisor $K_X$, the *$m$-th plurigenus* is $P_m(X) = h^0(X, mK_X)$, the *geometric genus* is $p_g(X) = P_1(X)$, and the *Kodaira dimension* is $\kappa(X) = \kappa(X, K_X)$. For an arbitrary variety $X$, $\kappa(X)$ is the Kodaira dimension of a smooth projective variety birational to $X$, which exists by Hironaka's resolution of singularities. A smooth projective variety is *of general type* if $\kappa(X) = n$.

Lean: `MinimalModel.kodairaDim`, in the project library.

For a smooth projective $X$ the Iitaka fibration of $K_X$ is the *Iitaka fibration of $X$*. Theorem 1.4.15 shows that the last definition is independent of the choice of model.

**Proposition 1.4.14 (pullback by a contraction).** Let $f \colon X \to Y$ be a contraction of projective varieties and $D$ a Cartier divisor on $Y$. Then $h^0(X, m f^*D) = h^0(Y, mD)$ for every $m$, and $\kappa(X, f^*D) = \kappa(Y, D)$.

Lean: not yet in Lean.

**Theorem 1.4.15 (birational invariance of the plurigenera).** Let $X$ and $X'$ be smooth projective varieties that are birational. Then $P_m(X) = P_m(X')$ for every $m \ge 1$, and $\kappa(X) = \kappa(X')$.

Lean: not yet in Lean.

**Proposition 1.4.16 (products).** Let $X$ and $X'$ be projective varieties, $D$ and $D'$ Cartier divisors on them, and $D \boxtimes D' = p^*D + p'^*D'$ on $X \times X'$. Then $\kappa(D \boxtimes D') = \kappa(D) + \kappa(D')$, with $-\infty + j = -\infty$. In particular $\kappa(X \times X') = \kappa(X) + \kappa(X')$ for smooth projective $X$ and $X'$.

Lean: not yet in Lean.

### Proof in words

For large $m \in N(D)$ all the maps $\varphi_m$ have the same function field $K_\infty$, so by the equivalence between varieties and function fields they are one rational map up to birational maps of the targets. Resolving the indeterminacy of one of them and normalizing gives a morphism $f$. It is a contraction because its function field is algebraically closed in $k(X)$, and the field is algebraically closed because a finite extension $L$ of $K_\infty$ inside $k(X)$ is the function field of a finite cover of $Y_\infty$ through which $f$ factors, and the sections of a very ample bundle on that cover pull back to sections of a multiple of $D$; their ratios generate $L$ and lie in $K_\infty$. For a contraction $f$, the projection formula says that $f^*$ is a bijection on sections, so pulling back does not change Iitaka dimensions. For the plurigenera, a birational map of smooth varieties is a morphism outside codimension 2, pluricanonical forms pull back along it, and Hartogs extends them across the missing set; the pullback is injective because the map is an isomorphism on a dense open set, and symmetry gives equality.

### Examples

**Example 1.4.17 (why $m$ must be large).** Let $E$ be an elliptic curve and $D = p$ a point. Then $h^0(mp) = m$ for $m \ge 1$ (Corollary P5.1.11), $N(D) = \mathbb{Z}_{>0}$ and $\kappa(D) = 1$. The map $\varphi_2 \colon E \to \mathbb{P}^1$ is a morphism of degree 2 (Proposition P5.1.13, part 3), so its fibres are not connected and $k(\varphi_2) \subseteq k(E)$ is an extension of degree 2, not algebraically closed. For $m \ge 3$, $\varphi_m$ is a closed embedding, $k(\varphi_m) = k(E) = K_\infty$, and the Iitaka fibration is the identity $E \to E$. So part 2 of Theorem 1.4.12 fails for small $m \in N(D)$.

**Example 1.4.18 (a fibre of an elliptic fibration).** Let $S$ be a smooth projective surface and $f \colon S \to C$ a contraction onto a smooth curve of genus $g$ whose general fibre is an elliptic curve, and let $F = f^*q$ be the fibre over a point $q$. By Proposition 1.4.14, $h^0(mF) = h^0(C, mq)$, which is $m + 1 - g$ for $m \ge 2g - 1$ by Corollary P5.1.11. So $\kappa(F) = 1$, and for $m \ge 2g + 1$ the map $\varphi_m$ is $f$ followed by the embedding of $C$ by $|mq|$, so the Iitaka fibration of $F$ is $f$. A concrete case: let $X$ be the blow-up of $\mathbb{P}^2$ in the nine base points of a pencil of plane cubics spanned by two smooth cubics meeting transversally. The pencil becomes a morphism $X \to \mathbb{P}^1$ whose fibres are the strict transforms of the cubics, of class $3\ell - \sum_{i=1}^9 E_i = -K_X$ (Theorem P5.6.3). So $\kappa(X, -K_X) = 1$ and $h^0(-mK_X) = m + 1$. Compare Example P5.10.26, where nine points on one cubic whose sum has infinite order give $h^0(-mK_X) = 1$ and $\kappa(-K_X) = 0$, with the same numbers $(-K_X)^2 = 0$ and $-K_X$ nef.

**Example 1.4.19 (the surface $E \times E$).** Let $E$ be an elliptic curve with origin $O$, $S = E \times E$, $f_1 = \{O\} \times E = p_1^*O$, $f_2 = E \times \{O\} = p_2^*O$ and $\Delta$ the diagonal. By Lemma P5.11.4, $h^0(mf_1) = h^0(E, mO) \, h^0(E, \mathcal{O}_E) = m$, so $\kappa(f_1) = 1$, and for $m \ge 3$ the map $\varphi_m$ is $p_1$ followed by an embedding of $E$, so the Iitaka fibration of $f_1$ is $p_1$; likewise $\kappa(f_2) = 1$. The map $\psi(x, y) = (x - y, y)$ is an automorphism of $S$ by Theorem P5.4.4, with inverse $(u, y) \mapsto (u + y, y)$, and $\psi(x, x) = (O, x)$, so $\psi^{-1}(f_1) = \Delta$ and $\Delta = \psi^* f_1$. Pullback by an automorphism preserves all $h^0$, so $\kappa(\Delta) = 1$, with Iitaka fibration $p_1 \circ \psi$, the difference map $(x, y) \mapsto x - y$. By Example P5.12.9 the three classes have square 0 and pairwise products 1. The sum $D = f_1 + f_2 + \Delta$ has $D^2 = 6 > 0$ and $D \cdot H > 0$ for every ample $H$, since $D$ is a nonzero sum of curves, so $D$ is big by Proposition P5.11.3, part 4. The canonical divisor is $K_S = p_1^*K_E + p_2^*K_E \sim 0$, so $P_m(S) = 1$ for all $m$ and $\kappa(S) = 0$, in agreement with Proposition P5.11.5.

**Example 1.4.20 (hypersurfaces and products of curves).** Let $X \subseteq \mathbb{P}^{n+1}$ be a smooth hypersurface of degree $d$, $n \ge 1$, and $H$ a hyperplane section. By Corollary P3.12.31, $K_X \sim (d - n - 2)H$. If $d > n + 2$, then $K_X$ is ample and $\kappa(X) = n$. If $d = n + 2$, then $K_X \sim 0$, $P_m(X) = 1$ and $\kappa(X) = 0$. If $d < n + 2$, then $h^0(-jH) = 0$ for $j \ge 1$, since a nonzero section $s$ of $\mathcal{O}_X(-j)$ times a section $t$ of $\mathcal{O}_X(j)$ not vanishing at a given point is a nonzero constant, which forces $\mathcal{O}_X(j)$ to be trivial, while it is ample on a variety of positive dimension. So $\kappa(X) = -\infty$. For a quintic surface, $K_X = H$, and the sequence $0 \to \mathcal{O}_{\mathbb{P}^3}(m - 5) \to \mathcal{O}_{\mathbb{P}^3}(m) \to \mathcal{O}_X(m) \to 0$ with $H^1(\mathcal{O}_{\mathbb{P}^3}(m - 5)) = 0$ (Theorem P4.2.1) gives $P_m(X) = \binom{m + 3}{3} - \binom{m - 2}{3}$ for $m \ge 1$, where $\binom{j}{3} = 0$ for $j < 3$. So $P_1 = 4$, $P_2 = 10$, $P_5 = 55$, and $P_m$ grows like $\frac{5}{2} m^2$.

Let $X = C_1 \times \dots \times C_r$ be a product of smooth projective curves of genera $g_i$. Then $K_X = \sum_i p_i^* K_{C_i}$ (Har77, Exercise II.8.3), so by Proposition 1.4.16 and Proposition P5.11.5, part 1, $\kappa(X) = -\infty$ if some $g_i = 0$, and otherwise $\kappa(X)$ is the number of $i$ with $g_i \ge 2$. When all $g_i \ge 1$, the Iitaka fibration of $X$ is the projection to the product of the factors of genus at least 2, and its fibres are the products of the elliptic factors, with $\kappa = 0$, as part 3 of Theorem 1.4.12 predicts. Example P5.11.10 is the case $E \times C$.

**Example 1.4.21 (the Kodaira dimension needs a smooth model).** Let $C \subseteq \mathbb{P}^2$ be a smooth plane quartic, of genus 3, given by $F(x, y, z) = 0$, and let $X = V_+(F) \subseteq \mathbb{P}^3$ be the cone over $C$, with vertex $v = [0 : 0 : 0 : 1]$. It is a normal hypersurface of degree 4, singular only at $v$, and its dualizing sheaf is $\omega_X \cong \mathcal{O}_X(4 - 4) = \mathcal{O}_X$, since $X$ is a hypersurface, hence a local complete intersection, and $\omega_X \cong \omega_{\mathbb{P}^3} \otimes \mathcal{O}_X(X)$ (Har77, Theorem III.7.11), the same formula as in Corollary P3.12.31. So the naive count $h^0(\omega_X^{\otimes m}) = 1$ suggests $\kappa = 0$. But $X$ is birational to $C \times \mathbb{P}^1$: on the open set $w \ne 0$ the cone is the affine cone $\{F = 0\} \subseteq \mathbb{A}^3$, and $(c, t) \mapsto t \cdot \hat c$, for a lift $\hat c$ of $c \in C$ in the chart $z = 1$, is a birational map from $C \times \mathbb{A}^1$. By Proposition 1.4.16 and Definition 1.4.13, $\kappa(X) = \kappa(C) + \kappa(\mathbb{P}^1) = -\infty$. So the Kodaira dimension of a singular variety is not $\kappa(X, K_X)$ in general. The vertex here is a singularity that is not canonical, and for varieties with canonical singularities the two numbers do agree; this is one reason why the program allows exactly those singularities on its minimal models.

### Proof

*Proof of Theorem 1.4.12.* Let $m_1$, $X_\infty$, $\mu$, $f_0 \colon X_\infty \to Y_{m_1}$, $Y_\infty$ and $f \colon X_\infty \to Y_\infty$ be as in the proof of the upper bound in Theorem 1.4.6. Then $X_\infty$ and $Y_\infty$ are normal projective varieties, $\mu$ is birational, $f$ is surjective and projective, $\dim Y_\infty = \dim Y_{m_1} = \kappa$ by Proposition 1.4.4, and $f^* k(Y_\infty) = f_0^* k(Y_{m_1}) = k(\varphi_{m_1}) = K_\infty$, since normalization does not change the function field.

*An injection of line bundles.* Let $s_0, \dots, s_r$ be the basis of $H^0(m_1D)$ that defines $\varphi_{m_1}$, write $\mathcal{L} = \mu^* \mathcal{O}_X(m_1 D)$ and $\mathcal{M} = f_0^* \mathcal{O}_{Y_{m_1}}(1)$, and let $W_j \subseteq X_\infty$ be the open set where $f_0^* y_j \ne 0$. The $W_j$ cover $X_\infty$, and $\mathcal{M}|_{W_j}$ is free with basis $f_0^* y_j$. The rational function $f_0^*(y_i/y_j)$ is regular on $W_j$ and equals $s_i/s_j$, since both are the pullback of $y_i/y_j$ on the dense open set where $\varphi_{m_1}$ is defined. So $\mu^* s_i$ and $f_0^*(y_i/y_j) \, \mu^* s_j$ are sections of $\mathcal{L}$ on $W_j$ that agree on a dense open set, hence agree. Define $\iota_j \colon \mathcal{M}|_{W_j} \to \mathcal{L}|_{W_j}$ by $f_0^* y_j \mapsto \mu^* s_j$. Then $\iota_j(f_0^* y_i) = \mu^* s_i$ on $W_j$ for every $i$, so the $\iota_j$ glue to $\iota \colon \mathcal{M} \to \mathcal{L}$ with $\iota(f_0^* y_i) = \mu^* s_i$. It is a nonzero map of invertible sheaves on an integral scheme, so it is injective, and so is $\iota^{\otimes r'} \colon \mathcal{M}^{r'} \to \mathcal{L}^{r'}$ for each $r' \ge 1$.

*Algebraic closedness.* Let $L$ be the algebraic closure of $K_\infty$ in $k(X)$. As in the proof of Proposition 1.4.4, part 3, $L$ is finite over $K_\infty$. Let $\rho \colon Y'' \to Y_\infty$ be the normalization of $Y_\infty$ in $L$ (Har77, Exercise II.3.8). It is a finite morphism, and $Y''$ is a normal projective variety with $k(Y'') = L$. Over an affine open $V \subseteq Y_\infty$, an element of $L$ integral over $\mathcal{O}(V)$ is a rational function on $f^{-1}(V)$ that is integral over the local rings of the normal variety $X_\infty$, so it is regular there. Hence $f$ factors as $f = \rho \circ g$ with $g \colon X_\infty \to Y''$. The sheaf $\mathcal{O}_{Y_{m_1}}(1)$ is ample, so its pullback $\mathcal{M}_\infty$ to $Y_\infty$ and $\mathcal{M}'' = \rho^* \mathcal{M}_\infty$ are ample, by Corollary P4.2.11, part 2, applied to the finite morphisms $Y_\infty \to Y_{m_1}$ and $\rho$. Choose $r' \ge 1$ with $\mathcal{M}''^{r'}$ very ample (Theorem P3.6.25). Then $k(Y'') = L$ is generated by the ratios $\sigma/\tau$ of sections of $\mathcal{M}''^{r'}$, the coordinate ratios of the embedding. Now $g^* \mathcal{M}'' = f^* \mathcal{M}_\infty = \mathcal{M}$, so $g^*\sigma$ and $g^*\tau$ are sections of $\mathcal{M}^{r'}$, and $\iota^{\otimes r'}$ sends them to sections of $\mathcal{L}^{r'} = \mu^* \mathcal{O}_X(r' m_1 D)$ with the same ratio, because an injective map of invertible sheaves is locally multiplication by one rational function. Since $X$ is normal and $\mu$ is projective and birational, $\mu_* \mathcal{O}_{X_\infty} = \mathcal{O}_X$ by Theorem P4.6.8, and the projection formula P4.4.10 gives $H^0(X_\infty, \mathcal{L}^{r'}) = H^0(X, \mathcal{O}_X(r' m_1 D))$. So $\sigma/\tau$ is a ratio of two sections of $r' m_1 D$, with $r' m_1 \in N(D)$, and lies in $K_\infty$. Hence $L = K_\infty$, and $K_\infty$ is algebraically closed in $k(X)$. By Corollary P4.6.16, applied to the projective surjective morphism $f$ onto the normal variety $Y_\infty$, $f$ is a contraction. This proves part 1.

*Part 2.* Let $m \in N(D)$ be large enough that $k(\varphi_m) = K_\infty$, by Proposition 1.4.4, part 3. The dominant rational maps $\varphi_m \circ \mu \colon X_\infty \dashrightarrow Y_m$ and $f \colon X_\infty \to Y_\infty$ induce field inclusions $k(Y_m) \to k(X)$ and $k(Y_\infty) \to k(X)$ with the same image $K_\infty$. So there is an isomorphism $\alpha \colon k(Y_m) \to k(Y_\infty)$ with $f^* \circ \alpha = (\varphi_m \circ \mu)^*$. By the equivalence between varieties with dominant rational maps and finitely generated fields (Har77, Corollary I.4.5), $\alpha = \nu_m^*$ for a birational map $\nu_m \colon Y_\infty \dashrightarrow Y_m$, and $\nu_m \circ f$ and $\varphi_m \circ \mu$ induce the same map of function fields, so they are equal.

*Uniqueness.* If $\mu'$ and $f'$ also have property 1, then $f'^* k(Y'_\infty) = K_\infty$ as well, inside $k(X'_\infty) = k(X)$. The isomorphism $k(Y'_\infty) \to k(Y_\infty)$ through $K_\infty$ is $\beta^*$ for a birational map $\beta$ by the same corollary of Har77, and $\beta \circ f$ and $f' \circ \mu'^{-1} \circ \mu$ induce the same map of function fields, so they are equal.

*Part 3* is Laz04, Theorem 2.1.33, which is stated for a line bundle on a normal projective variety with $\kappa > 0$ and constructs the same fibration $\varphi_\infty \colon X_\infty \to Y_\infty$ as the limit of the maps $\varphi_m$; for $\kappa = 0$ the base is a point and the statement is the hypothesis. $\square$

*Proof of Proposition 1.4.14.* By the projection formula P4.4.10 with $q = 0$, $f_*(f^* \mathcal{O}_Y(mD)) = \mathcal{O}_Y(mD) \otimes f_* \mathcal{O}_X = \mathcal{O}_Y(mD)$, so $H^0(X, mf^*D) = H^0(Y, mD)$. So the two divisors have the same function $m \mapsto h^0$, and the same Iitaka dimension by the last sentence of Theorem 1.4.6, or by $N = \emptyset$ in both cases. $\square$

*Proof of Theorem 1.4.15.* Let $\varphi \colon X \dashrightarrow X'$ be birational and $U = \operatorname{dom}(\varphi)$. Since $X$ is normal and $X'$ projective, $X \setminus U$ has codimension at least 2, by Theorem P3.10.29, part 2. The morphism $\varphi|_U \colon U \to X'$ gives a map $\varphi^* \Omega_{X'} \to \Omega_U$, hence, on top exterior powers and their tensor powers, a map $\varphi^* \omega_{X'}^{\otimes m} \to \omega_U^{\otimes m}$ and a linear map

$$\varphi^* \colon H^0(X', \omega_{X'}^{\otimes m}) \to H^0(U, \omega_X^{\otimes m}).$$

The restriction $H^0(X, \omega_X^{\otimes m}) \to H^0(U, \omega_X^{\otimes m})$ is an isomorphism: on an open set $V$ where $\omega_X$ is trivial, sections are functions, and Theorem P3.7.33 extends functions on $V \cap U$ to $V$, since $V \setminus U$ has codimension at least 2 in $V$; the extensions glue by uniqueness. The map $\varphi$ restricts to an isomorphism between dense open sets $V_0 \subseteq U$ and $V_0' \subseteq X'$, where $\varphi^*$ is the isomorphism of sheaves given by the isomorphism of varieties. If $\varphi^* \omega = 0$, then $\omega$ vanishes on $V_0'$, so $\omega = 0$. So $P_m(X') \le P_m(X)$. The inverse birational map gives $P_m(X) \le P_m(X')$. Equal plurigenera for all $m$ give equal Kodaira dimensions by Theorem 1.4.6. $\square$

*Proof of Proposition 1.4.16.* By Lemma P5.11.4, $h^0(m(D \boxtimes D')) = h^0(mD) \, h^0(mD')$. If $N(D)$ or $N(D')$ is empty, then one factor vanishes for every $m$, and $\kappa(D \boxtimes D') = -\infty$. Otherwise $N(D) \cap N(D')$ contains every large multiple of the least common multiple of $e(D)$ and $e(D')$, by Lemma 1.4.3. For those $m$, Theorem 1.4.6 gives $h^0(m(D \boxtimes D')) \ge a a' m^{\kappa + \kappa'}$, and for all $m$ it gives $h^0(m(D \boxtimes D')) \le b b' m^{\kappa + \kappa'}$, with $\kappa = \kappa(D)$ and $\kappa' = \kappa(D')$. By the last sentence of Theorem 1.4.6, $\kappa(D \boxtimes D') = \kappa + \kappa'$. For smooth projective $X$ and $X'$, $K_{X \times X'} = K_X \boxtimes K_{X'}$ (Har77, Exercise II.8.3). $\square$

### Exercises

1. (A) Show that $\kappa(\mathbb{P}^n) = -\infty$, and that $\kappa(A) = 0$ for an abelian variety $A$, using $K_A \sim 0$.
2. (A) Let $C$ be a smooth projective curve of genus $g \ge 2$. Show that the Iitaka fibration of $C$ is the identity, and that $\varphi_m$ is a closed embedding for $m \ge 3$, while $\varphi_1$ is not an embedding when $C$ is hyperelliptic.
3. (A) Let $X$ be a smooth projective variety. Show that $\kappa(X \times \mathbb{P}^1) = -\infty$, and deduce that every smooth projective variety birational to $X \times \mathbb{P}^1$ has all plurigenera zero.
4. (B) Let $g \colon X' \dashrightarrow X$ be a dominant rational map between smooth projective varieties of the same dimension. Show that $P_m(X) \le P_m(X')$ for every $m$, and so $\kappa(X) \le \kappa(X')$.
5. (B) Let $S = E \times C$ with $E$ elliptic and $g(C) = 2$. Compute $P_m(S)$ for all $m \ge 1$, identify the Iitaka fibration of $S$, and check that its general fibre $F \cong E$ has $K_S|_F \sim 0$.
6. (C) Let $X$ be normal and $\kappa(D) = 0$. Show that for each $m \in N(D)$ the linear system $|mD|$ is a single divisor $F_m$, that $F_m + F_{m'} = F_{m + m'}$, and that $m' F_m = m F_{m'}$. Deduce that $e(D) \in N(D)$, so $N(D) = e(D) \mathbb{Z}_{>0}$.

### Lean

`MinimalModel.kodairaDim` is the Iitaka dimension of a canonical divisor, as in Definition 1.4.13, with $\bot$ for $-\infty$. The library has no Iitaka fibration yet, and neither the birational invariance of the plurigenera nor the formula for products is in Lean. The contraction in Theorem 1.4.12 is the notion of the library's contraction theorem, a projective morphism with $f_* \mathcal{O} = \mathcal{O}$.

### Notes and history

The fibration is due to Iitaka (1971), who used it to organize the classification of varieties by the Kodaira dimension; Ueno's lecture notes of 1975 give the classical account. The proof of parts 1 and 2 follows the structure of Laz04, Theorem 2.1.33, with the algebraic closedness written out through the normalization in a finite extension, and part 3 is cited from there. The birational invariance of the plurigenera is classical; for surfaces it is Theorem P5.11.6. Iitaka's easy addition $\kappa(X, D) \le \kappa(F, D|_F) + \dim Y$ for a fibration with general fibre $F$, and his conjecture $\kappa(X) \ge \kappa(F) + \kappa(Y)$ on the subadditivity of the Kodaira dimension, start from this fibration; the conjecture is open in general, and Kawamata showed that it follows from the existence of good minimal models, so from Conjectures 1.1.27 and 1.1.31.
