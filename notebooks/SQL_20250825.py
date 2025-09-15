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
            "/notebooks/SQL_20250822.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250826.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3657

    Table: customer_transactions

    | Column Name      | Type    | 
    |------------------|---------|
    | transaction_id   | int     |
    | customer_id      | int     |
    | transaction_date | date    |
    | amount           | decimal |
    | transaction_type | varchar |

    transaction_id is the unique identifier for this table. transaction_type can be either 'purchase' or 'refund'. Write a solution to find loyal customers. A customer is considered loyal if they meet ALL the following criteria:

    - Made at least 3 purchase transactions.
    - Have been active for at least 30 days.
    - Their refund rate is less than 20% .
    - Return the result table ordered by customer_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        customer_id
    FROM
        customer_transactions
    GROUP BY
        1
    HAVING
        MAX(transaction_date) - MIN(transaction_date) >= 30
            AND COUNT(transaction_id) >= 3
            AND (COUNT(transaction_id) FILTER (WHERE transaction_type = 'refund'))*1.0 / COUNT(transaction_id) < 0.2
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
        customer_transactions["transaction_date"] = pd.to_datetime(customer_transactions["transaction_date"])
        df = customer_transactions.groupby("customer_id").agg(
            date_max=("transaction_date", "max"),
            date_min=("transaction_date", "min"),
            count_all=("transaction_id", "count"),
            refund_ratio=("transaction_type", lambda x: (x == "refund").mean()),
        )
        df["active_range"] = (df["date_max"] - df["date_min"]).dt.days
        df = (
            df[(df["active_range"] >= 30) & (df["count_all"] >= 3) & (df["refund_ratio"] < 0.2)]
            .reset_index()[["customer_id"]]
            .sort_values("customer_id")
        )
        return df

    return


if __name__ == "__main__":
    app.run()
