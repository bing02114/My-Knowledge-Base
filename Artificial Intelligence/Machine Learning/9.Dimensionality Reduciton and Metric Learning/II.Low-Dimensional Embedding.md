### 1.Curse of Dimensionality

>In high-dimensional spaces, **data samples become sparse**, and distance calculations become difficult. This phenomenon is a severe obstacle for many machine learning methods and is known as the "curse of dimensionality."

### 2.Dimensionality Reduction

>An important way to mitigate the curse of dimensionality is through dimensionality reduction. It transforms the original high-dimensional attribute space into a low-dimensional "subspace." The density of samples increases significantly in this subspace, making learning easier.

### 3.Low-Dimensional Embedding

>The rationale for dimensionality reduction is that although the collected data may be high-dimensional, the data relevant to the learning task might actually reside in a low-dimensional embedding within the high-dimensional space

### 4.Multi-Dimensional Scaling (MDS)

>A classic dimensionality reduction technique that aims to preserve the distances between samples from the original space in the new low-dimensional space.

**Process**: It takes a distance matrix of the original samples as input. It then calculates an inner product matrix **B** and performs an eigenvalue decomposition on **B**. The final low-dimensional representation is obtained by selecting the top _d'_ eigenvectors corresponding to the largest eigenvalues