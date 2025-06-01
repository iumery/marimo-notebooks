import marimo

__generated_with = "0.13.15"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# Section A""")
    return


@app.cell
def _(mo):
    mo.md(r"""Solve $2$ of the $3$ problems below.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $G$ be a group of order $2^4\cdot 5^3 \cdot 11$, $H$ be a group of order $5^3 \cdot 11$. Prove $H$ has a normal Sylow $11$-subgroup. Suppose $n_5(G) < 16$, prove $G$ has a non-trivial normal subgroup of order divisible by $5$. Suppose $n_5(G) = 16$, use part 1 to prove $G$ has a normal (Sylow) $11$-subgroup**.

    Idea

    1. $1$ is the only number can divide $5^3$ and $\equiv 1 \pmod{11}$ thus $n_{11}(H) = 1$ and that Sylow $11$-subgroup is normal;
    2. Given $n_5(G) < 16$, it could be $1$ or $11$. If it is $1$ we are done. Otherwise consider $G$ acts on $N_G(S)$ where $S$ is a Sylow $5$-subgroup, this gives a homomorphism $\varphi:G \to S_{11}$. Now $| G/\ker{\varphi} |$ needs to divide $| G | = 2^4 \cdot 5^3 \cdot 11$ but also $| S_{11} | = 11!$. Notice that $11!$ has only two factors of $5$ come from $5$ and $10$, thus $| G/\ker{\varphi} |$ cannot have $5^3$ as a factor, so $\ker{\varphi}$ has $5$ as a factor;
    3. Let $S$ be a Sylow $5$-subgroup, we know then $N_G(S)$ is of index $16$ thus $| N_G(S) | = 5^3 \cdot 11$, so it has a normal $11$-subgroup $A$. Consider $N_G(A)$, since $A \lhd N_G(S)$ we must have that $N_G(S) \le N_G(A)$, in particular $[G:N_G(A)] | 16$. View $A$ as a Sylow $11$-subgroup of $G$, we know also that $[G:N_G(A)] \equiv 1 \pmod{11}$. Thus the only possibility is to have $[G:N_G(A)] = 1$ thus the normalizer of $A$ in $G$ is $G$ itself, thus $A$ is normal.
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
    **Let $G$ be a group of order $52$ with the following presentation**: $$\langle a,b | a^{13} = b^4 = 1, bab^{-1} = a^t \rangle.$$ **What is the correct value of $t$? What are the conjugacy classes of $G$? Write down the character table of $G$, show steps**.

    Idea

    This is a typical question about character table. The answer is $t = 8$ (or $5$ because $5\cdot 8 \equiv 1 \pmod{13}$). $G' = \langle a \rangle$ and $G$ has $7$ conjugacy classes, following not hard from the presentation. For character table, see [here](https://people.maths.bris.ac.uk/~matyd/GroupNames/1/C13sC4.html).
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
        r"""**A problem about linear group. Let $G = GL(n, \mathbb{F}_q)$ where $\mathbb{F}_q$ is a field of order $q = p^r$, $p$ is a prime. The first part asks what is the order of $G$ and what is the order of $U < G$ where $U$ is the subgroup of $G$ consists of upper triangular matrices with $1$ on the diagonal. Two more parts**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Section B""")
    return


@app.cell
def _(mo):
    mo.md(r"""Solve $2$ of the $3$ problems below.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **What is the definition of simple module? State and prove Schur's Lemma. Let $\rho$ be a representation of $G$, $g \in Z(G)$. What can you say about $\rho(g)$? Let $G$ be simple, $g \in G$ and $g \ne 1$, $V$ be a simple $\mathbb{C}G$-module with dimension $k$ and $\chi$ be the corresponding character, show that $| \chi(g) | < k$**.

    Idea

    For the definition and Schur's Lemma, see note. If $g \in Z(G)$ then $\rho(g) \in Z(GL(n, \mathbb{C}))$ where we know $Z(GL(n, \mathbb{C})) = \lbrace \lambda I | \lambda \in \mathbb{C}^{*} \rbrace$. If $G$ is simple then $Z(G)$ must be $1$, in particular $g \notin Z(G)$ thus $\rho(g) \ne \lambda I$, but we also know $| \chi(g) | \le k$ with equality holds if and only if $\rho(g) = \lambda I$, result follows.
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
        r"""**Let $F$ be a field, $R = F[x_1,\dots,x_n]$. Show that $I = (x_1-c_1,\dots,x_n-c_n)$ is a maximal ideal in $R$ for $c_i \in F$. Suppose $F$ is uncountable and $E$ is of finite type as an $F$-algebra (i.e. $E = R/I$), show that $E$ is an algebraic extension of $F$. State and prove Weak Nullstellensatz**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 6""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**A problem about Galois Theory. The first part asks to prove $\mathbb{Q}[2\cos(2\pi/7)]$ is Galois and compute the Galois group. The second part asks whether a certain polynomial is solvable by radical or not**."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Section C""")
    return


@app.cell
def _(mo):
    mo.md(r"""Solve the problem below.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Problem 7""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    **Let $K = \mathbb{Q}[\sqrt{-151}]$, $R = \mathbb{Z}[\sqrt{-151}]$. Show that $R$ is not a Dedekind domain and give a non-invertible fractional ideal. What is $O_K$ and what is the class group $\text{Cl}(K)$**?

    Idea

    This is a typical question about Dedekind domain we did a lot before. $2$ is singular prime. Since $-151 \equiv 1 \pmod{4}$ we know $O_K = \mathbb{Z}[\frac{1+\sqrt{-151}}{2}]$. Class group is $\mathbb{Z}_7$.
    """
    )
    return


if __name__ == "__main__":
    app.run()
