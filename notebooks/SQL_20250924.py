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
            "/notebooks/SQL_20250923.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250925.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2701

    Table: Transactions

    | Column Name      | Type |
    |------------------|------|
    | transaction_id   | int  |
    | customer_id      | int  |
    | transaction_date | date |
    | amount           | int  |

    transaction_id is the primary key of this table. Each row contains information about transactions that includes unique (customer_id, transaction_date) along with the corresponding customer_id and amount.  

    Write an SQL query to find the customers who have made consecutive transactions with increasing amount for at least three consecutive days. Include the customer_id, start date of the consecutive transactions period and the end date of the consecutive transactions period. There can be multiple consecutive transactions by a customer.

    Return the result table ordered by customer_id, consecutive_start, consecutive_end in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH filtraton AS (
        SELECT
            customer_id, t1.transaction_date
        FROM
            Transactions t1
                JOIN Transactions t2 USING(customer_id)
        WHERE
            t2.amount > t1.amount
                AND t2.transaction_date = t1.transaction_date + INTERVAL '1 day'
    ),
    grouping AS (
        SELECT
            customer_id,
            transaction_date,
            (transaction_date - INTERVAL '1 day' * ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY transaction_date)) AS grp
        FROM
            filtraton
    )
    SELECT
        customer_id,
        MIN(transaction_date) AS consecutive_start,
        CAST(MIN(transaction_date) + INTERVAL '1 day' * COUNT(*) AS DATE) AS consecutive_end
    FROM
        grouping
    GROUP BY
        customer_id, grp
    HAVING
        COUNT(*) >= 2
    ORDER BY
        1, 2;
    """
    return


@app.cell
def _():
    import pandas as pd


    def consecutive_increasing_transactions(
        transactions: pd.DataFrame,
    ) -> pd.DataFrame:
        df = (
            transactions.sort_values(["customer_id", "transaction_date"])
            .reset_index(drop=True)
            .reset_index()
        )
        df["group1"] = (
            df["transaction_date"] - pd.to_datetime("2023-01-01")
        ).dt.days - df.index
        df["group2"] = (df.amount <= df.amount.shift(1)).cumsum().fillna(0)
        df = (
            df.groupby(["customer_id", "group1", "group2"])
            .agg(
                cnt=("index", "count"),
                consecutive_start=("transaction_date", "min"),
                consecutive_end=("transaction_date", "max"),
            )
            .reset_index()
        )
        df = df[df["cnt"] >= 3][
            ["customer_id", "consecutive_start", "consecutive_end"]
        ]
        return df
    return


if __name__ == "__main__":
    app.run()
