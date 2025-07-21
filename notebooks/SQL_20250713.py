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
            "/notebooks/SQL_20250711.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250714.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 24: Trials with Redundant Outcome Titles

    Goal: Find interventional trials that report at least 5 outcome measures, where at least 2 of those outcomes share the same outcome title (case-insensitive).

    Requirements:

    - Use the AACT database.
    - Use only trials where `study_type = 'Interventional'`.
    - Use the `outcomes` table and treat `outcomes.title` as the label for the outcome.
    - Normalize outcome titles by:
        - Lowercasing
        - Trimming whitespace
    - For each `nct_id`:
        - Count how many total outcomes exist
        - Count how many **normalized titles** appear more than once
    - Output: `nct_id`, `total_outcomes`, `redundant_title_count`
    - Only include trials where:
        - `total_outcomes >= 5`
        - `redundant_title_count >= 1`
    - Order by `redundant_title_count` DESC, then `total_outcomes` DESC
    - Limit 50 rows
    """
    )
    return


@app.cell
def _():
    """
    WITH study_outcomes AS (
        SELECT
            nct_id,
            TRIM(INITCAP(title)) AS title
        FROM
            studies
                JOIN outcomes USING(nct_id)
        WHERE
            LOWER(study_type) = 'interventional'
    )
    SELECT
        nct_id,
        COUNT(title) AS total_outcomes,
        COUNT(title) - COUNT(DISTINCT title) AS redundant_title_count
    FROM
        study_outcomes
    GROUP BY
        1
    HAVING
        COUNT(title) >= 5
        AND
        COUNT(title) - COUNT(DISTINCT title) >= 1
    ORDER BY
        3 DESC,
        2 DESC
    LIMIT
        50;
    """
    return


if __name__ == "__main__":
    app.run()
