import marimo

__generated_with = "0.13.6"
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
    mo.md(r"""# 2.4 The Product and Quotient Rules""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Product Rule""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""If $h(x) = f(x) \cdot g(x)$, then $$\boxed{h'(x) = f(x) g'(x) + f'(x) g(x)}.$$"""
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
    Differentiate $f(x) = x^3\cdot\cos(x)$.

    By the product rule, we have $f'(x) = (x^3)' \cos(x) + x^3\cos'(x)$ $=3x^2\cos(x) - x^3\sin(x)$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Quotient Rule""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""If $\displaystyle h(x) = \frac{f(x)}{g(x)}$, then $$\boxed{h'(x) = \frac{g(x)f'(x) - f(x)g'(x)}{g^2(x)}}.$$"""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Remark""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Unlike product rule (we have an addition), in the quotient rule we have a subtraction on the numerator, thus it **does matter** which one of $g(x)f'(x)$ and $f(x)g'(x)$ is at the front.

    One way to remember the correct way, is to **remember you should first write down denominator of the original function, $g$**, to get
    $$\frac{g(x)~~~~~~~~~~~~~~~~~~~~~~~~~~~~}{g^2(x)},$$ now it should be easy to write down the rest, because the numerator should be 'a function times a derivative, minus a(nother) function times a derivative', and we get $$\frac{g(x)f'(x) - f(x)g'(x)}{g^2(x)}.$$
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
    Differentiate $\displaystyle f(x) = \frac{x^6 - 2x^3 + 5}{x^2}$.

    By the quotient rule, we have $\displaystyle f'(x) = \frac{x^2(x^6-2x^3+5)' - (x^6-2x^3+5)(x^2)'}{(x^2)^2}$ $\displaystyle = \frac{(x^2)(6x^5-6x^2) - (x^6-2x^3+5)(2x)}{x^4}$ $\displaystyle = \frac{6x^7 - 6x^4 - 2x^7 + 4x^4 - 10x}{x^4}$ $\displaystyle = \frac{4x^6-2x^3-10}{x^3}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Derivatives of Trigonometric Functions""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $\sin'(x) = \cos(x)$;
    2. $\cos'(x) = -\sin(x)$;
    3. $\tan'(x) = \sec^2(x)$;
    4. $\csc'(x) = -\csc(x)\cot(x)$;
    5. $\sec'(x) = \sec(x)\tan(x)$;
    6. $\cot'(x) = -\csc^2(x)$.

    After we derived the derivatives for $\sin(x)$ and $\cos(x)$, we can get the other formulas from product and quotient rules, for example: $\displaystyle \tan'(x) = \left(\frac{\sin(x)}{\cos(x)}\right)'$ $\displaystyle = \frac{\cos(x)\sin'(x) - \sin(x)\cos'(x)}{\cos^2(x)}$ $\displaystyle = \frac{\cos^2(x)+ \sin^2(x)}{\cos^2(x)}$ $\displaystyle = \frac{1}{\cos^2(x)}$ $= \sec^2(x)$.
    """
    )
    return


if __name__ == "__main__":
    app.run()
