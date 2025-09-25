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
            "/notebooks/SQL_20250922.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250924.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2394

    Table: Employees

    | Column Name  | Type |
    |--------------|------|
    | employee_id  | int  |
    | needed_hours | int  |

    employee_id is column with unique values for this table. Each row contains the id of an employee and the minimum number of hours needed for them to work to get their salary.

    Table: Logs

    | Column Name | Type     |
    |-------------|----------|
    | employee_id | int      |
    | in_time     | datetime |
    | out_time    | datetime |

    (employee_id, in_time, out_time) is the primary key (combination of columns with unique values) for this table. Each row of this table shows the time stamps for an employee. in_time is the time the employee started to work, and out_time is the time the employee ended work. All the times are in October 2022. out_time can be one day after in_time which means the employee worked after the midnight.

    In a company, each employee must work a certain number of hours every month. Employees work in sessions. The number of hours an employee worked can be calculated from the sum of the number of minutes the employee worked in all of their sessions. The number of minutes in each session is rounded up.

    For example, if the employee worked for 51 minutes and 2 seconds in a session, we consider it 52 minutes.

    Write a solution to report the IDs of the employees that will be deducted. In other words, report the IDs of the employees that did not work the needed hours.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    WITH hour_agg AS (
        SELECT
            employee_id,
            SUM(CEIL((EXTRACT(EPOCH FROM out_time) - EXTRACT(EPOCH FROM in_time))/60)/60) AS total_hour
        FROM
            Logs
        GROUP BY
            1
    )
    SELECT
        employee_id
    FROM
        Employees
            LEFT JOIN hour_agg USING (employee_id)
    WHERE
        total_hour IS NULL
            OR total_hour < needed_hours;
    """
    return


@app.cell
def _():
    import pandas as pd


    def employees_with_deductions(
        employees: pd.DataFrame, logs: pd.DataFrame
    ) -> pd.DataFrame:
        logs["session_hour"] = (
            -(-(logs["out_time"] - logs["in_time"]).dt.total_seconds() / 60 // 1)
        ) / 60
        df = pd.merge(
            employees,
            logs.groupby("employee_id", as_index=False)["session_hour"].sum(),
            how="left",
            on="employee_id",
        )
        return df[
            (df["session_hour"].isna()) | (df["session_hour"] < df["needed_hours"])
        ][["employee_id"]]
    return


if __name__ == "__main__":
    app.run()
