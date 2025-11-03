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
            "/notebooks/SQL_20251104.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251106.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3058

    Table: Friends

    | Column Name | Type |
    |-------------|------|
    | user_id1    | int  |
    | user_id2    | int  |

    (user_id1, user_id2) is the primary key (combination of columns with unique values) for this table. Each row contains user id1, user id2, both of whom are friends with each other.

    Write a solution to find all pairs of users who are friends with each other and have no mutual friends.

    Return the result table ordered by user_id1, user_id2 in ascending order.
    """)
    return


@app.cell
def _():
    """
    WITH all_pair AS (
        SELECT
            user_id1,
            user_id2
        FROM
            Friends
        UNION
        SELECT
            user_id2,
            user_id1
        FROM
            Friends
    )
    (SELECT
        user_id1,
        user_id2
    FROM
        Friends
    EXCEPT
    SELECT
        ap1.user_id1 AS user_id1,
        ap2.user_id1 AS user_id2
    FROM
        all_pair ap1
            JOIN all_pair ap2 ON ap1.user_id2 = ap2.user_id2
    WHERE
        (ap1.user_id1, ap2.user_id1) IN (SELECT * FROM Friends)
    )
    ORDER BY user_id1, user_id2
    """
    return


@app.cell
def _():
    import pandas as pd


    def friends_with_no_mutual_friends(friends: pd.DataFrame) -> pd.DataFrame:
        buddies = pd.concat(
            [
                friends,
                friends.rename(
                    columns={"user_id2": "user_id1", "user_id1": "user_id2"}
                ),
            ]
        )
        df = friends.merge(buddies, how="outer", on="user_id1").merge(
            buddies, how="outer", left_on="user_id2_x", right_on="user_id2"
        )
        df = df[df.user_id2_y == df.user_id1_y].iloc[:, [0, 1]]
        df = friends.merge(
            df,
            how="left",
            left_on=["user_id1", "user_id2"],
            right_on=["user_id1_x", "user_id2_x"],
        )
        df = df[df.user_id1_x.isna()].iloc[:, [0, 1]]
        df = df.sort_values(["user_id1", "user_id2"])
        return df
    return


if __name__ == "__main__":
    app.run()
