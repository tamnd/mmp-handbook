---
title: Convex cones and duality
nodes: []
sources: [Ful93, Laz04, Deb01]
reads_with: [Ful93:1.2, Laz04:1.4, Deb01:ch1]
requires: [P7.2, P7.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Convex cones and duality

### Statement

Throughout, $V$ is a finite-dimensional real vector space with its Euclidean topology, $V^*$ is its dual, and $V^{**}$ is identified with $V$. The pairing of $\varphi \in V^*$ and $x \in V$ is written $\varphi(x)$ or $\varphi \cdot x$. In the applications $V = N_1(X)$ and $V^* = N^1(X)$, paired by intersection numbers (Theorem P7.2.12).

**Definition P7.4.1 (convex cones).**

1. A *convex cone* is a nonempty subset $K \subseteq V$ with $x + y \in K$ and $t x \in K$ for all $x, y \in K$ and $t \geq 0$. The convex cone *spanned* by a set $S$ is the set of finite sums $\sum_i t_i s_i$ with $t_i \geq 0$ and $s_i \in S$, written $\langle S \rangle$; it contains $0$. A convex cone is *polyhedral* if it is spanned by a finite set, and *simplicial* if it is spanned by a linearly independent finite set.
2. The *dual cone* of a convex cone $K \subseteq V$ is $K^\vee = \{ \varphi \in V^* : \varphi(x) \geq 0 \text{ for all } x \in K \}$, a convex cone in $V^*$.
3. A convex cone $K$ is *salient* if $K \cap (-K) = \{0\}$, that is, if $K$ contains no line through the origin. It is *full-dimensional* if it spans $V$ as a vector space.
4. A *face* of a convex cone $K$ is a convex subcone $F \subseteq K$ such that $u, v \in K$ and $u + v \in F$ imply $u, v \in F$. An *extremal ray* of $K$ is a face of the form $\mathbb{R}_{\geq 0} x$ with $x \neq 0$. For $\varphi \in K^\vee$ the set $K \cap \varphi^\perp$, where $\varphi^\perp = \{ x : \varphi(x) = 0 \}$, is the face *cut out* by $\varphi$.

**Lemma P7.4.2 (separation).** Let $C \subseteq V$ be a nonempty closed convex set and $v \in V \setminus C$. There is $\psi \in V^*$ with $\psi(v) < \psi(c)$ for every $c \in C$. If $C$ is a closed convex cone, $\psi$ can be taken in $C^\vee$ with $\psi(v) < 0$.

Lean: not in Lean as stated.

**Proposition P7.4.3 (duality of cones).** Let $K \subseteq V$ be a convex cone and $\overline{K}$ its closure.

1. $\overline{K}$ is a convex cone, $K^\vee$ is a closed convex cone, and $K^\vee = (\overline{K})^\vee$.
2. $(K^\vee)^\vee = \overline{K}$. In particular two closed convex cones with the same dual are equal, and the map $K \mapsto K^\vee$ is an inclusion-reversing bijection from the closed convex cones of $V$ to those of $V^*$.
3. The interior of $K^\vee$ is the set of $\varphi$ with $\varphi(x) > 0$ for every $x \in \overline{K} \setminus \{0\}$. So $K^\vee$ has nonempty interior if and only if $\overline{K}$ is salient, and $\overline{K}$ has nonempty interior, that is, $K$ is full-dimensional, if and only if $K^\vee$ is salient.
4. For $\varphi \in K^\vee$, the set $\overline{K} \cap \varphi^\perp$ is a face of $\overline{K}$, and it is $\{0\}$ if and only if $\varphi$ is in the interior of $K^\vee$.

Lean: not in Lean as stated.

**Proposition P7.4.4 (polyhedral cones).** Let $K = \langle v_1, \dots, v_m \rangle \subseteq V$.

1. (Carathéodory.) Every $x \in K$ is a nonnegative combination of a linearly independent subset of $\{ v_1, \dots, v_m \}$, and $K$ is closed.
2. Every face of $K$ is the cone spanned by the $v_i$ that it contains. So $K$ has finitely many faces, and every extremal ray of $K$ is $\mathbb{R}_{\geq 0} v_i$ for some $i$.
3. (Farkas, Minkowski and Weyl.) $K^\vee$ is polyhedral. A convex cone is polyhedral if and only if it is an intersection of finitely many closed half-spaces $\{ \varphi \geq 0 \}$.

Lean: `MinimalModel.IsRatPolyCone`, in the project library, says that a set of classes in $N^1(X)$ is the convex cone spanned by the classes of finitely many Cartier divisors, a rational polyhedral cone in the sense of part 1 of Definition P7.4.1.

**Proposition P7.4.5 (closed salient cones and their extremal rays).** Let $K \subseteq V$ be a closed salient convex cone and $h \in V^*$ a functional in the interior of $K^\vee$.

1. The slice $\Sigma_h = \{ x \in K : h(x) = 1 \}$ is compact and convex, and every nonzero $x \in K$ is a positive multiple of exactly one point of $\Sigma_h$.
2. $\mathbb{R}_{\geq 0} x$, for $x \in \Sigma_h$, is an extremal ray of $K$ if and only if $x$ is an extreme point of $\Sigma_h$, that is, $x$ is not the midpoint of two distinct points of $\Sigma_h$.
3. (Minkowski.) $\Sigma_h$ is the convex hull of its extreme points, and $K$ is the convex cone spanned by its extremal rays.

Lean: not in Lean as stated.

### Proof in words

Everything rests on separation: a point outside a closed convex set is separated from it by a hyperplane, and the hyperplane can be found through the nearest point of the set. For a cone this says that the cone is cut out by the functionals that are nonnegative on it, which is the bipolar formula $(K^\vee)^\vee = \overline{K}$. A functional is in the interior of the dual cone exactly when it is positive on the compact set of unit vectors of $\overline{K}$, and such a functional exists exactly when $\overline{K}$ contains no line. For a closed salient cone such a functional $h$ cuts a compact slice, the extremal rays are the extreme points of the slice, and Minkowski's theorem, proved by induction on the dimension through supporting hyperplanes, reconstructs the slice and the cone from them. For polyhedral cones the faces and the dual are finite objects, by Carathéodory's reduction to linearly independent generators.

For $V = N_1(X)$ and $K = NE(X)$, Section 4.2 uses part 2 of Proposition P7.4.3 to recover $\overline{NE}(X)$ from the nef cone, part 3 to see that ample classes are the interior points of the nef cone, and part 4 to attach a face of $\overline{NE}(X)$ to every nef class.

### Examples

**Example P7.4.6 (simplicial cones and dual bases).** Let $v_1, \dots, v_\rho$ be a basis of $V$ and $\varphi_1, \dots, \varphi_\rho$ the dual basis of $V^*$, with $\varphi_i(v_j) = \delta_{ij}$. Then $K = \langle v_1, \dots, v_\rho \rangle$ is the set of $x$ with $\varphi_i(x) \geq 0$ for all $i$, and
$$K^\vee = \langle \varphi_1, \dots, \varphi_\rho \rangle.$$
Indeed $\varphi = \sum_i c_i \varphi_i$ has $\varphi(v_j) = c_j$, so $\varphi \in K^\vee$ if and only if every $c_j \geq 0$. Both cones are closed, salient and full-dimensional. The faces of $K$ are the $2^\rho$ cones $\langle v_i : i \in I \rangle$, $I \subseteq \{1, \dots, \rho\}$, and the face $\langle v_i : i \in I \rangle$ is cut out by $\sum_{j \notin I} \varphi_j$. For $\rho = 2$ this is the situation of every projective variety with Picard number $2$: by Proposition P7.4.4 and part 1 of Proposition P7.4.5, a closed salient full-dimensional cone in $\mathbb{R}^2$ is spanned by its two boundary rays, so $\overline{NE}(X)$ and $\operatorname{Nef}(X)$ are each spanned by two rays, and each boundary ray of one is cut out by a boundary ray of the other. Examples P7.3.15, P7.3.16 and P7.3.17 are instances.

**Example P7.4.7 (the round cone).** Let $V = \mathbb{R}^{1 + r}$, $r \geq 1$, with the quadratic form $q(x) = x_0^2 - x_1^2 - \dots - x_r^2$ and bilinear form $b$, and identify $V$ with $V^*$ by $b$. Let $K = \{ x : q(x) \geq 0, x_0 \geq 0 \}$. Then $K$ is a closed salient full-dimensional convex cone, $K^\vee = K$, and every ray on its boundary $\{ q = 0, x_0 \geq 0 \}$ is extremal. For $x, y \in K$ the Cauchy-Schwarz inequality in $\mathbb{R}^r$ gives
$$b(x, y) = x_0 y_0 - \textstyle\sum_{i \geq 1} x_i y_i \geq x_0 y_0 - |x'| |y'| \geq 0,$$
where $x' = (x_1, \dots, x_r)$ and $|x'| \leq x_0$, $|y'| \leq y_0$. So $K \subseteq K^\vee$, and $K$ is convex, since $x \in K$ if and only if $|x'| \leq x_0$, and $|x' + y'| \leq |x'| + |y'|$. Conversely, if $y \notin K$, either $y_0 < 0$, and then $b(y, (1, 0, \dots, 0)) < 0$, or $|y'| > y_0 \geq 0$, and then $x = (|y'|, y')$ lies in $K$ with $b(y, x) = y_0 |y'| - |y'|^2 < 0$. So $K^\vee = K$. A boundary point $x \neq 0$ has $b(x, x) = 0$, so it cuts out the face $K \cap x^\perp$, which contains $x$. If $y \in K \cap x^\perp$, equality holds in both inequalities above, so $y' $ is a nonnegative multiple of $x'$ and $y_0 = |y'|$, and $y$ is a multiple of $x$. The face cut out by $x$ is therefore the ray $\mathbb{R}_{\geq 0} x$, and every boundary ray is extremal. For $r \geq 2$ the boundary contains infinitely many rays, so $K$ is not polyhedral, by part 2 of Proposition P7.4.4. This is the shape of $\overline{NE}(E \times E)$ in Example P5.12.9.

**Example P7.4.8 (cones that are not closed).** In $V = \mathbb{R}^2$, the cone $K = \{ (x, y) : y > 0 \} \cup \{ 0 \}$ is salient and its closure, the half-plane $y \geq 0$, is not. Its dual is the ray spanned by the functional $(x, y) \mapsto y$, which has empty interior, in accordance with part 3 of Proposition P7.4.3: salience of $\overline{K}$, not of $K$, is what controls the dual. The cone $K' = \{ (x, y) : x \geq 0, y > 0 \} \cup \{ 0 \}$ is not closed, its closure is the closed quadrant, and $K'$ and its closure have the same dual, the quadrant of $V^*$. The cone of curves of Mumford's surface has this shape: by Example P7.4.24 below, $NE(X)$ is contained in the union of $\{0\}$ with a half-open quadrant, and its closure is a closed quadrant whose ray $\mathbb{R}_{\geq 0} \xi$ contains no nonzero point of $NE(X)$.

### Proof

*Lemma P7.4.2.* Choose $c_0 \in C$ and put $R = |v - c_0|$ for a Euclidean norm. The set $C \cap \{ c : |v - c| \leq R \}$ is compact and nonempty, so the continuous function $c \mapsto |v - c|$ attains its minimum on it at some $w$, and $w$ is a point of $C$ nearest to $v$. Then $w \neq v$. Let $\psi(x) = \langle x, w - v \rangle$. For $c \in C$ and $0 < t \leq 1$, the point $w + t(c - w)$ is in $C$, so $|w + t(c - w) - v|^2 \geq |w - v|^2$, that is, $2t \langle c - w, w - v \rangle + t^2 |c - w|^2 \geq 0$. Dividing by $t$ and letting $t \to 0$ gives $\psi(c) \geq \psi(w)$. Also $\psi(w) - \psi(v) = |w - v|^2 > 0$, so $\psi(v) < \psi(w) \leq \psi(c)$. If $C$ is a cone, $tw \in C$ for all $t \geq 0$, and the function $t \mapsto |tw - v|^2$ has a minimum on $[0, \infty)$ at $t = 1$, so its derivative $2 \langle w, tw - v \rangle$ vanishes at $t = 1$ when $w \neq 0$, and $\psi(w) = 0$ also when $w = 0$. Then $\psi(c) \geq 0$ for all $c \in C$, so $\psi \in C^\vee$, and $\psi(v) < 0$.

*Proposition P7.4.3.* Part 1. A limit of sums and nonnegative multiples of limits is a limit of sums and multiples, so $\overline{K}$ is a convex cone. $K^\vee = \bigcap_{x \in K} \{ \varphi : \varphi(x) \geq 0 \}$ is an intersection of closed half-spaces containing $0$, so it is a closed convex cone. A functional nonnegative on $K$ is nonnegative on $\overline{K}$ by continuity, so $K^\vee = (\overline{K})^\vee$.

Part 2. For $x \in \overline{K}$ and $\varphi \in K^\vee$, $\varphi(x) \geq 0$, so $\overline{K} \subseteq (K^\vee)^\vee$. If $v \notin \overline{K}$, Lemma P7.4.2 gives $\psi \in (\overline{K})^\vee = K^\vee$ with $\psi(v) < 0$, so $v \notin (K^\vee)^\vee$. The bijection follows, with inverse again $K \mapsto K^\vee$, and it reverses inclusions since a larger cone imposes more conditions.

Part 3. Fix a Euclidean norm and let $S = \{ x \in \overline{K} : |x| = 1 \}$, a compact set. If $\varphi > 0$ on $S$, then $\varphi \geq c$ on $S$ for some $c > 0$, and every $\psi$ with operator norm $\| \psi - \varphi \| < c$ is positive on $S$, hence nonnegative on $\overline{K}$; so $\varphi$ is in the interior of $K^\vee$. Conversely, let $\varphi$ be in the interior of $K^\vee$ and $x \in \overline{K} \setminus \{0\}$. Choose $\psi \in V^*$ with $\psi(x) < 0$. For small $t > 0$, $\varphi + t\psi \in K^\vee$, so $\varphi(x) \geq -t \psi(x) > 0$. If $\overline{K}$ contains a line $\mathbb{R} x$, no functional is positive on both $x$ and $-x$, so the interior of $K^\vee$ is empty. If $\overline{K}$ is salient, the convex hull $T$ of $S$ is compact, being the image of a compact set under the continuous map $(t, s) \mapsto \sum t_i s_i$ on $\{ t_i \geq 0, \sum t_i = 1 \} \times S^{\dim V + 1}$ by Carathéodory's theorem for convex hulls, and it does not contain $0$: if $0 = \sum_i t_i s_i$ with $t_1 > 0$, then $-t_1 s_1 = \sum_{i \geq 2} t_i s_i \in \overline{K}$, so $s_1 \in \overline{K} \cap (-\overline{K}) = \{0\}$, which is false since $|s_1| = 1$. Lemma P7.4.2, applied to $T$ and $v = 0$, gives $\psi$ with $\psi > \psi(0) = 0$ on $T \supseteq S$, so $\psi$ is in the interior of $K^\vee$ (and $S = \emptyset$, $\overline{K} = \{0\}$, $K^\vee = V^*$ is the trivial case). Applying this to $K^\vee$ in place of $K$, and using part 2, $(K^\vee)^\vee = \overline{K}$ has nonempty interior if and only if $K^\vee$ is salient. A convex cone has nonempty interior if and only if it spans $V$: if it contains a basis $v_1, \dots, v_\rho$, it contains the open set $\{ \sum t_i v_i : t_i > 0 \}$, and if it spans a proper subspace, it lies in that subspace. Since $K$ and $\overline{K}$ span the same subspace, the last statement of part 3 follows.

Part 4. Let $F = \overline{K} \cap \varphi^\perp$. It is a convex subcone. If $u, v \in \overline{K}$ and $u + v \in F$, then $\varphi(u), \varphi(v) \geq 0$ and $\varphi(u) + \varphi(v) = 0$, so $\varphi(u) = \varphi(v) = 0$ and $u, v \in F$. By part 3, $F = \{0\}$ if and only if $\varphi > 0$ on $\overline{K} \setminus \{0\}$, if and only if $\varphi$ is in the interior of $K^\vee$.

*Proposition P7.4.4.* Part 1. Let $x = \sum_i a_i v_i$ with $a_i \geq 0$, and suppose that the $v_i$ with $a_i > 0$ are linearly dependent, with $\sum_i c_i v_i = 0$, $c_i = 0$ when $a_i = 0$, and some $c_i > 0$ (replace $c$ by $-c$ if needed). Let $t = \min \{ a_i / c_i : c_i > 0 \}$. Then $x = \sum_i (a_i - t c_i) v_i$ with nonnegative coefficients and one more coefficient equal to $0$. Repeating, $x$ is a nonnegative combination of linearly independent $v_i$. So $K$ is the union of the cones $\langle v_i : i \in I \rangle$ over the subsets $I$ with $\{ v_i \}_{i \in I}$ linearly independent. Each of these is the image of the closed orthant $\mathbb{R}_{\geq 0}^I$ under an injective linear map, which is a homeomorphism onto its image, a closed subspace, so each is closed, and a finite union of closed sets is closed.

Part 2. Let $F$ be a face and $x = \sum_i a_i v_i \in F$ with $a_i \geq 0$. For each $i$ with $a_i > 0$, $x = a_i v_i + \sum_{j \neq i} a_j v_j$ with both terms in $K$, so $a_i v_i \in F$ and $v_i \in F$. So $F$ is spanned by the $v_i$ it contains, and there are at most $2^m$ faces. If $F = \mathbb{R}_{\geq 0} x$ is an extremal ray, the $v_i$ in $F$ are nonnegative multiples of $x$, not all $0$, so $F = \mathbb{R}_{\geq 0} v_i$ for one of them.

Part 3. This is the theorem of Farkas, Minkowski and Weyl. It is proved by Fourier-Motzkin elimination, or by induction on $m$, in Fulton, *Introduction to toric varieties*, Section 1.2 (Ful93), where it appears as property (1) of convex polyhedral cones. The second statement follows from the first and part 2 of Proposition P7.4.3: if $K = \langle v_i \rangle$, then $K^\vee = \langle \varphi_1, \dots, \varphi_s \rangle$ for some $\varphi_j$, and $K = (K^\vee)^\vee = \bigcap_j \{ \varphi_j \geq 0 \}$; conversely, $\bigcap_j \{ \varphi_j \geq 0 \} = \langle \varphi_1, \dots, \varphi_s \rangle^\vee$ is the dual of a polyhedral cone, so it is polyhedral by the first statement.

*Proposition P7.4.5.* Part 1. By part 3 of Proposition P7.4.3, $h > 0$ on the compact set $S$ of unit vectors of $K$, so $h \geq c |x|$ on $K$ for some $c > 0$. So $\Sigma_h$ is closed and bounded, hence compact, and it is convex as the intersection of $K$ with an affine hyperplane. A nonzero $x \in K$ has $h(x) > 0$, and $t x \in \Sigma_h$ exactly for $t = 1 / h(x)$.

Part 2. Let $x \in \Sigma_h$. Suppose $x$ is extreme in $\Sigma_h$ and $u + v = t x$ with $u, v \in K$ and $t \geq 0$. If $u = 0$ or $v = 0$, both are in $\mathbb{R}_{\geq 0} x$. Otherwise $h(u), h(v) > 0$, $t = h(u) + h(v) > 0$, and $x = (h(u)/t)(u / h(u)) + (h(v)/t)(v / h(v))$ is a convex combination of two points of $\Sigma_h$ with positive weights. A point $x$ that is a convex combination $s a + (1 - s) b$ of distinct points $a, b$ of a convex set, with $0 < s < 1$, is the midpoint of the distinct points $x - \epsilon(a - b)$ and $x + \epsilon(a - b)$, which lie on the segment $[a, b]$ for small $\epsilon > 0$. Since $x$ is extreme, $u / h(u) = v / h(v)$, and then both equal $x$. So $u, v \in \mathbb{R}_{\geq 0} x$. Conversely, if $x = (a + b)/2$ with $a \neq b$ in $\Sigma_h$, then $a + b = 2x$ with $a, b \in K$ and $a \notin \mathbb{R}_{\geq 0} x$, since $h(a) = h(x) = 1$ and $a \neq x$; so the ray is not a face.

Part 3. Induction on the dimension $d$ of the affine span $A$ of a nonempty compact convex set $T$; the claim is that $T$ is the convex hull of its extreme points. For $d = 0$, $T$ is a point. Let $d > 0$ and $x \in T$. If $x$ is in the boundary of $T$ relative to $A$, choose points $v_n \in A \setminus T$ converging to $x$. Lemma P7.4.2 gives linear functionals $\psi_n$, nonconstant on $A$ and normalized to have norm $1$ on the direction space of $A$, with $\psi_n(v_n) < \psi_n(t)$ for $t \in T$. A subsequence converges to $\psi$, nonconstant on $A$, with $\psi(x) \leq \psi(t)$ for every $t \in T$. Then $T' = T \cap \{ \psi = \psi(x) \}$ is a compact convex set with affine span of dimension less than $d$, containing $x$, and an extreme point of $T'$ is extreme in $T$: if it is the midpoint of $a, b \in T$, then $\psi(a), \psi(b) \geq \psi(x)$ with average $\psi(x)$, so $a, b \in T'$. By induction $x$ is a convex combination of extreme points of $T$. If $x$ is in the relative interior, a line through $x$ in $A$ meets $T$ in a segment $[a, b]$ with $a$, $b$ in the relative boundary, by compactness, and $x$ is a convex combination of $a$ and $b$, each of which is a convex combination of extreme points. Applying this to $T = \Sigma_h$ and using parts 1 and 2, every nonzero $x \in K$ is a positive multiple of a convex combination of points spanning extremal rays.

### Exercises

1. (A) Let $K = \langle (1, 0, 0), (1, 1, 0), (1, 0, 1), (1, 1, 1) \rangle \subseteq \mathbb{R}^3$. Find its extremal rays, its faces and generators of $K^\vee$, and check part 3 of Proposition P7.4.4 directly.
2. (A) Show that the intersection of two faces of a convex cone is a face, that a face of a face is a face, and that the extremal rays of a polyhedral salient cone $K$ span $K$.
3. (B) Let $K$ be a closed convex cone and $F$ a face of $K$. Show that $F$ is closed when $K$ is polyhedral, and give a closed convex cone in $\mathbb{R}^3$ with a face that is not cut out by any $\varphi \in K^\vee$.
4. (B) Let $T \colon V \to W$ be linear and $K \subseteq V$ a closed convex cone with $K \cap \ker T = \{0\}$. Show that $T(K)$ is closed and that $T(K)^\vee = (T^*)^{-1}(K^\vee)$. Give an example with $K \cap \ker T \neq \{0\}$ and $T(K)$ not closed.
5. (B) In Example P7.4.7, show that $K$ is not polyhedral for $r \geq 2$ by exhibiting infinitely many extremal rays, and that for $r = 1$ it is the simplicial cone spanned by $(1, 1)$ and $(1, -1)$.
6. (C) Let $K \subseteq V$ be a polyhedral salient full-dimensional cone. Show that $\rho \mapsto K \cap \rho^\perp$ is a bijection from the extremal rays $\rho$ of $K^\vee$ to the faces of $K$ that span a hyperplane of $V$, and that every face of $K$ is cut out by some $\varphi \in K^\vee$.

### Lean

The project library works with classes as functions on curves and has `MinimalModel.IsRatPolyCone` for rational polyhedral cones in $N^1(X)$ and `MinimalModel.interiorN1` for the interior relative to $N^1(X)$. Mathlib has convex cones and their duals in `ConvexCone` and `PointedCone`, and the separation theorem in a topological vector space, which contains Lemma P7.4.2. The handbook adds no `MinimalModel` node here.

### Notes and history

The duality of cones and the theorem of Farkas, Minkowski and Weyl are classical, and Fulton's Section 1.2 (Ful93) proves the facts used here in the language of toric geometry. Minkowski's theorem is the finite-dimensional case of the Krein-Milman theorem. Lazarsfeld, Section 1.4 (Laz04), and Debarre, Chapter 1 (Deb01), use these facts without proof. The distinction between a cone and its closure, which is invisible for polyhedral cones by part 1 of Proposition P7.4.4, is the reason the minimal model program works with $\overline{NE}(X)$ rather than $NE(X)$.
