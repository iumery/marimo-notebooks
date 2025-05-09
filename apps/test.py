import marimo

__generated_with = "0.13.6"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Section 0.7

    ### Exercise 0

    **Recalling that $\begin{pmatrix} n \\ k \end{pmatrix} \overset{\text{def}}{=} \frac{n!}{k!(n - k)!}$, prove that for any integers $n \ge k \ge 1$ one has: $\begin{pmatrix} n + 1 \\ k \end{pmatrix} = \begin{pmatrix} n \\ k \end{pmatrix} + \begin{pmatrix} n \\ k-1 \end{pmatrix}$**.

    Proof

    We have $$\begin{aligned}\begin{pmatrix} n + 1 \\ k \end{pmatrix} &\overset{\text{def}}{=} \frac{(n + 1)!}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1)}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 + k - k)}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k) + (n!)k}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k)}{k!(n + 1 - k)!} + \frac{(n)!k}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k)}{k!(n - k)!(n + 1 - k)} + \frac{(n)!k}{(k - 1)!(n - k + 1)!k} \\ &= \frac{(n)!}{k!(n - k)!} + \frac{(n)!}{(k - 1)!(n - k + 1)!} \\ &\overset{\text{def}}{=} \begin{pmatrix} n \\ k \end{pmatrix} + \begin{pmatrix} n \\ k-1 \end{pmatrix}.\end{aligned}$$

    ### Exercise 1

    **Use induction on $n$ to prove Newton's formula: $(a + b)^n = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} a^k b^{n - k}$**.

    Proof

    If $n = 0$, $(a + b)^n = 1$, $\sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} a^k b^{n - k} = 1 \cdot 1 \cdot 1 = 1$, thus equality holds.

    Suppose equality holds for $m$, then: $$\begin{aligned}(a + b)^{m + 1} &= (a + b)(a + b)^m \\ &= (a + b) \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k} \\ &= \sum\limits_{k = 0}^{m} (\begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k}a + \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k}b) \\ &= \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^{k + 1} b^{m - k} + \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m + 1 - k} \\ &= \sum\limits_{k = 1}^{m + 1} \begin{pmatrix} m \\ k - 1 \end{pmatrix} a^{k} b^{m + 1 - k} + \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m + 1 - k} \\ &= \sum\limits_{k = 1}^{m} [(\begin{pmatrix} m \\ k - 1 \end{pmatrix} + \begin{pmatrix} m \\ k \end{pmatrix}) a^{k} b^{m + 1 - k}] \\ &~~~~~~~~~+ \begin{pmatrix} m \\ m + 1 - 1 \end{pmatrix} a^{m + 1}b^{m + 1 - m - 1} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1 - 0} \\ &= \sum\limits_{k = 1}^{m} [\begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}] + \begin{pmatrix} m \\ m \end{pmatrix} a^{m + 1}b^{0} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1} \\ &= \sum\limits_{k = 1}^{m} (\begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}) + \begin{pmatrix} m + 1 \\ m + 1 \end{pmatrix} a^{m + 1}b^{0} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1} \\ &= \sum\limits_{k = 0}^{m + 1} \begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}.\end{aligned}$$ Thus by induction, equality holds for all natural $n$.

    ### Exercise 2

    **Let $n$ be a positive integer. Prove that for any $k \in \lbrace 0, \dots, n \rbrace$, one has $\begin{pmatrix} n \\ k \end{pmatrix} < 2^n$**.

    Proof

    By Newton's formula, $2^n = (1 + 1)^n = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} 1^k 1^{n - k} = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix}$, since each $\begin{pmatrix} n \\ k \end{pmatrix} \ge 1$ by definition, and if $n$ positive, there is more than $1$ term in the summation, clearly $\begin{pmatrix} n \\ k \end{pmatrix} < 2^n$ for each possible $k$.

    ### Exercise 3

    **Use induction to prove the pigeonhole principle: any map from a set with $n + 1$ objects to a set with n objects is not injective**.

    Proof

    If $n = 0$, clearly $1$ object cannot be assigned injectively to $0$ object (I will use 'box' to reduce confusion).

    Assume that any map from a set with $m + 1$ objects to a set with $m$ boxes is not injective, then if we have $m + 2$ objects and $m + 1$ boxes:

    For any map from $m + 2$ objects and $m + 1$ boxes, for convenience and without losing generality, index the boxes from $1$ to $m + 1$.

    If $2$ or more objects are assigned to box No. 1, then clearly this map is not injective; if $1$ object is assigned to box No. 1, then we have $m + 1$ objects and $m$ boxes to be assigned. By assumption, there is no injective map to do so; if $0$ object is assigned to box No. 1, then we have $m + 2$ objects and $m$ boxes to be assigned. By assumption, there is no injective map to assign $m + 1$ objects to $m$ boxes injectively, thus clearly there is no injective map to assign $m + 2 - (m + 1) = 1$ more object.

    Thus by induction, any map from a set with $n + 1$ objects to a set with n objects is not injective.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Exercise 8

    **Compute the $GCD(528, 303)$ using the Euclidean algorithm**.

    Solution
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""By the Euclidean algorithm, $$\begin{aligned}528 &= 1 \cdot 303 + 225 \\ 303 &= 1 \cdot 225 + 78 \\ 225 &= 2 \cdot 78 + 69 \\ 78 &= 1 \cdot 69 + 9 \\ 69 &= 7 \cdot 9 + 6 \\ 9 &= 1 \cdot 6 + 3 \\ 6 &= 2 \cdot 3 + 0\end{aligned}$$ thus $GCD(528, 303) = 3$."""
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Exercise 9

    **Prove the 'Euclidean division for $\mathbb{Z}$ ': Given two integers $a, b$ with $b \ne 0$, there exists a unique pair of integers $(r, q)$ such that $a = b q + r \text{, and}0 \le r < | b |$**.

    Proof
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Consider the set $A = \lbrace a - b n | n \in \mathbb{Z}, a - b n \ge 0 \rbrace$. If $a \ge 0$, then $a - b\cdot 0 \in A$. If $a < 0$ and $b > 0$, since $a, b, n$ are all finite, clearly there exists large enough $-n \in \mathbb{Z}_+$ such that $b (-n) \ge -a$ thus $a - b n \in A$; if $a < 0$ and $b < 0$, similarly there exist large enough $n \in \mathbb{Z}_+$ such that $(-b) n \ge -a$ thus $a -b n \in A$.

    Since $a, b ,n \in \mathbb{Z}, \forall a, b, n$, $a - bn \in \mathbb{Z}$; since $a - bn \ge 0$, by definition $a - bn \in \mathbb{N}$, thus $A \subseteq \mathbb{N}$. Take the least element $a - b n \in A$ and name it $r$, let $q$ be the corresponding $n$.

    If $r \ge | b |$ and $b > 0$, then $a - b(n + 1) = a - b n - b = r - b \ge 0$ thus $a - b(n + 1) = r - b \in A$ and $r - b < r$, thus $r$ is not the least element in $A$, which is a contradiction. Similarly, if $r \ge | b |$ and $b < 0$, then $a - b(n - 1) = a - b n + b = r + b \in A$ and smaller than $r$, which is another contradiction. Thus $0 \le r < | b |$ and thus the pair $(r, q)$ exists.

    Suppose now that there is another pair of $(r', p')$ that satisfy the condition. I.e. $a - b q' = r'$ and $0 \le r' < | b |$. Then $0 \le a - b q' < | b | \implies b q' \le a < | b | + b q'$. Similarly for the origin pair $(r, q)$, we also have $b q \le a < | b | + b q$. By assumption, $q \ne q'$, without losing generality assume $q < q'$ thus $q + 1 \le q'$. Without losing generality assume $b > 0$, then $b q \le a < | b | + b q = b + b q = b (q + 1) \le b q' \le a < | b | + b q'$ thus $a < a$ which is a contradiction. Thus the pair $(r, q)$ is unique.
    """
    )
    return


@app.cell(column=1)
def _(mo):
    mo.md(
        r"""
    ## Section 0.7

    ### Exercise 0

    **Recalling that $\begin{pmatrix} n \\ k \end{pmatrix} \overset{\text{def}}{=} \frac{n!}{k!(n - k)!}$, prove that for any integers $n \ge k \ge 1$ one has: $\begin{pmatrix} n + 1 \\ k \end{pmatrix} = \begin{pmatrix} n \\ k \end{pmatrix} + \begin{pmatrix} n \\ k-1 \end{pmatrix}$**.

    Proof

    We have $$\begin{aligned}\begin{pmatrix} n + 1 \\ k \end{pmatrix} &\overset{\text{def}}{=} \frac{(n + 1)!}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1)}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 + k - k)}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k) + (n!)k}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k)}{k!(n + 1 - k)!} + \frac{(n)!k}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k)}{k!(n - k)!(n + 1 - k)} + \frac{(n)!k}{(k - 1)!(n - k + 1)!k} \\ &= \frac{(n)!}{k!(n - k)!} + \frac{(n)!}{(k - 1)!(n - k + 1)!} \\ &\overset{\text{def}}{=} \begin{pmatrix} n \\ k \end{pmatrix} + \begin{pmatrix} n \\ k-1 \end{pmatrix}.\end{aligned}$$

    ### Exercise 1

    **Use induction on $n$ to prove Newton's formula: $(a + b)^n = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} a^k b^{n - k}$**.

    Proof

    If $n = 0$, $(a + b)^n = 1$, $\sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} a^k b^{n - k} = 1 \cdot 1 \cdot 1 = 1$, thus equality holds.

    Suppose equality holds for $m$, then: $$\begin{aligned}(a + b)^{m + 1} &= (a + b)(a + b)^m \\ &= (a + b) \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k} \\ &= \sum\limits_{k = 0}^{m} (\begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k}a + \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k}b) \\ &= \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^{k + 1} b^{m - k} + \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m + 1 - k} \\ &= \sum\limits_{k = 1}^{m + 1} \begin{pmatrix} m \\ k - 1 \end{pmatrix} a^{k} b^{m + 1 - k} + \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m + 1 - k} \\ &= \sum\limits_{k = 1}^{m} [(\begin{pmatrix} m \\ k - 1 \end{pmatrix} + \begin{pmatrix} m \\ k \end{pmatrix}) a^{k} b^{m + 1 - k}] \\ &~~~~~~~~~+ \begin{pmatrix} m \\ m + 1 - 1 \end{pmatrix} a^{m + 1}b^{m + 1 - m - 1} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1 - 0} \\ &= \sum\limits_{k = 1}^{m} [\begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}] + \begin{pmatrix} m \\ m \end{pmatrix} a^{m + 1}b^{0} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1} \\ &= \sum\limits_{k = 1}^{m} (\begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}) + \begin{pmatrix} m + 1 \\ m + 1 \end{pmatrix} a^{m + 1}b^{0} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1} \\ &= \sum\limits_{k = 0}^{m + 1} \begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}.\end{aligned}$$ Thus by induction, equality holds for all natural $n$.

    ### Exercise 2

    **Let $n$ be a positive integer. Prove that for any $k \in \lbrace 0, \dots, n \rbrace$, one has $\begin{pmatrix} n \\ k \end{pmatrix} < 2^n$**.

    Proof

    By Newton's formula, $2^n = (1 + 1)^n = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} 1^k 1^{n - k} = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix}$, since each $\begin{pmatrix} n \\ k \end{pmatrix} \ge 1$ by definition, and if $n$ positive, there is more than $1$ term in the summation, clearly $\begin{pmatrix} n \\ k \end{pmatrix} < 2^n$ for each possible $k$.

    ### Exercise 3

    **Use induction to prove the pigeonhole principle: any map from a set with $n + 1$ objects to a set with n objects is not injective**.

    Proof

    If $n = 0$, clearly $1$ object cannot be assigned injectively to $0$ object (I will use 'box' to reduce confusion).

    Assume that any map from a set with $m + 1$ objects to a set with $m$ boxes is not injective, then if we have $m + 2$ objects and $m + 1$ boxes:

    For any map from $m + 2$ objects and $m + 1$ boxes, for convenience and without losing generality, index the boxes from $1$ to $m + 1$.

    If $2$ or more objects are assigned to box No. 1, then clearly this map is not injective; if $1$ object is assigned to box No. 1, then we have $m + 1$ objects and $m$ boxes to be assigned. By assumption, there is no injective map to do so; if $0$ object is assigned to box No. 1, then we have $m + 2$ objects and $m$ boxes to be assigned. By assumption, there is no injective map to assign $m + 1$ objects to $m$ boxes injectively, thus clearly there is no injective map to assign $m + 2 - (m + 1) = 1$ more object.

    Thus by induction, any map from a set with $n + 1$ objects to a set with n objects is not injective.
    """
    )
    return


@app.cell(column=2)
def _(mo):
    mo.md(
        r"""
    ## Section 0.7

    ### Exercise 0

    **Recalling that $\begin{pmatrix} n \\ k \end{pmatrix} \overset{\text{def}}{=} \frac{n!}{k!(n - k)!}$, prove that for any integers $n \ge k \ge 1$ one has: $\begin{pmatrix} n + 1 \\ k \end{pmatrix} = \begin{pmatrix} n \\ k \end{pmatrix} + \begin{pmatrix} n \\ k-1 \end{pmatrix}$**.

    Proof

    We have $$\begin{aligned}\begin{pmatrix} n + 1 \\ k \end{pmatrix} &\overset{\text{def}}{=} \frac{(n + 1)!}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1)}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 + k - k)}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k) + (n!)k}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k)}{k!(n + 1 - k)!} + \frac{(n)!k}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k)}{k!(n - k)!(n + 1 - k)} + \frac{(n)!k}{(k - 1)!(n - k + 1)!k} \\ &= \frac{(n)!}{k!(n - k)!} + \frac{(n)!}{(k - 1)!(n - k + 1)!} \\ &\overset{\text{def}}{=} \begin{pmatrix} n \\ k \end{pmatrix} + \begin{pmatrix} n \\ k-1 \end{pmatrix}.\end{aligned}$$

    ### Exercise 1

    **Use induction on $n$ to prove Newton's formula: $(a + b)^n = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} a^k b^{n - k}$**.

    Proof

    If $n = 0$, $(a + b)^n = 1$, $\sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} a^k b^{n - k} = 1 \cdot 1 \cdot 1 = 1$, thus equality holds.

    Suppose equality holds for $m$, then: $$\begin{aligned}(a + b)^{m + 1} &= (a + b)(a + b)^m \\ &= (a + b) \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k} \\ &= \sum\limits_{k = 0}^{m} (\begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k}a + \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k}b) \\ &= \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^{k + 1} b^{m - k} + \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m + 1 - k} \\ &= \sum\limits_{k = 1}^{m + 1} \begin{pmatrix} m \\ k - 1 \end{pmatrix} a^{k} b^{m + 1 - k} + \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m + 1 - k} \\ &= \sum\limits_{k = 1}^{m} [(\begin{pmatrix} m \\ k - 1 \end{pmatrix} + \begin{pmatrix} m \\ k \end{pmatrix}) a^{k} b^{m + 1 - k}] \\ &~~~~~~~~~+ \begin{pmatrix} m \\ m + 1 - 1 \end{pmatrix} a^{m + 1}b^{m + 1 - m - 1} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1 - 0} \\ &= \sum\limits_{k = 1}^{m} [\begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}] + \begin{pmatrix} m \\ m \end{pmatrix} a^{m + 1}b^{0} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1} \\ &= \sum\limits_{k = 1}^{m} (\begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}) + \begin{pmatrix} m + 1 \\ m + 1 \end{pmatrix} a^{m + 1}b^{0} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1} \\ &= \sum\limits_{k = 0}^{m + 1} \begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}.\end{aligned}$$ Thus by induction, equality holds for all natural $n$.

    ### Exercise 2

    **Let $n$ be a positive integer. Prove that for any $k \in \lbrace 0, \dots, n \rbrace$, one has $\begin{pmatrix} n \\ k \end{pmatrix} < 2^n$**.

    Proof

    By Newton's formula, $2^n = (1 + 1)^n = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} 1^k 1^{n - k} = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix}$, since each $\begin{pmatrix} n \\ k \end{pmatrix} \ge 1$ by definition, and if $n$ positive, there is more than $1$ term in the summation, clearly $\begin{pmatrix} n \\ k \end{pmatrix} < 2^n$ for each possible $k$.

    ### Exercise 3

    **Use induction to prove the pigeonhole principle: any map from a set with $n + 1$ objects to a set with n objects is not injective**.

    Proof

    If $n = 0$, clearly $1$ object cannot be assigned injectively to $0$ object (I will use 'box' to reduce confusion).

    Assume that any map from a set with $m + 1$ objects to a set with $m$ boxes is not injective, then if we have $m + 2$ objects and $m + 1$ boxes:

    For any map from $m + 2$ objects and $m + 1$ boxes, for convenience and without losing generality, index the boxes from $1$ to $m + 1$.

    If $2$ or more objects are assigned to box No. 1, then clearly this map is not injective; if $1$ object is assigned to box No. 1, then we have $m + 1$ objects and $m$ boxes to be assigned. By assumption, there is no injective map to do so; if $0$ object is assigned to box No. 1, then we have $m + 2$ objects and $m$ boxes to be assigned. By assumption, there is no injective map to assign $m + 1$ objects to $m$ boxes injectively, thus clearly there is no injective map to assign $m + 2 - (m + 1) = 1$ more object.

    Thus by induction, any map from a set with $n + 1$ objects to a set with n objects is not injective.
    """
    )
    return


@app.cell(column=3)
def _(mo):
    mo.md(
        r"""
    ## Section 0.7

    ### Exercise 0

    **Recalling that $\begin{pmatrix} n \\ k \end{pmatrix} \overset{\text{def}}{=} \frac{n!}{k!(n - k)!}$, prove that for any integers $n \ge k \ge 1$ one has: $\begin{pmatrix} n + 1 \\ k \end{pmatrix} = \begin{pmatrix} n \\ k \end{pmatrix} + \begin{pmatrix} n \\ k-1 \end{pmatrix}$**.

    Proof

    We have $$\begin{aligned}\begin{pmatrix} n + 1 \\ k \end{pmatrix} &\overset{\text{def}}{=} \frac{(n + 1)!}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1)}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 + k - k)}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k) + (n!)k}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k)}{k!(n + 1 - k)!} + \frac{(n)!k}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k)}{k!(n - k)!(n + 1 - k)} + \frac{(n)!k}{(k - 1)!(n - k + 1)!k} \\ &= \frac{(n)!}{k!(n - k)!} + \frac{(n)!}{(k - 1)!(n - k + 1)!} \\ &\overset{\text{def}}{=} \begin{pmatrix} n \\ k \end{pmatrix} + \begin{pmatrix} n \\ k-1 \end{pmatrix}.\end{aligned}$$

    ### Exercise 1

    **Use induction on $n$ to prove Newton's formula: $(a + b)^n = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} a^k b^{n - k}$**.

    Proof

    If $n = 0$, $(a + b)^n = 1$, $\sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} a^k b^{n - k} = 1 \cdot 1 \cdot 1 = 1$, thus equality holds.

    Suppose equality holds for $m$, then: $$\begin{aligned}(a + b)^{m + 1} &= (a + b)(a + b)^m \\ &= (a + b) \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k} \\ &= \sum\limits_{k = 0}^{m} (\begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k}a + \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k}b) \\ &= \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^{k + 1} b^{m - k} + \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m + 1 - k} \\ &= \sum\limits_{k = 1}^{m + 1} \begin{pmatrix} m \\ k - 1 \end{pmatrix} a^{k} b^{m + 1 - k} + \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m + 1 - k} \\ &= \sum\limits_{k = 1}^{m} [(\begin{pmatrix} m \\ k - 1 \end{pmatrix} + \begin{pmatrix} m \\ k \end{pmatrix}) a^{k} b^{m + 1 - k}] \\ &~~~~~~~~~+ \begin{pmatrix} m \\ m + 1 - 1 \end{pmatrix} a^{m + 1}b^{m + 1 - m - 1} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1 - 0} \\ &= \sum\limits_{k = 1}^{m} [\begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}] + \begin{pmatrix} m \\ m \end{pmatrix} a^{m + 1}b^{0} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1} \\ &= \sum\limits_{k = 1}^{m} (\begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}) + \begin{pmatrix} m + 1 \\ m + 1 \end{pmatrix} a^{m + 1}b^{0} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1} \\ &= \sum\limits_{k = 0}^{m + 1} \begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}.\end{aligned}$$ Thus by induction, equality holds for all natural $n$.

    ### Exercise 2

    **Let $n$ be a positive integer. Prove that for any $k \in \lbrace 0, \dots, n \rbrace$, one has $\begin{pmatrix} n \\ k \end{pmatrix} < 2^n$**.

    Proof

    By Newton's formula, $2^n = (1 + 1)^n = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} 1^k 1^{n - k} = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix}$, since each $\begin{pmatrix} n \\ k \end{pmatrix} \ge 1$ by definition, and if $n$ positive, there is more than $1$ term in the summation, clearly $\begin{pmatrix} n \\ k \end{pmatrix} < 2^n$ for each possible $k$.

    ### Exercise 3

    **Use induction to prove the pigeonhole principle: any map from a set with $n + 1$ objects to a set with n objects is not injective**.

    Proof

    If $n = 0$, clearly $1$ object cannot be assigned injectively to $0$ object (I will use 'box' to reduce confusion).

    Assume that any map from a set with $m + 1$ objects to a set with $m$ boxes is not injective, then if we have $m + 2$ objects and $m + 1$ boxes:

    For any map from $m + 2$ objects and $m + 1$ boxes, for convenience and without losing generality, index the boxes from $1$ to $m + 1$.

    If $2$ or more objects are assigned to box No. 1, then clearly this map is not injective; if $1$ object is assigned to box No. 1, then we have $m + 1$ objects and $m$ boxes to be assigned. By assumption, there is no injective map to do so; if $0$ object is assigned to box No. 1, then we have $m + 2$ objects and $m$ boxes to be assigned. By assumption, there is no injective map to assign $m + 1$ objects to $m$ boxes injectively, thus clearly there is no injective map to assign $m + 2 - (m + 1) = 1$ more object.

    Thus by induction, any map from a set with $n + 1$ objects to a set with n objects is not injective.
    """
    )
    return


@app.cell(column=4)
def _(mo):
    mo.md(
        r"""
    ## Section 0.7

    ### Exercise 0

    **Recalling that $\begin{pmatrix} n \\ k \end{pmatrix} \overset{\text{def}}{=} \frac{n!}{k!(n - k)!}$, prove that for any integers $n \ge k \ge 1$ one has: $\begin{pmatrix} n + 1 \\ k \end{pmatrix} = \begin{pmatrix} n \\ k \end{pmatrix} + \begin{pmatrix} n \\ k-1 \end{pmatrix}$**.

    Proof

    We have $$\begin{aligned}\begin{pmatrix} n + 1 \\ k \end{pmatrix} &\overset{\text{def}}{=} \frac{(n + 1)!}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1)}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 + k - k)}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k) + (n!)k}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k)}{k!(n + 1 - k)!} + \frac{(n)!k}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k)}{k!(n - k)!(n + 1 - k)} + \frac{(n)!k}{(k - 1)!(n - k + 1)!k} \\ &= \frac{(n)!}{k!(n - k)!} + \frac{(n)!}{(k - 1)!(n - k + 1)!} \\ &\overset{\text{def}}{=} \begin{pmatrix} n \\ k \end{pmatrix} + \begin{pmatrix} n \\ k-1 \end{pmatrix}.\end{aligned}$$

    ### Exercise 1

    **Use induction on $n$ to prove Newton's formula: $(a + b)^n = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} a^k b^{n - k}$**.

    Proof

    If $n = 0$, $(a + b)^n = 1$, $\sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} a^k b^{n - k} = 1 \cdot 1 \cdot 1 = 1$, thus equality holds.

    Suppose equality holds for $m$, then: $$\begin{aligned}(a + b)^{m + 1} &= (a + b)(a + b)^m \\ &= (a + b) \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k} \\ &= \sum\limits_{k = 0}^{m} (\begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k}a + \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k}b) \\ &= \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^{k + 1} b^{m - k} + \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m + 1 - k} \\ &= \sum\limits_{k = 1}^{m + 1} \begin{pmatrix} m \\ k - 1 \end{pmatrix} a^{k} b^{m + 1 - k} + \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m + 1 - k} \\ &= \sum\limits_{k = 1}^{m} [(\begin{pmatrix} m \\ k - 1 \end{pmatrix} + \begin{pmatrix} m \\ k \end{pmatrix}) a^{k} b^{m + 1 - k}] \\ &~~~~~~~~~+ \begin{pmatrix} m \\ m + 1 - 1 \end{pmatrix} a^{m + 1}b^{m + 1 - m - 1} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1 - 0} \\ &= \sum\limits_{k = 1}^{m} [\begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}] + \begin{pmatrix} m \\ m \end{pmatrix} a^{m + 1}b^{0} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1} \\ &= \sum\limits_{k = 1}^{m} (\begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}) + \begin{pmatrix} m + 1 \\ m + 1 \end{pmatrix} a^{m + 1}b^{0} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1} \\ &= \sum\limits_{k = 0}^{m + 1} \begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}.\end{aligned}$$ Thus by induction, equality holds for all natural $n$.

    ### Exercise 2

    **Let $n$ be a positive integer. Prove that for any $k \in \lbrace 0, \dots, n \rbrace$, one has $\begin{pmatrix} n \\ k \end{pmatrix} < 2^n$**.

    Proof

    By Newton's formula, $2^n = (1 + 1)^n = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} 1^k 1^{n - k} = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix}$, since each $\begin{pmatrix} n \\ k \end{pmatrix} \ge 1$ by definition, and if $n$ positive, there is more than $1$ term in the summation, clearly $\begin{pmatrix} n \\ k \end{pmatrix} < 2^n$ for each possible $k$.

    ### Exercise 3

    **Use induction to prove the pigeonhole principle: any map from a set with $n + 1$ objects to a set with n objects is not injective**.

    Proof

    If $n = 0$, clearly $1$ object cannot be assigned injectively to $0$ object (I will use 'box' to reduce confusion).

    Assume that any map from a set with $m + 1$ objects to a set with $m$ boxes is not injective, then if we have $m + 2$ objects and $m + 1$ boxes:

    For any map from $m + 2$ objects and $m + 1$ boxes, for convenience and without losing generality, index the boxes from $1$ to $m + 1$.

    If $2$ or more objects are assigned to box No. 1, then clearly this map is not injective; if $1$ object is assigned to box No. 1, then we have $m + 1$ objects and $m$ boxes to be assigned. By assumption, there is no injective map to do so; if $0$ object is assigned to box No. 1, then we have $m + 2$ objects and $m$ boxes to be assigned. By assumption, there is no injective map to assign $m + 1$ objects to $m$ boxes injectively, thus clearly there is no injective map to assign $m + 2 - (m + 1) = 1$ more object.

    Thus by induction, any map from a set with $n + 1$ objects to a set with n objects is not injective.
    """
    )
    return


@app.cell(column=5)
def _(mo):
    mo.md(
        r"""
    ## Section 0.7

    ### Exercise 0

    **Recalling that $\begin{pmatrix} n \\ k \end{pmatrix} \overset{\text{def}}{=} \frac{n!}{k!(n - k)!}$, prove that for any integers $n \ge k \ge 1$ one has: $\begin{pmatrix} n + 1 \\ k \end{pmatrix} = \begin{pmatrix} n \\ k \end{pmatrix} + \begin{pmatrix} n \\ k-1 \end{pmatrix}$**.

    Proof

    We have $$\begin{aligned}\begin{pmatrix} n + 1 \\ k \end{pmatrix} &\overset{\text{def}}{=} \frac{(n + 1)!}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1)}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 + k - k)}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k) + (n!)k}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k)}{k!(n + 1 - k)!} + \frac{(n)!k}{k!(n + 1 - k)!} \\ &= \frac{(n)!(n + 1 - k)}{k!(n - k)!(n + 1 - k)} + \frac{(n)!k}{(k - 1)!(n - k + 1)!k} \\ &= \frac{(n)!}{k!(n - k)!} + \frac{(n)!}{(k - 1)!(n - k + 1)!} \\ &\overset{\text{def}}{=} \begin{pmatrix} n \\ k \end{pmatrix} + \begin{pmatrix} n \\ k-1 \end{pmatrix}.\end{aligned}$$

    ### Exercise 1

    **Use induction on $n$ to prove Newton's formula: $(a + b)^n = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} a^k b^{n - k}$**.

    Proof

    If $n = 0$, $(a + b)^n = 1$, $\sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} a^k b^{n - k} = 1 \cdot 1 \cdot 1 = 1$, thus equality holds.

    Suppose equality holds for $m$, then: $$\begin{aligned}(a + b)^{m + 1} &= (a + b)(a + b)^m \\ &= (a + b) \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k} \\ &= \sum\limits_{k = 0}^{m} (\begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k}a + \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m - k}b) \\ &= \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^{k + 1} b^{m - k} + \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m + 1 - k} \\ &= \sum\limits_{k = 1}^{m + 1} \begin{pmatrix} m \\ k - 1 \end{pmatrix} a^{k} b^{m + 1 - k} + \sum\limits_{k = 0}^{m} \begin{pmatrix} m \\ k \end{pmatrix} a^k b^{m + 1 - k} \\ &= \sum\limits_{k = 1}^{m} [(\begin{pmatrix} m \\ k - 1 \end{pmatrix} + \begin{pmatrix} m \\ k \end{pmatrix}) a^{k} b^{m + 1 - k}] \\ &~~~~~~~~~+ \begin{pmatrix} m \\ m + 1 - 1 \end{pmatrix} a^{m + 1}b^{m + 1 - m - 1} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1 - 0} \\ &= \sum\limits_{k = 1}^{m} [\begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}] + \begin{pmatrix} m \\ m \end{pmatrix} a^{m + 1}b^{0} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1} \\ &= \sum\limits_{k = 1}^{m} (\begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}) + \begin{pmatrix} m + 1 \\ m + 1 \end{pmatrix} a^{m + 1}b^{0} + \begin{pmatrix} m \\ 0 \end{pmatrix} a^0 b^{m + 1} \\ &= \sum\limits_{k = 0}^{m + 1} \begin{pmatrix} m + 1 \\ k \end{pmatrix} a^{k} b^{m + 1 - k}.\end{aligned}$$ Thus by induction, equality holds for all natural $n$.

    ### Exercise 2

    **Let $n$ be a positive integer. Prove that for any $k \in \lbrace 0, \dots, n \rbrace$, one has $\begin{pmatrix} n \\ k \end{pmatrix} < 2^n$**.

    Proof

    By Newton's formula, $2^n = (1 + 1)^n = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix} 1^k 1^{n - k} = \sum\limits_{k = 0}^{n} \begin{pmatrix} n \\ k \end{pmatrix}$, since each $\begin{pmatrix} n \\ k \end{pmatrix} \ge 1$ by definition, and if $n$ positive, there is more than $1$ term in the summation, clearly $\begin{pmatrix} n \\ k \end{pmatrix} < 2^n$ for each possible $k$.

    ### Exercise 3

    **Use induction to prove the pigeonhole principle: any map from a set with $n + 1$ objects to a set with n objects is not injective**.

    Proof

    If $n = 0$, clearly $1$ object cannot be assigned injectively to $0$ object (I will use 'box' to reduce confusion).

    Assume that any map from a set with $m + 1$ objects to a set with $m$ boxes is not injective, then if we have $m + 2$ objects and $m + 1$ boxes:

    For any map from $m + 2$ objects and $m + 1$ boxes, for convenience and without losing generality, index the boxes from $1$ to $m + 1$.

    If $2$ or more objects are assigned to box No. 1, then clearly this map is not injective; if $1$ object is assigned to box No. 1, then we have $m + 1$ objects and $m$ boxes to be assigned. By assumption, there is no injective map to do so; if $0$ object is assigned to box No. 1, then we have $m + 2$ objects and $m$ boxes to be assigned. By assumption, there is no injective map to assign $m + 1$ objects to $m$ boxes injectively, thus clearly there is no injective map to assign $m + 2 - (m + 1) = 1$ more object.

    Thus by induction, any map from a set with $n + 1$ objects to a set with n objects is not injective.
    """
    )
    return


if __name__ == "__main__":
    app.run()
