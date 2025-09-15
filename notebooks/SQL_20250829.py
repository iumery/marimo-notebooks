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
            "/notebooks/SQL_20250828.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250902.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 1193

    Table: Transactions

    | Column Name   | Type    |
    |---------------|---------|
    | id            | int     |
    | country       | varchar |
    | state         | enum    |
    | amount        | int     |
    | trans_date    | date    |

    id is the primary key of this table. The table has information about incoming transactions. The state column is an enum of type ["approved", "declined"].
 

    Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        TO_CHAR(trans_date, 'YYYY-MM') AS month,
        country,
        COUNT(*) AS trans_count,
        COUNT(state) FILTER (WHERE state = 'approved') AS approved_count,
        SUM(amount) AS trans_total_amount,
        COALESCE(SUM(amount) FILTER (WHERE state = 'approved'), 0) AS approved_total_amount
    FROM
        Transactions
    GROUP BY
        1, 2;
    """
    return


@app.cell
def _():
    import pandas as pd

    def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
        transactions["month"] = pd.to_datetime(transactions["trans_date"]).dt.strftime("%Y-%m")
        transactions["state"] = transactions["state"].str.replace("approved", "1").replace("declined", "0").astype(int)
        transactions["approved_total_amount"] = transactions["amount"] * transactions["state"]
        resq = (
            transactions.groupby(["month", "country"], dropna=False)
            .agg(
                {
                    "id": "count",
                    "state": "sum",
                    "amount": "sum",
                    "approved_total_amount": "sum",
                }
            )
            .reset_index()
        )
        return resq.rename(
            columns={
                "id": "trans_count",
                "state": "approved_count",
                "amount": "trans_total_amount",
            }
        )

    return


if __name__ == "__main__":
    app.run()
