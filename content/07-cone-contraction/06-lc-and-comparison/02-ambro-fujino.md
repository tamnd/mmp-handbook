---
title: The theorems of Ambro and Fujino for lc pairs
nodes: [MMV52CGQMS]
sources: [Fuj11, Amb03d, Fuj17d]
reads_with: [Fuj11:1.1, Fuj17d:ch5, Fuj17d:ch6]
requires: [4.2, 5.1, 5.2, 7.4, 7.5]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The theorems of Ambro and Fujino for lc pairs

### Statement

This section states the cone, contraction, base point free and vanishing theorems for arbitrary projective lc pairs, due to Ambro and Fujino, and sketches their proofs. The proofs are not given in full: each theorem is marked as cited, and the proof sections are sketches. The hypothesis of Section 1, a klt boundary, is dropped. The new difficulty is the non-klt locus, which may be a variety with its own cohomology, like the elliptic curve over the vertex of Example 7.6.5, and the Kawamata-Viehweg vanishing of Volume 5 fails for lc pairs with nef and big divisors (Example 5.1.17). Throughout, $X$ is a normal projective variety of dimension $d$ over a field of characteristic $0$ and $(X, \Delta)$ is an lc pair with $\Delta$ a $\mathbb{Q}$-divisor and $a (K_X + \Delta)$ Cartier.

**Definition 7.6.7 (lc centres and the non-klt locus).** An *lc centre* of $(X, \Delta)$ is the image in $X$ of a divisor $G$ over $X$ with $a(G, X, \Delta) = -1$. The *non-klt locus* $\operatorname{Nklt}(X, \Delta)$ is the union of the lc centres, a closed subset of $X$, and $(X, \Delta)$ is klt exactly when it is empty.

**Theorem 7.6.8 (Fujino's vanishing theorem, cited).** Let $f \colon X \to Z$ be a morphism to a projective variety and $N$ a Cartier divisor on $X$ with $N - (K_X + \Delta) \sim_\mathbb{Q} f^* A$ for an ample $\mathbb{Q}$-divisor $A$ on $Z$.

1. Every associated prime of $R^j f_* \mathcal{O}_X(N)$ is the generic point of the image of $X$ or of an lc centre of $(X, \Delta)$, for every $j \ge 0$.
2. $H^i(Z, R^j f_* \mathcal{O}_X(N)) = 0$ for every $i > 0$ and $j \ge 0$.

In particular, for $Z = X$ and $f = \operatorname{id}$, $H^i(X, \mathcal{O}_X(N)) = 0$ for $i > 0$ whenever $N - (K_X + \Delta)$ is ample. If $W$ is a union of lc centres, the restriction $H^0(X, \mathcal{O}_X(N)) \to H^0(W, \mathcal{O}_W(N))$ is surjective, where $W$ carries the reduced structure given by a natural ideal $\mathcal{I}_W$ with $H^1(X, \mathcal{I}_W(N)) = 0$.

Lean: not yet in Lean.

**Theorem 7.6.9 (the base point free theorem for lc pairs, cited).** Let $L$ be a nef Cartier divisor with $b L - (K_X + \Delta)$ ample for some $b > 0$. Then $|m L|$ is free for every $m \gg 0$.

Lean: not yet in Lean.

**Theorem 7.6.10 (the cone theorem for lc pairs, Ambro and Fujino, cited).** Let $H$ be ample.

1. $\overline{NE}(X) = \overline{NE}(X)_{K_\Delta \ge 0} + \sum_j \mathbb{R}_{\ge 0} [C_j]$ for countably many rational curves $C_j$ with $0 < -K_\Delta \cdot C_j \le 2d$, each spanning a $K_\Delta$-negative extremal ray.
2. For every $\varepsilon > 0$ only finitely many $C_j$ are $(K_\Delta + \varepsilon H)$-negative.
3. Every $K_\Delta$-negative extremal face $F$ is cut out by a nef Cartier divisor $L$ with $L - K_\Delta$ ample.

Lean: `MinimalModel.ConeTheoremLc`, in the project library, states parts 1 and 2 as a statement without proof.

**Theorem 7.6.11 (the contraction theorem for lc pairs, Fujino, cited).** Every $K_\Delta$-negative extremal face $F$ has a contraction $\varphi_F \colon X \to Y$ onto a normal projective variety with the properties 1 to 4 of Theorem 7.5.2.

Lean: not yet in Lean.

### Proof in words

*A sketch.* The proofs in this volume use three facts about a klt pair: Kawamata-Viehweg vanishing, the nonvanishing theorem behind the base point free theorem, and Shokurov's argument that a divisor $L$ with $L - K_\Delta$ ample has a section not vanishing at a chosen point, obtained by producing an lc centre there and lifting sections from it. For lc pairs the lc centres are already present and need not be produced. Ambro's idea (Amb03d) is to treat the non-klt locus $W$ as a variety in its own right, with a structure he calls a *quasi-log structure*: an snc pair upstairs whose image is $W$ and whose discrepancy data restrict from those of $(X, \Delta)$. Theorem 7.6.8, proved by Fujino through the Hodge theory of snc pairs (the injectivity theorem of Section 5.2 for reduced snc divisors), is the vanishing theorem for these objects. It lets sections of $\mathcal{O}_W(mL)$ lift to $X$. Base point freeness on $W$ follows by induction on dimension, since $W$ has smaller dimension and lc centres of a quasi-log structure again carry quasi-log structures (adjunction). The base point free theorem for $X$ then follows from that on $W$ and the klt argument away from $W$. The rationality theorem and the cone theorem follow from the base point free theorem as in Chapters 3 and 4, and the contraction theorem as in Chapter 5. The rational curves with the bound $2d$ come from a separate argument of Fujino, which reduces to a dlt model of $(X, \Delta)$ and uses Kawamata's theorem there.

### Examples

**Example 7.6.12 (three lines in the plane).** Let $X = \mathbb{P}^2$ and $\Delta = \ell_1 + \ell_2 + \ell_3$, three lines in general position, so $(X, \Delta)$ is lc, $K_X + \Delta \sim 0$, and the lc centres are the three lines and their three intersection points, with $W = \operatorname{Nklt}(X, \Delta) = \Delta$. For $N = \mathcal{O}(1)$, $N - (K_X + \Delta) = \mathcal{O}(1)$ is ample, and the sequence $0 \to \mathcal{O}(-2) \to \mathcal{O}(1) \to \mathcal{O}_\Delta(1) \to 0$ gives $H^1(X, \mathcal{O}(-2)) = 0$ and a surjection $H^0(\mathcal{O}(1)) \to H^0(\mathcal{O}_\Delta(1))$, in fact an isomorphism of $3$-dimensional spaces, since $H^2(\mathcal{O}(-2)) = 0$. For $N = \mathcal{O}_X$, which is not allowed since $N - (K_X + \Delta) = 0$ is not ample, the sequence $0 \to \mathcal{O}(-3) \to \mathcal{O} \to \mathcal{O}_\Delta \to 0$ gives $H^1(\mathcal{O}_\Delta) \cong H^2(\mathcal{O}(-3)) = k$: the triangle $\Delta$ has arithmetic genus $1$, the cohomology of the lc centre that Theorem 7.6.8 has to control.

**Example 7.6.13 (the cone over a plane cubic again).** For the cone $X \subseteq \mathbb{P}^3$ over a smooth plane cubic of Example 7.6.5, $(X, 0)$ is lc with $\operatorname{Nklt}(X, 0) = \{v\}$ and $-K_X = \mathcal{O}_X(1)$ ample. Theorem 7.6.10 applies, where Theorem 7.6.2 did not: $\overline{NE}(X)$ is the ray of a line $\ell$ through $v$, a rational curve with $-K_X \cdot \ell = 1 \le 4$, and the contraction is $X \to \operatorname{Spec} k$. Theorem 7.6.8 with $N = 0$, where $N - K_X = \mathcal{O}(1)$ is ample, gives $H^i(X, \mathcal{O}_X) = 0$ for $i > 0$, although the resolution $Y$ of Example 7.6.5, ruled over an elliptic curve, has $H^1(Y, \mathcal{O}_Y) = k$. So $X$ does not have rational singularities, while vanishing holds on $X$ itself.

**Example 7.6.14 (lc centres and nef and big divisors).** In Example 5.1.17, $(X, E)$ is the blow-up of $\mathbb{P}^2$ at a point with its exceptional curve, $N = K_X + E + H$ and $N - (K_X + E) = H$ is nef and big, and $H^1(X, \mathcal{O}_X(N)) \ne 0$. The divisor $H$ is not ample: it is zero on the lc centre $E$. Theorem 7.6.8 in its relative form, for the blow-down $f \colon X \to \mathbb{P}^2$ with $H = f^* \ell$, gives the vanishing of $H^i(\mathbb{P}^2, f_* \mathcal{O}_X(N))$ for $i > 0$ instead, and part 1 says that the torsion of $R^j f_* \mathcal{O}_X(N)$ could only be supported at the image of $E$.

### Proof

*Sketch, Theorem 7.6.8.* This is proved in Fuj11 and in Fuj17d, Chapter 5. One passes to a dlt blow-up, and then to an snc pair $(V, \Delta_V)$ over $X$ with $K_V + \Delta_V = g^*(K_X + \Delta)$ up to an effective exceptional divisor. The reduced part of $\Delta_V$ is a simple normal crossing divisor, and the injectivity theorem for snc pairs, proved by mixed Hodge theory as in Theorem 5.2.2, gives torsion freeness and vanishing for $V$ and each stratum of the reduced boundary. These descend to $X$ because the higher direct images of $\mathcal{O}_V$ twisted by the exceptional part vanish. The restriction statement follows from vanishing for the ideal sheaf $\mathcal{I}_W$, defined as the pushforward of $\mathcal{O}_V(-\lfloor \Delta_V \rfloor^{=1})$ twisted by the exceptional part.

*Sketch, Theorem 7.6.9.* This is proved in Fuj11. If $(X, \Delta)$ is klt, it is the base point free theorem of Chapter 2. Otherwise let $W = \operatorname{Nklt}(X, \Delta)$. By adjunction for quasi-log structures (Amb03d; Fuj17d, Chapter 6), $W$ carries a quasi-log structure induced by $K_X + \Delta$, of smaller dimension, and by induction $|m L|_W|$ is free for $m \gg 0$. By Theorem 7.6.8 applied to $N = m L$, sections lift from $W$ to $X$, so the base locus of $|m L|$ is disjoint from $W$. Off $W$ the pair is klt, and the argument of Chapter 2, with Shokurov's creation of new lc centres at base points and Theorem 7.6.8 for lifting, removes the remaining base points.

*Sketch, Theorems 7.6.10 and 7.6.11.* This is Fuj11, Theorem 1.1, and Ambro (Amb03d) for quasi-log varieties. With Theorem 7.6.9 in place of the base point free theorem of Chapter 2, the rationality theorem holds with the same bound on denominators, and then the proofs of Lemma 7.4.3 to Corollary 7.4.7, which use only these two theorems, Kleiman's criterion and convexity, apply verbatim and give parts 2 and 3 and the decomposition without curves. The contraction is constructed from $L$ as in Theorem 7.5.2. For the rational curves of part 1, Fujino takes a dlt blow-up $g \colon (X', \Delta') \to (X, \Delta)$ with $K_{X'} + \Delta' = g^*(K_X + \Delta)$, perturbs $(X', \Delta')$ to klt pairs as in Section 1, and pushes forward the curves of Kawamata's theorem, using that $g$ contracts no curve in the relevant ray and the integrality argument of Theorem 7.6.2, part 3 (Fuj11).

### Exercises

1. (A) For $(\mathbb{P}^2, \ell_1 + \ell_2 + \ell_3)$, list the lc centres and compute $a(G, X, \Delta)$ for the exceptional divisor $G$ of the blow-up of the point $\ell_1 \cap \ell_2$.
2. (A) In Example 7.6.12, check $h^0(\mathcal{O}_\Delta(1)) = 3$ directly from the three lines glued at three points.
3. (B) Let $X$ be the cone over a smooth plane curve of degree $e \ge 4$. Show that $X$ is not lc, and that for $e = 3$ it is lc with the vertex as the only lc centre.
4. (B) Let $(X, \Delta) = (\mathbb{P}^1 \times \mathbb{P}^1, D_1 + D_2)$ for two distinct fibres of the first projection. Use Theorem 7.6.10 to find the cone and its negative rays, and check the lengths against $2d = 4$.
5. (B) In Example 7.6.14, write $N = f^* \mathcal{O}(-2) + 2E$, compute $f_* \mathcal{O}_X(N)$ and $R^1 f_* \mathcal{O}_X(N)$, and check that $R^1 f_* \mathcal{O}_X(N)$ is a skyscraper sheaf of length $1$ at the image of $E$ and that $H^i(\mathbb{P}^2, f_* \mathcal{O}_X(N)) = 0$ for $i > 0$.
6. (C) Let $(X, \Delta)$ be lc and suppose that every lc centre is a point. Show that $\operatorname{Nklt}(X, \Delta)$ is a finite set, that a quasi-log structure on a point is trivial, and deduce Theorem 7.6.9 in this case from the klt argument and Theorem 7.6.8 alone.

### Lean

The library has `MinimalModel.ConeTheoremLc`, for lc pairs over a field of characteristic $0$, as a statement without proof, attached to Fuj11. The vanishing, base point free and contraction theorems for lc pairs are not yet in Lean.

### Notes and history

Ambro introduced quasi-log varieties in Amb03d and proved the cone theorem for them, which contains the lc case. Fujino gave a complete and simplified treatment of the vanishing theorems, the base point free theorem and the cone and contraction theorems for lc pairs in Fuj11, by working with snc pairs rather than general quasi-log structures, and the book Fuj17d develops the theory of quasi-log schemes in full. The length bound $2d$ for lc pairs is also in Fuj11. This section only sketches these proofs; the rest of the handbook uses them as cited results.
