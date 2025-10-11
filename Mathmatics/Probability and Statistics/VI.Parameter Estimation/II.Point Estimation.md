### 1.Method of Moments

#### 1.1 Definition

>The method of moments is an estimation method based on a simple substitution idea. 
>
>Its basic principle is to use sample moments to estimate the corresponding population moments.
>
>If an unknown parameter is related to a certain population moment, one can naturally construct this sample moment to estimate the unknown parameter.

#### 1.2 Sample Moments

k-th sample raw moments:

$a_k = \frac{1}{n} \sum_{i=1}^{n} X_i^k$

k-th sample central moment:

$m_k = \frac{1}{n} \sum_{i=1}^{n} (X_i - \bar{X})^k$

Guaranteed by the Law of Large Numbers:

$a_k \xrightarrow{p} \alpha_k$

$m_k \xrightarrow{p} \mu_k$

#### 1.3 Common Method of Moments Estimations

**In the Poisson Distribution P(λ)**

>We have $\lambda = E(X) = \alpha_1$. The moment estimator of $\alpha_1$ is $a_1$, therefore:
>
>$$\hat{\lambda} = a_1 = \frac{1}{n} \sum_{i=1}^{n} X_i$$

**In the Exponential Distribution E(λ)**

>We have $\mu = E(X) = \frac{1}{\lambda} \Rightarrow \lambda = \frac{1}{E(X)} = \frac{1}{\alpha_1}$. The moment estimator of $\alpha_1$ is $a_1$, therefore:
>
>$$\hat{\lambda} = \frac{1}{a_1} = \frac{1}{\frac{1}{n} \sum_{i=1}^{n} X_i}$$

**In the Normal Population N(μ,σ2)**

>We have $\mu = E(X) = \alpha_1$ and $\sigma^2 = E(X^2) - (E(X))^2 = \alpha_2 - \alpha_1^2$. The moment estimators of $\alpha_1$ and $\alpha_2$ are $a_1$ and $a_2$ respectively. Therefore, we use them to estimate $\mu$ and $\sigma^2$ as follows:
>
>$$\hat{\mu} = a_1 = \frac{1}{n} \sum_{i=1}^{n} X_i$$ 
>$$\hat{\sigma}^2 = a_2 - a_1^2 = \frac{1}{n} \sum_{i=1}^{n} X_i^2 - \left(\frac{1}{n} \sum_{i=1}^{n} X_i\right)^2$$

**In the Uniform Population U(a,b)**

>We have the following relationships for the population moments:
>
>$$\alpha_1 = EX = \frac{a+b}{2}$` `$\alpha_2 - \alpha_1^2 = D(X) = \frac{(b-a)^2}{12}$$
>
>Therefore, solving this system of equations for a and b yields:
>
>$$a = \alpha_1 - \sqrt{3(\alpha_2 - \alpha_1^2)}$` `$b = \alpha_1 + \sqrt{3(\alpha_2 - \alpha_1^2)}$$
>
>So, we respectively use the sample moments $a_1$ and $a_2$ to estimate the parameters a and b:
>
>$$\hat{a} = a_1 - \sqrt{3(a_2 - a_1^2)}$$
> $$\hat{b} = a_1 + \sqrt{3(a_2 - a_1^2)}$$



***
### 2.Maximum Likelihood Estimation

#### 2.1 Definition

>Let $X=(X_1, \dots, X_n)$ be a sample drawn from a population with a probability function $f(x; \theta)$, where $\theta$ is an unknown parameter or a vector of unknown parameters. Let $x=(x_1, \dots, x_n)$ be the observed values of the sample. 
>
>For a given $x$, let $\hat{\theta} = \hat{\theta}(x)$ satisfy the following condition:
>
>$L(\hat{\theta}) = \max_{\theta \in \Theta} L(x; \theta)$
>
>Then $\hat{\theta}$ is called the **Maximum Likelihood Estimate (MLE)** of $\theta$, and $\hat{\theta}(X)$ is the **Maximum Likelihood Estimator**. $L(x; \theta)$ is the **Likelihood Function**. 
>
>If $\hat{\theta}$ is the MLE of $\theta$, then $g(\hat{\theta})$ is the MLE of $g(\theta)$. Since $\ln L(\theta)$ and $L(\theta)$ have the same maximum point, one can also use $\ln L(\theta)$ for MLE. Usually, $l(\theta) = \ln L(\theta)$ is called the **Log-Likelihood Function**.

#### 2.2 Specific Operational Method

Finding the maximum likelihood estimate is equivalent to **finding the maximum value of the likelihood function**. In the case of a simple random sample:

$$L(x; \theta) = \prod_{i=1}^{n} f(x_i; \theta)$$

* If the likelihood function is monotonic with respect to $\theta$, the maximum point can be found directly using its monotonic property.

* If the likelihood function is not monotonic and is differentiable with respect to $\theta$, we can find its stationary points by letting:

$$\frac{dL(\theta)}{d\theta} = 0$$

	* or

$$\frac{dl(\theta)}{d\theta} = 0$$

* When $\theta$ is a vector (multivariable), let:

$$\frac{\partial l(\theta)}{\partial \theta_i} = 0$$

* Then, determin whether these stationary points are the maximum value.



