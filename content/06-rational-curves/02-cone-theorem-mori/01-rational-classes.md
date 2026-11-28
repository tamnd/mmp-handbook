---
title: Rational curves of small anticanonical degree
nodes: []
sources: [Mor82, KM98, Kol96, Deb01]
reads_with: [KM98:1.3, Deb01:ch6, Kol96:III.1]
requires: [1.1, P7.2, P7.3, P7.4, P8.2, 6.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Rational curves of small anticanonical degree

### Statement

Let $X$ be a smooth projective variety of dimension $n$ over an algebraically closed field $k$ of any characteristic. For a class $\delta \in N^1(X)$ write $\overline{NE}(X)_{\delta \ge 0} = \{ z \in \overline{NE}(X) : \delta \cdot z \ge 0 \}$, and similarly with $>$, $\le$ and $<$. This section proves the three ingredients of the cone theorem: a degree bound for rational curves measured by an ample $\mathbb{Q}$-divisor, the decomposition of every rational class into classes of small anticanonical degree, and a finiteness statement.

**Lemma 6.2.1 (the degree bound for $\mathbb{Q}$-divisors).** Let $A$ be an ample $\mathbb{Q}$-divisor on $X$ and $C \subseteq X$ an integral curve with $K_X \cdot C < 0$. There is a rational curve $\Gamma \subseteq X$ with
$$A \cdot \Gamma \le \frac{2n \, A \cdot C}{-K_X \cdot C}.$$

Lean: not yet in Lean.

**Proposition 6.2.2 (rational classes decompose).** Let $\Gamma \subseteq X$ be a rational curve. Then there are finitely many rational curves $\Gamma_1, \dots, \Gamma_r$ and $\Gamma'_1, \dots, \Gamma'_s$, with $0 < -K_X \cdot \Gamma_i \le n + 1$ and $K_X \cdot \Gamma'_j \ge 0$, and positive integers $a_i$, $b_j$, such that
$$[\Gamma] = \sum_{i=1}^r a_i [\Gamma_i] + \sum_{j=1}^s b_j [\Gamma'_j].$$

Lean: not yet in Lean.

**Definition 6.2.3 (the cone of small rational curves).** Let $\mathcal{R}$ be the set of rational curves $\Gamma \subseteq X$ with $0 < -K_X \cdot \Gamma \le n + 1$. Put
$$W' = \overline{NE}(X)_{K_X \ge 0} + \sum_{\Gamma \in \mathcal{R}} \mathbb{R}_{\ge 0} [\Gamma] \subseteq \overline{NE}(X),$$
the set of finite sums, and let $W$ be its closure. Both are convex cones, and by Proposition 6.2.2 the class of every rational curve on $X$ lies in $W'$.

**Lemma 6.2.4 (finiteness of the steep classes).** Let $H$ be an ample $\mathbb{R}$-divisor and $\varepsilon > 0$. The set of classes $[\Gamma]$ with $\Gamma \in \mathcal{R}$ and $(K_X + \varepsilon H) \cdot \Gamma < 0$ is finite.

Lean: not yet in Lean.

**Lemma 6.2.5 (sums of closed subcones).** Let $K_1, K_2 \subseteq \overline{NE}(X)$ be closed convex cones. Then $K_1 + K_2$ is closed. In particular the sum of a closed convex subcone of $\overline{NE}(X)$ and finitely many rays of $\overline{NE}(X)$ is closed.

Lean: not yet in Lean.

### Proof in words

Corollary P8.2.11 and Theorem P8.2.12 give the degree bound for an integral ample divisor, and both sides of the bound are linear in $A$, so it passes to $\mathbb{Q}$-divisors by clearing denominators. The decomposition is an induction on the degree against a fixed ample divisor: a rational curve of anticanonical degree at least $n + 2$ breaks by Corollary 6.1.4 into rational cycles of smaller degree, and the induction stops at curves that are either $K_X$-nonnegative or of anticanonical degree at most $n + 1$. Finiteness holds because a $(K_X + \varepsilon H)$-negative curve of $\mathcal{R}$ has $H$-degree less than $(n + 1)/\varepsilon$, and curve classes are lattice points of a compact slice of the cone. The last lemma is the compactness of the slice once more: in a salient cone the summands of a bounded sequence of sums stay bounded.

### Examples

**Example 6.2.6 (projective space).** On $\mathbb{P}^n$ every rational curve of degree $d$ has class $d [L]$, and $\mathcal{R}$ is the set of lines, since $-K \cdot \Gamma = (n + 1) d \le n + 1$ forces $d = 1$. Proposition 6.2.2 is the decomposition $[\Gamma] = d [L]$, and the induction of its proof breaks $\Gamma$ in at most $d - 1$ steps. Here $W' = \mathbb{R}_{\ge 0} [L] = \overline{NE}(\mathbb{P}^n)$.

**Example 6.2.7 (the plane blown up at a point).** Let $X = \operatorname{Bl}_p \mathbb{P}^2$ with $h$ the pullback of the class of a line and $e$ the exceptional curve, so $-K_X = 3h - e$ in $N^1$ and, in $N_1$, a curve has class $a [\ell] - b [e]$ with $a = h \cdot C$ and $b = e \cdot C$, where $[\ell]$ is the class of the pullback of a general line. The strict transform $\Gamma$ of a rational curve of degree $a$ with multiplicity $b$ at $p$ has $-K_X \cdot \Gamma = 3a - b$, and $0 \le b \le a$ for $\Gamma \ne e$. Proposition 6.2.2 writes $[\Gamma] = b [\tilde\ell] + (a - b) [\ell]$, where $\tilde\ell = \ell - e$ is the strict transform of a line through $p$ with $-K_X \cdot \tilde\ell = 2$, and $\ell = \tilde\ell + e$ with $-K_X \cdot e = 1$. All classes are in $\langle [e], [\tilde\ell] \rangle$, and $\mathcal{R}$ contains $e$, the lines $\tilde\ell$ and the pullbacks of general lines ($-K_X \cdot \ell = 3 = n + 1$).

**Example 6.2.8 (no rational curves).** If $X$ contains no rational curve, for example an abelian variety or a product of curves of genus at least $1$, then $\mathcal{R} = \emptyset$ and $W' = \overline{NE}(X)_{K_X \ge 0}$. The cone theorem of the next section then says that $K_X$ is nef, which is Theorem P8.2.13 read backwards: a variety whose canonical class is not nef contains a rational curve.

### Proof

*Lemma 6.2.1.* Let $m \ge 1$ be an integer with $m A$ an integral ample divisor, and $\nu \colon \tilde C \to C$ the normalization, a smooth projective curve with $\nu_* \tilde C = C$, so $-K_X \cdot \nu_* \tilde C = -K_X \cdot C > 0$. By part 4 of Theorem 6.1.2, applied to $\nu$ and $mA$, there is a rational curve $\Gamma$ with $m A \cdot \Gamma \le 2n \, m A \cdot C / (-K_X \cdot C)$. Divide by $m$.

*Proposition 6.2.2.* Fix an integral very ample divisor $H$. Then $H \cdot \Gamma$ is a positive integer for every curve, and the proof is by induction on $H \cdot \Gamma$. If $K_X \cdot \Gamma \ge 0$, take $s = 1$ and $\Gamma'_1 = \Gamma$. If $0 < -K_X \cdot \Gamma \le n + 1$, take $r = 1$ and $\Gamma_1 = \Gamma$. Otherwise $-K_X \cdot \Gamma \ge n + 2$, and Corollary 6.1.4 gives $[\Gamma] = [Z_1] + [Z_2]$ with $Z_1$, $Z_2$ nonzero rational $1$-cycles, all of whose components $\Gamma''$ have $H \cdot \Gamma'' < H \cdot \Gamma$. By induction each component is a positive integral combination of classes of the required kind, and so is $[\Gamma] = \sum c_k [\Gamma''_k]$ with $c_k$ the multiplicities.

*Lemma 6.2.4.* If $\Gamma \in \mathcal{R}$ and $(K_X + \varepsilon H) \cdot \Gamma < 0$, then $\varepsilon H \cdot \Gamma < -K_X \cdot \Gamma \le n + 1$, so $[\Gamma]$ lies in $T = \{ z \in \overline{NE}(X) : H \cdot z \le (n + 1)/\varepsilon \}$. By Corollary P7.3.14 the slice $\{ z \in \overline{NE}(X) : H \cdot z = 1 \}$ is compact, so $T$, the union of its multiples by $t \in [0, (n + 1)/\varepsilon]$, is compact. The class of a curve lies in $N_1(X)_\mathbb{Z}$, which is a lattice by Theorem P7.2.12, so it is discrete, and a discrete subset of a compact set is finite.

*Lemma 6.2.5.* Let $H$ be ample, so $H \cdot z > 0$ for $z \in \overline{NE}(X) \setminus \{0\}$ (Corollary P7.3.14). Let $z_m = u_m + v_m$ with $u_m \in K_1$, $v_m \in K_2$, and $z_m \to z$. Then $H \cdot u_m + H \cdot v_m = H \cdot z_m$ is bounded, and $H \cdot u_m, H \cdot v_m \ge 0$, so $u_m$ and $v_m$ lie in a set $\{ y \in \overline{NE}(X) : H \cdot y \le c \}$, which is compact as in the proof of Lemma 6.2.4. After passing to a subsequence, $u_m \to u \in K_1$ and $v_m \to v \in K_2$, since $K_1$, $K_2$ are closed, and $z = u + v \in K_1 + K_2$. A finite set of rays of $\overline{NE}(X)$ spans a closed convex cone, a polyhedral cone (Proposition P7.4.4), so the second statement follows from the first.

### Exercises

1. (A) In Lemma 6.2.1 take $X = \mathbb{P}^n$, $A = \mathcal{O}(1)$ and $C$ a curve of degree $d$. Check that the bound gives $A \cdot \Gamma \le 2n/(n + 1) < 2$, so $\Gamma$ is a line.
2. (A) Let $X = \mathbb{P}^1 \times \mathbb{P}^2$ and $\Gamma$ a rational curve of class $a [\ell_1] + b [\ell_2]$. Write down the decomposition of Proposition 6.2.2 obtained by breaking, and the members of $\mathcal{R}$ that appear.
3. (B) Show that the bound $n + 1$ in Definition 6.2.3 cannot be lowered in general: on $\mathbb{P}^n$ every rational curve has $-K \cdot \Gamma \ge n + 1$.
4. (B) Let $H = \mathcal{O}(1)$ on $\mathbb{P}^n$. List the classes of Lemma 6.2.4 for each $\varepsilon > 0$, and find the value of $\varepsilon$ at which the set becomes empty.
5. (B) Show by an example in $\mathbb{R}^3$ that the sum of two closed convex cones need not be closed when the ambient cone is not salient, and explain where the proof of Lemma 6.2.5 uses salience.
6. (C) Let $X$ be a smooth projective surface with a rational curve $\Gamma$ of self-intersection $\Gamma^2 \ge 0$ and $-K_X \cdot \Gamma \ge 4$. Use the adjunction formula to show $\Gamma^2 \ge 2$, and show that the breaking of Proposition 6.2.2 can be realized by curves through two fixed points of $\Gamma$.

### Lean

The library states the cone theorem for klt pairs as `MinimalModel.ConeTheoremKlt`, with the conclusion `MinimalModel.ConeDecomposition`, in characteristic $0$. It has no families of rational curves, so Lemma 6.2.1, Proposition 6.2.2, Lemma 6.2.4 and Lemma 6.2.5 are not yet in Lean.

### Notes and history

The decomposition of Proposition 6.2.2 by repeated breaking is Mori's (Mor82), and it is the form in which bend-and-break enters the proof of the cone theorem in KM98, Section 1.3, Kol96, Chapter III.1, and Debarre's Chapter 6 (Deb01). The finiteness of Lemma 6.2.4 is what makes the extremal rays discrete away from $K_X^\perp$.
