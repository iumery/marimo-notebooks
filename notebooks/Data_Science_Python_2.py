import marimo

__generated_with = "0.15.3"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


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
    mo.md(r"""# Optimization, Part 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Goal""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""This practice set is designed to develop the ability to model and solve a variety of optimization problems. It includes problems that cover key topics: moment optimization over probability distributions, equivalence of integer program formulations, modeling logical constraints using binary variables, scheduling tasks to minimize weighted completion time, and converting general linear programs into standard form."""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Attention!

    Code in this notebook **WOULD NOT** run directly as Marimo does not include AMPL package (it needs registration anyway). Check AMPL [official website](https://ampl.com) for more info.

    ///
    """
    )
    return


@app.cell
def _():
    """
    from amplpy import AMPL
    from itertools import product
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Problem 1""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Form a linear program that identifies the discrete probability distribution, that takes `k` values, whose first and second moment are `M_1` and `M_2`, and whose fourth moment is maximized.

    Solve this linear program for `k = 5; M_1 = 3.5; M_2 = 15`, and `k = 80; M_1 = 10; M_2 = 200`.
    """
    )
    return


@app.cell
def _():
    '''
    def solve_moment_problem(k, M1, M2):
        ampl = AMPL()

        ampl.eval(
            """
            param k;
            set INDEX := 1..k;
            param M1;
            param M2;

            var p {INDEX} >= 0;

            s.t. TotalProb: sum {i in INDEX} p[i] = 1;
            s.t. FirstMoment: sum {i in INDEX} i * p[i] = M1;
            s.t. SecondMoment: sum {i in INDEX} (i^2) * p[i] = M2;

            maximize FourthMoment: sum {i in INDEX} (i^4) * p[i];
            """
        )

        ampl.param["k"] = k
        ampl.param["M1"] = M1
        ampl.param["M2"] = M2

        ampl.set_option("solver", "gurobi")

        ampl.solve()

        p_vals = ampl.get_variable("p").to_dict()
        fourth_moment = ampl.get_objective("FourthMoment").value()

        return p_vals, fourth_moment
    '''
    return


@app.cell
def _():
    """
    k = 5
    M1 = 3.5
    M2 = 15

    p_opt, max_fourth_moment = solve_moment_problem(k, M1, M2)

    print("Optimal Distribution:")
    for i in range(1, k + 1):
        print(f"p_{i} = {p_opt[i]:.4f}")

    print(f"Max Fourth Moment = {max_fourth_moment:.4f}")

    # Gurobi 12.0.2:Gurobi 12.0.2: optimal solution; objective 344
    # 3 simplex iterations
    # Optimal Distribution:
    # p_1 = 0.1250
    # p_2 = 0.3333
    # p_3 = 0.0000
    # p_4 = 0.0000
    # p_5 = 0.5417
    # Max Fourth Moment = 344.0000
    """
    return


@app.cell
def _():
    """
    k = 80
    M1 = 10
    M2 = 200

    p_opt, max_fourth_moment = solve_moment_problem(k, M1, M2)

    print("Optimal Distribution:")
    for i in range(1, k + 1):
        print(f"p_{i} = {p_opt[i]:.4f}")

    print(f"Max Fourth Moment = {max_fourth_moment:.4f}")

    # Gurobi 12.0.2:Gurobi 12.0.2: optimal solution; objective 822680
    # 10 simplex iterations
    # Optimal Distribution:
    # p_1 = 0.0000
    # p_2 = 0.0000
    # p_3 = 0.0000
    # p_4 = 0.0000
    # p_5 = 0.0000
    # p_6 = 0.0000
    # p_7 = 0.0000
    # p_8 = 0.4167
    # p_9 = 0.5634
    # p_10 = 0.0000
    # p_11 = 0.0000
    # p_12 = 0.0000
    # p_13 = 0.0000
    # p_14 = 0.0000
    # p_15 = 0.0000
    # p_16 = 0.0000
    # p_17 = 0.0000
    # p_18 = 0.0000
    # p_19 = 0.0000
    # p_20 = 0.0000
    # p_21 = 0.0000
    # p_22 = 0.0000
    # p_23 = 0.0000
    # p_24 = 0.0000
    # p_25 = 0.0000
    # p_26 = 0.0000
    # p_27 = 0.0000
    # p_28 = 0.0000
    # p_29 = 0.0000
    # p_30 = 0.0000
    # p_31 = 0.0000
    # p_32 = 0.0000
    # p_33 = 0.0000
    # p_34 = 0.0000
    # p_35 = 0.0000
    # p_36 = 0.0000
    # p_37 = 0.0000
    # p_38 = 0.0000
    # p_39 = 0.0000
    # p_40 = 0.0000
    # p_41 = 0.0000
    # p_42 = 0.0000
    # p_43 = 0.0000
    # p_44 = 0.0000
    # p_45 = 0.0000
    # p_46 = 0.0000
    # p_47 = 0.0000
    # p_48 = 0.0000
    # p_49 = 0.0000
    # p_50 = 0.0000
    # p_51 = 0.0000
    # p_52 = 0.0000
    # p_53 = 0.0000
    # p_54 = 0.0000
    # p_55 = 0.0000
    # p_56 = 0.0000
    # p_57 = 0.0000
    # p_58 = 0.0000
    # p_59 = 0.0000
    # p_60 = 0.0000
    # p_61 = 0.0000
    # p_62 = 0.0000
    # p_63 = 0.0000
    # p_64 = 0.0000
    # p_65 = 0.0000
    # p_66 = 0.0000
    # p_67 = 0.0000
    # p_68 = 0.0000
    # p_69 = 0.0000
    # p_70 = 0.0000
    # p_71 = 0.0000
    # p_72 = 0.0000
    # p_73 = 0.0000
    # p_74 = 0.0000
    # p_75 = 0.0000
    # p_76 = 0.0000
    # p_77 = 0.0000
    # p_78 = 0.0000
    # p_79 = 0.0000
    # p_80 = 0.0200
    # Max Fourth Moment = 822680.0000
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Problem 2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Show that the following integer programs all have the same set of feasible solutions:

    - $97x_1 + 32x_2 + 25x_3 + 20x_4 \le 139$, $x_i \in \lbrace 0 , 1 \rbrace$
    - $2x_1 + x_2 + x_3 + x_4 \le 3$, $x_i \in \lbrace 0 , 1 \rbrace$
    - $x_1 + x_2 + x_3 \le 2$, $x_1 + x_2 + x_4 \le 2$, $x_1 + x_3 + x_4 \le 2$, $x_i \in \lbrace 0 , 1 \rbrace$

    This is an easy exericse that can be done by hand. AMPL does not provide a native way to check feasible solutions. To check with Python:
    """
    )
    return


@app.cell
def _():
    """
    feasible_points = list(product([0, 1], repeat=4))


    def constraint1(x):
        return 97 * x[0] + 32 * x[1] + 25 * x[2] + 20 * x[3] <= 139


    def constraint2(x):
        return 2 * x[0] + x[1] + x[2] + x[3] <= 3


    def constraint3(x):
        return (
            x[0] + x[1] + x[2] <= 2 and x[0] + x[1] + x[3] <= 2 and x[0] + x[2] + x[3] <= 2
        )


    feasible1 = {x for x in feasible_points if constraint1(x)}
    feasible2 = {x for x in feasible_points if constraint2(x)}
    feasible3 = {x for x in feasible_points if constraint3(x)}

    print(
        "All three constraint systems have the same feasible set:",
        feasible1 == feasible2 == feasible3,
    )

    print("Feasible solutions (x1, x2, x3, x4):")
    for sol in sorted(feasible1):
        print(sol)

    # All three constraint systems have the same feasible set: True
    # Feasible solutions (x1, x2, x3, x4):
    # (0, 0, 0, 0)
    # (0, 0, 0, 1)
    # (0, 0, 1, 0)
    # (0, 0, 1, 1)
    # (0, 1, 0, 0)
    # (0, 1, 0, 1)
    # (0, 1, 1, 0)
    # (0, 1, 1, 1)
    # (1, 0, 0, 0)
    # (1, 0, 0, 1)
    # (1, 0, 1, 0)
    # (1, 1, 0, 0)
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Problem 3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Model the following constraints in choosing a subset from 1, 2, ..., 7:

    - You cannot choose all of them
    - You must choose at least one of them
    - 1 cannot be chosen if 3 is chosen
    - 4 can only be chosen if 2 is chosen
    - You must either choose both 1 and 5, or neither of them
    - You must either choose at least one of 1, 2, 3, or choose at least two of 2, 4, 5, 6

    An example objective is given (maximize items chosen), the following is the full AMPL setup:
    """
    )
    return


@app.cell
def _():
    '''
    def solve_subset_selection():
        ampl = AMPL()

        ampl.eval(
            """
            set I := 1..7;

            var x {i in I} binary;
            var y binary;

            # Constraints
            s.t. NotAll: sum {i in I} x[i] <= 6;
            s.t. AtLeastOne: sum {i in I} x[i] >= 1;
            s.t. No1if3: x[1] + x[3] <= 1;
            s.t. FourOnlyIfTwo: x[4] <= x[2];
            s.t. OneAndFiveTogether: x[1] = x[5];

            # Disjunctive constraint using auxiliary binary y
            s.t. DisjunctLeft:  x[1] + x[2] + x[3] >= 1 - 3*y;
            s.t. DisjunctRight: x[2] + x[4] + x[5] + x[6] >= 2 - 4*(1 - y);

            # Dummy objective: maximize number of selected items
            maximize NumSelected: sum {i in I} x[i];
            """
        )

        ampl.set_option("solver", "gurobi")
        ampl.solve()

        x_vals = ampl.get_variable("x").to_dict()
        selected_items = [i for i in range(1, 8) if x_vals[i] == 1]
        num_selected = ampl.get_objective("NumSelected").value()

        return selected_items, num_selected
    '''
    return


@app.cell
def _():
    """
    items, total = solve_subset_selection()

    print("Selected items:", items)
    print("Total selected:", int(total))

    # Gurobi 12.0.2:Gurobi 12.0.2: optimal solution; objective 6
    # 0 simplex iterations
    # Selected items: [1, 2, 4, 5, 6, 7]
    # Total selected: 6
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Problem 4""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Suppose that we have a single machine and we have several tasks to perform on this machine. The machine process one task at a time but we can choose the order in which the tasks are performed. Suppose each task has a weight, we want to minimize the average weighted completion time of the tasks. To clarify, the *completion time* means the cumulative completion time. For example, suppose we have two tasks A, B. Suppose they take 1 and 10 minutes to complete, respectively, and they have weights 10 and 1, respectively, then:

    - If we do A then B, the average weighted completion time is calculated as $1 \cdot 10 + (1 + 10) \cdot 1 = 21$, and
    - If we do B then A, the average weighted completion time is calculated as $10 \cdot 1 + (10 + 1) \cdot 10 = 120$

    We can show that if there is a sequence of times $x_1, \dots, x_k$ that satisfy the constraints: for all distinct tasks $i$ and $j$, either $x_j \ge x_i + t_i$ or $x_i \ge x_j + t_j$, where $t_i$ is the time to complete the single task $i$, then the tasks can be placed in a sequence such that task $i$ is started at time $x_i$. In other words, the above constraints are the ones we should use in the program.

    Formulate an integer program that can be used to identify the optimal sequence of tasks, and solve the following instance:

    | Task | Processing Time | Weight |
    | ---- | --------------- | ------ |
    | 1 | 5 minutes | 0.1 |
    | 2 | 10 minutes | 0.2 |
    | 3 | 17 minutes | 0.3 |
    | 4 | 8 minutes | 0.15 |
    | 5 | 9 minutes | 0.05 |
    | 6 | 14 minutes | 0.05 |
    | 7 | 28 minutes | 0.15 |
    """
    )
    return


@app.cell
def _():
    '''
    def solve_weighted_completion_time(task_ids, processing_times, weights):
        ampl = AMPL()

        ampl.eval(
            """
            set TASKS;

            param t {TASKS};  # processing time
            param w {TASKS};  # weight

            var x {TASKS} >= 0;  # start time
            var z {i in TASKS, j in TASKS: i != j} binary;  # precedence

            param BIG;

            # Disjunctive constraints
            s.t. Ordering1 {i in TASKS, j in TASKS: i != j}:
                x[j] >= x[i] + t[i] - BIG * (1 - z[i,j]);

            s.t. Ordering2 {i in TASKS, j in TASKS: i != j}:
                x[i] >= x[j] + t[j] - BIG * z[i,j];

            # Objective: minimize weighted completion time
            minimize WeightedCompletion:
                sum {i in TASKS} w[i] * (x[i] + t[i]);
            """
        )

        ampl.set["TASKS"] = task_ids
        ampl.param["BIG"] = sum(processing_times.values())  # conservative Big-M

        ampl.param["t"] = processing_times
        ampl.param["w"] = weights

        ampl.set_option("solver", "gurobi")
        ampl.solve()

        x_vals = ampl.get_variable("x").to_dict()
        C_vals = {i: x_vals[i] + processing_times[i] for i in task_ids}
        obj_val = ampl.get_objective("WeightedCompletion").value()

        schedule = sorted(task_ids, key=lambda i: x_vals[i])

        return schedule, C_vals, obj_val
    '''
    return


@app.cell
def _():
    """
    task_ids = list(range(1, 8))
    processing_times = {1: 5, 2: 10, 3: 17, 4: 8, 5: 9, 6: 14, 7: 28}
    weights = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.15, 5: 0.05, 6: 0.05, 7: 0.15}

    schedule, completion_times, total = solve_weighted_completion_time(
        task_ids, processing_times, weights
    )

    print("Optimal Task Order:", schedule)
    print("Completion Times:")
    for i in schedule:
        print(f"Task {i}: {completion_times[i]} minutes")

    print(f"Total Weighted Completion Time = {total:.4f}")

    # Gurobi 12.0.2:Gurobi 12.0.2: optimal solution; objective 37.5
    # 49 simplex iterations
    # 1 branching node
    # Optimal Task Order: [1, 2, 4, 3, 5, 7, 6]
    # Completion Times:
    # Task 1: 5 minutes
    # Task 2: 15 minutes
    # Task 4: 23 minutes
    # Task 3: 40 minutes
    # Task 5: 49 minutes
    # Task 7: 77 minutes
    # Task 6: 91 minutes
    # Total Weighted Completion Time = 37.5000
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
    A linear program with the form 

    $$\begin{aligned} \max(c^Tx) &\text{ s.t.} \\ Ax &\le b \\ x &\ge 0 \end{aligned}$$

    is said to be of standard form. Describe how to re-formulate a linear program into a standard form in the following situations:

    - the linear problem is a minimization problem
    - one constraint is an equality constraint
    - one constraint is a greater-than-or-equal constraint
    - one variable is restricted to be non-positive
    - one variable is *not* restricted

    Write the following linear program in standard form: 

    $$\begin{aligned} \min(2x_1 - x_2 + 4x_3) &\text{ s.t.} \\ x_1 + x_2 + x_4 &\le 2 \\ 3x_2 - x_3 &= 5 \\ x_3 + x_4 &\ge 3 \\ x_1 &\ge 0 \\ x_3 &\le 0 \end{aligned}$$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Solution:

    - negate the objective coefficients, $\min(c^Tx)$ becomes $\max(-c^Tx)$
    - $a^T x = b$ becomes two inequalities $\begin{cases} a^T x \le b \\ -a^T x \le -b \end{cases}$
    - $a^T x \ge b$ becomes $-a^T x \le -b$
    - introduce $x_i' = -x_i$, $x_i \le 0$ becomes $x_i' \ge 0$
    - introduce $x_i = x_i^+ - x_i^-$, add constraints $x_i^+, x_i^- \ge 0$

    Use above, the example linear program can be written as:

    $$\begin{aligned} \max(-2x_1 + x_2^+ - x_2^- + 4x_3') &\text{ s.t.} \\ x_1 + x_2^+ - x_2^- + x_4^+ - x_4^- &\le 2 \\ 3x_2^+ - 3x_2^- + x_3' &\le 5 \\ -3x_2^+ + 3x_2^- - x_3' &\le -5 \\ x_3' - x_4^+ + x_4^- &\le -3 \\ x_1, x_2^+, x_2^-, x_3', x_4^+, x_4^- &\ge 0\end{aligned}$$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## An extra question for linear programs""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Even'Star Organic Farm was founded in 1997 by Brett Grohsgal, a former chef in Washington DC. The company owns a 104-acre farm in southern Maryland, and grows and sells organic produce. This problem describes the business issues faced by Brett, and the data is based on actual observations.

    Brett has decided to grow five different types of produce: watermelon, basil, cucumbers, sweet potatoes, and winter squash. He distributes his produce through three different channels: Restaurants, Community-Supported Agriculture, and Farmers' Markets.

    Initially, he sold exclusively to restaurants. He knows of 20 restaurants that will buy his produce from his connections as a former chef. As his farm expanded, he also started selling his produce at a local farmers' market, where he can command a higher price. Recently, he has also started selling through Community Supported Agriculture (CSA), a program in which individuals pay a $400 subscription price to get a box of produce each week for 15 weeks. He currently knows of 90 individuals who are interested in buying his produce through the CSA program.

    Brett wanted to decide the number of cases of each type of produce to sell in each channel (there are 15 decision variables). Brett's objective is to maximize total profit (total revenue minus total cost).

    The variable cost per client is:

    - Restaurant: \$214.40
    - CSA: \$31.68
    - Farmer's Market: \$0

    To compute the total variable cost for each restaurant client, we use the information that eachrestaurant client will buy 119 cases of produce during the season. So, the total number of restaurantclients served in a season can be computed as the total number of cases sold to restaurants, dividedby 119. Note that the number of restaurant clients Brett gives produce to could be fractional(like 16.57). This is a simplification we'll make for this problem, so please ignore the fact that thisnumber should be integer.

    To compute the total variable cost for CSA clients, we need to know that each CSA customerwill buy $400 worth of produce during the season. So, the total number of CSA clients servedcan be computed by dividing the total dollar amount sent to CSA customers by $400. Note thatthe number of CSA clients Brett gives produce to could be fractional (like 16.57). This is againa simplification we'll make for this problem, so please ignore the fact that this number should beinteger.

    There is no variable cost for farmers' market clients.

    Brett has a limited amount of produce that he can sell each season, and he needs to decide howmuch produce to sell through each channel (restaurants, CSA, or farmers' markets). Brett can't sellnegative cases, and he can't sell more cases than he produces. Produce Data:

    | Produce | Number of Available Cases | Restaurant Price | CSA Price | Farmer's Market Price |
    | ------- | ------------------------- | ---------------- | --------- | --------------------- |
    | Watermelon | 167 | \$20 | \$20 | \$20.25 |
    | Basil | 406 | \$26 | \$36 | \$34 |
    | Cucumber | 251 | \$24 | \$24 | \$25.20 |
    | Sweet Potato | 107 | \$36 | \$36 | \$36 |
    | Winter Squash | 133 | \$36 | \$36 | \$36 |

    Due to the truck capacity, the number of cases sold at the farmers' market can't be more than 500. At most 20 restaurants will buy his produce, and at most 90 CSA customers will buy his produce.

    Model Brett's problem as a linear optimization problem and solve it to get the optimal solution.

    Now suppose that Brett has purchased additional acres of land, which allows him to produce 10 additional cases of one of his vegetables. Which vegetable should he plant on these additional acres?
    """
    )
    return


@app.cell
def _():
    """
    def solve_optimize_produce_allocation_array(produce_array, produce_names, cost_data):

        channels = ["Restaurant", "CSA", "FarmersMarket"]

        # Basic sanity check
        assert produce_array.shape == (
            len(produce_names),
            len(channels) + 1,
        ), "produce_array shape must match (num_produce, 1 + num_channels)"

        # Init AMPL
        ampl = AMPL()
        ampl.set_option("solver", "gurobi")

        # AMPL model string
        ampl.eval(
            r'''
            set PRODUCE;
            set CHANNELS;

            param Supply {PRODUCE} >= 0;
            param Price {PRODUCE, CHANNELS} >= 0;
            param CostPerCase {CHANNELS} default 0;

            param CSACostRate;
            param RestaurantCasePerClient;
            param CSARevenuePerClient;

            param MaxRestaurantClients;
            param MaxCSAClients;
            param MaxFarmersMarketCases;

            var x {PRODUCE, CHANNELS} >= 0;

            maximize TotalProfit:
                sum {i in PRODUCE, j in CHANNELS} (
                    if j = "CSA" then
                        x[i,j] * Price[i,j] * (1 - CSACostRate)
                    else
                        x[i,j] * (Price[i,j] - CostPerCase[j])
                );

            subject to SupplyLimit {i in PRODUCE}:
                sum {j in CHANNELS} x[i,j] <= Supply[i];

            subject to RestaurantLimit:
                sum {i in PRODUCE} x[i,"Restaurant"] <= MaxRestaurantClients * RestaurantCasePerClient;

            subject to CSALimit:
                sum {i in PRODUCE} x[i,"CSA"] * Price[i,"CSA"] <= MaxCSAClients * CSARevenuePerClient;

            subject to FarmersMarketLimit:
                sum {i in PRODUCE} x[i,"FarmersMarket"] <= MaxFarmersMarketCases;
            '''
        )

        # Sets
        ampl.set["PRODUCE"].set_values(produce_names)
        ampl.set["CHANNELS"].set_values(channels)

        # Supply
        ampl.param["Supply"].set_values(
            {p: produce_array[i, 0] for i, p in enumerate(produce_names)}
        )

        # Price (skip first column)
        price_dict = {
            (produce_names[i], channels[j]): float(produce_array[i, j + 1])
            for i in range(len(produce_names))
            for j in range(len(channels))
        }
        ampl.param["Price"].set_values(price_dict)

        # Cost per case
        restaurant_cost_per_case = (
            cost_data["restaurant_cost_per_client"] / cost_data["num_restaurant"]
        )
        cost_per_case = {
            "Restaurant": restaurant_cost_per_case,
            "CSA": 0.0,
            "FarmersMarket": 0.0,
        }
        ampl.param["CostPerCase"].set_values(cost_per_case)

        # Client-level constraints
        ampl.param["RestaurantCasePerClient"] = cost_data["num_restaurant"]
        ampl.param["CSARevenuePerClient"] = cost_data["csa_revenue_per_client"]
        ampl.param["CSACostRate"] = (
            cost_data["csa_cost_per_client"] / cost_data["csa_revenue_per_client"]
        )

        ampl.param["MaxRestaurantClients"] = cost_data["max_restaurant_clients"]
        ampl.param["MaxCSAClients"] = cost_data["max_csa_clients"]
        ampl.param["MaxFarmersMarketCases"] = cost_data["max_farmers_market_cases"]

        # Solve
        ampl.solve()

        # Extract results
        x = ampl.get_variable("x")
        result = {
            produce: {channel: x[produce, channel].value() for channel in channels}
            for produce in produce_names
        }

        return result, ampl
    """
    return


@app.cell
def _():
    """
    produce_names = ["Watermelon", "Basil", "Cucumber", "SweetPotato", "WinterSquash"]

    # rows: Watermelon, Basil, Cucumber, SweetPotato, WinterSquash according to produce_names above
    # cols: Supply, R Price, C Price, F Price
    produce_array = np.array(
        [
            [167, 20.0, 20.0, 20.25],
            [406, 26.0, 36.0, 34.0],
            [251, 24.0, 24.0, 25.2],
            [107, 36.0, 36.0, 36.0],
            [133, 36.0, 36.0, 36.0],
        ]
    )

    cost_data = {
        "restaurant_cost_per_client": 214.4,
        "num_restaurant": 119,
        "csa_cost_per_client": 31.68,
        "csa_revenue_per_client": 400,
        "max_restaurant_clients": 20,
        "max_csa_clients": 90,
        "max_farmers_market_cases": 500,
    }

    result, ampl = solve_optimize_produce_allocation_array(
        produce_names=produce_names,
        produce_array=produce_array,
        cost_data=cost_data,
    )

    result

    # Gurobi 12.0.2:Gurobi 12.0.2: optimal solution; objective 31520.69725
    # 1 simplex iteration
    #
    # {'Watermelon': {'Restaurant': 0.0, 'CSA': 0.0, 'FarmersMarket': 167.0},
    #  'Basil': {'Restaurant': 0.0, 'CSA': 406.0, 'FarmersMarket': 0.0},
    #  'Cucumber': {'Restaurant': 0.0, 'CSA': 0.0, 'FarmersMarket': 251.0},
    #  'SweetPotato': {'Restaurant': 25.0, 'CSA': 0.0, 'FarmersMarket': 82.0},
    #  'WinterSquash': {'Restaurant': 133.0, 'CSA': 0.0, 'FarmersMarket': 0.0}}
    """
    return


@app.cell
def _():
    """
    def recommend_extra_production(ampl, produce_names, extra_cases=10):

        duals = ampl.get_constraint("SupplyLimit")
        shadow_prices = {produce: duals[produce].dual() for produce in produce_names}

        gains = {produce: shadow_prices[produce] * extra_cases for produce in produce_names}
        best_produce, best_gain = max(gains.items(), key=lambda x: x[1])

        print(
            f"\nBrett should grow more {best_produce}, expecting an extra ${best_gain:.2f} profit for {extra_cases} additional cases.\n"
        )

        print(f"{'Produce':20} {'Shadow Price'}")
        for produce in produce_names:
            dual = shadow_prices[produce]
            print(f"{produce:20} ${dual:.4f}")

        return best_produce, best_gain
    """
    return


@app.cell
def _():
    """
    _, _ = recommend_extra_production(ampl, produce_names, 10)

    # Brett should grow more SweetPotato, expecting an extra $341.98 profit for 10 additional cases.

    # Produce              Shadow Price
    # Watermelon           $18.4483
    # Basil                $33.1488
    # Cucumber             $23.3983
    # SweetPotato          $34.1983
    # WinterSquash         $34.1983
    """
    return


if __name__ == "__main__":
    app.run()
