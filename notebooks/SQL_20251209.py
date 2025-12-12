import marimo

__generated_with = "0.18.1"
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
            "/notebooks/SQL_20251208.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251210.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3705

    Table: restaurant_orders

    | Column Name      | Type     |
    |------------------|----------|
    | order_id         | int      |
    | customer_id      | int      |
    | order_timestamp  | datetime |
    | order_amount     | decimal  |
    | payment_method   | varchar  |
    | order_rating     | int      |

    order_id is the unique identifier for this table. payment_method can be cash, card, or app. order_rating is between 1 and 5, where 5 is the best (NULL if not rated). order_timestamp contains both date and time information.

    Write a solution to find golden hour customers - customers who consistently order during peak hours and provide high satisfaction. A customer is a golden hour customer if they meet ALL the following criteria:

    - Made at least 3 orders.
    - At least 60% of their orders are during peak hours (11:00-14:00 or 18:00-21:00).
    - Their average rating for rated orders is at least 4.0, round it to 2 decimal places.
    - Have rated at least 50% of their orders.

    Return the result table ordered by average_rating in descending order, then by customer_id in descending order.
    """)
    return


@app.cell
def _():
    """
    SELECT
        customer_id,
        COUNT(order_id) AS total_orders,
        ROUND((COUNT(order_id) FILTER (WHERE order_timestamp::TIME BETWEEN '11:00:00' AND '14:00:00' OR order_timestamp::TIME BETWEEN '18:00:00' AND '21:00:00'))*100.0 / COUNT(order_id), 0) AS peak_hour_percentage,
        ROUND(AVG(order_rating), 2) AS average_rating
    FROM
        restaurant_orders
    GROUP BY
        customer_id
    HAVING
        COUNT(order_id) >= 3
            AND (COUNT(order_id) FILTER (WHERE order_timestamp::TIME BETWEEN '11:00:00' AND '14:00:00' OR order_timestamp::TIME BETWEEN '18:00:00' AND '21:00:00'))*100.0 / COUNT(order_id) >= 60
            AND ROUND(AVG(order_rating), 2) >= 4.0
            AND COUNT(order_rating)*100.0 /  COUNT(order_id) >= 50
    ORDER BY
        4 DESC, 1 DESC
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_golden_hour_customers(
        restaurant_orders: pd.DataFrame,
    ) -> pd.DataFrame:
        df = restaurant_orders.copy()
        df["order_timestamp"] = pd.to_datetime(df["order_timestamp"])
        df["hour"] = df["order_timestamp"].dt.hour

        df = df.groupby("customer_id", as_index=False).agg(
            total_orders=("order_id", "nunique"),
            peak_cnt=(
                "order_id",
                lambda x: x[
                    (df.loc[:, "hour"].between(11, 13))
                    | (df.loc[:, "hour"].between(18, 20))
                ].nunique(),
            ),
            average_rating=("order_rating", "mean"),
            rating_cnt=("order_rating", "count"),
        )

        df["peak_hour_percentage"] = (df["peak_cnt"] * 100) / df["total_orders"]
        df["rating_percentage"] = df["rating_cnt"] / df["total_orders"]

        df = df[
            (df["total_orders"] >= 3)
            & (df["peak_hour_percentage"] >= 60)
            & (df["average_rating"] >= 4)
            & (df["rating_percentage"] >= 0.5)
        ]

        df["average_rating"] = df["average_rating"].round(2)
        df["peak_hour_percentage"] = df["peak_hour_percentage"].round()

        df = df[
            [
                "customer_id",
                "total_orders",
                "peak_hour_percentage",
                "average_rating",
            ]
        ].sort_values(
            by=["average_rating", "customer_id"], ascending=[False, False]
        )

        return df
    return


if __name__ == "__main__":
    app.run()
