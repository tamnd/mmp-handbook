---
title: Mori's proof and the klt proof compared
nodes: [MMDZBZY2BV, MMHTX4Z2B7]
sources: [KM98, Mor82, Kaw91, Kol96, Deb01]
reads_with: [KM98:1.24, KM98:3.7, Kol96:III.1, Deb01:ch7]
requires: [5.1, 5.6, 6.1, 6.2, 6.3, 7.4, 7.5]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Mori's proof and the klt proof compared

### Statement

Volume 6 proved the cone theorem for a smooth projective variety by Mori's bend-and-break, and this volume proved it for klt pairs through vanishing. The two proofs reach overlapping conclusions by opposite routes. This section records where they agree, what each gives that the other does not, and three examples that separate them. For a $K_\Delta$-negative extremal ray $R$ of a projective klt pair, or of a smooth projective variety with $\Delta = 0$, put
$$\ell(R) = \min \{ -K_\Delta \cdot \Gamma : \Gamma \text{ a rational curve with } [\Gamma] \in R \},$$
the *length* of $R$, as in Lemma 6.1.6.

**Proposition 7.6.15 (the two theorems agree on smooth varieties).** Let $X$ be a smooth projective variety over an algebraically closed field of characteristic $0$ and $\Delta = 0$. Then Theorem 6.2.9 and Theorem 7.4.6 describe the same set of $K_X$-negative extremal rays. Every such ray $R$ is spanned by a rational curve $\Gamma$ with $-K_X \cdot \Gamma \le d + 1$, it is cut out by a nef Cartier divisor $L$ with $L - K_X$ ample, and it has a contraction $\varphi_R$ as in Theorem 7.5.2.

Lean: not yet in Lean.

**Proposition 7.6.16 (lengths).** Let $(X, \Delta)$ be a projective klt pair of dimension $d$ over a field of characteristic $0$, with $a (K_X + \Delta)$ Cartier, and $R$ a $K_\Delta$-negative extremal ray.

1. The minimum $\ell(R)$ exists, $\ell(R) \in \frac1a \mathbb{Z}$, and $0 < \ell(R) \le 2d$.
2. If $X$ is smooth and $\Delta = 0$, then $\ell(R)$ is an integer and $\ell(R) \le d + 1$, with equality for $X = \mathbb{P}^d$.
3. The bound $2d$ is attained for $d = 1$, by $(\mathbb{P}^1, 0)$, and $\ell(R)$ need not be an integer when $X$ is singular or $\Delta \ne 0$.

Lean: not yet in Lean.

### Proof in words

*The two routes.* Mori's proof starts from curves. Bend-and-break, with the Frobenius in positive characteristic, produces through every point of a $K_X$-negative curve a rational curve of bounded anticanonical degree (Theorem 6.1.2). The cone is then shown to be spanned by the $K_X$-nonnegative part and these rational curves, and the rays are found among their classes; discreteness follows because only finitely many classes of bounded degree are steep (Lemma 6.2.4). The klt proof starts from divisors. The rationality theorem, a consequence of Kawamata-Viehweg vanishing, finds the nef thresholds $A + r K_\Delta$ with bounded denominators. The rays are faces cut out by these nef divisors, discreteness comes from the lattice $\frac1N \mathbb{Z}$ of Lemma 7.4.5, and curves enter only at the end, through the base point free theorem (Corollary 7.4.12) and Kawamata's theorem (Theorem 7.4.13), which itself uses bend-and-break on resolutions of fibres.

*What each gives.* Mori's proof needs $X$ smooth, or at least the deformation theory of morphisms from curves to $X$, and $\Delta = 0$; it works in every characteristic and gives the sharp bound $d + 1$. The klt proof needs characteristic $0$, because vanishing fails in positive characteristic (Counterexample 5.6.8), but it allows klt singularities and boundaries. These are exactly what the minimal model program produces: a divisorial contraction of a smooth variety may have a singular target (Example 7.5.15), and the program must then continue on it. Its bound is $2d$. Most importantly, it gives the supporting divisor $L$ with $L - K_\Delta$ ample (Corollary 7.4.7), to which the base point free theorem applies, and so the contraction of every negative face in every dimension (Theorem 7.5.2). Mori's proof gives a nef supporting divisor (Corollary 6.2.11), but no base point free theorem for it in positive characteristic or in dimension at least $4$. Contractions in Volume 6 came from Mori's classification for smooth threefolds (Theorem 6.3.9).

*The proofs of the propositions.* Proposition 7.6.15 is formal: both theorems describe the extremal rays of the same cone on which $K_X$ is negative, Mori's bound is Corollary 6.2.10, and the supporting divisor and the contraction come from this volume. Proposition 7.6.16 combines the discreteness of $\frac1a \mathbb{Z}$ with the two bounds.

### Examples

**Example 7.6.17 (a singular surface that only the klt theorem sees).** Let $X = \mathbb{P}(1, 1, n)$, $n \ge 3$, and $\pi \colon \mathbb{F}_n \to X$ the contraction of $C_-$ (Example 7.4.21). Mori's theorem applies to $\mathbb{F}_n$, where it sees only the ray of $F$, of length $2$, since $K_{\mathbb{F}_n} \cdot C_- = n - 2 > 0$. It does not apply to $X$, which is singular. Theorem 7.4.6 applies to $X$, which is klt, and gives the single ray of $\ell = \pi(F)$ of length $\frac{n + 2}{n}$, the image of the ray of $F$. The length of the ray drops from $2$ to $\frac{n+2}{n}$, by the correction term $\frac{n-2}{n} C_- \cdot F$ in $K_{\mathbb{F}_n} = \pi^* K_X - \frac{n-2}{n} C_-$.

**Example 7.6.18 (a ray that only a boundary makes negative).** On $\mathbb{F}_n$, $n \ge 3$, with $\Delta = c \, C_-$ and $\frac{n-2}{n} < c < 1$ (Example 7.4.22), both rays are $K_\Delta$-negative, while for $\Delta = 0$ the ray of $C_-$ is $K$-positive. Mori's theorem for $K_{\mathbb{F}_n}$ does not see the contraction to $\mathbb{P}(1, 1, n)$; the klt cone theorem for $K_{\mathbb{F}_n} + c \, C_-$ does, and Theorem 7.5.2 produces it. Running the minimal model program for the pair, rather than for $\mathbb{F}_n$, is what makes the singular surface $\mathbb{P}(1, 1, n)$ appear.

**Example 7.6.19 (positive characteristic).** Let $k$ have characteristic $p > 0$ and $X$ a smooth projective variety over $k$. Theorem 6.2.9 holds for $X$ with Mori's bound $d + 1$. The proof of Theorem 7.4.6 breaks at its first step: the rationality theorem of Chapter 3 rests on Kawamata-Viehweg vanishing, which fails for nef and big divisors even on smooth rational surfaces (Counterexample 5.6.8). For $X = \mathbb{F}_n$ the conclusions still hold, since the cone and its contractions can be computed directly (Proposition P7.4.19), but the general klt statements are not available in this volume in positive characteristic.

### Proof

*Proposition 7.6.15.* A $K_X$-negative extremal ray is a property of the cone $\overline{NE}(X)$ and of the class $K_X$, so the two theorems describe the same set of rays; Theorem 6.2.9 lists them as spanned by rational curves, and Theorem 7.4.6, part 2, as exposed rational rays. Since $X$ is smooth, $(X, 0)$ is klt by Definition 4.2.1. Corollary 6.2.10 gives a rational curve $\Gamma$ with $[\Gamma] \in R$ and $-K_X \cdot \Gamma \le d + 1$. Corollary 7.4.7 gives $L$, and Theorem 7.5.2 the contraction.

*Proposition 7.6.16, part 1.* By Theorem 7.4.13 the set of rational curves $\Gamma$ with $[\Gamma] \in R$ is nonempty and contains one with $-K_\Delta \cdot \Gamma \le 2d$. For every such $\Gamma$, $a \, (-K_\Delta \cdot \Gamma)$ is a positive integer, since $a (K_X + \Delta)$ is Cartier and $[\Gamma] \in R$. So the values in $(0, 2d]$ form a finite set, and the minimum exists, lies in $\frac1a \mathbb{Z}$ and is at most $2d$.

*Part 2.* Here $a = 1$, so $\ell(R)$ is an integer, and Corollary 6.2.10 gives $\ell(R) \le d + 1$. For $X = \mathbb{P}^d$ the cone is the ray of a line, every curve $\Gamma$ of degree $e \ge 1$ has $-K_X \cdot \Gamma = (d + 1) e \ge d + 1$, and a line attains $d + 1$.

*Part 3.* For $d = 1$, $\mathbb{P}^1$ has a single ray, spanned by $\mathbb{P}^1$ itself, of length $2 = 2d$. Example 7.6.17 gives $\ell = \frac{n+2}{n}$, and Example 7.4.16 gives $d + 1 - c$ for $(\mathbb{P}^d, c H_0)$, neither an integer for suitable $n$ and $c$. In Example 7.6.17 the minimum is attained by $\ell$: since $-K_X \equiv (n + 2) \ell$ and $n \ell$ is Cartier, every curve $\Gamma$ has $n \ell \cdot \Gamma \in \mathbb{Z}_{> 0}$, so $-K_X \cdot \Gamma = \frac{n+2}{n} \, (n \ell \cdot \Gamma) \ge \frac{n+2}{n}$.

### Exercises

1. (A) For $X = \mathbb{P}^1 \times \mathbb{P}^2$, compute the lengths of both rays and compare them with $d + 1 = 4$ and $2d = 6$.
2. (A) Show that for a smooth projective curve $X$ of genus $g$, $\overline{NE}(X)$ has a $K_X$-negative ray exactly when $g = 0$, and that its length is $2$.
3. (B) For $X = \mathbb{P}(1, 1, n)$, show that every integral curve through the vertex has class a positive integer multiple of $\ell$, and compute $\ell(R)$ for $(X, c \, \ell_0)$ with $\ell_0$ a line through the vertex and $0 < c < 1$.
4. (B) Let $X$ be the blow-up of $\mathbb{P}^3$ along a line, as in Proposition 7.5.17. Compute both lengths, and check that the two bounds $d + 1 = 4$ and $2e$ of Theorem 7.4.13 hold for each ray with the appropriate $e$.
5. (B) Show that the length of a fibre type ray of a smooth threefold onto a surface is $1$ or $2$, and onto a curve is at most $3$, using Theorem 6.3.9 and the examples of Section 5.3 as models.
6. (C) Let $(X, \Delta)$ be klt and $R$ a negative ray whose contraction is birational with exceptional locus $E$ and $e = \dim E - \dim \varphi(E)$. Show that $\ell(R) \le 2e$, and compute $\ell(R)$ and $e$ for the divisorial rays of Examples 7.5.15 and 7.5.19, comparing $\ell(R)$ with $e + 1$.

### Lean

`MinimalModel.ConeTheoremKlt`, `MinimalModel.LengthOfExtremalRays` and `MinimalModel.ContractionTheorem` state the theorems of this volume all as statements without proof. The comparison itself is not a Lean statement.

### Notes and history

Mori proved the cone theorem for smooth varieties in Mor82 by bend-and-break, with the reduction to positive characteristic. The vanishing route is due to Kawamata, Reid, Shokurov and Kollár, and gives the cone theorem for klt pairs and the contraction theorem together (KM98, Chapter 3). Kawamata's bound $2d$ (Kaw91) uses Mori's method on the fibres. Whether $d + 1$ bounds the lengths of all klt pairs is open in general. Kol96, Chapter III, and Deb01, Chapter 7, discuss both proofs.
