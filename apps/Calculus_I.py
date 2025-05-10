import marimo

__generated_with = "0.13.6"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# 0 Review""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    These are some preliminary formulas or facts that you should have learnt in your pre-calculus course(s). They are considered as prerequisite and will be used through out the course.

    The boxed or colored ones are in particular important, they will be the keys to solve problems on your tests.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Arithmetic Operations""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $ab + ac = a(b+c)$;
    2. $\displaystyle \frac{a}{b} + \frac{c}{d} = \frac{ad+bc}{bd}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Exponent""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $a^0 = 1$ for any real number $a$;
    2. $a^na^m = a^{n+m}$;
    3. $(a^n)^m = a^{nm}$;
    4. $(ab)^n = a^nb^n$;
    5. $\displaystyle a^{-n} = \frac{1}{a^n}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Radical""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $\sqrt[n]{a}$ and $a^{\frac{1}{n}}$ are two different notations for the same thing; for $n=2$, we simplify the notation to $\sqrt{a}$ (which is the same as $a^{\frac{1}{2}}$);
    2. $\sqrt[n]{ab} = \sqrt[n]{a}\sqrt[n]{b}$;
    3. $\sqrt[m]{\sqrt[n]{a}} = \sqrt[mn]{a}$;
    4. $\sqrt[n]{a^n} = \begin{cases} a,&n\text{ odd} \\ | a |,&n\text{ even}\end{cases}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition
        type: danger

    There is a difference between $x^2 = a$ and $x = \sqrt{a}$. The former admits two solutions for $x$ but the latter **only admits one**.

    For example, if we write $x^2 = 4$, then $x = 2$ or $-2$. However, if we write $x = \sqrt{4}$, then the **only solution** is that $x = 2$ (i.e. the positive root). $x = -2$ is not a solution for $x = \sqrt{4}$.
    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Absolute Value""")
    return


app._unparsable_cell(
    r"""
    1. $| ab | = | a \| b |$;
    2. $| a + b | \le | a | + | b |$.
    """,
    name="_"
)


@app.cell
def _(mo):
    mo.md(r"""## Inequality and Equality""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $| a | < b \implies -b < a < b$;
    2. $| a | > b \implies a < -b \text{ or } a > b$;
    3. $\displaystyle \frac{a}{b} < 0 \implies (a < 0\text{ and }b > 0)\text{ or }(a > 0\text{ and }b < 0)$;
    4. $\displaystyle \frac{a}{b} > 0 \implies (a < 0\text{ and }b < 0)\text{ or }(a > 0\text{ and }b > 0)$;
    5. $\boxed{\frac{a}{b} = 0\text{ if }a=0\text{ and }b\ne 0}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Factoring""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $\boxed{a^2 - b^2 = (a+b)(a-b)}$;
    2. $a^2 + 2ab + b^2 = (a+b)^2$;
    3. $a^2 - 2ab + b^2 = (a-b)^2$;
    4. If $n$ is odd, then $$a^n + b^n = (a + b)(a^{n-1} - ba^{n-2} + b^2a^{n-3} - \dots + b^{n-1})$$ and $$a^n - b^n = (a - b)(a^{n-1} + ba^{n-2} + b^2a^{n-3} + \dots + b^{n-1}).$$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition

    [See here](https://math.libretexts.org/Bookshelves/Algebra/Algebra_and_Trigonometry_(OpenStax)/01%3A_Prerequisites/1.05%3A_Factoring_Polynomials) for a detailed explanation for factoring polynomials. Factoring polynomials will be a crucial technique in the second half of this course.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Quadratic Formula""")
    return


@app.cell
def _(mo):
    mo.md(r"""The root(s) for $ax^2 + bx + c = 0, a \ne 0$ is(are) $$\boxed{x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}}.$$ In particular if $b^2-4ac$ is positive, there are two distinct real roots, if it is $0$, there is one double-root (i.e. technically they are still two roots, but they are equal), if it is negative, there is no real root.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Common Mistakes""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $(x^2)^3 = x^{2\cdot 3} = x^6$, not $x^{2+3} = x^5$;
    2. Except for special cases, $(a+b)^n \ne a^n + b^n$, and $\displaystyle \frac{1}{a^n + b^n} \ne \frac{1}{a^n} + \frac{1}{b^n}$;
    3. $2(x+1)^2 \ne (2x+2)^2$;
    4. Notice the difference between $a^{-n}$ and $a^{\frac{1}{n}}$. $a^{-n}$ means 'one over $a$ to $n$-th power', $a^{\frac{1}{n}}$ means '$n$-th root of $a$'.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 1 (Simplification)""")
    return


@app.cell
def _(mo):
    mo.md(r"""$$\begin{aligned}&(\frac{1}{x} + \frac{1}{x+y})\cdot (x+y)^{-2} \cdot \frac{x^2 - y^2}{y^2} \\ =& (\frac{1\cdot(x+y)}{x\cdot(x+y)} + \frac{1 \cdot x}{(x+y) \cdot x}) \cdot \frac{1}{(x+y)^2} \cdot \frac{(x+y)(x-y)}{y^2}\\ =& \frac{x+y+x}{x(x+y)}\cdot \frac{1}{(x+y)^2} \cdot \frac{(x+y)(x-y)}{y^2} \\ =& \frac{(x+y+x)(x+y)(x-y)}{x(x+y)(x+y)^2y^2} \\ =&\frac{(2x+y)(x-y)}{x(x+y)^2y^2} \end{aligned}$$""")
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 2 (Inequality)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Solve $\displaystyle \frac{x + 2}{x - 5} < 0$.

    There are two possibilities:

    1. $x+2 < 0\text{ and }x-5 > 0$, which implies that $x < -2 \text{ and }x>5$, which cannot happen;
    2. $x+2 > 0\text{ and }x-5 < 0$, which implies that $x > -2 \text{ and }x <5$, which means $-2<x<5$ or $x \in (-2,5)$.

    Thus the answer is $x \in (-2, 5)$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example 3 (Factoring Polynomial)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Write the summation $$3x^3(x-3)^{-\frac{2}{3}}+2(x-3)^{\frac{1}{3}}$$ as a product.

    1. Pick any one of the summand, say $3x^3(x-3)^{-\frac{2}{3}}$;
    2. Within this summand, look at its terms one by one, i.e. $3$, $x^3$, and $(x-3)^{-\frac{2}{3}}$;
        1. $3$ is a constant term, is there a constant term in the other summand? Yes, we have $2$ in the second summand. What is the greatest common factor of $3$ and $2$? It is $1$. Since it is in a product, $1$ can be omitted so we move to next term;
        2. $x^3$ has base $x$, is there an $x$-based term in the other summand? No. We move to the next term;
        3. $(x-3)^{-\frac{2}{3}}$ has base $(x-3)$, is there an $(x-3)$-based term in the other summand? Yes, we have $(x-3)^{\frac{1}{3}}$. Within $(x-3)^{-\frac{2}{3}}$ and $(x-3)^{\frac{1}{3}}$, choose the one with the **least** power as the greatest common factor. In this case we have $(x-3)^{-\frac{2}{3}}$;
    3. Collect the common factors, in this case we just have one, that is $(x-3)^{-\frac{2}{3}}$;
    4. Write $$(x-3)^{-\frac{2}{3}}\cdot($$ Now, what are left-overs for each of the original summand?
        1. For the first summand $3x^3(x-3)^{-\frac{2}{3}}$, if we take out $(x-3)^{-\frac{2}{3}}$, we are left with $3x^3$, so we write $$(x-3)^{-\frac{2}{3}}\cdot(3x^3$$ and move to the next summand;
        2. For the second summand $2(x-3)^{\frac{1}{3}}$, if we take out $(x-3)^{-\frac{2}{3}}$, we are left with $2(x-3)$. Why? because $\displaystyle \frac{2(x-3)^{\frac{1}{3}}}{(x-3)^{-\frac{2}{3}}}$ $= 2(x-3)$, using the rules in 'Exponent' above. So we write $$(x-3)^{-\frac{2}{3}}(3x^3+2(x-3)).$$ We close the parentheses because there is no more summand.
    5. Finally, we can clean things up by expand $2(x-3)$ and get $$(x-3)^{-\frac{2}{3}}(3x^3+2x-6).$$
    """
    )
    return


@app.cell(column=1)
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
    /// admonition

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
    /// admonition

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
    /// admonition

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
    mo.md(
        r"""
    /// admonition

    On above example 1, 2, we used two methods to get expression of line. Both methods are valid, and both formats of the solutions are acceptable in this course.

    ///
    """
    )
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
    /// admonition

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


@app.cell(column=2)
def _(mo):
    mo.md(r"""# 1.3 the Limit of a Function""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Limit of a Function

    We say that the limit of $f(x)$ as $x$ approaches to $a$ is $L$ (**a real number**), and write $\lim\limits_{x \to a}f(x) = L$, provided that the value of $f(x)$ is arbitrarily close to $L$ when $x$ is sufficiently close to $a$, but not equals $a$, on either side.

    We say that the limit of $f(x)$ as $x$ approaches to $a$ from the right is $L$, or the right-hand-limit of $f(x)$ as $x$ approaches to $a$ is $L$, and write $\lim\limits_{x \to a^+}f(x) = L$, provided that the value of $f(x)$ is arbitrarily close to $L$ when $x$ is sufficiently close to $a$ and also strictly larger than $a$.

    We say that the limit of $f(x)$ as $x$ approaches to $a$ from the left is $L$, or the left-hand-limit of $f(x)$ as $x$ approaches to $a$ is $L$, and write $\lim\limits_{x \to a^-}f(x) = L$, provided that the value of $f(x)$ is arbitrarily close to $L$ when $x$ is sufficiently close to $a$ and also strictly smaller than $a$.

    **Notice that none of the three limits necessarily exists**.

    >[!NOTE]
    >
    >Limit makes practical things easier. For example, in some sense it allows us to divide by zero. It allow us to study the local behaviormn bcc of a function (i.e. what happens to the function near a point), which usually is much simpler than studying the whole thing. A big part of Calculus only makes sense if we understand limit.
    >
    >For functions that looks 'nice' (for example, a straight line), limit will be a straight-forward idea. But weird things can happen when we talk about the general case, and that's why we need to spend some more time to understand it.

    >[!NOTE]
    >
    >One important thing about the above definition is that the limit needs to be a *single* number. It means a function can have only one limit at a point $a$ (if there is any), that is, it is impossible that $\lim\limits_{x\to 1}f(x) = 2$ but also $\lim\limits_{x \to 1}f(x) = 3$. But of course, $\lim\limits_{x \to 1}f(x)$ and $\lim\limits_{x\to 2}f(x)$ can have different values.
    >
    >However, this is no longer the case if we jump out of calculus settings. If $f$ is a function with codomain being a non-[Hausdorff space](https://en.wikipedia.org/wiki/Hausdorff_space), then it can have more than one limit point for the same $a$.

    ### Example 1 (Practical Problem)

    A famous population model is the logistic model. It models the population of a given area or the world. The dependent variable $x$ is time, and the output is, of course, the population. The logistic function reads
    $$
    f(x) = \frac{P}{1 + e^{k(x-c)}}
    $$
    where $P, k, c$ are certain parameters (i.e. fixed numbers, or constant), $k$ is negative. The output $f(x)$ when $x$ is sufficiently large enough, is close to $P$, but will never reach $L$ (why?). We say the limit of $f$ as $x$ approaches to infinity is $P$, and write $\lim\limits_{x \to \infty}f(x) = P$.

    ### Example 2

    The limit of $f(x)$ as $x$ approaches to $a$ **not necessarily has anything to do with the actual value $f(a)$**, for example, $\lim\limits_{x \to 2}f(x)=4$ in all of the following cases:

    1. $f(x) = x^2$ for $x \in [0,4]$. In this case $f(a)$ is defined and $f(a) = 4 = \lim\limits_{x \to a}f(x)$;
    2. $f(x) = \begin{cases}x^2,&x\ne 2\\10,&x=2\end{cases}$. In this case $f(a)$ is defined, but $f(a) = 10 \ne \lim\limits_{x \to a}f(x)$;
    3. $f(x) = x^2$ for $x \ne 2$. In this case $f(a)$ is not even defined, but we still have $\lim\limits_{x \to 2}f(x) = 4$.

    ## Intuitive Way to Calculate Limit

    An intuitive way to calculate limit is to plug-in values that are close to $a$, but not equal to $a$. For example, we can plugin $x = 2.00001$, $x = 2.0000001$, $x = 1.999999$, etc. in the above example, and we can see the resulting values are indeed close to $4$.

    **You should not use the intuitive way to calculate any limit on any exam or quiz** because the intuitive way of calculating the limit may not work (and the calculation is nearly impossible without a calculator anyway), here are the three usual reasons:

    1. The value you plug into the function is not close enough to $a$ (an in practice, there is no general way to decide which value is considered 'close enough' to $a$);
    2. Problems involving floating point on your calculator or computer: basically, any program, especially program that is not well-written, has a certain range of numbers it can handle, if your input is too large, too small, or have too much floating points, you may get all different kinds of errors. The book gives an example of evaluating

    $$
    \lim\limits_{t \to 0}\frac{\sqrt{t^2 + 9}-3}{t^2}.
    $$

    If you try very small value of $t = 0.0000001$, *some* calculators will tell you the answer is 0, but the true limit is $\frac{1}{6}$;

    3. **The limit does not exist**.

    ### Example 1 (Limit Does Not Exist)

    This example is known as the 'Topologist's Sine Curve'. Consider the function $f(x) = \sin(\frac{1}{x})$ for $x > 0$ and try to evaluate $\lim\limits_{x \to 0}f(x)$.

    1. If we take $\displaystyle x = \frac{1}{\pi}, \frac{1}{2\pi}, \cdots, \frac{1}{10000\pi}, \cdots$, we have $f(x) = \sin(n \pi) = 0$;
    2. If we take $\displaystyle x = \frac{2}{\pi}, \frac{2}{5\pi}, \cdots, \frac{2}{10001\pi}, \cdots$, we have $f(x) = 1$;
    3. If we take $\displaystyle x = \frac{2}{3\pi}, \frac{2}{7\pi}, \cdots, \frac{2}{10003\pi}, \cdots$, we have $f(x) = -1$.

    The problem is that there is no $L$ (**a single number**) that $f(x)$ is arbitrarily close to, no matter how close $x$ is to $0$. Thus **we say $\displaystyle \lim\limits_{x\to 0}\sin(\frac{1}{x})$ does not exist**.

    ### Example 2 (Limit Does Not Exist)

    **If the left-hand-limit and right-hand-limit both exists but not equal, we also say the limit does not exist**. For example, if
    $$
    f(x) = \begin{cases} 1,&x < 0 \\ 0,&x\ge 0\end{cases}
    $$
    then $\lim\limits_{x \to 0^-}f(x) = 1$ $\ne 0 = \lim\limits_{x \to 0^+}f(x)$. Thus $\lim\limits_{x \to 0}f(x)$ does not exist.

    ### Example 3 (Limit Does Not Exist)

    Evaluate $\displaystyle \lim\limits_{x \to 0}\frac{|x|}{x}$.

    **Absolute value function is a very special function, we should consider different cases when the input is negative or positive**. If we evaluate left-hand-limit, we have $\displaystyle \lim\limits_{x \to 0^-}\frac{|x|}{x}$ $\displaystyle = \lim\limits_{x \to 0^-}\frac{-x}{x}$ (because $x \to 0^-$ means $x$ is close to $0$ but smaller than $0$, meaning that $x$ is negative thus $|x| = -x$) $= -1$; yet if we evaluate right-hand-limit, we have $\displaystyle \lim\limits_{x\to 0^+}\frac{|x|}{x}$ $\displaystyle =\lim\limits_{x \to 0^+}\frac{x}{x} = 1$. The limits from two sides are different, thus the limit does not exist.

    ## Formal Definition of Limit

    Let $f: X \to Y$, $Y \subset \mathbb{R}$ be a function and $a \in X$. We say that $f$ approaches to $L$ as $x$ goes to $a$, and write $\lim\limits_{x \to a}f(x) = L$ provided that: for every $\varepsilon > 0$, there exists $\delta > 0$ such that $| L - f(x) | < \varepsilon$ whenever $x \in X$ and $| x - a | < \delta$.

    **You do not need to know the above definition in this course**. But if you are majoring in math, it is highly recommended to read this formal definition carefully, try some $\varepsilon$ and $\delta$ values with the examples above, and get the point of this definition - you will eventually take a course where this idea is applied everywhere. This is known as the epsilon-delta definition of limit.
    """
    )
    return


@app.cell(column=3)
def _(mo):
    mo.md(r"""# 1.4 Calculating Limits""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Limit

    Recall that we say $\lim\limits_{x\to a}f(x) = L$ if there exists $L$ such that $f(x)$ is arbitrarily close to $L$ whenever $x$ is sufficiently close to $a$.

    ## Main Limit Theorem

    We can do operations on limits in the usual sense. Remember we cannot simply divide number by zero. Suppose $\lim\limits_{x\to a}f(x)$ and $\lim\limits_{x\to a}g(x)$ both exists and $c$ denotes a constant, then:

    1. $\lim\limits_{x\to a}(f(x)+g(x)) = \lim\limits_{x\to a}f(x)+\lim\limits_{x\to a}g(x)$;
    2. $\lim\limits_{x\to a}(f(x)-g(x)) = \lim\limits_{x\to a}f(x)-\lim\limits_{x\to a}g(x)$;
    3. $\lim\limits_{x\to a}(f(x)\cdot g(x)) = \lim\limits_{x\to a}f(x) \cdot \lim\limits_{x\to a}g(x)$;
    4. $\lim\limits_{x\to a}\frac{f(x)}{g(x)} = \frac{\lim\limits_{x\to a}f(x)}{\lim\limits_{x\to a}g(x)}$ provided that $\lim\limits_{x\to a}g(x) \ne 0$;
    5. $\lim\limits_{x\to a}(cf(x)) = c \lim\limits_{x\to a}f(x)$;
    6. $\lim\limits_{x\to a}(f(x))^n = (\lim\limits_{x\to a}f(x))^n$;
    7. $\lim\limits_{x\to a}\sqrt[n]{f(x)} = \sqrt[n]{\lim\limits_{x\to a}f(x)}$;
    8. $\lim\limits_{x\to a}c = c$;
    9. **If we somehow know $f$ is continuous at $a$**, then $\lim\limits_{x\to a}f(x) = f(a)$.

    These statements also work for one-side-limits: replace all $\lim\limits_{x \to a}$ by $\lim\limits_{x \to a^+}$ or $\lim\limits_{x \to a^-}$.

    ### Example (Evaluating Limits)

    1. $\displaystyle \lim\limits_{x\to 2}\frac{x^2 + 5x + 3}{x-1}$ $\displaystyle = \frac{2^2+5\cdot 2 + 3}{2-1}$ $=17$;
    2. $\displaystyle \lim\limits_{x\to 0}(\frac{1}{x} + \frac{1}{x^2-x})$ $\displaystyle = \lim\limits_{x\to 0}\frac{x}{x^2-x}$ $\displaystyle =\lim\limits_{x\to 0}\frac{1}{x-1}$ $=-1$;
    3. $\displaystyle \lim\limits_{x\to 0}\frac{\sqrt{x^2+9}-3}{x^2}$ $\displaystyle = \lim\limits_{x\to 0}\frac{\sqrt{x^2+9}-3}{x^2} \cdot \frac{\sqrt{x^2+9}+3}{\sqrt{x^2+9}+3}$ $\displaystyle = \lim\limits_{x\to 0} \frac{x^2}{x^2(\sqrt{x^2+9}+3)}$ $\displaystyle = \lim\limits_{x\to 0}\frac{1}{(\sqrt{x^2+9}+3)} = \frac{1}{6}$.

    ## Theorem

    $\lim\limits_{x\to a}f(x) = L$ if and only if $\lim\limits_{x\to a^+}f(x) = L$ and $\lim\limits_{x\to a^-}f(x) = L$, with the possible exceptions at end-points.

    For example, if we are given $f(x)$ whose domain is $[1,2]$, then $\lim\limits_{x\to 1^-}f(x)$ does not make much sense because there is no $x$ in the domain of $f$ such is smaller than $1$: in this case, $\lim\limits_{x \to 1}f(x) = L$ as long as $\lim\limits_{x \to 1^+}f(x) = L$. Similar for the other end-point.

    ### Example 1

    Consider the function
    $$
    f(x) = \begin{cases} x^2+5x, & x<2\\ 6x+2, & x \ge 2 \end{cases}
    $$
    Does $\lim\limits_{x\to 2}f(x)$ exist? If it does, what is it?
    Using rule 9. (why are these function continuous? See [1.5 Continuity](1.5 Continuity.md)), we know $\lim\limits_{x \to 2^-}f(x) = 2^2 + 5\cdot 2 = 14$, and $\lim\limits_{x \to 2^+}f(x) = 6\cdot 2 + 2 = 14$. Since they are equal, by the above theorem, $\lim\limits_{x\to 2}f(x)$ exists and equals $14$.

    ![](/Users/zedanliu/Documents/project/marimo-notebooks/apps/public/Pasted image 20220828085649.png)

    ### Example 2

    The step function is defined to be $f(x) = \lfloor x \rfloor$ which denote the largest integer smaller than or equals to $x$. For example, $\lfloor 2 \rfloor = 2$, $\lfloor 2.5 \rfloor = 2$, and $\lfloor -2.3 \rfloor = -3$.

    The step function does not have limit at all integers. For example, $\lim\limits_{x\to2^-}f(x) = 2$ but $\lim\limits_{x \to 2^+}f(x) = 3$, thus $\lim\limits_{x\to 2} f(x)$ does not exist.

    ## Lemma

    Suppose $f(x) \le g(x)$ when $x$ is near $a$ (except possibly at $a$), and both $\lim\limits_{x\to a}f(x)$, $\lim\limits_{x\to a}g(x)$ exist, then $\lim\limits_{x\to a}f(x) \le \lim\limits_{x\to a}g(x)$.

    ## Squeeze Theorem

    Suppose $f(x) \le g(x) \le h(x)$ when $x$ is near $a$ (except possibly at $a$), and $\lim\limits_{x\to a}f(x) = \lim\limits_{x \to a}h(x) = L$, then we also have $\lim\limits_{x \to a}g(x) = L$.

    ### Example

    Evaluate $\displaystyle \lim\limits_{x\to 0}x^2\cdot\sin(\frac{1}{x})$.

    As we known from last lecture, $\displaystyle \lim\limits_{x\to 0}\sin(\frac{1}{x})$ does not exist, so we cannot just calculate the limits for two parts and multiply them together. We use the Squeeze Theorem.

    Notice that $\displaystyle -1 \le \sin(\frac{1}{x}) \le 1$, thus we have $\displaystyle -x^2 \le x^2\cdot\sin(\frac{1}{x}) \le x^2$. Now we know that $\lim\limits_{x\to 0}-x^2 = 0$ and $\lim\limits_{x\to 0}x^2 = 0$ (using rule 9.), thus by the Squeeze Theorem, we have $\displaystyle \lim\limits_{x\to 0}x^2\cdot\sin(\frac{1}{x}) = 0$.

    ## An Important Limit

    $$
    \boxed{\lim\limits_{x\to 0}\frac{\sin(x)}{x} = 1}.
    $$

    ![](/Users/zedanliu/Documents/project/math-notes/_assets/Pasted image 20220828094454.png)

    From the picture we can see when $x$ is small and greater than $0$, we have $\sin(x) < x < \tan(x)$, do some algebra we have:

    1. $\displaystyle \frac{\sin(x)}{x}<1$;
    2. $\displaystyle 1 < \frac{\tan(x)}{x} = \frac{\sin(x)}{\cos(x)\cdot x}$ $\displaystyle \implies \cos(x)< \frac{\sin(x)}{x}$.

    The Squeeze Theorem applies because $\lim\limits_{x\to 0}\cos(x) = 1$ (rule 9.), and we have $\displaystyle \lim\limits_{x\to 0^+}\frac{\sin(x)}{x} = 1$. For $x < 0$, remember sine is an odd function so we have $\displaystyle \frac{\sin(x)}{x} = \frac{\sin(-x)}{-x}$ so we have the same result.

    ### Example 1

    Evaluate $\displaystyle \lim\limits_{x\to 0}\frac{\sin(5x)}{2x}$.

    At a first glance, the answer might appear to be $1$ as a direct result of the above equality - this is **not correct**. The above equality in particular says that the limit of $\sin(\text{an expression})$ divided by **the same expression** as that expression goes to $0$, is $1$. In this example, the denominator appears to be $2x$ but the top has $\sin(5x)$ instead of $2x$, thus we need some extra effort.

    $\displaystyle \lim\limits_{x\to 0}\frac{\sin(5x)}{2x}$ $\displaystyle =\lim\limits_{x\to 0}\frac{\sin(5x)}{2x}\cdot\frac{5}{5}$ $\displaystyle =\lim\limits_{x\to 0}\frac{\sin(5x)}{5x} \cdot \frac{5}{2}$ $\displaystyle =1 \cdot \frac{5}{2}= \frac{5}{2}$. We create a quotient that is indeed $\sin(\text{an expression})$ divided by **the same expression**, also notice $5x$ indeed goes to $0$ if $x$ itself goes to $0$.

    ### Example 2

    Now we know $\displaystyle \lim\limits_{x\to 0}\frac{\sin(x)}{x} = 1$, what about $\displaystyle \lim\limits_{x\to 0}\frac{x}{\sin(x)}$?

    Simply apply rule 4. And 8.: $\displaystyle \lim\limits_{x\to 0}\frac{x}{\sin(x)}$ $\displaystyle = \lim\limits_{x\to 0}\frac{1}{\frac{\sin(x)}{x}}$ $\displaystyle = \frac{\lim\limits_{x\to 0}1}{\lim\limits_{x\to 0}\frac{\sin(x)}{x}}$ $\displaystyle = \frac{1}{1} = 1$ as well.

    ## Typical Methods to Evaluate a Limit

    1. Try first if the limit is of an indeterminant form or not, if it is not, you can simply plug in value to get result. Otherwise:
    2. If there is absolute value function involved, you should try to evaluate the limit from left and right separately;
    3. If there are trigonometry functions involved, you should try to use Squeeze Theorem or rewrite the function in terms of $\sin(\cdot)$ and apply the important limit;
    4. Otherwise, you should try to simplify the expression and try to get rid of the indeterminant form. Typical methods include combining fractions, and multiply/quotient by conjugate (useful when a square root function, or $1 \pm \cos(\cdot)$ is involved).

    Of course, these are not all possible methods to evaluate an arbitrary limit. Practice more and see what else can happen!

    ## Another Important Limit

    $$
    \lim\limits_{x\to 0}\frac{\cos(x) - 1}{x} = 0.
    $$

    This can be derived using the important limit above. The proof is left as an exercise.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r""" """)
    return


@app.cell
def _(mo):
    mo.md(r""" """)
    return


@app.cell
def _(mo):
    mo.md(r""" """)
    return


@app.cell
def _(mo):
    mo.md(r""" """)
    return


@app.cell
def _(mo):
    mo.md(r""" """)
    return


@app.cell(column=4)
def _(mo):
    mo.md(r"""# 1.5 Continuity""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Continuity

    Recall in the last lecture we had a theorem (rule 9. In [Main Limit Theorem](1.4 Calculating Limits.md#Main Limit Theorem)): if we somehow know $f$ is continuous at $a$, then $\lim\limits_{x\to a}f(x) = f(a)$.

    In fact, this is the definition (meaning this is an 'if and only if' statement) of continuous function:

    A function $f$ is continuous at $a$ if (and only if) $\lim\limits_{x \to a}f(x) = f(a)$. Notice by writing down $\lim\limits_{x \to a}f(x) = f(a)$, we are assuming that the limit of $f(x)$ as $x$ approaches to $a$ exists (left-hand-side of the equation), and $a$ is in the domain of $f$ (right-hand-side of the equation).

    >[!NOTE]
    >
    >If $a$ is not in the domain of $f$, then $f$ cannot be continuous at $a$.

    >[!CAUTION]
    >
    >Suppose the statement 'if I have class, then I go to school' is given.
    >
    >1. If I go to school, does it mean that I necessarily have class? **No**! I can still go to school if I do not have class.
    >2. If I do not go to school, does it mean that I necessarily do not have class? **Yes**! Otherwise the statement is false.
    >
    >In general, the statement 'if P, then Q' is equivalent with 'if not Q, then not P', and is **not** equivalent with 'if Q, then P'.

    Like limit, we can define one-side-continuity: a function $f$ is continuous from the right at $a$ if $\lim\limits_{x \to a^+}f(x) = f(a)$, and is continuous from the left at $a$ if $\lim\limits_{x \to a^-}f(x) = f(a)$.

    If $f$ is not continuous at $a$, we can also say that $f$ is discontinuous at $a$.

    If $f$ is continuous at every point in on an interval, we say $f$ is continuous on that interval. If $f$ is continuous at every point in its domain, we simply say $f$ is continuous, **note that a continuous function is still discontinuous at points that are not in its domain**.

    ### Example (Continuity)

    1. $\displaystyle f(x) = \frac{1}{x}$ is discontinuous at $0$, because $0$ is not even in its domain; but as the same time, $\displaystyle f(x) = \frac{1}{x}$ **is** a continuous function, because it is continuous at every point in its domain which is $\mathbb{R}\setminus \lbrace 0 \rbrace$;
    2. $f(x) = \lfloor x \rfloor$ is discontinuous at every integer $x$;
    3. $f(x) = \begin{cases} \frac{\sqrt{x^2+9}-3}{x^2}, & x \ne 0 \\ \frac{1}{6}, & x = 0\end{cases}$ is continuous everywhere, because in [last section](1.4 Calculating Limits.md#Example (Evaluating Limits)) we showed that $\displaystyle \lim\limits_{x\to 0}\frac{\sqrt{x^2+9}-3}{x^2} = \frac{1}{6}$;
    4. Similarly, if in contrary we define $f(x) = \begin{cases} \frac{\sqrt{x^2+9}-3}{x^2}, & x \ne 0 \\ 1, & x = 0\end{cases}$, then $f$ is discontinuous at $x = 0$.

    ## Construct a Continuous Function

    If $f, g$ are continuous at $a$, then $f+g, f-g, f\cdot g, f/g$ (provided that $g(a)\ne 0$) are continuous at $a$.

    If $g$ is continuous at $a$ and $g(a)=b$, and $f$ is continuous at $b$, then $f \circ g$ is continuous at $a$.

    ## Typical Continuous Functions

    1. Polynomials are continuous (in particular, constant function is continuous);
    2. Rational functions are continuous **on its domain**, in particular, they are not continuous at the points that make the denominator zero;
    3. Root functions are continuous (on its domain);
    4. Trigonometry functions are continuous on their domain: $\sin(x)$ and $\cos(x)$ are continuous at all points, $\tan(x), \cot(x), \sec(x)$ and $\csc(x)$ are continuous except at points where they are not defined.

    ### Example

    Find all possible constant $c$ that makes $f$ continuous:
    $$
    f(x) = \begin{cases} x + c, & x <0 \\ 2x^2 - c^2, & x \ge 0\end{cases}
    $$
    No matter what $c$ is, $f$ is a polynomial on $x<0$, so $f$ is continuous if $x<0$. **Similarly $f$ is continuous if $x>0$** (excluding $0$). The only possible problematic point is $x = 0$.

    At $x = 0$, we have that $\lim\limits_{x \to 0^-}f(x) = 0 + c =c$ and $\lim\limits_{x \to 0^+}f(x) = 0 - c^2 = -c^2$. We need they to be the same, thus we solve for $c = -c^2$ or $c(c+1) = 0$, we get either $c = 0$ or $c = -1$.

    >[!NOTE]
    >
    >Why can't we just say 'Similarly $f$ is continuous if $x\ge 0$' (closed interval)?
    >
    >This is because we need two-sided limit, and if we just look at the interval $[0, \infty)$ then at $0$ we only have right-side limit.

    ## Intermediate Value Theorem

    Suppose $f$ is continuous on an closed interval $[a, b]$, and $f(a) \ne f(b)$. Let $m$ be a number between $f(a)$ and $f(b)$, then there exists a number $c \in (a, b)$ such that $f(c) = m$.
    """
    )
    return


@app.cell(column=5)
def _(mo):
    mo.md(r"""# 1.6 Limits Involving Infinity""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Limits Involving Infinity

    We say that $f(x)$ goes to infinity as $x$ goes to $a$, and write $\lim\limits_{x \to a} f(x) = \infty$, provided that the value of $f(x)$ is arbitrarily large when $x$ is sufficiently close to $a$.

    ![](/Users/zedanliu/Documents/project/math-notes/_assets/Pasted image 20220902153551.png)

    The line $x = a$ is called a vertical asymptote of the graph of $f(x)$.

    We say that $f(x)$ goes to $L$ as $x$ goes to infinity, and write $\lim\limits_{x \to \infty}f(x) = L$, provided that the value of $f(x)$ is arbitrarily close to $L$ when $x$ is sufficiently large.

    ![](/Users/zedanliu/Documents/project/math-notes/_assets/Pasted image 20220902154343.png)

    The line $y = L$ is called a horizontal asymptote of the graph of $f(x)$.

    We say that $f(x)$ goes to infinity as $x$ goes to infinity, and write $\lim\limits_{x \to \infty}f(x) = \infty$, provided that the value of $f(x)$ is arbitrarily large when $x$ is sufficiently large.

    Similarly, we can talk about:

    1. $\lim\limits_{x \to a^-}f(x) = \infty$;
    2. $\lim\limits_{x \to a^+}f(x) = - \infty$;
    3. $\lim\limits_{x \to -\infty}f(x) = L$, in this case $y = L$ is also a horizontal asymptote. In particular, a function **$f$ can have at most $2$ horizontal asymptotes**;
    4. $\dots$

    All these limits, as before, do not necessarily exist.

    It is not really meaningful, however, to talk about 'the right-side-limit as $x$ goes to infinity', since infinity means being 'arbitrarily large', and it does not make much sense to have numbers to be 'larger than arbitrarily large'. In this sense, 'as $x$ goes to infinity' automatically means the left-side-limit.

    Another remark is that 'infinity' is not a number, or in symbolic language, $\infty \notin \mathbb{R}$. It is a rather abstract concept that is 'larger than any given number'. In particular, if $\lim\limits_{x \to a}f(x) = \infty$, **we still say [the limit does NOT exist](1.3 the Limit of a Function.md#Limit of a Function)**. Sometimes people call limits of this form 'improper limits'.

    >[!NOTE]
    >
    >There is another term called a slant asymptote. It happens to a rational function when the degree of the polynomial on the numerator is larger than the degree of the polynomial on the denominator. To find the slant asymptote, do a long division and collect terms with non-negative degree. For example, the function $\displaystyle \frac{x^3}{x^2 - 1}$ has a slant asymptote. Since it equals $\displaystyle \frac{x(x^2-1) + \text{extra terms}}{x^2-1}$, the slant asymptote line is $y = x$.

    ### Example 1

    1. $\displaystyle \lim\limits_{x \to 0^+} \frac{1}{x} = \infty$;
    2. $\lim\limits_{x \to \pi^-} \cot(x) = -\infty$;
    3. $\displaystyle \lim\limits_{x \to \infty} \frac{1}{x} = 0$;
    4. $\displaystyle \lim\limits_{x \to \infty} \frac{x}{x^3 + 1} = 0$;
    5. $\lim\limits_{x \to \infty} \sin(x) = \text{DNE}$.

    ### Example 2

    Find vertical and horizontal asymptotes of $\displaystyle f(x) = \frac{2x^2 + x - 1}{x^2 + x - 2}$.

    1. **Vertical asymptotes happen when, for rational functions, the denominator is zero (i.e. the function is not defined)**. In this case it means $x^2 + x - 2 = 0$, thus $x = -2$ or $1$;
    2. **Horizontal asymptotes happen at the line $y = \lim\limits_{x \to \infty}f(x)$ and $y = \lim\limits_{x \to - \infty}f(x)$ given that the limit exists**. In this case, both limits are $2$, see below for evaluation.

    ## Theorem

    Let $r > 0$ be an rational number and $c$ be any real number, then $\displaystyle \lim\limits_{x \to \infty}\frac{c}{x^r} = 0$ and $\displaystyle \lim\limits_{x \to -\infty} \frac{c}{x^r} = 0$.

    ## Indeterminate Forms

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

    ### Example

    The method we use is 'quotient by the highest power'.

    $\displaystyle \lim\limits_{x \to \infty} \frac{3x+5}{x-4}$ $\displaystyle = \lim\limits_{x \to \infty} \frac{\frac{3x}{x}+\frac{5}{x}}{\frac{x}{x}-\frac{4}{x}}$ $\displaystyle = \lim\limits_{x \to \infty}\frac{3 + \frac{5}{x}}{1 - \frac{4}{x}}$, now we use the above theorem that $\displaystyle \lim\limits_{x\to \infty}\frac{5}{x} = 0$ and $\displaystyle \lim\limits_{x \to \infty}\frac{4}{x} = 0$, so the limit we have $\displaystyle = \frac{3+0}{1 - 0} = 3$.

    ### Important Remark

    You must write $\lim\limits_{x \to a}$ operator **at each step**.

    You *can* just write $\lim$ (without $x \to a$) **starting from the second step**, if you are not changing $a$. However, you **cannot** completely omit the limit operator - it is mathematically **wrong** if you do so.

    ### More Examples

    1. $\lim\limits_{x \to \infty} \sqrt{64x^2 + x} - 8x$ $\displaystyle =\lim\limits_{x\to \infty}(\sqrt{64x^2+x}-8x)\cdot \frac{\sqrt{64x^2+x}+8x}{\sqrt{64x^2+x}+8x}$ $\displaystyle =\lim\limits_{x\to \infty}\frac{64x^2+x-64x^2}{\sqrt{64x^2+x}+8x}$ $\displaystyle =\lim\limits_{x\to \infty}\frac{x}{\sqrt{64x^2+x}+8x}$ $\displaystyle =\lim\limits_{x\to \infty}\frac{1}{\sqrt{64+\frac{1}{x}}+8}$ $\displaystyle =\frac{1}{\sqrt{64}+8}$ $\displaystyle = \frac{1}{16}$;
    2. $\displaystyle \lim\limits_{x \to \infty} \frac{\sqrt{4x^2+5}}{x-2} =$ $\displaystyle \lim\limits_{x\to \infty} \frac{\sqrt{4x^2+5}/x}{(x-2)/x}$ $\displaystyle = \lim\limits_{x\to \infty} \frac{\sqrt{\frac{4x^2}{x^2} + \frac{5}{x^2}}}{\frac{x}{x}- \frac{2}{x}}$ $\displaystyle = \lim\limits_{x\to \infty} \frac{\sqrt{4 + \frac{5}{x^2}}}{1 - \frac{2}{x}}$ $\displaystyle = \frac{\sqrt{4}}{1} = 2$. **Notice here the 'highest power' is $1$**, instead of $2$, that is because terms appear inside a square-root only have half of the power as it appears to have, e.g. $\sqrt{x^8}$ is actually a term with degree $4$.

    A particularly interesting example as a variation is $\displaystyle \lim\limits_{x \to -\infty} \frac{\sqrt{4x^2+5}}{x-2} =$ $\displaystyle \lim\limits_{x\to -\infty} \frac{\sqrt{4x^2+5}/x}{(x-2)/x}$ $\displaystyle = \lim\limits_{x\to \infty} \frac{{\color{red}-}\sqrt{\frac{4x^2}{x^2} + \frac{5}{x^2}}}{\frac{x}{x}- \frac{2}{x}}$ $= \lim\limits_{x\to \infty} \frac{{\color{red}-}\sqrt{4 + \frac{5}{x^2}}}{1 - \frac{2}{x}}$ $\displaystyle = {\color{red}-}\frac{\sqrt{4}}{1} = -2$. This is because $\sqrt{x^2} = |x|$, thus if $x$ is negative, we have $\sqrt{x^2} = -x$. This makes sense: the expression $\displaystyle \frac{\sqrt{4x^2+5}}{x-2}$, when $x$ is negative, is a positive number (square root is always non-negative, by definition) divided by a negative number, thus a negative number.

    Moral of the story: be very careful about signs, especially when square root is involved.
    """
    )
    return


if __name__ == "__main__":
    app.run()
