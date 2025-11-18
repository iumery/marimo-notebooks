import marimo

__generated_with = "0.17.8"
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
            "/notebooks/SQL_20251118.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251120.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3140

    Table: Cinema

    | Column Name | Type |
    |-------------|------|
    | seat_id     | int  |
    | free        | bool |

    seat_id is an auto-increment column for this table. Each row of this table indicates whether the ith seat is free or not. 1 means free while 0 means occupied.

    Write a solution to find the length of longest consecutive sequence of available seats in the cinema.

    Note:

    There will always be at most one longest consecutive sequence.
    If there are multiple consecutive sequences with the same length, include all of them in the output.

    Return the result table ordered by first_seat_id in ascending order.
    """)
    return


@app.cell
def _():
    """
    WITH group_info AS (
        SELECT
            seat_id,
            free,
            seat_id - ROW_NUMBER() OVER (ORDER BY seat_id) AS grp
        FROM
            Cinema
        WHERE
            free = 1
    ),
    group_count AS (
        SELECT
            seat_id,
            grp,
            COUNT(grp) OVER (PARTITION BY grp)  AS streak
        FROM
             group_info
    )
    SELECT
        MIN(seat_id) AS first_seat_id,
        MAX(seat_id) AS last_seat_id,
        MAX(streak) AS consecutive_seats_len
    FROM
        group_count
    WHERE
        streak = (SELECT MAX(streak) FROM group_count)
    GROUP BY
        grp
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
        df = cinema.sort_values("seat_id")
        df["tag"] = df["seat_id"] - df.groupby("free")["free"].cumsum()
        df = (
            df[df["free"] == 1]
            .groupby("tag")
            .agg(
                first_seat_id=("seat_id", "min"),
                last_seat_id=("seat_id", "max"),
                consecutive_seats_len=("tag", "count"),
            )
        )
        return df[df["consecutive_seats_len"] == max(df["consecutive_seats_len"])]
    return


if __name__ == "__main__":
    app.run()
