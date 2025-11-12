import marimo

__generated_with = "0.17.4"
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
            "/notebooks/SQL_20251113.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251117.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3118

    Table: Purchases

    | Column Name   | Type |
    |---------------|------|
    | user_id       | int  |
    | purchase_date | date |
    | amount_spend  | int  |

    (user_id, purchase_date, amount_spend) is the primary key (combination of columns with unique values) for this table. purchase_date will range from November 1, 2023, to November 30, 2023, inclusive of both dates. Each row contains user_id, purchase_date, and amount_spend.

    Table: Users

    | Column Name | Type |
    |-------------|------|
    | user_id     | int  |
    | membership  | enum |

    user_id is the primary key for this table. membership is an ENUM (category) type of ('Standard', 'Premium', 'VIP'). Each row of this table indicates the user_id, membership type.

    Write a solution to calculate the total spending by Premium and VIP members on each Friday of every week in November 2023.  If there are no purchases on a particular Friday by Premium or VIP members, it should be considered as 0.

    Return the result table ordered by week of the month,  and membership in ascending order.
    """)
    return


@app.cell
def _():
    """
    WITH cte1(week_of_month) AS (
       VALUES (1),(2),(3),(4)
    ),
    cte2(membership) AS (
       VALUES ('VIP'), ('Premium')
    )
    SELECT
        week_of_month,
        c2.membership,
        SUM(CASE WHEN EXTRACT(DOW FROM purchase_date) = 5 THEN amount_spend ELSE 0 END) AS total_amount
    FROM
        (cte1 c1 CROSS JOIN cte2 c2)
            LEFT JOIN (Purchases p JOIN Users u USING (user_id)) ON week_of_month = EXTRACT(DAY FROM purchase_date)::INT/7+1 AND c2.membership = u.membership
    GROUP BY
        1, 2
    ORDER BY
        1, 2;
    """
    return


@app.cell
def _():
    import pandas as pd


    def friday_purchases(
        purchases: pd.DataFrame, users: pd.DataFrame
    ) -> pd.DataFrame:
        df = pd.merge(users, purchases, on="user_id")
        df["week_of_month"] = df.purchase_date.dt.day.agg(lambda x: x // 7 + 1)
        df = (
            df[
                (df["purchase_date"].dt.weekday == 4)
                & (df["membership"].isin(["Premium", "VIP"]))
            ]
            .groupby(["week_of_month", "membership"])["amount_spend"]
            .sum()
            .reset_index(name="total_amount")
        )
        df = (
            pd.DataFrame(
                {
                    "membership": ["Premium", "VIP"] * 4,
                    "week_of_month": [1, 1, 2, 2, 3, 3, 4, 4],
                }
            )
            .merge(df, on=["week_of_month", "membership"], how="left")
            .fillna(0)
            .iloc[:, [1, 0, 2]]
        )
        return df
    return


if __name__ == "__main__":
    app.run()
