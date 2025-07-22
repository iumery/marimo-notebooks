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
            "/notebooks/SQL_20250704.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250706.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 14: Indirectly Connected Airports via One Transfer

    Goal: Find the top 20 airport pairs (A → C) that are not directly connected, but can be reached with a single transfer at a third airport B (i.e., A → B → C).

    Requirements:

    - Use the `postgres_air.flight` table.
    - A direct connection is defined by any row where A = departure_airport and C = arrival_airport.
    - An indirect connection is defined when:
        - There exists a flight from A → B,
        - And a separate flight from B → C,
        - Where A, B, and C are all **distinct** airports.
        - And there is **no direct flight** from A → C.
    - Count how many distinct B airports exist for each (A → C) pair.
    - Output: source_airport (A), destination_airport (C), num_transfer_options
    - Only include pairs with at least 3 distinct connecting airports B.
    - Order by num_transfer_options DESC, then source_airport, destination_airport
    - Limit to 20 rows.

    Notes:

    - All airport codes are 3-letter strings in `flight.departure_airport` and `flight.arrival_airport`.
    - Exclude any A = B = C cases or reuse of airports within a route.
    """
    )
    return


@app.cell
def _():
    """
    WITH unique_dep_arr AS (
        SELECT DISTINCT
            departure_airport,
            arrival_airport
        FROM
            flight
    ),
    a_b_c_line AS (
        SELECT
            u1.departure_airport AS source_airport,
            u1.arrival_airport AS middle_airport,
            u2.arrival_airport AS destination_airport
        FROM
            unique_dep_arr u1
                JOIN unique_dep_arr u2 ON u1.arrival_airport = u2.departure_airport
                    AND u1.departure_airport != u2.arrival_airport
                    AND (u1.departure_airport, u2.arrival_airport) NOT IN (SELECT * FROM unique_dep_arr)
    )
    SELECT
        source_airport,
        destination_airport,
        COUNT(middle_airport) AS num_transfer_options
    FROM
        a_b_c_line
    GROUP BY
        1, 2
    HAVING
        COUNT(middle_airport) >=3
    ORDER BY
        3 DESC,
        1, 2
    LIMIT
        20;
    """
    return


if __name__ == "__main__":
    app.run()
