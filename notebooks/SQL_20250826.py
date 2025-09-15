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
            "/notebooks/SQL_20250825.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250827.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 1934

    Table: Signups

    | Column Name    | Type     |
    |----------------|----------|
    | user_id        | int      |
    | time_stamp     | datetime |

    user_id is the column of unique values for this table. Each row contains information about the signup time for the user with ID user_id.

    Table: Confirmations

    | Column Name    | Type     |
    |----------------|----------|
    | user_id        | int      |
    | time_stamp     | datetime |
    | action         | ENUM     |

    (user_id, time_stamp) is the primary key (combination of columns with unique values) for this table. user_id is a foreign key (reference column) to the Signups table. action is an ENUM (category) of the type ('confirmed', 'timeout'). Each row of this table indicates that the user with ID user_id requested a confirmation message at time_stamp and that confirmation message was either confirmed ('confirmed') or expired without confirming ('timeout').

    The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.

    Write a solution to find the confirmation rate of each user.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        user_id,
        ROUND(COALESCE((COUNT(*) FILTER (WHERE action = 'confirmed')) * 1.0 / COUNT(*), 0), 2) AS confirmation_rate
    FROM
        Signups
            LEFT JOIN Confirmations USING(user_id)
    GROUP BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
        confirmation_rates = (
            confirmations.groupby("user_id")
            .agg(
                confirmation_rate=(
                    "action",
                    lambda x: round((x == "confirmed").mean(), 2),
                )
            )
            .reset_index()
        )
        df = pd.merge(signups, confirmation_rates, on="user_id", how="left")[["user_id", "confirmation_rate"]].fillna(0)
        return df

    return


if __name__ == "__main__":
    app.run()
