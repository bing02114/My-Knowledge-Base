### 1.Definition

>A decision tree is a common machine learning method that makes decisions based on a tree structure. It contains a root node, several internal nodes, and several leaf nodes

* **Leaf node**: represent the decision results (class labels).
* **Non-leaf nodes**: (root and internal nodes) represent an attribute test

### 2.Learning Goal

>To produce a decision tree with strong generalization ability, meaning it performs well on unseen examples.

### 3.Algorithm Strategy

>The basic algorithm follows a "divide-and-conquer" strategy, generating a tree through a recursive process

### 4.Termination Conditions: 

>The recursion stops under three conditions

1. All samples in the current node belong to the same class
2. The current attribute set is empty, or all samples have the same value on all attributes
3. The current node contains an empty set of samples
