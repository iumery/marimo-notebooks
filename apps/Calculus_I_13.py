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
    mo.md(
        r"""
    /// admonition | MTH 161
        type: danger

    2.8 is part of MTH 151 curriculum, but not in MTH 161.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# 2.8 Linear Approximation""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Linear Approximation""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Recall the definition of derivative of $f$ at a point $a$ is given by $$f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}.$$ This means that $$f'(a) \approx \frac{f(x) - f(a)}{x - a}, \text{ if }x\text{ is close to }a.$$ Rearrange this expression, we get $$f(x) \approx f(a) + f'(a)(x-a),$$ again given that $x$ and $a$ are close.

    We denote the RHS as $L(x)$ or $L_f(x,a)$, and it is called the linearization of $f$ at $a$, it is a function of $x$. $L(x)$ is the linear approximation of $f(x)$ for $x$ close to $a$. It is also called the tangent linear approximation: since the expression of $L(x)$ is given by $$L(x) = f(a) + f'(a)(x-a)$$ where $a, f(a), f'(a)$ are all constant, the graph of $L(x)$ is a straight line, passing the point $(a, f(a))$ which is on the graph of $f(x)$, and has slope $f'(a)$. Thus $L(x)$ is exactly the tangent line of the graph of $f(x)$ at $x = a$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Use linear approximation to approximate $\sin(0.1)$.

    We approximate $\sin(0.1)$ by sine at $0$. By the above formula, $$f(x) \approx L(x) = \sin(0) + \sin'(0)(x - 0) = \cos(0)x = x$$ if $x$ is close to $a$. In particular, $f(0.1) \approx 0.1$.

    Use a calculator, we can check that $$\sin(0.1) \approx 0.0998334…,$$ so our approximation is pretty good.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Non-Example""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Approximate $\sin(\pi)$ using the linearization of $f$ at $0$.

    By above, if we do the linearization at $0$, we get $f(x) \approx x$, thus $$\sin(\pi) \approx \pi \approx 3.1415926…,$$ but we know $\sin(\pi) = 0$. The approximation is pretty bad because $\pi$ is not considered 'close to $0$'. However, there is no general way to indicate which $x$'s are considered "close to $a$" for a given $a$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Use linearization of $$f(x) = (1+x)^p$$ to approximate $\sqrt{0.99}$.

    Use the formula, we get, when $x$ is close to $0$, $$f(x) \approx L(x) = (1+0)^p + f'(0)(x - 0) = 1 + px.$$ In our case, we plugin $x = -0.01$, $p = \frac{1}{2}$ so that $$f(-0.01) = \sqrt{1-0.01} = \sqrt{0.99}.$$ The linear approximation gives $$f(x) \approx 1 - \frac{1}{2}0.01 = 0.995.$$ A calculator will tell us $\sqrt{0.99} \approx 0.994987…$, so again we get a pretty good approximation.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Differential Approximation""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Recall again we have the definition of derivative $$f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a},$$ with Leibniz notation we can write it as $$\frac{dy}{dx} = f'(x).$$ Notice here $dy$ and $dx$ are merely notations, we can think $dx$ as a variable (that is independent from $x$) and $dy$ is a function of $dx$ and $x$. We can write the above expression as $$dy = f'(x)dx,$$ and $dy$ is known as the differential of $y$.

    Differentials can be used to estimate the change in the value of a function resulting from a small change in input values. Consider a function $f$ that is differentiable at $a$. Suppose the input is changed by a small amount, and we want to find how much is the output changed.

    Suppose $x$ is changed from $a$ to $a + dx$, so that the change is $dx$ (or denoted as $\Delta x$), then the change in $y$ is given by $$\Delta y = f(a + dx) - f(a)$$ (this is not approximation). Instead of calculating the actual change in $y$, it is often easier to approximate the change in $y$ using a linear approximation. By above, $$f(x) \approx L(x) = f(a) + f'(a)(x-a),$$ if $dx$ is small, then we have $$f(a+dx) \approx L(a + dx) = f(a) + f'(a)(a+dx - a),$$ rearrange we get $$f(a+dx) - f(a) \approx f'(a)dx,$$ but LHS is exactly $\Delta y$, and RHS is $dy$ as discussed above, thus $$\Delta y \approx dy = f'(a)dx.$$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""<img src="public/Pasted image 20220315182352.png" width="600" />""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose $y = x^2 + x$, compute and compare $\Delta y$ and $dy$ at $x = 5$ with $dx = 0.1$.

    The actual change of $y$ from $x = 5$ to $x = 5.1$ is $$\Delta y = 5.1^2 + 5.1 - 5^2 - 5 = 1.11.$$ The approximation $$dy = f'(a)dx = f'(5)\cdot 0.1 = 11 \cdot 0.1 = 1.1.$$ The difference is $0.01$, which is pretty good.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose we have a container of a shape of semi-sphere. We measure the radius of the (large circle of the) container to be $1$ meter, but the measure is not exact, that the actual radius is $1 \pm 0.01$ meters. Use differentials to estimate the error in the computed volume of the container.

    The volume of the container is given by $$V = \frac{1}{2} \cdot \frac{4}{3} \pi r^3 = \frac{2}{3}\pi r^3,$$ which is a function depends on $r$. By the formula, $$\Delta V \approx dV = 2\pi r^2dr = \pm 0.02 \pi.$$ The actual possible error is $$\Delta V = f(1 \pm 0.01) - f(1) = 0.0202007 \pi, \text{ or }-0.0198007\pi.$$
    """
    )
    return


if __name__ == "__main__":
    app.run()
