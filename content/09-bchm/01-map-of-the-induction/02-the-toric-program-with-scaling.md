---
title: The toric program with scaling
nodes: []
sources: [BCHM10, CLS11, KM98]
reads_with: [CLS11:15, BCHM10:3]
requires: [1.1, 3.4, 3.5, 3.6, 3.7, 8.1]
level: advanced
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The toric program with scaling

### Statement

The program with scaling is the form of the minimal model program that BCHM10 run. Chapter 3 defines it for $\mathbb{Q}$-factorial klt pairs and proves its basic properties. On a toric variety every step is a computation with the fan, and this section runs it on a toric 3-fold.

Let $\Sigma$ be a complete simplicial fan with $X = X_\Sigma$ projective, so that $X$ is $\mathbb{Q}$-factorial (Theorem 3.3.20). A torus-invariant $\mathbb{Q}$-divisor $\Delta = \sum_\rho \delta_\rho D_\rho$ with $0 \le \delta_\rho < 1$ makes $(X, \Delta)$ a klt pair, by the toric discrepancy formula (Theorem 3.3.34). Curve classes and divisor classes pair through the relations: if $r = (r_\rho)$ is the vector of a relation $\sum_\rho r_\rho u_\rho = 0$ that represents a class in $N_1(X)$, then $D_\rho \cdot r = r_\rho$ (Theorem 3.4.5 and Theorem 3.7.3).

**Definition 9.1.17 (the toric program with scaling).** Let $X$ and $\Delta$ be as above and let $H$ be a torus-invariant $\mathbb{Q}$-divisor such that $K_X + \Delta + H$ is nef. Put $(X_0, \Delta_0, H_0) = (X, \Delta, H)$. Given $(X_k, \Delta_k, H_k)$, let
$$\lambda_k = \inf \{ t \ge 0 : K_{X_k} + \Delta_k + t H_k \text{ is nef} \}.$$
If $\lambda_k = 0$, stop: $K_{X_k} + \Delta_k$ is nef. Otherwise choose an extremal ray $R_k$ of $\overline{NE}(X_k)$ with $(K_{X_k} + \Delta_k) \cdot R_k < 0$ and $(K_{X_k} + \Delta_k + \lambda_k H_k) \cdot R_k = 0$, and let $\varphi_k$ be its contraction (Theorem 3.5.6). If $\varphi_k$ is of fibre type, stop: $\varphi_k$ is a Mori fibre space. If it is divisorial, let $X_{k+1}$ be its target; if it is small, let $X_{k+1}$ be its flip (Theorem 3.5.20). Let $\Delta_{k+1}$ and $H_{k+1}$ be the pushforwards or strict transforms of $\Delta_k$ and $H_k$. The numbers $\lambda_k$ are the *thresholds* of the program.

The toric program with scaling is a toric $(K_X + \Delta)$-MMP in the sense of Definition 3.6.7, with a rule that chooses the ray. It terminates by Theorem 3.6.8.

**Lemma 9.1.18 (thresholds on a toric variety).** In Definition 9.1.17, suppose $\lambda_k > 0$, and let $\lambda_{-1} = 1$.

1. $K_{X_k} + \Delta_k + \lambda_{k-1} H_k$ is nef, so $\lambda_k \le \lambda_{k-1}$.
2. $\lambda_k = \max \{ -(K_{X_k} + \Delta_k) \cdot C / H_k \cdot C \}$, the maximum over the finitely many torus-invariant curves $C$ of $X_k$ with $(K_{X_k} + \Delta_k) \cdot C < 0$; each such $C$ has $H_k \cdot C > 0$. In particular $\lambda_k$ is rational.
3. A ray $R_k$ as in Definition 9.1.17 exists: the ray spanned by a curve where the maximum in part 2 is attained, if that ray is extremal, and in any case an extremal ray of the face of $\overline{NE}(X_k)$ on which $K_{X_k} + \Delta_k + \lambda_k H_k$ vanishes.

Lean: not yet in Lean.

The example is the 3-fold of Proposition 3.6.15. Let $e_1, e_2, e_3$ be the standard basis of $N = \mathbb{Z}^3$, $e_0 = -e_1 - e_2 - e_3$ and $v = e_1 + 2e_2 + 3e_3$. The star subdivision of the fan of $\mathbb{P}^3$ at $v$ is the weighted blow-up $X \to \mathbb{P}^3$ with weights $(1, 2, 3)$, with exceptional divisor $E = D_v$, and $X^+$ is the flip of the curve $C_{23}$ of $X$. Order the rays $e_0, e_1, e_2, e_3, v$. The relations $r_1 = (1, 1, 1, 1, 0)$ and $r_2 = (0, -1, -2, -3, 1)$ form a basis of $N_1(X) = N_1(X^+)$, and the map $D \mapsto (D \cdot r_1, D \cdot r_2)$ identifies $N^1(X) = N^1(X^+)$ with $\mathbb{R}^2$. In these coordinates
$$D_0 = (1, 0), \quad D_1 = (1, -1), \quad D_2 = (1, -2), \quad D_3 = (1, -3), \quad E = (0, 1), \quad K = -\textstyle\sum_\rho D_\rho = (-4, 5).$$

**Proposition 9.1.19 (scaling by $3D_0 + 2D_3$).** Let $H = 3D_0 + 2D_3$ on $X^+$, of class $(5, -6)$, and $\Delta = 0$. Then $H$ is ample, and the toric $K$-program with scaling of $H$ is
$$X^+ \dashrightarrow X \to \mathbb{P}^3 \to \mathrm{pt},$$
the flip of $C^+$, the contraction of $E$ and the Mori fibre space $\mathbb{P}^3 \to \mathrm{pt}$, with thresholds $\lambda_0 = 1$, $\lambda_1 = \frac56$ and $\lambda_2 = \frac45$.

Lean: not yet in Lean.

**Proposition 9.1.20 (scaling by $D_0 + D_3$).** Let $H' = D_0 + D_3$ on $X^+$, of class $(2, -3)$, and $\Delta = 0$. Then $H'$ is ample, and the toric $K$-program with scaling of $H'$ is
$$X^+ \to \mathbb{P}(1, 1, 2, 3) \to \mathrm{pt},$$
the contraction of $D_3^+$ to a smooth point and the Mori fibre space $\mathbb{P}(1, 1, 2, 3) \to \mathrm{pt}$, with thresholds $\lambda_0 = 3$ and $\lambda_1 = \frac73$.

Lean: not yet in Lean.

### Proof in words

On a toric variety the cone of curves is spanned by the finitely many torus-invariant curves, so a threshold is the largest of finitely many ratios $-K \cdot C / H \cdot C$. After a step the divisor $K + \lambda H$ that was zero on the contracted ray is a pullback from the base of the contraction, so it stays nef, and the thresholds can only go down.

In the example everything is read off from two coordinates. The cone of curves of $X^+$ has two edges, $C^+$ with $K \cdot C^+ = -\frac12$ and $C^+_{13}$ with $K \cdot C^+_{13} = -\frac32$. For $H = (5, -6)$ the ratios are $1$ and $\frac34$, so the flip comes first; for $H' = (2, -3)$ they are $1$ and $3$, so the divisorial contraction comes first. Both rays are $K$-negative, the ratio for $C^+$ is larger exactly when $5a + 4b > 0$ for $H = (a, b)$, and the dividing line $5a + 4b = 0$ is the line through $-K = (4, -5)$.

### Examples

**Example 9.1.21 (the walk through the chambers).** By Theorem 3.7.3 the effective cone of $X^+$ is spanned by the classes of the $D_\rho$; in the plane of $N^1$ they lie, in clockwise order, on the rays of $E = (0, 1)$, $D_0 = (1, 0)$, $D_1 = (1, -1)$, $D_2 = (1, -2)$ and $D_3 = (1, -3)$. The nef cone of $X^+$ is the cone between $D_1$ and $D_2$, since a class $(a, b)$ is nef on $X^+$ exactly when $a + b \le 0$ and $2a + b \ge 0$, and the nef cone of $X$ is the cone between $D_0$ and $D_1$, given by $a + b \ge 0$ and $b \le 0$. The cone between $E$ and $D_0$ is the chamber of $\mathbb{P}^3$, on which $E$ is in the stable base locus, and the cone between $D_2$ and $D_3$ is the chamber of $\mathbb{P}(1, 1, 2, 3)$, on which $D_3$ is. These are the chambers of the secondary fan, as in Example 3.7.16. In Proposition 9.1.19 the classes $K + tH = (5t - 4, 5 - 6t)$ for $t$ decreasing from $\infty$ move from the direction of $H$ toward $K$: at $t = 1$ the class is $(1, -1)$, on the wall between the chambers of $X^+$ and of $X$; at $t = \frac56$ it is $(\frac16, 0)$, on the ray of $D_0$, the boundary of the movable cone; at $t = \frac45$ it is $(0, \frac15)$, on the ray of $E$, the boundary of the effective cone. In Proposition 9.1.20 the classes $K + tH' = (2t - 4, 5 - 3t)$ meet the ray of $D_2$ at $t = 3$ and the ray of $D_3$ at $t = \frac73$. This is Corollary 3.7.14 for the divisor $K$ with the order of the walls fixed by the scaling divisor.

**Example 9.1.22 (a tie).** Let $H = -K_{X^+}$, of class $(4, -5)$, which is ample by part 3 of Proposition 3.6.15. Then $K + tH = (t - 1) H$, so $\lambda_0 = 1$ and $K + \lambda_0 H \equiv 0$ vanishes on the whole cone of curves. Both rays satisfy the conditions of Definition 9.1.17, and the program may start with either: the flip followed by the contraction of $E$, with $\lambda_1 = \lambda_2 = 1$, or the contraction of $D_3^+$, with $\lambda_1 = 1$. The two programs end at the two Mori fibre spaces of Example 3.6.17. A tie of thresholds is the only source of choice in a program with scaling, and a general scaling divisor avoids it at the first step.

**Example 9.1.23 (the six statements on this example).** The example sees each of the statements of Section 1 in its simplest form. The flip exists by Theorem 3.5.20, an instance of $A_3$ and of Theorem 8.3.10. The models of the divisors $K + tH$, $t > 0$, are the finitely many toric varieties of the chambers of Example 9.1.21, an instance of $E_3$. Each divisor $K + tH$ with $t \ge \frac45$ is effective, as its class is in the effective cone, an instance of $D_3$, and the program stops after finitely many steps because the thresholds run through the finitely many walls.

### Proof

*Lemma 9.1.18.* For part 1, let $k \ge 1$ and $D = K_{X_{k-1}} + \Delta_{k-1} + \lambda_{k-1} H_{k-1}$, which is nef and vanishes on $R_{k-1}$, and let $\varphi = \varphi_{k-1} \colon X_{k-1} \to Z$. If $\varphi$ is divisorial, $X_k = Z$, and by Theorem 1.1.12, applied to a Cartier multiple of $D$, $D \sim_{\mathbb{Q}} \varphi^* L$ for a $\mathbb{Q}$-Cartier divisor $L$ on $Z$, which is $\varphi_* D = K_{X_k} + \Delta_k + \lambda_{k-1} H_k$; it is nef because $\varphi^* L$ is nef and $\varphi$ is surjective. If $\varphi$ is small, part 1 of Proposition 8.1.17, applied to $B = D$, gives $c = 0$, because $D \cdot R_{k-1} = 0$ while $(K_{X_{k-1}} + \Delta_{k-1}) \cdot R_{k-1} < 0$, and so $D \sim_{\mathbb{Q}} \varphi^* L$ and $D^+ \sim_{\mathbb{Q}} \varphi^{+*} L$, and $D^+ = K_{X_k} + \Delta_k + \lambda_{k-1} H_k$ is nef. For $k = 0$ the divisor $K + \Delta + H$ is nef by hypothesis. So $\lambda_k \le \lambda_{k-1}$.

For part 2, by the toric cone theorem, Theorem 3.4.21, $\overline{NE}(X_k)$ is spanned by the classes of the finitely many torus-invariant curves. Write $D_t = K_{X_k} + \Delta_k + t H_k$. Let $C$ be a torus-invariant curve. If $(K_{X_k} + \Delta_k) \cdot C \ge 0$, then for $t \in [0, \lambda_{k-1}]$, $D_t \cdot C = (1 - t/\lambda_{k-1})(K_{X_k} + \Delta_k) \cdot C + (t/\lambda_{k-1}) D_{\lambda_{k-1}} \cdot C \ge 0$ by part 1. If $(K_{X_k} + \Delta_k) \cdot C < 0$, then $D_{\lambda_{k-1}} \cdot C \ge 0$ forces $H_k \cdot C > 0$, and $D_t \cdot C \ge 0$ if and only if $t \ge -(K_{X_k} + \Delta_k) \cdot C / H_k \cdot C$. So on $[0, \lambda_{k-1}]$ nefness of $D_t$ is the conjunction of finitely many conditions $t \ge c_C$, and $\lambda_k = \max_C c_C$, a maximum of finitely many rational numbers, which is positive by hypothesis.

For part 3, let $C$ attain the maximum, and let $F$ be the face of $\overline{NE}(X_k)$ on which $D_{\lambda_k}$ vanishes; it contains $[C]$, on which $K_{X_k} + \Delta_k$ is negative. A polyhedral face is spanned by its extremal rays, so one of them, $R$, has $(K_{X_k} + \Delta_k) \cdot R < 0$, and $D_{\lambda_k} \cdot R = 0$.

*Proposition 9.1.19.* By part 3 of Proposition 3.6.15, $\overline{NE}(X^+)$ is spanned by $C^+ = -\frac12 (r_1 + r_2)$ and $C^+_{13} = r_1 + \frac12 r_2$, so a class $(a, b)$ has $(a, b) \cdot C^+ = -\frac12 (a + b)$ and $(a, b) \cdot C^+_{13} = a + \frac12 b$. For $H = (5, -6)$ these are $\frac12$ and $2$, both positive, so $H$ is ample by Kleiman's criterion. For $K = (-4, 5)$ they are $-\frac12$ and $-\frac32$. By part 2 of Lemma 9.1.18 the ratios are $\frac{1/2}{1/2} = 1$ for $C^+$ and $\frac{3/2}{2} = \frac34$ for $C^+_{13}$, so $K + H$ is nef and $\lambda_0 = 1$, attained only on the ray of $C^+$, which is small. Its flip is $X$, by Example 3.6.17, and $H_1$ has the same class $(5, -6)$, since a flip does not change the classes of the $D_\rho$.

By part 1 of Proposition 3.6.15, $\overline{NE}(X)$ is spanned by $C_{23} = r_1 + r_2$ and $-r_2$, with $(a, b) \cdot C_{23} = a + b$ and $(a, b) \cdot (-r_2) = -b$. Here $K \cdot C_{23} = 1 > 0$ and $K \cdot (-r_2) = -5$, while $H_1 \cdot (-r_2) = 6$. The only $K$-negative ray is that of $-r_2$, with ratio $\frac56$, so $\lambda_1 = \frac56$, and its contraction is the blow-down of $E$ to $\mathbb{P}^3$. Check: $K + \frac56 H_1 = (\frac16, 0) = \frac16 D_0$ is the pullback of $\frac16$ of a plane, nef and zero on $-r_2$.

On $\mathbb{P}^3$, $H_2 = 3H_0 + 2H_3 \sim 5h$ for the hyperplane class $h$, and $K_{\mathbb{P}^3} + tH_2 \sim (5t - 4)h$ is nef if and only if $t \ge \frac45$. So $\lambda_2 = \frac45$, the ray is all of $\overline{NE}(\mathbb{P}^3)$, and its contraction is $\mathbb{P}^3 \to \mathrm{pt}$, a Mori fibre space. The thresholds $1 > \frac56 > \frac45$ decrease, as part 1 of Lemma 9.1.18 requires.

*Proposition 9.1.20.* With the formulas above, $H' = (2, -3)$ has $H' \cdot C^+ = \frac12$ and $H' \cdot C^+_{13} = \frac12$, so $H'$ is ample, and the ratios are $\frac{1/2}{1/2} = 1$ for $C^+$ and $\frac{3/2}{1/2} = 3$ for $C^+_{13}$. So $\lambda_0 = 3$, attained only on the ray of $C^+_{13}$, and by part 4 of Proposition 3.6.15 its contraction is $X^+ \to \mathbb{P}(1, 1, 2, 3)$, which maps $D_3^+$ to a smooth point. Check: $K + 3H' = (2, -4) = 2D_2$, which vanishes on $C^+_{13}$ since $2 \cdot 1 - \frac12 \cdot 4 = 0$. The target has the rays $e_0, e_1, e_2, v$ with the relation $3e_0 + 2e_1 + e_2 + v = 0$, so its class group modulo torsion is $\mathbb{Z}$ with $D_{e_0}, D_{e_1}, D_{e_2}, D_v$ of degrees $3, 2, 1, 1$, and $K$ of degree $-7$. The pushforward of $H'$ is $D_{e_0}$, of degree $3$, so $K + tH'_1$ has degree $3t - 7$ and $\lambda_1 = \frac73$; the contraction of the only ray is the map to a point. The thresholds $3 > \frac73$ decrease.

### Exercises

1. (A) Run the toric $K$-program with scaling of $H = D_0 + D_1 + D_2 + D_3$ on $X^+$: check that $H$ is ample and find the thresholds and the models.
2. (A) Show that for an ample class $H = (a, b)$ on $X^+$ the first step of the $K$-program with scaling of $H$ is the flip if $5a + 4b > 0$ and the divisorial contraction if $5a + 4b < 0$.
3. (B) For $H = (a, b)$ ample on $X^+$ with $5a + 4b > 0$, compute the three thresholds of the program as functions of $a$ and $b$, and check that they decrease.
4. (B) Run the toric $K$-program with scaling of $H = 4D_0 + 2D_3$ on $X$ itself (not on $X^+$): check that $K + H$ is nef on $X$, and find the thresholds.
5. (B) Let $X = \mathbb{F}_1$, the blow-up of $\mathbb{P}^2$ at a torus-fixed point, with exceptional curve $E$ and fibre $F$. For $H = aF + bE$ ample, run the toric $K$-program with scaling of $H$ and find the value of $a/b$ at which the program changes from $\mathbb{F}_1 \to \mathbb{P}^2 \to \mathrm{pt}$ to $\mathbb{F}_1 \to \mathbb{P}^1$.
6. (C) Prove that for $H$ outside a finite union of hyperplanes of $N^1(X^+)$ the toric $K$-program with scaling of $H$ on $X^+$ has strictly decreasing thresholds and a unique ray at each step, and use Example 9.1.22 to show that the hypothesis cannot be dropped.

### Lean

Nothing in this section is in Lean. The library defines one step of the program with scaling as `MinimalModel.IsScalingStep`, with the threshold and the condition that the scaled divisor is zero on the contracted curves, but it has no toric model of the program.

### Notes and history

The program with scaling was introduced by Shokurov and is the program of BCHM10, Section 3.10; the toric case, as a walk through the chambers of the secondary fan, goes back to the work of Reid on the toric minimal model program and of Oda and Park, and is treated in CLS11, Chapter 15. The example of the weighted blow-up with weights $(1, 2, 3)$ and its flip is that of Volume 3, Propositions 3.6.15 and Example 3.6.17. The fact that the choice of a general scaling divisor fixes the order in which walls are crossed is what makes the program with scaling a tool for termination: the thresholds are a monotone parameter, and Chapter 3 shows that with a big boundary the program visits each model at most once.
