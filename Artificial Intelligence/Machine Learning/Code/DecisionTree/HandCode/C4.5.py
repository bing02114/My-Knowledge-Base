import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature_index=None, threshold=None, children=None, leaf_value=None):
        self.feature_index = feature_index
        self.threshold = threshold
        self.children = children
        self.leaf_value = leaf_value

    def is_leaf_node(self):
        return self.leaf_value is not None

class C45DecisionTree:
    def __init__(self, min_samples_leaf=1, max_depth=100, is_categorical=None):
        self.min_samples_leaf = min_samples_leaf
        self.max_depth = max_depth
        self.root = None
        self.is_categorical = is_categorical

    def _entropy(self, y):
        hist = np.bincount(y)
        ps = hist / len(y)
        return -np.sum([p * np.log2(p) for p in ps if p>0])

    def _gain_ratio(self, y, children_y_list):
        parent_entropy = self._entropy(y)
        n_parent = len(y)
        if n_parent == 0:
            return 0
        weighted_child_entropy = sum((len(child_y) / n_parent) * self._entropy(child_y) for child_y in children_y_list)
        information_gain = parent_entropy - weighted_child_entropy
        split_info = -np.sum(
            [(len(child_y) / n_parent) * np.log2(len(child_y) / n_parent) for child_y in children_y_list if
             len(child_y) > 0])
        if split_info == 0:
            return 0
        return information_gain / split_info

    def _find_best_split(self, X, y):
        best_gain_ratio = -1
        best_split = {}
        n_features = X.shape[1]

        for feature_index in range(n_features):
            feature_values = X[:, feature_index]

            if not self.is_categorical[feature_index]:
                unique_values = np.unique(feature_values)
                if len(unique_values) > 1:
                    thresholds = (unique_values[:-1]+unique_values[1:]) /2
                    for threshold in thresholds:
                        left_indices = np.where(feature_values <= threshold)[0]
                        right_indices = np.where(feature_values > threshold)[0]
                        if len(left_indices) >0 and len(right_indices)>0:
                            gain_ratio = self._gain_ratio(y, y[left_indices],y[right_indices])
                            if gain_ratio > best_gain_ratio:
                                best_gain_ratio = gain_ratio
                                best_split = {
                                    'feature_index': feature_index,
                                    'threshold': threshold,
                                    'children_indices': [left_indices,right_indices]
                                }
            else:
                unique_values = np.unique(feature_values)
                if len(unique_values) > 1:  # Only split if there's more than one value
                    children_indices = [np.where(feature_values == val)[0] for val in unique_values]
                    gain_ratio = self._gain_ratio(y, [y[idx] for idx in children_indices])
                    if gain_ratio > best_gain_ratio:
                        best_gain_ratio = gain_ratio
                        best_split = {
                            'feature_index': feature_index,
                            'threshold': None,  # No threshold for categorical
                            'children_indices': children_indices
                        }

            return best_split

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))


        if (depth >= self.max_depth or
                n_labels == 1 or
                n_samples < self.min_samples_leaf * 2):  # *2 because a split needs two children
            leaf_value = Counter(y).most_common(1)[0][0]
            return Node(leaf_value=leaf_value)

            # Find the best split
        best_split = self._find_best_split(X, y)

        if not best_split:
            leaf_value = Counter(y).most_common(1)[0][0]
            return Node(leaf_value=leaf_value)

        # Recursive Step
        feature_index = best_split['feature_index']
        threshold = best_split['threshold']
        children_indices_list = best_split['children_indices']

        children = {}
        # For categorical features, the keys are the actual feature values
        if self.is_categorical[feature_index]:
            feature_values = np.unique(X[:, feature_index])
            for i, indices in enumerate(children_indices_list):
                X_child, y_child = X[indices], y[indices]
                children[feature_values[i]] = self._grow_tree(X_child, y_child, depth + 1)
        # For continuous features, the keys are 0 (left <=) and 1 (right >)
        else:
            X_left, y_left = X[children_indices_list[0]], y[children_indices_list[0]]
            children[0] = self._grow_tree(X_left, y_left, depth + 1)

            X_right, y_right = X[children_indices_list[1]], y[children_indices_list[1]]
            children[1] = self._grow_tree(X_right, y_right, depth + 1)

        return Node(feature_index=feature_index, threshold=threshold, children=children)


    def fit(self, X, y):
        if self.is_categorical is None:
            # By default, assume all are continuous if not specified
            self.is_categorical = [False] * X.shape[1]
        self.root = self._grow_tree(X, y)


    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.leaf_value

        feature_index = node.feature_index
        # Continuous feature
        if node.threshold is not None:
            if x[feature_index] <= node.threshold:
                return self._traverse_tree(x, node.children[0])  # Go left
            else:
                return self._traverse_tree(x, node.children[1])  # Go right
        # Categorical feature
        else:
            feature_value = x[feature_index]
            if feature_value in node.children:
                return self._traverse_tree(x, node.children[feature_value])
            else:
                # Handle unseen value during prediction (e.g., return majority of parent)
                # For simplicity, we just stop. A real implementation needs a better fallback.
                return None


    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])


# --- Example Usage with a Mixed Dataset ---

# Features: Outlook(categorical), Temperature(continuous), Humidity(continuous), Wind(categorical)
# Target: Play Tennis (No=0, Yes=1)
# Data encoding:
# Outlook: Sunny=0, Overcast=1, Rain=2
# Wind: Weak=0, Strong=1
X_train = np.array([
    [0, 85, 85, 0],  # Sunny, 85F, 85% Hum, Weak
    [0, 80, 90, 1],  # Sunny, 80F, 90% Hum, Strong
    [1, 83, 86, 0],  # Overcast, 83F, 86% Hum, Weak
    [2, 70, 96, 0],  # Rain, 70F, 96% Hum, Weak
    [2, 68, 80, 0],  # Rain, 68F, 80% Hum, Weak
    [2, 65, 70, 1],  # Rain, 65F, 70% Hum, Strong
    [1, 64, 65, 1],  # Overcast, 64F, 65% Hum, Strong
    [0, 72, 95, 0],  # Sunny, 72F, 95% Hum, Weak
    [0, 69, 70, 0],  # Sunny, 69F, 70% Hum, Weak
    [2, 75, 80, 0],  # Rain, 75F, 80% Hum, Weak
    [0, 75, 70, 1],  # Sunny, 75F, 70% Hum, Strong
    [1, 72, 90, 1],  # Overcast, 72F, 90% Hum, Strong
    [1, 81, 75, 0],  # Overcast, 81F, 75% Hum, Weak
    [2, 71, 91, 1],  # Rain, 71F, 91% Hum, Strong
])

y_train = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0])

# Specify which features are categorical
is_categorical_features = [True, False, False, True]

# Instantiate and train the C4.5 model
c45_tree = C45DecisionTree(max_depth=5, is_categorical=is_categorical_features)
c45_tree.fit(X_train, y_train)

# Make a prediction
# Outlook=Sunny(0), Temp=75F(continuous), Humidity=95%(continuous), Wind=Strong(1)
X_new = np.array([0, 75, 95, 1])
prediction = c45_tree.predict([X_new])
print(f"Prediction for {X_new}: {'Yes' if prediction[0] == 1 else 'No'}")