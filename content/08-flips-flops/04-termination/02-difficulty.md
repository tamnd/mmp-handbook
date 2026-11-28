---
title: Shokurov's difficulty and termination for terminal and canonical 3-folds
nodes: []
sources: [Sho85, KMM87, KM98, Lip78]
reads_with: [KMM87:ch5, KM98:6]
requires: [3.3, 4.1, 4.2, 4.3, 4.4, 4.6, P8.13]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Shokurov's difficulty and termination for terminal and canonical 3-folds

### Statement

The ground field $k$ is algebraically closed of characteristic $0$. A *sequence of flips* is a sequence $X_0 \dashrightarrow X_1 \dashrightarrow X_2 \dashrightarrow \cdots$ in which each $X_i \dashrightarrow X_{i+1}$ is the flip of a flipping contraction $\varphi_i \colon X_i \to Z_i$ of $(X_i, 0)$, in the sense of Definition 8.4.1. The varieties need not be projective, and no extremality or $\mathbb{Q}$-factoriality is assumed.

**Definition 8.4.8 (difficulty).** Let $X$ be a normal variety with $K_X$ $\mathbb{Q}$-Cartier. Its *difficulty* is
$$d(X) = \#\{ E \text{ exceptional over } X : a(E, X) < 1 \},$$
a number in $\{0, 1, 2, \dots\} \cup \{\infty\}$.

**Lemma 8.4.9 (the difficulty is finite).** Let $X$ be a canonical variety and $f \colon Y \to X$ a resolution, with exceptional prime divisors $E_1, \dots, E_k$ on $Y$. Every exceptional divisor $E$ over $X$ with $a(E, X) < 1$ is one of the $E_i$, so $d(X) \le k$. If $X$ is terminal and $K_X$ is Cartier, then $d(X) = 0$.

Lean: not yet in Lean.

**Lemma 8.4.10 (a crepant divisor over a curve of singular points).** Let $X$ be a canonical 3-fold and $C \subset X$ a curve with $X$ singular at the generic point of $C$. Then there is a divisor $E$ over $X$ with centre $C$ and $a(E, X) = 0$.

Lean: not yet in Lean.

**Theorem 8.4.11 (termination of terminal 3-fold flips, Shokurov).** Let $X_0$ be a terminal 3-fold, so that $d(X_0) < \infty$ by Lemma 8.4.9. Every $X_i$ in a sequence of flips starting at $X_0$ is terminal and
$$d(X_{i+1}) \le d(X_i) - 1.$$
So the sequence has at most $d(X_0)$ flips.

Lean: not yet in Lean.

**Theorem 8.4.12 (termination of canonical 3-fold flips).** Let $X_0$ be a canonical 3-fold. Every $X_i$ in a sequence of flips starting at $X_0$ is canonical, $d(X_{i+1}) \le d(X_i) - 1$, and the sequence has at most $d(X_0)$ flips.

Lean: not yet in Lean.

**Corollary 8.4.13 (flips pass through points of higher index).** Let $X$ be a terminal 3-fold and $\varphi \colon X \to Z$ a flipping contraction that has a flip. Then the flipping locus contains a point at which $K_X$ is not Cartier. In particular a terminal 3-fold with $K_X$ Cartier has no flips, and a sequence of flips of a terminal 3-fold has at most $\sum_P d_P$ steps, where $P$ runs over the finitely many points of index at least $2$ and $d_P$ is the number of exceptional divisors with centre $P$ and discrepancy less than $1$.

Lean: not yet in Lean.

### Proof in words

Discrepancies go up under a flip, by Lemma 8.4.2, so every divisor counted by $d(X^+)$ is counted by $d(X)$. It is enough to find one divisor counted by $d(X)$ and not by $d(X^+)$. Take a flipped curve $C^+$. The 3-fold $X^+$ is terminal, so it is smooth at the generic point of $C^+$, and the blow-up of $C^+$ there gives a divisor $E$ with $a(E, X^+) = 1$. Its centre on $Z$ is a point of the flipped locus, so $a(E, X) < 1$ by the strict inequality. So $d$ drops by at least one. For canonical $X^+$, the same works once $X^+$ is smooth at the generic point of $C^+$; if it were not, a crepant divisor over $C^+$, given by the minimal resolution of the surface singularity at the generic point, would have discrepancy $0$ over $X^+$ and negative discrepancy over $X$, which is impossible. The finiteness of $d$ comes from a resolution: every divisor that is exceptional over a resolution has discrepancy at least $1$ over the resolution, and the canonical condition keeps the correction term nonnegative.

### Examples

**Example 8.4.14 (the point $\frac12(1,1,1)$).** Let $X = \frac12(1,1,1)$ and $f \colon Y \to X$ the weighted blow-up of Example 4.4.8, with $Y$ the total space of $\mathcal{O}_{\mathbb{P}^2}(-2)$, smooth, and one exceptional divisor $E \cong \mathbb{P}^2$ with $a(E, X) = \frac12$ (Example 4.2.25). So $X$ is terminal, and Lemma 8.4.9 for this resolution gives $d(X) \le 1$, while $E$ is counted, so $d(X) = 1$. A terminal 3-fold whose only singular points are $s$ points of type $\frac12(1,1,1)$ has $d = s$, and by Theorem 8.4.11 any sequence of flips starting at it has at most $s$ steps.

**Example 8.4.15 (the ordinary double point).** Let $X = \{xy = zw\} \subset \mathbb{A}^4$ and $f \colon Y \to X$ the blow-up of the plane $\{x = z = 0\}$, a small resolution with exceptional curve $C \cong \mathbb{P}^1$ (Volume 3, Example 3.5.23). Since $f$ is small, $K_Y - f^* K_X$ is supported on no divisor and is $0$, so every exceptional divisor over $X$ is exceptional over the smooth variety $Y$, and $a(E, X) = a(E, Y) \ge 1$ by Proposition P8.13.4. So $d(X) = 0$, as Lemma 8.4.9 predicts, since $K_X$ is Cartier and $X$ is terminal (Example 4.4.20). The blow-up of the vertex has discrepancy exactly $1$.

**Example 8.4.16 (the Francia flip, counted).** In Example 8.4.5, $X^-$ has one singular point, of type $\frac12(1,1,1)$, so $d(X^-) = 1$ by Example 8.4.14, and $X^+$ is smooth, so $d(X^+) = 0$. The divisor that Theorem 8.4.11 produces is the blow-up $E_v$ of $C^+$, with $a(E_v, X^+) = 1$, and it is the one divisor counted by $d(X^-)$, with $a(E_v, X^-) = \frac12$. So the bound of Theorem 8.4.11 is attained: one flip, and $d$ drops from $1$ to $0$.

**Example 8.4.17 (the points $\frac1r(1, -1, a)$).** Let $r \ge 2$ and $1 \le a < r$ with $\gcd(a, r) = 1$, and let $X = \frac1r(1, -1, a)$, terminal by the terminal lemma, Theorem 4.4.6. In the toric description, Lemma 4.4.3, $N = \mathbb{Z}^3 + \mathbb{Z} \frac1r(1, -1, a)$ and $X$ is the cone $\operatorname{Cone}(e_1, e_2, e_3)$. For $1 \le i \le r - 1$ let $\bar{\imath}$ be the residue of $ai$ modulo $r$ in $\{1, \dots, r - 1\}$, nonzero because $\gcd(a, r) = 1$, and
$$v_i = \tfrac1r \big(i, \, r - i, \, \bar{\imath}\big) \in N,$$
which is $i \cdot \frac1r(1, -1, a)$ reduced modulo $\mathbb{Z}^3$. The $v_i$ are distinct primitive vectors interior to the cone, and by Theorem 3.3.34 the divisor of the ray of $v_i$ has discrepancy $\frac1r(i + r - i + \bar{\imath}) - 1 = \frac{\bar{\imath}}{r}$, which lies in $(0, 1)$. So $d(X) \ge r - 1$. The set of discrepancies $\{ \bar{\imath}/r \}$ is $\{1/r, 2/r, \dots, (r-1)/r\}$, since $i \mapsto \bar{\imath}$ is a bijection of $\{1, \dots, r-1\}$. For $r = 2$ this is Example 8.4.14.

**Example 8.4.18 (a klt point with infinite difficulty).** Let $X = \frac14(1,1,1)$, the cone over $(\mathbb{P}^2, \mathcal{O}(4))$, and $f \colon Y \to X$ the blow-up of the vertex, with $Y$ the total space of $\mathcal{O}_{\mathbb{P}^2}(-4)$ and $E \cong \mathbb{P}^2$. By Theorem 4.2.19, $a(E, X) = -1 + \frac34 = -\frac14$, so $X$ is klt and not canonical, and $K_Y = f^* K_X - \frac14 E$. For a line $\ell \subset E$, let $F_\ell$ be the exceptional divisor of the blow-up of $Y$ along $\ell$. By Lemma P8.13.3, $a(F_\ell, X) = a(F_\ell, Y) - \frac14 \operatorname{ord}_{F_\ell} E = 1 - \frac14 = \frac34 < 1$. Distinct lines give distinct divisors, since their centres on $Y$ differ. So $d(X) = \infty$, and the canonical hypothesis of Lemma 8.4.9 cannot be dropped.

### Proof

*Lemma 8.4.9.* Write $K_Y = f^* K_X + A$ with $A = \sum_i a(E_i, X) E_i$, where only the exceptional prime divisors of $Y$ appear, by Definition P8.13.1. Since $X$ is canonical, $A \ge 0$. Let $E$ be an exceptional divisor over $X$ that is not one of the $E_i$. The prime divisors of $Y$ are the $E_i$ and the strict transforms of the prime divisors of $X$, which are not exceptional over $X$, so $E$ is not a prime divisor of $Y$. So $E$ is exceptional over $Y$, and by Lemma P8.13.3 and Proposition P8.13.4,
$$a(E, X) = a(E, Y) + \operatorname{ord}_E(A) \ge 1 + 0 = 1.$$
So every $E$ with $a(E, X) < 1$ is one of the $E_i$. If $K_X$ is Cartier, then $K_Y - f^*K_X$ is an integral divisor near every point, so every $a(E, X)$ is an integer. If $X$ is also terminal, every exceptional $E$ has $a(E, X) \ge 1$, and $d(X) = 0$.

*Lemma 8.4.10.* Let $\eta$ be the generic point of $C$ and $R = \mathcal{O}_{X, \eta}$, a normal local ring of dimension $2$, essentially of finite type over $k$, so excellent, and singular by hypothesis. A resolution of $X$ (Theorem 4.2.10), localized at $\eta$, is a resolution of $\operatorname{Spec} R$, and by Lipman's theory of two-dimensional schemes (Lip78) $\operatorname{Spec} R$ has a minimal resolution $g \colon S \to \operatorname{Spec} R$, obtained from any resolution by contracting the exceptional curves $\Gamma$ with $\Gamma^2 < 0$ and $K \cdot \Gamma < 0$. The exceptional curves $\Gamma_1, \dots, \Gamma_s$ of $g$ are curves over the residue field $\kappa(\eta)$, $s \ge 1$ because $R$ is singular, and the arguments of Volume 4, Chapter 3, hold for them with intersection numbers taken over $\kappa(\eta)$: the intersection matrix is negative definite (Theorem 4.3.1), $K_S$ is $g$-nef on the minimal resolution (part 1 of Proposition 4.3.5), and the negativity lemma (Lemma 4.3.2) holds. Write $K_S = g^* K + \sum_j a_j \Gamma_j$, which makes sense because $K_X$ is $\mathbb{Q}$-Cartier. The divisor $B = -\sum_j a_j \Gamma_j$ has $B \cdot \Gamma_l = -K_S \cdot \Gamma_l \le 0$ for every $l$, so $B \ge 0$ by Lemma 4.3.2 and every $a_j \le 0$. Each $\Gamma_j$ defines a divisorial valuation of $k(X)$ with centre $\eta$, that is, a divisor $E_j$ over $X$ with centre $C$, and $a(E_j, X) = a_j$, because discrepancies are computed at the generic point of the divisor and the localization of a model of $X$ at $E_j$ is the local ring of $S$ at $\Gamma_j$. Since $X$ is canonical, $a_j \ge 0$. So $a(E_1, X) = 0$.

*Theorem 8.4.11 and Theorem 8.4.12.* Let $X = X_i$, $\varphi = \varphi_i \colon X \to Z$, and $X^+ = X_{i+1}$ with $\varphi^+ \colon X^+ \to Z$. By Corollary 8.4.4, if $X$ is terminal or canonical, so is $X^+$. By induction every $X_i$ is terminal, or canonical, and $d(X_i) < \infty$ by Lemma 8.4.9.

Let $E$ be an exceptional divisor over $X^+$ with $a(E, X^+) < 1$. It is exceptional over $X$, and $a(E, X) \le a(E, X^+) < 1$ by Lemma 8.4.2. So the divisors counted by $d(X^+)$ are among those counted by $d(X)$, and it suffices to find one divisor counted by $d(X)$ and not by $d(X^+)$.

The morphism $\varphi^+$ is not an isomorphism. If it were, $K_Z$ would be $\mathbb{Q}$-Cartier, and $K_X$ and $\varphi^* K_Z$ would be $\mathbb{Q}$-Cartier divisors that agree outside $\operatorname{Ex}(\varphi)$, which has codimension at least $2$, so $K_X \sim_{\mathbb{Q}} \varphi^* K_Z$ would be numerically trivial on the curves contracted by $\varphi$; but $-K_X$ is $\varphi$-ample and $\varphi$ is not an isomorphism, so it contracts a curve, a contradiction. By Zariski's main theorem $\varphi^+$ has a positive dimensional fibre, and since $\varphi^+$ is small and $\dim X^+ = 3$, the fibre contains a curve $C^+$, contracted to a point $z \in Z$. By part 1 of Lemma 8.4.2, $z \in S = \varphi(\operatorname{Ex}(\varphi))$.

The variety $X^+$ is smooth at the generic point of $C^+$. In the terminal case this is Theorem 4.4.15. In the canonical case, if $X^+$ were singular at the generic point of $C^+$, Lemma 8.4.10 would give a divisor $E$ over $X^+$ with centre $C^+$ and $a(E, X^+) = 0$; its centre on $Z$ is $z \in S$, so part 3 of Lemma 8.4.2 would give $a(E, X) < 0$, and $E$ is exceptional over $X$, against the hypothesis that $X$ is canonical.

So there is an open set $U \subseteq X^+$, smooth, with $U \cap C^+$ a nonempty smooth closed curve in $U$. Let $E_0$ be the exceptional divisor of the blow-up of $U$ along $U \cap C^+$. By part 1 of Proposition P8.13.4 and Corollary 4.1.15, $a(E_0, X^+) = 1$, so $E_0$ is not counted by $d(X^+)$. Its centre on $X^+$ is $C^+$, and its centre on $Z$ is $\varphi^+(C^+) = z \in S$, so $a(E_0, X) < a(E_0, X^+) = 1$ by part 3 of Lemma 8.4.2, and $E_0$ is exceptional over $X$. So $E_0$ is counted by $d(X)$. This proves $d(X^+) \le d(X) - 1$. Since $d \ge 0$, a sequence of flips starting at $X_0$ has at most $d(X_0)$ steps.

*Corollary 8.4.13.* The divisor $E_0$ of the proof above has $a(E_0, X) < 1$ and centre $c_X(E_0) \subseteq \varphi^{-1}(z) \subseteq \operatorname{Ex}(\varphi)$. If $c_X(E_0)$ were a curve, $X$ would be smooth at its generic point by Theorem 4.4.15, and $E_0$ would be exceptional over a smooth open subset of $X$, so $a(E_0, X) \ge 1$ by Proposition P8.13.4 and Corollary 4.1.15. So $c_X(E_0)$ is a point $P \in \operatorname{Ex}(\varphi)$. If $K_X$ were Cartier near $P$, the discrepancies of divisors with centre $P$ would be positive integers, by the argument of Lemma 8.4.9 on a neighbourhood of $P$, and $a(E_0, X) \ge 1$. So $K_X$ is not Cartier at $P$. If $K_X$ is Cartier everywhere, no flip exists. For the bound, the divisors counted by $d(X)$ have centres at singular points, by the same argument with Theorem 4.4.15, and the singular points of index $1$ contribute nothing, so $d(X) = \sum_P d_P$, and Theorem 8.4.11 gives the bound.

### Exercises

1. (A) Let $X = \frac13(1,2,1) = \frac13(1,-1,1)$. Find the two vectors $v_1, v_2$ of Example 8.4.17 and their discrepancies, and check that $v_1 + v_2 = e_1 + e_2 + e_3$.
2. (A) Let $X = \frac13(1,1,1)$, the cone over $(\mathbb{P}^2, \mathcal{O}(3))$. Show that $X$ is canonical and not terminal, and that $d(X) = 1$, using the blow-up of the vertex.
3. (B) Let $X = S \times \mathbb{A}^1$ with $S$ the $A_1$ surface singularity, as in Example 4.4.21. Compute $d(X)$ and identify the crepant divisor of Lemma 8.4.10 over the curve of singular points.
4. (B) Show that the conclusion $d(X^+) \le d(X) - 1$ of Theorem 8.4.11 holds with $d(X^+) \le d(X) - c$, where $c$ is the number of irreducible components of the flipped locus.
5. (B) Let $X$ be a terminal 3-fold all of whose singular points are of type $\frac1r(1, -1, a)$ for various $r$. Assuming that $d_P = r_P - 1$ for each such point (a theorem of Kawamata on the economic resolution), bound the number of flips in a sequence starting at $X$ by $\sum_P (r_P - 1)$.
6. (C) Let $X$ be a klt variety of dimension at least $2$ that is not canonical. Show that $d(X) = \infty$: on a resolution $Y$ on which a divisor $E$ with $-1 < a(E, X) < 0$ appears, blow up general curves, or points if $\dim X = 2$, of $E$ and compute with Lemma P8.13.3 as in Example 8.4.18. Explain which step of the proof of Theorem 8.4.12 needs the canonical hypothesis besides Lemma 8.4.9.

### Lean

The library has `MinimalModel.IsTerminal` and `MinimalModel.IsFlip`, and `MinimalModel.ThreefoldTermination` states termination of 3-fold lc flips, which contains Theorem 8.4.11 and Theorem 8.4.12; it is a statement without proof. The difficulty is not yet in Lean.

### Notes and history

The difficulty is Shokurov's, from the appendix to his nonvanishing paper (Sho85), where it proves Theorem 8.4.11. KMM87, Chapter 5, gives the proof and the extension to canonical 3-folds, and KM98, Chapter 6, gives the version for pairs. The argument is the model for every termination proof that counts divisors: the count is finite, it does not go up, and a flipped curve produces a divisor that leaves it. In dimension 4 the flipped locus can be a curve, of codimension $3$; its blow-up has discrepancy $2$ over $X^+$, the strict inequality only gives a discrepancy less than $2$ over $X$, and the count of divisors with discrepancy less than $1$ need not decrease; Section 3 explains what replaces it. Corollary 8.4.13 says that a flip of a terminal 3-fold happens only through points of index at least $2$, which is how Mori's classification of extremal neighbourhoods begins (Chapter 2).
