### 1.Objective

>Linear regression attempts to learn a linear model that predicts a real-valued output as accurately as possible.
>
>The goal is to make $f(x_{i})≃ y_{i}$

### 2.Parameter Estimation

#### 2.1 Least Square Method

>This method finds the parameters w and b that minimize the mean squared error (also known as square loss). It corresponds to finding a line that minimizes the sum of Euclidean distances from all sample points to the line.

$$\theta=(X^{T}X)^{-1}X^{T}y$$

#### 2.2 Variation

**Log-linear Regression**

$$lny=w^{T}x+b$$

**Generalized Linear Model**

$$y=g^{-1}(w^{T}x+b)$$

