---
title: The ample and nef cones over a base
nodes: []
sources: [KM98, Laz04, Deb01, Kle66]
reads_with: [KM98:ch1, Laz04:1.4, Deb01:ch1]
requires: [P5.5, P5.12, 1.1, 1.2]
level: background
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The ample and nef cones over a base

### Statement

In this volume $k$ is an algebraically closed field of characteristic $0$. In this chapter $\pi \colon X \to Z$ is a projective morphism from a normal quasi-projective variety $X$ to a quasi-projective variety $Z$. When $Z = \operatorname{Spec} k$, the variety $X$ is projective and the subscript $Z$ is dropped from the notation.

Chapter 2 sets up the numerical spaces over $Z$, and this chapter uses the following facts from it. A curve *over $Z$* is an integral curve $C \subseteq X$ with $\pi(C)$ a point. Two $\mathbb{R}$-Cartier divisors $D, D'$ (Definition 1.1.6) are *numerically equivalent over $Z$*, written $D \equiv_Z D'$, if $D \cdot C = D' \cdot C$ for every curve $C$ over $Z$. The space $N^1(X/Z)$ is the real vector space of $\mathbb{R}$-Cartier divisors modulo $\equiv_Z$. The space $N_1(X/Z)$ is the real vector space of finite sums $\sum a_i C_i$ of curves over $Z$, modulo the sums that are zero against every Cartier divisor. Both spaces are finite dimensional, the intersection pairing $N^1(X/Z) \times N_1(X/Z) \to \mathbb{R}$ is perfect, and $N^1(X/Z)$ is spanned by the classes of Cartier divisors. Give both spaces the Euclidean topology. The *rational points* of $N^1(X/Z)$ are the classes $\frac1m [D]$ with $D$ Cartier and $m \ge 1$. They form a $\mathbb{Q}$-vector space that contains a basis of $N^1(X/Z)$, so they are dense. A Cartier divisor $D$ is *$\pi$-ample*, or ample over $Z$, if its restriction to $\pi^{-1}(V)$ is ample for every affine open $V \subseteq Z$. The relative Kleiman criterion of Chapter 2 (KM98, Theorem 1.44) says:

> a Cartier divisor $D$ is ample over $Z$ if and only if $D \cdot z > 0$ for every nonzero $z \in \overline{NE}(X/Z)$,

where $\overline{NE}(X/Z)$ is defined below. In particular ampleness over $Z$ depends only on the class of $D$ in $N^1(X/Z)$. For $Z = \operatorname{Spec} k$ this is Theorem 1.1.9.

**Definition 1.3.1 (the cones over a base).** In the setting above:

1. The *cone of curves* $NE(X/Z) \subseteq N_1(X/Z)$ is the set of sums $\sum a_i [C_i]$ with $a_i \ge 0$ and $C_i$ curves over $Z$. Its closure is $\overline{NE}(X/Z)$.
2. The *nef cone* is $\operatorname{Nef}(X/Z) = \{ x \in N^1(X/Z) : x \cdot C \ge 0 \text{ for every curve } C \text{ over } Z \}$. An $\mathbb{R}$-Cartier divisor is *nef over $Z$* if its class is in $\operatorname{Nef}(X/Z)$.
3. The *ample cone* $\operatorname{Amp}(X/Z)$ is the set of sums $\sum r_i [A_i]$ with $r_i > 0$ and $A_i$ Cartier divisors ample over $Z$. An $\mathbb{R}$-Cartier divisor is *ample over $Z$* if its class is in $\operatorname{Amp}(X/Z)$.

For a convex cone $K$ in a real vector space $W$ and a perfect pairing $V \times W \to \mathbb{R}$ of finite dimensional spaces, the *dual cone* is $K^\vee = \{ x \in V : x \cdot z \ge 0 \text{ for all } z \in K \}$, and similarly for a cone in $V$. Since $x \cdot (-)$ is linear and continuous, $\operatorname{Nef}(X/Z) = NE(X/Z)^\vee = \overline{NE}(X/Z)^\vee$.

**Lemma 1.3.2 (dual cones).** Let $V \times W \to \mathbb{R}$ be a perfect pairing of finite dimensional real vector spaces and $K \subseteq W$ a closed convex cone.

1. $(K^\vee)^\vee = K$.
2. The interior of $K^\vee$ is the set $\{ x \in V : x \cdot z > 0 \text{ for all } z \in K \setminus \{0\} \}$.
3. If $K^\vee$ has an interior point, then $K \cap (-K) = \{0\}$.

Lean: not yet in Lean.

**Lemma 1.3.3 (convex sets with an interior point).** Let $C$ be a convex subset of a finite dimensional real vector space with nonempty interior $C^\circ$.

1. If $c \in C^\circ$, $y \in \overline{C}$ and $0 \le \lambda < 1$, then $\lambda y + (1 - \lambda) c \in C^\circ$.
2. $\overline{C} = \overline{C^\circ}$, and the interior of $\overline{C}$ is $C^\circ$.

Lean: not yet in Lean.

**Theorem 1.3.4 (the ample and nef cones over a base).** Let $\pi \colon X \to Z$ be as above.

1. $\operatorname{Amp}(X/Z) = \{ x \in N^1(X/Z) : x \cdot z > 0 \text{ for all } z \in \overline{NE}(X/Z) \setminus \{0\} \}$. This set is open and nonempty, and it is the interior of $\operatorname{Nef}(X/Z)$.
2. $\operatorname{Nef}(X/Z)$ is the closure of $\operatorname{Amp}(X/Z)$.
3. $\overline{NE}(X/Z) = \operatorname{Nef}(X/Z)^\vee$, so $\operatorname{Nef}(X/Z)$ and $\overline{NE}(X/Z)$ are dual cones, and $\overline{NE}(X/Z)$ contains no line.
4. A rational point $x$ of $N^1(X/Z)$ lies in $\operatorname{Amp}(X/Z)$ if and only if $mx$ is the class of a Cartier divisor ample over $Z$ for some $m \ge 1$.

Lean: not yet in Lean.

**Corollary 1.3.5 (nef plus ample).** Let $x \in \operatorname{Nef}(X/Z)$ and $h \in \operatorname{Amp}(X/Z)$. Then $x + h \in \operatorname{Amp}(X/Z)$. A class $x$ is nef over $Z$ if and only if $x + \varepsilon h$ is ample over $Z$ for every $\varepsilon > 0$.

Lean: not yet in Lean.

### Proof in words

Everything is linear algebra once the relative Kleiman criterion is known. The nef cone is by definition the dual of the closed cone of curves. A closed convex cone is the dual of its dual by the separation theorem, and the interior of a dual cone is the set of forms that are strictly positive on the nonzero points of the cone: a form that vanishes at a nonzero point of the cone can be pushed out of the dual cone by a small perturbation, and a strictly positive form stays strictly positive nearby because the slice of the cone where a strictly positive form equals $1$ is compact. The Kleiman criterion says that the strictly positive integral classes are exactly the ample classes over $Z$, and a real strictly positive class is a positive combination of rational ones, because the strictly positive classes form an open set.

The difficulty is the Kleiman criterion itself, which Chapter 2 proves. Positivity on the curves alone is not enough: Example 1.3.9 gives a class on $E \times E$ that is positive on every curve and is not ample, because the cone of curves of $E \times E$ is not closed.

### Examples

**Example 1.3.6 (the plane blown up at a point).** Let $X = \operatorname{Bl}_p \mathbb{P}^2$, with $\ell$ the pullback of a line and $E$ the exceptional curve, so that $\ell^2 = 1$, $E^2 = -1$ and $\ell \cdot E = 0$. By Example P5.12.7,
$$\overline{NE}(X) = \mathbb{R}_{\ge 0}[E] + \mathbb{R}_{\ge 0}[\ell - E], \qquad \operatorname{Nef}(X) = \mathbb{R}_{\ge 0}\ell + \mathbb{R}_{\ge 0}(\ell - E).$$
The duality of Theorem 1.3.4 is visible: $x = a\ell - bE$ has $x \cdot E = b$ and $x \cdot (\ell - E) = a - b$, so $x$ is nef if and only if $0 \le b \le a$, and ample if and only if $0 < b < a$. Conversely $y = \alpha(\ell - E) + \beta E$ has $y \cdot \ell = \alpha$ and $y \cdot (\ell - E) = \beta$, so $y \in \operatorname{Nef}(X)^\vee$ if and only if $\alpha, \beta \ge 0$. The two boundary rays of the nef cone are $\ell$, which is zero on $E$ and defines the contraction $X \to \mathbb{P}^2$, and $\ell - E$, which is zero on the fibre class $\ell - E$ and defines the ruling $X \to \mathbb{P}^1$ by the lines through $p$.

Now let $Z = \mathbb{P}^2$ and let $\pi \colon X \to \mathbb{P}^2$ be the blow-up. The only curve over $Z$ is $E$, since $\pi$ is an isomorphism off $E$. So $N_1(X/Z) = \mathbb{R}[E]$, which is nonzero because $E \cdot E = -1 \ne 0$, and $N^1(X/Z)$ is the line $N^1(X)/E^\perp$, identified with $\mathbb{R}$ by $x \mapsto x \cdot E$. Under this identification $\ell \mapsto 0$, $E \mapsto -1$ and $\ell - E \mapsto 1$. Then $\overline{NE}(X/Z) = \mathbb{R}_{\ge 0}[E]$, $\operatorname{Nef}(X/Z) = \mathbb{R}_{\ge 0}$ and $\operatorname{Amp}(X/Z) = \mathbb{R}_{> 0}$. In particular $-E$ is ample over $\mathbb{P}^2$, as it should be: $\mathcal{O}_X(-E)$ is the relative $\mathcal{O}(1)$ of the blow-up.

**Example 1.3.7 (the quadric surface).** Let $X = \mathbb{P}^1 \times \mathbb{P}^1$ with the fibre classes $F_1$ and $F_2$, so $(aF_1 + bF_2) \cdot (cF_1 + dF_2) = ad + bc$ (Example P5.5.9). By Example P5.12.8, $\overline{NE}(X) = \operatorname{Nef}(X) = \mathbb{R}_{\ge 0} F_1 + \mathbb{R}_{\ge 0} F_2$, and $aF_1 + bF_2$ is ample if and only if $a > 0$ and $b > 0$. The cone is self-dual: $F_1 \cdot F_1 = 0$, $F_1 \cdot F_2 = 1$, so the dual basis of $F_1, F_2$ is $F_2, F_1$, and the dual of the positive quadrant is again the positive quadrant.

Let $Z = \mathbb{P}^1$ and let $\pi$ be the projection whose fibres have class $F_1$. Every curve over $Z$ lies in a fibre, and the fibres are integral, so every curve over $Z$ is a fibre and $N_1(X/Z) = \mathbb{R}F_1$. The space $N^1(X/Z)$ is identified with $\mathbb{R}$ by $x \mapsto x \cdot F_1$, under which $aF_1 + bF_2 \mapsto b$. So $\operatorname{Nef}(X/Z) = \{ b \ge 0 \}$ and $\operatorname{Amp}(X/Z) = \{ b > 0 \}$: the class $F_2$, a section of $\pi$, is ample over $Z$ without being ample on $X$.

**Example 1.3.8 (the Hirzebruch surfaces).** Let $n \ge 1$ and $X = \mathbb{F}_n$, with fibre $F$, negative section $C_-$ and positive section $C_+ \sim C_- + nF$, so that $F^2 = 0$, $C_- \cdot F = 1$, $C_-^2 = -n$ and $C_+^2 = -n + 2n = n$. By Example P5.12.8,
$$\overline{NE}(\mathbb{F}_n) = \mathbb{R}_{\ge 0}[C_-] + \mathbb{R}_{\ge 0}[F], \qquad \operatorname{Nef}(\mathbb{F}_n) = \mathbb{R}_{\ge 0}[F] + \mathbb{R}_{\ge 0}[C_+].$$
In the basis $C_-, F$ the Gram matrix is $\left(\begin{smallmatrix} -n & 1 \\ 1 & 0 \end{smallmatrix}\right)$, and the class $x = aC_- + bF$ has $x \cdot C_- = b - na$ and $x \cdot F = a$. So $x$ is nef if and only if $b \ge na \ge 0$, and ample if and only if $b > na > 0$. The boundary ray $F$ vanishes on $F$ and gives the ruling $\mathbb{F}_n \to \mathbb{P}^1$. The boundary ray $C_+$ vanishes on $C_-$: for $n = 1$ it gives the contraction $\mathbb{F}_1 \to \mathbb{P}^2$ of Example 1.3.6, and for $n \ge 2$ it gives the contraction of $C_-$ to the vertex of the cone over the rational normal curve of degree $n$. The anticanonical class $-K = 2C_- + (n + 2)F$ has $a = 2$ and $b = n + 2$, so it is ample if and only if $n + 2 > 2n$, that is $n = 1$, nef if and only if $n \le 2$, and not nef for $n \ge 3$, where $-K \cdot C_- = 2 - n < 0$.

Over $Z = \mathbb{P}^1$, with $\pi$ the ruling, every curve over $Z$ is a fibre, $N_1(X/Z) = \mathbb{R}[F]$, and $N^1(X/Z) \cong \mathbb{R}$ by $x \mapsto x \cdot F = a$. So $\operatorname{Nef}(X/Z) = \{ a \ge 0 \}$, and the section $C_-$, which is not nef on $X$, is ample over $\mathbb{P}^1$.

**Example 1.3.9 (positive on every curve, not ample).** Let $E$ be an elliptic curve, $S = E \times E$ and $H$ an ample divisor. By Example P5.12.9, $\overline{NE}(S) = \operatorname{Nef}(S) = \{ x : x^2 \ge 0, \ x \cdot H \ge 0 \}$ and $\rho(S) \ge 3$. By Lemma P5.12.3, $H^\perp$ is negative definite of dimension $\rho - 1 \ge 2$. Scale $H$ so that $H^2 = 1$ in $N^1(S)$. A nonzero boundary point is $x = aH + x_0$ with $x_0 \in H^\perp$ and $a = \sqrt{-x_0^2} > 0$, so the boundary rays are in bijection with the rays of $H^\perp$, a space of dimension at least $2$. There are uncountably many of them, while the classes of curves lie in the countable group $\operatorname{Num}(S)$. Choose a boundary ray $R$ that contains no class of a curve, and $0 \neq x \in R$.

Let $C$ be a curve and $y = [C]$, so $y^2 \ge 0$ and $y \cdot H > 0$. Then $x \cdot y \ge 0$ because $x$ is nef. Suppose $x \cdot y = 0$ and that $x, y$ are linearly independent. On their span $W$ the form is $(\alpha x + \beta y)^2 = \beta^2 y^2 \ge 0$, so $W \cap H^\perp = \{0\}$, and $\dim W + \dim H^\perp = 2 + \rho - 1 > \rho$, which is impossible. So $y = \lambda x$ with $\lambda > 0$, and $[C] \in R$, against the choice of $R$. Hence $x \cdot C > 0$ for every curve $C$. But $x$ is not ample: a class $\sum r_i [A_i]$ with $r_i > 0$ and $A_i$ ample has square $\sum r_i r_j A_i \cdot A_j > 0$, since a multiple of $A_i$ is linearly equivalent to an effective curve and $A_j$ is positive on it by Theorem P5.12.5, while $x^2 = 0$. Here the hypothesis of Theorem 1.3.4 that is dropped is the closure: $x$ is positive on $NE(S) \setminus \{0\}$, but it vanishes on the nonzero point $x$ of $\overline{NE}(S)$.

### Proof

*Lemma 1.3.2.* (1) By definition $K \subseteq (K^\vee)^\vee$. Let $y \in W \setminus K$. Fix a Euclidean inner product $\langle \, , \rangle$ on $W$, and let $p$ be the point of the closed convex set $K$ nearest to $y$. For $z \in K$ and $t \ge 0$ the points $p + tz$ and $tp$ lie in $K$, and the minimality of $|p - y|^2$ at $t = 1$ for $tp$ and at $t = 0$ for $p + tz$ gives $\langle p - y, p \rangle = 0$ and $\langle p - y, z \rangle \ge 0$. Then $\langle p - y, y \rangle = \langle p - y, p \rangle - |p - y|^2 < 0$. Since the pairing is perfect, there is $x \in V$ with $x \cdot w = \langle p - y, w \rangle$ for all $w \in W$. This $x$ lies in $K^\vee$ and $x \cdot y < 0$, so $y \notin (K^\vee)^\vee$.

(2) Let $A$ be the set of the statement. Let $x$ be an interior point of $K^\vee$ and $z \in K \setminus \{0\}$. Since the pairing is perfect there is $v \in V$ with $v \cdot z > 0$. If $x \cdot z = 0$, then $x - \varepsilon v \in K^\vee$ for small $\varepsilon > 0$, and $(x - \varepsilon v) \cdot z < 0$, a contradiction. So $x \cdot z > 0$, and the interior of $K^\vee$ lies in $A$. Conversely, if $K = \{0\}$, then $A = V = K^\vee$. Otherwise suppose $A \ne \emptyset$ and fix $x_0 \in A$ and a norm on $W$. The slice $\Sigma = \{ z \in K : x_0 \cdot z = 1 \}$ is closed. It is bounded: otherwise there are $z_j \in \Sigma$ with $|z_j| \to \infty$, a subsequence of $z_j / |z_j|$ converges to some $z \in K$ with $|z| = 1$, and $x_0 \cdot z = \lim 1/|z_j| = 0$, against $x_0 \in A$. So $\Sigma$ is compact. Every $z \in K \setminus \{0\}$ is a positive multiple of a point of $\Sigma$, so $A = \{ x : \min_{z \in \Sigma} x \cdot z > 0 \}$. The function $x \mapsto \min_\Sigma x \cdot z$ is continuous, so $A$ is open. Since $A \subseteq K^\vee$, $A$ lies in the interior of $K^\vee$.

(3) Let $x$ be an interior point of $K^\vee$. If $z$ and $-z$ both lie in $K$ and $z \ne 0$, then (2) gives $x \cdot z > 0$ and $-x \cdot z > 0$, which is absurd. $\square$

*Lemma 1.3.3.* (1) There is $r > 0$ with the ball $B(c, r) \subseteq C$. Choose $y_j \in C$ with $y_j \to y$. By convexity $\lambda y_j + (1 - \lambda) B(c, r) \subseteq C$, and this is the ball of radius $(1 - \lambda) r$ about $\lambda y_j + (1 - \lambda) c$. For $j$ large, $|\lambda y_j - \lambda y| < (1 - \lambda) r / 2$, so the ball of radius $(1 - \lambda) r / 2$ about $x = \lambda y + (1 - \lambda) c$ lies in $C$, and $x \in C^\circ$.

(2) Fix $c \in C^\circ$. For $y \in \overline{C}$, part (1) puts $\lambda y + (1 - \lambda) c$ in $C^\circ$ for $\lambda < 1$, and letting $\lambda \to 1$ gives $y \in \overline{C^\circ}$. The other inclusion is clear. Now let $x$ be an interior point of $\overline{C}$. For small $\varepsilon > 0$ the point $y = x + \varepsilon (x - c)$ lies in $\overline{C}$, and $x = \frac{1}{1 + \varepsilon} y + \frac{\varepsilon}{1 + \varepsilon} c$, which lies in $C^\circ$ by part (1). So the interior of $\overline{C}$ is in $C^\circ$, and the other inclusion is clear. $\square$

*Theorem 1.3.4.* Put $K = \overline{NE}(X/Z)$, a closed convex cone, so that $\operatorname{Nef}(X/Z) = K^\vee$. Let $A = \{ x : x \cdot z > 0 \text{ for } z \in K \setminus \{0\} \}$. By Lemma 1.3.2, $A$ is the interior of $\operatorname{Nef}(X/Z)$, and it is open.

First, $\operatorname{Amp}(X/Z) \subseteq A$. Each Cartier divisor ample over $Z$ has its class in $A$ by the relative Kleiman criterion, and $A$ is closed under sums and under multiplication by positive reals, so it contains every positive combination of such classes. Since $\pi$ is projective, a Cartier divisor ample over $Z$ exists, so $A \ne \emptyset$.

Next, $A \subseteq \operatorname{Amp}(X/Z)$. A rational point $q \in A$ is $\frac1m [D]$ with $D$ Cartier, and $D$ is positive on $K \setminus \{0\}$, so $D$ is ample over $Z$ by the relative Kleiman criterion, and $q \in \operatorname{Amp}(X/Z)$. Let $x \in A$ be arbitrary and $\rho = \dim N^1(X/Z)$. Choose a basis $e_1, \dots, e_\rho$ and $\varepsilon > 0$ so small that the points $v_0 = x - \varepsilon (e_1 + \dots + e_\rho)$ and $v_i = x + \varepsilon e_i$ lie in the open set $A$. They are affinely independent, and $x = \frac{1}{\rho + 1}(v_0 + v_1 + \dots + v_\rho)$ is in the interior of their simplex. The barycentric coordinates of $x$ with respect to $\rho + 1$ points depend continuously on the points, so if each $v_i$ is replaced by a rational point $q_i \in A$ close enough to it, the coordinates of $x$ stay positive. Then $x$ is a positive combination of the $q_i$, which lie in $\operatorname{Amp}(X/Z)$, so $x \in \operatorname{Amp}(X/Z)$. This proves (1).

(2) $\operatorname{Nef}(X/Z)$ is closed and convex with nonempty interior $\operatorname{Amp}(X/Z)$, so it is the closure of its interior by Lemma 1.3.3.

(3) The first statement is Lemma 1.3.2(1) for $K$, and the second is Lemma 1.3.2(3), since $\operatorname{Nef}(X/Z) = K^\vee$ has an interior point.

(4) If $mx = [D]$ with $D$ ample over $Z$, then $x \in \operatorname{Amp}(X/Z)$ by definition. Conversely, if $x = \frac1m [D]$ is in $\operatorname{Amp}(X/Z) = A$, then $D$ is positive on $K \setminus \{0\}$ and is ample over $Z$ by the relative Kleiman criterion. $\square$

*Corollary 1.3.5.* For $z \in \overline{NE}(X/Z) \setminus \{0\}$, $x \cdot z \ge 0$ and $h \cdot z > 0$ by Theorem 1.3.4(1), so $(x + h) \cdot z > 0$ and $x + h \in \operatorname{Amp}(X/Z)$. Since $\varepsilon h \in \operatorname{Amp}(X/Z)$ for $\varepsilon > 0$, a nef class has $x + \varepsilon h$ ample. Conversely, if $x + \varepsilon h$ is ample for every $\varepsilon > 0$, then $x = \lim_{\varepsilon \to 0}(x + \varepsilon h)$ lies in the closed set $\operatorname{Nef}(X/Z)$. $\square$

### Exercises

1. (A) On $\operatorname{Bl}_p \mathbb{P}^2$, decide which of $\ell - E$, $2\ell - E$, $3\ell - 2E$, $3\ell - 4E$ are nef and which are ample, and for each nef class that is not ample name a curve on which it vanishes.
2. (A) For $\pi \colon \mathbb{F}_n \to \mathbb{P}^1$, show that $C_-$ and $C_+$ have the same image in $N^1(\mathbb{F}_n/\mathbb{P}^1)$, and that both are ample over $\mathbb{P}^1$.
3. (B) Let $K \subseteq W$ be the cone spanned by finitely many vectors $z_1, \dots, z_r$ that span $W$. Show that $K$ is closed, that $K^\vee = \{ x : x \cdot z_i \ge 0 \text{ for all } i \}$, and that the interior of $K^\vee$ is $\{ x : x \cdot z_i > 0 \text{ for all } i \}$. Deduce the ample cones of Examples 1.3.6 to 1.3.8 again.
4. (B) Let $X$ be projective and $\pi \colon X \to Z$ a morphism to a quasi-projective variety. Show that the natural surjection $N^1(X) \to N^1(X/Z)$ maps $\operatorname{Nef}(X)$ into $\operatorname{Nef}(X/Z)$ and $\operatorname{Amp}(X)$ into $\operatorname{Amp}(X/Z)$. For the blow-up $\operatorname{Bl}_p \mathbb{P}^2 \to \mathbb{P}^2$, show that the image of $\operatorname{Nef}(X)$ is all of $\operatorname{Nef}(X/Z)$.
5. (B) Show that the closed convex cone $\overline{NE}(X/Z)$ is spanned by its extremal rays when it contains no line, and list the extremal rays of $\overline{NE}(X)$ for $X = \operatorname{Bl}_p \mathbb{P}^2$, $\mathbb{P}^1 \times \mathbb{P}^1$ and $\mathbb{F}_n$.
6. (C) Let $X \xrightarrow{f} Y \xrightarrow{g} Z$ be projective morphisms with $\pi = g \circ f$. Show that every curve over $Y$ is a curve over $Z$, that this gives an injection $N_1(X/Y) \to N_1(X/Z)$ and a surjection $N^1(X/Z) \to N^1(X/Y)$, and that the surjection maps $\operatorname{Amp}(X/Z)$ into $\operatorname{Amp}(X/Y)$. Check it for $\mathbb{F}_1 \to \mathbb{P}^1 \to \operatorname{Spec} k$.

### Lean

The project library has the positivity notions of this section for divisors, not yet the cones. `MinimalModel.IsRelAmple` is ampleness of a Cartier divisor over $Z$, tested on the inverse images of affine opens, and `MinimalModel.IsRAmpleOver` is an $\mathbb{R}$-divisor that is $\mathbb{R}$-linearly equivalent to a positive combination of such divisors. `MinimalModel.IsNef` is nefness against the curve classes of an intersection structure, and `MinimalModel.IsNefOver` and `MinimalModel.IsNefRel` are the versions over $Z$. `MinimalModel.KleimanCriterion` is the absolute Kleiman criterion, stated and not proved. The fidelity choice to note is that the library states ampleness up to $\mathbb{R}$-linear equivalence, while this section works with numerical classes over $Z$; the two agree by the Kleiman criterion. Mathlib has `PointedCone` and the dual cone `PointedCone.dual`, and the separation step of Lemma 1.3.2 is the geometric Hahn-Banach theorem of Mathlib, but no cone of curves.

### Notes and history

Kleiman proved the criterion and the duality of the nef cone and the closed cone of curves in his 1966 paper *Toward a numerical theory of ampleness* (Kle66), together with the finiteness of the Néron-Severi rank in the form that the theory needs. The relative versions are in KM98, Section 1.4, and the cone formalism of this section follows Laz04, Section 1.4, and Deb01, Chapter 1. Example 1.3.9 is the reason the closure cannot be dropped. An older example of the same phenomenon is Mumford's ruled surface over a curve of genus at least $2$, with a divisor that is positive on every curve and has square $0$ (Hartshorne, *Ample subvarieties of algebraic varieties*, Chapter I, Example 10.6). In the minimal model program the duality is used in the following form: a nef divisor that vanishes on exactly one extremal ray of $\overline{NE}(X/Z)$ is the input of the contraction theorem.
