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
            "/notebooks/SQL_20251020.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251022.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2993

    Table: Purchases

    | Column Name   | Type |
    |---------------|------|
    | user_id       | int  |
    | purchase_date | date |
    | amount_spend  | int  |

    (user_id, purchase_date, amount_spend) is the primary key (combination of columns with unique values) for this table. purchase_date will range from November 1, 2023, to November 30, 2023, inclusive of both dates. Each row contains user id, purchase date, and amount spend.

    Write a solution to calculate the total spending by users on each Friday of every week in November 2023. Output only weeks that include at least one purchase on a Friday.

    Return the result table ordered by week of month in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        EXTRACT(WEEK FROM purchase_date) - EXTRACT(WEEK FROM '2023-10-31'::DATE) + 1 as week_of_month,
        MAX(purchase_date) AS purchase_date,
        SUM(amount_spend) AS total_amount
    FROM
        Purchases
    WHERE
        EXTRACT('DOW' FROM purchase_date) = 5
    GROUP BY
        1
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:
        df = purchases.copy()
        df["dow"] = df["purchase_date"].dt.dayofweek
        df = df[df["dow"] == 4]
        df["week_of_month"] = (df["purchase_date"].dt.day - 1) // 7 + 1
        df = df.groupby(["week_of_month", "purchase_date"])["amount_spend"].sum().reset_index(name="total_amount")
        return df

    return


if __name__ == "__main__":
    app.run()
