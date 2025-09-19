import marimo

__generated_with = "0.15.4"
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
            "/notebooks/SQL_20250917.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250919.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2372

    Table: Salesperson

    | Column Name    | Type    |
    |----------------|---------|
    | salesperson_id | int     |
    | name           | varchar |

    salesperson_id contains unique values. Each row in this table shows the ID of a salesperson.

    Table: Customer

    | Column Name    | Type |
    |----------------|------|
    | customer_id    | int  |
    | salesperson_id | int  |

    customer_id contains unique values. salesperson_id is a foreign key (reference column) from the Salesperson table. Each row in this table shows the ID of a customer and the ID of the salesperson. 

    Table: Sales

    | Column Name | Type |
    |-------------|------|
    | sale_id     | int  |
    | customer_id | int  |
    | price       | int  |

    sale_id contains unique values. customer_id is a foreign key (reference column) from the Customer table. Each row in this table shows ID of a customer and the price they paid for the sale with sale_id.

    Write a solution to report the sum of prices paid by the customers of each salesperson. If a salesperson does not have any customers, the total value should be 0.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        salesperson_id,
        name,
        SUM(COALESCE(price, 0)) AS total
    FROM
        Salesperson
            LEFT JOIN Customer USING (salesperson_id)
            LEFT JOIN Sales USING (customer_id)
    GROUP BY
        1, 2
    """
    return


@app.cell
def _():
    import pandas as pd

    def calculate_influence(salesperson: pd.DataFrame, customer: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
        df = pd.merge(salesperson, customer, how="left", on="salesperson_id")
        df = pd.merge(df, sales, how="left", on="customer_id")
        df.fillna(0, inplace=True)
        df = df.groupby(["salesperson_id", "name"], as_index=False).agg(total=("price", "sum"))
        return df

    return


if __name__ == "__main__":
    app.run()
