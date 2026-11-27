---
title: The Euler sequence
nodes: []
sources: [Vak25, Har77, Stacks]
reads_with: [Vak25:ch21, Har77:II.8]
requires: [P1.12, P3.6, P3.8, P3.9]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Euler sequence

### Statement

Let $A$ be a ring, $S = A[x_0, \dots, x_n]$ with $n \geq 1$, and $P = \mathbb{P}^n_A = \operatorname{Proj} S$. Write $\Omega_P = \Omega_{P/A}$. On $D_+(x_j) = \operatorname{Spec} A[x_0/x_j, \dots, x_n/x_j]$ the sheaf $\Omega_P$ is free with basis the $d(x_i/x_j)$, $i \neq j$, by part 5 of Theorem P3.12.2. Let $e_0, \dots, e_n$ be the standard basis of the graded module $S(-1)^{n+1}$, each $e_i$ of degree $1$, so that $\widetilde{S(-1)^{n+1}} = \mathcal{O}_P(-1)^{n+1}$ by Proposition P3.6.11. A section of $\mathcal{O}_P(-1)$ on $D_+(x_j)$ is an element of degree $-1$ of $S_{x_j}$, such as $1/x_j$.

**Theorem P3.12.20 (the Euler sequence).** There is an exact sequence of $\mathcal{O}_P$-modules
$$
0 \longrightarrow \Omega_{P/A} \xrightarrow{\ \alpha\ } \mathcal{O}_P(-1)^{n+1} \xrightarrow{\ \beta\ } \mathcal{O}_P \longrightarrow 0 ,
$$
where $\beta(\sum_i g_i e_i) = \sum_i g_i x_i$ and, on $D_+(x_j)$,
$$
\alpha\big(d(x_i/x_j)\big) = \frac{x_j e_i - x_i e_j}{x_j^2} = \frac{1}{x_j}\, e_i - \frac{x_i}{x_j^2}\, e_j .
$$
Twisted by $\mathcal{O}_P(1)$, it is the sequence $0 \to \Omega_P(1) \to \mathcal{O}_P^{n+1} \to \mathcal{O}_P(1) \to 0$ of Exercise 5 of Section 6.4, for the projective bundle of the free sheaf of rank $n + 1$ over $\operatorname{Spec} A$.

Lean: not in Lean as stated.

**Lemma P3.12.21 (determinants in exact sequences).** Let $0 \to \mathcal{E}' \to \mathcal{E} \to \mathcal{E}'' \to 0$ be an exact sequence of locally free sheaves of ranks $a$, $a + b$ and $b$ on a scheme $X$. Then there is a natural isomorphism
$$
\det \mathcal{E}' \otimes \det \mathcal{E}'' \xrightarrow{\ \sim\ } \det \mathcal{E} , \qquad (e'_1 \wedge \dots \wedge e'_a) \otimes (e''_1 \wedge \dots \wedge e''_b) \mapsto e'_1 \wedge \dots \wedge e'_a \wedge \tilde e''_1 \wedge \dots \wedge \tilde e''_b ,
$$
where $\det \mathcal{F} = \bigwedge^{\operatorname{rank} \mathcal{F}} \mathcal{F}$ and $\tilde e''_j$ are local lifts of the $e''_j$ to $\mathcal{E}$.

Lean: Mathlib has the exterior powers `exteriorPower` with notation `⋀[R]^n M` (definition). The lemma is not in Lean as stated.

**Corollary P3.12.22 (the canonical sheaf of projective space).**

1. $\bigwedge^n \Omega_{P/A} \cong \mathcal{O}_P(-n - 1)$.
2. $\Gamma(P, \Omega_P(m)) = \ker\big(S_{m-1}^{n+1} \to S_m\big)$ for every $m$, the map being $(g_i) \mapsto \sum_i g_i x_i$. In particular $\Gamma(P, \Omega_P) = \Gamma(P, \Omega_P(1)) = 0$, and for $A = k$ a field, $\Gamma(P, \Omega_P(2))$ has dimension $\binom{n+1}{2}$, with basis the sections $x_j e_i - x_i e_j$, $i < j$, which Example P3.12.25 writes as the forms $x_j\,dx_i - x_i\,dx_j$.

Lean: not in Lean as stated.

**Proposition P3.12.23 (differentials of a product).** Let $X$ and $Y$ be schemes over $S$, $P = X \times_S Y$ with projections $p$ and $q$. Then the map
$$
p^* \Omega_{X/S} \oplus q^* \Omega_{Y/S} \longrightarrow \Omega_{P/S}
$$
given by the first sequences of Theorem P3.12.4 is an isomorphism. If $X$ and $Y$ are smooth over a field $k = S$ of pure dimensions $a$ and $b$, then $P$ is smooth of pure dimension $a + b$ and $\bigwedge^{a + b} \Omega_P \cong p^* \bigwedge^a \Omega_X \otimes q^* \bigwedge^b \Omega_Y$.

Lean: not in Lean as stated.

### Proof in words

On affine space $\mathbb{A}^{n+1}$ the differentials are free on $dx_0, \dots, dx_n$. A form on $\mathbb{P}^n$ pulls back to the punctured affine space as a form that is invariant under scaling and that vanishes on the Euler vector field $\sum_i x_i\,\partial/\partial x_i$, the direction of the scaling. Writing $\sum_i g_i\,dx_i$ for such a form, the condition is $\sum_i g_i x_i = 0$, and the coefficients $g_i$ have degree $-1$, as $dx_i$ has degree $1$. So the forms on $\mathbb{P}^n$ are the kernel of $\beta$, which is the Euler sequence. The chart computation makes this precise without the punctured affine space: the formula $d(x_i/x_j) = (x_j\,dx_i - x_i\,dx_j)/x_j^2$ is the quotient rule. The determinant of the sequence gives the canonical sheaf, since the determinant is multiplicative in exact sequences.

### Examples

**Example P3.12.24 (the Euler sequence on the line).** For $n = 1$, with $t = x_1/x_0$ on $D_+(x_0)$ and $s = x_0/x_1$ on $D_+(x_1)$, the map $\alpha$ sends $dt$ to $(x_0 e_1 - x_1 e_0)/x_0^2$ and $ds$ to $(x_1 e_0 - x_0 e_1)/x_1^2$. On the overlap $-t^{-2} \alpha(dt) = -(x_0^2/x_1^2)(x_0 e_1 - x_1 e_0)/x_0^2 = \alpha(ds)$, in agreement with $ds = -t^{-2}\,dt$. By Lemma P3.12.21, $\Omega_{\mathbb{P}^1} \otimes \mathcal{O} \cong \det \mathcal{O}(-1)^2 = \mathcal{O}(-2)$, which is Example P3.12.6 again.

**Example P3.12.25 (the forms of degree two).** Let $A = k$ be a field. By part 2 of Corollary P3.12.22, the global sections of $\Omega_{\mathbb{P}^n}(2)$ are the tuples $(g_i)$ of linear forms with $\sum_i g_i x_i = 0$. The forms $x_j e_i - x_i e_j$ for $i < j$ are in the kernel, and they span it: the map $S_1^{n+1} \to S_2$ is surjective, so its kernel has dimension $(n+1)^2 - \binom{n+2}{2} = \binom{n+1}{2}$, and the $x_j e_i - x_i e_j$ are linearly independent. On $D_+(x_j)$ the section $x_j e_i - x_i e_j$ is $\alpha(x_j^2\,d(x_i/x_j))$, the quotient rule written as $x_j^2\,d(x_i/x_j) = x_j\,dx_i - x_i\,dx_j$. For $n = 1$ this is the single section $x_0^2\,dt$ of $\Omega_{\mathbb{P}^1}(2) \cong \mathcal{O}$, which generates it.

**Example P3.12.26 (products of projective spaces).** Let $P = \mathbb{P}^n_k \times_k \mathbb{P}^m_k$ with projections $p$, $q$, and write $\mathcal{O}(a, b) = p^* \mathcal{O}(a) \otimes q^* \mathcal{O}(b)$. By Proposition P3.12.23 and Corollary P3.12.22,
$$
\Omega_P \cong p^* \Omega_{\mathbb{P}^n} \oplus q^* \Omega_{\mathbb{P}^m} , \qquad \bigwedge^{n+m} \Omega_P \cong \mathcal{O}(-n-1, -m-1) .
$$
For the smooth quadric surface $\mathbb{P}^1 \times \mathbb{P}^1$ the top forms are $\mathcal{O}(-2, -2)$. Under the Segre embedding as $V_+(x_0 x_3 - x_1 x_2) \subseteq \mathbb{P}^3$ the sheaf $\mathcal{O}(1, 1)$ is the restriction of $\mathcal{O}_{\mathbb{P}^3}(1)$, so the top forms of the quadric are $\mathcal{O}_{\mathbb{P}^3}(-2)|_Q$. Section 12.4 recovers this from the adjunction formula: $-2 = 2 - 3 - 1$.

**Example P3.12.27 (the tangent sheaf).** The tangent sheaf of a smooth scheme $X$ over $k$ is $\mathcal{T}_X = \mathcal{H}om(\Omega_X, \mathcal{O}_X)$, locally free of rank $\dim X$. The Euler sequence is a sequence of locally free sheaves, so it stays exact after dualizing:
$$
0 \longrightarrow \mathcal{O}_P \xrightarrow{\ \beta^\vee\ } \mathcal{O}_P(1)^{n+1} \xrightarrow{\ \alpha^\vee\ } \mathcal{T}_P \longrightarrow 0 .
$$
Here $\beta^\vee(1) = \sum_i x_i e_i^\vee$ is the Euler vector field $\sum_i x_i\,\partial/\partial x_i$, and $\alpha^\vee$ sends $x_j e_i^\vee$ to the vector field $x_j\,\partial/\partial x_i$, which is well defined on $\mathbb{P}^n$ only modulo the Euler field. The global sections of $\mathcal{O}(1)^{n+1}$ are the $(n+1) \times (n+1)$ matrices, the Lie algebra of $\mathrm{GL}_{n+1}$, and the sequence shows that the matrices modulo the scalars, the Lie algebra of $\mathrm{PGL}_{n+1}$, give global vector fields on $\mathbb{P}^n$. That these are all of them needs $H^1(\mathbb{P}^n, \mathcal{O}) = 0$, Serre's computation of the cohomology of projective space.

### Proof

*Proof of Theorem P3.12.20.* Let $M \subseteq S(-1)^{n+1}$ be the kernel of the map of graded modules $S(-1)^{n+1} \to S$, $\sum_i g_i e_i \mapsto \sum_i g_i x_i$, which has degree $0$. Its image is the ideal $S_+ = (x_0, \dots, x_n)$. So there is an exact sequence of graded modules
$$
0 \to M \to S(-1)^{n+1} \to S \to S/S_+ \to 0 .
$$
By part 3 of Proposition P3.6.11 the sheaf functor is exact. On $D_+(x_j)$ the element $x_j \in S_+$ acts as $0$ on $S/S_+$ and is invertible in the localization, so $(S/S_+)_{(x_j)} = 0$, and $\widetilde{S/S_+} = 0$. So $0 \to \widetilde M \to \mathcal{O}_P(-1)^{n+1} \to \mathcal{O}_P \to 0$ is exact, and the second map is $\beta$. It remains to identify $\widetilde M$ with $\Omega_P$.

Fix $j$ and write $B_j = S_{(x_j)} = A[x_0/x_j, \dots, x_n/x_j]$. An element of $M_{(x_j)}$ is $\sum_i g_i e_i$ with $g_i \in S_{x_j}$ homogeneous of degree $-1$ and $\sum_i g_i x_i = 0$. Then $g_i x_j \in B_j$. Define the $B_j$-linear map
$$
\varphi_j \colon M_{(x_j)} \to \Omega_{B_j/A} , \qquad \varphi_j\Big(\sum_i g_i e_i\Big) = \sum_i (g_i x_j)\, d(x_i/x_j) .
$$
For $i \neq j$ let $m_i = (x_j e_i - x_i e_j)/x_j^2$. It lies in $M_{(x_j)}$, as $x_j x_i - x_i x_j = 0$, and $\varphi_j(m_i) = d(x_i/x_j) - (x_i/x_j)\, d(1) = d(x_i/x_j)$. The $m_i$ generate $M_{(x_j)}$: for $\sum_i g_i e_i \in M_{(x_j)}$,
$$
\sum_{i \neq j} (g_i x_j) m_i = \sum_{i \neq j} g_i e_i - \Big(\sum_{i \neq j} \frac{g_i x_i}{x_j}\Big) e_j = \sum_{i \neq j} g_i e_i + g_j e_j ,
$$
since $\sum_{i \neq j} g_i x_i = -g_j x_j$. So $\varphi_j$ maps a set of generators of $M_{(x_j)}$ to a basis of the free module $\Omega_{B_j/A}$. Then $\varphi_j$ is surjective, and it is injective: if $\varphi_j(\sum_{i \neq j} h_i m_i) = \sum_{i \neq j} h_i\, d(x_i/x_j) = 0$, then all $h_i = 0$. So $\varphi_j$ is an isomorphism, the $m_i$ form a basis of $M_{(x_j)}$, and $\varphi_j^{-1}$ is the formula for $\alpha$ in the statement.

The $\varphi_j$ agree on overlaps. On $D_+(x_j x_l)$, the quotient rule in $\Omega_{B_{jl}/A}$, $B_{jl} = S_{(x_j x_l)}$, applied to $x_i/x_j = (x_i/x_l)(x_l/x_j)$, gives
$$
x_j\, d(x_i/x_j) = x_l\, d(x_i/x_l) + \frac{x_j x_i}{x_l}\, d(x_l/x_j) ,
$$
so for $\sum_i g_i e_i \in M_{(x_j x_l)}$,
$$
\sum_i g_i x_j\, d(x_i/x_j) = \sum_i g_i x_l\, d(x_i/x_l) + \Big(\sum_i g_i x_i\Big) \frac{x_j}{x_l}\, d(x_l/x_j) = \sum_i g_i x_l\, d(x_i/x_l) .
$$
Both sides are elements of $\Omega_{B_{jl}/A}$, which is $\Omega_P$ on $D_+(x_j x_l)$ by Theorem P3.12.2, and the restrictions of $\widetilde M$ are the localizations by part 1 of Proposition P3.6.11. So the isomorphisms $\widetilde M|_{D_+(x_j)} \cong \Omega_P|_{D_+(x_j)}$ glue to an isomorphism $\widetilde M \cong \Omega_P$. Composing its inverse with the inclusion $\widetilde M \to \mathcal{O}_P(-1)^{n+1}$ gives $\alpha$.

For the twist, $\mathcal{O}_P(-1) \otimes \mathcal{O}_P(1) \cong \mathcal{O}_P$ by part 4 of Proposition P3.6.11, and tensoring with the invertible sheaf $\mathcal{O}_P(1)$ is exact, so $0 \to \Omega_P(1) \to \mathcal{O}_P^{n+1} \to \mathcal{O}_P(1) \to 0$ is exact with second map $e_i \mapsto x_i$, which is the sequence of the exercise. $\square$

*Proof of Lemma P3.12.21.* Work on an open set $U$ on which $\mathcal{E}'$ and $\mathcal{E}''$ are free. The formula is well defined: replacing $\tilde e''_1$ by $\tilde e''_1 + e'$ with $e' \in \mathcal{E}'(U)$ adds the term $e'_1 \wedge \dots \wedge e'_a \wedge e' \wedge \dots$, which vanishes because $e'_1 \wedge \dots \wedge e'_a \wedge e'$ is the image of an element of $\bigwedge^{a+1} \mathcal{E}'|_U = 0$. It is multilinear and alternating in the $e'_i$ and in the $e''_j$, so it defines a map $\det \mathcal{E}' \otimes \det \mathcal{E}'' \to \det \mathcal{E}$ on $U$, and these maps agree on overlaps because the formula does not involve choices. On $U$ choose bases $e'_1, \dots, e'_a$ of $\mathcal{E}'$ and $e''_1, \dots, e''_b$ of $\mathcal{E}''$, and lifts $\tilde e''_j$. Then $e'_1, \dots, e'_a, \tilde e''_1, \dots, \tilde e''_b$ is a basis of $\mathcal{E}|_U$: it generates, by exactness, and it has $a + b$ elements in a free module of rank $a + b$, so it is a basis by the determinant argument of the proof of Theorem P3.12.14. So the map sends a generator to a generator and is an isomorphism. $\square$

*Proof of Corollary P3.12.22.* (1) By Theorem P3.12.20 and Lemma P3.12.21, $\bigwedge^n \Omega_P \otimes \det \mathcal{O}_P \cong \det \mathcal{O}_P(-1)^{n+1}$. Here $\det \mathcal{O}_P = \mathcal{O}_P$, and $\det \mathcal{O}_P(-1)^{n+1} \cong \mathcal{O}_P(-1)^{\otimes (n+1)} \cong \mathcal{O}_P(-n-1)$ by Lemma P3.12.21 applied $n$ times to the split sequences of the direct sum and by part 4 of Proposition P3.6.11.

(2) Tensoring the Euler sequence with $\mathcal{O}_P(m)$ gives the exact sequence $0 \to \Omega_P(m) \to \mathcal{O}_P(m-1)^{n+1} \to \mathcal{O}_P(m) \to 0$. Global sections are left exact (Proposition P2.5.22), so $\Gamma(P, \Omega_P(m))$ is the kernel of $\Gamma(\mathcal{O}(m-1))^{n+1} \to \Gamma(\mathcal{O}(m))$, which is the kernel of $S_{m-1}^{n+1} \to S_m$ by Theorem P3.6.12. For $m = 0$ the source is $S_{-1}^{n+1} = 0$. For $m = 1$ the map is $A^{n+1} \to S_1$, $(a_i) \mapsto \sum_i a_i x_i$, which is injective. For $m = 2$ and $A = k$ see Example P3.12.25. $\square$

*Proof of Proposition P3.12.23.* The scheme $P \to Y$ is the base change of $X \to S$ along $Y \to S$, so part 4 of Theorem P3.12.2 gives $\Omega_{P/Y} \cong p^* \Omega_{X/S}$; in the same way $\Omega_{P/X} \cong q^* \Omega_{Y/S}$. Let $u \colon p^* \Omega_{X/S} \oplus q^* \Omega_{Y/S} \to \Omega_{P/S}$ be the map of the statement and $v \colon \Omega_{P/S} \to \Omega_{P/Y} \oplus \Omega_{P/X} \cong p^* \Omega_{X/S} \oplus q^* \Omega_{Y/S}$ the sum of the second maps of the first sequences for $P \to Y \to S$ and $P \to X \to S$. The composite $p^* \Omega_{X/S} \to \Omega_{P/S} \to \Omega_{P/X}$ is zero, by exactness of the first sequence for $P \to X \to S$, and the composite $p^* \Omega_{X/S} \to \Omega_{P/S} \to \Omega_{P/Y}$ is the base change isomorphism, as both send $1 \otimes dh$ to $d(p^\sharp h)$. With the same statements for $q$, $v \circ u$ is an isomorphism, so $u$ is injective. It is surjective: on affine opens $P$ is $\operatorname{Spec}(B \otimes_A C)$, and $\Omega_{B \otimes_A C/A}$ is generated by the $d(b \otimes c) = (b \otimes 1)\, d(1 \otimes c) + (1 \otimes c)\, d(b \otimes 1)$, which lie in the image of $u$. So $u$ is an isomorphism.

If $X$ and $Y$ are smooth over $k$ of pure dimensions $a$ and $b$, then $P$ has pure dimension $a + b$ (Theorem P3.7.4 and Chapter 7 for products of varieties), and $\Omega_P$ is locally free of rank $a + b$ by the first part, so $P$ is smooth by Corollary P3.12.11. The statement on top forms is Lemma P3.12.21 for the split sequence $0 \to p^* \Omega_X \to \Omega_P \to q^* \Omega_Y \to 0$, since pullback commutes with exterior powers. $\square$

### Exercises

1. (A) Check by a direct computation on $D_+(x_0) \cap D_+(x_1)$ of $\mathbb{P}^2$ that the formulas for $\alpha(d(x_2/x_0))$ and $\alpha(d(x_2/x_1))$ agree with $d(x_2/x_0) = (x_1/x_0)\, d(x_2/x_1) + (x_2/x_1)\, d(x_1/x_0)$.
2. (A) Show that $\Gamma(\mathbb{P}^n_k, \bigwedge^n \Omega(n + 1)) = k$, and that a generator is, on $D_+(x_0)$, the form $x_0^{n+1}\, d(x_1/x_0) \wedge \dots \wedge d(x_n/x_0)$. Compare with Example P1.12.28.
3. (A) Show that $\Gamma(\mathbb{P}^n_k, \Omega_{\mathbb{P}^n}(m)) = 0$ for $m \leq 1$.
4. (B) Show that $\Omega_{\mathbb{P}^n_k}$ is not isomorphic to a direct sum of invertible sheaves for $n \geq 2$. Hint: by Theorem P3.8.20 and Corollary P3.9.11 every invertible sheaf is some $\mathcal{O}(a)$; use $\Gamma(\Omega(1)) = 0$ and part 1 of Corollary P3.12.22.
5. (B) Show that $\mathcal{T}_{\mathbb{P}^n_k}(-1)$ is generated by $n + 1$ global sections, and that these are linearly independent in $\Gamma(\mathbb{P}^n_k, \mathcal{T}(-1))$.
6. (C) Let $Y$ be a scheme, $\mathcal{E}$ a locally free sheaf of rank $r + 1$ on $Y$, and $\pi \colon \mathbb{P}(\mathcal{E}) = \operatorname{Proj} \operatorname{Sym} \mathcal{E} \to Y$ the projective bundle of Section 6.4. Prove the relative Euler sequence $0 \to \Omega_{\mathbb{P}(\mathcal{E})/Y} \to \pi^* \mathcal{E} \otimes \mathcal{O}(-1) \to \mathcal{O} \to 0$, and deduce $\bigwedge^r \Omega_{\mathbb{P}(\mathcal{E})/Y} \cong \pi^* \det \mathcal{E} \otimes \mathcal{O}(-r - 1)$.

### Lean

Projective space is in Mathlib as the scheme `AlgebraicGeometry.Proj` of a graded ring; the twisting sheaves, the sheaf of differentials and the Euler sequence are not. The exterior powers are `exteriorPower` (definition). In mmp-lean the canonical divisor is the divisor of a rational top form, `MinimalModel.CanonicalDivisor`, and the fidelity checks of `MinimalModel/Fidelity/ToricCone.lean` use the canonical divisor of the toric model of $\mathbb{P}^2$, minus the sum of the three boundary lines, whose degree on a line is $-3$. Corollary P3.12.22 for $n = 2$ is the same fact, $K_{\mathbb{P}^2} = -3H$. The handbook adds no `MinimalModel` node here.

### Notes and history

The Euler sequence is Hartshorne, Theorem II.8.13, and Vakil, Section 21.4, both by a similar kernel argument. Hartshorne proves it for $\mathbb{P}^n_A$ with the same chart computation, and its relative form for projective bundles is Exercise 6. The literature state is theorem. The name comes from Euler's identity $\sum_i x_i\, \partial F/\partial x_i = (\deg F) F$ for a homogeneous polynomial, whose vector field $\sum_i x_i\,\partial/\partial x_i$ is the image of $\beta^\vee$. The formula $K_{\mathbb{P}^n} = -(n+1) H$ makes $\mathbb{P}^n$ the first Fano variety: $-K$ is ample. In the minimal model program $\mathbb{P}^n$ is the end of the program for every rationally connected variety of Picard number one that it reaches, and $\mathbb{P}^n \to \operatorname{Spec} k$ is the simplest Mori fibre space.
