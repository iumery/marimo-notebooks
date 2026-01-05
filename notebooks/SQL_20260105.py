import marimo

__generated_with = "0.18.4"
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
            "/notebooks/SQL_20251216.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20260106.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3793

    Table: prompts

    | Column Name | Type    |
    |-------------|---------|
    | user_id     | int     |
    | prompt      | varchar |
    | tokens      | int     |

    (user_id, prompt) is the primary key (unique value) for this table. Each row represents a prompt submitted by a user to an AI system along with the number of tokens consumed. Write a solution to analyze AI prompt usage patterns based on the following requirements:

    - For each user, calculate the total number of prompts they have submitted.
    - For each user, calculate the average tokens used per prompt (Rounded to 2 decimal places).
    - Only include users who have submitted at least 3 prompts.
    - Only include users who have submitted at least one prompt with tokens greater than their own average token usage.

    Return the result table ordered by average tokens in descending order, and then by user_id in ascending order.
    """)
    return


@app.cell
def _():
    """
    SELECT
        user_id,
        COUNT(prompt) AS prompt_count,
        ROUND(AVG(tokens), 2) AS avg_tokens
    FROM
        prompts
    GROUP BY
        1
    HAVING
        COUNT(prompt) >= 3
            AND
                MAX(tokens) > AVG(tokens)
    ORDER BY
        3 DESC, 1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_users_with_high_tokens(prompts: pd.DataFrame) -> pd.DataFrame:
        df = prompts.groupby("user_id", as_index=False).agg(
            max_tokens=("tokens", "max"),
            avg_tokens=("tokens", "mean"),
            prompt_count=("prompt", "count"),
        )
        df = df.query("max_tokens > avg_tokens").query("prompt_count >= 3")
        df["avg_tokens"] = df["avg_tokens"].round(2)
        df = df[["user_id", "prompt_count", "avg_tokens"]]
        df.sort_values(
            ["avg_tokens", "user_id"], ascending=[False, True], inplace=True
        )
        return df
    return


if __name__ == "__main__":
    app.run()
