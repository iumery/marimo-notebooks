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
    mo.md(r"""# 2.2 Derivative as a Function""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Derivative of a Function""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""Recall we have that the derivative of $f(x)$ at $a$, denoted by $f'(a)$, is given by (provided that the following limit exists) $$f'(a) = \lim\limits_{h \to 0} \frac{f(a+h) - f(a)}{h}.$$ If the above limit does exists, we say $f$ is differentiable at $a$. Otherwise we say it is not differentiable at $a$. If the limit exists for all $a$ in a given **open** interval, we say $f$ is differentiable on that open interval; and if the limit exists for all $a$ in the domain of $f$, we simply say $f$ is differentiable."""
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | End-points
        type: info

    If $f$ is defined on a **closed** interval $[m,n]$, then $f$ is **never** differentiable at $m$ and $n$ (the end-points) because the limits do not exist (why?).

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Replace $a$ by $x$ in the above limit, we get $$f'(x) = \lim\limits_{h \to 0} \frac{f(x+h) - f(x)}{h},$$ thus we can view it as a new function that assign each $x$ to $\displaystyle \lim\limits_{h \to 0} \frac{f(x+h) - f(x)}{h}$ (provided the limit exists). This function is called the derivative of $f$, denoted as $f'$. The domain of $f'$ can be smaller than $f$.

    There are various notations for differentiation, given that $f(x) = y$, the followings mean **exactly the same thing**:

    1. $f'(x)$;
    2. $y'$;
    3. $\displaystyle \frac{dy}{dx}$;
    4. $\displaystyle \frac{df}{dx}$;
    5. $D_x(f)$;
    6. $Df(x)$;
    7. $\dots$
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
    Derive the derivative of $f(x) = \sqrt{x}$ using the definition of derivative.

    (This is a typical question on the exam. On the exam, the formula $\displaystyle f'(x) = \lim\limits_{h \to 0} \frac{f(x+h) - f(x)}{h}$ will be provided.)

    By definition, we have $\displaystyle f'(x) = \lim\limits_{h \to 0} \frac{f(x+h) - f(x)}{h}$ $\displaystyle =\lim\limits_{h \to 0} \frac{\sqrt{x+h} + \sqrt{x}}{h}$. Remember when we solve limits with this form, a good idea is to try 'multiply by conjugate': $\displaystyle = \lim\limits_{h \to 0} \frac{\sqrt{x+h} + \sqrt{x}}{h}\cdot \frac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}}$ $=\displaystyle \lim\limits_{h \to 0} \frac{(x+h)-x}{h(\sqrt{x+h}+\sqrt{x})}$ $\displaystyle = \lim\limits_{h \to 0} \frac{1}{\sqrt{x + h} + \sqrt{x}}$ $\displaystyle = \frac{1}{2 \sqrt{x}}$ $\displaystyle = \frac{1}{2}x^{-\frac{1}{2}}$.

    **There is an advantage to always write powers, roots, or fraction of powers and roots in the exponential form** (as we did in the last step), we will get to it in the next section.
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
        r"""$f(x) = | x |$ is not differentiable at $0$: $\displaystyle f'(0) = \lim\limits_{h \to 0} \frac{f(0+h) - f(0)}{h}$ $\displaystyle = \lim\limits_{h \to 0} \frac{| h |}{h}$, but we should have seen this before that this limit does not exist."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Theorem""")
    return


@app.cell
def _(mo):
    mo.md(r"""If $f$ is differentiable at $a$, then $f$ is continuous at $a$.""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Proof""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    We want to show that $f$ is continuous at $a$, that is, $\lim\limits_{x \to a}f(x) = f(a)$. Once $a$ is given, $f(a)$ is a constant, thus $\lim\limits_{x \to a}f(x) = f(a) = \lim\limits_{x \to a}f(a)$ which happens if and only if $\lim\limits_{x \to a}(f(x)-f(a)) = 0$ (Main Theorem).

    To show the latter equality, we write $\lim\limits_{x \to a}(f(x)-f(a)) =$ $\displaystyle \lim\limits_{x \to a}((f(x)-f(a))\cdot\frac{x-a}{x-a})$ $\displaystyle =\lim\limits_{x \to a} \frac{f(x) - f(a)}{x - a} \cdot \lim\limits_{x \to a}(x-a)$ (apply the Main Theorem that the limit of product is product of limits). Notice now the first part is exactly the definition of derivative of $f$ at $a$, and the second part is clearly $0$, so we can continue to write $= f'(a) \cdot 0$, which is $0$.

    One thing to notice here is to recall that 'infinity limit' is not well-defined, so $f'(a)$ cannot be $\infty$ thus there is no indeterminate form involved.

    The converse of the theorem is false: **$f$ is continuous at $a$ does not imply that $f$ is differentiable at $a$**. In fact, there are continuous function that is not differentiable at any point!
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Converse of the Statement
        type: danger

    $f$ being continuous at $a$ does not imply differentiability of $f$ at $a$. $| x |$ is an example, it is continuous but not differentiable at $0$.

    Another remark is that, since the logic statement 'A implies B' is equivalent with the logic statement 'not B implies not A', the above theorem is equivalent with the following statement:

    'If $f$ is not continuous at $a$, then $f$ cannot be differentiable at $a$'.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Function That is Not Differentiable""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    There are three common reasons that a function $f(x)$ is **not differentiable** at a point $a$:

    1. The graph of $f$ at the point $(a, f(a))$ has a 'corner' (for example, $f(x) = | x |$ at $0$);
    2. $f$ is not continuous at $a$;
    3. The limit that defines the derivative does not exist (technically this includes the other two reasons). Notice that, as mentioned before, **this includes the case that $\displaystyle \lim\limits_{h \to 0} \frac{f(a+h) - f(a)}{h} = \infty$**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Higher Derivatives""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Since we can view $f'$ as a function, we can take the derivative of this new function, i.e. $(f')'$ and we denote it as $f''$. This function is known as the second derivative of $f$.

    Similarly, we can take third, forth derivatives of $f$, and so on. We say a function is smooth if it has $n$-th derivative for any positive integer $n$.

    Notation-wise, for higher derivative we usually write, for example, $f^{(4)}(x)$ (i.e. number with parenthesis on superscript) instead of $f''''(x)$ for readability.
    """
    )
    return


if __name__ == "__main__":
    app.run()
