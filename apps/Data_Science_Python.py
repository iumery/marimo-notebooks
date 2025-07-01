import marimo

__generated_with = "0.14.9"
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
    # Machine Learning and Optimization in Python

    This collection of notebooks explores foundational topics in data processing, machine learning, and optimization using Python. The goal is to build a solid base for applied data science and optimization, emphasizing clarity, reproducibility, and problem-solving through code.
    """
    )
    return


if __name__ == "__main__":
    app.run()
