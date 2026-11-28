---
title: Mori dream spaces and Mori chambers
nodes: []
sources: [HK00, CLS11, BCHM10, Laz04]
reads_with: [HK00:1, CLS11:15]
requires: [1.3, 2.2, 3.7]
level: advanced
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Mori dream spaces and Mori chambers

### Statement

Let $X$ be a normal projective $\mathbb{Q}$-factorial variety over an algebraically closed field of characteristic zero. A *small $\mathbb{Q}$-factorial modification* of $X$ is a birational map $f \colon X \dashrightarrow X'$ to a normal projective $\mathbb{Q}$-factorial variety that is an isomorphism in codimension one. The movable cone $\overline{\mathrm{Mov}}(X)$ is the closed cone in $N^1(X)_{\mathbb{R}}$ spanned by the classes of divisors whose stable base locus has codimension at least two.

**Definition 9.6.1 (Mori dream space, Hu and Keel).** Following HK00, Definition 1.10, $X$ is a *Mori dream space* if

1. $\operatorname{Pic}(X)_{\mathbb{Q}} = N^1(X)_{\mathbb{Q}}$;
2. $\operatorname{Nef}(X)$ is the cone spanned by finitely many semiample line bundles;
3. there are finitely many small $\mathbb{Q}$-factorial modifications $f_i \colon X \dashrightarrow X_i$ such that each $X_i$ satisfies condition 2 and $\overline{\mathrm{Mov}}(X) = \bigcup_i f_i^* \operatorname{Nef}(X_i)$.

**Definition 9.6.2 (Cox ring).** Suppose $\operatorname{Pic}(X)$ is free of finite rank $\rho$, with a basis given by line bundles $\mathcal{O}_X(L_1), \ldots, \mathcal{O}_X(L_\rho)$ for Cartier divisors $L_i$. The *Cox ring* of $X$ is
$$\operatorname{Cox}(X) = \bigoplus_{\mathbf{m} \in \mathbb{Z}^\rho} H^0\bigl(X, \mathcal{O}_X(m_1 L_1 + \cdots + m_\rho L_\rho)\bigr),$$
with multiplication of sections; it is a $\mathbb{Z}^\rho$-graded domain, a subring of $k(X)[t_1^{\pm 1}, \ldots, t_\rho^{\pm 1}]$, and up to isomorphism it does not depend on the basis.

**Theorem 9.6.3 (Hu and Keel).** Let $X$ be a normal projective $\mathbb{Q}$-factorial variety with $\operatorname{Pic}(X)$ free of finite rank and $\operatorname{Pic}(X)_{\mathbb{Q}} = N^1(X)_{\mathbb{Q}}$.

1. $X$ is a Mori dream space if and only if $\operatorname{Cox}(X)$ is a finitely generated $k$-algebra.
2. If $X$ is a Mori dream space, then $\overline{\mathrm{Eff}}(X)$ and $\overline{\mathrm{Mov}}(X)$ are rational polyhedral cones, the section ring $R(X, D)$ is finitely generated for every divisor $D$, $\overline{\mathrm{Eff}}(X)$ is the union of finitely many Mori chambers (Definition 9.6.4), and for every divisor $D$ the minimal model program for $D$ can be run and terminates, with each step a divisorial contraction, a flip for $D$, or a fibration, and each model one of the finitely many models of the chambers.

Lean: not yet in Lean.

**Definition 9.6.4 (Mori chambers).** Let $X$ be a Mori dream space. For an effective $\mathbb{Q}$-divisor $D$ let $\varphi_D \colon X \dashrightarrow X(D) = \operatorname{Proj} R(X, D)$ be its ample model. Two effective divisors $D$, $D'$ are *Mori equivalent* if $\varphi_D$ and $\varphi_{D'}$ agree up to an isomorphism of the targets. A *Mori chamber* is the closure of a Mori equivalence class whose interior in $N^1(X)_{\mathbb{R}}$ is nonempty.

**Theorem 9.6.5 (projective toric varieties are Mori dream spaces).** Let $X = X_\Sigma$ be a projective $\mathbb{Q}$-factorial toric variety, that is, $\Sigma$ is a complete simplicial fan with $X_\Sigma$ projective. Then $X$ is a Mori dream space, and its Mori chambers are the maximal cones of the secondary fan of Definition 3.7.10 that lie in the effective cone.

Lean: not yet in Lean.

### Proof in words

Hu and Keel prove Theorem 9.6.3 by variation of geometric invariant theory: a finitely generated Cox ring presents $X$ as a GIT quotient of the affine variety $\operatorname{Spec} \operatorname{Cox}(X)$ by the torus $\operatorname{Hom}(\operatorname{Pic} X, \mathbb{G}_m)$, and the GIT chambers of the characters are the Mori chambers. Conversely the finitely many models and their semiample nef cones make every graded piece of the Cox ring a finite sum of pieces controlled by finitely many semiample divisors, and Gordan's lemma assembles these into finitely many generators. The theorem is cited.

For a toric variety the Cox ring is the polynomial ring in one variable for each ray of the fan, by the theorem of Cox, and the chambers are those of the secondary fan, along which the toric minimal model program of Volume 3 walks.

### Examples

**Example 9.6.6 (the chambers of $\mathbb{F}_n$).** Let $n \ge 1$ and $X = \mathbb{F}_n$ with negative section $C_-$, $C_-^2 = -n$, and fibre $F$. By Example 1.3.22, $\overline{\mathrm{Eff}}(X)$ is spanned by $C_-$ and $F$, and $D = aC_- + bF$ with $a, b \ge 0$ is nef if and only if $b \ge na$, so $\operatorname{Nef}(X) = \langle F, C_- + nF \rangle$. Since $X$ is a surface, a small $\mathbb{Q}$-factorial modification is an isomorphism and $\overline{\mathrm{Mov}}(X) = \operatorname{Nef}(X)$. The ample models are as follows.

1. In the interior of $\operatorname{Nef}(X)$, $D$ is ample and $X(D) = \mathbb{F}_n$.
2. On the ray $\mathbb{R}_{> 0} F$, $D$ is the pullback of $\mathcal{O}_{\mathbb{P}^1}(b)$, and $X(D) = \mathbb{P}^1$.
3. For $0 \le b < na$ with $b > 0$, the Zariski decomposition is $P = \frac{b}{n}(C_- + nF)$, $N = (a - \frac{b}{n}) C_-$ (Example 1.3.22), and by Proposition 9.5.9 of Chapter 5, $R(X, D)$ agrees up to a Veronese subring with $R(X, C_- + nF)$. The divisor $C_- + nF$ is nef, big and free, contracts exactly $C_-$, and maps $\mathbb{F}_n$ onto the cone over the rational normal curve of degree $n$, the weighted projective plane $\mathbb{P}(1, 1, n)$; for $n = 1$ this is $\mathbb{P}^2$. So $X(D) = \mathbb{P}(1, 1, n)$, also on the ray $b = na$.
4. On the ray $\mathbb{R}_{> 0} C_-$, $h^0(X, mC_-) = 1$ for all $m$, and $X(D)$ is a point.

So there are two Mori chambers, $\operatorname{Nef}(X) = \langle F, C_- + nF \rangle$ with model $\mathbb{F}_n$ and $\langle C_- + nF, C_- \rangle$ with model $\mathbb{P}(1, 1, n)$; the rays $F$ and $C_-$ carry the lower-dimensional models $\mathbb{P}^1$ and a point. This is the secondary fan of $\mathbb{F}_n$ of Example 3.7.17 in Volume 3.

**Example 9.6.7 (the five chambers of the plane blown up at two points).** Let $X = S_2$ be the blow-up of $\mathbb{P}^2$ at two points $p$, $q$, with exceptional curves $E_1$, $E_2$, $L$ the pullback of a line, and $E_{12} \sim L - E_1 - E_2$ the strict transform of the line through $p$ and $q$. These are the three $(-1)$-curves, and by Theorem 2.2.2, $\overline{\mathrm{Eff}}(X) = \overline{NE}(X) = \langle E_1, E_2, E_{12} \rangle$. For $D = aL - b_1 E_1 - b_2 E_2$ one has $D \cdot E_1 = b_1$, $D \cdot E_2 = b_2$ and $D \cdot E_{12} = a - b_1 - b_2$, so $\operatorname{Nef}(X)$ is cut out by $b_1, b_2 \ge 0$ and $b_1 + b_2 \le a$, with extremal rays $L$, $L - E_1$ and $L - E_2$. In terms of the generators of the effective cone,
$$L = E_1 + E_2 + E_{12}, \qquad L - E_1 = E_2 + E_{12}, \qquad L - E_2 = E_1 + E_{12}.$$
In the plane section of the cone with barycentric coordinates relative to $E_1, E_2, E_{12}$, the class $L$ is the barycentre and $L - E_1$, $L - E_2$ are the midpoints of the sides $E_2 E_{12}$ and $E_1 E_{12}$. The five chambers and their models are:

1. $\operatorname{Nef}(X) = \langle L, L - E_1, L - E_2 \rangle$, model $X$;
2. $\langle L, L - E_2, E_1 \rangle$: here $D = \alpha L + \beta(L - E_2) + \gamma E_1$ with $\alpha, \beta, \gamma \ge 0$, the Zariski decomposition is $P = \alpha L + \beta(L - E_2)$, $N = \gamma E_1$, since $P$ is nef with $P \cdot E_1 = 0$, and the model is the contraction of $E_1$, which is $\mathbb{F}_1$;
3. $\langle L, L - E_1, E_2 \rangle$: symmetrically, the contraction of $E_2$, again $\mathbb{F}_1$;
4. $\langle L, E_1, E_2 \rangle$: $P = \alpha L$, $N = \beta E_1 + \gamma E_2$, the model is $\mathbb{P}^2$;
5. $\langle L - E_1, L - E_2, E_{12} \rangle$: $P = \alpha(L - E_1) + \beta(L - E_2)$ with $P \cdot E_{12} = 0$, $N = \gamma E_{12}$, and contracting $E_{12}$ gives $\mathbb{P}^1 \times \mathbb{P}^1$, with $L - E_1$ and $L - E_2$ the pullbacks of the two rulings.

In the triangle with vertices $E_1, E_2, E_{12}$, these are the triangles $(L, M_1, M_2)$, $(L, M_2, E_1)$, $(L, M_1, E_2)$, $(L, E_1, E_2)$ and $(M_1, M_2, E_{12})$, with $M_1 = L - E_1$ and $M_2 = L - E_2$. The four triangles with vertex $L$ fill the angle around $L$, because the rays from $L$ towards $E_1$, $M_2$, $M_1$, $E_2$ occur in this cyclic order, and the corner triangle at $E_{12}$ fills the rest of the quadrilateral $(L, M_2, E_{12}, M_1)$. So the five chambers tile $\overline{\mathrm{Eff}}(X)$ with disjoint interiors, the decomposition predicted by Theorem 9.6.3. The faces between them carry the lower-dimensional models: the ray $L - E_1$ gives the fibration $X \to \mathbb{P}^1$ from the pencil of lines through $p$, and so on.

### Proof

*Proof of Theorem 9.6.3.* This is Proposition 2.9 of Hu and Keel (HK00) for part 1, together with their Proposition 1.11 for part 2; it is cited. $\square$

*Proof of Theorem 9.6.5.* Since $\Sigma$ is simplicial, $X$ is $\mathbb{Q}$-factorial. For a complete toric variety the Picard group is free of finite rank and numerical and linear equivalence agree on Cartier divisors (CLS11, Chapter 6), so $\operatorname{Pic}(X)_{\mathbb{Q}} = N^1(X)_{\mathbb{Q}}$. By the theorem of Cox (CLS11, Chapter 5), the ring $\bigoplus_{[D] \in \operatorname{Cl}(X)} H^0(X, \mathcal{O}_X(D))$ is the polynomial ring $k[x_\rho : \rho \in \Sigma(1)]$, graded by the class group. As $X$ is $\mathbb{Q}$-factorial, $\operatorname{Pic}(X)$ is a subgroup of finite index of $\operatorname{Cl}(X)$, and $\operatorname{Cox}(X)$ is the part of the polynomial ring of degrees in $\operatorname{Pic}(X)$, which is the ring of invariants of the finite diagonalizable group $\operatorname{Hom}(\operatorname{Cl}(X)/\operatorname{Pic}(X), \mathbb{G}_m)$ acting through the grading. Invariants of a finite group acting on a finitely generated algebra in characteristic zero are finitely generated, so $\operatorname{Cox}(X)$ is finitely generated, and $X$ is a Mori dream space by Theorem 9.6.3. The description of the chambers is the identification of the GIT chambers of the torus action on $\mathbb{A}^{\Sigma(1)}$ with the cones of the secondary fan, as in Volume 3 (Theorem 3.7.9 and Corollary 3.7.14). $\square$

### Exercises

1. (B) Compute the Cox ring of $\mathbb{F}_n$ as a polynomial ring in four variables with its $\mathbb{Z}^2$-grading, and recover the two chambers of Example 9.6.6 as the GIT chambers.
2. (B) For $X = \mathbb{P}^1 \times \mathbb{P}^1$ show that $\overline{\mathrm{Eff}}(X) = \operatorname{Nef}(X)$ is a single chamber, and list the ample models on its two boundary rays.
3. (B) In Example 9.6.7, determine the ample model of every class on each of the nine boundary segments and rays of the five chambers.
4. (B) Let $X = S_3$ be the plane blown up at three non-collinear points. Show that $\overline{\mathrm{Eff}}(X)$ has six extremal rays, the six $(-1)$-curves, and count the Mori chambers that contain $L$ in their boundary.
5. (C) Let $X$ be the blow-up of $\mathbb{P}^3$ at two points, with exceptional divisors $E_1$, $E_2$ and $H$ the pullback of a plane. The strict transform of the line through the points has normal bundle $\mathcal{O}(-1)^{\oplus 2}$. Show that $X$ has a small $\mathbb{Q}$-factorial modification $X \dashrightarrow X'$ other than the identity, and compute $\overline{\mathrm{Mov}}(X)$ and its decomposition into $\operatorname{Nef}(X)$ and the pullback of $\operatorname{Nef}(X')$.
6. (C) Show that a Mori dream space $X$ has only finitely many contracting birational maps $X \dashrightarrow Y$ to $\mathbb{Q}$-factorial projective varieties, up to isomorphism, using part 2 of Theorem 9.6.3, and give a variety for which this finiteness fails.

### Lean

The project library defines `IsMoriDreamSpace` in `MinimalModel/Statements/Cones.lean`, with the conditions of $\mathbb{Q}$-factoriality, torsion of numerically trivial Cartier divisors up to multiples, and a finitely generated nef cone, following Definition 9.6.1. The theorem of Hu and Keel and the toric case are not formalised.

### Notes and history

Mori dream spaces were introduced by Hu and Keel (HK00), who proved the characterization by finite generation of the Cox ring and related the chamber decomposition to variation of GIT. The Cox ring of a toric variety was introduced by Cox; Cox, Little and Schenck (CLS11) treat it together with the secondary fan and the toric minimal model program. The chamber decomposition of the plane blown up at two points is the simplest case in which every type of model occurs.
