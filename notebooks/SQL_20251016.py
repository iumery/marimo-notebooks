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
            "/notebooks/SQL_20251015.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251017.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2988

    Table: Employees

    | Column Name | Type    |
    |-------------|---------|
    | emp_id      | int     |
    | emp_name    | varchar |
    | dep_id      | int     |
    | position    | varchar |

    emp_id is column of unique values for this table. This table contains emp_id, emp_name, dep_id, and position.

    Write a solution to find the name of the manager from the largest department. There may be multiple largest departments when the number of employees in those departments is the same.

    Return the result table sorted by dep_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        emp_name AS manager_name,
        dep_id
    FROM
        Employees
    WHERE
        position = 'Manager'
            AND dep_id IN (
                SELECT
                    dep_id
                FROM
                    Employees
                GROUP BY
                    1
                HAVING
                    COUNT(*) = (SELECT COUNT(*) FROM Employees GROUP BY dep_id ORDER BY 1 DESC LIMIT 1)
            )
    ORDER BY
        2;
    """
    return


@app.cell
def _():
    import pandas as pd

    def find_manager(employees: pd.DataFrame) -> pd.DataFrame:
        df = employees.copy()
        df["cnt"] = df.groupby("dep_id")["emp_id"].transform("count")
        df["rnk"] = df["cnt"].rank(method="min", ascending=False)
        df = (
            df[(df["rnk"] == 1) & (df["position"] == "Manager")][["emp_name", "dep_id"]]
            .rename(columns={"emp_name": "manager_name"})
            .sort_values("dep_id", ascending=True)
        )
        return df

    return


if __name__ == "__main__":
    app.run()
