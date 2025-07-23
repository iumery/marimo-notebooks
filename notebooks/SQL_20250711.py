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
            "/notebooks/SQL_20250710.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250713.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 23: Age Discrepancy Across Trial Designs

    Goal: Find interventional trials that claim to accept "Adults" (i.e., age 18–64), but whose lower age bound is above 25 or upper bound is below 60 — i.e., contradicting the label.

    Requirements:

    - Use the AACT database.
    - Focus only on trials where `study_type = 'Interventional'`
    - Join `eligibilities` and `studies` tables.
    - Only include trials where `eligibilities.gender = 'All'` (to simplify)
    - For each trial, inspect:
        - `eligibilities.minimum_age`
        - `eligibilities.maximum_age`
        - `eligibilities.healthy_volunteers` (optional context)
    - Detect trials that list:
        - `eligibilities.minimum_age > 25` OR
        - `eligibilities.maximum_age < 60`
        BUT still claim `eligibilities.criteria` includes the word "Adults" or phrase like "age 18–64"

    Output:

    - nct_id, minimum_age, maximum_age, excerpt_from_criteria
    - Order by minimum_age DESC

    Notes:

    - You may need to parse `minimum_age` and `maximum_age` which are text fields (e.g., '30 Years')
    - Use `ILIKE` to scan `eligibilities.criteria` for "Adults", "18 to 64", or similar patterns
    - Limit to 100 rows
    """
    )
    return


@app.cell
def _():
    r"""
    SELECT
        nct_id,
        minimum_age,
        maximum_age,
        CASE
            WHEN minimum_age ~ '^\d+' AND CAST(SPLIT_PART(minimum_age, ' ', 1) AS INT) > 25 THEN 'CONTRADICTING'
            WHEN maximum_age ~ '^\d+' AND CAST(SPLIT_PART(maximum_age, ' ', 1) AS INT) < 60 THEN 'CONTRADICTING'
            ELSE 'NOT CONTRADICTING'
        END AS contradiction_status,
        LEFT(criteria, 100) AS excerpt_from_criteria
    FROM
        studies
            JOIN eligibilities USING(nct_id)
    WHERE
        LOWER(study_type) = 'interventional'
        AND LOWER(gender) = 'all'
        AND (
            LOWER(criteria) LIKE '%adults%'
            OR LOWER(criteria) LIKE '%18 to 64%'
        )
    LIMIT
        100;
    """
    return


if __name__ == "__main__":
    app.run()
