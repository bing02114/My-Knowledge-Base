基于您提供的五份历年真题（2020-2024）以及Lecture 4 (L4) 的课件与讲义，**Lecture 4: Deep Learning & Automatic Differentiation (深度学习与自动微分)** 是该课程考试中**最稳定、最必考**的模块之一。几乎每年的第一题或第二题都会涉及到计算图和自动微分。

以下是关于 L4 的考点总结与考察形式分析：

### 1. 核心考点 (Core Exam Points)

#### A. 计算图的绘制 (Computational Graphs)

这是自动微分的基础。考试通常会给出一个具体的数学函数（可能是概率密度函数、损失函数或矩阵运算），要求将其分解为基本算子（primitives）。

- **考点细节：**
    
    - 识别输入节点、中间节点和输出节点。
        
    - 正确处理矩阵运算（Matrix Multiplication）、逐元素运算（Element-wise）和特殊函数（Log, Exp, Trace, Cholesky等）。
        
    - **2024年 Q1a:** 柯西分布的分母部分 $\gamma[1+(\frac{x-x_{0}}{\gamma})^{2}]$ 的计算图 1。
        
    - **2023年 Q1c:** 高斯分布对数密度 $L(y;\mu,\sigma^{2})$ 的计算图 2。
        
    - **2022年 Q1b:** 涉及 Trace 和 Cholesky 分解的复杂函数 $f=Tr(L)+\frac{1}{2}y^{\top}L^{-\top}L^{-1}y$ 的计算图 3。
        

#### B. 自动微分模式的选择与效率分析 (Forward vs. Reverse Mode AD)

这是 L4 最核心的概念考点，主要考察对时间复杂度和空间复杂度的理解。

- **核心知识：**
    
    - **Forward Mode (前向模式):** 适合 **输入维度少 ($N_{in} \ll N_{out}$)** 的情况。计算 Jacobian-Vector Product ($Jv$)。复杂度与输入维度成正比 $O(N_{in})$ 4。
        
    - **Reverse Mode (反向模式/Backprop):** 适合 **输出维度少 ($N_{in} \gg N_{out}$)** 的情况（如标量 Loss）。计算 Vector-Jacobian Product ($v^TJ$)。复杂度与输出维度成正比 $O(N_{out})$ 5。
        
    - **结论：** 机器学习通常计算标量损失函数对大量参数的梯度，因此首选 **Reverse Mode**。
        
- **真题印证：**
    
    - **2024年 Q1a(ii):** 明确询问计算 $\partial/\partial\gamma$ 时，Forward 还是 Backward 模式在计算和空间上更高效 6。
        
    - **2023年 Q2b:** 询问 "In general, when is it preferable to use backward mode automatic differentiation?" 7。
        

#### C. 具体传播过程推导 (Algorithmic Derivation)

考试可能要求写出具体的更新公式，而不仅仅是求导结果。

- **考点细节：**
    
    - **Forward Mode:** 写出 Primal Trace (数值) 和 Tangent Trace (导数) 的更新。
        
    - **Reverse Mode:** 写出 Adjoint (伴随变量 $\bar{v} = \frac{\partial L}{\partial v}$) 的更新公式，即 Chain Rule 的累加 $\sum \frac{\partial L}{\partial child} \frac{\partial child}{\partial parent}$。
        
    - **2023年 Q1d:** 要求写出 Forward mode updates for the value tangent 8。
        
    - **2022年 Q1c:** 要求推导每个操作的 Backwards pass 9。
        

#### D. 深度线性网络 (Deep Linear Networks)

虽然 L4 介绍了非线性激活函数，但考试常考察“如果没有激活函数会怎样”。

- **考点细节：**
    
    - 证明多层线性网络（去除激活函数）等价于单层线性模型（矩阵连乘 $W_L...W_1 = W_{total}$）。
        
    - **2024年 Q2a:** 要求证明一个移除了激活函数的深度网络只是线性模型的一种复杂写法 10。
        

---

### 2. 考察形式 (Exam Question Formats)

根据历年试卷，L4 的考察形式非常固定，通常出现在 Q1 或 Q2 的前半部分：

#### 形式一：画图与分析 (Draw & Analyze)

- **典型问法：** "Draw the computational graph..." 紧接着 "Discuss which would be more efficient: forward or backward propagation..."
    
- **应对策略：**
    
    - 画图时，节点代表变量（Scalars/Vectors/Matrices），边代表操作。
        
    - 分析效率时，必须比较 Input Dimension (参数数量) 和 Output Dimension (Loss 维度)。如果是 Loss Function，输出是 1 (Scalar)，必选 Backward Mode。
        

#### 形式二：算法执行 (Execute the Algorithm)

- **典型问法：** "Write out the forward mode updates..." 或 "Derive the backwards pass..."
    
- **应对策略：**
    
    - **Forward Mode:** 定义 $v_i$ (值) 和 $\dot{v}_i$ (导数)。对于乘法 $v_3 = v_1 v_2$，导数更新为 $\dot{v}_3 = \dot{v}_1 v_2 + v_1 \dot{v}_2$。
        
    - **Reverse Mode:** 定义伴随 $\bar{v}_i$。注意如果一个节点输出给多个子节点，反向传播时梯度要 **相加 (Sum)** 11。
        

#### 形式三：理论证明 (Theoretical Proof)

- **典型问法：** 关于模型架构的性质（如 2024 年的 Deep Linear Network）。
    
- **应对策略：** 利用矩阵结合律 $(AB)C = A(BC)$ 证明多层矩阵相乘可以坍缩为一个矩阵。
    

---

### 3. 复习建议 (Summary for Revision)

1. **熟练绘制计算图：** 找几个复杂的数学公式（包含 $\exp, \log, \text{trace}, \det$ 等），练习把它们拆解成计算图。
    
2. **牢记效率准则：**
    
    - **Forward Mode:** Cost $\propto$ Inputs. Good for $f: \mathbb{R} \to \mathbb{R}^N$.
        
    - **Reverse Mode:** Cost $\propto$ Outputs. Good for $f: \mathbb{R}^N \to \mathbb{R}$ (Machine Learning!).
        
3. **区分数学求导与自动微分：** 考试如果问 "Compute the gradient"，通常是用矩阵微积分（L2/L3内容）；如果问 "Derive the backward pass" 或涉及 "Computational Graph"，则是考自动微分（L4内容），需要按步骤写出中间变量的导数更新，而不是直接写最终结果。
    
4. **注意矩阵运算的反向传播：** 2022年考到了矩阵逆 ($X^{-1}$) 和 Cholesky 分解的导数。复习讲义中关于矩阵操作的梯度传递规则（如 Trace 的导数、逆的导数）12。

***
***
### 1.计算图与微分

**计算图**

* **绘制**：会画复杂数学表达式的计算图，将其分解为基本运算构成的DAG
* **计算**：会计算前向和反向模式的中间和最终结果
* **效率分析**：会分析前向与反向传播的效率差别
* **应用场景**：理解何时选择前/反向模式

**微分**

* **链式法则**： 会使用雅可比矩阵的乘积表示总导数
* **导数维度**： 会计算梯度和雅可比矩阵等导数形式的维度
* **索引模式运算**：会将矩阵乘法写成元素求和形式
* **索引模式求导**：会使用索引符号计算具体导数

### 2.深度学习与线性模型

**激活函数的意义**

* 证明多个仿射变换（y=Wx+b）的复合本身就是一个单一的仿射变换，即没有激活函数的深度学习模型是一个线性模型
