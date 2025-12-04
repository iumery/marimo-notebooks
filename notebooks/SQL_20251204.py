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
            "/notebooks/SQL_20251203.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251205.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LeetCode 3204

    Table: user_permissions

    | Column Name | Type    |
    |-------------|---------|
    | user_id     | int     |
    | permissions | int     |

    user_id is the primary key. Each row of this table contains the user ID and their permissions encoded as an integer. Consider that each bit in the permissions integer represents a different access level or feature that a user has.

    Write a solution to calculate the following:

    - common_perms: The access level granted to all users. This is computed using a bitwise AND operation on the permissions column.
    - any_perms: The access level granted to any user. This is computed using a bitwise OR operation on the permissions column.

    Return the result table in any order.
    """)
    return


@app.cell
def _():
    """
    SELECT
        BIT_AND(permissions) AS common_perms,
        BIT_OR(permissions) AS any_perms
    FROM
        user_permissions;
    """
    return


@app.cell
def _(reduce):
    import pandas as pd


    def analyze_permissions(user_permissions: pd.DataFrame) -> pd.DataFrame:
        common_perms = reduce(lambda x, y: x & y, user_permissions["permissions"])
        any_perms = reduce(lambda x, y: x | y, user_permissions["permissions"])
        df = pd.DataFrame(
            {
                "common_perms": [common_perms],
                "any_perms": [any_perms],
            }
        )
        return df
    return


if __name__ == "__main__":
    app.run()
