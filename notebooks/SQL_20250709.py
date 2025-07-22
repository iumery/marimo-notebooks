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
            "/notebooks/SQL_20250708.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250710.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 21: First-Time Drug–Condition Trials in the Last 5 Years

    Goal: Identify trials from the past 5 years where a drug was tested with a condition for the first time in recorded AACT history.

    Requirements:

    - Use the AACT database.
    - Define a drug-condition pair as (intervention_name, condition_name), where intervention_type = 'Drug'
    - For each such pair, determine the **earliest trial start_date** in AACT history.
    - Then identify whether that **first occurrence** happened in the past 5 years.
    - Output: nct_id, intervention_name, condition_name, first_trial_start_date
    - Only include pairs where the first trial was in the past 5 years (relative to today).
    - Order by first_trial_start_date DESC
    """
    )
    return


@app.cell
def _():
    """
    WITH start_date_ranking AS (
        SELECT
            nct_id,
            TRIM(INITCAP(conditions.name)) AS condition_name,
            TRIM(INITCAP(interventions.name)) AS intervention_name,
            start_date,
            ROW_NUMBER()
                OVER (
                    PARTITION BY
                        TRIM(INITCAP(conditions.name)),
                        TRIM(INITCAP(interventions.name))
                    ORDER BY start_date
                ) AS start_date_rank
        FROM
            conditions
                JOIN interventions USING(nct_id)
                JOIN studies USING(nct_id)
        WHERE
            LOWER(intervention_type) = 'drug'
            AND
            start_date IS NOT NULL
    )
    SELECT
        nct_id,
        condition_name,
        intervention_name,
        start_date AS first_trial_start_date
    FROM
        start_date_ranking
    WHERE
        start_date_rank = 1
        AND
        start_date BETWEEN (NOW() - INTERVAL '5 years') AND NOW()
    ORDER BY
        4 DESC;
    """
    return


if __name__ == "__main__":
    app.run()
