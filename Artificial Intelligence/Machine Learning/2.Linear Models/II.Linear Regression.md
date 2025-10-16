### 1.Objective

>Linear regression attempts to learn a linear model that predicts a real-valued output as accurately as possible.
>
>The goal is to make $f(x_{i})≃ y_{i}$

***
### 2.Parameter Estimation

#### 2.1 Least Square Method

>This method finds the parameters w and b that minimize the mean squared error (also known as square loss). It corresponds to finding a line that minimizes the sum of Euclidean distances from all sample points to the line.

$$\theta=(X^{T}X)^{-1}X^{T}y$$

#### 2.2 Variation

**Log-linear Regression**

$$lny=w^{T}x+b$$

**Generalized Linear Model**

$$y=g^{-1}(w^{T}x+b)$$


***
### 3.Finding the optimal parameters

#### 3.1 The Analytical Solution (Normal Equation)

**Formula**

$$\theta = (X^{T}X)^{-1}X^{T}y$$

#### 3.2 The Iterative Solution (Gradient Descent)

**Formula**

$$\theta \leftarrow \theta-η\nabla_{\theta}L(\theta)$$

$$\nabla_{\theta}L(\theta)=(2/m)X^{T}(X\theta-y)$$

#### 3.3 Comparison

|                            | $$\theta = (X^{T}X)^{-1}X^{T}y$$                 | $$\theta \leftarrow \theta-η\nabla_{\theta}L(\theta)$$ |
| -------------------------- | ------------------------------------------------ | ------------------------------------------------------ |
| Feature                    | Analytical Solution (Normal Equation)            | Iterative Solution (Gradient Descent)                  |
| Core Idea                  | Set gradient to zero and solve directly.         | Start with a guess and step downhill.                  |
| Speed                      | Very fast for small n. Very slow for large n.    | Can be slow for small n. Much faster for large n.      |
| Scalability (vs. Features) | Poor, scales with O(n3).                         | Excellent, scales with O(n) per iteration.             |
| Hyperparameters            | None.                                            | Requires tuning learning rate, iterations, etc.        |
| Feature Scaling            | Not necessary.                                   | Essential for good performance.                        |
| Exactness                  | Provides the exact mathematical solution.        | Provides an approximation of the solution.             |
| Singular Matrix （XTX）      | Fails completely.                                | Works fine, finds one of the solutions.                |
| When to Use                | When the number of features is small (< 10,000). | When the number of features is large.                  |

***
### 4. Variant of Linear Regression

#### 4.1 Introduction

>Standard linear regression, also known as **Ordinary Least Squares (OLS)**, works by finding the parameters that minimize the sum of squared errors. While powerful, it has weaknesses:

- **Overfitting**: If there are many features (especially more features than data points), the model can become too complex and fit the noise in the training data, leading to poor performance on new data.
    
- **Multicollinearity**: If features are highly correlated with each other, the model's coefficients can become unstable and very large, making the model unreliable.

#### 4.2  Ridge Regression (L2 regularization) 

>**Core Problem it Solves**: Multicollinearity and overfitting.

$$L(\theta)=||X\theta-y||^{2}_{2}+\lambda||\theta||^{2}_{2}$$

$$L(\theta)=\sum^{m}_{i=1}(\hat{y_i}-y_{i})^{2}+\lambda\sum^{n}_{j=1}\theta^{2}_{j}$$

where $\lambda$ is the regularization strength, a hyperparameter that you must tune

- **Key Effect on Weights**: The L2 penalty forces the weights to be **small**, but it does not force them to be exactly zero. It "shrinks" all coefficients towards zero, which makes the model more stable and less sensitive to individual data points. This is also known as **Weight Decay**.
    
- **Pros**:
    
    - Effectively reduces model complexity and prevents overfitting.
        
    - Mathematically guarantees that the solution is unique and stable, even if the data suffers from multicollinearity.
        
- **Cons**:
    
    - It keeps all features in the model; it just reduces their weights. This can hurt interpretability if you have hundreds of irrelevant features.

$$\nabla_{\theta}L(\theta)=(2X^{T}X\theta-2X^{T}y)+2\lambda\theta$$

$$\theta=(X^{T}X+\lambda I)^{-1}X^{T}y$$
><font color="Red">This is the closed-form solution for Ridge Regression. The addition of λI makes the matrix invertible even if XTX is singular.</font>

#### 4.3 Lasso Regreession (L1 regularization)

>**Core Problem it Solves**: Overfitting and **Feature Selection**.

$$L(\theta)=||X\theta-y||^{2}_{2}+\lambda||\theta||_{1}$$

$$L(\theta)=\sum^{m}_{i=1}(\hat{y_i}-y_{i})^{2}+\lambda\sum^{n}_{j=1}|\theta|$$

- **Key Effect on Weights**: The L1 penalty has a unique property: it can force the coefficients of the least important features to become **exactly zero**. This means Lasso can perform **automatic feature selection**, effectively removing irrelevant features from the model. The resulting model is "sparse".
    
- **Pros**:
    
    - Creates simpler, more interpretable models by discarding useless features.
        
    - Can improve model performance if many features are truly irrelevant.
        
- **Cons**:
    
    - If there is a group of highly correlated features, Lasso tends to arbitrarily select one of them and zero out the others, which can be unstable.
        
    - The loss function is not differentiable at zero, requiring more complex optimization algorithms.

$$\nabla_{\theta}L(\theta)=(2X^{T}X\theta-2X^{T}y)+\lambda sgn(\theta)$$

>Because the term sgn(θ) depends on the sign of θ itself, this equation is **not a linear system** and cannot be solved for θ using standard matrix algebra. **Therefore, Lasso Regression has no general closed-form solution.** It must be solved using iterative optimization algorithms, such as Coordinate Descent or LARS (Least Angle Regression).

#### 4.4 Elastic Net

>**Core Problem it Solves**: A compromise that gets the benefits of both Ridge and Lasso.

$$L(\theta)=||X\theta-y||^{2}_{2}+\lambda_{1}||\theta||_{1}+\lambda_{2}||\theta||^{2}_{2}$$

- **Key Effect on Weights**: It is a hybrid. It can perform feature selection like Lasso, but it is more stable in the presence of correlated features. If there is a group of correlated features, it tends to either select or discard the entire group, which is often a more desirable behavior than Lasso's arbitrary selection.
    
- **Pros**:
    
    - Often performs better than Lasso when features are highly correlated.
        
    - Combines the stability of Ridge with the feature selection of Lasso.
        
- **Cons**:
    
    - It has two hyperparameters to tune (the overall strength and the L1/L2 mix), which makes model tuning more complex.