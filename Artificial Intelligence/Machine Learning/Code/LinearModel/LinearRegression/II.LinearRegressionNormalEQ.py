import numpy as np

class LinearRegressionNormalEq:
    def __init__(self):
        self.weights = None

    def fit(self, X, y):
        X_argumented = np.c_[np.ones((X.shape[0],1)),X]

        try:
            XTX = X_argumented.T @ X_argumented
            XTX_inv = np.linalg.inv(XTX)
            XTy = X_argumented.T @ y
            self.weights = XTX_inv @ XTy
        except np.linalg.LinAlgError:
            raise RuntimeError("XTX is not invertible")
            self.weights = None

    def predict(self, X):
        if self.weights is None:
            raise RuntimeError("fit() is required")
        X_argumented = np.c_[np.ones((X.shape[0],1)),X]
        return X_argumented @ self.weights

X_train = np.array([
    [1, 1],
    [1, 2],
    [2, 2],
    [2, 3]
])

# y_train 根据真实关系 y = 2 + 3*x1 + 4*x2 生成
y_train = np.array([
    [9],   # 2 + 3*1 + 4*1
    [13],  # 2 + 3*1 + 4*2
    [16],  # 2 + 3*2 + 4*2
    [20]   # 2 + 3*2 + 4*3
])

model_ne = LinearRegressionNormalEq()
model_ne.fit(X_train, y_train)

print("(b,w1):", model_ne.weights.flatten())

X_new = np.array([
    [1,1],
    [2,2]
])
predictions = model_ne.predict(X_new)
print("predictions:", predictions.flatten())