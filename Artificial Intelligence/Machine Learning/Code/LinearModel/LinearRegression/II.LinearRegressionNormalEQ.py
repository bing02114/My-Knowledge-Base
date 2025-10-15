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
            print("X.T @ X is singular matrix, which is invertible.")
            self.weights = None

    def predict(self, X):
        if self.weights is None:
            raise RuntimeError("fit() is required")
        X_argumented = np.c_[np.ones((X.shape[0],1)),X]
        return X_argumented @ self.weights

X_train = np.array([[1],[2],[3],[4],[5],[6]])
y_train = np.array([2,4,6,8,10,12])

model_ne = LinearRegressionNormalEq()
model_ne.fit(X_train, y_train)

print("(b,w1):", model_ne.weights.flatten())

X_new = np.array(([0],[2]))
predictions = model_ne.predict(X_new)
print("predictions:", predictions.flatten())
