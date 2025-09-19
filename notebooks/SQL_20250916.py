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
            "/notebooks/SQL_20250915.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250917.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2346

    Table: Students

    | Column Name   | Type |
    |---------------|------|
    | student_id    | int  |
    | department_id | int  |
    | mark          | int  |

    student_id contains unique values. Each row of this table indicates a student's ID, the ID of the department in which the student enrolled, and their mark in the exam.

    Write a solution to report the rank of each student in their department as a percentage, where the rank as a percentage is computed using the following formula: (student_rank_in_the_department - 1) * 100 / (the_number_of_students_in_the_department - 1). The percentage should be rounded to 2 decimal places. student_rank_in_the_department is determined by descending mark, such that the student with the highest mark is rank 1. If two students get the same mark, they also get the same rank.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    WITH rank_in_department AS (
        SELECT
            student_id,
            department_id,
            RANK() OVER (PARTITION BY department_id ORDER BY mark DESC) AS rank,
            COUNT(student_id) OVER (PARTITION BY department_id) AS count
        FROM
            students
    )
    SELECT
        student_id,
        department_id,
        ROUND((rank - 1) * 100.0 / GREATEST((count - 1), 1), 2) AS percentage
    FROM
        rank_in_department
    """
    return


@app.cell
def _():
    import pandas as pd

    def compute_rating(students: pd.DataFrame) -> pd.DataFrame:
        students["rank"] = students.groupby("department_id")["mark"].rank(method="min", ascending=False)
        students["num_students"] = students.groupby("department_id")["student_id"].transform("count")
        students["percentage"] = ((students["rank"] - 1) * 100) / (students["num_students"] - 1)
        students.loc[students["num_students"] == 1, "percentage"] = 0.00
        students["percentage"] = students["percentage"].round(2)
        return students[["student_id", "department_id", "percentage"]]

    return


if __name__ == "__main__":
    app.run()
