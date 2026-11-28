---
title: Holomorphic functions of several variables
nodes: []
sources: [Huy05, Voi02, Hor90, GH78, Har06]
reads_with: [Huy05:1.1, Voi02:1.1, Hor90:II.2, GH78:0.1]
requires: []
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Holomorphic functions of several variables

### Statement

Throughout the chapter $z = (z_1, \dots, z_n)$ are the coordinates of $\mathbb{C}^n$, $z_j = x_j + i y_j$, and $|z| = (\sum_j |z_j|^2)^{1/2}$. For a multi-index $\alpha \in \mathbb{Z}_{\geq 0}^n$ write $z^\alpha = z_1^{\alpha_1} \cdots z_n^{\alpha_n}$, $|\alpha| = \sum_j \alpha_j$, $\alpha! = \alpha_1! \cdots \alpha_n!$, $e_j$ for the $j$-th unit vector, and for $\rho \in (0,\infty)^n$, $\rho^\alpha = \rho_1^{\alpha_1} \cdots \rho_n^{\alpha_n}$. Results of one complex variable (the Cauchy integral formula on a disc, Riemann's removable singularity theorem, the residue theorem, the argument principle, and the fact that a locally uniform limit of holomorphic functions of one variable is holomorphic) are used freely.

**Definition P6.1.1 (polydiscs and holomorphic functions).** For $a \in \mathbb{C}^n$ and $r = (r_1, \dots, r_n) \in (0, \infty]^n$ the *polydisc* with centre $a$ and polyradius $r$ is $\Delta(a, r) = \{ z : |z_j - a_j| < r_j \text{ for all } j \}$. When all $r_j$ are finite, its *distinguished boundary* is the torus $\partial_0 \Delta(a,r) = \{ z : |z_j - a_j| = r_j \text{ for all } j \}$, and $\bar\Delta(a,r)$ is the closed polydisc. Let $U \subseteq \mathbb{C}^n$ be open. A function $f \colon U \to \mathbb{C}$ is *holomorphic* if it is continuous and holomorphic in each variable separately: for every $a \in U$ and every $j$, the function $t \mapsto f(a_1, \dots, a_{j-1}, t, a_{j+1}, \dots, a_n)$ is holomorphic on a neighbourhood of $a_j$ in $\mathbb{C}$. The holomorphic functions on $U$ form a $\mathbb{C}$-algebra $\mathcal{O}(U)$, and $U \mapsto \mathcal{O}(U)$ is a sheaf of rings $\mathcal{O}_U$ on $U$.

**Definition P6.1.2 (Wirtinger derivatives).** For a $C^1$ function $f$ on an open set of $\mathbb{C}^n$,
$$\frac{\partial f}{\partial z_j} = \frac12 \Bigl( \frac{\partial f}{\partial x_j} - i \frac{\partial f}{\partial y_j} \Bigr), \qquad \frac{\partial f}{\partial \bar z_j} = \frac12 \Bigl( \frac{\partial f}{\partial x_j} + i \frac{\partial f}{\partial y_j} \Bigr).$$
With $dz_j = dx_j + i\, dy_j$ and $d\bar z_j = dx_j - i\, dy_j$ one has $df = \sum_j \frac{\partial f}{\partial z_j} dz_j + \sum_j \frac{\partial f}{\partial \bar z_j} d\bar z_j$, $\overline{\partial f/\partial z_j} = \partial \bar f/\partial \bar z_j$, $\partial z_k/\partial z_j = \delta_{jk}$ and $\partial \bar z_k / \partial z_j = 0$. Both operators are derivations. The Cauchy-Riemann equations for $t \mapsto f(\dots, t, \dots)$ in the $j$-th slot read $\partial f / \partial \bar z_j = 0$.

**Theorem P6.1.3 (Cauchy integral formula on a polydisc).** Let $f$ be holomorphic on a neighbourhood of the closed polydisc $\bar\Delta = \bar\Delta(a, r)$ with $r \in (0, \infty)^n$. Then for every $z \in \Delta(a, r)$
$$f(z) = \frac{1}{(2\pi i)^n} \int_{\partial_0 \Delta} \frac{f(\zeta_1, \dots, \zeta_n)}{(\zeta_1 - z_1) \cdots (\zeta_n - z_n)} \, d\zeta_1 \cdots d\zeta_n,$$
the integral taken over the torus parametrized by $\zeta_j = a_j + r_j e^{i \theta_j}$, $\theta \in [0, 2\pi]^n$.

Lean: not yet in Lean.

**Theorem P6.1.4 (power series expansion and Cauchy estimates).** Let $f$ be holomorphic on $\Delta(a, r)$, $r \in (0, \infty]^n$.

1. There are unique $c_\alpha \in \mathbb{C}$ such that $f(z) = \sum_\alpha c_\alpha (z - a)^\alpha$ for all $z \in \Delta(a,r)$, the series converging absolutely and uniformly on compact subsets of $\Delta(a,r)$.
2. (Cauchy estimates.) If $0 < \rho_j < r_j$ for all $j$ and $M = \sup_{\partial_0 \Delta(a, \rho)} |f|$, then $|c_\alpha| \leq M \rho^{-\alpha}$ for every $\alpha$.
3. Conversely, if the terms of a power series $\sum_\alpha c_\alpha (z-a)^\alpha$ are bounded at a point $w$ with all $w_j \neq a_j$, the series converges absolutely and uniformly on compact subsets of $\Delta(a, (|w_1 - a_1|, \dots, |w_n - a_n|))$ and its sum is holomorphic there.

Lean: not yet in Lean.

**Corollary P6.1.5 (smoothness and the Cauchy-Riemann equations).** A holomorphic function $f$ on an open set $U \subseteq \mathbb{C}^n$ is $C^\infty$, its partial derivatives $\partial^{|\alpha|} f / \partial z^\alpha$ are holomorphic, $\partial f / \partial \bar z_j = 0$ for all $j$, and the coefficients in Theorem P6.1.4 are $c_\alpha = \frac{1}{\alpha!} \frac{\partial^{|\alpha|} f}{\partial z^\alpha}(a)$. Conversely a $C^1$ function $f$ on $U$ with $\partial f / \partial \bar z_j = 0$ for all $j$ is holomorphic.

Lean: not yet in Lean.

**Theorem P6.1.6 (identity theorem and maximum principle).** Let $U \subseteq \mathbb{C}^n$ be open and connected and $f \in \mathcal{O}(U)$.

1. If $f$ vanishes on a nonempty open subset of $U$, or if all partial derivatives $\partial^{|\alpha|} f / \partial z^\alpha$ vanish at one point of $U$, then $f = 0$.
2. If $|f|$ has a local maximum at a point of $U$, then $f$ is constant.

Lean: not yet in Lean.

**Proposition P6.1.7 (Weierstrass convergence theorem).** Let $f_k \in \mathcal{O}(U)$ converge to $f \colon U \to \mathbb{C}$ uniformly on compact subsets of $U$. Then $f$ is holomorphic, and for every $\alpha$ the derivatives $\partial^{|\alpha|} f_k / \partial z^\alpha$ converge to $\partial^{|\alpha|} f / \partial z^\alpha$ uniformly on compact subsets of $U$.

Lean: not yet in Lean.

**Theorem P6.1.8 (the inhomogeneous Cauchy-Riemann equation in one variable).** Write $w = s + it$ for the variable of $\mathbb{C}$, so that $dw \wedge d\bar w = -2i \, ds \wedge dt$.

1. (Cauchy-Pompeiu formula.) Let $D \subset \mathbb{C}$ be an open disc and $u$ a $C^1$ function on a neighbourhood of $\bar D$. For $z \in D$,
$$u(z) = \frac{1}{2\pi i} \int_{\partial D} \frac{u(w)}{w - z} \, dw + \frac{1}{2\pi i} \int_D \frac{\partial u/\partial \bar w (w)}{w - z} \, dw \wedge d\bar w.$$
2. Let $T$ be an open subset of $\mathbb{R}^m$ and $g \in C^\infty(\mathbb{C} \times T)$ with $g(w, \tau) = 0$ for $w \notin K$, for some compact $K \subset \mathbb{C}$. Then
$$u(z, \tau) = \frac{1}{2\pi i} \int_{\mathbb{C}} \frac{g(w, \tau)}{w - z} \, dw \wedge d\bar w$$
is $C^\infty$ on $\mathbb{C} \times T$, every derivative of $u$ in $\tau$ is obtained by differentiating $g$ under the integral, and $\partial u / \partial \bar z = g$. If $T$ is an open subset of $\mathbb{C}^m = \mathbb{R}^{2m}$ and $g$ is holomorphic in $\tau$ for each fixed $w$, then $u$ is holomorphic in $\tau$ for each fixed $z$.

Lean: not yet in Lean.

**Definition P6.1.9 (holomorphic maps).** Let $U \subseteq \mathbb{C}^n$ and $V \subseteq \mathbb{C}^m$ be open. A map $F = (F_1, \dots, F_m) \colon U \to V$ is *holomorphic* if every $F_i$ is holomorphic. Its *complex Jacobian* at $a$ is the matrix $J_F(a) = (\partial F_i / \partial z_j (a))$. A *biholomorphism* is a holomorphic bijection whose inverse is holomorphic. By the chain rule for Wirtinger derivatives, $\partial (G \circ F)_k / \partial \bar z_j = \sum_i \frac{\partial G_k}{\partial w_i} \frac{\partial F_i}{\partial \bar z_j} + \sum_i \frac{\partial G_k}{\partial \bar w_i} \frac{\partial \bar F_i}{\partial \bar z_j}$, so compositions of holomorphic maps are holomorphic by Corollary P6.1.5, and $J_{G \circ F}(a) = J_G(F(a)) J_F(a)$.

**Theorem P6.1.10 (holomorphic inverse and implicit function theorems).**

1. Let $F \colon U \to \mathbb{C}^n$ be holomorphic, $U \subseteq \mathbb{C}^n$ open, $a \in U$ and $\det J_F(a) \neq 0$. There are open neighbourhoods $U' \ni a$ and $V' \ni F(a)$ such that $F \colon U' \to V'$ is a biholomorphism.
2. Let $G \colon U \to \mathbb{C}^m$ be holomorphic on an open set $U \subseteq \mathbb{C}^n \times \mathbb{C}^m$ with coordinates $(z, w)$, let $(a, b) \in U$ with $G(a,b) = 0$, and assume that the matrix $(\partial G_i / \partial w_j (a,b))$ is invertible. There are open neighbourhoods $A \ni a$ and $B \ni b$ with $A \times B \subseteq U$ and a holomorphic map $\varphi \colon A \to B$ such that for $(z,w) \in A \times B$, $G(z, w) = 0$ if and only if $w = \varphi(z)$.

Lean: not yet in Lean.

### Proof in words

Every result of the section comes from the one-variable Cauchy formula applied in each variable separately. Iterating it over a polydisc expresses $f$ through its values on the distinguished boundary, and expanding the kernel $\prod_j (\zeta_j - z_j)^{-1}$ in a geometric series gives the power series, whose coefficients are bounded by the Cauchy estimates. Power series give smoothness, the identity theorem (the set where all derivatives vanish is open and closed) and the limit theorem (uniform limits preserve the Cauchy formula). The maximum principle reduces to one variable on complex lines. The inverse function theorem is the real one together with the observation that the differential of the inverse is complex linear. For the inhomogeneous equation $\partial u/\partial \bar z = g$ the Cauchy kernel $1/(\pi z)$ is a fundamental solution: Stokes' theorem on the complement of a small disc gives the Cauchy-Pompeiu formula, and the substitution $w = z + \zeta$ moves all derivatives onto $g$, which gives smoothness and the dependence on parameters.

### Examples

**Example P6.1.11 (domains of convergence).** The domain of convergence of a power series in several variables need not be a polydisc. The series $\sum_{k \geq 0} z_1^k z_2^k$ converges exactly where $|z_1 z_2| < 1$, an unbounded open set containing both coordinate axes, and its sum is $1/(1 - z_1 z_2)$ there. Part 3 of Theorem P6.1.4 is consistent with this: for $w$ with $|w_1 w_2| < 1$ and $w_1 w_2 \neq 0$, the polydisc $\Delta(0, (|w_1|, |w_2|))$ lies inside $\{ |z_1 z_2| < 1 \}$, and $\{|z_1 z_2| < 1\}$ is the union of these polydiscs together with the two axes. The sum $1/(1 - z_1 z_2)$ is holomorphic on the larger set $\{ z_1 z_2 \neq 1 \}$, but the series diverges at every point with $|z_1 z_2| \geq 1$, since its terms do not tend to $0$. Similarly $\sum_k z_1^k$ converges on $\{|z_1| < 1\} \times \mathbb{C}$, the polydisc of polyradius $(1, \infty)$.

**Example P6.1.12 (zero sets are not discrete).** In one variable the zeros of a nonzero holomorphic function on a connected open set are isolated. For $n \geq 2$ this fails: $f = z_1$ vanishes on the hyperplane $\{z_1 = 0\}$, and $f = z_1 z_2$ on the union of two lines in $\mathbb{C}^2$. So part 1 of Theorem P6.1.6 cannot be weakened to vanishing on a set with an accumulation point, and Corollary P6.1.15 shows that the zeros of a holomorphic function of $n \geq 2$ variables are never isolated. The hypothesis can be weakened in a different direction: if $U$ is connected, $U \cap \mathbb{R}^n \neq \emptyset$ and $f \in \mathcal{O}(U)$ vanishes on $U \cap \mathbb{R}^n$, then $f = 0$. Indeed, at $a \in U \cap \mathbb{R}^n$ the restriction $x \mapsto f(x)$ to $\mathbb{R}^n$ vanishes near $a$, and since $\partial f / \partial \bar z_j = 0$ the derivative $\partial f/\partial x_j$ equals $\partial f / \partial z_j$, which is again holomorphic. Inductively every $\partial^{|\alpha|} f / \partial z^\alpha (a)$ is a real partial derivative of $f|_{\mathbb{R}^n}$ at $a$, so it vanishes, and part 1 applies. The function $z_1$ vanishes on the real hypersurface $\{ z_1 = 0 \}$ of $\mathbb{C}^n$, of real dimension $2n-2$, but not on the totally real $\mathbb{R}^n$, of real dimension $n$; the size of a set does not decide whether it is a set of uniqueness.

### Proof

*Proof of Theorem P6.1.3.* Induction on $n$, the case $n = 1$ being the one-variable formula. Let $f$ be holomorphic on a neighbourhood of $\bar \Delta(a,r) = \bar\Delta' \times \bar D_n$, with $\Delta' \subseteq \mathbb{C}^{n-1}$ and $D_n$ the disc of radius $r_n$ about $a_n$. For $z = (z', z_n) \in \Delta$ the function $t \mapsto f(z', t)$ is holomorphic near $\bar D_n$, so $f(z', z_n) = \frac{1}{2\pi i}\int_{|\zeta_n - a_n| = r_n} f(z', \zeta_n) (\zeta_n - z_n)^{-1} d\zeta_n$. For fixed $\zeta_n$ on the circle, $z' \mapsto f(z', \zeta_n)$ is holomorphic near $\bar\Delta'$, so by induction $f(z', \zeta_n)$ is $(2\pi i)^{1-n}$ times the integral over $\partial_0 \Delta'$ of $f(\zeta', \zeta_n) \prod_{j<n} (\zeta_j - z_j)^{-1}$. Substituting gives an iterated integral of a continuous function on the compact torus $[0,2\pi]^n$, which equals the integral over the torus by Fubini's theorem.

*Proof of Theorem P6.1.4.* Fix $\rho$ with $0 < \rho_j < r_j$. For $z \in \Delta(a, \rho)$ and $\zeta \in \partial_0\Delta(a,\rho)$,
$$\prod_j \frac{1}{\zeta_j - z_j} = \prod_j \frac{1}{(\zeta_j - a_j)(1 - \frac{z_j - a_j}{\zeta_j - a_j})} = \sum_\alpha \frac{(z - a)^\alpha}{\prod_j (\zeta_j - a_j)^{\alpha_j + 1}}.$$
If $|z_j - a_j| \leq \theta \rho_j$ for all $j$ with $\theta < 1$, the terms are bounded by $\theta^{|\alpha|} \rho^{-\alpha} \prod_j \rho_j^{-1}$ uniformly in $\zeta$, and $\sum_\alpha \theta^{|\alpha|} = (1-\theta)^{-n}$. So by Theorem P6.1.3 on $\bar\Delta(a, \rho)$ the series may be integrated termwise against $f$, giving $f(z) = \sum_\alpha c_\alpha (z - a)^\alpha$ with
$$c_\alpha = \frac{1}{(2\pi i)^n} \int_{\partial_0 \Delta(a,\rho)} \frac{f(\zeta)}{\prod_j (\zeta_j - a_j)^{\alpha_j+1}} \, d\zeta_1 \cdots d\zeta_n,$$
and absolute and uniform convergence on $\{|z_j - a_j| \leq \theta \rho_j\}$. On the torus $d\zeta_j = i (\zeta_j - a_j) d\theta_j$, so $|c_\alpha| \leq (2\pi)^{-n} \int_{[0, 2\pi]^n} |f| \rho^{-\alpha} d\theta \leq M \rho^{-\alpha}$, which is part 2. Every compact subset of $\Delta(a,r)$ lies in some set $\{ |z_j - a_j| \leq \theta \rho_j \}$ with $\rho < r$ and $\theta < 1$, so the expansion holds on $\Delta(a,r)$ with the stated convergence. The coefficients do not depend on $\rho$ by uniqueness, which is proved as follows. If $\sum_\alpha c_\alpha (z-a)^\alpha = 0$ on $\Delta(a, r)$, restrict to $z = a + (\rho_1 e^{i\theta_1}, \dots, \rho_n e^{i \theta_n})$: the uniformly convergent series $\sum_\alpha c_\alpha \rho^\alpha e^{i \langle \alpha, \theta \rangle}$ vanishes identically, and integrating it against $e^{-i \langle \beta, \theta\rangle}$ over $[0, 2\pi]^n$ gives $c_\beta \rho^\beta = 0$.

For part 3, suppose $|c_\alpha| \, |w - a|^\alpha \leq C$ for all $\alpha$, where $|w-a|^\alpha = \prod_j |w_j - a_j|^{\alpha_j}$. On $\{ |z_j - a_j| \leq \theta |w_j - a_j| \}$, $\theta < 1$, the terms are bounded by $C \theta^{|\alpha|}$, so the series converges absolutely and uniformly there. Each partial sum over $|\alpha| \leq N$ is a polynomial. A uniform limit of continuous functions is continuous, and a uniform limit of functions holomorphic in one variable is holomorphic in that variable, so the sum is holomorphic.

*Proof of Corollary P6.1.5.* Let $\Delta(a, r) \subseteq U$ and write $f = \sum_\alpha c_\alpha (z-a)^\alpha$ as in Theorem P6.1.4. Fix $\rho < r$, $\theta < 1$ and $M$ as in part 2. On $Q = \{ |z_k - a_k| \leq \theta \rho_k \}$ the termwise derivative $\partial/\partial x_j$ of the series is $\sum_\alpha \alpha_j c_\alpha (z-a)^{\alpha - e_j}$, whose terms are bounded by $M \alpha_j \theta^{|\alpha| - 1} / \rho_j$, a summable family. So the series of $x_j$-derivatives converges uniformly on $Q$, and the same holds for $\partial / \partial y_j$, whose termwise series is $i$ times the previous one. A uniformly convergent series of $C^1$ functions whose derivative series converge uniformly is $C^1$ with the termwise derivatives. Hence $f$ is $C^1$ on the interior of $Q$, $\partial f / \partial y_j = i \, \partial f / \partial x_j$, that is $\partial f / \partial \bar z_j = 0$, and $\partial f / \partial z_j = \sum_\alpha \alpha_j c_\alpha (z-a)^{\alpha - e_j}$. This series has bounded terms at every point of $\Delta(a,r)$ with nonzero coordinates by the same estimate, so it is holomorphic on $\Delta(a,r)$ by part 3 of Theorem P6.1.4. By induction on $|\alpha|$, $f$ is $C^\infty$, every $\partial^{|\alpha|} f/ \partial z^\alpha$ is holomorphic and given by the termwise derivative, and evaluating at $z = a$ gives $\partial^{|\alpha|} f / \partial z^\alpha (a) = \alpha! \, c_\alpha$. Conversely, if $f$ is $C^1$ with $\partial f / \partial \bar z_j = 0$, it is continuous, and each slice function $t \mapsto f(\dots, t, \dots)$ is $C^1$ and satisfies the Cauchy-Riemann equation, so it is holomorphic in one variable. So $f$ is holomorphic.

*Proof of Theorem P6.1.6.* Let $A$ be the set of $b \in U$ at which all $\partial^{|\alpha|} f / \partial z^\alpha$ vanish. It is closed because the derivatives are continuous (Corollary P6.1.5). It is open: if $b \in A$, the expansion of $f$ on a polydisc about $b$ has all coefficients $0$ by Corollary P6.1.5, so $f$ vanishes on that polydisc, and so do its derivatives. If $f$ vanishes on a nonempty open set $V$, then $V \subseteq A$. In either case of part 1, $A$ is nonempty, so $A = U$ and $f = 0$. For part 2, let $|f|$ have a local maximum at $a$, and let $B$ be a ball about $a$ in $U$ with $|f| \leq |f(a)|$ on $B$. For $z \in B$ the function $g(\lambda) = f(a + \lambda (z - a))$ is holomorphic on a disc $\{|\lambda| < 1 + \varepsilon\}$ (it is a composition with an affine map, Definition P6.1.9), and $|g| \leq |g(0)|$ on it. By the one-variable maximum principle $g$ is constant, so $f(z) = g(1) = g(0) = f(a)$. Thus $f - f(a)$ vanishes on $B$, and $f$ is constant by part 1.

*Proof of Proposition P6.1.7.* The limit $f$ is continuous, and on each slice it is a locally uniform limit of holomorphic functions of one variable, so it is holomorphic. Differentiating the Cauchy formula of Theorem P6.1.3 under the integral, which is allowed since the integrand is smooth in $z$ for $z$ away from the torus, gives for $\bar\Delta(a, 2\rho) \subseteq U$ and $z \in \Delta(a, \rho)$
$$\frac{\partial^{|\alpha|} h}{\partial z^\alpha}(z) = \frac{\alpha!}{(2\pi i)^n} \int_{\partial_0 \Delta(a, 2\rho)} \frac{h(\zeta)}{\prod_j (\zeta_j - z_j)^{\alpha_j + 1}} \, d\zeta_1 \cdots d\zeta_n$$
for every $h$ holomorphic near $\bar\Delta(a, 2\rho)$. Since $|\zeta_j - z_j| \geq \rho_j$ there, $\sup_{\Delta(a, \rho)} |\partial^{|\alpha|} (f_k - f) / \partial z^\alpha| \leq \alpha! \, 2^n \rho^{-\alpha} \sup_{\partial_0 \Delta(a, 2\rho)} |f_k - f|$, which tends to $0$. A compact subset of $U$ is covered by finitely many such $\Delta(a, \rho)$.

*Proof of Theorem P6.1.8.* For part 1 fix $z \in D$ and $\varepsilon > 0$ with $\{|w - z| \leq \varepsilon\} \subset D$, and let $D_\varepsilon = D \setminus \{ |w - z| \leq \varepsilon \}$. The $1$-form $\eta = u(w) (w-z)^{-1} dw$ is $C^1$ near $\bar D_\varepsilon$ and
$$d\eta = \frac{\partial}{\partial \bar w} \Bigl( \frac{u}{w - z} \Bigr) d\bar w \wedge dw = - \frac{\partial u / \partial \bar w}{w - z} \, dw \wedge d\bar w,$$
because $1/(w-z)$ is holomorphic on $D_\varepsilon$. Stokes' theorem gives $\int_{\partial D} \eta - \int_{|w - z| = \varepsilon} \eta = - \int_{D_\varepsilon} (\partial u/\partial \bar w)(w-z)^{-1} dw \wedge d\bar w$, both circles oriented counterclockwise. As $\varepsilon \to 0$, $\int_{|w-z| = \varepsilon} \eta = i \int_0^{2\pi} u(z + \varepsilon e^{i\theta}) d\theta \to 2 \pi i \, u(z)$, and the integral over $D_\varepsilon$ tends to the integral over $D$, since $|w - z|^{-1}$ is integrable near $z$: $\int_{|\zeta| < \varepsilon} |\zeta|^{-1} ds\, dt = 2 \pi \varepsilon$. Rearranging gives the formula.

For part 2 substitute $w = z + \zeta$: $u(z, \tau) = \frac{1}{2\pi i} \int_{\mathbb{C}} g(z + \zeta, \tau) \zeta^{-1} d\zeta \wedge d\bar\zeta$. For $(z, \tau)$ in a compact set $Z \times T'$, the integrand vanishes unless $\zeta$ lies in the compact set $K - Z$, and every derivative of $g$ in $(z, \tau)$ is bounded on the relevant compact set. Since $\zeta^{-1}$ is integrable on compact sets, the dominated convergence theorem allows differentiation under the integral to every order, so $u$ is $C^\infty$ and its derivatives are the integrals of the derivatives of $g$. In particular, undoing the substitution and taking a disc $D$ containing $K$ and $z$,
$$\frac{\partial u}{\partial \bar z}(z, \tau) = \frac{1}{2\pi i} \int_D \frac{\partial g / \partial \bar w (w, \tau)}{w - z} \, dw \wedge d\bar w = g(z, \tau),$$
by part 1 applied to $g(\cdot, \tau)$, which vanishes on $\partial D$. If $T \subseteq \mathbb{C}^m$ and $g$ is holomorphic in $\tau$, then $\partial u / \partial \bar \tau_j$ is the integral of $\partial g / \partial \bar\tau_j = 0$, so $u(z, \cdot)$ is holomorphic by Corollary P6.1.5.

*Proof of Theorem P6.1.10.* Identify $\mathbb{C}^n$ with $\mathbb{R}^{2n}$. Since $\partial F_i / \partial \bar z_j = 0$, the real differential of $F$ at $z$ is $v \mapsto J_F(z) v$, a complex linear map. The real determinant of a complex linear map $A$ is $|\det A|^2$: both sides are multiplicative and invariant under conjugation by $GL_n(\mathbb{C})$, so it suffices to treat an upper triangular $A$, whose real matrix is block upper triangular with $2 \times 2$ diagonal blocks $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ of determinant $a^2 + b^2 = |\lambda|^2$ for the diagonal entries $\lambda = a + ib$. So $dF_a$ is invertible, and the real inverse function theorem gives open sets $U' \ni a$ and $V' \ni F(a)$ such that $F \colon U' \to V'$ is a diffeomorphism with smooth inverse $G$. Its differential $dG_{F(z)} = (dF_z)^{-1}$ is complex linear. A real linear map $L \colon \mathbb{C}^n \to \mathbb{C}$ written as $L = \sum_j a_j dz_j + \sum_j b_j d\bar z_j$ is complex linear if and only if all $b_j = 0$, since $dz_j(iv) = i\, dz_j(v)$ and $d\bar z_j (iv) = -i\, d\bar z_j(v)$. Applied to $dG_k$ this gives $\partial G_k / \partial \bar w_j = 0$, so $G$ is holomorphic by Corollary P6.1.5.

For part 2 apply part 1 to $H(z, w) = (z, G(z, w))$, whose Jacobian at $(a,b)$ is block triangular with determinant $\det (\partial G_i / \partial w_j(a,b)) \neq 0$. It gives open sets $W \ni (a,b)$ and $W' \ni (a, 0)$ and a holomorphic inverse $K \colon W' \to W$, necessarily of the form $K(z, y) = (z, \psi(z, y))$. Choose $A \times B \subseteq W$ containing $(a,b)$, and shrink $A$ so that $(z, 0) \in W'$ and $\psi(z, 0) \in B$ for $z \in A$, which is possible because $\psi(a, 0) = b$. For $(z, w) \in A \times B$, $G(z,w) = 0$ means $H(z,w) = (z, 0)$, that is $(z, w) = K(z, 0)$, that is $w = \psi(z,0)$. So $\varphi(z) = \psi(z, 0)$ works.

*Verification of Example P6.1.11.* If $|z_1 z_2| < 1$, the series is geometric with ratio $z_1 z_2$. If $|z_1 z_2| \geq 1$, the terms have modulus at least $1$. A point with $|z_1 z_2| < 1$ and $z_1 z_2 \neq 0$ lies in $\Delta(0, (|z_1| t, |z_2| t))$ for any $1 < t < |z_1 z_2|^{-1/2}$, and $(|z_1| t)(|z_2| t) < 1$.

### Exercises

1. (A) Compute $\partial / \partial z_j$ and $\partial / \partial \bar z_j$ of $|z|^2$, of $\log |z|^2$ on $\mathbb{C}^n \setminus \{0\}$ and of $\bar z_1 z_2$, and verify that $\frac{\partial^2}{\partial z_j \partial \bar z_k} |z|^2 = \delta_{jk}$ and $\frac{\partial^2}{\partial \bar z_j \partial z_j} = \frac14 \bigl( \frac{\partial^2}{\partial x_j^2} + \frac{\partial^2}{\partial y_j^2} \bigr)$.
2. (A) Find the domains of convergence of $\sum_{k, l \geq 0} z_1^k z_2^l$ and of $\sum_{k \geq 0} (z_1 + z_2)^k$, and check part 3 of Theorem P6.1.4 on each. Show that the second domain contains no polydisc about $0$ of polyradius $(r_1, r_2)$ with $r_1 + r_2 > 1$.
3. (B) Prove Liouville's theorem on $\mathbb{C}^n$: a bounded holomorphic function on $\mathbb{C}^n$ is constant. More generally, show that if $|f(z)| \leq C (1 + |z|)^N$ on $\mathbb{C}^n$, then $f$ is a polynomial of degree at most $N$.
4. (B) (Schwarz lemma on the polydisc.) Let $f$ be holomorphic on the unit polydisc $\Delta = \Delta(0, (1, \dots, 1))$ with $|f| \leq 1$ and $f(0) = 0$. Show that $|f(z)| \leq \max_j |z_j|$ on $\Delta$. Show by an example that the maximum principle fails if $U$ is not connected.
5. (B) Let $F \colon U \to \mathbb{C}^n$ be holomorphic. Show that the real Jacobian determinant of $F$ is $|\det J_F|^2 \geq 0$, so that holomorphic maps preserve the orientation of $\mathbb{C}^n = \mathbb{R}^{2n}$. Show that $F(z_1, z_2) = (z_1, z_1 z_2)$ is holomorphic and bijective from $\{z_1 \neq 0\}$ onto itself, and that $J_F$ is singular on $\{z_1 = 0\}$.
6. (C) (Osgood's lemma.) Let $f \colon \Delta \to \mathbb{C}$ on a polydisc be holomorphic in each variable separately and locally bounded. Show that $f$ is continuous, hence holomorphic in the sense of Definition P6.1.1. Use the Cauchy estimate in one variable to obtain, for a holomorphic function $g$ on a disc of radius $r$ about $c$ with $|g| \leq M$, the estimate $|g(t) - g(s)| \leq 2 M r^{-1} |t - s|$ for $|t - c|, |s - c| \leq r/2$, and change one coordinate at a time.

### Lean

Mathlib has holomorphic functions of one complex variable, the Cauchy integral formula on circles, analytic functions of several variables as convergent multivariable power series, and the real inverse function theorem; it does not have the theory of several complex variables developed in this chapter. The handbook adds no `MinimalModel` node here.

### Notes and history

Power series and integral formulas in several variables go back to Cauchy and Weierstrass. Osgood (1899) observed that a continuous function that is holomorphic in each variable separately is holomorphic, and Exercise 6 is his lemma that local boundedness suffices. Hartogs (Har06) proved in 1906 that continuity is automatic: a function that is holomorphic in each variable separately is holomorphic. That theorem is harder and is not used in this volume, which takes continuity as part of Definition P6.1.1, following Huybrechts, Section 1.1 (Huy05), and Hörmander, Chapter II (Hor90). The Cauchy-Pompeiu formula is due to Pompeiu (1905); the fact that $1/(\pi z)$ is a fundamental solution of $\partial / \partial \bar z$ is the starting point of the $\bar\partial$-methods of Sections 1.2 and 1.4 and of the $L^2$ methods of Chapter 8. Example P6.1.11 is the simplest instance of the theorem that domains of convergence of power series are logarithmically convex complete Reinhardt domains (Hor90, Section II.2).
