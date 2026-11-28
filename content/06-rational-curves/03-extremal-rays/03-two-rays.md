---
title: Fibre type rays and Fano manifolds of Picard number two
nodes: []
sources: [Wis91, MM81, Kol96, Deb01, KM98]
reads_with: [Wis91:all, Deb01:ch5, Kol96:IV.2]
requires: [P7.3, P7.4, P8.3, 6.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Fibre type rays and Fano manifolds of Picard number two

### Statement

Let $X$ be a smooth projective variety of dimension $n$, with the conventions of Section 1. A contraction $\varphi \colon X \to Y$ of an extremal ray is *of fibre type* if $\dim Y < n$.

**Proposition 6.3.15 (rational curves in a fibre type ray).** Let $k$ have characteristic $0$, $R$ a $K_X$-negative extremal ray with a contraction $\varphi \colon X \to Y$ of fibre type, and $x \in X$ a general point. There is a rational curve $\Gamma$ through $x$ with $[\Gamma] \in R$ and $-K_X \cdot \Gamma \le 2n$. In particular $X$ is uniruled, and some family of rational curves with class in $R$ is dominating.

Lean: not yet in Lean.

**Proposition 6.3.16 (two fibre type rays).** Let $R_1 \ne R_2$ be $K_X$-negative extremal rays with contractions $\varphi_1$, $\varphi_2$, and suppose that for $i = 1, 2$ there is a dominating family $V_i$ of rational curves with $[V_i] \in R_i$ and $-K_X \cdot V_i = \ell(R_i)$. Then
$$\ell(R_1) + \ell(R_2) \le n + 2.$$

Lean: not yet in Lean.

**Proposition 6.3.17 (Fano manifolds of Picard number two).** Let $X$ be a Fano manifold with $\rho(X) = 2$. Then $\overline{NE}(X) = R_1 + R_2$ for exactly two extremal rays, both $K_X$-negative and spanned by rational curves $\Gamma_i$ with $-K_X \cdot \Gamma_i \le n + 1$, and $\operatorname{Nef}(X) = \langle L_1, L_2 \rangle$ for nef Cartier divisors $L_i$ with $L_i^\perp \cap \overline{NE}(X) = R_i$.

Lean: not yet in Lean.

### Proof in words

For a fibre type ray, take a curve through a general point inside its fibre and apply the theorem of Miyaoka and Mori with the ample class $-K_X + mL$, where $L$ is the pullback of an ample class from $Y$. The degree bound does not see $L$ on the fibre, so for $m$ large the rational curve it produces has degree $0$ against $L$ and is contracted: it lies in $R$. For two fibre type rays with dominating minimal families, the loci of the curves of the two families through a general point $x$ lie in the two fibres through $x$, which meet in finitely many points because no curve is contracted by both maps. By Corollary 6.3.2 the loci have dimensions at least $\ell(R_i) - 1$, and two subvarieties through a point of a smooth variety that meet in a finite set have dimensions adding to at most $n$. For $\rho = 2$ the cone of a Fano manifold is a two-dimensional polyhedral cone, so it has two rays, and the supporting divisors of Corollary 6.2.11 span the dual cone.

### Examples

**Example 6.3.18 (products of projective spaces).** On $\mathbb{P}^a \times \mathbb{P}^b$ the two rays have lengths $a + 1$ and $b + 1$, both of fibre type, with dominating families of lines in the two factors. Then $\ell(R_1) + \ell(R_2) = a + b + 2 = n + 2$, so Proposition 6.3.16 is sharp. For $\mathbb{P}^1 \times \mathbb{P}^2$ the lengths are $2$ and $3$, of types C2 and D3 in Theorem 6.3.9.

**Example 6.3.19 (the blow-up of $\mathbb{P}^3$ at a point).** By Proposition 6.2.17, $\operatorname{Bl}_p \mathbb{P}^3$ is Fano with $\rho = 2$, with a ray of type E2, of length $2$, and a ray of type C2, of length $2$, the $\mathbb{P}^1$-bundle over $\mathbb{P}^2$. Only one ray is of fibre type, so Proposition 6.3.16 does not apply.

**Example 6.3.20 (the blow-up of $\mathbb{P}^3$ along a line).** Let $X = \operatorname{Bl}_C \mathbb{P}^3$ for a line $C$, with $H$ the pullback of a plane and $E$ the exceptional divisor, so $-K_X = 4H - E$. One ray is spanned by a fibre $f$ of $E \to C$, with $-K_X \cdot f = 1$: type E1. The projection from $C$ is a morphism $X \to \mathbb{P}^1$ whose fibres are the planes through $C$, so the other ray is spanned by a line $m$ in such a plane, meeting $C$ once: $-K_X \cdot m = 4 - 1 = 3$, type D3. Since $\rho(X) = 2$ and $-K_X$ is positive on both rays, $-K_X$ is ample by Theorem P7.3.13, and $X$ is Fano.

**Example 6.3.21 (the flag threefold).** Let $W \subseteq \mathbb{P}^2 \times \mathbb{P}^2$ be the divisor of bidegree $(1, 1)$ given by $\sum_i x_i y_i = 0$, the variety of pairs (point, line through it), which is $\mathbb{P}(T_{\mathbb{P}^2})$. Then $-K_W = 2 H_1 + 2 H_2$ by adjunction, both projections are $\mathbb{P}^1$-bundles, of type C2, and their fibres are lines with $-K_W \cdot f = 2$. So $\ell(R_1) + \ell(R_2) = 4 < 5 = n + 2$.

### Proof

*Proposition 6.3.15.* Let $L$ be the pullback of an ample Cartier divisor on $Y$, so $L$ is nef with $L^\perp \cap \overline{NE}(X) = R$. On the compact slice $\Sigma$ of Corollary P7.3.14, $L \ge 0$ with $L = 0$ exactly on $R \cap \Sigma$, where $-K_X > 0$. By compactness there is an integer $m_0$ with $-K_X + m L > 0$ on $\Sigma$ for $m \ge m_0$, and then $H_m = -K_X + m L$ is ample by Theorem P7.3.13. Fix $m = m_0 + 2n + 1$, and let $x$ be a general point and $F$ the fibre of $\varphi$ through $x$, of positive dimension since $\varphi$ is of fibre type; choose an integral curve $C \subseteq F$ through $x$. Then $[C] \in R$, so $K_X \cdot C < 0$ and $L \cdot C = 0$, and $X$ is smooth along $C$. By Theorem P8.3.6 there is a rational curve $\Gamma$ through $x$ with
$$H_{m_0} \cdot \Gamma + (m - m_0) L \cdot \Gamma = H_m \cdot \Gamma \le \frac{2n \, H_m \cdot C}{-K_X \cdot C} = 2n.$$
Since $H_{m_0}$ is ample, $H_{m_0} \cdot \Gamma > 0$, so $(2n + 1) L \cdot \Gamma < 2n$, and the nonnegative integer $L \cdot \Gamma$ is $0$. So $[\Gamma] \in R$ and $-K_X \cdot \Gamma = H_m \cdot \Gamma \le 2n$. By the last statement of Theorem P8.3.6, $X$ is uniruled. The rational curves of class in $R$ through general points come from countably many families, the components of $\operatorname{Hom}(\mathbb{P}^1, X)$, and the general points of $X$ are not covered by countably many proper closed subsets when $k$ is uncountable (Lemma P8.3.2); so one family is dominating. Over a countable field the statement follows by base change to an uncountable algebraically closed field, since the components of the Hom scheme and their loci are defined over $k$.

*Proposition 6.3.16.* Let $x$ be a general point, so that $x \in \operatorname{ev}_0(V_1) \cap \operatorname{ev}_0(V_2)$, each $\operatorname{ev}_0(V_i)$ containing a dense open subset of $X$. By Lemma 6.1.6, $V_i$ is unsplit, and by Corollary 6.3.2, $Z_i = \operatorname{Locus}((V_i)_x)$ has dimension at least $\ell(R_i) - 1$. The members of $(V_i)_x$ have class in $R_i$, so they are contracted by $\varphi_i$, and $Z_i \subseteq F_i$, the fibre of $\varphi_i$ through $x$. A curve $C \subseteq F_1 \cap F_2$ would have $[C] \in R_1 \cap R_2 = \{0\}$, which is impossible, so $Z_1 \cap Z_2$ is finite, and it contains $x$. Since $X$ is smooth, $Z_1 \cap Z_2$ is the intersection of $Z_1 \times Z_2$ with the diagonal $\Delta \subseteq X \times X$, and near $(x, x)$ the diagonal is cut out by $n$ equations, so every irreducible component of $Z_1 \cap Z_2$ through $x$ has dimension at least $\dim Z_1 + \dim Z_2 - n$ by Krull's height theorem. Hence $\dim Z_1 + \dim Z_2 \le n$, and $\ell(R_1) - 1 + \ell(R_2) - 1 \le n$.

*Proposition 6.3.17.* By Corollary 6.2.12, $\overline{NE}(X)$ is a rational polyhedral cone, spanned by classes of rational curves with $-K_X \cdot \Gamma \le n + 1$. It is salient by Corollary P7.3.14, and it spans $N_1(X)$, of dimension $2$, since $N_1(X)$ is spanned by classes of curves. A salient polyhedral cone of dimension $2$ has exactly two extremal rays $R_1$, $R_2$ and is their sum (part 2 of Proposition P7.4.4). Both are $K_X$-negative since $-K_X$ is ample. Corollary 6.2.11 gives nef Cartier divisors $L_i$ with $L_i^\perp \cap \overline{NE}(X) = R_i$. The dual of $R_1 + R_2$ is spanned by the two functionals that vanish on $R_2$ and on $R_1$ respectively and are nonnegative on the cone, which are positive multiples of $L_2$ and $L_1$. So $\operatorname{Nef}(X) = \overline{NE}(X)^\vee = \langle L_1, L_2 \rangle$.

### Exercises

1. (A) For $W$ of Example 6.3.21, find $L_1$, $L_2$ of Proposition 6.3.17, and check that $W \to \mathbb{P}^2$ by either projection has fibres $\mathbb{P}^1$.
2. (A) Check that $\operatorname{Bl}_C \mathbb{P}^3$ of Example 6.3.20 has $\rho = 2$, and compute the intersection numbers $H^3$, $H^2 E$, $H E^2$, $E^3$.
3. (B) Show that the hypothesis $-K_X \cdot V_i = \ell(R_i)$ in Proposition 6.3.16 cannot be dropped from the proof, by finding the step that uses unsplitness.
4. (B) Let $X$ be a smooth projective variety with two distinct extremal rays of fibre type, with contractions $\varphi_i \colon X \to Y_i$. Show that the fibres of $\varphi_1$ and $\varphi_2$ through a general point meet in a finite set, and deduce $\dim Y_1 + \dim Y_2 \ge n$. Check the case of equality on $\mathbb{P}^a \times \mathbb{P}^b$.
5. (B) Let $X = \mathbb{P}_{\mathbb{P}^1}(\mathcal{O} \oplus \mathcal{O}(1) \oplus \mathcal{O}(1))$. Show that $X \cong \operatorname{Bl}_C \mathbb{P}^3$ for a line $C$, and identify the two rays of Example 6.3.20 in this description.
6. (B) Let $X$ be a Fano manifold with $\rho(X) = 2$ whose two contractions are both $\mathbb{P}^1$-bundles over smooth varieties of dimension $n - 1$. Show that $\ell(R_1) = \ell(R_2) = 2$ and $4 \le n + 2$, and that $W$ of Example 6.3.21 is an example for $n = 3$.

### Lean

Nothing in this section is in Lean. The library has `MinimalModel.ExtremalRay`, `MinimalModel.KleimanCriterion` and `MinimalModel.ContractionTheorem`, but no families of rational curves and no Fano manifolds of given Picard number.

### Notes and history

Proposition 6.3.16 is in the circle of results of Wiśniewski (Wis91) and of Kol96, Section IV.2. Mori and Mukai classified the Fano threefolds with $\rho \ge 2$ (MM81), using the contractions of Theorem 6.3.9 on each ray. Proposition 6.3.15 is the input to Section 3 of Chapter 4, where the general fibre of a fibre type contraction is shown to be Fano and rationally connected.
