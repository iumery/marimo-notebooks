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
            "/notebooks/SQL_20251209.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251211.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3716

    Table: subscription_events

    | Column Name      | Type    |
    |------------------|---------|
    | event_id         | int     |
    | user_id          | int     |
    | event_date       | date    |
    | event_type       | varchar |
    | plan_name        | varchar |
    | monthly_amount   | decimal |

    event_id is the unique identifier for this table. event_type can be start, upgrade, downgrade, or cancel. plan_name can be basic, standard, premium, or NULL (when event_type is cancel). monthly_amount represents the monthly subscription cost after this event. For cancel events, monthly_amount is 0.

    Write a solution to Find Churn Risk Customers - users who show warning signs before churning. A user is considered churn risk customer if they meet ALL the following criteria:

    - Currently have an active subscription (their last event is not cancel).
    - Have performed at least one downgrade in their subscription history.
    - Their current plan revenue is less than 50% of their historical maximum plan revenue.
    - Have been a subscriber for at least 60 days.

    Return the result table ordered by days_as_subscriber in descending order, then by user_id in ascending order.
    """)
    return


@app.cell
def _():
    """
    WITH churn_info AS (
        SELECT
            user_id,
            FIRST_VALUE(event_date) OVER (PARTITION BY user_id ORDER BY event_date) AS first_login,
            FIRST_VALUE(plan_name) OVER (PARTITION BY user_id ORDER BY event_date DESC) AS current_plan,
            FIRST_VALUE(monthly_amount) OVER (PARTITION BY user_id ORDER BY event_date DESC) AS current_monthly_amount,
            FIRST_VALUE(event_date) OVER (PARTITION BY user_id order by event_date DESC) AS last_ogin,
            COUNT(*) FILTER (WHERE event_type ='downgrade') OVER (PARTITION BY user_id) AS cnt_upgrade,
            COUNT(*) FILTER (WHERE event_type ='cancel') OVER (PARTITION BY user_id) AS cnt_cancel,
            ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY event_date DESC) AS rn,
            MAX(monthly_amount) OVER (PARTITION BY user_id) AS max_historical_amount
        FROM
            subscription_events
    )
    SELECT
        user_id,
        current_plan,
        current_monthly_amount,
        max_historical_amount,
        last_ogin - first_login AS days_as_subscriber
    FROM
        churn_info
    WHERE
        rn=1
            AND cnt_upgrade > 0
            AND cnt_cancel = 0
            AND last_ogin - first_login >=60
            AND current_monthly_amount < 0.5 * max_historical_amount
    ORDER BY
        5 DESC, 1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_churn_risk_customers(
        subscription_events: pd.DataFrame,
    ) -> pd.DataFrame:
        df = subscription_events.copy()
        df["event_date"] = pd.to_datetime(df["event_date"])
        df = (
            df.groupby("user_id")
            .agg(
                latest_event=("event_type", "last"),
                has_downgrade=("event_type", lambda x: "downgrade" in x.values),
                current_monthly_amount=("monthly_amount", "last"),
                max_historical_amount=("monthly_amount", "max"),
                days_as_subscriber=(
                    "event_date",
                    lambda x: (x.max() - x.min()).days,
                ),
                current_plan=("plan_name", "last"),
            )
            .reset_index()
        )
        df = df[
            (df["latest_event"] != "cancel")
            & (df["has_downgrade"] == True)
            & (df["current_monthly_amount"] / df["max_historical_amount"] < 0.5)
            & (df["days_as_subscriber"] >= 60)
        ][
            [
                "user_id",
                "current_plan",
                "current_monthly_amount",
                "max_historical_amount",
                "days_as_subscriber",
            ]
        ]
        df.sort_values(
            ["days_as_subscriber", "user_id"],
            ascending=[False, True],
            inplace=True,
        )
        return df
    return


if __name__ == "__main__":
    app.run()
