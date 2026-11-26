---
title: Spectral sequences and filtered complexes
nodes: []
sources: [Wei94, Har77]
reads_with: [Wei94:ch5]
requires: [P2.2, P2.3]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Spectral sequences and filtered complexes

### Statement

Throughout, $\mathcal{A}$ is an abelian category. All spectral sequences in this handbook are cohomological: the differentials raise the total degree by one.

**Definition P2.4.1 (spectral sequence).** Let $a \geq 0$ be an integer. A *spectral sequence* starting on page $a$ consists of the following data.

1. For each $r \geq a$, a family of objects $E_r^{p,q}$ of $\mathcal{A}$, indexed by $p, q \in \mathbb{Z}$. The family $E_r = (E_r^{p,q})$ is the *page* $r$.
2. For each $r \geq a$, maps $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ with $d_r d_r = 0$.
3. For each $r \geq a$, isomorphisms $E_{r+1}^{p,q} \cong \ker(d_r: E_r^{p,q} \to E_r^{p+r,q-r+1}) / \operatorname{im}(d_r: E_r^{p-r,q+r-1} \to E_r^{p,q})$.

The integer $p$ is the *filtration degree*, $q$ the *complementary degree*, and $n = p + q$ the *total degree*. The differential $d_r$ moves $r$ steps to the right and $r - 1$ steps down, so it raises the total degree by one.

Lean: Mathlib `CategoryTheory.SpectralSequence` (with a general complex shape on each page), and `CategoryTheory.E₂CohomologicalSpectralSequenceNat` for the first quadrant case that starts on page $2$.

A *morphism* $f: E \to E'$ of spectral sequences is a family of maps $f_r: E_r^{p,q} \to E_r'^{p,q}$ that commute with the differentials and such that $f_{r+1}$ is the map induced by $f_r$ on cohomology.

**Definition P2.4.2 (first quadrant, the limit page).** A spectral sequence is *first quadrant* if $E_a^{p,q} = 0$ whenever $p < 0$ or $q < 0$. Then $E_r^{p,q} = 0$ for all $r \geq a$ outside the first quadrant, since $E_r^{p,q}$ is a subquotient of $E_a^{p,q}$. For fixed $(p,q)$ and $r > \max(p, q+1)$, the differential leaving $E_r^{p,q}$ lands in complementary degree $q - r + 1 < 0$, and the differential arriving at $E_r^{p,q}$ starts in filtration degree $p - r < 0$. So both are zero and $E_r^{p,q} = E_{r+1}^{p,q}$. This stable value is $E_\infty^{p,q}$.

**Definition P2.4.3 (convergence).** A first quadrant spectral sequence *converges* to a family of objects $H^n$, written $E_a^{p,q} \Rightarrow H^{p+q}$, if each $H^n$ has a decreasing filtration
$$H^n = F^0 H^n \supseteq F^1 H^n \supseteq \cdots \supseteq F^n H^n \supseteq F^{n+1} H^n = 0$$
with isomorphisms $E_\infty^{p, n-p} \cong F^p H^n / F^{p+1} H^n$ for $0 \leq p \leq n$.

So $H^n$ has a finite filtration whose graded pieces are the objects $E_\infty^{p,q}$ on the line $p + q = n$. The spectral sequence determines the graded pieces, not $H^n$ itself: there is an extension problem.

**Definition P2.4.4 (filtered complex).** A *filtered complex* is a complex $C^\bullet$ in $\mathcal{A}$ with a decreasing family of subcomplexes $\cdots \supseteq F^p C^\bullet \supseteq F^{p+1} C^\bullet \supseteq \cdots$. The filtration is *first quadrant* if $F^0 C^n = C^n$ and $F^{n+1} C^n = 0$ for all $n$, and $C^n = 0$ for $n < 0$. The *graded pieces* are the complexes $\operatorname{gr}^p C^\bullet = F^p C^\bullet / F^{p+1} C^\bullet$.

**Theorem P2.4.5 (the spectral sequence of a filtered complex).** Let $C^\bullet$ be a complex with a first quadrant filtration. There is a first quadrant spectral sequence, starting on page $0$, with
$$E_0^{p,q} = \operatorname{gr}^p C^{p+q}, \qquad E_1^{p,q} = H^{p+q}(\operatorname{gr}^p C^\bullet), \qquad E_0^{p,q} \Rightarrow H^{p+q}(C^\bullet).$$
The differential $d_0$ is induced by the differential of $C^\bullet$, and $d_1: H^{p+q}(\operatorname{gr}^p C) \to H^{p+q+1}(\operatorname{gr}^{p+1} C)$ is the connecting map of the short exact sequence of complexes $0 \to \operatorname{gr}^{p+1} C^\bullet \to F^p C^\bullet / F^{p+2} C^\bullet \to \operatorname{gr}^p C^\bullet \to 0$. The filtration on the limit is $F^p H^n(C^\bullet) = \operatorname{im}(H^n(F^p C^\bullet) \to H^n(C^\bullet))$. The construction is functorial for maps of filtered complexes.

Lean: not in Lean as stated.

**Proposition P2.4.6 (edge maps and degeneration).** Let $E_2^{p,q} \Rightarrow H^{p+q}$ be a convergent first quadrant spectral sequence.

1. For each $n$ there are *edge maps* $E_2^{n,0} \to H^n$ and $H^n \to E_2^{0,n}$. The first is the composite of the epimorphism $E_2^{n,0} \to E_\infty^{n,0}$ with the inclusion $E_\infty^{n,0} = F^n H^n \subseteq H^n$. The second is the composite of the epimorphism $H^n \to H^n / F^1 H^n = E_\infty^{0,n}$ with the inclusion $E_\infty^{0,n} \subseteq E_2^{0,n}$.
2. If $E_2^{p,q} = 0$ for all $q \neq 0$, then the edge maps $E_2^{n,0} \to H^n$ are isomorphisms. If $E_2^{p,q} = 0$ for all $p \neq 0$, then the edge maps $H^n \to E_2^{0,n}$ are isomorphisms.

Lean: not in Lean as stated.

In the situation of part 2 the spectral sequence *degenerates* on page $2$: all differentials $d_r$, $r \geq 2$, are zero. More generally a spectral sequence degenerates on page $r$ if $d_s = 0$ for all $s \geq r$, so that $E_r = E_\infty$.

**Theorem P2.4.7 (the five-term exact sequence).** A convergent first quadrant spectral sequence $E_2^{p,q} \Rightarrow H^{p+q}$ gives an exact sequence
$$0 \to E_2^{1,0} \to H^1 \to E_2^{0,1} \xrightarrow{d_2} E_2^{2,0} \to H^2,$$
where the maps $E_2^{1,0} \to H^1$ and $E_2^{2,0} \to H^2$ and $H^1 \to E_2^{0,1}$ are edge maps.

Lean: not in Lean as stated.

**Proposition P2.4.8 (comparison).** Let $E \Rightarrow H$ and $E' \Rightarrow H'$ be convergent first quadrant spectral sequences, and let $f: E \to E'$ be a morphism together with maps $h^n: H^n \to H'^n$ that respect the filtrations and induce $f_\infty$ on the graded pieces. If $f_r$ is an isomorphism for one $r$, then every $h^n$ is an isomorphism.

Lean: not in Lean as stated.

This applies to the spectral sequences of filtered complexes: a map of filtered complexes that is a quasi-isomorphism on each graded piece $\operatorname{gr}^p$ is a quasi-isomorphism, since it is an isomorphism on page $1$.

### Proof in words

A filtration of a complex gives two kinds of cohomology: the cohomology of the graded pieces, which is often easy to compute, and the cohomology of the whole complex, which is what one wants. The spectral sequence connects them in steps. On page $0$ one sees only the graded pieces. On page $1$ one has their cohomology. A class on page $1$ is represented by an element $x \in F^p C$ with $dx \in F^{p+1} C$, and $d_1$ records the image of $dx$ in the next graded piece. The page $r$ keeps the elements $x$ with $dx \in F^{p+r} C$, and $d_r$ records $dx$ modulo $F^{p+r+1}$. In a first quadrant filtration, $F^{p+r} C^{n+1} = 0$ for $r$ large, so the survivors are the true cycles of $F^p C$, modulo the true boundaries, and their classes fill the graded pieces of $H^n(C)$.

The edge maps and the five-term sequence come from the shape of the first quadrant. Near the edges most differentials start or end outside the quadrant, so they vanish. The low degree terms then survive with at most one nonzero differential, $d_2: E_2^{0,1} \to E_2^{2,0}$, and the filtration of $H^1$ and of $H^2$ has few steps. Reading off these steps gives the five terms. The comparison statement is the five lemma, applied along the finite filtrations.

### Examples

**Example P2.4.9 (the filtration by truncations).** Let $C^\bullet$ be a complex with $C^n = 0$ for $n < 0$. The *stupid filtration* $F^p C^n = C^n$ for $n \geq p$ and $0$ for $n < p$ is first quadrant. Its graded piece $\operatorname{gr}^p C$ is $C^p$ placed in degree $p$. So $E_1^{p,0} = C^p$, $E_1^{p,q} = 0$ for $q \neq 0$, and $d_1$ is the differential of $C$. The spectral sequence degenerates on page $2$ and gives back $H^n(C)$. This example is trivial, but the same filtration on the hypercohomology of a complex of sheaves gives the Hodge to de Rham spectral sequence of Section 4.3.

**Example P2.4.10 (two rows give a long exact sequence).** Suppose $E_2^{p,q} = 0$ unless $q \in \{0, 1\}$. Then the only possibly nonzero differential on page $2$ or later is $d_2: E_2^{p,1} \to E_2^{p+2,0}$, and $E_3 = E_\infty$. The filtration of $H^n$ has two steps, $0 \to E_\infty^{n,0} \to H^n \to E_\infty^{n-1,1} \to 0$. Splicing these with $0 \to E_\infty^{n-1,1} \to E_2^{n-1,1} \to E_2^{n+1,0} \to E_\infty^{n+1,0} \to 0$ gives the long exact sequence
$$\cdots \to E_2^{n,0} \to H^n \to E_2^{n-1,1} \xrightarrow{d_2} E_2^{n+1,0} \to H^{n+1} \to \cdots$$
(Exercise 3). The Gysin sequence of an oriented circle bundle in topology is of this type.

**Example P2.4.11 (a nonsplit extension).** The spectral sequence does not determine $H^n$. Let $A = \mathbb{Z}/4$ as a complex in degree $0$, filtered by $F^0 = \mathbb{Z}/4$, $F^1 = 2\mathbb{Z}/4$, $F^2 = 0$. This is not a first quadrant filtration in the sense above, since $F^1 C^0 \neq 0$, but the construction of the proof applies to any finite filtration. The graded pieces are $\mathbb{Z}/2$ and $\mathbb{Z}/2$, and the spectral sequence has $E_\infty^{0,0} = \mathbb{Z}/2$ and $E_\infty^{1,-1} = \mathbb{Z}/2$. The complex $\mathbb{Z}/2 \oplus \mathbb{Z}/2$ with the filtration by the second summand has the same $E_\infty$ page. So the limit $H^0$ is $\mathbb{Z}/4$ in one case and $(\mathbb{Z}/2)^2$ in the other.

**Example P2.4.12 (the five-term sequence for group cohomology).** For a group $G$, a normal subgroup $N$ and a $G$-module $M$, the Hochschild-Serre spectral sequence $E_2^{p,q} = H^p(G/N, H^q(N, M)) \Rightarrow H^{p+q}(G, M)$ is the Grothendieck spectral sequence of Section 4.3 for $M \mapsto M^N \mapsto (M^N)^{G/N}$. Its five-term sequence is the inflation-restriction sequence
$$0 \to H^1(G/N, M^N) \to H^1(G, M) \to H^1(N, M)^{G/N} \to H^2(G/N, M^N) \to H^2(G, M).$$
The Leray spectral sequence of Section 4.3 gives the analogous sequence for sheaf cohomology and a morphism of spaces.

### Proof

For the proofs, work with elements. A diagram with finitely many objects in $\mathcal{A}$ lies in a small abelian full subcategory closed under kernels and cokernels, and the Freyd-Mitchell embedding theorem of Section 2.2 embeds it exactly and fully faithfully in a module category. So arguments with elements of modules prove the statements in $\mathcal{A}$.

*Proof of the theorem on filtered complexes.* Write $Z_r^{p,n} = \{x \in F^p C^n : dx \in F^{p+r} C^{n+1}\}$ for $r \geq 0$, the elements of filtration $p$ that are cycles up to filtration $p + r$. Put $Z_{-1}^{p,n} = F^p C^n$. Define
$$E_r^{p,q} = \frac{Z_r^{p,p+q}}{Z_{r-1}^{p+1,p+q} + d Z_{r-1}^{p-r+1,p+q-1}}.$$
Both terms of the denominator lie in $Z_r^{p,p+q}$: an element of $Z_{r-1}^{p+1}$ has $dx \in F^{p+r}$, and an element $dy$ with $y \in Z_{r-1}^{p-r+1}$ lies in $F^p$ and has $d(dy) = 0$. The differential $d$ maps $Z_r^{p,n}$ into $Z_r^{p+r,n+1}$, since $d(dx) = 0$, and it maps the denominator of $E_r^{p,q}$ into the denominator of $E_r^{p+r,q-r+1}$. So $d$ induces $d_r: E_r^{p,q} \to E_r^{p+r,q-r+1}$ with $d_r d_r = 0$.

For $r = 0$ the formula gives $Z_0^{p} = F^p C$ and a denominator $F^{p+1} C + d F^{p+1} C = F^{p+1} C$, so $E_0^{p,q} = \operatorname{gr}^p C^{p+q}$, with $d_0$ induced by $d$. For $r = 1$ it gives $Z_1^{p,n} / (F^{p+1} C^n + d F^p C^{n-1})$. The cycles of $\operatorname{gr}^p C$ in degree $n$ are $Z_1^{p,n} / F^{p+1} C^n$, and the boundaries are $(d F^p C^{n-1} + F^{p+1} C^n) / F^{p+1} C^n$. So $E_1^{p,q} = H^{p+q}(\operatorname{gr}^p C)$. A class in $E_1^{p,q}$ is represented by $x \in F^p C$ with $dx \in F^{p+1} C$, and $d_1$ sends it to the class of $dx$ in $H(\operatorname{gr}^{p+1} C)$. This is the recipe for the connecting map of $0 \to \operatorname{gr}^{p+1} C \to F^p C / F^{p+2} C \to \operatorname{gr}^p C \to 0$ in Section 3.1: lift $x$, apply $d$, and read the result in the subcomplex.

The isomorphism $E_{r+1} \cong H(E_r, d_r)$ is a direct computation with these subgroups. It is done in Weibel, Chapter 5, and is not repeated here. Functoriality is clear from the formulas, since a map of filtered complexes maps each $Z_r^{p}$ into the corresponding group.

The filtration is first quadrant, so $E_0^{p,q} = \operatorname{gr}^p C^{p+q}$ vanishes for $p < 0$ and for $q < 0$. It remains to identify $E_\infty$. Fix $n$ and $p$ with $0 \leq p \leq n$, and let $r > n + 1$. Then $F^{p+r} C^{n+1} = 0$, since $p + r \geq n + 2$. So $Z_r^{p,n} = Z^p$, the cycles of $F^p C^n$. Also $Z_{r-1}^{p+1,n} = Z^{p+1}$, the cycles of $F^{p+1} C^n$, and $p - r + 1 \leq 0$, so $Z_{r-1}^{p-r+1,n-1} = \{y \in C^{n-1} : dy \in F^p C^n\}$ and $d Z_{r-1}^{p-r+1,n-1} = B \cap F^p C^n$, where $B = d C^{n-1}$. So
$$E_\infty^{p,n-p} = \frac{Z^p}{Z^{p+1} + (B \cap F^p C^n)}.$$
On the other side, $F^p H^n(C) = (Z^p + B)/B$, so
$$\frac{F^p H^n}{F^{p+1} H^n} = \frac{Z^p + B}{Z^{p+1} + B} \cong \frac{Z^p}{Z^p \cap (Z^{p+1} + B)} = \frac{Z^p}{Z^{p+1} + (Z^p \cap B)},$$
by the second isomorphism theorem and the modular law, which applies since $Z^{p+1} \subseteq Z^p$. Finally $Z^p \cap B = B \cap F^p C^n$, because every boundary is a cycle. This proves $E_\infty^{p,n-p} \cong F^p H^n / F^{p+1} H^n$. The filtration of $H^n$ starts at $F^0 H^n = H^n$ and ends at $F^{n+1} H^n = 0$, because $F^0 C^n = C^n$ and $F^{n+1} C^n = 0$. $\square$

*Proof of the proposition on edge maps.* Consider $E_r^{n,0}$ for $r \geq 2$. The differential leaving it lands in $E_r^{n+r, 1-r}$, which is zero since $1 - r < 0$. So $E_{r+1}^{n,0}$ is the cokernel of the arriving differential, a quotient of $E_r^{n,0}$. Composing these quotients gives an epimorphism $E_2^{n,0} \to E_\infty^{n,0}$. On the line $p + q = n$, the term $E_\infty^{n,0}$ is $F^n H^n / F^{n+1} H^n = F^n H^n$, a subobject of $H^n$. Dually, the differential arriving at $E_r^{0,n}$ starts at $E_r^{-r, n+r-1} = 0$, so $E_{r+1}^{0,n}$ is a kernel, a subobject of $E_r^{0,n}$, and $E_\infty^{0,n} = F^0 H^n / F^1 H^n = H^n / F^1 H^n$ is a subobject of $E_2^{0,n}$. This proves part 1.

For part 2, suppose $E_2^{p,q} = 0$ for $q \neq 0$. Every differential $d_r$, $r \geq 2$, changes $q$ by $1 - r \neq 0$, so its source or target is zero. So $E_2 = E_\infty$. On the line $p + q = n$ the only nonzero term is $E_\infty^{n,0}$. So $F^1 H^n = \cdots = F^n H^n$ and $F^0 H^n / F^1 H^n = 0$, hence $H^n = F^n H^n = E_\infty^{n,0} = E_2^{n,0}$, and this identification is the edge map. The case $p \neq 0$ is the same with the roles of the edges exchanged. $\square$

*Proof of the five-term exact sequence.* The low degree terms on page $\infty$ are as follows.

1. $E_\infty^{1,0} = E_2^{1,0}$. The differentials arriving at $E_r^{1,0}$ start at $E_r^{1-r,r-1}$ with $1 - r < 0$, and those leaving it end at $E_r^{1+r,1-r}$ with $1 - r < 0$.
2. $E_\infty^{0,1} = \ker(d_2: E_2^{0,1} \to E_2^{2,0})$. Nothing arrives at $E_r^{0,1}$, and for $r \geq 3$ the differential leaving it ends at complementary degree $2 - r < 0$.
3. $E_\infty^{2,0} = \operatorname{coker}(d_2: E_2^{0,1} \to E_2^{2,0})$. Nothing nonzero leaves $E_r^{2,0}$, and for $r \geq 3$ the differential arriving at it starts at filtration degree $2 - r < 0$.

The filtration of $H^1$ is $H^1 = F^0 H^1 \supseteq F^1 H^1 \supseteq F^2 H^1 = 0$, with $F^1 H^1 = E_\infty^{1,0}$ and $H^1 / F^1 H^1 = E_\infty^{0,1}$. With items 1 and 2 this gives an exact sequence $0 \to E_2^{1,0} \to H^1 \to \ker d_2 \to 0$. Item 3 shows that $E_2^{2,0} \to E_\infty^{2,0}$ is the cokernel of $d_2$, and $E_\infty^{2,0} = F^2 H^2 \subseteq H^2$. Splice the four pieces:
$$0 \to E_2^{1,0} \to H^1 \to \ker d_2 \to 0, \qquad 0 \to \ker d_2 \to E_2^{0,1} \xrightarrow{d_2} E_2^{2,0} \to \operatorname{coker} d_2 \to 0, \qquad \operatorname{coker} d_2 \hookrightarrow H^2.$$
Exactness at $H^1$ holds because the image of $E_2^{1,0}$ is the kernel of $H^1 \to \ker d_2$. Exactness at $E_2^{0,1}$ holds because the image of $H^1$ is $\ker d_2$. Exactness at $E_2^{2,0}$ holds because $\operatorname{coker} d_2 \to H^2$ is a monomorphism, so the kernel of $E_2^{2,0} \to H^2$ equals the kernel of $E_2^{2,0} \to \operatorname{coker} d_2$, which is $\operatorname{im} d_2$. The maps are the edge maps by construction. $\square$

*Proof of the comparison proposition.* If $f_r$ is an isomorphism of complexes, then the induced map $f_{r+1}$ on cohomology is an isomorphism. By induction every $f_s$, $s \geq r$, is an isomorphism, and so is $f_\infty$. Fix $n$. The map $h^n$ induces isomorphisms on the graded pieces $F^p H^n / F^{p+1} H^n \cong E_\infty^{p,n-p}$. Prove by descending induction on $p$ that $h^n: F^p H^n \to F^p H'^n$ is an isomorphism. For $p = n + 1$ both sides are zero. For the induction step, apply the five lemma of Section 2.3 to the map of short exact sequences
$$0 \to F^{p+1} H^n \to F^p H^n \to E_\infty^{p,n-p} \to 0 \quad \text{and} \quad 0 \to F^{p+1} H'^n \to F^p H'^n \to E_\infty'^{p,n-p} \to 0.$$
For $p = 0$ this gives that $h^n$ is an isomorphism. $\square$

### Exercises

1. (A) Draw the first quadrant of page $3$ and mark the arrows $d_3$ that start at $E_3^{0,2}$ and at $E_3^{1,2}$. For which $(p,q)$ is $E_3^{p,q} = E_\infty^{p,q}$ for every first quadrant spectral sequence?
2. (A) Let $E_2^{p,q} \Rightarrow H^{p+q}$ be first quadrant with $E_2^{p,q} = 0$ unless $p \in \{0, 1\}$. Show that $E_2 = E_\infty$ and that there are short exact sequences $0 \to E_2^{1,n-1} \to H^n \to E_2^{0,n} \to 0$.
3. (B) Prove the long exact sequence of the example with two rows, and identify all the maps.
4. (B) Let $E_2^{p,q} \Rightarrow H^{p+q}$ be first quadrant, with $E_2^{p,q} = 0$ for $0 < q < m$. Show that $E_2^{n,0} \to H^n$ is an isomorphism for $n < m$ and a monomorphism for $n = m$.
5. (B) Let $C^\bullet$ have a first quadrant filtration. Show that $H^n(C) = 0$ if $H^n(\operatorname{gr}^p C) = 0$ for all $p$. Show by an example with a filtration of length two that the converse fails.
6. (B) Let $E$ be a first quadrant spectral sequence of finite dimensional vector spaces over a field converging to $H$. Show that $\dim H^n \leq \sum_{p+q=n} \dim E_2^{p,q}$, with equality for all $n$ if and only if the sequence degenerates on page $2$. Deduce that $\sum_n (-1)^n \dim H^n = \sum_{p,q} (-1)^{p+q} \dim E_2^{p,q}$ when only finitely many $E_2^{p,q}$ are nonzero.
7. (C) Complete the proof of the theorem on filtered complexes: show that $\ker(d_r: E_r^{p,q} \to E_r^{p+r,q-r+1})$ is the image of $Z_{r+1}^{p,p+q} + Z_{r-1}^{p+1,p+q}$, that the image of $d_r$ arriving at $E_r^{p,q}$ is the image of $d Z_r^{p-r,p+q-1} + Z_{r-1}^{p+1,p+q}$, and deduce $H(E_r, d_r) \cong E_{r+1}$.

### Lean

Mathlib defines spectral sequences with an arbitrary complex shape on each page in `Mathlib/Algebra/Homology/SpectralSequence/Basic.lean`, through `CategoryTheory.SpectralSequence`, and the first quadrant shape through `ComplexShape.spectralSequenceNat`. Spectral sequences are constructed from Verdier's spectral objects, `CategoryTheory.Abelian.SpectralObject`, by `CategoryTheory.Abelian.SpectralObject.spectralSequence`. The spectral sequence of a filtered complex, convergence in the sense above, the edge maps and the five-term sequence are not yet stated in this form. The handbook adds no `MinimalModel` node here.

### Notes and history

Leray introduced spectral sequences and sheaves together, in work written as a prisoner of war and published from 1946 on, to compute the cohomology of a space fibred over another. Koszul gave the algebraic form with filtered differential modules. Cartan and Eilenberg's book of 1956 put spectral sequences into homological algebra, and Serre's thesis of 1951 made the Leray spectral sequence of a fibration a tool of homotopy theory. The definitions of convergence vary between sources. For first quadrant spectral sequences, all common definitions agree with the one above.
