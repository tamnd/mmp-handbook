---
title: The program for smooth surfaces
nodes: [MMRP5RX4JJ, MM8MGCYF75, MM861R2D6G]
sources: [Har77, KM98, Bea96, Mor82]
reads_with: [Har77:V.5, KM98:ch1, Bea96:ch2]
requires: [P0.6, P5, P7]
level: background
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The program for smooth surfaces

### Statement

Let $X$ be a smooth projective surface over $k$. Two divisors $D$ and $D'$ are *numerically equivalent* if $D \cdot C = D' \cdot C$ for every curve $C$ on $X$. The real vector space $N^1(X)$ of $\mathbb{R}$-divisors up to numerical equivalence has finite dimension $\rho(X)$, the *Picard number* (P7). On a surface, curves are divisors, so the space $N_1(X)$ of curves up to numerical equivalence is the same space, and the intersection form is a nondegenerate pairing on it.

**Definition 1.1.1.** The *cone of curves* $NE(X) \subset N_1(X)$ is the set of classes $\sum a_i [C_i]$ with $a_i \ge 0$ and $C_i$ curves. Its closure is $\overline{NE}(X)$. For a divisor $D$, write $\overline{NE}(X)_{D \ge 0} = \{ z \in \overline{NE}(X) : D \cdot z \ge 0 \}$. A ray $R = \mathbb{R}_{\ge 0} z$ in $\overline{NE}(X)$ is *extremal* if $a, b \in \overline{NE}(X)$ and $a + b \in R$ give $a, b \in R$.

Lean: `MinimalModel.IntersectionData.coneOfCurves` (the closure of the cone spanned by the curve classes) and `MinimalModel.ExtremalRay`, in the project library.

**Definition 1.1.2.** A *$(-1)$-curve* on $X$ is an irreducible curve $E$ with $E^2 = -1$ and $K_X \cdot E = -1$. By the adjunction formula $2p_a(E) - 2 = E^2 + K_X \cdot E = -2$, so $p_a(E) = 0$ and $E \cong \mathbb{P}^1$.

Lean: not a separate definition; the hypotheses of `MinimalModel.Castelnuovo` are the two intersection numbers.

**Theorem 1.1.3 (Castelnuovo).** Let $E$ be a $(-1)$-curve on a smooth projective surface $X$. Then there is a smooth projective surface $Y$, a point $p \in Y$ and a morphism $f \colon X \to Y$ with $f(E) = p$, such that $f$ maps $X \setminus E$ isomorphically onto $Y \setminus \{p\}$. The morphism $f$ is the blow-up of $Y$ at $p$.

Node: MMRP5RX4JJ · Lean: `MinimalModel.Castelnuovo`

**Theorem 1.1.4 (Cone theorem for surfaces).** Let $X$ be a smooth projective surface. Then there are countably many rational curves $C_i$ with $0 < -K_X \cdot C_i \le 3$ such that

$$
\overline{NE}(X) = \overline{NE}(X)_{K_X \ge 0} + \sum_i \mathbb{R}_{\ge 0} [C_i].
$$

Each ray $\mathbb{R}_{\ge 0}[C_i]$ is extremal. For each ample divisor $H$ and each $\varepsilon > 0$, only finitely many of the rays satisfy $(K_X + \varepsilon H) \cdot C_i < 0$.

Node: MM8MGCYF75 · Lean: `MinimalModel.SurfaceConeTheorem`

**Theorem 1.1.5 (Minimal model program for surfaces).** Let $X$ be a smooth projective surface. Then there is a finite sequence of contractions of $(-1)$-curves $X = X_0 \to X_1 \to \cdots \to X_m$, with every $X_i$ a smooth projective surface, such that $X_m$ satisfies one of these conditions.

1. $K_{X_m}$ is nef. Then $X_m$ is a *minimal model* of $X$.
2. There is a morphism $X_m \to B$ onto a smooth curve whose fibres are all smooth rational curves. Then $X_m$ is a $\mathbb{P}^1$-bundle over $B$.
3. $X_m \cong \mathbb{P}^2$.

In cases 2 and 3, $-K_{X_m}$ is ample on the fibres of a morphism to a variety of smaller dimension ($B$ or a point), and $X_m$ is a *Mori fibre space*.

Node: MM861R2D6G · Lean: `MinimalModel.SurfaceMMP`

### Proof in words

Castelnuovo's theorem is proved by a construction of $Y$. Take a very ample divisor $H$ on $X$ with $H^1(X, \mathcal{O}_X(H)) = 0$, and let $a = H \cdot E$. The linear system $|H + aE|$ has degree $(H + aE) \cdot E = a - a = 0$ on $E$, so it maps $E$ to a point. It separates the points and the tangent directions of $X \setminus E$. So its image $Y$ is a surface, and $f$ is an isomorphism off $E$. The hard step is the smoothness of $Y$ at $p = f(E)$. The proof computes the completed local ring of $Y$ at $p$ from the sections of $\mathcal{O}_X(-nE)$ restricted to $E$, and finds a power series ring in two variables (Hartshorne, Section V.5).

The cone theorem for surfaces has a direct proof with Riemann-Roch (KM98, Chapter 1). The main step shows that each $K_X$-negative extremal ray $R$ contains the class of a curve $C$. There are three cases. If $C^2 < 0$, then $K_X \cdot C < 0$ and adjunction give $C^2 = K_X \cdot C = -1$, so $C$ is a $(-1)$-curve. If $C^2 = 0$, then Riemann-Roch shows that $C$ moves in a pencil and gives a morphism to a curve whose fibres all have class in $R$; adjunction gives $p_a(C) = 0$ and $K_X \cdot C = -2$. If $C^2 > 0$, then $[C]$ is in the interior of $\overline{NE}(X)$, so $R$ is extremal only if $\rho(X) = 1$; then $-K_X$ is ample, and the classification of such surfaces gives $X \cong \mathbb{P}^2$ with $-K_X \cdot \ell = 3$ for a line $\ell$. The bound $3$ comes from this last case. In all dimensions, Mori's bend-and-break gives the rational curves (Section 1.3 and Volume 6).

The program follows. If $K_X$ is nef, stop. If not, the cone theorem gives a $K_X$-negative extremal ray. In the first case contract the $(-1)$-curve by Castelnuovo's theorem and repeat. In the other two cases stop at a Mori fibre space. Each contraction lowers $\rho$ by one, so there are at most $\rho(X) - 1$ contractions.

### Examples

Let $X = \mathrm{Bl}_p \mathbb{P}^2$, with $H$ the pullback of a line and $E$ the exceptional curve. Then $N_1(X)$ has the basis $H, E$, with $H^2 = 1$, $H \cdot E = 0$ and $E^2 = -1$. The canonical class is $K_X = -3H + E$. The strict transform of a line through $p$ has class $f = H - E$, with $f^2 = 0$. So

$$
K_X \cdot E = -1, \qquad K_X \cdot f = -3 + 1 = -2.
$$

Every curve $C \ne E$ has $C \cdot E \ge 0$ and $C \cdot f \ge 0$, because $f$ moves. A class $xH - yE$ meets $E$ in $y$ and $f$ in $x - y$, so $x \ge y \ge 0$ for such a curve. Since $xH - yE = x f + (x - y) E$, every curve class is a nonnegative combination of $E$ and $f$. So $\overline{NE}(X)$ is spanned by $E$ and $f$, and both rays are $K_X$-negative. The ray of $E$ gives the blow-down $X \to \mathbb{P}^2$, and the program ends at $\mathbb{P}^2$, case 3. The ray of $f$ gives the ruling $X \to \mathbb{P}^1$ by the lines through $p$, case 2. So the result of the program depends on the choice of the ray, and $X$ has no minimal model: $K_X \cdot f < 0$ for the moving curve $f$, so no blow-down of $X$ has $K$ nef.

Let $S \subset \mathbb{P}^3$ be a smooth quintic surface and $X = \mathrm{Bl}_q S$ for a point $q$. Then $K_S = \mathcal{O}_S(1)$ is ample, and $K_X = \pi^* K_S + E$. The only $K_X$-negative curve is $E$, and the program contracts it and stops at $S$, case 1. In general, when the Kodaira dimension is at least 0, the minimal model is unique.

A hypothesis that fails. On the Hirzebruch surface $\mathbb{F}_2$ the negative section $\sigma$ is a smooth rational curve with $\sigma^2 = -2$. Adjunction gives $K \cdot \sigma = 0$, so $\sigma$ is not a $(-1)$-curve. The curve $\sigma$ can be contracted, but the image is the quadric cone $\mathbb{P}(1, 1, 2)$, with an $A_1$ singularity (P0, Chapter 6). So the conclusion of Castelnuovo's theorem (a smooth $Y$) fails. This contraction is not a step of the program for smooth surfaces, but it is a step of the program for surfaces with singularities (Volume 2).

### Exercises

1. (A) Let $C$ be an irreducible curve on a smooth projective surface with $C^2 < 0$ and $K \cdot C < 0$. Use adjunction to show that $C$ is a $(-1)$-curve.
2. (A) On $\mathbb{F}_n$ let $\sigma$ be the section with $\sigma^2 = -n$. Show that $K \cdot \sigma = n - 2$, and that $\sigma$ is a $(-1)$-curve only for $n = 1$.
3. (A) Show that a surface with $K_X$ nef has no $(-1)$-curve.
4. (B) Let $X$ be the blow-up of $\mathbb{P}^2$ at two points. Find the three $(-1)$-curves of $X$. Show that the program can end at $\mathbb{P}^2$, at $\mathbb{F}_1 \to \mathbb{P}^1$, or at $\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1$.
5. (B) Show that $\rho(\mathrm{Bl}_p Y) = \rho(Y) + 1$, so each contraction of a $(-1)$-curve lowers $\rho$ by one. Conclude that the program has at most $\rho(X) - 1$ steps.
6. (B) Let $X$ be a smooth projective surface with $K_X$ nef. Use the factorization of birational morphisms of smooth surfaces into blow-ups (Hartshorne, Section V.5) to show that each birational morphism from $X$ to a smooth surface is an isomorphism.

### Lean

The intersection numbers in the project library are `MinimalModel.IntersectionData`, a structure that holds the numbers $D \cdot C$ and the finite dimension of $N_1(X)$ (the theorem of the base) as a field. Mathlib has no intersection theory on surfaces. `MinimalModel.Castelnuovo` asks for $E^2 = -1$ and $K \cdot E = -1$ and concludes that a proper morphism to a smooth projective surface maps $E$ to a closed point and is an isomorphism over the complement. It does not say that $f$ is the blow-up. `MinimalModel.SurfaceConeTheorem` leaves out the rationality of the $C_i$ and the bound $3$.

### Notes and history

Castelnuovo proved the contraction criterion around 1900, and Enriques built the classification of surfaces on it. The criterion is Hartshorne, Theorem V.5.7. The view of the surface program as a sequence of contractions of $K$-negative extremal rays is due to Mori (Mor82), who proved the cone theorem for smooth projective varieties of all dimensions. All three statements of this section are theorems. Volume 2 gives the full proofs, the program for surfaces with log terminal singularities, and abundance for surfaces.
