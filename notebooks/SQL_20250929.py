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
            "/notebooks/SQL_20250926.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250930.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2738

    Table: Files

    | Column Name | Type    |
    |-- ----------|---------|
    | file_name   | varchar |
    | content     | text    |

    file_name is the column with unique values of this table. Each row contains file_name and the content of that file.

    Write a solution to find the number of files that have at least one occurrence of the words 'bull' and 'bear' as a standalone word, respectively, disregarding any instances where it appears without space on either side (e.g. 'bullet', 'bears', 'bull.', or 'bear' at the beginning or end of a sentence will not be considered) 

    Return the word 'bull' and 'bear' along with the corresponding number of occurrences in any order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT
        'bull' AS word,
        COUNT(1) FILTER (WHERE content LIKE '% bull %') AS count
    FROM
        Files
    UNION
    SELECT
        'bear' AS word,
        COUNT(1) FILTER (WHERE content LIKE '% bear %') AS count
    FROM
        Files
    """
    return


@app.cell
def _():
    import pandas as pd

    def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
        bullcnt = files["content"].str.contains(" bull ").sum()
        bearcnt = files["content"].str.contains(" bear ").sum()
        return pd.DataFrame({"word": ["bull", "bear"], "count": [bullcnt, bearcnt]})

    return


if __name__ == "__main__":
    app.run()
