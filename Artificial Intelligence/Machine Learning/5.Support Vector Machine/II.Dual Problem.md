### 1.Why SVMs Use Duality

- **To Enable the Kernel Trick**: The dual problem's structure depends on the data only through **dot products** (xiT​xj​). This allows us to replace the dot product with a **kernel function** K(xi​,xj​), which implicitly maps the data into a higher-dimensional space. This is the key to finding complex, **non-linear** decision boundaries without the computational cost of working in a high-dimensional space. This is impossible in the primal form.
    
- **To Reveal Sparsity (Support Vectors)**: The solution to the dual problem is **sparse**. This means most of the dual variables (αi​) will be zero. The few data points with non-zero αi​ are the **Support Vectors**—the critical points that define the margin. This makes the model memory-efficient and provides insight into which data points are most important.
    
- **Computational Efficiency**: The primal problem's complexity depends on the number of features (`n`), while the dual's depends on the number of samples (`m`). For datasets with a huge number of features but relatively few samples (`n >> m`), solving the dual problem is much faster.

### 2.What is Duality

In optimization, duality is the principle that an optimization problem (the **primal problem**) can be viewed from an alternative perspective (the **dual problem**).

- **Primal Problem**: Typically a minimization problem, like finding the lowest point in a valley. e.g., minf(x) subject to constraints.
    
- **Dual Problem**: A related maximization problem derived from the primal, like finding the highest possible "floor" that can be placed underneath the entire valley. e.g., maxg(λ) subject to different constraints.
    

For convex problems like SVM, **strong duality** holds, which means the optimal value of the primal and dual problems are equal. Solving the dual is equivalent to solving the primal.


### 3.Introduction to Lagrange Multipliers

The method of Lagrange Multipliers is a technique for transforming a **constrained** optimization problem into an **unconstrained** form that is easier to work with. It does this by creating a new function called the **Lagrangian**.

**For Equality Constraint:**

* **Problem**: Minimize f(x) subject to h(x)=0
* **Lagrangian**: We introduce a multiplier $\lambda$ and form $L(x,\lambda)=f(x)-\lambda h(x)$
* **Solution**: The solution is found at the point where gradient of the Lagrangian is zero: $\Delta L(x,\lambda)=0$

**For Inequality Constraint**

* **Problem**: Minimize f(x) subject to $g(x)\leq 0$
* **Lagrangian**: We introduce a multiplier $\alpha \geq 0$ and form $L(x,a)=f(x)+\alpha g(x)$
* **Solution**: The solution must satisfy the **Karush-Kuhn-Tucker (KKT) conditions**, one of which is the **complementary slackness** condition: $\alpha ·g(x)=0$. This condition implies that either the multiplier α is zero, or the constraint g(x) is "active". For SVM, this means that for any data point that is not on the margin, its corresponding α must be zero.

### 4.Applying Lagrange Multipliers to the SVM Primal Problem

**Primal Problem**

* Minimize $\frac{1}{2}||w||^{2}$
* Subject to $y_{i}(w^{T}x_{i}+b)\geq 1$

**Rewrite Constraint**

* Rewrite the constraint as $1-y_{i}(w^{T}x_{i}+b)\leq 0$
* This matches the standard $g(x)\leq 0$ form

**Form the Lagrangian**

$$L(w,b,a)=\frac{1}{2}||w||^{2}+\sum^{m}_{i=1}\alpha_{i}[1-y_{i}(w^{T}x_{i}+b)]$$

**The Goal**

$$\min_{w,b}\{\max_{\alpha}L(w,b,\alpha)\}$$

	The Dual Problem:

$$\max_{\alpha}\{\min_{w,b}L(w,b,\alpha)\}$$


**Minimize w.r.t Primal Variables**

* $\nabla_{w}L=w-\sum \alpha_{i}y_{i}x_{i}=0 \rightarrow w=\sum^{m}_{i=1}\alpha_{i}y_{i}x_{i}$
* $\nabla_{b}L=-\sum a_{i}y_{i} \rightarrow \sum^{m}_{i=1}\alpha_{i}y_{i}=0$

**Substitude Back**

### 5.The Result of the Transformation (The Dual Problem)

**Objective**: Maximize with respect to $\alpha$

$$\max_{\alpha}L(\alpha)=\sum^{m}_{i=1}\alpha_{i}-\frac{1}{2}\sum^{m}_{i=1}\sum^{m}_{j=1}\alpha_{i}\alpha{j}y_{i}y_{j}(x_{i}^{T}x_{j})$$

**Subject to the constraint**

* $a_{i}\geq 0$
* $\sum^{m}_{i=1}\alpha_{i}y_{i}=0$

$$f(x)=\sum^{m}_{i=1}\alpha_{i}y_{i}x^{T}_{i}x+b$$

### 6.Solving with SMO

**Core Idea**: Instead of optimizing all `m` variables (αi​) at once, SMO breaks the problem down into the smallest possible sub-problems.

**The "Minimal" Step**: At each iteration, SMO selects **two** Lagrange multipliers (αi​ and αj​) to optimize jointly, while keeping all other multipliers fixed.

**Why Two?**: Due to the constraint ∑αi​yi​=0. If you only tried to optimize one αi​, this constraint would immediately fix its value, leaving no room for optimization. By choosing two, the constraint becomes αi​yi​+αj​yj​=constant, which defines a line. The sub-problem is then to find the optimum on this line segment (also bounded by box constraints for soft-margin SVMs).

**The process**

**1. Initialize all αi​ to 0.**

**2. Repeat until convergence**

a. Select a pair of multipliers (αi​,αj​) to optimize, typically using a heuristic to pick the ones that most violate the KKT conditions. 

b. Analytically solve the tiny 2-variable sub-problem to find the updated values for αi​ and αj​. c. Update the model's threshold `b`.

c. The algorithm stops when all multipliers satisfy the KKT conditions within a small tolerance.

**How to solve b**

$$b=\frac{1}{|S|}\sum_{s\in S}(y_{s}-\sum_{i\in S}\alpha_{i}y_{i}x_{i}^{T}x_{s})$$
