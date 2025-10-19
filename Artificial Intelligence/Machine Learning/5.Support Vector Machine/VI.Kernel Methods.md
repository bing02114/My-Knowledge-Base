### 1.General Model Form

>Both Support Vector Machines (SVMs) and Support Vector Regression (SVR) produce models that can be expressed as a linear combination of kernel functions evaluated on the training samples. This is known as the "representer theorem"

### 2.Representer Theorem

#### 2.1 Statement

>The theorem states that for a broad class of optimization problems (with a monotonically increasing regularization term and an arbitrary non-negative loss function), the optimal solution can always be written as a linear combination of kernel functions evaluated at the training points.


$$\min_{h\in H}F(h)=\Omega(||h||_{H})+l(h(x_{1}),\dots,h(x_{m}))$$

$$h^{*}(x)=\sum^{m}_{i=1}\alpha_{i}K(x,x_{i})$$

#### 2.2 Significance

>The theorem's power lies in its generality; it is not limited by the specific loss function or whether the regularization term is convex. It shows that the optimal solution for a wide range of problems can be expressed through this kernel-based linear combination.

### 3.Kernel Methods

>This has led to the development of a series of learning methods based on kernel functions, collectively known as "kernel methods"

>The most common approach is "kernelization," which extends a linear learner into a non-linear one by introducing a kernel function.

### 4.Kernelized Linear Discriminant Analysis (KLDA)

#### 4.1 Concept

>KLDA is a non-linear extension of Linear Discriminant Analysis (LDA) achieved through kernelization.

#### 4.2 Process

* Assume samples are mapped to a feature space F via some mapping ϕ, and then perform LDA in that space.
* Based on the representer theorem, the projection function h(x) can be written as $h(x)=\sum^{m}_{i=1}\alpha_{i}K(x,x_{i})$
* The projection vector **w** can be expressed as $w=\sum^{m}_{i=1}\alpha_{i}\phi(x_{i})·w$
* By substituting this expression into the LDA objective function, the problem is transformed into finding the vector α, which can be solved as a generalized eigenvalue problem.
* Once α is found, the projection function h(x) for new samples can be computed.