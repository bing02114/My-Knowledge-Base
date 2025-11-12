基于您提供的 **Lecture 10 (L10)** 课件、讲义以及近五年的考试真题，**Lecture 10: Bayesian Machine Learning (Part I) (贝叶斯机器学习第一部分)** 是课程中最核心、最难、也是考分占比极高的章节。

在考试中，这一章的内容通常涉及 **贝叶斯推断 (Bayesian Inference)** 的全过程，特别是 **共轭先验 (Conjugate Priors)** 的推导和 **后验分布 (Posterior Distribution)** 的计算。

以下是关于 L10 的考点总结与考察形式分析：

### 1. 核心考点 (Core Exam Points)

#### A. 贝叶斯定理与共轭先验 (Bayes Theorem & Conjugate Priors)

这是 L10 的基石，几乎每年的考试都会涉及。

- **核心知识：**
    
    - **贝叶斯公式:** $P(\theta | \mathcal{D}) \propto P(\mathcal{D} | \theta) P(\theta)$ 1。
        
    - **共轭先验:** 如果先验 $P(\theta)$ 与似然 $P(\mathcal{D}|\theta)$ 的乘积形式与先验属于同一分布族，则称该先验为共轭先验 2。
        
    - **常见共轭对 (Conjugate Pairs):**
        
        - **Beta-Bernoulli:** Likelihood 是 Bernoulli ($\theta^k(1-\theta)^{n-k}$)，Prior 是 Beta ($\theta^{\alpha-1}(1-\theta)^{\beta-1}$)，Posterior 是 Beta ($\alpha+k, \beta+n-k$) 3。
            
        - **Gaussian-Gaussian:** Likelihood 是 Gaussian，Prior 是 Gaussian，Posterior 也是 Gaussian 4。
            
- **真题印证：**
    
    - **2024年 Q2c:** 考察了 Binomial Likelihood 和 Beta Prior，要求推导 Beta Posterior 并解释参数含义。这是 Beta-Bernoulli 共轭的直接应用。
        
    - **2022年 Q1a:** 给定 Bernoulli Likelihood 和 Uniform Prior (Beta(1,1))，求后验分布并计算后验均值。
        
    - **2021年 Q2a:** 涉及 Bernoulli 变量和 Beta 分布的参数估计。
        

#### B. 贝叶斯线性回归 (Bayesian Linear Regression)

这是 L10 的重难点，涉及矩阵运算和高斯分布的性质。

- **核心知识：**
    
    - **模型假设:** Likelihood $y \sim \mathcal{N}(X\theta, \sigma^2I)$，Prior $\theta \sim \mathcal{N}(0, \tau^2I)$ 5。
        
    - **后验推导 (Deriving Posterior):** 通过“配方” (completing the square) 或“系数匹配” (equating coefficients) 的方法，证明后验 $P(\theta | \mathcal{D})$ 是高斯分布。
        
    - **后验参数:**
        
        - Mean: $\mu_{post} = (X^TX + \frac{\sigma^2}{\tau^2}I)^{-1}X^Ty$ 6。
            
        - Covariance: $\Sigma_{post} = (\frac{1}{\sigma^2}X^TX + I/\tau^2)^{-1}$ 7。
            
    - **与 Ridge Regression 的联系:** 后验均值 $\mu_{post}$ 恰好等于 Ridge Regression 的解（当 $\lambda = \sigma^2/\tau^2$ 时）8。
        
- **真题印证：**
    
    - **2021年 Q3b:** 假设 Gaussian Prior，要求推导 $\theta$ 的后验分布，并讨论 $N \to \infty$ 时的收敛分布。这直接考察了 Bayesian Linear Regression 的推导。
        

#### C. 后验预测分布 (Posterior Predictive Distribution)

不仅仅是求参数 $\theta$，还要对新数据 $x^*$ 进行预测。

- **核心知识：**
    
    - **定义:** $P(x^* | \mathcal{D}) = \int P(x^* | \theta) P(\theta | \mathcal{D}) d\theta$ 9。
        
    - **计算:** 对于 Beta-Bernoulli 模型，后验预测均值就是后验分布的期望 $\mathbb{E}[\theta | [cite_start]\mathcal{D}]$ 10。
        
- **真题印证：**
    
    - **2021年 Q2b(iii):** 要求计算 $p(x_{N+1}|t)$，即在给定前 $N$ 次观测的统计量 $t$ 后，下一次观测 $x_{N+1}$ 的条件密度。这就是典型的 Posterior Predictive Distribution。
        

---

### 2. 考察形式 (Exam Question Formats)

根据近五年真题，L10 的考察形式非常固定且硬核：

#### 形式一：推导后验分布 (Derive the Posterior)

- **典型问法：**
    
    - "Derive the posterior distribution for $\theta$ given the observed data..." (推导给定数据下 $\theta$ 的后验分布)。
        
    - "Show that it follows a Beta distribution." (证明它服从 Beta 分布)。
        
- **应对策略：**
    
    - 写出 $Posterior \propto Likelihood \times Prior$。
        
    - 代入具体的 PDF/PMF 公式。
        
    - 合并同类项（例如 $\theta$ 的指数），忽略常数项。
        
    - 识别出结果是哪个已知分布的核 (kernel)，从而写出分布名称和参数。
        

#### 形式二：贝叶斯与正则化的联系 (Connection to Regularization)

- **典型问法：**
    
    - "Show that the MAP estimate with Gaussian prior is equivalent to Ridge Regression." (证明高斯先验下的 MAP 估计等价于 Ridge 回归)。
        
    - "What is the converging distribution of $p(\theta|\mathcal{D})$ when $N \to \infty$?" (当数据量无穷大时，后验分布收敛于什么？——收敛于 Dirac Delta 函数，即 MLE 点估计)。
        
- **应对策略：**
    
    - 熟记 Bayesian Linear Regression 的后验均值公式，并能将其变形为 Ridge 的形式 $(X^TX + \lambda I)^{-1}X^Ty$。
        

#### 形式三：计算预测概率 (Calculate Predictive Probability)

- **典型问法：**
    
    - "What is the probability of the next outcome being 1?" (下一次结果为1的概率是多少？)
        
    - "Calculate the expected value of the posterior." (计算后验分布的期望)。
        
- **应对策略：**
    
    - 对于 Beta 后验 $Beta(\alpha', \beta')$，预测均值就是 $\alpha' / (\alpha' + \beta')$。
        
    - 这一步通常是送分题，只要后验参数推对，直接代入期望公式即可。
        

### 3. 复习建议 (Summary for Revision)

1. **死磕 Beta-Bernoulli 推导：** 这是最基础也是最常考的共轭模型。务必能从 Likelihood $\theta^k(1-\theta)^{n-k}$ 和 Prior $\theta^{\alpha-1}(1-\theta)^{\beta-1}$ 推导出 Posterior $Beta(\alpha+k, \beta+n-k)$。
    
2. **熟练掌握高斯配方：** Bayesian Linear Regression 的推导涉及到矩阵求导和配方技巧（completing the square），这是 L10 的难点。复习讲义 Lecture Note 10.2.1 节 11，尝试在白纸上重推一遍。
    
3. **理解 MAP 与 MLE 的区别：** MAP (Maximum A Posteriori) 是后验分布的众数 (Mode)，包含了先验信息；MLE 是似然函数的最大值。当先验是 Uniform 时，MAP = MLE。
    

**一句话总结：L10 是“贝叶斯推断”的主战场，考试必考“写出 Likelihood $\times$ Prior $\to$ 识别 Posterior 分布”的标准流程，特别是针对 Beta-Bernoulli 和 Gaussian-Gaussian 模型。**


。**