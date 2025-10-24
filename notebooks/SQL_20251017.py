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
            "/notebooks/SQL_20251016.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251020.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2989

    Table: Scores

    | Column Name  | Type    |
    |--------------|---------|
    | student_id   | int     |
    | student_name | varchar |
    | assignment1  | int     |
    | assignment2  | int     |
    | assignment3  | int     |

    student_id is column of unique values for this table. This table contains student_id, student_name, assignment1, assignment2, and assignment3.

    Write a solution to calculate the difference in the total score (sum of all 3 assignments) between the highest score obtained by students and the lowest score obtained by them.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    WITH total_score_info AS (
        SELECT
            student_id,
            SUM(assignment) AS total_score
        FROM
            Scores
                CROSS JOIN LATERAL UNNEST(ARRAY[assignment1, assignment2, assignment3]) AS assignment
        GROUP BY
            1
    )
    SELECT
        MAX(total_score) - MIN(total_score) AS difference_in_score
    FROM
        total_score_info;
    """
    return


@app.cell
def _():
    import pandas as pd

    def class_performance(scores: pd.DataFrame) -> pd.DataFrame:
        df = scores.set_index(["student_id", "student_name"]).stack().rename("score")
        difference_in_score = df.groupby(level=0).sum().max() - df.groupby(level=0).sum().min()
        df = pd.DataFrame({"difference_in_score": [difference_in_score]})
        return df

    return


if __name__ == "__main__":
    app.run()
