---
title: Resolution, principalization and functoriality
nodes: []
sources: [Hir64, Kol07, BM97, Vil89, Wlo05, AKMW02, KM98, Stacks]
reads_with: [Kol07:3, Hir64:0, BM97:1, AKMW02:0, KM98:0.4]
requires: [P3.7, P3.11, P5.6, P8.4, P8.12, 4.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Resolution, principalization and functoriality

### Statement

Throughout, $k$ is a field of characteristic $0$, a variety is an integral separated scheme of finite type over $k$, and resolutions and exceptional sets are as in Definition P8.4.1. On a smooth variety a prime divisor has a local equation at each of its points, and the condition below is the one of Definition P5.6.12 in every dimension.

**Definition P8.5.1 (simple normal crossings).** Let $M$ be a smooth variety of dimension $n$.

1. A divisor $D = \sum d_i D_i$ on $M$, with distinct prime divisors $D_i$, has *simple normal crossings* (is *snc*) if every $D_i$ is smooth and, for every point $y \in M$, the local equations at $y$ of the $D_i$ that pass through $y$ are part of a regular system of parameters of $\mathcal{O}_{M, y}$. A closed subset of pure codimension $1$ is snc if the reduced divisor with that support is.
2. A smooth closed subvariety $Z \subseteq M$ has *simple normal crossings with* an snc divisor $D$ if every point $z \in Z$ has a regular system of parameters $x_1, \dots, x_n$ of $\mathcal{O}_{M, z}$ such that $Z = V(x_1, \dots, x_c)$ near $z$ and every $D_i$ through $z$ is $V(x_j)$ near $z$ for some $j$.

Lean: the condition of part 1 at a point is `MinimalModel.IsSncAt`.

**Definition P8.5.2 (kinds of resolution).** Let $X$ be a reduced separated scheme of finite type over $k$, with smooth locus $X_{\mathrm{sm}}$ and singular locus $\operatorname{Sing} X$.

1. A resolution $f \colon Y \to X$ is *strong* if it is an isomorphism over $X_{\mathrm{sm}}$ and $f^{-1}(\operatorname{Sing} X)$ is an snc divisor.
2. A *smooth blow-up sequence* over a smooth variety $M$ is a sequence $M_r \to M_{r-1} \to \dots \to M_0 = M$ in which $M_{i+1}$ is the blow-up of $M_i$ along a smooth irreducible closed subvariety $Z_i$ of codimension at least $2$ that has simple normal crossings with the reduced preimage $H_i$ in $M_i$ of the earlier centres. Here $H_0 = \emptyset$, and given an snc divisor $E \subseteq M$, the sequence is *adapted to* $E$ if each $Z_i$ has simple normal crossings with $H_i$ together with the preimage of $E$.
3. Let $X \subseteq M$ be a closed reduced subscheme of a smooth variety. An *embedded resolution* of $X$ is a smooth blow-up sequence $\pi \colon M' \to M$ that is an isomorphism over $M \setminus \operatorname{Sing} X$, such that the strict transform $X'$ of $X$ is smooth and has simple normal crossings with the snc divisor $\operatorname{Exc}(\pi)$.
4. Let $\mathcal{I} \neq 0$ be an ideal sheaf on a smooth variety $M$ and $E$ an snc divisor. A *principalization* of $\mathcal{I}$ adapted to $E$ is a smooth blow-up sequence $\pi \colon M' \to M$ adapted to $E$ such that $\mathcal{I} \cdot \mathcal{O}_{M'} = \mathcal{O}_{M'}(-F)$ for an effective divisor $F$, and $\operatorname{Supp} F \cup \pi^{-1}(E) \cup \operatorname{Exc}(\pi)$ is snc.
5. A *log resolution* of a pair $(X, \Delta)$, with $X$ normal and $\Delta$ an $\mathbb{R}$-divisor, is as in Definition 4.2.9 of Volume 4: a resolution $f \colon Y \to X$ whose exceptional set is a divisor and for which $\operatorname{Exc}(f) \cup \operatorname{Supp} f^{-1}_* \Delta$ is snc.

Lean: a log resolution of a pair is `MinimalModel.HasLogResolution`; the other notions are not in Lean.

**Theorem P8.5.3 (Hironaka's resolution).** Every reduced separated scheme of finite type over a field of characteristic $0$ has a strong resolution, which is a composite of blow-ups along smooth centres lying over $\operatorname{Sing} X$. If $X$ is quasi-projective, the resolution is projective.

Lean: not in Lean as stated.

**Theorem P8.5.4 (embedded resolution).** Every closed reduced subscheme $X$ of a smooth variety $M$ over a field of characteristic $0$ has an embedded resolution.

Lean: not in Lean as stated.

**Theorem P8.5.5 (principalization).** Let $M$ be a smooth variety over a field of characteristic $0$, $E$ an snc divisor and $\mathcal{I} \neq 0$ an ideal sheaf. Then $\mathcal{I}$ has a principalization adapted to $E$ that is an isomorphism over the open set where $\mathcal{I} = \mathcal{O}_M$.

Lean: not in Lean as stated.

**Theorem P8.5.6 (functorial resolution).** Over a field $k$ of characteristic $0$ there is a rule $X \mapsto (\mathrm{BR}(X) \to X)$ that assigns to each reduced separated scheme of finite type a strong resolution which is a composite of blow-ups along smooth centres, such that for every smooth morphism $\varphi \colon X' \to X$ the sequence of blow-ups of $\mathrm{BR}(X')$ is the pullback along $\varphi$ of the sequence for $X$, with the steps whose centres pull back to the empty set omitted. In particular $\mathrm{BR}(X') \cong \mathrm{BR}(X) \times_X X'$ over $X'$. The same holds for embedded resolution and for principalization, with smooth morphisms of the ambient varieties.

Lean: not in Lean as stated.

**Corollary P8.5.7 (equivariant resolution).** Let a smooth algebraic group $G$ over $k$ act on $X$, with $\operatorname{char} k = 0$. Then $G$ acts on $\mathrm{BR}(X)$ so that $\mathrm{BR}(X) \to X$ is equivariant.

Lean: not in Lean as stated.

**Theorem P8.5.8 (weak factorization).** Let $\varphi \colon X \dashrightarrow X'$ be a birational map of smooth complete varieties over a field of characteristic $0$ that is an isomorphism over an open set $U$. Then $\varphi$ is a composite $X = X_0 \dashrightarrow X_1 \dashrightarrow \dots \dashrightarrow X_l = X'$ of birational maps in which each $X_j$ is smooth and complete, $U$ maps isomorphically into each $X_j$, and each $X_j \dashrightarrow X_{j+1}$ or its inverse is the blow-up of a smooth centre disjoint from the image of $U$.

Lean: not in Lean as stated.

**Lemma P8.5.9 (exceptional sets).** Let $f \colon Y \to X$ and $h \colon Y' \to Y$ be proper birational morphisms of varieties.

1. If $y \notin \operatorname{Exc}(f)$, then $f$ is an isomorphism over a neighbourhood of $f(y)$. So $\operatorname{Exc}(f) = f^{-1}(f(\operatorname{Exc}(f)))$, and $f$ is an isomorphism over $X \setminus f(\operatorname{Exc}(f))$.
2. $\operatorname{Exc}(f \circ h) = h^{-1}(\operatorname{Exc}(f)) \cup \operatorname{Exc}(h)$.
3. If $\pi \colon M_r \to M$ is a smooth blow-up sequence, then $\operatorname{Exc}(\pi)$ is the support of an effective Cartier divisor, the union of the preimages in $M_r$ of the exceptional divisors of the blow-ups.

Lean: not in Lean as stated.

**Proposition P8.5.10 (log resolutions of pairs).** Let $X$ be a normal variety over a field of characteristic $0$ and $\Delta$ an $\mathbb{R}$-divisor on $X$. Then $(X, \Delta)$ has a log resolution, projective if $X$ is quasi-projective.

Lean: not in Lean as stated.

**Proposition P8.5.11 (an antiample exceptional divisor).** Let $\pi \colon M_r \to M$ be a smooth blow-up sequence over a smooth quasi-projective variety. Then there is an effective Cartier divisor $A$ on $M_r$ with $\operatorname{Supp} A = \operatorname{Exc}(\pi)$ such that $-A$ is $\pi$-ample.

Lean: not in Lean as stated.

### Proof in words

The theorems of Hironaka, of the functorial school and of weak factorization are cited. What is proved here is what follows from them formally. A functorial resolution commutes with smooth morphisms, and the action and the projection $G \times X \to X$ are both smooth, so the two pullbacks of $\mathrm{BR}(X)$ to $G \times X$ agree, which is an action on $\mathrm{BR}(X)$. A log resolution of a pair comes from a strong resolution, whose exceptional set is already snc, followed by a principalization of the ideal of the preimage of the boundary adapted to that snc divisor. The bookkeeping of exceptional sets needs only the fact that a section of a separated morphism is a closed immersion. The antiample divisor comes from the tautological sheaf $\mathcal{O}(1) = \mathcal{O}(-E)$ of each blow-up.

### Examples

**Example P8.5.12 (the Whitney umbrella).** Let $X = V(x^2 - y^2 z) \subseteq \mathbb{A}^3$, whose singular locus is the line $L = V(x, y)$. Blow up $\mathbb{A}^3$ along $L$. In the chart $x = x'y$ the total transform is $V(y^2(x'^2 - z))$, the exceptional divisor is $E = V(y)$, and the strict transform is $X' = V(z - x'^2)$, which is smooth and meets $E$ transversally. In the chart $y = y'x$ it is $X' = V(1 - y'^2 z)$, again smooth and transversal to $E = V(x)$. So one blow-up along the singular locus is an embedded resolution, and $X' \cong \mathbb{A}^2$, with coordinates $x', y$ and the map $(x', y) \mapsto (x'y, y, x'^2)$, which is the normalization of Example P3.7.40. The preimage of $L$ in $X'$ is the smooth curve $V(y)$, so this is a strong resolution, although the map from that curve to $L$ has degree $2$.

**Example P8.5.13 (the cusp, resolved and embedded).** For the cusp $C = V(y^2 - x^3) \subseteq \mathbb{A}^2$, one blow-up of the origin makes the strict transform smooth, and $C_1 \to C$ is its normalization. The strict transform is tangent to the exceptional curve, though, so this is not an embedded resolution in the sense of Definition P8.5.2. After two blow-ups three curves pass through one point, and only the third blow-up gives an embedded resolution, the minimal log resolution of Example P8.4.11. An embedded resolution of $X$ asks more than a resolution of $X$.

**Example P8.5.14 (the cone over a smooth plane curve).** Let $V \subseteq \mathbb{P}^2$ be a smooth curve of degree $e \geq 2$ and $X = C(V, \mathcal{O}_V(1))$ the affine cone, as in Definition P8.12.1. By Proposition P8.12.3, the blow-up of the vertex $f \colon Y \to X$ is a resolution with exceptional divisor $E \cong V$, a smooth curve, with $\mathcal{O}_Y(E)|_E \cong \mathcal{O}_V(-1)$ of degree $-e$, and $K_Y \sim p^* K_V - E$. It is an isomorphism away from the vertex, so it is a strong resolution with one blow-up of a point. The discrepancy of $E$ is computed in Chapter 13.

**Example P8.5.15 (the quadratic transformation).** Let $\varphi \colon \mathbb{P}^2 \dashrightarrow \mathbb{P}^2$, $[x : y : z] \mapsto [yz : xz : xy]$, an isomorphism over the complement $U$ of the three coordinate lines. Let $S \to \mathbb{P}^2$ be the blow-up of the three coordinate points. The strict transforms of the three coordinate lines are disjoint $(-1)$-curves, by Proposition P5.6.4, and $\varphi$ lifts to a morphism $S \to \mathbb{P}^2$ that contracts them. So $\varphi$ is the composite of three blow-ups of points followed by three blow-downs, a factorization as in Theorem P8.5.8 with $l = 6$ in which all blow-ups come first. Weak factorization says that such a factorization exists in every dimension; the strong form, with all blow-ups first, is an open problem in dimension at least $3$.

### Proof

*Corollary P8.5.7.* Let $a, p_2 \colon G \times X \to X$ be the action and the projection. The projection is smooth because $G$ is smooth over $k$, and $a = p_2 \circ \alpha$ for the automorphism $\alpha(g, x) = (g, gx)$ of $G \times X$, so $a$ is smooth. By Theorem P8.5.6, $\mathrm{BR}(G \times X)$ is isomorphic over $G \times X$ both to $\mathrm{BR}(X) \times_{X, a} (G \times X)$ and to $\mathrm{BR}(X) \times_{X, p_2} (G \times X) = G \times \mathrm{BR}(X)$. Composing one isomorphism with the inverse of the other and then projecting to $\mathrm{BR}(X)$ gives a morphism $\tilde a \colon G \times \mathrm{BR}(X) \to \mathrm{BR}(X)$ with $f \circ \tilde a = a \circ (1 \times f)$, where $f \colon \mathrm{BR}(X) \to X$. Two morphisms from a reduced scheme to the separated $X$-scheme $\mathrm{BR}(X)$ that lie over the same morphism to $X$ agree if they agree on a dense open set. The axioms of an action for $\tilde a$ hold over the dense open set where $f$ is an isomorphism, since they hold for $a$, so they hold everywhere.

*Lemma P8.5.9.* For part 1, let $V \ni y$ be open with $f|_V$ an isomorphism onto an open $W \ni f(y)$, and let $u \colon W \to V \subseteq f^{-1}(W)$ be the inverse. Then $u$ is a section of $f$ over $W$. A section of a separated morphism is a closed immersion, so $u(W)$ is a closed subset of the irreducible scheme $f^{-1}(W)$ of the same dimension, hence equal to it as a set. Since $f^{-1}(W)$ is reduced, $u$ is an isomorphism onto $f^{-1}(W)$, and $f$ is an isomorphism over $W$. So no point over $W$ lies in $\operatorname{Exc}(f)$, which gives the two equalities; normality of $X$ is not needed.

For part 2, if $y' \notin \operatorname{Exc}(h)$ and $h(y') \notin \operatorname{Exc}(f)$, then $h$ maps a neighbourhood of $y'$ isomorphically onto an open set, which can be shrunk so that $f$ maps it isomorphically onto an open set, so $y' \notin \operatorname{Exc}(f \circ h)$. Conversely, let $V' \ni y'$ be open with $f \circ h|_{V'}$ an isomorphism onto an open $W$. The morphism $s = h \circ (f \circ h|_{V'})^{-1} \colon W \to f^{-1}(W)$ is a section of $f$ over $W$, so, as in part 1, $f$ is an isomorphism over $W$ and $h(y') \notin \operatorname{Exc}(f)$. Then $h|_{V'}$ is the composite of the isomorphism $f \circ h|_{V'} \colon V' \to W$ with the isomorphism $(f|_{f^{-1}(W)})^{-1} \colon W \to f^{-1}(W)$, an open subset of $Y$, so $y' \notin \operatorname{Exc}(h)$.

For part 3, let $\beta \colon \operatorname{Bl}_Z M \to M$ be the blow-up of a smooth centre of codimension $c \geq 2$, with exceptional divisor $E$, a Cartier divisor by part 2 of Theorem P3.11.3. It is an isomorphism over $M \setminus Z$ by part 3 of that theorem, and its fibres over $Z$ are projective spaces of dimension $c - 1 \geq 1$, by Theorem P3.11.4, so no point of $E$ is isolated in its fibre, and $\operatorname{Exc}(\beta) = E$. Induction on $r$ with part 2 gives $\operatorname{Exc}(\pi_{i+1}) = \beta_{i+1}^{-1}(\operatorname{Exc}(\pi_i)) \cup E_{i+1}$, and the preimage of the support of a Cartier divisor is the support of its pullback.

*Proposition P8.5.10.* Let $g \colon X' \to X$ be a strong resolution, by Theorem P8.5.3. Part 1 of Lemma P8.5.9 shows that $\operatorname{Exc}(g) = g^{-1}(\operatorname{Sing} X)$: the morphism $g$ is an isomorphism over $X_{\mathrm{sm}}$, and it is not an isomorphism over any neighbourhood of a singular point. So $E_1 = \operatorname{Exc}(g)$ is an snc divisor. Let $\mathcal{I}$ be the ideal sheaf of the reduced closed subset $g^{-1}(\operatorname{Supp} \Delta)$, which is the unit ideal if $\Delta = 0$, and let $h \colon Y \to X'$ be a principalization of $\mathcal{I}$ adapted to $E_1$, by Theorem P8.5.5, with $\mathcal{I} \cdot \mathcal{O}_Y = \mathcal{O}_Y(-F)$. Put $f = g \circ h$. By parts 2 and 3 of Lemma P8.5.9, $\operatorname{Exc}(f) = h^{-1}(E_1) \cup \operatorname{Exc}(h)$ is a divisor. The strict transform of each component of $\Delta$ lies in $h^{-1}(V(\mathcal{I})) = \operatorname{Supp} F$. So $\operatorname{Exc}(f) \cup \operatorname{Supp} f^{-1}_* \Delta$ is a union of components of the snc divisor $\operatorname{Supp} F \cup h^{-1}(E_1) \cup \operatorname{Exc}(h)$, and is snc. If $X$ is quasi-projective, $g$ and $h$ are projective, being composites of blow-ups.

*Proposition P8.5.11.* Induction on $r$, the case $r = 0$ being $A = 0$. For one blow-up $\beta$ along $Z$ with exceptional divisor $E$, $\mathcal{O}(-E) = \mathcal{I}_Z \cdot \mathcal{O}$ is the sheaf $\mathcal{O}(1)$ of the Proj of the Rees algebra of Definition P3.11.1, which is generated in degree $1$, so $-E$ is $\beta$-ample. Write $\pi = \pi' \circ \beta$, where $\pi' \colon M_{r-1} \to M$ has an effective $A'$ with $\operatorname{Supp} A' = \operatorname{Exc}(\pi')$ and $-A'$ relatively ample, and $\beta$ is the last blow-up. For a $\beta$-ample sheaf $L$ and a $\pi'$-ample sheaf $L'$, $L \otimes \beta^* L'^{\otimes N}$ is $\pi$-ample for $N \gg 0$, over the quasi-compact base $M$ (the Stacks Project, the chapter on morphisms of schemes, the section on relatively ample invertible sheaves). So $A = N \beta^* A' + E$ has $-A$ relatively ample for $N \gg 0$, and $\operatorname{Supp} A = \beta^{-1}(\operatorname{Exc}(\pi')) \cup E = \operatorname{Exc}(\pi)$ by Lemma P8.5.9.

### Exercises

1. (A) Show that $V(xyz) \subseteq \mathbb{A}^3$ is snc and that $V(xy(x - y)) \subseteq \mathbb{A}^3$ is not, and show that the blow-up of the $z$-axis is a log resolution of the second.
2. (A) In Example P8.5.12, check that the two charts glue, that $X'$ meets $E$ in a smooth curve, and that $X' \to X$ is finite.
3. (B) Show that the cone over a smooth plane cubic has a log resolution with one exceptional curve $E$, and that $E$ is an elliptic curve with $E^2 = -3$.
4. (B) Verify the factorization of Example P8.5.15: compute the lift $S \to \mathbb{P}^2$ in coordinates near one exceptional curve, and show that it contracts the strict transforms of the three coordinate lines.
5. (B) Let $M_2 \to M_1 \to \mathbb{A}^3$ be the blow-up of the $z$-axis followed by the blow-up of a point of the exceptional divisor $E_1$. Show that the exceptional set of the composite is the union of the strict transform of $E_1$ and the second exceptional divisor, and that it is snc.
6. (C) Let $\mathbb{G}_m$ act on $\mathbb{A}^2$ by $t \cdot (x, y) = (t^2 x, t^3 y)$, which preserves the cusp $V(y^2 - x^3)$. Show directly from part 2 of Theorem P8.4.10, without Corollary P8.5.7, that $\mathbb{G}_m$ acts on the minimal log resolution of the cusp compatibly with its action on $\mathbb{A}^2$.

### Lean

The predicate `MinimalModel.IsSncAt` in `MinimalModel/Statements/Basic.lean` says that a set of prime divisors has simple normal crossings at a point and that the variety is smooth there: the divisors through the point have local equations that are part of a regular system of parameters of the stalk. This is part 1 of Definition P8.5.1 at one point. The predicate `MinimalModel.HasLogResolution` in the same file says that a pair has a log resolution: a proper birational morphism from a smooth variety such that the exceptional divisors and the strict transforms of the components of the boundary satisfy `MinimalModel.IsSncAt` at every point, and that is an isomorphism outside the images of the exceptional divisors. Its docstring records it as the hypothesis shared with one of the specifications of the program. The theorems of Hironaka, the functorial versions and weak factorization are not in Lean.

### Notes and history

Hironaka proved resolution, embedded resolution and principalization in characteristic $0$ in 1964, in a paper of over two hundred pages. Functorial and constructive versions came later: Villamayor in 1989 and Bierstone and Milman in 1997 gave algorithms driven by explicit invariants, Encinas and Hauser and Włodarczyk simplified them, and Kollár's book of 2007 presents a version whose output commutes with smooth morphisms. Abramovich, Karu, Matsuki and Włodarczyk proved weak factorization in 2002, using toroidal geometry and a result of Morelli, and Włodarczyk gave an independent proof. Strong factorization, with all blow-ups before all blow-downs, remains open in dimension at least $3$. Abramovich, Temkin and Włodarczyk, and independently McQuillan, later gave a resolution algorithm by weighted blow-ups, with a simpler invariant.
