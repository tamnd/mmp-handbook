---
title: Blow-ups and projective bundles
nodes: []
sources: [Laz04, Deb01, Har77, Kle66]
reads_with: [Laz04:1.1.C, Deb01:1.1, Har77:II.8, Har77:V.2]
requires: [P1.9, P3.6, P3.11, P4.4, P5.6, P5.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Blow-ups and projective bundles

### Statement

This section computes intersection numbers on the varieties that serve as examples for the rest of the volume: blow-ups of points and projective bundles over $\mathbb{P}^1$, which include the Hirzebruch surfaces. The tools are the cutting rule (part 6 of Theorem P7.1.6), the projection formula (Theorem P7.1.15) and asymptotic Riemann-Roch in several variables (part 1 of Theorem P7.1.17). For a projective bundle $\mathbb{P}(\mathcal{E}) = \operatorname{Proj} \operatorname{Sym} \mathcal{E}$ the convention is that of Definition P3.6.33, so that $\pi_* \mathcal{O}_{\mathbb{P}(\mathcal{E})}(1) = \mathcal{E}$ (Proposition P3.6.35).

**Proposition P7.1.23 (the blow-up of a point).** Let $X$ be a smooth projective variety of dimension $n \geq 2$, $p \in X$ a closed point and $\pi \colon \tilde X = \operatorname{Bl}_p X \to X$ the blow-up, with exceptional divisor $E = \pi^{-1}(p)$.

1. $\tilde X$ is a projective variety, $\pi$ is birational, $E$ is an effective Cartier divisor, $E \cong \mathbb{P}^{n-1}_k$, and $\mathcal{O}_{\tilde X}(-E)|_E \cong \mathcal{O}_{\mathbb{P}^{n-1}}(1)$.
2. For line bundles $L_1, \dots, L_n$ on $X$, $(\pi^* L_1 \cdots \pi^* L_n) = (L_1 \cdots L_n)$.
3. For $1 \leq j \leq n - 1$ and line bundles $L_1, \dots, L_{n-j}$ on $X$, $(\pi^* L_1 \cdots \pi^* L_{n-j} \cdot E^j) = 0$.
4. $E^n = (-1)^{n-1}$.
5. For a line bundle $L$ on $X$ and $b \in \mathbb{Z}$, $(\pi^* L - bE)^n = (L^n) - b^n$.
6. Let $e \subseteq E$ be a line of $E \cong \mathbb{P}^{n-1}$. Then $\pi^* L \cdot e = 0$ and $E \cdot e = -1$. If $C \subseteq X$ is a curve not through $p$, then $E \cdot \pi^{-1}(C) = 0$.

Lean: not in Lean as stated.

**Proposition P7.1.24 (split bundles over the line).** Let $a_0, \dots, a_{r-1} \in \mathbb{Z}$, $r \geq 2$, $\mathcal{E} = \mathcal{O}(a_0) \oplus \cdots \oplus \mathcal{O}(a_{r-1})$ on $\mathbb{P}^1$, $P = \mathbb{P}(\mathcal{E})$ with projection $\pi$, $\xi = \mathcal{O}_P(1)$ and $F = \pi^* \mathcal{O}_{\mathbb{P}^1}(1)$, the class of a fibre. Then $P$ is a smooth projective variety of dimension $r$, and
$$\xi^r = a_0 + \dots + a_{r-1} = \deg \mathcal{E}, \qquad \xi^{r-1} \cdot F = 1, \qquad \xi^{r-j} \cdot F^j = 0 \ \text{for } j \geq 2.$$

Lean: not in Lean as stated.

**Corollary P7.1.25 (the Hirzebruch surfaces).** On $\mathbb{F}_n = \mathbb{P}(\mathcal{O} \oplus \mathcal{O}(n))$, $n \geq 0$, with the curves $C_-$, $C_+$ and $F$ of Definition P3.11.24 and $\xi = \mathcal{O}(1) = \mathcal{O}(C_+)$,
$$C_+^2 = n, \quad C_+ \cdot F = 1, \quad F^2 = 0, \quad C_-^2 = -n, \quad C_- \cdot C_+ = 0, \quad C_- \cdot F = 1,$$
and $(aC_- + bF) \cdot (cC_- + dF) = -n ac + ad + bc$.

Lean: not in Lean as stated.

### Proof in words

On the blow-up, $E$ is a projective space on which $\mathcal{O}(E)$ restricts to $\mathcal{O}(-1)$, and every line bundle pulled back from $X$ restricts to the trivial bundle, because $E$ maps to a point. The cutting rule moves every intersection number that involves $E$ onto $E$, where it becomes an intersection number of copies of $\mathcal{O}(-1)$ and of trivial bundles on $\mathbb{P}^{n-1}$: it is $(-1)^{n-1}$ if only copies of $\mathcal{O}(-1)$ occur and zero otherwise. The numbers that do not involve $E$ are unchanged because $\pi$ is birational.

On a projective bundle over $\mathbb{P}^1$ the Euler characteristic of $\mathcal{O}_P(m) \otimes \pi^* \mathcal{O}(t)$ is the Euler characteristic of $\operatorname{Sym}^m \mathcal{E} \otimes \mathcal{O}(t)$ on $\mathbb{P}^1$, which for a split bundle is a sum of Euler characteristics of line bundles. Its homogeneous part of degree $r$ is computed by a symmetry argument, and asymptotic Riemann-Roch in two variables reads off all intersection numbers of $\xi$ and $F$ at once.

### Examples

**Example P7.1.26 (the blow-up of projective space at a point).** Let $X = \mathbb{P}^n$, $p = [1 : 0 : \dots : 0]$, $H$ the pullback of a hyperplane and $E$ the exceptional divisor on $\tilde X = \operatorname{Bl}_p \mathbb{P}^n$. By Proposition P7.1.23, $H^n = 1$, $H^{n-j} E^j = 0$ for $0 < j < n$, $E^n = (-1)^{n-1}$, and
$$(aH - bE)^n = a^n - b^n.$$
In particular $(H - E)^n = 0$. This has a geometric reason. The projection from $p$ is the morphism $\tilde X \to \mathbb{P}^{n-1}$, $([x], [u]) \mapsto [u]$, of the description $\tilde X = V_+(x_i u_j - x_j u_i : 1 \leq i < j \leq n) \subseteq \mathbb{P}^n \times \mathbb{P}^{n-1}$ obtained from Theorem P3.11.4 on the chart $x_0 \neq 0$. The pullback of a hyperplane $u_1 = 0$ of $\mathbb{P}^{n-1}$ is the strict transform of the hyperplane $x_1 = 0$ through $p$, whose class is $H - E$, so $H - E$ is pulled back from a variety of dimension $n - 1$ and $(H - E)^n = 0$ by Corollary P7.1.16. For curves: a line $\ell$ not through $p$ has $H \cdot \ell = 1$, $E \cdot \ell = 0$; a line $e \subseteq E$ has $H \cdot e = 0$, $E \cdot e = -1$; the strict transform $\tilde \ell_p$ of a line through $p$ meets $E$ transversally in one point and has $H \cdot \tilde \ell_p = 1$, $E \cdot \tilde \ell_p = 1$, so $(H - E) \cdot \tilde \ell_p = 0$: it is a fibre of the projection.

**Example P7.1.27 (the plane blown up at points).** Let $p_1, \dots, p_r \in \mathbb{P}^2$ be distinct and $S_r$ the blow-up of all of them, with exceptional curves $E_i$ and $H$ the pullback of a line. By Proposition P7.1.23 applied one point at a time, or by Example P5.6.8, $H^2 = 1$, $E_i^2 = -1$, $H \cdot E_i = 0$ and $E_i \cdot E_j = 0$ for $i \neq j$. So $(aH - \sum_i b_i E_i)^2 = a^2 - \sum_i b_i^2$. The strict transform of a line through $p_i$ and $p_j$ has class $H - E_i - E_j$ and self-intersection $-1$, and the strict transform of a conic through five of the points has class $2H - \sum_{i \in I} E_i$, $|I| = 5$, and self-intersection $4 - 5 = -1$. These are among the $(-1)$-curves of Theorem P5.9.26.

**Example P7.1.28 (rational normal scrolls).** Let $1 \leq a_0 \leq \dots \leq a_{r-1}$ and $\mathcal{E} = \bigoplus_i \mathcal{O}(a_i)$ on $\mathbb{P}^1$. Then $\mathcal{E}$ is generated by global sections and $H^0(\mathbb{P}^1, \mathcal{E}) = \bigoplus_i H^0(\mathcal{O}(a_i))$ has dimension $N + 1 = \sum_i (a_i + 1)$. The sections of $\xi$ are $H^0(P, \xi) = H^0(\mathbb{P}^1, \mathcal{E})$ by Proposition P3.6.35, and they define a morphism $\varphi \colon P \to \mathbb{P}^N$ whose image is the *rational normal scroll* $S(a_0, \dots, a_{r-1})$. When all $a_i \geq 1$ the morphism is a closed immersion, and by Proposition P7.1.24 the scroll has degree $\xi^r = \sum_i a_i$. The cubic scroll $S(1, 2) \subseteq \mathbb{P}^4$ is $\operatorname{Bl}_p \mathbb{P}^2$ embedded by the conics through $p$, of class $2H - E$, and indeed $(2H - E)^2 = 4 - 1 = 3$. The scroll $S(1, 1) \subseteq \mathbb{P}^3$ is the quadric, of degree $2$.

**Example P7.1.29 (the Hirzebruch surface $\mathbb{F}_1$).** By Theorem P3.11.26, $\mathbb{F}_1 = \operatorname{Bl}_p \mathbb{P}^2$, with $C_- = E$, $F = H - E$ and $C_+ = C_- + F = H$. Corollary P7.1.25 gives $C_+^2 = 1 = H^2$, $C_-^2 = -1 = E^2$, $F^2 = (H - E)^2 = 0$, in agreement with Example P7.1.26 for $n = 2$. In general the two computations of Corollary P7.1.25 and Proposition P5.9.9 agree: the class of $\mathcal{O}(1)$ is $C_+ \sim C_- + nF$ with $C_+^2 = n$.

### Proof

*Proposition P7.1.23.* Part 1. Let $\mathcal{I}$ be the ideal sheaf of $p$. The blow-up is $\operatorname{Proj}_X \bigoplus_{d \geq 0} \mathcal{I}^d$, which is projective over $X$ and so projective over $k$; it is integral and $\pi$ is birational by part 4 of Theorem P3.11.3. By part 2 of the same theorem, $\mathcal{I} \mathcal{O}_{\tilde X} = \mathcal{O}_{\tilde X}(1)$ is invertible, and it is the ideal sheaf of $E$, so $\mathcal{O}_{\tilde X}(-E) = \mathcal{O}_{\tilde X}(1)$. The exceptional divisor is the closed subscheme $\operatorname{Proj} \bigl( \bigoplus_d \mathcal{I}^d \otimes \mathcal{O}_X / \mathcal{I} \bigr) = \operatorname{Proj} \bigoplus_d \mathfrak{m}^d / \mathfrak{m}^{d+1}$, where $\mathfrak{m}$ is the maximal ideal of $\mathcal{O}_{X, p}$. Since $X$ is smooth at $p$, $\mathcal{O}_{X, p}$ is regular of dimension $n$, and by Theorem P1.9.2 the associated graded ring is the polynomial ring $k[T_1, \dots, T_n]$. So $E \cong \mathbb{P}^{n-1}_k$, and $\mathcal{O}_{\tilde X}(1)|_E = \mathcal{O}_E(1)$. That $\tilde X$ is smooth along $E$ is not needed below; it follows from Theorem P3.11.4 applied to a regular system of parameters at $p$, as in Hartshorne, Theorem II.8.24.

Part 2 is Corollary P7.1.16, because $\pi$ is birational. For parts 3 and 4, let $s_E$ be the canonical section of $\mathcal{O}_{\tilde X}(E)$. It does not vanish at the generic point of $\tilde X$, the only associated point of $\mathcal{O}_{\tilde X}$, and its cokernel is $\mathcal{O}_E$. By part 6 of Theorem P7.1.6 with $L_n = \mathcal{O}(E)$, and part 7,
$$(\pi^* L_1 \cdots \pi^* L_{n-j} \cdot E^j) = \bigl( \pi^* L_1|_E \cdots \pi^* L_{n-j}|_E \cdot \mathcal{O}_E(E)^{j-1} \bigr)_E.$$
The composite $E \to X$ factors through $\operatorname{Spec} \kappa(p) = \operatorname{Spec} k$, so $\pi^* L_i|_E$ is pulled back from a point and is trivial. If $j \leq n - 1$, at least one of the bundles on the right is trivial, and the number is $0$ by part 4 of Theorem P7.1.6. If $j = n$, the right side is $(\mathcal{O}_{\mathbb{P}^{n-1}}(-1)^{n-1}) = (-1)^{n-1}$ by Example P7.1.8 and multilinearity. Part 5 follows by expanding $(\pi^* L - bE)^n$ by multilinearity and symmetry: only the terms $j = 0$ and $j = n$ survive, and they give $(L^n) + (-b)^n (-1)^{n-1} = (L^n) - b^n$.

Part 6. The curve $e$ maps to the point $p$, so $\pi^* L \cdot e = \deg (\pi^* L|_e) = 0$ by part 2 of Proposition P7.1.7, and $E \cdot e = \deg \mathcal{O}_E(E)|_e = \deg \mathcal{O}_{\mathbb{P}^1}(-1) = -1$. A curve $\pi^{-1}(C)$ with $p \notin C$ is disjoint from $E$, so $\mathcal{O}(E)$ is trivial on it. $\square$

*Proposition P7.1.24.* Locally over $\mathbb{P}^1$, $P \cong \mathbb{P}^{r-1} \times U$ by part 3 of Proposition P3.6.35, so $P$ is smooth, integral and of dimension $r$; it is projective over $\mathbb{P}^1$ and so over $k$. Let $m > -r$ and $t \in \mathbb{Z}$. By part 4 of Theorem P4.4.14 with $\mathcal{G} = \mathcal{O}(t)$,
$$\chi(P, \xi^m \otimes F^t) = \chi(\mathbb{P}^1, \operatorname{Sym}^m \mathcal{E} \otimes \mathcal{O}(t)).$$
For $m \geq 0$, $\operatorname{Sym}^m \mathcal{E} = \bigoplus_{\mathbf{b}} \mathcal{O}(\mathbf{b} \cdot \mathbf{a})$, the sum over $\mathbf{b} \in \mathbb{Z}_{\geq 0}^r$ with $|\mathbf{b}| = m$, where $\mathbf{b} \cdot \mathbf{a} = \sum_i b_i a_i$. By Theorem P4.2.1, $\chi(\mathbb{P}^1, \mathcal{O}(c)) = c + 1$ for every $c$. Let $N_m = \binom{m + r - 1}{r - 1}$ be the number of such $\mathbf{b}$. By symmetry in the coordinates, $\sum_{|\mathbf{b}| = m} b_i$ is the same for every $i$, and summing over $i$ gives $m N_m$, so each is $m N_m / r$. Hence
$$\chi(P, \xi^m \otimes F^t) = \sum_{|\mathbf{b}| = m} (\mathbf{b} \cdot \mathbf{a} + t + 1) = N_m (t + 1) + \frac{m N_m}{r} \deg \mathcal{E}$$
for $m \geq 0$, and both sides are polynomials in $(m, t)$, by Theorem P7.1.4 for the left side, so the identity holds for all $m, t$. Since $N_m = \frac{m^{r-1}}{(r-1)!} + O(m^{r-2})$, the homogeneous part of degree $r$ of the right side is
$$\frac{m^{r-1} t}{(r-1)!} + \frac{\deg \mathcal{E}}{r!} m^r.$$
By part 1 of Theorem P7.1.17 with $L_1 = \xi$, $L_2 = F$, this part is $\sum_{j=0}^{r} \frac{(\xi^{r-j} \cdot F^j)}{(r-j)! \, j!} m^{r-j} t^j$. Comparing coefficients gives $\xi^r = \deg \mathcal{E}$, $\xi^{r-1} \cdot F = 1$ and $\xi^{r-j} \cdot F^j = 0$ for $j \geq 2$. $\square$

*Corollary P7.1.25.* Proposition P7.1.24 with $r = 2$, $a_0 = 0$, $a_1 = n$ gives $\xi^2 = n$, $\xi \cdot F = 1$, $F^2 = 0$. By part 2 of Proposition P5.9.9, $\xi = \mathcal{O}(C_+)$ and $C_+ \sim C_- + nF$ (part 3 of Theorem P3.11.25). So $C_- = \xi - nF$ in $\operatorname{Pic}$, $C_-^2 = n - 2n = -n$, $C_- \cdot F = 1$ and $C_- \cdot C_+ = n - n = 0$, consistent with the disjointness of $C_-$ and $C_+$. The general formula follows by bilinearity. $\square$

### Exercises

1. (A) On $\operatorname{Bl}_p \mathbb{P}^3$, compute $(2H - E)^3$, $H^2 \cdot E$ and $H \cdot E^2$, and the intersection numbers of $H$ and $E$ with a line in $E$ and with the strict transform of a line through $p$.
2. (A) On $\mathbb{F}_n$, compute $K^2$ for $K = -2C_- - (n + 2) F$ and check that it is $8$ for every $n$, as in Proposition P5.9.9.
3. (B) Let $X$ be smooth projective of dimension $n$ and $\tilde X$ the blow-up of two distinct points $p_1$, $p_2$, with exceptional divisors $E_1$, $E_2$. Show that $E_1 \cdot E_2 \cdot D_3 \cdots D_n = 0$ for all divisors $D_i$, and compute $(\pi^* L - E_1 - E_2)^n$.
4. (B) Let $P = \mathbb{P}(\mathcal{O} \oplus \mathcal{O} \oplus \mathcal{O}(1))$ over $\mathbb{P}^1$. Show that $\xi$ is generated by global sections, that the morphism it defines maps $P$ birationally onto $\mathbb{P}^3$ and contracts the surface $\mathbb{P}(\mathcal{O} \oplus \mathcal{O}) \cong \mathbb{P}^1 \times \mathbb{P}^1$ to a line, and use $\xi^3 = 1$ to compute the degree of the image.
5. (B) Let $\mathcal{E}$ be a vector bundle of rank $r$ on $\mathbb{P}^1$ and $\mathcal{L} = \mathcal{O}(c)$. Using part 2 of Proposition P3.6.35, show that $\xi_{\mathcal{E} \otimes \mathcal{L}}$ corresponds to $\xi_{\mathcal{E}} + cF$, and check that Proposition P7.1.24 is compatible: $(\xi + cF)^r = \deg \mathcal{E} + rc$.
6. (C) Let $X$ be smooth projective of dimension $n$ and $Z \subseteq X$ a smooth subvariety of dimension $z$ and codimension $c \geq 2$, with blow-up $\pi \colon \tilde X \to X$ and exceptional divisor $E = \mathbb{P}(N^\vee)$ over $Z$, where $N$ is the normal bundle. Assuming $\mathcal{O}_E(-E) = \mathcal{O}_{\mathbb{P}(N^\vee)}(1)$, show that $(\pi^* L)^{n-j} \cdot E^j = 0$ for $1 \leq j < c$, and that $(\pi^* L)^{z} \cdot E^c = (-1)^{c-1} (L^z \cdot Z)$.

### Lean

Mathlib has neither blow-ups nor projective bundles of vector bundles, so none of these computations is in Mathlib. The project library does not compute intersection numbers on specific varieties. The handbook adds no `MinimalModel` node here.

### Notes and history

The formula $E^n = (-1)^{n-1}$ and the vanishing of the mixed terms are the higher-dimensional form of $E^2 = -1$ on a surface (Theorem P5.6.3). The computation of $\xi^r = \deg \mathcal{E}$ is the first case of the Grothendieck relation $\sum_i (-1)^i \pi^* c_i(\mathcal{E}) \xi^{r-i} = 0$ that defines the Chern classes of $\mathcal{E}$; on a split bundle over $\mathbb{P}^1$ it reads $\xi^r = c_1(\mathcal{E}) \xi^{r-1}$, which is what the proof checks. Rational normal scrolls are classical, and they are the varieties of minimal degree together with the quadrics, the cones over them and the Veronese surface, by a theorem of del Pezzo and Bertini. The literature state of every statement here is theorem. In the minimal model program, the blow-up of a point of a smooth threefold is the basic divisorial contraction, with $E \cong \mathbb{P}^2$ and $E^3 = 1$, and the projective bundles over curves are the basic Mori fibre spaces.
