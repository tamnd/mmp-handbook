---
title: Serre's finiteness and vanishing theorems
nodes: []
sources: [Har77, Vak25, Ser55, Stacks]
reads_with: [Har77:III.5, Vak25:ch18]
requires: [P1.2, P2.7, P3.4, P3.5, P3.6, P4.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Serre's finiteness and vanishing theorems

### Statement

Let $A$ be a Noetherian ring and $X$ a projective scheme over $A$ in the sense of Definition P3.4.29, with a closed immersion $i \colon X \to \mathbb{P}^r_A$ over $A$. Write $\mathcal{O}_X(1) = i^* \mathcal{O}(1)$ and $\mathcal{F}(n) = \mathcal{F} \otimes \mathcal{O}_X(1)^{\otimes n}$.

**Theorem P4.2.7 (Serre).** For every coherent sheaf $\mathcal{F}$ on $X$:

1. $H^p(X, \mathcal{F})$ is a finitely generated $A$-module for every $p$, and it is $0$ for $p > r$.
2. There is $n_0$ such that $H^p(X, \mathcal{F}(n)) = 0$ for all $p > 0$ and all $n \geq n_0$.

Lean: not in Lean as stated.

**Corollary P4.2.8 (projective schemes over a field).** Let $X$ be projective over a field $k$ and $\mathcal{F}$ coherent on $X$. Then every $H^p(X, \mathcal{F})$ is a finite-dimensional $k$-vector space. Write $h^p(X, \mathcal{F}) = \dim_k H^p(X, \mathcal{F})$.

Lean: not in Lean as stated.

**Corollary P4.2.9 (large twists make sections exact).** Let $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ be an exact sequence of coherent sheaves on $X$. There is $n_0$ such that
$$0 \to \Gamma(X, \mathcal{F}'(n)) \to \Gamma(X, \mathcal{F}(n)) \to \Gamma(X, \mathcal{F}''(n)) \to 0$$
is exact for every $n \geq n_0$.

Lean: not in Lean as stated.

The second main result characterizes ampleness, Definition P3.6.22, by cohomology. Unlike the definition, the criterion is stable under the operations of Corollary P4.2.11, and it is the form of ampleness that the vanishing theorems of the later volumes refine.

**Theorem P4.2.10 (Serre's cohomological criterion for ampleness).** Let $A$ be a Noetherian ring, $X$ a proper scheme over $A$ and $\mathcal{L}$ an invertible sheaf on $X$. The following are equivalent:

1. $\mathcal{L}$ is ample.
2. For every coherent sheaf $\mathcal{F}$ on $X$ there is $n_0$ such that $H^p(X, \mathcal{F} \otimes \mathcal{L}^n) = 0$ for all $p > 0$ and all $n \geq n_0$.
3. For every coherent sheaf $\mathcal{F}$ on $X$ there is $n_0$ such that $H^1(X, \mathcal{F} \otimes \mathcal{L}^n) = 0$ for all $n \geq n_0$.

Lean: not in Lean as stated.

**Corollary P4.2.11 (closed subschemes and finite morphisms).** Let $A$ be Noetherian, $X$ proper over $A$ and $\mathcal{L}$ ample on $X$.

1. For every closed subscheme $Y \subseteq X$, $\mathcal{L}|_Y$ is ample on $Y$.
2. For every finite morphism $f \colon Y \to X$, $f^* \mathcal{L}$ is ample on $Y$.

Lean: not in Lean as stated.

### Proof in words

On projective space every coherent sheaf is a quotient of a finite sum of line bundles $\mathcal{O}(-q)$, by Serre's theorem P3.6.23, and the kernel is again coherent. For the line bundles, Theorem P4.2.1 gives both finiteness and vanishing after a twist. A descending induction on the degree $p$ then passes both properties from the sum of line bundles and the kernel to the sheaf, using that cohomology vanishes above degree $r$. A projective scheme reduces to projective space by pushing forward along the closed immersion.

For the criterion, an ample line bundle has a power that embeds $X$ as a closed subscheme of a projective space, and Serre's vanishing applies to each of the finitely many twists by the powers below it. Conversely, if $H^1$ vanishes after twisting, sections at a closed point $P$ lift from the fibre $\mathcal{F} \otimes k(P)$ to global sections, Nakayama's lemma makes them generate near $P$, and quasi-compactness turns finitely many such neighbourhoods into global generation everywhere.

### Examples

**Example P4.2.12 (the twist needed for a hypersurface).** Let $Y = V_+(f) \subseteq \mathbb{P}^r_k$ be a hypersurface of degree $d \geq 1$, $r \geq 2$. Twisting the sequence of Example P4.2.5 gives $0 \to \mathcal{O}(n-d) \to \mathcal{O}(n) \to \mathcal{O}_Y(n) \to 0$. For $n \geq -r$ the groups $H^p(\mathbb{P}^r, \mathcal{O}(n))$ vanish for all $p > 0$, and Theorem P4.2.1 gives $H^p(Y, \mathcal{O}_Y(n)) = 0$ for $p > 0$, $p \neq r - 1$, and $H^{r-1}(Y, \mathcal{O}_Y(n)) \cong H^r(\mathbb{P}^r, \mathcal{O}(n - d))$, which vanishes if and only if $n \geq d - r$. Since $d - r - 1 \geq -r$, the group $H^{r-1}(Y, \mathcal{O}_Y(d - r - 1)) \cong H^r(\mathbb{P}^r, \mathcal{O}(-r-1)) \cong k$ is nonzero, so the best $n_0$ in Theorem P4.2.7 for $\mathcal{O}_Y$ is $d - r$. For a plane curve of degree $d$ it is $d - 2$, and $H^1(Y, \mathcal{O}_Y(d - 3)) \cong k$: the twist by $d - 3$ is the canonical sheaf of the curve by Corollary P3.12.31 when $Y$ is smooth.

**Example P4.2.13 (the theorem needs properness).** Let $U = \mathbb{A}^2_k \setminus \{0\}$, an open subscheme of $\mathbb{P}^2_k$, and $\mathcal{O}_U(1)$ the restriction of $\mathcal{O}(1)$, which is trivial on $U \subseteq D_+(x_0)$. By Example P4.1.5, $H^1(U, \mathcal{O}_U(n)) \cong H^1(U, \mathcal{O}_U)$ is infinite-dimensional for every $n$. So both parts of Theorem P4.2.7 fail for a quasi-projective scheme that is not projective.

**Example P4.2.14 (a line bundle that is not ample).** On $X = \mathbb{P}^1_k$ take $\mathcal{L} = \mathcal{O}_X$ and $\mathcal{F} = \mathcal{O}(-2)$. Then $H^1(X, \mathcal{F} \otimes \mathcal{L}^n) = H^1(X, \mathcal{O}(-2)) \cong k$ for every $n$, so by Theorem P4.2.10 the trivial bundle is not ample. The same $\mathcal{F}$ shows that $\mathcal{O}(-1)$ is not ample, since $H^1(\mathcal{O}(-2-n)) \neq 0$ for $n \geq 0$. On the other hand $\mathcal{O}(1)$ satisfies condition 2 by Theorem P4.2.7, which recovers its ampleness from Theorem P3.6.23.

### Proof

*Theorem P4.2.7.* First reduce to $X = \mathbb{P}^r_A$. A closed immersion is finite, so $i_* \mathcal{F}$ is coherent by part 3 of Theorem P3.5.33. By the projection formula for the invertible sheaf $\mathcal{O}(1)$, which is immediate on a trivializing cover, $i_*(\mathcal{F}(n)) \cong (i_* \mathcal{F})(n)$. By Proposition P4.1.19, $H^p(X, \mathcal{F}(n)) \cong H^p(\mathbb{P}^r_A, (i_* \mathcal{F})(n))$ for all $p$ and $n$. So assume $X = \mathbb{P}^r_A$.

By Corollary P4.1.10, $H^p(X, \mathcal{G}) = 0$ for $p > r$ and every quasi-coherent $\mathcal{G}$. Prove by descending induction on $p$ the following statement $(\ast)_p$: for every coherent $\mathcal{F}$ on $X$, $H^p(X, \mathcal{F})$ is finitely generated, and if $p > 0$ there is $n_0$ with $H^p(X, \mathcal{F}(n)) = 0$ for $n \geq n_0$. For $p > r$ this holds. Assume $(\ast)_{p+1}$.

Let $\mathcal{F}$ be coherent. By Theorem P3.6.23 there is $q$ such that $\mathcal{F}(q)$ is generated by finitely many global sections $s_1, \dots, s_N$. They define a surjection $\mathcal{O}^N \to \mathcal{F}(q)$, and twisting by $-q$ a surjection $\mathcal{E} = \mathcal{O}(-q)^N \to \mathcal{F}$. Its kernel $\mathcal{R}$ is coherent by Proposition P3.5.22. Twisting by $\mathcal{O}(n)$ is exact, since $\mathcal{O}(n)$ is invertible, so for every $n$ there is an exact sequence
$$H^p(X, \mathcal{E}(n)) \to H^p(X, \mathcal{F}(n)) \to H^{p+1}(X, \mathcal{R}(n)).$$
For $n = 0$ the left term is $H^p(X, \mathcal{O}(-q))^N$, finitely generated by Theorem P4.2.1, and the right term is finitely generated by $(\ast)_{p+1}$. Since $A$ is Noetherian, the middle term is finitely generated. If $p > 0$, the left term $H^p(X, \mathcal{O}(n - q))^N$ vanishes for all $n$ when $p \neq r$, and for $n - q > -r-1$ when $p = r$, by Theorem P4.2.1. The right term vanishes for $n$ large by $(\ast)_{p+1}$ applied to $\mathcal{R}$. So the middle term vanishes for $n$ large. This proves $(\ast)_p$, and $(\ast)_0, \dots, (\ast)_r$ together give the theorem: for part 2 take the largest of the finitely many $n_0$ for $1 \leq p \leq r$. $\square$

*Corollary P4.2.8.* Apply Theorem P4.2.7 with $A = k$. $\square$

*Corollary P4.2.9.* The long exact sequence gives exactness of $0 \to \Gamma(\mathcal{F}'(n)) \to \Gamma(\mathcal{F}(n)) \to \Gamma(\mathcal{F}''(n)) \to H^1(X, \mathcal{F}'(n))$, and the last term vanishes for $n \geq n_0$ by part 2 of Theorem P4.2.7 applied to $\mathcal{F}'$. $\square$

*Theorem P4.2.10.* $(1) \Rightarrow (2)$. By Theorem P3.6.25 there is $m \geq 1$ with $\mathcal{L}^m$ very ample over $A$, and since $X$ is proper the immersion $j \colon X \to \mathbb{P}^N_A$ with $j^* \mathcal{O}(1) \cong \mathcal{L}^m$ is closed by part 3 of Proposition P3.6.24. So $X$ is projective over $A$ with $\mathcal{O}_X(1) = \mathcal{L}^m$. Let $\mathcal{F}$ be coherent. Apply part 2 of Theorem P4.2.7 to each of the coherent sheaves $\mathcal{F} \otimes \mathcal{L}^s$, $0 \leq s < m$, and let $n_1$ be the largest of the resulting bounds. Every $n \geq m n_1$ is $n = m t + s$ with $0 \leq s < m$ and $t \geq n_1$, and then $H^p(X, \mathcal{F} \otimes \mathcal{L}^n) = H^p(X, (\mathcal{F} \otimes \mathcal{L}^s)(t)) = 0$ for $p > 0$.

$(2) \Rightarrow (3)$ is clear.

$(3) \Rightarrow (1)$. Let $\mathcal{F}$ be coherent and $P \in X$ a closed point, with ideal sheaf $\mathcal{I}_P$ and residue field $k(P)$. The sequence $0 \to \mathcal{I}_P \mathcal{F} \to \mathcal{F} \to \mathcal{F}/\mathcal{I}_P \mathcal{F} \to 0$ is an exact sequence of coherent sheaves, and the quotient is the skyscraper sheaf at $P$ with value $\mathcal{F}_P \otimes k(P)$. Tensor with $\mathcal{L}^n$, which is exact. By (3) applied to $\mathcal{I}_P \mathcal{F}$ there is $n_0$ with $H^1(X, \mathcal{I}_P \mathcal{F} \otimes \mathcal{L}^n) = 0$ for $n \geq n_0$, so
$$\Gamma(X, \mathcal{F} \otimes \mathcal{L}^n) \to (\mathcal{F} \otimes \mathcal{L}^n)_P \otimes k(P)$$
is surjective for $n \geq n_0$. By Nakayama's lemma over the local ring $\mathcal{O}_{X,P}$, the stalk $(\mathcal{F} \otimes \mathcal{L}^n)_P$ is generated by global sections. Since $\mathcal{F} \otimes \mathcal{L}^n$ is coherent, finitely many of these global sections generate it on an open neighbourhood of $P$: the cokernel of the map from $\mathcal{O}_X^M$ they define is coherent with stalk $0$ at $P$, so its support is a closed set not containing $P$.

The neighbourhood depends on $n$, so a uniform one is needed. Apply the same argument to $\mathcal{O}_X$: there is $n_1 \geq 1$ and an open $V \ni P$ on which $\mathcal{L}^{n_1}$ is generated by global sections. Apply it to the coherent sheaves $\mathcal{F} \otimes \mathcal{L}^{s}$, $n_0 \leq s < n_0 + n_1$: there are open sets $U_s \ni P$ on which $\mathcal{F} \otimes \mathcal{L}^{s}$ is generated by global sections. On $W_P = V \cap \bigcap_s U_s$, every $\mathcal{F} \otimes \mathcal{L}^n$ with $n \geq n_0$ is generated by global sections: write $n = s + t n_1$ with $n_0 \leq s < n_0 + n_1$ and $t \geq 0$, and take the products of generating sections of $\mathcal{F} \otimes \mathcal{L}^s$ and of $t$ factors of generating sections of $\mathcal{L}^{n_1}$.

The open sets $W_P$ cover all closed points of $X$. In a quasi-compact scheme every nonempty closed subset contains a closed point, so the complement of $\bigcup_P W_P$ is empty, and by quasi-compactness finitely many $W_{P_1}, \dots, W_{P_l}$ cover $X$. For $n$ at least the largest of the corresponding bounds, $\mathcal{F} \otimes \mathcal{L}^n$ is generated by global sections on each $W_{P_i}$, hence on $X$. Since $X$ is Noetherian, being of finite type over $A$, this is ampleness in the sense of part 2 of Definition P3.6.22. $\square$

*Corollary P4.2.11.* For part 2, $Y$ is proper over $A$ by Proposition P3.4.19, since finite morphisms are proper and proper morphisms compose. Let $\mathcal{G}$ be coherent on $Y$. Then $f_* \mathcal{G}$ is coherent by part 3 of Theorem P3.5.33, and the projection formula $f_*(\mathcal{G} \otimes f^* \mathcal{L}^n) \cong f_* \mathcal{G} \otimes \mathcal{L}^n$ holds, as one checks on a cover of $X$ trivializing $\mathcal{L}$. A finite morphism is affine and $X$ is separated, being proper over $A$, so by Proposition P4.1.19
$$H^p(Y, \mathcal{G} \otimes f^* \mathcal{L}^n) \cong H^p(X, f_* \mathcal{G} \otimes \mathcal{L}^n),$$
which vanishes for $p > 0$ and $n$ large by Theorem P4.2.10 applied on $X$. By Theorem P4.2.10 on $Y$, $f^* \mathcal{L}$ is ample. Part 1 is the case of the closed immersion $Y \to X$, which is finite. $\square$

### Exercises

1. (A) Show that the smallest $n_0$ in part 2 of Theorem P4.2.7 for $\mathcal{F} = \mathcal{O}(q)$ on $\mathbb{P}^r_A$, $A \neq 0$, is $-q - r$.
2. (A) Let $Z \subseteq \mathbb{P}^r_k$ be a finite set of closed points with the reduced structure. Show that $H^p(Z, \mathcal{F}) = 0$ for every quasi-coherent $\mathcal{F}$ on $Z$ and every $p > 0$, and deduce from Corollary P4.2.9 that for $n$ large every function on $Z$ is the restriction of a form of degree $n$, in the sense that $H^0(\mathbb{P}^r, \mathcal{O}(n)) \to H^0(Z, \mathcal{O}_Z(n))$ is surjective.
3. (B) Let $A$ be Noetherian and $\mathcal{F}$ coherent on $X = \mathbb{P}^r_A$. Show that the graded $S$-module $\bigoplus_{n \geq 0} \Gamma(X, \mathcal{F}(n))$ is finitely generated. Use the surjection $\mathcal{E} \to \mathcal{F}$ of the proof of Theorem P4.2.7 and the vanishing of $H^1$ of the twists of its kernel.
4. (B) Let $X$ be proper over a Noetherian ring $A$ and $\mathcal{L}, \mathcal{M}$ invertible sheaves with $\mathcal{L}$ ample. Show that $\mathcal{L} \otimes \mathcal{M}$ is ample if $\mathcal{M}$ is generated by global sections, and deduce that $\mathcal{L}^n \otimes \mathcal{M}$ is ample for $n$ large.
5. (C) Let $X$ be proper over a Noetherian ring $A$, $\mathcal{N} \subseteq \mathcal{O}_X$ its nilradical and $\mathcal{L}$ invertible. Show that $\mathcal{L}$ is ample if and only if $\mathcal{L}|_{X_{\mathrm{red}}}$ is ample. Filter a coherent $\mathcal{F}$ by the subsheaves $\mathcal{N}^j \mathcal{F}$, which stop at $0$ because $\mathcal{N}^m = 0$ for some $m$, note that the quotients are $\mathcal{O}_{X_{\mathrm{red}}}$-modules, and use condition 2 of Theorem P4.2.10 with Proposition P4.1.19.
6. (C) Let $X$ be proper over a Noetherian ring $A$, and let $X_1, X_2 \subseteq X$ be closed subschemes with ideals $\mathcal{I}_1, \mathcal{I}_2$ such that $\mathcal{I}_1 \cap \mathcal{I}_2 = 0$. Show that $\mathcal{L}$ is ample on $X$ if and only if each $\mathcal{L}|_{X_i}$ is ample. For a coherent $\mathcal{F}$ on $X$, show that $\mathcal{I}_1 \mathcal{F}$ is an $\mathcal{O}_{X_2}$-module, since $\mathcal{I}_2 \mathcal{I}_1 \subseteq \mathcal{I}_1 \cap \mathcal{I}_2 = 0$, and that $\mathcal{F}/\mathcal{I}_1 \mathcal{F}$ is an $\mathcal{O}_{X_1}$-module, and use condition 2 of Theorem P4.2.10.

### Lean

Mathlib has the $\operatorname{Proj}$ construction, `AlgebraicGeometry.Proj`, and proper morphisms, `AlgebraicGeometry.IsProper`. Serre's finiteness and vanishing theorems and the cohomological criterion for ampleness are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

Theorem P4.2.7 is in Serre's *Faisceaux algébriques cohérents* (Ser55) for projective varieties over an algebraically closed field, and in Hartshorne as Theorem III.5.2. The criterion of Theorem P4.2.10 is Hartshorne's Proposition III.5.3, with the observation that only $H^1$ is needed, which is how the proof is written there. Grothendieck extended the finiteness to the higher direct images of coherent sheaves under proper morphisms, the form used in the later chapters of this volume. The literature state is theorem. In the minimal model program Serre vanishing is used in two ways: as a black box that makes any sufficiently positive twist acyclic, and as the model for the Kodaira and Kawamata-Viehweg vanishing theorems, which give the same conclusion for the adjoint twists $\omega_X \otimes \mathcal{L}$ by an ample or nef and big $\mathcal{L}$ without the word sufficiently. The criterion of Theorem P4.2.10 is how ampleness is checked on the reducible and nonreduced schemes that occur as fibres and boundaries.
