---
title: Circuits and the type of a contraction
nodes: []
sources: [CLS11, Rei83, FS04, Har77]
reads_with: [CLS11:ch15, Rei83:1]
requires: [3.1, 3.2, 3.3, 3.4]
level: core
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## Circuits and the type of a contraction

### Statement

A birational contraction changes the fan only inside a few cones, and each of these cones has a simple shape: it is spanned by $n + 1$ vectors with one linear relation. This section studies such cones, proves that they have exactly two natural triangulations, and uses them to decide whether a contraction is divisorial or small.

**Definition 3.5.10 (circuit data).** *Circuit data* in $N_{\mathbb{R}} \cong \mathbb{R}^n$ is a set $W = \{w_0, \dots, w_n\}$ of $n + 1$ primitive vectors of $N$ that span $N_{\mathbb{R}}$, together with a nonzero relation $\sum_i q_i w_i = 0$, $q \in \mathbb{Q}^{W}$. The relation is unique up to a factor, since the relations form a space of dimension $(n + 1) - n = 1$. Put

$$J_+ = \{i : q_i > 0\}, \qquad J_0 = \{i : q_i = 0\}, \qquad J_- = \{i : q_i < 0\},$$

and let $Z = \{w_i : q_i \neq 0\}$ be the *circuit* of $W$. We assume $J_+ \neq \emptyset$ and $J_- \neq \emptyset$. For $A \subset W$, $\operatorname{Cone}(A)$ is the cone it spans. Let $T_+$ be the set of the cones $\operatorname{Cone}(A)$ for the subsets $A \subset W$ that do not contain all of $\{w_j : j \in J_+\}$, and $T_-$ the same with $J_-$. The maximal cones of $T_\pm$ are $\operatorname{Cone}(W \setminus \{w_j\})$ with $j \in J_\pm$.

**Lemma 3.5.11 (the two triangulations).** Let $(W, q)$ be circuit data.

1. For each $i$ with $q_i \neq 0$, $W \setminus \{w_i\}$ is a basis of $N_{\mathbb{R}}$. The vectors of $Z$ span a space of dimension $|Z| - 1$, and the vectors $w_i$ with $q_i = 0$ map to a basis of $N_{\mathbb{R}} / \operatorname{span}(Z)$.
2. The cone $\operatorname{Cone}(W)$ is strongly convex.
3. $T_+$ and $T_-$ are simplicial fans whose support is $\operatorname{Cone}(W)$.
4. The walls of $T_+$ that lie in two of its maximal cones are the cones $\operatorname{Cone}(W \setminus \{w_j, w_{j'}\})$ with $j \neq j'$ in $J_+$, and the wall relation of each of them (Theorem 3.4.5) is a positive multiple of $q$. For $T_-$ the walls are $\operatorname{Cone}(W \setminus \{w_k, w_{k'}\})$ with $k \neq k'$ in $J_-$, and the wall relation is a positive multiple of $-q$.

Lean: not yet in Lean.

**Proposition 3.5.12 (the faces of a circuit cone).** Let $(W, q)$ be circuit data and $B = \{w_i : q_i = 0\}$. The proper faces of $\operatorname{Cone}(W)$ are of two kinds:

1. the cones $\operatorname{Cone}(A)$ with $A \subset W$ such that $A$ misses some $w_j$ with $j \in J_+$ and some $w_k$ with $k \in J_-$;
2. the cones $\operatorname{Cone}(Z \cup B')$ with $B' \subsetneq B$.

For a face $\operatorname{Cone}(A)$ of the first kind, $A$ is the set of vectors of $W$ in it. The cones of the first kind are exactly the cones of $T_+ \cap T_-$, so $T_+$ and $T_-$ agree on every face of $\operatorname{Cone}(W)$ that does not contain $Z$. Every face of $\operatorname{Cone}(W)$ that contains all $w_k$ with $k \in J_-$ contains $Z$, so the smallest face that contains $\sigma_- = \operatorname{Cone}(w_k : k \in J_-)$ is $\operatorname{Cone}(Z)$, which is $\operatorname{Cone}(W)$ itself when $J_0 = \emptyset$.

Lean: not yet in Lean.

**Proposition 3.5.13 (multiplicities).** Let $(W, q)$ be circuit data such that $W$ generates the lattice $N$ and $q \in \mathbb{Z}^W$ is primitive. Then $N \cong \mathbb{Z}^W / \mathbb{Z} q$, with $w_i$ the image of the $i$-th basis vector, and for $q_j \neq 0$

$$\operatorname{mult} \operatorname{Cone}(W \setminus \{w_j\}) = |q_j|.$$

Lean: not yet in Lean.

**Theorem 3.5.14 (the local contraction).** Let $(W, q)$ be circuit data, $U = U_{\operatorname{Cone}(W)}$, and $X_\pm = X_{T_\pm}$. The identity of $N$ gives proper birational toric morphisms $\pi_\pm \colon X_\pm \to U$.

1. $\pi_+$ is an isomorphism over $U \setminus V_U(\operatorname{Cone}(Z))$, and $\pi_+^{-1}(V_U(\operatorname{Cone}(Z))) = V_+(\sigma_-)$ with $\sigma_- = \operatorname{Cone}(w_k : k \in J_-)$. This set has dimension $n - |J_-|$, and $\pi_+$ maps it onto $V_U(\operatorname{Cone}(Z))$, of dimension $n - |Z| + 1$, with fibres of dimension at least $|J_+| - 1$ everywhere.
2. If $|J_+| \ge 2$, the exceptional locus of $\pi_+$ is $V_+(\sigma_-)$. If $|J_+| = 1$, $T_+$ is the fan of one simplicial cone and $\pi_+$ is an isomorphism.
3. The same holds for $\pi_-$ with $J_+$ and $J_-$ exchanged.
4. $X_+ \setminus V_+(\sigma_-)$ and $X_- \setminus V_-(\sigma_+)$, with $\sigma_+ = \operatorname{Cone}(w_j : j \in J_+)$, are the same open subset $X_{T_+ \cap T_-}$ of both.

So if $|J_-| = 1$, then $X_- = U$ and $\pi_+$ is a divisorial contraction with exceptional divisor $D_{w_k}$. If $|J_+| \ge 2$ and $|J_-| \ge 2$, both $\pi_+$ and $\pi_-$ are small, and $X_+$ and $X_-$ are isomorphic in codimension one.

Lean: not yet in Lean.

**Theorem 3.5.15 (the structure of an extremal contraction).** Let $\Sigma$ be complete simplicial with $X = X_\Sigma$ projective, $R$ an extremal ray with $J_- \neq \emptyset$, $b^R$ its relation (Lemma 3.5.2), $Z = \{u_\rho : \rho \in J_+ \cup J_-\}$, and $\pi = \pi_R \colon X \to Z_R = X_{\Sigma_R}$ its contraction (Theorem 3.5.6).

1. Each maximal cone $C$ of $\Sigma_R$ is either a maximal cone of $\Sigma$ none of whose walls is an $R$-wall, or it contains an $R$-wall in its interior. In the second case $C = \operatorname{Cone}(W_C)$, where $W_C$ is the set of minimal generators of the rays of $\Sigma$ in $C$; it has $n + 1$ elements, $(W_C, b^R)$ is circuit data with circuit $Z$, and the cones of $\Sigma$ in $C$ are the cones of $T_+(W_C)$.
2. Each cone $F$ of $\Sigma_R$ that contains $Z$ is a face $F = \operatorname{Cone}(Z \cup B_F)$, with $B_F \subset W_C \setminus Z$, of a maximal cone $C$ of the second kind in part 1. The rays of $\Sigma$ in $F$ are the vectors of $Z \cup B_F$, and the cones of $\Sigma$ in $F$ are the cones $\operatorname{Cone}(A)$ with $A \subset Z \cup B_F$ not containing all of $\{u_\rho : \rho \in J_+\}$. Every cone of $\Sigma_R$ that does not contain $Z$ is a cone of $\Sigma$.
3. The exceptional locus of $\pi$ is $V(\sigma_-)$, of dimension $n - |J_-|$, and $\pi(V(\sigma_-)) = V(\operatorname{Cone}(Z))$, of dimension $n - |Z| + 1$.
4. If $|J_-| = 1$, say $J_- = \{\rho_k\}$, then $\pi$ is divisorial with exceptional divisor $D_k$. The fan $\Sigma_R$ is simplicial with rays $\Sigma(1) \setminus \{\rho_k\}$, so $Z_R$ is $\mathbb{Q}$-factorial and projective with $\rho(Z_R) = \rho(X) - 1$.
5. If $|J_-| \ge 2$, then $\pi$ is small. The fan $\Sigma_R$ has the same rays as $\Sigma$, and the cone $\operatorname{Cone}(Z) \in \Sigma_R$ is not simplicial, so $Z_R$ is not $\mathbb{Q}$-factorial.

Together with part 5 of Theorem 3.5.6, the contraction of $R$ is of fibre type if $J_- = \emptyset$, divisorial if $|J_-| = 1$, and small if $|J_-| \ge 2$.

Lean: not yet in Lean. In `MinimalModel.Toric.IsToricStep` the divisorial case is the case where the next fan is the base $G$ itself, which is part 4 here.

### Proof in words

Take $n + 1$ vectors with one relation $q$, and add a multiple of $q$ to the coefficients of a point of their cone. Moving the multiple one way, the first coefficient to reach zero is one with $q_j > 0$; moving it the other way, it is one with $q_k < 0$. So every point of the cone lies in a cone $\operatorname{Cone}(W \setminus \{w_j\})$ with $j \in J_+$, and also in one with $j \in J_-$. These are the two triangulations, and they differ only inside the faces that contain the whole circuit. For the square $u_1 + u_3 = u_2 + u_4$ they are the two diagonals.

In the triangulation $T_+$ every cone that is not shared with $T_-$ contains all the $w_k$ with $q_k < 0$. Those cones make up the orbit closure of $\sigma_-$, so the toric morphism to the cone is an isomorphism away from it. That orbit closure has dimension $n - |J_-|$ and maps to the orbit closure of the face $\operatorname{Cone}(Z)$, of dimension $n - |J_+| - |J_-| + 1$, so its fibres have dimension at least $|J_+| - 1$. For a single negative coefficient this is a divisor; for two or more it has codimension at least two.

For a projective toric variety, the domain fan of a supporting divisor of $R$ merges the maximal cones that are joined by $R$-walls. Each $R$-wall has the relation $b^R$, so the merged cone contains the rays of $Z$, and it contains one more ray of $\Sigma$ for each dimension that $Z$ does not span. Its triangulation by $\Sigma$ is $T_+$. So the local picture above is the whole picture near the exceptional locus.

### Examples

**Example 3.5.16 (the cone over a square).** Let $u_1 = (0,0,1)$, $u_2 = (1,0,1)$, $u_3 = (1,1,1)$, $u_4 = (0,1,1)$ as in Example 3.1.7, with $u_1 + u_3 = u_2 + u_4$. Take $q = (1, -1, 1, -1)$, so $J_+ = \{1, 3\}$, $J_- = \{2, 4\}$ and $J_0 = \emptyset$. Then

$$T_+ = \{\operatorname{Cone}(u_2, u_3, u_4), \operatorname{Cone}(u_1, u_2, u_4)\}, \qquad T_- = \{\operatorname{Cone}(u_1, u_3, u_4), \operatorname{Cone}(u_1, u_2, u_3)\},$$

together with their faces: $T_+$ cuts the square along the diagonal $\operatorname{Cone}(u_2, u_4)$ and $T_-$ along $\operatorname{Cone}(u_1, u_3)$. The fan $T_-$ is the fan $\Sigma_+$ of Example 3.4.9. The faces of the first kind in Proposition 3.5.12 are the four edges $\operatorname{Cone}(u_i, u_{i+1})$, the four rays and $\{0\}$, and there is no face of the second kind since $B = \emptyset$. The $u_i$ generate $\mathbb{Z}^3$ and $q$ is primitive, so all four cones have multiplicity $|q_j| = 1$ by Proposition 3.5.13, and both $X_\pm$ are smooth. By Theorem 3.5.14 both $\pi_\pm$ are small, with exceptional loci the curves $V_+(\operatorname{Cone}(u_2, u_4))$ and $V_-(\operatorname{Cone}(u_1, u_3))$ over the vertex of the cone.

**Example 3.5.17 (the quotients $\frac12(1,1)$ and $\frac13(1,1)$).** Let $\sigma_n = \operatorname{Cone}(e_2, n e_1 - e_2)$ be the cone of $\frac1n(1,1)$ of Example 3.1.6, with $n \ge 2$, and let $W = \{w_1, w_2, w_3\}$ with $w_1 = e_2$, $w_2 = n e_1 - e_2$, $w_3 = e_1$. The relation is $w_1 + w_2 - n w_3 = 0$, so $q = (1, 1, -n)$, $J_+ = \{1, 2\}$ and $J_- = \{3\}$. The fan $T_-$ is the single cone $\operatorname{Cone}(w_1, w_2) = \sigma_n$, and $T_+$ has the two cones $\operatorname{Cone}(w_2, w_3)$ and $\operatorname{Cone}(w_1, w_3)$: it is the resolution of Example 3.1.31. The $w_i$ generate $\mathbb{Z}^2$ and $q$ is primitive, so the two cones of $T_+$ have multiplicity $1$ and $\sigma_n$ has multiplicity $n$, by Proposition 3.5.13. By Theorem 3.5.14, $\pi_+ \colon X_+ \to U_{\sigma_n}$ is divisorial with exceptional curve $E = D_{w_3} = V_+(\operatorname{Cone}(w_3))$.

The wall $\operatorname{Cone}(w_3)$ lies between two smooth cones, so its wall relation is $q$ itself, and $E \cdot E = D_{w_3} \cdot E = -n$, $D_{w_1} \cdot E = D_{w_2} \cdot E = 1$, and $K \cdot E = -(1 + 1 - n) = n - 2$. Write $K_{X_+} = \pi_+^* K_U + a E$. Then $K \cdot E = a E^2$ gives $a = -(n-2)/n$, which agrees with Proposition 3.3.35: $w_3 = \frac1n w_1 + \frac1n w_2$, so $a(w_3) = \frac2n - 1$.

- For $\frac12(1,1)$, $n = 2$: $K \cdot E = 0$ and $a = 0$. The contraction is crepant, and $X_+$ is the minimal resolution of the quadric cone with $E$ a $(-2)$-curve.
- For $\frac13(1,1)$, $n = 3$: $K \cdot E = 1 > 0$ and $a = -\frac13$. The contraction is $K$-positive: it is the contraction of an extremal ray for the divisor $-K$, or for $E$ itself, since $E \cdot E = -3 < 0$, but not for $K$. So the $K$-MMP over $U_{\sigma_3}$ does not contract $E$, and $X_+$ is already a minimal model over $U_{\sigma_3}$. The singularity $\frac13(1,1)$ is klt and not canonical.

**Example 3.5.18 (the contractions of a weighted blow-up).** Let $X$ be the weighted blow-up of $\mathbb{P}^3$ with weights $(1, 2, 3)$ of Problem 4 of Chapter 4: the star subdivision of the fan of $\mathbb{P}^3$ at $v = e_1 + 2 e_2 + 3 e_3$, with $e_0 = -e_1 - e_2 - e_3$. That problem shows that $NE(X)$ has two extremal rays, spanned by $C_{23} = V(\operatorname{Cone}(e_2, e_3))$ and by the curves in $E = D_v$. The wall $\operatorname{Cone}(e_2, e_3)$ lies between $\operatorname{Cone}(e_0, e_2, e_3)$ and $\operatorname{Cone}(v, e_2, e_3)$, which both have determinant $\pm 1$, and

$$e_0 + v = e_2 + 2 e_3.$$

So the relation is $b^R = (1, 1, -1, -2)$ on $(e_0, v, e_2, e_3)$, with $J_+ = \{e_0, v\}$, $J_- = \{e_2, e_3\}$ and $J_0 = \{e_1\}$. By Theorem 3.5.15 the contraction of $C_{23}$ is small, with exceptional locus $V(\operatorname{Cone}(e_2, e_3)) = C_{23}$, and $K \cdot C_{23} = -(1 + 1 - 1 - 2) = 1$. Here $|Z| = 4 = n + 1$, so $B = \emptyset$, and the domain that contains the wall is $\operatorname{Cone}(e_0, v, e_2, e_3)$. For the other ray, the walls $\operatorname{Cone}(v, e_i)$ have relations proportional to $-r_2 = (0, 1, 2, 3, -1)$ in the coordinates $(e_0, e_1, e_2, e_3, v)$, that is, to $e_1 + 2 e_2 + 3 e_3 - v = 0$. So $J_- = \{v\}$, the contraction is divisorial with exceptional divisor $E$, and $\Sigma_R$ is the fan of $\mathbb{P}^3$, by part 4 of Theorem 3.5.15.

### Proof

*Proof of Lemma 3.5.11.* Part 1. The relations among $W \setminus \{w_i\}$ are the relations of $W$ with coefficient $0$ at $w_i$, and the only relations of $W$ are the multiples of $q$, with $q_i \neq 0$. So the $n$ vectors $W \setminus \{w_i\}$ are independent, hence a basis. For the same reason any $|Z| - 1$ vectors of $Z$ are independent, and $Z$ itself is dependent, so $\dim \operatorname{span}(Z) = |Z| - 1$. Since $W$ spans $N_{\mathbb{R}}$, the $|B| = n + 1 - |Z|$ vectors of $B$ span $N_{\mathbb{R}} / \operatorname{span}(Z)$, whose dimension is $n - |Z| + 1$, so they form a basis of it.

Part 2. If $x$ and $-x$ lie in $\operatorname{Cone}(W)$, adding the two expressions gives $\sum_i \lambda_i w_i = 0$ with all $\lambda_i \ge 0$, so $\lambda = t q$. Since $q$ has a positive and a negative coordinate, $t = 0$, so the two expressions are zero and $x = 0$.

Part 3. Let $x \in \operatorname{Cone}(W)$ and choose $\lambda \ge 0$ with $x = \sum \lambda_i w_i$. The expressions of $x$ as a combination of $W$ are $\lambda + t q$, $t \in \mathbb{R}$, and $\lambda + t q \ge 0$ holds exactly for $t$ in the closed interval $[t_{\mathrm{lo}}, t_{\mathrm{hi}}]$ with

$$t_{\mathrm{lo}} = \max_{j \in J_+} \Big( -\frac{\lambda_j}{q_j} \Big) \le 0, \qquad t_{\mathrm{hi}} = \min_{k \in J_-} \frac{\lambda_k}{|q_k|} \ge 0.$$

Put $\mu = \lambda + t_{\mathrm{lo}} q$. It is the unique nonnegative expression of $x$ that is smallest on $J_+$, and it does not depend on the choice of $\lambda$. We claim: for $j \in J_+$, $x \in \operatorname{Cone}(W \setminus \{w_j\})$ if and only if $\mu_j = 0$. If $\mu_j = 0$, then $\mu$ is an expression of $x$ in $W \setminus \{w_j\}$ with nonnegative coefficients. Conversely, a nonnegative expression $\lambda + t q$ with coefficient $0$ at $j$ has $t = -\lambda_j / q_j \le t_{\mathrm{lo}}$, and it is nonnegative, so $t \ge t_{\mathrm{lo}}$; so $t = t_{\mathrm{lo}}$ and $\mu_j = 0$. Some $j \in J_+$ attains the maximum in $t_{\mathrm{lo}}$, so $\mu_j = 0$ for it, and the cones $\operatorname{Cone}(W \setminus \{w_j\})$ with $j \in J_+$ cover $\operatorname{Cone}(W)$.

The claim also gives the intersections. For $S \subset J_+$, a point lies in $\operatorname{Cone}(W \setminus \{w_j\})$ for all $j \in S$ if and only if $\mu_j = 0$ for $j \in S$, if and only if it lies in $\operatorname{Cone}(W \setminus \{w_j : j \in S\})$, by the same argument. So the intersection of two cones $\operatorname{Cone}(A)$ and $\operatorname{Cone}(A')$ of $T_+$, with $A$ and $A'$ each inside some $W \setminus \{w_j\}$, is $\operatorname{Cone}(A \cap A')$: inside the simplicial cone $\operatorname{Cone}(W \setminus \{w_j\})$ the coefficients of a point are unique, so a point of $\operatorname{Cone}(A) \cap \operatorname{Cone}(A')$ has $\mu$ supported in $A$ and in $A'$. A face of a simplicial cone spanned by a basis is the cone of a subset of the basis, so $\operatorname{Cone}(A \cap A')$ is a face of both. The faces of the cones of $T_+$ are in $T_+$, since a subset of $A$ again misses some $w_j$ with $j \in J_+$. So $T_+$ is a simplicial fan with support $\operatorname{Cone}(W)$; its cones are strongly convex by part 2. For $T_-$ use $-q$, which exchanges $J_+$ and $J_-$.

Part 4. Two maximal cones $\operatorname{Cone}(W \setminus \{w_j\})$ and $\operatorname{Cone}(W \setminus \{w_{j'}\})$ of $T_+$ meet in $\operatorname{Cone}(W \setminus \{w_j, w_{j'}\})$, of dimension $n - 1$, which is a wall between them. A cone of dimension $n - 1$ in $T_+$ is $\operatorname{Cone}(W \setminus \{w_i, w_l\})$, and the maximal cones that contain it are those $\operatorname{Cone}(W \setminus \{w_j\})$ with $j \in \{i, l\} \cap J_+$; it lies in two of them exactly when $i, l \in J_+$. For such a wall, with the standard labels $u_n = w_{j'}$ and $u_{n+1} = w_j$, the wall relation is a relation of $W$, so a multiple of $q$, and its coefficients at $w_j$ and $w_{j'}$ are positive by Theorem 3.4.5. Since $q_j > 0$, the multiple is positive. For $T_-$ the same argument gives a positive multiple of $-q$. $\square$

*Proof of Proposition 3.5.12.* Let $F$ be a proper face, $F = \operatorname{Cone}(W) \cap m^\perp$ with $m \ge 0$ on $W$ and $m \neq 0$ on some $w_i$. By Proposition 3.1.4, $F = \operatorname{Cone}(A)$ with $A = W \cap m^\perp$. Pairing $m$ with the relation gives $\sum_{j \in J_+} q_j \langle m, w_j \rangle = \sum_{k \in J_-} |q_k| \langle m, w_k \rangle$, with all terms nonnegative. If $m$ vanishes on $Z$, then $A = Z \cup B'$ with $B' = B \cap m^\perp$, and $B' \neq B$ since $m \neq 0$ on $W$. Otherwise one side of the equation is positive, so both are, and $m$ is positive at some $w_j$ with $j \in J_+$ and some $w_k$ with $k \in J_-$; then $A$ misses $w_j$ and $w_k$.

Conversely, let $A \subset W \setminus \{w_j, w_k\}$ with $j \in J_+$, $k \in J_-$. By part 1 of Lemma 3.5.11, $W \setminus \{w_k\}$ is a basis. Let $m_1$ be the form that vanishes on $W \setminus \{w_j, w_k\}$ with $\langle m_1, w_j \rangle = 1$. The relation gives $q_j + q_k \langle m_1, w_k \rangle = 0$, so $\langle m_1, w_k \rangle = q_j / |q_k| > 0$. For each $w \in (W \setminus \{w_j, w_k\}) \setminus A$, let $m_w$ be the form that is $1$ at $w$ and $0$ on the other vectors of the basis $W \setminus \{w_k\}$. Then $m = s m_1 + \sum_w m_w$, for $s$ large, is $0$ on $A$, positive on the other vectors of $W \setminus \{w_k\}$, and positive at $w_k$. So $\operatorname{Cone}(A) = \operatorname{Cone}(W) \cap m^\perp$ is a face. For $B' \subsetneq B$, part 1 of Lemma 3.5.11 gives a form on $N_{\mathbb{R}} / \operatorname{span}(Z)$ that is $0$ on $B'$ and $1$ on $B \setminus B'$; pulled back to $N_{\mathbb{R}}$ it is $0$ on $Z \cup B'$ and positive on the rest of $W$, so $\operatorname{Cone}(Z \cup B')$ is a face.

A subset $A \subset W$ gives a cone of $T_+ \cap T_-$ if and only if it misses some $w_j$ with $j \in J_+$ and some $w_k$ with $k \in J_-$, which is the first kind. For a face $\operatorname{Cone}(A)$ of the first kind, the form $m$ just built is positive on $W \setminus A$, so the vectors of $W$ in the face are exactly $A$. Finally, let $F = \operatorname{Cone}(W) \cap m^\perp$ be a face that contains all $w_k$ with $k \in J_-$. Then the right side of the paired relation above is $0$, so the left side is $0$, and $m$ vanishes on all $w_j$ with $j \in J_+$. So $F \supset Z$. $\square$

*Proof of Proposition 3.5.13.* The map $\mathbb{Z}^W \to N$ that sends the $i$-th basis vector to $w_i$ is onto, and its kernel is the group of integral relations, which has rank one. Since $N$ has no torsion, the kernel is saturated, so it is generated by a primitive vector, which is $\pm q$. So $N \cong \mathbb{Z}^W / \mathbb{Z} q$. The sublattice generated by $W \setminus \{w_j\}$ is the image of the coordinate sublattice $\mathbb{Z}^{W \setminus \{w_j\}}$, and

$$N / \langle W \setminus \{w_j\} \rangle \cong \mathbb{Z}^W / (\mathbb{Z}^{W \setminus \{w_j\}} + \mathbb{Z} q) \cong \mathbb{Z} / q_j \mathbb{Z},$$

by projection to the $j$-th coordinate. The multiplicity of the simplicial cone is the index of the lattice generated by its minimal generators, which is $|q_j|$. $\square$

*Proof of Theorem 3.5.14.* Both $T_\pm$ have support $\operatorname{Cone}(W)$ and their cones lie in $\operatorname{Cone}(W)$, so the identity of $N$ is compatible with $T_\pm$ and the fan of the faces of $\operatorname{Cone}(W)$, and it gives proper birational toric morphisms by Theorem 3.2.38, as in Corollary 3.2.39.

Part 1. By Proposition 3.5.12, the fan $T_0 = T_+ \cap T_-$ is the set of faces of $\operatorname{Cone}(W)$ that do not contain $Z$. These are cones of $T_+$, so $\pi_+$ is an isomorphism over $U_F$ for each such face $F$, by Corollary 3.2.39. By part 3 of Theorem 3.2.29, the union of the $U_F$ is the union of the orbits $O(F)$ with $F \not\supset Z$, which is $U \setminus V_U(\operatorname{Cone}(Z))$ by part 4 of the same theorem. The orbits of $X_+$ that do not lie over this set are the $O(\delta)$ for $\delta \in T_+ \setminus T_0$, and a subset $A$ of $W$ that misses some $w_j$ with $j \in J_+$ but no $w_k$ with $k \in J_-$ contains $\{w_k : k \in J_-\}$. So these $\delta$ are the cones of $T_+$ that contain $\sigma_-$, and their orbits form $V_+(\sigma_-)$, of dimension $n - |J_-|$. By Theorem 3.2.37, part 3, $\pi_+$ maps $O(\sigma_-)$ into the orbit of the smallest face of $\operatorname{Cone}(W)$ that contains $\sigma_-$, which is $\operatorname{Cone}(Z)$ by Proposition 3.5.12; as $\pi_+$ is proper and $O(\sigma_-)$ is dense in $V_+(\sigma_-)$, $\pi_+(V_+(\sigma_-))$ is the closed invariant set $V_U(\operatorname{Cone}(Z))$, irreducible of dimension $n - \dim \operatorname{Cone}(Z) = n - |Z| + 1$. Every fibre of the surjective morphism $V_+(\sigma_-) \to V_U(\operatorname{Cone}(Z))$ has dimension at least $(n - |J_-|) - (n - |Z| + 1) = |J_+| - 1$ at each of its points, by Hartshorne, Exercise II.3.22.

Part 2. If $|J_+| \ge 2$, every point of $V_+(\sigma_-)$ lies in a fibre of positive dimension, and the points outside it lie over the set where $\pi_+$ is an isomorphism; so the exceptional locus is $V_+(\sigma_-)$. If $J_+ = \{j\}$, then $T_+$ has the single maximal cone $\operatorname{Cone}(W \setminus \{w_j\})$, which is then all of $\operatorname{Cone}(W)$, and $\pi_+$ is the identity of $U$.

Part 3 is the same argument with $-q$. Part 4 holds because both open sets are the toric variety of the common subfan $T_0$, by part 1 and its analogue for $T_-$.

For the last paragraph: if $J_- = \{k\}$, then $X_- = U$ by part 2 for $\pi_-$, $V_+(\sigma_-) = D_{w_k}$ is a divisor, and $|J_+| \ge 2$: otherwise $Z = \{w_j, w_k\}$ and $q_j w_j = |q_k| w_k$, so the primitive vectors $w_j$ and $w_k$ are positive multiples of each other and hence equal, while the $n + 1$ vectors of $W$ are distinct. So $\pi_+$ is divisorial. If $|J_\pm| \ge 2$, both exceptional loci have codimension at least $2$, and part 4 gives an isomorphism between the complements. $\square$

*Proof of Theorem 3.5.15.* Part 1. Let $C$ be a maximal cone of $\Sigma_R$. If it contains only one maximal cone of $\Sigma$, then $C$ is that cone, and none of its walls is an $R$-wall, since the two cones on the sides of an $R$-wall have the same form $m_\sigma$ by part 2 of Proposition 3.5.5, so they lie in the same domain. Assume that $C$ contains two maximal cones of $\Sigma$. By part 5 of Proposition 3.5.5, each maximal cone $\sigma \subset C$ shares an $R$-wall $\tau$ with another maximal cone $\sigma' \subset C$. By Lemma 3.5.2, with the standard labels $\sigma = \tau + \mathbb{R}_{\ge 0} u_n$ and $\sigma' = \tau + \mathbb{R}_{\ge 0} u_{n+1}$, the vectors of $Z$ lie in $\sigma(1) \cup \{u_{n+1}\}$ and $u_{n+1} \in Z$. So $\sigma(1) = (Z \setminus \{z_\sigma\}) \cup B_\sigma$ for one vector $z_\sigma = u_{n+1}$ of $Z$ with $b^R$-coefficient positive, and a set $B_\sigma$ of rays disjoint from $Z$. Crossing $\tau$ replaces $u_n \in Z$ by $u_{n+1} \in Z$ and keeps the rays of $\tau$, so $B_{\sigma'} = \tau(1) \setminus Z = B_\sigma$. By the chains of part 5 of Proposition 3.5.5, $B_\sigma = B$ is the same for all maximal $\sigma \subset C$. Put $W = Z \cup B$. Then $|W| = n + 1$, $W$ spans $N_{\mathbb{R}}$, and $b^R$ is a relation of $W$, so $(W, b^R)$ is circuit data with circuit $Z$ and $J_0 \cap W = B$.

Let $S \subset J_+$ be the set of $j$ with $\operatorname{Cone}(W \setminus \{w_j\}) \subset C$, so that $C$ is the union of these cones, which all lie in $\operatorname{Cone}(W)$. We have $|S| \ge 2$. Every $w \in W$ lies in $\operatorname{Cone}(W \setminus \{w_j\})$ for some $j \in S$ with $w_j \neq w$, so $W \subset C$, and $C$ is convex, so $C = \operatorname{Cone}(W)$. If some $j' \in J_+$ were not in $S$, the interior of $\operatorname{Cone}(W \setminus \{w_{j'}\})$, which is a nonempty open subset of $\operatorname{Cone}(W) = C$, would be covered by the finitely many closed cones $\operatorname{Cone}(W \setminus \{w_j\})$ with $j \in S$, so one of them would meet it in a set with nonempty interior; but two different maximal cones of the fan $T_+$ meet in a proper face. So $S = J_+$, and the maximal cones of $\Sigma$ in $C$ are those of $T_+(W)$. The rays of $\Sigma$ in $C$ are rays of these cones, so they are the vectors of $W$, and $W = W_C$.

Part 2. Let $F \in \Sigma_R$ contain the vectors of $Z$. The vectors of $Z$ are minimal generators of rays of $\Sigma$, and they are linearly dependent, so they do not lie in one simplicial cone of $\Sigma$: a ray of $\Sigma$ inside a cone of $\Sigma$ is a ray of that cone. So $F$ is not a face of a maximal cone of $\Sigma$, and the maximal cone $C$ of $\Sigma_R$ of which $F$ is a face is of the second kind in part 1. By Proposition 3.5.12, $F = \operatorname{Cone}(Z \cup B_F)$ with $B_F \subset B$ (with $B_F = B$ when $F = C$), and the cones of $\Sigma$ in $F$ are the cones of $T_+(W_C)$ in $F$, which are the faces of the maximal cones $\operatorname{Cone}(W_C \setminus \{w_j\})$ that lie in $F$, namely the $\operatorname{Cone}(A)$ with $A \subset Z \cup B_F$ not containing all of $\{u_\rho : \rho \in J_+\}$. A vector of $W_C$ that lies in $F$ is in $Z \cup B_F$, because the form that cuts out $F$ is positive on the rest of $W_C$. If $F \in \Sigma_R$ does not contain $Z$, it is a face of a maximal cone $C$; if $C$ is a cone of $\Sigma$, so is $F$, and otherwise $F$ is a face of the first kind of $\operatorname{Cone}(W_C)$, which is a cone of $T_+(W_C)$ and so of $\Sigma$.

Part 3. By Lemma 3.5.3 and part 3 of Theorem 3.5.6, every curve contracted by $\pi$ lies in $V(\sigma_-)$. A point in the exceptional locus lies in a fibre of positive dimension, which contains a curve through the point, so the exceptional locus is contained in $V(\sigma_-)$. Conversely, $\sigma_-$ lies in an $R$-wall, which lies in a maximal cone $C = \operatorname{Cone}(W_C)$ of $\Sigma_R$ of the second kind. The smallest cone of $\Sigma_R$ that contains $\sigma_-$ is a face of $C$ that contains all $u_k$ with $k \in J_-$, so it is $\operatorname{Cone}(Z)$ by Proposition 3.5.12. As in the proof of Theorem 3.5.14, $\pi$ maps $V(\sigma_-)$, of dimension $n - |J_-|$, onto $V(\operatorname{Cone}(Z))$, of dimension $n - |Z| + 1$, and every fibre of this map has dimension at least $|J_+| - 1 \ge 1$, by part 4 of Lemma 3.5.2. So every point of $V(\sigma_-)$ is in the exceptional locus.

Part 4. If $J_- = \{\rho_k\}$, the exceptional locus is $V(\rho_k) = D_k$. In each maximal cone $C = \operatorname{Cone}(W_C)$ of the second kind, $T_-(W_C)$ is a single simplicial cone, so $C = \operatorname{Cone}(W_C \setminus \{u_k\})$ is simplicial; the other maximal cones of $\Sigma_R$ are cones of $\Sigma$. So $\Sigma_R$ is simplicial and $Z_R$ is $\mathbb{Q}$-factorial by Theorem 3.3.20. Its rays are rays of $\Sigma$, since each cone of $\Sigma_R$ is a union of cones of $\Sigma$. The ray $\rho_k$ is not one of them: $u_k$ is a combination of the other vectors of $Z$ with positive coefficients, so it lies in the relative interior of $\operatorname{Cone}(Z \setminus \{u_k\})$, a cone of dimension $|Z| - 1 \ge 2$. Every other ray $\rho$ is a face of a maximal cone of $\Sigma_R$: either of a cone of $\Sigma$, or of $\operatorname{Cone}(W_C \setminus \{u_k\})$, which is simplicial with $u_\rho$ among its generators. So $\Sigma_R(1) = \Sigma(1) \setminus \{\rho_k\}$, and $\rho(Z_R) = \rho(X) - 1$ by Theorem 3.4.20. $Z_R$ is projective by Theorem 3.5.6.

Part 5. If $|J_-| \ge 2$, the exceptional locus $V(\sigma_-)$ has codimension $|J_-| \ge 2$. Every ray of $\Sigma$ is a face of a maximal cone of $\Sigma_R$: this is clear in a maximal cone of the first kind, and in $\operatorname{Cone}(W_C)$ each single vector misses some $w_j$ with $j \in J_+$ and some $w_k$ with $k \in J_-$, since $|J_\pm| \ge 2$, so it spans a face of the first kind. The cone $\operatorname{Cone}(Z)$ is a face of $\operatorname{Cone}(W_C)$ by Proposition 3.5.12, so it is in $\Sigma_R$, and it has $|Z|$ rays in dimension $|Z| - 1$, so it is not simplicial. By Theorem 3.3.20, $Z_R$ is not $\mathbb{Q}$-factorial. $\square$

### Exercises

1. (A) Let $W = \{e_1, e_2, e_3, e_1 + e_2 + e_3\}$ in $\mathbb{R}^3$. Find $q$, $J_\pm$, $T_+$ and $T_-$, and identify $\pi_+$ as the blow-up of $\mathbb{A}^3$ at the origin.
2. (A) List all faces of the cone over a square of Example 3.5.16 by Proposition 3.5.12, and check that $\operatorname{Cone}(W)$ itself is the only cone that contains $Z$.
3. (A) In Example 3.5.17, check that $K \cdot E = n - 2$ also by the adjunction formula on the smooth surface $X_+$, with $E \cong \mathbb{P}^1$ and $E^2 = -n$.
4. (B) Let $W = \{e_1, e_2, e_1 + e_2, e_3\}$ in $\mathbb{R}^3$, with $q$ the relation $e_1 + e_2 - (e_1 + e_2) = 0$. Show that $J_0 = \{e_3\}$, that $\operatorname{Cone}(W) = \operatorname{Cone}(e_1, e_2, e_3)$, and that $\pi_+$ is the blow-up of $\mathbb{A}^3$ along a coordinate line. List the faces of the second kind.
5. (B) Let $(W, q)$ be circuit data with $J_+ = \{j\}$. Show that $w_j$ lies in $\operatorname{Cone}(w_k : k \in J_-)$, that $\operatorname{Cone}(W) = \operatorname{Cone}(W \setminus \{w_j\})$ is simplicial, and deduce again that $T_+$ is the fan of the faces of one cone.
6. (B) Let $q = (a_1, a_2, -b_1, -b_2)$ with positive integers and $W$ the images of the basis in $N = \mathbb{Z}^4 / \mathbb{Z} q$, assuming $q$ primitive. Find the multiplicities of the four cones of $T_+$ and $T_-$. When are both $X_\pm$ smooth?
7. (C) Assume $J_0 = \emptyset$. Show that every simplicial fan with support $\operatorname{Cone}(W)$ whose rays are among the rays of $W$ is $T_+$ or $T_-$.
8. (C) In Theorem 3.5.15, show that every maximal cone of $\Sigma$ that contains $\sigma_-$ lies in a maximal cone of $\Sigma_R$ of the second kind, using part 3.

### Lean

- Status: not yet in Lean. The library has fans and simplicial cones, but no circuits, no triangulations and no toric varieties.
- Fidelity: the definition `MinimalModel.Toric.IsToricStep` in `MinimalModel/Toric/Program.lean` asks for a base fan $G$ that the fan $A.F$ refines with relative Picard number one, and a simplicial fan $B.F$ that refines $G$ with the same rays as $G$. Part 4 of Theorem 3.5.15 says that in the divisorial case $B.F = \Sigma_R$ is a valid choice, and part 5 that in the small case $\Sigma_R$ has the rays of $\Sigma$, as that definition expects. The definitions do not mention circuits; Theorem 3.5.15 is the reason they describe every toric step.
- No node of the map covers this section.

### Notes and history

The decomposition of an extremal contraction by the signs of the relation, with the fibre type, divisorial and small cases decided by $J_-$, is the core of Reid's paper of 1983, which the map cites for the toric contractions and flips, and it is in Cox-Little-Schenck, Section 15.4. The proofs in this section were written for the handbook from the circuit lemma, and Reid's paper has not been read for it. The two triangulations of a circuit are a standard part of the theory of triangulations; Cox-Little-Schenck use them in Section 15.2 with the secondary fan, the subject of Chapter 7. The cone over a square and the cones $\sigma_n$ are running examples of the volume: Example 3.1.7 and Example 3.1.31. The weighted blow-up of Example 3.5.18 returns in Section 3, where the contraction of $C_{23}$ is flipped, and in Chapter 6.
