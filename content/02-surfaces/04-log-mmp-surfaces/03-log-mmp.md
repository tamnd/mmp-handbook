---
title: The log minimal model program for surfaces
nodes: [MMXV8DZWP4]
sources: [KM98, Mat02, Kol13]
reads_with: [KM98:ch3, Mat02:ch1]
requires: [P3.11, P5.12, 2.3, 2.5, 3.3, 4.1, 4.2, 4.3]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The log minimal model program for surfaces

### Statement

Sections 1 and 2 give the two ingredients of the program for a klt surface pair: every negative extremal ray is spanned by a curve, and every such ray can be contracted, either to a point of a new klt surface pair or onto a lower-dimensional base. Since a contraction of a surface is never small, there are no flips, and the program is a finite sequence of contractions of curves. This section defines its outputs, proves that it terminates and that the two outputs exclude each other, and computes runs on Hirzebruch surfaces and on $\mathbb{P}(1,1,n)$.

**Definition 2.4.16 (log minimal models, log Mori fibre spaces and runs).** Let $(X, \Delta)$ be a klt surface pair.

1. A *log minimal model* of $(X, \Delta)$ is a klt surface pair $(X_m, \Delta_m)$ with a birational morphism $g \colon X \to X_m$ such that $\Delta_m = g_*\Delta$, $K_{X_m} + \Delta_m$ is nef, and $a(E, X, \Delta) < a(E, X_m, \Delta_m)$ for every $g$-exceptional curve $E$.
2. A *log Mori fibre space* is a klt surface pair $(X, \Delta)$ with the contraction $\varphi \colon X \to B$ of a $(K_X + \Delta)$-negative extremal ray with $\dim B < 2$. By Theorem 2.4.12, either $B$ is a point, $\rho(X) = 1$ and $-(K_X + \Delta)$ is ample, or $B$ is a smooth projective curve and $\rho(X) = 2$.
3. A *run of the log minimal model program* from $(X, \Delta)$ is a sequence of klt surface pairs $(X_0, \Delta_0) = (X, \Delta)$, $(X_1, \Delta_1)$, $\dots$, $(X_N, \Delta_N)$ built as follows. If $K_{X_i} + \Delta_i$ is nef, the run stops. Otherwise choose a $(K_{X_i} + \Delta_i)$-negative extremal ray $R_i$. If its square is nonnegative, the run stops with the log Mori fibre space $\varphi_{R_i} \colon X_i \to B$. If its square is negative, let $\varphi_i \colon X_i \to X_{i+1}$ be the divisorial contraction of Theorem 2.4.10 and $\Delta_{i+1} = \varphi_{i*}\Delta_i$, and continue.

The definition follows KM98, Definition 3.50, where a log minimal model is reached by a birational map whose inverse contracts no divisor. For surfaces the program only contracts curves, and its output is a morphism.

**Theorem 2.4.17 (the log minimal model program for klt surface pairs).** Let $(X, \Delta)$ be a klt surface pair.

1. Every run from $(X, \Delta)$ is defined at each step: each $(X_i, \Delta_i)$ is a klt surface pair, in particular $X_i$ is $\mathbb{Q}$-factorial, and $\rho(X_i) = \rho(X) - i$.
2. Every run stops, after $N \le \rho(X) - 1$ divisorial contractions.
3. A run stops either at a log minimal model $(X_N, \Delta_N)$ of $(X, \Delta)$, with $g = \varphi_{N-1} \circ \dots \circ \varphi_0$, or at a log Mori fibre space $\varphi \colon X_N \to B$.

Lean: not yet in Lean.

**Proposition 2.4.18 (the two outcomes exclude each other).** Let $(X, \Delta)$ be a klt surface pair. If some run from $(X, \Delta)$ stops at a log Mori fibre space, then $(X, \Delta)$ has no log minimal model, and every run from $(X, \Delta)$ stops at a log Mori fibre space. If some run stops at a log minimal model, every run does.

Lean: not yet in Lean.

**Theorem 2.4.19 (the log minimal model program for lc surfaces).** Let $X$ be a normal projective surface and $\Delta$ a boundary with $K_X + \Delta$ $\mathbb{R}$-Cartier, such that $(X, \Delta)$ is lc or $X$ is $\mathbb{Q}$-factorial. Then the cone theorem holds for $(X, \Delta)$, every $(K_X + \Delta)$-negative extremal ray has a contraction onto a normal projective variety, a birational contraction contracts one curve to a point and gives a pair of the same kind, and every sequence of such contractions stops after at most $\rho(X) - 1$ steps at a pair with $K + \Delta$ nef or at a Mori fibre space. This is due to Fujino (2012) over $\mathbb{C}$ and to Tanaka (2014) in every characteristic.

Lean: not yet in Lean. The statement for lc pairs is `MinimalModel.LcSurfaceMMP`.

### Proof in words

Termination is a count: each divisorial contraction lowers the Picard number by one, and the Picard number of a surface is at least one, so at most $\rho(X) - 1$ contractions can happen. Each step keeps the pair klt and $\mathbb{Q}$-factorial by Theorem 2.4.10, so the next step is again covered by Sections 1 and 2. When the run stops at a nef pair, discrepancies have strictly increased on every contracted curve, because the curve contracted at a step gains $a > 0$ and later steps only increase discrepancies. The two outcomes exclude each other because of a covering family of curves. A log Mori fibre space is covered by curves on which $K + \Delta$ is negative, the general ones avoid the finitely many points blown up on the way back to $X$, and their strict transforms on $X$ have the same intersection with $K_X + \Delta$. On the other hand, $K_X + \Delta$ is the pullback of the nef class of a log minimal model plus an effective exceptional divisor, so it is nonnegative on every curve outside finitely many.

### Examples

**Example 2.4.20 (two runs from a Hirzebruch surface).** Let $n \ge 2$ and $1 - \frac2n < b < 1$, and let $(X, \Delta) = (F_n, bC_-)$. By Example 2.4.6 both rays of $\overline{NE}(F_n)$ are negative: $(K + \Delta) \cdot C_- = n - 2 - bn < 0$ and $(K + \Delta) \cdot F = b - 2 < 0$. So there are two runs. Choosing the ray of $F$, of square $0$, stops at once with the log Mori fibre space $F_n \to \mathbb{P}^1$, the ruling, with $N = 0$. Choosing the ray of $C_-$, of square $-n$, contracts it by Example 2.4.13 to $(X_1, \Delta_1) = (\mathbb{P}(1,1,n), 0)$, with $\rho(X_1) = 1$. By Example 2.4.21, $-K_{X_1}$ is ample, so the single ray of $X_1$ has positive square and the run stops with the log Mori fibre space $X_1 \to \operatorname{pt}$, after $N = 1 = \rho(F_n) - 1$ contraction. The two runs end at different log Mori fibre spaces, so the output of the program is not unique. For $b \le 1 - \frac2n$ and $n \ge 3$ only the first run exists.

**Example 2.4.21 (the klt del Pezzo surface $\mathbb{P}(1,1,n)$).** Let $n \ge 2$, $\varphi \colon F_n \to X = \mathbb{P}(1,1,n)$ the contraction of $C_-$, which is the minimal resolution of $X$ by Definition 2.3.7, since $C_-^2 = -n \ne -1$, and $\ell = \varphi_*F$ the image of a fibre, a curve through the singular point $p'$. Then
$$\varphi^*\ell = F + \tfrac1n C_-, \qquad \ell^2 = \big(F + \tfrac1n C_-\big) \cdot F = \tfrac1n,$$
since $(F + tC_-) \cdot C_- = 1 - nt$ vanishes for $t = \frac1n$. The canonical class of $F_n$ is $K = -2C_- - (n+2)F$, and $\varphi_*$ gives $K_X \sim -(n+2)\ell$. By Example 2.4.13, $K = \varphi^*K_X - \frac{n-2}{n}C_-$. Check: $\varphi^*K_X - \frac{n-2}{n}C_- = -(n+2)F - \frac{n+2}{n}C_- - \frac{n-2}{n}C_- = -(n+2)F - 2C_-$. Then
$$K_X^2 = (n+2)^2 \ell^2 = \frac{(n+2)^2}{n}, \qquad -K_X \cdot \ell = \frac{n+2}{n}.$$
As a check, $K^2 = 8$ on $F_n$, and $(\varphi^*K_X)^2 = (K + \frac{n-2}{n}C_-)^2 = 8 + 2\frac{n-2}{n}(n-2) - \frac{(n-2)^2}{n} = 8 + \frac{(n-2)^2}{n} = \frac{(n+2)^2}{n}$. Since $\rho(X) = 1$ and $-K_X \cdot \ell > 0$, Kleiman's criterion shows that $-K_X$ is ample. The class group of $X$ is $\mathbb{Z}\ell$ and the Picard group is $n\mathbb{Z}\ell$ (Example 3.3.17), so $mK_X$ is Cartier if and only if $n$ divides $m(n+2)$, that is, $\frac{n}{\gcd(n, 2)}$ divides $m$. So $X$ is a klt del Pezzo surface of Picard number $1$, Gorenstein only for $n = 2$, where it is the quadric cone, and canonical only for $n = 2$, by $a(C_-, X, 0) = -\frac{n-2}{n}$. Its degree $K_X^2 = \frac{(n+2)^2}{n}$ is not an integer for $n \ge 3$, except for $n = 4$, where it is $9$.

**Example 2.4.22 (a run to a log minimal model).** On $F_n$, let $C_+ \sim C_- + nF$ be a section disjoint from $C_-$. By Example P3.11.30 the sections $\sigma_c$, for polynomials $c(t)$ of degree at most $n$, are all disjoint from $C_-$ and linearly equivalent to $C_+$. Let $G_1 = \sigma_0 = C_+$ and $G_2 = \sigma_c$ with $c$ of degree $n$ with $n$ distinct roots. Over the affine line $U_0$ with coordinate $t$ the two sections meet where $c(t) = 0$, at $n$ points, and over $t = \infty$ they do not meet, because $c$ has degree exactly $n$. Since $G_1 \cdot G_2 = (C_- + nF)^2 = n$, they meet transversally at these $n$ points. So $\Delta = bC_- + \gamma(G_1 + G_2)$ has simple normal crossings, and for $0 \le b, \gamma < 1$ the pair is klt by Theorem 4.2.14. Then
$$K + \Delta = (2\gamma + b - 2)C_- + (2\gamma n - n - 2)F,$$
$$(K + \Delta) \cdot C_- = n - 2 - bn, \qquad (K + \Delta) \cdot F = b + 2\gamma - 2.$$
Take $n = 4$, $b = \frac34$ and $\gamma = \frac78$. Then $K + \Delta = \frac12 C_- + F$, with $(K + \Delta) \cdot C_- = -1 < 0$ and $(K + \Delta) \cdot F = \frac12 > 0$. The only negative ray is that of $C_-$, and every run contracts it: $a = \frac{-1}{-4} = \frac14$, which is $b - \frac{n-2}{n} = \frac34 - \frac12$, as in Example 2.4.13. The image $(X_1, \Delta_1) = (\mathbb{P}(1,1,4), \frac78(G_1' + G_2'))$ has $K_{X_1} + \Delta_1 \equiv \varphi_*(\frac12 C_- + F) = \ell$, which is ample, since $\rho(X_1) = 1$ and $\ell^2 = \frac14 > 0$. The curves $G_i'$ do not pass through the singular point, and $a(C_-, X_1, \Delta_1) = -\frac34 + \frac14 = -\frac12 = a(C_-, X_1, 0)$, as Example 2.4.21 predicts. So the run stops after one step at a log minimal model, and the discrepancy of $C_-$ rose from $-\frac34$ to $-\frac12$. In general the image has $K_{X_1} + \Delta_1 \equiv (2\gamma n - n - 2)\ell$. For $n = 4$, $b = \frac34$ and $\gamma = \frac34$, it is numerically trivial, and the run ends at a log minimal model with $K + \Delta \equiv 0$, while $(K + \Delta) \cdot F = \frac14 > 0$ keeps the ruling from being a log Mori fibre space.

**Example 2.4.23 (rulings through the vertex of $\mathbb{P}(1,1,n)$).** Let $X = \mathbb{P}(1,1,n)$ with $n \ge 2$, and $\Delta = \sum_{i=1}^m a_i \ell_i$ for the images $\ell_i$ of distinct fibres $F_i$ of $F_n$, with $0 \le a_i \le 1$. Every $\ell_i$ passes through the singular point. By Example 2.4.21,
$$\varphi^*(K_X + \Delta) = K + \tfrac{n-2}{n}C_- + \sum_i a_i\big(F_i + \tfrac1n C_-\big),$$
so the crepant pullback is $\Delta_{F_n} = \sum_i a_i F_i + \frac{n - 2 + \sum_i a_i}{n} C_-$. The curves $F_i$ and $C_-$ form a divisor with simple normal crossings, so by Theorem 4.2.14 the pair is klt if and only if every $a_i < 1$ and $\sum_i a_i < 2$, and lc if and only if every $a_i \le 1$ and $\sum_i a_i \le 2$. In both cases $K_X + \Delta \equiv (\sum_i a_i - n - 2)\ell$ is anti-ample. So a klt pair of this form is always a log Mori fibre space over a point: the singular point limits the boundary through it, and the boundary of Example 2.4.22, which makes $K + \Delta$ ample, avoids the singular point.

### Proof

*Theorem 2.4.17.* (1) and (2) By induction on $i$: if $(X_i, \Delta_i)$ is a klt surface pair and the run does not stop, the ray $R_i$ has negative square, and Theorem 2.4.10 gives a klt surface pair $(X_{i+1}, \Delta_{i+1})$ with $\rho(X_{i+1}) = \rho(X_i) - 1$. Since $\rho \ge 1$ for every projective surface, the number $N$ of divisorial contractions satisfies $\rho(X) - N \ge 1$.

(3) A run stops for one of the two reasons of Definition 2.4.16. If it stops at a log Mori fibre space, there is nothing to prove. Suppose it stops at $(X_N, \Delta_N)$ with $K_{X_N} + \Delta_N$ nef, and let $g = \varphi_{N-1} \circ \dots \circ \varphi_0$. Then $g$ is a birational morphism, $g_*\Delta = \Delta_N$, and $(X_N, \Delta_N)$ is a klt surface pair. The $g$-exceptional curves are the strict transforms on $X$ of the curves $C_i \subset X_i$ contracted by $\varphi_i$, for $i < N$. By part 4 of Theorem 2.4.10, $a(C_i, X_{i+1}, \Delta_{i+1}) = a(C_i, X_i, \Delta_i) + a_i$ with $a_i > 0$, and every later step does not decrease any discrepancy. Every earlier step does not decrease it either, and the discrepancy of the divisor $C_i$ over $X$ is $a(C_i, X, \Delta) \le a(C_i, X_i, \Delta_i)$. So $a(C_i, X, \Delta) < a(C_i, X_N, \Delta_N)$, and $(X_N, \Delta_N)$ is a log minimal model.

*Proposition 2.4.18.* Suppose a run ends with a log Mori fibre space $\varphi \colon X'' \to B$, reached by $h \colon X \to X''$, and suppose $g \colon X \to M$ is a log minimal model. Let $S \subset X''$ be the finite set of points over which $h$ is not an isomorphism, and $\Delta'' = h_*\Delta$.

There are infinitely many integral curves $L'' \subset X''$ that avoid $S$ and have $(K_{X''} + \Delta'') \cdot L'' < 0$. If $B$ is a curve, take the fibres of $\varphi$ over points of $B$ outside $\varphi(S)$: their classes lie in the negative ray. If $B$ is a point, $-(K_{X''} + \Delta'')$ is ample and $\rho(X'')= 1$. Take $H''$ very ample. For a point $x \notin S$, the members of $|H''|$ through $x$ form a hyperplane of $|H''|$, and those among them that avoid the finite set $S$ form a nonempty open subset of it, since $H''$ separates points. Let $L''$ be a component through $x$ of such a member. As $x$ varies these give infinitely many curves avoiding $S$. Every curve on $X''$ has class a positive multiple of the generator of $\overline{NE}(X'')$, on which $K_{X''} + \Delta''$ is negative, so $(K_{X''} + \Delta'') \cdot L'' < 0$.

Let $L = h^{-1}_* L''$. Since $h$ is an isomorphism over a neighbourhood of $L''$, $L$ is disjoint from the $h$-exceptional curves. The $\mathbb{Q}$-divisor $K_X + \Delta - h^*(K_{X''} + \Delta'')$ is $h$-exceptional, since its pushforward is $0$, so
$$(K_X + \Delta) \cdot L = h^*(K_{X''} + \Delta'') \cdot L = (K_{X''} + \Delta'') \cdot L'' < 0.$$
On the other hand, write $K_X + \Delta = g^*(K_M + \Delta_M) + \sum_E e_E E$, a sum over the $g$-exceptional curves. For such $E$, with $\Delta = g^{-1}_*\Delta_M + \sum_E \delta_E E$, Definition 4.1.4 gives $K_X + g^{-1}_*\Delta_M = g^*(K_M + \Delta_M) + \sum_E a(E, M, \Delta_M) E$, and $a(E, X, \Delta) = -\delta_E$, so
$$e_E = a(E, M, \Delta_M) + \delta_E = a(E, M, \Delta_M) - a(E, X, \Delta) > 0.$$
The curves $L$ are infinitely many, so one of them is not a $g$-exceptional curve. For that one, $(K_X + \Delta) \cdot L = (K_M + \Delta_M) \cdot g_*L + \sum_E e_E E \cdot L \ge 0$, since $K_M + \Delta_M$ is nef and $E \cdot L \ge 0$. This contradicts the display. So no log minimal model exists, and by part 3 of Theorem 2.4.17 every run stops at a log Mori fibre space. The last sentence is the contrapositive of the first.

*Theorem 2.4.19.* This is cited from Fujino, *Minimal model theory for log surfaces* (Publ. RIMS 48, 2012), and Tanaka, *Minimal models and abundance for positive characteristic log surfaces* (Nagoya Math. J. 216, 2014). Here is what changes from Sections 1 and 2. The cone theorem in the $\mathbb{Q}$-factorial case is Theorem 2.4.4, which used only $\mathbb{Q}$-factoriality and $\delta_j \le 1$. When $X$ is not $\mathbb{Q}$-factorial, Mumford's intersection theory still gives the cone of curves and the dictionary of Lemma 2.4.2, and the curves of negative square are handled as in Lemma 2.4.3. For the contraction of a curve $C$ of negative square, the hypothesis $\theta_i < 1$ of Lemma 2.4.8 fails when some coefficient of $\Delta_Y$ equals $1$, and the singularities produced need not be rational: an lc pair can produce a simple elliptic or a cusp singularity. Fujino constructs the contraction by an argument that does not need the contracted point to be rational, and the classification of lc surface germs in Theorem 4.3.20 shows which singularities can appear. Tanaka adapts the construction to positive characteristic, where the Kawamata-Viehweg vanishing theorem is not available. Termination is again the count of Picard numbers.

### Exercises

1. (A) Run the log minimal model program from $(\mathbb{P}^2, \frac34(L_1 + L_2 + L_3 + L_4))$ for four general lines, and from $(\mathbb{P}^2, \frac12(L_1 + L_2 + L_3))$ for three concurrent lines. Which outcome occurs in each case?
2. (A) For $(F_3, \frac23 C_-)$ list all runs of the program and their outputs. For $(F_3, \frac13 C_-)$ do the same.
3. (B) In Example 2.4.22 with $n = 4$, find all pairs $(b, \gamma) \in [0, 1)^2$ for which the runs stop at a log minimal model. Show that some run stops at a log Mori fibre space over $\mathbb{P}^1$ if and only if $b + 2\gamma < 2$, and compare the answer with the condition that $K + \Delta$ is a nonnegative combination of $C_-$ and $F$.
4. (B) Show that $\mathbb{P}(1,1,n)$ has no log minimal model for any klt boundary $\Delta$ supported on the images of fibres of $F_n$, and find a klt boundary $\Delta$ on $\mathbb{P}(1,1,n)$ with $K + \Delta$ ample.
5. (B) Let $(X, \Delta)$ be a klt surface pair with $\rho(X) = r$. Show that every run has at most $r - 1$ steps, and give a pair on a blow-up of $\mathbb{P}^2$ in $r - 1$ points for which some run has exactly $r - 1$ divisorial steps.
6. (C) Show that a log minimal model of a klt surface pair $(X, \Delta)$ with $K_X + \Delta$ big is unique: if $g_1 \colon X \to M_1$ and $g_2 \colon X \to M_2$ are two log minimal models, then the $g_i$-exceptional curves are the curves $\Gamma$ on $X$ with $\Gamma \subseteq \operatorname{Supp} N$, where $K_X + \Delta = P + N$ is the Zariski decomposition, and $M_1 \cong M_2$ over $X$. You may use that the positive part of $K_X + \Delta$ is the pullback of $K_{M_i} + \Delta_{M_i}$.

### Lean

The theorem and the proposition for klt pairs are not yet in Lean. The library states the lc case as `MinimalModel.LcSurfaceMMP`: for every projective lc pair `A` of dimension $2$, `MinimalModel.EveryProgramEnds A`, that is, each sequence of steps is finite and every program extends to one that ends with a minimal model or a Mori fibre space. Its outcomes use `MinimalModel.IsMinimalModel` and `MinimalModel.IsMoriFibreSpace`. Theorem 2.4.17 is the klt case of this statement with the bound on the number of steps added. The smooth case is `MinimalModel.SurfaceMMP`.

### Notes and history

For klt surface pairs the program is the case of dimension $2$ of the program for klt pairs, and termination is the same count of Picard numbers as for smooth surfaces in Theorem P5.12.21. Fujino, *Minimal model theory for log surfaces* (Publ. RIMS 48, 2012), proved it for all lc surfaces and for $\mathbb{Q}$-factorial surfaces with a boundary, and proved abundance for lc surfaces; Tanaka, *Minimal models and abundance for positive characteristic log surfaces* (Nagoya Math. J. 216, 2014), extended both to every characteristic. KM98, Chapter 3, presents the program for klt pairs in any dimension, where the flips of Chapter 6 and termination are the main difficulties; for surfaces both vanish. Matsuki, Chapter 1, uses surfaces as the model case. The surfaces $\mathbb{P}(1,1,n)$ are the simplest klt del Pezzo surfaces of Picard number $1$. Kol13, Chapter 3, classifies the lc surface singularities that the lc case has to handle. Theorem 2.5.22 gives abundance for lc surface pairs, and Proposition 2.5.23 proves the big klt case, so that the log minimal models of this section have semiample $K + \Delta$.
