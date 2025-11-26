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
            "/notebooks/SQL_20251124.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251126.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3172

    Table: emails

    | Column Name | Type     |
    |-------------|----------|
    | email_id    | int      |
    | user_id     | int      |
    | signup_date | datetime |

    (email_id, user_id) is the primary key (combination of columns with unique values) for this table. Each row of this table contains the email ID, user ID, and signup date.

    Table: texts

    | Column Name   | Type     |
    |---------------|----------|
    | text_id       | int      |
    | email_id      | int      |
    | signup_action | enum     |
    | action_date   | datetime |

    (text_id, email_id) is the primary key (combination of columns with unique values) for this table. signup_action is an enum type of ('Verified', 'Not Verified'). Each row of this table contains the text ID, email ID, signup action, and action date.

    Write a Solution to find the user IDs of those who verified their sign-up on the second day.

    Return the result table ordered by user_id in ascending order.
    """)
    return


@app.cell
def _():
    """
    SELECT DISTINCT
        user_id
    FROM
        emails e
            JOIN texts t ON e.email_id = t.email_id
                AND e.signup_date::DATE + INTERVAL '1 day' = t.action_date::DATE
    WHERE
        signup_action = 'Verified'
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_second_day_signups(
        emails: pd.DataFrame, texts: pd.DataFrame
    ) -> pd.DataFrame:
        df_emails = emails.copy()
        df_emails["action_date"] = (
            df_emails["signup_date"] + pd.Timedelta(1, unit="D")
        ).dt.date
        df_texts = texts.copy()
        df_texts["action_date"] = df_texts["action_date"].dt.date
        df = pd.merge(df_emails, df_texts, on=["email_id", "action_date"])
        df = (
            df.query("signup_action == 'Verified'")[["user_id"]]
            .drop_duplicates()
            .sort_values("user_id")
        )
        return df
    return


if __name__ == "__main__":
    app.run()
