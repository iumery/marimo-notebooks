import marimo

__generated_with = "0.13.15"
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
    mo.md(r"""# 2.7 Application of Chain Rule Related Rates""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Motivation""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Suppose we have some ice cream in a cone. The cone has top radius $4$ cm and height $12$ cm. Unfortunately the ice cream has melted, and even more unfortunately - they are dripping out of the cone from a hole at the bottom, at a constant rate of $2 \text{cm}^3/\text{min}$. What is the rate of change of level of the ice cream remaining in the cone when the level is $3$ cm?

    (Recall that the formula of calculating volume of a cone is $\displaystyle V = \frac{1}{3}\pi r^2 h$)

    Let us consider this question in a more general or abstract setting. Basically we have three (or more) quantities (we have $4$ in the above question: height, radius, volume - and time) $A, B, C, …$. We know the rate of change of, say, $B$ with respect to $A$, we know the relation between $B$ and $C$, and we want to know the rate of change of $C$ with respect to $A$.

    **At its core, we want to compute the rate of change of some quantity in terms of the rate of change of another quantity. So basically, it is the Chain Rule**. This kind of problem is called 'related rates problem'.

    In real world problems, this is probably more useful than you think. Some quantities or rates of change are easier to be measured. In the above example, we can assume the hole at the bottom of the cone is not expanding so the rate of ice cream dripping is **fixed**; however, if the rate of dripping is fixed, then the rate of change of level is **not fixed** - because the higher level is, the more ice cream there is, the slower the level decrease. With the technique we learn in this section, we can use a quantity that is easy to measure to calculate another quantity that is hard to measure.

    The procedure of solving the above question is to take derivatives of everything with respect to time - we know the derivative of volume with respect to time, and we can find the derivative of level with respect to time using Chain Rule.

    In a general setting, we take derivative of everything with respect to the certain quantity $A$ we are interested in - usually we know the derivative of one other quantity $B$ with respect to that quantity $A$ and want to calculate the derivative of another quantity $C$ with respect to $A$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Solve the Problem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    We know the volume of a cone with respect to (top) radius and height is $\displaystyle V = \frac{1}{3}\pi r^2 h$. From the problem description we can view $V, r, h$ all being functions of $t$, $V$ can also be viewed as function of $r$ and $h$, and we know that $\displaystyle \frac{dV}{dt} = -2$. We want to calculate $\displaystyle \frac{dh}{dt}$ when $h = 3$.

    First we need to take care of the 'extra' variable problem. Notice that the ratio between the height and radius of remaining ice cream is always fixed - which is the same as the ratio between the height and radius of the cone itself. That is, we always have $\displaystyle \frac{h}{r} = \frac{12}{4}$ $\implies h = 3r$, or $\displaystyle r = \frac{1}{3}h$. Thus we can safely write $\displaystyle V = \frac{1}{3}\pi (\frac{1}{3}h)^2 \cdot h$ $\displaystyle = \frac{1}{27}\pi h^3$. Now we only have three interesting quantities, volume, height, and time.

    So consider $\displaystyle V = \frac{1}{27}\pi h^3$. Now:

    1. View $V$ as a function of $t$, then we get that LHS is simply $\displaystyle \frac{dV}{dt}$, which we are given it is $-2$;
    2. View $V$ as a function of $h$, and view $h$ as a function of $t$, then we can also calculate $\displaystyle \frac{dV}{dt}$ $\displaystyle = \frac{dV}{dh}\frac{dh}{dt}$ because of the Chain Rule. We can calculate $\displaystyle \frac{dV}{dh}$ using the usual differentiation rule (power rule & constant rule) and get $\displaystyle \frac{dV}{dh} = \frac{1}{9}\pi h^2$;
    3. Put things together, we get an equation $\displaystyle -2 = \frac{dV}{dt}$ $\displaystyle = \frac{dV}{dh}\frac{dh}{dt}$ $\displaystyle = \frac{1}{9}\pi h^2 \frac{dh}{dt}$, and now it is straight-forward to see $\displaystyle \frac{dh}{dt} = -\frac{18}{\pi h^2}$;
    4. Plug in $h = 3$, then $\displaystyle \frac{dh(3)}{dt} = -\frac{2}{\pi}$ which is about $-0.6 \text{cm}/\text{min}$ (during the exam, just leave it as $\displaystyle -\frac{2}{\pi}$).

    To put it simple, in a related rate problem, **every** variable is treated as a dependent variable as we studied in implicit differentiation (technically, we should treat the time variable as the independent variable, but it should not appear in the equation anyway).
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Strategy of Solve Related Rates Problem""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. Read the problem carefully, possibly use a diagram to help;
    2. Write down the quantity that the question is asking about (height in above question);
    3. Write down an equation that involves this quantity and other quantities we have information about ($\displaystyle V = \frac{1}{3}\pi r^2 h$ above);
    4. Substitute variables if needed ($\displaystyle V = \frac{1}{27}\pi h^3$)
    5. Take derivative, recall that each variable is treated as a dependent variable ($\displaystyle V' = \frac{1}{9}\pi h^2 h'$)
    6. Plug-in known information and get result.
    """
    )
    return


if __name__ == "__main__":
    app.run()
