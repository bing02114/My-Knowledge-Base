# 1. Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 2. Create some synthetic non-linear data
np.random.seed(42)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.random.randn(80) * 0.1 # A sine wave with some noise

# 3. Instantiate and train the model
# We set max_depth to prevent the tree from overfitting to the noise
model_reg = DecisionTreeRegressor(max_depth=6, random_state=42)
model_reg.fit(X, y)

# 4. Make predictions
# We create a dense set of points to see the model's prediction line
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_pred = model_reg.predict(X_test)

# 5. Evaluate the model's performance
y_train_pred = model_reg.predict(X)
mse = mean_squared_error(y, y_train_pred)
r2 = r2_score(y, y_train_pred)
print(f"Decision Tree Regressor Mean Squared Error: {mse:.4f}")
print(f"Decision Tree Regressor R-squared: {r2:.4f}\n")

# 6. Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, s=20, edgecolor="black", c="cornflowerblue", label="data")
plt.plot(X_test, y_pred, color="red", label=f"prediction (max_depth={model_reg.max_depth})", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()