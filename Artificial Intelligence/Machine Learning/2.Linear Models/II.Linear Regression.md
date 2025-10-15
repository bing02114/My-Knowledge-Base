### 1.Objective

>Linear regression attempts to learn a linear model that predicts a real-valued output as accurately as possible.
>
>The goal is to make $f(x_{i})≃ y_{i}$

### 2.Parameter Estimation

#### 2.1 Least Square Method

>This method finds the parameters w and b that minimize the mean squared error (also known as square loss). It corresponds to finding a line that minimizes the sum of Euclidean distances from all sample points to the line.

$$\theta=(X^{T}X)^{-1}X^{T}y$$

#### 2.2 Variation

**Log-linear Regression**

$$lny=w^{T}x+b$$

**Generalized Linear Model**

$$y=g^{-1}(w^{T}x+b)$$




特性正规方程法 (Normal Equation)梯度下降法 (Gradient Descent)**求解方式**解析解，一步到位迭代解，逐步逼近**计算复杂度**O(n3) (主要耗时在求逆)，其中n是特征数O(k⋅m⋅n)，其中k是迭代次数**超参数****无****需要**选择学习率 η 和迭代次数 k**数据缩放**不需要**强烈推荐**，可以加快收敛速度**适用场景****特征数量较少时** (n < 10,000) 非常快且精准**特征数量巨大时** 是唯一可行的选择**优点**简单、无需调参可扩展性强，适用于非常大的数据集**缺点**当特征数巨大时，矩阵求逆非常慢且耗内存需要仔细调整超参数，否则可能不收敛或收敛慢