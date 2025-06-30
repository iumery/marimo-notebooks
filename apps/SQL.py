import marimo

__generated_with = "0.14.8"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    nav_menu = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
        },
        orientation="vertical",
    )
    nav_menu
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # SQL Practice with the DVDRental Dataset

    As part of my ongoing effort to stay sharp in SQL and relational database design, I’ve been regularly solving practice problems using the DVDRental sample database, a widely used dataset that simulates the operations of a DVD rental store. It offers enough complexity to reflect real-world schemas, including foreign keys, many-to-many relationships, and temporal fields.

    You can find the dataset [here](https://neon.com/postgresql/postgresql-getting-started/postgresql-sample-database). The goal is to strengthen both query writing and data reasoning, with each challenge grounded in a realistic business scenario. All queries are written in PostgreSQL, but should be easily adapted to other SQL dialects.
    """
    )
    return


if __name__ == "__main__":
    app.run()
