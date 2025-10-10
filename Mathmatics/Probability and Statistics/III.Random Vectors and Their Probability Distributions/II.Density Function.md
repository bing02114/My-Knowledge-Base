### 1.Joint Density Function

>Let (X,Y) be a random vector. If there exists a non-negative function $$f(x,y)$$ on $$\mathbb{R}^2$$
>such that for any rectangular set $$D = \{(x,y) | a < x \le b, c < y \le d\}$$
>in $$\mathbb{R}^2$$ the following holds:
>
>$$P((X,Y) \in D) = \iint_D f(x,y) dxdy$$

### 2.Marginal Density Function

>If $$f(x,y)$$ is the joint density of a random vector (X,Y), then the marginal densities of X and Y, denoted as $$f_{X}(x)$$ and $$f_{Y}(y)$$ respectively (also called marginal density), can be obtained by integrating out the other variable：
>
>$$f_X(x) = \int_{-\infty}^{\infty} f(x,y) dy$$
>$$f_Y(y) = \int_{-\infty}^{\infty} f(x,y) dx$$

### 3.Independence

>Let X,Y have marginal probability densities $$f_{X}(x)$$
>$$f_{Y}(y)$$
>The necessary and sufficient condition for X,Y to be mutually independent is that the random vector (X,Y) has a joint density $$f(x,y)$$ such that:
>
>$$f(x,y) = f_X(x) f_Y(y)$$

>If X,Y are known to be independent, then for a given X=x0, the ranges of values for Y is independent of x0

>If $$(X_1, X_2, \dots, X_n)$$ is a continuous random vector, its joint probability density function $$f(x_1, \dots, x_n)$$ can be represented as a product of n functions $$g_1, \dots, g_n$$
>where each $$g_i$$ depends only on $$x_i$$
>Then $$X_1, \dots, X_n$$ are mutually independent, and the marginal density function of each  $$X_i$$
>: $$f_{X_i}(x_i)$$
>differs from $$g_{i}(x+{i})$$ only by a constant factor

