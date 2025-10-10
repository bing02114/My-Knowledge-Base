### 1.Gamma Function

$$\Gamma(\alpha) = \int_0^\infty x^{\alpha-1}e^{-x}dx, \quad \alpha > 0$$

### 2.Definition

$$X \sim \Gamma(\alpha, \beta)$$

>The Gamma distribution is a flexible, two-parameter family of right-skewed continuous probability distributions.
>
>It can be seen as a generalization of the exponential distribution and is often used to **model the waiting time until the a-th event occurs in a Poisson process**

### 3.Probability Density Function

$$f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1}e^{-\beta x}, \quad (x \ge 0)$$

### 4.Expectation and Variance

$$E(X) = \frac{\alpha}{\beta}, D(X) = \frac{\alpha}{\beta^2}$$

### 5.Properties

>* **The sum of α independent and identically distributed exponential random variables** is a Gamma random variable with shape parameter α
>
>* **The Exponential distribution and the Chi-squared distribution are special cases of the Gamma distribution** 