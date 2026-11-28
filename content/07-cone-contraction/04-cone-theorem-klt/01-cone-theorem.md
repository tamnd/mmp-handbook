---
title: The cone theorem for klt pairs
nodes: [MMDZBZY2BV]
sources: [KM98, KMM87, Mat02, Kaw91]
reads_with: [KM98:3.15, Mat02:ch8]
requires: [P7.3, P7.4, 4.2, 6.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The cone theorem for klt pairs

### Statement

Throughout the chapter $k$ is an algebraically closed field of characteristic $0$, $(X, \Delta)$ is a projective klt pair (Definition 4.2.1) of dimension $d$ with $\Delta$ an effective $\mathbb{Q}$-divisor, and $a$ is the least positive integer such that $a(K_X + \Delta)$ is Cartier. Write $K_\Delta \in N^1(X)$ for the class of $K_X + \Delta$. For $\delta \in N^1(X)$ and a subset $C \subseteq \overline{NE}(X)$ write $C_{\delta \ge 0} = \{ z \in C : \delta \cdot z \ge 0 \}$, and similarly with $<$. For an ample class $H$ the slice $\Sigma_H = \{ z \in \overline{NE}(X) : H \cdot z = 1 \}$ is compact, and every nonzero $z \in \overline{NE}(X)$ is a positive multiple of a point of it (Corollary P7.3.14). The *dimension* of a convex cone is the dimension of its linear span.

Two results of the earlier chapters of this volume are the only inputs beyond Volumes P7 and 6. The *rationality theorem* of Chapter 3: if $K_\Delta$ is not nef and $H$ is an ample Cartier divisor, then the nef threshold
$$r(H) = \max \{ t \in \mathbb{R} : H + t K_\Delta \text{ is nef} \}$$
is a rational number $u/v$ with $u, v$ positive integers and $v \le a(d + 1)$ (KM98, Theorem 3.5). The *base point free theorem* of Chapter 2: if $D$ is a nef Cartier divisor and $b D - (K_X + \Delta)$ is nef and big for some $b > 0$, then $|m D|$ is free for every $m \gg 0$ (KM98, Theorem 3.3). This section uses only the rationality theorem.

**Definition 7.4.1 (supporting divisors and extremal faces).** A *face* of $\overline{NE}(X)$ is a closed convex subcone $F$ such that $u, v \in \overline{NE}(X)$ and $u + v \in F$ imply $u, v \in F$. It is an *extremal face*, and an *extremal ray* if it has dimension $1$. It is *$K_\Delta$-negative* if $K_\Delta \cdot z < 0$ for every $z \in F \setminus \{0\}$. For a nef class $L$ put $F_L = \overline{NE}(X) \cap L^\perp$, a face of $\overline{NE}(X)$, since $L \cdot u + L \cdot v = 0$ with both terms nonnegative forces both to vanish. Let $\mathcal{L}$ be the set of nef Cartier divisors $L$ such that $F_L \ne \{0\}$ and $F_L$ is $K_\Delta$-negative; these are the *$K_\Delta$-negative supporting divisors*. A face of the form $F_L$ is *exposed*.

The zero divisor lies in $\mathcal{L}$ exactly when $K_\Delta$ is negative on $\overline{NE}(X) \setminus \{0\}$, and then $F_0 = \overline{NE}(X)$.

**Lemma 7.4.2 (positivity near a face).** Let $L$ be a nef class, $F = F_L$, and $D \in N^1(X)$ with $D \cdot z > 0$ for every $z \in F \setminus \{0\}$. There is $k_0$ such that $D + k L$ is ample for every real $k \ge k_0$.

Lean: not yet in Lean.

**Lemma 7.4.3 (thresholds on a face).** Suppose that $K_\Delta$ is not nef. Let $C$ be either $\overline{NE}(X)$ or $F_L$ for some $L \in \mathcal{L}$, let $A \in N^1(X)_\mathbb{Q}$ be a class with $A \cdot z > 0$ for $z \in C \setminus \{0\}$, and let $m \ge 1$ be an integer such that $m A$ is the class of a Cartier divisor. Put
$$r_C(A) = \sup \{ t \ge 0 : (A + t K_\Delta) \cdot z \ge 0 \text{ for every } z \in C \}.$$

1. $0 < r_C(A) < \infty$, and $m \, r_C(A) = u/v$ with $u, v$ positive integers and $v \le a(d + 1)$.
2. There is $L' \in \mathcal{L}$ with $F_{L'} = C \cap (A + r_C(A) K_\Delta)^\perp$, and this face is nonzero.

Lean: `MinimalModel.RationalityTheorem`, in the project library, is the rationality theorem used in the proof, the case $C = \overline{NE}(X)$, as a statement without proof.

**Lemma 7.4.4 (the closure lemma).** Suppose that $K_\Delta$ is not nef. Let $C$ be either $\overline{NE}(X)$ or $F_L$ for some $L \in \mathcal{L}$, and suppose that $\dim C \ge 2$. Let $B$ be the closure of
$$C_{K_\Delta \ge 0} + \sum \{ F_{L'} : L' \in \mathcal{L}, \ F_{L'} \subsetneq C \}.$$
Then $B = C$.

Lean: not yet in Lean.

**Lemma 7.4.5 (discreteness of exposed rays).** Let $H$ be ample and $\varepsilon > 0$. Only finitely many extremal rays of the form $F_L$ with $L \in \mathcal{L}$ satisfy $(K_\Delta + \varepsilon H) \cdot F_L < 0$. Each such ray is spanned by a class in $N_1(X)_\mathbb{Q}$.

Lean: not yet in Lean.

**Theorem 7.4.6 (the cone theorem for klt pairs).** Let $H$ be an ample class.

1. For every $\varepsilon > 0$ there are finitely many $K_\Delta$-negative extremal rays $R_1, \dots, R_m$ with
$$\overline{NE}(X) = \overline{NE}(X)_{K_\Delta + \varepsilon H \ge 0} + \sum_{i=1}^m R_i.$$
2. Let $\{ R_i \}_{i \in I}$ be the set of $K_\Delta$-negative extremal rays. Then $I$ is countable, only finitely many $R_i$ are $(K_\Delta + \varepsilon H)$-negative for each $\varepsilon > 0$, every $R_i$ is exposed and spanned by a rational class, and
$$\overline{NE}(X) = \overline{NE}(X)_{K_\Delta \ge 0} + \sum_{i \in I} R_i,$$
with no closure taken on the right.
3. Every $K_\Delta$-negative extremal face $F$ is the sum of the finitely many $R_i$ that it contains, and $F = F_L$ for some $L \in \mathcal{L}$.

Lean: `MinimalModel.ConeTheoremKlt`, in the project library, is parts 1 and 2 with the rays spanned by $K_\Delta$-negative curves, as a statement without proof; the curves are supplied by Corollary 7.4.12.

**Corollary 7.4.7 (supporting divisors of extremal faces).** Let $F$ be a $K_\Delta$-negative extremal face. There are a closed convex cone $V \subseteq \overline{NE}(X)$ and $L \in \mathcal{L}$ such that $\overline{NE}(X) = V + F$, $V$ meets the span of $F$ only in $0$, $F_L = F$ and $L \cdot v > 0$ for $v \in V \setminus \{0\}$. For every $M \in N^1(X)$ with $M \cdot z = 0$ for all $z \in F$ there is $k_0$ such that, for every $k \ge k_0$, the class $k L + M$ is nef with $F_{kL + M} = F$, and $k L + M - K_\Delta$ is ample.

Lean: not yet in Lean.

**Corollary 7.4.8 (log Fano pairs).** If $-K_\Delta$ is ample, then $\overline{NE}(X)$ is a rational polyhedral cone, the sum of finitely many $K_\Delta$-negative extremal rays.

Lean: not yet in Lean.

### Proof in words

The proof is Kawamata's, in the form of KM98, Theorem 3.15. The rationality theorem says that if an ample divisor $A$ is pushed in the direction of $K_\Delta$ until it stops being ample, it stops at a rational time with bounded denominator, and the nef divisor where it stops cuts out a $K_\Delta$-negative exposed face. Lemma 7.4.3 extends this to the cone $F_L$ of an exposed face, by replacing $A$ with $A + k L$: for large $k$ the threshold on $X$ is the threshold on $F_L$. The closure lemma then says that these faces, together with the $K_\Delta$-nonnegative part, fill the cone. If they did not, a divisor $M$ positive on what they fill and negative somewhere on the cone, pushed by just enough of an ample $H$ to be positive on the cone, would produce an exposed face on which $M$ is negative, a contradiction. Applying the lemma inside faces lowers the dimension, so the one-dimensional exposed faces suffice. Their generators, normalized by $K_\Delta \cdot z = -1$, have coordinates with bounded denominators by part 1 of Lemma 7.4.3, so only finitely many lie in a compact region: this is the discreteness. The rest is convex geometry as in the proof of Theorem 6.2.9.

### Examples

**Example 7.4.9 (thresholds on a quadric).** Let $X = \mathbb{P}^1 \times \mathbb{P}^1$ with rulings $f_1, f_2$ and $\Delta = \frac12 D$ for the diagonal $D$, a smooth curve of class $(1, 1)$, so $(X, \Delta)$ is klt by Corollary 4.2.13 and $a = 2$. Write classes of divisors as $(\alpha, \beta)$ with $(\alpha, \beta) \cdot f_1 = \beta$ and $(\alpha, \beta) \cdot f_2 = \alpha$. Then $K_\Delta = (-2, -2) + \frac12 (1, 1) = (-\frac32, -\frac32)$, and for $H = (1, 2)$ the divisor $H + t K_\Delta = (1 - \frac32 t, 2 - \frac32 t)$ is nef exactly for $t \le \frac23$. So $r(H) = \frac23$, with denominator $3 \le a(d + 1) = 6$, and $H + \frac23 K_\Delta = (0, 1)$ cuts out the ray of $f_2$. For $H = (1, 1)$ the threshold is again $\frac23$ and $H + \frac23 K_\Delta = 0$: the face it cuts out is the whole cone, which is why Lemma 7.4.4 chooses $M$ away from the classes proportional to $K_\Delta$.

**Example 7.4.10 (the threshold on a face stabilizes).** Let $X = \mathbb{P}^1 \times \mathbb{P}^2$, $\Delta = 0$, with $p_1^* \mathcal{O}(1) = h_1$, $p_2^* \mathcal{O}(1) = h_2$, a line $f$ in a fibre of $p_1$ and a fibre $g$ of $p_2$, so that $h_1 \cdot g = h_2 \cdot f = 1$ and $h_1 \cdot f = h_2 \cdot g = 0$, and $K_X = -2 h_1 - 3 h_2$. Take $L = h_1 \in \mathcal{L}$, with $F_L = \mathbb{R}_{\ge 0} [f]$, and $A = h_2$, positive on $F_L \setminus \{0\}$ and not ample. The threshold on the face is $r_F(A) = A \cdot f / (-K_X \cdot f) = \frac13$. The threshold on $X$ of $A + k L = (k, 1)$ is the largest $t$ with $k - 2t \ge 0$ and $1 - 3t \ge 0$, that is $\min(k/2, 1/3)$, which is nondecreasing in $k$ and equal to $\frac13$ for $k \ge \frac23$. For $k = 2$ the divisor $A + 2L + \frac13 K_X = (\frac43, 0)$ cuts out exactly $F_L$, as in the proof of part 2 of Lemma 7.4.3.

**Example 7.4.11 (infinitely many rays with a boundary).** Let $X$ be the blow-up of $\mathbb{P}^2$ at the nine base points of a general pencil of cubics, $F$ a smooth fibre of the elliptic fibration, and $\Delta = \frac12 F$, klt by Corollary 4.2.13. Then $-K_X \equiv F$, so $K_\Delta \equiv -\frac12 F$ is anti-nef and not anti-ample, since $F^2 = 0$. Every $(-1)$-curve $E_i$ is a section of the fibration, so $K_\Delta \cdot E_i = -\frac12$. By Example P7.4.22 the $E_i$ span infinitely many extremal rays, all $K_\Delta$-negative, and part 2 of Theorem 7.4.6 says that they accumulate only on $K_\Delta^\perp$: for a fixed ample $H$, $H \cdot E_i \to \infty$ as in Example 6.2.15, so $(K_\Delta + \varepsilon H) \cdot E_i \ge 0$ for all but finitely many $i$.

### Proof

*Lemma 7.4.2.* Fix an ample class $H$ and the compact slice $\Sigma = \Sigma_H$. The set $U = \{ z \in \Sigma : D \cdot z > 0 \}$ is open in $\Sigma$ and contains $F \cap \Sigma$. On the compact set $\Sigma \setminus U$ the class $L$ is positive, because $L \cdot z = 0$ for $z \in \overline{NE}(X)$ means $z \in F$; so $L \ge \lambda > 0$ there, and $D \ge -c$ on $\Sigma$ for some $c \ge 0$. Put $k_0 = 2c/\lambda + 1$. For $k \ge k_0$ the class $D + k L$ is positive on $U$, since $L \ge 0$ there, and on $\Sigma \setminus U$, since $D + k L \ge -c + k \lambda > 0$ there. So $D + k L$ is positive on $\Sigma$, hence on $\overline{NE}(X) \setminus \{0\}$, and it is ample by Kleiman's criterion, Theorem P7.3.13.

*Lemma 7.4.3, the case $C = \overline{NE}(X)$.* Here $A$ is ample by Theorem P7.3.13, and $m A$ is an ample Cartier divisor. Since $m A + t K_\Delta$ is nef if and only if $A + (t/m) K_\Delta$ is, $r(m A) = m \, r_C(A)$, and the rationality theorem gives $m \, r_C(A) = u/v$ with $v \le a(d + 1)$. The ample cone is open, so $A + t K_\Delta$ is ample for small $t > 0$ and $r_C(A) > 0$; and $r_C(A) < \infty$ because $K_\Delta \cdot z < 0$ for some $z$. Put $r = r_C(A)$ and $L' = a v \cdot (m A) + u \cdot a (K_X + \Delta)$, a Cartier divisor whose class is $a v m (A + r K_\Delta)$, nef by the definition of $r$, with $F_{L'} = C \cap (A + r K_\Delta)^\perp$. If this face were $0$, then $A + r K_\Delta$ would be positive on $\overline{NE}(X) \setminus \{0\}$, hence ample, and $A + (r + \eta) K_\Delta$ would be ample for small $\eta > 0$, against the maximality of $r$. For $z \in F_{L'} \setminus \{0\}$, $K_\Delta \cdot z = -A \cdot z / r < 0$. So $L' \in \mathcal{L}$.

*Lemma 7.4.3, the case $C = F_L$.* The set $C \cap \Sigma$ is compact and nonempty, $A \ge \alpha > 0$ on it and $K_\Delta \le -\beta < 0$ on it, so the set of admissible $t$ is a closed interval $[0, r]$ with $\alpha / \max |K_\Delta| \le r \le \max A / \beta$. By Lemma 7.4.2, $A + k L$ is ample for $k \ge k_0$; take $k$ integral. Since $m(A + k L)$ is Cartier, the first case gives $m \, r(A + k L) \in \frac1N \mathbb{Z}$, with $N = (a(d+1))!$, writing $r(\cdot)$ for the threshold on $\overline{NE}(X)$. The sequence $r_k = r(A + k L)$ is nondecreasing, because $L$ is nef, and bounded by $r$, because $L$ vanishes on $C$. A bounded nondecreasing sequence in $\frac1{mN} \mathbb{Z}$ is eventually constant, say $r_k = r_\infty$ for $k \ge k_1$.

Suppose that $r_\infty < r$, and pick $s$ with $r_\infty < s < r$. Then $A + s K_\Delta = (1 - s/r) A + (s/r)(A + r K_\Delta)$ is positive on $C \setminus \{0\}$, since the first term is positive there and the second nonnegative. By Lemma 7.4.2, $A + s K_\Delta + k L$ is ample for $k \gg 0$, so $r_k \ge s > r_\infty$ for $k \gg 0$, a contradiction. Hence $r_k = r$ for $k \ge k_1$, and $m r = m r_{k_1} = u/v$ with $v \le a(d+1)$ by the first case applied to $A + k_1 L$. This proves part 1.

For part 2, let $k = k_1 + 1$ and let $L'$ be the Cartier divisor that the first case attaches to $A + k L$; it is a positive multiple of $A + k L + r K_\Delta$. For $z \in \overline{NE}(X)$,
$$(A + k L + r K_\Delta) \cdot z = (A + k_1 L + r K_\Delta) \cdot z + L \cdot z,$$
a sum of two nonnegative terms since $r_{k_1} = r$. So $L' \cdot z = 0$ if and only if $L \cdot z = 0$ and $(A + r K_\Delta) \cdot z = 0$, that is, $F_{L'} = C \cap (A + r K_\Delta)^\perp$. This face is nonzero: the minimum of $A + r K_\Delta$ on the compact set $C \cap \Sigma$ is $0$, since a positive minimum $\mu$ would allow $t = r + \mu / \max |K_\Delta|$. It is $K_\Delta$-negative because it lies in $C$, so $L' \in \mathcal{L}$.

*Lemma 7.4.4.* Let $H$ be an ample Cartier divisor, $\Sigma = \Sigma_H$, and $W$ the span of $C$. Suppose that $B \ne C$, and pick $z_0 \in C \setminus B$. The cone $B$ is closed and convex, so by Lemma P7.4.2 there is $\psi \in N^1(X)$ with $\psi \ge 0$ on $B$ and $\psi \cdot z_0 < 0$. For small $\delta > 0$, $\psi + \delta H$ is positive on the compact set $B \cap \Sigma$ and negative at $z_0$, and both conditions are open in $N^1(X)$. Let $\Lambda \subseteq N^1(X)$ be the set of classes whose restriction to $W$ is a multiple of the restriction of $K_\Delta$. It is a linear subspace, and it is proper: the pairing is perfect (Theorem P7.2.12), so restriction $N^1(X) \to W^*$ is onto, and $\dim W^* \ge 2$. Since $N^1(X)_\mathbb{Q}$ is dense, there is $M \in N^1(X)_\mathbb{Q} \setminus \Lambda$ with $M > 0$ on $B \setminus \{0\}$ and $M \cdot z_0 < 0$.

Put $t_0 = -\min_{C \cap \Sigma} M > 0$, so $M + x H \ge 0$ on $C$ exactly for $x \ge t_0$, and pick $z_1 \in C \cap \Sigma$ with $M \cdot z_1 = -t_0$. Then $z_1 \notin B$, so $z_1 \notin C_{K_\Delta \ge 0}$ and $K_\Delta \cdot z_1 < 0$. For rational $x > t_0$ the class $A_x = M + x H$ is positive on $C \setminus \{0\}$, and $K_\Delta$ is negative somewhere on $C$, at $z_1$. Lemma 7.4.3 gives $r_x = r_C(A_x) > 0$ and $L'_x \in \mathcal{L}$ with $F_{L'_x} = C \cap (A_x + r_x K_\Delta)^\perp \ne \{0\}$.

If $F_{L'_x} = C$, then $A_x + r_x K_\Delta$ vanishes on $W$, so $(M + x H)|_W = -r_x K_\Delta|_W$. If this held for two values $x \ne x'$, subtracting would give $H|_W \in \mathbb{R} K_\Delta|_W$ and then $M|_W \in \mathbb{R} K_\Delta|_W$, that is, $M \in \Lambda$. So for all rational $x > t_0$ but at most one, $F_{L'_x} \subsetneq C$ and $F_{L'_x} \subseteq B$. Choose $z_x \in F_{L'_x} \cap \Sigma$. Then $M \cdot z_x > 0$, while
$$M \cdot z_x = -x - r_x K_\Delta \cdot z_x \le -x + c \, r_x, \qquad c = \max_\Sigma |K_\Delta|.$$
Since $A_x + r_x K_\Delta \ge 0$ at $z_1$, $(x - t_0) + r_x K_\Delta \cdot z_1 \ge 0$, so $r_x \le (x - t_0) / (-K_\Delta \cdot z_1)$, which tends to $0$ as $x \to t_0$. Then $-x + c\, r_x \to -t_0 < 0$, and $M \cdot z_x < 0$ for rational $x$ close to $t_0$, a contradiction.

*Lemma 7.4.5.* The ample cone is open and nonempty and $N^1(X)_\mathbb{Q}$ is dense, so there are ample Cartier divisors $H_1, \dots, H_\rho$ whose classes form a basis of $N^1(X)$. Let $R = F_L$ with $L \in \mathcal{L}$ be a ray, with generator $z$ normalized by $K_\Delta \cdot z = -1$. For $C = R$ and $A = H_j$, $(H_j + t K_\Delta) \cdot z = H_j \cdot z - t$, so $r_R(H_j) = H_j \cdot z$, and part 1 of Lemma 7.4.3 with $m = 1$ gives $H_j \cdot z \in \frac1N \mathbb{Z}$, $N = (a(d + 1))!$. So $z$ lies in the lattice of $N_1(X)$ dual to $\frac1N$ times the basis $(H_j)$, and in particular $z \in N_1(X)_\mathbb{Q}$. If in addition $(K_\Delta + \varepsilon H) \cdot z < 0$, then $H \cdot z < 1/\varepsilon$, and $z$ lies in the compact set $\{ w \in \overline{NE}(X) : H \cdot w \le 1/\varepsilon \}$. A compact set contains finitely many points of a lattice, and distinct rays have distinct normalized generators.

*Theorem 7.4.6, a reduction.* If $K_\Delta$ is nef, then $\overline{NE}(X) = \overline{NE}(X)_{K_\Delta \ge 0}$, there are no $K_\Delta$-negative faces, and all three parts hold with no rays. Assume from now on that $K_\Delta$ is not nef. Let $\mathcal{R}$ be the set of rays $F_L$ with $L \in \mathcal{L}$ and $\dim F_L = 1$. Two facts on faces are used. First, if $F$ is a face, then $\overline{NE}(X) \cap \operatorname{span}(F) = F$: an element $z = f_1 - f_2$ with $f_i \in F$ and $z \in \overline{NE}(X)$ has $z + f_2 = f_1 \in F$, so $z \in F$. Second, a face $F' \subsetneq F$ has smaller dimension, since equal spans would give $F = \overline{NE}(X) \cap \operatorname{span}(F) = F'$.

*Step 1: $\overline{NE}(X)$ is the closure of $\overline{NE}(X)_{K_\Delta \ge 0} + \sum_{R \in \mathcal{R}} R$.* For a face $F$ let $S(F)$ be the closure of the sum of the rays of $\mathcal{R}$ contained in $F$. By induction on $\dim F_L$, $F_L \subseteq S(F_L)$ for every $L \in \mathcal{L}$: if $\dim F_L = 1$ then $F_L \in \mathcal{R}$, and if $\dim F_L \ge 2$ then Lemma 7.4.4 with $C = F_L$, where $C_{K_\Delta \ge 0} = \{0\}$, writes $F_L$ as the closure of a sum of faces $F_{L'} \subsetneq F_L$, of smaller dimension, each contained in $S(F_{L'}) \subseteq S(F_L)$. If $\dim N_1(X) = 1$, then $\overline{NE}(X)$ is a ray on which $K_\Delta$ is negative, so $0 \in \mathcal{L}$ and $\overline{NE}(X) \in \mathcal{R}$. Otherwise Lemma 7.4.4 with $C = \overline{NE}(X)$ and the inclusions $F_L \subseteq S(F_L)$ give Step 1.

*Step 2: part 1.* Let $R_1, \dots, R_m$ be the finitely many rays of $\mathcal{R}$ on which $K_\Delta + \varepsilon H$ is negative (Lemma 7.4.5), and $V = \overline{NE}(X)_{K_\Delta + \varepsilon H \ge 0} + \sum_i R_i$. Lemma 6.2.5 says that $V$ is closed; its proof uses only that $\overline{NE}(X)$ is closed and salient (Corollary P7.3.14), so it applies here. Since $H \ge 0$ on $\overline{NE}(X)$, $V$ contains $\overline{NE}(X)_{K_\Delta \ge 0}$, and it contains every $R \in \mathcal{R}$, either as some $R_i$ or because $(K_\Delta + \varepsilon H) \cdot R \ge 0$. By Step 1, $V = \overline{NE}(X)$. Each $R_i$ is a one-dimensional face, so a $K_\Delta$-negative extremal ray.

*Step 3: part 2.* Let $R$ be a $K_\Delta$-negative extremal ray with generator $z$, and choose $\varepsilon > 0$ with $(K_\Delta + \varepsilon H) \cdot z < 0$. Write $z = w + \sum_i a_i z_i$ by part 1, with $w \in \overline{NE}(X)_{K_\Delta + \varepsilon H \ge 0}$, $a_i \ge 0$ and $z_i$ a generator of $R_i$. Extremality puts every summand in $R$, so $w = 0$ and $R = R_i$ for some $i$. Hence the $K_\Delta$-negative extremal rays are exactly the rays of $\mathcal{R}$, which are exposed and rational by Lemma 7.4.5; those that are $(K_\Delta + \varepsilon H)$-negative are finite in number, and $I$ is the union of these finite sets over $\varepsilon = 1/j$, so it is countable. Finally $\overline{NE}(X)$ is closed and salient, so by part 3 of Proposition P7.4.5 every $z \in \overline{NE}(X)$ is a finite sum of elements of extremal rays, each of which is either some $R_i$ or lies in $\overline{NE}(X)_{K_\Delta \ge 0}$.

*Step 4: part 3.* The face $F$ is $K_\Delta$-negative, so $K_\Delta \le -\beta < 0$ on the compact set $F \cap \Sigma_H$; take $\varepsilon < \beta$, so that $K_\Delta + \varepsilon H < 0$ on $F \setminus \{0\}$, and write part 1 for this $\varepsilon$. Let $I_F$ be the set of $i$ with $R_i \subseteq F$. For $z \in F$, a decomposition $z = w + \sum a_i z_i$ has all its summands in $F$, so $w \in F_{K_\Delta + \varepsilon H \ge 0} = \{0\}$ and $a_i = 0$ for $i \notin I_F$. Hence $F = \sum_{i \in I_F} R_i$. The existence of $L$ is part of Corollary 7.4.7, proved next.

*Corollary 7.4.7.* Keep the notation of Step 4 and put $V = \overline{NE}(X)_{K_\Delta + \varepsilon H \ge 0} + \sum_{i \notin I_F} R_i$, closed by Lemma 6.2.5, so $\overline{NE}(X) = V + F$. Let $W = \operatorname{span}(F)$. If $v \in V \cap W$, then $v \in \overline{NE}(X) \cap W = F$, so in a decomposition $v = w + \sum_{i \notin I_F} a_i z_i$ every summand lies in $F$; then $w = 0$, and $a_i z_i \ne 0$ would give $R_i \subseteq F = \sum_{j \in I_F} R_j$, so that $z_i$ is a sum of elements of the $R_j$, each of which lies in $R_i$ by extremality, and $R_i = R_j$ for some $j \in I_F$, which is absurd. So $V \cap W = \{0\}$.

Let $\pi \colon N_1(X) \to N_1(X)/W$ be the quotient. The set $K = \pi(V \cap \Sigma_H)$ is compact, and its convex hull $\hat K$ is compact and does not contain $0$: a relation $\sum \lambda_j \pi(v_j) = 0$ with $v_j \in V \cap \Sigma_H$, $\lambda_j \ge 0$ and $\sum \lambda_j = 1$ gives $\sum \lambda_j v_j \in V \cap W = \{0\}$, against $H \cdot \sum \lambda_j v_j = 1$. A compact convex set not containing $0$ is strictly separated from $0$ by a linear form (Lemma P7.4.2), so there is a linear form $\ell$ on $N_1(X)/W$ with $\ell > 0$ on $\hat K$. Its pullback $L_0 = \ell \circ \pi \in N^1(X)$ vanishes on $W$ and is positive on $V \setminus \{0\}$. The space $W$ is spanned by the rational generators of the $R_i$, $i \in I_F$, so $W^\perp \subseteq N^1(X)$ is defined over $\mathbb{Q}$ and its rational points are dense in it; positivity on the compact set $V \cap \Sigma_H$ is an open condition, so $L_0$ may be taken rational, and a positive multiple $L$ of it is Cartier. For $z = v + f$ with $v \in V$ and $f \in F$, $L \cdot z = L \cdot v \ge 0$, with equality only for $v = 0$. So $L$ is nef with $F_L = F$, and $L \in \mathcal{L}$. This also completes Step 4.

For the last assertion, let $M \cdot F = 0$. On $V \cap \Sigma_H$, $L \ge \lambda > 0$, while $|M|$ and $|K_\Delta|$ are bounded by some $c$, so for $k \ge k_0 = 3c / \lambda$ both $k L + M$ and $k L + M - K_\Delta$ are positive on $V \setminus \{0\}$. For $z = v + f \in \overline{NE}(X)$, $(k L + M) \cdot z = (k L + M) \cdot v \ge 0$, with equality only if $v = 0$, so $k L + M$ is nef with $F_{kL + M} = F$; and $(k L + M - K_\Delta) \cdot z = (kL + M - K_\Delta) \cdot v - K_\Delta \cdot f$, which is positive unless $v = f = 0$. By Theorem P7.3.13, $k L + M - K_\Delta$ is ample.

*Corollary 7.4.8.* Take $H = -K_\Delta$ and $\varepsilon = \frac12$ in part 1. Then $K_\Delta + \varepsilon H = \frac12 K_\Delta$ is negative on $\overline{NE}(X) \setminus \{0\}$, so the first summand is $\{0\}$ and $\overline{NE}(X) = \sum_{i=1}^m R_i$, with each $R_i$ spanned by a rational class.

### Exercises

1. (A) In Example 7.4.9, compute $r(H)$ for $H = (2, 3)$ and identify the face cut out by $H + r(H) K_\Delta$. Check the denominator bound.
2. (A) Let $X = \mathbb{P}^2$ and $\Delta = c \ell$ for a line $\ell$ and $0 \le c < 1$ rational. Compute $r(\mathcal{O}(1))$ and check that it has the form $u/v$ with $v \le a \cdot 3$, where $a$ is the denominator of $c$.
3. (B) Show that Lemma 7.4.2 fails if $D$ is only assumed nonnegative on $F$: take $X = \mathbb{P}^1 \times \mathbb{P}^1$, $L = (1, 0)$ and $D = (-1, 0)$.
4. (B) Prove that every extremal face of $\overline{NE}(X)$ that is the sum of finitely many rational rays and meets $\overline{NE}(X)_{K_\Delta \ge 0}$ only in $0$ is exposed, using only the argument of Corollary 7.4.7.
5. (B) Let $X$ be as in Example 7.4.10. List all faces of $\overline{NE}(X)$ and the divisors of $\mathcal{L}$ that cut them out, up to positive multiples.
6. (C) Let $F$ be a $K_\Delta$-negative extremal face. Show that every face of $F$ is a $K_\Delta$-negative extremal face of $\overline{NE}(X)$, that $F$ has only finitely many faces, and that each of them is exposed.

### Lean

The library has `MinimalModel.ConeTheoremKlt`, with conclusion `MinimalModel.ConeDecomposition`, for projective klt pairs in characteristic $0$, and `MinimalModel.RationalityTheorem`, the input of Lemma 7.4.3, both as statements without proof. `MinimalModel.KleimanCriterion` is Theorem P7.3.13. Lemmas 7.4.2 to 7.4.5 and the corollaries are not yet in Lean.

### Notes and history

The cone theorem for klt pairs was proved by Kawamata, with contributions of Reid, Shokurov and Kollár, through the rationality and base point free theorems; the standard account is KMM87, and the proof here follows KM98, Theorem 3.15, and Matsuki's Chapter 8 (Mat02). The proof of Lemma 7.4.4 by thresholds replaces Mori's bend-and-break: no rational curve appears in this section, and the rays are found as exposed faces. The rational curves and the length bound $2d$ come from Kawamata's theorem of Section 2. In KM98 the boundary may have real coefficients, and the case of real coefficients reduces to the rational case by a perturbation of $\Delta$.
