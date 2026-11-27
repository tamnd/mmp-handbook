---
title: Riemann-Roch on a normal projective curve
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:IV.1, Vak25:ch19]
requires: [P2.7, P3.7, P3.8, P3.9, P4.2, P4.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Riemann-Roch on a normal projective curve

### Statement

In this section $k$ is a field and $C$ is a *normal projective curve* over $k$: an integral, normal, projective $k$-scheme of dimension $1$. Its local rings at closed points are discrete valuation rings (part 5 of Proposition P3.7.32), every Weil divisor is locally principal, and $\operatorname{Pic}(C) \cong \operatorname{Cl}(C)$ (Example P3.9.16). A divisor is a finite sum $D = \sum_P n_P P$ of closed points, and its *degree* is
$$\deg D = \sum_P n_P \, [\kappa(P) : k].$$
The arithmetic genus of Definition P4.3.9 is $p_a(C) = 1 - \chi(C, \mathcal{O}_C)$.

**Theorem P4.3.16 (Riemann-Roch, first form).** For every divisor $D$ on $C$,
$$\chi(C, \mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D)) = \deg D + 1 - p_a(C).$$

Lean: not in Lean as stated.

**Corollary P4.3.17 (consequences).** Let $D$ be a divisor on $C$ and $K = K(C)$ the function field.

1. $\deg \operatorname{div}(f) = 0$ for every $f \in K^*$. So $\deg$ is defined on $\operatorname{Pic}(C)$: for an invertible sheaf $\mathcal{L} \cong \mathcal{O}_C(D)$, $\deg \mathcal{L} = \deg D$ does not depend on $D$, and $\deg$ is a homomorphism $\operatorname{Pic}(C) \to \mathbb{Z}$.
2. If $\deg D < 0$, then $H^0(C, \mathcal{O}_C(D)) = 0$.
3. If $\deg D = 0$ and $H^0(C, \mathcal{O}_C(D)) \neq 0$, then $D \sim 0$.
4. $h^0(C, \mathcal{O}_C(D)) \geq \deg D + 1 - p_a(C)$. In particular $D$ is linearly equivalent to an effective divisor if $\deg D \geq p_a(C)$.

Lean: not in Lean as stated.

**Proposition P4.3.18 (degree of an embedded curve).** Let $\mathcal{L}$ be an invertible sheaf on $C$. Then $\chi(C, \mathcal{L}^{\otimes n}) = n \deg \mathcal{L} + 1 - p_a(C)$ for every $n \in \mathbb{Z}$. If $C \subseteq \mathbb{P}^r_k$ is a closed subscheme, then $P_C(n) = n \deg \mathcal{O}_C(1) + 1 - p_a(C)$, so the degree of Definition P4.3.9 is $\deg C = \deg \mathcal{O}_C(1)$.

Lean: not in Lean as stated.

The theorem is the *Riemann inequality* $h^0 \geq \deg D + 1 - p_a$ together with an exact correction term $h^1$. Serre duality, in a later chapter of this part, identifies $h^1(\mathcal{O}_C(D))$ with $h^0(\mathcal{O}_C(K_C - D))$ for a canonical divisor $K_C$, which turns the theorem into the classical statement of Roch.

### Proof in words

Adding a point $P$ to $D$ enlarges $\mathcal{O}_C(D)$ by a skyscraper sheaf with stalk $\kappa(P)$ at $P$, because the local ring at $P$ is a discrete valuation ring and $\mathcal{O}_C(D)$ is free of rank one there. A skyscraper sheaf has no higher cohomology and its global sections have dimension $[\kappa(P) : k]$, so $\chi$ increases by exactly the amount by which $\deg$ increases. Starting from $D = 0$, every divisor is reached by adding and removing points, so $\chi(\mathcal{O}_C(D)) - \deg D$ is the constant $\chi(\mathcal{O}_C)$. Linearly equivalent divisors have isomorphic sheaves and therefore the same $\chi$, so principal divisors have degree zero, and the remaining consequences come from comparing $\deg$ with an effective divisor of sections.

### Examples

**Example P4.3.19 (the projective line).** On $C = \mathbb{P}^1_k$, the point $\infty = V_+(x_0)$ has degree $1$ and $\mathcal{O}_C(\infty) \cong \mathcal{O}(1)$, so $\mathcal{O}_C(n \infty) \cong \mathcal{O}(n)$. By Theorem P4.2.1, $\chi(\mathcal{O}(n)) = n + 1$ for all $n$, which is the theorem with $p_a = 0$. A closed point $P = V_+(g)$, with $g$ an irreducible form of degree $e$, has $[\kappa(P) : k] = e$ and $P - e \infty = \operatorname{div}(g / x_0^e)$, so $\deg \colon \operatorname{Pic}(\mathbb{P}^1_k) \to \mathbb{Z}$ is an isomorphism, inverse to $n \mapsto [\mathcal{O}(n)]$.

**Example P4.3.20 (a conic without rational points).** Let $C = V_+(x^2 + y^2 + z^2) \subseteq \mathbb{P}^2_{\mathbb{R}}$. It is a smooth conic, hence a normal projective curve with $p_a(C) = 0$ by Example P4.3.12, and it has no $\mathbb{R}$-points. Every closed point $P$ has $\kappa(P)$ a finite extension of $\mathbb{R}$ different from $\mathbb{R}$, so $\kappa(P) \cong \mathbb{C}$ and $\deg P = 2$. The line $z = 0$ meets $C$ in the single closed point $P_0$ given by $x^2 + y^2 = 0$, with residue field $\mathbb{C}$, so $\mathcal{O}_C(1) \cong \mathcal{O}_C(P_0)$ has degree $2$, in agreement with Proposition P4.3.18. The image of $\deg$ is $2\mathbb{Z}$, and $C \not\cong \mathbb{P}^1_{\mathbb{R}}$, although $C_{\mathbb{C}} \cong \mathbb{P}^1_{\mathbb{C}}$. Corollary P4.3.17(4) gives $h^0(\mathcal{O}_C(P_0)) \geq 3$, and the three sections $x, y, z$ of $\mathcal{O}_C(1)$ realize this bound.

**Example P4.3.21 (smooth plane curves).** Let $C = V_+(f) \subseteq \mathbb{P}^2_k$ be a normal plane curve of degree $d$, so $p_a(C) = (d-1)(d-2)/2$ by Example P4.2.5 and $\deg \mathcal{O}_C(1) = d$. The sequence $0 \to \mathcal{O}(n - d) \to \mathcal{O}(n) \to \mathcal{O}_C(n) \to 0$ and Theorem P4.2.1 give $H^1(\mathcal{O}_C(n)) \cong H^2(\mathbb{P}^2_k, \mathcal{O}(n - d))$, which vanishes for $n \geq d - 2$. So for these $n$,
$$h^0(C, \mathcal{O}_C(n)) = nd + 1 - \frac{(d-1)(d-2)}{2},$$
and the inequality of Corollary P4.3.17(4) is an equality. For $n = d - 3$ and $d \geq 3$, $h^1 = h^2(\mathcal{O}(-3)) = 1$, so the inequality is strict by exactly one.

**Example P4.3.22 (normality is needed).** The nodal cubic $C = V_+(y^2 z - x^3 - x^2 z) \subseteq \mathbb{P}^2_k$ is integral of dimension $1$, with $p_a(C) = 1$ by Example P4.2.5, and its normalization is $\mathbb{P}^1_k$, with $p_a = 0$. The local ring at the node $P = [0 : 0 : 1]$ is not a discrete valuation ring (part 5 of Proposition P3.7.32), the ideal sheaf of $P$ is not invertible, and the Weil divisor $P$ is not Cartier. The induction step of the proof needs $\mathcal{O}_C(D)$ to be free of rank one at the added point, so the theorem as stated does not apply at the node. It does hold, with the same proof, for Cartier divisors supported on the smooth locus. The difference $p_a(C) - p_a(\mathbb{P}^1_k) = 1$ is the contribution of the node to the arithmetic genus.

### Proof

*Theorem P4.3.16.* Let $P$ be a closed point and $D$ a divisor. By part 2 of Proposition P3.8.28, $\mathcal{O}_C(D - P) \subseteq \mathcal{O}_C(D)$, with quotient $\mathcal{Q}$. The divisors $D$ and $D - P$ agree on $C \setminus \{P\}$, so $\mathcal{Q}$ is supported on the closed point $P$. Let $\pi$ be a uniformizer of the discrete valuation ring $\mathcal{O}_{C, P}$ and choose an open $U \ni P$ with $D|_U = \operatorname{div}(g)|_U$ and $\operatorname{div}(\pi)|_U = P$. Then $(D - P)|_U = \operatorname{div}(g/\pi)|_U$, and part 3 of Proposition P3.8.28 gives $\mathcal{O}_C(D)|_U = g^{-1} \mathcal{O}_U$ and $\mathcal{O}_C(D - P)|_U = \pi g^{-1} \mathcal{O}_U$. So
$$\mathcal{Q}_P = g^{-1} \mathcal{O}_{C, P} / g^{-1} \pi \mathcal{O}_{C, P} \cong \mathcal{O}_{C, P} / \pi \mathcal{O}_{C, P} = \kappa(P).$$
A sheaf supported on a closed point is the pushforward of its stalk from that point, so it is flasque and $H^p(C, \mathcal{Q}) = 0$ for $p \geq 1$, while $H^0(C, \mathcal{Q}) = \kappa(P)$ has dimension $[\kappa(P) : k]$. All sheaves involved are coherent, so their cohomology is finite-dimensional by Theorem P4.2.7, and by part 1 of Proposition P4.3.2,
$$\chi(\mathcal{O}_C(D)) = \chi(\mathcal{O}_C(D - P)) + [\kappa(P) : k].$$
Set $\phi(D) = \chi(\mathcal{O}_C(D)) - \deg D$. The identity says $\phi(D) = \phi(D - P)$ for every $D$ and $P$. Every divisor is obtained from $0$ by finitely many additions and removals of points, so $\phi(D) = \phi(0) = \chi(\mathcal{O}_C) = 1 - p_a(C)$. $\square$

*Corollary P4.3.17.* (1) By part 3 of Proposition P3.8.28, $\mathcal{O}_C(D) \cong \mathcal{O}_C(D - \operatorname{div}(f))$, so both have the same $\chi$, and Theorem P4.3.16 gives $\deg D = \deg (D - \operatorname{div} f)$. Since $\deg$ is additive on divisors, it descends to $\operatorname{Cl}(C) \cong \operatorname{Pic}(C)$, using part 4 of Proposition P3.8.28 for the independence of $D$.

(2) and (3). A nonzero $f \in H^0(C, \mathcal{O}_C(D))$ satisfies $E = D + \operatorname{div}(f) \geq 0$ by the definition of $\mathcal{O}_C(D)$. Then $\deg D = \deg E \geq 0$ by (1), which proves (2). If $\deg D = 0$, then $E$ is effective of degree $0$, hence $E = 0$ because every point has positive degree, and $D = -\operatorname{div}(f) \sim 0$.

(4) The space $C$ is Noetherian of dimension $1$, so $H^p(C, \mathcal{O}_C(D)) = 0$ for $p \geq 2$ by Grothendieck vanishing, Theorem P2.7.13. Hence $h^0 = \chi + h^1 \geq \chi = \deg D + 1 - p_a(C)$. If $\deg D \geq p_a(C)$, this is at least $1$, and a nonzero section $f$ gives the effective divisor $D + \operatorname{div}(f) \sim D$. $\square$

*Proposition P4.3.18.* By Example P3.9.16, $\mathcal{L} \cong \mathcal{O}_C(D)$ for a divisor $D$, and then $\mathcal{L}^{\otimes n} \cong \mathcal{O}_C(nD)$, since on an open where $D = \operatorname{div}(g)$ both sides are $g^{-n} \mathcal{O}$. Theorem P4.3.16 gives $\chi(\mathcal{L}^{\otimes n}) = n \deg D + 1 - p_a(C)$. For $\mathcal{L} = \mathcal{O}_C(1)$, part 1 of Theorem P4.3.4 identifies the left side with $P_C(n)$, whose leading coefficient is $\deg C$ by Definition P4.3.9 with $d = 1$. $\square$

### Exercises

1. (A) On $\mathbb{P}^1_k$, check Theorem P4.3.16 directly for $D = a \cdot 0 + b \cdot \infty$, with $0 = V_+(x_1)$, by computing a basis of $H^0(\mathcal{O}_C(D))$ inside $k(t)$, $t = x_1 / x_0$.
2. (A) For the conic of Example P4.3.20, compute $h^0(\mathcal{O}_C(nP_0))$ for all $n \in \mathbb{Z}$, and show that no divisor of odd degree exists on $C$.
3. (A) Let $C$ be a normal projective curve and $\mathcal{L}$ an invertible sheaf with $\deg \mathcal{L} > 0$. Show that $h^0(\mathcal{L}^{\otimes n}) \geq n \deg \mathcal{L} + 1 - p_a(C)$, and that $\mathcal{L}^{\otimes n}$ has a nonzero section for $n \geq p_a(C) / \deg \mathcal{L}$.
4. (B) Let $C$ be a normal projective curve over $k$ with $\Gamma(C, \mathcal{O}_C) = k$, and $P$ a $k$-rational point. Show that $h^0(\mathcal{O}_C(nP)) \leq n + 1$ for $n \geq 0$, using the sequences of the proof of Theorem P4.3.16, and show that $p_a(C) = h^1(C, \mathcal{O}_C) \geq 0$.
5. (B) Let $C$ be as in Exercise 4 with $p_a(C) = 0$ and $P$ a rational point. Show that $h^0(\mathcal{O}_C(P)) = 2$, and that a nonconstant $f \in H^0(\mathcal{O}_C(P))$ has a pole of order exactly one at $P$ and no other pole.
6. (C) In the setting of Exercise 5, show that the sections $1, f$ of $\mathcal{O}_C(P)$ define a morphism $C \to \mathbb{P}^1_k$ that is finite and birational, and conclude that $C \cong \mathbb{P}^1_k$. Compare with Example P4.3.20.

### Lean

Riemann-Roch for curves is not in Lean as stated. Mathlib has discrete valuation rings, the valuation of a Dedekind domain at a prime, and the class group of a Dedekind domain, which are the local and affine inputs of the proof. The handbook adds no `MinimalModel` node here.

### Notes and history

Riemann proved the inequality $\ell(D) \geq \deg D + 1 - g$ for compact Riemann surfaces in 1857, and his student Roch identified the defect in 1865 as the dimension of a space of differentials. The proof above, by induction on points with the Euler characteristic absorbing the defect, is Serre's from the 1955 paper on coherent sheaves, and Hartshorne IV.1 and Vakil 19.2 follow it. The literature state is theorem. In the minimal model program, Riemann-Roch on curves is the one-dimensional case of the asymptotic Riemann-Roch formula $\chi(\mathcal{O}_X(nD)) = D^{\dim X} n^{\dim X} / (\dim X)! + O(n^{\dim X - 1})$, which, with Kawamata-Viehweg vanishing, gives the non-vanishing theorem and through it the base point free theorem.
