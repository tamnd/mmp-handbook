---
title: Flat base change
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:III.9, Vak25:ch25]
requires: [P1.1, P3.13, P4.1, P4.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Flat base change

### Statement

Throughout, $f \colon X \to Y$ is a morphism, $g \colon Y' \to Y$ a morphism, and
$$X' = X \times_Y Y' \xrightarrow{g'} X, \qquad f' \colon X' \to Y'$$
the base change, with $f g' = g f'$. For $y \in Y$ the *fibre* is $X_y = X \times_Y \operatorname{Spec} \kappa(y)$, and $\mathcal{F}_y$ is the pullback of $\mathcal{F}$ to $X_y$.

**Theorem P4.5.1 (flat base change).** Let $f$ be quasi-compact and separated, $\mathcal{F}$ a quasi-coherent sheaf on $X$, and $g$ flat. For every $q \geq 0$ there is a natural isomorphism
$$g^* R^q f_* \mathcal{F} \xrightarrow{\ \sim\ } R^q f'_* (g'^* \mathcal{F})$$
of quasi-coherent sheaves on $Y'$. Over affine open sets $V' = \operatorname{Spec} B \subseteq Y'$ and $V = \operatorname{Spec} A \subseteq Y$ with $g(V') \subseteq V$ it is the map $H^q(f^{-1}V, \mathcal{F}) \otimes_A B \to H^q(f'^{-1} V', g'^* \mathcal{F})$ of Theorem P4.1.17.

Lean: not in Lean as stated.

**Corollary P4.5.2 (stalks and the generic fibre).** Let $f$ and $\mathcal{F}$ be as in Theorem P4.5.1 and $y \in Y$.

1. $(R^q f_* \mathcal{F})_y \cong H^q(X \times_Y \operatorname{Spec} \mathcal{O}_{Y, y}, \mathcal{F})$, the cohomology of the restriction of $\mathcal{F}$ to the preimage of the local scheme at $y$.
2. If $Y$ is integral with generic point $\eta$, then $(R^q f_* \mathcal{F})_\eta \cong H^q(X_\eta, \mathcal{F}_\eta)$.
3. For a field extension $K \supseteq k$ and $X$ quasi-compact and separated over $k$, $H^q(X_K, \mathcal{F}_K) \cong H^q(X, \mathcal{F}) \otimes_k K$.

Lean: not in Lean as stated.

Part 3 is Example P4.1.20 again. The base change map exists for every $g$, flat or not, and Section 5.3 studies it for the inclusion of a point, $\operatorname{Spec} \kappa(y) \to Y$, which is almost never flat. In that case it is the map
$$\varphi^q(y) \colon R^q f_* \mathcal{F} \otimes \kappa(y) \to H^q(X_y, \mathcal{F}_y).$$

### Proof in words

Both sides are quasi-coherent, so the theorem is local on $Y'$ and on $Y$, and over affine pieces both sides are the sheaves of modules computed by Theorem P4.4.1. There the statement is that tensoring a Čech complex with a flat algebra commutes with taking cohomology, which is Theorem P4.1.17. The stalk at $y$ is the base change to the local ring $\mathcal{O}_{Y,y}$, a flat localization of any affine neighbourhood, and the generic stalk of an integral base is the base change to the function field, which is the generic fibre.

### Examples

**Example P4.5.3 (three points that become collinear).** Let $A = k[t]$, $Y = \operatorname{Spec} A$, and let $Z \subseteq \mathbb{P}^2_Y$ be the union of the three sections
$$p_1 = [1 : 0 : 0], \qquad p_2 = [0 : 1 : 0], \qquad p_3 = [1 : 1 : t],$$
which are pairwise disjoint over every point of $Y$. Then $\mathcal{O}_Z$ is the direct sum of three copies of $\mathcal{O}_Y$ pushed forward, flat over $Y$, and from $0 \to \mathcal{I}_Z \to \mathcal{O} \to \mathcal{O}_Z \to 0$ the ideal sheaf $\mathcal{I}_Z$ and $\mathcal{F} = \mathcal{I}_Z(1)$ are flat over $Y$ too. Over $Y$ itself, $H^0(\mathbb{P}^2_A, \mathcal{F})$ is the set of linear forms $a x + b y + c z$ with $a, b, c \in A$ vanishing at the three sections, that is $a = 0$, $b = 0$ and $a + b + t c = 0$. So $c = 0$ and $f_* \mathcal{F} = 0$. Over the point $t = 0$ the three points lie on the line $z = 0$, so $H^0(\mathbb{P}^2_k, \mathcal{F}_0) = k z \neq 0$, and
$$f_* \mathcal{F} \otimes \kappa(0) = 0 \to H^0(X_0, \mathcal{F}_0) = k$$
is not an isomorphism. The inclusion of the point is not flat, and Theorem P4.5.1 does not apply. Over $t = c \neq 0$ the points are not collinear and $H^0(\mathcal{F}_c) = 0$.

**Example P4.5.4 (the generic fibre).** In Example P4.5.3, part 2 of Corollary P4.5.2 gives $H^q(X_\eta, \mathcal{F}_\eta) = (R^q f_* \mathcal{F})_\eta$ over $K = k(t)$. By Example P4.5.11 below, $R^1 f_* \mathcal{F} = (A/tA)^\sim$ is the skyscraper $k$ at $t = 0$, so its generic stalk is $0$, and the generic fibre has $H^0 = H^1 = 0$, which matches the three non-collinear points $[1 : 0 : 0]$, $[0 : 1 : 0]$, $[1 : 1 : t]$ over $k(t)$.

**Example P4.5.5 (étale and open base changes).** For an open immersion $g \colon Y' \to Y$, Theorem P4.5.1 is the compatibility of $R^q f_*$ with restriction to open sets. For the finite étale map $g \colon \mathbb{G}_m \to \mathbb{G}_m$, $s \mapsto s^2$ over a field of characteristic not $2$, which is flat, the higher direct images of a family over $\mathbb{G}_m$ pull back to those of the family over the double cover, so a family whose $R^q f_*$ is locally free of rank $r$ remains so after the cover.

### Proof

*Theorem P4.5.1.* The base change $f'$ is quasi-compact, since over an affine $V' \subseteq g^{-1}(V)$ its preimage is $f^{-1}(V) \times_V V'$, covered by the finitely many affine sets $U_i \times_V V'$ for a finite affine cover $(U_i)$ of $f^{-1}(V)$, and it is separated by part 3 of Proposition P3.4.9. By Theorem P4.4.1 applied to $f$ and to $f'$, both sides are quasi-coherent, and the pullback of a quasi-coherent sheaf is quasi-coherent (Proposition P3.5.32). Let $V = \operatorname{Spec} A \subseteq Y$ and $V' = \operatorname{Spec} B \subseteq g^{-1}(V)$ be affine. Then $f^{-1}(V)$ is quasi-compact and separated over $A$, $f'^{-1}(V') = f^{-1}(V) \times_A B$, and
$$(g^* R^q f_* \mathcal{F})|_{V'} = (H^q(f^{-1}V, \mathcal{F}) \otimes_A B)^\sim, \qquad R^q f'_*(g'^* \mathcal{F})|_{V'} = H^q(f^{-1}V \times_A B, g'^* \mathcal{F})^\sim,$$
by Theorem P4.4.1 and part 1 of Proposition P3.5.32. Theorem P4.1.17 gives a natural map from the first module to the second, an isomorphism because $B$ is flat over $A$ (Definition P3.13.1 and Proposition P3.13.2 for the flatness of $A \to B$ on affine pieces). The map of Theorem P4.1.17 is the map of Čech complexes $C^\bullet \otimes_A B \to C^\bullet_B$ for a finite affine cover, and it is compatible with shrinking $V'$ to a basic open subset and $V$ to a smaller affine open subset containing $g(V')$. So these maps glue to a morphism of sheaves on $Y'$, which is an isomorphism on every $V'$. $\square$

*Corollary P4.5.2.* (1) Let $V = \operatorname{Spec} A \ni y$ be affine, $y = \mathfrak{p}$. By Theorem P4.4.1, $(R^q f_* \mathcal{F})_y = H^q(f^{-1}V, \mathcal{F})_\mathfrak{p} = H^q(f^{-1} V, \mathcal{F}) \otimes_A A_\mathfrak{p}$, and Theorem P4.1.17 for the flat map $A \to A_\mathfrak{p}$ identifies this with the cohomology over $f^{-1}(V) \times_A A_\mathfrak{p} = X \times_Y \operatorname{Spec} \mathcal{O}_{Y, y}$. (2) For $y = \eta$, $\mathcal{O}_{Y, \eta} = \kappa(\eta)$ is the function field and $X \times_Y \operatorname{Spec} \kappa(\eta) = X_\eta$. (3) Every $k$-vector space is flat over $k$. $\square$

### Exercises

1. (A) Let $f \colon X \to Y$ be quasi-compact and separated, $\mathcal{F}$ quasi-coherent, and $Y$ integral with generic point $\eta$. Show that if $R^q f_* \mathcal{F}$ is coherent and $H^q(X_\eta, \mathcal{F}_\eta) = 0$, then $R^q f_* \mathcal{F}$ vanishes on a dense open subset of $Y$.
2. (A) In Example P4.5.3, compute $H^0(\mathcal{F}_c)$ and $H^1(\mathcal{F}_c)$ for every $c \in k$ directly, using $\chi(\mathcal{F}_c) = \chi(\mathcal{O}(1)) - 3 = 0$.
3. (A) Let $A \to B$ be faithfully flat, $f \colon X \to \operatorname{Spec} A$ quasi-compact and separated, and $\mathcal{F}$ quasi-coherent. Show that $H^q(X, \mathcal{F}) = 0$ if and only if $H^q(X_B, \mathcal{F}_B) = 0$.
4. (B) Let $f \colon X \to Y$ be projective, $Y$ Noetherian and $\mathcal{F}$ coherent. Using the completion $\mathcal{O}_{Y,y} \to \widehat{\mathcal{O}}_{Y,y}$ (Corollary P1.6.14), show that $(R^q f_* \mathcal{F})_y \otimes \widehat{\mathcal{O}}_{Y,y} \cong H^q(X \times_Y \operatorname{Spec} \widehat{\mathcal{O}}_{Y,y}, \mathcal{F})$. (Chapter 6 compares this with the limit of the cohomology of the thickened fibres.)
5. (B) Let $Y = \operatorname{Spec} k[t]$ and $X = V_+(x y - t z^2) \subseteq \mathbb{P}^2_Y$. Show that $X$ is flat over $Y$, compute $f_* \mathcal{O}_X(n)$ and $R^1 f_* \mathcal{O}_X(n)$ for all $n$ from the sequence $0 \to \mathcal{O}(n-2) \to \mathcal{O}(n) \to \mathcal{O}_X(n) \to 0$ on $\mathbb{P}^2_Y$, and check that they commute with restriction to every point of $Y$.
6. (C) Let $f \colon X \to Y$ be quasi-compact and separated, $g \colon Y' \to Y$ arbitrary, and $\mathcal{F}$ quasi-coherent on $X$ and flat over $Y$. Use Example P4.5.3 to show that the base change map $g^* f_* \mathcal{F} \to f'_* g'^* \mathcal{F}$ need not be an isomorphism. Suppose that $f^{-1}(V)$ is covered by $n + 1$ affine open sets for every affine $V \subseteq Y$. Show that the base change map $g^* R^n f_* \mathcal{F} \to R^n f'_* g'^* \mathcal{F}$ is an isomorphism for every $g$, using that $\check{H}^n$ is the cokernel of the last Čech differential and that $\otimes_A B$ is right exact. (Flatness of $\mathcal{F}$ is not needed here.)

### Lean

Flat base change for the cohomology of quasi-coherent sheaves is not in Mathlib, nor is the Čech description it rests on. The handbook adds no `MinimalModel` node here.

### Notes and history

Theorem P4.5.1 is Hartshorne III.9.3 and EGA III.1.4.15. Grothendieck's insight was that the failure of base change for a non-flat $g$ is controlled by a single complex of finitely generated modules, the subject of Section 5.2. The literature state is theorem. In the minimal model program, flat base change is how a statement over the generic point of the base, for instance about the generic fibre of a Mori fibre space, is spread out to an open subset of the base, which is the first step of every argument by Noetherian induction on the base.
