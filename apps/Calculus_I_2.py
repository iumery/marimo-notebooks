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
    mo.md(r"""# 1.3 the Limit of a Function""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Limit of a Function""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    We say that the limit of $f(x)$ as $x$ approaches to $a$ is $L$ (**a real number**), and write $\lim\limits_{x \to a}f(x) = L$, provided that the value of $f(x)$ is arbitrarily close to $L$ when $x$ is sufficiently close to $a$, but not equals $a$, on either side.

    We say that the limit of $f(x)$ as $x$ approaches to $a$ from the right is $L$, or the right-hand-limit of $f(x)$ as $x$ approaches to $a$ is $L$, and write $\lim\limits_{x \to a^+}f(x) = L$, provided that the value of $f(x)$ is arbitrarily close to $L$ when $x$ is sufficiently close to $a$ and also strictly larger than $a$.

    We say that the limit of $f(x)$ as $x$ approaches to $a$ from the left is $L$, or the left-hand-limit of $f(x)$ as $x$ approaches to $a$ is $L$, and write $\lim\limits_{x \to a^-}f(x) = L$, provided that the value of $f(x)$ is arbitrarily close to $L$ when $x$ is sufficiently close to $a$ and also strictly smaller than $a$.

    **Notice that none of the three limits necessarily exists**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Why do we study limits?
        type: info

    Limit makes practical things easier. For example, in some sense it allows us to divide by zero. It allow us to study the local behaviormn bcc of a function (i.e. what happens to the function near a point), which usually is much simpler than studying the whole thing. A big part of Calculus only makes sense if we understand limit.

    For functions that looks 'nice' (for example, a straight line), limit will be a straight-forward idea. But weird things can happen when we talk about the general case, and that's why we need to spend some more time to understand it.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Limit
        type: danger

    One important thing about the above definition is that the limit needs to be a *single* number. It means a function can have only one limit at a point $a$ (if there is any), that is, it is impossible that $\lim\limits_{x\to 1}f(x) = 2$ but also $\lim\limits_{x \to 1}f(x) = 3$. But of course, $\lim\limits_{x \to 1}f(x)$ and $\lim\limits_{x\to 2}f(x)$ can have different values.

    However, this is no longer the case if we jump out of calculus settings. If $f$ is a function with codomain being a non-[Hausdorff space](https://en.wikipedia.org/wiki/Hausdorff_space), then it can have more than one limit point for the same $a$.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 1 (Practical Problem)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""A famous population model is the logistic model. It models the population of a given area or the world. The dependent variable $x$ is time, and the output is, of course, the population. The logistic function reads $$f(x) = \frac{P}{1 + e^{k(x-c)}}$$ where $P, k, c$ are certain parameters (i.e. fixed numbers, or constant), $k$ is negative. The output $f(x)$ when $x$ is sufficiently large enough, is close to $P$, but will never reach $L$ (why?). We say the limit of $f$ as $x$ approaches to infinity is $P$, and write $\lim\limits_{x \to \infty}f(x) = P$."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 2 (Function Value at a Point)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The limit of $f(x)$ as $x$ approaches to $a$ **not necessarily has anything to do with the actual value $f(a)$**, for example, $\lim\limits_{x \to 2}f(x)=4$ in all of the following cases:

    1. $f(x) = x^2$ for $x \in [0,4]$. In this case $f(a)$ is defined and $f(a) = 4 = \lim\limits_{x \to a}f(x)$;
    2. $f(x) = \begin{cases}x^2,&x\ne 2\\10,&x=2\end{cases}$. In this case $f(a)$ is defined, but $f(a) = 10 \ne \lim\limits_{x \to a}f(x)$;
    3. $f(x) = x^2$ for $x \ne 2$. In this case $f(a)$ is not even defined, but we still have $\lim\limits_{x \to 2}f(x) = 4$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Intuitive Way to Calculate Limit""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    An intuitive way to calculate limit is to plug-in values that are close to $a$, but not equal to $a$. For example, we can plugin $x = 2.00001$, $x = 2.0000001$, $x = 1.999999$, etc. in the above example, and we can see the resulting values are indeed close to $4$.

    **You should not use the intuitive way to calculate any limit on any exam or quiz** because the intuitive way of calculating the limit may not work (and the calculation is nearly impossible without a calculator anyway), here are the three usual reasons:

    1. The value you plug into the function is not close enough to $a$ (an in practice, there is no general way to decide which value is considered 'close enough' to $a$);
    2. Problems involving floating point on your calculator or computer: basically, any program, especially program that is not well-written, has a certain range of numbers it can handle, if your input is too large, too small, or have too much floating points, you may get all different kinds of errors. The book gives an example of evaluating $$\lim\limits_{t \to 0}\frac{\sqrt{t^2 + 9}-3}{t^2}.$$ If you try very small value of $t = 0.0000001$, *some* calculators will tell you the answer is 0, but the true limit is $\frac{1}{6}$;
    3. **The limit does not exist**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 1 (Limit Does Not Exist)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    This example is known as the 'Topologist's Sine Curve'. Consider the function $f(x) = \sin(\frac{1}{x})$ for $x > 0$ and try to evaluate $\lim\limits_{x \to 0}f(x)$.

    1. If we take $\displaystyle x = \frac{1}{\pi}, \frac{1}{2\pi}, \cdots, \frac{1}{10000\pi}, \cdots$, we have $f(x) = \sin(n \pi) = 0$;
    2. If we take $\displaystyle x = \frac{2}{\pi}, \frac{2}{5\pi}, \cdots, \frac{2}{10001\pi}, \cdots$, we have $f(x) = 1$;
    3. If we take $\displaystyle x = \frac{2}{3\pi}, \frac{2}{7\pi}, \cdots, \frac{2}{10003\pi}, \cdots$, we have $f(x) = -1$.

    The problem is that there is no $L$ (**a single number**) that $f(x)$ is arbitrarily close to, no matter how close $x$ is to $0$. Thus **we say $\displaystyle \lim\limits_{x\to 0}\sin(\frac{1}{x})$ does not exist**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 2 (Limit Does Not Exist)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""**If the left-hand-limit and right-hand-limit both exists but not equal, we also say the limit does not exist**. For example, if $$f(x) = \begin{cases} 1,&x < 0 \\ 0,&x\ge 0\end{cases}$$ then $\lim\limits_{x \to 0^-}f(x) = 1$ $\ne 0 = \lim\limits_{x \to 0^+}f(x)$. Thus $\lim\limits_{x \to 0}f(x)$ does not exist."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 3 (Limit Does Not Exist)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Evaluate $\displaystyle \lim\limits_{x \to 0}\frac{|x|}{x}$.

    **Absolute value function is a very special function, we should consider different cases when the input is negative or positive**. If we evaluate left-hand-limit, we have $\displaystyle \lim\limits_{x \to 0^-}\frac{|x|}{x}$ $\displaystyle = \lim\limits_{x \to 0^-}\frac{-x}{x}$ (because $x \to 0^-$ means $x$ is close to $0$ but smaller than $0$, meaning that $x$ is negative thus $|x| = -x$) $= -1$; yet if we evaluate right-hand-limit, we have $\displaystyle \lim\limits_{x\to 0^+}\frac{|x|}{x}$ $\displaystyle =\lim\limits_{x \to 0^+}\frac{x}{x} = 1$. The limits from two sides are different, thus the limit does not exist.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Formal Definition of Limit""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Let $f: X \to Y$, $Y \subset \mathbb{R}$ be a function and $a \in X$. We say that $f$ approaches to $L$ as $x$ goes to $a$, and write $\lim\limits_{x \to a}f(x) = L$ provided that: for every $\varepsilon > 0$, there exists $\delta > 0$ such that $| L - f(x) | < \varepsilon$ whenever $x \in X$ and $| x - a | < \delta$.

    **You do not need to know the above definition in this course**. But if you are majoring in math, it is highly recommended to read this formal definition carefully, try some $\varepsilon$ and $\delta$ values with the examples above, and get the point of this definition - you will eventually take a course where this idea is applied everywhere. This is known as the epsilon-delta definition of limit.
    """
    )
    return


if __name__ == "__main__":
    app.run()
