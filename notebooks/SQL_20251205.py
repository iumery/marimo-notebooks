import marimo

__generated_with = "0.18.1"
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
            "/notebooks/SQL_20251204.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251209.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3214

    Table: user_transactions

    | Column Name      | Type     |
    |------------------|----------|
    | transaction_id   | integer  |
    | product_id       | integer  |
    | spend            | decimal  |
    | transaction_date | datetime |

    The transaction_id column uniquely identifies each row in this table. Each row of this table contains the transaction ID, product ID, the spend amount, and the transaction date.

    Write a solution to calculate the year-on-year growth rate for the total spend for each product.

    The result table should include the following columns:

    - year: The year of the transaction.
    - product_id: The ID of the product.
    - curr_year_spend: The total spend for the current year.
    - prev_year_spend: The total spend for the previous year.
    - yoy_rate: The year-on-year growth rate percentage, rounded to 2 decimal places.

    Return the result table ordered by product_id,year in ascending order.
    """)
    return


@app.cell
def _():
    """
    WITH agg_user_transactions AS (
        SELECT
            product_id,
            SUM(spend) AS spend,
            EXTRACT(YEAR FROM transaction_date) AS year
        FROM
            user_transactions
        GROUP BY
            3, 1
    )
    SELECT
        year,
        product_id,
        spend AS curr_year_spend,
        LAG(spend, 1) OVER (PARTITION BY product_id ORDER BY year) AS prev_year_spend,
        ROUND(spend * 100.0 / LAG(spend, 1) OVER (PARTITION BY product_id ORDER BY year) - 100.0, 2) AS yoy_rate
    FROM
        agg_user_transactions
    ORDER BY
        2, 1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def calculate_yoy_growth(user_transactions: pd.DataFrame) -> pd.DataFrame:
        df = user_transactions.copy()
        df["year"] = df["transaction_date"].dt.year
        df = (
            df.groupby(["product_id", "year"], as_index=False)["spend"]
            .sum()
            .sort_values(by=["product_id", "year"])
        )
        df["curr_year_spend"] = df["spend"]
        df["prev_year_spend"] = df.groupby("product_id")["curr_year_spend"].shift(
            1
        )
        df["yoy_rate"] = (
            (df["curr_year_spend"] / df["prev_year_spend"] - 1) * 100.0
        ).round(2)
        df = df[
            [
                "year",
                "product_id",
                "curr_year_spend",
                "prev_year_spend",
                "yoy_rate",
            ]
        ]
        return df
    return


if __name__ == "__main__":
    app.run()
