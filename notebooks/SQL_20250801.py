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
            "/notebooks/SQL_20250725.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250802.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 37: Dominant Co-Flying Partner

    Goal: For each passenger who has taken at least 10 flights in the last year, find the person they've most frequently flown with on the same flight.

    Requirements:

    - Use the 'postgres_air' database.
    - Consider only flights in the past 1 year (`scheduled_departure >= NOW() - INTERVAL '1 year'`)
    - Count co-flying as being booked on the same `flight_id`
    - Output: passenger_id, full_name, partner_full_name, num_flights_together
    - If tie, pick the one with lexicographically smallest full name
    - Order by num_flights_together DESC, then passenger_id
    """
    )
    return


@app.cell
def _():
    """
    WITH recent_flights AS (
        SELECT
            passenger_id,
            CONCAT(INITCAP(first_name), ' ', INITCAP(last_name)) AS full_name,
            flight_id
        FROM
            passenger
                JOIN booking_leg USING (booking_id)
                JOIN flight USING (flight_id)
        WHERE
            scheduled_departure >= NOW() - INTERVAL '1 year'
    ),
    passenger_flight_count AS (
        SELECT
            passenger_id
        FROM
            recent_flights
        GROUP BY
            1
        HAVING
            COUNT(*) >= 10
    ),
    co_flying_pairs AS (
        SELECT
            r1.passenger_id AS p1_id,
            r1.full_name AS p1_name,
            r2.passenger_id AS p2_id,
            r2.full_name AS p2_name,
            COUNT(*) AS shared_flights
        FROM
            recent_flights r1
                JOIN recent_flights r2 ON r1.flight_id = r2.flight_id AND r1.passenger_id != r2.passenger_id
        WHERE
            r1.passenger_id IN (SELECT passenger_id FROM passenger_flight_count)
        GROUP BY
            1, 2, 3, 4
    ),
    ranked_partners AS (
        SELECT
            *,
            ROW_NUMBER() OVER (PARTITION BY p1_id ORDER BY shared_flights DESC, p2_name) AS rn
        FROM
            co_flying_pairs
    )
    SELECT
        p1_id AS passenger_id,
        p1_name AS full_name,
        p2_name AS partner_full_name,
        shared_flights AS num_flights_together
    FROM
        ranked_partners
    WHERE
        rn = 1
    ORDER BY
        num_flights_together DESC, passenger_id;
    """
    return


if __name__ == "__main__":
    app.run()
