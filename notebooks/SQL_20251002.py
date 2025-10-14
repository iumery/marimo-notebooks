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
            "/notebooks/SQL_20251001.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251003.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2820

    Table: Votes

    | Column Name | Type    | 
    |-------------|---------| 
    | voter       | varchar | 
    | candidate   | varchar |

    (voter, candidate) is the primary key (combination of unique values) for this table. Each row of this table contains name of the voter and their candidate. 

    The election is conducted in a city where everyone can vote for one or more candidates or choose not to vote. Each person has 1 vote so if they vote for multiple candidates, their vote gets equally split across them. For example, if a person votes for 2 candidates, these candidates receive an equivalent of 0.5 votes each.

    Write a solution to find candidate who got the most votes and won the election. Output the name of the candidate or If multiple candidates have an equal number of votes, display the names of all of them.

    Return the result table ordered by candidate in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    WITH vote_with_weight AS (
        SELECT
            voter,
            candidate,
            1.0 / (COUNT(1) OVER (PARTITION BY voter)) AS weighted_vote
        FROM
            Votes
        WHERE
            candidate IS NOT NULL
    )
    SELECT
        candidate
    FROM
        vote_with_weight
    GROUP BY
        1
    HAVING
        SUM(weighted_vote) = (
            SELECT
                SUM(weighted_vote)
            FROM
                vote_with_weight
            GROUP BY
                candidate
            ORDER BY
                1 DESC
            LIMIT
                1
        )
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd

    def get_election_results(votes: pd.DataFrame) -> pd.DataFrame:
        df = votes.dropna()
        df["vote_weight"] = 1.0 / df.groupby("voter").transform("count")
        df = df.groupby("candidate", as_index=False)["vote_weight"].sum()
        df["rank"] = df["vote_weight"].rank(method="min", ascending=False)
        df = df[df["rank"] == 1][["candidate"]].sort_values("candidate")
        return df

    return


if __name__ == "__main__":
    app.run()
