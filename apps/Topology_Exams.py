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
    mo.md(r"""# Fall Semester Midterm Practice""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1

    **Let $X$ be a topological space. Show that a set $A \subseteq X$ is open if and only if each $x \in A$ has an open neighborhood $U(x)$ such that $U(x) \subseteq A$**.

    Idea

    $(\implies)$ $U(x) = A$ is simply such an $U$;

    $(\impliedby)$ Claim and show that $\displaystyle A = \bigcup\limits_{x \in A}U(x)$, then it is union of open sets thus open.

    ## Problem 2

    **If $L$ is a straight line in the plane, describe the topology that $L$ inherits as a subspace of $\mathbb{R}_a \times \mathbb{R}$ where $\mathbb{R}_a$ stands for the real line with the anti-discrete topology**.

    Idea

    Only open set in $\mathbb{R}_a$ is $\varnothing$ and $\mathbb{R}$. In case of $\varnothing$ then the topology $L$ inherits is $\varnothing$; Otherwise it is either an open interval or $\mathbb{R}$.

    ## Problem 3

    **The function $f: \mathbb{R} \rightarrow \mathbb{R}^{\omega}$ is given by the formula $f(t) = (t, 2t, 3t, \dots)$. Prove or disprove**:

    1. $f$ **is continuous if $\mathbb{R}^{\omega}$ is given the product topology**;
    2. $f$ **is continuous if $\mathbb{R}^{\omega}$ is given the uniform topology**.

    Idea

    1. Yes, because each $c t$ is continuous;
    2. No, because $c t$ is unbounded.

    ## Problem 4

    **Let $(X, d)$ be a metric space, and $a \in X$ a fixed point. Prove that the function $f: X \rightarrow \mathbb{R}$ given by $f(x) = d(x, a)$ is continuous**.

    Idea

    An open set containing $d(x, a)$ has the form $(d(x, a) - r, d(x, a) + r)$, then $B_d(x, r/2)$ is open in $X$ such that $f(B_d(x, r/2)) \subseteq (d(x, a) - r, d(x, a) + r)$.

    ## Problem 5

    **Let $(X, d)$ be a metric space, $A \subseteq X$ and $x \in X$. Prove that $x$ is in the closure of $A$ if and only if there is a sequence $x_n \in A$ which converges to $x$**.

    Idea

    $(\implies)$ pick $x_i$ be a point in $A \cap B_d(x, 1/i)$ then it is a sequence converge to $x$;

    $(\impliedby)$ for any $U(x)$ by definition it contains infinitely many $x_n$'s that is in $A$.

    ## Problem 6

    **Consider the sequence $a_n = 1/n, n \in \mathbb{Z}_+$ of points on the real line $\mathbb{R}$. With respect to which of the following topologies does $a_n$ converge? When it does, what is the limit**?

    1. $\mathbb{R}_K$;
    2. $\mathbb{R}_l$;
    3. **The finite complement topology**.

    Idea

    1. Not converge, because $K = \lbrace a_n \rbrace$ is simply not included in (some) open sets in $\mathbb{R}_K$;
    2. Converge to $0$;
    3. Converge to all $r \in R$.

    ## Problem 7

    **Let $X$ be a topological space, and suppose that $X$ is Hausdorff**:

    1. **Prove that any subspace $A \subseteq X$ is Hausdorff**;
    2. **Prove that a quotient space $X/ \sim$ need not to be Hausdorff**.

    Idea

    1. For any $x, y$ and $U(x), U(y)$ disjoint open sets in $X$, $U(x) \cap A, U(y) \cap A$ are disjoint open sets in $A$;
    2. $\mathbb{R}/ \mathbb{Z} \cong S^1$ is Hausdorff; $\mathbb{R}/ \mathbb{Q}$ is not.

    ## Problem 8

    **Describe all continuous functions $f: \mathbb{R} \rightarrow \mathbb{R}_l$**.

    Idea

    $\mathbb{R}_l$ is totally disconnect. If $f$ is continuous then it maps connected space to connected space thus $f(\mathbb{R})$ is connected, thus $f(\mathbb{R})$ can only be a single point, i.e. $f$ is constant.

    ## Problem 9

    **Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be a continuous function and $\Gamma_f = \lbrace (x, f(x)) \rbrace$ its graph. Prove that $\Gamma_f$ is closed and connected**.

    Idea

    1. Closed: any point $(x, y), y \ne f(x)$ is not in the closure of $\Gamma_f$;
    2. Connected: consider $g: \mathbb{R} \rightarrow \mathbb{R}^2$ given by $g(x) = (x, f(x))$ then $g$ is continuous and the graph is simply the image of $g$ and is thus connected.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Midterm Exam""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1

    **Let $X$ be a topological space and $A_{\alpha} \subset X$ a family of subsets. Prove that** $$\bigcup_{\alpha}\overline{A_{\alpha}} \subset \overline{\bigcup_{\alpha}A_{\alpha}}$$ **and give an example where equality fails**.

    ## Problem 2

    **Let $X$ be a topological space and let $X \times X$ have product topology. Define the diagonal map $\Delta: X \to X \times X$ by the formula $\Delta(x) = (x,x)$ for $x \in X$**.

    1. **Prove that the diagonal map $\Delta$ is continuous**;
    2. **Prove that $X$ is Hausdorff if and only if the image of $\Delta$ is closed**.

    ## Problem 3

    **Let $S^1$ be the unit circle in complex plane. Define the equivalence relation on $S^1$ by $z \sim w$ if and only if $z =w$ or $z = -w$. Prove that the quotient space $S^1/\sim$ is homeomorphic to $S^1$**.

    ## Problem 4

    **Let $X$ be a topological space and $f_n: X\to \mathbb{R}$ a sequence of continuous functions. Let $x_n \in X$ be a sequence of points in $X$ converging to $x \in X$. Prove that if the sequence $(f_n)$ converges uniformly to $f$, then the sequence $(f_n(x_n))$ converges to $f(x)$**.

    ## Problem 5

    **Let $X$ be a topological space and $f, g: X \to [0,1]$ continuous functions. Suppose that $X$ is connected and $f$ is surjective. Prove that there must be a point $x \in X$ such that $f(x) = g(x)$**.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Final Exam""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1

    **Let $X$ and $Y$ be metric spaces and $f, g: X\to Y$ continuous maps. Suppose that $f = g$ on a subset $A \subset X$ which is dense in $X$. Prove that then $f =g$ on the entire $X$**.

    ## Problem 2

    **Prove that a subspace $A \subset \mathbb{R}^n$ is compact if and only if every continuous function $f: A \to \mathbb{R}$ attains its maximum on $A$**.

    ## Problem 3

    **Prove that every compact Hausdorff space $X$ is regular**.

    ## Problem 4

    **Let $\{x_n\}$ and $\{y_n\}$ be Cauchy sequences in a metric space $(X,d)$. Prove that the sequence of real numbers $\{d(x_n,y_n)\}$ converges**.

    ## Problem 5

    **Let $(X,d)$ be a complete metric space**.

    1. **Prove that if $X$ is totally bounded then it is sequentially compact**;
    2. **Will the conclusion of part 1 necessarily hold if $X$ is bounded? Justify your answer**.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Midterm Practice""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 1

    **Give the definition of a smooth manifold, prove that $X = \lbrace (x, y) \in \mathbb{R}^2 \| x | + | y | = 1 \rbrace$ is not a smooth manifold**.

    Idea

    1. $X$ is an $n$-manifold if for any $p \in X$ there is an neighborhood of $p$, namely $O(p)$, diffeomorphic to some open set $U \subseteq \mathbb{R}^n$;
    2. If one want to define $dr$ at the vertices, since the direction approaching from different sides are different, one must have $r' = 0$, but then it cannot be a diffeomorphism.

    ## Exercise 2

    **Give an example of a smooth homeomorphism between smooth manifold which is not a diffeomorphism**.

    Idea

    $f(x) = x^3$ is such an example, the idea is the same as above, at zero we have $f' = 0$.

    ## Exercise 3

    **Let $f: \mathbb{R}^2 \to \mathbb{R}^2$ be given by $f(x, y) = (x,y-y^2-x^2)$**.

    1. **Prove that $f$ is a local diffeomorphism at the origin**;
    2. **Find a local inverse for $f$ at the origin**;
    3. **Find a point $p \in \mathbb{R}^2$ such that $f$ is not a local diffeomorphism at $p$**.

    Idea

    1. $x \mapsto x$ is clearly a smooth bijection with smooth inverse; for $y$, essentially we want to prove $y - y^2$ is injective: we solve for $y_0 - y_0^2 = y_1 - y_1^2$ then either $y_0 = y_1$ or $y_0 = 1-y_1$, take a small interval, for example, $x, y < 1/2$, then $y - y^2$ is injective (Or more easily we may use Inverse Function Theorem here, but I do prefer the above one, as I think it has a more smooth connection with the next sub-question);
    2. The first coordinate works trivially; the second coordinate, we want to find the inverse of $z = y - y^2 - x^2$, i.e. to get $y = g(z)$, viewing $x$ as a constant. Remember we have that $y<1/2$ and realize that essentially we are solve an quadratic equation here, so that $y = \frac{1\pm\sqrt{1-4(x^2+z)}}{2}$, since $y < 1/2$ we take $-$ here;
    3. By above, we can notice that $1/2$ is a (the) critical point (of the parabola), so take $p = (0,1/2)$ then $f$ is not a local diffeomorphism (not bijective) at $p$.

    ## Exercise 4

    **Let $X$ consists of all $2\times 2$ real matrices $A$ such that $\det{A} = 1$ and $AA^T$ is diagonal**.

    1. **Describe $X$ as the solution set of two equations in four variables**;
    2. **Show that $X$ is a manifold, what is its dimension**?
    3. **Calculate the tangent space to $X$ at the identity matrix $E$**;
    4. **Is $X$ a Lie group with respect to the usual matrix multiplication**?

    Idea

    1. Let $A = \begin{pmatrix} a&b\\c&d \end{pmatrix}$ then by $\det{A} = 1$ we have $ad-bc = 1$ and by $AA^T = 0$ we have $ac+bd = 0$;
    2. Consider the function $f:\mathbb{R}^4 \to \mathbb{R}^2, (a,b,c,d) \mapsto (ad-bc,ac+bd)$, we want to show that $(1,0)$ is a regular value. So we need to calculate $df_M(N)$ where $M \in X$ and $N$ is some arbitrary $2 \times 2$ matrix, by definition this equals $\lim\limits_{t \to 0}\frac{f(M+tN) - f(M)}{t}$, expand everything, remember that $f(M) = (1,0)$, and it is not hard to get the limit equals $(aD+dA-cB-bC, aC+cA+bD+dB)$ (where $M =\begin{pmatrix} A&B\\C&D \end{pmatrix}, N =\begin{pmatrix} a&b\\c&d \end{pmatrix}$), for fixed $A,B,C,D$ and arbitrary $a,b,c,d$ this is surjective, thus by preimage theorem $X$ is manifold of dimension $4-2= 2$;
    3. For $E$, $A, D = 1, B,C = 0$ thus the derivative becomes $(a+d, b+c)$, and the tangent space equals $\ker{df_E} = \lbrace a,b,c,d | a+d = 0, b+c = 0\rbrace$;
    4. Essentially we need to check if multiplication is internal, and $A^{-1}$ is in the set, because everything else inherit from the fact that we are using usual multiplication as the operation: if $A, B \in X$ then $\det{AB} = \det{A}\det{B} = 1$ and $AB(AB)^T = ABB^TA^T$, expand this and one should see that the the off-diagonal terms may not be zeroes, so the set with matrix multiplication does not form a group.

    ## Exercise 5

    **Prove that any submersion $f: X \to Y$ of smooth manifolds is an open map**.

    Idea

    By local submersion theorem $f$ is (locally) equivalent with projection map, which is open: $\pi: X \times Y \to X$ be the projection map, any open set in $X \times Y$ has by definition the form $\cup (U \times V)$ where $U, V$ open in $X, Y$ respectively, then $\pi(\cup (U \times V)) = \cup (\pi(U \times V)) = \cup U$ is open.

    ## Exercise 6

    **What does it mean that a manifold is contractible? Show that any contractible manifold is connected**.

    Idea

    1. $X$ is contractible if $\text{id}:X\to X$ is homotopic to a constant map $c: X\to X, x \to c$. $X$ is contractible if and only if all smooth map from an arbitrary manifold $Y$ to $X$ are homotopic;
    2. For any $x \in X$, by definition there is a homotopy $F(x,t)$ where $F(x,0) = \text{id}(x) = x$ and $F(x,1) = c$, i.e. there is a (smooth) path from $x$ to $c$. For any $x, y$, find the path from $x$ to $c$ and $y$ to $c$, connect them together we have a path from $x$ to $y$, thus $X$ is (path-) connected.

    ## Exercise 7

    **Let $X$ be a smooth manifold of dimension $n$, prove that any smooth map $f:X \to S^m$ such that $n < m$ is homotopic to a constant map**.

    Idea

    By (mini-) Sard, $f(X)$ has measure zero in $S^m$ thus we have some $\lbrace x \rbrace \notin S^m$, consider the stereographic projection $g: S^m - \lbrace x \rbrace \to \mathbb{R}^m$ and that $g \circ f:X\to S^m-\lbrace x \rbrace \to \mathbb{R}^m$, since $\mathbb{R}^m$ is contractible $g\circ f$ is homotopy to any smooth map $r: X \to \mathbb{R}^m$, in particular $c: X \to \mathbb{R}^m, x \to c$. Compose $g \circ f$ with $g^{-1}$ and we are done.

    ## Exercise 8

    **Let $TX$ be the tangent bundle to a smooth compact manifold $X$, prove that the map $f: X \to TX$ given by the formula $f(x) = (x, 0)$ is an embedding**.

    Idea

    Choose local parametrization $$\begin{CD}O(p) @>f>> O(p) \times \mathbb{R}^n \\@ArAA @AAsA \\ U @>h>> U \times \mathbb{R}^n \end{CD}$$ where $s(u,v) = (r(u), dr_u(v))$, then $h(u) = (u, 0)$, hence $h$ is an immersion, thus so is $f$. Since $f$ is injective and $X$ is compact, $f$ is an embedding.

    ## Exercise 9

    1. **Give the definition of a manifold with boundary**;
    2. **Let $X$ be compact manifold with boundary, show that its boundary $\partial X$ is compact**;
    3. **Find an example in which $\partial X$ is compact and $X$ is not**.

    Idea

    1. $X$ is an $n$-manifold if for any $p \in X$ there is an neighborhood of $p$, namely $O(p)$, diffeomorphic to some open set $U \subseteq \mathbb{R}^n_+$;
    2. We know that $\partial X$ is closed; if $X$ is compact then $X$ is bounded, thus clearly so does $\partial X$, thus $\partial X$ is closed and bounded in $\mathbb{R}^n$ thus compact;
    3. $[0,1)$ where $\partial X = \lbrace 0 \rbrace$ is finite thus compact; half open interval is clearly not compact.

    ## Exercise 10

    **Let $f: S^2 \to \mathbb{R}^2$ be a smooth map an $y \in \mathbb{R}^2$ its regular value, prove that the number of points in $f^{-1}(y)$ is even**.

    Idea

    Since $\mathbb{R}^2$ is not compact but $f(S^2)$ must be compact, $f$ is not surjective, thus $\# f^{-1}(y) = 0$ mod $2$.

    ## Exercise 11

    **Show that there is a complex number $z \in \mathbb{C}$ such that $z^2 = (1+iz)e^{-| z |^2}$**.

    Idea

    Can be solved with Rouché's Theorem.

    Professor said that the intention was to have $z^3$ instead of $z^2$, in that case, the degree mod $2$ being $1$ implies the result.

    ## Exercise 12

    **Let $S^n \subseteq \mathbb{R}^{n+1}$ be the unit sphere $| x | = 1$ and $f: S^n \to S^n$ a smooth map such that $f(-x) = f(x)$, show that $\deg_2{f} = 0$ mod $2$**.

    Idea

    If $f$ is not surjective then automatically $\deg_2{f} = 0$, otherwise if $x \in f^{-1}(q)$ then by assumption $-x$ is also in $f^{-1}(q)$, $x \ne -x$ unless $x = 0$, but $0 \notin S^n$. Thus preimage of $q$ always come in pairs, i.e. the number of them $= 0$ mod $2$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Midterm Exam""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1

    **Let $X$ and $Y$ be smooth manifolds, not necessarily compact, and $f: X \to Y$ a smooth map. Prove that the map $F:X\to X \times Y$ given by $F(x) = (x,f(x))$ is an embedding whose image is the graph of $f$**.

    ## Problem 2

    **The orthogonal group $O(n) \subset M_n(\mathbb{R})$ consists of all real $n \times n$ matrices $A$ such that $AA^T = E$, where $E$ is the identity matrix**.

    1. **Prove that $O(n)$ is a group**;
    2. **Prove that $O(n)$ is a smooth manifold and find its dimension**;
    3. **Calculate the tangent space $T_AO(n) \subset M_n(\mathbb{R})$ for an arbitrary $A \in O(n)$**;
    4. **Prove that $O(n)$ is compact**;
    5. **Prove that $O(n)$ is not connected**.

    ## Problem 3

    **Let $f, g: S^n \to S^n$ be smooth maps such that $g(x) \ne -f(x)$ for any $x \in S^n$. Prove that $f$ and $g$ are homotopic**.

    ## Problem 4

    **Let $W$ be a compact connected $(n+1)$-manifold with boundary $\partial W = X \cup Y$ consisting of two path components, $X$ and $Y$. Prove that, for any smooth map $F: W \to Z$ to a connected $n$-manifold $Z$, the maps obtained by restricting $F$ to the boundary components $X$ and $Y$ have the same $\pmod{2}$ degree**.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Final Exam""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1

    **Find the critical values of the smooth function $f: \mathbb{R}^2 \to \mathbb{R}$ given by the formula** $$f(x,y,z) = x^3+xy+y^3+1.$$

    ## Problem 2

    **Let $C \subset \mathbb{R}^3$ be the cylinder $x^2 + y^2 = 1$. Determine if the following vector fields are tangent to $C$**:

    1. **$F = (x^2-1)i + xyj + xzk$**;
    2. **$F = xi + yj + 2xz^2k$**.

    ## Problem 3

    **Let $f,g: S^n \to S^n$ be smooth functions. Prove that if $|\deg(f)| \ne |\deg(g)|$ then there exists a point $x \in S^n$ such that the vectors $f(x)$ and $g(x)$ are orthogonal to each other. *Hint: try the straight line homotopy $(1-t)\cdot f(x) + t\cdot g(x), t \in [0,1]$***.

    ## Problem 4

    **Let $M \subset \mathbb{R}^3$ be an embedded $2$-manifold bounding a compact region in $\mathbb{R}^3$. Orient $M$ outward. Suppose that $M$ intersects the coordinate $xy$-plane transversally in the curve $x^2 + y^2 = 2$, and denote by $M_1$ the portion of $M$ above the $xy$-plane. Let** $$w = (x^2 + y^2)dx \wedge dy + x^2ydy\wedge dz+ xy^2dx \wedge dz.$$

    1. **Evaluate $dw$**;
    2. **Use Stokes' Theorem to evaluate $\int_{M_1}w$**.

    """
    )
    return


if __name__ == "__main__":
    app.run()
