### 1.Core Idea

>Also known as "Fisher discriminant analysis," LDA **projects samples onto a line** such that same-class samples' projection points are as close as possible, while different-class samples' projection points are as far as possible

### 2.Key Concepts

**Within-class Scatter Matrix (Sw​)**: Aims to be minimized to make same-class projections closer. 

>Sw is a "scaled" covariance matrix.
>
>$$Cov_{c}=\frac{1}{N_{c}-1}\sum_{i\in c}(x_{i}-\mu_{c})(x_{i}-\mu_{c})^{T}$$
>
>SW​ describes the **average spread of data points _within_ their own class**.
>
>**Geometric Meaning:**
>
>Imagine each class of data points as a "cloud" or an ellipsoid in high-dimensional space. The covariance matrix for a single class describes the shape, size, and orientation of that cloud. SW​ is the sum of these individual class covariance matrices. Therefore, **SW​ represents the average shape and size of the data clouds for all classes**
>
>**Covariance**:
>
>Covariance is a measure of the **joint variability of two random variables**. It tells you how two variables change together.
>
>- The **diagonal elements** are the **variances** of each individual feature.
 >   
>- The **off-diagonal elements** are the **covariances** between pairs of features.
   > 
>- **Geometric Meaning**: The covariance matrix describes the **shape, size, and orientation of the data cloud** (ellipsoid). Its eigenvectors point in the directions of the principal axes of the cloud, and its eigenvalues measure the variance (spread) along those axes.



$$S_{W}=\sum^{C}_{c=1}S_c$$

$$S_{c}=\sum_{i\in class~c}(x_{i}-\mu_{c})(x_{i}-\mu_{c})^{T}$$


**Between-class Scatter Matrix (Sb​)**: Aims to be maximized to make different-class projections farther apart. 

>SB​ describes the **spread of the _class centers (means)_ around the overall mean of all data.**

$$S_{B}=\sum^{C}_{c=1}N_{c}(\mu_{c}-\mu)(\mu_c-\mu)^{T}$$

### 3.Objective Function

>The goal is to maximize the generalized Rayleigh quotient


$$J=\frac{w^{T}S_{b}w}{w^{T}S_{w}w}$$

>**w: a projection matrix**

- **Geometric Meaning**: The vector `w` defines a **direction** (a line or axis) in the high-dimensional space. The mathematical operation of projecting a data point `x` onto this line is done via the **dot product**.
    
- **The Math**: The projection of a vector `x` onto the direction defined by a unit vector `w` is given by the scalar value `x · w`. This scalar value is the new, single coordinate of the data point in the lower-dimensional space.

>$w^{T}Aw$
>
>It measures the variance (or "stretch") of the matrix A  in the direction of the vector w


* The quadratic form **wTSB​w represents the variance of the class means _after they have been projected_ onto the line defined by `w`**

* ***wTSW​w represents the sum of the variances _within_ each class _after projection_**.



**The Derivation: Finding the Maximum**

$$\nabla_{w}J(w)=\frac{(\nabla_{w}f(w))·g(w)-f(w)·(\nabla_{w}g(w))}{[g(w)]^2}$$

$$\nabla_{w}J(w)=\frac{(2S_{B}w)(w^{T}S_{W}w)-(w^{T}S_{B}w)(2S_{W}w)}{(w^{T}S_{W}w)^2}$$

**Set the Gradient to Zero**

$$(S_{B}w)(w^{T}S_{W}w)=(S_{W}w)(w^{T}S_{B}w)$$

$$S_{B}w=\frac{w^{T}S_{B}w}{w^{T}S_{W}w}(S_{W}w)$$

**Recognizing the Eigenvalue**

$$S_{B}w=\lambda S_{W}w$$

where $$\lambda=\frac{w^{T}S_{B}w}{w^{T}S_{W}w}$$

**The Generalized Eigenvalue Problem**

$$(S_{W}^{-1}S_{B})w=\lambda w$$

>The optimal projection vector `w` are the eigenvectors of the matrix $S_{W}^{-1}S_{B}$
>
>The value of the objective function, $J(w)$ for any given eigenvector solution `w` is its corresponding eigenvalue $\lambda$
>
>Therefore, to maximize J(w), we mush choose the eigenvector w that corresponds to the largest eigenvalue $\lambda$


**Conclusion**: The closed-form solution for the best 1-dimensional projection vector `w` in LDA is the **principal eigenvector** (the eigenvector associated with the largest eigenvalue) of the matrix SW−1​SB​. If you want to project to `k` dimensions, you choose the top `k` eigenvectors.


### 4. Multi-class Extension

>LDA can be extended to multi-class tasks, where it **projects** samples into an _N_-1 dimensional space, serving as a **classic supervised dimensionality reduction technique.**

