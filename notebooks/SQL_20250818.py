import marimo

__generated_with = "0.14.16"
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
            "/notebooks/SQL_20250817.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250819.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3482

    Table: Employees

    | Column Name    | Type    | 
    |----------------|---------|
    | employee_id    | int     |
    | employee_name  | varchar |
    | manager_id     | int     |
    | salary         | int     |
    | department     | varchar |

    employee_id is the unique key for this table. Each row contains information about an employee, including their ID, name, their manager's ID, salary, and department. manager_id is null for the top-level manager (CEO).

    Write a solution to analyze the organizational hierarchy and answer the following:

    - Hierarchy Levels: For each employee, determine their level in the organization (CEO is level 1, employees reporting directly to the CEO are level 2, and so on).
    - Team Size: For each employee who is a manager, count the total number of employees under them (direct and indirect reports).
    - Salary Budget: For each manager, calculate the total salary budget they control (sum of salaries of all employees under them, including indirect reports, plus their own salary).
    - Return the result table ordered by the result ordered by level in ascending order, then by budget in descending order, and finally by employee_name in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH RECURSIVE leadership AS (
        SELECT
            manager_id,
            employee_id,
            employee_name,
            salary,
            1 AS level
        FROM
            employees
        WHERE
            manager_id IS NULL
        UNION
        SELECT
            e.manager_id,
            e.employee_id,
            e.employee_name,
            e.salary,
            l.level+1 AS level
        FROM
            employees e
                JOIN leadership l ON e.manager_id = l.employee_id
    ),
    subordinate AS (
        SELECT
            employee_id,
            salary,
            manager_id
        FROM
            employees
        UNION
        SELECT
            e.employee_id,
            e.salary,
            s.manager_id
        FROM
            employees e
                JOIN subordinate s ON s.employee_id = e.manager_id
    )
    SELECT
        l.employee_id,
        l.employee_name,
        level,
        COUNT(s.employee_id) AS team_size,
        COALESCE(SUM(s.salary), 0) + l.salary AS budget
    FROM
        leadership l
            LEFT JOIN subordinate s ON s.manager_id = l.employee_id
    GROUP BY
        1,2,3,
        l.salary
    ORDER BY
        3, 5 DESC, 2;
    """
    return


@app.cell
def _():
    import pandas as pd


    def build_leadership(employees: pd.DataFrame) -> pd.DataFrame:
        out = []
        frontier = employees[employees["manager_id"].isna()].copy()
        frontier["level"] = 1
        out.append(frontier)

        while not frontier.empty:
            nxt = employees.merge(
                frontier[["employee_id", "level"]],
                left_on="manager_id",
                right_on="employee_id",
                how="inner",
                suffixes=("", "_mgr"),
            )
            if nxt.empty:
                break
            nxt = nxt.drop(columns=["employee_id_mgr"])
            nxt["level"] = nxt["level"] + 1
            out.append(nxt)
            frontier = nxt

        return pd.concat(out, ignore_index=True)


    def build_subordinate(employees: pd.DataFrame) -> pd.DataFrame:
        base = employees[["employee_id", "salary", "manager_id"]].copy()
        results = [base]
        frontier = base[["employee_id", "manager_id"]].copy()

        while True:
            nxt = employees.merge(
                frontier.rename(
                    columns={"employee_id": "parent_emp", "manager_id": "root_mgr"}
                ),
                left_on="manager_id",
                right_on="parent_emp",
                how="inner",
            )
            if nxt.empty:
                break
            step = nxt[["employee_id", "salary"]].copy()
            step["manager_id"] = nxt["root_mgr"]
            results.append(step)
            frontier = step[["employee_id", "manager_id"]].copy()

        return pd.concat(results, ignore_index=True)


    def analyze_organization_hierarchy(employees: pd.DataFrame) -> pd.DataFrame:
        ldr = build_leadership(employees)
        sub = build_subordinate(employees)

        merged = ldr.merge(
            sub,
            left_on="employee_id",
            right_on="manager_id",
            how="left",
            suffixes=("", "_sub"),
        )

        out = merged.groupby(
            ["employee_id", "employee_name", "level", "salary"], as_index=False
        ).agg(
            team_size=("employee_id_sub", "count"),
            sum_sub=("salary_sub", "sum"),
        )
        out["budget"] = out["sum_sub"].fillna(0) + out["salary"]
        out = out.drop(columns=["sum_sub", "salary"]).sort_values(
            by=["level", "budget", "employee_name"], ascending=[True, False, True]
        )
        return out
    return


if __name__ == "__main__":
    app.run()
