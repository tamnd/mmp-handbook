---
title: Elliptic curves and the group law
nodes: []
sources: [Har77, Sil09, Vak25]
reads_with: [Har77:IV.4, Sil09:III]
requires: [P3.10, P4.5, P4.6, P5.1, P5.2, P5.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Elliptic curves and the group law

### Statement

In this section $k$ is algebraically closed.

**Definition P5.4.1 (elliptic curve).** An *elliptic curve* is a pair $(E, O)$ of a smooth projective curve $E$ of genus $1$ and a point $O \in E$. By Proposition P5.1.13 the map $P \mapsto [P - O]$ is a bijection $E \to \operatorname{Pic}^0(E)$, and the group structure transported from $\operatorname{Pic}^0(E)$ is the *group law* of $(E, O)$. So $P + Q = R$ if and only if $P + Q \sim R + O$.

**Theorem P5.4.2 (Weierstrass form).** Let $(E, O)$ be an elliptic curve. There are functions $x, y \in K(E)$ with poles only at $O$, of orders $2$ and $3$, such that $[x : y : 1]$ is the embedding of $E$ by $|3O|$ onto a plane cubic
$$y^2 + a_1 xy + a_3 y = x^3 + a_2 x^2 + a_4 x + a_6, \tag{W}$$
with $O = [0 : 1 : 0]$ a flex whose tangent is the line at infinity. If $\operatorname{char} k \neq 2, 3$, the coordinates can be chosen so that the equation is $y^2 = x^3 + ax + b$, and a cubic of this form is smooth if and only if $\Delta = 4a^3 + 27b^2 \neq 0$. Conversely, every smooth cubic (W) with $O = [0:1:0]$ is an elliptic curve.

Lean: Mathlib `WeierstrassCurve`, `WeierstrassCurve.Δ`, `WeierstrassCurve.IsElliptic` and the group law `WeierstrassCurve.Affine.Point.instAddCommGroup` on the points of a Weierstrass curve (definitions and proved in Mathlib). The equivalence with curves of genus $1$ is not in Lean as stated.

**Lemma P5.4.3 (families of divisors of degree one).** Let $S$ be an integral variety, $g_1, \dots, g_r \colon S \to E$ morphisms with graphs $\Gamma_i \subseteq E \times S$, and $n_1, \dots, n_r$ integers with $\sum n_i = 1$. Then there is a morphism $h \colon S \to E$ such that $h(s) \sim \sum_i n_i g_i(s)$ as divisors on $E$, for every closed point $s \in S$.

Lean: not in Lean as stated.

**Theorem P5.4.4 (the group law is a morphism).** The maps $m \colon E \times E \to E$, $(P, Q) \mapsto P + Q$, and $i \colon E \to E$, $P \mapsto -P$, are morphisms. For each $Q$, translation $\tau_Q \colon P \mapsto P + Q$ is an automorphism of $E$, so the automorphism group of $E$ acts transitively. If $E$ is a plane cubic in Weierstrass form, then $P + Q + R = 0$ if and only if $P, Q, R$ are the three intersections, with multiplicity, of $E$ with a line.

Lean: not in Lean as stated for curves of genus $1$; Mathlib proves the group law on the points of a Weierstrass curve.

**Theorem P5.4.5 (the $j$-invariant).** Let $\operatorname{char} k \neq 2, 3$. For $E \colon y^2 = x^3 + ax + b$ with $\Delta \neq 0$ set
$$j(E) = 1728 \cdot \frac{4a^3}{4a^3 + 27b^2}.$$

1. Two such curves $E, E'$ are isomorphic as elliptic curves if and only if $(a', b') = (u^4 a, u^6 b)$ for some $u \in k^*$, if and only if $j(E) = j(E')$.
2. Two curves of genus $1$ are isomorphic if and only if they have the same $j$-invariant, for any choice of base points.
3. Every $j \in k$ is the $j$-invariant of an elliptic curve.

Lean: Mathlib `WeierstrassCurve.j` and the invariance of $j$ under changes of variables, `WeierstrassCurve.variableChange_j` (definitions and proved in Mathlib). The classification statement is not in Lean as stated.

### Proof in words

Riemann-Roch gives $\ell(nO) = n$ for $n \geq 1$, so there are functions with poles of each order $n \geq 2$ at $O$ and nowhere else. The seven functions $1, x, y, x^2, xy, y^2, x^3$ lie in the six-dimensional space $L(6O)$, and the relation among them is the Weierstrass equation. The group law is algebraic because the point $h(s)$ linearly equivalent to a family of divisors of degree $1$ is the zero of the unique section of a line bundle on each fibre. Cohomology and base change makes this section vary algebraically with $s$. An isomorphism of Weierstrass curves preserving $O$ preserves the spaces $L(2O)$ and $L(3O)$, so it changes $x$ and $y$ by an affine substitution, and the short Weierstrass form leaves only the scaling $x \mapsto u^2 x$, $y \mapsto u^3 y$. The $j$-invariant is the invariant of this scaling.

### Examples

**Example P5.4.6 (Legendre form).** Let $\operatorname{char} k \neq 2$. Every elliptic curve is isomorphic to $E_\lambda \colon y^2 = x(x - 1)(x - \lambda)$ for some $\lambda \neq 0, 1$: move the three roots of the cubic in $x$ to $0, 1, \lambda$ by an affine change of $x$, and rescale $y$. In characteristic $\neq 2, 3$ one computes
$$j(E_\lambda) = 256 \frac{(\lambda^2 - \lambda + 1)^3}{\lambda^2 (\lambda - 1)^2}.$$
The six values $\lambda, 1/\lambda, 1 - \lambda, 1/(1 - \lambda), \lambda/(\lambda - 1), (\lambda - 1)/\lambda$, obtained by permuting $0, 1, \infty$, give the same curve, and the map $\lambda \mapsto j$ has degree $6$.

**Example P5.4.7 (the points of order $2$ and $3$).** Let $E \colon y^2 = f(x)$ with $\operatorname{char} k \neq 2$. A point $P \neq O$ has $2P = 0$ if and only if $2P \sim 2O$, if and only if $x - x(P)$ has a double zero at $P$, if and only if $y(P) = 0$. So $E[2] = \{ O, (e_1, 0), (e_2, 0), (e_3, 0) \} \cong (\mathbb{Z}/2)^2$ for the roots $e_i$ of $f$. Similarly $3P = 0$ if and only if $3P \sim 3O$, which is the divisor of a line, if and only if the tangent at $P$ meets $E$ only at $P$: the points of order dividing $3$ are the nine flexes of $E$ in characteristic $\neq 3$, by the Hessian count of Exercise 4.

**Example P5.4.8 (curves with extra automorphisms).** By part 1 of Theorem P5.4.5, the automorphisms of $(E, O)$ are the $u$ with $u^4 a = a$ and $u^6 b = b$. If $ab \neq 0$, this is $u = \pm 1$, the automorphisms $\pm 1$. For $j = 1728$, $E \colon y^2 = x^3 - x$, it is the group $\mu_4$, with $u = i$ acting by $(x, y) \mapsto (-x, iy)$. For $j = 0$, $E \colon y^2 = x^3 - 1$, it is $\mu_6$.

**Example P5.4.9 (the surface $E \times E$).** The group law gives curves on $S = E \times E$: the fibres of the projections, the diagonal $\Delta$, the antidiagonal $\{ (P, -P) \}$, the fibres of $m$, and for each $n$ the graph of multiplication by $n$. The map $(P, Q) \mapsto (P, P + Q)$ is an automorphism of $S$ that moves the fibre $E \times \{O\}$ to the diagonal. So all these curves are images of each other under automorphisms of $S$, or under the endomorphisms of $E$ of Example P5.4.8. Chapter 5 computes their intersection numbers. For instance $\Delta^2 = 0$, since $\Delta$ is the image of a fibre under an automorphism, while the graph $\Gamma_n$ of multiplication by $n$ meets $\Delta$ in the points with $(n - 1)P = 0$. Example P5.5.19 computes $\Gamma^2$ for the graph of any endomorphism, and Section 5.3 uses the graph of the Frobenius on $E \times E$ to prove Hasse's bound (Example P5.5.27).

### Proof

*Theorem P5.4.2.* By Theorem P5.1.10 and $K \sim 0$, $\ell(nO) = n$ for $n \geq 1$, and $L(O) = k$. So $L(2O) = \langle 1, x \rangle$ with $v_O(x) = -2$, and $L(3O) = \langle 1, x, y \rangle$ with $v_O(y) = -3$. The functions $1, x, y, x^2, xy, y^2, x^3$ lie in $L(6O)$, which has dimension $6$, so they satisfy a linear relation. In it, $y^2$ and $x^3$ are the only terms with a pole of order $6$, and all other terms have distinct pole orders less than $6$. So both coefficients are nonzero, and after scaling $x$ and $y$ the relation has the form (W).

By Proposition P5.1.13, part 3, $|3O|$ embeds $E$ as a plane cubic, and $[x : y : 1]$ is this embedding, since $1, x, y$ is a basis of $L(3O)$. Its image satisfies the cubic (W), which is irreducible because the image is a curve of degree $3$, so the image is $V(\text{W})$. The point $O$ maps to $[0 : 1 : 0]$, the point where $x/y$ and $1/y$ vanish, and the line at infinity $z = 0$ pulls back to the divisor $3O$, so it meets $E$ only at $O$, with multiplicity $3$: $O$ is a flex.

If $\operatorname{char} k \neq 2$, replacing $y$ by $y + (a_1 x + a_3)/2$ removes the terms $xy$ and $y$. If also $\operatorname{char} k \neq 3$, replacing $x$ by $x - a_2/3$ removes $x^2$, giving $y^2 = x^3 + ax + b$. The partial derivatives of $y^2 - f(x)$ are $2y$ and $-f'(x)$. So an affine singular point is a point $(e, 0)$ with $f(e) = f'(e) = 0$, which exists if and only if $f$ has a repeated root, if and only if the discriminant $-(4a^3 + 27b^2)$ of $f$ vanishes. At $[0 : 1 : 0]$, in the chart $y = 1$, the equation is $z = x^3 + a x z^2 + b z^3$, which is smooth. Conversely, a smooth plane cubic has genus $1$ by Example P4.7.23.

*Lemma P5.4.3.* Let $\pi \colon X = E \times S \to S$ be the projection. The diagonal $\Delta_E \subseteq E \times E$ is a smooth curve on a smooth surface, so it is an effective Cartier divisor, and $\Gamma_i = (\mathrm{id} \times g_i)^{-1}(\Delta_E)$. Its local equation pulls back to a function on the integral scheme $X$ that is not identically zero, so $\Gamma_i$ is an effective Cartier divisor. On the fibre $X_s = E \times \{s\}$, $\Gamma_i$ restricts to $\Delta_E \cap (E \times \{g_i(s)\})$, the reduced point $g_i(s)$, since $\Delta_E$ and the fibre $E \times \{g_i(s)\}$ meet transversally. Let $\mathcal{L} = \mathcal{O}_X(\sum n_i \Gamma_i)$, so $\mathcal{L}|_{X_s} \cong \mathcal{O}_E(D_s)$ with $D_s = \sum_i n_i g_i(s)$ of degree $1$. Then $h^0(\mathcal{L}_s) = 1$ and $h^1(\mathcal{L}_s) = 0$ by Proposition P5.1.13 and Riemann-Roch. The morphism $\pi$ is projective and flat, being a base change of $E \to \operatorname{Spec} k$, and $S$ is reduced. So by Theorem P4.5.16, $\pi_* \mathcal{L}$ is invertible and $\pi_* \mathcal{L} \otimes \kappa(s) \to H^0(X_s, \mathcal{L}_s)$ is an isomorphism for every $s$.

Cover $S$ by open sets $U$ on which $\pi_* \mathcal{L}$ has a generator $\sigma$. As a section of $\mathcal{L}$ on $X_U$, $\sigma$ restricts on each fibre to a nonzero section of $\mathcal{O}_E(D_s)$, whose divisor is a single reduced point $h(s)$, the unique point with $h(s) \sim D_s$. Let $Z \subseteq X_U$ be the zero scheme of $\sigma$. The projection $Z \to U$ is projective with finite fibres, so it is finite by Corollary P4.6.17, and $\pi_* \mathcal{O}_Z$ is coherent with $\pi_* \mathcal{O}_Z \otimes \kappa(s) = \mathcal{O}(Z_s) = \kappa(s)$, since a finite morphism is affine and the fibre $Z_s$ is the reduced point $h(s)$. By Nakayama's lemma the image of $1$ generates $\pi_* \mathcal{O}_Z$ near each point, so $\mathcal{O}_U \to \pi_* \mathcal{O}_Z$ is surjective and $Z \to U$ is a closed immersion. It is surjective on closed points and $U$ is reduced, so $Z \to U$ is an isomorphism. The composite $U \cong Z \hookrightarrow E \times U \to E$ is a morphism sending $s$ to $h(s)$. These morphisms agree on overlaps, since they agree on closed points and $E$ is separated, so they glue to $h$.

*Theorem P5.4.4.* For $m$, apply Lemma P5.4.3 to $S = E \times E$, the two projections and the constant map $O$, with $n = (1, 1, -1)$: then $h(P, Q) \sim P + Q - O$, which is $P + Q$ in the group law. For $i$, apply it to $S = E$, the constant map $O$ with $n = 2$ and the identity with $n = -1$. Translation $\tau_Q$ is the restriction of $m$ to $E \times \{Q\}$, a morphism with inverse $\tau_{-Q}$. For three points of a Weierstrass cubic, $P + Q + R = 0$ means $P + Q + R \sim 3O$. Since $3O$ is cut out by the line at infinity and $|3O|$ is the linear system of lines (Theorem P5.4.2), this holds if and only if $P + Q + R$ is the divisor cut out by a line.

*Theorem P5.4.5.* Part 1. Let $\phi \colon E \to E'$ be an isomorphism with $\phi(O) = O'$. Then $\phi^*$ maps $L(nO')$ onto $L(nO)$ for every $n$, so $\phi^* x' = \alpha x + \beta$ and $\phi^* y' = \gamma y + \delta x + \epsilon$ with $\alpha \gamma \neq 0$. Substituting into $y'^2 = x'^3 + a' x' + b'$ gives a relation among $1, x, y, x^2, xy, y^2, x^3$ in $L(6O)$. After replacing $y^2$ by $x^3 + ax + b$, the functions $1, x, y, x^2, xy, x^3$ have distinct pole orders $0, 2, 3, 4, 5, 6$, so they are linearly independent, and each coefficient of the relation vanishes. The coefficient of $xy$ gives $2 \gamma \delta = 0$, so $\delta = 0$, and then the coefficient of $y$ gives $2 \gamma \epsilon = 0$, so $\epsilon = 0$. The coefficient of $x^2$ gives $3 \alpha^2 \beta = 0$, so $\beta = 0$, using $\operatorname{char} k \neq 2, 3$. The remaining coefficients give $\gamma^2 = \alpha^3$, $\gamma^2 a = \alpha a'$ and $\gamma^2 b = b'$. With $u = \gamma / \alpha$, $\alpha = \gamma^2/\alpha^2 = u^2$ and $\gamma = u^3$, so $a' = u^4 a$ and $b' = u^6 b$. Conversely such $u$ defines the isomorphism $(x, y) \mapsto (u^2 x, u^3 y)$ preserving $O$.

The $j$-invariant is unchanged by $(a, b) \mapsto (u^4 a, u^6 b)$. Conversely let $j(E) = j(E')$, which is equivalent to $a^3 b'^2 = a'^3 b^2$. Then $a = 0$ if and only if $a' = 0$, these being the curves with $j = 0$, and $b = 0$ if and only if $b' = 0$, the curves with $j = 1728$. If $a = a' = 0$, take $u$ with $u^6 = b'/b$, and if $b = b' = 0$, take $u$ with $u^4 = a'/a$. If $a b a' b' \neq 0$, take $u$ with $u^2 = a b' / (a' b)$. Then
$$u^4 a = \frac{a^3 b'^2}{a'^2 b^2} = a', \qquad u^6 b = \frac{a^3 b'^3}{a'^3 b^2} = b',$$
both by $a^3 b'^2 = a'^3 b^2$.

Part 2. If $C$ has genus $1$ and $O, O'$ are two points, the translation $\tau_{O' - O}$ of $(C, O)$ is an automorphism of $C$ carrying $O$ to $O'$, so the isomorphism class of $(C, O)$ does not depend on $O$. Part 3. For $j \neq 0, 1728$ take $a = 3j(1728 - j)$ and $b = 2j(1728 - j)^2$, which satisfy $4a^3 / (4a^3 + 27b^2) = j / 1728$ and $\Delta \neq 0$. For $j = 0$ take $y^2 = x^3 + 1$, and for $j = 1728$ take $y^2 = x^3 + x$.

### Exercises

1. (A) Compute the group law on $y^2 = x^3 + ax + b$ explicitly: for $P = (x_1, y_1)$ and $Q = (x_2, y_2)$ with $x_1 \neq x_2$, show that $x(P + Q) = \lambda^2 - x_1 - x_2$ with $\lambda = (y_2 - y_1)/(x_2 - x_1)$.
2. (A) Verify the formula for $j(E_\lambda)$ in Example P5.4.6, by moving $E_\lambda$ to short Weierstrass form, and show that $j(E_\lambda) = 1728$ for $\lambda = -1$ and $j(E_\lambda) = 0$ for $\lambda^2 - \lambda + 1 = 0$.
3. (B) Show that the cuspidal cubic $y^2 = x^3$ and the nodal cubic $y^2 = x^2(x+1)$ carry group laws on their smooth loci by the same chord rule, isomorphic to the additive group $k$ and the multiplicative group $k^*$.
4. (B) Show that a smooth plane cubic in characteristic $\neq 3$ has exactly nine flexes, by intersecting it with its Hessian curve and showing that each intersection is transversal, and deduce $E[3] \cong (\mathbb{Z}/3)^2$.
5. (B) Let $\operatorname{char} k = p > 2$ and $E \colon y^2 = x^3 + ax + b$. Show that $E[p]$ is either $\mathbb{Z}/p$ or $0$, using Proposition P5.2.10 and the factorization of multiplication by $p$ through the Frobenius, given that multiplication by $p$ has degree $p^2$.
6. (C) Show that every morphism $\phi \colon E \to E'$ of elliptic curves with $\phi(O) = O'$ is a group homomorphism. Apply Theorem P5.4.4 to see that $\psi(P, Q) = \phi(P + Q) - \phi(P) - \phi(Q)$ is a morphism $E \times E \to E'$ mapping $E \times \{O\}$ and $\{O\} \times E$ to $O'$, and prove the rigidity lemma: such a morphism is constant. For the rigidity lemma, take an affine neighbourhood $V$ of $O'$, show that the set of $Q$ with $\psi(E \times \{Q\}) \subseteq V$ is open, and use that a morphism from the projective curve $E$ to the affine $V$ is constant.

### Lean

Mathlib formalizes Weierstrass curves over any commutative ring, their discriminant and $j$-invariant, changes of variables and the group law on their points, with the abelian group structure proved through the identification with the class group of the coordinate ring. It does not formalize the passage from a curve of genus $1$ to its Weierstrass model, or the group law as a morphism of varieties. The handbook adds no `MinimalModel` node here.

### Notes and history

The chord and tangent construction goes back to Newton and Fermat, and the description of elliptic curves as complex tori $\mathbb{C}/\Lambda$ through the Weierstrass $\wp$-function to Weierstrass and Jacobi; the algebraic theory over an arbitrary field is due to Weil. The proof of Lemma P5.4.3 is the simplest case of the representability of the Picard functor. The literature state is theorem. Hasse's bound $|\#E(\mathbb{F}_q) - q - 1| \leq 2 \sqrt{q}$ is proved in Section 5.3 for curves of every genus, as Weil's bound (Theorem P5.5.25). For the rest of the arithmetic of elliptic curves see Silverman, Chapter V. In the minimal model program, a smooth projective variety with $K_X \equiv 0$ is the higher-dimensional analogue of an elliptic curve, and the abelian varieties among them are the ones whose group law makes them homogeneous.
