---
title: Picard numbers of the basic examples
nodes: []
sources: [Laz04, Deb01, Har77]
reads_with: [Laz04:1.1.C, Deb01:ch1]
requires: [P3.8, P3.9, P3.11, P5.6, P5.9, P5.12, P7.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Picard numbers of the basic examples

### Statement

This section computes $N^1(X)$ and $N_1(X)$, with dual bases, for the examples that carry the rest of the volume. In each case the computation also shows which classes contain curves, which is the starting point of the cones of Chapter 4.

**Proposition P7.2.21 (projective spaces and their products).**

1. $\operatorname{Pic}(\mathbb{P}^n) = N^1(\mathbb{P}^n)_\mathbb{Z} = \mathbb{Z} [\mathcal{O}(1)]$ for $n \geq 1$, and $N_1(\mathbb{P}^n) = \mathbb{R} [\ell]$ for a line $\ell$, with $\mathcal{O}(1) \cdot \ell = 1$. So $\rho(\mathbb{P}^n) = 1$, and a curve of degree $d$ has class $d [\ell]$.
2. Let $X = \mathbb{P}^a \times \mathbb{P}^b$ with $a, b \geq 1$, $H_i = p_i^* \mathcal{O}(1)$, and $\ell_1 = \ell \times \{y\}$, $\ell_2 = \{x\} \times \ell'$ for lines $\ell \subseteq \mathbb{P}^a$, $\ell' \subseteq \mathbb{P}^b$ and points $x$, $y$. Then $\operatorname{Pic}(X) = N^1(X)_\mathbb{Z} = \mathbb{Z} H_1 \oplus \mathbb{Z} H_2$, $\rho(X) = 2$, and $[\ell_1]$, $[\ell_2]$ is the basis of $N_1(X)$ dual to $H_1$, $H_2$. Every curve $C$ has class $(H_1 \cdot C)[\ell_1] + (H_2 \cdot C)[\ell_2]$ with both coefficients nonnegative.

Lean: not in Lean as stated.

**Proposition P7.2.22 (products).** Let $X$ and $Y$ be projective varieties with projections $p_1$, $p_2$ from $X \times Y$. Then
$$p_1^* + p_2^* \colon N^1(X) \oplus N^1(Y) \to N^1(X \times Y)$$
is injective, so $\rho(X \times Y) \geq \rho(X) + \rho(Y)$.

Lean: not in Lean as stated.

**Proposition P7.2.23 (the blow-up of a point).** Let $X$ be a smooth projective variety of dimension $n \geq 2$, $p \in X$ a closed point, $\pi \colon \tilde X \to X$ the blow-up with exceptional divisor $E \cong \mathbb{P}^{n-1}$, and $e \subseteq E$ a line.

1. $\operatorname{Pic}(\tilde X) = \pi^* \operatorname{Pic}(X) \oplus \mathbb{Z} [\mathcal{O}(E)]$, with $\pi^*$ injective.
2. $N^1(\tilde X) = \pi^* N^1(X) \oplus \mathbb{R} [E]$, so $\rho(\tilde X) = \rho(X) + 1$.
3. $\pi_* \colon N_1(\tilde X) \to N_1(X)$ is surjective with kernel $\mathbb{R} [e]$. A curve in $E$ of degree $d$ in $E \cong \mathbb{P}^{n-1}$ has class $d [e]$. A curve $\tilde C \not\subseteq E$ has $\pi_* [\tilde C] = [\pi(\tilde C)]$ and $E \cdot \tilde C \geq 0$.

Lean: not in Lean as stated.

**Proposition P7.2.24 (the Hirzebruch surfaces).** Let $n \geq 0$ and $\mathbb{F}_n = \mathbb{P}(\mathcal{O} \oplus \mathcal{O}(n))$ with the curves $C_-$, $C_+$, $F$ of Definition P3.11.24. Then $\operatorname{Pic}(\mathbb{F}_n) = N^1(\mathbb{F}_n)_\mathbb{Z} = \mathbb{Z} C_- \oplus \mathbb{Z} F$ and $\rho(\mathbb{F}_n) = 2$. Under the identification $N_1 = N^1$ of Proposition P7.2.8, the basis $[C_-]$, $[F]$ of $N_1(\mathbb{F}_n)$ is dual to the basis $F$, $C_+$ of $N^1(\mathbb{F}_n)$. Every curve $C$ has class $(F \cdot C)[C_-] + (C_+ \cdot C)[F]$ with both coefficients nonnegative.

Lean: not in Lean as stated.

### Proof in words

On projective space and its products the Picard group is computed by removing coordinate hyperplanes, which leaves an affine space with trivial class group, so the hyperplanes generate. Lines in the two factors are dual to the two hyperplane classes by the projection formula, because a line in one factor maps isomorphically to the first projection and to a point under the second.

For a blow-up, removing the exceptional divisor leaves $X$ minus a point, whose class group is that of $X$ because a point has codimension at least $2$. So the Picard group grows by the class of $E$, which is not a multiple of a pullback because it has degree $-1$ on a line of $E$ while pullbacks have degree $0$ there. Pushforward of curves kills exactly the line class $e$, by a dimension count.

The coefficients of a curve class in a dual basis are intersection numbers with the basis of $N^1$. When that basis consists of globally generated line bundles, the coefficients are nonnegative by Chapter 1. This gives, without any further work, the cone that contains all curves.

### Examples

**Example P7.2.25 (the blow-up of projective space at a point).** Let $\tilde X = \operatorname{Bl}_p \mathbb{P}^n$, $n \geq 2$, with $H = \pi^* \mathcal{O}(1)$ and $E$ as in Example P7.1.26. Let $\ell$ be the preimage of a line not through $p$ and $e$ a line in $E$. By Proposition P7.2.23, $N^1(\tilde X)$ has basis $H$, $E$ and $N_1(\tilde X)$ has basis $[\ell]$, $[e]$, with
$$H \cdot \ell = 1, \quad H \cdot e = 0, \quad E \cdot \ell = 0, \quad E \cdot e = -1,$$
by part 6 of Proposition P7.1.23. Let $\tilde\ell_p$ be the strict transform of a line through $p$. By Example P7.1.26, $H - E$ is the pullback of $\mathcal{O}(1)$ under the morphism $q \colon \tilde X \to \mathbb{P}^{n-1}$ of projection from $p$, which maps $\tilde\ell_p$ to a point. So $(H - E) \cdot \tilde\ell_p = 0$ by part 2 of Proposition P7.2.7, and $H \cdot \tilde\ell_p = 1$ since $\pi$ maps $\tilde \ell_p$ birationally onto a line. Hence $E \cdot \tilde\ell_p = 1$ and $[\tilde\ell_p] = [\ell] - [e]$. Every curve $\tilde C \not\subseteq E$ has class $d[\ell] - m[e]$ with $d = H \cdot \tilde C$ the degree of $\pi(\tilde C)$ and $m = E \cdot \tilde C$. Both $H$ and $H - E$ are pulled back from $\mathcal{O}(1)$, so they are globally generated, and part 1 of Proposition P7.1.14 gives $d \geq 0$ and $d - m \geq 0$; part 3 of Proposition P7.2.23 gives $m \geq 0$. So
$$d[\ell] - m[e] = m [\tilde\ell_p] + (d - m)[\ell] = m [\tilde\ell_p] + (d - m)([\tilde\ell_p] + [e]),$$
and every curve class, including the classes $d[e]$ of curves in $E$, is a nonnegative combination of $[e]$ and $[\tilde\ell_p]$. For $n = 2$ this is the computation of Example P5.12.7.

**Example P7.2.26 (the plane blown up at points).** Let $S_r$ be the blow-up of $\mathbb{P}^2$ at $r$ distinct points, with $H$ and $E_1, \dots, E_r$ as in Example P7.1.27. By Example P5.6.8 and Proposition P7.2.8, $N^1(S_r)_\mathbb{Z} = \operatorname{Pic}(S_r) = \mathbb{Z} H \oplus \bigoplus_i \mathbb{Z} E_i$ and $\rho(S_r) = r + 1$; the intersection form is diagonal with entries $1, -1, \dots, -1$, so it is unimodular, and $N_1(S_r)_\mathbb{Z}$, identified with $\operatorname{Pic}(S_r)$, is dual to $N^1(S_r)_\mathbb{Z}$. The basis of $N_1$ dual to $H, E_1, \dots, E_r$ is $[H], -[E_1], \dots, -[E_r]$. A curve that is the strict transform of a plane curve of degree $d$ with multiplicities $m_i$ at the points has class $dH - \sum_i m_i E_i$ (Proposition P5.6.4).

**Example P7.2.27 (an elliptic ruled surface).** Let $E$ be an elliptic curve and $S = E \times \mathbb{P}^1 = \mathbb{P}(\mathcal{O}_E^2)$. By part 1 of Theorem P5.9.4, $\operatorname{Pic}(S) = \mathbb{Z} h \oplus p_1^* \operatorname{Pic}(E)$, which is not finitely generated, and by part 2, $N^1(S)_\mathbb{Z} = \operatorname{Num}(S) = \mathbb{Z} h \oplus \mathbb{Z} f$, where $h = [E \times \{y\}]$ and $f = [\{x\} \times \mathbb{P}^1]$. So $\rho(S) = 2 = \rho(E) + \rho(\mathbb{P}^1)$, and the inequality of Proposition P7.2.22 is an equality here, while it is strict for $E \times E$ by Example P7.2.19.

### Proof

*Proposition P7.2.21.* Part 1. The local rings of $\mathbb{P}^n$ are localizations of polynomial rings, so $\operatorname{Pic}(\mathbb{P}^n) \cong \operatorname{Cl}(\mathbb{P}^n) \cong \mathbb{Z}$ by Theorem P3.9.10 and part 3 of Theorem P3.8.20, generated by the class of a hyperplane $H$, and $\mathcal{O}(H) \cong \mathcal{O}(1)$ by Proposition P3.8.30. The line $\ell$ is isomorphic to $\mathbb{P}^1$ and $\mathcal{O}(1)|_\ell \cong \mathcal{O}_{\mathbb{P}^1}(1)$, so $\mathcal{O}(1) \cdot \ell = 1$ by part 2 of Proposition P7.1.7. So $\mathcal{O}(d) \cdot \ell = d \neq 0$ for $d \neq 0$, and $\operatorname{Pic}(\mathbb{P}^n) \to N^1(\mathbb{P}^n)_\mathbb{Z}$ is an isomorphism. By Proposition P7.2.5, $N_1(\mathbb{P}^n)$ has dimension $1$ and basis $[\ell]$. A curve $C$ of degree $d = \mathcal{O}(1) \cdot C$ (Corollary P7.1.18) has $\mathcal{O}(1) \cdot (C - d \ell) = 0$, so $[C] = d[\ell]$.

Part 2. The scheme $X$ is covered by the open sets $D_+(x_i) \times D_+(y_j) \cong \mathbb{A}^{a+b}$, so its local rings are localizations of polynomial rings and are factorial, and $X$ is integral. By Theorem P3.9.10, $\operatorname{Pic}(X) \cong \operatorname{Cl}(X)$. Let $V_1 = V_+(x_0) \times \mathbb{P}^b$ and $V_2 = \mathbb{P}^a \times V_+(y_0)$, which are prime divisors since they are isomorphic to $\mathbb{P}^{a-1} \times \mathbb{P}^b$ and $\mathbb{P}^a \times \mathbb{P}^{b-1}$. Their complement is $\mathbb{A}^a \times \mathbb{A}^b = \mathbb{A}^{a+b}$, whose class group is $0$ by Proposition P3.8.12. By part 2 of Theorem P3.8.13, $\operatorname{Cl}(X)$ is generated by $V_1$ and $V_2$, and $\mathcal{O}_X(V_i) \cong H_i$ by part 4 of Proposition P3.9.27 and Proposition P3.8.30. The projection $p_1$ maps $\ell_1$ isomorphically onto $\ell$ and maps $\ell_2$ to a point, so part 2 of Proposition P7.2.7 gives $H_1 \cdot \ell_1 = \mathcal{O}(1) \cdot \ell = 1$ and $H_1 \cdot \ell_2 = 0$; symmetrically $H_2 \cdot \ell_1 = 0$ and $H_2 \cdot \ell_2 = 1$. So a combination $a_1 H_1 + a_2 H_2$ that is numerically trivial has $a_1 = a_2 = 0$. Hence $\operatorname{Pic}(X) = \mathbb{Z} H_1 \oplus \mathbb{Z} H_2 = N^1(X)_\mathbb{Z}$, and $[\ell_1]$, $[\ell_2]$ is the dual basis of $N_1(X)$ by part 3 of Proposition P7.2.5. A curve $C$ has the class $(H_1 \cdot C)[\ell_1] + (H_2 \cdot C)[\ell_2]$, since both sides have the same intersection numbers with $H_1$ and $H_2$. The $H_i$ are globally generated, so the coefficients are nonnegative by part 1 of Proposition P7.1.14. $\square$

*Proposition P7.2.22.* The product $X \times Y$ is a projective variety. Let $\alpha \in N^1(X)$ and $\beta \in N^1(Y)$ with $p_1^* \alpha + p_2^* \beta = 0$. For a curve $C \subseteq X$ and a closed point $y \in Y$, the curve $C \times \{y\}$ maps isomorphically onto $C$ under $p_1$ and to a point under $p_2$. By part 2 of Proposition P7.2.7,
$$0 = (p_1^* \alpha + p_2^* \beta) \cdot [C \times \{y\}] = \alpha \cdot [C] + 0.$$
So $\alpha$ pairs to zero with every curve and $\alpha = 0$. Symmetrically $\beta = 0$. $\square$

*Proposition P7.2.23.* As in the proof of Proposition P7.1.23, $\tilde X$ is a smooth projective variety (Hartshorne, Theorem II.8.24), so its local rings are regular, hence factorial, and $\operatorname{Pic}(\tilde X) \cong \operatorname{Cl}(\tilde X)$ by Theorem P3.9.10; the same holds for $X$. By part 3 of Theorem P3.11.3, $\pi$ is an isomorphism $\tilde X \setminus E \to X \setminus \{p\}$, and $\operatorname{Cl}(X) \to \operatorname{Cl}(X \setminus \{p\})$ is an isomorphism by part 3 of Theorem P3.8.13, since $n \geq 2$. The exceptional divisor $E \cong \mathbb{P}^{n-1}$ is a prime divisor, so part 2 of Theorem P3.8.13 gives an exact sequence
$$\mathbb{Z} E \to \operatorname{Cl}(\tilde X) \to \operatorname{Cl}(\tilde X \setminus E) \to 0.$$
The composite of $\pi^* \colon \operatorname{Pic}(X) \to \operatorname{Pic}(\tilde X)$ with restriction to $\tilde X \setminus E \cong X \setminus \{p\}$ is restriction from $X$ to $X \setminus \{p\}$, an isomorphism. So $\pi^*$ is injective and $\operatorname{Pic}(\tilde X) = \pi^* \operatorname{Pic}(X) + \mathbb{Z} [\mathcal{O}(E)]$. If $\pi^* L \cong \mathcal{O}(mE)$, then intersecting with $e$ gives $0 = -m$ by part 6 of Proposition P7.1.23, so the sum is direct and $\mathcal{O}(E)$ has infinite order. This is part 1.

Part 2. The classes $\pi^* N^1(X)$ and $[E]$ span $N^1(\tilde X)$ by part 1. If $\pi^* \alpha + t[E] = 0$, then pairing with $[e]$ gives $-t = 0$, and then $\alpha = 0$ by part 3 of Proposition P7.2.7, as $\pi$ is surjective.

Part 3. By part 3 of Proposition P7.2.7, $\pi_*$ is surjective, and the dimensions are $\rho(X) + 1$ and $\rho(X)$, so its kernel has dimension $1$. It contains $[e]$, which is not zero since $E \cdot e = -1$. Let $C \subseteq E$ be a curve of degree $d$ in $E \cong \mathbb{P}^{n-1}$ and $M$ a line bundle on $\tilde X$. Then $M|_E \cong \mathcal{O}_{\mathbb{P}^{n-1}}(c)$ for some $c$ by part 1 of Proposition P7.2.21, and by part 7 of Theorem P7.1.6 and part 1 of Proposition P7.2.21 on $E$, $M \cdot C = cd$ and $M \cdot e = c$. So $[C] = d[e]$. Let $\tilde C \not\subseteq E$ be a curve. The map $\tilde C \to \pi(\tilde C)$ is birational, as $\pi$ is an isomorphism off $E$, so $\pi_*[\tilde C] = [\pi(\tilde C)]$. The canonical section of $\mathcal{O}(E)$ does not vanish at the generic point of $\tilde C$, so by part 6 of Theorem P7.1.6 and part 1 of Proposition P7.1.7, $E \cdot \tilde C$ is the length of the finite scheme $\tilde C \cap E$, which is nonnegative. $\square$

*Proposition P7.2.24.* By part 4 of Theorem P3.11.25, $\operatorname{Pic}(\mathbb{F}_n) = \mathbb{Z} F \oplus \mathbb{Z} C_-$. By Corollary P7.1.25 the intersection matrix of $C_-$, $F$ is $\begin{pmatrix} -n & 1 \\ 1 & 0 \end{pmatrix}$, of determinant $-1$, so no nonzero combination is numerically trivial, and $N^1(\mathbb{F}_n)_\mathbb{Z} = \operatorname{Pic}(\mathbb{F}_n)$ with $\rho = 2$. With $C_+ \sim C_- + nF$, Corollary P7.1.25 gives $F \cdot C_- = 1$, $F \cdot F = 0$, $C_+ \cdot C_- = 0$ and $C_+ \cdot F = 1$, which is the duality. A class $x$ equals $(F \cdot x)[C_-] + (C_+ \cdot x)[F]$, since both sides pair in the same way with the basis $F$, $C_+$. The line bundle $\mathcal{O}(F)$ is the pullback of $\mathcal{O}_{\mathbb{P}^1}(1)$, and $\mathcal{O}(C_+) = \mathcal{O}_{\mathbb{F}_n}(1)$ is a quotient of the pullback of $\mathcal{O} \oplus \mathcal{O}(n)$, which is globally generated for $n \geq 0$. So both are globally generated, and the coefficients of a curve class are nonnegative by part 1 of Proposition P7.1.14. $\square$

### Exercises

1. (A) On $\mathbb{P}^1 \times \mathbb{P}^1$, write the class of the diagonal and of a curve of bidegree $(a, b)$ in the basis $[\ell_1]$, $[\ell_2]$, and check the result against Example P5.5.9.
2. (A) On $\mathbb{F}_n$, write $[C_+]$ and the class of a curve in $|C_+ + F|$ in the basis $[C_-]$, $[F]$ of $N_1$.
3. (B) Let $X = \mathbb{P}^{a_1} \times \dots \times \mathbb{P}^{a_s}$. Show that $\operatorname{Pic}(X) = N^1(X)_\mathbb{Z} = \mathbb{Z}^s$ and find the basis of $N_1(X)$ dual to the pullbacks of the hyperplane classes.
4. (B) Let $\tilde X$ be the blow-up of $\mathbb{P}^n$ at two distinct points $p_1$, $p_2$. Find bases of $N^1(\tilde X)$ and $N_1(\tilde X)$, and the class of the strict transform of the line through $p_1$ and $p_2$.
5. (B) Let $\mathcal{E} = \mathcal{O} \oplus \mathcal{O}(a_1) \oplus \dots \oplus \mathcal{O}(a_{r-1})$ on $\mathbb{P}^1$ with $a_i \geq 0$ and $P = \mathbb{P}(\mathcal{E})$. Using Proposition P7.1.24, show that $\xi$ and $F$ are linearly independent in $N^1(P)$, and, assuming $\operatorname{Pic}(P) = \mathbb{Z} \xi \oplus \mathbb{Z} F$, find the basis of $N_1(P)$ dual to $F$, $\xi$.
6. (C) Let $C_1$, $C_2$ be smooth projective curves of genus at least $1$ with no nonconstant morphism $C_1 \to C_2$. Admitting that $\operatorname{Num}(C_1 \times C_2)$ is spanned by the two fibre classes and the classes of graphs of morphisms, show that $\rho(C_1 \times C_2) = 2$, and contrast with $E \times E$.

### Lean

Mathlib has projective space as a scheme and products of schemes, but no Picard group of $\mathbb{P}^n$ as a scheme and no class group excision. The project library has no computed example of `MinimalModel.N1` or `MinimalModel.IntersectionData.N₁`; its statements are about arbitrary normal projective varieties. The handbook adds no `MinimalModel` node here.

### Notes and history

The computation of the class group of projective space by excision is in Hartshorne, Proposition II.6.4, and the product case is Exercise II.6.1 there. The blow-up of a point adds one to the Picard number, a fact that goes back to the Italian school for surfaces and that P5 Ch. 6 proves for surfaces through the intersection form. The literature state is theorem. The numbers $\rho(E \times E) \in \{3, 4\}$ and the relation with complex multiplication are classical; Lazarsfeld, Section 1.5.B, uses them to show that the nef cone of an abelian surface can be round, which is Example P5.12.9 of P5 and returns in Chapter 4.
