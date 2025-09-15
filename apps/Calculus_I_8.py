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
    mo.md(r"""# 2.3 Basic Differentiation Formulas""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Constant Function""")
    return


@app.cell
def _(mo):
    mo.md(r"""If $f(x) = c$, then $f$ is differentiable and $$f'(x) = 0.$$""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Power Function""")
    return


@app.cell
def _(mo):
    mo.md(r"""If $f(x) = x^r$ where $r$ is a real number, then $$f'(x) = rx^{r-1}.$$""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Sine and Cosine Function""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1.   If $f(x) = \sin(x)$, then $f'(x) = \cos(x)$;
    2.   If $f(x) = \cos(x)$, then $f'(x) = -\sin(x)$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Proof""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    If $f(x) = \sin(x)$, then $$\begin{aligned} f'(x) &= \lim\limits_{h \to 0} \frac{\sin(x + h) - \sin(x)}{h} \\ &=\lim\limits_{h \to 0}\frac{\sin(x)\cos(h)+ \cos(x)\sin(h) - \sin(x)}{h} \\ &=\lim\limits_{h \to 0}\left(\sin(x)\cdot\frac{\cos(h) - 1}{h} + \cos(x)\cdot\frac{\sin(h)}{h}\right) \\ &= \sin(x) \cdot 0 + \cos(x) \cdot 1 \\&= \cos(x)\end{aligned}$$ as desired. We used addition formula for sine, and the two important limits involving sine and cosine in the above proof.

    We can show that $\cos'(x) = -\sin(x)$ in a similar manner.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Basic Operations on Differentiation""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. If $f(x) = c\cdot g(x)$, $g$ is differentiable, then $f'(x) = c\cdot g'(x)$;
    2. If $f, g$ are differentiable, then $(f+g)'(x) = f'(x) + g'(x)$;
    3. If $f, g$ are differentiable, then $(f-g)'(x) = f'(x) - g'(x)$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    What is the derivative of $f(x) = (x+3)^2$?

    At the first glance, we cannot solve this problem with the basic rules. $f(x)$ is not a constant, it is not a power function, it is not sine or cosine, and it is not a result of basic operations - it is a composition of $g(x) = x+3$ and $f(x) = x^2$.

    However, if we expand $f(x)$, we get that $f(x) = x^2 + 6x + 9$ which is a summation of power functions and multiplication of constants, thus by the above rules, we get that $f'(x) = 2x + 6$.

    **Moral of the story: try to simplify the expression first before taking derivative**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Factorization and Expansion
        type: info

    In your previous math courses, 'simplify an expression' probably always means 'factor an expression' (i.e. we can factor $x^2 + 6x + 9$ to get $(x+3)^2$). But this is not the case anymore. 'Simplify' really means 'try to make following steps easier', and 'simplify an expression' can sometimes mean 'expand an expression' (i.e. we can expand $(x+3)^2$ to get $x^2+6x+9$).

    In above example, we expand the expression; in some other example, we probably will factor the expression. There is not really a rule here: if you are not sure what to do, try one way to see if you are making progress - and if you are not, don't give up, try the other way!

    ///
    """
    )
    return


if __name__ == "__main__":
    app.run()
