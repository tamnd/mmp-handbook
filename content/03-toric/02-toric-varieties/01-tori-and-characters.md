---
title: Tori, characters and one-parameter subgroups
nodes: []
sources: [CLS11, Ful93]
reads_with: [CLS11:ch1, Ful93:1.1]
requires: [P8.6, 3.1]
level: core
kind: background
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Tori, characters and one-parameter subgroups

### Statement

**Definition 3.2.1 (torus, characters, one-parameter subgroups).** Let $N \cong \mathbb{Z}^n$ be a lattice and $M = \operatorname{Hom}(N, \mathbb{Z})$. The *torus* of $N$ is the affine group variety $T_N = \operatorname{Spec} k[M]$, where $k[M] = \bigoplus_{m \in M} k \chi^m$ is the group algebra with $\chi^m \chi^{m'} = \chi^{m + m'}$. A choice of basis gives $k[M] = k[x_1^{\pm 1}, \dots, x_n^{\pm 1}]$ and $T_N \cong (k^*)^n$. A *character* of $T_N$ is a morphism of algebraic groups $T_N \to k^*$, and a *one-parameter subgroup* is a morphism of algebraic groups $k^* \to T_N$. For $m \in M$ the function $\chi^m$ is a character. For $u \in N$ let $\lambda^u \colon k^* \to T_N$ be the morphism with $\chi^m(\lambda^u(t)) = t^{\langle m, u \rangle}$.

**Proposition 3.2.2 (the two lattices).** The maps $m \mapsto \chi^m$ and $u \mapsto \lambda^u$ are isomorphisms of groups from $M$ to the characters of $T_N$ and from $N$ to the one-parameter subgroups of $T_N$. For $m \in M$ and $u \in N$ the composite $\chi^m \circ \lambda^u$ is the character $t \mapsto t^{\langle m, u \rangle}$ of $k^*$. Also $T_N = N \otimes_{\mathbb{Z}} k^*$, with $u \otimes t = \lambda^u(t)$.

Lean: not yet in Lean.

**Definition 3.2.3 (toric variety).** A *toric variety* is a variety $X$ with an open subset isomorphic to a torus $T_N$, such that the action of $T_N$ on itself by multiplication extends to an algebraic action $T_N \times X \to X$. It is *affine* when $X$ is affine.

**Definition 3.2.4 (the variety of a set of characters).** Let $\mathcal{A} = \{m_1, \dots, m_s\} \subset M$ be a finite set. Let $\Phi_{\mathcal{A}} \colon T_N \to k^s$ be the morphism $t \mapsto (\chi^{m_1}(t), \dots, \chi^{m_s}(t))$. The variety $Y_{\mathcal{A}}$ is the Zariski closure of the image of $\Phi_{\mathcal{A}}$ in $\mathbb{A}^s$.

**Proposition 3.2.5 (affine toric varieties from semigroups).** Let $\mathcal{A} \subset M$ be finite, let $\mathbb{N}\mathcal{A}$ be the semigroup that it generates and $\mathbb{Z}\mathcal{A}$ the group that it generates.

1. $Y_{\mathcal{A}}$ is an affine toric variety. Its coordinate ring is the semigroup algebra $k[\mathbb{N}\mathcal{A}] \subset k[M]$, its torus is the torus with character lattice $\mathbb{Z}\mathcal{A}$, and its dimension is the rank of $\mathbb{Z}\mathcal{A}$.
2. The ideal of $Y_{\mathcal{A}}$ in $k[x_1, \dots, x_s]$ is spanned by the binomials $x^\alpha - x^\beta$ with $\alpha, \beta \in \mathbb{N}^s$ and $\sum_i \alpha_i m_i = \sum_i \beta_i m_i$.
3. Every affine toric variety is isomorphic to some $Y_{\mathcal{A}}$, and so to $\operatorname{Spec} k[S]$ for a finitely generated semigroup $S$ in a lattice that $S$ generates as a group.

Lean: not yet in Lean.

### Proof in words

A character is a unit of $k[M]$ that is compatible with the group law. The units of a Laurent polynomial ring are the monomials $c \chi^m$ with $c \in k^*$, because the product of two Laurent polynomials has as leading and trailing terms the products of the leading and trailing terms, for any monomial order. Compatibility with the group law means $\chi(1) = 1$, so $c = 1$. The same argument for $k[t^{\pm 1}]$ shows that a one-parameter subgroup is given by $n$ integers, which form a vector $u \in N$.

For Proposition 3.2.5, the map $k[x_1, \dots, x_s] \to k[M]$, $x_i \mapsto \chi^{m_i}$, is the comorphism of $\Phi_{\mathcal{A}}$. Its image is $k[\mathbb{N}\mathcal{A}]$, and its kernel is the ideal of the closure of the image, which is $Y_{\mathcal{A}}$. The kernel is spanned by binomials because $k[M]$ is graded by $M$ with one-dimensional pieces: a polynomial maps to zero exactly when the coefficients of the monomials of each degree $m \in M$ sum to zero. The torus $T' = \operatorname{Spec} k[\mathbb{Z}\mathcal{A}]$ is the image of $\Phi_{\mathcal{A}}$, it is the open set of $Y_{\mathcal{A}}$ where all $x_i$ are nonzero, and its multiplication extends to $Y_{\mathcal{A}}$ through the comorphism $\chi^m \mapsto \chi^m \otimes \chi^m$. Part 3 is cited without proof (Cox-Little-Schenck, Chapter 1): a finite set of eigenfunctions of the torus that generates the coordinate ring gives the embedding.

### Examples

**Example 3.2.6 (affine space and the torus).** For $\mathcal{A} = \{e_1^*, \dots, e_n^*\}$ the semigroup is $\mathbb{N}^n$ and $Y_{\mathcal{A}} = \mathbb{A}^n$. For $\mathcal{A} = \{\pm e_1^*, \dots, \pm e_n^*\}$, $Y_{\mathcal{A}}$ is the closed subvariety $x_i y_i = 1$ of $\mathbb{A}^{2n}$, which is the torus $(k^*)^n$ itself. For $u = (a_1, \dots, a_n) \in N$ the one-parameter subgroup is $\lambda^u(t) = (t^{a_1}, \dots, t^{a_n})$.

**Example 3.2.7 (the quadric cone).** Let $M = \mathbb{Z}^2$ and $\mathcal{A} = \{(1,0), (1,1), (1,2)\}$. Then $\Phi_{\mathcal{A}}(s, t) = (s, st, st^2)$, and the only relation is $(1,0) + (1,2) = 2 \cdot (1,1)$. So $Y_{\mathcal{A}}$ is the quadric cone $xz = y^2$ in $\mathbb{A}^3$. The group $\mathbb{Z}\mathcal{A}$ is all of $\mathbb{Z}^2$, so the torus is $(k^*)^2$, embedded as the set $xyz \neq 0$. More generally, $\mathcal{A} = \{(1, j) : 0 \le j \le n\}$ gives the cone over the rational normal curve of degree $n$ in $\mathbb{A}^{n+1}$. Its ideal is generated by the $2 \times 2$ minors of the matrix with rows $(x_0, \dots, x_{n-1})$ and $(x_1, \dots, x_n)$. Section 2 shows that this is the affine toric variety of the cone $\sigma_n$ of Example 3.1.6.

**Example 3.2.8 (the cuspidal cubic is toric and not normal).** Let $M = \mathbb{Z}$ and $\mathcal{A} = \{2, 3\}$. Then $\Phi_{\mathcal{A}}(t) = (t^2, t^3)$ and $Y_{\mathcal{A}}$ is the cuspidal cubic $y^2 = x^3$. Its coordinate ring is $k[t^2, t^3]$, and $\mathbb{N}\mathcal{A} = \{0, 2, 3, 4, \dots\}$. The element $t = t^3 / t^2$ of the fraction field is integral over $k[t^2, t^3]$, as a root of $T^2 - t^2$, and it is not in the ring. So $Y_{\mathcal{A}}$ is a toric variety that is not normal. The failure is that $\mathbb{N}\mathcal{A}$ is not saturated in $\mathbb{Z}\mathcal{A} = \mathbb{Z}$: the element $1$ has the multiple $2 \in \mathbb{N}\mathcal{A}$ but is not in $\mathbb{N}\mathcal{A}$. The toric varieties of fans are normal, and they never have this kind of singularity.

**Example 3.2.9 (the lattice of the torus can change).** Let $M = \mathbb{Z}$ and $\mathcal{A} = \{2\}$. Then $Y_{\mathcal{A}} = \mathbb{A}^1$, but its torus has character lattice $2\mathbb{Z}$, not $\mathbb{Z}$. The map $\Phi_{\mathcal{A}} \colon k^* \to k^*$ is $t \mapsto t^2$, which is not an isomorphism: in characteristic not 2 it has kernel $\{\pm 1\}$, and in characteristic 2 it is bijective on points but its comorphism $k[s^{\pm 1}] \to k[t^{\pm 1}]$, $s \mapsto t^2$, is not surjective. This is why part 1 of Proposition 3.2.5 names the lattice $\mathbb{Z}\mathcal{A}$.

### Exercises

1. (A) Find the binomial ideal of $Y_{\mathcal{A}}$ for $\mathcal{A} = \{(1,0), (1,1), (1,2), (1,3)\}$, and check that it is generated by three quadrics.
2. (A) Show that $\chi^m \circ \lambda^u$ is $t \mapsto t^{\langle m, u \rangle}$, and that $\lambda^u$ is injective if and only if $u$ is primitive or, in characteristic $p > 0$, $u$ is $p^e$ times a primitive vector.
3. (B) Prove that the units of $k[x_1^{\pm 1}, \dots, x_n^{\pm 1}]$ are the elements $c x^a$ with $c \in k^*$ and $a \in \mathbb{Z}^n$.
4. (B) Let $\mathcal{A} = \{3, 5\} \subset \mathbb{Z}$. Find the equation of $Y_{\mathcal{A}}$, show that it is not normal, and show that its normalization is $\mathbb{A}^1 = \operatorname{Spec} k[t]$.

### Lean

- Status: not yet in Lean. The Lean library works with the lattice $\mathbb{Z}^n$ inside $\mathbb{R}^n$ (`MinimalModel.Toric.NR`, `MinimalModel.Toric.toNR`). It has no torus, no characters and no varieties $Y_{\mathcal{A}}$ yet.
- Fidelity: in Lean the lattice $N$ is always $\mathbb{Z}^n$ with its standard basis, and the dual lattice $M$ does not appear yet.
- No node of the map covers this section.

### Notes and history

The name "toric variety" comes from the torus $T_N$, which is called an algebraic torus because $(\mathbb{C}^*)^n$ retracts onto the compact torus $(S^1)^n$. The first systematic treatments are Demazure (1970), who used fans to study the Cremona group, and Kempf, Knudsen, Mumford and Saint-Donat (1973), who used them for toroidal embeddings and semistable reduction. The varieties $Y_{\mathcal{A}}$ and their binomial ideals are the subject of Sturmfels, *Gröbner bases and convex polytopes*, and of Cox-Little-Schenck, Chapter 1. Some authors require a toric variety to be normal; this handbook does not, so that the cuspidal cubic of Example 3.2.8 is an example.
