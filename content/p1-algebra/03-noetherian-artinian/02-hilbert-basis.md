---
title: The Hilbert basis theorem
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch7, Mat86:ch1, Eis95:ch1]
requires: [P1.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Hilbert basis theorem

### Statement

**Theorem P1.3.10 (Hilbert basis theorem).** If $A$ is a Noetherian ring, then the polynomial ring $A[x]$ is Noetherian.

Lean: Mathlib `Polynomial.isNoetherianRing` (proved in Mathlib).

*Proof.* Suppose that an ideal $I \subseteq A[x]$ is not finitely generated. Choose $f_1 \in I$ of least degree. Step by step, choose $f_{i+1} \in I \setminus (f_1, \dots, f_i)$ of least degree; this set is never empty, since $I$ is not finitely generated. Let $d_i = \deg f_i$ and let $a_i$ be the leading coefficient of $f_i$. By the choice, $d_1 \leq d_2 \leq \dots$. The chain of ideals $(a_1) \subseteq (a_1, a_2) \subseteq \dots$ of $A$ stops, so for some $N$ there are $u_1, \dots, u_N \in A$ with $a_{N+1} = \sum_{i \leq N} u_i a_i$. Put
$$
g = f_{N+1} - \sum_{i=1}^{N} u_i x^{d_{N+1} - d_i} f_i .
$$
The sum has degree at most $d_{N+1}$ and its coefficient of $x^{d_{N+1}}$ is $a_{N+1}$, so $\deg g < d_{N+1}$. Also $g \in I$ and $g \notin (f_1, \dots, f_N)$, since $f_{N+1} \notin (f_1, \dots, f_N)$. This contradicts the choice of $f_{N+1}$ as an element of least degree. $\square$

**Corollary P1.3.11.** If $A$ is Noetherian, then $A[x_1, \dots, x_n]$ is Noetherian, and so is every finitely generated $A$-algebra. In particular every finitely generated algebra over a field, and every finitely generated $\mathbb{Z}$-algebra, is Noetherian.

Lean: Mathlib `MvPolynomial.isNoetherianRing` and `Algebra.FiniteType.isNoetherianRing` (proved in Mathlib).

*Proof.* Induction on $n$, with $A[x_1, \dots, x_n] = A[x_1, \dots, x_{n-1}][x_n]$. A finitely generated $A$-algebra is a quotient of some $A[x_1, \dots, x_n]$, and quotients of Noetherian rings are Noetherian (Section 3.1). $\square$

**Corollary P1.3.12 (finitely many equations).** Let $k$ be a field and $S \subseteq k[x_1, \dots, x_n]$ any set of polynomials. Then there are $f_1, \dots, f_r \in S$ with $V(S) = V(f_1, \dots, f_r)$ in $k^n$ and in $\operatorname{Spec} k[x_1, \dots, x_n]$.

Lean: Mathlib proves the ingredient `MvPolynomial.isNoetherianRing`; the handbook does not name a single declaration.

*Proof.* The ideal $(S)$ is finitely generated. Each generator is a finite combination of elements of $S$, so finitely many elements $f_1, \dots, f_r$ of $S$ generate $(S)$. Then $V(S) = V((S)) = V(f_1, \dots, f_r)$. $\square$

**Remark P1.3.13 (power series).** If $A$ is Noetherian, then $A[[x]]$ is Noetherian. The proof is the one above with the leading coefficient replaced by the lowest coefficient: choose $f_{i+1}$ in $I \setminus (f_1, \dots, f_i)$ of greatest order, and use the convergence of an infinite sum of correction terms in the $x$-adic topology. Chapter 6 gives the general statement for completions. Mathlib has the instance `IsNoetherianRing R⟦X⟧`, proved by Cohen's theorem of Section 3.1.

### Proof in words

To find generators of an ideal of $A[x]$, look at the leading coefficients of its elements. These form ideals of $A$, which are finitely generated. A polynomial whose leading coefficient is a combination of the leading coefficients of earlier polynomials can be reduced to lower degree, and the process ends. This is also the idea behind the division algorithm and Gröbner bases.

The geometric content is that affine varieties are defined by finitely many equations, and that the coordinate ring $k[X]$ of an affine variety is Noetherian. So all the results of Chapter 2 on Noetherian rings apply to $k[X]$: primary decomposition, associated primes, and finitely many minimal primes. Every scheme of finite type over a field or over $\mathbb{Z}$ is Noetherian, and the MMP never leaves this class.

### Examples

**Example P1.3.14 (a plane curve).** The set $V(S)$ for $S = \{y - x^2, y^2 - x^4, y^3 - x^6, \dots\}$ is the parabola $V(y - x^2)$, since every element of $S$ is a multiple of $y - x^2$. The corollary says that this happens for every $S$: some finite part of $S$ defines the same set.

**Example P1.3.15 (a subalgebra that is not finitely generated).** The ring $B = k[x, xy, xy^2, \dots]$ of Section 3.1 is a subalgebra of $k[x, y]$, and it is not Noetherian, so it is not a finitely generated $k$-algebra. Subalgebras of finitely generated algebras need not be finitely generated. Hilbert's fourteenth problem asked whether rings of invariants $k[x_1, \dots, x_n]^G$ for a group $G$ acting linearly are always finitely generated. Nagata gave a counterexample in 1959. For a finite group $G$ the answer is yes, by Exercise 5 and Chapter 4.

**Example P1.3.16 (a ring of finite type over $\mathbb{Z}$).** The ring $\mathbb{Z}[x, y]/(y^2 - x^3 - 1)$ is Noetherian. Its spectrum maps to $\operatorname{Spec} \mathbb{Z}$, and the fibre over a prime $p$ is the affine curve $y^2 = x^3 + 1$ over $\mathbb{F}_p$. Families over $\operatorname{Spec} \mathbb{Z}$ or over a curve are the setting of the relative MMP in Volume 1, and the Hilbert basis theorem makes them Noetherian.

### Exercises

1. (A) Let $S = \{x^a y^b : a + b \geq 5\} \subseteq k[x, y]$. Find a finite subset $T \subseteq S$ with $(T) = (S)$, and show that no proper subset of your $T$ works.
2. (A) Show that $\mathbb{Z}[\sqrt{2}]$, $k[t^2, t^3]$ and $k[x, y, z]/(xy - z^2)$ are Noetherian.
3. (B) Let $A$ be Noetherian and $f = \sum a_i x^i \in A[x]$. Show that $f$ is nilpotent if and only if every $a_i$ is nilpotent. Deduce that the nilradical of $A[x]$ is $\mathfrak{N}[x]$, where $\mathfrak{N}$ is the nilradical of $A$, and that it is a nilpotent ideal (use Section 3.3).
4. (B) Fill in the proof of the remark on power series: if $A$ is Noetherian, then $A[[x]]$ is Noetherian.
5. (C) (Artin-Tate.) Let $A \subseteq B \subseteq C$ be rings with $A$ Noetherian, $C$ a finitely generated $A$-algebra, and $C$ finitely generated as a $B$-module. Show that $B$ is a finitely generated $A$-algebra. (Hint: write the algebra generators $x_i$ of $C$ and the products $x_i y_j$ of module generators in terms of module generators $y_j$. Let $B_0 \subseteq B$ be the $A$-algebra generated by the coefficients. Then $C$ is a finite $B_0$-module, $B_0$ is Noetherian, and $B$ is a $B_0$-submodule of $C$.)

### Lean

The Hilbert basis theorem is `Polynomial.isNoetherianRing`, the case of several variables is `MvPolynomial.isNoetherianRing`, and the case of finitely generated algebras is `Algebra.FiniteType.isNoetherianRing`. The Artin-Tate lemma of Exercise 5 is `fg_of_fg_of_fg`. The handbook adds no `MinimalModel` node here.

### Notes and history

Hilbert proved the basis theorem in 1890 in his work on invariant theory. His proof was not constructive, and Gordan is said to have called it theology, not mathematics. The proof by leading coefficients is the standard one. Artin and Tate proved their lemma in 1951. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 7, and Matsumura, Chapter 1.
