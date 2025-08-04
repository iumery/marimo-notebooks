import marimo

__generated_with = "0.14.10"
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
            "/notebooks/SQL_20250721.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250723.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 33: Repeated Trial Titles with Different Conditions

    Goal: Find interventional studies that have the exact same title appearing in multiple trials, but linked to different conditions.

    Requirements:

    - Only include trials where the study_type is 'Interventional'.
    - Titles should be matched case-insensitively and whitespace-trimmed.
    - Show only titles that appear in at least 2 trials **with different condition groups**.
    - For each such title, return:
        - title
        - number of distinct trials
        - number of distinct condition names
        - list of condition groups (sorted alphabetically)

    Hints:

    - Use `studies.title`, `studies.study_type`, and the `conditions` table
    - Watch out for subtle whitespace and case issues in titles and condition names
    """
    )
    return


@app.cell
def _():
    """
    WITH title_and_condition AS (
        SELECT
            TRIM(INITCAP(brief_title)) AS title,
            name AS condition_name,
            nct_id
        FROM
            studies
                JOIN conditions USING(nct_id)
        WHERE
            LOWER(study_type) = 'interventional'
    )
    SELECT
        title,
        COUNT(DISTINCT nct_id) AS num_distinct_trial,
        COUNT(DISTINCT condition_name) AS num_distinct_condition,
        STRING_AGG(DISTINCT condition_name, ', ') AS list_condition
    FROM
        title_and_condition
    GROUP BY
        1
    HAVING
        COUNT(DISTINCT condition_name) > 1
    ORDER BY
        3 DESC,
        2 DESC,
        1;
    """
    return


if __name__ == "__main__":
    app.run()
