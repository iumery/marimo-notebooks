import marimo

__generated_with = "0.16.5"
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
            "/notebooks/SQL_20251030.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251103.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3055

    Table: Fraud

    | Column Name | Type    |
    |-------------|---------|
    | policy_id   | int     |
    | state       | varchar |
    | fraud_score | int     |

    policy_id is column of unique values for this table. This table contains policy id, state, and fraud score.The Leetcode Insurance Corp has developed an ML-driven predictive model to detect the likelihood of fraudulent claims. Consequently, they allocate their most seasoned claim adjusters to address the top 5% of claims flagged by this model.

    Write a solution to find the top 5 percentile of claims from each state.

    Return the result table ordered by state in ascending order, fraud_score in descending order, and policy_id in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH pct_rank_info AS (
        SELECT
            policy_id,
            state,
            fraud_score,
            PERCENT_RANK() OVER (PARTITION BY state ORDER BY fraud_score DESC) AS pct_rank
        FROM
            Fraud
    )
    SELECT
        policy_id,
        state,
        fraud_score
    FROM
        pct_rank_info
    WHERE
        pct_rank <= 0.05
    ORDER BY
        2, 3 DESC, 1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def top_percentile_fraud(fraud: pd.DataFrame) -> pd.DataFrame:
        df = fraud.copy()
        df["pct_rank"] = df.groupby("state")["fraud_score"].rank("dense", pct=True)
        df = (
            df.query("pct_rank>=0.95")
            .drop(columns=["pct_rank"])
            .sort_values(
                ["state", "fraud_score", "policy_id"],
                ascending=[True, False, True],
            )
        )
        return df

    return


if __name__ == "__main__":
    app.run()
