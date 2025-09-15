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
    mo.md(r"""# 4.2 Definite Integral""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Definite Integral""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose $f$ is continuous on $[a, b]$ (notice this is a closed interval). Recall from last section that the signed area $A$ under the curve $f$ on $[a, b]$ is calculated as $$A = \lim\limits_{n \to \infty}\sum_{i = 1}^nf(x_i^*)\Delta(x),$$ where $\displaystyle \Delta(x) = \frac{b-a}{n}$, $[a,b]$ is divided into $n$ sub-intervals with equal length (in particular, each interval has length $\Delta(x)$), and $x_i^*$ is any number in the $i$-th sub-interval mentioned above.

    **Define** this limit to be the definite integral of $f$ from $a$ to $b$, and denote it $\int_a^bf(x)dx$. In other words, $$\int_a^bf(x)dx := \lim\limits_{n \to \infty}\sum_{i = 1}^n f(x_i^*)\Delta(x).$$ **Put it in words, the definite integral of $f$ from $a$ to $b$ is defined to be the signed area of the region bounded by $f$, $x = a$, $x = b$, and the $x$-axis**.

    The sum $\displaystyle \sum_{i = 1}^n f(x_i^*)\Delta(x)$ is known as a Riemann sum, **it can be negative or positive (thus so does the definite integral)**. $f(x)$ is called the integrand, $a$ is called the lower limit (or lower bound), $b$ is called the upper limit (or upper bound).
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
    Write down the expression for $\displaystyle \int_1^3\sin(\sqrt{x})dx$ has a limit of Riemann sum.

    From the integral notation, we know $a = 1$ and $b = 3$, thus $\displaystyle \Delta(x) = \frac{b-a}{n} = \frac{2}{n}$. If we divide $[a, b] = [1, 3]$ to $n$ equal parts, then they are $\displaystyle [1, 1 + \frac{2}{n}]$, $\displaystyle [1 + \frac{2}{n}, 1 + \frac{4}{n}]$, $\displaystyle [1 + \frac{4}{n},1 + \frac{6}{n}]$, $\dots$, $\displaystyle [1 + \frac{2(n-1)}{n}, 1 + \frac{2n}{n} = 3]$. Since $x_i$ can be chosen arbitrarily from those intervals, let us for example just choose the right endpoint. That is, $\displaystyle x_1^* = 1+ \frac{2}{n}$, $\displaystyle x_2^* = 1+ \frac{4}{n}$, $\displaystyle x_3^* = 1+ \frac{6}{n}$, $\dots$, $\displaystyle x_n^* = 1 + \frac{2n}{n}$.

    We should realize there is a simpler way to write $x_i^*$'s: we start with $1$, and each step we add $\displaystyle \frac{2}{n}$. Thus $x_i^*$ (the right endpoint) can be written as $\displaystyle x_i^* = 1 + i\cdot \frac{2}{n}$.

    So now we get what are the $x_i^*$'s and what is $\Delta(x)$, we can plug them into the definition and get: $$\int_1^3\sin(\sqrt{x})dx = \lim\limits_{n \to \infty}\sum_{i = 1}^n\left[\sin(\sqrt{1 + i \cdot \frac{2}{n}})\frac{2}{n}\right].$$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Remark 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    For an arbitrary function $f$ on $[a,b]$, the limit $\displaystyle \lim\limits_{n \to \infty}\sum_{i = 1}^n f(x_i^*)\Delta(x)$ may not exist. **When this limit does not exist, we say $f$ is not integrable on $[a,b]$ (recall that if this limit is infinity, it is also counted as 'not exist')**; and when this limit does exist, we say $f$ is integrable on $[a, b]$.

    **Continuous $f$ is always integrable**. But continuity is not necessary for a function to be integrable. **Unbounded $f$ (i.e. it has a vertical asymptote on $[a,b]$) is *never* integrable**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Remark 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""As a matter of fact, we do not even need to divide $[a, b]$ into $n$ **equal** parts. However, the choice of this partition is also not arbitrary. It is rather hard (and beyond the scope of this course) to carefully define those things."""
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
    $\displaystyle f(x) = \begin{cases}\frac{1}{x}&,x\ne 0 \\ 0&,x = 0 \end{cases}$ is not integrable on $[0,1]$. The function is not bounded.

    What about $[-1, 1]$? There could be a debate on this:

    1. The answer is $0$, because of symmetry;
    2. The answer is undefined, for the same reason that it is not defined on $[0,1]$.

    To be consistent with other topics, we usually take the second reasoning: it is undefined on $[-1,1]$ despite of the symmetry.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Properties of Definite Integral""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The book continues this section in a pretty formal and careful way. In some sense those formalities are not needed. **There are many properties of definite integral that can be understood in a rather intuitive way**.

    Let us assume the function being integrated is continuous.

    1. **First, recall that the definite integral is the same as signed area**;
    2. $\displaystyle \int_a^b f(x) dx = - \int_b^a f(x)dx$: from the definition we should have the upper bound to be no less than the lower bound - but, in case that the upper bound is smaller, you can view the signed area as a signed area that 'goes to the other direction', thus in some sense it should have the **opposite sign** with the bound flipped;
    3. $\displaystyle \int_a^a f(x) dx = 0$: area of a line segment is $0$;
    4. $\displaystyle \int_a^b c dx = (b-a)c$: the integral can be interpret as the area of the region bounded by the $x$-axis, $x = a$, $x = b$, and $y = c$, which is a rectangle with height $c$ and length $b-a$, thus the (signed) area is $(b-a)c$;
    5. The following properties involving operations are due to the fact you can do operations to shapes:
    	1. $\displaystyle \int_a^b cf(x)dx = c\int_a^b f(x)dx$;
    	2. $\displaystyle \int_a^b f(x) + g(x) dx = \int_a^b f(x) dx + \int_a^b g(x) dx$;
    	3. For any real numbers $a, b, c$, $\displaystyle \int_a^b f(x) dx = \int_a^c f(x) dx + \int_c^b f(x) dx$;
    6. Comparison Properties, those should also be intuitive when interpreting geometrically:
    	1. If $f(x) \ge 0$ on $[a, b]$, then $\displaystyle \int_a^b f(x) dx \ge 0$;
    	2. If $f(x) \ge g(x)$ on $[a, b]$, then $\displaystyle \int_a^b f(x) dx \ge \int_a^b g(x) dx$;
    	3. In particular, if $m \le f(x) \le M$ on $[a, b]$, then $\displaystyle \int_a^b m dx \le \int_a^b f(x) dx \le \int_a^b M dx$, thus $\displaystyle m(b-a) \le \int_a^b f(x) dx \le M(b-a)$ due to the above property.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Exercises""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. Evaluate $\displaystyle \int\limits_0^{10}| x - 5 | dx$ using the property of definite integral;
    2. If $\displaystyle \int_1^5 f(x) dx = 12$ and $\displaystyle \int_4^5 f(x) dx = 4$, what is $\displaystyle \int_1^4 f(x) dx$?
    """
    )
    return


if __name__ == "__main__":
    app.run()
