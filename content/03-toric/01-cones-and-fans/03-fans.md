---
title: Fans and the separation lemma
nodes: []
sources: [CLS11, Ful93]
reads_with: [CLS11:ch3, CLS11:1.2, Ful93:1.4]
requires: [P8.6, 3.1]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Fans and the separation lemma

### Statement

From now on a *cone* means a strongly convex rational polyhedral cone in $N_{\mathbb{R}}$, unless the text says otherwise.

**Definition 3.1.17.** A *fan* in $N_{\mathbb{R}}$ is a finite set $\Sigma$ of cones such that

1. every face of a cone of $\Sigma$ is a cone of $\Sigma$, and
2. the intersection of two cones of $\Sigma$ is a face of each of them.

Lean: `MinimalModel.Toric.Fan`.

**Definition 3.1.18.** Let $\Sigma$ be a fan. Its *support* is $|\Sigma| = \bigcup_{\sigma \in \Sigma} \sigma$. The fan is *complete* if $|\Sigma| = N_{\mathbb{R}}$. Write $\Sigma(r)$ for the set of cones of dimension $r$. A cone of dimension 1 is a *ray*. A ray $\rho$ contains a unique primitive lattice point $u_\rho$, that is, a point of $\rho \cap N$ that is not a multiple $k u$ with $k \ge 2$ and $u \in N$. It is the *minimal generator* of $\rho$. For a cone $\sigma$, $\sigma(1)$ is the set of rays of $\sigma$, and $\sigma = \operatorname{Cone}(u_\rho : \rho \in \sigma(1))$.

Lean: `MinimalModel.Toric.Fan.support`, `MinimalModel.Toric.Fan.IsComplete`, `MinimalModel.Toric.IsRay` and `MinimalModel.Toric.Fan.rays` (the set $\Sigma(1)$). The minimal generator $u_\rho$ is `MinimalModel.Toric.rayGenerator`, on a fan `MinimalModel.Toric.Fan.generator`, and `MinimalModel.Toric.IsRay.isPrimitive_rayGenerator` says that it is primitive in the sense of `MinimalModel.Toric.IsPrimitive`.

**Definition 3.1.19.** A cone $\sigma$ is *smooth* if its minimal generators are part of a $\mathbb{Z}$-basis of $N$. It is *simplicial* if its minimal generators are linearly independent over $\mathbb{R}$. A fan is smooth, or simplicial, if all its cones are. For a simplicial cone $\sigma$ with $N_\sigma = \operatorname{span}(\sigma) \cap N$, the *multiplicity* is the index $\operatorname{mult}(\sigma) = [N_\sigma : \sum_{\rho \in \sigma(1)} \mathbb{Z} u_\rho]$. So a simplicial cone is smooth if and only if its multiplicity is 1.

Lean: `MinimalModel.Toric.IsSimplicial` and `MinimalModel.Toric.Fan.IsSimplicialFan`. Smooth cones and the multiplicity are not yet in Lean.

**Proposition 3.1.20.** Let $\Sigma$ be a nonempty fan. Then $\{0\} \in \Sigma$, and $\sigma \cap \sigma' \in \Sigma$ for all $\sigma, \sigma' \in \Sigma$. Each cone of $\Sigma$ is a face of a maximal cone of $\Sigma$, so $\Sigma$ is the set of faces of its maximal cones.

Lean: `MinimalModel.Toric.Fan.bot_mem` and `MinimalModel.Toric.Fan.inf_mem`.

**Lemma 3.1.21 (separation lemma).** Let $\sigma$ and $\sigma'$ be cones whose intersection $\tau = \sigma \cap \sigma'$ is a face of each. Then there is $m \in \sigma^\vee \cap (-\sigma')^\vee \cap M$ with

$$\tau = \sigma \cap m^\perp = \sigma' \cap m^\perp.$$

Lean: not yet in Lean.

The form $m$ is nonnegative on $\sigma$ and nonpositive on $\sigma'$. So the hyperplane $m^\perp$ separates the two cones, and it meets each of them exactly in $\tau$. In Chapter 2 this lemma makes the gluing of affine charts separated.

### Proof in words

Proposition 3.1.20 is a direct use of the axioms. The separation lemma looks at the cone $\gamma = \sigma - \sigma' = \sigma + (-\sigma')$. Its dual is $\sigma^\vee \cap (-\sigma')^\vee$, the forms that are nonnegative on $\sigma$ and nonpositive on $\sigma'$. A form in the relative interior of $\gamma^\vee$ vanishes only on the smallest face of $\gamma$, which is the largest linear subspace $\gamma \cap (-\gamma)$. A point $v$ of $\sigma$ on which this form vanishes is in $-\gamma$, so $-v = a - b$ with $a \in \sigma$ and $b \in \sigma'$. Then $v + a = b$ lies in $\sigma \cap \sigma' = \tau$, and since $\tau$ is a face of $\sigma$, the point $v$ lies in $\tau$. This is the only place where the axiom on intersections is used, and it is the reason for the axiom.

### Examples

**Example 3.1.22 (the fan of a cone and the fan of $\mathbb{A}^n$).** For a cone $\sigma$, the set of all faces of $\sigma$ is a fan, by Proposition 3.1.4. In Lean it is `MinimalModel.Toric.Fan.ofCone`. The fan of the faces of the orthant $\operatorname{Cone}(e_1, \dots, e_n)$ is the fan of $\mathbb{A}^n$, `MinimalModel.Toric.Fan.affine`. It is smooth, and its support is the orthant (`MinimalModel.Toric.Fan.support_affine`). The fan $\{\{0\}\}$ is the fan of the torus, `MinimalModel.Toric.Fan.trivial`. The fan of the faces of $\sigma_n$ (Example 3.1.6) is simplicial. Its maximal cone has multiplicity $|\det(e_2, n e_1 - e_2)| = n$, so it is smooth only for $n = 1$.

**Example 3.1.23 (the fan of $\mathbb{P}^1$).** In $N_{\mathbb{R}} = \mathbb{R}$ the fan $\{\{0\}, \mathbb{R}_{\ge 0}, \mathbb{R}_{\le 0}\}$ is complete and smooth. It has two rays, with minimal generators $1$ and $-1$. This is the Lean example `MinimalModel.Toric.P1.fan`, with `MinimalModel.Toric.P1.isComplete`, `MinimalModel.Toric.P1.isSimplicialFan` and `MinimalModel.Toric.P1.card_ray`.

**Example 3.1.24 (the fan of $\mathbb{P}^2$ and of $\mathbb{P}^n$).** In $\mathbb{R}^2$ let $u_0 = -e_1 - e_2$, $u_1 = e_1$, $u_2 = e_2$. The fan of $\mathbb{P}^2$ has the three maximal cones $\operatorname{Cone}(u_1, u_2)$, $\operatorname{Cone}(u_2, u_0)$, $\operatorname{Cone}(u_0, u_1)$, the three rays and $\{0\}$. Two maximal cones meet in a common ray, and the three cones cover the plane, so the fan is complete. Each pair of the $u_i$ is a basis of $\mathbb{Z}^2$, so the fan is smooth. For $\mathbb{P}^n$ put $u_0 = -e_1 - \dots - e_n$ and $u_i = e_i$, and take the cones spanned by proper subsets of $\{u_0, \dots, u_n\}$. The relation $u_0 + u_1 + \dots + u_n = 0$ is the reason for the name: Chapter 2 shows that the homogeneous coordinates $x_0, \dots, x_n$ of $\mathbb{P}^n$ correspond to the rays.

**Example 3.1.25 (the Hirzebruch surfaces).** The product of two fans $\Sigma_1$ in $(N_1)_{\mathbb{R}}$ and $\Sigma_2$ in $(N_2)_{\mathbb{R}}$ is the fan $\{\sigma_1 \times \sigma_2\}$ in $(N_1 \oplus N_2)_{\mathbb{R}}$. The product of two copies of the fan of $\mathbb{P}^1$ has rays $\pm e_1$, $\pm e_2$ and four quadrants as maximal cones. It is the fan of $\mathbb{P}^1 \times \mathbb{P}^1$. For $n \ge 0$, the fan of the Hirzebruch surface $\mathbb{F}_n$ has the rays

$$u_1 = e_1, \quad u_2 = e_2, \quad u_3 = -e_1 + n e_2, \quad u_4 = -e_2,$$

and the four maximal cones $\operatorname{Cone}(u_1, u_2)$, $\operatorname{Cone}(u_2, u_3)$, $\operatorname{Cone}(u_3, u_4)$, $\operatorname{Cone}(u_4, u_1)$. Consecutive generators form a basis, since $\det(u_2, u_3) = 1$ and $\det(u_3, u_4) = 1$, so the fan is smooth and complete. For $n = 0$ it is the fan of $\mathbb{P}^1 \times \mathbb{P}^1$. The relations $u_1 + u_3 = n u_2$ and $u_2 + u_4 = 0$ come back in Chapter 3, where they give the self-intersections $-n$ and $n$ of the two sections.

**Example 3.1.26 (the weighted projective plane $\mathbb{P}(1,1,n)$).** Remove the ray $u_2$ from the fan of $\mathbb{F}_n$ and merge the two cones that contain it. The result has the rays $u_1, u_3, u_4$ and the maximal cones $\operatorname{Cone}(u_1, u_3)$, $\operatorname{Cone}(u_3, u_4)$, $\operatorname{Cone}(u_4, u_1)$. It is a complete simplicial fan, and $u_1 + u_3 + n u_4 = 0$. The cone $\operatorname{Cone}(u_1, u_3) = \operatorname{Cone}(e_1, -e_1 + n e_2)$ has multiplicity $n$. The linear map that exchanges $e_1$ and $e_2$ is in $\mathrm{GL}_2(\mathbb{Z})$. It maps $e_2$ to $u_1$ and $n e_1 - e_2$ to $u_3$, so it carries $\sigma_n$ to $\operatorname{Cone}(u_1, u_3)$, and the cone is the cone of $\frac1n(1,1)$. This fan is the fan of $\mathbb{P}(1,1,n)$, and in Chapter 2 the removal of $u_2$ becomes the contraction of the negative section of $\mathbb{F}_n$ to the singular point of $\mathbb{P}(1,1,n)$.

**Example 3.1.27 (a set of cones that is not a fan).** Let $\sigma = \operatorname{Cone}(e_1, e_2)$ and $\sigma' = \operatorname{Cone}(e_1 + e_2, -e_1 + e_2)$. Both are smooth cones. Their intersection is $\operatorname{Cone}(e_2, e_1 + e_2)$, which is not a face of $\sigma$ or of $\sigma'$. So the set of faces of $\sigma$ and $\sigma'$ is not a fan, and the separation lemma fails: a form that is nonnegative on $\sigma$, nonpositive on $\sigma'$ and zero on $\sigma \cap \sigma'$ must vanish on $e_2$ and on $e_1 + e_2$, so it is zero, and then it vanishes on all of $\sigma$.

### Proof

*Proof of Proposition 3.1.20.* Let $\sigma \in \Sigma$. Then $\{0\}$ is a face of $\sigma$ by part 4 of Proposition 3.1.4, so $\{0\} \in \Sigma$. For $\sigma, \sigma' \in \Sigma$, the intersection is a face of $\sigma$ by axiom 2, so it is in $\Sigma$ by axiom 1. Since $\Sigma$ is finite, each cone $\tau$ lies in a maximal cone $\sigma$, and then $\tau = \tau \cap \sigma$ is a face of $\sigma$ by axiom 2. $\square$

*Proof of Lemma 3.1.21.* Put $\gamma = \sigma + (-\sigma')$, a rational polyhedral cone, maybe not strongly convex. A form is in $\gamma^\vee$ if and only if it is nonnegative on $\sigma$ and on $-\sigma'$, so $\gamma^\vee = \sigma^\vee \cap (-\sigma')^\vee$. It is a rational cone by Theorem 3.1.3. Its relative interior is open in its span, which is a rational subspace, so it contains a lattice point $m$.

First, $\gamma \cap m^\perp = \gamma \cap (-\gamma)$. The inclusion $\supseteq$ holds because $m$ is nonnegative on $\gamma$ and on $-\gamma$. Let $v \in \gamma$ with $\langle m, v \rangle = 0$, and suppose $-v \notin \gamma$. By part 2 of Theorem 3.1.3 there is $m'' \in \gamma^\vee$ with $\langle m'', -v \rangle < 0$. Since $m$ is in the relative interior of $\gamma^\vee$, the form $m - \varepsilon(m'' - m)$ lies in $\gamma^\vee$ for small $\varepsilon > 0$. Its value at $v$ is $-\varepsilon \langle m'', v \rangle < 0$. This is a contradiction, so $-v \in \gamma$.

Now $\tau \subseteq \sigma \cap m^\perp$: for $v \in \tau$, $v \in \sigma$ gives $\langle m, v \rangle \ge 0$, and $v \in \sigma'$ gives $\langle m, -v \rangle \ge 0$. Conversely let $v \in \sigma$ with $\langle m, v \rangle = 0$. Then $v \in \gamma \cap m^\perp$, so $-v \in \gamma$, and $-v = a - b$ with $a \in \sigma$, $b \in \sigma'$. So $v + a = b \in \sigma \cap \sigma' = \tau$. The points $v$ and $a$ lie in $\sigma$, and their sum lies in the face $\tau = \sigma \cap m_0^\perp$ for some $m_0 \in \sigma^\vee$. Then $\langle m_0, v \rangle + \langle m_0, a \rangle = 0$ with both terms nonnegative, so $\langle m_0, v \rangle = 0$ and $v \in \tau$. This proves $\tau = \sigma \cap m^\perp$. The same argument with the roles of $\sigma$ and $\sigma'$ exchanged and $-m$ in place of $m$ gives $\tau = \sigma' \cap m^\perp$. $\square$

### Exercises

1. (A) Draw the fan of $\mathbb{F}_1$ and check that removing the ray $u_2$ and merging the two cones gives the fan of $\mathbb{P}^2$ in a basis of $\mathbb{Z}^2$.
2. (A) Show that the fan of $\mathbb{P}^n$ in Example 3.1.24 is complete and smooth.
3. (A) For $\sigma = \operatorname{Cone}(e_1, e_2)$ and $\sigma' = \operatorname{Cone}(e_2, -e_1)$, find all $m$ of the separation lemma.
4. (B) Show that every complete fan in $\mathbb{R}^2$ is simplicial, and that the rays of a complete fan in $\mathbb{R}^2$ can be numbered $u_1, \dots, u_r$ in the counterclockwise order with maximal cones $\operatorname{Cone}(u_i, u_{i+1})$.
5. (B) Let $\Sigma$ be a smooth complete fan in $\mathbb{R}^2$ with rays $u_1, \dots, u_r$ in counterclockwise order, indices mod $r$. Show that $u_{i-1} + u_{i+1} = b_i u_i$ for integers $b_i$. Compute the $b_i$ for $\mathbb{P}^2$ and $\mathbb{F}_n$.
6. (B) Let $u_0, u_1, u_2 \in \mathbb{Z}^2$ be primitive with $q_0 u_0 + q_1 u_1 + q_2 u_2 = 0$ for positive integers $q_i$ with $\gcd(q_0, q_1, q_2) = 1$, and suppose that the $u_i$ span $\mathbb{Z}^2$. Show that the three cones spanned by pairs form a complete simplicial fan. It is the fan of the weighted projective plane $\mathbb{P}(q_0, q_1, q_2)$. Compute the multiplicities of its cones for $(q_0, q_1, q_2) = (1, 2, 3)$.

### Lean

The Lean structure follows Definition 3.1.17, with the faces of Mathlib:

```lean
structure Fan (n : ℕ) where
  /-- The cones of the fan. -/
  cones : Set (PointedCone ℝ (NR n))
  finite : cones.Finite
  rational : ∀ σ ∈ cones, IsRationalPolyhedral σ
  stronglyConvex : ∀ σ ∈ cones, IsStronglyConvex σ
  face_mem : ∀ σ ∈ cones, ∀ τ : PointedCone ℝ (NR n), τ.IsFaceOf σ → τ ∈ cones
  inter_face : ∀ σ ∈ cones, ∀ τ ∈ cones, PointedCone.IsFaceOf (σ ⊓ τ) σ
```

- Status: the definition and the instances are in the project library. `MinimalModel.Toric.Fan.bot_mem` and `MinimalModel.Toric.Fan.inf_mem` prove Proposition 3.1.20 except its last sentence. The fans `MinimalModel.Toric.Fan.trivial`, `MinimalModel.Toric.Fan.ofCone`, `MinimalModel.Toric.Fan.affine`, `MinimalModel.Toric.P1.fan` and `MinimalModel.Toric.P2.fan` are instances. Check F2 of spec 06.3 asks for such instances, so that the hypotheses of a statement about fans can hold. The separation lemma is not yet in Lean.
- Fidelity: axiom 2 is stated for the first cone only, `inter_face`, and `MinimalModel.Toric.Fan.inter_face_right` gives it for the second. The lattice is always $\mathbb{Z}^n \subset \mathbb{R}^n$. A cone of the Lean library is simplicial if it is spanned by some linearly independent lattice points, `MinimalModel.Toric.IsSimplicial`. This agrees with Definition 3.1.19, since such points lie on the rays of the cone.
- No node of the map covers this section. The fans of $\mathbb{P}^2$ and $\mathbb{F}_n$ are not yet in Lean.

### Notes and history

Fans first appear in Demazure's paper of 1970 on the Cremona group, for smooth complete toric varieties. Kempf, Knudsen, Mumford and Saint-Donat (1973) gave the general theory, with the name "torus embeddings", and Danilov's survey of 1978 made it standard. The separation lemma is in all texts: see Fulton, Section 1.2, and Cox-Little-Schenck, Chapter 1. The Hirzebruch surfaces are named after Hirzebruch's paper of 1951. The integers $b_i$ of Exercise 5 are the negatives of the self-intersections of the invariant curves, and Chapter 3 proves this. Weighted projective spaces are the simplest singular complete toric varieties, and they come back in the toric MMP as the targets of divisorial contractions.
