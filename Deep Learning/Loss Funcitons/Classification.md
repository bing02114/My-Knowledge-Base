### 1.Binary Cross-Entropy / Log Loss

>The most common loss function for **binary classification** problems (two classes, 0 and 1). It measures the performance of a model whose output is a probability value between 0 and 1.

$$L=-\frac{1}{n}\sum^{n}_{i=1}[y_{i}log(\hat{y_{i}})+(1-y_i)log(1-\hat{y_{i}})]$$
**Properties**

>The loss increases as the predicted probability diverges from the actual label. A perfect model would have a log loss of 0.


### 2.Categorical Cross-Entropy

>A generalization of Binary Cross-Entropy used for **multi-class classification** problems.

$$L=-\frac{1}{n}\sum^{n}_{i=1}\sum^{C}_{j=1}y_{ij}log(\hat{y_{ij}})$$

**Properties**

>It measures the **dissimilarity between the true distribution (one-hot encoded vector) and the predicted distribution (output from a softmax layer).**

### 3.Hinge Loss

>A loss function primarily used for "maximum-margin" classification, most notably for **Support Vector Machines (SVMs)**.

$$L=\frac{1}{n}\sum^{n}_{i=1}max(0,1-y_i·\hat{y_i})$$
**Properties**

>It penalizes predictions that are not only on the wrong side of the decision boundary but also those that are too close to it (within the margin). Correctly classified points that are outside the margin have a loss of 0.**特性：** 它不仅惩罚那些在决策边界错误一侧的预测，也惩罚那些离边界太近（在间隔内部）的预