### 1.Definition

Let $X_1, X_2, \dots, X_n$ be a sample from a population X. $X_{(i)}$ is called the i-th order statistic of this sample; its value is the i-th observation after sorting the sample values from smallest to largest. 

After sorting from smallest to largest as $x_{(1)}, x_{(2)}, \dots, x_{(n)}$, the sequence $X_{(1)}, X_{(2)}, \dots, X_{(n)}$ is called the order statistics.

### 2.Density Function

Let the population X have a probability density function (PDF) $f(x)$ and a cumulative distribution function (CDF) $F(x)$. Let $X_1, X_2, \dots, X_n$ be a sample. 

The density function of the k-th order statistic $X_{(k)}$ is:

$$f_{k}(x)=\frac{n!}{(k-1)!(n-k)!}[F(x)]^{k-1}[1-F(x)]^{n-k}f(x)$$


### 3.Distribution Function

 When $k=1, n$ we can obtain:

* CDF of the minimum, k=1 $F_1(x) = 1 - (1-F(x))^n$

* CDF of the maximum, k=n $F_n(x) = F(x)^n$

 