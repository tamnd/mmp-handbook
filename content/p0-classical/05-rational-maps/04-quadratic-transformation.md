---
title: The standard quadratic transformation
nodes: [MMRP5RX4JJ]
sources: [Har77, Rei88, Sha13, Har92]
reads_with: [Har77:V.5, Rei88:ch5, Sha13:ch2, Har92:lecture7]
requires: [P0.3, P0.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The standard quadratic transformation

### Statement

Let $p_1 = (1 : 0 : 0)$, $p_2 = (0 : 1 : 0)$, $p_3 = (0 : 0 : 1)$ be the coordinate points of $\mathbb{P}^2$, and let $L_1 = \{x = 0\}$, $L_2 = \{y = 0\}$, $L_3 = \{z = 0\}$ be the coordinate lines. The line $L_i$ passes through the two points $p_j$ with $j \neq i$. Put $U = \mathbb{P}^2 \setminus \{p_1, p_2, p_3\}$ and $T = \mathbb{P}^2 \setminus (L_1 \cup L_2 \cup L_3) = \{xyz \neq 0\}$.

**Definition P0.5.26.** The *standard quadratic transformation* is the rational map

$$ \sigma : \mathbb{P}^2 \dashrightarrow \mathbb{P}^2, \quad (x : y : z) \mapsto (yz : xz : xy). $$

A *Cremona transformation* is a birational map $\mathbb{P}^2 \dashrightarrow \mathbb{P}^2$. The Cremona transformations form a group $\operatorname{Bir}(\mathbb{P}^2)$ under composition, the *Cremona group*.

Lean: not in Lean.

**Example P0.5.27.** On $T$ divide the three coordinates by $xyz$: $\sigma(x : y : z) = (1/x : 1/y : 1/z)$. So on the torus $T$ the map $\sigma$ is the inversion of coordinates, and it maps $T$ to $T$.

**Example P0.5.28.** On $L_1 \setminus \{p_2, p_3\}$ the coordinates satisfy $x = 0$ and $yz \neq 0$, so $\sigma(0 : y : z) = (yz : 0 : 0) = p_1$. The map $\sigma$ contracts the line $L_1$ minus two points to the point $p_1$. In the same way it contracts $L_2$ to $p_2$ and $L_3$ to $p_3$.

**Theorem P0.5.29 (the quadratic transformation).** Let $\sigma$ be the standard quadratic transformation.

1. The domain of definition of $\sigma$ is $U$. The map $\sigma$ restricts to an automorphism of $T$, and $\sigma \circ \sigma = \mathrm{id}$ as rational maps. So $\sigma$ is a Cremona transformation and its own inverse.
2. Let $(a : b : c)$ be coordinates on the target $\mathbb{P}^2$, and let $p'_i$ and $L'_i$ be its coordinate points and lines. The set $\Gamma = V(ax - by, by - cz) \subset \mathbb{P}^2 \times \mathbb{P}^2$ is the closure of the graph of $\sigma|_U$. Let $\pi$ and $\pi'$ be its two projections. Then $\pi$ is an isomorphism over $U$, and over each chart $\{x \neq 0\}$, $\{y \neq 0\}$, $\{z \neq 0\}$ of $\mathbb{P}^2$ it is isomorphic to the blow-up of $\mathbb{A}^2$ at the origin, with the origin at $p_1$, $p_2$, $p_3$. So $\pi$ is the blow-up of $\mathbb{P}^2$ at $p_1, p_2, p_3$. The same holds for $\pi'$ at $p'_1, p'_2, p'_3$, and $\sigma = \pi' \circ \pi^{-1}$.
3. Let $E_i = \pi^{-1}(p_i)$ and let $\widetilde{L}_i \subset \Gamma$ be the strict transform of $L_i$. Then $\pi'$ maps $E_i$ isomorphically onto the line $L'_i$, and $\pi'^{-1}(p'_i) = \widetilde{L}_i$. So $\pi'$ contracts the three disjoint curves $\widetilde{L}_1, \widetilde{L}_2, \widetilde{L}_3$, and $\sigma$ is the blow-up of three points followed by the contraction of three curves.

Lean: not in Lean.

*Proof.* Part 1. The three quadrics $yz$, $xz$, $xy$ vanish together exactly when two of $x, y, z$ vanish, that is, at $p_1$, $p_2$, $p_3$. So $\sigma$ is a morphism on $U$. It is not defined at $p_3$. Suppose that it is a morphism near $p_3$ with value $q$ at $p_3$. For $\lambda \in k$, let $M_\lambda = \{y = \lambda x\}$, a line through $p_3$. On $M_\lambda \cap U$, with $z = 1$, the map is $(\lambda x : x : \lambda x^2) = (\lambda : 1 : \lambda x)$, and this formula is a morphism on all of $M_\lambda \cap \{z \neq 0\}$ with value $(\lambda : 1 : 0)$ at $p_3$. Two morphisms from the curve $M_\lambda \cap \{z \neq 0\}$ that agree on a dense open set are equal (Section 5.2), so $q = (\lambda : 1 : 0)$ for every $\lambda$. This is false. By the symmetry of the formula under permutations of the coordinates, $\sigma$ is not defined at $p_1$ or $p_2$ either. The example above shows that $\sigma(T) \subset T$ and that $\sigma \circ \sigma = \mathrm{id}$ on $T$, since $1/(1/x) = x$. So $\sigma|_T$ is an automorphism of $T$, and $\sigma \circ \sigma = \mathrm{id}$ as rational maps.

Part 2. For $P = (x : y : z) \in U$ the point $\sigma(P) = (yz : xz : xy)$ satisfies $ax = by = cz = xyz$, so the graph of $\sigma|_U$ lies in $\Gamma$. Conversely, let $(P, Q) \in \Gamma$ with $P \in U$ and $Q = (a : b : c)$. If $xyz \neq 0$, then $(a, b, c) = \mu (1/x, 1/y, 1/z)$ with $\mu = ax$, so $Q = \sigma(P)$. If $x = 0$ and $yz \neq 0$, then $by = ax = 0$ and $cz = 0$, so $b = c = 0$ and $Q = p'_1 = \sigma(P)$. The other cases are the same. So $\Gamma \cap \pi^{-1}(U)$ is the graph of $\sigma|_U$, and $\pi$ maps it isomorphically onto $U$, with inverse $P \mapsto (P, \sigma(P))$.

Over the chart $z = 1$, which contains $p_3$ and no other $p_i$, the equations are $ax = by$ and $c = by$. If $a = b = 0$, then $c = 0$, which is impossible. So the rule $((x, y), (a : b : c)) \mapsto ((x, y), (b : a))$ is a morphism $\Gamma \cap \{z \neq 0\} \to \operatorname{Bl}_0 \mathbb{A}^2 = \{xv = yu\}$, with $u = b$ and $v = a$. Its inverse is $((x, y), (u : v)) \mapsto ((x, y), (v : u : uy))$, and the two maps commute with the projections to $\mathbb{A}^2$. So $\Gamma \cap \{z \neq 0\} \cong \operatorname{Bl}_0 \mathbb{A}^2$ over $\mathbb{A}^2$, with the origin at $p_3$. The equations $ax = by = cz$ are invariant under the simultaneous cyclic permutation of $(x, y, z)$ and $(a, b, c)$, so the same holds over the charts $x \neq 0$ and $y \neq 0$.

Thus $\Gamma$ is covered by the three open sets $\Gamma \cap \pi^{-1}\{x \neq 0\}$, $\Gamma \cap \pi^{-1}\{y \neq 0\}$, $\Gamma \cap \pi^{-1}\{z \neq 0\}$. Each is irreducible (Section 5.3), and each contains the nonempty open set $\pi^{-1}(T)$. A space covered by irreducible open sets that all contain one nonempty open set is irreducible. So $\Gamma$ is irreducible, and its nonempty open subset $\pi^{-1}(U)$, the graph of $\sigma|_U$, is dense in it. So $\Gamma$ is the closure of the graph.

The involution $\tau((x : y : z), (a : b : c)) = ((a : b : c), (x : y : z))$ preserves the equations $ax = by = cz$, so it is an automorphism of $\Gamma$ with $\pi' = \pi \circ \tau$. So $\pi'$ is also the blow-up at the three coordinate points. On $\pi^{-1}(U)$ the map $\pi' \circ \pi^{-1}$ is $P \mapsto \sigma(P)$, so $\sigma = \pi' \circ \pi^{-1}$ as rational maps.

Part 3. Put $x = y = 0$, $z = 1$ in the equations: $c = 0$, and $a, b$ are free. So $E_3 = \{p_3\} \times \{c = 0\} = \{p_3\} \times L'_3$, and $\pi'$ maps it isomorphically onto $L'_3$. Apply $\tau$: $\pi'^{-1}(p'_3) = \{z = 0\} \times \{p'_3\} = L_3 \times \{p'_3\}$. This set is closed and irreducible, and its points over $L_3 \setminus \{p_1, p_2\}$ form $\pi^{-1}(L_3 \setminus \{p_1, p_2\})$, by the example above. So it is the strict transform $\widetilde{L}_3$. The cases $i = 1, 2$ follow by the cyclic symmetry. The curves $\widetilde{L}_i = \pi'^{-1}(p'_i)$ are fibres of $\pi'$ over distinct points, so they are disjoint. $\square$

**Remark P0.5.30.** P5 Ch. 5 defines the self-intersection $D^2$ of a curve $D$ on a nonsingular projective surface, and P5 Ch. 6 shows that a blow-up at a nonsingular point of $D$ lowers $D^2$ by $1$. A line in $\mathbb{P}^2$ has $L^2 = 1$, and $L_i$ passes through two of the three blown-up points, so $\widetilde{L}_i^2 = 1 - 2 = -1$. This agrees with Part 3: $\widetilde{L}_i$ is the exceptional curve of $\pi'$ over $p'_i$, and an exceptional curve of the blow-up of a point has self-intersection $-1$. Each $\widetilde{L}_i$ is isomorphic to $\mathbb{P}^1$. A curve $E \cong \mathbb{P}^1$ with $E^2 = -1$ is a $(-1)$-curve.

**Theorem P0.5.31 (Castelnuovo's contractibility criterion).** Let $Y$ be a nonsingular projective surface over $k$, and let $E \subset Y$ be a curve with $E \cong \mathbb{P}^1$ and $E^2 = -1$. Then there are a nonsingular projective surface $Y_0$, a point $P \in Y_0$ and an isomorphism $Y \cong \operatorname{Bl}_P Y_0$ over $Y_0$ that maps $E$ to the exceptional curve.

Node: MMRP5RX4JJ · Lean: `MinimalModel.Castelnuovo`

This theorem is cited here without proof. It is Hartshorne Theorem V.5.7, and P5 Ch. 7 proves it. Part 3 above is an instance: the three $(-1)$-curves $\widetilde{L}_i$ on $\Gamma$ contract, and the contraction is $\pi'$, with $Y_0 = \mathbb{P}^2$.

**Theorem P0.5.32 (Noether and Castelnuovo).** The Cremona group $\operatorname{Bir}(\mathbb{P}^2)$ over an algebraically closed field $k$ is generated by the projective linear group $\mathrm{PGL}_3(k)$ and the standard quadratic transformation $\sigma$.

Lean: not in Lean.

This theorem is cited without proof. The proof is long. It studies the base points of a Cremona transformation and their multiplicities. It is not used in the handbook.

### Proof in words

The formula $(yz : xz : xy)$ is the inversion $(1/x : 1/y : 1/z)$ multiplied by $xyz$. Inversion is its own inverse on the torus, so the only question is what happens on the three coordinate lines. The graph closure answers it: the equations $ax = by = cz$ are symmetric in the source and the target, and in each chart they are the equation $xv = yu$ of the blow-up of a point. So both projections are blow-ups of three points. The curves contracted by one projection are the strict transforms of the coordinate lines, and the curves it blows down onto lines are the exceptional curves of the other projection.

### Examples

**Example P0.5.33.** Let $M = \{x + y + z = 0\}$, a line through none of the $p_i$. The set $M \cap T$ is dense in $M$, and $\sigma$ is continuous on $U$, so $\sigma(M \cap U)$ and $\sigma(M \cap T)$ have the same closure. A point $Q \in T$ lies in $\sigma(M \cap T)$ if and only if $\sigma(Q) \in M$, because $\sigma$ is an involution of $T$. The condition $\sigma(a : b : c) \in M$ is $bc + ac + ab = 0$. So $\sigma(M \cap T) = C \cap T$ with $C = \{bc + ac + ab = 0\}$. The conic $C$ is nonsingular: the partial derivatives $b + c$, $a + c$, $a + b$ vanish together only at $a = b = c = 0$ when $\operatorname{char} k \neq 2$, and when $\operatorname{char} k = 2$ they vanish at $(1 : 1 : 1)$, which is not on $C$. So $C$ is irreducible, $C \cap T$ is dense in $C$, and the closure of $\sigma(M \cap U)$ is $C$. The conic $C$ passes through $p'_1, p'_2, p'_3$. In general $\sigma$ maps a line through no $p_i$ to a conic through the three points $p'_i$, and the pullback of a line $\{\alpha a + \beta b + \gamma c = 0\}$ is the conic $\{\alpha yz + \beta xz + \gamma xy = 0\}$ through the three base points. This is the reason for the name quadratic.

**Example P0.5.34.** The rule "the image of a line is a conic" fails for a line through a base point. Let $M_\lambda = \{y = \lambda x\}$ with $\lambda \neq 0$, a line through $p_3$ and no other $p_i$. As in the proof of Part 1, $\sigma(x : \lambda x : z) = (\lambda z : z : \lambda x)$, so $\sigma$ maps $M_\lambda$ onto the line $\{a = \lambda b\}$, which passes through $p'_3$. The degree drops from $2$ to $1$. The pullback of the image line $\{a - \lambda b = 0\}$ is the conic $\{yz - \lambda xz = 0\}$, and it splits as $M_\lambda \cup L_3$. For $M = L_3$ itself the image is a point.

### Exercises

1. (A) Show that $E_i$ meets $\widetilde{L}_j$ if and only if $i \neq j$, and that then they meet in one point. So the six curves form a hexagon.
2. (A) Let $C$ be a nonsingular conic through $p_1, p_2, p_3$. Show that the closure of $\sigma(C \cap U)$ is a line through none of the $p'_i$.
3. (A) Show that $\sigma$ commutes with every permutation matrix and with every diagonal matrix $\operatorname{diag}(\lambda, \mu, \nu)$ up to replacing it by $\operatorname{diag}(\lambda^{-1}, \mu^{-1}, \nu^{-1})$.
4. (B) Let $C = V(F) \subset \mathbb{P}^2$ be a curve of degree $d$ that contains no $L_i$, with multiplicity $m_i$ at $p_i$. Show that $F(yz, xz, xy) = x^{m_1} y^{m_2} z^{m_3} G$ with $G$ of degree $2d - m_1 - m_2 - m_3$, and that the closure of $\sigma(C \cap U)$ is $V(G)$ when this curve is irreducible.
5. (B) Show that $\psi(x : y : z) = (xy : xz : z^2)$ is a Cremona transformation with inverse $(a : b : c) \mapsto (b^2 : ac : bc)$. Find the points where $\psi$ is not defined, and compare with $\sigma$.

### Lean

Not in Lean. Mathlib has projective spaces and rational maps of schemes, but no blow-up, so the factorization of Part 2 cannot be stated. The map node `MinimalModel.Castelnuovo` of tamnd/mmp-lean states the contractibility criterion for the program.

### Notes and history

Luigi Cremona studied birational maps of the plane in the 1860s, and the quadratic transformation is the basic example. Max Noether stated around 1870 that the quadratic transformations and the projective maps generate the Cremona group. His proof had a gap, and Castelnuovo gave the first complete proof in 1901. The literature state of both theorems in this section is theorem. Hartshorne proves the criterion as Theorem V.5.7. Castelnuovo's criterion is the step of the minimal model program for surfaces that contracts a $(-1)$-curve (P5 Ch. 12, and Volume 2). In higher dimension, the analogue of the contraction $\pi'$ is a divisorial contraction (Volume 1).
