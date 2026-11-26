---
title: Quasi-coherent sheaves on affine schemes
nodes: []
sources: [Vak25, Har77, GW20, EGA1, Stacks]
reads_with: [Vak25:ch13, Har77:II.5, GW20:ch7]
requires: [P1.1, P1.2, P2.6, P3.1, P3.2, P3.3, P3.5]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Quasi-coherent sheaves on affine schemes

### Statement

Quasi-coherent, of finite type, of finite presentation and locally free are the conditions of Definition P2.6.26: local presentations by free modules. This section proves that on an affine scheme they are the conditions on modules that their names suggest. For a scheme $X$, write $\mathsf{QCoh}(X)$ for the full subcategory of $\mathsf{Mod}(\mathcal{O}_X)$ of quasi-coherent sheaves. For an open set $U$ and $f \in \mathcal{O}_X(U)$, write $U_f$ for the open set of the points of $U$ where $f$ does not vanish, as in Lemma P3.3.3. For an affine $U$ it is the basic open set $D(f)$.

**Proposition P3.5.10 (quasi-coherent means locally $\widetilde{M}$).** Let $X$ be a scheme and $\mathcal{F}$ an $\mathcal{O}_X$-module. Then $\mathcal{F}$ is quasi-coherent if and only if every point of $X$ has an affine open neighbourhood $U \cong \operatorname{Spec} B$ with $\mathcal{F}|_U \cong \widetilde{M}$ for some $B$-module $M$. In this case such neighbourhoods $U$ form a basis of the topology of $X$.

Lean: Mathlib `AlgebraicGeometry.Scheme.Modules.exists_affineOpenCover_presentation` (a quasi-coherent sheaf has presentations on an affine open cover) and the instance `AlgebraicGeometry.Scheme.Modules.isQuasicoherent_restrictFunctor` (restriction to an open subscheme preserves quasi-coherence), both in Mathlib.

**Lemma P3.5.11 (sections over the locus where a function does not vanish).** Let $X$ be a scheme, $\mathcal{F}$ a quasi-coherent $\mathcal{O}_X$-module and $f \in \Gamma(X, \mathcal{O}_X)$.

1. If $X$ is quasi-compact and $s \in \mathcal{F}(X)$ has $s|_{X_f} = 0$, then $f^n s = 0$ for some $n \geq 0$.
2. If $X$ has a finite cover by affine open sets $U_1, \dots, U_r$ such that every $U_i \cap U_j$ is quasi-compact, then the restriction induces an isomorphism $\mathcal{F}(X)_f \cong \mathcal{F}(X_f)$.

Lean: for $\mathcal{F} = \mathcal{O}_X$ this is Mathlib `AlgebraicGeometry.isLocalization_basicOpen_of_qcqs`. For modules it is not in Lean as stated.

**Theorem P3.5.12 (quasi-coherent sheaves on an affine scheme).** Let $X = \operatorname{Spec} A$ and let $\mathcal{F}$ be an $\mathcal{O}_X$-module. The following are equivalent:

1. $\mathcal{F}$ is quasi-coherent;
2. $\mathcal{F} \cong \widetilde{M}$ for some $A$-module $M$;
3. the counit $\theta_\mathcal{F} \colon \Gamma(X, \mathcal{F})^\sim \to \mathcal{F}$ of Theorem P3.5.2 is an isomorphism.

So $M \mapsto \widetilde{M}$ and $\mathcal{F} \mapsto \Gamma(X, \mathcal{F})$ are inverse equivalences of categories between $\mathsf{Mod}_A$ and $\mathsf{QCoh}(X)$.

Lean: Mathlib `AlgebraicGeometry.isQuasicoherent_iff_isIso_fromTildeΓ` (the equivalence of 1 and 3), `AlgebraicGeometry.isIso_fromTildeΓ_iff` and `AlgebraicGeometry.essImage_tilde` (the equivalence with 2), and `AlgebraicGeometry.tildeEquiv` (the equivalence of categories), all in Mathlib.

**Corollary P3.5.13 (quasi-coherent sheaves on a scheme).** Let $X$ be a scheme and $\mathcal{F}$ an $\mathcal{O}_X$-module.

1. $\mathcal{F}$ is quasi-coherent if and only if $\mathcal{F}|_U \cong \mathcal{F}(U)^\sim$ for every affine open set $U$, and if and only if this holds for every member of one cover of $X$ by affine open sets.
2. If $\mathcal{F}$ is quasi-coherent, $U$ is an affine open set and $f \in \mathcal{O}_X(U)$, then $\mathcal{F}(U_f) = \mathcal{F}(U)_f$.
3. If $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ is an exact sequence of quasi-coherent sheaves and $U$ is affine, then $0 \to \mathcal{F}'(U) \to \mathcal{F}(U) \to \mathcal{F}''(U) \to 0$ is exact.

Lean: not in Lean as stated.

**Proposition P3.5.14 (finiteness conditions on an affine scheme).** Let $X = \operatorname{Spec} A$ and let $M$ be an $A$-module.

1. $\widetilde{M}$ is of finite type if and only if $M$ is finitely generated.
2. $\widetilde{M}$ is of finite presentation if and only if $M$ is finitely presented.
3. $\widetilde{M}$ is locally free of finite rank, that is, every point has a neighbourhood $U$ with $\widetilde{M}|_U \cong \mathcal{O}_U^n$ for some finite $n$, if and only if $M$ is finitely presented and $M_\mathfrak{p}$ is a free $A_\mathfrak{p}$-module for every prime $\mathfrak{p}$. In this case every prime $\mathfrak{p}$ has an $f \notin \mathfrak{p}$ with $M_f$ free over $A_f$.

Lean: Mathlib `AlgebraicGeometry.presentationTilde` gives a presentation of $\widetilde{M}$ from generators of $M$. The converses are not in Lean as stated.

### Proof in words

The definition of quasi-coherence asks for a local presentation $\mathcal{O}^{(J)} \to \mathcal{O}^{(I)} \to \mathcal{F} \to 0$. On a small affine open set, the map of free sheaves is the sheaf of a map of free modules, by full faithfulness, and the cokernel is the sheaf of the cokernel module, by exactness. So a quasi-coherent sheaf is $\widetilde{M}$ locally.

The real content is the passage from local to global on $\operatorname{Spec} A$. A section over $D(f)$ is given on finitely many small affine pieces by fractions $m_i/f^{n}$. After multiplication by a power of $f$ these fractions extend to the pieces, and after a further power they agree on the overlaps and glue. This is the argument of Lemma P3.3.3 with modules in place of functions, and it needs the same finiteness. It proves $\mathcal{F}(D(f)) = \mathcal{F}(X)_f$, which says that $\mathcal{F}$ is the sheaf of its global sections. The finiteness conditions then pass from local to global by the usual trick: the $f_i$ that cover $\operatorname{Spec} A$ generate the unit ideal, and a module that vanishes after inverting each $f_i$ is zero.

### Examples

**Example P3.5.15 (a sheaf that is not quasi-coherent).** The sheaf $\mathcal{F} = (0, K, 0)$ on the spectrum of a discrete valuation ring of Example P3.5.8 is not quasi-coherent, by Theorem P3.5.12: $\Gamma(X, \mathcal{F}) = 0$, and $\mathcal{F} \neq 0$. The extension by zero $j_! \mathcal{O}_U$ of Example P2.6.33 fails for the same reason. Its stalks are all free, so the failure is not visible on stalks.

**Example P3.5.16 (finite type but not finite presentation).** Let $A = k[x_1, x_2, \dots]$ and $M = A/\mathfrak{m}$ with $\mathfrak{m} = (x_1, x_2, \dots)$, so $M = k$. The sheaf $\widetilde{M}$ is the skyscraper sheaf $k$ at the origin, and it is of finite type, generated by one section. It is not of finite presentation. Otherwise $M$ would be finitely presented by Proposition P3.5.14, and then the kernel $\mathfrak{m}$ of $A \to M$ would be finitely generated by Lemma P1.1.49. But $\mathfrak{m}$ is not finitely generated, since finitely many generators involve only finitely many variables $x_1, \dots, x_N$ and do not produce $x_{N+1}$. Over a Noetherian ring the two conditions agree.

**Example P3.5.17 (a line bundle that is not trivial).** Let $A = \mathbb{Z}[\sqrt{-5}]$ and $\mathfrak{p} = (2, 1 + \sqrt{-5})$. By Example P1.2.11, $\mathfrak{p}_\mathfrak{q}$ is free of rank $1$ over $A_\mathfrak{q}$ for every prime $\mathfrak{q}$, and $\mathfrak{p}$ is not principal. The ring $A$ is Noetherian, so $\mathfrak{p}$ is finitely presented, and $\widetilde{\mathfrak{p}}$ is locally free of rank $1$ by part 3 of Proposition P3.5.14: it is a line bundle on $\operatorname{Spec} A$. It is not isomorphic to $\mathcal{O}_X$: by Theorem P3.5.12 such an isomorphism would be an isomorphism $A \cong \mathfrak{p}$ of $A$-modules, and the image of $1$ would generate $\mathfrak{p}$. So $\operatorname{Pic}(\operatorname{Spec} A) \neq 0$. Chapter 9 identifies this group with the class group of $A$ of P1 Ch. 7.

**Example P3.5.18 (an ideal that is not locally free).** Let $A = k[x, y]$ and $I = (x, y)$. The sheaf $\widetilde{I}$ is of finite presentation. It is locally free away from the origin, since $I_x = A_x$ and $I_y = A_y$. It is not locally free near the origin. If $\widetilde{I}|_U \cong \mathcal{O}_U^r$ on a neighbourhood $U$ of the origin, then at the generic point $\widetilde{I}_\eta = I \otimes_A K = K$ gives $r = 1$, and at the origin $I_\mathfrak{m} / \mathfrak{m} I_\mathfrak{m} = I/\mathfrak{m} I$ has dimension $2$ over $k$, with basis $\bar x, \bar y$, which gives $r = 2$. Section 5.3 turns this count of dimensions into a general criterion.

**Example P3.5.19 (the lemma needs finiteness).** Let $X = \bigsqcup_{n \geq 1} \operatorname{Spec} k[t]$, $\mathcal{F} = \mathcal{O}_X$ and $f = (t, t, \dots)$. Example P3.3.6 shows that $\mathcal{F}(X)_f \to \mathcal{F}(X_f)$ is not surjective. So part 2 of Lemma P3.5.11 fails for the quasi-coherent sheaf $\mathcal{O}_X$ on a scheme that is not quasi-compact. Example P3.3.6 also shows that part 1 fails without quasi-compactness.

### Proof

*Proof of Proposition P3.5.10.* Suppose that $\mathcal{F}|_U \cong \widetilde{M}$ with $U = \operatorname{Spec} B$. Choose a presentation $B^{(J)} \to B^{(I)} \to M \to 0$. By parts 2 and 3 of Proposition P3.5.1 and $\widetilde{B} = \mathcal{O}_U$, the sequence $\mathcal{O}_U^{(J)} \to \mathcal{O}_U^{(I)} \to \mathcal{F}|_U \to 0$ is exact. So if every point has such a $U$, then $\mathcal{F}$ is quasi-coherent.

Conversely, let $\mathcal{F}$ be quasi-coherent, $x \in X$ and $W$ an open neighbourhood of $x$. Choose an open $U' \ni x$ with an exact sequence $\mathcal{O}_{U'}^{(J)} \xrightarrow{\alpha} \mathcal{O}_{U'}^{(I)} \to \mathcal{F}|_{U'} \to 0$. Choose an affine open $V \ni x$ and a basic open set $U = D(g)$ of $V$ with $x \in U \subseteq U' \cap W$, and write $U = \operatorname{Spec} B$ (Proposition P3.1.13). On $U$ the sources and targets of $\alpha$ are $(B^{(J)})^\sim$ and $(B^{(I)})^\sim$ by part 3 of Proposition P3.5.1, so by part 1 of Theorem P3.5.2 the restriction $\alpha|_U$ is $\widetilde{u}$ for a $B$-linear map $u \colon B^{(J)} \to B^{(I)}$. Let $M = \operatorname{coker} u$. The sequence $B^{(J)} \to B^{(I)} \to M \to 0$ is exact, so $\widetilde{M}$ is the cokernel of $\widetilde{u}$ by part 2 of Proposition P3.5.1. Cokernels are unique up to unique isomorphism, so $\mathcal{F}|_U \cong \widetilde{M}$. This proves the converse, and since $U \subseteq W$ for an arbitrary $W$, it also proves the last statement. $\square$

*Proof of Lemma P3.5.11.* First a remark on refinement. Let $V \cong \operatorname{Spec} B$ be an affine open set with $\mathcal{F}|_V \cong \widetilde{M}$, and let $g$ be a function on an open set that contains $V$. Then $V_g$ is the basic open set $D(g|_V)$, and $\mathcal{F}(V_g) = M_{g|_V}$ by Corollary P3.1.5, with restriction the localization map.

(1) By Proposition P3.5.10 and quasi-compactness, $X$ is covered by finitely many affine open sets $V_1, \dots, V_m$ with $\mathcal{F}|_{V_i} \cong \widetilde{M_i}$. The restriction $s_i = s|_{V_i} \in M_i$ maps to $0$ in $\mathcal{F}((V_i)_f) = (M_i)_f$, so $f^{n_i} s_i = 0$ for some $n_i$. With $n = \max n_i$, $f^n s$ vanishes on every $V_i$, so $f^n s = 0$.

(2) Each $U_i$ is quasi-compact, so by Proposition P3.5.10 and the remark it is covered by finitely many basic open sets of $U_i$ on which $\mathcal{F}$ is $\widetilde{M}$. Together these form a finite cover of $X$ by affine open sets $V_1, \dots, V_m$ with $\mathcal{F}|_{V_k} \cong \widetilde{M_k}$. Every $V_k \cap V_l$ is quasi-compact: if $V_k = (U_i)_g$ and $V_l = (U_j)_h$, then $V_k \cap V_l = (U_i \cap U_j)_{gh}$, and a set of the form $W_{gh}$ in a quasi-compact scheme $W$ is quasi-compact, because its intersection with each of finitely many affine open sets that cover $W$ is a basic open set of that affine set.

Injectivity. Let $s/f^a \in \mathcal{F}(X)_f$ restrict to $0$ on $X_f$. Then $s|_{X_f} = 0$, so $f^n s = 0$ for some $n$ by part 1, and $s/f^a = 0$.

Surjectivity. Let $t \in \mathcal{F}(X_f)$. On $V_k$, the restriction $t|_{(V_k)_f}$ lies in $\mathcal{F}((V_k)_f) = (M_k)_f$ by the remark, so it is $t_k / f^{n}$ for some $t_k \in \mathcal{F}(V_k)$, with one $n$ for all $k$ since there are finitely many. On $V_k \cap V_l$ the section $t_k - t_l$ restricts to $f^n t - f^n t = 0$ on $(V_k \cap V_l)_f$. The scheme $V_k \cap V_l$ is quasi-compact, so by part 1 there is $p$, again one for all $k, l$, with $f^p (t_k - t_l) = 0$ on $V_k \cap V_l$. So the sections $f^p t_k$ agree on the overlaps and glue to $s \in \mathcal{F}(X)$, with $s|_{X_f} = f^{n + p} t$ because this holds on each $(V_k)_f$. So $t$ is the image of $s / f^{n + p}$. $\square$

*Proof of Theorem P3.5.12.* (3) implies (2) with $M = \Gamma(X, \mathcal{F})$, and (2) implies (1) by Proposition P3.5.10 with $U = X$.

(1) implies (3). Let $M = \Gamma(X, \mathcal{F})$. The scheme $X$ satisfies the hypothesis of part 2 of Lemma P3.5.11 with the cover by $X$ itself, and so does every basic open set $D(f)$. For $f \in A$, the map $(\theta_\mathcal{F})_{D(f)} \colon M_f \to \mathcal{F}(D(f))$ is $m/f^n \mapsto f^{-n} m|_{D(f)}$, by the construction in the proof of Theorem P3.5.2. This is the map of part 2 of Lemma P3.5.11 for $X$ and $f$, so it is an isomorphism. So $\theta_\mathcal{F}$ is an isomorphism on every basic open set. A morphism of sheaves that is bijective on the members of a basis is bijective on stalks, because each stalk is the colimit over the members of the basis that contain the point, and so it is an isomorphism (part 3 of Theorem P2.6.3).

The equivalence. The functor $M \mapsto \widetilde{M}$ lands in $\mathsf{QCoh}(X)$ by (2) implies (1). The isomorphisms $\Gamma(X, \widetilde{M}) = M$ of Corollary P3.1.5 and $\theta_\mathcal{F} \colon \Gamma(X, \mathcal{F})^\sim \cong \mathcal{F}$ for quasi-coherent $\mathcal{F}$ are natural, so the two functors are inverse equivalences. $\square$

*Proof of Corollary P3.5.13.* (1) Quasi-coherence is a local condition, and the restriction of a quasi-coherent sheaf to an open set is quasi-coherent, directly from Definition P2.6.26. If $\mathcal{F}$ is quasi-coherent and $U$ is affine, then $\mathcal{F}|_U$ is quasi-coherent and Theorem P3.5.12 gives $\mathcal{F}|_U \cong \mathcal{F}(U)^\sim$. If $\mathcal{F}|_{U_i} \cong \mathcal{F}(U_i)^\sim$ for the members of an affine open cover, then $\mathcal{F}$ is quasi-coherent by Proposition P3.5.10.

(2) By part 1, $\mathcal{F}|_U \cong \mathcal{F}(U)^\sim$, and $U_f = D(f)$, so $\mathcal{F}(U_f) = \mathcal{F}(U)_f$ by Corollary P3.1.5.

(3) Let $U = \operatorname{Spec} A$. By part 1 and the naturality of $\theta$, the restricted sequence is isomorphic to the sequence of sheaves of $0 \to \mathcal{F}'(U) \to \mathcal{F}(U) \to \mathcal{F}''(U) \to 0$. That sequence of sheaves is exact, so the sequence of modules is exact by part 4 of Proposition P3.5.1. $\square$

*Proof of Proposition P3.5.14.* A local-to-global step is used twice. *Claim:* if $f_1, \dots, f_r$ generate the unit ideal and $N_{f_i}$ is finitely generated over $A_{f_i}$ for every $i$, then $N$ is finitely generated. Indeed, choose finitely many elements of $N$ whose images generate every $N_{f_i}$, which is possible after clearing denominators, which are units. Let $N' \subseteq N$ be the submodule they generate. Then $(N/N')_{f_i} = 0$ for every $i$ by Theorem P1.2.5. Every prime $\mathfrak{p}$ misses some $f_i$, because the $f_i$ generate the unit ideal, so $(N/N')_\mathfrak{p}$ is a localization of $(N/N')_{f_i} = 0$. So $N = N'$ by Theorem P1.2.8.

A second remark is used in all three parts. Let $\alpha \colon \mathcal{O}_U^a \to \widetilde{M}|_U$ be a morphism on an open set $U$, and let $D(g) \subseteq U$. Then $\alpha|_{D(g)}$ is a morphism $(A_g^a)^\sim \to (M_g)^\sim$ on $\operatorname{Spec} A_g$, by part 1 of Proposition P3.5.3, so it is $\widetilde{u}$ for an $A_g$-linear map $u \colon A_g^a \to M_g$ by part 1 of Theorem P3.5.2. By part 4 of Proposition P3.5.1, $\alpha|_{D(g)}$ is surjective if and only if $u$ is, and the same holds for exactness of sequences.

(1) If $A^n \to M$ is surjective, then $\mathcal{O}_X^n \to \widetilde{M}$ is surjective by part 2 of Proposition P3.5.1. Conversely, let $\widetilde{M}$ be of finite type. Every point lies in a basic open set $D(g)$ inside an open set on which $\mathcal{O}^n \to \widetilde{M}$ is surjective, and by the remark $M_g$ is then finitely generated over $A_g$. The space $X$ is quasi-compact (Proposition P1.2.17), so finitely many such $D(g_i)$ cover $X$, and then the $g_i$ generate the unit ideal. So $M$ is finitely generated by the claim.

(2) If $A^m \to A^n \to M \to 0$ is a finite presentation, it gives a finite presentation of $\widetilde{M}$ by Proposition P3.5.1. Conversely, let $\widetilde{M}$ be of finite presentation. Then $\widetilde{M}$ is of finite type, and $M$ is finitely generated by part 1. Choose a surjection $\pi \colon A^n \to M$ with kernel $K$. As in part 1, there are $g_1, \dots, g_r$ that generate the unit ideal with exact sequences $A_{g_i}^{b} \to A_{g_i}^{a} \to M_{g_i} \to 0$, so each $M_{g_i}$ is a finitely presented $A_{g_i}$-module. The localization $\pi_{g_i} \colon A_{g_i}^n \to M_{g_i}$ is surjective with kernel $K_{g_i}$ (Theorem P1.2.5), so $K_{g_i}$ is finitely generated by Lemma P1.1.49. By the claim, $K$ is finitely generated, and $M$ is finitely presented.

(3) Suppose that $\widetilde{M}$ is locally free of finite rank. A sheaf $\mathcal{O}_U^n$ is of finite presentation, so $\widetilde{M}$ is of finite presentation, and $M$ is finitely presented by part 2. The stalk $M_\mathfrak{p}$ is the stalk of $\mathcal{O}_U^n$, the free module $A_\mathfrak{p}^n$.

Conversely, let $M$ be finitely presented with $M_\mathfrak{p}$ free of rank $r$. Choose $m_1, \dots, m_r \in M$ whose images form a basis of $M_\mathfrak{p}$; this is possible since the denominators are units of $A_\mathfrak{p}$. Let $u \colon A^r \to M$ send the $i$th basis vector to $m_i$, so that $u_\mathfrak{p}$ is an isomorphism. The cokernel $C$ of $u$ is finitely generated with $C_\mathfrak{p} = 0$. Each of its finitely many generators is killed by an element outside $\mathfrak{p}$, so their product $f_1 \notin \mathfrak{p}$ has $C_{f_1} = 0$, and $u_{f_1}$ is surjective. The module $M_{f_1}$ is finitely presented over $A_{f_1}$, so the kernel $K$ of $u_{f_1}$ is finitely generated by Lemma P1.1.49, and $K_\mathfrak{p} = 0$ because $u_\mathfrak{p}$ is injective. As before there is $f_2 \notin \mathfrak{p}$ with $K_{f_2} = 0$. For $f = f_1 f_2$ the map $u_f \colon A_f^r \to M_f$ is an isomorphism. So $M_f$ is free, and $\widetilde{M}|_{D(f)} \cong (M_f)^\sim \cong \mathcal{O}_{D(f)}^r$ by Proposition P3.5.3. $\square$

### Exercises

1. (A) Let $X$ be a scheme. Show that $\mathcal{O}_X$, every locally free sheaf and every direct sum of quasi-coherent sheaves are quasi-coherent, by checking the condition of part 1 of Corollary P3.5.13 on an affine open cover.
2. (A) Let $X = \operatorname{Spec} A$ and let $\mathcal{F}$ be a quasi-coherent sheaf with $\mathcal{F}_\mathfrak{p} = 0$ for every closed point $\mathfrak{p}$. Show that $\mathcal{F} = 0$.
3. (A) Let $X = \operatorname{Spec} A$. Show that a morphism $\varphi \colon \mathcal{F} \to \mathcal{G}$ of quasi-coherent sheaves is an isomorphism if and only if $\varphi_X$ is an isomorphism, and give an example of a morphism $\varphi$ of $\mathcal{O}_X$-modules with $\varphi_X$ an isomorphism that is not an isomorphism.
4. (B) Let $X$ be a quasi-compact and quasi-separated scheme, and $\mathcal{F}$ a quasi-coherent sheaf. Let $f \in \Gamma(X, \mathcal{O}_X)$ and $t \in \mathcal{F}(X_f)$. Show that $f^N t$ is the restriction of a global section for some $N$. Interpret this for $X = \operatorname{Spec} k[x]$, $\mathcal{F} = \mathcal{O}_X$ and $f = x$.
5. (B) Let $X = \operatorname{Spec} A$ and let $\mathcal{F}$ be a quasi-coherent sheaf of finite type with $\mathcal{F}_\mathfrak{p} = 0$. Show that $\mathcal{F}|_{D(f)} = 0$ for some $f \notin \mathfrak{p}$. Show by the module $\bigoplus_{n \ge 1} \mathbb{Q}[x]/(x - n)$ over $\mathbb{Q}[x]$, at the generic point, that finite type is needed.
6. (B) Let $A$ be a ring. Show that a finitely generated projective $A$-module $P$ gives a locally free sheaf $\widetilde{P}$ of finite rank, and conversely that $M$ is projective if $\widetilde{M}$ is locally free of finite rank. (For the converse, show that $\operatorname{Hom}_A(M, -)$ is exact by localizing at the primes, using that $\operatorname{Hom}_A(M, N)_\mathfrak{p} = \operatorname{Hom}_{A_\mathfrak{p}}(M_\mathfrak{p}, N_\mathfrak{p})$ for $M$ finitely presented.)
7. (C) Let $X = \operatorname{Spec} A$ and $U = D(f_1) \cup \dots \cup D(f_r)$. Show that every quasi-coherent sheaf $\mathcal{G}$ on $U$ is the restriction of a quasi-coherent sheaf on $X$. (Use the pushforward $j_* \mathcal{G}$ along $j \colon U \to X$ and part 2 of Lemma P3.5.11 to compute its sections over $D(g)$; Section 5.4 proves the general case.)

### Lean

Mathlib proves the main theorem of the section in the form `AlgebraicGeometry.isQuasicoherent_iff_isIso_fromTildeΓ`, and packages it as the equivalence `AlgebraicGeometry.tildeEquiv` between `ModuleCat R` and the full subcategory of quasi-coherent sheaves of modules on `Spec R`. Its notion of quasi-coherence is `SheafOfModules.IsQuasicoherent`, which asks for local presentations as in Definition P2.6.26. The finiteness statements of Proposition P3.5.14 and the exactness of sections in Corollary P3.5.13 are not in Lean as stated. The handbook adds no `MinimalModel` node here.

### Notes and history

The theorem is EGA I, Chapter I, Theorem 1.4.1, and Hartshorne, Corollary II.5.5, where the proof goes through Lemma II.5.3, the module form of Lemma P3.3.3. Vakil, Chapter 13, defines quasi-coherence by the condition of part 1 of Corollary P3.5.13 and proves its independence of the cover by the affine communication lemma. The literature state is theorem. In the minimal model program, the sheaves $\mathcal{O}_X(D)$ of a Weil divisor on a normal variety are quasi-coherent of finite type, and the passage from a sheaf to its module of sections over an affine chart is how the local computations of Volume 4 are made.
