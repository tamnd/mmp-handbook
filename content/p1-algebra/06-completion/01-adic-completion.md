---
title: Inverse limits, adic completion and the Krull intersection theorem
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch10, Mat86:ch3, Eis95:ch7]
requires: [P1.1, P1.3, P1.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Inverse limits, adic completion and the Krull intersection theorem

### Statement

**Definition P1.6.1 (inverse system and inverse limit).** An *inverse system* of $A$-modules is a sequence of modules $M_1, M_2, \dots$ with linear maps $\theta_{n}: M_{n+1} \to M_n$. Its *inverse limit* is the submodule
$$
\varprojlim M_n = \{(x_n) \in \textstyle\prod_n M_n : \theta_n(x_{n+1}) = x_n \text{ for all } n\}
$$
of the product, the sequences that are compatible under the maps. A map of inverse systems $(M'_n) \to (M_n)$ is a family of linear maps $M'_n \to M_n$ that commute with the $\theta_n$, and it induces a map of inverse limits. If every $M_n$ is a ring and every $\theta_n$ a ring homomorphism, the inverse limit is a ring.

Lean: Mathlib defines the completion directly as `AdicCompletion` (definition), a submodule of the product as here.

**Lemma P1.6.2 (exactness of inverse limits).** Let $0 \to (M'_n) \to (M_n) \to (M''_n) \to 0$ be a sequence of maps of inverse systems that is exact at every $n$. Then
$$
0 \to \varprojlim M'_n \to \varprojlim M_n \to \varprojlim M''_n
$$
is exact. If every map $\theta'_n: M'_{n+1} \to M'_n$ is surjective, then $\varprojlim M_n \to \varprojlim M''_n$ is surjective.

Lean: not in Lean in this form; Mathlib proves exactness of adic completion directly, as `AdicCompletion.map_exact`.

*Proof.* Exactness on the left is clear, since the limit is a submodule of the product and the product of exact sequences is exact. For the surjectivity, let $(z_n) \in \varprojlim M''_n$. Choose $y_1 \in M_1$ over $z_1$. Suppose $y_n \in M_n$ maps to $z_n$. Choose any $y \in M_{n+1}$ over $z_{n+1}$. Then $\theta_n(y) - y_n$ maps to $z_n - z_n = 0$, so it equals the image of some $x \in M'_n$. Since $\theta'_n$ is surjective, $x = \theta'_n(x')$ for some $x' \in M'_{n+1}$. Put $y_{n+1} = y - x'$. Then $y_{n+1}$ maps to $z_{n+1}$ and $\theta_n(y_{n+1}) = y_n$. The sequence $(y_n)$ lies in $\varprojlim M_n$ and maps to $(z_n)$. $\square$

**Definition P1.6.3 (adic completion).** Let $I$ be an ideal of $A$ and $M$ an $A$-module. The modules $M/I^n M$ with the quotient maps $M/I^{n+1}M \to M/I^n M$ form an inverse system. The *$I$-adic completion* of $M$ is
$$
\hat{M} = \varprojlim M/I^n M .
$$
The maps $M \to M/I^n M$ give a natural map $M \to \hat{M}$, with kernel $\bigcap_n I^n M$. The module $M$ is *separated* if this kernel is $0$, and *complete* if the map is an isomorphism. The completion $\hat{A}$ is a ring, and $\hat{M}$ is an $\hat{A}$-module.

Lean: Mathlib `AdicCompletion`, `IsHausdorff`, `IsPrecomplete` and `IsAdicComplete` (definitions); Mathlib says Hausdorff for separated.

The completion has a topological meaning. The sets $x + I^n M$ form a basis of a topology on $M$, the *$I$-adic topology*. It is Hausdorff exactly when $M$ is separated. A sequence $(x_k)$ is Cauchy if for every $n$ the classes of $x_k$ in $M/I^n M$ are constant for large $k$, and $\hat{M}$ is the module of Cauchy sequences modulo null sequences. Concretely, an element of $\hat{M}$ is a series $\sum_{j \geq 0} m_j$ with $m_j \in I^j M$: its image in $M/I^n M$ is the finite sum $\sum_{j < n} m_j$.

**Definition P1.6.4 (stable filtration).** A *filtration* of $M$ is a chain of submodules $M = M_0 \supseteq M_1 \supseteq \dots$. It is an *$I$-filtration* if $I M_n \subseteq M_{n+1}$ for all $n$, and *stable* if in addition $I M_n = M_{n+1}$ for all large $n$.

Lean: Mathlib `Ideal.Filtration` and `Ideal.Filtration.Stable` (definitions).

**Lemma P1.6.5 (equivalent filtrations).** Let $(M_n)$ and $(M'_n)$ be filtrations of $M$ such that for every $n$ there are $a$ and $b$ with $M_a \subseteq M'_n$ and $M'_b \subseteq M_n$. Then $\varprojlim M/M_n \cong \varprojlim M/M'_n$, compatibly with the maps from $M$. Every stable $I$-filtration $(M_n)$ satisfies $I^n M \subseteq M_n$ and $M_{n + c} = I^n M_c \subseteq I^n M$ for some $c$, so it defines the $I$-adic completion.

Lean: not in Lean in this form.

*Proof.* Let $(x_n) \in \varprojlim M/M_n$. For each $n$ choose $a(n) \geq n$ with $M_{a(n)} \subseteq M'_n$, and let $y_n$ be the image of $x_{a(n)}$ in $M/M'_n$. This does not depend on the choice of $a(n)$, since the $x_n$ are compatible, and $(y_n)$ is compatible. The map $(x_n) \mapsto (y_n)$ and the map in the other direction are inverse to each other. For a stable filtration, $I^n M = I^n M_0 \subseteq M_n$ by induction, and if $I M_n = M_{n+1}$ for $n \geq c$, then $M_{n+c} = I^n M_c$. $\square$

**Theorem P1.6.6 (Krull's intersection theorem).** Let $A$ be a Noetherian ring, $I$ an ideal, $M$ a finitely generated $A$-module and $N = \bigcap_n I^n M$. Then $IN = N$, and there is $a \in I$ with $(1 - a) N = 0$. In particular:

1. if $I \subseteq \operatorname{Jac}(A)$, for example if $A$ is local and $I \neq A$, then $M$ is separated: $\bigcap_n I^n M = 0$;
2. if $A$ is a domain and $I \neq A$, then $\bigcap_n I^n = 0$.

Lean: Mathlib `Ideal.iInf_pow_smul_eq_bot_of_le_jacobson`, `Ideal.iInf_pow_eq_bot_of_isLocalRing` and `Ideal.iInf_pow_eq_bot_of_isDomain` (proved in Mathlib).

*Proof.* By the Artin-Rees lemma (Lemma P1.5.33) there is $c$ with $I^n M \cap N = I^{n-c}(I^c M \cap N)$ for $n \geq c$. Since $N \subseteq I^n M$ for every $n$, this reads $N = I^{n-c} N$, and with $n = c + 1$ it gives $N = IN$. The module $N$ is finitely generated, since $A$ is Noetherian, so Corollary P1.1.24 gives $b \equiv 1 \pmod I$ with $bN = 0$; put $a = 1 - b$. In case (1), $1 - a$ is a unit, since $a \in \operatorname{Jac}(A)$, so $N = 0$; or directly, Nakayama's lemma applies to $IN = N$. In case (2), take $M = A$. Then $(1 - a) N = 0$ with $1 - a \neq 0$, since $a \in I \neq A$, so $N = 0$ in the domain $A$. $\square$

**Proposition P1.6.7 (power series are complete).** Let $A$ be a ring and $B = A[[x_1, \dots, x_n]]$ with $J = (x_1, \dots, x_n)$. Then $B$ is $J$-adically separated and complete, and it is the $J$-adic completion of $A[x_1, \dots, x_n]$.

Lean: Mathlib `MvPowerSeries.toAdicCompletionAlgEquiv` (the isomorphism with the completion of the polynomial ring, for finitely many variables), with `IsAdicComplete` instances for `MvPowerSeries` and `PowerSeries` (proved in Mathlib).

*Proof.* The ideal $J^k$ of $B$ is the set of series whose terms all have degree at least $k$: such a series is a finite sum $\sum_{|\alpha| = k} x^\alpha g_\alpha$, by grouping its terms by a monomial of degree $k$ that divides them. So $B/J^k B$ is the module of polynomials of degree less than $k$, the same as $A[x]/(x)^k$ with $x = (x_1, \dots, x_n)$. A compatible sequence of truncations is a power series, and a power series is determined by its truncations, so $B = \varprojlim B/J^k = \varprojlim A[x]/(x)^k$. $\square$

### Proof in words

The completion of $M$ along $I$ is the module of all formal series $\sum m_j$ with $m_j \in I^j M$, or equivalently of all compatible systems of approximations modulo $I^n M$. For the ideal of a point, an element of the completion is a Taylor series at the point, and $M/I^n M$ is the module of Taylor expansions of order $n - 1$. Inverse limits are exact on the left. They are exact on the right when the transition maps of the kernels are surjective, because then a compatible sequence can be lifted one step at a time.

The Krull intersection theorem says that, in the Noetherian case, the natural map to the completion is injective on finitely generated modules over a local ring. A function on a variety that vanishes to infinite order at a point is zero near the point. The proof uses the Artin-Rees lemma: the intersection $N$ of all $I^n M$ satisfies $N = IN$, and Nakayama's lemma then kills it. In the world of smooth functions the statement is false, and the Noetherian hypothesis is the difference.

### Examples

**Example P1.6.8 (Taylor series at a point).** Let $A = k[x_1, \dots, x_n]$ and $\mathfrak{m} = (x_1, \dots, x_n)$, the ideal of the origin. By the last proposition, $\hat{A} = k[[x_1, \dots, x_n]]$. The local ring $A_{\mathfrak{m}}$ has the same completion with respect to $\mathfrak{m}A_{\mathfrak{m}}$, since $A_{\mathfrak{m}}/\mathfrak{m}^n A_{\mathfrak{m}} = A/\mathfrak{m}^n$: the ring $A/\mathfrak{m}^n$ is local with maximal ideal $\mathfrak{m}/\mathfrak{m}^n$, so it is its own localization. The map $A_{\mathfrak{m}} \to k[[x_1, \dots, x_n]]$ sends a rational function $f/g$ with $g(0) \neq 0$ to its Taylor series at the origin, and it is injective by the Krull intersection theorem.

**Example P1.6.9 (the $p$-adic integers).** Let $p$ be a prime number. The $(p)$-adic completion of $\mathbb{Z}$ is the ring $\mathbb{Z}_p = \varprojlim \mathbb{Z}/p^n$ of $p$-adic integers. An element is a series $\sum_{j \geq 0} c_j p^j$ with digits $c_j \in \{0, \dots, p - 1\}$, and every element has exactly one such expansion. For example $-1 = \sum_{j \geq 0} (p - 1) p^j$, since $1 + \sum_{j < n} (p - 1) p^j = p^n \equiv 0 \pmod{p^n}$. An integer $m$ prime to $p$ is a unit in every $\mathbb{Z}/p^n$, so it is a unit in $\mathbb{Z}_p$, and $\mathbb{Z}_{(p)} \subseteq \mathbb{Z}_p$. The ring $\mathbb{Z}_p$ is a discrete valuation ring with maximal ideal $p \mathbb{Z}_p$ (Exercise 4 and Chapter 7).

**Example P1.6.10 (a smooth function that is flat at a point).** Let $A$ be the ring of germs at $0$ of smooth functions $\mathbb{R} \to \mathbb{R}$. It is a local ring with maximal ideal $\mathfrak{m}$ of the germs that vanish at $0$, and $\mathfrak{m} = (x)$ by Hadamard's lemma: $f(x) - f(0) = x \int_0^1 f'(tx) \, dt$. The germ $f(x) = e^{-1/x^2}$, with $f(0) = 0$, has all derivatives zero at $0$, and the same argument applied $n$ times shows $f = x^n g_n$ with $g_n$ smooth. So $0 \neq f \in \bigcap_n \mathfrak{m}^n$, and the Krull intersection theorem fails. The ring $A$ is not Noetherian. Its completion is $\mathbb{R}[[x]]$, and the map $A \to \mathbb{R}[[x]]$, the Taylor series, is surjective by Borel's theorem but not injective.

**Example P1.6.11 (the theorem fails outside the Jacobson radical).** Let $A = k[x]$, $I = (x)$ and $M = A/(x - 1)$. Then $x$ acts on $M \cong k$ as $1$, so $IM = M$ and $\bigcap_n I^n M = M \neq 0$. Here $a = x$ satisfies $(1 - a) M = 0$, as the theorem says. Geometrically, $M$ lives at the point $x = 1$, away from $V(I)$, and the completion along $V(I)$ does not see it: $\hat{M} = 0$.

### Exercises

1. (A) Show that $1 - x$ is a unit in $k[[x]]$ with inverse $\sum x^j$, and that $f \in A[[x]]$ is a unit if and only if its constant term is a unit in $A$. Deduce that $k[[x_1, \dots, x_n]]$ is a local ring.
2. (A) Find the first four $3$-adic digits of $1/2$ and of $-1/2$ in $\mathbb{Z}_3$.
3. (A) Let $I$ and $J$ be ideals with $I^r \subseteq J \subseteq I$ for some $r$. Show that the $I$-adic and the $J$-adic completions of a module agree. Deduce that the completion of a Noetherian ring along $I$ depends only on $\sqrt{I}$.
4. (A) Show that $\mathbb{Z}_p$ is a domain, that $\mathbb{Z}_p/p^n \mathbb{Z}_p \cong \mathbb{Z}/p^n$, and that every nonzero element of $\mathbb{Z}_p$ has the form $u p^n$ with $u$ a unit. Deduce that $\mathbb{Z}_p$ is a local principal ideal domain.
5. (B) Let $A = k[x]$ and $I = (x(x - 1))$. Show that $\hat{A} \cong k[[x]] \times k[[x - 1]]$. (Hint: the Chinese remainder theorem for $(x^n)$ and $((x-1)^n)$.) Interpret the result: $V(I)$ is two points.
6. (B) Let $n \geq 2$. Show that the $(n)$-adic completion of $\mathbb{Z}$ is $\prod_{p \mid n} \mathbb{Z}_p$.
7. (B) Complete the details of the example of the flat function: show $e^{-1/x^2} = x^n g_n$ with $g_n$ smooth, and show that $x \notin \mathfrak{m}^2$, so that the failure does not come from $\mathfrak{m}^2 = \mathfrak{m}$.
8. (C) Let $A$ be Noetherian, $I$ an ideal and $M$ finitely generated. Show that $\bigcap_n I^n M$ is the set of $m \in M$ that are killed by some element of $1 + I$. Deduce that $\bigcap_n I^n M$ is the kernel of $M \to \prod_{\mathfrak{m} \supseteq I} M_{\mathfrak{m}}$, the product over the maximal ideals that contain $I$.

### Lean

Mathlib defines `AdicCompletion I M` as the submodule of compatible sequences in $\prod_n M/I^n M$, with the classes `IsHausdorff`, `IsPrecomplete` and `IsAdicComplete`. It proves the Krull intersection theorem in three forms, `Ideal.iInf_pow_smul_eq_bot_of_le_jacobson`, `Ideal.iInf_pow_eq_bot_of_isLocalRing` and `Ideal.iInf_pow_eq_bot_of_isDomain`, through the Artin-Rees lemma `Ideal.exists_pow_inf_eq_pow_smul` and stable filtrations `Ideal.Filtration.Stable`. The $p$-adic integers are `PadicInt`, defined as a subring of the $p$-adic numbers rather than as an inverse limit. The handbook adds no `MinimalModel` node here.

### Notes and history

Hensel introduced the $p$-adic numbers in 1897, by analogy with power series expansions of algebraic functions. The intersection theorem is due to Krull. The proof here, through the Artin-Rees lemma, is the one of Atiyah-Macdonald, Chapter 10. The example of the flat function goes back to Cauchy. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 10, Matsumura, Chapter 3, and Eisenbud, Chapter 7.
