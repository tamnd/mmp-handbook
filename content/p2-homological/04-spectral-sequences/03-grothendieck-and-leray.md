---
title: The Grothendieck and Leray spectral sequences
nodes: []
sources: [Wei94, Gro57, Har77, KM98]
reads_with: [Wei94:ch5, Gro57:ch2, Har77:ch3, KM98:ch5]
requires: [P2.3, P2.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Grothendieck and Leray spectral sequences

### Statement

Throughout, $\mathcal{A}$ and $\mathcal{B}$ are abelian categories with enough injectives, and $\mathcal{C}$ is abelian. A complex $K^\bullet$ is *nonnegative* if $K^p = 0$ for $p < 0$. For a complex $K^\bullet$ write $Z^p(K)$, $B^p(K)$ and $H^p(K)$ for its cycles, boundaries and cohomology in degree $p$.

**Definition P2.4.21 (Cartan-Eilenberg resolution).** Let $K^\bullet$ be a nonnegative complex in $\mathcal{A}$. A *Cartan-Eilenberg resolution* of $K^\bullet$ is a first quadrant double complex $I^{\bullet,\bullet}$ of injective objects, with commuting squares, together with a map of complexes $\varepsilon: K^\bullet \to I^{\bullet,0}$ such that, for each $p$, the following columns, with the maps induced by $\varepsilon$, are injective resolutions:
$$Z^p(K) \to Z_h^p(I^{\bullet,\bullet}), \qquad B^p(K) \to B_h^p(I^{\bullet,\bullet}), \qquad H^p(K) \to H_h^p(I^{\bullet,\bullet}).$$
Here $Z_h^p(I^{\bullet,\bullet})$ is the column $q \mapsto \ker(d_h: I^{p,q} \to I^{p+1,q})$ with the maps induced by $d_v$, and similarly for $B_h^p$ and $H_h^p$.

**Proposition P2.4.22 (Cartan-Eilenberg resolutions).** Let $K^\bullet$ be a nonnegative complex in $\mathcal{A}$.

1. $K^\bullet$ has a Cartan-Eilenberg resolution.
2. In a Cartan-Eilenberg resolution, each column $K^p \to I^{p,\bullet}$ is an injective resolution of $K^p$.
3. In each row $I^{\bullet,q}$, the short exact sequences $0 \to Z_h^p \to I^{p,q} \to B_h^{p+1} \to 0$ and $0 \to B_h^p \to Z_h^p \to H_h^p \to 0$ split. So for every left exact functor $F: \mathcal{A} \to \mathcal{C}$ there are natural isomorphisms $H_h^p(F(I^{\bullet,q})) \cong F(H_h^p(I^{\bullet,q}))$, compatible with the maps induced by $d_v$.

Lean: not in Lean as stated.

**Definition P2.4.23 (hypercohomology).** Let $F: \mathcal{A} \to \mathcal{C}$ be left exact, $K^\bullet$ a nonnegative complex, and $I^{\bullet,\bullet}$ a Cartan-Eilenberg resolution. The *hyperderived functors* of $F$ at $K^\bullet$ are
$$\mathbb{R}^n F(K^\bullet) = H^n(\operatorname{Tot} F(I^{\bullet,\bullet})),$$
with the signs of Section 4.2 on $F(I^{\bullet,\bullet})$. For $F = \Gamma(X, -)$ on sheaves these are the *hypercohomology groups* $\mathbb{H}^n(X, K^\bullet)$.

Two Cartan-Eilenberg resolutions of $K^\bullet$ are homotopy equivalent as double complexes, and a map $K^\bullet \to L^\bullet$ lifts to a map of Cartan-Eilenberg resolutions, unique up to homotopy (Weibel, Chapter 5). So $\mathbb{R}^n F(K^\bullet)$ does not depend on the choice and is functorial in $K^\bullet$. If $K^\bullet = A$ is one object in degree $0$, an injective resolution of $A$ placed in the column $0$ is a Cartan-Eilenberg resolution, so $\mathbb{R}^n F(A) = R^n F(A)$.

**Theorem P2.4.24 (the hypercohomology spectral sequences).** Let $F: \mathcal{A} \to \mathcal{C}$ be left exact and $K^\bullet$ a nonnegative complex in $\mathcal{A}$. There are two convergent first quadrant spectral sequences
$${}^{I}E_1^{p,q} = R^q F(K^p) \Rightarrow \mathbb{R}^{p+q} F(K^\bullet), \qquad {}^{II}E_2^{p,q} = R^p F(H^q(K^\bullet)) \Rightarrow \mathbb{R}^{p+q} F(K^\bullet).$$
In the first, $d_1: R^q F(K^p) \to R^q F(K^{p+1})$ is induced by the differential of $K^\bullet$.

Lean: not in Lean as stated.

**Theorem P2.4.25 (Grothendieck spectral sequence).** Let $G: \mathcal{A} \to \mathcal{B}$ and $F: \mathcal{B} \to \mathcal{C}$ be left exact, and suppose that $G$ sends injective objects to $F$-acyclic objects. Then for each object $A$ of $\mathcal{A}$ there is a convergent first quadrant spectral sequence
$$E_2^{p,q} = R^p F(R^q G(A)) \Rightarrow R^{p+q}(F G)(A).$$

Lean: not in Lean as stated.

The spectral sequence is natural in $A$ from page $2$ on (Weibel, Chapter 5). Its five-term exact sequence is
$$0 \to R^1 F(G A) \to R^1(F G)(A) \to F(R^1 G(A)) \to R^2 F(G A) \to R^2(F G)(A).$$

**Corollary P2.4.26 (Leray spectral sequence).** Let $f: X \to Y$ be a continuous map and $\mathcal{F}$ a sheaf of abelian groups on $X$. There is a convergent first quadrant spectral sequence
$$E_2^{p,q} = H^p(Y, R^q f_* \mathcal{F}) \Rightarrow H^{p+q}(X, \mathcal{F}).$$
For a second map $g: Y \to Z$ there is a spectral sequence $E_2^{p,q} = R^p g_* (R^q f_* \mathcal{F}) \Rightarrow R^{p+q}(g f)_* \mathcal{F}$. The same holds for a morphism of ringed spaces and a sheaf of $\mathcal{O}_X$-modules, with the same groups.

Lean: not in Lean as stated.

**Corollary P2.4.27 (vanishing of higher direct images).** Let $f: X \to Y$ and $\mathcal{F}$ be as above.

1. If $R^q f_* \mathcal{F} = 0$ for all $q > 0$, then $H^n(X, \mathcal{F}) \cong H^n(Y, f_* \mathcal{F})$ for all $n$.
2. In general there is an exact sequence
$$0 \to H^1(Y, f_* \mathcal{F}) \to H^1(X, \mathcal{F}) \to H^0(Y, R^1 f_* \mathcal{F}) \to H^2(Y, f_* \mathcal{F}) \to H^2(X, \mathcal{F}).$$

Lean: not in Lean as stated.

### Proof in words

To compose two derived functors, resolve twice. An injective resolution $J^\bullet$ of $A$ computes the derived functors of $G$: the complex $G(J^\bullet)$ has cohomology $R^q G(A)$. To apply $F$ to this complex, resolve it once more, now by a double complex $I^{\bullet,\bullet}$. A Cartan-Eilenberg resolution is a double complex that resolves the complex, its cycles, its boundaries and its cohomology all at once, with split rows. The two spectral sequences of $F(I^{\bullet,\bullet})$ then see two things. Column by column, $F$ meets the objects $G(J^p)$, which are $F$-acyclic by assumption, so only $F G(J^\bullet)$ survives, and its cohomology is $R^n(F G)(A)$. Row by row, the split rows let $F$ pass through cohomology, so $F$ meets the objects $H^q(G(J^\bullet)) = R^q G(A)$ and their resolutions, and page $2$ is $R^p F(R^q G(A))$.

Sheaf cohomology on $X$ is the composite of the pushforward $f_*$ and sheaf cohomology on $Y$, and $f_*$ preserves injectives. So the Grothendieck spectral sequence applies and gives Leray's spectral sequence. When the higher direct images vanish, the spectral sequence has one row, and the cohomology on $X$ is the cohomology of $f_* \mathcal{F}$ on $Y$.

### Examples

**Example P2.4.28 (rational singularities and the minimal model program).** Let $X$ be a variety over a field of characteristic $0$ and $f: Y \to X$ a resolution of singularities. The variety $X$ has *rational singularities* if $f_* \mathcal{O}_Y = \mathcal{O}_X$ and $R^i f_* \mathcal{O}_Y = 0$ for all $i > 0$. If this holds for one resolution, it holds for every resolution (Kollár and Mori, Chapter 5). Then part 1 of the corollary gives $H^i(Y, \mathcal{O}_Y) \cong H^i(X, \mathcal{O}_X)$ for all $i$. Kawamata log terminal singularities are rational (Kollár and Mori, Chapter 5), and the proof uses the vanishing theorems of P7 Ch. 8 and 9. So for the varieties of the minimal model program, the cohomology of the structure sheaf can be computed on any resolution. In particular $h^i(X, \mathcal{O}_X)$ is a birational invariant of projective varieties with klt singularities (Exercise 5).

**Example P2.4.29 (contractions).** Let $(X, \Delta)$ be a klt pair, $X$ projective, and $f: X \to Z$ the contraction of a $(K_X + \Delta)$-negative extremal ray (Volume 7). Then $f_* \mathcal{O}_X = \mathcal{O}_Z$, and $-(K_X + \Delta)$ is $f$-ample. The relative Kawamata-Viehweg vanishing theorem, applied to the divisor $0 = K_X + \Delta + (-(K_X + \Delta))$, gives $R^i f_* \mathcal{O}_X = 0$ for $i > 0$. So $H^i(X, \mathcal{O}_X) \cong H^i(Z, \mathcal{O}_Z)$ for all $i$. The five-term sequence for $\mathcal{O}_X^\times$ shows that $f^*: \operatorname{Pic} Z \to \operatorname{Pic} X$ is injective (Exercise 6). With the contraction theorem, which says that a line bundle of degree $0$ on the curves of the ray comes from $Z$, this identifies $\operatorname{Pic} Z$ with the group of line bundles on $X$ of degree $0$ on the curves of the ray.

**Example P2.4.30 (the Hodge to de Rham spectral sequence).** Let $X$ be a smooth variety over a field $k$, and $\Omega_X^\bullet$ its de Rham complex, a nonnegative complex of sheaves of $k$-vector spaces whose differential is $k$-linear but not $\mathcal{O}_X$-linear. The algebraic de Rham cohomology is $H^n_{\mathrm{dR}}(X/k) = \mathbb{H}^n(X, \Omega_X^\bullet)$. The first hypercohomology spectral sequence is the *Hodge to de Rham spectral sequence*
$$E_1^{p,q} = H^q(X, \Omega_X^p) \Rightarrow H^{p+q}_{\mathrm{dR}}(X/k).$$
If $X$ is smooth and projective over a field of characteristic $0$, it degenerates on page $1$. This is a consequence of Hodge theory. Deligne and Illusie proved in 1987 that it also degenerates on page $1$ when $X$ is smooth and proper over a perfect field of characteristic $p > \dim X$ and lifts to the Witt vectors $W_2(k)$, and deduced the Kodaira vanishing theorem for such $X$ (P7 Ch. 11). Esnault and Viehweg derive the Kawamata-Viehweg vanishing theorem from the degeneration of a logarithmic version of this spectral sequence on cyclic covers (P7 Ch. 8).

**Example P2.4.31 (local to global Ext).** Let $X$ be a ringed space and $\mathcal{F}$, $\mathcal{G}$ sheaves of $\mathcal{O}_X$-modules. Then $\operatorname{Hom}(\mathcal{F}, -) = \Gamma(X, -) \circ \mathcal{H}om(\mathcal{F}, -)$, and $\mathcal{H}om(\mathcal{F}, \mathcal{I})$ is flasque for an injective $\mathcal{I}$ (P4 Ch. 8). Flasque sheaves are acyclic (Chapter 7), so the Grothendieck spectral sequence gives
$$E_2^{p,q} = H^p(X, \mathcal{E}xt^q(\mathcal{F}, \mathcal{G})) \Rightarrow \operatorname{Ext}^{p+q}(\mathcal{F}, \mathcal{G}).$$
Serre duality (P4 Ch. 7) and the deformation theory of the Hom and Hilbert schemes (P8 Ch. 1) use it in this form: if $\mathcal{F}$ is locally free, $\mathcal{E}xt^q(\mathcal{F}, \mathcal{G}) = 0$ for $q > 0$ and $\operatorname{Ext}^n(\mathcal{F}, \mathcal{G}) = H^n(X, \mathcal{F}^\vee \otimes \mathcal{G})$.

### Proof

*Proof of the proposition on Cartan-Eilenberg resolutions.* For part 1, the proof resolves the short exact sequences
$$0 \to B^p(K) \to Z^p(K) \to H^p(K) \to 0, \qquad 0 \to Z^p(K) \to K^p \to B^{p+1}(K) \to 0.$$
Choose injective resolutions of each $B^p(K)$ and each $H^p(K)$. The horseshoe lemma of Section 3.2, applied to the first sequence, gives an injective resolution of $Z^p(K)$ that is degreewise the direct sum of the two. Applied to the second sequence, it gives an injective resolution $I^{p,\bullet}$ of $K^p$ that is degreewise the direct sum of the resolutions of $Z^p(K)$ and $B^{p+1}(K)$. Define $d_h: I^{p,\bullet} \to I^{p+1,\bullet}$ as the composite $I^{p,\bullet} \to (\text{resolution of } B^{p+1}) \to (\text{resolution of } Z^{p+1}) \to I^{p+1,\bullet}$ of the projection and the two inclusions. Then $d_h d_h = 0$, the squares commute, and the cycles, boundaries and cohomology of the rows are the chosen resolutions. The details are in Weibel, Chapter 5.

For part 2, the sequence $0 \to Z_h^p \to I^{p,\bullet} \to B_h^{p+1} \to 0$ of columns is exact in each degree, and the augmented columns for $Z_h^p$ and $B_h^{p+1}$ are exact. The long exact sequence of Section 3.1, applied to the augmented columns, shows that the augmented column $K^p \to I^{p,\bullet}$ is exact. Each $I^{p,q}$ is injective by definition.

For part 3, each $B_h^{p}$, $Z_h^p$ and $H_h^p$ in degree $q$ is a term of an injective resolution, so it is injective. A short exact sequence that starts with an injective object splits. So the two sequences split. A choice of splittings writes the row $I^{\bullet,q}$ as a direct sum of complexes of two kinds: $H^p$ in degree $p$ with zero differential, and $B^{p+1} \xrightarrow{1} B^{p+1}$ in degrees $p$ and $p+1$. An additive functor preserves such a decomposition, so $H^p(F(I^{\bullet,q})) \cong F(H^p_h(I^{\bullet,q}))$. To see that the isomorphism does not depend on the splitting and is natural, describe it without the splitting. Since $F$ is left exact, $F(Z_h^p) = \ker(F(I^{p,q}) \to F(I^{p+1,q}))$. The map $F(I^{p-1,q}) \to F(B_h^p)$ is a split epimorphism, so the image of $F(I^{p-1,q})$ in $F(Z_h^p)$ is $F(B_h^p)$. So $H^p(F(I^{\bullet,q})) = F(Z_h^p)/F(B_h^p)$, and $F(Z_h^p)/F(B_h^p) = F(H_h^p)$ by the split sequence. These identifications are made of kernels and cokernels of maps induced by $d_h$, so they commute with the maps induced by $d_v$. $\square$

*Proof of the hypercohomology spectral sequences.* Let $I^{\bullet,\bullet}$ be a Cartan-Eilenberg resolution of $K^\bullet$, and apply the theorem of Section 4.2 to the double complex $F(I^{\bullet,\bullet})$, with the signs inserted.

The column filtration gives ${}^{I}E_1^{p,q} = H^q(F(I^{p,\bullet}))$. By part 2 of the proposition, $I^{p,\bullet}$ is an injective resolution of $K^p$, so ${}^{I}E_1^{p,q} = R^q F(K^p)$. The map $d_1$ is induced by $d_h$, which lies over the differential of $K^\bullet$. So $d_1$ is $R^q F$ of the differential of $K^\bullet$, by the comparison theorem of Section 3.2.

The row filtration gives ${}^{II}E_1^{p,q} = H_h^q(F(I^{\bullet,p}))$, with $d_1$ induced by $d_v$. By part 3 of the proposition, this is $F(H_h^q(I^{\bullet,p}))$, compatibly with the maps induced by $d_v$. So the row $q$ of page $1$, as $p$ varies, is $F$ applied to the column $H_h^q(I^{\bullet,\bullet})$, which is an injective resolution of $H^q(K^\bullet)$. Its cohomology in degree $p$ is $R^p F(H^q(K^\bullet))$. So ${}^{II}E_2^{p,q} = R^p F(H^q(K^\bullet))$. $\square$

*Proof of the Grothendieck spectral sequence.* Let $A \to J^\bullet$ be an injective resolution in $\mathcal{A}$, and let $K^\bullet = G(J^\bullet)$, a nonnegative complex in $\mathcal{B}$. Its cohomology is $H^q(K^\bullet) = R^q G(A)$ by definition. Apply the hypercohomology spectral sequences to $F$ and $K^\bullet$.

In the first, ${}^{I}E_1^{p,q} = R^q F(G(J^p))$. This is zero for $q > 0$, since $G(J^p)$ is $F$-acyclic, and equal to $F G(J^p)$ for $q = 0$, with $d_1$ induced by the differential of $F G(J^\bullet)$. So ${}^{I}E_2^{p,q} = 0$ for $q > 0$ and ${}^{I}E_2^{p,0} = H^p(F G(J^\bullet)) = R^p(F G)(A)$, since $F G$ is left exact. By the proposition on edge maps of Section 4.1, $\mathbb{R}^n F(K^\bullet) \cong R^n(F G)(A)$.

In the second, ${}^{II}E_2^{p,q} = R^p F(H^q(K^\bullet)) = R^p F(R^q G(A))$, and it converges to $\mathbb{R}^{p+q} F(K^\bullet) \cong R^{p+q}(F G)(A)$. The five-term sequence is the theorem of Section 4.1. $\square$

*Proof of the Leray spectral sequence.* For a sheaf $\mathcal{F}$ on $X$, $\Gamma(Y, f_* \mathcal{F}) = \mathcal{F}(f^{-1}(Y)) = \Gamma(X, \mathcal{F})$. So $\Gamma(X, -) = \Gamma(Y, -) \circ f_*$. Both functors are left exact (Chapter 5). The pushforward $f_*$ has the exact left adjoint $f^{-1}$ (Chapter 5), so it sends injective sheaves to injective sheaves (Section 3.3, Exercise 4), which are $\Gamma(Y, -)$-acyclic. The Grothendieck spectral sequence applies, with $R^q f_*$ the derived functors of $f_*$ (Chapter 7, P4 Ch. 4). The same argument with $g_*$ in place of $\Gamma(Y, -)$, and $(g f)_* = g_* f_*$, gives the second spectral sequence.

For a morphism of ringed spaces, the left adjoint $f^*$ of $f_*$ on sheaves of modules need not be exact. Instead, Chapter 7 proves that injective $\mathcal{O}_X$-modules are flasque, that $f_*$ of a flasque sheaf is flasque, and that flasque sheaves are acyclic for $\Gamma(Y, -)$ and for $g_*$. So the hypothesis of the Grothendieck spectral sequence holds. Chapter 7 also proves that the derived functors of $\Gamma$ and of $f_*$ computed in $\mathcal{O}_X$-modules agree with those computed in sheaves of abelian groups, so the groups are the same. $\square$

*Proof of the corollary on vanishing of higher direct images.* For part 1, the page $E_2^{p,q} = H^p(Y, R^q f_* \mathcal{F})$ vanishes for $q > 0$. By the proposition on edge maps of Section 4.1, the edge maps $H^n(Y, f_* \mathcal{F}) = E_2^{n,0} \to H^n(X, \mathcal{F})$ are isomorphisms. Part 2 is the five-term exact sequence of Section 4.1 for the Leray spectral sequence. $\square$

### Exercises

1. (A) Let $F$ be left exact and $K^\bullet$ a nonnegative complex of $F$-acyclic objects. Show that $\mathbb{R}^n F(K^\bullet) \cong H^n(F(K^\bullet))$. If also $K^\bullet$ is a resolution of an object $A$, deduce again that $R^n F(A) \cong H^n(F(K^\bullet))$, as in Section 3.3.
2. (A) Let $i: Z \to X$ be the inclusion of a closed subset. Granting that $i_*$ is exact (Chapter 5), show that $H^n(Z, \mathcal{F}) \cong H^n(X, i_* \mathcal{F})$ for every sheaf $\mathcal{F}$ on $Z$.
3. (A) Let $E$ be a locally free sheaf of finite rank on a ringed space $X$. Granting that $\mathcal{E}xt^q(E, \mathcal{G}) = 0$ for $q > 0$, use the local to global spectral sequence to show $\operatorname{Ext}^n(E, \mathcal{G}) \cong H^n(X, E^\vee \otimes \mathcal{G})$.
4. (B) Write the five-term exact sequence of the spectral sequence $R^p g_* R^q f_* \mathcal{F} \Rightarrow R^{p+q}(g f)_* \mathcal{F}$. Show that if $R^q f_* \mathcal{F} = 0$ for $q > 0$, then $R^n (g f)_* \mathcal{F} \cong R^n g_* (f_* \mathcal{F})$.
5. (B) Let $X$ and $X'$ be projective varieties over a field of characteristic $0$ with rational singularities, and $X \dashrightarrow X'$ a birational map. Using a resolution $W$ of the closure of its graph, show that $H^i(X, \mathcal{O}_X) \cong H^i(X', \mathcal{O}_{X'})$ for all $i$. Deduce that the flips and divisorial contractions of a klt minimal model program do not change $h^i(\mathcal{O})$.
6. (B) Let $f: X \to Y$ be a morphism of schemes with $f_* \mathcal{O}_X = \mathcal{O}_Y$. Show that $f_* \mathcal{O}_X^\times = \mathcal{O}_Y^\times$. Using $\operatorname{Pic} X \cong H^1(X, \mathcal{O}_X^\times)$, show that $f^*: \operatorname{Pic} Y \to \operatorname{Pic} X$ is injective, and that its image is the kernel of $\operatorname{Pic} X \to H^0(Y, R^1 f_* \mathcal{O}_X^\times)$.
7. (B) Let $G$ be a group and $N$ a normal subgroup. Show that $M \mapsto M^N$, from $G$-modules to $G/N$-modules, sends injectives to injectives. Deduce the Hochschild-Serre spectral sequence $H^p(G/N, H^q(N, M)) \Rightarrow H^{p+q}(G, M)$ and the inflation-restriction sequence of Section 4.1.
8. (C) Prove part 1 of the proposition on Cartan-Eilenberg resolutions in full: check that the horizontal maps defined in the proof commute with the vertical maps, and that the cycles, boundaries and cohomology of the rows are the chosen resolutions.

### Lean

Mathlib provides the general machine of spectral objects after Verdier, `CategoryTheory.Abelian.SpectralObject`, from which `CategoryTheory.Abelian.SpectralObject.spectralSequence` builds spectral sequences. Cartan-Eilenberg resolutions, hyperderived functors, the Grothendieck spectral sequence and the Leray spectral sequence are not yet in Mathlib in this form. In the language of Chapter 8, the Grothendieck spectral sequence comes from the isomorphism $\mathbf{R}(F G) \cong \mathbf{R} F \circ \mathbf{R} G$ of total derived functors, and this is the form a formalization would likely take. The handbook adds no `MinimalModel` node here.

### Notes and history

Leray constructed his spectral sequence for a continuous map in the 1940s, as the first application of sheaves. Cartan and Eilenberg's book of 1956 introduced the resolutions that bear their names and hyperderived functors. Grothendieck's Tohoku paper of 1957 proved the spectral sequence of a composite functor in the generality of abelian categories, and derived the Leray spectral sequence and the local to global Ext spectral sequence from it. Deligne and Illusie's proof of the degeneration of the Hodge to de Rham spectral sequence in characteristic $p$ is from 1987.
