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
            "/notebooks/SQL_20250806.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250808.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3611

    Table: employees

    | Column Name   | Type    |
    |---------------|---------|
    | employee_id   | int     |
    | employee_name | varchar |
    | department    | varchar |

    employee_id is the unique identifier for this table. Each row contains information about an employee and their department.

    Table: meetings

    | Column Name   | Type    |
    |---------------|---------|
    | meeting_id    | int     |
    | employee_id   | int     |
    | meeting_date  | date    |
    | meeting_type  | varchar |
    | duration_hours| decimal |

    meeting_id is the unique identifier for this table. Each row represents a meeting attended by an employee. meeting_type can be 'Team', 'Client', or 'Training'.

    Write a solution to find employees who are meeting-heavy - employees who spend more than 50% of their working time in meetings during any given week.

    - Assume a standard work week is 40 hours
    - Calculate total meeting hours per employee per week (Monday to Sunday)
    An employee is meeting-heavy if their weekly meeting hours > 20 hours (50% of 40 hours)
    - Count how many weeks each employee was meeting-heavy
    - Only include employees who were meeting-heavy for at least 2 weeks
    - Return the result table ordered by the number of meeting-heavy weeks in descending order, then by employee name in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH meeting_hours AS (
        SELECT
            employee_id,
            SUM(duration_hours) AS meeting_hrs
        FROM
            meetings
        GROUP BY
            employee_id,
            EXTRACT(WEEK FROM meeting_date),
            EXTRACT(YEAR FROM meeting_date)
    )
    SELECT
        employee_id,
        employee_name,
        department,
        COUNT(employee_id) AS meeting_heavy_weeks
    FROM
        employees
            JOIN meeting_hours USING(employee_id)
    WHERE
        meeting_hrs>20
    GROUP BY
        1,2,3
    HAVING
        COUNT(employee_id) > 1
    ORDER BY
        4 desc, 2;
    """
    return


@app.cell
def _():
    import pandas as pd

    def find_overbooked_employees(employees: pd.DataFrame, meetings: pd.DataFrame) -> pd.DataFrame:
        meetings["year"] = meetings.meeting_date.dt.year
        meetings["week"] = meetings.meeting_date.dt.isocalendar().week

        df = (
            meetings.groupby(["employee_id", "year", "week"])
            .sum("duration_hours")
            .reset_index()
            .rename(columns={"duration_hours": "meeting_heavy_weeks"})
        )

        df = df[df.meeting_heavy_weeks > 20.0].groupby(["employee_id"]).count().merge(employees, on="employee_id")

        return df[df.meeting_heavy_weeks > 1].sort_values(["meeting_heavy_weeks", "employee_name"], ascending=[False, True]).iloc[:, [0, 5, 6, 4]]

    return


if __name__ == "__main__":
    app.run()
