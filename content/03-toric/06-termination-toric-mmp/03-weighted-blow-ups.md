---
title: The MMP on weighted blow-ups of P^3
nodes: []
sources: [CLS11, FS04, Rei83]
reads_with: [FS04:3, CLS11:ch15]
requires: [3.3, 3.4, 3.5]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The MMP on weighted blow-ups of P^3

### Statement

This section runs the toric MMP by hand on two threefolds, the weighted blow-ups of $\mathbb{P}^3$ at a fixed point with weights $(1, 1, 2)$ and $(1, 2, 3)$. Every step is a computation with the wall relations of Chapter 4 and the circuits of Chapter 5. The first example has two $K$-MMPs that end at different Mori fibre spaces. The second has a $K$-positive small ray; its flip is a new projective threefold with $-K$ ample, which is a weighted blow-up of a different weighted projective space, and it carries a $D$-MMP with a flip followed by a divisorial contraction.

Fix the fan of $\mathbb{P}^3$ with rays $e_1, e_2, e_3$ and $e_0 = -e_1 - e_2 - e_3$, and coordinates $(e_0, e_1, e_2, e_3, v)$ on the space of relations $R(\Sigma)$ of the blow-up, identified with $N_1$ by Theorem 3.4.20. A class $b \in R(\Sigma)$ has $D_\rho \cdot b = b_\rho$ and $K \cdot b = -\sum_\rho b_\rho$ (Theorems 3.4.4 and 3.4.5). The wall classes are normalized as in Example 3.4.24: the coefficient of a wall class at the ray of a maximal cone $\sigma$ off the wall $\tau$ is $\operatorname{mult}(\tau) / \operatorname{mult}(\sigma)$. Write $C_{ij} = V(\operatorname{Cone}(e_i, e_j))$.

**Proposition 3.6.14 (the $(1, 1, 2)$ blow-up).** Let $X$ be the star subdivision of the fan of $\mathbb{P}^3$ at $v = e_1 + e_2 + 2 e_3$ (Example 3.4.24), with $r_1 = (1, 1, 1, 1, 0)$ and $r_2 = (0, -1, -1, -2, 1)$, and $\ell = V(\operatorname{Cone}(v, e_3))$.

1. $NE(X) = \mathbb{R}_{\ge 0} [C_{13}] + \mathbb{R}_{\ge 0} [\ell]$ with $[C_{13}] = r_1 + r_2$ and $[\ell] = -r_2$, and $K \cdot C_{13} = -1$, $K \cdot \ell = -3$.
2. The ray of $\ell$ is divisorial with $J_- = \{v\}$, and its contraction is the blow-down $X \to \mathbb{P}^3$ of $E = D_v$ to a point.
3. The ray of $C_{13}$ is divisorial with $J_- = \{e_3\}$, and its contraction $X \to \mathbb{P}(1,1,1,2)$ maps $D_3$ onto the curve $V(\operatorname{Cone}(e_0, v))$. The target has the rays $e_0, e_1, e_2, v$ with the relation $2 e_0 + e_1 + e_2 + v = 0$, and one singular point, $\frac12(1,1,1)$.
4. So $X$ has exactly two toric $K$-MMPs, $X \to \mathbb{P}^3 \to \mathrm{pt}$ and $X \to \mathbb{P}(1,1,1,2) \to \mathrm{pt}$. Both end with a Mori fibre space over a point, and the two end products are not isomorphic.

Lean: not yet in Lean.

**Proposition 3.6.15 (the $(1, 2, 3)$ blow-up and its flip).** Let $X$ be the star subdivision of the fan of $\mathbb{P}^3$ at $v = e_1 + 2 e_2 + 3 e_3$ (Example 3.5.18), with $r_1 = (1, 1, 1, 1, 0)$ and $r_2 = (0, -1, -2, -3, 1)$.

1. $NE(X) = \mathbb{R}_{\ge 0} [C_{23}] + \mathbb{R}_{\ge 0} (-r_2)$ with $[C_{23}] = r_1 + r_2$, $K \cdot C_{23} = 1$ and $K \cdot (-r_2) = -5$. The ray of $C_{23}$ is small and the other ray is the blow-down of $E = D_v$ to $\mathbb{P}^3$.
2. The flip $X^+$ of $C_{23}$ has the six maximal cones
$$\operatorname{Cone}(e_1, v, e_3), \ \operatorname{Cone}(e_1, e_2, v), \ \operatorname{Cone}(e_0, e_1, e_3), \ \operatorname{Cone}(e_0, e_1, e_2), \ \operatorname{Cone}(e_0, v, e_3), \ \operatorname{Cone}(e_0, v, e_2),$$
of multiplicities $2, 3, 1, 1, 1, 2$, and the flipped curve is $C^+ = V^+(\operatorname{Cone}(e_0, v))$.
3. $NE(X^+) = \mathbb{R}_{\ge 0} [C^+] + \mathbb{R}_{\ge 0} [C^+_{13}]$ with $[C^+] = -\frac12 (r_1 + r_2)$ and $[C^+_{13}] = r_1 + \frac12 r_2$, and $K \cdot C^+ = -\frac12$, $K \cdot C^+_{13} = -\frac32$. So $-K_{X^+}$ is ample.
4. The ray of $C^+_{13}$ is divisorial with $J_- = \{e_3\}$. Its contraction $X^+ \to \mathbb{P}(1,1,2,3)$ maps $D^+_3$ to a smooth point, and it is the weighted blow-up of that point with weights $(2, 1, 1)$. The target has the rays $e_0, e_1, e_2, v$ with the relation $3 e_0 + 2 e_1 + e_2 + v = 0$.

Lean: not yet in Lean.

### Proof in words

Each wall curve has a class that uses only the five rays, and only the four rays of its two maximal cones. So each class is the unique combination of $r_1$ and $r_2$ that has coefficient $0$ at the fifth ray, scaled by the multiplicities. Plotting the classes in the plane with basis $r_1, r_2$ shows the two edges of the cone of curves. The type of each edge is read off from the negative entries of its class, and the target of a divisorial contraction is the fan with one ray removed, whose relation names the weighted projective space.

### Examples

**Example 3.6.16 (the singular points and their mld).** On the $(1, 1, 2)$ blow-up the only singular cone is $\operatorname{Cone}(e_1, e_2, v)$, of multiplicity $2$. The form with the values $1$ at $e_1, e_2, v$ is $m = (1, 1, -\frac12)$, and the interior lattice point $e_1 + e_2 + e_3 = \frac12 (e_1 + e_2 + v)$ has $\langle m, \cdot \rangle = \frac32$. By Theorem 3.6.10 the mld at this point is $\frac32$, as for $\frac12(1,1,1)$ in Example 3.6.12; the point is $\frac12(1,1,1)$ and it is terminal. On the $(1, 2, 3)$ blow-up the singular cones are $\operatorname{Cone}(e_1, v, e_3)$, of multiplicity $2$, and $\operatorname{Cone}(e_1, e_2, v)$, of multiplicity $3$.

- For $\operatorname{Cone}(e_1, v, e_3)$, $(1, 1, 2) = \frac12 (e_1 + v + e_3)$ is a lattice point, and the sum of its coefficients is $\frac32$ (Proposition 3.3.35). The point is $\frac12(1,1,1)$, with mld $\frac32$.
- For $\operatorname{Cone}(e_1, e_2, v)$, the lattice points $\frac13 (a e_1 + b e_2 + c v)$ with $0 \le a, b, c < 3$ are those with $a + c \equiv 0$ and $b + 2c \equiv 0 \pmod 3$: they are $0$, $\frac13 (2 e_1 + e_2 + v) = (1, 1, 1)$ and $\frac13 (e_1 + 2 e_2 + 2 v) = (1, 2, 2)$, with coefficient sums $\frac43$ and $\frac53$. The point is $\frac13(2, 1, 1)$, its mld is $\frac43$, and it is terminal.

The weighted blow-up $X \to \mathbb{P}^3$ has discrepancy $1 + 2 + 3 - 1 = 5$ at $E$, by Proposition 3.3.35. On $\mathbb{P}(1,1,2,3)$ the singular cones are the cone without $e_0$, $\operatorname{Cone}(e_1, e_2, v)$, of multiplicity $3$, and the cone without $e_1$, $\operatorname{Cone}(e_0, e_2, v)$, of multiplicity $2$: the same two points $\frac13(2,1,1)$ and $\frac12(1,1,1)$, since these cones are cones of $X^+$ too.

**Example 3.6.17 (the $K$-MMPs of the $(1, 2, 3)$ blow-up and of its flip).** On $X$ the only $K$-negative ray is that of $E$, since $K \cdot C_{23} = 1$. So the toric $K$-MMP of $X$ is unique: $X \to \mathbb{P}^3 \to \mathrm{pt}$. The flip of $C_{23}$ is not a step of the $K$-MMP of $X$: it is a $D$-flip for every $D$ with $D \cdot C_{23} < 0$, for instance $D = -K_X$, so $X \dashrightarrow X^+$ is a $K$-antiflip, and its inverse $X^+ \dashrightarrow X$ is a $K$-flip. On $X^+$ both rays are $K$-negative, by part 3. So $X^+$ has two toric $K$-MMPs:

$$X^+ \dashrightarrow X \to \mathbb{P}^3 \to \mathrm{pt}, \qquad X^+ \to \mathbb{P}(1,1,2,3) \to \mathrm{pt}.$$

The first begins with a flip which, near the flipped curve, goes from the side with the point $\frac12(1,1,1)$ of $\operatorname{Cone}(e_0, v, e_2)$ to the smooth side, and it is the Francia flip of Example 3.5.25 read backwards: there $X \dashrightarrow X^+$ was computed as the flip of a $(-K)$-negative ray. The second contracts a divisor to a smooth point. As in Proposition 3.6.14, the two programs end at different Mori fibre spaces, $\mathbb{P}^3$ and $\mathbb{P}(1,1,2,3)$.

**Example 3.6.18 (a $D$-MMP with a flip).** Let $D = D_3$ on the $(1, 2, 3)$ blow-up $X$. Then $D \cdot C_{23} = -2$, the coefficient of $r_1 + r_2$ at $e_3$, and on the other ray $D_3 \cdot (-r_2) = 3 > 0$. So $D$ is not nef, and its only negative ray is the small ray of $C_{23}$. The first step of the $D_3$-MMP is the flip $X \dashrightarrow X^+$. On $X^+$,

$$D^+_3 \cdot C^+ = -\tfrac12 (1 - 3) = 1, \qquad D^+_3 \cdot C^+_{13} = 1 + \tfrac12 (-3) = -\tfrac12,$$

so the second step is the divisorial contraction $X^+ \to \mathbb{P}(1,1,2,3)$ of $D^+_3$ itself, and the pushforward of $D^+_3$ is $0$, which is nef. The program ends with the minimal model $(\mathbb{P}(1,1,2,3), 0)$:

$$X \dashrightarrow X^+ \to \mathbb{P}(1,1,2,3).$$

The steps follow Definition 3.6.7: the flip makes $D_3$ positive on the new curve $C^+$, and the contraction then removes the divisor. Here $D_3$ is effective, and its program contracts its support. The $D$-MMP with $D = D_0$, the pullback of a plane not through the blown-up point, is shorter: $D_0 \cdot (r_1 + r_2) = 1$ and $D_0 \cdot (-r_2) = 0$, so $D_0$ is nef on $X$, and $X$ is already a minimal model of $D_0$.

### Proof

*The wall classes of the $(1, 1, 2)$ blow-up.* These are computed in Example 3.4.24: in the basis $r_1, r_2$ the classes of the nine wall curves are $(1, 0)$ for the walls $\operatorname{Cone}(e_0, e_i)$, $(1, 1)$ for $C_{13}$ and $C_{23}$, $(1, \frac12)$ for $C_{12}$, $(0, -1)$ for $\ell$, and $(0, -\frac12)$ for $V(\operatorname{Cone}(v, e_1))$ and $V(\operatorname{Cone}(v, e_2))$.

*Proof of Proposition 3.6.14.* Part 1. By Theorem 3.4.21, $NE(X)$ is spanned by the nine classes. They all lie in the cone spanned by $(1, 1)$ and $(0, -1)$: $(1, 0) = (1, 1) + (0, -1)$, $(1, \frac12) = (1, 1) + \frac12 (0, -1)$, and $(0, -\frac12)$ is on the ray of $(0, -1)$. Since $(1, 1)$ and $(0, -1)$ are independent, they span the two edges. With $[C_{13}] = r_1 + r_2 = (1, 0, 0, -1, 1)$, $K \cdot C_{13} = -(1 - 1 + 1) = -1$, and with $[\ell] = -r_2 = (0, 1, 1, 2, -1)$, $K \cdot \ell = -(1 + 1 + 2 - 1) = -3$.

Part 2. The class $-r_2$ has the one negative entry at $v$, so $J_- = \{v\}$ and the ray is divisorial with exceptional divisor $D_v = E$ (Theorem 3.5.15, part 4). The fan of the contraction has the rays $e_0, e_1, e_2, e_3$. The maximal cones of $X$ that contain $v$ are joined by the walls $\operatorname{Cone}(v, e_i)$, whose classes lie on the ray, so they merge into one cone; by part 6 of Theorem 3.5.6 this is $\operatorname{Cone}(e_1, e_2, e_3)$, and the other maximal cones, $\operatorname{Cone}(e_0, e_i, e_j)$, have no wall on the ray. So the target fan is the fan of $\mathbb{P}^3$, and $\pi$ is the blow-down. The circuit is $Z = \{e_1, e_2, e_3, v\}$ with $|Z| = 4$, so $E$ maps to $V(\operatorname{Cone}(Z))$, a point (Theorem 3.5.15, part 3).

Part 3. The class $r_1 + r_2 = (1, 0, 0, -1, 1)$ has the one negative entry at $e_3$, so $J_- = \{e_3\}$, $J_+ = \{e_0, v\}$, and the ray is divisorial with exceptional divisor $D_3$. Its walls are those with class on the ray, $\operatorname{Cone}(e_1, e_3)$ and $\operatorname{Cone}(e_2, e_3)$. The relation $b^R = r_1 + r_2$ says $e_0 + v = e_3$. The maximal cones that contain $e_3$ are $\operatorname{Cone}(e_0, e_1, e_3)$, $\operatorname{Cone}(e_1, v, e_3)$, $\operatorname{Cone}(e_0, e_2, e_3)$ and $\operatorname{Cone}(v, e_2, e_3)$. The first two are joined by the wall $\operatorname{Cone}(e_1, e_3)$ and merge into $\operatorname{Cone}(e_0, e_1, v)$, which contains $e_3 = e_0 + v$; likewise the last two merge into $\operatorname{Cone}(e_0, e_2, v)$. These are the two cones of the second kind, with circuit data $W = \{e_0, e_1, e_3, v\}$ and $\{e_0, e_2, e_3, v\}$, both with circuit $Z = \{e_0, e_3, v\}$. The other maximal cones, $\operatorname{Cone}(e_0, e_1, e_2)$ and $\operatorname{Cone}(e_1, e_2, v)$, have no wall on the ray. So the target fan has the four maximal cones $\operatorname{Cone}(e_0, e_1, v)$, $\operatorname{Cone}(e_0, e_2, v)$, $\operatorname{Cone}(e_0, e_1, e_2)$ and $\operatorname{Cone}(e_1, e_2, v)$, which are the four cones spanned by three of $e_0, e_1, e_2, v$. Since

$$2 e_0 + e_1 + e_2 + v = (-2 + 1 + 0 + 1, \, -2 + 0 + 1 + 1, \, -2 + 0 + 0 + 2) = 0,$$

and the four vectors generate $\mathbb{Z}^3$, since $e_3 = -e_0 - e_1 - e_2$, this is the fan of $\mathbb{P}(2, 1, 1, 1) = \mathbb{P}(1,1,1,2)$, as in Example 3.3.25. Its cones have multiplicities equal to the weight of the missing ray: $\operatorname{Cone}(e_1, e_2, v)$, without $e_0$, has multiplicity $2$, and the other three are smooth. The image of $D_3$ is $V(\operatorname{Cone}(Z)) = V(\operatorname{Cone}(e_0, v))$, of dimension $n - |Z| + 1 = 1$ (Theorem 3.5.15, part 3).

Part 4. A toric $K$-MMP starts with a $K$-negative extremal ray, and both rays of $NE(X)$ are $K$-negative. The targets $\mathbb{P}^3$ and $\mathbb{P}(1,1,1,2)$ have Picard number $1$ and $-K = \sum D_\rho$, which is positive on the one extremal ray because the wall relations of a weighted projective space have positive coefficients. So the next step is the contraction to a point, of fibre type, and the program stops. The two end products are not isomorphic, since one is smooth and the other is not. $\square$

*The wall classes of the $(1, 2, 3)$ blow-up.* The multiplicities of the new cones are the coordinates of $v$: $\operatorname{Cone}(v, e_2, e_3)$ has $1$, $\operatorname{Cone}(e_1, v, e_3)$ has $2$, $\operatorname{Cone}(e_1, e_2, v)$ has $3$. Every wall here is a cone of multiplicity $1$: for each pair among $e_0, e_1, e_2, e_3, v$ that spans a wall, the $2 \times 2$ minors of the two vectors have greatest common divisor $1$; for instance $v$ and $e_1$ have the minors $-2$, $-3$ and $0$. The relations among four of the five rays are, for the rays without $e_1$, $e_2$ and $e_3$ respectively,

$$e_0 + v - e_2 - 2 e_3 = 0, \qquad 2 e_0 + e_1 - e_3 + v = 0, \qquad 3 e_0 + 2 e_1 + e_2 + v = 0,$$

which are $r_1 + r_2$, $2 r_1 + r_2$ and $3 r_1 + r_2$ in the coordinates $(e_0, e_1, e_2, e_3, v)$. Normalizing by the multiplicities gives $[C_{23}] = r_1 + r_2$, $[C_{13}] = r_1 + \frac12 r_2$ and $[C_{12}] = r_1 + \frac13 r_2$, while $[V(\operatorname{Cone}(e_0, e_i))] = r_1$ and the walls $\operatorname{Cone}(v, e_i)$ have classes on the ray of $-r_2 = (0, 1, 2, 3, -1)$. This is Problem 4 of Chapter 4.

*Proof of Proposition 3.6.15.* Part 1. In the basis $r_1, r_2$ the classes are $(1, 1)$, $(1, \frac12)$, $(1, \frac13)$, $(1, 0)$ and multiples of $(0, -1)$. All lie in the cone spanned by $(1, 1)$ and $(0, -1)$, since $(1, c) = (1, 1) + (1 - c)(0, -1)$ for $c \le 1$. So $NE(X)$ is spanned by $[C_{23}]$ and $-r_2$. Then $K \cdot C_{23} = -(1 + 0 - 1 - 2 + 1) = 1$ and $K \cdot (-r_2) = -(0 + 1 + 2 + 3 - 1) = -5$. The class of $C_{23}$ has the two negative entries at $e_2$ and $e_3$, so the ray is small (Example 3.5.18), and the ray of $-r_2$ has $J_- = \{v\}$ and is the blow-down to $\mathbb{P}^3$, by the argument of part 2 of Proposition 3.6.14.

Part 2. By Theorem 3.5.20 and Example 3.5.25, $\Sigma^+$ is obtained by removing the cones that contain $\sigma_- = \operatorname{Cone}(e_2, e_3)$, which are $\operatorname{Cone}(e_0, e_2, e_3)$, $\operatorname{Cone}(v, e_2, e_3)$ and the wall itself, and adding the cones of $T_-$ of the circuit $W = \{e_0, v, e_2, e_3\}$ with relation $(1, 1, -1, -2)$, whose maximal cones are $\operatorname{Cone}(W \setminus \{e_2\}) = \operatorname{Cone}(e_0, v, e_3)$ and $\operatorname{Cone}(W \setminus \{e_3\}) = \operatorname{Cone}(e_0, v, e_2)$. Their multiplicities are $|q_{e_2}| = 1$ and $|q_{e_3}| = 2$ (Proposition 3.5.13), since $W$ generates $\mathbb{Z}^3$ and the relation is primitive (Example 3.5.25). The other four maximal cones are cones of $X$, with the multiplicities above. The new wall is $\operatorname{Cone}(e_0, v)$, the interior wall of $T_-$, and $C^+$ is its curve.

Part 3. The nine walls of $\Sigma^+$ and their classes:

| wall | cones on its sides | multiplicities | class | $K \cdot C$ |
|---|---|---|---|---|
| $\operatorname{Cone}(e_0, v)$ | $\operatorname{Cone}(e_0, v, e_3)$, $\operatorname{Cone}(e_0, v, e_2)$ | $1, 2$ | $-\frac12 (r_1 + r_2)$ | $-\frac12$ |
| $\operatorname{Cone}(e_0, e_3)$ | $\operatorname{Cone}(e_0, v, e_3)$, $\operatorname{Cone}(e_0, e_1, e_3)$ | $1, 1$ | $2 r_1 + r_2$ | $-3$ |
| $\operatorname{Cone}(v, e_3)$ | $\operatorname{Cone}(e_0, v, e_3)$, $\operatorname{Cone}(e_1, v, e_3)$ | $1, 2$ | $r_1 + \frac12 r_2$ | $-\frac32$ |
| $\operatorname{Cone}(e_1, e_3)$ | $\operatorname{Cone}(e_1, v, e_3)$, $\operatorname{Cone}(e_0, e_1, e_3)$ | $2, 1$ | $r_1 + \frac12 r_2$ | $-\frac32$ |
| $\operatorname{Cone}(e_0, e_2)$ | $\operatorname{Cone}(e_0, v, e_2)$, $\operatorname{Cone}(e_0, e_1, e_2)$ | $2, 1$ | $\frac32 r_1 + \frac12 r_2$ | $-\frac72$ |
| $\operatorname{Cone}(v, e_2)$ | $\operatorname{Cone}(e_0, v, e_2)$, $\operatorname{Cone}(e_1, e_2, v)$ | $2, 3$ | $\frac12 r_1 + \frac16 r_2$ | $-\frac76$ |
| $\operatorname{Cone}(e_1, e_2)$ | $\operatorname{Cone}(e_1, e_2, v)$, $\operatorname{Cone}(e_0, e_1, e_2)$ | $3, 1$ | $r_1 + \frac13 r_2$ | $-\frac73$ |
| $\operatorname{Cone}(v, e_1)$ | $\operatorname{Cone}(e_1, v, e_3)$, $\operatorname{Cone}(e_1, e_2, v)$ | $2, 3$ | $-\frac16 r_2$ | $-\frac56$ |
| $\operatorname{Cone}(e_0, e_1)$ | $\operatorname{Cone}(e_0, e_1, e_3)$, $\operatorname{Cone}(e_0, e_1, e_2)$ | $1, 1$ | $r_1$ | $-4$ |

Each class is computed in the same way. For the wall $\operatorname{Cone}(e_0, v)$, the four rays of its two cones are $e_0, v, e_2, e_3$, so the class is a multiple of the relation $-(r_1 + r_2) = (-1, 0, 1, 2, -1)$ that has positive coefficients at the two rays $e_2$ and $e_3$ off the wall. The wall has multiplicity $1$ (the vectors $e_0$ and $v$ have the minor $(-1)(2) - (-1)(1) = -1$), so the coefficient at $e_3$, the ray of the cone of multiplicity $1$, is $1$, and the class is $\frac12 (-1, 0, 1, 2, -1)$. Then $K \cdot C^+ = -\frac12 (-1 + 1 + 2 - 1) = -\frac12$, as in Example 3.5.24. For the wall $\operatorname{Cone}(v, e_2)$ the rays are $e_0, e_1, e_2, v$, the relation is $3 r_1 + r_2 = (3, 2, 1, 0, 1)$, and the coefficient at $e_0$ must be $\frac12$, which gives $\frac16 (3 r_1 + r_2)$; the coefficient at $e_1$ is then $\frac13$, as the multiplicity $3$ requires. The other rows are the same computation, and the walls that are also walls of $X$ keep their classes. In all rows $K \cdot C = -\sum_\rho b_\rho$ with $\sum_\rho (r_1)_\rho = 4$ and $\sum_\rho (r_2)_\rho = -5$.

In the basis $r_1, r_2$ the nine classes are, up to positive factors, $(-1, -1)$, $(2, 1)$, $(3, 1)$, $(1, 0)$ and $(0, -1)$. Each is a nonnegative combination of $(-1, -1)$ and $(2, 1)$:

$$(3, 1) = 2 (2, 1) + (-1, -1), \qquad (1, 0) = (2, 1) + (-1, -1), \qquad (0, -1) = (2, 1) + 2 (-1, -1).$$

Since $(-1, -1)$ and $(2, 1)$ are independent, $NE(X^+)$ is the cone they span, with edges $[C^+]$ and $[C^+_{13}] = r_1 + \frac12 r_2$. Both have $K \cdot C < 0$. By Theorem 3.4.21 the nef cone is dual to $NE(X^+)$, and the ample cone is its interior, so $-K_{X^+}$ is ample.

Part 4. The class $2 r_1 + r_2 = (2, 1, 0, -1, 1)$ has the one negative entry at $e_3$, so the ray is divisorial with $J_- = \{e_3\}$ and exceptional divisor $D^+_3$. Its walls are $\operatorname{Cone}(e_0, e_3)$, $\operatorname{Cone}(v, e_3)$ and $\operatorname{Cone}(e_1, e_3)$, and they join the three maximal cones that contain $e_3$, which merge into $\operatorname{Cone}(e_0, e_1, v)$, containing $e_3 = 2 e_0 + e_1 + v$. The circuit is $Z = \{e_0, e_1, e_3, v\}$ with $|Z| = 4$, so $D^+_3$ maps to a point (Theorem 3.5.15, part 3). The three cones that contain $e_3$ are the star subdivision of $\operatorname{Cone}(e_0, e_1, v)$ at $e_3$. That cone is smooth, since $\det(e_0, e_1, v) = 1$, and in its basis $e_3 = 2 e_0 + e_1 + v$ has coordinates $(2, 1, 1)$; so the contraction is the weighted blow-up of a smooth point with weights $(2, 1, 1)$ (Corollary 3.2.39). The remaining maximal cones, $\operatorname{Cone}(e_1, e_2, v)$, $\operatorname{Cone}(e_0, e_1, e_2)$ and $\operatorname{Cone}(e_0, v, e_2)$, have no wall on the ray. So the target fan has the four cones spanned by three of $e_0, e_1, e_2, v$, and the relation

$$3 e_0 + 2 e_1 + e_2 + v = (-3 + 2 + 0 + 1, \, -3 + 0 + 1 + 2, \, -3 + 0 + 0 + 3) = 0$$

with the four vectors generating $\mathbb{Z}^3$ identifies it with $\mathbb{P}(3, 2, 1, 1) = \mathbb{P}(1,1,2,3)$. $\square$

### Exercises

1. (A) In Proposition 3.6.14, compute $D_\rho \cdot C_{13}$ and $D_\rho \cdot \ell$ for all five rays and check that $E \cdot \ell = -1$ and $D_3 \cdot C_{13} = -1$.
2. (A) Check the rows of the table in the proof of Proposition 3.6.15 for the walls $\operatorname{Cone}(e_0, e_3)$, $\operatorname{Cone}(e_0, e_2)$ and $\operatorname{Cone}(v, e_1)$.
3. (B) Find all toric $D$-MMPs of the $(1, 2, 3)$ blow-up for $D = E$ and for $D = D_1$, and identify their outcomes.
4. (B) Show that the contraction $X^+ \to \mathbb{P}(1,1,2,3)$ of Proposition 3.6.15 has discrepancy $3$ at $D^+_3$, and that this agrees with $K_{X^+} \cdot C^+_{13} = -\frac32$ and $D^+_3 \cdot C^+_{13} = -\frac12$.
5. (C) Let $X$ be the weighted blow-up of $\mathbb{P}^3$ at a fixed point with weights $(1, a, b)$, $1 \le a \le b$ coprime. Find the classes of the walls $C_{23}$ and $\operatorname{Cone}(v, e_i)$, and decide for which $(a, b)$ the ray of $C_{23}$ is $K$-negative, $K$-trivial or $K$-positive.

### Lean

- Status: not yet in Lean. The library has no fans of weighted projective spaces or of weighted blow-ups as named objects, and no computation of wall classes for them.
- Fidelity: each step above is a step `MinimalModel.Toric.IsToricStep` on fans in the sense of `MinimalModel/Toric/Program.lean`, and the final contractions to a point are `MinimalModel.Toric.IsToricMoriFibreSpace` with the base the quasi-fan with one cone, all of $N_{\mathbb{R}}$. Checking these instances in Lean would need the support functions of the specific divisors, which are not formalized.
- No node of the map covers this section. The examples illustrate the node MMAWP4SA44 (toric-mmp) of Section 2.

### Notes and history

The weighted blow-ups of $\mathbb{P}^3$ are the examples of the plan for this volume. The $(1, 1, 2)$ blow-up appeared in Example 3.4.24 and the $(1, 2, 3)$ blow-up in Problem 4 of Chapter 4 and in Examples 3.5.18 and 3.5.25. The computations of this section were made for the handbook from the wall relations, following the method of Cox-Little-Schenck, Chapter 15, and Fujino and Sato (2004, Section 3). That one variety can have several $K$-MMPs that end at different Mori fibre spaces is a general feature of the program; in the toric case the choices are the edges of the cone of curves, and the end products are related by birational maps that the Sarkisov program decomposes, a topic outside this volume.
