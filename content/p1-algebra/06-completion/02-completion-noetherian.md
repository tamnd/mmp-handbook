---
title: Completion of Noetherian rings
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
## Completion of Noetherian rings

### Statement

Throughout, $A$ is a Noetherian ring, $I$ an ideal and $\hat{\ }$ the $I$-adic completion.

**Theorem P1.6.12 (completion is exact).** Let $0 \to M' \to M \to M'' \to 0$ be an exact sequence of finitely generated $A$-modules. Then
$$
0 \to \hat{M}' \to \hat{M} \to \hat{M}'' \to 0
$$
is exact.

Lean: Mathlib `AdicCompletion.map_exact`, `AdicCompletion.map_injective` and `AdicCompletion.map_surjective` (proved in Mathlib).

*Proof.* Regard $M'$ as a submodule of $M$. The image of $I^n M$ in $M''$ is $I^n M''$, so for every $n$ the sequence
$$
0 \to M'/(M' \cap I^n M) \to M/I^n M \to M''/I^n M'' \to 0
$$
is exact. The transition maps of the first system are surjective, so by the lemma on exactness of inverse limits (Section 6.1) the limits form an exact sequence $0 \to \varprojlim M'/(M' \cap I^n M) \to \hat{M} \to \hat{M}'' \to 0$. By the Artin-Rees lemma (Lemma P1.5.33) the filtration $M'_n = M' \cap I^n M$ of $M'$ is a stable $I$-filtration: $I M'_n \subseteq M'_{n+1}$ always, and $M'_{n+1} = I^{n+1-c} M'_c = I M'_n$ for $n \geq c$. By the lemma on equivalent filtrations (Section 6.1), $\varprojlim M'/M'_n = \hat{M}'$. $\square$

**Theorem P1.6.13 (completion as a tensor product).** For every finitely generated $A$-module $M$ the natural map
$$
\hat{A} \otimes_A M \to \hat{M}, \qquad \hat{a} \otimes m \mapsto \hat{a} \cdot \hat{m},
$$
is an isomorphism. Here $\hat{m}$ is the image of $m$ in $\hat{M}$.

Lean: Mathlib `AdicCompletion.ofTensorProduct_bijective_of_finite_of_isNoetherian` and `AdicCompletion.ofTensorProductEquivOfFiniteNoetherian` (proved in Mathlib).

*Proof.* For $M = A^n$ the map is an isomorphism, since completion commutes with finite direct sums. Choose a presentation $A^m \to A^n \to M \to 0$, which exists since $A$ is Noetherian. The natural maps form a commutative diagram with the two rows
$$
\hat{A} \otimes A^m \to \hat{A} \otimes A^n \to \hat{A} \otimes M \to 0, \qquad \widehat{A^m} \to \widehat{A^n} \to \hat{M} \to 0 .
$$
Both rows are exact: the first because the tensor product is right exact, and the second by the last theorem, applied to $0 \to K \to A^n \to M \to 0$ and to $A^m \to K \to 0$, with $K$ the kernel. The maps from the first row to the second at the first two terms are isomorphisms. So the map at the third term is an isomorphism, since it is the map induced on cokernels. $\square$

**Corollary P1.6.14 (flatness).** The ring $\hat{A}$ is a flat $A$-module.

Lean: Mathlib `AdicCompletion.flat_of_isNoetherian` (instance, proved in Mathlib).

*Proof.* By the ideal criterion (Theorem P1.1.46) it is enough to show that $J \otimes_A \hat{A} \to \hat{A}$ is injective for every ideal $J$. By the last theorem this map is the completion $\hat{J} \to \hat{A}$ of the inclusion $J \to A$, and it is injective by the exactness of completion. $\square$

**Corollary P1.6.15 (quotients and powers).** For every ideal $J$ of $A$, $(A/J)^{\wedge} = \hat{A}/J\hat{A}$. Also $\hat{A}/I^n \hat{A} \cong A/I^n$, the ideal $I^n \hat{A}$ is the kernel of $\hat{A} \to A/I^n$, the ring $\hat{A}$ is $I\hat{A}$-adically complete, and $I\hat{A} \subseteq \operatorname{Jac}(\hat{A})$.

Lean: Mathlib `AdicCompletion.isAdicComplete` (completeness of the completion for a finitely generated ideal, proved in Mathlib).

*Proof.* The first claim is the tensor product theorem for $M = A/J$. For $J = I^n$, the module $A/I^n$ is killed by $I^n$, so its completion is $A/I^n$ itself, and $\hat{A}/I^n\hat{A} \cong A/I^n$ by the first claim. This isomorphism is induced by the map $\hat{A} \to A/I^n$, so $I^n \hat{A}$ is its kernel. Then $\varprojlim \hat{A}/I^n\hat{A} = \varprojlim A/I^n = \hat{A}$, so $\hat{A}$ is complete. For $t \in I\hat{A}$, the series $\sum_{j \geq 0} t^j$ converges in $\hat{A}$, since $t^j \in I^j \hat{A}$, and it is an inverse of $1 - t$. So $1 - t$ is a unit for every $t \in I\hat{A}$, which means $I\hat{A} \subseteq \operatorname{Jac}(\hat{A})$. $\square$

**Theorem P1.6.16 (the completion is Noetherian).** Let $I = (a_1, \dots, a_s)$. There is a surjective ring homomorphism $A[[x_1, \dots, x_s]] \to \hat{A}$ with $x_i \mapsto a_i$. In particular $\hat{A}$ is Noetherian.

Lean: not in Lean.

*Proof.* For a power series $F = \sum_\alpha c_\alpha x^\alpha$ with $c_\alpha \in A$, let $\Phi(F)$ be the sequence whose $n$-th term is the class of $\sum_{|\alpha| < n} c_\alpha a^\alpha$ in $A/I^n$. The terms are compatible, since $a^\alpha \in I^n$ for $|\alpha| \geq n$. The map $\Phi$ is a ring homomorphism, since modulo $I^n$ the product of two truncated series only depends on the terms of degree less than $n$.

For the surjectivity, let $y \in \hat{A}$ have components $\bar{y}_n \in A/I^n$. Choose lifts $y_n \in A$ of $\bar{y}_n$. Then $y_{n+1} - y_n \in I^n$, so it can be written as a form $\sum_{|\alpha| = n} c_\alpha a^\alpha$ of degree $n$ in the $a_i$, with $c_\alpha \in A$. Take $c_0 = y_1$ in degree $0$, and let $F = \sum_\alpha c_\alpha x^\alpha$. The truncation of $F$ in degrees less than $n$ maps to $y_1 + \sum_{j=1}^{n-1}(y_{j+1} - y_j) = y_n$, so $\Phi(F) = y$.

The ring $A[[x_1, \dots, x_s]] = A[[x_1, \dots, x_{s-1}]][[x_s]]$ is Noetherian by Remark P1.3.13 and induction on $s$, so its quotient $\hat{A}$ is Noetherian. $\square$

This theorem gives the general statement promised in Remark P1.3.13: the power series ring $A[[x_1, \dots, x_n]]$ is the completion of $A[x_1, \dots, x_n]$ along $(x_1, \dots, x_n)$ (Section 6.1), and the completion of every Noetherian ring along every ideal is Noetherian.

**Corollary P1.6.17 (power series are flat).** The ring $A[[x_1, \dots, x_n]]$ is flat over $A[x_1, \dots, x_n]$ and over $A$.

Lean: not in Lean in this form.

*Proof.* The ring $A[x_1, \dots, x_n]$ is Noetherian, and $A[[x_1, \dots, x_n]]$ is its completion, so it is flat over it by the flatness corollary. A polynomial ring is free, hence flat, over $A$, and a composite of flat maps is flat. $\square$

**Theorem P1.6.18 (completion of a local ring).** Let $(A, \mathfrak{m}, k)$ be a Noetherian local ring and $\hat{A}$ its $\mathfrak{m}$-adic completion.

1. $\hat{A}$ is a Noetherian local ring with maximal ideal $\mathfrak{m}\hat{A}$ and residue field $k$, and it is $\mathfrak{m}\hat{A}$-adically complete.
2. $\hat{A}$ is faithfully flat over $A$. The map $A \to \hat{A}$ is injective, and $J\hat{A} \cap A = J$ for every ideal $J$.
3. The rings $A$ and $\hat{A}$ have the same Hilbert-Samuel function, the same dimension, the same multiplicity and the same embedding dimension: $\dim_k \mathfrak{m}/\mathfrak{m}^2 = \dim_k \mathfrak{m}\hat{A}/\mathfrak{m}^2\hat{A}$.

Lean: Mathlib has the instance `IsLocalRing (AdicCompletion (maximalIdeal R) R)`, and `AdicCompletion.maximalIdeal_eq_map`, `AdicCompletion.residueField_map_bijective` and `AdicCompletion.spanFinrank_maximalIdeal_eq` (proved in Mathlib); the faithful flatness and the dimension are not in Lean in this form.

*Proof.* (1) By the last corollaries, $\hat{A}$ is Noetherian, complete, and $\hat{A}/\mathfrak{m}\hat{A} \cong A/\mathfrak{m} = k$ is a field, so $\mathfrak{m}\hat{A}$ is a maximal ideal. It lies in $\operatorname{Jac}(\hat{A})$, so it is in every maximal ideal, and it is the only one.

(2) The map is flat, and $\mathfrak{m}\hat{A} \neq \hat{A}$, so it is faithfully flat by Proposition P1.1.53. For an ideal $J$, the map $A/J \to (A/J)^{\wedge} = \hat{A}/J\hat{A}$ is injective by the Krull intersection theorem for the local ring $A/J$ (Section 6.1). Its kernel is $(J\hat{A} \cap A)/J$, so $J\hat{A} \cap A = J$. For $J = 0$ this is the injectivity of $A \to \hat{A}$.

(3) For every $n$, $\hat{A}/(\mathfrak{m}\hat{A})^n = \hat{A}/\mathfrak{m}^n\hat{A} \cong A/\mathfrak{m}^n$. On a module killed by $\mathfrak{m}^n\hat{A}$ the action of $\hat{A}$ factors through $\hat{A}/\mathfrak{m}^n\hat{A}$, which is the image of $A$, so the $\hat{A}$-submodules and the $A$-submodules are the same, and lengths agree. So $\ell_{\hat{A}}(\hat{A}/\mathfrak{m}^n\hat{A}) = \ell_A(A/\mathfrak{m}^n)$ for all $n$, and the dimension theorem (Theorem P1.5.35) gives $\dim \hat{A} = \dim A$. The multiplicities agree for the same reason. For the embedding dimension, $\mathfrak{m}\hat{A}/\mathfrak{m}^2\hat{A}$ is the maximal ideal of $\hat{A}/\mathfrak{m}^2\hat{A} \cong A/\mathfrak{m}^2$, which is $\mathfrak{m}/\mathfrak{m}^2$. $\square$

### Proof in words

Three facts carry the section. First, completion is exact on finitely generated modules: the Artin-Rees lemma says that the topology that $M$ induces on a submodule $M'$ is the $I$-adic topology of $M'$, and inverse limits are exact when the maps on the left are surjective. Second, an exact functor that agrees with $\hat{A} \otimes_A -$ on free modules agrees with it on all finitely presented modules, so $\hat{M} = \hat{A} \otimes_A M$, and the exactness of completion becomes the flatness of $\hat{A}$. Third, every element of $\hat{A}$ is a power series in the generators of $I$, so $\hat{A}$ is a quotient of a power series ring, which is Noetherian.

For a local ring the completion is again local, with the same residue field and the same quotients $A/\mathfrak{m}^n$. Everything that the quotients $A/\mathfrak{m}^n$ see, such as the Hilbert-Samuel function, the dimension and the embedding dimension, is the same for $A$ and $\hat{A}$. Faithful flatness makes $A$ a subring of $\hat{A}$ in which every ideal is cut out by its extension. In geometric terms, $\operatorname{Spec} \hat{A} \to \operatorname{Spec} A$ is a flat and surjective map from the formal neighbourhood of a point to its Zariski local neighbourhood.

### Examples

**Example P1.6.19 (hypersurface singularities).** Let $R = k[x_1, \dots, x_n]_{(x_1, \dots, x_n)}$ and $f \in R$ with $f(0) = 0$. The completion of $A = R/(f)$ is $k[[x_1, \dots, x_n]]/(f)$, by the corollary on quotients and Section 6.1. So the completion of the local ring of the node is $k[[x, y]]/(y^2 - x^2 - x^3)$, and that of the cusp is $k[[x, y]]/(y^2 - x^3)$. If $\operatorname{char} k \neq 2$, Section 6.3 shows that the first is isomorphic to $k[[s, t]]/(st)$, which is not a domain, while the local ring of the node is a domain.

**Example P1.6.20 ($p$-adic integers).** The $p$-adic completion of the local ring $\mathbb{Z}_{(p)}$ is $\mathbb{Z}_p$, since $\mathbb{Z}_{(p)}/p^n = \mathbb{Z}/p^n$. So $\mathbb{Z}_p$ is faithfully flat over $\mathbb{Z}_{(p)}$, both are local of dimension $1$, and $p^n \mathbb{Z}_p \cap \mathbb{Z}_{(p)} = p^n \mathbb{Z}_{(p)}$.

**Example P1.6.21 (the tensor product theorem fails for modules that are not finitely generated).** Let $A = k[x]_{(x)}$ and $M = k(x)$, its fraction field. Then $xM = M$, so $M/x^n M = 0$ and $\hat{M} = 0$. On the other hand $\hat{A} \otimes_A M = k[[x]] \otimes_{k[x]_{(x)}} k(x)$ is the localization of $k[[x]]$ at the nonzero elements of $A$, which is the field $k((x))$ of Laurent series, since $x$ becomes invertible. So $\hat{A} \otimes_A M \neq \hat{M}$.

**Example P1.6.22 (an injection whose completion is not injective).** Let $A = k[x]$, $I = (x)$, and consider the injection $A \to A$, multiplication by $x$. Its completion is multiplication by $x$ on $k[[x]]$, which is injective, as the theorem says. The localization map $A \to A_x = k[x, x^{-1}]$ is injective, but $A_x$ is not finitely generated, $x A_x = A_x$, and the completion of $A_x$ is $0$. So completion does not preserve injections of modules that are not finitely generated.

### Exercises

1. (A) Let $(A, \mathfrak{m})$ be a Noetherian local ring. Show that $\hat{A} = A$ if $A$ is Artinian.
2. (A) Let $(A, \mathfrak{m})$ be a Noetherian local ring. Show that $x \in A$ is a nonzerodivisor on $A$ if and only if it is a nonzerodivisor on $\hat{A}$. (Hint: flatness for one direction and the injectivity of $A \to \hat{A}$ for the other.)
3. (A) Show that if $\hat{A}$ is a domain, then $A$ is a domain. Section 6.3 shows that the converse fails.
4. (B) Show that $k[[x, y]]/(y^2 - x^3)$ is isomorphic to the subring $k[[t^2, t^3]]$ of $k[[t]]$. (Hint: every element of the quotient has the form $a(x) + y\, b(x)$.)
5. (B) Let $(A, \mathfrak{m})$ be a Noetherian local ring and $M$ a finitely generated module. Show that $M = 0$ if and only if $\hat{M} = 0$, and that $\ell_A(M) = \ell_{\hat{A}}(\hat{M})$ if $M$ has finite length.
6. (B) Let $A$ be Noetherian and $J$ an ideal. Show that $A[[x]]/JA[[x]] \cong (A/J)[[x]]$. With the flatness of power series, this supplies the facts used in Exercise 8 of Section 5.4.
7. (B) Let $(A, \mathfrak{m})$ be a Noetherian local ring. Show that $\hat{A}$ is $\mathfrak{m}$-adically complete as an $A$-module and that $\hat{\hat{A}} = \hat{A}$. Show that an ideal $\mathfrak{q}$ of $A$ is $\mathfrak{m}$-primary if and only if $\mathfrak{q}\hat{A}$ is $\mathfrak{m}\hat{A}$-primary.
8. (C) In the theorem on the Noetherian property, show that the kernel of $A[[x_1, \dots, x_s]] \to \hat{A}$ is $(x_1 - a_1, \dots, x_s - a_s)$. (Hint: let $B = A[[x_1, \dots, x_s]]$ and $K = (x_1 - a_1, \dots, x_s - a_s)$. Show that $B/K$ is complete for the $(x)$-adic topology, which on $B/K$ is the $I$-adic topology, and that $B/(K + (x)^n) \cong A/I^n$.)

### Lean

Mathlib proves the exactness of adic completion on finite modules over a Noetherian ring as `AdicCompletion.map_exact`, the tensor product formula as `AdicCompletion.ofTensorProductEquivOfFiniteNoetherian`, and the flatness of the completion as the instance `AdicCompletion.flat_of_isNoetherian`. For a Noetherian local ring it proves that the completion is local, with the extended maximal ideal and the same residue field, and with the same minimal number of generators of the maximal ideal. The Noetherian property of the completion, the faithful flatness and the equality of dimensions are not yet in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

Krull and Chevalley developed the theory of the completion of a local ring in the 1930s and 1940s. Zariski used completions to define analytic irreducibility and to compare the algebraic and the formal local rings of a variety, and Serre's GAGA of 1956 compared both with the analytic local ring. The proofs here are the ones of Atiyah-Macdonald, Chapter 10, except the proof of the Noetherian property, which uses power series as in Eisenbud, Chapter 7. The literature state of every result here is theorem. The section follows Atiyah-Macdonald, Chapter 10, Matsumura, Chapter 3, and Eisenbud, Chapter 7.
