---
title: The failure of vanishing in characteristic p
nodes: []
sources: [Ray78, Muk13, Kol13, CT18, Har77]
reads_with: [Muk13:sec2, Ray78:main, Kol13:3.1]
requires: [P4.5, P7.8, P7.9, P7.11]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The failure of vanishing in characteristic p

### Statement

Volume P7, Chapter 11, proves that Frobenius can kill a cohomology class on a Tango curve, states Raynaud's counterexample to Kodaira vanishing, and proves Kodaira vanishing for varieties that lift to $W_2(k)$ and for F-split varieties. This section explains why every counterexample has to involve a non-injective Frobenius, outlines Raynaud's construction, deduces the failure of Grauert-Riemenschneider vanishing, and proves that a single variety in characteristic $0$ satisfies Kawamata-Viehweg vanishing after reduction modulo all large primes. Throughout, $k$ is an algebraically closed field of characteristic $p > 0$ and $F \colon X \to X$ is the absolute Frobenius morphism, so that $F^* M \cong M^{\otimes p}$ for every line bundle $M$.

**Proposition 5.6.1 (counterexamples come from Frobenius).** Let $X$ be a smooth projective variety of dimension $n$, $L$ an ample line bundle and $0 \leq i < n$ with $H^i(X, L^{-1}) \neq 0$. Then there is $e \geq 0$ such that the map
$$F^* \colon H^i(X, L^{-p^e}) \to H^i(X, L^{-p^{e+1}})$$
is not injective. More precisely, for every nonzero $\xi \in H^i(X, L^{-1})$ there is $e \geq 0$ with $(F^e)^* \xi \neq 0$ and $(F^{e+1})^* \xi = 0$.

Lean: not yet in Lean.

**Remark 5.6.2 (an outline of Raynaud's construction).** This is an outline of the proof of Theorem P7.11.4, after Ray78 and the exposition of Muk13. Let $C$ be a Tango curve, with $\operatorname{div}(df) = pD$ as in Definition P7.11.1, and let $0 \neq \xi \in H^1(C, \mathcal{O}_C(-D))$ with $F^* \xi = 0$, which exists by Proposition P7.11.3.

1. The class $\xi \in \operatorname{Ext}^1(\mathcal{O}_C(D), \mathcal{O}_C)$ defines a nonsplit extension $0 \to \mathcal{O}_C \to \mathcal{E} \to \mathcal{O}_C(D) \to 0$ of rank $2$.
2. Its Frobenius pullback is the extension $0 \to \mathcal{O}_C \to F^* \mathcal{E} \to \mathcal{O}_C(pD) \to 0$ with class $F^* \xi = 0$, so it splits: $F^* \mathcal{E} \cong \mathcal{O}_C \oplus \mathcal{O}_C(pD)$.
3. On the ruled surface $P = \mathbb{P}(\mathcal{E}) \xrightarrow{\rho} C$, the quotient $\mathcal{E} \to \mathcal{O}_C(D)$ gives a section $C_0$. The quotient $F^* \mathcal{E} \to \mathcal{O}_C$ of the splitting gives a section of $\mathbb{P}(F^* \mathcal{E})$, and its image under the relative Frobenius $\mathbb{P}(F^* \mathcal{E}) \to \mathbb{P}(\mathcal{E})$ is a curve $C_1 \subset P$ that is purely inseparable of degree $p$ over $C$. Raynaud shows that the two curves are disjoint, and computes their classes in $\operatorname{Pic}(P)$ from the two quotients.
4. For a suitable integer $l \geq 2$ prime to $p$ such that the divisor $C_0 + C_1$ is divisible by $l$ in $\operatorname{Pic}(P)$, the cyclic cover $\pi \colon X \to P$ of degree $l$ branched along $C_0 + C_1$ (Proposition P7.8.10) is a smooth projective surface, since the branch divisor is smooth.
5. The direct image $\pi_* \mathcal{O}_X$ splits into eigensheaves, line bundles on $P$ built from the $l$-th root of $C_0 + C_1$. Raynaud chooses an ample line bundle $\mathcal{L}$ on $X$, built from the ramification divisor over $C_0$ and the pullback of a divisor on $C$, such that one eigensheaf of $\pi_* \mathcal{L}^{-1}$ has an $H^1$ that receives the class $\xi$ injectively through the Leray spectral sequence for $\rho$. So $H^1(X, \mathcal{L}^{-1}) \neq 0$.

The numerical conditions on $l$ and the choice of $\mathcal{L}$ are in Muk13, Section 2; the outline here records only the logic: a Frobenius-killed class on the base curve becomes a nonzero $H^1$ of the inverse of an ample bundle upstairs.

**Proposition 5.6.3 (Grauert-Riemenschneider fails).** Let $X$ be a smooth projective surface with an ample line bundle $L$ such that $H^1(X, L^{-1}) \neq 0$, as in Theorem P7.11.4. Let $\pi \colon Y = \operatorname{Spec}_X \bigoplus_{m \geq 0} L^m \to X$ be the total space of $L^{-1}$, and $\mu \colon Y \to Z = \operatorname{Spec} \bigoplus_{m \geq 0} H^0(X, L^m)$ the contraction of the zero section onto the vertex of the affine cone. Then $Y$ is a smooth threefold, $\mu$ is proper and birational, and $R^1 \mu_* \omega_Y \neq 0$.

Lean: not yet in Lean.

So Theorem P7.9.8 fails in every characteristic $p > 0$.

**Proposition 5.6.4 (reduction modulo large primes).** Let $X_0$ be a smooth projective variety over a field $K$ of characteristic $0$, $N_0$ a Cartier divisor and $\Delta_0$ a $\mathbb{Q}$-divisor with snc support and coefficients in $[0, 1)$, such that $N_0 - \Delta_0$ is ample. Then there are a finitely generated $\mathbb{Z}$-algebra $A \subseteq K$, a smooth projective morphism $X_A \to \operatorname{Spec} A$ with generic fibre $X_0$, divisors $N_A$, $\Delta_A$ restricting to $N_0$, $\Delta_0$, and a dense open set $U \subseteq \operatorname{Spec} A$, such that for every closed point $s \in U$ with residue field $\kappa(s)$ and algebraic closure $\overline{\kappa(s)}$, the fibre $X_{\bar s} = X_A \otimes \overline{\kappa(s)}$ satisfies
$$H^i(X_{\bar s}, \mathcal{O}(K_{X_{\bar s}} + N_{\bar s})) = 0 \quad \text{for } i > 0.$$
The characteristics of the closed points of $U$ include every sufficiently large prime.

Lean: not yet in Lean.

The bound on $p$ depends on $X_0$, $N_0$ and $\Delta_0$. Example 5.6.6 shows that no bound works for all varieties of a given dimension. Example P7.11.14 is the same argument for Kodaira vanishing run in the other direction, from characteristic $p$ to characteristic $0$ through Deligne-Illusie.

### Proof in words

If $\xi$ is a nonzero class in $H^i(X, L^{-1})$, its Frobenius pullbacks are classes in $H^i(X, L^{-p^e})$, which is dual to $H^{n-i}(X, \omega_X \otimes L^{p^e})$ and so vanishes for large $e$ by Serre vanishing. Some pullback is the last nonzero one. For Grauert-Riemenschneider, the total space of $L^{-1}$ is affine over $X$, so its cohomology is the sum over $m$ of the cohomology of $X$ with coefficients in the graded pieces, and the piece of $\omega_Y$ of degree $0$ is $\omega_X \otimes L$, whose $H^1$ is dual to $H^1(X, L^{-1}) \neq 0$; the cone $Z$ is affine, so this $H^1$ is the global sections of $R^1 \mu_* \omega_Y$. For reduction modulo $p$, every datum spreads out over a finitely generated ring, vanishing holds at the generic point by Kawamata-Viehweg in characteristic $0$, and semicontinuity spreads vanishing to an open set of closed points.

### Examples

**Example 5.6.5 (curves).** Kawamata-Viehweg vanishing holds on every smooth projective curve $C$ in every characteristic. If $N - \Delta$ is nef and big, then $\deg N > \deg \Delta \geq 0$, so $\deg(-N) < 0$ and $H^1(C, \mathcal{O}(K_C + N)) \cong H^0(C, \mathcal{O}(-N))^\vee = 0$ by Serre duality. Proposition 5.6.1 is consistent: for $n = 1$ the only case is $i = 0$, and $H^0(C, L^{-1}) = 0$ for ample $L$. A Tango curve has a non-injective Frobenius on $H^1(C, \mathcal{O}(-D))$ (Proposition P7.11.3), but $H^1$ is the top degree, where no vanishing is claimed.

**Example 5.6.6 (no uniform bound).** By Theorem P7.11.4 and Example P7.11.5, for every prime $p$ there is a smooth projective surface over $\overline{\mathbb{F}}_p$ that violates Kodaira vanishing. So there is no $p_0$ such that Kodaira vanishing holds for all smooth projective surfaces in characteristic $p \geq p_0$, and the open set $U$ of Proposition 5.6.4 genuinely depends on the variety. Raynaud's surfaces do not lift to $W_2(k)$ for $p \geq 3$ (Corollary P7.11.11).

**Example 5.6.7 (the threefold of Proposition 5.6.3).** Let $X$ be a Raynaud surface with ample $L$ and $h^1(X, L^{-1}) = h \geq 1$. The proof of Proposition 5.6.3 gives
$$H^0(Z, R^1 \mu_* \omega_Y) = \bigoplus_{m \geq 0} H^1(X, \omega_X \otimes L^{m+1}),$$
a module over $\bigoplus_m H^0(X, L^m)$ that is nonzero in degree $0$, of dimension $h$ there, and zero in large degrees by Serre vanishing. So $R^1 \mu_* \omega_Y$ is a nonzero sheaf of finite length supported at the vertex. In characteristic $0$ the same construction with any smooth projective $X$ and ample $L$ gives $R^1 \mu_* \omega_Y = 0$, by Kodaira vanishing in each degree.

**Counterexample 5.6.8 (rational surfaces, Cascini and Tanaka).** For every algebraically closed field of characteristic $p > 0$ there is a smooth projective rational surface $X$ and a nef and big $\mathbb{Q}$-divisor that violates Kawamata-Viehweg vanishing (CT18). Smooth rational surfaces satisfy Kodaira vanishing for ample line bundles, by Theorem P7.11.10 for $p \geq 3$, since they lift to $W_2(k)$, so the failure is specific to the fractional and the nef and big parts of the statement. This is the reason Volume 11 needs a vanishing theorem for each class of surfaces it uses, and not a general Kawamata-Viehweg theorem.

### Proof

*Proof of Proposition 5.6.1.* For every $e \geq 0$, $(F^e)^* L^{-1} \cong L^{-p^e}$, and $F^*$ induces additive, $p$-linear maps $H^i(X, L^{-p^e}) \to H^i(X, L^{-p^{e+1}})$ whose composite is $(F^{e+1})^*$. By Serre duality, $H^i(X, L^{-p^e}) \cong H^{n-i}(X, \omega_X \otimes L^{p^e})^\vee$, and $n - i > 0$, so Serre vanishing gives $H^i(X, L^{-p^e}) = 0$ for $e$ large. Let $\xi \neq 0$ and let $e + 1$ be the least integer with $(F^{e+1})^* \xi = 0$; it exists and is positive, since $(F^0)^* \xi = \xi \neq 0$. Then $(F^e)^* \xi$ is a nonzero element of the kernel of $F^*$ on $H^i(X, L^{-p^e})$. The kernel of a $p$-linear map is a subgroup, so the map is not injective. $\square$

*Proof of Proposition 5.6.3.* The morphism $\pi$ is the total space of the line bundle $L^{-1}$, smooth of relative dimension $1$, so $Y$ is a smooth threefold. Since $\pi$ is affine with $\pi_* \mathcal{O}_Y = \bigoplus_{m \geq 0} L^m$, and $\Omega_{Y/X} = \pi^* L$ for the total space of $L^{-1}$, the exact sequence of differentials gives $\omega_Y = \pi^*(\omega_X \otimes L)$. By the projection formula,
$$\pi_* \omega_Y = \bigoplus_{m \geq 0} \omega_X \otimes L^{m+1}, \qquad H^1(Y, \omega_Y) = \bigoplus_{m \geq 0} H^1(X, \omega_X \otimes L^{m+1}),$$
since $\pi$ is affine. The summand $m = 0$ is $H^1(X, \omega_X \otimes L) \cong H^1(X, L^{-1})^\vee \neq 0$, by Serre duality on the surface $X$. The ring $R = \bigoplus_{m \geq 0} H^0(X, L^m)$ is finitely generated because $L$ is ample, $Z = \operatorname{Spec} R$ is the affine cone over $(X, L)$, and $\mu$, given by $R = H^0(Y, \mathcal{O}_Y)$, is proper and birational, an isomorphism outside the zero section, which it contracts to the vertex (Kol13, Section 3.1). Since $Z$ is affine, $H^0(Z, R^1 \mu_* \omega_Y) = H^1(Y, \omega_Y)$ by the Leray spectral sequence, and this is nonzero. $\square$

*Proof of Proposition 5.6.4.* The variety $X_0$, the divisors $N_0$ and the components of $\Delta_0$ are defined by finitely many equations with coefficients in $K$; let $A_1 \subseteq K$ be the $\mathbb{Z}$-algebra generated by these coefficients, so that they are defined over $A_1$. Smoothness and projectivity of the morphism, smoothness of the components of $\Delta_A$ and the snc condition, and ampleness of $N_A - \Delta_A$ hold on the generic fibre, so they hold over a dense open subset of $\operatorname{Spec} A_1$, by the standard results on spreading out (EGA IV, Sections 8, 9 and 12); shrinking, replace $A_1$ by a localization $A = A_1[1/a]$ over which they hold. The sheaf $\mathcal{F} = \mathcal{O}_{X_A}(K_{X_A / A} + N_A)$ is a line bundle on $X_A$, flat over $A$, and its restriction to each fibre is $\mathcal{O}(K + N)$ of that fibre. By Theorem P7.8.18 on the generic fibre, base changed to an algebraic closure of $K$, $H^i(X_0, \mathcal{O}(K_{X_0} + N_0)) = 0$ for $i > 0$. By Theorem P4.5.13 over the Noetherian base $\operatorname{Spec} A$, which applies to $\mathcal{F}$, the set of points $s$ with $h^i(s) \geq 1$ is closed for each $i$, and it does not contain the generic point. Its complement, intersected over $1 \leq i \leq \dim X_0$, is a dense open set $U$. For a closed point $s \in U$, flat base change from $\kappa(s)$ to $\overline{\kappa(s)}$ gives the vanishing on $X_{\bar s}$. Finally, the image of $U$ in $\operatorname{Spec} \mathbb{Z}$ is constructible by Chevalley's theorem and contains the generic point, since $A \subseteq K$ has characteristic $0$; so it contains all but finitely many primes, and the closed points over such a prime have that characteristic. $\square$

### Exercises

1. (A) Let $L$ be an ample line bundle on a smooth projective variety $X$ in characteristic $p$. Show that if $F^* \colon H^1(X, L^{-p^e}) \to H^1(X, L^{-p^{e+1}})$ is injective for every $e \geq 0$, then $H^1(X, L^{-1}) = 0$.
2. (A) Show that the extension $\mathcal{E}$ in Remark 5.6.2 is not split, while $F^* \mathcal{E}$ is, and compute $\deg \mathcal{E}$ and $\deg F^* \mathcal{E}$.
3. (B) In Proposition 5.6.3, show that the same construction with $X = \mathbb{P}^2$ and $L = \mathcal{O}(1)$ gives $Y \to Z = \mathbb{A}^3$, the blow-up of the origin, and that $R^1 \mu_* \omega_Y = 0$ in every characteristic.
4. (B) Show that in Proposition 5.6.4 the hypothesis that $N_0 - \Delta_0$ be ample can be replaced by nef and big, provided $N_0 - \Delta_0$ is written as an ample divisor plus an effective divisor as in Kodaira's lemma before spreading out. Where does the argument use that $\Delta_0$ is snc?
5. (B) Let $E$ be an elliptic curve in characteristic $p$. Show that Frobenius on $H^1(E, \mathcal{O}_E)$ is zero exactly when $E$ is supersingular, and that this does not contradict any vanishing theorem.
6. (C) Let $X$ be a smooth projective variety in characteristic $p$ with an ample $L$ and $H^i(X, L^{-1}) \neq 0$ for some $i < \dim X$. Deduce from Proposition 5.6.1 and Lemma P7.11.16 that $X$ is not F-split, and compare with Example P7.11.22.

### Lean

None of the statements of this section is in Lean.

### Notes and history

Raynaud's counterexample is from 1978 (Ray78); its exposition with explicit numerical conditions is Mukai's (Muk13), who also constructs counterexamples of higher dimension. The failure of Grauert-Riemenschneider through the cone construction is standard, and appears for example in Kollár's treatment of cones (Kol13, Section 3.1). Reduction modulo $p$ as in Proposition 5.6.4 goes back to the proof of Kodaira vanishing by Deligne and Illusie, and to Hara's work on rational singularities in large characteristic; the converse problem, that the reductions of a variety with a given singularity have a given F-singularity for $p \gg 0$, is the subject of Section 3. Counterexamples to Kawamata-Viehweg on rational surfaces in every characteristic were found by Cascini and Tanaka (CT18); for del Pezzo surfaces in large characteristic, vanishing does hold (Section 2).
