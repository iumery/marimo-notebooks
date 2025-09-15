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
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Compute the fundamental group and homology groups of the topological space obtained by removing the three coordinate axes from $\mathbb{R}^3$**.

    Idea

    This space is homotopic with $S^2$ with $6$ points removed, or $\bigvee\limits_5 S^1$.
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
    **Let $X$ be a topological space, let $A \subset X$ be its retract. Prove that $H_*(X) \cong H_*(A) \oplus H_*(X, A)$**.

    Idea

    $A \subset X$ being a retract means we can obtain a short exact sequence $$0 \to H_*(A) \to H_*(X) \to H_*(X, A) \to 0.$$ By Splitting Lemma, this sequence splits.
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
    **The topological space $X$ is obtained by attaching a Möbius band $M$ to the projective plane $\mathbb{R}P^2$ via a homeomorphism of the boundary circle of $M$ to the standard $\mathbb{R}P^1$ in $\mathbb{R}P^2$**.

    1. **Compute $\pi_1(X)$**;
    2. **Compute $H_*(X)$ and $H^*(X)$**;
    3. **Compute $H_*(X;\mathbb{Z}_2)$ and $H^*(X; \mathbb{Z}_2)$**.

    Idea

    By Seifert-Van Kampen Theorem, $\pi_1(X) = \langle a, b | b^2 = 1, a^2 = b \rangle$ $\cong \langle a | a^4 = 1 \rangle$ $\cong \mathbb{Z}_4$. $H_1(X)$ is abelianization of $\mathbb{Z}_4$ which is also $\mathbb{Z}_4$. $H_0(X)$ is of course $\mathbb{Z}$. Use Mayer-Vietoris Sequence to get $H_2(X) = 0$. Use definition of cohomology and Universal Coefficient Theorem to find the others.
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
    **Let $X$ be a closed connected orientable $4$-manifold whose second homology group $H_2(X)$ has rank $1$. Prove that there does not exist a free action of the group $\mathbb{Z}_2$ on $X$**.

    Idea

    Rank of $H_4(X)$ is $1$ because $X$ is orientable, rank of $H_0(X)$ is $1$ because $X$ is connected. Rank of $H_3(X)$ and $H_1(X)$ are equal due to Poincaré duality. Since $H_2(X)$ has rank $1$, $\chi(X)$ must be odd. But free action on $\mathbb{Z}_2$ gives a covering space $X \to X/\mathbb{Z}_2$ so $\chi(X) = 2\chi(X/\mathbb{Z}_2)$, contradiction.
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
    **Let $f: X \to Y$ be a continuous map between two closed connected oriented $n$-manifolds such that $\deg(f) = 1$. Prove that the induced homomorphism $f_*: \pi_1(X) \to \pi_1(Y)$ is surjective**.

    Idea

    $f_*(\pi_1(X))$ is a subgroup of $\pi_1(Y)$, so we have $p: \tilde{Y} \to Y$ corresponds to $f_*(\pi_1(X))$ (i.e. $p_*(\pi_1(\tilde{Y})) = f_*(\pi_1(X))$). Map Lifting Property implies that there exists $\tilde{f}$ such that $f = \tilde{f} \circ p$ so $\deg(f) = \deg(\tilde{f}) \cdot \deg(p)$. Since $\deg(f) = 1$, $\deg(p)$ must be $\pm 1$ thus $p$ is a homeomorphism. In particular, $f_*(\pi_1(X)) = p_*(\pi_1(\tilde{Y})) = \pi_1(Y)$, meaning $f_*$ is surjective.
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
    **Let $\Sigma_g$ be a closed connected orientable surface of genus $g \ge 1$**.

    1. **Prove that $\pi_k(\Sigma_g) = 0$ for $k \ge 2$**;
    2. **Use part 1 to prove that $\pi_1(\Sigma_g)$ is not isomorphic to a free group**.

    Idea

    The first part is because $\mathbb{R}^2$ is the universal cover of $\Sigma_g$ and is contractible. In particular, $\Sigma_g$ is a $K(\pi_1(\Sigma_g), 1)$. We also know $\bigvee_nS^1$ is $K(F_n, 1)$. If $\pi_1(\Sigma_g) \cong F_n$ then $\Sigma_g \cong \bigvee_nS^1$ which is not.
    """
    )
    return


if __name__ == "__main__":
    app.run()
