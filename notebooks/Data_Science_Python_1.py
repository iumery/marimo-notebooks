import marimo

__generated_with = "0.14.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    from numpy.typing import NDArray
    import matplotlib.pyplot as plt

    return NDArray, mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    nav_menu = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
        },
        orientation="vertical",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Warm-up""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Goal

    The goal of this practice is to strengthen Python programming skills in scientific computing by working with arrays, matrices, expressions, control flow, and plotting, and to apply these concepts to visualize fractals such as Julia and Mandelbrot sets.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Section 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (a)

    Scalar variables, make the following variables.

    - $a = 10$
    - $b = 2.5\times 10^{23}$
    - $c = 2 + 3i$ where $i^2 = -1$
    - $d = e^{i2\pi/3}$
    """
    )
    return


@app.cell
def _(np):
    a: int = 10
    b: float = 2.5e23
    # 1j means i and 0.3j mean 0.3i, etc.
    # No space between the number and j
    c: complex = 2 + 3j
    d: complex = np.exp(2j * np.pi / 3)
    return a, c, d


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (b)

    Vector variables, make the following variables, as numpy arrays.

    - $\mathbf{u} = \begin{pmatrix} 3.14 & 15 & 9 & 26 \end{pmatrix}$
    - $\mathbf{v} = \begin{pmatrix} 2.71 \\ 8 \\ 28 \\ 182 \end{pmatrix}$
    - $\mathbf{w} = \begin{pmatrix} 5 & 4.8 & 4.6 & \dots & -4.8 & -5 \end{pmatrix}$
    - $\mathbf{m} = \begin{pmatrix} 10^0 & 10^{0.01} & \dots & 10^{0.99} & 10^1 \end{pmatrix}$
    """
    )
    return


@app.cell
def _(NDArray, np):
    # np.reshape: one of the argument can be left as -1 to indicate "use whatever shape needed at this dimension"
    u: NDArray = np.array([3.14, 15, 9, 26]).reshape(1, -1)
    v: NDArray = np.array([2.71, 8, 28, 182]).reshape(-1, 1)
    w: NDArray = np.linspace(5, -5, 51)
    m: NDArray = np.logspace(0, 1, 101, base=10)
    return m, u, v


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (c)

    Matrix variables, make the following variables.

    - $A$, a $9 \times 9$ matrix full of $2$s
    - $B$, a $9 \times 9$ matrix of zeros with $\begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 4 & 3 & 2 & 1 \end{pmatrix}$ on the diagonal
    - $C$, a $10 \times 10$ matrix with numbers $1, \dots, 100$ down the column
    - $D = \begin{pmatrix} 13 & -1 & 5 \\ -22 & 10 & 87\end{pmatrix}$
    - $E$, a $5 \times 3$ matrix of random integers with values on the range $-3$ to $3$
    """
    )
    return


@app.cell
def _(NDArray, np):
    A: NDArray[int] = np.full(shape=[9, 9], fill_value=2)
    B: NDArray[int] = np.diag([1, 2, 3, 4, 5, 4, 3, 2, 1])
    C: NDArray[int] = np.linspace(1, 100, 100).astype(int).reshape(10, 10).T
    D: NDArray[int] = np.array([[13, -1, 5], [-22, 10, 87]])
    # The result is not uniformly distributed because of the sampling and rounding process here
    E: NDArray[int] = (
        (-3 + 6 * np.random.random_sample(5 * 3)).round().astype(int).reshape(5, 3)
    )
    return A, B, C, D


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (d)

    Scalar expressions, using the variables created in (a), calculate $x$ and $y$.

    - $\displaystyle x = \frac{1}{1 + e^{-(a-15)/6}}$
    - $\displaystyle y = \frac{\log(\mathcal{R}[(c+d)(c-d)] \cdot \sin(a \pi / 3))}{c\overline{c}}$ where $\mathcal{R}$ indicates the real part of a complex number and $\log$ is the natural logarithm
    """
    )
    return


@app.cell
def _(a: int, c: complex, d: complex, np):
    x: np.float64 = 1 / (1 + np.exp(-(a - 15) / 6))
    # When we are certain that the operation will yield a real number, we can take the real part by .real and annotate the type as float
    y: np.float64 = (
        np.log(np.real((c + d) * (c - d)) * np.sin(a * np.pi / 3)) / (c * np.conj(c))
    ).real
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (e)

    Vector expression, using the variables created in (b), evaluate the expressions below elementwise.

    - $\displaystyle \mathbf{x} = \frac{1}{\sqrt{2 \pi (2.5)^2}}e^{-\mathbf{v}^2 / (2 \cdot (2.5)^2)}$
    - $\displaystyle \mathbf{y} = \sqrt{(\mathbf{u}^T)^2 + \mathbf{v}^2}$
    - $\displaystyle \mathbf{z} = \log_{10}(\frac{1}{\mathbf{m}})$, does the output make sense?
    """
    )
    return


@app.cell
def _(NDArray, m: "NDArray", np, u: "NDArray", v: "NDArray"):
    x_vec: NDArray[np.float64] = (1 / np.sqrt(2 * np.pi * (2.5**2))) * np.exp(
        -(v**2) / (2 * (2.5**2))
    )
    y_vec: NDArray[np.float64] = np.sqrt((u.T) ** 2 + v**2)
    z_vec: NDArray[np.float64] = np.log10(1 / m)
    return (z_vec,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""`z_vec` should be an array from 0 to -1 because $\log_{10}(1/10^x) = \log_{10}(10^{-x}) = -x$."""
    )
    return


@app.cell
def _(z_vec: "NDArray[np.float64]"):
    z_vec
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (f)

    Matrix expressions, using the variables created in (b) and (c), evaluate the expressions below.

    - $X = (\mathbf{u} \cdot \mathbf{v}) A^2$
    - $Y = \mathbf{v} \cdot \mathbf{u}$
    - $Z = \det(C) (AB)^T$ 
    """
    )
    return


@app.cell
def _(
    A: "NDArray[int]",
    B: "NDArray[int]",
    C: "NDArray[int]",
    NDArray,
    np,
    u: "NDArray",
    v: "NDArray",
):
    X: NDArray[np.float64] = (np.dot(u, v)) * np.linalg.matrix_power(A, 2)
    Y: NDArray[np.float64] = np.dot(v, u)
    # We can also use A @ B for matrix multiplication
    Z: NDArray[np.float64] = np.linalg.det(C) * np.matmul(A, B).T
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (g)

    Common functions and indexing.

    - Compute the column-wise sum of $C$
    - Compute the mean across the rows of $D$
    - Display only the second column of $D$
    - Display only the first row of $D$
    - Replace the top row of $D$ with $[1, 1, 1]$
    - Extract the submatrix of $C$ that only contains rows $2$ through $9$ and columns $2$ through $9$
    - Make the vector $\mathbf{k} = \begin{pmatrix} 1 & 2 & 3 & \dots & 20 \end{pmatrix}$ and then make every other value in it negative to get $\mathbf{k} = \begin{pmatrix} 1 & -2 & 3 & \dots & 19 & -20 \end{pmatrix}$
    - Make $\mathbf{r}$ a $1 \times 5$ vector using `np.random.random_sample`. Find the elements that have values strictly less than $0.5$ and set those values to $0$
    """
    )
    return


@app.cell
def _(C: "NDArray[int]", D: "NDArray[int]", NDArray, np):
    # `keepdims=True` to make column wise operation leaving a row (also by default) and row wise operation leaving a column (by default it leaves a row also)
    column_wise_sum_C: NDArray[int] = np.sum(C, axis=0, keepdims=True)
    row_wise_mean_D: NDArray[np.float64] = np.mean(D, axis=1, keepdims=True)
    second_column_D: NDArray[int] = D[:, 1]
    first_row_D: NDArray[int] = D[0, :]
    D[0] = [1, 1, 1]
    submatrix_C: NDArray[int] = C[2:10, 2:10]
    k_vec: NDArray[int] = np.linspace(1, 20, 20).astype(int) * (-1) ** (
        np.arange(0, 20)
    )
    r_vec: NDArray[np.float64] = np.random.random_sample((1, 5))
    r_vec[r_vec < 0.5] = 0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Section 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (a)

    First, we'll deal with a geometric series $\displaystyle S = \sum_{k = 0}^{\infty} r^k$. We need to define the value of $r$ and the values of $k$. Say $r = 0.99$ and $k$ is an array containing the integers from $0$ to $1000$, inclusive.

    - Calculate each term in the series $a_k = r^k$
    - Calculate the partial sums $\displaystyle S_k = \sum_{i = 0}^k a_i$
    - Calculate the value of the infinite series using the fact that $\displaystyle S = \frac{1}{1 - r}$
    - Plot:
        - Plot the value of the inifite series
        - On the same plot, plot the value of the finite series
        - Label the axes, give the figure a title, and create a legend
    """
    )
    return


@app.cell
def _(NDArray, np):
    r: float = 0.99
    num_sum_geom: int = 1000
    k: NDArray[int] = np.linspace(0, num_sum_geom, num_sum_geom + 1).astype(int)
    a_k_geom: NDArray[np.float64] = r**k
    S_k_geom: NDArray[np.float64] = np.cumsum(a_k_geom)
    S_geom: float = 1 / (1 - r)
    return S_geom, S_k_geom, r


@app.cell
def _(S_geom: float, S_k_geom: "NDArray[np.float64]", plt, r: float):
    plt.figure(figsize=(5, 3))
    # `label` is required for legend plotting
    plt.plot(S_k_geom, label="Infinite sum")
    plt.axhline(S_geom, color="orange", label="Finite sum")
    plt.title(f"Convergence of geometric series with r={r}")
    plt.xlabel("index")
    plt.ylabel("sum")
    plt.legend()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (b)

    Do a similar thing for the $p$-series $\displaystyle S = \sum_{n = 1}^{\infty} \frac{1}{n^2}$. Use $n$ as a vector containing all the integers from $1$ to $500$, inclusive. Also, note $\displaystyle S = \frac{\pi^2}{6}$.
    """
    )
    return


@app.cell
def _(NDArray, np):
    num_sum_p: int = 500
    n: NDArray[int] = np.linspace(1, num_sum_p, num_sum_p).astype(int)
    a_k_p: NDArray[np.float64] = 1 / n**2
    S_k_p: NDArray[np.float64] = np.cumsum(a_k_p)
    S_p: float = np.pi**2 / 6
    return S_k_p, S_p


@app.cell
def _(S_k_p: "NDArray[np.float64]", S_p: float, plt):
    plt.figure(figsize=(5, 3))
    plt.plot(S_k_p, label="Infinite sum")
    plt.axhline(S_p, color="orange", label="Finite sum")
    plt.title(f"Convergence of p-series with p=2")
    plt.xlabel("index")
    plt.ylabel("sum")
    plt.legend()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (c)

    Visualize the error in the partial sums. Plot $|S_n - S|$ for both the series. Use a logarithmic scale for the vertical axis, and add a grid for ease of reading.
    """
    )
    return


@app.cell
def _(
    S_geom: float,
    S_k_geom: "NDArray[np.float64]",
    S_k_p: "NDArray[np.float64]",
    S_p: float,
    np,
    plt,
    r: float,
):
    plt.figure(figsize=(10, 3))

    plt.subplot(1, 2, 1)
    plt.plot(np.abs(S_k_geom - S_geom), label="Error")
    # Use plt.semilogy() for logarithmic scale y axis
    plt.semilogy()
    plt.grid()
    plt.xlabel("index")
    plt.ylabel("finite series truncation error")
    plt.title(f"Convergence of geometric series with r={r}")

    plt.subplot(1, 2, 2)
    plt.plot(np.abs(S_k_p - S_p), label="Error")
    plt.semilogy()
    plt.grid()
    plt.xlabel("index")
    plt.ylabel("finite series truncation error")
    plt.title(f"Convergence of p-series with p=2")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Section 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""Loops and flow control: Make function called `loopTest(M, N)` that loops through the values $M$ through $N$. For each number $n$ it should display `n is divisible by 3` or `n is NOT divisible by 3` and it should stop after finding three occurrences of a number divisible by three."""
    )
    return


@app.function
def loopTest(M: int, N: int) -> None:
    count = 0
    for number in range(M, N + 1):
        if number % 3 == 0:
            print(f"{number} is divisible by 3")
            count += 1
            if count >= 3:
                break
        else:
            print(f"{number} is NOT divisible by 3")


@app.cell
def _():
    loopTest(10, 13)
    print("---")
    loopTest(13, 0)
    print("---")
    loopTest(1, 200)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 4

    The following description is adapted from Wikipedia at [Julia set](http://en.wikipedia.org/wiki/Julia_set).

    Given two complex numbers $c$ and $z_0$, we define the following recursion $$z_n = z_{n-1}^2 + c,\,\,\,\,\,\, n = 1, 2,3, \dots$$ This is a dynamical system known as a quadratic map. Given a specific choice of $c$ and $z_0$, the above recursion leads to a sequence of complex numbers $z_1, z_2, z_3, \dots$ called the orbit of $z_0$. Depending on the exact choice of $c$ and $z_0$, a large range of orbit patterns are possible. For a given fixed $c$, most choices of $z_0$ yield orbits that tend towards infinity. For some values of $c$ certain choices of $z_0$ yield orbits that eventually go into a periodic loop. Finally, some starting values yield orbits that appear to dance around the complex plane, apparently at random. (This is an example of chaos.) These starting values, $z_0$ , make up the Julia set of the map, denoted $J_c$ . In this problem, you will write python code that visualizes a slightly different set, called the filled-in Julia set (or Prisoner Set), denoted $K_c$ , which is the set of all $z_0$ with orbits which do not tend towards infinity. The "normal" Julia set $J_c$ is the boundary of the filled-in Julia set.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (a)

    It has been shown that if the modulus of $z_n$ becomes larger than $2$ for some $n$ then it is guaranteed that the orbit will tend to infinity. The value of $n$ for which this becomes true is called the 'escape velocity' of a particular $z_0$. Write a function that returns the escape velocity of a given $z_0$ and $c$. The function declaration should be `n = escapeVelocity(z0, c, N)` where `N` is the maximum allowed escape velocity (basically, if the modulus of $z_n$ does not exceed $2$ for $n < N$, return `N` as the escape velocity. This will prevent infinite loops).

    To check your escape velocity function, run `escapeVelocity(0.3+0.4j, -0.3+0.6j, 100)`. The result should be `6`.
    """
    )
    return


@app.cell
def _(np):
    def escapeVelocity(z0: complex, c: complex, N: int) -> int:
        z_current = z0
        # Start with 1 in the for loop since z_0 is given already
        for n in range(1, N):
            z_next: complex = z_current**2 + c
            z_current: complex = z_next
            if np.abs(z_current) > 2:
                return n
        return N

    return (escapeVelocity,)


@app.cell
def _(escapeVelocity):
    escapeVelocity(0.3 + 0.4j, -0.3 + 0.6j, 100)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (b)

    To generate the filled in Julia set, write the following function `M = julia(zMax, c, N)`. `zMax` will be the maximum of the imaginary and complex parts of the various $z_0$s for which we will compute escape velocities. `c` and `N` are the same as defined above, and `M` is the matrix that contains the escape velocity of various $z_0$s.

    - In this function, you first want to make a $500×500$ array that contains complex numbers with real part between `-zMax` and `zMax`, and imaginary part between `-zMax` and `zMax`. Call this array `Z`. Make the imaginary part vary along the $y$-axis of this array. You can most easily do this by using np.linspace and np.meshgrid, but you can also do it with a loop.
    - For each element of `Z`, compute the escape velocity (by calling `escapeVelocity`) and store it in the same location in a matrix `M`. When done, the matrix `M` should be the same size as `Z` and contain escape velocities with values between $1$ and $N$.
    - Run your julia function with various `zMax`, `c`, and `N` values to generate various fractals. To display the fractal use `plt.imshow`; you may also want to use `origin='lower'` so the origin is in the lower-left corner instead of the upper-left corner).
    """
    )
    return


@app.cell
def _(NDArray, escapeVelocity, np):
    def julia(zMax: float, c: complex, N: int) -> NDArray[int]:
        zMax = np.abs(zMax)
        n: int = 500
        rows: NDArray[np.float64]
        cols: NDArray[np.float64]
        # `np.meshgrid` will return a tuple of two ndarray's with the row and column values
        rows, cols = np.meshgrid(
            np.linspace(-zMax, zMax, n), np.linspace(-zMax, zMax, n), indexing="ij"
        )
        # Direct operation on the rows and columns is possible
        Z: NDArray[complex] = cols + rows * 1j
        # `np.vectorize` provides a clean way to apply a function to an ndarray
        # The `excluded` argument tells which arguments are held constant but it is not essential
        escape: np.vectorize = np.vectorize(
            escapeVelocity,
            excluded=["c", "N"],
        )
        M: NDArray[int] = escape(z0=Z, c=c, N=N)
        return M

    return (julia,)


@app.cell
def _(NDArray, julia, np, plt):
    def plot_julia(zMax: float, c: complex, N: int) -> None:
        M: NDArray[int] = julia(zMax, c, N)
        zMax = np.abs(zMax)
        plt.figure(figsize=(4, 4))
        # `extent` gives the heatmap a customized *display* range
        plt.imshow(
            M,
            cmap="viridis",
            origin="lower",
            extent=(-zMax, zMax, -zMax, zMax),
        )
        plt.colorbar()
        plt.title(f"Escape Velocity Map with\nz={zMax},\n c={c},\nand N={N}")
        plt.show()

    return (plot_julia,)


@app.cell
def _(plot_julia):
    plot_julia(1, -0.297491 + 1j * 0.641051, 100)
    plot_julia(0.35, -0.297491 + 1j * 0.641051, 250)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (c)

    Now make another function `benoit(zMax, N)`, identical to julia except that the recursion should be $$z_n = z_{n−1}^2 + z_0,\,\,\,\,\,\, n = 2, 3, 4,\dots,\,\,\,\,\,\, z_1 = 0$$

    Notice that the point in the complex plane, $z_0$, is now playing the role of the constant $c$ from the Julia set, and that the recursion always starts at the origin. You could write a new function similar to `escapeVelocity` but since the functional form of this recursion (quadratic map) is the same, you can re-use `escapeVelocity` but with $z_0$  going in place of $c$ and setting the $z_0$ to zero.

    Show the result of `benoit(2, 100)` with imshow as above. You will recognize the image!
    """
    )
    return


@app.cell
def _(NDArray, escapeVelocity, np):
    def benoit(zMax: float, N: int) -> NDArray[int]:
        zMax = np.abs(zMax)
        n: int = 500
        rows: NDArray[np.float64]
        cols: NDArray[np.float64]
        rows, cols = np.meshgrid(
            np.linspace(-zMax, zMax, n),
            np.linspace(-zMax, zMax, n),
            indexing="ij",
        )
        Z: NDArray[complex] = cols + rows * 1j
        escape: np.vectorize = np.vectorize(
            escapeVelocity,
            excluded=["z0", "N"],
        )
        M: NDArray[int] = escape(z0=0, c=Z, N=N)
        return M

    return (benoit,)


@app.cell
def _(NDArray, benoit, np, plt):
    def plot_benoit(zMax: float, N: int) -> None:
        M: NDArray[int] = benoit(zMax, N)
        zMax = np.abs(zMax)
        plt.figure(figsize=(4, 4))
        plt.imshow(
            M,
            cmap="viridis",
            origin="lower",
            extent=(-zMax, zMax, -zMax, zMax),
        )
        plt.colorbar()
        plt.title(f"Escape Velocity Map with\nz={zMax} and N={N}")
        plt.show()

    return (plot_benoit,)


@app.cell
def _(plot_benoit):
    plot_benoit(2, 250)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""It's the Mandelbrot set!""")
    return


if __name__ == "__main__":
    app.run()
