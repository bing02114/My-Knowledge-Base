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
