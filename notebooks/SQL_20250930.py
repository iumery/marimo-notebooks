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
            "/notebooks/SQL_20250929.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251001.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2752

    Table: Transactions

    | Column Name      | Type |
    |------------------|------|
    | transaction_id   | int  |
    | customer_id      | int  |
    | transaction_date | date |
    | amount           | int  |

    transaction_id is the column with unique values of this table. Each row contains information about transactions that includes unique (customer_id, transaction_date) along with the corresponding customer_id and amount.  

    Write a solution to find all customer_id who made the maximum number of transactions on consecutive days.

    Return all customer_id with the maximum number of consecutive transactions. Order the result table by customer_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH grp_info AS (
        SELECT
            customer_id,
            transaction_date - (MIN(transaction_date) OVER (PARTITION BY customer_id)) - (COUNT(1) OVER (PARTITION BY customer_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)) AS consecutive_grp
        FROM (
            SELECT
                *
            FROM
                transactions
            ORDER BY
                customer_id,
                transaction_date
        )
    )
    SELECT
        customer_id
    FROM
        grp_info
    GROUP BY
        customer_id,
        consecutive_grp
    HAVING
        COUNT(*) = (
            SELECT
                COUNT(*)
            FROM
                grp_info
            GROUP BY
                customer_id,
                consecutive_grp
            ORDER BY
                1 DESC
            LIMIT
                1
        )
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def find_customers(transactions: pd.DataFrame) -> pd.DataFrame:
        df = transactions.sort_values(by=["customer_id", "transaction_date"])
        df["rn"] = df.groupby("customer_id").cumcount()
        df["anchor"] = df["transaction_date"] - pd.to_timedelta(df["rn"], unit="D")
        df = df.groupby(["customer_id", "anchor"], as_index=False)["transaction_date"].count()
        max_days = df["transaction_date"].max()
        df = df[df["transaction_date"] == max_days][["customer_id"]].sort_values(by="customer_id")
        return df

    return


if __name__ == "__main__":
    app.run()
