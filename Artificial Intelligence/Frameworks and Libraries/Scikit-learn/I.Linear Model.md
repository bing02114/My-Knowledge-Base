### 1.Linear Regression

#### 1.1 Function

``` python
model = LinearRegression(fit_intercept=True,copy_X=True,n_jobs=None)
```

#### 1.2 Parameters

- `fit_intercept=True`: (Default) This tells the model to calculate the intercept `b`. If set to `False`, it assumes the data is already centered and the line will pass through the origin.
    
- `copy_X=True`: (Default) This makes a copy of the input data `X` before fitting. Set to `False` to perform in-place operations, which might save memory but can alter your original data.
    
- `n_jobs=None`: (Default) The number of CPU cores to use for the computation. `None` usually means 1, while `-1` means using all available cores.

#### 1.3 Example

``` python
import numpy as np  
from sklearn.linear_model import LinearRegression  
  
# 1. 创建一些示例数据  
X = np.array([[1], [2], [3], [4], [5]]) # 特征 (例如，工作年限)  
y = np.array([3, 5, 7, 9, 11])        # 目标 (例如，薪水，单位：万)  
  
# 2. 实例化并拟合模型  
model = LinearRegression()  
model.fit(X, y)  
  
# 3. 查看学习到的参数  
print(f"系数 (w): {model.coef_}")  
print(f"截距 (b): {model.intercept_}")  
# 期望输出: 系数 (w): [2.], 截距 (b): 1.0# 这意味着模型学习到了关系 y = 2x + 1  
# 4. 对新数据点进行预测  
new_X = np.array([[6]])  
prediction = model.predict(new_X)  
print(f"对X=6的预测: {prediction}")  
# 期望输出: 对X=6的预测: [13.]  
  
# 5. 评估模型  
print(f"R-squared 分数: {model.score(X, y)}")  
# 期望输出: R-squared 分数: 1.0 (对于这个简单数据是完美拟合)
```
***
### 2.Logistic Regression

#### 2.1 Function

``` python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
```

#### 2.2 Key Hyperparameters

- **`penalty`**: A string (`'l1'`, `'l2'`, `'elasticnet'`, `'none'`) specifying the regularization to use. This is the most important parameter for controlling overfitting.
    
    - `'l2'` (Default): Ridge regularization. Penalizes large weights.
        
    - `'l1'`: Lasso regularization. Can force some weights to become zero, performing feature selection.
        
    - `'elasticnet'`: A combination of L1 and L2.
        
    - `'none'`: No regularization.
        
- **`C`**: A positive float (Default: 1.0). This is the **inverse of regularization strength**.
    
    - A **smaller `C`** specifies **stronger regularization**.
        
    - A **larger `C`** specifies **weaker regularization**.
        
- **`solver`**: A string specifying the algorithm to use for optimization. The choice of solver depends on the penalty and the dataset size.
    
    - `'lbfgs'` (Default): A good general-purpose solver for L2 or no penalty.
        
    - `'liblinear'`: Good for smaller datasets. It's one of the few that supports the L1 penalty.
        
    - `'saga'` and `'sag'`: Faster for large datasets. `'saga'` is versatile and supports all penalties.

#### 2.3 example

``` python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.metrics import classification_report

# 1. Create a sample dataset
X, y = make_classification(n_samples=200, n_features=10, n_informative=5, n_redundant=0, random_state=42)

# 2. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Instantiate and fit the model (with default L2 regularization)
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# 4. Make predictions
class_preds = model.predict(X_test)
proba_preds = model.predict_proba(X_test)

print("Example Class Prediction:", class_preds[0])
print("Example Probability Prediction [P(y=0), P(y=1)]:", proba_preds[0])

# 5. Evaluate the model
print("\nModel Accuracy:", model.score(X_test, y_test))
print("\nClassification Report:\n", classification_report(y_test, class_preds))
```

***
### 3.Linear Discriminant Analysis

#### 3.1 Function

``` python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Instantiate the model, specifying the number of components for dimensionality reduction
lda = LinearDiscriminantAnalysis(n_components=2)
```
#### 3.2 Key Hyperparameters

- **`n_components`**: An integer. This is the most important parameter for dimensionality reduction. It specifies the desired number of dimensions for the output (the `k` in our previous discussion). It cannot be larger than `min(n_features, n_classes - 1)`.
    
- **`solver`**: A string (`'svd'`, `'lsqr'`, `'eigen'`) specifying the algorithm to use.
    
    - `'svd'` (Default): Singular Value Decomposition. This is the recommended solver for most cases. It does not compute the covariance matrix directly and is more computationally stable, especially when the number of features is large.
        
    - `'eigen'`: Eigendecomposition. This solver directly computes the eigenvectors of SW−1​SB​, exactly matching the theory we discussed. It is less stable than SVD and requires the calculation of the inverse of SW​.
        
- **`shrinkage`**: Can be `None`, `'auto'`, or a float between 0 and 1. This is a form of regularization that can improve performance when the number of samples is small compared to the number of features.

#### 3.3 Example

``` python
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
```