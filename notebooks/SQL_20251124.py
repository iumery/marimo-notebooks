import marimo

__generated_with = "0.17.8"
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
            "/notebooks/SQL_20251121.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251125.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3166

    Table: ParkingTransactions

    | Column Name  | Type      |
    |--------------|-----------|
    | lot_id       | int       |
    | car_id       | int       |
    | entry_time   | datetime  |
    | exit_time    | datetime  |
    | fee_paid     | decimal   |

    (lot_id, car_id, entry_time) is the primary key (combination of columns with unique values) for this table. Each row of this table contains the ID of the parking lot, the ID of the car, the entry and exit times, and the fee paid for the parking duration.

    Write a solution to find the total parking fee paid by each car across all parking lots, and the average hourly fee (rounded to 2 decimal places) paid by each car. Also, find the parking lot where each car spent the most total time.

    Return the result table ordered by car_id in ascending order.

    Note: Test cases are generated in such a way that an individual car cannot be in multiple parking lots at the same time.
    """)
    return


@app.cell
def _():
    """
    WITH parking_info AS (
        SELECT
            lot_id,
            car_id,
            EXTRACT(EPOCH FROM exit_time - entry_time)/3600 AS park_time,
            fee_paid
        FROM
            ParkingTransactions
    ),
    time_lot_info AS (
        SELECT DISTINCT ON (car_id)
            car_id,
            lot_id,
            SUM(park_time) AS time_lot
        FROM
            parking_info
        GROUP BY
            1, 2
        ORDER BY
            1, 3 DESC
    )
    SELECT
        car_id,
        SUM(fee_paid) AS total_fee_paid,
        ROUND(SUM(fee_paid)*1.0/SUM(park_time), 2) AS avg_hourly_fee,
        MAX(tli.lot_id) AS most_time_lot
    FROM
        parking_info pi
            JOIN time_lot_info tli USING (car_id)
    GROUP BY
        1
    ORDER BY
        1
    """
    return


@app.cell
def _():
    import pandas as pd


    def calculate_fees_and_duration(
        parking_transactions: pd.DataFrame,
    ) -> pd.DataFrame:
        df = parking_transactions.copy()
        df["parking_time"] = (df["exit_time"] - df["entry_time"]).astype(
            int
        ) / 3600e9
        df_max_lot = (
            df.groupby(["car_id", "lot_id"], as_index=False)["parking_time"]
            .sum()
            .sort_values("parking_time", ascending=False)
            .drop_duplicates("car_id")[["car_id", "lot_id"]]
            .rename(columns={"lot_id": "most_time_lot"})
        )
        df_other = df.groupby("car_id", as_index=False).agg(
            total_fee_paid=("fee_paid", "sum"), total_hour=("parking_time", "sum")
        )
        df_other["avg_hourly_fee"] = (
            df_other["total_fee_paid"] / df_other["total_hour"]
        ).round(2)
        df = pd.merge(df_other, df_max_lot, on="car_id")[
            ["car_id", "total_fee_paid", "avg_hourly_fee", "most_time_lot"]
        ].sort_values("car_id")
        return df
    return


if __name__ == "__main__":
    app.run()
