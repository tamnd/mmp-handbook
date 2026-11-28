---
title: The tangent space and the dimension estimate
nodes: []
sources: [Kol96, Deb01, AM69, Mor79, Mor82]
reads_with: [Kol96:II.1, Deb01:2.2, AM69:11]
requires: [P1.5, P3.6, P3.7, P3.12, P4.2, P4.7, P5.3, P5.4, P5.10, P7.1, P7.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The tangent space and the dimension estimate

### Statement

In this section $X$ is a smooth projective variety of dimension $n$, with tangent bundle $T_X = \Omega_X^\vee$, locally free of rank $n$ by Corollary P3.12.11, and canonical divisor $K_X$ with $\mathcal{O}_X(K_X) \cong \omega_X = \det \Omega_X$. For a point $x$ of a scheme $H$ locally of finite type over $k$, write $\dim_x H = \dim \mathcal{O}_{H, x}$; by part 3 of Theorem P3.7.4 applied to the irreducible components of $H$ through $x$, this is the largest dimension of such a component.

**Theorem P8.1.9 (the tangent space).** Let $C$ be a projective scheme over $k$, $B \subseteq C$ a closed subscheme with ideal sheaf $\mathcal{I}_B$, $f \colon C \to X$ a morphism and $g = f|_B$. Then there is a natural isomorphism of $k$-vector spaces
$$T_{[f]} \operatorname{Hom}(C, X; g) \cong H^0(C, f^* T_X \otimes \mathcal{I}_B).$$
In particular $T_{[f]} \operatorname{Hom}(C, X) \cong H^0(C, f^* T_X)$.

Lean: not in Lean as stated.

**Theorem P8.1.10 (the local structure, cited).** Let $C$ be a smooth projective curve, $B \subseteq C$ a finite set of points, $f \colon C \to X$ a morphism, $g = f|_B$ and $\mathcal{E} = f^* T_X \otimes \mathcal{O}_C(-B)$. Put $a = h^0(C, \mathcal{E})$ and $c = h^1(C, \mathcal{E})$. Then the completion of the local ring of $\operatorname{Hom}(C, X; g)$ at $[f]$ is isomorphic to
$$k[[t_1, \dots, t_a]]/(F_1, \dots, F_c)$$
for some power series $F_1, \dots, F_c$ without constant or linear terms.

Lean: not in Lean as stated.

**Lemma P8.1.11 (Riemann-Roch for vector bundles on a curve).** Let $C$ be a smooth projective curve of genus $g$ and $\mathcal{E}$ a locally free sheaf of rank $r$ on $C$, with $\deg \mathcal{E} = \deg \det \mathcal{E}$. Then
$$\chi(C, \mathcal{E}) = \deg \mathcal{E} + r(1 - g).$$

Lean: not in Lean as stated.

**Corollary P8.1.12 (the dimension estimate).** Let $C$ be a smooth projective curve of genus $g$, $B \subseteq C$ a set of $b$ points, $f \colon C \to X$ a morphism and $g_B = f|_B$. Then
$$\dim_{[f]} \operatorname{Hom}(C, X; g_B) \geq h^0(C, f^* T_X(-B)) - h^1(C, f^* T_X(-B)) = -K_X \cdot f_* C + n(1 - g) - n b.$$
In particular $\dim_{[f]} \operatorname{Hom}(C, X) \geq -K_X \cdot f_* C + n \chi(\mathcal{O}_C)$.

Lean: not in Lean as stated.

**Corollary P8.1.13 (unobstructed morphisms).** In the situation of Corollary P8.1.12, if $H^1(C, f^* T_X(-B)) = 0$, then $\operatorname{Hom}(C, X; g_B)$ is smooth at $[f]$ of dimension $-K_X \cdot f_* C + n(1 - g) - n b$. For $C = \mathbb{P}^1$ and $f$ nonconstant:
1. if $f$ is free, then $\operatorname{Hom}(\mathbb{P}^1, X)$ is smooth at $[f]$ of dimension $-K_X \cdot f_* \mathbb{P}^1 + n$, and $\operatorname{Hom}(\mathbb{P}^1, X; f|_{\{0\}})$ is smooth at $[f]$ of dimension $-K_X \cdot f_* \mathbb{P}^1$;
2. if $f$ is very free, then $\operatorname{Hom}(\mathbb{P}^1, X; f|_{\{0, \infty\}})$ is smooth at $[f]$ of dimension $-K_X \cdot f_* \mathbb{P}^1 - n$.

Lean: not in Lean as stated.

### Proof in words

A tangent vector at $[f]$ is a morphism from $C \times \operatorname{Spec} k[\varepsilon]$ to $X$ that restricts to $f$; since $C \times \operatorname{Spec} k[\varepsilon]$ has the same underlying space as $C$, it is $f^\# + \varepsilon D$ with $D$ a derivation, that is, a section of $f^* T_X$. The deformation theory of morphisms, which is cited, says that the obstructions to extending a deformation over a small extension lie in $H^1(C, f^* T_X)$, so the complete local ring is a power series ring in $h^0$ variables modulo at most $h^1$ equations. Krull's dimension theorem bounds the dimension of such a ring below by $h^0 - h^1$, and Riemann-Roch for vector bundles computes $h^0 - h^1$ as $\deg f^* T_X + n(1 - g)$, where $\deg f^* T_X = -K_X \cdot f_* C$.

### Examples

**Example P8.1.14 (lines in projective space).** Let $f \colon \mathbb{P}^1 \to L \subseteq \mathbb{P}^n$ be an isomorphism onto a line. By Example P5.4.13, $f^* T_{\mathbb{P}^n} \cong \mathcal{O}(2) \oplus \mathcal{O}(1)^{n-1}$, so $f$ is very free and $-K_{\mathbb{P}^n} \cdot L = 2 + (n - 1) = n + 1$. By Corollary P8.1.13, $\operatorname{Hom}(\mathbb{P}^1, \mathbb{P}^n)$ is smooth of dimension $2n + 1$ at $[f]$, which agrees with Example P8.1.7 for $d = 1$; with $f(0)$ fixed the dimension is $n + 1$, and with $f(0)$ and $f(\infty)$ fixed it is $1$, the copy of $\mathbb{G}_m$ of Exercise 2 of Section 1.1. The count $n + 1 = (2n + 1) - n$ matches the geometry: the lines through $f(0)$ form a $\mathbb{P}^{n-1}$, and each is parametrized with $0 \mapsto f(0)$ by the $2$-dimensional group of automorphisms of $\mathbb{P}^1$ fixing $0$.

**Example P8.1.15 (a $(-2)$-curve, where the estimate is strict).** Let $S$ be the blow-up of $\mathbb{P}^2$ in six distinct points with $P_1, P_2, P_3$ on a line, and $C$ the strict transform of that line, as in Example P5.10.9: $C \cong \mathbb{P}^1$, $C^2 = -2$ and $K_S \cdot C = 0$. Let $f \colon \mathbb{P}^1 \to C \subseteq S$ be an isomorphism. The conormal sequence of Theorem P3.12.14, dualized, gives $0 \to T_C \to T_S|_C \to N_{C/S} \to 0$ with $T_C \cong \mathcal{O}(2)$ and $N_{C/S} = \mathcal{O}_C(C) \cong \mathcal{O}(-2)$. The extension class lies in $\operatorname{Ext}^1(\mathcal{O}(-2), \mathcal{O}(2)) = H^1(\mathcal{O}(4)) = 0$ by parts 1 and 4 of Proposition P4.7.2 and Theorem P4.2.1, so $f^* T_S \cong \mathcal{O}(2) \oplus \mathcal{O}(-2)$, with $h^0 = 3$ and $h^1 = 1$. The estimate of Corollary P8.1.12 is $-K_S \cdot C + 2 = 2$. The actual dimension is $3$. Let $f'$ be a $k$-point of the connected component of $\operatorname{Hom}(\mathbb{P}^1, S)$ containing $[f]$. By Proposition P8.1.6, $f'_* \mathbb{P}^1 \equiv C$. If the image $C'$ of $f'$ were a curve different from $C$, then $C \cdot f'_* \mathbb{P}^1 \geq 0$, since distinct curves meet nonnegatively, while $C \cdot C = -2$. So $f'(\mathbb{P}^1) = C$, and $f'_* \mathbb{P}^1 = \deg(f') [C] \equiv [C]$ forces $\deg f' = 1$ because $H \cdot C > 0$ for an ample $H$. Then $f^{-1} \circ f' \in \operatorname{Aut}(\mathbb{P}^1)$, and the component is the orbit $f \circ \operatorname{PGL}_2$ of Example P8.1.8, of dimension $3$. Since the tangent space has dimension $h^0 = 3$, the scheme is smooth at $[f]$ although $H^1 \neq 0$.

**Example P8.1.16 (translations of an elliptic curve).** Let $E$ be an elliptic curve and $f = \mathrm{id}_E$. Then $T_E \cong \mathcal{O}_E$, since $\omega_E \cong \mathcal{O}_E$, so $h^0(T_E) = h^1(T_E) = 1$ and the estimate is $-K_E \cdot E + 1 \cdot \chi(\mathcal{O}_E) = 0$. The translations $x \mapsto x + a$ form a $1$-dimensional family through $[\mathrm{id}]$, so $\dim_{[\mathrm{id}]} \operatorname{Hom}(E, E) \geq 1$, while the tangent space has dimension $1$; so the local ring at $[\mathrm{id}]$ is regular of dimension $1$. Again the scheme is smooth of dimension $h^0$, one more than the estimate.

### Proof

*Theorem P8.1.9.* Write $H = \operatorname{Hom}(C, X; g)$ and $k[\varepsilon] = k[t]/(t^2)$. By Proposition P3.7.13, $T_{[f]} H$ is the set of $k$-morphisms $\operatorname{Spec} k[\varepsilon] \to H$ sending the point to $[f]$, and by Theorem P8.1.4 and Proposition P8.1.5 these are the morphisms $F \colon C[\varepsilon] = C \times \operatorname{Spec} k[\varepsilon] \to X$ over $k$ with $F|_C = f$ and $F|_{B[\varepsilon]} = g \circ \mathrm{pr}$, where $\mathrm{pr} \colon B[\varepsilon] \to B$ is the projection. The scheme $C[\varepsilon]$ has the underlying space of $C$ and structure sheaf $\mathcal{O}_C[\varepsilon] = \mathcal{O}_C \oplus \varepsilon \mathcal{O}_C$. Since $F|_C = f$, the map of spaces of $F$ is that of $f$, and $F$ is given by a map of sheaves of $k$-algebras $F^\# \colon f^{-1} \mathcal{O}_X \to \mathcal{O}_C \oplus \varepsilon \mathcal{O}_C$ whose first component is $f^\#$; it is automatically local, because $\varepsilon$ is nilpotent. Write $F^\# = f^\# + \varepsilon D$. Then $F^\#$ is multiplicative and $k$-linear exactly when $D$ is $k$-linear and
$$D(a b) = f^\#(a) D(b) + f^\#(b) D(a),$$
that is, when $D \colon f^{-1} \mathcal{O}_X \to \mathcal{O}_C$ is a $k$-derivation over $f^\#$. By the universal property of differentials, these correspond to $f^{-1} \mathcal{O}_X$-linear maps $f^{-1} \Omega_X \to \mathcal{O}_C$, that is, to $\mathcal{O}_C$-linear maps $f^* \Omega_X \to \mathcal{O}_C$, the sections of $\mathcal{H}om(f^* \Omega_X, \mathcal{O}_C) = f^* T_X$, using that $\Omega_X$ is locally free. The condition on $B[\varepsilon]$ says that $D$ composed with $\mathcal{O}_C \to \mathcal{O}_B$ vanishes, that is, that the corresponding map $f^* \Omega_X \to \mathcal{O}_C$ lands in $\mathcal{I}_B$; such maps are the sections of $\mathcal{H}om(f^* \Omega_X, \mathcal{I}_B) = f^* T_X \otimes \mathcal{I}_B$. The trivial deformation $f \circ \mathrm{pr}$ corresponds to $D = 0$, and the vector space structure of Proposition P3.7.13, defined through $k[\varepsilon_1, \varepsilon_2]/(\varepsilon_1, \varepsilon_2)^2$, corresponds to the sum and scalar multiples of derivations.

*Theorem P8.1.10.* This is the deformation theory of morphisms, Kollár, Theorems I.2.17 and II.1.2 (Kol96); see also Debarre, Section 2.2 (Deb01). The proof is not given here. In outline, for a small extension $A' \to A$ of Artin local $k$-algebras with kernel $k \cdot \epsilon$ and a morphism $F \colon C_A \to X$ extending $f$, the extensions of $F$ to $C_{A'}$ form a torsor under $H^0(C, \mathcal{E})$ when they exist, and the obstruction to their existence is a class in $H^1(C, \mathcal{E})$, obtained by gluing local extensions, which exist because $X$ is smooth. A complete local ring with these properties has the stated form. The hypothesis that $B$ is reduced and $C$ a smooth curve keeps the statement within what Part A uses.

*Lemma P8.1.11.* Induct on $r$. For $r = 1$ this is the Riemann-Roch theorem P5.3.10, since $p_a(C) = g$. Let $r \geq 2$ and fix an embedding $C \subseteq \mathbb{P}^N$. By Theorem P3.6.23, $\mathcal{E}(m)$ is generated by global sections for some $m$, and it is nonzero, so it has a nonzero section $s \colon \mathcal{O}_C \to \mathcal{E}(m)$, injective because $C$ is integral and $\mathcal{E}(m)$ is locally free. Let $\mathcal{T}$ be the torsion subsheaf of $\mathcal{E}(m)/s \mathcal{O}_C$, $\mathcal{M}$ the kernel of $\mathcal{E}(m) \to (\mathcal{E}(m)/s \mathcal{O}_C)/\mathcal{T}$ and $\mathcal{Q}$ the image. The stalks of $\mathcal{Q}$ are finitely generated torsion-free modules over the local rings of $C$, which are discrete valuation rings by part 5 of Proposition P3.7.15, so they are free and $\mathcal{Q}$ is locally free of rank $r - 1$. Then $0 \to \mathcal{M} \to \mathcal{E}(m) \to \mathcal{Q} \to 0$ is locally split, so $\mathcal{M}$ is locally free of rank $1$. Twisting by $\mathcal{O}(-m)$ gives an exact sequence $0 \to \mathcal{M}' \to \mathcal{E} \to \mathcal{Q}' \to 0$ of locally free sheaves of ranks $1$, $r$ and $r - 1$. The map $\mathcal{M}' \otimes \det \mathcal{Q}' \to \det \mathcal{E}$, $u \otimes (\bar q_1 \wedge \dots \wedge \bar q_{r-1}) \mapsto u \wedge q_1 \wedge \dots \wedge q_{r-1}$ for local lifts $q_i$ of $\bar q_i$, is well defined because changing a lift changes the wedge by a multiple of $u \wedge u = 0$, and it is an isomorphism where the sequence splits, so everywhere. Hence $\deg \mathcal{E} = \deg \mathcal{M}' + \deg \mathcal{Q}'$. The long exact cohomology sequence gives $\chi(\mathcal{E}) = \chi(\mathcal{M}') + \chi(\mathcal{Q}')$, and by induction
$$\chi(\mathcal{E}) = \deg \mathcal{M}' + 1 - g + \deg \mathcal{Q}' + (r - 1)(1 - g) = \deg \mathcal{E} + r(1 - g).$$

*Corollary P8.1.12.* Let $\mathcal{O}$ be the local ring of $\operatorname{Hom}(C, X; g_B)$ at $[f]$, a Noetherian local ring because the scheme is locally of finite type over $k$, and $\hat{\mathcal{O}}$ its completion. By Atiyah and Macdonald, Corollary 11.19 (AM69), $\dim \mathcal{O} = \dim \hat{\mathcal{O}}$. By Theorem P8.1.10, $\hat{\mathcal{O}} = A/I$ with $A = k[[t_1, \dots, t_a]]$ and $I = (F_1, \dots, F_c)$; $A$ is a Noetherian local ring of dimension $a$ by Corollary P1.5.36. Let $d' = \dim A/I$. By the dimension theorem P1.5.35 applied to $A/I$, there are $u_1, \dots, u_{d'}$ in the maximal ideal of $A$ whose images generate a primary ideal for the maximal ideal of $A/I$. Then $u_1, \dots, u_{d'}, F_1, \dots, F_c$ generate an ideal of $A$ whose radical is the maximal ideal, and Theorem P1.5.35 applied to $A$ gives $a \leq d' + c$. So
$$\dim_{[f]} \operatorname{Hom}(C, X; g_B) = d' \geq a - c = \chi(C, f^* T_X(-B)).$$
By Lemma P8.1.11 with $r = n$, $\chi(C, f^* T_X(-B)) = \deg f^* T_X(-B) + n(1 - g)$. Twisting a bundle of rank $n$ by the line bundle $\mathcal{O}_C(-B)$ of degree $-b$ multiplies its determinant by $\mathcal{O}_C(-B)^{\otimes n}$, so $\deg f^* T_X(-B) = \deg f^* T_X - n b$. Finally $\det f^* T_X = f^* \det T_X = f^* \omega_X^{-1}$, so $\deg f^* T_X = \deg f^* \mathcal{O}_X(-K_X) = -K_X \cdot f_* C$ by Proposition P7.1.7 and the projection formula of Proposition P7.2.7. For $B = \emptyset$, $n(1 - g) = n \chi(\mathcal{O}_C)$.

*Corollary P8.1.13.* If $c = h^1 = 0$, Theorem P8.1.10 gives $\hat{\mathcal{O}} \cong k[[t_1, \dots, t_a]]$, a regular local ring of dimension $a$. The maximal ideals of $\mathcal{O}$ and $\hat{\mathcal{O}}$ have isomorphic quotients by their squares and $\dim \mathcal{O} = \dim \hat{\mathcal{O}}$ (AM69, Proposition 10.15 and Corollary 11.19), so $\mathcal{O}$ is regular of dimension $a$. By part 2 of Proposition P3.7.15, $[f]$ lies on a single irreducible component of the scheme, of dimension $a$ by part 3 of Theorem P3.7.4; removing the other components, which are closed and miss $[f]$, the scheme has pure dimension $a$ near $[f]$, and part 2 of Theorem P3.7.24 shows that it is smooth of dimension $a$ at $[f]$. By Corollary P8.1.12, $a = a - c = -K_X \cdot f_* C + n(1 - g) - n b$. For $C = \mathbb{P}^1$ write $f^* T_X \cong \bigoplus_i \mathcal{O}(a_i)$ by Theorem P5.4.10. If $f$ is free, all $a_i \geq 0$, so $H^1(f^* T_X) = 0$ and $H^1(f^* T_X(-1)) = 0$ by part 2 of Corollary P5.4.11, which gives part 1 with $b = 0$ and $b = 1$. If $f$ is very free, $H^1(f^* T_X(-2)) = 0$ by part 3 of Corollary P5.4.11, which gives part 2.

### Exercises

1. (A) Let $f \colon \mathbb{P}^1 \to \mathbb{P}^2$ be an isomorphism onto a smooth conic. Using Example P5.4.14, show that $\operatorname{Hom}(\mathbb{P}^1, \mathbb{P}^2)$ is smooth of dimension $8$ at $[f]$, in agreement with Example P8.1.7.
2. (A) Let $f \colon \mathbb{P}^1 \to \mathbb{P}^n$ have degree $d \geq 1$. Using the Euler sequence of Theorem P3.12.20 pulled back by $f$, show that $f^* T_{\mathbb{P}^n}$ is a quotient of $\mathcal{O}(d)^{n+1}$ of degree $(n + 1) d$, that $H^1(f^* T_{\mathbb{P}^n}) = 0$, and that $\operatorname{Hom}_d(\mathbb{P}^1, \mathbb{P}^n)$ is smooth of dimension $(n + 1) d + n$.
3. (B) Let $S$ be a smooth projective surface and $C \subseteq S$ a $(-1)$-curve. Show that $T_S|_C \cong \mathcal{O}(2) \oplus \mathcal{O}(-1)$, that $\operatorname{Hom}(\mathbb{P}^1, S)$ is smooth of dimension $3$ at an isomorphism $f \colon \mathbb{P}^1 \to C$, and that its component through $[f]$ is $f \circ \operatorname{PGL}_2$.
4. (C) Let $C$ be a smooth projective curve, $B = \{ c_1, \dots, c_b \} \subseteq C$ and $f \colon C \to X$. Show directly that $\dim_{[f]} \operatorname{Hom}(C, X; f|_B) \geq \dim_{[f]} \operatorname{Hom}(C, X) - n b$: the fibre of $\operatorname{Hom}(C, X) \to X^b$, $h \mapsto (h(c_1), \dots, h(c_b))$, is cut out near $[f]$ by the pullbacks of $n b$ generators of the maximal ideal of the regular local ring of $X^b$ at $f(B)$, and the argument of Corollary P8.1.12 applies.
5. (B) Let $C$ be a smooth projective curve of genus $g \geq 2$. Show that $H^0(C, T_C) = 0$, that $[\mathrm{id}_C]$ is an isolated reduced point of $\operatorname{Hom}(C, C)$, and, using composition with automorphisms and Theorem P8.1.4, that the automorphisms of $C$ are isolated reduced points of $\operatorname{Hom}(C, C)$.
6. (B) Let $f \colon \mathbb{P}^1 \to X$ be free and $p \in \mathbb{P}^1$. Show that the differential at $(p, [f])$ of the evaluation morphism $\operatorname{ev} \colon \mathbb{P}^1 \times \operatorname{Hom}(\mathbb{P}^1, X) \to X$ is $(v, s) \mapsto df_p(v) + s(p)$ on $T_p \mathbb{P}^1 \oplus H^0(f^* T_X)$, and that it is surjective.

### Lean

Tangent spaces of parameter spaces, the deformation theory of morphisms and Riemann-Roch for vector bundles on curves are not in the repository. The canonical divisor appears in `MinimalModel/Statements/Basic.lean` as `MinimalModel.CanonicalDivisor`, but intersection numbers with curves, which the estimate needs, are not formalized there.

### Notes and history

The identification of first order deformations with sections of $f^* T_X$ and the obstruction space $H^1(C, f^* T_X)$ go back to Grothendieck's work on the Hilbert scheme. Mori used the estimate $\dim_{[f]} \operatorname{Hom}(C, X) \geq -K_X \cdot C + n \chi(\mathcal{O}_C)$ in his proof of Hartshorne's conjecture (Mor79) and in his paper on extremal rays (Mor82), where it is the source of every rational curve. Kollár (Kol96, Chapter II) states it for morphisms from curves with arbitrary singularities and from families of curves, and Debarre (Deb01, Chapter 2) treats the case of smooth curves used here. Examples P8.1.15 and P8.1.16 show that the estimate is only a lower bound; when $H^1(C, f^* T_X) \neq 0$ the scheme may still be smooth, of larger dimension, and the estimate gives no information about singularities.
