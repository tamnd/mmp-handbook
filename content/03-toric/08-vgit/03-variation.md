---
title: Crossing the wall
nodes: []
sources: [CLS11, FS04]
reads_with: [CLS11:ch14, CLS11:ch15]
requires: [3.3, 3.5, 3.7, 3.8]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Crossing the wall

### Statement

Section 1 built three quotients from one action. Here the character varies. Its space is the line $G_U$ of Example 3.7.6, the wall is $0$, and passing through the wall is one step of the minimal model program. The kind of step depends only on the signs of the weights, and its direction for $K$ depends only on their sum.

Keep the assumptions of Section 2: $r \ge 3$, $J_0 = \emptyset$, and well formed weights. For $\chi \in \mathbb{Z}$ the quotient $X_\chi$ of Definition 3.8.1 is $X_+$ for $\chi > 0$, $X_0$ for $\chi = 0$ and $X_-$ for $\chi < 0$ (Proposition 3.8.2). Under part 5 of Theorem 3.8.8, $\operatorname{Cl}(X_\pm) \otimes \mathbb{R} = \mathbb{R}$, and the class of $\sum_i a_i D_{u_i}$ is $\sum_i a_i q_i$, which is the identification $G_U = \mathbb{R}$ of Example 3.7.6. The character and the divisor class are the same number.

**Definition 3.8.13 (the chambers).** The *chambers* of the action are the half-lines $\mathbb{R}_{>0}$ and $\mathbb{R}_{<0}$ in $G_U = \mathbb{R}$, and the *wall* is the point $0$. The *weight sum* is $s(q) = \sum_i q_i$.

By Theorem 3.3.26 the canonical divisor of $X_\pm$ is $-\sum_i D_{u_i}$, of class $-s(q)$ when every $u_i$ is a ray.

**Theorem 3.8.14 (crossing the wall).** Let $q$ be as above.

1. (Flips and flops.) Suppose $|J_+| \ge 2$ and $|J_-| \ge 2$. Then $\pi_+$ and $\pi_-$ are small, with exceptional loci the images of $V(x_k : k \in J_-)$ and $V(x_j : j \in J_+)$, which are the weighted projective spaces $\mathbb{P}(q_j : j \in J_+)$ and $\mathbb{P}(|q_k| : k \in J_-)$, of dimensions $|J_+| - 1$ and $|J_-| - 1$. A torus-invariant $\mathbb{Q}$-divisor whose class lies in the chamber $\mathbb{R}_{>0}$ is ample on $X_+$, and one whose class lies in $\mathbb{R}_{<0}$ is ample on $X_-$. In particular:
   - if $s(q) > 0$, then $-K_{X_+}$ is ample, $K_{X_-}$ is ample, and $\pi_-$ is the $K$-flip of $\pi_+$;
   - if $s(q) = 0$, then $K_{X_\pm} \sim 0$, and $X_+ \dashrightarrow X_-$ is a flop;
   - if $s(q) < 0$, the same holds with $X_+$ and $X_-$ exchanged.
2. (Divisorial contractions.) Suppose $J_- = \{k\}$ and $|J_+| \ge 2$. Then $\pi_- \colon X_- \to X_0$ is an isomorphism, $X_0$ is the affine toric variety of the simplicial cone $\operatorname{Cone}(u_j : j \in J_+)$, and $\pi_+$ is a proper birational morphism whose exceptional locus is the prime divisor $E = D_{u_k}$, the image of $x_k = 0$, isomorphic to $\mathbb{P}(q_j : j \in J_+)$. Its discrepancy is given by
$$K_{X_+} = \pi_+^* K_{X_0} + a E, \qquad a = \frac{\sum_{j \in J_+} q_j}{|q_k|} - 1 = \frac{s(q)}{|q_k|}.$$
3. (Mori fibre spaces.) Suppose $J_- = \emptyset$. Then $X_- = \emptyset$, $X_0$ is a point, and $X_+ = \mathbb{P}(q)$, on which $-K$ has class $s(q) > 0$ and is ample. So $X_+ \to X_0$ is a Mori fibre space over a point.

Lean: not yet in Lean.

The case $J_+ = \{j\}$ with $|J_-| \ge 2$ is part 2 with the signs exchanged: then $\pi_+$ is an isomorphism and $\pi_-$ contracts $D_{u_j}$. The case $|J_+| = |J_-| = 1$ is excluded by $r \ge 3$ and $J_0 = \emptyset$.

### Proof in words

The fans of $X_\pm$ are the triangulations of the circuit, so Chapter 5 already knows their contractions: Theorem 3.5.14 gives the exceptional loci, Corollary 3.5.22 gives the ample classes, and Section 2 turns its divisors into the zero sets of coordinates. The canonical class is the class of $-\sum_i D_{u_i}$, which is the number $-s(q)$, so the sign of $s(q)$ says on which side $K$ is negative. In the divisorial case the discrepancy is read off from the one relation $\sum_i q_i u_i = 0$, which writes $u_k$ in terms of the other generators of the cone.

### Examples

**Example 3.8.15 (a table of small weights).** For $r = 3$ and $r = 4$ the theorem sorts the actions as follows.

| $q$ | $J_+$, $J_-$ | $s(q)$ | the step from $X_+$ |
| --- | --- | --- | --- |
| $(1, 1, 1)$ | $3$, $0$ | $3$ | $\mathbb{P}^2 \to$ point |
| $(1, 1, -1)$ | $2$, $1$ | $1$ | blow-up of $\mathbb{A}^2$, $a = 1$ |
| $(1, 1, -2)$ | $2$, $1$ | $0$ | minimal resolution of $\frac12(1,1)$, $a = 0$ |
| $(1, 1, -3)$ | $2$, $1$ | $-1$ | minimal resolution of $\frac13(1,1)$, $a = -\frac13$ |
| $(1, 1, -1, -1)$ | $2$, $2$ | $0$ | Atiyah flop |
| $(1, 1, -1, -2)$ | $2$, $2$ | $-1$ | inverse of the Francia flip |
| $(1, 1, 1, -1)$ | $3$, $1$ | $2$ | blow-up of $\mathbb{A}^3$, $a = 2$ |

For $(1, 1, -1, -2)$, $s(q) < 0$, so it is $X_-$ that has $-K$ ample over $X_0$, and the $K$-flip goes from $X_-$, with its point $\frac12(1,1,1)$, to the smooth $X_+$. This is the direction of Example 3.5.24: the flip resolves the singularity. For $(1, 1, -3)$ the discrepancy is negative, so $X_+ \to X_0$ is not a step of the $K$-MMP from $X_+$: it is $K_{X_+}$-positive. Read in the other direction it says that $\frac13(1,1)$ is not canonical, by Theorem 3.3.36.

**Example 3.8.16 (the Hirzebruch surface as a quotient by a torus of rank two).** Rank one is not the end of the story. Let $T = \mathbb{G}_m^2$ act on $\mathbb{A}^4$ by
$$(t, s) \cdot (x_1, x_2, x_3, x_4) = (t x_1, \ t^{-a} s \, x_2, \ t x_3, \ s x_4),$$
with the weights $\beta_1 = \beta_3 = (1, 0)$, $\beta_2 = (-a, 1)$, $\beta_4 = (0, 1)$ of Example 3.7.5. Let $V = \mathbb{A}^4 \setminus (V(x_1, x_3) \cup V(x_2, x_4))$. The four charts $x_i x_j \neq 0$, for the pairs $\{i, j\}$ that are complements of the maximal cones of the fan of $\mathbb{F}_a$, cover $V$. On the chart $x_3 x_4 \neq 0$ the slice $x_3 = x_4 = 1$ meets every orbit in exactly one point, since $(t, s)$ is fixed by $t x_3 = 1$ and $s x_4 = 1$. So the chart is $\mathbb{A}^2$ with coordinates $x_1/x_3$ and $x_2 x_3^a / x_4$, the invariant Laurent monomials with exponents in $\operatorname{Cone}(u_1, u_2)^\vee$. In the same way the four charts are the four affine planes of $\mathbb{F}_a$, glued as in Chapter 2, and $V/T = \mathbb{F}_a$. The other chambers of $G_U$ give the other quotients: for $a \ge 1$ and a character $\chi$ in the interior of $\operatorname{Cone}(\beta_2, \beta_4)$ the quotient contracts the negative section $D_2$ to a point, and the result is the weighted projective plane $\mathbb{P}(1,1,a)$. For $\chi$ outside $\operatorname{Cone}(\beta_1, \dots, \beta_4)$ there are no semi-invariants of positive weight, and the quotient is empty. Exercise 5 asks for the details.

### Proof

*Proof of part 1.* Both $J_\pm$ have at least two elements, so $(W, q)$ is circuit data and $X_\pm = X_{T_\pm}$ by Theorem 3.8.8. Theorem 3.5.14, part 2, says that the exceptional locus of $\pi_+$ is $V_+(\sigma_-)$ with $\sigma_- = \operatorname{Cone}(u_k : k \in J_-)$, and with $J_0 = \emptyset$ its dimension is $n - |J_-| = |J_+| - 1 \le n - 2$, so $\pi_+$ is small. By Theorem 3.2.29 the orbits in $D_{u_k}$ are the $O(\tau)$ with $u_k \in \tau$, and a cone of the simplicial fan $T_+$ contains $\sigma_-$ if and only if it contains every $u_k$, $k \in J_-$. So $V_+(\sigma_-)$ is the intersection of the divisors $D_{u_k}$, $k \in J_-$, which by part 4 of Theorem 3.8.8 is the image of $V(x_k : k \in J_-) \cap \mathbb{A}^r_+$. The points of $\mathbb{A}^r_+$ with $x_k = 0$ for all $k \in J_-$ are the points with $(x_j)_{j \in J_+} \neq 0$ and the other coordinates zero, and their orbits under $t \cdot x_j = t^{q_j} x_j$ form $\mathbb{P}(q_j : j \in J_+)$ by Theorem 3.8.3 for the weights $q_{J_+}$. The same holds for $\pi_-$.

For the ample classes, let $D = \sum_i a_i D_{u_i}$ have class $d = \sum_i a_i q_i$. If $d < 0$, Corollary 3.5.22 says that $-D$ is ample on $X_+$ and $D$ is ample on $X_-$. The divisor $-D$ has class $-d > 0$. So every divisor with class in $\mathbb{R}_{>0}$ is ample on $X_+$, and every divisor with class in $\mathbb{R}_{<0}$ is ample on $X_-$. The canonical divisors are $K_{X_\pm} = -\sum_i D_{u_i}$, of class $-s(q)$. If $s(q) > 0$, apply Corollary 3.5.22 to $D = K$: $-K_{X_+}$ is ample, $K_{X_-}$ is ample, and $\pi_-$ is the $K$-flip of $\pi_+$. If $s(q) = 0$, then $K_{X_\pm}$ has class $0$ in $\operatorname{Cl}(X_\pm) = \mathbb{Z}$, so it is linearly equivalent to $0$; both sides are crepant over $X_0$ and the map is a flop. If $s(q) < 0$, replace $q$ by $-q$, which exchanges $X_+$ and $X_-$.

*Proof of part 2.* As $J_- = \{k\}$, Theorem 3.5.14, part 2, for the sign-reversed circuit says that $T_-$ is the fan of the single cone $\operatorname{Cone}(W \setminus \{u_k\})$ and $\pi_-$ is an isomorphism; this cone is $\operatorname{Cone}(W)$, since $u_k = \sum_{j \in J_+} (q_j / |q_k|) u_j$ lies in it. It is simplicial by Lemma 3.5.11, part 1. The exceptional locus of $\pi_+$ is $V_+(\sigma_-) = V_+(\operatorname{Cone}(u_k)) = D_{u_k}$, which is the image of $x_k = 0$ by part 4 of Theorem 3.8.8, and it is $\mathbb{P}(q_j : j \in J_+)$ by the argument of part 1. For the canonical divisor, the fan $T_+$ refines the cone $\operatorname{Cone}(W)$, and $K_{X_0}$ is $\mathbb{Q}$-Cartier since the cone is simplicial (Corollary 3.3.27). By Theorem 3.3.34 the coefficient of $E = D_{u_k}$ in $K_{X_+} - \pi_+^* K_{X_0}$ is the discrepancy of $u_k$, and the coefficients of the other $D_{u_j}$ are $0$. Proposition 3.3.35, applied to $u_k = \sum_{j \in J_+} \lambda_j u_j$ with $\lambda_j = q_j / |q_k|$, gives the discrepancy $\sum_j \lambda_j - 1$. Since $s(q) = \sum_{j \in J_+} q_j - |q_k|$, this is $s(q)/|q_k|$.

*Proof of part 3.* Theorem 3.8.8, part 3, gives $X_0$, $X_-$ and $X_+ = \mathbb{P}(q)$. Every $u_i$ is a ray, so $\operatorname{Cl}(\mathbb{P}(q)) = \mathbb{Z}$ with $[D_{u_i}] = q_i$, and $-K = \sum_i D_{u_i}$ has class $s(q) > 0$. By Example 3.7.4 the nef cone is $\mathbb{R}_{\ge 0}$; the fan is complete and simplicial and $\mathbb{P}(q)$ is projective, so the ample cone is its interior $\mathbb{R}_{>0}$ by Theorem 3.7.3, part 2. So $-K$ is ample, and $\rho(\mathbb{P}(q)) = 1$, which makes $\mathbb{P}(q) \to \operatorname{Spec} k$ a Mori fibre space. $\square$

### Exercises

1. (A) For $q = (2, 3, -1, -1)$, find $s(q)$, the type of the step, the exceptional loci of $\pi_\pm$ and the singular points of $X_+$ and $X_-$.
2. (A) Show that for $J_- = \{k\}$ the divisor $-E$ on $X_+$ has class $|q_k| > 0$, so $-E$ is $\pi_+$-ample when $|J_+| \ge 2$. Deduce that $\pi_+$ is a $K$-negative divisorial contraction if and only if $s(q) > 0$.
3. (B) Show that the weighted blow-up of $\mathbb{A}^n$ with weights $(w_1, \dots, w_n)$, $\gcd = 1$, is $X_+$ for $q = (w_1, \dots, w_n, -1)$, and that its discrepancy is $\sum_i w_i - 1$.
4. (B) Classify the well formed $q$ with $r = 4$, $|J_\pm| = 2$ and $|q_i| \le 2$ up to order and sign, and say for each one whether $X_+ \dashrightarrow X_-$ is a flip or a flop and which side is singular.
5. (B) In Example 3.8.16, find the chambers of $G_U = \mathbb{R}^2$ cut out by the four lines spanned by the $\beta_i$, and the quotient for a character in each. Check that the chamber of $\mathbb{F}_a$ is the interior of $\operatorname{Cone}(\beta_1, \beta_4)$, the ample cone of Example 3.7.5, and that for $a = 1$ the other chamber gives $\mathbb{P}^2$.
6. (C) Let $T \subseteq \mathbb{G}_m^r$ be a subtorus acting on $\mathbb{A}^r$, and let $\chi$ be a character of $T$. Define $X_\chi$ as $\operatorname{Proj} \bigoplus_{k \ge 0} R_{k\chi}$, and show that it depends only on the cone of the secondary fan that contains $\chi$ in its relative interior. (Compare Cox-Little-Schenck, Chapter 14.)

### Lean

- Status: not yet in Lean. The toric canonical divisor `MinimalModel.Toric.Fan.canonical` is there, but the toric varieties, their ample cones and the flips are not.
- Fidelity: the discrepancy $s(q)/|q_k|$ is a computation with rational numbers once the relation $u_k = \sum_j \lambda_j u_j$ is known, and the combinatorial part of Proposition 3.3.35 could be checked in Lean before the varieties exist.
- No node of the map covers this section.

### Notes and history

The variation of GIT quotients was studied in general by Thaddeus (1996) and by Dolgachev and Hu (1998). For a torus acting on affine space, the chambers are the cones of the secondary fan of Gelfand, Kapranov and Zelevinsky, and the quotients are the toric varieties of Chapter 7; Cox-Little-Schenck, Chapters 14 and 15, give the full account, including the statement that every step of the toric MMP is a wall crossing. This section proves only the rank one case, where the secondary fan is the line $G_U = \mathbb{R}$ cut at $0$, and leaves the higher rank to Example 3.8.16 and Exercise 6. In rank one the theorem is the local form of the classification of extremal contractions of toric varieties in Chapter 5, now with the canonical class given by one number.
