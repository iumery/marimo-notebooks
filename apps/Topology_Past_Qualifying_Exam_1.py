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
    mo.md(r"""# Exam 1""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $X$ be a topological space, prove that $A \subseteq X$ is open if and only if each point of $A$ has an open neighborhood contained in $A$**.

    Idea:

    If $A$ is open, for any $a \in A$, $A$ is a open neighborhood of $a$ contained in $A$.

    Conversely, say for each $a$ we can find $U(a)$ open neighborhood of $a$ contained in $A$, then claim that $A = \cup U(a)$: for any $a \in A$, clearly it is in the union; for any $a \in \cup U(a)$, it is in some $U(a)$, but we define it to be contained in $A$.
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
    **Prove that the following two statements about a subspace $A \subseteq \mathbb{R}^n$ are equivalent**:

    1. **$A$ is compact**;
    2. **Every continuous function $f: A \to \mathbb{R}$ attains its maximum on $A$**.

    Idea:

    If $A$ is compact, then $f(A)$ is compact, now $f(A)$ is bounded implies that the there is a upper bounded, $f(A)$ is closed implies that the value can be achieved.

    If every continuous function $f: A \to \mathbb{R}$ attains its maximum on $A$, then in particular then function $f(a) = d(0,a)$ attains its maximum, that $A$ is bounded; now, suppose $A$ is not closed, meaning that there is a limit point $a$ of $A$ but it is not in $A$, then the function $f(x) = d(a,x)$ is never $0$ on $A$, thus $g(x) = 1/f(x)$ is well-defined and continuous thus attains maximum $M$, meaning that $f(x)$ achieve minimum $1/M$, but that means $a$ is not a limit point anyway.
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
    **Let $A_1, A_2, \dots$ be a sequence of connected subspace of a topological space $X$ such that $A_n \cap A_{n+1}$ is non-empty for all $n$, prove that the union $\cup A_n$ is connected**.

    Idea:

    $A_1 \cap A_2$ is not empty thus $A_1 \cup A_2$ is connected; see $A_1 \cup A_2$ as one connected set, and notice that $A_2 \subseteq A_1 \cup A_2$ thus $(A_1 \cup A_2) \cap A_3$ is not empty, thus $A_1 \cup A_2 \cup A_3$ is connected, continue inductively we have the desired statement.
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
    **Recall that $\ell^2$ is the metric space of all infinite sequences $x = (x_1,x_2,\dots)$ of real numbers such that the series $\sum x_n^2$ converges, with the metric $d(x,y) = \sqrt{\sum\limits(x_n - y_n)^2}$. Let $A \subseteq \ell^2$ consists of all sequences $x$ that are eventually zero, meaning that $x_n = 0$ for all but finitely many $n$**.

    1. **Prove that $A$ is dense in $\ell^2$**;
    2. **Use part 1 to prove that $\ell^2$ is a separable topological space**.

    Idea:

    1. For any $x \in \ell^2$ and any $r$ such that $B(x,r)$ is an arbitrary (small) basis element centered at $x$, $x$ by definition has the property that $\sum x_n^2$ converges, say the limit is $m$, then by definition of a convergent series it means that there exists $N$ such that $| \sum\limits^N x_n^2 - m | < r^2$, meaning that $\sum\limits_N^{\infty} x_n^2 < r^2$, but then the distance between $x$ and $a = (x_1,x_2, \dots, x_N, 0,0,\dots) \in A$ is defined as $= \sqrt{x_{N+1}^2+\dots} < \sqrt{r^2} = r$;
    2. If $A$ is countable then we are done, this is not the case, nevertheless, $A' \subseteq A$ with rational terms is countable (countably union of countable is countable), and it is also dense in $\ell^2$ because $\mathbb{Q}$ is dense in $\mathbb{R}$.
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
    **Prove that $\mathbb{R}^k$ and $\mathbb{R}^l$ are not diffeomorphic unless $k = l$**.

    Idea:

    Suppose they are diffeomorphic, then $Df_a: \mathbb{R}^k \to \mathbb{R}^l$ is an isomorphism of vector spaces (over $\mathbb{R}$, of course), it could only happen when $k = l$.
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
    **Prove that the $2$-sphere $S^2$ does not retract onto its equator $S^1 \subseteq S^2$, that is, there is no smooth map $r: S^2 \to S^1$ whose restriction to $S^1$ is the identity**.

    Idea:

    If there is such $r$, restrict it to the northern hemisphere (and $S^1$) is still smooth, however now it becomes a smooth map from $X \to \partial X$ with restriction on the boundary is the identity, we proved that this cannot happen.
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
    **Let $w = (3+2xy)dx + (x^2-3y^2)dy$ be a $1$-form on the $xy$-plane**.

    1. **Is $w$ closed**?
    2. **Is $w$ exact**?

    Idea:

    1. $dw = (2ydx + 2xdy)\wedge dx + (2xdx -6y dy) \wedge dy = 0$ thus it is closed;
    2. Yes, consider the $0$-form $\theta = x^2y-y^3+3x$, then $d\theta = w$.
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
    **Let $f_0, f_1: X\to Y$ be homotopic maps between compact oriented manifolds of dimension $n$. Prove that for all closed $n$-forms $w$ on $X$, we have that $\int_X f_0^{*}w = \int_X f_1^{*}w$**.

    Idea:

    Say the homotopy is $F:X\times [0,1] \to Y$. By assumption $F$ is smooth on $X \times \lbrace 0,1 \rbrace$ and is defined on $X \times [0,1]$, $w$ is closed, thus $\int_{X\times \lbrace 0,1 \rbrace}F^{*}w$ $= \int_{X \times [0,1]}dF^{*}w$ $= \int_{X \times [0,1]}F^{*}dw = 0$, on the other hand it also equals $\int_{-X\times\lbrace 0 \rbrace}F^{*}w + \int_{X \times \lbrace 0 \rbrace}F^{*}w$ $= -\int_{X\times\lbrace 0 \rbrace}F^{*}w + \int_{X \times \lbrace 0 \rbrace}F^{*}w$, but those are exactly $\int_X f_0^{*}w$ and $\int_X f_1^{*}w$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Exam 2""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $X$ and $Y$ be topological spaces and $f: X \to Y$ a map which is continuous and bijective**.

    1. **Give an example showing that $f$ need not be a homeomorphism**;
    2. **Prove that $f$ must be a homeomorphism under the additional assumption that $X$ is compact and $Y$ is Hausdorff**.

    Idea:

    1. The identity map between $3$-element sets with suitable topology on them to make the function continuous but not open is enough to be an example;
    2. Let us show the map is closed: for any $C \subseteq X$ be closed: closed subset of compact set is compact, thus $C$ is also compact, image of compact set under continuous function is compact, so $f(C)$ is compact, and finally compact subset of Hausdorff space is closed, thus $f(C)$ is closed. This shows $f^{-1}$ is also continuous.
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
    **Let $X$ be a non-empty compact topological space**.

    1. **Give an outline of the proof of the extreme value theorem**;
    2. **Part 1 presumes that $\mathbb{R}$ has the Euclidean topology, is the statement also true if $\mathbb{R}$ has the finite complement topology**?

    Idea:

    1. The image of compact set under continuous function is compact, which means bounded and closed in $\mathbb{R}$, now, boundedness implies that $f(X)$ must have certain upper and lower bounds, namely $\sup\limits{f(x)}$ and $\inf{f(x)}$, in metric space they are essentially limit points, so closed-ness implies that they must be attainable;
    2. Not really - for a counterexample just think about $f: [0,1] \to \mathbb{R}$, where $t \mapsto \tan(\pi(-0.5+t))$ if $t \in (0,1)$ and assign $t$ arbitrary value if $t \in \lbrace 0,1 \rbrace$, $[0,1]$ is given the standard topology and $\mathbb{R}$ given the finite complement topology, this function is continuous, because the only closed sets in $\mathbb{R}$ is now finite sets (and trivial ones), so its preimage is of course finite (or empty set and the whole $[0,1]$), thus closed. However extreme values are not attained at any given point.
    	The argument we used in part 1 basically fails at the very beginning, $\mathbb{R}$ equipped with finite complement topology is not even metrizable (not Hausdorff), so we cannot talk about boundedness.
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
    **Let $\lbrace x_n \rbrace$ and $\lbrace y_n \rbrace$ be Cauchy sequences in a metric space $(X,d)$, prove that the sequence of real numbers $\lbrace d(x_n,y_n) \rbrace$ converges**.

    Idea:

    By assumption, for any $\varepsilon > 0$ there exists $N$ such that $d(x_{n_1},x_{n_2}) < \varepsilon$ for any $n_1,n_2 > N$, and there exists $M$ such that $d(y_{m_1},y_{m_2}) < \varepsilon$ for any $m_1,m_2 > M$. Combine them and use $T = \max{(N,M)}$, for any (fixed) $\varepsilon > 0$ there exists $T$ such that $d(x_n,x_m) < \varepsilon$ and $d(y_n,y_m)<\varepsilon$ for any $n,m>T$.

    Now for any $\varepsilon>0$, find the above $T$, and fix any $m>T$ (so that now $d(x_m,y_m)$ is a known number), then for any $n>T$: $d(x_n,y_n)\le d(x_n,x_m)+d(x_m,y_m)+d(y_m,y_n) < 2\varepsilon+d(x_m,y_m)$, similarly $d(x_n,y_n) > d(x_m,y_m)-2\varepsilon$, and we have convergence.
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
    **Prove that the union of the two coordinate axes in $\mathbb{R}^2$ is not a manifold**.

    Idea:

    Denote this object as $T$:

    One approach is to say that at any point other than the origin, locally $T$ is diffeomorphic to $\mathbb{R}$, but that is certainly not true at the origin.

    Or we can say that at the origin, taking derivative from different directions leads to vector from different directions, forcing $r' = 0$, but then it cannot be a diffeomorphism.
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
    **The special orthogonal group $SO(n), n\ge 1$, consists of all real $n\times n$ matrices $A$ such that $A A^t = E$ and $\det{A} = 1$. Prove that $SO(n)$ is a smooth manifold, and determine its dimension**.

    Idea:

    $SO(n)$ is a subgroup of $O(n)$, which is a manifold of dimension $n(n-1)/2$. Also remember that $\det$ send $O(n)$ to $\lbrace \pm 1 \rbrace$ and $\lbrace 1 \rbrace$ is open, we have that $SO(n)$ is open (preimage of open is open), thus it is sub-manifold, and the dimension is the same.
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
    **Prove that there is no such manifold $Y$ such that the sphere $S^n$ of dimension $n \ge 2$ is diffeomorphic to $S^1 \times Y$**.

    Idea:

    If so, then $S^n \cong S^1 \times Y \to S^1 \times \lbrace y \rbrace$ (natural projection, smooth) $\cong S^1$ is a smooth map from $S^n \to S^1$ that fixes $S^1$. This is not possible.
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
    **Let $S^n, n \ge 1$ be the unit sphere in $\mathbb{R}^{n+1}$ given by $\| x \| = 1$. Suppose that $f: S^n \to S^n$ is a smooth map such that the position vector of $x \in S^n$ and the position vector of $f(x) \in S^n$ are perpendicular to each other for all $x \in S^n$, prove that $f$ is homotopic to the identity map of $S^n$, show that such an $f$ exists if and only if $n$ is odd**.

    Idea:

    Since $f$ has codomain $S^n$, $F(x,t) = \frac{xt+f(x)(1-t)}{\| xt+f(x)(1-t) \|}$ gives us the desired homotopy (denominator is never zero because $x$ and $f(x)$ are perpendicular, in particular not on the same line).

    Now note that in particular $f$ is a non-vanishing vector field, thus it does not exists if $n$ is even; if $n = 2k-1$ is odd, then $f(x_1,\dots,x_{2k}) = (-x_2,x_1,-x_4,x_3,\dots,-x_{2k},x_{2k-1})$ which clearly always lie on $S^{2k-1}$ gives the desired vector field.
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
    **Let $X \subseteq \mathbb{R}^3$ be a compact connected orientable surface without boundary, and let $\omega \in \Omega^1(X)$, prove that $d\omega$ must vanish at some point of $X$**.

    Idea:

    This is the first two steps in the proof of Stokes' Theorem, basically we want to show that $\int_X dw = 0$, see here.

    Let $\lbrace O_{\alpha} \rbrace$ be an open covering of $X$ by open sets parameterized by $r_{\alpha}: U_{\alpha} \to O_{\alpha}$, $U_{\alpha} \subseteq \mathbb{R}^n$, and let $\lambda_{\alpha}: X \to \mathbb{R}$ be a partition of unity subordinate to $\lbrace O_{\alpha} \rbrace$. Write $\int_X dw = \int_X d(\sum \lambda_{\alpha})w = \sum\limits_{\alpha} \int_X d(\lambda_{\alpha}w)$.

    Let $U \subseteq \mathbb{R}^2$ be open and $w \in \Omega^1(U)$ have compact support in $U$, then we need to prove that $\int_Udw = 0$. Write $w = a_1(x)dx^2 + a_2(x)dx^1$, then $dw = \frac{\partial a_1}{\partial x^1} dx^1 \wedge dx^2 + \frac{\partial a_2}{\partial x^2} dx^1 \wedge dx^2$. Interpret: $\int_U dw = \int_{\mathbb{R}^2}dw$ $= \int_{\mathbb{R}^2}\frac{\partial a_1}{\partial x^1} dx^1 dx^2 + \int_{\mathbb{R}^2}\frac{\partial a_2}{\partial x^2} dx^1 dx^2$. For any $i$, interpret the $i$-th term first with respect to $x^i$ to obtain $= \int_{\mathbb{R}}(\int_{-\infty}^{\infty}\frac{\partial a_1}{\partial x^1}dx^1)dx^2 + \int_{\mathbb{R}}(\int_{-\infty}^{\infty}\frac{\partial a_2}{\partial x^2}dx^2)dx^1$ $= \int_{\mathbb{R}}a_1(x^1, x^2) |_{x^1 = -\infty}^{\infty}dx^2 + \int_{\mathbb{R}}a_2(x^1, x^2) |_{x^2 = -\infty}^{\infty}dx^1 = 0 + 0$ because $w$ has compact support (in particular $\pm \infty$ is not in the support, i.e. valuation at $\pm \infty$ is zero).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Exam 3""")
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
        r"""
    **Let $\mathbb{R}^{\omega}$ be the countably infinite product of $\mathbb{R}$ with itself**.

    1. **Define both the product topology and the box topology on $\mathbb{R}^{\omega}$**;
    2. **Consider the function $f: \mathbb{R} \to \mathbb{R}^{\omega}$ given by $f(t) = (t,t,\dots)$, prove that $f$ is continuous when $\mathbb{R}^{\omega}$ is given the product topology but not when given the box topology**.

    Idea:

    1. Box topology is constructed by basis element of the form $\prod\limits U_i$, where $U_i = (a_i,b_i)$ is of the form of open interval in $\mathbb{R}$; Product topology is constructed in a similar way, however, all but finitely many $U_i = \mathbb{R}$ itself;
    2. In product topology, consider an arbitrary basis element $V = \prod\limits U_i = \prod\limits^N (a_i,b_i) \times \prod\limits \mathbb{R}$, we want to show the preimage of this is open: intersection of finite open sets is open, so $\cap (a_i,b_i) = U$ open, easy to see the preimage of $V$ is $U$, and we are done.

    In box topology, however, consider $V = (-1,1) \times (-1/2,1/2) \times \dots$ then we should see that no matter how small $\delta$ we choose, $f(-\delta,\delta)$ is not contained in $V$ thus the map is not continuous.
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
    1. **Define both the terms connected and path connected**;
    2. **Prove or give a counterexample: a path connected topological space is connected**;
    3. **Prove or give a counterexample: if $A \subseteq X$ is a path connected subset of a topological space, then its closure $\overline{A}$ is path connected**.

    Idea:

    1. Connected: no separation; Path connected: any two points admit a path;
    2. Suppose $X = U \cup V$ is a separation, choose $x_0 \in U, x_1 \in V$ and consider a path $\gamma: [0, 1] \rightarrow X$ such that $\gamma(0) = x_0$ and $\gamma(1) = x_1$, then $[0, 1] = \gamma^{-1}(X) = \gamma^{-1}(U) \cup \gamma^{-1}(V)$ is a separation of $[0, 1]$, which is a contradiction;
    3. Counterexample: the topologist's sine curve $S = \lbrace (x, \sin(\frac{1}{x})) | 0 < x \le 1 \rbrace$, $S$ is path connected but $\overline{S}$ is not path connected:
    	1. $S$ is image of an interval under a continuous function thus path connected;
    	2. Suppose $f(t) = (a(t),b(t))$ is a path connecting $(0,0)$ and $(1/\pi,0)$, in particular, it is continuous, then by intermediate value theorem there is $0<t_1<1$ so that $a(t_1) = \frac{2}{3\pi}$, notice in this case $b(t_1) = -1$. Similarly there is $0<t_2<t_1$ so that $a(t_2) = \frac{2}{5\pi}$, notice in this case $b(t_2) = 1$. Continue inductively we have a sequence $t_n$. Now $t_n$ is convergent, because it is bounded and monotone (in $\mathbb{R}$). By the continuity theorem in metric space we must have $f(t_n)$ convergent, but this is not true, because $b(t_n)$ does not converge.
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
    **Prove that a closed subspace of a compact space is compact**.

    Idea:

    Say $A \subseteq X$ is a closed subspace of a compact space. Want to show $A$ is compact. Let $\cup U_i$ be an arbitrary open covering of $A$, then $(\cup U_i) \cup (X-A)$ is an open covering for $X$, which must admit finite sub-covering, remove $(X-A)$ from that sub-covering and we get a finite sub-covering for $A$.
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
    **Let $f: X\to \mathbb{R}$ be a smooth function on a smooth, compact, boundary-less manifold $X$. Suppose $0$ is a regular value, prove that $f^{-1}(0)$ is diffeomorphic to the boundary of some smooth compact manifold $W$**.

    Idea:

    What we want to say here is that $\lbrace p | f(p) \le 0 \rbrace$ is a manifold with boundary $f^{-1}(0)$.

    The 'compact' part is easy, preimage of closed set is closed, and closed subset of compact set is compact.

    The set of points $p \in X$ where $f(p)<0$ is open (preimage of $(-\infty, 0)$) in $X$ thus is a manifold. For each $p \in X$ such that $f(p) = 0$, by the local submersion theorem, every $p \in f^{-1}(0)$ has a neighborhood with local coordinates $x_1, \dots, x_n$ such that $f^{-1}(0)$ is given by $x_n = 0$. The part of this neighborhood given by $f(x) \le 0$ (equivalently $x_n \le 0$) is homeomorphic to an open set in $\mathbb{R}^n_+$ of the second type.
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
    **Let $X$ be a compact smooth manifold, $Y$ be smooth manifold, and $Z$ be a closed smooth sub-manifold of $Y$**.

    1. **Define what it means for the smooth function $f: X \to Y$ to be transversal to $Z$**;
    2. **Define what it means for the two smooth functions $f_0,f_1: X\to Y$ to be homotopic**;
    3. **Show if $f_0,f_1: X\to Y$ are homotopic and both transversal to $Z$, then $I_2(f_0,Z) = I_2(f_1,Z)$, i.e. their mod $2$ intersection numbers with $Z$ are equal**.

    Idea:

    1. We say that $f$ is transversal to $Z$ if $\forall p \in f^{-1}(Z)$, $df_p(T_pX) + T_{f(p)}Z = T_{f(p)}Y$;
    2. We say that they are homotopic if there is a smooth map $F: X \times [0,1] \to Y$ such that $F(x,0) = f_0(x)$ and $F(x,1) = f_1(x)$;
    3. Let $F: X \times [0,1] \to Y$ be the homotopy between $f_0$ and $f_1$. By Extension Theorem we may assume $F$ is transversal to $Z$. Then $F^{-1}(Z)$ is a $1$-dimension sub-manifold of $X \times [0,1]$ (because in the definition of mod $2$ intersection number we explicitly ask $\dim{X} + \dim{Z} = \dim{Y}$, so now $\dim{X\times [0,1]} + \dim{Z} - \dim{Y}$ must be $1$) and its boundary is $\partial F^{-1}(Z) = F^{-1}(Z) \cap \partial (X \times [0,1]) = f_0^{-1}(Z) \times \lbrace 0 \rbrace \cup f_1^{-1}(Z) \times \lbrace 1 \rbrace$, but we know that a $1$-manifold always have even number of points on the boundary, thus we have the desired statement.
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
    **Let $r = \sqrt{x^2+y^2}$, for each non-negative integer $n$, determine whether the $1$-form $w_n = \frac{-ydx + xdy}{r^n}$ defined on $\mathbb{R}^2-\lbrace (0,0) \rbrace$ is closed or exact**.

    Idea:

    $n = 0$, then $w_0 =-ydx+xdy$, $dw_0 = -dy\wedge dx + dx \wedge dy = 2dx \wedge dy$ is not closed, so it cannot be exact, so it is neither closed nor exact;

    $n = 1$, then $w_1 = \frac{-y}{\sqrt{x^2+y^2}}dx + \frac{x}{\sqrt{x^2+y^2}}dy$, $dw_1 = \frac{x^2}{(x^2+y^2)^{3/2}}dx \wedge dy + \frac{y^2}{(x^2+y^2)^{3/2}}dx \wedge dy$ is not closed nor exact;

    $n = 2$, then $w_2 = \frac{-y}{x^2+y^2}dx + \frac{x}{x^2+y^2}dy$, one can check $dw_2 = 0$, see homework to see it is not exact;

    $n = 3$, not closed so not exact;

    $n = 4$, not closed so not exact;

    $\dots$

    i.e. only when $n = 2$ it is closed but not exact, otherwise it is neither closed nor exact.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Exam 4""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $X$ be a topological space. Prove that a subspace $A \subseteq X$ is dense if and only if its complement has empty interior**.

    Idea:

    $A$ is dense, then in particular any $x \in X-A$, any neighborhood of $x$ intersect with $A$, in other word, not entirely lying in $X-A$, thus no $x$ is in the interior, i.e. interior of $X-A$ is empty. This argument also work the other way round.
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
    **Let $(X,d)$ be a compact metric space with continuous contraction $f: X \to X$ ($f$ is a contraction if there exists a number $a < 1$ such that $d(f(x),f(y)) < ad(x,y)$ for any distinct $x,y \in X$), show that there exists a unique point $x \in X$ such that $f(x) = x$**.

    Idea:

    Denote $f^1 = f$ and $f^{n + 1} = f \circ f^n$. Consider the intersection $A$ of the sets $A_n = f^n(X)$.

    $A_1 = f(X)$ is image of compact space under continuous map thus compact, and it is subspace of a Hausdorff (metric) space thus closed. By a regular induction step, it is easy to see that $A_n = f^n(X)$ is compact and closed for all $n$.

    Suppose $x \in A$ then $x \in A_n$ for all $n$, thus $f(x) \in A_n$ for all $n > 1$, but $f(x)$ is naturally contained in $A_1 = f(X)$, thus $f(x) \in A_n$ for all $n$ thus $f(x) \in A$. Thus $f(A) \subseteq A$.

    Naturally $f^{n+1}(X) \subseteq f^n(X)$ for all $n$ because the domain and codomain are both $X$, each of them would be non-empty, thus their intersection $A$ (of a sequence of nested nonempty compact sets in a compact space) is non-empty.

    Now suppose $f$ is a contraction, then $d(f^n(x), f^n(y)) \le \alpha d(f^{n-1}(x), f^{n-1}(y)) \le \alpha^2 d(f^{n-2}(x), f^{n-2}(y)) \le \dots \rightarrow 0$ for some $\alpha < 1$, thus $A$ can have only one point $a$, since $f(A)$ is non-empty it must also be that exact point, i.e. it is the fixed point.

    To show this is the only fixed point: suppose $x, y$ are both fixed point, then $d(f(x), f(y)) = d(x, y) \le \alpha d(x, y) < d(x, y)$ which is impossible.
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
    **Let $f: X \to Y$ be a function between topological spaces. Prove that $f$ is continuous if and only if $f(\overline{A}) \subseteq \overline{f(A)}$ for any subset $A \subseteq X$**.

    Idea:

    Suppose $f$ is continuous and $A \subseteq X$, then $A \subseteq f^{-1}(f(A))$ $\subseteq f^{-1}(\overline{f(A)})$, now preimage of closed set must be closed, so $f^{-1}(\overline{f(A)})$ is closed, so it equals to its closure, that means $\overline{A} \subseteq f^{-1}(\overline{f(A)})$ as well. Apply $f$ both side we have $f(\overline{A}) \subseteq f(f^{-1}(\overline{f(A)})) \subseteq \overline{f(A)}$;

    Conversely, we want to show preimage of closed set is always closed. Suppose $B$ is closed in $Y$ so that $\overline{B} = B$, then $f(\overline{f^{-1}(B)})$ (now use the assumption) $\subseteq \overline{f(f^{-1}(B))} \subseteq \overline{B} = B$. In particular $f(\overline{f^{-1}(B)}) \subseteq B$, apply $f^{-1}$ each side we have $\overline{f^{-1}(B)} \subseteq f^{-1}(f(\overline{f^{-1}(B)})) \subseteq f^{-1}(B)$, but naturally $f^{-1}(B) \subseteq \overline{f^{-1}(B)}$, so we have equality, as thus $f^{-1}(B)$ is closed.
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
    **Prove the Intermediate Value Theorem: Let $f: X \to Y$ be a continuous map of the connected space $X$ to the ordered set $Y$ in the order topology. If $a$ and $b$ are two points of $X$ and $r$ is a point of $Y$ between $f(a)$ and $f(b)$, then there exists a point $c \in X$ such that $f(c) = r$**.

    Idea:

    If certain $r$ is not attainable, then consider $A = \lbrace y \in f(X) | y<r \rbrace$ and $B = \lbrace y \in f(X) | y > r \rbrace$: by construction they are non-empty (containing $f(a), f(b)$ respectively); they are disjoint, because an element in such $Y$ cannot both less than $r$ and larger than $r$; they are open because for example we can write $A = f(X) \cap (-\infty,r)$. So $A,B$ form a separation for $f(X)$, which is a contradiction because image of connected space under continuous map should be connected.
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
    **Prove the graph of $f(x,y) = \sqrt{x^2+y^2}$ is homeomorphic but not diffeomorphic to $\mathbb{R}^2$**.

    Idea:

    Homeomorphism: just use the natural projection $(x,y,\sqrt{x^2+y^2}) \mapsto (x,y)$ and the inverse $(x,y) \mapsto (x,y,\sqrt{x^2+y^2})$, they are both obviously continuous and bijective;

    At $(0,0)$ locally the graph looks like a cone, that leads to a problem, because either it is not differentiable there, or the derivative is $0$, either way it cannot be a smooth manifold.
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
    **For which values of $r>0$ does $H = \lbrace x^2+y^2-z^2-w^2 = 1 \rbrace \subseteq \mathbb{R}^4$ transversally intersect $S^3_r \subseteq \mathbb{R}^4$, the $3$-sphere of radius $r$ centered at the origin**?

    Idea:

    Let us try to solve for $x,y,z,w$, it is not hard to get from the assumptions that $\frac{r^2-1}{2} = z^2+w^2$ and $\frac{r^2+1}{2} = x^2+y^2$, so:

    1. If $0<r<1$ then there is no real solution for $z$ and $w$, thus the two objects do not have an intersection, so they are (vacuously) transversal at any points;

    2. If $r = 1$, then $z = w =0$ and $x^2+y^2 = 1$, i.e. the intersection is the $S^1 \subseteq \mathbb{R}^4$. At any of such point the normal vector for the two objects are both $(2x,2y,0,0)$, so they are linearly dependent, and causing that they do not transversally intersect there;

    3. If $r > 1$, the two objects intersect at those points where $\frac{r^2-1}{2} = z^2+w^2$ and $\frac{r^2+1}{2} = x^2+y^2$, by above argument, they intersect transversally there.
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
    **Let $X$ be a smooth, compact, boundary-less $n$-manifold and $f: X\to \mathbb{R}^n$ be a smooth map, prove that $f$ must have a critical point**.

    Idea:

    Let $\pi: \mathbb{R}^n \to \mathbb{R}$ be a canonical projection send the vector to, say, the first coordinate. Now $\pi(f)$ is a real function on a compact set, thus it must have a critical point $p$. Also that $f$ and $\pi$ are both smooth, so we have to be able to differentiate $\pi(f)$ at $p$, use the Chain Rule we have, $(\pi \circ f)'_p = \pi'_{f(p)} \circ f'_p$. Now remember that the definition of a critical point, that is at that point the derivative is not surjective. But $\pi'_{f(p)}$ is always surjective, so if $f'_p$ is surjective, we would have $(\pi \circ f)'_p$ be surjective, but that is not the case because $p$ is a critical point for $\pi f$, thus $f'_p$ is not surjective, which is equivalent with that $p$ is also a critical point for $f$.
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
    **Consider the $2$-form $\omega = zdx \wedge dy$ on $\mathbb{R}^3$**.

    1. **Is $\omega$ exact**?
    2. **Let $M$ be the paraboloid $z-x^2-y^2 = 1$ in $\mathbb{R}^3$, is the restriction of $\omega$ to $M$ exact**?

    Idea:

    1. $dw = 1dz \wedge dx \wedge dy = dx\wedge dy \wedge dz \ne 0$ so it is not closed, nor exact;
    2. In this case we can rewrite $w = (1+x^2+y^2)dx\wedge dy$, and that is equal to $d((x^3/3+x+xy^2)dy)$, so it is exact.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Exam 5""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $X$ and $Y$ be metric spaces, and $f,g : X\to Y$ be continuous. Suppose that $f = g$ on a subset $A \subseteq X$ which is dense in $X$, prove that $f = g$ on the entire $X$**.

    Idea:

    Suppose not, it means $f(x) \ne g(x)$ for some $x$. Since $Y$ is a metric space we can find $U_f,U_g$ neighborhood of $f(x)$ and $g(x)$ respectively that are disjoint. $f^{-1}(U_f)$ and $g^{-1}(U_g)$ are open, and they both contain $x$, so their intersection $V = f^{-1}(U_f)\cap g^{-1}(U_g)$ is also a neighborhood of $x$. Now use the fact that $A$ is dense, it means $V$ intersects $A$ at some $x'$, but for this $x'$ by our construction, $f(x') \in U_f$ and $g(x') \in U_g$ so they are not equal, so $f \ne g$ even on $A$, gives a contradiction.
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
    **Recall that a subspace $A$ of a topological space $X$ is called a retract of $X$ if there is a continuous map $r: X\to A$ such that $r\circ i = 1$ where $i: A \to X$ is the inclusion map. Prove that $\lbrace 0,1 \rbrace$ is not a retract of $[0,1]$**.

    Idea:

    In particular we want a surjective continuous map $r:[0,1] \to \lbrace 0,1 \rbrace$, which is impossible because image of connected set under continuous map is connected, yet $\lbrace 0,1 \rbrace$ is not.
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
    **Let $X$ be a Hausdorff topological space, and $A,B \subseteq X$ its compact subspaces, prove that $A \cap B$ is compact**.

    Idea:

    $A,B$ compact in Hausdorff $X$ so $A,B$ closed, so $A \cap B$ closed in $X$, so $A \cap B = (A \cap B) \cap A$ is closed in $A$ with subspace topology, and closed subset of compact space is compact.
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
    **Let $(X,d)$ be a metric space. Recall that a map $f: X \to X$ is called a contraction of $X$ if there is a number $c<1$ such that $d(f(x),f(y))\le cd(x,y)$ for all $x,y\in X$. Prove that if $f$ is a contraction of a complete metric space $X$ then there is a unique point $x \in X$ such that $f(x) = x$**.

    Idea:

    Define $f^1 = f$ and $f^{n + 1} = f \circ f^n$. Consider the intersection $A$ of the sets $A_n = f^n(X)$.

    $A_1 = f(X)$ is image of compact space under continuous map thus compact, and it is subspace of a Hausdorff (metric) space thus closed. By a regular induction step, it is easy to see that $A_n = f^n(X)$ is compact and closed for all $n$.

    Suppose $x \in A$ then $x \in A_n$ for all $n$, thus $f(x) \in A_n$ for all $n > 1$, but $f(x)$ is naturally contained in $A_1 = f(X)$, thus $f(x) \in A_n$ for all $n$ thus $f(x) \in A$. Thus $f(A) \subseteq A$.

    Similarly we can see that $f^{n+1}(X) \subseteq f^n(X)$ for all $n$, each of them would be non-empty, thus their intersection $A$ (whose diameter goes to $0$) is non-empty (this is a property for complete metric space).

    Now suppose $f$ is a contraction, then $d(f^n(x), f^n(y)) \le \alpha d(f^{n-1}(x), f^{n-1}(y)) \le \alpha^2 d(f^{n-2}(x), f^{n-2}(y)) \le \dots \rightarrow 0$ for some $\alpha < 1$, thus $A$ can have only one point $a$, since $f(A)$ is non-empty it must also be that exact point, i.e. it is the fixed point.

    To show this is the only fixed point: suppose $x, y$ are both fixed point, then $d(f(x), f(y)) = d(x, y) \le \alpha d(x, y) < d(x, y)$ which is impossible.
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
    **Let $f: X\to Y$ be a smooth map of compact manifolds of the same dimension, and $q \in Y$ is a regular value of $f$, prove that $f^{-1}(q)$ is finite**.

    Idea:

    By definition of a regular value, for each $x \in f^{-1}(y)$, $f$ is a submersion at $x$; since $\dim{X} = \dim{Y}$, $f$ is locally given by the identity map, thus $f$ is a local diffeomorphism at $x$. On the other hand, suppose $f^{-1}(y) \subseteq X$ is infinite, then by (limit-point) compactness of $X$, it has a limit point $x$, and $x \in f^{-1}(y)$ because $f^{-1}(y)$ is closed.

    But then, $f$ cannot even be injective near $x$ (every neighborhood contains another $x'$ in the preimage of $y$), hence not a local diffeomorphism, a contradiction, thus we have $f^{-1}(y)$ must be finite.
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
    **Prove that all contractible manifolds are simply connected. Give an example which shows the converse is not true**.

    Idea:

    Since $S^1$ itself is a manifold, let $g: S^1 \to X$ be an arbitrary map and $f: S^1 \to X$ be a constant map, since $X$ is contractible $g$ and $f$ are homotopic.

    $X$ is connected: say we have the homotopy $F(x,t)$ between $\text{id}$ to a constant map $f(x) = c$, for any fixed $x$ this gives us a continuous (smooth, but we don't really need it) map $g_x(t) = F(x,t)$ where $g_x(0) = x$ and $g_x(1) = c$. Now for any $x, y \in X$, find the map $g_x$ and $g_y$ and combine them to $g(t) = \begin{cases} g_x(2t), 0\le t\le 1/2\\g_y(2 - 2t), 1/2 \le t \le 1 \end{cases}$. This is a continuous map with $g(0) = x$ and $g(1) = y$, since $x,y$ arbitrary, we have $X$ is path-connected thus connected.

    By definition, $X$ with the above two properties is simply connected.

    The converse is false, for example, $S^2$ is simply connected but not contractible.
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
    **Let $S^n$ be the unit sphere in $\mathbb{R}^{n+1}$ given by $| x | = 1$, compute the degree of the antipodal map $f: S^n \to S^n$ defined as $x \mapsto -x$**.

    Idea:

    It consists of $n+1$ reflections, each of which has degree $-1$, so the antipodal map has degree $1$ if $n$ odd and $-1$ if $n$ even.
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
    **Use Stokes' Theorem to evaluate the integral: $\int_C 3x^2ydx + x^3dy + 3xydz$ where $C$ is the curve of intersection of the saddle $z = x^2-y^2$ with the cylinder $x^2+y^2 = 1$ oriented clock-wise as viewed from the top of the $z$-axis**.

    Idea:

    Calculate $dw$ first, $dw = 3x^2dy\wedge dx+3x^2dx\wedge dy+3y dx\wedge dz +3xdy \wedge dz$ $= 3y dx\wedge dz +3xdy \wedge dz$ (so basically $curl{\overline{F}} = (3x,-3y,0)$ here).

    Now parameterize the curve as $x = r\cos(t), y = r\sin(t)$ so that $z = x^2-y^2 = r^2(\cos^2(t) - \sin^2(t)) = r^2\cos(2t)$, i.e. we have the parametrization $\varphi(r, t) = (r\cos(t),r\sin(t),r^2\cos(2t))$, so we have $\frac{\partial \varphi}{\partial r} = (\cos(t),\sin(t),2r\cos(2t))$ and $\frac{\partial \varphi}{\partial t} = (-r\sin(t),r\cos(t),-2r^2\sin(2t))$, take the cross product gives us the normal vector on the surface we want to integrate: $n = \frac{\partial \varphi}{\partial r}\times \frac{\partial \varphi}{\partial t}$ $= (-2r^2\sin(t)\sin(2t)-2r^2\cos(2t)\cos(t),$ $-2r^2\cos(2t)\sin(t)-2r^2\cos(t)\sin(2t),r)$ (and noticing here the direction of the normal vector is wrong, we will need to use $-n$).

    Now the calculation: $\int_Cw = \int_0^{2\pi}\int_0^1 (3r\cos(t),-3r\sin(t), 0)\cdot (-n) drdt$ $= \int_0^{2\pi}\int_0^1 6r^3 drdt = 3\pi$.

    A revise:

    After we applied Stokes' Theorem, use parametrization like $(x,y,x^2-y^2)$ will save us a lot of energy:

    Consider the surface $C'$ be the part of the saddle such that $x^2+y^2\le 1$. Parameterize $C'$ by $r(x,y) = (x,y,x^2-y^2)$, $x^2+y^2 \le 1$, by Stokes' Theorem, $\int_C w = \int_{C'}dw$ $= \int_{C'}3y dx\wedge dz +3xdy \wedge dz$ $= \int \int_U 3y dx\wedge (2xdx-2ydy) +3xdy \wedge (2xdx-2ydy)$ $= \int \int_U -6y^2 dx\wedge dy - 6x^2 dx \wedge dy$ $= \int_0^{2\pi} \int_0^1 -6r^3 drd\theta$ $=-3\pi$, notice we orient in a different way so final answer should be $3\pi$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Exam 6""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Given a set $X$, let $\tau$ be the collection of all subsets $U$ of $X$ such that $X-U$ is either finite or all of $X$, show that $\tau$ is a topology on $X$**.

    Idea:

    This is the finite complement topology:

    1. $\varnothing, X$ are in $\tau$;
    2. Let $U_1,U_2 \in \tau$, then $X - (U_1 \cap U_2) = (X-U_1) \cup (X-U_2)$, finite union finite is finite, so $U_1 \cap U_2 \in \tau$;
    3. Let $U_i \in \tau$, then $X- \cup U_i = \cap (X-U_i)$, intersection of finite sets is finite, so $\cup U_i \in \tau$.
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
    **Prove or give a counterexample, a continuous bijective map from one topological space to another is a homeomorphism**.

    Idea:

    No, use a continuous bijection that is not open.
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
    **A subspace $A \subseteq \mathbb{R}^n$ has the property that every continuous function $f: A \to \mathbb{R}$ attains its maximum on $A$, show that $A$ must be compact**.

    Idea:

    1. $A$ is bounded: use the fact that $f(a) = d(0,a)$ attains maximum;
    2. $A$ is closed: suppose not and $a$ being a limit point of $A$ that is not in $A$, consider $f(x) = d(x,a)$, it will never be zero, so $g(x) = 1/f(x)$ is continuous and well defined, so it attains maximum, so $f$ attains minimum that is not zero, but that implies $a$ is not a limit point.
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
    **For points $x,y \in \mathbb{R}^2 - \lbrace 0 \rbrace$ impose $x \sim y$ if and only if $x$ and $y$ lie on the same line through the origin of $\mathbb{R}^2$, show that $\mathbb{R}^2-\lbrace 0 \rbrace/\sim \cong S^1$**.

    Idea:

    Let $F:\mathbb{R}^2 - \lbrace 0 \rbrace \to S^1$ be the map $x \to x/\| x \|$, since we took $0$ out this map is continuous, thus by the universal mapping property of quotient topology, we have that the map $f:\mathbb{R}^2-\lbrace 0 \rbrace/\sim \to S^1, [x] \to x/\| x\|$ is continuous. It is also not hard to check it is bijection, and a bijective quotient map is always a homeomorphism.
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
    **Prove or give a counterexample, a smooth homeomorphism from one smooth manifold to another is a diffeomorphism**.

    Idea:

    Use $f:\mathbb{R} \to \mathbb{R}, x\mapsto x^3$.
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
    **Prove that the set $X$ of all non-zero $2 \times 2$ matrices $A$ such that $AA^t$ is diagonal is a sub-manifold of $\mathbb{R}^4 = M_{2 \times 2}(\mathbb{R})$, what is the dimension of $X$? Is $X$ compact**?

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
    **Prove there is no non-vanishing vector field on the sphere $S^2$. On what connected, closed, compact, orientable surfaces does a non-vanishing vector field exist? What about for surfaces with boundary**?

    Idea:

    If such vector field exists, the antipodal map on $S^2$ would be homotopic to the identity map on $S^2$ but that is not true.

    If the Euler Characteristic of a manifold is zero then it admits a non-vanishing vector field, for exam sake let me jump it here.
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
    **Suppose $Z_0$ and $Z_1$ are compact, cobordant, $p$-dimensional smooth sub-manifolds of a smooth manifold $X$, prove that $\int_{Z_0}w = \int_{Z_1}w$ for every closed $p$-form $w$ on $X$**.

    Idea:

    We did not really study cobordant in the course so I guess this should not be in our exam, nevertheless, here we go, first a definition:

    Two manifolds of the same dimension are cobordant if their disjoint union is the boundary of a compact manifold one dimension higher.

    Since they are cobordant, $\int_{Z_0 - Z_1}w = \int_X dw$, but $w$ is closed, so $= 0$, and we have the desired statement.
    """
    )
    return


if __name__ == "__main__":
    app.run()
