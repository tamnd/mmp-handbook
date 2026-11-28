---
title: The theorem of Deligne and Illusie
nodes: []
sources: [DI87, EV92, Ray78, Har77]
reads_with: [DI87:2, EV92:10]
requires: [P2.4, P4.2, P4.4, P4.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The theorem of Deligne and Illusie

### Statement

Throughout, $k$ is algebraically closed of characteristic $p > 0$, and $X$ is a smooth projective variety over $k$ of dimension $d$. Since $k$ is perfect, the Frobenius twist $X' = X \times_{k, F} k$ is isomorphic to $X$ as a scheme, and the relative Frobenius $F_{X/k} \colon X \to X'$ is a finite flat $k$-morphism of degree $p^d$.

**Definition P7.11.8 (liftings).** Let $W_2(k)$ be the ring of Witt vectors of length $2$ of $k$, a flat $\mathbb{Z}/p^2$-algebra with $W_2(k)/p = k$; for $k = \overline{\mathbb{F}}_p$ it contains $\mathbb{Z}/p^2$. A *lifting* of $X$ to $W_2(k)$ is a scheme $\tilde X$ flat over $W_2(k)$ with $\tilde X \times_{W_2(k)} k \cong X$. The de Rham complex $\Omega^\bullet_X$ has $k$-linear differentials, and $F_{X/k *} \Omega^\bullet_X$ is a complex of coherent $\mathcal{O}_{X'}$-modules with $\mathcal{O}_{X'}$-linear differentials.

**Theorem P7.11.9 (Deligne-Illusie, black box).** If $X$ lifts to $W_2(k)$ and $d < p$, then there is an isomorphism in the derived category of $\mathcal{O}_{X'}$-modules
$$F_{X/k *} \Omega^\bullet_X \cong \bigoplus_{i = 0}^{d} \Omega^i_{X'}[-i].$$
In particular the Hodge to de Rham spectral sequence $E_1^{ij} = H^j(X, \Omega^i_X) \Rightarrow H^{i+j}_{dR}(X/k)$ degenerates at $E_1$.

Lean: not in Lean as stated.

**Theorem P7.11.10 (Kodaira and Akizuki-Nakano vanishing).** Suppose that $X$ lifts to $W_2(k)$ and $d < p$, and let $L$ be an ample line bundle on $X$. Then
$$H^j(X, \Omega^i_X \otimes L^{-1}) = 0 \quad \text{for } i + j < d, \qquad H^j(X, \Omega^i_X \otimes L) = 0 \quad \text{for } i + j > d.$$
In particular $H^j(X, \omega_X \otimes L) = 0$ for $j > 0$.

Lean: not in Lean as stated.

**Corollary P7.11.11 (Raynaud's surface does not lift).** For $p \geq 3$, the surface $X$ of Theorem P7.11.4 does not lift to $W_2(k)$.

Lean: not in Lean as stated.

### Proof in words

In characteristic $p$ the de Rham differential is linear over the $p$-th powers, so the de Rham complex is a complex of coherent sheaves on the Frobenius twist, and the Cartier isomorphism identifies its cohomology sheaves with the sheaves of forms on the twist. Deligne and Illusie show that a lifting to $W_2$ splits the complex into its cohomology sheaves, in degrees below $p$. The splitting is built from local liftings of Frobenius, which exist on a lifting to $W_2$ and differ by derivations, and the obstruction to gluing them disappears in the derived category.

Vanishing follows by a trick that uses Frobenius in place of Hodge theory. Twist the de Rham complex by $L^{-p}$, which is the Frobenius pullback of $L^{-1}$ and has a connection that makes the twist a complex. The hypercohomology of the twisted complex is computed in two ways. On $X'$ the decomposition writes it as the sum of the cohomology of $\Omega^i \otimes L^{-1}$, and on $X$ the Hodge spectral sequence bounds it by the sum of the cohomology of $\Omega^i \otimes L^{-p}$. So the dimensions for $L^{-1}$ are bounded by those for $L^{-p}$, and by iteration by those for $L^{-p^N}$, which vanish in low degree by Serre vanishing and Serre duality. The surface of Raynaud violates the conclusion, so it does not lift.

### Examples

**Example P7.11.12 (varieties that lift).** Projective space, smooth complete intersections in projective space, and smooth projective toric varieties are defined over $\mathbb{Z}$, with smooth models whose reductions are the given varieties, so they lift to $W_2(k)$, and indeed to $W(k)$. A smooth projective curve lifts, since the obstruction to lifting a smooth variety step by step lies in $H^2(X, T_X)$, which vanishes on a curve; and $H^2(X, \mathcal{O}_X) = 0$, so an ample line bundle lifts as well and the lifting is projective. So Theorem P7.11.10 holds for smooth hypersurfaces of dimension less than $p$; for projective space it is the computation of Theorem P4.2.1.

**Example P7.11.13 (the hypothesis $d < p$ in a small case).** Let $p = 2$ and $X$ a smooth projective surface. Then $d = 2 = p$, and Theorem P7.11.10 does not apply, even when $X$ lifts. Deligne and Illusie state a sharper vanishing, in the range $i + j < \min(d, p)$, which covers some cases with $d = p$ (DI87, Section 2, Corollary 2.8 as cited in EV92; the numbering is not checked against the paper); it is not proved here. For a curve, $d = 1 < p$ for every $p$, and the theorem reduces to Example P7.11.6.

**Example P7.11.14 (characteristic 0).** Let $X_0$ be a smooth projective variety over a field of characteristic $0$ and $L_0$ an ample line bundle. Spreading out, $X_0$ and $L_0$ are the generic fibre of a smooth projective scheme with an ample line bundle over a finitely generated $\mathbb{Z}$-algebra $A$. After shrinking $\operatorname{Spec} A$, $A$ is smooth over $\mathbb{Z}$. For a closed point of $\operatorname{Spec} A$ with residue characteristic $p > \dim X_0$, smoothness lets the map from $A$ to the algebraic closure $k$ of the residue field lift to a map $A \to W_2(k)$, and the base change of the model along it is a lifting of the reduction to $W_2(k)$, so Theorem P7.11.10 applies to the reduction. Semicontinuity then gives Kodaira and Akizuki-Nakano vanishing for $X_0$. This is the algebraic proof of Kodaira's theorem of Deligne and Illusie (DI87, Section 2), the proof that the black box Theorem P7.8.2 could cite in place of Hodge theory.

### Proof

*Theorem P7.11.9.* This is Deligne and Illusie, Theorem 2.1 and Corollary 2.4 (DI87), with an exposition in Esnault and Viehweg, Lectures 9 and 10 (EV92); it is a black box here.

*Theorem P7.11.10.* Write $F = F_{X/k}$, and let $L'$ be the line bundle on $X'$ that pulls back to $L$ under the projection $X' \to X$, so that $F^* L' \cong L^p$; under the isomorphism of schemes $X' \cong X$, $L'$ corresponds to $L$, so $h^j(X', \Omega^i_{X'} \otimes L'^{-1}) = h^j(X, \Omega^i_X \otimes L^{-1})$. The line bundle $F^* L'^{-1}$ has the connection $\nabla(f \cdot F^* s) = df \otimes F^* s$ for local sections $s$ of $L'^{-1}$, well defined since $d(g^p) = 0$, so $\Omega^\bullet_X \otimes F^* L'^{-1}$ is a complex, and by the projection formula
$$F_*(\Omega^\bullet_X \otimes F^* L'^{-1}) = F_* \Omega^\bullet_X \otimes L'^{-1} \cong \bigoplus_i \Omega^i_{X'} \otimes L'^{-1} [-i]$$
by Theorem P7.11.9, as complexes of $\mathcal{O}_{X'}$-modules up to quasi-isomorphism. Take hypercohomology in degree $n$. Since $F$ is finite, the hypercohomology of the left side on $X'$ is that of $\Omega^\bullet_X \otimes L^{-p}$ on $X$ (Corollary P4.4.3), and the hypercohomology spectral sequence with $E_1^{ij} = H^j(X, \Omega^i_X \otimes L^{-p})$ gives
$$\sum_{i + j = n} h^j(X, \Omega^i_X \otimes L^{-1}) = \dim \mathbb{H}^n(X, \Omega^\bullet_X \otimes L^{-p}) \leq \sum_{i + j = n} h^j(X, \Omega^i_X \otimes L^{-p}).$$
Applying this to $L^p, L^{p^2}, \dots$, which are ample, gives
$$\sum_{i + j = n} h^j(X, \Omega^i_X \otimes L^{-1}) \leq \sum_{i + j = n} h^j(X, \Omega^i_X \otimes L^{-p^N})$$
for every $N \geq 1$. Let $n < d$. For $i + j = n$, $j < d$, and Serre duality, Corollary P4.7.21, with $\omega_X \otimes (\Omega^i_X)^\vee \cong \Omega^{d-i}_X$, gives $h^j(X, \Omega^i_X \otimes L^{-p^N}) = h^{d - j}(X, \Omega^{d-i}_X \otimes L^{p^N})$, which is $0$ for $N \gg 0$ by Serre vanishing, Theorem P4.2.7, applied to a very ample power $L^m$ and the finitely many sheaves $\Omega^{d-i}_X \otimes L^r$, $0 \leq r < m$. This proves the first vanishing, and Serre duality turns it into the second, since $h^j(\Omega^i \otimes L) = h^{d-j}(\Omega^{d-i} \otimes L^{-1})$ and $i + j > d$ means $(d - i) + (d - j) < d$. The case $i = d$ of the second is the last statement.

*Corollary P7.11.11.* The surface $X$ has dimension $2 < p$, and $H^1(X, \omega_X \otimes \mathcal{L}) \neq 0$ for an ample $\mathcal{L}$, by Theorem P7.11.4. If $X$ lifted to $W_2(k)$, Theorem P7.11.10 would give $H^1(X, \omega_X \otimes \mathcal{L}) = 0$.

### Exercises

1. (A) Check Theorem P7.11.10 for $X = \mathbb{P}^1$ and $L = \mathcal{O}(1)$ directly, for every $p$.
2. (A) Let $X$ be a smooth projective curve of genus $g$ and $L$ ample. Show that the inequality in the proof of Theorem P7.11.10 for $n = 0$ is $h^0(L^{-1}) \leq h^0(L^{-p})$, and that both sides are $0$.
3. (B) Show that the connection on $F^* L'^{-1}$ in the proof is integrable and has $p$-curvature zero, and that its horizontal sections are the sections of $L'^{-1}$ pulled back by $F$.
4. (B) Deduce from Theorem P7.11.9 that $\sum_{i + j = n} h^j(X, \Omega^i_X) = \dim H^n_{dR}(X/k)$ for $X$ liftable with $d < p$, and check this for $X = \mathbb{P}^1 \times \mathbb{P}^1$.
5. (B) Let $X$ be the curve of Example P7.11.5 with $p \geq 3$. It lifts to $W_2(k)$ by Example P7.11.12. Explain why this does not contradict Proposition P7.11.3: compare the failure of injectivity of $F^*$ on $H^1(C, \mathcal{O}(-D))$ with the vanishing statements of Theorem P7.11.10 for $d = 1$.
6. (C) Using Example P7.11.14, prove Kodaira vanishing for a smooth hypersurface $X_0 \subset \mathbb{P}^n_{\mathbb{Q}}$ of degree $e$ and $L_0 = \mathcal{O}(1)|_{X_0}$ from Theorem P7.11.10, and compare with the direct computation from the sequence $0 \to \mathcal{O}(-e-1) \to \mathcal{O}(-1) \to \mathcal{O}_{X_0}(-1) \to 0$ and Theorem P4.2.1.

### Lean

The project library has no de Rham complex in positive characteristic, no Witt vector liftings of schemes and no positive characteristic vanishing. Mathlib has Witt vectors of rings and Kähler differentials, but not the de Rham complex of a scheme. The handbook adds no `MinimalModel` node here.

### Notes and history

Deligne and Illusie proved the decomposition theorem and the vanishing theorems for liftable varieties in 1987 (DI87), and deduced the degeneration of the Hodge to de Rham spectral sequence and Kodaira vanishing in characteristic $0$ by spreading out. The literature state is theorem. Esnault and Viehweg, Lectures 8 to 10 (EV92), give an exposition and extend the method to the Kawamata-Viehweg vanishing theorem for liftable varieties. Raynaud's surfaces do not lift to $W_2$, by Corollary P7.11.11, and the hypothesis $d < p$ is used in the construction of the decomposition.
