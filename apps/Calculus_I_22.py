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
    mo.md(r"""# 4.3 Evaluating Definite Integrals""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Evaluation Theorem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    If $f$ is **integrable** on $[a, b]$, then $\displaystyle \int\limits_a^b f(x) dx = F(b) - F(a)$, where $F$ is an antiderivative of $f$, i.e. $F$ is *any* function satisfies that $F'(x) = f(x)$.

    There are several remarks about the theorem:

    1. This theorem is a part of the so called 'Fundamental Theorem of Calculus';
    2. A rather surprising fact: **the valuation of definite integral depends only on the values of antiderivative at two end-points**;
    3. Same as all the theorem before, whenever we use a theorem we need to be sure if we satisfy the assumption. With this theorem, we need to have $f$ being **integrable** on a closed interval $[a, b]$. Recall that if $f$ is continuous, then $f$ is integrable: thus continuous function always satisfies the assumption. However, continuity is not necessary, see examples below;
    4. Any antiderivative works. Remember if $F$ is an antiderivative of $f$, then $F+c$ is also an antiderivative of $f$ for any $c$. For example, $\cos(x)$ is antiderivative of $\sin(x)$, $\cos(x) + c$ is also an antiderivative of $\sin(x)$. **But usually when we evaluate definite integral**, we use the 'simplest' antiderivative, i.e. $c = 0$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Examples""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Evaluate the following definite integral.

    1. $\displaystyle \int\limits_0^21+3y-y^2dy$. This example has nothing special: the integrand is continuous everywhere, so in particular it is continuous on $[0,2]$. It's antiderivative (general form) is $\displaystyle y + \frac{3}{2}y^2 - \frac{1}{3}y^3 + c$ and we can take $c = 0$ and set $\displaystyle F(y) = y + \frac{3}{2}y^2 - \frac{1}{3}y^3$. Thus $\displaystyle \int\limits_0^21+3y-y^2dy$ $= F(2) - F(0)$ $\displaystyle = 2 + 6 - \frac{8}{3} - 0$ $\displaystyle = \frac{16}{3}$;
    2. $\displaystyle \int\limits_{-\pi}^{\pi} \sin(x) dx$. Again, the integrand is continuous (everywhere). In this example, notice that $\sin(x)$ is an odd function and lower limit equals negative upper limit, thus the area of regions we are evaluating 'cancel' each other, the result should be $0$;
    3. $\displaystyle \int\limits_{-1}^1 \frac{1}{x} dx$. Recall from last lecture, this integral is not defined although the integrand is also an odd function and lower limit equals negative upper limit. The problem is that the integrand is not bounded;
    4. $\displaystyle \int\limits_{-\pi}^{\pi} | \sin(x) | dx$. The integrand is continuous everywhere and is not an odd function. However, it is not easy to find an antiderivative of $| \sin(x) |$ so we cannot simply evaluate it like example 1. The way we evaluate this integral to to write $\displaystyle \int\limits_{-\pi}^{\pi} | \sin(x) | dx$ $\displaystyle = \int\limits_{-\pi}^{0} -\sin(x) dx + \int\limits_{0}^{\pi} \sin(x) dx$ then evaluate in the usual way. Notice in the first part the integrand becomes $-\sin(x)$ because $\sin(x)$ on $(-\pi,0)$ is negative but $| \sin(x) |$ should be positive;
    5. $\displaystyle \int\limits_{-1}^1f(x)dx$ where $f(x) = \begin{cases}1&,x \in [-1,0] \\ \sin(x)&,x \in (0,1]\end{cases}$. An easy calculation would reveal that $f$ is not continuous on $[-1,1]$. However, we can view this definite integral as 'calculate the area under $y = 1$ on $[-1, 0]$ and the area under $y = \sin(x)$ on $(0,1]$', and notice that the area under $y = \sin(x)$ on $(0,1]$ is really the same as the area under $y = \sin(x)$ on $[0,1]$ (why?). Thus $\displaystyle \int\limits_{-1}^1f(x)dx$ $\displaystyle = \int\limits_{-1}^01dx + \int\limits_0^1\sin(x)dx$. In particular, this means **sometimes** we can do something to discontinuous $f$ so that we can still take the definite integral;
    6. Again consider $\displaystyle \int\limits_{-1}^1 \frac{1}{x} dx$. The integrand is not continuous at $0$, and we know that this definite integral is not defined. The point is: indeed it is **not always** that we can integrate discontinuous functions;
    7. **Simplification is crucial in taking integral**. Unlike taking derivative, where the product rule/quotient rule/chain rule can help us take derivative of all elementary functions, there is no such powerful rule in taking integral (there are rules, but not that powerful). Thus simplification will really be helpful. For example, it is impossible to evaluate $\displaystyle \int\limits_{0}^{\pi}\frac{\sin(x) + \sin(x)\tan^2(x)}{\sec^2(x)}dx$ directly. However, if we simplify the integrand and realize $\displaystyle \frac{\sin(x) + \sin(x)\tan^2(x)}{\sec^2(x)}$ $=\sin(x)$, then the definite integral is actually very easy to evaluate.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Motion Problem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Let $v(t) = t^2 - 2t - 8$ and $1 \le t \le 6$. $v$ is the velocity function for a particle along a straight line.

    What is the displacement function?

    To answer this question, probably we should ask first, what is a displacement function? From the name, displacement function should describe the displacement of the particle. That is, if we input the time $t$, the output should be the displacement of the particle during the time between starting point and $t$. In particular, if we know the position function $s(t)$, then in this problem, the displacement function should be $p(t) = s(t) - s(1)$.

    Recall that the derivative of position function gives us the velocity function. Thus position function is an antiderivative of the velocity function. Thus by the Evaluation Theorem, $\displaystyle s(t) - s(1) = \int\limits_1^t v(x) dx$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Dummy Variable
        type: info

    Notice we use another variable for the input of $v$. In general, the variable in the integrand can be changed arbitrarily (afterall, it is really just a name), $\displaystyle \int_a^b f(x)dx$ is the **same things** as $\displaystyle \int_a^b f(🍩)d🍩$.

    Here we used a general rule: **never let a variable appear both after $d$ and in the upper or lower limit**, for example, it is problematic to write $\displaystyle \int_x^b f(x) dx$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    In other words, $\displaystyle p(t) = \int\limits_1^t x^2 - 2x - 8 dx$. Choose an antiderivative for $v(x)$, say $\displaystyle V(x) = \frac{1}{3}x^3 - x^2 - 8x$, then $\displaystyle p(t) = V(t) - V(1) = \frac{1}{3}t^3 - t^2 - 8t - (\frac{1}{3} - 1 - 8)$ $\displaystyle = \frac{1}{3}t^3 - t^2 - 8t + \frac{26}{3}$.

    What is the displacement during the time period $1 \le t \le 6$?

    This question is the same as 'what is $p(6)$?'. Plugin $t = 6$, we get $\displaystyle p(6) = \frac{1}{3}6^3 - 6^2 - 8\cdot 6 + \frac{26}{3} = -\frac{10}{3}$ (it is the same as $\displaystyle \int_1^6v(t)dt$).

    What is the distance travelled during this time period?

    This question is asking us to evaluate the **unsigned area** of region under curve $v(t)$, or say, the area under curve $| v(t) |$. In order to find it, we need to know when is $v(t)$ positive and when is $v(t)$ negative.

    Write $v(t) = t^2 - 2t - 8 = (t-4)(t+2)$, we should be able to derive from there that if $1 \le t \le 4$, $v(t) \le 0$, and if $4 \le t \le 6$, then $v(t) \ge 0$. Thus $\displaystyle \int_1^6 | v(t) | dt = \int_1^4 -v(t) dt + \int_4^6 v(t) dt$ $\displaystyle = \int_1^4 - t^2 + 2t + 8 dt + \int_4^6 t^2 - 2t - 8 dt$. Evaluate in the usual ways, we get $\displaystyle = 18 + \frac{44}{3}$ $= \frac{98}{3}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Indefinite Integral""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The indefinite integral is not at all a new concept. It is really just another name for antiderivative. When we talk about 'indefinite integral of $f$' we are assuming we are talking about 'general form of antiderivative of $f$'. In particular, **do not forget $+c$**. The notation of indefinite integral of $f$ is $\displaystyle \int f(x) dx$.

    By above, we have $\displaystyle \int f(x) dx = F(x) + c$ where $F(x)$ is a function such that $F'(x) = f(x)$ and $c$ is an arbitrary number. So for example, the indefinite integral $\displaystyle \int \sin(x) dx$ equals $-\cos(x)+c$.
    """
    )
    return


if __name__ == "__main__":
    app.run()
