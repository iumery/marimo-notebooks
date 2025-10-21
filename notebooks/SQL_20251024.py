import marimo

__generated_with = "0.16.5"
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
            "/notebooks/SQL_20251023.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251027.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3050

    Table: Toppings

    | Column Name  | Type    | 
    |--------------|---------|
    | topping_name | varchar | 
    | cost         | decimal |

    topping_name is the primary key for this table. Each row of this table contains topping name and the cost of the topping. 

    Write a solution to calculate the total cost of all possible 3-topping pizza combinations from a given list of toppings. The total cost of toppings must be rounded to 2 decimal places.

    Note:

    - Do not include the pizzas where a topping is repeated. For example, ‘Pepperoni, Pepperoni, Onion Pizza’.
    - Toppings must be listed in alphabetical order. For example, 'Chicken, Onions, Sausage'. 'Onion, Sausage, Chicken' is not acceptable.

    Return the result table ordered by total cost in descending order and combination of toppings in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        t1.topping_name || ',' || t2.topping_name || ',' || t3.topping_name AS pizza,
        t1.cost + t2.cost + t3.cost AS total_cost
    FROM
        Toppings t1
            JOIN Toppings t2 ON t1.topping_name < t2.topping_name
            JOIN Toppings t3 ON t2.topping_name < t3.topping_name
    ORDER BY
        2 DESC,
        1 ASC;
    """
    return


@app.cell
def _():
    import pandas as pd


    def cost_analysis(toppings: pd.DataFrame) -> pd.DataFrame:
        df = toppings.sort_values("topping_name").reset_index(drop=True)
        pizza = []
        total_cost = []
        for i in range(len(df)):
            for j in range(i + 1, len(df)):
                for k in range(j + 1, len(df)):
                    pizza.append(
                        df["topping_name"][i]
                        + ","
                        + df["topping_name"][j]
                        + ","
                        + df["topping_name"][k]
                    )
                    total_cost.append(
                        round(df["cost"][i] + df["cost"][j] + df["cost"][k], 2)
                    )
        df = pd.DataFrame({"pizza": pizza, "total_cost": total_cost}).sort_values(
            ["total_cost", "pizza"], ascending=[False, True]
        )
        return df
    return


if __name__ == "__main__":
    app.run()
