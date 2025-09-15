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
            "/notebooks/SQL_20250826.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250828.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 262

    Table: Trips

    | Column Name | Type     |
    |-------------|----------|
    | id          | int      |
    | client_id   | int      |
    | driver_id   | int      |
    | city_id     | int      |
    | status      | enum     |
    | request_at  | varchar  |

    id is the primary key (column with unique values) for this table. The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table. Status is an ENUM (category) type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').

    Table: Users

    | Column Name | Type     |
    |-------------|----------|
    | users_id    | int      |
    | banned      | enum     |
    | role        | enum     |

    users_id is the primary key (column with unique values) for this table. The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner'). banned is an ENUM (category) type of ('Yes', 'No'). The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

    Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03" with at least one trip. Round Cancellation Rate to two decimal points.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        request_at AS "Day",
        ROUND(AVG(CASE WHEN status = 'completed' THEN 0.0 ELSE 1.0 END) , 2) AS "Cancellation Rate"
    FROM
        Trips
    WHERE
        client_id IN (SELECT users_id FROM Users WHERE banned = 'No')
            AND driver_id IN (SELECT users_id FROM Users WHERE banned = 'No')
            AND request_at >= '2013-10-01'
            AND request_at <= '2013-10-03'
    GROUP BY
        1
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
        unbanned_users = users[users["banned"] == "No"]
        df = trips[
            (trips["request_at"] >= "2013-10-01")
            & (trips["request_at"] <= "2013-10-03")
            & (trips["client_id"].isin(unbanned_users["users_id"]))
            & (trips["driver_id"].isin(unbanned_users["users_id"]))
        ]
        df = (
            df.groupby("request_at")
            .agg(
                cancellation_rate=(
                    "status",
                    lambda x: round((x != "completed").mean(), 2),
                )
            )
            .reset_index()
        )
        df.rename(
            columns={
                "request_at": "Day",
                "cancellation_rate": "Cancellation Rate",
            },
            inplace=True,
        )
        return df

    return


if __name__ == "__main__":
    app.run()
