import marimo

__generated_with = "0.16.5"
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
            "/notebooks/SQL_20251103.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251105.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3057

    Table: Project

    | Column Name | Type    |
    |-------------|---------|
    | project_id  | int     |
    | employee_id | int     |
    | workload    | int     |

    employee_id is the primary key (column with unique values) of this table. employee_id is a foreign key (reference column) to Employee table. Each row of this table indicates that the employee with employee_id is working on the project with project_id and the workload of the project.

    Table: Employees

    | Column Name      | Type    |
    |------------------|---------|
    | employee_id      | int     |
    | name             | varchar |
    | team             | varchar |

    employee_id is the primary key (column with unique values) of this table. Each row of this table contains information about one employee.

    Write a solution to find the employees who are allocated to projects with a workload that exceeds the average workload of all employees for their respective teams

    Return the result table ordered by employee_id, project_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH team_avg AS (
        SELECT
            team,
            AVG(workload) AS avg_workload
        FROM
            Project
                JOIN Employees USING (employee_id)
        GROUP BY
            1
    )
    SELECT
        employee_id,
        project_id,
        name AS employee_name,
        workload AS project_workload
    FROM
        Project
            JOIN Employees USING (employee_id)
            JOIN team_avg USING (team)
    WHERE
        workload > avg_workload
    ORDER BY
        1, 2;
    """
    return


@app.cell
def _():
    import pandas as pd


    def employees_with_above_avg_workload(
        project: pd.DataFrame, employees: pd.DataFrame
    ) -> pd.DataFrame:
        df = pd.merge(project, employees, on="employee_id")
        df["mean"] = df.groupby("team")["workload"].transform("mean")
        df = df.query("workload > mean")[
            ["employee_id", "project_id", "name", "workload"]
        ].rename(columns={"name": "employee_name", "workload": "project_workload"})
        df.sort_values(["employee_id", "project_id"], inplace=True)

        return df
    return


if __name__ == "__main__":
    app.run()
