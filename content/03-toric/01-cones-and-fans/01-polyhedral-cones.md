---
title: Polyhedral cones, duality and faces
nodes: []
sources: [CLS11, Ful93, Oda88]
reads_with: [CLS11:ch1, Ful93:1.2, Oda88:A.1]
requires: [P8.6]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Polyhedral cones, duality and faces

### Statement

Fix a lattice $N \cong \mathbb{Z}^n$ and its dual lattice $M = \operatorname{Hom}_{\mathbb{Z}}(N, \mathbb{Z})$. Write $\langle m, u \rangle$ for the pairing of $m \in M$ and $u \in N$. Put $N_{\mathbb{R}} = N \otimes_{\mathbb{Z}} \mathbb{R}$ and $M_{\mathbb{R}} = M \otimes_{\mathbb{Z}} \mathbb{R}$. The pairing extends to a perfect pairing $M_{\mathbb{R}} \times N_{\mathbb{R}} \to \mathbb{R}$. In Chapter 2, $N$ becomes the lattice of one-parameter subgroups of a torus and $M$ its lattice of characters. Throughout the volume, $e_1, \dots, e_n$ is the standard basis of $N = \mathbb{Z}^n$ and $e_1^*, \dots, e_n^*$ the dual basis of $M$.

**Definition 3.1.1.** A *convex polyhedral cone* in $N_{\mathbb{R}}$ is a set $\sigma = \operatorname{Cone}(S) = \{\sum_{u \in S} \lambda_u u : \lambda_u \ge 0\}$ for a finite set $S \subset N_{\mathbb{R}}$, with $\operatorname{Cone}(\emptyset) = \{0\}$. It is *rational* if $S$ can be taken in $N$. Its *dimension* $\dim \sigma$ is the dimension of the linear span of $\sigma$. It is *strongly convex* if $\sigma \cap (-\sigma) = \{0\}$. Its *dual cone* is $\sigma^\vee = \{m \in M_{\mathbb{R}} : \langle m, u \rangle \ge 0 \text{ for all } u \in \sigma\}$, and $\sigma^\perp = \{m \in M_{\mathbb{R}} : \langle m, u \rangle = 0 \text{ for all } u \in \sigma\}$.

Lean: `MinimalModel.Toric.latticeCone` (the cone of a finite set of lattice points), `MinimalModel.Toric.IsRationalPolyhedral` and `MinimalModel.Toric.IsStronglyConvex`. The dual cone is not yet in Lean.

**Definition 3.1.2.** Let $\sigma$ be a convex polyhedral cone. A *face* of $\sigma$ is a set $\tau = \sigma \cap m^\perp$ with $m \in \sigma^\vee$. Write $\tau \preceq \sigma$. The cone $\sigma$ is a face of itself ($m = 0$). A face of dimension $\dim \sigma - 1$ is a *facet*, and a face of dimension 1 is an *edge*. The *relative interior* $\operatorname{relint} \sigma$ is the interior of $\sigma$ in its linear span.

Lean: `MinimalModel.Toric.IsFace` (a face cut out by a linear form, as here). The fans of the Lean library use the faces of Mathlib, `PointedCone.IsFaceOf`, and `MinimalModel.Toric.IsFace.isFaceOf` proves that a face in the sense of this definition is one of them.

**Theorem 3.1.3 (duality).** Let $\sigma \subset N_{\mathbb{R}}$ be a convex polyhedral cone.

1. $\sigma^\vee$ is a convex polyhedral cone in $M_{\mathbb{R}}$. If $\sigma$ is rational, so is $\sigma^\vee$.
2. $(\sigma^\vee)^\vee = \sigma$.
3. $\sigma$ is strongly convex if and only if $\dim \sigma^\vee = n$.

Lean: not yet in Lean.

**Proposition 3.1.4 (faces).** Let $\sigma = \operatorname{Cone}(S)$ be a convex polyhedral cone.

1. If $\tau = \sigma \cap m^\perp$ is a face, then $\tau = \operatorname{Cone}(S \cap m^\perp)$. So every face is a convex polyhedral cone, rational if $\sigma$ is, and $\sigma$ has finitely many faces.
2. The intersection of two faces of $\sigma$ is a face of $\sigma$.
3. A face of a face of $\sigma$ is a face of $\sigma$.
4. If $\sigma$ is strongly convex, then $\{0\}$ is a face of $\sigma$.
5. The map $\tau \mapsto \tau^* = \sigma^\vee \cap \tau^\perp$ is a bijection from the faces of $\sigma$ to the faces of $\sigma^\vee$. It reverses inclusions, and $\dim \tau + \dim \tau^* = n$.

Lean: parts 1 and 4 are `MinimalModel.Toric.exists_subset_of_isFaceOf_latticeCone`, `MinimalModel.Toric.IsRationalPolyhedral.of_isFaceOf`, `MinimalModel.Toric.finite_setOf_isFaceOf_hull` and `MinimalModel.Toric.bot_isFaceOf`, for the faces of Mathlib. Parts 2, 3 and 5 are not yet in Lean in this form.

### Proof in words

A cone is given in two ways: by generators, as in the definition, and by inequalities, as the set where finitely many linear forms are nonnegative. The theorem of Minkowski and Weyl says that the two descriptions give the same class of sets. The inequalities of $\sigma$ are the generators of $\sigma^\vee$, so duality exchanges the two descriptions, and this is the content of Theorem 3.1.3. The difficulty is in part 2, which needs a separating hyperplane: a point outside a closed convex cone is separated from it by a linear form. This is Farkas' lemma, and the handbook cites it.

The statements on faces are elementary once the generators are fixed. A linear form that is nonnegative on $\sigma$ vanishes at a positive combination of generators only if it vanishes at each generator that appears. So the face is spanned by the generators on the hyperplane. Sums of linear forms give intersections of faces, and a small change of the form gives faces of faces. The face correspondence of part 5 says that the faces of a cone and of its dual form two lattices that are opposite to each other.

### Examples

**Example 3.1.5 (the orthant).** Let $\sigma = \operatorname{Cone}(e_1, \dots, e_n) \subset \mathbb{R}^n$. Then $\sigma^\vee = \operatorname{Cone}(e_1^*, \dots, e_n^*)$. For a subset $I \subseteq \{1, \dots, n\}$, put $m_I = \sum_{i \notin I} e_i^*$. Then $\sigma \cap m_I^\perp = \operatorname{Cone}(e_i : i \in I)$, and every face has this form by part 1 of Proposition 3.1.4. So $\sigma$ has $2^n$ faces. The dual face of $\operatorname{Cone}(e_i : i \in I)$ is $\operatorname{Cone}(e_j^* : j \notin I)$, of dimension $n - |I|$, as part 5 says. This cone is `MinimalModel.Toric.orthant` in Lean.

**Example 3.1.6 (the cone of $\frac1n(1,1)$).** Let $n \ge 1$ and $\sigma_n = \operatorname{Cone}(e_2, n e_1 - e_2) \subset \mathbb{R}^2$. A form $m = a e_1^* + b e_2^*$ is in $\sigma_n^\vee$ if and only if $b \ge 0$ and $na - b \ge 0$. The two boundary lines are $b = 0$ and $b = na$, so

$$\sigma_n^\vee = \operatorname{Cone}(e_1^*, e_1^* + n e_2^*).$$

The faces of $\sigma_n$ are $\{0\}$, the two edges and $\sigma_n$. The edge $\operatorname{Cone}(e_2)$ is $\sigma_n \cap (e_1^*)^\perp$, and its dual face is $\sigma_n^\vee \cap e_2^\perp = \operatorname{Cone}(e_1^*)$. Chapter 2 shows that this cone gives the cone over the rational normal curve of degree $n$. For $n = 2$ it is the quadric cone of P0 Chapter 6.

**Example 3.1.7 (the cone over a square).** In $\mathbb{R}^3$ let $u_1 = (0,0,1)$, $u_2 = (1,0,1)$, $u_3 = (1,1,1)$, $u_4 = (0,1,1)$, and $\sigma = \operatorname{Cone}(u_1, u_2, u_3, u_4)$. It is the cone over the unit square at height 1. The four facets are spanned by consecutive pairs. The facet $\operatorname{Cone}(u_1, u_2)$ lies on $y = 0$ and the form $e_2^*$ is positive on $u_3, u_4$. In the same way one finds the inner normals of all four facets:

$$\sigma^\vee = \operatorname{Cone}\big((1,0,0), (0,1,0), (-1,0,1), (0,-1,1)\big).$$

The cone $\sigma$ has 10 faces: $\{0\}$, four edges, four facets and $\sigma$. The generators satisfy $u_1 + u_3 = u_2 + u_4$, so $\sigma$ is not simplicial in the sense of Section 3. The four generators of $\sigma^\vee$ satisfy the same kind of relation: $(1,0,0) + (-1,0,1) = (0,1,0) + (0,-1,1)$.

**Example 3.1.8 (hypotheses that fail).** The half-plane $H = \{x_2 \ge 0\} = \operatorname{Cone}(e_1, -e_1, e_2)$ is polyhedral but not strongly convex. Its dual is the ray $\operatorname{Cone}(e_2^*)$, of dimension $1 < 2$, as part 3 of Theorem 3.1.3 predicts. Its faces are $H$ and the line $\mathbb{R} e_1$, so $\{0\}$ is not a face, and part 4 of Proposition 3.1.4 fails. The round cone $C = \{x_1^2 + x_2^2 \le x_3^2, x_3 \ge 0\}$ is closed and convex but not polyhedral. Each ray on its boundary is a face, so $C$ has infinitely many faces, and part 1 fails.

### Proof

*Proof of Proposition 3.1.4.* For part 1, let $v = \sum_{u \in S} \lambda_u u$ be in $\tau$, with all $\lambda_u \ge 0$. Each term $\lambda_u \langle m, u \rangle$ of $0 = \langle m, v \rangle$ is nonnegative, so $\lambda_u = 0$ when $\langle m, u \rangle > 0$. Thus $v \in \operatorname{Cone}(S \cap m^\perp)$, and the other inclusion is clear. A finite set $S$ has finitely many subsets. For part 2, let $\tau_i = \sigma \cap m_i^\perp$ with $m_i \in \sigma^\vee$. Then $m_1 + m_2 \in \sigma^\vee$, and on $\sigma$ the sum vanishes exactly where both terms vanish, because both are nonnegative. So $\tau_1 \cap \tau_2 = \sigma \cap (m_1 + m_2)^\perp$.

For part 3, let $\tau = \sigma \cap m^\perp$ and $\gamma = \tau \cap m'^\perp$ with $m' \in \tau^\vee$. Take $p > 0$ so large that $\langle m' + p m, u \rangle > 0$ for each $u \in S$ with $\langle m, u \rangle > 0$. For $u \in S$ with $\langle m, u \rangle = 0$ the vector $u$ lies in $\tau$, so $\langle m' + pm, u \rangle = \langle m', u \rangle \ge 0$. So $m' + pm \in \sigma^\vee$. By the argument of part 1, $\sigma \cap (m' + pm)^\perp$ is spanned by the $u \in S$ with $\langle m, u \rangle = \langle m', u \rangle = 0$, and this is $\gamma$ by part 1 applied twice.

For part 4, $\dim \sigma^\vee = n$ by Theorem 3.1.3, so $\sigma^\vee$ has an interior point $m$. Let $u \in \sigma$ with $\langle m, u \rangle = 0$. If $u \neq 0$, pick $m''$ with $\langle m'', u \rangle > 0$. For small $\varepsilon > 0$ the form $m - \varepsilon m''$ is still in $\sigma^\vee$, but it is negative at $u$. This is a contradiction, so $\sigma \cap m^\perp = \{0\}$. Part 5 uses Theorem 3.1.3 in both directions. The handbook cites it from Cox-Little-Schenck, Chapter 1, and Fulton, Section 1.2. $\square$

*Proof of Theorem 3.1.3.* This is cited without proof. Part 2 is Farkas' lemma: if $u_0 \notin \sigma$, the separation theorem for the closed convex set $\sigma$ gives $m$ with $\langle m, u_0 \rangle < 0 \le \langle m, \sigma \rangle$, so $u_0 \notin (\sigma^\vee)^\vee$. Part 1 is the theorem of Minkowski and Weyl, which says that a set is a finitely generated cone if and only if it is a finite intersection of closed half-spaces through $0$. The rational case follows because the facets of a rational cone are cut out by rational forms. For part 3, $\sigma^\vee$ lies in the subspace $(\sigma \cap (-\sigma))^\perp$, so $\dim \sigma^\vee = n$ forces $\sigma \cap (-\sigma) = 0$. Conversely, if $\dim \sigma^\vee < n$ there is $u \neq 0$ with $\langle \sigma^\vee, u \rangle = 0$, and part 2 puts both $u$ and $-u$ in $\sigma$. See Cox-Little-Schenck, Chapter 1, and Fulton, Section 1.2. $\square$

### Exercises

1. (A) Find the dual cone and all faces of $\operatorname{Cone}(e_1, e_1 + e_2) \subset \mathbb{R}^2$. Check part 5 of Proposition 3.1.4 for each face.
2. (A) Show that $\sigma^\perp$ is the largest linear subspace of $M_{\mathbb{R}}$ contained in $\sigma^\vee$. Deduce that $\sigma^\vee$ is strongly convex if and only if $\dim \sigma = n$.
3. (A) Let $\sigma$ be a convex polyhedral cone and $u \in \operatorname{relint} \sigma$. Show that the only face of $\sigma$ that contains $u$ is $\sigma$.
4. (B) Show that every proper face of $\sigma$ is the intersection of the facets that contain it. (Hint: use part 5 of Proposition 3.1.4 and the fact that a cone is spanned by its edges when it is strongly convex.)
5. (B) Compute the dual of the cone $\operatorname{Cone}(e_1, e_2, e_3, e_1 + e_2 - e_3) \subset \mathbb{R}^3$, and list its faces. Is it the cone over a square in another basis of $\mathbb{Z}^3$?
6. (B) Let $\tau$ be a face of $\sigma$. Show that $\tau^\vee = \sigma^\vee + \mathbb{R}_{\ge 0}(-m)$ for any $m \in \sigma^\vee$ with $\tau = \sigma \cap m^\perp$. Chapter 2 uses this in the form $S_\tau = S_\sigma + \mathbb{Z}_{\ge 0}(-m)$.

### Lean

The Lean library works in $N_{\mathbb{R}} = \mathbb{R}^n$ with the lattice $\mathbb{Z}^n$, through `MinimalModel.Toric.NR` and `MinimalModel.Toric.toNR`. A rational polyhedral cone is the $\mathbb{R}_{\ge 0}$-span of a finite set of lattice points, a Mathlib `PointedCone`:

```lean
noncomputable def latticeCone (S : Finset (Fin n → ℤ)) : PointedCone ℝ (NR n) :=
  Submodule.span (Nonneg ℝ) (toNR '' (S : Set (Fin n → ℤ)))
```

- Status: the definitions are in the project library. The proved results are part 1 of Proposition 3.1.4 (`MinimalModel.Toric.exists_subset_of_isFaceOf_latticeCone`, `MinimalModel.Toric.IsRationalPolyhedral.of_isFaceOf`, `MinimalModel.Toric.finite_setOf_isFaceOf_hull`) and part 4 (`MinimalModel.Toric.bot_isFaceOf`). Theorem 3.1.3 and part 5 of Proposition 3.1.4 are not yet in Lean.
- Fidelity: a face in Lean is a face in the sense of Mathlib, `PointedCone.IsFaceOf`: a subcone $\tau \subseteq \sigma$ such that $x, y \in \sigma$ and $x + ay \in \tau$ with $a > 0$ give $x, y \in \tau$. For polyhedral cones these are the faces of Definition 3.1.2. The Lean library proves one direction, `MinimalModel.Toric.IsFace.isFaceOf`. The other direction, that every face of a polyhedral cone is cut out by a linear form, is not yet in Lean.
- No node of the map covers this section. The section is background for the toric MMP node `MMAWP4SA44` of the later chapters.

### Notes and history

The two descriptions of a polyhedral cone are due to Minkowski (1896) and Weyl (1935), and Farkas proved his lemma in 1902. All statements of this section are theorems. The face correspondence is in every text on toric varieties; Cox-Little-Schenck, Chapter 1, is close to this section, and Oda's book has an appendix on convex geometry. Toric geometry uses only rational cones, but the duality theorem and the face statements hold for all polyhedral cones. The orthant, the cone $\sigma_n$ and the cone over a square come back in every chapter of this volume.
