---
title: The cone of curves and the cone theorem
nodes: [MMV4DPSCE3, MMDZBZY2BV]
sources: [KM98, Laz04, Deb01, Kle66, Mor82, KMM87, Fuj11]
reads_with: [KM98:ch1, KM98:ch3, Laz04:ch1, Deb01:ch1]
requires: [P7, 1.2]
level: background
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The cone of curves and the cone theorem

### Statement

Let $X$ be a projective normal variety over $k$. A *curve* on $X$ is an integral closed subscheme of dimension 1. For a Cartier divisor $D$ and a curve $C$, the number $D \cdot C$ is the degree of $\mathcal{O}_X(D)|_C$ (P7). It is linear in $D$, so it extends to $\mathbb{R}$-Cartier divisors.

**Definition 1.1.8.** Let $Z_1(X)_{\mathbb{R}}$ be the real vector space of finite sums $\sum a_i C_i$ of curves, and $N^1(X)$ the space of $\mathbb{R}$-Cartier divisors up to numerical equivalence. A 1-cycle $z$ is *numerically trivial* if $D \cdot z = 0$ for every Cartier divisor $D$. Then $N_1(X)$ is $Z_1(X)_{\mathbb{R}}$ modulo the numerically trivial cycles. The intersection pairing $N^1(X) \times N_1(X) \to \mathbb{R}$ is perfect, and both spaces have the finite dimension $\rho(X)$. The *cone of curves* $NE(X) \subset N_1(X)$ is the cone of classes of effective 1-cycles, and $\overline{NE}(X)$ is its closure. For a class $D \in N^1(X)$, $\overline{NE}(X)_{D \ge 0}$ is the part where $D$ is nonnegative. An *extremal ray* is a ray $R \subset \overline{NE}(X)$ with $a + b \in R$ for $a, b \in \overline{NE}(X)$ only if $a, b \in R$.

Lean: `MinimalModel.IntersectionData.N₁`, `MinimalModel.IntersectionData.coneOfCurves` and `MinimalModel.ExtremalRay`, in the project library.

The finite dimension of $N_1(X)$ comes from the theorem of the base (Néron and Severi, P7). The handbook uses it as a black box.

**Theorem 1.1.9 (Kleiman's criterion).** Let $X$ be a projective variety and $D$ an $\mathbb{R}$-Cartier divisor. Then $D$ is ample if and only if $D \cdot z > 0$ for every nonzero $z \in \overline{NE}(X)$.

Node: MMV4DPSCE3

So the nef cone and the closed cone of curves are dual: $D$ is nef if and only if $D \ge 0$ on $\overline{NE}(X)$, and the ample cone is the interior of the nef cone.

**Theorem 1.1.10 (Cone theorem).** Let $(X, \Delta)$ be a projective klt pair. Then there are countably many rational curves $C_i \subset X$ with $0 < -(K_X + \Delta) \cdot C_i \le 2 \dim X$ such that

$$
\overline{NE}(X) = \overline{NE}(X)_{K_X + \Delta \ge 0} + \sum_i \mathbb{R}_{\ge 0} [C_i].
$$

Each ray $\mathbb{R}_{\ge 0}[C_i]$ is extremal. For each ample $\mathbb{R}$-divisor $H$ and each $\varepsilon > 0$,

$$
\overline{NE}(X) = \overline{NE}(X)_{K_X + \Delta + \varepsilon H \ge 0} + \sum_{\text{finite}} \mathbb{R}_{\ge 0} [C_i].
$$

Node: MMDZBZY2BV · Lean: `MinimalModel.ConeTheoremKlt`

This is KM98, Theorem 3.7, parts 1 and 2. For smooth $X$ and $\Delta = 0$ it is Mori's cone theorem, KM98, Theorem 1.24, with the bound $\dim X + 1$. The cone of curves can be round or have infinitely many edges on the side where $K_X + \Delta \ge 0$. On the negative side it is locally polyhedral, and its edges accumulate only at the hyperplane $(K_X + \Delta)^\perp$.

### Proof in words

Kleiman's criterion has an easy half. Let $D$ be ample and $H$ any Cartier divisor. Then $mD - H$ is ample for large $m$, so $D \cdot z \ge \frac{1}{m} H \cdot z$ on $\overline{NE}(X)$. If $D \cdot z = 0$, then $H \cdot z \le 0$ for every $H$, so $z = 0$ by the perfect pairing. For the other half, suppose $D > 0$ on $\overline{NE}(X) \setminus 0$. A compact slice of the cone shows that $D - \varepsilon H$ is nef for an ample $H$ and a small $\varepsilon > 0$. Kleiman's theorem that nef divisors have $D^{\dim V} \cdot V \ge 0$ then gives $D^{\dim V} \cdot V > 0$ for every subvariety $V$, and the Nakai-Moishezon criterion ends the proof (Laz04, Chapter 1).

Mori's proof of the cone theorem for smooth $X$ makes rational curves. If $K_X \cdot C < 0$ for a curve $C$, then the deformations of the map $C \to X$ fixing one point have dimension at least $-K_X \cdot C - n \cdot g(C)$. Reduction to characteristic $p$ and the Frobenius map make this number large. Then bend-and-break splits the curve, and a rational curve appears with $-K_X \cdot C \le n + 1$. All known proofs of the existence of these rational curves pass through characteristic $p$. Volume 6 gives the proof.

For klt pairs the proof is different and needs no rational curves. It is the chain of Kawamata, Reid, Shokurov and Kollár: the Kawamata-Viehweg vanishing theorem gives the non-vanishing theorem, then the base point free theorem, then the rationality theorem, and these give the cone theorem (KM98, Chapter 3). The base point free theorem also gives the contractions of Section 1.4. The rational curves and the length bound $2 \dim X$ come later, from Kawamata's work on the length of extremal rays.

### Examples

The projective plane. $N_1(\mathbb{P}^n) = \mathbb{R}$, spanned by a line $\ell$, and $\overline{NE}(\mathbb{P}^n) = \mathbb{R}_{\ge 0}[\ell]$. Here $-K \cdot \ell = n + 1$, so the bound of Mori's theorem is sharp.

The quadric surface, computed in full. Let $X = \mathbb{P}^1 \times \mathbb{P}^1$ with the fibre classes $f_1 = \{pt\} \times \mathbb{P}^1$ and $f_2 = \mathbb{P}^1 \times \{pt\}$. Then $f_1^2 = f_2^2 = 0$ and $f_1 \cdot f_2 = 1$. A curve $C$ has class $a f_2 + b f_1$ with $a = C \cdot f_1 \ge 0$ and $b = C \cdot f_2 \ge 0$, because the fibres move. So $\overline{NE}(X) = \mathbb{R}_{\ge 0} f_1 + \mathbb{R}_{\ge 0} f_2$. The canonical class is $K_X = -2 f_1 - 2 f_2$, so $K_X \cdot f_1 = K_X \cdot f_2 = -2$. Both rays are $K_X$-negative, and $\overline{NE}(X)_{K_X \ge 0} = 0$. By Kleiman's criterion a divisor $x f_1 + y f_2$ is ample if and only if $x, y > 0$. The two contractions are the two projections, and both are Mori fibre spaces.

Infinitely many rays. Let $X$ be $\mathbb{P}^2$ blown up at 9 general points. Then $-K_X$ is the class of the strict transform of the cubic through the 9 points, $K_X^2 = 0$, and $X$ contains infinitely many $(-1)$-curves (Nagata). Each has $K_X \cdot E = -1$ and spans an extremal ray. The rays accumulate at the ray of $-K_X$, which lies on $K_X^\perp$. This is what the finiteness part of the cone theorem allows: for $\varepsilon > 0$ only finitely many $E$ have $(K_X + \varepsilon H) \cdot E < 0$, because $H \cdot E$ grows.

A hypothesis that fails. Let $E$ be an elliptic curve without complex multiplication and $X = E \times E$. Then $\rho(X) = 3$, and $N^1(X)$ is spanned by the two fibres and the diagonal. The intersection form has signature $(1, 2)$. Every curve on an abelian surface is nef, because translations move it, so $\overline{NE}(X)$ is the round cone $\{ z : z^2 \ge 0, z \cdot H \ge 0 \}$. Take $D = -H$ for an ample $H$ in place of $K_X + \Delta$. Then $D$ is negative on all of $\overline{NE}(X) \setminus 0$, and the $D$-negative extremal rays form a circle: uncountably many, and not discrete. So the conclusion of the cone theorem fails for $D$. The hypothesis that fails is the form of $D$: $-H$ is not $K_X + \Delta$ for an effective $\Delta$, since $K_X = 0$ and $-H$ is not effective. For the true $K_X = 0$ the cone theorem says only $\overline{NE}(X) = \overline{NE}(X)_{K_X \ge 0}$.

Mumford's example shows that the closure in Kleiman's criterion is needed. On a ruled surface over a curve of genus at least 2, built from a suitable stable bundle of degree 0, the tautological divisor is positive on every curve and has self-intersection 0, so it is not ample (Laz04, Chapter 1).

### Exercises

1. (A) Compute $\overline{NE}(X)$ and the nef cone of $X = \mathbb{P}^1 \times \mathbb{P}^1 \times \mathbb{P}^1$. Find $K_X \cdot C$ for the generator of each ray.
2. (A) Let $X = \mathrm{Bl}_p \mathbb{P}^2$. Use Section 1.1 to find the nef cone of $X$, and check Kleiman's criterion for $aH - bE$.
3. (A) Let $R$ be an extremal ray of $\overline{NE}(X)$, and let $z = \sum a_i C_i$ with all $a_i > 0$ be an effective 1-cycle with $[z] \in R \setminus 0$. Show that $[C_i] \in R$ for every $i$.
4. (B) Let $X$ be a smooth projective surface with $-K_X$ ample. Use the cone theorem and the finiteness part to show that $\overline{NE}(X)$ is a polyhedral cone spanned by finitely many rational curves.
5. (B) On the blow-up of $\mathbb{P}^2$ at 9 general points, let $E$ run through the $(-1)$-curves. Show that $(K_X + \varepsilon H) \cdot E < 0$ gives $H \cdot E < 1/\varepsilon$, and conclude the finiteness part for this $X$ from the fact that only finitely many $(-1)$-curves have bounded degree.
6. (B) Let $X = E \times E$ with $E$ without complex multiplication. Write the intersection form on the basis $f_1, f_2, \delta$ (two fibres and the diagonal), and show that it has signature $(1, 2)$.

### Lean

`MinimalModel.ConeDecomposition` is the conclusion of the cone theorem for a model: countably many curves $C_i$ with $(K + \Delta) \cdot C_i < 0$, the decomposition of $\overline{NE}(X)$, the extremality of each ray, and the finiteness for $K + \Delta + \varepsilon H$. `MinimalModel.ConeTheoremKlt` says that every projective klt pair has it. The rationality of the $C_i$ and the bound $2 \dim X$ are left out; they are the separate node S09, which needs the words of rational curves. Kleiman's criterion is a node of the map with no Lean statement yet. Mathlib has `PointedCone` and `Submodule.span`, and the project builds $\overline{NE}(X)$ from them.

### Notes and history

Kleiman proved his criterion in 1966 (Kle66). Mori proved the cone theorem for smooth projective varieties in 1982 (Mor82), with bend-and-break. Kawamata, Reid, Shokurov and Kollár proved it for klt pairs in the 1980s with vanishing theorems, and KMM87 is the standard account of this proof. Both statements are theorems. The cone theorem for lc pairs is also a theorem, due to Ambro and Fujino (Fuj11; Volume 7). Theorem 1.2.30 proves the relative Kleiman criterion, Volume 6 gives bend-and-break, and Volume 7 gives the full proofs of the cone and contraction theorems.
