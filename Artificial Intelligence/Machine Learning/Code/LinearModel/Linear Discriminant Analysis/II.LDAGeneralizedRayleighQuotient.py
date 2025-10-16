import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

class LDA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.linear_discriminants = None

    def fit(self, X, y):
        n_features = X.shape[1]
        class_labels = np.unique(y)

        mean_overall = np.mean(X, axis=0)

        S_W = np.zeros((n_features,n_features))
        S_B = np.zeros((n_features,n_features))

        for c in class_labels:
            X_c = X[y==c]
            mean_c = np.mean(X_c, axis=0)

            S_W += (X_c - mean_c).T @ (X_c - mean_c)

            n_c = X_c.shape[0]
            mean_diff = (mean_c - mean_overall).reshape(n_features,1)
            S_B += n_c * (mean_diff @ mean_diff.T)

        A = np.linalg.inv(S_W) @ S_B
        eigenvalues, eigenvectors = np.linalg.eig(A)

        eigenvectors = eigenvectors.T
        idxs = np.argsort((abs(eigenvalues))[::-1])
        eigenvalues = eigenvalues[idxs]
        eigenvectors = eigenvectors[idxs]

        self.linear_discriminants = eigenvectors[0:self.n_components].T

    def transform(self, X):
        return X @ self.linear_discriminants

# --- Example Usage with the Iris Dataset ---

# 1. Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 2. Instantiate and fit the LDA model
# We want to reduce from 4 features down to 2 for visualization
lda = LDA(n_components=2)
lda.fit(X, y)

# 3. Transform the data
X_projected = lda.transform(X)

print("Shape of original data:", X.shape)
print("Shape of transformed data:", X_projected.shape)

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
plt.legend(handles=scatter.legend_elements()[0], labels=list(iris.target_names))
plt.title("LDA of Iris Dataset")
plt.show()