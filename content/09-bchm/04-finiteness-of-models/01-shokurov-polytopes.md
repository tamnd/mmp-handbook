---
title: Shokurov polytopes
nodes: []
sources: [BCHM10, Sho92, Cor07, KM98]
reads_with: [BCHM10:3.7, Cor07:6]
requires: [1.5, 4.2, 7.4, 7.6]
level: advanced
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Shokurov polytopes

### Statement

Throughout, $X$ is a normal projective variety of dimension $n \ge 2$ over an algebraically closed field of characteristic zero. A boundary is an effective $\mathbb{R}$-divisor. Let $S_1, \ldots, S_k$ be distinct prime divisors on $X$ and let $\operatorname{WDiv}_{\mathbb{R}}(S)$ be the real vector space of $\mathbb{R}$-divisors supported on $S_1 \cup \cdots \cup S_k$, with the basis $S_1, \ldots, S_k$ and the rational structure given by the divisors with rational coefficients.

**Definition 9.4.1 (rational polytopes and the lc polytope).** A *rational polytope* in a real vector space with a rational structure is the convex hull of finitely many rational points; the empty set counts as a rational polytope. Equivalently, it is a bounded set cut out by finitely many inequalities $\ell \ge c$ with $\ell$ a rational linear form and $c \in \mathbb{Q}$. An affine subspace $V \subseteq \operatorname{WDiv}_{\mathbb{R}}(S)$ is *defined over the rationals* if it is the translate of the span of rational divisors by a rational divisor. For such $V$, assuming that $K_X + \Delta$ is $\mathbb{R}$-Cartier for every $\Delta \in V$ (for example, $X$ is $\mathbb{Q}$-factorial), put
$$\mathcal{L}(V) = \{ \Delta \in V : \Delta \ge 0 \text{ and } (X, \Delta) \text{ is log canonical} \}.$$
If $A$ is an ample $\mathbb{Q}$-divisor, $\mathcal{L}_A(V) = \{ \Delta = A + B : B \in V, \ B \ge 0, \ (X, A + B) \text{ is log canonical} \}$ is the version used by BCHM, with a fixed general ample part.

**Lemma 9.4.2 (the lc polytope is a rational polytope).** Let $V \subseteq \operatorname{WDiv}_{\mathbb{R}}(S)$ be an affine subspace defined over the rationals such that $K_X + \Delta$ is $\mathbb{R}$-Cartier for every $\Delta \in V$, and suppose that $K_X$ is $\mathbb{Q}$-Cartier and the $S_i$ are $\mathbb{Q}$-Cartier. Then $\mathcal{L}(V)$ is a rational polytope.

Lean: not yet in Lean.

**Definition 9.4.3 (weak log canonical models, log terminal models, ample models).** Let $(X, \Delta)$ be a pair with $X$ projective and $K_X + \Delta$ $\mathbb{R}$-Cartier. A *birational contraction* is a birational map $\varphi \colon X \dashrightarrow Y$ of normal projective varieties whose inverse contracts no divisor. A prime divisor $F$ on $X$ is *$\varphi$-exceptional* if $\varphi$ contracts it. Put $\Gamma = \varphi_* \Delta$ and suppose that $K_Y + \Gamma$ is $\mathbb{R}$-Cartier.

1. $\varphi$ is a *weak log canonical model* of $(X, \Delta)$ if $K_Y + \Gamma$ is nef and $a(F, X, \Delta) \le a(F, Y, \Gamma)$ for every $\varphi$-exceptional prime divisor $F$ on $X$.
2. $\varphi$ is a *log terminal model* of $(X, \Delta)$ if it is a weak log canonical model, $Y$ is $\mathbb{Q}$-factorial, $(Y, \Gamma)$ is dlt, and $a(F, X, \Delta) < a(F, Y, \Gamma)$ for every $\varphi$-exceptional $F$.
3. A rational map $\psi \colon X \dashrightarrow Z$ to a normal projective variety is the *ample model* of $K_X + \Delta$ if there is an ample $\mathbb{R}$-divisor $H$ on $Z$ such that, for a resolution $p \colon W \to X$ with $q = \psi \circ p$ a morphism, $p^*(K_X + \Delta) \sim_{\mathbb{R}} q^* H + E$ with $E \ge 0$, and every effective $B \sim_{\mathbb{R}} p^*(K_X + \Delta)$ satisfies $B \ge E$.

For a birational contraction $\varphi$ and a rational polytope $\mathcal{P}$ of boundaries put $\mathcal{W}_\varphi(\mathcal{P}) = \{ \Delta \in \mathcal{P} : \varphi \text{ is a weak log canonical model of } (X, \Delta) \}$ and $\mathcal{N}(\mathcal{P}) = \{ \Delta \in \mathcal{P} : K_X + \Delta \text{ is nef} \}$, so that $\mathcal{N}(\mathcal{P}) = \mathcal{W}_{\mathrm{id}}(\mathcal{P})$.

**Lemma 9.4.4 (the comparison divisor).** Let $\varphi \colon X \dashrightarrow Y$ be a birational contraction, $\Delta$ an $\mathbb{R}$-divisor on $X$ with $K_X + \Delta$ $\mathbb{R}$-Cartier, $\Gamma = \varphi_* \Delta$ with $K_Y + \Gamma$ $\mathbb{R}$-Cartier, and $p \colon W \to X$, $q \colon W \to Y$ a common resolution with $p$ projective. Put $E = p^*(K_X + \Delta) - q^*(K_Y + \Gamma)$.

1. $E = \sum_F \bigl( a(F, Y, \Gamma) - a(F, X, \Delta) \bigr) F$, the sum over the prime divisors $F$ of $W$, and $E$ is $q$-exceptional.
2. For every divisor $F$ over $W$, $a(F, Y, \Gamma) = a(F, X, \Delta) + \operatorname{mult}_F E$, where $\operatorname{mult}_F E$ is the coefficient of $F$ in the pullback of $E$ to a model on which $F$ is a divisor.
3. If $K_Y + \Gamma$ is nef, then $E \ge 0$ if and only if $a(F, X, \Delta) \le a(F, Y, \Gamma)$ for every $\varphi$-exceptional prime divisor $F$ on $X$, that is, if and only if $\varphi$ is a weak log canonical model.
4. If $E \ge 0$ and $(X, \Delta)$ is klt (respectively lc), then $(Y, \Gamma)$ is klt (respectively lc). If $\varphi$ is a weak log canonical model, then $K_X + \Delta$ is pseudo-effective.

Lean: not yet in Lean.

**Theorem 9.4.5 (Shokurov's nef polytope).** Let $X$ be $\mathbb{Q}$-factorial and let $\mathcal{P}$ be a rational polytope of boundaries supported on $S_1 \cup \cdots \cup S_k$ such that $(X, \Delta)$ is klt for every $\Delta \in \mathcal{P}$. Then $\mathcal{N}(\mathcal{P}) = \{ \Delta \in \mathcal{P} : K_X + \Delta \text{ is nef} \}$ is a rational polytope.

Lean: not yet in Lean.

**Proposition 9.4.6 (the polytope of a fixed model).** Let $X$ and $\mathcal{P}$ be as in Theorem 9.4.5, and let $\varphi \colon X \dashrightarrow Y$ be a birational contraction to a $\mathbb{Q}$-factorial normal projective variety. Then $\mathcal{W}_\varphi(\mathcal{P})$ is a rational polytope.

Lean: not yet in Lean.

### Proof in words

The lc condition is read off one log resolution, by Theorem 4.2.14. On a fixed log resolution the coefficients of the crepant pullback are affine functions of the coefficients of $\Delta$ with rational coefficients, so log canonicity is a finite system of rational linear inequalities, and $\mathcal{L}(V)$ is a rational polyhedron. It is bounded because the coefficients lie in $[0, 1]$.

For the nef polytope, write points of $\mathcal{P}$ as convex combinations $\sum t_i \Delta_i$ of the rational vertices. Nefness of $\sum t_i (K_X + \Delta_i)$ is tested on curves. The only curves that matter span extremal rays that are negative for some vertex, and on each such ray one can choose a rational curve of bounded degree against the most negative vertex, by Kawamata's length bound. The resulting test vectors $\bigl((K_X + \Delta_i) \cdot C\bigr)_i$ lie in a translate of a lattice and are bounded below, and among such vectors only the finitely many minimal ones give independent constraints. This is Dickson's lemma, and it makes the nef locus a finite intersection of rational half-spaces. The cone theorem of Volume 7 is stated for $\mathbb{Q}$-boundaries, so the argument first proves the equality at rational points and then passes to the closure.

For a fixed model $\varphi$, the condition $E \ge 0$ of Lemma 9.4.4 is again a finite system of rational linear inequalities, and on the polytope it cuts out, $\varphi_*$ carries boundaries to klt boundaries on $Y$ and the nef condition on $Y$ is Theorem 9.4.5 again.

### Examples

**Example 9.4.7 (three concurrent lines).** Let $L_1, L_2, L_3 \subseteq \mathbb{P}^2$ be distinct lines through a point $p$, and let $V$ be the span of $L_1, L_2, L_3$, so that $\Delta = d_1 L_1 + d_2 L_2 + d_3 L_3$. The blow-up $f \colon Y \to \mathbb{P}^2$ at $p$, with exceptional curve $G$, is a log resolution of $(\mathbb{P}^2, L_1 + L_2 + L_3)$: the strict transforms $L_i'$ are disjoint and meet $G$ transversally at three distinct points. Since $\operatorname{mult}_p \Delta = d_1 + d_2 + d_3$ and $K_Y = f^* K_{\mathbb{P}^2} + G$,
$$f^*(K_{\mathbb{P}^2} + \Delta) = K_Y + \sum_i d_i L_i' + (d_1 + d_2 + d_3 - 1) G.$$
By Theorem 4.2.14, $(\mathbb{P}^2, \Delta)$ with $\Delta \ge 0$ is lc if and only if $d_i \le 1$ for each $i$ and $d_1 + d_2 + d_3 \le 2$, and klt if and only if the inequalities are strict. So $\mathcal{L}(V)$ is the unit cube $[0, 1]^3$ with the corner $(1, 1, 1)$ cut off by the plane $d_1 + d_2 + d_3 = 2$. Its vertices are $0$, the three unit vectors and the three points $e_i + e_j$ with $i \ne j$, all rational, in agreement with Lemma 9.4.2.

**Example 9.4.8 (a nef polytope on $\mathbb{F}_1$).** Let $X = \mathbb{F}_1$ be the blow-up of $\mathbb{P}^2$ at a point, with exceptional curve $E$, $L$ the pullback of a line and $F$ a fixed fibre, so $F \sim L - E$, $L^2 = 1$, $E^2 = -1$, $L \cdot E = 0$ and $K_X \sim -3L + E$. The linear system $|6L - 3E| = |3L + 3F|$ is free, so a general member $A''$ is a smooth curve meeting $E$ and $F$ transversally, away from $E \cap F$. Put $A = \frac{1}{2} A''$ and, for $(s, u) \in [0, \frac{3}{4}]^2$,
$$\Delta_{s, u} = A + sE + uF.$$
The divisor $A + E + F$ has simple normal crossings and all coefficients of $\Delta_{s,u}$ are less than $1$, so every $(X, \Delta_{s, u})$ is klt, and $\mathcal{P} = \{\Delta_{s,u}\}$ is a rational polytope (a square). In $N^1(X)$,
$$K_X + \Delta_{s, u} \equiv -3L + E + 3L - \tfrac{3}{2} E + sE + u(L - E) = uL - \bigl(\tfrac{1}{2} - s + u\bigr) E.$$
The cone $\overline{NE}(X)$ is spanned by $E$ and $F$, and $(xL - yE) \cdot E = y$, $(xL - yE) \cdot F = x - y$. With $x = u$ and $y = \frac{1}{2} - s + u$, the divisor $K_X + \Delta_{s,u}$ is nef if and only if $u \ge s - \frac{1}{2}$ and $s \ge \frac{1}{2}$. So $\mathcal{N}(\mathcal{P})$ is the quadrilateral with vertices $(\frac{1}{2}, 0)$, $(\frac{3}{4}, \frac{1}{4})$, $(\frac{3}{4}, \frac{3}{4})$ and $(\frac{1}{2}, \frac{3}{4})$, a rational polytope. The two constraints come from the two extremal curves $E$ and $F$, which are the curves $C_R$ of the proof of Theorem 9.4.5.

### Proof

*Proof of Lemma 9.4.2.* Write $V = \Delta^0 + U$ with $\Delta^0$ a rational divisor and $U$ spanned by rational divisors, and identify $\operatorname{WDiv}_{\mathbb{R}}(S)$ with $\mathbb{R}^k$ through the coefficients $d = (d_1, \ldots, d_k)$. Then $V$ is cut out by finitely many rational linear equations. Let $f \colon Y \to X$ be a log resolution of $(X, S_1 + \cdots + S_k)$, which exists by Theorem 4.2.10, and let $F_1, \ldots, F_N$ be the prime divisors on $Y$ that are $f$-exceptional or strict transforms of some $S_i$. Since $K_X$ and the $S_i$ are $\mathbb{Q}$-Cartier, $f^* K_X$ and $f^* S_i$ are defined, and for $\Delta = \sum d_i S_i$,
$$f^*(K_X + \Delta) = K_Y + \sum_{j} b_j(d) F_j, \qquad b_j(d) = c_j + \sum_i d_i \operatorname{mult}_{F_j} f^* S_i,$$
where $c_j$ is the coefficient of $F_j$ in $f^* K_X - K_Y$, for a choice of $K_Y$ with $f_* K_Y = K_X$. The numbers $c_j$ and $\operatorname{mult}_{F_j} f^* S_i$ are rational, so each $b_j$ is an affine function of $d$ with rational coefficients. The support of $\sum_j b_j(d) F_j$ is contained in $\sum_j F_j$, which has simple normal crossings, so $f$ is a log resolution of $(X, \Delta)$ for every $d$. By Theorem 4.2.14, for $\Delta \ge 0$, the pair $(X, \Delta)$ is lc if and only if $b_j(d) \le 1$ for all $j$. Hence
$$\mathcal{L}(V) = \{ d \in V : d_i \ge 0 \text{ for all } i, \ b_j(d) \le 1 \text{ for all } j \},$$
a set cut out from $V$ by finitely many rational affine inequalities. If $F_j$ is the strict transform of $S_i$, then $b_j(d) = d_i$, so $\mathcal{L}(V) \subseteq [0, 1]^k$ is bounded. A bounded set cut out by finitely many rational inequalities is the convex hull of its vertices, each of which is the unique solution of a system of rational linear equations, hence rational. So $\mathcal{L}(V)$ is a rational polytope. $\square$

*Proof of Lemma 9.4.4.* Choose $K_W$ with $p_* K_W = K_X$ and $q_* K_W = K_Y$, which is possible because $\varphi$ is an isomorphism at the generic point of every prime divisor of $Y$. By definition of discrepancies, $p^*(K_X + \Delta) = K_W - \sum_F a(F, X, \Delta) F$ and $q^*(K_Y + \Gamma) = K_W - \sum_F a(F, Y, \Gamma) F$, where for $F$ the strict transform of a prime divisor $D$ on $X$ (respectively on $Y$) the discrepancy is minus the coefficient of $D$ in $\Delta$ (respectively $\Gamma$). Subtracting gives the formula in part 1. If $F$ is not $q$-exceptional, then $q(F)$ is a prime divisor $D_Y$ on $Y$; since $\varphi^{-1}$ contracts no divisor, $D_Y$ is the strict transform of a prime divisor $D$ on $X$, and the coefficient of $D_Y$ in $\Gamma = \varphi_* \Delta$ equals the coefficient of $D$ in $\Delta$. So $a(F, Y, \Gamma) = a(F, X, \Delta)$ and the coefficient of $F$ in $E$ is zero; $E$ is $q$-exceptional. Part 2 follows by applying part 1 on a higher resolution $W' \to W$ on which $F$ is a divisor, since the pullback of $E$ to $W'$ is $p'^*(K_X + \Delta) - q'^*(K_Y + \Gamma)$.

For part 3, $-E = q^*(K_Y + \Gamma) - p^*(K_X + \Delta)$ is numerically equivalent over $X$ to $q^*(K_Y + \Gamma)$, which is nef, so $-E$ is $p$-nef. By the negativity lemma, Theorem 1.5.22 applied to $p$ and $B = E$, $E \ge 0$ if and only if $p_* E \ge 0$. The divisor $p_* E$ is the sum over prime divisors $D$ of $X$ of $\bigl(a(D, Y, \Gamma) - a(D, X, \Delta)\bigr) D$; for $D$ not $\varphi$-exceptional the coefficient is zero by the argument of part 1 applied to the strict transform of $D$, and for $D$ $\varphi$-exceptional it is $a(D, Y, \Gamma) - a(D, X, \Delta)$. This proves part 3.

For part 4, if $E \ge 0$ then part 2 gives $a(F, Y, \Gamma) \ge a(F, X, \Delta)$ for every divisor $F$ over $Y$, which is also a divisor over $X$, and the boundary $\Gamma$ is effective as the pushforward of an effective divisor. So the klt and lc conditions pass from $(X, \Delta)$ to $(Y, \Gamma)$. If $\varphi$ is a weak log canonical model, part 3 gives $E \ge 0$, so $p^*(K_X + \Delta) = q^*(K_Y + \Gamma) + E$ is the sum of a nef and an effective divisor, hence pseudo-effective, and $K_X + \Delta = p_* p^*(K_X + \Delta)$ is pseudo-effective, as pushforward preserves effective classes and limits of them. $\square$

*Proof of Theorem 9.4.5.* Let $\Delta_1, \ldots, \Delta_r$ be the vertices of $\mathcal{P}$; they are effective $\mathbb{Q}$-divisors and each $(X, \Delta_i)$ is klt. Let $T = \{ t \in \mathbb{R}_{\ge 0}^r : \sum t_i = 1 \}$ be the standard simplex and $\Delta(t) = \sum t_i \Delta_i$, so that $t \mapsto \Delta(t)$ is a surjective affine map $T \to \mathcal{P}$ with rational coefficients and $K_X + \Delta(t) = \sum t_i (K_X + \Delta_i)$. Put $N_T = \{ t \in T : K_X + \Delta(t) \text{ is nef} \}$. Since the image of a rational polytope under an affine map with rational coefficients is the convex hull of the images of its vertices, it suffices to show that $N_T$ is a rational polytope. Since $X$ is $\mathbb{Q}$-factorial, there is an integer $m \ge 1$ with $m(K_X + \Delta_i)$ Cartier for every $i$.

*Step 1: test curves.* Let $\mathcal{R}$ be the set of extremal rays $R$ of $\overline{NE}(X)$ with $(K_X + \Delta_i) \cdot R < 0$ for at least one $i$. For $R \in \mathcal{R}$ choose an index $i(R)$ for which $(K_X + \Delta_i) \cdot z$ is minimal among $i = 1, \ldots, r$, for a fixed nonzero $z \in R$; the choice does not depend on $z$. Then $R$ is a $(K_X + \Delta_{i(R)})$-negative extremal ray, and by Theorem 7.4.13 applied to the klt pair $(X, \Delta_{i(R)})$ it is spanned by the class of a rational curve $C_R$ with $0 < -(K_X + \Delta_{i(R)}) \cdot C_R \le 2n$. Put $a(R) = \bigl( (K_X + \Delta_i) \cdot C_R \bigr)_{i = 1}^r$. Each entry lies in $\frac{1}{m} \mathbb{Z}$, and by the choice of $i(R)$ every entry is at least $(K_X + \Delta_{i(R)}) \cdot C_R \ge -2n$. So
$$a(R) \in \Lambda = \tfrac{1}{m} \mathbb{Z}^r \cap [-2n, \infty)^r.$$

*Step 2: finitely many constraints.* The map $a \mapsto m(a + 2n \mathbf{1})$ identifies $\Lambda$ with a subset of $\mathbb{Z}_{\ge 0}^r$, compatibly with the componentwise order. By Dickson's lemma, every subset of $\mathbb{Z}_{\ge 0}^r$ has finitely many minimal elements for the componentwise order, and every element dominates a minimal one. (Dickson's lemma follows by induction on $r$: an infinite antichain would contain, after passing to subsequences coordinate by coordinate, a sequence that is nondecreasing in every coordinate, which is not an antichain.) Let $a^1, \ldots, a^s$ be the minimal elements of $\{a(R) : R \in \mathcal{R}\}$. For $t \in T$ all $t_i \ge 0$, so $a(R) \ge a^j$ componentwise implies $t \cdot a(R) \ge t \cdot a^j$. Hence
$$N'_T = \{ t \in T : t \cdot a(R) \ge 0 \text{ for all } R \in \mathcal{R} \} = \{ t \in T : t \cdot a^j \ge 0 \text{ for } j = 1, \ldots, s \}$$
is cut out from $T$ by finitely many rational linear inequalities, and is a rational polytope. Since $t \cdot a(R) = (K_X + \Delta(t)) \cdot C_R$, every nef $K_X + \Delta(t)$ satisfies these inequalities, and $N_T \subseteq N'_T$.

*Step 3: rational points of $N'_T$ are nef.* Let $t \in N'_T \cap \mathbb{Q}^r$. Then $\Delta(t)$ is an effective $\mathbb{Q}$-divisor in $\mathcal{P}$ and $(X, \Delta(t))$ is klt. Suppose $K_X + \Delta(t)$ is not nef. By the cone theorem, Theorem 7.4.6, $\overline{NE}(X) = \overline{NE}(X)_{K_X + \Delta(t) \ge 0} + \sum_j R_j$ with $(K_X + \Delta(t))$-negative extremal rays $R_j$, and since $K_X + \Delta(t)$ is negative somewhere on $\overline{NE}(X)$, at least one such ray $R$ exists. As $\sum_i t_i (K_X + \Delta_i) \cdot R < 0$ with $t_i \ge 0$, some $(K_X + \Delta_i) \cdot R < 0$, so $R \in \mathcal{R}$, and $(K_X + \Delta(t)) \cdot C_R = t \cdot a(R) < 0$ because $C_R$ spans $R$. This contradicts $t \in N'_T$. So $t \in N_T$.

*Step 4: closure.* The nef cone is closed and $t \mapsto K_X + \Delta(t)$ is continuous into $N^1(X)_{\mathbb{R}}$, so $N_T$ is closed. A rational polytope is the closure of its rational points: every point is a convex combination of the rational vertices, and perturbing the weights to nearby rational weights gives nearby rational points. By Step 3, $N'_T \cap \mathbb{Q}^r \subseteq N_T$, so $N'_T \subseteq N_T$. With Step 2, $N_T = N'_T$, a rational polytope. $\square$

*Proof of Proposition 9.4.6.* Let $p \colon W \to X$ and $q \colon W \to Y$ be a common resolution with $p$ projective, for instance a resolution of the closure of the graph. For $\Delta \in \mathcal{P}$ let $E(\Delta) = p^*(K_X + \Delta) - q^*(K_Y + \varphi_* \Delta)$, which is defined because $X$ and $Y$ are $\mathbb{Q}$-factorial. The map $\Delta \mapsto E(\Delta)$ is affine with rational coefficients, and $E(\Delta)$ is supported on the finitely many $q$-exceptional prime divisors of $W$ by Lemma 9.4.4, part 1. So $\mathcal{P}' = \{ \Delta \in \mathcal{P} : E(\Delta) \ge 0 \}$ is cut out from $\mathcal{P}$ by finitely many rational inequalities and is a rational polytope. By Lemma 9.4.4, part 4, $(Y, \varphi_* \Delta)$ is klt for every $\Delta \in \mathcal{P}'$, and $\varphi_* \mathcal{P}'$ is a rational polytope of boundaries supported on the strict transforms of the $S_i$ on $Y$, as the image of a rational polytope under the linear map $\varphi_*$. By Theorem 9.4.5 on $Y$, $\mathcal{N}(\varphi_* \mathcal{P}')$ is a rational polytope, cut out from $\varphi_* \mathcal{P}'$ by finitely many rational inequalities $\ell_j \ge c_j$. By Lemma 9.4.4, part 3, $\varphi$ is a weak log canonical model of $(X, \Delta)$ if and only if $\Delta \in \mathcal{P}'$ and $\varphi_* \Delta \in \mathcal{N}(\varphi_* \mathcal{P}')$. So $\mathcal{W}_\varphi(\mathcal{P})$ is cut out from $\mathcal{P}'$ by the rational inequalities $\ell_j(\varphi_* \Delta) \ge c_j$, and is a rational polytope. $\square$

### Exercises

1. (B) In Example 9.4.7 replace the three concurrent lines by three lines in general position. Show that $\mathcal{L}(V) = [0, 1]^3$, and explain the difference through the log resolutions.
2. (B) Let $X = \mathbb{P}^2$ and $V$ the span of a smooth conic $Q$ and a line $L$ tangent to it. Compute $\mathcal{L}(V)$ by resolving the tangency with three blow-ups, and list its vertices.
3. (B) Show that the conclusion of Theorem 9.4.5 fails if one drops the bound on the lengths: give a sequence of integral vectors in $\mathbb{Z}^2$ with infinitely many minimal elements for the componentwise order, and explain which step uses the lower bound $-2n$.
4. (B) In Example 9.4.8 compute $\mathcal{W}_\varphi(\mathcal{P})$ for the blow-down $\varphi \colon \mathbb{F}_1 \to \mathbb{P}^2$, using Lemma 9.4.4 directly, and check that it is a triangle.
5. (C) In the setting of Theorem 9.4.5 let $\mathcal{A}(\mathcal{P}) = \{ \Delta \in \mathcal{P} : K_X + \Delta \text{ is ample} \}$. Prove that $\mathcal{A}(\mathcal{P})$ is convex and open in $\mathcal{P}$, and that its closure is $\mathcal{N}(\mathcal{P})$ when it is nonempty. Give an example, on $\mathbb{F}_1$, where $\mathcal{A}(\mathcal{P})$ is empty although $\mathcal{N}(\mathcal{P})$ is not.
6. (C) Prove the relative version of Theorem 9.4.5 for a projective morphism $X \to U$, using the relative cone theorem and the relative length bound, and explain why the curves $C_R$ must be taken contracted to points of $U$.

### Lean

The polytopes of this section are not formalised. The project library has the statement `MinimalModel.FinitenessOfModels` for Theorem 9.4.9 of the next section, which takes the rational polytope structure of $\mathcal{L}_A(V)$ as part of its setting.

### Notes and history

The rationality of the nef part of a polytope of boundaries is due to Shokurov, who used it in his work on 3-fold log flips and in the theory of log models. BCHM prove the relative version with real coefficients (their Section 3.7, with Lemma 3.7.2 for the lc polytope) and use it throughout; the argument with the length bound and the lattice $\frac{1}{m}\mathbb{Z}^r$ follows Corti's exposition in Cor07. The models of Definition 9.4.3 are those of BCHM, Definition 3.6.6 and the preceding definitions, in the projective case.
