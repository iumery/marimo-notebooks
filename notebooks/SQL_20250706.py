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
            "/notebooks/SQL_20250705.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250707.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 15: Condition Clashes — Overlapping Trials with the Same Condition

    Goal: Identify pairs of trials that study the same condition and have overlapping start/end dates.

    Requirements:

    - Use the AACT database.
    - For each pair of trials (A, B), find those that:
        - Share at least one condition name.
        - Have overlapping time windows, where:
            - A.start_date <= B.completion_date
            - B.start_date <= A.completion_date
        - A.nct_id < B.nct_id (to avoid duplicates and self-pairs).
    - Output: nct_id_A, nct_id_B, shared_condition, A.start_date, A.completion_date, B.start_date, B.completion_date
    - Only include pairs where both trials have non-null start and completion dates.
    - Order by shared_condition, nct_id_A, nct_id_B.
    - Limit to the first 100 rows.
    """
    )
    return


@app.cell
def _():
    """
    WITH trial_with_condition AS (
        SELECT
            nct_id,
            start_date,
            completion_date,
            TRIM(INITCAP(conditions.name)) AS condition
        FROM
            studies
                JOIN conditions USING(nct_id)
        WHERE
            start_date IS NOT NULL
            AND
            completion_date IS NOT NULL
    )
    SELECT
        t1.nct_id AS nct_id_A,
        t2.nct_id AS nct_id_B,
        t1.condition AS shared_condition,
        t1.start_date AS start_date_A,
        t1.completion_date AS completion_date_A,
        t2.start_date AS start_date_B,
        t2.completion_date AS completion_date_B
    FROM
        trial_with_condition t1
            JOIN trial_with_condition t2 ON t1.condition = t2.condition
                AND (t2.start_date BETWEEN t1.start_date AND t1.completion_date)
                AND t1.nct_id != t2.nct_id
    ORDER BY
        3
    LIMIT
        100;
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 16: Multi-Sponsor Conflicts of Interest

    Goal: Identify trials that are potentially subject to conflict of interest by having:

    - At least 3 different lead sponsors across all trials that studied the *same condition* within a 2-year window.

    Requirements:

    - Use the AACT database.
    - For each condition name, look for 2-year periods (rolling or fixed window, your choice) during which:
        - At least 3 distinct trials studied that condition
        - And those 3 trials had 3 **different lead sponsors**
    - Output: condition_name, window_start, window_end, sponsor_count, trial_count
    - Only include rows where sponsor_count ≥ 3
    - Order by sponsor_count DESC, then condition_name
    - Limit 50 rows
    """
    )
    return


@app.cell
def _():
    """
    WITH trial_with_condition AS (
        SELECT
            nct_id,
            start_date,
            completion_date,
            TRIM(INITCAP(conditions.name)) AS condition
        FROM
            studies
                JOIN conditions USING(nct_id)
        WHERE
            start_date IS NOT NULL
            AND
            completion_date IS NOT NULL
    )
    SELECT
        t1.nct_id AS nct_id_A,
        t2.nct_id AS nct_id_B,
        t1.condition AS shared_condition,
        t1.start_date AS start_date_A,
        t1.completion_date AS completion_date_A,
        t2.start_date AS start_date_B,
        t2.completion_date AS completion_date_B
    FROM
        trial_with_condition t1
            JOIN trial_with_condition t2 ON t1.condition = t2.condition
                AND (t2.start_date BETWEEN t1.start_date AND t1.completion_date)
                AND t1.nct_id != t2.nct_id
    ORDER BY
        3
    LIMIT
        100;
    """
    return


if __name__ == "__main__":
    app.run()
