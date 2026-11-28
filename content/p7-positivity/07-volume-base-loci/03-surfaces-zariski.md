---
title: Volumes and base loci on surfaces
nodes: []
sources: [Laz04, Nak04, Zar62, ELMNP06]
reads_with: [Laz04:2.3.E, Nak04:III.1]
requires: [P3.10, P5.5, P5.6, P5.8, P5.9, P7.1, P7.2, P7.3, P7.4, P7.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Volumes and base loci on surfaces

### Statement

Throughout, $S$ is a smooth projective surface over $k$, curves on $S$ are integral, and the Zariski decomposition of a pseudo-effective $\mathbb{Q}$-divisor $D = P + N$ is that of Theorem P5.8.24, with $P$ nef, $N$ effective, and the components $C_1, \dots, C_s$ of $N$ forming a negative definite configuration $\Sigma$ with $P \cdot C_j = 0$; both $P$ and $N$ have rational coefficients. For a negative definite configuration $\Sigma$ and an $\mathbb{R}$-divisor $D'$, $N_\Sigma(D')$ is the divisor of part 4 of Lemma P5.8.23. The pseudo-effective classes in the sense of Definition P5.8.22 are those of Definition P7.5.11, by part 3 of Proposition P7.4.15.

**Lemma P7.7.22 (fixed curves).** Let $\Sigma$ be a negative definite configuration and $D'$ an $\mathbb{R}$-divisor on $S$. Every effective $\mathbb{R}$-divisor $\Delta$ with $\Delta \equiv D'$ satisfies $\operatorname{mult}_C \Delta \geq \operatorname{mult}_C N_\Sigma(D')$ for every $C \in \Sigma$.

Lean: not in Lean as stated.

**Proposition P7.7.23 (volume and base loci on a surface).** Let $D$ be a pseudo-effective $\mathbb{Q}$-divisor on $S$ with Zariski decomposition $D = P + N$.

1. $\operatorname{vol}(D) = \operatorname{vol}(P) = P^2$.
2. $\mathbf{B}(D) = \operatorname{Supp} N \cup \mathbf{B}(P)$.
3. $\mathbf{B}_-(D) = \operatorname{Supp} N$.
4. $\operatorname{vol}(D) \geq D^2$, with equality if and only if $N = 0$, and $N = 0$ if and only if $D$ is nef.

Lean: not in Lean as stated.

**Definition P7.7.24 (asymptotic order of vanishing).** Let $X$ be a smooth projective variety, $\xi \in \operatorname{Big}(X)$ and $\Gamma \subseteq X$ a prime divisor. Put
$$\sigma_\Gamma(\xi) = \inf \{ \operatorname{mult}_\Gamma \Delta : \Delta \text{ an effective } \mathbb{R}\text{-divisor with } [\Delta] = \xi \},$$
a real number in $[0, \infty)$, and $N_\sigma(\xi) = \sum_\Gamma \sigma_\Gamma(\xi) \, \Gamma$.

The set over which the infimum runs is not empty: $\xi \in \operatorname{Eff}(X)$ by part 3 of Proposition P7.5.6, and $\operatorname{Eff}(X)$ is the convex cone spanned by the classes of effective Cartier divisors (Definition P7.4.13), so $\xi$ is the class of an effective $\mathbb{R}$-divisor. Nakayama, Chapter III (Nak04), shows that $\sigma_\Gamma(\xi) > 0$ for only finitely many $\Gamma$, so $N_\sigma(\xi)$ is an effective $\mathbb{R}$-divisor, and extends $\sigma_\Gamma$ to pseudo-effective classes by $\sigma_\Gamma(\xi) = \lim_{\varepsilon \to 0} \sigma_\Gamma(\xi + \varepsilon \alpha)$ with $\alpha$ ample; the decomposition $\xi = (\xi - N_\sigma(\xi)) + N_\sigma(\xi)$ is his *$\sigma$-decomposition*. On a surface it is the Zariski decomposition.

**Proposition P7.7.25 (the $\sigma$-decomposition of a surface).** Let $D$ be a big $\mathbb{Q}$-divisor on $S$ with Zariski decomposition $D = P + N$. Then $\sigma_\Gamma([D]) = \operatorname{mult}_\Gamma N$ for every prime divisor $\Gamma$, so $N_\sigma([D]) = N$.

Lean: not in Lean as stated.

### Proof in words

The negative part of a Zariski decomposition is rigid: every effective divisor numerically equivalent to $D$ contains it, because subtracting the part supported on the negative definite configuration leaves a divisor that meets the configuration nonnegatively, and the negativity lemma then forces the subtracted part to be at least $N$. So all sections of multiples of $D$ come from $P$, the volume of $D$ is the volume of the nef divisor $P$, which is $P^2$, and the stable base locus of $D$ is the support of $N$ together with that of $P$. A small ample perturbation of $D$ changes the negative part only slightly, so it stays supported on all of $\operatorname{Supp} N$, while $P$ plus an ample class is ample; this identifies the restricted base locus with $\operatorname{Supp} N$. Since $P \cdot N = 0$, $D^2 = P^2 + N^2$, and $N^2 < 0$ unless $N = 0$, so the volume exceeds the self-intersection exactly when $D$ is not nef.

The same rigidity bounds Nakayama's asymptotic order of vanishing from below by the coefficients of $N$. For the upper bound, a big nef $P$ is numerically an ample class plus an effective one, and a small part of that effective divisor, plus a general member of an ample multiple, realizes the coefficients of $N$ in the limit.

### Examples

**Example P7.7.26 (the plane blown up at a point).** Let $X = \operatorname{Bl}_p \mathbb{P}^2 = \mathbb{F}_1$, with $H$ the pullback of a line, the class $\ell$ of Example P5.8.27, and $E$ the exceptional curve. For $D = H + 2E$, Example P5.8.27 gives $P = H$, $N = 2E$, so Proposition P7.7.23 gives
$$\operatorname{vol}(H + 2E) = H^2 = 1, \qquad D^2 = -3,$$
in agreement with Example P7.7.11, and $\mathbf{B}(D) = \mathbf{B}_-(D) = E$, since $|H|$ is base point free. In general, for $D = xH - yE$ with $x > 0$:

1. if $0 < y < x$, $D$ is ample and all three loci are empty;
2. if $y = 0$, $\mathbf{B}(H) = \mathbf{B}_-(H) = \emptyset$ and $\mathbf{B}_+(H) = \operatorname{Null}(H) = E$, by Example P7.7.21;
3. if $y = x$, $D$ is nef and not big, $\mathbf{B}(D) = \mathbf{B}_-(D) = \emptyset$ and $\mathbf{B}_+(D) = X$;
4. if $y < 0$, $D \cdot E = y < 0$, the Zariski decomposition is $P = xH$, $N = -yE$, and $\mathbf{B}(D) = \mathbf{B}_-(D) = E$ by Proposition P7.7.23. For small $\varepsilon$, $D - \varepsilon(2H - E)$ is again of this type, so $\mathbf{B}_+(D) = E$ by part 2 of Proposition P7.7.15.

On the boundary ray of $E$, $D = bE$ with $b > 0$ has $P = 0$, $N = bE$, volume $0$, $\mathbf{B}(D) = \mathbf{B}_-(D) = E$ and $\mathbf{B}_+(D) = X$. On the surface $S_2$ of Example P5.8.28, the divisor $D = \tilde M + C_1 \equiv \ell - e_2$ of Example P5.8.29 has $P^2 = \frac12$ and $D^2 = 0$, so $\operatorname{vol}(D) = \frac12$, $h^0(mD)$ grows like $\frac14 m^2$, and $\mathbf{B}_-(D) = C_1$: the volume of an integral divisor need not be an integer, although it is rational on a surface.

**Example P7.7.27 (Hirzebruch surfaces).** Let $X = \mathbb{F}_n$, $n \geq 1$, with $C_-$, $C_+$, $F$ as in Proposition P7.4.19, and $D = aC_- + bF$ with $a, b \geq 0$ rational, the pseudo-effective cone by part 2 of that proposition. By Corollary P7.1.25, $D \cdot C_- = b - na$ and $D \cdot F = a$. If $b \geq na$, $D$ is nef and
$$\operatorname{vol}(aC_- + bF) = D^2 = a(2b - na).$$
If $0 \leq b < na$, $D \cdot C_- < 0$, so $\Theta = \{C_-\}$, and $(D - xC_-) \cdot C_- = b - na + nx = 0$ gives
$$N = \Big( a - \frac{b}{n} \Big) C_-, \qquad P = \frac{b}{n} C_- + bF \sim_\mathbb{Q} \frac{b}{n} C_+, \qquad \operatorname{vol}(D) = P^2 = \frac{b^2}{n}.$$
The two formulas agree on the ray $b = na$ of $C_+$, where both give $na^2$. Since $\mathcal{O}(C_+)$ is generated by global sections (proof of Proposition P7.2.24), $\mathbf{B}(P) = \emptyset$ for $b > 0$, and Proposition P7.7.23 gives $\mathbf{B}(D) = \mathbf{B}_-(D) = C_-$ when $0 < b < na$. For such $D$ and small $\varepsilon$, $D - \varepsilon(C_+ + F)$ satisfies the same inequalities, so $\mathbf{B}_+(D) = C_-$. On the ray of $C_+$, $\mathbf{B}(C_+) = \mathbf{B}_-(C_+) = \emptyset$, while $C_+ - \varepsilon(C_+ + F)$ lies in the chamber $b < na$, so $\mathbf{B}_+(C_+) = C_- = \operatorname{Null}(C_+)$, the curve contracted by $\varphi$ in part 3 of Proposition P7.4.19.

The anticanonical divisor is $-K \sim 2C_- + (n + 2)F$ by part 2 of Proposition P5.9.9, so $a = 2$, $b = n + 2$. For $n \leq 2$ it is nef and $\operatorname{vol}(-K) = K^2 = 8$. For $n \geq 3$, $b < na$, and
$$N = \frac{n - 2}{n} C_-, \qquad P \sim_\mathbb{Q} \frac{n + 2}{n} C_+, \qquad \operatorname{vol}(-K) = \frac{(n + 2)^2}{n} = 8 + \frac{(n - 2)^2}{n} > 8 = K^2.$$
Here $\mathbf{B}(-K) = \mathbf{B}_-(-K) = \mathbf{B}_+(-K) = C_-$.

**Example P7.7.28 (a negative part with two components).** Let $S_3$ be the plane blown up at three non-collinear points $p_1, p_2, p_3$, with $H$, $E_i$ as in Example P5.6.8 and $L_{ij} = H - E_i - E_j$ the strict transforms of the lines through $p_i$ and $p_j$; these six curves are the $(-1)$-curves of Proposition P7.4.21. Let
$$D = 4H - 3E_1 - 2E_2 - 2E_3 = L_{12} + L_{13} + (2H - E_1 - E_2 - E_3).$$
Then $D \cdot E_1 = 3$, $D \cdot E_2 = D \cdot E_3 = 2$, $D \cdot L_{23} = 0$ and $D \cdot L_{12} = D \cdot L_{13} = -1$. The curves $L_{12}$ and $L_{13}$ are disjoint, since $L_{12} \cdot L_{13} = 1 + E_1^2 = 0$, so $\Sigma = \{L_{12}, L_{13}\}$ has matrix $-I$ and is negative definite, and $N_\Sigma(D) = L_{12} + L_{13}$. The remainder $P = 2H - E_1 - E_2 - E_3$ has $P \cdot E_i = 1$ and $P \cdot L_{ij} = 0$, so it is nef by Proposition P7.4.21, and
$$P = 2H - E_1 - E_2 - E_3, \qquad N = L_{12} + L_{13}, \qquad P^2 = 1, \qquad N^2 = -2, \qquad D^2 = -1.$$
So $\operatorname{vol}(D) = 1$. The linear system $|P|$ of conics through the three points is base point free: it contains $L_{12} + M_3$ and $L_{13} + M_2$, for $M_i$ the strict transform of a line through $p_i$ alone, of class $H - E_i$; since $L_{12} \cdot L_{13} = L_{12} \cdot M_2 = M_3 \cdot L_{13} = 0$, the two members meet only at the point $M_2 \cap M_3$, which moves with the lines. So Proposition P7.7.23 gives $\mathbf{B}(D) = \mathbf{B}_-(D) = L_{12} \cup L_{13}$. Exercise 5 shows that $\mathbf{B}_+(D) = L_{12} \cup L_{13} \cup L_{23}$: the curve $L_{23}$ is not a base curve of any multiple of $D$, but it is one of every small negative perturbation.

### Proof

*Lemma P7.7.22.* Write $\Sigma = \{C_1, \dots, C_s\}$ and $\Delta = \Delta' + \sum_i g_i C_i$ with $g_i = \operatorname{mult}_{C_i} \Delta \geq 0$ and $\Delta'$ effective with no $C_i$ in its support. Then $\Delta' \cdot C_j \geq 0$ for every $j$, since distinct curves meet nonnegatively (Proposition P5.5.5). Put $Y = \sum_i g_i C_i - N_\Sigma(D')$, supported on $\Sigma$. Since $(D' - N_\Sigma(D')) \cdot C_j = 0$,
$$Y \cdot C_j = (D' - \Delta') \cdot C_j - N_\Sigma(D') \cdot C_j = -\Delta' \cdot C_j \leq 0$$
for every $j$. By the uniqueness in part 4 of Lemma P5.8.23, $N_\Sigma(Y) = Y$, and by the effectivity statement there, $Y$ is effective. So $g_i \geq \operatorname{mult}_{C_i} N_\Sigma(D')$.

*Proposition P7.7.23.* Choose $a \geq 1$ with $aD$, $aP$ and $aN$ integral. By the uniqueness in Theorem P5.8.24, the Zariski decomposition of $maD$ is $maP + maN$ for every $m \geq 1$, and $\lceil maN \rceil = maN$. Let $s_m$ be the canonical section of $\mathcal{O}_S(maN)$. By Corollary P5.8.26, multiplication by $s_m$ is an isomorphism
$$H^0(S, \mathcal{O}_S(maP)) \cong H^0(S, \mathcal{O}_S(maD)). \tag{*}$$

Part 1. By (*), $h^0(maD) = h^0(maP)$ for all $m$, so $\operatorname{vol}(aD) = \operatorname{vol}(aP)$, and part 2 of Proposition P7.7.3 gives $\operatorname{vol}(D) = \operatorname{vol}(P)$. Since $P$ is nef, $\operatorname{vol}(P) = P^2$ by Theorem P7.7.7.

Part 2. By (*), every section of $\mathcal{O}_S(maD)$ is $s_m t$ with $t$ a section of $\mathcal{O}_S(maP)$, so $\operatorname{Bs}|maD| = \operatorname{Supp} N \cup \operatorname{Bs}|maP|$, both sides being $S$ if $H^0(maP) = 0$. For $m$ divisible enough, part 4 of Proposition P3.10.2 identifies the two base loci with $\mathbf{B}(D)$ and $\mathbf{B}(P)$.

Part 3. Let $A$ be an ample $\mathbb{Q}$-divisor. Since $P$ is nef, $P + A$ is ample by part 3 of Theorem P7.3.12, so $\mathbf{B}(P + A) = \emptyset$ by part 2 of Lemma P7.7.13 applied to the divisor $0$. Part 3 of Lemma P7.7.13 applied to $D + A = (P + A) + N$ gives $\mathbf{B}(D + A) \subseteq \operatorname{Supp} N$, so $\mathbf{B}_-(D) \subseteq \operatorname{Supp} N$. Conversely, assume $N \neq 0$ and let $\Sigma$ be the configuration of its components. Since $(D - N) \cdot C_j = P \cdot C_j = 0$, uniqueness gives $N_\Sigma(D) = N$. Since $(-A) \cdot C_j < 0$ for every $j$, part 4 of Lemma P5.8.23 shows that $w = N_\Sigma(-A)$ is effective, and by linearity $N_\Sigma(D + \varepsilon A) = N - \varepsilon w$. For rational $\varepsilon > 0$ so small that every coefficient of $N - \varepsilon w$ on $C_j$ is positive, Lemma P7.7.22 applied to $m(D + \varepsilon A)$ shows that every member of $|m(D + \varepsilon A)|$ contains every $C_j$. So $\operatorname{Supp} N \subseteq \mathbf{B}(D + \varepsilon A) \subseteq \mathbf{B}_-(D)$.

Part 4. By Theorem P5.8.24, $D^2 = P^2 + N^2$. The configuration of components of $N$ is negative definite, so $N^2 \leq 0$ with equality only if $N = 0$, and $\operatorname{vol}(D) = P^2 = D^2 - N^2 \geq D^2$ by part 1, with equality if and only if $N = 0$. If $N = 0$, $D = P$ is nef. If $D$ is nef, $D = D + 0$ is a Zariski decomposition, and uniqueness gives $N = 0$.

*Proposition P7.7.25.* By part 1 of Proposition P7.7.23 and part 1 of Proposition P7.7.3, $\operatorname{vol}(P) = \operatorname{vol}(D) > 0$, so $P$ is big. Lower bound. Let $\Delta$ be an effective $\mathbb{R}$-divisor with $[\Delta] = [D]$. If $N \neq 0$, $N_\Sigma(D) = N$ as in the proof of part 3 of Proposition P7.7.23, and Lemma P7.7.22 gives $\operatorname{mult}_{C_j} \Delta \geq \operatorname{mult}_{C_j} N$. So $\sigma_\Gamma([D]) \geq \operatorname{mult}_\Gamma N$ for every $\Gamma$, trivially when $\Gamma$ is not a component of $N$. Upper bound. Choose $a \geq 1$ with $aP$ integral. By part 1 of Corollary P7.5.4, applied to $\mathcal{O}_S(aP)$, there are $q \geq 1$ and an effective Cartier divisor $G$ with $qaP - G$ ample; put $E = G/(qa)$ and $A = P - E$, an ample $\mathbb{Q}$-divisor. For rational $0 < t < 1$, $(1 - t) P + tA$ is ample by part 3 of Theorem P7.3.12, so for $m$ divisible enough $m((1 - t)P + tA)$ is a very ample Cartier divisor, and it has a member $G_t$ containing none of the finitely many curves $\Gamma$, $C_1, \dots, C_s$ and the components of $E$, since a hyperplane section can avoid finitely many given points. Then
$$\Delta_t = N + \tfrac1m G_t + tE \sim_\mathbb{Q} N + (1 - t) P + tA + tE = N + P = D$$
is effective with $\operatorname{mult}_\Gamma \Delta_t = \operatorname{mult}_\Gamma N + t \operatorname{mult}_\Gamma E$. Letting $t \to 0$ gives $\sigma_\Gamma([D]) \leq \operatorname{mult}_\Gamma N$.

### Exercises

1. (A) On $\mathbb{F}_n$ complete the table of Example P7.7.27: compute $\operatorname{vol}$, $\mathbf{B}$, $\mathbf{B}_-$ and $\mathbf{B}_+$ on the two boundary rays of $\overline{\operatorname{Eff}}(\mathbb{F}_n)$ and in the interior of $\operatorname{Nef}(\mathbb{F}_n)$.
2. (A) Show that the volume on $\mathbb{F}_n$ is continuously differentiable on $\operatorname{Big}(\mathbb{F}_n)$ but has no continuous second derivatives across the ray of $C_+$.
3. (B) On the surface $S_2$ of Example P7.7.26, show that $|2P| = |2\ell - e_1 - e_2|$ is base point free, using its members $\tilde L_0 + \tilde L$ and $\tilde M + \tilde M' + C_1$ with $\tilde L$ the pullback of a line not through $p_1$, and deduce $\mathbf{B}(D) = \mathbf{B}_-(D) = C_1$.
4. (B) Let $D$ be an effective $\mathbb{Q}$-divisor on $S$ with Zariski decomposition $P + N$. Using Proposition P5.8.25 and part 1 of Lemma P5.8.23, show that $\operatorname{vol}(D) = \max \{ P'^2 : P' \text{ a nef } \mathbb{Q}\text{-divisor with } P' \leq D \}$.
5. (C) Let $D$ be a big $\mathbb{Q}$-divisor on $S$ with Zariski decomposition $P + N$. Show that $\mathbf{B}_+(D)$ is the union of the curves $C$ with $P \cdot C = 0$, and deduce $\mathbf{B}_+(D) = L_{12} \cup L_{13} \cup L_{23}$ in Example P7.7.28. (Exercise 6 of Section 7.2 is the case $N = 0$.)
6. (C) Show that $\xi \mapsto P(\xi)$, the positive part of the Zariski decomposition of $\mathbb{R}$-divisor classes of Theorem P5.8.24, is continuous on $\operatorname{Big}(S)$, that $\operatorname{vol}(\xi) = P(\xi)^2$ for every real big class, and that on $\operatorname{Big}(S_3)$ the volume is given by finitely many quadratic polynomials, one on each region where the set of components of the negative part is constant.

### Lean

The project library defines `MinimalModel.IsNef`, `MinimalModel.IsBig` and `MinimalModel.IsPseudoEffective` for $\mathbb{R}$-divisors, and `MinimalModel.effCone` and `MinimalModel.nefCone`. It has no Zariski decomposition, no volume, no base loci and no $\sigma$-decomposition. Mathlib has no intersection theory on surfaces. The handbook adds no `MinimalModel` node here.

### Notes and history

Zariski introduced the decomposition in his study of the Riemann-Roch problem for high multiples of an effective divisor on a surface (Zar62), and Corollary P5.8.26 and part 1 of Proposition P7.7.23 are his application of it: the dimension $h^0(mD)$ is governed by the nef part, and grows like $\frac12 P^2 m^2$. Fujita extended the decomposition to pseudo-effective $\mathbb{R}$-divisors. Lazarsfeld, Section 2.3.E (Laz04), presents it together with the volume, and the identification of the negative part with the restricted base locus is in the work of Ein, Lazarsfeld, Mustaţă, Nakamaye and Popa (ELMNP06). The literature state is theorem. In higher dimension Nakayama's $\sigma$-decomposition (Nak04) is the replacement, but its positive part need not be nef: Cutkosky gave a big line bundle on a smooth projective threefold whose volume is irrational, which rules out a decomposition with rational nef positive part on any birational model, and Nakayama (Nak04) gave examples where the positive part of the $\sigma$-decomposition is not nef on any birational model. On a surface, Bauer, Küronya and Szemberg showed that the big cone has a locally finite decomposition into chambers on which the support of the negative part is constant and the volume is a quadratic polynomial; Exercise 6 is a case of it.
