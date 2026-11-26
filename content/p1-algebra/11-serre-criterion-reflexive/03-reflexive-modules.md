---
title: Reflexive modules
nodes: []
sources: [AM69, Mat86, Eis95]
reads_with: [Mat86:ch4, Eis95:ch11]
requires: [P1.1, P1.2, P1.7, P1.8, P1.9, P1.10]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Reflexive modules

### Statement

Throughout, $A$ is a Noetherian normal domain with fraction field $K$, and $M$ is a finitely generated $A$-module. For a prime $\mathfrak{p}$ of height one, $A_\mathfrak{p}$ is a DVR by Krull's theorem (Theorem P1.8.2), with valuation $v_\mathfrak{p}$.

**Definition P1.11.20 (dual and reflexive module).** The *dual* of $M$ is $M^* = \operatorname{Hom}_A(M, A)$. The *canonical map* $\varepsilon_M : M \to M^{**}$ sends $m$ to the evaluation $f \mapsto f(m)$. The module $M$ is *reflexive* if $\varepsilon_M$ is an isomorphism. The module $M$ is *torsion-free* if $am = 0$ with $a \neq 0$ implies $m = 0$, and its *rank* is $\dim_K M \otimes_A K$.

Lean: Mathlib `Module.Dual`, `Module.Dual.eval` and `Module.IsReflexive` (definitions).

A finitely generated free module is reflexive, and so is a direct summand of one, that is, a finitely generated projective module. Since $M$ is finitely presented, $(M^*)_\mathfrak{p} = (M_\mathfrak{p})^*$ for every prime $\mathfrak{p}$, the dual over $A_\mathfrak{p}$, and $\varepsilon_M$ localizes to $\varepsilon_{M_\mathfrak{p}}$.

**Lemma P1.11.21 (torsion-free modules).** Let $M$ be torsion-free and $V = M \otimes_A K$. Then $M \to V$, $m \mapsto m \otimes 1$, is injective, and $M$ embeds in a free module $A^r$ with $r$ the rank of $M$. The kernel of $\varepsilon_M$ is the torsion submodule of $M$, and $M^*$ is torsion-free for every $M$. Under the identification $M^* \subseteq \operatorname{Hom}_K(V, K)$, a $K$-linear form $f$ lies in $M^*$ if and only if $f(M) \subseteq A$.

Lean: not in Mathlib in this form.

*Proof.* The kernel of $M \to M \otimes_A K = M_{(0)}$ consists of the $m$ with $am = 0$ for some $a \neq 0$, which is $0$ for torsion-free $M$. Choose a basis $e_1, \dots, e_r$ of $V$ and generators $m_1, \dots, m_s$ of $M$. Each $m_j$ is a $K$-combination of the $e_i$, and there is a common denominator $c \neq 0$ with $cM \subseteq Ae_1 + \dots + Ae_r \cong A^r$. Multiplication by $c$ is injective on $M$, so $M$ embeds in $A^r$. A torsion element is killed by every linear map to the domain $A$, so it lies in $\ker \varepsilon_M$. Conversely, if $M$ is torsion-free, the coordinate functions of $A^r$ restricted to $cM$ separate the points of $M$, so $\ker \varepsilon_M = 0$; for general $M$ apply this to $M/T$, where $T$ is the torsion submodule, since every $f \in M^*$ factors through $M/T$. If $a f = 0$ with $a \neq 0$, then $a f(m) = 0$ in $A$ for all $m$, so $f = 0$, and $M^*$ is torsion-free. The last statement holds because an $A$-linear map $M \to A$ extends uniquely to a $K$-linear map $V \to K$, and $V$ is spanned by $M$. $\square$

**Theorem P1.11.22 (reflexive modules over a normal domain).** Let $M$ be torsion-free, and regard $M$ and all $M_\mathfrak{p}$ as submodules of $V = M \otimes_A K$. Then $M$ is reflexive if and only if
$$
M = \bigcap_{\operatorname{ht} \mathfrak{p} = 1} M_\mathfrak{p}
$$
inside $V$. The dual $N^*$ of every finitely generated module $N$ is reflexive.

Lean: not in Mathlib.

*Proof.* First let $N$ be any finitely generated module, and regard $N^*$ inside $W = \operatorname{Hom}_K(N \otimes_A K, K)$ as in the lemma. Then $N^* = \bigcap_\mathfrak{p} (N^*)_\mathfrak{p}$ over the primes of height one. Indeed, $\subseteq$ is clear. If $f \in W$ lies in every $(N^*)_\mathfrak{p} = \operatorname{Hom}_{A_\mathfrak{p}}(N_\mathfrak{p}, A_\mathfrak{p})$, then $f(n) \in \bigcap_\mathfrak{p} A_\mathfrak{p} = A$ for every $n \in N$, by the algebraic Hartogs theorem (Corollary P1.8.3), so $f \in N^*$.

Let $M$ be reflexive. Then $M \cong M^{**} = (M^*)^*$, and the identification is compatible with the embeddings into $V \cong V^{**}$, so $M$ is the intersection of its localizations by the first step applied to $N = M^*$.

Conversely, assume $M = \bigcap_\mathfrak{p} M_\mathfrak{p}$. By the lemma, $\varepsilon_M$ is injective, and $M \subseteq M^{**} \subseteq V$. For a prime $\mathfrak{p}$ of height one, $M_\mathfrak{p}$ is a finitely generated torsion-free module over the DVR $A_\mathfrak{p}$, which is a principal ideal domain, so $M_\mathfrak{p}$ is free and reflexive. So $(M^{**})_\mathfrak{p} = (M_\mathfrak{p})^{**} = M_\mathfrak{p}$. By the first step for $N = M^*$,
$$
M \subseteq M^{**} = \bigcap_\mathfrak{p} (M^{**})_\mathfrak{p} = \bigcap_\mathfrak{p} M_\mathfrak{p} = M .
$$
So $\varepsilon_M$ is an isomorphism. The last claim is the first step together with this argument applied to $M = N^*$, which is torsion-free by the lemma. $\square$

**Corollary P1.11.23 (reflexive modules have depth two).** Let $M$ be reflexive and $\mathfrak{p}$ a prime with $\operatorname{ht} \mathfrak{p} \geq 2$ and $M_\mathfrak{p} \neq 0$. Then $\operatorname{depth} M_\mathfrak{p} \geq 2$. If $A$ is a regular local ring of dimension $2$, every reflexive module is free.

Lean: not in Mathlib.

*Proof.* Replace $A$ by $A_\mathfrak{p}$ and $M$ by $M_\mathfrak{p}$, which is reflexive since $\varepsilon$ localizes. So let $A$ be local with maximal ideal $\mathfrak{m}$ of height at least $2$. A nonzero $x \in \mathfrak{m}$ is a nonzerodivisor on the torsion-free module $M$. Suppose that $u \in M$ satisfies $\mathfrak{m}u \subseteq xM$, and put $w = u/x \in V$. Then $\mathfrak{m}w \subseteq M$. For a prime $\mathfrak{q}$ of height one, $\mathfrak{m} \not\subseteq \mathfrak{q}$, so there is $s \in \mathfrak{m} \setminus \mathfrak{q}$ with $sw \in M$, and $w \in M_\mathfrak{q}$. By the theorem, $w \in M$, so $u \in xM$. So no nonzero element of $M/xM$ is killed by $\mathfrak{m}$, $\mathfrak{m} \notin \operatorname{Ass}(M/xM)$, and $\operatorname{depth} M \geq 2$.

If $A$ is regular local of dimension $2$, then $\operatorname{pd}_A M < \infty$ by Section 9.3, and the Auslander-Buchsbaum formula of Section 10.1 gives $\operatorname{pd}_A M = 2 - \operatorname{depth} M = 0$. So $M$ is free by Theorem P1.1.50. $\square$

The converse of the corollary holds: a torsion-free module $M$ with $\operatorname{depth} M_\mathfrak{p} \geq 2$ at every prime of height at least two is reflexive (Exercise 6). So over a normal surface the reflexive modules are the modules that are Cohen-Macaulay of dimension $2$ at every maximal ideal, the *maximal Cohen-Macaulay* modules. On a smooth surface every reflexive sheaf is locally free.

**Theorem P1.11.24 (divisorial ideals).** For a Weil divisor $D = \sum n_\mathfrak{p}[\mathfrak{p}]$, let
$$
A(D) = \{ f \in K^* : \operatorname{div}(f) + D \geq 0 \} \cup \{0\} .
$$
1. $A(D)$ is a reflexive fractional ideal of rank one, and $A(D)_\mathfrak{p} = t_\mathfrak{p}^{-n_\mathfrak{p}} A_\mathfrak{p}$ for every prime $\mathfrak{p}$ of height one, with $t_\mathfrak{p}$ a uniformizer of $A_\mathfrak{p}$.
2. Every reflexive module of rank one is isomorphic to $A(D)$ for some $D$.
3. $A(D) \cong A(D')$ if and only if $D$ and $D'$ are linearly equivalent, and $A(D)$ is invertible if and only if $D$ is Cartier.

So $D \mapsto A(D)$ is a bijection from $\operatorname{Cl}(A)$ to the set of isomorphism classes of reflexive modules of rank one, and it restricts to the injection $\operatorname{Pic}(A) \to \operatorname{Cl}(A)$ of Theorem P1.8.20.

Lean: not in Mathlib. Mathlib has `ClassGroup` for the ideal class group.

*Proof.* (1) The set $A(D)$ is an $A$-submodule of $K$. If $b \in A$ is nonzero with $v_\mathfrak{p}(b) \geq n_\mathfrak{p}$ for all $\mathfrak{p}$, for example a product of suitable powers of elements of the finitely many $\mathfrak{p}$ with $n_\mathfrak{p} > 0$, then $bA(D) \subseteq A$ by Corollary P1.8.3, so $A(D)$ is a fractional ideal, finitely generated since $A$ is Noetherian. Let $\mathfrak{p}$ have height one. Clearly $A(D) \subseteq t_\mathfrak{p}^{-n_\mathfrak{p}}A_\mathfrak{p}$, so it suffices to find $g \in A(D)$ with $v_\mathfrak{p}(g) = -n_\mathfrak{p}$. Let $g_0 = t_\mathfrak{p}^{-n_\mathfrak{p}}$, with $t_\mathfrak{p} \in A$ chosen with $v_\mathfrak{p}(t_\mathfrak{p}) = 1$. The set $S$ of primes $\mathfrak{q} \neq \mathfrak{p}$ of height one with $v_\mathfrak{q}(g_0) + n_\mathfrak{q} < 0$ is finite. Distinct primes of height one are incomparable, so $\mathfrak{q}_i \not\subseteq \mathfrak{p}$, and since $\mathfrak{p}$ is prime, the product $\mathfrak{q}_1 \cdots \mathfrak{q}_s$ of the primes in $S$ is not contained in $\mathfrak{p}$, and for $N$ large an element $a \in (\mathfrak{q}_1 \cdots \mathfrak{q}_s)^N \setminus \mathfrak{p}$ satisfies $v_\mathfrak{p}(a) = 0$ and $v_\mathfrak{q}(ag_0) + n_\mathfrak{q} \geq 0$ for all $\mathfrak{q}$. So $g = ag_0 \in A(D)$ with $v_\mathfrak{p}(g) = -n_\mathfrak{p}$. Now $A(D) = \bigcap_\mathfrak{p} t_\mathfrak{p}^{-n_\mathfrak{p}} A_\mathfrak{p} = \bigcap_\mathfrak{p} A(D)_\mathfrak{p}$ by definition, so $A(D)$ is reflexive by the theorem on reflexive modules.

(2) Let $M$ be reflexive of rank one. Then $M \otimes_A K \cong K$, and the lemma identifies $M$ with a finitely generated $A$-submodule $I \neq 0$ of $K$. For each prime $\mathfrak{p}$ of height one, $I_\mathfrak{p}$ is a nonzero finitely generated $A_\mathfrak{p}$-submodule of $K$, so $I_\mathfrak{p} = t_\mathfrak{p}^{-n_\mathfrak{p}}A_\mathfrak{p}$ for a unique integer $n_\mathfrak{p} = -\min_i v_\mathfrak{p}(a_i)$, where $a_1, \dots, a_r$ generate $I$. Only finitely many $n_\mathfrak{p}$ are nonzero, since each $a_i$ has only finitely many nonzero valuations by Theorem P1.8.2. Put $D = \sum n_\mathfrak{p}[\mathfrak{p}]$. By the theorem on reflexive modules and (1), $I = \bigcap I_\mathfrak{p} = \bigcap A(D)_\mathfrak{p} = A(D)$.

(3) An $A$-linear map between fractional ideals $I \to J$ is multiplication by an element of $K$, since it extends to a $K$-linear map $K \to K$. For $f \in K^*$, $fA(D) = A(D - \operatorname{div}(f))$ by the definition. So an isomorphism $A(D) \cong A(D')$ is multiplication by some $f$ with $A(D') = A(D - \operatorname{div}(f))$, and comparing localizations at the primes of height one gives $D' = D - \operatorname{div}(f)$. Conversely, $D' = D - \operatorname{div}(f)$ gives $A(D') = fA(D) \cong A(D)$. If $A(D)$ is invertible, then it is locally principal by Proposition P1.8.18, so at each maximal ideal $\mathfrak{m}$, $A(D)A_\mathfrak{m} = gA_\mathfrak{m}$, and comparing localizations at the primes of height one inside $\mathfrak{m}$ gives $D = -\operatorname{div}(g)$ near $\mathfrak{m}$, so $D$ is Cartier. Conversely, if $D = -\operatorname{div}(g)$ near each $\mathfrak{m}$, then $A(D)_\mathfrak{m} = A_\mathfrak{m}(D) = gA_\mathfrak{m}$, since $A(D)_\mathfrak{m}$ is the divisorial ideal of $D$ over $A_\mathfrak{m}$ by (1) and the theorem on reflexive modules, and $A(D)$ is invertible by Proposition P1.8.18. $\square$

For divisors $D$ and $E$ the reflexive hull of the product is $(A(D) \otimes_A A(E))^{**} \cong A(D + E)$ (Exercise 5). So the group law of $\operatorname{Cl}(A)$ is the reflexive tensor product. In the language of sheaves, $\mathcal{O}_X(D)$ is the reflexive sheaf of the divisor, and $\mathcal{O}_X(rD) = (\mathcal{O}_X(D)^{\otimes r})^{**}$ is its *reflexive power*. A divisor $D$ is $\mathbb{Q}$-Cartier if and only if some reflexive power $\mathcal{O}_X(rD)$ with $r \geq 1$ is invertible.

### Proof in words

A module over a normal domain is reflexive when it is determined by its behaviour at the prime divisors: an element of the generic fibre that is integral at every prime divisor is in the module. Duals have this property because the ring has it, by Hartogs, and modules over a DVR are free, so the double dual agrees with the module in codimension one and is the intersection of its localizations there. The same Hartogs argument gives depth two in codimension at least two. In rank one, the localizations at the prime divisors are powers of the uniformizers, and their exponents form a Weil divisor, so reflexive modules of rank one are the same as divisor classes.

### Examples

**Example P1.11.25 (the maximal ideal of the plane).** Let $A = k[x, y]$ and $\mathfrak{m} = (x, y)$. Then $\mathfrak{m}_\mathfrak{p} = A_\mathfrak{p}$ for every prime of height one, since such a prime does not contain $\mathfrak{m}$, so $\bigcap \mathfrak{m}_\mathfrak{p} = A \neq \mathfrak{m}$. So $\mathfrak{m}$ is torsion-free but not reflexive, and $\mathfrak{m}^{**} = A$. Its dual is $\mathfrak{m}^* = (A : \mathfrak{m}) = A$ by Example P1.8.6. The module $\mathfrak{m}$ has depth $1$ at the origin, since $A/\mathfrak{m}$ has depth $0$ and $A$ has depth $2$.

**Example P1.11.26 (the quadric cone).** Let $A = k[x, y, z]/(xy - z^2)$ and $\mathfrak{p} = (x, z)$, the prime of the line on the cone, as in Example P1.8.8. Then $\mathfrak{p} = A(-[\mathfrak{p}])$ by Proposition P1.8.5, so $\mathfrak{p}$ is reflexive of rank one. It is not invertible, since $[\mathfrak{p}]$ generates $\operatorname{Cl}(A) = \mathbb{Z}/2$ and is not Cartier at the vertex (Example P1.8.22), and by the corollary it has depth $2$ at the vertex, so it is a maximal Cohen-Macaulay module that is not free. Its square is $\mathfrak{p}^2 = (x^2, xz, z^2) = (x^2, xz, xy) = x\mathfrak{m}$, with $\mathfrak{m} = (x, y, z)$, which is not reflexive, while its reflexive hull is $A(-2[\mathfrak{p}]) = xA$, since $\operatorname{div}(x) = 2[\mathfrak{p}]$ by Example P1.8.8. So $\mathfrak{p}^{(2)} = xA \neq \mathfrak{p}^2$.

**Example P1.11.27 (the canonical module).** For a normal variety $X$ with canonical divisor $K_X$, the sheaf $\omega_X = \mathcal{O}_X(K_X)$ is reflexive of rank one, and the sheaves $\mathcal{O}_X(mK_X)$ are its reflexive powers. On the cone over the twisted cubic, $K_X$ is not Cartier at the vertex by Section 10.3, and $\mathcal{O}_X(3K_X)$ is invertible near the vertex, so $\omega_X$ is a reflexive module that is not invertible while its third reflexive power is. The canonical ring $\bigoplus_{m \geq 0} H^0(X, \mathcal{O}_X(mK_X))$ of Volume 9 is a ring of sections of reflexive sheaves.

**Example P1.11.28 (sections and small modifications).** Let $X$ be normal and $U \subseteq X$ open with complement of codimension at least $2$. For a reflexive sheaf $\mathcal{F}$, the restriction $\mathcal{F}(X) \to \mathcal{F}(U)$ is bijective, by the theorem on reflexive modules on each affine open set. A flip $X \dashrightarrow X^+$ is an isomorphism between open sets with complements of codimension at least $2$, so it identifies $H^0(X, \mathcal{O}_X(D))$ with $H^0(X^+, \mathcal{O}_{X^+}(D^+))$ for the strict transform $D^+$ (Volume 8).

### Exercises

1. (A) Show that a finitely generated projective module over $A$ is reflexive.
2. (A) Show that $\operatorname{Hom}_A(M, N)$ is reflexive when $N$ is reflexive. (Hint: use the characterization by localizations at primes of height one.)
3. (A) Let $A$ be a Dedekind domain. Show that every finitely generated torsion-free $A$-module is reflexive.
4. (B) Let $A = k[x, y, z, w]/(xw - yz)$ and $\mathfrak{p} = (x, y)$, as in Example P1.8.15. Show that $\mathfrak{p}$ is reflexive and that the reflexive hull of $\mathfrak{p}^n$ is the symbolic power $\mathfrak{p}^{(n)}$. Show that $\mathfrak{p}^{(n)}$ is not principal for $n \geq 1$, and relate this to Example P1.8.23.
5. (B) Show that $(A(D) \otimes_A A(E))^{**} \cong A(D + E)$ and that $A(D)^* \cong A(-D)$. (Hint: compute both sides at the primes of height one.)
6. (C) Let $M$ be a finitely generated torsion-free module with $\operatorname{depth} M_\mathfrak{p} \geq 2$ for every prime $\mathfrak{p}$ of height at least $2$. Show that $M$ is reflexive. (Hint: let $w \in \bigcap M_\mathfrak{p}$ and $I = \{a \in A : aw \in M\}$; show that every prime containing $I$ has height at least $2$, show that $\operatorname{depth}_I(M) \geq 2$ as in the proof of the proposition on codimension two in Section 11.1, and conclude as in the proposition on depth two and extension, with $M$ in place of $A$.)
7. (C) Let $A$ be a normal local domain of dimension $2$ with maximal ideal $\mathfrak{m}$. Show that $\mathfrak{m}$ is not reflexive, and that $\mathfrak{m}^* = A$. Deduce that for every reflexive $M$ the module $\operatorname{Hom}_A(\mathfrak{m}, M)$ equals $M$.

### Lean

Mathlib defines the dual `Module.Dual`, the evaluation map `Module.Dual.eval` and reflexive modules `Module.IsReflexive`, and it proves that finitely generated projective modules are reflexive. The characterization over a normal domain by localizations at height one primes, the depth of reflexive modules and the description of the class group by reflexive modules of rank one are not in Mathlib. The handbook adds no `MinimalModel` node here.

### Notes and history

The divisorial ideals $A(D)$ go back to the theory of Krull domains, where the divisorial ideals of a Krull domain are exactly the intersections of their localizations at the height one primes, and Samuel's lecture notes of 1964 develop the class group in this language. Reflexive sheaves were studied in geometry by Hartshorne, whose paper of 1980 on stable reflexive sheaves treats reflexive sheaves of rank two on threefolds, and by Reid, who used reflexive powers of the canonical sheaf to define canonical and terminal singularities. The literature state of every result here is theorem. The section follows Matsumura, Chapter 4, and Eisenbud, Chapter 11.
