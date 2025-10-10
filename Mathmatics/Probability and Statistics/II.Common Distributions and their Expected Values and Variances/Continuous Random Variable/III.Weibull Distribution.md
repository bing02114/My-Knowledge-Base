### 1.Definition

$$X \sim W(\lambda, \alpha)$$

>The Weibull distribution is a highly flexible continuous distribution used extensively in reliability engineering and survival analysis to model the lifetime of objects.
>
>Unlike the exponential distribution which assumes a constant failure rate, the Weibull distribution can **model failure rates that are decreasing, constant, or increasing over time**

### 2.PDF

$$f(x) = \lambda \alpha x^{\alpha-1} e^{-\lambda x^\alpha} \quad (x > 0)$$


### 3.CDF - cumulative distribution function

$$F(x) = 1 - e^{-\lambda x^\alpha} \quad (x > 0)$$

### 4.Properties

>* It is a generalization of the exponential distribution. The exponential distribution is a special case of the Weibull when its shape parameter a = 1
>
>* **The shape parameter (α) determines the nature of the failure rate. If α<1, the failure rate decreases over time (infant mortality). If α>1, the failure rate increases over time (wear-out).**