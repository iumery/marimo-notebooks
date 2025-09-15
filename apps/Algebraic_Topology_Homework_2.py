import marimo

__generated_with = "0.15.4"
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
    mo.md(r"""# Spring Semester Homework 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 18

    **For the closed orientable surface $M$ of genus $g\ge 1$, show that for each non-zero $\alpha \in H^1(M;\mathbb{Z})$ there exists $\beta \in H^1(M;\mathbb{Z})$ with $\alpha \beta \ne 0$. Deduce that $M$ is not homotopy equivalent to a wedge sum $X \vee Y$ of CW-complexes with non-trivial reduced homology. Do the same for closed non-orientable surfaces using cohomology with $\mathbb{Z}_2$ coefficients**.

    Proof

    <img src="public/Pasted image 20230121190401.png" width="300" />

    Examine Example 3.7. With the usual $\Delta$-complex structure we have for $M$, we have that the cup product of (cohomology classes) $\alpha_i$ and $\beta_j$ is $\alpha_i \cup \beta_j = \begin{cases}\gamma,&i = j\\ 0,&i\ne j\end{cases}$ for $\gamma$ being the dual generator of $H^2(M;\mathbb{Z})$. In particular, for any $\alpha$ that equals $\alpha_i$ or $\beta_j$, we can easily find $\beta$ such that $\alpha \beta \ne 0$. Since we know that $\alpha_i$ and $\beta_j$ form a basis for $H^1(M; \mathbb{Z})$ and cup product is distributive, the desired statement also works for any $\alpha \in H^1(M; \mathbb{Z})$.

    Suppose $M$ is homotopy equivalent to a wedge sum $X \vee Y$, then their reduced (co)homology groups are isomorphic. In particular, $H^2(X \vee Y; \mathbb{Z}) \cong$ $H^2(M; \mathbb{Z}) \cong$ $\mathbb{Z}$. Since $H^2(X \vee Y; \mathbb{Z}) = H^2(X; \mathbb{Z}) \times H^2(Y;\mathbb{Z})$, we must have one of $H^2(X; \mathbb{Z})$ and $H^2(Y;\mathbb{Z})$ is $\mathbb{Z}$ and the other is $0$.

    WLOG, say $H^2(X; \mathbb{Z}) = 0$. With similar argument, it is easy to see $H^n(X; \mathbb{Z}) = 0$ for all $n > 2$ and $n = 0$. But we assume $X$ has non-trivial reduced homology, thus $H^1(X; \mathbb{Z})$ must not be $0$. Thus we can pick some $\alpha \in H^1(X; \mathbb{Z})$ that is non-zero.

    Let $\beta \in H^1(X \vee Y; \mathbb{Z})$ be any element and consider inclusions $i_X: X \to X \vee Y$, $i_Y: Y \to X \vee Y$ which induce $i_X^*: H^*(X \vee Y; \mathbb{Z}) \to H^*(X; \mathbb{Z})$ and $i_Y^*: H^*(X \vee Y; \mathbb{Z}) \to H^*(Y; \mathbb{Z})$:

    1. Since $H^2(X; \mathbb{Z}) = 0$, we always have $H^2(X; \mathbb{Z}) \ni i_X^*(\alpha\beta) = 0$;
    2. Since $\alpha \in H^1(X; \mathbb{Z})$, we have $i_Y^*(\alpha)=0$ thus $i_Y^*(\alpha\beta) = 0$ because it's a ring homomorphism.

    Since $i_X^*$ and $i_Y^*$ induce isomorphism $H^2(X \vee Y; \mathbb{Z}) \cong H^2(X; \mathbb{Z}) \times H^2(Y; \mathbb{Z})$, and the image of $\alpha\beta$ under this isomorphism is $0$, we must have that $\alpha\beta \in H^2(X \vee Y; \mathbb{Z})$ is $0$.

    But we also have that $H^2(X \vee Y; \mathbb{Z})$ is isomorphic to $H^2(M; \mathbb{Z})$, thus we have find some non-zero $\alpha_M \in H^1(M; \mathbb{Z})$ such that $\alpha_M \beta_M = 0$ for all $\beta_M \in H^1(M; \mathbb{Z})$, which contradict the statement we have above.

    <img src="public/Pasted image 20230122120532.png" width="300" />

    For the cohomology of non-orientable surface with $\mathbb{Z}_2$ coefficients, examine Example 3.8 with the $\Delta$-complex structure on the right, then we know the product $\alpha_i \alpha_i$ is non-zero. Since $\alpha_i$'s form a basis for $H^1(M; \mathbb{Z}_2)$, we have the desired statement.

    For the second part, since for a non-orientable surface (so dimension is $2$), we must have that $H^2(M; \mathbb{Z}_2) \cong \mathbb{Z}_2$. So that if $M$ is homotopy equivalent with $X \vee Y$ then we must have that exactly one of $H^2(X; \mathbb{Z}_2)$ and $H^2(Y; \mathbb{Z}_2)$ is $\mathbb{Z}_2$, and we can follow the same argument to get the result.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 11

    **If $M_g$ denotes the closed orientable surface of genus $g$, show that degree $1$ maps $M_g \to M_h$ exists iff $g \ge h$**.

    Proof

    Suppose $g\ge h$, consider the map that maps $M_{g'}$, the interior of a surface of genus $h$ with one boundary circle, into $M_h$ minus a point $x$ in a natural way, and that maps the rest ($M_g \setminus M_{g'}$) to the single point $x$. This map has $x$ as the only critical point and has degree $1$.

    Suppose $g < h$. Suppose a degree $1$ map $f: M_g \to M_h$ exists, then by the previous question, $f_*: H_1(M_g) \cong \mathbb{Z}^{2g} \to H_1(M_h) \cong \mathbb{Z}^{2h}$ is surjective, which is impossible. So the other direction also holds and we get the if and only if statement.

    ## Problem 12

    **As an algebraic application of the preceding problem, show that in a free group $F$ with basis $x_1, \dots, x_{2k}$, the product of commutators $[x_1,x_2]\dots[x_{2k-1}, x_{2k}]$ is not equal to a product of fewer than $k$ commutators $[v_i, w_i]$ of elements $v_i, w_i \in F$**. *Hint: Recall that the $2$-ell of $M_k$ is attached by the product $[x_1,x_2]\dots[x_{2k-1},x_{2k}]$. From a relation $[x_1,x_2]\dots[x_{2k-1},x_{2k}]$ $= [v_1,w_1]\dots[v_j,w_j]$ in $F$, construct a degree $1$ map $M_j \to M_k$*.

    Proof

    Consider CW-complex structures on $M_j$ (with edges $a_1,\dots,a_{2j}$) and $M_k$ (with edges $x_1,\dots,x_{2k}$) of genus $j, k$ closed orientable surfaces. Define a map $f$ maps between the $1$-skeletons, such that $a_{2i-1}$ is mapped to $v_i$, and $a_{2i}$ is mapped to $w_i$. Then the product $[a_1,a_2]\dots [a_{2j-1},a_{2j}]$ is mapped to $[v_1,w_1]\dots[v_j,w_j]$ which by assumption equals $[x_1,x_2]\dots[x_{2k-1},x_{2k}]$.

    Extend $f$ to $F: M_j \to M_k$, since the edges are mapped as above, the $2$-cell of $M_j$ is mapped (homeomorphically) to the $2$-cell of $M_k$, thus $F$ has degree $1$, but then the previous question gives a contradiction because $j \not\ge k$.

    ## Problem 13

    **Let $M_h' \subset M_g$ be a compact subsurface of genus $h$ with one boundary circle, so $M_h'$ is homeomorphic to $M_h$ with an open disk removed. Show there is no retraction $M_g \to M_h'$ if $h > g/2$**. *Hint: Apply the previous problem, using the fact that $M_g - M_h'$ has genus $g - h$*.

    Proof

    Assume we have a retraction $r: M_g \to M_h'$. Consider the surface $\overline{M_g - M_h'}$, it has genus $g - h$ with one boundary circle. So we can define a map $i: M_{g-h} \to \overline{M_g - M_h'}$ where it maps all point but one naturally to $\overline{M_g - M_h'}$, and maps the remaining one point to an arbitrary point on the boundary circle of $\overline{M_g - M_h'}$.

    Consider $r \circ i: M_{g-h} \to \overline{M_g - M_h'} \to M_h'$. We have $\deg(r) = 1$ because it is a retraction, and $\deg(i) = 1$ because it can be understood as an inclusion. Thus $\deg(r \circ i) = 1$ but $g - h< h$ because $g<2h$, thus we have a contradiction from question 11.

    ## Problem 24

    **Let $M$ be a closed connected $3$-manifold, and write $H_1(M;\mathbb{Z})$ as $\mathbb{Z}^r \oplus F$, the direct sum of a free abelian group of rank $r$ and a finite group $F$. Show that $H_2(M; \mathbb{Z})$ is $\mathbb{Z}^r$ if $M$ is orientable and $\mathbb{Z}^{r-1} \oplus \mathbb{Z}_2$ if $M$ is non-orientable**.

    Proof

    1. Suppose $M$ is orientable. We know that $H_3(M;\mathbb{Z}) \cong \mathbb{Z}$ (orientable, dimension $3$), $H_0(M; \mathbb{Z}) \cong \mathbb{Z}$ (connected), and $H_i(M;\mathbb{Z}) = 0$ whenever $i>3$ (dimension $3$). By Corollary 3.37, we have that $\chi(M) = 0$. Recall now that the Euler characteristic is the alternating sum of rank of homology groups: since we assume $H_1(M;\mathbb{Z})$ has rank $r$, we must have $H_2(M; \mathbb{Z})$ also have rank $r$. By Corollary 3.28, $H_{3-1}(M; \mathbb{Z})$ is torsion-free, thus $H_2(M; \mathbb{Z}) = \mathbb{Z}^r$;
    2. Suppose $M$ is non-orientable. Follow the same argument, this time we have $H_3(M; \mathbb{Z}) \cong 0$, thus $H_2(M; \mathbb{Z})$ has rank $r-1$ by Corollary 3.37. Again by Corollary 3.28, we get that torsion of $H_2(M; \mathbb{Z})$ is $\mathbb{Z}_2$ thus we have $H_2(M;\mathbb{Z}) \cong \mathbb{Z}^{r-1} \oplus \mathbb{Z}_2$.

    ## Problem 25

    **Show that if a closed orientable manifold $M$ of dimension $2k$ has $H_{k-1}(M;\mathbb{Z})$ torsion-free, then $H_k(M; \mathbb{Z})$ is also torsion-free**.

    Proof

    The UCT for cohomology says that the following exact sequence splits: $$0 \to \text{Ext}(H_{n-1}(M;\mathbb{Z}),\mathbb{Z}) \to H^n(M;\mathbb{Z}) \to \text{Hom}(H_n(M;\mathbb{Z}),\mathbb{Z}) \to 0,$$ where $\text{Ext}(H, \mathbb{Z})$ is isomorphic to the torsion subgroup of $H$ (if it is finitely generated), and $\text{Hom}(H, \mathbb{Z})$ is isomorphic to certain $\mathbb{Z}^b$ where $b$ is the Betti number. Thus we have that $H^k(M;\mathbb{Z}) \cong \mathbb{Z}^b \oplus T_{k-1}$ (take $n = k$).

    Poincaré Duality says that $H^k(M;\mathbb{Z}) \cong H_{2k-k = k}(M; \mathbb{Z})$. Now if $T_{k-1}$ is trivial as assumed, then $H^k(M;\mathbb{Z}) \cong \mathbb{Z}^b$ $\cong H_k(M;\mathbb{Z})$ which just means $T_k$ is also trivial.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 3

    **Using the cup product structure, show there is no map $\mathbb{R}P^n \to \mathbb{R}P^m$ inducing a non-trivial map $H^1(\mathbb{R}P^m;\mathbb{Z}_2)$ $\to H^1(\mathbb{R}P^n;\mathbb{Z}_2)$ if $n > m$. What is the corresponding result for maps $\mathbb{C}P^n \to \mathbb{C}P^m$**?

    Proof

    Suppose we have some $f: \mathbb{R}P^n \to \mathbb{R}P^m$ which induces homomorphism $f^*: H^1(\mathbb{R}P^m; \mathbb{Z}_2) \to H^1(\mathbb{R}P^n;\mathbb{Z}_2)$. Since both groups are isomorphic to $\mathbb{Z}_2$, the only non-trivial map is the map sending $\alpha$ (generator of the domain) to $\beta$ (generator of the codomain).

    Now consider the induced map between cohomology ring $f^*: \mathbb{Z}_2[\alpha]/(\alpha^{m+1}) \to \mathbb{Z}_2[\beta]/(\beta^{n+1})$ where the former ring is generated by $\alpha$ and the latter ring is generated by $\beta$, then by above, $\alpha$ is sent to $\beta$. In the (domain) polynomial ring $\alpha^{m+1} = 0$, so we have $0 = f^*(\alpha^{m+1})$ $=(f^*(\alpha))^{m+1}$ $=\beta^{m+1}$ but it is not $0$ because $n+1>m+1$, so we have a contradiction.

    There is no map $\mathbb{C}P^n \to \mathbb{C}P^m$ inducing a non-trivial map $H^2(\mathbb{C}P^m;\mathbb{Z})$ $\to H^2(\mathbb{C}P^n;\mathbb{Z})$: we know these groups are (isomorphic to) $\mathbb{Z}$, so the possible non-trivial maps map $\alpha$ (generator of domain) to $k\beta$ ($\beta$ is generator of codomain, $k$ is non-zero integer). Again consider the induced map between cohomology ring $f^*: \mathbb{Z}[\alpha]/(\alpha^{m+1}) \to \mathbb{Z}[\beta]/(\beta^{n+1})$ that maps $\alpha$ to $k \beta$, it maps $0 = a^{m+1}$ to $(k\beta)^{m+1}$ which is not zero by the same reason, and we have a contradiction again.

    ## Problem 7

    **Use cup products to show that $\mathbb{R}P^3$ is not homotopy equivalent to $\mathbb{R}P^2 \vee S^3$**.

    Proof

    The cohomology ring of $\mathbb{R}P^3$ with $\mathbb{Z}_2$ coefficients is $\mathbb{Z}_2[\alpha]/(\alpha^4)$ (generated by $1, \alpha, \alpha^2, \alpha^3$ in each dimension, respectively). If we consider the reduced version then $\tilde{H^0}(\mathbb{R}P^3;\mathbb{Z}_2) = 0$ (the $0$-dimensional generator disappears) thus $\tilde{H^*}(\mathbb{R}P^3;\mathbb{Z}_2)$ is the sub-ring $R_1$ of $\mathbb{Z}_2[\alpha]/(\alpha^4)$ consisting of polynomials without constant term.

    Similarly, $\tilde{H^*}(\mathbb{R}P^2;\mathbb{Z}_2)$ is the sub-ring $R_2$ of $\mathbb{Z}_2[\beta]/(\beta^3)$ without constant term, $\tilde{H^*}(S^3;\mathbb{Z}_2)$ is the sub-ring $R_3$ of $\mathbb{Z}_2[\gamma]/(\gamma^2)$ without constant term. Since the reduced cohomology ring of wedge sum is just product of reduced cohomology rings, we get that $\tilde{H^*}(\mathbb{R}P^2 \vee S^3;\mathbb{Z}_2) \cong R_2 \times R_3$.

    But now $R_1$ and $R_2 \times R_3$ are not isomorphic: $\alpha \in R_1$ is an element with order $4$ but there is no such element in $R_2 \times R_3$.

    ## Problem 11

    **Using cup products, show that every map $S^{k+l} \to S^k \times S^l$ induces the trivial homomorphism $H_{k+l}(S^{k+l}) \to H_{k+l}(S^k \times S^l)$, assuming $k>0$ and $l>0$**.

    Proof

    Let $f$ be a (continuous) map $S^{k+l} \to S^k \times S^l$, $p_1$ and $p_2$ are projection from $S^k \times S^l$ to $S^k$ and $S^l$, respectively. Then $f$ induces homomorphism $H^{k+l}(S^k \times S^l) \to H^{k+l}(S^{k+l})$. By the Künneth formula, the domain is isomorphic to $\bigoplus\limits_{i+j=k+l}H^i(S^k) \otimes_{\mathbb{Z}} H^j(S^l)$ $\cong H^k(S^k) \otimes_{\mathbb{Z}} H^l(S^l)$ $\cong \mathbb{Z} \otimes_{\mathbb{Z}} \mathbb{Z}$ $\cong \mathbb{Z}$ is generated by $a \otimes b$ where $a, b$ are generators for $H^k(S^k) \cong \mathbb{Z}$ and $H^l(S^l) \cong \mathbb{Z}$, respectively. The isomorphism (in the Künneth formula) is realized by $a \otimes b \leftrightarrow a\times b$ $=p_1^*(a) \cup p_2^*(b)$.

    Write $f^*(a \times b)$ $= f^*(p_1^*(a) \cup p_2^*(b))$ $=f^*(p_1^*(a)) \cup f^*(p_2^*(b))$ $=((p_1\circ f)^*(a))\cup((p_2\circ f)^*(b))$ $= 0 \cup 0 = 0$, because $(p_1\circ f)^*: H^k(S^k) \to H^k(S^{k+l})=0$ and similar for $p_2$, thus $f^*$ maps the only generator to $0$ thus is the trivial homomorphism between cohomology, thus its dual $f_*$ is also the trivial homomorphism between homology.

    ## Problem 32

    **Show that a compact manifold does not retract onto its boundary**.

    Proof

    For simplicity of notation, we assume to use $\mathbb{Z}_2$ coefficients in all cohomology/homology groups in this problem.

    Suppose we have a compact $n$-manifold $M$ with boundary $\partial M$, and suppose $r: M \to \partial M$ is a retraction ($r \circ i = \text{id}_{\partial M}$). We can further assume $M$ is connected because the retraction should take place component-wise anyway. Consider the LES of $(M, \partial M)$: $$\begin{array}{cccccccc} \to & H_n(\partial M) & \to & H_n(M) & \to & H_n(M, \partial M) & \to & \\ \to & H_{n-1}(\partial M) & \xrightarrow{i_*} & H_{n-1}(M) & \to & H_{n-1}(M, \partial M) & \to & \end{array}$$ We have that:

    1. By retraction, the induced homomorphism $i_*$ is injective;
    2. Since all manifolds are $\mathbb{Z}_2$-orientable, Poincaré-Lefschetz Duality applies. $H_n(M) \cong H^0(M,\partial M)$ which $\cong \tilde{H^0}(M/\partial M)$ which is $0$ because $M$ is assumed to be connected;
    3. By orientability, $H_n(M,\partial M) \cong \mathbb{Z}_2$;

    So the following part: $$H_n(M) \to H_n(M,\partial M) \to H_{n-1}(\partial M) \to H_{n-1}(M)$$ is the same as: $$0 \to^0 \mathbb{Z}_2 \xrightarrow{\partial} H_{n-1}(\partial M) \xrightarrow{i_*} H_{n-1}(M).$$ In particular, $\ker{\partial} = \text{im}(0) = 0$, thus $\text{im}(\partial) = \mathbb{Z}_2$ thus $\ker{i_*} = \mathbb{Z}_2$, thus we have a contradiction because $i_*$ should be injective.

    ## Problem 33

    **Show that if $M$ is a compact contractible $n$-manifold then $\partial M$ is a homology $(n-1)$-sphere, that is, $H_i(\partial M;\mathbb{Z}) \cong H_i(S^{n-1};\mathbb{Z})$ for all $i$**.

    Proof

    A point does not have boundary; a compact contractible $1$-manifold can only be a line segment, in which case $\partial M$ equals two points and is a (homology) $0$-sphere. So we can assume $n\ge 2$.

    Suppose $M$ is orientable, then for the following part of LES of pair $$H_n(M) \to H_n(M,\partial M) \to H_{n-1}(\partial M) \to H_{n-1}(M),$$ we have $H_n(M), H_{n-1}(M) \cong 0$ (contractible), thus $H_{n-1}(\partial M)$ $\cong H_n(M, \partial M)$ $\cong \mathbb{Z}$ by definition of orientability. For other $i \ne 0$, use $H_i(\partial M)$ $\cong H_{i+1}(M,\partial M)$ $\cong^{\text{PL Duality}} H^{n-i-1}(M)$ $\cong 0$ because $M$ is contractible, and use reduced (co)homology for $i = 0$ to get $\tilde{H}_0(\partial M) = 0$, we get that $H_i(\partial M) \cong H_i(S^{n-1})$ for all $i$.

    In fact, $M$ can only be orientable. By Prop 3.42, $\partial M$ has a collar neighborhood $c(M)\cong \partial M \times [0,1)$. Consider $M\setminus c(M)$, then $M$ deformation retracts onto it by $H(x,t)$ where $H(x,t)=x$ if $x\in M\setminus c(M)$ and $H(x,t)$ equals the homeomorphic image of $x$ under $c(M) \cong \partial M \times [1-t,1)$ if $x \in c(M)$. $\text{int}(M)$ also deformation retracts onto it (similar $H$, just use the homeomorphism $c(M) \setminus \partial M \cong \partial M\times(0,1)$ instead).

    (Note: interior of contractible space is not necessarily contractible, so we are not 'making things complicated' above)

    Thus $\text{int}(M)= M\setminus \partial M$ is homotopy equivalent with $M$ thus contractible, thus simply connected, thus orientable, thus $M$ is orientable (p. 253).

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 3

    **For a path-connected space $X$, show that $\pi_1(X)$ is abelian if and only if all base-point-change homomorphisms $\beta_h$ depend only on the endpoints of the path $h$**.

    Proof

    Suppose $\pi_1(X,x_0)$ is abelian, and say $g, h$ are two paths from $x_1$ to $x_0$. Let $f$ be an arbitrary loop based at $x_0$, we want to show $\beta_g([f]) = \beta_h([f])$. We have: $$\begin{aligned}\beta_g([f]) &:= [g^{-1}\cdot f\cdot g] \\ &=[h^{-1}\cdot h\cdot g^{-1} \cdot f \cdot g \cdot h^{-1} \cdot h] \\ &=[h^{-1}\cdot (h\cdot g^{-1})\cdot f \cdot (h\cdot g^{-1})^{-1}\cdot h]\\&=:\beta_h([(h\cdot g^{-1})\cdot f \cdot (h\cdot g^{-1})^{-1}])\\&=\beta_h([h\cdot g^{-1}] [f] [(h\cdot g^{-1})^{-1}])\\&=\beta_h([f]).\end{aligned}$$ So we get the desired result. The last step is due to that $[h\cdot g^{-1}],[f],[(h\cdot g^{-1})^{-1}]$ are all elements in $\pi_1(X,x_0)$ which is assumed to be abelian.

    Suppose then $\pi_1(X, x_0)$ is not abelian, then we can find $f, g$ loops based at $x_0$ such that $[f][g] \ne [g][f]$. Denote $\mathbb{1}_{x_0}$ as the identity (constant loop at $x_0$), we have that $\beta_g([f]): = [g^{-1}\cdot f \cdot g]$ $\ne [f] =: \beta_{\mathbb{1}_{x_0}}([f])$ (inequality is because inverse is unique in a group), so we find two paths $g, \mathbb{1}_{x_0}$ with the same endpoint but different induced homomorphism, and the statement is proved.

    ## Problem 5

    **Show that for a space $X$, the following three conditions are equivalent**:

    1. **Every map $S^1 \to X$ is homotopic to a constant map, with image a point**;
    2. **Every map $S^1 \to X$ extends to a map $D^2 \to X$**;
    3. **$\pi_1(X, x_0) = 0$ for all $x_0 \in X$**.

    **Deduce that a space $X$ is simply connected if and only if all maps $S^1 \to X$ are homotopic**.

    Proof

    ($1 \implies 2$) Suppose we have a map $f: S^1 \to X$. By assumption we have $H(x,t)$ such that $h_1(x) = f(x)$ and $h_0(x) = x_0$ for some fixed point $x_0 \in X$ and $x \in S^1$. Notice every point in $D^2$ can be expressed as $tx$ where $x \in S^1$ and $t \in [0,1]$, and the pair $x, t$ is unique unless $t = 0$.

    Define $\tilde{f}: D^2 \to X$ by $\tilde{f}(tx) = H(x,t)$, then $\tilde{f}$ is well-defined because $H(x,0) = x_0$ for all $x$, $\tilde{f}|_{S^1} = h_1 = f$, and $\tilde{f}$ is continuous. So we found a desired extension.

    ($2 \implies 3$) Let $f$ be an arbitrary loop based at $x_0$, which can be understand as a function $f:(S^1,1) \to (X,x_0)$. We need to show that $[f] = \mathbb{1}_{x_0}$. By $2$, we can get an extension $\tilde{f}: D^2 \to X$. In particular, $f = \tilde{f} \circ i$ where $i: S^1 \to D^2$ is inclusion. Then by property of the induced homomorphisms, we get $f_* = (\tilde{f} \circ i)_*$ $= \tilde{f}_* \circ i_*$ $: \pi_1(S_1, 1) \to \pi_1(D^2, 1) \to \pi_1(X,x_0)$. Since $D^2$ is simply connected, $\pi_1(D^2,1)$ is trivial, thus $i_*$ thus the composition $f_*: \pi_1(S^1, 1) \to \pi_1(X,x_0)$ is trivial, which means that $f_*([\gamma]) = [f\circ \gamma] = \mathbb{1}_{x_0}$ for any loop $\gamma$ in $S^1$ based at $1$. Take $\gamma$ to be the map that goes $S^1$ once, we get $[f] = [f\circ \gamma] = \mathbb{1}_{x_0}$, as desired.

    ($3 \implies 1$) This is essentially by definition of fundamental group.

    By definition, $X$ being simply connected if and only if $X$ is path connected and has trivial fundamental group ($3$), which we proved is equivalent with that $X$ is path connected and all maps $S^1 \to X$ is homotopic to a constant map ($1$) - which is not hard to be seen equivalent with that all maps $S^1 \to X$ are homotopic (a constant map $S^1 \to X$ is a map $S^1 \to X$ in the first place, and homotopy is an equivalent relation).

    ## Problem 6

    **We can regard $\pi_1(X,x_0)$ as the set of base-point-preserving homotopy classes of maps $(S^1,s_0) \to (X, x_0)$. Let $[S^1,X]$ be the set of homotopy classes of maps $S^1 \to X$, with no conditions on base-points. Thus there is a natural map $\Phi: \pi_1(X, x_0) \to [S^1, X]$ obtained by ignoring base-points. Show that $\Phi$ is onto if $X$ is path-connected, and that $\Phi([f]) = \Phi([g])$ if and only if $[f]$ and $[g]$ are conjugate in $\pi_1(X, x_0)$. Hence $\Phi$ induces a one-to-one correspondence between $[S^1,X]$ and the set of conjugacy classes in $\pi_1(X)$ when $X$ is path-connected**.

    Proof

    First we show $\Phi$ is onto. That is, for any $f: S^1 \to X$, we would like to find some element in $\pi(X,x_0)$ so that its image under $\Phi$ is the homotopy class $[f]$.

    Observe that if $\alpha$ is a loop based at $a$ and $\beta$ is a path connecting $a$ and $b$, then ignoring the base point, $\beta^{-1}\cdot \alpha \cdot \beta$ is homotopic with $\alpha \cdot \beta \cdot \beta^{-1} = \alpha$ (we can think of it as we rotate the path along the path, the base point changes from $a$ to $b$). Now, understand $f$ as a loop based at some $x_1 \in X$. Since $X$ is path-connected, we can find a path $g:I \to X$ with $g(0) = x_1, g(1) = x_0$, so that $g^{-1} \cdot f \cdot g$ is a loop based at $x_0$. By the above observation and the definition of $\Phi$, we have that $\Phi([g^{-1} \cdot f \cdot g])$ $=\Phi([f]) = [f]$, so we have found the pre-image.

    The above equation $\Phi([g^{-1}\cdot f \cdot g]) = \Phi([f])$ also proves that if $[f]$ and $[h] = [g^{-1}][f][g]$ for certain $[g]$ are conjugate, then their image under $\Phi$ is the same.

    Now, suppose $f$ and $g$ are loops based at $x_0$ and $\Phi([f]) = \Phi([g])$, we need to show $[f]$ and $[g]$ are conjugate in the fundamental group.

    By the definition of $\Phi$, the assumption means that $f$ and $g$ are homotopic (ignoring base point), i.e. there is $H(x,t):S^1 \times I \to X$ with $h_0 = f, h_1 = g$. We have that $H(1,0)$ (base point of $f$) and $H(1, 1)$ (base point of $g$) are both $x_0$, but $H(1, t), 0<t<1$ may not be this point. Define $h: I \to X$ by $h(t) = H(1, t)$, then $h$ is continuous, $h(0) = h(1) = x_0$ so it is a loop based at $x_0$.

    <img src="public/Pasted image 20230223092327.png" width="600" />

    Then $f$ and $h\cdot g \cdot h^{-1}$ are homotopic with base point fixed, realized by the homotopy $L(x,t)$ where $l_0 = f$, $l_1 = h\cdot g \cdot h^{-1}$, and for $0<t<1$, $l_t$ be the loop (based at $x_0$) $h|_{[0,t]} \cdot h_t \cdot h|_{[0,t]}^{-1}$ (here $h_t$ is the loop defined above in $H(x,t)$, it is a loop based at $H(1,t) = h(t)$). In particular, $[f] = [h\cdot g \cdot h^{-1}]$ so $[f]$ and $[g]$ are conjugate by $[h]$ in the fundamental group.

    ## Problem 16

    <img src="public/Pasted image 20230217161525.png" width="400" />

    **Show that there are no retractions $r: X \to A$ in the following cases**:

    1. **$X = \mathbb{R}^3$ with $A$ any subspace homeomorphic to $S^1$**;
    2. **$X = S^1 \times D^2$ with $A$ its boundary torus $S^1 \times S^1$**;
    3. **$X = S^1 \times D^2$ with $A$ the circle shown in the figure**.

    Proof

    1. $\pi_1(X) = 1$ and $\pi_1(A) \cong \mathbb{Z}$, so there is no injective homomorphism from $\pi_1(A) \to \pi_1(X)$;
    2. $\pi_1(X) \cong \pi_1(S^1) \cong \mathbb{Z}$ and $\pi_1(A) \cong \mathbb{Z}^2$, so again there is no injective homomorphism from $\pi_1(A) \to \pi_1(X)$;
    3. We know for a retract $r$ we should have inclusion so that $(r \circ i)_* = r_* \circ i_* = \text{id}$. By definition, $i_*: \pi_1(A) \to \pi_1(X)$ sends the generator of $\pi_1(A)$, which is a loop goes around $A$ once (in either direction), to the same loop in $X$. But this loop in $X$ contract to a constant map - because now we can use any point in this solid torus, also there is no reason to not be able to self-cross. So $i_*$ is trivial, thus $(r\circ i)_*$ cannot be identity.

    ## Problem 3

    **Show that the complement of a finite set of points in $\mathbb{R}^n$ is simply connected if $n \ge 3$**.

    Proof

    Say the finite set of points are $X = \lbrace x_1, \dots, x_m \rbrace$ so the space we are interested at is $\mathbb{R}^n \setminus X$. Deformation retract $\mathbb{R}^n \setminus X$ to the space $\mathbb{R}^n$ with $(1,0,\dots,0),\dots,(m,0,\dots,0)$ removed. For simplicity we illustrate it in $\mathbb{R}^2$, but the idea is the same:

    <img src="public/Pasted image 20230224100139.png" width="600" />

    This space deformation retract to a space of wedge sum of $m$ copies of $(n-1)$-pheres of radius $\frac{1}{2}$, and we can further deformation retract this space to $m$ copies of $(n-1)$-spheres with a single connected point.:

    <img src="public/Pasted image 20230224101137.png" width="600" />

    This space is simply connected: for any loop $\gamma$, contract it to the single connection point of the wedge sum. We can do it because $\gamma$ restricted on each sphere consists of loops, and each $(n-1)$-sphere is simply connected for $n\ge 3$. So our original space deformation retract to a simply connected space, thus it is simply connected.

    ## Problem 4

    **Let $X \subset \mathbb{R}^3$ be the union of $n$ lines through the origin. Compute $\pi_1(\mathbb{R}^3 - X)$**.

    Solution

    This space is homotopic equivalent with $S^2$ with $n$ pairs of antipodal points removed through $f: \mathbb{R}^3 \setminus X \to S^2 \setminus \lbrace n \text{ pairs of points}\rbrace$, sending $x \to x/\| x \|$. Illustrate in lower dimension:

    <img src="public/Pasted image 20230226070640.png" width="400" />

    (i.e. it's just the usual homotopy equivalence between $\mathbb{R}^3 \setminus \text{origin} \to S^2$ with some extra lines also removed)

    This new space is homotopy equivalent with $D^2 \setminus \lbrace 2n-1\text{ points}\rbrace$ ('enlarge' one of the points), which is homotopy equivalent with $\mathbb{R}^2 \setminus \lbrace 2n-1 \text{ points}\rbrace$, whose fundamental group is the free group generated by $2n-1$ generators $F_{2n-1}$. Since the fundamental group is preserved by homotopy equivalence, $\pi_1(\mathbb{R}^3 \setminus X) \cong F_{2n-1}$.

    ## Problem 8

    **Compute the fundamental group of the space obtained from two tori $S^1 \times S^1$ by identifying a circle $S^1 \times \lbrace x_0 \rbrace$ in one torus with the corresponding circle $S^1 \times \lbrace x_0 \rbrace$ in the other torus**.

    Solution

    One embedding of this space is following (a big torus and a small torus, the small torus' outer longitude circle touches the inner longitude circle of the big torus):

    <img src="public/Pasted image 20230226072615.png" width="600" />

    This space is path connected so let us choose the base point to be on the identified circle ($x$ on the diagram). Then the outer torus $T_1$ has fundamental group $\langle a,b | aba^{-1}b^{-1} \rangle$ ($a$ is a longitude, $b$ is a meridian), the inner torus $T_2$ has fundamental group $\langle a,c | aca^{-1}c^{-1} \rangle$ (the same $a$ is also a longitude for $T_2$ that passes $x$), and their intersection $T$ is a circle with fundamental group $\langle a \rangle$ (again it's the same $a$ passing the same base point $x$).

    By Seifert-Van Kampen Theorem (call the entire space $X$), we have $\pi_1(X,x)$ $= \langle a,b,c | aba^{-1}b^{-1}, aca^{-1}c^{-1}, R_S\rangle$ where $R_S$ in our case is the relation (there is only one generator for $T$) $\varphi_{1*}(a) = \varphi_{2*}(a)$ where $\varphi_i$'s are the inclusion maps from $T \to T_i$. In our case $\varphi_{1*}(a)$ and $\varphi_{2*}(a)$ are simply $a$, so this relation can be discard, and we get that $\pi_1(X) \cong \pi_1(X, x)$ $\cong \langle a,b,c | aba^{-1}b^{-1}, aca^{-1}c^{-1} \rangle$.

    ## Problem 14

    **Consider the quotient space of a cube $I^3$ obtained by identifying each square face with the opposite square face via the right-handed screw motion consisting of a translation by one unit in the direction perpendicular to the face combined with a one-quarter twist of the face about its center point. Show this quotient space $X$ is a cell complex with two $0$-cells, four $1$-cells, three $2$-cells, and one $3$-cell. Using this structure, show that $\pi_1(X)$ is the quaternion group $\lbrace \pm 1, \pm i, \pm j , \pm k \rbrace$, of order eight**.

    Proof

    Start with a cube $I^3$ and do the identification:

    <img src="public/Pasted image 20230226155418.png" width="600" />

    We apply the procedure on the book (p. 50~51) to calculate the fundamental group.

    We start with the $1$-skeleton:

    <img src="public/Pasted image 20230226162554.png" width="400" />

    So $X^1$ can be seen as wedge sum of $3$ circles, and has fundamental group $\pi_1(X^1,u) \cong \langle cb, cd, ca^{-1}\rangle$ free group generated by $3$ generic loops in the space based at $u$ (the choice of base point and generators are of course not unique, though).

    Now we need to attach the three $2$-cells to it. By Proposition 1.26, we get that $\pi_1(X^2, u)$ $\cong \langle cb,cd,ca^{-1} | abcd, ca^{-1}b^{-1}d, d^{-1}a^{-1}cb \rangle$, using the attaching map illustrated in the right-most diagram in the first picture (i.e. $A$ is attached through $abcd$, etc., choose the loops to be based at $u$ so that we do not need to worry about change of base points). Again by that proposition, this is (isomorphic to) the fundamental group of $X$.

    Now we need to show this presentation gives us the quaternion group. Rewrite the presentation as follow: $$\langle cb,cd,ca^{-1} | ac^{-1}cbcd, ca^{-1}b^{-1}c^{-1}cd, d^{-1}c^{-1}ca^{-1}cb \rangle$$ by group operation and inserting $c^{-1}c$ to the relations. If we write $cb = i, cd = j, ca^{-1} = k$, we get that $$\langle i,j,k | k^{-1}ij, ki^{-1}j,j^{-1}ki\rangle$$ or $$\langle i,j,k | i^2 = j^2 = k^2 = ijk\rangle$$ which is a presentation of the quaternion group.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 5""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 4

    **Construct a simply-connected covering space of the space $X \subset \mathbb{R}^3$ that is the union of a sphere and a diameter. Do the same when $X$ is the union of a sphere and a circle intersecting it in two points**.

    Solution

    Consider $\tilde{X}$ to be the following space (in $\mathbb{R}^3$):

    <img src="public/Pasted image 20230309123311.png" width="600" />

    Which is an infinite copy of a sphere and a line segment. This space is homotopic equivalent with an infinite wedge sum of $S^2$ which is simply-connected. Consider $p: \tilde{X} \to X$ to be the map that maps points on spheres to points on the sphere; points on line segments to points on the diameter; and points on the intersection of sphere and line segments to points on the intersection of sphere and diameter. Illustrated as below, image/pre-images are corresponded in the same color:

    <img src="public/Pasted image 20230309124205.png" width="600" />

    Locally this $p$ works like a projection (the line segment is not inside the sphere through), so it is an $\infty$-to- $1$ covering map.

    For the second part, consider the following space as $\tilde{X}$ and correspondence:

    <img src="public/Pasted image 20230309130016.png" width="600" />

    (The graph in fact looks like the Cayley graph as shown on p. 77. The places like the indicated one above are not connecting, so it will not create a non-trivial loop) Again this $\tilde{X}$ is simply-connected. $p$ maps $\tilde{X}$ onto $X$ in a similar manner as the above $p$, it is also an $\infty$-to- $1$ covering map.

    ## Problem 8

    **Let $\tilde{X}$ and $\tilde{Y}$ be simply-connected covering spaces of the path-connected, locally path-connected spaces $X$ and $Y$. Show that if $X \simeq Y$ then $\tilde{X} \simeq \tilde{Y}$**.

    Proof

    Let $f: X \to Y$ and $g: Y \to X$ be the maps that realize the homotopy equivalence between $X$ and $Y$. Denote $p: \tilde{X} \to X$ and $q: \tilde{Y} \to Y$ to be the covering maps. Consider $f \circ p: \tilde{X} \to X \to Y$.

    By Proposition 1.33 (we can apply it because $X$ is locally path-connected implies $\tilde{X}$ is locally path connected, and $\tilde{X}$ is simply-connected implies it is path-connected), a lift $\widetilde{f \circ p}: \tilde{X} \to \tilde{Y}$ exists if and only if $(f \circ p)_*(\pi_1(\tilde{X})) \subset q_*(\pi_1(\tilde{Y}))$- the latter is true because of the simply-connected assumption so these are both trivial groups. For simplicity let us denote $\widetilde{f \circ p}$ as $\tilde{f}$ (and by lifting we mean that $q \circ \tilde{f} = f\circ p$). Similarly, use $g \circ q$ and $p$, we can get a lift $\tilde{g}: \tilde{Y} \to  \tilde{X}$ (and that $p \circ \tilde{g} = g \circ q$).

    We need to show that $\tilde{f}$ is a homotopy equivalence, we show it by showing that we can find some $\varphi$ and $\psi$ so that $\varphi \circ \tilde{f}$ and $\tilde{f} \circ \psi$ are both homotopic to identity (and the result follows from 0.11 as hinted).

    Notice by above, we have that $q\circ \tilde{f} \circ\tilde{g}$ $= f\circ p \circ \tilde{g}$ $= f\circ g \circ q$, which means that $\tilde{f} \circ \tilde{g}$ is a lift of $f \circ g \circ q$. We also know from assumption that $f \circ g \simeq \text{id}$ thus $f \circ g \circ q \simeq q$ (proved in Homework 01 in Fall semester).

    Let $H$ be the homotopy that realizes $f \circ g \circ q \simeq q$ (say with $h_0 = f \circ g \circ q$ and $h_1 = q$), then by Homotopy Lifting Property, we have a unique $\tilde{H}$ with $\tilde{h}_0 = \tilde{f} \circ \tilde{g}$. Consider $\tilde{h}_1$, it is some lift of $q$. Since the corresponding covering map is $q$, by lifting we mean that $q\circ \tilde{h}_1 = q$. Thus for any $\tilde{y} \in \tilde{Y}$, we have $q(\tilde{h}_1(\tilde{y})) = q(\tilde{y})$, which means $\tilde{h}_1(\tilde{y})$ and $\tilde{y}$ are in some same fiber. Since $\tilde{Y}$ is simply-connected, $q$ is a normal covering, thus there exists some deck transformation $u: \tilde{Y} \to \tilde{Y}$ sending $\tilde{h}_1(\tilde{y})$ to $\tilde{y}$. In particular $\tilde{h}_1\circ u$ maps $\tilde{h}_1(\tilde{y})$ to itself.

    Notice now $\tilde{h}_1\circ u$ is a lift of $q$ by definition of a deck transformation ($q\circ \tilde{h}_1 \circ u$ $=q\circ u$ $= q$); $\text{id}$ (on $\tilde{Y}$) is of course also a lift of $q$ and they agree at $\tilde{h}_1(\tilde{y})$, thus Unique Lifting Property applies, we get that $\tilde{h}_1 \circ u = \text{id}$. Finally, define $\psi$ to be $\tilde{g}\circ u$, we have found $\psi$ so that $\tilde{f} \circ \psi$ $=\tilde{f}\circ\tilde{g} \circ u$ $\simeq \tilde{h}_1 \circ u$ $= \text{id}$.

    Similarly, use that $p\circ \tilde{g} \circ \tilde{f}$ $= g\circ q \circ \tilde{f}$ $= g \circ f \circ p$ with a similar argument (but possibly different order of composing functions in the steps), we can find the desired $\varphi$ that realizes $\varphi \circ f \simeq \text{id}$. Combine everything we have, we get $\tilde{X} \simeq \tilde{Y}$.

    ## Problem 9

    **Show that if a path-connected, locally path-connected space $X$ has $\pi_1(X)$ finite, then every map $X \to S^1$ is null-homotopic**. *Hint: Use the covering space $\mathbb{R} \to S^1$*.

    Proof

    Let $f: X\to S^1$ be an arbitrary (continuous) map. Then it induces homomorphism $f_*: \pi_1(X) \to \pi_1(S^1)$ which by assumption is a homomorphism from a finite group to $\mathbb{Z}$, which must be trivial ($\mathbb{Z}$ does not have a non-trivial finite subgroup).

    Apply Proposition 1.33, using $p: \mathbb{R} \to S^1$ the standard universal covering and the assumption that $X$ is path-connected and locally path-connected. The inclusion condition is automatically true because $f_*$ is trivial as argued. Thus we can always get a lift $\tilde{f}: X \to \mathbb{R}$, with $p \circ \tilde{f} = f$.

    Since $\mathbb{R}$ is contractible, $\tilde{f}$ is null-homotopic, thus any composition of it in the form of $g \circ \tilde{f}$ is null-homotopic, which in particular means $f$ is null-homotopic, as desired.

    ## Problem 10

    **Find all the connected $2$-sheeted and $3$-sheeted covering spaces of $S^1 \vee S^1$, up to isomorphism of covering spaces without base-points**.

    Solution

    View $S^1 \vee S^1$ as a graph with one vertex and two edges $a, b$ (oriented). This vertex has both edges $a$ and $b$ coming in and coming out. So for the $2$-sheeted cover we should have two vertices, two edge $a$ and two edge $b$, with each vertex having both $a,b$ coming in and coming out. We can also assume/draw the graph without edges go over each other because we are classifying up to isomorphism/homeomorphism.

    <img src="public/Pasted image 20230312085113.png" width="600" />

    Iterate all the possibility. Start with one edge $a$ coming out of one of the vertex, then it either:

    1. Gets back to the same vertex. Then the other vertex must also have an edge $a$ coming out and coming in back (otherwise the first vertex will have two $a$ coming in). Then consider one edge $b$ coming out of the first vertex:
    	1. If it comes back to the same vertex, then the other vertex also have (another) edge $b$ coming out and comes back in, makes the graph not connected (graph 0);
    	2. If it goes to the other vertex, then the other edge $b$ must come out of the second vertex and come in to the first vertex, we get graph 3;
    2. Otherwise it goes in to the other vertex, use the same reasoning above:
    	1. If edge $b$ comes out of/in to different vertices, we get graph 1;
    	2. Otherwise we get graph 2.
	
        <img src="public/Pasted image 20230312085538.png" width="600" />
	
        (The labeled orientation and the position ordering of the edges are not important in $2$-sheeted case) These complete the classification, there are three possibilities.

    For $3$-sheeted covering, we can follow the same reasoning - the only difference is now we have three vertices and six edges (three $a$ and three $b$). Start with all edges come out of/in to different vertices, and iterate all possibilities. We'll omit the word description here:

    <img src="public/Pasted image 20230312111230.png" width="600" />

    Notice that unlike the $2$-sheeted cover, orientations do matter in some cases, so for example, the first two graphs are not isomorphic (we can change orientations all together, but not changing orientation of $b$'s without changing $a$'s). In total there are seven possibilities.

    ## Problem 3

    **Prove the Borsuk-Ulam Theorem by the following argument. Suppose on the contrary that $f: S^n \to \mathbb{R}^n$ satisfies $f(x) \ne f(-x)$ for all $x$. Then define $g: S^n \to S^{n-1}$ by $g(x) = (f(x) - f(-x))/|f(x) - f(-x)|$, so $g(-x) = -g(x)$ and $g$ induces a map $\mathbb{R}P^n \to \mathbb{R}P^{n-1}$. Show that part (a) applies to this map**.

    > Part (a)
    > 
    > There is no map $\mathbb{R}P^n \to \mathbb{R}P^m$ inducing a non-trivial map $H^1(\mathbb{R}P^m;\mathbb{Z}_2) \to H^1(\mathbb{R}P^n;\mathbb{Z}_2)$ if $n > m$.

    Proof

    Let us call the induced map $h: \mathbb{R}P^n \to \mathbb{R}P^{n-1}$. It would induce homomorphism $h_*: \pi_1(\mathbb{R}P^n) \to \pi_1(\mathbb{R}P^{n-1})$. We would show that $h_*$ is non-trivial. If that is true, then since these fundamental groups are both abelian thus $h_*$ also gives us non-trivial homomorphism between the first homology groups, which will give us non-trivial dual between first cohomology groups (with $\mathbb{Z}_2$ coefficient), which contradict part (a).

    Pick $\varphi$ so that it is a non-trivial loop $I\to \mathbb{R}P^n$. Consider the $2$-sheeted covering $S^n \to \mathbb{R}P^n$, we can lift $\varphi$ to $\tilde{\varphi}: I \to S^n$. The endpoints $\tilde{\varphi}(0)$ and $\tilde{\varphi}(1)$ must be antipodal (else the endpoints would be same and $\varphi$ is trivial), in particular we have $g\circ \tilde{\varphi}:I \to S^n \to S^{n-1}$ also has endpoints being antipodal. Consider the following diagram: $$\begin{array}{ccccc}&&S^n&\xrightarrow{g}&S^{n-1}\\&\nearrow_{\tilde{\varphi}}&\downarrow^p&&\downarrow^p\\I&\xrightarrow{\varphi}&\mathbb{R}P^n&\xrightarrow{h}&\mathbb{R}P^{n-1}\end{array}$$ It is commutative because of lifting and the construction of $g$. Thus $g\circ \tilde{\varphi}$ is a lift of $h \circ \varphi$. Since $g\circ \tilde{\varphi}$ is not a loop as discussed, $[h\circ \varphi] = h_*([\varphi])$ is not trivial, which in particular means $h_*$ is not trivial.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 6""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 12

    **Show that an $n$-connected, $n$-dimensional CW-complex is contractible**.

    Proof

    Call this space $X$. Consider the Compression Lemma applied with $Y = X$, $B = x_0$ and $A$ be a sub-complex that contains $x_0$. The assumption "… $\pi_n(Y, B, y_0) = 0$ for all $y_0 \in B$ " is true because of the $n$-connectedness assumption. Thus the lemma applies and in particular we get that the identity map $\text{id}: (X, A) = X \to (X, x_0)$ is homotopic (relative to $A$) to a map $X \to x_0$ (a constant map), which by definition means $X$ is contractible (identity is null-homotopic).

    ## Problem 14

    **Use cellular approximation to show that the $n$-skeletons of homotopy equivalent CW-complexes without cells of dimension $n+1$ are also homotopy equivalent**.

    Proof

    Suppose $X, Y$ are two homotopy equivalent CW-complexes without cells of dimension $n+1$. Let $f: X \to Y$ and $g: Y\to X$ be the two functions that realize the homotopy equivalence. By cellular approximation, we may assume that $f$ and $g$ are cellular maps (compositions of homotopic maps are still homotopic). Claim: $f$ and $g$ restricted to the $n$-skeletons of $X$ and $Y$ are the functions that realize the homotopy equivalence of the $n$-skeletons:

    Let $H: Y \times I \to Y$ be the homotopy between $f \circ g$ and $\text{id}$. By viewing $I$ as a one-cell, there is a natural CW structure on $Y \times I$. Since the restriction of $H$ on $Y \times \lbrace 0, 1 \rbrace$ (which is $f\circ g$ and $\text{id}$) is a cellular map, by cellular approximation, we can get a cellular map $H': Y \times I \to Y$ that is homotopic to $H$ relative to $Y \times \lbrace 0 , 1 \rbrace$, i.e. we get a homotopy (that itself is a cellular map) between $f \circ g$ and $\text{id}$. Now restrict $H'$ to $Y^{(n)}\times I$, we have $H'(Y^{(n)} \times I) \subseteq H'((Y \times I)^{(n+1)})$ $\subseteq Y^{(n+1)}$ $= Y^{(n)}$ (first step is due to product of CW-complexes, second step is due to cellular map, third step is due to there is no $n+1$-cell in $Y$).

    So this restriction is a (continuous) map between $Y^{(n)} \times I$ and $Y^{(n)}$; its restriction to $t = 0$ is $f \circ g$ restricted to $Y^{(n)}$ which is the same as $f|_{X^{(n)}} \circ g|_{Y^{(n)}}$ (by cellular map property), and its restriction to $t = 1$ is identity restricted to $Y^{(n)}$. So this restriction realizes that $f|_{X^{(n)}} \circ g|_{Y^{(n)}}$ and $\text{id}$ are homotopic. Similarly, we can get the homotopy between $g|_{Y^{(n)}} \circ f|_{X^{(n)}}$ and $\text{id}$, so we proved the claim.

    ## Problem

    **Show that the suspension homomorphism $\pi_n(X) \to \pi_{n+1}(\Sigma X)$ defined by $[f] \mapsto [\Sigma f]$ is well-defined**.

    Proof

    First we show the map is well-defined. We need to show that given two maps $f,g: S^n \to X$ that are homotopic, their suspensions $\Sigma f, \Sigma g: S^{n+1} \to \Sigma X$ are also homotopic. This is straight forward: given $H$ a homotopy between $f$ and $g$, consider $H \times \text{id}_I: S^n \times I \times I \to X \times I$ and then the quotient $\Sigma H: S^n\times I \times I/\sim \to X\times I/\sim$ which is the same as $\Sigma H: S^{n+1}\times I \to \Sigma X$; it is continuous and by construction has $\Sigma f$ and $\Sigma g$ as it's restriction to the end-points, so $\Sigma f$ and $\Sigma g$ are homotopic.

    To show the map (denote it by $\Sigma$) is a homomorphism, we need that for $[f], [g]$ in $\pi_n(X)$ (so that $[f]\cdot [g] = [f \cdot g]$), we have $\Sigma([f])\cdot \Sigma([g]) = \Sigma([f\cdot g])$, or $[\Sigma f]\cdot [\Sigma g] = [\Sigma(f \cdot g)]$. We will show in fact that $\Sigma f \cdot \Sigma g = \Sigma(f \cdot g)$. It's rather straight forward as illustrated:

    <img src="public/Pasted image 20230413114808.png" width="600" />

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 7""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1

    **Use homotopy groups to show there is no retraction $\mathbb{R}P^n \to \mathbb{R}P^k$ if $n>k>0$**.

    Proof

    Suppose there is such retraction, then the induced homomorphism of inclusion $i_*: \pi_k(\mathbb{R}P^k) \to \pi_k(\mathbb{R}P^n)$ is injective. We shall show this is impossible.

    If $k = 1$, then $\pi_1(\mathbb{R}P^1) \cong \pi_1(S^1) \cong \mathbb{Z}$ but $\pi_1(\mathbb{R}P^n) \cong \mathbb{Z}_2$, so there is no injective homomorphism between these.

    For $k \ge 2$, since $S^m$ is a covering space for $\mathbb{R}P^m$, we have that $\pi_k(S^m) \cong \pi_k(\mathbb{R}P^m)$. We know that $\pi_k(S^k) \cong \mathbb{Z}$, so we have that $\pi_k(\mathbb{R}P^k) \cong \mathbb{Z}$. We also know that for $k < m$, $\pi_k(S^m) = 0$, thus $\pi_k(\mathbb{R}P^n) = 0$. So again there cannot be an injective homomorphism from $\mathbb{Z} \to 0$ and we get the desired result.

    ## Problem 14

    **If an $n$-dimensional CW-complex $X$ contains a sub-complex $Y$ homotopy equivalent to $S^n$, show that the map $\pi_n(Y) \to \pi_n(X)$ induced by inclusion is injective**. *Hint: Use the Hurewicz homomorphism*.

    Proof

    If $n = 0$, then $X$, $Y$, $\pi_0(X)$ and $\pi_0(Y)$ are all discrete sets and the statement is trivial. If $n = 1$, then $X$ is a graph, $Y$ is homotopy equivalent to a circle. The image of a non-trivial loop in $Y$ under the inclusion map is still a non-trivial loop in $X$, so the map $\pi_1(Y) \to \pi_1(X)$ is in fact also an inclusion and thus injective.

    Now suppose $n \ge 2$. Since $Y \simeq S^n$, $H_n(Y) \cong \mathbb{Z}$ generated by certain $[\alpha]$. It is also an $n$-cycle in $X$ because $Y$ is a sub-complex, and since $X$ is $n$-dimensional, there is no $n$-boundary and thus $[\alpha]$ is non-trivial in $H_n(X)$. In particular, $H_n(Y) \to H_n(X)$ induced by inclusion is injective. Consider the Hurewicz homomorphism, then $\pi_n(Y) \xrightarrow{h} H_n(Y) \xrightarrow{i_*} H_n(X)$ is injective because $h$ is an isomorphism for $n \ge 2$ (this is due to the Hurewicz Theorem, it applies because $\pi_0(Y) = \dots = \pi_{n-1}(Y) = 0$ as it is homotopy equivalent to $S^n$). But this is the same map as $\pi_n(Y) \xrightarrow{i_*} \pi_n(X) \xrightarrow{h} H_n(X)$ because both maps the generator $[f]$ of $\pi_n(Y)$ to $[i\circ f \circ \alpha]$ where $\alpha$ is the fundamental class of $S^n$.

    Since $f\circ g$ injective implies $g$ injective, we have that the part $\pi_n(Y) \to \pi_n(X)$ is injective.

    ## Problem 15

    **Show that a closed simply-connected $3$-manifold is homotopy equivalent to $S^3$**. *Hint: Use Poincaré duality, and also the fact that closed manifolds are homotopy equivalent to CW-complexes, from Corollary A.12 in the Appendix. The stronger statement that a closed simply-connected $3$-manifold is homeomorphic to $S^3$ is the Poincaré conjecture, finally proved by Perelman. The higher-dimensional analog, that a closed $n$-manifold homotopy equivalent to $S^n$ is homeomorphic to $S^n$, had been proved earlier for all $n \ge 4$*.

    Proof

    Let us call this manifold $M$, by the hint, we can assume it is instead a CW-complex. Since $M$ is simply-connected, $\pi_1(M) = 0$ thus $H_1(M) = 0$ by Hurewicz. Simply-connectedness also implies that $M$ is orientable, thus $H_3(M) \cong \mathbb{Z}$. Being orientable means Poincaré duality applies, so $H_2(M) = H^1(M)$ which then by UCT $= \text{Ext}(H_0(M),\mathbb{Z}) \oplus \text{Hom}(H_1(M),\mathbb{Z})$ $= 0 \oplus 0 = 0$. The higher homology groups are of course trivial.

    By Hurewicz Theorem, $\pi_3(M) \cong \mathbb{Z}$. Let $f: S^3 \to M$ (understand as a spheroid) be the generator of $\pi_3(M)$, then its induced homomorphism is the isomorphism between $H_3(S^3) \to H_3(M)$, because the image of $f$ under the Hurewicz homomorphism is the generator of $H_3(M)$, which by construction is also the image of the fundamental class in $H_3(S^3)$.

    For $n$ that is not $0$ or $3$, $f$ of course induces isomorphisms from $H_n(S^3) \to H_n(M)$ because they are all just trivial. The isomorphism on the $0$-th homology is also straight-forward. Thus $f: S^3 \to M$ induces isomorphisms on all homology groups, thus by Whitehead Theorem, $S^3$ and $M$ are homotopy equivalent.

    """
    )
    return


if __name__ == "__main__":
    app.run()
