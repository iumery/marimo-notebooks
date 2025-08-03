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
            "/notebooks/SQL_20250724.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250801.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 36: Most Popular Connection Routes

    Goal: Identify the most frequently traveled *connection routes*, i.e., two-leg journeys within the same booking.

    Requirements:

    - Only consider bookings with exactly 2 legs (i.e., true one-connection trips).
    - A connection route is defined as (departure_airport_1 → arrival_airport_1 → arrival_airport_2)
    - Count how many times each connection route occurs across all passengers.
    - Output: departure_airport, connection_airport, final_arrival_airport, num_trips
    - Only include routes that occurred at least 10 times.
    - Order by num_trips descending, then alphabetically.
    """
    )
    return


@app.cell
def _():
    """
    WITH two_leg_bookings AS (
        SELECT
            booking_id,
            COUNT(*) AS leg_count
        FROM
            booking_leg
        GROUP BY
            booking_id
        HAVING COUNT(*) = 2
    ),
    legs_with_airports AS (
        SELECT
            b.booking_id,
            leg_num,
            f.departure_airport AS dep_airport,
            f.arrival_airport AS arr_airport
        FROM
            two_leg_bookings b
            JOIN booking_leg bl USING(booking_id)
            JOIN flight f USING(flight_id)
    ),
    joined_legs AS (
        SELECT
            l1.booking_id,
            l1.dep_airport AS origin,
            l1.arr_airport AS connection,
            l2.arr_airport AS final_dest
        FROM
            legs_with_airports l1
            JOIN legs_with_airports l2
                ON l1.booking_id = l2.booking_id
             AND l1.leg_num = 1
             AND l2.leg_num = 2
    )
    SELECT
        origin AS departure_airport,
        connection AS connection_airport,
        final_dest AS final_arrival_airport,
        COUNT(*) AS num_trips
    FROM
        joined_legs
    GROUP BY
        1, 2, 3
    HAVING
        COUNT(*) >= 10
    ORDER BY
        num_trips DESC, 1, 2, 3;
    """
    return


if __name__ == "__main__":
    app.run()
