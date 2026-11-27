---
title: Abundance for minimal surfaces of Kodaira dimension at most one
nodes: []
sources: [Bea96, Rei97, KM98, Har77]
reads_with: [Bea96:ch8, Bea96:ch9, Rei97:ch4]
requires: [P1.13, P4.4, P4.6, P5.1, P5.5, P5.7, P5.10, P5.11, P5.12, 1.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Abundance for minimal surfaces of Kodaira dimension at most one

### Statement

Throughout, $k$ is an algebraically closed field and a surface is a smooth projective surface over $k$, unless it is said to be normal. The minimal model program for a surface $S$ ends either at a Mori fibre space or at a minimal surface with nef canonical class (Theorem P5.12.21). Abundance says that a nef canonical class is semiample. This section proves the first step, that a nef canonical class has $\kappa \geq 0$, and then abundance for $\kappa = 0$ and $\kappa = 1$.

**Definition 2.5.1 (semiample divisor, semiample fibration).** Let $X$ be a normal projective variety and $D$ a Cartier divisor on $X$. Then $D$ is *semiample* if the linear system $|mD|$ is base point free for some $m \geq 1$. A $\mathbb{Q}$-Cartier $\mathbb{Q}$-divisor $D$ is semiample if some multiple $mD$ that is Cartier is semiample. If $|mD|$ is free, let $\varphi \colon X \to \mathbb{P}^N$ be the morphism it defines and $X \xrightarrow{\varphi'} Z \xrightarrow{g} \mathbb{P}^N$ its Stein factorization. The morphism $\varphi' \colon X \to Z$ is the *semiample fibration* of $D$. When $D = K_X$ it is the *Iitaka fibration* of $X$.

This is the semiampleness of Definition 1.1.26, for divisors with rational coefficients. The semiample fibration does not depend on $m$: the lemma below shows that it contracts exactly the curves $C$ with $D \cdot C = 0$ when $X$ is a surface, and a contraction of a normal variety is determined by the curves it contracts.

**Lemma 2.5.2 (the semiample fibration).** Let $X$ be a normal projective variety and $D$ a Cartier divisor with $|mD|$ base point free, and let $\varphi' \colon X \to Z$ be as in Definition 2.5.1.

1. $Z$ is a normal projective variety, $\varphi'_* \mathcal{O}_X = \mathcal{O}_Z$, and there is an ample Cartier divisor $A$ on $Z$ with $mD \sim \varphi'^* A$.
2. For every $j \geq 0$, pullback is an isomorphism $H^0(Z, \mathcal{O}_Z(jA)) \cong H^0(X, \mathcal{O}_X(jmD))$.
3. An integral curve $C \subseteq X$ is contracted by $\varphi'$ if and only if $D \cdot C = 0$. In particular $D$ is nef.
4. If $X$ is a smooth projective surface, then $\kappa(D) = \dim Z$.

Lean: not yet in Lean.

**Theorem 2.5.3 (a nef canonical class has $\kappa \geq 0$).** Let $S$ be a surface with $K_S$ nef. Then $\kappa(S) \geq 0$.

Lean: not yet in Lean.

**Theorem 2.5.4 (abundance for $\kappa = 0$).** Let $S$ be a surface with $K_S$ nef and $\kappa(S) = 0$. Then $K_S \equiv 0$ and $12 K_S \sim 0$. In particular $K_S$ is semiample, its semiample fibration is the map to a point, and the Veronese subring $\bigoplus_{n} H^0(S, 12 n K_S)$ of the canonical ring is the polynomial ring $k[t]$.

Lean: not yet in Lean.

**Theorem 2.5.5 (abundance for $\kappa = 1$).** Let $S$ be a surface with $K_S$ nef and $\kappa(S) = 1$. Then $K_S^2 = 0$, and there are a smooth projective curve $B$, a morphism $f \colon S \to B$ with $f_* \mathcal{O}_S = \mathcal{O}_B$ whose general fibre is an integral curve of arithmetic genus $1$, an integer $n \geq 1$ and a divisor $D$ on $B$ of positive degree with $n K_S \sim f^* D$. The divisor $K_S$ is semiample, and $f$ is its Iitaka fibration.

Lean: not yet in Lean.

The fibration $f$ is elliptic, or, only in characteristic $2$ and $3$, quasi-elliptic. Over $\mathbb{C}$ Kodaira's formula identifies $n$ and $D$.

**Theorem 2.5.6 (Kodaira's canonical bundle formula).** Let $k = \mathbb{C}$, and let $f \colon S \to B$ be a relatively minimal elliptic fibration: $B$ is a smooth projective curve, $f_* \mathcal{O}_S = \mathcal{O}_B$, the general fibre is a smooth curve of genus $1$, and no fibre contains a $(-1)$-curve. For a point $b \in B$ let $m_b$ be the greatest common divisor of the coefficients of the divisor $f^* b$, and let $b_1, \dots, b_r$ be the points with $m_i = m_{b_i} \geq 2$, with $f^* b_i = m_i F_i$. Then $R^1 f_* \mathcal{O}_S$ is an invertible sheaf. Put $L = (R^1 f_* \mathcal{O}_S)^\vee$. Then
$$\omega_S \cong f^* (\omega_B \otimes L) \otimes \mathcal{O}_S\Big(\sum_{i=1}^r (m_i - 1) F_i\Big), \qquad \deg L = \chi(\mathcal{O}_S) \geq 0.$$

Lean: not yet in Lean.

This is Kodaira's theorem, from "On compact analytic surfaces II and III", Ann. of Math. 77 (1963), 563 to 626, and 78 (1963), 1 to 40. The handbook cites it in the form of Barth, Hulek, Peters and Van de Ven, *Compact complex surfaces*, second edition, Springer 2004 (BHPV below), Theorem V.12.1 and its proof. The equality $\deg L = \chi(\mathcal{O}_S)$ is proved below. In characteristic $p$, Bombieri and Mumford ("Enriques' classification of surfaces in char. p, II", in *Complex analysis and algebraic geometry*, Cambridge 1977, Theorem 2) prove $R^1 f_* \mathcal{O}_S = M \oplus T$ with $M$ invertible and $T$ a torsion sheaf, and $\omega_S \cong f^*(\omega_B \otimes M^{\vee}) \otimes \mathcal{O}_S(\sum a_i F_i)$ with $0 \leq a_i \leq m_i - 1$, where $a_i = m_i - 1$ unless the fibre is a wild fibre, which needs $T \neq 0$ at $b_i$.

**Lemma 2.5.7 (multiple fibres push forward to nothing).** In the situation of Theorem 2.5.6, let $b \in B$ with $f^* b = mF$ and let $0 \leq j < m$. Then $f_* \mathcal{O}_S(jF) = \mathcal{O}_B$.

Lean: not yet in Lean.

**Corollary 2.5.8 (the plurigenera of an elliptic surface).** In the situation of Theorem 2.5.6, let $F$ be a general fibre, and put
$$d = 2g(B) - 2 + \chi(\mathcal{O}_S), \qquad \delta = d + \sum_{i=1}^r \Big(1 - \frac{1}{m_i}\Big).$$

1. $K_S \equiv \delta F$ and $K_S^2 = 0$.
2. For every $n \geq 1$, $P_n(S) = h^0(B, D_n)$, where $D_n = n(K_B + L) + \sum_i \lfloor n(m_i - 1)/m_i \rfloor \, b_i$ has degree $nd + \sum_i \lfloor n(m_i - 1)/m_i \rfloor$. Here $L$ also denotes a divisor of the invertible sheaf $L$.
3. If $\delta > 0$, then $K_S$ is nef and semiample, $\kappa(S) = 1$, and $M K_S \sim f^* D_M$ for $M = \operatorname{lcm}(m_1, \dots, m_r)$ ($M = 1$ if $r = 0$), with $\deg D_M = M \delta$. If $\delta = 0$, then $K_S \equiv 0$ and $\kappa(S) = 0$. If $\delta < 0$, then $\kappa(S) = -\infty$.

Lean: not yet in Lean.

### Proof in words

A surface with $\kappa = -\infty$ is birationally ruled, so it is dominated by a blow-up $W$ of $C \times \mathbb{P}^1$ on which a general ruling $F'$ has $K_W \cdot F' = -2$. On the other hand $K_W$ is the pullback of $K_S$ plus an effective exceptional divisor, and both parts meet $F'$ nonnegatively when $K_S$ is nef. This contradiction gives $\kappa \geq 0$.

Nef canonical class excludes $(-1)$-curves, so $S$ is minimal, and the classification (Theorem P5.11.26) gives the rest for $\kappa = 0$ and $\kappa = 1$: in the first case $K_S$ is torsion, and in the second a multiple of $K_S$ is the pullback of a divisor of positive degree from a curve, which has a free multiple. Kodaira's formula makes the second case numerical: the canonical class is a rational multiple $\delta F$ of a fibre, and $\delta$ is the degree of $K_B + L$ corrected by the multiple fibres. Every plurigenus is then $h^0$ of an explicit divisor on $B$, because a fraction of a multiple fibre pushes forward to $\mathcal{O}_B$.

### Examples

**Example 2.5.9 (Weierstrass fibrations over $\mathbb{P}^1$).** Let $k = \mathbb{C}$ and $N \geq 1$. For general forms $a \in H^0(\mathbb{P}^1, \mathcal{O}(4N))$ and $b \in H^0(\mathbb{P}^1, \mathcal{O}(6N))$, the surface $W \subseteq \mathbb{P}(\mathcal{O} \oplus \mathcal{O}(-2N) \oplus \mathcal{O}(-3N))$ given by $y^2 z = x^3 + a x z^2 + b z^3$ is smooth, and the projection $f \colon W \to \mathbb{P}^1$ is a relatively minimal elliptic fibration with the section $\{z = 0\}$, with only nodal singular fibres, and with $R^1 f_* \mathcal{O}_W \cong \mathcal{O}(-N)$ (Miranda, *The basic theory of elliptic surfaces*, ETS Pisa 1989, Chapters II and III). A section meets every fibre with intersection number $1$, so no fibre is multiple. Theorem 2.5.6 gives $L = \mathcal{O}(N)$, $\chi(\mathcal{O}_W) = N$ and
$$K_W \sim f^*(K_{\mathbb{P}^1} + L) = f^* \mathcal{O}(N - 2) = (N - 2) F.$$
For $N = 1$, $K_W = -F$ and $\kappa = -\infty$: $W$ is a rational elliptic surface, the surface $X_9$ of Theorem P5.10.21, where also $F = -K$. For $N = 2$, $K_W \sim 0$ and $W$ is a K3 surface. For $N \geq 3$, $K_W = (N - 2)F$ is free, $\kappa = 1$, and $P_n = h^0(\mathbb{P}^1, \mathcal{O}(n(N - 2))) = n(N - 2) + 1$ by the projection formula (Theorem P4.4.10) and $f_* \mathcal{O}_W = \mathcal{O}_{\mathbb{P}^1}$. Take $N = 3$. Then $p_g = 2$ and $P_n = n + 1$. The Leray spectral sequence of $f$ has only two rows, so for a sheaf $\mathcal{F} = f^* \mathcal{O}(n)$ it gives the exact sequence $0 \to H^1(\mathbb{P}^1, \mathcal{O}(n)) \to H^1(W, \mathcal{F}) \to H^0(\mathbb{P}^1, \mathcal{O}(n) \otimes R^1 f_* \mathcal{O}_W) \to 0$, the last term because $H^2$ of a sheaf on a curve vanishes. With $R^1 f_* \mathcal{O}_W = \mathcal{O}(-3)$ this gives $q = h^1(\mathcal{O}_W) = 0 + h^0(\mathcal{O}(-3)) = 0$ and $h^1(nK_W) = h^0(\mathcal{O}(n - 3)) = n - 2$ for $n \geq 2$. Riemann-Roch (Theorem P5.5.13) checks this: $\chi(\mathcal{O}_W) = 1 - 0 + p_g = 3 = N$, and for $n \geq 2$, $h^0(nK) - h^1(nK) + h^2(nK) = (n + 1) - (n - 2) + h^0((1 - n)K) = 3 = \chi(\mathcal{O}_W) + \frac{1}{2} n(n - 1) K^2$, since $K^2 = 0$ and $(1 - n)K = -(n - 1)F$ is not effective.

**Example 2.5.10 (the Dolgachev surface).** Let $k = \mathbb{C}$. Dolgachev constructed, by two logarithmic transformations of a rational elliptic surface, an algebraic surface $S$ with $p_g = q = 0$ and a relatively minimal elliptic fibration $f \colon S \to \mathbb{P}^1$ whose only multiple fibres have multiplicities $2$ and $3$ (Dolgachev, "Algebraic surfaces with $q = p_g = 0$", in *Algebraic surfaces*, C.I.M.E. 1977, Liguori, Naples 1981). Then $\chi(\mathcal{O}_S) = 1$, so $\deg L = 1$, $K_B + L$ has degree $d = -2 + 1 = -1$, and
$$\delta = -1 + \frac{1}{2} + \frac{2}{3} = \frac{1}{6}.$$
So $K_S \equiv \frac{1}{6} F$, $K_S$ is nef and $\kappa(S) = 1$. By Corollary 2.5.8, $P_n = h^0(\mathbb{P}^1, \mathcal{O}(e_n)) = \max(0, e_n + 1)$ with $e_n = -n + \lfloor n/2 \rfloor + \lfloor 2n/3 \rfloor$. This gives $e_1 = -1$, $e_2 = e_3 = e_4 = e_5 = 0$, $e_6 = 1$ and $e_{12} = 2$, so $P_1 = 0$, $P_2 = P_3 = P_4 = P_5 = 1$, $P_6 = 2$ and $P_{12} = 3$. For $n = 6$ the remainders $r_i$ of $6(m_i - 1)$ modulo $m_i$ vanish, so $6 K_S \sim f^* \mathcal{O}(1) = F$, and $|6 K_S| = |F|$ is the free pencil of fibres: $K_S$ is semiample with Iitaka fibration $f$, while $|K_S|$ is empty and $|2K_S|$ is a single divisor. For $n = 2$, $2(m_1 - 1) = 2 = 1 \cdot 2 + 0$ and $2(m_2 - 1) = 4 = 1 \cdot 3 + 1$, so $D_2$ has degree $-2 + 1 + 1 = 0$ and $2K_S \sim f^* D_2 + F_2 \sim F_2$, where $f^* b_2 = 3F_2$. So the unique member of $|2K_S|$ is the curve $F_2$ under the triple fibre.

**Example 2.5.11 (the product $E \times C$).** Let $E$ be an elliptic curve, $C$ a curve of genus $g \geq 2$, $S = E \times C$ and $q \colon S \to C$ the projection. By Example P5.11.10, $K_S = q^* K_C$, so $|K_S| = q^* |K_C|$ is base point free by Theorem P5.1.23. Kodaira's formula agrees: $R^1 q_* \mathcal{O}_S \cong H^1(E, \mathcal{O}_E) \otimes \mathcal{O}_C \cong \mathcal{O}_C$, so $L = \mathcal{O}_C$ and $\deg L = 0 = \chi(\mathcal{O}_S)$, there are no multiple fibres, and $\delta = 2g - 2$. By Lemma P5.11.4 and $H^0(E, \mathcal{O}_E(nK_E)) = H^0(E, \mathcal{O}_E) = k$,
$$R(S, K_S) = \bigoplus_{n \geq 0} H^0(S, nK_S) \cong \bigoplus_{n \geq 0} H^0(C, nK_C) = R(C, K_C),$$
a finitely generated ring with $\operatorname{Proj} R(C, K_C) = C$ (Example P1.13.31, since $K_C$ is ample by part 3 of Corollary P5.1.20). The Iitaka fibration of $S$ is $q$, and $P_n(S) = (2n - 1)(g - 1)$ for $n \geq 2$.

**Example 2.5.12 (failure without nefness).** Let $S = E \times C$ as in Example 2.5.11 and $\sigma \colon S' \to S$ the blow-up of a point, with exceptional curve $E_p$. Then $K_{S'} = \sigma^* K_S + E_p$ and $K_{S'} \cdot E_p = -1$, so $K_{S'}$ is not nef, and by part 3 of Lemma 2.5.2 it is not semiample. Every member of $|nK_{S'}|$ is $\sigma^* G + nE_p$ with $G \in |nK_S|$, because multiplication by the section of $\mathcal{O}(nE_p)$ maps $\sigma^* H^0(S, nK_S)$ injectively into $H^0(S', nK_{S'})$ and the two spaces have the same dimension (Theorem P5.11.6). So the base locus of every $|nK_{S'}|$ contains $E_p$, while $\kappa(S') = 1$ and $R(S', K_{S'}) \cong R(S, K_S)$ is still finitely generated. Abundance is a statement about the minimal model, not about $S$.

### Proof

*Proof of Lemma 2.5.2.* (1) $X$ is integral and normal, and $\mathcal{O}_Z = \varphi'_* \mathcal{O}_X$ by the construction of the Stein factorization (Theorem P4.6.15). For an open $U \subseteq Z$, $\mathcal{O}_Z(U) = \mathcal{O}_X(\varphi'^{-1} U)$ and an element of $k(Z) \subseteq k(X)$ that is integral over this ring is regular on the normal variety $\varphi'^{-1} U$, so it lies in the ring. So $Z$ is normal. It is projective because $g$ is finite and $\mathbb{P}^N$ is projective. Put $A = g^* H$ for a hyperplane $H$. A finite pullback of an ample divisor is ample (Har77, Exercise III.5.7), and $mD \sim \varphi^* H = \varphi'^* A$. (2) By the projection formula (Theorem P4.4.10), $\varphi'_* \mathcal{O}_X(jmD) \cong \varphi'_* \varphi'^* \mathcal{O}_Z(jA) \cong \mathcal{O}_Z(jA) \otimes \varphi'_* \mathcal{O}_X = \mathcal{O}_Z(jA)$, and taking global sections gives the claim. (3) $mD \cdot C = \deg(\varphi^* \mathcal{O}(1)|_C)$, which is $\deg(\varphi|_C) \cdot \deg \varphi(C)$ if $\varphi(C)$ is a curve and $0$ if it is a point. Since $g$ is finite, $\varphi(C)$ is a point exactly when $\varphi'(C)$ is a point. So $D \cdot C \geq 0$ always, with equality exactly for the contracted curves. (4) By part 2 and part 2 of Proposition P5.11.3, $\kappa(D) = \kappa(mD)$ is computed by $h^0(Z, jA)$. If $\dim Z = 0$, then $Z$ is a point, since $Z$ is connected and normal, so $h^0(jA) = 1$ for all $j$ and $\kappa(D) = 0$. If $\dim Z \geq 1$, choose $c$ with $cA$ very ample, embedding $Z$ in a projective space with homogeneous coordinate ring $T$. Then $h^0(Z, jcA) \geq \dim_k T_j$, and $\dim_k T_j$ is the Hilbert polynomial of $Z$ for $j$ large, of degree $\dim Z$ with positive leading coefficient (Har77, Theorem I.7.5). So $h^0(jcmD) \geq c' j^{\dim Z}$ for large $j$, and $\kappa(D) \geq \dim Z$. If $\dim Z = 2$ this gives $\kappa(D) = 2$ by part 1 of Proposition P5.11.3. If $\dim Z = 1$, then $Z$ is a smooth curve and $h^0(Z, jA) \leq j \deg A + 1$ (part 1 of Proposition P5.11.3 on a curve), so $\kappa(D) = 1$. $\square$

*Proof of Theorem 2.5.3.* Suppose $\kappa(S) = -\infty$. By part 1 of Theorem P5.11.26, $S$ is birationally ruled: there are a smooth projective curve $C$ and a birational map $\psi \colon C \times \mathbb{P}^1 \dashrightarrow S$. By Theorem P5.7.9 there is a composite of point blow-ups $\pi \colon W \to C \times \mathbb{P}^1$ such that $p = \psi \circ \pi \colon W \to S$ is a morphism. It is a birational morphism of smooth projective surfaces, so by Theorem P5.7.12 it is a composite of blow-ups of points, and by Lemma P5.11.15, $K_W = p^* K_S + Z_p$ with $Z_p$ effective and supported on the finitely many curves contracted by $p$. The centres of the blow-ups in $\pi$ map to finitely many points of $C \times \mathbb{P}^1$. Choose $c \in C$ such that the fibre $F = \{c\} \times \mathbb{P}^1$ contains none of them, and such that its strict transform $F' \subseteq W$ is not one of the curves contracted by $p$. This excludes finitely many $c$, because the curves $F'$ for different $c$ are distinct. Then $\pi$ is an isomorphism over a neighbourhood of $F$, so $F' \cong \mathbb{P}^1$ and $F'^2 = F^2 = 0$, and adjunction (Theorem P5.5.14) gives $K_W \cdot F' = 2 p_a(F') - 2 - F'^2 = -2$. On the other hand $p(F')$ is a curve, so part 3 of Lemma P5.11.15 gives $p^* K_S \cdot F' = K_S \cdot p(F') \geq 0$ because $K_S$ is nef, and $Z_p \cdot F' \geq 0$ because $F'$ is not a component of $Z_p$. So $K_W \cdot F' \geq 0$, a contradiction. $\square$

*Proof of Theorem 2.5.4.* If $E$ were a $(-1)$-curve, then $K_S \cdot E = -1$ by adjunction, against nefness. So $S$ is minimal, and part 2 of Theorem P5.11.26, applied with $S_0 = S$, gives $K_S \equiv 0$ and $12 K_S \sim 0$. Then $|12 K_S| = |0|$ is free, $h^0(12 n K_S) = 1$ for all $n \geq 0$, and the Veronese subring is generated by a nonzero section $t$ of $\mathcal{O}_S(12K_S) \cong \mathcal{O}_S$. $\square$

*Proof of Theorem 2.5.5.* As in the previous proof $S$ is minimal. Part 3 of Theorem P5.11.26 gives $K_S^2 = 0$, the fibration $f$, the integer $n$ and $D$ with $\deg D > 0$. For $j$ with $j \deg D \geq 2 g(B)$, the system $|jD|$ is free by part 1 of Corollary P5.1.20, so $f^* |jD| \subseteq |jnK_S|$ is free, and $K_S$ is semiample. Since $f_* \mathcal{O}_S = \mathcal{O}_B$, the projection formula gives $H^0(S, jnK_S) = f^* H^0(B, jD)$, so the morphism of $|jnK_S|$ is $f$ followed by the morphism $\varphi_{|jD|}$ of $B$, which is finite. The Stein factorization of this composite is $f$ followed by a finite map, because $f$ has connected fibres and $B$ is normal. So $f$ is the Iitaka fibration. $\square$

*Proof of the equality $\deg L = \chi(\mathcal{O}_S)$ in Theorem 2.5.6.* The fibres of $f$ have dimension $1$, so $R^q f_* \mathcal{O}_S = 0$ for $q \geq 2$, and the Leray spectral sequence gives $\chi(\mathcal{O}_S) = \chi(B, f_* \mathcal{O}_S) - \chi(B, R^1 f_* \mathcal{O}_S) = \chi(\mathcal{O}_B) - \chi(L^\vee)$. Riemann-Roch on $B$ gives $\chi(\mathcal{O}_B) - \chi(L^\vee) = (1 - g) - (-\deg L + 1 - g) = \deg L$. The rest of the theorem is cited. $\square$

*Proof of Lemma 2.5.7.* The question is local on $B$, and $f_* \mathcal{O}_S = \mathcal{O}_B$ away from $b$. Let $t$ be a uniformizer at $b$ and $h$ a rational function on a neighbourhood $U$ of $b$ with $f^* h \in \Gamma(f^{-1} U, \mathcal{O}_S(jF))$, that is $\operatorname{div}(f^* h) + jF \geq 0$ on $f^{-1} U$. Shrinking $U$, $h = u t^e$ with $u$ a unit, and $\operatorname{div}(f^* h) = e \, f^* b = emF$ on $f^{-1} U$. So $em + j \geq 0$, and since $0 \leq j < m$, $e \geq 0$. Hence $h$ is regular at $b$, and $f_* \mathcal{O}_S(jF) = f_* \mathcal{O}_S = \mathcal{O}_B$. $\square$

*Proof of Corollary 2.5.8.* (1) Any two fibres are algebraically equivalent, so $f^* b \equiv F$ for every $b$, $F_i \equiv F / m_i$, and $f^*(K_B + L) \equiv dF$ because $\deg(K_B + L) = 2g(B) - 2 + \chi(\mathcal{O}_S)$ by Theorem 2.5.6. So $K_S \equiv dF + \sum_i (m_i - 1) F / m_i = \delta F$, and $K_S^2 = \delta^2 F^2 = 0$. (2) Write $n(m_i - 1) = q_i m_i + r_i$ with $q_i = \lfloor n(m_i - 1)/m_i \rfloor$ and $0 \leq r_i < m_i$. Since $m_i F_i = f^* b_i$, Theorem 2.5.6 gives
$$nK_S \sim f^* D_n + \sum_i r_i F_i.$$
The fibres $F_i$ are disjoint, so Lemma 2.5.7, applied near each $b_i$, gives $f_* \mathcal{O}_S(\sum_i r_i F_i) = \mathcal{O}_B$. By the projection formula $f_* \mathcal{O}_S(nK_S) \cong \mathcal{O}_B(D_n)$, and $P_n(S) = h^0(B, D_n)$. (3) The divisor $F$ is nef, since $F^2 = 0$ and $F$ moves in a family of disjoint curves. If $\delta \geq 0$, then $K_S \equiv \delta F$ is nef. For $n = M$ every $r_i$ is $0$, because $m_i$ divides $M(m_i - 1)$, so $MK_S \sim f^* D_M$ with $\deg D_M = Md + \sum_i M(m_i - 1)/m_i = M\delta$. If $\delta > 0$, then $|jD_M|$ is free for $j$ large (part 1 of Corollary P5.1.20), so $K_S$ is semiample with semiample fibration $f$, and $\kappa(S) = 1$ by part 4 of Lemma 2.5.2. If $\delta = 0$, then $\kappa(S) \geq 0$ by Theorem 2.5.3, and $K_S \equiv 0$ gives $nK_S \cdot H = 0$ for an ample $H$, so the only possible effective member of $|nK_S|$ is $0$ and $h^0(nK_S) \leq 1$: $\kappa(S) = 0$. If $\delta < 0$, then $nK_S \cdot H = n\delta F \cdot H < 0$ and $h^0(nK_S) = 0$ for all $n \geq 1$, so $\kappa(S) = -\infty$. $\square$

### Exercises

1. (A) Let $D$ be a Cartier divisor on a normal projective variety. Show that $D$ is semiample if and only if $aD$ is semiample for one, and then every, $a \geq 1$. Show that if $|mD|$ is free, then $|jmD|$ is free for every $j \geq 1$.
2. (A) Let $S$ be a K3 surface. Show that $K_S$ is semiample, that its Iitaka fibration is the map to a point, and that $R(S, K_S) \cong k[t]$.
3. (B) Let $f \colon S \to B$ be a relatively minimal elliptic fibration over $\mathbb{C}$ with $g(B) = 1$, $\chi(\mathcal{O}_S) = 0$ and exactly one multiple fibre, of multiplicity $2$. Compute $\delta$, and show that $P_n(S) = \lfloor n/2 \rfloor$ for $n \geq 2$, while $P_1(S) \in \{0, 1\}$ depends on whether $L$ is trivial.
4. (B) In the situation of Lemma 2.5.7, show that $f_* \mathcal{O}_S(mF) = \mathcal{O}_B(b)$. Deduce that $h^0(S, mF) = 2$ when $B = \mathbb{P}^1$, although $h^0(S, jF) = 1$ for $0 \leq j < m$.
5. (B) Let $S$ be a surface with $\kappa(S) \geq 0$ that is not minimal. Show that $K_S$ is not nef, and that the base locus of $|nK_S|$ contains every $(-1)$-curve for every $n \geq 1$.
6. (C) Let $f \colon S \to \mathbb{P}^1$ be a relatively minimal elliptic fibration over $\mathbb{C}$ with $\chi(\mathcal{O}_S) = 1$ and multiple fibres of multiplicities $m_1, \dots, m_r$. Show that $\kappa(S) = 1$ if and only if $\sum_i (1 - 1/m_i) > 1$. For $r = 2$, show that this holds for every pair except $(2, 2)$, and for $(m_1, m_2) = (2, 5)$ find the smallest $n$ with $P_n(S) \geq 2$.

### Lean

`MinimalModel.IsSemiample` is the Lean form of semiampleness, for divisors with real coefficients, in the sense of Definition 1.1.26. The statements of this section are not yet in Lean; they depend on the classification of surfaces, which the Lean project states only in special cases.

### Notes and history

The statement that the canonical class of a minimal surface with $\kappa \geq 0$ is semiample is part of the Enriques-Kodaira classification. Enriques proved the classification of complex surfaces; Kodaira, in his series of papers on compact analytic surfaces (Amer. J. Math. 86 (1964), 751 to 798, and the later parts), gave the modern proof and the canonical bundle formula, and Bombieri and Mumford extended the classification to characteristic $p$ (Mumford, in *Global Analysis*, Princeton 1969, and Bombieri and Mumford, parts II and III, 1977). Beauville (Bea96, Chapters VIII and IX) proves the cases $\kappa = 0$ and $\kappa = 1$ over $\mathbb{C}$, and Reid (Rei97, Chapter 4) gives the shape of the argument. The proof of Theorem 2.5.3 is the standard one: the ruling gives a curve with $K \cdot F' < 0$ on every model, which a nef class cannot have. Iitaka introduced the fibration that bears his name and the Kodaira dimension of a divisor in general. In higher dimension the statement $\kappa \geq 0$ for nef $K_X$ is the case of a nef $K_X$ of the non-vanishing Conjecture 1.1.30, and the abundance Conjecture 1.1.31 asks for semiampleness.
