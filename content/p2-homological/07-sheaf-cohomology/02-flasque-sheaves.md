---
title: Flasque sheaves
nodes: []
sources: [Har77, God58, Gro57, Stacks]
reads_with: [Har77:ch3, God58:ch2]
requires: [P2.3, P2.5, P2.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Flasque sheaves

### Statement

Injective sheaves are hard to write down. This section introduces a larger class of sheaves that is easy to recognize and still has no higher cohomology. Resolutions by such sheaves compute cohomology, by Theorem P2.3.25.

**Definition P2.7.9 (flasque sheaf).** A sheaf $\mathcal{F}$ on a space $X$ is *flasque* if for every inclusion of open sets $V \subseteq U$ the restriction map $\mathcal{F}(U) \to \mathcal{F}(V)$ is surjective. Equivalently, every section over an open set extends to a global section.

Lean: Mathlib `TopCat.Presheaf.IsFlasque` and `TopCat.Sheaf.IsFlasque`.

**Lemma P2.7.10 (exact sequences with a flasque kernel).** Let $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ be an exact sequence in $\mathsf{Ab}(X)$ with $\mathcal{F}'$ flasque.

1. For every open $U$, the map $\mathcal{F}(U) \to \mathcal{F}''(U)$ is surjective.
2. If $\mathcal{F}$ is also flasque, then $\mathcal{F}''$ is flasque.

Lean: Mathlib `TopCat.Sheaf.IsFlasque.epi_of_shortExact` for part 1 and `TopCat.Sheaf.IsFlasque.of_shortExact_of_isFlasque₁₂` for part 2.

**Theorem P2.7.11 (flasque sheaves and cohomology).** Let $(X, \mathcal{O}_X)$ be a ringed space and $f: X \to Y$ a morphism of ringed spaces.

1. Every injective $\mathcal{O}_X$-module is flasque. Every injective object of $\mathsf{Ab}(X)$ is flasque.
2. If $\mathcal{F}$ is flasque, then $H^i(X, \mathcal{F}) = 0$ for all $i > 0$. So a resolution of a sheaf by flasque sheaves computes its cohomology.
3. If $\mathcal{F}$ is flasque, then $f_* \mathcal{F}$ is flasque and $R^i f_* \mathcal{F} = 0$ for all $i > 0$.
4. For an $\mathcal{O}_X$-module $\mathcal{F}$, the derived functors of $\Gamma(X, -)$ and of $f_*$ computed in $\mathsf{Mod}(\mathcal{O}_X)$ agree, as abelian groups and as sheaves of abelian groups, with those computed in $\mathsf{Ab}(X)$. The groups $H^i(X, \mathcal{F})$ are $\Gamma(X, \mathcal{O}_X)$-modules, and the sheaves $R^i f_* \mathcal{F}$ are $\mathcal{O}_Y$-modules.

Lean: Mathlib `TopCat.Sheaf.IsFlasque.pushforward_isFlasque` for the first claim of part 3; the other parts are not in Lean as stated.

**Proposition P2.7.12 (the Godement resolution).** For a sheaf $\mathcal{F}$ on $X$, let $\mathcal{C}^0(\mathcal{F})$ be the sheaf with
$$\mathcal{C}^0(\mathcal{F})(U) = \prod_{x \in U} \mathcal{F}_x,$$
the families of germs with no continuity condition, so that $\mathcal{C}^0(\mathcal{F}) = \prod_{x \in X} x_* \mathcal{F}_x$. Then $\mathcal{C}^0(\mathcal{F})$ is flasque, the map $\mathcal{F} \to \mathcal{C}^0(\mathcal{F})$ that sends a section to its germs is injective, and $\mathcal{F} \mapsto \mathcal{C}^0(\mathcal{F})$ is an exact functor. Put $\mathcal{C}^1(\mathcal{F}) = \mathcal{C}^0(\mathcal{C}^0(\mathcal{F})/\mathcal{F})$ and continue in the same way. This gives a resolution $0 \to \mathcal{F} \to \mathcal{C}^0(\mathcal{F}) \to \mathcal{C}^1(\mathcal{F}) \to \cdots$ by flasque sheaves, functorial and exact in $\mathcal{F}$, with
$$H^i(X, \mathcal{F}) \cong H^i(\Gamma(X, \mathcal{C}^\bullet(\mathcal{F}))).$$
If $\mathcal{F}$ is an $\mathcal{O}_X$-module, each $\mathcal{C}^n(\mathcal{F})$ is an $\mathcal{O}_X$-module.

Lean: Mathlib proves that skyscraper sheaves are flasque, `isFlasque_skyscraperSheaf_of_hasZeroObject`; the Godement resolution is not in Lean as stated.

**Theorem P2.7.13 (Grothendieck vanishing).** Let $X$ be a Noetherian topological space of dimension $n$. Then $H^i(X, \mathcal{F}) = 0$ for all $i > n$ and all sheaves of abelian groups $\mathcal{F}$ on $X$.

Lean: not in Lean as stated.

### Proof in words

A section of the quotient lifts locally. Zorn's lemma gives a maximal partial lift. If it is not defined everywhere, a local lift near a missing point differs from it by a section of the kernel on the overlap, and the flasque kernel lets the two be matched and glued. For the theorem, a section over an open set $U$ is a map from the extension by zero of $\mathcal{O}_U$, and these extensions by zero are nested. So injectivity of $\mathcal{I}$ makes every restriction map surjective. A flasque sheaf embeds in an injective one with a flasque quotient, and the lemma makes $\Gamma$ exact on that sequence. Dimension shifting then kills all higher cohomology. Since injective modules are flasque, an injective resolution in $\mathsf{Mod}(\mathcal{O}_X)$ is an acyclic resolution in $\mathsf{Ab}(X)$, and both theories give the same groups.

### Examples

**Example P2.7.14 (constant sheaves on irreducible spaces).** Let $X$ be an irreducible space and $A$ an abelian group. Every nonempty open subset of $X$ is irreducible, hence connected, so the constant sheaf $\underline{A}$ has $\underline{A}(U) = A$ for $U \neq \emptyset$, with identity restriction maps. So $\underline{A}$ is flasque, and $H^i(X, \underline{A}) = 0$ for $i > 0$. For a smooth projective complex curve $X$ of genus $g$, the Zariski topology gives $H^1(X, \mathbb{Z}) = 0$, while the classical topology gives $\mathbb{Z}^{2g}$. Constant coefficients carry topological information only in the classical topology. The Zariski topology is the right one for coherent sheaves, and comparison results such as GAGA link the two.

**Example P2.7.15 (a structure sheaf that is not flasque).** Let $X = \mathbb{A}^1$ over a field $k$. The function $1/t$ on $D(t) = \mathbb{A}^1 \setminus \{0\}$ is not the restriction of a polynomial, so $\mathcal{O}_X$ is not flasque. Still $H^1(\mathbb{A}^1, \mathcal{O}) = 0$, because a quasi-coherent sheaf on an affine scheme has no higher cohomology (P4 Ch. 1). The class of $\Gamma$-acyclic sheaves is strictly larger than the class of flasque sheaves.

**Example P2.7.16 (the resolution by rational functions on a curve).** Let $X$ be a smooth irreducible curve over an algebraically closed field $k$, with function field $K = k(X)$. Write $\underline{K}$ for the constant sheaf with value $K$. It is flasque by Example P2.7.14, and it contains $\mathcal{O}_X$. A section of $\underline{K}/\mathcal{O}_X$ over $U$ is locally a rational function modulo regular ones, so it has finitely many poles on each open set of a finite cover, hence finitely many poles on $U$. So the quotient is the sheaf $\bigoplus_{x} x_* (K/\mathcal{O}_{X,x})$, the sum over closed points, with sections over $U$ the finite families of principal parts at points of $U$. The restriction maps forget the principal parts outside $V$, so the quotient is flasque. The exact sequence
$$0 \to \mathcal{O}_X \to \underline{K} \to \bigoplus_{x} x_* (K/\mathcal{O}_{X,x}) \to 0$$
is a flasque resolution. By part 2 of the theorem,
$$H^0(X, \mathcal{O}_X) = \bigcap_x \mathcal{O}_{X,x}, \qquad H^1(X, \mathcal{O}_X) = \operatorname{coker}\Big(K \to \bigoplus_{x} K/\mathcal{O}_{X,x}\Big), \qquad H^i(X, \mathcal{O}_X) = 0 \text{ for } i \geq 2.$$
So $H^1(X, \mathcal{O}_X)$ is the group of principal parts that are not the principal parts of one rational function. This is the description by *répartitions* in Serre's proof of the Riemann-Roch theorem for curves. Exercise 5 shows that $H^1(\mathbb{P}^1, \mathcal{O}) = 0$ in this way, by partial fractions. The vanishing for $i \geq 2$ is also a case of Grothendieck vanishing, since $\dim X = 1$.

**Example P2.7.17 (flasque but not injective).** On a point, every sheaf is flasque, and the flasque sheaf $\mathbb{Z}$ is not an injective abelian group. So the class of flasque sheaves is strictly larger than the class of injective sheaves. It is still closed under the operations of Lemma P2.7.10 and under $f_*$, which the injective sheaves are not in general.

### Proof

*Lemma P2.7.10.* Part 1. Let $s \in \mathcal{F}''(U)$. Consider the set of pairs $(V, t)$ with $V \subseteq U$ open and $t \in \mathcal{F}(V)$ mapping to $s|_V$. Order the pairs by $(V, t) \leq (V', t')$ if $V \subseteq V'$ and $t'|_V = t$. The set is nonempty, since it contains $(\emptyset, 0)$. A chain $(V_\alpha, t_\alpha)$ has an upper bound: the sections $t_\alpha$ agree on the overlaps, so they glue to a section $t$ over $\bigcup V_\alpha$, and $t$ maps to $s$ on that union by the locality axiom of $\mathcal{F}''$. By Zorn's lemma there is a maximal pair $(V, t)$. Suppose $V \neq U$ and pick $x \in U \setminus V$. The map $\mathcal{F}_x \to \mathcal{F}''_x$ is surjective, so there is an open $W$ with $x \in W \subseteq U$ and $t' \in \mathcal{F}(W)$ mapping to $s|_W$. On $V \cap W$ the section $t - t'$ maps to $0$ in $\mathcal{F}''$, so it lies in $\mathcal{F}'(V \cap W)$. Since $\mathcal{F}'$ is flasque, it extends to $r \in \mathcal{F}'(W)$. Then $t' + r$ maps to $s|_W$ and agrees with $t$ on $V \cap W$. So $t$ and $t' + r$ glue to a section over $V \cup W$ that maps to $s|_{V \cup W}$. This contradicts maximality. So $V = U$, and $t$ is a preimage of $s$.

Part 2. Let $V \subseteq U$ and $s'' \in \mathcal{F}''(V)$. The sequence restricted to $V$ is exact with a flasque kernel, so part 1 gives $t \in \mathcal{F}(V)$ mapping to $s''$. Since $\mathcal{F}$ is flasque, $t$ extends to $\tilde{t} \in \mathcal{F}(U)$. The image of $\tilde{t}$ in $\mathcal{F}''(U)$ restricts to $s''$. $\square$

*Theorem P2.7.11.* Part 1. Let $U \subseteq X$ be open with inclusion $j_U$, and let $\mathcal{O}_U = j_{U!}(\mathcal{O}_X|_U)$ be the extension by zero. By the adjunction in the proof of part 3 of Theorem P2.7.3 and Proposition P2.6.4,
$$\operatorname{Hom}_{\mathcal{O}_X}(\mathcal{O}_U, \mathcal{I}) \cong \operatorname{Hom}_{\mathcal{O}_X|_U}(\mathcal{O}_X|_U, \mathcal{I}|_U) \cong \mathcal{I}(U),$$
where a map corresponds to the image of the section $1$ over $U$. For $V \subseteq U$ open, there is a map $\mathcal{O}_V \to \mathcal{O}_U$ that is the identity on sections over open subsets of $V$. On stalks it is the identity $\mathcal{O}_{X,x} \to \mathcal{O}_{X,x}$ for $x \in V$, and the map $0 \to (\mathcal{O}_U)_x$ for $x \notin V$, by Proposition P2.5.32. So it is injective. If $\mathcal{I}$ is injective, then $\operatorname{Hom}(\mathcal{O}_U, \mathcal{I}) \to \operatorname{Hom}(\mathcal{O}_V, \mathcal{I})$ is surjective. Under the isomorphisms above this map is the restriction $\mathcal{I}(U) \to \mathcal{I}(V)$, because both send a map to the image of $1$ over $V$. So $\mathcal{I}$ is flasque. For $\mathsf{Ab}(X)$, apply the same argument to the ringed space $(X, \underline{\mathbb{Z}})$, whose modules are the sheaves of abelian groups.

Part 2. Work in $\mathsf{Ab}(X)$. Let $\mathcal{F}$ be flasque. Embed $\mathcal{F}$ in an injective sheaf $\mathcal{I}$ and put $\mathcal{Q} = \mathcal{I}/\mathcal{F}$. By part 1, $\mathcal{I}$ is flasque, so $\mathcal{Q}$ is flasque by part 2 of the lemma. The long exact sequence and $H^i(X, \mathcal{I}) = 0$ for $i > 0$ give
$$H^1(X, \mathcal{F}) \cong \operatorname{coker}(\Gamma(X, \mathcal{I}) \to \Gamma(X, \mathcal{Q})), \qquad H^i(X, \mathcal{F}) \cong H^{i-1}(X, \mathcal{Q}) \ \ (i \geq 2).$$
The cokernel is $0$ by part 1 of the lemma. So $H^1(X, \mathcal{F}) = 0$ for every flasque sheaf $\mathcal{F}$ on every space. Since $\mathcal{Q}$ is flasque, induction on $i$ gives $H^i(X, \mathcal{F}) = H^{i-1}(X, \mathcal{Q}) = 0$. Flasque sheaves are therefore $\Gamma$-acyclic, and Theorem P2.3.25 shows that flasque resolutions compute cohomology.

Part 3. $(f_* \mathcal{F})(U) = \mathcal{F}(f^{-1}(U)) \to \mathcal{F}(f^{-1}(V)) = (f_* \mathcal{F})(V)$ is surjective, since $f^{-1}(V) \subseteq f^{-1}(U)$. By part 4 of Theorem P2.7.3, $R^i f_* \mathcal{F}$ is the sheafification of $V \mapsto H^i(f^{-1}(V), \mathcal{F})$. The restriction of a flasque sheaf to an open set is flasque, so this presheaf is $0$ for $i > 0$ by part 2.

Part 4. Let $\mathcal{F} \to \mathcal{I}^\bullet$ be an injective resolution in $\mathsf{Mod}(\mathcal{O}_X)$. The forgetful functor to $\mathsf{Ab}(X)$ is exact (part 2 of Theorem P2.6.3), so $\mathcal{I}^\bullet$ is a resolution of $\mathcal{F}$ in $\mathsf{Ab}(X)$. Each $\mathcal{I}^n$ is flasque by part 1, so it is acyclic for $\Gamma(X, -)$ by part 2 and for $f_*$ by part 3, in $\mathsf{Ab}(X)$. By Theorem P2.3.25, the groups $H^i(\Gamma(X, \mathcal{I}^\bullet))$, which are the derived functors in $\mathsf{Mod}(\mathcal{O}_X)$, are also the derived functors in $\mathsf{Ab}(X)$. The same argument applies to $f_*$. The groups $\Gamma(X, \mathcal{I}^n)$ are $\Gamma(X, \mathcal{O}_X)$-modules and the sheaves $f_* \mathcal{I}^n$ are $\mathcal{O}_Y$-modules, and the differentials are linear, so the cohomology carries these structures. $\square$

*Proposition P2.7.12.* The restriction map $\prod_{x \in U} \mathcal{F}_x \to \prod_{x \in V} \mathcal{F}_x$ is the projection onto a subset of the factors, so it is surjective. The presheaf $\mathcal{C}^0(\mathcal{F})$ is a sheaf, since a family of germs over $U$ is given by its restrictions to the sets of a cover. The map $\mathcal{F} \to \mathcal{C}^0(\mathcal{F})$ is injective by Proposition P2.5.4. If $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ is exact, then the stalks form exact sequences, and a product of exact sequences of abelian groups is exact. So $0 \to \mathcal{C}^0(\mathcal{F}')(U) \to \mathcal{C}^0(\mathcal{F})(U) \to \mathcal{C}^0(\mathcal{F}'')(U) \to 0$ is exact for every $U$, and the sequence of sheaves is exact. Put $\mathcal{Z}^1 = \mathcal{C}^0(\mathcal{F})/\mathcal{F}$ and $\mathcal{C}^1(\mathcal{F}) = \mathcal{C}^0(\mathcal{Z}^1)$, and in general $\mathcal{Z}^{n+1} = \mathcal{C}^n(\mathcal{F})/\mathcal{Z}^n$, where $\mathcal{Z}^n \to \mathcal{C}^n(\mathcal{F})$ is the germ map. Splicing the sequences $0 \to \mathcal{Z}^n \to \mathcal{C}^n(\mathcal{F}) \to \mathcal{Z}^{n+1} \to 0$ gives the resolution. Each $\mathcal{Z}^n$ is an exact functor of $\mathcal{F}$, by induction and the snake lemma, so the resolution is exact in $\mathcal{F}$. The formula for cohomology follows from part 2 of the theorem. For an $\mathcal{O}_X$-module, each $\mathcal{F}_x$ is an $\mathcal{O}_{X,x}$-module and $\prod_{x \in U} \mathcal{F}_x$ is an $\mathcal{O}_X(U)$-module through the germs of functions. $\square$

*Theorem P2.7.13.* The proof reduces to an irreducible space by induction on the number of irreducible components and on the dimension, using the exact sequence $0 \to j_! \mathcal{F}|_U \to \mathcal{F} \to i_* \mathcal{F}|_Z \to 0$ of Proposition P2.5.32 and the fact that on a Noetherian space cohomology commutes with filtered colimits. It then writes a sheaf as a filtered colimit of sheaves generated by finitely many sections, and treats the sheaves $j_! \underline{\mathbb{Z}}_U$ and their quotients by a further induction on dimension. See Hartshorne, Chapter III, Section 2, and Grothendieck's Tohoku paper. $\square$

### Exercises

1. (A) Show that the restriction of a flasque sheaf to an open set is flasque, and that a product of flasque sheaves is flasque.
2. (A) Show that the constant sheaf $\underline{\mathbb{Z}}$ on $\mathbb{R}$ is not flasque, using a section over the union of two disjoint open intervals.
3. (A) Let $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ be exact with $\mathcal{F}'$ and $\mathcal{F}''$ flasque. Show that $\mathcal{F}$ is flasque.
4. (B) Let $X$ be a Noetherian space. Show that every open set of $X$ is quasi-compact, that $\Gamma(U, \bigoplus_\alpha \mathcal{F}_\alpha) = \bigoplus_\alpha \Gamma(U, \mathcal{F}_\alpha)$, and that a direct sum of flasque sheaves on $X$ is flasque.
5. (B) In Example P2.7.16 take $X = \mathbb{P}^1$ and $K = k(t)$. Use partial fractions to show that every finite family of principal parts at closed points is the family of principal parts of one rational function, and deduce $H^1(\mathbb{P}^1, \mathcal{O}) = 0$. Then write $\mathcal{O}(-2)$ as the sheaf of functions with a zero of order at least $2$ at $\infty$, replace $K/\mathcal{O}_{X,\infty}$ by $K/\mathfrak{m}_\infty^2$ in the resolution, and show $H^1(\mathbb{P}^1, \mathcal{O}(-2)) \cong k$.
6. (B) Show that $\Gamma(X, \mathcal{C}^0(\mathcal{F})) = \prod_{x \in X} \mathcal{F}_x$. Compute the first two terms of the Godement resolution of $\underline{\mathbb{Z}}$ on the two point space $\{a, b\}$ with open sets $\emptyset$, $\{a\}$ and $X$, and check that its cohomology is $\mathbb{Z}$ in degree $0$ and $0$ otherwise.
7. (C) Let $X$ be a Noetherian space. Use Exercise 4 and the fact that a filtered colimit of injective sheaves on $X$ is flasque to show that $H^i(X, \bigoplus_\alpha \mathcal{F}_\alpha) = \bigoplus_\alpha H^i(X, \mathcal{F}_\alpha)$ for all $i$.

### Lean

Mathlib has flasque presheaves and sheaves, `TopCat.Presheaf.IsFlasque` and `TopCat.Sheaf.IsFlasque`, with the instances `TopCat.Presheaf.IsFlasque.pushforward_isFlasque` and `TopCat.Sheaf.IsFlasque.pushforward_isFlasque`. The surjectivity of sections in a short exact sequence with a flasque kernel is `TopCat.Sheaf.IsFlasque.epi_of_shortExact`, proved with Zorn's lemma as here, and the flasque quotient is `TopCat.Sheaf.IsFlasque.of_shortExact_of_isFlasque₁₂`. Skyscraper sheaves are flasque by `isFlasque_skyscraperSheaf_of_hasZeroObject`. The acyclicity of flasque sheaves, the comparison between modules and abelian sheaves, the Godement resolution and Grothendieck vanishing are not in Lean as stated.

### Notes and history

Flasque sheaves, *faisceaux flasques*, are due to Godement, whose book of 1958 builds sheaf cohomology from the canonical resolution of Proposition P2.7.12. Grothendieck's Tohoku paper proved the vanishing theorem for Noetherian spaces. Example P2.7.16 is the sheaf form of the répartitions that Weil and Serre used for curves. The minimal model program meets flasque sheaves mostly through part 4 of the theorem, which lets every cohomology group of a coherent sheaf be computed in abelian groups, and through Grothendieck vanishing, which bounds the degrees in every Leray spectral sequence.
