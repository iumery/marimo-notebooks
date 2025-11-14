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
            "/notebooks/SQL_20251114.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251118.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3124

    Table: Contacts

    | Column Name | Type    |
    |-------------|---------|
    | id          | int     |
    | first_name  | varchar |
    | last_name   | varchar |

    id is the primary key (column with unique values) of this table. id is a foreign key (reference column) to Calls table. Each row of this table contains id, first_name, and last_name.

    Table: Calls

    | Column Name | Type |
    |-------------|------|
    | contact_id  | int  |
    | type        | enum |
    | duration    | int  |

    (contact_id, type, duration) is the primary key (column with unique values) of this table. type is an ENUM (category) type of ('incoming', 'outgoing'). Each row of this table contains information about calls, comprising of contact_id, type, and duration in seconds.

    Write a solution to find the three longest incoming and outgoing calls.

    Return the result table ordered by type, duration, and first_name in descending order and duration must be formatted as HH:MM:SS.
    """)
    return


@app.cell
def _():
    """
    WITH rank_info AS (
        SELECT
            first_name,
            type,
            TO_CHAR((duration || ' seconds')::INTERVAL, 'HH24:MI:SS') AS duration_formatted,
            ROW_NUMBER() OVER (PARTITION BY type ORDER BY duration DESC) AS rnk
        FROM
            Calls ca
                JOIN Contacts co ON ca.contact_id = co.id
    )
    SELECT
        first_name,
        type,
        duration_formatted
    FROM
        rank_info
    WHERE
        rnk <= 3
    ORDER BY
        2 DESC, 3 DESC, 1 DESC;
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_longest_calls(
        contacts: pd.DataFrame, calls: pd.DataFrame
    ) -> pd.DataFrame:
        df = pd.merge(
            calls, contacts, how="left", left_on="contact_id", right_on="id"
        )
        df["duration"] = pd.to_datetime(df["duration"], unit="s")
        df["duration_formatted"] = df["duration"].dt.strftime("%H:%M:%S")
        incoming_df = (
            df[df["type"] == "incoming"]
            .sort_values(
                by=["duration_formatted", "first_name"], ascending=[False, False]
            )
            .head(3)
        )
        outgoing_df = (
            df[df["type"] == "outgoing"]
            .sort_values(
                by=["duration_formatted", "first_name"], ascending=[False, False]
            )
            .head(3)
        )
        df = pd.concat(
            [
                outgoing_df[["first_name", "type", "duration_formatted"]],
                incoming_df[["first_name", "type", "duration_formatted"]],
            ]
        )
        return df
    return


if __name__ == "__main__":
    app.run()
