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
            "/notebooks/SQL_20250930.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251002.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2793

    Table: Flights

    | Column Name | Type |
    |-------------|------|
    | flight_id   | int  |
    | capacity    | int  |

    flight_id column contains distinct values. Each row of this table contains flight id and capacity.

    Table: Passengers

    | Column Name  | Type     |
    |--------------|----------|
    | passenger_id | int      |
    | flight_id    | int      |
    | booking_time | datetime |

    passenger_id column contains distinct values. booking_time column contains distinct values. Each row of this table contains passenger id, booking time, and their flight id.

    Passengers book tickets for flights in advance. If a passenger books a ticket for a flight and there are still empty seats available on the flight, the passenger's ticket will be confirmed. However, the passenger will be on a waitlist if the flight is already at full capacity.

    Write a solution to determine the current status of flight tickets for each passenger.

    Return the result table ordered by passenger_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        passenger_id,
        CASE
            WHEN ROW_NUMBER() OVER (PARTITION BY flight_id ORDER BY booking_time) - COALESCE(capacity, 0) > 0 THEN 'Waitlist'
            ELSE 'Confirmed'
        END AS Status
    FROM
        Passengers
            LEFT JOIN Flights USING (flight_id)
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def ticket_status(
        flights: pd.DataFrame, passengers: pd.DataFrame
    ) -> pd.DataFrame:
        df = pd.merge(passengers, flights, how="left", on="flight_id")
        df["rank"] = df.sort_values("booking_time").groupby("flight_id").cumcount()
        df["Status"] = df["rank"] < df["capacity"]
        df["Status"] = df["Status"].map({True: "Confirmed", False: "Waitlist"})
        df = df[["passenger_id", "Status"]].sort_values("passenger_id")
        return df
    return


if __name__ == "__main__":
    app.run()
