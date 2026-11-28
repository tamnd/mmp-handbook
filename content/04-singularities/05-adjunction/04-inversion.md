---
title: Inversion of adjunction
nodes: []
sources: [KM98, Kaw07, Kol92, Sho92, Kol13]
reads_with: [KM98:ch5, Kol13:ch4]
requires: [4.1, 4.2, 4.3, 2.3, P5.5, P5.6, P5.7, P5.8]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Inversion of adjunction

### Statement

Inversion of adjunction is the converse of Theorem 4.5.17: the singularities of the different on $S$ control the singularities of $(X, S + B)$ in a neighbourhood of $S$. It is the main tool for proving that a pair is lc or plt, because the different lives in one dimension less. On surfaces it is a statement about curves, and this section proves it completely, from a vanishing theorem for a birational morphism of surfaces. In higher dimension it is a black box.

On a normal surface the pair $(X, S + B)$ need not have $K_X + S + B$ $\mathbb{R}$-Cartier. In that case the discrepancies are the numerical ones, computed with the numerical pullback (Definition 4.3.3), and lc and plt are defined by the conditions of Definition 4.2.1 on them. Theorem 4.2.14 holds in this setting with the same proof, since it only compares the crepant pullbacks on a log resolution and on its blow-ups by Theorem 4.2.12. So one log resolution decides.

**Theorem 4.5.25 (inversion of adjunction on surfaces).** Let $X$ be a normal surface, $P \in X$ a closed point, $S$ an integral curve through $P$, and $B \ge 0$ an $\mathbb{R}$-divisor with no component equal to $S$.

1. $(X, S + B)$ is lc near $P$ if and only if every coefficient of $\operatorname{Diff}_{S^\nu}(B)$ at a point of $\nu^{-1}(P)$ is at most 1.
2. $(X, S + B)$ is plt near $P$ if and only if $S$ is normal at $P$ and the coefficient of $\operatorname{Diff}_S(B)$ at $P$ is less than 1.

Lean: not yet in Lean.

In higher dimension, the lc case is a theorem of Kawakita, and the plt case is older.

**Theorem 4.5.26 (Kawakita: inversion of adjunction on log canonicity).** Let $X$ be a normal variety over a field of characteristic 0, $S$ a prime divisor with normalization $S^\nu$, and $B \ge 0$ an $\mathbb{R}$-divisor with no component equal to $S$, such that $K_X + S + B$ is $\mathbb{R}$-Cartier. Then $(X, S + B)$ is lc near $S$ if and only if $(S^\nu, \operatorname{Diff}_{S^\nu}(B))$ is lc.

Lean: not yet in Lean.

**Theorem 4.5.27 (Kollár-Shokurov connectedness).** Let $f \colon Y \to X$ be a proper birational morphism of normal varieties over a field of characteristic 0, and $\Delta_Y$ an $\mathbb{R}$-divisor on $Y$ such that $K_Y + \Delta_Y$ is $\mathbb{R}$-Cartier, $-(K_Y + \Delta_Y)$ is $f$-nef and $f_* \Delta_Y \ge 0$. Then for every point $x \in X$, the union of the centres on $Y$ of the divisors $E$ over $Y$ with $a(E, Y, \Delta_Y) \le -1$ meets $f^{-1}(x)$ in a connected set (possibly empty).

Lean: not yet in Lean.

**Theorem 4.5.28 (inversion of adjunction, plt case).** In the setting of Theorem 4.5.26, $(X, S + B)$ is plt near $S$ if and only if $S$ is normal and $(S, \operatorname{Diff}_S(B))$ is klt.

Lean: not yet in Lean.

*Status.* Theorems 4.5.26, 4.5.27 and 4.5.28 are black boxes in this chapter. Theorem 4.5.26 is Kaw07: M. Kawakita, *Inversion of adjunction on log canonicity*, Invent. Math. 167 (2007), no. 1, 129-133. Theorem 4.5.27 is due to Shokurov (Sho92) in low dimension and to Kollár in general (Kol92, Theorem 17.4); this chapter cites it in the form of KM98, Theorem 5.48. Theorem 4.5.28 is KM98, Theorem 5.50. The proofs use the relative Kawamata-Viehweg vanishing theorem, which Volume 5 proves. The proof of Theorem 4.5.25 below is the surface case of the proofs of Theorems 4.5.27 and 4.5.28, and its only black box is the following vanishing theorem.

**Theorem 4.5.29 (vanishing for a resolution of a surface).** Let $f \colon Y \to X$ be a resolution of a normal surface, $L$ an integral divisor on $Y$ and $N$ an $\mathbb{R}$-divisor on $Y$ with snc support and coefficients in $[0, 1)$. If $L - K_Y - N$ is $f$-nef, then $R^1 f_* \mathcal{O}_Y(L) = 0$.

Lean: not yet in Lean.

*Status.* Theorem 4.5.29 is a black box: it is the 2-dimensional case of the relative Kawamata-Viehweg vanishing theorem for a birational morphism (KM98, Theorem 2.70), and Volume 5 proves the vanishing theorem in general.

Throughout the rest of this section, $f \colon Y \to X$ is a resolution of a normal surface, projective over $X$, $\Delta_Y = \sum_D d_D D$ is an $\mathbb{R}$-divisor on $Y$ with snc support such that $K_Y + \Delta_Y \equiv_f 0$, that is, $(K_Y + \Delta_Y) \cdot E = 0$ for every exceptional curve $E$, and $N = \bigcup_{d_D \ge 1} D$.

**Theorem 4.5.30 (connectedness on surfaces).** In this setting, suppose that $f_* \Delta_Y \ge 0$, and let $P \in X$ be a closed point.

1. $N \cap f^{-1}(P)$ is connected (possibly empty).
2. If, near $f^{-1}(P)$, $N$ is a single non-exceptional curve $S'$ with $d_{S'} = 1$, then $S = f(S')$ is normal at $P$.

Lean: not yet in Lean.

**Lemma 4.5.31 (a good log resolution).** Let $(X, S + B)$ be as in Theorem 4.5.25. There is a log resolution $f \colon Y \to X$ of $(X, S + B)$ near $P$ such that, for the crepant pullback $K_Y + \Delta_Y = f^*(K_X + S + B)$, no component of $\Delta_Y$ with negative coefficient meets a component with coefficient at least 1.

Lean: not yet in Lean.

**Lemma 4.5.32 (curves of coefficient one).** In the setting of Theorem 4.5.30, let $E$ be an exceptional curve with $d_E = 1$. Then

$$\sum_{D \ne E} d_D \, (D \cdot E) = 2 - 2 p_a(E) \le 2.$$

If no component with negative coefficient meets $E$, then every term is nonnegative, and so $E$ meets at most two components with coefficient at least 1, counted with intersection multiplicity, and it does not meet a component with $d_D \ge 1$ in addition to one with $d_D > 1$.

Lean: not yet in Lean.

### Proof in words

The vanishing theorem says that on a resolution of a surface, functions on the part of $Y$ where $\Delta_Y$ has coefficient at least 1 all come from $X$. Concretely, write $\lfloor \Delta_Y \rfloor = F - A$ with $F$ and $A$ effective. Then $A - F$ differs from $K_Y + \{\Delta_Y\}$ by an $f$-numerically trivial divisor, so its $R^1$ vanishes, and $f_*\mathcal{O}_F$ is a quotient of $\mathcal{O}_X$. A quotient of a local ring is local, so its completion has no idempotents, and by the theorem on formal functions the support of $F$, which is $N$, meets the fibre in a connected set. If $F$ is only $S'$, then $\mathcal{O}_X \to \nu_*\mathcal{O}_{S^\nu}$ is surjective, which is normality of $S$.

For inversion of adjunction, suppose that the different is at most 1 and that some coefficient $d_D$ is greater than 1. Connectedness gives a chain of curves of coefficient at least 1 from $S'$ to $D$ inside the fibre. If the chain has length one, then $D$ meets $S'$ and the different has a coefficient $d_D > 1$. If it is longer, the last curve of coefficient exactly 1 meets a curve of coefficient 1 and a curve of coefficient greater than 1, which adjunction on that curve forbids: $(K_Y + \Delta_Y) \cdot E = 0$ for a curve $E$ of coefficient 1 says that the other coefficients add up to $2 - 2p_a(E)$. Two technical points need care. The resolution is chosen so that no curve of negative coefficient touches the curves in the chain (Lemma 4.5.31), and components of $B$ of coefficient 1 through $P$ are first perturbed away.

For plt, normality of $S$ comes from part 2 of connectedness, and the condition on the different rules out every way of failing plt: a curve of coefficient 1 in the fibre would be connected to $S'$, and so would meet $S'$ at the single point over $P$.

### Examples

**Example 4.5.33 (a line and a tangent cusp).** Let $X = \mathbb{A}^2$, $S = \{y = 0\}$ and $B = tC$ with $C = \{y^2 = x^3\}$ and $0 \le t \le 1$. The line $S$ is the tangent line of the cusp, and $(C \cdot S)_P = 3$, so $\operatorname{Diff}_S(tC) = 3t P$. By Theorem 4.5.25, $(X, S + tC)$ is lc if and only if $t \le \frac13$, and plt if and only if $t < \frac13$.

Check on the log resolution of Example 4.2.16, which is also a log resolution of $(X, S + C)$. In the second chart of the first blow-up, $y = x y_1$, the curves are $C_1 = \{y_1^2 = x\}$, $E_1 = \{x = 0\}$ and $S_1 = \{y_1 = 0\}$, all through the origin, with $S_1$ transversal to $E_1$. The second blow-up is at that origin, and $S_2$ meets $E_2$ away from the point $E_1 \cap E_2 \cap C_2$ blown up third. So $f^*S = S' + E_1 + 2E_2 + 3E_3$, with $S'$ meeting only $E_2$. With the crepant pullback $tC' + (2t - 1)E_1 + (3t - 2)E_2 + (6t - 4)E_3$ of $(X, tC)$ from Example 4.2.16,

$$\Delta_Y = S' + tC' + 2t E_1 + 3t E_2 + (6t - 1) E_3.$$

The pair is lc if and only if $6t - 1 \le 1$, that is $t \le \frac13$, and plt if and only if $t < \frac13$, since $S'$ meets only $E_2$, of coefficient $3t < 1$. The different is $3t \, (E_2 \cdot S') P = 3tP$, as computed. Check of $(K_Y + \Delta_Y) \cdot E_2 = 0$: $E_2^2 = -2$, $K_Y \cdot E_2 = 0$, and $1 + (6t - 1) - 2 \cdot 3t = 0$. The lc threshold drops from $\frac56$ for $(X, tC)$ to $\frac13$ for $(X, S + tC)$, and the different finds the new threshold with one intersection number.

**Example 4.5.34 (Problem 5 of Chapter 2, explained).** Let $V \subset \mathbb{P}^{N-1}$ be a smooth hypersurface of degree $d$, $N \ge 3$, and $X \subset \mathbb{A}^N$ the cone over $V$, a normal hypersurface. The blow-up $f$ of the origin is a log resolution of $(\mathbb{A}^N, X)$: the strict transform $X'$ is the total space of $\mathcal{O}_V(-1)$, which is smooth, and it meets the exceptional divisor $E \cong \mathbb{P}^{N-1}$ transversally along $V$. Since $K_Y = f^*K_{\mathbb{A}^N} + (N - 1)E$ and $f^*X = X' + dE$,

$$\Delta_Y = X' + (d - N + 1) E.$$

The restriction $(\Delta_Y - X')|_{X'} = (d - N + 1) V$ is supported on the zero section $V$ of $X'$, which is contracted by $g \colon X' \to X$. So $\operatorname{Diff}_X(0) = 0$, and the adjunction formula is $K_X = (K_{\mathbb{A}^N} + X)|_X$. Part 2 of Proposition 4.5.6 shows that $a(V, X, 0) = N - 1 - d$. So $X$ is lc if and only if $d \le N$, and klt if and only if $d < N$. By Theorems 4.5.26 and 4.5.28, $(\mathbb{A}^N, X)$ is lc near $X$ if and only if $d \le N$, and plt if and only if $d < N$. The direct computation on $Y$ gives the same: $d - N + 1 \le 1$ and $d - N + 1 < 1$. This is the agreement noted in Problem 5 of Chapter 2: the lc threshold $\min(1, N/d)$ of $X$ in $\mathbb{A}^N$ is 1 exactly when the cone $X$ is lc.

**Example 4.5.35 (a surface through a cuspidal curve).** Let $X = \mathbb{A}^3$, $S = \{z = 0\}$ and $B = \{z = x^2 + y^3\}$, a smooth surface meeting $S$ along the cuspidal curve $C = \{x^2 + y^3 = 0\} \subset S \cong \mathbb{A}^2$. Then $X$ and $S$ are smooth and $\operatorname{Diff}_S(tB) = tC$ by part 3 of Proposition 4.5.6. By Example 4.2.16, $(\mathbb{A}^2, tC)$ is lc if and only if $t \le \frac56$, and klt if and only if $t < \frac56$. So, by Theorems 4.5.26 and 4.5.28, $(\mathbb{A}^3, S + tB)$ is lc near $S$ if and only if $t \le \frac56$, and plt near $S$ if and only if $t < \frac56$. A log resolution of $(\mathbb{A}^3, S + tB)$ needs blow-ups along curves and points in a threefold; inversion of adjunction replaces it by the three blow-ups of Example 4.2.16.

### Proof

*Proof of Theorem 4.5.30.* (1) Write $\lfloor \Delta_Y \rfloor = F - A$, where $F = \sum_{d_D \ge 1} \lfloor d_D \rfloor D$ and $A = \sum_{d_D < 0} (-\lfloor d_D \rfloor) D$ are effective integral divisors with no common component. The support of $F$ is $N$. Every component of $A$ is exceptional, since $f_*\Delta_Y \ge 0$. The fractional part $\{\Delta_Y\} = \Delta_Y - \lfloor \Delta_Y \rfloor$ has snc support and coefficients in $[0, 1)$, and

$$(A - F) - K_Y - \{\Delta_Y\} = -(K_Y + \Delta_Y) \equiv_f 0,$$

which is $f$-nef. Theorem 4.5.29 gives $R^1 f_* \mathcal{O}_Y(A - F) = 0$. Push forward the exact sequence $0 \to \mathcal{O}_Y(A - F) \to \mathcal{O}_Y(A) \to \mathcal{O}_F(A) \to 0$. This shows that $f_*\mathcal{O}_Y(A) \to f_*\mathcal{O}_F(A)$ is surjective.

Next, $f_*\mathcal{O}_Y(A) = \mathcal{O}_X$. A section over $f^{-1}(U)$ is a rational function $\varphi$ with $\operatorname{div}(\varphi) + A \ge 0$. Since $A$ is exceptional, $\varphi$ is regular on $U$ minus finitely many points, hence regular on $U$ by Hartogs (Theorem P3.7.33), and then $\operatorname{div}(f^*\varphi) \ge 0$. Since $A$ and $F$ have no common component, the restriction of the canonical section of $\mathcal{O}_Y(A)$ embeds $\mathcal{O}_F$ in $\mathcal{O}_F(A)$, and the section 1 of $\mathcal{O}_X = f_*\mathcal{O}_Y(A)$ maps to the image of $1 \in f_*\mathcal{O}_F$. So $f_*\mathcal{O}_F(A) = \mathcal{O}_X \cdot 1 \subset f_*\mathcal{O}_F \subset f_*\mathcal{O}_F(A)$, and therefore

$$\mathcal{O}_X \to f_*\mathcal{O}_F \quad \text{is surjective.}$$

The sheaf $f_*\mathcal{O}_F$ is coherent (Theorem P4.4.8), so $R = (f_*\mathcal{O}_F)_P$ is a cyclic $\mathcal{O}_{X,P}$-module, and its completion $\hat R$ is a quotient of the local ring $\hat{\mathcal{O}}_{X,P}$. A quotient of a local ring is local or zero, so $\hat R$ has no idempotents other than 0 and 1. By the theorem on formal functions for the projective morphism $f|_F \colon F \to X$ (Corollary P4.6.3), $\hat R \cong \varprojlim_n H^0(F_n, \mathcal{O}_{F_n})$, as rings, where $F_n = F \times_X \operatorname{Spec}(\mathcal{O}_{X,P}/\mathfrak{m}_P^n)$. Each $F_n$ is a scheme with underlying space $F \cap f^{-1}(P) = N \cap f^{-1}(P)$. If this set is the disjoint union of two nonempty closed subsets $Z_1$ and $Z_2$, each $F_n$ is the disjoint union of two nonempty open and closed subschemes, and the functions equal to 1 on the first and 0 on the second form a compatible system of idempotents. Their limit is an idempotent of $\hat R$ different from 0 and 1, a contradiction. So $N \cap f^{-1}(P)$ is connected.

(2) Shrink $X$ to a neighbourhood of $P$ such that $N = S'$ and $F = S'$. By the proof of part 1, $\mathcal{O}_X \to f_*\mathcal{O}_{S'}$ is surjective near $P$. The curve $S'$ is smooth, since the support of $\Delta_Y$ is snc, and $f|_{S'}$ is finite and birational onto $S$, so $f_*\mathcal{O}_{S'} = \nu_*\mathcal{O}_{S^\nu}$. The surjection factors as $\mathcal{O}_X \to \mathcal{O}_S \to \nu_*\mathcal{O}_{S^\nu}$, so the second map, which is injective because $S$ is integral, is an isomorphism near $P$. So $S$ is normal at $P$. $\square$

*Proof of Lemma 4.5.31.* Let $f_0 \colon Y_0 \to X$ be the minimal resolution near $P$ (Definition 4.3.4). By the proof of part 2 of Proposition 4.5.4, the crepant pullback $\Delta_0$ of $(X, S + B)$ to $Y_0$ satisfies $\Delta_0 \ge 0$: its exceptional part is $(f_0^*K_X - K_{Y_0}) + (f_0^*(S + B) - f_{0*}^{-1}(S + B)) \ge 0$. By Theorem P5.6.17, a finite sequence of point blow-ups makes the total transform of $f_0^{-1}(S + B) \cup \operatorname{Exc}(f_0)$ an snc curve, and the composite $f$ is a log resolution. Along the sequence, track the following property of a crepant pullback $\Delta = \Delta^+ - \Delta^-$, with $\Delta^+, \Delta^- \ge 0$ without common components:

(J) every point $y$ on a component of $\Delta^-$ satisfies $\operatorname{mult}_y \Delta^+ < 1$.

Property (J) holds on $Y_0$, since $\Delta_0^- = 0$. Suppose it holds for $\Delta$ on a surface $Y_1$, and let $h$ be the blow-up of a point $y$, with exceptional curve $G$. As in the proof of Proposition 4.5.2, the new crepant pullback is $h^*\Delta - G$, and the coefficient of $G$ is $d_G = \operatorname{mult}_y \Delta^+ - \operatorname{mult}_y \Delta^- - 1$. Every component of $\Delta^-$ is a curve created by an earlier blow-up, so it is a smooth curve and its strict transform meets $G$ in at most one point. The points off $G$ are unchanged. For a point $z \in G$, the multiplicity of the new positive part at $z$ is at most $\max(d_G, 0) + \operatorname{mult}_y \Delta^+$, and in fact the strict transforms of the components of $\Delta^+$ through $y$ contribute in total at most $\operatorname{mult}_y \Delta^+$ at $z$, since $\sum_{z \in G} \operatorname{mult}_z D'' \le D'' \cdot G = \operatorname{mult}_y D$.

If $y$ lies on a component of $\Delta^-$, then $\operatorname{mult}_y \Delta^+ < 1$ by (J), so $d_G < 0$. Then $G$ is in the new negative part, the new positive part at $z \in G$ consists of strict transforms of components of $\Delta^+$ only, with multiplicity at most $\operatorname{mult}_y \Delta^+ < 1$, and (J) holds at every point of $G$. If $y$ lies on no component of $\Delta^-$ and $d_G < 0$, then $\operatorname{mult}_y \Delta^+ < 1$, and the same argument applies. If $y$ lies on no component of $\Delta^-$ and $d_G \ge 0$, then no negative component passes through a point of $G$, and (J) holds trivially on $G$. So (J) holds on $Y$.

Finally, (J) implies the statement: if a component of $\Delta_Y^-$ meets a component $D$ with $d_D \ge 1$ at a point $y$, then $\operatorname{mult}_y \Delta_Y^+ \ge d_D \ge 1$, contradicting (J). $\square$

*Proof of Lemma 4.5.32.* The curve $E$ is proper, so adjunction on $Y$ (Theorem P5.5.14) gives $K_Y \cdot E + E^2 = 2p_a(E) - 2$, and $p_a(E) \ge 0$. The condition $(K_Y + \Delta_Y) \cdot E = 0$ with $d_E = 1$ reads $K_Y \cdot E + E^2 + \sum_{D \ne E} d_D (D \cdot E) = 0$, which is the formula. If no negative component meets $E$, every term is nonnegative. A component with $d_D \ge 1$ meeting $E$ contributes at least $D \cdot E \ge 1$, and one with $d_D > 1$ contributes more than 1, so a component with $d_D \ge 1$ and another with $d_D > 1$ would give a sum greater than 2. $\square$

*Proof of Theorem 4.5.25.* Shrink $X$ to a neighbourhood of $P$ such that every component of $S + B$ passes through $P$, $X \setminus P$ is smooth and $(X \setminus P, S + B)$ is snc. Then the log resolution below is an isomorphism over $X \setminus P$. Let $f$ be the log resolution of Lemma 4.5.31 and $\Delta_Y$ the crepant pullback, so that $K_Y + \Delta_Y \equiv_f 0$, $f_*\Delta_Y = S + B \ge 0$, and by Theorem 4.2.14 the pair is lc if and only if every $d_D \le 1$. Since $S'$ is smooth and the support is snc, the coefficient of $\operatorname{Diff}_{S^\nu}(B)$ at a point $q \in S' \cap f^{-1}(P)$ is $d_D$ if $q$ lies on a component $D \ne S'$, and 0 otherwise. The fibre $f^{-1}(P)$ is connected (Theorem P4.6.7), and it is either the point $P$, if $f$ is an isomorphism near $P$, or a union of exceptional curves.

For a closed subset $W \subset Y$ consisting of components of $\Delta_Y$ meeting $f^{-1}(P)$, consider the graph whose vertices are these components, with an edge when two of them meet at a point of $f^{-1}(P)$. If $W \cap f^{-1}(P)$ is connected, this graph is connected: a splitting of the vertices into two sets with no edges between them splits $W \cap f^{-1}(P)$ into two disjoint closed subsets.

(1) If the pair is lc, Corollary 4.5.19 gives the bound on the different. Conversely, suppose that every coefficient of the different over $P$ is at most 1 and that some $d_D > 1$.

*Case 1: some component of $B$ has coefficient $b_j \ge 1$.* Let $B^{(1)}$ be the sum of the components of $B$ with coefficient at least 1, each with coefficient 1, and put $\Delta' = \Delta_Y - \varepsilon f^*B^{(1)}$ with $0 < \varepsilon < 1$. Then $K_Y + \Delta' \equiv_f 0$, $f_*\Delta' = S + B - \varepsilon B^{(1)} \ge 0$, and the support is still snc. Each component of $B^{(1)}$ passes through $P$, so $f^*B^{(1)}$ has a positive coefficient on every exceptional curve over $P$. (Its exceptional part $Z \ge 0$ satisfies $Z \cdot E \le 0$ for every $E$ and $Z \cdot E < 0$ for some $E$; if $Z$ had coefficient 0 on some $E$, connectedness of $f^{-1}(P)$ would give such an $E$ meeting a curve with positive coefficient, with $Z \cdot E > 0$.) So for $\varepsilon$ small, the components with $d' = 1$ are exactly $S'$, the components with $d' > 1$ are those with $d > 1$, and $D$ is among them. The new different is $\operatorname{Diff}_{S^\nu}(B) - \varepsilon (f^*B^{(1)})|_{S'}$, at most the old one. By Theorem 4.5.30, the set $N' \cap f^{-1}(P)$ for $\Delta'$ is connected, and so is the graph of its components. A shortest path in the graph from $S'$ to a vertex with $d' > 1$ has length 1, since the only vertex with $d' = 1$ is $S'$. So a component $C$ with $d'_C > 1$ meets $S'$ at a point $q$ over $P$, and the coefficient of the different at $q$ is at least $d'_C > 1$, a contradiction.

*Case 2: every component of $B$ has coefficient less than 1.* Then the components with $d \ge 1$ are $S'$ and some exceptional curves, and $D$ is exceptional. By Theorem 4.5.30, $N \cap f^{-1}(P)$ is connected, so the graph of the components of $N$ is connected. Let $S' = C_0, C_1, \dots, C_r$ be a shortest path from $S'$ to a vertex $C_r$ with $d_{C_r} > 1$. Then $C_1, \dots, C_r$ are exceptional and $d_{C_i} = 1$ for $0 < i < r$. If $r = 1$, then $C_1$ meets $S'$ at a point over $P$ and the different has a coefficient $d_{C_1} > 1$ there, a contradiction. If $r \ge 2$, the exceptional curve $C_{r-1}$ has $d = 1$ and meets $C_{r-2}$, with $d \ge 1$, and $C_r$, with $d > 1$. By Lemma 4.5.31 no negative component meets $C_{r-1}$, and Lemma 4.5.32 gives a contradiction. So every $d_D \le 1$, and the pair is lc near $P$.

(2) Suppose that $(X, S + B)$ is plt near $P$. Then it is lc, every exceptional $d_E < 1$, and every $b_j \le 1$ by part 1 of Theorem 4.2.3. Let $B_j$ be a component through $P$ with $b_j = 1$. Then $N \cap f^{-1}(P)$ consists of the finitely many points of $S'$ and of the curves $B_k'$ with $b_k = 1$ over $P$, and it is connected, so it is one point, at which $S'$ and $B_j'$ meet. Two components of coefficient 1 meeting contradict plt, as in the proof of Theorem 4.5.17. So near $f^{-1}(P)$, $N = S'$, and part 2 of Theorem 4.5.30 shows that $S$ is normal at $P$. The coefficient of the different is less than 1 by Corollary 4.5.19.

Conversely, suppose that $S$ is normal at $P$ and the coefficient of $\operatorname{Diff}_S(B)$ at $P$ is less than 1. Then $S' \cap f^{-1}(P)$ is a single point $q$. By part 1, the pair is lc near $P$, so every $d_D \le 1$. Suppose that it is not plt near any neighbourhood of $P$. On the log resolution $f$, by Corollary 4.2.13 and Theorem 4.2.14, this means, after shrinking $X$, that either some exceptional curve $E$ over $P$ has $d_E = 1$, or two components with coefficient 1 meet at a point $y$ over $P$. In the second case, if $f$ is an isomorphism near $P$, then $y = q = P$, one of the two components is $S'$ (only two components pass through a point of an snc curve on a surface, and every component of $B$ passes through $P$), and the different at $P$ is at least 1, a contradiction. If $f$ is not an isomorphism near $P$, then $y$ lies on an exceptional curve $E'$, and since at most two components pass through $y$, $E'$ is one of the two, with $d_{E'} = 1$: the first case. In the first case, $N \cap f^{-1}(P)$ is connected by Theorem 4.5.30 and contains $q$ and $E$, so $q$ is not an isolated point of it. Near $q$ the set $N \cap f^{-1}(P)$ is the union of $\{q\}$ and the exceptional curves through $q$ with $d \ge 1$. So $q$ lies on an exceptional curve $C$ with $d_C \ge 1$, and the coefficient of the different at $q$ is $d_C \ge 1$, a contradiction. So $(X, S + B)$ is plt near $P$. $\square$

### Exercises

1. (A) Let $X$ be the quadric cone, $S$ a line through the vertex and $B = bS_2$ for another line $S_2$ through the vertex. Use Theorem 4.5.25 and Example 4.5.16 to show that $(X, S + bS_2)$ is lc if and only if $b \le 1$ and plt if and only if $b < 1$.
2. (A) Let $X = \mathbb{A}^2$, $S = \{y = 0\}$ and $B = t\{y^2 = x^5\}$. Compute $\operatorname{Diff}_S(B)$ and use Theorem 4.5.25 to find the lc threshold of $\{y^2 = x^5\}$ with respect to $(\mathbb{A}^2, S)$.
3. (B) Let $X = \mathbb{A}^2$ and $S = \{x = 0\}$, a line transversal to the cusp $C = \{y^2 = x^3\}$. Compute $\operatorname{Diff}_S(tC)$ and show, with Theorem 4.5.25, that $(X, S + tC)$ is lc if and only if $t \le \frac12$. Check the coefficient of $E_3$ on the log resolution of Example 4.2.16.
4. (B) Show that the hypothesis $f_*\Delta_Y \ge 0$ in Theorem 4.5.30 cannot be dropped: on the blow-up $Y$ of $\mathbb{A}^2$ at the origin, find an $\mathbb{R}$-divisor $\Delta_Y = L_1' + L_2' - cL_3' + dE$, with $L_i'$ strict transforms of three lines through the origin, such that $K_Y + \Delta_Y \equiv_f 0$, $L_1'$ and $L_2'$ are the only components with coefficient at least 1, and $N \cap f^{-1}(P)$ is two points.
5. (B) Let $X$ be a normal surface and $S_1$, $S_2$ two curves through $P$ such that $(X, S_1 + S_2)$ is lc near $P$. Apply Theorem 4.5.30 to show that, on a log resolution, the strict transforms $S_1'$ and $S_2'$ are joined by a chain of exceptional curves with coefficient 1 or meet over $P$.
6. (C) Prove part 1 of Theorem 4.5.25 when $X$ is smooth at $P$, without the vanishing theorem: use only the blow-up formula $d_G = \operatorname{mult}_y \Delta - 1$ and induction on the number of blow-ups in a log resolution.

### Lean

Inversion of adjunction is not in Lean. The library has `MinimalModel.IsLc` and `MinimalModel.IsKlt`, which would state the two sides of Theorem 4.5.26 once the different is defined, but there is no different, no plt and no vanishing theorem.

### Notes and history

Shokurov formulated inversion of adjunction and proved it in low dimension as the key step of his construction of 3-dimensional log flips (Sho92), together with the connectedness lemma. Kollár proved connectedness in every dimension (Kol92, Theorem 17.4), from which the plt case of inversion of adjunction follows (KM98, Theorem 5.50). The lc case resisted for 15 years. Ein, Mustata and Yasuda proved it for $X$ smooth, or more generally lci, with jet schemes, and Kawakita proved the general case (Kaw07) by a short argument based on the vanishing theorem. The examples of this section show the main use of the theorem: a threshold on $X$ is computed by a threshold on the divisor $S$, one dimension down.
