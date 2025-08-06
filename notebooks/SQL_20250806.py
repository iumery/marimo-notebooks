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
            "/notebooks/SQL_20250805.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250807.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3617

    Table: students

    | Column Name  | Type    |
    |--------------|---------|
    | student_id   | int     |
    | student_name | varchar |
    | major        | varchar |

    student_id is the unique identifier for this table. Each row contains information about a student and their academic major.  

    Table: study_sessions

    | Column Name   | Type    |
    |---------------|---------|
    | session_id    | int     |
    | student_id    | int     |
    | subject       | varchar |
    | session_date  | date    |
    | hours_studied | decimal |

    session_id is the unique identifier for this table. Each row represents a study session by a student for a specific subject.

    Write a solution to find students who follow the Study Spiral Pattern - students who consistently study multiple subjects in a rotating cycle.

    - A Study Spiral Pattern means a student studies at least 3 different subjects in a repeating sequence
    - The pattern must repeat for at least 2 complete cycles (minimum 6 study sessions)
    - Sessions must be consecutive dates with no gaps longer than 2 days between sessions
    - Calculate the cycle length (number of different subjects in the pattern)
    - Calculate the total study hours across all sessions in the pattern
    - Only include students with cycle length of at least 3 subjects
    - Return the result table ordered by cycle length in descending order, then by total study hours in descending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH session_diff AS (
        SELECT
            session_id,
            student_id,
            subject,
            session_date,
            hours_studied,
            session_date - LAG(session_date) OVER (PARTITION BY student_id, subject ORDER BY session_id) AS subject_gap,
            session_date - LAG(session_date) OVER (PARTITION BY student_id ORDER BY session_id) AS date_gap
        FROM
            study_sessions
    ),
    spiral_check AS (
        SELECT
            student_id,
            COUNT(DISTINCT subject) AS cycle_length,
            COUNT(DISTINCT subject_gap) AS subject_gap_variants,
            (COUNT(date_gap) + 1) / COUNT(DISTINCT subject) AS cycle_repeats,
            SUM(CASE WHEN date_gap IN (1, 2) THEN 1 ELSE 0 END) AS consecutive_sessions,
            SUM(hours_studied) AS total_study_hours
        FROM
            session_diff
        GROUP BY
            student_id
    )
    SELECT
        student_id,
        student_name,
        major,
        cycle_length,
        total_study_hours
    FROM
        spiral_check
            JOIN students USING(student_id)
    WHERE
        cycle_repeats >= 2
        AND cycle_length >= 3
        AND consecutive_sessions + 1 >= cycle_repeats * cycle_length
    ORDER BY
        4 DESC,
        5 DESC;
    """
    return


if __name__ == "__main__":
    app.run()
