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
            "/notebooks/SQL_20250818.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250820.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### DataLemur Server Utilization Time

    Amazon Web Services (AWS) is powered by fleets of servers. Senior management has requested data-driven solutions to optimize server usage.

    Write a query that calculates the total time that the fleet of servers was running. The output should be in units of full days.

    Assumptions:

    - Each server might start and stop several times.
    - The total time in which the server fleet is running can be calculated as the sum of each server's uptime.

    server_utilization Table:

    | Column Name | Type |
    |-------------|------|
    | server_id | integer |
    | status_time | timestamp |
    | session_status | string |

    """
    )
    return


@app.cell
def _():
    """
    SELECT
        SUM(
            CASE
                WHEN session_status = 'stop' THEN status_time::DATE - '2022-01-01'::DATE
                WHEN session_status = 'start' THEN '2022-01-01'::DATE - status_time::DATE
            END
        ) AS total_uptime_days
    FROM
        server_utilization
    """
    return


if __name__ == "__main__":
    app.run()
