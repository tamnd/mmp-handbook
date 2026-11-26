---
title: Flat modules
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [AM69:ch2, Mat86:ch3, Eis95:ch6]
requires: [P1.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Flat modules

### Statement

**Definition P1.1.43 (flat module, flat homomorphism).** An $A$-module $N$ is *flat* if for every injective linear map $u: M' \to M$ the map $u \otimes 1: M' \otimes_A N \to M \otimes_A N$ is injective. A ring homomorphism $A \to B$ is *flat* if $B$ is a flat $A$-module.

Lean: Mathlib `Module.Flat` (a definition, through the injectivity of `rTensor` on ideals).

**Proposition P1.1.44 (flatness and exact sequences).** Let $N$ be flat. Then for every exact sequence $M' \xrightarrow{f} M \xrightarrow{g} M''$ the sequence $M' \otimes N \to M \otimes N \to M'' \otimes N$ is exact. Conversely, if tensoring with $N$ keeps every short exact sequence exact, then $N$ is flat.

Lean: Mathlib `Module.Flat.rTensor_preserves_injective_linearMap` and `Module.Flat.iff_rTensor_exact` (proved in Mathlib).

*Proof.* Let $K = \operatorname{im} f = \ker g$ and $I = \operatorname{im} g \subseteq M''$. The sequence $0 \to K \to M \to I \to 0$ is exact, so $K \otimes N \to M \otimes N \to I \otimes N \to 0$ is exact by right exactness. The map $I \otimes N \to M'' \otimes N$ is injective since $N$ is flat. So the kernel of $M \otimes N \to M'' \otimes N$ is the kernel of $M \otimes N \to I \otimes N$, which is the image of $K \otimes N$. Since $M' \to K$ is onto, $M' \otimes N \to K \otimes N$ is onto, again by right exactness. So the kernel is the image of $M' \otimes N$. The converse holds because an injective map $M' \to M$ is part of the short exact sequence $0 \to M' \to M \to M/M' \to 0$. $\square$

**Proposition P1.1.45 (free and projective modules).** A direct sum $\bigoplus N_\lambda$ is flat if and only if every $N_\lambda$ is flat. In particular $A$ is flat, every free module is flat, and every projective module is flat.

Lean: Mathlib `Module.Flat.directSum_iff`, `Module.Flat.of_free` and `Module.Flat.of_projective` (proved in Mathlib).

*Proof.* For a linear map $u: M' \to M$, the map $u \otimes 1$ on $M' \otimes \bigoplus N_\lambda \cong \bigoplus M' \otimes N_\lambda$ is the direct sum of the maps $u \otimes 1_{N_\lambda}$, by the basic isomorphisms of Section 1.3. A direct sum of maps is injective if and only if each one is. The module $A$ is flat since $M' \otimes A \to M \otimes A$ is $u$ itself. So free modules are flat. A projective module is a direct summand of a free module, so it is flat. $\square$

**Theorem P1.1.46 (ideal criterion).** An $A$-module $N$ is flat if and only if for every finitely generated ideal $I$ of $A$ the map $I \otimes_A N \to N$, $a \otimes n \mapsto an$, is injective.

Lean: Mathlib `Module.Flat.iff_rTensor_injective'` (for all ideals; proved in Mathlib with character modules).

*Proof sketch.* The condition is necessary by definition. For the converse, a standard reduction shows that it is enough to test injective maps $M' \to M$ with $M$ finitely generated and then with $M/M'$ cyclic, so $M/M' \cong A/I$. The condition for finitely generated ideals passes to all ideals, since an element of $I \otimes N$ already comes from $I' \otimes N$ for a finitely generated $I' \subseteq I$, and $I' \otimes N \to N$ is injective. The proof then uses the long exact sequence of $\operatorname{Tor}$: the condition says $\operatorname{Tor}_1^A(A/I, N) = 0$ for all $I$, and a dévissage gives $\operatorname{Tor}_1^A(Q, N) = 0$ for all $Q$. See Matsumura, Chapter 3, and Eisenbud, Chapter 6. P2 constructs $\operatorname{Tor}$. $\square$

**Proposition P1.1.47 (flat modules over a principal ideal domain).** Let $A$ be a principal ideal domain. An $A$-module $N$ is flat if and only if it is torsion free: $an = 0$ with $a \neq 0$ implies $n = 0$. In particular $\mathbb{Q}$ is a flat $\mathbb{Z}$-module and $\mathbb{Z}/n$, $n \geq 2$, is not.

Lean: Mathlib `Module.Flat.flat_iff_torsion_eq_bot_of_isBezout` and `IsDedekindDomain.flat_iff_torsion_eq_bot` (proved in Mathlib).

*Proof.* Let $a \neq 0$. Multiplication by $a$ on $A$ is injective, since $A$ is a domain. If $N$ is flat, the map $A \otimes N \to A \otimes N$ is injective, and it is multiplication by $a$ on $N$. So $N$ is torsion free. Conversely, let $N$ be torsion free and let $I = (a)$ be a nonzero ideal. The map $A \to I$, $x \mapsto ax$, is an isomorphism, so $I \otimes N \cong A \otimes N \cong N$, and under this isomorphism the map $I \otimes N \to N$ becomes multiplication by $a$. It is injective. For $I = 0$ there is nothing to prove. By the ideal criterion $N$ is flat. $\square$

**Lemma P1.1.48 (flatness of the third term).** Let $0 \to K \to F \to M \to 0$ be exact with $M$ flat. Then for every module $N$ the sequence $0 \to K \otimes N \to F \otimes N \to M \otimes N \to 0$ is exact.

Lean: Mathlib proves this with `Module.Flat` and `TensorProduct`; the handbook does not name a single declaration.

*Proof.* Only the injectivity of $K \otimes N \to F \otimes N$ needs proof. Choose an exact sequence $0 \to N' \to G \to N \to 0$ with $G$ free. Tensor the two sequences with each other. This gives a commutative diagram with three rows,

$$\begin{array}{ccccccc} K \otimes N' & \to & F \otimes N' & \to & M \otimes N' & \to & 0 \\ \downarrow & & \downarrow & & \downarrow & & \\ K \otimes G & \to & F \otimes G & \to & M \otimes G & \to & 0 \\ \downarrow & & \downarrow & & \downarrow & & \\ K \otimes N & \to & F \otimes N & \to & M \otimes N & \to & 0 \end{array}$$

whose rows and columns are right exact. The middle row is also injective on the left because $G$ is flat, and the right column is injective at the top because $M$ is flat. Let $x \in K \otimes N$ map to $0$ in $F \otimes N$. Lift $x$ to $y \in K \otimes G$. The image of $y$ in $F \otimes G$ maps to $0$ in $F \otimes N$, so it is the image of some $z \in F \otimes N'$. The image of $z$ in $M \otimes N'$ maps to the image of $y$ in $M \otimes G$, which is $0$ since $K \to F \to M$ is zero. As $M \otimes N' \to M \otimes G$ is injective, $z$ maps to $0$ in $M \otimes N'$, so $z$ is the image of some $w \in K \otimes N'$. The image $y'$ of $w$ in $K \otimes G$ and the element $y$ have the same image in $F \otimes G$, namely the image of $z$. As $K \otimes G \to F \otimes G$ is injective, $y = y'$. So $y$ comes from $K \otimes N'$, and its image $x$ in $K \otimes N$ is $0$ by the exactness of the left column. $\square$

**Lemma P1.1.49 (kernels for finitely presented modules).** Let $M$ be finitely presented, that is, $M \cong A^m/L$ with $L$ finitely generated. Then for every surjection $\varphi: A^n \to M$ the kernel of $\varphi$ is finitely generated.

Lean: Mathlib `Module.FinitePresentation` (a definition; this property is proved in Mathlib).

*Proof.* Let $\psi: A^m \to M$ be surjective with kernel $L$ finitely generated. Since $A^n$ is free and $\psi$ is onto, there is $\beta: A^n \to A^m$ with $\psi \beta = \varphi$. In the same way there is $\alpha: A^m \to A^n$ with $\varphi \alpha = \psi$. Let $e_1, \dots, e_n$ be the standard basis of $A^n$. The elements $e_i - \alpha\beta(e_i)$ and the elements $\alpha(l)$, for $l$ in a finite generating set of $L$, lie in $\ker \varphi$. They generate it: for $v \in \ker \varphi$, write $v = (v - \alpha\beta(v)) + \alpha\beta(v)$. The first term is a combination of the $e_i - \alpha\beta(e_i)$. For the second, $\psi\beta(v) = \varphi(v) = 0$, so $\beta(v) \in L$ and $\alpha\beta(v) \in \alpha(L)$. $\square$

**Theorem P1.1.50 (flat modules over a local ring).** Let $(A, \mathfrak{m}, k)$ be a local ring and $M$ a finitely presented flat $A$-module. Then $M$ is free, of rank $\dim_k M/\mathfrak{m}M$.

Lean: Mathlib `Module.free_of_flat_of_isLocalRing` (proved in Mathlib, for every finitely generated flat module).

*Proof.* Let $n = \dim_k M/\mathfrak{m}M$. By the corollary on minimal generators in Section 1.2, there are $x_1, \dots, x_n \in M$ whose images form a basis of $M/\mathfrak{m}M$, and they generate $M$. Let $\varphi: A^n \to M$ send $e_i$ to $x_i$, and let $K = \ker \varphi$. By the kernel lemma, $K$ is finitely generated. Tensor $0 \to K \to A^n \to M \to 0$ with $k$. By the lemma on the third term, and by $N \otimes_A k \cong N/\mathfrak{m}N$ from Section 1.3, the sequence $0 \to K/\mathfrak{m}K \to k^n \to M/\mathfrak{m}M \to 0$ is exact. The right map sends the basis of $k^n$ to a basis of $M/\mathfrak{m}M$, so it is an isomorphism. Hence $K/\mathfrak{m}K = 0$, so $K = \mathfrak{m}K$, and $K = 0$ by Nakayama's lemma. So $\varphi$ is an isomorphism. $\square$

Over a Noetherian ring every finitely generated module is finitely presented (Chapter 3). So over a Noetherian local ring a finitely generated module is flat if and only if it is free. The theorem holds for every finitely generated flat module over any local ring, but the proof is longer; see Matsumura, Chapter 3.

**Proposition P1.1.51 (flatness and intersections).** Let $N$ be flat and let $I, J$ be ideals of $A$. Then $I \otimes N \to IN$ is an isomorphism, and $(I \cap J)N = IN \cap JN$.

Lean: Mathlib `Module.Flat.rTensor_preserves_injective_linearMap` (proved in Mathlib; the intersection formula follows from it).

*Proof.* The map $I \otimes N \to A \otimes N = N$ is injective because $N$ is flat, and its image is $IN$. The sequence $0 \to I \cap J \to A \to A/I \oplus A/J$ is exact. Tensor it with $N$. By flatness, by the basic isomorphisms and by $(A/I) \otimes N \cong N/IN$, the sequence $0 \to (I \cap J) \otimes N \to N \to N/IN \oplus N/JN$ is exact. The image of the first map is $(I \cap J)N$, and the kernel of the second is $IN \cap JN$. $\square$

**Definition P1.1.52 (faithfully flat).** An $A$-module $N$ is *faithfully flat* if it is flat and $M \otimes_A N \neq 0$ for every nonzero $A$-module $M$. A ring homomorphism $A \to B$ is faithfully flat if $B$ is a faithfully flat $A$-module.

Lean: Mathlib `Module.FaithfullyFlat` (a definition).

**Proposition P1.1.53 (test for faithful flatness).** Let $A \to B$ be flat. Then $A \to B$ is faithfully flat if and only if $\mathfrak{m}B \neq B$ for every maximal ideal $\mathfrak{m}$ of $A$. In that case every maximal ideal of $A$ is the contraction of a maximal ideal of $B$.

Lean: Mathlib `Module.FaithfullyFlat.iff_flat_and_proper_ideal` (proved in Mathlib).

*Proof.* If $A \to B$ is faithfully flat, then $B/\mathfrak{m}B \cong (A/\mathfrak{m}) \otimes B \neq 0$. Conversely, let $M \neq 0$ and pick $x \neq 0$ in $M$. Then $Ax \cong A/I$ with $I = \operatorname{Ann}(x)$ a proper ideal, and $I \subseteq \mathfrak{m}$ for some maximal $\mathfrak{m}$ by Krull's theorem. Since $B$ is flat, $Ax \otimes B \to M \otimes B$ is injective. Its source is $B/IB$, which maps onto $B/\mathfrak{m}B \neq 0$. So $M \otimes B \neq 0$. For the last claim, $\mathfrak{m}B$ lies in a maximal ideal $\mathfrak{n}$ of $B$. Then $\mathfrak{n} \cap A$ is a proper ideal that contains $\mathfrak{m}$, so it equals $\mathfrak{m}$. $\square$

### Proof in words

A flat module is one that does not destroy injectivity. Free modules are flat because they are sums of copies of $A$. Over a principal ideal domain, a module fails to be flat exactly when an element is killed by a nonzero scalar. Over a local ring, a finitely presented flat module is free: Nakayama's lemma gives a surjection $A^n \to M$ that is an isomorphism mod $\mathfrak{m}$, and flatness passes the injectivity mod $\mathfrak{m}$ to the kernel.

The geometric meaning is continuity of fibres. Let $\pi: X = \operatorname{Spec} B \to T = \operatorname{Spec} A$ be a morphism of affine varieties with $B$ finite over $A$. If $B$ is flat over $A$, then $B_\mathfrak{p}$ is free over the local ring $A_\mathfrak{p}$ (Chapter 2 and the theorem above), so the fibre ring $B \otimes \kappa(t)$ has the same dimension over $\kappa(t)$ at every point $t$ when $T$ is connected. Fibres move in a family without jumps. For a family over a smooth curve, Section 2.4 will show that flatness means that no associated prime of $B$ lies over a closed point. In words: no component, and no embedded component, of $X$ sits inside a single fibre.

### Examples

**Example P1.1.54 (a conic degenerating to a node).** Let $A = k[t]$ and $B = k[x, y, t]/(xy - t) \cong k[x, y]$, with $t \mapsto xy$. The ring $B$ is a domain and $t$ maps to $xy \neq 0$, so a nonzero $g(t)$ maps to $g(xy) \neq 0$ and multiplication by it on $B$ is injective. So $B$ is torsion free over the principal ideal domain $k[t]$, hence flat. The fibre over $t = a$ is the curve $xy = a$. For $a \neq 0$ it is a smooth conic; for $a = 0$ it is two lines crossing at a node. This is the simplest flat degeneration of a smooth curve to a nodal curve, and stable reduction in Volume 13 is built from such families.

**Example P1.1.55 (a fibre that jumps).** Let $A = k[x]$ and $B = k[x, y]/(xy)$. The class of $y$ is nonzero in $B$ and $x \cdot y = 0$. So $B$ has $x$-torsion and is not flat over $k[x]$. The fibre over $x = a \neq 0$ is $k[y]/(ay) = k$, one point. The fibre over $x = 0$ is $k[y]$, a whole line. The line $x = 0$ is a component of $\operatorname{Spec} B$ that lies in one fibre, and this is the failure of flatness in geometric form.

**Example P1.1.56 (the blow-up is not flat).** Let $A = k[x, y]$ and $B = k[x, u]$ with $y \mapsto xu$, the chart of the blow-up of the origin from Section 1.3, Exercise 5. Take $I = (x)$ and $J = (y)$. Then $I \cap J = (xy)$, so $(I \cap J)B = x^2u B$. On the other side $IB = xB$ and $JB = xuB \subseteq xB$, so $IB \cap JB = xuB$. Since $xu \notin x^2uB$, the intersection formula fails, and $B$ is not flat over $A$. The fibre over the origin is the line $x = 0$ of the $(x, u)$ plane, the exceptional curve, while the fibres over the other points are single points or empty.

**Example P1.1.57 (localization).** For a multiplicative set $S$, the ring $S^{-1}A$ is flat over $A$, by the exactness of localization in Section 2.1. The map $A \to A_f$ is faithfully flat only if $D(f) = \operatorname{Spec} A$: if $f \in \mathfrak{m}$ for a maximal ideal $\mathfrak{m}$, then $\mathfrak{m}A_f = A_f$. The map $A \to A[x]$ is faithfully flat, since $A[x]$ is free and $A[x]/\mathfrak{m}A[x] = (A/\mathfrak{m})[x] \neq 0$.

### Exercises

1. (A) Show that $\mathbb{Z}[x]$ and $\mathbb{Z}[1/2]$ are flat $\mathbb{Z}$-modules and that $\mathbb{Z}[x]/(2x)$ is not.
2. (A) Let $A \to B$ be flat and $N$ a flat $B$-module. Show that $N$ is flat over $A$. Show that if $M$ is a flat $A$-module then $B \otimes_A M$ is a flat $B$-module.
3. (B) Let $A = k[t]$ and $B = k[x, y, t]/(y^2 - x^3 - t)$. Show that $B$ is flat over $A$ and describe the fibres. Which fibre is singular?
4. (B) Let $(A, \mathfrak{m})$ be a local domain that is not a field. Show that the residue field $A/\mathfrak{m}$ is not a flat $A$-module.
5. (B) Let $N$ be flat and $u: M \to M'$ a linear map. Show that $\ker(u) \otimes N \cong \ker(u \otimes 1)$ and $\operatorname{coker}(u) \otimes N \cong \operatorname{coker}(u \otimes 1)$.
6. (C) Let $A \to B$ be faithfully flat. Show that a sequence of $A$-modules is exact if it becomes exact after tensoring with $B$, and that $A \to B$ is injective. Deduce that for an ideal $I$ of $A$, $IB \cap A = I$.

### Lean

Mathlib defines `Module.Flat` and proves `Module.Flat.of_free`, `Module.Flat.of_projective` and `Module.Flat.directSum_iff`. The ideal criterion is `Module.Flat.iff_rTensor_injective'`, proved there with character modules rather than Tor. The torsion criterion is `Module.Flat.flat_iff_torsion_eq_bot_of_isBezout`, and for Dedekind domains `IsDedekindDomain.flat_iff_torsion_eq_bot`. The local theorem is `Module.free_of_flat_of_isLocalRing`, in the general finitely generated form. Faithful flatness is `Module.FaithfullyFlat`, with the test `Module.FaithfullyFlat.iff_flat_and_proper_ideal`. The handbook adds no `MinimalModel` node here.

### Notes and history

Serre introduced flatness in his paper on algebraic and analytic geometry (GAGA, 1956), where he proved that the analytic local ring of a variety is flat over the algebraic one. Grothendieck made flatness the basic notion of the theory of families in EGA IV, and Mumford called it a riddle that comes out of algebra but is technically the answer to many prayers. The literature state of every result here is theorem. The section follows Matsumura, Chapter 3, and Eisenbud, Chapter 6. Volume 13 uses flatness in the definition of a family of stable varieties, and P3 proves the constancy of the Hilbert polynomial in flat projective families.
