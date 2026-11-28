---
title: Semistable families of surfaces
nodes: []
sources: [KKMS73, Kaw88, KM98, Kaw94, Kul77, PP81]
reads_with: [KM98:7, KKMS73:ch2]
requires: [1.5, 4.2, 4.4, 7.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Semistable families of surfaces

### Statement

In this section $T$ is a smooth quasi-projective curve, or the germ of one at a point $0$, and $f \colon X \to T$ is a projective surjective morphism with connected fibres from a normal variety $X$. For $t \in T$ write $X_t = f^*(t)$ as a divisor. Theorem 8.6.6 and Theorem 8.6.7 are cited; the outline of Theorem 8.6.6 is marked as an outline. Everything else is proved.

**Definition 8.6.1 (semistable families).** The morphism $f \colon X \to T$ is *semistable* if $X$ is smooth and every fibre $X_t$ is a reduced divisor with simple normal crossings. For $f$ semistable and $T$ a germ, the *dual complex* of $X_0$ is the simplicial complex with a vertex for each component of $X_0$, an edge for each component of the intersection of two components, and so on.

**Theorem 8.6.2 (semistable reduction, Kempf, Knudsen, Mumford and Saint-Donat; cited).** Let $f \colon X \to T$ be a flat projective morphism to the germ of a smooth curve, with smooth general fibre. There is a finite base change $T' \to T$, $s \mapsto s^e = t$, and a projective birational morphism $X' \to X \times_T T'$, an isomorphism over $T' \setminus \{0\}$, such that $X' \to T'$ is semistable.

Lean: not yet in Lean.

**Proposition 8.6.3 (the relative Zariski lemma).** Let $f \colon X \to T$ be as above with $T$ a germ at $0$, and $X_0 = \sum m_i F_i$ with $F_i$ prime. Let $D = \sum d_i F_i$ be a $\mathbb{Q}$-Cartier $\mathbb{Q}$-divisor supported on $X_0$. If $D$ is $f$-nef, then $D = c X_0$ for some $c \in \mathbb{Q}$; in particular $D \equiv_T 0$.

Lean: not yet in Lean.

**Theorem 8.6.4 (the $K$-MMP of a semistable family of surfaces).** Let $f \colon X \to T$ be semistable with $\dim X = 3$. Every $K_X$-MMP over $T$ terminates. Each model $f_i \colon X_i \to T$ is $\mathbb{Q}$-factorial and terminal, and every fibre $f_i^*(t)$ is reduced. If $K_{X_t}$ is nef for general $t \in T$, each step is an isomorphism over all but finitely many points of $T$ and the program ends with a minimal model over $T$.

Lean: not yet in Lean.

**Corollary 8.6.5 (trivial canonical class).** Let $f \colon X \to T$ be semistable with $\dim X = 3$, $T$ a germ at $0$, and $K_X \sim G$ for a divisor $G$ supported on $X_0$, as happens when $K_{X_t} \sim 0$ for $t \ne 0$ and $T$ is small enough. Then the output $X'$ of any $K_X$-MMP over $T$ is a minimal model over $T$ with $K_{X'} \sim_{\mathbb{Q}} 0$.

Lean: not yet in Lean.

**Theorem 8.6.6 (semistable flips, Kawamata; Kollár and Mori; cited).** The flips that occur in Theorem 8.6.4 can be constructed from the semistable structure alone, without Mori's flip theorem: if $\varphi \colon X_i \to Y$ is a small $K_{X_i}$-negative extremal contraction over $T$ in the program of Theorem 8.6.4, its exceptional locus lies in a fibre $X_{i,0}$, the pair $(X_i, X_{i,0})$ is dlt, and the flip of $\varphi$ exists.

Lean: not yet in Lean.

**Theorem 8.6.7 (Kulikov; Persson and Pinkham; cited).** Let $f \colon X \to \Delta$ be a semistable family over a disc whose fibres $X_t$, $t \ne 0$, are K3 surfaces, and suppose that every component of $X_0$ is Kähler. There is a semistable family $f' \colon X' \to \Delta$, possibly not projective over $\Delta$, isomorphic to $X$ over $\Delta \setminus \{0\}$, with $K_{X'} \sim 0$. Its central fibre is of one of three types:

1. Type I: $X'_0$ is a smooth K3 surface.
2. Type II: $X'_0 = V_0 \cup \dots \cup V_k$ is a chain, with $V_0$ and $V_k$ rational, $V_1, \dots, V_{k-1}$ elliptic ruled, and the double curves elliptic.
3. Type III: every component of $X'_0$ is rational, the double curves on each component form a cycle of rational curves, and the dual complex is a triangulation of the 2-sphere.

Lean: not yet in Lean.

### Proof in words

The relative Zariski lemma is a connectedness argument: subtract the largest multiple of the fibre that the divisor allows; what is left is effective, misses a component of the fibre and is anti-nef, and a curve in that component through a point where the two meet has positive degree on it. The semistable program is the program of Chapter 5 for a 3-fold over a curve. Pushing a reduced fibre forward keeps it reduced, and if $K$ is nef on the general fibre the program cannot touch it. When the canonical class is supported on the central fibre, it ends nef and supported on a fibre, and the Zariski lemma makes it a multiple of the fibre, which is trivial over a germ.

*Outline for Theorem 8.6.6 (marked as an outline).* Since $X_{i,0} \equiv_T 0$, a $K$-negative ray is also $(K + X_{i,0})$-negative. The pair $(X_i, X_{i,0})$ starts dlt and stays dlt along the program (KM98, Chapter 3). A flipping curve lies in $X_{i,0}$, and it meets the components of $X_{i,0}$ in a controlled way, which leads to a short list of semistable extremal neighbourhoods. For each, the flip is written down, by a cyclic cover and a toric or explicit construction, in KM98, Chapter 7, following Kawamata (Kaw88) and Kollár and Mori. Kawamata (Kaw94) carries the same program out over a discrete valuation ring of positive or mixed characteristic.

### Examples

**Example 8.6.8 (a quartic degenerating to a tetrahedron).** Let $F$ be a general quartic form on $\mathbb{P}^3$ and $X = \{xyzw + tF = 0\} \subset \mathbb{P}^3 \times \Delta$. The fibre $X_0$ is the union of the four coordinate planes, and $X_t$ is a smooth quartic, a K3 surface, for small $t \ne 0$. The total space is singular exactly where $t = 0$, two of the coordinates vanish and $F = 0$: each of the $6$ edges of the tetrahedron meets $\{F = 0\}$ in $4$ points, so there are $24$ singular points. At such a point, on the edge $x = y = 0$ say, $z$, $w$ are units and $F$ is a local coordinate $u$, and the equation is $xy \cdot \text{unit} = -tu$: an ordinary double point. Blowing up the planes $\{x = t = 0\}$, $\{y = t = 0\}$ and $\{z = t = 0\}$ one after the other gives a projective small resolution $X' \to X$. At each of the $24$ points one of the two planes through it is replaced by its blow-up at the point and the other is unchanged, the fibre $X'_0$ is a reduced divisor with simple normal crossings, and $X' \to \Delta$ is semistable. Since $X \in |\mathcal{O}(4)|$, adjunction gives $K_X \sim 0$, and $K_{X'} \sim 0$ because $X' \to X$ is small. The components are rational, the double curves on each are the three lines of a triangle, and the dual complex is the boundary of a tetrahedron: Type III.

**Example 8.6.9 (a quartic degenerating to two quadrics).** Let $Q_1$, $Q_2$ be general quadric forms and $X = \{Q_1 Q_2 + tF = 0\} \subset \mathbb{P}^3 \times \Delta$. The fibre $X_0$ is the union of two smooth quadrics meeting along the elliptic quartic curve $E = \{Q_1 = Q_2 = 0\}$. The total space is singular at the $4 \cdot 4 = 16$ points of $E \cap \{F = 0\}$, each an ordinary double point $Q_1 Q_2 = -tF$, and a small resolution gives a semistable family with $K \sim 0$ whose central fibre is two rational surfaces glued along an elliptic curve: Type II with $k = 1$.

**Example 8.6.10 (blowing up a point of a fibre).** Let $f \colon S \to T$ be a semistable family of curves, $p \in S_0$ a point where $S_0$ is smooth, and $\pi \colon S' \to S$ the blow-up of $p$ with exceptional curve $E$. Then $f'^*(0) = \pi^* S_0 = S_0' + E$ with $S_0'$ the strict transform, so $S' \to T$ is still semistable, and $K_{S'} \cdot E = -1$. So $E$ spans a $K$-negative extremal ray over $T$, and the $K_{S'}$-MMP over $T$ contracts it and returns $S$. If $p$ is a node of $S_0$ instead, $\pi^* S_0 = S_0' + 2E$ and the family is no longer semistable: semistability is not preserved by arbitrary blow-ups, and the program of Theorem 8.6.4 only ever pushes fibres forward. For surfaces, Proposition 8.6.3 says that a divisor supported on a fibre and nef over $T$ is a multiple of the fibre; here $E \cdot E = -1$ and $E \cdot S_0' = 1$, so neither $E$ nor $S_0'$ is nef over $T$.

### Proof

*Proof of Proposition 8.6.3.* The fibre $X_0 = f^*(0)$ is Cartier and $X_0 \equiv_T 0$, since $0$ is a principal divisor on the germ $T$. Let $c = \max_i d_i / m_i$ and $D' = cX_0 - D = \sum (c m_i - d_i) F_i$. Then $D' \ge 0$, $D'$ is $\mathbb{Q}$-Cartier, $-D' \equiv_T D$ is $f$-nef, and some component $F_j$ is not in $\operatorname{Supp} D'$. Suppose $D' \ne 0$. Since $f$ has connected fibres, $X_0$ is connected, so there are components $F_j \not\subset \operatorname{Supp} D'$ and $F_k \subset \operatorname{Supp} D'$ that meet; let $p \in F_j \cap F_k$. Since $F_j$ is projective and $F_j \cap \operatorname{Supp} D'$ is a proper closed subset of it containing $p$, there is a curve $C \subset F_j$ through $p$ and not contained in $\operatorname{Supp} D'$. Then $D' \cdot C > 0$, because $D'$ is effective, $\mathbb{Q}$-Cartier and meets $C$ in a non-empty finite set. This contradicts $D' \cdot C = -(-D' \cdot C) \le 0$. So $D' = 0$ and $D = c X_0$. $\square$

*Proof of Theorem 8.6.4.* The 3-fold $X$ is smooth, hence $\mathbb{Q}$-factorial and terminal, and projective over $T$, so the program terminates by Theorem 8.5.3, and each $X_i$ is $\mathbb{Q}$-factorial and terminal by Lemma 8.5.2. Let $f_i \colon X_i \to T$ be the induced morphisms. At a divisorial step $\varphi \colon X_i \to X_{i+1}$, $f_i^*(t) = \varphi^* f_{i+1}^*(t)$, so $f_{i+1}^*(t) = \varphi_* f_i^*(t)$; at a flip $f_{i+1}^*(t)$ is the strict transform of $f_i^*(t)$, since they agree in codimension one. In both cases the coefficients of $f_{i+1}^*(t)$ are among those of $f_i^*(t)$, so the fibres stay reduced.

Suppose $K_{X_t}$ is nef for general $t$, and suppose by induction that $X_i \to X$ is an isomorphism over a dense open $U \subset T$. Let $R$ be the ray of a step from $X_i$, and $\Sigma$ the union of the curves with class in $R$, which is the exceptional locus of the contraction or all of $X_i$. If $\Sigma$ dominates $T$, it contains a curve $C$ in a general fibre $X_{i,t} \cong X_t$, and by adjunction $K_{X_i} \cdot C = K_{X_t} \cdot C \ge 0$, which contradicts $K_{X_i} \cdot R < 0$. So $\Sigma$ lies over finitely many points of $T$, the contraction is birational, and the step is an isomorphism over the complement. So the program never reaches a Mori fibre space and ends with a minimal model over $T$. $\square$

*Proof of Corollary 8.6.5.* Every curve in a fibre $X_t$ with $t \ne 0$ has $K_X \cdot C = G \cdot C = 0$, so the argument of Theorem 8.6.4 shows that every step is an isomorphism over $T \setminus \{0\}$, and the output is a minimal model $X'$ over $T$. Let $G'$ be the push-forward of $G$, supported on $X'_0$. Since the steps push $K$ forward, $K_{X'} \sim G'$, which is $\mathbb{Q}$-Cartier because $X'$ is $\mathbb{Q}$-factorial and nef over $T$. By Proposition 8.6.3, $G' = cX'_0$, and $X'_0 = f'^*(0) \sim 0$ on the germ. So $K_{X'} \sim_{\mathbb{Q}} 0$. $\square$

### Exercises

1. (A) In Example 8.6.8, list the $24$ singular points of $X$ and check that each is an ordinary double point.
2. (A) In Example 8.6.9, check that $E = \{Q_1 = Q_2 = 0\}$ is a smooth curve of genus $1$ for general $Q_1$, $Q_2$, and that $E$ meets $\{F = 0\}$ in $16$ points.
3. (A) In Example 8.6.10, compute $\pi^* S_0$ when $p$ is a smooth point and when $p$ is a node of $S_0$, and compute $K_{S'} \cdot E$ and $E^2$.
4. (B) Let $S \to T$ be a family of curves over a germ, with central fibre $S_0 = \sum m_i F_i$. Deduce from Proposition 8.6.3 that a vector $(d_i)$ with $\sum_i d_i F_i \cdot F_j \ge 0$ for all $j$ is a multiple of $(m_i)$, and compare with Lemma 1.5.20.
5. (B) Show that Proposition 8.6.3 fails if the fibres of $f$ are not connected, with the example of a family whose central fibre is two disjoint curves.
6. (C) In Example 8.6.8, show that on each component of $X'_0$ the double curves form an anticanonical cycle, a triangle of lines on $\mathbb{P}^2$ or its strict transform, and use the triple point formula to check the self-intersections of the double curves on the blown-up planes.

### Lean

Nothing in this section is in Lean yet. Semistable families and the relative Zariski lemma would sit next to `MinimalModel.IsTerminal` and `MinimalModel.IsMinimalModel`.

### Notes and history

Theorem 8.6.2 is in KKMS73. The semistable MMP for families of surfaces is due to Kawamata (Kaw88), who used it to give a new proof of Kulikov's theorem with the canonical class trivial in the projective category but with terminal singularities on the total space, as in Corollary 8.6.5. The construction of semistable flips is KM98, Chapter 7, where it gives an independent route to the 3-fold program for semistable families. Kawamata (Kaw94) extends it to positive and mixed characteristic. Theorem 8.6.7 is due to Kulikov (Kul77) and to Persson and Pinkham (PP81). Their models are complex manifolds and in general not projective over the disc; the projective output of Corollary 8.6.5 is in general singular. Volume 10 discusses the semistable program in higher dimensions.
