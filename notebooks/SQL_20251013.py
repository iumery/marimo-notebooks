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
            "/notebooks/SQL_20251010.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251014.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2985

    Table: Orders

    | Column Name       | Type |
    |-------------------|------|
    | order_id          | int  |
    | item_count        | int  |
    | order_occurrences | int  |

    order_id is column of unique values for this table. This table contains order_id, item_count, and order_occurrences.

    Write a solution to calculate the average number of items per order, rounded to 2 decimal places.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        ROUND(SUM(item_count * order_occurrences) * 1.0 / SUM(order_occurrences), 2) AS average_items_per_order
    FROM
        Orders
    """
    return


@app.cell
def _():
    import pandas as pd

    def compressed_mean(orders: pd.DataFrame) -> pd.DataFrame:
        average_items_per_order = (sum(orders["item_count"] * orders["order_occurrences"]) / sum(orders["order_occurrences"])).round(2)
        df = pd.DataFrame({"average_items_per_order": [average_items_per_order]})
        return df

    return


if __name__ == "__main__":
    app.run()
