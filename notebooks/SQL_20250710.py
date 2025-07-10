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
            "/notebooks/SQL_20250709.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_202507011.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 22: Multi-Trial Enrollment Acceleration

    Goal: Identify drugs (interventions) where each successive trial recruited participants faster than the previous one.

    Requirements:

    - Use the AACT database.
    - Only consider interventions where:
        - intervention_type = 'Drug'
        - enrollment_type = 'Actual'
        - enrollment and start/completion dates are all present
        - The drug appears in at least 3 such trials
    - Define **recruitment_rate** = enrollment / (completion_date - start_date in days)
    - For each drug, order its trials by start_date.
    - Only return drugs where recruitment_rate strictly increases in each successive trial.
    - Output: intervention_name, trial_count
    - Order by trial_count DESC, then intervention_name
    """
    )
    return


@app.cell
def _():
    """
    WITH drug_with_recruitment_rate AS (
        SELECT DISTINCT
            TRIM(INITCAP(interventions.name)) AS intervention_name,
            CAST(enrollment AS FLOAT) / NULLIF(completion_date - start_date, 0) AS recruitment_rate,
            start_date
        FROM
            interventions
                JOIN studies USING(nct_id)
        WHERE
            LOWER(intervention_type) = 'drug'
            AND
            LOWER(enrollment_type) = 'actual'
            AND
            enrollment IS NOT NULL
            AND
            start_date IS NOT NULL
            AND
            completion_date IS NOT NULL
    ),
    drug_with_recruitment_rate_rank AS (
        SELECT
            intervention_name,
            recruitment_rate,
            start_date,
            ABS(DENSE_RANK() OVER (PARTITION BY intervention_name ORDER BY start_date)
                - DENSE_RANK() OVER (PARTITION BY intervention_name ORDER BY recruitment_rate)) AS is_increasing
        FROM
            drug_with_recruitment_rate
    )
    SELECT
        intervention_name,
        COUNT(*) AS trial_count
    FROM
        drug_with_recruitment_rate_rank
    GROUP BY
        1
    HAVING
        SUM(is_increasing) = 0
        AND
        COUNT(*) >= 3
    ORDER BY
        2 DESC,
        1;
    """
    return


if __name__ == "__main__":
    app.run()
