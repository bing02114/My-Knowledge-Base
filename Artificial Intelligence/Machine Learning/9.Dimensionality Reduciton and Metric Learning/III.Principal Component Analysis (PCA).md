### 1.Concept

>PCA is one of the most commonly used dimensionality reduction methods. It can be derived from two equivalent perspectives: **"nearest reconstructibility"** and **"maximum separability."**

**Nearest Reconstructibility**: It seeks a hyperplane such that the sum of distances from all sample points to this hyperplane is minimized

**Maximum Separability**: It aims to find a hyperplane where the projections of all sample points are spread out as much as possible, maximizing the variance of the projected points.

### 2.Algorithm

>The solution involves performing an eigenvalue decomposition on the covariance matrix of the data. The transformation matrix **W** is formed by the _d'_ eigenvectors corresponding to the _d'_ largest eigenvalues

### 3.Effect

>PCA can increase sample density and, to some extent, serve as a denoising method by discarding components associated with smaller eigenvalues, which are often related to noise