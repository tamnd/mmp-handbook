---
title: Double complexes
nodes: []
sources: [Wei94, Har77]
reads_with: [Wei94:ch5, Har77:ch3]
requires: [P2.3, P2.4]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Double complexes

### Statement

Throughout, $\mathcal{A}$ is an abelian category.

**Definition P2.4.13 (double complex).** A *first quadrant double complex* $C$ in $\mathcal{A}$ is a family of objects $C^{p,q}$, $p, q \geq 0$, with maps $d_h: C^{p,q} \to C^{p+1,q}$ and $d_v: C^{p,q} \to C^{p,q+1}$ such that
$$d_h d_h = 0, \qquad d_v d_v = 0, \qquad d_h d_v + d_v d_h = 0.$$
The *columns* are the complexes $C^{p,\bullet}$ with differential $d_v$, and the *rows* are the complexes $C^{\bullet,q}$ with differential $d_h$. Write $H_v^q(C^{p,\bullet})$ and $H_h^p(C^{\bullet,q})$ for their cohomology.

Many double complexes arise with commuting squares, $d_h d_v = d_v d_h$, for example $\operatorname{Hom}(P_p, I^q)$ for complexes $P_\bullet$ and $I^\bullet$. Replacing $d_v$ by $(-1)^p d_v$ on the column $p$ gives anticommuting squares. This does not change the kernels or images of $d_v$, so the cohomology of rows and columns is the same.

**Definition P2.4.14 (total complex).** The *total complex* of a first quadrant double complex $C$ is the complex $\operatorname{Tot}(C)$ with
$$\operatorname{Tot}(C)^n = \bigoplus_{p+q=n} C^{p,q}, \qquad d = d_h + d_v.$$
The sum is finite, and $d d = d_h d_h + (d_h d_v + d_v d_h) + d_v d_v = 0$.

Lean: Mathlib `HomologicalComplex₂` (a complex of complexes, with commuting squares) and `HomologicalComplex₂.total`, which inserts the signs; `HomologicalComplex₂.flip` exchanges the two directions.

**Theorem P2.4.15 (the two spectral sequences of a double complex).** Let $C$ be a first quadrant double complex. There are two convergent first quadrant spectral sequences
$$ {}^{I}E_2^{p,q} = H_h^p H_v^q(C) \Rightarrow H^{p+q}(\operatorname{Tot} C), \qquad {}^{II}E_2^{p,q} = H_v^p H_h^q(C) \Rightarrow H^{p+q}(\operatorname{Tot} C).$$
In the first, ${}^{I}E_1^{p,q} = H_v^q(C^{p,\bullet})$ and $d_1$ is induced by $d_h$; so ${}^{I}E_2^{p,q}$ is the cohomology in degree $p$ of the complex $H_v^q(C^{\bullet,\bullet})$ with the maps induced by $d_h$. In the second, ${}^{II}E_1^{p,q} = H_h^q(C^{\bullet,p})$ and $d_1$ is induced by $d_v$. Both are functorial for maps of double complexes.

Lean: not in Lean as stated.

**Corollary P2.4.16 (exact rows).** Let $C$ be a first quadrant double complex whose rows are exact in positive degrees: $H_h^p(C^{\bullet,q}) = 0$ for all $p > 0$ and all $q$. Let $K^q = \ker(d_h: C^{0,q} \to C^{1,q})$, a complex with the differential induced by $d_v$. Then the inclusion $K^\bullet \to \operatorname{Tot}(C)$, through $K^n \subseteq C^{0,n}$, is a quasi-isomorphism. The same holds with rows and columns exchanged.

Lean: not in Lean as stated.

In particular, if all rows of $C$ are exact, or all columns are exact, then $\operatorname{Tot}(C)$ is exact. This is the *acyclic assembly lemma* for first quadrant double complexes.

**Corollary P2.4.17 (balance of Ext by a double complex).** Let $M$ and $N$ be objects of $\mathcal{A}$, let $P_\bullet \to M$ be a projective resolution and $N \to I^\bullet$ an injective resolution. Then the complexes $\operatorname{Hom}(P_\bullet, N)$ and $\operatorname{Hom}(M, I^\bullet)$ have isomorphic cohomology. Both are quasi-isomorphic to $\operatorname{Tot}$ of the double complex $\operatorname{Hom}(P_p, I^q)$.

Lean: not in Lean as stated.

Section 3.4 proved the same balance with $\delta$-functors. The double complex proof is the one that generalizes: it is the model for the Grothendieck spectral sequence of Section 4.3 and for the total derived functors of Chapter 8.

### Proof in words

A double complex has two natural filtrations of its total complex: by columns and by rows. Each gives a filtered complex as in Section 4.1. The graded pieces of the column filtration are the columns, so page $1$ is the vertical cohomology, and page $2$ takes the horizontal cohomology of that. The row filtration does the same in the other order. Both spectral sequences converge to the same object, the cohomology of the total complex. So information flows from one order of taking cohomology to the other.

The two corollaries are the most frequent use. If the rows are exact away from the first column, the row spectral sequence has one row on page $2$, and the cohomology of the total complex is the cohomology of that column of kernels. When the columns are also exact away from the bottom row, the total complex is a bridge between two different complexes, and their cohomology agrees. For $\operatorname{Hom}(P_p, I^q)$, the rows are exact because $\operatorname{Hom}(-, I^q)$ is exact, and the columns are exact because $\operatorname{Hom}(P_p, -)$ is exact.

### Examples

**Example P2.4.18 (two spectral sequences with different pages).** Let $k$ be a field, $C^{0,0} = C^{1,0} = k$, all other $C^{p,q} = 0$, and $d_h = 0$. Then $\operatorname{Tot}(C)$ is $k$ in degree $0$ and $k$ in degree $1$, with zero differential. The column spectral sequence has ${}^{I}E_2^{0,0} = k$ and ${}^{I}E_2^{1,0} = k$. The row spectral sequence has ${}^{II}E_1^{p,q} = H_h^q(C^{\bullet,p})$, so ${}^{II}E_2^{0,0} = k$ and ${}^{II}E_2^{0,1} = k$. The class in degree $1$ sits in filtration degree $1$ for the first and in filtration degree $0$ for the second. The two filtrations of $H^1(\operatorname{Tot} C)$ are different, but the limit is the same.

**Example P2.4.19 (Ext of cyclic groups).** Over $\mathbb{Z}$, let $M = \mathbb{Z}/n$ with the projective resolution $0 \to \mathbb{Z} \xrightarrow{n} \mathbb{Z}$, and $N = \mathbb{Z}/m$ with the injective resolution $\mathbb{Q}/\mathbb{Z} \xrightarrow{m} \mathbb{Q}/\mathbb{Z} \to 0$. The kernel of multiplication by $m$ on $\mathbb{Q}/\mathbb{Z}$ is $\frac{1}{m}\mathbb{Z}/\mathbb{Z} \cong \mathbb{Z}/m$, so this is a resolution. The double complex $\operatorname{Hom}(P_p, I^q)$ is the square with four copies of $\mathbb{Q}/\mathbb{Z}$, the horizontal maps multiplication by $n$ and the vertical maps multiplication by $\pm m$. The columns have $H_v^0 = \mathbb{Z}/m$ and $H_v^1 = 0$. So ${}^{I}E_2$ is the cohomology of $\mathbb{Z}/m \xrightarrow{n} \mathbb{Z}/m$, which is $\mathbb{Z}/d$ in degrees $0$ and $1$, with $d = \gcd(m,n)$. This gives $\operatorname{Hom}(\mathbb{Z}/n, \mathbb{Z}/m) \cong \mathbb{Z}/d$ and $\operatorname{Ext}^1(\mathbb{Z}/n, \mathbb{Z}/m) \cong \mathbb{Z}/d$, as in Section 3.4.

**Example P2.4.20 (Čech cohomology and sheaf cohomology).** Let $X$ be a topological space, $\mathcal{U} = (U_i)$ an open cover, $\mathcal{F}$ a sheaf of abelian groups with an injective resolution $\mathcal{F} \to \mathcal{I}^\bullet$. The Čech complexes form a double complex $C^{p,q} = \check{C}^p(\mathcal{U}, \mathcal{I}^q)$. Chapter 7 proves that the Čech complex of an injective sheaf is exact in positive degrees, with $H^0 = \Gamma(X, \mathcal{I}^q)$. So by the corollary, $\operatorname{Tot}(C)$ computes $H^n(\Gamma(X, \mathcal{I}^\bullet)) = H^n(X, \mathcal{F})$. The column $p$ has cohomology $\prod H^q(U_{i_0 \cdots i_p}, \mathcal{F})$, where $U_{i_0 \cdots i_p} = U_{i_0} \cap \cdots \cap U_{i_p}$. So the other spectral sequence is
$$E_2^{p,q} = \check{H}^p(\mathcal{U}, \underline{H}^q(\mathcal{F})) \Rightarrow H^{p+q}(X, \mathcal{F}),$$
where $\underline{H}^q(\mathcal{F})$ is the presheaf $U \mapsto H^q(U, \mathcal{F})$. If $\mathcal{F}$ has no higher cohomology on any finite intersection $U_{i_0 \cdots i_p}$, only the row $q = 0$ survives, and Čech cohomology computes sheaf cohomology. On a separated scheme with an affine cover and $\mathcal{F}$ quasi-coherent, this is the case by P4 Ch. 1. The standard computation of $H^i(\mathbb{P}^n, \mathcal{O}(d))$ by Čech cochains rests on this fact.

### Proof

*Proof of the theorem.* Filter $\operatorname{Tot}(C)$ by columns: ${}^{I}F^p \operatorname{Tot}(C)^n = \bigoplus_{i \geq p} C^{i, n-i}$. The differential $d_h$ raises $i$ and $d_v$ keeps it, so each ${}^{I}F^p$ is a subcomplex. Since $C$ is first quadrant, ${}^{I}F^0 \operatorname{Tot}^n = \operatorname{Tot}^n$ and ${}^{I}F^{n+1} \operatorname{Tot}^n = 0$, so the filtration is first quadrant. The graded piece $\operatorname{gr}^p \operatorname{Tot}(C)$ is the column $C^{p,\bullet}$, placed so that $C^{p,q}$ sits in degree $p + q$, with differential $d_v$. The theorem of Section 4.1 gives a convergent spectral sequence with ${}^{I}E_1^{p,q} = H^{p+q}(\operatorname{gr}^p) = H_v^q(C^{p,\bullet})$.

The map $d_1$ is the connecting map of $0 \to \operatorname{gr}^{p+1} \to {}^{I}F^p / {}^{I}F^{p+2} \to \operatorname{gr}^p \to 0$. To compute it, take $x \in C^{p,q}$ with $d_v x = 0$. It lifts to $x \in {}^{I}F^p / {}^{I}F^{p+2}$, and $dx = d_h x + d_v x = d_h x \in C^{p+1,q}$. So $d_1$ sends the class of $x$ to the class of $d_h x$, and ${}^{I}E_2^{p,q} = H_h^p H_v^q(C)$.

For the second spectral sequence, apply the first to the *transpose* $C^t$, with $(C^t)^{p,q} = C^{q,p}$ and the roles of $d_h$ and $d_v$ exchanged. It is again a first quadrant double complex with anticommuting squares, and $\operatorname{Tot}(C^t) = \operatorname{Tot}(C)$ with the same differential. Functoriality follows from the functoriality in Section 4.1, since a map of double complexes respects both filtrations. $\square$

*Proof of the corollary on exact rows.* First check that $K^\bullet$ is a complex and that the inclusion is a map of complexes. For $x \in K^q$, $d_h d_v x = - d_v d_h x = 0$, so $d_v x \in K^{q+1}$. In $\operatorname{Tot}(C)$, $dx = d_h x + d_v x = d_v x$. So $K^\bullet \to \operatorname{Tot}(C)$ commutes with the differentials.

Filter $K^\bullet$ by $F^p K^n = K^n$ for $n \geq p$ and $F^p K^n = 0$ for $n < p$, and $\operatorname{Tot}(C)$ by rows, ${}^{II}F^p \operatorname{Tot}(C)^n = \bigoplus_{j \geq p} C^{n-j,j}$. Since $K^n \subseteq C^{0,n} \subseteq {}^{II}F^n \operatorname{Tot}^n$, the inclusion is a map of filtered complexes. On page $1$, the filtered complex $K^\bullet$ gives $E_1^{p,0} = K^p$ and $E_1^{p,q} = 0$ for $q \neq 0$. The row filtration gives ${}^{II}E_1^{p,q} = H_h^q(C^{\bullet,p})$, which is $K^p$ for $q = 0$ and zero for $q > 0$ by the assumption. The map between them is the identity of $K^p$ on the row $q = 0$. So the map is an isomorphism on page $1$, and the comparison proposition of Section 4.1 shows that it is an isomorphism on cohomology. The exchanged statement follows by applying this to the transpose. $\square$

*Proof of the corollary on balance.* Replace the vertical maps of $\operatorname{Hom}(P_p, I^q)$ by $(-1)^p$ times themselves, to obtain anticommuting squares. Each row $q \mapsto \operatorname{Hom}(P_\bullet, I^q)$ is $\operatorname{Hom}(-, I^q)$ applied to the exact sequence $\cdots \to P_1 \to P_0 \to M \to 0$. Since $I^q$ is injective, $\operatorname{Hom}(-, I^q)$ is exact, so the row is exact in positive degrees with kernel $\operatorname{Hom}(M, I^q)$ in degree $0$. The corollary on exact rows gives a quasi-isomorphism $\operatorname{Hom}(M, I^\bullet) \to \operatorname{Tot}$. Each column $\operatorname{Hom}(P_p, I^\bullet)$ is $\operatorname{Hom}(P_p, -)$ applied to the exact sequence $0 \to N \to I^0 \to I^1 \to \cdots$. Since $P_p$ is projective, the column is exact in positive degrees, with kernel $\operatorname{Hom}(P_p, N)$ in degree $0$. The exchanged corollary gives a quasi-isomorphism $\operatorname{Hom}(P_\bullet, N) \to \operatorname{Tot}$. The signs $(-1)^p$ do not change the kernels of the vertical maps, and the horizontal maps are unchanged, so this complex is $\operatorname{Hom}(P_\bullet, N)$ with its usual differential. $\square$

### Exercises

1. (A) Let $C$ have commuting squares. Show that $\operatorname{Tot}(C)$ with $d = d_h + d_v$ is not a complex in general, and that $d = d_h + (-1)^p d_v$ on $C^{p,q}$ is a differential.
2. (A) Let $f: C \to D$ be a map of first quadrant double complexes such that each column map $C^{p,\bullet} \to D^{p,\bullet}$ is a quasi-isomorphism. Show that $\operatorname{Tot}(f)$ is a quasi-isomorphism.
3. (A) Compute $\operatorname{Ext}^i_{\mathbb{Z}}(\mathbb{Z}/n, \mathbb{Z})$ with both spectral sequences of the double complex $\operatorname{Hom}(P_p, I^q)$, where $P$ is $\mathbb{Z} \xrightarrow{n} \mathbb{Z}$ and $I$ is $\mathbb{Q} \to \mathbb{Q}/\mathbb{Z}$.
4. (B) State the corollary on exact rows for first quadrant homological double complexes $C_{p,q}$, with differentials of degree $-1$. Prove that $\operatorname{Tor}$ can be computed by a projective resolution of either variable, using the double complex $P_p \otimes Q_q$.
5. (B) Let $k$ be a field and $K^\bullet$, $L^\bullet$ complexes of $k$-vector spaces, zero in negative degrees. Show that $H^n(\operatorname{Tot}(K^\bullet \otimes L^\bullet)) \cong \bigoplus_{p+q=n} H^p(K) \otimes H^q(L)$. (Hint: compute the column spectral sequence, then reduce to the case where $K$ has zero differential with the comparison proposition.)
6. (B) Using the facts from Chapter 7 quoted in the example on Čech cohomology, show that $\check{H}^1(\mathcal{U}, \mathcal{F}) \to H^1(X, \mathcal{F})$ is a monomorphism for every cover, and that $\check{H}^p(\mathcal{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$ for all $p$ when $H^q(U_{i_0 \cdots i_p}, \mathcal{F}) = 0$ for all $q > 0$ and all finite intersections.
7. (C) The first quadrant hypothesis matters. Let $k$ be a field and define $C^{-i,i} = C^{-i,i+1} = k$ for $i \geq 0$, and $C^{p,q} = 0$ otherwise. Let $d_v: C^{-i,i} \to C^{-i,i+1}$ and $d_h: C^{-i,i} \to C^{-i+1,i}$ be the identity of $k$ for $i \geq 1$, and $d_v$ the identity for $i = 0$. Show that all columns are exact. Show that the complex $\prod_{p+q=n} C^{p,q}$ has $H^0 \cong k$, and that the complex $\bigoplus_{p+q=n} C^{p,q}$ is exact. Which row is not exact?

### Lean

Mathlib models a double complex as `HomologicalComplex₂`, a complex of complexes, so its squares commute. The total complex `HomologicalComplex₂.total` exists for a general pair of complex shapes and inserts the signs given by a `TotalComplexShape`. The transpose is `HomologicalComplex₂.flip`, and `HomologicalComplex₂.totalFlipIso` identifies the total complex of the flip with the total complex of $K$. The two spectral sequences, the corollary on exact rows and the balance of $\operatorname{Ext}$ by a double complex are not yet in this form. The handbook adds no `MinimalModel` node here.

### Notes and history

Double complexes and their two spectral sequences are in Cartan and Eilenberg's book of 1956, where they give the balance of the derived functors of the tensor product and of $\operatorname{Hom}$. Grothendieck's Tohoku paper of 1957 used them for the comparison of Čech cohomology with derived functor cohomology. Weibel, Chapter 5, discusses the convergence problems outside the first quadrant, of which Exercise 7 is the basic example.
