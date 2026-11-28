---
title: Cones of blow-ups, ruled surfaces and del Pezzo surfaces
nodes: []
sources: [Laz04, Deb01, Har77]
reads_with: [Laz04:1.5, Deb01:ch1]
requires: [P3.6, P3.11, P4.6, P5.9, P5.10, P5.12, P7.1, P7.2, P7.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Cones of blow-ups, ruled surfaces and del Pezzo surfaces

### Statement

This section computes the three cones $\overline{NE}$, $\operatorname{Nef}$ and $\overline{\operatorname{Eff}}$ of the basic examples, together with the morphisms that cut out the faces. On a smooth projective surface, $N_1 = N^1$ by Proposition P7.2.8, curves are effective divisors, and $\operatorname{Eff} = NE$ by part 3 of Proposition P7.4.15, so the surface examples have two cones to compute, $\overline{NE}$ and its dual $\operatorname{Nef}$. A class in the coordinates of a basis is written by its coefficients.

**Proposition P7.4.18 (the blow-up of projective space at a point).** Let $\pi \colon \tilde X = \operatorname{Bl}_p \mathbb{P}^n \to \mathbb{P}^n$, $n \geq 2$, with $H$, $E$, $e$, $\tilde\ell_p$ as in Example P7.2.25, and let $q \colon \tilde X \to \mathbb{P}^{n-1}$ be the projection from $p$, with $q^* \mathcal{O}(1) = H - E$ (Example P7.1.26). Write classes in $N^1(\tilde X)$ as $xH - yE$.

1. $NE(\tilde X) = \overline{NE}(\tilde X) = \langle [e], [\tilde\ell_p] \rangle$ and $\operatorname{Nef}(\tilde X) = \langle H, H - E \rangle = \{ 0 \leq y \leq x \}$.
2. $\operatorname{Eff}(\tilde X) = \overline{\operatorname{Eff}}(\tilde X) = \langle E, H - E \rangle = \{ x \geq 0, \ y \leq x \}$, which strictly contains $\operatorname{Nef}(\tilde X)$. The divisor $E$ is effective and not nef.
3. The faces of $\overline{NE}(\tilde X)$ other than $\{0\}$ and $\overline{NE}(\tilde X)$ are $F_\pi = \mathbb{R}_{\geq 0} [e]$ and $F_q = \mathbb{R}_{\geq 0} [\tilde\ell_p]$.

Lean: not in Lean as stated.

**Proposition P7.4.19 (the Hirzebruch surfaces).** Let $n \geq 1$ and $\mathbb{F}_n$ with $C_-$, $C_+$, $F$ as in Proposition P7.2.24, $q \colon \mathbb{F}_n \to \mathbb{P}^1$ the ruling, and $\varphi$ the morphism defined by the globally generated line bundle $\mathcal{O}(C_+)$.

1. $C_+ \equiv C_- + nF$, and $C_-^2 = -n$, $C_- \cdot F = 1$, $F^2 = 0$.
2. $NE(\mathbb{F}_n) = \overline{NE}(\mathbb{F}_n) = \operatorname{Eff}(\mathbb{F}_n) = \langle C_-, F \rangle$ and $\operatorname{Nef}(\mathbb{F}_n) = \langle F, C_+ \rangle$, which is strictly smaller.
3. $F_q = \mathbb{R}_{\geq 0} [F]$, and $F_\varphi = \mathbb{R}_{\geq 0} [C_-]$: the morphism $\varphi$ contracts the curve $C_-$ and no other curve. For $n = 1$, $\varphi$ can be taken to be the blow-down $\mathbb{F}_1 \to \mathbb{P}^2$.

Lean: not in Lean as stated.

**Proposition P7.4.20 (the plane blown up at two points).** Let $S = \operatorname{Bl}_{q_1, q_2} \mathbb{P}^2$, with $H$, $E_1$, $E_2$ as in Example P7.2.26 and $L_{12}$ the strict transform of the line through $q_1$ and $q_2$. Write classes as $xH - y_1 E_1 - y_2 E_2$.

1. $NE(S) = \overline{NE}(S) = \operatorname{Eff}(S) = \langle E_1, E_2, L_{12} \rangle$, a simplicial cone.
2. $\operatorname{Nef}(S) = \langle H, H - E_1, H - E_2 \rangle = \{ y_1 \geq 0, \ y_2 \geq 0, \ x \geq y_1 + y_2 \}$, and a class is ample if and only if the three inequalities are strict.
3. The three two-dimensional faces of $\overline{NE}(S)$ are the faces of morphisms: $\langle E_1, E_2 \rangle = F_\pi$ for the blow-down $\pi \colon S \to \mathbb{P}^2$, and $\langle L_{12}, E_2 \rangle$ and $\langle L_{12}, E_1 \rangle$ are the faces of the morphisms $S \to \mathbb{P}^1$ given by the pencils of lines through $q_1$ and through $q_2$. The three extremal rays are cut out by $2H - E_2$, $2H - E_1$ and $2H - E_1 - E_2$.

Lean: not in Lean as stated.

**Proposition P7.4.21 (del Pezzo surfaces).** Let $S_r$ be the blow-up of $\mathbb{P}^2$ at $r$ points in general position, $2 \leq r \leq 8$. Then
$$NE(S_r) = \overline{NE}(S_r) = \sum_{C} \mathbb{R}_{\geq 0} [C],$$
the sum over the finitely many $(-1)$-curves $C$ of Theorem P5.9.26, each of which spans an extremal ray. So $\overline{NE}(S_r)$ is polyhedral with $3, 6, 10, 16, 27, 56, 240$ extremal rays for $r = 2, \dots, 8$, $\operatorname{Nef}(S_r)$ is the polyhedral cone of the classes $\delta$ with $\delta \cdot C \geq 0$ for every $(-1)$-curve $C$, and $\delta$ is ample if and only if $\delta \cdot C > 0$ for every $(-1)$-curve $C$.

Lean: not in Lean as stated.

### Proof in words

In each example the cone of curves is bounded from inside by explicit curves and from outside by explicit nef classes, and the two bounds meet. The nef classes are pullbacks of ample classes by morphisms, a blow-down, a projection or a ruling, so they are nef and the face each one cuts out is the set of classes of the curves the morphism contracts. Duality then determines the nef cone from the cone of curves. For the effective cone of $\operatorname{Bl}_p \mathbb{P}^n$ the outer bound comes from the two covering families of lines of part 2 of Proposition P7.4.15. For del Pezzo surfaces the cone theorem for surfaces does the work: $-K$ is ample, so $\overline{NE}$ has no $K$-nonnegative part, and every extremal ray is spanned by a $(-1)$-curve, of which there are finitely many.

### Examples

**Example P7.4.22 (nine points: infinitely many rays).** Let $X$ be the blow-up of the nine base points of a pencil of plane cubics satisfying the hypothesis of Theorem P5.10.21. By Example P5.12.18, $X$ contains infinitely many $(-1)$-curves, and each spans an extremal ray of $\overline{NE}(X)$ by Lemma P5.12.11. Distinct $(-1)$-curves $C \neq C'$ have $C \cdot C' \geq 0 > C'^2$, so their classes are not proportional, and $\overline{NE}(X)$ has infinitely many extremal rays: it is not polyhedral, by part 2 of Proposition P7.4.4. By Theorem P5.10.23, $\operatorname{Nef}(X)$ is not polyhedral either, which also follows from the first statement and part 3 of Proposition P7.4.4, since the dual of a polyhedral cone is polyhedral and $\overline{NE}(X) = \operatorname{Nef}(X)^\vee$ by Theorem P7.4.9. Here $-K$ is the class of a fibre of the elliptic fibration $X \to \mathbb{P}^1$ given by the pencil, so it is nef with $K^2 = 0$ and it is not ample, and the extremal rays accumulate only on the hyperplane $K^\perp$ by part 3 of Theorem P5.12.14. In Proposition P7.4.21 the class $-K$ is ample and the cone is polyhedral; here $-K$ is nef and not ample, and the cone has infinitely many extremal rays.

**Example P7.4.23 (two surfaces with an elliptic factor).** Let $E$ be an elliptic curve. On $S = E \times \mathbb{P}^1$, with the classes $s$ and $f$ of Example P7.2.27, Example P5.12.19 gives $\overline{NE}(S) = \operatorname{Nef}(S) = \langle s, f \rangle$, and both $s$ and $f$ are classes of curves, so $NE(S) = \overline{NE}(S) = \operatorname{Eff}(S)$. The boundary rays are the faces of the projections: $f$ is the class of the fibres $\{x\} \times \mathbb{P}^1$, contracted by $p_1$, so $F_{p_1} = \mathbb{R}_{\geq 0} f$ by part 3 of Proposition P7.4.11, and similarly $F_{p_2} = \mathbb{R}_{\geq 0} s$. On $E \times E$, Example P5.12.9 gives $\overline{NE} = \operatorname{Nef} = \overline{\operatorname{Eff}} = \{ x : x^2 \geq 0, \ x \cdot H \geq 0 \}$, a round cone of the type of Example P7.4.7 in $N^1(E \times E)$ of dimension $\rho \geq 3$, with every boundary ray extremal, so neither cone is polyhedral. The ample cone is its interior $\{ x^2 > 0, x \cdot H > 0 \}$, and every boundary class is nef and not ample. In both surfaces the nef cone equals the closed cone of curves: the intersection form is nonnegative on curves, since no curve has negative square.

**Example P7.4.24 (Mumford's cones).** Let $X = \mathbb{P}(\mathcal{E})$ be the ruled surface of Example P7.3.24, with $\xi = \mathcal{O}_X(1)$ and fibre class $f$. By part 2 of Theorem P5.9.4, $N^1(X)$ has basis $\xi$, $f$ with $\xi^2 = 0$, $\xi \cdot f = 1$ and $f^2 = 0$. For $\delta = a \xi + b f$, $\delta \cdot \xi = b$ and $\delta \cdot f = a$.

1. Every curve $C'$ has class $a \xi + b f$ with $a \geq 0$ and $b > 0$. A fibre has class $f$. Otherwise, by part 2 of Example P7.3.24 and its proof, $[C'] = d \xi + (\deg \mathcal{M}) f$ with $d \geq 1$ and $\deg \mathcal{M} > 0$. So
$$NE(X) \subseteq \{ 0 \} \cup \{ a \xi + b f : a \geq 0, \ b > 0 \}.$$
2. $\xi$ and $f$ are nef, by part 2 of Example P7.3.24 for $\xi$ and since $f \cdot C' = a \geq 0$ for every curve, so $\operatorname{Nef}(X) = \langle \xi, f \rangle = \{ a, b \geq 0 \}$: a class $a\xi + bf$ is nef if and only if it is nonnegative on $f$ and on $\xi \in \overline{NE}(X)$, and $[\xi] \in \overline{NE}(X)$ by part 2 of Proposition P7.3.21.
3. By Theorem P7.4.9, $\overline{NE}(X) = \operatorname{Nef}(X)^\vee = \langle \xi, f \rangle = \overline{\operatorname{Eff}}(X)$, the same closed quadrant, and $\delta$ is ample if and only if $a > 0$ and $b > 0$.
4. The extremal ray $\mathbb{R}_{\geq 0} \xi$ of $\overline{NE}(X)$ is the face cut out by the nef class $\xi$, and by part 1 it contains no nonzero point of $NE(X)$. So $NE(X)$ is not closed, $\xi$ is not the class of an effective $\mathbb{R}$-divisor, and the face $F_\xi$ contains no curve.
5. No positive multiple of $\xi$ is generated by global sections, and no positive multiple $m\xi$ is numerically equivalent to $g^* A$ for a morphism $g \colon X \to Y$ to a projective scheme and $A$ ample. Indeed, if $m \xi \equiv g^* A$, then $g$ is not finite, since $m\xi$ is not ample (part 1 of Proposition P7.3.21) and part 5 of Proposition P7.3.9 applies. So some fibre of $g$ is not finite, by Corollary P4.6.17, and it contains a curve $C$, since an irreducible component of positive dimension of that fibre contains an irreducible closed subset of dimension $1$, the second term of a maximal chain of irreducible closed subsets (Hartshorne, Exercise II.3.20, in Har77). By part 3 of Proposition P7.4.11, $0 \neq [C] \in F_g = \overline{NE}(X) \cap (m\xi)^\perp = \mathbb{R}_{\geq 0} \xi$, which contradicts part 4. If $\xi^m$ were globally generated, part 6 of Proposition P7.4.11 would give such a morphism with $g^* \mathcal{O}(1) \cong \xi^m$.

So $\xi$ is nef, not ample, not effective, and not semiample: a nef class on the boundary of $\operatorname{Nef}(X)$ that comes from no morphism. In the examples with a polyhedral cone above, every boundary ray of $\operatorname{Nef}$ is the class of a morphism, and the minimal model program needs, and proves, this for the boundary classes that it uses.

### Proof

*Proposition P7.4.18.* Part 1 is Example P7.3.16. Part 2. The divisor $E$ is effective, and $H - E = q^* \mathcal{O}(1)$ is globally generated, so it has a nonzero section and is effective; so $\langle E, H - E \rangle \subseteq \operatorname{Eff}(\tilde X)$. For the other inclusion, apply part 2 of Proposition P7.4.15 to two families of curves. The strict transforms $\tilde\ell_p$ of the lines through $p$ all have the class $[\tilde\ell_p]$ (Example P7.2.25), and their union contains $\tilde X \setminus E$, since every point of $\mathbb{P}^n \setminus \{p\}$ lies on a line through $p$; this set is dense. The preimages $\ell$ of the lines not through $p$ all have the class $[\ell]$, and their union is $\tilde X \setminus E$. Since $(xH - yE) \cdot \tilde\ell_p = x - y$ and $(xH - yE) \cdot \ell = x$ by Example P7.2.25, every pseudo-effective class has $x \geq 0$ and $x - y \geq 0$. A class with these properties satisfies $xH - yE = x (H - E) + (x - y) E$ with $x, x - y \geq 0$, so it lies in $\langle E, H - E \rangle$. Hence $\operatorname{Eff}(\tilde X) = \overline{\operatorname{Eff}}(\tilde X) = \langle E, H - E \rangle$. The class $E$ is not nef, since $E \cdot e = -1$, so the inclusion $\operatorname{Nef} \subseteq \operatorname{Eff}$ is strict.

Part 3. A two-dimensional cone has exactly four faces: $\{0\}$, its two boundary rays, and itself (Example P7.4.6). By Example P7.2.25, $H \cdot e = 0$ and $H \cdot \tilde\ell_p = 1$, so by part 2 of Proposition P7.4.11 with $A = \mathcal{O}(1)$, $F_\pi = \overline{NE} \cap H^\perp = \mathbb{R}_{\geq 0}[e]$. Similarly $(H - E) \cdot e = 1$ and $(H - E) \cdot \tilde\ell_p = 0$, so $F_q = \mathbb{R}_{\geq 0} [\tilde\ell_p]$.

*Proposition P7.4.19.* Part 1. By Proposition P7.2.24, $F \cdot C_- = 1$, $F \cdot F = 0$, $C_+ \cdot C_- = 0$ and $C_+ \cdot F = 1$, and $C_-^2 = -n$ by Example P5.12.8. The class $C_- + nF$ has the same intersection numbers with the basis $[C_-]$, $[F]$ as $C_+$, namely $-n + n = 0$ and $1$, so $C_+ \equiv C_- + nF$ since the pairing is perfect.

Part 2. The cones of curves and the nef cone are Example P7.3.17, and $\operatorname{Eff} = NE$ by part 3 of Proposition P7.4.15. The class $C_- \in \operatorname{Eff}$ is not nef, since $C_- \cdot C_- = -n < 0$.

Part 3. The ruling $q$ satisfies $q^* \mathcal{O}(1) = \mathcal{O}(F)$, a fibre being the preimage of a point. By part 2 of Proposition P7.4.11, $F_q = \overline{NE} \cap F^\perp$, and a class $\alpha [C_-] + \beta [F]$ has $F \cdot (\alpha C_- + \beta F) = \alpha$, so $F_q = \mathbb{R}_{\geq 0} [F]$. The line bundle $\mathcal{O}(C_+)$ is globally generated (proof of Proposition P7.2.24), so part 6 of Proposition P7.4.11 applies: $F_\varphi = \overline{NE} \cap C_+^\perp$, and $C_+ \cdot (\alpha C_- + \beta F) = \beta$, so $F_\varphi = \mathbb{R}_{\geq 0} [C_-]$, and $\varphi$ contracts a curve $C$ if and only if $C_+ \cdot C = 0$. Such a curve has class $\alpha [C_-]$ with $\alpha = F \cdot C \geq 1$, so $C \cdot C_- = -n \alpha < 0$, while distinct curves have nonnegative intersection by Proposition P5.5.5. So $C = C_-$. For $n = 1$, the blow-down $\pi \colon \mathbb{F}_1 \cong \operatorname{Bl}_p \mathbb{P}^2 \to \mathbb{P}^2$ of Theorem P3.11.26 satisfies $\pi^* \mathcal{O}(1) = \mathcal{O}(C_+)$ by the same theorem, which sends $\pi^* V_+(z)$ to $C_+$, so it is a morphism of the kind in part 6 of Proposition P7.4.11.

*Proposition P7.4.20.* Part 1 is Example P5.12.17, with $\operatorname{Eff} = NE$ by part 3 of Proposition P7.4.15, and the cone is simplicial because $E_1$, $E_2$, $L_{12} = H - E_1 - E_2$ form a basis of $N^1(S)$.

Part 2. By Example P7.2.26, $H^2 = 1$, $E_i^2 = -1$, and $H \cdot E_i = E_1 \cdot E_2 = 0$. For $\delta = xH - y_1E_1 - y_2E_2$,
$$\delta \cdot E_1 = y_1, \qquad \delta \cdot E_2 = y_2, \qquad \delta \cdot L_{12} = x - y_1 - y_2.$$
By Theorem P7.4.9 and Example P7.4.6, $\operatorname{Nef}(S)$ is the simplicial cone spanned by the basis dual to $E_1, E_2, L_{12}$. That basis is $H - E_1$, $H - E_2$, $H$, since $(H - E_1) \cdot (E_1, E_2, L_{12}) = (1, 0, 0)$, $(H - E_2) \cdot (E_1, E_2, L_{12}) = (0, 1, 0)$ and $H \cdot (E_1, E_2, L_{12}) = (0, 0, 1)$. The ample cone is the interior, by part 3 of Theorem P7.4.9.

Part 3. The class $H = \pi^* \mathcal{O}(1)$ vanishes on $E_1$, $E_2$ and is positive on $L_{12}$, so $F_\pi = \langle E_1, E_2 \rangle$ by part 2 of Proposition P7.4.11. Let $\pi_2 \colon S \to \operatorname{Bl}_{q_1} \mathbb{P}^2$ be the blow-down of $E_2$ and $q_1' \colon \operatorname{Bl}_{q_1} \mathbb{P}^2 \to \mathbb{P}^1$ the projection from $q_1$, with $q_1'^* \mathcal{O}(1) = H - E$ (Example P7.1.26). The point $q_2$ does not lie on the exceptional curve over $q_1$, so $\pi_2^* E = E_1$ and $\pi_2^* H = H$, and the composite $S \to \mathbb{P}^1$ pulls $\mathcal{O}(1)$ back to $H - E_1$, which vanishes on $L_{12}$ and $E_2$ and is positive on $E_1$; so its face is $\langle L_{12}, E_2 \rangle$. The pencil through $q_2$ is symmetric. Finally $2H - E_2 = H + (H - E_2)$ vanishes on $E_1$ and is positive on $E_2$ and $L_{12}$, with values $1$ and $1$, so it cuts out $\mathbb{R}_{\geq 0} E_1$; similarly for $2H - E_1$; and $2H - E_1 - E_2 = (H - E_1) + (H - E_2)$ has values $1, 1, 0$ on $E_1, E_2, L_{12}$, so it cuts out $\mathbb{R}_{\geq 0} L_{12}$. Each of these rays is spanned by a $(-1)$-curve, and its contraction, a blow-down to a smooth surface, exists by part 1 of Theorem P5.12.15.

*Proposition P7.4.21.* By part 1 of Theorem P5.9.26 and Definition P5.9.24, $-K$ is ample on $S_r$. By Theorem P7.3.13, $-K \cdot z > 0$ for every $z \in \overline{NE}(S_r) \setminus \{0\}$, so $\overline{NE}(S_r)_{K \geq 0} = \{0\}$, and part 1 of Theorem P5.12.14 gives $\overline{NE}(S_r) = \sum_{i \in I} \mathbb{R}_{\geq 0} [C_i]$ over the $K$-negative extremal rays $R_i$. By Theorem P5.12.15, each $R_i$ is spanned by a curve $C_i \cong \mathbb{P}^1$ of one of three types. Types 2 and 3 have $\rho(S_r) \leq 2$, while $\rho(S_r) = r + 1 \geq 3$ by Example P7.2.26, so every $C_i$ is a $(-1)$-curve. Conversely, every $(-1)$-curve $C$ has $C^2 < 0$, so it spans an extremal ray by Lemma P5.12.11, which is $K$-negative since $K \cdot C = -1$. By part 2 of Theorem P5.9.26 there are finitely many $(-1)$-curves, with the numbers stated for $r = 2, \dots, 8$, and distinct $(-1)$-curves span distinct rays, as in Example P7.4.22. So $\overline{NE}(S_r)$ is the polyhedral cone they span, it is contained in $NE(S_r)$, and $NE(S_r) = \overline{NE}(S_r)$. The nef cone is its dual by Theorem P7.4.9, polyhedral by part 3 of Proposition P7.4.4, and the ample cone is the set of classes positive on the generators, by Theorem P7.3.13, since a class positive on finitely many generators is positive on $\overline{NE}(S_r) \setminus \{0\}$.

### Exercises

1. (A) On $\operatorname{Bl}_p \mathbb{P}^n$, find the classes $xH - yE$ that are effective and not nef, and those that are nef and not ample, and for each nef class on the boundary name the morphism whose pullback of $\mathcal{O}(1)$ it is, up to a positive multiple.
2. (A) On $\mathbb{F}_n$, write $-K = 2C_- + (n + 2)F$, use Proposition P7.4.19 to find for which $n$ the class $-K$ is ample and for which it is nef, and compare with Definition P5.9.24.
3. (B) For $S_3$, the plane blown up at three non-collinear points, list the six $(-1)$-curves and their classes, check that $\overline{NE}(S_3)$ has six extremal rays, and find the extremal rays of $\operatorname{Nef}(S_3)$, showing that there are five of them, among them $H$, $H - E_i$ and $2H - E_1 - E_2 - E_3$.
4. (B) Let $X = \operatorname{Bl}_p \mathbb{P}^a \times \mathbb{P}^b$, the blow-up of a point of $\mathbb{P}^a \times \mathbb{P}^b$, with $a, b \geq 1$. Find $\overline{NE}(X)$ and $\operatorname{Nef}(X)$ in the basis $H_1$, $H_2$, $E$, and show that $\overline{NE}(X)$ has three extremal rays.
5. (B) In Example P7.4.24, show directly that $\overline{NE}(X) \neq NE(X)$ by proving that the ray $\mathbb{R}_{\geq 0} \xi$ is a limit of rays of curves, using the classes $d \xi + g f$ of effective divisors, which exist for every $d \geq 1$ by Riemann-Roch on $C$ applied to $\operatorname{Sym}^d \mathcal{E} \otimes \mathcal{M}$ with $\deg \mathcal{M} = g$.
6. (C) Let $X$ be a smooth projective surface with $\overline{NE}(X)$ polyhedral and spanned by classes of curves. Show that every nef class is a nonnegative combination of finitely many nef classes $\delta_1, \dots, \delta_s$, each of which cuts out a face of $\overline{NE}(X)$ spanned by curves, and explain why Example P7.4.24 shows that the hypothesis that the generators be classes of curves cannot be dropped.

### Lean

The project library has no blow-ups, projective bundles or ruled surfaces, and its cones `MinimalModel.nefCone`, `MinimalModel.effCone` and `MinimalModel.IntersectionData.coneOfCurves` are defined for an abstract `IntersectionData`, so none of the computations of this section is stated there. Mathlib has no intersection theory on surfaces. The handbook adds no `MinimalModel` node here.

### Notes and history

The cones of the plane blown up at up to eight points in general position are classical, and their symmetry group is the Weyl group of the root system $E_r$; here they are deduced from the cone theorem for surfaces of P5 Ch. 12. Lazarsfeld, Section 1.5 (Laz04), gives Mumford's example and further examples, among them abelian surfaces, whose nef cone is the round cone of Example P7.4.23, and Debarre, Chapter 1 (Deb01), treats the cones in the setting of the cone theorem. That a boundary nef class need not come from a morphism, as in Example P7.4.24, is the reason the basepoint-free theorem of the minimal model program needs, for a nef divisor $D$, the hypothesis that $aD - K_X$ is nef and big for some $a > 0$.
