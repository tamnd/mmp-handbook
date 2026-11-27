---
title: The round cone of E x E
nodes: []
sources: [Laz04, Sil09, Bea96]
reads_with: [Laz04:1.5, Sil09:ch3]
requires: [P5.4, P5.5, P5.8, P5.12]
level: background
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The round cone of E x E

### Statement

Let $E$ be an elliptic curve over $k$ with origin $O$, and $S = E \times E$ (Example P5.4.9). Write $p_1, p_2$ for the projections, $f_1 = \{O\} \times E = p_1^*(O)$ and $f_2 = E \times \{O\} = p_2^*(O)$ for the fibres, and $\Delta$ for the diagonal. The difference map $\delta \colon S \to E$, $(P, Q) \mapsto P - Q$, is a morphism by Theorem P5.4.4, its fibres are the translates of $\Delta$, and $\Delta = \delta^*(O)$. The ring $\operatorname{End}(E)$ of endomorphisms fixing $O$ is $\mathbb{Z}$ or an order in an imaginary quadratic field, since $k$ has characteristic $0$ (Sil09, Corollary III.9.4). In the second case $E$ has *complex multiplication*.

**Theorem 1.3.24 (the Picard number of $E \times E$).** $\rho(S) = 2 + \operatorname{rank}_{\mathbb{Z}} \operatorname{End}(E)$. So $\rho(S) = 3$ if $E$ has no complex multiplication, and $\rho(S) = 4$ if it has.

Lean: not yet in Lean.

For every elliptic curve $E$, the classes $f_1$, $f_2$, $\Delta$ have the Gram matrix
$$\begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}$$
of determinant $2$ (Example P5.12.9), so they are linearly independent in $N^1(S)$. When $\rho(S) = 3$ they are a basis, and every class can be written uniquely as
$$x = (s - c) f_1 + (t - c) f_2 + c \Delta, \qquad s = x \cdot f_2, \quad t = x \cdot f_1, \quad c = \tfrac12 (s + t - x \cdot \Delta).$$
These are the coordinates $(s, t, c)$ of $x$. In them $f_1 = (1, 0, 0)$, $f_2 = (0, 1, 0)$, $\Delta = (1, 1, 1)$, and a direct expansion with the Gram matrix gives
$$x^2 = 2(st - c^2), \qquad x \cdot x' = st' + s't - 2cc', \qquad x \cdot (f_1 + f_2) = s + t.$$

**Theorem 1.3.25 (the cones of $E \times E$ without complex multiplication).** Let $E$ have no complex multiplication. In the coordinates $(s, t, c)$:

1. $\operatorname{Nef}(S) = \overline{NE}(S) = \operatorname{Psef}(S) = \{ s \ge 0, \ t \ge 0, \ st \ge c^2 \}$. With $\sigma = \frac12(s + t)$ and $\tau = \frac12(s - t)$ this is the circular cone $\sigma \ge \sqrt{\tau^2 + c^2}$.
2. $\operatorname{Amp}(S) = \operatorname{Big}(S) = \{ s > 0, \ t > 0, \ st > c^2 \}$.
3. $\operatorname{vol}(x) = x^2 = 2(st - c^2)$ for $x \in \operatorname{Psef}(S)$, and $\operatorname{vol}(x) = 0$ otherwise.
4. The rational rays on the boundary of $\overline{NE}(S)$ are exactly the rays of the classes $(p^2, q^2, pq)$ for coprime integers $p, q$, and each contains the class of an elliptic curve on $S$. The cone of curves is $NE(S) = \operatorname{Amp}(S) \cup \bigcup_{p, q} \mathbb{R}_{\ge 0} (p^2, q^2, pq)$. It is not closed.

Lean: not yet in Lean.

### Proof in words

The round shape comes from two facts of P5. On an abelian surface every curve can be moved by translations, so every curve has nonnegative square and is nef, and the nef cone, the closed cone of curves and the closed positive cone $\{ x^2 \ge 0, \ x \cdot H \ge 0 \}$ coincide (Example P5.12.9). A form of signature $(1, 2)$ makes this a circular cone in $\mathbb{R}^3$. The theorem on the Picard number, which is quoted, says that without complex multiplication $f_1$, $f_2$, $\Delta$ span $N^1(S)$, so the coordinates $(s, t, c)$ are global.

The volume and the big cone then come from Section 2: a pseudoeffective class is nef, so its volume is its square, and the big cone is the interior. The cone of curves is more delicate than its closure. The images of $E$ under $P \mapsto (qP, pP)$ are curves of square $0$, so they lie on the boundary, and an arithmetic argument shows that every rational boundary ray is one of them. The irrational boundary rays contain no curve, and a class on one of them is positive on every curve without being ample.

### Examples

**Example 1.3.26 (the elliptic curves $C_{p,q}$).** Let $p, q$ be coprime integers and $\varphi = (q, p) \colon E \to S$, $P \mapsto (qP, pP)$. Its kernel is $E[p] \cap E[q] = 0$, and its differential at every point is $(q, p) \ne 0$, so $\varphi$ is a closed immersion and $C_{p,q} = \varphi(E)$ is an elliptic curve on $S$. By the projection formula, $C \cdot g^*(O) = \deg(g \circ \varphi)$ for a morphism $g \colon S \to E$ with $g \circ \varphi$ nonconstant, and $0$ if it is constant. Since $\deg [m] = m^2$ for $m \ne 0$ (Sil09, Corollary III.6.4),
$$C_{p,q} \cdot f_1 = \deg [q] = q^2, \qquad C_{p,q} \cdot f_2 = \deg [p] = p^2, \qquad C_{p,q} \cdot \Delta = \deg [q - p] = (p - q)^2,$$
also in the degenerate cases $q = 0$, $p = 0$ or $p = q$. So the coordinates of $C_{p,q}$ are $(s, t, c) = (p^2, q^2, pq)$, and $C_{p,q}^2 = 2(p^2 q^2 - p^2 q^2) = 0$, as for every elliptic curve on an abelian surface. Particular cases:

1. $(p, q) = (0, 1)$ and $(1, 0)$ give $f_2$ and $f_1$, and $(1, 1)$ gives $\Delta$.
2. $(p, q) = (-1, 1)$ gives the antidiagonal $\{ (P, -P) \}$, with $(s, t, c) = (1, 1, -1)$, that is the class $2f_1 + 2f_2 - \Delta$.
3. $(p, q) = (n, 1)$ gives the graph $\Gamma_n$ of $[n]$, with $(s, t, c) = (n^2, 1, n)$, that is the class $(n^2 - n) f_1 + (1 - n) f_2 + n\Delta$. This agrees with Example P5.5.19: $\Gamma_n \cdot f_1 = 1$, $\Gamma_n \cdot f_2 = \deg [n] = n^2$ and $\Gamma_n^2 = 0$.

**Example 1.3.27 (an irrational boundary ray).** Let $E$ have no complex multiplication, and let $x$ be the class with coordinates $(s, t, c) = (1, 2, \sqrt 2)$, that is
$$x = (1 - \sqrt 2) f_1 + (2 - \sqrt 2) f_2 + \sqrt 2 \, \Delta.$$
Then $x^2 = 2(2 - 2) = 0$ and $s, t > 0$, so $x$ is a nonzero point of the boundary of $\overline{NE}(S)$, and $x$ is not ample. For the curves of Example 1.3.26,
$$x \cdot C_{p,q} = q^2 + 2p^2 - 2\sqrt 2 \, pq = (q - \sqrt 2 \, p)^2 > 0,$$
because $\sqrt 2$ is irrational. By Theorem 1.3.25(4), every other curve $C$ either has its class on a rational boundary ray, so that $[C]$ is a positive multiple of some $[C_{p,q}]$ and $x \cdot C > 0$, or has its class in the interior of $\overline{NE}(S)$, and then $x \cdot C > 0$ by Lemma 1.3.2(2), applied to $K = \operatorname{Nef}(S)$, whose dual is $\overline{NE}(S)$. So $x$ is positive on every curve. The ratios $x \cdot C_{p,q} / (C_{p,q} \cdot (f_1 + f_2)) = (q - \sqrt 2 p)^2/(p^2 + q^2)$ tend to $0$ along the solutions of Pell's equation $q^2 - 2p^2 = \pm 1$, which shows concretely that the positivity of $x$ is not uniform.

**Example 1.3.28 (complex multiplication raises the Picard number).** Let $E \colon y^2 = x^3 - x$, the curve with $j = 1728$, with the automorphism $[i](x, y) = (-x, iy)$ of Example P5.4.8. Let $\Gamma_i$ be the graph of $[i]$. Since $[i]$ is an automorphism, Example P5.5.19 with $d = 1$ and $g = 1$ gives $\Gamma_i \cdot f_1 = 1$, $\Gamma_i \cdot f_2 = 1$ and $\Gamma_i^2 = 0$. The points of $\Gamma_i \cap \Delta$ are the fixed points of $[i]$: $-x = x$ and $iy = y$ give $(0, 0)$, and $O$ is fixed. The endomorphism $1 - [i]$ has kernel $\{ O, (0, 0) \}$ and is separable in characteristic $0$, so it has degree $2$, and $\Gamma_i \cdot \Delta = \deg(1 - [i]) = 2$ by the projection formula applied to $\delta$. The Gram matrix of $f_1, f_2, \Delta, \Gamma_i$ is
$$\begin{pmatrix} 0 & 1 & 1 & 1 \\ 1 & 0 & 1 & 1 \\ 1 & 1 & 0 & 2 \\ 1 & 1 & 2 & 0 \end{pmatrix},$$
with determinant $-4$. So the four classes are independent and $\rho(S) \ge 4$, and $\rho(S) = 4$ by Theorem 1.3.24. The form has signature $(1, 3)$ by the Hodge index theorem (Theorem P5.5.22) and the sign of the determinant. Example P5.12.9 still applies: $\overline{NE}(S) = \operatorname{Nef}(S)$ is the round cone $\{ x^2 \ge 0, \ x \cdot (f_1 + f_2) \ge 0 \}$, now in a space of dimension $4$. In the coordinates $(s, t, c)$ of the subspace spanned by $f_1, f_2, \Delta$, the class $\Gamma_i$ would need $s = t = 1$ and $c = 0$, and the class $f_1 + f_2$ with these coordinates has square $2 \ne 0 = \Gamma_i^2$, so $\Gamma_i$ is not in that subspace.

### Proof

*Theorem 1.3.24.* This is Laz04, Section 1.5.B, which deduces it from the description of the Néron-Severi group of a product of curves $C_1 \times C_2$ as $\mathbb{Z}^2 \oplus \operatorname{Hom}(J(C_1), J(C_2))$ (Birkenhake and Lange, *Complex abelian varieties*, Theorem 11.5.1). The idea is as follows. A divisor $D$ on $S$ defines the morphism $\varphi_D \colon E \to \operatorname{Pic}^0(E) \cong E$ that sends $P$ to the class of $D|_{\{P\} \times E} - D|_{\{O\} \times E}$, and the map $D \mapsto (D \cdot f_1, D \cdot f_2, \varphi_D)$ induces an injection of $N^1(S)$ into $\mathbb{R}^2 \oplus (\operatorname{End}(E) \otimes \mathbb{R})$: if $\varphi_D = 0$, the seesaw theorem gives $D \sim p_1^* A + p_2^* B$, and such a divisor is numerically zero only if $\deg A = \deg B = 0$. The graphs of the endomorphisms show that the map is onto after tensoring with $\mathbb{R}$. For the lower bounds used in this section no citation is needed: $\rho(S) \ge 3$ for every $E$ by the Gram matrix above, and $\rho(S) \ge 4$ for $j = 1728$ by Example 1.3.28. $\square$

*Theorem 1.3.25.* By Theorem 1.3.24, $(s, t, c)$ are coordinates on $N^1(S)$. The class $H = f_1 + f_2 = (1, 1, 0)$ is ample: $H^2 = 2 > 0$, and every curve $C$ has $C \cdot H = \deg(p_1|_C) + \deg(p_2|_C) > 0$, since the two projections cannot both be constant on $C$, so Theorem P5.12.5 applies.

(1) By Example P5.12.9, $\overline{NE}(S) = \operatorname{Nef}(S) = \{ x^2 \ge 0, \ x \cdot H \ge 0 \}$, which is $\{ st \ge c^2, \ s + t \ge 0 \}$. If $st \ge c^2 \ge 0$, then $s$ and $t$ have the same sign or one is zero, so $s + t \ge 0$ is equivalent to $s, t \ge 0$. On a surface the classes of effective $\mathbb{R}$-divisors form $NE(S)$ (Definition P5.8.22), so $\operatorname{Psef}(S) = \overline{NE}(S)$. Finally $st = \sigma^2 - \tau^2$ and $s + t = 2\sigma$, so the cone is $\sigma \ge 0$, $\sigma^2 \ge \tau^2 + c^2$.

(2) By Theorem 1.3.4 and Theorem 1.3.16, $\operatorname{Amp}(S)$ and $\operatorname{Big}(S)$ are the interiors of the equal cones $\operatorname{Nef}(S)$ and $\operatorname{Psef}(S)$. The interior of $\{ \sigma \ge \sqrt{\tau^2 + c^2} \}$ is $\{ \sigma > \sqrt{\tau^2 + c^2} \}$, which is $\{ s, t > 0, \ st > c^2 \}$.

(3) A pseudoeffective class is nef by (1), so $\operatorname{vol}(x) = x^2$ by Theorem 1.3.17(3). Outside $\operatorname{Psef}(S)$ the volume is $0$ by Theorem 1.3.17(2).

(4) A nonzero rational point $(s, t, c)$ of the boundary has $st = c^2$ with $s, t \ge 0$. If $s = 0$, then $c = 0$ and the ray is that of $(0, 1, 0)$, which is $(p, q) = (0, 1)$. If $s > 0$, write $c/s = q/p$ in lowest terms with $p > 0$. Then $t/s = c^2/s^2 = q^2/p^2$, so $(s, t, c) = \frac{s}{p^2}(p^2, q^2, pq)$. Conversely each $(p^2, q^2, pq)$ is the class of $C_{p,q}$ by Example 1.3.26. This proves the first two statements.

The interior of $\overline{NE}(S)$ lies in $NE(S)$: the convex set $NE(S)$ contains the nonempty open set $\operatorname{Amp}(S)$, because a multiple of an ample divisor is linearly equivalent to an effective curve, so by Lemma 1.3.3 the interior of $\overline{NE}(S)$ is that of $NE(S)$. The interior is $\operatorname{Amp}(S)$ by (2), and the rational boundary rays lie in $NE(S)$ because they contain curves. Conversely let $y = \sum a_i [C_i] \in NE(S)$ with $a_i > 0$ lie on the boundary, so $y^2 = 0$. Each $[C_i]$ is nef, so $0 = y^2 = \sum a_i a_j \, C_i \cdot C_j$ is a sum of nonnegative terms, and $C_i \cdot C_j = 0$ for all $i, j$. As in Example 1.3.9, a plane on which the form is identically $0$ cannot exist in signature $(1, 2)$, so all $[C_i]$ lie on one ray, which is a rational boundary ray. Finally the class $x$ of Example 1.3.27 lies on an irrational boundary ray, so $x \in \overline{NE}(S) \setminus NE(S)$. $\square$

### Exercises

1. (A) Compute the coordinates $(s, t, c)$ of $f_1 + f_2 + \Delta$, check that it is ample, and compute its volume both from Theorem 1.3.25(3) and by expanding $(f_1 + f_2 + \Delta)^2$.
2. (A) Decide which of the classes $f_1 + f_2 - \Delta$, $2f_1 + 2f_2 - \Delta$ and $3f_1 + 3f_2 - \Delta$ are ample, nef or pseudoeffective, and compute their volumes.
3. (B) For $M = \left(\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\right) \in GL_2(\mathbb{Z})$ let $g_M \colon S \to S$ be $(P, Q) \mapsto (aP + bQ, cP + dQ)$. Show that $g_M$ is an automorphism, that it maps each curve $C_{p,q}$ onto another curve $C_{p',q'}$, and that the group of these automorphisms acts transitively on the rational boundary rays of $\overline{NE}(S)$.
4. (B) Let $E$ have no complex multiplication and $\pi = p_1 \colon S \to E$. Show that $N^1(S/E) \cong \mathbb{R}$ by $x \mapsto t = x \cdot f_1$, and compute $\operatorname{Nef}(S/E)$, $\operatorname{Amp}(S/E)$, $\operatorname{Eff}(S/E)$ and $\operatorname{Big}(S/E)$. Which of $f_1$, $f_2$, $\Delta$ and the antidiagonal are ample over $E$?
5. (B) For the class $x$ of Example 1.3.27, compute $x \cdot C_{p,q}$ for $(p, q) = (1, 1), (2, 3), (5, 7), (12, 17)$, and show that $\inf_C x \cdot C / (C \cdot (f_1 + f_2)) = 0$, the infimum over all curves $C$ on $S$.
6. (C) For the curve $E$ of Example 1.3.28 and integers $a, b$ not both $0$, let $\Gamma_{a,b}$ be the graph of $a + b[i]$. Show that $\Gamma_{a,b} \cdot f_1 = 1$, $\Gamma_{a,b} \cdot f_2 = a^2 + b^2$ and $\Gamma_{a,b}^2 = 0$, and express $[\Gamma_{a,b}]$ in the basis $f_1, f_2, \Delta, \Gamma_i$.

### Lean

The project library has no abelian surfaces and no cones of curves, so nothing in this section is formalized. Mathlib has Weierstrass curves and the group law on the points of an elliptic curve (`WeierstrassCurve.Affine.Point`), and its endomorphism ring is not yet available in a form that would state Theorem 1.3.24.

### Notes and history

The round cone of $E \times E$ is the standard example that the cone of curves need not be polyhedral or closed, and it appears in Laz04, Section 1.5.B, together with the computation of the Picard number, and in Bea96 as an example of an abelian surface. The rational boundary rays are the classes of the elliptic subgroups of $S$, which correspond to the primitive vectors of $\mathbb{Z}^2$ through the map $(p, q) \mapsto C_{p,q}$, and the automorphisms of Exercise 3 permute them. For a general abelian surface the same argument shows that $\overline{NE}$ is the closed positive cone, round when $\rho \ge 3$. An elliptic curve over $\mathbb{C}$ whose $j$-invariant is transcendental has no complex multiplication, since the $j$-invariants of curves with complex multiplication are algebraic integers (Silverman, *Advanced topics in the arithmetic of elliptic curves*, Theorem II.6.1).
