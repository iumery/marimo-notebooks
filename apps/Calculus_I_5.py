import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# 1.6 Limits Involving Infinity""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Limits Involving Infinity""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""We say that $f(x)$ goes to infinity as $x$ goes to $a$, and write $\lim\limits_{x \to a} f(x) = \infty$, provided that the value of $f(x)$ is arbitrarily large when $x$ is sufficiently close to $a$. The line $x = a$ is called a vertical asymptote of the graph of $f(x)$."""
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""![](/Users/zedanliu/Documents/project/math-notes/_assets/Pasted image 20220902153551.png)"""
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""We say that $f(x)$ goes to $L$ as $x$ goes to infinity, and write $\lim\limits_{x \to \infty}f(x) = L$, provided that the value of $f(x)$ is arbitrarily close to $L$ when $x$ is sufficiently large. The line $y = L$ is called a horizontal asymptote of the graph of $f(x)$."""
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""![](/Users/zedanliu/Documents/project/math-notes/_assets/Pasted image 20220902154343.png)"""
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    We say that $f(x)$ goes to infinity as $x$ goes to infinity, and write $\lim\limits_{x \to \infty}f(x) = \infty$, provided that the value of $f(x)$ is arbitrarily large when $x$ is sufficiently large.

    Similarly, we can talk about:

    1. $\lim\limits_{x \to a^-}f(x) = \infty$;
    2. $\lim\limits_{x \to a^+}f(x) = - \infty$;
    3. $\lim\limits_{x \to -\infty}f(x) = L$, in this case $y = L$ is also a horizontal asymptote. In particular, a function **$f$ can have at most $2$ horizontal asymptotes**;
    4. $\dots$

    All these limits, as before, do not necessarily exist.

    It is not really meaningful, however, to talk about 'the right-side-limit as $x$ goes to infinity', since infinity means being 'arbitrarily large', and it does not make much sense to have numbers to be 'larger than arbitrarily large'. In this sense, 'as $x$ goes to infinity' automatically means the left-side-limit.

    Another remark is that 'infinity' is not a number, or in symbolic language, $\infty \notin \mathbb{R}$. It is a rather abstract concept that is 'larger than any given number'. In particular, if $\lim\limits_{x \to a}f(x) = \infty$, **we still say the limit does NOT exist**. Sometimes people call limits of this form 'improper limits'.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Slant Asymptote
        type: info

    There is another term called a slant asymptote. It happens to a rational function when the degree of the polynomial on the numerator is larger than the degree of the polynomial on the denominator. To find the slant asymptote, do a long division and collect terms with non-negative degree. For example, the function $\displaystyle \frac{x^3}{x^2 - 1}$ has a slant asymptote. Since it equals $\displaystyle \frac{x(x^2-1) + \text{extra terms}}{x^2-1}$, the slant asymptote line is $y = x$.

    ///
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
    1. $\displaystyle \lim\limits_{x \to 0^+} \frac{1}{x} = \infty$;
    2. $\lim\limits_{x \to \pi^-} \cot(x) = -\infty$;
    3. $\displaystyle \lim\limits_{x \to \infty} \frac{1}{x} = 0$;
    4. $\displaystyle \lim\limits_{x \to \infty} \frac{x}{x^3 + 1} = 0$;
    5. $\lim\limits_{x \to \infty} \sin(x) = \text{DNE}$.
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
    Find vertical and horizontal asymptotes of $\displaystyle f(x) = \frac{2x^2 + x - 1}{x^2 + x - 2}$.

    1. **Vertical asymptotes happen when, for rational functions, the denominator is zero (i.e. the function is not defined)**. In this case it means $x^2 + x - 2 = 0$, thus $x = -2$ or $1$;
    2. **Horizontal asymptotes happen at the line $y = \lim\limits_{x \to \infty}f(x)$ and $y = \lim\limits_{x \to - \infty}f(x)$ given that the limit exists**. In this case, both limits are $2$, see below for evaluation.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Theorem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""Let $r > 0$ be an rational number and $c$ be any real number, then $\displaystyle \lim\limits_{x \to \infty}\frac{c}{x^r} = 0$ and $\displaystyle \lim\limits_{x \to -\infty} \frac{c}{x^r} = 0$."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Indeterminate Forms""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Since $\infty$ is not a number, it is **not necessarily true** that we can do arithmetic operations involving $\infty$. For example, to evaluate $\lim\limits_{x \to \infty}2x^2 - x$ or $\lim\limits_{x \to \infty}x - 2x^2$, we cannot simply use the Main Limit Theorem in section 1.4, and get that the result is $\infty - \infty$, because this does not tell us much information.

    There are four indeterminate forms:

    1. $\infty - \infty$, for example, $\lim\limits_{x \to \infty}2x^2 - x$;
    2. $\infty \cdot 0$, for example, $\displaystyle \lim\limits_{x \to 0}x \cdot \frac{1}{x^2+1}$;
    3. $\displaystyle \frac{0}{0}$, for example, $\displaystyle \lim\limits_{x\to 0}\frac{\sin(x)}{x}$;
    4. $\displaystyle \frac{\infty}{\infty}$, for example, $\displaystyle \lim\limits_{x \to \infty}\frac{2x+5}{3x^5+3x+3}$.

    There are other indeterminate forms, you are likely to learn them in Calculus 2.

    When a limit is of indeterminate form, **anything can happen to the result**. For example:

    1. $\lim\limits_{x \to \infty}2x^2 - x$;
    2. $\lim\limits_{x \to \infty}x - 2x^2$;
    3. $\lim\limits_{x \to \infty}x - x$,

    are all of the form $\infty - \infty$, but their values are $\infty, -\infty$, and $0$, respectively.

    The third example right above is a bit silly, but it does suggest us one of the way to solve indeterminate forms, that is to use **factoring and simplification**.

    Though as mentioned before, operations involving $\infty$ (and $0$) do **not necessarily** follow the arithmetic rules, but **some of them does follow the rule** in the intuitive sense. For example, $\infty + \infty$ can be thought at 'something that is arbitrarily large plus something that is also arbitrarily large' - and apparently, you get another thing that is even larger - which is also arbitrarily large. So for example, $\lim\limits_{x \to \infty} x + x^2$ is infinity.

    Like above Theorem, $\displaystyle \frac{c}{\pm \infty}$ is also **not** an indeterminate form. It has limit $0$.
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
    The method we use is referred as 'quotient by the highest power'.

    $\displaystyle \lim\limits_{x \to \infty} \frac{3x+5}{x-4}$ $\displaystyle = \lim\limits_{x \to \infty} \frac{\frac{3x}{x}+\frac{5}{x}}{\frac{x}{x}-\frac{4}{x}}$ $\displaystyle = \lim\limits_{x \to \infty}\frac{3 + \frac{5}{x}}{1 - \frac{4}{x}}$, now we use the above theorem that $\displaystyle \lim\limits_{x\to \infty}\frac{5}{x} = 0$ and $\displaystyle \lim\limits_{x \to \infty}\frac{4}{x} = 0$, so the limit we have $\displaystyle = \frac{3+0}{1 - 0} = 3$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Important Remark""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    You must write $\lim\limits_{x \to a}$ operator **at each step**.

    You *can* just write $\lim$ (without $x \to a$) **starting from the second step**, if you are not changing $a$. However, you **cannot** completely omit the limit operator - it is mathematically **wrong** if you do so.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### More Examples""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $\lim\limits_{x \to \infty} \sqrt{64x^2 + x} - 8x$ $\displaystyle =\lim\limits_{x\to \infty}(\sqrt{64x^2+x}-8x)\cdot \frac{\sqrt{64x^2+x}+8x}{\sqrt{64x^2+x}+8x}$ $\displaystyle =\lim\limits_{x\to \infty}\frac{64x^2+x-64x^2}{\sqrt{64x^2+x}+8x}$ $\displaystyle =\lim\limits_{x\to \infty}\frac{x}{\sqrt{64x^2+x}+8x}$ $\displaystyle =\lim\limits_{x\to \infty}\frac{1}{\sqrt{64+\frac{1}{x}}+8}$ $\displaystyle =\frac{1}{\sqrt{64}+8}$ $\displaystyle = \frac{1}{16}$;
    2. $\displaystyle \lim\limits_{x \to \infty} \frac{\sqrt{4x^2+5}}{x-2} =$ $\displaystyle \lim\limits_{x\to \infty} \frac{\sqrt{4x^2+5}/x}{(x-2)/x}$ $\displaystyle = \lim\limits_{x\to \infty} \frac{\sqrt{\frac{4x^2}{x^2} + \frac{5}{x^2}}}{\frac{x}{x}- \frac{2}{x}}$ $\displaystyle = \lim\limits_{x\to \infty} \frac{\sqrt{4 + \frac{5}{x^2}}}{1 - \frac{2}{x}}$ $\displaystyle = \frac{\sqrt{4}}{1} = 2$. **Notice here the 'highest power' is $1$**, instead of $2$, that is because terms appear inside a square-root only have half of the power as it appears to have, e.g. $\sqrt{x^8}$ is actually a term with degree $4$.

    A particularly interesting example as a variation is $\displaystyle \lim\limits_{x \to -\infty} \frac{\sqrt{4x^2+5}}{x-2} =$ $\displaystyle \lim\limits_{x\to -\infty} \frac{\sqrt{4x^2+5}/x}{(x-2)/x}$ $\displaystyle = \lim\limits_{x\to \infty} \frac{{\color{red}-}\sqrt{\frac{4x^2}{x^2} + \frac{5}{x^2}}}{\frac{x}{x}- \frac{2}{x}}$ $= \lim\limits_{x\to \infty} \frac{{\color{red}-}\sqrt{4 + \frac{5}{x^2}}}{1 - \frac{2}{x}}$ $\displaystyle = {\color{red}-}\frac{\sqrt{4}}{1} = -2$. This is because $\sqrt{x^2} = |x|$, thus if $x$ is negative, we have $\sqrt{x^2} = -x$. This makes sense: the expression $\displaystyle \frac{\sqrt{4x^2+5}}{x-2}$, when $x$ is negative, is a positive number (square root is always non-negative, by definition) divided by a negative number, thus a negative number.

    Moral of the story: be very careful about signs, especially when square root is involved.
    """
    )
    return


if __name__ == "__main__":
    app.run()
