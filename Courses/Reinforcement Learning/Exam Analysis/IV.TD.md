### **1. 算法公式识别与对比 (Algorithm Identification & Comparison)**

**考察内容：**

- **核心公式辨析：** 考试经常直接给出不同的更新公式，要求你识别它是哪种算法。
    
    - **TD(0):** $V(S) \leftarrow V(S) + \alpha [R + \gamma V(S') - V(S)]$ 1。
        
    - **SARSA:** 使用实际采取的下一个动作 $A'$ 更新：$Q(S,A) \leftarrow \dots + \alpha [R + \gamma Q(S',A') - Q(S,A)]$ 2。
        
    - **Q-learning:** 使用下一个状态的最大值更新：$Q(S,A) \leftarrow \dots + \alpha [R + \gamma \max_a Q(S',a) - Q(S,A)]$ 3。
        
    - **Expected SARSA:** 使用下一个状态的期望值更新：$Q(S,A) \leftarrow \dots + \alpha [R + \gamma \sum \pi(a|S')Q(S',a) - Q(S,A)]$ 4。
        
- **Double Learning (双重学习):** 识别其更新规则（使用两个独立的估计 $Q_1, Q_2$，一个用于选动作，一个用于评估），并理解其目的是为了解决**最大化偏差 (Maximization Bias)** 5。
    

**考察形式：**

- **多项选择题 (MCQ):**
    
    - **2021-2022 Q1a:** 列出四个公式，问哪些是 TD 更新、哪些使用了自举（Bootstrapping）6。
        
    - **2021-2022 Q1b:** 给出 Expected SARSA 的公式，问它与标准 Q-learning 相比有什么特点（如减少方差）7。
        
    - **2021-2022 Q1c:** 给出 Double Q-learning 的伪代码（以 0.5 概率更新 Q1 或 Q2），考察其内存需求（双倍）和计算量 8。
        

### **2. 手动计算 TD 更新 (Manual Calculation of TD Updates)**

**考察内容：**

- **数值计算：** 给定当前的价值估计 $V(s)$ 或 $Q(s,a)$、学习率 $\alpha$、折扣因子 $\gamma$ 以及一条简短的轨迹（或单步转移），计算更新后的价值。
    
- **TD 误差 (TD Error):** 计算 $\delta_t = R_{t+1} + \gamma V(S_{t+1}) - V(S_t)$ 9。
    

**考察形式：**

- **计算题 / 简答题:**
    
    - **2024-2025 Q2a(iii):** 给定当前估计 $V(s_1)=1, V(s_2)=-1$，观察到转移 $(s_1, r=1, s_2)$，要求计算 $\alpha=0.1$ 时的 $V(s_1)$ 更新值 10。
        
    - **2023-2024 Q2b:** 给定一个序列 $S_2, S_2, S_1, S_2, S_3$（其中 $S_3$ 终止），初始值为 0，$\alpha=0.5$，要求计算序列结束后的各状态价值 11。这考察了对 TD 逐步更新特性的掌握。
        

### **3. 算法性质与理论分析 (Theoretical Properties)**

**考察内容：**

- **On-policy vs Off-policy:**
    
    - SARSA 是 On-policy，因为它更新的值依赖于行为策略选择的 $A'$ 12。
        
    - Q-learning 是 Off-policy，因为它直接学习最优值 $Q^*$（通过 max 操作），而不关心行为策略是什么 13。
        
- **收敛性 (Convergence):**
    
    - **2020-2021 Q1e:** 考察 SARSA 收敛到最优策略的条件（如学习率 $\alpha$ 需满足 Robbins-Monro 条件：$\sum \alpha_t = \infty, \sum \alpha_t^2 < \infty$，以及所有状态需被无限次访问）14。
        
- **TD vs MC (收敛速度):**
    
    - **2022-2023 Q2b:** 再次提到这个经典考题。在特定奖励设置下（确定性 vs 随机），分析 TD(0) 和 MC 谁收敛更快。TD 通常在初期收敛更快，且对方差更鲁棒 15。
        

### **4. 偏差与方差 (Bias and Variance)**

**考察内容：**

- **Bootstrapping 的影响：** TD 使用自举（即用估计更新估计），这引入了**偏差 (Bias)**，但也显著降低了**方差 (Variance)**（相比于 MC）。
    
- **Off-policy 的挑战：** 纯 Off-policy 方法结合 Bootstrapping 和函数逼近（Function Approximation）时可能会发散（著名的“死亡三角” Triad），虽然这是 Lecture 4 的延伸，但理解 Q-learning 的 Off-policy 性质是基础 16。
    

**考察形式：**

- **多项选择题:**
    
    - **2024-2025 Q1d:** 考察关于自举值 $\hat{V}_{TD}$ 的期望和方差的数学性质 17。
        
    - **2024-2025 Q1e:** 问“为什么 Q-learning 被认为是 Off-policy 算法？”（答案：因为它使用一个策略产生的奖励来更新，但旨在学习另一个最优策略）18。
        

### **备考建议 (针对 Lecture 4)**

1. **背诵并区分三个公式：** 闭眼都能写出 SARSA、Q-learning 和 Expected SARSA 的更新公式。注意 max 和 sum 的区别。
    
2. **计算必练：** 找一道像 23/24 Q2b 那样的序列更新题，手动算一遍。注意：TD 是**每一步**都更新，后一步用到的 V 值是**前一步更新后**的值（如果是 Online 更新）。
    
3. **理解 Double Q-learning 的初衷：** 记住“最大化偏差”(Maximization Bias) 这个词，这是 Q-learning 的固有缺陷（因噪声导致高估），Double Learning 通过解耦“选择”和“评估”来解决它。
    
4. **On/Off-policy 判定标准：** 看更新公式里的 Target 是来自于“采样”（即行为策略产生的 $A_{t+1}$，如 SARSA）还是来自于“推断/最大化”（如 Q-learning 的 $\max Q$）。












***
***
old version
### 考点1 时序差分性质

**无偏性**

* 不使用$\epsilon$-greedy策略的TD(0) 不会引入偏差

**方差**

* TD的整体方差与单步方差和MC方差的对比

### 考点2 TD相关计算

**TD目标与TD误差计算**

* 会计算TD目标与TD误差

**TD更新计算**

* 会计算使用TD(0)更新的状态价值

**更新公式**

* 会所有TD算法的状态/动作价值更新公式

### 考点3 SARSA

**定义**

* 能从伪代码分辨出是不是SARSA

**性质**

* on-policy

**期望SARSA**

* 理解SARSA和期望SARSA
* 会比较SARSA和期望SARSA的计算量和方差

### 考点4 Q-Learning

**性质**

* Q-Learning为什么是off-policy

**Double Q-learning**

* 理解Double Q-Learning的原理
* 理解Double Q-Learning的计算消耗
* 理解Double Q-Learning的存储消耗
### 考点5 收敛性分析

**收敛速度**

* 会对比与MC的收敛速度

### 考点6 偏差与方差

**影响**

* 方差和偏差对TD(0)方法收敛性的影响