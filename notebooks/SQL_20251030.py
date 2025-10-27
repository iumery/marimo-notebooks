import marimo

__generated_with = "0.16.5"
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
            "/notebooks/SQL_20251029.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20251031.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 3054

    Table: Tree

    | Column Name | Type | 
    |-------------|------|
    | N           | int  | 
    | P           | int  |

    N is the column of unique values for this table. Each row includes N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.

    Write a solution to find the node type of the Binary Tree. Output one of the following for each node:

    - Root: if the node is the root node.
    - Leaf: if the node is the leaf node.
    - Inner: if the node is neither root nor leaf node.

    Return the result table ordered by node value in ascending order.
    """
    )
    return


@app.cell
def _():
    """
    SELECT DISTINCT
        t1.N,
        CASE
            WHEN t1.P IS NULL THEN 'Root'
            WHEN t2.P IS NULL THEN 'Leaf'
            ELSE 'Inner'
        END AS Type
    FROM
        Tree t1
            LEFT JOIN Tree t2 ON t1.N = t2.P
    ORDER BY
        1;
    """
    return


@app.cell
def _():
    import pandas as pd


    def binary_tree_nodes(tree: pd.DataFrame) -> pd.DataFrame:
        df = pd.merge(tree, tree, how="left", left_on="N", right_on="P")

        def check_nodes(row):
            if pd.isna(row["P_x"]):
                return "Root"
            elif pd.isna(row["P_y"]):
                return "Leaf"
            else:
                return "Inner"

        df["Type"] = df.agg(check_nodes, axis=1)
        df = (
            df[["N_x", "Type"]]
            .rename(columns={"N_x": "N"})
            .drop_duplicates()
            .sort_values("N")
        )
        return df
    return


if __name__ == "__main__":
    app.run()
