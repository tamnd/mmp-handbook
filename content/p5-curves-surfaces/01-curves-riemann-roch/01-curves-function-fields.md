---
title: Curves and their function fields
nodes: []
sources: [Har77, Vak25, Ful69]
reads_with: [Har77:I.6, Har77:II.6, Vak25:ch17]
requires: [P0.5, P1.4, P1.7, P3.4, P3.7, P3.9, P4.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Curves and their function fields

### Statement

In this section $k$ is algebraically closed. A *curve* is an integral separated scheme of finite type over $k$ of dimension $1$. Its function field $K(C)$ is a finitely generated extension of $k$ of transcendence degree $1$, a *function field of one variable* over $k$. A curve is *smooth* if all its local rings are regular. Since $k$ is algebraically closed, this agrees with smoothness over $k$ (P3 Ch. 7). A point of a curve means a closed point unless the text says otherwise.

**Proposition P5.1.1 (local rings of a curve).** Let $C$ be a curve and $P \in C$ a closed point. The following are equivalent:

1. $\mathcal{O}_{C, P}$ is a discrete valuation ring;
2. $\mathcal{O}_{C, P}$ is normal;
3. $\mathcal{O}_{C, P}$ is regular.

So a curve is smooth if and only if it is normal, and the normalization of any curve is a smooth curve, finite and birational over it. For $P$ smooth, write $v_P$ for the valuation of $K(C)$ with ring $\mathcal{O}_{C, P}$.

Lean: not in Lean as stated.

**Proposition P5.1.2 (extension of morphisms).** Let $C$ be a smooth curve, $P \in C$ a point, and $Y$ a proper variety. Every morphism $C \setminus \{P\} \to Y$ extends uniquely to a morphism $C \to Y$. Hence every rational map from a smooth curve to a proper variety is a morphism.

Lean: not in Lean as stated.

**Theorem P5.1.3 (curves and function fields).** Let $K$ be a function field of one variable over $k$.

1. There is a smooth projective curve $C_K$ with $K(C_K) \cong K$, and its local rings at closed points are exactly the discrete valuation rings $R$ with $k \subseteq R \subseteq K$ and fraction field $K$.
2. A smooth curve $C$ with $K(C) \cong K$ is isomorphic to an open subscheme of $C_K$. If $C$ is proper, then $C \cong C_K$.
3. The functor $C \mapsto K(C)$ is an anti-equivalence from the category of smooth projective curves over $k$, with nonconstant morphisms, to the category of function fields of one variable over $k$, with $k$-embeddings.

Lean: not in Lean as stated.

**Proposition P5.1.4 (finite morphisms of curves).** Let $f \colon C \to D$ be a nonconstant morphism of smooth projective curves.

1. $f$ is finite and surjective, $f_* \mathcal{O}_C$ is locally free of rank $n = [K(C) : K(D)]$, and $n$ is called the *degree* $\deg f$.
2. For a point $Q \in D$ with local parameter $t$, the divisor $f^* Q = \sum_{f(P) = Q} e_P P$ with $e_P = v_P(f^* t) \geq 1$, the *ramification index*, satisfies $\deg f^* Q = \sum_{f(P) = Q} e_P = n$.
3. The pullback $f^* \colon \operatorname{Div}(D) \to \operatorname{Div}(C)$, extended linearly, satisfies $f^* \operatorname{div}(g) = \operatorname{div}(f^* g)$, $f^* \mathcal{O}_D(E) \cong \mathcal{O}_C(f^* E)$, and $\deg f^* E = \deg f \cdot \deg E$.

Lean: not in Lean as stated.

**Corollary P5.1.5.** Let $C$ be a smooth projective curve.

1. A nonconstant rational function $g \in K(C)$ defines a morphism $g \colon C \to \mathbb{P}^1$ of degree $[K(C) : k(g)]$, and $\deg \operatorname{div}_0(g) = \deg \operatorname{div}_\infty(g) = [K(C) : k(g)]$.
2. Two smooth projective curves that are birational are isomorphic. Every curve $C'$ is birational to a unique smooth projective curve, the normalization of a projective closure of $C'$.

Lean: not in Lean as stated.

### Proof in words

At a point of a curve the local ring is a one-dimensional Noetherian local domain, and for such rings normal, regular and valuation ring mean the same thing. A valuation ring is exactly what the valuative criterion asks for, so morphisms extend across smooth points into proper targets. A function field $K$ contains a transcendental element $x$, and the integral closure of $k[x]$ and of $k[1/x]$ in $K$ glue to the normalization of $\mathbb{P}^1$ in $K$. This is a smooth curve, finite over $\mathbb{P}^1$ and hence projective. Every valuation ring of $K/k$ contains $k[x]$ or $k[1/x]$, and so it is one of the local rings of this curve. Since the curve is built from $K$ alone, up to isomorphism, the dictionary between curves and fields follows from the extension of morphisms. For a finite morphism, the sheaf $f_* \mathcal{O}_C$ is torsion free over a curve whose local rings are principal ideal domains, hence locally free. Its rank, computed at the generic point, is the degree of the field extension, and computed at a closed point, is the sum of the ramification indices.

### Examples

**Example P5.1.6 (the projective line).** The function field $k(x)$ has as valuation rings the localizations $k[x]_{(x - a)}$ for $a \in k$ and $k[1/x]_{(1/x)}$, by Example P1.7.10 for $\mathbb{Q}$ and the same argument for $k[x]$, a principal ideal domain. So $C_{k(x)} = \mathbb{P}^1$. The automorphisms of $k(x)$ over $k$ are the Möbius transformations $x \mapsto (ax + b)/(cx + d)$, and by Theorem P5.1.3 they are the automorphisms of $\mathbb{P}^1$, the group $\mathrm{PGL}_2(k)$.

**Example P5.1.7 (an affine curve and its completion).** Let $k$ have characteristic not $2$ and $C' = V(y^2 - x^3 + x) \subseteq \mathbb{A}^2$. The partial derivatives $2y$ and $1 - 3x^2$ vanish together only where $y = 0$ and $x^2 = 1/3$, which is not on the curve, so $C'$ is smooth. Its closure in $\mathbb{P}^2$ is $y^2 z = x^3 - x z^2$, with one point at infinity $[0 : 1 : 0]$, where in the chart $y = 1$ the equation $z = x^3 - x z^2$ has nonzero linear term. So the closure $C$ is the smooth projective curve of $K(C') = k(x)[y]/(y^2 - x^3 + x)$. The function $x \colon C \to \mathbb{P}^1$ has degree $2$: its fibre over $a \in k$ is the two points $(a, \pm \sqrt{a^3 - a})$ unless $a \in \{0, 1, -1\}$, and its pole divisor is $2 [0 : 1 : 0]$, since $v(x) = -2$ and $v(y) = -3$ at infinity.

**Example P5.1.8 (the cuspidal cubic).** The cubic $C' = V(y^2 - x^3) \subseteq \mathbb{A}^2$ has function field $k(t)$ with $t = y / x$, and $x = t^2$, $y = t^3$. The local ring at the origin is not normal: $t$ is integral over it, as $t^2 = x$, but not in it. The normalization is $\mathbb{A}^1 \to C'$, $t \mapsto (t^2, t^3)$, which is a bijection on points and is not an isomorphism. So a bijective morphism of curves need not be an isomorphism unless the target is smooth (Exercise 3).

**Example P5.1.9 (projection of a plane curve).** Let $C \subseteq \mathbb{P}^2$ be a smooth curve of degree $d \geq 2$ and $O \in C$. The projection $\pi_O$ from $O$ is defined on $C \setminus \{O\}$ and extends to $C$ by Proposition P5.1.2, with $\pi_O(O)$ the point given by the tangent line at $O$. Its fibre over a line $L$ through $O$ is $(L \cap C) - O$, so by Bezout's theorem (Corollary P4.3.11) its degree is $d - 1$. For $O \notin C$, the projection is a morphism of degree $d$. A plane cubic is therefore a double cover of $\mathbb{P}^1$, and Example P5.1.7 is the case $O = [0 : 1 : 0]$ with $\pi_O = x$.

### Proof

*Proposition P5.1.1.* The local ring $\mathcal{O}_{C, P}$ is a Noetherian local domain of dimension $1$, since $C$ has dimension $1$ and $P$ is a closed point of an integral scheme. By Theorem P1.7.12, it is a DVR if and only if it is normal, if and only if it is regular. The normalization $\nu \colon \widetilde{C} \to C$ is finite, surjective and birational by part 3 of Theorem P3.7.36, so $\widetilde{C}$ is a curve, and it is normal, hence smooth.

*Proposition P5.1.2.* Let $R = \mathcal{O}_{C, P}$, a DVR with fraction field $K = K(C)$, and $\varphi \colon C \setminus \{P\} \to Y$ the morphism. The generic point gives $\operatorname{Spec} K \to Y$, and since $Y$ is proper over $k$, the valuative criterion (Theorem P3.4.32) gives a unique extension $\operatorname{Spec} R \to Y$ compatible with $\operatorname{Spec} R \to \operatorname{Spec} k$. The image of the closed point is a point $y$. Choose an affine open $V = \operatorname{Spec} B \ni y$. The lift gives a ring map $B \to R \subseteq K$, the same map $B \to K$ as the generic point of $\varphi$. The generators of $B$ map to finitely many elements of $R$, each regular on some open neighbourhood $U$ of $P$, so $B \to K$ factors through $\mathcal{O}_C(U)$ and defines a morphism $\psi \colon U \to V$. The morphisms $\psi$ and $\varphi$ agree at the generic point, hence on a dense open subset of $U \setminus \{P\}$, and so on all of $U \setminus \{P\}$ by Theorem P3.4.11, as $C$ is reduced and $Y$ is separated. So $\psi$ and $\varphi$ glue to a morphism $C \to Y$. Uniqueness holds by Theorem P3.4.11 again, since $C \setminus \{P\}$ is dense. A rational map from $C$ is defined on a dense open set, whose complement is finite, and the extension is done one point at a time.

*Theorem P5.1.3, part 1.* Choose $x \in K$ transcendental over $k$. Then $K$ is a finite extension of $k(x)$, since $K$ is finitely generated of transcendence degree $1$. Let $A_0$ and $A_\infty$ be the integral closures of $k[x]$ and of $k[1/x]$ in $K$. By Theorem P1.4.32 they are finitely generated $k$-algebras, finite over $k[x]$ and $k[1/x]$. Their localizations at $x$ agree: both equal the integral closure of $k[x, 1/x]$ in $K$. So $U_0 = \operatorname{Spec} A_0$ and $U_\infty = \operatorname{Spec} A_\infty$ glue to a scheme $C_K$ with a morphism $\pi \colon C_K \to \mathbb{P}^1$ that is finite, since it is finite over the two charts of $\mathbb{P}^1$. The scheme $C_K$ is integral of dimension $1$, normal, and separated, since a finite morphism is separated and $\mathbb{P}^1$ is separated. It is proper over $k$, as a finite morphism is proper and $\mathbb{P}^1$ is proper, and $\pi^* \mathcal{O}(1)$ is ample by part 2 of Corollary P4.2.11, so $C_K$ is projective (Theorem P3.6.25). So $C_K$ is a smooth projective curve with function field $K$.

Let $R$ be a DVR with $k \subseteq R \subseteq K$ and fraction field $K$. Then $x \in R$ or $1/x \in R$. Say $x \in R$. Since $R$ is integrally closed, $A_0 \subseteq R$. The prime $\mathfrak{p} = \mathfrak{m}_R \cap A_0$ is not zero: otherwise every nonzero element of $A_0$ would be a unit of $R$, and $R$ would contain the fraction field $K$ of $A_0$. So $\mathfrak{p}$ is a maximal ideal of $A_0$, and $(A_0)_\mathfrak{p} \subseteq R$ with $\mathfrak{p} (A_0)_\mathfrak{p} \subseteq \mathfrak{m}_R$. If the inclusion were strict, there would be $u \in R$ with $v(u) < 0$ for the valuation $v$ of the DVR $(A_0)_\mathfrak{p}$. Then $u^{-1} \in \mathfrak{p} (A_0)_\mathfrak{p} \subseteq \mathfrak{m}_R$ and $1 = u \cdot u^{-1} \in \mathfrak{m}_R$, a contradiction. So $R = (A_0)_\mathfrak{p} = \mathcal{O}_{C_K, P}$ for the point $P = \mathfrak{p}$. Conversely every local ring at a closed point is such a DVR, by Proposition P5.1.1.

*Part 2.* Let $C$ be a smooth curve with $K(C) = K$. The identity of $K$ is a birational map $C \dashrightarrow C_K$, which is a morphism $\varphi \colon C \to C_K$ by Proposition P5.1.2. For each closed point $P$ of $C$, the local ring $\mathcal{O}_{C, P}$ is a DVR of $K/k$ and dominates $\mathcal{O}_{C_K, \varphi(P)}$, so the two are equal by the argument above. If two points $P, P'$ of $C$ have the same image $Q$, then $\mathcal{O}_{C, P} = \mathcal{O}_{C_K, Q} = \mathcal{O}_{C, P'}$ as subrings of $K$. The two morphisms $\operatorname{Spec} \mathcal{O}_{C_K, Q} \to C$ through $P$ and through $P'$ agree at the generic point, so they are equal by part 1 of Theorem P3.4.32, since $C$ is separated, and $P = P'$. So $\varphi$ is injective and an isomorphism on all local rings. Its image is constructible and dense, hence cofinite and open, and $\varphi$ is a homeomorphism onto it, since the proper closed sets on both sides are the finite sets. A homeomorphism onto an open subset that is an isomorphism on all stalks is an open immersion. If $C$ is proper, the image of $\varphi$ is closed and open in the irreducible $C_K$, hence everything.

*Part 3.* A nonconstant morphism $f \colon C \to D$ is dominant, since its image is irreducible, closed and not a point, so it gives $f^* \colon K(D) \to K(C)$. Conversely a $k$-embedding $K(D) \to K(C)$ is a dominant rational map $C \dashrightarrow D$ by Theorem P0.5.12, and a morphism by Proposition P5.1.2. These are inverse to each other, because a morphism of varieties is determined by its restriction to a dense open set. Every function field is $K(C_K)$, by part 1. So the functor is fully faithful and essentially surjective.

*Proposition P5.1.4, part 1.* The image of $f$ is closed, since $C$ is proper, irreducible and not a point, hence equal to $D$. Let $V = \operatorname{Spec} B \subseteq D$ be an affine open set, and $A$ the integral closure of $B$ in $K(C)$. By Theorem P1.4.32, $A$ is a finite $B$-module, and $\operatorname{Spec} A$ is a smooth curve with function field $K(C)$. By the proof of part 2 of Theorem P5.1.3 applied to the maps to $C_{K(C)} = C$, both $\operatorname{Spec} A$ and $f^{-1}(V)$ are open subschemes of $C$ consisting of the points whose local rings contain $B$. So $f^{-1}(V) = \operatorname{Spec} A$, and $f$ is finite. The $B$-module $A$ is finite and torsion free. At a point $Q \in V$, the ring $\mathcal{O}_{D, Q}$ is a DVR, hence a principal ideal domain, and a finite torsion free module over it is free. So $f_* \mathcal{O}_C$ is locally free, and its rank is $\dim_{K(D)} A \otimes_B K(D) = [K(C) : K(D)]$.

*Part 2.* Let $Q \in D$ with local parameter $t$, and $A_Q = (f_* \mathcal{O}_C)_Q$, a free $\mathcal{O}_{D, Q}$-module of rank $n$. Then $A_Q / t A_Q$ has dimension $n$ over $k$. The ring $A_Q$ is a semilocal Dedekind domain whose maximal ideals are the points $P_1, \dots, P_r$ over $Q$, and $t A_Q = \prod_i \mathfrak{m}_{P_i}^{e_i}$ with $e_i = v_{P_i}(t)$, by Theorem P1.7.22. By the Chinese remainder theorem, $A_Q / t A_Q \cong \prod_i \mathcal{O}_{C, P_i} / \mathfrak{m}_{P_i}^{e_i}$, which has dimension $\sum_i e_i$, since each residue field is $k$.

*Part 3.* The pullback of a Cartier divisor is defined by pulling back local equations (Definition P3.9.26), which gives the first two formulas; on a smooth curve Weil and Cartier divisors are the same (Example P3.9.16). The degree formula is part 2 by linearity.

*Corollary P5.1.5, part 1.* A nonconstant $g$ is transcendental over $k$, and defines a dominant rational map $C \dashrightarrow \mathbb{P}^1$, a morphism by Proposition P5.1.2. Its degree is $[K(C) : k(g)]$ by Proposition P5.1.4, and $\operatorname{div}_0(g) = g^* (0)$, $\operatorname{div}_\infty(g) = g^* (\infty)$, both of degree $\deg g$ by part 2.

*Part 2.* Birational curves have isomorphic function fields, and part 2 of Theorem P5.1.3 applies. For a curve $C'$, choose an affine open set and its closure in some $\mathbb{P}^N$; the normalization of that closure is a smooth curve, finite over a projective curve, hence projective (Corollary P4.2.11), and birational to $C'$.

### Exercises

1. (A) Show that $\operatorname{div}(g)$ has degree $0$ for every $g \in K(C)^*$ using Corollary P5.1.5, and compare with the proof of part 1 of Corollary P4.3.17.
2. (A) Let $C = V_+(x^d + y^d + z^d) \subseteq \mathbb{P}^2$ with $d$ prime to the characteristic. Compute the ramification of the projection $[x : y : z] \mapsto [x : y]$ to $\mathbb{P}^1$ and check part 2 of Proposition P5.1.4.
3. (A) Let $f \colon C \to D$ be a morphism of curves with $D$ smooth. Show that if $f$ is bijective on points and birational, then it is an isomorphism. Use Example P5.1.8 to show that the smoothness of $D$ is needed.
4. (B) Show that $\mathbb{A}^2 \setminus \{0\}$ admits a morphism to $\mathbb{P}^1$ that does not extend to $\mathbb{A}^2$, and explain why Proposition P5.1.2 fails for surfaces.
5. (B) Let $K = k(x, y)$ with $y^2 = f(x)$ for a polynomial $f$ of degree $2g + 1$ or $2g + 2$ without repeated roots, and $k$ of characteristic not $2$. Describe the curve $C_K$ by two affine charts, and show that it has one or two points over $x = \infty$ according to the parity of $\deg f$.
6. (C) Let $k$ be a field that is not algebraically closed. Show that $C_K$ still exists for a function field $K/k$ of one variable, as a regular projective curve over $k$, and that it may fail to be smooth over $k$ when $k$ is not perfect. Use $K = k(x, y)$ with $y^2 = x^p - t$ over $k = \mathbb{F}_p(t)$, $p$ odd.

### Lean

Mathlib has discrete valuation rings, the valuative criteria and function fields of integral schemes, but not the curve of a function field. The handbook adds no `MinimalModel` node here.

### Notes and history

The construction of a curve from its function field, as the set of valuation rings, is due to Dedekind and Weber (1882), who called the points of $C_K$ the places of $K$ and proved the Riemann-Roch theorem in this setting. Zariski extended the idea to higher dimension as the Riemann-Zariski space, which is not a variety: in dimension $2$ and higher, a rational map need not extend across a point, and the blow-ups of P5 Ch. 6 and 7 measure the failure. The literature state is theorem. For the minimal model program, the consequence is that birational geometry of curves is trivial: each birational class has one smooth projective model. In higher dimension a birational class has many smooth projective models, and the program chooses one.
