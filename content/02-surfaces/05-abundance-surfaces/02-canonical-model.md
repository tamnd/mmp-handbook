---
title: The canonical ring and the canonical model
nodes: []
sources: [Bea96, Rei97, Art66, KM98, Laz04, Kle66, Har77]
reads_with: [Bea96:ch10, Rei97:ch4, KM98:ch4]
requires: [P1.9, P1.13, P3.6, P3.12, P4.2, P4.4, P4.6, P5.1, P5.5, P5.8, P5.11, 1.1, 2.3, 4.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The canonical ring and the canonical model

### Statement

A minimal surface $S$ of general type has $K_S$ nef and big, and $K_S^2 > 0$ (part 4 of Theorem P5.11.26). The canonical class need not be ample: it is zero on the $(-2)$-curves. This section contracts those curves, proves that $K_S$ is semiample, and proves that the canonical ring is finitely generated with $\operatorname{Proj}$ the contracted surface. As before, $k$ is algebraically closed and surfaces are smooth and projective unless they are called normal.

**Definition 2.5.13 (canonical ring, canonical model).** The *canonical ring* of a surface $S$ is the graded ring
$$R(S, K_S) = \bigoplus_{n \geq 0} H^0(S, \mathcal{O}_S(nK_S)).$$
If $\kappa(S) = 2$ and $R(S, K_S)$ is finitely generated, the *canonical model* of $S$ is $S_{\mathrm{can}} = \operatorname{Proj} R(S, K_S)$. A *canonical surface* is a normal projective surface whose singularities are rational double points and whose canonical class is ample. For a normal projective variety $X$ and a Cartier divisor $D$, the *section ring* is $R(X, D) = \bigoplus_{n \geq 0} H^0(X, \mathcal{O}_X(nD))$, as in Example P1.13.31.

**Lemma 2.5.14 (the curves on which $K$ is trivial).** Let $S$ be a minimal surface of general type.

1. Every integral curve $C \subseteq S$ with $K_S \cdot C = 0$ is a smooth rational curve with $C^2 = -2$.
2. The classes of the curves $C$ with $K_S \cdot C = 0$ are linearly independent in $N^1(S)_{\mathbb{R}}$. So there are finitely many, $C_1, \dots, C_s$ with $s \leq \rho(S) - 1$, and their intersection matrix is negative definite.
3. Every connected component of $C_1 \cup \dots \cup C_s$ is a configuration of $(-2)$-curves whose dual graph is a Dynkin diagram of type $A$, $D$ or $E$, and Artin's criterion holds for it: it contracts to a rational double point.

Lean: not yet in Lean.

**Lemma 2.5.15 (finite generation for semiample divisors).** Let $X$ be a normal projective variety and $D$ a semiample Cartier divisor, with semiample fibration $\varphi' \colon X \to Z$ and $mD \sim \varphi'^* A$ as in Lemma 2.5.2. Then $R(X, D)$ is a finitely generated $k$-algebra and $\operatorname{Proj} R(X, D) \cong Z$. In particular, if $D$ is ample, then $\operatorname{Proj} R(X, D) \cong X$.

Lean: not yet in Lean.

**Theorem 2.5.16 (the canonical model).** Let $S$ be a minimal surface of general type, and $C_1, \dots, C_s$ the curves with $K_S \cdot C_i = 0$.

1. There are a normal projective surface $X$ and a birational morphism $f \colon S \to X$ that contracts exactly $C_1 \cup \dots \cup C_s$, one rational double point for each connected component, and is an isomorphism elsewhere. It is the minimal resolution of $X$.
2. $K_X$ is Cartier, $K_S = f^* K_X$, and $K_X$ is ample. So $X$ is a canonical surface, and its singularities are canonical.
3. $K_S$ is semiample with semiample fibration $f$. Pullback is an isomorphism of graded rings $R(X, K_X) \cong R(S, K_S)$, the canonical ring is finitely generated, and $S_{\mathrm{can}} = \operatorname{Proj} R(S, K_S) \cong X$.
4. If $S'$ is a smooth projective surface birational to $S$, then $R(S', K_{S'}) \cong R(S, K_S)$. So the canonical model depends only on the function field $k(S)$.

Lean: not yet in Lean.

The theorem shows that $K_S$ is semiample, but gives no bound on the multiple. Bombieri's theorem gives one.

**Theorem 2.5.17 (Bombieri).** Let $k = \mathbb{C}$ and let $S$ be a minimal surface of general type, with canonical model $f \colon S \to X$.

1. For $m \geq 2$ the linear system $|mK_S|$ has no fixed component.
2. For $m \geq 4$ the linear system $|mK_S|$ is base point free.
3. For $m \geq 5$ the morphism $\varphi_{|mK_S|}$ is birational onto its image, and it is $f$ followed by an embedding of $X$: $mK_X$ is very ample.

Lean: not yet in Lean.

This is the main theorem of E. Bombieri, "Canonical models of surfaces of general type", Publ. Math. IHÉS 42 (1973), 171 to 219, with the refinements for $m = 3$ and $m = 4$ of the same paper not stated here. The bound $5$ is sharp: for a surface with $K^2 = 1$ and $p_g = 2$ the map $\varphi_{|4K|}$ is not birational. Ekedahl ("Canonical models of surfaces of general type in positive characteristic", Publ. Math. IHÉS 67 (1988), 97 to 144) proved the same bounds in characteristic $p$, with additional exceptions in small characteristic. Theorem 2.5.17 gives a second proof of part 3 of Theorem 2.5.16 over $\mathbb{C}$: the Stein factorization of $\varphi_{|5K_S|}$ is a contraction $S \to Z$ with $5K_S$ the pullback of an ample divisor, and by part 3 of Lemma 2.5.2 it contracts exactly $C_1, \dots, C_s$.

### Proof in words

The curves on which $K_S$ is trivial lie in the orthogonal complement of a class of positive square, which is negative definite by the Hodge index theorem. Adjunction then forces them to be $(-2)$-curves, and their configurations are the $ADE$ configurations that Artin's criterion contracts to rational double points. A rational double point is a hypersurface singularity, so its canonical class is Cartier, given by a residue form, and the contraction is crepant by the negativity lemma. On the contracted surface $K_X$ has positive square and is positive on every curve, so it is ample by Nakai's criterion, and $K_S = f^* K_X$ is semiample.

Finite generation is then a statement about an ample divisor: the section ring of an ample divisor is finitely generated by Serre vanishing and Castelnuovo-Mumford regularity, and its $\operatorname{Proj}$ is the variety. Pullback identifies the canonical rings of $S$ and $X$ because $f_* \mathcal{O}_S = \mathcal{O}_X$, and the canonical ring is a birational invariant because a blow-up adds an exceptional divisor to $K$ that contributes no sections.

### Examples

**Example 2.5.18 (a quintic surface with a node).** Let $\operatorname{char} k = 0$ and
$$F = x_0^3 (x_1 x_2 - x_3^2) + x_1^5 + x_2^5 + x_3^5, \qquad X = V_+(F) \subseteq \mathbb{P}^3.$$
The partial derivatives are $F_0 = 3x_0^2 (x_1 x_2 - x_3^2)$, $F_1 = x_0^3 x_2 + 5x_1^4$, $F_2 = x_0^3 x_1 + 5 x_2^4$ and $F_3 = -2x_0^3 x_3 + 5x_3^4$. At a singular point with $x_0 = 0$, all $x_i^4$ vanish, which is impossible. At a singular point with $x_0 \neq 0$ and $(x_1, x_2, x_3) \neq 0$, write $q = x_1 x_2 - x_3^2$ and $G = x_1^5 + x_2^5 + x_3^5$: then $q = 0$, so $G = F - x_0^3 q = 0$, and $\nabla G = -x_0^3 \nabla q$ in the variables $x_1, x_2, x_3$. So the point $[x_1 : x_2 : x_3]$ of $\mathbb{P}^2$ lies on the conic $q = 0$ and the quintic $G = 0$, which are both smooth there, with the same tangent line. The conic is parametrized by $(s^2, t^2, st)$, and $G(s^2, t^2, st) = s^{10} + s^5 t^5 + t^{10}$. With $u = (s/t)^5$ this is $t^{10}(u^2 + u + 1)$, whose roots $u = \zeta, \zeta^2$ for a primitive cube root of unity $\zeta$ give ten distinct values of $s/t$, and $t = 0$ is not a root. So the conic and the quintic meet transversally in $10$ points, and there is no such singular point. The only singular point of $X$ is $p = [1 : 0 : 0 : 0]$, where in the chart $x_0 = 1$ the equation is $x_1 x_2 - x_3^2 + (\text{terms of degree } 5)$, with nondegenerate quadratic part: $p$ is an ordinary double point, the rational double point $A_1$. The surface $X$ is normal, as a hypersurface with an isolated singularity. Let $f \colon S \to X$ be the blow-up of $p$, the minimal resolution, with exceptional curve $E$, a smooth conic with $E^2 = -2$. The proof of Corollary P3.12.31 is local and applies to the smooth locus, so $K_X \sim H$ for a plane section $H$ there, hence on $X$, since the singular locus is a point. So $K_X$ is the Cartier divisor $H$. Write $K_S = f^* H + aE$. Adjunction gives $K_S \cdot E = 0$, and $f^* H \cdot E = 0$, so $-2a = 0$ and $K_S = f^* H$. So $K_S$ is nef and big with $K_S^2 = H^2 = 5$, $K_S \cdot E = 0$, and $K_S \cdot C = \deg f(C) > 0$ for every other curve. So $S$ is minimal of general type, $E$ is its only $(-2)$-curve, and $X$ is its canonical model. The sequence $0 \to \mathcal{O}_{\mathbb{P}^3}(m - 5) \to \mathcal{O}_{\mathbb{P}^3}(m) \to \mathcal{O}_X(m) \to 0$ and $H^1(\mathbb{P}^3, \mathcal{O}(m - 5)) = 0$ give $H^0(X, \mathcal{O}_X(m)) = k[x_0, \dots, x_3]_m / F \cdot k[x_0, \dots, x_3]_{m - 5}$, so
$$R(S, K_S) \cong R(X, \mathcal{O}_X(1)) = k[x_0, x_1, x_2, x_3]/(F).$$
It is generated in degree $1$ with one relation in degree $5$. As in Example P5.11.11, $p_g(S) = 4$, $P_2(S) = 10$ and $h^1(\mathcal{O}_X) = 0$. Since $p$ is a rational singularity, $R^1 f_* \mathcal{O}_S = 0$, and the Leray spectral sequence gives $q(S) = h^1(\mathcal{O}_X) = 0$. So $\chi(\mathcal{O}_S) = 5$ and $K_S^2 = 5$, the invariants of a smooth quintic. The bound of Theorem 2.5.17 is far from sharp here: already $|K_S|$ is free and $\varphi_{|K_S|}$ is $f$ followed by the embedding of $X$.

**Example 2.5.19 (a product of two curves).** Let $C_1$ and $C_2$ be curves of genera $g_1, g_2 \geq 2$ and $S = C_1 \times C_2$ with projections $p_1, p_2$. Then $K_S = p_1^* K_{C_1} + p_2^* K_{C_2}$, and $K_S$ is ample: $3K_{C_i}$ has degree $6g_i - 6 \geq 2g_i + 1$ and is very ample by part 2 of Corollary P5.1.20, and $3K_S$ is the pullback of $\mathcal{O}(1)$ under the Segre embedding of the product of the two embeddings. So $S$ has no $(-2)$-curve, $S = S_{\mathrm{can}}$, and by Lemma P5.11.4
$$R(S, K_S) = \bigoplus_{n \geq 0} H^0(C_1, nK_{C_1}) \otimes_k H^0(C_2, nK_{C_2}),$$
the Segre product of the two canonical rings. The invariants are $K_S^2 = 2(2g_1 - 2)(2g_2 - 2) = 8(g_1 - 1)(g_2 - 1)$, $p_g = g_1 g_2$, $q = g_1 + g_2$ and $\chi(\mathcal{O}_S) = 1 - g_1 - g_2 + g_1 g_2 = (g_1 - 1)(g_2 - 1)$. For $n \geq 2$, $P_n = (2n - 1)^2 (g_1 - 1)(g_2 - 1)$, which agrees with Riemann-Roch: $\chi(\mathcal{O}_S) + \frac{1}{2} n(n - 1) K_S^2 = (g_1 - 1)(g_2 - 1)(1 + 4n(n - 1))$ and $1 + 4n(n - 1) = (2n - 1)^2$.

**Example 2.5.20 (failure on a non-minimal surface).** Let $S$ be a minimal surface of general type and $S' \to S$ a composite of $r$ blow-ups of points. By part 4 of Theorem 2.5.16, $R(S', K_{S'}) \cong R(S, K_S)$ is finitely generated and $\operatorname{Proj} R(S', K_{S'})$ is the canonical model $X$ of $S$. But $K_{S'}$ is negative on the last exceptional curve, so it is not nef and not semiample, and $K_{S'}^2 = K_S^2 - r$. For the quintic of Example 2.5.18 blown up in $6$ points, $K_{S'}^2 = -1 < 0$ although $\kappa(S') = 2$. Finite generation and the canonical model are birational invariants, while semiampleness of $K$ holds only on the minimal model.

### Proof

*Proof of Lemma 2.5.14.* (1) Let $H$ be ample. By the Hodge index theorem (Theorem P5.5.22), the intersection form on $N^1(S)_{\mathbb{R}}$ is negative definite on $H^\perp$, a hyperplane. Let $v \neq 0$ be a class with $K_S \cdot v = 0$, and suppose $v^2 \geq 0$. On the plane spanned by $K_S$ and $v$, the form is $a^2 K_S^2 + b^2 v^2 \geq 0$ for $aK_S + bv$, and $K_S$ and $v$ are independent because $K_S^2 > 0 = K_S \cdot v$. This plane meets $H^\perp$ in a nonzero class $w$, since $2 + (\rho - 1) > \rho$, and then $w^2 \geq 0$ and $w^2 < 0$, a contradiction. So $K_S^\perp$ is negative definite. An integral curve $C$ has $C \cdot H > 0$, so its class is not zero, and $K_S \cdot C = 0$ gives $C^2 < 0$. Adjunction (Theorem P5.5.14) gives $2p_a(C) - 2 = C^2 + K_S \cdot C = C^2 < 0$, so $p_a(C) = 0$ and $C^2 = -2$, and an integral curve of arithmetic genus $0$ is smooth and rational. (2) Let $C_1, \dots, C_t$ be distinct such curves and suppose $\sum_i a_i C_i \equiv 0$ with real $a_i$. Write $\sum_i a_i C_i = P - N$ with $P, N \geq 0$ without common components. Then $P \equiv N$, so $P^2 = P \cdot N \geq 0$. But $P$ lies in $K_S^\perp$, so $P^2 < 0$ unless $P \equiv 0$, and an effective nonzero divisor is not numerically trivial. So $P = 0$, similarly $N = 0$, and all $a_i = 0$. The classes lie in the $(\rho - 1)$-dimensional space $K_S^\perp$, so $t \leq \rho - 1$, and the form on their span is negative definite. (3) Each connected component is a connected negative definite configuration of curves with $C_i^2 = -2$ and $K_S \cdot C_i = 0$, so Proposition P5.8.17 shows that it satisfies Artin's criterion and contracts to a rational double point. Its dual graph is of type $A$, $D$ or $E$ by Proposition 4.3.12. $\square$

*Proof of Lemma 2.5.15.* First let $A$ be an ample Cartier divisor on a projective variety $Z$, and $\mathcal{G}$ a coherent sheaf on $Z$. Choose $c \geq 1$ with $cA$ very ample, giving $Z \subseteq \mathbb{P}^M$ with $\mathcal{O}(1)|_Z = \mathcal{O}_Z(cA)$, and put $T = k[x_0, \dots, x_M]$. By Theorem P4.2.7 the sheaf $\mathcal{G}$, viewed on $\mathbb{P}^M$, is $n_1$-regular for some $n_1$, and by Corollary P4.2.17 the $T$-module $\bigoplus_{n \geq n_1} H^0(Z, \mathcal{G}(n))$ is generated by its part of degree $n_1$. Each $H^0(Z, \mathcal{G}(n))$ is finite dimensional, so $\Gamma_{\geq 0}(\mathcal{G}) = \bigoplus_{n \geq 0} H^0(Z, \mathcal{G}(n))$ is a finitely generated graded $T$-module.

Now let $D$ be semiample on $X$ with $mD \sim \varphi'^* A$. For $0 \leq i < cm$ the projection formula (Theorem P4.4.10) gives
$$\bigoplus_{n \geq 0} H^0(X, (ncm + i)D) \cong \bigoplus_{n \geq 0} H^0\big(Z, \mathcal{G}_i(n)\big), \qquad \mathcal{G}_i = \varphi'_* \mathcal{O}_X(iD),$$
and $\mathcal{G}_i$ is coherent because $\varphi'$ is projective. So $R(X, D)$ is the direct sum of the $cm$ finitely generated $T$-modules $\Gamma_{\geq 0}(\mathcal{G}_i)$, where $T$ acts through $T_1 = H^0(\mathbb{P}^M, \mathcal{O}(1)) \to H^0(Z, cA) = H^0(X, cmD)$. The images of $x_0, \dots, x_M$ together with finitely many module generators generate $R(X, D)$ as a $k$-algebra.

For the $\operatorname{Proj}$, put $R' = R(X, D)^{(cm)} = \bigoplus_n H^0(Z, \mathcal{O}_Z(n))$, using part 2 of Lemma 2.5.2. Let $I_Z \subseteq T$ be the ideal of all forms that vanish on $Z$. The map $(T/I_Z)_n \to H^0(Z, \mathcal{O}_Z(n))$ is injective by the definition of $I_Z$, and surjective for $n \geq n_0$ because $H^1(\mathbb{P}^M, \mathcal{I}_Z(n)) = 0$ for $n \geq n_0$ by Theorem P4.2.7. In degree $0$ both sides are $k$, since $Z$ is a connected reduced projective scheme over $k = \bar k$. So the Veronese subrings $(T/I_Z)^{(n_0)}$ and $R'^{(n_0)}$ are isomorphic. By part 5 of Proposition P3.6.4, applied three times, and part 4,
$$\operatorname{Proj} R(X, D) \cong \operatorname{Proj} R' \cong \operatorname{Proj} R'^{(n_0)} \cong \operatorname{Proj} (T/I_Z)^{(n_0)} \cong \operatorname{Proj} T/I_Z = Z.$$
If $D$ is ample, then $|mD|$ is very ample for $m$ large, $\varphi'$ is an isomorphism, and $Z = X$. $\square$

*Proof of Theorem 2.5.16.* (1) By Lemma 2.5.14 the curves $C_1, \dots, C_s$ form a negative definite configuration, each connected component of which satisfies Artin's criterion of Theorem P5.8.16. Artin's construction (Artin 1962, Amer. J. Math. 84, Theorem 2.3 and its proof) uses only the inequality $p_a(Z) \leq 0$ for every positive cycle $Z$ supported on the configuration. This inequality holds for the union: write $Z = Z_1 + \dots + Z_t$ with the $Z_j$ nonzero and supported on distinct components, so $Z_j \cdot Z_l = 0$ for $j \neq l$, and part 3 of Proposition P5.8.13 gives $p_a(Z) = \sum_j p_a(Z_j) - (t - 1) \leq 0$. So the whole configuration is contracted by one birational morphism $f \colon S \to X$ to a normal projective surface, with one rational double point for each component (part 3 of Proposition P5.8.17). No exceptional curve is a $(-1)$-curve, so $f$ is the minimal resolution of $X$, by Definition 2.3.7 and part 3 of Theorem 2.3.8.

(2) Let $x \in X$ be one of the singular points. By part 3 of Proposition P5.8.17 the local ring $\mathcal{O}_{X,x}$ has embedding dimension $3$. Embed an affine neighbourhood of $x$ in $\mathbb{A}^N$ with ideal $I$. By the Jacobian criterion (Theorem P1.9.12) the Jacobian matrix of $I$ has rank $N - 3$ at $x$, so there are $g_1, \dots, g_{N - 3} \in I$ with independent differentials at $x$, and near $x$ they define a closed subvariety $V \supseteq X$ that is smooth of dimension $3$ at $x$. The ideal of $X$ in the regular local ring $\mathcal{O}_{V,x}$ is a prime of height $1$, hence principal by Theorem P1.9.25: near $x$, $X = \{h = 0\} \subseteq V$. Let $u, v, w$ be regular parameters of $V$ at $x$, so that $du, dv, dw$ is a basis of $\Omega_V$ near $x$, and write $dh = h_u \, du + h_v \, dv + h_w \, dw$. On the smooth locus of $X$ near $x$ the relation $dh = 0$ shows that the rational $2$-form
$$\omega_0 = \frac{du \wedge dv}{h_w} = \frac{dv \wedge dw}{h_u} = \frac{dw \wedge du}{h_v}$$
is well defined. At each smooth point of $X$ near $x$ one of $h_u, h_v, h_w$ is nonzero, by the Jacobian criterion, and there $\omega_0$ is a generator of $\Omega^2_X$: for $h_w \neq 0$, $du, dv$ is a basis of $\Omega_X$. So $\operatorname{div}(\omega_0) = 0$ near $x$, since the singular locus is a point, and $K_X$ is Cartier at $x$ by part 3 of Proposition P3.12.29. Away from the singular points $X$ is smooth. So $K_X$ is Cartier.

Choose a rational $2$-form $\omega$ on $X$ and put $K_X = \operatorname{div}_X(\omega)$ and $K_S = \operatorname{div}_S(f^* \omega)$. These agree outside the exceptional curves, so $K_S = f^* K_X + \sum_i a_i C_i$ for integers $a_i$. For every $j$, $f^* K_X \cdot C_j = 0$ because $C_j$ maps to a point, and $K_S \cdot C_j = 0$, so $(\sum_i a_i C_i) \cdot C_j = 0$, and Theorem P5.8.2 gives $\sum_i a_i C_i = 0$. So $K_S = f^* K_X$.

By Corollary P5.8.5, the Mumford pullback of the Cartier divisor $K_X$ is the usual pullback, so $K_X^2 = (f^* K_X)^2 = K_S^2 > 0$. Let $C' \subseteq X$ be an integral curve and $C \subseteq S$ its strict transform. Then $C \to C'$ is birational, so $K_X \cdot C' = \deg (\mathcal{O}_X(K_X)|_{C'}) = \deg (\mathcal{O}_S(f^* K_X)|_C) = K_S \cdot C$, and $K_S \cdot C > 0$ because $C$ is not one of the $C_i$ and $K_S$ is nef. By the Nakai criterion for a projective scheme (Laz04, Theorem 1.2.23, from Kle66), $K_X$ is ample. Since $f$ is crepant and $K_X$ is Cartier, Theorem 4.3.11 shows that the singularities of $X$ are canonical.

(3) Choose $m$ with $mK_X$ very ample. Then $mK_S = f^*(mK_X)$ is base point free, so $K_S$ is semiample, and the morphism of $|mK_S|$ is $f$ followed by the embedding of $X$, whose Stein factorization is $f$ because $f_* \mathcal{O}_S = \mathcal{O}_X$ by Theorem P4.6.8. By the projection formula, $H^0(S, nK_S) = H^0(S, f^* nK_X) \cong H^0(X, nK_X)$ for all $n \geq 0$, compatibly with products. So $R(S, K_S) \cong R(X, K_X)$, which is finitely generated with $\operatorname{Proj} \cong X$ by Lemma 2.5.15.

(4) The surface $S'$ has $\kappa(S') = 2$ by Theorem P5.11.6, and by Corollary P5.11.19 the minimal model of $S'$ is $S$, reached by a composite of blow-ups $g \colon S' \to S$. By Lemma P5.11.15, $K_{S'} = g^* K_S + Z$ with $Z \geq 0$ exceptional. Let $s_Z$ be a section of $\mathcal{O}_{S'}(Z)$ with divisor $Z$. The maps $H^0(S, nK_S) \to H^0(S', nK_{S'})$, $\sigma \mapsto g^* \sigma \cdot s_Z^n$, are injective and multiplicative, and both sides have dimension $P_n(S) = P_n(S')$ by Theorem P5.11.6. So they form an isomorphism of graded rings. $\square$

### Exercises

1. (A) Let $S$ be a surface with $K_S$ ample. Show that $S$ is minimal of general type and $S = S_{\mathrm{can}}$. For a smooth quintic $S \subseteq \mathbb{P}^3$ with equation $F$, show $R(S, K_S) = k[x_0, \dots, x_3]/(F)$.
2. (A) Let $S$ be a minimal surface of general type and $C \subseteq S$ a smooth rational curve with $C^2 = -2$. Show that $K_S \cdot C = 0$, so that $C$ is one of the curves contracted to the canonical model.
3. (B) Let $C$ be a curve of genus $2$ with hyperelliptic map $C \to \mathbb{P}^1$ branched over the zeros of a binary sextic $f_6$. Show that $R(C, K_C) \cong k[x, y, z]/(z^2 - f_6(x, y))$ with $\deg x = \deg y = 1$ and $\deg z = 3$, so that the canonical ring of a curve need not be generated in degree $1$.
4. (B) Let $X$ be a normal projective surface with only rational double points and $K_X$ ample, and $f \colon S \to X$ its minimal resolution. Show that $S$ is a minimal surface of general type and that $X \cong S_{\mathrm{can}}$.
5. (B) Let $\pi \colon S \to \mathbb{P}^2$ be the double cover branched along a smooth curve of degree $10$, with $\operatorname{char} k \neq 2$. Show that $K_S = \pi^* \mathcal{O}(2)$ is ample, and compute $K_S^2 = 8$, $p_g = 6$, $q = 0$ and $\chi(\mathcal{O}_S) = 7$, using $\pi_* \mathcal{O}_S = \mathcal{O} \oplus \mathcal{O}(-5)$.
6. (C) Let $\operatorname{char} k = 0$ and $S$ a minimal surface of general type. Prove that $K_S$ is semiample without Artin's theorem: apply the base point free theorem (KM98, Theorem 3.3) to the klt pair $(S, 0)$ and $D = K_S$ with $a = 2$, and show with Lemma 2.5.2 that the semiample fibration is the contraction of Theorem 2.5.16.

### Lean

The finite generation of the canonical ring in all dimensions is `MinimalModel.FiniteGenerationCanonical`, the statement of the finite generation Theorem 1.1.29. Theorem 2.5.16 is its case of surfaces of general type, which the Lean project does not state separately. The statements of this section are not yet in Lean.

### Notes and history

The finite generation of the canonical ring of a surface goes back to Zariski, "The theorem of Riemann-Roch for high multiples of an effective divisor on an algebraic surface", Ann. of Math. 76 (1962), 560 to 615. Zariski introduced the decomposition of a divisor into a nef part and a negative part, Theorem P5.8.24, and studied the finite generation of section rings on surfaces. Mumford's appendix to the same paper, "The canonical ring of an algebraic surface", pages 612 to 615, proved that the canonical ring of a surface is finitely generated. The contraction of the $(-2)$-curves is from Artin's papers of 1962 and 1966 (Art66), which also identify the rational double points. Kodaira studied the pluricanonical maps in "Pluricanonical systems on algebraic surfaces of general type", J. Math. Soc. Japan 20 (1968), and Bombieri's paper of 1973 gave the effective bounds of Theorem 2.5.17 and the name canonical model. Reid (Rei97, Chapter 4) and Beauville (Bea96, Chapter X) are good introductions. In higher dimension finite generation of the canonical ring is the theorem of Birkar, Cascini, Hacon and McKernan, and of Siu, recalled in Example P1.13.31, and the canonical model is again $\operatorname{Proj}$ of the canonical ring.
