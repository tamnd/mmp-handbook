---
title: The structure sheaf of the prime spectrum
nodes: []
sources: [Vak25, Har77, GW20, EGA1]
reads_with: [Vak25:ch4, Har77:II.2, GW20:ch2]
requires: [P1.2, P2.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The structure sheaf of the prime spectrum

### Statement

Let $A$ be a ring and $X = \operatorname{Spec} A$, with the Zariski topology of P1 Ch. 2. For $f \in A$ the basic open set is $D(f) = \{\mathfrak{p} : f \notin \mathfrak{p}\}$. By Proposition P1.2.17 the sets $D(f)$ form a basis of the topology, and $D(f) \cap D(g) = D(fg)$, so the basis is closed under finite intersections. The plan of the section is to give each basic open set $D(f)$ the ring $A_f$ and then to extend to all open sets by the theorem on sheaves on a base, Theorem P2.5.34. Two points need care. First, an open set can be $D(f)$ for several $f$, so the ring must not depend on the choice. Second, the rule must satisfy the sheaf condition for covers of $D(f)$ by smaller basic open sets.

**Lemma P3.1.1 (inclusions of basic open sets).** For $f, g \in A$ the following are equivalent:

1. $D(f) \subseteq D(g)$;
2. $f^n \in (g)$ for some $n \geq 1$;
3. the image of $g$ in $A_f$ is a unit.

When they hold, there is a unique map of $A$-algebras $\rho_{fg} \colon A_g \to A_f$, and for every $A$-module $M$ a unique $A_g$-linear map $M_g \to M_f$ that is compatible with the maps from $M$. If $D(f) = D(g)$, these maps are isomorphisms.

Lean: Mathlib `PrimeSpectrum.basicOpen_le_basicOpen_iff` (1 and 2, in the form $f \in \sqrt{(g)}$) and `PrimeSpectrum.basicOpen_le_basicOpen_iff_algebraMap_isUnit` (1 and 3), proved in Mathlib; `IsLocalization.Away.lift` for the map.

The lemma lets the ring of a basic open set be defined by the set alone. For an open set $U$ of $X$, put
$$S_U = \{ g \in A : U \subseteq D(g) \},$$
the set of elements that vanish at no point of $U$. It is multiplicative, since $D(gh) = D(g) \cap D(h)$ and $D(1) = X$.

**Definition P3.1.2 (the presheaf on the basis).** Let $M$ be an $A$-module. For a basic open set $D$ put $\widetilde{M}(D) = S_D^{-1} M$, and for basic open sets $D' \subseteq D$ let the restriction $\widetilde{M}(D) \to \widetilde{M}(D')$ be the map $S_D^{-1} M \to S_{D'}^{-1} M$ given by $S_D \subseteq S_{D'}$. Write $\mathcal{O}$ for $\widetilde{A}$. Then $\mathcal{O}(D)$ is a ring, $\widetilde{M}(D)$ is an $\mathcal{O}(D)$-module, and restriction respects these structures.

For $D = D(f)$ the element $f$ lies in $S_D$, and each $g \in S_D$ is a unit in $A_f$ by the lemma. So the universal property of localization (Proposition P1.2.4) gives inverse isomorphisms $M_f \cong S_{D(f)}^{-1} M$. In this sense $\widetilde{M}(D(f)) = M_f$, and the restriction from $D(g)$ to $D(f) \subseteq D(g)$ is the map $M_g \to M_f$ of the lemma.

**Theorem P3.1.3 (the sheaf property on the basis).** Let $M$ be an $A$-module, $f \in A$ and $D(f) = \bigcup_{i \in I} D(f_i)$ a cover by basic open sets. Then the sequence
$$0 \to M_f \to \prod_{i \in I} M_{f_i} \to \prod_{i, j \in I} M_{f_i f_j}$$
is exact, where the first map is restriction and the second sends $(s_i)$ to $(s_i|_{D(f_if_j)} - s_j|_{D(f_if_j)})_{i,j}$. In words: a section of $\widetilde{M}$ over $D(f)$ that restricts to $0$ on every $D(f_i)$ is $0$, and sections over the $D(f_i)$ that agree on the overlaps come from one section over $D(f)$. So $\widetilde{M}$ is a sheaf on the basis of basic open sets (Definition P2.5.33).

Lean: Mathlib constructs the structure sheaf in another way, with locally fractional sections, as `AlgebraicGeometry.Spec.structureSheaf`. The sheaf property is then built into the definition, and the content of the theorem is `AlgebraicGeometry.StructureSheaf.IsLocalization.to_basicOpen` (the sections over $D(f)$ are $A_f$, proved in Mathlib). For modules: `AlgebraicGeometry.tilde`.

**Definition P3.1.4 (the structure sheaf).** The *structure sheaf* $\mathcal{O}_X$ of $X = \operatorname{Spec} A$ is the sheaf of rings on $X$ that extends the sheaf $\mathcal{O}$ on the basis, given by Theorem P2.5.34. For an $A$-module $M$, the sheaf $\widetilde{M}$ is the $\mathcal{O}_X$-module that extends $\widetilde{M}$ on the basis.

Theorem P2.5.34 is stated for sheaves of abelian groups. Its proof defines the section of the extension over an open set $U$ as a family of germs $(s_x)_{x \in U}$ that is locally given by sections over basic open sets. With rings in place of abelian groups the families of germs form a ring, and with an $\mathcal{O}$-module on the basis they form a module over it. So $\mathcal{O}_X$ is a sheaf of rings and $\widetilde{M}$ is an $\mathcal{O}_X$-module, in the sense of Definition P2.6.2.

**Corollary P3.1.5 (sections over basic open sets).** For every $f \in A$, $\mathcal{O}_X(D(f)) = A_f$ and $\widetilde{M}(D(f)) = M_f$. In particular the ring of global sections is $\Gamma(X, \mathcal{O}_X) = A$, and $\Gamma(X, \widetilde{M}) = M$.

Lean: Mathlib `AlgebraicGeometry.StructureSheaf.globalSectionsIso` (the global sections are $A$) and `AlgebraicGeometry.tilde.isoTop` (the global sections of $\widetilde{M}$ are $M$), both proved in Mathlib.

### Proof in words

The sheaf property is a partition of unity. Take $f = 1$. The sets $D(f_i)$ cover $X$ exactly when no prime contains all the $f_i$, that is, when the $f_i$ generate the unit ideal. Then $1 = \sum a_i f_i$ is a finite sum, so finitely many $D(f_i)$ already cover $X$: this is the quasi-compactness of P1.2.17. If $s_i = m_i/f_i^n$ are compatible sections, the global section is $m = \sum c_i m_i'$ for a partition of unity $1 = \sum c_i g_i$ adapted to the denominators. It is the algebraic form of the gluing of local functions by a partition of unity on a manifold. The only difference is that the denominators and the torsion in the localizations must be cleared first, which is why the proof replaces $f_i$ by a power.

The case of a general $f$ reduces to $f = 1$, because $D(f)$ is the spectrum of $A_f$ and the localizations of $M_f$ at the $f_i$ are the $M_{f_i}$. Infinite covers reduce to finite ones by quasi-compactness, with one more use of the injectivity part.

### Examples

**Example P3.1.6 (the integers).** Let $X = \operatorname{Spec} \mathbb{Z}$. Its points are $(0)$ and the $(p)$ for primes $p$. A nonempty open set is $U = X \setminus \{(p_1), \dots, (p_r)\}$, and it is $D(n)$ for $n = p_1 \cdots p_r$. So every open set is basic and $\mathcal{O}_X(U) = \mathbb{Z}[1/p_1, \dots, 1/p_r]$. The point $(0)$ lies in every nonempty open set, so it is dense: it is the generic point of $X$. The stalk at $(0)$ is the colimit of the rings $\mathbb{Z}[1/n]$, which is $\mathbb{Q}$, and the stalk at $(p)$ is the colimit over the $n$ prime to $p$, which is $\mathbb{Z}_{(p)}$. Section 1.2 proves this in general. An element of $\mathbb{Q}$ is a function defined away from the primes in its denominator.

**Example P3.1.7 (the affine line).** Let $k$ be a field and $X = \operatorname{Spec} k[x]$. The ring $k[x]$ is a principal ideal domain, so its primes are $(0)$ and the ideals $(\pi)$ for monic irreducible $\pi$. As for $\mathbb{Z}$, every open set is $D(g)$ with $g$ a product of irreducibles, and $\mathcal{O}_X(D(g)) = k[x]_g$, the rational functions whose denominators divide a power of $g$. When $k$ is algebraically closed the closed points are the $(x - a)$ with $a \in k$, and they are the points of the classical affine line.

**Example P3.1.8 (the power in the lemma).** In $A = k[x]$, $D(x) = D(x^2)$, while $x \notin (x^2)$. So the condition $D(f) \subseteq D(g)$ does not give $f \in (g)$, only $f^n \in (g)$. The two rings $A_x$ and $A_{x^2}$ are equal subrings of $k(x)$, as the lemma predicts. In a ring with nilpotents the power cannot be avoided in a stronger sense: in $A = k[x]/(x^2)$, $D(x) = \emptyset = D(0)$, and $A_x = 0$, since $x$ is nilpotent.

**Example P3.1.9 (a product).** Let $A = A_1 \times A_2$ and $e = (1, 0)$. By Proposition P1.2.20, $X = D(e) \sqcup D(1 - e)$, and $A_e = A_1$, $A_{1 - e} = A_2$. So $\mathcal{O}_X$ is $\mathcal{O}_{\operatorname{Spec} A_1}$ on one piece and $\mathcal{O}_{\operatorname{Spec} A_2}$ on the other. The sheaf property for the cover $X = D(e) \cup D(1 - e)$ is the isomorphism $A \cong A_1 \times A_2$, since $D(e) \cap D(1 - e) = D(0) = \emptyset$ and $A_0 = 0$.

**Example P3.1.10 (sections over an open set that is not basic).** Let $k$ be a field, $A = k[x, y]$, $X = \operatorname{Spec} A$ the affine plane and $U = D(x) \cup D(y)$, the complement of the closed point $\mathfrak{m} = (x, y)$. By the sheaf property, $\mathcal{O}_X(U)$ is the set of pairs $(a, b) \in A_x \times A_y$ with the same image in $A_{xy}$. All three rings are subrings of $k(x, y)$, so $\mathcal{O}_X(U) = A_x \cap A_y$. An element of this intersection is $g/x^m = h/y^n$ with $g, h \in A$, so $y^n g = x^m h$. As $A$ is factorial and $x$, $y$ are coprime primes, $x^m$ divides $g$, and the element lies in $A$. So $\mathcal{O}_X(U) = A$. Here the presheaf rule $U \mapsto S_U^{-1}A$ also gives $A$, since the only $g$ with no zero on $U$ are the constants. But $U$ is not a basic open set, and Chapter 2 shows that $(U, \mathcal{O}_X|_U)$ is not $\operatorname{Spec}$ of any ring. A function on $U$ extends across the point, which is the algebraic Hartogs theorem of P1 Ch. 8 in its simplest case.

### Proof

*Proof of the lemma.* By Proposition P1.2.16, $D(f) \subseteq D(g)$ means $V(g) \subseteq V(f)$, which holds if and only if $f \in \sqrt{(g)}$, that is, $f^n = a g$ for some $n$ and $a \in A$. Then $g \cdot (a/f^n) = 1$ in $A_f$, so 2 implies 3. If $g \cdot b/f^m = 1$ in $A_f$, then $f^k(gb - f^m) = 0$ for some $k$, so $f^{k + m} = g b f^k \in (g)$, and 3 implies 2. The map $\rho_{fg}$ exists and is unique by the universal property of $A \to A_g$ (Proposition P1.2.4), since $g$ maps to a unit of $A_f$. For a module, $M_g = A_g \otimes_A M$, and the map is $\rho_{fg} \otimes 1$; it is unique because $M_g$ is generated over $A_g$ by the image of $M$. If $D(f) = D(g)$, the maps $A_g \to A_f$ and $A_f \to A_g$ compose to $A$-algebra maps $A_f \to A_f$ and $A_g \to A_g$, which are the identity by uniqueness. $\square$

*Proof of the theorem.* Step 1, reduction to $f = 1$. Put $B = A_f$ and $N = M_f$. By Proposition P1.2.19 the map $\operatorname{Spec} B \to \operatorname{Spec} A$ is a homeomorphism onto $D(f)$, and it maps $D(f_i/1) \subseteq \operatorname{Spec} B$ onto $D(f) \cap D(f_i) = D(f_i)$. Since $D(f_i) \subseteq D(f)$, the element $f$ is a unit in $A_{f_i}$ by the lemma, so $N_{f_i} = (M_f)_{f_i} = M_{f f_i} = M_{f_i}$, and in the same way $N_{f_i f_j} = M_{f_i f_j}$. These identifications match the maps of the sequence. So it is enough to prove the theorem for the ring $B$, the module $N$ and the cover of $\operatorname{Spec} B$ by the $D(f_i)$. From now on $f = 1$ and $X = \bigcup_i D(f_i)$.

Step 2, a finite partition of unity. The equality $X = \bigcup D(f_i)$ says that no prime contains all the $f_i$. So the ideal they generate is $A$, and $1 = \sum_{i \in J} a_i f_i$ for a finite subset $J \subseteq I$. For each $N \geq 1$, the elements $f_i^N$ with $i \in J$ also generate $A$, since $D(f_i^N) = D(f_i)$ and so these sets still cover $X$.

Step 3, injectivity for a finite cover. Let $m \in M$ have image $0$ in $M_{f_i}$ for all $i \in J$. Then $f_i^{n} m = 0$ for one $n$ that works for all $i \in J$, since $J$ is finite. Write $1 = \sum_{i \in J} b_i f_i^n$. Then $m = \sum b_i f_i^n m = 0$. So $M \to \prod_{i \in J} M_{f_i}$ is injective, and so is $M \to \prod_{i \in I} M_{f_i}$.

Step 4, gluing for a finite cover. Let $s_i \in M_{f_i}$, $i \in J$, agree in each $M_{f_i f_j}$. Write $s_i = m_i / f_i^n$ with $m_i \in M$ and one $n$ for all $i \in J$. Agreement in $M_{f_i f_j}$ means that $(f_i f_j)^{N} (f_j^n m_i - f_i^n m_j) = 0$, with one $N$ for all pairs in $J \times J$. Put $g_i = f_i^{n + N}$ and $m_i' = f_i^N m_i$. Then $s_i = m_i'/g_i$, and the last equation says $g_j m_i' = g_i m_j'$ for all $i, j \in J$. By Step 2 there are $c_j$ with $1 = \sum_{j \in J} c_j g_j$. Put $m = \sum_{j \in J} c_j m_j'$. For $i \in J$,
$$g_i m = \sum_j c_j g_i m_j' = \sum_j c_j g_j m_i' = m_i',$$
so $m/1 = m_i'/g_i = s_i$ in $M_{f_i}$.

Step 5, gluing for the whole cover. Let $(s_i)_{i \in I}$ be compatible and let $m$ be the element of Step 4 for the finite subfamily $J$. Let $k \in I$. The sets $D(f_k f_i) = D(f_k) \cap D(f_i)$, $i \in J$, cover $D(f_k)$, since the $D(f_i)$ with $i \in J$ cover $X$. In $M_{f_k f_i}$ the image of $m$ is the image of $s_i$, which is the image of $s_k$ by compatibility. By Step 3, applied after the reduction of Step 1 to the ring $A_{f_k}$, the module $M_{f_k}$ and the finite cover of $D(f_k)$ by the $D(f_k f_i)$, $i \in J$, the elements $m/1$ and $s_k$ of $M_{f_k}$ are equal. So $m$ restricts to $s_k$ for every $k \in I$, and the sequence is exact in the middle. $\square$

*Proof of the corollary.* By Theorem P2.5.34 the extension $\mathcal{O}_X$ agrees with $\mathcal{O}$ on basic open sets, and $\mathcal{O}(D(f)) = A_f$ by the remark after Definition P3.1.2. The same holds for $\widetilde{M}$. For $f = 1$, $D(1) = X$ and $A_1 = A$. $\square$

### Exercises

1. (A) Show that $S_U = \{g : U \subseteq D(g)\}$ is a saturated multiplicative set: if $gh \in S_U$ then $g, h \in S_U$. For $U = D(f)$, show that $S_U$ is the set of $g$ that become units in $A_f$.
2. (A) Let $A = \mathbb{Z}$. Compute $\mathcal{O}_X(U)$ and the restriction maps for $U = D(6) \subseteq D(2) \subseteq X$. Show that every open set of $\operatorname{Spec} \mathbb{Z}$ is basic. Is every open set of $\operatorname{Spec} k[x, y]$ basic?
3. (A) Let $A$ be a ring with nilradical $N$. Show that $\operatorname{Spec} A$ and $\operatorname{Spec} A/N$ have the same space, and that $\mathcal{O}_{\operatorname{Spec} A}(D(f)) \to \mathcal{O}_{\operatorname{Spec} A/N}(D(f))$ is surjective with kernel $N_f$.
4. (B) Prove directly, without the theorem, that $\operatorname{Spec} A$ is quasi-compact and that every basic open set $D(f)$ is quasi-compact. Give an example of an open subset of the spectrum of a non-Noetherian ring that is not quasi-compact. (Try $A = k[x_1, x_2, \dots]$ and the complement of the origin.)
5. (B) Let $A = k[x, y, z]$ and $U = \operatorname{Spec} A \setminus V(x, y)$. Compute $\mathcal{O}(U)$ by the method of Example P3.1.10, and show that it is $A$. What changes for $U = \operatorname{Spec} A \setminus V(x)$?
6. (B) Hartshorne's definition. For an open set $U \subseteq \operatorname{Spec} A$ let $\mathcal{O}'(U)$ be the set of functions $s \colon U \to \bigsqcup_{\mathfrak{p} \in U} A_\mathfrak{p}$ with $s(\mathfrak{p}) \in A_\mathfrak{p}$ that are locally fractions: each point has a neighbourhood $V$ and $a, g \in A$ with $g \notin \mathfrak{q}$ and $s(\mathfrak{q}) = a/g$ for all $\mathfrak{q} \in V$. Show that $\mathcal{O}'$ is a sheaf, and construct an isomorphism $\mathcal{O}_X \cong \mathcal{O}'$. (Use the stalk computation of Section 1.2, or prove directly that $\mathcal{O}'(D(f)) = A_f$.)

### Lean

Mathlib defines the structure sheaf of $\operatorname{Spec} R$ as `AlgebraicGeometry.Spec.structureSheaf`, by the definition of Exercise 6: a section over $U$ is a dependent function into the localizations $R_\mathfrak{p}$ that is locally a fraction. The sheaf condition then holds by construction, and the work moves to the identification of the sections over a basic open set: the instance `AlgebraicGeometry.StructureSheaf.IsLocalization.to_basicOpen` says that the sections over $D(r)$ are a localization of $R$ at the powers of $r$, and `AlgebraicGeometry.StructureSheaf.globalSectionsIso` gives the global sections. The module version is `AlgebraicGeometry.tilde`, with `AlgebraicGeometry.tilde.isoTop`. The construction on a basis, as in this section, is not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

The construction is due to Grothendieck in EGA I (1960), where the structure sheaf of $\operatorname{Spec} A$ is defined on the basis of the sets $D(f)$ exactly as here and then extended. Serre's paper *Faisceaux algébriques cohérents* of 1955 had already defined varieties as spaces with a sheaf of local rings, but only over an algebraically closed field and with closed points only. Hartshorne, Section II.2, uses the definition of Exercise 6, and Vakil, Chapter 4, uses the basis with the same partition of unity argument. Mumford's Red Book (Mum99) gives a short form of the same proof. The literature state of every result in this section is theorem.
