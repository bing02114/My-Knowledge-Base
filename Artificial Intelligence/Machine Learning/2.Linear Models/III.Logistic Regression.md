### 1.Objective

>To perform classification tasks using a linear model by finding a monotonic differentiable function that links the classification task's true labels with the linear model's predicted values. 

### 2.Logistic Function

>Since the unit-step function is discontinuous, the logistic function is often used as a "surrogate function"

$$sigmoid(x)=\frac{1}{1+e^{-z}}$$

### 3.Model Form

>This model uses the linear regression model's prediction result to approximate the log odds of the true label

$$ln\frac{y}{1-y}=w^{T}x+b$$
### 4.Parameter Estimation

>The parameters **w** and _b_ are estimated using the "maximum likelihood method

#### 4.1 Defining the Probability

* Linear Combination: $z=\theta^{T}x_{i}$
* Sigmoid Function: $\sigma(z)=\frac{1}{1+e{-z}}$


$$ln\frac{y}{1-y}=w^{T}x+b$$

$$p(y=1|x)=\frac{e^{w^{T}x+b}}{1+e^{w^{T}x+b}}$$

$$p(y=0|)=\frac{1}{1+e^{w^{T}x+b}}$$

$$p(y_{i}=1|x_{i};\theta)=\hat{y_{i}}=\sigma(\theta^{T}x_{i})$$

$$p(y_{i}|x_{i};\theta)=(\hat{y_{i}})^{y_{i}}(1-\hat{y_{i}})^{1-y_{i}}$$

#### 4.2 The likelihood Function


$$L(\theta)=P(y|X;\theta)=\prod^{m}_{i=1}P(y_{i}|x_{i};\theta)=\prod^{m}_{i=1}(\hat{y_{i}})^{y_{i}}(1-\hat{y_{i}})^{1-y_{i}}$$


#### 4.3 Log-Likelihood Function


$$log(L(\theta))=log(\prod^{m}_{i=1}(\hat{y_{i}})^{y_{i}}(1-\hat{y_{i}})^{1-y_{i}})$$

$$=\sum^{m}_{i=1}log((\hat{y_{i}})^{y_{i}}(1-\hat{y_{i}})^{1-y_{i}})$$

$$=\sum^{m}_{i=1}[y_{i}log(\hat{y_{i}})+(1-y_{i})log(1-\hat{y_{i}})]$$

>This expression is the core of the **Binary Cross-Entropy** loss function. Maximizing the log-likelihood is equivalent to **minimizing the negative log-likelihood**, which is the loss function we use for training.

#### 4.4 Maximization via Gradient Ascent

$$\frac{\partial L(\theta)}{\partial \theta_{j}}=\frac{\partial}{\partial \theta_{j}}\sum^{m}_{i=1}[y_{i}log(\hat{y_{i}})+(1-y_{i})log(1-\hat{y_{i}})]$$

$$\frac{\partial \hat{y_{i}}}{\partial \theta_{j}}=\frac{\partial \sigma(\theta^{T}x)}{\partial \theta_{j}}=\sigma(\theta^{T}x_{i})(1-\sigma(\theta^{T}x_{i}))\frac{\partial(\theta^{T}x_{i})}{\partial \theta_{j}}=\hat{y_{i}}(1-\hat{y_{i}})x_{ij}$$

$$\frac{\partial log(L(\theta))}{\partial \theta_{j}}=\sum^{m}_{i=1}[y_{i}\frac{1}{\hat{y_{i}}}-(1-y_{i})\frac{1}{1-\hat{y_{i}}}]\frac{\partial \hat{y_{i}}}{\partial \theta_{j}}$$

$$=\sum^{m}_{i=1}[\frac{y_{i}-\hat{y_{i}}}{\hat{y_{i}}(1-\hat{y_{i}})}](\hat{y_{i}}(1-\hat{y_{i}})x_{ij})$$

$$=\sum^{m}_{i=1}(y_{i}-\hat{y_{i}})x_{ij}$$

therefore, the gradient is:

$$\nabla_{\theta}log(L(\theta))=\sum^{m}_{i=1}(y_{i}-\hat{y_{i}})=X^{T}(y-\hat{y})$$

#### 4.5 The Parameter Update Rule

**Gradient Ascent**

$$\theta_{new}\leftarrow \theta_{old}+θnew​←θold​+η∇θ​L(θ)$$
