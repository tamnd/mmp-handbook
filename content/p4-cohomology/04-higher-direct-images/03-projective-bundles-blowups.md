---
title: Projective bundles, the Leray spectral sequence and a blow-up
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:III.8, Vak25:ch18]
requires: [P2.4, P3.6, P3.11, P4.1, P4.2, P4.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Projective bundles, the Leray spectral sequence and a blow-up

### Statement

For a morphism $f \colon X \to Y$ and a sheaf $\mathcal{F}$ on $X$ the Leray spectral sequence of Corollary P2.4.26 is
$$E_2^{p,q} = H^p(Y, R^q f_* \mathcal{F}) \Rightarrow H^{p+q}(X, \mathcal{F}).$$
This section computes the higher direct images in two cases where the spectral sequence then gives the cohomology of $X$: projective bundles, where the higher direct images of the structure sheaf vanish, and the blow-up of a point of the plane, where they are skyscraper sheaves of known length.

Let $\mathcal{E}$ be a locally free sheaf of rank $r \geq 1$ on a scheme $Y$, and $\pi \colon P = \mathbb{P}(\mathcal{E}) \to Y$ the projective bundle of Definition P3.6.33, with $\mathcal{O}_P(1)$. Over an open $U$ on which $\mathcal{E}$ is free, $\pi^{-1}(U) \cong \mathbb{P}^{r-1}_U$ with $\mathcal{O}_P(1)$ corresponding to $\mathcal{O}(1)$ (part 3 of Proposition P3.6.35). So $\pi$ is quasi-compact and separated, and projective if $Y$ is quasi-compact. Write $\operatorname{Sym}^n \mathcal{E} = 0$ for $n < 0$.

**Theorem P4.4.14 (higher direct images on a projective bundle).** In this setting, for every $n \in \mathbb{Z}$:

1. $\pi_* \mathcal{O}_P(n) \cong \operatorname{Sym}^n \mathcal{E}$;
2. $R^q \pi_* \mathcal{O}_P(n) = 0$ for $q \neq 0, r - 1$, and $R^{r-1} \pi_* \mathcal{O}_P(n) = 0$ for $n > -r$ if $r \geq 2$;
3. for $r \geq 2$ and $n \leq -r$, $R^{r-1} \pi_* \mathcal{O}_P(n)$ is locally free of rank $\binom{-n-1}{r-1}$;
4. for every locally free $\mathcal{G}$ of finite rank on $Y$, every $n > -r$ and every $p$,
$$H^p(P, \mathcal{O}_P(n) \otimes \pi^* \mathcal{G}) \cong H^p(Y, \operatorname{Sym}^n \mathcal{E} \otimes \mathcal{G}).$$

Lean: not in Lean as stated.

**Corollary P4.4.15 (the structure sheaf of a projective bundle).** $\pi_* \mathcal{O}_P = \mathcal{O}_Y$, $R^q \pi_* \mathcal{O}_P = 0$ for $q > 0$, and $H^p(P, \mathcal{O}_P) \cong H^p(Y, \mathcal{O}_Y)$ for every $p$. If $Y$ is projective over a field, then $\chi(P, \mathcal{O}_P) = \chi(Y, \mathcal{O}_Y)$.

Lean: not in Lean as stated.

Let $k$ be a field, $Y = \mathbb{A}^2_k = \operatorname{Spec} k[x, y]$, $\mathfrak{m} = (x, y)$, and $\pi \colon \tilde X = \operatorname{Bl}_0 \mathbb{A}^2_k \to Y$ the blow-up of the origin, with exceptional divisor $E \cong \mathbb{P}^1_k$ (Theorem P3.11.4). The scheme $\tilde X$ is covered by the two charts
$$U_1 = \operatorname{Spec} k[x, v], \quad y = x v, \qquad U_2 = \operatorname{Spec} k[y, u], \quad x = y u,$$
with $U_1 \cap U_2 = \operatorname{Spec} k[x, v, v^{-1}]$, $u = v^{-1}$, and $E$ is the Cartier divisor given by $x$ on $U_1$ and by $y$ on $U_2$.

**Proposition P4.4.16 (the blow-up of a point of the plane).** For every $m \in \mathbb{Z}$, $R^q \pi_* \mathcal{O}_{\tilde X}(mE) = 0$ for $q \geq 2$, and:

1. for $m \geq 0$, $\pi_* \mathcal{O}_{\tilde X}(-mE) = \widetilde{\mathfrak{m}^m}$ and $R^1 \pi_* \mathcal{O}_{\tilde X}(-mE) = 0$;
2. for $m \geq 1$, $\pi_* \mathcal{O}_{\tilde X}(mE) = \mathcal{O}_Y$, and $R^1 \pi_* \mathcal{O}_{\tilde X}(mE)$ is a skyscraper sheaf at the origin of length $m(m-1)/2$.

In particular $\pi_* \mathcal{O}_{\tilde X} = \mathcal{O}_Y$ and $R^q \pi_* \mathcal{O}_{\tilde X} = 0$ for $q > 0$.

Lean: not in Lean as stated.

### Proof in words

On a projective bundle everything is local on $Y$, and over a trivializing open the bundle is a projective space over the base, whose higher direct images Example P4.4.4 computes: the sections of $\mathcal{O}(n)$ are the forms of degree $n$ and the only other cohomology is in the top degree $r - 1$, for $n \leq -r$. The projection formula moves a locally free sheaf from $Y$ through $\pi_*$, and when all higher direct images vanish the Leray spectral sequence collapses to an isomorphism. For the blow-up, $Y$ is affine, so the higher direct images are the cohomology of $\tilde X$, and the two charts give a Čech complex of monomials $x^a v^b$. The first chart contributes the monomials with $b \geq 0$, the second those with $b \leq a$, and the cohomology is what the two miss together, a triangle of monomials whose size is $m(m-1)/2$.

### Examples

**Example P4.4.17 (Künneth on a product of lines).** Let $X = \mathbb{P}^1_k \times_k \mathbb{P}^1_k$ with second projection $\pi$ to $Y = \mathbb{P}^1_k$, so that $\pi$ is $\mathbb{P}^1_Y \to Y$ and $\mathcal{O}(a, b) = \mathcal{O}_{\mathbb{P}^1_Y}(a) \otimes \pi^* \mathcal{O}_Y(b)$. By Example P4.4.4 and Proposition P4.4.10, $R^q \pi_* \mathcal{O}(a, b) \cong H^q(\mathbb{P}^1_k, \mathcal{O}(a)) \otimes_k \mathcal{O}_Y(b)$. The Leray spectral sequence has $E_2^{p,q} = H^q(\mathcal{O}(a)) \otimes H^p(\mathcal{O}(b))$, nonzero only for $p, q \in \{0, 1\}$. Every differential $d_r$, $r \geq 2$, changes $p$ by $r \geq 2$, so it is zero and $E_2 = E_\infty$. Since all terms are vector spaces,
$$h^1(\mathcal{O}(a, b)) = h^1(\mathcal{O}(a)) h^0(\mathcal{O}(b)) + h^0(\mathcal{O}(a)) h^1(\mathcal{O}(b)),$$
in agreement with Exercise 6 of Section 2.1. For $(a, b) = (-2, 0)$ this is $1$.

**Example P4.4.18 (Hirzebruch surfaces).** Let $F_n = \mathbb{P}(\mathcal{O} \oplus \mathcal{O}(n))$ over $\mathbb{P}^1_k$, $n \geq 0$ (Example P3.6.37), with $r = 2$. Corollary P4.4.15 gives $h^0(\mathcal{O}_{F_n}) = 1$ and $h^1 = h^2 = 0$, so $\chi(\mathcal{O}_{F_n}) = 1$ for all $n$. Part 4 of Theorem P4.4.14 gives, for $d \geq 0$,
$$H^0(F_n, \mathcal{O}(d)) \cong \bigoplus_{i = 0}^{d} H^0(\mathbb{P}^1_k, \mathcal{O}(i n)), \qquad h^0 = \sum_{i=0}^{d} (in + 1) = (d + 1)\Bigl(\frac{dn}{2} + 1\Bigr),$$
using $\operatorname{Sym}^d(\mathcal{O} \oplus \mathcal{O}(n)) = \bigoplus_{i=0}^d \mathcal{O}(in)$, and $H^1(F_n, \mathcal{O}(d)) = 0$. For $n = 1$, $F_1$ is the blow-up of $\mathbb{P}^2_k$ at a point (Theorem P3.11.26), and $h^0(\mathcal{O}(1)) = 3$.

**Example P4.4.19 (the first nonzero $R^1$).** By Proposition P4.4.16, $R^1 \pi_* \mathcal{O}_{\tilde X}(E) = 0$, and $R^1 \pi_* \mathcal{O}_{\tilde X}(2E)$ is the skyscraper $k$ at the origin, spanned by the class of the monomial $x^{-2} v^{-1} = x^{-1} y^{-1}$ on $U_1 \cap U_2$. The restriction $\mathcal{O}_{\tilde X}(E)|_E$ is $\mathcal{O}_{\mathbb{P}^1}(-1)$ (Exercise 4), so the sequence $0 \to \mathcal{O}((m-1)E) \to \mathcal{O}(mE) \to \mathcal{O}_E(-m) \to 0$ raises $h^1$ by at most $h^1(\mathbb{P}^1, \mathcal{O}(-m)) = m - 1$, and $\sum_{j=1}^m (j - 1) = m(m-1)/2$ shows that every step raises it by exactly that much. Since $K_{\tilde X} = E$ relative to $\pi$ (Theorem P3.12.32), $mE - K_{\tilde X} = (m-1)E$ has degree $1 - m$ on $E$. It is $\pi$-nef exactly for $m \leq 1$, and by Proposition P4.4.16 these are exactly the $m$ for which $R^1 \pi_* \mathcal{O}(mE)$ vanishes, as the relative Kawamata-Viehweg theorem predicts.

### Proof

*Theorem P4.4.14.* All four sheaves in parts 1 to 3 are quasi-coherent by Theorem P4.4.1, and the claims are local on $Y$. Over an affine open $V = \operatorname{Spec} A$ on which $\mathcal{E}$ is free, $\pi^{-1}(V) \cong \mathbb{P}^{r-1}_A$ with $\mathcal{O}_P(n)$ corresponding to $\mathcal{O}(n)$. Example P4.4.4 with $r - 1$ in place of $r$ gives $R^q \pi_* \mathcal{O}_P(n)|_V = 0$ for $q \neq 0, r - 1$, $R^{r-1} \pi_* \mathcal{O}_P(n)|_V$ free of rank $\binom{-n-1}{r-1}$ for $n \leq -r$ and $0$ for $n > -r$, and $\pi_* \mathcal{O}_P(n)|_V$ free of rank $\binom{n + r - 1}{r - 1}$ for $n \geq 0$ and $0$ for $n < 0$. For $r = 1$, $P = Y$ and $\mathcal{O}_P(n) = \mathcal{E}^{\otimes n}$, and parts 1 and 2 are clear. The identification $\pi_* \mathcal{O}_P(n) \cong \operatorname{Sym}^n \mathcal{E}$ is part 3 of Proposition P3.6.35 for $n \geq 0$, and both sides are $0$ for $n < 0$. This proves parts 1 to 3.

For part 4, Proposition P4.4.10 gives $R^q \pi_*(\mathcal{O}_P(n) \otimes \pi^* \mathcal{G}) \cong R^q \pi_* \mathcal{O}_P(n) \otimes \mathcal{G}$. For $n > -r$ this is $0$ for $q > 0$ by part 2, and it is $\operatorname{Sym}^n \mathcal{E} \otimes \mathcal{G}$ for $q = 0$ by part 1. Corollary P2.4.27(1) then gives the isomorphism. $\square$

*Corollary P4.4.15.* Take $n = 0$ and $\mathcal{G} = \mathcal{O}_Y$ in Theorem P4.4.14, with $\operatorname{Sym}^0 \mathcal{E} = \mathcal{O}_Y$. The Euler characteristics agree because the groups do. $\square$

*Proposition P4.4.16.* The scheme $\tilde X$ is separated, being a closed subscheme of $\mathbb{A}^2_k \times \mathbb{P}^1_k$, and $Y$ is affine, so by part 1 of Corollary P4.4.2, $R^q \pi_* \mathcal{O}(mE) = H^q(\tilde X, \mathcal{O}(mE))^\sim$, and by Corollary P4.1.9 these groups are the cohomology of the Čech complex of the cover $(U_1, U_2)$. In particular they vanish for $q \geq 2$.

The sheaf $\mathcal{O}(mE)$ is generated by $x^{-m}$ on $U_1$ and by $y^{-m}$ on $U_2$, and $y^{-m} = x^{-m} v^{-m}$ with $v$ a unit on $U_1 \cap U_2$. Inside $K = k(x, v)$ the Čech complex is
$$x^{-m} k[x, v] \oplus y^{-m} k[y, u] \to x^{-m} k[x, v, v^{-1}], \qquad (s_1, s_2) \mapsto s_1 - s_2.$$
All three terms are spanned by monomials $x^a v^b$, and the map respects monomials. The first term is spanned by the monomials with $a \geq -m$ and $b \geq 0$. In the second, $y^{-m} y^c u^d = x^{c - m} v^{c - m - d}$ with $c, d \geq 0$, which is the set of monomials with $a \geq -m$ and $b \leq a$. The third term is spanned by all monomials with $a \geq -m$.

So $H^0$ is spanned by the monomials with $a \geq -m$ and $0 \leq b \leq a$, which forces $a \geq 0$. These are the monomials $x^a v^b = x^{a - b} y^b$ of degree $a$ in $x$ and $y$, of degree at least $\max(0, -m)$. For $m \geq 1$ this is $k[x, y]$, and for $m \leq 0$ it is $\mathfrak{m}^{-m}$.

$H^1$ is spanned by the monomials with $a \geq -m$ that satisfy neither $b \geq 0$ nor $b \leq a$, that is, $a < b < 0$. This needs $a \leq -2$, so for $-m \geq -1$, that is $m \leq 1$, there are none, and $H^1 = 0$, which covers part 1 and the case $m = 1$. For $m \geq 2$ the pairs are $-m \leq a \leq -2$ with $a < b \leq -1$, and for each $a$ there are $-a - 1$ values of $b$, so
$$\dim_k H^1(\tilde X, \mathcal{O}(mE)) = \sum_{a = -m}^{-2} (-a - 1) = \sum_{j = 1}^{m - 1} j = \frac{m(m-1)}{2}.$$
Multiplication by $x$ sends $x^a v^b$ to $x^{a+1} v^b$, and by $y = xv$ to $x^{a+1} v^{b+1}$, so a power of $\mathfrak{m}$ kills $H^1$, and $R^1 \pi_* \mathcal{O}(mE)$ is supported at the origin, of length $m(m-1)/2$. $\square$

### Exercises

1. (A) Use Corollary P4.4.15 to compute $h^p(\mathcal{O})$ for $\mathbb{P}^1_k \times_k \mathbb{P}^1_k$ and for $\mathbb{P}(\mathcal{O} \oplus \mathcal{O}(n))$ over a smooth projective curve $C$, in terms of $p_a(C)$.
2. (A) For $X = \mathbb{P}^1_k \times_k \mathbb{P}^1_k$, compute $h^0$, $h^1$ and $h^2$ of $\mathcal{O}(a, b)$ for all $a, b$ by the method of Example P4.4.17, and check that $\chi(\mathcal{O}(a, b)) = (a + 1)(b + 1)$.
3. (A) In Proposition P4.4.16, compute $H^0(\tilde X, \mathcal{O}(-mE))$ for $m = 1, 2$ as the span of the monomials of the proof, and identify it with $\mathfrak{m}$ and $\mathfrak{m}^2$.
4. (B) Show that $\mathcal{O}_{\tilde X}(E)|_E \cong \mathcal{O}_{\mathbb{P}^1}(-1)$, with $E = V(x) \subseteq U_1$ and $V(y) \subseteq U_2$ glued along $u = v^{-1}$, by comparing the generators $x^{-1}$ and $y^{-1} = x^{-1} v^{-1}$. Use the sequence of Example P4.4.19 to recompute the length of $R^1 \pi_* \mathcal{O}(mE)$ by induction on $m$, proving that each connecting map $H^0(\mathcal{O}_E(-m)) \to H^1(\mathcal{O}((m-1)E))$ is zero and that $H^1(\mathcal{O}(mE)) \to H^1(\mathcal{O}_E(-m))$ is surjective.
5. (B) Let $\mathcal{E}$ be locally free of rank $r \geq 2$ on $Y$. Show that $R^{r-1} \pi_* \mathcal{O}_P(-r)$ is an invertible sheaf, and, for $Y$ affine with $\mathcal{E}$ free, identify it with $\mathcal{O}_Y$. (In general it is $\det \mathcal{E}^\vee$, which needs the relative canonical sheaf of Chapter 7.)
6. (C) Let $\pi \colon \tilde X \to \mathbb{A}^n_k$ be the blow-up of the origin, $n \geq 2$, covered by $n$ charts. Show that $\pi_* \mathcal{O}_{\tilde X} = \mathcal{O}$ and $R^q \pi_* \mathcal{O}_{\tilde X} = 0$ for $q > 0$, and compute $R^{n-1} \pi_* \mathcal{O}(mE)$ for $m \geq n$, using the identification of $\tilde X$ with the total space of $\mathcal{O}_{\mathbb{P}^{n-1}}(-1)$.

### Lean

Projective bundles and blow-ups are not in Mathlib as schemes over a base with their twisting sheaves, and the computations of this section are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Theorem P4.4.14 is Hartshorne Exercise III.8.4 and EGA III.2.1.15. The vanishing $R^q \pi_* \mathcal{O}_{\tilde X} = 0$ for the blow-up of a smooth point is the first case of the theorem that smooth points, and more generally quotient and klt singularities in characteristic $0$, are rational singularities. The literature state is theorem. In the minimal model program the blow-up of a smooth point of a surface is the inverse of the simplest divisorial contraction, the contraction of a $(-1)$-curve, and Example P4.4.19 shows the relative Kawamata-Viehweg vanishing theorem at work: $R^q \pi_* \mathcal{O}_{\tilde X}(D) = 0$ for $q > 0$ when $D - K_{\tilde X}$ is $\pi$-nef, and the first failure occurs exactly when $D - K_{\tilde X}$ becomes negative on $E$. Corollary P4.4.15 is used for Mori fibre spaces that are projective bundles, whose total space and base have the same cohomology of the structure sheaf.
