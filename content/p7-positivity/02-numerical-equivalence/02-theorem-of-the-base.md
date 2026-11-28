---
title: The theorem of the base
nodes: []
sources: [Laz04, Kle66, SGA6, Ser56, Deb01]
reads_with: [Laz04:1.1.C, Deb01:ch1]
requires: [P2.5, P2.7, P3.9, P5.4, P5.5, P5.12, P7.1]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The theorem of the base

### Statement

Let $X$ be a projective scheme over the algebraically closed field $k$, with $N^1(X)$ and $N_1(X)$ as in Definitions P7.2.3 and P7.2.4.

**Theorem P7.2.12 (theorem of the base).** $N^1(X)$ is finite-dimensional. Consequently $N^1(X)_\mathbb{Z}$ is a free abelian group of finite rank $\rho$, the map $N^1(X)_\mathbb{Z} \otimes \mathbb{R} \to N^1(X)$ is an isomorphism, $N_1(X)$ has dimension $\rho$, the pairing of Proposition P7.2.5 is perfect, and $N^1(X)_\mathbb{Z}$ and $N_1(X)_\mathbb{Z}$ are lattices of rank $\rho$ in $N^1(X)$ and $N_1(X)$.

Lean: not in Lean as stated; the field `finiteDim` of `MinimalModel.IntersectionData` assumes the finite dimension of $N_1(X)$.

**Lemma P7.2.13 (finite dimension gives a lattice).** Suppose $\dim N^1(X) = \rho < \infty$. Then there are curves $C_1, \dots, C_\rho$ on $X$ whose classes form a basis of $N_1(X)$, and for any such curves the map
$$N^1(X)_\mathbb{Z} \to \mathbb{Z}^\rho, \qquad [L] \mapsto \bigl( (L \cdot C_1), \dots, (L \cdot C_\rho) \bigr)$$
is injective. In particular $N^1(X)_\mathbb{Z}$ is free of finite rank, and all the conclusions of Theorem P7.2.12 hold.

Lean: not in Lean as stated.

**Proposition P7.2.14 (the theorem of the base over $\mathbb{C}$).** Let $k = \mathbb{C}$ and let $X^{\mathrm{an}}$ be the complex analytic space of $X$, with the first Chern class $c_1 \colon \operatorname{Pic}(X) \to H^2(X^{\mathrm{an}}, \mathbb{Z})$ of the exponential sequence. If $c_1(L) = 0$, then $L \equiv 0$. Consequently $N^1(X)_\mathbb{Z}$ is a quotient of the image of $c_1$, which is finitely generated, and $\rho(X) \leq \operatorname{rank} H^2(X^{\mathrm{an}}, \mathbb{Z}) = b_2(X^{\mathrm{an}})$.

Lean: not in Lean as stated.

**Definition P7.2.15 (Picard number).** The *Picard number* of $X$ is $\rho(X) = \dim_\mathbb{R} N^1(X) = \dim_\mathbb{R} N_1(X)$. The space $N^1(X)$ carries the Euclidean topology of a finite-dimensional real vector space, and $N^1(X)_\mathbb{Q} = N^1(X)_\mathbb{Z} \otimes \mathbb{Q}$ is a dense $\mathbb{Q}$-subspace, the space of *rational classes*.

**Corollary P7.2.16 (morphisms and subschemes).**

1. If $f \colon Y \to X$ is a surjective morphism of projective schemes, then $\rho(Y) \geq \rho(X)$.
2. If $Z \subseteq X$ is a closed subscheme with inclusion $i$, then $i_* \colon N_1(Z) \to N_1(X)$ has image the span of the classes of the curves contained in $Z$, and $i^* \colon N^1(X) \to N^1(Z)$ is its transpose.
3. A class $\xi \in N^1(X)$ is rational if and only if $\xi \cdot [C] \in \mathbb{Q}$ for every curve $C$. The classes of $\mathbb{Q}$-divisors are the rational classes.

Lean: not in Lean as stated.

### Proof in words

The two spaces are quotients of huge vector spaces by the kernels of a pairing, and nothing in the definitions bounds their dimension. Over $\mathbb{C}$ topology does. A line bundle has a first Chern class in $H^2(X^{\mathrm{an}}, \mathbb{Z})$, a finitely generated group because $X^{\mathrm{an}}$ is a compact triangulable space. The degree of a line bundle on a curve is the value of its first Chern class on the fundamental class of the normalized curve. So numerical classes are determined by Chern classes, and $\rho(X)$ is at most the second Betti number.

In positive characteristic there is no such topology, and the proof uses the Picard scheme instead: the line bundles algebraically equivalent to $0$ form the points of a connected group scheme, and the quotient, the Néron-Severi group, is finitely generated. This needs the machinery of Grothendieck's construction and is cited, not proved.

Once the dimension is finite, the integral structure is automatic. Finitely many curves give a basis of $N_1(X)$, and the intersection numbers with these curves embed $N^1(X)_\mathbb{Z}$ in $\mathbb{Z}^\rho$.

### Examples

**Example P7.2.17 (curves over $\mathbb{C}$).** Let $C$ be a smooth projective curve of genus $g$ over $\mathbb{C}$. Then $C^{\mathrm{an}}$ is a compact Riemann surface, $H^2(C^{\mathrm{an}}, \mathbb{Z}) = \mathbb{Z}$, and by Example P2.7.32 the kernel of $c_1$ is the torus $\operatorname{Pic}^0(C) = H^1(C, \mathcal{O}_C) / H^1(C, \mathbb{Z})$ of dimension $g$. Here $c_1$ is the degree, so the image of $c_1$ is $\mathbb{Z}$, which equals $N^1(C)_\mathbb{Z}$ by Example P7.2.9. The bound $\rho \leq b_2$ is an equality.

**Example P7.2.18 (projective space).** For $X = \mathbb{P}^n_\mathbb{C}$, $H^2(X^{\mathrm{an}}, \mathbb{Z}) = \mathbb{Z}$, so $\rho(\mathbb{P}^n) \leq 1$, and $\rho = 1$ because $\mathcal{O}(1)$ has degree $1$ on a line. Proposition P7.2.21 proves $N^1(\mathbb{P}^n)_\mathbb{Z} = \mathbb{Z}$ over any $k$ without topology.

**Example P7.2.19 (the product of an elliptic curve with itself).** Let $E$ be an elliptic curve over $\mathbb{C}$ and $S = E \times E$. By Example P5.12.9 the two fibres $f_1$, $f_2$ and the diagonal $\Delta$ have Gram matrix of determinant $2$, so their classes are linearly independent and $\rho(S) \geq 3$. The space $S^{\mathrm{an}}$ is a real $4$-dimensional torus, so $b_2(S^{\mathrm{an}}) = \binom{4}{2} = 6$ and $\rho(S) \leq 6$. Hodge theory sharpens this to $\rho(S) \leq h^{1,1}(S) = 4$, and $\rho(S) = 4$ exactly when $E$ has complex multiplication, the extra class being the graph of a complex multiplication (Lazarsfeld, Section 1.5.B). In particular $\rho$ is not a topological invariant: it jumps on a countable dense set of $j$-invariants, while $b_2$ is constant.

**Example P7.2.20 (the kernel of the class map).** On $S = E \times E$ the line bundles $p_1^* M$ with $M \in \operatorname{Pic}^0(E)$ are numerically trivial: $(p_1^* M \cdot C) = (M \cdot p_{1*} C) = 0$ for every curve $C$ by part 2 of Proposition P7.2.7, as $N^1(E)_\mathbb{Z} = \mathbb{Z}$ by the degree. So $\operatorname{Pic}^\tau(S)$ contains $p_1^* \operatorname{Pic}^0(E) \oplus p_2^* \operatorname{Pic}^0(E)$, an uncountable group over $\mathbb{C}$, while $N^1(S)_\mathbb{Z} \cong \mathbb{Z}^\rho$. The theorem of the base is a statement about the quotient only.

### Proof

*Lemma P7.2.13.* The classes of curves span $N_1(X)$, which has dimension $\rho$ by part 3 of Proposition P7.2.5. So some $\rho$ of them, $[C_1], \dots, [C_\rho]$, form a basis. If $(L \cdot C_i) = 0$ for all $i$, then $1 \otimes L$ pairs to zero with a basis of $N_1(X)$, so it is zero in $N^1(X)$ by part 1 of Proposition P7.2.5, and $[L] = 0$ by part 2. So $N^1(X)_\mathbb{Z}$ embeds in $\mathbb{Z}^\rho$ and is free of rank at most $\rho$.

The map $N^1(X)_\mathbb{Z} \otimes \mathbb{R} \to N^1(X)$ is surjective by part 2 of Proposition P7.2.5. For injectivity, let $L_1, \dots, L_s$ be a basis of $N^1(X)_\mathbb{Z}$ and consider the integer matrix $A = ((L_i \cdot C_j))$, of size $s \times \rho$. Its rows are linearly independent over $\mathbb{Z}$, by the injectivity just proved, hence over $\mathbb{Q}$, so $A$ has rank $s$ over $\mathbb{Q}$. The rank of a rational matrix is the size of its largest nonzero minor, which is the same over $\mathbb{R}$. So the rows are linearly independent over $\mathbb{R}$: a combination $\sum a_i L_i$ with real $a_i$ that is zero in $N^1(X)$ pairs to zero with every $C_j$, so all $a_i = 0$. Hence $N^1(X)_\mathbb{Z} \otimes \mathbb{R} \cong N^1(X)$ and $s = \rho$. In the basis dual to $[C_1], \dots, [C_\rho]$ the group $N^1(X)_\mathbb{Z}$ is a subgroup of $\mathbb{Z}^\rho$ of rank $\rho$, so it is a lattice. The group $N_1(X)_\mathbb{Z}$ contains $\mathbb{Z}[C_1] \oplus \dots \oplus \mathbb{Z}[C_\rho]$ and pairs integrally with the basis $L_1, \dots, L_\rho$ of $N^1(X)$, so it lies in the dual lattice of $N^1(X)_\mathbb{Z}$; it is a lattice too. $\square$

*Proposition P7.2.14.* The proof uses three facts of complex geometry, which this handbook does not prove; Lazarsfeld, Section 1.1.C, proves the proposition in the same way. First, $X^{\mathrm{an}}$ is a compact Hausdorff space that admits a finite triangulation (Łojasiewicz), so its cohomology groups are finitely generated. Second, the exponential sequence $0 \to \mathbb{Z} \to \mathcal{O}_{X^{\mathrm{an}}} \to \mathcal{O}_{X^{\mathrm{an}}}^\times \to 0$ is exact on any complex analytic space, as in Example P2.5.24, and its boundary map is a homomorphism $c_1 \colon \operatorname{Pic}(X^{\mathrm{an}}) \to H^2(X^{\mathrm{an}}, \mathbb{Z})$ by Theorem P2.7.28; composed with analytification $\operatorname{Pic}(X) \to \operatorname{Pic}(X^{\mathrm{an}})$ it is natural for morphisms. Third, on a smooth projective curve $\tilde C$, $c_1(M)$ is $\deg M$ times the positive generator of $H^2(\tilde C^{\mathrm{an}}, \mathbb{Z}) \cong \mathbb{Z}$; by GAGA (Ser56) it suffices to check this for $M = \mathcal{O}(x)$ with $x$ a point, where it is a local computation.

Let $C$ be a curve on $X$, $\nu \colon \tilde C \to C$ its normalization and $j \colon \tilde C \to X$ the composite. By part 2 of Proposition P7.1.7, $(L \cdot C) = \deg \nu^* (L|_C) = \deg j^* L$. By the second and third facts, $\deg j^* L$ is the image of $c_1(j^* L) = j^* c_1(L)$ in $H^2(\tilde C^{\mathrm{an}}, \mathbb{Z}) = \mathbb{Z}$. So $c_1(L) = 0$ implies $(L \cdot C) = 0$ for every curve, that is, $L \equiv 0$. Hence $\operatorname{Pic}(X) \to N^1(X)_\mathbb{Z}$ factors through the image of $c_1$, a subgroup of the finitely generated group $H^2(X^{\mathrm{an}}, \mathbb{Z})$, so it is finitely generated. Its rank is at most $b_2(X^{\mathrm{an}})$. A finitely generated group spans a real vector space of dimension at most its rank, so $\rho(X) \leq b_2(X^{\mathrm{an}})$. $\square$

*Theorem P7.2.12.* By Lemma P7.2.13 it suffices to prove $\dim N^1(X) < \infty$. Over $\mathbb{C}$ this is Proposition P7.2.14. Over an arbitrary algebraically closed field the theorem is due to Néron and Severi for smooth varieties and to Kleiman in general; see Kleiman, *Toward a numerical theory of ampleness* (Kle66), Kleiman's Exposé XIII of SGA 6 (SGA6), and Lazarsfeld, Remark 1.1.19 (Laz04). The proof there shows that the group of line bundles algebraically equivalent to $0$ has finite index in $\operatorname{Pic}^\tau(X)$ and that the Néron-Severi group $\operatorname{Pic}(X) / \operatorname{Pic}^0(X)$ is finitely generated; numerical classes are its quotient by torsion. This handbook cites the theorem in that generality. $\square$

*Corollary P7.2.16.* Part 1 is part 3 of Proposition P7.2.7. Part 2: by definition $i_*[C] = [C]$ for a curve $C \subseteq Z$, and $i^* \xi \cdot \gamma = \xi \cdot i_* \gamma$ is the projection formula of part 2 of Proposition P7.2.7. Part 3. A rational class pairs rationally with curves. Conversely, choose $C_1, \dots, C_\rho$ and a basis $L_1, \dots, L_\rho$ of $N^1(X)_\mathbb{Z}$ as in Lemma P7.2.13, with invertible rational matrix $A = ((L_i \cdot C_j))$. A class $\xi = \sum_i a_i [L_i]$ with all $\xi \cdot [C_j]$ rational has $(a_1, \dots, a_\rho) A \in \mathbb{Q}^\rho$, so all $a_i \in \mathbb{Q}$. The density of $N^1(X)_\mathbb{Q}$ holds because it contains a basis. $\square$

### Exercises

1. (A) Let $X$ be a projective variety over $\mathbb{C}$ with $H^2(X^{\mathrm{an}}, \mathbb{Z}) \cong \mathbb{Z}$. Show that $\rho(X) = 1$ and that every line bundle is numerically equivalent to a rational multiple of an ample one.
2. (A) Compute $b_2$ and the bound of Proposition P7.2.14 for $\mathbb{P}^1 \times \mathbb{P}^1$, and compare with $\rho = 2$.
3. (B) Show that $N^1(X)_\mathbb{Z}$ and $N_1(X)_\mathbb{Z}$ need not be dual lattices: on the elliptic surface $E \times E$ with $E$ without complex multiplication, compute the index of $N_1(S)_\mathbb{Z}$, identified with $N^1(S)_\mathbb{Z}$ by Proposition P7.2.8, in its dual lattice, using the Gram matrix of Example P5.12.9 and assuming that $f_1$, $f_2$, $\Delta$ form a basis of $N^1(S)_\mathbb{Z}$.
4. (B) Let $f \colon Y \to X$ be a surjective morphism of projective varieties with connected fibres and $\rho(Y) = \rho(X)$. Show that $f^* \colon N^1(X) \to N^1(Y)$ is an isomorphism and that $f$ contracts no curve, and deduce from Corollary P4.6.17 that $f$ is finite.
5. (B) Prove part 3 of Corollary P7.2.16 directly for $X = \mathbb{P}^1 \times \mathbb{P}^1$, and show that a class with irrational ratio of its two coordinates is not the class of any $\mathbb{Q}$-divisor.
6. (C) Let $E$ be an elliptic curve over $\overline{\mathbb{F}}_p$. Show that $\operatorname{Pic}^\tau(E)$ is an infinite torsion group, so not finitely generated, and that the subgroup $p_1^* \operatorname{Pic}^0(E) \oplus p_2^* \operatorname{Pic}^0(E)$ of $\operatorname{Pic}^\tau(E \times E)$ of Example P7.2.20 is torsion as well, using Example P7.2.10. Why is the sum direct?

### Lean

Mathlib has no Picard scheme, no Néron-Severi group and no theorem of the base. The project library makes the finite dimension an assumption: the structure `MinimalModel.IntersectionData` has a field `finiteDim` saying that the span of the curve classes, `MinimalModel.IntersectionData.N₁`, is finite-dimensional over $\mathbb{R}$. Every statement of the library that uses intersection numbers takes such a structure as input, so Theorem P7.2.12 is a hypothesis there, not a theorem. The handbook adds no `MinimalModel` node here.

### Notes and history

The finite generation of the group of divisors modulo algebraic equivalence on a complex surface is Severi's theorem of the base, and Néron proved it over an arbitrary algebraically closed field in 1952. Kleiman's Exposé XIII of SGA 6 gives the finiteness theorems for the Picard functor of Grothendieck, among them the finite generation of numerical classes on any proper scheme. The literature state is theorem. The complex proof through $c_1$ is in Lazarsfeld, Section 1.1.C, and it shows $\rho \leq b_2$. Lefschetz's theorem on $(1,1)$ classes identifies the image of $c_1$ for a smooth projective complex variety with the integral classes of Hodge type $(1,1)$, which gives the sharper bound $\rho \leq h^{1,1}$ used in Example P7.2.19; this is a statement of P6. The numbering of the remarks in Lazarsfeld, Section 1.1.C, should be checked against the edition used.
