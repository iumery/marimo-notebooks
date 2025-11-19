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
            "/notebooks/SQL_20251120.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251124.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3156

    Table: Tasks

    | Column Name   | Type     |
    |---------------|----------|
    | task_id       | int      |
    | employee_id   | int      |
    | start_time    | datetime |
    | end_time      | datetime |

    (task_id, employee_id) is the primary key for this table. Each row in this table contains the task identifier, the employee identifier, and the start and end times of each task.

    Write a solution to find the total duration of tasks for each employee and the maximum number of concurrent tasks an employee handled at any point in time. The total duration should be rounded down to the nearest number of full hours.

    Return the result table ordered by employee_id ascending order.
    """)
    return


@app.cell
def _():
    """
    WITH task_time_info AS (
        SELECT
            t1.employee_id,
            SUM(
                CASE
                    WHEN t1.task_id = t2.task_id THEN EXTRACT(EPOCH FROM t1.end_time - t1.start_time)
                    ELSE EXTRACT(EPOCH FROM t2.start_time - t1.end_time)
                END
            ) AS task_sec,
            COUNT(*) AS concurrent_tasks,
            MAX(t1.start_time) AS grp_start_time,
            MAX(t2.end_time) AS grp_end_time
        FROM
            Tasks t1
                INNER JOIN Tasks t2 ON t1.employee_id = t2.employee_id
                    AND t1.start_time <= t2.start_time
                    AND t1.end_time > t2.start_time
        GROUP BY
            1, t1.task_id
    )
    SELECT
        employee_id,
        CASE
            WHEN FLOOR(SUM(task_sec) / 3600) = 0
                THEN FLOOR(EXTRACT(EPOCH FROM MAX(grp_end_time) - MIN(grp_start_time)) / 3600)
            ELSE FLOOR(SUM(task_sec) / 3600)
        END AS total_task_hours,
        MAX(concurrent_tasks) AS max_concurrent_tasks
    FROM
        task_time_info
    GROUP BY
        1
    ORDER BY
        1;
    """
    return


@app.cell
def _(datetime):
    import pandas as pd


    def find_total_duration(tasks: pd.DataFrame) -> pd.DataFrame:
        time_zero = tasks["start_time"].min() - datetime.timedelta(days=1)
        tasks["start_time"] = -(tasks.start_time - time_zero).dt.total_seconds()
        tasks["end_time"] = (tasks.end_time - time_zero).dt.total_seconds()

        df = (
            tasks.melt(
                id_vars=["employee_id"],
                value_vars=["start_time", "end_time"],
                value_name="total_task_hours",
            )
            .sort_values("variable")
            .sort_values(["employee_id", "total_task_hours"], key=lambda x: abs(x))
        )

        df["max_concurrent_tasks"] = (
            df["total_task_hours"]
            .apply(lambda x: -x // (abs(x)))
            .astype(int)
            .cumsum()
        )
        df_mx = df.groupby("employee_id", as_index=False)[
            "max_concurrent_tasks"
        ].max()
        df = df[
            ((df.variable == "start_time") & (df.max_concurrent_tasks == 1))
            | ((df.variable == "end_time") & (df.max_concurrent_tasks == 0))
        ]

        df = df.groupby("employee_id", as_index=False)["total_task_hours"].sum()
        df["total_task_hours"] //= 3600

        return df.merge(df_mx)
    return


if __name__ == "__main__":
    app.run()
