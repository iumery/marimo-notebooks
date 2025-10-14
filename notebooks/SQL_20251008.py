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
            "/notebooks/SQL_20251007.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251009.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2853

    Table: Salaries

    | Column Name | Type    | 
    |-------------|---------| 
    | emp_name    | varchar | 
    | department  | varchar | 
    | salary      | int     |

    (emp_name, department) is the primary key (combination of unique values) for this table. Each row of this table contains emp_name, department and salary. There will be at least one entry for the engineering and marketing departments.

    Write a solution to calculate the difference between the highest salaries in the marketing and engineering department. Output the absolute difference in salaries.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        ABS(MAX(salary) FILTER (WHERE department = 'Engineering') - MAX(salary) FILTER (WHERE department = 'Marketing')) AS salary_difference
    FROM
        Salaries
    """
    return


@app.cell
def _():
    import pandas as pd

    def salaries_difference(salaries: pd.DataFrame) -> pd.DataFrame:
        mkt_highest = salaries[salaries["department"] == "Marketing"]["salary"].max()
        eng_highest = salaries[salaries["department"] == "Engineering"]["salary"].max()
        diff = abs(mkt_highest - eng_highest)
        df = pd.DataFrame({"salary_difference": [diff]})
        return df

    return


if __name__ == "__main__":
    app.run()
