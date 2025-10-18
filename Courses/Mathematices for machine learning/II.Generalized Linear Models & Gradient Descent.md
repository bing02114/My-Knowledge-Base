### 1.Generalized Linear Models (GLMs)

#### 1.1 Core Idea

>A GLM applies a **link function**, g, to the linear prediction


$$y=g^{-1}(\theta^{T}x)$$

#### 1.2 Example

**1.Poisson Regression**

$$\hat{y}=exp(\theta^{T}x)$$

**2.Logistic Regression**

$$\hat{y}=\sigma(\theta^{T}x)=\frac{1}{1+e^{-\theta^{T}x}} $$

![](Courses/Mathematices%20for%20machine%20learning/images/LogisticRegression.jpg)

***
### 2.Gradient Descent

#### 2.1 The Algorithm

**Initialize:** Start with a random guess for the model parameters θ.

**Compute Gradient:** Calculate the gradient of the loss function with respect to the parameters, ∇θ​L. The gradient points in the direction of the steepest increase of the loss.

**Update Parameters:** Take a small step in the _opposite_ direction of the gradient to move towards a minimum of the loss function. The size of this step is controlled by the **learning rate** α. The update rule is: θ(t+1)=θ(t)−α∇θ​L. Note: the slide incorrectly shows a '+', but the principle of descent is to subtract the gradient

**Repeat:** Go back to step 2 and repeat for a fixed number of iterations or until the loss stops decreasing

#### 2.2 Hyperparameters

**Learning Rate (α) :** A critical parameter. If it's too small, convergence is very slow. If it's too large, the algorithm may overshoot the minimum and fail to converge.

**Number of Iterations/Epochs:** Determines how many update steps the algorithm takes. More iterations generally lead to better convergence, up to a point where the loss plateaus

***
### 3.Computational Complexity Comparison

#### 3.1 Normal Equation (Closed-Form Solution)

$$(X^{T}X)^{-1}X^{T}y$$

* The complexity is dominated by the matrix inversion, which is approximately $O(n^{3})$, where n is the number of features. The full complexity is $O(n^{2}m+n^{3})$, where m is the number of data points
* This becomes very slow when the number of features is large.

#### 3.2 Gradient Descent (Iterative Solution)

* Each iteration involves calculating the gradient, which primarily consists of matrix-vector products (X⊤(Xθ−y))
* The complexity of one iteration is about O(mn)
* The total complexity is **O(kmn)** for k iterations.
* Gradient Descent is much more efficient than the Normal Equation when the number of features (n) is large, and it's the only option for models without a closed-form solution. For very large datasets, **Stochastic Gradient Descent (SGD)** can be used, which further reduces the complexity to O(kbn) where b is a small batch size.