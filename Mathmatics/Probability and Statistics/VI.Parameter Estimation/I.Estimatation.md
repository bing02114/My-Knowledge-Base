### 1.Classfication of Estimators

Let $\hat{\theta}$ be an estimator of $\theta$. Then we have:

* If $E\hat{\theta} = \theta$, then $\hat{\theta}$ is an **unbiased estimator** of $\theta$
* As the sample size $n \to \infty$, if $\hat{\theta}$ converges in probability to $\theta$, then $\hat{\theta}$ is a **consistent estimator** of $\theta$.
* As the sample size $n \to \infty$, if $\hat{\theta}$ converges with probability 1 (almost surely) to $\theta$, then $\hat{\theta}$ is a **strongly consistent estimator** of $\theta$

### 2.Estimation using Sample Mean and Sample Variance

* The sample mean $\bar{X}_n$ is a **strongly consistent and unbiased estimator** of the population mean $\mu$
* The sample variance $S^2$ is a **strongly consistent and unbiased estimator** of the population variance $\sigma^2$
* The sample standard deviation $S$ is a **strongly consistent estimator** of the population standard deviation $\sigma$, but it is biased, as $E(S) < \sigma$
