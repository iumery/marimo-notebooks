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
            "/notebooks/SQL_20251211.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251215.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3764

    Table: course_completions

    | Column Name       | Type    |
    |-------------------|---------|
    | user_id           | int     |
    | course_id         | int     |
    | course_name       | varchar |
    | completion_date   | date    |
    | course_rating     | int     |

    (user_id, course_id) is the combination of columns with unique values for this table. Each row represents a completed course by a user with their rating (1-5 scale).

    Write a solution to identify skill mastery pathways by analyzing course completion sequences among top-performing students:

    - Consider only top-performing students (those who completed at least 5 courses with an average rating of 4 or higher).
    - For each top performer, identify the sequence of courses they completed in chronological order.
    - Find all consecutive course pairs (Course A → Course B) taken by these students.
    - Return the pair frequency, identifying which course transitions are most common among high achievers.

    Return the result table ordered by pair frequency in descending order and then by first course name and second course name in ascending order.
    """)
    return


@app.cell
def _():
    """
    WITH course_info AS (
        SELECT
            user_id,
            completion_date,
            course_name
        FROM
            course_completions
        WHERE
            user_id IN (SELECT user_id FROM course_completions GROUP BY 1 HAVING COUNT(*) >= 5 AND AVG(course_rating)>=4)
    ),
    course_pairs AS (
        SELECT
            course_name AS first_course,
            LEAD(course_name, 1) OVER (PARTITION BY user_id ORDER BY completion_date) AS second_course
        FROM
            course_info
    )
    SELECT
        first_course,
        second_course,
        COUNT(*) AS transition_count
    FROM
        course_pairs
    WHERE
        second_course IS NOT NULL
    GROUP BY
        1, 2
    ORDER BY
        3 DESC, LOWER(first_course), LOWER(second_course);
    """
    return


@app.cell
def _():
    import pandas as pd

    def topLearnerCourseTransitions(courses: pd.DataFrame) -> pd.DataFrame:
        df = courses.copy()
        df["course_rating"] = df["course_rating"].fillna(4)
        df["ave"] = df.groupby("user_id")["course_rating"].transform("mean")
        df["cnt"] = df.groupby("user_id")["course_rating"].transform("count")
        df = df.sort_values(["user_id", "completion_date"])
        df["second_course"] = df["course_name"].shift(-1)

        mask = (
            (df["ave"] >= 4)
            & (df["cnt"] >= 5)
            & (df["user_id"] == df["user_id"].shift(-1))
        )

        transitions = (
            df.loc[mask]
            .rename(columns={"course_name": "first_course"})
            .groupby(["first_course", "second_course"], as_index=False)
            .size()
            .rename(columns={"size": "transition_count"})
        )

        transitions = (
            transitions.assign(
                _lower_first=lambda d: d["first_course"].str.lower(),
                _lower_second=lambda d: d["second_course"].str.lower(),
            )
            .sort_values(
                ["transition_count", "_lower_first", "_lower_second"],
                ascending=[False, True, True],
            )
            .drop(columns=["_lower_first", "_lower_second"])
        )

        return transitions[["first_course", "second_course", "transition_count"]]
    return


if __name__ == "__main__":
    app.run()
