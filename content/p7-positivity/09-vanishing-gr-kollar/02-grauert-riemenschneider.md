---
title: The Grauert-Riemenschneider theorem
nodes: []
sources: [KM98, Laz04, GR70, EV92, Har77]
reads_with: [KM98:2.4, Laz04:4.3, EV92:5]
requires: [P4.4, P4.7, P4.9, P5.6, P7.3, P7.8, 4.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Grauert-Riemenschneider theorem

### Statement

Throughout, $k$ has characteristic $0$. A morphism $f \colon X \to Z$ of varieties is *generically finite* if $\dim f(X) = \dim X$, that is, if its general fibre over the image is finite.

**Theorem P7.9.8 (Grauert-Riemenschneider).** Let $X$ be a smooth quasi-projective variety, $Z$ a variety and $f \colon X \to Z$ a proper generically finite morphism. Then
$$R^j f_* \omega_X = 0 \quad \text{for } j > 0.$$

Lean: not in Lean as stated.

**Corollary P7.9.9 (the direct image of $\omega$ is a birational invariant).** Let $Z$ be a quasi-projective variety and $f \colon X \to Z$ a projective resolution, that is, a projective birational morphism from a smooth variety. Then $Rf_* \omega_X = f_* \omega_X$, and the sheaf $f_* \omega_X$ does not depend on the projective resolution $f$: for two projective resolutions $f_1, f_2$ there is an isomorphism $f_{1*} \omega_{X_1} \cong f_{2*} \omega_{X_2}$ that is the identity over the smooth locus of $Z$.

Lean: not in Lean as stated.

### Proof in words

For a projective morphism the theorem is Kawamata-Viehweg vanishing with $N = 0$: the pullback $f^* H$ of an ample divisor by a generically finite morphism is nef and big, so relative vanishing applies to $K_X + 0$. The general case is local on $Z$. Over an affine open set of $Z$ the morphism is a closed subvariety of $\mathbb{P}^N$ times the open set, its closure in $\mathbb{P}^N$ times a projective closure of the open set is projective, and Hironaka's theorem resolves the closure without changing it over the smooth part, which contains the original variety. The higher direct images over the open set are unchanged.

The theorem says that $Rf_* \omega_X$ is a sheaf. Duality, in the form of Theorem P4.9.21, turns this into a statement about $Rf_* \mathcal{O}_X$, and this is how the theorem enters Kempf's criterion for rational singularities. It is false for $\mathcal{O}_X$ in place of $\omega_X$, as the cone over an elliptic curve shows, and false without the hypothesis that $f$ is generically finite, as any curve of positive genus mapping to a point shows. Section 9.3 replaces the second failure by Kollár's theorem: $R^j f_* \omega_X$ vanishes above the dimension of the general fibre.

### Examples

**Example P7.9.10 (the blow-up of a point of a surface).** Let $\mu \colon X \to S$ be the blow-up of a point of a smooth surface, with exceptional curve $E$, so that $\omega_X = \mu^* \omega_S \otimes \mathcal{O}_X(E)$. By the projection formula, $R^1 \mu_* \omega_X = \omega_S \otimes R^1 \mu_* \mathcal{O}_X(E)$, and $R^1 \mu_* \mathcal{O}_X(E) = 0$ by part 2 of Proposition P4.4.16, whose length $m(m-1)/2$ vanishes for $m = 1$. For $m = 2$ the length is $1$: the sheaf $\omega_X \otimes \mathcal{O}_X(E) = \mu^* \omega_S \otimes \mathcal{O}_X(2E)$ has $R^1 \mu_* \neq 0$. Twisting $\omega_X$ by a divisor that is negative on the fibre can destroy the vanishing.

**Example P7.9.11 (the cone over an elliptic curve).** Let $E$ be an elliptic curve and $L$ a line bundle of degree $d \geq 3$ on $E$, so that the ring $S = \bigoplus_{m \geq 0} H^0(E, L^m)$ is normal and generated in degree $1$, and let $C = \operatorname{Spec} S$ be the cone of Example P4.9.24. Let $Y = \operatorname{Spec}_E \bigoplus_{m \geq 0} L^m$, with affine projection $\pi \colon Y \to E$ and the resolution $f \colon Y \to C$ of the proof of Proposition P4.9.23. On the one hand,
$$R^1 f_* \mathcal{O}_Y = H^1(Y, \mathcal{O}_Y)^\sim = \Big( \bigoplus_{m \geq 0} H^1(E, L^m) \Big)^\sim = H^1(E, \mathcal{O}_E)^\sim,$$
which is $k$ at the vertex, by Proposition P4.4.2, Corollary P4.4.3 and $H^1(E, L^m) = 0$ for $m \geq 1$. On the other hand, the relative tangent bundle of the line bundle $\pi$ is $\pi^* L^{-1}$, so $\omega_{Y/E} = \pi^* L$ and $\omega_Y = \pi^*(\omega_E \otimes L) = \pi^* L$, since $\omega_E \cong \mathcal{O}_E$. The same computation gives
$$R^1 f_* \omega_Y = \Big( \bigoplus_{m \geq 0} H^1(E, L^{m+1}) \Big)^\sim = 0,$$
as Theorem P7.9.8 predicts. So the theorem fails for $\mathcal{O}_Y$ in place of $\omega_Y$. The shift by one in the grading is the whole difference, and it is the computation $K_Y = f^* K_C - E_0$ of Example P4.9.24 seen through the grading, where $E_0$ is the zero section.

**Example P7.9.12 (positive dimensional fibres).** Let $X$ be a smooth projective curve of genus $g \geq 1$ and $f \colon X \to \operatorname{Spec} k$ the structure morphism. Then $R^1 f_* \omega_X = H^1(X, \omega_X) = k$ by Serre duality, Corollary P4.7.21. The hypothesis that $f$ is generically finite is needed, and for a product $X = C \times \mathbb{P}^1 \to C$ the same failure appears in Example P7.9.18.

### Proof

*Theorem P7.9.8.* First suppose that $X$ and $Z$ are projective. Replacing $Z$ by the closed subvariety $f(X)$ changes no higher direct image, so assume $f$ surjective. Let $H$ be an ample divisor on $Z$. By Lemma P7.9.2, $f^* H$ is nef and big, so Theorem P7.9.3 applies with $N = 0$ and $\Delta = 0$, and gives $R^j f_* \omega_X = 0$ for $j > 0$.

In general the question is local on $Z$, so let $V \subseteq Z$ be an affine open set and $U = f^{-1}(V)$, a smooth quasi-projective variety with a proper morphism $f_U \colon U \to V$. Choose a locally closed embedding $U \subseteq \mathbb{P}^N$ and an open embedding $V \subseteq \bar V$ into a projective variety, for instance the closure of $V$ in a projective space containing an affine space in which $V$ is closed. The morphism $(\iota, f_U) \colon U \to \mathbb{P}^N \times V$ is an immersion, and it is proper because $f_U$ is proper and $\mathbb{P}^N \times V \to V$ is separated (Har77, II.4.8); so its image is closed and $U$ is a closed subvariety of $\mathbb{P}^N \times V$. Let $\bar U_0$ be the closure of $U$ in $\mathbb{P}^N \times \bar V$, a projective variety with $\bar U_0 \cap (\mathbb{P}^N \times V) = U$, and let $\nu \colon \bar U_1 \to \bar U_0$ be its normalization, a finite morphism which is an isomorphism over the normal open set $U$. By Theorem 4.2.10 there is a log resolution $\rho \colon \bar U \to \bar U_1$ of the pair $(\bar U_1, 0)$ that is an isomorphism over the smooth locus, which contains $U$. The composite $\bar f \colon \bar U \to \bar V$ of $\rho$, $\nu$ and the second projection is a morphism of projective varieties with $\bar U$ smooth, it is generically finite because it agrees with $f_U$ on the dense open set $U$, and $\bar f^{-1}(V) = U$ with $\bar f|_U = f_U$. By the projective case, $R^j \bar f_* \omega_{\bar U} = 0$ for $j > 0$, and its restriction to $V$ is $R^j f_{U*} \omega_U = (R^j f_* \omega_X)|_V$ (Har77, III.8.2). So $R^j f_* \omega_X$ vanishes on every affine open set.

*Corollary P7.9.9.* By Theorem P7.9.8 the complex $Rf_* \omega_X$ has cohomology only in degree $0$, so $Rf_* \omega_X = f_* \omega_X$. For two projective resolutions $f_1$, $f_2$, let $X_3$ be the closure of the graph of the birational map $X_1 \dashrightarrow X_2$ in $X_1 \times_Z X_2$, and $X_4 \to X_3$ a log resolution which is an isomorphism over the smooth locus, by Theorem 4.2.10, after normalization as in the proof of Theorem P7.9.8. The morphisms $g_i \colon X_4 \to X_i$ are projective and birational between smooth varieties, so $g_{i*} \omega_{X_4} = \omega_{X_i}$ by Lemma P4.9.19. Hence
$$f_{1*} \omega_{X_1} = f_{1*} g_{1*} \omega_{X_4} = (f_1 g_1)_* \omega_{X_4} = (f_2 g_2)_* \omega_{X_4} = f_{2*} g_{2*} \omega_{X_4} = f_{2*} \omega_{X_2},$$
and over the smooth locus of $Z$, where all the $f_i$ and $g_i$ are compared with the identity by Lemma P4.9.19, these are the identifications with $\omega_Z$.

### Exercises

1. (A) Let $\mu \colon X \to \mathbb{A}^n$ be the blow-up of the origin, $n \geq 2$, with exceptional divisor $E \cong \mathbb{P}^{n-1}$, so that $\omega_X = \mu^* \omega_{\mathbb{A}^n} \otimes \mathcal{O}_X((n-1)E)$. Deduce from Theorem P7.9.8 that $R^j \mu_* \mathcal{O}_X((n-1)E) = 0$ for $j > 0$.
2. (B) In Exercise 1, show that $R^{n-1} \mu_* \mathcal{O}_X(nE) \neq 0$, using the sequence $0 \to \mathcal{O}_X((n-1)E) \to \mathcal{O}_X(nE) \to \mathcal{O}_E(-n) \to 0$ and $H^{n-1}(\mathbb{P}^{n-1}, \mathcal{O}(-n)) = k$.
3. (B) Let $f \colon X \to Z$ be a generically finite surjective morphism of smooth projective varieties and $L$ a nef and big line bundle on $Z$. Show that $H^i(Z, f_* \omega_X \otimes L) = 0$ for $i > 0$, using Theorem P7.9.8, the Leray spectral sequence and Theorem P7.8.18 for $f^* L$.
4. (B) In Example P7.9.11, show that $H^0(Y, \omega_Y) = \bigoplus_{m \geq 1} H^0(E, L^m)$ as a graded $S$-module, so that $f_* \omega_Y$ is the maximal ideal of the vertex up to the choice of a generator of $\omega_E$. Deduce again that $f_* \omega_Y \neq \omega_C$.
5. (B) Let $X = Y \times W$ with $Y$ and $W$ smooth projective, $\dim W = d$, and $f \colon X \to Y$ the projection. Show that $R^d f_* \omega_X \cong \omega_Y$ and $R^j f_* \omega_X = 0$ for $j > d$, by the Künneth formula.
6. (C) Remove the hypothesis that $X$ is quasi-projective from Theorem P7.9.8: given a proper generically finite $f \colon X \to Z$ with $X$ smooth, use Chow's lemma and Theorem 4.2.10 to find a proper birational $g \colon X' \to X$ with $X'$ smooth and quasi-projective, apply the theorem to $g$ and to $f \circ g$, and conclude with the Leray spectral sequence.

### Lean

The project library has no statement of the Grauert-Riemenschneider theorem as such; in the projective case it is the instance $N = 0$, $\Delta = 0$ of `MinimalModel.KawamataViehweg`, which is stated without proof. Mathlib has no higher direct images of coherent sheaves. The handbook adds no `MinimalModel` node here.

### Notes and history

Grauert and Riemenschneider proved the theorem for complex spaces by analytic methods (GR70). The literature state is theorem. The deduction from Kawamata-Viehweg vanishing is in Kollár and Mori, Section 2.4 (KM98), in Lazarsfeld, Section 4.3 (Laz04), and in Esnault and Viehweg, Lecture 5 (EV92). Its main use in the minimal model program is through Kempf's criterion, Theorem P4.9.21, which characterizes rational singularities as normal Cohen-Macaulay singularities with $f_* \omega_Y = \omega_X$, and through it the theorem that klt singularities are rational, Kollár and Mori, Theorem 5.22. Corollary P7.9.9 is the reason why the sheaf $f_* \omega_X$ is an invariant of $Z$. The proof given here rests on Kodaira vanishing, which fails in characteristic $p$ (Chapter 11).
