### **1. Introduction: From MC to TD**

- **Recap (回顾):** Monte Carlo (MC) methods learn from complete episodes. They are unbiased but have high variance and cannot learn online (step-by-step) 1111.
    
- **Temporal Difference (TD) Learning (时序差分学习):**
    
    - **Best of Both Worlds (两全其美):** TD combines the sampling of MC with the bootstrapping of Dynamic Programming (DP)2222.
        
    - **Core Idea (核心思想):** Learn value functions by bootstrapping from current estimates. The update is based on the difference between successive predictions 3.
        
    - **Update Rule (更新规则):** $\text{New Estimate} = \text{Old Estimate} + \text{StepSize} \times [\text{Target} - \text{Old Estimate}]$4.
        
    - **Key Characteristics (关键特征):** Model-free (no environment model needed), Online (updates after every step), and Bootstrapping (uses current estimates to improve future ones) 5555.
        

### **2. TD(0) for Policy Evaluation (Prediction)**

### **(2. 用于策略评估（预测）的 TD(0))**

- **TD Error ($\delta_t$) (TD 误差):** Measures the difference between the current estimate and the "better" estimate (reward + discounted future value)6666.
    
    - **Formula:** $\delta_t = [R_{t+1} + \gamma V(S_{t+1})] - V(S_t)$.
        
    - **Interpretation:** If $\delta_t > 0$, we underestimated $V(S_t)$; if $\delta_t < 0$, we overestimated it.
        
- **TD(0) Update Rule (更新规则):**
    
    - $V(S_t) \leftarrow V(S_t) + \alpha [R_{t+1} + \gamma V(S_{t+1}) - V(S_t)]$.
        
    - **TD Target:** $R_{t+1} + \gamma V(S_{t+1})$ is the target we move towards10101010.
        
- **Comparison (对比):**
    
    - **MC Target:** $G_t$ (Actual return). Unbiased but high variance.
        
    - **TD Target:** $R_{t+1} + \gamma V(S_{t+1})$ (Estimated return). Biased (initially) but low variance.
        
    - TD allows learning from incomplete episodes and is often faster.
        

### **3. From Prediction to Control**

### **(3. 从预测到控制)**

- **Problem (问题):** Knowing state values $V^\pi(s)$ isn't enough for control without a model (we don't know which action leads to better states).
    
- **Solution (解决方案):** Learn **action values** $Q^\pi(s, a)$ directly.
    
- **Exploration vs. Exploitation (探索与利用):**
    
    - **On-policy:** Learn about the policy currently being followed (e.g., SARSA).
        
    - **Off-policy:** Learn about a different policy (e.g., Optimal Policy) than the one generating data (e.g., Q-Learning).
        

### **4. SARSA: On-Policy TD Control**

### **(4. SARSA：同策略 TD 控制)**

- **Name Origin (名称由来):** **S**tate - **A**ction - **R**eward - **S**tate - **A**ction ($S_t, A_t, R_{t+1}, S_{t+1}, A_{t+1}$)16.
    
- **Update Rule (更新规则):**
    
    - $Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha [R_{t+1} + \gamma Q(S_{t+1}, A_{t+1}) - Q(S_t, A_t)]$.
        
- **Algorithm (算法流程):**
    
    1. Take action $A_t$, observe $R_{t+1}, S_{t+1}$.
        
    2. Choose next action $A_{t+1}$ using the **same** policy (e.g., $\epsilon$-greedy).
        
    3. Update $Q$ using the actual next action $A_{t+1}$ .
        
- **Properties (性质):** It learns the value of the _current_ exploration policy. It is "safe" (e.g., in Cliff Walking, it learns a safer path to avoid falling due to random exploration) .
    

### **5. Q-Learning: Off-Policy TD Control**

### **(5. Q-Learning：异策略 TD 控制)**

- **Core Insight (核心洞察):** Learn the optimal Q-function $Q^*$ directly, regardless of the policy being followed.
    
- **Update Rule (更新规则):**
    
    - $Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha [R_{t+1} + \gamma \max_a Q(S_{t+1}, a) - Q(S_t, A_t)]$.
        
- **Key Difference (关键区别):**
    
    - It uses the **best possible action** ($\max_a$) for the target, not the action actually taken.
        
    - "What would happen if I acted optimally from now on?" vs SARSA's "What would happen if I keep following my current policy?" .
        
- **Properties (性质):** Converges to the optimal policy. In the Cliff Walking example, it learns the optimal (risky) path because it ignores the exploration noise in its updates.
    

### **6. Expected SARSA**

### **(6. 期望 SARSA)**

- **Motivation (动机):** SARSA's target has high variance because it depends on the random selection of the next action $A_{t+1}$.
    
- **Idea (思路):** Instead of sampling the next action, use the **expected value** over all possible next actions.
    
- **Update Rule (更新规则):**
    
    - $Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha [R_{t+1} + \gamma \sum_a \pi(a|S_{t+1}) Q(S_{t+1}, a) - Q(S_t, A_t)]$.
        
- **Advantages (优势):** Removes variance from action selection, more stable, often faster convergence.
    

### **7. Double Learning (Addressing Maximization Bias)**

### **(7. 双重学习（解决最大化偏差）)**

- **The Problem (问题):** Q-Learning's `max` operator introduces **Maximization Bias**.
    
    - Because estimates are noisy, $\mathbb{E}[\max(\text{estimates})] > \max(\text{true values})$. This makes the agent overly optimistic about values, potentially leading to poor policies.
        
- **The Solution: Double Q-Learning (解决方案：双重 Q-Learning)**
    
    - Use **two independent** Q-functions, $Q_1$ and $Q_2$.
        
    - Use $Q_1$ to **select** the best action: $A^* = \operatorname{argmax}_a Q_1(s, a)$.
        
    - Use $Q_2$ to **evaluate** that action: Value $= Q_2(s, A^*)$.
        
    - Since selection and evaluation are decoupled, the bias is eliminated.
        

### **Summary of Algorithms (算法总结)**

| **Algorithm (算法)** | **Type (类型)**              | **Target (目标值)**                           |
| ------------------ | -------------------------- | ------------------------------------------ |
| **TD(0)**          | Prediction (预测)            | $R + \gamma V(S')$                         |
| **SARSA**          | On-policy Control (同策略控制)  | $R + \gamma Q(S', A')$ (Actual action)     |
| **Q-Learning**     | Off-policy Control (异策略控制) | $R + \gamma \max_a Q(S', a)$ (Best action) |
| **Expected SARSA** | On/Off-policy Control      | $R + \gamma \sum \pi(a\|S')Q(S',a)$        |
