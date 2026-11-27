---
title: The cone of curves of a surface
nodes: []
sources: [Har77, KM98, Laz04, Kle66, Bea96]
reads_with: [KM98:ch1, Laz04:ch1, Har77:V.1]
requires: [P3.6, P3.13, P4.2, P4.5, P4.6, P5.4, P5.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The cone of curves of a surface

### Statement

In this chapter $k$ is algebraically closed, $S$ is a smooth projective surface over $k$, and the notation of Chapter 5 is in force: curves are effective divisors, $K = K_S$ is a canonical divisor, and $\operatorname{Num}(S)$ is the group of divisors modulo numerical equivalence (Definition P5.5.7). By the theorem of the base of Néron and Severi, $\operatorname{Num}(S)$ is a free abelian group of finite rank (Kleiman, SGA 6, Exposé XIII, and Lazarsfeld, *Positivity I*, Proposition 1.1.16). Its rank $\rho(S)$ is the *Picard number* of $S$. On a surface, curves and divisors are the same objects, so the space of curves and the space of divisors of Volume 1 coincide, and one space carries both.

**Definition P5.12.1 (the cones of a surface).** Let $N^1(S) = \operatorname{Num}(S) \otimes_\mathbb{Z} \mathbb{R}$, a real vector space of dimension $\rho(S)$ with the Euclidean topology, on which the intersection pairing extends to a symmetric bilinear form $x \cdot y$. Write $[D]$ for the class of a divisor $D$.

1. The *cone of curves* $NE(S) \subseteq N^1(S)$ is the set of finite sums $\sum a_i [C_i]$ with $a_i \geq 0$ real and $C_i$ integral curves, and $\overline{NE}(S)$ is its closure, the *closed cone of curves*.
2. The *nef cone* is $\operatorname{Nef}(S) = \{ x : x \cdot C \geq 0 \text{ for every integral curve } C \}$. A divisor is *nef* if its class is nef.
3. The *ample cone* $\operatorname{Amp}(S)$ is the set of finite sums $\sum a_i [H_i]$ with $a_i > 0$ real and $H_i$ ample divisors.
4. For a fixed ample divisor $H$, the *positive cone* is $\mathcal{P}(S) = \{ x : x^2 > 0, \ x \cdot H > 0 \}$.
5. For a class $d$, write $\overline{NE}(S)_{d \geq 0} = \{ y \in \overline{NE}(S) : d \cdot y \geq 0 \}$, and similarly with $> 0$, $\leq 0$ or $< 0$. Write $d^\perp = \{ y : d \cdot y = 0 \}$.
6. A closed convex subcone $F \subseteq \overline{NE}(S)$ is an *extremal face* if $u, v \in \overline{NE}(S)$ and $u + v \in F$ imply $u, v \in F$. An *extremal ray* is an extremal face of the form $R = \mathbb{R}_{\geq 0} x$ with $x \neq 0$. It is *$K$-negative* if $K \cdot x < 0$.

The pairing on $N^1(S)$ is nondegenerate: in a $\mathbb{Z}$-basis of $\operatorname{Num}(S)$ its Gram matrix is an integer matrix with nonzero determinant by Definition P5.5.7, and the same matrix is the Gram matrix over $\mathbb{R}$. A real class is nef if and only if $x \cdot y \geq 0$ for every $y \in \overline{NE}(S)$, since $x \cdot (-)$ is linear and continuous. By Lemma P5.12.3 below, $\mathcal{P}(S)$ does not depend on the choice of $H$.

**Lemma P5.12.2 (ample classes are positive on the cone).** Let $H$ be an ample divisor.

1. For every divisor $D$ there is $m_0$ such that $mH + D$ is nef for $m \geq m_0$.
2. $H \cdot y > 0$ for every $y \in \overline{NE}(S) \setminus \{0\}$.
3. The slice $\Sigma_H = \{ y \in \overline{NE}(S) : H \cdot y = 1 \}$ is compact, and there is a constant $c > 0$ with $|y| \leq c \, (H \cdot y)$ for all $y \in \overline{NE}(S)$, for any fixed norm on $N^1(S)$. In particular $\overline{NE}(S) \cap (-\overline{NE}(S)) = \{0\}$.

Lean: not in Lean as stated.

**Lemma P5.12.3 (the positive cone).** Let $H$ be an ample divisor.

1. For $x \in N^1(S)$ with $x \cdot H = 0$, $x^2 \leq 0$, with equality only if $x = 0$. The form on $N^1(S)$ has signature $(1, \rho(S) - 1)$.
2. For $x, y$ in the closure $\overline{\mathcal{P}}(S)$ of $\mathcal{P}(S)$, $x \cdot y \geq 0$, and $x \cdot y > 0$ if $x, y \in \mathcal{P}(S)$.
3. $\overline{\mathcal{P}}(S) = \{ x : x^2 \geq 0, \ x \cdot H \geq 0 \}$, and $\mathcal{P}(S) \subseteq \overline{\mathcal{P}}(S) \subseteq \overline{NE}(S)$. Every class $x \neq 0$ with $x^2 \geq 0$ lies in $\overline{\mathcal{P}}(S)$ or in $-\overline{\mathcal{P}}(S)$.
4. $\mathcal{P}(S)$ is open, and it does not depend on $H$.

Lean: not in Lean as stated.

**Lemma P5.12.4 (nef classes have nonnegative square).** Every $x \in \operatorname{Nef}(S)$ has $x^2 \geq 0$, so $\operatorname{Nef}(S) \subseteq \overline{\mathcal{P}}(S) \subseteq \overline{NE}(S)$. An integral curve $C$ with $C^2 \geq 0$ is nef.

Lean: not in Lean as stated.

**Theorem P5.12.5 (Nakai-Moishezon criterion).** A divisor $D$ on $S$ is ample if and only if $D^2 > 0$ and $D \cdot C > 0$ for every integral curve $C$.

Lean: not in Lean as stated.

**Theorem P5.12.6 (Kleiman's criterion).**

1. A divisor $D$ is ample if and only if $D \cdot y > 0$ for every $y \in \overline{NE}(S) \setminus \{0\}$.
2. $\operatorname{Amp}(S) = \{ x : x \cdot y > 0 \text{ for all } y \in \overline{NE}(S) \setminus \{0\} \}$, and this set is the interior of $\operatorname{Nef}(S)$. The nef cone is the closure of $\operatorname{Amp}(S)$.
3. $\overline{NE}(S) = \{ y : x \cdot y \geq 0 \text{ for all } x \in \operatorname{Nef}(S) \}$. So $\operatorname{Nef}(S)$ and $\overline{NE}(S)$ are dual cones.

Lean: not in Lean as stated.

### Proof in words

An ample divisor $H$ dominates every divisor, in the sense that $mH \pm D$ is globally generated for large $m$, so a class of $\overline{NE}(S)$ on which $H$ vanishes is killed by every divisor and is $0$. This makes the slice $H = 1$ of the cone compact, which is the one topological fact used throughout. The Hodge index theorem says that the form is negative definite on $H^\perp$, so $\{ x^2 > 0 \}$ has two halves, and the half containing $H$ is the positive cone. Its rational points are classes of effective divisors up to a multiple by Lemma P5.5.21, so it lies in $\overline{NE}(S)$. A nef class of negative square would pair negatively with a suitable boundary point of the positive cone, which is again in $\overline{NE}(S)$, so nef classes have nonnegative square. Nakai-Moishezon is the classical criterion, and it turns into Kleiman's criterion because a divisor positive on $\overline{NE}(S) \setminus \{0\}$ cannot have square $0$: it would lie in the closed positive cone, hence in $\overline{NE}(S)$, and pair to $0$ with itself. Duality is the separation theorem for closed convex cones, together with nondegeneracy of the pairing.

### Examples

**Example P5.12.7 (the plane blown up at a point).** Let $S = \operatorname{Bl}_p \mathbb{P}^2$, with $\operatorname{Num}(S) = \mathbb{Z} \ell \oplus \mathbb{Z} E$, $\ell^2 = 1$, $E^2 = -1$, $\ell \cdot E = 0$ and $K = -3\ell + E$ (Example P5.6.7). An integral curve other than $E$ is the strict transform $\tilde C$ of an integral plane curve $C$ of degree $d \geq 1$ with multiplicity $m \geq 0$ at $p$, of class $d\ell - mE$ by Proposition P5.6.4. If $\tilde C$ is not the strict transform of a line through $p$, choose a line $L$ through $p$; then $\tilde C \neq \tilde L$ and $0 \leq \tilde C \cdot \tilde L = (d\ell - mE) \cdot (\ell - E) = d - m$ by Proposition P5.5.5. So in all cases $m \leq d$ and
$$d\ell - mE = d(\ell - E) + (d - m) E,$$
a nonnegative combination of $[E]$ and $[\ell - E]$. Both are classes of curves, so $NE(S) = \overline{NE}(S) = \mathbb{R}_{\geq 0}[E] + \mathbb{R}_{\geq 0}[\ell - E]$. A class $a\ell - bE$ is nef if and only if $(a\ell - bE) \cdot E = b \geq 0$ and $(a\ell - bE) \cdot (\ell - E) = a - b \geq 0$, so $\operatorname{Nef}(S) = \mathbb{R}_{\geq 0} \ell + \mathbb{R}_{\geq 0} (\ell - E)$, and by Theorem P5.12.6 the ample classes are those with $a > b > 0$. Both boundary rays of $\overline{NE}(S)$ are $K$-negative: $K \cdot E = -1$ and $K \cdot (\ell - E) = -3 + 1 = -2$. The class $-K = 3\ell - E$ has $3 > 1 > 0$, so $-K$ is ample. The positive cone is $\{ a > |b| \}$, and it is strictly smaller than $\overline{NE}(S)$ because $E^2 = -1 < 0$.

**Example P5.12.8 (the quadric and the Hirzebruch surfaces).** On $\mathbb{P}^1 \times \mathbb{P}^1$, $\operatorname{Num} = \mathbb{Z} F_1 \oplus \mathbb{Z} F_2$ with $(aF_1 + bF_2) \cdot (cF_1 + dF_2) = ad + bc$ (Example P5.5.9). An integral curve $C$ that is not a fibre of either ruling has $C \cdot F_1 \geq 0$ and $C \cdot F_2 \geq 0$ by Proposition P5.5.5, and these are the coefficients of $F_2$ and $F_1$ in its class. So $\overline{NE} = \mathbb{R}_{\geq 0} F_1 + \mathbb{R}_{\geq 0} F_2$, and the same computation shows $\operatorname{Nef} = \overline{NE}$. The canonical class $K = -2F_1 - 2F_2$ has $K \cdot F_i = -2$.

For $n \geq 1$, the Hirzebruch surface $F_n$ has $\operatorname{Pic}(F_n) = \mathbb{Z} F \oplus \mathbb{Z} C_-$ with $C_+ \sim C_- + nF$ and $C_- \cap C_+ = \emptyset$ (Theorem P3.11.25). Two distinct fibres are disjoint, so $F^2 = 0$; the section $C_-$ meets a fibre transversally in one point, so $C_- \cdot F = 1$; and $0 = C_- \cdot C_+ = C_-^2 + n$ gives $C_-^2 = -n$. The genus formula (Theorem P5.5.14) for the smooth rational curves $F$ and $C_-$ gives $K \cdot F = -2$ and $K \cdot C_- = -2 + n$, so $K = -2C_- - (n + 2) F$. An integral curve $C \neq C_-, F$ of class $\alpha C_- + \beta F$ has $\alpha = C \cdot F \geq 0$ and $\beta - n\alpha = C \cdot C_- \geq 0$, so $\beta \geq n\alpha \geq 0$, and
$$\overline{NE}(F_n) = \mathbb{R}_{\geq 0} [C_-] + \mathbb{R}_{\geq 0} [F], \qquad \operatorname{Nef}(F_n) = \mathbb{R}_{\geq 0} [F] + \mathbb{R}_{\geq 0} [C_- + nF],$$
the second because $x = aC_- + bF$ has $x \cdot F = a$ and $x \cdot C_- = b - na$. The fibre ray is $K$-negative, and the ray of $C_-$ is $K$-negative only for $n = 1$, where $K \cdot C_- = -1$ and $F_1 \cong \operatorname{Bl}_p \mathbb{P}^2$ (Theorem P3.11.26) recovers Example P5.12.7.

**Example P5.12.9 (the round cone of $E \times E$).** Let $E$ be an elliptic curve and $S = E \times E$ (Example P5.4.9). The group law of $E$ is a morphism and its translations are automorphisms (Theorem P5.4.4), so the same holds for the group law of $S$ and its translations $t_a$, $a \in S$. Let $C$ be an integral curve. The closed subscheme $Z = \{ (a, s) : s - a \in C \} \subseteq S \times S$ is the image of $S \times C$ under the automorphism $(a, c) \mapsto (a, a + c)$, so $Z \cong S \times C$ is flat over the first factor, with fibre $t_a(C)$ over $a$. For a divisor $D$ on $S$ and a curve $\Gamma$, Definition P5.5.4 gives $D \cdot \Gamma = \chi(\mathcal{O}_\Gamma) - \chi(\mathcal{O}_\Gamma(-D))$, by the sequences $0 \to \mathcal{O}_S(-\Gamma) \to \mathcal{O}_S \to \mathcal{O}_\Gamma \to 0$ twisted by $\mathcal{O}_S(-D)$. With $\Gamma = t_a(C)$ both Euler characteristics are those of the fibres over $a$ of the sheaves $\mathcal{O}_Z$ and $\mathcal{O}_Z \otimes \operatorname{pr}_2^* \mathcal{O}_S(-D)$, flat over $S$, so they are constant in $a$ by Theorem P4.5.13. Hence $D \cdot t_a(C) = D \cdot C$ for all $a$, that is, $t_a(C) \equiv C$. If $t_a(C) = C$ for every $a$, then for a point $c \in C$ the whole of $S = \{ a + c \}$ would lie in $C$, which is absurd. So for some $a$, $t_a(C) \neq C$, and $C^2 = C \cdot t_a(C) \geq 0$ by Proposition P5.5.5. By Lemma P5.12.4 every integral curve is nef, so $NE(S) \subseteq \operatorname{Nef}(S)$, and taking closures with Lemmas P5.12.3 and P5.12.4,
$$\overline{NE}(S) = \operatorname{Nef}(S) = \overline{\mathcal{P}}(S) = \{ x : x^2 \geq 0, \ x \cdot H \geq 0 \}.$$
The fibres $f_1 = \{O\} \times E$ and $f_2 = E \times \{O\}$ and the diagonal $\Delta$, the graph of the identity, have $f_1^2 = f_2^2 = 0$ (distinct fibres are disjoint), $f_1 \cdot f_2 = 1$ (one transversal intersection point), and $\Delta \cdot f_1 = \Delta \cdot f_2 = 1$ and $\Delta^2 = 0$ by Example P5.5.19 with $g = 1$ and $d = 1$. The Gram matrix
$$\begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}$$
has determinant $2$, so $\rho(S) \geq 3$. Every ray on the boundary $\{ x^2 = 0 \}$ of $\overline{\mathcal{P}}(S)$ is extremal: if $u + v = x$ with $u, v \in \overline{\mathcal{P}}(S)$ and $x^2 = 0$, then $0 = u^2 + 2 u \cdot v + v^2$ is a sum of nonnegative terms by Lemma P5.12.3, so $u^2 = v^2 = u \cdot v = 0$; the span of $u$ and $v$ is then totally isotropic, and a form of signature $(1, \rho - 1)$ has no totally isotropic plane, so $u$ and $v$ are proportional to $x$. Since $\rho(S) \geq 3$, the cone $\{x^2 \geq 0, x \cdot H \geq 0\}$ is round and has uncountably many extremal rays, while there are only countably many classes of curves. So most extremal rays of $\overline{NE}(S)$ contain no class of a curve, and $\overline{NE}(S) \neq NE(S)$ in general. Here $K_E \sim 0$, since $\deg K_E = 0$ and $h^0(K_E) = 1$, so $K_S = p_1^* K_E + p_2^* K_E \sim 0$ by Example P5.5.19, and no ray is $K$-negative, and the cone theorem of Section 12.2 says nothing about this cone.

**Example P5.12.10 (surfaces with trivial canonical class).** Let $K_S \equiv 0$, for instance a smooth quartic surface $S \subseteq \mathbb{P}^3$, where $\omega_S \cong \mathcal{O}_S(4 - 3 - 1) = \mathcal{O}_S$ by Corollary P3.12.31. An integral curve $C$ with $C^2 < 0$ has $K \cdot C = 0$, so it is a $(-2)$-curve by Corollary P5.5.15. Every other integral curve has $C^2 \geq 0$ and $C \cdot H > 0$, so it lies in $\overline{\mathcal{P}}(S)$ by Lemma P5.12.3. Hence
$$NE(S) \subseteq \overline{\mathcal{P}}(S) + \sum_{C \text{ a } (-2)\text{-curve}} \mathbb{R}_{\geq 0} [C],$$
and $\overline{NE}(S)$ is the closure of the right side. In characteristic different from $2$, the Fermat quartic $x^4 + y^4 + z^4 + w^4 = 0$ contains the line $x = \zeta y$, $z = \zeta w$ for $\zeta^4 = -1$, since $(\zeta y)^4 + y^4 = 0$ and $(\zeta w)^4 + w^4 = 0$, and this line is a $(-2)$-curve: $L^2 = 2p_a(L) - 2 - K \cdot L = -2$ by Theorem P5.5.14. The round part and the rays of $(-2)$-curves are the shape of the cone of a K3 surface. These rays have $K \cdot C = 0$, so they are not $K$-negative.

### Proof

*Lemma P5.12.2.* (1) By Definition P3.6.22, there is $m_0$ such that $\mathcal{O}_S(D) \otimes \mathcal{O}_S(mH)$ is globally generated for $m \geq m_0$. If $\mathcal{L}$ is globally generated and $C$ is an integral curve, some section of $\mathcal{L}$ does not vanish at a chosen point of $C$, so its restriction to $C$ is a nonzero section of $\mathcal{L}|_C$, and $\deg \mathcal{L}|_C \geq 0$. By Theorem P5.5.6, $(mH + D) \cdot C \geq 0$.

(2) By Lemma P5.5.20, $H \cdot C > 0$ for every integral curve, so $H \cdot y \geq 0$ on $NE(S)$ and by continuity on $\overline{NE}(S)$. Let $y \in \overline{NE}(S)$ with $H \cdot y = 0$. For every divisor $D$, part (1) applied to $D$ and $-D$ gives $(mH \pm D) \cdot y \geq 0$ for large $m$, so $\pm D \cdot y \geq 0$ and $D \cdot y = 0$. The classes $[D]$ span $N^1(S)$ and the pairing is nondegenerate, so $y = 0$.

(3) The slice $\Sigma_H$ is closed. If it were unbounded, there would be $y_n \in \Sigma_H$ with $|y_n| \to \infty$, and a subsequence of $y_n / |y_n|$ would converge to some $y \in \overline{NE}(S)$ with $|y| = 1$ and $H \cdot y = \lim 1/|y_n| = 0$, contradicting (2). So $\Sigma_H$ is compact, and $c = \max_{\Sigma_H} |y|$ works, since every $y \neq 0$ in $\overline{NE}(S)$ is $(H \cdot y) \, y'$ with $y' \in \Sigma_H$. If $y$ and $-y$ both lie in $\overline{NE}(S)$, then $H \cdot y \geq 0$ and $-H \cdot y \geq 0$, so $y = 0$ by (2).

*Lemma P5.12.3.* (1) Let $V = \operatorname{Num}(S) \otimes \mathbb{Q}$ and $W = \{ v \in V : v \cdot H = 0 \}$, so $V = \mathbb{Q} H \oplus W$ because $H^2 > 0$. For $v \in W$, some integer multiple $nv$ is the class of a divisor orthogonal to $H$, so $v^2 \leq 0$, with equality only if $v = 0$, by Theorem P5.5.22. A quadratic form over $\mathbb{Q}$ has an orthogonal basis, so $W$ has a basis $w_2, \dots, w_\rho$ with $w_i \cdot w_j = 0$ for $i \neq j$ and $w_i^2 < 0$. Then $H, w_2, \dots, w_\rho$ is an orthogonal basis of $N^1(S)$ with one positive and $\rho - 1$ negative squares, which proves both claims, since $H^\perp \subseteq N^1(S)$ is the real span of the $w_i$.

(2) Write $x = aH + x_0$ and $y = bH + y_0$ with $x_0, y_0 \in H^\perp$, and let $q(z) = -z^2 \geq 0$ on $H^\perp$, a positive definite form by (1). For $x, y \in \mathcal{P}(S)$, $a, b > 0$, and $x^2 > 0$ reads $a \sqrt{H^2} > \sqrt{q(x_0)}$, similarly for $y$. By the Cauchy-Schwarz inequality for $q$,
$$x \cdot y = ab H^2 - q(x_0, y_0) \geq ab H^2 - \sqrt{q(x_0) q(y_0)} > 0,$$
where $q(x_0, y_0) = -x_0 \cdot y_0$ is the bilinear form of $q$. The closed case follows by continuity.

(3) The set $\{x^2 \geq 0, x \cdot H \geq 0\}$ is closed and contains $\mathcal{P}(S)$. Conversely, if $x^2 \geq 0$ and $x \cdot H \geq 0$, then for $t > 0$, $(x + tH)^2 = x^2 + 2t \, x \cdot H + t^2 H^2 > 0$ and $(x + tH) \cdot H > 0$, so $x = \lim_{t \to 0} (x + tH)$ lies in $\overline{\mathcal{P}}(S)$. Next let $x \in \mathcal{P}(S) \cap V$ be rational. Then $nx = [D]$ for a divisor $D$ and some $n \geq 1$, with $D^2 > 0$ and $D \cdot H > 0$, so by Lemma P5.5.21, $mD$ is linearly equivalent to an effective divisor $\sum a_i C_i$ for some $m \geq 1$, and $x = \frac{1}{mn} \sum a_i [C_i] \in NE(S)$. The set $\mathcal{P}(S)$ is open, so its rational points are dense in it, and $\mathcal{P}(S) \subseteq \overline{NE}(S)$; taking closures gives $\overline{\mathcal{P}}(S) \subseteq \overline{NE}(S)$. Finally if $x \neq 0$ and $x^2 \geq 0$, then $x \cdot H \neq 0$ by (1), so $x$ or $-x$ lies in $\overline{\mathcal{P}}(S)$.

(4) $\mathcal{P}(S)$ is defined by strict inequalities between continuous functions, so it is open. If $H'$ is another ample divisor and $x \in \mathcal{P}(S)$ is defined with $H$, then $x \in \overline{NE}(S) \setminus \{0\}$ by (3), so $x \cdot H' > 0$ by Lemma P5.12.2. So the positive cone for $H$ lies in that for $H'$, and by symmetry they are equal.

*Lemma P5.12.4.* Let $x$ be nef. Some multiple of $H$ is very ample, hence linearly equivalent to an effective divisor, so $[H] \in NE(S)$ and $x \cdot H \geq 0$. Suppose $x^2 < 0$ and write $x = aH + x_0$ with $x_0 \in H^\perp$ and $a = x \cdot H / H^2 \geq 0$. Then $a^2 H^2 + x_0^2 < 0$, so $x_0^2 < 0$, and $c = \sqrt{-x_0^2 / H^2}$ satisfies $c > a \geq 0$. The class $y = cH + x_0$ has $y^2 = c^2 H^2 + x_0^2 = 0$ and $y \cdot H = c H^2 > 0$, so $y \in \overline{\mathcal{P}}(S) \subseteq \overline{NE}(S)$ by Lemma P5.12.3, and
$$x \cdot y = ac H^2 + x_0^2 = ac H^2 - c^2 H^2 = c H^2 (a - c) < 0,$$
contradicting nefness. So $x^2 \geq 0$ and $x \cdot H \geq 0$, which is $x \in \overline{\mathcal{P}}(S)$ by Lemma P5.12.3. If $C$ is an integral curve with $C^2 \geq 0$, then $C \cdot C' \geq 0$ for every integral $C' \neq C$ by Proposition P5.5.5, and $C \cdot C = C^2 \geq 0$, so $C$ is nef.

*Theorem P5.12.5.* This is Hartshorne, Theorem V.1.10, and the argument is as follows. If $D$ is ample, then $D^2 > 0$ and $D \cdot C > 0$ by Lemma P5.5.20. Conversely, assume the two conditions. A multiple of an ample $H$ is linearly equivalent to an effective divisor, so $D \cdot H > 0$, and by Lemma P5.5.21 some $nD$ is linearly equivalent to an effective divisor. Since $D$ is ample if and only if $nD$ is, replace $D$ by this effective divisor and regard it as a closed subscheme of $S$ with components $C_i$. The restriction of $\mathcal{O}_S(D)$ to each $C_i$ has degree $D \cdot C_i > 0$ (Theorem P5.5.6), so it is ample on the integral curve $C_i$, and then $\mathcal{O}_D(D) = \mathcal{O}_S(D)|_D$ is ample on the scheme $D$, because ampleness may be tested on the reduced subscheme and on its irreducible components (Hartshorne, Exercise III.5.7). The sequence $0 \to \mathcal{O}_S((m - 1)D) \to \mathcal{O}_S(mD) \to \mathcal{O}_D(mD) \to 0$ and Theorem P4.2.10 give $H^1(\mathcal{O}_D(mD)) = 0$ for large $m$, so $h^1(\mathcal{O}_S(mD)) \leq h^1(\mathcal{O}_S((m - 1)D))$; these numbers are eventually constant, so $H^1(\mathcal{O}_S((m - 1)D)) \to H^1(\mathcal{O}_S(mD))$ is eventually an isomorphism and $H^0(\mathcal{O}_S(mD)) \to H^0(\mathcal{O}_D(mD))$ is eventually surjective. For large $m$, $\mathcal{O}_D(mD)$ is globally generated, so the sections of $\mathcal{O}_S(mD)$ generate it at every point of $D$, and the $m$-th power of the section defining $D$ generates it off $D$. So $|mD|$ is base point free and defines a morphism $\varphi \colon S \to \mathbb{P}^N$ with $\varphi^* \mathcal{O}(1) \cong \mathcal{O}_S(mD)$ (Theorem P3.6.21). A positive-dimensional fibre of $\varphi$ would contain an integral curve $C$ with $mD \cdot C = \deg \varphi^* \mathcal{O}(1)|_C = 0$, which is excluded. So $\varphi$ is finite by Corollary P4.6.17, and $\mathcal{O}_S(mD) = \varphi^* \mathcal{O}(1)$ is ample by Corollary P4.2.11.

*Theorem P5.12.6.* (1) If $D$ is ample, use Lemma P5.12.2. Conversely, if $D$ is positive on $\overline{NE}(S) \setminus \{0\}$, then $D \cdot C > 0$ for every integral curve, so $D$ is nef and $D^2 \geq 0$ by Lemma P5.12.4. If $D^2 = 0$, then $[D] \neq 0$ (since $D \cdot H > 0$) lies in $\overline{\mathcal{P}}(S) \subseteq \overline{NE}(S)$, and $D \cdot [D] = 0$ contradicts the hypothesis. So $D^2 > 0$ and $D$ is ample by Theorem P5.12.5.

(2) Let $A = \{ x : x \cdot y > 0 \text{ for } y \in \overline{NE}(S) \setminus \{0\} \} = \{ x : x \cdot y > 0 \text{ for } y \in \Sigma_H \}$. Since $\Sigma_H$ is compact, $x \mapsto \min_{\Sigma_H} x \cdot y$ is continuous, so $A$ is open, and $A \subseteq \operatorname{Nef}(S)$ gives $A \subseteq \operatorname{int} \operatorname{Nef}(S)$. If $x$ is an interior point of $\operatorname{Nef}(S)$, then $x - \varepsilon H$ is nef for small $\varepsilon > 0$, and $x \cdot y \geq \varepsilon H \cdot y > 0$ on $\overline{NE}(S) \setminus \{0\}$, so $x \in A$. Thus $A = \operatorname{int} \operatorname{Nef}(S)$. By Lemma P5.12.2 every ample class lies in $A$, and $A$ is a convex cone, so $\operatorname{Amp}(S) \subseteq A$. Conversely, a rational point $x \in A$ has a multiple $nx = [D]$ with $D$ ample by (1). For an arbitrary $x \in A$, choose a simplex with rational vertices in the open set $A$ containing $x$; then $x$ is a positive combination of rational points of $A$, hence of ample classes, and $x \in \operatorname{Amp}(S)$. For $x$ nef and $t > 0$, $x + tH$ is positive on $\overline{NE}(S) \setminus \{0\}$, so $x = \lim (x + tH)$ lies in the closure of $A$, while $\operatorname{Nef}(S)$ is closed. So $\operatorname{Nef}(S) = \overline{\operatorname{Amp}(S)}$.

(3) Every $y \in \overline{NE}(S)$ pairs nonnegatively with $\operatorname{Nef}(S)$ by definition. Let $y \notin \overline{NE}(S)$. Fix a Euclidean inner product $\langle \, , \rangle$ on $N^1(S)$, and let $p$ be the point of the closed cone $\overline{NE}(S)$ nearest to $y$. For $z \in \overline{NE}(S)$ and $t \geq 0$, the points $p + tz$ and $tp$ lie in $\overline{NE}(S)$, and minimality at $t = 0$ gives $\langle p - y, z \rangle \geq 0$ and $\langle p - y, p \rangle = 0$. Then $\langle p - y, y \rangle = -|p - y|^2 < 0$. By nondegeneracy, the linear form $\langle p - y, - \rangle$ is $x \cdot (-)$ for some $x \in N^1(S)$. This $x$ is nonnegative on $\overline{NE}(S)$, so it is nef, and $x \cdot y < 0$. So $y$ is not in the dual of $\operatorname{Nef}(S)$.

### Exercises

1. (A) On $\mathbb{P}^1 \times \mathbb{P}^1$, show that $aF_1 + bF_2$ is ample if and only if $a > 0$ and $b > 0$, and check the two conditions of Theorem P5.12.5 for $F_1 + F_2$ directly.
2. (A) On $F_n$, show that $-K = 2C_- + (n + 2) F$ is ample if and only if $n \leq 1$, and that for $n = 2$ it is nef but not ample.
3. (B) Show that if $\rho(S) = 2$, then $\overline{NE}(S)$ is spanned by two rays, and that a boundary ray of negative square is spanned by the class of an integral curve.
4. (B) Let $D$ be a divisor with $D^2 > 0$. Show that $[D]$ or $-[D]$ is an interior point of $\overline{NE}(S)$, and deduce that $nD$ or $-nD$ is effective up to linear equivalence for large $n$.
5. (B) Show that $x \cdot y \geq \sqrt{x^2 \, y^2}$ for $x, y \in \overline{\mathcal{P}}(S)$, with equality for $x, y \in \mathcal{P}(S)$ only if $x$ and $y$ are proportional.
6. (C) On $S = E \times E$, assume $\rho(S) = 3$, so that $f_1, f_2, \Delta$ span $N^1(S)$. Show that $f_1 + f_2$ is ample, and that $af_1 + bf_2 + c\Delta$ is ample if and only if $ab + bc + ca > 0$ and $a + b + 2c > 0$.

### Lean

Mathlib has convex cones in real vector spaces (`ConvexCone`, `PointedCone`) and extreme points of a set (`Set.extremePoints`), which are the linear algebra of this section. It has no intersection pairing on a surface, no Néron-Severi group, and no cone of curves, so none of the statements above can be formulated there yet. The handbook adds no `MinimalModel` node here.

### Notes and history

The criterion of Theorem P5.12.5 is due to Nakai (1963) and Moishezon (1964) in all dimensions, and Hartshorne, Theorem V.1.10, is the proof given here. Kleiman's criterion and the duality of the nef cone and the closed cone of curves are from Kleiman's 1966 paper *Toward a numerical theory of ampleness*, which also proves the theorem of the base used to define $\rho(S)$; Lazarsfeld, *Positivity I*, Section 1.4, is the modern account. The literature state is theorem. Example P5.12.9 is the first case where $\overline{NE}(S)$ is not polyhedral and is not generated by curves, and Example P5.12.10 shows the K3 shape of a round cone with $(-2)$-rays; neither is visible to the cone theorem, which only describes the $K$-negative side. In the minimal model program, Theorem P5.12.6 is the reason that a contraction can be built from a nef divisor vanishing on exactly one extremal ray, the route taken by the basepoint-free theorem of Volume 2.
