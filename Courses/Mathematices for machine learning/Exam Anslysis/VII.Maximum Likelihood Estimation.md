基于您提供的 **Lecture 8 (L8)** 课件、讲义以及近五年的考试真题，**Lecture 8: Maximum Likelihood and Unsupervised Learning (极大似然与无监督学习)** 是课程从“统计视角”转向“概率视角”的转折点。

在考试中，这一章的内容通常以 **极大似然估计 (MLE) 的推导 (Derivation)** 和 **指数族分布 (Exponential Families) 的性质** 为主。

以下是关于 L8 的考点总结与考察形式分析：

### 1. 核心考点 (Core Exam Points)

#### A. 极大似然估计 (Maximum Likelihood Estimation, MLE)

这是 L8 最核心的计算考点。虽然 L2/L3 也涉及 MLE，但 L8 将其推广到了任意概率分布，特别是指数族分布。

- **核心知识：**
    
    - **定义：** $\theta_{MLE} = \arg\max_{\theta} \prod P(x^{(i)}; \theta)$。
        
    - **NLL (负对数似然):** 通常最小化 $NLL(\theta) = -\sum \log P(x^{(i)}; \theta)$，因为它将乘积转化为求和，更易求导。
        
    - **推导步骤：** 写出 Likelihood $\to$ 取 Log $\to$ 求导 $\to$ 令导数为0解出 $\theta$ 1。
        
- **真题印证：**
    
    - **2024年 Q1b:** 要求推导线性回归中方差 $\sigma^2$ 的 MLE 2。这是一个非常经典的 L8 类型题目。
        
    - **2022年 Q2c:** 针对 Probabilistic CCA 模型，要求写出 MLE 目标函数，并推导 $\mu_a, \mu_b$ 的最优解 3。
        
    - **2021年 Q2a(i):** 对于伯努利分布，推导参数 $\mu$ 的 MLE 4。
        

#### B. 指数族分布 (Exponential Families)

这是 L8 的理论重点。

- **核心知识：**
    
    - **标准形式 (Canonical Form):** $p(x;\theta) = h(x) \exp(\theta^T s(x)) / z(\theta)$ 5。
        
    - **Sufficient Statistic (充分统计量):** $s(x)$。
        
    - **Partition Function (配分函数):** $z(\theta)$。
        
    - **性质：** 对数配分函数的导数等于充分统计量的期望：$\frac{d}{d\theta} \log z(\theta) = \mathbb{E}[s(x)]$ 6。这意味着 MLE 等价于矩匹配 (Method of Moments)。
        
- **真题印证：**
    
    - 虽然目前没有直接考“请把这个分布写成指数族形式”，但理解充分统计量的期望等于样本均值 ($\mathbb{E}[s(x)] = \frac{1}{m}\sum s(x^{(i)})$) 是解决 MLE 问题的快捷方式 7。
        

#### C. 矩估计 (Method of Moments, MoM)

- **核心知识：**
    
    - 令样本矩等于理论矩：$\frac{1}{m}\sum x^k = \mathbb{E}[x^k]$。
        
    - 对于指数族分布，MoM 估计量通常等于 MLE 估计量 8。
        

---

### 2. 考察形式 (Exam Question Formats)

根据近五年真题，L8 的考察形式主要如下：

#### 形式一：MLE 推导 (Derivation of MLE)

- **典型问法：**
    
    - "Compute the gradient of the log-likelihood with respect to..." (计算对数似然对某参数的梯度)。
        
    - "Compute the MLE for..." (计算某参数的 MLE)。
        
    - "Derive the Maximum Likelihood estimate of $\mu$ in terms of..." (推导 MLE 的闭式解)。
        
- **应对策略：**
    
    - 熟练掌握 Log 的性质 ($\log(ab) = \log a + \log b$, $\log(e^x) = x$)。
        
    - 能够对 Summation求导。
        
    - 常见分布的 PDF 必须看熟（虽然试卷可能会给，但熟练能提升速度）：高斯 (Gaussian)、伯努利 (Bernoulli)、泊松 (Poisson)、指数 (Exponential)。
        

#### 形式二：概率模型分析 (Probabilistic Modeling)

- **典型问法：**
    
    - "Write down the likelihood function for observing the data..." (写出观测数据的似然函数)。
        
    - "State the negative log likelihood..." (陈述负对数似然函数)。
        
- **应对策略：**
    
    - 区分 **Likelihood** (关于参数的函数) 和 **Density** (关于数据的函数)。
        
    - 能够处理 I.I.D. 假设（将联合概率写成连乘）。
        

### 3. 复习建议 (Summary for Revision)

1. **必练手推 MLE：** 找几个常见分布（Gaussian 的 $\mu$ 和 $\sigma^2$，Bernoulli 的 $\theta$，Exponential 的 $\lambda$），在白纸上完整推导一遍 MLE。2024年考了 Gaussian $\sigma^2$，2021年考了 Bernoulli，这是送分题，千万不能丢。
    
2. **理解 $\nabla \log z(\theta) = \mathbb{E}[s(x)]$：** 这个性质非常强大，它解释了为什么 MLE 往往就是让“模型均值”等于“样本均值”。
    
3. **注意变量：** 在求导时，搞清楚谁是变量（参数 $\theta$），谁是常数（数据 $x$）。
    

**一句话总结：L8 是“计算密集型”章节，考试必考 MLE 推导。请务必熟练掌握写出 Likelihood $\to$ Log $\to$ 求导 $\to$ 解方程的标准流程。**

***
***
基于您提供的 **Lecture 9 (L9)** 课件、讲义以及近五年的考试真题，**Lecture 9: Maximum Likelihood Estimation for Supervised Learning (监督学习的极大似然估计)** 是 L8 的延续，重点在于将 MLE 应用于有监督学习任务（如回归和分类）。

在考试中，这一章的内容通常涉及**特定模型（线性回归、逻辑回归）的 MLE 推导 (Derivation)** 以及**损失函数的概率解释 (Probabilistic Interpretation)**。

以下是关于 L9 的考点总结与考察形式分析：

### 1. 核心考点 (Core Exam Points)

#### A. 线性回归的概率视角 (Probabilistic Linear Regression)

这是 L9 最基础的考点。考试会考察你如何从概率模型推导出最小二乘法 (OLS)。

- **核心知识：**
    
    - **模型假设：** $y = X\theta + \epsilon, \epsilon \sim \mathcal{N}(0, \sigma^2)$。这意味着 $y \sim \mathcal{N}(X\theta, \sigma^2)$ 1。
        
    - **MLE 推导：** 写出 Likelihood $\prod \mathcal{N}(y^{(i)}|x^{(i)T}\theta, \sigma^2)$ $\to$ 取对数 $\to$ 忽略常数项 $\to$ 发现最小化 NLL 等价于最小化 MSE (Mean Squared Error) 2。
        
    - **结论：** **MLE with Gaussian Noise = OLS** 3。
        
- **真题印证：**
    
    - **2024年 Q1b:** 要求推导 $\sigma^2$ 的 MLE 4。这正是 L9 中线性回归概率视角的直接应用。
        
    - **2021年 Q2a:** 考察了 Bernoulli 分布的 MLE，虽然是分类问题，但推导思路与此一致。
        

#### B. 广义线性模型 (GLM) 与分类 (Classification)

这是 L9 的进阶考点，特别是逻辑回归 (Logistic Regression)。

- **核心知识：**
    
    - **Link Function:** 为了将线性输出 $x^T\theta$ 映射到概率空间 (0,1) 或其他空间，引入链接函数（如 Sigmoid/Logistic 函数）5。
        
    - **Bernoulli Likelihood:** 对于二分类，似然函数为 $P(y|\theta) = \sigma(x^T\theta)^y (1-\sigma(x^T\theta))^{1-y}$ 6。
        
    - **NLL 推导：** 取负对数得到 **Binary Cross-Entropy (二元交叉熵)** 损失函数 7。
        
    - **梯度推导：** $\frac{\partial}{\partial \theta} NLL = \sum (y^{(i)} - \sigma(x^{(i)T}\theta))x^{(i)}$ 8。
        
- **真题印证：**
    
    - **2023年 Q2a:** 要求写出 Logistic Regression 的 Likelihood 和 NLL，并推导梯度。这是 L9 内容的完美复刻 9。
        

#### C. 拉普拉斯噪声与 L1 损失 (Laplace Noise & MAE)

这是一个非常经典的扩展考点，用于考察学生举一反三的能力。

- **核心知识：**
    
    - 如果假设噪声 $\epsilon$ 服从拉普拉斯分布 (Laplace Distribution) $p(\epsilon) \propto \exp(-|\epsilon|)$，那么 MLE 等价于最小化绝对误差 (Mean Absolute Error, MAE) 10。
        
    - 对比：Gaussian $\to$ MSE (L2 Loss)；Laplace $\to$ MAE (L1 Loss)。
        
- **真题印证：**
    
    - **Lecture Slides 9 Slide 46:** 明确给出了一个 "Exam Preparation" 题目，要求证明 Laplace Likelihood 对应 MAE 11。这极有可能是考试原题或变体。
        

---

### 2. 考察形式 (Exam Question Formats)

根据近五年真题，L9 的考察形式主要如下：

#### 形式一：证明等价性 (Proof of Equivalence)

- **典型问法：**
    
    - "Show that the MLE for $\theta$ under Gaussian noise is equivalent to the OLS estimator." (证明高斯噪声下的 MLE 等价于 OLS)。
        
    - "Show that the MLE under Laplace noise equals the MAE minimizer." (证明拉普拉斯噪声下的 MLE 等价于 MAE 最小化)。
        
- **应对策略：**
    
    - 写出 $p(y|x)$ 的概率密度函数。
        
    - 写出 Joint Likelihood $\prod p(y^{(i)}|x^{(i)})$.
        
    - 取 Log，去掉与 $\theta$ 无关的常数项。
        
    - 观察剩下的项是否为 $\sum (y-\hat{y})^2$ 或 $\sum |y-\hat{y}|$。
        

#### 形式二：推导梯度 (Derivation of Gradient)

- **典型问法：**
    
    - "Derive the gradient of the negative log-likelihood w.r.t. $\theta$." (推导 NLL 对 $\theta$ 的梯度)。
        
- **应对策略：**
    
    - 熟练掌握 Sigmoid 函数的导数 $\sigma' = \sigma(1-\sigma)$。
        
    - 在推导 Logistic Regression 梯度时，注意利用 Chain Rule。
        

#### 形式三：概率模型构建 (Probabilistic Modeling)

- **典型问法：**
    
    - "Consider a scenario... write down the likelihood function." (针对某场景写出似然函数)。
        
    - 比如 **2024年 Q2c:** 考察了 Binomial 分布的似然函数和 Beta 后验 12。虽然这是贝叶斯内容（L10/L11），但写 Likelihood 是第一步，属于 L9 的范畴。
        

### 3. 复习建议 (Summary for Revision)

1. **必背结论：**
    
    - Gaussian Noise $\iff$ MSE Loss (L2)
        
    - Laplace Noise $\iff$ MAE Loss (L1)
        
    - Bernoulli Likelihood $\iff$ Binary Cross-Entropy Loss
        
2. **熟练推导 Logistic Regression：** 2023年刚考过，但作为核心考点，仍需熟练掌握从 Likelihood 到 Gradient 的全过程。
    
3. **关注 Slide 46 的练习题：** 讲义中专门列出的 "Exam Preparation (Laplace and MAE)" 13 是极高优先级的复习材料，务必能够独立推导。
    

**一句话总结：L9 是将“损失函数”赋予“概率意义”的章节。考试重点是证明特定噪声分布下的 MLE 等价于某种常见的损失函数最小化（如 MSE 或 MAE）**


