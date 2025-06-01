import marimo

__generated_with = "0.13.15"
app = marimo.App(width="columns")


@app.cell(column=0)
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
    return (nav_menu,)


@app.cell
def _(mo):
    mo.pdf(
        src="public/Exam 1.pdf",
        width="100%",
        height="75vh",
    )
    return


@app.cell(column=1)
def _(nav_menu):
    nav_menu
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Exam 2.pdf",
        width="100%",
        height="75vh",
    )
    return


@app.cell(column=2)
def _(nav_menu):
    nav_menu
    return


@app.cell
def _(mo):
    mo.pdf(
        src="public/Exam 3.pdf",
        width="100%",
        height="75vh",
    )
    return


if __name__ == "__main__":
    app.run()
