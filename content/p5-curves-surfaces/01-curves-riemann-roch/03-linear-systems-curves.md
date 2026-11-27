---
title: Linear systems on curves and the canonical embedding
nodes: []
sources: [Har77, Vak25, Ful69]
reads_with: [Har77:IV.3, Har77:IV.5, Vak25:ch19]
requires: [P3.10, P4.7, P5.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Linear systems on curves and the canonical embedding

### Statement

In this section $k$ is algebraically closed and $C$ is a smooth projective curve of genus $g$ over $k$. A *$g^r_d$* on $C$ is a linear system of dimension $r$ and degree $d$, that is, a projective subspace of dimension $r$ of some complete system $|D|$ with $\deg D = d$. A divisor $D$ is *special* if $\ell(K - D) > 0$. The morphism given by a base point free linear system is the one of Theorem P3.10.9.

**Proposition P5.1.19 (base points and very ampleness).** Let $D$ be a divisor on $C$.

1. The complete system $|D|$ is base point free if and only if $\ell(D - P) = \ell(D) - 1$ for every point $P$.
2. If $|D|$ is base point free, then $D$ is very ample, that is, the morphism of $|D|$ is a closed immersion, if and only if $\ell(D - P - Q) = \ell(D) - 2$ for all points $P, Q$, including $P = Q$.

Lean: not in Lean as stated.

**Corollary P5.1.20 (large degree).** Let $D$ be a divisor on $C$.

1. If $\deg D \geq 2g$, then $|D|$ is base point free.
2. If $\deg D \geq 2g + 1$, then $D$ is very ample, and embeds $C$ in $\mathbb{P}^{d - g}$ as a curve of degree $d = \deg D$.
3. $D$ is ample if and only if $\deg D > 0$.

Lean: not in Lean as stated.

**Definition P5.1.21 (hyperelliptic curve).** A curve $C$ of genus $g \geq 2$ is *hyperelliptic* if it has a morphism $C \to \mathbb{P}^1$ of degree $2$, that is, a $g^1_2$.

**Theorem P5.1.22 (Clifford).** Let $D$ be an effective special divisor on $C$. Then
$$2 (\ell(D) - 1) \leq \deg D.$$

Lean: not in Lean as stated.

**Theorem P5.1.23 (the canonical system).** Let $g \geq 2$.

1. The canonical system $|K|$ is base point free and defines the *canonical morphism* $\varphi_K \colon C \to \mathbb{P}^{g-1}$.
2. $K$ is very ample if and only if $C$ is not hyperelliptic. Then $\varphi_K$ embeds $C$ as a curve of degree $2g - 2$ in $\mathbb{P}^{g-1}$, the *canonical curve*.
3. If $C$ is hyperelliptic with $f \colon C \to \mathbb{P}^1$ of degree $2$ and $D = f^* (\mathrm{pt})$, then $K \sim (g - 1) D$, and $\varphi_K$ is $f$ followed by the Veronese embedding of $\mathbb{P}^1$ as a rational normal curve of degree $g - 1$ in $\mathbb{P}^{g-1}$.

Lean: not in Lean as stated.

**Corollary P5.1.24.** Every curve of genus $2$ is hyperelliptic, with the canonical morphism as its $g^1_2$. A curve of genus $3$ is either hyperelliptic or isomorphic to a smooth plane quartic.

Lean: not in Lean as stated.

### Proof in words

A point $P$ is a base point of $|D|$ exactly when every section of $\mathcal{O}_C(D)$ vanishes at $P$, which is the condition $\ell(D - P) = \ell(D)$. The morphism of $|D|$ separates $P$ and $Q$, or $P$ and a tangent direction at $P$, exactly when the sections vanishing at $P$ do not all vanish at $Q$, or to second order at $P$. Both conditions are computed by Riemann-Roch, and in degree $\geq 2g$ the correction term vanishes. For the canonical system, Riemann-Roch turns $\ell(K - P - Q)$ into $\ell(P + Q)$, and $\ell(P + Q) = 2$ is the existence of a map of degree $2$ to $\mathbb{P}^1$. Clifford's theorem bounds the dimension of a special system by adding divisors: $|D| \times |K - D| \to |K|$ has finite fibres, so the dimensions add up to at most $g - 1$.

### Examples

**Example P5.1.25 (elliptic normal curves).** Let $g = 1$ and $D$ of degree $n \geq 3$. By Corollary P5.1.20, $D$ embeds $C$ in $\mathbb{P}^{n-1}$ as a curve of degree $n$. For $n = 3$ this is a plane cubic, and for $n = 4$ a curve in $\mathbb{P}^3$ which lies on $h^0(\mathcal{O}_{\mathbb{P}^3}(2)) - \ell(2D) = 10 - 8 = 2$ independent quadrics, a complete intersection of two quadrics, by the degree count $2 \cdot 2 = 4$.

**Example P5.1.26 (genus $3$).** A smooth plane quartic $C$ has $K \sim H$ by Example P5.1.16, so the canonical morphism is the embedding $C \subseteq \mathbb{P}^2$, and $C$ is not hyperelliptic. The hyperelliptic curve $y^2 = f(x)$ with $\deg f = 8$ has $K \sim 2 (\infty_1 + \infty_2)$ by Example P5.1.18, and its canonical morphism $[1 : x : x^2]$ maps $C$ two to one onto a conic.

**Example P5.1.27 (genus $4$).** Let $C$ be a non-hyperelliptic curve of genus $4$, canonically embedded in $\mathbb{P}^3$ as a curve of degree $6$. By Corollary P5.1.11, $\ell(2K) = 4 \cdot 4 - 4 + 1 - 4 = 9$, while the quadrics of $\mathbb{P}^3$ form a space of dimension $10$. So $C$ lies on a quadric $Q$. In the same way $\ell(3K) = 15$ and the cubics form a space of dimension $20$, so $C$ lies on at least $5$ independent cubics, of which only $4$ are multiples of $Q$ by linear forms. So $C$ lies on a cubic $F$ not containing $Q$. The quadric $Q$ is irreducible, since $C$ is irreducible and not contained in a plane, and $Q \cap F$ is a curve of degree $6$ containing $C$. Exercise 5 asks for the proof that $C = Q \cap F$. Conversely, every smooth complete intersection of a quadric and a cubic in $\mathbb{P}^3$ is a canonical curve of genus $4$, by Example P4.7.24.

**Example P5.1.28 (equality in Clifford's theorem).** On a hyperelliptic curve with $g^1_2$ given by $D$, the divisor $mD$ for $0 \leq m \leq g - 1$ has $\ell(mD) \geq m + 1$, from the pullbacks of the sections of $\mathcal{O}_{\mathbb{P}^1}(m)$. It is special, since $K - mD \sim (g - 1 - m) D$ is effective. Clifford's theorem gives $\ell(mD) \leq m + 1$, so equality holds. The divisors $0$ and $K$ also give equality on any curve.

### Proof

*Proposition P5.1.19, part 1.* A point $P$ is a base point if and only if every section of $\mathcal{O}_C(D)$ vanishes at $P$, that is, $H^0(\mathcal{O}_C(D - P)) = H^0(\mathcal{O}_C(D))$. By part 4 of Corollary P5.1.11 the only other possibility is $\ell(D - P) = \ell(D) - 1$.

*Part 2.* Apply Theorem P3.10.12 with $V = H^0(\mathcal{O}_C(D))$. For $P \neq Q$, the sections vanishing at $P$ form $H^0(\mathcal{O}_C(D - P))$, and those vanishing at $P$ and $Q$ form $H^0(\mathcal{O}_C(D - P - Q))$. So $V$ separates $P$ and $Q$ if and only if $\ell(D - P - Q) < \ell(D - P) = \ell(D) - 1$, which by part 4 of Corollary P5.1.11 means $\ell(D - P - Q) = \ell(D) - 2$. For $P = Q$, the space $\mathfrak{m}_P \mathcal{L}_P / \mathfrak{m}_P^2 \mathcal{L}_P$ has dimension $1$, and the map $V_P \to \mathfrak{m}_P \mathcal{L}_P / \mathfrak{m}_P^2 \mathcal{L}_P$ has kernel $H^0(\mathcal{O}_C(D - 2P))$. It is surjective if and only if $\ell(D - 2P) < \ell(D - P)$, that is, $\ell(D - 2P) = \ell(D) - 2$.

*Corollary P5.1.20, part 1.* For every $P$, $\deg (D - P) \geq 2g - 1 > 2g - 2$, so by part 2 of Corollary P5.1.11, $\ell(D) = d + 1 - g$ and $\ell(D - P) = d - g$.

*Part 2.* For all $P, Q$, $\deg(D - P - Q) \geq 2g - 1$, so $\ell(D - P - Q) = d - 1 - g = \ell(D) - 2$. By part 1 and Proposition P5.1.19, $D$ is very ample, and $\ell(D) - 1 = d - g$. The image has degree $\deg \mathcal{O}_C(D) = d$ by Proposition P4.3.18.

*Part 3.* If $\deg D > 0$, then $\deg nD \geq 2g + 1$ for $n$ large, so $nD$ is very ample and $D$ is ample. Conversely, if $D$ is ample, some $nD$ is very ample, and the hyperplane section of the embedding is an effective nonzero divisor in $|nD|$, so $n \deg D > 0$.

*Theorem P5.1.22.* Let $a = \ell(D) - 1$ and $b = \ell(K - D) - 1$, both $\geq 0$ since $D$ is effective and special. Multiplication of sections gives a bilinear map $H^0(\mathcal{O}_C(D)) \times H^0(\mathcal{O}_C(K - D)) \to H^0(\omega_C)$, with $st \neq 0$ when $s, t \neq 0$, since $C$ is integral. On projective spaces it induces a morphism
$$\mu \colon |D| \times |K - D| \to |K|, \qquad (E, E') \mapsto E + E'.$$
It is the composite of the Segre embedding with a linear projection whose center does not meet the image, so it is a morphism of projective varieties. Its fibres are finite: an effective divisor $F \in |K|$ has finitely many effective divisors $E \leq F$, and $E$ determines $E' = F - E$. So the image of $\mu$ has dimension $a + b$, by the dimension of fibres (P3 Ch. 7), and $a + b \leq g - 1$. By Riemann-Roch, $a - b = \deg D + 1 - g$. Adding, $2a \leq \deg D$.

*Theorem P5.1.23, part 1.* Since $g \geq 1$, $\ell(P) = 1$ for every point $P$, by Proposition P5.1.12. By Riemann-Roch, $\ell(K - P) = \ell(P) + (2g - 3) + 1 - g = g - 1 = \ell(K) - 1$. By Proposition P5.1.19, $|K|$ is base point free.

*Part 2.* By Riemann-Roch, $\ell(K - P - Q) = \ell(P + Q) + (2g - 4) + 1 - g = \ell(P + Q) + g - 3$. So by Proposition P5.1.19, $K$ is very ample if and only if $\ell(P + Q) = 1$ for all $P, Q$. If $\ell(P + Q) \geq 2$ for some $P, Q$, the system $|P + Q|$ has dimension $\geq 1$. A nonconstant $h \in H^0(\mathcal{O}_C(P + Q))$ has $\deg \operatorname{div}_\infty(h) \leq 2$, and is a morphism to $\mathbb{P}^1$ of degree $1$ or $2$. Degree $1$ is excluded since $g \geq 2$, so $C$ is hyperelliptic. Conversely, if $f \colon C \to \mathbb{P}^1$ has degree $2$, a fibre $P + Q = f^*(\mathrm{pt})$ has $\ell(P + Q) \geq 2$. The degree of the canonical curve is $\deg K = 2g - 2$, by Proposition P4.3.18.

*Part 3.* The pullbacks $f^* s$ of the sections $s$ of $\mathcal{O}_{\mathbb{P}^1}(g - 1)$ are $g$ linearly independent sections of $\mathcal{O}_C((g - 1) D)$, since $f^*$ is injective on rational functions. So $\ell((g - 1) D) \geq g$. The divisor $(g - 1)D$ has degree $2g - 2$. If it is special, Clifford's theorem gives $\ell((g - 1)D) \leq g$. If it is not special, Riemann-Roch gives $\ell((g - 1)D) = g - 1$, a contradiction. So $\ell((g - 1) D) = g$, and $(g - 1)D \sim K$ by part 3 of Corollary P5.1.11. The sections $f^* s$ are then all the sections of $\omega_C$, and $\varphi_K$ is $f$ followed by the morphism of $|\mathcal{O}_{\mathbb{P}^1}(g - 1)|$, which is the Veronese embedding (Theorem P3.10.19).

*Corollary P5.1.24.* For $g = 2$, $|K|$ is base point free of degree $2$ and dimension $1$, so $\varphi_K$ is a morphism of degree $2$ to $\mathbb{P}^1$. For $g = 3$, if $C$ is not hyperelliptic, $\varphi_K$ embeds $C$ in $\mathbb{P}^2$ as a curve of degree $4$, which is smooth as the image of a smooth curve under a closed immersion.

### Exercises

1. (A) Show that the twisted cubic in $\mathbb{P}^3$ is the image of $\mathbb{P}^1$ by $|3P|$, and that every embedding of $\mathbb{P}^1$ as a nondegenerate curve of degree $d$ in $\mathbb{P}^d$ is a rational normal curve.
2. (A) Show that a hyperelliptic curve has exactly one $g^1_2$, using part 3 of Theorem P5.1.23: two different $g^1_2$ would give two different factorizations of $\varphi_K$.
3. (B) Show that every curve embeds in $\mathbb{P}^3$: given $C \subseteq \mathbb{P}^N$ with $N \geq 4$, show that the secant and tangent lines of $C$ form a variety of dimension at most $3$, and project from a point not on it.
4. (B) Let $C$ be non-hyperelliptic of genus $g \geq 3$, canonically embedded, and $E$ an effective divisor of degree $d \leq g - 1$. Show that the smallest linear space of $\mathbb{P}^{g-1}$ containing $E$, as a subscheme, has dimension $d - 1 - (\ell(E) - 1)$. This is the geometric form of Riemann-Roch.
5. (B) Complete Example P5.1.27: show that $Q \cap F$ is a curve of degree $6$ with no embedded points, and conclude $C = Q \cap F$. Deduce that a curve of genus $4$ has one or two $g^1_3$ according as $Q$ is a cone or smooth.
6. (C) Prove that equality holds in Clifford's theorem only for $D = 0$, $D \sim K$, or $C$ hyperelliptic and $D$ a multiple of the $g^1_2$. Use induction on $\deg D$ and a general point of the canonical curve.

### Lean

Mathlib does not have linear systems on curves or the canonical embedding. The handbook adds no `MinimalModel` node here.

### Notes and history

Clifford proved his theorem in 1878. The canonical embedding goes back to Noether, who proved in 1880 that a canonical curve is projectively normal, and Enriques and Petri described its ideal: it is generated by quadrics unless the curve is trigonal or a plane quintic. Green's conjecture of 1984, proved for general curves by Voisin in 2002 and 2005, extends this to the whole minimal free resolution. The literature state is theorem. In the minimal model program the curve case of the canonical system is the first instance of the trichotomy of Volume 1: $K$ negative on $\mathbb{P}^1$, trivial on elliptic curves, and ample on curves of genus $g \geq 2$, where $3K$ is very ample and gives the canonical model.
