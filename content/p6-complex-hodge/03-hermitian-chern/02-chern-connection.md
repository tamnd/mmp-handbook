---
title: The Chern connection and its curvature
nodes: []
sources: [Huy05, GH78, Wel80, Voi02, Che46]
reads_with: [Huy05:4.2, Huy05:4.3, GH78:0.5, Wel80:III]
requires: [P6.1, P6.2]
level: prereq
kind: theorem
status: drafted
drafted_by: writer@claude-opus-5-5
reviewed_by: []
---
## The Chern connection and its curvature

### Statement

Let $E$ be a smooth complex vector bundle of rank $r$ on a smooth manifold $X$, and write $\mathcal{A}^k(E) = \mathcal{A}^k_X \otimes_{\mathcal{A}_X} \mathcal{A}(E)$ for the sheaf of smooth $k$-forms with values in $E$, $A^k(E)$ for its global sections. Matrix conventions: a local frame is a row $e = (e_1, \dots, e_r)$, a section is $s = e \sigma = \sum_j \sigma_j e_j$ with $\sigma$ a column of functions or forms, and a change of frame is $e' = e g$ with $g$ an invertible matrix of functions, so that $\sigma = g \sigma'$. For matrices of forms, $(\alpha \wedge \beta)_{jk} = \sum_l \alpha_{jl} \wedge \beta_{lk}$, and $\alpha^*$ is the conjugate transpose, $(\alpha^*)_{jk} = \overline{\alpha_{kj}}$.

**Definition P6.3.11 (connections).** A *connection* on $E$ is a $\mathbb{C}$-linear map of sheaves $\nabla: \mathcal{A}(E) \to \mathcal{A}^1(E)$ with $\nabla(f s) = df \otimes s + f \nabla s$ for smooth functions $f$. It extends uniquely to maps $\nabla: \mathcal{A}^k(E) \to \mathcal{A}^{k+1}(E)$ with $\nabla(\alpha \otimes s) = d\alpha \otimes s + (-1)^k \alpha \wedge \nabla s$ for a $k$-form $\alpha$. In a frame $e$ the *connection matrix* $\theta = (\theta_{kj})$ of $1$-forms is defined by $\nabla e_j = \sum_k \theta_{kj} e_k$, that is $\nabla e = e \theta$, so that $\nabla(e \sigma) = e (d\sigma + \theta \sigma)$.

**Proposition P6.3.12 (existence and operations).** Let $X$ be Hausdorff and second countable.

1. Every $E$ has a connection. If $\nabla$ is one, the connections on $E$ are exactly $\nabla + \eta$ with $\eta \in A^1(\operatorname{End} E)$, and a convex combination $\sum_a \rho_a \nabla_a$ with smooth $\rho_a \geq 0$, $\sum_a \rho_a = 1$, locally finite, is a connection.
2. Under a change of frame $e' = e g$, $\theta' = g^{-1} dg + g^{-1} \theta g$.
3. Connections $\nabla_E$ and $\nabla_F$ induce connections on $E^*$, $E \oplus F$, $E \otimes F$, $\operatorname{End} E$, $\det E$ and $f^* E$, by $(\nabla \lambda)(s) = d(\lambda(s)) - \lambda(\nabla s)$, $\nabla_E \oplus \nabla_F$, $\nabla_E \otimes 1 + 1 \otimes \nabla_F$, the Leibniz rule on $\Lambda^r E$, and $f^*\nabla e = e \cdot f^*\theta$ in pulled back frames. Their connection matrices are $-\theta^T$ in the dual frame, $\operatorname{diag}(\theta_E, \theta_F)$, $\theta_E \otimes 1 + 1 \otimes \theta_F$, $\operatorname{tr} \theta$ for the frame $e_1 \wedge \dots \wedge e_r$ of $\det E$, and $f^* \theta$.

Lean: not yet in Lean.

**Definition P6.3.13 (curvature).** The *curvature* of $\nabla$ is the composite $F_\nabla = \nabla \circ \nabla: \mathcal{A}(E) \to \mathcal{A}^2(E)$. By Proposition P6.3.14 it is $\mathcal{A}_X$-linear, so it is a global section $F_\nabla \in A^2(\operatorname{End} E)$. A connection is *flat* if $F_\nabla = 0$.

**Proposition P6.3.14 (local form of the curvature and the Bianchi identity).** Let $\nabla$ be a connection with matrix $\theta$ in a frame $e$.

1. $\nabla^2$ is $\mathcal{A}_X$-linear, $\nabla^2(f s) = f \nabla^2 s$, and in the frame $e$, $\nabla^2(e \sigma) = e\, F \sigma$ with the curvature matrix $F = d\theta + \theta \wedge \theta$.
2. Under $e' = e g$, $F' = g^{-1} F g$.
3. (Bianchi identity) $dF = F \wedge \theta - \theta \wedge F$.
4. For a line bundle, $\theta$ is a $1$-form, $F = d\theta$ is a closed $2$-form independent of the frame, the curvature of $L \otimes L'$ with the tensor product connection is $F_L + F_{L'}$, and the curvature of $L^*$ is $-F_L$.

Lean: not yet in Lean.

**Definition P6.3.15 (metric and holomorphic compatibility).** Let $h$ be a Hermitian metric on $E$, extended to forms by $h(\alpha \otimes s, \beta \otimes t) = \alpha \wedge \bar\beta\, h(s, t)$.

1. $\nabla$ is *compatible with $h$*, or a *metric connection*, if $d\, h(s, t) = h(\nabla s, t) + h(s, \nabla t)$ for all local sections $s, t$.
2. Let $X$ be a complex manifold and $E$ a holomorphic vector bundle. In a holomorphic frame $e$ put $\bar\partial_E(e \sigma) = e\, \bar\partial \sigma$; this is independent of the holomorphic frame because holomorphic changes of frame $g$ satisfy $\bar\partial g = 0$, and it defines $\bar\partial_E: \mathcal{A}^{p,q}(E) \to \mathcal{A}^{p,q+1}(E)$. Split $\nabla = \nabla^{1,0} + \nabla^{0,1}$ by type. The connection $\nabla$ is *compatible with the holomorphic structure* if $\nabla^{0,1} = \bar\partial_E$.

**Theorem P6.3.16 (the Chern connection).** Let $E$ be a holomorphic vector bundle with a Hermitian metric $h$ on a complex manifold $X$. There is exactly one connection $\nabla$ on $E$, the *Chern connection* of $(E, h)$, that is compatible with $h$ and with the holomorphic structure. Let $e$ be a holomorphic frame and $H = (H_{jk})$ the matrix with $H_{jk} = h(e_k, e_j)$, the transpose of the Gram matrix $(h(e_j, e_k))$, so that $h(e \sigma, e \tau) = \tau^* H \sigma$. Then:

1. the connection matrix is $\theta = H^{-1} \partial H$, of type $(1,0)$;
2. the curvature matrix is $F = \bar\partial(H^{-1} \partial H)$, of type $(1,1)$;
3. $h(F s, t) + h(s, F t) = 0$, that is $H F + F^* H = 0$; in a unitary frame $F^* = -F$, so $iF$ is a Hermitian matrix of $(1,1)$-forms, $(iF)^* = iF$.

Lean: not yet in Lean.

**Corollary P6.3.17 (Hermitian line bundles).** Let $L$ be a holomorphic line bundle with a Hermitian metric $h$, and $h_i = |e_i|^2_h$ for a holomorphic frame $e_i$ on $U_i$. The Chern connection is $\nabla e_i = \partial \log h_i \cdot e_i$, and its curvature is
$$F_h = \bar\partial \partial \log h_i = -\partial\bar\partial \log h_i.$$
The form $c_1(L, h) = \frac{i}{2\pi} F_h = -\frac{i}{2\pi} \partial\bar\partial \log h_i$ is a closed real $(1,1)$-form on $X$. It is additive, $c_1(L \otimes L', h \otimes h') = c_1(L, h) + c_1(L', h')$, satisfies $c_1(L^*, h^*) = -c_1(L, h)$ and $c_1(f^*L, f^*h) = f^* c_1(L, h)$ for holomorphic $f$, and for a holomorphic section $s$ of $L$, $F_h = -\partial\bar\partial \log |s|^2_h$ outside the zeros of $s$.

Lean: not yet in Lean.

**Proposition P6.3.18 (curvature decreases in subbundles).** Let $(E, h)$ be a Hermitian holomorphic bundle, $S \subseteq E$ a holomorphic subbundle with the restricted metric, $Q = S^\perp$, and $\nabla$, $\nabla_S$ the Chern connections. For a local section $s$ of $S$ write $\nabla s = \nabla' s + \beta s$ with $\nabla' s \in \mathcal{A}^1(S)$ and $\beta s \in \mathcal{A}^1(Q)$. Then:

1. $\nabla' = \nabla_S$, and $\beta$ is an $\mathcal{A}_X$-linear form $\beta \in A^{1,0}(\operatorname{Hom}(S, Q))$, the *second fundamental form*;
2. $F_S = \operatorname{pr}_S \circ F_E|_S + \beta^\dagger \wedge \beta$, where $\beta^\dagger \in A^{0,1}(\operatorname{Hom}(Q, S))$ is the adjoint, $h(\beta s, q) = h(s, \beta^\dagger q)$;
3. for every local section $s$ of $S$, $i\, h(F_S s, s)$ and $i\, h(F_E s, s)$ are real $(1,1)$-forms, and $i\, h(F_E s, s) - i\, h(F_S s, s)$ is semipositive.

Lean: not yet in Lean.

### Proof in words

A connection differentiates sections; the difference of two connections is a matrix of $1$-forms, and partitions of unity glue the trivial connections $d$ of local frames into a global connection. Applying a connection twice kills the derivatives of functions, so $\nabla^2$ is a matrix of $2$-forms, the curvature $d\theta + \theta \wedge \theta$, and differentiating this formula gives the Bianchi identity. For a holomorphic Hermitian bundle the two conditions determine the connection matrix in a holomorphic frame: holomorphy says that $\theta$ has type $(1,0)$, metric compatibility says $dH = H\theta + \theta^* H$, and the $(1,0)$-part of this equation is $\partial H = H\theta$. So $\theta = H^{-1} \partial H$, and this formula transforms correctly under holomorphic changes of frame. Its curvature has no $(2,0)$-part because $\partial \theta = -\theta \wedge \theta$, and no $(0,2)$-part because $\theta$ has type $(1,0)$. For a line bundle the formula reads $\theta = \partial \log h$, so the curvature is $-\partial\bar\partial \log h$, and this is where the Fubini-Study form reappears. In a subbundle the curvature acquires the term $\beta^\dagger \wedge \beta$, which is negative because it is a sum of squares of the second fundamental form.

### Examples

**Example P6.3.19 ($\mathcal{O}(-1)$ and $\mathcal{O}(1)$ with the Fubini-Study metric).** Give $\mathcal{O}(-1)$ and $\mathcal{O}(1)$ on $\mathbb{P}^n$ the metrics of Example P6.3.9. For $\mathcal{O}(1)$, $h_i = |Z_i|^2 / \|Z\|^2$, so by Corollary P6.3.17
$$c_1(\mathcal{O}(1), h) = -\frac{i}{2\pi} \partial\bar\partial \log \frac{|Z_i|^2}{\|Z\|^2} = \frac{i}{2\pi} \partial\bar\partial \log \frac{\|Z\|^2}{|Z_i|^2} = \omega_{FS},$$
by Example P6.3.8. For $\mathcal{O}(-1)$, $|\varepsilon_i|^2 = \|Z\|^2 / |Z_i|^2$ and $c_1(\mathcal{O}(-1), h) = -\omega_{FS}$, in accordance with the dual rule. The Chern connection of $\mathcal{O}(1)$ in the chart $U_0$ is $\nabla e_0 = -\partial \log(1 + |z|^2)\, e_0 = -\frac{\sum_j \bar z_j\, dz_j}{1 + |z|^2} e_0$. The same result follows from the section $s = Z_0$: $|s|^2_h = |Z_0|^2 / \|Z\|^2$, and outside $\{Z_0 = 0\}$, $F_h = -\partial\bar\partial \log |s|^2_h$ gives $c_1 = \frac{i}{2\pi}\partial\bar\partial \log(1 + |z|^2)$ on $U_0$. Proposition P6.3.18 applies to $\mathcal{O}(-1) \subset \mathbb{P}^n \times \mathbb{C}^{n+1}$: the trivial bundle with the standard metric has Chern connection $d$ and $F = 0$, so $i F_{\mathcal{O}(-1)} = 2\pi\, c_1(\mathcal{O}(-1), h)$ must be seminegative, and indeed it is $-2\pi \omega_{FS}$. On $\mathcal{O}(d)$ with $|s|^2 = |s(Z)|^2 / \|Z\|^{2d}$, $c_1(\mathcal{O}(d), h) = d\, \omega_{FS}$ by additivity, for every $d \in \mathbb{Z}$.

**Example P6.3.20 (weights on the trivial bundle and flat line bundles).** On the trivial bundle $X \times \mathbb{C}$ with frame $1$, a metric is $|1|^2 = e^{-\varphi}$ for a smooth real function $\varphi$, the *weight*. Then $F = -\partial\bar\partial \log e^{-\varphi} = \partial\bar\partial \varphi$ and $c_1 = \frac{i}{2\pi} \partial\bar\partial \varphi = d(\frac{i}{2\pi} \bar\partial \varphi)$ is exact. It is positive if and only if the matrix $(\partial^2 \varphi / \partial z_j \partial \bar z_k)$ is positive definite. For $\varphi = |z|^2$ on $\mathbb{C}^n$, $c_1 = \frac{i}{2\pi} \sum dz_j \wedge d\bar z_j = \frac{1}{\pi} \omega_0$ is positive, although the bundle is trivial. This cannot happen on a compact $X$: if $c_1 = d\gamma$ is positive, then $c_1^n = d(\gamma \wedge c_1^{n-1})$ and Stokes gives $\int_X c_1^n = 0$, while $c_1^n > 0$ by Proposition P6.3.2. If $L$ has transition functions $g_{ij}$ with $|g_{ij}| = 1$, then $h_i = 1$ is a well-defined metric, since $h_j = |g_{ij}|^2 h_i$, and its Chern connection is flat. On the Hopf surface $X = (\mathbb{C}^2 \setminus \{0\}) / \langle z \mapsto 2z \rangle$ of Example P6.2.4 and $\lambda \in \mathbb{C}^*$, let $L_\lambda$ be the quotient of $(\mathbb{C}^2 \setminus \{0\}) \times \mathbb{C}$ by $(z, v) \sim (2z, \lambda v)$. With $c = \log |\lambda| / \log 2$, the function $\|z\|^{-2c} |v|^2$ is invariant, since $\|2z\|^{-2c} |\lambda v|^2 = 2^{-2c} |\lambda|^2 \|z\|^{-2c} |v|^2$, and defines a metric on $L_\lambda$ with weight $\varphi = c \log \|z\|^2$ in the frame $1$ upstairs. So $c_1(L_\lambda, h) = \frac{c\, i}{2\pi} \partial\bar\partial \log \|z\|^2$, which is $c$ times the pullback of $\omega_{FS}$ under $\mathbb{C}^2 \setminus \{0\} \to \mathbb{P}^1$, and descends to $X$. For $|\lambda| = 1$ the metric is flat; for $|\lambda| \neq 1$ the curvature form is $c$ times a nonzero semipositive form, and it is exact, $d(\frac{c\, i}{2\pi} \bar\partial \log \|z\|^2)$, where $\bar\partial \log \|z\|^2$ is invariant under $z \mapsto 2z$.

**Example P6.3.21 (a metric connection that is not holomorphic).** On the trivial line bundle of $\mathbb{C}^2$ with the metric $|1|^2 = 1$, let $a = z_1\, dz_2$ and $\nabla = d + \theta$ with $\theta = a - \bar a$. Since $\bar\theta = -\theta$, $dH = 0 = \theta + \bar\theta = H\theta + \theta^* H$, so $\nabla$ is a metric connection. Its $(0,1)$-part is $\bar\partial - \bar z_1\, d\bar z_2 \neq \bar\partial_E$, so $\nabla$ is not the Chern connection, which is $d$. Its curvature is
$$F = d\theta = dz_1 \wedge dz_2 - d\bar z_1 \wedge d\bar z_2,$$
which has a $(2,0)$-part and a $(0,2)$-part: the conclusion of type $(1,1)$ in Theorem P6.3.16 needs both compatibilities. The $(0,2)$-part is $(\nabla^{0,1})^2$: for a function $f$, $(\bar\partial - \bar a)(\bar\partial f - \bar a f) = -\bar\partial \bar a\, f = -d\bar z_1 \wedge d\bar z_2\, f$. Since it is not zero, $\nabla^{0,1}$ is not the $\bar\partial$-operator of any holomorphic structure on the trivial bundle. The form $\frac{i}{2\pi} F$ is still closed and is exact, as Section 3.3 predicts for every connection on a trivial bundle.

### Proof

*Proof of Proposition P6.3.12.* 1. On an open set with a frame $e$, $\nabla(e\sigma) = e\, d\sigma$ is a connection. With a partition of unity $\{\rho_a\}$ subordinate to a cover by such sets, $\nabla = \sum_a \rho_a \nabla_a$ is $\mathbb{C}$-linear and $\nabla(fs) = \sum_a \rho_a (df \otimes s + f \nabla_a s) = df \otimes s + f \nabla s$; the same computation shows that convex combinations of connections are connections. If $\nabla$, $\nabla'$ are connections, $(\nabla' - \nabla)(fs) = f (\nabla' - \nabla)(s)$, so the difference is $\mathcal{A}_X$-linear, that is, a section of $\mathcal{A}^1(\operatorname{End} E)$; conversely $\nabla + \eta$ satisfies the Leibniz rule. The extension to $k$-forms is forced by the formula, and it is well defined because $\alpha \wedge f \otimes s$ and $\alpha \otimes fs$ have the same image: $d(f\alpha) \otimes s + (-1)^k f\alpha \wedge \nabla s = d\alpha \otimes fs + (-1)^k \alpha \wedge (df \otimes s + f \nabla s)$.

2. $\nabla(e g \sigma') = e (d(g\sigma') + \theta g \sigma') = e g (d\sigma' + (g^{-1} dg + g^{-1} \theta g) \sigma')$.

3. Each formula satisfies the Leibniz rule, as one checks on $fs$. For the dual frame $e^*$ with $e^*_k(e_j) = \delta_{kj}$, $(\nabla e^*_k)(e_j) = 0 - e^*_k(\nabla e_j) = -\theta_{kj}$, so $\nabla e^*_k = -\sum_j \theta_{kj} e^*_j$ and the matrix is $-\theta^T$. On $\det E$, $\nabla(e_1 \wedge \dots \wedge e_r) = \sum_j e_1 \wedge \dots \wedge \nabla e_j \wedge \dots \wedge e_r = (\sum_j \theta_{jj})\, e_1 \wedge \dots \wedge e_r$, since the other components of $\nabla e_j$ give repeated vectors. The other matrices are read off from the definitions. $\square$

*Proof of Proposition P6.3.14.* 1. For a vector $\tau$ of $1$-forms, $\nabla(e\tau) = \sum_j (d\tau_j \otimes e_j - \tau_j \wedge \nabla e_j) = e (d\tau + \theta \wedge \tau)$, since $-\tau_j \wedge \theta_{kj} = \theta_{kj} \wedge \tau_j$. Hence
$$\nabla^2(e\sigma) = \nabla(e(d\sigma + \theta\sigma)) = e (d\theta\, \sigma - \theta \wedge d\sigma + \theta \wedge d\sigma + \theta \wedge \theta\, \sigma) = e (d\theta + \theta \wedge \theta) \sigma.$$
The derivatives of $\sigma$ cancel, so $\nabla^2$ is $\mathcal{A}_X$-linear and has matrix $F$.

2. $e' F' \sigma' = \nabla^2(e' \sigma') = \nabla^2(e g \sigma') = e F g \sigma' = e' g^{-1} F g \sigma'$.

3. $dF = d\theta \wedge \theta - \theta \wedge d\theta = (F - \theta\wedge\theta) \wedge \theta - \theta \wedge (F - \theta \wedge \theta) = F \wedge \theta - \theta \wedge F$.

4. For $r = 1$, $\theta \wedge \theta = 0$ and $g^{-1} F g = F$, so $F = d\theta$ is a global closed $2$-form. The tensor product connection has matrix $\theta_L + \theta_{L'}$ in the frame $e \otimes e'$, and the dual has $-\theta_L$, by Proposition P6.3.12. $\square$

*Proof of Theorem P6.3.16.* Let $e$ be a holomorphic frame on $U$. For a connection with matrix $\theta$, compatibility with the holomorphic structure says $\nabla^{0,1}(e\sigma) = e(\bar\partial \sigma + \theta^{0,1} \sigma)$ equals $e\, \bar\partial\sigma$ for all $\sigma$, that is $\theta^{0,1} = 0$. Metric compatibility for $s = e_k$, $t = e_j$ reads
$$dH_{jk} = h(\nabla e_k, e_j) + h(e_k, \nabla e_j) = \sum_l \theta_{lk} H_{jl} + \sum_l \overline{\theta_{lj}} H_{lk} = (H\theta + \theta^* H)_{jk},$$
and for general $s = e\sigma$, $t = e\tau$ the condition $d(\tau^* H \sigma) = \tau^* H (d\sigma + \theta\sigma) + (d\tau + \theta\tau)^* H \sigma$ is equivalent to $dH = H\theta + \theta^* H$. If $\theta$ has type $(1,0)$, then $\theta^*$ has type $(0,1)$, and the $(1,0)$-part of this equation is $\partial H = H \theta$. So $\theta = H^{-1} \partial H$, which proves uniqueness on $U$ and hence on $X$.

For existence, define $\nabla$ on $U$ by $\theta = H^{-1}\partial H$. It is compatible with the holomorphic structure because $\theta$ has type $(1,0)$, and with $h$ because $H^* = H$ gives $(\partial H)^* = \bar\partial H$ entrywise, hence $H\theta + \theta^* H = \partial H + (\partial H)^* H^{-1} H = \partial H + \bar\partial H = dH$. On the overlap of two such sets, both local connections are compatible with $h$ and the holomorphic structure, so they agree by uniqueness; hence they glue. One can also check this directly: for a holomorphic change $e' = eg$, $H' = g^* H g$ and $\partial g^* = (\bar\partial g)^* = 0$, so $H'^{-1}\partial H' = g^{-1} H^{-1} (\partial H\, g + H\, \partial g) = g^{-1}\theta g + g^{-1} dg$, in accordance with Proposition P6.3.12.

For the curvature, $\partial \theta = \partial(H^{-1}) \wedge \partial H = -H^{-1} \partial H\, H^{-1} \wedge \partial H = -\theta \wedge \theta$, so
$$F = d\theta + \theta\wedge\theta = \partial\theta + \bar\partial\theta + \theta \wedge \theta = \bar\partial \theta = \bar\partial(H^{-1}\partial H),$$
of type $(1,1)$. For part 3, differentiate $dH = H\theta + \theta^* H$: $0 = dH \wedge \theta + H\, d\theta + d\theta^*\, H - \theta^* \wedge dH$. Substituting $dH$ and using $(\theta\wedge\theta)^* = -\theta^* \wedge \theta^*$ and $d(\theta^*) = (d\theta)^*$ gives $0 = H(d\theta + \theta\wedge\theta) + ((d\theta)^* - \theta^* \wedge \theta^*) H = HF + F^* H$, where $F^* = (d\theta)^* + (\theta\wedge\theta)^* = (d\theta)^* - \theta^*\wedge\theta^*$. In the form $h(Fs, t) + h(s, Ft) = \tau^*(HF + F^*H)\sigma$ this is the first claim. In a unitary frame $H = I$ and $F^* = -F$, so $(iF)^* = -i F^* = iF$. $\square$

*Proof of Corollary P6.3.17.* For $r = 1$, $H = h_i$ and $\theta = h_i^{-1} \partial h_i = \partial \log h_i$, $F = \bar\partial\partial \log h_i = -\partial\bar\partial \log h_i$. By Theorem P6.3.16 and Proposition P6.3.14 it is a global closed $(1,1)$-form, and $F^* = \bar F = -F$ says that $iF$ is real, which also follows from Proposition P6.3.4. The metric $h \otimes h'$ has $|e_i \otimes e'_i|^2 = h_i h'_i$, the dual metric has $|e_i^*|^2 = h_i^{-1}$, and $f^* h$ has $|f^* e_i|^2 = h_i \circ f$; the formulas follow because $\log$ turns products into sums and $\partial\bar\partial$ commutes with holomorphic pullback (Proposition P6.1.33). For $s = f_i e_i$ with $f_i$ holomorphic, $\log |s|^2_h = \log |f_i|^2 + \log h_i$ outside the zeros of $f_i$, and $\partial\bar\partial \log |f_i|^2 = 0$ there, as in Example P6.3.8. $\square$

*Proof of Proposition P6.3.18.* 1. For local sections $s$, $t$ of $S$, $d h(s, t) = h(\nabla s, t) + h(s, \nabla t) = h(\nabla' s, t) + h(s, \nabla' t)$ since $\beta s \perp t$, so $\nabla'$ is a metric connection on $S$; it satisfies the Leibniz rule because $\operatorname{pr}_S(df \otimes s) = df \otimes s$. For a smooth section $s$ of $S$, $\nabla^{0,1} s = \bar\partial_E s$ lies in $\mathcal{A}^{0,1}(S)$ and equals $\bar\partial_S s$: in a holomorphic frame of $E$ whose first vectors form a holomorphic frame of $S$, a section of $S$ has components only in the first vectors, and $\bar\partial$ is taken componentwise. So $(\nabla')^{0,1} = \bar\partial_S$, $\nabla' = \nabla_S$ by Theorem P6.3.16, and $\beta s = \operatorname{pr}_Q \nabla^{1,0} s$ has type $(1,0)$. It is $\mathcal{A}_X$-linear: $\beta(fs) = \operatorname{pr}_Q(df \otimes s + f\nabla s) = f \beta s$.

2. Locally write $\beta = \sum_a dz_a \otimes B_a$ with $B_a$ sections of $\operatorname{Hom}(S, Q)$, so that $\beta^\dagger = \sum_a d\bar z_a \otimes B_a^\dagger$ and $\beta^\dagger \wedge \beta = \sum_{a,b} d\bar z_b \wedge dz_a \otimes B_b^\dagger B_a$. For a section $q$ of $Q$ and $s$ of $S$, $0 = d h(s, q) = h(\nabla s, q) + h(s, \nabla q) = h(\beta s, q) + h(s, \operatorname{pr}_S \nabla q)$, so $\operatorname{pr}_S \nabla q = -\beta^\dagger q$. For an $S$-valued $1$-form $\alpha \otimes s$, $\operatorname{pr}_S \nabla(\alpha \otimes s) = d\alpha \otimes s - \alpha \wedge \nabla_S s = \nabla_S(\alpha \otimes s)$. For the $Q$-valued $1$-form $\beta s = \sum_a dz_a \otimes B_a s$,
$$\operatorname{pr}_S \nabla(\beta s) = -\sum_a dz_a \wedge \operatorname{pr}_S \nabla(B_a s) = \sum_{a,b} dz_a \wedge d\bar z_b\, B_b^\dagger B_a s = -\beta^\dagger \wedge \beta s.$$
Then
$$\operatorname{pr}_S F_E s = \operatorname{pr}_S \nabla(\nabla_S s + \beta s) = \nabla_S \nabla_S s + \operatorname{pr}_S \nabla(\beta s) = F_S s - \beta^\dagger \wedge \beta s.$$

3. By Theorem P6.3.16, part 3, $h(Fs, s) = -h(s, Fs) = -\overline{h(Fs, s)}$ for both connections, so $i\, h(F s, s)$ is real. With $v_a = B_a s$, and since $h(B_a^\dagger B_b s, s) = h(B_b s, B_a s)$,
$$i\, h(\beta^\dagger \wedge \beta s, s) = i \sum_{a,b} d\bar z_a \wedge dz_b\, h(B_a^\dagger B_b s, s) = -i \sum_{a,b} h(v_b, v_a)\, dz_b \wedge d\bar z_a.$$
The matrix $(h(v_b, v_a))_{b,a}$ is a Gram matrix, Hermitian and positive semidefinite, so by Definition P6.3.3 this form is $-1$ times a semipositive form. Part 2 and $h(\operatorname{pr}_S F_E s, s) = h(F_E s, s)$ give $i\, h(F_S s, s) = i\, h(F_E s, s) + i\, h(\beta^\dagger \wedge \beta s, s)$, which is the claim. $\square$

### Exercises

1. (A) Show that the curvature of the Chern connection of $(L, h)$ changes by $\partial\bar\partial \varphi$ when $h$ is replaced by $e^{-\varphi} h$, and that $c_1(L, e^{-\varphi} h) - c_1(L, h)$ is exact.
2. (A) Show that a connection is metric if and only if its matrix in every local unitary frame is skew-Hermitian, $\theta^* = -\theta$.
3. (B) Show that the curvature of the Chern connection of $\operatorname{End} E$ is $\phi \mapsto [F, \phi]$, and that the Bianchi identity says that $F$ is parallel for this connection.
4. (B) For a holomorphic quotient $E \to Q$ with the quotient metric, show that $i\, h(F_Q q, q) - i\, h(F_E \tilde q, \tilde q)$ is semipositive, where $\tilde q$ is the lift of $q$ orthogonal to the kernel: curvature increases in quotients.
5. (B) Use Exercise 4 and the Euler sequence of Proposition P6.2.18 to show that the quotient metric on $T_{\mathbb{P}^n}$, induced from the metric of Example P6.3.9 on each summand of $\mathcal{O}(1)^{\oplus (n+1)}$, has $i\, h(F v, v)$ semipositive for every local section $v$.
6. (C) Let $(E, h)$ be a Hermitian holomorphic bundle with Chern connection $\nabla$, and $h'(s, t) = h(As, t)$ a second metric, $A$ a positive self-adjoint endomorphism. Show that in a holomorphic frame the Chern connection of $h'$ has matrix $\theta' = \theta + A^{-1}(\partial A + [\theta, A])$ and curvature $F' = F + \bar\partial(A^{-1} \nabla^{1,0} A)$, where $\nabla^{1,0} A = \partial A + [\theta, A]$ is computed with the connection of $\operatorname{End} E$.

### Lean

Mathlib has smooth manifolds, smooth vector bundles and differential forms in a basic form, and holomorphic functions of one variable. It has no connections on vector bundles in the sense used here, no curvature and no Chern connection. The handbook adds no `MinimalModel` node here.

### Notes and history

Chern introduced the connection of Theorem P6.3.16 in his work on characteristic classes of Hermitian manifolds (Che46), where the curvature of the canonical Hermitian connection gives the Chern forms of Section 3.3. The presentation follows Huybrechts, Sections 4.2 and 4.3 (Huy05), Griffiths and Harris, Section 0.5 (GH78), and Wells, Chapter III (Wel80). Conventions for connection matrices differ: Griffiths and Harris write $\nabla e_j = \sum_k \theta_{jk} e_k$ and use the Gram matrix $(h(e_j, e_k))$, and then $\theta = \partial H \cdot H^{-1}$; this section writes $\nabla e = e\theta$ and uses the transposed matrix $H_{jk} = h(e_k, e_j)$, so that $\theta = H^{-1}\partial H$. The two conventions give transposed curvature matrices, hence the same Chern forms. The decreasing of curvature in subbundles is the source of the positivity of quotients of ample bundles and of the negativity of $\mathcal{O}(-1)$, used in Chapter 6 for the vanishing theorems.
