### 1.Non-linearly Separable Problem

>For non-linearly separable problems, we can map the samples from the origin space to a higher-dimensional feature space, making them linearly separable in that space

### 2.Kernel Trick

>If the feature space dimension is very high, computing the inner product can be difficult. The "Kernel Trick" avoids this by defining a kernel function $k(x_{i},x_{j})=\phi(x_{i})^{T}\phi(x_{j})$, which calculates the inner product in the feature space as if it were computed in the original sample space, without explicitly computing the mapping.

$$k(x_{i},x_{j})=\phi(x_{i})^{T}\phi(x_{j})$$

$$f(x)=w^{T}\phi(x)+b$$

$$\max_{\alpha}\sum^{m}_{i=1}\alpha_{i}-\frac{1}{2}\sum^{m}_{i=1}\sum^{m}_{j=1}\alpha_{i}\alpha_{j}y_{i}y_{j}k(x_{i},x_{j})$$

$$f(x)=\sum^{m}_{i=1}\alpha_{i}y_{i}k(x,x_{i})+b$$

### 3.Common Kernels

#### 3.1 linear

$$K(x_{i},x_{j})=x_{i}^{T}x_{j}$$
**Feature Space**

>The mapping function is the identity function $\phi(x)=x$. The feature space is the same as the original input space

**Effect**

>It results in a standard linear classifier. The decision boundary is a straight line, a flat plane or a hyperplane.

**When to Use**

* When the data is already largely linearly separable
* When the number of features is very large compared to the number of samples

#### 3.2 Polynomial

$$K(x_{i},x_{j})=(\gamma x_{i}^{T}x_{j}+c)^{d}$$

**Parameters**:

* d(degree): It controls the degree of the polynomial
* c(coefficient): It trades off the influence of lower-degree terms versus higher-degree terms in the polynomial
* $\gamma$(gamma): A scaling factor for the dot product

**Feature Space**:

>This kernel implicitly maps the data to a higher-dimensional space that includes polynomial combinations of the original features.

**Effect**

>It creates smooth, non-linear, polynomial-shaped decision boundaries

**When to Use It**

* It is often used in problems where the relationship between classes is known to be polynomial, such as in some computer vision applications (e.g., image processing). It is more flexible than the linear kernel but is generally less popular than the RBF kernel because it has more hyperparameters to tune (`d`, `c`, `γ`) and can be numerically

#### 3.3 Gaussian / RBF 

$$K(x_{i},x_{j})=exp(-\gamma||x_{i}-x_{j}||^{2})$$
**Intution**:

The core of this formula is the squared Euclidean distance between two points, ∥xi​−xj​∥2. The kernel function essentially calculates a **similarity score** based on this distance.

- If two points xi​ and xj​ are very close, their distance is almost 0. The formula becomes exp(0), which is 1. They have maximum similarity.
    
- As the points get farther apart, their distance increases, making −γ×(distance) a large negative number. The formula exp(−large number) approaches 0. Their similarity drops off exponentially. Think of each support vector as a **lighthouse**. The RBF kernel measures the "brightness" of a new point as seen from each lighthouse. The closer the new point is to a support vector (a lighthouse), the higher its score (the brighter it appears). The final decision is based on the combined brightness from all the red lighthouses versus all the blue lighthouses.

**Parameters**

**`γ` (gamma):** This is a crucial parameter. It controls the "radius of influence" of each support vector (the width of the Gaussian bell curve).

- **Low `γ`**: The "light" from the lighthouse spreads very far. The influence is broad, leading to a smoother, simpler decision boundary (low variance, high bias).
    
- **High `γ`**: The light is very focused. The influence is narrow and local. Each support vector only affects its immediate vicinity, leading to a highly complex, wiggly decision boundary that can perfectly fit the training data but might be overfitting (high variance, low bias).

**Effect**

>It can create highly complex, non-linear boundaries of any shape. It's excellent for separating clusters that are intertwined or have complex shapes

**When to Use**

>When you have no prior knowledge about your data's structure, the RBF kernel is a robust and powerful first choice.


#### 3.4 Laplace

$$K(x_{i},x_{j})=exp(-\gamma||x_{i},x_{j}||_{1})$$

**Intution**

>The decay in similarity is less steep compared to the Gaussian kernel. Because the distance is not squared, the influence of points that are far away diminishes more slowly. This can make it more robust in certain situations. While the Gaussian RBF's similarity drop-off is a sharp bell curve, the Laplace kernel's is a sharper, pointier exponential curve.

**When to Use it**

>It is less common than the RBF kernel but can be a useful alternative. It is sometimes considered slightly more robust to noise or for data that has features on different scales, although proper data scaling is always recommended. It's a good candidate to try if the RBF kernel seems too sensitive or is not performing optimally.

#### 3.5 Sigmoid

$$K(x_{i},x_{j})=tanh(\gamma x_{i}^{T}x_{j}+c)$$

**Intuition**

>This formula mimics the activation of a single neuron in a **two-layer perceptron (a simple neural network)**. The term γxiT​xj​+c is like the weighted sum of inputs plus a bias, and the `tanh` function is the activation function that squashes the output to a range between -1 and 1. An SVM with a sigmoid kernel is, in some ways, equivalent to a simple two-layer neural network.

**Parameters**

>`γ` (gamma) and `c` (coefficient) act as the slope and intercept of a neuron's activation.

**When to Use It**

>**It is generally not recommended.** For many combinations of `γ` and `c`, the sigmoid kernel is not a valid kernel (it doesn't satisfy Mercer's Theorem), meaning the resulting optimization problem may not be convex and can be difficult to solve. Its performance is often worse than the RBF kernel. It should only be considered if you have a strong prior belief that your data follows this type of activation pattern, which is rare.