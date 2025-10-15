import numpy as np

class LinearRegressionGradientDescent:

    def __init__(self, learning_rate = 0.01, n_iterations = 1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.loss_history = []

    def fit(self, X, y):
        X_argumented = np.c_[np.ones((X.shape[0],1)),X]
        m, n_features = X_argumented.shape
        self.weights = np.random.randn(n_features, 1)

        for i in range(self.n_iterations):
            predictions = X_argumented @ self.weights
            errors = predictions - y
            gradients = (2/m) * X_argumented.T @ errors
            self.weights = self.weights - self.learning_rate * gradients
            loss = np.mean(errors**2)
            self.loss_history.append(loss)

    def predict(self, X):
        if self.weights is None:
            raise RuntimeError("fit() is required")

        X_argumented = np.c_[np.ones((X.shape[0],1)),X]
        return X_argumented @ self.weights

X_train = np.array([1,2,3,4]).reshape(-1,1)
y_train = np.array([1,2,3,4]).reshape(-1,1)

# 实例化并训练模型
model_gd = LinearRegressionGradientDescent(learning_rate=0.1, n_iterations=1000)
model_gd.fit(X_train, y_train)

# 查看学习到的权重
print("梯度下降法学到的权重 (b, w1):", model_gd.weights.flatten())

# 进行预测
X_new = np.array([[1], [2]]).reshape(-1,1)
predictions = model_gd.predict(X_new)
print("对新数据 [1] 和 [2] 的预测:", predictions.flatten())