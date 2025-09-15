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
    mo.md(r"""# 2.5 The Chain Rule""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Motivation""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The basic differentiation rule, product rule and quotient rules are helpful when we want to evaluate functions that are relatively simple.

    Consider the function $f(x) = (1+x^2)^{20}$. If you want to calculate it derivative using basic differentiation rule, then you need to expand it using binomial formula - it is not undoable, but very unpractical. You can also try product rule… for $20$ times, which is again not a very nice approach.

    And there are functions those rules do not even apply, for example, what if $20$ is replaced by $0.5$? You simply cannot expand the function, in this case, to get to a form that basic differentiation rule applies.

    For more complex functions, we use need a more powerful method to calculate its derivative, which is the Chain Rule.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## The Chain Rule""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose $f$ and $g$ are both differentiable, suppose their composition makes sense and $h(x) = (f \circ g)(x)$. Then $h$ is differentiable, and $\boxed{h'(x) = f'(g(x))\cdot g'(x)}$.

    The Chain Rule is often written is another form: suppose $y = f(u)$, $u = g(x)$, and they are both differentiable, then
    $$
    \boxed{\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}}.
    $$

    You can understand this expression as a product of fractions. **But you cannot cancel $d$**. '$dy$' is **one** variable, same for $dx$ and $du$. We merely name them with two letters.
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
    Let us evaluate the above function $f(x) = (1+x^2)^{20}$ using the Chain Rule.

    We can write it as that $f(u) = u^{20}$ and $u(x) = 1+x^2$. Then $f'(u) = 20u^{19}$ and $u'(x) = 2x$, thus the Chain Rule tells us the result $f'(x) = 20u^{19}\cdot 2x$, where now we should substitute $u = 1+x^2$ and get $f'(x) = 20(1+x^2)^{19}\cdot 2x$ $= 40 x (1+x^2)^{19}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Apply More Than One Rules""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose we want to find the derivative of $f(x) = x\sin(\sqrt{x})$. For the 'first layer', you may see the function as the product of two functions, $x$ and $\sin(\sqrt{x})$, and apply the product rule: $f'(x) = (x)' \sin(\sqrt{x}) + x (\sin(\sqrt{x}))'$ $= \sin(\sqrt{x}) + x(\sin(\sqrt{x}))'$.

    Now to find the derivative of $\sin(\sqrt{x})$, you can view it as a composition of functions, and apply the Chain Rule: Suppose $y(x) = \sin(\sqrt{x})$, then it can be viewed as $y(u) = \sin(u)$ and $u(x) = \sqrt{x} = x^{1/2}$, the Chain Rule tells us $\displaystyle y'(x) = (\cos(u))\cdot(\frac{1}{2}x^{-1/2})$ $\displaystyle = (\cos(x^{1/2}))\cdot (\frac{1}{2}x^{-1/2})$.

    Plugin to the above equation, we get $f'(x) = \sin(\sqrt{x}) + x(\sin(\sqrt{x}))'$ $\displaystyle = \sin(\sqrt{x}) + x (\cos(x^{1/2}))\cdot (\frac{1}{2}x^{-1/2})$, which equals $\displaystyle = \sin(\sqrt{x}) + \frac{1}{2}\sqrt{x}\cos(\sqrt{x})$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Apply Chain Rule More Than Once""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose we want to find the derivative of $f(x) = \sin(\cos(x^3))$.

    First we can take $u = \cos(x^3)$, so that $f(u) = \sin(u)$. Then $f'(x) = \cos(u) \cos'(x^3)$. Now look at the part $\cos(x^3) = g(x)$: we can take $v = x^3$ so that $g(v) = \cos(v)$, then $g'(x) = -\sin(v)3x^2$.

    Put things together, we get $f'(x) = -\cos(u)\sin(v)3x^2$, or $= - \cos(\cos(x^3)) \sin(x^3) 3x^2$ after the substitution.

    In general, one have that $$\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dv}\cdot\frac{dv}{dx},$$ where $y$ is written as a function of $u$, $u$ as a function of $v$, and $v$ as a function of $x$. You should see the pattern and infer how to use chain rule with even more times.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Substitution
        type: info

    If you use Chain Rule, you should always substitute back to the original variables in the final answer.

    ///
    """
    )
    return


if __name__ == "__main__":
    app.run()
