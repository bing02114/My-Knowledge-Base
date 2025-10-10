### 1.Definition

$$\ln X \sim N(\mu, \sigma^2)$$

>A lognormal distribution is a continuous probability distribution of a random variable whose natural logarithm is normally distributed.
>
>It is used to model random quantities that are always positive and have a right-skewed distribution

### 2.PDF

$$f(x) = \frac{1}{x\sigma\sqrt{2\pi}} \exp\left[-\frac{(\ln x - \mu)^2}{2\sigma^2}\right]$$

### 3.Expectation and Variance

$$E(X) = e^{\mu + \frac{\sigma^2}{2}}, D(X) = (e^{\sigma^2} - 1)e^{2\mu + \sigma^2}$$

### 4.Properties

>**The product of independent lognormally distributed random variables is also lognormally distributed.**