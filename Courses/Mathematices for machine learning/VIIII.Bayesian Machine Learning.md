### 1.Bayesian Terminology

$$P(A|B)=\frac{P(B|A)P(A)}{P(B)}$$

#### 1.1 Posterior Distribution

* Our updated belief after seeing the data (observation)

#### 1.2 Likelihood

* The probability of observing our data given a hypothesis

#### 1.3 Prior Distribution

* Our prior belief before seeing any data

#### 1.4 Model Evidence

* The total probability of the observation
* This is often treated as a normalizing constant

>Because the Evidence is a constant, we often use the proportional form

**Posterior ∝ Likelihood X Prior**

***
### 2.Bayesian Probability in ML

#### 2.1 Core Idea

>Data should not determine our belief in a vacuum. We must always consider data as updating our current beliefs

#### 2.2 Mathematical Formulation

>We represent our current beliefs with a **prior distribution** and our beliefs after seeing data with a **posterior distribution**.

***
### 3.The Bayesian Workflow

1. Choose likelihood
2. Choose prior
3. Compute the posterior distribution
4. Use the posterior to make prediction & reason about uncertainty

#### 3.1 Likelihood

**Bernoulli Likelihood**

$$p(x|\theta)=\theta^{x}(1-\theta)^{x}$$
$$p(D|\theta)=\prod^{n}_{i=1}p(x^{(i)}|\theta)$$
#### 3.2 Prior

>Choosing a prior is not an easy task

**Conjugate Prior**

>A convenient choice is a conjugate prior. This is a prior distribution selected such that the posterior distribution is in the same family as the prior.

* For the Bernoulli likelihood, the conjugate prior is the **Beta distribution**.

#### 3.3 Posterior

$$p(\theta|D)∝p(D|\theta)p(\theta)$$

#### 3.4 Prediction

>To make a prediction (e.g., what is the probability of the _next_ review, x∗, being positive?), we use the **posterior predictive distribution**:

$$p(x^{*}|D)=\int p(x^{*}|\theta)p(\theta|D)d \theta$$

**Uncertainty (不确定性):** We can also quantify our uncertainty using the variance of the posterior
***
### 4.Bayesian Linear Regression

This framework can be applied to supervised learning.

#### 4.1 Likelihood

We recall the normal likelihood for linear regression

#### 4.2 Prior

A conjugate prior for a normal likelihood is another **Normal distribution**. We can choose a simple one: p(θ)=N(0,τ2I) , which has the form p(θ)∝exp(−2τ2θ⊤θ​)

#### 4.3 Posterior

We know the posterior p(θ∣D) will also be a Normal distribution. We find its parameters by combining the log-likelihood and log-prior and matching terms.

#### 4.4 Result

we can get:

**Posterior Mean $\mu$**

**Posterior Covariance $\Sigma$**

***
### 5.Key Takeaways

**Conceptual**

* From a Bayesian perspective, the model parameters (θ) are considered random, and the data is fixed.
* The core idea is that data should _update_ our beliefs, not create them in a vacuum.

**Methodological**

* Specify your likelihood.
* Choose a conjugate prior to encode beliefs.
* Solve for the posterior by matching densities, which is often easiest in log-space.