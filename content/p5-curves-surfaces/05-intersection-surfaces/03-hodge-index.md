---
title: The Hodge index theorem and the Weil bound
nodes: []
sources: [Har77, Bea96, Rei97]
reads_with: [Har77:V.1, Bea96:ch1]
requires: [P3.6, P4.7, P5.1, P5.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Hodge index theorem and the Weil bound

### Statement

As before, $S$ is a smooth projective surface over an algebraically closed field $k$, and $K$ is a canonical divisor. A divisor $D$ is *effective up to linear equivalence* if $h^0(\mathcal{O}_S(D)) > 0$.

**Lemma P5.5.20 (ample divisors are positive on curves).** Let $H$ be an ample divisor. Then $H \cdot C > 0$ for every curve $C$ on $S$, and $H^2 > 0$.

Lean: not in Lean as stated.

**Lemma P5.5.21 (divisors of positive square).** Let $H$ be ample and $D$ a divisor with $D^2 > 0$ and $D \cdot H > 0$. Then $h^0(\mathcal{O}_S(nD)) \to \infty$ as $n \to \infty$, and in particular $nD$ is effective up to linear equivalence for $n$ large.

Lean: not in Lean as stated.

**Theorem P5.5.22 (Hodge index theorem).** Let $H$ be ample and $D$ a divisor with $D \cdot H = 0$. Then $D^2 \leq 0$, and $D^2 = 0$ if and only if $D \equiv 0$.

Lean: not in Lean as stated.

**Corollary P5.5.23 (the reverse Cauchy-Schwarz inequality).** Let $D$ be a divisor with $D^2 > 0$. Then for every divisor $E$,
$$(D \cdot E)^2 \geq D^2 \, E^2,$$
and if $D \cdot E = 0$, then $E^2 \leq 0$, with equality only if $E \equiv 0$. This applies to $D = H$ ample by Lemma P5.5.20.

Lean: not in Lean as stated.

**Corollary P5.5.24 (divisors on a product of curves).** Let $C_1$, $C_2$ be smooth projective curves, $S = C_1 \times C_2$, and $f_1 = \{x\} \times C_2$, $f_2 = C_1 \times \{y\}$ the fibres of the projections. For every divisor $D$ on $S$,
$$D^2 \leq 2 \, (D \cdot f_1)(D \cdot f_2).$$

Lean: not in Lean as stated.

For the last theorem, let $q$ be a power of a prime $p$ and $k = \overline{\mathbb{F}}_q$. Let $C \subseteq \mathbb{P}^n$ be a smooth projective curve of genus $g$ cut out by homogeneous polynomials with coefficients in $\mathbb{F}_q$. Its *$\mathbb{F}_q$-rational points* are the points with coordinates in $\mathbb{F}_q$, and $N = \# C(\mathbb{F}_q)$ is their number. The *$q$-power Frobenius* is the morphism
$$F \colon C \to C, \qquad [x_0 : \cdots : x_n] \mapsto [x_0^q : \cdots : x_n^q].$$

**Theorem P5.5.25 (Weil's bound).** In this situation
$$| N - q - 1 | \leq 2 g \sqrt{q}.$$

Lean: not in Lean as stated. Mathlib has finite fields and Frobenius (`frobenius`, `FiniteField.pow_card`), but not curves over them or their numbers of points as here.

### Proof in words

An ample divisor meets every curve positively, so a divisor with positive square and positive degree has many sections by Riemann-Roch: the term $h^2(nD) = h^0(K - nD)$ dies because $K - nD$ has negative degree. A divisor $D$ orthogonal to $H$ with $D^2 > 0$ would then make some $D + nH$ of the same kind, so $nD$ would be effective, and an effective divisor orthogonal to an ample class is zero. The rest is linear algebra of a form with one positive direction. On $C \times C$ over a finite field, the fixed points of the Frobenius are the intersection points of its graph $\Gamma$ with the diagonal $\Delta$, and they are transversal because the Frobenius has zero differential. Writing down the inequality of Corollary P5.5.24 for $r \Gamma + s \Delta$ gives a binary quadratic form in $(r, s)$ that is nonnegative, and its discriminant is the Weil bound.

### Examples

**Example P5.5.26 (the quadric surface).** On $\mathbb{P}^1 \times \mathbb{P}^1$ the form is $(a F_1 + b F_2) \cdot (c F_1 + d F_2) = ad + bc$ (Example P5.5.9), of signature $(1, 1)$. The ample class $H = F_1 + F_2$ has $H^2 = 2$, and its orthogonal complement is spanned by $F_1 - F_2$, with $(F_1 - F_2)^2 = -2 < 0$, as Theorem P5.5.22 requires. The hypothesis that $H$ is ample cannot be dropped. For $H' = F_1$, with $H'^2 = 0$, the class $D = F_1$ has $D \cdot H' = 0$ and $D^2 = 0$, but $D \not\equiv 0$. For $H'' = F_1 - F_2$, with $H''^2 = -2$, the class $D = F_1 + F_2$ has $D \cdot H'' = 0$ and $D^2 = 2 > 0$. The classes with $D^2 > 0$ are those with $ab > 0$, two opposite quadrants, and the ample classes $a, b > 0$ fill one of them.

**Example P5.5.27 (Hasse's bound).** For an elliptic curve over $\mathbb{F}_q$, Theorem P5.5.25 with $g = 1$ is Hasse's theorem $|N - q - 1| \leq 2 \sqrt{q}$, quoted in the notes to Section 4.1. The curve $y^2 = x^3 + x$ over $\mathbb{F}_5$ has the point at infinity and the three affine points $(0, 0)$, $(2, 0)$, $(3, 0)$: for $x = 1, 4$ the value $x^3 + x$ is $2$ or $3$, not a square. So $N = 4$ and $|4 - 6| = 2 \leq 2 \sqrt{5}$. Over $\mathbb{F}_2$, the curve $y^2 + y = x^3 + x$ is smooth, because the partial derivative in $y$ is $1$, and it has $N = 5$: the point at infinity and the four points with $x, y \in \mathbb{F}_2$. This is the largest value allowed, since $3 + 2\sqrt{2} < 6$. In general, Theorem P5.5.25 shows that a curve of genus $g$ over $\mathbb{F}_q$ has a rational point as soon as $\sqrt{q} \geq 2g$, because then $q + 1 - 2g \sqrt{q} \geq 1$.

**Example P5.5.28 (the Hermitian curve attains the bound).** Let $q = r^2$ with $r$ a power of $p$, and let $C$ be the plane curve $x^{r+1} + y^{r+1} + z^{r+1} = 0$ over $\mathbb{F}_q$. Its partial derivatives $(r + 1) x^r$, $(r+1) y^r$, $(r+1) z^r$ have no common zero, since $r + 1 \equiv 1 \pmod p$, so $C$ is smooth of genus $g = r(r - 1)/2$ (Example P5.5.16). The map $u \mapsto u^{r+1}$ is the norm $\mathbb{F}_q \to \mathbb{F}_r$; it sends $0$ to $0$, and each nonzero value is taken $r + 1$ times. Counting the affine solutions $(x, y, z) \in \mathbb{F}_q^3$ by the triples of norms $(a, b, c) \in \mathbb{F}_r^3$ with $a + b + c = 0$: there is one triple $(0, 0, 0)$, there are $3(r - 1)$ triples with exactly one zero, and $r^2 - 3r + 2$ triples with no zero. This gives
$$1 + 3(r-1)(r+1)^2 + (r - 1)(r - 2)(r + 1)^3 = 1 + (r - 1)(r + 1)^2 (r^2 - r + 1)$$
affine solutions, and dividing the nonzero ones by $q - 1 = (r - 1)(r + 1)$ gives $N = (r + 1)(r^2 - r + 1) = r^3 + 1$. On the other hand $q + 1 + 2 g \sqrt{q} = r^2 + 1 + r(r - 1) r = r^3 + 1$. So the Hermitian curve has the maximal number of points allowed by Theorem P5.5.25.

**Example P5.5.29 (curves of genus $0$).** For $g = 0$ the theorem says $N = q + 1$. For instance every smooth conic over $\mathbb{F}_q$ has $q + 1$ rational points, so it has one, and projection from it identifies the conic with $\mathbb{P}^1$ over $\mathbb{F}_q$. Over $\mathbb{R}$, where there is no Frobenius, the conic $x^2 + y^2 + z^2 = 0$ has no real points (Example P4.3.20).

### Proof

*Lemma P5.5.20.* By Theorem P3.6.25, $mH$ is very ample for some $m \geq 1$; fix an embedding $S \subseteq \mathbb{P}^N$ with $\mathcal{O}_S(1) = \mathcal{O}_S(mH)$. Write $C = \sum_i n_i C_i$ with $C_i$ integral and $n_i > 0$. Pick a closed point $x \in C_i$ and a hyperplane through $x$ that does not contain $C_i$. Its equation restricts to a nonzero section of $\mathcal{O}_{C_i}(mH)$ that vanishes at $x$, so its pullback to the normalization of $C_i$ is a nonzero section vanishing somewhere, and $\deg \mathcal{O}_{C_i}(mH) \geq 1$. By Theorem P5.5.6, $m H \cdot C = \sum_i n_i \deg \mathcal{O}_{C_i}(mH) > 0$. For $H^2$, take $C$ a curve in $|mH|$, so that $m H^2 = H \cdot C > 0$. $\square$

*Lemma P5.5.21.* By Theorem P5.5.13,
$$h^0(\mathcal{O}_S(nD)) + h^0(\mathcal{O}_S(K - nD)) \geq \chi(\mathcal{O}_S) + \tfrac{1}{2} n^2 D^2 - \tfrac{1}{2} n \, D \cdot K,$$
and the right side tends to infinity with $n$ because $D^2 > 0$. If $h^0(\mathcal{O}_S(K - nD)) > 0$, then $K - nD$ is linearly equivalent to an effective divisor, which is $0$ or a curve, and by Lemma P5.5.20, $H \cdot (K - nD) \geq 0$, that is, $n \leq (H \cdot K) / (H \cdot D)$. So $h^0(\mathcal{O}_S(K - nD)) = 0$ for $n$ large, and $h^0(\mathcal{O}_S(nD)) \to \infty$. $\square$

*Theorem P5.5.22.* Replacing $H$ by a multiple, by Theorem P3.6.25, assume $H$ very ample; the hypothesis $D \cdot H = 0$ is unchanged. Suppose $D^2 > 0$. By Lemma P5.5.1, $H' = D + nH$ is very ample for $n$ large, hence ample, and $D \cdot H' = D^2 + n D \cdot H = D^2 > 0$. By Lemma P5.5.21 for the pair $(D, H')$, some $mD$ with $m \geq 1$ is linearly equivalent to an effective divisor $C$. It is nonzero, since $(mD)^2 = m^2 D^2 > 0$, so $C$ is a curve and $H \cdot C > 0$ by Lemma P5.5.20. But $H \cdot C = m (H \cdot D) = 0$. This contradiction proves $D^2 \leq 0$.

Now suppose $D \cdot H = 0$, $D^2 = 0$, and $D \cdot E \neq 0$ for some divisor $E$. Put $E' = (H^2) E - (E \cdot H) H$. Then $E' \cdot H = 0$ and $D \cdot E' = (H^2)(D \cdot E) \neq 0$, since $H^2 > 0$ by Lemma P5.5.20. For an integer $t$, the divisor $D' = tD + E'$ satisfies $D' \cdot H = 0$ and
$$D'^2 = t^2 D^2 + 2t \, D \cdot E' + E'^2 = 2t \, D \cdot E' + E'^2.$$
For $|t|$ large with the sign of $D \cdot E'$, this is positive, contradicting the first part. So $D \equiv 0$. Conversely, $D \equiv 0$ gives $D^2 = 0$. $\square$

*Corollary P5.5.23.* Let $H$ be ample. First, $D \cdot H \neq 0$: otherwise Theorem P5.5.22 would give $D^2 \leq 0$. Let $E$ satisfy $D \cdot E = 0$, and suppose $E^2 > 0$; then $E \cdot H \neq 0$ in the same way. The divisor $G = (E \cdot H) D - (D \cdot H) E$ has $G \cdot H = 0$, so $G^2 \leq 0$ by Theorem P5.5.22. But
$$G^2 = (E \cdot H)^2 D^2 - 2 (E \cdot H)(D \cdot H)(D \cdot E) + (D \cdot H)^2 E^2 = (E \cdot H)^2 D^2 + (D \cdot H)^2 E^2 > 0.$$
So $E^2 \leq 0$. If $E^2 = 0$ and $E \not\equiv 0$, pick $E_1$ with $E \cdot E_1 \neq 0$ and put $E_2 = D^2 E_1 - (D \cdot E_1) D$, so that $D \cdot E_2 = 0$ and $E \cdot E_2 = D^2 (E \cdot E_1) \neq 0$. Then $tE + E_2$ is orthogonal to $D$ with $(tE + E_2)^2 = 2t (E \cdot E_2) + E_2^2 > 0$ for a suitable integer $t$, which was just excluded. For a general $E$, the divisor $E' = D^2 E - (D \cdot E) D$ has $D \cdot E' = 0$, so
$$0 \geq E'^2 = (D^2)^2 E^2 - 2 D^2 (D \cdot E)^2 + (D \cdot E)^2 D^2 = D^2 \big( D^2 E^2 - (D \cdot E)^2 \big),$$
and dividing by $D^2 > 0$ gives the inequality. $\square$

*Corollary P5.5.24.* The fibres $f_1$ and $\{x'\} \times C_2$ are disjoint for $x' \neq x$, so $f_1^2 = 0$, and likewise $f_2^2 = 0$. The curves $f_1$ and $f_2$ meet in the single point $(x, y)$, transversally, since local parameters at $x$ and $y$ pull back to a regular system of parameters of $\mathcal{O}_{S, (x, y)}$, so $f_1 \cdot f_2 = 1$ by Proposition P5.5.5. Put $h = f_1 + f_2$, with $h^2 = 2 > 0$. Let $d_1 = D \cdot f_1$, $d_2 = D \cdot f_2$, and
$$E = D - d_2 f_1 - d_1 f_2.$$
Then $E \cdot f_1 = d_1 - d_1 = 0$ and $E \cdot f_2 = d_2 - d_2 = 0$, so $E \cdot h = 0$ and $E^2 \leq 0$ by Corollary P5.5.23. Expanding,
$$E^2 = D^2 - 2 d_2 (D \cdot f_1) - 2 d_1 (D \cdot f_2) + 2 d_1 d_2 = D^2 - 2 d_1 d_2,$$
which gives the inequality. $\square$

*Theorem P5.5.25.* Let $r$ be the integer with $q = p^r$.

*Step 1: the Frobenius.* By Proposition P5.2.9, part 3, applied $r$ times, the composite of the $k$-linear Frobenius morphisms $C \to C^{(p)} \to \cdots \to C^{(p^r)}$ is $[x_i] \mapsto [x_i^q]$, and $C^{(p^r)}$ is defined by the equations of $C$ with coefficients raised to the power $q$, that is, by the same equations. So $F$ is a morphism $C \to C$ over $k$, of degree $q$ by part 1 of Proposition P5.2.9. A point $x = [x_0 : \cdots : x_n]$ is fixed by $F$ if and only if it is $\mathbb{F}_q$-rational. Indeed, if $[x_i^q] = [x_i]$, normalize a nonzero coordinate to $x_j = 1$; then $x_i^q = x_i$ for all $i$, so every $x_i \in \mathbb{F}_q$. The converse is clear.

*Step 2: transversality.* On $S = C \times C$ let $\Gamma$ be the graph of $F$ and $\Delta$ the diagonal. They are distinct integral curves, since $\deg F = q \neq 1$, and $\Gamma \cap \Delta$ is the set of points $(x, x)$ with $x$ fixed by $F$. Let $x$ be such a point, with $x_j \neq 0$, and $V = C \cap D_+(X_j)$, an affine open set with coordinate ring $A$ generated by $t_i = X_i / X_j$. Then $F^{-1}(V) = V$ and $F^*(t_i) = t_i^q$. The graph of $F|_V$ is the closed subscheme of $V \times V$ defined by the kernel of $A \otimes_k A \to A$, $a \otimes b \mapsto a F^*(b)$, which is generated by the elements $1 \otimes b - F^*(b) \otimes 1$. Pulling back along the diagonal, $a \otimes b \mapsto ab$, identifies $\Gamma \cap \Delta$ near $(x, x)$ with the closed subscheme of $V$ with ideal $\mathfrak{a}$ generated by the elements $b - F^*(b)$, $b \in A$. All of them vanish at $x$, since $F(x) = x$, so $\mathfrak{a} \subseteq \mathfrak{m}_x$. The values $c_i = t_i(x)$ lie in $\mathbb{F}_q$, and the elements $t_i - c_i$ generate $\mathfrak{m}_x$, so one of them, $u$, is a local parameter at $x$ by Nakayama's lemma. Then $F^*(u) = t_i^q - c_i = (t_i - c_i)^q = u^q$, and
$$u - F^*(u) = u (1 - u^{q-1}) \in \mathfrak{a}$$
with $1 - u^{q-1}$ a unit at $x$. So $\mathfrak{a} \mathcal{O}_{C,x} = \mathfrak{m}_x$, and the local intersection multiplicity of $\Gamma$ and $\Delta$ at $(x, x)$ is $1$. By Proposition P5.5.5, $\Gamma \cdot \Delta = N$.

*Step 3: the other intersection numbers.* By Example P5.5.19 with $d = q$ and with $d = 1$,
$$\Gamma \cdot f_1 = 1, \quad \Gamma \cdot f_2 = q, \quad \Gamma^2 = q (2 - 2g), \qquad \Delta \cdot f_1 = \Delta \cdot f_2 = 1, \quad \Delta^2 = 2 - 2g.$$

*Step 4: the quadratic form.* For integers $r', s$, let $D = r' \Gamma + s \Delta$. Then $D \cdot f_1 = r' + s$, $D \cdot f_2 = q r' + s$ and
$$D^2 = q(2 - 2g) r'^2 + 2 N r' s + (2 - 2g) s^2.$$
By Corollary P5.5.24, $D^2 \leq 2 (r' + s)(q r' + s) = 2 q r'^2 + 2 (q + 1) r' s + 2 s^2$. Simplifying,
$$Q(r', s) = g q \, r'^2 - (N - q - 1) \, r' s + g \, s^2 \geq 0$$
for all integers $r', s$. By homogeneity this holds for all rational $(r', s)$, and by continuity for all real ones. If $g = 0$, then $Q = -(N - q - 1) r' s$ is nonnegative everywhere only if $N = q + 1$. If $g \geq 1$, a positive semidefinite binary quadratic form has discriminant at most $0$:
$$(N - q - 1)^2 \leq 4 g^2 q,$$
which is the bound. $\square$

### Exercises

1. (A) On $\mathbb{P}^1 \times \mathbb{P}^1$, verify Corollary P5.5.23 directly for $D = a F_1 + b F_2$ with $a, b > 0$ and every $E = c F_1 + d F_2$.
2. (A) Let $H_1$ and $H_2$ be ample. Show that $(H_1 \cdot H_2)^2 \geq H_1^2 H_2^2$, and that equality holds on $\mathbb{P}^2$ but not for $F_1 + F_2$ and $F_1 + 2 F_2$ on $\mathbb{P}^1 \times \mathbb{P}^1$.
3. (B) Let $D^2 > 0$ and $D \cdot H > 0$ for one ample $H$. Show that $D \cdot H' > 0$ for every ample $H'$. Use that $a H + b H'$ is ample for positive integers $a$, $b$.
4. (B) For $C$ as in Theorem P5.5.25 and $m \geq 1$, show that $N_m = \# C(\mathbb{F}_{q^m})$ satisfies $|N_m - q^m - 1| \leq 2g \, q^{m/2}$, and that $C$ has points over $\mathbb{F}_{q^m}$ for all $m$ large.
5. (B) Show that Theorem P5.5.25 allows at most $8$ points on a curve of genus $2$ over $\mathbb{F}_2$. Using the canonical map of degree $2$ to $\mathbb{P}^1$ (Theorem P5.1.23), show that there are in fact at most $6$.
6. (C) Let $C$ be a smooth projective curve of genus $g$ and $\varphi \colon C \to C$ a morphism of degree $d$ other than the identity. Show that $\Gamma_\varphi \cdot \Delta \leq d + 1 + 2g \sqrt{d}$. Deduce that an automorphism $\varphi \neq \operatorname{id}$ of a curve of genus $g \geq 2$ has at most $2g + 2$ fixed points, counted with multiplicity.

### Lean

Mathlib has neither intersection numbers on surfaces nor the Hodge index theorem. For the Weil bound it has the finite field facts used in Step 1, such as `FiniteField.pow_card` ($a^q = a$ in $\mathbb{F}_q$), and the theory of elliptic curves over fields, but not the count of points of a curve over a finite field. The handbook adds no `MinimalModel` node here.

### Notes and history

The Hodge index theorem over $\mathbb{C}$ is a consequence of the Hodge decomposition, through the Hodge-Riemann bilinear relations, which give the signature $(1, h^{1,1} - 1)$ of the intersection form on $H^{1,1}$. The algebraic proof in every characteristic is due to Segre (1937) and Bronowski (1938), with the version above due to Grothendieck (1958). The literature state is theorem. Weil announced the Riemann hypothesis for curves over finite fields in 1940 and published proofs in 1948, one through the Jacobian and one through correspondences on $C \times C$; the proof above, by the Hodge index theorem on $C \times C$, is Mattuck and Tate's (1958) and Grothendieck's. The bound for all extensions $\mathbb{F}_{q^m}$ (Exercise 4) is equivalent to the Riemann hypothesis for the zeta function of $C$. Hasse had proved the case $g = 1$ in 1933. Combined with the theorem of Néron and Severi that $\operatorname{Num}(S)$ is finitely generated, Theorem P5.5.22 says that $\operatorname{Num}(S) \otimes \mathbb{R}$ has signature $(1, \rho - 1)$. In the minimal model program this is the reason the nef cone of a surface lies in the closure of one component of the positive cone $\{ D : D^2 > 0 \}$, and the reverse Cauchy-Schwarz inequality is the surface case of the Khovanskii-Teissier inequalities for nef divisors.
