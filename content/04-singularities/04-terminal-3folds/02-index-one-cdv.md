---
title: The index one cover and cDV points
nodes: []
sources: [KM98, Rei80, Rei83b, Rei87]
reads_with: [KM98:ch5, Rei87:ch3]
requires: [4.1, 4.2, 4.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The index one cover and cDV points

### Statement

The classification of terminal 3-fold singularities has two steps. The first reduces to the case where $K_X$ is Cartier, by the index one cover. The second classifies that case: the terminal 3-fold points with $K_X$ Cartier are the isolated compound Du Val points. Throughout, a *germ* $(X, P)$ is a normal variety with a point, and the statements are local at $P$. The classes of Chapter 2 are local, by Corollary 4.1.15, and they depend only on the analytic germ, since a log resolution of the germ computes them by Theorem 4.2.14. As in KM98, Chapter 5, and Rei87, the section uses analytic isomorphisms of germs freely.

**Definition 4.4.13 (index and index one cover).** Let $(X, P)$ be a germ with $K_X$ $\mathbb{Q}$-Cartier. The *index* of $X$ at $P$ is the least $r \ge 1$ with $r K_X$ Cartier at $P$. Choose a neighbourhood of $P$ on which $\mathcal{O}_X(rK_X)$ has a generator $s$. The *index one cover* is
$$\pi \colon \tilde X = \operatorname{Spec}_X \bigoplus_{i=0}^{r-1} \mathcal{O}_X(-iK_X) \to X,$$
where $\mathcal{O}_X(-iK_X)$ is the reflexive sheaf of the Weil divisor $-iK_X$, and the multiplication uses the isomorphism $\mathcal{O}_X(-rK_X) \cong \mathcal{O}_X$ given by $s$. The group $\mu_r$ acts on $\tilde X$ with weight $i$ on the summand $\mathcal{O}_X(-iK_X)$. This is the construction of Section 3.3, in any dimension.

**Proposition 4.4.14 (the index one cover).** In Definition 4.4.13:

1. $\tilde X$ is normal, $\pi$ is finite of degree $r$, $X = \tilde X / \mu_r$, and $\pi^{-1}(P)$ is one point $\tilde P$.
2. $\pi$ is étale over the open set where $K_X$ is Cartier. In particular $\pi$ is étale in codimension 1.
3. $K_{\tilde X} = \pi^* K_X$, and $K_{\tilde X}$ is Cartier.
4. If $X$ is terminal, then $\tilde X$ is terminal. If $X$ is canonical, then $\tilde X$ is canonical. $X$ is klt if and only if $\tilde X$ is klt.

Lean: not yet in Lean.

Parts 1 to 3 are KM98, Chapter 5, where the index one cover is constructed and studied. Up to isomorphism, $\tilde X$ does not depend on the choice of $s$ near $P$, since two choices differ by a unit, which has an $r$-th root in the analytic local ring.

**Theorem 4.4.15 (terminal 3-folds have isolated singularities).** Let $X$ be terminal. Then the singular locus of $X$ has codimension at least 3. In particular a terminal 3-fold has isolated singular points.

Lean: not yet in Lean.

This is KM98, Chapter 5, where it is proved for terminal pairs in every dimension.

**Definition 4.4.16 (compound Du Val point).** A point $P$ of a 3-fold $X$ is a *compound Du Val point*, or *cDV point*, if there is an analytic isomorphism of germs
$$(X, P) \cong \big( \{ f(x, y, z) + t \, g(x, y, z, t) = 0 \}, 0 \big) \subset (\mathbb{C}^4, 0),$$
where $f(x, y, z) = 0$ is a Du Val singularity of a surface (Theorem 4.3.13). Equivalently, $X$ is a hypersurface near $P$, and some hyperplane section $H = \{t = 0\}$ through $P$ is a Du Val surface. The point is of type $cA_n$, $cD_n$ or $cE_n$ when a general hyperplane section through $P$ is of type $A_n$, $D_n$ or $E_n$. A smooth point is a cDV point, with $g(0) \ne 0$.

**Theorem 4.4.17 (Reid).** Let $(X, P)$ be a 3-fold germ. Then $X$ is terminal at $P$ and $K_X$ is Cartier at $P$ if and only if $P$ is an isolated cDV point.

Lean: not yet in Lean.

This is Rei83b, Theorem (1.1); KM98, Section 5.3, gives a proof. The theorem builds on Reid's earlier study of canonical 3-fold points of index 1 (Rei80), where he shows that a general hyperplane section through such a point is a Du Val singularity or an elliptic singularity.

**Corollary 4.4.18 (the structure of a terminal point).** Let $(X, P)$ be a terminal 3-fold germ of index $r$, and $\pi \colon (\tilde X, \tilde P) \to (X, P)$ its index one cover. Then $(\tilde X, \tilde P)$ is an isolated cDV point, possibly smooth, and $\mu_r$ acts freely on $\tilde X \setminus \tilde P$. If $\tilde X$ is smooth at $\tilde P$, then $X \cong \frac1r(1, -1, a)$ analytically, with $\gcd(a, r) = 1$.

Lean: not yet in Lean.

### Proof in words

The index one cover takes an $r$-th root of a generator of $\mathcal{O}(rK_X)$. Where $K_X$ is already Cartier, this root exists on $X$, and the cover splits into $r$ sheets. So the cover is étale in codimension 1, its canonical divisor is the pullback of $K_X$, and the formula $A' = eA$ of Section 2.4 says that the classes go up. The singular locus of a terminal variety has codimension at least 3: a general surface section through a general point of a codimension 2 component would be a singular terminal surface.

For Reid's theorem, the easy direction uses a Du Val section $H$ through $P$. The pair $(X, H)$ is plt by inversion of adjunction, so every divisor $E$ over $P$ has $a(E, X, H) > -1$. Since $K_X + H$ is Cartier, this discrepancy is an integer, so it is at least 0, and adding back $H$, which vanishes along $E$, gives $a(E, X) \ge 1$. The hard direction starts from a terminal point of index 1, which is canonical. Reid's analysis of the general hyperplane section shows that it is Du Val or elliptic, and that in the elliptic case some divisor over $P$ has discrepancy 0, which is not allowed. So the section is Du Val, and the point is cDV. Putting the two steps together, every terminal point is a cyclic quotient of an isolated cDV point by an action that is free outside the point.

### Examples

**Example 4.4.19 (the point $xy + z^2 + t^3 = 0$ of type $cA_1$).** Let $X = \{ xy + z^2 + t^3 = 0 \} \subset \mathbb{A}^4$. The partial derivatives are $y$, $x$, $2z$ and $3t^2$, which vanish together only at the origin, so the origin $P$ is an isolated singular point. The section $t = 0$ is $\{xy + z^2 = 0\}$, the $A_1$ singularity. A general hyperplane through $P$ is $t = \lambda x + \mu y + \nu z$, and the section is $xy + z^2 + (\lambda x + \mu y + \nu z)^3 = 0$, whose quadratic part $xy + z^2$ still has rank 3, so it is again an $A_1$ singularity. So $P$ is a cDV point of type $cA_1$, and by Theorem 4.4.17 it is terminal of index 1. The rest of the example checks this directly by a log resolution.

*The blow-up of $P$.* Let $g \colon B \to \mathbb{A}^4$ be the blow-up of the origin, with exceptional divisor $E_0 \cong \mathbb{P}^3$, and let $X' \subset B$ be the strict transform of $X$, with $f \colon X' \to X$. The four charts are:

- in the chart $x = x' t$, $y = y' t$, $z = z' t$, the equation is $t^2(x'y' + z'^2) + t^3 = 0$, and $X'$ is $\{x'y' + z'^2 + t = 0\}$, which is smooth, since it is the graph of $t = -(x'y' + z'^2)$;
- in the chart $y = y' x$, $z = z' x$, $t = t' x$, the equation is $x^2(y' + z'^2) + x^3 t'^3 = 0$, and $X'$ is $\{y' + z'^2 + x t'^3 = 0\}$, which is smooth, since it is linear in $y'$;
- the chart of $y$ is the same, with $x$ and $y$ exchanged;
- in the chart $x = x' z$, $y = y' z$, $t = t' z$, the equation is $z^2(x'y' + 1) + z^3 t'^3 = 0$, and $X'$ is $\{x'y' + 1 + z t'^3 = 0\}$, whose gradient $(y', x', t'^3, 3 z t'^2)$ vanishes only where $x' = y' = 0$ and $t' = 0$, which is not on $X'$.

So $X'$ is smooth. The exceptional divisor $E = E_0 \cap X'$ is the projectivized tangent cone $\{xy + z^2 = 0\} \subset \mathbb{P}^3$, a quadric cone, which is reduced, with vertex $p = [0 : 0 : 0 : 1]$. The point $P$ has multiplicity 2 on $X$, so $g^* X = X' + 2 E_0$. With $K_B = g^* K_{\mathbb{A}^4} + 3 E_0$, adjunction gives
$$K_{X'} = (K_B + X')|_{X'} = \big( g^*(K_{\mathbb{A}^4} + X) + (3 - 2) E_0 \big)|_{X'} = f^* K_X + E,$$
so $a(E, X) = 1$.

*The second blow-up.* The divisor $E$ is singular at $p$, the origin of the first chart, where $X'$ has coordinates $x', y', z'$ and $E = \{t = 0\} = \{x'y' + z'^2 = 0\}$, an $A_1$ singularity of the surface $E$. Let $h \colon X'' \to X'$ be the blow-up of the smooth point $p$, with exceptional divisor $G \cong \mathbb{P}^2$. Then $K_{X''} = h^* K_{X'} + 2G$, and $h^* E = E'' + 2G$, since $E$ has multiplicity 2 at $p$. So
$$K_{X''} = (fh)^* K_X + h^* E + 2G = (fh)^* K_X + E'' + 4G,$$
and $a(G, X) = 4$. In the chart $x' = \alpha z'$, $y' = \beta z'$ of the second blow-up, $G = \{z' = 0\}$ and $E'' = \{\alpha \beta + 1 = 0\}$, and in the chart $y' = \beta x'$, $z' = \gamma x'$, $G = \{x' = 0\}$ and $E'' = \{\beta + \gamma^2 = 0\}$. The third chart is symmetric to the second. In each chart $E''$ and $G$ are smooth and meet transversally, along the conic $\{x'y' + z'^2 = 0\} \subset G$. So $fh$ is a log resolution of $X$, with crepant pullback $\Delta_{X''} = -E'' - 4G$.

*The discrepancy.* By Theorem 4.2.14 and Theorem 4.2.12,
$$\operatorname{discrep}(X) = \min\Big\{ 1, 4, \ \min\{ 1, \ 1 + 1, \ 1 + 4, \ 1 + 1 + 4 \} \Big\} = 1.$$
So $X$ is terminal, with $\operatorname{discrep}(X) = 1$, and the value 1 is attained by $E$.

**Example 4.4.20 (the ordinary double point).** Let $X = \{xy + zt = 0\}$. The singular point is isolated, and the section $t = z$ is $\{xy + z^2 = 0\}$, the $A_1$ singularity. So $X$ is of type $cA_1$, and Theorem 4.4.17 says that it is terminal. This agrees with Counterexample 4.2.26, where $X$ is the cone over $\mathbb{P}^1 \times \mathbb{P}^1$ by $\mathcal{O}(1,1)$ and the blow-up of the vertex has $a = 1$, and with Volume 3, Example 3.3.39, where the star subdivision at $(1,1,2)$ has $a = 1$. The two computations are the same: the star subdivision at $(1,1,2)$ is the blow-up of the vertex.

**Example 4.4.21 (a cDV point that is not isolated).** Let $X = \{xy + z^2 = 0\} \subset \mathbb{A}^4$, the product $S \times \mathbb{A}^1$ of the $A_1$ surface $S$ with a line. The section $t = 0$ is $S$, so every point of the $t$-axis is a cDV point, but none is isolated. Let $\tilde S \to S$ be the minimal resolution, with exceptional curve $C$, a $(-2)$-curve. The resolution is crepant, so $K_{\tilde S}$ is the pullback of $K_S$ (Theorem 4.3.11). Then $f \colon Y = \tilde S \times \mathbb{A}^1 \to X$ is a log resolution with one exceptional divisor $E = C \times \mathbb{A}^1$, and $K_Y = f^* K_X$. So $a(E, X) = 0$, and by Theorem 4.2.14, $\operatorname{discrep}(X) = \min\{0, 1\} = 0$. The point is canonical and not terminal, as Theorem 4.4.15 predicts, and the word "isolated" in Theorem 4.4.17 is needed.

**Example 4.4.22 (the cone over a cubic surface).** Let $X = \{x^3 + y^3 + z^3 + t^3 = 0\}$, the cone over the smooth cubic surface $V \subset \mathbb{P}^3$ by $L = \mathcal{O}_V(1)$. The singular point is isolated, and $K_X$ is Cartier. Since $K_V = \mathcal{O}_V(-1) = -L$, Theorem 4.2.19 gives $r = -1$ and $a = -1 - r = 0$ for the exceptional divisor $E \cong V$ of the blow-up of the vertex. So $X$ is canonical and not terminal. Theorem 4.4.17 agrees: the point has multiplicity 3, so every hyperplane section through it has multiplicity at least 3, and the Du Val singularities have multiplicity 2 (Theorem 4.3.13), so $X$ is not cDV. A general hyperplane section is the cone over a smooth plane cubic, an elliptic singularity, which is the case excluded in the proof of the hard direction.

**Example 4.4.23 (index one covers of cyclic quotients).** Let $X = \frac1r(a_1, a_2, a_3)$ with a faithful action and no pseudo-reflections, and let $H \subset \mu_r$ be the subgroup of the $\zeta^k$ with $k(a_1 + a_2 + a_3) \equiv 0 \pmod r$, the kernel of the character by which $\mu_r$ acts on $\omega = dx_1 \wedge dx_2 \wedge dx_3$. Then $\mathbb{A}^3 / H \to X$ is a cyclic cover of degree $[\mu_r : H] = r / \gcd(r, a_1 + a_2 + a_3)$, which is the index by Theorem 4.4.4. It is étale in codimension 1, since $\mu_r$ has no pseudo-reflections, and $\omega$ descends to a generator of the canonical sheaf of $\mathbb{A}^3 / H$, so $\mathbb{A}^3 / H$ has $K$ Cartier. This is the index one cover of $X$ (KM98, Chapter 5). For example:

- for $\frac1r(1, -1, a)$ with $\gcd(a, r) = 1$, $H = 1$ and the index one cover is $\mathbb{A}^3$, smooth, as Corollary 4.4.18 requires;
- for $\frac12(1,1,1)$, the index one cover is $\mathbb{A}^3$, of degree 2;
- for $\frac17(1,2,4)$, $H = \mu_7$, the index is 1, and the index one cover is $X$ itself. The point is canonical of index 1 and not terminal, so by Theorem 4.4.17 it is not cDV.

### Proof

*Proof of Proposition 4.4.14.* Parts 1 to 3 are KM98, Chapter 5. For part 2 in a sentence: on an open set $U$ where $K_X$ is Cartier, choose a generator $\omega$ of $\mathcal{O}_U(K_X)$, so that $s = u \omega^{\otimes r}$ with $u$ a unit. The algebra $\bigoplus_i \mathcal{O}_U(-iK_X)$ is then $\mathcal{O}_U[T]/(T^r - u)$, which is étale over $U$, since $u$ is a unit and $r$ is invertible. Normal varieties are regular in codimension 1, so $K_X$ is Cartier in codimension 1, and $\pi$ is étale in codimension 1. For part 4, the Hurwitz formula of Lemma 4.2.28 gives $K_{\tilde X} = \pi^* K_X + R$ with $R = 0$, since $\pi$ is étale in codimension 1. So the sub-pair $(\tilde X, \Delta')$ of Theorem 4.2.29 is $(\tilde X, 0)$, and part 3 and part 4 of that theorem give the claims. $\square$

*Proof of Theorem 4.4.15 (a sketch).* Let $n = \dim X$, and suppose that the singular locus has a component $Z$ of codimension 2. Take a log resolution $f \colon Y \to X$, and $n - 2$ general hyperplane sections $H_1, \dots, H_{n-2}$ through a general point $z$ of $Z$. Near $z$, the surface $S = H_1 \cap \dots \cap H_{n-2}$ is normal, and its strict transform $S_Y$ is a resolution of $S$ whose exceptional curves are the intersections of $S_Y$ with the exceptional divisors of $f$ that dominate $Z$. By adjunction, $K_{S_Y} = (K_Y + \sum_i (H_i)_Y)|_{S_Y}$ and $K_S = (K_X + \sum_i H_i)|_S$, and for general $H_i$ the pullback of $H_i$ is its strict transform near the general point of $f^{-1}(z)$. So the discrepancy of each exceptional curve of $S_Y$ over $S$ is the discrepancy of the divisor of $Y$ that contains it, which is positive. So $S$ is terminal at $z$. The surface $S$ is singular at $z$, since a Cartier divisor that is smooth at a point forces the ambient variety to be smooth there. This contradicts Proposition 4.4.1. The details of the Bertini argument are in KM98, Chapter 5. $\square$

*Proof of Theorem 4.4.17, the direction from cDV to terminal.* Let $P$ be an isolated cDV point, and $H = \{h = 0\}$ a hyperplane section through $P$ that is a Du Val surface, with $h$ a local function. The point is a hypersurface point, so $K_X$ is Cartier, and $H$ is a Cartier divisor. By Theorem 4.3.11, $H$ is canonical, so it is klt. By inversion of adjunction (KM98, Theorem 5.50), the pair $(X, H)$ is plt near $P$. Let $f \colon Y \to X$ be a resolution, and $E$ an exceptional divisor of $f$.

Suppose first that the centre of $E$ is $P$. Write $f^* H = H_Y + \sum_F v_F(h) F$, where $H_Y$ is the strict transform and $F$ runs over the exceptional divisors. Comparing
$$K_Y + H_Y = f^*(K_X + H) + \sum_F a(F, X, H) F, \qquad K_Y = f^* K_X + \sum_F a(F, X) F$$
gives $a(E, X, H) = a(E, X) - v_E(h)$. Since $K_X + H$ is Cartier, $K_Y + H_Y - f^*(K_X + H)$ is an integral divisor, so $a(E, X, H)$ is an integer. It is greater than $-1$ because the pair is plt, so it is at least 0. The centre of $E$ lies in $H$, so $v_E(h) \ge 1$, and
$$a(E, X) = a(E, X, H) + v_E(h) \ge 1.$$

Suppose next that the centre of $E$ is not $P$. Then the centre meets $X \setminus P$, which is smooth since $P$ is an isolated singular point. By Corollary 4.1.15 the discrepancy $a(E, X)$ is computed on $X \setminus P$, and on a smooth variety every exceptional divisor has discrepancy at least 1, by Theorem 4.2.12 with $\Delta = 0$. In both cases $a(E, X) \ge 1 > 0$, so $X$ is terminal at $P$, and $K_X$ is Cartier. $\square$

*Proof of Theorem 4.4.17, the direction from terminal to cDV (a sketch).* Let $X$ be terminal at $P$ with $K_X$ Cartier. By Theorem 4.4.15 the point is isolated. A terminal point is canonical, and Reid (Rei80) proves that a general hyperplane section $H$ through a canonical 3-fold point of index 1 is either a Du Val singularity or an elliptic Gorenstein singularity, a normal Gorenstein surface singularity of geometric genus 1. In the elliptic case Reid constructs, by a sequence of blow-ups adapted to $H$, an exceptional divisor $E$ over $P$ with $a(E, X) = 0$ (Rei80). This contradicts terminality. So $H$ is Du Val, and $P$ is a cDV point. KM98, Section 5.3, gives a proof along the same lines. $\square$

*Proof of Corollary 4.4.18.* By Proposition 4.4.14, $\tilde X$ is terminal and $K_{\tilde X}$ is Cartier, so by Theorem 4.4.17 the point $\tilde P$ is an isolated cDV point. By Theorem 4.4.15, $X \setminus P$ is smooth near $P$, so $K_X$ is Cartier there, and $\pi$ is étale over $X \setminus P$ by Proposition 4.4.14, part 2. So $\mu_r$ acts freely on $\pi^{-1}(X \setminus P) = \tilde X \setminus \tilde P$. If $\tilde X$ is smooth at $\tilde P$, then $(\tilde X, \tilde P) \cong (\mathbb{C}^3, 0)$, and by Cartan's lemma the action of $\mu_r$ is linear in suitable analytic coordinates, and then diagonal. So $X \cong \frac1r(a_1, a_2, a_3)$. The action is faithful, since $\pi$ has degree $r$, and free outside the origin, so it has no pseudo-reflections. By Theorem 4.4.6, $X \cong \frac1r(1, -1, a)$ with $\gcd(a, r) = 1$. $\square$

### Exercises

1. (A) Show that $X = \{xy + z^3 + t^3 = 0\}$ has an isolated singular point, and that the section $t = 0$ is an $A_2$ singularity. Deduce from Theorem 4.4.17 that $X$ is terminal.
2. (A) Show that $x^2 + y^2 + z^2 + t^2 = 0$ is the ordinary double point of Example 4.4.20 after a linear change of coordinates, and that its type is $cA_1$.
3. (B) In Example 4.4.19, let $H = \{t = 0\}$. Show that $v_E(t) = 1$ and $v_G(t) = 2$, so that $a(E, X, H) = 0$ and $a(G, X, H) = 2$. Check that these values are consistent with the proof of the direction from cDV to terminal.
4. (B) Use the equations of Theorem 4.3.13 to show that every Du Val singularity has multiplicity 2. Deduce that an isolated hypersurface singularity of a 3-fold with multiplicity at least 3 is never terminal.
5. (B) Let $X = \frac19(1,2,3)$. Show that the action has no pseudo-reflections, that the index is 3, and that the index one cover of Example 4.4.23 is $\frac13(1,2,0) \cong A_2 \times \mathbb{A}^1$. Deduce from Proposition 4.4.14 and Example 4.4.21 that $X$ is not terminal, and check this by the fractional part criterion, with $S(3) = 1$.
6. (C) Let $X = \{x^3 + y^3 + z^3 + t^3 = 0\}$. Show that a general hyperplane section through the origin is the cone over a smooth plane cubic curve, and that the blow-up of its vertex has an elliptic exceptional curve with discrepancy $-1$, by Theorem 4.2.19. Explain how this matches the elliptic case in the proof of the hard direction of Theorem 4.4.17.

### Lean

The results of this section are not yet in Lean. The definitions of terminal and canonical exist, as `MinimalModel.IsTerminal` and `MinimalModel.IsCanonical`, but the library has no index of a $\mathbb{Q}$-Cartier divisor, no cyclic covers, no analytic germs and no inversion of adjunction. The first statements that could be formalized are the integrality step of the proof of Theorem 4.4.17 and the computation of Example 4.4.19 on its explicit log resolution.

### Notes and history

The cDV points were introduced by Reid (Rei80), who showed that they are canonical, and the terminal singularities by Reid (Rei83b), who proved Theorem 4.4.17 and the reduction of the terminal case to the cDV case by the index one cover. The index one cover appears in Reid's papers (Rei80; Rei87), and KM98, Chapter 5, treats it in every dimension. The proof of the easy direction by inversion of adjunction is a later simplification, and KM98, Chapter 5, gives both directions. Chapter 5 of this volume treats adjunction and its inversion. The cDV points of type $cA$ are the simplest: Example 4.4.19 is the first case of the family $xy + z^2 + t^k$ of Problem 5, all of type $cA_1$.
