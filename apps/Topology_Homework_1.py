import marimo

__generated_with = "0.13.15"
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
    mo.md(r"""# Fall Semester Homework 01""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 1

    ### Exercise 1

    **Check the distributive laws for $\cup$ and $\cap$ and DeMorgan's laws**.

    1. $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$;
    2. $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$;
    3. $A - (B \cup C) = (A - B) \cap (A - C)$;
    4. $A - (B \cap C) = (A - B) \cup (A - C)$.

    Proof

    1. First statement: $$\begin{aligned}&\forall x, x \in A \cap (B \cup C)\\&\iff x \in A \text{ and } (x \in B \cup C)\\&\iff x \in A \text{ and } (x \in B \text{ or } x \in C)\\&\iff (x \in A \text{ and } x \in B) \text{ or } (x \in A \text{ and } x \in C)\\&\iff (x \in A \cap B) \text{ or } (x \in A \cap C)\\&\iff x \in (A \cap B) \cup (A \cap C)\end{aligned}$$
    2. Second statement: $$\begin{aligned}&\forall x, x \in A \cup (B \cap C)\\&\iff x \in A \text{ or } (x \in B \cap C)\\&\iff x \in A \text{ or } (x \in B \text{ and } x \in C)\\&\iff (x \in A \text{ or } x \in B) \text{ and } (x \in A \text{ or } x \in C)\\&\iff (x \in A \cup B) \text{ and } (x \in A \cup C)\\&\iff x \in (A \cup B) \cap (A \cup C)\end{aligned}$$
    3. Third statement: $$\begin{aligned} &\forall x, x \in A - (B \cup C)\\&\iff x \in A \text{ and } (x \notin B \cup C)\\&\iff x \in A \text{ and } (x \notin B \text{ and } x \notin C)\\&\iff (x \in A \text{ and } x \notin B) \text{ and } (x \in A \text{ and } x \notin C)\\  &\iff (x \in A - B) \text{ and } (x \in A - C)\\&\iff x \in (A - B) \cap (A - C)   \end{aligned}$$
    4. Fourth statement: $$\begin{aligned} &\forall x, x \in A - (B \cap C)\\&\iff x \in A \text{ and } (x \notin B \cap C)\\&\iff x \in A \text{ and } (x \notin B \text{ or } x \notin C)\\&\iff (x \in A \text{ and } x \notin B) \text{ or } (x \in A \text{ and } x \notin C)\\&\iff (x \in A - B) \text{ or } (x \in A - C)\\&\iff x \in (A - B) \cup (A - C)\end{aligned}$$

    And thus for all four statement above, ($x \in$ left $\iff$ $x \in$ right) $\implies$ (left $\subseteq$ right and right $\subseteq$ left) $\implies$ left = right.

    ### Exercise 5

    **Let $\mathcal{A}$ be a nonempty collection of sets. Determine the truth of each of the following statements and of their converses**:

    1. $x \in \bigcup\limits_{A \in \mathcal{A}}A \implies x \in A$ for least one $A \in \mathcal{A}$;
    2. $x \in \bigcup\limits_{A \in \mathcal{A}}A \implies x \in A$ for every $A \in \mathcal{A}$;
    3. $x \in \bigcap\limits_{A \in \mathcal{A}}A \implies x \in A$ for least one $A \in \mathcal{A}$;
    4. $x \in \bigcap\limits_{A \in \mathcal{A}}A \implies x \in A$ for every $A \in \mathcal{A}$.

    Proof

    1. The statement and its converse are both true by definition;
    2. Take $\mathcal{A} = \lbrace \lbrace 1 \rbrace , \lbrace 2 \rbrace \rbrace$ and take $x = 1$, then the statement is false as $x \notin \lbrace 2 \rbrace$. Conversely, if $x \in A$ for every $A \in \mathcal{A}$ and $\mathcal{A} \ne \varnothing$ then $x \in A$ for at least $A \in \mathcal{A}$, then by part 1, $x \in \bigcup\limits_{A \in \mathcal{A}}A$, thus the statement is true;
    3. By definition, $x \in \bigcap\limits_{A \in \mathcal{A}}A \implies x \in A$ for every $A \in \mathcal{A} \implies x \in A$ for at least $A \in \mathcal{A}$ (again since $\mathcal{A} \ne \varnothing$), thus the statement is true. Conversely, take $\mathcal{A} = \lbrace \lbrace 1 \rbrace , \lbrace 2 \rbrace \rbrace$ and take $x = 1$, then the statement is false as $x \notin \lbrace 1 \rbrace \cap \lbrace 2 \rbrace = \varnothing$;
    4. Both true by definition.

    ### Exercise 10

    **Let $\mathbb{R}$ denote the set of real numbers. For each of the following subsets of $\mathbb{R} \times \mathbb{R}$, determine whether it is equal to the Cartesian product of two subsets of $\mathbb{R}$**.

    1. $\lbrace (x, y) | x \text{ is an integer} \rbrace$;
    2. $\lbrace (x, y) | 0 < y \le 1 \rbrace$;
    3. $\lbrace (x, y) | y > x \rbrace$;
    4. $\lbrace (x, y) | x \text{ is not an integer and }y \text{ is an integer} \rbrace$;
    5. $\lbrace (x, y) | x^{2} + y^{2} < 1 \rbrace$.

    Solution

    1. $= \mathbb{Z} \times \mathbb{R}$ as by construction, every ordered pair $(x, y)$ where $x \in \mathbb{Z}$ and $y \in \mathbb{R}$ is in the above set;
    2. $= \mathbb{R} \times (0,1]$;
    3. Suppose it is equal to the Cartesian product of two subsets $A,B \subseteq \mathbb{R}$. Let $a<b<c$ and $a, b, c \in \mathbb{R}$, then $(a, b)$ is in the set (thus $b \in B$) and $(b, c)$ is in the set (thus $b \in A$). Then by definition of Cartesian product, $(b, b)$ is in the set, which is a contradiction as it is not true that $b > b$. Thus this set cannot equal to the Cartesian product of two subsets of $\mathbb{R}$;
    4. $= (\mathbb{R} - \mathbb{Z}) \times \mathbb{Z}$;
    5. $(0.9, 0.1)$ is in the set as $0.9 \cdot 0.9 + 0.1 \cdot 0.1 < 1$ and $(0.1, 0.9)$ also in the set for the same reason. If this is a Cartesian product then $(0.9, 0.9)$ is in the set, which is not true as $0.9 \cdot 0.9 + 0.9 \cdot 0.9 > 1$. Thus this set cannot equal to the Cartesian product of two subsets of $\mathbb{R}$.

    ## Section 2

    ### Exercise 1

    **Let $f: A \rightarrow B$. Let $A_0 \subseteq A$ and $B_0 \subseteq B$**.

    1. **Show that $A_0 \subseteq f^{-1}(f(A_0))$ and that equality holds if $f$ is injective**;
    2. **Show that $f(f^{-1}(B_0)) \subseteq B_0$ and that equality holds if $f$ is surjective**.

    Proof

    1. Suppose $x \in A_0$, then $f(x) \in f(A_0)$, by definition, $f^{-1}(f(A_0))$ $= \lbrace x | f(x) \in f(A_0) \rbrace$, thus $x \in f^{-1}(f(A_0))$. Thus $A_0 \subseteq f^{-1}(f(A_0))$. Suppose $x \in f^{-1}(f(A_0)) = \lbrace a | f(a) \in f(A_0) \rbrace$. By definition, $\forall b \in f(A_0), \exists a \in A_0$ such that $b = f(a)$. Since $f$ is injective, if $f(a') = f(a) \in f(A_0)$, then $a' = a \in A_0$, thus $x \in A_0$, and thus $f^{-1}(f(A_0)) \subseteq A_0$ and equality holds;
    2. Suppose $x \in f(f^{-1}(B_0))$, then by definition, $x \in \lbrace b | b=f(a)$ for at least one $a \in f^{-1}(B_0) \rbrace = \lbrace b | b=f(a)$ for at least one $a \in \lbrace a_0 | f(a_0) \in B_0 \rbrace \rbrace$, i.e. for each $x$, $\exists a$ such that $x (= b) = f(a) \in B_0$, thus $f(f^{-1}(B_0)) \subseteq B_0$. Suppose $x \in B_0$ and $f$ surjective, then $\exists a \in A$ such that $f(a) = x \implies a \in f^{-1}(x)$, thus $x = f(a) \subseteq f(f^{-1}(x)) \subseteq f(f^{-1}(B_0))$, thus $B_0 \subseteq f(f^{-1}(B_0))$ and equality holds.

    ### Exercise 2

    **Let $f: A \rightarrow B$ and let $A_i \subseteq A$ and $B_i \subseteq B$ for $i = 0$ and $i = 1$. Show that $f^{-1}$ preserves inclusions, unions, intersections, and differences of sets. Show that $f$ preserves inclusions and unions only**:

    1. $B_0 \subseteq B_1 \implies f^{-1}(B_0) \subseteq f^{-1}(B_1)$;
    2. $f^{-1}(B_0 \cup B_1) = f^{-1}(B_0) \cup f^{-1}(B_1)$;
    3. $f^{-1}(B_0 \cap B_1) = f^{-1}(B_0) \cap f^{-1}(B_1)$;
    4. $f^{-1}(B_0 - B_1) = f^{-1}(B_0) - f^{-1}(B_1)$;
    5. $A_0 \subseteq A_1 \implies f(A_0) \subseteq f(A_1)$;
    6. $f(A_0 \cup A_1) = f(A_0) \cup f(A_1)$;
    7. **$f(A_0 \cap A_1) \subseteq f(A_0) \cap f(A_1)$; show that equality holds if $f$ is injective**;
    8. **$f(A_0 - A_1) \supseteq f(A_0) - f(A_1)$; show that equality holds if $f$ is injective**.

    Proof

    1. By definition, $f^{-1}(B_0) = \lbrace a | f(a) \in B_0 \rbrace$. Thus for any $a \in f^{-1}(B_0)$, $f(a) \in B_0 \subseteq B_1$, thus $f(a) \in B_1$, thus $a \in \lbrace a | f(a) \in B_1 \rbrace = f^{-1}(B_1)$;
    2. $f^{-1}(B_0 \cup B_1)$ $= \lbrace a | f(a) \in B_0 \cup B_1 \rbrace$ $= \lbrace a | f(a) \in B_0 \text{ or } f(a) \in B_1 \rbrace$ $= \lbrace a | f(a) \in B_0 \rbrace \cup \lbrace a | f(a) \in B_1 \rbrace$ $= f^{-1}(B_0) \cup f^{-1}(B_1)$;
    3. $f^{-1}(B_0 \cap B_1)$ $= \lbrace a | f(a) \in B_0 \cap B_1 \rbrace$ $= \lbrace a | f(a) \in B_0 \text{ and } f(a) \in B_1 \rbrace$ $= \lbrace a | f(a) \in B_0 \rbrace \cap \lbrace a | f(a) \in B_1 \rbrace$ $= f^{-1}(B_0) \cap f^{-1}(B_1)$;
    4. $f^{-1}(B_0 - B_1)$ $= \lbrace a | f(a) \in B_0 - B_1 \rbrace$ $= \lbrace a | f(a) \in B_0 \text{ and } f(a) \notin B_1 \rbrace$ $= \lbrace a | f(a) \in B_0 \rbrace - \lbrace a | f(a) \in B_1 \rbrace$ $= f^{-1}(B_0) - f^{-1}(B_1)$;
    5. Suppose $b_0 \in f(A_0)$ $= \lbrace b | b = f(a)$ for at least one $a \in A_0 \rbrace$, then $b_0 = f(a)$ for at least one $a \in A_0$. Since $A_0 \subseteq A_1$, $a \in A_1$, thus $b_0 = f(a)$ for (at least)one $a \in A_1$ as well. Then by definition $b_0 \in f(A_1)$;
    6. $f(A_0 \cup A_1) = \lbrace b | b = f(a)$ for at least one $a \in A_0 \cup A_1 \rbrace = \lbrace b | b = f(a)$ for at least one $a \in A_0$ or $a \in A_1 \rbrace = \lbrace b | b = f(a)$ for at least one $a \in A_0 \rbrace \cup \lbrace b | b = f(a)$ for at least one $a \in A_1 \rbrace = f(A_0) \cup f(A_1)$;
    7. $f(A_0 \cap A_1) = \lbrace b | b = f(a)$ for at least one $a \in A_0 \cap A_1 \rbrace = \lbrace b | b = f(a)$ for at least one $a \in A_0$ and $a \in A_1 \rbrace = \lbrace b | b = f(a_0)$ for at least one $a_0 \in A_0 \rbrace \cap \lbrace b | b = f(a_0)$ for at least the same $a_0 \in A_1 \rbrace \subseteq \lbrace b | b = f(a_0)$ for at least one $a_0 \in A_0 \rbrace \cap \lbrace b | b = f(a_1)$ for at least one $a_1 \in A_1 \rbrace = f(A_0) \cap f(A_1)$. If $f$ is injective, then $b = f(a_0) = f(a_1) \implies a_0 = a_1$, we can thus substitute all $a_1$ by $a_0$ and equality holds;
    8. $f(A_0) - f(A_1) = \lbrace b | b = f(a_0)$ for at least one $a_0 \in A_0 \rbrace - \lbrace b | b = f(a_1)$ for at least one $a_1 \in A_1 \rbrace = \lbrace b | b = f(a_0)$ for at least one $a_0 \in A_0$ and $b \ne f(a_1)$ for all $a_1 \in A_1 \rbrace = \lbrace b | b = f(a)$ for at least one $a \in A_0 - A_1 \rbrace - \lbrace b | b = f(a)$ for at least one $a \in A_0 - A_1$ and for at least one $a \in A_1 \rbrace \subseteq \lbrace b | b = f(a)$ for at least one $a \in A_0 - A_1 \rbrace = f(A_0 - A_1)$. If $f$ is injective, then $f(a') = f(a) \implies a' = a$, thus $a \in A_0 - A_1 \implies a \notin A_1$ thus $\lbrace b | b = f(a)$ for at least one $a \in A_0 - A_1$ and for at least one $a \in A_1 \rbrace = \varnothing$, thus equality holds.

    ### Exercise 4

    **Let $f: A \rightarrow B$ and $g: B \rightarrow C$**.

    1. **If $C_0 \subseteq C$, show that $(g \circ f)^{-1}(C_0) = f^{-1}(g^{-1}(C_0))$**;
    2. **If $f$ and $g$ are injective, show that $g \circ f$ is injective**;
    3. **If $g \circ f$ is injective, what can you say about injectivity of $f$ and $g$**?
    4. **If $f$ and $g$ are surjective, show that $g \circ f$ is surjective**;
    5. **If $g \circ f$ is surjective, what can you say about surjectivity of $f$ and $g$**?
    6. **Summarize your answer to part 2 to 5 in the form of a theorem**.

    Proof

    1. By definition, $(g \circ f)^{-1}(C_0) = \lbrace a | g \circ f(a) \in C_0 \rbrace$. While $g^{-1}(C_0) = \lbrace b | g(b) \in C_0 \rbrace$, thus $f^{-1}(g^{-1}(C_0))$ $= f^{-1}(\lbrace b | g(b) \in C_0 \rbrace)$ $= \lbrace a | f(a) \in \lbrace b | g(b) \in C_0 \rbrace \rbrace$ $= \lbrace a | g(f(a)) \in C_0 \rbrace \rbrace$. Thus they are equal;
    2. For any $a, a' \in A$, if $g(f(a)) = g(f(a'))$, by injectivity of $g$, $f(a) = f(a')$, and by injectivity of $f$, $a = a'$, thus $g \circ f$ injective;
    3. If $f$ is not injective, then by definition, $\exists a \ne a' \in A$ with $f(a) = f(a')$. Then for such $a, a'$, $g(f(a)) = g(f(a'))$ and $a \ne a'$, which contradict the assumption that $g \circ f$ injective, thus $f$ is injective. The injectivity of $g$ does not matter;
    4. For any $c \in C$, since $g$ is surjective, $\exists b \in B$ such that $g(b) = c$, for such $b$, since $f$ is surjective, $\exists a \in A$ such that $f(a) = b$, thus $c = g(b) = g(f(a))$. Since $c$ is arbitrary, $g \circ f$ is surjective;
    5. If $g \circ f$ is surjective, then for each $c' \in C$, $c' = g \circ f(a')$ for some $a' \in A$. By the definition of a function, $\exists b \in B$ such that $f(a) = b, \forall a \in A$. Thus for the above $c'$ and $a'$, pick $b'$ such that $f(a') = b'$. Then $c' = g(f(a')) = g(b')$ for some $b' \in B$. Since $c'$ is arbitrary, $g$ is surjective;
    6. Let $f: A \rightarrow B$ and $g: B \rightarrow C$ be functions, then:
    	1. If $f$ and $g$ are injective, so is $g \circ f$;
    	2. If $f$ and $g$ are surjective, so is $g \circ f$;
    	3. If $g \circ f$ is injective, so is $f$;
    	4. If $g \circ f$ is surjective, so is $g$.

    ## Section 7

    ### Exercise 3

    **Let $X$ be the two-element set $\lbrace 0, 1 \rbrace$. Show there is a bijective correspondence between the set $\mathcal{P}(\mathbb{Z}_+)$ and the Cartesian product $X^{\omega}$**.

    Proof

    Define $g: \mathcal{P}(\mathbb{Z}_+) \rightarrow X^{\omega}$ as $g(A) = (x_i)$ such that $i \in \mathbb{Z}_+$ and $x_i = 1$ if and only if $i \in A$, otherwise $x_i = 0$. For example $g(\lbrace 1,3,5 \rbrace) = (1010100000 \cdots)$. Suppose $A = A' \in \mathcal{P}(\mathbb{Z}_+)$, then for each $i$, $g(A)_i =$ appearances of $i$ in $A$ = appearances of $i$ in $A'$ = $g(A')_i$, thus $g(A) = g(A')$, thus $g$ is well defined.

    Suppose $A, A' \in \mathcal{P}(\mathbb{Z}_+)$ and $g(A) = g(A') = (x_i)$, then for each $i$, by construction, if $i \in A$, then $x_i = 1$, then $i \in A'$, thus $A \subseteq A'$, similarly, $A' \subseteq A$ and thus they are equal. Thus $g$ is injective.

    For any $X' \in X^{\omega}$, $X' = (x'_i)$. Then for each $i$, construct a set $A'$ as: $A'$ contain $i$ if and only if $x'_i = 1$. Since $i \in \mathbb{Z}_+, \forall i$, we have $A' \subseteq \mathbb{Z}_+$ thus $A' \in \mathcal{P}(\mathbb{Z}_+)$. By construction $g(A') = X'$; since $X'$ is arbitrary, $g$ is surjective.

    ### Exercise 5

    **Determine, for each of the following sets, whether or not it is countable, Justify your answers**.

    1. **The set $A$ of all functions $f: \lbrace 0, 1 \rbrace \rightarrow \mathbb{Z_+}$**;
    2. **The set $B_n$ of all functions $f: \lbrace 1, \cdots, n \rbrace \rightarrow \mathbb{Z_+}$**;
    3. **The set $C = \bigcup\limits_{n \in \mathbb{Z}_+}B_n$**;
    4. **The set $D$ of all functions $f: \mathbb{Z_+} \rightarrow \mathbb{Z_+}$**;
    5. **The set $E$ of all functions $f: \mathbb{Z_+} \rightarrow \lbrace 0, 1 \rbrace$**;
    6. **The set $F$ of all functions $f: \mathbb{Z_+} \rightarrow \lbrace 0, 1 \rbrace$ that are 'eventually zero'**;
    7. **The set $G$ of all functions $f: \mathbb{Z_+} \rightarrow \mathbb{Z_+}$ that are eventually $1$**;
    8. **The set $H$ of all functions $f: \mathbb{Z_+} \rightarrow \mathbb{Z_+}$ that are eventually constant**;
    9. **The set $I$ of all two-element subsets of $\mathbb{Z}_+$**;
    10. **The set $J$ of all finite subsets of $\mathbb{Z}_+$**.

    Solution

    1. Consider the map send each $f \in A$ to $(f(0), f(1))$, this is a bijection from $A$ to $\mathbb{Z}_+^{2}$, we know $\mathbb{Z}_+^{2}$ is countable, thus $A$ countable;
    2. Similar with part 1, there is a bijection between $B$ and $\mathbb{Z}_+^{n}$ which is countable thus $B$ countable;
    3. By part 2, each $B_n$ is countable. $\mathbb{Z}_+$ is countable, and since a countable union of countable sets is countable, $C$ is countable;
    4. For any function $g: \mathbb{Z}_+ \rightarrow D$, denote $g(n) = (x_{n1},x_{n_2}, \cdots, x_{nm}, \cdots)$ where each $x_{ij} \in \mathbb{Z}_+$. Now for $x = (x_1, x_2, \cdots)$, set $x_i = x_{ii} + 1, \forall i$. Then $x \in D$ but $x \ne g(i), \forall i$. Thus $g$ cannot be surjective thus not bijective, $D$ is not countable;
    5. Similar with part 4, set $x_i = 1 - x_{ii}, \forall i$ and we have $E$ not countable (this is the same as the proof of the countability of $X^{\omega}$);
    6. Let $F_n$ be the set of all functions $f: \mathbb{Z_+} \rightarrow \lbrace 0, 1 \rbrace$ that are 'eventually zero' after $n$. Then $F = \bigcup\limits_{n \in \mathbb{Z}_+}F_n$. $F_1$ is trivially countable (and also $F_2$ is countable because of part 1 above). Suppose $F_n$ is countable, then $F_{n+1}$ takes all functions in $F_n$ and maps $n$ to either $0$ or $1$, thus there is a bijection between $F_{n+1}$ and the Cartesian product $F_n \times \lbrace 0, 1 \rbrace$ of two countable sets thus $F_{n+1}$ countable. Thus $F_n$ is countable for all $n$, thus $F$ is the union of countable many countable sets, thus countable;
    7. $G$ is a subset of $H$ below, since $H$ is countable, $G$ is countable;
    8. Let $H_n$ be the set of all functions $f: \mathbb{Z_+} \rightarrow \mathbb{Z_+}$ that are eventually constant after $n$. Then $H = \bigcup\limits_{n \in \mathbb{Z}_+}H_n$. $H_1$ is countable since it maps all $\mathbb{Z}_+$ to a constant number in $\mathbb{Z}_+$ thus there is a (identity) one-to-one correspondence between $H_1$ and $\mathbb{Z}_+$. Suppose $H_n$ is countable, then $H_{n+1}$ takes all functions in $H_n$ and maps $n$ to a constant in $\mathbb{Z}_+$, thus there is a bijection between $H_{n+1}$ and $H_n \times \mathbb{Z}_+$, thus $H_n$ countable for all $n$, and thus $H$ countable;
    9. $I$ is a subset of $J$ below, since $J$ is countable, $I$ is countable;
    10.	Let $J_n$ be the set of all subsets with $n$ elements of $\mathbb{Z}_+$. Then $J = \bigcup\limits_{n \in \mathbb{Z}_+}J_n + \varnothing$. For each $n$, an element of $J_n$ is a set of $n$ natural numbers, thus there is a bijection between $J_n$ and $\mathbb{Z}_+^{n}$, thus $J_n$ countable. Thus $J$ countable.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 02""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 3

    ### Exercise 1

    **Define two points $(x_0, y_0)$ and $(x_1, y_1)$ of the plane to be equivalent if $y_0 - x_0^2 = y_1 - x_1^2$. Check that this is an equivalence relation and describe the equivalence classes**.

    Proof

    Denote $\mathcal{R}$ with such relation.

    1. Clearly $y_0 - x_0^2 = y_0 - x_0^2$ thus $(x_0, y_0) \mathcal{R}(x_0, y_0)$ and reflexivity holds;
    2. If $(x_0, y_0) \mathcal{R}(x_1, y_1)$ then $y_0 - x_0^2 = y_1 - x_1^2$ thus $(x_1, y_1) \mathcal{R}(x_0, y_0)$ and symmetry holds;
    3. If $(x_0, y_0) \mathcal{R}(x_1, y_1)$ and $(x_1, y_1) \mathcal{R}(x_2, y_2)$ then $y_0 - x_0^2 = y_1 - x_1^2 = y_2 - x_2^2$ thus $(x_0, y_0) \mathcal{R}(x_2, y_2)$ and transitivity holds.

    Thus $\mathcal{R}$ is an equivalence relation.

    Let $f: \mathbb{R} \rightarrow \mathbb{R}$ given by $f(x) = x^2$, then two points $(x_0, y_0)$ and $(x_1, y_1)$ of the plane to be equivalent if $y_0 - f(x_0) = y_1 - f(x_1)$, so we can think each equivalence class as a 'slice' of the plane by the function $f$. I.e. geometrically in this case, all points lay on the curve $x^2$ form an equivalence class; all points lay on the curve $x^2 + c$ form an equivalence class, for each real constant $c$.

    ### Exercise 3

    **Here is a 'proof' that every relation $C$ that is both symmetric and transitive is also reflexive: 'Since $C$ is symmetric, $aCb \implies b Ca$. Since $C$ is transitive, $aCb$ and $bCa$ together imply $aCa$, as desired.' Find the flaw in this argument**.

    Solution

    To have the 'symmetric' step works we need to have some $b (\ne a)$ such that $aCb$, such $b$ does not have to exist.

    ### Exercise 6

    **Define a relation on the plane by setting $(x_0, y_0) < (x_1, y_1)$ if either $y_0 - x_0^2 < y_1 - x_1^2$, or $y_0 - x_0^2 = y_1 - x_1^2$ and $x_0 < x_1$. Show that this is an order relation the plane, and describe it geometrically**.

    Proof

    Denote $\mathcal{R}$ with such relation.

    1. $\forall (x_0, y_0) \ne (x_1, y_1)$, either:
    	1. $x_0 < x_1$ then:
    		1. If $y_0 - x_0^2 < y_1 - x_1^2$, then $(x_0, y_0) \mathcal{R}(x_1, y_1)$;
    		2. If $y_0 - x_0^2 = y_1 - x_1^2$, then $(x_0, y_0) \mathcal{R}(x_1, y_1)$;
    		3. If $y_0 - x_0^2 > y_1 - x_1^2$, then $y_1 - x_1^2 < y_0 - x_0^2$ thus $(x_1, y_1) \mathcal{R}(x_0, y_0)$;
    	2. $x_0 = x_1$ then:
    		1. If $y_0 - x_0^2 < y_1 - x_1^2$, then $(x_0, y_0) \mathcal{R}(x_1, y_1)$;
    		2. If $y_0 - x_0^2 > y_1 - x_1^2$, then $y_1 - x_1^2 < y_0 - x_0^2$ thus $(x_1, y_1) \mathcal{R}(x_0, y_0)$;
    	3. $x_1 < x_0$ then:
    		1. If $y_0 - x_0^2 < y_1 - x_1^2$, then $(x_0, y_0) \mathcal{R}(x_1, y_1)$;
    		2. If $y_0 - x_0^2 = y_1 - x_1^2$, then $(x_1, y_1) \mathcal{R}(x_0, y_0)$;
    		3. If $y_0 - x_0^2 > y_1 - x_1^2$, then $y_1 - x_1^2 < y_0 - x_0^2$ thus $(x_1, y_1) \mathcal{R}(x_0, y_0)$.
		
    		Thus comparability holds;
    2. Let $(x, y)$ be an arbitrary pair in the plane, then it is not true that $y - x^2 < y - x^2$ and $x < x$ thus $x \mathcal{R}x$ false and non-reflexivity holds;
    3. If $(x_0, y_0) < (x_1, y_1)$ and $(x_1, y_1) < (x_2, y_2)$ then either:
    	1. $y_0 - x_0^2 < y_1 - x_1^2$ and $y_1 - x_1^2 < y_2 - x_2^2$, thus $y_0 - x_0^2 < y_2 - x_2^2$ and $(x_0, y_0) \mathcal{R}(x_2, y_2)$;
    	2. $y_0 - x_0^2 < y_1 - x_1^2$ and $y_1 - x_1^2 = y_2 - x_2^2$ and $x_1 < x_2$ thus $y_0 - x_0^2 < y_2 - x_2^2$ and $(x_0, y_0) \mathcal{R}(x_2, y_2)$;
    	3. $y_0 - x_0^2 = y_1 - x_1^2$ and $x_0 < x_1$ and $y_1 - x_1^2 < y_2 - x_2^2$ thus $y_0 - x_0^2 < y_2 - x_2^2$ and $(x_0, y_0) \mathcal{R}(x_2, y_2)$;
    	4. $y_0 - x_0^2 = y_1 - x_1^2$ and $x_0 < x_1$ and $y_1 - x_1^2 = y_2 - x_2^2$ and $x_1 < x_2$ thus $y_0 - x_0^2 = y_2 - x_2^2$ and $x_0 < x_2$ and $(x_0, y_0) \mathcal{R}(x_2, y_2)$.
	
    	Thus transitivity holds.

    Thus $\mathcal{R}$ is an order relation.

    Similar with Exercise 1, a point $a$ in the plane is '$<$' a point $b$ if it lays 'below' the curve $x^2 + c$ that passes $b$, or it lays on the curve but 'to the left' of $b$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 03""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 13

    ### Exercise 1

    **Let $X$ be a topological space; let $A$ be a subset of $X$. Suppose that for each $x \in A$ there is an open set $U$ containing $x$ such that $U \subseteq A$. Show that $A$ is open in $X$**.

    Proof

    For each $x \in A$ let's choose one $U_x \subseteq A$ open set in $X$ contains $x$, and claim that $\bigcup\limits_{x \in A}U_x = A$.

    If $x \in \bigcup\limits_{x \in A}U_x$, then by definition $x \in U_{x'} \subseteq A$ for some $x'$, i.e. $\bigcup\limits_{x \in A}U_x \subseteq A$; If $x \in A$, then by construction it is contained in the $U_x$ we choose, thus it is in the union, i.e. $\bigcup\limits_{x \in A}U_x \supseteq A$. Thus $\bigcup\limits_{x \in A}U_x = A$, and since union of open sets is open, $A$ open in $X$.

    ### Exercise 3

    1. **Show that the collection $\tau_c$ given in Example 4 of Section 12 is a topology on the set $X$: Let $X$ be a set; let $\tau_c$ be the collection of all subsets $U$ of $X$ such that $X - U$ either is countable or is all of $X$**;
    2. **Is the collection $\tau_{\infty} = \lbrace U | X - U$ is infinite or empty or all of $X \rbrace$ a topology on $X$**?

    Proof

    1.   Follow the definition of a topology:
         1. $X - \varnothing$ is all of $X$ and $X - X = \varnothing$ is countable, thus $\varnothing, X \in \tau_c$;
         2. Let $\lbrace U_c \rbrace$ be a family of open sets in $X$ indexed by $c$. Then $X - \cup U_c = \cap (X - U_c)$. If $X - U_c = X, \forall c$, then $\cap (X - U_c) = X$ thus contained in $\tau_c$; otherwise $X - U_c$ countable for some $c$, thus their intersection must be a subset of this countable set thus countable, by definition it is contained in $\tau_c$;
         3. $X - \bigcap\limits_{c = 1}^{n}U_c = \bigcup\limits_{c = 1}^{n} (X - U_c)$ is union of countable many countable sets thus countable and thus contained in $\tau_c$. Thus by definition, $\tau_c$ is a topology;
    2.   Let's check if it satisfy the definition of a topology:
         1. $X - \varnothing$ is all of $X$ and $X - X = \varnothing$ is empty, thus $\varnothing, X \in \tau_{\infty}$;
         2. Say $X = \mathbb{R}, U_1 = (- \infty, 0) = \lbrace x \in \mathbb{R} | x < 0 \rbrace$, $U_2 = (0, + \infty) = \lbrace x \in \mathbb{R} | x > 0 \rbrace$, $X - U_1$ and $X - U_2$ are both infinite, thus $U_1, U_2 \in \tau_{\infty}$. However $X - U_1 \cup U_2$ $= \mathbb{R} - \lbrace x \in \mathbb{R} | x < 0 \text{ or } x > 0 \rbrace = \lbrace 0 \rbrace$ is not infinite, not empty, and not all of $X$. So union of open sets in $\tau_{\infty}$ may not be open, thus $\tau_{\infty}$ not a topology;
         3. Similarly take $U_1 = \mathbb{R}, U_2 = \lbrace 0 \rbrace$ then $U_1 \cap U_2 = \lbrace x \in \mathbb{R} | x < 0 \text{ or } x > 0 \rbrace$ and $X - U_1 \cap U_2 = \mathbb{R} - \lbrace x \in \mathbb{R} | x < 0 \text{ or } x > 0 \rbrace = \lbrace 0 \rbrace$. So intersection of finite open sets may not by open, thus $\tau_{\infty}$ not a topology.

    ### Exercise 4

    1. **If $\lbrace \tau_{\alpha} \rbrace$ is a family of topologies on $X$, show that $\cap \tau_{\alpha}$ is a topology on $X$**;
    2. **Let $\lbrace \tau_{\alpha} \rbrace$ be a family of topologies on $X$. Show that there is a unique smallest topology on $X$ containing all the collections $\tau_{\alpha}$, and a unique largest topology contained in all $\tau_{\alpha}$**;
    3. **If $X = \lbrace a, b, c \rbrace$, let $\tau_1 = \lbrace \varnothing, X, \lbrace a \rbrace, \lbrace a, b \rbrace \rbrace$ and $\tau_2 = \lbrace \varnothing, X, \lbrace a \rbrace, \lbrace b, c \rbrace \rbrace$. Find the smallest topology containing $\tau_1$ and $\tau_2$, and the largest topology contained in $\tau_1$ and $\tau_2$**.

    Proof

    1. Follow the definition of a topology:

    	1. $\varnothing \in \tau_{\alpha}, \forall \alpha$ since they are all topologies, thus $\varnothing \in \cap \tau_{\alpha}$; similar with $X$;
    	2. Let $\lbrace U_a \rbrace$ be a family of open sets in $X$ indexed by $a$. Then $U_a \in \cap \tau_{\alpha}$ for all $a$, which means $U_a \in \tau_{\alpha}$ for all $\alpha$, for all $a$. Thus for each $\alpha$, since $\tau_{\alpha}$ is a topology, $\cup U_a \in \tau_{\alpha}$, thus $\cup U_a \in \cap \tau_{\alpha}$;
    	3. Similarly for each $\alpha$, since $\tau_{\alpha}$ is a topology, $\bigcap\limits_{a = 1}^n U_a \in \tau_{\alpha}$ thus $\bigcap\limits_{a = 1}^n U_a \in \cap \tau_{\alpha}$.

    	Thus $\cap \tau_{\alpha}$ is a topology on $X$;

    2. Intuitively, the first topology should contain everything in the family, but 'no more' (however notice that, for example, $\lbrace \varnothing, X, \lbrace a \rbrace, \lbrace b \rbrace \rbrace$ is not a topology on a three elements set $X$, but $\lbrace \varnothing, X, \lbrace a \rbrace \rbrace$ and $\lbrace \varnothing, X, \lbrace b \rbrace \rbrace$ are. So it cannot be strictly 'no more', but no more than everything we already have, plus something else necessary to make the whole thing a well-defined topology); the second one should be contained in every member of the family, but no less.
    	So in some sense, they work like union and intersection in the usual sense, but it will be a bit harder to build the first one.

    	1. Unique smallest topology on $X$ containing all the collections $\tau_{\alpha}$:
    		So consider the union of open sets $\cup \tau_{\alpha}$, each of its element is a subset of $X$, and since $\tau_{\alpha}$ is a topology for all $\alpha$, $X$ itself is in the collection of open sets, thus the union is $X$. By definition, $\cup \tau_{\alpha}$ is a sub-basis for a topology on $X$. Denote the topology generated by this sub-basis as $\tau_s$ and claim that this is the unique smallest topology on $X$ containing all the collections $\tau_{\alpha}$.
    		By the book, $\mathcal{B}_s$ of all finite intersections of elements of $\cup \tau_{\alpha}$ is a basis for $\tau_s$.
    		Let $\mathcal{B}$ be a basis for an arbitrary $\tau_{\alpha}$.
    		Then for each $x \in X$ and $B \in \mathcal{B}$ containing $x$, by Lemma 13.1, $B \in \tau_{\alpha}$ thus $B \in \cup \tau_{\alpha}$, thus $B \in \mathcal{B}_s$ and take $B = B_s \in \mathcal{B}_s$ we have $x \in B_s \subseteq B$.
    		By Lemma 13.3, $\tau_s$ is finer than this arbitrary $\tau_{\alpha}$, thus it contains all $\tau_{\alpha}$.
    		Now suppose $\tau$ is a topology contains all $\tau_{\alpha}$.
    		Then for each $U = \cup B_s \in \tau_s$, by definition each $B_s$ is a finite intersection of elements of $\cup \tau_{\alpha}$, i.e. $B_s = \bigcap\limits_{i = 1}^{n} B_{s_i}$, with each $B_{s_i} \in \cup \tau_{\alpha}$, thus $B_{s_i} \in \tau_{\alpha} \subseteq \tau$ for some $\alpha$, thus $B_{s_i} \in \tau$. Since $\tau$ is a topology, $B_s$, the finite intersection is also in $\tau$, and $U$, the union is also in $\tau$. I.e. $\tau_s \subseteq \tau$. Thus $\tau_s$ is coarser than this arbitrary $\tau$, and we have $\tau_s$ is a smallest topology on $X$ containing all the collections $\tau_{\alpha}$.
    		Suppose $\tau_s$ and $\tau_s'$ are both smallest topology on $X$ containing all the collections $\tau_{\alpha}$, then $\tau_s \subseteq \tau_s'$ and $\tau_s' \subseteq \tau_s$ thus they are the same thing;
    	2. Unique largest topology contained in all $\tau_{\alpha}$:
    		Claim that the topology $\cap \tau_{\alpha}$ in (i). is the unique largest topology contained in all $\tau_{\alpha}$. Let's denote it $\tau_l$.
    		By construction it is contained in all $\tau_{\alpha}$.
    		Now suppose $\tau$ is a topology contained in all $\tau_{\alpha}$.
    		Then for any $U \in \tau$, $U \in \tau_{\alpha}, \forall \alpha$, thus $U \in \cap \tau_{\alpha} = \tau_l$. Thus $\tau_l$ is finer than this arbitrary $\tau$ and $\tau_l$ is a largest topology on $X$ contained in all $\tau_{\alpha}$.
    		Similarly suppose $\tau_l$ and $\tau_l'$ are both largest topology on $X$ contained in all $\tau_{\alpha}$, then $\tau_l \subseteq \tau_l'$ and $\tau_l' \subseteq \tau_l$ thus they are the same thing;
    3. Follow the above proof, we have $\tau_1 \cup \tau_2 = \lbrace \varnothing, X, \lbrace a \rbrace, \lbrace a, b \rbrace, \lbrace b, c \rbrace \rbrace$, $\mathcal{B}$ the finite intersection of the union is $\lbrace \varnothing, X, \lbrace a \rbrace, \lbrace b \rbrace, \lbrace a, b \rbrace, \lbrace b, c \rbrace \rbrace$, and finally $\tau_s$ is generated by $\mathcal{B}$ is $\lbrace \varnothing, X, \lbrace a \rbrace, \lbrace b \rbrace, \lbrace a, b \rbrace, \lbrace b, c \rbrace \rbrace$; $\tau_l = \tau_1 \cap \tau_2 = \lbrace \varnothing, X, \lbrace a \rbrace \rbrace$.

    ### Exercise 6

    **Show that the topologies of $\mathbb{R}_l$ and $\mathbb{R}_K$ are not comparable**.

    Proof

    Consider $B_l = [0, 1)$, a basis element for the topology of $\mathbb{R}_l$, and $x = 0$. Let $B_k$ be a basis element for the topology of $\mathbb{R}_k$ containing $x$. Then by definition it has the form $(a, b)$ or $(a, b) - K$. Since $B_k$ contains $0$, we have $a < 0 < b$. Consider $\frac{a}{2}$, since $\frac{a}{2} < 0$, it is not in $K$, but it is in the interval $(a, b)$, thus $\frac{a}{2} \in B_k$. Since it is negative, it is not in $B_l$. Thus $B_k$ is not contained in $B_l$. Thus topology of $\mathbb{R}_l$ is not finer than topology of $\mathbb{R}_k$.

    Now consider $B_k = (-1, 1) - K$, and again $x = 0$. Let $B_l$ be a basis element for the topology of $\mathbb{R}_l$ containing $x$. By definition it has the form $[a, b)$ and $a \le 0 < b$. If $b > 1/2$ then $1/2 \in B_l$ but $1/2 \in K$ thus $1/2 \notin B_k$. Otherwise $b = \frac{1}{1/b}> \frac{1}{\lceil \frac{1}{b} \rceil}>0$ where $\lceil \frac{1}{b} \rceil$ is the smallest integer greater than or equal to $\frac{1}{b}$. For example, $b = 0.003 = 1/(1/0.003) > 1/334 \approx 0.0029 > 0$. Notice that $\frac{1}{\lceil \frac{1}{b} \rceil} \in B_l$ but $\frac{1}{\lceil \frac{1}{b} \rceil} \in K$ thus $\frac{1}{\lceil \frac{1}{b} \rceil} \notin B_k$. Thus $B_l$ is not contained in $B_k$ and we have topology of $\mathbb{R}_k$ is not finer than topology of $\mathbb{R}_l$.

    We may conclude now that they are not comparable.

    ### Exercise 7

    **Consider the following topologies on $\mathbb{R}$**:

    1. $\tau_1 =$ **the standard topology**,
    2. $\tau_2 =$ **the topology of $\mathbb{R}_K$**,
    3. $\tau_3 =$ **the finite complement topology**,
    4. $\tau_4 =$ **the upper limit topology, having all sets $(a, b]$ as basis**,
    5. $\tau_5 =$ **the topology having all sets $(- \infty, a) = \lbrace x | x < a \rbrace$ as basis**.

    **Determine, for each of these topologies, which of the others it contains**.

    Solution

    1. $\tau_1 =$ the standard topology:
    	1. By the book, $\tau_2$ is strictly finer than $\tau_1$;
    	2. For each $U \in \tau_3$, by definition $\mathbb{R} - U$ is finite or $U = \mathbb{R}$. If $U = \mathbb{R}$, then $U \in \tau_1$; if else, $\mathbb{R} - U = \lbrace u_1, \dots, u_n \rbrace$, and $U = (- \infty, u_1) \cup (u_1, u_2) \cup \dots \cup (u_n, + \infty)$ $= \bigcup\limits_{i=0}^{\infty}(u_1-i-1, u_1-i) \cup (u_1, u_2) \cup \dots \cup \bigcup\limits_{j=0}^{\infty}(u_n+j, u_n+j+1)$, i.e. $U$ can be written in the form of union of intervals in the form $(a, b)$ thus again is in $\tau_1$. Thus $\tau_3 \subseteq \tau_1$.
    		On the other hand say $U = (0, 1) \in \tau_1$, then $\mathbb{R} - U$ is neither finite nor $\mathbb{R}$, thus $\tau_1$ is not contained in $\tau_3$.
    		Thus $\tau_1$ strictly finer than $\tau_3$;
    	3. $\tau_4$ is strictly finer than $\tau_1$ in the similar way as the lower limit topology does;
    	4. For each $B_5 \in \mathcal{B}_5$ containing $x$, $B_5$ is in the form $(- \infty, a)$ with $x < a$. Then $(x-1, a)$ is a basis element in the basis generates $\tau_1$ and it is a subset of $B_5$. By Lemma 13.3 $\tau_1$ is finer than $\tau_5$.
    		On the other hand consider $B_1 = (0, 1) \in \mathcal{B}_1$ containing, say, $x = 1/2$. Let $B_5 \in \mathcal{B}_5$ contains $x$, then it has the form $(- \infty, a)$ with $x < a$. Thus $0 \in B_5$ but $0 \notin B_1$, i.e. $\tau_1$ is not contained in $\tau_5$.
    		Thus $\tau_1$ strictly finer than $\tau_5$;
    2. $\tau_2 =$ the topology of $\mathbb{R}_K$:
    	1. By above $\tau_3 \subset \tau_1 \subset \tau_2$;
    	2. For each $B_2 \in \mathcal{B}_2$ containing $x$, $B_2 = (a, b)$ or $(a, b)-K$ with $a < x < b$. If $B_2 = (a, b)$ then $B_4 = (a, x] \in \mathcal{B}_4$ is a subset of $B_2$ containing $x$. If $B_2 = (a, b) - K$, if $x \le 0$ then again $(a, x] \in \mathcal{B}_4$ is a subset of $B_2$ containing $x$; if $0 < x < 1$, notice that $x \ne \frac{1}{n}, \forall n \in \mathbb{Z}_+$ otherwise it is in $K$. Thus $x_l = \frac{1}{\lceil 1/x \rceil} < \frac{1}{1/x} = x < \frac{1}{\lfloor 1/x \rfloor} = x_r$ where $\lceil 1/x \rceil$ is the smallest integer greater than $1/x$ and $\lfloor 1/x \rfloor$ is the largest integer smaller than $1/x$. Then $(\frac{x + x_l}{2}, \frac{x + x_r}{2}] \in \mathcal{B}_4$ contains $x$ and it is a subset of $B_2$; if $x > 1$, $(1, \frac{x + b}{2}]$ is the desired half-open interval. Thus $\tau_2 \subseteq \tau_4$.
    		On the other hand, consider $B_4 = (-1, 0] \in \mathcal{B}_4$ containing $x = 0$; let $B_2$ be a basis element in $\mathcal{B}_2$ containing $x$, then it has the form $(a, b)$ or $(a, b) - K$, with $a < 0 < b$. Similarly as above, take some $b'$ between $\frac{1}{\lceil 1/b \rceil}$ and $b$, it is not in $K$ but in $(a, b)$ thus in $B_2$, and it is not in $B_4$ cause it is positive. Thus $\tau_4$ is not contained in $\tau_2$, and we conclude that $\tau_2 \subset \tau_4$;
    	3. By above $\tau_5 \subset \tau_1 \subset \tau_2$;
    3. $\tau_3 =$ the finite complement topology:
    	1. By above $\tau_3 \subset \tau_1 \subset \tau_2 \subset \tau_4$;
    	2. Consider $U = \mathbb{R} - \lbrace 0 \rbrace \in \tau_3$ containing $1$; if $U \in \tau_5$ containing $1$, then by Lemma 13.1 there is $B_5 \in \mathcal{B}_5$ contained in $U$. $B_5$ is in the form $(- \infty, a)$ with $1 < a$ thus it contains $0$. Thus it cannot be contained in $U$. Thus $\tau_3$ is not contained in $\tau_5$;
    		On the other hand, consider $U = (- \infty, 0) \in \tau_5$, then $\mathbb{R} - U$ is neither finite nor $\mathbb{R}$ thus $U$ not in $\tau_3$, thus $\tau_5$ is not contained in $\tau_3$;
    		Thus we conclude they are not comparable;
    4. $\tau_4 =$ the upper limit topology, having all sets $(a, b]$ as basis:
    	1. By above $\tau_5 \subset \tau_1 \subset \tau_2 \subset \tau_4$.

    ## Section 16

    ### Exercise 2

    **If $\tau$ and $\tau'$ are topologies on $X$ and $\tau'$ is strictly finer than $\tau$, what can you say about the corresponding subspace topologies on the subset $Y$ of $X$**?

    Solution

    Let $\tau_Y$ and $\tau_Y'$ be the subspace topologies on the subset $Y$ corresponding to $\tau$ and $\tau'$ respectively. Then by definition $\tau_Y = \lbrace Y \cap U | U \in \tau \rbrace$ and $\tau_Y' = \lbrace Y \cap U | U \in \tau' \rbrace$. For any $U' \in \tau_Y$, by definition $U' = Y \cap U$ with some $U \in \tau$. Since $\tau \subset \tau'$, for any $U \in \tau$, $U \in \tau'$ thus $U'$ satisfy the condition $U' = Y \cap U$ with some $U \in \tau'$, thus $U' \in \tau_Y'$. I.e. $\tau_Y'$ finer than $\tau_Y$.

    Consider $X = \lbrace a, b, c \rbrace$ and $Y = \lbrace a, b \rbrace$; consider first $\tau = \lbrace \varnothing, X \rbrace \subset \tau' = \lbrace \varnothing, X, \lbrace a, b \rbrace \rbrace$, then the corresponding subspace topologies are $\tau_Y = \lbrace \varnothing, Y \rbrace = \tau_Y' = \lbrace \varnothing, Y \rbrace$.

    Now consider $\tau = \lbrace \varnothing, X \rbrace \subset \tau' = \lbrace \varnothing, X, \lbrace a \rbrace, \lbrace a, b \rbrace \rbrace$, then the corresponding subspace topologies are $\tau_Y = \lbrace \varnothing, Y \rbrace \subset \tau_Y' = \lbrace \varnothing, Y, \lbrace a \rbrace \rbrace$.

    Thus $\tau_Y'$ is not necessarily strictly finer.

    ### Exercise 3

    **Consider the set $Y = [-1, 1]$ as a subspace of $\mathbb{R}$. Which of the following sets are open in $Y$? Which are open in $\mathbb{R}$**?

    1. $A = \lbrace x | \frac{1}{2} < | x | < 1 \rbrace$;
    2. $B = \lbrace x | \frac{1}{2} < | x | \le 1 \rbrace$;
    3. $C = \lbrace x | \frac{1}{2} \le | x | < 1 \rbrace$;
    4. $D = \lbrace x | \frac{1}{2} \le | x | \le 1 \rbrace$;
    5. $E = \lbrace x | 0 < | x | < 1, 1/x \notin \mathbb{Z}_+ \rbrace$.

    Solution

    1. $A$ is a union of open intervals in $\mathbb{R}$ thus open in $\mathbb{R}$; Notice $A \subseteq Y$, by the definition of subspace topology, $Y \cap A = A \in \tau$ is in $\tau_Y$ thus $A$ also open in $Y$;
    2. $B$ is a union of half-open intervals in $\mathbb{R}$ thus not open in $\mathbb{R}$; Take $U = (-2, -1/2) \bigcup\limits(1/2,2)$ open in $\mathbb{R}$ then $B = Y \cap U$ is open in $Y$;
    3. $C$ is a union of half-open intervals in $\mathbb{R}$ thus not open in $\mathbb{R}$; Assume $C = Y \cap U$ for some $U \in \tau$. Let $\mathcal{B}$ be the collection of all open intervals in the real line, by Lemma 16.1, $\mathcal{B}_Y = \lbrace B \cap Y | B \in \mathcal{B} \rbrace$ is a basis for the subspace topology on $Y$. Consider any basis element $B_Y \in \mathcal{B}_Y$ containing $x = 1/2$, $B_Y = Y \cap B$ for some $B$, thus $B$ has the form $(a, b)$ with $a < 1/2 < b$. Take $a' = \frac{\max(a,-1/2) + 1/2}{2}$ then $a' \in B_Y$ but $a' \notin C$. Since $B_Y$ is arbitrary, there is no $B_Y$ such that $B_Y \subseteq C$ thus $C$ cannot be a union of $B_Y$, thus is not open in $Y$;
    4. Similar with $C$, $D$ is not open in $\mathbb{R}$ and not open in $Y$;
    5. We may write $E$ as $E = (-1, 0) \cup (0, 1) - K$, with K the same definition in the $K$-topology. And is the same thing as $(-1, 0) \cup (1, 1/2) \cup (1/2, 1/3) \cup \dots$ union of open sets thus open in $\mathbb{R}$; Notice that $E \subseteq Y$, thus similar with $A$, $E$ is open in $Y$.

    ### Exercise 8

    **If $L$ is a straight line in the plane, describe the topology $L$ inherits as a subspace of $\mathbb{R}_l \times \mathbb{R}$ and as a subspace of $\mathbb{R}_l \times \mathbb{R}_l$. In each case it is a familiar topology**.

    Solution

    By Theorem 15.1 the collection $\lbrace [a, b) \times (c, d) | [a, b) \in \tau_l, (c, d) \in \tau \rbrace$ is a basis for the topology of $\mathbb{R}_l \times \mathbb{R}$ and $\lbrace [a, b) \times [c, d) | [a, b) \in \tau_l, [c, d) \in \tau_l \rbrace$ is a basis for the topology of $\mathbb{R}_l \times \mathbb{R}_l$.

    Thus a basis of the topology of $\mathbb{R}_l \times \mathbb{R}$ and $\mathbb{R}_l \times \mathbb{R}_l$ contains (graphically) sets like:

    <img src="public/Pasted image 20220326102951.png" width="600" />

    Then the subspace topology is the intersection of, in the case, graphically, a straight line with the area. Notice that the direction of the line matters:

    <img src="public/Pasted image 20220326103158.png" width="600" />

    ### Exercise 9

    **Show that the dictionary order topology on the set $\mathbb{R} \times \mathbb{R}$ is the same as the product topology $\mathbb{R}_d \times \mathbb{R}$, where $\mathbb{R}_d$ denotes $\mathbb{R}$ in the discrete topology. Compare this topology with the standard topology on $\mathbb{R}^2$**.

    Proof

    Let's denote the dictionary order topology on the set $\mathbb{R} \times \mathbb{R}$ as $\tau_{\text{dict}}$ and the product topology $\mathbb{R}_d \times \mathbb{R}$ as $\tau_{\text{prod}}$ with $\mathcal{B}_{\text{dict}}, \mathcal{B}_{\text{prod}}$ as bases respectively. By the book, $\mathcal{B}_{\text{dict}} = \lbrace (a \times b, a' \times b') | a<a'$ or $a = a', b < b' \rbrace$. By Theorem 15.1, $\mathcal{B}_{\text{prod}} = \lbrace \lbrace x \rbrace \times (a, b) | x \in \mathbb{R}, a < b \rbrace$.

    Consider any basis element $B_{\text{dict}} = (a \times b, a' \times b')$ containing some $(x, y) \in \mathbb{R}^2$, then either:

    1. $a < x < a'$, then the set $\lbrace x \rbrace \times (y-1, y+1)$ is a basis element of $\mathcal{B}_{\text{prod}}$ containing in $B_{\text{dict}}$ and contains $(x, y)$;
    2. $a < x = a', y < b'$, then the set $\lbrace x \rbrace \times (y-1, (y+b')/2)$ is a basis element of $\mathcal{B}_{\text{prod}}$ containing in $B_{\text{dict}}$ and contains $(x, y)$;
    3. $a = x < a', b < y$, then the set $\lbrace x \rbrace \times ((y+b)/2, y+1)$ is a basis element of $\mathcal{B}_{\text{prod}}$ containing in $B_{\text{dict}}$ and contains $(x, y)$;
    4. $a = x = a', b < y < b'$, then the set $\lbrace x \rbrace \times ((y+b)/2, (y+b')/2)$ is a basis element of $\mathcal{B}_{\text{prod}}$ containing in $B_{\text{dict}}$ and contains $(x, y)$.

    So either case, by Lemma 13.3, we have $\tau_{\text{dict}} \subseteq \tau_{\text{prod}}$.

    Now consider any basis element $B_{\text{prod}} = \lbrace x \rbrace \times (a, b)$ containing some $(x, y) \in \mathbb{R}^2$, then $a < y < b$, the set $(x \times (a+y)/2, x \times (b+y)/2)$ is a basis element of $\mathcal{B}_{\text{dict}}$ containing in $B_{\text{prod}}$ and contains $(x, y)$. Thus we have $\tau_{\text{dict}} \supseteq \tau_{\text{prod}}$, thus they are equal.

    Now let's compare $\tau_{\text{dict}} = \tau_{\text{prod}}$ with the standard topology $\tau$ on $\mathbb{R}^2$ with $\mathcal{B}$ as basis.

    Consider any basis element $B = ((a, b), (c, d))$ containing $(x, y) \in \mathbb{R}^2$. Then $a < x < b, c < y < d$, then the set $\lbrace x \rbrace \times ((y+c)/2, (y+d)/2)$ is a basis element of $\mathcal{B}_{\text{prod}}$ containing in $B$ and contains $(x, y)$. Thus we have $\tau \subseteq \tau_{\text{prod}}$.

    On the other hand, consider the basis element $\lbrace 0 \rbrace \times (-1, 1)$ containing $(0, 0)$. Then for any basis element $B$ of the form $((a, b), (c, d))$, if it contains $(0, 0)$, then $a < 0 < b, c < 0 < d$. Pick $a' = a/2$, then $(a', 0) \in B$ but $(a', 0) \notin B_{\text{prod}}$. Thus we have $\tau_{\text{prod}}$ is not contained in $\tau$ and that means $\tau \subset \tau_{\text{prod}}$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 04""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 17

    ### Exercise 2

    **Show that if $A$ is closed in $Y$ and $Y$ closed in $X$, then $A$ is closed in $X$**.

    Proof

    By definition, $X - Y$ open in $X$. By theorem 17.2 $A$ closed in $Y$ then $\exists A'$ closed in $X$ such that $A = A' \cap Y$, notice that thus $X - A'$ open in $X$;
    Then $X - A = X - (A' \cap Y) = (X - A') \cup (X - Y)$ union of open sets is open in $X$, thus $A$ closed in $X$.

    ### Exercise 6

    **Let $A, B$, and $A_{\alpha}$ denote subsets of a space $X$. Prove the following**:

    1. **If $A \subseteq B$, then $\overline{A} \subseteq \overline{B}$**;
    2. $\overline{A \cup B} = \overline{A} \cup \overline{B}$;
    3. **$\overline{\cup A_{\alpha}} \supseteq \bigcup\limits{\overline A_{\alpha}}$, give an example where equality fails**.

    Proof

    1. For any $x \in \overline{A}$, by theorem 17.5 every open set $U$ containing $x$ intersects $A$, say $x' \in U \cap A$, then $x' \in U$ and $x' \in A$. Since $A \subseteq B$, $x' \in B$, thus $x' \in U \cap B$. Since $U$ is arbitrary, every open set $U$ containing $x$ intersects $B$. Thus again by theorem 17.5, $x \in \overline{B}$;
    2. For any $x \in \overline{A \cup B}$, by theorem 17.5 every open set $U$ containing $x$ intersects $A \cup B$, thus $U$ intersect $A$ or $B$. Suppose $x \notin \overline{A} \cup \overline{B}$, then $x \notin \overline{A}$ and $x \notin \overline{B}$, then $\exists U_A$ containing $x$ such that $U_A \cap A = \varnothing$ and $\exists U_B$ containing $x$ such that $U_B \cap B = \varnothing$. Since $x \in U_A$ and $x \in U_B$ thus $U_A \cap U_B \ne \varnothing$, take $U' = U_A \cap U_B$, then $x \in U'$ and $U' \cap A = \varnothing, U' \cap B = \varnothing$, which is a contradiction, thus the negation holds; Now suppose $x \in \overline{A} \cup \overline{B}$, if $x \in \overline{A}$ then $\forall U$ open set containing $x$, $\exists x' \in U$ and $x' \in A$, thus $x' \in A \cup B$ thus $x' \in U \cap (A \cup B)$ thus $x \in \overline{A \cup B}$; similar if $x \in \overline{B}$. Thus inclusion holds either way and thus equality holds;
    3. For any $x \in \bigcup\limits{\overline A_{\alpha}}$, $x \in A_{\alpha}$ for some $\alpha$, then for any $U$ open set containing $x$, $\exists x' \in U$ and $x' \in A_{\alpha}$ thus $x' \in \cup A_{\alpha}$ thus $x' \in U \cap (\cup A_{\alpha})$ thus $x \in \overline{\cup A_{\alpha}}$. Say $A_{n} = (1/n,1-1/n)$, then $\cup A_{n} = (0,1)$ and $\overline{\cup A_n} = [0, 1]$ yet $0, 1 \notin [1/n, 1-1/n], \forall n$ thus $0, 1 \notin \bigcup\limits{\overline A_n}$.

    ### Exercise 8

    **Let $A, B$, and $A_{\alpha}$ denote subsets of a space $X$. Determine whether the following equations hold; if an equality fails, determine whether one of the inclusions holds**.

    1. $\overline{A \cap B} = \overline{A} \cap \overline{B}$;
    2. $\overline{\cap A_{\alpha}} = \bigcap\limits{\overline A_{\alpha}}$;
    3. $\overline{A - B} = \overline{A} - \overline{B}$.

    Proof

    1. For any $x \in \overline{A \cap B}$, we have $\forall U$ open set containing $x$, $\exists x' \in U$ and $x' \in A \cap B$ thus $x' \in A$ and $x' \in B$ thus $x' \in U \cap A$ and $x' \in U \cap B$ thus $x \in \overline{A}$ and $x \in \overline{B}$ thus $x \in \overline{A} \cap \overline{B}$; For the other way around, consider $A = [-1,0), B = (0, 1]$ then easy to see that left side is empty while right side is the set of a single element $0$, thus it is not hold;
    2. For any $x \in \overline{\cap A_{\alpha}}$, we have $\forall U$ open set containing $x$, $\exists x' \in U$ and $x' \in \cap A_{\alpha}$ thus $x' \in A_{\alpha}$ for all $\alpha$ thus $x' \in A_{\alpha} \cap U$ for all $\alpha$ thus $x \in \overline A_{\alpha}$ for all $\alpha$ thus $x \in \bigcap\limits{\overline A_{\alpha}}$; The counter example in (i). also works here, thus $\supseteq$ does not work;
    3. For any $x \in \overline{A} - \overline{B}$, by definition $x \in \overline{A}$ and $x \notin \overline{B}$ thus we have $\forall U$ open set containing $x$, $\exists x' \in U$ and $x' \in A$, and $\exists U_B$ open set containing $x$ and $U_B \cap B = \varnothing$. For any $U$ as above, let $U' = U \cap U_B$, then it is a finite intersection of open sets thus open. $U'$ contains $x$. Then by construction $\exists x' \in U'$ and $x' \in A$. Since $U' \subseteq U_B$, it does not intersect $B$ thus $x' \notin B$, thus $x' \in A - B$. Since $U' \subseteq U$, $x' \in U$, thus in conclusion, for any $U$ we have this $x' \in U \cap (A - B)$ thus $x \in \overline{A - B}$; For the other way around, consider $A = [0,1]$ and $B = [1/2, 1]$ then $A - B = [0, 1/2)$ thus $\overline{A - B} = [0, 1/2]$ and $\overline{A} - \overline{B} = [0, 1] - [1/2, 1] = [0, 1/2)$, we see they are not equal.

    ## Section 18

    ### Exercise 5

    **Show that the subspace $(a, b)$ of $\mathbb{R}$ is homeomorphic with $(0, 1)$ and the subspace $[a, b]$ of $\mathbb{R}$ is homeomorphic with $[0, 1]$**.

    Proof

    Define $f: (a, b) \rightarrow (0, 1)$ by $f(x) = \frac{x - a}{b - a}$. If $\frac{x - a}{b - a} = \frac{x' - a}{b - a}$ then $x - a = x' - a$ thus $x = x'$; for any $y \in (0,1), x = (b - a)y+a$ is the preimage. Thus $f$ bijection; thus it has an inverse $f^{-1}: (1, 0) \rightarrow (a, b)$ given by $f^{-1}(y) = (b-a)y+a$ which is continuous. Thus by definition $f$ is a homeomorphism. Proof is the same for the closed interval $[a, b]$.

    ### Exercise 8

    **Let $Y$ be an ordered set in the order topology. Let $f, g: X \rightarrow Y$ be continuous**.

    1. **Show that the set $\lbrace x | f(x) \le g(x) \rbrace$ is closed in $X$**;
    2. **Let $h: X \rightarrow Y$ be the function $h(x) = \min(f(x), g(x))$. Show that $h$ is continuous**.

    Proof

    1.   Let $S = \lbrace x | f(x) \le g(x) \rbrace$, then $X - S = \lbrace x | f(x) > g(x) \rbrace$, then for each $y_0 \in Y$, consider the set $A_{<y_0} = \lbrace y \in Y | y < y_0 \rbrace$ and the set $A_{>y_0} = \lbrace y \in Y | y > y_0 \rbrace$, they are open rays in the ordered topology thus open. Then $f^{-1}(A_{>y_0}) = \lbrace x | f(x) > y_0 \rbrace$ and $g^{-1}(A_{<y_0}) = \lbrace x | g(x) < y_0 \rbrace$, they are preimage of open set under continuous $f, g$ thus they are open. Thus their intersection $f^{-1}(A_{>y_0}) \cap g^{-1}(A_{<y_0})$ $= \lbrace x | g(x) < y_0 < f(x) \rbrace$ is open in $X$.
    	Consider the union over $Y$: $S' = \bigcup\limits_{y_0 \in Y} f^{-1}(A_{>y_0}) \cap g^{-1}(A_{<y_0})$ is open in $X$. We have $S' \subseteq X - S$ (because $x \in S'$ satisfy that $f(x) > g(x)$), but at this point $X - S$ is not (necessarily) contained in $S'$ because there may be situations that $f(x) > g(x)$ but there is no $y \in Y$ between $f(x)$ and $g(x)$.
    	To calibrate this situation, denote $y_+$ as the immediate successor of $y$ in $Y$ if the immediate successor exists, or just $y$ if not; denote $y_-$ as the immediate predecessor of $y$ in $Y$ if the immediate predecessor exists, or just $y$ if not.
    	Change $S' = \bigcup\limits_{y_0 \in Y} f^{-1}(A_{>y_{0_-}}) \cap g^{-1}(A_{<y_{0_+}})$. In the above example, then when we take $y = 1$, immediate successor of $1$ is $2$, thus $f^{-1}(2) = g^{-1}(1)$ is also included in the union.
         Thus for any $x \in X - S$:
    	1. If $f(x) > g(x)$, then $x \in S'$;1. If there exists $y$ such that $f(x) > y > g(x)$, take this $y$ and we have $x \in S'$;
    	2. Else if $y$ is the immediate successor of $g(x)$, then $f(x) > y \succ g(x)$, take this $y$ and we have $x \in S'$;
    	3. Otherwise $y$ is the immediate predecessor of $f(x)$, then $f(x) \succ y > g(x)$, take this $y$ and we have $x \in S'$.
    
    	Thus $S' = X - S$ and it is open in $X$, and thus $S$ is closed in $X$;
    2.   Let $S = \lbrace x | f(x) \le g(x) \rbrace$ and $S' = \lbrace x | f(x) \ge g(x) \rbrace$; by the first part they are both closed, also $X = S \cup S'$. If $x \in S \cap S'$ then $f(x) \le g(x)$ and $g(x) \le f(x)$ thus $f(x) = g(x)$. Then define $h'(x) = \begin{cases} f(x), x \in S \\ g(x), x \in S' \end{cases}$ then $h'(x) = \min(f(x), g(x)) = h(x)$, and $f, g$ continuous, thus by the pasting lemma, $h$ is continuous.

    ### Exercise 11

    **Let $F: X \times Y \rightarrow Z$. We say that $F$ is continuous in each variable separately if for each $y_0$ in $Y$, the map $h: X \rightarrow Z$ defined by $h(x) = F(x \times y_0)$ is continuous and for each $x_0$ in $X$, the map $k: Y \rightarrow Z$ defined by $k(y) = F(x_0 \times y)$ is continuous. Show that if $F$ is continuous, then $F$ is continuous in each variable separately**.

    Proof

    Let's fix $y_0 \in Y$ and define $h$ as above. Since $F$ is continuous, by theorem 18.1, for each $x \in X$ and each neighborhood $V$ of $F(x \times y_0)$, there is a neighborhood $U$ of $x \times y_0$ such that $F(U) \subseteq V$.

    Then there is a basis element $U_X \times U_Y \subseteq U$ containing $x \times y_0$ with $x \in U_X$. For any $z \in h(U_X)$, $z = h(x')$ for some $x' \in U_X$ thus $x' \times y_0 \in U_X \times U_Y$; Thus $z = h(x') = F(x',y_0) \in F(U_X \times U_Y) \subseteq F(U) \subseteq V$, i.e. $h(U_X) \subseteq V$.

    Since $x$ arbitrary, again by theorem 18.1, $h$ is continuous. Similarly $k$ is continuous, and we may conclude $F$ is continuous in each variable separately.

    ### Exercise 12

    **Let $F: \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}$ be defined by the equation** $$F(x \times y) = \begin{cases} xy/(x^2+y^2),& x \times y \ne 0 \times 0 \\ 0 ,& x \times y = 0 \times 0 \end{cases}.$$

    1. **Show that $F$ is continuous in each variable separately**;
    2. **Compute the function $g: \mathbb{R} \rightarrow \mathbb{R}$ defined by $g(x) = F(x \times x)$**;
    3. **Show that $F$ is not continuous**.

    Proof

    1. For any fixed $y_0$, $h(x) = F(x, y_0) = \begin{cases} xy_0/(x^2+y_0^2) ,& x \times y_0 \ne 0 \times 0 \\ 0 ,& x \times y_0 = 0 \times 0 \end{cases}$ If $y_0 \ne 0$ then $h(x) = xy_0/(x^2+y_0^2)$, the only potential concern is when the denominator is $0$, which will not happen as $x^2 + y_0^2$ is always positive, thus $h$ is continuous; if $y_0 = 0$, $h(x) = \begin{cases} 0/(x^2) ,& x \times 0 \ne 0 \times 0 \\ 0 ,& x \times 0 = 0 \times 0 \end{cases}$, we see this is just $h(x) = 0$ a constant function thus continuous. Similar with fixed $x$. Thus $F$ is continuous in each variable separately;
    2. We have $$g(x) = F(x \times x) = \begin{cases} xx/(x^2+x^2) = \frac{1}{2} ,& x \times x \ne 0 \times 0 \\ 0 ,& x \times x = 0 \times 0 \end{cases};$$
    3. Notice that if we define $f(x) = x \times x$ then $g(x) = F(f(x))$. $f$ is continuous by theorem 18.4. If $F$ continuous then by theorem 18.2 $g$ is composition of two continuous functions thus continuous. However $g$ is not continuous(at $0$), thus $F$ cannot be continuous.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 05""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 17

    ### Exercise 13

    **Show that $X$ is Hausdorff if and only if the diagonal $\triangle = \lbrace x \times x | x \in X \rbrace$ is closed in $X \times X$**.

    Proof

    Suppose $X$ is Hausdorff. The complement of $\triangle$ in $X \times X$ is $\triangle^C = X \times X - \triangle = \lbrace x \times y | x, y \in X, x \ne y \rbrace$. For any $x \ne y \in X$, since $X$ is Hausdorff, there exists neighborhoods $U \ni x, V \ni y$ that are disjoint. By theorem 15.1, $U \times V$ is a basis for the topology $X \times X$, thus $U \times V$ is an open set in $X \times X$. Since $U, V$ disjoint, we have for any $x' \in U, y' \in V$, $x' \ne y'$, thus $x' \times y' \notin \triangle$. Thus we found $U \times V$ an open set containing $x \times y$ that does not intersect $\triangle$. By theorem 17.5, $x \times y \notin \overline{\triangle}$. So any element not in the diagonal is not in the closure of the diagonal. As a result, the closure of $\triangle$ is itself, so that it is closed.

    Now suppose the diagonal $\triangle = \lbrace x \times x | x \in X \rbrace$ is closed in $X \times X$. By corollary 17.7, it contains all its limit points, in other words, for any $x \ne y$, $x \times y$ is not a limit point of the diagonal thus by definition there exist a neighborhood $U_0$ of $x \times y$ that does not intersect $\triangle$. Thus there is a basis element $U \times V$ of $X \times X$ with $x \in U, y \in V, U \times V \subset U_0$. Since $U_0$ does not intersect $\triangle$, so does $U \times V$. And if $U, V$ not disjoint, then $\exists z \in U \cap V$, then $z \times z \in U \times V$ and by construction $z \times z \in \triangle$ thus $U \times V$ and $\triangle$ intersect, which is a contradiction, thus $U, V$ disjoint. Since $x, y$ are arbitrary, by definition $X$ is Hausdorff.

    Comment

    More generally ($\implies$ direction), if $Y$ is Hausdorff and $f$ is continuous, then $Gr_f = \lbrace (x, f(x)) | x \in X, f(x) \in Y \rbrace$ is closed, the reasoning is basically the same with the above exercise.

    ### Exercise 14

    **In the finite complement topology on $\mathbb{R}$, to what point or points does the sequence $x_n = 1/n$ converge**?

    Proof

    $x_n$ converges to all points in $\mathbb{R}$: Suppose there exists $a \in \mathbb{R}$ that $x_n$ does not converge to. By (negation of) definition of convergence, $x_n$ does not converge to $a$ if $\exists U(a), \forall N \in \mathbb{N}, \exists n \ge N$ such that $x_n \notin U(a)$. That is, there are infinitely many $n$ such that $x_n \notin U(a)$. By construction, $x_n$'s are all distinct, thus there are infinitely many $r \in \mathbb{R}$ with $r \notin U(a)$, in other words, $\mathbb{R} - U(a)$ is infinite. $U(a)$ is not empty because it contains $a$, thus by definition of a finite complement topology, $U(a)$ is not open in $\mathbb{R}$, which is a contradiction. Thus $x_n$ converges to $a$ for all $a \in \mathbb{R}$.

    ## Section 20

    ### Exercise 3

    **Let $X$ be a metric space with metric $d$**.

    1. **Show that $d: X \times X \rightarrow \mathbb{R}$ is continuous**;
    2. **Let $X'$ denote a space having the same underlying set as $X$. Show that if $d:X' \times X' \rightarrow \mathbb{R}$ is continuous, then the topology of $X'$ is finer than the topology of $X$**.

    Proof

    1. For any $x_0, y_0 \in X$ and an open set $V \subseteq \mathbb{R}$ containing $d(x_0, y_0)$, there exists a basis element $B$ of $\mathbb{R}$ with $d(x_0, y_0) \in B \subseteq V$, and $B$ has the form $(d(x_0, y_0) - a, d(x_0, y_0) + b)$ (WLOG let's say $a < b$). Since $X$ is a metric space, $B_d(x_0, \frac{a}{3})$ is a basis element of $X$ containing $x_0$ and $B_d(y_0, \frac{a}{3})$ is a basis element of $X$ containing $y_0$. Thus $B_d(x_0, \frac{a}{3}) \times B_d(y_0, \frac{a}{3})$ is a basis element of $X \times X$ containing $x_0 \times y_0$. Thus for each element $x \times y \in B_d(x_0, \frac{a}{3}) \times B_d(y_0, \frac{a}{3})$, $d(x, y) \le d(x, x_0) + d(x_0, y) \le d(x, x_0) + d(x_0, y_0) + d(y_0, y)$ $< \frac{a}{3} + d(x_0, y_0) + \frac{a}{3}$ $= d(x_0, y_0) + \frac{2}{3}a$. Similarly, $d(y_0,x) + d(x,y) + d(y,x_0) \ge d(x_0, y_0)$ thus $d(x, y) > d(x_0, y_0) - \frac{2}{3}a$. Thus $d(B_d(x_0, \frac{a}{3}) \times B_d(y_0, \frac{a}{3}))$ $\subseteq (d(x_0, y_0) - \frac{2}{3}a, d(x_0, y_0) + \frac{2}{3}a)$ $\subseteq B \subseteq V$. By theorem 18.1(4), $d$ is continuous;
    2. Suppose $d:X' \times X' \rightarrow \mathbb{R}$ is continuous, by exercise in last homework we have $d$ continuous with each variable separately, i.e. for each $y_0 \in X$, $h: X' \rightarrow \mathbb{R}$ given by $x \mapsto d(x, y_0)$ is continuous. For any $x$ in $X$ and $B_d(x_0, \varepsilon)$ basis element of $X$ containing $x$, by definition $B_d(x_0, \varepsilon) = \lbrace y | d(x_0, y) < \varepsilon \rbrace$ $= \lbrace y | d(y, x_0) < \varepsilon \rbrace$ $= h^{-1}((- \infty, \varepsilon))$ for the fixed $x_0$. $(- \infty, \varepsilon)$ is open in $\mathbb{R}$ (or say, $[0, \varepsilon)$ is open in non-negative reals), thus preimage of it under $h$ is open. Thus there exists a basis element $B' \subseteq B_d(x_0, \varepsilon)$ containing $x$, which means the topology of $X'$ is finer than the topology of $X$.

    ### Exercise 4

    **Consider the product, uniform, and box topologies on $\mathbb{R}^{\omega}$**.

    1. **In which topologies are the following functions from $\mathbb{R}$ to $\mathbb{R}^{\omega}$ continuous**?
    	1. $f(t) = (t, 2t, 3t, \dots)$;
    	2. $g(t) = (t, t, t, \dots)$;
    	3. $h(t) = (t, \frac{1}{2}t, \frac{1}{3}t, \dots)$;

    2. **In which topologies do the following sequences converge**?
    	1. $w_1 = (1, 1, 1, 1, \dots), w_2 = (0, 2, 2, 2, \dots), w_3 = (0, 0, 3, 3, \dots), \dots$;
    	2. $x_1 = (1, 1, 1, 1, \dots), x_2 = (0, 1/2, 1/2, 1/2, \dots), x_3 = (0, 0, 1/3, 1/3, \dots), \dots$;
    	3. $y_1 = (1, 0, 0, 0, \dots), y_2 = (1/2, 1/2, 0, 0, \dots), y_3 = (1/3, 1/3, 1/3, 0, \dots), \dots$;
    	4. $z_1 = (1, 1, 0, 0, \dots), z_2 = (1/2, 1/2, 0, 0, \dots), z_3 = (1/3, 1/3, 0, 0, \dots), \dots$.

    Solution

    1. Since $f_{\alpha}(t) = t, f_{\beta}(t) = c t, f_{\theta}(t) = \frac{1}{c}t$ are all continuous for a constant $c$, thus by theorem 19.6, $f(t), g(t), h(t)$ are all continuous if $\mathbb{R}^{\omega}$ is given the product topology;
        Suppose $\mathbb{R}^{\omega}$ is given the uniform topology. Consider the basis element $B = B_{\overline{\rho}}(x, \varepsilon)$ with some $F(t) = (F_1(t), F_2(t), \dots) = (c_1 t, c_2 t, \dots) \in B$. Then by definition, $\overline{\rho}(x, F(t))$ $= \sup\limits_n(\overline{d}(x_n, F_n(t)))$ $= \sup\limits_n(\overline{d}(x_n, c_n t))$ $= \sup\limits_n(\min(d(x_n, c_n t), 1))$ $= M < \varepsilon$. Now consider any neighborhood of $t$, it has the form $(t - a, t + a)$. $F$ is linear. By the definition of a metric, $\overline{\rho}(x, F(t + a)) = \overline{\rho}(x, F(t) + F(a)) \le \overline{\rho}(x, F(t)) + \overline{\rho}(F(t), F(t)+F(a))$ $= M + \sup\limits_n(\overline{d}(c_n t, c_n (t + a))) = M + \sup\limits_n(\overline{d}(0, c_n a)) = M'$. To have $F$ continuous, we want to find an $a$ to make $M' < \varepsilon$. Now if $F = f$, i.e. $c_n = n$, then $c_n a$ is not bounded for any $a$ thus for small enough $\varepsilon$ relative to $M$, $M' < \varepsilon$ does not hold, thus $f$ not continuous. If $F = g$, i.e. $c_n = 1$, take $a = \frac{\varepsilon - M}{2}$ then $M' = M + 1 \cdot a = M + \frac{\varepsilon - M}{2} < \varepsilon$, by this we find a neighborhood of $t$ contained in the neighborhood of $g(t)$, thus $g(t)$ is continuous. For the same reason and with the same $a$, $h(t)$ is also continuous;
    	Now if $\mathbb{R}^{\omega}$ is given the box topology. Consider the basis element $B = (-1, 1) \times (- \frac{1}{2}, \frac{1}{2}) \times \dots$. If $f^{-1}(B)$ is open in $\mathbb{R}$, it contains some interval with the form $(- \delta, \delta)$ thus $f((- \delta, \delta)) \subseteq B$ thus $f_n((- \delta, \delta))$ $= (-n \delta, n \delta)$ $\subseteq (- \frac{1}{n}, \frac{1}{n})$ for all $n$, this is cannot be true, thus we have a contradiction. Thus $f^{-1}(B)$ is not open, thus $f(t)$ not continuous. For the same reason and same $B$, $g(t)$ is also not continuous. And for the same logic, take $B =$ $(-1, 1) \times (- \frac{1}{2^2}, \frac{1}{2^2}) \times (- \frac{1}{3^2}, \frac{1}{3^2}) \times \dots$, $(- \frac{1}{n} \delta, \frac{1}{n} \delta)$ $\subseteq (- \frac{1}{n^2}, \frac{1}{n^2})$ gives a contradiction thus $h(t)$ is also not continuous.
        So to make it clearer, in conclusion:

        1. In product topology, all three functions are continuous;
        2. In box topology, all three functions are not continuous;
        3. In uniform topology, $g, h$ are continuous, $f$ is not;

    2. Claim that $w_n \rightarrow 0$ in product topology. $\frac{\overline{d}(w_i, 0)}{i} = \frac{\min({d}(w_i, 0), 1)}{i} = \frac{1}{i} \rightarrow 0$ thus any open interval centered at $0$ contains all $w_n$ after some index. In uniform topology, observe that (as above) $d(w_i, 0)$ is always greater than $1$. I.e. take $\varepsilon = 1, \forall N \in \mathbb{N}, \exists n \ge N, | w_n - 0 | > 1$, thus $w_n$ does not converge in the uniform topology. Thus $w_n$ also does not converge in the box topology since box topology is even finer;
        $x_n$ converges to $0$ in the product topology with the same reason. For any $\varepsilon > 0$, take some $N > \frac{1}{\varepsilon}$, then for any $n > N$, $| x_n - 0 | < \frac{1}{n} < \varepsilon$ thus $x_n$ converges to $0$ in the uniform topology. Say $x_n$ converges to $a$ in the box topology, take $U(a) = (a - \frac{1}{2}, a + \frac{1}{2}) \times (a - \frac{1}{3}, a + \frac{1}{3}) \times \dots$. If we want to have $x_1 \in U(a)$ then we must have $a-1/2 < 1 <a+1/2 \implies 1-1/2<a<1+1/2$. But then infinitely many $x_2, x_3, \dots \notin U(a)$ because $0 \notin (a - \frac{1}{2}, a + \frac{1}{2})$, $\forall 1-1/2<a<1+1/2$. Similarly we can see that for $U(a)$, at most finitely many (actual, $1$) element(s) of $x_n$ are contained in this neighborhood. Thus by definition, $x_n$ does not converge (to any point) in box topology.
        With the same argument and take the same $U(a)$, $y_n$ converges in product topology and uniform topology, but not in box topology.
        $z_n$ converges to $0$ in product topology and uniform topology with the same logic. In box topology, for any $\varepsilon_1, \varepsilon_2 > 0$, let $\varepsilon = \min(\varepsilon_1, \varepsilon_2)$, any neighborhood $U(0)$ have the form $(- \varepsilon_1, \varepsilon_1) \times (- \varepsilon_2, \varepsilon_2) \times \dots$, then $z_n \in U(0)$ for all $n > 1/ \varepsilon$ thus there are infinitely many element of the sequence in $U(0)$, by definition $z_n$ converges to $0$.

    ## Section 21

    ### Exercise 10

    **Using the closed set formulation of continuity (Theorem 18.1), show that the following are closed subsets of $\mathbb{R}^2$: $A = \lbrace x \times y | x y = 1 \rbrace$, $S^1 = \lbrace x \times y | x^2 + y^2 = 1 \rbrace$, $B^2 = \lbrace x \times y | x^2 + y^2 \le 1 \rbrace$**.

    Proof

    By theorem 21.4, $f: \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}$ given by $f(x, y) = x y, f(x, y) = x^2 + y^2$ are constructed from the inclusion map using addition and multiplication thus continuous. $\lbrace 1 \rbrace$ and $(- \infty, 1]$ are closed in $\mathbb{R}$, by theorem 18.1 their preimage under continuous functions are closed.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 06""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 22

    ### Exercise 2

    1. **Let $p: X \rightarrow Y$ be a continuous map. Show that if there is a continuous map $f: Y \rightarrow X$ such that $p \circ f$ equals the identity map of $Y$, then $p$ is a quotient map**;
    2. **If $A \subseteq X$, a retraction of $X$ onto $A$ is a continuous map $r: X \rightarrow A$ such that $r(a) = a$ for each $a \in A$. Show that a retraction is a quotient map**.

    Proof

    1. If $p^{-1}(V)$ is open in $X$ for some $V$ in $Y$, then $f^{-1}(p^{-1}(V))$ $= (p \circ f)^{-1}(V)$ $= V$ since its the identity. Since $f$ is continuous, $V$ is open in $Y$. Conversely if $V$ is open in $Y$, then $p^{-1}(V)$ is open in $X$ because $p$ is continuous. By definition, $p$ is a quotient map;
    2. By construction $r$ is a surjective map, thus it has a right inverse, that map would be inclusive thus continuous. By (i), it is a quotient map.

    ### Exercise 3

    **Let $\pi_i: \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}$ be projection on the first coordinate. Let $A$ be the subspace of $\mathbb{R} \times \mathbb{R}$ consisting of all points $x \times y$ for which either $x \ge 0$ or $y = 0$ or both; let $q: A \rightarrow \mathbb{R}$ be obtained by restricting $\pi_1$. Show that $q$ is a quotient map that is neither open nor closed**.

    Proof

    Let $f: A \rightarrow \mathbb{R} \times \lbrace 0 \rbrace$ given by $(x, y) \mapsto (x, 0)$, $g: \mathbb{R} \times \lbrace 0 \rbrace \rightarrow \mathbb{R}$ given by $(x, 0) \mapsto x$. Then by construction $A \supseteq \mathbb{R} \times \lbrace 0 \rbrace$, $f$ is continuous and $f((x,0)) = (x,0), \forall x$. By previous exercise part (ii), $f$ is a quotient map. Also $g$ is a homeomorphism. By theorem 22.2 we have $q = f(g)$ is a quotient map.

    Now we give counterexamples to show $q$ is neither open nor closed. $\mathbb{R} \times \lbrace y \in \mathbb{R} | y < 0 \rbrace$ is open in $\mathbb{R}^2$, yet $\mathbb{R} \times \lbrace y \in \mathbb{R} | y < 0 \rbrace \cap A = \lbrace x \ge 0 \rbrace \times \lbrace y < 0 \rbrace$ and $q(\lbrace x \ge 0 \rbrace \times \lbrace y < 0 \rbrace) = \lbrace x \ge 0 \rbrace$ which is not open in $\mathbb{R}$ thus $q$ not open;

    On the other hand, take $\lbrace x \in \mathbb{R} | x > 0 \rbrace \times \lbrace y \in \mathbb{R} | y = 1/x \rbrace$ is closed in $\mathbb{R}^2$, yet $q(\lbrace x \in \mathbb{R} | x > 0 \rbrace \times \lbrace y \in \mathbb{R} | y = 1/x \rbrace) = \lbrace x > 0 \rbrace$ which is not closed in $\mathbb{R}$ thus $q$ not closed.

    ### Exercise 4

    1. **Define an equivalence relation on the plane $X = \mathbb{R}^2$ as follows: $x_0 \times y_0 \sim x_1 \times y_1 \text{ if } x_0 + y_0^2 = x_1 + y_1^2$. Let $X^{*}$ be the corresponding quotient space. It is homeomorphic to a familiar space, what is it**?
    2. **Repeat (i). for the equivalence relation $x_0 \times y_0 \sim x_1 \times y_1 \text{ if } x_0^2 + y_0^2 = x_1^2 + y_1^2$**.

    Solution

    1.   Let $g: X \rightarrow \mathbb{R}$ given by $x \times y \mapsto x + y^2$. Then $g$ is surjective and continuous. Consider the map $h: \mathbb{R} \rightarrow X$ given by $x \mapsto x \times 0$, then $h$ is the continuous right inverse of $g$. By previous exercise, $g$ is a quotient map. Let $f: X^{*} \rightarrow \mathbb{R}$ be the map induced by $g$. If $x_0 + y_0^2 = x_1 + y_1^2$ then by definition $x_0 \times y_0 = x_1 \times y_1$, thus $[x_0 \times y_0] = [x_1 \times y_1]$, thus $f$ is an injection; $f$ is a quotient map thus a surjection, thus $f$ is a bijection. By corollary 22.3, $f$ is a homeomorphism between $X^{*}$ and $\mathbb{R}$;
    2.   To maintain $g$ being surjective, take $g: X \rightarrow \mathbb{R}_+ + \lbrace 0 \rbrace$ given by $x \times y \mapsto x^2 + y^2$, and take $h: \mathbb{R}_+ + \lbrace 0 \rbrace \rightarrow X$ given by $x \mapsto \sqrt{x} \times 0$. The rest argument remains the same and we have $X^{*}$ homeomorphic to $\mathbb{R}_+ + \lbrace 0 \rbrace$.

    ## Section 23

    ### Exercise 3

    **Let $\lbrace A_{\alpha} \rbrace$ be a collection of connected subspaces of $X$; let $A$ be a connected subspace of $X$. Show that if $A \cap A_{\alpha} \ne \varnothing$ for all $\alpha$, then $A \cup (\cup A_{\alpha})$ is connected**.

    Proof

    Suppose $A \cup (\cup A_{\alpha}) = U \cup V$ is a separation. By lemma 23.2, $A$ and each $A_{\alpha}$ lies entirely within $U$ or $V$. WOLG say $A \subseteq U$, then for each $\alpha$, $\exists a \in A \cap A_{\alpha}$ $\implies a \in A \subseteq U$ $\implies \exists a \in A_{\alpha}$ such that $a \in U$, thus $A_{\alpha}$ lie entirely within $U$. Since $\alpha$ is selected arbitrarily, that is to say $A$ and all $A_{\alpha}$ lies in $U$, thus $V$ is empty, which is a contradiction.

    ### Exercise 4

    **Show that if $X$ is an infinite set, it is connected in the finite complement topology**.

    Proof

    Suppose $X = U \cup V$ is a separation. By definition of a separation, $U$ must be non-empty and open, and by definition of the complement topology, $X - U = V$ must be finite, thus $U$ must be infinite. However, $V$ is also open, which by definition of the complement topology requires $X - V = U$ being finite, thus we have a contradiction.

    ### Exercise 5

    **A space is totally disconnected if its only connected subspaces are one-point sets. Show that if $X$ has the discrete topology, then $X$ is totally disconnected. Does the converse hold**?

    Proof

    Let $V$ be an non-empty subspace of $X$, thus there exists $x \in V$. Since $X$ has the discrete topology, $\lbrace x \rbrace$ is open in $X$ thus open in $V$; but $V - \lbrace x \rbrace$ is also open in $X$ thus open in $V$. If $V - \lbrace x \rbrace$ is non-empty, $V - \lbrace x \rbrace$ and $\lbrace x \rbrace$ would form a separation of $V$. This could not happen by the construction. Thus $V - \lbrace x \rbrace$ is empty, i.e. $V$ contains only one point.

    The converse does not hold, as $\mathbb{Q}$ is totally disconnected, but it is not discrete in $\mathbb{R}$.

    ## Section 24

    ### Exercise 2

    **Let $f:S^1 \rightarrow \mathbb{R}$ be a continuous map. show there exists a point $x$ of $S^1$ such that $f(x) = f(-x)$**.

    Proof

    $f(x)$ and $f(-x)$ are both continuous. Thus $F(x) = f(x) - f(-x)$ is also continuous. For an arbitrary $x$, if $F(x) = 0$ then $f(x) = f(-x)$ we are done, if not, WLOG assume $F(x) > 0$, then $F(-x) = f(-x) - f(x) = - F(x) < 0$. I.e. $F(x) > 0 > F(-x)$. $S^1$ is a connected space and $\mathbb{R}$ is an ordered set in the order topology, thus $\exists x'$ between $x$ and $-x$ such that $F(x') = 0$ by theorem 24.3.

    ### Exercise 3

    **Let $f: X \rightarrow X$ be continuous. Show that if $X = [0, 1]$, there is a point $x$ such that $f(x) = x$. The point $x$ is called a fixed point of $f$. What happens if $X = [0, 1)$ or $(0, 1)$**?

    Proof

    Let $F(x) = f(x) - x$, then $F$ is continuous. If $f(0) = 0$ or $f(1) = 1$ then we are done; otherwise we would have $f(0) > 0, f(1) < 1$. Plug into $F$, thus $F(0) = f(0) - 0 > 0, F(1) = f(1) - 1 < 0$, again by theorem 24.3, there exists $0 < x_0 < 1$ such that $F(x_0) = 0 \implies f(x_0) = x_0$.

    The above argument works only because we have two (relatively) known values to work with, thus the argument does not work if $X = [0, 1)$ or $(0, 1)$. Indeed if we take $f$ given by $x \mapsto \frac{1}{2} + \frac{x}{2}$ then it's an counterexample for both situations.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 07""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 24

    ### Exercise 8

    1. **Is a product of path-connected spaces necessarily path-connected**?
    2. **If $A \subseteq X$ and $A$ is path-connected, is $\overline{A}$ necessarily path-connected**?
    3. **If $f:X \rightarrow Y$ is continuous and $X$ is path-connected, is $f(X)$ necessarily path-connected**?
    4. **If $\lbrace A_{\alpha} \rbrace$ is a collection of path-connected subspaces of $X$ and if $\cap A_{\alpha} \ne \varnothing$, is $\cup A_{\alpha}$ necessarily path connected**?

    Solution

    1. Let's call the spaces $X, Y$. By definition, for any $x_0, x_1 \in X, y_0, y_1 \in Y$, there exist $f_x, f_y$ continuous map with $f_x(0) = x_0, f_x(1) = x_1, f_y(0) = y_0, f_x(1) = y_1$. Now take $f = (f_x, f_y)$, by theorem 19.6, $f$ is also continuous, and clearly $f(0 \times 0) = (x_0, y_0), f(1 \times 1) = (x_1, y_1)$. Since $x_0, x_1, y_0, y_1$ are arbitrary, that is to say the product is path-connected. So the answer is yes;
    2. The answer is no, we have topologist's sine curve as a counter-example;
    3. The answer is yes as we proved during the class. Let $y_0, y_1 \in f(X)$ be arbitrary points. Then $\exists x_0, x_1 \in X$ such that $f(x_0)=y_0, f(x_1) = y_1$. Choose a path $\gamma: [0, 1] \rightarrow X$ such that $\gamma(0) = x_0, \gamma(1) = x_1$ then $f \circ \gamma: [0, 1] \rightarrow X \rightarrow Y$ is a path in $Y$ from $f(\gamma(0)) = y_0$ to $f(\gamma(1)) = y_1$;
    4. The answer is yes: Take $a_0 \in \cap A_{\alpha}$ as our 'origin', then for any $a_1, a_2 \in \cup A_{\alpha}$, say $a_1 \in A_{1}, a_2 \in A_{2}$. Since $a_0$ is in the intersection, $a_0 \in A_{1}$ and $a_0 \in A_2$, thus there are paths connecting $a_0$ with $a_1$ and $a_0$ with $a_2$. By pasting lemma, the map connects $a_1$ to $a_0$ then to $a_2$ is also continuous (if in case $a_1 = a_0$ then there is no need to connect $a_1$ to $a_0$, the path from $a_0$ to $a_2$ is intuitively a path connecting $a_1$ and $a_2$, similar with $a_2 = a_0$). Since $a_1, a_2$ are arbitrary, by definition the union is path-connected.

    ### Exercise 10

    **Show that if $U$ is an open connected subspace of $\mathbb{R}^2$, then $U$ is path connected**.

    Proof

    Given $x_0 \in U$, let $A$ be the set of points that can be joined to $x_0$ by a path in $U$. By previous exercise $A$ is path-connected.
    Let $x_1$ be an arbitrary point in $A \subseteq \mathbb{R}^2$, thus $x_1$ is of form $(x, y)$ and there exists a basis element containing $x_1$, $B = (a, b) \times (c, d)$ with $a < x < b, c < y < d$, then for any $b = (x', y') \in B$, simply take $f = (f_x, f_y)$ with $f_x: [0, 1] \rightarrow [x', x], f_y: [0, 1] \rightarrow [y', y]$, $f_x(t) = x' + (1-t)x, f_y(t) = y' + (1-t)y, 0 \le t \le 1$, then $f$ is a path connecting $y, b$, thus $B \subseteq A$. In other word, any point in $A$ has an open set contained in $A$ containing it. By previous exercise we have $A$ is open.

    Now suppose $U - A$ is not empty. Then for any $x_2 \in U - A$ there exists a basis $B' \subseteq U$ containing $x_2$. Suppose $B' \cap A \ne \varnothing$, say it contains $x_3$, then by the above argument, there is a path connecting $x_2$ and $x_3$, but there is also a path connecting $x_3$ and $x_0$, in other word, $x_2 \in A$, which is a contradiction. Thus $B' \subseteq U - A$, again, any point in $U - A$ has an open set contained in $U - A$ containing it, thus $U - A$ is also open.

    Then $U = A \cup (U - A)$ clearly forms a separation, but this contradiction the assumption that $U$ is connected. Thus $U - A$ is empty, i.e. $U = A$.

    We showed at very beginning that $A$ is path-connected, that is, $U$ is path-connected.

    ## Section 26

    ### Exercise 1

    1. **Let $\tau, \tau'$ be two topologies on the set $X$; suppose that $\tau' \supseteq \tau$. What does the compactness of $X$ under one of these topologies imply about compactness under the other**?
    2. **Show that if $X$ is compact Hausdorff under both $\tau, \tau'$, then either $\tau$ and $\tau'$ are equal or they are not comparable**.

    Solution

    1. Suppose $X$ under $\tau'$ is compact. Let $X = \bigcup\limits_{\alpha \in A} U_{\alpha}$ with $U_{\alpha} \in \tau$ be an open covering, since $U_{\alpha} \in \tau \subseteq \tau'$, $X = \bigcup\limits_{\alpha \in A} U_{\alpha}$ can be seen as an open covering with $U_{\alpha} \in \tau'$. By the compactness of $X$ under $\tau'$, there exists a finite sub-covering $X = \bigcup\limits_{i = 1}^n U_{i}$. But this can be seen as a finite sub-covering with $U_i \in \tau$ in the first place. Since the covering is arbitrary, $X$ under $\tau$ is also compact.
    	The argument clearly does not work the other way around. Indeed if we take $[0, 1]$ as our $X$ then it is compact under standard topology; but it does not if lower limit topology is given, for example, no finite sub-collection of $(\bigcup\limits_n [0, 1 - \frac{1}{n})) \cup [1, 2)$ covers $[0, 1]$;
    2. Suppose that $\tau' \supseteq \tau$, take $f: X$ (given $\tau'$) $\rightarrow X$ (given $\tau$) as the inclusion map;
    	1. It is continuous because $\tau \subseteq \tau'$;
    	2. It is clearly a bijection;
    	3. We have $X$ given $\tau'$ is compact and $X$ given $\tau$ is Hausdorff.
	
    	By theorem 26.6 $f$ is a homeomorphism, thus $\tau'$ and $\tau$ are the same.

    ### Exercise 2

    1. **Show that in the finite complement topology on $\mathbb{R}$, every subspace is compact**;
    2. **If $\mathbb{R}$ has the topology consisting of all sets $A$ such that $\mathbb{R} - A$ is either countable or all of $\mathbb{R}$, is $[0, 1]$ a compact subspace**?

    Proof

    1. Let $X$ be a subspace and $X = \bigcup\limits_{\alpha \in A} U_{\alpha}$ be a covering. By definition of finite complement topology each $U_{\alpha}$ contains all but finitely many points of $\mathbb{R}$ thus covers all but finitely many points of $X$. Then the remaining finitely many points can clearly be covered by a finite sub-covering. By definition $X$ is compact;
    2. No, for example, let $A_1 = \mathbb{R} - \lbrace 1, 1/2, 1/3, \dots \rbrace$, $A_2 = \mathbb{R} - \lbrace 1/2, 1/3, \dots \rbrace$, and so on. Then each $R - A_i$ is clearly countable. Then $\bigcup\limits_{i = 1}^{\infty} A_i$ covers $[0, 1]$ but no finite sub-covering can do that.

    ### Exercise 5

    **Let $A, B$ be disjoint compact subspaces of the Hausdorff space $X$. Show that there exist disjoint open sets $U, V$ containing $A, B$ respectively**.

    Proof

    Let $a \in A$, since $A, B$ disjoint clearly we have $a \notin B$, then by lemma 26.4, there exist disjoint open set $U_a \ni a, V_a \supseteq B$. Then $\bigcup\limits_{a \in A}U_a$ forms a covering for $A$. Since $A$ is compact, $\bigcup\limits_{i = 1}^{n}U_i$ is a finite sub-covering. Take $\bigcap\limits_{i = 1}^n V_i$ be the corresponding $V_a \supseteq B$'s, by construction $B \subseteq \bigcap\limits_{i = 1}^n V_i$, $\bigcap\limits_{i = 1}^n V_i$ is intersection of finitely many open sets thus open. If $(\bigcap\limits_{i = 1}^n V_i) \cap (\bigcup\limits_{i = 1}^{n}U_i)$ is not empty, then there exist some $x$ in all $V_i$ and in some $U_i$, but that means $x \in V_j$ and $x \in U_j$ for some particular $j$, which contradict the construction that they are disjoint. Thus $\bigcap\limits_{i = 1}^n V_i, \bigcup\limits_{i = 1}^{n}U_i$ are disjoint, name them $V, U$ and we find the open set required.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 08""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Additional Problems

    ### Problem 1

    **Let $(X, d)$ be a metric space and $A \subseteq X$ its subspace. Define the function $d_A: X \rightarrow \mathbb{R}$ by the formula $d_A(x) = \inf{ \lbrace d(x, a) | a \in A \rbrace}$. Prove that $d_A$ is continuous, and that $d_A(x) = 0$ if and only if $x \in \overline{A}$**.

    Proof

    The second half of the statement:

    1. If $x \in \overline{A}$:
    	$0$ is a lower bound for any metric thus $d_A(x) \ge 0$. Suppose $d_A(x) > 0$. $x \in \overline{A} \implies B = B_d(x, d_A(x))$ is a basis element of $(X, d)$ containing $x$ and it must intersect $A$. Say $a_0 \in A \cap B$, then $a_0 \in A$ and by definition $a_0 \in B \implies d(x, a_0) < d_A(x)$, thus $d_A(x)$ is not the $\inf$. Thus $d_A(x) = 0$;
    2. If $d_A(x) = 0$:
    	If $x \notin \overline{A}$, then there exists basis element $B$ containing $x$ that does not intersect $A$. WLOG say $B = B_d(x, r)$ be a ball centered at $x$ with radius $r (> 0)$, then we have $\forall a \in A, a \notin B \implies d(x, a) \ge r$. Then $r$ is a lower bound of $d(x, a)$ that is greater than $0$, thus $d_A(x) \ge r > 0$ which is a contradiction. Thus $x \in \overline{A}$.

    Now for any $x \in X$ and $V \ni d_A(x) \in \mathbb{R}$, there exists basis element $V \supseteq B_{\mathbb{R}} \ni d_A(x)$ with the form $B_{\mathbb{R}} = (d_A(x) - m, d_A(x) + m)$. Consider the ball $B_X = B_d(x, m/2)$, $d(B_X)$ $= \lbrace \inf{\lbrace d(x', a) | a \in A \rbrace} | x' \in B_X \rbrace$ $\le \lbrace \inf{\lbrace d(x, x') + d(x, a) | a \in A \rbrace} | x' \in B_X \rbrace$ $= \lbrace \inf{\lbrace d(x, a) | a \in A \rbrace} + \inf{\lbrace d(x, x') | a \in A \rbrace} | x' \in B_X \rbrace$ $\le d_A(x) + m/2$; similarly $d(B_X) \ge d_A(x) - m/2$. Thus $B_X$ is an open set in $X$ containing $x$ whose image is contained in open set containing $d_A(x)$, since $x, V$ are arbitrary, $d_A$ is continuous.

    ### Problem 2

    **Let $(X, d)$ be a metric space. Prove that $A \subseteq X$ is bounded if and only if $\text{diam}(A)$ is finite**.

    Proof

    If $A$ is bounded. By definition, there exists $R > 0$ such that $A \subseteq B_d(0, R)$. Then for any $a_1, a_2 \in A, d(a_1, a_2) \le d(a_1, 0) + d(0, a_2) \le 2 R$, thus $2 R$ is an upper bound for $d(a_1, a_2)$ which is finite. Clearly $\text{diam}(A) = \sup\limits{\lbrace d(a_1, a_2) \rbrace} \le 2 R$ is also finite.

    Now say $\text{diam}(A) = R$. Fix an arbitrary point $a_0 \in A$, then for any $a_1 \in A$, $d(a_1, 0) \le d(a_1, a_0) + d(a_0, 0) \le R + d(a_0, 0)$. In other word, $A \subseteq B_d(0, R + d(a_0, 0))$. For fixed $a_0$, $R + d(a_0, 0)$ is clearly defined, thus by definition, $A$ is bounded.

    ### Problem 3

    **Let $GL(2, \mathbb{R})$ denote the set of all $2 \times 2$ matrices $A$ with real entries such that $det(A) \ne 0$. Let $SL(2, \mathbb{R}) \subseteq GL(2, \mathbb{R})$ denote the matrices with $det(A) = 1$. Give $GL(2, \mathbb{R})$ and $SL(2, \mathbb{R})$ topologies by regarding them as subsets of $\mathbb{R}^4$ via $A = \begin{pmatrix} a \ b \\ c \ d \end{pmatrix} \rightarrow (a, b, c, d) \in \mathbb{R}^4$. Determine whether $GL(2, \mathbb{R})$ and $SL(2, \mathbb{R})$ are compact**.

    Solution

    Given any $0 < R \in \mathbb{R}$, consider $A = (R, 0, 0, 1/R)$ then $det(A) = 1$ and $d(A, 0) = \sqrt{R^2 + (1/R)^2} > R$ with the Euclidean metric. Thus $SL(2, \mathbb{R})$ is not bounded, thus it cannot be compact. Exact same argument works for $GL(2, \mathbb{R})$.

    ### Problem 4

    **Let $(X, d)$ be a metric space whose diameter equals $4$, and consider its open covering $X = \bigcup\limits_{x \in X}(X - \lbrace x \rbrace)$. Prove that $\delta = 3$ is a Lebesgue number for this covering**.

    Proof

    Let $A$ be a subset of $X$ with diameter less than $3$. Suppose for any $x \in X$, $x \in A$, then $X \subseteq A$, thus $4 = \text{diam}(X) \le \text{diam}(A) < 3$ which is not true. Thus there exists $x_0 \in X$ such that $x_0 \notin A$. Since $A \subseteq X$ and $x_0 \notin A$, we have $A \subseteq X - \lbrace x_0 \rbrace$. Since $A$ is arbitrary, we have $3$ is a Lebesgue number by definition.

    ### Problem 5

    **Let $D^2 \subseteq \mathbb{R}^2$ be the closed unit disk given by $x^2 + y^2 \le 1$ and let $X = D^2 - \lbrace 0 \rbrace$ with the subspace topology. Show that there exists an open covering of X which does not have Lebesgue number**.

    Proof

    Prove by giving an example:

    Let $U_{\alpha}$ be family of open balls such that the center is on $x^2 + y^2 = 1$ and the radius is $1$.

    Then for any $x \in X, d(x, 0) > 0 \implies d(x, x') < 1$ for some $x'$ on $x^2+y^2 = 1 \implies x \in D(x', 1)$, thus $\cup U_{\alpha}$ forms an open covering of $X$.

    <img src="public/Pasted image 20220326111646.png" width="600" />

    Then for any $\delta$, a punctured disk centered at $0$ with radius less than $\delta/2$ is a subset of $X$ with diameter less than $\delta$, but it is clearly not contained in any $U_{\alpha}$ (because $A$ always contain some point in the 'other' half of the plane opposite with a given $U_{\alpha}$).

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 09""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 17

    ### Exercise 15

    **Show the $T_1$ axiom is equivalent to the condition that for each pair of points of $X$, each has a neighborhood not containing the other**.

    Proof

    By the definition on the book, $X$ is $T_1$ space $\implies \lbrace x \rbrace$ is closed for all $x \in X \implies X - \lbrace x \rbrace$ is open, thus for any $y \ne x$, $X - \lbrace x \rbrace$ is a neighborhood containing $y$ but not $x$;

    On the other hand, for any $x \in X, y \ne x$, there exists neighborhood $U(y) \subseteq X - \lbrace x \rbrace$, by previous exercises, this implies that $X - \lbrace x \rbrace$ is open, i.e. $\lbrace x \rbrace$ is closed.

    ### Exercise 16

    **Consider the five topologies on $\mathbb{R}$ given in Exercise 7 of Section 13 ($\mathbb{R}$, $\mathbb{R}_K$, finite complement topology, $\mathbb{R}_u$, topology with basis $(- \infty, a)$)**:

    1. **Determine the closure of the set $K$ under each of these topologies**.
    	Solution
    	1. $\mathbb{R}$: the closure is clearly $K \cup \lbrace 0 \rbrace$;
    	2. $\mathbb{R}_K$: any point other than point in $K$ has a neighborhood does not include any of $K$ simply by construction, thus any point out side $K$ cannot be a limit point, i.e. the closure is $K$ itself;
    	3. **Finite complement topology**: by previous exercise we have the result any point can be a limit point of $K$ given finite complement topology, i.e. the closure is $\mathbb{R}$;
    	4. $\mathbb{R}_u$: the closure is $K$ itself:
    		for any $a \le 0$, $(a-1,a]$ is a neighborhood of $a$ that does not intersect $K$ (with any other points than $a$);
    		for any $a > 1$, $(1, a]$ does the work;
    		for any $0 < a \le 1$, find the $n$ such that $1/(n+1) < a \le 1/n$, then $(1/(n+1), 1/n]$ does the work;
    	5. **Topology with basis $(- \infty, a)$**: it is clear that as long as $a > 0$, $(- \infty, a)$ intersects $K$ with infinitely many points. Thus the closure is $\mathbb{R}_+$;
    2. **Which of these topologies satisfy the Hausdorff axiom? the $T_1$ axiom**?
    	Solution
    	1. $\mathbb{R}$: it is clearly Hausdorff, and thus satisfies $T_1$ axiom;
    	2. $\mathbb{R}_K$: $K$-topology is strictly finer than the standard topology, thus it also satisfies both axioms;
    	3. **Finite complement topology**: it is not Hausdorff, because for any two distinct points, their neighborhoods together can only exclude finitely many points, i.e. any two neighborhoods of them contains infinitely many points in common. It is $T_1$: for any $x \ne y$, $\mathbb{R} - \lbrace y \rbrace$ is a neighborhood of $x$ exclude $y$ and $\mathbb{R} - \lbrace x \rbrace$ is a neighborhood of $y$ exclude $x$;
    	4. $\mathbb{R}_u$: upper limit topology is strictly finer than the standard topology, thus it also satisfies both axioms;
    	5. **Topology with basis $(- \infty, a)$**: it is not Hausdorff: for any $x \ne y$ and any neighborhood $U(x), U(y)$, $U(x)$ contains basis element $(- \infty, x)$ and $U(y)$ contains basis element $(- \infty, y)$, they clearly intersect. It is neither $T_1$: WLOG say $x > y$ then the neighborhood of $x$ contains $y$.

    ## Section 28

    ### Exercise 4

    **A space $X$ is said to be countably compact if every countable open covering of $X$ contains a finite sub-collection that covers $X$. Show that for a $T_1$ space $X$, countable compactness is equivalent to limit point compactness**. *Hint: If no finite sub-collection of $U_n$ covers $X$, choose $x_n \notin U_1 \cup \dots \cup U_n$ for each $n$*.

    Proof

    1. Countable compactness $\implies$ limit point compactness:
    	Suppose that $X$ is countably compact and $Y \subseteq X$ is an infinite subset of $X$. Let $Z \subseteq Y$ be a countably infinite subset of $Y$. If $z$ is a limit point of $Z$, by definition any of its neighborhood intersects with $Z$ other than $z$, thus it clearly also intersects with $Y$ other than $z$, i.e. limit point of $Z$ is limit point of $Y$.
    	Suppose $Z$ has no limit point, then $Z$ is closed (in $X$). If $\bigcup\limits_{\omega}U$ is a countable open covering of $Z$, then $\bigcup\limits_{\omega}U \cup (X - Z)$ is a countable open covering of $X$, thus it admit a finite sub-covering, which is a finite sub-covering of $Z$ if we then remove $(X - Z)$, i.e. $Z$ is countably compact.
    	On the other hand, by definition of (having no) limit point, $\forall z \in Z$, $\exists U(z) \ni z$ such that $U(z) \cap Z = \lbrace z \rbrace$. Since $Z$ is countable, $\bigcup\limits_z U(z)$ is a countable open covering of $Z$, thus by above argument, it admit a finite sub-covering, but this implies that $Z$ is finite, which is a contradiction. Thus $Z$ has limit point(s), so does $Y$;
    2. Limit point compactness $\implies$ countable compactness:
    	Suppose $X$ is limit-point compact and $\bigcup\limits_{\omega}U$ is a countable open covering of $X$. Suppose that no finite sub-collection of $U$'s covers $X$. Let $V_n = U_1 \cup \dots \cup U_n$, by construction $V_n$ does not cover $X$. Thus we can choose $x_n \notin V_n$ for each $n$. This defines a sequence in $X$, thus by definition it has a limit point $x \in X$. Notice that however since $\cup_{\omega} U$ covers $X$, there does exist $V_{n_{x'}} \ni x'$ for all $x' \in X$. Thus there exists $V_{n_x} \ni x$. For a given sequence $n_x$ would be fixed (finite) thus $V_{n_x}$ can contain only finitely many $x_i$'s, say they are $x_n, \dots, x_{n + m}$. Since $X$ is $T_1$, for each of $x_i \in \lbrace x_n, \dots, x_{n + m} \rbrace$ we can find $U(x)_{x_{i}}$ containing $x$ but not $x_i$. Then $\cap_i (V_{n_x} \cap U(x){x_i})$ (is intersection of finitely many open sets thus open) contains $x$ but none of the element in the sequence, thus $x$ is not a limit point, which is a contradiction, thus $\cup_{\omega}U$ admits finite sub-covering.

    ### Exercise 7

    **Let $(X, d)$ be a metric space. If $f$ satisfies the condition $d(f(x), f(y)) < d(x, y)$ for all $x, y \in X$ with $x \ne y$, then $f$ is called a shrinking map. If there is a number $\alpha < 1$ such that $d(f(x), f(y)) \le \alpha d(x, y)$ for all $x, y \in X$, then $f$ is called a contraction. A fixed point of $f$ is a point $x$ such that $f(x) = x$**.

    1. **If $f$ is a contraction and $X$ is compact, show $f$ has a unique fixed point**. *Hint: Define $f^1 = f$ and $f^{n + 1} = f \circ f^n$. Consider the intersection $A$ of the sets $A_n = f^n(X)$*;
    2. **Show more generally that if $f$ is a shrinking map and $X$ is compact, then $f$ has a unique fixed point**. *Hint: Let $A$ be as before. Given $x \in A$, choose $x_n$ so that $x = f^{n+1}(x_n)$. If $a$ is the limit of some subsequence of the sequence $y_n = f^n(x_n)$, show that $a \in A$ and $f(a) = x$. Conclude that $A = f(A)$, so that $\text{diam}(A) = 0$*;
    3. **Let $X = [0, 1]$. Show that $f(x) = x - x^2/2$ maps $X$ into $X$ and is a shrinking map that is not a contraction**. *Hint: Use the mean-value theorem of calculus*;
    4. **The result in (i). holds if $X$ is a complete metric space, such as $\mathbb{R}$; see the exercises of Section $43$. The result in (ii). does not: Show that the map $f: \mathbb{R} \rightarrow \mathbb{R}$ given by $f(x) = [x + (x^2 + 1)^{1/2}]/2$ is a shrinking map that is not a contraction and has no fixed point**.

    Proof

    1. (Assume from the statement that $f$ is a map from $X$ to $X$)
    	Define $f^1 = f$ and $f^{n + 1} = f \circ f^n$. Consider the intersection $A$ of the sets $A_n = f^n(X)$.
    	$A_1 = f(X)$ is image of compact space under continuous map thus compact, and it is subspace of a Hausdorff (metric) space thus closed. By a regular induction step, it is easy to see that $A_n = f^n(X)$ is compact and closed for all $n$.
    	Suppose $x \in A$ then $x \in A_n$ for all $n$, thus $f(x) \in A_n$ for all $n > 1$, but $f(x)$ is naturally contained in $A_1 = f(X)$, thus $f(x) \in A_n$ for all $n$ thus $f(x) \in A$. Thus $f(A) \subseteq A$.
    	Similarly we can see that $f^{n+1}(X) \subseteq f^n(X)$ for all $n$, each of them would be non-empty, thus their intersection $A$ (of a sequence of nested nonempty compact sets) is non-empty.
    	Now suppose $f$ is a contraction, then $d(f^n(x), f^n(y))$ $\le \alpha d(f^{n-1}(x), f^{n-1}(y))$ $\le \alpha^2 d(f^{n-2}(x), f^{n-2}(y))$ $\le \dots$ $\rightarrow 0$ for some $\alpha < 1$, thus $A$ can have only one point $a$, since $f(A)$ is non-empty it must also be that exact point, i.e. it is the fixed point.
    	To show this is the only fixed point: suppose $x, y$ are both fixed point, then $d(f(x), f(y)) = d(x, y) \le \alpha d(x, y) < d(x, y)$ which is impossible;
    2. The part of last problem in blue still holds. We want to show that for a shrinking map, $A$ still can have only one point.
    	Given $x \in A$, choose a sequence of $x_n$ so that $x = f^{n+1}(x_n)$, we can do this because $x$ is in the intersection thus we can always achieve this value. Let $y_n = f^n(x_n)$, consider the sequence $y_n$, since $X$ is compact and metric, $X$ is sequentially compact, thus there is a subsequence of $y_n$ converges to some $a$. Thus any neighborhood of $a$ contains infinitely many points of the subsequence, in other word any neighborhood of $a$ intersect with $A_n$ for all $n$, thus $a \in \overline{A_n}$ for all $n$. Now by above argument, $A_n$ is closed, thus $\overline{A_n} = A_n$, $a \in A_n$ for all $n$ thus $a \in A$. By construction we have $f(y_n) = f \circ f^n(x_n) = f^{n+1}(x_n) \equiv x$, thus $f(a) = x$. Since the choice of $x$ is arbitrary, $A \subseteq f(A)$, combining with above argument we have $A = f(A)$. This causes trouble, as shrinking map requires the image to be 'smaller'.
    	Suppose there are more than one points in $A$. Suppose $x = f(x'), y = f(y')$ is a pair of point in $A$ with the largest distance, then $d(x, y) = d(f(x'), f(y')) < d(x', y') \le d(x, y)$, which is a contradiction. Thus there is only one point in $A$ and by construction it is the fixed point.
    	To show this is the only fixed point is similar: suppose $x, y$ are both fixed point, then $d(f(x), f(y)) = d(x, y) < d(x, y)$ which is impossible;
    3. It is easy to see $f([0,1]) = [0, 1/2]$ and it is strictly increasing, thus it maps $X$ to $X$, not surjective, though.
    	For $y > x$, $d(f(x),f(y)) = f(y) - f(x) = y - y^2/2 - x + x^2/2 = (y-x)(1-(y+x)/2)$. For $x \ne y \in [0, 1]$, $(1-(y+x)/2)$ clearly greater then $0$ less then $1$ thus $d(f(x),f(y)) < y-x = d(x, y)$ thus it is a shrinking map.
    	For any given $\alpha > 0$, choose small enough $\varepsilon$ then $d(f(0),f(\varepsilon)) = f(0) - f(\varepsilon) = \varepsilon - \varepsilon^2/2 > \alpha \varepsilon = \alpha d(0, \varepsilon)$, thus it is not a contraction;
    4. Clearly this is a strictly increasing map, and for $y > x$, $d(f(x), f(y))$ $= f(y) -f(x)$ $= \frac{y + \sqrt{y^2+1}}{2} - \frac{x + \sqrt{x^2+1}}{2}$ $< \frac{y - x + y - x}{2}$ $= y - x$ ($<$ holds because we implicitly choose $y > x$) thus it is a shrinking map.
    	Similar as above, we can see the limit of $f(y) - f(x)$ is indeed $y - x$, thus for any fixed $\alpha$ if we choose $x ,y$ large enough then $f(y) - f(x)$ will not be bounded by $\alpha(y-x)$, thus it is not a contraction.
    	$f(x) > \frac{x + x}{2} = x$ for all $x$ thus there is no fixed point.

    ## Section 29

    ### Exercise 6

    **Show that the one-point compactification of $\mathbb{R}$ is homeomorphic with the circle $S^1$**.

    Proof

    $\mathbb{R}$ is homeomorphic with the open interval $(0, 2 \pi)$, now define $f: (0, 2 \pi) \rightarrow S^1 - \lbrace (1, 0) \rbrace$ by $f(\theta) = (\cos(\theta), \sin(\theta))$, $f$ is clearly a homeomorphism. Thus $\mathbb{R}$ is homeomorphic with the unit circle with one point removed.
    Now by definition, $S^1$ is compact Hausdorff and $S^1 - \lbrace (1, 0) \rbrace$ is a proper subspace whose closure is clearly $S^1$, thus $S^1$ is a one-point compactification of $S^1 - \lbrace (1, 0) \rbrace$. Thus $S^1$ is homeomorphic with the one-point compactification of $\mathbb{R}$.

    ### Exercise 8

    **Show that the one-point compactification of $\mathbb{Z}_+$ is homeomorphic with the subspace $\lbrace 0 \rbrace \cup \lbrace 1/n | n \in \mathbb{Z}_+ \rbrace$ of $\mathbb{R}$**.

    Proof

    $\mathbb{Z}_+$ is homeomorphic with $K = \lbrace 1/n | n \in \mathbb{Z}_+ \rbrace$ by the continuous bijection $f(n) = 1/n$. From the previous exercise $\lbrace 0 \rbrace \cup K$ is the one-point compactification of $K$ thus the one-point compactification of $\mathbb{Z}_+$ is homeomorphic with $\lbrace 0 \rbrace \cup \lbrace 1/n | n \in \mathbb{Z}_+ \rbrace$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 10""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 30

    ### Exercise 4

    **Show that every compact metrizable space $X$ has a countable basis**.

    Proof

    For each $n \in \mathbb{N}$, let $A_n$ be a finite covering of $X$ by $\frac{1}{n}$-balls. Consider their union $\bigcup A_n$, it's a union of countable many finite sets thus it is countable, we claim it is a basis for topology on $X$:

    1. All $x \in X$ are covered, because each $A_n$ covers $X$ already;
    2. If $x \in B_{\frac{1}{n}}(a)$ and $x \in B_{\frac{1}{m}}(b)$, then $d(x,a) + d(x,b) < \frac{1}{n} + \frac{1}{m}$, thus there exists $\varepsilon > 0$ such that $4\varepsilon + d(x,a) + d(x,b) < \frac{1}{n} + \frac{1}{m}$, it follows that any ball with radius $\varepsilon$ contains $x$ is contained in the intersection $B_{\frac{1}{n}}(a)$ and $B_{\frac{1}{m}}(b)$. Take $n'$ large enough, we can get $\frac{1}{n'} < \varepsilon$. Since by construction $A_{n'}$ covers $X$, we can find a such ball.

    ## Section 32

    ### Exercise 3

    **Show that every locally compact Hausdorff space is regular**.

    Proof

    Say $X$ is a locally compact Hausdorff space. Let $A$ be an arbitrary closed (proper) subset and $x \in X - A$. Since $X$ is locally compact, there exists $U_0(x)$ neighborhood of $x$ such that $\overline{U_0(x)}$ is compact, thus closed since $X$ is Hausdorff.

    Consider $A \cap \overline{U_0(x)}$. Since $A$ is closed in $X$, this intersection is closed in $\overline{U_0(x)}$, thus it is compact. From previous materials we can find $U \ni x$ and $W \supset (A \cap \overline{U_0(x)})$, two disjoint open sets in $\overline{U_0(x)}$. Now consider $V = W \cup (X - \overline{U_0(x)})$, it is open in $X$ and it is disjoint from $U$. Any point in $A$ is either in $W \cap A$ or $(X - \overline{U_0(x)}) \cap A$, because $(\overline{U_0(x)} - W)\cap A$ $=(\overline{U_0(x)}\cap A)- (W\cap A)$ $= \varnothing$, implies $A \subseteq V$. Thus we find $U \ni x$ and $V \supseteq A$, disjoint open sets in $X$, thus $X$ is regular.

    ## Section 34

    ### Exercise 1

    **Give an example showing that a Hausdorff space with a countable basis need not be metrizable**.

    Proof

    We learnt that $\mathbb{R}_k$ is Hausdorff but not regular, and it has a countable basis, thus $\mathbb{R}_k$ is not metrizable.

    ### Problem 6

    **Prove that the plane $\mathbb{R}^2$ with the dictionary order topology is metrizable but not second-countable**.

    Proof

    From previous homework we know that the dictionary order topology on $\mathbb{R}^2$ is the same as $\mathbb{R}_d \times R$. Since $R_d$ is metrizable with discrete metric and $\mathbb{R}$ is metrizable with Euclidean metric, their product is metrizable with $\rho((x_1,y_1),(x_2,y_2)) = \max(d_d(x_1,y_1), d(x_2,y_2))$.

    For each $x \in \mathbb{R}$, $\lbrace x \rbrace \times \mathbb{R}$ is open in $\mathbb{R}_d\times \mathbb{R}$, so there must be a basis element $B_x$ s.t. $B_x \subset \lbrace x \rbrace \times \mathbb{R}$. Clearly if $x \ne y$, $B_x \cap B_y = \varnothing$, thus (any) basis $B = \lbrace B_x \rbrace$ cannot be countable, thus $\mathbb{R}_d \times \mathbb{R}$ (and thus the dictionary order topology) is not second countable.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 11""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 35

    ### Exercise 1

    **Show that the Tietze extension theorem implies the Urysohn lemma**.

    Proof

    Let $A, B$ be two disjoint closed sets in a normal space $X$. Define $f: A \cup B \rightarrow [a, b]$ as $f(x) = a, \forall x \in A; f(x) = b, \forall x \in B$, it is easy to see this is a continuous map (preimage of open set is open). $A \cup B$ is closed, thus Tietze extension theorem implies that this map can be extended to continuous map $X \rightarrow [a, b]$ of the form as the Urysohn lemma described.

    ### Exercise 4

    **Let $Z$ be a topological space. If $Y$ is a subspace of $Z$, we say that $Y$ is a retract of $Z$ if there is a continuous map $r: Z \rightarrow Y$ such that $r(y) = y$ for each $y \in Y$**.

    1. **Show that if $Z$ is Hausdorff and $Y$ is a retract of $Z$ then $Y$ is closed in $Z$**.	
    2. **Let $A$ be a two-point set in $\mathbb{R}^2$. Show that $A$ is not a retract of $\mathbb{R}^2$**;
    3. **Let $S^1$ be the unit circle in $\mathbb{R}^2$. Show that $S^1$ is a retract of $\mathbb{R}^2 - \lbrace 0 \rbrace$, where $0$ is the origin. Can you conjecture whether or not $S^1$ is a retract of $\mathbb{R}^2$**?

    Proof

    1. Let $x \in Z - Y$. Since $r$ is a function, there exists some $y \in Y$ such that $r(x) = y$. Clearly $x \ne y$, thus Hausdorff properties implies that there exists disjoint open sets $U \ni x, V \ni y$. Since $V$ is open in $Z$, $V \cap Y$ is open in $Y$; since $r$ is continuous, $r^{-1}(V \cap Y)$ is open in $Z$. Note that this set contains $x$, because $y \in V$ and $y \in Y$ and $x \in r^{-1}(y)$. Finally consider $W = U \cap r^{-1}(V \cap Y)$:
    	1. It is open and contains $x$ thus is a neighborhood of $x$;
    	2. It does not intersect with $Y$: if $y_0 \in r^{-1}(V \cap Y), y_0 \in Y$ then by construction it is in $V$, but we know $U, V$ are disjoint.
    		Since $x$ is arbitrary, we have that for any $x \in Z - Y$, there is a neighborhood of $x$ lies in $Z - Y$, by an exercise we did long time ago, this implies $Z - Y$ is open, i.e. $Y$ closed;
    2. Each point in $A$ is clearly open thus its pre-images are open, disjoint (otherwise $r$ is not a function), non-empty (the preimage contains the mapped point for sure), and their union is the whole space (again, otherwise $r$ is not a function). But then by definition these two pre-image sets form a separation of $\mathbb{R}^2$, which is a contradiction because $\mathbb{R}^2$ should be connected;
    3. Define $r: \mathbb{R}^2 - \lbrace 0 \rbrace \rightarrow S^1$ as $x \mapsto \frac{x}{d(x,0)}$ where $d$ is the Euclidean metric, i.e. all points on a ray projected from the origin is mapped to the point where this ray intersect the unit circle.
    	This is a continuous map ($f(\overline{A}) \subseteq \overline{f(A)}$), thus $S^1$ is a retract of $\mathbb{R}^2 - \lbrace 0 \rbrace$.
    	I would conjecture that $S^1$ is not a retract of $\mathbb{R}^2$, otherwise $0$ must be mapped to something on the circle, while points near around $0$ are mapped to (everywhere of) the unit circle (this clearly would be the hard part to prove, if the proof follows this argument… I guess), so image of 'near' points are not 'near', i.e. the map would not be continuous;

    ## Section 36

    ### Exercise 5

    **The Hausdorff condition is an essential part of the definition of a manifold; it is not implied by the other parts of the definition. Consider the following space: Let $X$ be the union of the set $\mathbb{R} - \lbrace 0 \rbrace$ and the two-point set $\lbrace p, q \rbrace$. Topologize $X$ by taking as basis the collection of all open intervals in $\mathbb{R}$ that do not contain $0$, along with all sets of the form $(-a, 0) \cup \lbrace p \rbrace \cup (0, a)$ and all sets of the form $(-a, 0) \cup \lbrace q \rbrace \cup (0, a)$, for $a > 0$. The space $X$ is called the line with two origins**.

    1. **Check that this is a basis for a topology**;
    2. **Show that each of the spaces $X - \lbrace p \rbrace$ and $X - \lbrace q \rbrace$ is homeomorphic to $\mathbb{R}$**;
    3. **Show that $X$ satisfies the $T_1$ axiom, but is not Hausdorff**;
    4. **Show that $X$ satisfies all the conditions for a $1$-manifold except for the Hausdorff condition**.

    Proof

    1. Follow the axioms:
    	1. All point of $\mathbb{R} - \lbrace 0 \rbrace$ is clearly included by some open interval does not contain $0$; and $p, q$ are clearly included by basis element of the $(-a, 0) \cup \lbrace p \rbrace \cup (0, a)$ or $(-a, 0) \cup \lbrace q \rbrace \cup (0, a)$ form;
    	2. If $x$ is in the intersection of two open intervals then it is in a smaller open interval in the intersection. Otherwise $x$ is in the intersection $((-a, 0) \cup (0, a)) \cap ((-b, 0) \cup (0, b))$, while either $a \le b$ or $a > b$, either case one basis element lies completely in the other.
    		By definition, this is a basis for a topology;
    2. Consider the map $f: \mathbb{R} \rightarrow X - \lbrace p \rbrace = \mathbb{R} - \lbrace 0 \rbrace + \lbrace q \rbrace$ given by $x \mapsto x$ for all $x \ne 0$ and $0 \mapsto q$. So basically we just gives $0$ a new name, namely $q$. This is a continuous map, as preimage of each basis element is clear open: preimage of basis element of the form $(a, b), 0 \notin (a, b)$ is itself, and preimage of basis element of the form $(-a, 0) \cup \lbrace q \rbrace \cup (0, a)$ is $(-a, 0) \cup \lbrace 0 \rbrace \cup (0, a) = (-a, a)$. The map is clearly a bijection and its inverse, similar with the above argument, is also continuous, thus it is a homeomorphism, i.e. $X - \lbrace p \rbrace$ is homeomorphic to $\mathbb{R}$.
    	$X - \lbrace q \rbrace$ is homeomorphic to $\mathbb{R}$ with the very similar argument;
    3. Being $T_1$:
    	1. Any basis element containing $p$ does not contains $q$;
    	2. For any $b \ne 0$, take $a < | b |$ then $(-a, 0) \cup \lbrace p \rbrace \cup (0, a)$ is a neighborhood of $p$ not containing $b$;
    	3. For any $a, b \ne 0$, take small enough $\varepsilon > 0$ we would have $(a - \varepsilon, a + \varepsilon)$ containing neither $p, q$ or $b$.
		
	
    	That are all the situations, in each case we can separate two points in the way $T_1$ axiom requires, thus the space is $T_1$.
    	Not being Hausdorff:
    	$p, q$ cannot be separated: any neighborhood of $p$ contains a basis element of the form $(-a, 0) \cup \lbrace p \rbrace \cup (0, a)$ and any neighborhood of $q$ contains a basis element of the form $(-b, 0) \cup \lbrace q \rbrace \cup (0, b)$. They clearly intersect each other;
    4. Follow the definition:
    	1. We just showed above it is not Hausdorff;
    	2. $X = (X - \lbrace p \rbrace) \cup (X - \lbrace q \rbrace)$, each point of $X$ is clearly in (at least) one of the above subsets, which we proved above is homeomorphic to $\mathbb{R}$ itself;
    	3. $X$ does have a countable basis (as $\mathbb{R}$ does): take all the basis element described in the exercise: $(a, b)$ not containing $0$, $(-c, 0) \cup \lbrace p \rbrace \cup (0, c)$, $(-d, 0) \cup \lbrace p \rbrace \cup (0, d)$, but with $a, b, c, d$ rational.

    ## Additional Problem

    ### Problem 7

    **Let $A$ be a subspace of a regular space $X$ and consider the partition of $X$ which consists of $A$ and the singletons $\lbrace x \rbrace$ for all $x \notin A$. This partition defines an equivalence relation on $X$ whose quotient space (with quotient topology) is called $X/A$. Prove that $X/A$ is Hausdorff if and only if $A$ is closed**.

    Proof

    ($\implies$) Suppose $X/A$ is Hausdorff, then $\lbrace a \rbrace$ is closed thus the preimage under the quotient map (which is continuous), which is exactly $A$, is closed.

    ($\impliedby$) Suppose $A$ is closed, then there exists disjoint open sets $U \ni x, V \supseteq A$ in $X$ because $X$ is regular. Consider the quotient map $p: X \rightarrow X/A$, say $p(A) = a$:

    1. $a \notin p(U)$: otherwise there exists $a' \in U$ such that $p(a') = a$, but that by construction means $a' \in A$, i.e. $U \cap A \ne \varnothing$;
    2. $p(U), p(V)$ are actually disjoint: we just showed that $a$ cannot be in the intersection, thus the intersection can only contains singletons, but that also cannot happen because $y \in p(U) \cap p(V) \implies y \in U \cap V$ which is impossible.

    Thus $p(U), p(V)$ are disjoint open (since $p$ is quotient) sets containing $x, a$ respectively. For $x, y \ne p^{-1}(A)$, the argument still holds (and simpler, because they are then both singletons). Thus $X/A$ is Hausdorff.

    ### Problem 8

    **The second-countability is an essential part of the definition of a manifold: show that $\mathbb{R}^2$ with the dictionary order topology satisfies all the conditions for a $1$-manifold except for second-countability**.

    Proof

    We use the fact that this topology is the same as $\mathbb{R}_d \times \mathbb{R}$.

    1. We showed in the last homework that it is not second-countable;
    2. Each point $(a, b)$ in $\mathbb{R}^2$ is contained in $\lbrace a \rbrace \times (c, d)$ for some $c < b < d$, which is homeomorphic to $(c, d) \subseteq \mathbb{R}$;
    3. It is Hausdorff, consider $(a_0, b_0), (a_1, b_1) \in \mathbb{R}^2$:
    	1. If $a_0 \ne a_1$ then any $\lbrace a_0 \rbrace \times (c_0, d_0), c_0 < b_0 < d_0$ and $\lbrace a_1 \rbrace \times (c_1, d_1), c_1 < b_1 < d_1$ do the separation;
    	2. If $a_0 = a_1$ then we need to separate $b_0, b_1$ on the real line, this is clearly doable, as $\mathbb{R}$ is Hausdorff.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 12""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 28

    ### Exercise 6

    **Let $(X, d)$ be a metric space. If $f: X \rightarrow X$ satisfies the condition $d(f(x), f(y)) = d(x, y)$ for all $x, y \in X$, then $f$ is called an isometry of $X$. Show that if $f$ is an isometry and $X$ is compact, then $f$ is bijective and hence a homeomorphism**.

    Proof

    1. $f$ is injective: $f(x) = f(y) \implies d(f(x), f(y)) = 0 = d(x, y) \implies x = y$;
    2. $f$ is continuous: by Theorem 21.1., simply take $\delta = \varepsilon$ we would have $d(f(x), f(y)) = d(x, y) < \delta = \varepsilon$, thus $f$ is continuous;
    3. $f$ is surjective: suppose we have an $a$ which is not in the image of $f(X)$. Since $f$ is continuous and $X$ is compact, $f(X)$ is compact and thus closed. Thus $a \notin \overline{f(X)}$, thus there exists $\varepsilon > 0$ such that $B_d(a, \varepsilon)$ (being a basis element containing $a$) that does not intersect with $f(X)$.

    Set $x_1 = a$ and $x_{n+1} = f(x_n)$. Then for any $n \ne m$ we have $d(x_n, x_m)$ $= d(f(x_{n-1}), f(x_{m-1}))$ $= d(x_{n-1}, x_{m-1})$ $= \dots$ $= d(x_{n-m+1}, x_1)$, which must $\ge \varepsilon$ because $x_{n-m+1}$ is by construction in $f(X)$ thus not in the $\varepsilon$-ball centered at $x_1 = a$. But then this means $X$ is not sequentially compact, thus not compact, which is a contradiction.

    ## Section 43

    ### Exercise 3

    **Two metrics $d$ and $d'$ on a set $X$ are said to be metrically equivalent if the identity map $i: (X, d) \rightarrow (X, d')$ and its inverse are both uniformly continuous**.

    1. **show that $d$ is metrically equivalent to the standard bounded metric $\overline{d}$ derived from $d$**;
    2. **Show that if $d$ and $d'$ are metrically equivalent, then $X$ is complete under $d$ if and only if it is complete under $d'$**.

    Proof

    1. Consider the function $i: (X, d) \rightarrow (X, \overline{d})$. For any $\varepsilon > 0$, take $\delta = \varepsilon$ then for any $x_1, x_2 \in X, \overline{d}(i(x_1), i(x_2)) = \overline{d}(x_1, x_2) =$, since we essentially only interested in those small enough (namely those less than $1$), this is by definition the same as $= d(x_1, x_2) < \delta = \varepsilon$, thus by definition, $i$ is uniformly continuous;
    	Similarly consider the function $i': (X, \overline{d}) \rightarrow (X, d)$. For any $\varepsilon > 0$, take $\delta = \varepsilon$ then for any $x_1, x_2 \in X$, $d(i'(x_1), i'(x_2)) = d(x_1, x_2) = \overline{d}(x_1, x_2) < \delta = \varepsilon$ thus $i'$ is uniformly continuous.
    	By above definition $d$ is metrically equivalent to $\overline{d}$;
    2. Suppose $X$ is complete under $d$ and let $x_n$ be a Cauchy sequence in $X$ with respect to $d'$. For any $\varepsilon_{d'} > 0$, we can find $N_{d'}$ such that $d'(x_n, x_m) < \varepsilon_{d'}$ for all $n, m > N_{d'}$.
    	Since the function $i': (X, d') \rightarrow (X, d)$ is uniformly continuous, for any $\varepsilon_d > 0$, we can find $\delta_d$ such that $d'(x_1, x_2) < \delta_a \implies d(x_1, x_2) < \varepsilon_d$. Take $\varepsilon_{d'} < \delta_d$, we would have $d'(x_n, x_m) < \varepsilon_{d'} < \delta_d \implies d(x_n, x_m) < \varepsilon_d$ for all $n, m > N_{d'}$. Thus $x_n$ is a Cauchy sequence respect to $d$, thus it has a convergent sub-sequence $x_{n_k}$ with respect to $d$.
    	Say $\lim\limits x_{n_k} = x$, given any $\varepsilon > 0$, find $N$ such that $d'(x_n, x_m) < \varepsilon/2, \forall n, m > N$. Since the function $i: (X, d) \rightarrow (X, d')$ is uniformly continuous, similar with the above argument, we can take small enough $\varepsilon'$ so that $d(x_{n_k}, x) < \varepsilon' \implies d'(x_{n_k}, x) < \varepsilon/2$ with $n_k \ge N$. Then $d'(x_{n}, x) \le d'(x_n, x_{n_k}) + d'(x_{n_k}, x) < \varepsilon$ for all large enough $n$'s, i.e. $x_n$ converge to $x$ respect to $d'$. Since $x_n$ is arbitrary, $X$ is complete under $d'$.
    	The statement is in if and only if form but is symmetric, thus both ways hold.

    ### Exercise 4

    **Show that the metric space $(X, d)$ is complete if and only if for every nested sequence $A_1 \supseteq A_2 \supseteq \dots$ of non-empty closed sets of $X$ such that $\text{diam}(A_n) \rightarrow 0$, the intersection of the sets $A_n$ is non-empty**.

    Proof

    ($\implies$) Suppose $(X, d)$ is complete and we have a nested sequence described as above. For each $n$, choose $x_n \in A_n$.

    This is a Cauchy sequence: for any $\varepsilon > 0$, find $N$ such that $\text{diam}(A_n) < \varepsilon$ for all $n > N$. Then for any $m, n > N$ we have $x_m \in A_m \subseteq A_N$ and $x_n \in A_n \subseteq A_N$, thus $d(x_m, x_n) \le \text{diam}(A_N) < \varepsilon$. Sinnce $X$ is complete, we have $\lim\limits x_n = x$, for some $x$.

    $x$ is in the intersection: for any fixed $n$, for any $m > n$, we have $x_m \in A_m \subseteq A_n$ thus $\lbrace x_n, x_{n+1}, \dots \rbrace \subseteq F_n$. This is clearly a subsequence of $x_n$, thus it has limit point $x$, which must lie in $A_n$ since $A_n$ is closed. Thus $x$ is in $n$ for all $n$, i.e. it is inside the intersection. Thus the intersection is non-empty.

    ($\impliedby$) Now suppose $x_n$ is a Cauchy sequence in $(X, d)$.

    Take $A_1 = X$ be a non-empty closed set of $X$, it contains all of $x_i$'s; Since $X$ is metric thus Hausdorff, $x_1$ and $x_i, i>1$ can be separated by disjoint open balls. Since $x_n$ is Cauchy, eventually for some $x_N$, $B_d(x_N, \varepsilon)$ does not contain $x_1$ and it contains all $x_i, i \ge N$. Thus this finite intersection of $\bigcap\limits_{n = 2}^N B_d(x_1, \varepsilon_n)$ (where each $B_d(x_1, \varepsilon_n)$ contains $x_1$ but not $x_n$) is open, contains $x_1$, but contains none of the other $x_i$'s. Let $A_2 = A_1 - \bigcap\limits_{n = 2}^N B_d(x_1, \varepsilon_n)$, then $A_2$ is a non-empty closed set of $X$, it contains all of $x_i$'s other than $x_1$;

    Continue inductively we may find a (clearly it is nested) sequence of non-empty closed sets $A_n$'s, each $A_n$ contains all but the first $n-1$ terms of $x_n$. $\text{diam}(A_n) \rightarrow 0$: since $x_n$ is Cauchy, for any $\varepsilon > 0$ we can find $N$ such that all $x_i$'s with $i > N$ is contained in a set with \text{diam}eter $\varepsilon$, but this means $\text{diam}(A_{n+1})$ must smaller than $\varepsilon$, otherwise it would also contain the unwanted $n+1$-th element of $x_n$. Since $\varepsilon$ is arbitrary, we have $\text{diam}(A_n) \rightarrow 0$.

    Now suppose the intersection of this nested sequence is not empty, i.e. contains some $x$, claim $\lim\limits x_n = x$: for any $\varepsilon > 0$, there exists $N$ such that $\text{diam}(A_n) < \varepsilon$ and contains infinitely many $x_i$'s by construction; since $X$ is metric thus regular, we can find open $V \supseteq A_n$ with $\text{diam}(V) < \varepsilon$. Then $V$ is a neighborhood of $x$ containing all but finitely many $x_i$'s, since $\varepsilon$ is arbitrary, $\lim\limits x_n = x$, thus $X$ is complete.

    ### Exercise 5

    **If $(X, d)$ is a metric space , recall that a map $f: X \rightarrow X$ is called a contraction if there is a number $\alpha < 1$ such that $d(f(x), f(y)) \le \alpha d(x, y)$ for all $x, y \in X$. Show that if $f$ is a contraction of a complete metric space, then there is a unique point $x \in X$ such that $f(x) = x$**.

    Proof

    Let $x_0$ be an arbitrary point in $X$, inductively define $x_{n+1} = f(x_n)$ (so that $x_n = f^n(x_0)$).

    $x_n$ is Cauchy: for any $m > n$ we have $d(x_m, x_n) = d(f^m(x_0), f^n(x_0)) \le \alpha d(f^{m-1}(x_0), f^{n-1}(x_0))$ $\le \dots \le \alpha^n d(f^{m-n}(x_0), x_0)$, this is not enough, as the $f^{m-n}$ part may get arbitrarily far away from $x_0$, so we decompose the distance part to get: $\le \alpha^n(d(f^{m-n}(x_0), f^{m-n-1}(x_0)) + d(f^{m-n-1}(x_0), f^{m-n-2}(x_0)) + \dots + d(f(x_0), x_0)$ $= \alpha^n (\alpha^{m-n-1} d(f(x_0),x_0) +$ $\dots + d(f(x_0),x_0))$ $\le \alpha^n (\sum\limits_{i = 0}^{\infty} \alpha_i)d(f(x_0), x_0)$ $= \frac{\alpha^n}{1 - \alpha}d(f(x_0), x_0)$ and now it is safe to say it goes to zero.

    Since $X$ is complete, $\lim\limits x_n = x$ for some $x$, claim this is the fixed point: $f(x) = f(\lim\limits x_n) = \lim\limits f(x_n) = \lim\limits x_{n+1} = x$.

    Such $x$ is unique: suppose $x, y$ are both fixed point, then $d(x, y) = d(f(x), f(y))$ is a contradiction.

    ## Section 44

    ### Exercise 1

    **Given $n$, show there is a continuous surjective map $g: I \rightarrow I^n$**.

    Proof

    Consider the map $f_1 = f: I \rightarrow I^2$ given in the book/lecture, then the map $f_2 = (f \times f) \circ f: I \rightarrow I^2$ $= I \times I \rightarrow I^2 \times I^2 = I^4$ would be a (composite of) surjective and continuous map.

    Similarly, compose $(f \times f \times f \times f)$ with the above function we would get a surjective and continuous map $f_3: I \rightarrow I^{2^3}$.

    Go inductively we may get $f_n: I \rightarrow I^{2^n}$, compose this function with the projection (which is clearly surjective and continuous) $\pi_n: I^{2^n} \rightarrow I^{n}$ we will get $g = \pi_n \circ f_n: I \rightarrow I^{2^n} \rightarrow I^n$ as desired.

    """
    )
    return


if __name__ == "__main__":
    app.run()
