
### 1.Definition

Let $X_1, X_2, \dots, X_n$ be a sample from a standard normal distribution $N(0,1)$, and let
$$X = \sum_{i=1}^{n} X_i^2$$
The X is a chi-squared random variable with n degrees of freedom, and its distribution is called the chi-squared distribution with n degrees of freedom, denoted as $$X \sim \chi_n^2$$

### 2.Probability Density

The probability density function (PDF) is:

$$f_n(x) = \begin{cases} \frac{1}{2^{n/2}\Gamma(\frac{n}{2})} x^{\frac{n}{2}-1}e^{-\frac{x}{2}}, & x > 0 \\ 0, & x \le 0 \end{cases}$$

One can observe the relationship between the chi-squared distribution with n degrees of freedom and the Gamma distribution:

$$X = \sum_{i=1}^{n} X_i^2 \sim \Gamma(\frac{n}{2}, \frac{1}{2})$$

![](Mathmatics/Probability%20and%20Statistics/images/chisquared.png)

### 3.Properties


### 4.Upper α-Quantile
