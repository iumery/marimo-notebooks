import marimo

__generated_with = "0.14.16"
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
            "/notebooks/SQL_20250815.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250817.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" """)
    return


@app.cell
def _():
    """
    WITH user_trial AS (
        SELECT DISTINCT user_id FROM UserActivity WHERE activity_type = 'free_trial'
    ),
    user_paid AS (
        SELECT DISTINCT user_id FROM UserActivity WHERE activity_type = 'paid'
    )
    SELECT
        user_id,
        ROUND(AVG(activity_duration) FILTER (WHERE activity_type='free_trial'),2) AS trial_avg_duration,
        ROUND(AVG(activity_duration) FILTER (WHERE activity_type='paid'),2) AS paid_avg_duration
    FROM
        UserActivity
    WHERE
        user_id in (SELECT user_id FROM user_trial INNER JOIN user_paid USING(user_id))
    GROUP BY
        user_id
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def analyze_subscription_conversion(
        user_activity: pd.DataFrame,
    ) -> pd.DataFrame:
        def find_mean(activity: str, name: str) -> pd.DataFrame:
            return (
                user_activity[user_activity["activity_type"] == activity]
                .groupby("user_id")
                .mean("activity_duration")
                .apply(lambda x: round(x, 2))
                .reset_index()
                .rename(columns={"activity_duration": name})
            )

        return pd.merge(
            find_mean("free_trial", "trial_avg_duration"),
            find_mean("paid", "paid_avg_duration"),
            on="user_id",
        )
    return


if __name__ == "__main__":
    app.run()
