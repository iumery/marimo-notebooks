import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    nav_menu = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
        },
        orientation="vertical",
    )
    nav_menu
    return


@app.cell
def _(mo):
    mo.md(r"""# Summary""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. Deformation retraction:
        1. <mark style="background: #BBFABBA6;">A subspace $A \subset X$ is a deformation retract if there is a homotopy $F: X \times I \to X$ such that $f_0 = \text{id}$, $f_1(X) = A$ and $f_t|_A = \text{id}$</mark>;

    2. Retraction:
        1. <mark style="background: #BBFABBA6;">A subspace $A \subset X$ is a retract if there is a continuous map $r: X \to A$ such that $r \circ i = \text{id}$ where $i: A \to X$ is inclusion map</mark>;
        2. If $X$ retracts to $A$, then the induced homomorphism of the inclusion $i: A \to X$ is injective;

    3. Homotopy equivalence:
        1. <mark style="background: #BBFABBA6;">$f: X \to Y$ is called a homotopy equivalence if there is a map $g: Y \to X$ such that $f\circ g \simeq \text{id}$ and $g \circ f \simeq \text{id}$</mark>;
        2. If there exist maps $g, h: Y \to X$ such that $f \circ g \simeq \text{id}$ and $h \circ f \simeq \text{id}$ for $f: X \to Y$, then $f$ is a homotopy equivalence;

    4. Contractible space:
        1. <mark style="background: #BBFABBA6;">A space that is homotopy equivalent with a point is a contractible space</mark>;
        2. Retract of a contractible space is contractible;
        3. $X$ is contractible if and only if every map $f: X \to Y$ is null-homotopic, also if and only if every map $f: Y \to X$ is null-homotopic;

    5. Homology (CW-complex)

    6. Simplicial homology ($\Delta$ or simplicial complex)

    7. Singular homology (topological space)

    8. Universal Mapping Property of Quotient Space:
        1. Let $h: X \rightarrow Y$ be a map which is constant on the equivalence classes of $(X, \sim)$ (meaning that $x \sim y \implies h(x) = h(y)$), then:
            1. $\exists f: X/ \sim \rightarrow Y$ such that $f \circ \pi = h$;
            2. $f$ is continuous if and only if $h$ is continuous;
            3. $f$ is a quotient map if and only if $h$ is a quotient map;
    
    9. Construction of spaces:
        1. <mark style="background: #BBFABBA6;">Cone of $X$: $CX = (X \times I)/(X \times \lbrace 1 \rbrace)$</mark>;
        2. <mark style="background: #BBFABBA6;">Suspension of $X$: $SX = CX/(X \times \lbrace 0 \rbrace)$</mark>, $SS^n = S^{n+1}$;
        3. <mark style="background: #BBFABBA6;">Reduced suspension of $(X,x)$: $\Sigma X = SX/(x \times I)$</mark>;
        4. <mark style="background: #BBFABBA6;">Wedge sum of $X$ and $Y$: $X \vee Y = (X \cup Y)/(x \sim y)$</mark>;
        5. If $A \subset Y$ is a sub-complex, $f, g: A \to X$ are homotopic, then $X \cup_f Y \simeq X \cup_g Y$;
    
    10. Homotopy Extension Property:
        1. <mark style="background: #BBFABBA6;">A subspace $A \subset X$ is said to have HEP if for all homotopy $H: A \to Y$ and all map $f_0: X \to Y$ such that $f_0|_A = h_0$, there exists a homotopy $F: X \to Y$ such that $f_t|_A = h_t$</mark>;
        2. If $A \subset X$ is sub-complex, then $A$ has HEP;
        3. If $A \subset X$ with HEP is contractible, then $X \simeq X/A$ via projection;
        4. If $A \subset X$ is sub-complex, then $(X \cup CA)/CA \simeq X \cup CA$;
        5. If $A \subset X$ has HEP and the inclusion $i: A \to X$ is a homotopy equivalence, then $A$ is a deformation retract of $X$;
        6. Two spaces $X, Y$ are homotopy equivalent if and only if there is a third space containing both $X, Y$ as deformation retracts;
        7. <mark style="background: #FFB86CA6;">$S^n/S^m \simeq S^n \vee S^{m+1}$</mark>;
        8. If $X$ is a CW-complex, then $SX \simeq \Sigma X$;
    
    11. Chain maps:
        1. <mark style="background: #BBFABBA6;">A sequence $f_n$ is a chain map if for all $n$, the diagram commutes</mark>: $$\begin{array}{rrr}C_n(X) &\to& C_{n-1}(X) \\ \downarrow_{f_n} & & \downarrow_{f_{n-1}} \\ C_n(Y)&\to&C_{n-1}(Y)\end{array}$$
    
    12. Chain homotopy:
        1. <mark style="background: #BBFABBA6;">A sequence of homomorphism $p_n: C_n(X) \to C_{n+1}(Y)$ is a chain homotopy between $f_n$ and $g_n$ if $p_{n-1} \circ \partial_n^X + \partial_{n+1}^Y \circ p_{n} = g_n - f_n$ for each $n$</mark>;
    
    13. <mark style="background: #FF5582A6;">Long exact sequence of a pair</mark>:
    
        1. Let $A \subset X$ be a subspace, then the inclusion $i: A \to X$ induces: $$\begin{array}{rrr}&H_*(A) &\\\nearrow_{-1}&\searrow_{i_*}\\H_*(X,A)&\xleftarrow{}&H_*(X) \end{array}$$
        2. If $\varnothing \ne A \subset X$ is sub-complex, then $H_n(X,A) \cong \tilde{H_n}(X/A)$ induced by the map $q: (X, A) \to (X/A, A/A)$ that is induced by quotient;
        3. If $\varnothing \ne A \subset X$, then $H_n(X, A) \cong \tilde{H_n}(X \cup CA)$:
            1. <mark style="background: #FFB86CA6;">$H_n(\Sigma X) \cong H_n(SX) \cong H_{n-1}(X)$</mark>;
            2. $H_n(S^k) \cong H_{n-1}(S^{k-1})$;
        4. $H_n(X,\lbrace x \rbrace) \cong \tilde{H_n}(X)$, $H_n(X, \varnothing) \cong H_n(X)$, $H_n(X,X) = 0$;
        5. $H_0(X, A) = 0$ if and only if $A$ meets each path-component of $X$;
        6. $H_1(X, A) = 0$ if and only if $H_1(A) \to H_1(X)$ is surjective and each path-component of $X$ contains at most one path-component of $A$;
        7. If $X$ is an $n$-dimensional CW-complex, then $H_n(X)$ is free;
    
    14. Long exact sequence of a triple:
        1. Let $A \subset V \subset X$ be subspaces, then the inclusions induce: $$\begin{array}{rrr}&H_*(V,A) &\\\nearrow_{-1}&\searrow\\H_*(X,A)&\xleftarrow{} & H_*(X,V) \end{array}$$
        2. (Excision) If $A \subset V \subset X$ with $\overline{A} \subset V^{\circ} \subset X$, then the induced homomorphism for inclusion $i: (X - A, V - A) \to (X, V)$ is isomorphism for each $n$;
        3. If $A \subset X$ is a sub-complex, then there exists open neighborhood $V$ of $A$ such that $A \subset V$ is a deformation retract;
        4. If $A, B \subset X$ are sub-complexes with $A \cup B = X$, then the induced homomorphism for inclusion $i: (B, A \cap B) \to (X, A)$ is isomorphism for each $n$;
    
    15. Five Lemma:
        1. Consider: $$\begin{array} {ccccccccc} A & \to &B &\to &C&\to&D& \to& E \\ \downarrow^{\alpha}&\circ&\downarrow^{\beta} &\circ&\downarrow^{\gamma}&\circ&\downarrow^{\delta}&\circ&\downarrow^{\varepsilon} \\A' & \to &B' &\to &C'&\to& D'& \to& E'\end{array}$$ where the two rows are exact, $\beta, \delta$ are isomorphisms, $\alpha$ is epimorphism, and $\varepsilon$ is monomorphism, then $\gamma$ is isomorphism;
    
    16. Local homology:
        1. <mark style="background: #BBFABBA6;">The groups $H_n(X, X - \lbrace x \rbrace)$ are called the local homology groups of $X$ at $x$</mark>;
        2. If $X$ is an $n$-manifold, then $H_k(X, X - \lbrace x \rbrace) \cong H_k(\mathbb{R}^n, \mathbb{R}^n - \lbrace x \rbrace) = \mathbb{Z}$ if $k = n$ and $0$ otherwise;
    
    17. Cellular homology:
        1. $H_n(X) \cong H_n(X^{(n+1)}) \cong H_n(X^{(n+2)}) \cong \dots$ if $\dim(X) < \infty$;
    
    18. Degree of $f: S^n \to S^n$:
        1. <mark style="background: #BBFABBA6;">Let $f: S^n \to S^n$, then $f_*: \tilde{H_n}(S^n) \to \tilde{H_n}(S^n)$ is a homomorphism $f_*: \mathbb{Z} \to \mathbb{Z}$ thus a multiplication by $d$, define $\deg(f) = d$</mark>;
        2. If $f \simeq g$, then $\deg(f) = \deg(g)$;
        3. $\deg(f\circ g) = \deg(f)\cdot \deg(g)$;
        4. $\deg(Sf) = \deg(f)$;
        5. If $f: S^n \to S^n$ has no fixed point, then $\deg(f) = (-1)^{n+1}$;
        6. Identity map on $S^n$ has degree $1$, antipodal map on $S^n$ has degree $(-1)^{n+1}$;
    
    19. Local degree of $f: X \to Y$ between $n$-manifolds:
        1. <mark style="background: #BBFABBA6;">Let $f: X \to Y$ where $X, Y$ are $n$-manifolds, then for each $x \in X$, $f_*: H_n(X, X-\lbrace x\rbrace) \to H_n(Y, Y - \lbrace f(x) \rbrace)$ is a homomorphism $f_*: \mathbb{Z} \to \mathbb{Z}$ thus a multiplication by $d$, define $\deg_x(f) = d$</mark>;
        2. If $f: S^n \to S^n$ and pre-image of $y$ is $\lbrace x_1, \dots, x_n \rbrace$, then $\deg(f) = \sum\limits_{i}\deg_{x_i}(f)$;
    
    20. <mark style="background: #FF5582A6;">Euler Characteristic</mark>:
    
        1. <mark style="background: #BBFABBA6;">If $X$ is a finite CW-complex, then $\chi(X) = \sum\limits_i(-1)^i\cdot(\#\text{ of }i\text{ -cells})$</mark>;
        2. $\chi(X) = \sum\limits_i(-1)^i\text{rank}(H_i(X))$ $= \sum\limits_i(-1)^i\text{rank}(H^i(X))$;
        3. If $X \simeq Y$, then $\chi(X) = \chi(Y)$;
        4. If $X$ and $Y$ are finite CW-complexes, then $\chi(X \times Y) = \chi(X)\cdot\chi(Y)$;
        5. If $p: \tilde{X} \to X$ is an $n$-fold cover, then $\chi(\tilde{X}) = n\cdot \chi(X)$;
        6. Let $A_n, B_n, C_n$ be finitely generated abelian groups with the long exact sequence $\dots \to A_n \to B_n$ $\to C_n \to A_{n-1} \to B_{n-1}$ $\to C_{n-1} \to \dots \to C_0 \to 0$, let $\chi(A) = \sum\limits_{i = 0}^{\infty}(-1)^i\text{rank}(A_i)$ (resp. $B, C$), then $\chi(B) = \chi(A) + \chi(C)$;
        7. <mark style="background: #FFB86CA6;">If $X$ is closed odd-dimensional-manifold, then $\chi(X) = 0$</mark>;
    
    21. Splitting Lemma:
        1. For a short exact sequence $0 \to A \xrightarrow{i} B \xrightarrow{j} C \to 0$ of abelian groups, $B \cong A \oplus C$ if and only if there is a homomorphism $p: B \to A$ such that $p \circ i = \text{id}$, also if and only if there is a homomorphism $q: C \to B$ such that $j\circ q = \text{id}$;
    
    22. Mayer-Vietoris Long Exact Sequence:
        1. <mark style="background: #BBFABBA6;">Let $X$ be a CW-complex with sub-complexes $A, B$ such that $A \cup B = X$, let $i_A: A\cap B \to A$, $i_B: A \cap B \to B$, $j_A: A \to X$ and $j_B: B \to X$, define $i(e) = (i_{A*}(e), -i_{B*}(e))$ and $j(e_A, e_B) = j_{A*}(e_A) + j_{B*}(e_B)$, then they induces the Mayer-Vietoris LES</mark> $$\begin{array}{rrr}&H_*(A\cap B) &\\\nearrow_{-1}&\searrow_{i}\\H_*(X)&\xleftarrow{j}&H_*(A) \oplus H_*(B) \end{array}$$ <mark style="background: #BBFABBA6;">works also with reduced homology</mark>;
    
    23. Cohomology with coefficient

    24. Reduced cohomology

    25. Relative cohomology

    26. Long exact sequence of a pair for cohomology: $$\begin{array}{rrr}&H^*(X,A;G) &\\\nearrow_{+1}&\searrow\\H^*(A;G)&\xleftarrow{i^*}&H^*(X;G) \end{array}$$
    
    27. Mayer-Vietoris Long Exact Sequence for Cohomology: $$\begin{array}{rrr}&H^*(X;G) &\\\nearrow_{+1}&\searrow^{(j_A^*,j_B^*)}\\H^*(A\cap B;G)&\xleftarrow{i_A^*-i_b^*}&H^*(A;G)\oplus H^*(B;G) \end{array}$$
    
    28. <mark style="background: #FFB86CA6;">Universal Coefficient Theorem for Cohomology</mark>:
    
        1. $H^n(X; G) \cong \text{Hom}(H_n(X), G) \oplus \text{Ext}(H_{n-1}(X), G)$;
        2. $\text{rank}(H_n(X)) = \text{rank}(H^n(X))$;
        3. $H^0(X; G) \cong \text{Hom}(H_0(X), G)$;
        4. $H^1(X; G) \cong \text{Hom}(H_1(X), G)$;
        5. $H^n(X; \mathbb{Q}) \cong \text{Hom}(H_n(X), \mathbb{Q})$;
        6. If the homology groups $H_n(X)$ and $H_{n-1}(X)$ are finitely generated, denote $T_i(X)$ to be the torsion subgroup of $H_i(X)$, then $H^n(X) \cong (H_n(X)/T_n(X))\oplus T_{n-1}(X)$;
    
    29. <mark style="background: #FFB86CA6;">Tensor product $A \otimes B$</mark>:
    
        1. $$\begin{array} {|r|r|r|}\hline A\diagdown B & \mathbb{Z} & \mathbb{Z}_m \\ \hline \mathbb{Z} & \mathbb{Z} & \mathbb{Z}_m \\ \hline \mathbb{Z}_n & \mathbb{Z}_n & \mathbb{Z}_{\gcd(n,m)} \\ \hline \end{array}$$
        2. $A \otimes B \cong B \otimes A$;
        3. $A \otimes \mathbb{Q} \cong \mathbb{Q}^{\text{rank}(A)}$;
        4. $A \otimes \mathbb{Z} \cong A$;
        5. Distributivity with direct sum;
        6. For a given $G$, $f: A \to B$ between abelian groups induces $f^*: A\otimes G \to B \otimes G$ with $a \otimes g \mapsto f(a) \otimes g$; $f: \mathbb{Z} \xrightarrow{\cdot n} \mathbb{Z}$ induces $f^*: G \xrightarrow{\cdot n} G$;
    
    30. Homology with coefficient:
        1. <mark style="background: #FFB86CA6;">$H^n(X; \mathbb{Z}_p) \cong \text{Hom}(H_n(X;\mathbb{Z}_p), \mathbb{Z}_p)$</mark>;
        2. If $f: S^n \to S^n$ has degree $d$, then $f_*: H_k(S^k; G) \to H_k(S^k; G)$ is multiplication by $d$;
    
    31. <mark style="background: #FFB86CA6;">Universal Coefficient Theorem for Homology</mark>:
    
        1. $H_n(X; G)\cong (H_n(X) \otimes G) \oplus \text{Tor}(H_{n-1}(X), G)$;
        2. $H_n(X; \mathbb{Q}) \cong H_n(X) \otimes \mathbb{Q}$;
        3. $H_n(X, A; G) \cong (H_n(X,A) \otimes G) \oplus \text{Tor}(H_{n-1}(X, A), G)$;
    
    32. <mark style="background: #FFB86CA6;">$\text{Hom}(A, B)$</mark>:
    
        1. $$\begin{array} {|r|r|r|}\hline A\diagdown B & \mathbb{Z} & \mathbb{Z}_m \\ \hline \mathbb{Z} & \mathbb{Z} & \mathbb{Z}_m \\ \hline \mathbb{Z}_n & 0 & \mathbb{Z}_{\gcd(n,m)} \\ \hline \end{array}$$
        2. $\text{Hom}(A, \mathbb{Q}) = \mathbb{Q}^{\text{rank}(A)}$;
        3. For a given $G$, $f: A \to B$ between abelian groups induces $f^*: \text{Hom}(B, G) \to \text{Hom}(A, G)$; $f: \mathbb{Z} \xrightarrow{\cdot n} \mathbb{Z}$ induces $f^*: G \xrightarrow{\cdot n} G$;
        4. Naturality with direct sum;
    
    33. <mark style="background: #FFB86CA6;">$\text{Ext}(A, B)$</mark>:
    
        1. $$\begin{array} {|r|r|r|}\hline A\diagdown B & \mathbb{Z} & \mathbb{Z}_m \\ \hline \mathbb{Z} & 0 & 0 \\ \hline \mathbb{Z}_n & \mathbb{Z}_n & \mathbb{Z}_{\gcd(n,m)} \\ \hline \end{array}$$
        2. $\text{Ext}(A, \mathbb{Q}) = 0$;
        3. Naturality with direct sum;
        4. $\text{Ext}(H, \mathbb{Z})$ is isomorphic to the torsion subgroup of $H$ if it is finitely generated;
    
    34. <mark style="background: #FFB86CA6;">$\text{Tor}(A, B)$</mark>:
    
        1. $$\begin{array} {|r|r|r|}\hline A\diagdown B & \mathbb{Z} & \mathbb{Z}_m \\ \hline \mathbb{Z} & 0 & 0 \\ \hline \mathbb{Z}_n & 0 & \mathbb{Z}_{\gcd(n,m)} \\ \hline \end{array}$$
        2. $\text{Tor}(A, B) = 0$ if either $A$ or $B$ is torsion free;
    
    35. Geometric meaning of generators of $H^1(F)$ and $H^2(F)$ where $F$ is closed surface

    36. Cup product:
        1. <mark style="background: #BBFABBA6;">For $\varphi \in C^k(X; R)$ and $\psi \in C^l(X; R)$, define $\varphi \cup \psi \in C^{k+l}(X; R)$ by $(\sigma: \Delta^{k+l} \to X)$ $\mapsto \varphi(\sigma|_{[v_0,\dots, v_k]})$ $\cdot \psi(\sigma|_{[v_k, \dots, v_{k+l}]})$, it is well defined on $H^{k}(X;R) \times H^l(X;R) \to H^{k+l}(X;R)$</mark>;
        2. Induced homomorphism $f^*: H^n(Y; R) \to H^n(X; R)$ satisfies $f^*(\alpha \cup \beta) = f^*(\alpha) \cup f^*(\beta)$;
        3. If $\alpha \in H^k(X, A; R)$ and $\beta \in H^l(X, A; R)$, then $\alpha \cup \beta = (-1)^{kl}(\beta \cup \alpha)$;
    
    37. <mark style="background: #FF5582A6;">Orientation</mark>:
    
        1. <mark style="background: #BBFABBA6;">A local orientation of an $n$-manifold $X$ at $x$ is a choice of generator of $H_n(X, X - \lbrace x \rbrace) \cong \mathbb{Z}$, an orientation of $X$ is a consistent choice of local orientation</mark>;
        2. If $X$ is closed $n$-manifold, then $H_n(X) \cong \mathbb{Z}$ if $X$ is orientable, $H_n(X) = 0$ if $X$ is non-orientable;
        3. <mark style="background: #BBFABBA6;">The fundamental class $[X]$ of an orientable $n$-manifold $X$ is a choice of generator of $H_n(X) \cong \mathbb{Z}$</mark>;
        4. If $X$ is closed $n$-manifold, then $H_n(X; R) \cong R$ if and only if $X$ is $R$-orientable, all closed $n$-manifold is $\mathbb{Z}_2$-orientable;
        5. If $X$ is compact $n$-manifold with boundary, then $H_n(X, \partial X; R) \cong R$ if and only if $X$ is $R$-orientable;
        6. If $X$ is simply-connected, then $X$ is orientable;
        7. <mark style="background: #FFB86CA6;">If $X$ is closed $n$-manifold, then the torsion subgroup of $H_{n-1}(X)$ is trivial if $X$ is orientable and $\mathbb{Z}_2$ if $X$ is non-orientable</mark>;
        8. Covering space of an orientable manifold is orientable;
        9. $X$ and $Y$ are orientable if and only if $X\times Y$ is orientable;
    
    38. Degree of $f: X \to Y$ between orientable $n$-manifolds:
        1. Definitions with homology and cohomology are equivalent;
        2. $f: S^2 \to \Sigma_g$ has $\deg(f) = 0$;
    
    39. Cap product:
        1. <mark style="background: #BBFABBA6;">For $\sigma \in C_k(X, R)$ and $\varphi \in C^l(X, R)$ such that $l<k$, define $\sigma \cap \varphi$ $= \varphi(\sigma|_{[v_0, \dots, v_l ]})$ $\cdot \sigma|_{[v_l,\dots, v_k]}$ $\in C_{k-l}(X,R)$, it is well defined on $H_k(X;R) \times H^l(X;R) \to H_{k-l}(X;R)$</mark>;
    
    40. <mark style="background: #FF5582A6;">Cohomology ring</mark>:
    
        1. Give $H^*(X) \otimes H^*(Y)$ a ring structure $\bigoplus\limits_m\left(\bigoplus\limits_{k+l = m}\left(H^k(X) \otimes H^l(Y)\right)\right)$ by defining product $(a \otimes b)\cdot(c\otimes d) = (-1)^{| b \| c |}(a \cup c)\otimes (b \cup d)$;
    
    41. <mark style="background: #FF5582A6;">Poincaré Duality</mark>:
    
        1. <mark style="background: #FFB86CA6;">If $X$ is closed orientable $n$-manifold, then $H_k(X) \cong H^{n-k}(X)$, where the isomorphism is given by $\varphi \mapsto [X] \cap \varphi$; in particular, $\text{rank}(H_k(X)) = \text{rank}(H_{n-k}(X))$</mark>;
        2. If $X$ is closed $n$-manifold, then $H_k(X; \mathbb{Z}_2) \cong H^{n-k}(X; \mathbb{Z}_2)$;
        3. If $X$ is compact $R$-orientable $n$-manifold where $\partial X$ can be written as $A \cup B$ where $A \cap B$ is common boundary for $A$ and $B$, then $H_k(X,A;R) \cong H^{n-k}(X,B;R)$;
        4. <mark style="background: #FFB86CA6;">If $X$ is closed orientable $n$-manifold and $K$ is a compact, locally contractible subspace, then $H_k(X, X - K) \cong H^{n-k}(K)$</mark>;
    
    42. <mark style="background: #FFB86CA6;">Poincaré Lefschetz Duality</mark>:
    
        1. If $X$ is compact $R$-orientable $n$-manifold with boundary, then $H^k(X; R) \cong H_{n-k}(X, \partial X; R)$ and $H^k(X, \partial X; R) \cong H_{n-k}(X; R)$;
        2. If $X$ is compact odd-dimensional-manifold with boundary, then $\chi(\partial X) = 2\chi(X)$;
        3. Compact manifold does not retract onto its boundary;
    
    43. <mark style="background: #FFB86CA6;">Alexander Duality</mark>:
    
        1. If $K \subset S^n$ is compact and locally contractible proper subspace, then $\tilde{H_i}(S^n \setminus K) \cong \tilde{H}^{n-i-1}(K)$; note that $K \subset \mathbb{R}^n$ can also be viewed as lying in $S^n$;
        2. If $X \subset \mathbb{R}^n$ is compact and locally contractible, then $H_{n-1}(X)$ and $H_{n-2}(X)$ is torsion free; in particular, a closed non-orientable $n$-manifold cannot be embedded in $\mathbb{R}^{n+1}$;
    
    44. Half-Lives-Half-Dies:
        1. <mark style="background: #FFB86CA6;">If $X$ is an orientable $3$-manifold with boundary, then $\text{rank}(\ker i_*: H_1(\partial X) \to H_1(X)) = \frac{1}{2}\text{rank}(H_1(\partial X))$</mark>;
    
    45. <mark style="background: #FF5582A6;">Künneth Formula</mark>:
    
        1. <mark style="background: #FFB86CA6;">$H^m(X \times Y) \cong \left(\bigoplus\limits_{k+l=m}(H^k(X) \otimes H^l(Y))\right) \oplus \left(\bigoplus\limits_{p+q = m+1}\text{Tor}(H^p(X), H^q(Y))\right)$; if either $H^n(X)$ or $H^n(Y)$ are free abelian for all $n$, then $H^*(X \times Y) \cong H^*(X) \otimes H^*(Y)$ as graded ring</mark>;
        2. If $A \subset X$ and $B \subset Y$ are sub-complexes, and if either $H^n(X,A;R)$ or $H^n(Y, B;R)$ are free abelian for all n, then $H^*(X \times Y, A\times Y \cup B \times X; R)$ $\cong H^*(X,A;R) \otimes H^*(Y,B;R)$;
        3. $H_m(X \times Y) \cong \left(\bigoplus\limits_{k+l=m}(H_k(X) \otimes H_l(Y))\right) \oplus \left(\bigoplus\limits_{p+q = m-1}\text{Tor}(H_p(X), H_q(Y))\right)$;
    
    46. Fundamental group

    47. Change of base-point isomorphism:
        1. Let $x_0, x_1 \in X$, $X$ be path-connected, and $\gamma$ be a path connecting $x_0$ and $x_1$, then $\beta_{\gamma}: \pi_1(X,x_0) \to \pi_1(X,x_1)$ defined by $[f] \mapsto [\gamma^{-1}\cdot f \cdot \gamma]$ is the change of base-point isomorphism;
        2. $\pi_1(X)$ is abelian if and only if all change of base-point homomorphism $\beta_{\gamma}$ depend only on the end-points of $\gamma$;
    
    48. Seifert-Van Kampen Theorem:
        1. Suppose that $X = U_1 \cup U_2$ such that $U_1,U_2,U_1\cap U_2$ are non-empty, open and path connected. Choose a base point $x \in U_1 \cap U_2$ and assume $\pi_1(U_1 \cap U_2, x) = \langle S;R \rangle$, $\pi_1(U_j,x) = \langle S_j;R_j \rangle$ for $j = 1,2$. Denote $R_S$ be the set of relations $\varphi_{1{*}}(s) = \varphi_{2{*}}(s)$ for $s \in S$ ($\varphi_j$ is the inclusion map from $U_1 \cap U_2$ to $U_j$), then $\pi_1(X,x)$ is isomorphic to the group defined by the generators $S_1 \cup S_2$ and the relations $R_1 \cup R_2 \cup R_S$;
    
    49. <mark style="background: #FF5582A6;">Covering space</mark>:
    
        1. If $p: \tilde{X} \to X$ and $q: \tilde{Y} \to Y$ are coverings, then $p \times q: \tilde{X} \times \tilde{Y} \to X \times Y$ is covering;
        2. If $p: \tilde{X} \to X$ and $q: \tilde{Y} \to Y$ are coverings where $\tilde{X}, \tilde{Y}$ are simply-connected and $X, Y$ are path-connected and locally path-connected, then if $X \simeq Y$ then $\tilde{X} \simeq \tilde{Y}$;
        3. If $p: \tilde{X} \to X$ is a covering, choose $x \in X$ and $\tilde{x} \in p^{-1}(x)$, then $p_*:\pi_1(\tilde{X},\tilde{x}) \to \pi_1(X, x)$ is injective and $[\pi_1(X,x): p_*(\pi_1(\tilde{X},\tilde{x}))]$ equals the number of sheets of the covering;
        4. Equivalence class of coverings of $X$ is in bijective correspondence with conjugacy classes of subgroups of $\pi_1(X, x)$; <mark style="background: #BBFABBA6;">the covering is said to be regular if the corresponding subgroup is normal, universal if the corresponding subgroup is $1$</mark>;
        5. <mark style="background: #BBFABBA6;">Two coverings $p_1:\tilde{X_1} \to X$ and $p_2: \tilde{X_2} \to X$ are said to be equivalent if there is a homeomorphism $f: \tilde{X_1} \to \tilde{X_2}$</mark>;
        6. Induced homomorphism of covering map is isomorphism on $\pi_n$ if $n \ge 2$;
    
    50. Deck transformation:
        1. <mark style="background: #BBFABBA6;">For a covering $p: \tilde{X} \to X$, the homeomorphisms $d: \tilde{X} \to \tilde{X}$ such that $p\circ d = p$ are called deck transformations, they form a group $G(\tilde{X})$</mark>;
        2. A covering $p: \tilde{X} \to X$ is regular if for each $x \in X$ and each pair $\tilde{x}_1, \tilde{x}_2 \in p^{-1}(x)$ there exists a deck transformation taking $\tilde{x}_1$ to $\tilde{x}_2$;
    
    51. Path Lifting Property:
        1. If $p: \tilde{X} \to X$ is a covering, then for each path $f: I \to X$ which starts at $x$, there exists a unique lift $\tilde{f}: I \to \tilde{X}$ that starts at each $\tilde{x} \in p^{-1}(x)$;
    
    52. Homotopy Lifting Property:
        1. If $p: \tilde{X} \to X$ is a covering, $F: Y \times I \to X$ is a homotopy, and $\tilde{f}_0: Y \to \tilde{X}$ lifts $f_0: Y \to X$, then there exists a unique homotopy $\tilde{F}: Y \times I \to \tilde{X}$ of $\tilde{f}_0$ that lifts $F$;
        2. Let $\gamma_0$ and $\gamma_1$ be paths in $X$ homotopic rel $\lbrace 0, 1 \rbrace$, then their lifts $\tilde{\gamma_0}, \tilde{\gamma_1}$ such that $\tilde{\gamma_0}(0) = \tilde{\gamma_1}(0)$ are still homotopic rel $\lbrace 0 ,1 \rbrace$;
    
    53. <mark style="background: #FF5582A6;">Map Lifting Lemma</mark>:
    
        1. If $p: \tilde{X} \to X$ is a covering, $f: Y \to X$ with $Y$ path-connected and locally path-connected, then a lift $\tilde{f}: Y \to \tilde{X}$ exists if and only if $f_*(\pi_1(Y)) \subset p_*(\pi_1(\tilde{X}))$;
    
    54. Unique Lifting Property:
        1. If $p: \tilde{X} \to X$ is a covering, $f: Y \to X$ with $Y$ connected lifts to $\tilde{f_1}$ and $\tilde{f_2}$ that agree at a point of $Y$, then $\tilde{f_1} = \tilde{f_2}$;
    
    55. Subgroup of free group is free:
        1. <mark style="background: #FFB86CA6;">If $A \subset F_n$ has index $k$, then $\text{rank}(A) = 1 + k(n-1)$</mark>;
    
    56. Covering space action:
        1. <mark style="background: #BBFABBA6;">An action $G$ on $Y$ is a homomorphism $G \to \text{Homeo}(Y)$, under this context we view $g$ as a homeomorphism $Y \to Y$</mark>;
        2. <mark style="background: #BBFABBA6;">An action $G$ on $Y$ is a covering space action if each $y \in Y$ has an open neighborhood $U$ such that $g(U)$ are disjoint for all $g \in G$</mark>;
        3. <mark style="background: #BBFABBA6;">An action $G$ on $Y$ is a free action if no $g: Y \to Y$ has a fixed point except for $g = \text{id}$</mark>;
        4. If $G$ acts on $Y$ by a covering space action, then:
            1. The quotient map $p: Y \to Y/G$ is a regular covering;
            2. $G$ is the group of deck transformations of $p: Y \to Y/G$ if $Y$ is path-connected;
            3. $G$ is isomorphic to $\pi_1(Y/G)/p_*(\pi_1(Y))$ if $Y$ is path-connected and locally path-connected;
        5. Every regular covering is equivalent to a covering $Y \to Y/G$ for some $Y$ and $G$;
    
    57. If $M$ is non-orientable, then there exists an epimorphism $\pi_1(M) \to \mathbb{Z}_2$ (corresponding to this is the orientation double cover); in particular, if $\pi_1(M)$ does not have a subgroup of index $2$, then $M$ is orientable;

    58. Higher homotopy group:
        1. <mark style="background: #BBFABBA6;">An $n$-spheriod in $X$ based at $x$ is a continuous map $f: (I^n, \partial I^n) \to (X, x)$; $\pi_n(X, x)$ is defined to be the set of homotopy classes of $n$-spheriods for $n \ge 1$; $\pi_i(X, x)$ has a group structure for $i \ge 1$, $\pi_i(X, x)$ is abelian for $i \ge 2$</mark>;
    
    59. Cellular Approximation Theorem:
        1. <mark style="background: #BBFABBA6;">$f: X \to Y$ between CW-complexes is a cellular map if it takes $n$-skeleton of $X$ to $n$-skeleton of $Y$ for each $n$</mark>;
        2. Every map $f: X \to Y$ of CW-complexes is homotopic to a cellular map; if $f$ is already cellular on a sub-complex $A \subset X$, then the homotopy can be taken rel $A$;
        3. $\pi_n(X) \cong \pi_n(X^{(n+1)})$;
        4. There exists a $2$-dimensional CW-complex $X$ with $\pi_1(X) \cong G$ for any (finitely presented) group $G$;
    
    60. Relative homotopy group:
        1. <mark style="background: #BBFABBA6;">A relative $n$-spheriod in $(X, A)$ based at $x$ is a continuous map $f: (D^n, S^{n-1}, s) \to (X, A, x)$; $\pi_n(X, A, x)$ is defined to be the set of homotopy classes of relative $n$-spheriods for $n \ge 1$; $\pi_0(X, A, x)$ is not defined, $\pi_i(X, A, x)$ has a group structure for $i \ge 2$, $\pi_i(X, A,x)$ is abelian for $i \ge 3$</mark>;
    
    61. Long exact sequence of a pair for homotopy group:
        1. $$\begin{array}{rrr}&\pi_*(A) &\\\nearrow^{\partial}_{-1}&\searrow_{i_*}\\\pi_*(X,A)&\xleftarrow{j_*}&\pi_*(X) \end{array}$$ where $\partial$ is restriction to $S^{n-1}$;
        2. $\pi_n(X, A, x) \ne \pi_n(X/A, x)$;
    
    62. $n$-connectedness:
        1. <mark style="background: #BBFABBA6;">A space $X$ is $n$-connected if $\pi_i(X) = 0$ for all $i \le n$</mark>;
        2. <mark style="background: #BBFABBA6;">A CW pair $(X, A)$ is $n$-connected if $X \setminus A$ has no cell of dimension $> n$ up to homotopy equivalence</mark>;
    
    63. Freudanthal Theorem:
        1. <mark style="background: #BBFABBA6;">The map $\pi_n(X) \to \pi_{n+1}(\Sigma X)$ defined by $[f] \mapsto [\Sigma f]$ is called the suspension homomorphism</mark>;
        2. <mark style="background: #FFB86CA6;">If $X$ is an $(n-1)$-connected CW-complex, then the suspension homomorphism $\pi_k(X) \to \pi_{k+1}(\Sigma X)$ is an isomorphism for $k<2n-1$ and epimorphism for $k = 2n-1$</mark>;
        3. If $A \subset X$ is a sub-complex, $A$ is $s$-connected, $X$ is $r$-connected, then the map $\pi_k(X,A) \to \pi_k(X/A)$ induced by quotient map $X \to X/A$ is an isomorphism for $k<r+s+1$ and epimorphism for $k = r+s+1$;
    
    64. <mark style="background: #FF5582A6;">Whitehead Theorem</mark>:
    
        1. If a map $f: X \to Y$ between CW-complexes induces isomorphisms $f_*: \pi_n(X) \to \pi_n(Y)$ for all $n$, then $f$ is a homotopy equivalence; if $f$ is an inclusion map, then $X$ is a deformation retract of $Y$;
        2. If $X$ is a CW-complex with $\pi_n(X) = 0$ for all $n$, then $X$ is contractible;
        3. If a map $f: X \to Y$ between simply-connected CW-complexes induces isomorphisms $f_*: H_n(X) \to H_n(Y)$ for all $n$, then $f$ is a homotopy equivalence;
        4. If $X$ is a simply-connected CW-complex with $\tilde{H_n}(X) = 0$ for all $n$, then $X$ is contractible;
    
    65. Compression Lemma:
        1. <mark style="background: #FFB86CA6;">Let $A \subset X$ be sub-complex and $\varnothing \ne B \subset Y$ be subspace, if $\pi_n(Y, B, y) = 0$ for each $y \in B$ for each $n$ such that $X \setminus A$ has cells of dimension $n$, then every map $f: (X, A) \to (Y, B)$ is homotopic rel $A$ to a map $g: X \to B$</mark>;
        2. Let $A \subset X$ be sub-complex, $Y$ be path-connected, $f: A \to Y$, if $\pi_{n-1}(Y) = 0$ for each $n$ such that $X \setminus A$ has cells of dimension $n$, then $f$ can be extended to $F: X \to Y$;
    
    66. Hurewicz Theorem:
        1. <mark style="background: #BBFABBA6;">Given a space $X$, define the Hurewicz homomorphism $h: \pi_n(X) \to H_n(X)$ by $[f] \mapsto f_*([S^n])$; similarly, define $h: \pi_n(X,A) \to H_n(X,A)$ by $[f] \mapsto f_*([D^n, \partial D^n])$</mark>;
        2. <mark style="background: #FFB86CA6;">If $X$ is $(n-1)$-connected, $n \ge 2$, then $\tilde{H_i}(X) = 0$ for $i < n$ and $\pi_n(X) \cong H_n(X)$</mark>;
        3. <mark style="background: #FFB86CA6;">If $(X,A)$ is $(n-1)$-connected (or, if $\pi_0(X/A) = 0$ and $\pi_i(X,A) = 0$ for $1\le i <n$), $n \ge 2$, $A$ is simply-connected and non-empty, then $H_i(X,A) = 0$ for $i < n$ and $\pi_n(X,A) \cong H_n(X, A)$</mark>;
    
    67. Eilenberg-MacLane Space:
        1. <mark style="background: #BBFABBA6;">A connected topological space $X$ is called an Eilenberg-MacLane Space of type $K(G, n)$ if the only non-trivial homotopy group of $X$ is $\pi_n(X) \cong G$</mark>;
        2. For any $n \ge 1$ and $G$ (abelian if $n \ge 2$), there exists a CW-complex that is $K(G, n)$ that is unique up to homotopy equivalence;
        3. If a finite-dimensional CW-complex $X$ is a $K(G, 1)$, then $G$ is torsion free;
        4. <mark style="background: #FFB86CA6;">Denote $[X,Y]$ to be the set of homotopy classes of maps $X \to Y$; if $X$ is a path-connected CW-complex and $G$ is an abelian group, $n \ge  1$, then there is a natural bijection $[X, K(G,n)] \to H^n(X;G)$</mark>;
        5. $[X, S^n] \cong H^n(X;\mathbb{Z})$.

    """
    )
    return


if __name__ == "__main__":
    app.run()
