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
    mo.md(r"""# 4.5 Substitution Method""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Introduction""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Say $f(x) = \sin(x^2)$, we can use the Chain Rule to calculate $f'(x) = 2x\cdot\cos(x^2)$. That is to say, $2x \cdot \cos(x^2)$ is an antiderivative of $\sin(x^2)$, thus if we want to evaluate $\displaystyle \int 2x\cdot\cos(x^2) dx$, we know it should equal $\sin(x^2)+C$. Or if we want to evaluate $\displaystyle \int\limits_a^b 2x\cdot\cos(x^2) dx$, we know it should equal $\sin(b^2) - \sin(a^2)$.

    Let us generalize this idea:
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## The Substitution Rule (for Indefinite Integral)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""Suppose $g(x)$ is differentiable (with range $I$) and $f, g'$ are integrable (on $I$). Write $u = g(x)$ for simplicity, then: $$\boxed{\int f(u)u'~dx = \int f(u)du}.$$ The important point is that the variable that we take integration with has changed. The process of applying the Substitution Rule is sometimes referred as 'U-substitution', because we often use $u$ as the dummy variable in the mid-step."""
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Sustitution Rule and Chain Rule
        type: info

    The Substitution Rule can be viewed as the inverse of Chain Rule. It is not nearly as powerful as the Chain Rule, though. Take the example above, we can only take integration because there is an $2x$ term 'outside' of $\cos(x^2)$, which coincidentally is the derivative of $x^2$. There is no way (using elementary functions) to find the integral of $\cos(x^2)$ by itself.

    ///
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
    Evaluate $\displaystyle \int \cos^4(x)\sin(x)dx$.

    Consider $u = \cos(x)$ and $f(u) = u^4$, then $u' = - \sin(x)$, and the original integral can be written as $\displaystyle -\int \cos^4(x)\cdot(-\sin(x))dx$ $\displaystyle = - \int f(u)u'~dx$ $\displaystyle = -\int f(u) du$ by the Substitution Rule.

    That is, the original integral is the same as $\displaystyle - \int u^4 du$, which equals $\displaystyle - \frac{u^5}{5} + C$. Substitute back to $x$ using $u = \cos(x)$, we get $\displaystyle = - \frac{\cos^5(x)}{5} + C$.

    It is **very** common to have a term that does not match. In above example, we do not have $-\sin(x)$ at the beginning. We have to create a $-1$ by taking product of the original integral with $1 = -1 \cdot -1$, then proceed. Do not forget to time the other $-1$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | When to Use U-Substitution and How to Choose U
        type: danger

    If there is a composition of functions, then a U-substitution should be considered. Like a Chain Rule, the first candidate for $u$ is the part 'inside'.

    When you apply the Chain Rule, you are creating a product. **Thus when you do a U-substitution (which can be viewed as the inverse) and you can notice a product, then you should look for the 'more complicated' one, and use the 'inside' part as your $u$**.

    For example, if the original integrand is $\displaystyle \sqrt{x} \cdot \sin(1 + x^{3/2})$, then you can view it as the product of $\sqrt{x}$ and $\displaystyle \sin(1 + x^{3/2})$. The latter seems 'more complicated' (it has trigonometry function & a complicated power), and it is composition of sine function and $1+x^{3/2}$. Thus a natural selection for $u$ is $1 + x^{3/2}$.

    **But, you should understand that this is not the only way to determine U. For example, if you want to calculate $\displaystyle \int \sqrt{1 - x^2}dx$, then you should in fact substitute $x = \cos(u)$ or $x = \sin(u)$. This is not needed for this course, but you will learn more about it in Calculus II**.

    You should never use $u = x$, it does nothing to the integral.
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
    1. $\displaystyle \int (2-x)^6 dx$. Take $f(u) = u^6$ and $u = 2-x$, then $u' = -1$ and $\displaystyle \int (2-x)^6 dx = - \int -1 \cdot (2-x)^6dx$ $\displaystyle = - \int u' f(u) dx$ $\displaystyle = - \int f(u) du$ $\displaystyle = - \int u^6 du$ $\displaystyle = - \frac{u^7}{7} + C$ $\displaystyle = - \frac{(2-x)^7}{7} + C$;
    2. $\displaystyle \int \sqrt{x} \cdot \sin(1 + x^{3/2}) dx$. Take $f(u) = \sin(u)$ and $u = 1 + x^{3/2}$, then $\displaystyle u' = \frac{3}{2}x^{1/2} = \frac{3}{2}\sqrt{x}$. Thus $\displaystyle \int \sqrt{x} \cdot \sin(1 + x^{3/2}) dx$ $\displaystyle = \frac{2}{3} \int \frac{3}{2} \sqrt{x} \cdot \sin(1 + x^{3/2}) dx$ $\displaystyle = \frac{2}{3} \int u' f(u) dx$ $\displaystyle = \frac{2}{3} \int f(u) du$ $\displaystyle = \frac{2}{3} \int \sin(u) du$ $\displaystyle = -\frac{2}{3}\cos(u) + C$ $\displaystyle = -\frac{2}{3}\cos(1 + x^{3/2})$;

    Sometimes it is not enough to just take a product of constant. We need to get a bit more creative:

    $\displaystyle \int x \sqrt{x - 4} dx$. A rather natural choice of $u$ is $x-4$ so that $u' = 1$. But what about $f$?

    If we choose $\displaystyle f(u) = \sqrt{u}$, then the original integrand is not $f(u)u' = \sqrt{x-4}$, so it does not work.

    We need to choose $f(u) = (u+4)\sqrt{u}$, then $f(u)u' = (u+4)\sqrt{u} = (x-4+4)\sqrt{x-4} = x\sqrt{x - 4}$.

    Thus the original integral equals $\displaystyle \int f(u) du$ $\displaystyle = \int (u+4)\sqrt{u}du$ $\displaystyle = \int u^{3/2} +4 u^{1/2} du$ $\displaystyle = \frac{2}{5}u^{5/2} + \frac{8}{3}u^{3/2} + C$ $\displaystyle = \frac{2}{5}(x-4)^{5/2} + \frac{8}{3}(x-4)^{3/2} + C$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Remark""")
    return


@app.cell
def _(mo):
    mo.md(r"""Always try to do simplification **at each step** when you take integration.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## A Rather Different Approach""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The last example above suggests that a different approach may be needed - because in general it could be hard to figure out what is $f$.

    WLOG, say the original dummy variable is $x$. The different approach:

    1. Try to determine $u$ using the above approach. If you are not 100% sure what should be your $u$, take a reasonable guess using the above idea;
    2. Your $u$ should depend on $x$, thus we can take derivative with respect to $x$, write it as $\displaystyle \frac{du}{dx} = u'$;
    3. Move $dx$ to the other side, i.e. get $du = u' dx$;
    4. Try to create $u'$ in the original integrand. Whatever left is your $f$. Try to make $f$ a function depends only on $u$ (**in particular, no $x$ anymore**);
    5. If step 4 cannot be done, then you need to reconsider the choice of $u$;
    6. Replace $u'dx$ by $du$, now you get $\displaystyle \int f(u) du$ and U-substitution is done. Proceed from there.
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
    Evaluate $\displaystyle \int 5(z-4)\sqrt[3]{z^2 - 8z}dz$.

    1. First we choose $u$, it is natural to choose $u = z^2 - 8z$ because it is 'inside' a rather complicated function;
    2. Take derivative, $\displaystyle \frac{du}{dz} = 2z - 8$;
    3. Thus $du = (2z -8)dz$;
    4. We want to create $(2z-8)dz$ $= 2(z-4)dz$ in the integral. We of course already have $dz$; we also have $(z-4)$ already, so we need to create a $2$, so we write original integral $\displaystyle = \int \frac{2}{2}\cdot 5 \cdot (z-4) \sqrt[3]{z^2 - 8z} dz$, or $\displaystyle = \int \frac{5}{2}\sqrt[3]{z^2 - 8z} \cdot 2 \cdot (z-4) dz$.
    	So we can replace $2(z-4)dz$ by $du$ and write it as $\displaystyle = \int \frac{5}{2}\sqrt[3]{z^2 - 8z} du$. Then we try to replace $z$ by $u$ using the relation $u = z^2 - 8z$, it is rather straight-forward, we get $\displaystyle = \int \frac{5}{2}\sqrt[3]{u}du$;
    5. Now this becomes much simpler, we just take the integral using basic rules, and get $\displaystyle = \frac{5}{2}\frac{3}{4}u^{4/3} + C$ $\displaystyle = \frac{15}{8}(z^2 - 8z)^{4/3}+C$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## The Substitution Rule (for Definite Integral)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The Substitution Rule for definite integral is similar with the rule above, we just **need to also do something to the upper and lower limits of the integral**.

    Suppose $g(x)$ is differentiable (with range $I$) and $f, g'$ are integrable (on $I$). Write $u = g(x)$ for simplicity, then: $$\boxed{\int\limits_a^b f(u)u'~dx = \int\limits_{g(a)}^{g(b)} f(u)du}.$$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example (Definite Integral)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Evaluate $\displaystyle \int\limits_0^1x^2(1+2x^3)^5dx$.

    Take $u = 1 + 2x^3$, then $\displaystyle \frac{du}{dx} = 6x^2$ so $du = 6x^2 dx$.

    We need to adjust the upper limit to $u(1) = 1 + 2 = 3$ and the lower limit to $u(0) = 1 + 0 = 1$, thus we have the original integral $\displaystyle = \int\limits_{1}^3 \frac{6}{6}x^2(1+2x^3)^5dx$ $\displaystyle = \int\limits_1^3 \frac{1}{6}u^5du$ $\displaystyle = \frac{u^6}{36}|_1^3$ $\displaystyle = \frac{182}{9}$.
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
        r"""Notice above, when we take $\displaystyle \int \frac{1}{6}u^5du$, $u^6$ is **NOT** an antiderivative, it should be $\displaystyle \frac{u^6}{6 \cdot 6}$. Be careful about calculation."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Remark 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""When apply U-substitution to definition integral, remember to change the upper and lower limits of the integral. Also, when we finally plug-in the upper and lower limits to evaluate the integral, **do not substitute back x**: see the above example, we evaluated $\displaystyle = \frac{u^6}{36}|_1^3$ $\displaystyle = \frac{3^6}{36} - \frac{1^6}{36}$, **not** $\displaystyle = \frac{u^6}{36}|_1^3$ $\displaystyle = \frac{(1+2x^3)^6}{36}|_1^3$ $\displaystyle = \frac{(1+2\cdot 3^3)^6}{36} - \frac{(1+2\cdot 1^3)^6}{36}$. This is because $3$ and $1$ are already corresponding to $u$, not $x$. In fact, if you really insist substituting back $u = 1+2x^3$, you need to change the upper and lower limits back to $0$ and $1$."""
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Symmetry""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    We have mentioned this before when we talk about properties of definite integral, here we go a little bit more in detail.

    Given a function, let us call the the part of its graph to the left of $y$-xis the left part, and the part of its graph to the right of $y$-axis the right part. Then:

    1. If we flip left part along $y$-axis and we get the right part (or equivalently, flip right part along $y$-axis and get the left part), we say the function is even. $f(x) = \cos(x)$ is even. $x^n$ where $n$ is an even integer is even. Mathematically, if $f(x) = f(-x)$ for all $x$, then $f$ is even. For example, $x^2 + 1$ is also even;
    2. If we flip left part along $y$-axis and then flip the result along $x$-axis and we get the right part (or equivalently do the process to the right part and get the left part), we say the function is odd. $f(x) = \sin(x)$ is odd. $x^n$ where $n$ is an odd integer is odd. Mathematically, if $f(x) = -f(-x)$ for all $x$, then $f$ is odd;
    3. A function does not need to be either odd or even. $(x+1)^2$ is neither odd nor even.

    We can get symmetry from product of functions:

    1. The product of even function with even function is even;
    2. The product of even function with odd function is odd;
    3. The product of odd function with odd function is even.

    It's a bit different from even number and odd number, because even number times odd number gives even number. When we think of functions, we can think even function is $+$ and odd function is $-$, so $+ \cdot + = +$, $+ \cdot - = -$, and $- \cdot - = +$ which correspond to the above rules.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Definite Integral on Symmetry Functions""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. If $f$ is even, then $\displaystyle \int_{-a}^af(x)dx = 2 \int_0^af(x)dx$;
    2. If $f$ is odd, then $\displaystyle \int_{-a}^af(x)dx = 0$.

    So whenever you see the definite integral with upper limit equals negative of lower limit, try to see if the integrand is **odd**. If it is, the result is immediate.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Example (Symmetry)""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $\displaystyle \int\limits_{-\pi}^{\pi} \frac{x^2\sin(x)}{1+x^4}dx$. Notice the integrand can be viewed as a product with three functions $\displaystyle x^2 \cdot \sin(x) \cdot \frac{1}{1+x^4}$, where $x^2$ is even, $\sin(x)$ is odd, $\displaystyle \frac{1}{1+x^4}$ is even. The integral is well defined because the denominator is never $0$. Since the integrand is an odd function, we have that the result is $0$ immediately;
    2. $\displaystyle \int\limits_{-2}^2 x^6+3x^2+2dx$. The integrand is an even function, thus the integral is the same as $\displaystyle 2\int\limits_0^2 x^6+3x^2+2dx$, which does not really help too much. Nevertheless, the final calculation might be a bit easier now, since we only need to plug-in $0$ to the antiderivative, instead of $-2$.
    """
    )
    return


if __name__ == "__main__":
    app.run()
