---
title: Mixed multiplier ideals of monomial ideals
nodes: []
sources: [How01, Laz04, CLS11, KM98]
reads_with: [How01:main-theorem, Laz04:ch9, CLS11:ch11]
requires: [P7.10, P8.7, P8.8, 4.6]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Mixed multiplier ideals of monomial ideals

### Statement

Several ideals with independent exponents appear when two linear systems are perturbed at once, and a boundary appears whenever the pair is not the variety alone. Both are handled by mixed multiplier ideals. On affine space with a boundary on the coordinate hyperplanes and monomial ideals, the toric computation of Theorem P7.10.17 extends with one change: the shift by $\mathbf{1}$ becomes a shift by $\mathbf{1} - d$, where $d$ records the boundary.

**Definition 5.3.14 (mixed multiplier ideals).** Let $(X, \Delta)$ be a pair, $\mathfrak{a}_1, \dots, \mathfrak{a}_r$ nonzero ideals and $c_1, \dots, c_r \geq 0$ rational. Let $\mu \colon Y \to X$ be a log resolution of $(X, \Delta; \mathfrak{a}_1 \cdots \mathfrak{a}_r)$ on which every $\mathfrak{a}_i \mathcal{O}_Y = \mathcal{O}_Y(-F_i)$ is invertible, with $\operatorname{Exc}(\mu) + \mu^{-1}_* \Delta + \sum_i F_i$ of snc support. Put
$$\mathcal{J}(X, \Delta; \mathfrak{a}_1^{c_1} \cdots \mathfrak{a}_r^{c_r}) = \mu_* \mathcal{O}_Y\Big(-\big\lfloor \Delta_Y + \textstyle\sum_i c_i F_i \big\rfloor\Big).$$

Since $\sum_i c_i F_i$ is an effective $\mathbb{Q}$-divisor with snc support, the proofs of Proposition 5.3.2, Proposition 5.3.3 and Theorem 5.3.5 apply verbatim with $cF$ replaced by $\sum_i c_i F_i$: the mixed ideal is an ideal, it does not depend on $\mu$, it is $\mathcal{O}_X$ exactly when every coefficient of $\Delta_Y + \sum_i c_i F_i$ is less than $1$, and its higher direct images from a projective log resolution vanish. For $c_1 = \dots = c_r = c$ it equals $\mathcal{J}(X, \Delta; (\mathfrak{a}_1 \cdots \mathfrak{a}_r)^c)$, since $(\mathfrak{a}_1 \cdots \mathfrak{a}_r) \mathcal{O}_Y = \mathcal{O}_Y(-\sum_i F_i)$.

On $X = \mathbb{A}^n$ with coordinates $x_1, \dots, x_n$, let $H_j = \{x_j = 0\}$, $\sigma = \mathbb{R}^n_{\geq 0}$, and for a monomial ideal $\mathfrak{a}$ let $P(\mathfrak{a})$ and $\varphi_{\mathfrak{a}}$ be the Newton polyhedron and its support function of Definition 4.6.10, with $P(\mathcal{O}) = \sigma$ and $\varphi_{\mathcal{O}} = 0$. For $d = (d_1, \dots, d_n) \in \mathbb{Q}^n_{\geq 0}$ put $\Delta_d = \sum_j d_j H_j$, so $(\mathbb{A}^n, \Delta_d)$ is a pair.

**Theorem 5.3.15 (mixed monomial multiplier ideals).** Let $\mathfrak{a}_1, \dots, \mathfrak{a}_r$ be nonzero monomial ideals, $c_1, \dots, c_r \geq 0$ rational, $d \in \mathbb{Q}^n_{\geq 0}$, and $P_c = \sum_i c_i P(\mathfrak{a}_i)$ the Minkowski sum, with $P_c = \sigma$ if every $c_i = 0$. Then
$$\mathcal{J}(\mathbb{A}^n, \Delta_d; \mathfrak{a}_1^{c_1} \cdots \mathfrak{a}_r^{c_r}) = \big( x^v : v \in \mathbb{Z}^n_{\geq 0}, \ v + \mathbf{1} - d \in \operatorname{Int}(P_c) \big).$$

Lean: not yet in Lean.

**Corollary 5.3.16 (thresholds with a toric boundary).** Let $\mathfrak{a} \neq (1)$ be a nonzero monomial ideal and $d \in \mathbb{Q}^n$ with $0 \leq d_j < 1$. Then
$$\operatorname{lct}(\mathbb{A}^n, \Delta_d; \mathfrak{a}) = \max\{ c \geq 0 : \mathbf{1} - d \in c P(\mathfrak{a}) \} = \min\Big\{ \frac{\langle \mathbf{1} - d, u \rangle}{\varphi_{\mathfrak{a}}(u)} : u \in \sigma \cap \mathbb{Z}^n, \ \varphi_{\mathfrak{a}}(u) > 0 \Big\},$$
and the multiplier ideal $\mathcal{J}(\mathbb{A}^n, \Delta_d; \mathfrak{a}^c)$ is $\mathcal{O}$ exactly for $c$ below this number. For $d = 0$ this is Corollary P7.10.18 and Theorem 4.6.11.

Lean: not yet in Lean.

### Proof in words

A common smooth refinement of the normal fans of all the Newton polyhedra gives one toric log resolution for every ideal and for the coordinate hyperplanes, and on it every divisor in sight is torus invariant. The crepant pullback of $K + \Delta_d$ is computed from the torus-invariant form $\frac{dx_1}{x_1} \wedge \dots \wedge \frac{dx_n}{x_n}$, and contributes $1 - \langle \mathbf{1} - d, u_\rho \rangle$ along the divisor of the ray $u_\rho$; the ideals contribute $\sum_i c_i \varphi_i(u_\rho)$, which is the support function of the Minkowski sum $P_c$. The condition for a monomial to lie in the push-forward is then the inequality $\langle v + \mathbf{1} - d, u_\rho \rangle > \varphi_{P_c}(u_\rho)$ for every ray, by the same integer rounding as in Theorem P7.10.17, and the rays cut out the interior of $P_c$. The threshold is the first $c$ at which $\mathbf{1} - d$ leaves the interior of $cP(\mathfrak{a})$.

### Examples

**Example 5.3.17 (the ideal $(x^2, y^3)$ with a boundary line).** Let $\mathfrak{a} = (x^2, y^3) \subseteq k[x, y]$, so $P(\mathfrak{a}) = \{ p \geq 0 : \frac{p_1}{2} + \frac{p_2}{3} \geq 1 \}$ (Example P7.10.19), and $\Delta = d_1 H_1$ with $H_1 = \{x = 0\}$ and $0 \leq d_1 < 1$. The point $\mathbf{1} - d = (1 - d_1, 1)$ lies in $cP(\mathfrak{a})$ if and only if $\frac{1 - d_1}{2} + \frac13 \geq c$, so
$$\operatorname{lct}(\mathbb{A}^2, d_1 H_1; \mathfrak{a}) = \frac{5 - 3 d_1}{6}.$$
For $d_1 = \frac12$ the monomial $x^a y^b$ lies in $\mathcal{J}(\mathbb{A}^2, \frac12 H_1; \mathfrak{a}^c)$ if and only if $\frac{a + 1/2}{2} + \frac{b + 1}{3} > c$. The left side is $\frac{7}{12}$ at $(0, 0)$, $\frac{11}{12}$ at $(0, 1)$, $\frac{13}{12}$ at $(1, 0)$, $\frac54$ at $(0, 2)$, $\frac{17}{12}$ at $(1, 1)$ and $\frac{19}{12}$ at $(2, 0)$, so
$$\mathcal{J}\big(\mathbb{A}^2, \tfrac12 H_1; \mathfrak{a}^c\big) = \begin{cases} (1) & c < \frac{7}{12}, \\ (x, y) & \frac{7}{12} \leq c < \frac{11}{12}, \\ (x, y^2) & \frac{11}{12} \leq c < \frac{13}{12}, \\ (x^2, xy, y^2) & \frac{13}{12} \leq c < \frac54. \end{cases}$$
Compared with Example P7.10.19, where $d_1 = 0$, the boundary moves every jump down by $\frac14$, the amount $\frac{d_1}{2}$ by which it shifts the $x$-coordinate of $\mathbf{1}$, measured by the facet $\frac{p_1}{2} + \frac{p_2}{3} = c$.

**Example 5.3.18 (two ideals with independent exponents).** Let $\mathfrak{a}_1 = (x^2, y)$ and $\mathfrak{a}_2 = (x, y^2)$ in $k[x, y]$. Then $P(\mathfrak{a}_1) = \{ p \geq 0 : p_1 + 2 p_2 \geq 2 \}$ and $P(\mathfrak{a}_2) = \{ p \geq 0 : 2 p_1 + p_2 \geq 2 \}$, with support functions $\varphi_1(1, 2) = 2$, $\varphi_1(2, 1) = 1$, $\varphi_2(1, 2) = 1$, $\varphi_2(2, 1) = 2$, and $\varphi_i(e_j) = 0$. The rays $e_1$, $e_2$, $(1, 2)$ and $(2, 1)$ generate a fan on which both support functions are linear, and
$$c_1 P(\mathfrak{a}_1) + c_2 P(\mathfrak{a}_2) = \{ p \geq 0 : p_1 + 2 p_2 \geq 2 c_1 + c_2, \ 2 p_1 + p_2 \geq c_1 + 2 c_2 \}.$$
By Theorem 5.3.15 with $d = 0$, $\mathcal{J}(\mathbb{A}^2; \mathfrak{a}_1^{c_1} \mathfrak{a}_2^{c_2}) = \mathcal{O}$ if and only if $\mathbf{1}$ is interior, that is,
$$2 c_1 + c_2 < 3 \quad \text{and} \quad c_1 + 2 c_2 < 3.$$
The klt region is a quadrilateral with vertices $(0, 0)$, $(\frac32, 0)$, $(1, 1)$ and $(0, \frac32)$. On the axes it gives $\operatorname{lct}(\mathfrak{a}_i) = \frac32$, which is Corollary P7.10.18, and on the diagonal $c_1 = c_2 = c$ it gives $c < 1$, the threshold of the product $\mathfrak{a}_1 \mathfrak{a}_2 = (x^3, xy, y^3)$, whose Newton polyhedron $\{ p_1 + 2p_2 \geq 3, 2p_1 + p_2 \geq 3 \}$ is the Minkowski sum. The region is not the product of the two intervals $[0, \frac32)$: the two ideals share the valuations of the rays $(1, 2)$ and $(2, 1)$, so they compete.

**Example 5.3.19 (the maximal ideal of $\mathbb{A}^3$ with three planes).** Let $\mathfrak{m} = (x, y, z)$, $\Delta = t(H_1 + H_2 + H_3)$ with $0 \leq t < 1$, so $d = (t, t, t)$. By Example P7.10.20, $P(\mathfrak{m}) = \{ p \geq 0 : |p| \geq 1 \}$, and Theorem 5.3.15 gives $x^v \in \mathcal{J}(\mathbb{A}^3, \Delta; \mathfrak{m}^c)$ if and only if $|v| + 3 - 3t > c$, so
$$\mathcal{J}(\mathbb{A}^3, \Delta; \mathfrak{m}^c) = \mathfrak{m}^{\max(0, \lfloor c + 3t \rfloor - 2)}, \qquad \operatorname{lct}(\mathbb{A}^3, \Delta; \mathfrak{m}) = 3(1 - t).$$
Directly: on the blow-up $\mu$ of the origin, with exceptional divisor $E \cong \mathbb{P}^2$, the strict transforms $H'_j$ meet $E$ in the three sides of a triangle, so $\mu$ is a log resolution, $K_Y = \mu^* K + 2E$, $\mu^* H_j = H'_j + E$ and $\mathfrak{m} \mathcal{O}_Y = \mathcal{O}_Y(-E)$. So $\Delta_Y + cF = t \sum_j H'_j + (3t - 2 + c) E$, the round-down is $\lfloor c + 3t - 2 \rfloor E$ for $t < 1$, and $\mu_* \mathcal{O}_Y(-kE) = \mathfrak{m}^k$ for $k \geq 0$. The two computations agree.

### Proof

*Theorem 5.3.15.* For each $i$ with $\mathfrak{a}_i \neq \mathcal{O}$, the proof of Theorem 4.6.11 gives a fan with support $\sigma$ on whose cones $\varphi_i = \varphi_{\mathfrak{a}_i}$ is linear; let $\Sigma_0$ be a common refinement of these fans, which is again a fan with support $\sigma$ on whose cones every $\varphi_i$ is linear, and $\Sigma$ a smooth refinement of $\Sigma_0$, by Theorem P8.8.4. Let $\mu \colon Y = X_\Sigma \to \mathbb{A}^n$ be the toric morphism, proper and birational by Proposition P8.8.2. As in the proof of Theorem P7.10.17, the rays of $\Sigma$ include the coordinate rays, $\mathfrak{a}_i \mathcal{O}_Y = \mathcal{O}_Y(-F_i)$ with $F_i = \sum_\rho \varphi_i(u_\rho) D_\rho$, and the torus-invariant divisors $D_\rho$ form an snc divisor containing $\operatorname{Exc}(\mu)$ and the strict transforms of the $H_j$. So $\mu$ is a log resolution of $(\mathbb{A}^n, \Delta_d; \mathfrak{a}_1 \cdots \mathfrak{a}_r)$, and by Proposition 5.3.2 for mixed ideals it computes the mixed multiplier ideal.

Let $\omega = \frac{dx_1}{x_1} \wedge \dots \wedge \frac{dx_n}{x_n}$. On $\mathbb{A}^n$, $\operatorname{div}(\omega) = -\sum_j H_j$, so $K_{\mathbb{A}^n} + \Delta_d$ is represented by $-\sum_j (1 - d_j) H_j$. On $Y$, $\operatorname{div}(\omega) = -\sum_\rho D_\rho$ by Theorem P8.7.17, and $\mu^* H_j = \operatorname{div}(x_j) = \sum_\rho \langle e_j, u_\rho \rangle D_\rho$ by part 3 of Lemma P8.7.2. With $K_Y$ represented by $\operatorname{div}(\omega)$,
$$\Delta_Y = \mu^*(K_{\mathbb{A}^n} + \Delta_d) - K_Y = \sum_\rho \big(1 - \langle \mathbf{1} - d, u_\rho \rangle\big) D_\rho.$$
The support function of $P_c$ is $\varphi_c = \sum_i c_i \varphi_i$, because the minimum of a linear form on a Minkowski sum is the sum of the minima. So
$$-\Big\lfloor \Delta_Y + \sum_i c_i F_i \Big\rfloor = \sum_\rho a_\rho D_\rho, \qquad a_\rho = \langle \mathbf{1}, u_\rho \rangle - 1 - \big\lfloor \langle d, u_\rho \rangle + \varphi_c(u_\rho) \big\rfloor,$$
using that $\langle \mathbf{1}, u_\rho \rangle$ is an integer. By Proposition P8.7.3 the global sections are spanned by the monomials $x^v$, $v \in \mathbb{Z}^n$, with $\langle v, u_\rho \rangle \geq -a_\rho$ for every ray, that is, $\langle v + \mathbf{1}, u_\rho \rangle - 1 \geq \lfloor \langle d, u_\rho \rangle + \varphi_c(u_\rho) \rfloor$. The left side is an integer, so this holds if and only if
$$\langle v + \mathbf{1} - d, u_\rho \rangle > \varphi_c(u_\rho) \quad \text{for every } \rho \in \Sigma(1).$$
For the coordinate ray $e_j$ it says $v_j + 1 - d_j > \varphi_c(e_j) \geq 0$, so $v_j > d_j - 1 \geq -1$ and $v \in \mathbb{Z}^n_{\geq 0}$. Since every $\varphi_i$, and hence $\varphi_c$, is linear on the cones of $\Sigma$, the last paragraph of the proof of Theorem P7.10.17 applies to the polyhedron $P_c$ with support function $\varphi_c$, in place of $cP(\mathfrak{a})$ with $c\varphi$: the closed half-spaces $\langle w, u_\rho \rangle \geq \varphi_c(u_\rho)$ cut out $P_c$, and the strict inequalities cut out its interior. So the conditions say $v + \mathbf{1} - d \in \operatorname{Int}(P_c)$. If every $c_i = 0$, $\varphi_c = 0$ and the same argument gives $\operatorname{Int}(\sigma)$, as the convention $P_c = \sigma$ requires.

*Corollary 5.3.16.* By Proposition 5.3.3, part 1, for mixed ideals and Theorem 5.3.15 with $v = 0$, the ideal is $\mathcal{O}$ if and only if $\mathbf{1} - d \in \operatorname{Int}(cP(\mathfrak{a}))$. Since $P(\mathfrak{a}) + \sigma = P(\mathfrak{a})$ and $0 \notin P(\mathfrak{a})$, the sets $cP(\mathfrak{a})$ decrease as $c$ increases, so the set of $c$ with $\mathbf{1} - d \in \operatorname{Int}(cP(\mathfrak{a}))$ is an interval $[0, c_0)$, and $c_0 = \max\{c : \mathbf{1} - d \in cP(\mathfrak{a})\}$, which is positive because $\mathbf{1} - d$ has positive coordinates. The description of $cP(\mathfrak{a})$ by the inequalities $\langle w, u \rangle \geq c \varphi_{\mathfrak{a}}(u)$ for $u \in \sigma \cap \mathbb{Z}^n$ gives the minimum formula. The threshold of Definition 4.6.2 is the supremum of the $c$ for which the triple is lc, and the klt condition holds exactly below $c_0$ and fails at $c_0$, since at $c_0$ the inequality for some ray is an equality, a coefficient equal to $1$; above $c_0$ that coefficient exceeds $1$. So the threshold is $c_0$.

### Exercises

1. (A) Use Theorem 5.3.15 with every $c_i = 0$ to show that $\mathcal{J}(\mathbb{A}^n, \Delta_d) = (x^v : v_j \geq \lfloor d_j \rfloor)$, and compare with part 2 of Proposition P7.10.4.
2. (A) In Example 5.3.17, compute $\operatorname{lct}(\mathbb{A}^2, d_2 H_2; \mathfrak{a})$ for a boundary $d_2 H_2$ on the other axis, and find for which $(d_1, d_2)$ the pair $(\mathbb{A}^2, d_1 H_1 + d_2 H_2)$ with $\mathfrak{a}^c$, $c = \frac12$, is klt.
3. (B) In Example 5.3.18, compute $\mathcal{J}(\mathbb{A}^2; \mathfrak{a}_1^{c_1} \mathfrak{a}_2^{c_2})$ for $(c_1, c_2) = (1, 1)$ and $(c_1, c_2) = (\frac32, 0)$, and show that both are the maximal ideal.
4. (B) Show that Theorem 5.3.15 implies $\mathcal{J}(\mathbb{A}^n, \Delta_{d + e_j}; \mathfrak{a}^c) = x_j \cdot \mathcal{J}(\mathbb{A}^n, \Delta_d; \mathfrak{a}^c)$, and check that this is part 3 of Proposition 5.3.3 for $B = H_j$.
5. (B) Let $\mathfrak{a} = (x^a, y^b)$ and $\Delta = d_1 H_1 + d_2 H_2$ with $0 \leq d_i < 1$. Show that $\operatorname{lct}(\mathbb{A}^2, \Delta; \mathfrak{a}) = \frac{1 - d_1}{a} + \frac{1 - d_2}{b}$.
6. (C) Show from Definition 5.3.14 that $\mathcal{J}(\mathfrak{a}_1^{c_1} \mathfrak{a}_2^{c_2}) \subseteq \mathcal{J}(\mathfrak{a}_1^{c_1}) \cap \mathcal{J}(\mathfrak{a}_2^{c_2})$ for any two nonzero ideals, and show by computing both sides in Example 5.3.18 for $(c_1, c_2) = (1, 1)$ that the inclusion can be strict. Compare with the subadditivity theorem, Theorem P7.10.12.

### Lean

The library has toric varieties and fans but no multiplier ideals and no Newton polyhedra of ideals. Theorem 5.3.15 and Corollary 5.3.16 are not yet in Lean.

### Notes and history

Howald computed the multiplier ideals of a monomial ideal (How01), which is Theorem P7.10.17 in Volume P7, and Lazarsfeld, Section 9.3.C (Laz04), gives the proof by toric resolution. The mixed version and the toric boundary are routine extensions of the same argument and are stated in this form in the literature on mixed multiplier ideals and on toric pairs; the boundary enters only through the crepant pullback of $K + \Delta_d$, which shifts the point $\mathbf{1}$ to $\mathbf{1} - d$. The klt region of Example 5.3.18 is the simplest instance of a region of mixed log canonical thresholds, the set of exponents for which several boundaries can be added at once while the pair stays klt.
