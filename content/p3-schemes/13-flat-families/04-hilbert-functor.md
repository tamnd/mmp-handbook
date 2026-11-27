---
title: The Hilbert functor and families of hypersurfaces
nodes: []
sources: [Vak25, Har77, Gro61]
reads_with: [Vak25:ch24, Har77:III.9]
requires: [P1.1, P1.3, P1.5, P1.13, P2.1, P2.5, P3.3, P3.6, P3.13]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Hilbert functor and families of hypersurfaces

### Statement

By Theorem P3.13.16, the Hilbert polynomial is constant in a flat family over a connected base. Fixing the polynomial gives a moduli problem.

**Definition P3.13.32 (the Hilbert functor).** Let $n \geq 1$ and $P \in \mathbb{Q}[m]$. For a scheme $T$, let $\operatorname{Hilb}^P(T)$ be the set of closed subschemes $Z \subseteq \mathbb{P}^n_T = \mathbb{P}^n_\mathbb{Z} \times T$ that are flat over $T$ and whose fibre $Z_t \subseteq \mathbb{P}^n_{\kappa(t)}$ has Hilbert polynomial $P$ for every $t \in T$. For $g \colon T' \to T$, let $g^* Z = Z \times_T T' \subseteq \mathbb{P}^n_{T'}$. This makes $\operatorname{Hilb}^P = \operatorname{Hilb}^P_{\mathbb{P}^n}$ a functor $\mathsf{Sch}^{\mathrm{op}} \to \mathsf{Set}$, the *Hilbert functor*.

Lean: not in Lean as stated.

The pullback lies in $\operatorname{Hilb}^P(T')$: it is a closed subscheme by Proposition P3.3.20, flat over $T'$ by part 3 of Proposition P3.13.3, and its fibre over $t' \in T'$ is $Z_t \times_{\kappa(t)} \kappa(t')$ for $t = g(t')$, which has Hilbert polynomial $P$ by part 2 of Lemma P3.13.13. Closed subschemes and flatness are local, so $\operatorname{Hilb}^P$ is a Zariski sheaf.

Write $S_A = A[x_0, \dots, x_n]$ for a ring $A$. A form $F \in (S_A)_d$ has *unit content* if its coefficients generate the unit ideal of $A$.

**Lemma P3.13.33 (McCoy).** Let $A$ be a ring and $F \in S_A$. If $F$ is a zero divisor in $S_A$, there is $c \neq 0$ in $A$ with $cF = 0$. In particular a form with unit content is a nonzerodivisor in $S_A$.

Lean: not in Lean as stated.

**Lemma P3.13.34 (local freeness of a cokernel).** Let $(A, \mathfrak{m}, \kappa)$ be a local ring and $\varphi \colon A^a \to A^b$ a homomorphism with $\varphi \otimes \kappa$ injective. Then $\varphi$ is injective and $\operatorname{coker} \varphi$ is free of rank $b - a$.

Lean: not in Lean as stated.

**Proposition P3.13.35 (relative hypersurfaces).** Let $A$ be a ring, $d \geq 1$, $F \in (S_A)_d$ a form with unit content, and $Z = V_+(F) = \operatorname{Proj} S_A/(F) \subseteq \mathbb{P}^n_A$.

1. For every ring map $A \to B$ the image $F_B$ of $F$ in $S_B$ has unit content, and $Z \times_A B = V_+(F_B)$.
2. For every $m \geq 0$, the $A$-module $(S_A/(F))_m$ is flat, and its localization at every prime is free of rank $P_d(m) = \binom{m + n}{n} - \binom{m - d + n}{n}$, where the second term is $0$ for $m < d$.
3. $Z$ is flat over $A$, and every fibre $Z_\mathfrak{p}$ is a hypersurface of degree $d$ in $\mathbb{P}^n_{\kappa(\mathfrak{p})}$. So $Z \in \operatorname{Hilb}^{P_d}(\operatorname{Spec} A)$.
4. If $G \in (S_A)_d$ has unit content and $V_+(G) = V_+(F)$ as closed subschemes, then $G = uF$ for a unit $u \in A^\times$.

Lean: not in Lean as stated.

**Definition P3.13.36 (the functor of hypersurfaces).** Let $d \geq 1$. For a scheme $T$, let $\mathbf{H}_d(T)$ be the set of closed subschemes $Z \subseteq \mathbb{P}^n_T$ for which there is a cover of $T$ by affine opens $T_i = \operatorname{Spec} A_i$ and forms $F_i \in (S_{A_i})_d$ with unit content such that $Z \cap \mathbb{P}^n_{T_i} = V_+(F_i)$. Pullback is as in Definition P3.13.32, which preserves $\mathbf{H}_d$ by part 1 of Proposition P3.13.35. These are the *families of hypersurfaces of degree $d$* over $T$, and $\mathbf{H}_d$ is a subfunctor of $\operatorname{Hilb}^{P_d}$ by part 3.

Lean: not in Lean as stated.

**Theorem P3.13.37 (the space of hypersurfaces).** Let $N = \binom{n + d}{d} - 1$ and give $\mathbb{P}^N_\mathbb{Z}$ homogeneous coordinates $a_\alpha$ indexed by the monomials $x^\alpha$ of degree $d$. The functor $\mathbf{H}_d$ is represented by $\mathbb{P}^N_\mathbb{Z}$, with universal family the *universal hypersurface*
$$
\mathcal{Z} = V\Big(\sum_\alpha a_\alpha x^\alpha\Big) \subseteq \mathbb{P}^n_\mathbb{Z} \times \mathbb{P}^N_\mathbb{Z},
$$
the closed subscheme that over the chart $D_+(a_\beta)$ is $V_+(\sum_\alpha (a_\alpha/a_\beta) x^\alpha)$. A morphism $T \to \mathbb{P}^N$ is the same as a family of hypersurfaces of degree $d$ over $T$.

Lean: not in Lean as stated.

**Proposition P3.13.38 (hypersurfaces are determined by their polynomial).** Let $k$ be a field, $d \geq 1$, and $X \subseteq \mathbb{P}^n_k$ a closed subscheme with $P_X = P_d$. Then $X = V_+(F)$ for a nonzero form $F$ of degree $d$, unique up to a scalar. So $\mathbf{H}_d(k) = \operatorname{Hilb}^{P_d}(k) = \mathbb{P}^N(k)$.

Lean: not in Lean as stated.

**Theorem P3.13.39 (Grothendieck; black box).** For every $P \in \mathbb{Q}[m]$, the functor $\operatorname{Hilb}^P_{\mathbb{P}^n}$ is represented by a projective scheme $\operatorname{Hilb}^P(\mathbb{P}^n)$ over $\mathbb{Z}$, the *Hilbert scheme*, with a universal family $\mathcal{Z} \subseteq \mathbb{P}^n \times \operatorname{Hilb}^P(\mathbb{P}^n)$. This is a black box, the row "Hilbert schemes" of the table in P0 Ch. 1, stated in P8 Ch. 1 with reference [Gro61].

Lean: not in Lean as stated.

### Proof in words

A family of hypersurfaces is locally the zero set of one form whose coefficients never vanish together. Such a form stays a nonzerodivisor after every base change, because a zero divisor of a polynomial ring is killed by a single scalar. So every fibre is a hypersurface of degree $d$, the graded pieces of the quotient have the expected rank on every fibre, and Nakayama's lemma turns this into local freeness. The form is determined by the subscheme up to a unit, so the coefficients of the local forms glue to an invertible sheaf with generating sections. That is a morphism to $\mathbb{P}^N$ by the universal property of projective space.

Over a field, a closed subscheme with the Hilbert polynomial of a hypersurface of degree $d$ is one: the greatest common divisor $G$ of its ideal cuts out a hypersurface, and the remaining factor of the ideal lives in codimension at least $2$, too small to affect the leading coefficient $d/(n-1)!$. For general $P$ Grothendieck's theorem constructs the Hilbert scheme as a closed subscheme of a Grassmannian; this handbook uses it as a black box.

### Examples

**Example P3.13.40 (conics).** For $n = 2$, $d = 2$, $N = 5$, and a conic is $a_{00} x_0^2 + a_{01} x_0 x_1 + a_{02} x_0 x_2 + a_{11} x_1^2 + a_{12} x_1 x_2 + a_{22} x_2^2$. The space of conics is $\mathbb{P}^5$, and by Proposition P3.13.38 it is also the set of $k$-points of $\operatorname{Hilb}^{2m+1}(\mathbb{P}^2)$. The families of Example P3.13.21 are morphisms $\operatorname{Spec} k[t]_{(t)} \to \mathbb{P}^5$: the smooth conics degenerate to a line pair at $[xy - tz^2]$ and to a double line at $[x^2 - tyz]$, two points of the closed subsets of singular conics and of double lines.

**Example P3.13.41 (points on the line).** For $n = 1$, $P_d(m) = (m + 1) - (m - d + 1) = d$ for $m \geq d$. By Proposition P3.13.38 a closed subscheme of $\mathbb{P}^1_k$ with constant Hilbert polynomial $d$ is $V_+(F)$ for a binary form of degree $d$. So $d$ points of $\mathbb{P}^1$ with multiplicities, a finite subscheme of length $d$, is a point of $\mathbb{P}^d$, the coefficients of $F$. Over an algebraically closed field $F = \prod_i (b_i x_0 - a_i x_1)$, and the map $(\mathbb{P}^1)^d \to \mathbb{P}^d$, $([a_i : b_i])_i \mapsto [F]$, is surjective with fibres the orbits of the symmetric group. Points collide when two factors agree, and the limit is a double root, still of length $d$: this is Example P3.13.10 in coordinates.

**Example P3.13.42 (lines).** A line in $\mathbb{P}^n_k$ has Hilbert polynomial $m + 1$ (Example P3.13.19). Example P3.13.30 gives a family of lines over $\operatorname{Gr}(2, n + 1)$, flat with fibres of polynomial $m + 1$, so it is an element of $\operatorname{Hilb}^{m+1}(\operatorname{Gr}(2, n + 1))$ and defines a morphism $\operatorname{Gr}(2, n + 1) \to \operatorname{Hilb}^{m+1}(\mathbb{P}^n)$ by Theorem P3.13.39. This morphism is an isomorphism; on $k$-points this says that a closed subscheme with Hilbert polynomial $m + 1$ is a line (Exercise 5). For $n = 3$ the lines in space form the Klein quadric of Example P3.13.29.

**Example P3.13.43 (twisted cubics).** A twisted cubic $C \subseteq \mathbb{P}^3_k$, the image of $\mathbb{P}^1$ by $[s : t] \mapsto [s^3 : s^2 t : s t^2 : t^3]$, has $h_C(m) = 3m + 1$, since the forms of degree $m$ restrict to the binary forms of degree $3m$. The twisted cubics form a family of dimension $12$: $15 = \dim \operatorname{PGL}_4$ minus $3 = \dim \operatorname{PGL}_2$. A plane cubic curve with a point added, not in its plane, has Hilbert polynomial $3m + 1$ as well, since the plane cubic has $3m$ by Example P3.13.18 and the point adds $1$ by part 4 of Lemma P3.13.13, and these form a family of dimension $3 + 9 + 3 = 15$, a plane, a cubic in it and a point. Piene and Schlessinger showed that $\operatorname{Hilb}^{3m+1}(\mathbb{P}^3)$ has exactly two irreducible components, of dimensions $12$ and $15$, which meet along a locus of dimension $11$: plane nodal cubics with an embedded point at the node, pointing out of the plane. So a Hilbert scheme need not be irreducible, and the component of the curves one cares about can be the smaller one.

**Example P3.13.44 (pairs of points in the plane).** A closed subscheme $Z \subseteq \mathbb{P}^2_k$ with Hilbert polynomial $2$ is finite of length $2$: two distinct points, or one point with a tangent direction, a double point $V(x, y^2)$ in local coordinates. The restriction $S_1 \to \Gamma(Z, \mathcal{O}_Z(1))$ has a kernel of dimension at least $3 - 2 = 1$, so $Z$ lies on a line $L$, and it is the unique line, since two lines meet in a point of length $1$. Inside $L \cong \mathbb{P}^1$, $Z$ is a point of $\operatorname{Hilb}^2(\mathbb{P}^1) = \mathbb{P}^2$ by Example P3.13.41. So the $k$-points of $\operatorname{Hilb}^2(\mathbb{P}^2)$ fibre over the dual plane of lines with fibres $\mathbb{P}^2$, of total dimension $4 = 2 \cdot 2$. The double points at one point $p$ form a $\mathbb{P}^1$, the directions at $p$ (Exercise 6).

### Proof

*Proof of Lemma P3.13.33.* First let $n = 0$, so $S_A = A[u]$, and write $F = \sum_{j=0}^{s} a_j u^j$. Choose $g \neq 0$ of minimal degree $e$ with $gF = 0$, with leading coefficient $b_e$. If $a_j g = 0$ for every $j$, then $b_e a_j = 0$ for every $j$, and $c = b_e$ has $cF = 0$. Otherwise let $j$ be the largest index with $a_j g \neq 0$. Then $0 = gF = g \sum_{i \leq j} a_i u^i$, and its coefficient of $u^{e + j}$ is $b_e a_j$, which is $0$. So $a_j g$ has degree less than $e$, and $(a_j g) F = a_j (gF) = 0$ with $a_j g \neq 0$, contradicting the minimality of $e$.

In general let $GF = 0$ with $G \neq 0$, and choose an integer $D$ larger than the degree of $F$ and of $G$ in each variable. The ring map $\sigma \colon S_A \to A[u]$, $x_i \mapsto u^{D^i}$, maps the monomials of degree less than $D$ in each variable to distinct powers of $u$, by uniqueness of the base $D$ expansion. So $\sigma(G) \neq 0$, $\sigma(G)\sigma(F) = 0$, and the first step gives $c \neq 0$ with $c \sigma(F) = 0$. The coefficients of $\sigma(F)$ are the coefficients of $F$, so $cF = 0$. If $F$ has unit content and $cF = 0$, then $c$ kills the ideal generated by the coefficients, which is $A$, so $c = 0$. $\square$

*Proof of Lemma P3.13.34.* Let $v_1, \dots, v_a$ be the images of the standard basis. Their classes in $\kappa^b$ are linearly independent, so there are $w_{a+1}, \dots, w_b \in A^b$ such that the classes of $v_1, \dots, v_a, w_{a+1}, \dots, w_b$ form a basis of $\kappa^b$. The map $\psi \colon A^a \oplus A^{b - a} \to A^b$ that sends the standard basis to these elements is surjective modulo $\mathfrak{m}$, hence surjective by Nakayama's lemma (Theorem P1.1.25). A surjective endomorphism of the finitely generated module $A^b$ is an isomorphism (Theorem P1.1.27), so $\psi$ is an isomorphism. It restricts to $\varphi$ on $A^a$, so $\varphi$ is injective, and $\operatorname{coker} \varphi \cong A^{b - a}$. $\square$

*Proof of Proposition P3.13.35.* Part 1. The coefficients of $F_B$ are the images of the coefficients of $F$, and they generate the image of the unit ideal. The second claim is part 2 of Lemma P3.13.13 with $I = (F)$.

Part 2. Multiplication by $F$ is a homomorphism $\mu \colon (S_A)_{m-d} \to (S_A)_m$ of free modules of ranks $\binom{m - d + n}{n}$ and $\binom{m + n}{n}$, with cokernel $(S_A/(F))_m$. Let $\mathfrak{p}$ be a prime of $A$. The coefficients of $F$ generate $A$, so they are not all in $\mathfrak{p}$, and the image $\bar F$ of $F$ in $\kappa(\mathfrak{p})[x]$ is nonzero. As $\kappa(\mathfrak{p})[x]$ is a domain, $\mu \otimes \kappa(\mathfrak{p})$ is injective. By Lemma P3.13.34 over $A_\mathfrak{p}$, $(S_A/(F))_m \otimes A_\mathfrak{p}$ is free of rank $P_d(m)$. A module whose localizations are all flat is flat (Proposition P3.13.2).

Part 3. The chart $Z \cap D_+(x_i)$ is $\operatorname{Spec} (S_A/(F))_{(x_i)}$, and $(S_A/(F))_{(x_i)}$ is the filtered colimit of the modules $(S_A/(F))_m$ along multiplication by $x_i$, through $a \mapsto a/x_i^m$. For an injective map $N' \to N$ of $A$-modules, $(S_A/(F))_{(x_i)} \otimes N' \to (S_A/(F))_{(x_i)} \otimes N$ is the colimit of injective maps, since tensor products commute with colimits (Proposition P2.1.44), and it is injective since filtered colimits are exact (Proposition P2.1.46). So every chart is flat over $A$, and $Z$ is flat. By part 1, $Z_\mathfrak{p} = V_+(\bar F)$ with $\bar F \neq 0$ of degree $d$, which has Hilbert polynomial $P_d$ by Example P3.13.17.

Part 4. On $D_+(x_i) = \operatorname{Spec} A_i$, $A_i = A[x_0/x_i, \dots, x_n/x_i]$, the ideal of $Z$ is generated by $f_i = F/x_i^d$, and that of $V_+(G)$ by $g_i = G/x_i^d$. The element $f_i$ is a nonzerodivisor of $A_i$, since $F$ is a nonzerodivisor of $S_A$ by Lemma P3.13.33, hence of the localization $(S_A)_{x_i}$, and $A_i$ is a subring of it. As the ideals agree, $g_i = h_i f_i$ for a unique $h_i \in A_i$. On $D_+(x_i x_j)$, $f_j = (x_i/x_j)^d f_i$ and $g_j = (x_i/x_j)^d g_i$, so $h_j f_i = g_i = h_i f_i$, and $h_i = h_j$ there as $f_i$ is a nonzerodivisor. They glue to $h \in \Gamma(\mathbb{P}^n_A, \mathcal{O}) = A$ (Theorem P3.6.12), and $G = hF$, since this holds in each $(S_A)_{x_i}$ and $S_A \to (S_A)_{x_0}$ is injective. In the same way $F = h' G$, so $F = h h' F$, and $hh' = 1$ because $F$ is a nonzerodivisor. $\square$

*Proof of Theorem P3.13.37.* Let $Z \in \mathbf{H}_d(T)$ with cover $T_i = \operatorname{Spec} A_i$ and forms $F_i$. For an affine open $W \subseteq T_i \cap T_j$, Proposition P3.13.35 (parts 1 and 4, over $\mathcal{O}(W)$) gives a unique unit $u \in \mathcal{O}(W)^\times$ with $F_j|_W = u F_i|_W$. By uniqueness these units glue to $u_{ij} \in \Gamma(T_i \cap T_j, \mathcal{O})^\times$ with $F_j = u_{ij} F_i$, and $u_{ik} = u_{jk} u_{ij}$ on triple overlaps, since $F$ is a nonzerodivisor. Glue the sheaves $\mathcal{O}_{T_i}$ along multiplication by $u_{ij}$ (Theorem P2.5.35) to an invertible sheaf $\mathcal{L}$, in which the coefficients $(F_i)_\alpha$ glue to global sections $s_\alpha$. At each point some coefficient of $F_i$ is a unit of the local ring, because the coefficients generate the unit ideal of $A_i$, so the $s_\alpha$ generate $\mathcal{L}$. By Theorem P3.6.21 they define $\varphi_Z \colon T \to \mathbb{P}^N_\mathbb{Z}$. A different choice of cover and forms gives an isomorphic pair $(\mathcal{L}, (s_\alpha))$: on a common refinement the forms differ by units, again by part 4 of Proposition P3.13.35, and these units define the isomorphism. So $\varphi_Z$ depends only on $Z$, by part 3 of Theorem P3.6.21.

Conversely let $\varphi \colon T \to \mathbb{P}^N$ correspond to $(\mathcal{L}, (s_\alpha))$. On an affine open $T_i = \operatorname{Spec} A_i$ with a trivialization $\mathcal{L}|_{T_i} \cong \mathcal{O}_{T_i}$, the $s_\alpha$ become elements of $A_i$ that generate it, and $F_i = \sum_\alpha s_\alpha x^\alpha$ has unit content. A different trivialization multiplies $F_i$ by a unit, which does not change $V_+(F_i)$. So the $V_+(F_i)$ agree on overlaps and glue to $Z_\varphi \in \mathbf{H}_d(T)$. The two constructions are inverse to each other, and both are compatible with pullback, as the pullback of $V_+(F_i)$ is $V_+$ of the pulled back form by part 1 of Proposition P3.13.35. For $T = \mathbb{P}^N$ and $\varphi$ the identity, $(\mathcal{L}, s_\alpha) = (\mathcal{O}(1), a_\alpha)$, and on $D_+(a_\beta)$ the trivialization by $a_\beta$ gives the form $\sum_\alpha (a_\alpha/a_\beta) x^\alpha$, whose coefficient of $x^\beta$ is $1$. So $Z_{\mathrm{id}} = \mathcal{Z}$ is the universal family. $\square$

*Proof of Proposition P3.13.38.* Let $S = k[x_0, \dots, x_n]$ and $I = I_X$, a saturated ideal. If $I = 0$, then $X = \mathbb{P}^n_k$ and $P_X$ has degree $n$, while $P_d$ has degree $n - 1$. So $I \neq 0$. Let $G$ be a greatest common divisor of the nonzero elements of $I$ in the factorial ring $S$. It is homogeneous of some degree $e \geq 0$, since the homogeneous components of an element of $I$ lie in $I$. Let $J = \{h \in S : Gh \in I\}$, a homogeneous ideal with $I = GJ$, because every element of $I$ is divisible by $G$. The nonzero elements of $J$ have no common factor other than units. The ideal $J$ is saturated: if $x_i^l h \in J$ for all $i$, then $x_i^l G h \in I$ for all $i$, so $Gh \in I$ and $h \in J$.

Let $\mathfrak{p}$ be a prime that contains $J$. If $\operatorname{ht} \mathfrak{p} = 1$, then $\mathfrak{p} = (f)$ for a prime element $f$ by Proposition P1.5.23, and $f$ divides every element of $J$, which is impossible. So $\operatorname{ht} \mathfrak{p} \geq 2$ and $\dim S/\mathfrak{p} \leq n - 1$ by Corollary P1.5.42, for every prime that contains $J$. Hence $\dim S/J \leq n - 1$, and the Hilbert polynomial $P_{S/J}$ has degree at most $n - 2$ by Theorem P1.13.16.

Multiplication by $G$ gives an exact sequence of graded modules
$$
0 \to (S/J)(-e) \xrightarrow{G} S/I \to S/(G) \to 0,
$$
since $(G)/I = (G)/GJ \cong (S/J)(-e)$, as $G$ is a nonzerodivisor. So $P_d(m) = P_X(m) = P_e(m) + P_{S/J}(m - e)$, with $P_e = 0$ for $e = 0$. The polynomial $P_e$ has degree $n - 1$ and leading coefficient $e/(n-1)!$ for $e \geq 1$, by Example P3.13.17, and $P_d$ has leading coefficient $d/(n-1)!$. As $P_{S/J}$ has degree at most $n - 2$, comparing coefficients of $m^{n-1}$ gives $e = d$, and then $P_{S/J} = 0$. So $(S/J)_m = 0$ for large $m$, $x_i^m \in J$ for all $i$, and $1 \in J$ as $J$ is saturated. Hence $I = (G)$ and $X = V_+(G)$, with $G$ of degree $d$. If $V_+(G) = V_+(G')$, part 4 of Proposition P3.13.35 over $k$ gives $G' = uG$. So $\operatorname{Hilb}^{P_d}(k) = \mathbf{H}_d(k)$, which is $\mathbb{P}^N(k)$ by Theorem P3.13.37. $\square$

### Exercises

1. (A) Show that $\mathbf{H}_1 \cong \mathbb{P}^n_\mathbb{Z}$, the space of hyperplanes, and identify it with $\operatorname{Gr}(n, n + 1)$ using Exercise 3 of Section 13.3.
2. (A) Over $A = k[t]$, show that $t x_0 + (1 - t) x_1$ has unit content and $t x_0$ does not. Compare the fibres of $V_+(t x_0)$ over $t = 0$ and $t = 1$ with Example P3.13.22.
3. (A) Show that $F \in (S_A)_d$ has unit content if and only if its image in $\kappa(\mathfrak{p})[x]$ is nonzero for every prime $\mathfrak{p}$ of $A$.
4. (B) Let $k$ be a field of characteristic not $2$. Write a conic as $x^{\mathsf{T}} M x$ with $M$ symmetric. Show that the singular conics form the cubic hypersurface $V_+(\det M) \subseteq \mathbb{P}^5_k$, and that the double lines form the image of the Veronese map $\mathbb{P}^2 \to \mathbb{P}^5$, $\ell \mapsto \ell^2$, a surface.
5. (B) Let $k$ be a field and $X \subseteq \mathbb{P}^n_k$ a closed subscheme with $P_X = m + 1$. Show that $X$ is a line. (Let $L$ be the union of the components of $X$ of dimension $1$, with the reduced structure. Show that $L$ is a line, using the leading coefficient $1$. Then $I_X \subseteq I_L$, the Hilbert polynomial of $I_L/I_X$ is $P_X - P_L = 0$, and $I_X$ is saturated, so $I_X = I_L$.)
6. (B) Let $p = [0 : 0 : 1] \in \mathbb{P}^2_k$. Show that the closed subschemes of length $2$ supported at $p$ have ideals $(a x_0 + b x_1) + (x_0, x_1)^2$ in the local coordinates $x_0, x_1$ at $p$, with $[a : b] \in \mathbb{P}^1(k)$, so that they form a $\mathbb{P}^1$, the directions at $p$.

### Lean

Nothing in this section is in Lean as stated. Mathlib's `Polynomial.hilbertPoly` (Section 13.2) is the algebraic part of the Hilbert polynomial, and the Hilbert functor, families of hypersurfaces and Hilbert schemes are not in Mathlib. mmp-lean uses the Hilbert scheme only through the black box of Theorem P3.13.39, whose Lean hypothesis is not yet named in the table of P0 Ch. 1. The handbook adds no `MinimalModel` node here.

### Notes and history

The space $\mathbb{P}^N$ of hypersurfaces is classical: the conics through five general points, one point of $\mathbb{P}^5$ cut out by five hyperplanes, are a nineteenth-century computation in this space. Grothendieck constructed Hilbert schemes in his Séminaire Bourbaki talk of 1961 [Gro61], by embedding $\operatorname{Hilb}^P$ in a Grassmannian of quotients of $\Gamma(\mathbb{P}^n, \mathcal{O}(m))$ for large $m$, with Mumford's regularity bound in his later lectures on curves on surfaces giving a uniform $m$. Lemma P3.13.33 is McCoy's theorem (1942). The twisted cubics are the work of Piene and Schlessinger (1985). Hartshorne proved in 1966 that $\operatorname{Hilb}^P(\mathbb{P}^n_k)$ is connected. The literature state is theorem.

The Hilbert scheme and the Hom scheme, an open subscheme of a Hilbert scheme, are the black box of P8 Ch. 1, and the program uses them to deform curves, as in the bend and break arguments.
