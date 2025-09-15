import marimo

__generated_with = "0.15.4"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np

    return mo, np


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
    mo.md(
        r"""
    /// attention | Attention!

    Code in this notebook involving AMPL **WOULD NOT** run directly as Marimo does not include AMPL package (it needs registration anyway). Check AMPL [official website](https://ampl.com) for more info.

    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Optimization, Part 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Goal""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""This set develops modeling and solution skills for optimization problems. Topics include feasibility recovery in LPs, formulation strength in integer programming, branch-and-bound for knapsack, heuristic methods (greedy, local, tabu, annealing), and inventory control under uncertainty."""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Problem 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Assume we are given an LP in standard form

    $$\begin{aligned} \max_{x}(c^Tx) &\text{ s.t.} \\ Ax &\le b \\ x &\ge 0 \end{aligned}$$

    where $b$ may contain some negative components, in which case it is not clear if there is even a feasible solution. Formulate a new LP such that:

    - The new LP always has a feasible solution which has a simple, closed form
    - The new LP takes an objective value of 0 if the original LP is feasible
    - The new LP takes an objective value of greater than 0 if the orginal LP is infeasible
    - Given a solution to the new LP with objective value of 0, one can construct a feasible solution to the original LP
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Form a new LP by introducing variables $y_i \ge 0$ (one for each constraint). Consider the LP:

    $$\begin{aligned} \min_{x, y}\sum y &\text{ s.t.} \\ Ax - y &\le b \\ x &\ge 0 \\ y &\ge 0\end{aligned}$$

    - It is always feasible: let $x = 0$ and $y_i = -\min(0, b_i)$
    - If the original LP is feasible, then $y = 0$ is a feasible solution and is clearly minimizing $1^Ty$
    - If the original LP is infeasible, then some $(Ax)_i$ exceeds $b_i$, forcing $y_i$ to be greater than 0, making the new LP takes an objective value greater than 0
    - We can get a feasible solution by simply extracting the $x$ part of optimal solution of the new LP. Notice this does not necessarily give an optimal solution of the original LP
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Problem 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Formulation A has the following constraints:

    $$\begin{aligned}\sum_{j=1}^nx_{ij} &=1,\forall i \\ x_{ij} &\le y_j, \forall i, j \\ x, y &\ge 0 \\ x_{ij}, y_j & \in \mathbb{Z}, \forall i, j\end{aligned}$$

    Formulation B has the following constraints:

    $$\begin{aligned}\sum_{j=1}^nx_{ij} &=1,\forall i \\ \sum_{i=1}^mx_{ij} &\le my_j, \forall j \\ x, y &\ge 0 \\ x_{ij}, y_j & \in \mathbb{Z}, \forall i, j\end{aligned}$$

    Which formulation is stronger?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""Formulation A is stronger. The second constraint in Formulation B just gives a total cap of $x_{ij}$ in a row, but the second constraint in Formulation A gives a cap to them individually."""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Problem 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Solve the following problem by branch-and-bound.

    $$\begin{aligned} \max_{x}17x_1 + 10x_2 + 25x_3 + 17x_4 &\text{ s.t.} \\ 5x_1 + 3x_2 + 8x_3 + 7x_4 &\le 12 \\ x_i &\in \lbrace 0, 1 \rbrace \end{aligned}$$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    First solve the LP:

    $$\begin{aligned} \max_{x}17x_1 + 10x_2 + 25x_3 + 17x_4 &\text{ s.t.} \\ 5x_1 + 3x_2 + 8x_3 + 7x_4 &\le 12 \\ x_i &\in [0, 1] \end{aligned}$$

    Do a quick value per weight, we see $w_1 = 17/5 > w_2 = 10/3 > w_3 = 25/8 > w_4 = 17/7$ so the optimal solution is $x_1 = 1, x_2 = 1$ and leaves $x_3 = 0.5$. Now we do branch-and-cut.

    First, $x_3 = 0$, we get the LP:

    $$\begin{aligned} \max_{x}17x_1 + 10x_2 + 17x_4 &\text{ s.t.} \\ 5x_1 + 3x_2 + 7x_4 &\le 12 \\ x_i &\in \lbrace 0, 1 \rbrace \end{aligned}$$

    Apparently the optimal solution here is $x_1 = 1, x_4 = 1 \implies$ object $= 17+17 = 34$.

    Next, $x_3 = 1$, we get the LP:

    $$\begin{aligned} \max_{x}17x_1 + 10x_2 + 25 + 17x_4 &\text{ s.t.} \\ 5x_1 + 3x_2 + 7x_4 &\le 4 \\ x_i &\in \lbrace 0, 1 \rbrace \end{aligned}$$

    Apparently the optimal solution here is $x_2 = 1 \implies$ object $= 10+25 = 35$. Combine things together, optimal solution for the original program is $x_2 = 1, x_3 = 1$ gives $17x_1 + 10x_2 + 25x_3 + 17x_4 = 35$.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Problem 4""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Consider a general binary knapsack problem

    $$\begin{aligned} \max_{x}\sum_{i=1}^nc_ix_i &\text{ s.t.} \\ \sum_{i=1}^n a_ix_i &\le B \\ x_i &\in \lbrace 0, 1 \rbrace \end{aligned}$$

    1. Describe a greedy heuristic for constructing a solution to this problem.
    2. Implement local search heuristic for this problem.
    3. Extend your local search heuristic to a tabu search heuristic.
    4. Extend your local search heuristic to a simulated annealing heuristic.
    5. Run each of your heuristics on some randomly generated problem instances. Solve these instances with Gurobi. How close to the optimal solution do your heuristics achieve?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""1. See above""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""2. Python implement:""")
    return


@app.cell
def _(np):
    def knapsack_local_search(c, a, B, max_iter=1000):
        n = len(c)
        c = np.array(c)
        a = np.array(a)

        ratio = c / a
        order = np.argsort(-ratio)
        x = np.zeros(n, dtype=int)
        total_weight = 0

        for i in order:
            if total_weight + a[i] <= B:
                x[i] = 1
                total_weight += a[i]

        best_x = x.copy()
        best_value = np.dot(c, x)

        for _ in range(max_iter):
            improved = False
            for i in range(n):
                x_new = best_x.copy()
                x_new[i] = 1 - x_new[i]

                new_weight = np.dot(a, x_new)
                if new_weight > B:
                    continue

                new_value = np.dot(c, x_new)
                if new_value > best_value:
                    best_x = x_new
                    best_value = new_value
                    improved = True
                    break

            if not improved:
                break

        return best_x, best_value

    return (knapsack_local_search,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""3. Python implement:""")
    return


@app.cell
def _(np):
    def knapsack_tabu_search(c, a, B, max_iter=500, tabu_tenure=5):
        n = len(c)
        c = np.array(c)
        a = np.array(a)

        ratio = c / a
        order = np.argsort(-ratio)
        x = np.zeros(n, dtype=int)
        total_weight = 0

        for i in order:
            if total_weight + a[i] <= B:
                x[i] = 1
                total_weight += a[i]

        best_x = x.copy()
        best_value = np.dot(c, x)

        tabu_list = {}

        for iteration in range(max_iter):
            best_neighbor = None
            best_neighbor_value = -np.inf
            move_to_make = None

            for i in range(n):
                x_candidate = x.copy()
                x_candidate[i] = 1 - x_candidate[i]
                weight_candidate = np.dot(a, x_candidate)
                if weight_candidate > B:
                    continue

                value_candidate = np.dot(c, x_candidate)

                is_tabu = i in tabu_list and tabu_list[i] > iteration
                aspiration = value_candidate > best_value

                if not is_tabu or aspiration:
                    if value_candidate > best_neighbor_value:
                        best_neighbor = x_candidate
                        best_neighbor_value = value_candidate
                        move_to_make = i

            if best_neighbor is None:
                break

            x = best_neighbor

            if best_neighbor_value > best_value:
                best_value = best_neighbor_value
                best_x = best_neighbor

            tabu_list[move_to_make] = iteration + tabu_tenure

        return best_x, best_value

    return (knapsack_tabu_search,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""4. Python implement:""")
    return


@app.cell
def _(np):
    def knapsack_simulated_annealing(c, a, B, T_init=100.0, T_min=1e-3, alpha=0.95, max_iter=1000):
        n = len(c)
        c = np.array(c)
        a = np.array(a)

        ratio = c / a
        order = np.argsort(-ratio)
        x = np.zeros(n, dtype=int)
        total_weight = 0

        for i in order:
            if total_weight + a[i] <= B:
                x[i] = 1
                total_weight += a[i]

        best_x = x.copy()
        best_value = np.dot(c, x)

        T = T_init

        for step in range(max_iter):
            i = np.random.randint(0, n)
            x_new = x.copy()
            x_new[i] = 1 - x_new[i]

            weight_new = np.dot(a, x_new)
            if weight_new > B:
                continue

            value_old = np.dot(c, x)
            value_new = np.dot(c, x_new)
            delta = value_new - value_old

            if delta > 0 or np.random.rand() < np.exp(delta / T):
                x = x_new

            if value_new > best_value:
                best_x = x_new
                best_value = value_new

            T *= alpha
            if T < T_min:
                break

        return best_x, best_value

    return (knapsack_simulated_annealing,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""5. AMPL Python API implement:""")
    return


@app.cell
def _():
    """
    from amplpy import AMPL


    def solve_knapsack_ampl(c, a, B):

        ampl = AMPL()
        ampl.set_option("solver", "gurobi")

        n = len(c)

        # AMPL model
        ampl.eval(
            '''
            set ITEMS;

            param c {ITEMS};  # value
            param a {ITEMS};  # weight
            param B;          # capacity

            var x {i in ITEMS} binary;

            maximize TotalValue:
                sum {i in ITEMS} c[i] * x[i];

            subject to Capacity:
                sum {i in ITEMS} a[i] * x[i] <= B;
            '''
        )

        items = list(range(1, n + 1))
        ampl.set["ITEMS"].set_values(items)
        ampl.param["c"].set_values(dict(zip(items, c)))
        ampl.param["a"].set_values(dict(zip(items, a)))
        ampl.param["B"] = B

        ampl.solve()

        x = ampl.get_variable("x")
        best_x = np.array([int(round(x[i].value())) for i in items])
        best_value = ampl.get_objective("TotalValue").value()

        return best_x, best_value
    """
    return


@app.cell
def _(np):
    def generate_knapsack_instance(n=50, seed=None):
        if seed is not None:
            np.random.seed(seed)

        c = np.random.randint(10, 100, size=n)  # values between 10 and 100
        a = np.random.randint(5, 50, size=n)  # weights between 5 and 50
        B = int(np.random.uniform(0.5, 0.7) * np.sum(a))  # 50–70% of total weight

        return c.tolist(), a.tolist(), B

    c, a, B = generate_knapsack_instance(n=30)
    return B, a, c


@app.cell
def _(
    B,
    a,
    c,
    knapsack_local_search,
    knapsack_simulated_annealing,
    knapsack_tabu_search,
):
    x_best, val_best = knapsack_local_search(c, a, B)
    print("Local search:")
    print("Selected:", x_best)
    print("Total value:", val_best)

    x_best, val_best = knapsack_tabu_search(c, a, B)
    print("Tabu search:")
    print("Best solution:", x_best)
    print("Total value:", val_best)

    x_best, val_best = knapsack_simulated_annealing(c, a, B)
    print("Simulated Annealing:")
    print("Best solution:", x_best)
    print("Total value:", val_best)

    """
    x_best, val_best = solve_knapsack_ampl(c, a, B)
    print("Gurobi:")
    print("Selected:", x_best)
    print("Total Value:", val_best)
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Problem 5""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Consider the dynamic single item inventory problem. Your company sells a single item. Right now, you have $x_0$ units of the item. In each day $t$, some number $d_t$ of customers arrive and attempt to buy the product. Each unit sold produces \$r of revenue. If you have more customers than demand in any day, you lose the excess customers, and do not sell anything to them. At the end of each day, you can choose to order more product, which will arrive $L$ days later. If you order $k$ units of products, you must pay \$ $\alpha +\beta k$, where $\alpha$ is a flat delivery fee, and $\beta$ is the per-unit cost. If we let $z_t$ be the amount ordered at end of day $t$, then the amount of inventory $x_t$ available at the beginning of each day t can be calculated recursively by:

    $$x_t = \begin{cases} z_{t - L} &, d_{t-1} \ge x_{t-1}, \\ x_{t - 1} - d_{t - 1} + z_{t - L} &, d_{t-1} < x_{t-1}.\end{cases}$$

    Suppose that you have some method for producing an estimate $\hat{d}_t$ for the value $d_t$. Describe, in detail, a method that you could use to decide at the end of each day how much inventory to order.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Assume expectation of $d_t$ is positive, suppose $\alpha = 0$ then we should always just order any many as we can because there is no penalties on overstocking (can introduce penalty by adding storage fee or spoilage). With a positive $\alpha$, ordering too often becomes expensive. The general idea is to wait until a *projected* shortfall is large enough that is worth paying the flat fee $\alpha$.

    1. Step 1: Simulate inventory over days $t, \dots, t+L$ using the formula and the demand estimation  
    2. Step 2: Forecast demand over window starting at $t+L$:  
        Choose a short forecast horizon $H'$ and compute: $D = \sum_{s=t+L}^{t+L+H'} \hat{d}_s$
    3. Step 3: Compute projected shortfall $k = \max(0, D - x_{t+L})$: the number of units needed (beyond what you expect to have) to meet projected demand
    4. Step 4: Compute gain from selling: $G = (r - \beta) \cdot k$, place the order if $G > \alpha$
    5. Step 5: Main records and proceed to next day
    """
    )
    return


if __name__ == "__main__":
    app.run()
