基于您提供的 **Lecture 5 (L5)** 课件、讲义以及近五年的考试真题（特别是2023年的试卷），L5 **"Convexity, Convergence, & Optimization" (凸性、收敛性与优化)** 是理论性最强的一章。

在考试中，这一章的内容通常不涉及复杂的计算图绘制，而是侧重于**数学证明 (Proofs)** 和 **理论条件的陈述 (Theoretical Conditions)**。

以下是关于 L5 的考点总结与考察形式分析：

### 1. 核心考点 (Core Exam Points)

#### A. 凸性的定义与判别 (Definitions & Tests for Convexity)

这是 L5 最直接的考点。2023年的考试直接考察了这一块。

- **核心知识：**
    
    - **Secant Definition (割线定义/零阶条件):** $f(tx + (1-t)y) \le tf(x) + (1-t)f(y)$。这是凸函数的标准定义 1。
        
    - **Tangent Definition (切线定义/一阶条件):** $f(y) \ge f(x) + \nabla f(x)^T(y-x)$。即凸函数始终位于其切线（或超平面）上方。
        
    - **Hessian Test (海森矩阵判别法/二阶条件):** 函数 $f$ 是凸的 $\iff$ 其海森矩阵 $H$ 是半正定的 (Positive Semi-Definite, PSD)，即 $\forall v, v^T H v \ge 0$ 2。
        
    - **性质：** 凸函数的局部极小值即为全局极小值 3。
        
- **真题印证：**
    
    - **2023 Q1a(i):** 明确要求 "state the definition of convexity in terms of the tangent of a function" (用切线定义凸性)。
        
    - **2023 Q1a(ii):** 要求证明 "maximum of two convex functions is itself a convex function" (两个凸函数的最大值仍是凸函数)。
        
    - **2023 Q2d:** 要求证明 Logistic Regression 的 Hessian 是 PSD 的，从而说明它是凸优化问题。
        

#### B. 线性回归的梯度下降收敛性分析 (Convergence Analysis of GD in Linear Models)

这是 L5 讲义中篇幅最长、数学推导最密集的部分。虽然还没考过完整的推导，但其结论（特征值与学习率的关系）是高频概念。

- **核心知识：**
    
    - **递推公式 (Recurrence Relation):** 证明 GD 在线性回归下的更新公式可写为 $\theta^{(t)} - \theta^* = (I - \alpha X^\top X)^t (\theta^{(0)} - \theta^*)$ 4。
        
    - **收敛条件 (Convergence Condition):** 收敛取决于矩阵 $(I - \alpha X^\top X)$ 的特征值。为了收敛，需要最大特征值 $\lambda_{max} < 1$。
        
    - **学习率界限 (Learning Rate Bound):** 必须满足 $\alpha < \frac{2}{\lambda_{max}(X^\top X)}$ 才能保证收敛 5。
        
- **考察潜力：** 这是一个极好的“压轴题”素材，可能会问你如何选择 $\alpha$ 或者证明某种特定情况下的收敛性。
    

#### C. 梯度下降的进展界 (Progress Bounds & Lipschitz Continuity)

这是解释“为什么 GD 能工作”的理论基础。

- **核心知识：**
    
    - **Lipschitz Continuous Gradient:** 梯度的变化率被常数 $L$ 有界：$\|\nabla \mathcal{L}(u) - \nabla \mathcal{L}(v)\| [cite_start]\le L\|u-v\|$ 6。
        
    - **Descent Lemma (下降引理):** 如果满足上述条件，每一步 GD 都会使 Loss 至少下降一定量：$\mathcal{L}(\theta^{(t+1)}) \le \mathcal{L}(\theta^{(t)}) - \frac{1}{2L}\|\nabla \mathcal{L}(\theta^{(t)})\|^2$ 7。
        
- **真题印证：** 暂无直接大题，但这是理解优化算法效率的基础，常用于解释为什么牛顿法比 GD 快（二阶 vs 一阶收敛）。
    

---

### 2. 考察形式 (Exam Question Formats)

根据近五年真题，L5 的考察形式非常“数学化”，主要有以下两类：

#### 形式一：定义与证明 (Definition & Proof)

- **典型问法：**
    
    - "State the definition of convexity..." (陈述定义)
        
    - "Prove that the Hessian is positive semi-definite." (证明海森矩阵半正定)
        
    - "Prove that the maximum of two convex functions is convex." (证明凸函数性质)
        
- **应对策略：**
    
    - **背诵：** 必须熟记凸函数的三种定义（Secant, Tangent, Hessian）。
        
    - **矩阵代数：** 在证明 Hessian PSD 时，通常需要利用 $v^T A v \ge 0$ 的形式。对于 GLM（如逻辑回归），通常会推导出 $v^T X^T D X v = (Xv)^T D (Xv)$ 的形式，其中 $D$ 是非负对角矩阵，从而证明其非负。
        

#### 形式二：收敛性分析 (Convergence Analysis)

- **典型问法：**
    
    - "For what learning rate $\alpha$ will the algorithm converge?" (询问 $\alpha$ 的范围)
        
    - "Derive the recurrence relation for the error term $\theta^{(t)} - \theta^*$." (推导误差递推项)
        
- **应对策略：**
    
    - 熟练掌握 Lecture Note 5.5 节中关于 Linear Regression GD 的推导过程。特别是如何从 $\theta^{(t+1)} = \theta^{(t)} - \alpha X^T(X\theta^{(t)} - y)$ 变换到误差项的几何级数形式。
        

### 3. 复习建议 (Summary for Revision)

1. **攻克凸性证明：** 重点复习 2023 Q1a 和 Q2d。特别是如何证明 $f(x) = \log(1+e^x)$ 或类似的 Loss Function 是凸的（求二阶导/Hessian）。
    
2. **理解几何级数矩阵形式：** 明白 $(I - \alpha H)^t$ 随 $t \to \infty$ 趋于 0 的条件是 $|1 - \alpha \lambda_i| < 1$。这是 L5 关于收敛性最核心的数学直觉。
    
3. **区分牛顿法与梯度下降：** 虽然牛顿法在 L3 提过，但 L5 提供了理论支撑（二阶泰勒展开）。理解牛顿法利用了曲率（Curvature/Hessian）信息，因此收敛更快，但计算 $H^{-1}$ 昂贵。
    

**一句话总结：L5 是“硬数学”章节，考试喜欢考定义背诵和严谨的数学证明（特别是凸性和Hessian矩阵）。**


***
***
### 1.凸性

**定义**

* 会从割线定义得到切线和凸性的定义

**性质**

* 会证明两个凸函数的最大值仍然是凸函数



### 2.海森矩阵

**计算**

* 会计算某些模型的海森矩阵

**性质**

* 会证明海森矩阵的正定/半正定性
* 会描述海森矩阵对优化问题的意义

**复杂度**

* 会计算求海森矩阵过程的复杂度（矩阵乘法等）