### 1.Shift in Perspective: From Statistics to Probability

#### 1.1 Previous Focus

>In the first half of the course, we viewed learning from a statistical viewpoint, often dealing with supervised learning data D={(x(i),y(i))}.

#### 1.2 New Focus

>We are now shifting to a probabilistic perspective, which enables broader analysis. This lecture focuses on unsupervised learning, where we only have features, x(i)∼P(X) , and our goal is **Density Estimation**.

***
### 2.Foundations of Probability

#### 2.1 Sample Space $\Omega$

>The collection of all possible outcomes of an experiment.

#### 2.2 Event Space A

>The set of outcomes we can measure , often the powerset of the sample space.

#### 2.3 $\sigma-Algebra$

>The formal definition for the event space. It is a collection of subsets A of Ω that must be closed under complements and countable unions. This ensures that if we can measure an event E, we can also measure "not E" (Ec).

#### 2.4 Probability Measure P

>A function that maps events in the σ-algebra to a value between [0, 1]. It must satisfy:

1. $P(\Omega)=1$
2. $P(B) \geq 0$
3. $P(U^{\infty}_{i=1}B_i)=\sum^{\infty}_{i=1}P(B_i)$

#### 2.5 Cumulative Distribution Function CDF

>For continuous sets (like the real numbers R), the CDF F(x) defines the probability P(X≤x). It is a function F:R→[0,1] that is monotonic , right-continuous , and has limits F(−∞)=0 and F(∞)=1.

#### 2.6 Probability Density Function PDF

>The derivative of the CDF. This function p(x) is what we typically work with.

#### 2.7 Key Takeaway

>When we write x∼p(x), we are simply talking about a function, the PDF.

***
### 3.Key Probability Rules & Distribution

#### 3.1 Joint Probability 

$$P(x,y)$$
#### 3.2 Marginal Distribution

$$P(x)=\int_{\Omega_y}P(x,y)dy$$

#### 3.3 Conditional Probability

$$P(x|y)=\frac{P(x,y)}{P(y)}$$

#### 3.4 Independence

$$P(x,y)=P(x)P(y)$$

#### 3.5 Expectation

$$E[x]=\int_{\Omega_x}xp(x)dx$$
***
### 4.Density Estimation & Maximum Likelihood Estimation

>**Density Estimation** is the task of finding which distribution best fits our observed data

#### 4.1 Step1: Make Assumptions (i.i.d.)

* **Identically Distributed:** We assume all data points x(i) come from a single, unknown distribution p(x)
* **Independently Distributed:** We assume the observations are independent of each other.

#### 4.2 Define the Likelihood Function L($\theta$)

* The Likelihood measures the "goodness of fit" of a parameter θ′ (e.g., λ′)
* It is the joint probability of observing all our data given that parameter: L(θ′)=P(x(1),...,x(m);θ′).
* Because of the **independence** assumption, this joint probability becomes a product:

$$L(\theta')=\prod^{m}_{i=1}P(x^{(i)};\theta')$$

#### 4.3 Define the MLE Problem

* The **Maximum Likelihood Estimator (MLE)** is the parameter θ that _maximizes_ this likelihood function.

$$\theta_{MLE}=\arg\max_{\theta}\prod^{m}_{i=1}P(x^{(i)};\theta)$$

#### 4.4 Solve the Optimization 

* Optimizing a product (∏) is difficult. We can transform it into a sum (∑) by taking the `log`.
* This is valid because the `log` function is strictly increasing, so it preserves the location of the maximum (it doesn't change the `argmax`).

$$LL(\theta)=\log L(\theta)=\sum^{m}_{i=1}\log P(x^{(i)};\theta)$$

* **Negative Log-Likelihood (NLL):** By convention, optimizers often _minimize_. We can simply negate the LL to turn the problem into a minimization.

$$\arg\max_{\theta}LL(\theta)=\arg\min_{\theta}(-LL(\theta))=:\arg\min_{\theta}NLL(\theta)$$


### 5.Exponential Families and the Method of Moments

#### 5.1 Expoential Family

>A class of distributions that unifies many common PDFs. The canonical form is

$$p(x;\theta)=\frac{h(x)\exp(\theta^{T}s(x))}{z(\theta)}$$
* h(x): Base measure.
* s(x): **Sufficient Statistic** (contains all information needed from x).
* z(θ): Normalizing constant (or partition function).

#### 5.2 MLE for Exponential Families

**Key Identity**

$$\frac{d}{d\theta}\log z(\theta)=E_{\theta}[s(X)]$$
>The derivative of the log-normalizer is the expectation of the sufficient statistic


#### 5.3 The MLE First-Order Condition

>Setting the NLL derivative to zero yields a powerful result:

$$E_{\theta}[s(X)]=\frac{1}{m}\sum^{m}_{i=1}s(x^{(i)})$$

* This means the MLE is the parameter θ that makes the **theoretical expectation of the sufficient statistic** equal to its **empirical sample estimate**.

#### 5.4 Method of Moments MoM

>This identity motivates the MoM. The MoM sets the theoretical moments (like the mean, E[xk]) of a distribution equal to their sample estimators and solves for the parameters .

* For the exponential distribution, s(x)=x. The condition becomes $$E_λ​[X]=\frac{1}{m}​∑x^{(i)}.$$
* We know the theoretical mean is $E_λ​[X]=1/λ.$
* Solving $1/\lambda=\hat{\mu}_m$​ gives the MoM estimator $\hat{\lambda}_{MoM}=1/\hat{\mu}_m$, which is the same as the MLE


#### 5.5 MoM vs. MLE

>This is **not a general result**. However, for exponential family distributions in their normal (canonical) form with a single parameter, the MoM _will_ give the same result as the MLE.
