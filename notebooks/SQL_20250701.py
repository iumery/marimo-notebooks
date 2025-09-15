import marimo

__generated_with = "0.15.4"
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
            "/notebooks/SQL_20250630.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250702.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 7: Categorize Trials by Status and Study Type

    Goal: From the AACT database, summarize how many studies fall into each combination of overall status and study type.

    Requirements:

    - Use the 'studies' table from the ctgov schema.
    - Output: overall_status, study_type_grouped, study_count
    - Group study types using a CASE statement:
        - 'Interventional' stays as is
        - 'Observational' and 'Observational [Patient Registry]' become 'Observational'
        - All others become 'Other'
    - Order by study_count descending
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        overall_status,
        CASE
            WHEN UPPER(study_type) = 'INTERVENTIONAL' THEN 'Interventional'
            WHEN UPPER(study_type) LIKE 'OBSERVATIONAL%' THEN 'Observational'
            ELSE 'Other'
        END AS study_type_grouped,
        COUNT(*) AS study_count
    FROM
        studies
    GROUP BY
        1, 2
    ORDER BY
        3 DESC;
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 8: Average Arrival Delay by Aircraft and Destination

    Goal: Compute the average arrival delay for each aircraft type at each destination airport.

    Requirements:

    - Use the 'flight' table from the postgres_air schema.
    - Output: aircraft_code, arrival_airport, avg_arrival_delay
    - Ignore null or negative arrival delays
    - Round avg_arrival_delay to 2 decimal places
    - Only include combinations with at least 50 flights
    - Order by avg_arrival_delay descending
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        aircraft_code,
        arrival_airport,
        ROUND(AVG(EXTRACT(EPOCH FROM actual_arrival - scheduled_arrival)) / 60, 2) AS avg_arrival_delay
        -- EPOCH gives difference in seconds
        FROM
        flight
    WHERE
        actual_arrival > scheduled_arrival
    GROUP BY
        1, 2
    HAVING
        COUNT(*) >= 50
    ORDER BY
        3 DESC;
    """
    return


if __name__ == "__main__":
    app.run()
