### 1.Functions of Discrete Random Vectors

**Additive Property of Poisson Distribution**

>If $$X_1, X_2, \dots, X_n$$ are mutually independent and $$X_i \sim P(\lambda_i)$$, then:
>
>$$Z_n = X_1 + X_2 + \dots + X_n \sim P(\lambda_1 + \lambda_2 + \dots + \lambda_n)$$

**Additive Property of Binomial Distribution**

>If $$X_1, X_2, \dots, X_n$$ are mutually independent and $$X_i \sim B(m_i, p)$$, then:
>
>$$Z_n = X_1 + X_2 + \dots + X_n \sim B(m_1 + m_2 + \dots + m_n, p)$$

**Additive Property of Normal Distribution**

>If $$X_1, X_2, \dots, X_n$$ are mutually independent and $$X_i \sim N(\mu_i, \sigma_i^2)$$, then a linear combination is also normally distributed:
>
>$$Z_n = c_0 \pm c_1 X_1 \pm c_2 X_2 \pm \dots \pm c_n X_n \sim N(c_0 \pm c_1 \mu_1 \pm c_2 \mu_2 \pm \dots \pm c_n \mu_n, c_1^2 \sigma_1^2 + c_2^2 \sigma_2^2 + \dots + c_n^2 \sigma_n^2)$$

### 2.Functions of Continuous Random Vectors

**Addition**

>Let $$(X,Y)$$ have a joint density $$f(x,y)$$. The probability density of $$U=X+Y$$ is given by:
>
>$$f_U(u) = \int_{-\infty}^{\infty} f(x, u-x)dx = \int_{-\infty}^{\infty} f(u-y, y)dy$$
>When X,Y are independent
>
>$$f_U(u) = \int_{-\infty}^{\infty} f_X(x) f_Y(u-x)dx = \int_{-\infty}^{\infty} f_X(u-y) f_Y(y)dy$$

**Subtraction**

>Let $$(X,Y)$$ have a joint density $$f(x,y)$$. The probability density of $$V=X-Y$$ is given by:
>
>$$f_V(v) = \int_{-\infty}^{\infty} f(x, x-v)dx = \int_{-\infty}^{\infty} f(v+y, y)dy$$
>When X,Y are independent
>
>$$f_V(v) = \int_{-\infty}^{\infty} f_X(x) f_Y(x-v)dx = \int_{-\infty}^{\infty} f_X(v+y) f_Y(y)dy$$

**Extreme Values**

>**Maximum Value**
>
> Let $$(X,Y)$$ have a joint density $$f(x,y)$$. The probability density of $$Z = \max(X,Y)$$ is:
> 
> $$f_{max}(z) = f_X(z)f_Y(z)$$
>
>**Minimum Value**
>
>Let $$(X,Y)$$ have a joint density $$f(x,y)$$. The probability density of $$Z = \min(X,Y)$$ is:
> 
> $$f_{min}(z) = 1-(1-f_{X}(z))(1-f_{Y}(z))$$

### 3.Joint PDF of Functions of Random Vectors

If $$x = x(u,v), y = y(u,v)$$ has continuous partial derivatives in an open set D on the plane, and the Jacobian determinant is

$$J = \frac{\partial(x,y)}{\partial(u,v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix} \ne 0$$

Then we have:

$$dxdy = \left| \frac{\partial(x,y)}{\partial(u,v)} \right| dudv = |J|dudv, \quad (u,v) \in D$$
Then, using this, we obtain the joint density of the random vector $$(U,V)$$: $$g(u,v) = f(x(u,v), y(u,v))|J|$$

### 4. Conditional Probability Density

The conditional probability density function is defined as:

$$f_{X|Y}(x|y) = \frac{f(x,y)}{f_Y(y)}$$

Therefore, the necessary and sufficient condition for X,Y to be indenpendent is $$f_{X|Y}(x|y) = f_X(x)$$
