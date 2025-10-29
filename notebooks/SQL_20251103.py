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
            "/notebooks/SQL_20251031.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251104.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3056

    Table: Activities

    | Column Name   | Type    |
    |---------------|---------|
    | activity_id   | int     |
    | user_id       | int     |
    | activity_type | enum    |
    | time_spent    | decimal |

    activity_id is column of unique values for this table. activity_type is an ENUM (category) type of ('send', 'open'). This table contains activity id, user id, activity type and time spent.

    Table: Age

    | Column Name | Type |
    |-------------|------|
    | user_id     | int  |
    | age_bucket  | enum |

    user_id is the column of unique values for this table. age_bucket is an ENUM (category) type of ('21-25', '26-30', '31-35'). This table contains user id and age group.

    Write a solution to calculate the percentage of the total time spent on sending and opening snaps for each age group. Precentage should be rounded to 2 decimal places.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        age_bucket,
        COALESCE(ROUND(100.0 * (SUM(time_spent) FILTER (WHERE activity_type = 'send')) / (SUM(time_spent)), 2), 0) AS send_perc,
        COALESCE(ROUND(100.0 * (SUM(time_spent) FILTER (WHERE activity_type = 'open')) / (SUM(time_spent)), 2), 0) AS open_perc
    FROM
        Activities
            JOIN Age USING (user_id)
    GROUP BY
        1
    """
    return


@app.cell
def _():
    import pandas as pd

    def snap_analysis(activities: pd.DataFrame, age: pd.DataFrame) -> pd.DataFrame:
        df = pd.merge(activities, age, on="user_id")
        df = df.groupby("age_bucket", as_index=False).apply(
            lambda x: pd.Series(
                {
                    "send_perc": round(
                        100.0 * x[x["activity_type"] == "send"]["time_spent"].sum() / x["time_spent"].sum(),
                        2,
                    ),
                    "open_perc": round(
                        100.0 * x[x["activity_type"] == "open"]["time_spent"].sum() / x["time_spent"].sum(),
                        2,
                    ),
                }
            )
        )
        df.fillna(0, inplace=True)
        return df

    return


if __name__ == "__main__":
    app.run()
