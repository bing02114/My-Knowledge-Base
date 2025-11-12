基于您提供的五份历年真题（2020-2024）以及Lecture 2 (L2) 的课件与讲义，**Linear Models (线性模型)** 是该课程绝对的核心考点之一。它不仅作为独立题目出现，还常与概率（MLE/MAP）和优化（梯度下降）结合考察。

以下是关于 L2 Linear Regression 的考点总结与考察形式分析：

### 1. 核心考点 (Core Exam Points)

#### A. 矩阵微积分与最小二乘法推导 (Vector Calculus & OLS Derivation)

这是最基础也是最硬核的考点。Lecture 2 花了大量篇幅讲解如何对 $\mathcal{L}(\theta) = \|X\theta - y\|_2^2$ 进行求导 1111。

- **考点细节：**
    
    - 熟练运用矩阵求导恒等式，特别是 $\nabla_{\theta}c^{\top}\theta=c^{\top}$ 和 $\nabla_{\theta}(\theta^{\top}A\theta)=\theta^{\top}(A+A^{\top})$ 2222。
        
    - 推导普通最小二乘 (OLS) 的闭式解 $\theta=(X^{\top}X)^{-1}X^{\top}y$ 3。
        
    - **2021年 Q3a** 考察了计算闭式解与梯度下降的计算成本对比 4。
        
    - **2020年 Q1** 考察了线性自编码器（类似线性回归）的梯度推导 5555。
        

#### B. 基函数展开 (Basis Expansion)

为了处理非线性关系，课程引入了 $\phi(x)$ 的概念 6。

- **考点细节：**
    
    - 如何构建 $\phi(x)$ 来捕捉特定的非线性关系（如多项式、指数关系等）7。
        
    - 证明某些看似复杂的模型（如多层线性网络）实际上等价于经过仿射变换的线性回归 8。
        
    - **2024年 Q2a** 要求证明一个去除了激活函数的深度网络本质上是线性模型 9。
        
    - **2023年 Q1e** 给定资产价格与特征的指数/二次关系，要求写出具体的 $\phi(x)$ 10。
        

#### C. 正则化 (Regularization)

为了防止过拟合，引入了正则项（如 Ridge Regression）1111。

- **考点细节：**
    
    - 理解 $l_2$ 正则化（Ridge）的目标函数 $\mathcal{L}(\theta) + \lambda||\theta||_2^2$ 及其几何意义 12121212。
        
    - 理解正则化系数 $\lambda$ 的作用：$\lambda$ 越大，参数越趋近于0，模型越平滑 13。
        
    - **贝叶斯解释：** 理解 $l_2$ 正则化对应于参数的高斯先验 (Gaussian Prior)，而 $l_1$ 对应拉普拉斯先验 (Laplace Prior)。
        
    - **2021年 Q3c** 明确考察了何时选择大的 $\lambda$，以及 $l_1$ 正则化对应的 MAP 目标函数和约束优化问题 141414。
        

#### D. 概率视角的线性回归 (Probabilistic Interpretation)

L2 的内容经常与 Lecture 5 的概率视角结合考察。

- **考点细节：**
    
    - **MLE (极大似然估计)：** 证明最小化平方误差等价于高斯噪声假设下的 MLE 15。
        
    - **估计量的性质：** 偏差 (Bias) 和方差 (Variance)。
        
    - **2024年 Q1b/c** 考察了线性回归中方差 $\sigma^2$ 的 MLE 推导，以及估计量的有偏/无偏性讨论 161616。
        

---

### 2. 考察形式 (Exam Question Formats)

根据历年试卷，L2 的考察形式主要分为以下三类：

#### 类型一：推导与计算 (Derivation & Calculation)

- **形式：** 给定一个变体的损失函数（例如加了正则项，或者矩阵形式略有不同），要求你画出计算图 (Computational Graph) 或使用矩阵微积分求梯度。
    
- **例题风格：**
    
    - "Derive the gradient of the log-likelihood with respect to $\sigma^2$." (2024 Q1c) 17
        
    - "Consider a linear autoencoder... represent the derivatives... using matrix chain rule." (2020 Q1c) 18
        

#### 类型二：建模与设计 (Modeling & Design)

- **形式：** 给出一个实际场景（如资产定价、疾病传播），描述变量间的非线性关系，要求你写出 **Basis Expansion function $\phi(x)$**。
    
- **例题风格：**
    
    - "Asset price depends exponentially on $x_1$... quadratically on $x_2$. Write the basis expansion function $\phi(x)$." (2023 Q1e) 19
        

#### 类型三：概念辨析与解释 (Conceptual Analysis)

- **形式：** 询问关于模型性质的理解，如过拟合、正则化的选择、计算复杂度对比、数据预处理的作用。
    
- **例题风格：**
    
    - "Describe and explain the role of data normalization." (2024 Q2b) 20
        
    - "Compare computational cost of full-batch gradient descent vs closed-form solution." (2021 Q3a) 21
        
    - "Explain why linear regression is still a suitable model for these non-linear relationships." (2023 Q1e) 22
        

### 3. 复习建议 (Summary for Revision)

针对 L2，建议您重点掌握：

1. **手推 OLS：** 能够闭眼写出 $(X\theta - y)^T(X\theta - y)$ 的梯度推导过程 23。
    
2. **背诵恒等式：** 熟记 $\nabla_x x^TAx$ 和 $\nabla_x b^Tx$ 等矩阵求导公式 24242424。
    
3. **理解 $\phi(x)$：** 明白如何通过 $\phi(x)$ 把非线性问题转化为线性问题求解 25。
    
4. **联系概率：** 明白 Ridge Regression $\leftrightarrow$ Gaussian Prior，Lasso $\leftrightarrow$ Laplace Prior 26。



***
***
### 1.解析解法

**公式推导**

* 需要知道线性回归的解析解以及推导过程

**复杂度**

* 会计算闭式解的复杂度

### 2.正则化

**意义**

* 会描述L2正则化对线性回归的影响

**参数**

* 知道如何选择正则化系数