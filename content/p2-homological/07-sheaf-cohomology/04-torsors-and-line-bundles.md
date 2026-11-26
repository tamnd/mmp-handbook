---
title: Torsors, line bundles and lifting sections
nodes: []
sources: [Har77, Ser55, Ser56, Stacks]
reads_with: [Har77:ch3]
requires: [P2.5, P2.6]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Torsors, line bundles and lifting sections

### Statement

The group $H^1$ has a geometric meaning. It classifies objects that are locally trivial but may be globally twisted. For the sheaf $\mathcal{O}_X^\times$ these objects are the line bundles. This section proves the classification and uses it to compute $\operatorname{Pic}(\mathbb{P}^1)$, as promised in Example P2.6.31.

**Definition P2.7.26 (torsor).** Let $\mathcal{G}$ be a sheaf of groups on $X$. A *$\mathcal{G}$-torsor* is a sheaf of sets $\mathcal{P}$ with a right action $\mathcal{P} \times \mathcal{G} \to \mathcal{P}$ such that:

1. for every open $U$ with $\mathcal{P}(U) \neq \emptyset$, the group $\mathcal{G}(U)$ acts simply transitively on $\mathcal{P}(U)$;
2. there is an open cover $(U_i)$ of $X$ with $\mathcal{P}(U_i) \neq \emptyset$ for all $i$.

A morphism of torsors is a morphism of sheaves that commutes with the action. The torsor $\mathcal{G}$, with $\mathcal{G}$ acting by right multiplication, is the *trivial torsor*.

Lean: not in Lean as stated.

**Theorem P2.7.27 (torsors and $H^1$).** Let $\mathcal{G}$ be a sheaf of groups and $\mathcal{U} = (U_i)$ an open cover.

1. Isomorphism classes of $\mathcal{G}$-torsors $\mathcal{P}$ with $\mathcal{P}(U_i) \neq \emptyset$ for all $i$ are in bijection with $\check{H}^1(\mathcal{U}, \mathcal{G})$, the set of cocycles $(g_{ij})$, $g_{ij} \in \mathcal{G}(U_{ij})$, with $g_{ij} g_{jk} = g_{ik}$ on $U_{ijk}$, modulo the relation $g'_{ij} = h_i^{-1} g_{ij} h_j$ for $h_i \in \mathcal{G}(U_i)$. The trivial torsor corresponds to the class of $g_{ij} = 1$.
2. If $\mathcal{G}$ is abelian, the isomorphism classes of all $\mathcal{G}$-torsors are in bijection with $H^1(X, \mathcal{G})$.
3. A torsor is trivial if and only if it has a global section.

Lean: Mathlib `CategoryTheory.PresheafOfGroups.H1`, the quotient of `CategoryTheory.PresheafOfGroups.OneCocycle` by the cohomology relation, is the set of part 1 for a family of objects in a category; the bijection with torsors is not in Lean as stated.

**Theorem P2.7.28 (the Picard group as $H^1$).** Let $(X, \mathcal{O}_X)$ be a ringed space. The map that sends an invertible sheaf $\mathcal{L}$ to the class of its transition functions is a group isomorphism
$$\operatorname{Pic}(X) \cong H^1(X, \mathcal{O}_X^\times).$$
Under it, the line bundles that are trivial on the sets of a cover $\mathcal{U}$ form the subgroup $\check{H}^1(\mathcal{U}, \mathcal{O}_X^\times)$. More generally, isomorphism classes of locally free sheaves of rank $r$ that are trivial on the sets of $\mathcal{U}$ are in bijection with $\check{H}^1(\mathcal{U}, \mathrm{GL}_r(\mathcal{O}_X))$.

Lean: Mathlib `CommRing.Pic` is the Picard group of a ring; the isomorphism with $H^1$ is not in Lean as stated.

**Proposition P2.7.29 (lifting sections).** Let $X$ be a variety, $S \subseteq X$ an effective Cartier divisor with inclusion $i$, and $\mathcal{L}$ an invertible sheaf. There is an exact sequence
$$0 \to H^0(X, \mathcal{L}(-S)) \to H^0(X, \mathcal{L}) \to H^0(S, \mathcal{L}|_S) \to H^1(X, \mathcal{L}(-S)) \to H^1(X, \mathcal{L}) \to \cdots,$$
where $\mathcal{L}(-S) = \mathcal{L} \otimes \mathcal{O}_X(-S)$. If $H^1(X, \mathcal{L}(-S)) = 0$, every section of $\mathcal{L}|_S$ lifts to a section of $\mathcal{L}$.

Lean: not in Lean as stated.

### Proof in words

Choose a section $s_i$ of the torsor on each $U_i$. On $U_{ij}$ two sections differ by a unique element of the group, and these elements form a cocycle. Another choice of sections changes the cocycle by a coboundary. Conversely, a cocycle glues copies of the trivial torsor. For an abelian group, Theorem P2.7.22 identifies $H^1$ with the colimit of the Čech groups over all covers. A line bundle is the same as a torsor under $\mathcal{O}_X^\times$, namely the sheaf of its local generators, and the cocycle is the family of transition functions of Proposition P2.6.28. Lifting sections is the long exact sequence of a restriction sequence.

### Examples

**Example P2.7.30 (the Picard group of $\mathbb{P}^1$).** Let $k$ be a field and keep the cover $U_0 = \operatorname{Spec} k[t]$, $U_1 = \operatorname{Spec} k[s]$ of Example P2.6.9. A line bundle on $U_0$ is the sheaf of an invertible $k[t]$-module (P3 Ch. 5), and an invertible module over a principal ideal domain is free. So every line bundle $\mathcal{L}$ on $\mathbb{P}^1$ is trivial on $U_0$ and on $U_1$, and by Theorem P2.7.28 its class lies in $\check{H}^1(\mathcal{U}, \mathcal{O}^\times)$. For a cover by two sets, a cochain is one unit on $U_{01}$, every cochain is a cocycle, and by Exercise 1 of Section 7.3, written multiplicatively,
$$\check{H}^1(\mathcal{U}, \mathcal{O}^\times) = \frac{k[t, t^{-1}]^\times}{k[t]^\times \cdot k[s]^\times} = \frac{\{ c t^n : c \in k^\times, n \in \mathbb{Z} \}}{k^\times} \cong \mathbb{Z}.$$
The class of $t^n$ is the transition function of $\mathcal{O}(n)$ (Example P2.6.31). So $\operatorname{Pic}(\mathbb{P}^1) = \{ \mathcal{O}(n) : n \in \mathbb{Z} \} \cong \mathbb{Z}$. The degree $n$ is read off from $h^0$ or $h^1$ by Example P2.7.23.

**Example P2.7.31 (the ideal sheaf of two points).** On $\mathbb{P}^1$ let $Z = \{0, \infty\}$, where $0$ is $t = 0$ in $U_0$ and $\infty$ is $s = 0$ in $U_1$. The ideal sheaf $\mathcal{I}_Z$ is $t k[t]$ on $U_0$ and $s k[s]$ on $U_1$. Trivialize it by $\varphi_0(f) = f/t$ on $U_0$ and $\varphi_1(g) = g/s$ on $U_1$. Then $\varphi_0 \varphi_1^{-1}(h) = h s/t = t^{-2} h$, so the transition function is $t^{-2}$, and $\mathcal{I}_Z \cong \mathcal{O}(-2)$. This proves the isomorphism used in Examples P2.5.25 and P2.7.7. In the same way the ideal sheaf $\mathfrak{m}_\infty$ of the point $\infty$ is $k[t]$ on $U_0$ and $s k[s]$ on $U_1$, with transition function $t^{-1}$, so $\mathfrak{m}_\infty \cong \mathcal{O}(-1)$. This agrees with the description of $\mathcal{O}(n)$ as $\mathcal{O}(n \cdot \infty)$ in Example P2.6.9.

**Example P2.7.32 (the exponential sequence and the first Chern class).** Let $X$ be a compact connected complex manifold. Theorem P2.7.28 holds for the holomorphic structure sheaf, so the long exact sequence of Example P2.7.6 becomes
$$0 \to H^1(X, \mathbb{Z}) \to H^1(X, \mathcal{O}_X) \to \operatorname{Pic}(X) \xrightarrow{c_1} H^2(X, \mathbb{Z}) \to H^2(X, \mathcal{O}_X).$$
The image of $c_1$ is the *Néron-Severi group* $\mathrm{NS}(X)$, and the kernel is $\operatorname{Pic}^0(X) = H^1(X, \mathcal{O}_X)/H^1(X, \mathbb{Z})$, the line bundles that are topologically trivial. For a smooth projective curve of genus $g$, $\operatorname{Pic}^0(X)$ is a complex torus of dimension $g$, the Jacobian. If $H^1(X, \mathcal{O}_X) = 0$, as for $\mathbb{P}^1$ by Example P2.7.23 and GAGA (Serre 1956), then $c_1$ is injective and $\operatorname{Pic}(X) = \mathrm{NS}(X)$. In the minimal model program the numerical classes of line bundles form the space $N^1(X)_{\mathbb{R}} = \mathrm{NS}(X) \otimes \mathbb{R}$ modulo numerical equivalence, in which the cone theorem and the ample cone live (Volume 7).

**Example P2.7.33 (sections of $\mathcal{O}(n)$ separate points).** On $\mathbb{P}^1$ let $S = p$ be a closed point with residue field $k$ and $\mathcal{L} = \mathcal{O}(n)$, so that $\mathcal{L}(-S) \cong \mathcal{O}(n - 1)$ by Exercise 3 for $p \neq \infty$ and by Example P2.7.31 for $p = \infty$. For $n \geq 0$, $H^1(\mathbb{P}^1, \mathcal{O}(n - 1)) = 0$ by Example P2.7.23. So by Proposition P2.7.29 every value $\mathcal{L}|_p \cong k$ is the value of a global section, and $\mathcal{O}(n)$ is generated by its global sections for $n \geq 0$. For $n = -1$ the group $H^1(\mathcal{O}(-2)) \cong k$ is not zero, and indeed $\mathcal{O}(-1)$ has no nonzero section. The base point free theorem (Volume 7) runs the same argument on a variety $X$ with a divisor $S$, where Kawamata-Viehweg vanishing (P7 Ch. 8) gives $H^1(X, \mathcal{O}_X(mD - S)) = 0$.

### Proof

*Theorem P2.7.27.* Part 1. Let $\mathcal{P}$ be a torsor and choose $s_i \in \mathcal{P}(U_i)$. On $U_{ij}$ both $s_i$ and $s_j$ are sections, so there is a unique $g_{ij} \in \mathcal{G}(U_{ij})$ with $s_j = s_i g_{ij}$. On $U_{ijk}$, $s_k = s_j g_{jk} = s_i g_{ij} g_{jk}$ and $s_k = s_i g_{ik}$, so $g_{ij} g_{jk} = g_{ik}$ by simple transitivity. Other sections $s'_i = s_i h_i$ give $s'_j = s'_i h_i^{-1} g_{ij} h_j$, so the class of the cocycle does not depend on the choice. An isomorphism of torsors carries the chosen sections to sections with the same cocycle, so isomorphic torsors have the same class. Conversely, given a cocycle $(g_{ij})$, glue the trivial torsors $\mathcal{G}|_{U_i}$ along the maps $\mathcal{G}|_{U_{ij}} \to \mathcal{G}|_{U_{ij}}$, $x \mapsto g_{ij} x$, which are compatible with the right action. The cocycle condition is the condition of Theorem P2.5.35, so this gives a sheaf $\mathcal{P}$ with a right action, isomorphic to $\mathcal{G}$ on each $U_i$, and the images of the sections $1$ have cocycle $(g_{ij})$. If two torsors have cohomologous cocycles, then after a change of sections they have the same cocycle, and the map $s_i x \mapsto s'_i x$ on each $U_i$ is well defined on overlaps and glues to an isomorphism. So the two constructions are inverse bijections.

Part 2. Every torsor is trivial on some cover, by condition 2. A refinement of covers gives a map of the sets in part 1 that is compatible with the bijections. So the isomorphism classes of torsors are $\varinjlim_{\mathcal{U}} \check{H}^1(\mathcal{U}, \mathcal{G})$, which is $H^1(X, \mathcal{G})$ by Theorem P2.7.22.

Part 3. If $s \in \mathcal{P}(X)$, the map $\mathcal{G} \to \mathcal{P}$, $g \mapsto s|_U g$ on $U$, is an isomorphism of torsors by simple transitivity. Conversely, the trivial torsor has the global section $1$. $\square$

*Theorem P2.7.28.* For an invertible sheaf $\mathcal{L}$, let $\mathcal{P}$ be the sheaf of local generators: $\mathcal{P}(U)$ is the set of $e \in \mathcal{L}(U)$ such that $\mathcal{O}_U \to \mathcal{L}|_U$, $a \mapsto a e$, is an isomorphism. The group $\mathcal{O}_X^\times$ acts by multiplication. If $e$ and $e'$ are generators over $U$, then $e' = u e$ for a unique unit $u$, so the action is simply transitive, and $\mathcal{P}(U_i) \neq \emptyset$ on any cover on which $\mathcal{L}$ is trivial. So $\mathcal{P}$ is an $\mathcal{O}_X^\times$-torsor. The cocycle of $\mathcal{P}$ for generators $e_i$, $e_j = e_i g_{ij}$, is the family of transition functions of Proposition P2.6.28 for the trivializations $\varphi_i(e_i) = 1$, up to the convention $g_{ij}$ versus $g_{ij}^{-1}$, which does not change the class. Proposition P2.6.28 says that line bundles trivial on $\mathcal{U}$ correspond to $\check{H}^1(\mathcal{U}, \mathcal{O}_X^\times)$, and Theorem P2.7.27 extends this to all line bundles and $H^1(X, \mathcal{O}_X^\times)$. For the group law, if $e_i$ and $f_i$ generate $\mathcal{L}$ and $\mathcal{M}$ on $U_i$, then $e_i \otimes f_i$ generates $\mathcal{L} \otimes \mathcal{M}$, and its transition functions are the products $g_{ij} g'_{ij}$. So the bijection is a homomorphism. The case of rank $r$ is the general form of Proposition P2.6.28, with the matrices $g_{ij}$ as a cocycle of the sheaf of groups $\mathrm{GL}_r(\mathcal{O}_X)$. $\square$

*Proposition P2.7.29.* The sequence $0 \to \mathcal{O}_X(-S) \to \mathcal{O}_X \to i_* \mathcal{O}_S \to 0$ is exact (Example P2.5.25). Tensoring with the locally free $\mathcal{L}$ keeps it exact, since locally it is a direct sum of copies of the sequence, and $\mathcal{L} \otimes i_* \mathcal{O}_S \cong i_* (\mathcal{L}|_S)$ by the projection formula (Theorem P2.6.30). Proposition P2.7.4 gives $H^n(X, i_* (\mathcal{L}|_S)) = H^n(S, \mathcal{L}|_S)$, and part 2 of Theorem P2.7.3 gives the long exact sequence. $\square$

### Exercises

1. (A) Show that the map $\operatorname{Pic}(X) \to H^1(X, \mathcal{O}_X^\times)$ sends $\mathcal{L}^\vee$ to the inverse of the class of $\mathcal{L}$.
2. (A) Let $A$ be a local ring. Show that $\operatorname{Pic}(\operatorname{Spec} A) = 0$ in two ways: from Nakayama's lemma, and from Theorem P2.7.28 and Exercise 6 of Section 7.1.
3. (B) Let $p_1, \ldots, p_d$ be distinct points of $\mathbb{A}^1 \subset \mathbb{P}^1$ and $D = p_1 + \cdots + p_d$. Compute the transition function of the ideal sheaf $\mathcal{O}(-D)$ for the standard cover, and show that $\mathcal{O}(-D) \cong \mathcal{O}(-d)$.
4. (B) Show that $\mathcal{O}(n)$ on $\mathbb{P}^1$ is generated by global sections if and only if $n \geq 0$.
5. (B) Twist the Euler sequence $0 \to \mathcal{O}(-1) \to \mathcal{O}^2 \to \mathcal{O}(1) \to 0$ on $\mathbb{P}^1$ by $\mathcal{O}(-1)$. Show that the connecting map $H^0(\mathbb{P}^1, \mathcal{O}) \to H^1(\mathbb{P}^1, \mathcal{O}(-2))$ is an isomorphism, and deduce that the twisted sequence does not split.
6. (B) Let $X$ be a ringed space and $0 \to \mathcal{O}_X \to \mathcal{E} \to \mathcal{O}_X \to 0$ an exact sequence of $\mathcal{O}_X$-modules. Show that the image of $1$ under the connecting map is a class in $H^1(X, \mathcal{O}_X)$ that vanishes if and only if the sequence splits, and that every class arises in this way.
7. (C) Let $X$ be a compact connected complex manifold with $H^1(X, \mathcal{O}_X) = 0$. Show that $c_1: \operatorname{Pic}(X) \to H^2(X, \mathbb{Z})$ is injective. For $X = \mathbb{P}^1$, with $H^2(\mathbb{P}^1, \mathbb{Z}) \cong \mathbb{Z}$ quoted from topology, show that $c_1(\mathcal{O}(n)) = \pm n$ times a generator, with a sign that depends on the convention for $\exp(2 \pi i f)$.
8. (C) Show that vector bundles of rank $r$ on $\mathbb{P}^1$ are in bijection with the double cosets $\mathrm{GL}_r(k[s]) \backslash \mathrm{GL}_r(k[t, t^{-1}]) / \mathrm{GL}_r(k[t])$, using that finitely generated projective modules over $k[t]$ are free. The theorem of Grothendieck, which this exercise does not ask you to prove, says that every such bundle is $\bigoplus_m \mathcal{O}(a_m)$. Check it for the diagonal matrices.

### Lean

Mathlib defines nonabelian $\check{H}^1$ of a presheaf of groups for a family of objects, `CategoryTheory.PresheafOfGroups.H1`, as the quotient of `CategoryTheory.PresheafOfGroups.OneCocycle` by the cohomology relation. It defines the Picard group of a commutative ring, `CommRing.Pic`, with the criterion `CommRing.Pic.subsingleton_iff` for it to vanish and instances that make it trivial for local rings and for GCD domains, which cover the two affine pieces of Example P2.7.30. Torsors for a sheaf of groups, the isomorphism $\operatorname{Pic}(X) \cong H^1(X, \mathcal{O}_X^\times)$, the Picard group of $\mathbb{P}^1$ and the first Chern class are not in Lean as stated.

### Notes and history

The classification of fibre bundles by $H^1$ with coefficients in a sheaf of groups is due to the Cartan seminar and to Grothendieck's work on nonabelian cohomology. The exponential sequence and the first Chern class go back to Kodaira and Spencer, and to the Lefschetz theorem on $(1,1)$ classes. Serre's papers of 1955 and 1956 computed line bundles and cohomology on projective space with Čech cochains, and GAGA transferred the results between the algebraic and the analytic settings. Grothendieck's theorem on vector bundles on $\mathbb{P}^1$ appeared in 1957. In the minimal model program, Theorem P2.7.28 is how Cartier divisors and line bundles become the same objects, and Proposition P2.7.29 is the form in which vanishing theorems produce sections.
