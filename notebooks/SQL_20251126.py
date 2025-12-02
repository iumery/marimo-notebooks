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
            "/notebooks/SQL_20251125.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251202.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3182

    Table: students

    | Column Name | Type     |
    |-------------|----------|
    | student_id  | int      |
    | name        | varchar  |
    | major       | varchar  |

    student_id is the primary key (combination of columns with unique values) for this table. Each row of this table contains the student ID, student name, and their major.

    Table: courses

    | Column Name | Type     |
    |-------------|----------|
    | course_id   | int      |
    | name        | varchar  |
    | credits     | int      |
    | major       | varchar  |

    course_id is the primary key (combination of columns with unique values) for this table. Each row of this table contains the course ID, course name, the number of credits for the course, and the major it belongs to.

    Table: enrollments

    | Column Name | Type     |
    |-------------|----------|
    | student_id  | int      |
    | course_id   | int      |
    | semester    | varchar  |
    | grade       | varchar  |

    (student_id, course_id, semester) is the primary key (combination of columns with unique values) for this table. Each row of this table contains the student ID, course ID, semester, and grade received.

    Write a solution to find the students who have taken all courses offered in their major and have achieved a grade of A in all these courses.

    Return the result table ordered by student_id in ascending order.
    """)
    return


@app.cell
def _():
    """
    SELECT
        student_id
    FROM (
        SELECT
            s.student_id,
            COUNT(c.course_id) AS num_course,
            COUNT(grade) FILTER (WHERE grade = 'A') AS num_a
        FROM
            students s
                LEFT JOIN courses c USING (major)
                LEFT JOIN enrollments e ON s.student_id = e.student_id AND c.course_id = e.course_id
        GROUP BY
            1
    )
    WHERE
        num_course = num_a
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def find_top_scoring_students(enrollments: pd.DataFrame, students: pd.DataFrame, courses: pd.DataFrame) -> pd.DataFrame:
        df = pd.merge(students[["student_id", "major"]], courses[["course_id", "major"]], how="left", on="major")
        df = pd.merge(df, enrollments[["student_id", "course_id", "grade"]], how="left", on=["student_id", "course_id"])
        df = df.groupby("student_id", as_index=False).agg(
            num_course=("course_id", "count"),
            num_A=("grade", lambda x: sum(x=="A"))
        )
        df = df[df["num_course"] == df["num_A"]][["student_id"]].sort_values("student_id")
        return df
    return


if __name__ == "__main__":
    app.run()
