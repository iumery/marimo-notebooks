import marimo

__generated_with = "0.17.4"
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
            "/notebooks/SQL_20251105.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251107.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3059

    Table: Emails

    | Column Name | Type    |
    |-------------|---------|
    | id          | int     |
    | email       | varchar |

    id is the primary key (column with unique values) for this table. Each row of this table contains an email. The emails will not contain uppercase letters.

    Write a solution to find all unique email domains and count the number of individuals associated with each domain. Consider only those domains that end with .com.

    Return the result table orderd by email domains in ascending order.
    """)
    return


@app.cell
def _():
    """
    SELECT
        SPLIT_PART(email, '@', 2) AS email_domain,
        COUNT(1) AS count
    FROM
        Emails
    WHERE
        email ILIKE '%.com'
    GROUP BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_unique_email_domains(emails: pd.DataFrame) -> pd.DataFrame:
        df = emails[emails["email"].str.endswith(".com")]["email"].str.split(
            "@", expand=True
        )
        df["email_domain"] = df[[1]]
        df = df.groupby("email_domain")[0].count().reset_index(name="count")
        df.sort_values("email_domain", inplace=True)
        return df
    return


if __name__ == "__main__":
    app.run()
