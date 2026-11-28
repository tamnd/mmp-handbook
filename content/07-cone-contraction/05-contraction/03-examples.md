---
title: Contractions of Fano threefolds with Picard number two
nodes: [MMQ2K4RSHT]
sources: [KM98, Mat02, Mor82, MM81]
reads_with: [KM98:1.32, Mor82:3, Mat02:ch8]
requires: [P3.6, P3.8, P7.3, P7.4, 4.1, 6.3, 7.4]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Contractions of Fano threefolds with Picard number two

### Statement

A smooth Fano variety $X$ with $\rho(X) = 2$ has a cone of curves with exactly two extremal rays, both $K_X$-negative, and Theorem 7.5.2 gives two contractions. This section works out two threefolds in full. The first has a divisorial contraction onto a curve and a fibre type contraction onto $\mathbb{P}^1$. The second is a conic bundle over $\mathbb{P}^2$ whose other contraction is a $\mathbb{P}^1$-bundle over $\mathbb{P}^2$. Volume 6 met both varieties through Mori's classification (Examples 6.3.20 and 6.4.21); here the contractions come from the contraction theorem, and their types from Section 2. All varieties are over a field $k$ of characteristic $0$.

**Proposition 7.5.17 (the blow-up of $\mathbb{P}^3$ along a line).** Let $C \subseteq \mathbb{P}^3$ be a line, $\pi \colon X = \operatorname{Bl}_C \mathbb{P}^3 \to \mathbb{P}^3$ the blow-up with exceptional divisor $E$, $H = \pi^* \mathcal{O}(1)$ and $G = H - E$. Let $e$ be a fibre of $E \to C$ and $m$ the strict transform of a line meeting $C$ in one point.

1. $\operatorname{Pic}(X) = \mathbb{Z} H \oplus \mathbb{Z} E$, $\rho(X) = 2$, and $H \cdot e = 0$, $E \cdot e = -1$, $H \cdot m = 1$, $E \cdot m = 1$.
2. $\overline{NE}(X) = \langle e, m \rangle$, $\operatorname{Nef}(X) = \langle H, G \rangle$, and $-K_X = 4 H - E = 3 H + G$ is ample, with $-K_X \cdot e = 1$ and $-K_X \cdot m = 3$.
3. The contraction of $\mathbb{R}_{\ge 0} [e]$ is $\pi$. It is divisorial, with exceptional divisor $E$ mapped onto the curve $C$, and $K_X = \pi^* K_{\mathbb{P}^3} + E$.
4. The contraction of $\mathbb{R}_{\ge 0} [m]$ is the morphism $q \colon X \to \mathbb{P}^1$ defined by $|G|$, the pencil of planes through $C$. It is of fibre type onto a curve, and every fibre is a plane $P \cong \mathbb{P}^2$ in which $m$ is a line.

Lean: not yet in Lean.

**Proposition 7.5.18 (a conic bundle over the plane).** Let $X \subseteq \mathbb{P}^2_x \times \mathbb{P}^2_y$ be the divisor of bidegree $(1, 2)$
$$x_0 y_0^2 + x_1 y_1^2 + x_2 y_2^2 = 0,$$
with projections $p_1$, $p_2$, $h_i = p_i^* \mathcal{O}(1)$, a fibre $f$ of $p_2$ and a line $c$ in a singular fibre of $p_1$.

1. $X$ is a smooth threefold, $p_2 \colon X \to \mathbb{P}^2_y$ is a $\mathbb{P}^1$-bundle, $\operatorname{Pic}(X) = \mathbb{Z} h_1 \oplus \mathbb{Z} h_2$ and $\rho(X) = 2$.
2. $h_1 \cdot f = 1$, $h_2 \cdot f = 0$, $h_1 \cdot c = 0$, $h_2 \cdot c = 1$, $\overline{NE}(X) = \langle f, c \rangle$, and $-K_X = 2 h_1 + h_2$ is ample, with $-K_X \cdot f = 2$ and $-K_X \cdot c = 1$.
3. The contraction of $\mathbb{R}_{\ge 0} [c]$ is $p_1$, a conic bundle: the fibre over $x$ is the conic $\sum x_i y_i^2 = 0$ in $\mathbb{P}^2_y$, smooth for $x_0 x_1 x_2 \ne 0$, a pair of distinct lines on the three lines $x_0 x_1 x_2 = 0$ away from their intersection points, and a double line over the three points $[1 : 0 : 0]$, $[0 : 1 : 0]$, $[0 : 0 : 1]$.
4. The contraction of $\mathbb{R}_{\ge 0} [f]$ is $p_2$. Both contractions are of fibre type onto a surface.

Lean: not yet in Lean.

### Proof in words

Both varieties have two free divisor classes, $H$ and $G$ in the first case and $h_1$ and $h_2$ in the second, and two curves on which the intersection matrix with them is the identity. Each free class is nef and vanishes on one of the curves, so the two curves span extremal rays and the cone is the simplicial cone they span. The anticanonical class is positive on both, so the variety is Fano, and the free divisors are supporting divisors of the two rays. By the uniqueness in Theorem 7.5.2, the morphisms they define, which have connected fibres, are the contractions, and the types are read off from the fibres. The formula $K_X = \pi^* K_{\mathbb{P}^3} + E$ is both Lemma 4.1.20 and part 2 of Proposition 7.5.11.

### Examples

**Example 7.5.19 (lengths against the bounds).** In Proposition 7.5.17, the divisorial ray has length $1$ with $e = \dim E - \dim C = 1$, and the fibre type ray has length $3$ with $e = 3 - 1 = 2$; Kawamata's bounds $2e$ of Theorem 7.4.13 are $2$ and $4$. In Proposition 7.5.18, the ray of $f$ has length $2$ with $e = 1$, so Kawamata's bound $2e = 2$ is attained, and the ray of $c$ has length $1$, while a smooth conic fibre, of class $2c$, has degree $2$. The lines $c$, not the smooth fibres, are the curves of minimal degree in their ray.

**Example 7.5.20 (the relative cone of a conic bundle).** For $p_1 \colon X \to \mathbb{P}^2_x$ of Proposition 7.5.18, $\overline{NE}(X/\mathbb{P}^2_x) = \mathbb{R}_{\ge 0} [c]$, and the two lines $c_1$, $c_2$ of a reducible fibre over a point of $\{x_0 = 0\}$ have the same class, so they are numerically equivalent on $X$ although neither moves in the fibre. Over the open set $V = \{x_0 x_1 x_2 \ne 0\}$ the restriction $p_1^{-1}(V) \to V$ is a smooth conic bundle whose generic fibre is a conic over $k(V)$ without a rational point, while over the three lines the two components are exchanged by monodromy around the vertices, which is why the components are not separate rays. The relative Picard number $\rho(X) - \rho(\mathbb{P}^2) = 1$ agrees with Corollary 7.5.3.

**Example 7.5.21 (the projective bundle structure).** In Proposition 7.5.17, $X \cong \mathbb{P}(\mathcal{O} \oplus \mathcal{O} \oplus \mathcal{O}(1))$ over $\mathbb{P}^1$, with $q$ the bundle projection: the planes through $C$ are parametrized by $\mathbb{P}^1$ and each contains $C$. With $\xi$ the tautological class and $g$ the class of a fibre, $\xi = H$ and $g = G$, and $K_X = -3 \xi + q^* (K_{\mathbb{P}^1} + \det) = -3 H + (-2 + 1) G = -4 H + E$, in agreement with part 2. The curve $C' = \pi^{-1}(C) \cap P$ for a fibre $P$ is the copy of $C$ in that plane.

### Proof

*Proposition 7.5.17, part 1.* By Theorem P3.8.13, $\operatorname{Cl}(X \setminus E) = \operatorname{Cl}(\mathbb{P}^3 \setminus C) = \operatorname{Cl}(\mathbb{P}^3) = \mathbb{Z}$, generated by the restriction of $H$, since $C$ has codimension $2$, and the kernel of $\operatorname{Cl}(X) \to \operatorname{Cl}(X \setminus E)$ is generated by $E$. As $X$ is smooth, $\operatorname{Pic}(X) = \operatorname{Cl}(X)$ is generated by $H$ and $E$. Since $\pi$ maps $e$ to a point, $H \cdot e = 0$. The divisor $E$ is $\mathbb{P}(N^\vee_{C/\mathbb{P}^3})$ with $N_{C/\mathbb{P}^3} = \mathcal{O}(1)^{\oplus 2}$, and $\mathcal{O}_E(E)$ is the tautological $\mathcal{O}(-1)$, so $E \cdot e = -1$. The line $m$ maps isomorphically to a line meeting $C$ transversally in one point, so $H \cdot m = 1$ and $E \cdot m = 1$. The intersection matrix is invertible, so $H$ and $E$ are numerically independent and $\rho(X) = 2$.

*Part 2.* The class $H$ is free. The linear system of planes through $C$ has base locus $C$, and after blowing up $C$ it becomes the free system $|H - E| = |G|$, defining $q$; $G \cdot e = 1$ and $G \cdot m = 0$. So $H$ and $G$ are nef, and in the basis dual to $(H, G)$ every class $z$ is $(G \cdot z) e + (H \cdot z) m$ with nonnegative coefficients for $z \in \overline{NE}(X)$. So $\overline{NE}(X) = \langle e, m \rangle$, and by duality $\operatorname{Nef}(X) = \langle H, G \rangle$. By Lemma 4.1.20, $K_X = \pi^* K_{\mathbb{P}^3} + (2 - 1) E = -4 H + E$, so $-K_X = 3 H + G$, positive on $e$ and $m$, and ample by Theorem P7.3.13.

*Part 3.* The ray $\mathbb{R}_{\ge 0} [e]$ is $F_H$, and $H - K_X$ is ample, so $H$ is a supporting divisor as in Corollary 7.4.7. The morphism of $|H|$ is $\pi$, a contraction by Theorem P4.6.8, which contracts exactly the curves in $E$ lying in fibres of $E \to C$, the curves with class in $\mathbb{R}_{\ge 0} [e]$. By part 4 of Theorem 7.5.2 it is the contraction of the ray. It is birational with exceptional locus the divisor $E$, so it is divisorial, and $E \cdot e < 0$ as Proposition 7.5.10 requires. The discrepancy formula is that of part 2, and it agrees with part 2 of Proposition 7.5.11, where $\alpha = K_X \cdot e / E \cdot e = 1$.

*Part 4.* The fibre of $q$ over a point of $\mathbb{P}^1$ is the strict transform of a plane $P_0 \supseteq C$. Since $C$ is a Cartier divisor on $P_0$, the blow-up of $P_0$ along $C$ is an isomorphism, so the fibre is $P \cong \mathbb{P}^2$; it is connected and reduced, and $q_* \mathcal{O}_X = \mathcal{O}_{\mathbb{P}^1}$ by Theorem P4.6.15, since a finite morphism onto the normal curve $\mathbb{P}^1$ with connected reduced fibres is an isomorphism. A line $\ell \subseteq P$ not equal to $C$ meets $C$ once, so $H \cdot \ell = 1$ and $E \cdot \ell = 1$, and $[\ell] = [m]$; the curves contracted by $q$ are the curves in the fibres, with classes in $\mathbb{R}_{\ge 0} [m]$. As $G - K_X$ is ample, part 4 of Theorem 7.5.2 identifies $q$ with the contraction of the ray.

*Proposition 7.5.18, part 1.* The partial derivatives are $\partial F / \partial x_i = y_i^2$ and $\partial F / \partial y_i = 2 x_i y_i$. At a singular point all $y_i^2$ vanish, which is impossible on $\mathbb{P}^2_y$, so $X$ is smooth, of dimension $3$. The fibre of $p_2$ over $y$ is the line $\sum y_i^2 x_i = 0$ in $\mathbb{P}^2_x$, since $(y_0^2, y_1^2, y_2^2) \ne 0$. So $X = \mathbb{P}(\mathcal{Q})$, where $\mathcal{O}^{\oplus 3} \to \mathcal{Q}$ is the quotient of rank $2$ dual to the kernel of $(y_0^2, y_1^2, y_2^2) \colon \mathcal{O}^{\oplus 3} \to \mathcal{O}(2)$, and Proposition P3.6.35 gives $\operatorname{Pic}(X) = \mathbb{Z} h_1 \oplus \mathbb{Z} h_2$, with $h_1$ restricting to $\mathcal{O}(1)$ on the fibres.

*Part 2.* The fibre $f$ is a line in $\mathbb{P}^2_x \times \{y\}$, so $h_1 \cdot f = 1$ and $h_2 \cdot f = 0$. The fibre of $p_1$ over $x = [0 : 1 : 1]$ is $y_1^2 + y_2^2 = 0$, two lines through $[1 : 0 : 0]$, and a line $c$ among them has $h_1 \cdot c = 0$ and $h_2 \cdot c = 1$. Both $h_1$ and $h_2$ are free, so nef, and as in Proposition 7.5.17, $\overline{NE}(X) = \langle f, c \rangle$. By adjunction, $K_X = (K_{\mathbb{P}^2 \times \mathbb{P}^2} + X)|_X = (-3 + 1) h_1 + (-3 + 2) h_2 = -2 h_1 - h_2$, which gives the degrees, and $-K_X$ is ample by Theorem P7.3.13.

*Part 3.* The ray $\mathbb{R}_{\ge 0} [c]$ is $F_{h_1}$ and $h_1 - K_X$ is ample. The fibres of $p_1$ are plane conics, connected, so the Stein factorization of $p_1$ is finite and bijective onto the normal surface $\mathbb{P}^2_x$, hence birational, hence an isomorphism by Theorem P4.6.8, and $p_1$ is a contraction. It contracts exactly the curves in its fibres, so by part 4 of Theorem 7.5.2 it is the contraction of the ray. The conic $\sum x_i y_i^2$ is diagonal with rank equal to the number of nonzero $x_i$: rank $3$ gives a smooth conic, rank $2$ two distinct lines, and rank $1$ a double line.

*Part 4.* The ray $\mathbb{R}_{\ge 0} [f]$ is $F_{h_2}$, $h_2 - K_X$ is ample, and $p_2$ is a $\mathbb{P}^1$-bundle, a contraction with exactly the fibres as contracted curves. Both bases have dimension $2 < 3$.

### Exercises

1. (A) In Proposition 7.5.17, compute the class in $N_1(X)$ of the strict transform of a conic meeting $C$ in two points, and of a line in $E$ that is a section of $E \to C$.
2. (A) In Proposition 7.5.18, compute $(-K_X)^3$ using $h_1^3 = 0$, $h_1^2 h_2 = 2$, $h_1 h_2^2 = 1$ and $h_2^3 = 0$ on $X$, and check the last four numbers.
3. (B) Let $X = \operatorname{Bl}_p \mathbb{P}^3$. Find the two extremal rays, their lengths and their contractions, and show that one is divisorial onto a point and the other of fibre type onto $\mathbb{P}^2$.
4. (B) Let $X \subseteq \mathbb{P}^2_x \times \mathbb{P}^2_y$ be a smooth divisor of bidegree $(1, 1)$. Show that both projections are $\mathbb{P}^1$-bundles and that $-K_X \cdot f = 2$ for the fibres of either.
5. (B) For the conic bundle $p_1$ of Proposition 7.5.18, show that the discriminant curve of a general divisor of bidegree $(1, 2)$ is a smooth cubic, and that the special equation of Proposition 7.5.18 is a degeneration with discriminant three lines.
6. (C) Show that a smooth Fano threefold $X$ with $\rho(X) = 2$ and a divisorial contraction $\pi \colon X \to \mathbb{P}^3$ onto a line, as in Proposition 7.5.17, is the blow-up of $\mathbb{P}^3$ along that line, using Theorem 6.3.9 for the structure of $\pi$ near $E$.

### Lean

The varieties and contractions of this section are not yet in Lean. The general statement used is `MinimalModel.ContractionTheorem`, which exists without proof.

### Notes and history

Smooth Fano threefolds with $\rho = 2$ were classified by Mori and Mukai (MM81) through the two contractions given by Mori's theorem (Mor82); there are $36$ families, and the two varieties of this section are among them. Conic bundles over surfaces are the fibre type contractions of smooth threefolds onto surfaces (Theorem 6.3.9), and the discriminant curve controls their rationality questions.
