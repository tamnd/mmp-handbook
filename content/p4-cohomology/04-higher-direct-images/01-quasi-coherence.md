---
title: Quasi-coherence of higher direct images
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:III.8, Vak25:ch18]
requires: [P2.4, P2.7, P3.4, P3.5, P4.1, P4.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Quasi-coherence of higher direct images

### Statement

Let $f \colon X \to Y$ be a morphism of schemes and $\mathcal{F}$ an $\mathcal{O}_X$-module. The higher direct images $R^q f_* \mathcal{F}$ are the right derived functors of $f_*$ (Definition P2.7.1). By part 4 of Theorem P2.7.11 they may be computed in $\mathsf{Mod}(\mathcal{O}_X)$ or in $\mathsf{Ab}(X)$, they are $\mathcal{O}_Y$-modules, and by part 4 of Theorem P2.7.3, $R^q f_* \mathcal{F}$ is the sheafification of the presheaf $V \mapsto H^q(f^{-1}(V), \mathcal{F})$. In particular $(R^q f_* \mathcal{F})|_V = R^q (f|_{f^{-1}V})_* (\mathcal{F}|_{f^{-1}V})$ for every open $V \subseteq Y$.

**Theorem P4.4.1 (quasi-coherence of higher direct images).** Let $f \colon X \to Y$ be quasi-compact and separated, and $\mathcal{F}$ a quasi-coherent sheaf on $X$. Then $R^q f_* \mathcal{F}$ is quasi-coherent for every $q \geq 0$, and for every affine open $V = \operatorname{Spec} A \subseteq Y$ there is a natural isomorphism
$$(R^q f_* \mathcal{F})|_V \cong H^q(f^{-1}(V), \mathcal{F})^\sim$$
of $\mathcal{O}_V$-modules, with $H^q(f^{-1}(V), \mathcal{F})$ an $A$-module through $A \to \Gamma(f^{-1}V, \mathcal{O}_X)$.

Lean: not in Lean as stated.

**Corollary P4.4.2 (first consequences).** Let $f \colon X \to Y$ and $\mathcal{F}$ be as in Theorem P4.4.1.

1. If $Y = \operatorname{Spec} A$ is affine, then $H^q(X, \mathcal{F}) \cong \Gamma(Y, R^q f_* \mathcal{F})$ and $R^q f_* \mathcal{F} \cong H^q(X, \mathcal{F})^\sim$.
2. If every point of $Y$ has an affine open neighbourhood $V$ such that $f^{-1}(V)$ is covered by $r$ affine open sets, then $R^q f_* \mathcal{F} = 0$ for $q \geq r$. For $\pi \colon \mathbb{P}^n_Y \to Y$ this holds with $r = n + 1$.
3. If $R^q f_* \mathcal{F} = 0$ for all $q > 0$, then $H^q(X, \mathcal{F}) \cong H^q(Y, f_* \mathcal{F})$ for every $q$, and $f_* \mathcal{F}$ is quasi-coherent.

Lean: not in Lean as stated.

**Corollary P4.4.3 (affine morphisms).** Let $f \colon X \to Y$ be an affine morphism and $\mathcal{F}$ a quasi-coherent sheaf on $X$.

1. $R^q f_* \mathcal{F} = 0$ for all $q > 0$.
2. $H^q(X, \mathcal{F}) \cong H^q(Y, f_* \mathcal{F})$ for every $q$, with no hypothesis on $Y$.
3. For every morphism $g \colon Y \to Z$, $R^q (g f)_* \mathcal{F} \cong R^q g_* (f_* \mathcal{F})$ for every $q$.

In particular all three hold for closed immersions and for finite morphisms.

Lean: not in Lean as stated.

Part 2 removes the separatedness of $Y$ from Proposition P4.1.19, as announced there.

### Proof in words

Over an affine open $V$, the preimage $f^{-1}(V)$ is a quasi-compact separated scheme, so its cohomology is the cohomology of a Čech complex of a finite affine cover. Shrinking $V$ to a basic open $D(g)$ shrinks every member of the cover to its locus where $g$ does not vanish, and the sections of a quasi-coherent sheaf there are the localizations at $g$. So the Čech complex over $D(g)$ is the localization of the Čech complex over $V$, and localization is exact, so the cohomology over $D(g)$ is the localization of the cohomology over $V$. This is the defining property of the sheaf $M^\sim$ attached to $M = H^q(f^{-1}V, \mathcal{F})$, and the higher direct image, being the sheafification of $V \mapsto H^q(f^{-1}V, \mathcal{F})$, is that sheaf. For an affine morphism every $f^{-1}(V)$ is affine, so its higher cohomology vanishes by Serre's theorem, and the Leray spectral sequence collapses.

### Examples

**Example P4.4.4 (projective space over a base).** Let $Y$ be a scheme, $r \geq 1$ and $\pi \colon \mathbb{P}^r_Y \to Y$, with $\mathcal{O}(n)$ pulled back from $\mathbb{P}^r_\mathbb{Z}$. Over an affine $V = \operatorname{Spec} A$, Theorem P4.4.1 and Theorem P4.2.1 give
$$\pi_* \mathcal{O}(n)|_V = (A[x_0, \dots, x_r]_n)^\sim, \qquad R^r \pi_* \mathcal{O}(n)|_V \cong \Bigl(\bigoplus_{a} A \, x^{a}\Bigr)^\sim,$$
the second sum over exponent vectors $a$ with all $a_i \leq -1$ and $\sum a_i = n$, and $R^q \pi_* \mathcal{O}(n) = 0$ for $q \neq 0, r$. By the base change part of Theorem P4.2.1 these modules are $A \otimes_\mathbb{Z} H^q(\mathbb{P}^r_\mathbb{Z}, \mathcal{O}(n))$, naturally in $A$, so they glue to $R^q \pi_* \mathcal{O}(n) \cong \mathcal{O}_Y \otimes_\mathbb{Z} H^q(\mathbb{P}^r_\mathbb{Z}, \mathcal{O}(n))$: $\pi_* \mathcal{O}(n)$ is free of rank $\binom{n + r}{r}$ for $n \geq 0$ and $0$ for $n < 0$, and $R^r \pi_* \mathcal{O}(n)$ is free of rank $\binom{-n-1}{r}$ for $n \leq -r - 1$ and $0$ for $n \geq -r$, with $R^r \pi_* \mathcal{O}(-r-1) \cong \mathcal{O}_Y$.

**Example P4.4.5 (the punctured plane).** Let $j \colon U = \mathbb{A}^2_k \setminus \{0\} \to \mathbb{A}^2_k = \operatorname{Spec} k[x, y]$ be the inclusion, quasi-compact and separated. By Example P4.1.12 and part 1 of Corollary P4.4.2,
$$j_* \mathcal{O}_U = \mathcal{O}_{\mathbb{A}^2}, \qquad R^1 j_* \mathcal{O}_U = M^\sim, \quad M = \bigoplus_{a, b \leq -1} k \, x^a y^b,$$
and $R^q j_* \mathcal{O}_U = 0$ for $q \geq 2$ by part 2, since $U = D(x) \cup D(y)$. The module $M$ is not finitely generated, since $x$ and $y$ act surjectively and each element is killed by a power of $(x, y)$. So $R^1 j_* \mathcal{O}_U$ is quasi-coherent, supported at the origin, and not coherent. Theorem P4.4.8 shows that this cannot happen for a projective morphism.

**Example P4.4.6 (a fibre that does not see $R^1$).** Keep $U = \mathbb{A}^2_k \setminus \{0\}$ and let $f \colon U \to \mathbb{A}^1_k = \operatorname{Spec} k[x]$ be the first coordinate, as in Example P4.1.21. By part 1 of Corollary P4.4.2, $R^1 f_* \mathcal{O}_U$ is the sheaf of the $k[x]$-module $M$ of Example P4.4.5. Every element of $M$ is killed by a power of $x$, so $R^1 f_* \mathcal{O}_U$ is supported at the origin of $\mathbb{A}^1_k$, and its stalk there is $M \neq 0$. The fibre $f^{-1}(0) = \operatorname{Spec} k[y, y^{-1}]$ is affine and has no $H^1$, and every other fibre $\{a\} \times \mathbb{A}^1_k$ is affine as well. So $R^1 f_* \mathcal{O}_U$ is not computed by the cohomology of the fibres. Chapter 5 shows that it is when $f$ is flat and proper and the fibre cohomology has constant dimension.

**Example P4.4.7 (the affine line with a doubled origin).** Let $X$ be the line with a doubled origin of Example P4.1.13 and $f \colon X \to \mathbb{A}^1_k$ the morphism that is the identity on both copies. It is quasi-compact but not separated, and Theorem P4.4.1 does not apply as stated. The preimage of every affine open $V \subseteq \mathbb{A}^1_k$ is covered by the two copies of $V$, whose intersection $V \setminus \{0\}$ is affine, so Proposition P4.1.23 still computes $H^q(f^{-1}V, \mathcal{O}_X)$. The Čech complex is $A \oplus A \to A_x$, $(a, b) \mapsto a - b$, which is not surjective onto $A_x$ when $0 \in V$, and the cokernel $A_x / A$ localizes. So $f_* \mathcal{O}_X = \mathcal{O}_{\mathbb{A}^1}$ and $R^1 f_* \mathcal{O}_X = (k[x, x^{-1}]/k[x])^\sim$, a quasi-coherent sheaf supported at $0$.

### Proof

*Theorem P4.4.1.* Let $V = \operatorname{Spec} A \subseteq Y$ be affine and $X_V = f^{-1}(V)$. Since $f$ is quasi-compact, $X_V$ is quasi-compact, and since $f$ and $V \to \operatorname{Spec} \mathbb{Z}$ are separated, $X_V$ is separated by part 2 of Proposition P3.4.9. Choose a finite cover $\mathcal{U} = (U_1, \dots, U_m)$ of $X_V$ by affine open sets. Every finite intersection $U_I = U_{i_0} \cap \dots \cap U_{i_p}$ is affine, so by Corollary P4.1.9,
$$H^q(X_V, \mathcal{F}) \cong H^q(C^\bullet), \qquad C^p = \prod_{i_0 < \dots < i_p} \mathcal{F}(U_{i_0 \cdots i_p}),$$
a complex of $A$-modules. For $g \in A$, $f^{-1}(D(g)) = (X_V)_g$, the locus where the image of $g$ in $\Gamma(X_V, \mathcal{O}_X)$ does not vanish. It is covered by the affine open sets $(U_i)_g$, with intersections $(U_I)_g$, and $\mathcal{F}((U_I)_g) = \mathcal{F}(U_I)_g$ by part 2 of Lemma P3.5.11 applied to the affine scheme $U_I$. So the Čech complex of $(X_V)_g$ for this cover is $C^\bullet \otimes_A A_g$. Localization is exact, so $H^q(C^\bullet \otimes_A A_g) = H^q(C^\bullet)_g$, and Corollary P4.1.9 gives
$$H^q(f^{-1} D(g), \mathcal{F}) \cong H^q(X_V, \mathcal{F})_g,$$
compatibly with the restriction maps for $D(g') \subseteq D(g)$, since restriction of Čech complexes from the cover $(U_i)_g$ to the cover $(U_i)_{g'}$ is the localization map. So on the basis of basic open subsets of $V$ the presheaf $P^q \colon W \mapsto H^q(f^{-1}W, \mathcal{F})$ agrees with the sheaf $M^\sim$, $M = H^q(X_V, \mathcal{F})$, compatibly with restriction. The sheafification of a presheaf is determined by its values on a basis, since its stalks are colimits over basic neighbourhoods, so the sheafification of $P^q|_V$ is $M^\sim$. By part 4 of Theorem P2.7.3, $(R^q f_* \mathcal{F})|_V \cong M^\sim$. The isomorphism does not depend on the cover, since any two finite affine covers have a common refinement and Corollary P4.1.9 is compatible with refinement. Quasi-coherence is local on $Y$ (Corollary P3.5.13). $\square$

*Corollary P4.4.2.* (1) Take $V = Y$ in Theorem P4.4.1, and use $\Gamma(Y, M^\sim) = M$. (2) If $f^{-1}(V)$ is covered by $r$ affine open sets, then $H^q(f^{-1}V, \mathcal{F}) = 0$ for $q \geq r$ by Corollary P4.1.10, so $(R^q f_* \mathcal{F})|_V = 0$. The space $\mathbb{P}^n_V$ is covered by the $n + 1$ affine open sets $D_+(x_i)$. (3) The isomorphism is Corollary P2.4.27(1), and $f_* \mathcal{F}$ is quasi-coherent by part 1 of Theorem P3.5.33 or by the case $q = 0$ of Theorem P4.4.1. $\square$

*Corollary P4.4.3.* (1) For every affine open $V \subseteq Y$ the preimage $f^{-1}(V)$ is affine, so $H^q(f^{-1}V, \mathcal{F}) = 0$ for $q > 0$ by Theorem P4.1.8. The affine open sets form a basis of $Y$, so the sheafification of $V \mapsto H^q(f^{-1}V, \mathcal{F})$ is $0$, and $R^q f_* \mathcal{F} = 0$ by part 4 of Theorem P2.7.3. This needs no separatedness. (2) is Corollary P2.4.27(1). (3) The Leray spectral sequence $R^p g_* (R^q f_* \mathcal{F}) \Rightarrow R^{p+q} (g f)_* \mathcal{F}$ of Corollary P2.4.26 has $E_2^{p,q} = 0$ for $q > 0$, so it degenerates and the edge map $R^p g_*(f_* \mathcal{F}) \to R^p (g f)_* \mathcal{F}$ is an isomorphism (Proposition P2.4.6). Closed immersions and finite morphisms are affine. $\square$

### Exercises

1. (A) Let $X = \mathbb{P}^1_k \times_k \mathbb{A}^1_k$ and $f \colon X \to \mathbb{A}^1_k$ the projection. Compute $R^q f_* \mathcal{O}_X(n)$ for all $q$ and $n$ as $k[t]$-modules.
2. (A) Let $f \colon X \to Y$ be quasi-compact and separated, $\mathcal{F}$ quasi-coherent, and $y \in Y$ with an affine neighbourhood $V = \operatorname{Spec} A$, $y = \mathfrak{p}$. Show that the stalk $(R^q f_* \mathcal{F})_y$ is $H^q(f^{-1}V, \mathcal{F})_\mathfrak{p}$, and that it is also $H^q(X \times_Y \operatorname{Spec} \mathcal{O}_{Y, y}, \mathcal{F})$, using Theorem P4.1.17 for the flat map $A \to A_\mathfrak{p}$.
3. (A) Let $i \colon Z \to X$ be a closed immersion and $f \colon X \to Y$ quasi-compact and separated. For a quasi-coherent sheaf $\mathcal{G}$ on $Z$, show that $R^q (f i)_* \mathcal{G} \cong R^q f_* (i_* \mathcal{G})$.
4. (B) Let $f \colon X \to Y$ be quasi-compact and separated, $Y$ affine, and $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ an exact sequence of quasi-coherent sheaves on $X$. Show that the long exact sequence of the $R^q f_*$ is the sheafification of the long exact cohomology sequence over $X$, and that $f_* \mathcal{F} \to f_* \mathcal{F}''$ is surjective if $R^1 f_* \mathcal{F}' = 0$.
5. (B) Let $f \colon X \to Y$ be a finite morphism of Noetherian schemes, $\mathcal{F}$ coherent on $X$ and $\mathcal{L}$ invertible on $Y$. Show that $H^q(X, \mathcal{F} \otimes f^* \mathcal{L}) \cong H^q(Y, f_* \mathcal{F} \otimes \mathcal{L})$ for every $q$, using Corollary P4.4.3 and Theorem P2.6.30. If $Y \subseteq \mathbb{P}^r_k$ is closed, deduce that $n \mapsto \chi(X, \mathcal{F} \otimes f^* \mathcal{O}_Y(n))$ is the Hilbert polynomial of the coherent sheaf $f_* \mathcal{F}$ (part 3 of Theorem P3.5.33).
6. (C) Let $X$ be the plane with a doubled origin, glued from two copies of $\mathbb{A}^2_k$ along $\mathbb{A}^2_k \setminus \{0\}$, and $f \colon X \to \mathbb{A}^2_k$ the identity on both copies. Show that $f^{-1}(\mathbb{A}^2_k)$ is covered by two affine open sets whose intersection is not affine, and compute $R^1 f_* \mathcal{O}_X$ and $R^2 f_* \mathcal{O}_X$ by the Mayer-Vietoris sequence of the two copies, using Example P4.1.12. Compare with Corollary P4.1.10.

### Lean

Mathlib has sheaf cohomology, `CategoryTheory.Sheaf.H`, but not the higher direct images of a morphism of schemes or their quasi-coherence. Theorem P4.4.1 and its corollaries are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Theorem P4.4.1 is Hartshorne III.8.5 and EGA III.1.4.10, where it is proved for quasi-compact quasi-separated morphisms by a Čech hypercovering argument. Separatedness keeps the proof at the level of Corollary P4.1.9. The vanishing for affine morphisms is EGA III.1.3.2. Example P4.4.6 is the first sign that higher direct images and fibre cohomology need flatness and properness to agree, the subject of Chapter 5. The literature state is theorem. In the minimal model program every statement about the cohomology of a contraction $f \colon X \to Z$ over an affine piece of $Z$ is, by Theorem P4.4.1, a statement about the sheaves $R^q f_* \mathcal{F}$, and this is the form in which the relative vanishing theorems are stated.
