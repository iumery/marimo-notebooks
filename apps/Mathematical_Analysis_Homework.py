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
    mo.md(r"""# Fall Semester Homework 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Problem A

    **We introduce the lexicographic order on $\mathbb{Z} \times \mathbb{Z}$. We say $(p_1, q_1) \le (p_2, q_2)$ if either $(p_1 < p_2)$ or $(p_1 = p_2$ and $q_1 \le q_2)$**.

    **Here $\le$ means less or equal and $<$ means strictly less. in the usual sense**.

    1. **Show that the lexicographic relation is indeed an order relation**;
    2. **Show that any two pairs can be compared, i.e. we can determine which is less than the other. We then say that the set $\mathbb{Z} \times \mathbb{Z}$ is totally ordered**;
    3. **Sketch how to generalize this relation for $\mathbb{Z}^k, k \ge 2$? What if the product is over infinitely many copies of $\mathbb{Z}$ (infinite words)**?

    Proof

    1. Let $\mathcal{R}$ be the relation on $(\mathbb{Z} \times \mathbb{Z}) \times (\mathbb{Z} \times \mathbb{Z})$ defined above.
    	I.e. $\mathcal{R} = \lbrace ((p_1, q_1), (p_2, q_2)) | (p_1 < p_2) \text{or}(p_1 = p_2 \text{and}q_1 \le q_2) \rbrace$.
    	Then:
    	1. $\forall (p, q) \in \mathbb{Z} \times \mathbb{Z}$, clearly $p = p$ and $q \le q$, thus $((p, q), (p, q)) \in \mathcal{R}$ and reflexivity holds;
    	2. If $((p_1, q_1), (p_2, q_2)) \in \mathcal{R}$ and $((p_2, q_2), (p_1, q_1)) \in \mathcal{R}$, then:
    		1. If $p_1 < p_2$ then $p_2 > p_1 \implies ((p_2, q_2), (p_1, q_1)) \notin \mathcal{R}$, similarly if $p_2 < p_1$ then $p_1 > p_2 \implies ((p_1, q_1), (p_2, q_2)) \notin \mathcal{R}$ Thus $p_1 = p_2$;
    		2. Under the condition that $p_1 = p_2$, if $q_1 < q_2$ then $q_2 > q_1 \implies ((p_2, q_2), (p_1, q_1)) \notin \mathcal{R}$, similarly if $q_2 < q_1$ then $q_1 > q_2 \implies ((p_1, q_1), (p_2, q_2)) \notin \mathcal{R}$. Thus $q_1 = q_2$.
		
    		Thus $(p_1, q_1) = (p_2, q_2)$ and anti-symmetry holds;
    	3. If $((p_1, q_1), (p_2, q_2)) \in \mathcal{R}$ and $((p_2, q_2), (p_3, q_3)) \in \mathcal{R}$, then either: 1. $p_1 < p_2$ and $p_2 < p_3$ thus $p_1 < p_3$ or; 2. $p_1 < p_2$ and $p_2 = p_3$ and $q_2 \le q_3$ thus $p_1 < p_3$ or; 3. $p_1 = p_2$ and $q_1 \le q_2$ and $p_2 < p_3$ thus $p_1 < p_3$ or; 4. $p_1 = p_2$ and $q_1 \le q_2$ and $p_2 = p_3$ and $q_2 \le q_3$ thus $p_1 = p_3$ and $q_1 \le q_3$.
	
    	Thus in either case $((p_1, q_1), (p_3, q_3)) \in \mathcal{R}$ and thus transitivity holds.
    	Thus $\mathcal{R}$ is an order relation;
    2. $\forall (p_1, q_1), (p_2, q_2) \in \mathbb{Z} \times \mathbb{Z}$:
    	1. If $p_1 < p_2$ then $((p_1, q_1), (p_2, q_2)) \in \mathcal{R}$, i.e. $(p_1, q_1) \le (p_2, q_2)$;
    	2. If $p_2 < p_1$ then $((p_2, q_2), (p_1, q_1)) \in \mathcal{R}$, i.e. $(p_2, q_2) \le (p_1, q_1)$;
    	3. If $p_1 = p_2$: 1. If $q_1 \le q_2$ then $((p_1, q_1), (p_2, q_2)) \in \mathcal{R}$, i.e. $(p_1, q_1) \le (p_2, q_2)$; 2. If $q_2 < q_1$ then $((p_2, q_2), (p_1, q_1)) \in \mathcal{R}$, i.e. $(p_2, q_2) \le (p_1, q_1)$;
	
    	The above argument listed all possible situation for two pairs in $\mathbb{Z} \times \mathbb{Z}$. Thus any two pairs can be compared;
    3. We may define the lexicographic order on $\mathbb{Z}^k$ by: $(p_1^1, p_1^2, \dots, p_1^k) \le (p_2^1, p_2^2, \dots, p_2^k)$ if either $(p_1^1 < p_2^1) \text{ or } (p_1^1 = p_2^1$ and $(p_1^2, \dots, p_1^k) \le (p_2^2, \dots, p_2^k)$ by the lexicographic order on $\mathbb{Z}^{k-1})$.
    	In the infinite case, let $P = (p_1, p_2, p_3, \dots) = p_1 p_2 p_3 \dots$ and $Q = q_1 q_2 q_3 \dots$ be two infinite words. Then: $P \le Q$ if either $\exists t \in \mathbb{Z}_+ + \lbrace 0 \rbrace$ such that $p_i = q_i, \forall i \le t$ and $p_{i+1} < q_{i+1}$ and $p_i = q_i, \forall i$.

    ### Problem B

    **We introduce the coordinate-wise order on $\mathbb{Z} \times \mathbb{Z}$. We say $(p_1, q_1) \le (p_2, q_2)$ if $(p_1 \le p_2)$ and $(q_1 \le q_2)$**.

    1. **Show that this relation is indeed an order relation**;
    2. **Show that NOT any two pairs can be compared. We say that the set $\mathbb{Z} \times \mathbb{Z}$ is partially ordered**.

    Proof

    1. Let $\mathcal{R}$ be the relation on $(\mathbb{Z} \times \mathbb{Z}) \times (\mathbb{Z} \times \mathbb{Z})$ defined above.
    	I.e. $\mathcal{R} = \lbrace ((p_1, q_1), (p_2, q_2)) | (p_1 \le p_2) \text{ and } (q_1 \le q_2) \rbrace$.
    	Then:
    	1. $\forall (p, q) \in \mathbb{Z} \times \mathbb{Z}$, clearly $p \le p$ and $q \le q$, thus $((p, q), (p, q)) \in \mathcal{R}$, thus reflexivity holds;
    	2. If $((p_1, q_1), (p_2, q_2)) \in \mathcal{R}$ and $((p_2, q_2), (p_1, q_1)) \in \mathcal{R}$, then:
    		1. If $p_1 < p_2$ then $p_2 > p_1 \implies ((p_2, q_2), (p_1, q_1)) \notin \mathcal{R}$, similarly if $p_2 < p_1$ then $p_1 > p_2 \implies ((p_1, q_1), (p_2, q_2)) \notin \mathcal{R}$. Thus $p_1 = p_2$;
    		2. Under the condition that $p_1 = p_2$, if $q_1 < q_2$ then $q_2 > q_1 \implies ((p_2, q_2), (p_1, q_1)) \notin \mathcal{R}$, similarly if $q_2 < q_1$ then $q_1 > q_2 \implies ((p_1, q_1), (p_2, q_2)) \notin \mathcal{R}$. Thus $q_1 = q_2$.
		
    		Thus anti-symmetry holds;
    	3. If $((p_1, q_1), (p_2, q_2)) \in \mathcal{R}$ and $((p_2, q_2), (p_3, q_3)) \in \mathcal{R}$, then $p_1 \le p_2$ and $q_1 \le q_2$ and $p_2 \le p_3$ and $q_2 \le q_3$ thus $p_1 \le p_3$ and $q_1 \le q_3$. Thus $((p_1, q_1), (p_3, q_3)) \in \mathcal{R}$ and thus transitivity holds.
	
    	Thus $\mathcal{R}$ is an order relation;
    2. Clearly $(1, 4)$ and $(3, 2)$ are two pairs in $\mathbb{Z} \times \mathbb{Z}$.
    	Since $4 > 2$, $(1, 4) > (3, 2)$;
    	Since $3 > 1$, $(3, 2) > (1, 4)$.
    	I.e. neither $((1, 4), (3, 2)) \notin \mathcal{R}$ nor $((3, 2), (1, 4)) \notin \mathcal{R}$ thus they cannot be compared.

    ### Exercise 1

    $\equiv$ **is an equivalence relation**.

    Proof

    For clarity let us denote $\mathcal{R} = \equiv$ (mod $m$) $= \lbrace (a, b) | \exists k \in \mathbb{Z} \text{such that}a - b = km \rbrace$ a relation on $A = \mathbb{Z}$.

    1. $\forall a \in A$, clearly $a - a = 0 = 0m$ thus $a \mathcal{R} a$, i.e. reflexivity holds;
    2. If $a \mathcal{R} b$, then by definition $a - b = km$ for some $k \in \mathbb{Z}$, then $b - a = -km$ and clearly $-k \in \mathbb{Z}$ thus $b \mathcal{R} a$ and symmetry holds;
    3. If $a \mathcal{R} b$ and $b \mathcal{R} c$ then $a - b = km$ for some $k$ and $b - c = k' m$ for some $k'$ thus $a - c = a + (- b + b) - c = (a - b) + (b - c) = km + k' m = (k + k')m$. Clearly $k + k' \in \mathbb{Z}$ thus $a \mathcal{R} c$ and transitivity holds.

    Thus $\mathcal{R}$ is an equivalence relation.

    ### Exercise 2

    **Prove the definition is equivalent**:

    1. $\mathbb{Z}_m = \mathbb{Z}/ \equiv = \lbrace \hat{0}, \hat{1}, \dots, \hat{m-1} \rbrace$;
    2. $\mathbb{Z}_m$ is a commutative group. $\hat{a} + \hat{b} = \hat{a + b}$.

    Proof

    If $a_1 \equiv a_2$ (mod $m$) and $b_1 \equiv b_2$ (mod $m$), then by definition $a_1 - a_2 = m k_1, \exists k_1 \in \mathbb{Z}$ and $b_1 - b_2 = m k_2, \exists k_2 \in \mathbb{Z}$. Thus $(a_1 + b_1) - (a_2 + b_2) = (a_1 - a_2) + (b_1 - b_2) = m k_1 + m k_2 = m(k_1 + k_2) = mk, \exists k \in \mathbb{Z}$, thus $a_1 + b_1 \equiv a_2 + b_2$ (mod $m$), i.e. $\hat{a_1 + b_1} = \hat{a_2 + b_2}$ thus the definition is consistent.

    ### Exercise 3

    **Let $A = \bigcup\limits_{i \in I}C_i$. Assume $C_i \ne \varnothing, \forall i$ and $C_i \cap C_{i'} = \varnothing, \forall i \ne i'$. Define $a \mathcal{R} b \iff \exists i \in I, a, b \in C_i$. Show $\mathcal{R}$ is an equivalence relation on $A$**.

    Proof

    1. Reflexivity is trivial;
    2. If $a \mathcal{R} b$, then $\exists i \in I, a, b \in C_i$ thus $b \mathcal{R} a$ and symmetry holds;
    3. If $a \mathcal{R} b$ and $b \mathcal{R} c$ then $\exists i \in I, a, b \in C_i$ and $\exists j \in I, b, c \in C_j$, thus $b \in C_i$ and $b \in C_j$. Since $C_i \cap C_{i'} = \varnothing, \forall i \ne i'$, we have $i = j$. Thus $a \in C_i$ and $c \in C_i$ thus $a \mathcal{R} c$ and transitivity holds.

    Thus $\mathcal{R}$ is an equivalence relation on $A$.

    Suppose we have an $x$, then $x \in A = \bigcup\limits_{i \in I}C_i$ if and only if $x \in C_i$ for some $i$. Since $C_i \cap C_{i'} = \varnothing, \forall i \ne i'$, we have $x \notin C_j, \forall j \ne i$. If $x' \in \hat{x} = \lbrace x' \in A | x \mathcal{R} x' \rbrace$ then $\exists j \in I, x, x' \in C_j$. Since $x \notin C_j, \forall j \ne i$, $x \in C_i$ and $x' \in C_i$, thus $\hat{x} \subseteq C_i$. If $x' \in C_i$, then by definition $x \mathcal{R}x'$ thus $x' \in \hat{x}$ thus $C_i \subseteq \hat{x}$. Thus $\hat{x} = C_i$. Thus $A/ \mathcal{R} =$ class of all (distinct) equivalence classes $= \lbrace C_i | i \in I \rbrace$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Exercise 1

    **Define the relation $\mathcal{R}$ on $\mathbb{N}$ as $(m, n) \mathcal{R} (m', n') \iff m + n' = n + m'$. Prove $\mathcal{R}$ is an equivalence relation**.

    Proof

    1. Clearly $m + n = n + m$ thus $(m, n) \mathcal{R} (m, n)$, reflexive holds;
    2. If $(m, n) \mathcal{R} (m', n')$, then $m + n' = n + m'$ thus $m' + n = n' + m$ (by changing order and side) thus $(m', n') \mathcal{R} (m, n)$, symmetric holds;
    3. If $(m, n) \mathcal{R} (m', n')$ and $(m', n') \mathcal{R} (m'', n'')$, then $m + n' = n + m'$, $m' + n'' = n' + m''$, thus $m + n' + m' + n'' = n + m' + n' + m''$, thus $n' + m' + m + n'' = n' + m' + n + m''$. By adding inverse of $n'$ and $m'$ with respect to addition in $\mathbb{R}$ to the left of both side, we have $m + n'' = n + m''$ thus $(m, n) \mathcal{R} (m'', n'')$, transitivity holds.

    Thus this is an equivalence relation.

    ### Exercise 2

    **Define $\hat{(m, n)}$ the equivalence class of '-'. Define the sum of two classes by $\hat{(m, n)} + \hat{(m', n')} = \hat{(m + m', n + n')}$**.

    1. **Show that $\hat{(m, n)} = \hat{(m+k, n+k)}$**.
    2. **Show that $\hat{(k, k)}$ is the neutral element with respect to addition**.
    3. **Show that $\hat{(m, n)} + \hat{(n, m)} = \hat{(k, k)}$**.

    Proof

    1. Clearly we have $m + (n+k) = n + (m+k)$, thus by above definition $(m, n) \mathcal{R} (m+k, n+k)$, thus their equivalence classes coincidence;
    2. For any pair $(m, k)$, by the above summation definition, $\hat{(m, n)} + \hat{(k, k)} = \hat{(m+k, n+k)} =^{\text{by (i).}} \hat{(m, n)}$ and $\hat{(k, k)} + \hat{(m, n)} = \hat{(k+m, k+n)} = \hat{(m+k, n+k)} =^{\text{by (i).}} \hat{(m, n)}$.
    	I.e. $\hat{(k, k)}$ is the (two-sided) identity element;
    3. By the above summation definition, $\hat{(m, n)} + \hat{(n, m)} = \hat{(m+n, n+m)}$.
    	Clearly we have $(m+n) + k = (n+m) + k$ thus $(m+n, n+m) \mathcal{R} (k, k)$ thus their equivalence classes coincidence.
    	Thus $\hat{(m, n)} + \hat{(n, m)} = \hat{(m+n, n+m)} = \hat{(k, k)}$.

    ## Section 1.1

    ### Exercise 4

    **What is the intersection of all the open intervals containing the closed interval $[0, 1]$? Justify your answer**.

    Solution

    Claim that the answer is $[0, 1]$.

    Proof

    By construction the intersection is $S = \bigcap\limits_{A \in \mathcal{A}} A, [0, 1] \subseteq A$, $A$ open. If $a \in [0, 1]$, then $a \in [0, 1] \subseteq A$, for all $A$, thus $a \in \bigcap\limits_{A \in \mathcal{A}} A = S$. If $a < 0$, then the open interval $(a, 2)$ contains $[0, 1]$ but not $a$, which is a contradiction. Similarly if $a > 1$ there is a contradiction. Thus $S = [0, 1]$.

    ### Exercise 5

    **What is the intersection of all the close intervals containing the open interval $(0, 1)$? Justify your answer**.

    Solution

    Claim that the answer is $[0, 1]$.

    Proof

    By construction the intersection is $S = \bigcap\limits_{A \in \mathcal{A}} A, (0, 1) \subseteq A$, $A$ closed. If $a \in (0, 1)$, then $a \in (0, 1) \subseteq A$ for all $A$ thus $a \in S$. If $a = 0$, suppose there exists $A$ such that $(0, 1) \subseteq A$, $A$ closed, and $0 \notin A$. Since $A$ closed, it is of the form $[a_l, a_u]$ with $0 < a_l$. Take $a' = \frac{a_l}{2}$, then $0 < a' < a_l$. Thus $a' \in (0, 1)$ but $a' \notin A$, which is a contradiction, thus such $A$ does not exist, thus $a = 0 \in S$. Similar with $a = 1$. If $a < 0$ or $a > 1$, take $A' = [0, 1]$, then $A' \in \mathcal{A}$ but $a \notin A'$ thus $a \notin S$. Thus $S = [0, 1]$.

    ### Exercise 6

    **What is the union of all of the closed intervals contained in the open interval $(0, 1)$? Justify your answer**.

    Solution

    Claim that the answer is $(0, 1)$.

    Proof

    By construction the union is $U = \bigcup\limits_{A \in \mathcal{A}}A, A \subseteq (0, 1), A$ closed. If $a \le 0$, $a \notin (0, 1)$, thus $a$ is not in any subset of $(0, 1)$, i.e. $a \notin A, \forall A$, thus $a \le 0$ is not in the union. Similar with $a \ge 1$. Otherwise $0 < a < 1$, take $a' = \frac{a}{2}$ and $b' = \frac{a + 1}{2}$ (mid-point of $a$ and $1$), then the closed interval $A' = [a', b'] \ni a$ is contained in $(0, 1)$ thus $A' \in \mathcal{A}$, i.e. such $a$ is in the union. Thus the union is $(0, 1)$.

    ### Exercise 8

    **Which of the following functions $f: \mathbb{R} \rightarrow \mathbb{R}$ are one to one and which ones are onto. Justify your answer**.

    1. $f(x) = x^2$;
    2. $f(x) = x^3$;
    3. $f(x) = e^x$.

    Solution

    1. $1 = f(1) = f(-1)$ thus $f$ not one-to-one. $x^2 = -1$ has no solution in $\mathbb{R}$ thus $f$ not onto;
    2. Let $g: \mathbb{R} \rightarrow \mathbb{R}$ given by $g(x) = x^{1/3}$. Cube root is a function. $\forall x \in \mathbb{R}, f(g(x)) = f(x^{1/3}) = (x^{1/3})^3 = x^1 = x$, and $g(f(x)) = g(x^3) = (x^3)^{1/3} = x$. Thus $f$ is a bijection thus both one-to-one and onto;
    3. Observe that $f$ is a strict increasing function, thus no $x < y$ would have image $f(x) = f(y)$, thus $f$ is one-to-one. $f$ not onto because $e^x$ is never negative for $x \in \mathbb{R}$.

    ### Exercise 11

    **Prove that, if $f: A \rightarrow B$ is a function and $E$ and $F$ are subsets of $A$, then $f(E \cup F) = f(E) \cup f(F)$**.

    Proof

    $f(E \cup F) = \lbrace b | b = f(a)$ for at least one $a \in E \cup F \rbrace = \lbrace b | b = f(a)$ for at least one $a \in E$ or $a \in F \rbrace = \lbrace b | b = f(a)$ for at least one $a \in E \rbrace \cup \lbrace b | b = f(a)$ for at least one $a \in F \rbrace = f(E) \cup f(F)$.

    ### Exercise 12

    **Prove that, if $f: A \rightarrow B$ is a function and $E$ and $F$ are subsets of $A$, then $f(E \cap F) \subseteq f(E) \cap f(F)$**.

    Proof

    $f(E \cap F) = \lbrace b | b = f(a)$ for at least one $a \in E \cap F \rbrace = \lbrace b | b = f(a)$ for at least one $a \in E$ and $a \in F \rbrace = \lbrace b | b = f(a_0)$ for at least one $a_0 \in E \rbrace \cap \lbrace b | b = f(a_0)$ for at least the same $a_0 \in F \rbrace \subseteq \lbrace b | b = f(a_0)$ for at least one $a_0 \in E \rbrace \cap \lbrace b | b = f(a_1)$ for at least one $a_1 \in F \rbrace = f(E) \cap f(F)$.

    ### Exercise 13

    **Give an example of a function $f: A \rightarrow B$ and subsets $F \subseteq E$ of $A$ for which $f(E) \backslash f(F) \ne f(E \backslash F)$**.

    Solution

    Let $A = B = \lbrace 1, 2, 3 \rbrace$, $f$ given by $f(1) = 1, f(2) = 1, f(3) = 2$, $F = \lbrace 2, 3 \rbrace$, and finally $E = \lbrace 1, 2, 3 \rbrace$. Then $f(E) = \lbrace 1, 2 \rbrace$, $f(F) = \lbrace 1, 2 \rbrace$, and we have $f(E) \backslash f(F) = \varnothing$ but $f(E \backslash F) = f(\lbrace 1 \rbrace) = \lbrace 1 \rbrace$, which are not equal.

    ### Exercise 14

    **Prove that equality holds in Parts (b) and (c) of Theorem 1.1.7 if the function $f$ is one-to-one**.

    Proof

    (b): Following exercise 12, if $f$ is injective, then $b = f(a_0) = f(a_1) \implies a_0 = a_1$, we can thus substitute all $a_0, a_1$ by $a$ and equality holds.

    (c): $f(E) - f(F) = \lbrace b | b = f(a_0)$ for at least one $a_0 \in E \rbrace - \lbrace b | b = f(a_1)$ for at least one $a_1 \in F \rbrace = \lbrace b | b = f(a_0)$ for at least one $a_0 \in E$ and $b \ne f(a_1)$ for all $a_1 \in F \rbrace = \lbrace b | b = f(a)$ for at least one $a \in E - F \rbrace - \lbrace b | b = f(a)$ for at least one $a \in E - F$ and for at least one $a \in F \rbrace \subseteq \lbrace b | b = f(a)$ for at least one $a \in E - F \rbrace = f(E - F)$. If $f$ is injective, then $f(a') = f(a) \implies a' = a$, thus $a \in E - F \implies a \notin F$ thus $\lbrace b | b = f(a)$ for at least one $a \in E - F$ and for at least one $a \in F \rbrace = \varnothing$, thus equality holds.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 1.2

    ### Exercise 11

    **Using induction, prove that $\sum\limits_{k = 1}^n (2k-1) = n^2$ for every $n \in \mathbb{N}$**.

    Proof

    If $n = 1$, $2 \cdot 1 - 1 = 1^2$, true.

    Now suppose $\sum\limits_{k = 1}^m (2k-1) = m^2$, then $\sum\limits_{k = 1}^{m + 1} (2k-1)$ $= \sum\limits_{k = 1}^{m} (2k-1) + 2(m + 1) - 1$ $= m^2 + 2(m+1) - 1$ $= m^2 + 2m + 1 = (m+1)^2$, i.e. statement true for $m+1$ given $m$ true. By induction the statement true for all natural $n$.

    ### Exercise 14

    **Let a sequence $\lbrace x_n \rbrace$ of numbers be defined recursively by $x_1 = 0$ and $x_{n+1} = \frac{x_n+1}{2}$. Prove by induction that $x_n \le x_{n+1}$ for all $n \in \mathbb{N}$. Would this conclusion change if we set $x_1 = 2$**?

    Proof

    $0 = x_1 \le x_2 = 1/2$ true. Now suppose $x_m \le x_{m+1}$, then $x_{m+2} = \frac{x_{m+1}+1}{2} \ge \frac{x_{m}+1}{2} = x_{m+1}$, i.e. statement true for $m+1$ given $m$ true. By induction the statement true for all natural $n$. Now $2 = x_1 \le x_2 = 1.5$ not true. Thus the conclusion does not hold. Notice that however the conclusion holds with $\ge$ with the similar logic.

    ### Exercise 16

    **Use induction in the form stated in the preceding exercise to prove that $n^2 < 2^n$ for all $n \ge 5$**.

    Proof

    $25 = 5^2 < 2^5 = 32$ true.

    Now suppose $m^2 < 2^m$, then $(m+1)^2 = m^2 + 2m + 1 < 2^m + 2m + 1$ (here by induction $2n + 1 < 2^n$ for all $n \ge 5$ as: $2 \cdot 5 + 1 = 11 < 32$ true, if $2m + 1 < 2^m$ true then $2(m+1) + 1 = 2m+1 + 2 < 2^m + 2^1 < 2^m + 2^m = 2^{m+1}$ thus statement holds for all $n \ge 5$) $< 2^m + 2^m = 2^{m + 1}$, i.e. statement true for $m+1$ given $m$ true. By induction the statement true for all $n \ge 5$.

    ### Exercise 17

    **Prove the identity $\begin{pmatrix} n \\ k-1 \end{pmatrix} + \begin{pmatrix} n \\ k \end{pmatrix} = \begin{pmatrix} n + 1 \\ k \end{pmatrix}$**.

    Proof

    $\begin{pmatrix} n + 1 \\ k \end{pmatrix} \overset{\text{def}}{=} \frac{(n + 1)!}{k!(n + 1 - k)!} = \frac{(n)!(n + 1)}{k!(n + 1 - k)!}$ $= \frac{(n)!(n + 1 + k - k)}{k!(n + 1 - k)!} = \frac{(n)!(n + 1 - k) + (n!)k}{k!(n + 1 - k)!}$ $= \frac{(n)!(n + 1 - k)}{k!(n + 1 - k)!} + \frac{(n)!k}{k!(n + 1 - k)!}$ $= \frac{(n)!(n + 1 - k)}{k!(n - k)!(n + 1 - k)} + \frac{(n)!k}{(k - 1)!(n - k + 1)!k}$ $= \frac{(n)!}{k!(n - k)!} + \frac{(n)!}{(k - 1)!(n - k + 1)!}$ $\overset{\text{def}}{=} \begin{pmatrix} n \\ k \end{pmatrix} + \begin{pmatrix} n \\ k-1 \end{pmatrix}$.

    ### Exercise 19

    **Prove the well ordering principle for the natural numbers: each non-empty subset $S$ of $\mathbb{N}$ contains a smallest element**.

    Proof

    Let $S$ be a non-empty subset of the natural. Assume there is no least element in $S$. Since $1$ is the least natural number, $1 \notin S$, thus $1 \in \mathbb{N} - S$. Suppose now $1, 2, \dots, m \notin S$, then $m + 1$ is smaller than anything else in the naturals, thus $m + 1$ not in $S$, $m + 1 \in \mathbb{N} - S$. By strong induction, $n \in \mathbb{N} - S, \forall n \in \mathbb{N}$, in other words, $\mathbb{N} = \mathbb{N} - S$, thus $S = \varnothing$, which is a contradiction. Thus there is a least element in $S$.

    ## Section 1.3

    ### Exercise 8

    **Assuming $x, y, z$ are elements of a field. $x y=0$ implies $x = 0$ or $y = 0$**.

    Proof

    $x y = 0$, if $x = 0$ or $y = 0$ or both then we are done. If $x \ne 0$, then by definition $\exists x^{-1}$ such that $x^{-1}x y = x^{-1}0 \implies 1 y = 0 \implies y = 0$. Similarly if $y \ne 0$ then $x = 0$. Thus $x = 0$ or $y = 0$.

    ### Exercise 11

    **Assuming $x, y, z$ are elements of an ordered field. $0 < x < y$ implies $y^{-1} < x^{-1}$**.

    Proof

    First we need show that $x > 0 \implies x^{-1} > 0$:

    Suppose not, then $-x^{-1} > 0$, then $x (-x^{-1}) > 0$, well the left side $= -1 (x^{-1} x) = -1 \cdot 1 = -1$ thus $-1 > 0$ which is a contradiction thus $x^{-1} > 0$.

    Thus $0 < x < y \implies 0 x^{-1} < x x^{-1} < y x^{-1} \implies y^{-1} 0 x^{-1} < y^{-1} x x^{-1} < y^{-1} y x^{-1} \implies 0 < y^{-1} < x^{-1}$.

    ### Exercise 12

    **Prove that the equation $x^2= 5$ has no rational solution**.

    Proof

    By Theorem 1.3.9 the solution is an integer. Clearly $0^2 = 0 \ne 5, 1^2 = -1^2 = 1 \ne 5, 2^2 = -2^2 = 4 \ne 5, 3^2 = -3^2 = 9 > 5$, and for $n$ with $| n | > 3$, $n^2 > 3^2 > 5$. At this point we have checked all possible solutions and they all fail, thus there is no solution in the rational field.

    ### Exercise 13

    **Generalize Theorem 1.3.9 by proving that every rational solution of a polynomial equation $x^n+ a_{n-1}x^{n-1} + \dots + a_1x + a_0= 0$, with integer coefficients $a_k$, is an integer solution**.

    Proof

    Let $r = \frac{x}{y}$ is a rational solution with $x, y$ no common divisor. Also take $a_0' = - a_0$. We can rewrite the equation as $\frac{x}{y}^n+ a_{n-1} \frac{x}{y}^{n-1} + \dots + a_1 \frac{x}{y} = a_0'$, thus we have, multiply $y^n$ both sides, $x^n + a_{n-1}x^{n-1}y + \dots + a_1 x y^{n-1} = a_0' y^n$ which implies $y$ divides $x^n + a_{n-1}x^{n-1}y + \dots + a_1 x y^{n-1} = x^n + y(a_{n-1}x^{n-1} + \dots + a_1 x y^{n-2}) \equiv x^n$ mod $y$ thus $y$ divides $x^n$. Then similar with the proof of theorem 1.3.9, this could only happen, under the assumption that $x, y$ has no common divisor, if $y = 1$, i.e. $r = x$ is an integer.

    ### Exercise 15

    **Use the result of the preceding exercise to prove that if a prime $p$ divides the product $n m$ of two positive integers, then it divides $n$ or it divides $m$**.

    Proof

    Suppose a prime $p$ divides the product $n m$ of two positive integers.

    If $p$ does not divide $n$, since $p$ prime, $p, n$ are relatively prime. By previous exercise, $\exists a, b$ such that $a p + b n = 1$, thus $a p m + b n m = m$, by construction we have that there exists a $k$ such that $k p = n m$, thus $a p m + b k p = m \implies p(a m + b k) = m$, which implies that $p$ divides $m$.

    With the same argument, if $p$ does not divide $m$, it divides $n$. Thus we conclude $p$ divides $n$ or it divides $m$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 1.4

    ### Exercise 1

    **For each of the following sets, describe the set of all upper bounds for the set**:

    1. **the set of odd integers**;
    2. $\lbrace 1 - 1/n: n \in \mathbb{N} \rbrace$;
    3. $\lbrace r \in \mathbb{Q} : r^3 < 8 \rbrace$;
    4. $\lbrace \sin(x): x \in \mathbb{R} \rbrace$.

    Solution

    1. This set is not bounded as for any $n = 2k+1, k \in \mathbb{N}$ be an integer, $n+2$ is an odd integer greater than $n$;
    2. Since $n \in \mathbb{N}$, $n > 0$, and by previous homework we have $n^{-1} = \frac{1}{n} > 0$, thus $1 - \frac{1}{n} < 1$ for all $n$, thus clearly $M$ is an upper bound for the set for any $M \in \lbrace M \in \mathbb{R} | M \ge 1 \rbrace$.
    	If $M' < 1$, we can write $M' = 1 - \varepsilon$ for some $\varepsilon > 0$, which implies there exists some $n \in \mathbb{N}$ such that $1/ \varepsilon < n, 1/n < \varepsilon$, thus $M' = 1 - \varepsilon < 1 - \frac{1}{n}$ for such $n$, in other word, $M'$ is not a upper bound of the original set.
    	Thus the set of all upper bound for this set is indeed $\lbrace M \in \mathbb{R} | M \ge 1 \rbrace$;
    3. Clearly the set of all upper bounds contains $\lbrace r \in \mathbb{R} : r^3 \ge 8 \rbrace = \lbrace r \in \mathbb{R} : r \ge 2 \rbrace$.
    	If we have $M_0$ such that $M_0 < 2$, by following exercise we have there exists a rational $M_0 < M' < 2$, take $M'' = \frac{M' + 2}{2}$ then $M''^3 = \frac{M'^3+ 6 M'^2+ 12 M'+ 8}{8} < \frac{8 + 6 \cdot 4 + 12 \cdot 2 + 8}{8} = 8$, since $(\mathbb{Q}, + , \cdot)$ is a field $M''$ is a rational. $M'' > M_0$ thus we have such $M_0$ is not an upper bound of the original set. In other word, the set of all upper bounds is $\lbrace r \in \mathbb{R} : r \ge 2 \rbrace$;
    4. From previous study we know sine has range $[-1, 1]$ in with real variables, thus its set of all upper bounds is $\lbrace x \in \mathbb{R} | x \ge 1 \rbrace$.

    ### Exercise 7

    **Prove that if $x < y$ are two real numbers, then there is a rational number $r$ with $x < r < y$**.

    Proof

    $x < y \implies y - x > 0$, take $\varepsilon = \frac{y - x}{2}$, then $y - x > \varepsilon > 0$, thus there exists $n \in \mathbb{N}$ such that $n > 1/ \varepsilon, \varepsilon > 1/n > 0$, thus $y - x > 1/n > 0 \implies n(y - x) = ny - nx > 1$, thus there exists $m \in \mathbb{Z}$ such that $ny > m > nx \implies y> \frac{m}{n} > x$, by definition $\frac{m}{n}$ is a rational, take this $\frac{m}{n} = r$ and we are done.

    ### Exercise 8

    **Prove that if $x$ is irrational and $r$ is a non-zero rational number, then $x+r$ and $rx$ are also irrational**.

    Proof

    For any $q, r \in \mathbb{Q}$ we can write $q = \frac{m}{n}, r = \frac{m'}{n'}$, thus $q - r = \frac{mn'-m' n}{n' n}$ is a rational, thus we have the statement that 'if $x + r$ and $r$ are rational, then $x$ is rational', take the negation we have if $x$ is irrational and $r$ is rational then $x + r$ is irrational.

    Similarly under the additional requirement that $m' \ne 0$, $r^{-1}$ exists and $qr^{-1} = \frac{mn'}{nm'}$ is rational, we have the statement that 'if $xr$ and $r \ne 0$ are rational, then $x$ is rational', take the negation we have if $x$ is irrational and $r \ne 0$ is rational then $xr$ is irrational.

    ### Exercise 9

    **We know that $\sqrt{2}$ is irrational. Use this fact and the previous exercise to prove that if $r < s$ are rational numbers, then there is an irrational number x with $r < x < s$**.

    Proof

    Clearly $0 < \frac{\sqrt{2}}{2} < 1$. Since $r < s \implies s - r > 0$ we have $0 < \frac{\sqrt{2}}{2}(s - r) < (s - r)$, add $r$ we have $r < r + \frac{\sqrt{2}}{2}(s - r) < s$.

    By previous exercise we have $r + \frac{\sqrt{2}}{2}(s - r)$ is a result of multiplication and addition of rational numbers and a irrational number thus is irrational, take this as our $x$ and we are done.

    ## Section 1.5

    ### Exercise 2

    **Find the sup and inf of the following sets. Tell whether each set has a maximum or a minimum**.

    1. $(1, 8]$;
    2. $\lbrace \frac{n+2}{n^2+1} \rbrace$;
    3. $\lbrace \frac{n}{m} | n, m \in \mathbb{Z}, n^2 < 5m^2 \rbrace$.

    Solution

    1. Clearly $\inf{S} = 1 \notin S$ and $\sup\limits{S} = 8 \in S$. $S$ has a maximum but not a minimum;
    2. $S = \lbrace \frac{3}{2}, \frac{4}{5}, \frac{5}{9}, \dots \rbrace$ by a simple induction step we see $S$ got the largest element at $n = 1$, in other words, $\sup\limits{S} = \frac{3}{2} \in S$.
    	Clearly $\frac{n+2}{n^2+1} > 0$ and claim that $\inf{S} = 0 \notin S$. Indeed, if $m > 0$ is a lower bound, then $\exists n \in \mathbb{N}$ such that $n > \frac{2}{m}+1, m> \frac{2}{n-1} = \frac{2n+2}{n^2+ 1}> \frac{n+2}{n^2+1}$ which is a contradiction. $S$ has a maximum but not a minimum;
    3. Claim that $\inf{S} = - \sqrt{5} \notin S, \sup\limits{S} = \sqrt{5} \notin S$. Suppose $M < \sqrt{5}$ is an upper bound, by previous exercise there exist rational $M < M' = \frac{n}{m} < \sqrt{5}$, this $n, m$ do satisfy the condition that $n^2 < 5 m^2$, thus $M$ is not an upper bound. Similar with the lower bound.
    	$S$ has neither a maximum nor a minimum. For any rational $0 < \frac{n}{m} < \sqrt{5}$, there exists rational $\frac{n}{m} < \frac{n'}{m'} < \sqrt{5}$, and it is easy to see $\frac{n'}{m'}$ is also in the set. Similar with the minimum.

    ### Exercise 6

    **Let $A$ and $B$ be non-empty subsets of $R$. Then $\sup\limits{A - B} = \sup\limits{A} - \inf{B}$**.

    Proof

    $\sup\limits{A - B} = \sup\limits{A + (- B)} = \sup\limits{A} + \sup\limits{-B} = \sup\limits{A} - \inf{B}$ by the previous part of the theorem.

    ### Exercise 10 - 13

    **Let $f$ and $g$ be functions defined on a set containing $A$ as a subset, and let $c \in \mathbb{R}$ be a positive constant. Then**:

    1. $\sup\limits_A{cf} = c \sup\limits_A{f}$ and $\inf\limits_A{cf} = c \inf\limits_A{f}$;
    2. $\sup\limits_A{-f} = - \inf\limits_A{f}$;
    3. $\sup\limits_A{\lbrace f + g \rbrace} \le \sup\limits_A{f} + \sup\limits_A{g}$ and $\inf\limits_A{f} + \inf\limits_A{g} \le \inf\limits_A{\lbrace f + g \rbrace}$;
    4. $\sup\limits{ \lbrace f(x) - f(y) | x, y \in A \rbrace} = \sup\limits_A{f} - \inf\limits_A{f}$.

    Proof

    1. $\sup\limits_A{cf} = \sup\limits{ \lbrace cf(x) | x \in A \rbrace} = c \sup\limits{ \lbrace f(x) | x \in A \rbrace} = c \sup\limits_A{f}$. Similar with $\inf$;
    2. $\sup\limits_A{-f} = \sup\limits{ \lbrace -f(x) | x \in A \rbrace} = - \inf{ \lbrace f(x) | x \in A \rbrace} = - \inf\limits_A{f}$;
    3. We have:
    	1. $\sup\limits_A{\lbrace f + g \rbrace} = \sup\limits{ \lbrace f(x) + g(y) | x, y \in A \rbrace}$ $\le^{\text{by Theorem 1.5.7 (e)}} \sup\limits{ \lbrace f(x) + g(x) | x \in A \rbrace} = \sup\limits_A{f} + \sup\limits_A{g}$;
    	2. $\inf\limits_A{\lbrace f + g \rbrace} = \inf{ \lbrace f(x) + g(y) | x, y \in A \rbrace}$ $\ge \inf{ \lbrace f(x) + g(x) | x \in A \rbrace} = \inf\limits_A{f} + \inf\limits_A{g}$;
    4. $\sup\limits{ \lbrace f(x) - f(y) | x, y \in A \rbrace} = \sup\limits{ \lbrace f(x) | x \in A \rbrace} + \sup\limits{ \lbrace - f(x) | x \in A \rbrace}$ $= \sup\limits{ \lbrace f(x) | x \in A \rbrace} - \inf{ \lbrace f(x) | x \in A \rbrace} = \sup\limits_A{f} - \inf\limits_A{f}$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 5""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 2.3

    ### Exercise 4

    **Prove that $\lim\limits \frac{\sin n}{n} = 0$**.

    Proof

    We know sine is bounded by $-1$ and $1$ on the real line, thus $-1/n \le \frac{\sin n}{n} \le 1/n$. Clearly $\lim\limits \frac{1}{n} = 0$ and $\lim\limits - \frac{1}{n} = 0$, by Squeeze Theorem $\lim\limits \frac{\sin n}{n} = 0$.

    ### Exercise 5

    **Let $\lbrace a_n \rbrace$ be a sequence of real numbers such that $\lim\limits a_n = 0$, and let $\lbrace b_n \rbrace$ be a bounded sequence. Then $\lim\limits a_n b_n = 0$**.

    Proof

    Say $b_n$ is bounded above by $U$ and bounded below by $L$, take $B = \max(| L | , | U |)$ then we have $| b_n | \le B$. Then by definition of sequence limit, for any $\varepsilon > 0$, exists $N$ such that $| a_n | \le \varepsilon/B$ for all $n > N$, thus $| a_n b_n | = | a_n \| b_n | \le | a_n | B \le \varepsilon$. By definition $a_n b_n$ has limit $0$.

    ### Exercise 8

    **Prove that if $\lbrace b_n \rbrace$ is a sequence of positive terms and $b_n \rightarrow b > 0$, then there is a number $m > 0$ such that $b_n \ge m$ for all $n$**.

    Proof

    We will prove by giving such an $m$. Take $m' = b/2 > 0$ and $\varepsilon = b/3 > 0$. By definition of sequence limit, there exists $N$ such that $| b_n - b | < b/3$ for all $n > N$, since $b_n$ positive, in other word $2b/3 < b_n < 4b/3$ for all $n > N$, thus $m' = b/2 < 2b/3 < b_n$ for all $n > N$. Now consider $\lbrace b_1, b_2, \dots, b_{N-1} \rbrace$. This set is finite thus we can find the smallest element, say it is $b_l$, clearly $b_l > 0$. Take $m = \min(m', b_l)$ then and we have got the $m$ we desired.

    ### Exercise 11

    **For each natural number $n$, let $b_n = n^{1/n} - 1$. Then $b_n$ is positive and $n = (1 + b_n)^n$. Use the Binomial Theorem to prove that $n \ge \frac{n(n - 1)}{2}b_n^2$ and, hence, that $b_n \le \sqrt{\frac{2}{n - 1}}$**.

    Proof

    By the Binomial Theorem $n = (1 + b_n)^n$ $= \begin{pmatrix} n \\ 0 \end{pmatrix} b_n^0 + \begin{pmatrix} n \\ 1 \end{pmatrix} b_n^1 + \begin{pmatrix} n \\ 2 \end{pmatrix} b_n^2 + \dots + \begin{pmatrix} n \\ n \end{pmatrix} b_n^n$ $= \begin{pmatrix} n \\ 0 \end{pmatrix} b_n^0 + \begin{pmatrix} n \\ 1 \end{pmatrix} b_n^1 + \frac{n (n - 1)}{2} b_n^2 + \dots + \begin{pmatrix} n \\ n \end{pmatrix} b_n^n \ge \frac{n (n - 1)}{2} b_n^2$ because clearly the other terms are all non-negative.

    Then $\frac{n (n - 1)}{2} b_n^2 \le n \implies \frac{n - 1}{2} b_n^2 \le 1 \implies b_n^2 \le \frac{2}{n - 1} \implies b_n \le \sqrt{\frac{2}{n - 1}}$.

    ### Exercise 12

    **Prove that $\lim\limits n^{1/n} = 1$**.

    Proof

    Take $b_n$ as the above exercise stated. Then for any $\varepsilon > 0$, $| b_N | = b_N \le \sqrt{\frac{2}{N-1}}$, take $N$ such that $\sqrt{\frac{2}{N-1}} < \varepsilon$, i.e. $\frac{2}{\varepsilon^2}+1 < N$ then for all $n > N$, $| b_n | < \varepsilon$, i.e. $\lim\limits b_n = 0$. Thus $\lim\limits(b_n + 1) = 0 + 1 = 1 \implies \lim\limits n^{1/n} = 1$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 6""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 2.4

    ### Exercise 1

    **Tell which of the following sequences are non-increasing, non-decreasing, bounded? Justify your answers**.

    1. $\lbrace n^2 \rbrace$;
    2. $\lbrace \frac{1}{\sqrt{n}} \rbrace$;
    3. $\lbrace \frac{-1^n}{n} \rbrace$;
    4. $\lbrace \frac{n}{2^n} \rbrace$;
    5. $\lbrace \frac{n}{n+1} \rbrace$.

    Solution

    1. For each $n$, $(n+1)^2 > (n)(n+1) > n^2$ thus it is (strictly) increasing. It is unbounded as for any $N$, pick $n = N$ then $n^2 > N$;
    2. For each $n$, $\sqrt{n + 1} > \sqrt{n}$ thus $\sqrt{n}$ strictly increasing and thus $\frac{1}{\sqrt{n}}$ (strictly) decreasing. For any $N$, pick $n = N^2 + 1$ then $\sqrt{n} > N$, thus $\lim\limits \sqrt{n} \rightarrow \infty$, thus $\lim\limits \frac{1}{\sqrt{n}} \rightarrow 0$; since it converges, it is bounded;
    3. This sequence is neither non-decreasing nor non-increasing, as it is easy to see that for any even $n$, $\frac{-1^{n-1}}{n-1}$ is negative, $\frac{-1^n}{n}$ itself is positive (increasing), yet $\frac{-1^{n+1}}{n+1}$ is again negative (decreasing). By Squeeze Theorem this sequence converges to $0$, thus it is bounded;
    4. $\frac{n+1}{2^{n+1}} = \frac{n+1}{2^{n}} * \frac{1}{2} = \frac{n/2 + 1/2}{2^{n}} \le \frac{n}{2^{n}}$ thus this sequence is non-increasing. Note that other than $n = 1$, the sequence is indeed strictly decreasing. It is bounded: it is non-increasing thus bounded above by the first term $1/2$; it is bounded below because all terms are positive;
    5. $\frac{n+1}{n+2} = \frac{(n+1)(n+1)/(n+2)}{n+1}$, by Euclidean division, $= \frac{n + \frac{1}{n+2}}{n+1} > \frac{n}{n+1}$ thus it is (strictly) increasing. It is bounded: it is non-decreasing thus bounded below by the first term $1/2$; it is bounded above because $1 > \frac{n}{n + 1}$ for any $n$.

    ### Exercise 4

    **Let $\lbrace d_n \rbrace$ be a sequence of $0$ and $1$ and define a sequence of numbers $\lbrace a_n \rbrace$ by $a_n = d_12^{-1} + \dots + d_n2^{-n}$. Prove that this sequence converges to a number between $0$ and $1$**.

    Proof

    $a_n$ is monotone: for any $n$, $a_{n+1} = a_{n} + d_{n + 1}2^{-n-1} \ge a_{n}$; $a_n$ is bounded: for any $n$, $0 = 0 \cdot 2^{-1} + \dots + 0 \cdot 2^{-n}$ $\le d_12^{-1} + \dots + d_n2^{-n}$ $\le 1 \cdot 2^{-1} + \dots + 1 \cdot 2^{-n}$ $< 1$. Therefor $a_n$ converges.

    By the above argument we see $0 \le a_n < 1$ for all $n$, take $b_n \equiv 0$ and $b_n \equiv 1$, by Theorem 2.3.8., $a_n$ converges to a number between $0$ and $1$.

    ### Exercise 8

    **Prove that $\lim\limits \frac{n^5 + 3n^3 + 2}{n^4 - n + 1} = \infty$**.

    Proof

    For any $n$, $\frac{n^5 + 3n^3 + 2}{n^4 - n + 1} = \frac{n(n^4 - n + 1) + 3n^3 +n^2-n+2}{n^4 - n + 1} = \frac{3n^3 +n^2-n+2}{n^4 - n + 1} + n$. It is clear that for any $n \ge 1, 3n^3 +n^2-n+2 > 0$ and $n^4 - n + 1 > 0$, thus $\frac{n^5 + 3n^3 + 2}{n^4 - n + 1} > n$. Since $n$ is unbounded, $\frac{n^5 + 3n^3 + 2}{n^4 - n + 1}$ is unbounded as well.

    ### Exercise 14

    **Suppose $\lbrace a_n \rbrace$ and $\lbrace b_n \rbrace$ are non-decreasing sequences that are interlaced in the sense that each term of the sequence $\lbrace a_n \rbrace$ is less than or equal to some term of the sequence $\lbrace b_n \rbrace$ and vice-versa. Prove that $\lim\limits a_n = \lim\limits b_n$**.

    Proof

    First, since $a_n, b_n$ are monotone, the limits do exist.

    Now, suppose $\lim\limits a_n < \lim\limits b_n$. Choose $\varepsilon$ such that $\lim\limits a_n + \varepsilon < \lim\limits b_n - \varepsilon$ (we can do that, even if $\lim\limits b_n$ is infinity). Then by definition of limit, there exists $N_a$ such that $| a_n - \lim\limits a_n | < \varepsilon$ for all $n > N_a$ and $N_b$ such that $| b_n - \lim\limits b_n | < \varepsilon$ for all $n > N_b$. Take $N = \max{(N_a, N_b)}$, consider the term $b_{N+1}$:

    $b_{N+1} > \lim\limits b_n - \varepsilon > \lim\limits a_n + \varepsilon$ thus it is greater than $a_n$ for any $n > N$; since $a_n$ is non-decreasing, $a_N \ge a_n$ for any $n \le N$, thus $b_{N+1} > a_n$ for all $n$, which contradict the assumption that there exists some $a_m$ such that $b_n$ is less than or equal to it. Thus $\lim\limits a_n \ge \lim\limits b_n$.

    Similarly we have $\lim\limits a_n \le \lim\limits b_n$ thus they are equal.

    ## Section 2.5

    ### Exercise 1

    **Give an example of a nested sequence of bounded open intervals that does not have a point in its intersection**.

    Solution

    $(0, 1) \supseteq (0, 1/2) \supseteq (0, 1/3) \supseteq \dots$

    Any negative number or $0$ is clearly not in the intersection. For any positive number $a$, by convergence of $\frac{1}{n}$, there exists $n$ such that $1/n < a$, thus $a$ is not contained in $(0, 1/n)$ thus it is not in the intersection.

    ### Exercise 6

    **For each of the following sequences $\lbrace a_n \rbrace$, find a subsequence which converges. Justify your answer**.

    1. $a_n = (-1)^n$;
    2. $a_n = \sin(n \pi/4)$;
    3. $a_n = \frac{n}{2^k} - 1$ with $k$ an integer chosen so that $2^k \le n < 2^{k+1}$.

    Solution

    1. Let $n_k = 1, 3, 5, \dots$ then $a_{n_k} = -1, -1, -1, \dots$ is constant thus converges;
    2. Let $n_k = 4, 8, 12, \dots$ then $a_{n_k} = 0, 0, 0, \dots$ is constant thus converges;
    3. Let $n_k = 1, 2, 4, 8, 16, \dots$ then by construction $a_{n_k} = 1/1 - 1, 2/2 - 1, 4/4 - 1, 8/8 - 1, 16/16 - 1, \dots$ is constant thus converges.

    ### Exercise 7

    **For each of the following sequences, determine how many different limits of subsequences there are. Justify your answer**.

    1. $\lbrace 1 + -1^n \rbrace$;
    2. $\lbrace \cos(n \pi / 3) \rbrace$;
    3. $1, 1/2, 1, 1/2, 1/3, \dots$.

    Solution

    1. This sequence can achieve only two values $0$ or $2$, each may be achieved for infinitely many times, thus they are the (only) two different limits of subsequences.
    	For any value other than $0, 2$, WLOG say $a < 0$, then there exists $\varepsilon > 0$ such that $a + \varepsilon < 0$ thus no term in the sequence is in $(a - \varepsilon, a+ \varepsilon)$ thus $a$ cannot be a limit;
    2. Similar as above, this sequence achieves only three values $0.5, -0.5, -1$, each may be achieved for infinitely many times, and thus they are the only three different limits of subsequences;
    3. There are infinitely many different limits of subsequences:
    	Take $n_k = 1, 3, 6, 10, \dots$ then $a_{n_k} \equiv 1$;
    	Take $n_k = 2, 4, 7, 11, \dots$ then $a_{n_k} \equiv 1/2$;
    	$\dots$
    	Thus we can find a subsequence with limit $1/n$ for any $n$, i.e. there are infinitely many different limits.

    ### Exercise 12

    **Given a series $\sum\limits_{k = 1}^{\infty} a_k$, set $s_n = \sum\limits_{k = 1}^{n} a_k$ and $t_n = \sum\limits_{k = 1}^{n} | a_k |$. Prove that $\lbrace s_n \rbrace$ converges if $\lbrace t_n \rbrace$ is bounded**.

    Proof

    By construction $t_n$ is monotone non-decreasing, since it is also bounded, it converges. Thus it is Cauchy. In other word, for any $\varepsilon > 0$ there exists $N$ such that for all $n, m > N$, WLOG say $n > m$, we have $\varepsilon > | t_n - t_m | = | \sum\limits_{k = 1}^{n} | a_k | - \sum\limits_{k = 1}^{m} | a_k \| = \| a_{n+1} | + | a_{n+2} | + \dots + | a_m \|$ $\ge | a_{n+1} + a_{n+2} + \dots + a_m | = | s_n - s_m |$. Thus $s_n$ is Cauchy, thus it converges.

    ## Section 2.6

    ### Exercise 1

    **Find $\limsup{a_n}$ and $\liminf{a_n}$ for the following sequences**:

    1. $a_n = -1^n$;
    2. $a_n = (\frac{-1}{n})^n$;
    3. $a_n = \sin(n \pi/3)$.

    Solution

    1. This sequence achieves only two values $\pm 1$, and we have $\inf\limits_{n \ge k}a_n \equiv -1$ and $\sup\limits_{n \ge k}a_n \equiv 1$, thus $\limsup{a_n} = 1$ and $\liminf{a_n} = -1$;
    2. We have $-(\frac{1}{n})^n \le a_n \le (\frac{1}{n})^n$ thus by Squeeze Theorem $a_n \rightarrow 0$, and thus $\limsup{a_n} = \liminf{a_n} = 0$;
    3. Similar with the first part, this sequence achieves only $\frac{\sqrt{3}}{2}, 0, - \frac{\sqrt{3}}{2}$ thus $\inf\limits_{n \ge k}a_n \equiv - \frac{\sqrt{3}}{2}$ and $\sup\limits_{n \ge k}a_n \equiv \frac{\sqrt{3}}{2}$, thus $\limsup{a_n} = \frac{\sqrt{3}}{2}$ and $\liminf{a_n} = - \frac{\sqrt{3}}{2}$.

    ### Exercise 4

    **If $\limsup{a_n}$ and $\limsup{b_n}$ are finite, prove that $\limsup{a_n + b_n} \le \limsup{a_n} + \limsup{b_n}$**.

    Proof

    Consider the inequality $\sup\limits_{n \ge k}a_n + \sup\limits_{n \ge k}b_n \ge a_l + b_l$ for any $l > k$, thus by definition $\sup\limits_{n \ge k}a_n + \sup\limits_{n \ge k}b_n$ is an upper bound for $a_n + b_n$ thus we have:

    $\sup\limits_{n \ge k}a_n + \sup\limits_{n \ge k}b_n \ge \sup\limits_{n \ge k}(a_n + b_n)$.

    Now take limit each side, we have $\limsup{a_n + b_n} \le \limsup{a_n} + \limsup{b_n}$.

    ### Exercise 5

    **If $\limsup{a_n}$ is finite, prove that $\liminf{-a_n} = - \limsup{a_n}$**.

    Proof

    Similarly, we have learnt before that $\inf\limits_{n \ge k}-a_n = - \sup\limits_{n \ge k}a_n$, take limit each side we have $\liminf{-a_n} = - \limsup{a_n}$.

    ### Exercise 8

    **If $\lbrace a_n \rbrace$ and $\lbrace b_n \rbrace$ are non-negative sequences and $\lbrace b_n \rbrace$ converges, prove that $\limsup{a_n b_n} = (\limsup{a_n})(\lim\limits{b_n})$**.

    Proof

    Consider the inequality $\sup\limits_{n \ge k}a_n \sup\limits_{n \ge k}b_n \ge a_l b_l$ for any $l > k$, thus $\sup\limits_{n \ge k}a_n b_n \le \sup\limits_{n \ge k}a_n \sup\limits_{n \ge k}b_n$. Take limit each side we have $\limsup\limits_{n \ge k}a_n b_n \le \lim\limits(\sup\limits_{n \ge k}a_n \sup\limits_{n \ge k}b_n) = (\limsup\limits_{n \ge k}a_n) (\limsup\limits_{n \ge k}b_n)$. Since $b_n$ converges, $\limsup\limits_{n \ge k}b_n = \lim\limits{b_n}$, thus we have $\limsup{a_n b_n} = (\limsup{a_n})(\lim\limits{b_n})$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 7""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 3.1

    ### Exercise 5

    **Show that the function $f(x) = | x |$ is continuous on all of $\mathbb{R}$**.

    Proof

    For any $x, x' \in \mathbb{R}$, we have $\| x | - | x' \| \le | x - x' |$, thus simply take $\delta = \varepsilon$, we have $| x - x' | < \delta \implies | f(x) - f(x') | \le | x - x' | < \delta = \varepsilon$, which implies continuity by definition.

    ### Exercise 9

    **Consider the function $f(x) = \begin{cases} 1 \text{, if }x \ge 0 \\ -1 \text{, if }x < 0 \end{cases}$, is this function continuous if its domain is $\mathbb{R}$? Is it continuous if its domain is cut down to $\lbrace x \in \mathbb{R} | x \ge 0 \rbrace$? How about if its domain is $\lbrace x \in \mathbb{R} | x \le 0 \rbrace$**?

    Solution

    1. Consider $x' = 0$ and $\varepsilon = 1/2$. For any $\delta > 0$, $\lbrace x \| x - x' | < \delta \rbrace = (x' - \delta, x' + \delta) = (- \delta, \delta)$, then $- \delta/2$ is clearly in this interval and it is a negative real number, by construction $f(- \delta/2) = -1$ thus $| f(- \delta/2) - f(x') | = 1 > 1/2 = \varepsilon$. In other word, we have an $\varepsilon$ such that for any $\delta$, $| x - x' | < \delta$ does not imply that $| f(x) - f(x') | < \varepsilon$ Thus $f$ is not continuous at $0$;
    2. $f |_{\lbrace x \in \mathbb{R} | x \ge 0 \rbrace}$ is by construction a constant function, thus it is clearly continuous;
    3. $f |_{\lbrace x \in \mathbb{R} | x \le 0 \rbrace}$ is not continuous at $0$ by the same argument with (i).

    ### Exercise 11

    **Prove that the function $f(x) = \begin{cases} \sin(1/x) \text{, if }x \ne 0 \\ 0 \text{, if }x = 0 \end{cases}$ is not continuous at $0$**.

    Proof

    First recall that $\sin(y) = 1$ at $y = \dots, \frac{\pi}{2}, \frac{5 \pi}{2}, \dots$, i.e. $y$ is of the form $\frac{(1 + 4n) \pi}{2}, n \in \mathbb{Z}$ thus $\sin(1/x) = 1$ at $x = \dots, \frac{2}{\pi}, \frac{2}{5 \pi}, \dots$, i.e. $x$ is of the form $\frac{2}{(1 + 4n) \pi}, n \in \mathbb{Z}$.

    Now consider $x' = 0$ and $\varepsilon = 1/2$. For any fixed $\delta > 0$, by taking large enough $n_0$, clearly we have some $x = \frac{2}{(1 + 4n_0) \pi} < \delta$, but then $| x - x' | = x - 0 = \frac{2}{(1 + 4n_0) \pi} < \delta$ with $| f(x) - f(x') | = 1 \ge \varepsilon$. Thus $f$ is not continuous at $0$.

    ### Exercise 12

    **Prove that the function $f(x) = \begin{cases} x \sin(1/x) \text{, if }x \ne 0 \\ 0 \text{, if }x = 0 \end{cases}$ is continuous at $0$**.

    Proof

    Consider $x' = 0$, then $| f(x) - f(x') | = | x \sin(1/x) | \le | x |$ since $\sin(1/x)$ is bounded by $-1$ and $1$. Thus simply take $\delta = \varepsilon$ then we have $| x - 0 | < \delta \implies | f(x) - f(0) | \le | x | < \delta = \varepsilon$. By definition we have $f$ continuous at $0$.

    ## Section 3.2

    ### Exercise 2

    **Prove that if $f$ is a continuous function on a closed bounded interval $I$ and if $f(x)$ is never $0$ for $x \in I$, then there is a number $m > 0$ such that $f(x) \ge m$ for all $x \in I$ or $f(x) \le -m$ for all $x \in I$**.

    Proof

    Suppose that $\exists x_0, x_1 \in I$ such that $f(x_0) < 0 < f(x_1)$, then by IVT $f$ must achieve $0$ in $I$, which contradict our construction. Thus $\forall x \in f(x), f(x) < 0$ or $f(x) > 0$.

    If $f(x) < 0$ for all $x$, by EVT, $f$ achieves its maximum in $I$, i.e. $f(x) \le M$ for some $M$, notice this $M$ must be strictly negative (because it is achievable) thus if we take $m = -M > 0$, then $f(x) \le -m$ for all $x \in I$;

    Similarly if $f(x) > 0$ for all $x$, take $m$ as its minimum then we have $f(x) \ge m$ for all $x \in I$.

    ### Exercise 4

    **Find an example of a function which is continuous on a bounded interval $I$ but is not bounded. Then find an example of a function which is continuous and bounded on a bounded interval $I$, but does not have a maximum value**.

    Solution

    1. $f: (- \pi/2, \pi/2) \rightarrow \mathbb{R}$ given by $x \mapsto \tan(x)$ is clearly continuous, $(- \pi/2, \pi/2)$ is bounded, but its range is not bounded;
    2. Then consider $f: (-1, 1)$ (it could be any open interval in $\mathbb{R}$) $\rightarrow \mathbb{R}$ given by $x \mapsto \arctan{x}$ then $f$ is strictly increasing thus its maximum is never achieved, but $f$ is continuous and bounded (by $- \pi/2, \pi/2$) on the given bounded domain.

    ### Exercise 5

    **Find an example of a function which is continuous on a closed interval $I$ but is not bounded. Then find an example of a function which is continuous and bounded on a closed interval $I$, but does not have a maximum value**.

    Solution

    1. Notice that $\mathbb{R}$ itself is closed on $\mathbb{R}$, so the identity map from $\mathbb{R}$ to $\mathbb{R}$ is an unbounded continuous function on a closed interval;
    2. The above example $f: (-1, 1) \rightarrow \mathbb{R}$ given by $x \mapsto \arctan{x}$ would still work, if we simply extend $f$ to the entire real line.

    ### Exercise 7

    **Show that if $f$ and $g$ are continuous functions on the interval $[a, b]$ such that $f(a) < g(a)$ and $g(b) < f(b)$ then there is a number $c \in (a, b)$ such that $f(c) = g(c)$**.

    Proof

    Define $F$ be a function on the interval $[a, b]$ given by $F(a) = f(a) - g(a)$, then $F$ is constructed by two continuous functions with minus operation thus is continuous.

    We have $f(a) < g(a) \implies F(a) = f(a) - g(a) < 0$ and similarly $F(b) = f(b) - g(b) > 0$, by IVT we conclude that $F$ achieves $0$ on $(a, b)$, in other word, there is a number $c \in (a, b)$ such that $f(c) = g(c)$.

    ### Exercise 8

    **Let $f$ be a continuous function from $[0, 1]$ to $[0, 1]$. Prove there is a point $c \in [0, 1]$ such that $f(c) = c$**.

    Proof

    Define $F$ be a function on $[0, 1]$ by $F(a) = f(a) - a$, then $F$ is constructed by two continuous functions with minus operation thus is continuous.

    If $f(0) = 0$ or $f(1) = 1$ then we are done.

    Otherwise, since the codomain of $f$ is $[0, 1]$, we have $f(0) > 0$, $f(1) < 1$, thus $F(0) = f(0) - 0 > 0$ and $F(1) = f(1) - 1 < 0$, again by IVT we conclude that $F$ achieves $0$ and thus $f$ has a fixed point.

    ### Exercise 9

    **Use the IVT to prove that, if $n$ is a natural number, then every positive number $a$ has a positive $n$-th root**.

    Proof

    For each given $n$ consider the function $f: \mathbb{R}_{\ge 0} \implies \mathbb{R}$ given by $x \mapsto x^n$. Clearly $f(0) = 0$, thus $f(0) < a$ for any positive $a$. Now take $x = \max{(1, a)}$, then if $a \le 1$ then $f(x) = 1^n = 1 \ge a$, if $a > 1$ then $f(x) = a^n \ge a$ for all natural $n$. In either case, we have $f(0) < a \le f(x)$, thus $a$ is a value that $f$ achieves by IVT, in other word, there exists $a' \in \mathbb{R}_{\ge 0}$ such that $a'^n = a$, where $a'$ could be considered as a positive $n$-th root of this arbitrary positive $a$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Fall Semester Homework 8""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 3.3

    ### Exercise 1

    **Is the function $f(x) = x^2$ uniformly continuous on $(0,1)$? Justify your answer**.

    Solution

    If we extend the domain to $[0, 1]$, $f$ is still well defined. Notice that $f$ (being a product of inclusion maps) is continuous on $[0, 1]$, a closed and bounded interval, thus $f$ is uniformly continuous on $[0, 1]$, thus it is clearly also uniformly continuous on a subset $(0, 1)$.

    ### Exercise 2

    **Is the function $f(x) = 1/x^2$ uniformly continuous on $(0,1)$? Justify your answer**.

    Solution

    Let $\varepsilon = 1$, for any $\delta > 0$, take $n \in \mathbb{N}$ such that $\frac{1}{n} < \delta$, then if we take $x_1 = \frac{1}{n}, x_2 = \frac{2}{n}$, then $| x_1 - x_2 | < \delta$, while $| f(x_1) - f(x_2) | = | \frac{1}{\frac{1}{n}} - \frac{1}{\frac{2}{n}} | = | n - \frac{n}{2} | = | \frac{n}{2} |$, since $n$ can be taken arbitrarily large, this value is clearly large than $\varepsilon$. By definition, $f$ is not uniformly continuous on $(0, 1)$.

    ### Exercise 3

    **Is the function $f(x) = x^2$ uniformly continuous on $(0, \infty)$? Justify your answer**.

    Solution

    Let $\varepsilon = 1$, for any $\delta > 0$, take $n \in \mathbb{N}$ such that $\frac{1}{n} < \delta$, then if we take $x_1 = n, x_2 = n + \frac{1}{n}$, then $| x_1 - x_2 | < \delta$, while $| f(x_1) - f(x_2) | = | n^2 - n^2 - \frac{1}{n^2} - 2 | = 2 + \frac{1}{n^2} > 1 = \varepsilon$. By definition, $f$ is not uniformly continuous on $(0, \infty)$.

    ### Exercise 4

    **Using only the $\varepsilon - \delta$ definition of uniform continuity, prove that the function $f(x) = \frac{x}{x + 1}$ is uniformly continuous on $[0, \infty)$**.

    Proof

    Let $x \ne y \in [0, \infty)$ be two arbitrary points, then $| f(x) - f(y) | = | \frac{x}{x+1} - \frac{y}{y+1} | = | \frac{x(y+1) - y(x+1)}{(x+1)(y+1)} | = | \frac{x - y}{(x+1)(y+1)} | \le | x - y |$. Thus simply let $\delta = \varepsilon$, then $| x - y | < \delta \implies | f(x) - f(y) | \le | x - y | < \varepsilon$, for any $\varepsilon$.

    ### Exercise 5

    **Show that $\sqrt{x}$ is uniformly continuous on $[0, 1]$**.

    Proof

    We know from previous materials that $\sqrt{x}$ is continuous on $[0, 1]$, since $[0, 1]$ is closed and bounded, $f$ is also uniformly continuous on it.

    ### Exercise 8

    **Let $f$ be a function defined on an interval $I$ and suppose that there are positive constants $K$ and $r$ such that $| f(x) - f(y) | \le K | x - y |^r$ for all $x, y \in I$. Prove that $f$ is uniformly continuous**.

    Proof

    Since $K$ and $r$ are fixed, then for any $\varepsilon$, take $\delta = \sqrt[r]{\frac{\varepsilon}{K}}$, then $| f(x) - f(y) | \le K | x - y |^r < K (\sqrt[r]{\frac{\varepsilon}{K}})^r = \varepsilon$. By definition $f$ is uniformly continuous.

    ### Exercise 9

    **Is the function $f(x) = \sin(1/x)$ continuous on $(0, 1)$? Is it uniformly continuous on $(0, 1)$? Justify your answer**.

    Solution

    $f$ is a composition of the sine function and a function of the form $x^r$, thus on their natural domain, $f$ is continuous.

    For previous homework we have $\sin(1/x) = 1$ at $x = \dots, \frac{2}{\pi}, \frac{2}{5 \pi}, \dots$, i.e. $x$ is of the form $\frac{2}{(4n + 1) \pi}, n \in \mathbb{Z}$. Similarly we have $\sin(1/x) = -1$ at $x$ with the form $\frac{2}{(4n - 1) \pi}, n \in \mathbb{Z}$ or $\frac{2}{(4n + 3) \pi}, n \in \mathbb{Z}$.

    For any $\delta$, clearly if we take sufficiently large $n$ then we would have $| \frac{2}{(4n - 1) \pi} - \frac{2}{(4n + 1) \pi} | < \delta$, but the distance of their images is a constant $2$. Thus $f$ is not uniformly continuous on $(0, 1)$.

    ### Exercise 10

    **Is the function $f(x) = x \sin(1/x)$ uniformly continuous on $(0, 1)$? Justify your answer**.

    Solution

    We proved in the last homework that if we define $f(0) = 0$ then the extension of $f$ on $[0, 1]$ is continuous (the case at $1$ is natural), thus $f$ is uniformly continuous on $(0, 1)$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 4.4

    ### Exercise 2

    **Prove that $| \sin(x) - x | \le \frac{1}{6}| x |^3$**.

    Proof

    Let $g(x) = \sin(x) - x$ and $f(x) = \frac{1}{6}x^3$. Easy to verify that $g(0) = f(0) = 0$ and that $f(x) \ne 0$ whenever $x \ne 0$.

    By Mean Value Theorem we have for $x > 0$, there exists $0 < c < x$ with $\frac{\sin(x) - x}{\frac{1}{6}x^3} = \frac{g(x) - g(0)}{f(x) - f(0)} = \frac{g'(c)}{f'(c)} = \frac{\cos(c) - 1}{\frac{1}{2}c^2}$.

    Now notice that if we take the numerator and denominator as the new $g$ and $f$ then again we have $g(0) = f(0) = 0$ and $f(x) \ne 0$ whenever $x \ne 0$.

    So we can apply Mean Value Theorem again, actually twice, to get that:

    1. There exists $0 < c_1 < c$ such that $\frac{\sin(x) - x}{\frac{1}{6}x^3} = \frac{\cos(c) - 1}{\frac{1}{2}c^2} = \frac{-\sin(c_1)}{c_1}$;
    2. There exists $0 < c_2 < c_1$ such that $\frac{\sin(x) - x}{\frac{1}{6}x^3} = \frac{\cos(c) - 1}{\frac{1}{2}c^2} = \frac{-\sin(c_1)}{c_1} = -\cos(c_2)$.

    Similar result with a minus sign can be reached for $x < 0$, thus we conclude that $\frac{| \sin(x) - x |}{\frac{1}{6}| x |^3} = | \cos(c_2) | \le 1$ for all $x \ne 0$ thus $| \sin(x) - x | \le \frac{1}{6}| x |^3$ for all $x$ (at $0$ it is clear that left hand side equals right hand side).

    ### Exercise 4

    **If $f$ is a function which is differentiable on an open interval $I$ containing $0$ and $f(0) = 0$, then prove that there is a $c$ between $0$ and $x$ at which $f(x) = \frac{f'(c)x^n}{c^{n-1}n}$**.

    Proof

    Let $g(x) = x^n$, notice that $g(0) = 0$ and $g(x) \ne 0$ whenever $x \ne 0$.

    Apply Mean Value Theorem we have that for $x > 0$, there exists $0 < c < x$ with $\frac{f(x) - f(0)}{g(x) - g(0)} = \frac{f'(c)}{g'(c)} = \frac{f'(c)}{n c^{n - 1}}$ $\implies f(x) = \frac{f'(c)x^n}{c^{n-1}n}$. Same result holds with a negative $x$.

    ### Exercise 5

    **Use the previous exercise and induction to prove that if $f$ is $n$-times differentiable on an open interval $I$ containing $0$ and if the $k$-th derivative $f^{(k)}$ of $f$ is $0$ at $0$ for $k = 0, 1, \dots, n-1$ then there is a $c$ between $0$ and $x$ at which $f(x) = f^{(n)}(c)\frac{x^n}{n!}$**.

    Proof

    We just proved the case where $n = 1$, for $n > 1$:

    Again take $g(x) = x^n$.

    Apply Mean Value Theorem we have that for $x > 0$, there exists $0 < c < x$ with $\frac{f(x) - f(0)}{g(x) - g(0)} = \frac{f'(c)}{g'(c)} = \frac{f'(c)}{n c^{n - 1}}$. As functions of $c$, $f'(0) = 0$ and $n0^{n-1} = 0$, so we can apply Mean Value Theorem again to get that there exists $0 < c_1 < c$ with $\frac{f(x) - f(0)}{g(x) - g(0)} = \frac{f'(c)}{g'(c)} = \frac{f'(c)}{n c^{n - 1}} = \frac{f''(c_1)}{n (n - 1)c_1^{n - 2}}$. By assumption we can actually continuing to apply Mean Value Theorem to get $\frac{f(x) - f(0)}{g(x) - g(0)} = \frac{f'(c)}{g'(c)} = \frac{f'(c)}{n c^{n - 1}} = \frac{f''(c_1)}{n (n - 1)c_1^{n - 2}} = \frac{f^{(3)}(c_2)}{n (n - 1) (n - 2)c_2^{n - 3}} = \dots = \frac{f^{(n-1)}(c_{n-2})}{n (n - 1) \dots 2 c_{n-2}} = \frac{f^{(n)}(c_{n-1})}{n!c_{n-1}}$ for some $0<c_{n-1}<\dots<c_1<c$. Name this $c_{n-1}$ as $c$ and we get the desired result. Same result holds for negative $x$.

    ### Exercise 6

    $\lim\limits_{x\to\infty}\frac{\ln{x}}{x^r}$ **where $r > 0$**.

    Solution

    $\lim\limits_{x \to \infty}\ln{x} = \infty$ and $\lim\limits_{x \to \infty}x^r = \infty$, meanwhile $\lim\limits_{x\to\infty}\frac{(\ln{x})'}{(x^r)'} = \lim\limits_{x\to\infty}\frac{1}{rx^r} = 0$ exists, thus by L'Hôpital's Rule the original limit is also $0$.

    ### Exercise 7

    $\lim\limits_{x \to 0} x\ln x$.

    Solution

    Left limit does not exist as $\ln$ is undefined with negative values. For the right limit, $\lim\limits_{x \to 0} x\ln x = \lim\limits_{x \to 0} \frac{\ln x}{1/x}$. Both numerator and denominator have limit infinity. Take derivatives for numerator and denominator and the result limit $= \lim\limits_{x \to 0} -x$ and this limit clearly exists and equals $0$. Thus by L'Hôpital's Rule the original (right) limit is also $0$.

    ### Exercise 8

    $\lim\limits_{x \to 0}\frac{\sin(x)-x}{x^3}$.

    Solution

    This limit has the form $0/0$, by L'Hôpital's Rule $\lim\limits_{x \to 0}\frac{\sin(x)-x}{x^3} = \lim\limits_{x \to 0}\frac{\cos(x)-1}{3x^2} = \lim\limits_{x \to 0}\frac{-\sin(x)}{6x} = \lim\limits_{x \to 0}\frac{-\cos(x)}{6} = -1/6$.

    ### Exercise 9

    $\lim\limits_{x\to 0}\frac{1+\cos(x)}{x^2}$.

    Solution

    This limit has the form $c/0$ and clearly has the result $= \infty$.

    (Maybe the author meant $1 - \cos(x)$ here? Then by L'Hôpital's Rule $\lim\limits_{x\to 0}\frac{1-\cos(x)}{x^2} = \lim\limits_{x\to 0}\frac{\sin(x)}{2x} = \lim\limits_{x\to 0}\frac{\cos(x)}{2} = 1/2$.)

    ### Exercise 10

    $\lim\limits_{x\to 0}x^x$.

    Solution

    The left side limit does not exist as for negative rational $x$ with odd denominator $x^x$ is undefined on $\mathbb{R}$. For the right limit $\lim\limits_{x\to 0+}x^x = \lim\limits_{x\to 0+}\exp{\ln{x^x}} = \exp\lim\limits_{x\to 0+}x\ln{x} = \exp{0} = 1$ by previous exercise.

    ### Exercise 12

    $\lim\limits_{x \to \infty}(\sqrt{x+1} - \sqrt{x})$.

    Solution

    Claim the limit is $0$:

    For any $\varepsilon0$, we have $| \sqrt{x+1} - \sqrt{x} | = | (\sqrt {x+1} - \sqrt{x}) \frac{\sqrt{x+1} + \sqrt{x}}{\sqrt{x+1} + \sqrt{x}} | = | \frac{1}{\sqrt{x+1} + \sqrt{x}} | < | \frac{1}{2\sqrt{x+1}} | < \varepsilon$ whenever $m < x$ for larger enough $m$. By definition the original limit is $0$.

    ### Exercise 14

    **Let $f$ be a differentiable function on $(0, \infty)$. Prove that if $\lim\limits_{x\to\infty}f(x) = \infty$ and $\lim\limits_{x\to \infty}f'(x) = L$ then $\lim\limits_{x\to\infty}\frac{e^{f(x)}}{\int_0^x e^{f(t)}dt} = L$**.

    Proof

    Since $\lim\limits_{x\to\infty}f(x) = \infty$, we have $\lim\limits_{x\to\infty}e^{f(x)} = \infty$, and observe that the area below $e^{f(t)}$ from $0$ to $x$ goes to infinity as $x$ goes (I cannot see a way to explicitly write it…). If we take derivatives for both numerator and denominator we have $(e^{f(x)})' = f'(x)e^{f(x)}$ and $(\int_0^x e^{f(t)}dt)' = e^{f(x)}$ by Fundamental Theorem of Calculus. It is easy to see that now we can apply L'Hôpital's Rule and thus the original limit equals $\lim\limits_{x\to \infty}f'(x) = L$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 2""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 5.1

    ### Exercise 2

    **Prove that $\int_0^1xdx$ exists by computing $U(f,P_n)$ and $L(f,P_n)$ for the function $f(x) = x$ and a partition $P_n$ of $[0,1]$ into $n$ equal sub-intervals. Then show that condition 5.1.7 of Theorem 5.1.8 is satisfied. Calculate the integral by taking the limit of the upper sums**.

    Proof

    $f(x) = x$ is a simple non-decreasing function so $m$ and $M$ in the calculation of $L$ and $U$ are easy.

    We have (for a certain $n$):

    $U(f,P_n) = \sum\limits_{i=0}^{n-1}\frac{1}{n}\frac{i+1}{n}$ and $L(f,P_n) = \sum\limits_{i=0}^{n-1}\frac{1}{n}\frac{i}{n}$. Thus $U - L = \sum\limits_{i=0}^{n-1}\frac{1}{n^2}< 1/n$, and clearly for any $\varepsilon$ one can choose large enough $n$ so that $U-L<1/n < \varepsilon$, thus the Riemann integral exists.

    With exactly the same argument, with the same sequence of partition, we have $\lim\limits(U-L) = \lim\limits{1/n} =0$, thus the 5.1.7 condition is satisfied.

    And we can use the summation formula to calculate $\lim\limits_{n\to \infty}U(f, P_n)$ $= \lim\limits\frac{1}{n^2}\sum\limits_{i=0}^{n-1}i+1$ $= \lim\limits\frac{1}{n^2}\frac{(1+n)n}{2}$ which is clearly $1/2$.

    ### Exercise 3

    **Prove by induction that $\sum\limits_{k=1}^nk^2 = \frac{n(n+1)(2n+1)}{6}$**.

    Proof

    Statement is clearly true for $n = 1$. If it is true for $n$, then $\sum\limits_{k=1}^{n+1}k^2 = \sum\limits_{k=1}^{n}k^2 + (n+1)^2$ $= \frac{n(n+1)(2n+1)}{6} + (n+1)^2$ $= \frac{n(n+1)(2n+1) + 6(n+1)^2}{6}$. Now it is easy to verify that $n(n+1)(2n+1) + 6(n+1)^2$ $= 2n^3 + 9n^2 + 13n+6$ $= (n+1)(n+2)(2n+3)$, thus the statement holds for $n+1$.

    ### Exercise 4

    **Prove that $\int_0^ax^2dx = a^3/3$ by expressing this integral as a limit of Riemann sums and find the limit**.

    Proof

    $\int_0^ax^2dx =\lim\limits_{n\to \infty}\sum\limits_{m=1}^{n}\frac{a}{n}(\frac{ma}{n})^2 = \lim\limits_{n\to \infty}\frac{a^3}{n^3}\sum\limits_{m=1}^{n}m^2$, now by above exercise we have $= \lim\limits_{n\to \infty}\frac{a^3}{n^3}\frac{n(n+1)(2n+1)}{6}$, it clearly has the limit $a^3/3$.

    ### Exercise 5

    **Let $f$ be the function on $[0,1]$ which is $0$ at every rational number and is $1$ at every irrational number. Is this function integrable on $[0,1]$? Prove that your answer is correct by using the definition of the integral**.

    Proof

    No.

    A fact from last semester that we need: any interval on $\mathbb{R}$ contains both rational and irrational numbers.

    This means that the lower sum $L = \sum m_i(x_{i+1} - x_i)$ is always $0$ because each $m_i$ is zero, while that the upper sum is always $1$, whichever partition we take. Thus they never equal and $f$ is not integrable.

    ### Exercise 8

    **Suppose $m$ and $M$ are lower and upper bounds for $f$ on $[a, b]$; that is, $m \le f(x) \le M, \forall x \in [a, b]$. Prove that $m(b-a)$ $\le \underline{\int_a^b}f(x)dx$ $\le \overline{\int_a^b}f(x)dx$ $\le M(b-a)$. What conclusion about $\int_a^bf(x)dx$ do you draw from this if the integral exists**?

    Proof

    $\overline{\int_a^b}f(x)dx$ $\overset{\text{def}}{=} \inf{U(f,P)}\le U(f,P)$ $\overset{\text{def}}{=}\sum\limits_iM_i(x_{i+1}-x_{i-1})$ $\le\sum\limits_iM(x_{i+1}-x_{i-1})=M(b-a)$, similar for the lower side. Also naturally we have $L(f,P) \le U(f,P)$ for any $P$ and thus $\underline{\int_a^b}f(x)dx \le \overline{\int_a^b}f(x)dx$.

    Join everything together we have $m(b-a)$ $\le \underline{\int_a^b}f(x)dx$ $\le \overline{\int_a^b}f(x)dx$ $\le M(b-a)$.

    We can conclude that $m(b-a)$ $\le \int_a^bf(x)dx$ $\le M(b-a)$ if it exists, because it is defined to be equal to the upper and lower integral, if it exists.

    ## Section 5.2

    ### Exercise 6

    **Prove that $1 \le \int_{-1}^1\frac{1}{1+x^{2n}}dx \le 2$ for all $n \in \mathbb{N}$**.

    Proof

    On $[-1,1]$, $\frac{1}{1+x^{2n}}$ is clearly bounded above by $M= 1$ ($x^{2n}$ always positive) and bounded below by $m = 1/2$ ($x^{2n}$ always less than $1$). By above exercise the integral is bounded by $m(b-a) = 1$ and $M(b-a) = 2$.

    ### Exercise 9

    **Prove that if $f$ is integrable on $[a,b]$, so is $f^2$**.

    Proof

    Let $P_n$ be Archimedean over $f$, then $\lim\limits{U(f^2,P_n) - L(f^2,P_n)} = \lim\limits{\sum\limits_i(M_i^{f^2}-m_i^{f^2})(x_{i+1}-x_i)}$ $= \lim\limits{\sum\limits_i(M_i^2-m_i^2)(x_{i+1}-x_i)}$ $= \lim\limits{\sum\limits_i(M_i + m_i)(M_i-m_i)(x_{i+1}-x_i)}$ ($*$), let $M^{*}$ be $\sup\limits{f(x)} + 1$, then ($*$) $< 2M^{*} \lim\limits{\sum\limits_i(M_i - m_i)(x_{i+1}-x_i)}$, but since $2M^{*}$ is fixed, this value goes to $0$ as $n \to \infty$, i.e. $\lim\limits{U(f^2,P_n) - L(f^2,P_n)} = 0$, thus $f^2$ is integrable.

    ### Exercise 10

    **Prove that if $f$ and $g$ are integrable on $[a,b]$, so is $fg$**.

    Proof

    Assuming we know that if $f$ and $g$ are integrable on $[a,b]$, so are $f+g$ (and $f-g$), which is proved during class, and $f^2$, which is proved above.

    Now $fg = \frac{1}{2}((f+g)^2 - f^2 - g^2)$, by above statement, $fg$ is integrable (easy to see $cf$ is integrable if $f$ is, because clearly $c\sum\limits(M_i-m_i)\to 0$).

    ## Section 5.3

    ### Exercise 4

    **Find $\frac{d}{dx}\int_{1/x}^xe^{-t^2}dt$**.

    Solution

    $e^{-t^2}$ is clearly continuous and thus Riemann integrable. Thus by Theorem 5.3.3 let $F(x) = \int_{1/x}^xe^{-t^2}dt = \int_{0}^xe^{-t^2}dt - \int_0^{1/x}e^{-t^2}dt$, **the derivative of the** first part simply equals $e^{-x^2}$ and for the second part we differentiate $F(1/x)$ which is $-x^{-2}F'(1/x)=-x^{-2}e^{-1/x^2}$. Together we have $\frac{d}{dx}\int_{1/x}^xe^{-t^2}dt = e^{-x^2} + x^{-2}e^{-1/x^2}$.

    ### Exercise 5

    **If $f(x) = -1/x$ then $f'(x) = 1/x^2$. Thus, Theorem 5.3.1 seems to imply that $\int_{-1}^11/x^2dx = f(1) - f(-1) = -1-1 = -2$. However, $1/x^2$ is a positive function, and so its integral over $[-1, 1]$ should be positive, what is wrong**?

    Solution

    $f'$ is not even integrable (bounded) on $[-1, 1]$.

    ### Exercise 9

    **Prove that if $f$ is integrable on $[a,b]$ and $c \in [a, b]$ then changing the value of $f$ at $c$ does not change the fact that $f$ is integrable or the value of its integral on $[a, b]$**.

    Proof

    Suppose $f(c) = y$ and say the new $\tilde{f(c)} = z$. Let $m$ denote the difference $m = |z - y|$.

    Say $P_n$ is Archimedean for $f$ and fix any $\varepsilon > 0$: add $\lbrace c - \varepsilon/2m, c + \varepsilon/2m\rbrace$ into each partition $P_i$'s and the new sequence of partitions (let's call it $\tilde{P_n}$) is still Archimedean for $f$ by the Refinement Lemma.

    We have: $| U(\tilde{f}, \tilde{P_n}) - L(\tilde{f}, \tilde{P_n}) |$ $= | U(\tilde{f}, \tilde{P_n}) +U(f,\tilde{P_n}) -U(f,\tilde{P_n}) + L(f,\tilde{P_n}) - L(f,\tilde{P_n})- L(\tilde{f}, \tilde{P_n}) |$ $\le | U(\tilde{f}, \tilde{P_n}) -U(f,\tilde{P_n})|$ $+| U(f,\tilde{P_n}) - L(f,\tilde{P_n})|$ $+| L(f,\tilde{P_n})- L(\tilde{f}, \tilde{P_n}) |$ ($*$).

    Now:

    1. The first term is less than or equal to $\varepsilon$: the only difference of upper sum of $f$ and $\tilde{f}$ is at $c$ and the difference is $m$, but the 'rectangle' there has width $\varepsilon/m$;
    2. The second term is less than $\varepsilon$, by the integrability of $f$;
    3. The third term is less than or equal to $\varepsilon$ for the same reason with the first term.

    So ($*$) $< 3\varepsilon \to 0$ so $\tilde{f}$ is integrable. Also by above we have $| U(\tilde{f}, \tilde{P_n}) -U(f,\tilde{P_n})| \to 0$ so the integral does not change value.

    ### Exercise 10

    **The function $f(x) = x/| x |$ has derivative $0$ everywhere but at $x = 0$. Its derivative $f'(x) = 0$ is integrable on $[-1, 1]$ and has integral $0$. However $f(1)-f(-1) = 2$. This seems to contradict Theorem 5.3.1. Explain why it does not**.

    Solution

    Theorem 5.3.1 requires $f$ to be continuous on $[a,b]$ and differentiable on $(a,b)$, neither conditions is met, so I do not see why we can even apply the theorem here.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 3""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 5.4

    ### Exercise 5

    **Using Definition 5.4.8 and the properties of $\exp$ prove the laws of exponents $a^{x+y} = a^xa^y$ and $a^{xy} = (a^x)^y$**.

    Proof

    $a^{x+y} \overset{\text{def}}{=} \exp{((x+y)\ln{a})} = \exp{(x\ln{a} + y\ln{a})}$ $=\exp{(x\ln{a})}\exp{(y\ln{a})} \overset{\text{def}}{=} a^xa^y$;

    $a^{xy} \overset{\text{def}}{=} \exp{(xy\ln(a))} = \lim\limits_{n \to \infty}\exp{(xy_n\ln(a))} =$, with rational $y_n \to y$, by continuity of $\exp$, $= \lim\limits_{n \to \infty}(\exp{(x\ln(a))})^{y_n}$ $\overset{\text{def}}{=} \lim\limits_{n \to \infty} (a^x)^{y_n} = (a^x)^y$.

    ### Exercise 6

    **Compute the derivative of $a^x$ for each $a > 0$**.

    Solution

    $\frac{da(x)}{dx} = \frac{d(\exp{(x\ln(a)}))}{dx}$ by chain rule $=\ln(a) \exp{(x \ln{a})} = \ln{a} \cdot a^x$.

    ### Exercise 8

    **If $f, g$ are integrable then $fg$ is integrable**.

    Proof

    $f, g$ are integrable then the sets of discontinuity $D_f$ and $D_g$ are negligible, claim that $D_{fg} \subseteq D_f \cup D_g$: suppose not, then there exists a point $p$ with $fg$ not continuous at $p$ but $f$ and $g$ are continuous at $p$, this cannot be true.

    Now another claim, finite union of negligible sets are negligible: say we have two negligible sets $A, B$. By definition we can choose the coverings $\cup I_{A_i}$ and $\cup I_{B_i}$ with each sum of volume less than $\varepsilon/2$, thus their union's sum of volume is less than $\varepsilon$.

    Thus $D_f \cup D_g$ and thus $D_{fg}$ is negligible, and thus $fg$ is integrable.

    ## Section 6.1

    ### Exercise 4

    **Determine whether the series converges: $\sum\limits_{k = 1}^{\infty} \frac{k^2-3k+1}{3k^2+k-2}$**.

    Solution

    The series diverges as $\frac{k^2-3k+1}{3k^2+k-2} \to \frac{1}{3} \ne 0$ when taking $k \to \infty$.

    ### Exercise 6

    **Determine whether the series converges: $\sum\limits_{k=1}^{\infty}\frac{k}{k^2-k+2}$**.

    Solution

    Easy to verify that $k^2-k+2 \le 2k^2$ for all natural $k$, thus $\frac{k}{k^2-k+2} \ge \frac{k}{2k^2} = \frac{1}{2k}$, by comparison test, if $\sum\limits_{k=1}^{\infty}\frac{k}{k^2-k+2}$ converges then so does $\sum\limits_{k=1}^{\infty}\frac{1}{k}$, which is not true, so $\sum\limits_{k=1}^{\infty}\frac{k}{k^2-k+2}$ does not converge.

    ### Exercise 8

    **Determine whether the series converges absolutely: $\sum\limits_{k = 1}^{\infty}\frac{-1^{k+1}}{\sqrt{k}}$**.

    Solution

    Taking term-wise absolute value the series becomes $\sum\limits_{k=1}^{\infty}\frac{1}{\sqrt{k}} = \sum\limits_{k=1}^{\infty}\frac{1}{k^{1/2}}$, which diverges as $1/2 < 1$.

    ### Exercise 11

    **Prove the following weak version of the comparison test using Theorem 6.1.8: If $a_1+a_2+\dots + a_k+\dots$ and $b_1+\dots+b_k+\dots$ are series of non-negative terms with $a_k \le b_k$ for all $k$, then if $b_1+\dots+b_k+\dots$ converges, so does $a_1+\dots+a_k+\dots$**.

    Proof

    By Theorem 6.1.8, if $\sum b_k$ converges then $\lbrace s_{b_n} \rbrace$ is bounded above. Say $M$ is a bound, thus $s_{b_n} = b_1 + \dots + b_n \le M$ for any $n$, but then $a_1 + \dots + a_n \le b_1 + \dots + b_n \le M$, thus $M$ is also a bound for $\lbrace s_{a_n} \rbrace$, since Theorem 6.1.8 is an if and only if statement, this implies that $\sum a_k$ converges.

    ### Exercise 12

    **Consider the decimal expansion $.d_1d_2\dots$ of a real number between $0$ and $1$, where $d_k$ is a sequence of integers between $0$ and $9$. This decimal expansion represents the sum of a certain infinite series, what series is it and why does it converge**?

    Solution

    $.d_1d_2\dots$ can be written as $0.d_1 + 0.0d_2+ \dots = d_110^{-1}+d_210^{-2}+\dots$ $=\sum\limits_{n=1}^{\infty}\frac{d_n}{10^n}$, this is a power series. Now since $d_k$ is between $0$ and $9$ we have $\sum\limits_{n=1}^{\infty}\frac{d_n}{10^n} \le \sum\limits_{n=1}^{\infty}\frac{9}{10^n} = 9\sum\limits_{n=1}^{\infty}0.1^n$, which is a convergent geometric series (to $1$), by comparison test the original decimal expansion is convergent.

    ### Exercise 13

    **Show that every real number in the interval $[0,1]$ has a decimal expansion as described in the previous exercise**.

    Proof

    Let's call the real number $r$, say $r \ne 1$ for the moment. Split $[0,1)$ to ten intervals $[0, \frac{1}{10}),[\frac{1}{10}, \frac{2}{10}), \dots, [\frac{9}{10}, 1)$. Clearly $r$ lies inside exactly one of the interval, say $r \in [\frac{k}{10}, \frac{k+1}{10})$, name $d_1 = k$.

    Similarly, split $[\frac{d_1}{10}, \frac{d_1+1}{10})$ to ten intervals $[\frac{d_1}{10}, \frac{d_1}{10}+\frac{1}{100}), \dots, [\frac{d_1}{10}+\frac{9}{100}, \frac{d_1+1}{10})$, this induces unique $d_2$. Repeat this process to get unique $\lbrace d_k \rbrace$, then by construction we have $.d_1d_2\dots = \lim\limits \frac{d_1}{10}+\frac{d_2}{100}+\dots = r$ (because the error term is $\frac{1}{10^k} \to 0$) so $.d_1d_2d_3\dots$ works as the decimal expansion of $r$.

    Now, if $r = 1$, if we allow $1 = 1.000\dots$ then we are done. Otherwise, claim that $r = 0.999\dots$, $d_k = 9$ for all $k$, is the decimal expansion of $1$:

    If not, since $r' = 0.999\dots$ clearly locates on the real line, it is a real number, observe that we have $0 \le r' \le 1$ (there is no way it is greater than $1$ or be negative). If $r' \ne 1 = r$, then there exists some other real number with $r' < r^{*} < r$, so we have $r^{*} \in [0, 1)$, thus it has a decimal expansion as constructed above, but by the construction, each decimal of $r^{*}$ is bounded above by $9$ thus $r^{*}$ is bounded above by $r'$, so we have $r' < r^{*} \le r'$ which is a contradiction.

    ## Section 6.2

    ### Exercise 1

    **Determine whether the series converges: $\sum\limits_{k = 2}^{\infty}\frac{1}{k \ln{k}}$**.

    Solution

    By integral test the series converges if and only if $\int_2^{\infty}\frac{1}{k \ln{k}}dk = \ln(\ln(k))|_2^{\infty}$ converges. Which is not true as $\ln(\ln(2))$ is a fixed real number but $\ln(\ln(k))$ goes to infinity as $k \to \infty$.

    ### Exercise 5

    **Determine whether the series converges: $\sum\limits_{k=1}^{\infty}\frac{k}{(3+-1^{k})^k}$**.

    Solution

    $\limsup | \frac{k}{(3+-1^{k})^k} |^{1/k}$ $= \limsup \frac{k}{(3+-1^{k})^k}^{1/k}$ $= \lim\limits \frac{k^{1/k}}{2} = 1/2 < 1$ thus by root test the series converges.

    ### Exercise 8

    **Determine whether the series converges: $\sum\limits_{k=1}^{\infty}ke^{-\sqrt{k}}$**.

    Solution

    Consider the sequence $k^3e^{-\sqrt{k}} = \frac{k^3}{e^{\sqrt{k}}}$, taking $k \to \infty$, we may apply L'Hôpital's Rule (for many times… before the power of $k$ on the top hits $0$, each turn is valid because clearly $ak^b \to \infty$ for positive $a,b$ and $e^{\sqrt{k}} \to \infty$) and we have that $\lim\limits_{k \to \infty}k^3e^{-\sqrt{k}} = 0$. We know that $\sum \frac{1}{k^2}$ converges, thus $\sum ke^{-\sqrt{k}} = \sum \frac{1}{k^2}k^3e^{-\sqrt{k}}$ (term-wise product of bounded sequence and (absolutely) convergent series) is convergent by the following exercise.

    ### Exercise 11

    **Prove that if $\sum a_k$ converges absolutely and $\lbrace b_k \rbrace$ is a bounded sequence, then $\sum a_kb_k$ also converges absolutely**.

    Proof

    WLOG say $a_k, b_k \ge 0$ for all $k$ (otherwise simply take the absolute value, then $\sum | a_k |$ by construction still converges absolutely and $\lbrace | b_k | \rbrace$ is bounded).

    Say $\lbrace b_k \rbrace$ is bounded by $M$. Denote $s_k = \sum a_kb_k$.

    For any $0<n<m$, $| s_m - s_n | = | a_{n+1}b_{n+1} + \dots + a_mb_m |$ $\le M| a_{n+1} +\dots + a_m|$. Since $\sum a_k$ is convergent, we have that by Cauchy test, fixing $\varepsilon$, there exists $N$ such that $| a_{n+1} +\dots + a_m| < \varepsilon/M$ whenever $n,m > N$. But then $| s_m - s_n | < M\varepsilon/M = \varepsilon$, thus $\sum a_kb_k$ converges by Cauchy test. Since we assumed that all terms are positive, $\sum a_kb_k$ is automatically absolutely convergent.

    ### Exercise 12

    **Prove that if $\sum a_k$ and $\sum b_k$ are series and $a_k = b_k$ except for finitely many values of $k$, then the two series either both converge or diverge**.

    Proof

    By assumption we can find $N \in \mathbb{N}$ such that $a_k = b_k$ whenever $k > N$, otherwise there are infinitely many different $a_k \ne b_k$. Now $\sum\limits_{k \in \mathbb{N}}a_k$ converges if and only if $\sum\limits_{k > N} a_k = \sum\limits_{k > N} b_k$ converges if and only if $\sum\limits_{k \in \mathbb{N}}b_k$ converges. Same for divergent series.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 4""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 6.3

    ### Exercise 1

    **Determine whether the given series converges absolutely, converges conditionally, or diverges: $\sum\limits_{k=1}^{\infty}\frac{(-1)^k}{k^{1/3}}$**.

    Solution

    1. $\lim\limits_{k \to \infty}\frac{1}{k^{1/3}}$ is $0$, thus the alternating series converges simply;
    2. $1/3 < 1$ thus we have $\sum \frac{1}{k^{1/3}}$ diverges, i.e. the original series does not converge absolutely.

    ### Exercise 3

    **Determine whether the given series converges absolutely, converges conditionally, or diverges: $\sum\limits_{k=2}^{\infty} \frac{(-1)^k}{\ln{k}}$**.

    Solution

    1. $\lim\limits_{k \to \infty} \frac{1}{\ln{k}}$ is $0$, thus the series converges simply;
    2. On $(1,\infty)$, $\ln{x}$ is bounded above by $x$ because $(x-\ln{x})' =1 - \frac{1}{x} > 0$ and $\ln{1} = 0 < 1$; since $\sum \frac{1}{k}$ does not converge and $\frac{1}{k} < \frac{1}{\ln{k}}$ for all $k \ge 2$, $\sum \frac{1}{\ln{k}}$ does not converge, i.e. original series does not converge absolutely.

    ### Exercise 5

    **Determine whether the given series converges absolutely, converges conditionally, or diverges: $\sum\limits_{k=1}^{\infty}\frac{(-1)^{k-1}}{k^{2+(-1)^k}}$**.

    Solution

    1. Again, passing $k \to \infty$, $\lim\limits \frac{1}{k^{2+(-1)^k}}$ is $0$ thus the series converges simply;
    2. Take absolute value and the series becomes $\frac{1}{1} + \frac{1}{2^3} + \frac{1}{3} + \frac{1}{4^3} + \dots$, note that the odd terms constitute a series $1/1 + 1/3 + 1/5 + \dots = \sum \frac{1}{2k+1}$, which diverges, thus the original series does not converge absolutely.

    ### Exercise 6

    **Given an example of two convergent series $\sum a_k$, $\sum b_k$ such that the series $\sum a_kb_k$ diverges**.

    Solution

    Take $\sum a_k = \sum b_k = \sum \frac{(-1)^k}{k^{0.1}}$, the two series both converges (simply) since $k^{0.1} \to \infty$, but $\sum a_kb_k$ cancels the alternating term thus becomes $\sum \frac{1}{k^{0.2}}$ diverges as $0.2 < 1$.

    ### Exercise 8

    **Approximate the sum of the alternating harmonic series $1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\dots+(-1)^{n-1}\frac{1}{n}+\dots$ to within $.01$ by computing an appropriate partial sum**.

    Solution

    We know that for such alternating sums, $| s - s_n | \le a_{n+1}$, thus we want $| a_{n+1} | \le .01$, i.e. $| a_{n+1} | = \frac{1}{n+1} \le .01 \implies n\ge 99$, computing the sum $\sum\limits_{k=1}^{99}(-1)^{k-1}\frac{1}{k}$ gives $\approx .6982$ (notice that $99$ is just an upper bound for the smallest $n$, for this particular problem, summing from $1$ to $50$ is already enough).

    ## Section 6.4

    ### Exercise 1

    **Prove that the function $f(x) = \sum\limits_{k=1}^{\infty}\frac{x^k}{k^2}$ is continuous on the interval $[-1,1]$**.

    Proof

    For each $k$, $\frac{x^k}{k^2}$ continuous on $[-1,1]$ because it is a product of $k$- $x$'s and a constant, namely $1/k^2$. We want to show uniform convergence: notice that for $| x | \le 1$, we have $| x^k | \le 1$ and $|\frac{x^k}{k^2}| \le \frac{1}{k^2}$, take $M_k = \frac{1}{k^2}$ (whom we know that $\sum 1/k^2$ converges) then by Weierstrass M-test we have that the series of function converges uniformly to $f$.

    ### Exercise 2

    **Prove that the function $f(x) = \sum\limits_{k=1}^{\infty}\frac{\sin(kx)}{2^k}$ is continuous on the entire real line**.

    Proof

    The idea is the same: first, each $\frac{\sin(kx)}{2^k}$ is continuous because it is product of constant and sine function, which is continuous on the whole line. Now $\sin(kx)$ is always bounded by $1$, and we have $| \frac{\sin(kx)}{2^k} | \le \frac{1}{2^k}$, take $M_k = \frac{1}{2^k}$ and notice that it is a convergent geometric series, thus by Weierstrass M-test, $f(x) = \sum\limits_{k=1}^{\infty}\frac{\sin(kx)}{2^k}$ converges uniformly and we have $f$ is continuous.

    ### Exercise 5

    **Find the radius of convergence of the indicated power series: $\sum\limits_{k=0}^{\infty} \frac{(-1)^{k-1}}{k+1}(x+2)^k$**.

    Solution

    $\frac{1}{R} = \limsup{| \frac{(-1)^{k-1}}{k+1} |^{1/k}} = \lim\limits_{k \to \infty}\sqrt[k]{\frac{1}{k+1}} = 1$, thus the radius of convergence is $1$.

    ### Exercise 7

    **Find the radius of convergence of the indicated power series: $\sum\limits_{k=0}^{\infty}k!(x-5)^k$**.

    Solution

    $\frac{1}{R} = \limsup{| k! |^{1/k}} = \lim\limits{\sqrt[k]{k!}}$. Think of that (for simplicity say $k$ even, but it does not really matter when sending it to infinity) $k! = 1\cdot 2 \cdot 3 \cdot \dots \cdot k > (\frac{k}{2}+1) \cdot (\frac{k}{2}+2) \cdot \dots \cdot k > (\frac{k}{2}+1)^{k/2}$, in words, because half of the terms are larger than $k/2$. We thus have $\lim\limits{\sqrt[k]{k!}} > \lim\limits{\sqrt[k]{(k/2 + 1)^{k/2}}} = \infty$, we have $1/R = \infty \implies R = 0$.

    ### Exercise 9

    **Beginning with the geometric series which converges to $\frac{1}{1-x}$ on $(-1,1)$, find power series which converge to $\frac{1}{1+x^2}$ and to $\arctan{x}$ on this same interval**.

    Solution

    For start we have $\frac{1}{1-x} = \sum\limits_{n=0}^{\infty}x^n = 1+x+x^2+x^3+\dots$. Notice that $x \in (-1,1) \implies -x^2 \in (-1,0]$ so we can take a substitution: $\frac{1}{1+x^2} = \sum\limits_{n=0}^{\infty}(-x^2)^n = 1-x^2+x^4-x^6+\dots$. The radius of convergence of this power series is clearly $1$, because the coefficients $c_k$ is of the form $-1^k$, denote $f(x) = \frac{1}{1+x^2} = \sum\limits_{n=0}^{\infty}(-x^2)^n = \sum\limits_{n=0}^{\infty}(-1)^nx^{2n}$, we have that $\int_0^x f(x)dx = \arctan{x} = \sum\limits_{n=0}^{\infty}\frac{(-1)^n}{2n+1}x^{2n+1} = x-\frac{x^3}{3}+\frac{x^5}{5}-\dots$ on $(-1,1)$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 5""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 7.1

    ### Exercise 7

    **For a norm on a vector space $X$ define by an inner product, prove that the parallelogram law: $\| x+y \|^2 + \| xy\|^2 = 2\| x\|^2 + 2 \| y \|^2$ holds for all $x, y \in X$**.

    Proof

    $\| x+y \|^2 + \| xy\|^2$ $\overset{\text{def}}{=} (x+y) \cdot (x+y) + (x-y) \cdot (x-y)$ expand it by 7.1.5 (using the distributivity and other properties of inner product) we have $= x\cdot x + 2x\cdot y + y \cdot y + x\cdot x - 2x\cdot y + y \cdot y = 2x\cdot x + 2y \cdot y$ is exactly the right hand side of the original equation.

    ### Exercise 8

    **Prove that $\| \cdot \|_{\infty}$ is a norm on $\mathbb{R}^d$**.

    Proof

    We check the three axioms:

    1. For any $x, y \in \mathbb{R}^d$, $\| x \|_{\infty} + \| y \|_{\infty}$ $= \max{| x_i |} + \max{| y_i |}$ $= | x_I | + | y_J |$ for some $i,j$. We reduce the problem to the absolute value (dimension $1$ case), and we know that for any $x_i, y_j$ we have $| x_i + y_j | \le | x_i | + | y_j |$, thus $| x_I | + | y_J | \ge | (x+y)_K | = \| x+y \|_{\infty}$;
    2. $\| ax \|_{\infty} = \max{| ax_i |} = a\max{| x_i |} = a \| x \|_{\infty}$;
    3. If $\| x \|_{\infty} = 0$ then $\max{| x_i |} = 0$, implies that $0 \ge | x_i |$ for all $i$. Since $| x_i | \ge 0$ for any $i$ by the property of the absolute value, we have that $x_i = 0$ for all $i$, i.e. $x = 0$.

    ### Exercise 10

    **Prove that the space $C(I)$ is a vector space**.

    Proof

    First recall that sum of two continuous functions is continuous; (point-wise) product of two continuous functions is continuous; constant map is continuous.

    Also that two functions are said to be the same if they have the same domain and codomain, and the value-assignments are the same.

    In fact, all the axioms are pretty much directly inherited from the fact that $\mathbb{R}^d$ itself is a vector space:

    1. $(f+g)+h = f+(g+h)$ is inherited from $\mathbb{R}^d$: for each $i \in I$, $(f+g)+h$ assign $i$ to $(f(i) + g(i)) + h(i) \in \mathbb{R}^d$, since $\mathbb{R}^d$ is a vector space, $(f(i) + g(i)) + h(i) = f(i) + (g(i) + h(i))$, so the term-wise assignments are same, the domain is always $I$, and sum of continuous function is continuous function, thus $(f+g)+h = f+(g+h)$;
    2. $f+g = g+f$ same by above;
    3. $(0+f) = f$ same by above;
    4. $0f = 0$ and $1f = f$, they are inherited from the properties of multiplication in $\mathbb{R}^d$;
    5. $a(bf) = (ab)f$ same by above;
    6. $(a+b)f = af+bf$: $(a+b)f$ assign each $i \in I$ to $(a+b)f(i) = af(i) + bf(i)$ because $f(i) \in \mathbb{R}^d$ is a vector space;
    7. $a(f+g) = af+ag$ similar by above.

    ### Exercise 11

    **Prove that the sup norm is really a norm on $C(I)$**.

    Proof

    We check the three axioms:

    1. $\| f \|_{\infty} + \| g \|_{\infty}$ $\overset{\text{def}}{=} \sup\limits{| f(x) |} + \sup\limits{| g(x) |}$, again we reduced the problem to $\mathbb{R}$ and we know that this is $\ge \sup\limits{| (f+g)(x) |}$ $= \| f+g \|_{\infty}$;
    2. $\| af \|_{\infty} = \sup\limits{| af(x) |} = a\sup\limits{| f(x) |} = a \| f \|_{\infty}$;
    3. If $\| f \|_{\infty} = 0$ then $\sup\limits{| f(x) |} = 0$ implies $| f(x) |$ is bounded above by $0$, i.e. $| f(x) | \le 0$, but it is also greater than or equal to $0$ because of the absolute value, thus $| f(x) | \equiv 0 \implies f(x) \equiv 0$, meaning $f = 0$.

    ### Exercise 12

    **Prove that if $\lbrace x_k \rbrace$ and $\lbrace y_k \rbrace$ are sequences of real numbers such that $\sum\limits_{k=1}^{\infty}x_k^2 < \infty$ and $\sum\limits_{k=1}^{\infty}y_k^2 < \infty$ then $\sum\limits_{k = 1}^{\infty}| x_ky_k | < \infty$**.

    Proof

    For each $k$ we have $0 \le (x_k - y_k)^2 = x_k^2 + y_k^2 - 2x_ky_k$ which implies $x_ky_k \le x_k^2 + y_k^2$, so does $| x_ky_k | \le x_k^2 + y_k^2$. If $\sum x_k^2$ and $\sum y_k^2$ are bounded, their term-wise sum $\sum x_k^2+y_k^2$ is also bounded, thus $\sum | x_ky_k |$ is bounded by above argument. Moreover, this sequence is naturally non-decreasing, thus it is convergent (being bounded and monotone), thus we write $\sum | x_ky_k | < \infty$.

    ### Exercise 13

    **Find a non-zero vector in $\mathbb{R}^3$ which is orthogonal to both $(1,0,2)$ and $(3,-1,1)$**.

    Solution

    We want a $(a,b,c)$ such that $a+2c = 0$ and $3a-b+c = 0$. The solution can be pretty arbitrary, for example, take $a = 2$ and $c = -1$ so that the first equation is satisfied, then solve for $b = 5$, and the result $(2,5,-1)$ is orthogonal to both vectors.

    ## Section 7.2

    ### Exercise 5

    **Determine whether or not the sequence converges and find its limit if it does converge: $x_n = (\ln{n+1} - \ln{n}, \sin(1/n))$**.

    Solution

    Rewrite $x_n = (\ln{(\frac{1}{n}+1)}, \sin(1/n))$, sending $n \to \infty$ we have $\ln{(\frac{1}{n}+1)} \to \ln{1} = 0$ and $\sin(1/n) \to 0$ component-wise, combine them together we have $x_n \to (0,0)$.

    ### Exercise 9

    **If $x_n = (\sin(n),\cos(n),1+(-1)^n)$, does the sequence $\lbrace x_n \rbrace \in \mathbb{R}^3$ have a convergent subsequence**?

    Solution

    Yes, because sine, cosine and $1\pm 1$ are all bounded.

    To actually find such a sequence, notice that $n$ is rational but $\pi$ is not, thus $\sin(n) \ne \sin(0) = 0$ and $\cos(n) \ne \cos(0) = 1$ for any $n > 0$. Start with $n_0 = 0$ (or just start with $n_1$, it does not really matter), now:

    Let $n_1$ be an integer greater than $n_0$ with the property that $| \sin(n_1) | < 1/1$ and $| \cos(n_1) -1 | < 1/1$;

    Let $n_2$ be an integer greater than $n_1$ with the property that $| \sin(n_2) | < 1/2$ and $| \cos(n_2) -1 | < 1/2$;

    Continue this we find a sequence $n_i$ such that $x_{n_i}$ with limit $(\sin(0), \cos(0),2)$.

    ### Exercise 12

    **If for $x,y \in \mathbb{R}$, we set $\delta(x,y) =0$ if $x = y$ and $\delta(x,y) = 1$ if $x \ne y$, prove that the result is a metric on $\mathbb{R}$**.

    Proof

    We check by axioms:

    1. If $x = y$ then $\delta(x,y) = 0 = \delta(y,x)$, if $x\ne y$ then $\delta(x,y) = 1 = \delta(y,x)$, either case the equality holds;
    2. Axiom $2$ is true by assumption;
    3. If $x = z$ then $0 = \delta(x,z) \le \delta(x,y) + \delta(y,z)$ no matter if $x = y$ or not, $y = z$ or not; if $x \ne z$ then $1 = \delta(x,z)$, if $y = x$ then $\delta(x,y) + \delta(y,z) = 0+1 = 1$, if $y \ne x$ but $y = z$ (or equals $x$ but not $z$) then $\delta(x,y) + \delta(y,z) = 1+0 = 1$, if $y \ne x$ and $y \ne z$ then $\delta(x,y) + \delta(y,z) = 1+1 = 2$, so either case the inequality holds.

    ### Exercise 13

    **What are the convergent sequences in the metric space described in the previous exercise**?

    Solution

    They must be the sequences that are 'eventually constant', i.e. $x_n = c$ for all $n > N$ (in this case the limit is clearly $c$). Otherwise any potential limit $x$ is not equal to, thus has distance $1$ with, infinitely many $x_n$'s, thus is not the limit for $x_n$.

    ### Exercise 14

    **Let $a,b \in \mathbb{R}^2$ and let $X$ be the set of all smooth parameterized curves joining $a$ to $b$ in $\mathbb{R}^2$ with parameter interval $[0,1]$. That is, $X$ is the set of all continuously differentiable functions $\gamma:[0,1] \to \mathbb{R}^2$, with $\gamma(0) = a$ and $\gamma(1) = b$. Show that is $\delta(\gamma_1,\gamma_2) = \sup\limits{\lbrace \| \gamma_1(t)-\gamma_2(t) \|: t \in [0,1] \rbrace}$ then $\delta$ is a metric on $X$**.

    Proof

    We check the three axioms:

    1. Use the fact that $\| x - y \| = \sqrt{\sum\limits(x-y)_i^2} = \sqrt{(y-x)_i^2} = \| y - x \|$, we can see that by assumption $\delta(\gamma_1,\gamma_2) = \delta(\gamma_2, \gamma_1)$;
    2. If $\gamma_1 = \gamma_2$ then the supreme of the normal is clearly $0$, thus $\delta(\gamma_1, \gamma_2) = 0$; on the other hand, if $\delta(\gamma_1,\gamma_2) = \sup\limits{\lbrace \| \gamma_1(t)-\gamma_2(t) \|: t \in [0,1] \rbrace} = 0$ then $\| \gamma_1(t)-\gamma_2(t) \|$ is bounded above by $0$, it is naturally bounded below by $0$, thus $\gamma_1 - \gamma_2 \equiv 0$ implies that they are identical;
    3. Use the fact that $\| \cdot \|$ is a norm in $\mathbb{R}^2$, we have $\| \gamma_1(t)-\gamma_2(t) \| \le \| \gamma_1(t)-\gamma_3(t) \| + \| \gamma_3(t)-\gamma_2(t) \|$ so that we have $\sup\limits(\| \gamma_1(t)-\gamma_2(t) \|)$ $\le \sup\limits(\| \gamma_1(t)-\gamma_3(t) \| + \| \gamma_3(t)-\gamma_2(t) \|)$ $\le \sup\limits(\| \gamma_1(t)-\gamma_3(t) \|) + \sup\limits(\| \gamma_3(t)-\gamma_2(t) \|)$. The triangle inequality follows.

    ### Exercise 15

    **Show that the metric space of the previous exercise is not complete**.

    Proof

    Construct a sequence of functions as follow:

    Let all $f_i$ be defined on $[0,1]$.

    1. Starting with $f_1$, let it be the smooth function with the assignment $f_1(1/2)=(1/2,0)$. Join $f_1(0)$ and $f_1(1/2)$ by the well-known smooth function $r(t) = e^{-1/t^2}$. The curve we actually use will be smooth and non-increasing;
    2. For $f_2$, let it be the smooth function with the assignment $f_2(1/2) = (1/2, 1/2)$ and $f_2(2/3) = (2/3, 0)$. Join both $f_2(0) \leftrightarrow f_2(1/2)$, also $f_2(1/2) \leftrightarrow f_2(2/3)$ by the smooth curve;
    3. For $f_3$, let it be the smooth function with the assignment $f_3(1/2) = (1/2, 1/2)$, $f_3(2/3) = (2/3, 1/3)$ and $f_3(3/4) = (3/4, 0)$. Join both $f_3(0) \leftrightarrow f_3(1/2)$, $f_3(1/2) \leftrightarrow f_3(2/3)$ and $f_3(2/3) \leftrightarrow f_3(3/4)$ by the smooth curve. Use the same curve joining $f_2(0) \leftrightarrow f_2(1/2)$ to join $f_3(0) \leftrightarrow f_3(1/2)$.

    Proceed like above and we have a sequence of smooth function that all have $f_i(0)=(0,1)$ and are 'eventually zero'.

    This sequence is Cauchy but not convergent when equip with the sup norm:

    1. Cauchy: $\delta(f_i, f_j) = \sup\limits{\lbrace \| f_i(t) - f_j(t) \| \rbrace}$, observe from the graph that the distance between $f_i$ and $f_j$ is at most $1/i$ (for example, difference between $f_2$ and $f_3$ is bounded above by $1/2$, because the first half and last $1/4$ of the two curves are the same, and this sup distance can be only attained somewhere in the interval $[1/2,3/4]$). Since $1/i$ goes to $0$ when we send $i \to \infty$, the sequence is Cauchy;
    2. Not convergent: suppose it is convergent to $f$, since all $f_i$ are eventually zero, $f$ must also be eventually $0$, i.e. exists $n \in [0,1]$ such that $f(x)=0, \forall x \in [n,1]$. Choose $M$ such that $1-1/M > n$, and consider $\varepsilon < 1/M$: then for any $m>M$, $\| f_m(1-1/M) - f(1-1/M) \|$ $= \| (1-1/M, 1/M) - (1-1/M, 0) \|$ $= 1/M$, but then $\delta(f, f_m) \ge 1/M > \varepsilon$, meaning that $f$ is not the limit after all.

    ### Exercise 17

    **Imagine a large building with many rooms, let $X$ be the set of rooms in this building and $\delta(x,y)$ is the length of the shortest path along the hallways and stairways of the building that leads from room $x$ to room $y$. Show that $\delta$ is a metric on $X$**.

    Proof

    We check the three axioms:

    1. The shortest path from $x$ to $y$ and $y$ to $x$ naturally should be the same;
    2. The shortest path from a room to the same room is $0$, and if the path is $0$ (i.e. we do not move), then we clearly stay in the same room;
    3. Suppose not (i.e. the shortest path from $x$ to $z$ is longer than from $x$ to $y$ plus from $y$ to $z$), then we go first from $x$ to $y$ then from $y$ to $z$ gives us a shorter path from $x$ to $z$, which contradict the fact that we are given a 'shortest' path from $x$ to $z$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 6""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Exercise 5.4.9

    **For which values of $p>0$ does the improper integral $\int_{0}^{1}\frac{1}{x^p}dx$ converge**?

    Solution

    By definition in the book we have the improper integral $\int_{0}^{1}\frac{1}{x^p}dx = \lim\limits_{a \to 0^+}\int_a^1 \frac{1}{x^p}dx$ (if the limit exists).

    By FTC we have: for $p \ne 1$, $(\frac{x^{1-p}}{1-p})' = \frac{1}{x^p}$ thus $\lim\limits_{a \to 0^+}\int_a^1 \frac{1}{x^p}dx=\lim\limits_{a \to 0^+}(\frac{1^{1-p}}{1-p} - \frac{a^{1-p}}{1-p})$, this limit exists if $p < 1$ (in this case $a^{1-p} \to 0$) and it diverges for $p> 1$ because $a^{1-p} = \frac{1}{a^{p-1}} \to \infty$ when passing $a \to 0^+$ in this case.

    For $p = 1$, $(\ln{x})' = \frac{1}{x}$, and we know that the improper integral does not converge because $\ln{x} \to -\infty$ as $x \to 0^+$.

    So in conclusion, the improper integral converge for $0<p<1$.

    ### Another Problem

    **Find $\lim\limits_{n \to \infty}\sum\limits_{k=1}^n(\frac{1}{\sqrt{n}+\frac{k}{\sqrt{n}}})^2$**.

    Solution

    First a little bit rewrite:

    $\lim\limits_{n \to \infty}\sum\limits_{k=1}^n(\frac{1}{\sqrt{n}+\frac{k}{\sqrt{n}}})^2$ $=\lim\limits_{n \to \infty}\sum\limits_{k=1}^n\frac{1}{n+\frac{k^2}{n}+2k}$ $=\lim\limits_{n \to \infty}\sum\limits_{k=1}^n\frac{1}{n}\frac{1}{1+\frac{k^2}{n^2}+\frac{2k}{n}}$ $=\lim\limits_{n \to \infty}\sum\limits_{k=1}^{n}\frac{1}{n}\frac{1}{(1+\frac{k}{n})^2}$.

    Recognize this as the Riemann sum $= \int_0^1 \frac{1}{(1+x)^2}dx$ ($\frac{1}{(1+x)^2}$ is continuous and bounded on $[0,1]$), since $(-\frac{1}{1+x})' = \frac{1}{(1+x)^2}$, we have the integral $= -\frac{1}{1+1} + \frac{1}{1+0} = \frac{1}{2}$.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 7""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 7.3

    ### Exercise 4

    **Find the interior, closure, and boundary for the set $\lbrace (x,y) \in \mathbb{R}^2 | \| (x,y) \| < 1 \rbrace \cup \lbrace (x,y) \in \mathbb{R}^2 | y = 0, -2 <x < 2 \rbrace$**.

    Solution

    1. Interior: for any $(x,y) \in \lbrace (x,y) \in \mathbb{R}^2 | \| (x,y) \| < 1 \rbrace$, choose small enough $\varepsilon$ and we have $B((x,y),\varepsilon) \subseteq \lbrace (x,y) \in \mathbb{R}^2 | \| (x,y) \| < 1 \rbrace$ thus in the union. Thus $(x,y)$ is in the interior. For any $(x,y) \in \lbrace (x,y) \in \mathbb{R}^2 | y = 0, -2 <x < 2 \rbrace - \lbrace (x,y) \in \mathbb{R}^2 | \| (x,y) \| < 1 \rbrace$ $= \lbrace (x,y) \in \mathbb{R}^2 | y =0, x \in (-2,-1] \cup [1,2) \rbrace$, for any $\varepsilon > 0$, the ball $B((x,y), \varepsilon)$ is not contained in the original union because the point $(x,\varepsilon/2)$ is not in the union, thus $(x,y)$ not in the interior.
    	So in conclusion, the interior contains all $(x,y) \in \lbrace (x,y) \in \mathbb{R}^2 | \| (x,y) \| < 1 \rbrace$;
    2. Use the result below (exercise 9) the closure is the closed unit disk union with the line segment $[-2,2]$ on $x$-axis;
    3. The boundary is their difference, that is the unit circle union with the line segments $[-2,-1]$ and $[1, 2]$.

    ### Exercise 9

    **If $A$ and $B$ are subsets of $\mathbb{R}^d$, show that $\overline{A \cup B} = \overline{A} \cup \overline{B}$. Is the analogous statement true for $A \cap B$**?

    Proof

    For any $x \in \overline{A \cup B}$, every open set $U$ containing $x$ intersects $A \cup B$, thus $U$ intersect $A$ or $B$. Suppose $x \notin \overline{A} \cup \overline{B}$, then $x \notin \overline{A}$ and $x \notin \overline{B}$, then $\exists U_A$ containing $x$ such that $U_A \cap A = \varnothing$ and $\exists U_B$ containing $x$ such that $U_B \cap B = \varnothing$. Since $x \in U_A$ and $x \in U_B$ thus $U_A \cap U_B \ne \varnothing$, take $U' = U_A \cap U_B$, then $x \in U'$ and $U' \cap A = \varnothing, U' \cap B = \varnothing$, which is a contradiction;

    Now suppose $x \in \overline{A} \cup \overline{B}$, if $x \in \overline{A}$ then $\forall U$ open set containing $x$, $\exists x' \in U$ and $x' \in A$, thus $x' \in A \cup B$ thus $x' \in U \cap (A \cup B)$ thus $x \in \overline{A \cup B}$; similar if $x \in \overline{B}$.

    Thus inclusion holds either way and thus equality holds.

    The analogous statement is generally not true, for example, $A = (0,1)$ and $B = (1,2)$ so that $A \cap B = \varnothing$ thus $\overline{A \cap B} = \varnothing$, but the intersection of their closure is $\lbrace 1 \rbrace$ (yet we do have the $\subseteq$ inclusion).

    ### Exercise 10

    **If $A$ and $B$ are subsets of $\mathbb{R}^d$, prove that $(A \cap B)^o = A^o \cap B^o$. Is the analogous statement true for $A \cup B$**?

    Proof

    For any $x \in (A \cap B)^o$, there exists $U$ of $x$ such that $U \subseteq A \cap B$ thus $U \subseteq A$ and $U \subseteq B$. Meaning that $x$ is in the interior of $A$ and interior of $B$ thus in the intersection of interiors;

    Now suppose $x \in A^o \cap B^o$, then $x \in A^o \implies \exists U_A(x) \subseteq A$ and $x \in B^o \implies \exists U_B(x) \subseteq B$. Now $U_A \cap U_B$ contains $x$ thus not empty, is a neighborhood of $x$, is open (finite intersection of open sets is open), and is inside $A \cap B$, thus $x \in (A \cap B)^o$.

    The analogous statement is generally not true, with a similar example, $A = [0,1]$ and $B =[1,2]$, the the interior of union is $(0,2)$ but the union of interior is $(0,1) \cup (1,2)$.

    ### Exercise 11

    **Let $\lbrace x_n \rbrace$ be a convergent sequence in $\mathbb{R}^d$ with limit $x$. Set $A = \lbrace x_1, \dots \rbrace \cup \lbrace x \rbrace$, show that $A$ is a closed set**.

    Proof

    We want to prove that the closure of $A$ is itself, in other word, any $y \notin A$ is not in its closure.

    Suppose not, and we have a $y \notin A$ but $y \in \overline{A}$. The latter means for any $\varepsilon$, $B(y,\varepsilon)$ contains some elements of $A$. If $B(y, \varepsilon)$ contains only finitely many points in $A$, then take the minimal of the distance from these points to $y$ as the new $\varepsilon$, we find a neighborhood of $y$ that does not contain any point in $A$ thus $y$ is not in the closure. Thus $B(y, \varepsilon)$ must contain infinitely many points in $A$, thus infinitely many points in $\lbrace x_1, \dots \rbrace$. But then since it works for all $\varepsilon$, it means $y$ is the limit of $\lbrace x_1, \dots \rbrace$, namely $x$, thus $y$ is in $A$, gives us a contradiction.

    ### Exercise 14

    **Find the interior and closure of the set $\mathbb{Q}$ in $\mathbb{R}$**.

    Solution

    The closure of course contains $\mathbb{Q}$, namely rational numbers, itself. For any irrational number, we know that any neighborhood of irrationals contains some rational numbers, thus all irrational numbers are also in the closure, thus $\overline{\mathbb{Q}} = \mathbb{R}$.

    For any $q \in \mathbb{Q}$, a rational number, we know also that any neighborhood of rationals contains come irrationals, in particular no neighborhood of $q$ is contained in $\mathbb{Q}$, thus $q$ not in the interior, thus the interior is the empty set.

    ### Exercise 15

    **If $E$ is a subset of $\mathbb{R}^d$, show that $(\overline{E})^c = (E^c)^o$**.

    Proof

    Suppose $x \in (\overline{E})^c$, that is $x \notin \overline{E}$, meaning that there exists $U$ neighborhood of $x$ that does not intersect with $E$, thus this $U$ is contained in $E^c$, thus $x$ is in the interior of $E^c$.

    This argument goes 'if and only if' form thus we have both inclusions.

    ## Section 7.4

    ### Exercise 5

    **Prove that if $K$ is a compact subset of $\mathbb{R}^d$ any $y$ is a point of $\mathbb{R}^d$ which is not in $K$, then there is a closest point to $y$ in $K$. That is, there is an $x_0 \in K$ such that $\| x_0 - y \| \le \| xy \|$ for all $x \in K$**.

    Proof

    Consider the function $f: K \to \mathbb{R}, k \mapsto \| k - y \|$. This is a composition of continuous functions thus continuous. More over, $K \subseteq \mathbb{R}^d$ is compact thus closed and bounded, so that $f$, a continuous function on closed and bounded set in $\mathbb{R}^d$ attains its minimum, take that $k$ and that is the $x_0$ we want.

    ### Exercise 7

    **Prove that if $K_1, K_2$ is a disjoint pair of compact sets, then there exists a disjoint pair of open sets $V_1, V_2$ such that $K_1 \subseteq V_1$ and $K_2 \subseteq V_2$**.

    Proof

    By the above exercise we know that for each point $k_i^1$ in $K_1$ we can always find its minimal distance to $K_2$, denote it $\varepsilon_{k_i^1}$, similarly, for each point $k_j^2 \in K_2$ we can find its minimal distance to $K_1$, denote it $\varepsilon_{k_j^2}$. Now consider the union $V_1 = \bigcup\limits_i B(k_i^1, \frac{1}{3}\varepsilon_{k_i^1})$ over all $k_i^1 \in K_1$ and $V_2 = \bigcup\limits_j B(k_j^2, \frac{1}{3}\varepsilon_{k_j^2})$ over all $k_j^2 \in K_2$. $V_1$ and $V_2$ are both unions of open sets thus open. And they are disjoint thus they are the sets we are looking for:

    Suppose they are not disjoint, then there exists $k$ such that for some $i, j$, $d(k_i^1, k_j^2) \le \frac{1}{3}\varepsilon_{k_j^2} + \frac{1}{3}\varepsilon_{k_i^1}$, WLOG say $\varepsilon_{k_i^1}$ is larger than $\varepsilon_{k_j^2}$, then $d(k_i^1, k_j^2) \le \frac{2}{3}\varepsilon_{k_i^1} < \varepsilon_{k_i^1}$, but that means the distance from $K_2$ to $k_1$ is less than the minimal distance we had before, gives us a contradiction.


    ### Exercise 8

    **Prove that a set $K \subseteq \mathbb{R}^d$ is compact if and only if every sequence in $K$ has a subsequence which converges to an element of $K$**.

    Proof

    The set $K$ is by assumption bounded, thus every sequence in it is clearly also bounded, thus has a convergent subsequence. Now use that $K$ is closed, thus contains every limit points, thus the convergent subsequence described just now converges to an element within $K$.

    ### Exercise 9

    **Show that it is true that the union of any finite collection of compact subsets of $\mathbb{R}^d$ is compact, but it is not true that the union of an infinite collection of compact subsets is necessarily compact**.

    Proof

    Let $\cup U_i$ be an arbitrary open cover for the finite union $\bigcup\limits_{i=1}^{n} K_i$ of compact sets. Since it covers the union of course it covers each $K_i$. Since each $K_i$ is compact, $\cup U_i$ admits a finite cover $\bigcup\limits_{j=1}^{n_{K_i}} U^{K_i}_j$ to cover $K_i$. Thus $\bigcup\limits_{i = 1}^n \bigcup\limits_{j=1}^{n_{K_i}} U^{K_i}_j$ can be used to cover $\bigcup\limits_{i=1}^{n} K_i$. It is a finite sub-cover of $\cup U_i$ (summation of finitely many finite terms is finite), and since $\cup U_i$ is arbitrary, $\bigcup\limits_{i=1}^n K_i$ is compact.

    For infinite collection, consider the union $\bigcup\limits_i [i,i+1] = \dots \cup [-2,-1] \cup [-1,0] \cup [0,1] \cup \dots$, each $[i,i+1]$ is compact but their union, which is the entire $\mathbb{R}$, is not.

    ### Exercise 10

    **Prove that if $A$ and $B$ are compact subsets of a metric space, then $A \cup B$ and $A \cap B$ are also compact**.

    Proof

    By above, $A \cup B$ is a union of finitely many compact sets thus compact (we did not use the fact we were working in $\mathbb{R}^d$ in above argument).

    By the book any compact subset of a metric space is closed (the book proved for $\mathbb{R}^d$, but only used the fact we are in a metric space), thus $A$ and $B$ are closed, thus their intersection $A \cap B$ is closed, and thus $A \cap B$ is a closed subset of compact set $A$ thus compact.

    ### Exercise 13

    **Prove that a compact metric space is complete (every Cauchy sequence converges)**.

    Proof

    If we are allowed to use other exercise's result (no. 11 in particular) the result is pretty straight-forward: every compact metric space is sequentially compact, a Cauchy sequence is of course a sequence, thus has convergent subsequence, thus converges:

    Suppose $(x_n)$ is a Cauchy sequence with convergent subsequence $(x_{n_k}) \to x$, then for any $\varepsilon > 0$, choose $N$ large enough such that $d(x,x_{n_k}) \le \varepsilon/3$ (this is from convergence of subsequence) and $d(x_n, x_{n_k}) \le \varepsilon/3$ (from Cauchy), for $n_k > n > N$, and thus $d(x, x_n)$ is less than $\varepsilon$ by triangle inequality.

    Proof of 11.

    Suppose $(X,d)$ is a compact metric space that is not sequentially compact, then there is a sequence $(a_i)$ in $X$ has no convergent subsequence. Thus $(a_i)$ contains infinitely many distinct points (otherwise choose those infinitely many non-distinct points and we have a constant subsequence which is convergent).

    Now let $x \in X$ be an arbitrary point, if for any $\varepsilon$ the ball $B(x, \varepsilon)$ contains a point from $(a_i)$ (except for $x$ itself), then by choosing $\varepsilon = 1, 1/2, 1/3, \dots$ and pick point in $(a_i)$ in the ball we have a convergent subsequence of $(a_i)$, which is by assumption does not exists, thus we have the negation: there is some $\varepsilon_x$ (for the particular $x$) such that $B(x, \varepsilon_x)$ does not contain any $(a_i)$ other than possibly $x$ itself.

    Since $x$ is arbitrary, consider the union $\bigcup\limits_x B(x, \varepsilon_x)$, this is an open cover for compact $X$, thus admit a finite sub-cover. But then each $B(x, \varepsilon_x)$ contains at most one point in $(a_i)$, thus a finite union of them contains only finitely many $a_i$, that is, $(a_i)$ contains only finitely many distinct point, we have a contradiction.

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Spring Semester Homework 8""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 7.5

    ### Exercise 4

    **Tell whether or not the set $A$ is connected, if $A$ is not connected, describe its connected components: $A = \lbrace (x,y) \in \mathbb{R}^2 | 1< \| (x,y) \| <2 \rbrace \cup \lbrace (x,y) \in \mathbb{R}^2 | \| (x,y) \| <1 \rbrace$**.

    Solution

    The two sets in the description of $A$ are disjoint, non-empty, and open, so they themselves form a separation for $A$, thus $A$ is not connected, the connected components are exactly that two sets.

    ### Exercise 6

    **Prove that the union of a collection of connected subsets of $\mathbb{R}^d$ with a point in common is also connected**.

    Proof

    Let us call that point $p$, the collection of connected sets are $C_i$ indexed by $i$, and suppose in contrast that their union $\cup C_i$ is not connected. By definition that means $\cup C_i = U \cup V$ is a separation. By assumption $p \in \cup C_i$ so $p$ is either in $U$ or $V$. WLOG say $p \in U$. Now $C_1$ contains $p$, if $C_1$ has an point lie inside $V$, then by definition, $U\cap C_1,V \cap C_1$ form a separation for $C_1$, but that is impossible because it is connected, thus $C_1$ lies entirely in $U$. This works for all $i$. Thus $C_i$ lies entirely in $U$ for all $i$, meaning that $\cup C_i \subseteq U$ and $\cup C_i \cap V = \varnothing$, thus $U,V$ are not a separation anyway.

    ### Exercise 9

    **Prove that if $E$ is an open connected subset of $\mathbb{R}^d$, then each pair of points in $E$ can be connected by piece-wise linear path in $E$**.

    Proof

    Consider the relation on $E$ that $a \sim b$ if and only if they can be connected by piece-wise linear path. This is an equivalence relation:

    1. $a\sim a$ for any $a$, because a point is in some sense 'linear';
    2. If $a \sim b$ then $b \sim a$, use the same path;
    3. If $a \sim b$ and $b \sim c$, then connect the two path we have a piece wise linear path connecting $a$ and $c$ thus $a \sim c$.

    Now fix some $a \in E$, its equivalence class $\overline{a}$ is open: for any $p \in \overline{a} \subseteq E$, which means $p$ is in an open set in $\mathbb{R}^d$, thus we can find $B(p,\varepsilon) \subseteq E$. For any $q \in B(p,\varepsilon)$, simply draw a straight line between $p$ and $q$ and we have a (piece-wise) linear path between them, thus $B(p, \varepsilon) \subseteq \overline{a}$. Since that works for arbitrary $p$, it means $\overline{a}$ is open.

    The equivalence class is also closed: because equivalence classes form a partition for $E$, thus $E-\overline{a}$ is union of equivalence classes, in particular $E-\overline{a}$ is union of open sets thus open, thus $\overline{a}$ is closed.

    Since the only sets that are both open and closed in a connected set is the set itself and the empty set, it means we only have one non-trivial equivalence class $\overline{a}$, which means every point has a piece-wise linear path connecting to $a$, and thus each pair of points have a piece-wise linear path connecting them.

    ## Section 8.2

    ### Exercise 1

    **If $A = \lbrace (x,y) \in \mathbb{R}^2 | 0\le x \le 1, 0 \le y \le 1 \rbrace$, which of the following sets cannot be the image of the set $A$ under a continuous function $F: A \to \mathbb{R}^2$**?

    1. $\overline{B_2(0,0)}$;
    2. $B_1(0)$;
    3. $\lbrace (x,y) \in \mathbb{R}^2 | 0\le x \le 1, 0 \le y \rbrace$;
    4. $\overline{B_1(0,0)} \cup \overline{B_1(3,0)}$;
    5. $\lbrace (t,t) \in \mathbb{R}^2 | t \in \mathbb{R}, 0 \le t \le 1 \rbrace$.

    Solution

    1. It can be, for some function like $(x,y) \mapsto (\frac{x}{\sqrt{x^2+y^2}}, \frac{y}{\sqrt{x^2+y^2}})$;
    2. No, because the image of compact set must be compact (in particular, closed) under continuous map;
    3. No, because the image of compact set must be compact (in particular, bounded) under continuous map;
    4. No, because the image of connected set must be connected under continuous map;
    5. It can be, just use the projection map. But there is no continuous injection.

    ### Exercise 4

    **If $F:\mathbb{R}^p \to \mathbb{R}^q$ is continuous and $A$ is a bounded subset of $\mathbb{R}^p$, prove that $\overline{F(A)} = F(\overline{A})$. Is this necessarily true if $A$ is not bounded**?

    Proof

    1. The first inclusion: $\overline{F(A)} \subseteq F(\overline{A})$: because $F(\overline{A})$ clearly contains $F(A)$, and $F(\overline{A})$ is image of closed and bounded, i.e. compact set thus compact, thus closed. But $\overline{F(A)}$ is by definition the smallest closet set containing $F(A)$, thus it must be contained in $F(\overline{A})$;
    2. The other way around: consider $F^{-1}(\overline{F(A)})$, it is the preimage of a closed set under a continuous function, thus closed. By property of functions, it also contains $A$, thus it contains $\overline{A}$ following a similar argument as above, i.e. $F^{-1}(\overline{F(A)}) \supseteq \overline{A}$, but then $\overline{F(A)} \supseteq F(F^{-1}(\overline{F(A)})) \supseteq F(\overline{A})$.

    If we don't have boundedness then it may not true, for example, take $A = [0,\infty)$ and consider the function $F: x\mapsto \frac{1}{x^2+1}$, then $\overline{F(A)}=[0,1]$ but $F(\overline{A}) = (0,1]$.

    ### Exercise 5

    **The image of a compact set under a continuous function is compact, hence closed. Is the image of a closed set under a continuous function necessarily closed**?

    Solution

    No, just use the above example $f:\mathbb{R} \to \mathbb{R}, x \to \frac{1}{x^2+1}$, the image is $(0,1]$ is not closed (also not open).

    ### Exercise 7

    **Is the sphere $\lbrace (x,y,z) \in \mathbb{R}^3 | x^2+y^2+z^2 = 1 \rbrace$ connected? How do you know**?

    Solution

    In a very informal way: the (surface of) Earth is (approximately) such a sphere, and we can move freely from any place to any other place continuously (say we are taking an air jet…), thus such surface is path-connected thus connected.

    ## Section 9.1

    ### Exercise 8

    **If $p>0$, let $f$ be the function $f(x,y) = \begin{cases} \frac{x^2}{(x^2+y^2)^p},& (x,y) \ne (0,0)\\ 0,& (x,y) = (0,0) \end{cases}$. For which values of $p$ is $\frac{\partial f}{\partial x}$ continuous at $(0,0)$**?

    Solution

    Using the product rule we can calculate that $\frac{\partial f(x,y)}{\partial x} = \begin{cases} \frac{2x(x^2+y^2)-2px^3}{(x^2+y^2)^{p+1}},& (x,y) \ne (0,0)\\ 0,& (x,y) = (0,0) \end{cases}$. In order to make it continuous we basically require the power in the bottom be smaller, i.e. $0 < p < 1/2$.

    ### Exercise 9

    **If $f$ is the function $f(x,y) = \begin{cases} \frac{x^3y-xy^3}{x^2+y^2},& (x,y) \ne (0,0)\\ 0,& (x,y) = (0,0) \end{cases}$, show by direct calculation that $\frac{\partial^2 f}{\partial x \partial y}$ is not continuous at $(0,0)$, a similar calculation shows that $\frac{\partial^2 f}{\partial y \partial x}$ is not continuous at $(0,0)$**.

    Solution

    we may calculate that $\frac{\partial f(x,y)}{\partial y} = \begin{cases} \frac{x^3-3xy^2}{x^2+y^2}-\frac{(2x^3y^2-2xy^4)}{(x^2+y^2)^2},& (x,y) \ne (0,0)\\ 0,& (x,y) = (0,0) \end{cases}$. This is continuous. And then $\frac{\partial^2 f(x,y)}{\partial x \partial y} = \begin{cases} \frac{3x^2-3y^2}{x^2+y^2}-\frac{x^3-3xy^2}{(x^2+y^2)^2}-\frac{6x^2y^2-2y^4}{(x^2+y^2)^2}+\frac{8x^3y^3-8xy^5}{(x^2+y^2)^3},& (x,y) \ne (0,0)\\ 0,& (x,y) = (0,0) \end{cases}$, we can see from the power that it is not continuous at $(0,0)$.

    Also we may calculate that $\frac{\partial f(x,y)}{\partial x} = \begin{cases} \frac{3x^2y-y^3}{x^2+y^2}-\frac{2x^4y-2x^2y^3}{(x^2+y^2)^2},& (x,y) \ne (0,0)\\ 0,& (x,y) = (0,0) \end{cases}$. This is continuous. And then $\frac{\partial^2 f(x,y)}{\partial y \partial x} = \begin{cases} \frac{3x^2-3y^2}{x^2+y^2}-\frac{3x^2y-y^3}{(x^2+y^2)^2}-\frac{2x^4-6x^2y^2}{(x^2+y^2)^2}+\frac{8x^5y-8x^3y^3}{(x^2+y^2)^3},& (x,y) \ne (0,0)\\ 0,& (x,y) = (0,0) \end{cases}$, since the original function is kind of 'symmetric', those calculations are the same, just interchange the sign and $x,y$. We can also see from the power that it is not continuous at $(0,0)$.

    ## Section 9.2

    ### Exercise 7

    **Prove that if $f$ is a real valued function defined on an open interval containing $a$ and if $S$ is an affine function such that $f(a) = S(a)$ and $\lim\limits_{h \to 0}\frac{f(a+h) - S(a+h)}{h} = 0$, then $S(a+h) = f(a) + f'(a)h$**.

    Proof

    $S:\mathbb{R} \to \mathbb{R}$ is affine, so it has the form $S(a+h)$ $= S(a) + hC =$ $f(a)+hC$. The latter part $hC = L(h)$ is by definition linear. By assumption we have $0 = \lim\limits_{h \to 0}\frac{f(a+h) - S(a+h)}{h}$ $= \lim\limits_{h \to 0}\frac{f(a+h) - f(a) - L(h)}{h}$, domain is an open interval so every point is an interior point, thus by definition $f$ is differentiable at every $a$.

    That is to say $f'$ does exist, and by definition $f'(a) = \lim\limits_{h \to 0}\frac{f(a+h) - f(a)}{h}$, thus $\lim\limits_{h \to 0}(f(a) + f'(a)h)$ $= \lim\limits_{h \to 0}(f(a) + f(a+h) - f(a))$ $= \lim\limits_{h \to 0}f(a+h)$; on the other hand, by assumption $\lim\limits_{h \to 0}\frac{f(a+h) - S(a+h)}{h} = 0$ thus $\lim\limits_{h \to 0}(f(a+h) - S(a+h)) = 0$ thus $\lim\limits_{h \to 0}f(a+h) = \lim\limits_{h \to 0}S(a+h)$.

    So we have the equality when sending $h \to 0$, but $S(a+h) = f(a)+hC$ is affine, since by above $C = f'(a)$ when $h$ is small, it means $S(a+h) = f(a) + h f'(a)$ for all $h$.

    ### Exercise 10

    **Does the function defined by $f(x,y) = \begin{cases} \frac{x^3}{x^2+y^2},& (x,y) \ne (0,0)\\ 0,& (x,y) = (0,0) \end{cases}$ have first order partial derivative at every point of $\mathbb{R}^2$? Is this function differentiable at $(0,0)$**?

    Solution

    For points other than $0$ we can just calculate the partial derivative in a usual way. At zero: with respect to $x$, fix $y = 0$ the function near $0$ becomes $= x^3/x^2 = x$, thus $\frac{\partial f}{\partial x}(0,0) = \lim\limits_{h \to 0}\frac{f(h,0)-f(0,0)}{h} = \lim\limits \frac{h}{h} = 1$. With respect to $y$, fix $x = 0$ the function near $0$ becomes constant zero, so has partial derivative $0$.

    If it has differential, then by above $df(0) = (1,0)$. Now by definition, $f$ is differentiable if there is some linear $L$ (which would be $(1,0)$) and that $\lim\limits_{h \to 0}\frac{f(h_1,h_2)-f(0,0)-L(h_1,h_2)}{\| h \|} = 0$ (say $h = (h_1,h_2)$ here). We can calculate that $\lim\limits_{h \to 0}\frac{f(h_1,h_2)-f(0,0)-L(h_1,h_2)}{\| h \|}$ $= \lim\limits \frac{\frac{h_1^3}{h_1^2+h^2_2} - h_1}{\sqrt{h_1^2+h_2^2}} = \lim\limits \frac{-h_1h_2^2}{(h_1^2+h_2^2)^{3/2}}$, but this limit does not exist. Thus $f$ is not differentiable at $0$.

    ### Exercise 12

    **Prove that a function $F: \mathbb{R}^p \to \mathbb{R}^q$ is affine if and only if it is differentiable everywhere and its differential matrix is constant**.

    Proof

    Definition of affine function: $F$ is affine if $F(x) = b+L(x)$.

    If $F$ is affine, then $\lim\limits_{h \to 0}\frac{F(a+h)-F(a)-L(h)}{\| h \|}$ (for any $a$) would be constant zero if we just take the $L$ as in the definition of our affine function: $\frac{F(a+h)-F(a)-L(h)}{\| h \|} = \frac{b+L(a+h)-b-L(a)-L(h)}{\| h \|} = 0$ since $L$ is by definition linear. Now this $L$, which by assumption is independent from the choice of $a$, is our differential matrix, and thus it is constant.

    Conversely we have that $\lim\limits_{h \to 0}\frac{F(a+h)-F(a)-L(h)}{\| h \|} = 0$ for some linear $L$ for all $a$. Consider $G:\mathbb{R}^p \to \mathbb{R}^q$ given by $G(x) = F(x) - L(x)$, then we have that for any $a$, $\lim\limits_{h \to 0}\frac{G(a+h)-G(a)}{\| h \|}$ $=\lim\limits \frac{F(a+h)-L(a+h) - F(a) +L(a)}{\| h \|}$ $=\lim\limits_{h \to 0}\frac{F(a+h)-F(a)-L(h)}{\| h \|} = 0$, thus $G$ is differentiable everywhere with the differential matrix being constant zero.

    Now fix any two points $x, y \in \mathbb{R}^p$, the whole line from $x$ to $y$ is also inside $\mathbb{R}^p$. Let us consider a parametrization $r(t) = G(tx+(1-t)y)$, where $t \in [0,1]$. Since $G$ is differentiable everywhere and $tx+(1-t)y$ is differentiable (seeing $x,y$ as constant), we can use the Chain Rule to see $r'(t) = 0$ for any $t$ because $dG(\cdot) \equiv 0$ by above. Thus $r$ is a constant, taking $t = 0$ and $1$ we have that $G(x) = G(y)$. Since this works for arbitrary $x,y$, we conclude $G$ is a constant map, and then $F = G+L$ is by definition affine.

    """
    )
    return


if __name__ == "__main__":
    app.run()
