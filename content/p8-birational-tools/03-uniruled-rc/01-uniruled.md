---
title: Uniruled varieties
nodes: []
sources: [Kol96, Deb01, KM98, MM86, BDPP13, Shi74, Har77]
reads_with: [Deb01:4.1, Kol96:IV.1]
requires: [P1.4, P3.7, P3.12, P4.5, P5.2, P5.4, P7.2, P7.4, P8.1, P8.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Uniruled varieties

### Statement

In this section $k$ is algebraically closed and $X$ is a projective variety of dimension $n \geq 1$ over $k$. A *family of rational curves* on $X$ is a variety $M$ with a morphism $F \colon \mathbb{P}^1 \times M \to X$; its members are the morphisms $f_m = F|_{\mathbb{P}^1 \times \{m\}}$.

**Definition P8.3.1 (uniruled).** The variety $X$ is *uniruled* if there is a family of rational curves $F \colon \mathbb{P}^1 \times M \to X$ that is dominant and has some member $f_m$ nonconstant.

**Lemma P8.3.2 (countable unions).** Let $k$ be uncountable and $W$ a variety over $k$. Then the set of closed points of $W$ is not contained in a countable union of proper closed subsets of $W$.

Lean: not in Lean as stated.

**Lemma P8.3.3 (surjective differentials).** Let $\varphi \colon V \to W$ be a morphism of varieties and $v \in V$ a closed point at which $V$ is smooth and $d\varphi_v \colon T_v V \to T_{\varphi(v)} W$ is surjective. Then $\varphi$ is dominant.

Lean: not in Lean as stated.

**Theorem P8.3.4 (uniruled varieties and rational curves).**

1. If $X$ is uniruled and $F \colon \mathbb{P}^1 \times M \to X$ is as in Definition P8.3.1, then every member $f_m$ is nonconstant, and through every closed point of $X$ there is a rational curve.
2. Let $k$ be uncountable, and suppose that the closed points of $X$ lying on rational curves are not contained in a countable union of proper closed subsets; for instance, that every closed point lies on a rational curve. Then $X$ is uniruled.
3. Let $X$ be smooth, $f \colon \mathbb{P}^1 \to X$ a free rational curve and $H_0$ the irreducible component of $\operatorname{Hom}(\mathbb{P}^1, X)$ through $[f]$, with its reduced structure. Then $\operatorname{ev} \colon \mathbb{P}^1 \times H_0 \to X$ is dominant, and $X$ is uniruled.
4. Let $k$ have characteristic $0$ and $X$ be smooth and uniruled. Then there is a dense open subset $U \subseteq X$ such that through every closed point of $U$ there is a free rational curve.

Lean: not in Lean as stated.

**Corollary P8.3.5 (uniruled varieties in characteristic $0$).** Let $k$ have characteristic $0$ and $X$ be smooth and uniruled. Then $K_X$ is not pseudo-effective, and $H^0(X, \omega_X^{\otimes m}) = 0$ for every $m \geq 1$.

Lean: not in Lean as stated.

**Theorem P8.3.6 (Miyaoka and Mori, cited).** Let $k$ have characteristic $0$, $X$ a projective variety of dimension $n$, $H$ an ample divisor and $x \in X$ a general point. Let $C \subseteq X$ be a curve through $x$ along which $X$ is smooth, with $K_X \cdot C < 0$. Then there is a rational curve $\Gamma$ through $x$ with
$$H \cdot \Gamma \leq \frac{2 n \, H \cdot C}{-K_X \cdot C}.$$
In particular, if through a general point of $X$ there is such a curve, then $X$ is uniruled.

Lean: not in Lean as stated.

**Theorem P8.3.7 (Boucksom, Demailly, Păun and Peternell, cited).** Let $X$ be a smooth projective variety over $\mathbb{C}$. Then $X$ is uniruled if and only if $K_X$ is not pseudo-effective.

Lean: not in Lean as stated.

**Example P8.3.8 (hypersurfaces of low degree).** Let $X \subseteq \mathbb{P}^N$ be a hypersurface of degree $d \leq N - 1$, with $N \geq 2$. Then through every point $x \in X$ there is a line contained in $X$. So $X$ is uniruled when $k$ is uncountable, by part 2 of Theorem P8.3.4; the family of all lines on $X$ gives the same conclusion over any $k$ (Exercise 2). If $X$ is smooth, $K_X = (d - N - 1) H|_X$ by adjunction, and a line $L \subseteq X$ has $-K_X \cdot L = N + 1 - d \geq 2$.

**Example P8.3.9 (a product with the line).** Let $C$ be a smooth projective curve of genus $g \geq 1$ and $X = C \times \mathbb{P}^1$. The family $F = \mathrm{id} \colon \mathbb{P}^1 \times C \to X$, with the factors swapped, shows that $X$ is uniruled. The rational curves on $X$ are exactly the fibres $\{c\} \times \mathbb{P}^1$: a nonconstant morphism $\mathbb{P}^1 \to C$ would make $C$ a curve dominated by $\mathbb{P}^1$, hence $C \cong \mathbb{P}^1$ by Theorem P5.2.12, so every rational curve maps to a point of $C$.

**Example P8.3.10 (varieties that are not uniruled).** Let $k$ have characteristic $0$ and $X$ smooth with $K_X$ nef, for example an abelian variety, a K3 surface, or a smooth hypersurface of degree $d \geq N + 1$ in $\mathbb{P}^N$. Then $X$ is not uniruled: a nef divisor is pseudo-effective by part 1 of Proposition P7.4.15, so Corollary P8.3.5 applies. In characteristic $p$ this fails. Shioda showed that the Fermat surface $x_0^{p+1} + x_1^{p+1} + x_2^{p+1} + x_3^{p+1} = 0$ in characteristic $p$ is unirational, hence uniruled, for every prime $p$ (Shi74), and for $p \geq 3$ its canonical class $(p - 3) H$ is nef, and ample for $p \geq 5$.

### Proof in words

A family of rational curves that dominates $X$ gives rational curves through a dense set of points. To reach every point, take a curve through the point meeting that dense set, lift it to the family, and take the limit of the rational curves along the lifted curve, as in Lemma P8.2.4: the limit is a connected union of rational curves through the point. Conversely, the scheme of morphisms $\mathbb{P}^1 \to X$ has only countably many components, so if rational curves pass through more points than countably many proper closed subsets can hold, the evaluation map of one component is dominant.

A free curve deforms in every direction: the differential of the evaluation map at it is surjective, so the evaluation map is dominant by a dimension count. In characteristic $0$ the converse holds at general points by generic smoothness, which makes the evaluation map smooth over an open set, and smoothness at $(p, [f])$ means that the sections of $f^* T_X$ generate its fibre at $p$, which forces every summand of $f^* T_X$ to have nonnegative degree. Free curves through general points have $-K_X \cdot f_* \mathbb{P}^1 > 0$, so they make $K_X$ negative on a covering family of curves, and pluricanonical forms restrict to zero on them.

### Examples

*Example P8.3.8.* Choose coordinates with $x = [1 : 0 : \dots : 0]$, and write the equation of $X$ in the affine chart $x_0 = 1$ as $G = G_1 + \dots + G_d$, with $G_i$ homogeneous of degree $i$ in $x_1, \dots, x_N$ and $G_0 = 0$ since $x \in X$. The line through $x$ in direction $v \in k^N \setminus \{0\}$ is $\{x + \lambda v\}$, and $G(\lambda v) = \sum_i \lambda^i G_i(v)$ vanishes identically exactly when $G_1(v) = \dots = G_d(v) = 0$. These are $d \leq N - 1$ homogeneous equations on $\mathbb{P}^{N-1}$, so by part 4 of Proposition P3.7.5 they have a common zero, a line through $x$ in $X$. The canonical class is computed from $K_{\mathbb{P}^N} = -(N + 1) H$ and the adjunction formula $K_X = (K_{\mathbb{P}^N} + X)|_X$.

*Example P8.3.10.* For an abelian variety or a K3 surface, $\omega_X \cong \mathcal{O}_X$ has a nonzero section, which also contradicts the second conclusion of Corollary P8.3.5 directly. For a smooth hypersurface of degree $d \geq N + 1$, $K_X = (d - N - 1) H|_X$ is nef. The Fermat surface is smooth when $p \nmid p + 1$, which always holds.

### Proof

*Lemma P8.3.2.* Let $Z_1, Z_2, \dots$ be proper closed subsets. Replacing $W$ by a nonempty affine open subset $W_0 = \operatorname{Spec} A$ and $Z_i$ by $Z_i \cap W_0$, which is still proper because $W$ is irreducible, assume $W$ affine of dimension $d$. By Theorem P1.4.27 there is a finite injective map $k[y_1, \dots, y_d] \to A$, so a finite morphism $\phi \colon W \to \mathbb{A}^d$, which is surjective by Theorem P1.4.12. Each $\phi(Z_i)$ is closed, by Theorem P1.4.13, and of dimension at most $\dim Z_i < d$ by Corollary P1.4.14, so it is a proper closed subset. If the closed points of $W$ lay in $\bigcup_i Z_i$, the closed points of $\mathbb{A}^d$ would lie in $\bigcup_i \phi(Z_i)$. So it suffices to treat $W = \mathbb{A}^d$, by induction on $d$. For $d = 0$ the only proper closed subset is empty. Let $d \geq 1$ and choose nonzero $g_i \in k[y_1, \dots, y_d]$ with $Z_i \subseteq V(g_i)$. The hyperplane $V(y_1 - a)$ lies in $V(g_i)$ only if $y_1 - a$ divides $g_i$, which happens for finitely many $a \in k$. Since $k$ is uncountable, there is $a \in k$ with $V(y_1 - a) \not\subseteq V(g_i)$ for all $i$. Then $V(y_1 - a) \cong \mathbb{A}^{d-1}$, the sets $V(g_i) \cap V(y_1 - a)$ are proper closed subsets of it, and by induction they do not contain all its closed points.

*Lemma P8.3.3.* Let $w = \varphi(v)$, $Y$ the closure of $\varphi(V)$, an irreducible closed subset of $W$, and $\Phi = \varphi^{-1}(w)$ the fibre, a closed subscheme of $V$. By Proposition P3.7.13, a tangent vector of $\Phi$ at $v$ is a morphism $\operatorname{Spec} k[\varepsilon] \to V$ at $v$ whose composite with $\varphi$ is the constant morphism at $w$, so $T_v \Phi = \ker d\varphi_v$, of dimension $\dim T_v V - \dim T_w W$. Since $V$ is smooth at $v$, $\dim T_v V = \dim V$, and by part 1 of Proposition P3.7.15, $\dim_v \Phi \leq \dim T_v \Phi = \dim V - \dim T_w W \leq \dim V - \dim W$, using part 1 of Proposition P3.7.15 again for $W$ at $w$. On the other hand, by part 2 of Theorem P3.7.6 applied to the dominant morphism $V \to Y$ of integral schemes, with $Y$ reduced, every irreducible component of $\Phi$ has dimension at least $\dim V - \dim Y$. So $\dim V - \dim Y \leq \dim V - \dim W$, that is, $\dim Y \geq \dim W$, and $Y = W$ because $W$ is irreducible.

*Theorem P8.3.4.* (1) Let $M_c \subseteq M$ be the set of $m$ with $f_m$ constant. By part 1 of Lemma P8.2.1, $M_c$ is open. The scheme $\mathbb{P}^1 \times M$ is a variety, so if $M_c$ were nonempty, part 2 of Lemma P8.2.1 would make every $f_m$ constant, contrary to the hypothesis. So $M_c$ is empty.

Let $x \in X$ be a closed point. The image of $F$ is dense; by Lemma P8.2.2 applied to $W = X$, with $U$ a dense open subset of $X$ contained in $F(\mathbb{P}^1 \times M)$, which exists because the image is constructible (Hartshorne, Exercise II.3.19 (Har77)), there is a curve $T \subseteq X$ through $x$ that meets $U$. Some irreducible component $W_1$ of $F^{-1}(T)$ maps onto a dense subset of $T$, since $T \cap U \subseteq F(F^{-1}(T))$. Let $x_1 \in F(W_1)$ be a closed point, $w_1 \in W_1$ over it, and apply Lemma P8.2.2 to $W_1$, $w_1$ and the open set $W_1 \setminus F^{-1}(x_1)$, which is nonempty because $F(W_1)$ is dense in the curve $T$: this gives a curve $D \subseteq W_1$ with $F(D)$ dense in $T$. If $p_2(D)$ is a point $m$, then $F(\mathbb{P}^1 \times \{m\})$ is a closed irreducible curve containing $F(D)$, hence equal to $T$, and $T$ is a rational curve through $x$. Otherwise, let $\widetilde D \to D$ be the normalization, $\bar D$ its smooth completion, $\widetilde D^\circ \subseteq \widetilde D$ a nonempty open subset, and
$$G \colon \mathbb{P}^1 \times \widetilde D^\circ \to X, \qquad (s, e) \mapsto F(s, p_2(e)).$$
Let $\sigma \colon \widetilde D \to \mathbb{P}^1$ be the composite with $p_1$, so that $G(\sigma(e), e) = F(e) \in T$. Apply Lemma P8.2.4 to $G$, with $S = \mathbb{P}^1 \times \bar D$, $\pi \colon S' \to S$ and $G' \colon S' \to X$. The closure $\Sigma$ of the graph of $\sigma$ in $S$ is a curve with $G(\Sigma) \supseteq F(D)$ dense in $T$, and its strict transform $\Sigma'$ in $S'$ satisfies $G'(\Sigma') = T \ni x$. Let $y \in \Sigma'$ with $G'(y) = x$, and $t = q(y)$. By Lemma P8.2.4, the fibre $S'_t$ is a connected union of curves isomorphic to $\mathbb{P}^1$, and $G'_*(S'_t) \equiv G_{e *} \mathbb{P}^1 \neq 0$ for $e \in \widetilde D^\circ$, so some component of $S'_t$ is not contracted by $G'$. As in the proof of Theorem P8.2.5, connectedness shows that every point of $G'(S'_t)$, in particular $x$, lies on the image of a component not contracted by $G'$, which is a rational curve.

(2) By Theorem P8.1.4, $\operatorname{Hom}(\mathbb{P}^1, X)$ is a disjoint union of countably many quasi-projective schemes, so it has countably many irreducible components $H_1, H_2, \dots$, which are varieties with their reduced structures. By Proposition P8.1.6, $H_i$ consists of constant morphisms or of nonconstant ones; let $H_1, H_2, \dots$ now denote the components of the second kind, and $V_i$ the closure of $\operatorname{ev}(\mathbb{P}^1 \times H_i)$. Every closed point lying on a rational curve lies on the image of the normalization $\mathbb{P}^1 \to X$ of that curve, so in some $V_i$. By hypothesis and Lemma P8.3.2, some $V_i$ equals $X$. Then $\operatorname{ev} \colon \mathbb{P}^1 \times H_i \to X$ is a dominant family of rational curves with nonconstant members.

(3) By Corollary P8.1.13, $\operatorname{Hom}(\mathbb{P}^1, X)$ is smooth at $[f]$, so near $[f]$ it equals $H_0$ and $T_{[f]} H_0 = H^0(\mathbb{P}^1, f^* T_X)$ by Theorem P8.1.9. By Exercise 6 of Section 1.2, the differential of $\operatorname{ev}$ at $(p, [f])$ is $(v, s) \mapsto df_p(v) + s(p)$, and it is surjective because $f^* T_X \cong \bigoplus_i \mathcal{O}(a_i)$ with all $a_i \geq 0$ is generated by global sections. The variety $\mathbb{P}^1 \times H_0$ is smooth at $(p, [f])$ and $X$ is smooth, so Lemma P8.3.3 shows that $\operatorname{ev}$ is dominant. Its members are nonconstant, since $f$ is.

(4) Let $F \colon \mathbb{P}^1 \times M \to X$ be as in Definition P8.3.1. By Theorem P3.12.12, replace $M$ by its smooth locus, a dense open subset, so that $\mathbb{P}^1 \times M$ is smooth by Proposition P3.12.23; $F$ is still dominant. By generic smoothness in characteristic $0$ (Hartshorne, Corollary III.10.7 (Har77)) there is a dense open $U \subseteq X$ over which $F$ is smooth, and replacing $U$ by $U \cap F(\mathbb{P}^1 \times M)$, which contains a dense open subset by the constructibility used in part 1, assume $U \subseteq F(\mathbb{P}^1 \times M)$. Let $x \in U$, $(p, m) \in F^{-1}(x)$ and $f = f_m$. Since $F$ is smooth at $(p, m)$, the differential $dF_{(p, m)} \colon T_p \mathbb{P}^1 \oplus T_m M \to T_x X$ is surjective (Har77, Proposition III.10.4). The family $F$ defines a morphism $\kappa \colon M \to \operatorname{Hom}(\mathbb{P}^1, X)$ with $F = \operatorname{ev} \circ (\mathrm{id} \times \kappa)$, so $dF_{(p, m)}(v, w) = df_p(v) + (d\kappa_m w)(p)$, with $d\kappa_m w \in H^0(\mathbb{P}^1, f^* T_X)$ by Theorem P8.1.9. The vector $df_p(v)$ is also the value at $p$ of a global section of $f^* T_X$, the image of a section of $T_{\mathbb{P}^1}$ under $df$, since $T_{\mathbb{P}^1} \cong \mathcal{O}(2)$ is generated by global sections. Hence the evaluation map $H^0(\mathbb{P}^1, f^* T_X) \to f^* T_X \otimes \kappa(p)$ is surjective. Write $f^* T_X \cong \bigoplus_i \mathcal{O}(a_i)$ by Theorem P5.4.10. A summand $\mathcal{O}(a_i)$ with $a_i < 0$ has no sections, so its fibre at $p$ would not be reached. So every $a_i \geq 0$ and $f$ is free, in the sense of Definition P5.4.12, through $x = f(p)$.

*Corollary P8.3.5.* By part 4 of Theorem P8.3.4, there is a free curve $f \colon \mathbb{P}^1 \to X$, and by part 3 the evaluation map of the component $H_0$ through $[f]$ is dominant. Write $f^* T_X \cong \bigoplus_i \mathcal{O}(a_i)$ with $a_i \geq 0$. The differential $df \colon T_{\mathbb{P}^1} = \mathcal{O}(2) \to f^* T_X$ is nonzero, because $f$ is nonconstant and $k$ has characteristic $0$, so $f$ is separable onto its image; since $\operatorname{Hom}(\mathcal{O}(2), \mathcal{O}(a)) = H^0(\mathcal{O}(a - 2)) = 0$ for $a < 2$, some $a_i \geq 2$. So $-K_X \cdot f_* \mathbb{P}^1 = \deg f^* T_X = \sum_i a_i \geq 2$. By Proposition P8.1.6, all members $g$ of $H_0$ have $g_* \mathbb{P}^1 \equiv f_* \mathbb{P}^1$, and their images cover a dense subset of $X$. A member $g$ has $g_* \mathbb{P}^1 = e_g [g(\mathbb{P}^1)]$ with $e_g$ the degree onto the image, a divisor of the positive integer $A \cdot f_* \mathbb{P}^1$ for a fixed ample $A$, so $e_g$ takes finitely many values. A finite union of subsets of $X$ each contained in a proper closed subset is contained in a proper closed subset, so for some $e$ the curves $g(\mathbb{P}^1)$ with $e_g = e$ have union not contained in any proper closed subset, and they all have class $\gamma = f_* \mathbb{P}^1 / e$. By part 2 of Proposition P7.4.15, $\delta \cdot \gamma \geq 0$ for every pseudo-effective class $\delta$, while $K_X \cdot \gamma < 0$, so $K_X$ is not pseudo-effective. If $s \in H^0(X, \omega_X^{\otimes m})$ is nonzero with $m \geq 1$, then $m K_X$ is linearly equivalent to the effective divisor of $s$, so $K_X$ is pseudo-effective, a contradiction.

*Theorem P8.3.6.* This is the theorem of Miyaoka and Mori (MM86); for smooth $X$ it is Kollár and Mori, Theorem 1.10 (KM98). The proof is not given here. It follows the proof of Theorem P8.2.12, reducing modulo $p$, with the refinement of Theorem P8.2.10 that keeps a fixed point: in characteristic $p$, a curve with $K_X \cdot C < 0$ deforms with $x$ and many other points fixed, and bend-and-break produces a rational curve through $x$ of bounded degree.

*Theorem P8.3.7.* This is Boucksom, Demailly, Păun and Peternell, Corollary 0.3 (BDPP13). One direction is Corollary P8.3.5. The other uses the duality between the pseudo-effective cone and the cone of movable curves, proved by analytic methods, together with Theorem P8.3.6. The proof is not given here.

### Exercises

1. (A) Show that $\mathbb{P}^n$ is uniruled, using the family of lines through a fixed point, and that every smooth projective rational variety is uniruled.
2. (B) Let $X \subseteq \mathbb{P}^N$ be a hypersurface of degree $d \leq N - 1$. Let $M \subseteq X \times \mathbb{P}^{N-1}$ be an irreducible component of the incidence variety of pairs $(x, [v])$ with the line through $x$ in direction $v$ contained in $X$, chosen to dominate $X$. Construct a family of rational curves over an open subset of $M$ and show that $X$ is uniruled over any algebraically closed field.
3. (A) Using the standard fact that every morphism from $\mathbb{P}^1$ to an abelian variety $A$ is constant, show that an abelian variety is not uniruled, in any characteristic.
4. (B) Let $X$ be smooth and $f \colon \mathbb{P}^1 \to X$ a rational curve with $f^* T_X \cong \mathcal{O}(2) \oplus \mathcal{O}(-1)$, as for a line on a cubic surface. Show that the differential of $\operatorname{ev}$ at $(p, [f])$ is not surjective, and explain why this is consistent with the cubic surface being uniruled.
5. (B) Let $k$ have characteristic $0$ and $X$ be smooth and uniruled. Show that for every ample $H$ there is a free rational curve $f$ through a general point with $-K_X \cdot f_* \mathbb{P}^1 \geq 2$, and that if $n = 1$, then $X \cong \mathbb{P}^1$.
6. (B) Let $k$ be countable and $n \geq 1$. Show that $X$ has countably many closed points, so that the hypothesis of part 2 of Theorem P8.3.4 never holds, and check that the proofs of parts 1, 3 and 4 do not use the cardinality of $k$.

### Lean

Uniruled varieties, families of rational curves and the evaluation morphism are not in the repository. The pseudo-effective cone appears only through the intersection data `MinimalModel.IntersectionData` of `MinimalModel/Statements/Basic.lean`; Corollary P8.3.5 and Theorem P8.3.7 are not stated there.

### Notes and history

Uniruledness is the higher-dimensional form of the condition $p_g = 0$, $\kappa = -\infty$ for surfaces, and the definition through a dominant rational map $\mathbb{P}^1 \times M \dashrightarrow X$ with $\dim M = n - 1$ is Kollár, Definition IV.1.1 (Kol96), equivalent to Definition P8.3.1 by Kollár, Proposition IV.1.3. Theorem P8.3.4 is Kollár, Section IV.1, and Debarre, Section 4.1 (Deb01). Miyaoka and Mori proved their criterion in 1986 (MM86), and it gives the uniruledness of every Mori fibre space. The equivalence of uniruledness with the failure of pseudo-effectivity of $K_X$ is due to Boucksom, Demailly, Păun and Peternell (BDPP13); the conjecture that uniruledness is equivalent to $\kappa(X) = -\infty$ is the nonvanishing conjecture of the minimal model program, open in dimension at least $4$. Shioda's examples (Shi74) show that in characteristic $p$ a uniruled surface can be of general type.
