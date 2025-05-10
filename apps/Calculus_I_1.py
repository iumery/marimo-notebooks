import marimo

__generated_with = "0.13.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# 1.1-1.2 Functions""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Functions""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Given two sets $X, Y$ (they can be the same), a function $f$ is a rule to assign each element in $X$ **exactly one element** in $Y$, we denote $f: X \to Y$. $X$ is called the domain of $f$ and $Y$ is called the codomain of $f$. In the scope of this course, $Y$ is also called the range of $f$.

    In this course, **$X, Y$ are always assumed to be subsets of the real numbers**. In particular, **we do not use complex numbers in this course**.

    If a question asks you what is the domain of a function $f$, it means to ask for the largest set where $f$ is defined. For example, the domain of $\displaystyle f(x) = \frac{1}{x}$ is $\mathbb{R} \setminus \lbrace 0 \rbrace$ (all real numbers except for $0$).

    The abstract element in the set $X$ is sometimes called the independent variable, and the abstract element in the set $Y$ is sometimes called the dependent variable. You can replace an independent variable by another one by changing all the old variable to the new one in the expression of the function. For example, if $\displaystyle f(x) = \sin(x) + x^2 + \frac{1}{x+2}$, then $f(m+3)$ $\displaystyle = \sin(m+3) + (m+3)^2$ $+ \frac{1}{m+3+2}$, i.e. replace all $x$ by $m+3$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Parenthesis
        type: danger

    It is always a good habit to write parenthesis when you replace the variable. For example, the following is a **very common mistake**:

    Question: $f(x) = -x$, what is $f(x-1)$?

    Wrong answer: $f(x-1) = -x-1$.

    Correct answer: $f(x-1) = -(x-1) = -x+1$.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    If under an assignment $f$, no two elements in $X$ correspond to the same element in $Y$, we say $f$ is injective. In the scope of this course, in such case we also say $f$ is bijective. For example, $f(x) = 2x$ is injective. $\sin(x)$ is not injective, because $\sin(0) = 0$ but $\sin(\pi)$ is also $0$.

    We may do operations of functions. Suppose $f, g$ are two functions, we can do (point-wise) addition, multiplication, subtraction, of division (given the divisor is not $0$) in the usual sense, that is, the sum of $f, g$ (viewed as a new function) evaluated at $x$ is defined to be the sum of $f$ evaluated at $x$ and $g$ evaluated at $x$, i.e. $(f+g)(x) = f(x) + g(x)$- of course, those operations only make sense when $x$ lies in the domains of both $f$ and $g$.

    We can compose two functions $f, g$ to one function $f \circ g$, which is defined by the rule $(f \circ g)(x) = f(g(x))$. For example, if $f(x) = e^x$ and $g(x) = x+5$, then $(f \circ g)(x)$ $=f(g(x))$ $= f(x+5)$ $= e^{x+5}$.

    We shall graph a function by plotting all possible points $(x, f(x))$. A curve needs to pass the vertical-line-test to be a graph of a function: any vertical line on the plane cannot intersect the graph of a function more than once. For example, a circle is not a graph of a function.

    We can transform a function $f$ in the sense that we can shift, stretch, shrink, or flip the graph of $f$. Suppose the original function is $y = f(x)$, then:

    1. $y = f(x) + c$ shift the graph of $f(x)$ up by $c$ units (if $c$ is negative, this means shift down);
    2. $y = f(x+c)$ shift the graph of $f(x)$ to the left by $c$ units (if $c$ is negative, this means shift to the right);
    3. $y = cf(x)$ stretch the graph of $f(x)$ vertically by a factor $c$ (if $c$ is smaller than $1$, this means shrink);
    4. $y = f(cx)$ shrink the graph of $f(x)$ horizontally by a factor $c$ (if $c$ is smaller than $1$, this means stretch);
    5. $y = -f(x)$ flip the graph along $x$-axis;
    6. $y = f(-x)$ flip the graph along $y$-axis.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Graphing
        type: info

    In this course, you should know how to graph $y = ax+b$, $y = x^2$, $y = x^3$, $y = \sqrt{r^2 - x^2}$, and $y = \sqrt{x}$ and how to transform these graphs. They will be used in the last two sections of this course (7.1 and 7.2).

    We will learn another way to graph more complicated functions.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Those may not be easy to remember. Try to understand why, and remember that you can always try to plot few points and infer what is the transformation from there.

    A function is said to be even if by flipping its graph along $y$-axis, you get the exact same graph, i.e. $f(x) = f(-x)$ for all $x \in X$; odd if by flipping its graph along $y$-axis followed by flipping along $x$-axis, you get the exact same graph, i.e. $f(x) = -f(-x)$ for all $x \in X$. For example, $f(x) = x^2$ is even, because $f(x) = x^2$ and $f(-x) = (-x)^2 = x^2$ and they are the same; $f(x) = x^3$ is odd, because $f(x) = x^3$ and $-f(-x) = -(-x)^3 = x^3$ and again they are the same.

    A function is said to be decreasing, increasing, non-decreasing, non-increasing in the intuitive sense by looking at its graph (if we are given the graph, of course). Mathematically speaking:

    1. $f$ is decreasing if $f(x) < f(y)$ whenever $x > y$;
    2. $f$ is non-increasing if $f(x) \le f(y)$ whenever $x > y$;
    3. $f$ is increasing if $f(x) > f(y)$ whenever $x > y$;
    4. $f$ is non-decreasing if $f(x) \ge f(y)$ whenever $x > y$.

    A function does not need to be decreasing/increasing/non-decreasing/non-increasing on its entire domain. For example, $f(x) = \sin(x)$ is increasing on $(0, \pi/2)$ but decreasing on $(\pi/2, \pi)$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Open or Closed Interval
        type: info

    It does not make too much sense to say a function is increasing or decreasing **at a point** (naturally, because it needs to compare with something).

    Because of this, it does not matter if we include the end-point or not for the interval of increasing/decreasing. For example, we can also say that $f(x) = \sin(x)$ is increasing on $[0, \pi/2]$ and decreasing on $[\pi/2, \pi]$.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Polynomials""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    A polynomial (of $x$) is a function of the form $f(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0$ where $n$ is a non-negative integer. For example, $f(x) = 5x^4+2x+1$ is a polynomial; $f(x) = x^{\frac{1}{2}}$ is not, $f(x) = x^{-2}$ also is not.

    If $n = 0$, then $f(x) = a_0$ is just a constant.

    If $n = 1$, such function is said to be linear, they have the form $f(x) = ax + b$. $a$ is called the slope and $b$ is called the intercept. The graph of a linear function is a straight line, it grows at a constant rate.

    **Two (different) linear functions have the same slope if and only if their graphs are parallel straight lines**. If two different straight lines are parallel, then they have no intersection point; otherwise they have exactly one intersection point.

    **The product of slopes of two linear functions is $-1$ if and only if their graphs are perpendicular (or orthogonal) straight lines**. For example, the graphs of $y = 2x$ and $\displaystyle y = -\frac{1}{2}x$ are perpendicular.

    You should be able to:

    1. **Given the slope of a linear function and one point it passes, find the full expression of the function**. For example, for a linear function $f(x) = mx+b$ and that $m = 2$ and it passes $(3, 4)$, then we have $f(x) = 2x+b$ and it satisfies $4 = 2\cdot 3 +b$. So $b = 4-6 = -2$, thus the full expression of $f(x)$ is $f(x) = 2x-2$;
    2. **Given the slope of a linear function and one point it passes, find the full expression of the line that is perpendicular to the given line that passes the given point**. For example, for a linear function $f(x) = mx+b$ and that $m = 2$ and it passes $(3, 4)$, then the line perpendicular to this line should have slope $\displaystyle \frac{-1}{2} = -\frac{1}{2}$, the line that has slope $\displaystyle -\frac{1}{2}$ that passes $(3,4)$ is $\displaystyle (y-4) = -\frac{1}{2}(x-3)$;
    3. Given two linear functions (with non-parallel graphs), find their intersection point. For example, if $f(x) = x+2$ and $g(x) = 5x-3$, you may set them to be equal, i.e. $x+2 = 5x-3$ which gives $5 = 4x$ thus $\displaystyle x = \frac{5}{4}$, thus the intersection point has coordinate $\displaystyle (\frac{5}{4},\frac{13}{4})$ by plug in $\displaystyle x = \frac{5}{4}$ to either $f$ or $g$;
    4. Given two points on the plane, find the line that pass through both of them. You do this by solving a linear system. For example, to find a linear function passes both $(1,2)$ and $(5,4)$, you solve the system $\begin{cases} 2 = m + b \\ 4 = 5m + b\end{cases}$, and the result should be $\begin{cases} m = \frac{1}{2} \\ b = \frac{3}{2} \end{cases}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Lemma""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Another rather simple class of polynomial functions is the power function, those are the functions of the form $f(x) = x^n$. If $n$ is odd, $x^n$ is an odd function, and if $n$ is even, $x^n$ is an even function.

    If a function is of the form $\displaystyle f(x) = \frac{p(x)}{q(x)}$ where $p(x)$ and $q(x)$ are polynomials, we say $f$ is a rational function. The domain of a rational function is the collection of $x$ such that $q(x) \ne 0$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Trigonometric Functions""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    There are six basic trigonometric functions. **You should at least remember what do $\sin(x)$ and $\cos(x)$ look like, and how the other four functions are derived from sine and cosine**:

    1. $\displaystyle \tan(x) = \frac{\sin(x)}{\cos(x)}$, in particular, it is not defined at the points where $\cos(x) = 0$, i.e. when $\displaystyle x = (n+\frac{1}{2})\pi$;
    2. $\displaystyle \cot(x) = \frac{\cos(x)}{\sin(x)}$, in particular, it is not defined at the points where $\sin(x) = 0$, i.e. when $x = n\pi$;
    3. $\displaystyle \sec(x) = \frac{1}{\cos(x)}$;
    4. $\displaystyle \csc(x) = \frac{1}{\sin(x)}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Distributivity
        type: danger

    Not every operation is distributive (over another operation) - in fact, most operations are *not* distributive. 
    This means, for example, in general, $\sin(x + y) \ne \sin(x) + \sin(y)$ and $\sin(x \cdot y) \ne \sin(x) \cdot \sin(y)$.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    There are some special values, you should know that:

    1. $\displaystyle \sin(\frac{1}{2}\pi) = 1$, $\sin(0) = \sin(\pi) = 0$, $\displaystyle \sin(\frac{3}{2}\pi) = -1$, and that $\sin(x)$ is $2\pi$-periodic, meaning that, for example, $\displaystyle \sin(\frac{5}{2}\pi)$ is also $1$;
    2. $\cos(0) = 1$, $\displaystyle \cos(\frac{1}{2}\pi) = \cos(\frac{3}{2}\pi) = 0$, $\cos(\pi) = -1$, and that $\cos(x)$ is $2\pi$-periodic.

    It is good to know that:

    1. $\displaystyle \sin(\frac{\pi}{6}) = \cos(\frac{\pi}{3}) = \frac{1}{2}$;
    2. $\displaystyle \sin(\frac{\pi}{3}) = \cos(\frac{\pi}{6}) = \frac{\sqrt{3}}{2}$;
    3. $\displaystyle \sin(\frac{\pi}{4}) = \cos(\frac{\pi}{4}) = \frac{\sqrt{2}}{2}$,

    and other special values, though they are not much needed in this course.

    There are several identities and formulas regards trigonometric functions. You should know the basic ones:

    1.   $\sin^2(x) + \cos^2(x) = 1$;
    2.   $\tan^2(x) + 1 = \sec^2(x)$;
    3.   $\cot^2(x)+1 = \csc^2(x)$.

    The double-angle formulas, half-angle formulas, and summation formulas are not much needed in this course thus are omitted from the notes, but it is good to review them. They will be used more frequently in Calculus II.
    """
    )
    return


if __name__ == "__main__":
    app.run()
