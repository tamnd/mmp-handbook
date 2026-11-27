---
title: The Zariski decomposition
nodes: []
sources: [Laz04, KM98, Bea96, Har77]
reads_with: [Laz04:2.3.E, KM98:ch1]
requires: [P5.5, P5.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Zariski decomposition

### Statement

The *real Néron-Severi space* of $S$ is $N^1(S)_{\mathbb{R}} = \operatorname{Num}(S) \otimes \mathbb{R}$, with $\operatorname{Num}(S)$ as in Definition P5.5.7. It is a finite dimensional real vector space, of dimension the Picard number $\rho = \rho(S)$, by the theorem of Néron and Severi that $\operatorname{Num}(S)$ is a finitely generated free abelian group (Hartshorne, Remark V.1.9.1; Lazarsfeld, Proposition 1.1.16). The intersection pairing induces a nondegenerate symmetric bilinear form on it. Every $\mathbb{R}$-divisor $D$ has a class in $N^1(S)_{\mathbb{R}}$, and $D \equiv D'$ means that the classes agree, that is, $D \cdot C = D' \cdot C$ for every integral curve $C$.

**Definition P5.8.22 (nef and pseudoeffective classes).** A class or $\mathbb{R}$-divisor $D$ is *nef* if $D \cdot C \geq 0$ for every integral curve $C$ on $S$. It is *pseudoeffective* if its class lies in the closure $\overline{\operatorname{NE}}(S)$ of the convex cone in $N^1(S)_{\mathbb{R}}$ spanned by the classes of integral curves. The classes of effective $\mathbb{R}$-divisors are exactly the elements of that convex cone, so $D$ is pseudoeffective if and only if it is a limit of classes of effective $\mathbb{R}$-divisors.

**Lemma P5.8.23 (the tools).**

1. If $D$ is pseudoeffective and $P$ is nef, then $D \cdot P \geq 0$.
2. The classes of the curves of a negative definite configuration are linearly independent in $N^1(S)_{\mathbb{R}}$. In particular a negative definite configuration has at most $\rho$ curves.
3. Let $D$ be pseudoeffective and $\Sigma$ a negative definite configuration, possibly empty, with $D \cdot C = 0$ for every $C \in \Sigma$. Then the set $\Theta$ of integral curves $C$ with $D \cdot C < 0$ is finite, and $\Sigma \cup \Theta$ is a negative definite configuration.
4. Let $\Sigma$ be a negative definite configuration and $D$ an $\mathbb{R}$-divisor. There is a unique $\mathbb{R}$-divisor $N_\Sigma(D)$ supported on $\Sigma$ with $(D - N_\Sigma(D)) \cdot C = 0$ for every $C \in \Sigma$. It depends linearly on the class of $D$, it is effective if $D \cdot C \leq 0$ for every $C \in \Sigma$, and $D - N_\Sigma(D)$ is pseudoeffective if $D$ is.

Lean: not in Lean as stated.

**Theorem P5.8.24 (Zariski decomposition).** Let $D$ be a pseudoeffective $\mathbb{R}$-divisor on $S$. There are a nef $\mathbb{R}$-divisor $P$ and an effective $\mathbb{R}$-divisor $N$ with
$$D = P + N,$$
such that $N = 0$ or the components of $N$ form a negative definite configuration, and $P \cdot C = 0$ for every component $C$ of $N$. The divisor $N$ is unique, and it depends only on the class of $D$. If $D$ has rational coefficients, so do $P$ and $N$. In all cases $P \cdot N = 0$ and $D^2 = P^2 + N^2$.

Lean: not in Lean as stated.

The divisors $P$ and $N$ are the *positive part* and the *negative part* of $D$. Zariski's algorithm in the proof constructs $N$ in at most $\rho$ steps.

**Proposition P5.8.25 (the positive part is the largest nef subdivisor).** Let $D$ be an effective $\mathbb{R}$-divisor with Zariski decomposition $D = P + N$. Then $N \leq D$, so $P$ is effective, and every nef $\mathbb{R}$-divisor $P'$ with $P' \leq D$ satisfies $P' \leq P$.

Lean: not in Lean as stated.

**Corollary P5.8.26 (the negative part is fixed).** Let $D$ be a pseudoeffective divisor on $S$ with Zariski decomposition $D = P + N$ and $n \geq 1$. Every member $G \in |nD|$ satisfies $G \geq \lceil nN \rceil$, where $\lceil \cdot \rceil$ rounds every coefficient up, and the inclusion $\mathcal{O}_S(nD - \lceil nN \rceil) \subseteq \mathcal{O}_S(nD)$ induces an isomorphism
$$H^0(S, \mathcal{O}_S(nD - \lceil nN \rceil)) \cong H^0(S, \mathcal{O}_S(nD)).$$

Lean: not in Lean as stated.

### Proof in words

A pseudoeffective divisor fails to be nef only along finitely many curves, and these curves together with the curves already removed form a negative definite configuration: otherwise Lemma P5.8.1 would produce a nef divisor supported on them with negative intersection with $D$. On a negative definite configuration one can subtract from $D$ the unique combination of the curves that makes the rest orthogonal to them, and the negativity lemma says that the subtracted divisor is effective when $D$ is negative on the configuration. Zariski's algorithm repeats this: subtract, look for the curves on which the remainder is still negative, add them to the configuration and subtract again. The configuration grows at each step and has at most $\rho$ curves, so the algorithm stops at a nef remainder.

Uniqueness and maximality come from one computation. If two decompositions differ, the part $A$ of the difference supported on the negative part of one of them has $A^2 \geq 0$, and negative definiteness forces $A = 0$. For an effective divisor, comparing with the nef subdivisor $0$ shows that the negative part is a subdivisor, and comparing with any nef subdivisor shows that the positive part is the largest. Applied to the members of $|nD|$, this says that every one of them contains $nN$, so the negative part carries no sections.

### Examples

**Example P5.8.27 (one curve).** On $\tilde S = \operatorname{Bl}_p \mathbb{P}^2$, with $\ell$ the pullback of a line and $E$ the exceptional curve, let $D = \ell + 2E$. By Example P5.6.7 every integral curve other than $E$ has class $a \ell - b E$ with $a \geq 1$ and $0 \leq b \leq a$, and $D \cdot (a\ell - bE) = a + 2b > 0$, while $D \cdot E = -2$. So $\Theta = \{E\}$ in the first step, $N_{\{E\}}(D) = 2E$ because $(D - 2E) \cdot E = 0$, and $D - 2E = \ell$ is nef. The Zariski decomposition is
$$P = \ell, \qquad N = 2E, \qquad D^2 = -3 = 1 + 4E^2 = P^2 + N^2.$$
By Corollary P5.8.26 and part 1 of Corollary P5.6.5, $h^0(\tilde S, nD) = h^0(\tilde S, n\ell) = h^0(\mathbb{P}^2, \mathcal{O}(n)) = \frac{(n + 1)(n + 2)}{2}$.

**Example P5.8.28 (two steps).** Let $S_2$ be the surface of Example P5.8.6 with $n = 1$: blow up $p_1 \in \mathbb{P}^2$, then a point $p_2 \in E_1$. Then $\operatorname{Pic}(S_2) = \mathbb{Z}\ell \oplus \mathbb{Z} e_1 \oplus \mathbb{Z} e_2$, and $C_1 = e_1 - e_2$, $C_2 = e_2$ are smooth rational curves with $C_1^2 = -2$, $C_2^2 = -1$, $C_1 \cdot C_2 = 1$. Every other integral curve $C$ is the strict transform of a plane curve of some degree $a \geq 1$, of class $a \ell - b_1 e_1 - b_2 e_2$ with $a \geq b_1 \geq b_2 \geq 0$ by Proposition P5.6.4, since $b_1$ is the multiplicity at $p_1$ and $b_2$ that of the strict transform at $p_2$, and $C \cdot C_1 = b_1 - b_2 \geq 0$, $C \cdot C_2 = b_2 \geq 0$.

Let $D = L + C_1 + C_2 \equiv \ell + e_1$, with $L$ the pullback of a line not through $p_1$. Then $D \cdot C_1 = -1$, $D \cdot C_2 = 0$, and $D \cdot C = a + b_1 > 0$ for the other curves. The first step gives $\Theta_0 = \{C_1\}$ and $N_{\{C_1\}}(D) = \frac12 C_1$, since $(D - \frac12 C_1) \cdot C_1 = -1 + 1 = 0$. The remainder $P_1 = D - \frac12 C_1$ has
$$P_1 \cdot C_2 = 0 - \tfrac12 = -\tfrac12 < 0, \qquad P_1 \cdot C = a + b_1 - \tfrac12 (b_1 - b_2) > 0,$$
so it is not nef, and $\Theta_1 = \{C_2\}$. The configuration $\Sigma_2 = \{C_1, C_2\}$ has matrix $\left(\begin{smallmatrix} -2 & 1 \\ 1 & -1 \end{smallmatrix}\right)$, with determinant $1$ and trace $-3$, so it is negative definite. Solving $(P_1 - x C_1 - y C_2) \cdot C_1 = 2x - y = 0$ and $(P_1 - x C_1 - y C_2) \cdot C_2 = -\frac12 - x + y = 0$ gives $x = \frac12$, $y = 1$. So
$$N = \tfrac12 C_1 + \tfrac12 C_1 + C_2 = C_1 + C_2 = e_1, \qquad P = D - N = L,$$
and $P = L$ is nef with $P \cdot C_1 = P \cdot C_2 = 0$. The answer is integral although the first step was not, and the second step was needed: the curve $C_2$ only became negative after $\frac12 C_1$ was removed. As a check, $D^2 = 1 - 1 = 0 = P^2 + N^2$.

**Example P5.8.29 (a fractional negative part).** On the same surface $S_2$, let $M$ be a line through $p_1$ whose direction at $p_1$ is not $p_2$. By Proposition P5.6.4 its strict transform $\tilde M$ has class $\ell - e_1$, with $\tilde M^2 = 0$, $\tilde M \cdot C_1 = 1$, $\tilde M \cdot C_2 = 0$. Let $D = \tilde M + C_1 \equiv \ell - e_2$. Then $D \cdot C_1 = -1$, $D \cdot C_2 = 1$, $D \cdot \tilde M = 1$, and $D \cdot C = a - b_2 \geq 0$ for every other integral curve $C$, so $\Theta_0 = \{C_1\}$ and $N_{\{C_1\}}(D) = \frac12 C_1$. The remainder $P = \tilde M + \frac12 C_1$ has $P \cdot C_2 = \frac12$, $P \cdot \tilde M = \frac12$ and $P \cdot C = a - \frac12(b_1 + b_2) \geq 0$ for the other curves, so it is nef, and
$$P = \tilde M + \tfrac12 C_1, \qquad N = \tfrac12 C_1, \qquad P^2 = \tfrac12, \qquad N^2 = -\tfrac12, \qquad D^2 = 0.$$
By part 2 of Corollary P5.6.5, applied to the blow-up $S_2 \to S_1$ of $p_2$ and to the members of $|\ell|$ on $S_1$ through $p_2$, the members of $|D| = |\ell - e_2|$ are the divisors $\tilde M' + C_1$ for the lines $M'$ through $p_1$ with direction other than $p_2$, together with $\tilde L_0 + C_1 + C_2$ for the line $L_0$ through $p_1$ with direction $p_2$, whose strict transform has class $\ell - e_1 - e_2$. Every member contains $C_1 = \lceil N \rceil$, as Corollary P5.8.26 says, and every member of $|nD|$ contains $\lceil n/2 \rceil C_1$. The negative part is not integral, and $nN$ is integral only for even $n$.

### Proof

*Lemma P5.8.23.* (1) The linear form $x \mapsto x \cdot P$ is continuous and nonnegative on the classes of integral curves, hence on the closed convex cone they span.

(2) If $\sum_i x_i C_i \equiv 0$, then $x^T M x = \left(\sum_i x_i C_i\right)^2 = 0$, so $x = 0$ by negative definiteness.

(3) Let $\Theta' \subseteq \Theta$ be finite and $\Sigma' = \Sigma \cup \Theta'$, a configuration because $\Sigma \cap \Theta = \emptyset$. Suppose $\Sigma'$ is not negative definite. Part 2 of Lemma P5.8.1 gives an effective $\mathbb{R}$-divisor $F = \sum_{C \in \Sigma'} y_C C \neq 0$ with $F \cdot C \geq 0$ for every $C \in \Sigma'$. For an integral curve $C \notin \Sigma'$, $F \cdot C \geq 0$ because $F$ is effective without $C$ in its support. So $F$ is nef, and $D \cdot F \geq 0$ by part 1. But
$$D \cdot F = \sum_{C \in \Sigma} y_C \, D \cdot C + \sum_{C \in \Theta'} y_C \, D \cdot C = \sum_{C \in \Theta'} y_C \, D \cdot C \leq 0,$$
with equality only if $y_C = 0$ for every $C \in \Theta'$. Then $F$ is supported on $\Sigma$, and $F^2 = \sum_{C \in \Sigma} y_C \, F \cdot C \geq 0$ contradicts the negative definiteness of $\Sigma$. So every such $\Sigma'$ is negative definite, has at most $\rho$ curves by part 2, and $\Theta$ is finite with $\Sigma \cup \Theta$ negative definite.

(4) A divisor $\sum_{C \in \Sigma} x_C C$ has the property if and only if $M x = (D \cdot C)_{C \in \Sigma}$, which has exactly one solution since $M$ is invertible, depending linearly on the numbers $D \cdot C$. If $D \cdot C \leq 0$ for $C \in \Sigma$, then $N_\Sigma(D) \cdot C = D \cdot C \leq 0$ for $C \in \Sigma$, and $N_\Sigma(D) \geq 0$ by Theorem P5.8.2. For the last statement, let $\pi(D) = D - N_\Sigma(D)$, a linear and continuous map on $N^1(S)_{\mathbb{R}}$. Let $D$ be effective and write $D = A + D'$ with $A$ supported on $\Sigma$ and $D' \geq 0$ without components in $\Sigma$. Then $N_\Sigma(A) = A$ by uniqueness, so $\pi(D) = \pi(D')$. Since $D' \cdot C \geq 0$ for $C \in \Sigma$, the divisor $-N_\Sigma(D')$ satisfies the hypothesis of Theorem P5.8.2, so $N_\Sigma(D') \leq 0$ and $\pi(D) = D' - N_\Sigma(D') \geq D' \geq 0$. So $\pi$ maps the cone of classes of effective $\mathbb{R}$-divisors into itself, and by continuity it maps $\overline{\operatorname{NE}}(S)$ into itself. $\square$

*Theorem P5.8.24.* *Existence.* Put $\Sigma_0 = \emptyset$, $N_0 = 0$ and $P_0 = D$. Suppose $\Sigma_k$ is a negative definite configuration, $N_k \geq 0$ is supported on $\Sigma_k$, and $P_k = D - N_k$ is pseudoeffective with $P_k \cdot C = 0$ for every $C \in \Sigma_k$. Let $\Theta_k$ be the set of integral curves $C$ with $P_k \cdot C < 0$. If $\Theta_k = \emptyset$, stop: $P = P_k$ is nef and $N = N_k$. Otherwise $\Sigma_{k+1} = \Sigma_k \cup \Theta_k$ is a negative definite configuration by part 3 of Lemma P5.8.23, and $P_k \cdot C \leq 0$ for every $C \in \Sigma_{k+1}$. Put
$$N_{k+1} = N_k + N_{\Sigma_{k+1}}(P_k), \qquad P_{k+1} = P_k - N_{\Sigma_{k+1}}(P_k) = D - N_{k+1}.$$
By part 4 of Lemma P5.8.23, $N_{\Sigma_{k+1}}(P_k) \geq 0$, so $N_{k+1} \geq 0$ is supported on $\Sigma_{k+1}$, $P_{k+1}$ is pseudoeffective, and $P_{k+1} \cdot C = 0$ for $C \in \Sigma_{k+1}$. The configurations $\Sigma_k$ strictly increase and have at most $\rho$ curves by part 2 of Lemma P5.8.23, so the process stops after at most $\rho$ steps. At the end, the support of $N$ is contained in the negative definite configuration $\Sigma_k$, so it is negative definite if nonempty, since a principal submatrix of a negative definite matrix is negative definite, and $P \cdot C = 0$ for all $C \in \Sigma_k$.

*Uniqueness.* Let $D = P + N = P' + N'$ be two decompositions with the stated properties, and write $N - N' = A - B$ with $A, B \geq 0$ without common components. Then $\operatorname{Supp} A \subseteq \operatorname{Supp} N$, and $A - B = P' - P$. So
$$A^2 = A \cdot (A - B) + A \cdot B = A \cdot P' - A \cdot P + A \cdot B.$$
Here $A \cdot P = 0$ because $P \cdot C = 0$ for the components $C$ of $N$, $A \cdot P' \geq 0$ because $P'$ is nef and $A$ effective, and $A \cdot B \geq 0$ because $A$ and $B$ have no common components. So $A^2 \geq 0$, and $A = 0$ because it is supported on the negative definite configuration $\operatorname{Supp} N$. By symmetry $B = 0$, and $N = N'$. If $D \equiv D'$, the decomposition $D' = (D' - N) + N$ has the same properties, because they only involve intersection numbers of $D' - N \equiv P$, so $N$ depends only on the class of $D$.

*Rationality.* If $D$ has rational coefficients, then at each step $N_{\Sigma_{k+1}}(P_k)$ solves a linear system with integer matrix and rational right side, so it has rational coefficients, and by induction so do $N$ and $P$. Finally $P \cdot N = \sum_C n_C \, P \cdot C = 0$ and $D^2 = P^2 + 2 P \cdot N + N^2 = P^2 + N^2$. $\square$

*Proposition P5.8.25.* Let $P'$ be a nef $\mathbb{R}$-divisor with $N' = D - P' \geq 0$. Write $N - N' = A - B$ with $A, B \geq 0$ without common components, so $\operatorname{Supp} A \subseteq \operatorname{Supp} N$ and $A - B = P' - P$. The computation in the proof of uniqueness gives $A^2 = A \cdot P' - A \cdot P + A \cdot B \geq 0$, which uses only that $P'$ is nef and $N'$ effective, so $A = 0$ and $N \leq N'$, that is, $P' = D - N' \leq D - N = P$. For $P' = 0$, which is nef with $P' \leq D$, this gives $N \leq D$ and $P \geq 0$. $\square$

*Corollary P5.8.26.* By Theorem P5.8.24 the decomposition of $nD$ is $nP + nN$: these satisfy the conditions, and the negative part is unique. A member $G \in |nD|$ is an effective divisor with $G \equiv nD$, so by Theorem P5.8.24 its negative part is $nN$, and Proposition P5.8.25 gives $G \geq nN$. Since $G$ has integer coefficients, $G \geq \lceil nN \rceil$. So every nonzero section $s$ of $\mathcal{O}_S(nD)$ has $\operatorname{div}(s) - \lceil nN \rceil \geq 0$, that is, $s$ is a section of the subsheaf $\mathcal{O}_S(nD - \lceil nN \rceil)$. The induced map on $H^0$ is injective because the sheaves are subsheaves of the constant sheaf of rational functions, and surjective by what was just shown. $\square$

### Exercises

1. (A) On $\operatorname{Bl}_p \mathbb{P}^2$, show that $\overline{\operatorname{NE}}$ is spanned by $E$ and $\ell - E$ and that the nef cone is spanned by $\ell$ and $\ell - E$. For $D = a\ell + bE$ pseudoeffective, show that $N = \max(b, 0) E$.
2. (A) Check $P \cdot N = 0$ and $D^2 = P^2 + N^2$ in Examples P5.8.27, P5.8.28 and P5.8.29, and show that $N^2 < 0$ whenever $N \neq 0$.
3. (A) Show that the Zariski decomposition of $D + F$, for $F$ nef with $F \cdot C = 0$ for every component $C$ of $N$, is $(P + F) + N$, and that the decomposition of $cD$ for $c > 0$ is $cP + cN$.
4. (B) Let $D$ be pseudoeffective. Show that $P^2 \geq D^2$, and that $P \equiv 0$ if and only if $D$ is numerically equivalent to an effective $\mathbb{R}$-divisor whose support is negative definite.
5. (B) On the surface $S_2$ of Example P5.8.28, let $D = L + t C_1 + s C_2$ with $s, t \geq 0$ not both zero. Show that the Zariski decomposition is $P = L$, $N = t C_1 + s C_2$, by checking that a nef divisor of the form $L + t' C_1 + s' C_2$ with $t', s' \geq 0$ must have $t' = s' = 0$, and using Proposition P5.8.25.
6. (C) (*Bauer's construction.*) Let $D$ be an effective $\mathbb{R}$-divisor. Show that the coefficientwise maximum of two nef $\mathbb{R}$-divisors $P_1, P_2 \leq D$ is nef, and deduce that among the nef $\mathbb{R}$-divisors $P'$ with $0 \leq P' \leq D$ there is a largest one $P$. Show without Zariski's algorithm that $D - P$ has negative definite support, or is zero, and that $P$ is orthogonal to its components, so that $D = P + (D - P)$ is the Zariski decomposition.

### Lean

Mathlib has convex cones (`ConvexCone`) and their closures in finite dimensional real vector spaces, which is the setting of Definition P5.8.22, but no nef or pseudoeffective cone of a surface and no Zariski decomposition. The handbook adds no `MinimalModel` node here.

### Notes and history

Zariski introduced the decomposition in 1962 for effective divisors, in *The theorem of Riemann-Roch for high multiples of an effective divisor on an algebraic surface*, Ann. of Math. 76 (1962), to study $h^0(nD)$ for large $n$ and the finite generation of the section ring $\bigoplus_n H^0(S, nD)$. Fujita extended it to pseudoeffective classes in 1979 (*On Zariski problem*, Proc. Japan Acad. 55), and Bauer gave in 2009 the short proof through the largest nef subdivisor of Exercise 6 (*A simple proof for the existence of Zariski decompositions on surfaces*, J. Algebraic Geom. 18). The presentation above follows Lazarsfeld, Section 2.3.E (Laz04). Bauer, Küronya and Szemberg showed in 2004 that the big cone of a surface is cut by the negative parts into locally finite chambers on which the volume is a quadratic form. The literature state is theorem. In the minimal model program the Zariski decomposition appears in the proof that the canonical ring of a smooth projective surface is finitely generated, in Fujita's theory of noncomplete and log surfaces, and as the model for Nakayama's $\sigma$-decomposition in higher dimension, where the negative part is still defined but the positive part need not be nef. In dimension $3$ and higher, Cutkosky's examples show that a big divisor need not have a Zariski decomposition with nef positive part, even after blowing up, which is one reason the higher dimensional program works with minimal models instead.
