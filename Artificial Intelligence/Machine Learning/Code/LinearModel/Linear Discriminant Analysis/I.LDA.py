import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_iris

# 1. Load data
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# 2. Instantiate and fit the model
# We want to reduce from 4 features down to 2 for visualization
lda = LinearDiscriminantAnalysis(n_components=2)
lda.fit(X, y)

# 3. Transform the data
X_projected = lda.transform(X)

print("Shape of original data:", X.shape)
print("Shape of transformed data:", X_projected.shape)

# Access the learned projection matrix (eigenvectors)
print("\nLearned projection matrix (scalings_):\n", lda.scalings_)

# 4. Visualize the result
plt.figure(figsize=(8, 6))
scatter = plt.scatter(
    X_projected[:, 0],
    X_projected[:, 1],
    c=y,
    edgecolor="none",
    alpha=0.8,
    cmap=plt.get_cmap("viridis", 3),
)
plt.xlabel("Linear Discriminant 1")
plt.ylabel("Linear Discriminant 2")
handles, _ = scatter.legend_elements()
plt.legend(handles=handles, labels=list(target_names))
plt.title("LDA of Iris Dataset using Scikit-learn")
plt.show()