---
title: Cones over smooth varieties
nodes: []
sources: [Kol13, KM98, Rei87]
reads_with: [Kol13:ch3, Rei87:ch3]
requires: [P8.12, 4.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Cones over smooth varieties

### Statement

Cones give the first large family of singularities in which every class of Section 2.1 occurs, and in which one number decides the class. This section computes that number.

Let $V$ be a smooth projective variety of dimension $n - 1 \ge 1$ and $L$ an ample line bundle on $V$. The *cone* over $V$ with respect to $L$ is

$$X = C(V, L) = \operatorname{Spec} R, \qquad R = \bigoplus_{m \ge 0} H^0(V, L^m).$$

The *vertex* is the point $0 \in X$ of the ideal $\bigoplus_{m \ge 1} H^0(V, L^m)$. Let $Y = \operatorname{Spec}_V \bigoplus_{m \ge 0} L^m$, the total space of the line bundle $L^{-1}$, with projection $p \colon Y \to V$ and zero section $E \cong V$. The following facts are in Kol13, Chapter 3, and this section uses them as a black box.

1. $R$ is a finitely generated normal domain of dimension $n$, so $X$ is a normal affine variety.
2. $H^0(Y, \mathcal{O}_Y) = R$, and the morphism $f \colon Y \to X$ it gives is proper and birational. It maps $E$ to the vertex and is an isomorphism from $Y \setminus E$ onto $X \setminus \{0\}$.
3. If $L$ is very ample and $V \subset \mathbb{P}^N$ by $L$ is projectively normal, then $X$ is the affine cone over $V$ in $\mathbb{A}^{N+1}$, and $f$ is the strict transform of $X$ in the blow-up of the origin.

So $f$ is a resolution of $X$ with one exceptional divisor $E$, and $E$ is smooth. Two more facts are simple computations, and the proof checks them: $\mathcal{O}_Y(-E) \cong p^* L$, and $K_Y \sim p^*(K_V + L)$, so $K_Y \sim p^* K_V - E$.

**Theorem 4.2.19 (the discrepancy of a cone).** Let $X = C(V, L)$ as above.

1. $K_X$ is $\mathbb{Q}$-Cartier if and only if $K_V \sim_{\mathbb{Q}} rL$ for some $r \in \mathbb{Q}$. If $m K_X$ is Cartier, then $m K_V \sim m r L$ with $m r \in \mathbb{Z}$.
2. In that case $K_Y = f^* K_X + a E$ with
$$a = a(E, X, 0) = -1 - r.$$
3. In that case $f$ is a log resolution of $(X, 0)$, and $\operatorname{discrep}(X, 0) = \min\{a, 1\}$. So $X$ is terminal if and only if $a > 0$, canonical if and only if $a \ge 0$, klt if and only if $a > -1$, and lc if and only if $a \ge -1$.

Lean: not yet in Lean.

**Corollary 4.2.20 (cones over curves).** Let $V$ be a smooth projective curve of genus $g$ and $L$ a line bundle of degree $d > 0$, and suppose that $K_X$ is $\mathbb{Q}$-Cartier. Then
$$a(E, X, 0) = -1 - \frac{2g - 2}{d}.$$
So $X$ is klt if and only if $g = 0$, and lc if and only if $g \le 1$. For $g = 0$ it is canonical if and only if $d \le 2$, and terminal if and only if $d = 1$, where $X \cong \mathbb{A}^2$. The condition on $K_X$ holds for every $L$ when $g \le 1$.

Lean: not yet in Lean.

For a curve, Section 3.1 removes the condition on $K_X$: the numerical pullback of Mumford gives the same formula for every $L$, even when $K_X$ is not $\mathbb{Q}$-Cartier.

### Proof in words

The zero section $E$ of $Y$ has normal bundle $L^{-1}$, and the ideal of $E$ is the part of degree at least 1 of $\bigoplus L^m$, which is $p^*L$. So $-E$ is the pullback of $L$, and the relative canonical bundle of a line bundle is the dual of the line bundle. This gives $K_Y \sim p^*K_V - E$. If $K_V$ is $r$ times $L$ up to torsion, then $K_Y$ is $-(1 + r)E$ up to torsion, so $m K_Y + m(1 + r)E$ is the divisor of a rational function $h$. Its pushforward $m K_X$ is the divisor of $h$, and so $K_X$ is $\mathbb{Q}$-Cartier with the discrepancy $-1 - r$. Conversely, if $m K_X$ is Cartier near the vertex, restrict its pullback to $E$ and read off $m K_V$ as a multiple of $L$. The resolution $Y$ is smooth with one smooth exceptional divisor, so it is a log resolution, and Section 2.2 decides the class.

### Examples

**Example 4.2.21 (cones over plane curves).** Let $V \subset \mathbb{P}^2$ be a smooth curve of degree $d$ and $L = \mathcal{O}_V(1)$. A plane curve is projectively normal, so $X = \{F = 0\} \subset \mathbb{A}^3$, the affine cone over $V$. Adjunction gives $K_V = \mathcal{O}_V(d - 3)$, so $r = d - 3$ and $K_X$ is Cartier, and
$$a(E, X, 0) = 2 - d.$$
The genus is $g = \frac{(d-1)(d-2)}{2}$, so $\frac{2g-2}{d} = d - 3$, and this agrees with the corollary. For $d = 1$ the cone is a plane and $a = 1$. For $d = 2$ it is the $A_1$ singularity, $a = 0$, canonical, as in Example 4.1.8.

**Example 4.2.22 (the cone over a plane cubic).** For $d = 3$, $V$ is an elliptic curve and $a = -1$. The cone $\{x^3 + y^3 + z^3 = 0\}$ is lc and not klt. Its singularity is a *simple elliptic* singularity. The resolution has one exceptional curve, an elliptic curve with $E^2 = -3$, and $K_Y = f^*K_X - E$. It is also not a rational singularity: $R^1 f_* \mathcal{O}_Y = \bigoplus_{m \ge 0} H^1(V, L^m)$ contains $H^1(V, \mathcal{O}_V) \ne 0$ (Kol13, Chapter 3). Section 3.3 places it among the lc surface germs.

**Example 4.2.23 (the cone over a plane quartic).** For $d = 4$, $V$ has genus 3 and $a = -2 < -1$. The cone $\{x^4 + y^4 + z^4 = 0\}$ is not lc. By part 2 of Theorem 4.1.21 its discrepancies are not bounded below: $\operatorname{discrep}(X, 0) = -\infty$. The crepant pullback is $(Y, 2E)$. The blow-ups of the proof of that theorem, at a point of $E$ and then at the points where the strict transform of $E$ meets the last exceptional curve, give divisors with discrepancy $-k$ for each $k \ge 1$.

**Example 4.2.24 (the quotient $\frac1n(1,1)$).** Let $V = \mathbb{P}^1$ and $L = \mathcal{O}(n)$. Then $R = \bigoplus_m H^0(\mathbb{P}^1, \mathcal{O}(nm))$ is the ring of polynomials in $s, t$ of degree divisible by $n$, the ring of invariants of $\mu_n$ acting by $\zeta \cdot (s, t) = (\zeta s, \zeta t)$. So $X = \frac1n(1,1)$. Here $K_{\mathbb{P}^1} = \mathcal{O}(-2)$, so $r = -\frac2n$ and
$$a(E, X, 0) = -1 + \frac2n = -\frac{n-2}{n}.$$
For $n = 2$ this is the $A_1$ singularity with $a = 0$. For $n = 3$ it is $\frac13(1,1)$ with $a = -\frac13$, klt and not canonical. Volume 3, Example 3.3.38, computes the same number from the cone $\sigma_n$ and the vector $m_{\sigma_n}$ of Volume 3, Example 3.3.30. Every $\frac1n(1,1)$ is klt, and the discrepancies tend to $-1$ as $n$ grows.

**Example 4.2.25 (the quotient $\frac12(1,1,1)$).** Let $V = \mathbb{P}^2$ and $L = \mathcal{O}(2)$. In the same way $X = \mathbb{A}^3 / \pm 1 = \frac12(1,1,1)$, the cone over the Veronese surface. Here $K_{\mathbb{P}^2} = \mathcal{O}(-3) = -\frac32 L$, so $r = -\frac32$ and
$$a(E, X, 0) = -1 + \frac32 = \frac12.$$
So $X$ is terminal, with $\operatorname{discrep}(X, 0) = \frac12$, and $2K_X$ is Cartier while $K_X$ is not. This is the simplest terminal singularity that is not Gorenstein. Volume 3, Example 3.3.24, proves that it is terminal by the toric criterion, and Volume 3, Example 3.3.40, gives the general case $\frac1n(1, \dots, 1)$ in dimension $N$: there $V = \mathbb{P}^{N-1}$, $L = \mathcal{O}(n)$, $r = -\frac{N}{n}$ and $a = \frac{N}{n} - 1$.

**Counterexample 4.2.26 (a cone with no $\mathbb{Q}$-Cartier canonical divisor).** Let $V = \mathbb{P}^1 \times \mathbb{P}^1$ and $L = \mathcal{O}(1, 2)$. Then $\operatorname{Pic}(V) \otimes \mathbb{Q} = \mathbb{Q}^2$, $K_V = \mathcal{O}(-2, -2)$, and $(-2, -2)$ is not a rational multiple of $(1, 2)$. By part 1, $K_X$ is not $\mathbb{Q}$-Cartier, and no discrepancy of $(X, 0)$ is defined. For $L = \mathcal{O}(1, 1)$, instead, $r = -2$ and $a = 1$: this cone is $\{xz = yw\} \subset \mathbb{A}^4$, the ordinary double point of dimension 3, and it is terminal, as in the example of Section 2.2.

**Counterexample 4.2.27 (curves of genus at least 2).** Let $V$ be a curve of genus $g \ge 2$ over $\mathbb{C}$. Then $K_V \sim_{\mathbb{Q}} rL$ forces $r = \frac{2g-2}{d}$, and it holds if and only if the class $d K_V - (2g - 2) L$ in $\operatorname{Pic}^0(V)$ is torsion (Exercise 6). This holds for $L = K_V$, where $a = -2$, and fails for a general $L$ of degree $d$. So for a general $L$ the cone over $V$ has no $\mathbb{Q}$-Cartier canonical divisor. The number $-1 - \frac{2g-2}{d}$ still makes sense as Mumford's numerical discrepancy, and Section 3.1 computes it.

### Proof

*The two facts on $Y$.* The ideal of $E$ in $\bigoplus_{m \ge 0} L^m$ is $\bigoplus_{m \ge 1} L^m = L \otimes \bigoplus_{m \ge 0} L^m$, which is $p^*L$ as an $\mathcal{O}_Y$-module. So $\mathcal{O}_Y(-E) \cong p^* L$. The relative cotangent sheaf of the total space of a line bundle with sheaf of sections $L^{-1}$ is $p^*(L^{-1})^\vee = p^* L$. The exact sequence $0 \to p^* \Omega_V \to \Omega_Y \to \Omega_{Y/V} \to 0$ gives $\omega_Y \cong p^* \omega_V \otimes p^* L$. So $K_Y \sim p^*K_V + p^*L \sim p^* K_V - E$. As a check, adjunction gives $(K_Y + E)|_E \sim K_V$, which is right since $E \cong V$.

*Part 1, the "if" direction, and part 2.* Suppose $m K_V \sim m r L$ with $m \ge 1$ and $mr \in \mathbb{Z}$. Then
$$m K_Y \sim p^*(mK_V) - mE \sim p^*(mrL) - mE \sim -mr E - mE = -m(1 + r) E.$$
So $m K_Y + m(1 + r) E = \operatorname{div}_Y(h)$ for a rational function $h$. Here $K_Y = \operatorname{div}_Y(\omega)$ for a rational form $\omega$, and $K_X = \operatorname{div}_X(\omega)$ with the same form, so $K_X = f_* K_Y$. Apply $f_*$: $f_* E = 0$, so $m K_X = \operatorname{div}_X(h)$. This is a principal divisor, so $m K_X$ is Cartier and $f^*(mK_X) = \operatorname{div}_Y(h) = mK_Y + m(1 + r)E$. Divide by $m$: $K_Y = f^* K_X - (1 + r) E$, so $a(E, X, 0) = -1 - r$.

*Part 1, the "only if" direction.* Let $m K_X$ be Cartier. Then $f^*(m K_X) - m K_Y$ is supported on $E$, so $f^*(m K_X) = m K_Y + b E$ for an integer $b$. Near the vertex, $m K_X = \operatorname{div}(h)$ on an open set $U \ni 0$, so $m K_Y + bE = \operatorname{div}(f^* h)$ on $f^{-1}(U) \supset E$. So the line bundle $\mathcal{O}_Y(mK_Y + bE)$ is trivial on a neighbourhood of $E$, and its restriction to $E$ is trivial. By the two facts, $\mathcal{O}_Y(m K_Y + bE) \cong p^*(\omega_V^m \otimes L^{m - b})$, and its restriction to $E \cong V$ is $\omega_V^m \otimes L^{m-b}$. So $m K_V \sim (b - m) L$, and $K_V \sim_{\mathbb{Q}} rL$ with $r = \frac{b - m}{m}$.

*Part 3.* $Y$ is smooth, $\operatorname{Exc}(f) = E$ is a smooth prime divisor, and $\Delta = 0$, so $f$ is a log resolution. The crepant pullback is $(Y, -aE)$. If $a < -1$, then $X$ is not lc by Theorem 4.2.14. If $a \ge -1$, the coefficient $-a$ is at most 1, and by the same theorem and Theorem 4.2.12, $\operatorname{discrep}(X, 0) = \min\{a, \operatorname{discrep}(Y, -aE)\} = \min\{a, 1, 1 + a\} = \min\{a, 1\}$. Here $\dim X = n \ge 2$. The four conditions follow, since klt and lc for $\Delta = 0$ are decided by the coefficient $-a$ alone.

*The corollary.* On a curve, $\operatorname{Pic}(V) \otimes \mathbb{Q} \to \mathbb{Q}$ by the degree, so $K_V \sim_{\mathbb{Q}} rL$ forces $r = \frac{2g-2}{d}$. Part 2 gives the formula. For $g = 0$, $\operatorname{Pic}(\mathbb{P}^1) = \mathbb{Z}$ by the degree, so $d K_V \sim -2L$ always. For $g = 1$, $K_V \sim 0 = 0 \cdot L$ always, and $K_X$ is Cartier. Now read the classes: $a > -1$ if and only if $2g - 2 < 0$; $a \ge -1$ if and only if $g \le 1$; for $g = 0$, $a = -1 + \frac2d \ge 0$ if and only if $d \le 2$, and $a > 0$ if and only if $d = 1$. For $d = 1$, $R = k[s, t]$. $\square$

### Exercises

1. (A) Let $V = \mathbb{P}^2$ and $L = \mathcal{O}(1)$, so $X = \mathbb{A}^3$. Check that the theorem gives $a = 2$, and compare with Example 4.1.6.
2. (A) Let $V = \mathbb{P}^2$ and $L = \mathcal{O}(3)$. Show that $X$ is Gorenstein, canonical and not terminal.
3. (B) Let $V = \mathbb{P}^1 \times \mathbb{P}^1$ and $L = \mathcal{O}(p, q)$ with $p, q \ge 1$. Show that $K_X$ is $\mathbb{Q}$-Cartier if and only if $p = q$, and that then $a(E, X, 0) = \frac{2}{p} - 1$. Which of these cones are terminal, and which are canonical?
4. (B) Let $V = \{F = 0\} \subset \mathbb{P}^{N-1}$ be a smooth hypersurface of degree $d$, with $N \ge 3$, and $X = \{F = 0\} \subset \mathbb{A}^N$ its affine cone. Blow up the origin of $\mathbb{A}^N$, with exceptional divisor $E_0$. Use $K_{\mathrm{Bl}} = f^* K_{\mathbb{A}^N} + (N - 1)E_0$, $f^* X = X' + d E_0$ and adjunction to $X'$ to show that $a(E, X, 0) = N - 1 - d$. Check this against the theorem with $K_V = \mathcal{O}_V(d - N)$.
5. (B) Let $V$ be an elliptic curve and $L$ of degree $d \ge 1$. Show that $K_X$ is Cartier and that $X$ is lc and not klt for every $d$. For $d = 3$, identify $X$ with a cone over a plane cubic.
6. (C) Let $V$ be a smooth curve of genus $g \ge 2$ over $\mathbb{C}$ and $L$ of degree $d$. Show that $K_X$ is $\mathbb{Q}$-Cartier if and only if $d K_V - (2g - 2) L$ is a torsion point of $\operatorname{Pic}^0(V)$. Deduce that the set of such $L$ of degree $d$ is countable, so that the condition fails for a general $L$.

### Lean

The theorem and the corollary are not yet in Lean. The library has `MinimalModel.IsRCartier` and `MinimalModel.CanonicalDivisor`, so part 1 can be stated with these names. The cone construction and the total space of a line bundle are not yet in the library.

### Notes and history

Cones are the first examples of Reid's survey (Rei87) and of Kol13, Chapter 3, which treats them in general, with a boundary and for $L$ only ample. The computation of $a = -1 - r$ goes back to the study of surface singularities by Mumford and Artin. The examples show three points that the later chapters use. First, the class of a cone depends on $(V, L)$ only through $r$: Fano $V$ give klt cones, Calabi-Yau $V$ give lc cones that are not klt, and $V$ of general type give cones that are not lc. Second, the condition that $K_X$ is $\mathbb{Q}$-Cartier is a real condition, and it fails often. Third, for $\frac1n(1,1)$ the discrepancy tends to $-1$, so the klt surface germs have no uniform lower bound for $a$ above $-1$. The minimal log discrepancies of Chapter 6 measure this.
