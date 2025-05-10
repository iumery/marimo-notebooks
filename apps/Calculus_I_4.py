import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# 1.5 Continuity""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Continuity""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Recall in the last lecture we had a theorem (rule 9. In Main Limit Theorem): if we somehow know $f$ is continuous at $a$, then $\lim\limits_{x\to a}f(x) = f(a)$.

    In fact, this is the definition (meaning this is an 'if and only if' statement) of continuous function:

    A function $f$ is continuous at $a$ if (and only if) $\lim\limits_{x \to a}f(x) = f(a)$. Notice by writing down $\lim\limits_{x \to a}f(x) = f(a)$, we are assuming that the limit of $f(x)$ as $x$ approaches to $a$ exists (left-hand-side of the equation), and $a$ is in the domain of $f$ (right-hand-side of the equation).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Domain
        type: info

    If $a$ is not in the domain of $f$, then $f$ cannot be continuous at $a$.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Contraposition
        type: danger

    Suppose the statement 'if I have class, then I go to school' is given.

    1. If I go to school, does it mean that I necessarily have class? **No**! I can still go to school if I do not have class.
    2. If I do not go to school, does it mean that I necessarily do not have class? **Yes**! Otherwise the statement is false.

    In general, the statement 'if P, then Q' is equivalent with 'if not Q, then not P', its contraposition, and is **not** equivalent with 'if Q, then P'.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Like limit, we can define one-side-continuity: a function $f$ is continuous from the right at $a$ if $\lim\limits_{x \to a^+}f(x) = f(a)$, and is continuous from the left at $a$ if $\lim\limits_{x \to a^-}f(x) = f(a)$.

    If $f$ is not continuous at $a$, we can also say that $f$ is discontinuous at $a$.

    If $f$ is continuous at every point in on an interval, we say $f$ is continuous on that interval. If $f$ is continuous at every point in its domain, we simply say $f$ is continuous, **note that a continuous function is still discontinuous at points that are not in its domain**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example (Continuity)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $\displaystyle f(x) = \frac{1}{x}$ is discontinuous at $0$, because $0$ is not even in its domain; but as the same time, $\displaystyle f(x) = \frac{1}{x}$ **is** a continuous function, because it is continuous at every point in its domain which is $\mathbb{R}\setminus \lbrace 0 \rbrace$;
    2. $f(x) = \lfloor x \rfloor$ is discontinuous at every integer $x$;
    3. $f(x) = \begin{cases} \frac{\sqrt{x^2+9}-3}{x^2}, & x \ne 0 \\ \frac{1}{6}, & x = 0\end{cases}$ is continuous everywhere, because in last section we showed that $\displaystyle \lim\limits_{x\to 0}\frac{\sqrt{x^2+9}-3}{x^2} = \frac{1}{6}$;
    4. Similarly, if in contrary we define $f(x) = \begin{cases} \frac{\sqrt{x^2+9}-3}{x^2}, & x \ne 0 \\ 1, & x = 0\end{cases}$, then $f$ is discontinuous at $x = 0$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Construct a Continuous Function""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    If $f, g$ are continuous at $a$, then $f+g, f-g, f\cdot g, f/g$ (provided that $g(a)\ne 0$) are continuous at $a$.

    If $g$ is continuous at $a$ and $g(a)=b$, and $f$ is continuous at $b$, then $f \circ g$ is continuous at $a$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Typical Continuous Functions""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. Polynomials are continuous (in particular, constant function is continuous);
    2. Rational functions are continuous **on its domain**, in particular, they are not continuous at the points that make the denominator zero;
    3. Root functions are continuous (on its domain);
    4. Trigonometry functions are continuous on their domain: $\sin(x)$ and $\cos(x)$ are continuous at all points, $\tan(x), \cot(x), \sec(x)$ and $\csc(x)$ are continuous except at points where they are not defined.
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
    Find all possible constant $c$ that makes $f$ continuous: $$f(x) = \begin{cases} x + c, & x <0, \\ 2x^2 - c^2, & x \ge 0.\end{cases}$$ No matter what $c$ is, $f$ is a polynomial on $x<0$, so $f$ is continuous if $x<0$. **Similarly $f$ is continuous if $x>0$** (excluding $0$). The only possible problematic point is $x = 0$.

    At $x = 0$, we have that $\lim\limits_{x \to 0^-}f(x) = 0 + c =c$ and $\lim\limits_{x \to 0^+}f(x) = 0 - c^2 = -c^2$. We need they to be the same, thus we solve for $c = -c^2$ or $c(c+1) = 0$, we get either $c = 0$ or $c = -1$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Open and Closed Interval
        type: danger

    Why can't we just say 'Similarly $f$ is continuous if $x\ge 0$' (closed interval)?

    This is because we need two-sided limit, and if we just look at the interval $[0, \infty)$ then at $0$ we only have right-side limit.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Intermediate Value Theorem""")
    return


@app.cell
def _(mo):
    mo.md(r"""Suppose $f$ is continuous on an closed interval $[a, b]$, and $f(a) \ne f(b)$. Let $m$ be a number between $f(a)$ and $f(b)$, then there exists a number $c \in (a, b)$ such that $f(c) = m$.""")
    return


if __name__ == "__main__":
    app.run()
