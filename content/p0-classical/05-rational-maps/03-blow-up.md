---
title: The blow-up of a point in the plane
nodes: []
sources: [Har77, Sha13, Har92]
reads_with: [Har77:I.4, Sha13:ch2, Har92:lecture7]
requires: [P0.3, P0.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The blow-up of a point in the plane

### Statement

**Definition P0.5.15.** Let $(x, y)$ be coordinates on $\mathbb{A}^2$ and $(u : v)$ homogeneous coordinates on $\mathbb{P}^1$. The *blow-up of $\mathbb{A}^2$ at the origin* is the closed subset

$$ X = \operatorname{Bl}_0 \mathbb{A}^2 = \{ ((x, y), (u : v)) : xv = yu \} \subset \mathbb{A}^2 \times \mathbb{P}^1, $$

with the map $\pi : X \to \mathbb{A}^2$ induced by the first projection. The *exceptional curve* is $E = \pi^{-1}(0) = \{0\} \times \mathbb{P}^1$.

Lean: not in Lean; Mathlib has no blow-up of a scheme along a closed subscheme.

The equation $xv = yu$ says that the point $(x, y)$ lies on the line through $0$ with direction $(u : v)$. So $X$ is the set of pairs (point, line through $0$ that contains the point). Over a point $P \neq 0$ there is exactly one such line, and over $0$ every line is allowed.

**Example P0.5.16.** The open set $U_1 = X \cap \{u \neq 0\}$ has the coordinate $t = v/u$ on $\mathbb{P}^1$, and the equation becomes $y = xt$. So the map $\mathbb{A}^2 \to U_1$, $(x, t) \mapsto ((x, xt), (1 : t))$, is an isomorphism, with inverse $((x, y), (u : v)) \mapsto (x, v/u)$. In this chart $\pi(x, t) = (x, xt)$ and $E \cap U_1 = \{x = 0\}$.

**Example P0.5.17.** The open set $U_2 = X \cap \{v \neq 0\}$ has the coordinate $s = u/v$, and the map $\mathbb{A}^2 \to U_2$, $(s, y) \mapsto ((sy, y), (s : 1))$, is an isomorphism. In this chart $\pi(s, y) = (sy, y)$ and $E \cap U_2 = \{y = 0\}$. On $U_1 \cap U_2$ the coordinates satisfy $s = 1/t$ and $y = xt$.

**Definition P0.5.18.** Let $f \in k[x, y]$ be a nonconstant polynomial with $f(0) = 0$, and let $C = V(f)$. The *strict transform* of $C$ is the closure $\widetilde{C}$ of $\pi^{-1}(C \setminus \{0\})$ in $X$. Write $f = f_m + f_{m+1} + \dots + f_d$ with $f_j$ homogeneous of degree $j$ and $f_m \neq 0$. The number $m \geq 1$ is the *multiplicity* of $C$ at $0$ (Section 6.4 studies it).

Lean: not in Lean.

**Example P0.5.19.** For the line $C = V(y - ax)$ the multiplicity is $1$. In the chart $U_1$ the preimage is $V(xt - ax) = V(x) \cup V(t - a)$. The strict transform is the line $\{t = a\}$, and it meets $E$ in the single point $(0, (1 : a))$, the direction of $C$.

**Example P0.5.20.** For the pair of lines $C = V(xy)$ the multiplicity is $2$ and $f_2 = xy$. The strict transform has two components, the strict transforms of the two axes. They meet $E$ at $(1 : 0)$ and $(0 : 1)$, so they are disjoint in $X$. The blow-up separates curves through $0$ with different tangent directions.

**Theorem P0.5.21 (blow-up of the plane at a point).** Let $\pi : X \to \mathbb{A}^2$ be the blow-up at $0$.

1. $X$ is covered by two open sets $U_1$ and $U_2$, each isomorphic to $\mathbb{A}^2$. So $X$ is an irreducible surface, and every point of $X$ is nonsingular.
2. The map $\pi$ restricts to an isomorphism $X \setminus E \to \mathbb{A}^2 \setminus \{0\}$, and $E \cong \mathbb{P}^1$.
3. Let $C = V(f)$ be as in the definition above, with multiplicity $m$. In the chart $U_1$, $f(x, xt) = x^m \widetilde{f}(x, t)$ with $\widetilde{f}(x, t) = f_m(1, t) + x f_{m+1}(1, t) + \dots + x^{d - m} f_d(1, t)$, and $\widetilde{C} \cap U_1 = V(\widetilde{f})$. As sets, $\pi^{-1}(C) = E \cup \widetilde{C}$.
4. $\widetilde{C} \cap E$ is the set of points $(0, (a : b))$ with $f_m(a, b) = 0$. So it has at least $1$ and at most $m$ points, and exactly $m$ points if and only if $f_m$ is a product of $m$ pairwise non-proportional linear forms.

Lean: not in Lean.

*Proof.* Part 1. The two examples above show $U_1 \cong U_2 \cong \mathbb{A}^2$, and $U_1 \cup U_2 = X$ because $u$ and $v$ do not both vanish. Each $U_i$ is irreducible. The set $U_1 \cap U_2$ is not empty, and it is open in the irreducible space $U_1$, so it is dense in $U_1$. Thus $\overline{U_2} \supset U_1$, and $X = \overline{U_2}$ is irreducible. A point of $X$ is a point of $\mathbb{A}^2$ in one chart, and $\mathbb{A}^2$ is nonsingular (Section 6.2).

Part 2. The map $\mathbb{A}^2 \setminus \{0\} \to X$, $(x, y) \mapsto ((x, y), (x : y))$, is a morphism, because $x$ and $y$ do not both vanish. It lands in $X \setminus E$, and $\pi$ composed with it is the identity. Conversely, for $((x, y), (u : v)) \in X \setminus E$ the vector $(x, y)$ is not zero and $xv = yu$, so $(u : v) = (x : y)$. So the two maps are inverse to each other. The equality $E = \{0\} \times \mathbb{P}^1$ holds because $xv = yu$ is automatic for $x = y = 0$.

Part 3. Substitute $y = xt$: the form $f_j(x, xt) = x^j f_j(1, t)$, so $f(x, xt) = x^m \widetilde{f}(x, t)$. Thus $\pi^{-1}(C) \cap U_1 = V(x) \cup V(\widetilde{f})$, and $V(x) = E \cap U_1$. The polynomial $x$ does not divide $\widetilde{f}$, because $\widetilde{f}(0, t) = f_m(1, t)$. This polynomial is not zero: if $f_m = \sum_i a_i x^{m-i} y^i$, then $f_m(1, t) = \sum_i a_i t^i$, and some $a_i \neq 0$. Factor $\widetilde{f} = g_1 \cdots g_r$ into irreducible polynomials. Each $V(g_j)$ is irreducible, because $(g_j)$ is a prime ideal and $I(V(g_j)) = (g_j)$ by the Nullstellensatz. If $V(g_j) \subset V(x)$, then $x \in I(V(g_j)) = (g_j)$, so $g_j$ is a unit times $x$, which is false. So $V(g_j) \cap \{x \neq 0\}$ is a nonempty open subset of $V(g_j)$, and it is dense in $V(g_j)$. This shows that $V(\widetilde{f})$ is the closure in $U_1$ of $V(\widetilde{f}) \cap \{x \neq 0\} = \pi^{-1}(C \setminus \{0\}) \cap U_1 \cap \{x \neq 0\}$. The points of $\pi^{-1}(C \setminus \{0\}) \cap U_1$ with $x = 0$ have $y = xt = 0$, so there are none. Thus $V(\widetilde{f}) = \widetilde{C} \cap U_1$. The same computation in $U_2$, with $f(sy, y) = y^m (f_m(s, 1) + y f_{m+1}(s, 1) + \dots)$, gives $\pi^{-1}(C) \cap U_2 = (E \cap U_2) \cup (\widetilde{C} \cap U_2)$.

Part 4. In $U_1$ the points of $\widetilde{C} \cap E$ are $(0, t)$ with $f_m(1, t) = 0$, that is, the directions $(1 : t)$ with $f_m(1, t) = 0$. In $U_2$ they are the directions $(s : 1)$ with $f_m(s, 1) = 0$. Together these are the zeros of $f_m$ on $\mathbb{P}^1$. Over the algebraically closed field $k$ a nonzero binary form of degree $m$ is a product of $m$ linear forms $b_i x - a_i y$, and its zeros on $\mathbb{P}^1$ are the points $(a_i : b_i)$. There are between $1$ and $m$ of them, and $m$ exactly when no two factors are proportional. $\square$

**Proposition P0.5.22 (blow-up of the projective plane at a point).** Let $p = (0 : 0 : 1) \in \mathbb{P}^2$ and

$$ \operatorname{Bl}_p \mathbb{P}^2 = \{ ((x : y : z), (u : v)) : xv = yu \} \subset \mathbb{P}^2 \times \mathbb{P}^1. $$

The first projection $\pi$ is an isomorphism over $\mathbb{P}^2 \setminus \{p\}$, and over the chart $\{z \neq 0\} \cong \mathbb{A}^2$ it is the blow-up of $\mathbb{A}^2$ at $0$. The second projection $q : \operatorname{Bl}_p \mathbb{P}^2 \to \mathbb{P}^1$ has as fibre over $(u : v)$ the strict transform of the line $\{vx = uy\}$ through $p$. Each fibre is isomorphic to $\mathbb{P}^1$ and meets $E = \pi^{-1}(p)$ in exactly one point.

Lean: not in Lean.

*Proof.* The equation is bihomogeneous, so it defines a closed subset of $\mathbb{P}^2 \times \mathbb{P}^1$, a projective variety by the Segre embedding (Chapter 4). On $z = 1$ the equation is the equation of $\operatorname{Bl}_0 \mathbb{A}^2$. On the open set $(x, y) \neq (0, 0)$, which is $\mathbb{P}^2 \setminus \{p\}$, the map $(x : y : z) \mapsto ((x : y : z), (x : y))$ is an inverse of $\pi$, as in Part 2 of the theorem. The fibre $q^{-1}(u : v)$ is $\{(x : y : z) : vx = uy\} \times \{(u : v)\}$, a line $L$ through $p$. Its points other than $(p, (u : v))$ form $\pi^{-1}(L \setminus \{p\})$, and the fibre is closed and irreducible, so it is the strict transform of $L$. It meets $E = \{p\} \times \mathbb{P}^1$ only in $(p, (u : v))$. $\square$

### Proof in words

The blow-up replaces the origin by the set of lines through it. A curve through the origin approaches it along its tangent directions, so its strict transform meets the new curve $E$ at those directions. In coordinates everything is the substitution $y = xt$, which divides each homogeneous part $f_j$ by $x^j$. The factor $x^m$ is the copy of $E$ inside $\pi^{-1}(C)$, and the rest is the strict transform. The only care needed is to show that the rest has no component inside $E$, which follows from $f_m \neq 0$.

### Examples

**Example P0.5.23.** Let $\operatorname{char} k \neq 2$ and let $C = V(y^2 - x^2 - x^3)$, the nodal cubic, with $m = 2$ and $f_2 = y^2 - x^2 = (y - x)(y + x)$. In $U_1$,

$$ f(x, xt) = x^2 t^2 - x^2 - x^3 = x^2 (t^2 - 1 - x), $$

so $\widetilde{C} \cap U_1 = V(t^2 - 1 - x)$. It meets $E = \{x = 0\}$ in the two points $t = 1$ and $t = -1$, the directions of the two branches $y = \pm x$. In $U_2$, $f(sy, y) = y^2 (1 - s^2 - s^3 y)$, and the strict transform has no point with $s = 0$, so it lies in $U_1$. Thus $\widetilde{C} = \{t^2 = 1 + x\}$, which is isomorphic to $\mathbb{A}^1$ by $t \mapsto (t^2 - 1, t)$. The composite $\mathbb{A}^1 \to C$ is $t \mapsto (t^2 - 1, t(t^2 - 1))$. One blow-up resolves the node, and the two points of $C$ over $0$ are $t = \pm 1$.

**Example P0.5.24.** The hypothesis "the factors of $f_m$ are not proportional" fails for the cusp $C = V(y^2 - x^3)$: here $f_2 = y^2$, a square, and Part 4 gives one point instead of two. Indeed $f(x, xt) = x^2 (t^2 - x)$, so $\widetilde{C} \cap U_1 = \{x = t^2\}$. It meets $E = \{x = 0\}$ only at $t = 0$, and there the tangent line of $\widetilde{C}$ is $x = 0$, which is $E$ itself. So $\widetilde{C}$ is tangent to $E$. In $U_2$, $f(sy, y) = y^2 (1 - s^3 y)$ has no zero on $E$. The strict transform is nonsingular and isomorphic to $\mathbb{A}^1$, and $\pi$ restricted to it is $t \mapsto (t^2, t^3)$.

**Example P0.5.25.** If $C$ does not pass through $0$, then $\pi^{-1}(C)$ does not meet $E$ and $\pi^{-1}(C) \cong C$. There is no factor $x^m$, and the definition of the multiplicity does not apply.

### Exercises

1. (A) Compute the strict transform of $C = V(xy(x - y))$. Show that it has three disjoint components, and find the three points where they meet $E$.
2. (A) Let $C = V(y^2 - x^4)$, the tacnode. Show that $\widetilde{C} \cap U_1 = V(t^2 - x^2)$. Show that $\widetilde{C}$ is singular at the point $(0, 0)$ of $U_1$, and that a second blow-up at this point makes the strict transform nonsingular.
3. (A) Show that the strict transform of a curve $C \subset \mathbb{A}^2$ through $0$ does not depend on the choice of linear coordinates up to the action of $\mathrm{GL}_2(k)$ on $\mathbb{P}^1$.
4. (B) Define $\operatorname{Bl}_0 \mathbb{A}^n \subset \mathbb{A}^n \times \mathbb{P}^{n-1}$ by the equations $x_i u_j = x_j u_i$. Show that it is covered by $n$ open sets isomorphic to $\mathbb{A}^n$, and that $\pi^{-1}(0) \cong \mathbb{P}^{n-1}$.
5. (B) In $\operatorname{Bl}_p \mathbb{P}^2$, let $\widetilde{M}$ be the preimage of a line $M$ that does not pass through $p$. Show that $\widetilde{M} \cap E = \emptyset$ and that $q$ restricts to an isomorphism $\widetilde{M} \to \mathbb{P}^1$.

### Lean

Not in Lean. Mathlib has no blow-up of a scheme along a closed subscheme, and no strict transform. A formal version could use the charts above, or the relative Proj of the Rees algebra $\bigoplus_n \mathfrak{m}^n$.

### Notes and history

The blow-up of a point, called the $\sigma$-process in the older literature, goes back to the work of Max Noether and others on plane curve singularities in the nineteenth century. Hartshorne treats it at the end of Section I.4, and Shafarevich in Chapter 2. The general blow-up of a scheme along a closed subscheme is in P3 Ch. 11. The surface $\operatorname{Bl}_p \mathbb{P}^2$ is the Hirzebruch surface $\mathbb{F}_1$ (P5 Ch. 9). P5 Ch. 6 shows $E^2 = -1$, and Volume 4 computes the discrepancy $a(E, \mathbb{A}^2) = 1$, which is the coefficient of $E$ in $K_X = \pi^* K_{\mathbb{A}^2} + E$. The resolutions of the node and the cusp above return in P8 Ch. 4, and the cusp again in Volume 4, where its log canonical threshold is $\frac56$.
