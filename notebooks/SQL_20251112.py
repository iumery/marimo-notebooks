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
            "/notebooks/SQL_20251111.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251113.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3089

    Table: Posts

    | Column Name | Type    |
    |-------------|---------|
    | post_id     | int     |
    | user_id     | int     |
    | post_date   | date    |

    post_id is the primary key (column with unique values) for this table. Each row of this table contains post_id, user_id, and post_date.

    Write a solution to find users who demonstrate bursty behavior in their posting patterns during February 2024. Bursty behavior is defined as any period of 7 consecutive days where a user's posting frequency is at least twice to their average weekly posting frequency for February 2024.

    Note: Only include the dates from February 1 to February 28 in your analysis, which means you should count February as having exactly 4 weeks.

    Return the result table orderd by user_id in ascending order.
    """)
    return


@app.cell
def _():
    """
    WITH feb_post AS (
        SELECT
            *,
            COUNT(*) OVER (PARTITION BY user_id) * 1.0 / 4 AS avg_weekly_posts
        FROM
            Posts
        WHERE
            post_date BETWEEN '2024-02-01' AND '2024-02-28'
    ),
    week_post AS (
        SELECT
            *,
            COUNT(post_id) OVER (PARTITION BY user_id ORDER BY post_date RANGE BETWEEN INTERVAL '6 day' PRECEDING AND CURRENT ROW) AS max_7day_posts
        FROM
            feb_post
    )
    SELECT
        user_id,
        MAX(max_7day_posts) AS max_7day_posts,
        MAX(avg_weekly_posts) AS avg_weekly_posts
    FROM
        week_post
    GROUP BY
        1
    HAVING
        MAX(max_7day_posts ) >= 2 * MAX(avg_weekly_posts)
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_bursty_behavior(posts: pd.DataFrame) -> pd.DataFrame:
        df = posts[
            (posts["post_date"].dt.year == 2024)
            & (posts["post_date"].dt.month == 2)
            & (posts["post_date"].dt.day <= 28)
        ]
        df = df.set_index("post_date").sort_index()
        max_weekly = (
            df.groupby("user_id")["post_id"]
            .rolling("7D")
            .count()
            .reset_index()
            .rename(columns={"post_id": "weekly_posts"})
        )
        max_weekly["max_7day_posts"] = max_weekly.groupby("user_id")[
            "weekly_posts"
        ].transform("max")
        avg_weekly = (
            df.groupby("user_id")["post_id"]
            .count()
            .reset_index()
            .rename(columns={"post_id": "avg_weekly_posts"})
        )
        avg_weekly["avg_weekly_posts"] = avg_weekly["avg_weekly_posts"] / 4
        df = pd.merge(max_weekly, avg_weekly, on="user_id")
        df = df[df["max_7day_posts"] >= df["avg_weekly_posts"] * 2][
            ["user_id", "max_7day_posts", "avg_weekly_posts"]
        ].drop_duplicates()
        return df
    return


if __name__ == "__main__":
    app.run()
