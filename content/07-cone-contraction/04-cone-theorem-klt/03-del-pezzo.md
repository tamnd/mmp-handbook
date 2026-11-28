---
title: Cones of log del Pezzo surfaces
nodes: [MMDZBZY2BV, MMHTX4Z2B7]
sources: [KM98, Mat02, Kol96]
reads_with: [KM98:3.7, KM98:4.11, Kol96:III.3]
requires: [P7.3, P7.4, 4.2, 6.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Cones of log del Pezzo surfaces

### Statement

A *log del Pezzo surface* is a projective klt pair $(X, \Delta)$ of dimension $2$ with $-(K_X + \Delta)$ ample. For $\Delta = 0$ and $X$ smooth these are the del Pezzo surfaces, whose cones Volume 6 computed by Mori's method and Proposition P7.4.21. The klt cone theorem reaches the singular surfaces and the surfaces with a boundary, which Mori's method does not. A klt surface is $\mathbb{Q}$-factorial (KM98, Proposition 4.11), so intersection numbers of Weil divisors are defined and $N^1(X) = N_1(X)$; this is used without further comment. Write $K_\Delta$ for the class of $K_X + \Delta$, as in Section 1.

**Proposition 7.4.19 (cones of log del Pezzo surfaces).** Let $(X, \Delta)$ be a log del Pezzo surface.

1. $\overline{NE}(X) = \sum_{j=1}^{s} \mathbb{R}_{\ge 0} [\Gamma_j]$ for finitely many rational curves $\Gamma_j$ with $0 < -K_\Delta \cdot \Gamma_j \le 4$, and each $\mathbb{R}_{\ge 0} [\Gamma_j]$ is an extremal ray. In particular $NE(X) = \overline{NE}(X)$.
2. If $C \subseteq X$ is an integral curve with $C^2 < 0$, then $\mathbb{R}_{\ge 0} [C]$ is an extremal ray of $\overline{NE}(X)$, and $C$ is the only integral curve whose class lies in it.

Lean: not yet in Lean.

Part 2 holds for every projective $\mathbb{Q}$-factorial surface, with the same proof.

### Proof in words

Since $-K_\Delta$ is ample, the $K_\Delta$-nonnegative part of the cone is $0$, and Corollary 7.4.8 makes the cone polyhedral, spanned by finitely many negative extremal rays. Theorem 7.4.13 supplies rational curves of length at most $2 \cdot 2 = 4$ in each ray, and a finite sum of rays spanned by curves is already a cone of effective classes, so no closure is needed. A curve of negative self-intersection is extremal because every other curve meets it nonnegatively: if its class splits as a sum, intersecting with the curve itself forces both summands back onto its ray.

### Examples

**Example 7.4.20 (smooth del Pezzo surfaces again).** Let $\Delta = 0$ and $X$ smooth with $-K_X$ ample. For $X = \mathbb{P}^2$ the cone is the ray of a line, of length $3$. For $X = \mathbb{P}^1 \times \mathbb{P}^1$ it is spanned by the two rulings, each of length $2$. For $X = \mathbb{F}_1$ it is $\langle C_-, F \rangle$ by Proposition P7.4.19, with $-K_X \cdot C_- = 1$ and $-K_X \cdot F = 2$. For the blow-up $S_r$ of $\mathbb{P}^2$ at $2 \le r \le 8$ points in general position, Proposition P7.4.21 gives the rays of the $(-1)$-curves $C$, with $-K_X \cdot C = 1$ by adjunction. In every case the minimal length is at most $3 = d + 1$, Mori's bound of Corollary 6.2.10, and the bound $4$ of Proposition 7.4.19 is not attained. Every $(-1)$-curve and the curve $C_-$ of $\mathbb{F}_1$ illustrate part 2.

**Example 7.4.21 (the weighted projective plane $\mathbb{P}(1, 1, n)$).** Let $n \ge 2$ and let $\pi \colon \mathbb{F}_n \to X$ be the morphism of Proposition P7.4.19 defined by $\mathcal{O}(C_+)$, which contracts $C_-$ and no other curve. Its image is the cone over the rational normal curve of degree $n$, which is $\mathbb{P}(1, 1, n)$ (Example 5.1.18), with one singular point $\pi(C_-)$. Write $K_{\mathbb{F}_n} = \pi^* K_X + b C_-$. Adjunction on $C_- \cong \mathbb{P}^1$ gives $K_{\mathbb{F}_n} \cdot C_- = -2 - C_-^2 = n - 2$, and $\pi^* K_X \cdot C_- = 0$, so $b C_-^2 = n - 2$ and
$$K_{\mathbb{F}_n} = \pi^* K_X - \frac{n - 2}{n} C_-.$$
The discrepancy $-\frac{n-2}{n} > -1$, so $X$ is klt, as Theorem 4.2.30 also gives, since $X$ is the quotient of $\mathbb{A}^2$ by $\mu_n$ near the vertex. The Picard number is $\rho(X) = \rho(\mathbb{F}_n) - 1 = 1$, and the cone is the ray of $\ell = \pi(F)$. Since $\pi^* \ell = F + \frac1n C_-$,
$$-K_X \cdot \ell = -\Bigl( K_{\mathbb{F}_n} + \frac{n-2}{n} C_- \Bigr) \cdot F = 2 - \frac{n - 2}{n} = \frac{n + 2}{n},$$
and $\ell^2 = (F + \frac1n C_-)^2 = \frac2n - \frac1n = \frac1n$. So $-K_X \equiv (n + 2) \ell$ is ample and $(X, 0)$ is a log del Pezzo surface with a ray of length $\frac{n+2}{n}$: $2$ for the quadric cone $n = 2$, and tending to $1$ as $n$ grows. The line $\ell$ is a rational curve, as Theorem 7.4.13 asserts.

**Example 7.4.22 (a log del Pezzo structure on $\mathbb{F}_n$).** Let $n \ge 3$, so that $K_{\mathbb{F}_n} \cdot C_- = n - 2 > 0$ and $\mathbb{F}_n$ is not a del Pezzo surface. Let $c$ be rational with $\frac{n - 2}{n} < c < 1$ and $\Delta = c \, C_-$, klt by Corollary 4.2.13. With $K_{\mathbb{F}_n} \equiv -2 C_- - (n + 2) F$,
$$K_\Delta \cdot C_- = (n - 2) - c n < 0, \qquad K_\Delta \cdot F = -2 + c < 0.$$
By Proposition P7.4.19, $\overline{NE}(\mathbb{F}_n) = \langle C_-, F \rangle$, so $-K_\Delta$ is positive on the cone and ample by Theorem P7.3.13: $(\mathbb{F}_n, c \, C_-)$ is a log del Pezzo surface. Both rays are negative, of lengths $2 - c$ and $2 - (1 - c) n$. They are cut out by the nef divisors $F$ and $C_+ = C_- + n F$, and the morphisms they define are the ruling $q \colon \mathbb{F}_n \to \mathbb{P}^1$ and the contraction $\pi \colon \mathbb{F}_n \to \mathbb{P}(1, 1, n)$ of Example 7.4.21. For $n = 3$ and $c = \frac12$, with $a = 2$, take the ample $H = C_- + 4 F$, so $H \cdot C_- = H \cdot F = 1$. Then $(H + t K_\Delta) \cdot C_- = 1 - \frac t2$ and $(H + t K_\Delta) \cdot F = 1 - \frac{3t}{2}$, so $r(H) = \frac23$, with denominator $3 \le a(d + 1) = 6$, and $H + \frac23 K_\Delta \equiv \frac23 F$ cuts out the ray of $F$, as in Lemma 7.4.3.

### Proof

*Proposition 7.4.19, part 1.* Since $-K_\Delta$ is ample, $K_\Delta \cdot z < 0$ for every $z \in \overline{NE}(X) \setminus \{0\}$ by Theorem P7.3.13, so $\overline{NE}(X)_{K_\Delta \ge 0} = 0$. By Corollary 7.4.8, $\overline{NE}(X)$ is the sum of finitely many $K_\Delta$-negative extremal rays $R_1, \ldots, R_s$, and by Theorem 7.4.13 each $R_j$ is $\mathbb{R}_{\ge 0} [\Gamma_j]$ for a rational curve $\Gamma_j$ with $0 < -K_\Delta \cdot \Gamma_j \le 2 \cdot 2 = 4$. The classes $[\Gamma_j]$ lie in $NE(X)$, which is a convex cone, so $\overline{NE}(X) = \sum_j \mathbb{R}_{\ge 0} [\Gamma_j] \subseteq NE(X) \subseteq \overline{NE}(X)$.

*Part 2.* If $\rho(X) = 1$, the cone is a single ray and there is nothing to prove for extremality; uniqueness is proved below. Let $V$ be the closure of the convex cone spanned by the classes of the integral curves $D \ne C$. For such $D$, $C \cdot D \ge 0$ since $C \not\subseteq D$, so $C \cdot v \ge 0$ for all $v \in V$ by continuity. By Lemma 6.2.5, $\mathbb{R}_{\ge 0} [C] + V$ is closed; it contains every curve class, so it equals $\overline{NE}(X)$. Suppose $[C] = u + w$ with $u, w \in \overline{NE}(X)$, and write $u = \alpha [C] + u'$, $w = \beta [C] + w'$ with $\alpha, \beta \ge 0$ and $u', w' \in V$. Then $(1 - \alpha - \beta) [C] = u' + w'$, and intersecting with $C$ gives $(1 - \alpha - \beta) C^2 = C \cdot (u' + w') \ge 0$, so $1 - \alpha - \beta \le 0$. If $1 - \alpha - \beta < 0$, then $u' + w'$ and $-(u' + w')$ both lie in $\overline{NE}(X)$, and $\overline{NE}(X)$ is salient by Proposition P7.3.14, so $u' + w' = 0$ and then $1 - \alpha - \beta = 0$, a contradiction. So $u' + w' = 0$, hence $u' = w' = 0$ by salience again, and $u, w \in \mathbb{R}_{\ge 0} [C]$. Finally, if $D \ne C$ is an integral curve with $[D] = \lambda [C]$, then $\lambda > 0$ because $H \cdot D > 0$ for an ample $H$, and $0 \le C \cdot D = \lambda C^2 < 0$, which is absurd.

### Exercises

1. (A) Let $X = \mathbb{P}^2$ and $\Delta = c Q$ for a smooth conic $Q$ and rational $0 \le c < 1$. Show that $(X, \Delta)$ is log del Pezzo exactly when $c < \frac32$, so always, and compute the length of the ray.
2. (A) In Example 7.4.21 with $n = 3$, show that $3 \ell$ is Cartier and $\ell$ is not, and that $a = 3$ is the index of $K_X$.
3. (B) For $\mathbb{F}_n$ with $n \ge 3$ and $\Delta = c \, C_- + e F_0$ for a fibre $F_0$, find the set of rational $(c, e) \in [0, 1)^2$ for which $(\mathbb{F}_n, \Delta)$ is log del Pezzo, and the lengths of the two rays.
4. (B) Let $(X, \Delta)$ be log del Pezzo with $\rho(X) \ge 2$. Show that every extremal ray is spanned by an integral curve $C$ with $C^2 \le 0$, using that a class $z$ with $z^2 > 0$ and $H \cdot z > 0$ lies in the interior of $\overline{NE}(X)$ by Riemann-Roch.
5. (B) Let $X$ be the cubic surface, $S_6$. Use part 2 of Proposition 7.4.19 and Proposition P7.4.21 to show that the cone has exactly $27$ extremal rays, and that a general $(-K_X)$-section $E$, an elliptic curve, gives a log del Pezzo pair $(X, \frac12 E)$ with all lengths $\frac12$.
6. (C) Let $(X, \Delta)$ be a log del Pezzo surface with $\rho(X) = 1$ and let $\ell$ span the cone. Show that $-K_\Delta \cdot \ell \le 4$ cannot be improved to $-K_\Delta \cdot \ell \le 2$, using Example 7.4.21 with $n = 2$ and the pair $(\mathbb{P}^2, 0)$, and explain why $3$ is the best possible bound among these examples.

### Lean

Log del Pezzo surfaces and the cones of this section are not yet in Lean. The inputs `MinimalModel.ConeTheoremKlt` and `MinimalModel.LengthOfExtremalRays` exist as statements without proof.

### Notes and history

For klt surfaces the lengths of extremal rays are bounded by $3$, with equality only for $\mathbb{P}^2$ with $\Delta = 0$, by the classification of extremal contractions of surfaces (KM98, Chapter 3, and Kol96, Chapter III). The general bound $2d = 4$ of Kawamata is enough for everything in this volume. Log del Pezzo surfaces with quotient singularities are the two-dimensional log Fano varieties, and Example 7.4.21 is the first of them that is not smooth.
