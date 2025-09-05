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
            "/notebooks/SQL_20250904.html": f"{mo.icon('lucide:arrow-big-left')} Last Day",
            "/notebooks/SQL_20250908.html": f"{mo.icon('lucide:arrow-big-right')} Next Day",
        },
        orientation="horizontal",
    )
    nav_menu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### LeetCode 2199

    Table: Keywords

    | Column Name | Type    |
    |-------------|---------|
    | topic_id    | int     |
    | word        | varchar |

    (topic_id, word) is the primary key (combination of columns with unique values) for this table. Each row of this table contains the id of a topic and a word that is used to express this topic. There may be more than one word to express the same topic and one word may be used to express multiple topics.

    Table: Posts

    | Column Name | Type    |
    |-------------|---------|
    | post_id     | int     |
    | content     | varchar |

    post_id is the primary key (column with unique values) for this table. Each row of this table contains the ID of a post and its content. Content will consist only of English letters and spaces.
 
    Leetcode has collected some posts from its social media website and is interested in finding the topics of each post. Each topic can be expressed by one or more keywords. If a keyword of a certain topic exists in the content of a post (case insensitive) then the post has this topic.

    Write a solution to find the topics of each post according to the following rules:

    - If the post does not have keywords from any topic, its topic should be "Ambiguous!".
    - If the post has at least one keyword of any topic, its topic should be a string of the IDs of its topics sorted in ascending order and separated by commas ','. The string should not contain duplicate IDs.

    Return the result table in any order.
    """
    )
    return


@app.cell
def _():
    """
    WITH words AS (
        SELECT
            post_id,
            UNNEST(STRING_TO_ARRAY(LOWER(content),' ')) AS content
        FROM
            Posts
    ),
    valid AS (
        SELECT DISTINCT
            post_id,
            topic_id
        FROM
            words w
                LEFT JOIN keywords kw ON w.content = LOWER(kw.word)
        ORDER BY
            1, 2
    ),
    combine AS (
        SELECT
            post_id,
            STRING_AGG(CAST(topic_id AS TEXT),',') AS topic
        FROM
            valid
        GROUP BY
            1
    )
    SELECT
        post_id,
        COALESCE(topic, 'Ambiguous!') AS topic
    FROM
        combine
    ORDER BY
        1
    """
    return


@app.cell
def _():
    import pandas as pd


    def find_topic(keywords: pd.DataFrame, posts: pd.DataFrame) -> pd.DataFrame:
        posts["content_word"] = posts["content"].str.lower().str.split()
        exploded_posts = posts.explode("content_word")
        keywords["word"] = keywords["word"].str.lower()
        common_words = pd.merge(
            exploded_posts,
            keywords,
            left_on="content_word",
            right_on="word",
            how="left",
        )
        grouped = (
            common_words.groupby("post_id")["topic_id"]
            .agg(lambda x: sorted(set(x.dropna())))
            .reset_index()
        )
        grouped["topic"] = grouped["topic_id"].transform(
            lambda x: ",".join(map(str, x)) if x else "Ambiguous!"
        )
        return grouped[["post_id", "topic"]]
    return


if __name__ == "__main__":
    app.run()
