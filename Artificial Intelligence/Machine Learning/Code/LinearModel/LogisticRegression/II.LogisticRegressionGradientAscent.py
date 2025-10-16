import numpy as np
import matplotlib.pyplot as plt

class LogisticRegression:
    def __init__(self, learning_rate = 0.01, n_iterations = 1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.loss_history = []

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        X_augmented = np.c_[np.ones((X.shape[0],1)),X]
        m_samples, n_features = X_augmented.shape

        self.weights = np.random.randn(n_features,1)

        for i in range(self.n_iterations):

            logits = X_augmented @ self.weights
            y_hat = self._sigmoid(logits)

            gradients = (1/m_samples) * X_augmented.T @ (y-y_hat)
            self.weights = self.weights + self.learning_rate * gradients

            cost = -(1/m_samples) * np.sum( y * np.log(y_hat) + (1-y)*np.log(1-y_hat))
            self.loss_history.append(cost)

    def predict_proba(self, X):
        if self.weights is None:
            raise RuntimeError("Model has not been trained. Please call fit() first.")
        X_augmented = np.c_[np.ones((X.shape[0],1)),X]
        logits = X_augmented @ self.weights
        return self._sigmoid(logits)

    def predict(self, X, threshold=0.5):
        probabilities = self.predict_proba(X)
        return (probabilities >= threshold).astype(int).flatten()

# --- Example Usage ---

# 1. Create a simple, linearly separable dataset
np.random.seed(42)
m_samples = 100
X = np.random.rand(m_samples, 2) * 5
# Create a linear boundary: y = 1 if 2*x1 - 3*x2 + 1 > 0
y = (2 * X[:, 0] - 3 * X[:, 1] + 1 > 0).astype(int).reshape(-1, 1)

# 2. Instantiate and train the model
model = LogisticRegression(learning_rate=0.1, n_iterations=3000)
model.fit(X, y)

# 3. Print the learned weights
# The first weight is the bias (intercept), the next are for the features
print("Learned weights (b, w1, w2):", model.weights.flatten())

# 4. Make predictions on new data
X_new = np.array([
    [4, 1],  # Should be class 1 (2*4 - 3*1 + 1 = 6 > 0)
    [1, 3]   # Should be class 0 (2*1 - 3*3 + 1 = -6 < 0)
])
predictions = model.predict(X_new)
probabilities = model.predict_proba(X_new)

print("\nPredictions for new data:", predictions)
print("Probabilities for new data (P(y=1)):", probabilities.flatten())

# 5. (Optional) Plot the loss history to see convergence
plt.plot(model.loss_history)
plt.title("Loss (Cross-Entropy) during Training")
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.show()