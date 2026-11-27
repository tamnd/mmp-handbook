---
title: The blow-up of a point on a surface
nodes: []
sources: [Har77, Bea96, Rei97]
reads_with: [Har77:V.3, Bea96:ch2]
requires: [P1.9, P3.8, P3.11, P3.12, P4.4, P4.6, P5.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The blow-up of a point on a surface

### Statement

In this chapter $k$ is algebraically closed, $S$ is a smooth projective surface over $k$, and the notation of Chapter 5 is in force: curves on $S$ are effective divisors, $\operatorname{Pic}(S) = \operatorname{Cl}(S)$, and $K_S$ is a canonical divisor. Let $p \in S$ be a closed point with maximal ideal $\mathfrak{m} = \mathfrak{m}_p \subseteq \mathcal{O}_{S,p}$ and ideal sheaf $\mathcal{I}_p$. Let $\pi \colon \tilde S = \operatorname{Bl}_p S \to S$ be the blow-up of $p$ (Definition P3.11.1), with exceptional divisor $E = V(\mathcal{I}_p \mathcal{O}_{\tilde S})$. The local ring $\mathcal{O}_{S,p}$ is regular of dimension $2$. For a regular system of parameters $x, y$, Theorem P1.9.2 identifies the associated graded ring $\operatorname{gr}_\mathfrak{m}(\mathcal{O}_{S,p}) = \bigoplus_n \mathfrak{m}^n / \mathfrak{m}^{n+1}$ with the polynomial ring $k[X, Y]$, where $X$ and $Y$ are the classes of $x$ and $y$.

**Definition P5.6.1 (multiplicity and tangent directions).** For $0 \neq f \in \mathcal{O}_{S,p}$ the *multiplicity* $\operatorname{mult}_p(f)$ is the largest $m$ with $f \in \mathfrak{m}^m$, and the *leading form* of $f$ is its class $f_m(X, Y) \in \mathfrak{m}^m / \mathfrak{m}^{m+1} = k[X, Y]_m$, a nonzero binary form of degree $m$. For a curve $C$ on $S$ with local equation $f$ at $p$, the *multiplicity* of $C$ at $p$ is $m_p(C) = \operatorname{mult}_p(f)$, and the *tangent directions* of $C$ at $p$ are the zeros of $f_m$ on the projective line $\operatorname{Proj} k[X, Y]$. Local equations differ by units, so both depend only on $C$.

For a plane curve and the standard coordinates, these are the multiplicity and tangent lines of Definition P3.11.18. Since $\operatorname{gr}_\mathfrak{m}$ is a domain, the leading form of $fg$ is $f_m g_n$, and $m_p(C + D) = m_p(C) + m_p(D)$. The point $p$ lies on $C$ if and only if $m_p(C) \geq 1$, and $C$ is smooth at $p$ if and only if $m_p(C) = 1$, since $\mathcal{O}_{S,p}/(f)$ is regular exactly when $f \notin \mathfrak{m}^2$ (Proposition P1.9.4).

**Theorem P5.6.2 (the blow-up of a point of a smooth surface).**

1. $\tilde S$ is a smooth projective surface, and $\pi$ is a projective birational morphism that is an isomorphism over $S \setminus \{p\}$, with $\pi^{-1}(p) = E$ as sets.
2. $E \cong \operatorname{Proj} k[X, Y] \cong \mathbb{P}^1_k$, and the conormal sheaf of $E$ is $\mathcal{I}_E / \mathcal{I}_E^2 \cong \mathcal{O}_E(1)$. So $\mathcal{O}_{\tilde S}(E)|_E \cong \mathcal{O}_E(-1)$.
3. $\pi_* \mathcal{O}_{\tilde S} = \mathcal{O}_S$ and $R^q \pi_* \mathcal{O}_{\tilde S} = 0$ for $q > 0$.
4. For every invertible sheaf $\mathcal{L}$ on $S$ and every $i$, $H^i(\tilde S, \pi^* \mathcal{L}) \cong H^i(S, \mathcal{L})$.

Lean: not in Lean as stated.

**Theorem P5.6.3 (the Picard group and the intersection form of the blow-up).**

1. $\operatorname{Pic}(\tilde S) = \pi^* \operatorname{Pic}(S) \oplus \mathbb{Z} E$, and $\pi^* \colon \operatorname{Pic}(S) \to \operatorname{Pic}(\tilde S)$ is injective. A divisor $\tilde D$ on $\tilde S$ is $\pi^* D + a E$ with $a = -\tilde D \cdot E$ and $D$ the closure of $\tilde D|_{\tilde S \setminus E}$ in $S$.
2. For divisors $D$ and $D'$ on $S$, $\pi^* D \cdot \pi^* D' = D \cdot D'$, $\pi^* D \cdot E = 0$ and $E^2 = -1$.
3. $K_{\tilde S} = \pi^* K_S + E$ and $K_{\tilde S}^2 = K_S^2 - 1$. For every $i$, $h^i(\mathcal{O}_{\tilde S}) = h^i(\mathcal{O}_S)$, so $\chi(\mathcal{O}_{\tilde S}) = \chi(\mathcal{O}_S)$.
4. $\operatorname{Num}(\tilde S) = \pi^* \operatorname{Num}(S) \oplus \mathbb{Z} E$, an orthogonal sum, and $\pi^*$ is an isometry onto the first summand. In particular the rank of $\operatorname{Num}$ goes up by $1$.

Lean: not in Lean as stated.

**Proposition P5.6.4 (total and strict transforms).** Let $C$ be a curve on $S$, $m = m_p(C)$, and $C = \sum_i a_i C_i$ with distinct integral curves $C_i$.

1. For $0 \neq f \in \mathcal{O}_{S,p}$, $\operatorname{ord}_E(\pi^* f) = \operatorname{mult}_p(f)$.
2. $\pi^* C = \tilde C + m E$, where $\tilde C = \sum_i a_i \tilde C_i$ is a curve on $\tilde S$ not containing $E$ and $\tilde C_i$ is the strict transform of $C_i$ (Definition P3.11.11). So $\tilde C \sim \pi^* C - m E$.
3. The restriction of $\tilde C$ to $E = \operatorname{Proj} k[X, Y]$ is the divisor of the leading form $f_m$. So $\tilde C \cap E$ is the set of tangent directions of $C$ at $p$, and $\tilde C \cdot E = m$.
4. $\tilde C^2 = C^2 - m^2$, $K_{\tilde S} \cdot \tilde C = K_S \cdot C + m$ and $p_a(\tilde C) = p_a(C) - m(m-1)/2$.
5. If $C$ is integral and $p$ is a smooth point of $C$, then $\pi$ restricts to an isomorphism $\tilde C \to C$.

Lean: not in Lean as stated.

**Corollary P5.6.5 (linear systems with an assigned point).**

1. For $m \geq 0$, $\pi_* \mathcal{O}_{\tilde S}(-mE) = \mathcal{I}_p^m$, and for $n \geq 0$, $\pi_* \mathcal{O}_{\tilde S}(nE) = \mathcal{O}_S$.
2. Let $D$ be a divisor on $S$ and $m \geq 0$. Pullback identifies $H^0(\tilde S, \mathcal{O}(\pi^* D - mE))$ with the space of sections of $\mathcal{O}_S(D)$ whose divisor has multiplicity at least $m$ at $p$. So the members of $|\pi^* D - m E|$ are the divisors $\tilde C + (m_p(C) - m) E$ for $C \in |D|$ with $m_p(C) \geq m$, and
$$h^0(\tilde S, \pi^* D - m E) \geq h^0(S, D) - \frac{m(m+1)}{2}.$$
3. For $n \geq 0$, $h^0(\tilde S, \pi^* D + nE) = h^0(S, D)$. In particular $nE$ is the only member of $|nE|$.

Lean: not in Lean as stated.

**Proposition P5.6.6 (intersection multiplicities under a blow-up).** Let $C$ and $D$ be curves on $S$ with no common component, of multiplicities $m$ and $n$ at $p$. Then $\tilde C$ and $\tilde D$ have no common component, and
$$(C \cdot D)_p = mn + \sum_{q \in E} (\tilde C \cdot \tilde D)_q .$$
So $(C \cdot D)_p \geq m_p(C) \, m_p(D)$, with equality if and only if $C$ and $D$ have no common tangent direction at $p$.

Lean: not in Lean as stated.

### Proof in words

Near $p$ the blow-up is the one computed in Theorem P3.12.32: a regular system of parameters $x, y$ gives two charts, on which $y = xt$ or $x = ys$, and $E$ is the line with coordinate $t$. A function $f$ of multiplicity $m$ pulls back to $x^m$ times a function whose restriction to $E$ is the dehomogenized leading form $f_m(1, t)$. This one computation gives the multiplicity of $E$ in $\pi^* C$, the points where $\tilde C$ meets $E$, and the self-intersection $E^2 = -1$, since $x$ and $y$ are two sections of the conormal bundle of $E$ with a single simple zero each. The cohomology of $\tilde S$ is that of $S$ because the higher direct images of $\mathcal{O}_{\tilde S}$ vanish, by the theorem on formal functions: the thickenings $nE$ are built from the sheaves $\mathcal{O}_E(n)$, which have no $H^1$. Once $\chi$ does not change under pullback, the definition of the pairing through Euler characteristics gives $\pi^* D \cdot \pi^* D' = D \cdot D'$ at once, and the rest is the arithmetic of the orthogonal sum $\pi^* \operatorname{Pic}(S) \oplus \mathbb{Z} E$ together with the adjunction formula.

### Examples

**Example P5.6.7 (the plane blown up at a point).** Let $S = \mathbb{P}^2$ with line class $\ell$ and $\tilde S = \operatorname{Bl}_p \mathbb{P}^2$, which is the Hirzebruch surface $F_1$ by Theorem P3.11.26. By Theorem P5.6.3, $\operatorname{Pic}(\tilde S) = \mathbb{Z} \ell \oplus \mathbb{Z} E$, writing $\ell$ for $\pi^* \ell$, with $\ell^2 = 1$, $\ell \cdot E = 0$, $E^2 = -1$, and $K_{\tilde S} = -3\ell + E$ with $K_{\tilde S}^2 = 9 - 1 = 8$. A line through $p$ has strict transform of class $\ell - E$, with $(\ell - E)^2 = 0$ and $K_{\tilde S} \cdot (\ell - E) = -2$. These strict transforms are the fibres of the ruling $\tilde S \to \mathbb{P}^1$, and $E$, with $E \cdot (\ell - E) = 1$, is the negative section $C_-$ of $F_1$. A plane curve of degree $d$ with multiplicity $m$ at $p$ has strict transform of class $d\ell - mE$ by Proposition P5.6.4, which recovers part 2 of Theorem P3.11.19.

**Example P5.6.8 (the plane blown up at several points).** Let $p_1, \dots, p_r \in \mathbb{P}^2$ be distinct, and blow them up one after another. The point $p_{i+1}$ is not blown up yet, so its preimage is a single point off the earlier exceptional curves, and Theorem P5.6.3 applies at each step. The result $S_r$ has
$$\operatorname{Pic}(S_r) = \mathbb{Z} \ell \oplus \mathbb{Z} E_1 \oplus \dots \oplus \mathbb{Z} E_r, \quad \ell^2 = 1, \ E_i^2 = -1, \quad K_{S_r} = -3\ell + E_1 + \dots + E_r,$$
with the $E_i$ orthogonal to each other and to $\ell$, and $K_{S_r}^2 = 9 - r$, $\chi(\mathcal{O}_{S_r}) = 1$. A line through exactly two of the points, $p_i$ and $p_j$, has strict transform $\ell - E_i - E_j$, a smooth rational curve with self-intersection $1 - 2 = -1$ and $K \cdot (\ell - E_i - E_j) = -3 + 2 = -1$. If $p_1, p_2, p_3$ lie on a line, its strict transform has class $\ell - E_1 - E_2 - E_3$, self-intersection $-2$ and $K \cdot (\ell - E_1 - E_2 - E_3) = 0$: a $(-2)$-curve in the sense of Corollary P5.5.15. A smooth conic through exactly five of the points has strict transform $2\ell - E_1 - \dots - E_5$, again with square and canonical degree $-1$. Chapters 9 and 10 return to these curves.

**Example P5.6.9 (the quadric blown up at a point).** Let $Q = V(xw - yz) \subseteq \mathbb{P}^3$, $p = [0 : 0 : 0 : 1]$, and $\pi \colon \tilde Q \to Q$ the blow-up of $p$. With the rulings $F_1$ and $F_2$ of Example P5.5.9, $\operatorname{Pic}(\tilde Q) = \mathbb{Z} F_1 \oplus \mathbb{Z} F_2 \oplus \mathbb{Z} E$ with $F_1 \cdot F_2 = 1$, $F_i^2 = 0$, $E^2 = -1$, and $K_{\tilde Q} = -2F_1 - 2F_2 + E$ by Example P3.12.26. The two lines of $Q$ through $p$ are $L_1 = V(x, y)$ and $L_2 = V(x, z)$, one in each ruling. Their strict transforms $L_i - E$ have $(F_i - E)^2 = -1$, $K_{\tilde Q} \cdot (F_i - E) = -2 + 1 = -1$ and $(F_1 - E) \cdot (F_2 - E) = 1 - 1 = 0$: two disjoint $(-1)$-curves.

The projection from $p$, $[x : y : z : w] \mapsto [x : y : z]$, is defined on $Q \setminus \{p\}$. Near $p$, with $w = 1$, $Q$ is the graph $x = yz$, the functions $y, z$ are local parameters, and $x \in \mathfrak{m}^2$. So $x, y, z$ are sections of $\mathcal{O}_Q(1)$ of multiplicity at least $1$ at $p$, and by Corollary P5.6.5 they pull back to sections of $\pi^* \mathcal{O}_Q(1)(-E) = \mathcal{O}(F_1 + F_2 - E)$. Off $E$ they have no common zero, and on $E = \operatorname{Proj} k[Y, Z]$ the pullbacks of $y$ and $z$ restrict to the forms $Y$ and $Z$ by Proposition P5.6.4, while $x$ restricts to $0$. So they have no common zero on $\tilde Q$ and define a morphism $\varphi \colon \tilde Q \to \mathbb{P}^2$ extending the projection. A point $[x : y : z]$ with $x \neq 0$ has the single preimage $w = yz/x$, so $\varphi$ is birational. It maps $E$ to the line $V(x)$, and it contracts $L_1 - E$ and $L_2 - E$ to the points $[0 : 0 : 1]$ and $[0 : 1 : 0]$. Chapter 7 shows that $\varphi$ is the blow-up of $\mathbb{P}^2$ at these two points, so $\operatorname{Bl}_p(\mathbb{P}^1 \times \mathbb{P}^1) \cong \operatorname{Bl}_{q_1, q_2} \mathbb{P}^2$.

**Example P5.6.10 (nodal and cuspidal cubics).** Let $C \subseteq \mathbb{P}^2$ be a cubic with a double point at $p$. Then $\tilde C \sim 3\ell - 2E$, $\tilde C^2 = 9 - 4 = 5$, $K_{\tilde S} \cdot \tilde C = -9 + 2 = -7$, and $p_a(\tilde C) = 1 - 1 = 0$. Since $\tilde C^2 + K_{\tilde S} \cdot \tilde C = -2$, Corollary P5.5.15 shows $\tilde C \cong \mathbb{P}^1$: one blow-up normalizes the cubic. For the nodal cubic $y^2 = x^2(x + 1)$ the leading form is $Y^2 - X^2$, so $\tilde C$ meets $E$ in the two points $t = \pm 1$, each transversally, as in Example P3.11.13. For the cuspidal cubic $y^2 = x^3$ the leading form is $Y^2$, so $\tilde C$ meets $E$ only at $t = 0$, with $(\tilde C \cdot E)_{t = 0} = 2$: the strict transform is smooth and tangent to $E$, as in Example P3.11.14.

**Example P5.6.11 (tangent curves).** In $\mathbb{A}^2 \subseteq \mathbb{P}^2$ let $C$ be the conic $y = x^2$ and $D$ the line $y = 0$. They meet only at the origin, with $(C \cdot D)_0 = \dim_k k[x, y]_{(x, y)}/(y - x^2, y) = 2$, and both have the tangent direction $Y = 0$, that is, $t = 0$. In the chart $y = xt$, $\tilde C = V(t - x)$ and $\tilde D = V(t)$, which meet transversally at the point $t = 0$ of $E$. So $(C \cdot D)_0 = 1 \cdot 1 + 1$, as Proposition P5.6.6 says. For the nodal cubic $C \colon y^2 = x^2(x + 1)$ and its tangent line $D \colon y = x$, $(C \cdot D)_0 = \dim_k k[x]_{(x)}/(x^3) = 3 = 2 \cdot 1 + 1$, and the extra $1$ is the transverse intersection of $\tilde C$ and $\tilde D$ at the common tangent direction $t = 1$.

### Proof

*Theorem P5.6.2.* (1) and (2). By the proof of Theorem P3.12.32 there is an affine open neighbourhood $W = \operatorname{Spec} B$ of $p$ on which $\mathcal{I}_p$ is generated by a regular sequence $x, y$ of $B$, and $\pi^{-1}(W)$ is covered by the two charts
$$U_1 = \operatorname{Spec} B[t]/(xt - y), \qquad U_2 = \operatorname{Spec} B[s]/(ys - x),$$
which are smooth surfaces, with $E \cap U_1 = V(x) = \operatorname{Spec} k[t]$ and $E \cap U_2 = V(y) = \operatorname{Spec} k[s]$, glued along $s = 1/t$. The images of $x$ and $y$ in $\mathcal{O}_{S,p}$ are a regular system of parameters, and $t = y/x$ is the coordinate $Y/X$ on $\operatorname{Proj} k[X, Y]$. So $E \cong \operatorname{Proj} k[X, Y] \cong \mathbb{P}^1_k$. By Theorem P3.11.3, $\pi$ is proper and birational, $\tilde S$ is integral, and $\pi$ is an isomorphism over $S \setminus \{p\}$. Away from $\pi^{-1}(W)$ the surface $\tilde S$ is isomorphic to $S \setminus \{p\}$, so $\tilde S$ is smooth, and $\pi^{-1}(p) = V(\mathcal{I}_p \mathcal{O}_{\tilde S}) = E$ as sets.

For projectivity, let $S \subseteq \mathbb{P}^N$ be closed, with coordinates $x_0, \dots, x_N$ chosen so that $p = [1 : 0 : \dots : 0]$. Let $P \subseteq \mathbb{P}^N \times \mathbb{P}^{N-1}$ be the closed subscheme $V(x_i u_j - x_j u_i : 1 \leq i < j \leq N)$. Over $D_+(x_0) = \mathbb{A}^N$, $P$ is the blow-up of the origin by Theorem P3.11.4. Over $\mathbb{P}^N \setminus \{p\}$, where $x_1, \dots, x_N$ have no common zero, the equations say $[u] = [x_1 : \dots : x_N]$, so $P$ is the graph of the linear projection from $p$, isomorphic to $\mathbb{P}^N \setminus \{p\}$, and over the overlap the two descriptions agree. So $P = \operatorname{Bl}_p \mathbb{P}^N$, using part 1 of Theorem P3.11.3 to glue. The ideal of $p$ in $\mathbb{P}^N$ restricts to the ideal of $p$ in $S$, so by part 2 of Corollary P3.11.10, $\tilde S$ is a closed subscheme of $P$. So $\tilde S$ is closed in $S \times \mathbb{P}^{N-1}$, hence $\pi$ is projective, and $\tilde S$ is closed in $\mathbb{P}^N \times \mathbb{P}^{N-1}$, which is projective by Theorem P3.10.20.

On $U_1$ the ideal $\mathcal{I}_E$ is generated by $x$, and on $U_2$ by $y$. Since $y = xt$ on $U_1$ and $x = ys$ on $U_2$, the elements $x$ and $y$ are sections of $\mathcal{I}_E$ over $\pi^{-1}(W)$, and their images are global sections of the line bundle $\mathcal{I}_E / \mathcal{I}_E^2$ on $E$. The image of $x$ generates on $E \cap U_1$ and equals $s$ times the generator $y$ on $E \cap U_2$, so its divisor is the single point $s = 0$ with multiplicity $1$. A line bundle on $\mathbb{P}^1_k$ with a section whose divisor has degree $1$ is $\mathcal{O}(1)$ (Corollary P3.9.11), so $\mathcal{I}_E / \mathcal{I}_E^2 \cong \mathcal{O}_E(1)$, with $x$ and $y$ the sections $X$ and $Y$. Since $\mathcal{I}_E = \mathcal{O}_{\tilde S}(-E)$, this gives $\mathcal{O}_{\tilde S}(E)|_E \cong \mathcal{O}_E(-1)$.

(3) The surface $S$ is normal (Corollary P1.9.26), and $\pi$ is projective and birational between integral schemes, so $\pi_* \mathcal{O}_{\tilde S} = \mathcal{O}_S$ by Theorem P4.6.8. The fibres of $\pi$ have dimension at most $1$, so $R^q \pi_* \mathcal{O}_{\tilde S} = 0$ for $q \geq 2$ by Corollary P4.6.2. The sheaf $R^1 \pi_* \mathcal{O}_{\tilde S}$ is coherent (Theorem P4.4.8), and it vanishes on $S \setminus \{p\}$, where $\pi$ is an isomorphism. At $p$ apply the theorem on formal functions (Theorem P4.6.1) to $\pi^{-1}(W) \to W$. Since $\mathfrak{m}^n \mathcal{O}_{\tilde S} = \mathcal{I}_E^n$, the scheme $X_n$ is the subscheme $nE$ defined by $\mathcal{I}_E^n$. As $\mathcal{I}_E$ is invertible, $\mathcal{I}_E^n / \mathcal{I}_E^{n+1} \cong (\mathcal{I}_E / \mathcal{I}_E^2)^{\otimes n} \cong \mathcal{O}_E(n)$, which gives exact sequences
$$0 \to \mathcal{O}_E(n) \to \mathcal{O}_{(n+1)E} \to \mathcal{O}_{nE} \to 0 .$$
By Theorem P4.2.1, $H^1(E, \mathcal{O}_E(n)) = 0$ for $n \geq 0$, and $H^1(E, \mathcal{O}_E) = 0$. By induction $H^1(nE, \mathcal{O}_{nE}) = 0$ for all $n \geq 1$. So the $\mathfrak{m}$-adic completion of the finitely generated module $M = (R^1 \pi_* \mathcal{O}_{\tilde S})_p$ is $0$. Then $M = \mathfrak{m} M$, and $M = 0$ by Nakayama. So $R^1 \pi_* \mathcal{O}_{\tilde S} = 0$.

(4) By the projection formula (Proposition P4.4.10) and part 3, $\pi_* \pi^* \mathcal{L} \cong \mathcal{L} \otimes \pi_* \mathcal{O}_{\tilde S} = \mathcal{L}$ and $R^q \pi_* \pi^* \mathcal{L} \cong \mathcal{L} \otimes R^q \pi_* \mathcal{O}_{\tilde S} = 0$ for $q > 0$. By part 3 of Corollary P4.4.2, $H^i(\tilde S, \pi^* \mathcal{L}) \cong H^i(S, \pi_* \pi^* \mathcal{L}) = H^i(S, \mathcal{L})$. $\square$

*Theorem P5.6.3.* (2) Write $\mathcal{L} = \mathcal{O}_S(D)$ and $\mathcal{M} = \mathcal{O}_S(D')$. By part 4 of Theorem P5.6.2, $\chi(\pi^* \mathcal{N}) = \chi(\mathcal{N})$ for every invertible $\mathcal{N}$ on $S$. The pullback commutes with tensor products and inverses, so Definition P5.5.4 gives
$$(\pi^* \mathcal{L} \cdot \pi^* \mathcal{M}) = \chi(\mathcal{O}_{\tilde S}) - \chi(\pi^* \mathcal{L}^{-1}) - \chi(\pi^* \mathcal{M}^{-1}) + \chi(\pi^*(\mathcal{L}^{-1} \otimes \mathcal{M}^{-1})) = (\mathcal{L} \cdot \mathcal{M}).$$
The restriction $\pi^* \mathcal{L}|_E$ is the pullback of $\mathcal{L}|_{\{p\}}$ along $E \to \{p\}$, a trivial bundle, so $\pi^* D \cdot E = \deg(\pi^* \mathcal{L}|_E) = 0$ by Theorem P5.5.6. By the same theorem and part 2 of Theorem P5.6.2, $E^2 = \deg \mathcal{O}_E(-1) = -1$.

(1) Both $S$ and $\tilde S$ are regular, so $\operatorname{Pic} = \operatorname{Cl}$ for both (Corollary P3.9.11). Let $\tilde D$ be a divisor on $\tilde S$. The open set $\tilde S \setminus E$ is isomorphic to $S \setminus \{p\}$, and by part 1 of Theorem P3.8.13 the divisor $\tilde D|_{\tilde S \setminus E}$ is the restriction of a unique divisor $D$ on $S$, since $\{p\}$ has codimension $2$. Then $\tilde D$ and $\pi^* D$ agree on $\tilde S \setminus E$, so by the same theorem $\tilde D - \pi^* D = aE$ for some $a \in \mathbb{Z}$. Intersecting with $E$ and using part 2 gives $\tilde D \cdot E = -a$. If $\pi^* D + aE \sim 0$, then $a = -(\pi^* D + aE) \cdot E = 0$, and $\pi^* D = \operatorname{div}(h)$ for a rational function $h$. Restricting to $S \setminus \{p\}$ shows that $D - \operatorname{div}(h)$ is a divisor supported on $\{p\}$, which is $0$. So $D \sim 0$, and the sum is direct with $\pi^*$ injective.

(3) The formula $K_{\tilde S} = \pi^* K_S + E$ is Theorem P3.12.32. By part 2, $K_{\tilde S}^2 = K_S^2 + 2 \pi^* K_S \cdot E + E^2 = K_S^2 - 1$. Part 4 of Theorem P5.6.2 with $\mathcal{L} = \mathcal{O}_S$ gives $h^i(\mathcal{O}_{\tilde S}) = h^i(\mathcal{O}_S)$.

(4) The decomposition of part 1 is orthogonal by part 2. If $\pi^* D + aE \equiv 0$, then intersecting with $E$ gives $a = 0$, and intersecting with $\pi^* D'$ gives $D \cdot D' = 0$ for all $D'$, so $D \equiv 0$. Conversely $D \equiv 0$ gives $\pi^* D \equiv 0$, since $\pi^* D$ is orthogonal to $E$ and to every $\pi^* D'$. So the numerically trivial classes of $\tilde S$ are the $\pi^* D$ with $D \equiv 0$, and $\operatorname{Num}(\tilde S) = \pi^* \operatorname{Num}(S) \oplus \mathbb{Z} E$. $\square$

*Proposition P5.6.4.* (1) and (3). Use the charts of the proof of Theorem P5.6.2, and shrink $W$ so that a local equation $f$ of $C$ at $p$ lies in $B$, with $C \cap W = V(f)$, and $f = \sum_{i + j = m} a_{ij} x^i y^j$ with $a_{ij} \in B$: this is possible since $f \in \mathfrak{m}^m = (x, y)^m \mathcal{O}_{S,p}$, after inverting a denominator $b \in B$ with $b(p) \neq 0$. The leading form is $f_m = \sum a_{ij}(p) X^i Y^j$, nonzero by assumption. On $U_1$, $y = xt$ gives
$$\pi^* f = x^m g, \qquad g = \sum_{i + j = m} a_{ij} t^j, \qquad g|_{E \cap U_1} = \sum a_{ij}(p) t^j = f_m(1, t),$$
and symmetrically $\pi^* f = y^m g'$ on $U_2$ with $g'|_{E \cap U_2} = f_m(s, 1)$. The polynomial $f_m(1, t)$ is not zero, because its coefficients are those of $f_m$, so $g \notin (x)$. Since $x$ generates the ideal of the prime divisor $E$ on $U_1$, $\operatorname{ord}_E(\pi^* f) = m$, which is (1). The function $g$ on $U_1$ and $g'$ on $U_2$ are local equations of the effective divisor $\pi^* C - mE$ near $E$, and their restrictions to $E$ are the dehomogenizations of $f_m$ on the two charts. So $(\pi^* C - mE)|_E$ is the divisor of $f_m$, of degree $m$, which is (3) once (2) is proved, using $\tilde C \cdot E = \deg \mathcal{O}(\tilde C)|_E$ (Theorem P5.5.6).

(2) The divisor $\tilde C = \pi^* C - mE$ is effective by the computation above, and $E \not\subseteq \operatorname{Supp} \tilde C$ because $\operatorname{ord}_E(g) = 0$. On $\tilde S \setminus E \cong S \setminus \{p\}$ it is $\sum a_i (C_i \setminus \{p\})$. A divisor without $E$ in its support is determined by its restriction to $\tilde S \setminus E$, and by Proposition P3.11.12 the closure of $\pi^{-1}(C_i \setminus \{p\})$ is the strict transform $\tilde C_i$. So $\tilde C = \sum a_i \tilde C_i$.

(4) By Theorem P5.6.3, $\tilde C^2 = (\pi^* C - mE)^2 = C^2 - m^2$ and $K_{\tilde S} \cdot \tilde C = (\pi^* K_S + E) \cdot (\pi^* C - mE) = K_S \cdot C + m$. By the genus formula (Theorem P5.5.14),
$$2 p_a(\tilde C) - 2 = \tilde C^2 + K_{\tilde S} \cdot \tilde C = C^2 + K_S \cdot C - m^2 + m = 2 p_a(C) - 2 - m(m - 1).$$

(5) If $p \notin C$ there is nothing to prove. Otherwise $m = 1$, and $p_a(\tilde C) = p_a(C)$ by (4). The morphism $\pi|_{\tilde C} \colon \tilde C \to C$ is birational by Proposition P3.11.12, so the two integral curves have the same normalization by Theorem P5.1.3, and they have the same local rings away from $p$ and $\tilde C \cap E$. By the genus formula of Proposition P5.3.2 for both curves, $\sum_{q \in \tilde C \cap E} \delta_q(\tilde C) = \delta_p(C) = 0$. So $\tilde C$ is smooth, and $\tilde C \cap E$ is one point by (3). Then $\pi|_{\tilde C}$ is a birational morphism of smooth projective curves, an isomorphism by Theorem P5.1.3. $\square$

*Corollary P5.6.5.* (1) Let $V \subseteq S$ be open. A section of $\mathcal{O}_{\tilde S}(-mE)$ over $\pi^{-1}(V)$ is a regular function $h$ on $\pi^{-1}(V)$ with $\operatorname{ord}_E(h) \geq m$. By part 3 of Theorem P5.6.2, $h = \pi^* f$ for a unique $f \in \mathcal{O}_S(V)$, and if $p \in V$ then $\operatorname{ord}_E(\pi^* f) = \operatorname{mult}_p(f)$ by part 1 of Proposition P5.6.4. So the condition is $f_p \in \mathfrak{m}^m$, that is, $f \in \mathcal{I}_p^m(V)$. A section of $\mathcal{O}_{\tilde S}(nE)$ over $\pi^{-1}(V)$ is a rational function regular on $\pi^{-1}(V) \setminus E \cong V \setminus \{p\}$ with a pole of order at most $n$ along $E$. A regular function on $V \setminus \{p\}$ extends to $V$ by the Hartogs property (Theorem P3.7.33), so the section lies in $\mathcal{O}_S(V)$.

(2) By the projection formula (Proposition P4.4.10) and part 1, $\pi_* \mathcal{O}(\pi^* D - mE) \cong \mathcal{O}_S(D) \otimes \mathcal{I}_p^m$, whose global sections are the sections $s$ of $\mathcal{O}_S(D)$ with $\operatorname{mult}_p(s) \geq m$ in a local trivialization. For such $s$ with divisor $C$, the divisor of $\pi^* s$ as a section of $\mathcal{O}(\pi^* D - mE)$ is $\pi^* C - mE = \tilde C + (m_p(C) - m) E$ by Proposition P5.6.4. The inequality holds because the condition $s_p \in \mathfrak{m}^m \mathcal{O}_S(D)_p$ is the vanishing of the image of $s$ in $\mathcal{O}_S(D)_p / \mathfrak{m}^m \mathcal{O}_S(D)_p \cong \mathcal{O}_{S,p}/\mathfrak{m}^m$, a space of dimension $\sum_{j = 0}^{m - 1} (j + 1) = m(m+1)/2$ by Theorem P1.9.2.

(3) As in (2), $\pi_* \mathcal{O}(\pi^* D + nE) \cong \mathcal{O}_S(D)$ by part 1. For $D = 0$ the only sections of $\mathcal{O}(nE)$ are the constants, whose divisor is $nE$. $\square$

*Proposition P5.6.6.* The components of $\tilde C$ and $\tilde D$ are the strict transforms of those of $C$ and $D$ by Proposition P5.6.4, and distinct integral curves have distinct strict transforms, since these are closures of the distinct sets $\pi^{-1}(C_i \setminus \{p\})$. By Theorem P5.6.3,
$$\tilde C \cdot \tilde D = (\pi^* C - mE) \cdot (\pi^* D - nE) = C \cdot D - mn .$$
By Proposition P5.5.5 both sides are sums of local multiplicities. At a point $q \notin E$ the local rings of $\tilde S$ at $q$ and of $S$ at $\pi(q)$ are the same, and so are the local equations, so the local multiplicities at points off $E$ and off $p$ match. Subtracting gives the formula. The sum over $q \in E$ is zero exactly when $\tilde C \cap \tilde D \cap E = \emptyset$, and by part 3 of Proposition P5.6.4 that means that $C$ and $D$ have no common tangent direction. $\square$

### Exercises

1. (A) On $\operatorname{Bl}_p \mathbb{P}^2$, find all classes $D = a\ell - bE$ with $D^2 = K \cdot D = -1$. Show that $E$ is the only one.
2. (A) Let $C \subseteq \mathbb{P}^2$ be an integral curve of degree $d \geq 2$ with a point $p$ of multiplicity $m$. Using $\tilde C \cdot (\ell - E) \geq 0$ for the strict transform of a line through $p$ not contained in $C$, show that $m \leq d$, and show that $m \leq d - 1$ by choosing the line through $p$ and a second point of $C$.
3. (B) Let $p \in \mathbb{P}^2$. Show that $h^0(\operatorname{Bl}_p \mathbb{P}^2, 2\ell - 2E) = 3$, that every member of $|2\ell - 2E|$ is $\tilde L_1 + \tilde L_2$ for two lines $L_1, L_2$ through $p$, and that the bound of Corollary P5.6.5 is an equality here.
4. (B) Let $p_1, p_2, p_3 \in \mathbb{P}^2$ be non-collinear and $S_3$ the blow-up of the three points. Show that the strict transforms of the three lines $p_i p_j$ are disjoint $(-1)$-curves, and that $\ell' = 2\ell - E_1 - E_2 - E_3$ and $E'_i = \ell - E_j - E_k$, for $\{i, j, k\} = \{1, 2, 3\}$, form a basis of $\operatorname{Pic}(S_3)$ with the same intersection matrix as $\ell, E_1, E_2, E_3$ and with $K_{S_3} = -3\ell' + E'_1 + E'_2 + E'_3$.
5. (B) Show that $h^0(\tilde S, nK_{\tilde S}) = h^0(S, nK_S)$ for every $n \geq 0$. Deduce that the plurigenera do not change under the blow-up of a point.
6. (C) Find an isometry between $\operatorname{Pic}(\operatorname{Bl}_p(\mathbb{P}^1 \times \mathbb{P}^1))$, with basis $F_1, F_2, E$, and $\operatorname{Pic}(\operatorname{Bl}_{q_1, q_2} \mathbb{P}^2)$, with basis $\ell, E_1, E_2$, that maps canonical class to canonical class and matches the classes in Example P5.6.9: $F_1 - E$ and $F_2 - E$ go to $E_1$ and $E_2$, and $E$ goes to the strict transform $\ell - E_1 - E_2$ of the line through $q_1$ and $q_2$.

### Lean

Mathlib has blow-ups neither of schemes nor of ideals in the form used here, and it does not formalize the intersection pairing on a surface. It has the Rees algebra of an ideal (`reesAlgebra`) and ideal-adic filtrations (`Ideal.Filtration`), from which the multiplicity of Definition P5.6.1 could be built. The handbook adds no `MinimalModel` node here.

### Notes and history

The blow-up of a point, as the quadratic transformation of plane curves, goes back to Noether, Cremona and Max Noether's work of the 1870s on the resolution of plane curve singularities. The formulas $E^2 = -1$, $K_{\tilde S} = \pi^* K_S + E$ and the behaviour of strict transforms are Hartshorne, Propositions V.3.2 to V.3.7, and Beauville, Chapter II. Hartshorne proves $\pi^* D \cdot \pi^* D' = D \cdot D'$ by moving $D'$ away from $p$; the proof above uses instead the invariance of $\chi$ under pullback, which is where the vanishing of $R^1 \pi_* \mathcal{O}_{\tilde S}$ enters. The literature state is theorem. In the language of Volume 4, the coefficient $1$ of $E$ in $K_{\tilde S} - \pi^* K_S$ is the discrepancy of $E$ over the smooth surface $S$, and the computation of Theorem P3.12.32 is the first case of the statement that smooth varieties are terminal. The equality $R^1 \pi_* \mathcal{O}_{\tilde S} = 0$ says that a smooth point is a rational singularity, and Corollary P5.6.5 is the basis of the theory of linear systems with assigned base points used for del Pezzo surfaces in Chapter 9 and Chapter 10.
