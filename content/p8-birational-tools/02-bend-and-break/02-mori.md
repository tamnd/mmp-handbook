---
title: Mori's theorem on the existence of rational curves
nodes: []
sources: [Mor79, Mor82, KM98, Deb01, Kol96, Eis95, Har77, Stacks]
reads_with: [KM98:1.2, Deb01:3, Kol96:II.5]
requires: [P3.12, P4.5, P5.1, P5.2, P5.5, P5.6, P5.9, P5.12, P7.1, P7.2, P7.3, P7.4, P8.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Mori's theorem on the existence of rational curves

### Statement

In this section $X$ is a smooth projective variety of dimension $n$ over an algebraically closed field $k$, $C$ is a smooth projective curve of genus $g$, and $f \colon C \to X$ is a morphism. The notation of Section 2.1 is in force: $f_* C$ is the image cycle and a rational curve is a curve with normalization $\mathbb{P}^1$. An ample divisor is a Cartier divisor, so its degree on a curve is a positive integer.

**Theorem P8.2.9 (rational curves in characteristic $p$).** Let $k$ have characteristic $p > 0$, and suppose $-K_X \cdot f_* C > 0$. Then for every closed point $c \in C$ there is a rational curve on $X$ through $f(c)$.

Lean: not in Lean as stated.

**Theorem P8.2.10 (bend-and-break with a degree bound, cited).** Let $X$ be a projective variety, $H$ an ample divisor on $X$, $B \subseteq C$ a set of $b \geq 1$ closed points, and suppose
$$\dim_{[f]} \operatorname{Hom}(C, X; f|_B) \geq 1.$$
Then there is a rational curve $\Gamma \subseteq X$ meeting $f(B)$ with
$$H \cdot \Gamma \leq \frac{2 \, H \cdot f_* C}{b}.$$

Lean: not in Lean as stated.

**Corollary P8.2.11 (the degree bound in characteristic $p$).** Let $k$ have characteristic $p > 0$, $H$ an ample divisor on $X$, and suppose $d = -K_X \cdot f_* C > 0$. Then there is a rational curve $\Gamma \subseteq X$ with
$$H \cdot \Gamma \leq \frac{2 n \, H \cdot f_* C}{-K_X \cdot f_* C}.$$

Lean: not in Lean as stated.

**Theorem P8.2.12 (the degree bound in characteristic $0$).** The conclusion of Corollary P8.2.11 holds when $k$ has characteristic $0$.

Lean: not in Lean as stated.

**Theorem P8.2.13 (Mori).** Let $X$ be a smooth projective variety of dimension $n$ over an algebraically closed field of any characteristic, and suppose that $K_X$ is not nef. Then $X$ contains a rational curve $\Gamma$ with
$$0 < -K_X \cdot \Gamma \leq n + 1.$$

Lean: not in Lean as stated.

**Example P8.2.14 (lines in projective space).** Let $X = \mathbb{P}^n$ and $L$ a line. Then $K_{\mathbb{P}^n} = -(n + 1) H$ for a hyperplane $H$, by the Euler sequence of Theorem P3.12.20, and $H \cdot L = 1$, so $-K_{\mathbb{P}^n} \cdot L = n + 1$. Every curve $\Gamma$ on $\mathbb{P}^n$ has $-K \cdot \Gamma = (n + 1) \deg \Gamma \geq n + 1$, so the bound of Theorem P8.2.13 is attained, and attained only by lines.

**Example P8.2.15 (surfaces).** For a smooth projective surface, Theorem P8.2.13 gives a rational curve with $-K \cdot \Gamma \in \{1, 2, 3\}$. All three values occur. On a smooth cubic surface $S \subseteq \mathbb{P}^3$, $-K_S$ is the hyperplane class, and a line $L$ has $-K_S \cdot L = 1$. On $\mathbb{P}^1 \times \mathbb{P}^1$, $-K$ has bidegree $(2, 2)$ and a ruling $F$ has $-K \cdot F = 2$. On the blow-up of $\mathbb{P}^2$ at a point, the exceptional curve $E$ has $K \cdot E = E^2 = -1$ by Theorem P5.6.3, so $-K \cdot E = 1$, and the strict transform of a line through the point, a fibre of the ruling, has $-K \cdot F = 2$. On $\mathbb{P}^2$ a line has $-K \cdot L = 3$.

**Example P8.2.16 (where the Frobenius is needed).** Let $X = \mathbb{P}^2$ and $C \subseteq X$ a smooth plane cubic, of genus $1$, with $f$ the inclusion. Then $-K \cdot C = 9$ and Corollary P8.1.12 gives $\dim_{[f]} \operatorname{Hom}(C, \mathbb{P}^2; f|_{\{c\}}) \geq 9 + 2 (1 - 1) - 2 = 7$, so Theorem P8.2.5 applies directly, in any characteristic, and gives a rational curve through every point of $C$. If instead $C$ has genus $g$ and $-K \cdot f_* C = 1$, the estimate with one fixed point is $1 - n g$, which is negative as soon as $g \geq 1$, and no deformation of $f$ is guaranteed. In characteristic $p$, composing with the Frobenius $q$ times replaces $1 - n g$ by $q - n g$, and this is what the proof of Theorem P8.2.9 uses. On an abelian variety $K_X = 0$ is nef and there are no rational curves at all, as Exercise 3 of Section 2.1 shows from the other side.

### Proof in words

The dimension estimate $\dim_{[f]} \operatorname{Hom}(C, X; f|_B) \geq -K_X \cdot f_* C + n(1 - g) - n b$ is useless when the genus is large compared with $-K_X \cdot f_* C$. In characteristic $p$, the Frobenius morphism $C_m \to C$ of degree $q = p^m$ does not change the genus, while composing with it multiplies $-K_X \cdot f_* C$ by $q$. For $q$ large the composite deforms with about $q d / n$ points fixed, and bend-and-break gives a rational curve, of $H$-degree at most $2 q \, H \cdot f_* C$ divided by the number of fixed points, which tends to $2 n \, H \cdot f_* C / d$.

In characteristic $0$ there is no Frobenius. The variety, the curve and the morphism are defined over a finitely generated ring $R \subseteq k$, and their reductions modulo the maximal ideals of $R$ live over finite fields. Each reduction contains a rational curve of bounded degree, so the scheme of morphisms $\mathbb{P}^1 \to X_R$ of bounded degree, which is of finite type over $R$, has points over every closed point of $\operatorname{Spec} R$. Its image is constructible, so it contains the generic point, and the generic fibre has a point over $k$.

For Mori's theorem, the bound is applied to the ample divisor $H + t K_X$, with $t$ just below the nef threshold of $H$ with respect to $K_X$. A curve on which $H + s K_X$ is negative, for $s$ just above the threshold, gives a rational curve on which $H + t K_X$ has degree less than $1$, and this forces $K_X$ to be negative on it. A $K_X$-negative rational curve of least $H$-degree has $-K_X \cdot \Gamma \leq n + 1$: otherwise it deforms with two points fixed in a family of dimension at least $2$, and the second form of bend-and-break splits it into curves of smaller degree, one of which is still $K_X$-negative.

### Examples

*Example P8.2.14.* A line $f \colon \mathbb{P}^1 \to \mathbb{P}^n$ has $f^* T_{\mathbb{P}^n} \cong \mathcal{O}(2) \oplus \mathcal{O}(1)^{n-1}$, as in Example P8.2.8, so with two points fixed it moves in a family of dimension $(n + 1) - n = 1$. This is the borderline case of the last step in the proof of Theorem P8.2.13: the curve does not break, and $-K \cdot L = n + 1$ exactly.

*Example P8.2.15.* The values follow from $K_{\mathbb{P}^1 \times \mathbb{P}^1} = -2F_1 - 2F_2$ by part 3 of Theorem P5.9.4, from $F_1 \cdot F_2 = 1$ and $F_i^2 = 0$, and, on the blow-up, from $K = \pi^* K_{\mathbb{P}^2} + E$ and the class $\pi^* \ell - E$ of the fibre, which give $-K \cdot (\pi^* \ell - E) = 3 - 1 = 2$. For the cubic surface, $K_S = (K_{\mathbb{P}^3} + S)|_S = -H|_S$ by adjunction, as in Section 1.3.

*Example P8.2.16.* For the cubic, $-K_{\mathbb{P}^2} \cdot C = 3 \cdot 3$, and Theorem P8.2.5 gives $3 \ell \equiv f'_* C + Z$ with $Z$ a nonzero sum of rational curves through $f(c)$. Since $Z \neq 0$ and $f'_* C$ is effective, $Z$ has degree $1$, $2$ or $3$, so its components are lines, smooth conics or singular rational cubics.

### Proof

*Theorem P8.2.9.* Let $K = K(C)$. Since $k$ is perfect, $K^{1/p} = \{a : a^p \in K\}$ is a function field of one variable over $k$, isomorphic to $K$ as a field by $a \mapsto a^p$. Let $C_1$ be the smooth projective curve with function field $K^{1/p}$, by Theorem P5.1.3. The inclusion $K \subseteq K^{1/p}$ gives a morphism $C_1 \to C$, which is the Frobenius morphism of $C_1$, since $K = (K^{1/p})^p$. By Proposition P5.2.9, it has degree $p$ and $g(C_1) = g(C)$. Iterating $m$ times gives a morphism $\phi \colon C_m \to C$ of degree $q = p^m$, bijective on points, with $g(C_m) = g$. Let $h = f \circ \phi$ and $d = -K_X \cdot f_* C > 0$. Then $h_* C_m = q f_* C$ and $-K_X \cdot h_* C_m = q d$. Let $c_m \in C_m$ be the point over $c$. By Corollary P8.1.12 with $b = 1$,
$$\dim_{[h]} \operatorname{Hom}(C_m, X; h|_{\{c_m\}}) \geq q d + n(1 - g) - n = q d - n g,$$
which is at least $1$ for $m$ large. Theorem P8.2.5 gives a nonzero sum of rational curves whose support contains $h(c_m) = f(c)$.

*Theorem P8.2.10.* This is in Kollár and Mori, Section 1.2 (KM98), and Kollár, Section II.5 (Kol96); see also Debarre, Chapter 3 (Deb01). It goes back to Mori (Mor79, Mor82). The proof is not given here. It refines the proof of Theorem P8.2.5: a curve through $[f]$ in $\operatorname{Hom}(C, X; f|_B)$ gives a blown-up surface $S'$ and a morphism $F' \colon S' \to X$ that contracts the strict transforms $\Sigma_1, \dots, \Sigma_b$ of the curves $\{c_i\} \times \bar T$, and the Hodge index theorem applied to $F'^* H$ and the $\Sigma_i$ bounds the total $H$-degree of the images of the exceptional curves over the $b$ points of indeterminacy, so that one of the $b$ points contributes a rational curve of $H$-degree at most $2 H \cdot f_* C / b$.

*Corollary P8.2.11.* Let $\phi \colon C_m \to C$ and $q = p^m$ be as in the proof of Theorem P8.2.9, and $h = f \circ \phi$. For $q$ large, the integer
$$b_q = \left\lfloor \frac{q d - n g - 1}{n} \right\rfloor + 1$$
is at least $1$, and $n b_q \leq q d - n g + n - 1$. Choose a set $B \subseteq C_m$ of $b_q$ closed points. By Corollary P8.1.12,
$$\dim_{[h]} \operatorname{Hom}(C_m, X; h|_B) \geq q d + n(1 - g) - n b_q \geq 1.$$
By Theorem P8.2.10 there is a rational curve $\Gamma_q$ with
$$H \cdot \Gamma_q \leq \beta_q = \frac{2 \, H \cdot h_* C_m}{b_q} = \frac{2 q \, H \cdot f_* C}{b_q}.$$
Since $b_q / q \to d / n$ as $q \to \infty$, $\beta_q \to \beta = 2 n \, H \cdot f_* C / d$. So $\beta_q < \lfloor \beta \rfloor + 1$ for $q$ large, and since $H \cdot \Gamma_q$ is an integer, $H \cdot \Gamma_q \leq \lfloor \beta \rfloor \leq \beta$.

*Theorem P8.2.12.* Both sides of the inequality are multiplied by $m$ when $H$ is replaced by $m H$, so assume that $H$ is very ample, and embed $X \subseteq \mathbb{P}^N$ by $H$. Let $D = \lfloor 2 n \, H \cdot f_* C / d \rfloor$ and, for $1 \leq e \leq D$, $P_e(m) = (1 + e) m + 1$, the Hilbert polynomial of the graph of a morphism $\mathbb{P}^1 \to \mathbb{P}^N$ of degree $e$ with respect to $\mathcal{O}(1, 1)$, as in Exercise 4 of Section 1.1.

The following facts are cited from the standard limit arguments (Stacks, the chapter on limits of schemes; Kollár, Section II.5 (Kol96)). The equations of $X$, of an embedding of $C$, of the graph of $f$ and of the finitely many coefficients that occur lie in a subring $R \subseteq k$ finitely generated over $\mathbb{Z}$, and after inverting one nonzero element of $R$ there are a smooth projective morphism $X_R \to \operatorname{Spec} R$ with $X_R \subseteq \mathbb{P}^N_R$ and $X_R \times_R k \cong X$, a smooth projective curve $C_R \to \operatorname{Spec} R$ with geometrically connected fibres of genus $g$ and $C_R \times_R k \cong C$, a morphism $f_R \colon C_R \to X_R$ over $R$ restricting to $f$, and an invertible sheaf $\omega_{X_R / R}$ restricting to the canonical sheaf on every geometric fibre.

Let $\mathfrak{m} \subseteq R$ be a maximal ideal. The residue field $R / \mathfrak{m}$ is finite, because $R$ is a finitely generated $\mathbb{Z}$-algebra (Eisenbud, Theorem 4.19 (Eis95)), so of positive characteristic $p$. Let $\bar s$ be an algebraic closure of $R / \mathfrak{m}$ and $X_{\bar s}$, $C_{\bar s}$, $f_{\bar s}$ the base changes. The degrees $\deg f_R^* \omega_{X_R / R}^{-1}$ and $\deg f_R^* \mathcal{O}(1)$ on the fibres of $C_R$ are locally constant on $\operatorname{Spec} R$ by Theorem P4.5.13, since they are differences of Euler characteristics of flat sheaves, and $\operatorname{Spec} R$ is connected because $R$ is a domain. So $-K_{X_{\bar s}} \cdot f_{\bar s *} C_{\bar s} = d$ and $H \cdot f_{\bar s *} C_{\bar s} = H \cdot f_* C$. By Corollary P8.2.11 there is a rational curve $\Gamma \subseteq X_{\bar s}$ with $H \cdot \Gamma \leq D$, and its normalization $\mathbb{P}^1 \to X_{\bar s}$ is a morphism of degree $e = H \cdot \Gamma$ with $1 \leq e \leq D$. So the scheme
$$M = \bigsqcup_{e = 1}^{D} \operatorname{Hom}^{P_e}_R(\mathbb{P}^1_R, X_R),$$
quasi-projective over $R$ by Theorem P8.1.4, has a point over every closed point of $\operatorname{Spec} R$. Its image in $\operatorname{Spec} R$ is constructible by Chevalley's theorem (Hartshorne, Exercise II.3.19 (Har77)). A finitely generated $\mathbb{Z}$-algebra is a Jacobson ring (Eis95, Theorem 4.19), so every nonempty constructible subset of $\operatorname{Spec} R$ contains a closed point; applied to the complement of the image, this shows that the image is all of $\operatorname{Spec} R$, and in particular contains the generic point. So $M \times_R \operatorname{Frac}(R)$ is a nonempty scheme of finite type over $\operatorname{Frac}(R) \subseteq k$, and $M \times_R k$ is nonempty and of finite type over the algebraically closed field $k$, so it has a $k$-point. This is a morphism $\mathbb{P}^1 \to X$ whose graph has Hilbert polynomial $P_e$ with $1 \leq e \leq D$, a morphism of degree $e$ with respect to $H$. Its image $\Gamma$ is a rational curve with $H \cdot \Gamma \leq e \leq D$.

*Theorem P8.2.13.* Fix an ample divisor $H$. Since $K_X$ is not nef, there is a curve $C_1$ with $K_X \cdot C_1 < 0$. Let
$$t_0 = \sup \{ t \geq 0 : H + t K_X \text{ is nef} \}.$$
By part 3 of Theorem P7.4.9 the ample cone is open, so $H + t K_X$ is ample for small $t > 0$, and $t_0 > 0$; and $(H + t K_X) \cdot C_1 < 0$ for $t > H \cdot C_1 / (-K_X \cdot C_1)$, so $t_0 < \infty$. The nef cone is closed and convex by part 2 of Theorem P7.4.9, so $H + t K_X$ is nef exactly for $0 \leq t \leq t_0$. For $0 \leq t < t_0$,
$$H + t K_X = \left(1 - \frac{t}{t_0}\right) H + \frac{t}{t_0} (H + t_0 K_X)$$
is the sum of an ample and a nef class, which is ample by part 2 of Theorem P7.3.11.

Choose rational numbers $0 < t < t_0 < s$ with $s - t < 1 / (2n)$. Since $H + s K_X$ is not nef, there is a curve $C'$ with $(H + s K_X) \cdot C' < 0$; then $-K_X \cdot C' > H \cdot C' / s > 0$. Let $f \colon C \to X$ be the normalization of $C'$, so $f_* C = C'$, and let $m \geq 1$ be an integer with $A = m (H + t K_X)$ an ample Cartier divisor. By Corollary P8.2.11 or Theorem P8.2.12 there is a rational curve $\Gamma_1$ with
$$(H + t K_X) \cdot \Gamma_1 = \frac{A \cdot \Gamma_1}{m} \leq \frac{2 n \, (H + t K_X) \cdot C'}{-K_X \cdot C'} = 2 n \left( \frac{H \cdot C'}{-K_X \cdot C'} - t \right) < 2 n (s - t) < 1.$$
If $K_X \cdot \Gamma_1 \geq 0$, then $(H + t K_X) \cdot \Gamma_1 \geq H \cdot \Gamma_1 \geq 1$, a contradiction. So $K_X \cdot \Gamma_1 < 0$.

So the set of rational curves $\Gamma$ with $K_X \cdot \Gamma < 0$ is nonempty. Choose one, $\Gamma$, with $H \cdot \Gamma$ as small as possible, and let $f \colon \mathbb{P}^1 \to \Gamma$ be its normalization, so $f_* \mathbb{P}^1 = \Gamma$. Suppose $-K_X \cdot \Gamma \geq n + 2$. By Corollary P8.1.12 with $b = 2$,
$$\dim_{[f]} \operatorname{Hom}(\mathbb{P}^1, X; f|_{\{0, \infty\}}) \geq -K_X \cdot \Gamma + n - 2 n \geq 2.$$
By Theorem P8.2.6, $\Gamma \equiv \sum_i a_i \Gamma_i$ with rational curves $\Gamma_i$, integers $a_i > 0$ and $\sum_i a_i \geq 2$. Then $-K_X \cdot \Gamma = \sum_i a_i (-K_X \cdot \Gamma_i) > 0$, so $K_X \cdot \Gamma_i < 0$ for some $i$. Since $H \cdot \Gamma = \sum_j a_j H \cdot \Gamma_j$ with every $H \cdot \Gamma_j \geq 1$ and $\sum_j a_j \geq 2$, $H \cdot \Gamma_i \leq H \cdot \Gamma - 1$. This contradicts the minimality of $H \cdot \Gamma$. Hence $0 < -K_X \cdot \Gamma \leq n + 1$.

### Exercises

1. (A) Let $X = \mathbb{P}^n$ and $H$ a hyperplane. Show that $H + t K$ is nef exactly for $t \leq 1 / (n + 1)$, so $t_0 = 1 / (n + 1)$ in the proof of Theorem P8.2.13, and that the rational curve of least degree produced there is a line.
2. (A) Let $X = \mathbb{P}^1 \times \mathbb{P}^1$ and $H = F_1 + F_2$. Compute $t_0 = 1/2$ and show that every $K$-negative rational curve of least $H$-degree is a ruling, with $-K \cdot F_i = 2$.
3. (B) Let $k$ have characteristic $p > 0$ and let $X$ be a smooth projective variety with $-K_X$ ample. Using Lemma P8.2.2 and Theorem P8.2.9, show that through every closed point of $X$ there is a rational curve.
4. (B) Let $S$ be a smooth projective surface with $K_S$ not nef. Show that $S$ contains a rational curve $\Gamma$ with $0 < -K_S \cdot \Gamma \leq 3$, and that if also $\Gamma^2 < 0$, then $\Gamma$ is a $(-1)$-curve, using part 2 of Corollary P5.5.15.
5. (B) In the proof of Theorem P8.2.13, show that the curve $\Gamma$ of least $H$-degree satisfies the stronger conclusion that $\dim_{[f]} \operatorname{Hom}(\mathbb{P}^1, X; f|_{\{0, \infty\}}) \leq 1$, and compute this dimension for a line in $\mathbb{P}^n$ and a ruling of $\mathbb{P}^1 \times \mathbb{P}^1$.
6. (C) Let $f \colon \mathbb{P}^1 \to \mathbb{P}^n$ be an isomorphism onto a smooth conic, $n \geq 2$. Show that $f^* T_{\mathbb{P}^n}(-2)$ is a quotient of $\mathcal{O}^{\oplus (n+1)}$, that $\operatorname{Hom}(\mathbb{P}^1, \mathbb{P}^n; f|_{\{0, \infty\}})$ is smooth of dimension $n + 2$ at $[f]$, and, using a family as in Example P8.2.7, that the conic degenerates to two lines, one through $f(0)$ and one through $f(\infty)$.

### Lean

The nef threshold $t_0$ of the proof of Theorem P8.2.13 is `MinimalModel.nefThreshold` in `MinimalModel/Statements/Basic.lean`, the supremum of the $t \geq 0$ with $H + t D$ nef, stated for the intersection data `MinimalModel.IntersectionData`; nefness is `MinimalModel.IsNef`, and `MinimalModel.ExtremalRay` is the structure of an extremal ray of the closed cone of curves. Rational curves, the Frobenius morphism of a curve, spreading out and the scheme of morphisms are not in the repository, and Mori's theorem is not stated there. The toric cone theorem `MinimalModel.Toric.toricConeTheorem` is proved in the repository; it is combinatorial, and the curves in it are the torus-invariant curves of walls, which are rational, but no statement about rational curves is made.

### Notes and history

Mori proved Theorem P8.2.9 and its consequence in characteristic $0$ in his proof of Hartshorne's conjecture (Mor79), and Theorem P8.2.13 in his paper on extremal rays (Mor82), where the bound $n + 1$ and the rational curves on extremal rays first appear. The proof through the nef threshold and the degree bound follows Kollár and Mori, Sections 1.2 and 1.3 (KM98), and Debarre, Chapter 3 (Deb01). Theorem 1.10 of KM98 is stronger than Theorem P8.2.13: if $-K_X \cdot C > 0$ for a curve $C$, then through every point $x \in C$ there is a rational curve $\Gamma$ with $H \cdot \Gamma \leq 2 n \, H \cdot C / (-K_X \cdot C)$ and $-K_X \cdot \Gamma \leq n + 1$; the proof keeps track of the point in the reduction modulo $p$. The statement that every $K_X$-negative extremal ray contains a rational curve with $0 < -K_X \cdot \Gamma \leq n + 1$ is Theorem P5.12.13; it combines the argument above with the cone theorem. No proof of the existence of rational curves in characteristic $0$ that avoids the reduction to characteristic $p$ is known.
