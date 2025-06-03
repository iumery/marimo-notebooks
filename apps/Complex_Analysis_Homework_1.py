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
    ## Exercise 4

    **Solve the quadratic equation $z^2 + (\alpha + i \beta)z + \gamma + i\delta = 0$**.

    Solution

    Rewrite the equation as following: $$z^2 + (\alpha + i \beta) z + (\frac{\alpha + i \beta}{2})^2 - (\frac{\alpha + i \beta}{2})^2 + \gamma + i \delta = 0$$ (i.e. we complete the square). Move things around we get $$(z + \frac{\alpha + i \beta}{2})^2 =  (\frac{\alpha + i \beta}{2})^2 - \gamma - i \delta.$$
    Now the RHS, although complicated, must be a complex number - it could be just $0$ or complex number with only real or imaginary part. In any cases, we can calculate it without too much difficulty.

    During the class we learnt that we can take square root of any complex number. Suppose we do the calculation and get that $x + i y$ and $-x - iy$ to be the two square roots of the RHS of above equation, then since any complex number has exactly two (not necessarily distinct since the RHS could be zero) complex roots, we must have that $z + \frac{\alpha + i\beta}{2} = x+ i y$ or $z + \frac{\alpha + i \beta}{2} = -x - iy$, move $\frac{\alpha + i \beta}{2}$ to the right and we have the solutions for $z$.

    ## Exercise 1

    **Show that the system of all matrices of the special form $\begin{pmatrix} \alpha & \beta \\ -\beta & \alpha \end{pmatrix}$, combined by matrix addition and matrix multiplication, is isomorphic to the field of complex numbers**.

    Proof

    Denote the space of all such matrices as $X$, define $f: X \to \mathbb{C}$ by $\begin{pmatrix} \alpha & \beta \\ -\beta & \alpha \end{pmatrix} \mapsto \alpha + i \beta$. We need to show that $X$ is a field, $f$ is a field homomorphism, and $f$ is a bijection (assume from class we already know $\mathbb{C}$ is a field):

    1. $X$ is a field:
    	1. Associativity: this is because matrix addition and multiplication are associative;
    	2. Commutative: for addition, this is because matrix addition is commutative; for multiplication, we can check $\begin{pmatrix} \alpha & \beta \\ -\beta & \alpha \end{pmatrix} \cdot \begin{pmatrix} \gamma & \delta \\ -\delta & \gamma \end{pmatrix}$ $= \begin{pmatrix} \alpha\gamma - \beta\delta & \beta\gamma + \alpha \delta \\ -\beta\gamma - \alpha\delta & \alpha\gamma - \beta\delta \end{pmatrix}$ $= \begin{pmatrix} \gamma & \delta \\ -\delta & \gamma \end{pmatrix} \cdot \begin{pmatrix} \alpha & \beta \\ -\beta & \alpha \end{pmatrix}$;
    	3. The addition identity and multiplication identity are $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ respectively;
    	4. For any $\begin{pmatrix} \alpha & \beta \\ -\beta & \alpha \end{pmatrix}$, its additive inverse is $\begin{pmatrix} -\alpha & -\beta \\ \beta & -\alpha \end{pmatrix}$ which is easily seen lies inside $X$;
    	5. For any $\begin{pmatrix} \alpha & \beta \\ -\beta & \alpha \end{pmatrix}$ that is not the addition identity, its multiplicative inverse is $\begin{pmatrix} \frac{\alpha}{\alpha^2 + \beta^2} & \frac{-\beta}{\alpha^2 + \beta^2} \\ \frac{\beta }{\alpha^2 + \beta^2} & \frac{\alpha }{\alpha^2 + \beta^2} \end{pmatrix}$;
    	6. Distributivity: this is because matrix addition and multiplication are distributive;
    2. $f$ is a field homomorphism:
    	1. $f(\begin{pmatrix} \alpha & \beta \\ -\beta & \alpha \end{pmatrix} + \begin{pmatrix} \gamma & \delta \\ -\delta & \gamma \end{pmatrix})$ $= f(\begin{pmatrix} \alpha+\gamma & \beta + \delta \\ -\beta - \delta & \alpha + \gamma\end{pmatrix})$ $= \alpha + \gamma + i(\beta + \delta)$ $= (\alpha + i\beta) + (\gamma + i \delta)$ $= f(\begin{pmatrix} \alpha & \beta \\ -\beta & \alpha \end{pmatrix}) + f(\begin{pmatrix} \gamma & \delta \\ -\delta & \gamma \end{pmatrix})$;
    	2. $f(\begin{pmatrix} \alpha & \beta \\ -\beta & \alpha \end{pmatrix} \cdot \begin{pmatrix} \gamma & \delta \\ -\delta & \gamma \end{pmatrix})$ $= f(\begin{pmatrix} \alpha\gamma - \beta\delta & \beta\gamma + \alpha \delta \\ -\beta\gamma - \alpha\delta & \alpha\gamma - \beta\delta \end{pmatrix})$ $= \alpha\gamma - \beta\delta + i(\beta\gamma + \alpha\delta)$ $=(\alpha + i\beta)(\gamma + i \delta)$ $=f(\begin{pmatrix} \alpha & \beta \\ -\beta & \alpha \end{pmatrix}) \cdot f(\begin{pmatrix} \gamma & \delta \\ -\delta & \gamma \end{pmatrix})$;
    	3. $f(\begin{pmatrix} 1&0 \\ 0&1\end{pmatrix}) = 1$;
    3. $f$ is a bijection:
    	1. Any field homomorphism is injective;
    	2. Surjectivity is also obvious, for any $\alpha + i \beta \in \mathbb{C}$, $\begin{pmatrix} \alpha & \beta \\ -\beta & \alpha \end{pmatrix} \in X$ is the preimage.

    That proves the desired statement.

    ## Exercise 3

    **Prove that $| \frac{a-b}{1-\overline{a}b} | = 1$ if either $| a | = 1$ or $| b | = 1$. What exception must be made if $| a | = | b | = 1$**?

    Proof

    If $| a | = 1$, then $1 = a\overline{a}$, so we have $| \frac{a-b}{1 - \overline{a}b} |$ $=| \frac{a - b}{a\overline{a} - \overline{a}b} |$ $= | \frac{1}{\overline{\alpha}} \cdot \frac{a-b}{a-b} |$ $= | \frac{1}{\overline{\alpha}} | \cdot | \frac{a-b}{a-b} |$ $= 1 \cdot 1 = 1$.

    If $| b | = 1$, then $1 = b \overline{b}$, so we have $| \frac{a-b}{1 - \overline{a}b} |$ $= | \frac{a - b}{b\overline{b} - \overline{a}b} |$ $= | \frac{1}{b} | \cdot | \frac{a-b}{\overline{b} - \overline{a}} |$. Now notice that if $a = a_r + i a_i$ and $b = b_r + ib_i$, then $a - b = (a_r - b_r) + i(a_i - b_i)$ whereas $\overline{b} - \overline{a}$ $= b_r - i b_i - (a_r - ia_i)$ $=(b_r - a_r) + i(a_i - b_i)$ so their modulus are the same, so $| \frac{1}{b} | \cdot | \frac{a-b}{\overline{b} - \overline{a}} | = 1 \cdot 1 = 1$ as well.

    In the case of $| a | = | b | = 1$, we must except the case that makes the denominator of the expression, i.e. $1 - \overline{a}b$, to be zero, so we need to except the case that $\overline{a}b = 1$. Since $| a | = 1 \Rightarrow \overline{a}a = 1$, this means $b = a$ because multiplicative inverse is unique.

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

    **Prove that $| \frac{a - b}{1 - \overline{a}b} | < 1$ if $| a | < 1$ and $| b | < 1$**.

    Proof

    We will prove a stronger statement as follow: $$\begin{aligned}| \frac{a - b}{1 - \overline{a}b} | <& 1 \\ | \frac{a - b}{1 - \overline{a}b} |^2 <& 1 \\ \frac{| a - b |^2}{| 1 - \overline{a}b |^2} <& 1 \\ | a - b |^2 <& | 1 - \overline{a}b |^2 \\ (a - b)(\overline{a} - \overline{b}) <& (1 - \overline{a}b)(1 - a\overline{b}) \\ a\overline{a} + b \overline{b} - a \overline{b} - b\overline{a} <& 1 + ab\overline{ab} - \overline{a}b - a \overline{b} \\ a\overline{a} + b \overline{b} <& 1 + ab\overline{ab} \\ 0 <& (1 - a \overline{a})(1 - b \overline{b}) \\ 0 <& (1 - | a |^2)(1 - | b |^2).\end{aligned}$$ It follows that $| \frac{a - b}{1 - \overline{a}b} | < 1$ if and only if both $| a |$ and $| b |$ are strictly greater than or less than $1$, in particular the statement in the problem is proved.

    ## Exercise 2

    **Prove that the points $a_1, a_2, a_3$ are vertices of an equilateral triangle if and only if $a_1^2 + a_2^2 + a_3^2 = a_1a_2 + a_2a_3 + a_3a_1$**.

    Proof

    ($\Longrightarrow$) Proved during class.

    ($\Longleftarrow$) Rewrite the equation to get that:

    1. $a_1^2 -a_1a_2 - a_1a_3 + a_2a_3 = -a_2^2 - a_3^2 + 2a_2a_3$ which is equivalent with that $(a_1 - a_2)(a_1 - a_3) = (a_3 - a_2)(a_2 - a_3)$, or $\frac{a_1 - a_2}{a_3 - a_2} = \frac{a_2 - a_3}{a_1 - a_3}$. The later has a geometric meaning that the angle $\angle a_1a_2a_3$ is the same as $\angle a_1a_3a_2$;
    2. Now do the similar thing again but, say, interchange $a_1$ and $a_3$, we then get the angle $\angle a_1a_2a_3$ is the same as $\angle a_3a_1a_2$.

    Thus all three of the angle of the triangle are the same, that is the triangle is equilateral.

    ## Exercise 1

    **Express $\cos(3\varphi)$, $\cos(4\varphi)$ and $\sin(5 \varphi)$ in terms of $\cos(\varphi)$ and $\sin(\varphi)$**.

    Solution

    If $z = \cos(\varphi) + i \sin(\varphi)$, we know that $z^3 = \cos(3\varphi) + i \sin(3\varphi)$, from the property of conjugation we know thus $(\overline{z})^3 = \overline{(z^3)}$ $= \cos(3\varphi) - i\sin(3\varphi)$, add them together we get $(\cos(\varphi) + i\sin(\varphi))^3 + (\cos(\varphi) - i \sin(\varphi))^3 = 2\cos(3\varphi)$, and thus $\frac{(\cos(\varphi) + i\sin(\varphi))^3 + (\cos(\varphi) - i \sin(\varphi))^3}{2}$ $= \cos(3\varphi)$. Similarly, $\frac{(\cos(\varphi) + i\sin(\varphi))^4 + (\cos(\varphi) - i \sin(\varphi))^4}{2}$ $= \cos(4\varphi)$. For sine, we take subtraction to get the imaginary part, that is $\frac{(\cos(\varphi) + i\sin(\varphi))^5 - (\cos(\varphi) - i \sin(\varphi))^5}{2i} = \sin(5\varphi)$.

    ## Exercise 4

    **If $w$ is given by $w = \cos(\frac{2\pi}{n}) + i \sin(\frac{2\pi}{n})$, prove that $1 + w^h + w^{2h} + \cdots + w^{(n-1)h} = 0$ for any integer $h$ which is not a multiple of $n$**.

    Proof

    Denote the sum $1 + w^h + w^{2h} + \cdots + w^{(n-1)h}$ as $W$, then we have $w^h \cdot W = w^h + w^{2h} + \cdots + w^{nh}$. Notice now $w^{nh} = \cos(\frac{2\pi n h}{n}) + i \sin(\frac{2\pi n h}{n})$ $= 1$, thus we can continue to write $w^h \cdot W = w^h + w^{2h} + \cdots +w^{(n-1)h} + 1$ which is again $W$.

    In short, $w^h \cdot W = W$. Since $\mathbb{C}$ is a field, it follows that either $w^h = 1$ or $W = 0$. Since $h$ is not a multiple of $n$, $w^{h} = \cos(\frac{2\pi h}{n}) + i \sin(\frac{2\pi h}{n})$ $\ne \cos(2\pi) + i \sin(2\pi) = 1$, thus we must have the summation equals $0$ as desired.

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

    **Show that $z$ and $z'$ correspond to diametrically opposite points on the Riemann sphere if and only if $z \overline{z'} = -1$**.

    Proof

    ($\implies$) Suppose $w, w'$ are antipodal points, $z \in \mathbb{C}$ corresponds to $w$ and $z'$ corresponds to $w'$. Then geometrically $w$ and $w'$ lie on a great circle that passes both north and south pole. Take that interception plane, we get the following graph:

    <img src="public/Pasted image 20220912011518.png" width="600" />

    Since the line segment $ww'$ is a diameter of the circle, $\angle wNw' = 90^{\circ}$. Thus the Pythagorean Theorem tells us (length of) $ON^2 = Oz \cdot Oz'$, which in our case means $1 = | z | \cdot | z' |$. In particular, we must have $| z\overline{z'} | = 1$.

    Now imagine to 'look down from north pole':

    <img src="public/Pasted image 20220912012153.png" width="600" />

    We shall see that the line connecting $zz'$ passes the origin, which in particular means $\arg{z} = \arg{z'} + \pi$. Thus $\arg{z\overline{z'}} = \arg{z} + \arg{\overline{z'}}$ $=\arg{z} - (\arg{z} - \pi) = \pi$.

    Put them together, we have that the magnitude of $z\overline{z'}$ is $1$ and the argument of $z\overline{z'}$ is $\pi$, these information define one complex number, which is $-1$, as desired.

    ($\impliedby$) The argument also works conversely. If $z\overline{z'} = -1$ and suppose $\arg{z} = \arg{z'} + \theta$, we have $\arg{z\overline{z'}} = \pi$ which implies $\theta = \pi$, i.e. $z, z'$ lie on a line that passes through the origin, thus $w$ and $w'$ lie on a great circle that passes through both north and south pole. Now apply the converse of the Pythagorean Theorem which is also true, we get that (using the same notation as in above graph) $\angle wNw' = 90^{\circ}$ which implies $w$ and $w'$ lie on a diameter, which means they are antipodal points.

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
    ## Exercise 2

    **Verify Cauchy-Riemann's equations for the functions $z^2$ and $z^3$**.

    Solution

    Write $z = x + iy$ then $f(z) = z^2$ can be rewrite as $f(x+iy) = (x^2-y^2) + i 2xy$, or $f(x+iy) = u(x,y) + iv(x,y)$ for $u(x, y) = x^2 - y^2$ and $v(x, y) = 2 xy$. Thus $\frac{\partial u}{\partial x} = 2x$, $\frac{\partial u}{\partial y} = -2y$, $\frac{\partial v}{\partial x} = 2y$ and $\frac{\partial v}{\partial y} = 2x$. Thus it is true that $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$ and $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$.

    Similarly, $f(z) = z^3$ can be rewrite as $f(x + iy) = u(x, y) + iv(x,y)$ where $u(x,y) = x^3-3xy^2$ and $v(x,y) = 3x^2y - y^3$. Thus $\frac{\partial u}{\partial x} = 3x^2-3y^2$, $\frac{\partial u}{\partial y} = -6xy$, $\frac{\partial v}{\partial x} = 6xy$ and $\frac{\partial v}{\partial y} = 3x^2 - 3y^2$. Thus it is true that $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$ and $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$.

    So in both cases, the CR-equations are satisfied.

    ## Exercise 3

    **Find the most general harmonic polynomial of the form $ax^3 + bx^2y + cxy^2 + dy^3$. Determine the conjugate harmonic function and the corresponding analytic function by integration and by the formal method**.

    Solution

    Call this polynomial $u(x, y)$, then we need to satisfy $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$, that is, $6ax + 2by + 2cx + 6dy = 0$. Since $x, y$ are independent variable, this equation is achieved if and only if $3a = -c$ and $b = -3d$. I.e. $u(x,y) = ax^3 - 3dx^2y - 3axy^2 + dy^3$.

    We can calculate $\frac{\partial u}{\partial x} = 3ax^2 + 2bxy + cy^2$ and $\frac{\partial u}{\partial y} = bx^2 + 2cxy + 3dy^2$. Since the conjugate harmonic function, call it $v(x,y)$, needs to satisfy the Cauchy-Riemann Equations with $u$, we have that $\frac{\partial v}{\partial x} = - bx^2 - 2cxy - 3dy^2$ and $\frac{\partial v}{\partial y} = 3ax^2 + 2bxy + cy^2$. Take integral with respect to $x$ we can get $-\frac{b}{3}x^3 - cx^2y - 3dxy^2 + e$ for some constant $e$, and take integral with respect to $y$ we can get $3ax^2y + bxy^2 + \frac{c}{3}y^3 + e'$ for some constant $e'$. Put them together we have that $v(x,y) = -\frac{b}{3}x^3 - cx^2y - 3dxy^2 + \frac{c}{3}y^3 + e$, or $v(x,y) = dx^3 + 3ax^2y - 3dxy^2 - ay^3 + e$ for some constant $e$.

    By the formal method, still call the conjugate $v$, and the analytic function being $f(z)$ (whose real part is $u$). Then we have $f(z)$ $= 2u(\frac{z}{2},\frac{z}{2i}) - u(0,0)$ $=2(a\frac{z^3}{8} + b\frac{z^2}{4}\frac{z}{2i} + c\frac{z}{2}\frac{z^2}{-4} + d\frac{z^3}{-8i})$ $=a\frac{z^3}{4} + b\frac{z^3}{4i} - c\frac{z^3}{4} - d\frac{z^3}{4i}$ $=\frac{(a-i b-c+i d)}{4}(x^3 + i3x^2y - 3xy^2 - iy^3)$, replace $c = -3a$ and $b = -3d$ we get $=(a+i d)(x^3 + i3x^2y - 3xy^2 - iy^3)$. Expand it, we get the real part is $ax^3 - 3axy^2 - 3dx^2y + dy^3$ which is indeed $u$. The conjugate harmonic function $v$ is the imaginary part, which is $dx^3 + 3ax^2y - 3dxy^2 - ay^3$ and it is consistent with the above calculation (up to a constant).

    ## Exercise 4

    **Show that an analytic function cannot have a constant absolute value without reducing to a constant**.

    Proof

    Suppose $f = u + iv$, then $| f |^2 = (u + iv)(u - iv) = (u u + v v) + i(-u v + u v) = u^2 + v^2$. It is a constant by assumption.

    Take the derivative of $u^2 + v^2 =$ constant with respect to $x, y$ both side, then: $\begin{cases} u_xu+v_xv = 0 \\ u_y u + v_y v = 0 \end{cases}.$ Since $f$ is analytic, it has to satisfy the Cauchy-Riemann Equation, thus we can rewrite the above two equations as: $\begin{cases} u_x u - u_y v = 0 \\ u_xv+u_yu = 0 \end{cases}.$ Which can be viewed as: $\begin{pmatrix} u & -v \\ v & u \end{pmatrix}\begin{pmatrix} u_x \\ u_y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}.$ Noticing $det(\begin{pmatrix} u & -v \\ v & u \end{pmatrix}) = u^2 + v^2$.

    If $u^2 + v^2 = 0$ then both $u, v$ have to be $0$, thus $f = 0$ is constant. Otherwise the matrix has non-zero determinant, then the two vectors $(u, v)$ and $(-v, u)$ are linearly independent, which by definition means $u_x, u_y$ are both zero, thus $u_x, u_y, v_x, v_y$ all zero, thus both $u, v$ are constant, thus $f$ is a constant.

    ## Exercise 5

    **Prove rigorously that the functions $f(z)$ and $\overline{f(\overline{z})}$ are simultaneously analytic**.

    Proof

    Suppose $f(z)$ is analytic (that is $f'(z) = \lim\limits_{h \to 0}\frac{f(z+h) - f(z)}{h}$ exists), we want to show $(\overline{f(\overline{z})})'$ exists. We have: $$\begin{aligned} (\overline{f(\overline{z})})' :=& \lim\limits_{h \to 0} \frac{\overline{f(\overline{z+h})} - \overline{f(\overline{z})}}{h} \\ =& \lim\limits_{h \to 0}\frac{\overline{f(\overline{z}+\overline{h}) - f(\overline{z})}}{h} \\ =& \lim\limits_{h \to 0}\overline{\left(\frac{f(\overline{z}+\overline{h}) - f(\overline{z})}{\overline{h}}\right)} \\ =& \overline{\left(\lim\limits_{h \to 0}\frac{f(\overline{z}+\overline{h}) - f(\overline{z})}{\overline{h}}\right)}.\end{aligned}$$ (Each step is due to some basic properties of complex conjugate)

    The last expression can be viewed as $\overline{f'(\overline{z})}$, which is assumed to exist, thus $(\overline{f(\overline{z})})'$ exists which means $\overline{f(\overline{z})}$ is analytic. Notice now if $g(z) = \overline{f(\overline{z})}$, then $\overline{g(\overline{z})} = f(z)$, thus the converse that $\overline{f(\overline{z})}$ is analytic implies $f(z)$ is analytic is also proven.

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
    ## Exercise 1

    **Expand $(1-z)^{-m}$, $m$ a positive integer, in powers of $z$**.

    Solution

    Consider $f(z) = (1-z)^{-m}$, we know from Abel's Theorem that the expansion $f(z) = \sum a_nz^n$ is of form $$f(z) = \sum \frac{f^{(n)}(0)}{n!}z^n.$$ Notice now that for $f(z) = (1-z)^{-m}$, we have $f'(z) = -m(1-z)^{-m-1}\cdot(-1)$ $=m(1-z)^{-m-1}$, $f''(z) = m(m+1)(1-z)^{-m-2}$, and so on. In general we have $f^{(n)}(z) = m(m+1)\cdots(m+n-1)(1-z)^{-m-n}$, or we can write $f^{(n)}(z) = \frac{(m+n-1)!}{(m-1)!}(1-z)^{-m-n}$ thus $f^{(n)}(0) = \frac{(m+n-1)!}{(m-1)!}$. This works for any $n \ge 1$. For the first coefficient, it is not hard to direct calculate $f(0) = 1$.

    Substitute the above information to $f(z) = \sum\limits_{n = 0}^{\infty} \frac{f^{(n)}(0)}{n!}z^n$, we get $f(z) = 1 + \sum\limits_{n = 1}^{\infty} \frac{(m+n-1)!}{(m-1)!n!}z^n$. Notice this is of the form of binomial coefficients, so we can also write it as: $f(z) = 1 + \sum\limits_{n = 1}^{\infty} \begin{pmatrix}m+n-1\\n \end{pmatrix}z^n$ and we have the desired expansion.

    ## Exercise 3

    **Find the radius of convergence of the following power series: $\sum n^pz^n, \sum \frac{z^n}{n!}, \sum n!z^n, \sum q^{n^2}z^n~(| q | < 1), \sum z^{n!}.$**

    Solution

    So we will be evaluating some $\limsup$.

    For the first one, since we know $\limsup \sqrt[n]{| n |} = 1$, we must have $\limsup \sqrt[n]{| n^p |}$ $= \left(\limsup \sqrt[n]{| n |} \right)^p = 1^p = 1$ as well, so the radius of convergence is $1/1 = 1$ for any $p$.

    For the second and third one, notice $n! = n(n-1)\cdots 2 \cdot 1$ thus at least $\lfloor \frac{n}{2} \rfloor$ terms are greater than $\lfloor \frac{n}{2} \rfloor$ (or simply remove the floors), thus $n! > (\frac{n}{2})^{\frac{n}{2}}$ thus $\limsup \sqrt[n]{n!}$ $\ge (\frac{n}{2})^{1/2} \to \infty$ and similarly $\frac{1}{n!} < (\frac{2}{n})^{\frac{n}{2}}$ thus $\limsup \sqrt[n]{\frac{1}{n!}}$ $\le (\frac{2}{n})^{1/2} \to 0$. It follows that, by taking the reciprocal, that radius of convergence for $\sum \frac{z^n}{n!}$ is infinity, and the radius of convergence for $\sum n!z^n$ is $0$.

    For the forth one, evaluate $\limsup \sqrt[n]{| q^{n^2} |}$ $= \limsup | q |^n = 0$ for $q < 1$, thus the radius of convergence is infinity.

    For the last one, rewrite the series as $\sum z^{n!} = \sum a_nz^n$ where $a_n = \begin{cases} 1,& n = m!\text{ for some }m \\ 0,& \text{ otherwise}\end{cases}$, then it is rather clear that the radius of convergence is $\frac{1}{\limsup \sqrt[n]{a_n}}$ $= \frac{1}{\lim 1} = 1$.

    ## Exercise 4

    **If $\sum a_nz^n$ has radius of convergence $R$, what is the radius of convergence of $\sum a_nz^{2n}$? Of $\sum a_n^2z_n$**?

    Solution

    By assumption we have $\limsup\limits_{n \to \infty} \sqrt[n]{| a_n |} = \frac{1}{R}$. Write $\sum a_nz^{2n}$ $= \sum b_nz^n$ where $b_n = \begin{cases} a_{n/2},&n\text{ even}\\0,&n\text{ odd}\end{cases}$. Then it's radius of convergence is by definition $R' = \frac{1}{\limsup \sqrt[n]{| b_n |}}$ $= \frac{1}{\limsup \sqrt[n]{| a_{n/2} |}}$ $= \frac{1}{\limsup_m \sqrt[2m]{| a_m |}}$ $=\left( \frac{1}{\limsup \sqrt[m]{| a_m |}} \right)^{1/2}$ $= R^{1/2}$.

    Similarly, the radius of convergence for the second series is $R'' = \frac{1}{\limsup \sqrt[n]{| a_n^2 |}}$ $= \left(\frac{1}{\limsup \sqrt[n]{| a_n |}}\right)^2$ $= R^2$.

    ## Exercise 6

    **If $\sum a_nz^n$ and $\sum b_nz^n$ have radii of convergence $R_1$ and $R_2$, show that the radius of convergence of $\sum a_nb_nz^n$ is at least $R_1R_2$**.

    Proof

    Denote the radius of convergence of $\sum a_nb_nz^n$ to be $R$.

    By basic property of $\limsup$, we have $\limsup \sqrt[n]{| a_nb_n |}$ $= \limsup (\sqrt[n]{| a_n|} \sqrt[n]{| b_n |})$ $\le \limsup \sqrt[n]{| a_n |}\cdot\limsup \sqrt[n]{| b_n |}$. In other words, $\frac{1}{R} \le \frac{1}{R_1} \frac{1}{R_2} = \frac{1}{R_1R_2}$ which implies $R \ge R_1R_2$.

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
    ## Exercise 1

    **Find the values of $\sin(i), \cos(i), \tan(1+i)$**.

    Solution

    By definition, $\sin(i) = \frac{e^{ii} - e^{-ii}}{2i}$ $= \frac{e^{-1}-e^1}{2i}$ $= \frac{i}{2}(e - \frac{1}{e})$. Similarly, $\cos(i) = \frac{e^{ii} + e^{-ii}}{2}$ $= \frac{e^{-1}+ e^1}{2}$ $= \frac{1}{2}(\frac{1}{e}+e)$.

    Thus $\sin(1+i)$ $= \cos(1)\cdot\sin(i) + \sin(1)\cdot\cos(i)$ $= \cos(1) \cdot \frac{i}{2}(e - \frac{1}{e}) + \sin(1) \cdot \frac{1}{2}(\frac{1}{e}+e)$, and $\cos(1+i)$ $= \cos(1)\cdot\cos(i) - \sin(1)\cdot\sin(i)$ $= \cos(1)\cdot\frac{1}{2}(\frac{1}{e}+e) - \sin(1)\cdot\frac{i}{2}(e - \frac{1}{e})$, so $\tan(1+i) = \frac{\cos(1) \cdot \frac{i}{2}(e - \frac{1}{e}) + \sin(1) \cdot \frac{1}{2}(\frac{1}{e}+e)}{\cos(1)\cdot\frac{1}{2}(\frac{1}{e}+e) - \sin(1)\cdot\frac{i}{2}(e - \frac{1}{e})}$ $=\frac{\cos(1) \cdot i(e - \frac{1}{e}) + \sin(1) \cdot (\frac{1}{e}+e)}{\cos(1)\cdot(\frac{1}{e}+e) - \sin(1)\cdot i(e - \frac{1}{e})}$.

    ## Exercise 2

    **The hyperbolic cosine and sine are defined by $\cosh(z) = \frac{e^z + e^{-z}}{2}$, $\sinh(z) = \frac{e^z - e^{-z}}{2}$. Express them through $\cos(iz), \sin(iz)$. Derive the addition formulas and formulas for $\cosh(2z), \sinh(2z)$**.

    Solution

    By definition, $\cos(iz) = \frac{e^{iiz} + e^{-iiz}}{2}$ $= \frac{e^{-z}+e^{z}}{2}$, so it is the same as $\cosh(z)$, i.e. $\cosh(z) = \cos(iz)$. Similarly, $\sin(iz) = \frac{e^{iiz} - e^{-iiz}}{2i}$ $= \frac{e^{-z} - e^z}{2i}$ $=\frac{(e^z - e^{z})\cdot -1}{2i}$ $= \frac{e^z - e^{-z}}{2}\cdot i$ thus $\sin(iz) = i\sinh(z)$, or $\sinh(z) = -i\sin(iz)$.

    From above, we have $\cosh(a+b)$ $= \cos(i(a+b)) = \cos(ia + ib)$ $= \cos(ia)\cos(ib) - \sin(ia)\sin(ib)$ $= = \cos(ia)\cos(ib) + i\sin(ia)i\sin(ib)$ $=\cosh(a)\cosh(b)+\sinh(a)\sinh(b)$, using the results above. Similarly, we have $\sinh(a+b)$ $= -i\sin(i(a+b))$ $= -i(\cos(ia)\sin(ib) + \sin(ia)\cos(ib))$ $= -i\sin(ib)\cos(ia) - i\sin(ia)\cos(ib)$ $= \sinh(b)\cosh(a) + \sinh(a)\cosh(b)$.

    In particular, take $a = b = z$, we get $\cosh(2z) = \cosh^2(z) + \sinh^2(z)$, and $\sinh(2z) = 2\sinh(z)\cosh(z)$.

    ## Exercise 3

    **Find the values of $e^z$ for $z = -\frac{\pi i}{2}, \frac{3}{4}\pi i, \frac{2}{3}\pi i$**.

    Solution

    $e^{-\frac{\pi i}{2}}$ is the complex number written in $re^{i\theta}$ form with radius $1$ and $\theta = -\frac{\pi}{2}$ which is $-90$ in degree, look at the complex plane, this corresponds to the point $(0,-1)$, or $-i$ as the complex number. Similarly, $e^{\frac{3}{4}\pi i}$ corresponds to the vector with length $1$ and angle $\frac{3}{4}\pi$ which is $135$ in degree, so it corresponds to the complex number $-\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}$. Finally, $e^{\frac{3}{2}\pi i}$ has length $1$ and angle $120$ in degree, so it corresponds to $-\frac{1}{2}+i \frac{\sqrt{3}}{2}$.

    ## Exercise 4

    **For what values of $z$ is $e^z$ equal to $2$, $-1$, $i$, $-i/2$, $-1-i$, $1+2i$**?

    Solution

    1. Write $z = x + iy$, then $e^{x+iy} = 2$ is equivalent with $e^x = 2$ and $e^{iy} = 1$, so $x = \log{2}$ and $y = 0+2 n \pi$, i.e. $z = \log{2} + 2n\pi i$ for any integer $n$;
    2. Similarly, for $e^{x+iy} = -1$ we get $e^x = 1$ (so $x = 0$) and $e^{iy} = -1$, so $y = \pi + 2n\pi$, i.e. $z = (\pi + 2n\pi)i$ for any $n$;
    3. For $e^{x + iy} = i$, we have $e^x = 1$ so $x = 0$, and $e^{iy} = i$ so $y = \frac{\pi}{2}  + 2n \pi$, so $z = (\frac{\pi}{2}  + 2n \pi)i$;
    4. For $e^{x + iy} = -i/2$, we have $e^x = \frac{1}{2}$ and $e^{iy} = -i$, so $x = \log{\frac{1}{2}} = -\log{2}$ and $y = \frac{3}{2}\pi + 2n \pi$, so $z = -\log{2} + (\frac{3}{2}\pi + 2n \pi)i$;
    5. For $e^{x + iy} = -1-i$, we have $e^x = \sqrt{2}$ and $e^{iy} = -\frac{\sqrt{2}}{2} - i \frac{\sqrt{2}}{2}$, so $x = \log{2^{1/2}} = \frac{1}{2}\log{2}$ and $y = \frac{5}{4}\pi + 2n\pi$, so $z = \frac{1}{2}\log{2} + (\frac{5}{4}\pi +2n\pi)i$;
    6. For $e^{x + iy} = 1+2i$, we have $e^x = \sqrt{5}$ and the radius between $i + 2i$ and $x$-xis is $\tan^{-1}{2}$, so $x = \frac{1}{2}\log{5}$ and $y = \tan^{-1}{2} + 2n \pi$, so $z = \frac{1}{2}\log{5} + (\tan^{-1}{2}+ 2n \pi)i$.

    ## Exercise 6

    **Determine all values of $2^i, i^i, (-1)^{2i}$**.

    Solution

    1. By definition, $2^i = e^{i\log{2}}$, where $\log{2} = \log{2} + 2n\pi i$, so $2^i = e^{i\log{2}-2n\pi}$ $=e^{i\log{2}}/e^{2n\pi}$ for any $n$;
    2. Similarly, $i^i = e^{i \log{i}}$. Now $\log{i} = \log{1} + (\frac{1}{2}\pi + 2n\pi)i$ $=(\frac{1}{2}\pi + 2n\pi)i$. So $i^i = e^{-\frac{1}{2}\pi - 2n\pi} = \frac{1}{e^{\frac{1}{2}\pi}e^{2n\pi}}$ for any $n$;
    3. Similarly, $(-1)^{2i} = e^{2i\log{-1}}$, where $\log{-1} = \log{1} + (\pi + 2n\pi)i$ $= (\pi + 2n \pi)i$, so $(-1)^{2i} = e^{-2\pi -4n\pi} = \frac{1}{e^{2\pi}e^{4n\pi}}$ for any $n$.

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
    ## Exercise 1

    **Prove that the reflection $z \to \overline{z}$ is not a linear transformation**.

    Proof

    If the map, call it $f$, is linear then it needs to satisfy that $f(wz) = wf(z)$. But $f(wz) = \overline{wz}$ $= \overline{w} \cdot \overline{z}$ $= \overline{w} f(z)$ which does not equal to $wf(z)$ in general (if $w$ is not real). Thus $f$ is not linear.

    ## Exercise 2

    **If $T_1z = \frac{z+2}{z+3}$ and $T_2z = \frac{z}{z+1}$, find $T_1T_2z, T_2T_1z$ and $T_1^{-1}T_2z$**.

    Solution

    The inverse of $T_1$ is given as $T_1^{-1}z = \frac{3z - 2}{-z + 1}$. $T_1$ can be expressed in a matrix as $A_1 = \begin{pmatrix} 1&2\\1&3\end{pmatrix}$, $T_2$ as $A_2 = \begin{pmatrix} 1&0\\1&1\end{pmatrix}$, and $T_1^{-1}$ as $A_3 = \begin{pmatrix} 3&-2\\-1&1\end{pmatrix}$. Thus $T_1T_2$ can be expressed in matrix as $A_1A_2 = \begin{pmatrix} 3&2\\4&3\end{pmatrix}$, $T_2T_1$ as $\begin{pmatrix} 1&2\\2&5\end{pmatrix}$, and $T_1^{-1}T_2$ as $\begin{pmatrix} 1&-2\\0&1\end{pmatrix}$. Thus $T_1T_2z = \frac{3z+2}{4z+3}$, $T_2T_1z = \frac{z+2}{2z+5}$, and $T_1^{-1}T_2z = z - 2$.

    ## Exercise 1

    **Find the linear transformation which carries $0, i, -i$ into $1, -1, 0$**.

    Solution

    Call $z_1 = i$, $z_2 = 0$ and $z_3 = -i$. We know that the linear transformation $Sz = \frac{z - z_3}{z - z_4} \cdot \frac{z_2 - z_4}{z_2 - z_3}$ maps $0 = z_2$ to $1$, $-i = z_3$ to $0$, $z_4$ to $\infty$, and $z_1$ to $\frac{z_1 - z_3}{z_1 - z_4} \cdot \frac{z_2 - z_4}{z_2 - z_3}$. So it maps $i$ to $\frac{i + i}{i - z_4} \cdot \frac{0 - z_4}{0 + i} = -1$, thus $\frac{-2z_4}{i-z_4} = -1$, thus $z_4 = \frac{i}{3}$. Thus the map is $Sz = \frac{z + i}{z - \frac{i}{3}} \cdot \frac{0 - \frac{i}{3}}{0 + i}$ $= \frac{-z-i}{3z - 3i}$.

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
    ## Problem 1 4.2.2

    **Compute** $$\int_{|z| = 1}\frac{e^z}{z}dz.$$

    Solution

    Consider $f(z) = e^z$, then $f(0) = \frac{1}{2\pi i}\int_{|z| = 1} \frac{e^z}{z}dz$ thus the integral equals $2\pi i$.

    ## Problem 2 4.2.2

    **Compute** $$\int_{|z| = 2}\frac{dz}{z^2+1}$$ **by decomposition of the integrand in partial fractions**.

    Solution

    Write $\int_{|z| = 2}\frac{dz}{z^2+1}$ $= \frac{i}{2} \int \frac{1}{z+i}dz - \frac{i}{2}\int \frac{1}{z-i}dz$. Now let $f(z) = 1$, by the integral formula we get the first integral equals $2\pi i$ and so does the second one, so they combine to give $\int_{|z| = 2}\frac{dz}{z^2+1}=0$.

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
    ## Problem 1 4.2.3

    **Compute**:

    1. $\int_{| z | = 1}e^zz^{-n}dz$;
    2. $\int_{| z | = 2} z^n(1-z)^m dz$;
    3. **$\int_{| z | = \rho} |z-a|^{-4}|dz|$ ($| a | \ne \rho$)**.

    Solution

    1. We have a singularity at $0$. Consider $f(z) = e^z$, then we know (equation 24 on book) $f^{(n-1)}(0) = \frac{(n-1)!}{2\pi i} \int_{|z| = 1}\frac{e^z}{z^n}dz$ so $\int_{|z | = 1}e^zz^{-n}dz = f^{(n-1)}(0) \cdot \frac{2\pi i}{(n-1)!}$ $= \frac{2\pi i}{(n-1)!}$;
    2. We need to exam different cases of $n$ and $m$;
    	1. If they are both non-negative, then the integrand is entire thus the integral equals $0$;
    	2. If $n$ is non-negative but $m$ is negative, then we have a singularity at $1$. Consider $f(z) = z^n(-1)^{-m}$, then $f^{(-m-1)}(1) = \frac{(-m-1)!}{2\pi i} \int_{|z | = 2} \frac{z^n(-1)^{-m}}{(z-1)^{-m}}dz$. Since $f^{(-m-1)}(1) = n\cdot (n-1) \cdots (n+m+2) (-1)^{-m}$, we get that $\int_{|z| = 2} z^n(1-z)^mdz = -2\pi i \frac{n\cdot (n-1) \cdots (n+m+2)}{(-m-1)!}$ or $-2\pi i \begin{pmatrix} n\\-m-1 \end{pmatrix}$;
    	3. If $n$ is negative but $m$ is non-negative, consider $f(z) = (1-z)^m$, then with a similar calculation we get $f^{(-n-1)}(0) = (-1)^{-n-1}\begin{pmatrix}m\\-n-1 \end{pmatrix}$, thus $\int_{|z| = 2}z^n(1-z)^mdz = (-1)^{-n-1}2\pi i \begin{pmatrix} m \\ -n-1 \end{pmatrix}$;
    	4. If both $n$ and $m$ are negative number. We may separate $|z| = 2$ to two parts, one contains $0$ and one contains $1$ (oriented in same direction in the sense of Goursat's Theorem). Then the contour contains $0$ would not have $1$ as singularity, so we can use the above formula to calculate the integral on that contour; similar for the other one. Add them together, we get that $\int_{|z| = 2}z^n(1-z)^mdz$ $=2\pi i(-\begin{pmatrix} n\\-m-1 \end{pmatrix} + (-1)^{-n-1} \begin{pmatrix} m \\ -n-1 \end{pmatrix})$. Expand the binomial coefficients and we shall see they all get cancelled out, and we get that the integral equals $0$;
    3. Assume $\rho \ne 0$ otherwise it's trivial, again we need different case:
    	1. If $a = 0$, then $\int_{|z | = \rho}|z|^{-4}|dz|$ $=\int_0^{2\pi}\frac{|i\rho e^{it}|}{|\rho e^{it}|^4}dt$ $= 2\pi\cdot\frac{1}{\rho^3}$;
    	2. Otherwise, notice on $|z| = \rho$ we have $z\overline{z} = \rho^2$ thus we may write: $$\begin{aligned}\int_{|z| = \rho}\frac{1}{|z-a|^4}|dz|&=\int\frac{1}{(z-a)^2(\overline{z}-\overline{a})^2}|dz|\\&=\int\frac{1}{(z-a)^2(\frac{\rho^2}{z}-\overline{a})^2}\frac{-i\rho}{z}dz\\&=-i\rho\int\frac{z}{(\overline{a}z-\rho^2)^2(z-a)^2}dz.\end{aligned}$$
    		1. Now, suppose $a$ is inside $|z| = \rho$, then we can take $f = \frac{z}{(\overline{a}z-\rho^2)^2}$ (no singularity inside the circle), then the original integral equals $-i\rho f'(a) 2\pi i$ $=f'(a)2\rho\pi$ $=2\rho\pi\frac{\overline{a}a+\rho^2}{(\rho^2-\overline{a}a)^3}$;
    		2. Suppose $a$ is outside $|z| = \rho$, then write the integral $= \frac{-i\rho}{\overline{a}^2}\int\frac{z}{(z-\rho^2/\overline{a})^2(z-a)^2}dz$ then $\rho^2/\overline{a}$ is inside the circle, and thus by the Cauchy's formula (take $f = \frac{z}{(z-a)^2}$) we get the integral equals $-\frac{i\rho}{\overline{a}^2}f'(\frac{\rho^2}{\overline{a}})2\pi i$ $= -2\rho\pi\frac{a+\frac{\rho^2}{\overline{a}}}{(\frac{\rho^2}{\overline{a}}-a)^3\overline{a}^2}$ $=-2\rho\pi\frac{a\overline{a}+\rho^2}{(\rho^2-a\overline{a})^3}$.

    ## Problem 2 4.2.3

    **Prove that a function which is analytic in the whole plane and satisfies an inequality $| f(z) | < |z |^n$ for some $n$ and all sufficiently large $|z|$ reduces to a polynomial**.

    Proof

    Let $a$ be an arbitrary number on the plane. Let $C$ be the circle with radius $r$ so that it bounds $a$.

    We know that $f^{(k)}(a) = \frac{k!}{2\pi i} \int_C \frac{f(z)}{(z-a)^{k+1}}dz$. For the numerator we have $| f(z) | < r^n$. For the denominator, by taking $r$ large enough (so the circle is far away enough from $a$), we can assume the denominator to be bounded below by $(\frac{1}{2}r)^{k+1}$. Thus $|f^{(k)}(a)| \le \frac{k!2\pi r}{2\pi} \frac{r^n}{(r/2)^{k+1}}$.

    Now, take $k > n+1$, we see $| f^{(k)}(a) | \le \frac{m}{r^{k-n-1}}$ for certain constant $m$, thus $| f^{(k)}(a) | = 0$ because we can take arbitrary large $r$. That is, $f$ is a function with certain $k$-h (and all above) derivative being $0$, which means $f$ must be a polynomial.

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
    ## Problem 1 4.3.2

    **If $f(z)$ and $g(z)$ have the algebraic orders $h$ and $k$ at $z = a$, show that $fg$ has the order $h+k$, $f/g$ the order $h-k$, and $f+g$ an order which does not exceed $\max(h,k)$**.

    Proof

    By definition:

    1. $\lim\limits_{z \to a}|z-a|^{\alpha}|f(z)| = 0$ for $\alpha>h$;
    2. $\lim\limits_{z \to a}|z-a|^{\alpha}|f(z)| = \infty$ for $\alpha<h$;
    3. $\lim\limits_{z \to a}|z-a|^{\beta}|g(z)| = 0$ for $\beta>g$;
    4. $\lim\limits_{z \to a}|z-a|^{\beta}|g(z)| = \infty$ for $\beta<g$.

    Then (because of the naturality of modules and limit operation):

    1. If $\gamma > h+g$, then $\lim\limits_{z \to a}|z-a|^{\gamma}|f(z)g(z)|$ $= \lim\limits_{z\to a}|z-a|^{\gamma_1}|z-a|^{\gamma_2}|f(z)\|g(z)| = 0$ $= \lim\limits_{z\to a}(|z-a|^{\gamma_1}|f(z)|)\cdot\lim\limits_{z\to a}(|z-a|^{\gamma_2}|g(z)|) = 0\cdot 0 = 0$ for $\gamma_1+\gamma_2 = \gamma$ and $\gamma_1>h$, $\gamma_2 > g$;
    2. If $\gamma < h+g$, similarly write $\gamma=\gamma_1 + \gamma_2$ with $\gamma_1 < h$ and $\gamma_2 < g$, we get $\lim\limits_{z \to a}|z-a|^{\gamma}|f(z)g(z)| = \infty\cdot\infty = \infty$;
    3. If $\gamma > h-g$, write $\gamma = \gamma_1 - \gamma_2$ with $\gamma_1 > h$ and $\gamma_2 > g$, we get $\lim\limits_{z \to a}|z-a|^{\gamma}|f(z)/g(z)| = 0\cdot 0 = 0$;
    4. If $\gamma < h-g$, write $\gamma = \gamma_1 - \gamma_2$ with $\gamma_1 < h$ and $\gamma_2 < g$, we get $\lim\limits_{z \to a}|z-a|^{\gamma}|f(z)/g(z)| = \infty\cdot\infty = \infty$.

    Thus $fg, f/g$ have orders $h+k, h-k$.

    Suppose for contradiction that order of $f+g$, denoted as $l$, is larger than $\max(h,k)$, then we can pick $\gamma$ that is larger than both $h, k$ but less than $l$, we get that $\lim\limits_{z\to a}|z-a|^{\gamma}|f(z) + g(z)| \le$ $\lim\limits_{z\to a}|z-a|^{\gamma}|f(z)|$ $+ \lim\limits_{z\to a}|z-a|^{\gamma}|g(z)|$ $= 0 + 0 = 0$ (by triangle inequality), which contradict that $l$ being the order - this limit should be $\infty$ as $\gamma < l$.

    ## Problem 2 4.3.2

    **Show that a function which is analytic in the whole plane and has a non-essential singularity at $\infty$ reduces to a polynomial**.

    Proof

    Call this function $f$, it has a non-essential singularity at $\infty$, which means $g(z) = f(\frac{1}{z})$ has a non-essential singularity at $0$ (also by the description, $g$ has no other singularities elsewhere). Say the algebraic order of $g$ is $h$, there are three cases:

    1. $h = 0$, which means $g(0) \ne 0$ and analytic at $0$, so $f(z)$ is entire and bounded, thus is a constant by Liouville;
    2. $h < 0$, which means $g(z)$ has a zero of order $h$, so still $f(z)$ is entire and bounded thus a constant;
    3. $h > 0$, which means $g(z)$ has a pole of order $h$, apply Theorem 8 (Taylor) to get (at $a = 0$ and $z \ne 0$) $g(z) = \frac{B_h}{z^h} + \frac{B_{h-1}}{z^{h-1}} + \dots + \frac{B_1}{z} + \varphi(z)$ where $\varphi(z)$ is analytic at $0$. Since $g$ has no other poles, $\varphi$ is entire (and bounded) thus a constant. In particular $f(\frac{1}{z}) = \frac{B_h}{z^h} + \frac{B_{h-1}}{z^{h-1}} + \dots + \frac{B_1}{z} + c$ thus $f(z) = B_hz^h + B_{h-1}z^{h-1} + \dots + B_1z + c$ is a polynomial.

    ## Problem 3 4.3.2

    **Show that the functions $e^z, \sin(z)$ and $\cos(z)$ have essential singularities at $\infty$**.

    Proof

    Since these three functions are all known to be analytic in the whole plane, if they do not have essential singularities at $\infty$ then by last problem they reduces to a polynomial, but that is not true (none of them has derivatives stabilize to $0$).

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
    ## Problem 1 4.3.3

    **Determine explicitly the largest disk about the origin whose image under the mapping $w = z^2 + z$ is one-to-one**.

    Solution

    Let us call the open disk $D$, suppose $w$ is not injective on $D$, that is, there exists $a, b \in D$ such that $a^2 + a = b^2 + b$ with $a \ne b$, which is equivalent with $a^2 - b^2 = b - a$, divide both side by $b-a$ (it's not zero by assumption) we get $a+b = -1$. This may happen if and only if $D$ (which is open) has radius larger than $\frac{1}{2}$: if the radius is smaller than or equals to $\frac{1}{2}$ then $|a+b|\le|a|+|b|<1$, and if the radius is larger than $\frac{1}{2}$ then there is some obvious (real) solution. So the largest possible disk has radius $\frac{1}{2}$.

    ## Problem 2 4.3.3

    **Determine explicitly the largest disk about the origin whose image under the mapping $w= e^z$ is one-to-one**.

    Solution

    Similarly, suppose $w$ is not injective on $D$, that is, we have $e^a = e^b$ on $D$, which is equivalent with $e^{a-b} = 1$, which is equivalent with that $a - b = 2\pi i n$ for some $n \in \mathbb{Z}$. This is the only source of non-injectivity - in particular, the function is injective if and only if the disk do not contain two points differ by $2\pi$ in the imaginary coordinate, which means the largest possible $D$ has radius $\pi$.

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
    ## Problem 1

    **Compute** $$\int_{|z| = 4} \frac{e^z}{z(z^2+\pi^2)}dz$$ **by using residues**.

    Solution

    The function $\frac{e^z}{z(z^2+\pi^2)}$ $= \frac{e^z}{z(z+i\pi)(z-i\pi)}$ has singularity at $0, \pm i \pi$ (all are simple poles) and $|z| = 4$ encloses all of them. Let us compute the residues of the function at all those three points:

    1. Residue at $0$ is given by $\lim\limits_{z \to 0}\frac{e^z}{(z+i\pi)(z-i\pi)}$ $= \frac{1}{\pi^2}$;
    2. Residue at $i \pi$ is given by $\lim\limits_{z \to i \pi} \frac{e^z}{z(z+i\pi)}$ $= \frac{1}{2\pi^2}$;
    3. Residue at $-i\pi$ is given by $\lim\limits_{z \to -i\pi} \frac{e^z}{z(z-i\pi)}$ $= \frac{1}{2\pi^2}$ as well.

    And now by Residue Theorem, the integral in the question equals $(2\pi i)\cdot (\frac{1}{\pi^2} + \frac{2}{2\pi^2})$ $= \frac{4 i}{\pi}$.

    ## Problem 2

    **Compute** $$\int_{|z-2i| = 4}\frac{1}{\cosh(z)}dz.$$

    Solution

    We know that $\frac{1}{\cosh(z)}$ is by definition $\frac{2}{e^z + e^{-z}}$. In particular the integrand has singularity when $e^z + e^{-z} = 0$, or $e^{-z}(e^{2z}+1) = 0$. Since $e^z$ is never $0$, we get $e^{2z} = -1$ thus $2z = i\pi+2ni\pi$ and thus $z = \frac{i\pi}{2}+in\pi$ and they are all simple poles. In particular, $z = \frac{i\pi}{2} + i\pi$, $\frac{i\pi}{2}$, $\frac{i\pi}{2} - i\pi$, are the only poles inside $|z - 2i| = 4$.

    Now, use the fact that if $f = g/h$ then $\text{Res}(f,c) = \frac{g(c)}{h'(c)}$ (we need $g, h$ to be holomorphic around $c$, $h(c) = 0$ and $h'(c) \ne 0$, but they are straight-forward or we have already knew). We get that:

    1. Residue at $\frac{3i\pi}{2}$ is $\frac{2}{e^{\frac{3i\pi}{2}}-e^{-\frac{3i\pi}{2}}}$ $= i$;
    2. Similar, residue at $\frac{i\pi}{2}$ is $-i$ and;
    3. Residue at $-\frac{i\pi}{2}$ is $i$.

    Apply Residue Theorem, the result of the integral equals $(2\pi i)\cdot (i-i+i) = -2\pi$.

    ## Problem 3

    **Find the residue of $\frac{\cos(z)}{z^n}$ at $z = 0$ in terms of $n$**.

    Solution

    It is a rather well-known fact that the Taylor expansion of $\cos(z)$ at $0$ is $1 - \frac{z^2}{2!} + \frac{z^4}{4!} - \dots$ $= \sum\limits_{k = 0}^{\infty} \frac{(-1)^k z^{2k}}{(2k)!}$. Thus $\frac{\cos(z)}{z^n} = \sum\limits_{k = 0}^{\infty} \frac{(-1)^k z^{2k}}{(2k)!z^n}$. In particular, we know the residue is the coefficient of the $z^{-1}$ term, thus:

    1. If $n\le 0$, then residue is $0$;
    2. If $n > 0$ is even number, then there is no term in the series with degree $-1$ thus also we have residue is $0$;
    3. If $n > 0$ is odd equals some $2k+1$, then the coefficient of the $z^{-1}$ term is $\frac{(-1)^k}{(2k)!}$ is the residue. For example, residue of $\cos(z)/z$ at $z = 0$ is $\frac{(-1)^0}{0!} = 1$, residue of $\cos(z)/z^3$ at $z = 0$ is $\frac{(-1)^1}{2!} = -\frac{1}{2}$, and so on.

    Write the answer in $n$, we have $$\text{Res}(\frac{\cos(z)}{z^n}, 0) = \begin{cases} 0,&n\le0\text{ or }n\text{ is positive and even}, \\ \frac{(-1)^{(n-1)/2}}{(n-1)!},&n\text{ is positive and odd}.\end{cases}$$

    """
    )
    return


if __name__ == "__main__":
    app.run()
