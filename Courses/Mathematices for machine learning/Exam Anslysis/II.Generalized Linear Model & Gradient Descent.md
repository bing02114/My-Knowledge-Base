基于您提供的Lecture 3 (L3) 课件、讲义以及近五年的考试真题，**Lecture 3: Generalized Linear Models & Gradient Descent (广义线性模型与梯度下降)** 在考试中主要扮演着连接线性模型（L2）与概率/深度学习（后续课程）的桥梁角色。

L3 的核心考点非常集中，主要围绕 **“为什么 OLS 不再适用”** 以及 **“如何通过梯度下降求解非线性问题”** 展开。

以下是关于 L3 的考点总结与考察形式分析：

### 1. 核心考点 (Core Exam Points)

#### A. 梯度下降与 OLS 的计算复杂度对比 (Computational Complexity: GD vs. OLS)

这是一个高频且极具区分度的考点。L3 讲义花了很大篇幅详细推导了两者的复杂度 1111。

- **核心知识：**
    
    - **OLS (Ordinary Least Squares):** 计算闭式解 $\theta=(X^{\top}X)^{-1}X^{\top}y$ 涉及矩阵乘法和求逆。对于 $X \in \mathbb{R}^{m \times n}$，复杂度主要由矩阵求逆主导，整体为 **$O(n^2m + n^3)$** 2222。
        
    - **GD (Gradient Descent):** 迭代更新 $\theta^{(t+1)}=\theta^{(t)}-\alpha\nabla_{\theta}\mathcal{L}$。每次迭代计算梯度 $X^{\top}(X\theta-y)$ 的复杂度为 **$O(mn)$** 3。若迭代 $k$ 次，总复杂度为 **$O(kmn)$** 4。
        
    - **结论：** 当特征维度 $n$ 很大时（$n > k$），梯度下降比 OLS 更高效 5。
        
- **真题印证：**
    
    - **2021年 Q3a:** 明确要求比较全批量梯度下降 (full-batch GD) 与闭式解 (closed-form) 的计算成本，并询问在什么情况下 $N$ (数据量) 较大时应选择哪种方法。
        
    - **2023年 Q2e:** 要求写出梯度和海森矩阵 (Hessian) 的计算复杂度，并据此讨论何时选择牛顿法 (Newton-Raphson) 还是梯度下降。
        

#### B. 广义线性模型 (GLMs) 的梯度推导 (Derivation of Gradients for GLMs)

由于引入了非线性激活函数（Link Function 的逆），GLM 通常没有闭式解，必须使用链式法则求导 66。

- **核心知识：**
    
    - **通用形式：** $y=g^{-1}(\theta^{\top}x)$ 7。
        
    - **Poisson Regression (泊松回归):** 使用指数函数 $\hat{y}=exp(X\theta)$ 8。讲义详细推导了其梯度形式：$\nabla_{\theta}\mathcal{L}(\theta)=2((exp(X\theta)-y)\circ exp(X\theta))^{\top}X$ 9。
        
    - **Logistic Regression (逻辑回归):** 使用 Sigmoid 函数 $\sigma(z) = \frac{1}{1+e^{-z}}$ 10101010。
        
- **真题印证：**
    
    - **2023年 Q2a/c:** 这是一个典型的 L3 题目，要求写出逻辑回归的似然函数，并使用商法则 (quotient rule) 求导，最后计算梯度和海森矩阵。
        
    - **2020年 Q1c:** 虽然是自编码器，但考查形式是“使用多元链式法则表示导数”，与 L3 中推导 GLM 梯度的技巧一致。
        

#### C. 凸性与优化算法 (Convexity & Optimization)

- **核心知识：**
    
    - 理解为什么某些损失函数（如 MSE 用于泊松回归或逻辑回归）虽然可导，但可能不是最佳选择（非凸或无闭式解）11111111。
        
    - **梯度下降 (Gradient Descent):** 迭代公式、学习率 $\alpha$ 的影响（步长太大震荡，太小收敛慢）121212121212121212。
        
- **真题印证：**
    
    - **2023年 Q2d:** 要求证明 Hessian 是半正定的 (Positive Semi-Definite)，从而证明优化问题的凸性 (Convexity)。
        

---

### 2. 考察形式 (Exam Question Formats)

根据近五年真题，L3 的内容通常以以下形式出现：

#### 形式一：复杂度分析题 (Complexity Analysis)

- **典型问法：** "State the computational complexity of computing the gradient..." 或 "For what N is it definitely preferable to compute the closed-form solution?"
    
- **应对策略：** 必须背诵 OLS ($O(n^3)$) 和 GD ($O(kmn)$) 的大O符号表达式，并能用简单的句子解释每一项来源（例如：$n^3$ 来自矩阵求逆，$mn$ 来自矩阵向量乘法）。
    

#### 形式二：数学推导题 (Derivation)

- **典型问法：** "Compute the gradient and Hessian of the likelihood..."
    
- **应对策略：**
    
    - 熟练掌握 Sigmoid 函数的导数性质：$\sigma'(z) = \sigma(z)(1-\sigma(z))$。
        
    - 熟练掌握指数函数的矩阵求导：$\nabla_\theta exp(X\theta)$。
        
    - 注意链式法则在矩阵形式下的维度匹配。
        

#### 形式三：概念解释题 (Conceptual Explanation)

- **典型问法：** "Why is linear regression not suitable for this situation?" (参考 L3 讲义中关于输出范围约束的讨论，如泊松回归用于计数，逻辑回归用于分类) 13131313。
    
- **应对策略：** 结合输出空间的限制（例如：必须为正数、必须在0到1之间）来回答。
    

### 3. 复习建议 (Summary for Revision)

1. **死磕复杂度：** 请务必理解并记住 Slide 37-45 关于 Computational Complexity 的推导过程 14。这是拿分点，也是容易混淆的点。
    
2. **手推逻辑回归：** 2023年刚刚考过逻辑回归的完整推导，这意味着你需要对 GLM 的推导流程非常熟悉。建议尝试推导讲义中提到的 **Poisson Regression + MSE Loss** 的梯度 15，作为练习，以防考试更换 Link Function。
    
3. **关注 Link Function：** 理解 $g^{-1}$ 的作用是将线性预测 $\theta^T x$ 映射到目标空间（如正实数或概率空间）16。

***
***
### 1.对数似然回归

**Sigmoid函数**

* **微分**：会求导Simgoid函数

**似然函数**

* **公式**：会写对数似然回归的分类概率和负对数似然
* **微分**：会求似然函数的梯度，包括推导过程
* **性质**：会证明对数似然回归没有闭式解

### 2.基函数扩展

**扩展函数设计**

* 会根据给定的问题设计目标扩展函数

**性质证明**

* 会证明使用基函数扩展的模型仍然是线性回归模型（参数的线性回归）

### 3.梯度下降

**复杂度**

* **计算**：会计算梯度下降的复杂度并与求闭式解复杂度比较
* **应用场景**：会分析梯度下降和闭式解何时使用

**设计**

* **梯度下降改进**：知道代替全批量梯度下降法的效率提升方法