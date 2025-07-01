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

    As part of my ongoing effort to stay sharp in SQL and relational database design, I’ve been regularly solving practice problems using a collection of rich, realistic datasets. These include:

    - [DVDRental](https://neon.com/postgresql/postgresql-getting-started/postgresql-sample-database) - a classic sample database known as Sakila for MySQL, that simulates the operations of a DVD rental store, with a schema complex enough to reflect real-world use cases like foreign keys, many-to-many relationships, and temporal fields.
    - [AACT](https://aact.ctti-clinicaltrials.org) (Aggregate Analysis of ClinicalTrials.gov) - a publicly available database that captures detailed metadata on clinical trials, offering opportunities to work with large-scale healthcare data, hierarchical designs, and nuanced filters.
    - [postgres_air](https://github.com/hettie-d/postgres_air?tab=readme-ov-file) - a realistic airline operations database with airport, flight, and delay data, ideal for exploring geospatial joins, network structures, and time-dependent patterns.

    The goal is to strengthen both query writing and data reasoning, with each challenge grounded in a realistic scenario. All queries are written in PostgreSQL, but should be easily adapted to other SQL dialects.
    """
    )
    return


if __name__ == "__main__":
    app.run()
