import numpy as np
from collections import Counter


# --- Helper Functions ---

def find_majority(y):
    if len(y) == 0:
        return None
    # 将 NumPy 整数转换为标准的 Python int
    return int(Counter(y).most_common(1)[0][0])


def predict_single(tree, x):
    """Predict the class for a single data point using the dictionary-based tree."""
    # If it's a leaf node, return the prediction
    if 'leaf_value' in tree:
        return tree['leaf_value']

    feature_index = tree['feature_index']
    feature_value = x[feature_index]

    # If the feature value from the sample exists as a branch
    if feature_value in tree['children']:
        child_node = tree['children'][feature_value]
        return predict_single(child_node, x)
    else:
        # Fallback for unseen values: return the majority class of the current node
        # A more robust implementation would store this, but we'll use a placeholder
        return tree.get('majority_class', None)


def calculate_accuracy(tree, X, y):
    """Calculate the accuracy of a tree on a given dataset."""
    if len(y) == 0:
        return 1.0  # Or 0.0, depends on convention. 1.0 means no errors.

    predictions = [predict_single(tree, x) for x in X]
    correct = np.sum(predictions == y)
    return correct / len(y)


# --- The Main Post-Pruning Function ---

def post_prune(node, X_train, y_train, X_val, y_val):
    """
    Recursively prunes a decision tree using Reduced Error Pruning.
    This function modifies the tree in-place.
    """
    # Base case: if the node is a leaf, do nothing and return it.
    if 'leaf_value' in node:
        return node

    feature_index = node['feature_index']

    # --- 1. Recursively prune the children first (Post-order traversal) ---
    for value, child_node in node['children'].items():
        # Filter the datasets for the child
        train_mask = X_train[:, feature_index] == value
        val_mask = X_val[:, feature_index] == value

        # Recurse
        post_prune(child_node, X_train[train_mask], y_train[train_mask],
                   X_val[val_mask], y_val[val_mask])

    # --- 2. Decide whether to prune the current node ---

    # Accuracy of the unpruned subtree on the validation set
    accuracy_unpruned = calculate_accuracy(node, X_val, y_val)

    # What would the prediction be if we turned this node into a leaf?
    # The leaf's value should be the majority class of the TRAINING data at this node.
    majority_class_at_node = find_majority(y_train)
    node['majority_class'] = majority_class_at_node  # Store for fallback prediction

    # Accuracy if we prune (replace the subtree with a single leaf)
    accuracy_pruned = np.mean(y_val == majority_class_at_node) if len(y_val) > 0 else 0

    print(f"Considering node splitting on feature {feature_index}...")
    print(f"  Accuracy with subtree: {accuracy_unpruned:.4f}")
    print(f"  Accuracy if pruned to leaf (predicting '{majority_class_at_node}'): {accuracy_pruned:.4f}")

    # If pruning is better or equal, turn this node into a leaf
    if accuracy_pruned >= accuracy_unpruned:
        print(f"  DECISION: Pruning node. Replacing with leaf value '{majority_class_at_node}'.\n")
        # Modify the node to become a leaf
        node.clear()  # Remove feature_index, children, etc.
        node['leaf_value'] = majority_class_at_node
    else:
        print("  DECISION: Keeping subtree.\n")

    return node


# --- Main Execution ---

# 1. Data Preparation
# Features: Outlook(0), Temperature(1), Humidity(2), Wind(3)
# Target: Play Tennis (No=0, Yes=1)
# Outlook: Sunny=0, Overcast=1, Rain=2
# Wind: Weak=0, Strong=1
X = np.array([
    [0, 0, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [2, 1, 0, 0],
    [2, 2, 1, 0], [2, 2, 1, 1], [1, 2, 1, 1], [0, 1, 0, 0],
    [0, 2, 1, 0], [2, 1, 1, 0], [0, 1, 1, 1], [1, 1, 0, 1],
    [1, 0, 1, 0], [2, 1, 0, 1]
])
y = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0])

# Split into a training set and a validation set
X_train, y_train = X[:10], y[:10]
X_val, y_val = X[10:], y[10:]

# 2. Define the initial, fully grown (overfit) tree as a dictionary
# This tree is manually constructed to be fully grown on the training data.
# Feature indices: 0=Outlook, 2=Humidity, 3=Wind
initial_tree = {
    'feature_index': 0,  # Root node splits on Outlook
    'children': {
        0: {  # Case: Outlook = Sunny (0)
            'feature_index': 2,  # Split on Humidity
            'children': {
                0: {'leaf_value': 0},  # Humidity = High (0) -> No
                1: {'leaf_value': 1}  # Humidity = Normal (1) -> Yes
            }
        },
        1: {'leaf_value': 1},  # Case: Outlook = Overcast (1) -> Yes (Pure node)
        2: {  # Case: Outlook = Rain (2)
            'feature_index': 3,  # Split on Wind
            'children': {
                0: {'leaf_value': 1},  # Wind = Weak (0) -> Yes
                1: {'leaf_value': 0}  # Wind = Strong (1) -> No
            }
        }
    }
}

# 3. Evaluate Before Pruning
print("--- Initial Overfit Tree ---")

import json

print(json.dumps(initial_tree, indent=2))
initial_accuracy = calculate_accuracy(initial_tree, X_val, y_val)
print(f"\nAccuracy on validation set BEFORE pruning: {initial_accuracy:.4f}\n")

# 4. Perform Post-Pruning
print("--- Starting Post-Pruning Process ---\n")
# We need to pass the full datasets to the root call
pruned_tree = post_prune(initial_tree, X_train, y_train, X_val, y_val)

# 5. Evaluate After Pruning
print("\n--- Final Pruned Tree ---")
print(json.dumps(pruned_tree, indent=2))
final_accuracy = calculate_accuracy(pruned_tree, X_val, y_val)
print(f"\nAccuracy on validation set AFTER pruning: {final_accuracy:.4f}")