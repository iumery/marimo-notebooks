import marimo

__generated_with = "0.13.6"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    nav_menu_1 = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
        },
        orientation="vertical",
    )
    nav_menu_1
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 1.pdf",
        width="100%",
        height="75vh",
    )
    return


@app.cell(column=1)
def _(mo):
    nav_menu_2 = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
        },
        orientation="vertical",
    )
    nav_menu_2
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 2.pdf",
        width="100%",
        height="75vh",
    )
    return


@app.cell(column=2)
def _(mo):
    nav_menu_3 = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
        },
        orientation="vertical",
    )
    nav_menu_3
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 3.pdf",
        width="100%",
        height="75vh",
    )
    return


@app.cell(column=3)
def _(mo):
    nav_menu_4 = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
        },
        orientation="vertical",
    )
    nav_menu_4
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 4.pdf",
        width="100%",
        height="75vh",
    )
    return


@app.cell(column=4)
def _(mo):
    nav_menu_5 = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
        },
        orientation="vertical",
    )
    nav_menu_5
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 5.pdf",
        width="100%",
        height="75vh",
    )
    return


@app.cell(column=5)
def _(mo):
    nav_menu_6 = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
        },
        orientation="vertical",
    )
    nav_menu_6
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 6.pdf",
        width="100%",
        height="75vh",
    )
    return


@app.cell(column=6)
def _(mo):
    nav_menu_7 = mo.nav_menu(
        {
            "/index.html": f"{mo.icon('lucide:home')} Home",
        },
        orientation="vertical",
    )
    nav_menu_7
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Quiz 7.pdf",
        width="100%",
        height="75vh",
    )
    return


if __name__ == "__main__":
    app.run()
