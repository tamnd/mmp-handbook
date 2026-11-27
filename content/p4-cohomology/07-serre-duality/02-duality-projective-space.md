---
title: Serre duality on projective space
nodes: []
sources: [Har77, Vak25, GW23, Stacks]
reads_with: [Har77:III.7, Vak25:ch30]
requires: [P2.3, P2.7, P3.12, P4.2, P4.7]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Serre duality on projective space

### Statement

Let $k$ be a field, $P = \mathbb{P}^n_k$ and $\omega_P = \mathcal{O}_P(-n-1)$, which is $\bigwedge^n \Omega_{P/k}$ by Corollary P3.12.22. For a finite-dimensional vector space $V$ write $V' = \operatorname{Hom}_k(V, k)$. By Theorem P4.2.1, $H^n(P, \omega_P)$ is one-dimensional with basis the class of $(x_0 \cdots x_n)^{-1}$. Let
$$t \colon H^n(P, \omega_P) \xrightarrow{\ \sim\ } k$$
be the isomorphism sending this class to $1$, the *trace*. For a coherent sheaf $\mathcal{F}$ on $P$, a map $\varphi \colon \mathcal{F} \to \omega_P$ induces $H^n(\varphi) \colon H^n(P, \mathcal{F}) \to H^n(P, \omega_P)$, and composing with $t$ gives the pairing
$$\operatorname{Hom}(\mathcal{F}, \omega_P) \times H^n(P, \mathcal{F}) \to k, \qquad (\varphi, \xi) \mapsto t(H^n(\varphi)(\xi)).$$

**Theorem P4.7.8 (Serre duality on projective space).** Let $\mathcal{F}$ be a coherent sheaf on $P = \mathbb{P}^n_k$.

1. The pairing above is perfect: it induces an isomorphism $\theta^0 \colon \operatorname{Hom}(\mathcal{F}, \omega_P) \xrightarrow{\sim} H^n(P, \mathcal{F})'$.
2. For every $i \geq 0$ there are isomorphisms
$$\theta^i \colon \operatorname{Ext}^i_P(\mathcal{F}, \omega_P) \xrightarrow{\ \sim\ } H^{n-i}(P, \mathcal{F})',$$
natural in $\mathcal{F}$, extending $\theta^0$ and compatible with the connecting maps of short exact sequences in $\mathcal{F}$.

Lean: not in Lean as stated.

**Corollary P4.7.9 (duality for vector bundles).** For a locally free sheaf $\mathcal{E}$ of finite rank on $\mathbb{P}^n_k$ and every $i$,
$$H^i(P, \mathcal{E}) \cong H^{n-i}(P, \mathcal{E}^\vee \otimes \omega_P)'.$$
In particular $h^i(\mathcal{E}) = h^{n-i}(\mathcal{E}^\vee(-n-1))$.

Lean: not in Lean as stated.

**Corollary P4.7.10 (negative twists).** For a locally free sheaf $\mathcal{E}$ of finite rank on $\mathbb{P}^n_k$, $H^i(P, \mathcal{E}(-q)) = 0$ for every $i < n$ and every $q$ large enough.

Lean: not in Lean as stated.

Corollary P4.7.10 is Serre vanishing read through duality. It fails for sheaves that are not locally free: for the skyscraper $k(p)$, $H^0(k(p)(-q)) = k$ for all $q$. Section 7.3 shows that this failure, for the sheaves $\mathcal{O}_X(-q)$ on a closed subscheme $X$, measures exactly how far $X$ is from being Cohen-Macaulay.

### Proof in words

For $\mathcal{F} = \mathcal{O}(m)$, part 1 is the perfect pairing between $H^0(\mathcal{O}(-m-n-1))$ and $H^n(\mathcal{O}(m))$ computed in Chapter 2. Both sides of part 1 are left exact contravariant functors of $\mathcal{F}$, since $H^n$ is right exact on $\mathbb{P}^n$, and every coherent sheaf has a presentation by sums of line bundles $\mathcal{O}(m)$, so part 1 follows by the five lemma. For part 2, both sides are contravariant $\delta$-functors in $\mathcal{F}$, and both vanish in positive degrees on the sums $\mathcal{O}(-q)^{\oplus m}$ for $q$ large, which cover every coherent sheaf. A $\delta$-functor with this property is universal, so the isomorphism in degree $0$ extends uniquely to a morphism of $\delta$-functors, and since both are universal, the extension is an isomorphism.

### Examples

**Example P4.7.11 (the projective line).** On $\mathbb{P}^1_k$, $\omega = \mathcal{O}(-2)$, and Corollary P4.7.9 for $\mathcal{E} = \mathcal{O}(d)$ says $h^1(\mathcal{O}(d)) = h^0(\mathcal{O}(-2-d))$, which is $-d - 1$ for $d \leq -2$ and $0$ otherwise, in agreement with Theorem P4.2.1. With $\chi(\mathcal{O}(d)) = d + 1$ this is the Riemann-Roch theorem (Theorem P4.3.16) on $\mathbb{P}^1$, where duality turns $h^1(D)$ into $h^0(K - D)$.

**Example P4.7.12 (the cotangent bundle of the plane).** Let $P = \mathbb{P}^2_k$. The Euler sequence $0 \to \Omega_P \to \mathcal{O}(-1)^{3} \to \mathcal{O} \to 0$ (Theorem P3.12.20) and Theorem P4.2.1 give $H^0(\Omega_P) = 0$, $H^1(\Omega_P) \cong H^0(\mathcal{O}) = k$ and $H^2(\Omega_P) = 0$, since $\mathcal{O}(-1)$ has no cohomology on $\mathbb{P}^2$. For a locally free sheaf of rank $2$, $\mathcal{E}^\vee \otimes \bigwedge^2 \mathcal{E} \cong \mathcal{E}$ by the pairing $\mathcal{E} \otimes \mathcal{E} \to \bigwedge^2 \mathcal{E}$, so $\Omega_P^\vee \otimes \omega_P \cong \Omega_P$, and Corollary P4.7.9 says $h^i(\Omega_P) = h^{2-i}(\Omega_P)$. The numbers $0, 1, 0$ are symmetric, as they must be. The class spanning $H^1(\Omega_P)$ is the first Chern class of $\mathcal{O}(1)$.

**Example P4.7.13 (a skyscraper sheaf).** Let $p \in \mathbb{P}^n_k$ be a $k$-point. Then $\operatorname{Hom}(k(p), \omega_P) = 0$ and $H^n(k(p)) = 0$ for $n \geq 1$, which is part 1. For part 2 in degree $n$, $\operatorname{Ext}^n(k(p), \omega_P) \cong H^0(k(p))' = k$. Locally at $p$ the Koszul resolution of $k(p)$ by the $n$ local equations of $p$ shows $\mathcal{E}xt^i(k(p), \omega_P) = 0$ for $i \neq n$ and $\mathcal{E}xt^n(k(p), \omega_P) \cong k(p)$ (Exercise 3 of Section 7.1 for $n = 2$). Since these sheaves are skyscrapers, the spectral sequence relating groups and sheaves degenerates, and $\operatorname{Ext}^n(k(p), \omega_P) = \Gamma(\mathcal{E}xt^n(k(p), \omega_P)) = k$, as duality predicts.

### Proof

*Theorem P4.7.8, part 1.* Both sides are additive contravariant functors of $\mathcal{F}$, and $\theta^0$ is natural in $\mathcal{F}$.

*Step 1: line bundles.* Let $\mathcal{F} = \mathcal{O}(m)$. Then $\operatorname{Hom}(\mathcal{O}(m), \omega_P) = H^0(P, \mathcal{O}(-m-n-1))$, and for $\varphi$ given by a form $g$ of degree $-m-n-1$, $H^n(\varphi)$ is multiplication by $g$ from $H^n(\mathcal{O}(m))$ to $H^n(\mathcal{O}(-n-1))$. So the pairing of part 1 is the multiplication pairing
$$H^0(P, \mathcal{O}(-m-n-1)) \times H^n(P, \mathcal{O}(m)) \to H^n(P, \mathcal{O}(-n-1)) \xrightarrow{t} k,$$
which is perfect by part 4 of Theorem P4.2.1 if $-m-n-1 \geq 0$. If $-m-n-1 < 0$, both spaces are zero by parts 1 and 2 of Theorem P4.2.1. By additivity, $\theta^0$ is an isomorphism for every finite sum of line bundles $\mathcal{O}(m)$.

*Step 2: exactness.* The functor $\operatorname{Hom}(-, \omega_P)$ sends a right exact sequence $\mathcal{F}_1 \to \mathcal{F}_0 \to \mathcal{F} \to 0$ to a left exact sequence. The functor $H^n(P, -)$ is right exact, since $H^{n+1}(P, -) = 0$ on quasi-coherent sheaves by Theorem P2.7.13, since $P$ has dimension $n$, and dualizing a right exact sequence of vector spaces gives a left exact sequence. So $0 \to H^n(\mathcal{F})' \to H^n(\mathcal{F}_0)' \to H^n(\mathcal{F}_1)'$ is exact.

*Step 3.* By Theorem P3.6.23 there is a surjection $\mathcal{F}_0 = \mathcal{O}(-a)^{\oplus m} \to \mathcal{F}$, and applying the same to its kernel gives a presentation $\mathcal{F}_1 \to \mathcal{F}_0 \to \mathcal{F} \to 0$ with $\mathcal{F}_1$, $\mathcal{F}_0$ sums of line bundles. In the commutative diagram
$$\begin{array}{ccccccc} 0 \to & \operatorname{Hom}(\mathcal{F}, \omega_P) & \to & \operatorname{Hom}(\mathcal{F}_0, \omega_P) & \to & \operatorname{Hom}(\mathcal{F}_1, \omega_P) \\ & \downarrow \theta^0 & & \downarrow \theta^0 & & \downarrow \theta^0 \\ 0 \to & H^n(\mathcal{F})' & \to & H^n(\mathcal{F}_0)' & \to & H^n(\mathcal{F}_1)' \end{array}$$
the rows are exact by Step 2 and the second and third vertical maps are isomorphisms by Step 1. So the first is an isomorphism. $\square$

*Theorem P4.7.8, part 2.* View both sides as covariant functors on the opposite category $\mathsf{Coh}(P)^{\mathrm{op}}$, which is abelian. A short exact sequence $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ gives the long exact sequence of $\operatorname{Ext}^i(-, \omega_P)$ by part 3 of Proposition P4.7.2, and the long exact sequence of $H^{n-i}(-)'$ by Theorem P2.7.3 and exactness of $V \mapsto V'$, with the indices running the same way. So $S^i = \operatorname{Ext}^i(-, \omega_P)$ and $T^i = H^{n-i}(-)'$ are $\delta$-functors on $\mathsf{Coh}(P)^{\mathrm{op}}$, for $i \geq 0$.

*Both are effaceable.* In $\mathsf{Coh}(P)^{\mathrm{op}}$ a monomorphism $\mathcal{F} \to \mathcal{M}$ is a surjection $\mathcal{M} \to \mathcal{F}$ of coherent sheaves. Every $\mathcal{F}$ is a quotient of $\mathcal{M} = \mathcal{O}(-q)^{\oplus m}$ for every $q$ large enough, by Theorem P3.6.23. For $i > 0$ and $q > 0$:
- $S^i(\mathcal{M}) = H^i(P, \omega_P(q))^{\oplus m} = H^i(P, \mathcal{O}(q - n - 1))^{\oplus m}$ by part 4 of Proposition P4.7.2, which is $0$ for $0 < i < n$ by part 3 of Theorem P4.2.1 and for $i = n$ by part 2, since $q - n - 1 > -n - 1$;
- $T^i(\mathcal{M}) = H^{n-i}(P, \mathcal{O}(-q))'^{\oplus m}$, which is $0$ for $0 < n - i < n$ by part 3 of Theorem P4.2.1 and for $n - i = 0$ by part 1, since $-q < 0$.

So both $\delta$-functors are effaceable. The proof of Corollary P2.3.23 shows that an effaceable $\delta$-functor is universal: its construction of the extension uses only the existence of effacing monomorphisms, not injective objects. By universality of $(S^i)$, the isomorphism $\theta^0 \colon S^0 \to T^0$ of part 1 extends uniquely to a morphism of $\delta$-functors $\theta \colon S \to T$. By universality of $(T^i)$, the inverse of $\theta^0$ extends uniquely to $\eta \colon T \to S$. Then $\eta \circ \theta$ and $\theta \circ \eta$ extend the identities in degree $0$, so by uniqueness they are the identities. So every $\theta^i$ is an isomorphism. $\square$

*Corollary P4.7.9.* By part 4 of Proposition P4.7.2, $\operatorname{Ext}^{n-i}(\mathcal{E}, \omega_P) = H^{n-i}(P, \mathcal{E}^\vee \otimes \omega_P)$, and by Theorem P4.7.8 it is $H^i(P, \mathcal{E})'$. Dualize. $\square$

*Corollary P4.7.10.* By Corollary P4.7.9, $H^i(P, \mathcal{E}(-q)) \cong H^{n-i}(P, \mathcal{E}^\vee \otimes \omega_P(q))'$, and for $n - i > 0$ this vanishes for $q$ large by part 2 of Theorem P4.2.7. $\square$

### Exercises

1. (A) Use Corollary P4.7.9 to compute $h^i(\mathbb{P}^n, \mathcal{O}(m))$ for $i = n$ from the case $i = 0$, and check it against Theorem P4.2.1.
2. (A) Let $\mathcal{E}$ be locally free on $\mathbb{P}^n_k$. Show that $\chi(\mathcal{E}) = (-1)^n \chi(\mathcal{E}^\vee(-n-1))$, and check it for $\mathcal{E} = \mathcal{O}(m)$ with the Hilbert polynomial $\binom{m + n}{n}$.
3. (B) Show that Theorem P4.7.8 holds over any Noetherian ring $A$ in place of $k$ for $\mathcal{F}$ locally free, with $V' = \operatorname{Hom}_A(V, A)$ in part 1, but that part 2 fails in general: compare both sides for $A = \mathbb{Z}$, $n = 0$, $i = 1$ and $\mathcal{F} = (\mathbb{Z}/p)^\sim$.
4. (B) Compute $h^i(\mathbb{P}^n, \Omega^p)$ for all $i$, $p$ using the exterior powers of the Euler sequence, and check the symmetry $h^i(\Omega^p) = h^{n-i}(\Omega^{n-p})$ predicted by Corollary P4.7.9 and the pairing $\Omega^p \otimes \Omega^{n-p} \to \omega_P$.
5. (B) Let $C \subseteq \mathbb{P}^2_k$ be a plane curve of degree $d$. Using $0 \to \mathcal{O}(-d) \to \mathcal{O} \to \mathcal{O}_C \to 0$ and Theorem P4.7.8, show that $\operatorname{Ext}^1_P(\mathcal{O}_C, \omega_P) \cong H^1(C, \mathcal{O}_C)'$, and compute both sides as $\binom{d - 1}{2}$-dimensional.
6. (C) Prove the projective space case of the theorem on the trace: for a finite morphism $\pi \colon \mathbb{P}^n_k \to \mathbb{P}^n_k$ given by $n + 1$ forms of degree $e$ with no common zero, construct a trace map $H^n(\pi_* \omega_P) \to H^n(\omega_P)$ compatible with $t$, and show that $\pi_* \omega_P \cong \mathcal{H}om(\pi_* \mathcal{O}_P, \omega_P)$. (Use part 1 of Theorem P4.7.8 twice.)

### Lean

Mathlib has neither the cohomology of $\mathcal{O}(m)$ on projective space nor Serre duality. It has right derived functors of additive functors (`CategoryTheory.Functor.rightDerived`). The handbook adds no `MinimalModel` node here.

### Notes and history

Serre proved the duality theorem for vector bundles on smooth projective varieties in *Un théorème de dualité* (1955), with the analytic version for compact complex manifolds proved through Dolbeault cohomology. Grothendieck reformulated it for coherent sheaves on projective schemes with $\operatorname{Ext}^i(\mathcal{F}, \omega)$ in 1957, and the proof on projective space by universal $\delta$-functors is Hartshorne's proof of III.7.1. The literature state is theorem. In the minimal model program, Corollary P4.7.9 is the prototype of every computation that converts a vanishing $H^i(K_X + L) = 0$ into a vanishing $H^{n-i}(-L) = 0$, the form in which Kodaira vanishing is used in Volume 5.
