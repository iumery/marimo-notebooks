import marimo

__generated_with = "0.14.16"
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
    /// admonition | Square-root vs. Square
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


@app.cell
def _(mo):
    mo.md(
        r"""
    1. $| ab | = | a | | b |$;
    2. $| a + b | \le | a | + | b |$.
    """
    )
    return


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


if __name__ == "__main__":
    app.run()
