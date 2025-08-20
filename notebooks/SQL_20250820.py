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
            "/notebooks/SQL_20250819.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250821.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 185

    Table: Employee

    | Column Name  | Type    |
    |--------------|---------|
    | id           | int     |
    | name         | varchar |
    | salary       | int     |
    | departmentId | int     |

    id is the primary key (column with unique values) for this table. departmentId is a foreign key (reference column) of the ID from the Department table. Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 
    Table: Department

    | Column Name | Type    |
    |-------------|---------|
    | id          | int     |
    | name        | varchar |

    id is the primary key (column with unique values) for this table. Each row of this table indicates the ID of a department and its name.

    A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

    Write a solution to find the employees who are high earners in each of the departments.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    WITH salary_rank AS (
        SELECT
            d.name AS Department,
            e.name AS Employee,
            e.salary AS Salary,
            DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank
        FROM
            Employee e
                JOIN Department d ON e.departmentId = d.id
    )
    SELECT
        Department,
        Employee,
        Salary
    FROM
        salary_rank
    WHERE
        salary_rank <= 3;
    """
    return


@app.cell
def _():
    import pandas as pd


    def top_three_salaries(
        employee: pd.DataFrame, department: pd.DataFrame
    ) -> pd.DataFrame:
        salary_rank = (
            employee[["name", "salary", "departmentId"]]
            .rename(
                columns={
                    "name": "Employee",
                    "salary": "Salary",
                    "departmentId": "id",
                }
            )
            .copy()
        )
        salary_rank["rank"] = salary_rank.groupby("id")["Salary"].rank(
            method="dense", ascending=False
        )
        salary_rank = salary_rank[salary_rank["rank"] <= 3]
        return pd.merge(salary_rank, department, on="id").rename(
            columns={"name": "Department"}
        )[["Department", "Employee", "Salary"]]
    return


if __name__ == "__main__":
    app.run()
