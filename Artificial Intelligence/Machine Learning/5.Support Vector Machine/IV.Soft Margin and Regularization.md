### 1.Soft Margin

>To handle noise and outliers in real-world tasks, "soft margin" is introduced, which allows some samples to not satisfy the constraints. This is achieved by introducing "slack variables"

### 2.Surrogate Loss

>The 0/1 loss function is non-convex and non-continuous, making the optimization problem difficult to solve. Therefore, other functions are often used as "surrogate losses," such as hinge loss, exponential loss, and logistic loss

### 3.Regularization

>The optimization objective can be viewed more generally as a combination of a **"structural risk"** (regularization term) Ω(f) and an **"empirical risk"** (loss term) ∑ℓ(f(xi​),yi​). The regularization term expresses our preference for models with certain properties (e.g., lower complexity), which helps reduce the risk of overfitting.

**Goal**

$$\min_{f}\Omega(f)+C\sum^{m}_{i=1}l(f(x_{i}),y_{i})$$

>C` defines the **tolerance** of the model for errors on the training data.

- **Low `C`**: The gatekeeper is very **lenient**. It's okay if some points from the wrong class sneak into the club or across the margin. The priority is to keep the club's entrance (the margin) as wide as possible, even if it means some non-members get in. This creates a **soft margin** and can lead to **underfitting**.
    
- **High `C`**: The gatekeeper is extremely **strict**. It will heavily penalize any point that is on the wrong side of the margin. The priority is to classify every training point correctly, even if it means making the entrance (the margin) very narrow. This creates a **hard margin** and can lead to **overfitting**.

### 4.Difference compared to Hard-Margin SVM

#### 4.1 C

>C defines the tolerance of the model for errors on the training data

#### 4.2 The SMO algorithm

>The difference between these two kinds of SVM is in the clip operation
>
>Hard: 0<=a
>
>Soft: 0<=a<=C

