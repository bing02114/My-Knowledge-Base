import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature_index=None, children=None, leaf_value=None):
        self.feature_index = feature_index
        self.children = children
        self.leaf_value = leaf_value

    def is_leaf_node(self):
        return self.leaf_value is not None

class ID3DecisionTree:

    def __init__(self):
        self.root = None

    def _entropy(self, y):
        hist = np.bincount(y)
        ps = hist / len(y)
        return -np.sum([p * np.log2(p) for p in ps if p > 0])

    def _information_gain(self, X, y, feature_index):
        parent_entropy = self._entropy(y)
        feature_values = np.unique(X[:, feature_index])
        child_entropy_sum = 0
        for value in feature_values:
            child_indices = np.where(X[:, feature_index] == value)[0]
            if len(child_indices) == 0:
                continue
            weight = len(child_indices) / len(y)
            child_entropy = self._entropy(y[child_indices])
            child_entropy_sum += weight * child_entropy

        return parent_entropy - child_entropy_sum

    def _find_best_split(self, X, y, feature_indices):
        best_gain = -1
        best_feature_index = -1
        for feature_index in feature_indices:
            gain = self._information_gain(X, y, feature_index)
            if gain > best_gain:
                best_gain = gain
                best_feature_index = feature_index
        return best_feature_index

    def _grow_tree(self, X, y, feature_indices):
        if len(np.unique(y)) == 1:
            return Node(leaf_value=y[0])
        if len(feature_indices) == 0:
            majority_class = Counter(y).most_common(1)[0][0]
            return Node(leaf_value=majority_class)

        best_feature_index = self._find_best_split(X, y, feature_indices)

        if best_feature_index == -1 or self._information_gain(X, y, best_feature_index) == 0:
            majority_class = Counter(y).most_common(1)[0][0]
            return Node(leaf_value=majority_class)

        children = {}
        remaining_feature_indices = [i for i in feature_indices if i != best_feature_index]

        for value in np.unique(X[:, best_feature_index]):
            X_subset = X[X[:, best_feature_index] == value]
            y_subset = y[X[:, best_feature_index] == value]
            children[value] = self._grow_tree(X_subset, y_subset, remaining_feature_indices)

        return Node(feature_index=best_feature_index, children=children)

    def fit(self, X, y):
        self.root = self._grow_tree(X, y, feature_indices=list(range(X.shape[1])))

    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.leaf_value

        feature_value = x[node.feature_index]

        if feature_value not in node.children:
            return None

        return self._traverse_tree(x, node.children[feature_value])

    def predict(self, X):
        return [self._traverse_tree(x, self.root) for x in X]

X_train = np.array([
    [0, 0, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [2, 1, 0, 0],
    [2, 2, 1, 0], [2, 2, 1, 1], [1, 2, 1, 1], [0, 1, 0, 0],
    [0, 2, 1, 0], [2, 1, 1, 0], [0, 1, 1, 1], [1, 1, 0, 1],
    [1, 0, 1, 0], [2, 1, 0, 1]
])

y_train = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]) # 不打, 不打, 打, 打...

# 实例化并训练 ID3 模型
id3_tree = ID3DecisionTree()
id3_tree.fit(X_train, y_train)

# 进行预测
# 预测新的一天: 天气=晴(0), 温度=冷(2), 湿度=高(0), 风力=强(1)
X_new = np.array([0, 2, 0, 1])
prediction = id3_tree.predict([X_new])
print(f"对 {X_new} 的预测: {'打' if prediction[0] == 1 else '不打'}")
# 期望结果是不打 (0)