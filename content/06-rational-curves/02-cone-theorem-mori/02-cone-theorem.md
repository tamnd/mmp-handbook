---
title: The cone theorem for smooth varieties by Mori's method
nodes: []
sources: [Mor82, KM98, Kol96, Deb01]
reads_with: [KM98:1.24, Deb01:ch6, Kol96:III.1]
requires: [P5.12, P7.3, P7.4, P8.2, 6.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The cone theorem for smooth varieties by Mori's method

### Statement

Let $X$ be a smooth projective variety of dimension $n$ over an algebraically closed field $k$ of any characteristic, with the notation of Section 1. An *extremal ray* of $\overline{NE}(X)$ is a ray $R$ of the cone such that $u, v \in \overline{NE}(X)$ and $u + v \in R$ imply $u, v \in R$, and $R$ is $K_X$-negative if $K_X \cdot z < 0$ for $z \in R \setminus \{0\}$.

**Theorem 6.2.9 (the cone theorem, Mori).** Let $H$ be an ample divisor on $X$.

1. Every $K_X$-negative extremal ray $R$ of $\overline{NE}(X)$ is $\mathbb{R}_{\ge 0} [\Gamma]$ for a rational curve $\Gamma$ with $0 < -K_X \cdot \Gamma \le n + 1$.
2. For every $\varepsilon > 0$ there are finitely many rational curves $\Gamma_1, \dots, \Gamma_m$ with $0 < -K_X \cdot \Gamma_i \le n + 1$ such that
$$\overline{NE}(X) = \overline{NE}(X)_{K_X + \varepsilon H \ge 0} + \sum_{i=1}^m \mathbb{R}_{\ge 0} [\Gamma_i].$$
3. Let $\{ R_i \}_{i \in I}$ be the set of $K_X$-negative extremal rays. Then $I$ is countable, for every $\varepsilon > 0$ only finitely many $R_i$ are $(K_X + \varepsilon H)$-negative, and
$$\overline{NE}(X) = \overline{NE}(X)_{K_X \ge 0} + \sum_{i \in I} R_i,$$
with no closure taken on the right.

Lean: `MinimalModel.ConeTheoremKlt`, in the project library, is the cone theorem for a projective klt pair $(X, \Delta)$ in characteristic $0$ with the bound $2 \dim X$, as a statement without proof; the case $\Delta = 0$ in characteristic $0$ is parts 2 and 3 here with the weaker bound.

**Corollary 6.2.10 (the length of extremal rays).** Every $K_X$-negative extremal ray $R$ has $\ell(R) \le n + 1$, with $\ell(R)$ as in Lemma 6.1.6.

Lean: `MinimalModel.LengthOfExtremalRays`, in the project library, is the bound $\ell(R) \le 2 \dim X$ for a projective klt pair in characteristic $0$, as a statement without proof.

**Corollary 6.2.11 (supporting divisors).** Let $R$ be a $K_X$-negative extremal ray. There is a nef Cartier divisor $L$ on $X$ with $\{ z \in \overline{NE}(X) : L \cdot z = 0 \} = R$. In particular every $K_X$-negative extremal ray is exposed.

Lean: not yet in Lean.

**Corollary 6.2.12 (Fano manifolds).** If $-K_X$ is ample, then $\overline{NE}(X) = NE(X)$ is a rational polyhedral cone, spanned by the classes of finitely many rational curves $\Gamma$ with $-K_X \cdot \Gamma \le n + 1$.

Lean: not yet in Lean.

### Proof in words

Section 1 proved that the class of every rational curve lies in the cone $W'$ spanned by the $K_X$-nonnegative part and the curves of $\mathcal{R}$. The heart of the proof is that the closure $W$ of $W'$ is the whole cone. If it were not, a rational $\mathbb{Q}$-divisor $D$ would be positive on $W$ and negative somewhere on $\overline{NE}(X)$. Pushing $D$ by just enough of $H$ gives an ample $A$ that is very small on a curve $C$ on which $D$ is as negative as possible, and since that curve is $K_X$-negative by a definite amount, the degree bound of Lemma 6.2.1 produces a rational curve $\Gamma$ of small $A$-degree. But $D \cdot \Gamma > 0$, so $A \cdot \Gamma$ is at least the amount of $H$ that was added, and the two bounds contradict each other. Once $W$ is the whole cone, finiteness (Lemma 6.2.4) and closedness of finite sums (Lemma 6.2.5) give part 2, extremality gives part 1, and Minkowski's theorem, that a closed salient cone is spanned by its extremal rays, gives part 3 without a closure.

### Examples

**Example 6.2.13 (a ruled surface over an elliptic curve).** Let $E$ be an elliptic curve and $X = E \times \mathbb{P}^1$, with $f = \{ p \} \times \mathbb{P}^1$ and $s = E \times \{ q \}$. Then $K_X = p_2^* K_{\mathbb{P}^1}$, so $K_X \cdot f = -2$ and $K_X \cdot s = 0$, and $\overline{NE}(X) = \langle [s], [f] \rangle$ by Example P7.4.23. The $K_X$-nonnegative part is the ray $\mathbb{R}_{\ge 0} [s]$, which contains no rational curve, and the only $K_X$-negative extremal ray is $\mathbb{R}_{\ge 0} [f]$, spanned by the fibres of the projection to $E$, with $\ell = 2 \le n + 1 = 3$. Part 3 reads $\overline{NE}(X) = \mathbb{R}_{\ge 0} [s] + \mathbb{R}_{\ge 0} [f]$.

**Example 6.2.14 (the cubic surface).** On a smooth cubic surface $S$, $-K_S$ is ample, and Corollary 6.2.12 says that the cone is polyhedral and spanned by rational curves of anticanonical degree at most $3$. Proposition 6.1.18 identifies the extremal rays as the $27$ rays spanned by the lines, of length $1$. The conics, of degree $2$, and the twisted cubics of Example 6.1.21, of degree $3$, are in $\mathcal{R}$ but span no extremal ray.

**Example 6.2.15 (where $\varepsilon$ is needed).** Let $X$ be the blow-up of $\mathbb{P}^2$ at the nine base points of a general pencil of cubics. By Example P7.4.22, $X$ has infinitely many $(-1)$-curves $E_i$, each spanning a $K_X$-negative extremal ray of length $-K_X \cdot E_i = 1$, and $-K_X$ is the class of a fibre $F$ of the elliptic fibration, nef with $K_X^2 = 0$. The rays accumulate only on $K_X^\perp$, which meets $\overline{NE}(X)$ in the ray of $F$ among others, so the $\varepsilon$ in part 2 cannot be dropped: for each $\varepsilon > 0$ only finitely many $E_i$ are $(K_X + \varepsilon H)$-negative, and no finite set of rays together with $\overline{NE}(X)_{K_X \ge 0}$ spans the cone.

### Proof

*Step 1: $W = \overline{NE}(X)$.* Fix an integral ample divisor $H$ and the compact slice $\Sigma = \{ z \in \overline{NE}(X) : H \cdot z = 1 \}$ of Corollary P7.3.14. Suppose that $W \ne \overline{NE}(X)$ and pick $z_0 \in \overline{NE}(X) \setminus W$. By Lemma P7.4.2 there is $\psi \in W^\vee$ with $\psi(z_0) < 0$. For small $\delta > 0$ the class $\psi + \delta H$ is positive on $W \cap \Sigma$, a compact set, and negative at $z_0$. Both conditions are open, and $N^1(X)_\mathbb{Q}$ is dense in $N^1(X)$ by Theorem P7.2.12, so there is a $\mathbb{Q}$-divisor $D$ with $D \cdot w > 0$ for $w \in W \setminus \{0\}$ and $D \cdot z_0 < 0$. In particular $D \cdot \Gamma > 0$ for every rational curve $\Gamma$, because $[\Gamma] \in W'$ by Proposition 6.2.2.

Put $r = -\min_\Sigma D > 0$ and $F_0 = \{ z \in \Sigma : D \cdot z = -r \}$. A point of $F_0$ is not in $W$, so it is not in $\overline{NE}(X)_{K_X \ge 0}$, and $K_X < 0$ on $F_0$. By compactness there are $c > 0$ and $\eta_1 > 0$ with $K_X \cdot z \le -c$ for every $z \in \Sigma$ with $D \cdot z \le -r + \eta_1$: otherwise a sequence $z_m \in \Sigma$ with $D \cdot z_m \to -r$ and $K_X \cdot z_m > -1/m$ has a limit point in $F_0$ with $K_X \ge 0$.

Choose a rational number $\mu$ with $r < \mu < r (1 + c/(4n))$ and $0 < \eta \le \eta_1$ with $\eta < c r/(4n)$. The classes of effective $1$-cycles are dense in $\overline{NE}(X)$, so some effective cycle $Z$ has $D \cdot Z < (-r + \eta) H \cdot Z$, and some component $C$ of $Z$ then has $D \cdot C < (-r + \eta) H \cdot C$, since both sides are additive in $Z$. So $[C]/(H \cdot C)$ lies in $\Sigma$ with $D \le -r + \eta$, and $K_X \cdot C \le -c \, H \cdot C$.

Let $A = D + \mu H$, a $\mathbb{Q}$-divisor. On $\Sigma$, $A \ge -r + \mu > 0$, so $A$ is ample by Kleiman's criterion, Theorem P7.3.13. And $A \cdot C < (\mu - r + \eta) H \cdot C$. Lemma 6.2.1 gives a rational curve $\Gamma$ with
$$A \cdot \Gamma \le \frac{2n \, A \cdot C}{-K_X \cdot C} < \frac{2n (\mu - r + \eta)}{c} < \frac{2n}{c} \cdot \frac{c r}{2n} = r.$$
On the other hand $A \cdot \Gamma = D \cdot \Gamma + \mu H \cdot \Gamma > \mu \ge r$, since $D \cdot \Gamma > 0$ and $H \cdot \Gamma \ge 1$. This contradiction proves $W = \overline{NE}(X)$.

*Step 2: part 2.* Let $H$ be ample and $\varepsilon > 0$, and let $\Gamma_1, \dots, \Gamma_m$ be curves of $\mathcal{R}$ representing the finitely many classes of Lemma 6.2.4. Put $V = \overline{NE}(X)_{K_X + \varepsilon H \ge 0} + \sum_i \mathbb{R}_{\ge 0} [\Gamma_i]$, which is closed by Lemma 6.2.5. It contains $\overline{NE}(X)_{K_X \ge 0}$, since $H \ge 0$ on the cone, and it contains $[\Gamma]$ for every $\Gamma \in \mathcal{R}$: either $(K_X + \varepsilon H) \cdot \Gamma \ge 0$, or $[\Gamma]$ is one of the $[\Gamma_i]$. So $V \supseteq W'$, hence $V \supseteq W = \overline{NE}(X)$ by Step 1.

*Step 3: part 1.* Let $R$ be a $K_X$-negative extremal ray with generator $z$, and choose $\varepsilon > 0$ with $(K_X + \varepsilon H) \cdot z < 0$. By part 2, $z = v + \sum_i a_i [\Gamma_i]$ with $v \in \overline{NE}(X)_{K_X + \varepsilon H \ge 0}$ and $a_i \ge 0$. Since $R$ is extremal, every summand lies in $R$. Then $v = 0$, since $K_X + \varepsilon H$ is negative on $R \setminus \{0\}$, so some $a_i [\Gamma_i]$ is a nonzero element of $R$, and $R = \mathbb{R}_{\ge 0} [\Gamma_i]$. This recovers Theorem P5.12.13.

*Step 4: part 3.* By Step 3 and Lemma 6.2.4, the $(K_X + \varepsilon H)$-negative extremal rays are spanned by the finitely many classes of that lemma, and $I$ is the union over $\varepsilon = 1/m$ of these finite sets, so it is countable. The cone $\overline{NE}(X)$ is closed and salient (Corollary P7.3.14), so by part 3 of Proposition P7.4.5 every $z \in \overline{NE}(X)$ is a finite sum of elements of extremal rays. Each of these rays is either $K_X$-negative, one of the $R_i$, or lies in $\overline{NE}(X)_{K_X \ge 0}$. So $z \in \overline{NE}(X)_{K_X \ge 0} + \sum_i R_i$, and the reverse inclusion is clear.

*Corollary 6.2.10.* By part 1, $R = \mathbb{R}_{\ge 0} [\Gamma]$ with $-K_X \cdot \Gamma \le n + 1$, and $\ell(R) \le -K_X \cdot \Gamma$.

*Corollary 6.2.11.* Write $R = \mathbb{R}_{\ge 0} [\Gamma_1]$ in part 2, for an $\varepsilon$ with $(K_X + \varepsilon H) \cdot R < 0$ and $H$ integral, and put $V' = \overline{NE}(X)_{K_X + \varepsilon H \ge 0} + \sum_{[\Gamma_i] \notin R} \mathbb{R}_{\ge 0} [\Gamma_i]$, closed by Lemma 6.2.5, so that $\overline{NE}(X) = V' + R$. Then $[\Gamma_1] \notin V'$: in a decomposition of $[\Gamma_1]$ in $V'$ every summand lies in $R$ by extremality, and each summand is $0$ by the choice of $\varepsilon$ and of the $\Gamma_i$. As in Step 1, there is a $\mathbb{Q}$-divisor $M$ positive on $V' \setminus \{0\}$ with $M \cdot \Gamma_1 < 0$. Put $s = -M \cdot \Gamma_1 / H \cdot \Gamma_1$, a positive rational number, and $L = M + s H$. Then $L \cdot \Gamma_1 = 0$ and $L > 0$ on $V' \setminus \{0\}$, so for $w = v + t [\Gamma_1]$ with $v \in V'$ and $t \ge 0$, $L \cdot w = L \cdot v \ge 0$, with equality if and only if $v = 0$. So $L$ is nef with $L^\perp \cap \overline{NE}(X) = R$, and a multiple of $L$ is the class of a Cartier divisor.

*Corollary 6.2.12.* Take $H = -K_X$ and $\varepsilon = 1/2$ in part 2. Then $K_X + \varepsilon H = -\tfrac12 H$ is negative on $\overline{NE}(X) \setminus \{0\}$, so $\overline{NE}(X)_{K_X + \varepsilon H \ge 0} = 0$ and $\overline{NE}(X) = \sum_{i=1}^m \mathbb{R}_{\ge 0} [\Gamma_i]$, which is contained in $NE(X)$.

### Exercises

1. (A) On $X = E \times \mathbb{P}^1$ of Example 6.2.13, find the supporting divisor $L$ of Corollary 6.2.11 for the ray of $f$, and identify the morphism it defines.
2. (A) Check Corollary 6.2.12 on $\mathbb{P}^1 \times \mathbb{P}^1$: find the rays, the curves that span them and their anticanonical degrees.
3. (B) Show that Step 1 of the proof uses $K_X$ only through Lemma 6.2.1 and the fact that $[\Gamma] \in W'$ for every rational curve, and state the version of Step 1 for a nef divisor $N$ in place of $\overline{NE}(X)_{K_X \ge 0}$.
4. (B) Show that if $K_X$ is not nef, then some $K_X$-negative extremal ray exists, by applying part 3 of Proposition P7.4.5 to a class $z$ with $K_X \cdot z < 0$. Deduce Theorem P8.2.13 from Theorem 6.2.9.
5. (B) In Example 6.2.15, show that the classes $[E_i]$ of the $(-1)$-curves satisfy $-K_X \cdot E_i = 1$ and $H \cdot E_i \to \infty$ for a fixed ample $H$, and that $[E_i]/(H \cdot E_i)$ converges to a point of $K_X^\perp$.
6. (B) Let $X$ be smooth with $K_X$ not nef and $\rho(X) = 1$. Show that $X$ is Fano.
7. (B) Let $C$ be a smooth projective curve of genus $g \ge 2$, $e > 0$ and $X = \mathbb{P}(\mathcal{O}_C \oplus \mathcal{O}_C(-D))$ for a divisor $D$ of degree $e$, with fibre $f$ and negative section $C_0$, $C_0^2 = -e$. Show that $\overline{NE}(X) = \langle [C_0], [f] \rangle$, that $K_X \cdot C_0 = 2g - 2 + e > 0$, and that Theorem 6.2.9 holds with a single $K_X$-negative extremal ray and a $K_X$-positive one.

### Lean

The library has `MinimalModel.ConeTheoremKlt`, with conclusion `MinimalModel.ConeDecomposition`, and `MinimalModel.LengthOfExtremalRays`, both for projective klt pairs in characteristic $0$ and both as statements without proof. The case $\Delta = 0$ of each is a statement on smooth varieties in characteristic $0$ with the bound $2n$, weaker than Corollary 6.2.10. The library has no statement in positive characteristic, and Corollary 6.2.11 and Corollary 6.2.12 are not yet in Lean. `MinimalModel.KleimanCriterion` is Theorem P7.3.13, used in Step 1.

### Notes and history

The cone theorem for smooth varieties is Mori's (Mor82), proved there with the bound $n + 1$ in every characteristic. The method uses no vanishing theorem, and it is the method that works in positive characteristic, where the proof of Volume 7 is not available. The proof here follows KM98, Theorem 1.24, and Debarre's Chapter 6 (Deb01). The cone theorem for klt pairs, with the bound $2n$ for the length due to Kawamata (Kaw91), is proved in Volume 7 by the other method. Corollary 6.2.11 is the first step of the contraction theorem, and in characteristic $0$ the base point free theorem of Volume 7 makes a multiple of $L$ base point free and gives the contraction of $R$.
