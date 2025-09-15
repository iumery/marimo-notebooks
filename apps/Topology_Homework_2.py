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
    mo.md(r"""# Spring Semester Homework 01""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 1.1

    ### Exercise 1

    **If $k < l$ we can consider $\mathbb{R}^k$ to be the subset in $\mathbb{R}^l$. Show that smooth functions on $\mathbb{R}^k$, considered as a subset of $\mathbb{R}^l$, are the same as usual**.

    Proof

    Suppose $f$ is a smooth function $f: \mathbb{R}^k \to \mathbb{R}^m$. Consider the function $F: \mathbb{R}^l \to \mathbb{R}^m, (x_1, \dots, x_l) \mapsto f(x_1, \dots, x_k)$, then $F$ is smooth because $f$ is. Also it is clear that $F |_{\mathbb{R}^k \cap \mathbb{R}^l} = F |_{\mathbb{R}^k} = f (= f |_{\mathbb{R}^k \cap \mathbb{R}^l})$. Thus $f$ is smooth on $\mathbb{R}^k$ considered as a subset of $\mathbb{R}^l$.

    Conversely, suppose $f$ is smooth on $\mathbb{R}^k$ considered as a subset of $\mathbb{R}^l$. By definition, we have that for each $x \in \mathbb{R}^k \subseteq \mathbb{R}^l$ there is neighborhood $U \subseteq \mathbb{R}^l$ of $x$ and a smooth $F: U \to \mathbb{R}^m$ such that $F |_{U \cap \mathbb{R}^k} = f |_{U \cap \mathbb{R}^k}$. Since $F$ is smooth (by having continuous partial derivatives of all orders) we have that $f |_{U \cap \mathbb{R}^k}$ also has continuous partial derivatives of all orders, which means $f |_{U \cap \mathbb{R}^k}$ is smooth (on $U \cap \mathbb{R}^k$); since $x$ is arbitrary, $f$ is smooth on $\mathbb{R}^k$.

    ### Exercise 2

    **Suppose that $X$ is a subset of $\mathbb{R}^N$ and $Z$ is a subset of $X$. Show that the restriction to $Z$ of any smooth map on $X$ is a smooth map on $Z$**.

    Proof

    For any $z \in Z$, by definition of smoothness, we have that there exists $U \subseteq \mathbb{R}^N$ neighborhood of $z$ with $F: U \to \mathbb{R}^m, F |_{X\cap U} = f |_{X \cap U}$. Consider $U \cap Z$: it is a neighborhood of $z$ and it is contained in $U \cap X$, thus $F |_{Z \cap U} = f |_{Z \cap U}$, i.e. the restriction is also smooth.

    ### Exercise 4

    1. **Let $B_a$ be the open ball $\lbrace x \| x |^2 < a \rbrace$ in $\mathbb{R}^k$. Show that the map $x \mapsto \frac{ax}{\sqrt{a^2 - | x |^2}}$ is a diffeomorphism of $B_a$ onto $\mathbb{R}^k$**;
    2. **Suppose that $X$ is a $k$-dimensional manifold. Show that every point in $X$ has a neighborhood diffeomorphic to all of $\mathbb{R}^k$. Thus local parametrizations may always be chosen with all of $\mathbb{R}^k$ for their domains**.

    Proof

    1. The map is surjective: for any wanted $y \in \mathbb{R}^k$, pick $x$ with the same 'direction' with $y$ and with needed 'length' then this $x$ will be mapped to $y$ (zero vector is mapped to zero vector, vector with length close to $a$ is mapped to a vector with large length; the map is clearly continuous, thus any length can be mapped to).
    	Write the function as $y = \frac{ax}{\sqrt{a^2 - | x |^2}}$, take square each side and it is not hard to find the inverse to be $x = \frac{ay}{\sqrt{a^2 + | y |^2}}$ (from $\mathbb{R}^k$ to $B_a$). Now both functions are compositions of 'basic' smooth functions (identity, square, square root, etc.) thus they are both smooth, and thus $x \mapsto \frac{ax}{\sqrt{a^2 - | x |^2}}$ is a diffeomorphism of $B_a$ onto $\mathbb{R}^k$;
    2. By definition of a $k$-manifold, for each $p \in X$, there is an open neighborhood $O(p) \subseteq X$ which is diffeomorphic to an open set $U \subseteq \mathbb{R}^k$: the diffeomorphism $r: U \to O(p)$ is a local parametrization of $O(p)$. Now $r^{-1}(p) \in U$ and we can choose $B = B_a(r^{-1}(p)) \subseteq U$ with a small enough $a$. By previous exercise the restriction of $r |_B$ is also a diffeomorphism (local parametrization). By part 1 we have a diffeomorphism $g: \mathbb{R}^k \to B$, thus (inverse of) the composition $r |_B \circ g: \mathbb{R}^k \to B \to O(p)$ would be a diffeomorphism between a neighborhood of $x$ to $\mathbb{R}^k$.

    ### Exercise 6

    **A smooth bijective map of manifolds need not be a diffeomorphism. In fact, show that $f: \mathbb{R}^1 \to \mathbb{R}^1, f(x) = x^3$, is an example**.

    Solution

    The inverse of $f$ is $g = f^{-1} = x^{1/3}$ and is not even differentiable at $0$: $\lim\limits_{h \to 0}\frac{g(h)-g(0)}{h} = \lim\limits_{h \to 0}h^{-2/3}$ is undefined, graphically the slope is a vertical line there. Thus $f$ is not a diffeomorphism.

    ### Exercise 8

    **Prove that the paraboloid in $\mathbb{R}^3$, defined by $x^2 + y^2 - z^2 = a$, is a manifold if $a > 0$. Why doesn't $x^2 + y^2 - z^2 = 0$ define a manifold**?

    Proof

    <img src="public/Pasted image 20210903021328.png" width="400" />

    (a graph from WolframAlpha to help illustrate)

    Fix any $a > 0$, we show that it is a $2$-manifold by giving the following graphs that cover it:

    1. Bottom part that looks like a volcano: it can be parameterized by $f_1: \mathbb{R}^2 - \overline{B_a} \to \mathbb{R}^3, (x, y) \mapsto (x, y, -\sqrt{x^2 + y^2 - a})$ (works like inverse of a projection);
    2. A circle in the middle (and the surrounding): just like the parametrization of $S^1$ we may do it by four parts:
    	1. $f_2: B_a \to \mathbb{R}^3, (x, z) \mapsto (x,\sqrt{a+x^2-z^2},z)$, the domain $B_a$ here could be pretty arbitrary, because in the end all we need is to cover the middle line;
    	2. $f_3: B_a \to \mathbb{R}^3, (x, z) \mapsto (x,-\sqrt{a+x^2-z^2},z)$;
    	3. $f_4: B_a \to \mathbb{R}^3, (y, z) \mapsto (\sqrt{a+y^2-z^2},y,z)$; and,
    	4. $f_5: B_a \to \mathbb{R}^3, (y, z) \mapsto (-\sqrt{a+y^2-z^2},y,z)$. Each of them would look like this:

    	<img src="public/Pasted image 20210903021613.png" width="400" />

    3. And finally the top part, which is a volcano up-side-down, parameterized by $f_6: \mathbb{R}^2 - \overline{B_a} \to \mathbb{R}^3, (x, y) \mapsto (x, y, \sqrt{x^2 + y^2 - a})$.

    In the case that $a = 0$ the graph looks like this:

    <img src="public/Pasted image 20210903021534.png" width="400" />

    Then the middle point $(0, 0, 0)$ has no neighborhood $O$ diffeomorphic to $\mathbb{R}^m$ (in particular, $\mathbb{R}^2$) (not even homeomorphic to, because if we remove $(0, 0, 0)$ from $O$ then it got two components, while $\mathbb{R}^2$ still has one component after removing a point).

    ### Exercise 12

    **Stereographic projection is a map $\pi$ from the punctured sphere $S^2 - \lbrace N \rbrace$ on to $\mathbb{R}^2$, where $N$ is the north pole $(0, 0, 1)$. For any $p \in S^2 - \lbrace N \rbrace$, $\pi(p)$ is defined to be the point at which the line through $N$ and $p$ intersects the $xy$ plane. Prove that $\pi: S^2 - \lbrace N \rbrace \to \mathbb{R}^2$ is a diffeomorphism**.

    Proof

    We show this by explicitly giving $\pi$ and its inverse:

    In other word, for each $p$ on the punctured sphere with the coordinate $(x_1, \dots, x_{k+1})$ we want to find the coordinate of its image.

    For each coordinate of $\pi$, 'cut through' this coordinate (and take the projection of $p$ on the cut plane), for example, say we cut through 'the first dimension':

    <img src="public/Pasted image 20220326104219.png" width="400" />

    This cut leaves us a plane.

    On this projection, $N$ has the coordinate $(0,1)$, if we project $p$ onto this plane we have the coordinate $(x_1, x_{k+1})$. With little knowledge in geometry it is easy to find that the line connecting $N$ and $p$ intersects the horizontal axis at $(\frac{x_1}{1-x_{k+1}}, 0)$. In other word, the value of the first coordinate of $\pi(p)$ is $\frac{x_1}{1-x_{k+1}}$.

    In general, $\pi$ maps $(x_1, \dots, x_{k+1})$ to $(\frac{x_1}{1-x_{k+1}}, \dots, \frac{x_k}{1-x_{k+1}})$.

    It is not too hard to compute its inverse: $\pi^{-1}$ maps $(y_1, \dots, y_k)$ to $(\frac{2y_1}{y_1^2 + \dots + y_k^2 + 1}, \dots, \frac{2y_k}{y_1^2 + \dots + y_k^2 + 1}, \frac{y_1^2 + \dots + y_k^2 - 1}{y_1^2 + \dots + y_k^2 + 1})$, using the fact that $\sum y_i^2 = 1$.

    Clearly both $\pi$ and its inverse are smooth, thus $\pi$ is a diffeomorphism.

    ### Exercise 14

    **If $f: X \to X'$ and $g: Y \to Y'$ are smooth maps, define a product map $f \times g: X \times Y \to X' \times Y'$ by $(f \times g)(x, y) = (f(x), g(y))$. Show that $f \times g$ is smooth**.

    Proof

    For any $(x, y) \in X \times Y$, we have $x \in X$ and $y \in Y$ thus by definition, there exists neighborhood $U = U(x), V = V(y)$ with $F$ smooth and $F |_{X \cap U} = f |_{X \cap U}$, $G$ smooth and $G |_{Y \cap V} = g |_{Y \cap V}$. Consider the product $(X \cap U) \times (Y \cap V)$, it equals to $(X \times Y) \cap (U \times V)$. Thus $f \times g$ coincides $F \times G$ on $(X \cap U) \times (Y \cap V) = (X \times Y) \cap (U \times V)$. From the definition of product topology $U \times V$ is open, thus $F \times G$ is naturally smooth on $U \times V$ because it still has continuous derivatives of all orders, thus $f \times g$ is also smooth.

    ### Exercise 16

    **The diagonal $\triangle$ in $X \times X$ is the set of points of the form $(x, x)$. Show that $\triangle$ is diffeomorphic to $X$, so $\triangle$ is a manifold if $X$ is**.

    Proof

    Let $f: X \to \triangle$ given by $x \mapsto (x, x)$. For any $x \in X$, let $U = U(x)$ be a neighborhood of $x$ in $\mathbb{R}^m$ and let $F: U \to \mathbb{R}^N$ given by $x \mapsto (x, x)$. Now for any $x_0 \in U$, the tangent vector at $x_0$ is: $F'(x_0) = \lim\limits_{h \to 0}\frac{F(x_0+h)-F(x_0)}{h}$ $= \lim\limits_{h \to 0}\frac{(x_0+h,x_0+h) - (x_0, x_0)}{h}$ $= \lim\limits_{h \to 0}(1,1)$ $= (1,1)$ is constant, thus $F$ is smooth, which coincides $f$ on $U$, thus $f$ is smooth. Now the inverse of $f$ is $f^{-1}:\triangle \to X$ given by $(x,x) \to x$ is a projection, and we know that a projection map is smooth. Thus $\triangle$ is diffeomorphic to $X$.

    ### Exercise 18

    1. **An extremely useful function $f:\mathbb{R} \to \mathbb{R}$ is $f(x) = e^{-1/x^2}, x > 0, 0, x \le 0$. Prove that $f$ is smooth**;
    2. **Show that $g(x) = f(x-a)f(b-x)$ is a smooth function, positive on $(a, b)$ and zero elsewhere ($a < b$). Then $h(x) = \frac{\int_{-\infty}^xgdx}{\int_{-\infty}^{\infty}gdx}$ is a smooth function satisfying $h(x) = 0$ for $x < a$, $h(x) = 1$ for $x > b$, and $0 < h(x) < 1$ for $x \in (a, b)$**;
    3. **Now construct a smooth function on $\mathbb{R}^k$ that equals $1$ on the ball of radius $a$, zero outside the ball of radius $b$, and is strictly between $0$ and $1$ at intermediate points**.

    Proof

    1. Claim that $(e^{-1/x^2})^{(n)} = e^{-1/x^2}P_n(1/x)$ where $P_n$ is a polynomial of degree $3n$ for all natural $n$:
    	Indeed, the case $n = 1$ is true: $(e^{-1/x^2})' = e^{-1/x^2} \frac{2}{x^3}$;
    	Suppose statement holds for $n$: then $(e^{-1/x^2})^{(n+1)} = ((e^{-1/x^2})^{(n)})'$ $= (e^{-1/x^2}P_n(1/x))'$ $= e^{-1/x^2} \frac{2}{x^3} P_n(1/x) + e^{-1/x^2} P_n'(1/x)(-1/x^2)$, and we can see that $\frac{2}{x^3} P_n(1/x) + P_n'(1/x)(-1/x^2)$ is a polynomial of degree $3n$.
    	Thus we proved the claim by induction.
    	Now, for each natural $n$ we have $\lim\limits_{h \to 0+}\frac{(e^{-1/h^2})^{(n)}}{h}$ $= \lim\limits_{h \to 0+}\frac{e^{-1/h^2}P_n(1/h)}{h}$ $= \lim\limits_{h \to 0+}e^{-1/h^2}\tilde{P}(1/h)$ for some rational $\tilde{P}$, and this limit is clearly $0$. Thus the original $f$ has continuous derivatives of all orders thus smooth;
    2. Since $f$ is smooth, $g$ being composition (and product) of smooth functions is smooth. If $a < x < b$ then $x-a>0$ and $b-x>0$ thus $f(x-a)$ and $f(b-x)$ are positive, thus $g(x)$ positive. Similarly if $x \le a$ or $x \ge b$, then either $f(x-a)$ or $f(b-x)$ is zero thus $g(x)$ is zero.
    	Now $\int_{-\infty}^{\infty}gdx$ is fixed, and by Fundamental Theorem of Calculus $(\int_{-\infty}^xgdx)' = g(x)$ which is smooth, thus $h$ is smooth.
    	If $x < a$ then area below $g$ is identical $0$, $\int_{-\infty}^xgdx = 0 \implies h(x) = 0$;
    	If $x > b$ then area below $g$ (before it hits $x$) covers everything, thus $\int_{-\infty}^xgdx = \int_{-\infty}^{\infty}gdx$ thus $h(x) = 1$;
    	If $a < x < b$ then $g(x) > 0$ meaning that $\int_{-\infty}^xgdx < \int_{-\infty}^{\infty}gdx$, thus $0 < h(x) < 1$;
    3. $f: \mathbb{R}^k \to \mathbb{R}, x \mapsto \| x \|$ is clearly smooth, thus $F: \mathbb{R}^k \to \mathbb{R}, x \mapsto 1 - h(\| x \|)$ is a function that satisfies everything we want.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 02""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 1.2

    ### Exercise 1

    **For a sub-manifold $X$ of $Y$, let $i: X \to Y$ be the inclusion map, check that $di_x$ is the inclusion map of $T_x(X)$ into $T_{f(x)}(Y)$**.

    Proof

    Let $x \in X \subseteq Y$ and $r: U \to X$ and $s: V \to Y$ be local parametrizations, we can define $h = s^{-1} \circ i \circ r:U \to X \to Y \to V$, and then from there define $di_0 = ds_0 \circ dh_0 \circ dr^{-1}_0$. Now since $X \subseteq Y$ we can see $r$ as the same mapping but with $Y$ as codomain, so that we can simply write $h = s^{-1} \circ r$, thus $dh_0 = ds^{-1}_0 \circ dr_0$, and thus $di_0 = ds_0 \circ ds^{-1}_0 \circ dr_0 \circ dr^{-1}_0 = \text{id}$. In other words it is a inclusion map.

    ### Exercise 3

    **Let $V$ be a vector subspace of $\mathbb{R}^N$, show that $T_x(V) = V$ if $x \in V$**.

    Proof

    Let $V$ be a $k$-dimensional vector subspace of $\mathbb{R}^N$. Claim that $V$ is diffeomorphic to $\mathbb{R}^k$: indeed, choose $v_1, \dots, v_k$ be a set of basis of $V$ then every element of $V$ is of the form $x_1v_1 + \dots + x_kv_k, x_i \in \mathbb{R}$. Consider the map $r(x_1v_1 + \dots + x_kv_k) = (x_1 , \dots , x_k)$, it can be extended to the whole $\mathbb{R}^k$, and it has the inverse $r^{-1}(x_1, \dots, x_k) = x_1v_1 + \dots + x_kv_k$. So $r$ is a diffeomorphism.

    Now $r$ is clearly linear, so we have $T_x(V) = dr_0(\mathbb{R}^k) = r(\mathbb{R}^k) = V$, for any $x \in V$.

    ### Exercise 4

    **Suppose that $f:X \to Y$ is a diffeomorphism, prove that at each $x$ its derivative $df_x$ is an isomorphism of tangent spaces**.

    Proof

    Let $f^{-1}$ be the inverse map, then $\text{id} = f^{-1} \circ f$ and $\text{id} = f \circ f^{-1}$, they imply that $df^{-1}_{f(x)}\circ df_x = d(\text{id}) = \text{id}$ and $df_{f^{-1}(y)}\circ df^{-1}_y = d(\text{id}) = \text{id}$. Thus $df_x$ is linear, one-to-one and onto, thus an isomorphism of tangent spaces.

    ### Exercise 5

    **Prove that $\mathbb{R}^k$ and $\mathbb{R}^l$ are not diffeomorphic if $k \ne l$**.

    Proof

    By the exercise above, if $\mathbb{R}^k$ and $\mathbb{R}^l$ are diffeomorphic then they are also isomorphic as vector spaces, which clearly cannot be true.

    ### Exercise 8

    **What is the tangent space to the paraboloid defined by $x^2 + y^2 - z^2 = a$ at $(\sqrt{a}, 0, 0)$, where $a>0$**?

    Solution

    From last homework we have this parametrization $f: B_a \to \mathbb{R}^3, (x, y) \mapsto (\sqrt{a+x^2-y^2},x,y)$.

    Now $f_x = (\frac{x}{\sqrt{a+x^2-y^2}},1,0)$ and $f_y = (-\frac{y}{\sqrt{a+x^2-y^2}},0,1)$. So $f_x = (0,1,0)$ and $f_y = (0,0,1)$ at $(\sqrt{a}, 0, 0)$, where $x = 0$ and $y = 0$ in this case.

    It is pretty intuitive to understand graphically, the tangent space (plane) is a 'vertical' plane parallel to the $y-z$ plane through that point.

    Not a redo:

    It may be better to write $x, y, z$ in a more understandable order (I was confused by myself above, to be honest): $f: B_a \to \mathbb{R}^3, (y, z) \mapsto (\sqrt{a+z^2-y^2},y,z)$. And that $f_y = (\frac{y}{\sqrt{a+z^2-y^2}},1,0) = (0, 1, 0)$ and $f_z = (-\frac{z}{\sqrt{a+z^2-y^2}},0,1) = (0, 0, 1)$.

    ### Exercise 9

    1. **Show that for any manifolds $X$ and $Y$, $T_{(x,y)}(X \times Y)$ $= T_x(X) \times T_y(Y)$**;
    2. **Let $f: X\times Y \to X$ be the projection map $(x, y) \to x$. Show that $df_{(x,y)}:T_x(X) \times T_y(Y) \to T_x(X)$ is the analogous projection $(v, w) \to v$**;
    3. **Fixing any $y \in Y$ gives an injection mapping $f: X \to X \times Y$ by $f(x) = (x, y)$. Show that $df_x(v) = (v, 0)$**;
    4. **Let $f:X \to X'$, $g:Y \to Y'$ be any smooth maps, prove that $d(f\times g)_{(x,y)} = df_x \times dg_y$**.

    Proof

    1. Let $r = r_1 \times r_2: U \times V \to X \times Y$ be a local parametrization.
    	We have $dr_{(u,v)} = \begin{pmatrix}r_{1_u}&r_{2_u}\\r_{1_v}&r_{2_v}\end{pmatrix} = \begin{pmatrix}r_{1_u}&0\\0&r_{2_v}\end{pmatrix} =dr_{1_u} \times dr_{2_v}$ and $T_{(x,y)}(X \times Y)$ $= dr_{(u,v)}(\mathbb{R}^{k} \times \mathbb{R}^l)$ $= dr_{1_u}(\mathbb{R}^{k}) \times dr_{2_v}(\mathbb{R}^{l})$ $= T_x(X) \times T_y(Y)$;
    2. $f$ can been seen as a restriction of $\pi: \mathbb{R}^N \times \mathbb{R}^M \to \mathbb{R}^N$, the natural projection map. So $df_{(x,y)}(v,w) = d\pi_{(x,y)}(v,w) =$ (using the fact that a projection is a linear map) $= \pi(v,w) = v$.
    	The domain should have been $T_{(x,y)}(X \times Y)$, but by part 1 it is the same as $T_x(X) \times T_y(Y)$;
    3. Let $r:U \to X$ and $s:V \to Y$ be parametrizations and set $s(0) = y$. We can define $h = (r \times s)^{-1} \circ f \circ r$, we have $h(u) = (r \times s)^{-1}(f(r(u)))$ $=(r \times s)^{-1}(r(u),y) = (u, 0)$ and thus $h = \text{id} \times 0 = dh_0$. Now we can define $df_x = (dr_0 \times ds_0) \circ (\text{id} \times 0) \circ dr^{-1}_0$ and $df_x(v)$ gives us $(v, ds_0(0)) = (v, 0)$;
    4. Let $\pi_1: X \times Y \to X$ and $\pi_2: X\times Y \to Y$ be projections;
    	Let $i_1:X' \to X' \times Y'$ and $i_2:Y' \to X'\times Y'$ be inclusions.
    	Now $f \times g = i_1(f(\pi_1))+i_2(g(\pi_2))$, and $d(f\times g)_{(x,y)}(u,v)$ $= di_{1_{f(x)}}\circ df_x \circ d\pi_{1_{(x,y)}}(u,v) + di_{2_{g(y)}}\circ dg_y \circ d\pi_{2_{(x,y)}}(u,v)$.
    	Following from the previous parts we have: $d(f\times g)_{(x,y)}(u,v)$ $=^{\text{part 2}} di_{1_{f(x)}} \circ df_x(u) + di_{2_{g(y)}} \circ dg_y(v)$ $=^{\text{part 3}} (df_x(u), 0) + (0, dg_y(v))$ $= (df_x(u), dg_y(v))$ and the result follows.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 03""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 1.3

    ### Exercise 3

    **Let $f:\mathbb{R} \to \mathbb{R}$ be a local diffeomorphism, prove that the image of $f$ is an open interval and that, in fact, $f$ maps $\mathbb{R}$ diffeomorphically onto this interval**.

    Proof

    $\mathbb{R}$ is connected, thus the image must be an interval; $f(\mathbb{R}) = f(\bigcup\limits_{x\in\mathbb{R}}{U(x)}) = \bigcup\limits_{x\in\mathbb{R}}f(U(x))$ is open by definition, so the image is open.

    We proved in the class that $f'$ never vanish, thus $f$ is injective (being strictly increasing or decreasing), thus $f:\mathbb{R} \to \text{im}(f)$ is bijective. Say $f^{-1}$ is the inverse, for any $f(x) \in \text{im}(f)$, $f$ maps $U(f^{-1}(f(x)))$, an neighborhood of the preimage, diffeomorphically to $V(f(x))$, an neighborhood of the point, thus $f^{-1}$ is smooth around $f(x)$, and thus $f^{-1}$ is smooth since $f(x)$ is arbitrary. By definition, both $f$ and $f^{-1}$ are smooth thus $f$ is a diffeomorphism.

    ### Exercise 4

    **To contrast with Exercise 3, construct a local diffeomorphism $f:\mathbb{R}^2 \to \mathbb{R}^2$ that is not a diffeomorphism onto its image**.

    Solution

    We want to have a such function that is not injective: $z \to e^z$ the complex exponential may do the job. It is not injective so does not have an inverse, so it cannot be an diffeomorphism. However for each point we can choose a small neighborhood (where no two points with $z_1 = z_2 \pm 2 n \pi i$ are in it) and define $\log$ safely on this region, thus it is a local diffeomorphism.

    ### Exercise 6

    1. **If $f,g$ are immersions, show that $f \times g$ is immersion**;
    2. **If $f,g$ are immersions, show that $g \circ f$ is immersion**;
    3. **If $f$ is an immersion, show that its restriction to any sub-manifold of its domain is an immersion**.
    4. **When $\dim{X} = \dim{Y}$, show that the immersions $f:X\to Y$ are the same as local diffeomorphisms**.
	
    Proof

    1. By previous exercise we have $d(f\times g)_{(x,y)} = df_x \times dg_y$, a product of injective maps, which is injective, thus by definition $f \times g$ is also an immersion;
    2. By the Chain Rule we have $d(g\circ f)_x = dg_{f(x)} \circ df_x$, a composition of injective maps, which is injective, thus $g \circ f$ is an immersion;
    3. Say $f: X \to Y$ is an immersion and $Z \subseteq X$ is a sub-manifold.
    	Let $i: Z \to X$ be an inclusion map, so that $f|_Z = f \circ i$, differentiate both side we have ${df|_Z}_x = df_{f(x)} \circ di_x$. By previous exercise we have that $di_x$ is still inclusive, thus injective. Thus ${df|_Z}_x$ is injective and we have $f|_Z$ is an immersion;
    4. By the Local Immersion Theorem, with the case $\dim{X} = \dim{Y}$, for any $x$ and $y = f(x)$ we have local coordinates around $x$ and $y$ with $f(x_1,\dots,x_n) = (x_1,\dots,x_n)$, which is simply the identity map, thus $f$ is a local diffeomorphism.

    ### Exercise 7

    1. **Check that $g:\mathbb{R} \to S^1, g(t) = (\cos(2\pi t),\sin(2\pi t))$ is in fact a local diffeomorphism**;
    2. **From Exercise 6, it follows that $G: \mathbb{R}^2 \to S^1 \times S^1, G = g\times g$ is a local diffeomorphism. Also, if $L$ is a line in $\mathbb{R}^2$, the restriction $G: L \to S^1\times S^1$ is an immersion. Prove that if $L$ has irrational slope, $G$ is one-to-one on $L$**.

    Proof

    1. It is clear that $\cos(2 \pi t)$ and $\sin(2 \pi t)$ are periodic with $1$, thus for any $t \in \mathbb{R}$ if we take $U = U(t) = (t-0.25, t+0.25)$ then $g|_U$ is bijective, is smooth and has smooth inverse. Thus $g$ is a local diffeomorphism;
    2. We can compute $dg_t = (-\sin(2\pi t),\cos(2\pi t))$ which is never $(0,0)$, thus $\ker{dg_t} = 0$ and rank is $1$, thus $dg_t$ is injective and $g$ is an immersion. It then follows that $G$ is an immersion and the restriction of a line on $G$ is an immersion by previous exercises.
    	Let $L$ be a straight line in $\mathbb{R}^2$ with $t \mapsto at+b, a\in \mathbb{R} -\mathbb{Q}$, then every point on this line has the coordinate of the form $(t, at+b)$. If $G(t,at+b) = G(s,as+b)$ then $\cos(2\pi t) = \cos(2\pi s)$, $\sin(2\pi t) = \sin(2\pi s)$, $\cos(2\pi (at+b)) = \cos(2\pi (as+b))$, and $\sin(2\pi (at+b)) = \sin(2\pi (as+b))$.
    	Thus we need to have $t-s \in \mathbb{Z}$ and $at-as \in \mathbb{Z}$, which is impossible unless $t = s$, thus $G$ is injective.

    ### Exercise 8

    **Check the map $\mathbb{R} \to \mathbb{R}^2, t \mapsto (\frac{e^t+e^{-t}}{2},\frac{e^t-e^{-t}}{2})$ is an embedding. Prove that its image is one nappe of the hyperbola $x^2-y^2=1$**.

    Proof

    Let's call this map $r$.

    1. $r$ is an immersion: $dr_t = (\frac{e^t-e^{-t}}{2},\frac{e^t+e^{-t}}{2})$. If $dr_t(x) = dr_t(y)$ then $(e^t-e^{-t})x = (e^t-e^{-t})y$ and $(e^t+e^{-t})x = (e^t+e^{-t})y$. Adding these two equations together and it is easy to have $x = y$, thus $dr_t$ is injective and $r$ is an immersion;
    2. $r$ is injective: if $r(x) = r(y)$, then $e^x+e^{-x} = e^y+e^{-y}$ and $e^x-e^{-x} = e^y-e^{-y}$, again add two equations, and we can see $r$ is injective because the exponential function is injective;
    3. $r$ is proper: we work with the Euclidean space, so we need to show that the preimage of closed and bounded set is closed and bounded:
    	1. Closed: $r$ is continuous, thus preimage of closed set is closed;
    	2. Bounded: both $\frac{e^t+e^{-t}}{2}$ and $\frac{e^t-e^{-t}}{2}$ grow much faster than $t$, thus if they are bounded, the preimage is clearly bounded.

    By definition, $r$ is an injective and proper immersion, thus is an embedding.

    Now the second part:

    1. For any $t \in \mathbb{R}$, $(\frac{e^t+e^{-t}}{2})^2-(\frac{e^t-e^{-t}}{2})^2$ $= \frac{1}{4}((e^t)^2+(e^{-t})^2+2e^te^{-t}-(e^t)^2-(e^{-t})^2+2e^te^{-t})$ $= e^te^{-t} = 1$. Thus $\text{im}(r) \subseteq Graph(x^2-y^2=1)$;
    2. Now for any $(x,y)\in Graph(x^2-y^2=1)$ such that $x > 0$ (the right part):
    	1. If $0<x<1$ then $y$ is undefined on $\mathbb{R}$ and we don't need to check them;
    	2. If $x = 1$ then $y = 0$ and we can check that at $t = 0$ the corresponding $(\frac{e^t+e^{-t}}{2},\frac{e^t-e^{-t}}{2}) = (1,0)$;
    	3. If $x > 1$, it is clear that there is some $t$ such that $\frac{e^t+e^{-t}}{2} = x$, then $y = \pm \sqrt{x^2-1}$ $= \pm \sqrt{\frac{1}{4}((e^t)^2+(e^{-t})^2+2)-1}$ $= \pm \sqrt{\frac{1}{4}((e^t)^2+(e^{-t})^2-2)}$ $= \pm \frac{e^t-e^{-t}}{2}$. Notice that if $t$ is a solution for $\frac{e^t+e^{-t}}{2} = x$ then $-t$ is also a solution, putting it to $y$ we exactly will have $-\frac{e^t-e^{-t}}{2} = \frac{e^{-t}-e^{-(-t)}}{2}$.

    Thus $\text{im}(r) \subseteq Graph(x^2-y^2=1)$ and $\text{im}(r) \supseteq Graph(x^2-y^2=1), x>0$ and the equality $\text{im}(r) = Graph(x^2-y^2=1), x>0$ holds.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 04""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 1.4

    ### Exercise 7

    **(Stack of Record Theorem) Suppose that $y$ is a regular value of $f: X \to Y$, where $X$ is compact and has the same dimension as $Y$. Show that $f^{-1}(y)$ is a finite set $\lbrace x_1,\dots,x_N \rbrace$. Prove there exists a neighborhood $U$ of $y$ in $Y$ such that $f^{-1}(U)$ is a disjoint union $V_1 \cup \dots \cup V_N$ where $V_t$ is an open neighborhood of $x_t$ and $f$ maps each $V_t$ diffeomorphically onto $U$**.

    Proof

    1. By definition of a regular value, for each $x \in f^{-1}(y)$, $f$ is a submersion at $x$; since $\dim{X} = \dim{Y}$, $f$ is locally given by the identity map, thus $f$ is a local diffeomorphism at $x$. On the other hand, suppose $f^{-1}(y) \subseteq X$ is infinite, then by (limit-point) compactness of $X$, it has a limit point $x$, and $x \in f^{-1}(y)$ because $f^{-1}(y)$ is closed.
    	But then, $f$ cannot even be injective near $x$ (every neighborhood contains another $x'$ in the preimage of $y$), hence not a local diffeomorphism, a contradiction, thus we have $f^{-1}(y)$ must be finite;
    2. By above, there exists $W_i \supseteq x_i$ mapped diffeomorphically to $U_i$.
    	Since $x_i$'s are finite, we can choose those $W_i$'s small enough such that they are mutually disjoint.
    	Now let $U = \cap U_i$, this is a finite intersection so $U$ is neighborhood of $y$, and let $V_i = f^{-1}(U) \cap W_i$ for each $i$, then by construction each $V_i$ is neighborhood of $x_i$ and they are mutually disjoint (because $W_i$'s are). Restrict $f$ on $W_i$ then by assumption it is a bijection, thus $f(V_i) = f(f^{-1}(U) \cap W_i) = U \cap f(W_i) = U \cap U_i = U$. Also by previous exercise (restriction on smooth map), we have that $f$ restricted on $V_i$ maps $V_i$ diffeomorphically to $U$, for each $i$.

    ### Exercise 9

    **Show that the orthogonal group $O(n)$ is compact**.

    Proof

    Since we work in the Euclidean space, we need to show $O(n)$ is closed and bounded.

    1. Closed: it is the preimage of $E$ under $f: A \to AA^T$ (which can be thought as a polynomial, which is continuous) thus it is closed;
    2. Bounded: write $A \in O(n)$ in the form $(a_{ij})$ then by $AA^T = E$ we have a collection of $n \times n$ equations:
    	1. $a_{11}a_{11}+a_{12}a_{12} + \dots + a_{1n}a_{1n} = 1$ (first row product with first column, it is on the diagonal);
    	2. $a_{11}a_{21}+a_{12}a_{22} + \dots + a_{1n}a_{2n} = 0$ (first row product with second column, it is not on the diagonal);
    	3. $\dots$

    	The value not on the diagonal does not really matter here, the point is that, it is obvious that $\sum\limits_j a_{ij}^2 = 1$ for each $i$, thus the Euclidean norm of the whole matrix $A$ is then $\sqrt{n}$, a fixed number. In other word, $O(n)$ is bounded.

    ### Exercise 12

    **Prove that the set of all $2 \times 2$ matrices of rank $1$ is a three-dimensional sub-manifold of $\mathbb{R}^4 = M(2)$**.

    Proof

    Consider the determinant function $\det:M(2) -\lbrace 0 \rbrace \to \mathbb{R}$.

    Notice that for a $2 \times 2$ matrix, by definition it is only possible to have rank $0,1$ or $2$. If its determinant is $0$, it is non-invertible, thus cannot have full rank $= 2$; if in addition it is non-zero (that's the only case when rank is zero), it must have rank $1$.

    In other word, it is sufficient to show that $0$ is a regular value for $\det: M(2) - \lbrace 0 \rbrace \to \mathbb{R}$:

    Let $A = \begin{pmatrix} a&b\\c&d \end{pmatrix}\in M(2)$ with zero determinate, then $d\det_A(A') = \lim\limits_{t\to 0}\frac{\det{A + tA'} - \det{A}}{t}$ $= \lim\limits\frac{(a+ta')(d+td')-(c+tc')(b+tb')-ad+cb}{t}$ $= a' d+ad'-c' b-cb'$. This is surjective.

    By Preimage Theorem, the set of non-zero $2 \times 2$ matrices with zero determinant, thus the set of $2 \times 2$ matrices with rank $1$, is a sub-manifold of $\mathbb{R}^4$ of dimension $\dim{\mathbb{R}^4} - \dim{\mathbb{R}} = 3$.

    ## Additional Problems

    ### Problem A1

    **Let $GL(n, \mathbb{C})$ consist of complex $n \times n$ matrices $A$ such that $\det{A} \ne 0$. Show that $GL(n, \mathbb{C})$ is a Lie group of dimension $2n^2$. It is called the (complex) general linear group**.

    Proof

    Follows the reasoning for $GL(n, \mathbb{R})$:

    $GL(n, \mathbb{C}) \subseteq M_{n\times n}(\mathbb{C})$ consists of all $n\times n$ matrices $A$ with $\det{A} \ne 0$. The function $\det: M_{n \times n}(\mathbb{C}) \to \mathbb{C}$ is a smooth function (being a polynomial), hence $\det^{-1}(0) \subseteq M_{n \times n}(\mathbb{C})$ is closed and $GL(n, \mathbb{C}) = M_{n\times n}(\mathbb{C}) - \det^{-1}(0)$ is open. Therefore, $GL(n, \mathbb{C})$ is a sub-manifold of dimension $2n^2$ (Here is because each complex valued $m \times n$ matrix can be broken down into $2$ matrices, both real valued, and have dimension $mn$).

    Since $\det{AB} = \det{A}\det{B}$ and $\det{A^{-1}} = (\det{A})^{-1}$, $GL(n, \mathbb{C})$ is a group with respect to matrices multiplication.

    Notice that the multiplication $GL(n,\mathbb{C}) \times GL(n,\mathbb{C}) \to GL(n,\mathbb{C})$ and the inverse $GL(n,\mathbb{C}) \to GL(n,\mathbb{C})$ are smooth functions because they can be seen as polynomials: $(AB)_{ij} = \sum\limits_kA_{ik}B_{kj}$ and $A^{-1} = adj{A}/\det{A}$.

    By definition, $GL(n,\mathbb{C})$ is a Lie group of dimension $2n^2$.

    ### Problem A2

    **Let $SL(n, \mathbb{C})$ consist of complex $n \times n$ matrices $A$ such that $\det{A} = 1$. Show that $SL(n, \mathbb{C})$ is a Lie group of dimension $2n^2 - 2$. It is called the (complex) special linear group**.

    Proof

    Consider the function $\det:M_{n \times n}(\mathbb{C}) \to \mathbb{C}$, we want to show that $1$ is a regular value, it is pretty much the same following the reasoning for $SL(n,\mathbb{R})$.

    We want to show that $d(\det)_A:M_{n \times n}(\mathbb{C}) \to \mathbb{C}$ is surjective for all $A$ with $\det{A} = 1$.

    1. Let $A = E$ be the identity matrix and $h \in M_{n \times n}(\mathbb{C})$, then $d(\det)_E(h) = \lim_{t\to 0} \frac{\det{E+th}-\det{E}}{t}$ ($*$).
    	Calculate $\det{E+th}$: let $h = \begin{pmatrix} h_{11}&\cdots&h_{1n}\\ \cdots&\cdots&\cdots \\ h_{n1}&\cdots&h_{nn} \end{pmatrix}$, then $\det{E+th} = \det{\begin{pmatrix} 1+th_{11}&\cdots&th_{1n}\\ \cdots&\cdots&\cdots \\ th_{n1}&\cdots&1+th_{nn} \end{pmatrix}}$ ('$1+$' on the diagonal) $= 1+ t(h_{11} + \cdots + h_{nn}) + O(t^2)$ $= 1 + t\cdot tr(h) + O(t^2)$, therefore ($*$) = $tr(h)$. It is surjective;
    2. Let $A$ be an arbitrary matrix with $\det{A} = 1$. Then $d(\det)_A = \lim_{t \to 0} \frac{\det{A+th}-\det{A}}{t}$ $= \lim_{t\to 0}\frac{\det{A}\det{(E+tA^{-1}h)}-\det{A}}{t} = tr(A^{-1}h)$. For any $z \in \mathbb{C}$, choose $B$ such that $tr(B) = z$ and let $h = AB$, then $tr(A^{-1}h) = tr(A^{-1}AB) = tr(B) = z$.

    Either way, the derivative is surjective and $1$ is indeed a regular value, thus $SL(n,\mathbb{C})$ is a sub-manifold of $M_{n\times n}(\mathbb{C})$ with dimension $2n^2 - 2$ ($\mathbb{C}$ has dimension $2$).

    Now since $\det{AB} = \det{A}\det{B}$ and $\det{A^{-1}} = (\det{A})^{-1}$ thus $SL(n,\mathbb{C})$ is still a group with respect to matrix multiplication, and multiplication and inverse are smooth, we have that $SL(n, \mathbb{C})$ is a Lie group of dimension $2n^2 - 2$.

    ### Problem A3

    **Let $U(n)$ consist of complex $n \times n$ matrices $A$ such that $A\overline{A}^T = E$. Here, $\overline{A}$ is obtained from $A$ by replacing each entry of $A$ with its complex conjugate. Show that $U(n)$ is a Lie group of dimension $n^2$. It is called the unitary group**.

    Proof

    Start with the simple part: $U(n)$ is a group with respect to matrix multiplication because $(AB)\overline{(AB)}^T = (AB)(\overline{B}^T\overline{A}^T) = E$ and if $A\overline{A}^T = E$ then $\overline{A}^T = A^{-1}$, thus $(A^{-1})\overline{A^{-1}}^T = \overline{A}^T A = A \overline{A}^T = E \implies A^{-1} \in U(n)$. Multiplication and inverse are smooth as usual. Now we need to show that it is a sub-manifold of dimension $n^2$.

    Consider the function $f: M_{n \times n}(\mathbb{C}) \to M_{n \times n}(\mathbb{C})$ given by $A \mapsto A\overline{A}^T$.

    Clearly this map is not surjective, we need to understand its range: notice that for any $A$, $\overline{A\overline{A}^T}^T = \overline{\overline{A}^T}^T\overline{A}^T = A\overline{A}^T$. In other words, the range consists of matrix whose conjugate transpose is itself $H = \lbrace A | \overline{A}^T = A \rbrace$.

    A basis for this space:

    1. On the diagonal it is required to have $(a)_{ii}$ being real, so it has basis matrix with $(i,i) = 1$ and everywhere else $0$, there are $n$ of them;
    2. Now for anywhere else, it may be broken down into two parts:
    	1. Real part consists of matrix with $(i,j) = (j, i) = 1, i\ne j$, since the real part does not change when we taking conjugate transpose. There are $n(n-1)/2$ of them;
    	2. And imaginary part consists of matrix with $(i, j) = 1, (j,i) = -1, i\ne j$, since the imaginary part got 'inverted' when taking conjugate transpose. There are also $n(n-1)/2$ of them.

    So $\dim{H} = n + n(n-1) = n^2$, if we can show that $E$ is a regular value for $f$ we are done.

    $U(n) = f^{-1}(E)$, for any $A \in U(n)$, we have $df_A(h) = \lim\limits_{t \to 0}\frac{f(A+th)-f(A)}{t}$ $=\lim\limits\frac{(A+th)\overline{(A+th)}^T-A\overline{A}^T}{t}$ $=\lim\limits\frac{A\overline{A}^T + t(h\overline{A}^T+A\overline{h}^T) + O(t^2) - A\overline{A}^T}{t}$ $=h\overline{A}^T + A\overline{h}^T$.

    We want to show this map is surjective:

    For any $C \in H$, let $C = \frac{1}{2}\overline{C}^T+\frac{1}{2}C$ and solve the equations:

    1. $A\overline{h}^T = \frac{1}{2}C$: $\overline{h}^T = \frac{1}{2}A^{-1}C = \frac{1}{2}\overline{A}^TC \implies h = \frac{1}{2}\overline{C}^TA$;
    2. Now check: $h\overline{A}^T = \frac{1}{2}\overline{C}^TA\overline{A}^T = \frac{1}{2}\overline{C}^T$ is indeed what we want.

    This shows that the derivative is surjective, thus $E$ is a regular value for $f$, and its preimage, $f^{-1}(E) = U(n)$ is a sub-manifold of dimension $2n^2 - n^2 = n^2$.

    ### Problem A4

    **Show that $U(1)$ is diffeomorphic, as a manifold, to the circle. Let $SU(2)$ be the subgroup of $U(2)$ consisting of matrices with determinant $1$. Show that $SU(2)$ is diffeomorphic, as a manifold, to the $3$-sphere**.

    Proof

    1. By definition $U(1) = \lbrace (a+ib) | (a+ib)(a-ib) = 1 \implies a^2+b^2 = 1, a,b \in \mathbb{R} \rbrace$, so simply take $f: U(1) \to S^1$ as the identity map, it is clearly a diffeomorphism;
    2. Let $A = \begin{pmatrix} a_{11}+ib_{11}&a_{12}+ib_{12}\\a_{21}+ib_{21}&a_{22}+ib_{22} \end{pmatrix} \in SU(2)$, then it has to satisfy that $A\overline{A}^T = E$ and $\det{A} = 1$. Notice that since $A\overline{A}^T = E$ we have $\overline{A}^T = A^{-1}$.
    	This made $SU(2)$ rather simple:
    	If $A = \begin{pmatrix} a&b\\c&d \end{pmatrix} \in SU(2)$ then $A^{-1} = \frac{1}{\det{A}}\begin{pmatrix} d&-b\\-c&a \end{pmatrix} = \begin{pmatrix} d&-b\\-c&a \end{pmatrix} = \overline{A}^T = \begin{pmatrix} \overline{a}&\overline{c}\\\overline{b}&\overline{d} \end{pmatrix}$.
    	So we have to have $a = \overline{d}$ and $c = -\overline{b}$ and $A$ is simplified to $\begin{pmatrix} a&-\overline{b}\\b&\overline{a} \end{pmatrix} = \begin{pmatrix} u+iv&-x+iy\\x+iy&u-iv \end{pmatrix}$.
    	Now it is clear that in order to have $A\overline{A}^T = E$ we need to have $u^2+v^2+x^2+y^2 = 1$. Thus $SU(2)$ is diffeomorphic to the $3$-sphere.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 05""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 1.5

    ### Exercise 2

    **Which of the following linear spaces intersect transversally**?

    1. **The $xy$ plane and the $z$ axis in $\mathbb{R}^3$**;
    2. **The $xy$ plane and the plane spanned by $\lbrace (3,2,0),(0,4,-1) \rbrace$ in $\mathbb{R}^3$**;
    3. **The plane spanned by $\lbrace (1,0,0),(2,1,0) \rbrace$ and the $y$ axis in $\mathbb{R}^3$**;
    4. $\mathbb{R}^k \times \lbrace 0 \rbrace$ **and $\lbrace 0 \rbrace \times \mathbb{R}^l$ in $\mathbb{R}^n$**;
    5. $\mathbb{R}^k \times \lbrace 0 \rbrace$ **and $\mathbb{R}^l \times \lbrace 0 \rbrace$ in $\mathbb{R}^n$**;
    6. $V \times \lbrace 0 \rbrace$ **and the diagonal in $V \times V$**;
    7. **The symmetric $(A^T = A)$ and the skew symmetric $(A^T = -A)$ matrices in $M(n)$**.

    Solution

    First, notice that all of those spaces are vector spaces (plane, diagonal, symmetric matrix, etc.), so their tangent space at any point is just themselves, making the job much easier.

    Now we check them one by one:

    1. Is transversal, clearly they together span $\mathbb{R}^3$;
    2. Is transversal, in fact two planes are always transversal as long as they are not the same plane;
    3. Is not transversal, they together only span the $xy$ plane;
    4. It is a generalization of the above $\mathbb{R}^3$ cases, if $n \le k + l$ then each dimension is being spanned (not $0$) thus transversal;
    5. Similar with above, however, this time we have to have either $n = l$ or $n = k$ (assuming $k,l\le n$) to make sure the spaces span $\mathbb{R}^n$;
    6. Is transversal, for any $v_1 \times v_2 \in V \times V$, choose $v_2 \times v_2$ from the diagonal and $(v_1 - v_2) \times 0$, they combine into $v_1 \times v_2$;
    7. Is transversal, any matrix in $M(n)$ can be written into linear combination (summation) of a symmetric matrix and a skew symmetric matrix. For example, $\begin{pmatrix} 2&3\\-7&9 \end{pmatrix}$ can be written as $\begin{pmatrix} 2&-2\\-2&9 \end{pmatrix}$ (symmetric matrix, meet the diagonal, then take average of each transposing value, $(3-7)/2 = -2$ this case) and $\begin{pmatrix} 0&5\\-5&0 \end{pmatrix}$ (skew symmetric matrix, $0$ in the diagonal, then padding the rest).

    ### Exercise 4

    **Let $X$ and $Z$ be transversal sub-manifolds of $Y$. Prove that if $y \in X \cap Z$, then $T_y(X\cap Z) = T_yX \cap T_yZ$**.

    Proof

    Since $X \cap Z \subseteq X$ and $\subseteq Z$, naturally $T_y(X \cap Z) \subseteq T_yX$ and $T_y(X \cap Z) \subseteq T_yZ$ thus $T_y(X \cap Z) \subseteq T_yX \cap T_yZ$. Since both sides are vector spaces, all we need is to show that they have the same dimension.

    Since $X$ and $Z$ are transversal we have that $\dim{X \cap Z} = \dim{X} + \dim{Z} - \dim{Y}$, thus $\dim{T_y(X \cap Z)} = \dim{T_yX} + \dim{T_yZ} - \dim{T_yY}$ ($*$).

    On the other hand, by direct calculation we have that $\dim{(T_yX \cap T_yZ)} = \dim{T_yX} + \dim{T_yZ} - \dim{(T_yX + T_yZ)}$ ($**$) (kind of like playing with the Venn diagrams: the union of two sets is the sum of the two sets excludes their intersection otherwise the intersection is counted twice), but $X$ and $Z$ are transversal implies that $T_yX + T_yZ = T_yY$ and thus $\dim{(T_yX + T_yZ)} = \dim{T_yY}$.

    Thus the value of ($*$) and ($**$) indeed coincides, and we have $T_y(X\cap Z) = T_yX \cap T_yZ$.

    ### Exercise 8

    **For which values of $a$ does the hyperboloid defined by $x^2+y^2-z^2 = 1$ intersect the sphere $x^2+y^2+z^2 = a$ transversally? What does the intersection look like for different values of $a$**?

    Solution

    If $\sqrt{a}<1$, there is no intersection between the two surfaces, thus trivially they are transversal:

    <img src="public/Pasted image 20210903021337.png" width="400" />

    If $\sqrt{a} = 1$, the intersection is $x^2 + y^2 = 1$. By previous exercise we can see that for any point in the intersection, the tangent spaces to the hyperboloid and the sphere are the same (vertical plane parallel with the $yz$ plane), and they cannot span $\mathbb{R}^3$, thus they are not transversal:

    <img src="public/Pasted image 20210903021612.png" width="400" />

    Otherwise $\sqrt{a}>1$, solve for the two equations we have that $z = \pm\sqrt{\frac{a-1}{2}} \ne 0$ and thus the gradient of the hyperboloid (at a point in the intersection, of course) of the sphere are $(2x,2y,-2z)$ and $(2x,2y,2z)$ are linearly independent, thus the two tangent spaces would span $\mathbb{R}^3$, and the two surfaces are transversal:

    <img src="public/Pasted image 20210903021550.png" width="400" />

    ### Exercise 9

    **Let $V$ be a vector space, and let $\Delta$ be the diagonal of $V \times V$. For a linear map $A: V \to V$, consider the graph $W = \lbrace (v, Av): v \in V \rbrace$. Show that $W$ and $\Delta$ are transversal if and only if $+1$ is not an eigenvalue of $A$**.

    Proof

    By definition $W$ and $\Delta$ are transversal is the same as saying $W + \Delta = V \times V$. Thus any element $u \times v \in V \times V$ should be able to be written as $u \times v = (v_1 + v_2) \times (v_1 + Av_2)$, where $(v_1, v_1)$ is from the diagonal and $(v_2, Av_2)$ is from $W$.

    In other words, we need to solve for $u = Iv_1 + Iv_2$ and $v = Iv_1 + Av_2$ for arbitrary $u,v$. We have $v-u = (A-I)v_2$ and we can solve for $v_2$ (for arbitrary $u,v$) if and only if $A-I = A-1I$ is invertible, but this is equivalent with that $\det{A-1I}$ is non-zero and $1$ is not an eigenvalue of $A$.

    ## Section 1.6

    ### Exercise 3

    **Show that every connected manifold $X$ is arc-wise connected: given any two points $x_0,x_1 \in X$, there exists a smooth curve $f: I \to X$ with $f(0) = x_0, f(1) = x_1$**.

    Proof

    1. Claim that being joined by a smooth curve is an equivalence relation:
    	1. The relation is trivially reflexive;
    	2. The relation is symmetric: say $x_0$ and $x_1$ is connected by smooth $h$, define $\tilde{h}$ by $\tilde{h}(t) = h(1-t)$ then this is smooth (composite $h$ and $(1-t)$) curve connecting $\tilde{h}(0) = h(1) = x_1$ and $\tilde{h}(1) = h(0) = x_0$;
    	3. The relation is transitive: suppose $x_{0,1,2} \in X$ such that $f$ is a smooth curve with $f(0) = x_0, f(1) = x_1$ and $g$ is a smooth curve with $g(0) = x_1, g(1) = x_2$. We can construct homotopies $F: X \times I \to X, F(x,t) = f(t)$ and $G: X \times I \to X, G(x,t) = g(t)$. Since smooth homotopy is an equivalence relation, there is a homotopy $H$ with $H(x,0) = x_0, H(x,1) = x_2$, and it can induce $h(t) = h_x(t) = H(x,t)$, a smooth map connecting $x_0$ and $x_2$;
    2. The equivalence classes are open:
    	Take any $x \in X$ and let $R$ be the equivalence class for $x$. Since $X$ is a manifold, there exists $O(x)$ diffeomorphic to $\mathbb{R}^k$, which is arc-wise connected, thus $O(x)$ is arc-wise connected. But that means $O(x) \subseteq R$. Since $x$ is arbitrary, this implies that its equivalence class $R$ is open.
    	Now, for any $x \in X$, say $R$ is the equivalence class, if $R$ not equals $X$, then $X-R$ is the union of all other equivalence classes, which is a union of open sets thus is open, but then $X = R \cup (X-R)$ forms a separation thus $X$ is not connected, we have a contradiction. Thus in fact $X$ has only one equivalence class, and this is equivalent with the statement we want.

    ### Exercise 4

    **A manifold $X$ is contractible if its identity map is homotopic to some constant map $X \to \lbrace x \rbrace$, $x$ being a point of $X$. Check that if $X$ is contractible, then all maps of an arbitrary manifold $Y$ into $X$ are homotopic (and conversely)**.

    Proof

    By assumption, let $F$ be the homotopy between identity map $\text{id}$ on $X$ and a constant map $f$, i.e. $F(x,0) = \text{id}(x) = x$, $F(x,1) = f(x) = c$. Then for any $g: Y \to X$, $F \circ (g \times \text{id}_I): Y\times I \to X \times I \to X$ is a homotopy between $g$ and the constant map, as $F(g(y), 0) = \text{id}(g(y)) = g(y)$ and $F(g(y), 1) = f(g(y)) = c$. In other word, any $g$ is homotopic to the constant map.

    We proved that homotopy is an equivalence relation, so any two $g_1, g_2$ are homotopic to the constant function thus homotopic to each other.

    The converse is simple: since it works for arbitrary manifold $Y$, we can take $Y = X$ (by assumption $X$ is indeed a manifold, so we can do it) then $X$ is clearly contractible.

    ### Exercise 6

    **A manifold $X$ is simply connected if it is connected and if every map of the circle $S^1$ into $X$ is homotopic to a constant. Check that all contractible spaces are simply connected, but convince yourself that the converse is false**.

    Proof

    Since $S^1$ is a manifold, let $g: S^1 \to X$ be an arbitrary map and $f: S^1 \to X$ be a constant map, by above exercise $g$ and $f$ are homotopic.

    $X$ is connected: say we have the homotopy $F(x,t)$ between $\text{id}$ to a constant map $f(x) = c$, for any fixed $x$ this gives us a continuous (smooth, but we don't really need it) map $g_x(t) = F(x,t)$ where $g_x(0) = x$ and $g_x(1) = c$. Now for any $x, y \in X$, find the map $g_x$ and $g_y$ and combine them to $g(t) = \begin{cases} g_x(2t), 0\le t\le 1/2\\g_y(2 - 2t), 1/2 \le t \le 1 \end{cases}$. This is a continuous map with $g(0) = x$ and $g(1) = y$, since $x,y$ arbitrary, we have $X$ is path-connected thus connected.

    The converse is false, for example, $S^2$ is simply connected but not contractible.

    ### Exercise 7

    **Show that the antipodal map $x \to -x$ of $S^k \to S^k$ is homotopic to the identity if $k$ is odd**.

    Proof

    If $k = 1$, we have the homotopy $F_1(x,y,t) = \begin{pmatrix} \cos(\pi t)&-\sin(\pi t)\\\sin(\pi t)&\cos(\pi t) \end{pmatrix} \begin{pmatrix} x\\y \end{pmatrix}$ $= \begin{pmatrix} x\cos(\pi t)-y\sin(\pi t)\\x\sin(\pi t)+y\cos(\pi t) \end{pmatrix}$, so that $F_1(x,y,0) = \begin{pmatrix} x\\y \end{pmatrix}$ and $F_1(x,y,1) = \begin{pmatrix} -x\\-y \end{pmatrix}$, all these functions are clearly smooth.

    Analogous to this, for any $k$ odd, consider this linear map:

    $F_k(x_1,\dots,x_{2k}, t)$ $= \begin{pmatrix} \cos(\pi t)&-\sin(\pi t)&0&0&\dots&\dots&0&0\\ \sin(\pi t)&\cos(\pi t)&0&0&\dots&\dots&0&0\\ 0&0&\cos(\pi t)&-\sin(\pi t)&\dots&\dots&0&0\\ 0&0&\sin(\pi t)&\cos(\pi t)&\dots&\dots&0&0\\ 0&0&0&0&\dots&\dots&0&0\\ 0&0&0&0&\dots&\dots&0&0\\ 0&0&0&0&\dots&\dots&\cos(\pi t)&-\sin(\pi t)&\\ 0&0&0&0&\dots&\dots&\sin(\pi t)&\cos(\pi t) \end{pmatrix} \begin{pmatrix} x_1\\x_2\\\dots\\x_{2k} \end{pmatrix}$, the image would be $\begin{pmatrix} y_1\\y_2\\\dots\\y_{2k} \end{pmatrix}$ where we can calculate that:

    1. $y_1 =x_1\cos(\pi t)-x_2\sin(\pi t) = \begin{cases} x_1, t= 0\\-x_1,t=1 \end{cases}$;
    2. $y_2 =x_1\sin(\pi t)+x_2\cos(\pi t) = \begin{cases} x_2, t= 0\\-x_2,t=1 \end{cases}$;
    3. $y_3 =x_3\cos(\pi t)-x_4\sin(\pi t) = \begin{cases} x_3, t= 0\\-x_3,t=1 \end{cases}$;
    4. $\dots$

    And this is the homotopy we want.

    Not a Redo:

    We also need to show that for any $t$ and odd $k$, $F_k(S^k, t) \subseteq S^k$, this can be easily done by triangle-function calculations, but it should be part of the proof.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 06""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 1.6

    ### Exercise 9

    **Prove that the Stability Theorem is false on non-compact domains. Let $\rho: \mathbb{R} \to \mathbb{R}$ be a function with $\rho(s) = 1$ if $| s | < 1$, $\rho(s) = 0$ if $| s | > 2$. Define $f_t:\mathbb{R} \to \mathbb{R}$ by $f_t(x) = x\rho(tx)$. Verify that this is a counterexample to all six parts of the theorem**.

    Proof

    In the given example, $f_0:\mathbb{R} \to \mathbb{R}$ is given as $f_0(x) = x\rho(0) = x$, i.e. the identity map. So it is clearly a diffeomorphism and a local diffeomorphism; graphically it is easy to see that it is transversal to any given sub-manifold; and it is also immersion, submersion, and embedding (I guess it is not totally rigorous here since $\dim{\mathbb{R}} = \dim{\mathbb{R}}$?).

    Now, for any $t > 0$, take large (or small) enough $x$ then we will have that $| tx | > 2$ so that $f_t(x) = 0$ for all such $x$. But then $f_t$ clearly cannot be injective near $x$, so it is neither a local diffeomorphism nor a diffeomorphism; also, its derivative is also constant $0$ so neither injective nor surjective, thus $f_t$ is not an immersion, a submersion, or an embedding. Consider $Z = \lbrace 0 \rbrace$ then $f_t^{-1}(0) = \lbrace x | x = 0$ or $| x |>2/| t |\rbrace$, but for larger or small enough $x$, $df_x(T_xX) + T_{f(x)}Z = \lbrace 0 \rbrace + \lbrace 0 \rbrace \ne \mathbb{R} = T_{f(x)}Y$, so $f$ is not transversal to $Z$.

    ## Section 1.7

    ### Exercise 4

    **Prove that the rational numbers have measure zero in $\mathbb{R}$, even though they are dense**.

    Proof

    We know that $\mathbb{Q}$ is countable, so we can write $\mathbb{Q} = \bigcup\limits_i r_i$, with $r_i$ be enumerated rational numbers. Given any $\varepsilon > 0$ we can cover $\mathbb{Q}$ with (one-dimensional) cubes $\bigcup\limits_i (r_i - \varepsilon/2^{i+2}, r+\varepsilon/2^{i+2}$ with the total volume being a geometric series $\varepsilon/4 + \varepsilon/8 + \dots$ $= \frac{1}{4}(\varepsilon + \varepsilon/2 + \dots)$ $= \varepsilon/2 < \varepsilon$, by definition $\mathbb{Q}$ has measure zero.

    ### Exercise 6

    **Prove that the sphere $S^k$ is simply connected if $k > 1$**.

    Proof

    Clearly $S^k$ is path connected thus connected, we need to check the other condition about homotopy.

    Let $f: S^1 \to S^k$ be a smooth map (of manifolds), since $k > 1$ we have $\dim{S^1} < \dim{S^k}$. By Sard, there exists $p \in S^k$ with $p \notin f(S^1)$. Consider the stereographic projection using $p$ as the 'north pole', $S^k - \lbrace p \rbrace$ can be seen that is diffeomorphic with $\mathbb{R}^k$, which is contractible, thus $S^k - \lbrace p \rbrace$ is contractible.

    $f(S^1)$ is contained in $S^k - \lbrace p \rbrace$, so by definition of contractible manifold, $f$ is homotopic to some constant map $g: S^1 \to \lbrace c \rbrace \subseteq S^k -\lbrace p \rbrace$, but the domain of $f$ is in fact $S^1$. Since $f$ can be arbitrary, by definition, $S^k$ is simply connected.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 07""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 1.8

    ### Exercise 5

    **Prove that the projection map $p:TX \to X, (x,v) \mapsto x$ is a submersion**.

    Proof

    ~~Say $X$ is a $n$-manifold (so that $TX$ is also a manifold). Let $r: O(x,v) \to U$ and $s: O(x) \to V$ be local coordinates with $r(x,v) = (x,v)$, $s(x) = x$, so that we can define $h = s\circ p|_{}\circ r^{-1}: U \to O(x,v) \to O(x) \to V$, $(x,v) \mapsto (x,v) \mapsto x \mapsto x$ is a linear map. Now $d\pi_{(x,v)}$ is the Jacobian of $h$ which would have the form $\begin{pmatrix}I_n | 0\end{pmatrix}$, which has rank $= n$ equals the number of rows, thus $d\pi_{(x,v)}$ is surjective thus $\pi$ is a submersion at $(x,v)$. Since $(x,v)$ can be arbitrary, $\pi$ is a submersion.~~

    Redo:

    Need to show that for any $(x,v) \in TX$, the derivative $dp_{(x,v)}: T_{(x,v)}(TX) \to T_xX$ is surjective. Choose a local parametrization $r:U \to O(x)$ for $x$, then $dr: U \times \mathbb{R}^n \to TO(x)$, $dr(u,v) = (r(u), dr_u(v))$ is a local parametrization for $TX$. Then we have: $$\begin{CD}TO(x) @>p>> O(x) \\@AdrAA @AArA \\ U\times\mathbb{R}^n @>h>> U \end{CD}$$ $h(u,v) = r^{-1}(p(dr(u,v))) = u$, hence $h:U\times \mathbb{R}^n \to U$ is just the projection onto $U$. Its derivative is also a projection, hence surjective, and then $dp_{(x,v)}$ is surjective.

    ### Exercise 6

    **A vector field $\vec{v}$ on a manifold $X$ in $\mathbb{R}^N$ is a smooth map $\vec{v}: X \to \mathbb{R}^N$ such that $\vec{v}(x)$ is always tangent to $X$ at $x$. Verify that the following definition which does not explicitly mention the ambient $\mathbb{R}^N$ is equivalent: a vector field $\vec{v}$ on $X$ is a cross section of $TX$- that is, a smooth map $\vec{v}: X \to TX$ such that $p \circ \vec{v}$ equals the identity map of $X$**.

    Proof

    $\vec{v}(x) = v$ is always tangent to $X$ at $x$ means that $v$ lies inside $T_xX$. For each $x \in X$, assign one such $v$ to it as $\vec{v}(x) = v$ and re-write it as $\vec{v}(x) = (x,v)$ so that $(x,v)$ has the form $x \in X, v \in T_xX$. By definition of a tangent bundle, $\vec{v}(x) \in TX$ and $\vec{v}(X) \subseteq TX$ Furthermore, $p \circ \vec{v}(x) = p(\vec{v}(x)) = p(x,v) = x$ maps $x$ to itself for any $x \in X$.

    For the other way round: in that definition $\vec{v}(x)$ must have the form $(y,u)$, where $y$ in $X$ and $u \in T_yX$. But if $y \ne x$, then $p(\vec{v}(x)) = p(y,u) = y \ne x$ is not the identity, thus $y = x$ and $u \in T_xX$ anyway. Re-write $\vec{v}(x) = u$ and this map sends $x$ to some $u$ in the tangent space, thus being tangent to $X$ at $x$, for any $x$.

    ### Exercise 7

    **A point $x \in X$ is a zero of the vector field $\vec{v}$** if $\vec{v}(x) = 0$ Show that **if $k$ is odd, there exists a vector field $\vec{v}$** on $S^k$ **having no zeros**.

    Proof

    For any odd $k = 2n-1$, consider the map $\vec{v}(x_1, x_2, \dots, x_{2n}) = (-x_2, x_1, \dots, -x_{2n}, x_{2n-1})$ This is a vector field: for any $(x_1, x_2, \dots, x_{2n})$, $\vec{v}(x_1, x_2, \dots, x_{2n}) \cdot (x_1, x_2, \dots, x_{2n})$ $=-x_1x_2+x_1x_2 -\dots-x_{2n}x_{2n-1}+x_{2n}x_{2n-1} =0$, thus the two vectors are perpendicular and thus the image is in the tangent space.

    By construction, $0 \in \mathbb{R}^{2n}$ is the only possible zero of the vector field (we need $x_i = 0$ for all $i$), but clearly $0$ is not in $X$, thus the vector field does not have a zero.

    ### Exercise 8

    **Prove that if $S^k$ has a non-vanishing vector field, then its antipodal map is homotopic to the identity**.

    Proof

    Let $\vec{v}$ be the non-vanishing vector field we have. Now define a map $\vec{u}, x \mapsto \frac{\vec{v}(x)}{\| \vec{v}(x) \|}$ so that the image vector always have length $1$, we can do this because $\|\vec{v}(x) \|$ is by assumption never $0$. $\vec{u}$ is a vector field, because its image is inherited from $\vec{v}$, just with possibly different length.

    Now define $F: S^k \times I \to S^k$ with $(x,t) \mapsto x\cos(t\pi) + \vec{u}(x)\sin(t\pi)$, we have:

    1. $F(x,0) = x$ is the identity;
    2. $F(x,1) = -x$ is the antipodal map;
    3. For any $t$ and any $x$, $\| F(x,t) \|$ $= \| x \| \cos^2(t \pi) + \| \vec{u}(x) \| \sin^2(t \pi)$ $= 1$ as both $x$ and $\vec{u}(x)$ has length $1$, so that each $f_t$ indeed has codomain $S^k$;
    4. Each $f_t$ and $F$ are smooth, they are simply product of smooth functions.

    I.e. We find such homotopy between the identity and the antipodal map.

    ### Exercise 10

    **Prove that every $k$-dimensional manifold $X$ may be immersed in $\mathbb{R}^{2k}$**.

    Proof

    Let $f: X \to \mathbb{R}^N$ be an immersion with $2k < N$, and consider the map $g: TX \to \mathbb{R}^N$, $(p,v) \mapsto df_p(v)$.

    By class material we have that $\dim(TX) = 2k < N$, thus by mini-Sard, $\text{im}(g)$ have measure zero in $\mathbb{R}^N$, thus there exists $a \ne 0$ not in $\text{im}(g)$. Let $H$ be the hyperplane in $\mathbb{R}^N$ perpendicular to $a$. Consider the orthogonal projection $\pi: \mathbb{R}^N \to H$, we claim that it is an immersion:

    Suppose not, then there is a point $p \in X$ such that $d(\pi \circ f)_p: T_pX \to H$ is not injective, i.e. the kernel of the map is not $0$: $\exists v \ne 0$ with $0 = d(\pi \circ f)_p(v)$ $=(d\pi \circ df)_p(v)$ $= \pi(df_p(v))$, hence either $df_p(v) = 0$ or $df_p(v)$ is perpendicular to $H$ thus equals some $t\cdot a$ with $t \ne 0$. By assumption $df_p$ is injective thus $df_p(v) \ne 0$, thus it equals $t\cdot a$.

    But then $a = \frac{1}{t}df_p(v) =^{\text{linear}} df_p(\frac{1}{t}\cdot v) = g(p, \frac{1}{t} \cdot v) \in \text{im}(g)$, since we explicitly assumed that $a$ not being in the image, this gives a contradiction.

    So we can reduce $N$ to $\dim{H} < N$, the process is repeatable, if necessary, until $\dim{H} = 2k$ (then we cannot apply mini-Sard to get such $a$ we need), thus we may (use this method to) reduce $N$ to the desired $2k$.

    ## Section 2.2

    ### Exercise 1

    **Any one-dimensional, compact, connected sub-manifold of $\mathbb{R}^3$ is diffeomorphic to a circle. But can it be deformed into a circle within $\mathbb{R}^3$**?

    Solution

    I think the exercise is asking if we can 'unwrap' any loop in $\mathbb{R}^3$ without breaking it. The answer is no, a trefoil is an example.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 08""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 2.1

    ### Exercise 1

    **If $U \subseteq \mathbb{R}^k$ and $V \subseteq \mathbb{R}^k_+$ are neighborhoods of $0$, prove that there exists no diffeomorphism of $V$ with $U$**.

    Proof

    ~~The statement is true for $k = 1$, indeed, there is no even homeomorphism between $U,V$ in the form $U = (a, b)$, $V = [0, c)$.~~

    ~~Now for $k = 2$: if there exists a diffeomorphism $f = (f_1(x_1, x_2), f_2(x_1,x_2))$, then by fixing $x_1 = c$, $f$ induces a map $\tilde{f}(x_2) = f_1(c,x_2)$ which is a diffeomorphism between $U, V$ in the $k = 1$ case, which cannot be true as argued. Thus there is no diffeomorphism between $U, V$ when $k = 2$ neither.~~

    ~~Now we can continue inductively to get the desired statement.~~

    Redo:

    The problem of above proof is that in the $k=2$ case we cannot ensure that the induced $V$ has the form $[0,c)$.

    In fact, on a second thought, this works out in a much simpler (more basic) way:

    $U$ is by assumption open in $\mathbb{R}^k$, no problem.

    $V$, however, has $0$ that is not in its interior ($x \in \text{int}(X)$ if and only if there exists $O(x) \subseteq X$), thus $V$ is not open in $\mathbb{R}^k$.

    A diffeomorphism is a homeomorphism, and thus an open map, thus $U, V$ cannot be diffeomorphic.

    ### Exercise 2

    **Prove that if $f: X \to Y$ is a diffeomorphism of manifolds with boundary, then $\partial f$ maps $\partial X$ diffeomorphically onto $\partial Y$**.

    Proof

    Say $x \in \partial X$, suppose we have $f(x) = y \notin \partial Y$. Then by definition, $y$ is not a point that belong to the image (say under some local parametrization $r: U \to O(y)$) of the boundary of $\mathbb{R}^k_+$. But then $f^{-1}\circ r$ is a (composition of) diffeomorphism between $U$, which is an open set of $\mathbb{R}^k_+$ of the first type, and some $O(x)$, which contradict the fact that $x \in \partial X$. Thus $f(x) = y \in \partial Y$. In other words, $f(\partial X) \subseteq \partial Y$.

    The same argument applies to $f^{-1}$ which is also a diffeomorphism, so we have $f(\partial X) = \partial Y$.

    Moreover, restriction of a smooth map is smooth and restriction of a bijective map is bijective, thus we have $f$ restricted on $\partial X$ is a bijection and is smooth (also have smooth inverse, of course), thus it is a diffeomorphism.

    ### Exercise 4

    **Show that the solid hyperboloid $x^2+y^2-z^2\le a$ is a manifold with boundary ($a > 0$)**.

    Proof

    $\mathbb{R}^3$ is a manifold (without boundary). Consider the map $f: \mathbb{R}^3 \to \mathbb{R}$ given by $(x,y,z) \mapsto x^2+y^2-z^2$ so that $df_{(x,y,z)}(u,v,w) = 2xu+2yv-2zw$, this map is surjective unless $x=y=z=0$, but that is only of concern when given $a = 0$. Thus $a>0$ is a regular value for $f$, and thus $\lbrace (x,y,z) | f(x,y,z)\le a \rbrace$ is a manifold with boundary as desired.

    ### Exercise 6

    **There are two standard ways of making manifolds with boundary out of the unit square by gluing a pair of opposite edges. Simple gluing produces the cylinder, whereas gluing after one twist produces the closed Möbius band. Check that the boundary of the cylinder is two copies of $S^1$, while the boundary of the Möbius band is one copy of $S^1$. Consequently, the cylinder and Möbius band are not diffeomorphic. What happens if you twist $n$ times before gluing**?

    Solution

    Say we have $I^2$ and we glue upper side with lower side, so that the boundary of the resulting object would be $\lbrace (0,i) | i \in I \rbrace \cup \lbrace (1,i) | i \in I \rbrace$.

    1. For a cylinder, glue without twisting gives us $(i,0) \equiv (i,1)$.
    	In particular, $(0,0) \equiv (0,1)$, $(1,0) \equiv (1,1)$, but no $(0,i)$ and $(1,j)$ are equivalent.
    	Thus $f_1:[0,1] \to I^2, i \mapsto (0,i)$, noticing that $f_1(0) \equiv f_1(1)$, gives us a copy of $S^1$, and $f_2:[0,1] \to I^2, i \mapsto (1,i)$ gives us another copy of $S^1$. The images are $\lbrace (0,i) | i \in I \rbrace$ and $\lbrace (1,i) | i \in I \rbrace$ respectively and are disjoint, i.e. the boundary $\lbrace (0,i) | i \in I \rbrace \cup \lbrace (1,i) | i \in I \rbrace$ is given by two copies of $S^1$;
    2. For a Möbius band, glue with one twist gives us $(i,0) \equiv (1-i,1)$.
    	In particular, $(0,0) \equiv (1,1), (1,0) \equiv (0,1)$.
    	Thus $f:[0,1] \to I^2$, $i \mapsto \begin{cases} (0,2i),i\le 1/2\\(1,2i-1),i\ge1/2 \end{cases}$, notice that at $i = 1/2$ the two definition coincides, because $(0,1) \equiv (1,0)$, and that $f(1) = f(0)$, gives us one copy of $S^1$, and that is the boundary of a Möbius band;
    3. If we twist more times, the results are the analogous, because twisting $n$ times gives us that $(i,0) \equiv (1-1+1-1+\dots+/-i,1)$ is either $(i,1)$ (i.e. $n$ even, in this case the boundary is the same as cylinder's boundary) or $(1-i,1)$ (i.e. $n$ odd, boundary is the same as Möbius band's boundary).

    ## Section 2.2

    ### Exercise 3

    **Find maps of the solid torus into itself having no fixed points. Where does the proof of the Brouwer theorem fail**?

    Solution

    Consider the map(s) $f_{\alpha}: ST \to ST$ given by $(r,\theta,h) \to (r,\theta+\alpha,h)$, where the first coordinate is the distance of the projection of the point onto xy-plane and the center of the torus; second coordinate is the angle; and the third coordinate is the height. I.e. the map rotates the torus by angle $\alpha$. This map does not have a fixed point unless (mod $\pi$) we have $\theta+\alpha = \theta \implies \alpha = 0$.

    The proof of the Brouwer theorem fails because $g$ is not easy to be defined here; originally we define $g$ as the intersection of $(x, f(x))$ line and the boundary that is closest to $x$, but it does not work now.

    For example, if we take $f$ as a 180 degree rotation, then for $x$ at the 'middle' of the donuts (in an annulus case it means that the distances from $x$ to the inner and outer circle are same), the line $(x, f(x))$ will hit the annulus at four points, two of which are 'closest' to $x$ and are closer to $x$ than $f(x)$ (remark, this never happens in $D^n$).

    We cannot let $g(x)$ takes two values there, otherwise $g$ is not even a function, so we need to make a choice:

    - If we just randomly pick one, this will make $g$ not being continuous;
    - If say we make a new rule that $t$ must less than or equal $1$ so that we pick the $g$ on the inner circle, then it causes $g$ to never take value on the outer circle, so that $g|_{\partial ST}$ is not the identity map anyway (in some sense this also makes $g$ not being continuous).

    ### Exercise 4

    **Prove that the Brouwer theorem is false for the open ball $| x |^2 < a$**.

    Proof

    Let's say we have a $k$ dimensional disk and WLOG say $a = 1$. Take $e = (1,0,0, \dots, 0) \in \mathbb{R}^k$. Consider the map $f:D^k \to D^k$ (not surjective though) given as $x \to \frac{x + e}{2}$:

    1. The codomain is indeed $D^k$: for any $(x_1, \dots, x_k) \in D^k$, $\| f(x_1, \dots, x_k) \|^2$ $= ((x_1+1)/2)^2 + (x_2/2)^2 + \dots + (x_k/2)^2$ $= \frac{x_1^2+\dots+x_k^2}{4} + \frac{1}{4} + \frac{x_1}{2}$ $< \frac{1}{4} + \frac{1}{4} + \frac{1}{2} = 1$, i.e. $f(x_1, \dots, x_k) \in D^k$;
    2. There is no fixed point: $f(x) = \frac{x+e}{2} = x \implies x = e = (1,0,\dots,0)$ but this point is not in $D^k$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 09""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 2.4

    ### Exercise 1

    **Prove that there exists a complex number $z$ such that $z^7 + \cos(| z |^2)(1+93z^4) = 0$**.

    Proof

    Let $f(z) = z^7 + \cos(| z |^2)(1+93z^4)$.

    Consider the homotopy $F(z,t) = z^7 + t(\cos(| z |^2)(1+93z^4))$ with $F(z,0) = z^7$ and $F(z,1) = f(z)$. View each function as $f_t: \mathbb{C} \to \mathbb{C}$. Let $W_R \subseteq \mathbb{C}$ be the disk of radius $R$ centered at the origin, then $\partial W_R = \lbrace z \| z | = R \rbrace$, take large enough $R$ then $f_t$ will not attain zero on that circle, as $z^7$ out pace the other two terms a lot. Thus we may consider the map $\frac{f_t(z)}{| f_t(z) |}: \partial W_R \to S^1$ because the denominator is never $0$. It is a homotopy between $\frac{f_0(z)}{| f_0(z) |} =\frac{z^7}{R^7}$ and $\frac{f_1(z)}{| f_1(z) |} = \frac{f(z)}{| f(z) |}$. So that $\deg_2{\frac{f(z)}{| f(z) |}} = \deg_2{\frac{z^7}{R^7}}$ mod $2$.

    Now $\deg_2{\frac{z^7}{R^7}} = 7$, thus $\deg_2{\frac{f(z)}{| f(z) |}} = 1$ mod $2$, by the proposition we had in the class this means $\frac{f(z)}{| f(z) |}$ does not extend to $W_R$, and thus $| f(z) | = 0 = f(z)$ in $W_R$.

    ### Exercise 7

    **Prove that $S^1$ is not simply connected**.

    Proof

    Consider the identity map $\text{id}: S^1 \to S^1$, $S^1$ is connected and is compact, and that $\deg_2{\text{id}} = \# \text{id}^{-1}(q)$ mod $2 = 1$. On the other hand, for a constant map $c: S^1 \to S^1$, by assumption it is not surjective thus $\deg_2{c} = 0$. Since $0 \ne 1$, the identity and constant maps are not homotopic, thus $S^1$ is not simply connected.

    ### Exercise 10

    **Prove that $S^2$ and the torus are not diffeomorphic**.

    Proof

    Proved in earlier homework that $S^2$ is simply connected, if the torus is not simply connected we are done.

    Consider the composition: $\text{id}: S^1 \xrightarrow{i} T^2 \to^p S^1$ where $i(x) = (x,y_0) \in S^1 \times S^1 =T^2$ and $p(x,y) = x$ for some $y_0 \in S^1$. If $i$ is homotopic to a constant map then so does $\text{id} = p \circ i$, which cannot be true.

    ### Exercise 11

    **Suppose that $f: X \to Y$ has $\deg_2{f} \ne 0$, prove that $f$ is onto**.

    Proof

    If $f$ is not onto, by definition there exists $q \in Y$ such that $f^{-1}(q)$ is empty, thus it must be a regular value of $f$. By assumption $\# f^{-1}(q) = 0$, which is exactly the definition of $\deg_2{f}$. This is the contra-positive of the desired statement.

    ### Exercise 12

    **If $Y$ is not compact, then $\deg_2{f} = 0$ for all maps $f:X \to Y$ ($X$ compact)**.

    Proof

    If $X$ is compact, then $f(X)$ (assuming being smooth) is compact, thus $f(X) \ne Y$, by the same argument as above, $f$ is not surjective thus $\deg_2{f}$ is $0$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 10""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 3.2

    ### Exercise 2

    **Let $\beta = \lbrace v_1, \dots, v_k \rbrace$ be an ordered basis for $V$. Show that**:

    1. **replacing one $v_i$ by a multiple $cv_i$ yields an equivalently oriented ordered basis if $c > 0$, an oppositely oriented one if $c < 0$**;
    2. **transposing two elements (i.e. interchanging the places of $v_i$ and $v_j$, $i \ne j$) yields an oppositely oriented ordered basis**;
    3. **subtracting from one $v_i$ a linear combination of the other yields an equivalently oriented ordered basis**.

    Proof

    1. Consider the transformation between $\beta$ and the basis described in the question, the transformation can be given by the matrix with form $M = \begin{pmatrix} 1&0&0&0&0&0\\&&\dots\\0&0&c&0&0&0\\0&0&0&1&0&0\\&&\dots\\0&0&0&0&0&1 \end{pmatrix}$, i.e. the diagonal goes $(1, \dots, 1, c, 1,\dots, 1)$, all $1$ but $i$ th position with $c$, and non-diagonal positions all $0$. To calculate the determinant of this matrix we simple take product of the diagonal and the result is $c$. Thus by definition, this resulting basis is equivalently oriented if $c = \det{M} > 0$, and oppositely oriented if $c = \det{M} < 0$;
    2. Similarly, the transformation between such two bases may be given by a matrix with the form $M = \begin{pmatrix} 1&0&0&0&0&0\\&&\dots\\0&0&0&1&0&0\\0&0&1&0&0&0\\&&\dots\\0&0&0&0&0&1 \end{pmatrix}$. I.e. it is $E$ but the $i$-th row's $1$ goes to $j$ th position, and the $j$ th row's $1$ goes to $i$ th position. This matrix yield $\det{M} = -1$, and thus results an oppositely oriented basis;
    3. Similarly, the transformation between such two bases may be given by a matrix with the form $M = \begin{pmatrix} 1&-x_2&-x_3&\dots&-x_{n-1}&-x_n\\&&\dots\\0&0&1&0&0&0\\0&0&0&1&0&0\\&&\dots\\0&0&0&0&0&1 \end{pmatrix}$ where we subtract $x_2v_2 + x_3v_3 + \dots + x_nv_n$ from $v_1$: but this matrix is an upper triangle matrix and the determinant of this transformation is simply the product of terms on the diagonal $= 1>0$ and it is orientation preserving.

    ### Exercise 6

    $\mathbb{R}^k_+$ **is oriented by the standard orientation of $\mathbb{R}^k$, thus $\partial \mathbb{R}^k_+$ acquires a boundary orientation, but $\partial \mathbb{R}^k_+$ may be identified with $\mathbb{R}^{k-1}$. Show that the boundary orientation agrees with the standard orientation of $\mathbb{R}^{k-1}$ if and only if $k$ is even. Symbolically, we may express it as $\partial \mathbb{R}^k_+ = (-1)^k\mathbb{R}^{k-1}$**.

    Proof

    Let us use the standard basis for $\mathbb{R}^k$, i.e. $\lbrace e_i \rbrace_{i = 1,\dots,k}$.

    At every point $x \in \mathbb{R}^k_+$ there is a unit vector (basis element) in $T_x\mathbb{R}^k_+$ perpendicular to $T_x\partial \mathbb{R}^k_+$ pointing outwards, and it is exactly $-e_k$ = $(0,\dots,0,-1)$ (denoted $n_x$ in the book).

    Now $\lbrace e_i \rbrace_{i = 1,\dots,k-1}$ forms a basis for $T_x\partial \mathbb{R}^k_+$ and the (boundary) orientation is determined by the sign of the ordered basis $\lbrace -e_k, e_1, e_2, \dots, e_{k-1} \rbrace$.

    The transformation between this basis and the standard basis consists of $k-1$ permutations (move $-e_k$ to the right, one step at a time), and one multiplication (turn $-e_k$ to $e_k$). In total there are $k$ steps, each step changes the sign of basis, so if $k$ is even the orientation is preserved and if $k$ is odd the orientation is reversed, that is exactly the desired statement.

    ## Section 3.3

    ### Exercise 2

    1. **Compute the degree of the antipodal map $S^k \to S^k, x\to -x$**;
    2. **Prove that the antipodal map is homotopic to the identity if and only if $k$ is odd**;
    3. **Prove that there exists a non-vanishing vector field in $S^k$ if and only if $k$ is odd**;
    4. **Could mod $2$ theory prove part 2 and 3**?

    Solution

    1. The transformation between bases may be given by a diagonal matrix with all $-1$ on the diagonal, each $-1$ gives 'reversing' for the orientation and thus the degree of the map is $(-1)^{k+1}$, in particular, $1$ if $k$ is odd and $-1$ if $k$ is even;
    2. The identity map clearly has degree $1$, but by above, if $k$ is even the antipodal map has degree $-1$, thus cannot be homotopic to the identity map; we proved before that if $k$ is odd then we the antipodal map is homotopic to the identity, combine the two results and we have the 'if and only if' statement;
    3. Similarly, we use the results from previous homework:
    	1. If $k$ is odd then there exists a non-vanishing vector field;
    	2. If $k$ is even, by above, the antipodal map is NOT homotopic to the identity, thus there does not exists a non-vanishing vector field in $S^k$.
	
    	Combine the two statements and we have the 'if and only if' statement;
    4. Not really, because in part 2 if $k$ is even then the degree $2$ mod is $1$ (while degree is $-1$, where in fact we want this number not equal to $1$). Since part 2 fails, we cannot use this argument to proceed to part 3.

    ### Exercise 7

    **Prove that the map $S^1 \to S^1$ defined by $z \to \overline{z}^m$ has degree $-m$**.

    Proof

    This map is the composition of a reflection (with degree $-1$) following a rise to power $m$ (with degree $m$), thus has degree $-m$ (we are using the result below).

    ### Exercise 10

    **Suppose that $X \xrightarrow{f} Y \xrightarrow{g} Z$ are given, and prove that $\deg{g \circ f} = \deg{f} \cdot \deg{g}$**.

    Proof

    Say $z$ is a regular for $g \circ f$, we need to calculate the signed sum of $x \in (g \circ f)^{-1}(z)$. Rewrite this set of preimage of $z$ as $\lbrace x \in X | f(x) = y$ where $g(y) = z \rbrace$, so that $\deg{g \circ f}$ $= \sum\limits_{x \in (g \circ f)^{-1}(z)} \varepsilon_{g \circ f}(x)$ $= \sum\limits_{y \in g^{-1}(z)}(\sum\limits_{x \in f^{-1}(y)} \varepsilon_{g \circ f}(x))$.

    Now for any fixed $y$, the property that $dg_y$ is whether orientation preserving or reversing is fixed, thus we may continue write the above equation $= \sum\limits_{y \in g^{-1}(z)} (\varepsilon_g(y)\sum\limits_{x \in f^{-1}(y)}\varepsilon_f(x))$ and we can split the sum as $= (\sum\limits_{y \in g^{-1}(z)}\varepsilon_g(y))(\sum\limits_{x \in f^{-1}(y)}\varepsilon_f(x))$ and it is exactly $\deg{g}\cdot\deg{f}$.

    Let $r \in Z$ be a regular value for $g \circ f: X \to Y \to Z$ and let $p \in (g\circ f)^{-1}(r)$, then $d(g\circ f)_p$ is an isomorphism and so do $df_p$ and $dg_{f(p)}$ because $d(g\circ f)_p = dg_{f(p)} \circ df_p$. Thus $r = g(f(p))$ is a regular value for $g$ and any $q$ such that $g(q) = r$ are regular values for $f$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 11""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 4.2

    ### Exercise 1

    **Suppose that $T \in \wedge^p(V^{*})$ and $v_1,\dots, v_p \in V$ are linearly dependent, prove that $T(v_1,\dots,v_p) = 0$**.

    Proof

    By assumption of linear dependency we have some $a^1,\dots, a^p \ne 0$ such that $a^iv_i = 0$, so that, for example, we can write that $v_1 = (a^2v_2 + \dots + a^pv_p)/a^1$, then we have $T(v_1,\dots,v_p) = T((a^2v_2 + \dots + a^pv_p)/a^1, v_2,\dots, v_p)$, since $T$ is essentially a multi ($q$)-linear function, we can 'split' $T$ on the first variable to get $= \frac{a^2}{a^1}T(v_2,v_2,\dots,v_p) + \dots + \frac{a^p}{a^1}T(v_p,v_2,\dots,v_p)$, but then each term would be $0$ (because from the definition of alternating $(0,q)$-tensor, $T(v_2,v_2,\dots,v_p) = -T(v_2,v_2,\dots,v_p)$ so it must be zero), thus we have the desired statement.

    ### Exercise 2

    **Dually, suppose that $\varphi_1, \dots, \varphi_p \in V^{*}$ are linearly dependent, prove that $\varphi_1 \wedge \dots \wedge \varphi_p = 0$**.

    Proof

    Again, we have some $a^1,\dots, a^p \ne 0$ such that $a^i\varphi_i = 0$, so that we can write that $\varphi_1 = (a^2\varphi_2 + \dots + a^p\varphi_p)/a^1$, then we have $\varphi_1 \wedge \dots \wedge \varphi_p$ $= ((a^2\varphi_2 + \dots + a^p\varphi_p)/a^1) \wedge \varphi_2 \wedge \dots \wedge \varphi_p$, we can just do distribution here to split it to $= \frac{a^2}{a^1}\varphi_2 \wedge \varphi_2 \wedge \dots \wedge \varphi_p + \dots + \frac{a^p}{a^1}\varphi_p \wedge \varphi_2 \wedge \dots \wedge \varphi_p$, then each term is again $0$ thus we have the desired statement.

    ### Exercise 6

    1. **Let $T$ be a non-zero element of $\wedge^k(V^{*})$, where $\dim{V} = k$, prove that two ordered bases $\lbrace v_1,\dots,v_k \rbrace$ and $\lbrace v_{1'}, \dots, v_{k'} \rbrace$ for $V$ are equivalently oriented if and only if $T(v_1,\dots,v_k)$ and $T(v_{1'}, \dots, v_{k'})$ have the same sign**;
    2. **Suppose that $V$ is oriented, show that the one-dimensional vector space $\wedge^k(V^{*})$ acquires a natural orientation by defining the sign of a non-zero element $T \in\wedge^k(V^{*})$ to be the sign of $T(v_1,\dots,v_k)$ for any positively oriented ordered basis $\lbrace v_1,\dots,v_k \rbrace$ for $V$**;
    3. **Conversely, show that an orientation of $\wedge^k(V^{*})$ naturally defines an orientation on $V$ by reversing the above**.

    Proof

    1. Say $A$ is the linear operator that transform $\lbrace v_1,\dots,v_k \rbrace$ to $\lbrace v_{1'}, \dots, v_{k'} \rbrace$ (so that $A$ is from $V$ to $V$, and induces the linear operator $A^{*}$), the two basis are equivalently oriented if and only if $\det{A}$ is positive. By the Determinant Theorem we have $T(v_{1'}, \dots, v_{k'})$ $=T(A(v_{1}, \dots, v_{k}))$ $= A^{*}T(v_{1}, \dots, v_{k})$ $= \det{A} T(v_{1}, \dots, v_{k})$, so they have the same sign;
    2. Say $A$ is a linear operator $V \to V$ between $v_1,\dots,v_k$ to an equivalently oriented basis $v_{1'}, \dots, v_{k'}$, then $T(v_{1'},\dots, v_{k'})$ $= \det{A}T(v_1,\dots,v_k)$, but since both basis are equivalently oriented, $\det{A}$ must be positive, meaning that the sign of $T(v_{1},\dots, v_{k})$ is independent from the choice of (same oriented) basis.
    	Also that in case that the two bases are reversely oriented, it happens if and only if $\det{A}$ is negative, if and only if $T(v_{1},\dots, v_{k})$ and $T(v_{1'},\dots, v_{k'})$ have different signs. Thus we indeed have two different orientations;
    3. Define an equivalence relation as follow: two basis on $V$, $v_1,\dots,v_k$ and $v_{1'},\dots,v_{k'}$, are equivalently oriented if $T(v_1,\dots,v_k)$ and $T(v_{1'},\dots,v_{k'})$ have the same sign. This naturally gives two possible classes.
    	Since $T(v_1,\dots,v_k)$ and $T(v_{1'},\dots,v_{k'})$ have the same sign if and only if $\det{A}$ of the linear operator is positive, we can say $v_{1},\dots,v_{k}$ and $v_{1'},\dots,v_{k'}$ are equivalently oriented if and only if $\det{A}$ is positive, but such an $A$ is unique because it is a transformation between bases, and $\det{A}$ is either positive or negative, but not both, so that any two basis cannot be both equivalently and reversely oriented.
    	Now, call $v_1,\dots,v_k$ positive if $T(v_1,\dots,v_k)$ positive, and the definition is well-define.


    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 12""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 4.4

    ### Exercise 1

    **Let $Z$ be a finite set of points in $X$, considered as a $0$-manifold. Fix an orientation of $Z$, an assignment of orientation numbers $\sigma(z) = \pm 1$ to each $z \in Z$. Let $f$ be any function on $X$, considered as a $0$-form, and check that $\int_Z f = \sum\limits_{z \in Z} \sigma(z)\cdot f(z)$**.

    Solution

    I think this comes purely from definition: since $f$ is a (real-valued) function, the integral on each single point will be $f(x)$ or $-f(x)$ given the point is positively or negatively oriented, so integral on a finite set of points will be the sum of them, i.e. $\sum\limits_{z \in Z} \sigma(z)\cdot f(z)$.

    ### Exercise 3

    **Let $c:[a,b] \to X$ be a smooth curve, and let $c(a) = p$, $c(b) = q$, show that if $w$ is the differential of a function on $X$, $w = df$, then $\int_a^b c^{*} w = f(q) - f(p)$**.

    Proof

    $LHS= \int_a^b c^{*} w$ $= \int_{[a,b]}c^{*}w$ (nothing happens this step, just another way to write)

    $= \int_X w$ (this is from the change of variable, we 'undo' the pull-back)

    $= \int_X df$, and this is exactly $f(q) - f(p)$, assuming the 'end points' of the curve of $X$ are $p$ and $q$.

    ### Exercise 4

    **Let $c:[a,b] \to X$ be a smooth curve, and let $f:[a_1,b_1] \to [a,b]$ be a smooth map with $f(a_1) = a$, $f(b_1) = b$, show that the integrals $\int_a^b c^{*}w$ and $\int_{a_1}^{b_1}(c\circ f)^{*} w$ are the same**.

    Proof

    From the assumption we can use $f$ (it is smooth) to get a pull back $f^{*}\cdot$ from $[a,b]$ to $[a_1, b_1]$, so we have $\int_a^b c^{*}w$ $= \int_{a_1}^{b_1}f^{*}c^{*}w$ (we also used the fact that $f$ is orientation preserving here, because from assumption the order of $a,b$ do not change…) $=\int_{a_1}^{b_1}(c \circ f)^{*}w$. We used the fact that $(f \circ g)^{*}(\omega) = g^{*}(f^{*}(\omega))$ here.

    ### Exercise 8

    **Define a $1$-form $w$ on the punctured plane $\mathbb{R}^2 - \lbrace 0 \rbrace$ by $w(x,y) = \frac{-ydx}{x^2+y^2} + \frac{xdy}{x^2+y^2}$**.

    1. **Calculate $\int_Cw$ for any circle $C$ of radius $r$ around the origin**;
    2. **Prove that in the half plane $\lbrace x > 0 \rbrace$, $w$ is the differential of a function**;
    3. **Why isn't $w$ the differential of a function globally on $\mathbb{R}^2 - \lbrace 0 \rbrace$**?

    Solution

    1. Let us use the standard way to parameterize a circle: let $\gamma:[0,2\pi] \to C, t \to (r\cos(t), r\sin(t))$, then we can write $\int_Cw =\int_0^{2\pi}\gamma^{*}w$ $= \int_0^{2\pi}(\frac{-y}{x^2+y^2}x'(t) + \frac{x}{x^2+y^2}y'(t))dt$, now we can replace every $x, y$ with $r\cos(t)$ and $r\sin(t)$, and do the calculation: $= \int_0^{2\pi}(\frac{r^2(\sin^2(t) + \cos^2(t))}{r^2(\cos^2(t) + \sin^2(t))})dt$, so everything in the fraction got canceled out, and the result is $2\pi$;
    2. Let us just try the hint, and use the formula $\arctan'{x} = \frac{1}{x^2+1}$:
    	1. $\frac{\partial}{\partial x}\arctan{y/x}$ $= \frac{-\frac{y}{x^2}}{1+\frac{y^2}{x^2}} = \frac{-y}{x^2+y^2}$, and;
    	2. $\frac{\partial}{\partial y}\arctan{y/x}$ $= \frac{1/x}{1 + \frac{y^2}{x^2}} = \frac{x}{x^2+y^2}$.

    	And turns out they coincides with $w$, and thus $w$ is the differential of $\arctan$;
    3. Because $\arctan{y/x}$ is not continuous (not even defined) on the y-axis, i.e. $x= 0$.

    ## Section 4.5

    ### Exercise 1

    **Calculate the exterior derivatives of the following forms in $\mathbb{R}^3$**:

    1. $w = z^2dx \wedge dy + (z^2+2y)dx \wedge dz$;
    2. $w = 13xdx + y^2dy + xyzdz$;
    3. $w = fdg$, where $f$ and $g$ are functions;
    4. $w = (x+2y^3)(dz \wedge dx + \frac{1}{2}dy \wedge dx)$.

    Solution

    1. $dw = \frac{\partial z^2}{\partial z}dz\wedge dx \wedge dy + \frac{\partial z^2+2y}{\partial y}dy\wedge dx \wedge dz$ $=(2z-2)dx \wedge dy \wedge dz$ (two flips in the first term, one in the second);
    2. $dw = (13 dx)\wedge dx + (2y dy) \wedge dy + (yz dx + xz dy + xy dz)\wedge dz$ $=yz dx \wedge dz + xz dy \wedge dz$;
    3. $dw = d(fdg) = dfdg+fddg$ by the product rule, and we know $ddg = 0$, so $dw = dfdg$;
    4. $dw = 6y^2 dy \wedge dz \wedge dx = 6y^2 dx \wedge dy \wedge dz$.

    ### Exercise 2

    **Show that the vector field $(\frac{-y}{x^2+y^2}, \frac{x}{x^2+y^2})$ has curl zero, but that it cannot be written as the gradient of any functions**.

    Proof

    Since curl is defined in $\mathbb{R}^3$ we need to pad a $0$ to the field, i.e. let $F = (\frac{-y}{x^2+y^2}, \frac{x}{x^2+y^2}, 0)$, then $curl{F}$ is defined to be $\det{\begin{pmatrix} i&j&k\\ \frac{\partial}{\partial x}& \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ \frac{-y}{x^2+y^2} & \frac{x}{x^2+y^2} & 0\end{pmatrix}}$, we don't really have $z$ here and the calculation is kind of simple, we have it $= (0,0,\frac{y^2-x^2}{(x^2+y^2)^2} - \frac{y^2-x^2}{(x^2+y^2)^2})$ and it is exactly the zero vector.

    It cannot be written as the gradient of some function because the vector field is not conservative, which comes from above exercise 4.4.8 part 1, its integral is path-dependent: we integrated it along a closed curve, but the result is not $0$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 13""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 4.7

    ### Exercise 6

    **The Divergence Theorem is also useful in electrostatics, let $D$ be a compact region in $\mathbb{R}^3$ with a smooth boundary $S$. Assume $0 \in \text{int}(D)$. If an electric charge of magnitude $q$ is places at $0$, the resulting force field is $q\vec{r}/r^3$, where $\vec{r}(x)$ is the vector to a point $x$ from $0$ and $r(x)$ is its magnitude. Show that the amount of charge $q$ can be determined from the force on the boundary by proving Gauss's Law: $\int_S \vec{F}\cdot \vec{n}dA = 4\pi q$**.

    Proof

    First let us write down the full statement of the Divergence Theorem and check whether can we apply it:

    Suppose $V$ is a subset of $\mathbb{R}^n$ which is compact and has a piece-wise smooth boundary $S$. If $\vec{F}$ is a continuously differentiable vector field defined on a neighborhood of $V$, then $\int\int\int_Vdiv{\vec{F}}dV = \int\int_S\vec{F}\cdot \vec{n}dS$.

    By assumption we have $\vec{F} = q\vec{r}/r^3$ $=(\frac{q}{(x^2+y^2+z^2)^{3/2}}x,\frac{q}{(x^2+y^2+z^2)^{3/2}}y, \frac{q}{(x^2+y^2+z^2)^{3/2}}z)$, thus we have a problem at $0$, the vector field is not differentiable there, we need to take $0$ out.

    Consider a small enough open ball $B(0,c) \subseteq \text{int}(D)$ (existence is by the assumption $0 \in int{D}$), let us denote its boundary, the sphere, $S^2_{c}$. By assumption $D$ is a compact domain, the boundary is (piece-wise) smooth. Now if we take $B = B(0,c)$ out, the remaining $D - B$ is still a compact domain, and its boundary is $S \cup S^2_{c}$ is still (piece-wise) smooth. Also now $\vec{F}$ is continuously differentiable in a neighborhood of $D-B$ (the only trouble we may have was $0$ and we took it out), thus we can apply the Divergence Theorem ($S$ and $S^2_{c}$ are reversely oriented):

    $\int\int_{S-S^2_c} \vec{F}\cdot \vec{n}dA$ $=\int\int\int_{D -B}div{\vec{F}}dxdydz$.

    Let us calculate $div{\vec{F}} = q\frac{(-2x^2+y^2+z^2)+(-2y^2+x^2+z^2)+(-2z^2+x^2+y^2)}{(x^2+y^2+z^2)^{5/2}}$ thus it is constant zero, in other words $\int\int\int_{D -B}div{\vec{F}}dxdydz = 0$, and thus $\int\int_{S} \vec{F}\cdot \vec{n}dA = \int\int_{S^2_c} \vec{F}\cdot \vec{n}dA$.

    So we reduce the problem on some arbitrary domain to a problem on a sphere, where we simply have $\vec{n} = \vec{r}/r = \vec{c}/c$ since the radius is $c$. Similarly $\vec{F} = q\vec{c}/c^3$ thus $\vec{F} \cdot \vec{n} = q/c^2$ (a constant) on $S^2_c$, and we have $\int\int_{S^2_c} \vec{F}\cdot \vec{n}dA$ $= \int\int_{S^2_c}q/c^2dA$, now use the formula for sphere surface area, $= (q/c^2) \pi c^2 4 = 4\pi q$ as desired.

    ### Exercise 8

    **Suppose that $X = \partial W$, $W$ is compact and $f:X \to Y$ is a smooth map. Let $w$ be a closed $k$-form on $Y$, where $k = \dim{X}$, prove that if $f$ extends to all of $W$, then $\int_Xf^{*}w = 0$**.

    Proof

    First a definition from section 4.6 in the book: a $p$-form $w$ on $X$ is closed if (and only if) $dw = 0$.

    Now, by assumption $W$ is an $k+1$ manifold, so we can apply Stokes' Theorem to get $\int_Xf^{*}w = \int_{\partial W}f^{*}w$ (nothing happens this step) $= \int_{W}d(f^{*}w)$ (apply the theorem) $= \int_Wf^{*}(dw)$ (by properties of the exterior derivative), and by the definition of a closed differential form it equals $0$ as desires.

    ### Exercise 9

    **Suppose that $f_0,f_1 : X\to Y$ are homotopic maps and that the compact, boundary-less manifold $X$ has dimension $k$, prove that for all closed $k$-forms $w$ on $Y$, $\int_Xf_0^{*}w = \int_Xf_1^{*}w$**.

    Proof

    Say the homotopy is given by $F:X \times [0,1] \to Y$, we know from previous materials that $X \times [0,1]$ is a $k$-manifold with boundary $X \times \lbrace 0,1 \rbrace$. By assumption (restriction of) $F$ is smooth on $X \times \lbrace 0,1 \rbrace$ and is defined on $X \times [0,1]$. Also that $w$ is closed by assumption, we can thus use the previous exercise to get that $\int_{X \times \lbrace 0,1 \rbrace}F^{*}w = 0$.

    While on the other hand, we can write $\int_{X \times \lbrace 0,1 \rbrace}F^{*}w$ (the two parts have different orientations) $= \int_{-X \times \lbrace 0 \rbrace}F^{*}w + \int_{X \times \lbrace 1 \rbrace}F^{*}w$ $= - \int_{X \times \lbrace 0 \rbrace}F^{*}w + \int_{X \times \lbrace 1 \rbrace}F^{*}w$, now by assumption of the homotopy we have, $F$ restricted on $X \times \lbrace 0 \rbrace$ is simply $f_0$ and $X \times \lbrace 0 \rbrace$ is just the same as $X$ (respectively, $1$). So we can write $= -\int_Xf^{*}_0w + \int_Xf^{*}_1w$. Recall that it equals $0$, thus we have that $\int_Xf^{*}_0w = \int_Xf^{*}_1w$ as desired.

    ### Exercise 10

    **Show that if $X$ is a simply connected manifold, then $\oint_{\gamma}w = 0$ for all closed $1$-forms $w$ on $X$ and all closed curves $\gamma$ in $X$**.

    Proof

    By definition of simply connected manifold, let $r:S^1 \to X$ be (the) smooth map with image $\gamma$, it is homotopic to some constant map $c: S^1 \to X, x \mapsto c$.

    Now $S^1$ is a compact, boundary-less manifold with dimension $1$, since $w$ is a closed $1$-form, we can apply exercise 9 to get $\oint_{\gamma}w =\int_{S^1}r^{*}w = \int_{S^1}c^{*}w$ (first equality by change of variable).

    Now consider $D(0,1)$, it has $S^1$ as its boundary, $D(0,1)$ is closed and bounded thus compact, $c$ is a smooth (constant) map on $S^1$, and it can be easily extended to $D(0,1)$, still maps everything to $c$. Then for closed $1$-form $w$, by exercise 8 we have that $\int_{S^1}c^{*}w = 0$, and thus we have the desired statement.

    """
    )
    return


if __name__ == "__main__":
    app.run()
