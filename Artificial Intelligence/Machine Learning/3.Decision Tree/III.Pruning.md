### 1.Purpose

>Pruning is the main technique used by decision tree algorithms to combat "overfitting"

### 2.Basic Strategies

#### 2.1 Pre-pruning

>During tree generation, estimate whether a node's split will improve the tree's generalization performance. If not, stop the split and mark the current node as a leaf

**Pros**: Reduces the risk of overfitting and significantly cuts down on training and testing time. 

**Cons**: Has a risk of underfitting due to its "greedy" nature, as it might prevent splits that could lead to significant performance improvements later on

#### 2.2 Post-Pruning

>First, generate a complete decision tree. Then, from the bottom up, examine non-leaf nodes. If replacing the subtree corresponding to a node with a leaf node improves the tree's generalization performance, then perform the replacement.

**Pros**: Generally results in a decision tree with better generalization performance than pre-pruning because it has a lower risk of underfitting.

**Cons**: The training time overhead is much larger because it requires generating a full tree first.
