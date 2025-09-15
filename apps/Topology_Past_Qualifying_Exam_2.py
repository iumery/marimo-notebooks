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
    mo.md(r"""# Exam 7""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $A$ be a subset of a topological space $X$, prove that $A$ is open in $X$ if and only if every point in $A$ has a neighborhood contained in $A$**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $f: X\to Y$ be a continuous bijective map from a compact topological space $X$ to a Hausdorff topological space $Y$, show that $f$ is a homeomorphism**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Prove that every compact Hausdorff space $X$ is regular**.

    Idea:

    Say $A \subseteq X$ is closed and $x$ is a point in $X - A$, we need to separate them: since $A$ is closed in compact set, it is compact. Now for each point $a$ in $A$ assign it with $U(a)$ such that $U(a)$ is disjoint with some $U_a(x)$, neighborhood of $x$ (we can do that because $X$ is Hausdorff), now the collection $\lbrace U(a) \rbrace$ (more precisely it is $U(a) \cap A$, but it is not important here) for an open covering for $A$ thus admit a finite covering. Now $\bigcup\limits^N U(a)$ and $\bigcap\limits^N U_a(x)$ are disjoint open sets containing $A$ and $x$ respectively.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $(X,d)$ be a metric space, $A \subseteq X$ and $x \in X$, prove that the point $x$ is in the closure of $A$ if and only if there is a sequence of points $x_n \in A$ that converges to $x$**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 5""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $S^m \subseteq \mathbb{R}^{m+1}$ be the unit sphere, prove if $m$ is odd, then the antipodal map $\alpha: S^m \to S^m$ is homotopic to the identity map. Is the same true if $m$ is even**?"""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 6""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $H \subseteq \mathbb{R}^3$ be the hyperboloid defined by $x^2+y^2-z^2 = 1$, for $a > 0$, let $S_a \subseteq \mathbb{R}^3$ be the sphere $(x-2)^2+y^2+z^2 = a$, for what values of $a$ does $S_a$ intersect $H$ transversally? For each value of $a$ where $S_a$ and $H$ do not intersect transversally, what does the intersection look like**?

    Idea:

    Normal vectors are $(2x,2y,-2z)$ and $(2(x-2),2y,2z)$ respectively, and:

    1. If $0<a<1$ then there is no real solution, i.e. no intersection;
    2. If $a = 1$ then the two object intersect at one point, namely $(1,0,0)$, calculate the normal vectors and easy to see they do not intersect transversally;
    3. If $a = 9$ then the two object intersect… at an object like the shape $8$, and they intersect transversally except for the point $(-1,0,0)$;
    4. Otherwise they intersect transversally.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 7""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $f: X\to Y$ be a smooth map of compact smooth manifolds, show that the map $F:X\to X\times Y$ given by $F(x) = (x,f(x))$ is an embedding**.

    Idea:

    We need to show $F$ is an immersion, injective and proper.

    1. For any $p$, $dF_p = (1,df_p)$ is never zero so it is injective, i.e. $F$ immersion;
    2. If $(x_1,f(x_1)) = (x_2,f(x_2))$ then automatically $x_1 = x_2$ thus $F$ injective;
    3. $F$ is a continuous map from compact $X$ to Hausdorff $X \times Y$ thus it is proper.

    By the way, actually we do not need to require $X,Y$ to be compact: consider any open set in $X \times Y$, since we have the product topology open set are of the form $U\times V$ where $U$ open in $X$ and $V$ open in $Y$, and the preimage is just $U$ by the construction, now if $U\times V$ is compact, then it is closed and bounded, so $U$ is closed, because it is preimage of closed set under continuous $F$, $U$ is bounded because $U \times V$ is bounded.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 8""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Show that the $1$-form $w = (\frac{-y}{x^2+y^2})dx+(\frac{x}{x^2+y^2})dy$ on $\mathbb{R}^2-\lbrace 0 \rbrace$ is closed but not exact**.

    Idea:

    1. To calculate the curl, rise $F$ to $F(x,y,z) = (\frac{-y}{x^2+y^2},\frac{x}{x^2+y^2})$ and calculate $\det{\begin{pmatrix} i&j&k\\ \frac{\partial}{\partial x}& \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ \frac{-y}{x^2+y^2} & \frac{x}{x^2+y^2} & 0\end{pmatrix}}$, we don't really have $z$ here and the calculation is kind of simple, we have it $= (0,0,\frac{y^2-x^2}{(x^2+y^2)^2} - \frac{y^2-x^2}{(x^2+y^2)^2}) = (0,0,0)$ i.e. $F$ has zero curl;
    2. Notice that if we take a $1$-form $w = \frac{-y}{x^2+y^2}dx +\frac{x}{x^2+y^2}dy$ and evaluate it around a circle $C$ centered at $0$ then we have: parameterize the circle with $\gamma:[0,2\pi] \to C, t \to (r\cos(t), r\sin(t))$, then we can write $\int_Cw =\int_0^{2\pi}\gamma^{*}w$ $= \int_0^{2\pi}(\frac{-y}{x^2+y^2}x'(t) + \frac{x}{x^2+y^2}y'(t))dt$, now we can replace every $x, y$ with $r\cos(t)$ and $r\sin(t)$, and do the calculation: $= \int_0^{2\pi}(\frac{r^2(\sin^2(t) + \cos^2(t))}{r^2(\cos^2(t) + \sin^2(t))})dt$, so everything in the fraction got canceled out, and the result is $2\pi \ne 0$, meaning that the vector field is not conservative, and gradient theorem told us if the vector field is not conservative it cannot be gradient of our desired function.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Exam 8""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $(X,d)$ be a metric space, $A \subseteq X$ and $x \in X$, prove that a point $x$ is in the closure of $A$ if and only if there is a sequence $x_n \in A$ which converges to $x$**.

    Idea:

    If $x$ is in the closure, by definition, $B(x,1), B(x,1/2), B(x,1/3), \dots$ all intersect with $A$, pick a point in each $B(x,1/n)\cap A$ and name it $x_n$, we have a sequence $x_n \in A$ converges to $x$.

    Conversely, for any neighborhood $U$ of $x$, by definition of a convergent sequence, there are infinitely many $x_n \in U$, i.e. $U \cap A \ne \varnothing$, so $x \in \overline{A}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Prove that every continuous map $f:[0,1] \to [0,1]$ has a fixed point, is the same true for continuous maps $(0,1)\to (0,1)$**?

    Idea:

    $f$ needs to map $\lbrace 0,1 \rbrace$ to somewhere, if $f(0) = 0$ or $f(1) = 1$ we are done, otherwise we have $f(0)>0$ and $f(1) < 1$. If we define $g(x) = f(x) - x$, then $g(0)>0$ and $g(1)<0$, by IVT we have some $c$ such that $g(c) = 0$, which means $f(c) - c = 0$.

    No, just use something like $x \mapsto x/2$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $\mathbb{R}_l$ be the real line with the lower limit topology**.

    1. **Determine the path components of $\mathbb{R}_l$**;
    2. **Describe all continuous functions $f:\mathbb{R} \to \mathbb{R}_l$**.

    Idea:

    1. For any $a<b \in \mathbb{R}_l$ we can separate them with $(-\infty,a) \cup [b,\infty)$ (it does not work in the standard topology because we need the two set span the space), so $a,b$ are not even in same connected components, so cannot in path components, i.e. path components are single points;
    2. Following from above, remember that $\mathbb{R}$ is connected, so image under continuous function need to be connected, i.e. $f(\mathbb{R})$ must be connected, so must be a single point, i.e. continuous functions are constant functions.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $f: X\to Y$ be a continuous bijection of a compact space $X$ to a Hausdorff space $Y$, show that $f$ is a homeomorphism**.

    Idea:

    Closed in $X$ implies compact in $X$ implies image is compact implies image is close.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 5""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **For which values of $a$ does the hyperboloid $x^2+y^2-z^2 = 1$ intersect the sphere $x^2+y^2+z^2 = a$ transversally**?

    Idea:

    1. If $a<1$ then there is no real solution for $z$, so no intersection, vacuously transversal;
    2. If $a =1$ then $z = 0$, the normal vector of the two objects at the intersection(s) coincidence, so they do not span $\mathbb{R}^3$ and not intersect transversally;
    3. If $a>1$ then $z \ne 0$, intersect transversally.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 6""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **The orthogonal group $O(n)$ consists of all $n \times n$ matrices $A$ such that $AA^t = E$**.

    1. **Evaluate the tangent space to $O(n)$ at $E \in O(n)$**;
    2. **Prove that $O(n)$ is compact**.

    Idea:

    It is compact because it is closed (preimage of $E$ under $A \to AA^t$) and bounded (Euclidean norm is always $\sqrt{n}$).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 7""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $f:S^2 \to S^2$ be a smooth map**.

    1. **Can a point $q \in S^2$ have infinitely many pre-images**?
    2. **Prove that the set of points $q \in S^2$ with infinitely many pre-images has measure zero**;
    3. **Prove that, if $f$ is not surjective, it is homotopic to a constant map**.

    Idea:

    1. Sure, think about a constant map. But by Stack of Record Theorem, preimage of a regular point must be finite, i.e. such $q$ must be critical point;
    2. By Sard, critical point has measure zero;
    3. $f$ not surjective then degree is zero, constant map also has degree zero, by Hopf, they are homotopic.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 8""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Show that the vector field on $\mathbb{R}^2 - \lbrace 0 \rbrace$ given by $F(x,y) = (\frac{-y}{x^2+y^2},\frac{x}{x^2+y^2})$ has zero curl but cannot be written as the gradient of any smooth function $f:\mathbb{R}^2-\lbrace 0 \rbrace \to \mathbb{R}$**.

    Idea:

    1. To calculate the curl, rise $F$ to $F(x,y,z) = (\frac{-y}{x^2+y^2},\frac{x}{x^2+y^2})$ and calculate $\det{\begin{pmatrix} i&j&k\\ \frac{\partial}{\partial x}& \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ \frac{-y}{x^2+y^2} & \frac{x}{x^2+y^2} & 0\end{pmatrix}}$, we don't really have $z$ here and the calculation is kind of simple, we have it $= (0,0,\frac{y^2-x^2}{(x^2+y^2)^2} - \frac{y^2-x^2}{(x^2+y^2)^2}) = (0,0,0)$ i.e. $F$ has zero curl;
    2. Notice that if we take a $1$-form $w = \frac{-y}{x^2+y^2}dx +\frac{x}{x^2+y^2}dy$ and evaluate it around a circle $C$ centered at $0$ then we have: parameterize the circle with $\gamma:[0,2\pi] \to C, t \to (r\cos(t), r\sin(t))$, then we can write $\int_Cw =\int_0^{2\pi}\gamma^{*}w$ $= \int_0^{2\pi}(\frac{-y}{x^2+y^2}x'(t) + \frac{x}{x^2+y^2}y'(t))dt$, now we can replace every $x, y$ with $r\cos(t)$ and $r\sin(t)$, and do the calculation: $= \int_0^{2\pi}(\frac{r^2(\sin^2(t) + \cos^2(t))}{r^2(\cos^2(t) + \sin^2(t))})dt$, so everything in the fraction got canceled out, and the result is $2\pi \ne 0$, meaning that the vector field is not conservative, and gradient theorem told us if the vector field is not conservative it cannot be gradient of our desired function.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Exam 9""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $X$ be a topological space, prove that a subspace $A \subseteq X$ is dense if and only if its complement $X-A$ has empty interior**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 2""")
    return


@app.cell
def _(mo):
    mo.md(r"""**Prove that every continuous map $f:[0,1] \to [0,1]$ has a fixed point, is the same true for continuous maps $(0,1) \to (0,1)$**?""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 3""")
    return


@app.cell
def _(mo):
    mo.md(r"""**Prove that every compact Hausdorff space $X$ is regular**.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Recall that the metric space $\ell^2(\mathbb{R})$ consists of all sequences $x = \lbrace x_n \rbrace$ of real numbers such that $\sum x_n^2$ converges, with metric $d(x,y) = \sqrt{\sum (x_n-y_n)^2}$. Prove that the unit ball $B_1(0) \subseteq \ell^2(\mathbb{R})$ given by $\sum x_n^2 \le 1$ is not compact**.

    Idea:

    $B_1(0)$ is not compact because it is not sequentially compact (as per say, we are in a metric space):

    Consider the sequence $x_i = (0, \dots, 0, 1, 0, \dots)$, $1$ at the $i$-th position and all other $0$'s. Since $x_i$ is eventually zero, it indeed lies in $\ell^2(\mathbb{R})$. However this sequence does not have a convergent subsequence because calculate the distance between any such two sequences gives $d(x_i, x_j) = \sqrt{2}$ ($i \ne j$, of course).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 5""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $f:X\to Y$ be a diffeomorphism of smooth manifolds. Show that for every $x \in X$, the derivative $df_x: T_xX \to T_{f(x)}Y$ is an isomorphism**.

    Idea:

    Let $f^{-1}$ be the inverse map, then $\text{id} = f^{-1} \circ f$ and $\text{id} = f \circ f^{-1}$, they imply that $df^{-1}_{f(x)}\circ df_x = d(\text{id}) = \text{id}$ and $df_{f^{-1}(y)}\circ df^{-1}_y = d(\text{id}) = \text{id}$. Thus $df_x$ is linear, one-to-one and onto, thus an isomorphism.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 6""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Prove that the set $X$ of all non-zero $2 \times 2$ real matrices $A$ such that $AA^t$ is diagonal is a sub-manifold of $\mathbb{R}^4$, what is the dimension of $X$? Is $X$ compact**?

    Idea:

    Notice that such matrices need to have $ab+cd = 0$, so we prove that $X = f^{-1}(0)$ where $f:X\to \mathbb{R}, \begin{pmatrix} a&b\\c&d \end{pmatrix}\mapsto ab+cd$, $0$ is a regular value and we are done. The proof is actually easy, $df_M(h) = a' b+b' a+c' d+d' c$ where $M = \begin{pmatrix} a&b\\c&d \end{pmatrix}$ is in $X$ and $h = \begin{pmatrix} a'&b'\\c'&d' \end{pmatrix}$ is obviously surjective (i.e. it can map to any value in $\mathbb{R}$, because there is no limit on $h$). So it is a sub-manifold of dimension $3$. $X$ is not compact because it is not bounded: for example, any matrix with the form $\begin{pmatrix} a&0\\0&a \end{pmatrix}$ is in $X$ and $a$ can be arbitrarily large.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 7""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Prove that there is no non-vanishing vector field on $S^2$**.

    Idea:

    Because $2$ is even. The logical sequence is this: $2$ is even, implies antipodal map is not homotopic to identity (because the degree are different), implies there no non-vanishing vector field on it (because this is the negation of a statement we proved: if there is a non-vanishing vector field, antipodal map is homotopic to identity).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 8""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $S \subseteq \mathbb{R}^3$ be the paraboloid $z = x^2+y^2,x^2+y^2\le 1$, oriented by the upward normal vector, and $w = dx\wedge(dy+dz)$, evaluate $\int_Sw$**.

    Idea:

    Parameterize $S$ by $r(x,y) = (x,y,x^2+y^2)$, then $\int_S dx \wedge(dy + dz)$ $= \int\int_U dx \wedge(dy + 2xdx+2ydy)$ $= \int\int_U dx\wedge dy + 2y dx \wedge dy$ $= \int\int_U (1+2y) dxdy$ $= \int_0^{2\pi} \int_0^1 (1+2r\sin(\theta))rdrd\theta$ $=\int_0^{2\pi}(1/2 + 2/3\sin(\theta))d\theta = \pi$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Exam 10""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $f:X\to Y$ be a map of topological spaces, prove that $f$ is continuous if and only if for every $x \in X$ and every open neighborhood $V(f(x))\subseteq Y$, there exists an open neighborhood $U(x) \subseteq X$ such that $f(U(x)) \subseteq V(f(x))$**.

    Idea:

    If $f$ is continuous then it is easy, because preimage of open set is open, just choose that set as the $U$.

    Conversely, let $V$ be an arbitrary (non-empty) open set in $Y$ and let $x \in f^{-1}(V)$, then $f(x) \in V$, so by assumption there is some $U$ neighborhood of $x$ such that $f(U) \subseteq V$, so $U \subseteq f^{-1}(f(U)) \subseteq f^{-1}(V)$. Since this work for any $x$ in the preimage, we have that $f^{-1}(V)$ is open, result follows.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $(X,d)$ be a metric space, prove that**:

    1. **For any subset $A \subseteq X$, the formula $d_A(x) = \inf\lbrace d(x,a) | a \in A \rbrace$ defines a continuous function $d_A:X\to \mathbb{R}$**;
    2. $\overline{A} = \lbrace x \in X | d_A(x) = 0 \rbrace$.

    Idea:

    1. For any $x \in X$ and $V \ni d_A(x) \in \mathbb{R}$, there exists basis element $V \supseteq B_{\mathbb{R}} \ni d_A(x)$ with the form $B_{\mathbb{R}} = (d_A(x) - m, d_A(x) + m)$. Consider the ball $B_X = B_d(x, m/2)$, $d(B_X) = \lbrace \inf{\lbrace d(x', a) | a \in A \rbrace} | x' \in B_X \rbrace \le \lbrace \inf{\lbrace d(x, x') + d(x, a) | a \in A \rbrace} | x' \in B_X \rbrace$ $= \lbrace \inf{\lbrace d(x, a) | a \in A \rbrace} + \inf{\lbrace d(x, x') | a \in A \rbrace} | x' \in B_X \rbrace \le d_A(x) + m/2$; similarly $d(B_X) \ge d_A(x) - m/2$. Thus $B_X$ is an open set in $X$ containing $x$ whose image is contained in open set containing $d_A(x)$, since $x, V$ are arbitrary, $d_A$ is continuous;
    2. If $x \in \overline{A}$, $0$ is a lower bound for any metric thus $d_A(x) \ge 0$. Suppose $d_A(x) > 0$. $x \in \overline{A} \implies B = B_d(x, d_A(x))$ is a basis element of $(X, d)$ containing $x$ and it must intersect $A$. Say $a_0 \in A \cap B$, then $a_0 \in A$ and by definition $a_0 \in B \implies d(x, a_0) < d_A(x)$, thus $d_A(x)$ is not the $\inf$. Thus $d_A(x) = 0$;
    	If $d_A(x) = 0$: if $x \notin \overline{A}$, then there exists basis element $B$ containing $x$ that does not intersect $A$. WLOG say $B = B_d(x, r)$ be a ball centered at $x$ with radius $r (> 0)$, then we have $\forall a \in A, a \notin B \implies d(x, a) \ge r$. Then $r$ is a lower bound of $d(x, a)$ that is greater than $0$, thus $d_A(x) \ge r > 0$ which is a contradiction. Thus $x \in \overline{A}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Prove that a compact subset of a Hausdorff space is closed**.

    Idea:

    It is very similar with the proof that compact Hausdorff space is regular/normal: for any $x$ that is not in the subset, use compactness of the subset to find a neighborhood of $x$ that is disjoint with that subset, since this work for all $x$, it means complement of the subset is open thus the subset itself is closed.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $X$ be a connected normal space, let $A$ be a proper closed subset of $X$, show that there is a continuous surjective map $f: X\to S^1$ such that $f(a) = 1$ for all $a \in A$**.

    Idea:

    Since $A$ is proper, there exists some $x \in X-A$, clearly $x$ and $A$ are both closed and they are disjoint, so we can apply the Urysohn Lemma to get a continuous $f: X\to [0,1]$, $f(A) = 0$ and $f(x) = 1$. Now this map is surjective: because if some $c$ is not attained, it means the image of $X$ under $f$ is not connected, that cannot happen. Now, map this interval to $S^1$ by joining $0,1$ together at the point $(0,1)$, call this map $g$, then the composition $gf$ is what we want: it is continuous and surjective, and $g(f(A)) = g(0) = (0,1)$. The preimage is not really $A$ but fortunately we did not require that.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 5""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **For $x,y \in \mathbb{R}^2-\lbrace 0 \rbrace$, put $x\sim y$ if and only if $x$ and $y$ lie on a line through the origin, show that $\mathbb{R}^2 - \lbrace 0 \rbrace/\sim$ with the quotient topology is homeomorphic to a circle**.

    Idea:

    Let $F:\mathbb{R}^2 - \lbrace 0 \rbrace \to S^1$ be the map $x \to x/\| x \|$, since we took $0$ out this map is continuous, thus by the universal mapping property of quotient topology, we have that the map $f:\mathbb{R}^2-\lbrace 0 \rbrace/\sim \to S^1, [x] \to x/\| x\|$ is continuous. It is also not hard to check it is bijection, and a bijective quotient map is always a homeomorphism.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 6""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Show that if $f:X\to Y$ is an immersion of smooth manifolds then its differential $df:TX\to TY$ is also an immersion**.

    Idea:

    By Local Immersion Theorem $f$ is locally given by $i$, i.e. if we draw the chart here $s\circ f \circ r^{-1} = i$ so that $ds \circ df \circ (dr^{-1}) = di = i$ ($i$ is inclusion map, and $di_x$ is inclusion map for any $x$ also), i.e. $df$ is also locally given by $i$ so it is an immersion.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 7""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Prove that no smooth compact manifold of dimension $n\ge 1$ is contractible**.

    Idea:

    If it is contractible the identity map is homotopic to a constant map, but their mod $2$ degree is then different, meaning that the manifold itself cannot be smooth compact manifold.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 8""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $C$ be a simple closed curve in the $xy$-plane not passing through the origin, evaluate $\oint_c\frac{xdy-ydx}{x^2+y^2}$**.

    Idea:

    If the curve enclose origin then the integral is either $2\pi$ or $-2\pi$ depends on the orientation, otherwise (by Green's Theorem) it is zero.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Exam 11""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $f: X\to Y$ be a continuous bijection from a compact topological space $X$ onto a Hausdorff topological space $Y$, show that $f$ is a homeomorphism**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**A subspace $A \subseteq \mathbb{R}^n$ has the property that every continuous function $f:A \to \mathbb{R}$ attains its maximum on $A$. Show that $A$ is compact**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $Z$ be a topological space and $Y \subseteq Z$ a retract of $Z$, meaning that there is a continuous map $r:Z\to Y$ such that $r(y) =y$ for every $y \in Y$. Show that if $Z$ is Hausdorff then $Y$ is closed in $Z$**.

    Idea:

    Let $z \in Z-Y$ and that $y = r(z) \in Y$, so that $z \ne y$. Since we are in a Hausdorff space, we can find $U(z), U(y)$ disjoint open set containing $z,y$ respectively. Now claim, the set $r^{-1}(U(y) \cap Y) \cap U(z)$ is a neighborhood of $z$ contained in $Z-Y$: it contains $z$, because $U(z)$ contains $z$ and image of $z$ is in $U(y)$ (and of course in $Y$) thus $z$ is in the preimage; it is open because $U(y) \cap Y$ is open in $Y$ (with subspace topology); it is disjoint from $Y$, because if a point $p$ in $r^{-1}(U(y) \cap Y) \cap U(z)$ is in $Y$, then $r(p) = p$ is also in $Y$, in particular $r(p) \in U(z)$ (use the right half), however since $p$ also in $r^{-1}(U(y) \cap Y)$, it means $r(p)$ is also in $U(y) \cap Y$, in particular in $U(y)$, but they should be disjoint.

    With this claim proved, we have $Z-Y$ open so $Y$ is closed.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Show that for every $n\ge 3$ there is a continuous surjective map $g: I \to I^n$, show that such a map cannot be smooth**.

    Idea:

    Remember the Peano curve, it is a continuous surjective map $f: I \to I^2$, compose numbers of Peano curve together we have a continuous surjective map as desired.

    There cannot be such a smooth map, because smooth map maps a set of measure zero to a set of measure zero.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 5""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Show that a smooth manifold $X$ is path connected if and only if it is connected**.

    Idea:

    If it is path connected, then it is always connected.

    Conversely, fix some $x \in X$ and let $U$ be its path component, we want to show both $U$ and $X-U$ are open (so that since $X$ is connected, one of them must be empty, but it cannot be $U$, because $U$ at least contains $x$):

    For any $x' \in X$, since $X$ is a smooth manifold, it is locally homeomorphic to an open ball in $\mathbb{R}^n$, which is path-connected, so $x'$ has some neighborhood that is path-connected, so this neighborhood lies either entirely in $U$ or entirely in $X-U$, this proves that both $U$ and $X-U$ are open.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 6""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $f:X\to Y$ be a smooth map of compact smooth manifolds, show that the map $F:X\to X\times Y$ given by $F(x) = (x,f(x))$ is an embedding**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 7""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $S^m \subseteq \mathbb{R}^{m+1}$ be the unit sphere, prove that the antipodal map $r:S^{2n+1} \to S^{2n+1}, x\mapsto -x$ is homotopic to the identity map, is the same true for the antipodal map $r:S^{2n} \to S^{2n}, x\mapsto -x, n\ge 1$**?"""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 8""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**Let $C$ be a smoothly embedded circle in the $xy$-plane not passing through the origin, evaluate $\int_C \frac{(2x^3+2xy^2-2y)dx+(2y^3+2x^2y+2x)dy}{x^2+y^2}$**."""
    )
    return


if __name__ == "__main__":
    app.run()
