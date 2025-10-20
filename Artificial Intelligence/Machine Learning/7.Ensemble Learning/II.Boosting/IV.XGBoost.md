### 1.Core Idea of XGBoost

>XGBoost is an optimized and scalable implementation of the Gradient Boosting framework. 
>
>While it is based on the same core principle as GBDT (training new learners to correct the residuals of the previous ensemble), XGBoost introduces several significant improvements.
>
>The most crucial one is a more formalized **regularized objective function**. 
>
>This objective function controls the model's complexity and prevents overfitting. 
>
>XGBoost uses a second-order Taylor expansion of the loss function to find the optimal solution more efficiently and accurately, which is a key difference from traditional GBDT that only uses the first-order gradient.

### 2.The Objective Function

>The objective function in XGBoost is what the algorithm tries to minimize at each step. It's the core of its innovation and consists of two parts: the **loss function**, which measures the model's error on the training data, and the **regularization term**, which penalizes the complexity of the model.

$${Obj}^{t}=\sum^{n}_{i=1}L(y_{i},\hat{y_{i}}^{(t-1)}+f_{t}(x_{i}))+\Omega(f_{t})$$

where

- L(yi​,y^​i​) is the loss function (e.g., Mean Squared Error for regression, Log Loss for classification).
	
- yi​ is the true label for the i-th sample. 
    
- y^​i(t−1)​ is the prediction for the i-th sample from the previous t−1 trees. 
    
- ft​(xi​) is the prediction from the new tree we are adding at step t. 
    
- Ω(ft​) is the regularization term for the new tree ft​. 


### 3.Taylor Expansion and Simplification

>To find the optimal tree ft​ quickly, XGBoost uses a second-order Taylor expansion of the loss function around the prediction $\hat{y}_{i}^{(t−1)}$​.


### 4.The Regularization Term

>The regularization term Ω(ft​) is defined based on the structure of the tree. It penalizes having too many leaves and having large leaf weights (predictions), which helps to create simpler, more generalizable trees.


### 5.Finding the Optimal Leaf Weights and Structure

>By substituting the regularization term into the objective function and grouping terms by leaf, we can find the optimal weight wj∗​ for each leaf and the resulting optimal objective function value.


### 6.Key Feature and Improvements of XGBoost

- **Regularization:** The inclusion of γ and λ in the objective function directly controls model complexity, making it more robust against overfitting than standard GBDT.
    
- **Sparsity-Aware Split Finding:** XGBoost has a built-in routine to handle missing values. It learns a default direction for missing values at each node.
    
- **Parallel and Distributed Computing:** While the trees are built sequentially, the process of finding the best split for each node can be parallelized. XGBoost has excellent support for this.
    
- **Cache-Aware Access:** XGBoost is designed to make optimal use of hardware by allocating internal buffers to store gradient statistics in a cache-friendly manner.
    
- **Column Block for Parallel Learning:** The data is sorted and stored in in-memory units called "blocks." This structure allows the expensive part of split-finding (iterating over columns) to be parallelized.