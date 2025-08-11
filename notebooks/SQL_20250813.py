import marimo

__generated_with = "0.14.16"
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
            "/notebooks/SQL_20250812.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250814.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


if __name__ == "__main__":
    app.run()
