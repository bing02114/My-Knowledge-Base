### 1.Sample Mean and Sample Variance of a General Population

Let the distribution of population X be unknown, but we know $E(X)=\mu, D(X)=\sigma^2$. Let $X_1, X_2, \dots, X_n$ be a sample from population X.

* Sample Mean: $\bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i$
* Sample Variance: $S^2 = \frac{1}{n-1}\sum_{i=1}^{n} (X_i - \bar{X})^2$

Then we have:

$$E(\bar{X}) = \mu, D(\bar{X}) = \frac{\sigma^2}{n}$$ $$E(S^2) = \sigma^2$$

### 2.Properties of Sample Mean and Sample Variance from a Normal Population

Let $X_1, X_2, \dots, X_n \sim N(\mu, \sigma^2)$, and let $\bar{X}, S^2$ be the sample mean and sample variance, respectively. Then

* $\bar{X} \sim N(\mu, \frac{\sigma^2}{n})$
* $\frac{(n-1)S^2}{\sigma^2} \sim \chi_{n-1}^2$
* $\bar{X}, S^2$ are mutually independent

### 3.Several Important Theorems

Let $X_1, X_2, \dots, X_n$ be i.i.d. from $N(\mu, \sigma^2)$. Then (One-Sample t-statistic):

>$T = \frac{\sqrt{n}(\bar{X}-\mu)}{S} \sim t(n-1)$

Let $X_1, \dots, X_m$ be i.i.d. from $N(\mu_1, \sigma_1^2)$ and $Y_1, \dots, Y_n$ be i.i.d. from $N(\mu_2, \sigma_2^2)$, and the two samples are independent. Assume $\sigma_1^2 = \sigma_2^2 = \sigma^2$. Then (Two-Sample t-statistic):

>$$\frac{(\bar{X}-\bar{Y})-(\mu_1-\mu_2)}{\sqrt{\frac{\sigma_1^2}{m} + \frac{\sigma_2^2}{n}}} \sim N(0,1)$$
>
>Therefore:
>
>$T = \frac{(\bar{X}-\bar{Y})-(\mu_1-\mu_2)}{S_w \sqrt{\frac{1}{m} + \frac{1}{n}}} \sim t(n+m-2)$
>
>Where:
>
>$S_w = \sqrt{\frac{(m-1)S_1^2 + (n-1)S_2^2}{n+m-2}}$



