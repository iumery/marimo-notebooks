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
    mo.md(r"""# 7.2 Volumes by Slicing""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Introduction""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Let us recall that a cylinder with height $h$ and base radius $r$ has volume $\pi r^2 h$. Why is this the case?

    One way of thinking this is 'stacking cookies'. Suppose you have $h$ cookies, each of them has unit height (i.e. height is $1$), then for each of them, the value of volume is the same as the value of area, which is $\pi r^2$, stack them together, the total volume should be $h \cdot \pi r^2$ which coincides our formula.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""<img src="/public/Pasted image 20241116092602.png" width="250"/>""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Now let us do some modifications to this simple example.

    First, let us assume the cylinder is **laid down**. This does not change any calculation, just change a bit how we view it.

    Second, now imagine that the crackers may **have different radius**. They still **have the same height, but the height may not be $1$**. **They are still stacked** so that the centers are on a straight (horizontal) line.

    So how do we calculate the volume of this new stack of crackers?

    Suppose we have $n$ crackers, and their total height is $b-a$ (image they start to be stacked at $x = a$, and they end up to $x = b$). Since we assumed that all the crackers have the same height, each of them should have height $\displaystyle \frac{b-a}{n}$.

    Each of them can be viewed as a little cylinder with height $\displaystyle \frac{b-a}{n}$ and certain radius (say the first cracker has radius $r_1$, the second with $r_2$, and so on), thus each one of them has volume $\displaystyle \pi r_i^2 \frac{b-a}{n}$.

    If we want to evaluate the total volume, we simply add them together, i.e. $$\text{total volume }=\sum\limits_{i=1}^n \pi r_i^2 \frac{b-a}{n}.$$ Now, if we are using infinitely many crackers to evaluate the volume, we get $$\text{total volume }=\lim\limits_{n \to \infty}\sum\limits_{i=1}^n \pi r_i^2 \frac{b-a}{n}.$$ **The above equation should look familiar to you** - indeed, if we view the radius $r$ as a function depending on the $x$-alue, then the above expression is the same as the definite integral $$\int\limits_a^b\pi r^2(x)dx.$$ We do not *have* to 'lay down' the crackers. In that case, we just think $r$ as a function of $y$ and take integration with respect to $y$.

    The volume we get as discussed above is called the volume of a solid of revolution. The solid is constructed by rotating a curve along a straight line.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""<img src="/public/Pasted image 20230813095136.png" width="400" />""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""The formula for volume of a solid of revolution about $x$-axis is $$\boxed{\text{volume by rotating about }x\text{-axis} = \int\limits_a^b\pi r^2(x)dx}.$$ And the formula for volume of a solid of revolution about $y$-axis is $$\boxed{\text{volume by rotating about }y\text{-axis} = \int\limits_a^b\pi r^2(y)dy}.$$"""
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Rotating Axis
        type: danger

    Inspect the above formulas more carefully, observing that with this method, **if we are rotating about $x$-axis, then the radius has to be a function that depends on $x$**. Similarly, if we are rotating about $y$-axis, then the radius **has to** be a function that depends on $y$.

    ///
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Volume of Cylinder""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    A cylinder can be get by rotating a horizontal line segment along $x$-axis.

    In particular, the radius function is $r$ (a constant). Take the rotation, by above formula, we get that the volume of solid of revolution equals $\displaystyle \int\limits_0^h \pi r^2 dx$ (notice $r$ here is a constant!) which simply equals $\displaystyle \pi r^2 x |_0^h = \pi r^2 h$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Volume of Cone""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    A cone can be get by rotating a line segment along $x$-axis. What is this line segment? It passes the point $(0,r)$ (because the base radius is $r$), it also passes the point $(h, 0)$ (because at height $h$ the cone comes to the tip), thus the line segment has expression $\displaystyle y = -\frac{r}{h}x + r$. This is the function for the radius when we calculate the volume.

    Thus by above formula, we get the volume of solid of revolution equals $\displaystyle \int\limits_0^h \pi (\frac{r}{h}x+r)^2 dx$. Do the calculation, the result is indeed $\displaystyle \frac{1}{3}\pi r^2 h$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Volume of Ball""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    A ball can be get by rotating a half-circle along $x$-axis. But for purpose of example, let us think of it as rotating a half-circle along $y$-axis.

    The function of the half-circle is $x = \sqrt{r^2 - y^2}$, thus by above formula, we get the volume of solid of revolution equals $\displaystyle \int\limits_{-r}^r \pi (r^2 - y^2) dy$ which indeed equals $\displaystyle \frac{4}{3}\pi r^3$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Typical Problem on Exam""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    A typical problem on this section may use knowledge also on 7.1. Here is an example:

    Find the volume of the solid of revolution obtained by rotating the **region** enclosed by the curves $y = \sqrt{x}$ and $\displaystyle y = \frac{x}{2}$ about the $x$-axis.

    Let us start by finding the region enclosed by the two curves (this is from 7.1). Set $\displaystyle \sqrt{x} = \frac{x}{2}$, solve for it, we get $x = 0$ or $x = 4$. On $[0, 4]$, $\sqrt{x}$ is above $\displaystyle \frac{x}{2}$ (why? plug in a value in $(0,4)$ and check!).

    Now, we want to rotate this **region**. Try to image it, and you should get that the result of rotating the region about $x$-axis is the same as the result of rotating $\sqrt{x}$ about $x$-axis on $[0,4]$ **minus** the result of rotating $\frac{x}{2}$ about $x$-axis on $[0,4]$. You can start by imagining stack of cookies - but now each cookie is not disk-shaped, but annulus-shaped.

    Thus, we should calculate $\displaystyle \int\limits_0^4 \pi (\sqrt{x})^2 dx$ $\displaystyle - \int\limits_0^4 \pi (\frac{x}{2})^2 dx$, (which equals $\displaystyle \int\limits_0^4 \pi (\sqrt{x})^2 - (\frac{x}{2})^2) dx$) and the result is $\displaystyle \frac{8}{3}\pi$.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Formula""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    In general, the volume of solid of revolution of a region bounded between $f$ and $g$, assuming $f$ is on top, and the rotating axis being the $x$-axis, is: $$\boxed{\int\limits_a^b \pi (f^2 - g^2) dx}.$$

    A very **common mistake** is to have $\displaystyle \int\limits_a^b \pi (f - g)^2 dx$: no, you need to take square then subtraction, not the other way around (the correct formula is easier in calculation, as a matter of fact).
    """
    )
    return


if __name__ == "__main__":
    app.run()
