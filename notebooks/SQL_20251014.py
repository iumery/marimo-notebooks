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
            "/notebooks/SQL_20251013.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251015.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2986

    Table: Transactions

    | Column Name      | Type     |
    |------------------|----------|
    | user_id          | int      |
    | spend            | decimal  |
    | transaction_date | datetime |

    (user_id, transaction_date) is column of unique values for this table. This table contains user_id, spend, and transaction_date.

    Write a solution to find the third transaction (if they have at least three transactions) of every user, where the spending on the preceding two transactions is lower than the spending on the third transaction.

    Return the result table by user_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH transaction_ranked AS (
        SELECT
            user_id,
            spend,
            transaction_date,
            ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_date) AS rnk
        FROM
            Transactions
    ),
    max_of_two AS (
        SELECT
            user_id,
            MAX(spend) AS max_spend_for_two
        FROM
            transaction_ranked
        WHERE
            rnk < 3
        GROUP BY
            1
    )
    SELECT
        user_id,
        spend AS third_transaction_spend,
        transaction_date AS third_transaction_date
    FROM
        transaction_ranked
            JOIN max_of_two USING (user_id)
    WHERE
        spend > max_spend_for_two AND rnk = 3
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def find_third_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
        df = transactions.sort_values(["user_id", "transaction_date"])

        df = df.groupby("user_id").head(3)

        df = df[
            (df["spend"] > df.shift(1)["spend"])
            & (df["user_id"] == df.shift(1)["user_id"])
            & (df["spend"] > df.shift(2)["spend"])
            & (df["user_id"] == df.shift(2)["user_id"])
        ]
        df = df.rename(
            columns={
                "spend": "third_transaction_spend",
                "transaction_date": "third_transaction_date",
            }
        )[
            ["user_id", "third_transaction_spend", "third_transaction_date"]
        ].sort_values("user_id")
        return df

    return


if __name__ == "__main__":
    app.run()
