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
            "/notebooks/SQL_20250714.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_202507016.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 26: Conditional Sponsor Overlap in Condition Groups

    Goal: Find sponsor organizations that have led trials across *multiple different condition groups* within a rolling time window, showing possible strategic expansion.

    Requirements:

    - Use the AACT database.
    - Focus only on sponsors where `lead_or_collaborator = 'lead'`.
    - For each `sponsor.name`, determine the number of distinct condition groups it has led trials in.
    - A "condition group" is defined by the **first word** of each `conditions.name` (case-insensitive). e.g., "Breast Cancer" and "Breast Tumor" both map to `"breast"`.
    - Only consider trials that started **within any 3-year sliding window** (e.g., Jan 2017–Jan 2020).
    - For each sponsor and 3-year window, compute:
        - Number of **distinct trials** they led
        - Number of **distinct condition groups**
    - Only include sponsor-window pairs where:
        - Distinct condition groups ≥ 3
        - Distinct trials ≥ 5

    Output:

    - sponsor_name
    - window_start
    - window_end
    - trial_count
    - group_count
    - (optional: list of condition groups in that window, comma-separated)
    """
    )
    return


@app.cell
def _():
    """
    WITH sponsor_with_condition AS (
    SELECT DISTINCT
        nct_id,
        start_date,
        CAST(start_date + INTERVAL '3 YEARS' AS DATE) AS rolling_end_date,
        SPLIT_PART(SPLIT_PART(UPPER(conditions.name),' ',1),',',1) AS condition_name,
        sponsors.name AS sponsors_name
    FROM
        studies
            JOIN conditions USING(nct_id)
            JOIN sponsors USING(nct_id)
    WHERE
        LOWER(lead_or_collaborator) = 'lead'
    ),
    sponsor_with_condition_rolling_data AS (
        SELECT
            sc1.nct_id,
            sc1.start_date,
            sc1.rolling_end_date,
            sc2.condition_name,
            sc1.sponsors_name
        FROM
            sponsor_with_condition sc1
                JOIN sponsor_with_condition sc2 ON sc1.sponsors_name = sc2.sponsors_name AND sc2.start_date BETWEEN sc1.start_date AND sc1.rolling_end_date
    )
    SELECT
        sponsors_name,
        start_date,
        rolling_end_date,
        COUNT(*) AS trial_count,
        COUNT(DISTINCT condition_name) AS group_count,
        STRING_AGG(DISTINCT condition_name, ', ') AS list_of_condition_groups

    FROM
        sponsor_with_condition_rolling_data
    GROUP BY
        sponsors_name,start_date,rolling_end_date
    HAVING
        COUNT(*) >= 5
        AND
        COUNT(DISTINCT condition_name) >= 3
    ORDER BY
        1, 2,
        4 DESC,
        5 DESC;
    """
    return


if __name__ == "__main__":
    app.run()
