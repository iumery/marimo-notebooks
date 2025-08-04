import marimo

__generated_with = "0.14.10"
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
            "/notebooks/SQL_20250801.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250803.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## LeetCode 3451

    Table:  logs

    | Column Name | Type    |
    |-------------|---------|
    | log_id      | int     |
    | ip          | varchar |
    | status_code | int     |

    `log_id` is the unique key for this table. Each row contains server access log information including IP address and HTTP status code. Write a solution to find invalid IP addresses. An IPv4 address is invalid if it meets any of these conditions:

    - Contains numbers greater than 255 in any octet
    - Has leading zeros in any octet (like 01.02.03.04)
    - Has less or more than 4 octets

    Return the result table ordered by `invalid_count`, `ip` in descending order respectively. 
    """
    )
    return


@app.cell
def _():
    """
    WITH octet_info AS (
        SELECT
            log_id,
            UNNEST(STRING_TO_ARRAY(ip, '.')) AS octet,
            ip
        FROM
            logs
    ),
    octet_invalid_info AS (
        SELECT
            log_id,
            ip,
            CASE
                WHEN CAST(octet AS INT) > 255 THEN 1
                WHEN octet LIKE '0%' THEN 1
                ELSE 0
            END AS invalid
        FROM
            octet_info
    ),
    octet_grouped AS (
        SELECT
            log_id,
            ip
        FROM
            octet_invalid_info
        GROUP BY
            1, 2
        HAVING
            COUNT(*) <> 4
            OR
            MAX(invalid) = 1
    )
    SELECT
        ip,
        COUNT(*) AS invalid_count
    FROM
        octet_grouped
    GROUP BY
        1
    ORDER BY
        2 DESC,
        1 DESC;
    """
    return


if __name__ == "__main__":
    app.run()
