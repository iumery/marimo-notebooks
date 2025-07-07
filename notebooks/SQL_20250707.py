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
            "/notebooks/SQL_20250706.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250708.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 17: Multiphase Intervention Coverage

    Goal: Identify drugs (interventions) that have been tested in at least 3 different trial phases.

    Requirements:

    - Use the AACT database.
    - Consider only interventions where intervention_type = 'Drug'.
    - For each intervention name, count how many distinct `phase` values it's associated with.
    - Only include drugs tested in 3 or more distinct phases.
    - Output: intervention_name, phase_count
    - Order by phase_count DESC, then intervention_name
    """
    )
    return


@app.cell
def _():
    """
    WITH drug_by_phase AS (
        SELECT
            nct_id,
            INITCAP(interventions.name) AS intervention_name,
            TRIM(INITCAP(REGEXP_SPLIT_TO_TABLE(phase, '/'))) AS phase
        FROM
            interventions
                JOIN studies USING(nct_id)
        WHERE
            LOWER(intervention_type) = 'drug'
            AND phase IS NOT NULL
            AND phase != 'NA'
    )
    SELECT
        intervention_name,
        COUNT(DISTINCT phase) AS phase_count
    FROM
        drug_by_phase
    GROUP BY
        1
    HAVING
        COUNT(DISTINCT phase) >= 3
    ORDER BY
        2 DESC,
        1;
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 18: Longest Operational Airport Pair

    Goal: Find the airport-to-airport route that has operated flights across the longest calendar span.

    Requirements:

    - Use the `postgres_air.flight` table.
    - Group by (departure_airport, arrival_airport).
    - For each pair, calculate the range between:
        - the earliest scheduled_departure
        - the latest scheduled_arrival
    - Output: departure_airport, arrival_airport, span_days
    - Only include pairs where span_days >= 1000
    - Order by span_days DESC
    - Limit to top 10 results
    """
    )
    return


@app.cell
def _():
    """
    WITH span_by_airport_and_route AS (
        SELECT
            departure_airport,
            arrival_airport,
            flight_no,
            MAX(CAST(scheduled_arrival AS date)) - MIN(CAST(scheduled_departure AS date)) AS span_days
        FROM flight
        GROUP BY
            1, 2, 3
    )
    SELECT
        departure_airport,
        arrival_airport,
        MAX(span_days) AS span_days
    FROM
        span_by_airport_and_route
    GROUP BY
        1, 2
    ORDER BY
        3 DESC,
        1, 2;
    """
    return


if __name__ == "__main__":
    app.run()
