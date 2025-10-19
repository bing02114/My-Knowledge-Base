### 1.Purpose

>The Expectation-Maximization (EM) algorithm is a powerful tool for estimating parameters in the presence of "unobserved" or "latent variables"

### 2.Basic Idea

>It is an iterative method. If the parameters were known, we could infer the optimal values of the latent variables (E-step). Conversely, if the values of the latent variables were known, we could conveniently perform maximum likelihood estimation for the parameters (M-step)

### 3.Two Steps

**E-step (Expectation)**: Using the current parameters $\theta^{t}$ ,infer the distribution of the latent variables $P(Z|X,\theta^{t})$ and compute the expectation of the log-likelihood of the complete data

**M-step (Maximization)**: Find the parameters $\theta^{t+1}$ that maximize the expected log-likelihood computed in the E-step

