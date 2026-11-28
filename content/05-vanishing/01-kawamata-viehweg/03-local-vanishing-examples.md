---
title: Local vanishing and two computations
nodes: []
sources: [KM98, Laz04, EV92, Har77]
reads_with: [Laz04:ch9, KM98:ch2]
requires: [P4.4, P7.10, 1.5, 4.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Local vanishing and two computations

### Statement

Theorem 5.1.12 has a local form, with the base equal to the variety itself. It needs no klt hypothesis and no positivity, because every divisor is ample relative to the identity. For a smooth variety and an effective divisor it is Theorem P7.10.9, the local vanishing behind multiplier ideals; the form below allows a normal variety and a divisor that is only $\mathbb{Q}$-Cartier. The section then works two examples by hand, one for each kind of statement in this chapter: a fractional line arrangement in the plane, where the round-up, the klt threshold and the predicted vanishing are explicit, and the blow-up of a smooth centre, where the theorem predicts exactly which twists by the exceptional divisor have no higher direct images.

**Theorem 5.1.19 (local vanishing on a normal variety).** Let $X$ be a normal quasi-projective variety, $D$ a $\mathbb{Q}$-Cartier $\mathbb{Q}$-divisor on $X$, and $\mu \colon Y \to X$ a projective birational morphism from a smooth variety such that $\operatorname{Exc}(\mu) \cup \mu^{-1}(\operatorname{Supp} D)$ is the support of an snc divisor. Then
$$R^j \mu_* \mathcal{O}_Y\big(K_Y - \lfloor \mu^* D \rfloor\big) = 0 \quad \text{for } j > 0.$$

Lean: not yet in Lean.

### Proof in words

Put $N = \lceil -\mu^* D \rceil = -\lfloor \mu^* D \rfloor$ and $\Theta = N + \mu^* D$, the fractional part that the round-up adds. Then $\Theta$ has snc support and coefficients in $[0, 1)$, and $N - \Theta = \mu^*(-D)$ is the pullback of a divisor that is ample over $X$, since every divisor is ample over $X$ for the identity. Theorem 5.1.12 with $Z = X$ is exactly the claim. In the examples, the round-up is computed component by component, and the predicted vanishing is compared with a direct computation by the projection formula and the exact sequence of the exceptional divisor.

### Examples

**Example 5.1.20 (the complete quadrangle).** Let $p_1, \dots, p_4 \in \mathbb{P}^2$ be four points, no three collinear, and $L_{ij}$, for $1 \leq i < j \leq 4$, the six lines through two of them. Each $p_i$ lies on the three lines $L_{ij}$, $j \neq i$, and two lines with no common index meet in one of the three diagonal points $L_{12} \cap L_{34}$, $L_{13} \cap L_{24}$, $L_{14} \cap L_{23}$; these account for all $\binom62 = 15$ intersections, as $4 \cdot 3 + 3 = 15$. Let $A = \sum L_{ij}$, of degree $6$, and for rational $c \geq 0$ consider the pair $(\mathbb{P}^2, c A)$. Let $\mu \colon Y \to \mathbb{P}^2$ be the blow-up of $p_1, \dots, p_4$ with exceptional curves $E_1, \dots, E_4$, $E = \sum_i E_i$, $H = \mu^* \ell$ for a line $\ell$, and $L'_{ij}$ the strict transforms. Then $\mu^* L_{ij} = L'_{ij} + E_i + E_j$, the three $L'_{ij}$ through $p_i$ meet $E_i$ in three distinct points, and the only other intersections are the three transverse diagonal points, so $\sum L'_{ij} + E$ is snc and $\mu$ is a log resolution. With $K_Y = \mu^* K_{\mathbb{P}^2} + E$ (Proposition 1.5.14),
$$\Delta_Y = c \sum L'_{ij} + (3c - 1) E,$$
so the pair is klt if and only if $c < 1$ and $3c - 1 < 1$, that is, $c < \frac23$ (Theorem 4.2.14). At a diagonal point the pair is snc with coefficients $c$, so the triple points alone decide the threshold.

Let $0 \leq c < \frac23$ and $N = d \ell$. Since $0 \leq c < 1$, $\lceil -c \rceil = 0$, and $\lceil 1 - 3c \rceil = 1 - \lfloor 3c \rfloor$, so Corollary 5.1.16 gives
$$N_Y = d H + (1 - \lfloor 3c \rfloor) E, \qquad \Theta = c \sum L'_{ij} + \{3c\} E,$$
with $\mu_* \mathcal{O}_Y(N_Y) = \mathcal{O}_{\mathbb{P}^2}(d)$, $R^j \mu_* \mathcal{O}_Y(N_Y) = 0$ for $j > 0$, and $N_Y - (K_Y + \Theta) = (d + 3 - 6c) H$. This is nef and big when $d > 6c - 3$, and then Corollary 5.1.14, part 1, for the klt pair $(Y, \Theta)$ gives $H^i(Y, \mathcal{O}_Y(N_Y)) = 0$ for $i > 0$. For $c < \frac16$ the prediction includes $d = -2$, that is, $H^i(Y, \mathcal{O}_Y(-2H + E)) = 0$, and for $c < \frac13$ it includes $d = -1$. These are checked directly. On the rational surface $Y$, Riemann-Roch reads $\chi(\mathcal{O}_Y(D)) = 1 + \frac12 D \cdot (D - K_Y)$, with $K_Y = -3H + E$, $H^2 = 1$, $H \cdot E_i = 0$ and $E_i^2 = -1$. For $D = -2H + E$, $D - K_Y = H$ and $\chi = 1 - 1 = 0$; $h^0(D) = 0$ because $D \cdot H = -2 < 0$ with $H$ nef, and $h^2(D) = h^0(K_Y - D) = h^0(-H) = 0$, so $h^1(D) = 0$. For $D = -H + E$, $D - K_Y = 2H$ and $\chi = 1 - 1 = 0$, with $h^0 = h^2 = 0$ in the same way. For $d = -3$, $N_Y = K_Y$ has $h^2 = 1$, and $d > 6c - 3$ excludes $d = -3$ for every $c \geq 0$. For $\frac13 \leq c < \frac23$, $N_Y = dH$ and the prediction $d > 6c - 3 \geq -1$ is weaker than the truth $H^i(Y, \mathcal{O}_Y(dH)) = H^i(\mathbb{P}^2, \mathcal{O}(d)) = 0$ for $d \geq -2$: the theorem pays for the boundary with positivity.

At $c = \frac23$ the coefficient of $E$ in $\Delta_Y$ is $1$, the pair is lc and not klt, and $\lceil \mu^* N - \Delta_Y \rceil = d H - E$. Its push-forward is $\mathcal{I}_\Sigma(d)$, where $\mathcal{I}_\Sigma$ is the ideal of the reduced set $\Sigma = \{p_1, \dots, p_4\}$, by the projection formula and $\mu_* \mathcal{O}_Y(-E_i) = \mathfrak{m}_{p_i}$ near $p_i$. So Lemma 5.1.11 fails at the threshold, and the defect is the ideal $\mathcal{I}_\Sigma$; Chapter 3 identifies it as the multiplier ideal of the pair (Example 5.3.6).

**Example 5.1.21 (the blow-up of a smooth centre).** Let $X$ be a smooth quasi-projective variety, $W \subseteq X$ a smooth closed subvariety of codimension $r \geq 2$ with ideal $\mathcal{I}$, $\mu \colon Y = \operatorname{Bl}_W X \to X$ the blow-up and $E$ the exceptional divisor. Then $E = \mathbb{P}(\mathcal{I}/\mathcal{I}^2)$ is a projective bundle $\pi \colon E \to W$ with fibres $\mathbb{P}^{r-1}$, and $\mathcal{O}_Y(-E)|_E = \mathcal{O}_E(1)$ (Har77, Theorem II.8.24), so $-E$ is $\mu$-ample, and $K_Y = \mu^* K_X + (r - 1) E$ by Proposition 1.5.14. For an integer $k$ and $N = k E$,
$$N - K_Y = (k - r + 1) E - \mu^* K_X,$$
which is $\mu$-nef if and only if $k \leq r - 1$, since $\mu^* K_X$ has degree $0$ on curves in the fibres and $E$ has degree $-1$ on a line in a fibre. Corollary 5.1.15 for the smooth, hence klt, pair $(Y, 0)$ gives
$$R^j \mu_* \mathcal{O}_Y(k E) = 0 \quad \text{for } j > 0 \text{ and } k \leq r - 1.$$
The direct check uses the sequences $0 \to \mathcal{O}_Y((k - 1) E) \to \mathcal{O}_Y(k E) \to \mathcal{O}_E(-k) \to 0$, where $\mathcal{O}_E(-k) = \mathcal{O}_Y(kE)|_E$. For $k \ll 0$, $R^j \mu_* \mathcal{O}_Y(kE) = 0$ for $j > 0$ by relative Serre vanishing for the $\mu$-ample $-E$ (Theorem P4.4.9). The sheaf $R^j \mu_* \mathcal{O}_E(-k)$ is the push-forward from $W$ of $R^j \pi_* \mathcal{O}_E(-k)$, which vanishes for $j > 0$ when $-k > -r$, by Theorem P4.4.14, part 2. So, by induction on $k$ from $k \ll 0$ up to $k = r - 1$, the long exact sequences give $R^j \mu_* \mathcal{O}_Y(kE) = 0$ for $j > 0$ and every $k \leq r - 1$. The theorem and the direct computation agree.

**Example 5.1.22 (the bound is sharp).** In Example 5.1.21 take $k = r$. Then $N - K_Y = E - \mu^* K_X$ is not $\mu$-nef, and the conclusion fails. In the sequence $0 \to \mathcal{O}_Y((r - 1)E) \to \mathcal{O}_Y(rE) \to \mathcal{O}_E(-r) \to 0$ the first sheaf has no higher direct images, so
$$R^{r-1} \mu_* \mathcal{O}_Y(r E) \cong R^{r-1} \pi_* \mathcal{O}_E(-r),$$
which is locally free of rank $\binom{r-1}{r-1} = 1$ on $W$ by Theorem P4.4.14, part 3, and so is nonzero. For a point of a surface, $r = 2$ and $R^1 \mu_* \mathcal{O}_Y(2E)$ is the skyscraper $k$ of Proposition P4.4.16 and Example P4.4.19. For a point of a threefold, $r = 3$ and the first failure is $R^2 \mu_* \mathcal{O}_Y(3E) \cong k$, while $R^1 \mu_* \mathcal{O}_Y(kE) = 0$ for every $k$, by the same sequences, since $R^1 \pi_* \mathcal{O}_{\mathbb{P}^2}(n) = 0$ for every $n$.

### Proof

*Theorem 5.1.19.* Put $N = \lceil -\mu^* D \rceil$, a Cartier divisor on the smooth variety $Y$, with $N = -\lfloor \mu^* D \rfloor$, and $\Theta = N + \mu^* D$. The support of $\mu^* D$ lies in $\mu^{-1}(\operatorname{Supp} D)$, so $\Theta$ has snc support, and its coefficients have the form $\lceil x \rceil - x \in [0, 1)$. The divisor $A = -D$ is $\mathbb{Q}$-Cartier and ample over $X$ for the identity, by Definition 1.2.25, since every line bundle on an affine scheme is ample. With $m \geq 1$ such that $mD$ is Cartier and $m \Theta$ is integral, $m(N - \Theta) = \mu^*(mA)$ as Cartier divisors, so $N - \Theta \sim_\mathbb{Q} \mu^* A$ in the sense of Theorem 5.1.12. That theorem, for $Z = X$, $f = \mathrm{id}_X$ and $h = \mu$, gives $R^j \mu_* \mathcal{O}_Y(K_Y + N) = 0$ for $j > 0$, and $K_Y + N = K_Y - \lfloor \mu^* D \rfloor$.

If $X$ is smooth and $D$ is effective, then $K_Y - \lfloor \mu^* D \rfloor = K_{Y/X} - \lfloor \mu^* D \rfloor + \mu^* K_X$, and the projection formula (Proposition P4.4.10) recovers the first vanishing of Theorem P7.10.9.

### Exercises

1. (A) In Example 5.1.20, compute $N_Y$ and $\Theta$ for $c = \frac12$ and $N = d \ell$, and list the $d$ for which Corollary 5.1.14 gives $H^i(Y, \mathcal{O}_Y(N_Y)) = 0$ for $i > 0$.
2. (A) In Example 5.1.21 with $X = \mathbb{P}^3$ and $W$ a line, so $r = 2$, show that $R^1 \mu_* \mathcal{O}_Y(2E)$ is a line bundle on $W$ and identify its degree using Theorem P4.4.14, part 3, and the conormal bundle $\mathcal{I}/\mathcal{I}^2 \cong \mathcal{O}_W(-1)^{\oplus 2}$.
3. (B) Let $D = \frac{1}{2} C$ on $\mathbb{A}^2$, with $C$ the cuspidal cubic $y^2 = x^3$, and $\mu$ the minimal log resolution, by three blow-ups. Compute $\lfloor \mu^* D \rfloor$ and $K_{Y/\mathbb{A}^2}$ and show that $\mu_* \mathcal{O}_Y(K_{Y/\mathbb{A}^2} - \lfloor \mu^* D \rfloor) = \mathcal{O}$, and state what Theorem 5.1.19 gives for this resolution.
4. (B) Let $X$ be the quadric cone $\{xy = z^2\} \subseteq \mathbb{A}^3$, $\mu \colon Y \to X$ the blow-up of the vertex with exceptional curve $E$, and $D = cL$ for a line $L$ through the vertex, as in Example 4.5.20. Show that $\mu$ satisfies the hypothesis of Theorem 5.1.19 and compute $\lfloor \mu^* D \rfloor$ for $0 \leq c < 2$.
5. (B) Let $\mu$ be the blow-up of the origin of $\mathbb{A}^2$ with exceptional curve $E$. Show that $R^1 \mu_* \mathcal{O}_Y(K_Y - \lfloor \mu^* D \rfloor + E) \neq 0$ for $D = 0$, so the round-down in Theorem 5.1.19 cannot be weakened by an exceptional divisor. For $D = a \ell$ with $\ell$ a line through the origin and $0 < a < 2$ rational, compute $K_Y - \lfloor \mu^* D \rfloor$ and check the theorem against Proposition P4.4.16.
6. (C) Let $W \subseteq X$ be a smooth centre of codimension $r$ and $\mu$ the blow-up. Use Example 5.1.21 and the Leray spectral sequence to show $H^i(Y, \mathcal{O}_Y(\mu^* M + kE)) \cong H^i(X, \mathcal{O}_X(M))$ for every Cartier divisor $M$ on a projective $X$, every $i$ and $0 \leq k \leq r - 1$, and show that this fails for $k = r$ when $r = 2$ and $W$ is a point of $\mathbb{P}^2$.

### Lean

The library has no blow-ups of smooth centres and no higher direct images of coherent sheaves. Theorem 5.1.19 is not yet in Lean. The examples are not formalized.

### Notes and history

Local vanishing for smooth $X$ is Lazarsfeld, Theorem 9.4.1 (Laz04), and it is the reason why multiplier ideals have the expected functoriality: the push-forward of $\mathcal{O}_Y(K_{Y/X} - \lfloor \mu^* D \rfloor)$ is the only non-zero direct image. Example 5.1.21 is the cohomological form of the statement that a blow-up of a smooth centre is a rational resolution of the smooth variety, extended to the twists by the exceptional divisor; for $k = 0$ it is $R^j \mu_* \mathcal{O}_Y = 0$, which Proposition P4.4.16 checks for a point of the plane, and Exercise 6 for $k = 0$ is the invariance of cohomology under blow-ups of smooth centres. The quadrangle of Example 5.1.20 returns as an example of a multiplier ideal and of Nadel vanishing in Chapter 3.
