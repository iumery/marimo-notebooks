import marimo

__generated_with = "0.15.4"
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

    ### Exercise 8

    **Compute the $GCD(528, 303)$ using the Euclidean algorithm**.

    Solution

    By the Euclidean algorithm, $$\begin{aligned}528 &= 1 \cdot 303 + 225 \\ 303 &= 1 \cdot 225 + 78 \\ 225 &= 2 \cdot 78 + 69 \\ 78 &= 1 \cdot 69 + 9 \\ 69 &= 7 \cdot 9 + 6 \\ 9 &= 1 \cdot 6 + 3 \\ 6 &= 2 \cdot 3 + 0\end{aligned}$$ thus $GCD(528, 303) = 3$.

    ### Exercise 9

    **Prove the 'Euclidean division for $\mathbb{Z}$ ': Given two integers $a, b$ with $b \ne 0$, there exists a unique pair of integers $(r, q)$ such that $a = b q + r \text{, and}0 \le r < | b |$**.

    Proof

    Consider the set $A = \lbrace a - b n | n \in \mathbb{Z}, a - b n \ge 0 \rbrace$. If $a \ge 0$, then $a - b\cdot 0 \in A$;

    If $a < 0$ and $b > 0$, since $a, b, n$ are all finite, clearly there exists large enough $-n \in \mathbb{Z}_+$ such that $b (-n) \ge -a$ thus $a - b n \in A$; if $a < 0$ and $b < 0$, similarly there exist large enough $n \in \mathbb{Z}_+$ such that $(-b) n \ge -a$ thus $a -b n \in A$.

    Since $a, b ,n \in \mathbb{Z}, \forall a, b, n$, $a - bn \in \mathbb{Z}$; since $a - bn \ge 0$, by definition $a - bn \in \mathbb{N}$, thus $A \subseteq \mathbb{N}$.

    Take the least element $a - b n \in A$ and name it $r$, let $q$ be the corresponding $n$.

    If $r \ge | b |$ and $b > 0$, then $a - b(n + 1) = a - b n - b = r - b \ge 0$ thus $a - b(n + 1) = r - b \in A$ and $r - b < r$, thus $r$ is not the least element in $A$, which is a contradiction.

    Similarly, if $r \ge | b |$ and $b < 0$, then $a - b(n - 1) = a - b n + b = r + b \in A$ and smaller than $r$, which is another contradiction.

    Thus $0 \le r < | b |$ and thus the pair $(r, q)$ exists.

    Suppose now that there is another pair of $(r', p')$ that satisfy the condition. I.e. $a - b q' = r'$ and $0 \le r' < | b |$.

    Then $0 \le a - b q' < | b | \implies b q' \le a < | b | + b q'$.

    Similarly for the origin pair $(r, q)$, we also have $b q \le a < | b | + b q$.

    By assumption, $q \ne q'$, without losing generality assume $q < q'$ thus $q + 1 \le q'$. Without losing generality assume $b > 0$, then $b q \le a < | b | + b q = b + b q = b (q + 1) \le b q' \le a < | b | + b q'$ thus $a < a$ which is a contradiction.

    Thus the pair $(r, q)$ is unique.
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
    ## Section 0.7

    ### Exercise 14

    **Think of a number. Square it. Divide the result by $3$. Why is the remainder always $0$ or $1$, but never $2$? Justify your answer**.

    Proof

    Let $n \in \mathbb{Z}$ be an arbitrary number. Then in $\mathbb{Z}_3$, $\hat{n}$ is equivalent to exactly one of $\hat{0}, \hat{1}$ or $\hat{2}$.

    If $\hat{n} = \hat{0}$, then $\hat{n} \cdot \hat{n} = \hat{0} \cdot \hat{n} = \hat{0 \cdot n} = \hat{0}$, i.e. remainder of the square is $0$; if $\hat{n} = \hat{1}$, then $\hat{n} \cdot \hat{n} = \hat{1} \cdot \hat{n} = \hat{1 \cdot n} = \hat{n} = \hat{1}$, i.e. remainder of the square is $1$; if $\hat{n} = \hat{2}$, then $\hat{n} = \hat{-1}$, thus $\hat{n} \cdot \hat{n} = \hat{-1} \cdot \hat{-1} = \hat{-1 \cdot -1} = \hat{1}$, i.e. remainder of the square is $1$.

    Since we listed all the situations above, we may see that the remainder of a square is never $2$.

    ### Exercise 16

    **What are the last two digits of $913250946798^6$**?

    Solution

    Since we need to know the last 'two' digits, we work in $\mathbb{Z}_{100}$, then:

    $913250946798^6 = (9132509468 \cdot 100 - 2)^6 \equiv (2)^6 = 64$ mod $100$. I.e. the last two digits are $64$.

    ### Exercise 17

    **Compute $12345678^{23456789}$ mod $3$**.

    Solution

    Notice that $12345678 \equiv 0$ mod $3$ as the summation of its digits are $1+2+3+4+5+6+7+8 = 36$ is divisible by $3$. Thus $12345678^{23456789} \equiv 0^{23456789} \equiv 0$ mod $3$.

    ### Exercise 18

    **Suppose that a number $x$ can be written in the decimal representation as '$abcabc$', with $a, b, c$ decimal digits. (For example, $x = 285285$.) Show that $x$ is always a multiple of $13$**.

    Proof

    Let $x$ be a number which can be written in the form '$abcabc$'. Then $x = 100000a + 10000b + 1000c + 100a + 10b + c =100100a + 10010b + 1001c$ $= 1001(100a + 10b + c)$. Note that $1001 = 13 \cdot 77$, i.e. $13 | 1001$, thus $13 | 1001 \cdot n$ for any $n$ thus $13 | x$.

    ### Exercise 19

    **Find the remainder of the division of $11^{118}$ by $59$**.

    Proof

    Note that $59$ is a prime.

    Then $11^{118} = 11^{59 + 59} = 11^{59} \cdot 11^{59} \equiv^{\text{by Fermats little theorem}} 11 \cdot 11 = 121 = 2 \cdot 59 + 3 \equiv 3$ mod $59$. I.e. the remainder of the division is $3$.

    ### Exercise 20

    **Write the number $73$ on a piece of paper, fold it up, and give it to an unsuspecting friend. Ask your friend to write his/her birth year twice in a calculator. Then ask your friend if the number is divisible by any chance by $137$; ask him/her to verify with the calculator. Then say, 'please divide the result by your birth year'. Ask your friend to unwrap the paper: the calculator and the piece of paper will magically tell the same number, $73$! Can you spoil the magic and explain the trick**?

    Solution

    Let $x$ be a number which can be written in the form '$abcdabcd$'. Then $x = 10000000a + 1000000b + 100000c + 10000d + 1000a + 100b + 10c + 1d$ $= 10001000a + 1000100b + 100010c +10001d= 10001(1000a + 100b + 10c + 1d)$, notice that $10001 = 137 \cdot 73$ and $1000a + 100b + 10c + 1d$ is exactly the number written as '$abcd$', i.e. the birth year. Thus $x = 137 \cdot 73 \cdot B$ if we denote the birth year as $B$, and thus clearly the number written down, $x$, is divisible by $137$, and the answer of the division is divisible by $B$, and the answer of the division is $73$.
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
    ## Section 1.5

    ### Exercise 3

    **Let $A$ be a C-ring with $1$. Show that $(-1)\cdot(-1) = 1$. Show that for any $a$ in $A$, $(-1)\cdot a=-a$**.

    Proof

    Assume that $A \ne \lbrace 0 \rbrace$. By the property of $0$, $0 = (-1)\cdot 0$, and $(-1)\cdot 0$ $= (-1)\cdot (1 + (-1))$ $= (-1)\cdot (1) + (-1)\cdot(-1)$ by distributivity. Since $1$ is the multiplication identity, $0 = -1 + (-1)\cdot(-1)$ thus $(-1)\cdot(-1)$ is the inverse of $-1$ with respect to addition. Since inverse is unique, it must be $1$.

    Similarly, $0 = a\cdot 0 = a\cdot (1 + (-1)) = a \cdot 1 + a \cdot (-1) = a + a\cdot (-1)$ thus $a\cdot(-1) = (-1)\cdot a$ act as inverse of $a$ with respect to addition thus it is $-a$.

    ### Exercise 8

    **Consider $A = \lbrace f: \mathbb{R} \rightarrow \mathbb{R}, f \text{ is continuous} \rbrace$. The sum of two functions $f$ and $g$ in $A$ is defined as the function that maps $x$ to the real number $f(x) + g(x)$. Similarly, the product of two functions $f$ and $g$ in $A$ is the function that sends $x$ to $f(x)g(x)$. Show that with these two operations, $A$ is a C-ring**.

    Proof

    Follow the definition of a C-ring:

    1. For all $f, g \in A$, $f, g$ continuous $\implies \forall a \in \mathbb{R}, \forall \varepsilon0, | x - a | < \delta_f \implies | f(x) - f(a) | < \varepsilon$, and $| x - a | < \delta_g \implies | g(x) - g(a) | < \varepsilon$:
    	Then take $\delta_f', \delta_g'$ satisfying that $\forall a \in \mathbb{R}$, $\forall \varepsilon > \varepsilon/2 > 0$, $| x - a | < \delta_f' \implies | f(x) - f(a) | < \varepsilon/2$, and $| x - a | < \delta_g' \implies | g(x) - g(a) | < \varepsilon/2$, take $\delta = \min(\delta_f', \delta_g')$ we have $| x - a | < \delta$ $\implies | f(x) + g(x) - (f(a) + g(a)) |$ $= | (f(x) - f(a)) + (g(x) - g(a)) |$ $\le | (f(x) - f(a)) | + | (g(x) - g(a)) |$ $< \varepsilon/2 + \varepsilon/2$ $= \varepsilon, \forall \varepsilon, a$, thus the point-wise addition of two continuous functions is continuous thus in $A$;
    	Similarly take $\delta_f'$ such that $| x - a | < \delta_f' \implies | f(x) - f(a) | < \frac{\varepsilon}{2(| g(a) | + \varepsilon)}$; $\delta_g'$ such that $| x - a | < \delta_g'$ $\implies | g(x) - g(a) | < \frac{\varepsilon}{2 | f(a) | +1}$; $\delta'$ such that $| x - a | < \delta'$ $\implies | g(x) - g(a) | < \varepsilon$;
    	Pick $\delta = \min(\delta_f', \delta_g', \delta')$ then: $| f(x)g(x) - f(a)g(a) |$ $= | f(x)g(x) - f(a)g(x)$ $+ f(a)g(x) - f(a)g(a) |$ $\le | f(x) - f(a) \| g(x) |$ $+ | g(x) - g(a) \| f(a) |$ $\le \frac{\varepsilon}{2(| g(a) | + \varepsilon)} | g(a)$ $+ \varepsilon | + \frac{\varepsilon}{2 | f(a) | +1} | f(a) | \\ < \varepsilon/2 + \varepsilon/2 = \varepsilon, \forall \varepsilon, a$, thus the point-wise product of two continuous functions is continuous thus in $A$;
    2. Addition associativity holds as $f$ are real-valued functions;
    3. Addition commutativity holds as $f$ are real-valued functions;
    4. Take $f_0: \mathbb{R} \rightarrow \mathbb{R}$ given by $f_0(x) = 0, \forall x \in \mathbb{R}$. Clearly this $f_0$ is continuous, and for all $f \in A$, $f + f_0$ is defined as the function that maps $x$ to the real number $f(x) + f_0(x) = f(x) + 0 = f(x)$, since the domain and the codomain are also the same, $f + f_0 = f$, thus we have $f_0$ (act as) the neutral element;
    5. For any $f \in A$, define $f_{-}$ as $f_{-}(x) = -f(x), \forall x$, then for all $x$, $f_-(x) + f(x) = -f(x) + f(x) = 0 = f_0(x)$, thus we have $f_-$ (act as) the additive inverse;
    6. Multiplication associativity holds as $f$ are real-valued functions;
    7. Multiplication commutativity holds as $f$ are real-valued functions;
    8. Distributivity holds as $f$ are real-valued functions.

    Thus by definition, $A$ with the defined two operations is a C-ring.

    ### Exercise 10

    **Let $A$ be a C-ring. Suppose in $A$ there is a non-zero nilpotent element. Is it true that in $A$ there is a non-zero element $a$ such that $a^2 = 0$**?

    Proof

    Suppose $b \ne 0$ is a nilpotent element and let $N$ be the smallest positive integer such that $b^N = 0$, let's assume $N \ge 2$, otherwise the proof is trivial; then $(b^{N - 1})^2 = b^{2N - 2}$ with $2N - 2 \ge 2$ and notice that $2N -2 \ge N$, thus $(b^{N - 1})^2 = 0$.

    By construct $b^{N - 1} \ne 0$ thus we find the element we want.

    ### Exercise 11

    **Is there an element $a$ in $\mathbb{Z}_{10}$ such that $a^2 = 0$? What about in $\mathbb{Z}_{20}$**?

    Solution

    By Exercise 12 below, $\mathbb{Z}_{10}$ is reduce thus such $a$ does not exist. On the other hand $10^2 = 0$ in $\mathbb{Z}_{20}$.

    ### Exercise 12

    **A positive integer $m$ is called square-free if either $m$ is a prime or $m$ is a product of distinct primes. Show that $\mathbb{Z}_m$ is reduced if and only if $m$ is a square-free**.

    Proof

    ($\implies$) Suppose $m$ not square-free, then $m$ contains product of non-distinct prime, say $m = ppm'$ with $p$ prime. Then $\widehat{pm'}^2 = \widehat{pm' p m'} = \widehat{ppm'} \widehat{m'} = \hat{0} \widehat{m'} = 0$ thus $\mathbb{Z}_m$ not reduced, i.e. negation holds;

    ($\impliedby$) Suppose $\mathbb{Z}_m$ is not reduced, thus there exist non-zero $a \in \mathbb{Z}_m$ and $N$ the smallest positive integer such that $a^N = 0$, clearly $N > 1$ otherwise $a^1 = a = 0$. $a \ne 1$ because $1$ is invertible. Then we can write $a = p_1^{n_1} \dots p_k^{n_k}$ with $p_i$ distinct primes, and $n_j \ge 1$ (for example, 6 = 2^1 3^1), and $a^N = (p_1^{n_1} \dots p_k^{n_k})^N = p_1^{n_1 N} \dots p_k^{n_k N}=0$, then by definition $mm' = p_1^{n_1 N} \dots p_k^{n_k N}$ for some $m'$. If $m$ is square-free, then $m = p_{i_1} \dots p_{i_j}$ with $i$'s $\in \lbrace 1, 2, \dots, k \rbrace$, then $m | p_1^{n_1} \dots p_k^{n_k} | p_1^{n_1 (N-1)} \dots p_k^{n_k (N-1)}$ thus $a^{N - 1} = 0$ which is a contradiction. Thus $m$ is not square-free and the negation holds.

    ### Exercise 13

    **Let $A$ be a C-ring. Prove that if $a, b$ are nilpotent, $a + b$ is also nilpotent**.

    Proof

    If $a$ or $b$ is $0$ it is trivial.

    Suppose $a, b$ nilpotent with $n, m$ smallest positive integer make $a^n = 0$ and $b^m = 0$. Then $(a + b)^{n + m} = \sum\limits_{k = 0}^{n + m} \begin{pmatrix} n+m \\ k \end{pmatrix}a^{n+m-k}b^{k}$. While if $k \le m$ then $a^{n+m-k}=a^na^{m-k} = 0$, otherwise $b^k = b^mb^{k-m} = 0$, thus every term in the summation is $0$ thus the summation is $0$ with clearly $n+m$ is a positive integer thus by definition $(a + b)$ nilpotent.
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
    ## Section 4.5

    ### Exercise 3

    **Show that $\mathbb{Z} [x, y]/(y)$ is isomorphic to $\mathbb{Z} [x]$**.
    Proof

    Consider the function $\varphi: \mathbb{Z} [x, y] \rightarrow \mathbb{Z} [x]$ with $f(x, y) \mapsto f(x, 0)$.

    Clearly we want to use the First Isomorphic Theorem:

    1. $\varphi$ is a homomorphism: this is clear by the definition of polynomial addition and multiplication;
    2. $\varphi$ is surjective: for any $f(x) \in \mathbb{Z} [x]$, $\varphi(f(x))$ itself would map $f(x)$ (considered as polynomial of $x$ and $y$) to $f(x)$;
    3. $\ker{\varphi} = (y)$:
    	1. For any $g(x, y) \in (y), g(x, y) = y \cdot h(x, y)$ for some $h(x, y)$, and $\varphi(g(x, y)) = \varphi(y \cdot h(x, y)) = \varphi(y) \varphi(h(x, y)) = 0 \cdot h(x, 0) = 0$ thus $g(x, y)$ is in the kernel;
    	2. For any $g(x, y)$ in the kernel, by definition a polynomial of $x$ and $y$ can be written in the form $g(x, y) = h_0(x) + h_1(x)y + h_2(x)y^2 + \dots + h_n(x)y^n$ where $h_i(x)$'s are polynomials of $x$, thus by definition $0 = g(x, 0) = h_0(x) + h_1(x)0 + \dots + h_n(x)0^n$ thus $h_0(x) = 0$, which means $g(x,y) = h_1(x)y + \dots + h_n(x) y^n \in (y)$.

    Thus by the First Isomorphic Theorem, $\varphi$ induces an isomorphism from $\mathbb{Z} [x, y]/(y)$ to $\mathbb{Z}[x]$.

    ### Section 5.5

    ### Exercise 1

    **Consider the ideal $J = (x+1, x-1)$ in $\mathbb{Z} [x]$. Is it proper? Is it prime? Is it maximal**?

    Solution

    It is proper, notice that $x + 1 = 1 \cdot (x - 1) + 2$ thus $1 \in \mathbb{Z} [x]$ would never be achieved;

    We need to understand the quotient $\mathbb{Z} [x]/(x+1, x-1)$. From above we have $(x+1, x-1) = (2, x+1)$ thus $\mathbb{Z} [x]/ (x+1, x-1) \cong \mathbb{Z} [x]/(2, x+1) \cong \mathbb{Z}_2 [x]/(x+1) \cong \mathbb{Z}_2$, which is a field. Thus it is maximal and prime.

    ### Exercise 2

    **How many ideals with less than $10$ elements does $\mathbb{Z}$ have**?

    Solution

    All ideals of $\mathbb{Z}$ are of the form $(n) = \lbrace kn, k \in \mathbb{Z} \rbrace$, each of the set $(n)$ clearly has infinitely many elements unless $n = 0$, thus there is one ideal with less than $10$ elements in $\mathbb{Z}$.

    ### Exercise 3

    **Show that a domain $A$ is a field if and only if $A$ has finitely many ideals**.

    Proof

    ($\implies$) Clearly $(0)$ is an ideal of $A$. Suppose $(a)$ is another ideal of $A$ with $a \ne 0$. Since $A$ is a field, $a$ is invertible thus $a a' = 1$ for some $a' \in A \implies 1 \in (a)$ thus $(a) = A$ by Explosion Lemma. In other words, there are only two ideals in $A$;

    ($\impliedby$) Since $A$ is a domain, at least $A$ contains an $a \ne 0$. $(a), (a^2), (a^3), \dots$ are all ideals. Since $A$ only have finitely many ideals, we must have $(a^n) = (a^m)$ for some $n, m$. Thus $a^n b = a^m$ for some $b \in A$ thus $a^m(1-a^{n-m}b) = 0$. Since $A$ is a domain, $a^m \ne 0 \implies a^{n-m}b = 1$, WLOG say $n > m$ then $a(a^{n-m-1}b) = 1$, in other word, $a$ is invertible. Thus $A$ is a field.

    ### Exercise 4

    **If every proper ideal of $A$ is prime, show that $A$ is a field**.

    Proof

    For an arbitrary $0 \ne a \in A$, consider the ideal $(a^2)$.

    If it is not a proper ideal, then $(a^2) = A$. Thus $1 \in (a^2)$, thus there exists $b \in A$ such that $1 = a^2 b = a(ab)$, thus $a$ is invertible.

    If it is a proper ideal, then it is prime. Since $a \cdot a = a^2 \in (a^2)$, we have $a \in (a^2)$. Thus there exists $b \in A$ such that $a = a^2 b \implies a(1 - ab) = 0$. Now if $a \ne 0$, we must have $1 - ab = 0 \implies ab = 1$, thus $a$ is invertible.

    Since $a$ is arbitrary, we conclude $A$ is a field.

    ### Exercise 5

    **Prove that $(5)$ is not prime in $\mathbb{Z} [i]$**.

    Proof

    Consider that $5 = (2 + i) (2 -i)$, clearly $2+i \notin (5)$ and $2 - i \notin (5)$.
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
    ## Section 6.5

    ### Exercise 1

    **Let $f(x) = 2x^7 + 25x^3 + 10x^2 - 30$. Prove that $\mathbb{Q} [x]/(f)$ is a field**.

    Proof

    By Eisenstein's criterion, take $p = 5$, then it is easy to see that $5$ does not divide $2$, $25$ does not divide $-30$, and $5$ divides $25, 10$, and $-30$, thus $f$ is irreducible over $\mathbb{Z} [x]$. $f$ is clearly primitive, thus it is also irreducible over $\mathbb{Q} [x]$. Since $\mathbb{Q}$ is a PID, we have $(f)$ is a maximal ideal, which implies that $\mathbb{Q} [x]/(f)$ is a field.

    I think it would also work if we use Modulo- $m$ criterion with $m = 7$, which however would take much more effort.

    ### Exercise 2

    **For what integer values of $b$ is the polynomial $2x^2 + b$ is irreducible in $\mathbb{Z} [x]$**?

    Solution

    In $\mathbb{Z} [x]$, a polynomial of the form $2x^2 + m$ can only possibly be written as $(ax^2 + b)(c)$ or $(ax + b)(cx + d)$.

    If it is the first case then:

    1. $a = 2, c = 1$, then $c$ is invertible;
    2. $a = 1, c = 2$, then $2x^2 + m$ can never be irreducible, as $(a x^2 + b)$ and $(c)$ are both not invertible over $\mathbb{Z} [x]$. In other word, if we want $2x^2 + m$ be irreducible then we cannot have even $m$.

    If it is the second case then:

    WLOG say $a = 2, c = 1$, then we have to have $ad + cb = 0 \implies -2 d = b$, for example $(2x - 2)(x + 1) = 2x^2 - 2$ is reducible.

    The second case is actually weaker than the first case (for example, it does not show that $2x^2 - 4$ is reducible), so in conclusion, odd $b$ would make $2x^2 + m$ irreducible in $\mathbb{Z} [x]$.

    And a quick check: if $m = 2k$ (is even) then clearly $2x^2 + m = 2(x^2 + k)$ is a non-trivial factorization; otherwise $m$ is odd then use quadratic formula it is easy to see $2x^2 + m$ has no integer solutions.

    ### Exercise 3

    **Prove that: (Eisenstein for domains) Let $A$ be a domain with $1$. Let $f = a_0 + a_1 x + \dots + a_n x^n$ be a polynomial in $A[x]$. If there exists a prime ideal $P$ such that**:

    1. **$a_n$ does not belong to $P$**;
    2. **$a_i$ belongs to $P$ for all $i < n$**;
    3. **$a_0$ does not belong to $P^2$**.

    **Then $f$ cannot be written as product of polynomials of lower degree. In particular, if $f$ is not a multiple of a constant polynomial, then $f$ is irreducible**.

    Proof

    Suppose $f = g h$ where $g = \sum\limits_{i = 0}^{m\prime < n} g_i x^i, h = \sum\limits_{j = 0}^{m\prime\prime < n} h_j x^j \in A[x]$. Set $D \overset{\text{def}}{=} A/P$, since $P$ is prime, $D$ is a domain. Consider $\overline{f}$ over $D$, then for each $a_i, i<n, a_i \in P \implies a_i \equiv 0 \implies \overline{f} = \overline{a_n}x^n$.

    On the other hand, $\overline{f} = \overline{g} \overline{h} = (\sum\limits_{i = 0}^{m\prime} \overline{g_i}x^i)(\sum\limits_{j = 0}^{m\prime\prime} \overline{h_j}x^j) = \sum\limits_{m = 0}^{n} (\sum\limits_{i + j = m} \overline{g_i h_j}x^m) \implies \overline{g_0} = 0$ and $\overline{h_0} = 0$, i.e. $\overline{g}, \overline{h}$ have zero constant term, i.e. the constant terms $g_0, h_0$ of them are both in $P$. But then $f_0 = g_0 h_0 \in P^2$, which is a contradiction.

    The last part (In particular…) follows immediately: such $f$ can be only written as $f = cf'$ (where $f'$ has the same degree with $f$) otherwise we cannot factor it anymore.

    ### Exercise 4

    **Let $p$ be a prime. Factor the polynomial $f = x^{p-1}-1$ in $\mathbb{Z}_p[x]$**.

    Solution

    By Fermat's little theorem $x = 1, \dots, p - 1$ are solutions (and obviously they are distinct) for $f$. Since $f$ is a polynomial of degree $p-1$ it has at most $p-1$ solutions. In other word, $x = 1, \dots, p - 1$ are exact these $p - 1$ solutions.

    Thus we can factor $f$ as $f = (x - 1)(x - 2) \dots(x - p + 1)$ in $\mathbb{Z}_p[x]$.

    ### Exercise 5

    **Is $x^3 + 2$ irreducible in $\mathbb{Z}_7[x]$**?

    Solution

    The degree is only $3$ so it suffices to check if it has root(s) in $\mathbb{Z}_7$:

    1. $0^3 + 2 = 2 \equiv 2$;
    2. $1^3 + 2 = 3 \equiv 3$;
    3. $2^3 + 2 = 10 \equiv 3$;
    4. $3^3 + 2 = 29 \equiv 1$;
    5. $4^3 + 2 = 66 \equiv 3$;
    6. $5^3 + 2 = 127 \equiv 1$;
    7. $6^3 + 2 = 218 \equiv 1$.

    It admits no roots, thus it is irreducible.
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
    ## Section 7.5

    ### Exercise 1

    **Let $p$ be a prime number, is there a field $K$ such that $\mathbb{Q} \subset K \subset \mathbb{Q}[\sqrt[p]{2}]$**?

    Solution

    It is clear that $\sqrt[p]{2}$ is algebraic over $\mathbb{Q}$, because it is (a) root for $x^p-2$. Thus by Theorem 369 we have that $\mathbb{Q}[\sqrt[p]{2}] = \mathbb{Q}(\sqrt[p]{2})$ is by definition the smallest (sub-)field containing both $\mathbb{Q}$ and $\sqrt[p]{2}$, also clearly $deg(\sqrt[p]{2}) = p$.

    If there is a field $K$ with $\mathbb{Q} \subseteq K \subseteq \mathbb{Q}[\sqrt[p]{2}]$, by Lagrange we have $[\mathbb{Q}[\sqrt[p]{2}]:\mathbb{Q}] = p = [\mathbb{Q}[\sqrt[p]{2}]:K][K:\mathbb{Q}]$, since $p$ is prime, either $[\mathbb{Q}[\sqrt[p]{2}]:K] = 1$ or $[K:\mathbb{Q}] = 1$, which means either $\mathbb{Q}[\sqrt[p]{2}] = K$ or $K = \mathbb{Q}$. In other words, there is no $K$ strictly in between $\mathbb{Q}[\sqrt[p]{2}]$ and $\mathbb{Q}$.

    ### Exercise 2

    **Prove that $\mathbb{Q}(\sqrt{3}+i) = \mathbb{Q}(\sqrt{3},i)$ and find the minimal polynomial of $\sqrt{3}+i$ over $\mathbb{Q}$**.

    Proof

    If a field contains both $\sqrt{3}$ and $i$ it clearly contains $\sqrt{3}+i$, so $\mathbb{Q}(\sqrt{3}+i) \subseteq \mathbb{Q}(\sqrt{3},i)$.

    If a field $F$ contains $\sqrt{3} + i$, then it must contain $\sqrt{3} + i$ rise to the power $3$, which is exactly $8i$, now $8$ is clearly invertible in $\mathbb{Q}$, thus $F$ contains $i$, and thus $\sqrt{3}$, so $\mathbb{Q}(\sqrt{3}+i) \supseteq \mathbb{Q}(\sqrt{3},i)$ and thus the equality holds.

    Starting with something simple: it is easy to verify that $(\sqrt{3}+i)^6 = -64$, which is clearly a rational number. So $x^6+64$ is a polynomial in $\mathbb{Q}[x]$ with $\sqrt{3}+i$ as root. Now we want to see if we can factor it: notice $x^6+64 = (x^2)^3+4^3 = (x^2+4)(x^4 - 4x^2 + 16)$. So $x^4 - 4x^2 + 16$ is now a polynomial in $\mathbb{Q}[x]$ with $\sqrt{3}+i$ as root. It is irreducible: clearly it does not have rational roots, and there is no way to factor it to the form $(x^2+ax+b)(x^2+cx+d)$ with $a,b,c,d$ in $\mathbb{Q}$. Thus by Proposition 362, $x^4 - 4x^2 + 16$ is the minimal polynomial of $\sqrt{3}+i$ over $\mathbb{Q}$.

    ### Exercise 3

    **Find the minimal polynomial of $\sqrt[3]{7}-1$ over $\mathbb{Q}$**.

    Solution

    Let's check generally how do we proceed $\sqrt[3]{x}-1$:

    Since we have a cubic root it is natural to rise it to power $3$ first: we have $x - 3x^{2/3} + 3x^{1/3} - 1$. Now we get rid of the $x^{2/3}$ term by adding $3(\sqrt[3]{x}-1)^2$ to it, we will get $x - 3x^{1/3} + 2$. Now it is easy: adding $3(\sqrt[3]{x}-1)$ to it and we will have something rational leftover: $x-1$.

    Now, for our case:

    Going backwards (and plug in $x = 7$) we will get that $y^3+3y^2+3y-6$ is a rational polynomial with $\sqrt[3]{7}-1$ as root. Since it is a polynomial of degree $3$ it is easy to check that it has no rational root thus irreducible. Thus $y^3+3y^2+3y-6$ is the minimal polynomial of $\sqrt[3]{7}-1$ over $\mathbb{Q}$.

    ### Exercise 4

    **Find the minimal polynomial of $\sqrt[3]{3}-\sqrt[3]{9}$ over $\mathbb{Q}$**.

    Solution

    Notice that we can re-write $\sqrt[3]{3}-\sqrt[3]{9}$ as $3^{1/3}-3^{2/3}$.Replace $3$ with $x$.

    Proceed as before, rise it to power $3$ we have $(x^{1/3})^3 - 3 (x^{1/3})^2 x^{2/3} + 3 x^{1/3} (x^{2/3})^2 - (x^{2/3})^3 = x-3x^{4/3}+3x^{5/3}-x^2$, now we can add $3x(x^{1/3}-x^{2/3})$ to it to have $x-x^2$.

    Again, go backwards and plugin $x = 3$, we get $x^3+9x+6$ is a polynomial in $\mathbb{Q}$ with root $\sqrt[3]{3}-\sqrt[3]{9}$. It does not have rational root so it is irreducible. Thus $x^3+9x+6$ is the minimal polynomial we want.

    ### Exercise 6

    **Prove that $[\overline{\mathbb{Q}}(\pi):\overline{\mathbb{Q}}]$ is infinite**.

    Proof

    Suppose that $[\overline{\mathbb{Q}}(\pi):\overline{\mathbb{Q}}] = d$. By Theorem 373, it means that there is a polynomial $a_0 + a_1x^1 + \dots + a_dx^d$ with $a_i \in \overline{\mathbb{Q}}$ and $a_0 + a_1\pi^1 + \dots + a_d\pi^d = 0$.

    Since $a_i \in \overline{\mathbb{Q}}$, $a_i$ is algebraic over $\mathbb{Q}$, it follows that $\pi$ is algebraic over $\mathbb{Q}(a_0,\dots,a_d)$. But then $[\mathbb{Q}(\pi,a_0,\dots,a_d):\mathbb{Q}]$, which equals to $[\mathbb{Q}(\pi,a_0,\dots,a_d):\mathbb{Q}(a_0,\dots,a_d)][\mathbb{Q}(a_0,\dots,a_d):\mathbb{Q}]$, is finite, thus $\pi$ is algebraic over $\mathbb{Q}$, which is a contradiction.

    ### Exercise 8

    **Prove that there are $p(p-1)/2$ monic irreducible quadratic polynomials in $\mathbb{Z}_p[x]$**.

    Proof

    For each $1<p \in \mathbb{N}$, there are $p\cdot p$ many distinct monic quadratic polynomials in total. So it is the same to show there are $p^2 - p(p-1)/2 = p(p+1)/2$ reducible quadratic polynomials.

    For each $p$, clearly $x+c, 0 \le c < p, c \in \mathbb{Z}$ are the only (irreducible) monic polynomial with degree $1$. If a monic quadratic polynomial may be factorized, it must be factored into two monic degree $1$ polynomials. But there are exactly $1+2+\dots+p = p(1+p)/2$ distinct ways to combine the monic degree $1$ polynomials.

    For example in $\mathbb{Z}_3$, $x+0, x+1, x+2$ are the only monic degree $1$ polynomials, thus the possible monic reducible quadratic polynomials are $(x+0)(x+0)$, $(x+0)(x+1)$, $(x+0)(x+2)$, $(x+1)(x+1)$, $(x+1)(x+2)$, and $(x+2)(x+2)$. There are $3+2+1$ of them.
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
    ## Section 8.9

    ### Exercise 1

    **In $GL_2(\mathbb{R})$, what is the period of the element $a = \begin{pmatrix} 1&1\\-1&0 \end{pmatrix}$**?

    Solution

    Calculate that: $a^1 = \begin{pmatrix} 1&1\\-1&0 \end{pmatrix}$; $a^2 = \begin{pmatrix} 0&1\\-1&-1 \end{pmatrix}$; $a^3 = \begin{pmatrix} -1&0\\0&-1 \end{pmatrix}$.

    And now it is clear we would get $a^6 = I$ being the identity, and we would not get it earlier ($4,5$ not divisor of $6$) thus period is $6$.

    ### Exercise 2

    **Is the multiplicative group of non-zero real numbers isomorphic to the additive group of all real numbers**?

    Solution

    Let $f$ be a group homomorphism between $G = (\mathbb{R}-\lbrace 0 \rbrace,\times)$ and $H = (\mathbb{R}, +)$. We know that $f$ maps identity to identity, so $f(1) = 0$, but by definition of a homomorphism, $f(ab) = f(a)+f(b)$, and we have $-1\cdot -1 = 1 \implies f(-1)+f(-1) = f(-1\cdot -1) = f(1) = 0$, but then $f$ is not injective, so there is no $f$ being isomorphism. Indeed, however, the multiplicative group of positive real numbers is isomorphic to the additive group of all real numbers.

    ### Exercise 5

    **Let $x,y$ be two group elements such that $x^{2018} = y^{2019}$ and $xyx=yxy$, prove that $x = y = e$**.

    Proof

    $xyx = yxy$, multiple both side $y^{-1}x^{-1}$ to the right we have:

    $xyxy^{-1}x^{-1} = y$ ($*$).

    Take square of ($*$) we have $y^2 = xyxy^{-1}x^{-1}xyxy^{-1}x^{-1} = xyx^2y^{-1}x^{-1}$;

    Take cube of ($*$) we have $y^3 = xyx^2y^{-1}x^{-1}xyxy^{-1}x^{-1} = xyx^3y^{-1}x^{-1}$;

    Similarly we can see $y^{2019} = x^{2018} = xyx^{2019}y^{-1}x^{-1}$, thus $x^{-1}x^{2018}x = x^{2018} = y^{2019} = yx^{2019}y^{-1}$, similarly $y^{-1}y^{2019}y = y^{2019} = x^{2019}$.

    But then $y^{2019} = x^{2018}x = y^{2019}x$ thus $x = e$.

    Plug into $xyx=yxy$ we have $y = yy$ thus $y = e$ as well.

    ### Exercise 10

    **Let $G$ be a group where $x^2 = e$ for all $x \in G$, prove that $G$ is abelian**.

    Proof

    For any $x, y$ in $G$, since $G$ is a group, clearly $xy \in G$, thus $(xy)(xy) = e$ by construction. Which means $xy$ is the inverse of $xy$.

    On the other hand, consider $(xy)(yx) = x(yy)x = xx = e$, thus $yx$ is the inverse of $xy$ as well.

    We know in a group, inverse is unique, thus $xy = yx$, i.e. $G$ is abelian.

    ### Exercise 11

    **Let $G$ be a group with $2p$ elements with $p$ prime, prove that $G$ contains a subgroup with $13$ elements**.

    Proof

    By Cauchy, there exists $g \in G$ with $\pi(g) = p$, now $\langle g \rangle$ is a subgroup of $G$ and has exactly $p$ elements.
    """
    )
    return


if __name__ == "__main__":
    app.run()
