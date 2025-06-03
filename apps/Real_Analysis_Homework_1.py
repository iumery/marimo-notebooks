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
    ## Exercise 2

    **Prove an analogue of Theorem 1.8 for $n$ functions**.

    Proof

    The statement we want to prove:

    Let $u_1,u_2,\dots,u_n$ be $n$ real measurable functions on a measurable space $X$, $Y$ be some topological space, let $\Phi$ be a continuous mapping of $\mathbb{R}^n \to Y$. Define $h(x) = \Phi(u_1(x),\dots,u_n(x))$ for $x \in X$, then $h:X\to Y$ is measurable.

    Let $f(x) = (u_1(x),\dots,u_n(x))$ then $h = \Phi \circ f$, if $f$ is measurable then $h$ is measurable:

    Let $R$ be an arbitrary $n$ dimension rectangle in the form $R = I_1 \times I_2 \times \dots \times I_n$, then $f^{-1}(R)= u_1^{-1}(I_1) \cap \dots\cap u_n^{-1}(I_n)$ (if $x \in f^{-1}(R)$ then $f(x) \in R$ then $u_1(x) \in I_1,\dots,u_n(x) \in I_n$ then $x \in u_1^{-1}(I_1),\dots,x \in u_n^{-1}(I_n)$ thus $x$ is in the intersection, similar the other way around).

    So $f^{-1}(R)$ is measurable because it is a finite intersection of measurable set. Since the $n$-rectangles form a basis for $\mathbb{R}^n$, any $V$ open in $\mathbb{R}^n$ (which is second countable) is a countable union of such $R$'s, so we can write $f^{-1}(V) = f^{-1}(\bigcup\limits_{i = 1}^{\infty}R_i) = \bigcup\limits_{i = 1}^{\infty}f^{-1}(R_i)$ is a countable union of measurable sets thus is measurable.

    Since $V$ can be chose arbitrarily, $f$ thus $h$ is measurable.

    ## Exercise 3

    **Prove that if $f$ is a real function on a measurable space $X$ such that $\lbrace x:f(x) \ge r\rbrace$ is measurable for every rational $r$, then $f$ is measurable**.

    Proof

    By taking set subtraction we can see that $\lbrace x:a\le f(x) <b \rbrace$ is measurable for any rational $a,b$. Every open interval in $\mathbb{R}$ can be written as a countable union of half-open intervals of the form $[a,b),a,b\in\mathbb{Q}$, and every open set in $\mathbb{R}$ can be written as a countable union of open intervals, i.e. $\lbrace x : f(x) \in U\rbrace$ is measurable for any $U$ open in $\mathbb{R}$, meaning $f$ is measurable.

    ## Exercise 4

    **Let $\lbrace a_n\rbrace$ and $\lbrace b_n\rbrace$ be sequences in $[-\infty,\infty]$, and prove the following assertions**:

    1. **$\limsup_{n\to\infty}(-a_n) = -\liminf_{n\to \infty}a_n$**;
    2. **$\limsup_{n\to\infty}(a_n+b_n) \le \limsup_{n\to\infty}(a_n) + \limsup_{n\to\infty}(b_n)$ provided none of the sums is of the form $\infty - \infty$**;
    3. **If $a_n \le b_n$ for all $n$, then $\liminf_{n\to \infty}a_n \le \liminf_{n\to \infty}b_n$**.

    **Show by an example that strict inequality can hold in 2**.

    Proof

    1. $\liminf a_n$ $\overset{\text{def}}{=} \lim\limits_{k \to \infty}\inf\limits_{n>k}a_n$ $= \lim\limits_{k \to \infty}(-\sup\limits_{n>k}(-a_n))$ $\overset{\text{def}}{=} -\limsup(-a_n)$ (if $b$ is a lower bound of $a_n$ then $-b$ is an upper bound of $-a_n$ because $b \le a_n \implies -a_n \le -b_n$);
    2. Consider the inequality $\sup\limits_{n > k}a_n + \sup\limits_{n > k}b_n \ge a_l + b_l$ for any $l > k$, thus by definition $\sup\limits_{n > k}a_n + \sup\limits_{n > k}b_n$ is an upper bound for $a_n + b_n$ thus we have $\sup\limits_{n > k}a_n + \sup\limits_{n > k}b_n \ge \sup\limits_{n > k}(a_n + b_n)$. Now pass limit each side, we have $\limsup{(a_n + b_n)} \le \limsup{(a_n)} + \limsup{(b_n)}$ (as long as we do not have the undefined form $\infty-\infty$);
    3. If $a_n \le b_n$ for all $n$ then any lower bound for $a_n$'s is a lower bound for $b_n$'s, i.e. $\inf\limits_{n>k}a_n \le \inf\limits_{n>k}b_n$, now pass limit we have $\liminf_{n\to \infty}a_n \le \liminf_{n\to \infty}b_n$.

    For example if $\lbrace a_n\rbrace = -1,1,-1,1,\dots$ and $\lbrace b_n\rbrace = 1,-1,1,-1,\dots$ then $a_n+b_n \equiv 0$ so $\limsup(a_n+b_n) = 0$, yet $\limsup(a_n) = \limsup(b_n) = 1$.

    ## Exercise 5

    1. **Suppose $f:X\to [-\infty,\infty]$ and $g:X\to [-\infty,\infty]$ are measurable. Prove that the sets $\lbrace x:f(x) < g(x)\rbrace,\lbrace x:f(x) = g(x)\rbrace$ are measurable**;
    2. **Prove that the set of points at which a sequence of measurable real-valued functions converges to a finite limit is measurable**.

    Proof

    1. Since $f, g$ are measurable, so is $f-g:X\to [-\infty,\infty]$, so $\lbrace x:f(x) < g(x)\rbrace = (f-g)^{-1}([-\infty,0))$ is preimage of open set is measurable. Thus $\lbrace x:f(x) \ge g(x)\rbrace = \lbrace x:f(x) < g(x)\rbrace^c$ is measurable; interchange the role of $f,g$ we get $\lbrace x:f(x) \le g(x)\rbrace$ is measurable, so $\lbrace x:f(x)= g(x)\rbrace$ $= \lbrace x:f(x) \ge g(x)\rbrace \cap \lbrace x:f(x) \le g(x)\rbrace$ is measurable;
    2. If I understand this right the question is asking to show $\lbrace x: \lim\limits f_n(x)$ exists and finite $\rbrace$ is measurable. Notice that $f_n$ converge if and only if $\limsup f_n = \liminf f_n$ and we proved that if $\lbrace f_n\rbrace$ is a sequence of measurable function then $\limsup f_n$ and $\liminf f_n$ are measurable, so $\lbrace x: \lim\limits f_n(x)$ exists $\rbrace$ $=\lbrace x: \limsup f_n(x) = \liminf f_n(x)\rbrace$ is measurable by part 1. Now notice that $(-\infty, \infty]$ and $[-\infty,\infty)$ are open, so taking preimage and intersection with the above set and we get the desired statement.

    ## Exercise 6

    **Let $X$ be an uncountable set, let $M$ be the collection of all sets $E \subseteq X$ such that either $E$ or $E^c$ is at most countable, and define $\mu(E) = 0$ in the first case, $\mu(E) = 1$ in the second. Prove that $M$ is a $\sigma$-algebra in $X$ and that $\mu$ is a measure on $M$. Describe the corresponding measurable functions and their integrals**.

    Proof

    $M$ is a $\sigma$-algebra:

    1. $X^c = \varnothing$ is finite so $X \in M$;
    2. If $A \in M$ then either $A = (A^c)^c$ is at most countable or $A^c$ is at most countable, which by definition means $A^c \in M$;
    3. If $A = \cup A_i$ and $A_i \in M$ for all $i$:
    	1. If $A_i$ countable for all $i$ then $A$ is countable thus in $M$;
    	2. If for at least one $i$, $A_i \in M$ because $A_i^c$ is countable, WLOG say $A_1^c$ is countable, then $A^c = (\cup A_i)^c = \cap A_i^c \subseteq A_1^c$ so $A^c$ is at most countable, thus $A \subset M$.

    $\mu$ is a measure on $M$:

    1. The range of $\mu$ is clearly in $[0,\infty]$ and $\mu$ is non-trivial;
    2. Suppose $\lbrace A_i\rbrace$ is a disjoint countable collection of members of $M$, then at most one of $A_i$ is in $M$ because $A_i^c$ is countable (if $A_1^c$ and $A_2^c$ are both countable, since $A_1,A_2$ are disjoint, $A_1 \subset A_2^c$, we have a contradiction because we assumed $A_1$ is uncountable).
    	Now it is easy to see that if one $A_i^c$ is countable then $\mu(\cup A_i) = 1 = \sum \mu(A_i)$ and if no $A_i^c$ is countable then $\mu(\cup A_i) = 0 = \sum \mu(A_i)$, so in either case we have countably additive.

    Suppose now $f:X\to \mathbb{R}$ is a measurable function. For any $a \in \mathbb{R}$, since the set $\lbrace a\rbrace$ can be written as intersection of countably many open sets (i.e. it is a $G_{\delta}$, in particular, it is a Borel set), so $f^{-1}(a) = E$ is in $M$ by Theorem 1.12, now:

    1. Suppose this $E$ is uncountable, then $E^c$ is at most countable. We can see that $\int_X f d\mu = \int_Esd\mu$ where $s$ takes value $a$ on $E$ and any value on $E^c$. In other words, as long as there is one $a$ such that its preimage is uncountable, the integral of $f$ over $X$ is $a$;
    2. Suppose then for any $a \in \mathbb{R}$, $f^{-1}(a) = E_a$ is countable, then we can write $X = \bigcup\limits_{a \in \mathbb{R}}E_a = \sqcup_{a \in \mathbb{R}}E_a$ (disjoint because otherwise $f$ is not a function), by removing all empty $E_a$ we get $X = \sqcup_{a \in I}E_a$. Since $E_a$'s are all countable yet $X$ is uncountable, there must be uncountably many such $a$, i.e. $f(X) \subseteq \mathbb{R}$ is uncountable. Choose some $a$ such that $f(X) \cap (-\infty,a)$ and $f(X) \cap (a,\infty)$ are both uncountable, then $f^{-1}(-\infty,a)$ and $f^{-1}(a,\infty)$ are both uncountable, measurable and disjoint, we proved above that this cannot happen.

    ## Exercise 7

    **Suppose $f_n:X\to [0,\infty]$ is measurable for $n = 1,2,3,\dots$, $f_1 \ge f_2 \ge f_3\ge \dots \ge 0$, $f_n(x) \to f(x)$ as $n \to \infty$ for every $x\in X$, and $f_1 \in L^1(\mu)$. Prove that then $\lim\limits_{n\to \infty}\int_Xf_nd\mu = \int_Xfd\mu$ and show that this conclusion does not follow if the condition $f_1 \in L^1(\mu)$ is omitted**.

    Proof


    This is an immediate result of the Lebesgue Dominated Convergence Theorem.

    Consider $X = [0,\infty)$ and $\mu$ be the Lebesgue measure. Consider the sequence of functions:

    1. $f_1 = 1\chi_{[0,1)}+\frac{1}{2} \chi_{[1,2)}+\frac{1}{3}\chi_{[2,3)}+\dots$;
    2. $f_2 = \frac{1}{2}\chi_{[0,1)}+\frac{1}{4} \chi_{[1,2)}+\frac{1}{6}\chi_{[2,3)}+\dots$;
    3. $f_3 = \frac{1}{3}\chi_{[0,1)}+\frac{1}{6} \chi_{[1,2)}+\frac{1}{9}\chi_{[2,3)}+\dots$;
    4. $\dots$

    Each $f_n$ is measurable and $f_1\ge f_2\ge \dots$. It is easy to see $f_n \to 0$.

    We know that $\sum\limits_{n=1}^{\infty}\frac{1}{n} = \infty$, thus $\int_Xf_nd\mu = \infty$ for any $n$ (so in particular, $f_1$ is not $L^1$), and so does its limit. On the other hand, $\int_X 0 d\mu = 0 \ne \infty$.

    ## Exercise 8

    **Put $f_n = \chi_E$ if $n$ is odd, $f_n = 1-\chi_E$ if $n$ is even. What is the relevance of this example to Fatou's lemma**?

    Solution

    For example, consider $X = [0,1]$, $E = [0,1/2]$ with the Lebesgue measure, then $\int_X f_{odd}d\mu = \int_X f_{even}d \mu = 1/2$ so $\liminf \int_X f_n d\mu = 1/2$. On the other hand for each $x \in X$, $\liminf f_n(x) = 0$ thus $\int_X (\liminf f_n)d\mu = 0$ so we have strict inequality.

    ## Exercise 9

    **Suppose $\mu$ is a positive measure on $X$, $f:X\to [0,\infty]$ is measurable, $\int_Xfd\mu = c$ where $0 <c<\infty$, and $\alpha$ is a constant. Prove that $\lim\limits_{n\to \infty}\int_Xn\log[1+(f/n)^{\alpha}]d\mu = \begin{cases}\infty,&0<\alpha<1\\c,&\alpha = 1\\0,&1<\alpha<\infty\end{cases}$**.

    Proof

    First notice that $\int_Xfd\mu = c$ implies that $\mu(X) \ne 0$ so the integral is not trivial.

    Suppose $\alpha\ge 1$, if $x = 0$ then $\alpha x = n\log[1+(x/n)^{\alpha}]$, and $(\alpha x - n\log[1+(x/n)^{\alpha}])' = \alpha - \frac{\alpha(x/n)^{\alpha-1}}{(x/n)^{\alpha}+1}>0$ for $x>0$, and any $n\ge 1$, thus we may conclude that $n\log[1+(f/n)^{\alpha}] <\alpha f$.

    Now if $\alpha = 1$ then $\lim\limits_{n\to \infty} n\log[1+(x/n)] = \lim\limits \frac{\log(1+x/n)}{1/n} = \lim\limits \frac{nx}{n+x} = x$ by L'Hospital;

    If $\alpha>1$, similarly we have $\lim\limits_{n\to \infty} n\log[1+(x/n)^{\alpha}] = \lim\limits \frac{-\frac{\alpha(x/n)^{\alpha}}{n+n(x/n)^{\alpha}}}{-1/n^2} = \lim\limits \frac{\alpha n}{(n/x)^{\alpha}+1}$. We can actually see here that if $\alpha>1$ then we can cancel the $n$ on the numerator and get the limit is $0$, while if $\alpha<1$ then we cancel the $n$ on the denominator and the limit is $\infty$.

    So by Dominated Convergence Theorem, we get the parts: $\lim\limits_{n\to \infty}\int_{X}n\log[1+(f/n)^{\alpha}]d\mu = \begin{cases}\int_{X - f^{-1}(\infty)}fd\mu=c,&\alpha = 1\\\int_{X - f^{-1}(\infty)}0d\mu=0,&1<\alpha<\infty\end{cases}$ (notice we integrate over $X - f^{-1}(\infty)$, but it does not really matter because we have the assumption $\int_Xfd\mu = c$ so $\mu(f^{-1}(\infty))$ must be $0$).

    Otherwise if $\alpha<1$, then consider Fatou's Lemma: $\lim\limits_{n\to \infty}\int_Xn\log[1+(f/n)^{\alpha}]d\mu$ $= \liminf_{n\to \infty}\int_Xn\log[1+(f/n)^{\alpha}]d\mu$ $\ge \int_X (\liminf_{n\to \infty}n\log[1+(f/n)^{\alpha}])d\mu = \infty$ because by above we have $\lim\limits_{n\to \infty}n\log[1+(f/n)^{\alpha}] = \infty$ if $\alpha < 1$, and we complete the proof.

    ## Exercise 10

    **Suppose $\mu(X)<\infty$, $\lbrace f_n\rbrace$ is a sequence of bounded complex measurable functions on $X$, and $f_n \to f$ uniformly on $X$. Prove that $\lim\limits_{n \to \infty}\int_Xf_nd\mu = \int_Xfd\mu$ and show that the hypothesis $\mu(X) <\infty$ cannot be omitted**.

    Proof

    Since we have uniform convergence, for $\varepsilon$ choose $N$ such that $| f_N(x) - f(x) | < 1 \implies | f(x) | < | f_N(x) | + 1$ for all $x \in X$, so $\int_X | f | d\mu$ $<\int_X | f_N(x) | d\mu+ \int_X 1d\mu$ $=\int_X | f_N(x) | d\mu + \mu(X)$ $<\infty$ by the assumptions, so $f$ is also $L^1$.

    For each $n$, $| \int_X f_n d\mu - \int_X f d\mu |$ $\le \int_X | f_n-f | d\mu$ $\le \int_X\sup\limits_{x}(| f_n-f |)d\mu$ $=\sup\limits_{x}(| f_n-f |)\mu(X)$. If we pass limit then by definition of uniform convergence $\lim\limits_{n\to \infty}\sup\limits_{x}(| f_n-f |) = 0$, thus we have $\lim\limits | \int_X f_n d\mu - \int_X f d\mu | = 0$ $\implies \lim\limits \int_Xf_nd\mu = \int_Xfd\mu$.

    The example from exercise 7 also works here:

    Consider $X = [0,\infty)$ and $\mu$ be the Lebesgue measure, then we do not have $\mu(X) < \infty$. Consider the sequence of functions:

    1. $f_1 = 1\chi_{[0,1)}+\frac{1}{2} \chi_{[1,2)}+\frac{1}{3}\chi_{[2,3)}+\dots$;
    2. $f_2 = \frac{1}{2}\chi_{[0,1)}+\frac{1}{4} \chi_{[1,2)}+\frac{1}{6}\chi_{[2,3)}+\dots$;
    3. $f_3 = \frac{1}{3}\chi_{[0,1)}+\frac{1}{6} \chi_{[1,2)}+\frac{1}{9}\chi_{[2,3)}+\dots$;
    4. $\dots$

    We know that $\sum\limits_{n=1}^{\infty}\frac{1}{n} = \infty$, thus $\int_Xf_nd\mu = \infty$ for any $n$, and so does its limit. On the other hand, for any $\varepsilon>0$, choose $N$ large enough so that $1/N<\varepsilon$, then for any $n>N$, $| f_n(x) - 0 | < \varepsilon$, so $f_n$ converges uniformly to $0$, but $\int_X 0 d\mu = 0 \ne \infty$.

    ## Exercise 11

    **Show that $A = \bigcap\limits_{n = 1}^{\infty}\bigcup\limits_{k = n}^{\infty}E_k$ in Theorem 1.41, and hence prove the theorem without any reference to integration.**

    Proof

    ($A$ is defined to be the set of all $x$ which lie in infinitely many $E_k$ where $E_k$ is a sequence of measurable sets in $X$)

    Suppose $x\in A$, then $x\in E_k$ for infinitely many $k$, namely $k_1<k_2<\dots$. We must have $k_1\ge 1, k_2\ge 2, \dots$, so $x \in E_{k_1} \implies x\in \bigcup\limits_{k=1}^{\infty}E_k$, $x \in E_{k_2} \implies x\in \bigcup\limits_{k=2}^{\infty}E_k$, $\dots$, so $x$ is in the intersection.

    For the other inclusion, suppose $x\in \bigcap\limits_{n = 1}^{\infty}\bigcup\limits_{k = n}^{\infty}E_k$, then $x \in \bigcup\limits_{k = n}^{\infty}E_k$ for each $n$. Suppose $x\in \bigcup\limits_{k = 1}^{\infty}E_k$ because $x \in E_{k_1}$, then in order for $x$ to lie in $\bigcup\limits_{k = k_1+1}^{\infty}E_k$, we need to have $x \in E_{k_2}$ for some $k_2>k_1$. Continue and we have a sequence $k_1<k_2<\dots$ and $x$ lies in all of $E_{k_i}$'s, thus by definition $x \in A$.

    Now by the assumption we have $\mu(E_k) \to 0$, thus $\mu(\bigcup\limits_{k=n}^{\infty}E_k) \to 0$ and $\mu(A) = 0$, and the theorem is proved.

    ## Exercise 12

    **Suppose $f \in L^1(\mu)$. Prove that to each $\varepsilon>0$ there exists a $\delta>0$ such that $\int_E| f | d\mu < \varepsilon$ whenever $\mu(E) < \delta$**.

    Proof

    Fix some $\varepsilon>0$.

    For any (integer) $n$ we may write $\int_E | f | d\mu \le n\mu(E)+ \int_{| f |^{-1}(n,\infty)\cap E}| f | d\mu$.

    First we look at the second part $\int_{| f |^{-1}(n,\infty)\cap E}| f | d\mu$. For different values of $n$ we can see the integrals as integrals of a sequence $f_n$ (which is now nonnegative) over $E$, where each $f_n = f$ if $f(x)>n$ and $=0$ otherwise, then $\lim\limits_{n\to \infty}f_n(x) = 0$ for any $x \in E$ and $| f_n(x) | = f_n(x)$ is less than or equal to the original $| f(x) |$ which is $L^1$ by the assumption, so we can apply the Lebesgue Dominated Convergence Theorem and see that $\lim\limits_{n\to \infty}\int_E f_n d\mu = 0$. By definition of a limit, we can find large enough $n$ so that $\int_{| f |^{-1}(n,\infty)\cap E}| f | d\mu = \int_Ef_nd\mu < \varepsilon/2$.

    For such $n$, assign $\delta = \varepsilon/(2n)$, this is a $\delta$ we are looking for: as long as $\mu(E) < \delta$ we will have $\int_E | f | d\mu \le n\mu(E)+ \int_{| f |^{-1}(n,\infty)\cap E}| f | d\mu < \varepsilon/2+\varepsilon/2 = \varepsilon$.

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
    ## Exercise 1

    **Let $\lbrace f_n\rbrace$ be a sequence of real nonnegative functions on $\mathbb{R}$, and consider the following four statements**:

    1. **If $f_1$ and $f_2$ are upper semicontinuous, then $f_1+f_2$ is upper semicontinuous**;
    2. **If $f_1$ and $f_2$ are lower semicontinuous, then $f_1+f_2$ is lower semicontinuous**;
    3. **If each $f_n$ is upper semicontinuous, then $\sum\limits_1^{\infty}f_n$ is upper semicontinuous**;
    4. **If each $f_n$ is lower semicontinuous, then $\sum\limits_1^{\infty}f_n$ is lower semicontinuous**.

    **Show that three of these are true and that one is false. What happens if the word "nonnegative" is omitted? Is the truth of the statements affected if $\mathbb{R}$ is replaced by a general topological space**?

    Solution

    For the first part, the answer will be that 1,2,4 true and 3 false; so I will answer in this order to illustrate why 3 is false.

    Let $a$ be an arbitrary real number:

    1. The set $\lbrace x| (f_1+f_2)(x) < a \rbrace$ can be written as $= \bigcup\limits_{b \in \mathbb{R}}(\lbrace x | f_1(x) < b\rbrace \cap \lbrace x | f_2(x) < a - b \rbrace)$, the union can be taken over $b \in \mathbb{Q}$ instead: $= \bigcup\limits_{b \in \mathbb{Q}}(\lbrace x | f_1(x) < b\rbrace \cap \lbrace x | f_2(x) < a - b \rbrace)$, this is a countable union of finite intersection of open sets thus open, and thus $f_1+f_2$ is upper semicontinuous;
    2. The idea is the same, write $\lbrace x| (f_1+f_2)(x) > a \rbrace$ as $= \bigcup\limits_{b \in \mathbb{Q}}(\lbrace x | f_1(x) > b\rbrace \cap \lbrace x | f_2(x) > a - b \rbrace)$ and realize this is a countable union of finite intersection of open sets thus open, and thus $f_1+f_2$ is lower semicontinuous;
    3. (part 4) For each positive integer $n$, write $\lbrace x| (f_1+\dots + f_n)(x) > \alpha \rbrace$ as $= \bigcup\limits_{b_1,\dots,b_{n-1} \in \mathbb{Q}}(\lbrace x | f_1(x) > b_1 \rbrace \bigcap\limits$ $\dots \cap \lbrace x | f_{n-1}(x) > b_{n-1} \rbrace$ $\cap \lbrace x | f_n(x) > a - (b_1 + \dots + b_{n-1}) \rbrace)$. So we can see that $f_1 + \dots + f_n$ is lower semicontinuous. Write $\sum\limits_1^{\infty}f_n$ $=\lim\limits_{n\to \infty}(f_1 + \dots + f_n)$ and use the assumption that the functions are all non-negative, we can continue writing $= \sup\limits_n (f_1 + \dots + f_n)$. We may conclude using the fact that supremum of lower semicontinuous function is lower semicontinuous;
    4. (part 3) The above argument doesn't work with upper semicontinuous because of the last few steps: with the non-negative assumption, apparently the limit $\lim\limits_{n\to \infty}(f_1 + \dots + f_n)$ is in general not the infimum $= \inf\limits_n (f_1 + \dots + f_n) = f_1$. To see the statement is indeed not true, consider the series of functions $f_n = \chi_{[\frac{1}{n+1},\frac{1}{n}]}$ so that each $f_n$ is upper semicontinuous yet the infinite summation $\sum f_n = \chi_{(0,1]}$ is not.

    If we lift the assumption of non-negative, part 1,2 won't be affect because we never use this assumption. part 3 is of course still false, and from the construction of the counterexample for it, we should be able to see that the non-negative assumption is crucial for part 4. Here is a counterexample:

    Let $f_n$ be $\chi_{(\frac{1}{n+1},\frac{1}{n})}$ if $n$ is odd, and $-\chi_{[\frac{1}{n+1},\frac{1}{n}]}$ if $n$ is even. Then for any $-1<a<0$, $\lbrace x | \sum f_n > a\rbrace$ $= \lbrace x | \sum f_n = 0\rbrace \cup \lbrace x | \sum f_n = 1\rbrace$ $=(-\infty,0] \cup (1/3,1/2) \cup (1/5,1/4) \cup \dots$ is not open.

    This argument depends on the fact that codomain $\mathbb{R}$ is separable (having a countable dense subset $\mathbb{Q}$), but not the domain. As long as $f$ are still real valued functions (i.e. codomain not changing), the choice of the domain is not important.

    ## Exercise 2

    **Let $f$ be an arbitrary complex function on $\mathbb{R}$, and define $\varphi(x,\delta) = \sup\limits\lbrace | f(s) - f(t) |:s,t \in(x-\delta,x+\delta)\rbrace$, $\varphi(x) = \inf\lbrace \varphi(x,\delta): \delta>0\rbrace$. Prove that $\varphi$ is upper semicontinuous, that $f$ is continuous at a point $x$ if and only if $\varphi(x) = 0$, and hence that the set of points of continuity of an arbitrary complex function is a $G_{\delta}$**.

    **Formulate and prove an analogous statement for general topological spaces in place of $\mathbb{R}$**.

    Proof

    1. $\varphi$ is upper semicontinuous:
    	First notice that by construction, $\varphi(x,\delta) < \varphi(x,\delta')$ whenever $\delta < \delta'$; thus $\varphi(x) = \inf\lbrace \varphi(x,\delta):\delta > 0\rbrace = \lim\limits_{\delta \to 0}\varphi(x,\delta)$.
    	Let $a \in \mathbb{R}$ and consider the set $A = \lbrace x | \varphi(x) < a \rbrace$, we want to show this set is open. If $A$ is empty then it is automatically true, otherwise let $x_0 \in A$, it suffices to find a neighborhood of $x_0$ contained in $A$.
    	We have $a> \varphi(x_0) = \lim\limits_{\delta \to 0} \varphi(x_0,\delta)$. Pick an $\delta_0$ so that $\varphi(x_0,\delta_0) < a$, then $N(x_0) = (x_0 - \delta_0/2, x_0 + \delta_0/2)$ is a neighborhood of $x_0$ we want:
    	Suppose $x_1 \in N(x_0)$, then $$\begin{aligned}\varphi(x_1) =& \lim\limits_{\delta\to 0}\varphi(x_1,\delta) \\\le& \varphi(x_1,\delta_0/2)\\=&^{def} \sup\limits\lbrace | f(s) - f(t) |:s,t \in(x_1-\delta_0/2,x_1+\delta_0/2)\rbrace\end{aligned}.$$ Now notice $(x_1-\delta_0/2,x_1+\delta_0/2)$ is entirely contained in $(x_0 - \delta_0, x_0 + \delta_0)$, thus we may continue write $$\begin{aligned}\le&\sup\limits\lbrace | f(s) - f(t) |:s,t \in(x_0-\delta_0,x_0+\delta_0)\rbrace\\=&^{def}\varphi(x_0,\delta_0)\\<&a\end{aligned}$$
    	by our construction. Thus $x_1 \in A$ and thus $N(x_0) \subset A$;
    2. $f$ is continuous at $x$ if and only if $\varphi(x) = 0$:
    	1. ($\implies$) Suppose $f$ is continuous at $x$, then for any $\varepsilon0$ we may find $\delta > 0$ such that $| x - y | < \delta$ implies that $| f(x) - f(y) | < \varepsilon/2$. Use triangle inequality we have $| f(s) - f(t) | < \varepsilon, \forall s,t \in (x - \delta, x + \delta)$; pass supremum we have $\sup\limits\lbrace | f(s) - f(t) |:s,t \in(x-\delta,x+\delta)\rbrace \le \varepsilon$. Thus $\varphi(x)$ $\le \varphi(x,\delta)$ $= \sup\limits\lbrace | f(s) - f(t) |:s,t \in(x-\delta,x+\delta)\rbrace$ $\le \varepsilon$ which means it is $0$;
    	2. ($\impliedby$) Suppose now $\varphi(x) = 0$, then by above we have $\lim\limits_{\delta \to 0}\varphi(x,\delta) = 0$. Thus for any $\varepsilon>0$ we may find $\delta>0$ such that $\varepsilon>\varphi(x,\delta)$ $= \sup\limits\lbrace | f(s) - f(t) |:s,t \in (x-\delta,x+\delta)\rbrace$ by taking $s = x$ we have that $\ge | f(x) -f(t)|$ for any $t \in (x-\delta,x+\delta)$, thus by definition $f$ is continuous at $x$.

    	For the 'hence' statement, by above we know that the set of points of continuity of $f$ is $\lbrace x : \varphi(x) = 0\rbrace$ which can be written as $= \bigcap\limits_{n=1}^{\infty}\lbrace x : \varphi(x) < 1/n\rbrace$. Since $\varphi$ is upper semicontinuous, this is a countable intersection of open sets, i.e. a $G_{\delta}$;
    3. General version statement:
    	Suppose $f:X\to \mathbb{C}$ where $(X,\tau)$ is a topological space, define $\varphi(x,U) = \sup\limits\lbrace | f(s) - f(t) |:s,t \in U\rbrace$, $\varphi(x) = \inf\lbrace \varphi(x,U): U\in \tau, x\in U\rbrace$, then $\varphi$ is upper semicontinuous and $f$ is continuous at a point $x$ if and only if $\varphi(x) = 0$. The proof is pretty much the same:
    	1. $\varphi$ is upper semicontinuous:
    		Let $a \in \mathbb{R}$ and consider the set $A = \lbrace x | \varphi(x) < a \rbrace$. If $A$ is empty then it is empty, otherwise let $x_0 \in A$.
    		We have $a> \varphi(x_0)$, thus we can find $\varepsilon>0$ such that $\varphi(x_0) + \varepsilon < a$. By property of infimum and supremum it follows that there is an $U$ neighborhood of $x_0$ such that $\lbrace | f(s) - f(t) |:s,t \in U\rbrace < a$. In this formulation $x_0$ is not really important and we automatically have $U \subset A$;
    	2. $f$ is continuous at $x$ if and only if $\varphi(x) = 0$:
    		Suppose $f$ is continuous at $x$, then for any $\varepsilon > 0$ we may find $U$ neighborhood of $x$ such that $f(U) \subset B(f(x),\varepsilon)$, thus for any $s,t \in U, | f(s) - f(t) | < 2 \varepsilon$ thus $\varphi(x) < 2 \varepsilon$ thus $\varphi(x) = 0$. It also works the other way around;
    	3. The 'hence' part is still the same, because (as being used above) the codomain of $\varphi$ which is $\mathbb{R}$ is unchanged.

    ## Exercise 3

    **Let $X$ be a metric space, with metric $\rho$. For any nonempty $E \subset X$, define $\rho_E(x) = \inf\lbrace \rho(x,y): y \in E\rbrace$. Show that $\rho_E$ is a uniformly continuous function on $X$. If $A, B$ are disjoint nonempty closed subsets of $X$, examine the relevance of the function $f(x) = \frac{\rho_A(x)}{\rho_A(x) + \rho_B(x)}$ to Urysohn's lemma**.

    Proof

    Fix some $\varepsilon > 0$ and some $E$. Let $\delta = \varepsilon$. For any two points $x,y \in X$ such that $\rho(x,y) < \delta$, by triangle inequality we have $$\begin{aligned}\rho_E(x) \le& \rho(x,a),\forall a \in E\\\rho_E(x) \le& \rho(x,y) + \rho(y,a),\forall a \in E\\\rho_E(x) - \rho(x,y) \le& \rho(y,a),\forall a\in E \\ \rho_E(x) - \rho(x,y) \le& \rho_E(y)\\ \rho_E(x) - \rho_E(y) \le& \rho(x,y).\end{aligned}$$ Swap $x,y$ we will have $\rho_E(y) - \rho_E(x) = -(\rho_E(x) - \rho_E(y)) \le \rho(x,y)$ thus $| \rho_E(x) - \rho_E(y) | \le \rho(x,y) < \delta = \varepsilon$. Since $\delta$ only depends on $\varepsilon$, by definition $\rho_E$ is uniformly continuous.

    This is a function that can be used to prove Urysohn's Lemma (in a much easier way) in a metric space. Urysohn's Lemma says we can always find a function such is:

    1. Well-defined: The denominator is never $0$;
    2. Continuous: From above (also that denominator is never $0$);
    3. $K \prec f \prec V$: Notice that a metric space needs not to be locally compact (for example, $\mathbb{Q}$), thus the function may not have the compact support property. $f$ takes value $0$ on $A$ and value $1$ on $B$, consider $A = X-V$ and $B = K$ then we have an analogous property.

    ## Exercise 4

    **Examine the proof of the Riesz theorem and prove the following two statements**:

    1. **If $E_1 \subset V_1$ and $E_2 \subset V_2$ where $V_1, V_2$ are disjoint open sets, then $\mu(E_1 \cup E_2) = \mu(E_1) + \mu(E_2)$ even if $E_1, E_2$ are not in $M$**;
    2. **If $E \in M_F$, then $E = N \cup K_1 \cup K_2 \cup \dots$ where $\lbrace K_i\rbrace$ is a disjoint countable collection of compact sets and $\mu(N) = 0$**.

    Proof

    1. By step 1. Of the proof of Riesz Representation Theorem, $\mu(E_1 \cup E_2) \le \mu(E_1) + \mu(E_2)$. Now recall that we defined (no matter if $E \in M$) that $\mu(E) = \inf\lbrace \mu(V): V$ open, $V \supset E\rbrace$. Let $U_1,U_2$ be disjoint open sets containing $E_1,E_2$ respectively, then $U_1 \cap V_1, U_2 \cap V_2$ are also disjoint open sets containing $E_1,E_2$ respectively, so $E_1 \cup E_2 \subset (V_1 \cap U_1) \cup (V_2 \cap U_2)$. Now $\mu((V_1 \cap U_1) \cup (V_2 \cap U_2))$ $= \mu(V_1 \cap U_1) + \mu(V_2 \cap U_2) \ge \mu(E_1) + \mu(E_2)$ for any such $U_1,U_2$, pass to infimum, we have $\mu(E_1 \cup E_2)$ $\overset{\text{def}}{=}\inf\lbrace \mu((V_1 \cap U_1) \cup (V_2 \cap U_2))\rbrace \ge \mu(E_1) + \mu(E_2)$. Put things together we have equality;
    2. Let $E \in M_F$ and set $E_1 = E$, by step 5., we can find $K_1 \subset E_1 \subset V_1$ with $\mu(V_1 - K_1) < 1/1$. Set $E_2 = E_1 - K_1$, by definition of $M_F$ (so $K_1 \in M_F$) and step 6 (so $V_1 - K_1 \in M_F$), $E_2 \in M_F$, so we can find $K_2 \subset E_2 \subset V_2$ with $\mu(V_2 - K_2) < 1/2$. Continue this process and we get a countable collections of disjoint compact sets $\lbrace K_i\rbrace$. Set $N = E - \cup K_i$ then $N$ always lies in $V_n - K_n$ for any $n$, thus $\mu(N) \le 1/n$ for any $n$, which means $\mu(N) = 0$.

    ## Exercise 5

    **Let $E$ be Cantor's familiar middle thirds set. Show that $m(E) = 0$ even though $E$ and $\mathbb{R}$ have the same cardinality**.

    Proof

    From the construction of the Cantor set, we can write $E = \bigcap\limits_{i=0}^{\infty} E_i$ where $m(E_i) = (\frac{2}{3})^i$, then $m(E) \le (\frac{2}{3})^i$ for arbitrary $i$ thus is clearly $0$.

    By an argument from topology (non-empty compact Hausdorff without isolated point $\implies$ uncountable) we can show $E$ is uncountable. But technically this does not say $E$ and $\mathbb{R}$ has the same cardinality.

    To show that, realize that each number $\alpha$ in $[0,1]$ can be expressed in the following way: divides $[0,1]$ to three parts, $[0,1/3], [1/3,2/3], [2/3,1]$, if $\alpha$ lies in the first/second/third part, record a $0/1/2$; divides the part that $\alpha$ lied in into three new parts, if $\alpha$ lies in the first/second/third new part, record a $0/1/2$, and so on. This will not give a unique expression, but it is okay: for example, $1/3 = 0.1$ or $=0.0\dot{2}$ because it lies in both $[0,1/3]$ and $[1/3,2/3]$.

    Now notice that in the construction of Cantor set, at step $n$ we eliminate numbers with expression with $1$ on the $n$-th place. And thus the numbers in Cantor set are exactly those with some expression with only number $0$ and $2$ (so for example $1/3$ is in the set). Now observe that numbers with expressions consist of only $0$ and $2$ are different if and only if the expressions are different. Replace all $2$ by $1$ and realize that it can now be viewed as a number in $[0,1]$ written in base $2$. So the cardinality of $E$ is no less than the cardinality of $[0,1]$. Since $E \subset [0,1]$ the cardinality of $E$ is no more than the cardinality of $[0,1]$, and we have equality.

    ## Exercise 6

    **Construct a totally disconnected compact set $K \subset \mathbb{R}$ such that $m(K) > 0$. If $v$ is lower semicontinuous and $v \le \chi_K$, show that actually $v \le 0$. Hence $\chi_K$ cannot be approximated from below by lower semicontinuous functions, in the sense of the Vitali-Caratheodory Theorem**.

    Solution

    We do a construction that is analogous to the Cantor set with some modification:

    Let $K_0 = [0,1]$, let $K_1$ be $K_0$ with the middle $\frac{1}{3^1}$-'length' open subset removed.

    Let $K_2$ be $K_1$ with a $\frac{1}{3^2}\frac{1}{2^1} = \frac{1}{18}$-'length' open subset removed in each remaining part.

    Continue as that, each $K_n$ is $K_{n-1}$ with a $\frac{1}{3^n}\frac{1}{2^{n-1}}$-'length' open subset removed in each remaining part.

    In other words, we basically do the same steps as in the construction of a Cantor set, but we remove (much) less numbers each step.

    Let $K = \bigcap\limits_{i = 0}^{\infty}K_i$ and this is our $K$. $K$ is:

    1. Compact: Each $K_i$ is closed, so $K$ is closed; $K$ is also bounded, so $K$ is compact;
    2. $m(K)>0$: For each $n$, notice that $K_n$ is constructed from $K_{n-1}$ with $2^{n-1}$ many of $\frac{1}{3^n}\frac{1}{2^{n-1}}$-'length' open sets removed, so $m(K_n) = m(K_{n-1}) - \frac{1}{3^{n}}$. I.e. $m(K_n) = 1 - \frac{1}{3^1}- \frac{1}{3^2}- \frac{1}{3^3}-\dots - \frac{1}{3^{n}}$ and that $m(K) = \lim\limits m(K_n) = 1/2>0$, which can be calculated as $1$ minus an infinite summation of a geometric sequence;
    3. $K$ is totally disconnected: Notice that each $K_n$ is by construction a disjoint union of $2^n$ many closed set of the same certain length, which must go to zero as $n$ goes to infinity, thus $K$ cannot contain any open interval, i.e. $K$ is totally disconnected.

    If $v$ is lower semicontinuous then by definition the set $A = \lbrace x | v(x)>0\rbrace$ has to be open. Since $v \le \chi_K$ we must have $A \subset K$. But we just proved that $K$ does not contain any open interval, so $A = \varnothing$, and thus $v \le 0$.

    ## Exercise 7

    **If $0 < \varepsilon$, construct an open set $E \subset [0,1]$ which is dense in $[0,1]$ such that $m(E) = \varepsilon$**.

    Solution

    We can just take $E$ be the complement of $K$ as in the last problem, then this $E$ will be open (complement of closed set), dense (as argued above, interior of $K$ is empty), and $m(E)$ will be a certain value. For a given $\varepsilon$, essentially we just need to solve $\varepsilon = \sum (\frac{1}{c})^n$ (because $m(E) = 1 - m(K)$ ) $= \frac{1/c}{1-1/c}$ for $c$, which obviously always have a solution. Use this $c$ to substitute every $3$ in the last problem, get $K$, take complement and we get desired $E$.

    ## Exercise 9

    **Construct a sequence of continuous functions $f_n$ on $[0,1]$ such that $0\le f_n \le 1$ and $\lim\limits_{n \to \infty}\int_0^1f_n(x)dx = 0$ but such that the sequence $\lbrace f_n(x)\rbrace$ converges for no $x \in [0,1]$**.

    Solution

    A point that will help about the construction:

    If we just think of 'simple' functions then the continuity requirement is not really a constraint because we can always 'smooth' the part that is not continuous, the value of (Riemann) integral of the original and smoothed functions are the same:

    <img src="public/Pasted image 20210930172033.png" width="600" />

    Since the construction below will only use simple functions, we just assume every function is already smoothed thus continuous.

    Now, consider the list of all fractional expressions in $(0,1]$ which labeled in the order $\frac{1}{1}, \frac{1}{2}, \frac{2}{2}, \frac{1}{3},\frac{2}{3},\frac{3}{3}, \dots, \frac{1}{n},\frac{2}{n}, \dots, \frac{n}{n},\dots$. For each $p/q$, assign it a function $$f_{p,q}(x) = \begin{cases}1,&x \in [\frac{p}{q} - \frac{1}{q}, \frac{p}{q}]\\0,&\text{otherwise}\end{cases}.$$ Since the cardinality of all fractional expressions is countable, we can now label $f_{1,1},f_{1,2},\dots$ as our $f_1,f_2,\dots$:

    1. By construction, $\int_0^1f_{p,q}dx = \frac{1}{q}$, thus $\lim\limits_{n \to \infty}\int_0^1f_n(x)dx = \lim\limits_{q \to \infty}\int_0^1f_{p,q}(x)dx = 0$;

    <img src="public/Pasted image 20210930174955.png" width="600" />

    3. On the other hand, notice that each number in $[0,1]$ lies inside of infinitely many intervals of the form $[\frac{p}{q} - \frac{1}{q}, \frac{p}{q}]$ (and apparently, it also lies outside of infinitely many such intervals). For example, $0.1$ lies in $[0,1/2],[0,1/3],\dots,[0,1/10],[1/11,2/11],\dots$. Thus for any $x \in [0,1]$, $x$ takes value $0$ for infinitely many $f_n$, and takes value $1$ also for infinitely many $f_n$, thus $f_n$ does not converge at $x$.

    ## Exercise 10

    **If $\lbrace f_n\rbrace$ is a sequence of continuous functions on $[0,1]$ such that $0\le f_n \le 1$ and such that $f_n(x) \to 0$ as $n\to \infty$ for every $x \in [0,1]$, then $\lim\limits_{n \to \infty}\int_0^1f_n(x)dx = 0$. Try to prove this without using any measure theory or any theorems about Lebesgue integration**.

    Proof

    It is an immediate result of Lebesgue's Dominated Convergence Theorem, but I don't know how to do it without using measure theory.

    ## Exercise 11

    **Let $\mu$ be a regular Borel measure on a compact Hausdorff space $X$. Assume $\mu(X) = 1$. Prove that there is a compact set $K\subset X$ (the carrier or support of $\mu$) such that $\mu(K) = 1$ but $\mu(H) < 1$ for every proper compact subset $H$ of $K$**.

    Proof

    Define $K$ to be the intersection of all compact sets $K_i$ ($X$ is a such set) with measure $1$. Then:

    1. $K$ is compact: each $K_i$ is compact in Hausdorff $X$ thus closed, the intersection of all $K_i$'s is then closed, and $\cap K_i \subset K_1$ is a closed subset of compact set thus compact;
    2. $\mu(K) = 1$: Let $V$ be an open set containing $K$, then $V^c$ is closed (lies in compact $X$) thus compact. Notice that the set $K_i^c \cap V^c$ is open in $V^c$ (with subspace topology), and that $\cup (K_i^c \cap V^c) = (\cup K_i^c) \cap V^c$ (using $\cup K_i^c = (\cap K_i)^c = K^c \supset V^c$) $= V^c$, so this is an open covering, so it admits a finite sub-covering, say $V^c = (K_1^c \cap V^c) \cup \dots \cup (K_n^c \cap V^c) = (K_1^c \cup \dots \cup K_n^c) \cap V^c$. Now since $\mu(K_i) = 1, \mu(X) = 1$, $\mu(K_i^c) = 0$ for any $i$, thus $\mu(K_1^c \cup \dots \cup K_n^c) = 0$ thus $\mu(V^c) \le 0 \implies \mu(V^c) = 0$ thus $\mu(V) = 1$. Since $V$ is chosen arbitrarily, it follows that any open set containing $K$ has measure $1$; since $\mu$ is regular, $K$ must have measure $1$;
    3. $\mu(H)< 1$: If not, then $H$ is some $K_i$ in the construction of $K$, but then it is not a proper subset of $K$.

    ## Exercise 12

    **Show that every compact subset of $\mathbb{R}$ is the support of a Borel measure**.

    Proof

    Let $K$ be a compact subset of $\mathbb{R}$, consider the measure $\mu_K(E) = \mu(E)/\mu(K)$ where $\mu$ denote the Lebesgue measure. Since $\mu$ is a Borel measure and $\mu(K)$ is now just a fixed number, $\mu_K$ is a Borel measure. Now $\mu_K(K)$ is apparently $1$; suppose $H$ is a proper compact subset of $K$, since we work in $\mathbb{R}$ then $K$ and $H$ are just closed and bounded (union of) intervals, and there must be certain $(a,b)$ contained in $K-H$, thus $\mu(H) < \mu(K)$, thus $\mu_K(H) = \mu(H)/\mu(K) < 1$. By definition $K$ is the support of this Borel measure.

    ## Exercise 13

    **Is it true that every compact subset of $\mathbb{R}$ is the support of a continuous function? if not, can you describe the class of all compact sets in $\mathbb{R}$ which are supports of continuous functions? Is your description valid in other topological spaces**?

    Solution

    1. No, for example, a single-point set cannot be support of a continuous function: otherwise the function takes some non-zero value at that point, and zero on all other points, making the function not continuous;
    2. The class of all compact sets in $\mathbb{R}$ which are supports of continuous functions are those compact sets whose each connect component has non-empty interior:
    	1. If a compact set is of this type: since we do not need differentiability it is very easy to construct a continuous function has support of each of the compact set's connect component;
    	2. If not, then this compact set has some isolated points, and it cannot be the support of a continuous function as argued above;
    3. Not in general, for example if we take $X = \lbrace a, b, c\rbrace$ with $\tau = \lbrace \varnothing, X, \lbrace a\rbrace\rbrace$ and consider $f:X \to X$, $f(X) = \lbrace b\rbrace$. $f$ is continuous. The support of $f$ is $\lbrace b, c\rbrace$ (the smallest closed set contains $\lbrace b\rbrace$), it is connected, yet has an empty interior (the only open set contained in it is the empty set).

    ## Exercise 14

    **Let $f$ be a real-valued Lebesgue measurable function on $\mathbb{R}^k$. Prove that there exist Borel functions $g,h$ such that $g(x) = h(x)$ a.e. $[m]$, and $g(x)\le f(x) \le h(x)$ for every $x \in \mathbb{R}^k$**.

    Proof

    Split $\mathbb{R}^k$ into $k$-unit cubes $(c_1,c_1+1] \times \dots \times (c_k, c_k+1]$. Note there are only countably many of such cubes. Let's fix one of such cube $C$, and consider for now $f$ on $C$ only, then:

    1. $m(C) = 1 < \infty$;
    2. Let $n \in \mathbb{Z}$ and consider $C_n = f^{-1}((n,n+1]) \cap C$, this is a countable partition of $f(C)$. Then by this construction $n<f(C_n)\le n+1$. Since we work with Lebesgue measure, we can apply the corollary of Lusin's Theorem (in that corollary we assumed $| f | \le 1$, but that is not a big problem - we can just think our $f$ of a constant map add a map bounded by $1$) to get a sequence $\lbrace \sigma_{n,m}\rbrace$ such that $f(x) = \lim\limits_{m \to \infty} \sigma_{n,m} = \sigma_n$ a.e. on $C_n$. Each $\sigma_{n,m}$ is by the theorem continuous thus Borel measurable, thus $\sigma_n$ is Borel measurable. Define $\sigma$ on $C$ where $\sigma(x) = \sigma_n(x)$ for $x$ in corresponding $C_n$. Then $\sigma$ is Borel measurable and $f = \sigma$ a.e. (countable union of measure zero is still measure zero) on $C$.

    Do this for each $C$ cube and extend the domain for $f$ and $\sigma$, then $\sigma$ is a Borel function on $\mathbb{R}^k$ such that $f = \sigma$ a.e.

    Consider the set $X = \lbrace x | f(x) \ne \sigma(x)\rbrace$, this set has measure $0$, define a function $\varphi$ on $\mathbb{R}^k$ as following: if $x \notin X$, $\varphi(x) = 0$, otherwise, $\varphi(x) = \lceil \sigma(x) - f(x) \rceil$ (the smallest integer that larger than or equal to $\sigma(x) - f(x)$). This $\varphi$ is easy to see to be a Borel function.

    Define our $g(x) = \sigma(x) - \varphi(x)$, it is a Borel function by construction, and $g(x) = \sigma(x) - \lceil \sigma(x) - f(x) \rceil$ $\le f(x)$ for all $x$. Measure of the set that $g(x) \ne f(x)$ is by construction $0$.

    Since this works for any real-valued Lebesgue measurable $f$, it also work for $-f$ (which is apparently also real-valued Lebesgue measurable), thus we can find $-h \le -f$ thus we can find $f \le h$. $g(x) \ne h(x)$ only if $g(x) \ne f(x)$ and $h(x) \ne f(x)$ thus have measure zero, so $g(x) = h(x)$ a.e.

    ## Exercise 15

    **It is easy to guess the limits of $\int_0^n (1-\frac{x}{n})^ne^{x/2}dx$ and $\int_0^n (1+\frac{x}{n})^ne^{-2x}dx$ as $n\to \infty$. Prove that your guesses are correct**.

    Proof

    For the first one: define a sequence $\lbrace f_n\rbrace$ where $f_n(x) = (1-\frac{x}{n})^ne^{x/2}$ on $[0,n]$ and $0$ otherwise. This is an important limit and we know that $\lim\limits f_n = e^{x/2 - x} = e^{-x/2}$. For any $n$ we can see from the derivative that $(1-\frac{x}{n})^n \le e^x$ on $[0,n]$ (equality only at $0$), so $\lim\limits f_n > f_n$ for all $n$ and $x$. Since $e^{-x/2}$ is $L^1$ we can apply the Lebesgue's Dominated Convergence Theorem to get $\lim\limits_{n\to \infty}\int_0^n (1-\frac{x}{n})^ne^{x/2}dx$ $= \lim\limits \int_0^n e^{-x/2}dx = \lim\limits (2e^0 - 2e^{-n}) = 2$, just use the common Riemann integral.

    The second one can be evaluated in a similar way, $\lim\limits \int_0^n (1+\frac{x}{n})^ne^{-2x}dx$ $= \lim\limits \int_0^n e^{-x}dx = 1$.

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
    ## Exercise 1

    **Prove that the supremum of any collection of convex functions on $(a,b)$ is convex on $(a,b)$ if it is finite, and that point-wise limits of sequences of convex functions are convex. What can you say about upper and lower limits of sequence of convex functions**?

    Proof

    Suppose $\lbrace f_i \rbrace$ is a collection of convex functions on $(a,b)$ and $f$ is the supremum. By definition we have $f_i((1-\lambda)x + \lambda y) \le (1-\lambda)f_i(x) + \lambda f_i(y)$, since $f$ is the supremum we have $\le (1-\lambda)f(x) + \lambda f(y)$. But since this works for any $i$, so we have $\sup(f_i((1-\lambda)x + \lambda y)) \le (1-\lambda)f(x) + \lambda f(y)$, i.e. $f((1-\lambda)x + \lambda y) \le (1-\lambda)f(x) + \lambda f(y)$ which by definition means convexity.

    Suppose $\lbrace f_i \rbrace$ is a collection of convex functions and $f$ is the point-wise limit, if we do not have convexity for $f$, i.e. $(1-\lambda)f(x) + \lambda f(y) < f((1-\lambda)x + \lambda y)$ for certain $x,y, \lambda$, then by definition of limit, we will have $(1-\lambda)f_i(x) + \lambda f_i(y) < f_i((1-\lambda)x + \lambda y)$ for some $f_i$, so $f_i$ is not convex.

    The difference between the second and third statement is the second statement assumes the existence of the point-wise limit. For the third statement, we may have the situation that we have some arbitrary upper or lower bound of the functions, yet no 'infinity' comes into play.

    Nevertheless, the upper limits of sequence of convex functions are still convex: if $\lbrace f_i \rbrace$ is a sequence of convex functions and $f$ is the upper limit, then for contradiction if $f((1-\lambda)x + \lambda y) > (1-\lambda)f(x) + \lambda f(y)$ then $f((1-\lambda)x + \lambda y) > (1-\lambda)f_i(x) + \lambda f_i(y)$ for any $i$, but then there will be some $i$ with $f_i((1-\lambda)x + \lambda y) > (1-\lambda)f_i(x) + \lambda f_i(y)$.

    The inequality does not work for the lower limit. Take $f_1(x) = x$ on $(0,1)$, $f_2(x) = 1-x$ on $(0,1)$, and $f_i = 0.5$ for any $i > 2$, then we have a counterexample.

    ## Exercise 2

    **If $\varphi$ is convex on $(a,b)$ and if $\psi$ is convex and non-decreasing on the range of $\varphi$, prove $\psi \circ \varphi$ is convex on $(a,b)$. For $\varphi>0$, show that the convexity of $\log{\varphi}$ implies the convexity of $\varphi$, but not vice versa**.

    Proof

    We have $$\begin{aligned} \psi(\varphi((1-\lambda)x + \lambda y)) &\le \psi((1-\lambda)\varphi(x) + \lambda \varphi(y)) \\ &\le (1-\lambda)\psi(\varphi(x)) + \lambda \psi(\varphi(y)) \end{aligned}.$$
    The first inequality comes from that $\psi$ is non-decreasing and convexity of $\varphi$, and the second one comes from the convexity of $\psi$; by definition we have convexity of $\psi \circ \varphi$.

    For the second, we know $\exp$ is convex and non-decreasing, so $\log(\varphi)$ being convex implies $\exp(\log(\varphi)) = \varphi$ being convex by part 1.

    Converse not true: $\varphi(x) = x$ the identity map is convex (say on $(0,1)$), yet $\log(x)$ is certainly not convex.

    ## Exercise 3

    **Assume that $\varphi$ is a continuous real function on $(a,b)$ such that $\varphi(\frac{x+y}{2}) \le \frac{1}{2}\varphi(x) + \frac{1}{2}\varphi(y)$ for all $x$ and $y \in (a,b)$. Prove that $\varphi$ is convex**.

    Proof

    Fix any $\lambda, x, y$ in the setting of a convex function.

    If $\lambda$ is a fraction of the form $m/2^n$ then things are easy, for example if $\lambda = 1/4$ we can see the condition for convexity holds as follow: let $x' = \frac{3}{4}x + \frac{1}{4}y$ and $x'' = \frac{1}{2}x + \frac{1}{2}y$, then $\varphi(x') \le \frac{\varphi(x) + \varphi(x'')}{2}$ $\le \frac{\varphi(x) + \frac{\varphi(x) + \varphi(y)}{2}}{2}$.

    If not, then we can approximate such $\lambda$ by a fraction of the form $r = m/2^n$, i.e. so that $| \varphi((1-\lambda)x + \lambda y) - \varphi((1-r)x + r y) |$ and $| (1-\lambda)\varphi(x) + \lambda\varphi(y) - (1-r)\varphi(x) - r\varphi(y) |$ are both arbitrarily small, and thus we have convexity.

    This approximation apparently requires continuity, so in general if we omit the continuity requirement, $\varphi$ may not be convex.

    ## Exercise 6

    **Let $m$ be Lebesgue measure on $[0,1]$ and define $\| f \|_p$ with respect to $m$. Find all functions $\Phi$ on $[0,\infty)$ such that the relation $\Phi(\lim\limits_{p\to 0} \| f \|_p) = \int\limits_0^1 (\Phi \circ f)dm$ holds for every bounded measurable positive $f$. Show first that $c\Phi(x) + (1-c)\Phi(1) = \Phi(x^c), x>0, 0 \le c \le 1$. Compare with Exercise 5(d)**.

    Proof

    Fix any $x > 0$ and consider the function $f = \chi_Cx + \chi_{C'}$ for some $c \in [0,1]$ and $C = [0,c], C' = (c,1]$. This $f$ is by construction bounded, measurable, and positive. We have, by definition, $\| f \|_p = (\int_{[0,1]} | \chi_Cx + \chi_{C'} |^p dm)^{1/p}$. Notice that we have $| \chi_C x + \chi_{C'} |^p = \chi_Cx^p + \chi_{C'}$, so we can continue write $\| f \|_p = (\int_{[0,1]} \chi_Cx^p + \chi_{C'} dm)^{1/p}$ $= (m(C)x^p + m(C'))^{1/p}$ $= (cx^p + (1-c))^{1/p}$.

    So now $\Phi(\lim\limits_{p\to 0} \| f \|_p) = \Phi(\lim\limits_{p \to 0}(cx^p + (1-c))^{1/p})$, the limit inside can be calculated by taking log and apply the L'Hospital's rule, and the result is $x^c$, so we have $\Phi(\lim\limits_{p\to 0} \| f \|_p) = \Phi(x^c)$.

    On the other hand, $\Phi \circ f = \Phi(\chi_Cx + \chi_{C'}) = \chi_C\Phi(x) + \chi_{C'}\Phi(1)$, so $\int\limits_0^1 (\Phi \circ f)dm = \int\limits_0^1 \chi_C\Phi(x) + \chi_{C'}\Phi(1) dm$ $=m(C)\Phi(x) + m(C')\Phi(1)$ $=c\Phi(x) + (1-c)\Phi(1)$.

    Combine them, thus if by assumption $\Phi(\lim\limits_{p\to 0} \| f \|_p) = \int\limits_0^1 (\Phi \circ f)dm$, then we must have $c\Phi(x) + (1-c)\Phi(1) = \Phi(x^c)$, $x$ can be any positive number, and $0 \le c \le 1$.

    Now if $c>1$, then $0\le 1/c \le 1$, so $1/c\Phi(x) + (1-1/c)\Phi(1) = \Phi(x^{1/c})$, substitute $y = x^{1/c}$, we can get $1/c\Phi(y^c) + (1-1/c)\Phi(1) = \Phi(y)$ $\implies c\Phi(y) + (1-c)\Phi(1) = \Phi(y^c)$, so actually the equality holds for all $c \ge 0$.

    Consider the function $\varphi$ defined as $\varphi(x) = \Phi(x) - \Phi(1)$, then $\varphi(x^c) = c\varphi(x)$. In particular, note that any number $y > 0$ can be written as $y = e^{\ln{y}}$, thus $\varphi(y) = \varphi(e)\ln{y} = (\Phi(e) - \Phi(1))\ln{y}$. In case that $y<1$, we need to write it as $\varphi(y) = \varphi(1/e)\ln{1/y} = -(\Phi(1/e)-\Phi(1))\ln{y}$ (because we require $c \ge 0$), and thus $\Phi(x)$ has the form $$\Phi(x) = \begin{cases} (\Phi(e) - \Phi(1))\ln{x} + \Phi(1),& x\ge 1 \\ \Phi(1) -(\Phi(1/e) - \Phi(1))\ln{x},& 0<x<1 \end{cases}.$$

    ## Exercise 10

    **Suppose $f_n \in L^p(\mu)$ for $n = 1,2,\dots$ and $\| f_n - f \|_p \to 0$ and $f_n \to g$ a.e. as $n \to \infty$. What relation exists between $f$ and $g$**?

    Solution

    From $\| f_n - f \|_p \to 0$ we have $f_n \to f$ a.e. (the first part of proof of Theorem 3.11 that $L^p(\mu)$ is complete). Since $f_n \to g$ a.e. as well, it is easy to see $f = g$ a.e. (union of two measure zero sets is of measure zero).

    ## Exercise 11

    **Suppose $\mu(\Omega) = 1$, and suppose $f,g$ are positive measurable functions on $\Omega$ such that $fg \ge 1$. Prove that $\int_{\Omega}fd\mu \cdot \int_{\Omega}gd\mu \ge 1$**.

    Proof

    If $f,g$ are positive measurable functions and $fg \ge 1$, then $\sqrt{f},\sqrt{g}$ are also positive measurable functions with $\sqrt{fg} \ge 1$ (measurable because taking square root is a continuous function).

    So now we can apply Hölder's inequality on $\sqrt{f}, \sqrt{g}$ with $p = q = 2$, then $$(\int_{\Omega}\sqrt{f}^2d\mu)^{1/2}(\int_{\Omega}\sqrt{g}^2d\mu)^{1/2} \ge \int_{\Omega}\sqrt{fg}d\mu \ge \int_{\Omega}1 d\mu = 1.$$ Taking square both side and we have the desired inequality.

    (A little remark: here is no need to argue if $f, \sqrt{f}$ are $L^2$, etc., because the integrals are defined anyway, and it does not matter if it goes to infinity because we only want to show it is $\ge 1$)

    ## Exercise 12

    **Suppose $\mu(\Omega) = 1$ and $h: \Omega \to [0,\infty]$ is measurable. If $A = \int_{\Omega}hd\mu$, prove that $\sqrt{1+A^2} \le \int_{\Omega}\sqrt{1+h^2}d\mu \le 1+A$. If $\mu$ is Lebesgue measure on $[0,1]$ and $h$ is continuous, $h = f'$, the above inequality have a simple geometric interpretation. From this, conjecture for general $\Omega$ under what conditions on $h$ equality can hold in either of the above inequalities, and prove your conjecture**.

    Proof

    1. Prove the inequality:
    	1. For the first part, notice that it is in the form of the Jensen's Inequality, so this part is proven if $\sqrt{1+x^2}$ is convex: indeed, take derivative we have $x(1+x^2)^{-1/2}$ and second derivative we have $(1+x^2)^{-3/2}$ which is always positive, thus we have convexity;
    	2. For the second part, write $1+A = 1 + \int_{\Omega}hd\mu$ $= \int_{\Omega}1 + h d\mu$ (because $\mu(\Omega)=1$), then we can see if we can prove $\sqrt{1+h^2} \le 1 + h$ then this part is proven: this just comes from that $1+h^2 \le 1+2h+h^2 = (1+h)^2$ if $h\ge 0$;
    2. A geometric interpretation:
    	In this setting $\int_{\Omega}\sqrt{1+h^2}d\mu = \int_0^1 \sqrt{1 + f'^2}dx$, recall that this integral calculates the distance between $f(0)$ and $f(1)$ along the curve $f$.
    	By Fundamental Theorem of Calculus, $A = f(1) - f(0)$, so $\sqrt{1+A^2}$ can be thought as the straight-segment distance between $f(0)$ and $f(1)$; $1+A$ can be thought as the two-straight-segment-passing-corner distance between $f(0)$ and $f(1)$.
    	So this inequality just gives a natural range of the curve length of the graph of a non-decreasing (because $f' = h$ is by assumption non-negative) function;
    3. From the geometric interpretation we could guess that the first equality holds if and only if $f$ is a straight line, i.e. $f' = h$ is a constant (with a little calculation, this constant is $A$) a.e., and the second equality holds if and only if $f$ is a horizontal line (it cannot have height, otherwise it is not a graph), i.e. $f' = h = 0$ a.e. (in this case the first equality also holds):
    	1. If $h = A$ is then $\int_{\Omega}\sqrt{1+h^2}d\mu = \sqrt{1+h^2} = \sqrt{1+A^2}$, and if $h = 0 = A$ then $\int_{\Omega}\sqrt{1+h^2}d\mu = \sqrt{1+h^2} = 1 = 1+0 = A$;
    	2. Converse for the first equality comes from Jensen's Inequality's proof, if $\sqrt{1+A^2} = \int_{\Omega}\sqrt{1+h^2}d\mu$ then $\varphi(h) = \varphi(A) + \beta(h -A)$, thus either $\varphi$ is affine (not our case: we have $\varphi(x) = \sqrt{1+x^2}$) or $h$ is constant and must be $A$ a.e;
    	3. Converse for the second equality: we need to have $1+h^2 = (1+h)^2$ a.e. thus $h = 0$ a.e.

    (I am not sure what does the problem mean by 'for general $\Omega$', apparently for different $\Omega$ thus different $\mu(\Omega)$ the equalities are not the same, we need to change $1$ to $\mu(\Omega)$)

    ## Exercise 13

    **Under what conditions on $f,g$ does equality hold in the conclusions of Theorem 3.8 and 3.9? You may have to treat the cases $p = 1$ and $p = \infty$ separately**.

    Solution

    ### Part 1

    Theorem 3.8 says: If $p,q$ are conjugate exponents, $1 \le p \le \infty$, and if $f \in L^p(\mu)$, $g \in L^q(\mu)$, then $fg \in L^1(\mu)$ and $$\| fg \|_1 \le \| f \|_p\| g \|_q.$$ If $1 < p < \infty$ then this is Hölder's inequality, so equality holds if equality in Hölder's Inequality holds, which we know happens if and only if that $af^p = bg^q$ a.e. for some non-zero constant $a,b$, or that we have the trivial cases that at least one of $f,g$ is zero a.e.

    If $p = 1$ (then $q = \infty$), then we want $| f(x)g(x) | = \| f \|_{\infty} | g(x) |$ for almost all $x$, which happens if and only if $g \equiv 0$ or $\| f \|_{\infty} = | f(x) |$ (then product of absolute values is absolute value of products), i.e. $f$ is constant a.e.. The case $p = \infty$ is the analogous.

    ### Part 2

    Theorem 3.9 says: If $1 \le p \le \infty$ and $f,g \in L^p(\mu)$, then $f+g \in L^p(\mu)$ and $$\| f+g \|_p \le \| f \|_p+\| g \|_p.$$ If $1< p < \infty$ then this is Minkowski's Inequality. Look at the proof of Minkowski's Inequality, we can see that equality holds if and only if at least one of $f,g$ is $0$ a.e. or equality in Hölder's Inequality holds for $f$ and $(f+g)^{p-1}$, and for $g$ and $(f+g)^{p-1}$, i.e. exists non-zero $a,b$ such that $af^p = b(f+g)^{qp-q}$ a.e. and non-zero $c,d$ such that $cg^p = d(f+g)^{qp-q}$ a.e.

    Put things together, equality holds if and only if that at least one of $f,g$ is zero a.e., or that $f = ag$ for some non-zero $a$ a.e.

    If $p = 1$, equality holds if and only if $| f+ g | = | f | + | g |$ a.e., which holds if and only if $f,g$ are both non-negative or both non-positive, or at least one of $f,g$ is $0$ a.e.

    If $p = \infty$, then equality holds if essential supreme of $f+g$ equals sum of essential supremes, i.e. $f,g$ achieve/approaches their essential supreme at the same time (this include the cases that at least on of $f,g$ is zero a.e.).

    ## Exercise 14

    **Suppose $1 < p < \infty$, $f \in L^p = L^p((0,\infty))$ relative to Lebesgue measure, and $F(x) = \frac{1}{x}\int_0^x f(t)dt, (0 < x < \infty)$**:

    1. **Prove Hardy's inequality $\| F \|_p \le \frac{p}{p-1}\| f \|_p$ which shows that the mapping $f \to F$ carries $L^p$ into $L^p$**;
    2. **Prove that equality holds only if $f = 0$ a.e**;
    3. **Prove that the constant $p/(p-1)$ cannot be replaced by a smaller one**;
    4. **If $f > 0$ and $f \in L^1$, prove that $F \notin L^1$**.

    Proof

    ### Part 1

    Let $q$ be the conjugate exponent of $p$, notice that then we can write $q = \frac{p}{p-1}$.

    Start by $F(x)$ and we will 'construct' $\| F \|_p$. Let $a$ be some real number, we can write $$| x F(x) | := | \int\limits_0^xf(t)t^at^{-a}dt|.$$
    Apply Hölder's Inequality $$\le(\int\limits_0^x| f(t)|^pt^{pa}dt)^{1/p}(\int\limits_0^xt^{-qa}dt)^{1/q}.$$ Now just do some calculation, notice that we need $0<qa<1$ for this to work $$= (\int\limits_0^x| f(t)|^pt^{pa}dt)^{1/p}(\frac{x^{1-qa}}{1-qa})^{1/q}.$$ Since $x$ is just viewed as a positive constant, we can write $$\begin{aligned}| F(x) | &\le (\int\limits_0^x| f(t)|^pt^{pa}dt)^{1/p}x^{1/q-a-1}(1-qa)^{-1/q} \\ | F(x) |^p &\le (\int\limits_0^x| f(t)|^pt^{pa}dt)~x^{p/q-pa-p}~(1-qa)^{-p/q} \\ &= (\int\limits_0^x| f(t)|^pt^{pa}dt)~x^{-1-pa}~(1-qa)^{-p/q} \end{aligned}.$$ Take integral we have $$\begin{aligned} \int\limits_0^\infty | F(x) |^p dx &\le \int\limits_0^\infty [(\int\limits_0^x| f(t)|^pt^{pa}dt)~x^{-1-pa}~(1-qa)^{-p/q}]dx \\ &= (1-qa)^{-p/q}\int\limits_0^\infty\int\limits_0^x| f(t)|^pt^{pa}x^{-1-pa}dtdx\end{aligned}.$$ We do a change of order of taking integral, it is viable because everything inside is positive. Then just do some simplification $$\begin{aligned}&= (1-qa)^{-p/q}\int\limits_0^\infty\int\limits_t^{\infty}| f(t)|^pt^{pa}x^{-1-pa}dxdt \\ &= (1-qa)^{-p/q}\int\limits_0^\infty| f(t)|^pt^{pa}(\int\limits_t^{\infty}x^{-1-pa}dx)dt \\ &= (1-qa)^{-p/q}\int\limits_0^\infty| f(t)|^pt^{pa}(\frac{t^{-pa}}{pa})dt \\ &= (1-qa)^{-p/q}\frac{1}{pa}\int\limits_0^\infty| f(t)|^pdt\end{aligned}.$$ Thus $$\begin{aligned}\| F(x) \|_p &\le ((1-qa)^{-p/q}\frac{1}{pa})^{1/p}\| f(x) \|_p\end{aligned}.$$ If we now take $a = \frac{1}{pq}$ then $((1-qa)^{-p/q}\frac{1}{pa})^{1/p}$ $= ((1-\frac{1}{p})^{-p/q}q)^{1/p}$ $=(q^{p/q}q)^{1/p} = q$, and we have the desired inequality.

    ### Part 2

    Look at the above proof and we see the only inequality is the first step when we apply Hölder, so equality in Hardy's Inequality holds if and only if the equality in Hölder's Inequality holds, that is either we have the trivial case $f = 0$ a.e. or there are non-zero $m,n$ such that $m(f(t)t^{1/pq})^p = n(t^{-1/pq})^q$ $\implies f^p = \frac{c}{t}$, but then $\| f \|_p = (\int\limits_0^{\infty}\frac{c}{t}dt)^{1/p}$ and it is known that $\int\limits_0^{\infty}\frac{1}{t}dt$ does not converge, so $f$ is not $L^p$ thus this is not an viable option, so equality only holds at the trivial case, i.e. $f = 0$ a.e.

    ### Part 3

    Prove by an example: consider $f(x) = x^{-1/p}$ on $[1,A]$ and $0$ elsewhere for some $A>1$, then $\| f \|_p = (\int\limits_1^A x^{-1} dx)^{1/p} = (\log{A})^{1/p}$. On the other hand, if $x<1$ then $F(x) = 0$, if $1<x<A$ then $F(x) = \frac{1}{x}\int\limits_1^xt^{-1/p}dt$ $= \frac{px^{-1/p}-p}{p-1}$, and if $A<x$ then $F(x) = \frac{pA^{1-1/p}-p}{x(p-1)}$.

    (I think the idea here is then to calculate $\lim\limits_{A \to \infty}\frac{\| F \|_p}{\| f \|_p}$. To calculate $\| F \|_p$, first evaluate from $1$ to $A$, then from $A$ to $\infty$, which is $$\| F \|_p^p = \int\limits_1^A(\frac{px^{-1/p}-p}{p-1})^pdx + \int\limits_A^{\infty}(\frac{pA^{1-1/p}-p}{x(p-1)})^pdx,$$ but I'm not sure how to do that by hand, the result from WolframAlpha gives: the limit is $\frac{p}{p-1}$, and thus no constant smaller than this value could work in the Hardy's Inequality)

    ### Part 4

    Under the assumption we have $F(x) = \frac{1}{x}\int_0^x f(t)dt$, choose some (measurable) set $E$ such that $f(E) > a$ for a positive $a$ (existence is by that $f>0$), then for $x>\sup{E}$ we have $F(x) \ge \frac{1}{x} \int_Ead\mu = \frac{a\mu(E)}{x} = \frac{c}{x}$, yet it is known that $\int_n^{\infty}\frac{c}{x}dx$ does not converge for any $n$, thus $F$ is not $L^1$.

    ## Exercise 18

    **Let $\mu$ be a positive measure on $X$. A sequence $\lbrace f_n \rbrace$ of complex measurable functions on $X$ is said to converge in measure to the measurable function $f$ if to every $\varepsilon there corresponds an $N$ such that $\mu(\lbrace x : | f_n(x) - f(x) | > \varepsilon\rbrace) < \varepsilon$ for all $n > N$. Assume $\mu(X) <\infty$ and prove the following statements**:

    1. **If $f_n(x) \to f(x)$ a.e., then $f_n \to f$ in measure**;
    2. **If $f_n \in L^p(\mu)$ and $\| f_n - f \|_p \to 0, 1 \le p \le \infty$, then $f_n \to f$ in measure**;
    3. **If $f_n \to f$ in measure, then $\lbrace f_n \rbrace$ has a subsequence which converges to $f$ a.e**.

    **Investigate the converses of 1. And 2., what happens to 1., 2., 3., if $\mu(X) = \infty$, for instance, if $\mu$ is the Lebesgue measure on $\mathbb{R}$**?

    Proof

    ### Part 1

    Fix some $\varepsilon>0$.

    Suppose $f_n(x) \to f(x)$ a.e., it means that for almost all $x$, $f_n(x) \to f(x)$, which means that for almost all $x$, there exists some $N_x$, depending on $x$, such that $| f_{n_x}(x) - f(x) | \le \varepsilon$ for all $n_x > N_x$. Now index on $N_x$, consider $A_N = \lbrace x : | f_{n_x}(x) - f(x) | \le \varepsilon$ for all $n_x>N\rbrace$, then $\lbrace x | f_n(x) \to f(x) \rbrace = \cup A_N$. By assumption we have $\mu(\cup A) = \mu(X)$.

    Write $\lbrace x : | f_n(x) - f(x) | > \varepsilon\rbrace$ $= X - \lbrace x : | f_n(x) - f(x) | \le \varepsilon$ for some $n \rbrace$, so the measure $\mu(\lbrace x : | f_n(x) - f(x) | > \varepsilon\rbrace)$ $= \mu(X - \lbrace x : | f_n(x) - f(x) | \le \varepsilon$ for some $n \rbrace )$. Since this should work for arbitrary $\varepsilon$, this value $= \mu(X - \cup A) = 0$ as desired.

    ### Part 2

    Fix some $\varepsilon$.

    Suppose $p = \infty$, $\| f_n(x) - f(x) \|_{\infty} \to 0$ means $\| f_n(x) - f(x) \|_{\infty} \le \varepsilon$ for large enough $n$, which means $| f_n(x) - f(x) | \le \varepsilon$ a.e. by definition for large enough $n$. It is equivalent to say that $\mu(\lbrace x : | f_n(x) - f(x) | > \varepsilon\rbrace) = 0$ for large enough $n$.

    Suppose $1 \le p < \infty$. Denote the set $\lbrace x : | f_n(x) - f(x) | > \varepsilon\rbrace = B_n$, then $\| f_n - f \|_p$ $:= (\int_X| f_n - f |^p)^{1/p}$ $\ge (\int_{B_n}\varepsilon^p)^{1/p}$ $= (\varepsilon^p\mu(B_n))^{1/p}$, thus $\mu(B_n) \le (\frac{\| f_n - f \|_p}{\varepsilon})^p$. Since $\| f_n - f \|_p \to 0$, $\mu(B_n)$ thus $\mu(\lbrace x : | f_n(x) - f(x) | > \varepsilon\rbrace)$ takes arbitrarily small value for large enough $n$.

    ### Part 3

    For each $i$, there exists $N_i$ such that $\mu(\lbrace x : | f_n(x) - f(x) | > 2^{-i}\rbrace) < 2^{-i}$ for all $n > N_i$. Pick $n_i > N_i$ and $n_i > n_{i-1},\dots,n_1$, then we have a subsequence $f_{n_i}$ of $f_n$. Now use the fact that $\sum\limits_{i} 2^{-i} = 1 < \infty$, so almost all $x$ lie in at most finitely many sets such that $\lbrace x : | f_n(x) - f(x) | > 2^{-i}\rbrace$ (Theorem 1.41), which is equivalent to say that for almost all $x$ we have $f_{n_i} \to f$.

    ### Part 4

    The converse of part 1 says convergence in measure implies convergence point-wise a.e. This is not true, Homework 2 Exercise 9 is a counterexample.

    The converse of part 2 says convergence in measure implies convergence in $L^p$ norm. This is also not true, and we can use the same counterexample.

    ### Part 5

    If $\mu = m$ and $X = \mathbb{R}$, then:

    1. Part 1 is false, for example, $f_n = \chi_{[n,n+1]} \to 0$ for any $x$ point-wisely, but not converge to $0$ in measure;
    2. Part 2,3 are true, the proof does not depend on that $\mu(X)<\infty$.

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
    ## Exercise 1

    **If $M$ is a closed subspace of $H$, prove that $M = (M^{\perp})^{\perp}$. Is there a similar true statement for subspaces $M$ which are not necessarily closed**?

    Proof

    If $x \in M$ then it is by definition perpendicular to any $y \in M^{\perp}$ , thus by definition it is in $(M^{\perp})^{\perp}$.

    Conversely, suppose $x \in (M^{\perp})^{\perp}$, clearly $x \in H$, so we may write $x = y + z$ with $y \in M, z \in M^{\perp}$. In particular $(x, z) = (y+z,z)$. Now the LHS equals $0$ because $x, z$ are perpendicular. RHS equals $(y,z) + (z,z) = (z,z)$ because $y,z$ are perpendicular, thus $z = 0$, thus $x =y$ with $y \in M$, i.e. $x \in M$.

    We know that $M^{\perp}$ is always closed (intersection of closed subset), so $M^{\perp} = ((M^{\perp})^{\perp})^{\perp}$ always work.

    ## Exercise 2

    **Let $\lbrace x_n \rbrace$ be a linearly independent set of vectors in $H$. Show that the following construction yields an orthonormal set $\lbrace u_n \rbrace$ such that $\lbrace x_1,\dots, x_N \rbrace$ and $\lbrace u_1,\dots, u_N \rbrace$ have the same span for all $N$**:

    **Put $u_1 = x_1/\| x_1 \|$. Having $u_1,\dots, u_{n-1}$ define** $$v_n = x_n - \sum\limits_{i = 1}^{n-1}(x_n, u_i)u_i,~~~~ u_n = v_n/\| v_n \|.$$ **This leads to a proof of the existence of a maximal orthonormal set in separable Hilbert spaces which makes no appeal to the Hausdorff maximality principle (a space is separable if it contains a countable dense subset)**.

    Proof

    Since all $u_i$ is defined as a vector divided by its norm, clearly we have $\| u_i \| = 1$ for all viable $i$.

    By induction on $j$ we show $(u_n, u_m) = 0$ for $n<m$. If $m = 1$ then there is no viable $u_n$. If $m = 2$ then only possible $u_n$ is $u_1$ and $v_2$ is defined as $(x_2 - (x_2, u_1)u_1)$, then $(u_1, v_2) = (u_1, x_2 - (x_2, u_1)u_1)$ $=(u_1,x_2) - (x_2,u_1)(u_1,u_1)$ $=0$, so $(u_1, u_2) = 0$ as well, so it works for $m = 2$.

    For a fixed $m$ and $n<m$, we can write $(v_m, u_n)$ $= (x_m - \sum\limits_{i=1}^{m-1}(x_m,u_i)u_i, u_n)$ $= (x_m - (x_m,u_1)u_1 - (x_m,u_2)u_2 - \dots - (x_m,u_{m-1})u_{m-1}, u_n)$ $= (x_m, u_n) - (x_m, u_n) = 0$ because by induction assumption $(u_i, u_n) = 0$ for $i <m, i \ne n$, and $(u_n, u_n) = 1$. Since $u_m$ and $v_m$ only different by a scalar, we have that $(u_n, u_m) = 0$ for $n < m$.

    So $\lbrace u_i \rbrace$ is an orthonormal set.

    Span of $\lbrace u_i \rbrace$ lies inside span of $\lbrace x_i \rbrace$, because $\lbrace u_i \rbrace$ are constructed from $\lbrace x_i \rbrace$. It is also not hard to see $\lbrace x_i \rbrace$ are constructible from $\lbrace u_i \rbrace$ so the other inclusion also works.

    If $H$ is separable then it admits a countable dense subset, so it admits a (at most) countable basis, which can be seen as $\lbrace x_N \rbrace$, now use the above construction to make $\lbrace u_N \rbrace$, then the set $P$ of all finite linear combinations of members of $\lbrace u_{N} \rbrace$ is by construction dense, thus $\lbrace u_N \rbrace$ is maximal (and it is countable) by Theorem 4.18.

    ## Exercise 3

    **Show that $L^p(T)$ is separable if $1\le p < \infty$, but $L^{\infty}(T)$ is not separable**.

    Proof

    We proved that trigonometry polynomials are dense in $C(T)$, since $T$ is compact, every map in $C(T)$ is also in $C_C(T)$ (because any closed subset of compact space is compact, i.e. support is always compact), and that we know for $1 \le p < \infty$, $C_C(T)$ is dense in $L^p(T)$. Now the definition of a trigonometry polynomials uses real numbers, but since $\mathbb{Q}$ is dense in $\mathbb{R}$, 'rational' trigonometry polynomials are also dense in $C(T)$, there are countably many such polynomials, and result follows.

    For $L^{\infty}(T)$: consider the functions $\lbrace f_a(t) \rbrace$ where $$f_a = \begin{cases} 1, t \in [0,a) \\ 0, t \in [a,2\pi] \end{cases} = \chi_{[0,a)}, a \in [0,2\pi].$$ Apparently there are uncountably different $f_a$'s, yet for any $a < b$, we have $f_b - f_a = \chi_{[a,b]}$, so that $\| f_b - f_a \|_p = 1$. Thus there is no way to remove any $f_a$ from the set and still have the rest of $\lbrace f_a \rbrace$ be (potentially) dense. In particular $L^{\infty}(T)$ cannot have a countable dense subset, i.e. it is not separable.

    ## Exercise 4

    **Show that $H$ is separable if and only if $H$ contains a maximal orthonormal system which is at most countable**.

    Proof

    We will use Theorem 4.18.

    If $H$ contains a maximal orthonormal system which is at most countable, then the set $P$ of all finite linear combinations of members of $\lbrace u_{\alpha} \rbrace$ is dense in $H$, $P$ is countable, thus $H$ is separable.

    The converse is proved in Exercise 2.

    ## Exercise 5

    **If $M = \lbrace x | Lx = 0 \rbrace$, where $L$ is a continuous linear functional on $H$, prove that $M^{\perp}$ is a vector space of dimension $1$ unless $M = H$**.

    Proof

    If $L$ is a continuous linear functional on $H$, then there is a unique $y \in H$ such that $Lx = (x,y), \forall x \in H$. So a given $L$ implies a unique $y$, and $M$ is equivalently defined as $\lbrace x | (x,y) = 0 \rbrace$. Denote the space spanned by $y$ by $N$, then $N = M^{\perp}$:

    $N$ is closed because it contains all scalar multiplication of $y$. So by Exercise 1, $N = (N^{\perp})^{\perp}$. Now it is from definition of $N$ and $M$ that $N^{\perp} = M$ because $M$ consists of all element that perpendicular to $y$ thus scalar multiplications of $y$. Plug into $N = (N^{\perp})^{\perp}$ we have that $N = M^{\perp}$.

    If $H = M$ then $y = 0$ then $M^{\perp}$ is of dimension-zero, otherwise $y \ne 0$ and $M^{\perp}$ be a space spanned by $1$ element is of dimension-one.

    ## Exercise 7

    **Suppose $\lbrace a_n \rbrace$ is a sequence of positive numbers such that $\sum a_n b_n < \infty$ whenever $b_n \ge 0$ and $\sum b_n^2 < \infty$, prove that $\sum a_n^2 < \infty$**.

    Proof

    Since $a_n$ are all positive, if in contrary that $\sum a_n^2$ not converge then it must diverge to infinity. So suppose $\sum a_n^2 = \infty$. By definition of limit, we can split $\mathbb{N}$ to infinite many disjoint sub-intervals $N_i$ such that $s_i = \sum\limits_{n \in N_i}a_n^2 > 1$. We can write $\sum\limits_n a_n^2 = \sum\limits_{i} \sum\limits_{n \in N_i} a_n^2 = \sum\limits_i s_i$.

    Let $b_n = \frac{1}{i\sqrt{s_i}}a_n$ for $n \in N_i$, this is a positive sequence, and we have:

    1. $\sum\limits_na_nb_n = \sum\limits_n a_n^2 \frac{1}{i\sqrt{s_i}}$ $= \sum\limits_i \frac{1}{i\sqrt{s_i}} \sum\limits_{n \in N_i}a_n^2$ $=\sum\limits_i \frac{s_i}{i\sqrt{s_i}}$ $> \sum\limits_i \frac{1}{i}$ because $s_i > 1$ and this sequence diverges;
    2. $\sum\limits_n b_n^2 = \sum\limits_n \frac{1}{i^2s_i}a_n^2$ $= \sum\limits_i \frac{1}{i^2s_i} \sum\limits_{n \in N_i}a_n^2$ $= \sum\limits_i \frac{1}{i^2}$, and this sequence is known to be convergent.

    So there is positive convergent sequence $b_n$ makes $a_nb_n$ divergent, this is the negation of the original statement, thus we are finished.

    ## Exercise 9

    **If $A \subset [0,2 \pi]$ and $A$ is measurable, prove that $\lim\limits_{n \to \infty} \int_A \cos(nx)dx = \lim\limits_{n \to \infty} \int_A \sin(nx)dx = 0$**.

    Proof

    Since the whole space $[0,2\pi]$ is of finite measure, result will follow if we show $\lim\limits_{n \to \infty} \int_0^{2\pi} \cos(nx)dx = \lim\limits_{n \to \infty} \int_0^{2\pi} \sin(nx)dx = 0$.

    Now $\int_0^{2\pi}e^{inx}dx$ $=\frac{e^{inx}}{in} |_0^{2\pi}$ $= \frac{e^{2in \pi}-1}{in}$, it goes to $0$ as $n \to \infty$ because $e^{2 i n \pi}$ always have length $1$. So both real and imaginary parts, i.e. $\int_0^{2\pi} \cos(nx)dx$ and $\int_0^{2\pi} \sin(nx)dx$ go to $0$ as $n \to \infty$.

    ## Exercise 14

    **Compute $\min\limits_{a,b,c}\int\limits_{-1}^1 | x^3 - a - bx - cx^2|^2dx$ and find $\max\int\limits_{-1}^1x^3g(x)dx$, where $g$ is subject to the restrictions $\int\limits_{-1}^1g(x)dx = \int\limits_{-1}^1xg(x)dx = \int\limits_{-1}^1x^2g(x)dx = 0$ and $\int\limits_{-1}^1| g(x) |^2 dx = 1$**.

    Solution

    Consider $f(x) = x^3$, then in $H = L^2(-1,1)$ with $L^2$ norm we have $\| f \|^2 = \int\limits_{-1}^1 | x^3 |^2 dx$. Consider $M$ be span of $\langle 1,x,x^2 \rangle$ lies insider $H$, we decomposite $f$ into $Pf$ and $Qf$. By our definition of $M$, $Pf$ is of the form $a + bx + cx^2$. Since $f = Pf+Qf$ we must have $Qf = x^3 - a - bx - cx^2$.

    We know $Pf \perp Qf$, so $(Pf, Qf) = 0$, the left hand side is defined as $\int\limits_{-1}^1 (a+bx+cx^2)(x^3-a-bx-cx^2)dx$. Expand and some elementary calculus gives us ($x^{odd}$ terms just vanish) $= -\frac{2}{15}(15a^2 + 10 ac + 5b^2 - 3b + 3c^2)$ and we want non-trivial $a,b,c$ to make this $0$. An relatively obvious solution is that $a = c = 0$ and $b = \frac{3}{5}$.

    Now Theorem 4.11 tells us $\| Pf - f \|^2$ which is just our original $\int\limits_{-1}^1 | x^3 - a - bx - cx^2|^2dx$ is minimized at $a = c = 0, b = 3/5$ (also that it is actually unique). At this point $\int\limits_{-1}^1 | x^3 - a - bx - cx^2|^2dx$ becomes $\int\limits_{-1}^1 | x^3 - \frac{3}{5}x |^2dx$ and it is easy to be calculated with some elementary calculus, the answer is $= \frac{8}{175}$.

    For part two, we have $$\begin{aligned}\int\limits_{-1}^1x^3g(x)dx&= \int\limits_{-1}^1(x^3-a-bx-cx^2+a+bx+cx^2)g(x)dx\\&= \int\limits_{-1}^1(x^3-a-bx-cx^2)g(x)dx + \int\limits_{-1}^1(-a-bx-cx^2)g(x)dx\\&= \int\limits_{-1}^1(x^3-a-bx-cx^2)g(x)dx\end{aligned}$$ because by assumption we have $$\int\limits_{-1}^1g(x)dx = \int\limits_{-1}^1xg(x)dx = \int\limits_{-1}^1x^2g(x)dx = 0$$ are all zero. Now by Cauchy-Schwarz we have $$\begin{aligned}\int\limits_{-1}^1 (x^3-a-bx-cx^2)g(x)dx &\le (\int\limits_{-1}^1(x^3-a-bx-cx^2)^2dx)^{1/2}(\int\limits_{-1}^1(g(x))^2dx)^{1/2} \\ &=(\int\limits_{-1}^1(x^3-a-bx-cx^2)^2dx)^{1/2}\end{aligned}$$ because by assumption we have $$\int\limits_{-1}^1| g(x) |^2 dx = 1.$$ So we see the $\max\int\limits_{-1}^1x^3g(x)dx$ is bounded above by the square-root of the answer of part 1, i.e. $\max\int\limits_{-1}^1x^3g(x)dx \le \sqrt{\frac{8}{175}}$. The equality in Cauchy-Schwarz in our case is achievable (equality is achieved if $g(x)$ is a multiple of $f(x)$. In our case let $g(x)$ be $\sqrt{\frac{175}{8}}(x^3- \frac{3}{5}x)$ will do the job), so the maximum is indeed $\sqrt{\frac{8}{175}}$.

    ## Exercise 16

    **If $x_0 \in H$ and $M$ is a closed linear subspace of $H$, prove that $\min \lbrace \| x - x_0 \| : x \in M \rbrace = \max \lbrace |(x_0, y)| : y \in M^{\perp}, \| y \| = 1\rbrace$**.

    Proof

    We can write $x_0 = Px_0 + Qx_0$, $Px_0 \in M$ and $Qx_0 \in M^{\perp}$. We know that $Px_0$ is the nearest point to $x_0$ in $M$, in other words, $\| Px_0 - x_0 \| = \min \lbrace \| x-x_0 \|:x\in M \rbrace$ which is the LHS. Move things around we have $\| Px_0 - x_0 \| = \| Qx_0 \|$, so if RHS equals $\| Qx_0 \|$ then we are done.

    First notice that if we take $y = \frac{Qx_0}{\| Qx_0 \|}$ then $y \in M^{\perp}$, $\| y \| = 1$, and $| (x_0, y) |$ $= | Qx_0\cdot \overline{\frac{Qx_0}{\| Qx_0 \|}} |$ (because $y \in M^{\perp}$, the part with $Px_0$ equals $0$.) $= \| Qx_0 \|$. We want to show it is the maximum.

    Let $y_0 \in M^{\perp}$ and $\| y_0 \| = 1$. Then $| (x_0, y_0) |$ $= | (Px_0+Qx_0, y_0) |$ $= | (Qx_0, y_0) |$ (again the part with $Px_0$ equals $0$) $= | (\frac{\| Qx_0 \|}{\| Qx_0 \|}Qx_0, y_0) |$ $= \| Qx_0 \\| (\frac{Qx_0}{\| Qx_0 \|}, y_0) |$ $\le \| Qx_0 \| \| \frac{Qx_0}{\| Qx_0 \|} \| \| y_0 \|$ $= \| Qx_0 \|$. So $\| Qx_0 \|$ is indeed an upper-bound, and since we saw it is achievable, it is the maximum. The result follows.

    """
    )
    return


if __name__ == "__main__":
    app.run()
