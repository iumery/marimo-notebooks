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
            "/notebooks/SQL_20250919.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250923.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2388

    Table: CoffeeShop

    | Column Name | Type    |
    |-------------|---------|
    | id          | int     |
    | drink       | varchar |

    id is the primary key (column with unique values) for this table. Each row in this table shows the order id and the name of the drink ordered. Some drink rows are nulls.

    Write a solution to replace the null values of the drink with the name of the drink of the previous row that is not null. It is guaranteed that the drink on the first row of the table is not null.

    Return the result table in the same order as the input.
    """
    )
    return


@app.cell
def _():
    """
    WITH group_by_last_nonnull AS (
        SELECT
            id,
            drink,
            COUNT(1) FILTER (WHERE drink IS NOT NULL) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS grouping
        FROM
            coffeeshop
    )
    SELECT
        id,
        COALESCE(drink, FIRST_VALUE(drink) OVER (PARTITION BY grouping)) AS drink
    FROM
        group_by_last_nonnull
    """
    return


@app.cell
def _():
    import pandas as pd


    def change_null_values(coffee_shop: pd.DataFrame) -> pd.DataFrame:
        return coffee_shop.fillna(method="ffill")
    return


if __name__ == "__main__":
    app.run()
