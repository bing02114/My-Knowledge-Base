### 1.Goal

>A common stratrgy for estimating class-conditional probabilities is to first assume a specific probability distribution form and then estimate the distribution's parameters based on the training samples. The training process of a probability model is essentially a parameter estimation process

### 2.Maximum Likelihood Estimation (MLE)

>MLE is a classic method for estimating probability distribution parameters from data samples

### 3.Process

>Given the dataset $D_c$ for class c, the likelihood of the parameters $\hat{\theta}_c$ is $P(D_c|\theta_c)=\prod_{x\in D_c}P(x|\theta_c)$. MLE seeks to find the parameter value θ^c​ that maximizes this likelihood (or more commonly, the log-likelihood).

$$LL(\theta_c)=\sum_{x\in D_c}logP(x|\theta_c)$$
### 4.Limitation

>The accuracy of the estimation heavily depends on whether the assumed probability distribution form matches the underlying true data distribution.