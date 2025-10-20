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
            "/notebooks/SQL_20251021.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251023.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2994

    Table: Purchases

    | Column Name   | Type |
    |---------------|------|
    | user_id       | int  |
    | purchase_date | date |
    | amount_spend  | int  |

    (user_id, purchase_date, amount_spend) is the primary key (combination of columns with unique values) for this table. purchase_date will range from November 1, 2023, to November 30, 2023, inclusive of both dates. Each row contains user id, purchase date, and amount spend.

    Write a solution to calculate the total spending by users on each Friday of every week in November 2023. If there are no purchases on a particular Friday of a week, it will be considered as 0.

    Return the result table ordered by week of month in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        EXTRACT(WEEK FROM purchase_date) - EXTRACT(WEEK FROM '2023-10-31'::DATE) + 1 AS week_of_month,
        MAX(purchase_date)::DATE AS purchase_date,
        COALESCE(SUM(amount_spend),0) AS total_amount
    FROM
        Purchases
            RIGHT JOIN GENERATE_SERIES('2023-11-03'::DATE,'2023-11-30'::DATE, INTERVAL '7 days') AS g(purchase_date) USING (purchase_date)
    WHERE
        EXTRACT('DOW' FROM purchase_date) = 5
    GROUP BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd
    from datetime import datetime


    def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:
        dates = pd.DataFrame(
            {
                "purchase_date": pd.date_range(
                    start=datetime(2023, 11, 1),
                    end=datetime(2023, 11, 30),
                    freq="d",
                )
            }
        )
        dates["day_of_week"] = dates["purchase_date"].dt.dayofweek
        dates["week_of_year"] = dates["purchase_date"].dt.isocalendar().week
        dates["start_time"] = (
            dates["purchase_date"].dt.to_period("M").dt.start_time
        )
        dates["first_week"] = dates["start_time"].dt.isocalendar().week
        dates["week_of_month"] = dates["week_of_year"] - dates["first_week"] + 1
        df = purchases.groupby(by="purchase_date", as_index=False).agg(
            total_amount=("amount_spend", "sum")
        )
        df = pd.merge(
            dates.loc[
                dates["day_of_week"] == 4, ["week_of_month", "purchase_date"]
            ],
            df,
            how="left",
            on="purchase_date",
        ).fillna(0)
        df = df.sort_values(by="week_of_month", ascending=True)
        return df
    return


if __name__ == "__main__":
    app.run()
