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
            "/notebooks/SQL_20251024.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251028.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3051

    Table: Candidates

    | Column Name  | Type    | 
    |--------------|---------|
    | candidate_id | int     | 
    | skill        | varchar |

    (candidate_id, skill) is the primary key (columns with unique values) for this table. Each row includes candidate_id and skill.

    Write a query to find the candidates best suited for a Data Scientist position. The candidate must be proficient in Python, Tableau, and PostgreSQL.

    Return the result table ordered by candidate_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        candidate_id
    FROM (
        SELECT candidate_id FROM Candidates WHERE skill = 'Python'
            INTERSECT SELECT candidate_id FROM Candidates WHERE skill = 'Tableau'
            INTERSECT SELECT candidate_id FROM Candidates WHERE skill = 'PostgreSQL'
    ) sub
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def find_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
        candidate_id = set(candidates["candidate_id"])
        for skill in ["Python", "Tableau", "PostgreSQL"]:
            sub_candidate_id = set(candidates[candidates["skill"] == skill]["candidate_id"])
            candidate_id = candidate_id & sub_candidate_id
        df = pd.DataFrame({"candidate_id": list(candidate_id)}).sort_values("candidate_id")
        return df

    return


if __name__ == "__main__":
    app.run()
