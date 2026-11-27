---
title: First computations
nodes: []
sources: [Har77, Vak25, Stacks]
reads_with: [Har77:III.4, Vak25:ch18]
requires: [P2.6, P2.7, P3.2, P3.5, P3.6, P3.12, P4.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## First computations

### Statement

The simplest Čech complexes come from covers by two affine open sets. The Mayer-Vietoris sequence of P2 Ch. 7 then has only four terms.

**Proposition P4.1.23 (Mayer-Vietoris for two affine pieces).** Let $X = U \cup V$ be a scheme covered by two affine open sets whose intersection $U \cap V$ is affine, for instance any separated scheme covered by two affine open sets. For every quasi-coherent $\mathcal{F}$ there is an exact sequence
$$0 \to \mathcal{F}(X) \to \mathcal{F}(U) \oplus \mathcal{F}(V) \xrightarrow{\ d\ } \mathcal{F}(U \cap V) \to H^1(X, \mathcal{F}) \to 0, \qquad d(a, b) = b|_{U \cap V} - a|_{U \cap V},$$
natural in $\mathcal{F}$, and $H^p(X, \mathcal{F}) = 0$ for $p \geq 2$.

Lean: not in Lean as stated.

**Proposition P4.1.24 (the projective line over a ring).** Let $A$ be a ring and $n \in \mathbb{Z}$. Then $H^0(\mathbb{P}^1_A, \mathcal{O}(n))$ is a free $A$-module of rank $\max(n + 1, 0)$, $H^1(\mathbb{P}^1_A, \mathcal{O}(n))$ is a free $A$-module of rank $\max(-n - 1, 0)$, and $H^p(\mathbb{P}^1_A, \mathcal{O}(n)) = 0$ for $p \geq 2$. For every ring map $A \to B$ the maps of Theorem P4.1.17 are isomorphisms.

Lean: not in Lean as stated.

The second statement is the relative form of Example P2.7.23. Chapter 2 proves the same for $\mathbb{P}^r_A$ and all $r$, with $H^r(\mathbb{P}^r_A, \mathcal{O}(-r-1)) \cong A$.

### Proof in words

A cover by two affine open sets with affine intersection has a Čech complex of length one, and Corollary P4.1.9 says that it computes cohomology. Its kernel is the module of global sections and its cokernel is $H^1$. On $\mathbb{P}^1_A$ the three rings are polynomial and Laurent polynomial rings over $A$, the differential respects the grading by the degree in $t$, and the computation of Example P2.7.23 goes through over $A$ monomial by monomial.

### Examples

**Example P4.1.25 (the class of $dt/t$).** Let $X = \mathbb{P}^1_k$ with the charts $U_0 = \operatorname{Spec} k[t]$, $U_1 = \operatorname{Spec} k[s]$, $s = t^{-1}$, and let $\Omega = \Omega_{X/k}$ be the sheaf of differentials of P3 Ch. 12. It is free on $U_0$ with basis $dt$ and on $U_1$ with basis $ds = -t^{-2} \, dt$. By Proposition P4.1.23, $H^1(X, \Omega)$ is the cokernel of
$$k[t] \, dt \oplus k[s] \, ds \to k[t, t^{-1}] \, dt, \qquad (a \, dt, b \, ds) \mapsto -b(t^{-1}) t^{-2} \, dt - a \, dt.$$
The image is spanned by the $t^m \, dt$ with $m \geq 0$, from $a$, and with $m \leq -2$, from $b$. So $H^1(\mathbb{P}^1_k, \Omega) = k \cdot [dt/t]$ is one-dimensional, and the coefficient of $t^{-1} \, dt$, the residue at $t = 0$, is an isomorphism $H^1(\mathbb{P}^1_k, \Omega) \to k$. This agrees with $\Omega \cong \mathcal{O}(-2)$ and Example P2.7.23. The residue map is the trace map of Serre duality on $\mathbb{P}^1$, which Chapter 7 constructs in general.

**Example P4.1.26 (a sheaf of modules that is not quasi-coherent).** Let $X = \mathbb{A}^1_k = \operatorname{Spec} k[t]$, $P$ the origin, $U = X \setminus \{P\}$ and $j \colon U \to X$ the inclusion. The extension by zero $j_! \mathcal{O}_U$ is an $\mathcal{O}_X$-module with stalk $\mathcal{O}_{X,x}$ at $x \neq P$ and $0$ at $P$. A section over a connected open $W \ni P$ is a function on $W \cap U$ whose support is closed in $W$, and on the irreducible set $W \cap U$ only $0$ has this property. So $\Gamma(X, j_! \mathcal{O}_U) = 0$. The quotient $\mathcal{O}_X / j_! \mathcal{O}_U$ is supported on the closed point $P$, with stalk $\mathcal{O}_{X, P} = k[t]_{(t)}$, so it is the skyscraper sheaf with value $k[t]_{(t)}$ at $P$. The long exact sequence of $0 \to j_! \mathcal{O}_U \to \mathcal{O}_X \to \mathcal{O}_X/j_! \mathcal{O}_U \to 0$ and $H^1(X, \mathcal{O}_X) = 0$ give
$$H^1(X, j_! \mathcal{O}_U) \cong k[t]_{(t)}/k[t] \neq 0,$$
which contains the class of $1/(t - 1)$. So the affine line has an $\mathcal{O}_X$-module with nonzero $H^1$, and Theorem P4.1.8 needs the hypothesis of quasi-coherence. The sheaf $j_! \mathcal{O}_U$ is not quasi-coherent, as also follows from $\Gamma(X, j_! \mathcal{O}_U) = 0$ and Theorem P3.5.12.

**Example P4.1.27 (constant sheaves and two points).** Keep $X = \mathbb{A}^1_k$, now with two distinct closed points $P$ and $Q$, and let $U = X \setminus \{P, Q\}$ with inclusion $j$. For the constant sheaf $\underline{\mathbb{Z}}$ there is an exact sequence $0 \to j_! \underline{\mathbb{Z}}_U \to \underline{\mathbb{Z}}_X \to \mathbb{Z}_P \oplus \mathbb{Z}_Q \to 0$ with skyscraper sheaves on the right. The constant sheaf on the irreducible space $X$ is flasque, so $H^1(X, \underline{\mathbb{Z}}_X) = 0$ (Example P2.7.14), and
$$H^1(X, j_! \underline{\mathbb{Z}}_U) \cong \operatorname{coker}(\mathbb{Z} \xrightarrow{\ (1, 1)\ } \mathbb{Z}^2) \cong \mathbb{Z}.$$
With one point removed instead of two the same sequence gives $H^1 = 0$. The Zariski cohomology of sheaves of abelian groups that are not modules sees the combinatorics of closed sets, and has nothing to do with the coherent theory.

**Example P4.1.28 (Čech cohomology of a cover that is not fine enough).** Let $X = \mathbb{P}^1_k$ and cover it by the single open set $X$. The Čech complex of $\mathcal{O}(-2)$ for this cover is $\Gamma(X, \mathcal{O}(-2)) = 0$ in degree $0$, with $\check{H}^1 = 0$, while $H^1(X, \mathcal{O}(-2)) \cong k$. Its only member $X$ is not affine, so Corollary P4.1.9 does not apply. The colimit over refinements of Theorem P2.7.22 recovers $H^1$ from the standard cover.

### Proof

*Proposition P4.1.23.* Order the cover as $(U, V)$. The ordered Čech complex is $\mathcal{F}(U) \times \mathcal{F}(V) \to \mathcal{F}(U \cap V)$ in degrees $0$ and $1$, with differential $d(a, b) = b - a$ restricted to $U \cap V$, by Definition P2.7.18. All finite intersections are $U$, $V$ or $U \cap V$, which are affine, so by Corollary P4.1.9 its cohomology is $H^p(X, \mathcal{F})$. In degree $0$ this is $\mathcal{F}(X)$ by the sheaf property, in degree $1$ it is the cokernel of $d$, and in degrees $p \geq 2$ it is $0$. The naturality follows from the naturality of the Čech complex in $\mathcal{F}$. A separated scheme has affine intersections of affine open sets (Proposition P3.4.12). $\square$

*Proposition P4.1.24.* Use the cover of $\mathbb{P}^1_A$ by $U_0 = \operatorname{Spec} A[t]$ and $U_1 = \operatorname{Spec} A[s]$ with $s = t^{-1}$ and $U_{01} = \operatorname{Spec} A[t, t^{-1}]$. As in Example P2.7.23, $\mathcal{O}(n)$ is trivial on each chart, and with the trivialization on $U_0$ the complex of Proposition P4.1.23 is
$$A[t] \oplus A[s] \xrightarrow{d} A[t, t^{-1}], \qquad d(f, g) = t^n g(t^{-1}) - f.$$
The three modules are free with bases of monomials, and $d$ maps the monomial basis of the source to signed monomials of the target: $t^m \mapsto -t^m$ for $m \geq 0$ from $f$, and $s^j \mapsto t^{n - j}$ for $j \geq 0$ from $g$. So the image of $d$ is the free submodule spanned by the $t^m$ with $m \geq 0$ or $m \leq n$, and the cokernel is free on the $t^m$ with $n < m < 0$, of rank $\max(-n-1, 0)$. The kernel consists of the pairs $(f, g)$ with $f = t^n g(t^{-1})$. Writing $f = \sum_m c_m t^m$, this forces $c_m = 0$ unless $0 \leq m \leq n$, and then $g$ is determined by $f$. So the kernel is free on the $t^m$ with $0 \leq m \leq n$, of rank $\max(n+1, 0)$. By Proposition P4.1.23 these are $H^0$ and $H^1$, and $H^p = 0$ for $p \geq 2$.

For a ring map $A \to B$, $\mathbb{P}^1_A \times_A \operatorname{Spec} B = \mathbb{P}^1_B$ and the pullback of $\mathcal{O}(n)$ is $\mathcal{O}(n)$, and the complex for $B$ is the complex for $A$ tensored with $B$, as in the proof of Theorem P4.1.17. The bases of monomials of kernel, image and cokernel are compatible with $- \otimes_A B$, since the differential is a signed matching of basis elements. So the maps $H^p(\mathbb{P}^1_A, \mathcal{O}(n)) \otimes_A B \to H^p(\mathbb{P}^1_B, \mathcal{O}(n))$ are isomorphisms. $\square$

### Exercises

1. (A) Let $X = \mathbb{P}^1_k$ and $\mathcal{T} = \Omega^\vee$ its tangent sheaf. Use Proposition P4.1.23 to show that $H^0(X, \mathcal{T})$ is three-dimensional, spanned by $\partial_t$, $t \partial_t$ and $t^2 \partial_t$, and that $H^1(X, \mathcal{T}) = 0$.
2. (A) Let $X$ be the affine line with a doubled origin. Compute $H^0$ and $H^1$ of the line bundle $\mathcal{L}_n$ glued from $\mathcal{O}$ on the two charts by multiplication by $t^n$ on $U_{12}$, for each $n \in \mathbb{Z}$, and show that $H^1(X, \mathcal{L}_n)$ is infinite-dimensional for every $n$.
3. (A) In Example P4.1.27, compute $H^0$ and $H^1$ of $j_! \underline{\mathbb{Z}}_U$ when $r$ distinct closed points are removed.
4. (B) Let $C \subseteq \mathbb{P}^2_k$ be the conic $V_+(xz - y^2)$, with $k$ algebraically closed. Cover it by the two affine open sets $C \cap D_+(x)$ and $C \cap D_+(z)$, show that both are isomorphic to $\mathbb{A}^1_k$ and that their intersection is $\mathbb{G}_m$, and compute $H^1(C, \mathcal{O}_C) = 0$. Deduce that the restriction of $\mathcal{O}_{\mathbb{P}^2}(1)$ to $C$ has $h^0 = 3$ and $h^1 = 0$.
5. (B) Let $A$ be a ring, $X = \mathbb{P}^1_A$, and $0 \to \mathcal{O}(-2) \xrightarrow{(x_1, -x_0)} \mathcal{O}(-1)^{\oplus 2} \xrightarrow{(x_0, x_1)} \mathcal{O} \to 0$ the Koszul sequence of the coordinates. Compute its long exact sequence with Proposition P4.1.24 and identify the connecting map $H^0(\mathcal{O}) \to H^1(\mathcal{O}(-2))$.

### Lean

Mathlib has the $\operatorname{Proj}$ construction, `AlgebraicGeometry.Proj`, with its separatedness `AlgebraicGeometry.Proj.isSeparated`, and the sheaf of a module on an affine scheme. The Mayer-Vietoris sequence for quasi-coherent sheaves, the cohomology of $\mathcal{O}(n)$ on $\mathbb{P}^1_A$ and the computations of this section are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

The computation of Proposition P4.1.24 is the case $r = 1$ of Serre's computation of the cohomology of projective space in *Faisceaux algébriques cohérents*, which Chapter 2 reproduces. The residue description of $H^1(\mathbb{P}^1, \Omega)$ in Example P4.1.25 is the oldest form of duality on curves, and the extension by zero of Example P4.1.26 is Hartshorne's standard example of a sheaf of modules on an affine scheme with nonzero cohomology. The literature state is theorem. The minimal model program meets such Čech computations in the examples of every volume, from the curves of Volume 1 to the surfaces of Volume 2, and the base change statement of Proposition P4.1.24 is the model for the theorem on cohomology and base change of Chapter 5.
