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
            "/notebooks/SQL_20250905.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250909.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2252

    Table: Products

    | Column Name | Type    |
    |-------------|---------|
    | product_id  | int     |
    | store       | varchar |
    | price       | int     |

    (product_id, store) is the primary key (combination of columns with unique values) for this table. Each row of this table indicates the price of product_id in store. There will be at most 30 different stores in the table. price is the price of the product at this store.
 
    Important note: This problem targets those who have a good experience with SQL. If you are a beginner, we recommend that you skip it for now.

    Implement the procedure PivotProducts to reorganize the Products table so that each row has the id of one product and its price in each store. The price should be null if the product is not sold in a store. The columns of the table should contain each store and they should be sorted in lexicographical order.

    The procedure should return the table after reorganizing it.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    import pandas as pd


    def dynamic_pivoting_table(products: pd.DataFrame) -> pd.DataFrame:
        return products.pivot(
            index="product_id", columns="store", values="price"
        ).reset_index()
    return


if __name__ == "__main__":
    app.run()
