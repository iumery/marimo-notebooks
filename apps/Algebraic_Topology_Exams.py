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
    mo.md(r"""# Fall Semester Midterm Exam""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Problem 1

    **Let $X$ be the solid triangle $\Delta PQR$ with identifications of all three oriented edges as $\overrightarrow{PQ} = \overrightarrow{QR} = \overrightarrow{RP}$**.

    1. **Find a $\Delta$-complex structure on $X$**;
    2. **Using this $\Delta$-complex structure, compute the simplicial homology groups of $X$**.

    ## Problem 2

    **Assume $X$ retracts to a subspace $A \subset X$**.

    1. **Show that a retraction $r: X \to A$ induces a surjection $r_*:H_n(X) \to H_n(A)$**;
    2. **Prove that if $X$ is contractible, then $A$ is also contractible**.

    ## Problem 3

    **Let $X$ be the theta graph, i.e. the graph homeomorphic to the union of a circle and a diameter. Prove the following**:

    1. **$X$ retracts to any point $x \in X$**;
    2. **$X$ does not deformation retract to any point $x \in X$**;
    3. **$CX$, the cone on $X$, deformation retracts to any point $x$ in its base $X$**.

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

    **Let $X$ be the space obtained by attaching two $2$-cells to $S^1$ so that the one attaching map has degree $a$ and the other has degree $b$**.

    1. **Compute the homology and cohomology groups of $X$**;
    2. **Compute the homology and cohomology groups of $X$ with $\mathbb{Z}_2$ coefficients**.

    ## Problem 2

    **Let $Y$ be the space obtained by gluing the two ends of $S^1 \times I$ together via a map $S^1 \to S^1$ of degree $d > 0$. Use Mayer-Vietoris to calculate the homology of $Y$**.

    ## Problem 3

    **Let $M$ be a compact connected $3$-manifold with boundary $S_0 \sqcup S_1 \subset \partial M$. Suppose $M$ retracts to $S_0$**.

    1. **Show that $H_2(M) = H_2(S_0) \oplus H_2(M,S_0)$**;
    2. **Suppose $H_2(M,S_0) = 0$. Show that the retraction must induce an isomorphism $H_2(S_1) \to H_2(S_0)$**;
    3. **Show that there is no retraction from the solid torus minus an open ball to its torus boundary component**.

    ## Problem 4

    **Let $W$ be the $\Delta$-complex obtained from one $2$-simplex whose three edges are all identified**.

    1. **Compute the simplicial cohomology of $W$ with coefficients in $\mathbb{Q}$**;
    2. **Regard $W$ as a topological space, compute the local homology of the vertex**.

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

    **Let $p$ and $q$ be points in a path connected topological space $X$. Let $u$ and $w$ be paths from $p$ to $w$. Then we have isomorphisms $\beta_u$ and $\beta_w$ from $\pi_1(X,p)$ to $\pi_1(X,q)$. Under what conditions on $u$ and $w$ are these the same isomorphisms? That is, discuss what must hold true about the paths $u$ and $w$ if $\beta_u([\gamma]) = \beta_w([\gamma])$ for every $[\gamma] \in \pi_1(X,p)$**.

    ## Problem 2

    **Given an embedding $f: S^1 \times D^2 \to S^3$, let $V$ be its image. Let $X = S^3 - \text{int}(V)$ be the complement of its interior. Compute the homology groups $H_*(X;\mathbb{Z})$ and $H_*(X,\partial X; \mathbb{Z})$**.

    ## Problem 3

    **Show that $S^1 \times S^2$ and $S^1 \vee S^2 \vee S^3$ have isomorphic cohomology groups. Are they homotopy equivalent? Explain why or why not**.

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

    **Let $X$ be the CW-complex obtained from two copies of the Möbius band by identifying their boundary circles with some orientation via a map $f$ of degree $n$. Calculate $\pi_1(X,x)$ for some base point $x$**.

    ## Problem 2

    **Let $\Sigma_g$ be a closed orientable surface of genus $g$, the connected sum of $g$ tori $T^2$. Recall that for $g \ge 2$, the universal cover of $\Sigma_g$ is the hyperbolic plane, which is homeomorphic to $\mathbb{R}^2$**.

    1. **Show that any continuous map $f: \mathbb{R}P^2 \to \Sigma_3$ must be homotopic to a constant map**;
    2. **Describe a map $T^2 \to \Sigma_3$ that is not homotopic to a constant map. Prove that it is not homotopic to a constant map**;
    3. **For which $g$ does $\Sigma_g$ cover $\Sigma_3$? Describe the covering maps**.

    ## Problem 3

    **Let $M$ be a compact oriented closed manifold of dimension $2k$. Prove that if $H_{k-1}(M;\mathbb{Z})$ is torsion-free, then the group $H_k(M;\mathbb{Z})$ is also torsion-free**.

    ## Problem 4

    **Let $Y = S^2 \times \mathbb{R}P^3$ and $Z = S^3 \times \mathbb{R}P^2$. Let $y \in Y$ and $z \in Z$ be base points**.

    1. **Compute $\pi_1(Y,y)$ and $\pi_1(Z,z)$**;
    2. **Show that $\pi_k(Y,y) = \pi_k(Z,z)$ for all integers $k \ge 1$**;
    3. **Are these spaces homotopy equivalent? Justify your answer**.

    """
    )
    return


if __name__ == "__main__":
    app.run()
