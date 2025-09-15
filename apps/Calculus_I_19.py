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
    mo.md(r"""# 3.7 Antiderivative""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Motivative""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    When we do differentiation, i.e. take derivative, we essentially know the relation between two quantities, and calculate the rate of change of one quantities with respect to the other. For example, we have the example when we introduce differentiation, that we know the position of a ball (i.e. the relation between position and time), and we want to know the rate of change of position with respect to time (i.e. the derivative, or the velocity).

    It is then a natural question to ask: can we go backwards? If we know the rate of change, can we derive the relation?

    Take some time to think about it, the answer should be 'yes and no'. Let us again use the velocity example.

    We can derive some information of the position - suppose we are on a straight road **and we know where we are right now**, we also know we were moving at $60 \text{ m/min}$ (for the last minute) along the road. Then we should know that, exact one minute ago, we were located at $60$ meters from where we are right now back on the road (i.e. we get a relation between our position and time).

    However, we can only know exactly where were we **if we know where are we right now**. If we just know the velocity, but not the current location, then we can only say that one minute ago we were $60$ meters from the current location, **but we don't know where exactly it is**.

    This translates to the general idea:

    1. A function $F$ is called **an** antiderivative of $f$ (on an interval $I$) if $F'(x) = f(x)$ (for all $x \in I$);
    2. Antiderivative for a function is **not unique**, if $F$ is an antiderivative of $f$ on $I$, then $G(x) = F(x) + c$ for any constant number $c$ is also an antiderivative for $f$ on $I$. If $F$ is an antiderivative of $f$, then $F(x) + c$ is called the general form of antiderivative.

    For example, if $f(x) = 2x$, then $F(x) = x^2$ is **an** antiderivative of $f$, because $F'(x) = 2x$. Since we know the derivative of a constant is always $0$ and we know the summation rule of differentiation, it should not be hard to see that $G(x) = x^2 + 1$ also has $G'(x) = 2x = f(x)$ thus **it is also an antiderivative** of $f$. Similarly, $H(x) = x^2 + c$ for any given constant $c$ is an antiderivative of $f$.

    **Moral of the story: always write $+c$ when you take antiderivative**.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Antidifferentiation Formulas""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    From above, you may probably see that antidifferentiation is some kind of converse of differentiation (that is where it gets its name after all). Here we are writing down the same formulas for derivatives, just use it backwards… **and plus a constant**.

    | Function | Antiderivative |
    |:--|:--|
    | $x^n, n\ne -1$ | $\displaystyle \frac{x^{n+1}}{n+1} + c$ |
    | $\cos(x)$ | $\sin(x) + c$ |
    | $\sin(x)$ | $-\cos(x) + c$ |
    | $\sec^2(x)$ | $\tan(x) + c$ |
    | $\sec(x)\tan(x)$ | $\sec(x) + c$ |
    | $\csc^2(x)$ | $-\cot(x) + c$ |
    | $\csc(x)\cot(x)$ | $-\csc(x) + c$ |

    We also have some basic rules:

    1. If $F$ is an antiderivative of $f$, then $a\cdot F$ is an antiderivative of $a\cdot f$ for any constant $a$;
    2. If $F$ is an antiderivative of $f$ and $G$ is an antiderivative of $g$, then $F+G$ is an antiderivative of $f+g$. Notice that we do not need to write two constant terms when we add them together: a constant plus a constant just gives another (possibly different) constant.

    There is a rule in antidifferentiation corresponds to the Chain Rule in differentiation. We will study them in the next chapter.

    For now, you should know that: taking antiderivative in general is **much harder** than taking derivative. We are able to differentiate **all** elementary functions, and functions that are built from them (product, quotient, composition, etc.). But this is not the case in antidifferentiation. There are functions that does not have (elementary) antiderivatives - many of them looks 'simple', here are some typical examples:

    1. $\displaystyle \frac{\sin(x)}{x}$;
    2. $\sin(x^2)$;
    3. $\displaystyle \frac{1}{\ln(x)}$;
    4. $\dots$

    A good exercise is to try to think of some functions that has derivatives of the above functions - and see why they fail.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Differential Equation""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    An equation that involves derivatives of a function is called a differential equation. There are ordinary differential equations and partial differential equations.

    The study of differential equations is one of the most important sub-field of applied math, and plays important role in physics, economics, finance, bio-math, etc. For example:

    1. Black-Scholes Equation for stock-option pricing;
    2. Lotka–Volterra Equations for modeling predator/prey populations of two species;
    3. In general, there are heat equations, wave equations, etc. in physics.

    Antidifferentiation is the most basic type of differential equation.
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
    Find the general form of antiderivative of $\displaystyle f(x) = 4\sin(x) + \frac{2x^5 - \sqrt{x}}{x}$.

    There is no formula to take care of antiderivatives in quotient form, so **do not try to take antiderivative directly of a quotient**. Instead, we rewrite it to functions that we are familiar with.

    $\displaystyle f(x) = 4\sin(x) + \frac{2x^5}{x} - \frac{\sqrt{x}}{x}$ $= 4\sin(x) + 2x^4 - x^{-1/2}$, and we look at it term-by-term:

    1. The antiderivative of $\sin(x)$ is $-\cos(x)+c$, thus the antiderivative of $4\sin(x)$ is $-4\cos(x) + c$;
    2. The antiderivative of $x^4$ is $\displaystyle \frac{x^5}{5}+c$, thus the antiderivative of $2x^4$ is $\displaystyle \frac{2x^5}{5}+ c$;
    3. The antiderivative of $x^{-1/2}$ is $\displaystyle \frac{x^{1/2}}{1/2}+c$, or $2x^{1/2}+c$.

    Put things together with summation (and subtraction) rule, we get that the antiderivative of $\displaystyle 4\sin(x) + \frac{2x^5 - \sqrt{x}}{x}$ is $\displaystyle -4\cos(x) + \frac{2x^5}{5} - 2x^{1/2} + c$. **Be careful about the signs before each term**, and notice we only $+c$ at the very end, and do not need to write $+c$ three times when we put things together.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Differential Equation with Initial Condition""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""Sometimes we will be given extra information so that we can determine what is the constant term $c$. This information is usually called initial condition."""
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
    Suppose $F$ is an antiderivative of $\displaystyle f(x) = 4\sin(x) + \frac{2x^5 - \sqrt{x}}{x}$, we also know that $F(0) = 3$, find $F$.

    From above we know the general form of $F$, that is, $\displaystyle F(x) = -4\cos(x) + \frac{2x^5}{5} - 2x^{1/2} + c$. We now also know $F(0) = 3$, plug this piece of information into our equation, we get $F(0) = -4\cos(0) + 0 - 0 + c = 3$, or $-4 + c = 3$, which implies $c = 7$.

    Thus we have a specific solution, that is $\displaystyle F(x) = -4\cos(x) + \frac{2x^5}{5} - 2x^{1/2} + 7$. This is **the** function that is an antiderivative of $f$, also satisfy the initial condition.
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
    A ball is thrown **upward** with a speed of $6 \text{ m/s}$ at level $1 \text{ m}$. Write down the relation between its height (in meters) above ground and time (in seconds). Specify the domain of your function so that it makes sense, assume the ball stay still after it touches the ground.

    The concealed information is that the ball is under the effect of gravity (well, let us assume the ball is thrown on earth). Since the ball is thrown upward and gravity goes downward, the ball has an acceleration of $-10 \text{ m/t}^2$. Notice if the unit in the question is feet, then the number is $-32$.

    That is, if $v(t)$ is the velocity of the ball and $a(t)$ is the acceleration, then we know $v(t)$ is an antiderivative of $a(t) = -10$, thus $v(t) = -10t + c$. Since we know initially $v(0) = 6$, plugin and we get $c = 6$, that is, $v(t) = -10t + 6$.

    The height (position) function $s(t)$ is an antiderivative of $v(t)$, thus $s(t) = -5t^2 + 6t + c$. We are also given that $s(0) = -0+0+c = 1$, thus $c = 1$ and $s(t) = -5t^2+6t +1$.

    The ball hit the ground when $s(t) = 0$, that is $-5t^2 + 6t +1 = 0$. Use quadratic formula to get that $\displaystyle t = \frac{3 \pm \sqrt{14}}{5}$.

    Apparently $t$ should be non-negative thus the feasible $t$ is $\displaystyle \frac{3 + \sqrt{14}}{5}$.

    Thus the final answer should be $s(t) = -5t^2 + 6t +1$, $\displaystyle 0 \le t \le \frac{3 +\sqrt{14}}{5}$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Sigma Notation""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The Sigma notation is a convenient way of writing (a long) sums using the greek letter $\Sigma$:

    Let $a_m, a_{m+1}, \dots, a_n$ be numbers, $m, n$ are integers such that $m \le n$, then the notation $\displaystyle \sum\limits_{i = m}^na_i$ stands for $a_m + a_{m+1} + \dots + a_n$. The letter $i$ is called the index of summation. It takes consecutive integer values starts with $m$ and ends with $n$ (inclusive), i.e. $m$, $m+1$, $\dots$, $n$. You can of course use other letters, but usually we use $i, j, k$ or greek letters $\alpha, \beta$. The $a_i$'s are the terms to be summed together, called summands, usually it is written as a function of $i$ (the index).

    Notice **this is merely a notation**, there is no real difference between $\displaystyle \sum\limits_{i = m}^na_i$ and $a_m + a_{m+1} + \dots + a_n$. This is just a convenient way of writing. For example:

    1. $\displaystyle \sum\limits_{i = 1}^5i^2$ is the same as $1^2 + 2^2 + 3^2 + 4^2 + 5^2$;
    2. $\displaystyle \sum\limits_{i = 1}^{10}1$ is the same as $\overbrace{1 + 1 + 1 + \dots + 1}^{10\text{ times}}$, notice the summands do not depend on $i$ here;
    3. $\displaystyle \sum\limits_{i = 3}^62^i$ is the same as $2^3 + 2^4 + 2^5 + 2^6$, notice the index does not start with $1$ here;
    4. $\displaystyle \sum\limits_{i = -3}^1 \frac{5+13i}{i^3-\cos(i\pi)}$ is the same as $\displaystyle \frac{5+13\cdot(-3)}{(-3)^3-\cos(-3\pi)} + \frac{5+13\cdot(-2)}{(-2)^3-\cos(-2\pi)}$ $\displaystyle + \frac{5+13\cdot(-1)}{(-1)^3-\cos(-1\pi)}$ $\displaystyle + \frac{5+13\cdot 0}{0^3-\cos(0\pi)}$ $\displaystyle + \frac{5+13\cdot(1)}{1^3-\cos(1\pi)}$, notice the index can also start with a negative integer, also notice that the summands can be complicated, it is any function depends or does not depend on the index.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Index
        type: info

    In a summation, we often use $i$ as the index. You should understand that **this $i$ has nothing to do with imaginary numbers**. Whether $i$ is some index or a square root of $-1$ should be clear from the context.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Basic Rules of Sigma Notation""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. If $c$ is a constant, then $\displaystyle \sum\limits_{i = m}^nca_i = c \sum\limits_{i = m}^na_i$ (i.e. we can pull the constant out from the summation). This is equivalent with the distribution law: $ca_m + ca_{m+1} + \dots + ca_n$ $= c(a_m + a_{m+1} + \dots + a_n)$;
    2. $\displaystyle \sum\limits_{i = m}^{n}(a_i + b_i)$ $\displaystyle = \sum\limits_{i = m}^n a_i + \sum\limits_{i = m}^n b_i$. This is due to the commutativity property of summation;
    3. Similarly, $\displaystyle \sum\limits_{i = m}^{n}(a_i - b_i)$ $\displaystyle = \sum\limits_{i = m}^n a_i - \sum\limits_{i = m}^n b_i$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Summation Rule""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Recall we have the summation rule, known as the Gauss's Trick, that if $n$ is an positive integer, then $\displaystyle 1 + 2 + \dots + n$ $\displaystyle = \frac{(1+n)n}{2}$.

    Written in Sigma notation, we have $$\sum\limits_{i = 1}^n i = \frac{n(n+1)}{2}.$$ Similarly there are two other formulas: $$\sum\limits_{i = 1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$$ and $$\sum\limits_{i = 1}^n i^3 = \left[\frac{n(n+1)}{2}\right]^2.$$
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
    Simplify $\displaystyle \sum\limits_{i = 1}^n(4 - \frac{3i^2}{n^2})\frac{4}{n}$ and evaluate $\displaystyle \lim\limits_{n \to \infty}\sum\limits_{i = 1}^n(4 - \frac{3i^2}{n^2})\frac{4}{n}$.

    $\displaystyle \sum\limits_{i = 1}^n(4 - \frac{3i^2}{n^2})\frac{4}{n}$ $\displaystyle = \frac{4}{n}(\sum\limits_{i = 1}^n4 - \sum\limits_{i=1}^n \frac{3i^2}{n^2})$ $\displaystyle =\frac{4}{n}(4n - \frac{3}{n^2}\sum\limits_{i=1}^ni^2)$ $\displaystyle = \frac{4}{n}(4n - \frac{3}{n^2} \frac{n(n+1)(2n+1)}{6})$ $\displaystyle = 16 - \frac{2(n+1)(2n+1)}{n^2}$.

    So the limit is $\displaystyle \lim\limits_{n \to \infty}\sum\limits_{i = 1}^n(4 - \frac{3i^2}{n^2})\frac{4}{n}$ $\displaystyle = \lim\limits_{n \to \infty}16 - \frac{2(n+1)(2n+1)}{n^2}$ $= 16-4 = 12$.
    """
    )
    return


if __name__ == "__main__":
    app.run()
