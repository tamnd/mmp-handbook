---
title: The Hom scheme and bend-and-break, recalled
nodes: []
sources: [Mor79, Mor82, Kol96, Deb01, KM98]
reads_with: [Deb01:ch2, Deb01:ch3, Kol96:II.1, KM98:1.2]
requires: [P5.4, P7.2, P7.4, P8.1, P8.2]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Hom scheme and bend-and-break, recalled

### Statement

The volume works with the following conventions, which are those of Volume P8, Chapters 1 to 3.

**Definition 6.1.1 (conventions and rational curves).** Throughout the volume, $k$ is an algebraically closed field and $X$ is a smooth projective variety of dimension $n$ over $k$, unless a statement says otherwise. A *rational curve* on $X$ is an integral closed curve $\Gamma \subseteq X$ whose normalization is $\mathbb{P}^1$; its normalization map $\nu \colon \mathbb{P}^1 \to \Gamma \subseteq X$ is birational onto $\Gamma$ and $\nu_* \mathbb{P}^1 = \Gamma$. For a nonconstant morphism $f \colon \mathbb{P}^1 \to X$ the cycle $f_* \mathbb{P}^1$ is $d \, \Gamma$, where $\Gamma = f(\mathbb{P}^1)$ and $d$ is the degree of $f$ onto its image, and its class in $N_1(X)$ (Definition P7.2.4) is written $[f]$. A *rational $1$-cycle* is an effective $1$-cycle $\sum_i a_i \Gamma_i$ with every $\Gamma_i$ a rational curve. For a divisor $D$ the number $D \cdot f_* \mathbb{P}^1 = \deg f^* D$ is written $D \cdot f$.

The volume uses the following results of Volume P8, which it does not prove again. The list fixes the notation of the later chapters.

**Theorem 6.1.2 (the tools of Volume P8).** Let $X$ be as in Definition 6.1.1.

1. (The Hom scheme, Theorem P8.1.4 and Proposition P8.1.6.) For a smooth projective curve $C$, a finite set $B \subseteq C$ and a morphism $g \colon B \to X$, the morphisms $C \to X$ that restrict to $g$ form a scheme $\operatorname{Hom}(C, X; g)$, a disjoint union of countably many quasi-projective schemes, with an evaluation morphism $\operatorname{ev} \colon C \times \operatorname{Hom}(C, X; g) \to X$. The class $[f_* C]$ is constant on each connected component.
2. (The dimension estimate, Theorem P8.1.10 and Corollary P8.1.12.) For $f \colon C \to X$ with $C$ of genus $g$ and $b = |B|$, $\dim_{[f]} \operatorname{Hom}(C, X; f|_B) \ge -K_X \cdot f_* C + n(1 - g) - n b$. If $H^1(C, f^* T_X(-B)) = 0$, the scheme is smooth of that dimension at $[f]$ (Corollary P8.1.13). For $C = \mathbb{P}^1$, $f$ is *free* or *very free* if every summand of $f^* T_X$ has degree at least $0$ or at least $1$ (Definition P5.4.12).
3. (Bend-and-break, Theorems P8.2.5 and P8.2.6.) If $f \colon \mathbb{P}^1 \to X$ is nonconstant and $\dim_{[f]} \operatorname{Hom}(\mathbb{P}^1, X; f|_{\{0, \infty\}}) \ge 2$, then $f_* \mathbb{P}^1 \equiv Z_1 + Z_2$ with $Z_1$ and $Z_2$ nonzero rational $1$-cycles.
4. (Rational curves of bounded degree, Corollary P8.2.11 and Theorem P8.2.12.) If $C \to X$ is a morphism from a smooth projective curve with $-K_X \cdot f_* C > 0$ and $H$ is an ample divisor, there is a rational curve $\Gamma \subseteq X$ with $H \cdot \Gamma \le 2n \, H \cdot f_* C / (-K_X \cdot f_* C)$.
5. (Mori, Theorem P8.2.13.) If $K_X$ is not nef, there is a rational curve $\Gamma$ with $0 < -K_X \cdot \Gamma \le n + 1$.

Lean: not yet in Lean.

The estimate of part 2 bounds the dimension of the local ring at $[f]$. The later chapters need the same bound for each irreducible component through $[f]$, which the local structure theorem gives.

**Lemma 6.1.3 (every component has the expected dimension).** Let $f \colon \mathbb{P}^1 \to X$ be a morphism and $B \subseteq \mathbb{P}^1$ a set of $b$ points. Every irreducible component of $\operatorname{Hom}(\mathbb{P}^1, X; f|_B)$ through $[f]$ has dimension at least $-K_X \cdot f + n - n b$.

Lean: not yet in Lean.

**Corollary 6.1.4 (curves of large degree break).** Let $\Gamma \subseteq X$ be a rational curve with $-K_X \cdot \Gamma \ge n + 2$. Then $\Gamma \equiv Z_1 + Z_2$ with $Z_1$ and $Z_2$ nonzero rational $1$-cycles. If $H$ is an ample divisor, then $H \cdot \Gamma' < H \cdot \Gamma$ for every component $\Gamma'$ of $Z_1$ or $Z_2$.

Lean: not yet in Lean.

The opposite situation, a class that cannot break, is the one of the minimal curves of an extremal ray.

**Definition 6.1.5 (families, loci and unsplit classes).**

1. A *family of rational curves* on $X$ is an irreducible component $V$ of $\operatorname{Hom}(\mathbb{P}^1, X)$, with its reduced structure, whose members are nonconstant. Its class $[V]$ is the class $[f]$ of any member (Proposition P8.1.6), and $-K_X \cdot V$ means $-K_X \cdot [V]$.
2. The *locus* $\operatorname{Locus}(V)$ is the closure of $\operatorname{ev}(\mathbb{P}^1 \times V)$ in $X$. For a point $x \in X$, $V_x \subseteq V$ is the closed subset of members $f$ with $f(0) = x$, and $\operatorname{Locus}(V_x)$ is the closure of $\operatorname{ev}(\mathbb{P}^1 \times V_x)$. The family is *dominating* if $\operatorname{Locus}(V) = X$.
3. A class $\alpha \in N_1(X)$ is *unsplit* if it is not the class of a sum $Z_1 + Z_2$ of two nonzero rational $1$-cycles. A family is *unsplit* if its class is unsplit.

**Lemma 6.1.6 (minimal curves of an extremal ray do not break).** Let $R$ be a $K_X$-negative extremal ray of $\overline{NE}(X)$ that contains the class of a rational curve, and let
$$\ell(R) = \min \{ -K_X \cdot \Gamma : \Gamma \text{ a rational curve with } [\Gamma] \in R \}.$$
If $\Gamma$ is a rational curve with $[\Gamma] \in R$ and $-K_X \cdot \Gamma = \ell(R)$, then $[\Gamma]$ is unsplit, and so is the class of every family $V$ whose members are birational onto curves of class $[\Gamma]$.

Lean: not yet in Lean.

**Corollary 6.1.7 (unsplit classes have small degree).** Let $f \colon \mathbb{P}^1 \to X$ be nonconstant with $[f]$ unsplit. Then every irreducible component of $\operatorname{Hom}(\mathbb{P}^1, X; f|_{\{0, \infty\}})$ through $[f]$ has dimension at most $1$, and
$$-K_X \cdot f \le n + 1.$$

Lean: not yet in Lean.

### Proof in words

Lemma 6.1.3 is Krull's height theorem applied to the local structure theorem: the complete local ring at $[f]$ is a power series ring in $h^0$ variables modulo $h^1$ equations, and each minimal prime of such a ring has dimension at least $h^0 - h^1$. Corollary 6.1.4 is the dimension count that drives the whole volume. A rational curve with two points held fixed moves in a family of dimension at least $-K_X \cdot \Gamma - n$, the group $\mathbb{G}_m$ of automorphisms of $\mathbb{P}^1$ fixing $0$ and $\infty$ accounts for one dimension, and as soon as one more dimension is available, bend-and-break splits the curve. So a rational curve can be cut down until its anticanonical degree is at most $n + 1$, and the $H$-degree decreases at each cut. Lemma 6.1.6 runs the argument backwards: the pieces of a broken curve in an extremal ray stay in the ray, so a curve of minimal degree in the ray cannot break, and Corollary 6.1.7 turns the impossibility of breaking into a bound on dimensions.

### Examples

**Example 6.1.8 (lines and conics in projective space).** In $\mathbb{P}^n$ a line $L$ has $\mathcal{O}(1) \cdot L = 1$, so its class is unsplit: a sum of two nonzero rational $1$-cycles has degree at least $2$. By Corollary 6.1.7, the lines through two fixed points move in a family of dimension at most $1$, which is the orbit of $\mathbb{G}_m$, in accordance with Example P8.2.8, and $-K_{\mathbb{P}^n} \cdot L = n + 1$ attains the bound of Corollary 6.1.7. A smooth conic $Q \subseteq \mathbb{P}^n$ with $n \ge 2$ has $-K \cdot Q = 2(n + 1) \ge n + 2$, and Corollary 6.1.4 says that it breaks; Example P8.2.7 shows the conics through two fixed points of $\mathbb{P}^2$ degenerating to a pair of lines, and $2 [L]$ is the decomposition.

**Example 6.1.9 (the product $\mathbb{P}^1 \times \mathbb{P}^2$).** Let $X = \mathbb{P}^1 \times \mathbb{P}^2$ with $H_1$, $H_2$, $\ell_1$, $\ell_2$ as in Proposition P7.2.21, so $-K_X = 2 H_1 + 3 H_2$ and $n = 3$. The class $[\ell_1]$ is unsplit: a nonzero rational $1$-cycle $Z$ has class $a [\ell_1] + b [\ell_2]$ with $a, b \ge 0$ integers not both $0$, and a decomposition $[\ell_1] = [Z_1] + [Z_2]$ would give classes $a_i [\ell_1] + b_i [\ell_2]$ with $b_1 = b_2 = 0$ and $a_1 + a_2 = 1$, while a nonzero cycle with $b_i = 0$ has $a_i = (H_1 + H_2) \cdot Z_i \ge 1$, since $H_1 + H_2$ is ample. The same argument shows that $[\ell_2]$ is unsplit. Their degrees are $-K_X \cdot \ell_1 = 2$ and $-K_X \cdot \ell_2 = 3$, both at most $n + 1 = 4$. The graph of an isomorphism $\mathbb{P}^1 \to L$ onto a line $L \subseteq \mathbb{P}^2$ is a rational curve of class $[\ell_1] + [\ell_2]$, with $-K_X$-degree $5 = n + 2$; Corollary 6.1.4 predicts that it breaks, and it does: the graphs of the maps $t \mapsto [1 : s t : 0]$ restricted to the line $\{x_2 = 0\}$ degenerate as $s \to 0$ to $\mathbb{P}^1 \times \{[1 : 0 : 0]\} \cup \{\infty\} \times L$.

### Proof

*Theorem 6.1.2.* Each part is the result of Volume P8 named in it. In part 4 the curve $\Gamma$ is given by Corollary P8.2.11 in characteristic $p$ and by Theorem P8.2.12 in characteristic $0$, applied to the morphism $C \to X$; both are stated for an ample divisor $H$ on $X$ and the cycle $f_* C$.

*Lemma 6.1.3.* Put $\mathcal{E} = f^* T_X(-B)$, $a = h^0(\mathbb{P}^1, \mathcal{E})$ and $c = h^1(\mathbb{P}^1, \mathcal{E})$, so $a - c = -K_X \cdot f + n - n b$ by Corollary P8.1.12. Let $\mathcal{O}$ be the local ring of $\operatorname{Hom}(\mathbb{P}^1, X; f|_B)$ at $[f]$ and $\hat{\mathcal{O}}$ its completion, which is $k[[t_1, \dots, t_a]]/(F_1, \dots, F_c)$ by Theorem P8.1.10. In the regular local ring $k[[t_1, \dots, t_a]]$ every minimal prime $\mathfrak{q}$ over $(F_1, \dots, F_c)$ has height at most $c$ by Krull's height theorem, so $\dim \hat{\mathcal{O}}/\mathfrak{q} \ge a - c$, since a regular local ring is catenary and every maximal chain of primes has length $a$. An irreducible component $Z$ through $[f]$ corresponds to a minimal prime $\mathfrak{p}$ of $\mathcal{O}$, and $\dim Z = \dim \mathcal{O}/\mathfrak{p}$, since $Z$ is a variety of finite type over $k$ and $[f]$ a closed point. The map $\mathcal{O} \to \hat{\mathcal{O}}$ is faithfully flat, so by going down every minimal prime of $\hat{\mathcal{O}}$ over $\mathfrak{p} \hat{\mathcal{O}}$ is a minimal prime of $\hat{\mathcal{O}}$, and $\dim \mathcal{O}/\mathfrak{p} = \dim \hat{\mathcal{O}}/\mathfrak{p} \hat{\mathcal{O}} \ge a - c$. This is the argument of Kol96, Theorem II.1.2.

*Corollary 6.1.4.* Let $f \colon \mathbb{P}^1 \to \Gamma$ be the normalization, so $[f] = [\Gamma]$. By part 2 of Theorem 6.1.2 with $b = 2$,
$$\dim_{[f]} \operatorname{Hom}(\mathbb{P}^1, X; f|_{\{0, \infty\}}) \ge -K_X \cdot \Gamma + n - 2n = -K_X \cdot \Gamma - n \ge 2,$$
and part 3 gives $\Gamma \equiv Z_1 + Z_2$. If $\Gamma'$ is a component of $Z_1$, then $H \cdot \Gamma = H \cdot Z_1 + H \cdot Z_2 \ge H \cdot \Gamma' + H \cdot Z_2 > H \cdot \Gamma'$, since $H$ is positive on every curve and $Z_2 \ne 0$.

*Lemma 6.1.6.* Suppose $[\Gamma] = [Z_1] + [Z_2]$ with $Z_1$, $Z_2$ nonzero rational $1$-cycles. Every component $\Gamma'$ of $Z_1$ or $Z_2$ has $[\Gamma'] \in \overline{NE}(X)$, and $[\Gamma]$ is a sum of positive multiples of these classes. Since $R$ is a face of $\overline{NE}(X)$ (Definition P7.4.1), a sum of elements of $\overline{NE}(X)$ that lies in $R$ has all its summands in $R$, so $[\Gamma'] \in R$ for every component $\Gamma'$. As $R$ is $K_X$-negative, $-K_X \cdot \Gamma' > 0$, and $-K_X \cdot \Gamma'$ is an integer, so $-K_X \cdot \Gamma' \ge 1$ and $-K_X \cdot \Gamma' \ge \ell(R)$ by minimality. Then $\ell(R) = -K_X \cdot \Gamma = -K_X \cdot Z_1 - K_X \cdot Z_2 \ge 2 \ell(R)$, which is impossible since $\ell(R) \ge 1$. A family whose members are birational onto curves of class $[\Gamma]$ has class $[\Gamma]$.

*Corollary 6.1.7.* If a component through $[f]$ had dimension at least $2$, then $\dim_{[f]} \operatorname{Hom}(\mathbb{P}^1, X; f|_{\{0, \infty\}}) \ge 2$ and part 3 of Theorem 6.1.2 would split $[f]$. By Lemma 6.1.3 with $b = 2$, every such component has dimension at least $-K_X \cdot f - n$, so $-K_X \cdot f - n \le 1$.

### Exercises

1. (A) Show that the class of a rational curve $\Gamma$ with $H \cdot \Gamma = 1$ for some ample divisor $H$ is unsplit, and deduce from Corollary 6.1.7 that $-K_X \cdot \Gamma \le n + 1$.
2. (A) Let $X = \mathbb{P}^1 \times \mathbb{P}^1$ and $\Gamma$ the diagonal. Compute $-K_X \cdot \Gamma$ and check that Corollary 6.1.4 applies. Exhibit the decomposition $[\Gamma] = [\ell_1] + [\ell_2]$ as a degeneration of curves of class $(1, 1)$ through two fixed points.
3. (B) Let $\nu \colon \mathbb{P}^1 \to \Gamma$ be the normalization of a rational curve and $f = \nu \circ g$ with $g \colon \mathbb{P}^1 \to \mathbb{P}^1$ of degree $d \ge 2$. Show that $[f] = d [\Gamma]$ is not unsplit, and check directly that $\dim_{[f]} \operatorname{Hom}(\mathbb{P}^1, X; f|_{\{0, \infty\}}) \ge 2$: the morphisms $\nu \circ g'$ with $g'$ of degree $d$, $g'(0) = g(0)$ and $g'(\infty) = g(\infty)$ form a family of dimension $2d - 1$ (Example P8.1.7).
4. (B) In Lemma 6.1.3, take $X = \mathbb{P}^2$, $B = \emptyset$ and $f$ the normalization of a nodal cubic. Compute $a$ and $c$ and check that the component through $[f]$ has dimension exactly $a - c$.
5. (B) Show that Lemma 6.1.6 needs the ray to be extremal. On $X = \mathbb{P}^1 \times \mathbb{P}^2$, the ray $R$ spanned by $[\ell_1] + [\ell_2]$ is $K_X$-negative and contains the class of a rational curve. Find the minimal value of $-K_X \cdot \Gamma$ over rational curves $\Gamma$ with $[\Gamma] \in R$, and show that a curve attaining it is not unsplit.
6. (C) Let $V$ be an unsplit family with $-K_X \cdot V = n + 1$. Use Corollary 6.1.7 and Lemma 6.1.3 to show that for every member $f$ the scheme $\operatorname{Hom}(\mathbb{P}^1, X; f|_{\{0, \infty\}})$ has dimension exactly $1$ at $[f]$, and that the members of $V$ through two fixed general points of $\operatorname{Locus}(V)$ form finitely many $\mathbb{G}_m$-orbits.

### Lean

The library has the vocabulary of curves and extremal rays: `MinimalModel.Curve.IsRational` and `MinimalModel.ExtremalRay` in the project library. It has no Hom schemes and no families of curves, so Theorem 6.1.2, Lemma 6.1.3, Corollary 6.1.4, Lemma 6.1.6 and Corollary 6.1.7 are not yet in Lean.

### Notes and history

The dimension estimate and bend-and-break are due to Mori (Mor79, Mor82), who introduced them to prove Hartshorne's conjecture that a smooth projective variety with ample tangent bundle is a projective space. The form of Lemma 6.1.3 for every component is Kol96, Theorem II.1.2, and Debarre's book proves it in Chapter 2 (Deb01). The term unsplit and the systematic use of Corollary 6.1.7 come from the work on Fano manifolds in the 1990s; Kol96, Chapter IV.2, and Deb01, Chapter 5, use it in the same way.
