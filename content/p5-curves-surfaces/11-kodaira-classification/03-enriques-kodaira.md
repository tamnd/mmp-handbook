---
title: The Enriques-Kodaira classification
nodes: []
sources: [Bea96, Har77, Rei97]
reads_with: [Bea96:ch8, Har77:V.6, Rei97:ch4]
requires: [P3.12, P4.2, P4.4, P5.5, P5.6, P5.7, P5.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Enriques-Kodaira classification

### Statement

As before, $S$ is a smooth projective surface over an algebraically closed field $k$, and $S_0$ denotes a minimal model of $S$ (Definition P5.11.13). By Theorem P5.11.6, $\kappa(S) = \kappa(S_0)$, and by Corollary P5.11.19, $S_0$ is unique up to isomorphism when $\kappa(S) \geq 0$. The classification describes $S_0$ in each of the four cases $\kappa \in \{-\infty, 0, 1, 2\}$. This section proves the numerical part that follows from Sections 11.1 and 11.2 and states the rest, with references.

**Definition P5.11.23 (the classes of surfaces).**

1. $S$ is *rational* if it is birational to $\mathbb{P}^2$, and *birationally ruled* if it is birational to $C \times \mathbb{P}^1$ for a curve $C$.
2. A *K3 surface* is a surface with $K_S \sim 0$ and $q(S) = 0$.
3. If $\operatorname{char} k \neq 2$, an *Enriques surface* is a surface with $q(S) = p_g(S) = 0$ and $2K_S \sim 0$. Then $K_S \not\sim 0$, since $p_g = 0$.
4. An *abelian surface* is an abelian variety of dimension $2$, that is, a smooth projective connected group variety of dimension $2$.
5. A *bielliptic surface* is a quotient $(E \times F)/G$, where $E$ and $F$ are elliptic curves and $G$ is a finite group of translations of $E$ that acts on $F$ with $F/G \cong \mathbb{P}^1$, through the diagonal action, which is free.
6. An *elliptic fibration* on $S$ is a surjective morphism $f \colon S \to B$ onto a curve whose general fibre is a smooth curve of genus $1$. A *quasi-elliptic fibration* is one whose general fibre is a cuspidal rational curve; these exist only in characteristic $2$ and $3$.
7. $S$ is *of general type* if $\kappa(S) = 2$.

**Proposition P5.11.24 (numerical characters of minimal surfaces with $\kappa \geq 0$).** Let $S$ be minimal with $\kappa(S) \geq 0$.

1. $K_S$ is nef and $K_S^2 \geq 0$.
2. $\kappa(S) = 2$ if and only if $K_S^2 > 0$.
3. If $\kappa(S) \in \{0, 1\}$, then $K_S^2 = 0$. If $\kappa(S) = 0$, then $P_n(S) \in \{0, 1\}$ for all $n$. If $\kappa(S) = 1$, then $P_n(S) \geq 2$ for some $n$.
4. If $mK_S \sim 0$ for some $m \geq 1$, then $\kappa(S) = 0$.

Lean: not in Lean as stated.

**Theorem P5.11.25 (Castelnuovo's rationality criterion).** A smooth projective surface $S$ is rational if and only if $q(S) = P_2(S) = 0$.

Lean: not in Lean as stated.

**Theorem P5.11.26 (the Enriques-Kodaira classification).** Let $S$ be a smooth projective surface over $k$ and $S_0$ a minimal model.

1. ($\kappa = -\infty$.) $\kappa(S) = -\infty$ if and only if $S$ is birationally ruled. Then $S_0$ is $\mathbb{P}^2$ or a geometrically ruled surface $\mathbb{P}(\mathcal{E}) \to C$ over a curve, and $S_0$ is not unique. $S$ is rational exactly when $q(S) = 0$, and otherwise $q(S) = g(C)$.
2. ($\kappa = 0$.) $K_{S_0}$ is numerically trivial and $12 K_{S_0} \sim 0$. If $\operatorname{char} k \neq 2, 3$, then $S_0$ is exactly one of: a K3 surface, an Enriques surface, an abelian surface, or a bielliptic surface, with $(p_g, q) = (1, 0)$, $(0, 0)$, $(1, 2)$ and $(0, 1)$ respectively. In characteristic $2$ and $3$ the same four classes occur, distinguished by the second Betti number $b_2 = 22, 10, 6, 2$ of $\ell$-adic cohomology, but the class with $b_2 = 2$ also contains *quasi-hyperelliptic* surfaces, quotients of $E \times C$ with $C$ a cuspidal rational curve, and in characteristic $2$ there are Enriques surfaces, in the sense of Bombieri and Mumford, with $K \sim 0$ and $p_g = q = 1$.
3. ($\kappa = 1$.) $K_{S_0}^2 = 0$, and $S_0$ has an elliptic fibration, or, only in characteristic $2$ and $3$, a quasi-elliptic fibration $f \colon S_0 \to B$, such that $nK_{S_0} \sim f^* D$ for some $n \geq 1$ and some divisor $D$ of positive degree on $B$. For $n$ large and divisible, $\varphi_{|nK_{S_0}|}$ is $f$ followed by an embedding of $B$.
4. ($\kappa = 2$.) $K_{S_0}^2 > 0$, and $S_0$ is the unique minimal model. If $\operatorname{char} k = 0$, then $\chi(\mathcal{O}_S) > 0$, $K_{S_0}^2 \geq 2 p_g - 4$ (Noether's inequality), $K_{S_0}^2 \leq 9 \chi(\mathcal{O}_S)$ (the Bogomolov-Miyaoka-Yau inequality), and $\varphi_{|nK_{S_0}|}$ is birational onto its image for every $n \geq 5$.

Lean: not in Lean as stated.

In characteristic $0$, Enriques's theorem says that $S$ is birationally ruled if and only if $P_{12}(S) = 0$, so the classification is decided by finitely many plurigenera and the irregularity.

### Proof in words

The numerical part is a consequence of the nefness of $K$ on a minimal surface with $\kappa \geq 0$. A nef divisor $K$ with $mK$ effective has $K^2 \geq 0$. If $K^2 > 0$, Riemann-Roch makes $h^0(nK)$ grow like $n^2$. Conversely, if $\kappa = 2$, a multiple of $K$ is an ample divisor plus an effective one, and nefness turns this into $K^2 > 0$. The easy half of Castelnuovo's criterion is birational invariance applied to $\mathbb{P}^2$.

The rest of Theorem P5.11.26 is not proved in this handbook. Its proof has three parts of different nature. For $\kappa = -\infty$ one must produce a rational curve that moves, starting from $P_{12} = 0$ or from $K$ not nef, which is Castelnuovo's and Enriques's analysis of adjoint linear systems $|C + nK|$, or, in the language of Chapter 12, the cone theorem. For $\kappa = 0$ and $\kappa = 1$ one must show that $K$ is torsion or semiample, which uses Noether's formula, the Albanese map and a careful study of elliptic fibrations, including Kodaira's list of singular fibres. For $\kappa = 2$ the statements are effective results on pluricanonical maps.

### Examples

**Example P5.11.27 (the table of invariants).** Over $k = \mathbb{C}$, the minimal surfaces with $\kappa \leq 1$, and the minimal surfaces of general type, have the following invariants. Here $\chi = \chi(\mathcal{O}_S) = 1 - q + p_g$, $e$ is the topological Euler number, and $b_1 = 2q$.

| class | $\kappa$ | $p_g$ | $q$ | $K^2$ | $b_2$ |
|---|---|---|---|---|---|
| $\mathbb{P}^2$ | $-\infty$ | $0$ | $0$ | $9$ | $1$ |
| geometrically ruled over a curve of genus $g$ | $-\infty$ | $0$ | $g$ | $8(1 - g)$ | $2$ |
| K3 | $0$ | $1$ | $0$ | $0$ | $22$ |
| Enriques | $0$ | $0$ | $0$ | $0$ | $10$ |
| abelian | $0$ | $1$ | $2$ | $0$ | $6$ |
| bielliptic | $0$ | $0$ | $1$ | $0$ | $2$ |
| elliptic with $\kappa = 1$ | $1$ | $\geq 0$ | $\geq 0$ | $0$ | $12\chi - 2 + 4q$ |
| general type | $2$ | $\geq 0$ | $\geq 0$ | $\geq 1$ | $12\chi - K^2 - 2 + 4q$ |

The columns $p_g$, $q$ and $K^2$ are proved in this chapter for one member of each of the first five rows that the handbook constructs: $\mathbb{P}^2$ in Example P5.11.7, $C \times \mathbb{P}^1$ in Example P5.11.8, the quartic surface and $E \times E'$ in Example P5.11.9, and the Enriques surface of Example P5.11.28 below. Within each class they are constant, by the cited Theorem P5.11.26. The surfaces $E \times C$ with $g(C) \geq 2$ of Example P5.11.10 lie in the row $\kappa = 1$, with $p_g = g$, $q = g + 1$, $\chi = 0$ and $b_2 = 4g + 2$, and the quintic and $C_1 \times C_2$ of Examples P5.11.11 and P5.11.12 in the last row. The column $b_2$ comes from Noether's formula $12 \chi = K^2 + e$ (Beauville, Chapter I) and $e = 2 - 2b_1 + b_2$, which give $b_2 = 12\chi - K^2 - 2 + 4q$. For instance a K3 surface has $\chi = 2$ and $b_2 = 24 - 2 = 22$, an abelian surface has $\chi = 0$ and $b_2 = -2 + 8 = 6$, a ruled surface has $\chi = 1 - g$ and $b_2 = 12(1 - g) - 8(1 - g) - 2 + 4g = 2$, and the quintic has $\chi = 5$, $K^2 = 5$ and $b_2 = 60 - 5 - 2 = 53$.

**Example P5.11.28 (an Enriques surface).** Let $\operatorname{char} k \neq 2$, and in $\mathbb{P}^5$ with coordinates $x_0, x_1, x_2, y_0, y_1, y_2$ let
$$X = V_+(Q_1, Q_2, Q_3), \qquad Q_i = A_i(x_0, x_1, x_2) + B_i(y_0, y_1, y_2),$$
with $A_i$, $B_i$ quadratic forms. For a general choice, $X$ is a smooth surface, the conics $V(A_1), V(A_2), V(A_3) \subseteq \mathbb{P}^2$ have no common point, and neither do the $V(B_i)$ (Beauville, Chapter VIII). By the second part of Corollary P3.12.31 applied three times, $\omega_X \cong \mathcal{O}_X(2 + 2 + 2 - 6) = \mathcal{O}_X$, and $q(X) = 0$ because $H^1(\mathcal{O}) = 0$ for complete intersections of dimension at least $2$ (Hartshorne, Exercise III.5.5). So $X$ is a K3 surface, with $\chi(\mathcal{O}_X) = 2$. The involution $\sigma(x, y) = (x, -y)$ preserves $X$. Its fixed points in $\mathbb{P}^5$ are the points with $y = 0$ or $x = 0$, and $X$ meets these planes in $V(A_1, A_2, A_3) = \emptyset$ and $V(B_1, B_2, B_3) = \emptyset$. So $\sigma$ acts freely on $X$.

The quotient by a free action of $\mathbb{Z}/2$ (Mumford, *Abelian varieties*, Section 7) is a smooth projective surface $Y$ with a finite étale morphism $f \colon X \to Y$ of degree $2$, and $f_* \mathcal{O}_X = \mathcal{O}_Y \oplus \mathcal{L}$, where $\mathcal{L}$ is the $(-1)$-eigensheaf of $\sigma$, with $\mathcal{L}^{\otimes 2} \cong \mathcal{O}_Y$ and $f^* \mathcal{L} \cong \mathcal{O}_X$. Since $f$ is étale, $f^* \omega_Y \cong \omega_X \cong \mathcal{O}_X$. The invariants of $Y$ follow from the handbook.

1. Since $2\mathcal{L} \sim 0$, $\mathcal{L} \cdot D = \frac{1}{2}(2\mathcal{L}) \cdot D = 0$ for all $D$, so Riemann-Roch (Theorem P5.5.13) gives $\chi(\mathcal{L}) = \chi(\mathcal{O}_Y)$. As $f$ is finite, hence affine, $H^i(X, \mathcal{O}_X) = H^i(Y, f_* \mathcal{O}_X)$ by Corollary P4.4.3, so $2 = \chi(\mathcal{O}_X) = 2\chi(\mathcal{O}_Y)$ and $\chi(\mathcal{O}_Y) = 1$.
2. $H^1(\mathcal{O}_Y)$ is a direct summand of $H^1(Y, f_* \mathcal{O}_X) = H^1(\mathcal{O}_X) = 0$, so $q(Y) = 0$ and $p_g(Y) = \chi(\mathcal{O}_Y) - 1 + q(Y) = 0$.
3. Let $\mathcal{M}$ be invertible on $Y$ with $f^* \mathcal{M} \cong \mathcal{O}_X$. By the projection formula, $H^0(Y, \mathcal{M}^{-1}) \oplus H^0(Y, \mathcal{M}^{-1} \otimes \mathcal{L}) = H^0(X, f^* \mathcal{M}^{-1}) = k$, so $\mathcal{N} = \mathcal{M}^{-1}$ or $\mathcal{N} = \mathcal{M}^{-1} \otimes \mathcal{L}$ has a nonzero section, with divisor $F \geq 0$. Then $f^* \mathcal{N} \cong \mathcal{O}_X$, so $f^* F$ is an effective divisor linearly equivalent to $0$. For an ample $H$ on $X$ this gives $H \cdot f^* F = 0$, while every component $C$ of $f^* F$ has $H \cdot C > 0$ by Lemma P5.5.20, so $f^* F = 0$. Since $f$ is surjective, $F = 0$. So $\mathcal{M} \cong \mathcal{O}_Y$ or $\mathcal{M} \cong \mathcal{L}$.
4. Applied to $\mathcal{M} = \omega_Y$, and since $p_g(Y) = 0$ excludes $\omega_Y \cong \mathcal{O}_Y$, this gives $\omega_Y \cong \mathcal{L}$. So $2K_Y \sim 0$ and $K_Y \not\sim 0$.

So $Y$ is an Enriques surface: $P_n(Y) = 1$ for $n$ even and $P_n(Y) = 0$ for $n$ odd, $\kappa(Y) = 0$, $K_Y^2 = 0$, and $Y$ is minimal since $K_Y \equiv 0$ is nef. It has $q = p_g = 0$ and is not rational, because $P_2(Y) = 1$. This is the example by which Enriques showed in 1896 that $q = p_g = 0$ does not imply rationality, and the reason why Castelnuovo's criterion involves $P_2$.

**Example P5.11.29 (rationality from Castelnuovo's criterion).** Let $X \subseteq \mathbb{P}^3$ be a smooth cubic surface. By Example P5.11.11, $q(X) = 0$ and $P_2(X) = 0$, since $2K_X = -2H$. So $X$ is rational by Theorem P5.11.25. Chapter 10 makes this explicit by exhibiting $X$ as $\mathbb{P}^2$ blown up in six points, which is the direct route, and gives $K_X^2 = 9 - 6 = 3$, the degree of $X$. The same argument applies to every smooth surface with $-K$ ample, since then $h^0(nK) = 0$ for $n \geq 1$, as long as $q = 0$. For the surfaces $C \times \mathbb{P}^1$ with $g(C) \geq 1$, $P_2 = 0$ but $q = g \neq 0$, so the condition $q = 0$ is needed as well.

**Example P5.11.30 (fibrations defined by the canonical system).** On $S = E \times C$ with $g(C) \geq 2$, the second projection $q \colon S \to C$ is an elliptic fibration with all fibres isomorphic to $E$, and $nK_S = q^*(nK_C)$, a divisor of degree $n(2g - 2) > 0$ on $C$ pulled back, as part 3 of Theorem P5.11.26 predicts. By Lemma P5.11.4, every section of $nK_S$ is the pullback of a section of $nK_C$, so for $n \geq 3$, when $nK_C$ is very ample (Corollary P5.1.20), $\varphi_{|nK_S|}$ is $q$ followed by the embedding $\varphi_{|nK_C|}$. On $C_1 \times C_2$ with $g_i \geq 2$, instead, $|nK|$ separates points for $n \geq 3$, since it contains $p_1^* |nK_{C_1}| + p_2^* |nK_{C_2}|$, and $\varphi_{|nK|}$ is the Segre product of the two embeddings, so birational as part 4 predicts. On an abelian or K3 surface $|nK| = \{0\}$ and $\varphi_{|nK|}$ maps to a point.

### Proof

*Proposition P5.11.24.* (1) is Proposition P5.11.17.

(2) Fix a very ample $H$ as in Proposition P5.11.3. Suppose $K^2 > 0$. Since $K$ is nef and $H$ is linearly equivalent to an integral curve, $K \cdot H \geq 0$. If $K \cdot H = 0$, the Hodge index theorem (Theorem P5.5.22) gives $K^2 \leq 0$. So $K \cdot H > 0$, and $\kappa(S) = 2$ by part 4 of Proposition P5.11.3. Conversely let $\kappa(S) = 2$. By part 5 of Proposition P5.11.3, $aK \sim A + F$ with $a \geq 1$, $A$ ample and $F$ effective. Then
$$a^2 K^2 = aK \cdot (A + F) \geq aK \cdot A = A^2 + F \cdot A > 0,$$
using $aK \cdot F \geq 0$, since $K$ is nef and $F$ is a nonnegative combination of integral curves, and $A^2 > 0$, $F \cdot A \geq 0$ by Lemma P5.5.20.

(3) By (1) and (2), $\kappa \leq 1$ gives $K^2 = 0$. The statements about $P_n$ are part 3 of Proposition P5.11.3.

(4) If $mK \sim 0$, then $h^0(nmK) = 1$ for all $n$, and $h^0(jK) \leq 1$ for all $j$: if $h^0(jK) \geq 2$, then $h^0(jmK) \geq 2$ by part 3 of Proposition P5.11.3 and its proof, while $jmK \sim 0$ and $h^0(\mathcal{O}_S) = 1$. So $\kappa(S) = 0$. $\square$

*Theorem P5.11.25.* If $S$ is rational, then $q(S) = q(\mathbb{P}^2) = 0$ and $P_2(S) = P_2(\mathbb{P}^2) = 0$ by Theorem P5.11.6 and Example P5.11.7. The converse is not proved in this handbook. Over $\mathbb{C}$ it is Beauville, Theorem V.1, and in every characteristic it is due to Zariski (1958); Hartshorne, Section V.6, states it in the form $p_a = P_2 = 0$, which is equivalent: $P_2 = 0$ forces $p_g = 0$, because the square of a nonzero section of $K$ is a nonzero section of $2K$, and then $p_a = \chi(\mathcal{O}_S) - 1 = -q$. $\square$

*Theorem P5.11.26.* This theorem is cited without proof; only the inequalities $K_{S_0}^2 = 0$ for $\kappa \in \{0, 1\}$ and $K_{S_0}^2 > 0$ for $\kappa = 2$ are proved here, in Proposition P5.11.24, and the uniqueness of $S_0$ for $\kappa \geq 0$ in Corollary P5.11.19, while the non-uniqueness for $\kappa = -\infty$ is Example P5.11.20. In characteristic $0$ the theorem is Beauville, Chapters VI to X: the case $\kappa = -\infty$ is Enriques's theorem of Chapter VI, the case $\kappa = 0$ is Chapter VIII, $\kappa = 1$ is Chapter IX and $\kappa = 2$ is Chapter X. Bombieri's theorem on the pluricanonical maps (1973) gives the last claim of part 4. In characteristic $p > 0$ the theorem is due to Zariski for $\kappa = -\infty$, to Mumford (1969) for the surfaces with $\kappa \geq 0$ and $\chi$ arbitrary, and to Bombieri and Mumford (1976, 1977) for $\kappa = 0$ and $\kappa = 1$, including the quasi-hyperelliptic and quasi-elliptic cases. Hartshorne, Section V.6, gives a summary in every characteristic. The minimal models for $\kappa = -\infty$ are described in Chapter 9, Theorems P5.9.17 and P5.9.20. $\square$

### Exercises

1. (A) Verify the column $b_2$ of Example P5.11.27 for every row from Noether's formula, and compute $e$ for each of the first six rows.
2. (A) Let $X \subseteq \mathbb{P}^4$ be a smooth complete intersection of two quadrics. Show that $K_X = -H$, that $q(X) = P_2(X) = 0$, and conclude that $X$ is rational.
3. (B) Let $S$ be minimal with $\kappa(S) \in \{0, 1\}$, and $mK_S \sim F = \sum a_i C_i \neq 0$ with $a_i > 0$. Show that $K_S \cdot C_i = 0$ for every $i$, and that $F^2 = 0$.
4. (B) Show that every integral curve $C$ on the Enriques surface $Y$ of Example P5.11.28 has $C^2$ even and $C^2 \geq -2$, so that $Y$ contains no $(-1)$-curve, and use Riemann-Roch to show that $\chi(\mathcal{O}_Y(D)) = 1 + \frac{1}{2} D^2$ for every divisor $D$.
5. (B) Using only Theorem P5.11.6, show that no two of the four classes with $\kappa = 0$ of Theorem P5.11.26 in characteristic $0$ contain birational surfaces, and that a surface with $\kappa = 0$ is never birational to one with $\kappa = 1$.
6. (C) Let $S$ be a minimal surface of general type. Show that $h^0(-K_S) = 0$ and $P_2(S) \geq \chi(\mathcal{O}_S) + K_S^2$, and check that equality holds for the quintic surface and for $C_1 \times C_2$ with $g_1, g_2 \geq 2$.

### Lean

Mathlib has abelian varieties neither as projective group schemes nor through their invariants, and it does not define K3, Enriques or elliptic surfaces, plurigenera or Kodaira dimension, so none of the statements of this section can be stated there. The handbook adds no `MinimalModel` node here.

### Notes and history

The classification goes back to the Italian school. Castelnuovo proved the rationality criterion in 1896 and Enriques constructed the surface of Example P5.11.28 in the same years. Enriques's book *Le superficie algebriche* (1949) contains the classification of algebraic surfaces over $\mathbb{C}$ in terms of plurigenera, with $P_{12}$ characterizing ruled surfaces. Kodaira extended it to all compact complex surfaces in *On the structure of compact complex analytic surfaces* I to IV (1964 to 1968), including the non-algebraic surfaces of class VII, and gave the list of singular fibres of elliptic fibrations. The algebraic theory over $\mathbb{C}$ was rewritten in Shafarevich's seminar (1965) and in Beauville's book, which this section follows. In characteristic $p$, Zariski proved Castelnuovo's criterion (1958), Mumford treated the general case (1969), and Bombieri and Mumford completed the cases $\kappa = 0$ and $\kappa = 1$ in *Enriques' classification of surfaces in char. p*, II (1977) and III (1976), finding the quasi-hyperelliptic surfaces and the non-classical Enriques surfaces of characteristic $2$. The literature state is theorem. The Bogomolov-Miyaoka-Yau inequality is due to Miyaoka and Yau (1977) and fails in characteristic $p$. In the language of the minimal model program, the classification is abundance for surfaces: on a minimal surface with $\kappa \geq 0$ the nef divisor $K$ is semiample, and $\kappa$ is the dimension of the image of its Iitaka fibration. Chapter 12 recovers the first step, the existence of the minimal model or of a Mori fibre space, from the cone theorem.
