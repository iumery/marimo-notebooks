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
            "/notebooks/SQL_20250924.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250926.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2720

    Table: Friends

    | Column Name | Type |
    |-------------|------|
    | user1       | int  |
    | user2       | int  |

    (user1, user2) is the primary key (combination of unique values) of this table. Each row contains information about friendship where user1 and user2 are friends.

    Write a solution to find the popularity percentage for each user on Meta/Facebook. The popularity percentage is defined as the total number of friends the user has divided by the total number of users on the platform, then converted into a percentage by multiplying by 100, rounded to 2 decimal places.

    Return the result table ordered by user1 in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH all_pairs AS (
        SELECT
            user1,
            user2
        FROM
            Friends
        UNION
        SELECT
            user2 AS user1,
            user1 AS user2
        FROM
            Friends
    )
    SELECT
        user1,
        ROUND(COUNT(user2) * 100.0 / (SELECT COUNT(DISTINCT user1) FROM all_pairs), 2) AS percentage_popularity
    FROM
        all_pairs
    GROUP BY
        1
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def popularity_percentage(friends: pd.DataFrame) -> pd.DataFrame:
        friends_reverse = friends[["user2", "user1"]].rename(columns={"user1": "user2", "user2": "user1"})
        df = pd.concat([friends, friends_reverse]).drop_duplicates()
        total_user = len(df["user1"].drop_duplicates())
        df = df.groupby("user1", as_index=False).agg(percentage_popularity=("user2", "count"))
        df["percentage_popularity"] = (100.0 * df["percentage_popularity"] / total_user).round(2)
        return df

    return


if __name__ == "__main__":
    app.run()
