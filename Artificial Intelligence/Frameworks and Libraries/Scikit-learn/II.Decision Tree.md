
>Scikit-learn's decision tree module **implements an optimised version of the CART algorithm**, and it **does not** provide separate, distinct implementations of ID3 or C4.5.

### 1.Classifier

``` python
from sklearn.tree import DecisionTreeClassifier

# This uses the CART algorithm with its standard Gini Impurity criterion
cart_model = DecisionTreeClassifier(criterion='gini', random_state=42)

# This uses a CART-like structure (binary tree) but with an
# ID3/C4.5-like splitting criterion (Information Gain)
id3_like_model = DecisionTreeClassifier(criterion='entropy', random_state=42)
```

#### 2. Key Hyperparameters

### **Hyperparameters for Tree Structure and Splitting**

These parameters control how the tree decides on the best split at each node.
#### 1. **`criterion`**

- **Default**: `'gini'`
    
- **Options**: `'gini'`, `'entropy'`
    
- **What it does**: This is the function used to measure the quality of a split. The algorithm chooses the feature and threshold that yields the best split according to this criterion.
    
    - **`'gini'`**: Uses the **Gini Impurity**. It measures the probability of a randomly chosen sample from the node being incorrectly classified. It is computationally faster.
        
    - **`'entropy'`**: Uses **Information Gain**, which is based on the concept of entropy. It measures the reduction in uncertainty after a split. It tends to produce slightly more balanced trees.
        
- **Tuning Advice**: The difference in performance between the two is often small. `'gini'` is a great default. You can include `'entropy'` in your hyperparameter search to see if it provides a slight edge.
    

#### **2. `splitter`**

- **Default**: `'best'`
    
- **Options**: `'best'`, `'random'`
    
- **What it does**: This defines the strategy used to choose the split at each node.
    
    - **`'best'`**: The algorithm evaluates all possible splits for all features and chooses the one that is best according to the `criterion`.
        
    - **`'random'`**: The algorithm evaluates a random subset of possible splits and chooses the best one among them. This can speed up training and sometimes help prevent overfitting.
        
- **Tuning Advice**: `'best'` is the standard for a single decision tree. `'random'` is more relevant for ensembles like Random Forests where introducing randomness is key.
    

---

### **Hyperparameters for Controlling Tree Growth (Pre-Pruning)**

These are the most important parameters for preventing overfitting. They stop the tree from growing too deep and complex.

#### **3. `max_depth`**

- **Default**: `None`
    
- **Options**: An integer or `None`.
    
- **What it does**: This sets the maximum depth of the tree.
    
    - If `None`, the tree will expand until all leaves are pure or until they contain fewer samples than `min_samples_split`. This is very likely to overfit.
        
- **Tuning Advice**: This is one of the **most important hyperparameters to tune**. A smaller `max_depth` creates a simpler model that generalizes better. Use cross-validation to find an optimal value, often in the range of 3 to 15.
    

#### **4. `min_samples_split`**

- **Default**: `2`
    
- **Options**: An integer or a float (fraction).
    
- **What it does**: This is the minimum number of samples a node must have before it can be considered for splitting.
    
    - An `int` value is the absolute number of samples.
        
    - A `float` value is a fraction of the total samples (`ceil(min_samples_split * n_samples)`).
        
- **Tuning Advice**: Increasing this value makes the model more conservative, as it will stop splitting on nodes with fewer samples. This helps prevent the model from learning from noise in small groups of data. This is another key parameter to tune.
    

#### **5. `min_samples_leaf`**

- **Default**: `1`
    
- **Options**: An integer or a float (fraction).
    
- **What it does**: This is the minimum number of samples that are required to be at a leaf node. A split will only be considered if it leaves at least `min_samples_leaf` training samples in each of the left and right branches.
    
- **Tuning Advice**: Similar to `min_samples_split`, this parameter is crucial for controlling overfitting. Increasing this value ensures that every final decision is based on a reasonably sized group of samples. Sometimes, tuning this parameter is more intuitive than tuning `min_samples_split`.
    

#### **6. `max_leaf_nodes`**

- **Default**: `None`
    
- **Options**: An integer or `None`.
    
- **What it does**: Limits the total number of leaf nodes in the tree. The tree is grown in a "best-first" manner, where the nodes that provide the largest impurity decrease are expanded first.
    
- **Tuning Advice**: This provides another direct way to control the complexity of the model. It can be used as an alternative to `max_depth`.
    

---

### **Other Important Hyperparameters**

#### **7. `class_weight`**

- **Default**: `None`
    
- **Options**: `None`, `'balanced'`, or a dictionary.
    
- **What it does**: Sets weights for different classes. This is extremely useful for **imbalanced datasets**.
    
    - `None`: All classes have a weight of 1.
        
    - `'balanced'`: Automatically adjusts weights to be inversely proportional to class frequencies in the input data.
        
    - `dict`: Manually specify the weight for each class (e.g., `{0: 1, 1: 5}`).
        
- **Tuning Advice**: If your classes are imbalanced, set this to `'balanced'` as a first step.
    

#### **8. `random_state`**

- **Default**: `None`
    
- **Options**: An integer or `None`.
    
- **What it does**: Controls the randomness of the estimator. If `splitter='random'` or `max_features` is used, the results can vary on each run.
    
- **Tuning Advice**: **Always set this to a fixed integer during development and experimentation.** This ensures that your results are reproducible.


#### 3. Example

``` python
# 1. Import necessary libraries  
from sklearn.datasets import load_iris  
from sklearn.model_selection import train_test_split  
from sklearn.tree import DecisionTreeClassifier  
from sklearn.metrics import accuracy_score, classification_report  
  
# 2. Load the data  
# The Iris dataset has 3 classes (species of iris) and 4 features.  
iris = load_iris()  
X, y = iris.data, iris.target  
  
# 3. Split the data into training and testing sets  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  
  
# 4. Instantiate and train the model  
# We set random_state for reproducibility  
model_clf = DecisionTreeClassifier(max_depth=3, random_state=42)  
model_clf.fit(X_train, y_train)  
  
# 5. Make predictions on the test set  
y_pred = model_clf.predict(X_test)  
  
# 6. Evaluate the model's performance  
accuracy = accuracy_score(y_test, y_pred)  
print(f"Decision Tree Classifier Accuracy: {accuracy:.4f}\n")  
print("Classification Report:")  
print(classification_report(y_test, y_pred, target_names=iris.target_names))
```

***

### 2.Regression

#### 2.1 Function

``` python
from sklearn.tree import DecisionTreeClassifier

# This uses the CART algorithm with its standard Gini Impurity criterion
cart_model = DecisionTree(criterion='gini', random_state=42)
```

#### 2.2 Key Hyperparameters

**Criterion**

- **`'squared_error'` (Default)**: Uses Mean Squared Error (MSE). It chooses the split that minimizes the squared error within the child nodes. This is equivalent to minimizing variance.
    
- **`'friedman_mse'`**: A variation of MSE with an improvement for potential splits.
    
- **`'absolute_error'`**: Uses Mean Absolute Error (MAE). This is less sensitive to outliers than MSE.
    
- **`'poisson'`**: For modeling count data.

#### 2.3 Example

``` python
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
```