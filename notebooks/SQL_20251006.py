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
            "/notebooks/SQL_20251003.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251007.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2854

    Table: Steps
 
    | Column Name | Type | 
    |-------------|------| 
    | user_id     | int  | 
    | steps_count | int  |
    | steps_date  | date |

    (user_id, steps_date) is the primary key for this table. Each row of this table contains user_id, steps_count, and steps_date.

    Write a solution to calculate 3-day rolling averages of steps for each user.

    We calculate the n-day rolling average this way: For each day, we calculate the average of n consecutive days of step counts ending on that day if available, otherwise, n-day rolling average is not defined for it.

    Output the user_id, steps_date, and rolling average. Round the rolling average to two decimal places.

    Return the result table ordered by user_id, steps_date in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH full_rolling_info AS (
        SELECT
            user_id,
            steps_date,
            ROUND(AVG(steps_count) OVER (PARTITION BY user_id ORDER BY steps_date RANGE BETWEEN INTERVAL '2 days' PRECEDING AND CURRENT ROW), 2) AS rolling_average,
            COUNT(1) OVER (PARTITION BY user_id ORDER BY steps_date RANGE BETWEEN INTERVAL '2 days' PRECEDING AND CURRENT ROW) AS rolling_count
        FROM
            Steps
    )
    SELECT
        user_id,
        steps_date,
        rolling_average
    FROM
        full_rolling_info
    WHERE
        rolling_count = 3
    ORDER BY
        1, 2;
    """
    return


@app.cell
def _():
    import pandas as pd


    def rolling_average(steps: pd.DataFrame) -> pd.DataFrame:
        df = steps.sort_values(["user_id", "steps_date"]).set_index("steps_date")

        df["rolling_average"] = (
            df.groupby("user_id")["steps_count"]
            .rolling("2D", closed="both")
            .mean()
            .round(2)
            .reset_index(level=0, drop=True)
        )
        df["rolling_count"] = (
            df.groupby("user_id")["steps_count"]
            .rolling("2D", closed="both")
            .count()
            .reset_index(level=0, drop=True)
        )
        df.reset_index(inplace=True)
        df = df[df["rolling_count"] == 3][
            ["user_id", "steps_date", "rolling_average"]
        ].sort_values(["user_id", "steps_date"])
        return df
    return


if __name__ == "__main__":
    app.run()
