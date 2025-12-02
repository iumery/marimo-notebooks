import marimo

__generated_with = "0.18.1"
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
            "/notebooks/SQL_20251126.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251203.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3188

    Table: students

    | Column Name | Type     |
    |-------------|----------|
    | student_id  | int      |
    | name        | varchar  |
    | major       | varchar  |

    student_id is the primary key for this table. Each row contains the student ID, student name, and their major.

    Table: courses

    | Column Name | Type              |
    |-------------|-------------------|
    | course_id   | int               |
    | name        | varchar           |
    | credits     | int               |
    | major       | varchar           |
    | mandatory   | enum              |

    course_id is the primary key for this table. mandatory is an enum type of ('Yes', 'No'). Each row contains the course ID, course name, credits, major it belongs to, and whether the course is mandatory.

    Table: enrollments

    | Column Name | Type     |
    |-------------|----------|
    | student_id  | int      |
    | course_id   | int      |
    | semester    | varchar  |
    | grade       | varchar  |
    | GPA         | decimal  |

    (student_id, course_id, semester) is the primary key (combination of columns with unique values) for this table. Each row contains the student ID, course ID, semester, and grade received.

    Write a solution to find the students who meet the following criteria:

    - Have taken all mandatory courses and at least two elective courses offered in their major.
    - Achieved a grade of A in all mandatory courses and at least B in elective courses.
    - Maintained an average GPA of at least 2.5 across all their courses (including those outside their major).

    Return the result table ordered by student_id in ascending order.
    """)
    return


@app.cell
def _():
    """
    WITH major_mandatory AS (
        SELECT
            major,
            mandatory,
            COUNT(*) as total
        FROM
            courses
        GROUP BY
            1, 2
    )
    SELECT
        student_id
    FROM
        enrollments e
            JOIN courses c USING (course_id)
            JOIN students s USING (student_id)
            LEFT JOIN major_mandatory mm ON s.major = mm.major
    WHERE
        mm.mandatory = 'Yes'
    GROUP BY
        1
    HAVING
        MAX(total) = SUM(CASE WHEN s.major = c.major AND c.mandatory = 'Yes' AND grade = 'A' THEN 1 ELSE 0 END)
            AND SUM(CASE WHEN s.major = c.major AND c.mandatory = 'No' AND grade IN ('A', 'B') THEN 1 ELSE 0 END) >= 2
            AND AVG(GPA) >= 2.5
    ORDER BY
        1
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_top_scoring_students(
        students: pd.DataFrame, courses: pd.DataFrame, enrollments: pd.DataFrame
    ) -> pd.DataFrame:
        df_major_mandatory = (
            courses.groupby(["major", "mandatory"])["course_id"]
            .count()
            .reset_index(name="total")
        )
        df = pd.merge(enrollments, courses, on="course_id", suffixes=("_e", "_c"))
        df = pd.merge(df, students, on="student_id", suffixes=("_e", "_s"))
        df = pd.merge(
            df,
            df_major_mandatory,
            left_on="major_s",
            right_on="major",
            how="left",
            suffixes=("_e", "_m"),
        )
        df = df[df["mandatory_m"] == "Yes"]
        df = (
            df.groupby("student_id")
            .apply(
                lambda g: (
                    g["total"].max()
                    == g[
                        (g["major_s"] == g["major_e"])
                        & (g["mandatory_e"] == "Yes")
                        & (g["grade"] == "A")
                    ].count()
                )
                & (
                    g[
                        (g["major_s"] == g["major_e"])
                        & (g["mandatory_e"] == "No")
                        & ((g["grade"] == "A") | (g["grade"] == "B"))
                    ].count()
                    >= 2
                )
                & (g["GPA"].mean() >= 2.5),
                include_groups=False,
            )
            .reset_index()
        )
        df = df[df["course_id"] == True][["student_id"]].sort_values("student_id")
        return df
    return


if __name__ == "__main__":
    app.run()
